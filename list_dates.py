
import sys
import argparse
import textwrap

from pprint import pprint, pformat
from binascii import hexlify
from datetime import datetime
from scapy.all import *

from pump import lib

from pump.history import NotADate, parse_date

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

      print "#### RECORD %s: %s %#04x %s" % (i, date_str, opcode, stats)
      print "    hex (%s)" % len(datum)
      print lib.hexdump(datum, indent=4)
      print "    decimal"
      print int_dump(datum, indent=11)
      print "    datetime\n%s" % (lib.hexdump(tail, indent=4))
      print "    extra(%s)" % len(extra),
      if len(extra) > 0:
        print "\n%s" % (lib.hexdump(extra, indent=4))
        print int_dump(extra, indent=11)
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
