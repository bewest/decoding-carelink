
import lib
import logging
import time

log = logging.getLogger( ).getChild(__name__)

from errors import StickError, AckError, BadDeviceCommError

def CRC8(data):
  return lib.CRC8.compute(data)

class StickCommand(object):
  """Basic stick command
  """
  code = [ 0x00 ]
  label = __doc__
  delay = .001
  size = 64

  def __str__(self):
    code = ' '.join([ '%#04x' % op for op in self.code ])
    return '{0}:{1}'.format(self.__class__.__name__, code)
  def __repr__(self):
    return '<{0:s}>'.format(self)
  def format(self):
    return self.format_cl2(*self.code)

  def format_cl2(self, msg, a2=0x00, a3=0x00):
    # generally commands are 3 bytes, most often CMD, 0x00, 0x00
    msg = bytearray([ msg, a2, a3 ])
    return msg

  def parse(self, data):
    self.data = data

  def respond(self, raw):
    if len(raw) == 0:
      log.error("ACK is zero bytes!")
      # return False
      raise AckError("ACK is 0 bytes: %s" % lib.hexdump(raw))
    commStatus = raw[0]
    # usable response
    assert commStatus == 1, ('commStatus: %02x expected 0x1' % commStatus)
    status     = raw[1]
    # status == 102 'f' NAK, look up NAK
    if status == 85: # 'U'
      return raw[:3], raw[3:]
    assert False, ("NAK!!\n%s" % lib.hexdump(raw[:3]))
    

class ProductInfo(StickCommand):
  """Get product info from the usb device."""
  code   = [ 4 ]
  SW_VER = 16
  label  = 'usb.productInfo'
  rf_table  = { 001: '868.35Mhz' ,
                000: '916.5Mhz'  ,
                255: '916.5Mhz'  }
  iface_key = { 3: 'USB',
                1: 'Paradigm RF' }

  @classmethod
  def decodeInterfaces( klass, L ):
    n, tail    = L[ 0 ], L[ 1: ]
    interfaces = [ ]
    for x in xrange( n ):
      i    = x*2
      k, v = tail[i], tail[i+1]
      interfaces.append( ( k, klass.iface_key.get( v, 'UNKNOWN'  ) ) )
    return interfaces

  @classmethod
  def decode( klass,  data ):
    return {
      'rf.freq'          : klass.rf_table.get( data[ 5 ], 'UNKNOWN' )
    , 'serial'           : str( data[ 0:3 ]).encode( 'hex'  )
    , 'product.version'  : '{0}.{1}'.format( *data[ 3:5 ] )
    , 'description'      : str( data[ 06:16 ] )
    , 'software.version' : '{0}.{1}'.format( *data[ 16:18 ] )
    , 'interfaces'       : klass.decodeInterfaces( data[ 18: ] )
    }

  _test_ok = bytearray( [
  ] )
  def parse(self, data):
    """
      #>>>
    """
    return self.decode(data)

class InterfaceStats(StickCommand):
  code          = [ 5 ]
  INTERFACE_IDX = 19
  label         = 'usb.interfaceStats'
  @classmethod
  def decode( klass, data):
    return {
      'errors.crc'      : data[ 0 ]
    , 'errors.sequence' : data[ 1 ]
    , 'errors.naks'     : data[ 2 ]
    , 'errors.timeouts' : data[ 3 ]
    , 'packets.received': lib.BangLong( data[ 4: 8 ] )
    , 'packets.transmit': lib.BangLong( data[ 8:12 ] )
    }
  def parse(self, data):
    """
      #>>>
    """
    return self.decode(data)


class UsbStats(InterfaceStats):
  code = [ 5, 1 ]

class RadioStats(InterfaceStats):
  code = [ 5, 0 ]

class SignalStrength(StickCommand):
  code = [ 6, 0 ]
  def parse(self, data):
    """
      #>>>
    """
    # result[0] is signal strength
    self.value = int(data[0])
    log.info('%r:readSignalStrength:%s' % (self, int(data[0])))
    return int(data[0])

