
import serial
import argparse
import sys

from pprint import pprint, pformat


import pump
import logging

io = logging.getLogger( )

def get_argparser( ):
  parser = argparse.ArgumentParser( )

  parser.add_argument(
    '--port', '-p', default='/dev/ttyUSB0',
    help="path to serial port"
  )

  parser.add_argument(
    '--verbosity', '-v', 
    default=0,

    action="count",
    help="verbosity"
  )

  parser.add_argument(
    '--log', '-l', 
    default=sys.stdout,
    type=argparse.FileType('a'),
    help="log output (stdout default)"
  )

  parser.add_argument(
    'serial', default='208850',
    help="serial number of target pump (eg. 208850)"
  )

  return parser


class App(object):
  _log_map = { 0: logging.INFO, 1: logging.DEBUG,
               2: logging.WARN, 3: logging.DEBUG }
  def __init__(self):
    self.parser = get_argparser( )
    self.opts = self.parser.parse_args( )
    logging.basicConfig(stream=self.opts.log)
    if self.opts.log.name != '<stdout>':
      stdout = logging.StreamHandler(stream=sys.stdout)
      io.addHandler(stdout)

    io.setLevel(self._log_map.get(self.opts.verbosity, logging.DEBUG))

  def main(self):

    io.debug( "debug hello world!!!" )
    io.info( "info hello world!!!" )
    io.warn( "warn hello world!!!" )
    io.error( "error hello world!!!" )
    io.critical( "critical hello world!!!" )
    io.fatal( "fatal hello world!!!" )


if __name__ == '__main__':
  import doctest
  doctest.testmod( )
  
  app = App( )
  app.main( )

#####
# EOF
