import logging
import time

log = logging.getLogger( ).getChild(__name__)
import commands
import lib
import models
from errors import StickError, AckError, BadDeviceCommError


class Session(object):
  def __init__(self, stick):
    self.stick = stick
    self.should_download = True
  def init(self, skip_power_control=False):
    stick = self.stick
    log.info('test fetching product info %s' % stick)
    log.info(pformat(stick.product_info( )))
    log.info('get signal strength of %s' % stick)
    signal = 0
    while signal < 50:
      signal = stick.signal_strength( )
    log.info('we seem to have found a nice signal strength of: %s' % signal)
  def end(self):
    stick = self.stick
    log.info(pformat(stick.usb_stats( )))
    log.info(pformat(stick.radio_stats( )))

  def execute(self, command):
    self.command = command
    for i in xrange(max(1, self.command.retries)):
      log.info('execute attempt: %s' % (i + 1))
      try:
        self.expectedLength = self.command.bytesPerRecord * self.command.maxRecords
        self.transfer( )
        if self.should_download:
          log.info('sleeping %s before download' % command.effectTime)
          time.sleep(command.effectTime)
          self.download( )
        log.info('finished executing:%s' % command)
        if command.done( ):
          return command
      except BadDeviceCommError, e:
        log.critical("ERROR: %s" % e)
        # self.clearBuffers( )
    log.critical('this seems like a problem')

  def download(self):
    errors = [ ]
    if self.expectedLength > 0:
      log.info('proceeding with download')
      data = self.stick.download( )
      #self.command.data = data
      self.command.respond(data)
      return data
    else:
      log.info('no download required')
    assert not errors, ("with errors:%s" %"\n".join( map(str, errors) ))
  def transfer(self):
    log.info('session transferring packet')
    return self.stick.transmit_packet(self.command)

class Pump(Session):
  def __init__(self, stick, serial='208850'):
    super(type(self), self).__init__(stick)
    self.serial = serial
    log.info('setting up to talk with %s' % serial)

  def power_control(self, minutes=None):
    log.info('BEGIN POWER CONTROL %s' % self.serial)
    # print "PowerControl SERIAL", self.serial
    response = self.query(commands.PowerControl, minutes=minutes)
    power = self.command
    log.info('manually download PowerControl serial %s' % self.serial)
    data = self.stick.download( )
    log.info("ENDING manual download:\n%s" % lib.hexdump(data))
    return data

  def setModel (self, model=None, number=None):
    if number:
      self.model = models.lookup(number, self)
    if model:
      self.model = model
  def read_model(self):
    model = self.query(commands.ReadPumpModel)
    self.modelNumber = model.getData( )
    self.setModel(number=self.modelNumber)
    return model

  def read_history_0(self):
    log.info("read HISTORY DATA")
    comm = commands.ReadHistoryData(serial=self.serial, page=0)
    self.execute(comm)
    log.info('comm:READ history data page!!!:\n%s' % (comm.getData( )))

  def execute(self, command):
    command.serial = self.serial
    return super(type(self), self).execute(command)
  def query(self, Command, **kwds):
    command = Command(serial=self.serial, **kwds)
    self.execute(command)
    return command

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
  from pprint import pformat
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
  log.info("howdy! I'm going to take a look at your pump.")
  stick = stick.Stick(link.Link(port, timeout=.200))
  stick.open( )
  session = Pump(stick, serial_num)
  log.info(pformat(stick.interface_stats( )))
  session.power_control( )
  log.info(pformat(stick.interface_stats( )))
  log.info('PUMP MODEL: %s' % session.read_model( ))
  log.info(pformat(stick.interface_stats( )))
  log.info('PUMP READ PAGE 0: %s' % session.read_history_0( ))
  log.info(pformat(stick.interface_stats( )))
  log.info("howdy! all done looking at pump")
  # stick.open( )

#####
# EOF
