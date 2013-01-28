
import sys
import argparse
import textwrap

from pprint import pprint, pformat
from binascii import hexlify
# from datetime import datetime
# from scapy.all import *

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



class Base(object):
  """
    >>> str( Base( bytearray([ 0x00, 0x00 ]) ) )
    'Base unknown head[2], body[0] op[0x00]'

  """
  head_length = 2
  body_length = 0
  date_length = 5
  def __init__(self, head=bytearray( )):
    self.bolus = bytearray( )
    self.opcode = head[0]
    self.head = head
    self.date = bytearray( )
    self.datetime = None
    self.body = bytearray( )

  def __str__(self):
    name = self.__class__.__name__
    lengths = 'head[{}], body[{}]'.format(len(self.head), len(self.body))
    # opcodes = ' '.join(['%#04x' % x for x in self.head[:1]])
    opcodes = 'op[%#04x]' % self.opcode
    return ' '.join([name, self.date_str( ), lengths, opcodes ])

  def date_str(self):
    result = 'unknown'
    if self.datetime is not None:
      result = self.datetime.isoformat( )
    else:
      if len(self.date) == 5:
        result = "{}".format(history.unmask_date(self.date))
    return result

  def parse(self, bolus):
    head_length = self.head_length
    date_length = self.date_length

    self.bolus = bolus
    self.head   = bolus[:head_length]
    body_offset = head_length + date_length
    self.date   = bolus[head_length:body_offset]
    self.body   = bolus[body_offset:]
    self.decode( )

  def decode(self):
    pass

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
    hour_bits = self.date[1:] and history.extra_hour_bits(self.date[1]) or [ ]
    year_bits = self.date[4:] and history.extra_year_bits(self.date[4]) or [ ]
    day_bits  = self.date[3:] and history.extra_hour_bits(self.date[3]) or [ ]
    if 1 in hour_bits:
      extra.append("HOUR BITS: {}".format(str(hour_bits)))
    if 1 in day_bits:
      extra.append("DAY BITS: {}".format(str(day_bits)))
    if 1 in year_bits:
      extra.append("YEAR BITS: {}".format(str(year_bits)))
    decoded = self.decode( )
    if decoded is not None:
      extra.append("DECODED: {}".format(pformat(self.decode( ))))
    if extra:
      extra = '    ' + ' '.join(extra)
    else:
      extra = ''
    return '\n'.join([ prefix, head, date, body, extra ])

class Record(Base):
  pass

class VariableHead(Base):
  def __init__(self, head):
    Base.__init__(self, head)
    self.head_length = head[1]

class KnownRecord(Base):
  opcode = 0x00
  decodes_date = True

  def parse_time(self):
    self.datetime = parse_date(self.date)

  def decode(self):
    self.parse_time( )

_known = {

}

class InvalidRecord(KnownRecord):
  pass
  # 0x0c: 22,
  # 0x6d: 46,
  # 0x6d: 46 - 5,

class Bolus(KnownRecord):
  opcode = 0x01
  head_length = 4
class Prime(KnownRecord):
  opcode = 0x03
  head_length = 5
class NoDelivery(KnownRecord):
  opcode = 0x06
  head_length = 4
class ResultTotals(KnownRecord):
  opcode = 0x07
  head_length = 5
  body_length = 38 + 3

class ChangeBasalProfile(KnownRecord):
  opcode = 0x08
  body_length = 42
class ClearAlarm(KnownRecord):
  opcode = 0x0C
class SelectBasalProfile(KnownRecord):
  opcode = 0x14
class EndTempBasal(KnownRecord):
  opcode = 0x16
class ChangeTime(KnownRecord):
  opcode = 0x17
class NewTimeSet(KnownRecord):
  opcode = 0x18
class LowBattery(KnownRecord):
  opcode = 0x19
class Battery(KnownRecord):
  opcode = 0x1a
class PumpSuspend(KnownRecord):
  opcode = 0x1e
class PumpResume(KnownRecord):
  opcode = 0x1f
class CalForBG(KnownRecord):
  opcode = 0x0a
  def decode(self):
    self.parse_time( )
    return { 'amount': int(self.head[1]) }
    pass
class Rewind(KnownRecord):
  opcode = 0x21
class EnableDisableRemote(KnownRecord):
  opcode = 0x26
  body_length = 14
class ChangeRemoteID(KnownRecord):
  opcode = 0x27
class TempBasal(KnownRecord):
  opcode = 0x33
  body_length = 1
class LowReservoir(KnownRecord):
  opcode = 0x34
class BolusWizard(KnownRecord):
  opcode = 0x5b
  body_length = 13
class BolusGiven(VariableHead):
  opcode = 0x5c
  date_length = 0
class ChangeUtility(KnownRecord):
  opcode = 0x63
class ChangeTimeDisplay(KnownRecord):
  opcode = 0x64

_confirmed = [ Bolus, Prime, NoDelivery, ResultTotals, ChangeBasalProfile,
               ClearAlarm, SelectBasalProfile, EndTempBasal, ChangeTime,
               NewTimeSet, LowBattery, Battery, PumpSuspend, PumpResume,
               CalForBG, Rewind, EnableDisableRemote, ChangeRemoteID,
               TempBasal, LowReservoir, BolusWizard, BolusGiven, ChangeUtility,
               ChangeTimeDisplay ]

class hack1(InvalidRecord):
  opcode = 0x6d
  head_length = 46

_confirmed.append(hack1)

for x in _confirmed:
  _known[x.opcode] = x

del x

def suggest(head):
  """
  """
  klass = _known.get(head[0], Base)
  record = klass(head)
  return record

def parse_record(fd, head=bytearray( )):
  # head    = bytearray(fd.read(2))
  date    = bytearray( )
  body    = bytearray( )
  record  = suggest(head)
  remaining = record.head_length - len(head)
  if remaining > 0:
    head.extend(bytearray(fd.read(remaining)))
  if record.date_length > 0:
    date.extend(bytearray(fd.read(record.date_length)))
  if record.body_length > 0:
    body.extend(bytearray(fd.read(record.body_length)))
  record.parse( head + date + body )
  # print str(record)
  # print record.pformat(prefix=str(record) )
  return record



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

    if B == bytearray( [ 0x00, 0x00 ] ):
      print ("#### STOPPING DOUBLE NULLS @ %s," % stream.tell( )),
      nulls = eat_nulls(stream)
      print "reading more to debug %#04x" % B[0]
      print lib.hexdump(B, indent=4)
      print int_dump(B, indent=11)

      extra = bytearray(stream.read(32))
      print "##### DEBUG HEX"
      print lib.hexdump(extra, indent=4)
      print "##### DEBUG DECIMAL"
      print int_dump(extra, indent=11)
      # print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
      break
    record = parse_record( stream, B )
    records.append(record)
    continue

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
      print record.pformat(prefix)
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
