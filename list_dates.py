
import sys
import argparse
import textwrap

from pprint import pprint, pformat
from binascii import hexlify
from datetime import datetime
from scapy.all import *

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

def parse_years_strict(year):
  """
    >>> parse_years(0x06)
    2006

  """
  y = (year & Mask.year) + 2000
  return y

def parse_years(year):
  y = (year & Mask.year) + 2000
  if year > 15 or y < 0 or y < 2002 or y > 2015:
    raise ValueError(y)
  return y

def encode_year(year):
  pass

def encode_monthbyte(sec=18, minute=30, month=10):
  """
  >>> encode_monthbyte( ) == bytearray(b'\x92\x9e')
  True

  >>> quick_hex(encode_monthbyte( ))
  '0x92 0x9e'

  >>> encode_monthbyte(sec=10) == bytearray(b'\x8a\x9e')
  True

  >>> encode_monthbyte(sec=35) == bytearray(b'\xa3\x9e')
  True

  >>> encode_monthbyte(sec=50) == bytearray(b'\xb2\x9e')
  True

  >>> encode_monthbyte(minute=10) == bytearray(b'\x92\x8a')
  True

  >>> encode_monthbyte(minute=35) == bytearray(b'\x92\xa3')
  True

  >>> encode_monthbyte(minute=50) == bytearray(b'\x92\xb2')
  True

  >>> encode_monthbyte(month=1) == bytearray(b'\x12^')
  True

  >>> encode_monthbyte(month=2) == bytearray(b'\x12\x9e')
  True

  >>> encode_monthbyte(month=3) ==  bytearray(b'\x12\xde')
  True

  """

  encoded = [ 0x00, 0x00 ]


  high = (month & (0x3 << 2)) >> 2
  low  = month & (0x3)

  encoded[0] = sec | (high << 6)
  encoded[1] = minute | (low << 6)
  return bytearray( encoded )

  printf("0x%.2x 0x%.2x\n", buf[0], buf[1]);

def encode_minute(minute=30, month=10):
  """
  >>> quick_hex(encode_minute( ))
  '0x9e'

  """
  low  = month & (0x3)
  encoded = minute | (low << 6)
  return bytearray( [ encoded ] )

def quick_hex(bb):
  return ' '.join( [ '%#04x' % x for x in bb ] )
def encode_second(sec=18, month=10):
  """
  >>> encode_second( ) == bytearray(b'\x92')
  True

  >>> quick_hex(encode_second( ))
  '0x92'

  """
  high = (month & (0x3 << 2)) >> 2
  encoded = sec | (high << 6)
  return bytearray( [ encoded ] )

def test_time_encoders( ):
  """
  >>> test_time_encoders( )
  True
  """

  one = bytearray().join([encode_second( ), encode_minute( )])
  two = encode_monthbyte( )
  return one == two

def parse_date(data):
  try:
    seconds = parse_seconds(data[0])
    minutes = parse_minutes(data[1])
    hours   = parse_hours(data[2])
    day     = parse_day(data[3])
    year    = parse_years(data[4])
    if year < 0 or year < 2002 or year > 2015:
      raise ValueError(year)
    month   = parse_months( data[0], data[1] )
    date = datetime(year, month, day, hours, minutes, seconds)
    return date
  except ValueError, e:
    raise NotADate(e)


def opcode_min_read(opcode):
  TABLE = {
    0x07: 29,
    #0x1f: 8,
  }
  offset = TABLE.get(opcode, 1)
  return offset


def opcode_read_ahead(opcode, fd=None):
  TABLE = {
    0x5b: 22,
    #0x64: 4,
    0x03: 4,
    #0x6b: 33,
    0x6b: 27,
    0x45: 6,
    0x07: -1,
    #0x1f: 22,
    #0x1f: 8,
  }
  return TABLE.get(opcode, 0)
  if TABLE.get(opcode) is not None:
    #print "special opcode %#04x, read:%s" % (opcode, TABLE[opcode])
    return bytearray(fd.read(TABLE[opcode]))
  return bytearray( )

def sniff_invalid_opcode(opcode):
  if opcode == 0x00:
    raise NotADate("invalid opcode")

def eat_nulls(fd):
  nulls = bytearray( )
  for B in iter(lambda: fd.read(1), ""):
    if B == 0x00:
      nulls.append(B)
    else:
      fd.seek(fd.tell( ) - 1)
      break
  print "found %s nulls" % len(nulls)
  return nulls

def find_dates(stream):
  records = [ ]
  bolus = bytearray(stream.read(4))
  extra = bytearray( )
  opcode = ''
  for B in iter(lambda: stream.read(1), ""):
    h, t = B[:1], B[1:]
    bolus.append(h)
    bolus.extend(t)
    if len(bolus) < 6:
      bolus.extend(stream.read(opcode_min_read(bolus[0])))
    try:
      date = parse_date(bolus[-5:])
      opcode = bolus[0]
      if len(bolus) <= 5:
        raise NotADate('too short of a record')
      #sniff_invalid_opcode( bolus[0] )
      extra_len = opcode_read_ahead(bolus[0])
      if extra_len > 0:
        extra.extend( bytearray(stream.read(extra_len)) )
      records.append( (date, bolus[:-5], bolus[-5:], extra) )
      bolus = bytearray(stream.read(4))
      extra = bytearray( )
      opcode = ''
    except NotADate, e:
      opcode = bolus[0]
      pass
  return records

def int_dump(stream, indent=0):
  """
  >>> int_dump(bytearray([0x01, 0x02]))
  '   1    2'


  """
  cells = [ '%#04s' % (x) for x in stream ]
  lines = [ ]
  indent = ''.join( [ ' ' ] * indent )
  while cells:
    octet = cells[:8]
    line  = ' '.join(octet)
    lines.append(indent + line)
    cells = cells[8:]

  out = ('\n').join([ line for line in lines ])
  return out

def main( ):
  parser = get_opt_parser( )
  opts = parser.parse_args( )
  tw_opts = {
    'width': 50,
    'subsequent_indent': '          ',
    'initial_indent': '       ',
  }
  wrapper = textwrap.TextWrapper(**tw_opts)
  for stream in opts.infile:
    records = find_dates(stream)
    print "%s: %s records" % (stream.name, len(records))
    i = 0
    for rec in records:
      date, datum, tail, extra = rec
      opcode = datum[0]
      stats = "hex({}), extra({})".format(len(datum), len(extra))
      date_str = str(date)
      if date is not None:
        date_str = date.isoformat( )

      print "RECORD %s: %s %#04x %s" % (i, date_str, opcode, stats)
      print "  hex (%s)" % len(datum)
      print lib.hexdump(datum)
      print "  decimal"
      print int_dump(datum, indent=7)
      print "  datetime\n%s" % (lib.hexdump(tail))
      print "  extra(%s)" % len(extra),
      if len(extra) > 0:
        print "\n%s" % (lib.hexdump(extra))
        print int_dump(extra, indent=7)
      else:
        print "%s" % (None)
      print ""
      i += 1
    stream.close( )

if __name__ == '__main__':
  import doctest
  failures, tests = doctest.testmod( )
  if failures > 0:
    print "REFUSING TO RUN DUE TO FAILED TESTS"
    sys.exit(1)
  main( )
#####
# EOF
