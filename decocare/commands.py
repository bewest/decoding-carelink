
import logging
import time

import lib

class BadResponse (Exception):
  pass

"""

Implementation and decoding of lots of commands.

Each command inherits from :py:`BaseCommand`, which takes care of the
basic logic for informing the stick if we have recieved all the data
we expect to recieve.

Many commands are supported by Medtronic but not listed here.
Examples would include setting profiles and rates.
(One theory is that these commands are turned into setters with
correct arguments.)

"""

log = logging.getLogger( ).getChild(__name__)

def CRC8(data):
  return lib.CRC8.compute(data)

class BaseCommand(object):
  code    = 0x00
  descr   = "(error)"
  retries = 2
  timeout = 3
  params  = [ ]
  bytesPerRecord = 0
  maxRecords = 0
  effectTime = 0

  responded = False

  def __init__(self, code, descr, *args):
    self.code   = code
    self.descr  = descr
    self.params = [ ]

  def done(self):
    found = len(self.data or [ ])
    expect = int(self.maxRecords * self.bytesPerRecord)
    expect_size = "found[{}] expected[{}]".format(found, expect)
    log.info("%s:download:done?explain=%s" % (self, expect_size))
    return found >= expect
  def format(self):
    pass

  def respond(self, data):
    if getattr(self, 'data', None):
      self.data.extend(data)
    else:
      self.data = data
    self.getData( )
    self.responded = True

  def hexdump (self):
    return lib.hexdump(self.data)

class FieldChecker (object):
  def __init__ (self, msg, required=[]):
    self.msg = msg
    self.required = required

  def check_fields (self, data):
    for field in self.required:
      if field not in data:
        raise BadResponse( )
  def __call__ (self, data):
    self.msg.validate(data)
    self.check_fields(data)
    return True

class PumpCommand(BaseCommand):
  #serial = '665455'
  #serial = '206525'
  serial = '208850'

  params = [ ]
  bytesPerRecord = 64
  maxRecords = 1
  retries = 2
  effectTime = .500
  data = bytearray( )
  Validator = FieldChecker
  output_fields = [ ]
  __fields__ = ['maxRecords', 'code', 'descr',
                'serial', 'bytesPerRecord', 'retries', 'params']
  def __init__(self, **kwds):
    for k in self.__fields__:
      value = kwds.get(k, getattr(self, k))
      setattr(self, k, value)
    self.allocateRawData( )
    self.data = bytearray( )
    self.name = self.log_name( )
    self.checker = self.Validator(self, required=self.output_fields)

  def log_name(self, prefix=''):
    return prefix + '{}.data'.format(self.__class__.__name__)

  def save(self, prefix=''):
    name = '{}'.format(self.log_name(prefix))
    handle = open(name, 'wb')
    handle.write(self.data)
    handle.close( )

  def __str__(self):
    if self.responded:
      return '{}:size[{}]:data:{}'.format(self.__class__.__name__,
                                          self.size, repr(self.getData( )))
    return '{}:data:unknown'.format(self.__class__.__name__)

  def __repr__(self):
    return '<{0}>'.format( self)

  def validate (self, data):
    return True
  def check_output (self, data):
    return self.checker(data)

  def getData(self):
    return self.data

  def allocateRawData(self):
    self.size = self.bytesPerRecord * self.maxRecords

  def format(self):
    params = self.params
    code   = self.code
    maxRetries = self.retries
    serial = list(bytearray(self.serial.decode('hex')))
    paramsCount = len(params)
    head   = [ 1, 0, 167, 1 ]
    # serial
    packet = head + serial
    # paramCount 2 bytes
    packet.extend( [ (0x80 | lib.HighByte(paramsCount)),
                             lib.LowByte(paramsCount) ] )
    # not sure what this byte means
    button = 0
    # special case command 93
    if code == 93:
      button = 85
    packet.append(button)
    packet.append(maxRetries)
    # how many packets/frames/pages/flows will this take?
    responseSize = self.calcRecordsRequired()
    # really only 1 or 2?
    pages = responseSize
    if responseSize > 1:
      pages = 2
    packet.append(pages)
    packet.append(0)
    # command code goes here
    packet.append(code)
    packet.append(CRC8(packet))
    packet.extend(params)
    packet.append(CRC8(params))
    log.debug(packet)
    return bytearray(packet)

  def calcRecordsRequired(self):
    length = self.bytesPerRecord * self.maxRecords
    i = length / 64
    j = length % 64
    if j > 0:
      return i + 1
    return i

class ManualCommand(PumpCommand):
  def __init__(self, **kwds):
    self.name = kwds.get('name', self.__class__.__name__)
    super(type(self), self).__init__(**kwds)
    self.kwds = kwds
    self.name = kwds.get('name', self.__class__.__name__)
  def __str__(self):
    if self.responded:
      return '{}:{}:size[{}]:'.format(self.name, self.kwds,
                                      self.size)
    return '{}:{}:data:unknown'.format(self.name, self.kwds)

  def log_name(self, prefix=''):
    return prefix + '{}.data'.format(self.name)
  def __repr__(self):
    return '<{0}>'.format(self)

  def getData(self):
    return self.hexdump( )

class PowerControl(PumpCommand):
  """
    >>> PowerControl(serial='665455').format() == PowerControl._test_ok
    True
  """
  _test_ok = bytearray( [ 0x01, 0x00, 0xA7, 0x01, 0x66, 0x54, 0x55, 0x80,
                          0x02, 0x55, 0x00, 0x00, 0x00, 0x5D, 0xE6, 0x01,
                          0x0A, 0xA2 ] )
  code = 93
  descr = "RF Power On"
  params = [ 0x01, 0x0A ]
  retries = 0
  maxRecords = 0
  #timeout = 1
  # effectTime = 7
  effectTime = 12
  def __init__(self, minutes=None, **kwds):
    if minutes is not None:
      self.minutes = int(minutes)
      kwds['params'] = [ 0x01, self.minutes ]
    super(PowerControl, self).__init__(**kwds)

class PowerControlOff(PowerControl):
  """
  Here's an example where arguments clearly modify behavior.
  """
  params = [ 0x00, 0x00 ]

# MMPump???/	CMD_????????	69	0x45	('E')	??
class PumpExperiment_OP69 (PumpCommand):
  code = 69

# MMPump???/	CMD_????????	70	0x46	('F')	??
class PumpExperiment_OP70 (PumpCommand):
  code = 70

# MMPump???/	CMD_????????	71	0x47	('G')	??
class PumpExperiment_OP71 (PumpCommand):
  code = 71

# MMPump???/	CMD_????????	72	0x48	('H')	??
class PumpExperiment_OP72 (PumpCommand):
  code = 72

# MMPump???/	CMD_????????	73	0x49	('I')	??
class PumpExperiment_OP73 (PumpCommand):
  code = 73

# MMPump???/	SelectBasalProfile	74	0x4a	('J')	OK
class SelectBasalProfile (PumpCommand):
  code = 74

class SelectBasalProfileSTD (SelectBasalProfile):
  params = [ 0 ]