class LinkStatus(StickCommand):
  code = [ 0x03 ]
  reason = ''

  def __str__(self):
    if getattr(self, 'error', False):
      return '{0}:error:{2}%s:reason:{1}'.format(self.__class__.__name__, self.error, self.reason)
    
    return super(type(self), self).__str__( )
      
  def record_error(self, result):
    self.error  = True
    self.ack    = result[0] # 0 indicates success
    # believe success = result[1] # 'U' or 'f'
    self.status = result[2]
    lb, hb      = result[3], result[4]
    self.size   = lib.BangInt((lb, hb))

    if self.ack == 0 and (self.status & 0x1) > 0:
      self.error = False
    self.set_reason(self.status)

  def set_reason(self, status):
    reasons = [ ]
    if (status & 0x2) > 0:
      reasons.append('STATUS: receive in progress!')
    if (status & 0x4) > 0:
      reasons.append('STATUS: transmit in progress!')
    if (status & 0x8) > 0:
      reasons.append('STATUS: interface error!')
    if (status & 0x10) > 0:
      reasons.append('STATUS: recieve overflow!')
    if (status & 0x20) > 0:
      reasons.append('STATUS: transmit overflow!')
    if (status & 0x1) > 0:
      reasons.append('STATUS: OK')
    msg = '\n'.join(map(str, [ self, ', '.join(reasons) ]))
    log.info(msg)
    self.reasons = reasons

  def parse(self, result):
    """
      #>>>
    """
    self.record_error(result)
    if self.ack != 0:
      log.error("readStatus: non-zero status: %02x" % self.ack)
      # should this trigger a retry, and if so where?
      # should the other usb commands also trigger these retries? and at the
      # same points?
      raise AckError("readStatus: non-zero status: %02x" % self.ack)
    if self.error is not True:
      return self.size
    return 0

class ReadRadio(StickCommand):
  code = [ 0x0C, 0x00 ]
  def __init__(self, size):
    self.size = size
    self.dl_size = size
    packet = [12, 0, lib.HighByte(size), lib.LowByte(size)]
    if size < 64:
      log.error('size is less than 64, which will cause an error. trying 64 instead')
      self.size = 64
    self.code = packet + [ CRC8(packet) ]

  def __str__(self):
    return '{0}:size:{1}'.format(self.__class__.__name__, self.dl_size)
  def __repr__(self):
    return '<{0:s}>'.format(self)
  def format(self):
    msg = bytearray(self.code)
    return msg

  def respond(self, raw):
    if len(raw) == 0:
      log.error("ReadRadio ACK is zero bytes!")
      # return False
      raise AckError("ACK is 0 bytes: %s" % lib.hexdump(raw))
    log.info('readData validating remote raw[ack]: %02x' % raw[0])
    log.info('readData; foreign raw should be at least 14 bytes? %s %s' % (len(raw), len(raw) > 14))
    log.info('readData; raw[retries] %s' % int(raw[3]))
    dl_status = int(raw[0])
    if dl_status != 0x02: # this differs from the others?
      raise BadDeviceCommError("bad dl raw! %r" % raw)
      assert (int(raw[0]) == 2), repr(raw)
    return raw[:1], raw
    
  def parse(self, raw):
    """
    log.info('readData validating remote raw[ack]: %02x' % raw[0])
    log.info('readData; foreign raw should be at least 14 bytes? %s %s' % (len(raw), len(raw) > 14))
    log.info('readData; raw[retries] %s' % int(raw[3]))
    dl_status = int(raw[0])
    if dl_status != 0x02: # this differs from the others?
      raise BadDeviceCommError("bad dl raw! %r" % raw)
      assert (int(raw[0]) == 2), repr(raw)
    # raw[1] != 0 # interface number !=0
    # raw[2] == 5 # timeout occurred
    # raw[2] == 2 # NAK
    # raw[2] # should be within 0..4
    log.info("readData ACK")
    lb, hb    = raw[5] & 0x7F, raw[6]
    self.eod  = (raw[5] & 0x80) > 0
    """
    lb, hb    = raw[5] & 0x7F, raw[6]
    self.eod  = (raw[5] & 0x80) > 0
    resLength = lib.BangInt((lb, hb))
    log.info('XXX resLength: %s' % resLength)
    #assert resLength < 64, ("cmd low byte count:\n%s" % lib.hexdump(raw))

    data = raw[13:13+resLength]
    self.packet = data
    log.info('found packet len(%s)\n%s' % (len(self.packet), lib.hexdump(self.packet)))
    assert len(data) == resLength
    head = raw[13:]
    crc = raw[-1]
    # crc check
    log.info('readDeviceDataIO:msgCRC:%r:expectedCRC:%r:data:%s' % (crc, CRC8(data), lib.hexdump(data)))
    assert crc == CRC8(data)
    return data

class TransmitPacket(StickCommand):
  code = [ 1, 0, 167, 1 ]
  head = [ 1, 0, 167, 1 ]
  # wraps pump commands
  def __init__(self, command):
    self.command = command
    self.params  = command.params
    self.code    = command.code
    self.retries = command.retries
    self.serial  = command.serial
    self.delay = command.effectTime

  def __str__(self):
    if getattr(self, 'command', False):
      return '{0}:{1:s}'.format(self.__class__.__name__, self.command)
    code = ' '.join([ '%#04x' % op for op in self.head ])
    return '{0}:{1}'.format(self.__class__.__name__, code)
  def __repr__(self):
    return '<{0:s}>'.format(self)
  

  def calcRecordsRequired(self):
    return self.command.calcRecordsRequired( )

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

  def respond(self, raw):
    code = self.command.code
    params = self.params
    if code != 93 or params[0] != 0:
      ack, body = super(type(self), self).respond(raw)
      return ack, body
      
    return (bytearray(raw), bytearray(raw))
  def parse(self, results):
    return results
    #self.checkAck(results)


