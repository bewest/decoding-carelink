#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from decocare import commands, models, cgm
import json, argparse, sys

from decocare.history import HistoryPage
from decocare.helpers import cli

from dateutil.parser import parse
from dateutil.tz import gettz

class DownloadHistory (cli.CommandApp):
    """%(prog)s - Grab history
    """
    def customize_parser (self, parser):

        parser.add_argument('--model',
                            # type=get_model,
                            choices=models.known.keys( ))

        parser.add_argument('--timezone',
                            default=gettz( ),
                            type=gettz,
                            help="Timezone to use")
        parser.add_argument('--parser-out',
                            dest="parsed_data",
                            default='-',
                            type=argparse.FileType('w'),
                            help="Put history json in this file")
        return parser


    def download_page (self, number):
        return self.exec_request(self.pump, commands.ReadGlucoseHistory, args=dict(page=number), render_decoded=False,render_hexdump=False)

    def download_history (self, args, pageRange):
        records = [ ]
        for i in range(1 + pageRange['page'] - pageRange['isig'], pageRange['page']):
            print "Next page ", i
            try:
                pageRaw = self.download_page(i).data
                pageResult = cgm.PagedData.Data(pageRaw)
                records.extend(pageResult.decode())
            except:
                print "Unexpected error when downloading cgm-page ", i, " from pump:", sys.exc_info()[0]

        recordsJson = json.dumps(records);
        args.parsed_data.write(recordsJson)

        handle = open('glucose.json', 'wb')
        handle.write(recordsJson)
        handle.close( )

    def getPagesRange(self):
        range = self.exec_request(self.pump, commands.ReadCurGlucosePageNumber, render_decoded=False,render_hexdump=False)
        return range.getData( )

    def main (self, args):
        # Set Global variables..
        self.timezone = args.timezone

        info = self.getPagesRange()
        self.download_history(args, info)

if __name__ == '__main__':
    app = DownloadHistory( )
    app.run(None)

