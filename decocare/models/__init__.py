
from decocare import commands, history, cgm
from decocare import lib
import types

class Task (object):
  def __init__ (self, msg, handler=None, **kwargs):
    self.msg = msg
    if handler:
      self.func = handler
  def __get__ (self, obj, objtype=None):
    if obj is None:
      return self
    else:
      return types.MethodType(self, obj)
  @staticmethod
  def func (self, response):
    return response.getData( )
  def __call__ (self, inst, **kwds):
    # print "__calll__", inst, self.func
    # self.func( )
    self.response = inst.session.query(self.msg, **kwds)
    return types.MethodType(self.func, inst)(self.response)
    # return self.response.getData( )

  @classmethod
  def handler (klass, msg, **kwargs):
    def closure (func):
      return Task(msg, handler=func, **kwargs)
    return closure

class Cursor (object):
  # Info
  # Page
  def __init__ (self, inst, **kwds):
    self.inst = inst
    self.kwds = kwds
  def get_page_info (self):
    self.info = self.inst.session.query(self.Info)
  def download_page (self, num):
    page = self.inst.session.query(self.Page, page=num)
    for record in self.find_records(page):
      yield record
  def range (self, info):
    raise NotImplemented( )
  def find_records (self, response):
    raise NotImplemented( )
  def iter (self):
    self.get_page_info( )
    for n in self.range(self.info.getData( )):
      yield self.download_page(n)

class PageIterator (Task):

  def __init__ (self, Cursor=None, handler=None):
    self.Cursor = Cursor
    if handler:
      self.func = handler

  def __call__ (self, inst, **kwds):
    self.pager = self.Cursor(inst, **kwds)
    for page in self.pager.iter( ):
      for record in page:
        yield record

  @classmethod
  def handler (klass, **kwargs):
    def closure (func):
      return klass(func, **kwargs)
    return closure


class PumpModel (object):
  bolus_strokes = 20
  basal_strokes = 40
  larger = False
  def __init__(self, model, session):
    self.model = model
    self.session = session

  read_status = Task(commands.ReadPumpStatus)
  read_temp_basal = Task(commands.ReadBasalTemp)
  read_settings = Task(commands.ReadSettings)
  read_reservoir = Task(commands.ReadRemainingInsulin)
  read_carb_ratios = Task(commands.ReadCarbRatios512)
  read_bg_targets = Task(commands.ReadBGTargets)
  read_insulin_sensitivies = Task(commands.ReadInsulinSensitivities)
  read_current_glucose_pages = Task(commands.ReadCurGlucosePageNumber)
  read_current_history_pages = Task(commands.ReadCurPageNumber)
  suspend_pump = Task(commands.PumpSuspend)
  resume_pump = Task(commands.PumpResume)
  read_battery_status = Task(commands.ReadBatteryStatus)


  def decode_unabsorbed (self, raw):
    doses = [ ]
    while raw and len(raw) > 2:
      head, tail = raw[:3], raw[3:]
      doses.append(self.decode_unabsorbed_component(*head) )
      raw = tail
    return doses

  def decode_unabsorbed_component (self, amount, age, _curve,strokes=40.0):
    curve = ((_curve & 0b110000) << 4)
    unabsorbed = { 'amount': amount/strokes,
                   'age': age + curve,
                   # 'curve': curve,
                 }
    return unabsorbed

  @PageIterator.handler( )
  class iter_glucose_pages (Cursor):
    Info = commands.ReadCurGlucosePageNumber
    Page = commands.ReadGlucoseHistory
    def range (self, info):
      start = int(info['page'])
      end = start - int(info['glucose'])
      return xrange(start, end, -1)
    def find_records (self, response):
      page = cgm.PagedData.Data(response.data, larger=self.inst.larger)
      return page.decode( )

  @PageIterator.handler( )
  class iter_history_pages (Cursor):
    Info = commands.ReadCurPageNumber
    Page = commands.ReadHistoryData
    def range (self, info):
      start = 0
      end = int(info)
      return xrange(start, end)
    def find_records (self, response):
      decoder = history.HistoryPage(response.data, self.inst)
      records = decoder.decode( )
      return records

  filter_glucose_date = Task(commands.FilterGlucoseHistory.ISO)
  filter_isig_date = Task(commands.FilterISIGHistory.ISO)

  @Task.handler(commands.ReadHistoryData)
  def read_history_data (self, response):
    decoder = history.HistoryPage(response.data, self)
    records = decoder.decode( )
    return records

  @Task.handler(commands.ReadGlucoseHistory)
  def read_glucose_data (self, response):
    records = [ ]
    page = cgm.PagedData.Data(response.data, larger=self.larger)
    records.extend(page.decode( ))
    return records

  @Task.handler(commands.ReadSettings)
  def my_read_settings (self, response):
    self.settings = response.getData( )
    return self.settings

  @Task.handler(commands.ReadRTC)
  def read_clock (self, response):
    clock = lib.parse.date(response.getData( ))
    return clock

  _set_temp_basal = Task(commands.TempBasal.Program)

  _bolus = Task(commands.Bolus)
  strokes_per_unit = 10
  def bolus (self, units=None, **kwds):
    params = self.fmt_bolus_params(units)
    program = dict(requested=dict(units=units, params=list(params)))
    results = self._bolus(params=params, **kwds)
    program.update(**results)
    program.update(**self.read_status( ))
    return program
  def fmt_bolus_params (self, units):
    strokes = int(float(units) * self.strokes_per_unit)
    if (self.larger or self.strokes_per_unit > 10):
      return [lib.HighByte(strokes), lib.LowByte(strokes)]
    return [strokes]

  def set_temp_basal (self, rate=None, duration=None, temp=None, **kwds):
    basals = dict(rate=rate, duration=duration, temp=temp)
    result = self._set_temp_basal(**basals)
    if not result.get('recieved'):
      result.update(requested=basals)
    result.update(**self.read_temp_basal( ))
    return result


class Model508 (PumpModel):
  old6cBody = 31
  pass

class Model511 (Model508):
  read_basal_profile_std = Task(commands.ReadProfiles511_STD)
  read_basal_profile_a = Task(commands.ReadProfiles511_A)
  read_basal_profile_b = Task(commands.ReadProfiles511_B)

  def read_selected_basal_profile (self, **kwds):
    settings = self.read_settings( )
    selected = settings['selected_pattern']
    patterns = {
        0 : self.read_basal_profile_std
      , 1 : self.read_basal_profile_a
      , 2 : self.read_basal_profile_b
      }
    return patterns[selected](**kwds)


class Model512 (Model511):
  read_basal_profile_std = Task(commands.ReadProfile_STD512)
  read_basal_profile_a = Task(commands.ReadProfile_A512)
  read_basal_profile_b = Task(commands.ReadProfile_B512)


class Model515 (Model512):
  read_bg_targets = Task(commands.ReadBGTargets515)
  pass

class Model522 (Model515):
  old6cBody = 38
  pass

class Model722 (Model522):
  pass

class Model523 (Model522):
  strokes_per_unit = 40
  larger = True
  read_carb_ratios = Task(commands.ReadCarbRatios)

class Model723 (Model523):
  pass

class Model530 (Model523):
  pass

class Model540 (Model530):
  pass

class Model554 (Model540):
  pass

known = {
  '508': Model508
, '511': Model511
, '512': Model512
, '515': Model515
, '522': Model522
, '523': Model523
, '530': Model530
, '540': Model540
, '554': Model554
, '722': Model722
, '723': Model723
}

def lookup (model, session):
  klass = known.get(model, PumpModel)
  return klass(model, session)

