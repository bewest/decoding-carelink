#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from decocare import commands
import io
import json
import argparse

from datetime import datetime
from dateutil import relativedelta
from dateutil.parser import parse
from dateutil.tz import gettz

from decocare import lib
from decocare.history import parse_record, HistoryPage
from decocare.helpers import cli

class LatestActivity (cli.CommandApp):
  """%(prog)s - Grab latest activity


  Query pump for latest activity.
  """
  def customize_parser (self, parser):
    parser.add_argument('--no-clock',
            dest="clock",
            action="store_false",
            default=True,
            help="Also report current time on pump."
          )
    parser.add_argument('--no-basal',
            dest="basal",
            action="store_false",
            default=True,
            help="Also report basal rates."
          )
    parser.add_argument('--no-temp',
            dest="temp",
            action="store_false",
            default=True,
            help="Also report temp basal rates."
          )
    parser.add_argument('--no-reservoir',
            dest="reservoir",
            action="store_false",
            default=True,
            help="Also report remaining insulin in reservoir."
          )
    parser.add_argument('--no-status',
            dest="status",
            action="store_false",
            default=True,
            help="Also report current suspend/bolus status."
          )
    parser.add_argument('--parser-out',
            dest="parsed_data",
            default='-',
            type=argparse.FileType('w'),
            help="Put history json in this file"
          )
    parser.add_argument('--rtc-out',
            dest="rtc_archive",
            default='-',
            type=argparse.FileType('w'),
            help="Put clock json in this file"
          )
    parser.add_argument('--reservoir-out',
            dest="reservoir_archive",
            default='-',
            type=argparse.FileType('w'),
            help="Put reservoir json in this file"
          )
    parser.add_argument('--settings-out',
            dest="settings",
            default='-',
            type=argparse.FileType('w'),
            help="Put settings json in this file"
          )
    parser.add_argument('--temp-basal-status-out',
            dest="tempbasal",
            default='-',
            type=argparse.FileType('w'),
            help="Put temp basal status json in this file"
          )
    parser.add_argument('--basals-out',
            dest="basals",
            default='-',
            type=argparse.FileType('w'),
            help="Put basal schedules json in this file"
          )
    parser.add_argument('--status-out',
            dest="status",
            default='-',
            type=argparse.FileType('w'),
            help="Put status json in this file"
          )
    parser.add_argument('--timezone',
            default=gettz( ),
            type=gettz,
            help="Timezone to use"
          )
    parser.add_argument('minutes',
            type=int,
            nargs="?",
            default=30,
            help="[default: %(default)s)]"
          )
    return parser


  def report_clock (self, args):
    self.clock = self.exec_request(self.pump, commands.ReadRTC)
    self.time = lib.parse.date(self.clock.getData( ))
    self.time = self.time.replace(tzinfo=args.timezone)
    self.timezone = args.timezone
    self.since = self.time - self.delta
    results = dict(now=self.time.isoformat( )
              , observed_at=datetime.now(args.timezone).isoformat( )
              , model=self.pump.modelNumber
              , _type='RTC')

    print "```json"
    args.rtc_archive.write(json.dumps(results, indent=2))
    print ''
    print "```"

  def report_status (self, args):
    status = self.exec_request(self.pump, commands.ReadPumpStatus)
    self.status = status.getData( )
    args.status.write(json.dumps(self.status, indent=2))

  def report_temp (self, args):
    temp = self.exec_request(self.pump, commands.ReadBasalTemp)
    self.temp = temp.getData( )
    args.tempbasal.write(json.dumps(self.temp, indent=2))
    
  def report_settings (self, args):
    settings = self.exec_request(self.pump, commands.ReadSettings)
    self.settings = settings.getData( )
    args.settings.write(json.dumps(self.settings, indent=2))

  def report_reservoir (self, args):
    reservoir = self.exec_request(self.pump, commands.ReadRemainingInsulin)
    self.reservoir = reservoir.getData( )
    args.reservoir_archive.write(json.dumps(self.reservoir, indent=2))

  def report_basal (self, args):
    profile = self.settings['selected_pattern']
    query = { 0: commands.ReadProfile_STD512
            , 1: commands.ReadProfile_A512
            , 2: commands.ReadProfile_B512
            }
    basals = self.exec_request(self.pump, query[profile])
    self.basals = basals.getData( )
    args.basals.write(json.dumps(self.basals, indent=2))

  def download_page (self, number):
    kwds = dict(page=number)
    page = self.exec_request(self.pump, commands.ReadHistoryData, args=kwds)
    return page

  def find_records (self, page, larger=None):
    decoder = HistoryPage(page, self.pump.model)
    records = decoder.decode( )
    print "SINCE", self.since.isoformat( )
    for record in records:
      print "  * found record", record['_type'], record.get('timestamp')
      print "  * should quit", record.get('timestamp') < self.since.isoformat( ), self.enough_history
      if record.get('timestamp'):
        dt = parse(record['timestamp'])
        dt = dt.replace(tzinfo=self.timezone)
        record.update(timestamp=dt.isoformat( ))
        if record['timestamp'] < self.since.isoformat( ):
          self.enough_history = True
        if record['timestamp'] >= self.since.isoformat( ):
          self.records.append(record)
    return records

  def download_history (self, args):
    i = 0
    print "find records since", self.since.isoformat( )
    self.enough_history = False
    self.records = [ ]
    while not self.enough_history:
      history = self.download_page(i)
      remainder = self.find_records(history.data)
      i = i + 1
    results = self.records
    print "```json"
    args.parsed_data.write(json.dumps(results, indent=2))
    print ''
    print "```"

  def main (self, args):
    self.delta = relativedelta.relativedelta(minutes=args.minutes)
    self.report_settings(args)
    if args.clock:
      self.report_clock(args )
    if args.status:
      self.report_status(args)
    if args.temp:
      self.report_temp(args)
    if args.basal:
      self.report_basal(args)
    if args.reservoir:
      self.report_reservoir(args)
    self.download_history(args)

if __name__ == '__main__':
  app = LatestActivity( )
  app.run(None)

