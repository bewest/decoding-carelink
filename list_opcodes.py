
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
    0x01: 'Bolus',
    0x03: 'Prime',
    0x06: 'NoDelivery',
    0x07: 'ResultTotals',
    0x08: 'ChangeBasalProfile',
    0x14: 'SelectBasalProfile',
    0x16: 'TempBasal[eof]',
    0x17: 'ChangeTime',
    0x18: 'NewTimeSet',
    0x19: 'LowBattery',
    0x1a: 'Battery',
    0x1e: 'PumpSuspend',
    0x1f: 'PumpResume',
    0x0a: 'CalForBG',
    0x21: 'Rewind',
    0x26: 'EnableDisableRemote',
    0x27: 'ChangeRemoteID',
    0x33: 'TempBasal',
    0x34: 'LowReservoir',
    0x5b: 'BolusWizard',
    0x5c: 'BolusGiven?',
    0x63: 'ChangeUtility?',
    0x64: 'ChangeTimeDisplay',

  }

  _head = {
    0x01: 4,
    0x03: 5,

    # 0x0c: 7,
    0x06: 4,
    0x07: 5,

    0x28: 7,
    0x45: 7,


    # 0x6c: 79 + 38 + 14,
    # 0x6c: 0,


    # observed on bewest-pump
    # 0x2e: 24,
    # 0x5c: 12,
    0x5b: 2,
    0x5c: 2,

    # 0x0c: 22,
    0x6d: 46,

    # hacks

    #0x0c: 19,
    #0x18: 1,
    #0x06: 3,
    # 0x00: 3,
    # 0x6b: 7,
    # 0x27: 16,
  }
  _date = 5
  _body = {
    #0x5b: 15,
    # 0x5b: 22,
    0x5b: 13,
    0x45: 3,
    #0x06: 7,
    0x07: 38 + 3,

    0x08: 42,
    0x34: 0,
    0x33: 1,
    0x26: 14,

    # 0x6b: 15,
    # 0x18: 6,
    # 0x21: 23,

    #0x6c: 32,

    # observed on bewest-pump


    # hacks
    #0x0a: 0,
    #0x6c: 3,
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
  def has_variable_head(cls, opcode):
    if opcode == 0x5c:
      return True
    return False

  @classmethod
  def variable_read(cls, opcode, body):
    if opcode == 0x5c and body[1:]:
      print "XXX: VARIABLE READ: %#04x" % body[1]
      return body[1]
    return 0
  @classmethod
  def seeks_null(cls, opcode, body):
    return False
    if opcode ==  0x5c:
      return True
    if False and opcode == 0x5b:
      # print 'XXX: %#04x' % body[13]
      if body[13:] and body[13] ==  0x5c:
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
        result = "MIDNIGHT!?: {}".format(history.unmask_date(self.date))
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
    extra = [ ]
    hour_bits = history.extra_hour_bits(self.date[1])
    year_bits = history.extra_year_bits(self.date[4])
    day_bits  = history.extra_hour_bits(self.date[3])
    if 1 in hour_bits:
      extra.append("HOUR BITS: {}".format(str(hour_bits)))
    if 1 in day_bits:
      extra.append("DAY BITS: {}".format(str(day_bits)))
    if 1 in year_bits:
      extra.append("YEAR BITS: {}".format(str(year_bits)))
    extra = '    ' + ' '.join(extra)
    return '\n'.join([ prefix, head, date, body, extra ])


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
    # print lib.hexdump(bolus)
    if B == bytearray([ 0x00 ]):
      return bolus
  return bolus

def find_dates(stream):
  records = [ ]
  errors  = [ ]
  bolus = bytearray( )
  extra = bytearray( )
  opcode = ''
  for B in iter(lambda: bytearray(stream.read(2)), bytearray("")):

    opcode = B[0]
    #bolus.append(B)
    bolus.extend(B)

    head_length = Record.lookup_head(opcode)
    body_length = Record.lookup_body(opcode)
    date_length = Record.lookup_date(opcode)
    total = len(bolus)


    if total < head_length:
      bolus.extend(bytearray(stream.read(head_length-total)))
    variable_read = Record.variable_read(opcode, bolus)

    if variable_read > 2:

      print "super special"
      bolus.extend(bytearray(stream.read(variable_read)))
      #print lib.hexdump( bolus )
      opcode = bolus[variable_read]
      #print "NEW OPCODE %#04x" % opcode
      head_length = Record.lookup_head(opcode)
      body_length = Record.lookup_body(opcode)
      total = len(bolus) - variable_read

      if total < head_length:
        bolus.extend( stream.read(head_length-total) )
      total = len(bolus)

      #body_length = Record.lookup_body(opcode)
      #date_length = Record.lookup_date(opcode)
      #total = len(bolus)

    total = len(bolus)
    head_length = total
      

    head = bolus[:max(total, 1)]

    bolus.extend(bytearray(stream.read(date_length)))
    date = bolus[head_length:head_length+date_length]
    total = len(bolus)
    # print repr(bolus), date_length, repr(date)
    if len(date) < 5:
      print "DATE LESS THAN 5!", stream.tell( )
      print lib.hexdump(bolus)
      break
      records[-1].body.extend(bolus)
    datetime = parse_date(date)
    if bytearray( [0x00] * min(total, 5) ) in bolus:
      nulls = bytearray(eat_nulls(stream))
      pos = stream.tell( )
      if pos > 1021:
        bolus = bolus + nulls + bytearray(stream.read(-1))
        crc = bolus[-2:]
        nulls = bolus[:-2]
        print "EOF {} nulls, CRC:".format(len(nulls))
        print lib.hexdump(crc)
      else:
        print "TOO MANY NULLS, BAILING ON STREAM at %s " % stream.tell( )
        print lib.hexdump(bolus)
        print lib.hexdump(nulls)
        print "MISSING: ARE THERE 32 more bytes?"
        print lib.hexdump(bytearray(stream.read(32)))
      # records[-1].body.extend(nulls)
      break

    
    if not Record.is_midnight(head):
      if datetime is None:
        print "#### MISSING DATETIME, reading more to debug %#04x" % opcode
        bolus.extend(bytearray(stream.read(24)))
        print "##### DEBUG HEX"
        print lib.hexdump(bolus, indent=4)
        print "##### DEBUG DECIMAL"
        print int_dump(bolus, indent=11)
        print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
        break

    if datetime is not None or Record.is_midnight(head):

      body = bytearray(stream.read(body_length))
      bolus.extend(body)
      if False or Record.seeks_null(opcode, body):
        print "should eat up to null, second %s" % repr(body[1:])
        if body[1:]:
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
    print "## START %s" % (stream.name)
    records = find_dates(stream)
    i = 0
    for record in records:

      prefix = '#### RECORD {} {}'.format(i, str(record))
      # record.pformat(prefix)
      i += 1
    print "`end %s: %s records`" % (stream.name, len(records))
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
