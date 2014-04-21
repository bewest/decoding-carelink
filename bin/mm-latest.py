#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from decocare import commands

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
    parser.add_argument('--no-status',
            dest="status",
            action="store_false",
            default=True,
            help="Also report current suspend/bolus status."
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
    self.time = self.clock.getData( )
  def report_status (self):
    status = self.exec_request(self.pump, commands.ReadPumpStatus)
    self.status = status.getData( )
  def report_temp (self):
    temp = self.exec_request(self.pump, commands.ReadBasalTemp)
    self.temp = temp.getData( )
    
  def report_settings (self):
    settings = self.exec_request(self.pump, commands.ReadSettings)
    self.settings = settings.getData( )
  def report_basal (self):
    profile = self.settings['selected_pattern']
    query = { 0: commands.ReadProfile_STD512
            , 1: commands.ReadProfile_A512
            , 2: commands.ReadProfile_B512
            }
    basals = self.exec_request(self.pump, query[profile])
    self.basals = basals.getData( )
  def main (self, args):
    self.report_settings( )
    if args.clock:
      self.report_clock( )
    if args.status:
      self.report_status( )
    if args.temp:
      self.report_temp( )
    if args.basal:
      self.report_basal( )

if __name__ == '__main__':
  app = LatestActivity( )
  app.run(None)

