
import logging
import time

import lib

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
    log.info("%s:download:done?:%s" % (self, expect_size))
    return found >= expect
  def format(self):
    pass

  def respond(self, data):
    self.data = data
    self.getData( )
    self.responded = True

  def hexdump (self):
    return lib.hexdump(self.data)

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
  __fields__ = ['maxRecords', 'code', 'descr',
                'serial', 'bytesPerRecord', 'retries', 'params']
  def __init__(self, **kwds):
    for k in self.__fields__:
      value = kwds.get(k, getattr(self, k))
      setattr(self, k, value)
    self.allocateRawData( )
    self.data = bytearray( )
    self.name = self.log_name( )

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
    super(type(self), self).__init__(**kwds)
    self.name = kwds.get('name', self.__class__.__name__)
    self.kwds = kwds
  def __str__(self):
    if self.responded:
      return '{}:{}:size[{}]:data:{}'.format(self.name, self.kwds,
                                          self.size, str(self.getData( )))
    return '{}:{}:data:unknown'.format(self.name, self.kwds)

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
  effectTime = 7

class PowerControlOff(PowerControl):
  """
  Here's an example where arguments clearly modify behavior.
  """
  params = [ 0x00, 0x0A ]

class TempBasal(PumpCommand):
  """

  """

  code = 76
  descr = "Set temp basal"
  params = [ 0x00, 0x00, 0x00 ]
  retries = 0
  #maxRecords = 0
  #timeout = 1

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
  """
  _test_ok = bytearray([ 0x01, 0x00, 0xA7, 0x01, 0x20, 0x88, 0x50, 0x80,
               0x01, 0x00, 0x02, 0x02, 0x00, 0x80, 0x9B, 0x03,
               0x36, ])

  def __init__(self, page=None, **kwds):
    if page is None and kwds.get('params', [ ]):
      page = kwds.pop('params')[0] or 0

    if page is not None:
      self.page = int(page)
      kwds['params'] = [ self.page ]
    super(type(self), self).__init__(**kwds)

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
    return data

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
    if len(data) == 1:
      return int(data[0])
    return lib.BangLong(data[0:4])


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
      'year'  : 2000 + (data[4] & 0x0F),
      'month' : int(data[5]),
      'day'   : int(data[6]),
    }
    return "%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s:%(second)s" % (d)

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

  def getData(self):
    data = self.data
    log.info("READ remaining insulin:\n%s" % lib.hexdump(data))
    return lib.BangInt(data[0:2])/10.0


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
    rate = lib.BangInt(data[2:4])/40.0
    duration = lib.BangInt(data[4:6])
    log.info("READ temporary basal:\n%s" % lib.hexdump(data))
    return { 'rate': rate, 'duration': duration }

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


class ReadSettings(PumpCommand):
  """
  XXX: changed in MM512 to 192

  """

  code = 192
  descr = "Read Settings"
  params = [ ]
  retries = 2
  maxRecords = 1

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
    maxBasal = lib.BangInt(data[6:8]) / 40
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
    insulin_action_type = data[17]
    low_reservoir_warn_type = data[18]
    low_reservoir_warn_point = data[19]
    keypad_lock_status = data[20]

    values = locals( )
    # safety
    values.pop('self')
    values.pop('data')

    return values

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


class SetSuspend(PumpCommand):
  code = 77
  descr = "Set Pump Suspend/Resume status"
  params = [ ]
  retries = 2
  maxRecords = 1

class PumpSuspend(SetSuspend):
  descr = "Suspend pump"
  params = [ 1 ]

class PumpResume(SetSuspend):
  descr = "Resume pump (cancel suspend)"
  params = [ 0 ]

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



class ReadGlucoseHistory(PumpCommand):
  """
  """
  descr = "Read glucose history"
  code = 131
  params = [ ]
  retries = 2



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
  log.info('comm:READ history data page!!!:\n%s' % (lib.hexdump(comm.getData( ))))

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
  'ReadSettings', 'ReadTotalsToday', 'SetSuspend',
  'PushEASY', 'PushUP', 'PushDOWN', 'PushACT', 'PushESC',
  'TempBasal', 'ManualCommand'
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
  
