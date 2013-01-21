
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
  _names = {
    0x07: 'ResultTotals',
    0x03: 'Prime',
    0x26: 'EnableDisableRemote',
    0x27: 'ChangeRemoteID',
    0x5b: 'BolusWizard',
    0x33: 'TempBasal',
    0x16: 'TempBasal[eof]',
    0x63: 'ChangeUtility?',
    0x1e: 'PumpSuspend',
    0x1f: 'PumpResume',
    0x64: 'ChangeTimeDisplay',
    0x17: 'ChangeTime',
    0x18: 'NewTimeSet',

  }
  _head = {
    0x03: 5,
    # 0x0c: 7,
    0x28: 7,
    0x07: 2,
    #0x18: 1,
    #0x06: 3,
    0x45: 7,
    # 0x03: 4,
    # 0x01: 4,


    0x00: 3,

    # hacks
    0x6b: 7,
    # 0x27: 16,
  }
  _date = 5
  _body = {
    #0x5b: 15,
    # 0x5b: 22,
    0x5b: 22,
    0x6b: 15,
    0x45: 3,
    0x07: 38,
    # 0x18: 6,
    # 0x21: 23,
    0x34: 0,
    0x33: 1,
    0x26: 14,

    # hacks
    #0x0a: 0,
    
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
  def seeks_null(cls, opcode, body):
    if opcode == 0x5b:
      print 'XXX: %#04x' % body[13]
      if body[13] ==  0x5c:
        return True
    return False

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
    name = self._names.get(self.opcode, self.__class__.__name__)
    lengths = 'head[{}], body[{}]'.format(len(self.head), len(self.body))
    # opcodes = ' '.join(['%#04x' % x for x in self.head[:1]])
    opcodes = '%#04x' % self.opcode
    return ' '.join([name, self.date_str( ), lengths, opcodes ])

  def date_str(self):
    result = 'unknown'
    if self.datetime is not None:
      result = self.datetime.isoformat( )
    else:
      if self.is_midnight(self.head):
        result = "MIDNIGHT!?"
    return result
    
  def pformat(self, prefix=''):
    head = '\n'.join([ "    op hex (%s)" % len(self.head), lib.hexdump(self.head, indent=4),
                       "    decimal", int_dump(self.head, indent=11) ])
    date = '\n'.join([ "    datetime (%s)" % self.date_str( ),
                       lib.hexdump(self.date, indent=4) ])

    body = "    body (%s)" % len(self.body)
    if len(self.body) > 0:
      body = '\n'.join([ body,
                         "    hex", lib.hexdump(self.body, indent=4),
                         "    decimal", int_dump(self.body, indent=11) ])
    return '\n'.join([ prefix, head, date, body ])


def eat_nulls(fd):
  nulls = bytearray( )
  for B in iter(lambda: bytearray(fd.read(1)), bytearray("")):
    if B[0] == 0x00:
      nulls.extend(B)
    else:
      fd.seek(fd.tell( ) - 1)
      break
  print "found %s nulls" % len(nulls)
  return nulls

def seek_null(fd):
  bolus = bytearray( )
  for B in iter(lambda: fd.read(1), ""):
    bolus.append(B)
    print lib.hexdump(bolus)
    if B == bytearray([ 0x00 ]):
      return bolus
  return bolus

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
    total = len(bolus)
    # print repr(bolus), date_length, repr(date)
    if len(date) < 5:
      records[-1].body.extend(bolus)
      continue
    datetime = parse_date(date)
    if bytearray( [0x00] * total ) == bolus:
      nulls = bytearray(eat_nulls(stream))
      records[-1].body.extend(nulls)
      break
    
    if not Record.is_midnight(head):
      assert datetime is not None, "\n%s" % lib.hexdump(bolus)
    if datetime is not None or Record.is_midnight(head):

      body = bytearray(stream.read(body_length))
      bolus.extend(body)
      if Record.seeks_null(opcode, body):
        print "should eat up to null"
        if body[-1] != 0x00:
          extra = seek_null(stream)
          print "found %s extra" % len(extra)
          body.extend(extra)
          bolus.extend(extra)
        epi = bytearray(stream.read(date_length))
        finished = parse_date(epi)
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
    for record in records:

      prefix = '#### RECORD {} {}'.format(i, str(record))
      # record.pformat(prefix)
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
