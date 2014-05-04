import sys
import argparse
import io

from pprint import pprint, pformat
from binascii import hexlify

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
  minute = (one & 0b111111 )
  return minute

def parse_hours (one):
  return (one & 0x1F )

def parse_day (one):
  return one & 0x1F

def parse_months (one):
  return one >> 4

def parse_date (data, unmask=False, theory_1=False, strict=False):
  """
  """
  data = data[:]
  seconds = 0
  minutes = 0
  hours   = 0

  year    = times.parse_years(data[0])
  day     = parse_day(data[1])
  # XXX: minutes is suspect, what to do when > 59?
  minutes = parse_minutes(data[2])

  hours   = parse_hours(data[3])

  month   = parse_months(data[3])
  if theory_1:
    # XXX: incorrect and hacky and bad code
    if minutes > 59:
      month = month - 1
      minutes = (minutes & 0x0F) + 1
    if month < 1:
      month = (month + 12) % 12 + 1


  try:
    date = datetime(year, month, day, hours, minutes, seconds)
    return date
  except ValueError, e:
    if strict:
      raise
    if unmask:
      return (year, month, day, hours, minutes, seconds)
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
    , 0x10: 7
    , 0x0c: 4
    }
    if op > 0 and op < 32:
      return sizes.get(op, None)
    return None

  def collect_glucose (self):
    glucose = bytearray( )
    for B in iter(lambda: bytearray(self.stream.peek(1)), ""):
      if self.suggest(B[0]) is None and B[0] > 0x0F:
        glucose.extend(self.stream.read(1))
      else:
        break
    return glucose
  def decode (self):
    """
      XXX: buggy code

        * fails to acknowledge gaps in time
        * fails to acknowledge SensorSync
    """
    records = [ ]
    prefix = bytearray( )
    for B in iter(lambda: self.stream.read(1), ""):
      B = bytearray(B)
      if B[0] == 0x01:
        prefix.extend(B)
        continue
      # if B[0] == 0x03:
      suggestion = self.suggest(B[0])
      if suggestion is None:
        prefix.extend(bytearray(B))
      else:
        op = B[0]
        # print "LOOKING AT OP", " {0:#04x}".format(op)
        # print lib.hexdump(prefix + B)
        raw = bytearray(self.stream.read(suggestion))
        # print "date/body"
        date, body = raw[:4], raw[4:]
        # print lib.hexdump(date)
        # print lib.hexdump(body)
        date.reverse( )
        date = parse_date(date)
        glucose = self.collect_glucose( )
        if date is None:
          print "COULD NOT DECODE", " {0:#04x}".format(op), ' @ byte {0}'.format(self.stream.tell( ))
          print lib.hexdump(prefix)
          print lib.hexdump(B)
          print lib.hexdump(raw)
          expected_date = raw[:4]
          expected_date.reverse( )
          print "expected a date", parse_date(expected_date, unmask=True, theory_1=True)
          print lib.hexdump(glucose)
          date = parse_date(expected_date, theory_1=True, strict=True)
          print "ATTEMPTING", date


        cgm = glucose[:]
        # cgm.reverse( )
        cgm = self.map_glucose(cgm, start=date, delta=self.delta_ago( ))
        # cgm.reverse( )
        prior = prefix[:]
        prior = self.map_glucose(prior, start=date, delta=self.delta_ago(reverse=True))
        prior.reverse( )
        records.extend(prior)
        records.extend(cgm)
        records.append(self.to_dict(op, body, date, glucose, prefix))
        prefix = bytearray( )
    records.reverse( )
    self.records = records
    return records

  def map_glucose (self, values, start=None, delta=None):
    cgms = [ ]
    last = start
    if delta is None:
      delta = self.delta_ago( )
    for x in list(values):
      i = len(cgms)
      date = last
      record = dict(date=date.isoformat( ), name='GlucoseSensorData', op=x, amount='??')
      if x > 20:
        x = int(x) * 2
        record.update(amount=x)
      if x == 02:
        record = dict(date=date.isoformat( ), name='SensorWeakSignal', op=x, amount='none')
      if x == 19:
        record = dict(date=date.isoformat( ), name='Not Sure, cannot find in csv', op=x, amount='gap')
      cgms.append(record)
      if x != 19:
        last = last - delta
    return cgms

  def delta_ago (self, reverse=False, offset=1):
    delta = relativedelta(minutes=5*offset)
    if reverse:
      delta = relativedelta(minutes=-5*offset)
    return delta

  def to_dict (self, op=None, body=None, date=None, glucose=None, prefix=None):
    names = {
      0x0e: 'CalBGForGH'
    , 0x08: 'SensorTimestamp'
    , 0x0d: 'SensorSync'
    , 0x0b: 'SensorStatus'
    , 0x0f: 'SensorCalFactor'
    }
    name = names.get(op, 'ERROR')
    record = dict(op=op, date=date.isoformat( ), cgm=list(glucose), name=name, prefix=list(prefix))
    if name == 'ERROR':
      record.update(name='ERROR_{0:#04x}'.format(op), prefix=list(body+glucose))
    if name == 'SensorCalFactor':
      factor = lib.BangInt([ body[0], body[1] ]) / 1000.0
      record.update(factor=factor)

    if name == 'CalBGForGH':
      amount = int(body[0])
      if amount < 32:
        amount = 0x100 + amount
      record.update(amount=amount)

    return record

from dateutil.relativedelta import relativedelta

import json
class ListCGM (object):

  def print_records (self, records, opts={}):
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
