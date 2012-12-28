#!/usr/bin/python
import user

#import struct
import sys
import serial
import time
import logging
from pprint import pprint, pformat

from pump import link
from pump.commands import *
from pump import lib

#from insulaudit.core import Command
#from insulaudit.clmm.usbstick import *
#from insulaudit import lib

logging.basicConfig( stream=sys.stdout )
log = logging.getLogger( 'auditor' )
log.setLevel( logging.DEBUG )
log.info( 'hello world' )
io  = logging.getLogger( 'auditor.io' )
io.setLevel( logging.DEBUG )

"""
######################
#
############################
#
# USB(Pump) Command Stuff
#

"""

"""
######################
#
# Pump
#

# every command needs:
# code, retries, params, length, pages

"""

class Link( link.Link ):
  class ID:
    VENDOR  = 0x0a21
    PRODUCT = 0x8001
  timeout = .100
  def __init__( self, port, timeout=None ):
    super(type(self), self).__init__(port, timeout)

  def setTimeout(self, timeout):
    self.serial.setTimeout(timeout)
  def getTimeout(self):
    return self.serial.getTimeout()

  def initUSBComms(self):
    self.initCommunicationsIO()
    #self.initDevice()

  def getSignalStrength(self):
    result = self.readSignalStrength()
    signal = result[0]

  def readSignalStrength(self):
    result = self.sendComLink2Command(6, 0)
    # result[0] is signal strength
    log.info('%r:readSignalStrength:%s' % (self, int(result[0])))
    return result

  def initCommunicationsIO(self):
    # close/open serial
    self.readProductInfo( )
    sig = 0
    while sig < 50:
      sig = self.readSignalStrength()
  def endCommunicationsIO(self):
    self.readSignalStrength()
    self.readInterfaceStatistics()
    # close port
    self.close()

  def readProductInfo(self):
    result = self.sendComLink2Command(4)
    # 1/0/255
    log.info('readProductInfo:result')
    freq   = result[5]
    info   = self.decodeProductInfo(result)
    log.info('product info: %s' % pformat(info))
    # decodeInterface stats
      
  def decodeProductInfo(self, data):
    return USBProductInfo.decode(data)

  def sendComLink2Command(self, msg, a2=0x00, a3=0x00):
    # generally commands are 3 bytes, most often CMD, 0x00, 0x00
    msg = bytearray([ msg, a2, a3 ])
    io.info('sendComLink2Command:write')
    self.write(msg)
    return self.checkAck()
    # throw local usb exception

  def checkAck(self):
    time.sleep(.050)
    result     = bytearray(self.read(64))
    io.info('checkAck:read')
    commStatus = result[0]
    # usable response
    assert commStatus == 1
    status     = result[1]
    # status == 102 'f' NAK, look up NAK
    if status == 85: # 'U'
      log.info('ACK OK')
      return result[3:]
    assert False, "NAK!!"

  def decodeIFaceStats(self, data):
    return InterfaceStats.decode(data)

  def readInterfaceStatistics(self):
    # decode and log stats
    result = self.sendComLink2Command(5, 0)
    info   = self.decodeIFaceStats(result)
    log.info("read radio Interface Stats: %s" % pformat(info))
    result = self.sendComLink2Command(5, 1)
    info   = self.decodeIFaceStats(result)
    log.info("read stick Interface Stats: %s" % pformat(info))


#######################
#
#
#
def CRC8(data):
  return lib.CRC8.compute(data)

################################
# Remote Stuff
#

class BaseCommand(object):
  code    = 0x00
  descr   = "(error)"
  retries = 2
  timeout = 3
  params  = [ ]
  bytesPerRecord = 0
  maxRecords = 0
  effectTime = 1

  def __init__(self, code, descr, *args):
    self.code   = code
    self.descr  = descr
    self.params = [ ]

  def format(self):
    pass

  def allocateRawData(self):
    self.raw = self.bytesPerRecord * self.maxRecords