class SelectBasalProfileA (SelectBasalProfile):
  params = [ 1 ]

class SelectBasalProfileB (SelectBasalProfile):
  params = [ 2 ]

# MMPump???/	CMD_????????	75	0x4b	('K')	??
class PumpExperiment_OP75 (PumpCommand):
  code = 75

class TempBasal(PumpCommand):
  """

  """

  code = 76
  descr = "Set temp basal"
  params = [ 0x00, 0x00, 0x00 ]
  retries = 0
  #maxRecords = 0
  #timeout = 1

  def getData(self):
    status = { 0: 'absolute' }
    received = True if (len(self.data) > 0 and self.data[0] is 0) else False
    return dict(recieved=received, temp=status.get(self.params[0], 'percent'))
  @classmethod
  def Program (klass, rate=None, duration=None, temp=None, **kwds):
    assert duration % 30 is 0, "duration {0} is not a whole multiple of 30".format(duration)
    assert temp in [ 'percent', 'absolute' ], "temp field <{0}> should be one of {1}".format(temp, ['percent', 'absolute' ])
    if temp in [ 'percent' ]:
      return TempBasalPercent(params=klass.format_percent_params(rate, duration), **kwds)

    return klass(params=klass.format_params(rate, duration), **kwds)
  @classmethod
  def format_percent_params (klass, rate, duration):
    duration = int(duration / 30)
    rate = int(rate)
    params = [rate, duration]
    return params

  @classmethod
  def format_params (klass, rate, duration):
    duration = duration / 30
    rate = int(rate / 0.025)
    params = [0x00, rate, duration]
    return params



class SetSuspend(PumpCommand):
  code = 77
  descr = "Set Pump Suspend/Resume status"
  params = [ ]
  retries = 2
  maxRecords = 1
  def getData(self):
    status = { 0: 'resumed', 1: 'suspended' }
    received = True if self.data[0] is 0 else False
    return dict(recieved=received, status=status.get(self.params[0]))

class PumpSuspend(SetSuspend):
  descr = "Suspend pump"
  params = [ 1 ]

class PumpResume(SetSuspend):
  descr = "Resume pump (cancel suspend)"
  params = [ 0 ]

class SetAutoOff (PumpCommand):
  code = 78
  maxRecords = 0

class SetEnabledEasyBolus (PumpCommand):
  code = 79
  maxRecords = 0

class SetBasalType (PumpCommand):
  code = 104

class TempBasalPercent (TempBasal):
  """

  """

  code = 105
  descr = "Set temp basal by percent"
  params = [ 0x00, 0x00 ]
  retries = 0
  #maxRecords = 0
  #timeout = 1

class KeypadPush(PumpCommand):
  code = 91
  descr = "Press buttons on the keypad"
  params = [ ]
  retries = 1
  maxRecords = 0

  @classmethod
  def ACT(klass, **kwds):
    return klass(params=[0x02], **kwds)

  @classmethod
  def ESC(klass, **kwds):
    return klass(params=[0x01], **kwds)

  @classmethod
  def DOWN(klass, **kwds):
    return klass(params=[0x04], **kwds)

  @classmethod
  def UP(klass, **kwds):
    return klass(params=[0x03], **kwds)

  @classmethod
  def EASY(klass, **kwds):
    return klass(params=[0x00], **kwds)

def PushACT (**kwds):
  return KeypadPush.ACT(**kwds)

def PushESC (**kwds):
  return KeypadPush.ESC(**kwds)

def PushDOWN (**kwds):
  return KeypadPush.DOWN(**kwds)

def PushUP (**kwds):
  return KeypadPush.UP(**kwds)

def PushEASY (**kwds):
  return KeypadPush.EASY(**kwds)


class ReadErrorStatus508 (PumpCommand):
  """

  """
  code = 38
  descr = "error status"
  params = [ ]

class ReadBolusHistory (PumpCommand):
  """

  """
  code = 39
  descr = "bolus history"
  params = [ ]

class ReadDailyTotals (PumpCommand):
  """

  """
  code = 40
  descr = "..."
  params = [ ]

class ReadPrimeBoluses (PumpCommand):
  """

  """
  code = 41
  descr = "..."
  params = [ ]

class ReadAlarms (PumpCommand):
  """

  """
  code = 42
  descr = "..."
  params = [ ]

class ReadProfileSets (PumpCommand):
  """

  """
  code = 43
  descr = "..."
  params = [ ]

class ReadUserEvents (PumpCommand):
  """

  """
  code = 44
  descr = "..."
  params = [ ]

class ReadRemoteControlID (PumpCommand):
  """

  """
  code = 46
  descr = "..."
  params = [ ]

class Read128KMem (PumpCommand):
  """

  """
  code = 55
  descr = "..."
  params = [ ]

class Read256KMem (PumpCommand):
  """

  """
  code = 56
  descr = "..."
  params = [ ]

class Bolus (PumpCommand):
  """
  Bolus some insulin.

  XXX: Be careful please.
  Best trying this not connected to the pump until you trust it.
  """
  code = 66
  descr = "Bolus"
  params = [ ]
  def getData(self):
    received = True if self.data[0] is 0x0c else False
    return dict(recieved=received, _type='BolusRequest')


class ReadErrorStatus(PumpCommand):
  """
    >>> ReadErrorStatus(serial='665455').format() == ReadErrorStatus._test_ok
    True
  """
  _test_ok = bytearray([ 0x01, 0x00, 0xA7, 0x01, 0x66, 0x54, 0x55, 0x80,
                         0x00, 0x00, 0x02, 0x01, 0x00, 0x75, 0xD7, 0x00 ])
  code = 117
  descr = "Read Error Status any current alarms set?"
  params = [ ]
  retries = 2
  maxRecords = 1

