import sys
import argparse
import io

from pprint import pprint, pformat
from binascii import hexlify
from datetime import datetime

from datetime import datetime
from decocare import lib
from decocare.records import times

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
  return parser


def parse_minutes (one):
  minute = (one & 0x7F )
  return minute

def parse_hours (one):
  return (one & 0x1F )

def parse_day (one):
  return one & 0x1F

def parse_months (one):
  return one >> 4

def parse_date (data):
  """
  """
  data = data[:]
  seconds = 0
  minutes = 0
  hours   = 0

  year    = times.parse_years(data[0])
  day     = parse_day(data[1])
  minutes = parse_minutes(data[2])

  hours   = parse_hours(data[3])

  month   = parse_months(data[3])

  try:
    date = datetime(year, month, day, hours, minutes, seconds)
    return date
  except ValueError, e:
    pass
  return None

class PagedData (object):

  def __init__ (self, stream):
    raw = bytearray(stream.read(1024))
    data, crc = raw[0:1022], raw[1022:]
    computed = lib.CRC16CCITT.compute(bytearray(data))
    if lib.BangInt(crc) != computed:
      assert lib.BangInt(crc) == computed, "CRC does not match page data"
    
    data.reverse( )
    self.data = self.eat_nulls(data)
    self.stream = io.BufferedReader(io.BytesIO(self.data))

  def map_glucose (self, values, start=None):
    cgms = [ ]
    for x in list(values):
      if x > 20:
        x = int(x) * 2
      cgms.append(x)
    return cgms
  def eat_nulls (self, data):
    i = 0
    while data[i] == 0x00:
      i = i+1
    return data[i:]
  def suggest (self, op):
    sizes = {
    #  0x01: 1
    #, 0x03: 1
      0x08: 4
    , 0x0b: 4
    , 0x0d: 4
    , 0x0f: 6
    , 0x0e: 5
    }
    if op > 0 and op < 32:
      return sizes.get(op, None)
    return None

  def collect_glucose (self):
    glucose = bytearray( )
    for B in iter(lambda: bytearray(self.stream.peek(1)), ""):
      if self.suggest(B[0]) is None:
        glucose.extend(self.stream.read(1))
      else:
        break
    return glucose
  def decode (self):
    records = [ ]
    prefix = bytearray( )
    for B in iter(lambda: self.stream.read(1), ""):
      B = bytearray(B)
      suggestion = self.suggest(B[0])
      if suggestion is None:
        prefix.extend(bytearray(B))
      else:
        op = B[0]
        body = bytearray(self.stream.read(suggestion))
        date, body = body[:4], body[4:]
        date.reverse( )
        date = parse_date(date)
        glucose = self.collect_glucose( )
        records.append(self.to_dict(op, body, date, glucose, prefix))
        prefix = bytearray( )
    records.reverse( )
    self.records = records
    return records
  def to_dict (self, op=None, body=None, date=None, glucose=None, prefix=None):
    names = {
      0x0e: 'CalBGForGH'
    , 0x08: 'SensorTimestamp'
    , 0x0d: 'SensorSync'
    , 0x0b: 'SensorStatus'
    , 0x0f: 'SensorCalFactor'
    }
    name = names.get(op, 'ERROR')
    record = dict(op=op, date=date.isoformat( ), cgm=self.map_glucose(glucose), name=name, prefix=list(prefix))
    if name == 'SensorCalFactor':
      factor = lib.BangInt([ body[0], body[1] ]) / 1000.0
      record.update(factor=factor)

    if name == 'CalBGForGH':
      amount = int(body[0])
      if amount < 32:
        amount = 0x100 + amount
      record.update(amount=amount)

    return record

class ListCGM (object):

  def print_records (self, records, opts={}):
    import json
    print json.dumps(records, indent=2)
  def main(self):
    parser = get_opt_parser( )
    opts = parser.parse_args( )
    self.records = [ ]
    for stream in opts.infile:
      page = PagedData(stream)
      self.records.extend(page.decode( ))

    self.print_records(self.records)

if __name__ == '__main__':
  app = ListCGM( )
  app.main( )
#####
# EOF