class Device(object):
  def __init__(self, link):
    self.link = link

  def execute(self, command):
    self.command = command
    self.allocateRawData()
    self.sendAndRead()

  def sendAndRead(self):
    self.sendDeviceCommand()
    time.sleep(self.command.effectTime)
    if self.expectedLength > 0:
      # in original code, this modifies the length tested in the previous if
      # statement
      self.command.data = self.readDeviceData()

  def sendDeviceCommand(self):
    packet = self.buildTransmitPacket()
    io.info('sendDeviceCommand:write:%r' % (self.command))
    self.link.write(packet)
    time.sleep(.001)
    code = self.command.code
    params = self.command.params
    if code != 93 or params[0] != 0:
      self.link.checkAck()

  def allocateRawData(self):
    self.command.allocateRawData()
    self.expectedLength = self.command.bytesPerRecord * self.command.maxRecords

  def readDeviceData(self):
    self.eod = False
    results  = bytearray( )
    while not self.eod:
      data = self.readDeviceDataIO( )
      results.extend(data)
    return results

  def readDeviceDataIO(self):
    results   = self.readData()
    lb, hb    = results[5] & 0x7F, results[6]
    self.eod  = (results[5] & 0x80) > 0
    resLength = lib.BangInt((lb, hb))
    log.info('XXX resLength: %s' % resLength)
    #assert resLength < 64, ("cmd low byte count:\n%s" % lib.hexdump(results))

    data = results[13:13+resLength]
    assert len(data) == resLength
    crc = results[-1]
    # crc check
    log.info('readDeviceDataIO:msgCRC:%r:expectedCRC:%r:data:%r' % (crc, CRC8(data), data))
    assert crc == CRC8(data)
    return data

  def readData(self):
    bytesAvailable = self.getNumBytesAvailable()
    packet = [12, 0, lib.HighByte(bytesAvailable), lib.LowByte(bytesAvailable)]
    packet.append( CRC8(packet) )

    response = self.writeAndRead(packet, bytesAvailable)
    # assert response.length > 14
    assert (int(response[0]) == 2), repr(response)
    # response[1] != 0 # interface number !=0
    # response[2] == 5 # timeout occurred
    # response[2] == 2 # NAK
    # response[2] # should be within 0..4
    log.info("readData ACK")
    return response

  def writeAndRead(self, msg, length):
    io.info("writeAndRead:")
    self.link.write(bytearray(msg))
    time.sleep(.300)
    self.link.setTimeout(self.command.timeout)
    return bytearray(self.link.read(length))

  def getNumBytesAvailable(self):
    result = self.readStatus( )
    start = time.time()
    i     = 0
    while result == 0 and time.time() - start < 1:
      log.debug('%r:getNumBytesAvailable:attempt:%s' % (self, i))
      result = self.readStatus( )
      time.sleep(.10)
      i += 1
    log.info('getNumBytesAvailable:%s' % result)
    return result

  def readStatus(self):
    result         = self.link.sendComLink2Command(3)
    commStatus     = result[0] # 0 indicates success
    assert commStatus == 0
    status         = result[2]
    lb, hb         = result[3], result[4]
    bytesAvailable = lib.BangInt((lb, hb))
    self.status    = status

    if (status & 0x1) > 0:
      return bytesAvailable
    return 0

  def buildTransmitPacket(self):
    return self.command.format( )

class PumpCommand(BaseCommand):
  #serial = '665455'
  #serial = '206525'
  serial = '208850'

  params = [ ]
  bytesPerRecord = 64
  maxRecords = 1
  retries = 2
  __fields__ = ['maxRecords', 'code', 'descr',
                'serial', 'bytesPerRecord', 'params']
  def __init__(self, **kwds):
    for k in self.__fields__:
      value = kwds.get(k, getattr(self, k))
      setattr(self, k, value)

  def getData(self):
    return self.data

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
    io.info(packet)
    return bytearray(packet)

  def calcRecordsRequired(self):
    length = self.bytesPerRecord * self.maxRecords
    i = length / 64
    j = length % 64
    if j > 0:
      return i + 1
    return i


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
  timeout = 1
  effectTime = 9

