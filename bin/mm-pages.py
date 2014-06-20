#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from decocare import commands
import io
import json

from datetime import datetime
from dateutil import relativedelta

from decocare import lib
from decocare.history import parse_record, HistoryPage
from decocare.helpers import cli

def page_range (spec):
  r = spec.split(',')
  pages = [ ]
  for s in r:
    p = s.split('..')
    if len(p) is 2:
      pages.extend(range(int(p[0]), int(p[1]) + 1))
      continue
    p = s.split('-')
    if len(p) is 2:
      pages.extend(range(int(p[0]), int(p[1]) + 1))
      continue
    pages.append(int(s))
  return pages

class PumpPager (cli.CommandApp):
  """%(prog)s - Download and decode pages of history from pump.


  Download history pages from the pump.
  """
  def customize_parser (self, parser):
    parser.add_argument('--query',
            dest="query",
            action="store_true",
            default=False,
            help="Query number of pages available."
          )
    # subparsers = parser.add_subparsers(help="Type of pages", dest="command")
    # history_parser = subparsers.add_parser("history", help="ReadHistoryData pages")
    # history_parser.add_argument('pages'
      # )
    choices = [ 'history', 'cgm', 'vcntr' ]
    parser.add_argument('variant',
                        # action="append",
                        choices=choices,
                        help="Type of history pages to retrieve."
                        )
    parser.add_argument('range',
                        help="Page range",
                        nargs='+',
                        type=page_range
      )
    return parser

  def download_page (self, number):
    kwds = dict(page=number)
    page = self.exec_request(self.pump, commands.ReadHistoryData, args=kwds)
    return page

  def query_pages (self):
    pages = self.exec_request(self.pump, commands.ReadCurPageNumber)
    return pages.getData( )
    
  def main (self, args):
    print args
    print args.variant
    print args.range[0]
    if args.query:
      self.query_pages( )
    pages = args.range[0]
    larger = int(self.pump.model.getData( )[1:]) > 22
    records = [ ]
    for n in pages:
      history = self.download_page(n)
      page = HistoryPage(history.data)
      records.extend(page.decode( ))
    print "```json"
    print json.dumps(records, indent=2)
    print "```"


if __name__ == '__main__':
  app = PumpPager( )
  app.run(None)

