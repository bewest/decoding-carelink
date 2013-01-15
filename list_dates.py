
import sys
import argparse
import textwrap

from pprint import pprint, pformat
from binascii import hexlify
from datetime import datetime

from pump import lib

class NotADate(Exception): pass


class Mask:
  time   = 0xC0
  invert = 0x3F
  year   = 0x0F

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


def parse_seconds(sec):
  """
  >>> parse_seconds(0x92)
  18
  """
  return sec & Mask.invert

def parse_minutes(minutes):
  """
  >>> parse_minutes(0x9e)
  30
  """
  return minutes & Mask.invert


def parse_hours(hours):
  """
  >>> parse_hours(0x0b)
  11
  """
  return int(hours)

def parse_day(day):
  """
  >>> parse_day( 0x01 )
  1
  """
  return day & Mask.year

def parse_months(seconds, minutes):
  """
  >>> parse_months( 0x92, 0x9e )
  10
  """
  high = (seconds & Mask.time) >> 4
  low  = (minutes & Mask.time) >> 6
  return high | low

def parse_years(year):
  y = (year & Mask.year) + 2000
  if year > 15 or y < 0 or y < 2002 or y > 2015:
    raise ValueError(y)
  return y

def parse_date(data):
  try:
    seconds = parse_seconds(data[0])
    minutes = parse_minutes(data[1])
    hours   = parse_hours(data[2])
    day     = parse_day(data[3])
    year    = parse_years(data[4])
    month   = parse_months( data[0], data[1] )
    date = datetime(year, month, day, hours, minutes, seconds)
    return date
  except ValueError, e:
    raise NotADate(e)

def opcode_read_ahead(opcode, fd):
  TABLE = {
    0x5b: 22,
    #0x64: 4,
    0x03: 4,
    0x6b: 27,
    # 0x00: 4,
    #0x1f: 22,
    #0x1f: 8,
  }
  if TABLE.get(opcode) is not None:
    #print "special opcode %#04x, read:%s" % (opcode, TABLE[opcode])
    return bytearray(fd.read(TABLE[opcode]))
  return bytearray( )

def sniff_invalid_opcode(opcode):
  if opcode == 0x00:
    raise NotADate("invalid opcode")

def find_dates(stream):
  records = [ ]
  bolus = bytearray(stream.read(4))
  for B in iter(lambda: stream.read(1), ""):
    bolus.append(B)
    try:
      date = parse_date(bolus[-5:])
      if len(bolus) <= 5:
        raise NotADate('too short of a record')
      #sniff_invalid_opcode( bolus[0] )
      bolus.extend( opcode_read_ahead(bolus[0], stream) )
      records.append( (date, bolus[:-5]) )
      bolus = bytearray(stream.read(4))
    except NotADate, e:
      pass
  return records


def main( ):
  parser = get_opt_parser( )
  opts = parser.parse_args( )
  tw_opts = {
    'width': 40,
    'subsequent_indent': '    ',
    'initial_indent': '    ',
  }
  wrapper = textwrap.TextWrapper(**tw_opts)
  for stream in opts.infile:
    records = find_dates(stream)
    print "%s: %s records" % (stream.name, len(records))
    for rec in records:
      date, datum = rec
      opcode = datum[0]

      print "%s %02x" % (date.isoformat( ), opcode)
      print lib.hexdump(datum)

if __name__ == '__main__':
  import doctest
  doctest.testmod( )
  main( )
#####
# EOF
