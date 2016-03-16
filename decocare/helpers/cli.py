import sys, os
import logging
import time
import argparse
from pprint import pformat

log = logging.getLogger( ).getChild(__name__)

from decocare import link, stick, session, commands, lib, scan

class CommandApp(object):
  def __init__(self):
    self.env = self.parse_env( )
    self.parser = self.get_parser( )
    self.autocomplete( )

  @classmethod
  def parse_env (klass):
    return {
     "serial": os.environ.get('SERIAL', ''),
     "port": os.environ.get('PORT', '')
    }

  def autocomplete (self):
    try:
      import argcomplete
      argcomplete.autocomplete(self.parser)
    except ImportError:
      # no auto completion
      pass

  def help (self):
    return self.__class__.__doc__

  def get_parser (self):
    helptext = self.help( ).split("\n")
    description = '\n'.join(helptext[0:2])
    epilog = '\n'.join(helptext[2:])
    parser = argparse.ArgumentParser(description=description, epilog=epilog)
    parser.add_argument('--serial', type=str,
                        dest='serial',
                        default=self.env.get('serial', ''),
                        help="serial number of pump [default: %(default)s]")
    parser.add_argument('--port', type=str,
                        dest='port',
                        default=(self.env.get('port') or 'scan'),
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
    parser.add_argument('--rf-minutes',
                        dest='session_life',
                        type=int, default=10,
                        help="How long RF sessions should last"
                        )
    parser.add_argument('--auto-init',
                        dest='autoinit',
                        action='store_true', default=False,
                        help="Send power ctrl to initialize RF session."
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
    if args.port == 'scan' or args.port == "":
      args.port = scan.scan( )
    uart = stick.Stick(link.Link(args.port))
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
    if not args.autoinit:
      if args.init:
        pump.power_control(minutes=args.session_life)
      model = pump.read_model( )
      self.model = model
    else:
      self.autoinit(args)
    print "```"
    print '### PUMP MODEL: `%s`' % self.model

  def autoinit (self, args):
    for n in xrange(3):
      print "AUTO INIT", n
      self.sniff_model( )
      if len(self.model.getData( )) != 3:
        self.stats
        print "SENDING POWER ON", n
        self.pump.power_control(minutes=args.session_life)
      else:
        print '### PUMP MODEL: `%s`' % self.model
        break
  def sniff_model (self):
    model = self.pump.read_model( )
    print "GOT MODEL", model
    self.model = model
  def postlude (self, args):
    if args.no_postlude:
      print "##### skipping postlude"
      return
    print "### end stats"
    self.stats( )
  def stats (self):
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
        self.exec_request(self.pump, flow)


  def exec_request (self, pump, msg, args={},
                    dryrun=False,
                    save=False,
                    prefix='',
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
      print repr(response.getData( ))
      print "```"
    if save:
      response.save(prefix=prefix)
    return response

