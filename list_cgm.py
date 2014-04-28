import sys
import argparse

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

class Records (object):
  raw = bytearray( )
  opcodes = {
    0x0e: 'CalBGForGH'
  , 0x08: 'SensorTimestamp'
  , 0x0b: 'SensorStatus'
  , 0x0f: 'SensorCalFactor'
  }
  def __init__ (self):
    self.raw = bytearray( )
  def append (self, data):
    self.raw.extend(data)
  def has_records (self):
    if len(self.raw) > 4:
      last = self.raw[-1]
      if last < 32:
        if last == 0x0d or self.raw[-2] == 0x0d:
          return False
        if self.raw[-3] == 0x0d or self.opcodes.get(last, False):
          if parse_date(self.raw[-5:]):
            return True
    return False
  def list (self):
    records = [ ]
    last = self.raw[-1]
    opcode = self.opcodes.get(last, False)
    date = parse_date(self.raw[-5:-1])
    if date:
      date = date.isoformat( )
    prefix = self.raw[:-5]
    curr = False
    if opcode == 'CalBGForGH':
      amount = int(prefix[0])
      if amount < 32:
        amount = 0x100 + amount
      curr = dict(date=date, prefix=lib.hexdump(prefix), name=opcode, amount=amount)
    if opcode == 'SensorTimestamp':
      cgms = [ ]
      for x in list(prefix):
        glucose = int(x) * 2
        cgms.append(glucose)
      curr = dict(date=date, prefix=lib.hexdump(prefix), name=opcode, glucose=cgms)
    if opcode == 'SensorCalFactor':
      factor = lib.BangInt([ prefix[1], prefix[0] ]) / 1000.0
      curr = dict(date=date, prefix=lib.hexdump(prefix), name=opcode, factor=factor)
    if opcode == 'SensorStatus':
      curr = dict(date=date, prefix=lib.hexdump(prefix), name=opcode)
      pass
    if curr:
      records.append(curr)
    return records

class ListCGM (object):
  def list_records (self, stream):
    records = [ ]
    batch = Records( )
    for B in iter(lambda: stream.read(1), ""):
      batch.append(B)
      if batch.has_records( ):
        records.extend(batch.list( ))
        batch = Records( )
    return records


  def print_records (self, records, opts={}):
    import json
    print json.dumps(records, indent=2)
  def main(self):
    parser = get_opt_parser( )
    opts = parser.parse_args( )
    self.records = [ ]
    for stream in opts.infile:
      self.records.extend(self.list_records(stream))

    self.print_records(self.records)

if __name__ == '__main__':
  app = ListCGM( )
  app.main( )
#####
# EOF
