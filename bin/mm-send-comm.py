#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
import argparse
import sys, os
from decocare import link, stick, session, commands, lib
from pprint import pformat
import logging
import time
log = logging.getLogger( ).getChild(__name__)

def parse_env ( ):
  return {
   "serial": os.environ.get('SERIAL', ''),
   "port": os.environ.get('PORT', '')
  }


class CommandApp(object):
  def __init__(self):
    self.env = parse_env( )
    self.parser = self.get_parser( )
    self.autocomplete( )

  def autocomplete (self):
    try:
      import argcomplete
      argcomplete.autocomplete(self.parser)
    except ImportError:
      # no auto completion
      pass

  def get_parser (self):
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
    parser.add_argument('--skip-prelude',
                        dest='no_prelude',
                        action='store_true', default=False,
                        help="Don't do the normal prelude."
                        )
    parser.add_argument('--no-rf-prelude',
                        dest='no_rf_prelude',
                        action='store_true', default=False,
                        help="Do the prelude, but don't query the pump."
                        )
    parser.add_argument('--skip-postlude',
                        dest='no_postlude',
                        action='store_true', default=False,
                        help="Don't do the normal postlude."
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
    parser = self.customize_parser(parser)
    return parser

  def customize_parser (self, parser):
    parser.add_argument('commands',
                        nargs="+",
                        #dest='status',
                        choices=['act', 'esc', 'up', 'down', 'easy' ],
                        default='act',
                        help="buttons to press [default: %(default)s)]"
                        )
    return parser

  def configure (self):
    args = self.parser.parse_args( )
    level = None
    if args.verbose > 0:
      level = args.verbose > 1 and logging.DEBUG or logging.INFO
    logging.basicConfig(stream=sys.stdout, level=level)
    self.args = args
    return args

  def run (self, args):
    if not args:
      args = self.configure( )
    self.prelude(args)
    self.main(args)
    self.postlude(args)

  def prelude (self, args):
    if args.no_prelude:
      print "##### skipping prelude"
      return
    print "## do stuff with an insulin pump over RF"
    print "using", "`", args, "`"

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
    self.uart = uart
    self.pump = pump
    self.model = None
    if args.no_rf_prelude:
      print "##### skipping normal RF preludes"
      return
    print "```"
    if args.init:
      pump.power_control( )
    model = pump.read_model( )
    self.model = model
    print "```"
    print '### PUMP MODEL: `%s`' % model

  def postlude (self, args):
    if args.no_postlude:
      print "##### skipping postlude"
      return
    print "### end stats"
    print "```"
    stats = self.uart.interface_stats( )
    print "```"
    print "```javascript"
    print pformat(stats)
    print "```"

  def main (self, args):
    for flow in args.commands:
      print '### ', flow
      if args.dryrun:
        print "#### dry run, no action taken"
      else:
        exec_request(self.pump, flow)

command_map = {
    'easy': commands.KeypadPush.EASY,
    'esc': commands.KeypadPush.ESC,
    'act': commands.KeypadPush.ACT,
    'down': commands.KeypadPush.DOWN,
    'up': commands.KeypadPush.UP,
}

def exec_request (pump, msg, args={},
                  dryrun=False,
                  render_decoded=True,
                  render_hexdump=True):
  if dryrun:
    print "skipping query", pump, msg, args
    return False
  response = pump.query(msg, **args)
  print "response: %s" % response
  if render_hexdump:
    print "hexdump:"
    print "```python"
    print response.hexdump( )
    print "```"
  if render_decoded:
    print "#### decoded:"
    print "```python"
    print response.getData( )
    print "```"
  return response

class SendMsgApp(CommandApp):
  def main (self, args):
    if args.prefix:
      self.execute_list(args.prefix)
    if args.command == "ManualCommand":
      kwds = {
          'params': map(int, getattr(args, 'params', [ ])),
          'retries': getattr(args, 'retries', 0),
          'effectTime': getattr(args, 'effectTime'),
          'code': args.code,
          'name': getattr(args, 'name', "ExperimentCode%02x" % args.code),
          'descr': getattr(args, 'descr', "Experimental msg")
        }
      msg = commands.ManualCommand
      exec_request(self.pump, msg, args=kwds, dryrun=args.dryrun, render_hexdump=False)
    if args.command == "sleep":
      time.sleep(args.timeout)
    if args.postfix:
      self.execute_list(args.postfix)

  def execute_list (self, messages):
    for name in messages:
      msg = getattr(commands, name)
      print msg
      exec_request(self.pump, msg, dryrun=self.args.dryrun, render_hexdump=self.args.verbose>0)

  def customize_parser (self, parser):
    choices = commands.__all__
    parser.add_argument('--prefix',
                        action="append",
                        choices=choices,
                        help="Built-in commands to run before the main one."
                        )

    parser.add_argument('--postfix',
                        action="append",
                        choices=choices,
                        help="Built-in commands to run after the main one."
                        )

    subparsers = parser.add_subparsers(help="commands", dest="command")
    sleep_parser = subparsers.add_parser("sleep", help="Just sleep between command sets")
    sleep_parser.add_argument('timeout', type=float, default=2)
    all_parser = subparsers.add_parser("ManualCommand", help="Customize a command")
    all_parser.add_argument('code', type=int
                           )
    #__fields__ = ['maxRecords', 'code', 'descr',
    #            'serial', 'bytesPerRecord', 'retries', 'params']
    all_parser.add_argument('--params', type=str, action="append",
                            default=commands.ManualCommand.params
                           )
    all_parser.add_argument('--descr', type=str, default="Experimental command"
                           )
    all_parser.add_argument('--name', type=str
                           )
    all_parser.add_argument('--save', type=str
                           )
    all_parser.add_argument('--effectTime', type=float,
                            default=commands.ManualCommand.effectTime
                           )
    all_parser.add_argument('--maxRecords', type=int,
                            default=commands.ManualCommand.maxRecords
                           )
    all_parser.add_argument('--bytesPerRecord', type=int,
                            default=commands.ManualCommand.bytesPerRecord
                           )

    return parser


if __name__ == '__main__':
  app = SendMsgApp( )
  app.run(None)

