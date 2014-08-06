#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from decocare import commands
from decocare.helpers import cli

class BolusApp (cli.CommandApp):
  """ %(prog)s - Send bolus command to a pump.

  XXX: Be careful please.

  Units might be wrong.  Keep disconnected from pump until you trust it by
  observing the right amount first.
  """
  def customize_parser (self, parser):

    parser.add_argument('--units',
                        dest='strokes',
                        type=fmt_params,
                        help="Amount of insulin to bolus. [default: %(default)s)]"
                        )

    return parser
  def main (self, args):
    print args
    self.bolus(args);

  def bolus (self, args):
    query = commands.Bolus
    kwds = dict(params=[args.strokes])

    resp = self.exec_request(self.pump, query, args=kwds,
                 dryrun=args.dryrun, render_hexdump=False)
    return resp

def fmt_params (units):
  return int(float(units) * 10)

if __name__ == '__main__':
  app = BolusApp( )
  app.run(None)
