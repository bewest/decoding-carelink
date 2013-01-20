
import sys
import argparse
import textwrap

from pprint import pprint, pformat
from binascii import hexlify
# from datetime import datetime
from scapy.all import *

from pump import lib, history

from pump.history import NotADate

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

def parse_date(date):
  try:
    return history.parse_date(date)
  except NotADate, e: pass

  return None

class Record(object):
  _head = {
    # 0x03: 5
    0x0c: 7,
    0x28: 7,
    0x07: 2,
    0x18: 1,
    # 0x03: 4,
  }
  _date = 5
  _body = {
    0x5b: 15,
    0x07: 38,
    0x18: 6,
    0x21: 23,
    
  }
  def __init__(self, head=bytearray( ), date=bytearray( ), body=bytearray( ) ):
    self.head = head
    self.date = date
    self.opcode = None
    if head[:1]:
      self.opcode = head[0]
    self.datetime = parse_date(date)
    self.body = body

  @classmethod
  def lookup_head(cls, opcode):
    return cls._head.get(opcode, 2)
    
  @classmethod
  def lookup_date(cls, opcode):
    return cls._date

  @classmethod
  def is_midnight(cls, head):
    if head[1:] and head[0] == 0x07:
      if head[1:] and head[1] == 0x00:
          return True
    return False

  @classmethod
  def lookup_body(cls, opcode):
    # print "lookup body for opcode %#04x" % (opcode)
    return cls._body.get(opcode, 0)

  def __str__(self):
    name = self.__class__.__name__
    date = 'unknown'
    if self.datetime is not None:
      date = self.datetime.isoformat( )
    lengths = 'head[{}], body[{}]'.format(len(self.head), len(self.body))
    # opcodes = ' '.join(['%#04x' % x for x in self.head[:1]])
    opcodes = '%#04x' % self.opcode
    return ' '.join([name, date, lengths, opcodes ])

  def date_str(self):
    result = 'unknown'
    if self.datetime is not None:
      result = self.datetime.isoformat( )
    else:
      if self.is_midnight(self.head):
        result = "MIDNIGHT!?"
    return result
    
  def pformat(self, prefix=''):
    head = '\n'.join([ "  hex (%s)" % len(self.head), lib.hexdump(self.head, indent=2),
                       "  decimal", int_dump(self.head, indent=9) ])
    date = '\n'.join([ "  datetime (%s)" % self.date_str( ),
                       lib.hexdump(self.date, indent=2) ])

    body = "  body (%s)" % len(self.body)
    if len(self.body) > 0:
      body = '\n'.join([ body,
                         "  hex", lib.hexdump(self.body, indent=2),
                         "  decimal", int_dump(self.body, indent=9) ])
    return '\n'.join([ prefix, head, date, body ])


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
  bolus = bytearray( )
  extra = bytearray( )
  opcode = ''
  for B in iter(lambda: stream.read(1), ""):

    if len(bolus) == 0:
      opcode = bytearray(B)[0]
    bolus.append(B)

    head_length = Record.lookup_head(opcode)
    body_length = Record.lookup_body(opcode)
    date_length = Record.lookup_date(opcode)
    total = len(bolus)

    if total < head_length:
      bolus.extend(bytearray(stream.read(head_length-total)))

    head = bolus[:head_length]

    bolus.extend(bytearray(stream.read(date_length)))
    date = bolus[head_length:head_length+date_length]
    # print repr(bolus), date_length, repr(date)
    datetime = parse_date(date)
    if not Record.is_midnight(head):
      assert datetime is not None, "\n%s" % lib.hexdump(bolus)
    if datetime is not None or Record.is_midnight(head):

      body = bytearray(stream.read(body_length))
      bolus.extend(body)
      record = Record(head, date, body)
      prefix = "#### RECORD %s %s" % (len(records), str(record) )
      print record.pformat(prefix)
      print ""
      records.append(record)
      bolus = bytearray( )
      opcode = ''

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
      print lib.hexdump(datum, indent=2)
      print "  decimal"
      print int_dump(datum, indent=9)
      print "  datetime\n%s" % (lib.hexdump(tail, indent=2))
      print "  extra(%s)" % len(extra),
      if len(extra) > 0:
        print "\n%s" % (lib.hexdump(extra, indent=2))
        print int_dump(extra, indent=9)
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
