
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

    self.bolus  = bolus
    self.head   = bolus[:head_length]
    body_offset = head_length + date_length
    self.date   = bolus[head_length:body_offset]
    self.body   = bolus[body_offset:]
    return self.decode( )

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
    decode_msg = ''
    if decoded is not None:
      decode_msg = '\n'.join([ '###### DECODED',
                                '```python',
                                '{}'.format(pformat(self.decode( ))),
                                '```', ])
    if extra:
      extra = '    ' + ' '.join(extra)
    else:
      extra = ''
    return '\n'.join([ prefix, decode_msg, head, date, body, extra ])

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
  """
  """
  _test_1 = bytearray([ 0x0a, 0x8b,
                        0xee, 0x04, 0x2f, 0x12, 0x0c, ])
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
class Bolus(KnownRecord):
  """
  >>> rec = Bolus(Bolus._test_1[:4])
  >>> decoded = rec.parse(Bolus._test_1)
  >>> print str(rec)
  Bolus 2012-12-18T15:05:28 head[4], body[0] op[0x01]

  >>> print pformat(decoded)
  {'amount': 5.6, 'programmed': 5.6}

  """
  _test_1 = bytearray([ 0x01, 0x38, 0x38, 0x00,
                        0xdc, 0x05, 0x4f, 0x12, 0x0c, ])
  opcode = 0x01
  head_length = 4
  def decode(self):
    self.parse_time( )
    dose = { 'amount': self.head[1]/10.0,
             'programmed': self.head[2]/10.0,
           }
    return dose

class BolusWizard(KnownRecord):
  """
  Decode/parse bolus wizard records.
  >>> rec = BolusWizard(BolusWizard._test_1[:2])
  >>> decoded = rec.parse(BolusWizard._test_1)
  >>> print str(rec)
  BolusWizard 2013-01-20T13:07:45 head[2], body[13] op[0x5b]
  >>> print pformat(decoded)
  {'bg': 108,
   'bg_target_high': 125,
   'bg_target_low': 106,
   'bolus_estimate': 1.1,
   'carb_input': 15,
   'carb_ratio': 13,
   'correction_estimate': 0.0,
   'sensitivity': 45,
   'unabsorbed_insulin_total': 4.8}

  """
  # missing unabsorbed_insulin_count = 4
  _test_1 = bytearray([ 0x5b, 0x6c,
                        0x2d, 0x47, 0x0d, 0x14, 0x0d,
                        0x0f, 0x50, 0x0d, 0x2d, 0x6a, 0x00, 0x0b, 0x00,
                        0x00, 0x30, 0x00, 0x0b, 0x7d, ])

  _test_2 = bytearray([ 0x5b, 0x8b,
                        0xdc, 0x05, 0x0f, 0x12, 0x0c,
                        0x45, 0x50, 0x0d, 0x2d, 0x6a, 0x03, 0x35, 0x00,
                        0x00, 0x00, 0x00, 0x38, 0x7d, ])
  opcode = 0x5b
  body_length = 13
  def decode(self):
    self.parse_time( )
    bg = lib.BangInt([ self.body[1] & 0x0f, self.head[1] ])
    carb_input = int(self.body[0])
    wizard = { 'bg': bg, 'carb_input': carb_input,
               'carb_ratio': int(self.body[2]),
               'sensitivity': int(self.body[3]),
               'bg_target_low': int(self.body[4]),
               'bg_target_high': int(self.body[12]),
               'bolus_estimate': int(self.body[11])/10.0,
               'correction_estimate': int(self.body[7])/10.0,
               'unabsorbed_insulin_total': int(self.body[9])/10.0,
               # 'unabsorbed_insulin_total': int(self.body[9])/10.0,
               'carb_input': int(self.body[0]),
               # 'food_estimate': int(self.body[0]),
             }
    return wizard

def decode_unabsorbed(amount, age, curve,strokes=40.0):
  unabsorbed = { 'amount': amount/strokes,
                 'age': age,
                 'curve': curve, }
  return unabsorbed

class BolusGiven(VariableHead):
  """
  >>> rec = BolusGiven( BolusGiven._test_1[:2] )
  >>> print str(rec)
  BolusGiven unknown head[2], body[0] op[0x5c]

  >>> print pformat(rec.parse( BolusGiven._test_1 ))
  [{'age': 78, 'amount': 1.25, 'curve': 4},
   {'age': 88, 'amount': 0.95, 'curve': 4}]

  >>> rec = BolusGiven( BolusGiven._test_2[:2] )
  >>> print str(rec)
  BolusGiven unknown head[2], body[0] op[0x5c]

  >>> print pformat(rec.parse( BolusGiven._test_2 ))
  [{'age': 60, 'amount': 2.6, 'curve': 4},
   {'age': 160, 'amount': 2.5, 'curve': 4}]

  """
  _test_1 = bytearray([ 0x5c, 0x08,
                        0x32, 0x4e, 0x04, 0x26, 0x58, 0x04, ])

  _test_2 = bytearray([ 0x5c, 0x08,
                        0x68, 0x3c, 0x04,
                        0x64, 0xa0, 0x04, ])
  opcode = 0x5c
  date_length = 0
  def decode(self):
    raw = self.head[2:]
    doses = [ ]
    while raw:
      head, tail = raw[:3], raw[3:]
      doses.append( decode_unabsorbed(*head) )
      raw = tail
    return doses

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