class Stick(object):
  """
    The carelink usb stick acts like a buffer.

    It has a variety of commands providing synchronous IO, eg, you may
    generally perform a read immediately after writing to it, and expect a
    response.

    The commands operate on a local buffer used to facilitate exchanging
    messages over RF with the pump. RF communication with the pump
    happens asynchronously, requiring us to go through 3 separate
    phases for each message we'd like to exchange with the pumps:
      * transmit - send commmand
      * poll_size - loop
      * download - loop

    Each command is usually only 3 bytes.

    A special command is 
  """
  link = None
  def __init__(self, link):
    self.link = link
    self.command = None

  def process(self):
    log.info('link %s processing %s)' % ( self, self.command ))
    # self.link.process(command)
    self.link.write(self.command.format( ))
    log.debug('sleeping %s' % self.command.delay)
    time.sleep(self.command.delay)
    raw = bytearray(self.link.read(self.command.size))

    if len(raw) == 0:
      log.info('zero length READ, try once more sleep .100')
      time.sleep(.100)
      self.link.write(self.command.format( ))
      log.debug('sleeping %s' % self.command.delay)
      time.sleep(self.command.delay)
      raw = bytearray(self.link.read(self.command.size))

    ack, response = self.command.respond(raw)
    info = self.command.parse(response)
    log.info('finished processing {0}, {1}'.format(self.command, repr(info)))
    return info
    
  def query(self, Command):
    self.command = command = Command( )
    return self.process( )

  def product_info(self):
    return self.query(ProductInfo)

  def interface_stats(self):
    return {'usb': self.usb_stats( ), 'radio': self.radio_stats( ) }
    
  def usb_stats(self):
    return self.query(UsbStats)

  def radio_stats(self):
    return self.query(RadioStats)

  def signal_strength(self):
    return self.query(SignalStrength)

  def poll_size(self):
    size  = self.read_status( )
    start = time.time()
    i     = 0
    log.debug('%r:STARTING POLL PHASE:attempt:%s' % (self, i))
    #while size == 0 and size < 64 and time.time() - start < 1:
    while size < 64 and time.time() - start < 1:
      log.debug('%r:poll:attempt:%s' % (self, i))
      size  = self.read_status( )
      log.debug('sleeping in POLL, .250')
      time.sleep(.250)
      i += 1
    log.info('STOP POLL after %s attempts:size:%s' % (i, size))
    return size
    
  def read_status(self):
    log.debug('read_status')
    result = self.query(LinkStatus)
    self.last_status = self.command
    return result

  def download_packet(self, size):
    log.info("download_packet:%s" % (size))
    self.command = ReadRadio(size)
    packet = self.process( )
    return packet
    
  def download(self):
    eod = False
    results  = bytearray( )
    while not eod:
      size = self.poll_size( )
      if size < 64:
        size = self.poll_size( )
      if size == 0:
        break

      #assert size > 64, ("size(%s) < 64 will break the stick" % size)

      #if size > 64:
      data = self.download_packet(size)
      results.extend(data)
      eod = self.command.eod
    return results

  def transmit_packet(self, command):
    packet = TransmitPacket(command)
    self.command = packet
    log.info('transmit_packet:write:%r' % (self.command))
    result = self.process( )
    return result

  def open(self):
    for attempt in xrange( 3 ):
      try:
        log.info('%s' % self.product_info( ))
        log.info('get signal strength of %s' % self)
        signal = 0
        while signal < 50:
          signal = self.signal_strength( )
        log.info('we seem to have found a nice signal strength of: %s' % signal)
      except AckError, e:
        log.info('failed:(%s):\n%s' % (attempt, e))
    

if __name__ == '__main__':
  import doctest
  doctest.testmod( )

  import sys
  port = None
  port = sys.argv[1:] and sys.argv[1] or False
  if not port:
    print "usage:\n%s /dev/ttyUSB0" % sys.argv[0]
    sys.exit(1)
  import link
  from pprint import pformat
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
  log.info("howdy! I'm going to take a look at your carelink usb stick.")
  stick = Stick(link.Link(port))
  stick.open( )
  log.info('test fetching product info %s' % stick)
  log.info(pformat(stick.product_info( )))
  log.info('get signal strength of %s' % stick)
  signal = 0
  while signal < 50:
    signal = stick.signal_strength( )
  log.info('we seem to have found a nice signal strength of: %s' % signal)
  log.info("""
    at this point, we could issue remote commands to a medical
    device, let's inspect the interfaces""".strip( ))
  log.info(pformat(stick.usb_stats( )))
  log.info(pformat(stick.radio_stats( )))
  size = stick.poll_size( )
  log.info("can we poll the size? %s" % (size))
  if size > 64:
    log.info("can we download ? %s" % (lib.hexdump(stick.download( ))))

#####
# EOF