class PowerControlOff(PowerControl):
  params = [ 0x00, 0x0A ]

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
    >>> ReadHistoryData(serial='208850').format() == ReadHistoryData._test_ok
    True
  """
  _test_ok = bytearray([ 0x01, 0x00, 0xA7, 0x01, 0x20, 0x88, 0x50, 0x80,
               0x01, 0x00, 0x02, 0x02, 0x00, 0x80, 0x9B, 0x03,
               0x36, ])

  code = 128
  descr = "Read History Data"
  params = [ 0x00 ]
  retries = 2
  maxRecords = 2
  effectTime = .100

  def getData(self):
    data = self.data
    log.info("XXX: READ HISTORY DATA!!:\n%s" % lib.hexdump(data))
    return data

class ReadCurPageNumber(PumpCommand):
  """
  """

  code = 157
  descr = "Read Cur Page Number"
  params = [ ]
  retries = 2
  maxRecords = 1

  def getData(self):
    data = self.data
    log.info("XXX: READ cur page number:\n%s" % lib.hexdump(data))
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

  def alarm(self, alarm):
    d = { 'volume': alarm, 'mode': 2 }
    if alarm == 4:
      d = { 'volume': -1, 'mode': 1 }
    return d
    
  def getData(self):
    data = self.data
    log.info("READ pump settings:\n%s" % lib.hexdump(data))
    

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
    """
    # MM12
    insulin_action_type = data[17] == 0 and 'Fast' or 'Regular'
    """
    #MM15
    insulin_action_type = data[17]
    low_reservoir_warn_type = data[18]
    low_reservoir_warn_point = data[19]
    keypad_lock_status = data[20]

    return locals( )

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

def initDevice(link):
  device = Device(link)

  #comm   = PowerControl()
  #device.execute(comm)
  #log.info('comm:%s:data:%s' % (comm, getattr(comm, 'data', None)))

  comm   = ReadErrorStatus()
  device.execute(comm)
  log.info('comm:%s:data:%s' % (comm, getattr(comm, 'data', None)))

  comm   = ReadPumpState()
  device.execute(comm)
  log.info('comm:%s:data:%s' % (comm, getattr(comm, 'data', None)))

  return device

def do_commands(device):
  comm = ReadPumpModel( )
  device.execute(comm)
  log.info('comm:%s:data:%s' % (comm, getattr(comm.getData( ), 'data', None)))
  log.info('REMOTE PUMP MODEL NUMBER: %s' % comm.getData( ))

  log.info("READ RTC")
  comm = ReadRTC( )
  device.execute(comm)
  log.info('comm:RTC:%s' % (comm.getData( )))

  log.info("READ PUMP ID")
  comm = ReadPumpID( )
  device.execute(comm)
  log.info('comm:READ PUMP ID: ID: %s' % (comm.getData( )))


  log.info("Battery Status")
  comm = ReadBatteryStatus( )
  device.execute(comm)
  log.info('comm:READ Battery Status: %r' % (comm.getData( )))

  log.info("Firmware Version")
  comm = ReadFirmwareVersion( )
  device.execute(comm)
  log.info('comm:READ Firmware Version: %r' % (comm.getData( )))

  log.info("remaining insulin")
  comm = ReadRemainingInsulin( )
  device.execute(comm)
  log.info('comm:READ Remaining Insulin: %r' % (comm.getData( )))

  log.info("read totals today")
  comm = ReadTotalsToday( )
  device.execute(comm)
  log.info('comm:READ totals today: %r' % (comm.getData( )))

  log.info("read remote IDS")
  comm = ReadRadioCtrlACL( )
  device.execute(comm)
  log.info('comm:READ radio ACL: %r' % (comm.getData( )))

  log.info("read temporary basal")
  comm = ReadBasalTemp( )
  device.execute(comm)
  log.info('comm:READ temp basal: %r' % (comm.getData( )))

  log.info("read settings")
  comm = ReadSettings( )
  device.execute(comm)
  log.info('comm:READ settings!: %r' % (comm.getData( )))

  log.info("read contrast")
  comm = ReadContrast( )
  device.execute(comm)
  log.info('comm:READ contrast: %r' % (comm.getData( )))

  log.info("read cur page number")
  comm = ReadCurPageNumber( )
  device.execute(comm)
  log.info('comm:READ page number!!!: %r' % (comm.getData( )))

  log.info("read HISTORY DATA")
  comm = ReadHistoryData( )
  device.execute(comm)
  #log.info('comm:READ history data!!!: %r' % (comm.getData( )))

def get_pages(device):
  log.info("read cur page number")
  comm = ReadCurPageNumber( )
  device.execute(comm)
  pages = comm.getData( )
  log.info('attempting to read %s pages of history' % pages)

  for x in range(pages + 1):
    log.info('comm:READ HISTORY DATA page number: %r' % (x))
    comm = ReadHistoryData( params=[ x ] )
    device.execute(comm)
    comm.getData( )
  #log.info('comm:READ history data!!!: %r' % (comm.getData( )))

def shutdownDevice(device):
  comm = PowerControlOff()
  device.execute(comm)
  log.info('comm:%s:data:%s' % (comm, getattr(comm, 'data', None)))


if __name__ == '__main__':
  io.info("hello world")
  import doctest
  doctest.testmod( )

  port = None
  try:
    port = sys.argv[1]
  except IndexError, e:
    print "usage:\n%s /dev/ttyUSB0" % sys.argv[0]
    sys.exit(1)
    
  link = Link(port)
  link.initUSBComms()
  device = initDevice(link)
  do_commands(device)
  #get_pages(device)
  #shutdownDevice(device)
  link.endCommunicationsIO()
  #pprint( carelink( USBProductInfo(      ) ).info )


#####
# EOF
