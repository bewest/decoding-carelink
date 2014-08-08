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
  minutes = parse_minutes(data[2])
  hours   = parse_hours(data[3])
  month   = parse_months(data[3], data[2])

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
      0x01: dict(name='DataEnd',packet_size=0,date_type='none',op='0x01'),
      0x02: dict(name='SensorWeakSignal',packet_size=0,date_type='prevTimestamp',op='0x02'),
      0x03: dict(name='SensorCal',packet_size=1,date_type='prevTimestamp',op='0x03'),
      0x08: dict(name='SensorTimestamp',packet_size=4,date_type='minSpecific',op='0x08'),
      0x0b: dict(name='SensorStatus',packet_size=4,date_type='minSpecific',op='0x0b'),
      0x0c: dict(name='DateTimeChange',packet_size=14,date_type='secSpecific',op='0x0c'),
      0x0d: dict(name='SensorSync',packet_size=4,date_type='minSpecific',op='0x0d'),
      0x0e: dict(name='CalBGForGH',packet_size=5,date_type='minSpecific',op='0x0e'),
      0x0f: dict(name='SensorCalFactor',packet_size=6,date_type='minSpecific',op='0x0f'),
      0x10: dict(name='10-Something',packet_size=7,date_type='minSpecific',op='0x10'),
      0x13: dict(name='19-Something',packet_size=0,date_type='prevTimestamp',op='0x13')
    }
    if op > 0 and op < 20:
      record = records.get(op, None)
      if record is None:
        return dict(name='Could Not Decode',packet_size=0,op=op)
      else:
        return record
    else:
      record = dict(name='GlucoseSensorData',packet_size=0,date_type='prevTimestamp',op=op)
      record.update(sgv=(int(op) * 2))
      return record

  def decode (self):
    """
      XXX: buggy code

        * fails to acknowledge gaps in time
        * fails to acknowledge SensorSync
    """
    records = [ ]
    prefix_records = []
    for B in iter(lambda: self.stream.read(1), ""):
      B = bytearray(B)
      record = self.suggest(B[0])
      # read packet if needed
      if not record is None and record['packet_size'] > 0:
        raw_packet = bytearray(self.stream.read(record['packet_size']))

      if record['name'] == 'DataEnd':
        prefix_records.append(record)
        continue
      
      elif record['name'] == 'GlucoseSensorData' or record['name'] == 'SensorWeakSignal' \
        or record['name'] == 'SensorCal' or record['name'] == '19-Something':
        # add to prefixed records to add to the next sensor minute timestamped record
        if record['name'] == 'SensorCal':
          record.update(raw=self.byte_to_str(raw_packet))
          if int(raw_packet[0]) == 1:
            record.update(waiting='waiting')
          else:
            record.update(waiting='meter_bg_now')
        prefix_records.append(record)

      elif record['name'] == 'SensorTimestamp' or record['name'] == 'SensorCalFactor':
        # these are sensor minute timestamped records thus create the record
        # and map prefixed elements based on the timedelta
        record.update(raw=self.byte_to_str(raw_packet))
        date, body = raw_packet[:4], raw_packet[4:]  
        date.reverse()
        date = parse_date(date)
        record.update(date=date.isoformat())
        prefix_records.reverse()
        mapped_glucose_records = self.map_glucose(prefix_records, start=date, delta=self.delta_ago(reverse=True))
        # Update sensor cal factor
        if record['name'] == 'SensorCalFactor': 
          factor = lib.BangInt([ body[0], body[1] ]) / 1000.0
          record.update(factor=factor) 
        for r in mapped_glucose_records:
          records.append(r)
        records.append(record)
        prefix_records = []

      elif record['name'] == 'SensorStatus' or record['name'] == 'DateTimeChange' \
        or record['name'] == 'SensorSync' or record['name'] == '10-Something' \
        or record['name'] == 'CalBGForGH' :
        # independent record => parse and add to records list
        record.update(raw=self.byte_to_str(raw_packet))
        if record['name'] == 'SensorStatus' or record['name'] == 'SensorSync'\
        or record['name'] == 'CalBGForGH' :
          date, body = raw_packet[:4], raw_packet[4:]
          date.reverse()
          date = parse_date(date)
          record.update(date=date.isoformat())
          record.update(body=self.byte_to_str(body))
          # Update cal amount
          if record['name'] == 'CalBGForGH':
            amount = int(body[0])
            if amount < 32:
              amount = 0x100 + amount
            record.update(body=self.byte_to_str(body))
            record.update(amount=amount)
        records.append(record)
      else:
        # could not decode
        records.append(record)
      # End For  
    records.reverse()
    self.records = records
    return self.records

  def byte_to_str (self, byte_array):
    # convert byte array to a string
    hex_bytes = []
    for i in range(0, len(byte_array)):
      hex_bytes.append('{0:02x}'.format(byte_array[i]))
    return '-'.join(hex_bytes)

  def map_glucose (self, values, start=None, delta=None):
    last = start
    if delta is None:
      delta = self.delta_ago()
    for x in list(values):
      if x['name'] != '19-Something':
        last = last - delta
      x.update(date=last.isoformat())
    return values
          
  def delta_ago (self, reverse=False, offset=1):
    delta = relativedelta(minutes=5*offset)
    if reverse:
      delta = relativedelta(minutes=-5*offset)
    return delta

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

##### EOF
