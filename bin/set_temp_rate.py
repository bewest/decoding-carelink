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
  print "## set a temporary basal rate"
  print "hi", "`", args, "`"
  print "```"
  uart = stick.Stick(link.Link(args.port, timeout=.400))
  print "```"
  print "```"
  uart.open( )
  print "```"
  print "```"
  pump = session.Pump(uart, args.serial)
  print "```"
  print "```"
  stats = uart.interface_stats( )
  print "```"
  print "```javascript"
  print pformat(stats)
  print "```"
  print "```"
  model = pump.read_model( )
  print "```"
  print '### PUMP MODEL: `%s`' % model

  print "### existing temp basal"
  print "```"
  reader = commands.ReadBasalTemp(serial=pump.serial)
  pump.execute(reader)
  temp_basal = reader.getData( )
  print "```"
  print "```javascript"
  print pformat(temp_basal)
  print "```"

  print "### setting rate"
  print "#### sending command"
  print "```"
  #comm = commands.TempBasal(serial=device.serial, params=[ x ] )
  params = [0x00, 0x1f, 0x0a]
  comm = commands.TempBasal(serial=pump.serial, params=params)
  pump.execute(comm)
  page = comm.getData( )
  print "```"
  print "### result"
  log.info("XXX: SET TempBasal!!:\n```\n%s\n```" % lib.hexdump(page))

  print "```"
  reader = commands.ReadBasalTemp(serial=pump.serial)
  pump.execute(reader)
  temp_basal = reader.getData( )
  print "```"
  print "```javascript"
  print pformat(temp_basal)
  print "```"
  print "```"
  stats = uart.interface_stats( )
  print "```"
  print "```javascript"
  print pformat(stats)
  print "```"

if __name__ == '__main__':
  parser = get_parser( )
  args = parser.parse_args( )
  logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
  main(args)