class ReadHistoryData(PumpCommand):
  """
    >>> ReadHistoryData(serial='208850', params=[ 0x03 ]).format() == ReadHistoryData._test_ok
    True
    >>> ReadHistoryData(params=[ 0x01 ]).params
    [1]
    >>> ReadHistoryData(params=[ 0x02 ]).params
    [2]
    >>> ReadHistoryData(params=[ 0x03 ]).params
    [3]
    >>> ReadHistoryData(page=0x01).params
    [1]
    >>> ReadHistoryData(page=0x02).params
    [2]
    >>> ReadHistoryData(page=0x03).params
    [3]
  """
  __fields__ = PumpCommand.__fields__ + ['page']
  _test_ok = bytearray([ 0x01, 0x00, 0xA7, 0x01, 0x20, 0x88, 0x50, 0x80, 0x01, 0x00, 0x02, 0x02, 0x00, 0x80, 0x9B, 0x03, 0x36, ])

  page = None
  def __init__(self, page=None, **kwds):
    if page is None and kwds.get('params', [ ]):
      page = kwds.pop('params')[0] or 0

    if page is not None:
      self.page = int(page)
      kwds['params'] = [ self.page ]
    super(ReadHistoryData, self).__init__(**kwds)

  def log_name(self, prefix=''):
    return prefix + '{}-page-{}.data'.format(self.__class__.__name__, self.page)

  def __str__(self):
    base = ''.join([ self.__class__.__name__,
                    ':size[%s]:' % self.size,
                    '[page][%s]' % self.page ])
    return '{}:data[{}]:'.format(base, len(self.data))

  def done(self):
    eod = False
    found = len(self.data or [ ])
    expect = int(self.maxRecords * self.bytesPerRecord)
    expect_crc = CRC8(self.data[:-1])
    expect_size = "size check found[{}] expected[{}]".format(found, expect)
    found_crc = 0
    if self.responded and len(self.data) > 5:
      found_crc = self.data[-1]
      self.eod  = eod = (self.data[5] & 0x80) > 0
    explain_crc = "CRC ACK check found[{}] expected[{}]".format(found_crc, expect_crc)
    is_eod = 'and has eod set? %s' % (eod)
    log.info("%s:download:done %s:%s:%s" % (self, expect_size, explain_crc, is_eod))
    return found >= expect

  def respond(self, raw):
    log.info('{} extending original {} with found {}'.format(str(self), len(self.data), len(raw)))
    if len(raw) == self.size:
      log.info('{} download respond replace original {} with found {}'.format(str(self), len(self.data), len(raw)))
      self.data = raw
    elif len(self.data) == self.size:
      log.info('{} download respond original {}, XXX IGNORE found {}'.format(str(self), len(self.data), len(raw)))
      pass
    else:
      log.info('{} download respond extend original {} with found {}'.format(str(self), len(self.data), len(raw)))
      self.data.extend(raw)
    self.responded = True

  code = 128
  descr = "Read History Data"
  params = [ ]
  retries = 2
  maxRecords = 16
  effectTime = .100
  data = bytearray( )

  def getData(self):
    data = self.data
    # log.info("XXX: READ HISTORY DATA!!:\n%s" % lib.hexdump(data))
    return self.hexdump( )

class ReadCurPageNumber(PumpCommand):
  """
  """

  code = 157
  descr = "Read Cur Page Number"
  params = [ ]
  retries = 2
  maxRecords = 1
  pages = 'unknown'

  def __str__(self):
    return ':pages:'.join([self.__class__.__name__, str(self.pages) ])

  def respond(self, data):
    self.data = data
    self.pages = self.getData( )
    self.responded = True
  def getData(self):
    data = self.data
    log.info("XXX: READ cur page number:\n%s" % lib.hexdump(data))
    # MM12 does not support this command, but has 31 pages
    # Thanks to @amazaheri
    page = 32
    if len(data) == 1:
      return int(data[0])
    if len(data) > 3:
      page = lib.BangLong(data[0:4])
    # https://bitbucket.org/bewest/carelink/src/419fbf23495a/ddmsDTWApplet.src/minimed/ddms/deviceportreader/MMX15.java#cl-157
    if page <= 0 or page > 36:
      page = 36
    return page


# MMX22/	CMD_READ_CURRENT_GLUCOSE_HISTORY_PAGE_NUMBER	205	0xcd	('\xcd')	OK
class ReadCurGlucosePageNumber(PumpCommand):
  """
  """

  code = 205
  descr = "Read Cur Glucose Page Number"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    log.info("XXX: READ cur page number:\n%s" % lib.hexdump(data))
    if len(data) == 1:
      return int(data[0])
    return dict(page= lib.BangLong(data[0:4]), glucose=data[5], isig=data[7])


class ReadRTC(PumpCommand):
  """
  """

  code = 112
  descr = "Read RTC"
  params = [ ]
  retries = 2
  maxRecords = 1


  def getData(self):
    data = self.data
    d = {
      'hour'  : int(data[0]),
      'minute': int(data[1]),
      'second': int(data[2]),
      # XXX
      'year'  : lib.BangInt([data[3], data[4]]),
      'month' : int(data[5]),
      'day'   : int(data[6]),
    }
    return "{year:#04}-{month:#02}-{day:#02}T{hour:#02}:{minute:#02}:{second:#02}".format(**d)

class SetRTC (PumpCommand):
  """
  Set clock
  """
  code = 64
  descr = "Set RTC"
  retries = 2
  maxRecords = 0

  __fields__ = PumpCommand.__fields__ + ['clock']
  def __init__(self, clock=None, **kwds):
    params = kwds.get('params', [ ])
    self.clock = kwds.get('clock', None)
    if len(params) == 0:
      params.extend(SetRTC.fmt_datetime(clock))

    kwds['params'] = params
    super(SetRTC, self).__init__(**kwds)
  @classmethod
  def fmt_datetime (klass, dt):
    return [dt.hour, dt.minute, dt.second, lib.HighByte(dt.year), lib.LowByte(dt.year), dt.month, dt.day]

class ReadPumpID(PumpCommand):
  """
  """

  code = 113
  descr = "Read Pump ID"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    return str(data[0:6])

class ReadBatteryStatus(PumpCommand):
  """
  """

  code = 114
  descr = "Read Battery Status"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    bd = bytearray(data)
    volt = lib.BangInt((bd[1], bd[2]))
    indicator = bd[0]
    battery = {'status': {0: 'normal', 1: 'low'}[indicator], 'voltage': volt/100.0 }
    return battery


class ReadFirmwareVersion(PumpCommand):
  """
  """

  code = 116
  descr = "Read Firmware Version"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    log.debug("READ FIRMWARE HEX:\n%s" % lib.hexdump(data))
    return str(data.split( chr(0x0b) )[0]).strip( )

class ReadRemainingInsulin(PumpCommand):
  """
  """

  code = 115
  descr = "Read Remaining Insulin"
  params = [ ]
  retries = 2
  maxRecords = 1
  basalStrokes = 10.0
  startByte = 0
  endByte = 2

  def getData(self):
    data = self.data
    log.info("READ remaining insulin:\n%s" % lib.hexdump(data))
    return lib.BangInt(data[self.startByte:self.endByte])/self.basalStrokes


class ReadRemainingInsulin523(ReadRemainingInsulin):
  """
  """

  basalStrokes = 40.0
  startByte = 2
  endByte = 4


class ReadBasalTemp508 (PumpCommand):
  """
  """

  code = 64
  descr = "Read Temp Basal 508 (old)"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    rate = lib.BangInt(data[2:4])/40.0
    duration = lib.BangInt(data[4:6])
    log.info("READ temporary basal:\n%s" % lib.hexdump(data))
    return { 'rate': rate, 'duration': duration }


class ReadTodayTotals508 (PumpCommand):
  """
  """

  code = 65
  descr = "Read Totals Today"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    log.info("READ totals today:\n%s" % lib.hexdump(data))
    totals = {
      'today': lib.BangInt(data[0:2]) / 10.0,
      'yesterday': lib.BangInt(data[2:4]) / 10.0
    }
    return totals

# MMPump511/	ReadTotalsToday	121	0x79	('y')	OK
class ReadTotalsToday(PumpCommand):
  """
  """

  code = 121
  descr = "Read Totals Today"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    log.info("READ totals today:\n%s" % lib.hexdump(data))
    totals = {
      'today': lib.BangInt(data[0:2]) / 10.0,
      'yesterday': lib.BangInt(data[2:4]) / 10.0
    }
    return totals

