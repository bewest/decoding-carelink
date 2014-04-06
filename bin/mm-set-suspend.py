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
  parser.add_argument('--no-op',
                      dest='dryrun',
                      action='store_true', default=False,
                      help="Dry run, don't do main function"
                      )
  parser.add_argument('-v', '--verbose',
                      dest='verbose',
                      action='append_const', const=1,
                      help="Verbosity"
                      )
  parser.add_argument('--init',
                      dest='init',
                      action='store_true', default=False,
                      help="Send power ctrl to initialize RF session."
                      )
  parser.add_argument('commands',
                      nargs="+",
                      #dest='status',
                      choices=['query', 'suspend', 'resume'],
                      default='query',
                      help="Set or query pump status [default: %(default)s)]"
                      )
  argcomplete.autocomplete(parser)
  return parser

command_map = {
    'query': commands.ReadPumpStatus
  , 'suspend': commands.PumpSuspend
  , 'resume': commands.PumpResume
}

def exec_request (pump, request):
  msg = command_map.get(request)
  response = pump.query(msg)
  print "response: %s", response
  print "hexdump:",
  print "```"
  print lib.hexdump(response.data)
  print "```"
  print "##### decoded:\n```python\n", response.getData( ), "\n```"

def main (args):
  print "## query or set suspend/resume status"
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
  if args.init:
    pump.power_control( )
  model = pump.read_model( )
  print "```"
  print '### PUMP MODEL: `%s`' % model

  for flow in args.commands:
    print '### ', flow
    if args.dryrun:
      print "#### dry run, no action taken"
    else:
      exec_request(pump, flow)

  print "### end stats"
  print "```"
  stats = uart.interface_stats( )
  print "```"
  print "```javascript"
  print pformat(stats)
  print "```"

if __name__ == '__main__':
  parser = get_parser( )
  args = parser.parse_args( )
  level = None
  if args.verbose > 0:
    level = args.verbose > 1 and logging.DEBUG or logging.INFO
  logging.basicConfig(stream=sys.stdout, level=level)
  main(args)

