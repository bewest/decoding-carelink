#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from decocare import commands
from decocare.helpers import cli

class PressKeysApp (cli.CommandApp):
  """%(prog)s - Simulate presses on the keypad.


  Press keys on the keypad.
  """
  def customize_parser (self, parser):
    parser.add_argument('commands',
                        nargs="+",
                        choices=['act', 'esc', 'up', 'down', 'easy' ],
                        # default='act',
                        help="buttons to press [default: %(default)s)]"
                        )
    return parser

  def exec_request (self, pump, msg, **kwds):
    msg = lookup_command(msg)
    super(PressKeysApp, self).exec_request(pump, msg, **kwds)

command_map = {
    'easy': commands.PushEASY,
    'esc': commands.PushESC,
    'act': commands.PushACT,
    'down': commands.PushDOWN,
    'up': commands.PushUP
}

def lookup_command (name):
  return command_map.get(name)

if __name__ == '__main__':
  app = PressKeysApp( )
  app.run(None)

