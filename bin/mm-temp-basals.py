#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from decocare import commands
from decocare.helpers import cli
import argparse
import json

class TempBasalApp (cli.CommandApp):
  """ %(prog)s -  query or set temp basals

  Set or query temp basals.
  """
  def customize_parser (self, parser):
    parser.add_argument('command',
                        choices=['query', 'set', 'percent'],
                        default='query',
                        help="Set or query pump status [default: %(default)s)]"
                        )
    parser.add_argument('--duration',
                        dest='duration',
                        type=int, default=0,
                        help="Duration of temp rate [default: %(default)s)]"
                        )
    parser.add_argument('--rate',
                        dest='rate',
                        type=float, default=0,
                        help="Rate of temp basal [default: %(default)s)]"
                        )
    parser.add_argument('--out',
            dest="out",
            default='-',
            type=argparse.FileType('w'),
            help="Put basal in this file"
          )
    """
    subparsers = parser.add_subparsers(help="Main thing to do", dest="command")
    basals_parser = subparsers.add_parser("set", help="Just basals between command sets")
    basals_parser.add_argument('--duration',
                        dest='duration',
                        type=int, default=0,
                        help="Duration of temp rate [default: %(default)s)]"
                        )
    basals_parser.add_argument('--rate',
                        dest='rate',
                        type=float, default=0,
                        help="Rate of temp basal [default: %(default)s)]"
                        )
    """
    return parser
  def main (self, args):
    basals = self.query_temp(args)
    if args.command == "query":
      pass
    if args.command == "percent":
      params = format_percent_params(args)
      kwds = dict(params=params)
      msg = commands.TempBasalPercent
      resp = self.exec_request(self.pump, msg, args=kwds,
                   dryrun=args.dryrun, render_hexdump=True )
      basals = self.query_temp(args)
    if args.command == "set":
      params = format_params(args)
      kwds = dict(params=params)
      msg = commands.TempBasal
      resp = self.exec_request(self.pump, msg, args=kwds,
                   dryrun=args.dryrun, render_hexdump=True )
      basals = self.query_temp(args)

      # (serial=pump.serial, params=params)
    args.out.write(json.dumps(basals, indent=2))

  def query_temp (self, args):
    query = commands.ReadBasalTemp

    resp = self.exec_request(self.pump, query,
                 dryrun=args.dryrun, render_hexdump=False)
    results = resp.getData( )
    return results;

def format_percent_params (args):
  duration = int(args.duration / 30)
  rate = int(args.rate)
  params = [rate, duration]
  return params

def format_params (args):
  duration = args.duration / 30
  rate = int(args.rate / 0.025)
  params = [0x00, rate, duration]
  return params

if __name__ == '__main__':
  app = TempBasalApp( )
  app.run(None)

