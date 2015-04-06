#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from decocare import commands
from decocare.helpers import cli
import argparse
from decocare import lib
from dateutil.tz import gettz
from datetime import datetime
import time
import json

class SetRTCApp (cli.CommandApp):
  """ %(prog)s -  query or set RTC

  Set or query RTC.
  """
  def customize_parser (self, parser):
    parser.add_argument('command',
                        choices=['query', 'set', ],
                        default='query',
                        help="Set or query pump status [default: %(default)s)]"
                        )
    parser.add_argument('--rtc-out',
            dest="rtc_archive",
            default='-',
            type=argparse.FileType('w'),
            help="Put clock json in this file"
          )
    parser.add_argument('--timezone',
            default=gettz( ),
            type=gettz,
            help="Timezone to use"
          )
    parser.add_argument('--set',
            dest="set",
            required=True,
            type=lib.parse.date,
            help="Set clock to new value (iso8601)"
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
  def report_clock (self, args):
    self.clock = self.exec_request(self.pump, commands.ReadRTC)
    new_time = lib.parse.date(self.clock.getData( ))
    self.time = new_time
    return self.render_clock(self.clock)

  def render_clock (self, clock):
    new_time = lib.parse.date(clock.getData( ))
    new_time =  new_time.replace(tzinfo=self.args.timezone)
    results = dict(clock=new_time.isoformat( )
              , observed_at=datetime.now(self.args.timezone).isoformat( )
              , model=self.pump.model.getData( )
              , _type='RTC')

    print "```json"
    self.args.rtc_archive.write(json.dumps(results, indent=2))
    print ''
    print "```"
    return results

  def set_clock (self, args):
    msg = commands.SetRTC
    kwds = dict(params=commands.SetRTC.fmt_datetime(args.set))
    new_clock = self.exec_request(self.pump, msg, args=kwds)
    # self.render_clock(new_clock)
    return new_clock
  def main (self, args):
    if args.dryrun:
      print args.set
      print lib.hexdump(bytearray(commands.SetRTC.fmt_datetime(args.set)))
      # clocked = lib.parse.date(self.clock.getData( ))
      return
    clock = self.report_clock(args)
    if args.command == "query":
      pass
    if args.command == "set":

      new_clock = self.set_clock(args)

      time.sleep(1)
      clock = self.report_clock(args)

      # (serial=pump.serial, params=params)
    args.out.write(json.dumps(clock, indent=2))

  def query_temp (self, args):
    query = commands.ReadBasalTemp

    resp = self.exec_request(self.pump, query,
                 dryrun=args.dryrun, render_hexdump=False)
    results = resp.getData( )
    return results;

if __name__ == '__main__':
  app = SetRTCApp( )
  app.run(None)

