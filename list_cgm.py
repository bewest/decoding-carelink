import sys
import argparse

# TODO: should probably be able to remove this stuff
from pprint import pprint, pformat
from decocare import cgm
# this stuff will stay
def get_opt_parser( ):
  parser = argparse.ArgumentParser( )
  parser.add_argument('infile', nargs="+",
                      default=sys.stdin,
                      type=argparse.FileType('r'),
                      help="Find dates in this file.")

  parser.add_argument('--out',
                      default=sys.stdout,
                      type=argparse.FileType('w'),
                      help="Write records here.")
  parser.add_argument('--larger',
                      dest='larger', action='store_true')
  parser.add_argument('--no-larger',
                      dest='larger', action='store_false')

  return parser


import json
class ListCGM (object):

  def print_records (self, records, opts={}):
    print json.dumps(records, indent=2)
  def main(self):
    parser = get_opt_parser( )
    opts = parser.parse_args( )
    self.records = [ ]
    for stream in opts.infile:
      page = cgm.PagedData(stream, larger=opts.larger)
      self.records.extend(page.decode( ))

    self.print_records(self.records)

if __name__ == '__main__':
  app = ListCGM( )
  app.main( )
#####
