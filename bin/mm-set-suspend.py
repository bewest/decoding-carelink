#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from decocare import commands
from decocare.helpers import cli

class SetSuspendResumeApp (cli.CommandApp):
  """ %(prog)s -  query or set suspend/resume status

  Pause or resume pump.
  """
  def customize_parser (self, parser):
    parser.add_argument('commands',
                        nargs="+",
                        choices=['query', 'suspend', 'resume'],
                        default='query',
                        help="Set or query pump status [default: %(default)s)]"
                        )
    return parser

  def exec_request (self, pump, msg, **kwds):
    msg = lookup_command(msg)
    super(SetSuspendResumeApp, self).exec_request(pump, msg, **kwds)

command_map = {
    'query': commands.ReadPumpStatus
  , 'suspend': commands.PumpSuspend
  , 'resume': commands.PumpResume
}

def lookup_command (name):
  return command_map.get(name)

if __name__ == '__main__':
  app = SetSuspendResumeApp( )
  app.run(None)

