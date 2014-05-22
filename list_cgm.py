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

#def parse_months (one):
#  return one >> 4

def parse_months (first_byte, second_byte):
  first_two_bits  = first_byte  >> 6
  second_two_bits = second_byte >> 6
  return (first_two_bits << 2) + second_two_bits
  

def parse_date (data, unmask=False, theory_1=False, strict=False, minute_specific=False):
  """
  Some dates are formatted/stored down to the second (Sensor CalBGForPH) while
    others are stored down to the minute (CGM SensorTimestamp dates).
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

  month   = parse_months(data[3], data[2])
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
    """
    return a partially filled in acket/opcode
     info: name, packet size, date_type, op
     some info will be added later when the record is parsed:
       GlucoseSensorData, cal factor. amount, prefix, data
    """
    
    records = {
      0x01: dict(name='DataEnd',packet_size=0,date_type='none',op=0x01),
      0x02: dict(name='SensorWeakSignal',packet_size=0,date_type='prevTimestamp',op=0x02),
      0x03: dict(name='SensorCalFactor',packet_size=1,date_type='prevTimestamp',op=0x03),
      0x08: dict(name='SensorTimestamp',packet_size=4,date_type='minSpecific',op=0x08),
      0x0b: dict(name='SensorStatus',packet_size=4,date_type='minSpecific',op=0x0b),
      0x0c: dict(name='DateTimeChange',packet_size=14,date_type='secSpecific',op=0x0c),
      0x0d: dict(name='SensorSync',packet_size=4,date_type='minSpecific',op=0x0d),
      0x0e: dict(name='CalBGForGH',packet_size=5,date_type='minSpecific',op=0x0e),
      0x0f: dict(name='SensorCalFactor',packet_size=6,date_type='minSpecific',op=0x0f),
      0x10: dict(name='10-Something',packet_size=7,date_type='minSpecific',op=0x10),
    }
#    sizes = {
## x01 - used to mark the end of data in the file/page
#    #  0x01: 1
## x02 - weak signal    
#    #  0x02: 1
## 0x03 may be SensorCal packet: 0x00=waiting 0x01=waiting , no datetime stamp
#    #, 0x03: 1
## x08 - timestamp (looks like it's used to start a sensor and also when setting the time)
#      0x08: 4
#    , 0x0b: 4
## x0c - looks like it is used to mark time changes (possibly size 14 packet or 4 bytes in packet)
#    , 0x0c: 14
#    , 0x0d: 4
## x0e - CalBGForGH/CalBGForPH    
#    , 0x0e: 5
## x0f - sensor cal factor
#    , 0x0f: 6 
#    , 0x10: 7
#    
#    }
    if op > 0 and op < 32:
      return records.get(op, None)
    else:
      record = dict(name='GlucoseSensorData',packet_size=0,date_type='prevTimestamp',op=op)
      record.update(sgv=(op * 2))
      return record

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
      record = self.suggest(B[0])
      # read packet if needed
      if not record is None and record[packet_size] > 0:
        raw_packet = bytearray(self.stream.read(record[packet_size])

      if record[name] == 'DataEnd':
#      if B[0] == 0x01:
        prefix.extend(B)
        continue
      # if B[0] == 0x03:
#      suggestion = self.suggest(B[0])
      
      elif record[name] == 'SensorCalFactor' or record[name] == 'GlucoseSensorData'\
                      or record[name] == 'SensorWeakSignal':
        # add to prefixed records to add to the next sensor minute timestamped record
        if record[name] == 'SensorCalFactor':
          body = raw_packet
          # update sensor cal factor
          factor = lib.BangInt([ body[0], body[1] ]) / 1000.0
          record.update(factor=factor)
        prefix.extend(record)
      elif record[name] == 'SensorTimestamp' or record[name] == 'SensorCalFactor'\
                      or record[name] == 'CalBGForGH':
        # these are sensor minute timestamped records thus create the record
        # and map prefixed elements based on the timedelta

      elif record[name] == 'SensorStatus' or record[name] == 'DateTimeChange'\
                      or record[name] == 'SensorSync' or record[name] == '10-Something':
        # independent record => parse and add to records list

      else:
        # could not decode




      else:
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

        if op == 0x08 or op == 0x0f:
#         glucose = self.collect_glucose( )
          glucose = None
#         cgm = glucose[:]
#         cgm.reverse( )
#         cgm = self.map_glucose(cgm, start=date, delta=self.delta_ago( ))
#         cgm.reverse( )
        # only map data that has come before
        # take the timestamp and map data that comes after as CGM
          prior = prefix[:]
          prior.reverse()
          records.append(self.to_dict(op, body, date, glucose, prefix))
#          if op == 0x0f:
          date = date + self.delta_ago(reverse=False)
          prior = self.map_glucose(prior, start=date, delta=self.delta_ago(reverse=True))
          prior.reverse( )
          records.extend(prior)
          prefix = bytearray()
#          records.extend(cgm)
        else:
          records.append(self.to_dict(op, body, date, glucose, prefix))
#        prefix = bytearray( )
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

# to_dict should not be needed with changes made to suggest
  def to_dict (self, op=None, body=None, date=None, glucose=None, prefix=None):
    names = {
      0x0e: 'CalBGForGH'
    , 0x08: 'SensorTimestamp'
    , 0x0d: 'SensorSync'
    , 0x0b: 'SensorStatus'
    , 0x0f: 'SensorCalFactor'
    # 0x03 may be SensorCal packet: 0x00=waiting 0x01=waiting
    }
    name = names.get(op, 'ERROR')
    record = dict(op=op, date=date.isoformat( ), name=name, prefix=list(prefix))
#    record = dict(op=op, date=date.isoformat( ), cgm=list(glucose), name=name, prefix=list(prefix))
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
