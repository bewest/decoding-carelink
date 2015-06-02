#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from decocare import commands, models
import json, argparse

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

    def find_records (self, page):
        decoder = HistoryPage(page, self.pump.model)
        records = decoder.decode( )

        print "Found " , len(records), " records."
        for record in records:
            print "  * found record", record.get('timestamp'), record['_type']
            if record.get('timestamp'):
                dt = parse(record['timestamp'])
                dt = dt.replace(tzinfo=self.timezone)
                record.update(timestamp=dt.isoformat( ))
        return records

    def download_history (self, args):
        records = [ ]
        for i in range(0, 10):
            print "Next page ", i
            pageHistory = self.download_page(i)
            records.extend(self.find_records(pageHistory.data))
        args.parsed_data.write(json.dumps(records))

    def getRange(self):
        range = self.exec_request(self.pump, commands.ReadCurGlucosePageNumber, render_decoded=False,render_hexdump=False)
        return range.getData

    def main (self, args):
        # Set Global variables..
        self.timezone = args.timezone

        info = self.getRange()
        print "yes"
        print info
        print vars(info)
        print repr(info)
        print "yes"


        self.download_history(args)

if __name__ == '__main__':
    app = DownloadHistory( )
    app.run(None)

