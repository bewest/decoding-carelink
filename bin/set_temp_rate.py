#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argcomplete, argparse
import sys, os
from decocare import link, stick, session, commands, lib
from pprint import pformat
import logging
log = logging.getLogger( ).getChild(__name__)

def parse_env ( ):
  return {
   "serial": os.environ.get('SERIAL', ''),
   "port": os.environ.get('PORT', '')
  }

def get_parser ( ):
  conf = parse_env( )
  parser = argparse.ArgumentParser( )
  parser.add_argument('--serial', type=str,
                      dest='serial',
                      default=conf.get('serial', ''),
                      help="serial number of pump [default: %(default)s]")
  parser.add_argument('--port', type=str,
                      dest='port',
                      default=conf.get('port', ''),
                      help="Path to device [default: %(default)s]")
  parser.add_argument('--duration',
                      dest='duration',
                      type=int, default=0,
                      help="Duration of temp rate [default: %(default)s)]"
                      )
  parser.add_argument('--rate',
                      dest='rate',
                      type=int, default=0,
                      help="Rate of temp basal [default: %(default)s)]"
                      )
  argcomplete.autocomplete(parser)
  return parser

def main (args):
  print "hi", args
  uart = stick.Stick(link.Link(args.port, timeout=.400))
  uart.open( )
  pump = session.Pump(uart, args.serial)
  log.info(pformat(uart.interface_stats( )))
  log.info('PUMP MODEL: %s' % pump.read_model( ))

  #comm = commands.TempBasal(serial=device.serial, params=[ x ] )
  comm = commands.TempBasal(serial=pump.serial, params=[0x00, 0x20, 0x07])
  pump.execute(comm)
  page = comm.getData( )
  log.info("XXX: SET TempBasal!!:\n%s" % lib.hexdump(page))
  log.info(pformat(uart.interface_stats( )))

if __name__ == '__main__':
  parser = get_parser( )
  args = parser.parse_args( )
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
  main(args)

