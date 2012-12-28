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
