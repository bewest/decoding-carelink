#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from decocare import commands
import json

from decocare.history import HistoryPage
from decocare.helpers import cli

class LatestActivity (cli.CommandApp):
    """%(prog)s - Grab history
    """

    def download_page (self, number):
        kwds = dict(page=number)
        page = self.exec_request(self.pump, commands.ReadHistoryData, args=kwds)
        return page

    def find_records (self, page, larger=None):
        decoder = HistoryPage(page, self.pump.model)
        records = decoder.decode( )
        print "SINCE", self.since.isoformat( )
        for record in records:
            print "  * found record", record['_type'], record.get('timestamp')
            print "  * should quit", record.get('timestamp') < self.since.isoformat( ), self.enough_history
            if record.get('timestamp'):
                dt = parse(record['timestamp'])
                dt = dt.replace(tzinfo=self.timezone)
                record.update(timestamp=dt.isoformat( ))
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
        self.report_settings(args)
        if args.clock:
            self.report_clock(args )
        if args.status:
            self.report_status(args)
        if args.temp:
            self.report_temp(args)
        if args.basal:
            self.report_basal(args)
        if args.reservoir:
            self.report_reservoir(args)
        self.download_history(args)

if __name__ == '__main__':
    app = DownloadHistory( )
    app.run(None)

