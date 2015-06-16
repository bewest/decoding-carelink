#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from decocare import commands
from decocare import lib
from decocare.helpers import cli

class BolusApp (cli.CommandApp):
  """ %(prog)s - Send bolus command to a pump.

  XXX: Be careful please!

  Units might be wrong.  Keep disconnected from pump until you trust it by
  observing the right amount first.
  """
  def customize_parser (self, parser):
    parser.add_argument('units',
                         type=float,
                         help="Amount of insulin to bolus."
                       )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--515',
                        dest='strokes_per_unit',
                        action='store_const',
                        const=10
                      )
    group.add_argument('--554',
                        dest='strokes_per_unit',
                        action='store_const',
                        const=40
                      )
    group.add_argument('--strokes',
                        dest='strokes_per_unit',
                        type=int
                      )

    return parser
  def main (self, args):
    print args
    self.bolus(args);

  def bolus (self, args):
    query = commands.Bolus
    kwds = dict(params=fmt_params(args))

    resp = self.exec_request(self.pump, query, args=kwds,
                 dryrun=args.dryrun, render_hexdump=False)
    return resp

def fmt_params (args):
  strokes = int(float(args.units) * args.strokes_per_unit)
  if (args.strokes_per_unit > 10):
    return [lib.HighByte(strokes), lib.LowByte(strokes)]
  return [strokes]

if __name__ == '__main__':
  app = BolusApp( )
  app.run(None)
