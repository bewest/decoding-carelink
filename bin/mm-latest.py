#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from decocare import commands
import io
import json
import argparse

from datetime import datetime
from dateutil import relativedelta

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
    parser.add_argument('minutes',
            type=int,
            nargs="?",
            default=30,
            help="[default: %(default)s)]"
          )
    return parser


  def report_clock (self):
    self.clock = self.exec_request(self.pump, commands.ReadRTC)
    self.time = lib.parse.date(self.clock.getData( ))
    self.since = self.time - self.delta

  def report_status (self):
    status = self.exec_request(self.pump, commands.ReadPumpStatus)
    self.status = status.getData( )

  def report_temp (self):
    temp = self.exec_request(self.pump, commands.ReadBasalTemp)
    self.temp = temp.getData( )
    
  def report_settings (self):
    settings = self.exec_request(self.pump, commands.ReadSettings)
    self.settings = settings.getData( )

  def report_reservoir (self):
    reservoir = self.exec_request(self.pump, commands.ReadRemainingInsulin)
    self.reservoir = reservoir.getData( )

  def report_basal (self):
    profile = self.settings['selected_pattern']
    query = { 0: commands.ReadProfile_STD512
            , 1: commands.ReadProfile_A512
            , 2: commands.ReadProfile_B512
            }
    basals = self.exec_request(self.pump, query[profile])
    self.basals = basals.getData( )

  def download_page (self, number):
    kwds = dict(page=number)
    page = self.exec_request(self.pump, commands.ReadHistoryData, args=kwds)
    return page

  def find_records (self, page, larger=None):
    if larger is None:
      larger = int(self.pump.model.getData( )[1:]) > 22
    decoder = HistoryPage(page)
    records = decoder.decode( )
    print "SINCE", self.since.isoformat( )
    for record in records:
      print "  * found record", record['_type'], record.get('timestamp')
      print "  * should quit", record['timestamp'] < self.since.isoformat( ), self.enough_history
      if record['timestamp']:
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
    self.report_settings( )
    if args.clock:
      self.report_clock( )
    if args.status:
      self.report_status( )
    if args.temp:
      self.report_temp( )
    if args.basal:
      self.report_basal( )
    if args.reservoir:
      self.report_reservoir( )
    self.download_history(args)

if __name__ == '__main__':
  app = LatestActivity( )
  app.run(None)