# MMPump511/	ReadProfiles_STD	122	0x7a	('z')	OK
class ReadProfiles511_STD (PumpCommand):
  code = 122
# MMPump511/	ReadProfiles_A	123	0x7b	('{')	??
class ReadProfiles511_A (PumpCommand):
  code = 123
# MMPump511/	ReadProfiles_B	124	0x7c	('|')	??
class ReadProfiles511_B (PumpCommand):
  code = 124
# MMPump???/	CMD_?????	125	0x7d	('}')	??
class Model511_ExperimentOP125 (PumpCommand):
  code = 125
# MMPump???/	CMD_?????	126	0x7e	('~')	??
class Model511_ExperimentOP126 (PumpCommand):
  code = 126
# MMPump511/	ReadSettings	127	0x7f	DEL
class ReadSettings511 (PumpCommand):
  code = 127

# MMX11/	CMD_ENABLE_DISABLE_DETAIL_TRACE	160	0x9f	('\x9f')	??
class PumpTraceSelect (PumpCommand):
  code = 160

class PumpEnableDetailTrace (PumpTraceSelect):
  params = [ 1 ]

class PumpDisableDetailTrace (PumpTraceSelect):
  params = [ 0 ]

class Experiment_OP161 (PumpCommand):
  code = 161

class Experiment_OP162 (PumpCommand):
  code = 162

# MMPump511/	ReadPumpTrace	163	0xa3	('\xa3')	??
class ReadPumpTrace (PumpCommand):
  code = 163
  maxRecords = 16
# MMPump511/	ReadDetailTrace	164	0xa4	('\xa4')	??
class ReadDetailTrace (PumpCommand):
  code = 164
  maxRecords = 16

# MMPump11??/	CMD_????????????	165	0xa5	0xa5	??
class Model511_Experiment_OP165 (PumpCommand):
  code = 165

# MMPump511/	ReadNewTraceAlarm	166	0xa6	('\xa6')	??
class ReadNewTraceAlarm (PumpCommand):
  code = 166
  maxRecords = 16

# MMPump511/	ReadOldTraceAlarm	167	0xa7	('\xa7')	??
class ReadOldTraceAlarm (PumpCommand):
  maxRecords = 16
  code = 167

# MMPump???/	CMD_?????	36	0x24	('$')	??
class PumpExperimentSelfCheck_OP36 (PumpCommand):
  code = 36

# MMX22/	CMD_WRITE_GLUCOSE_HISTORY_TIMESTAMP	40	0x28	('(')	??
class WriteGlucoseHistoryTimestamp (PumpCommand):
  code = 40

class ReadRadioCtrlACL(PumpCommand):
  """
  """

  code = 118
  descr = "Read Radio ACL"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    ids = [ ]
    ids.append( str(data[0:6]) )
    ids.append( str(data[6:12]) )
    ids.append( str(data[12:18]) )
    log.info("READ radio ACL:\n%s" % lib.hexdump(data))
    return ids

class Model511_Experiment_OP119 (PumpCommand):
  code = 119

class Model511_Experiment_OP120 (PumpCommand):
  code = 120

class Model511_Experiment_OP121 (PumpCommand):
  code = 121

class Model511_Experiment_OP122 (PumpCommand):
  code = 122

class Model511_Experiment_OP123 (PumpCommand):
  code = 123

class Model511_Experiment_OP124 (PumpCommand):
  code = 124

class Model511_Experiment_OP125 (PumpCommand):
  code = 125

class Model511_Experiment_OP126 (PumpCommand):
  code = 126

class Model511_Experiment_OP127 (PumpCommand):
  code = 127

class Model511_Experiment_OP128 (PumpCommand):
  code = 128

class Model511_Experiment_OP129 (PumpCommand):
  code = 129

class Model511_Experiment_OP130 (PumpCommand):
  code = 130

# MMPump512/	CMD_READ_LANGUAGE	134	0x86	('\x86')	??
class ReadLanguage (PumpCommand):
  code = 134
# MMPump512/	CMD_READ_BOLUS_WIZARD_SETUP_STATUS	135	0x87	('\x87')	??
class ReadBolusWizardSetupStatus (PumpCommand):
  code = 135

# MMPump512/	CMD_READ_CARB_UNITS	136	0x88	('\x88')	OK
class ReadCarbUnits (PumpCommand):
  code = 136
  def getData (self):
    labels = { 1 : 'grams', 2: 'exchanges' }
    return dict(carb_units=labels.get(self.data[0], self.data[0]))

# MMPump512/	CMD_READ_BG_UNITS	137	0x89	('\x89')	??
class ReadBGUnits (PumpCommand):
  code = 137
  def getData (self):
    labels = { 1 : 'mg/dL', 2: 'mmol/L' }
    return dict(bg_units=labels.get(self.data[0], self.data[0]))

# MMPump512/	CMD_READ_CARB_RATIOS	138	0x8a	('\x8a')	OK
class ReadCarbRatios512 (PumpCommand):
  code = 138
  output_fields = ['units', 'schedule' ]
  def getData (self):
    # return self.model.decode_carb_ratios(self.data[:])
    units = self.data[0]
    labels = { 1 : 'grams', 2: 'exchanges' }
    fixed = self.data[1]
    data = self.data[1:1+(8 *2)]
    return dict(schedule=self.decode_ratios(data[0:], units=units), units=labels.get(units), first=self.data[0], raw=' '.join('0x{:02x}'.format(x) for x in self.data))

  item_size = 2
  num_items = 8
  @classmethod
  def decode_ratios (klass, data, units=0):
    data = data[0:(8 *2)]
    schedule = [ ]
    for x in range(len(data)/ 2):
      start = x * 2
      end = start + 2
      (i, r) = data[start:end]
      if x > 0 and i == 0:
        break
      ratio = int(r)
      if units == 2:
        ratio = r / 10.0
      schedule.append(dict(x=x, i=i, start=lib.basal_time(i), offset=i*30, ratio=ratio, r=r))
    return schedule

class ReadCarbRatios (PumpCommand):
  code = 138
  item_size = 3
  num_items = 8
  output_fields = ['units', 'schedule' ]
  def getData (self):
    units = self.data[0]
    labels = { 1 : 'grams', 2: 'exchanges' }
    fixed = self.data[1]
    data = self.data[2:2+(fixed *3)]
    return dict(schedule=self.decode_ratios(data, units=units), units=labels.get(units), first=self.data[0])

  @classmethod
  def decode_ratios (klass, data, units=0):
    schedule = [ ]
    for x in range(len(data)/ 3):
      start = x * 3
      end = start + 3
      (i, q, r) = data[start:end]
      if x > 0 and i == 0:
        break
      ratio = r/10.0
      if q:
        ratio = lib.BangInt([q, r]) / 1000.0
      schedule.append(dict(x=x, i=i, start=lib.basal_time(i), offset=i*30, q=q, ratio=ratio, r=r))
    return schedule

