import time
from pprint import pformat
from cli import CommandApp
from decocare import link, stick, session, commands, lib, scan

def get_parser ( ):
  app = SendMsgApp( )
  return app.get_parser( )

class SendMsgApp(CommandApp):
  """
  %(prog)s - send messages to a compatible MM insulin pump

  This tool is intended to help discover protocol behavior.
  Under no circumstance is it intended to deliver therapy.
  """
  def main (self, args):
    if args.prefix:
      self.execute_list(args.prefix, args.saveall)
    if args.command == "ManualCommand":
      kwds = {
          'params': map(int, getattr(args, 'params', [ ])),
          'retries': getattr(args, 'retries', 0),
          'effectTime': getattr(args, 'effectTime'),
          'maxRecords': getattr(args, 'maxRecords'),
          'bytesPerRecord': getattr(args, 'bytesPerRecord'),
          'code': args.code,
          'name': getattr(args, 'name', "ExperimentCode%02x" % args.code),
          'descr': getattr(args, 'descr', "Experimental msg")
        }
      msg = commands.ManualCommand
      resp = self.exec_request(self.pump, msg, args=kwds,
                   dryrun=args.dryrun, render_hexdump=False, save=args.save, prefix=args.prefix_path)
    if args.command == "sleep":
      time.sleep(args.timeout)
    if args.command == "tweak":
      Other = getattr(commands, args.other)
      kwds = commands.TweakAnotherCommand.get_kwds(Other, args)
      print Other, kwds
      resp = self.exec_request(self.pump, Other, args=kwds,
                   dryrun=args.dryrun, save=args.save, prefix=args.prefix_path)
    if args.postfix:
      self.execute_list(args.postfix, args.saveall)

  def execute_list (self, messages, save=False):
    for name in messages:
      msg = getattr(commands, name)
      print "###### sending `%s`" % getattr(msg, 'name', msg)
      resp = self.exec_request(self.pump, msg, dryrun=self.args.dryrun,
                          render_hexdump=self.args.verbose>0,
                          save=save, prefix=self.args.prefix_path)

  def customize_parser (self, parser):
    choices = commands.__all__
    choices.sort( )
    parser.add_argument('--prefix-path',
                        dest="prefix_path",
                        type=str,
                        default="",
                        help="Prefix to store saved files when using --save or --saveall."
                        )
    parser.add_argument('--saveall',
                        action="store_true",
                        default=False,
                        help="Whether or not to save all responses.",
                        )

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

    subparsers = parser.add_subparsers(help="Main thing to do between --prefix and--postfix", dest="command")
    sleep_parser = subparsers.add_parser("sleep", help="Just sleep between command sets")
    sleep_parser.add_argument('timeout', type=float, default=0,
                              help="Sleep in between running --prefix and --postfix"
                              )
    tweaker = subparsers.add_parser("tweak", help="Tweak a builtin command")
    tweaker.add_argument('other',
                        choices=choices,
                        help="Command to tweak."
                        )
    commands.TweakAnotherCommand.config_argparse(tweaker)
    all_parser = subparsers.add_parser("ManualCommand", help="Customize a command")
    all_parser.add_argument('code', type=int,
                            help="The opcode to send to the pump."
                           )
    #__fields__ = ['maxRecords', 'code', 'descr',
    #            'serial', 'bytesPerRecord', 'retries', 'params']
    all_parser.add_argument('--params', type=str, action="append",
                            help="parameters to format into sent message",
                            default=commands.ManualCommand.params
                           )
    all_parser.add_argument('--params_hexline', dest='params', type=lib.decode_hexline,
                            help="hex string, parameters to format into sent message"
                            # default=commands.ManualCommand.params
                           )


    all_parser.add_argument('--descr', type=str, default="Experimental command",
                            help="Description of command"
                           )
    all_parser.add_argument('--name', type=str,
                            help="Proposed name of command"
                           )
    all_parser.add_argument('--save', action="store_true", default=False,
                            help="Save response in a file."
                           )
    all_parser.add_argument('--effectTime', type=float,
                            help="time to sleep before responding to message, float in seconds",
                            default=commands.ManualCommand.effectTime
                           )
    all_parser.add_argument('--maxRecords', type=int,
                            help="number of frames in a packet composing payload response",
                            default=commands.ManualCommand.maxRecords
                           )
    all_parser.add_argument('--bytesPerRecord', type=int,
                            help="bytes per frame",
                            default=commands.ManualCommand.bytesPerRecord
                           )

    return parser

