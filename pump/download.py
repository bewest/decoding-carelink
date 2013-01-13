
import logging
log = logging.getLogger( ).getChild(__name__)

import lib
import commands

class Downloader(object):
  log_format = 'logs/'
  def __init__(self, stick=None, device=None, log_format=log_format):
    self.stick = stick
    stick.open( )
    self.device = device
    self.log_format = log_format

  def download(self):

    log.info("read HISTORY DATA")
    comm = commands.ReadHistoryData(serial=self.device.serial, page=0)
    self.device.execute(comm)
    log.info('comm:READ history data page!!!:\n%s' % (lib.hexdump(comm.getData( ))))
    comm.save(prefix=self.log_format)

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
  log.info("howdy! I'm going to take a look at your pump download something info.")
  stick = stick.Stick(link.Link(port, timeout=.400))
  stick.open( )
  session = session.Pump(stick, '208850')
  log.info(pformat(stick.interface_stats( )))

  downloader = Downloader(stick, session)
  downloader.download( )

  log.info(pformat(stick.interface_stats( )))
  log.info("howdy! we downloaded everything.")