# MMPump512/	CMD_READ_INSULIN_SENSITIVITIES	139	0x8b	('\x8b')	OK
class ReadInsulinSensitivities (PumpCommand):
  code = 139
  resp_1 = bytearray(b'\x01\x00-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
  resp_uk_1 = bytearray(str("""
02001600000000
00000000000000
00000000000000
00000000000000
00000000000000
00000000000000
00000000000000
00000000000000
""".strip( ).replace("\n", "").decode('hex')))

  output_fields = ['units', 'sensitivities' ]
  UNITS = {
    1: 'mg/dL',
    2: 'mmol/L'
  }
  def getData (self):
    # isFast = data[17] == 0
    isFast = self.data[0] is 1
    units = self.data[0]
    data = self.data[1:1+16]
    schedule = [ ]
    for x in range(8):
      start = x * 2
      end = start + 2
      (i, sensitivity) = data[start:end]
      if x > 0 and i == 0:
        break
      if units == 2:
        sensitivity = sensitivity / 10.0
      schedule.append(dict(x=x, i=i, start=lib.basal_time(i), offset=i*30, sensitivity=sensitivity))
    labels = { True: 'Fast', False: 'Regular' }
    return dict(sensitivities=schedule, first=self.data[0], units=self.UNITS.get(units))

# MMPump512/	CMD_READ_BG_TARGETS	140	0x8c	('\x8c')	??
class ReadBGTargets (PumpCommand):
  code = 140
class ReadBGTargets515 (PumpCommand):
  code = 159
  output_fields = ['units', 'targets' ]
  def getData (self):
    units = self.data[0]
    labels = { 1 : 'mg/dL', 2: 'mmol/L' }
    data = self.data[1:1+24]
    schedule = [ ]
    for x in range(8):
      start = x * 3
      end = start + 3
      (i, low, high) = data[start:end]
      if x > 0 and i == 0:
        break
      if units is 2:
        low = low / 10.0
        high = high / 10.0
      schedule.append(dict(x=x, i=i, start=lib.basal_time(i), offset=i*30, low=low, high=high))
    return dict(targets=schedule, units=labels.get(units), first=self.data[0], raw=' '.join('0x{:02x}'.format(x) for x in self.data))

# MMPump512/	CMD_READ_BG_ALARM_CLOCKS	142	0x8e	('\x8e')	??
class ReadBGAlarmCLocks (PumpCommand):
  code = 142
# MMPump512/	CMD_READ_RESERVOIR_WARNING	143	0x8f	('\x8f')	??
class ReadReservoirWarning (PumpCommand):
  code = 143
# MMPump512/	CMD_READ_BG_REMINDER_ENABLE	144	0x90	('\x90')	??
class ReadBGReminderEnable (PumpCommand):
  code = 144
# MMPump512/	CMD_READ_SETTINGS	145	0x91	('\x91')	??
class ReadSettings512 (PumpCommand):
  code = 145
# MMPump512/	CMD_READ_STD_PROFILES	146	0x92	('\x92')	??
class ReadProfile_STD512 (PumpCommand):
  """
    >>> import json
    >>> schedule = ReadProfile_STD512.decode(ReadProfile_STD512._test_result_1)
    >>> len(schedule)
    4
    >>> print json.dumps(schedule[0])
    {"i": 0, "start": "00:00:00", "rate": 0.8, "minutes": 0}
    >>> print json.dumps(schedule[1])
    {"i": 1, "start": "06:30:00", "rate": 0.9500000000000001, "minutes": 390}
    >>> print json.dumps(schedule[2])
    {"i": 2, "start": "09:30:00", "rate": 1.1, "minutes": 570}
    >>> print json.dumps(schedule[3])
    {"i": 3, "start": "14:00:00", "rate": 0.9500000000000001, "minutes": 840}

  """
  _test_result_1 = bytearray([
    32, 0, 0,
    38, 0, 13,
    44, 0, 19,
    38, 0, 28,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
  ])
  _test_schedule = {'total': 22.50, 'schedule': [
    { 'start': '12:00A', 'rate': 0.80 },
    { 'start': '6:30A', 'rate': 0.95 },
    { 'start': '9:30A', 'rate': 1.10 },
    { 'start': '2:00P', 'rate': 0.95 },
  ]}
  code = 146
  maxRecords = 2
  output_fields = [ ]
  def validate (self, data):
    i = 0
    valid = True
    last = None
    for profile in data:
      start = str(lib.basal_time(profile['minutes']/30))
      if 'rate' in profile and profile['i'] == i and start == profile['start']:
        if i == 0:
          if profile['minutes'] != 0:
            template = "{name} first scheduled item should be 00:00:00."
            msg = template.format(name=self.__class__.__name__)
            msg = "%s\n%s" % (msg, profile)
            raise BadResponse(msg)
        if last and profile['minutes'] <= last['minutes']:
          template = "{name} next scheduled item occurs before previous"
          msg = template.format(name=self.__class__.__name__)
          msg = "%s\n%s" % (msg, profile)
          raise BadResponse(msg)
      else:
        bad_profile = """Current profile: %s""" % (profile)
        template = """{bad_profile} Found in response to {name}
          i: {i} matches? {matches_i}
          our calcstart: {start}
          profile start: {profile_start}
          has a rate: {has_rate}
          start matches: {matches_start}
        """
        raise BadResponse(template.format(bad_profile=bad_profile
                  , name=self.__class__.__name__
                  , start=start
                  , profile_start=profile['start']
                  , has_rate= 'rate' in profile
                  , matches_i= profile['i'] == i
                  , matches_start=  start == profile['start']
                  , i=i))
        valid = False
      last = profile
      i = i + 1
    return True
  @staticmethod
  def decode (data):
    i = 0
    schedule = [ ]
    end = [ 0, 0, 0 ]
    none = [ 0, 0, 0x3F ]
    for i in xrange(len(data)/3):
      off = i*3
      r, z, m = data[off : off + 3]
      if [r,z,m] in [end, none]:
        break
      schedule.append(dict(i=i, minutes=m*30, start=str(lib.basal_time(m)), rate=r*.025))
    return schedule
  def getData (self):
    return self.decode(self.data)
# MMPump512/	CMD_READ_A_PROFILES	147	0x93	('\x93')	OK
class ReadProfile_A512 (ReadProfile_STD512):
  code = 147
# MMPump512/	CMD_READ_B_PROFILES	148	0x94	('\x94')	OK
class ReadProfile_B512 (ReadProfile_STD512):
  code = 148
# MMPump512/	CMD_READ_LOGIC_LINK_IDS	149	0x95	('\x95')	OK
class ReadLogicLinkIDS (PumpCommand):
  code = 149

# MMPump512??/	CMD_????????????????	150	0x96	('\x96')	??
class Model512Experiment_OP150 (PumpCommand):
  code = 150

# MMPump512/	CMD_READ_BG_ALARM_ENABLE	151	0x97	('\x97')	??
class ReadBGAlarmEnable (PumpCommand):
  code = 151

# MMPump512/	CMD_READ_TEMP_BASAL	152	0x98	('\x98')	OK
class ReadBasalTemp(PumpCommand):
  """
  MM511 - 120
  MM512 and up - opcode 152
  # strokes per basalunit = 40 - mm12, 10 in mm11
  """

  code = 152
  descr = "Read Temp Basal"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    temp = { 0: 'absolute', 1: 'percent' }[self.data[0]]
    status = dict(temp=temp)
    if temp is 'absolute':
      rate = lib.BangInt(data[2:4])/40.0
      duration = lib.BangInt(data[4:6])
      status.update(rate=rate, duration=duration)
    if temp is 'percent':
      rate = int(data[1])
      duration = lib.BangInt(data[4:6])
      status.update(rate=rate, duration=duration)
    log.info("READ temporary basal:\n%s" % lib.hexdump(data))
    return status

# MMGuardian3/	CMD_READ_SENSOR_SETTINGS	207	0xcf	('\xcf')	??
class GuardianSensorSettings (PumpCommand):
  code = 207
# MMGuardian3/	CMD_READ_SENSOR_PREDICTIVE_ALERTS	209	0xd1	('\xd1')	??
class GuardianSensorSettings (PumpCommand):
  code = 209
# MMGuardian3/	CMD_READ_SENSOR_DEMO_AND_GRAPH_TIMEOUT	210	0xd2	('\xd2')	??
class GuardianSensorDemoGraphTimeout (PumpCommand):
  code = 210
# MMGuardian3/	CMD_READ_SENSOR_ALARM_SILENCE	211	0xd3	('\xd3')	??
class GuardianSensorAlarmSilence (PumpCommand):
  code = 211
# MMGuardian3/	CMD_READ_SENSOR_RATE_OF_CHANGE_ALERTS	212	0xd4	('\xd4')	??
class GuardianSensorRateChangeAlerts (PumpCommand):
  code = 212

class ReadSettings(PumpCommand):
  """
  XXX: changed in MM512 to 192

  """

  code = 192
  descr = "Read Settings"
  params = [ ]
  retries = 2
  maxRecords = 1

  output_fields = ['maxBolus', 'maxBasal', 'insulin_action_curve' ]
  byte_map = {

  }

  def alarm(self, alarm):
    d = { 'volume': alarm, 'mode': 2 }
    if alarm == 4:
      d = { 'volume': -1, 'mode': 1 }
    return d
  def temp_basal_type(self, data):
    temp = { 'type': data[0] == 1 and "Percent" or "Units/hour",
             'percent': data[1]
           }
    return temp
  def getData(self):
    data = self.data
    log.info("READ pump settings:\n%s" % lib.hexdump(data))

    if len(data) < 2:
      log.info("pump settings: unsupported version, sorry")
      return data

    auto_off_duration_hrs = data[0]
    alarm = self.alarm(data[1])
    audio_bolus_enable = data[2] == 1
    audio_bolus_size = 0
    if audio_bolus_enable:
      audio_bolus_size = data[3] / 10.0
    variable_bolus_enable = data[4] == 1
    #MM23 is different
    maxBolus = data[5]/ 10.0
    # MM512 and up
    maxBasal = lib.BangInt(data[6:8]) / 40.0
    timeformat = data[8]
    insulinConcentration = {0: 100, 1: 50}[data[9]]
    patterns_enabled = data[10] == 1
    selected_pattern = data[11]
    rf_enable = data[12] == 1
    block_enable = data[13] == 1
    temp_basal = self.temp_basal_type(data[14:16])
    paradigm_enabled = data[16]
    """
    # MM12
    insulin_action_type = data[17] == 0 and 'Fast' or 'Regular'
    """
    #MM15
    # insulin_action_type = data[17]
    insulin_action_curve = data[17]
    low_reservoir_warn_type = data[18]
    low_reservoir_warn_point = data[19]
    keypad_lock_status = data[20]

    values = locals( )
    # safety
    values.pop('self')
    values.pop('data')

    return values

class ReadSettings523(ReadSettings):

  def getData(self):
    values = super(ReadSettings523, self).getData()
    data = self.data

    values['maxBasal'] = lib.BangInt(data[7:9]) / 40.0
    values['maxBolus'] = data[6]/ 10.0

    return values

# MMX15/	CMD_READ_SAVED_SETTINGS_DATE	193	0xc1	('\xc1')	??
class ReadSavedSettingsDate (PumpCommand):
  code = 193

class ReadContrast(PumpCommand):
  """
  """

  code = 195
  descr = "Read Contrast"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    log.info("READ contrast:\n%s" % lib.hexdump(data))
    return data



# MMX15/	CMD_READ_BOLUS_REMINDER_ENABLE	197	0xc5	('\xc5')	??
class ReadBolusReminderEnable (PumpCommand):
  code = 197

# MMX15/	CMD_READ_BOLUS_REMINDERS	198	0xc6	('\xc6')	??
class ReadBolusReminders (PumpCommand):
  code = 198

# MMX15/	CMD_READ_FACTORY_PARAMETERS	199	0xc7	('\xc7')	??
class ReadFactoryParameters (PumpCommand):
  code = 199

class ReadPumpStatus(PumpCommand):
  """
  """


  code = 206
  descr = "Read Pump Status"
  params = [ ]
  retries = 2
  maxRecords = 1
  def getData(self):
    data = self.data
    normal = { 03: 'normal' }
    status = { 'status': normal.get(data[0], 'error'),
               'bolusing': data[1] == 1,
               'suspended': data[2] == 1
             }
    return status

class ReadPumpState(PumpCommand):
  """
    >>> ReadPumpState(serial='665455').format() == ReadPumpState._test_ok
    True
  """
  _test_ok = bytearray([ 0x01, 0x00, 0xA7, 0x01, 0x66, 0x54, 0x55, 0x80,
                         0x00, 0x00, 0x02, 0x01, 0x00, 0x83, 0x2E, 0x00 ])

  code = 131
  descr = "Read Pump State"
  params = [ ]
  retries = 2
  maxRecords = 1



# MMX22/	CMD_READ_SENSOR_SETTINGS	153	0x99	('\x99')	??
class ReadSensorSettings (PumpCommand):
  """
  """
  descr = "Read sensor settings"
  code = 153
  params = [ ]
  retries = 2

class ReadSensorHistoryData (ReadHistoryData):
  def __init__(self, page=None, **kwds):
    params = kwds.pop('params', [ ])
    if page is not None:
      params = [ lib.LowByte(page >> 24), lib.LowByte(page >> 16),
                 lib.LowByte(page >>  8), lib.LowByte(page) ]

      self.page = page
    super(ReadSensorHistoryData, self).__init__(params=params, **kwds)
    self.params = params
    self.page = page

# MMX22/	CMD_READ_GLUCOSE_HISTORY	154	0x9a	('\x9a')	??
class ReadGlucoseHistory (ReadSensorHistoryData):
  """
    >>> ReadGlucoseHistory(page=1).params
    [0, 0, 0, 1]
    >>> list(ReadGlucoseHistory(page=1).format( ))
    [1, 0, 167, 1, 32, 136, 80, 128, 4, 0, 2, 2, 0, 154, 34, 0, 0, 0, 1, 155]
    >>> ReadGlucoseHistory(page=2).params
    [0, 0, 0, 2]
    >>> ReadGlucoseHistory(page=3)
    <ReadGlucoseHistory:size[1024]:[page][3]:data[0]:>
    >>> list(ReadGlucoseHistory(page=3).format( ))
    [1, 0, 167, 1, 32, 136, 80, 128, 4, 0, 2, 2, 0, 154, 34, 0, 0, 0, 3, 54]
    >>> ReadGlucoseHistory(page=3).params
    [0, 0, 0, 3]
    >>> ReadGlucoseHistory(params=[1]).params
    [1]
    >>> ReadGlucoseHistory(params=[2]).params
    [2]
    >>> ReadGlucoseHistory(params=[3]).params
    [3]
  """
  descr = "Read glucose history"
  code = 154
  params = [ ]

# MMX22/	CMD_READ_ISIG_HISTORY	155	0x9b	('\x9b')	??
class ReadISIGHistory (ReadSensorHistoryData):
  """
    >>> ReadISIGHistory(page=0).params
    [0, 0, 0, 0]

    >>> ReadISIGHistory(page=1).params
    [0, 0, 0, 1]

    >>> ReadISIGHistory(page=2).params
    [0, 0, 0, 2]

  """
  descr = "Read ISIG history"
  code = 155
  params = [ ]
  maxRecords = 32

# MMX22/	CMD_READ_CALIBRATION_FACTOR	156	0x9c	('\x9c')	??
class ReadCalibrationFactor (PumpCommand):
  """
  """
  code = 156

# MMX23/	CMD_READ_VCNTR_HISTORY	213	0xd5	('\xd5')	??
class ReadVCNTRHistory (ReadSensorHistoryData):
  code = 213

# MMX23/	CMD_READ_OTHER_DEVICES_IDS	240	0xf0	('\xf0')	??
class ReadOtherDevicesIDS (PumpCommand):
  code = 240


class ReadCaptureEventEnabled (PumpCommand):
  code = 241


class ChangeCaptureEventEnable (PumpCommand):
  code = 242
  params = [0]

  def __init__(self, enabled=True, **kwds):
    self.params[0] = int(enabled)
    super(ChangeCaptureEventEnable, self).__init__(**kwds)


class ReadConnectDevicesOtherDevicesStatus (PumpCommand):
  code = 243


class FilterHistory (PumpCommand):
  """

  """
  code = None
  begin = None
  end = None
  __fields__ = PumpCommand.__fields__ + ['begin', 'end']

  def __init__(self, begin=None, end=None, **kwds):
    params = kwds.get('params', [ ])
    if len(params) == 0:
      params.extend(lib.format_filter_date(begin))
      params.extend(lib.format_filter_date(end))

    kwds['params'] = params
    super(FilterHistory, self).__init__(**kwds)

  def getData(self):
    data = self.data
    if len(data) < 4:
      return bytearray(data)
    begin = lib.BangInt(data[0:2])
    end = lib.BangInt(data[2:4])
    return dict(begin=begin, end=end, params=self.params)

  @classmethod
  def ISO (klass, begin=None, end=None, **kwds):
    return klass(begin=lib.parse.date(begin), end=lib.parse.date(end), **kwds)

# MMX22??/	CMD_FILTER_BG	168	0xa8	('\xa8')	??
class FilterGlucoseHistory (FilterHistory):
  """
    >>> FilterGlucoseHistory.ISO(begin='2014-04-13', end='2014-04-14').params
    [7, 222, 4, 13, 7, 222, 4, 14]
  """
  code = 168

# MMX22??/	CMD_FILTER_ISIG	169	0xa9	('\xa9')	??
class FilterISIGHistory (FilterHistory):
  """
    >>> FilterISIGHistory.ISO(begin='2014-04-13', end='2014-04-14').params
    [7, 222, 4, 13, 7, 222, 4, 14]

  """
  code = 169

class TweakAnotherCommand (ManualCommand):
  @classmethod
  def get_kwds (klass, Other, args):
    kwds = { }
    fields = list(set(Other.__fields__) - set(['serial', ]))
    for k in fields:
      value = getattr(args, k, None)
      if value is not None:
        kwds[k] = value
    return kwds

  @classmethod
  def config_argparse (klass, parser):
    parser.add_argument('--params', type=int, action="append",
                        help="parameters to format into sent message"
                       )
    parser.add_argument('--params_hexline', dest='params', type=lib.decode_hexline,
                        help="hex string, parameters to format into sent message"
                        # default=commands.ManualCommand.params
                       )
    parser.add_argument('--descr', type=str,
                        help="Description of command"
                       )
    parser.add_argument('--name', type=str,
                        help="Proposed name of command"
                       )
    parser.add_argument('--save', action="store_true", default=False,
                        help="Save response in a file."
                       )
    parser.add_argument('--effectTime', type=float,
                        help="time to sleep before responding to message, float in seconds"
                       )
    parser.add_argument('--maxRecords', type=int,
                        help="number of frames in a packet composing payload response"
                       )
    parser.add_argument('--bytesPerRecord', type=int,
                        help="bytes per frame"
                       )

    parser.add_argument('--page', type=int,
                        help="Page to fetch (for ReadHistoryData)"
                       )

    parser.add_argument('--begin', type=lib.parse.date,
                        help="begin date for FilterHistory"
                       )
    parser.add_argument('--end', type=lib.parse.date,
                        help="end date for FilterHistory"
                       )


    return parser


class ReadPumpModel(PumpCommand):
  """
    >>> ReadPumpModel(serial='665455').format() == ReadPumpModel._test_ok
    True
  """
  code = 141
  descr = "Read Pump Model Number"
  params = [ ]
  retries = 2
  maxRecords = 1
  _test_ok = bytearray([ 0x01, 0x00, 0xA7, 0x01, 0x66, 0x54, 0x55, 0x80,
                         0x00, 0x00, 0x02, 0x01, 0x00, 0x8D, 0x5B, 0x00 ])

  def getData(self):
    data = self.data
    if len(data) == 0:
      return ''
    length = data[0]
    msg = data[1:1+length]
    self.model = msg
    return str(msg)

def do_commands(device):
  comm = ReadPumpModel( serial=device.serial )
  device.execute(comm)
  log.info('comm:%s:data:%s' % (comm, getattr(comm.getData( ), 'data', None)))
  log.info('REMOTE PUMP MODEL NUMBER: %s' % comm.getData( ))

  log.info("READ RTC")
  comm = ReadRTC( serial=device.serial )
  device.execute(comm)
  log.info('comm:RTC:%s' % (comm.getData( )))

  log.info("READ PUMP ID")
  comm = ReadPumpID( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ PUMP ID: ID: %s' % (comm.getData( )))


  log.info("Battery Status")
  comm = ReadBatteryStatus( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ Battery Status: %r' % (comm.getData( )))

  log.info("Firmware Version")
  comm = ReadFirmwareVersion( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ Firmware Version: %r' % (comm.getData( )))

  log.info("remaining insulin")
  comm = ReadRemainingInsulin( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ Remaining Insulin: %r' % (comm.getData( )))

  log.info("read totals today")
  comm = ReadTotalsToday( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ totals today: %r' % (comm.getData( )))

  log.info("read remote IDS")
  comm = ReadRadioCtrlACL( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ radio ACL: %r' % (comm.getData( )))

  log.info("read temporary basal")
  comm = ReadBasalTemp( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ temp basal: %r' % (comm.getData( )))

  log.info("read settings")
  comm = ReadSettings( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ settings!: %r' % (comm.getData( )))

  log.info("read contrast")
  comm = ReadContrast( serial=device.serial )
  device.execute(comm)
  log.info('comm:READ contrast: %r' % (comm.getData( )))

  log.info("read cur page number")
  comm = ReadCurPageNumber(serial=device.serial  )
  device.execute(comm)
  log.info('comm:READ page number!!!: %r' % (comm.getData( )))

  log.info("read HISTORY DATA")
  comm = ReadHistoryData(serial=device.serial, page=0)
  device.execute(comm)
  log.info('comm:READ history data page!!!:\n%s' % (comm.getData( )))

def get_pages(device):
  log.info("read cur page number")
  comm = ReadCurPageNumber(serial=device.serial )
  device.execute(comm)
  pages = comm.getData( )
  log.info('attempting to read %s pages of history' % pages)

  for x in range(pages + 1):
    log.info('comm:READ HISTORY DATA page number: %r' % (x))
    comm = ReadHistoryData(serial=device.serial, params=[ x ] )
    device.execute(comm)
    page = comm.getData( )
    log.info("XXX: READ HISTORY DATA!!:\n%s" % lib.hexdump(page))
    time.sleep(.100)

__all__ = [
  'BaseCommand', 'KeypadPush', 'PowerControl', 'PowerControlOff',
  'PumpCommand', 'PumpResume', 'PumpSuspend',
  'ReadBasalTemp', 'ReadBatteryStatus', 'ReadContrast',
  'ReadCurPageNumber', 'ReadErrorStatus', 'ReadFirmwareVersion',
  'ReadGlucoseHistory', 'ReadHistoryData', 'ReadPumpID',
  'ReadPumpModel', 'ReadPumpState', 'ReadPumpStatus',
  'ReadRTC', 'ReadRadioCtrlACL', 'ReadRemainingInsulin',
  'ReadRemainingInsulin523',
  'ReadSettings', 'ReadSettings523', 'ReadTotalsToday', 'SetSuspend',
  'PushEASY', 'PushUP', 'PushDOWN', 'PushACT', 'PushESC',
  'TempBasal', 'ManualCommand', 'ReadCurGlucosePageNumber',
  'SetAutoOff',
  'SetEnabledEasyBolus',
  'SetBasalType',
  'TempBasalPercent',
  'Bolus',
  'ReadErrorStatus508',
  'ReadBolusHistory',
  'ReadDailyTotals',
  'ReadPrimeBoluses',
  'ReadAlarms',
  'ReadProfileSets',
  'ReadUserEvents',
  'ReadRemoteControlID',
  'Read128KMem',
  'Read256KMem',
  'ReadBasalTemp508',
  'ReadTodayTotals508',
  'ReadSensorSettings',
  'ReadSensorHistoryData',
  'ReadISIGHistory',
  'FilterHistory',
  'FilterGlucoseHistory',
  'FilterISIGHistory',

  'ReadProfiles511_STD',
  'ReadProfiles511_A',
  'ReadProfiles511_B',
  'Model511_ExperimentOP125',
  'Model511_ExperimentOP126',
  'ReadSettings511',
  'ReadPumpTrace',
  'ReadDetailTrace',
  'Model511_Experiment_OP165',
  'ReadNewTraceAlarm',
  'ReadOldTraceAlarm',
  'WriteGlucoseHistoryTimestamp',
  'ReadLanguage',
  'ReadBolusWizardSetupStatus',
  'ReadCarbUnits',
  'ReadBGUnits',
  'ReadCarbRatios',
  'ReadCarbRatios512',
  'ReadInsulinSensitivities',
  'ReadBGTargets',
  'ReadBGTargets515',
  'ReadBGAlarmCLocks',
  'ReadReservoirWarning',
  'ReadBGReminderEnable',
  'ReadSettings512',
  'ReadProfile_STD512',
  'ReadProfile_A512',
  'ReadProfile_B512',
  'ReadLogicLinkIDS',
  'Model512Experiment_OP150',
  'ReadBGAlarmEnable',
  'GuardianSensorSettings',
  'GuardianSensorSettings',
  'GuardianSensorDemoGraphTimeout',
  'GuardianSensorAlarmSilence',
  'GuardianSensorRateChangeAlerts',
  'ReadSavedSettingsDate',
  'ReadBolusReminderEnable',
  'ReadBolusReminders',
  'ReadFactoryParameters',
  'ReadCalibrationFactor',
  'ReadVCNTRHistory',
  'ReadOtherDevicesIDS',
  'PumpTraceSelect',
  'PumpEnableDetailTrace',
  'PumpDisableDetailTrace',
  'Experiment_OP161',
  'Experiment_OP162',
  'Model511_Experiment_OP119',
  'Model511_Experiment_OP120',
  'Model511_Experiment_OP121',
  'Model511_Experiment_OP122',
  'Model511_Experiment_OP123',
  'Model511_Experiment_OP124',
  'Model511_Experiment_OP125',
  'Model511_Experiment_OP126',
  'Model511_Experiment_OP127',
  'Model511_Experiment_OP128',
  'Model511_Experiment_OP129',
  'Model511_Experiment_OP130',
  'SelectBasalProfile',
  'SelectBasalProfileSTD',
  'SelectBasalProfileA',
  'SelectBasalProfileB',
  'PumpExperiment_OP69',
  'PumpExperiment_OP70',
  'PumpExperiment_OP71',
  'PumpExperiment_OP72',
  'PumpExperiment_OP73',
  'PumpExperiment_OP75',
]

if __name__ == '__main__':
  import doctest
  doctest.testmod( )

  import sys
  port = None
  port = sys.argv[1:] and sys.argv[1] or False
  serial_num = sys.argv[2:] and sys.argv[2] or False
  if not port or not serial_num:
    print "usage:\n%s <port> <serial>, eg /dev/ttyUSB0 208850" % sys.argv[0]
    sys.exit(1)
  import link
  import stick
  import session
  from pprint import pformat
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
  log.info("howdy! I'm going to take a look at your pump and grab lots of info.")
  stick = stick.Stick(link.Link(port, timeout=.400))
  stick.open( )
  session = session.Pump(stick, serial_num)
  log.info(pformat(stick.interface_stats( )))
  log.info('PUMP MODEL: %s' % session.read_model( ))
  do_commands(session)
  log.info(pformat(stick.interface_stats( )))
  #get_pages(session)
  #log.info(pformat(stick.interface_stats( )))
  log.info("howdy! we downloaded a lot of pump info successfully.")
  # stick.open( )

