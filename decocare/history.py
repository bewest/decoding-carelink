#!/usr/bin/python
"""
This module provides some basic helper/formatting utilities,
specifically targeted at decoding ReadHistoryData data.

"""
import sys
from binascii import hexlify
from datetime import datetime

import lib
from records import *




_remote_ids = [
  bytearray([ 0x01, 0xe2, 0x40 ]),
  bytearray([ 0x03, 0x42, 0x2a ]),
  bytearray([ 0x0c, 0x89, 0x92 ]),
]

def decode_remote_id(msg):
  """
  practice decoding some remote ids:

  | 0x27
  | 0x01 0xe2 0x40
  | 0x03 0x42 0x2a
  | 0x28 0x0c 0x89
  | 0x92 0x00 0x00 0x00

  >>> decode_remote_id(_remote_ids[0])
  '123456'

  >>> decode_remote_id(_remote_ids[1])
  '213546'

  >>> decode_remote_id(_remote_ids[2])
  '821650'



  """
  high   = msg[ 0 ] * 256 * 256
  middle = msg[ 1 ] * 256
  low    = msg[ 2 ]
  return str(high + middle + low)

class Base(object):
  """
    >>> str( Base( bytearray([ 0x00, 0x00 ]) ) )
    'Base unknown head[2], body[0] op[0x00]'

  Each record in the history seems to have a two byte head, possibly
  some arguments, then a 5 byte description of the datetime, then
  maybe a body.  The most reliable way to identify records so far,
  seems to be through the 2 byte head.

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

  @classmethod
  def describe(klass):
    opstring = "0x%02x" % (getattr(klass, 'opcode', 0))
    name = klass.__name__
    out = [ klass.head_length, klass.date_length, klass.body_length ]
    return ",".join([ opstring, name ] + map(str, out))

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
        result = "{}".format(unmask_date(self.date))
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
                       "    decimal", lib.int_dump(self.head, indent=11) ])
    date = '\n'.join([ "    datetime (%s)" % self.date_str( ),
                       lib.hexdump(self.date, indent=4) ])

    body = "    body (%s)" % len(self.body)
    if len(self.body) > 0:
      body = '\n'.join([ body,
                         "    hex", lib.hexdump(self.body, indent=4),
                         "    decimal", lib.int_dump(self.body, indent=11) ])
    extra = [ ]
    hour_bits = self.date[1:] and extra_hour_bits(self.date[1]) or [ ]
    year_bits = self.date[4:] and extra_year_bits(self.date[4]) or [ ]
    day_bits  = self.date[3:] and extra_hour_bits(self.date[3]) or [ ]
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
                               '{}'.format(lib.pformat(self.decode( ))),
                               '```', ])
    if extra:
      extra = '    ' + ' '.join(extra)
    else:
      extra = ''
    return '\n'.join([ prefix, decode_msg, head, date, body, extra ])


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
  def decode(self):
    self.parse_time( )
    amount = self.head[4] / 10.0
    fixed  = self.head[2] / 10.0
    t = {0:'manual'}.get(fixed, 'fixed')
    prime = { 'type': t,
              'amount': amount,
              'fixed': fixed, }
    return prime

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

class CalBGForPH(KnownRecord):
  """
    >>> rec = CalBGForPH( CalBGForPH._test_1[:2] )
    >>> rec.parse( CalBGForPH._test_1 )
    {'amount': 139}
    >>> print str(rec)
    CalBGForPH 2012-12-18T15:04:46 head[2], body[0] op[0x0a]

  """
  _test_1 = bytearray([ 0x0a, 0x8b,
                        0xee, 0x04, 0x2f, 0x12, 0x0c, ])

  _test_2 = bytearray([ 0x0a, 0xa7,
                        0x22, 0x53, 0x30, 0x0e, 0x0d, ])

  _test_3 = bytearray([ 0x0a, 0xb0,
                        0x00, 0x6f, 0x2f, 0x0e, 0x0d, ])

  _test_4 = bytearray([ 0x0a, 0x42,
                        0x0c, 0x6c, 0x31, 0x0e, 0x8d, ])

  _test_5 = bytearray([ 0x0a, 0x60,
                        0x04, 0x59, 0x2b, 0x0e, 0x8d, ])
  _test_6 = bytearray([ 0x0a, 0x5b,
                        0x16, 0x52, 0x2a, 0x0e, 0x8d, ])
  opcode = 0x0a
  def decode(self):
    self.parse_time( )
    year_bits = extra_year_bits(self.date[4])

    return { 'amount': int(lib.BangInt([ year_bits[0], self.head[1] ])) }
    pass

class Rewind(KnownRecord):
  opcode = 0x21
class EnableDisableRemote(KnownRecord):
  opcode = 0x26
  body_length = 14
class ChangeRemoteID(KnownRecord):
  opcode = 0x27

class TempBasalDuration(KnownRecord):
  opcode = 0x16
  _test_1 = bytearray([ ])
  def decode(self):
    self.parse_time( )
    basal = { 'duration (min)': self.head[1] * 30, }
    return basal
class TempBasal(KnownRecord):
  opcode = 0x33
  body_length = 1
  _test_1 = bytearray([ ])
  def decode(self):
    self.parse_time( )
    basal = { 'rate': self.head[1] / 40.0, }
    return basal

class LowReservoir(KnownRecord):
  """
  >>> rec = LowReservoir( LowReservoir._test_1[:2] )
  >>> decoded = rec.parse(LowReservoir._test_1)
  >>> print str(rec)
  LowReservoir 2012-12-07T11:02:43 head[2], body[0] op[0x34]

  >>> print pformat(decoded)
  {'amount': 20.0}
  """
  opcode = 0x34
  _test_1 = bytearray([ 0x34, 0xc8,
                        0xeb, 0x02, 0x0b, 0x07, 0x0c, ])
  def decode(self):
    self.parse_time( )
    reservoir = {'amount' : int(self.head[1]) / 10.0 }
    return reservoir
class Bolus(KnownRecord):
  """
  >>> rec = Bolus(Bolus._test_1[:4])
  >>> decoded = rec.parse(Bolus._test_1)
  >>> print str(rec)
  Bolus 2012-12-18T15:05:28 head[4], body[0] op[0x01]

  >>> print pformat(decoded)
  {'amount': 5.6, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}

  """
  _test_1 = bytearray([ 0x01, 0x38, 0x38, 0x00,
                        0xdc, 0x05, 0x4f, 0x12, 0x0c, ])
  opcode = 0x01
  head_length = 4
  def decode(self):
    self.parse_time( )
    dose = { 'amount': self.head[1]/10.0,
             'programmed': self.head[2]/10.0,
             'type': '??',
             'dual_component': '??',
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
  {'_byte[5]': 0,
   '_byte[7]': 0,
   'bg': 108,
   'bg_target_high': 125,
   'bg_target_low': 106,
   'bolus_estimate': 1.1,
   'carb_input': 15,
   'carb_ratio': 13,
   'correction_estimate': 0.0,
   'food_estimate': 1.1,
   'sensitivity': 45,
   'unabsorbed_insulin_count': '??',
   'unabsorbed_insulin_total': 4.8,
   'unknown_byte[10]': 0,
   'unknown_byte[8]': 0}

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
    # XXX: I have no idea if this is correct; it seems to produce correct results.
    correction = ( twos_comp( self.body[7], 8 )
                 + twos_comp( self.body[5] & 0x0f, 8 ) ) / 10.0
    wizard = { 'bg': bg, 'carb_input': carb_input,
               'carb_ratio': int(self.body[2]),
               'sensitivity': int(self.body[3]),
               'bg_target_low': int(self.body[4]),
               'bg_target_high': int(self.body[12]),
               'bolus_estimate': int(self.body[11])/10.0,
               'food_estimate': int(self.body[6])/10.0,
               'unabsorbed_insulin_total': int(self.body[9])/10.0,
               'unabsorbed_insulin_count': '??',
               'correction_estimate': correction,
               '_byte[5]': self.body[5],
               '_byte[7]': int(self.body[7]), #
               'unknown_byte[8]': self.body[8],
               'unknown_byte[10]': self.body[10],
               # '??': '??',
               # 'unabsorbed_insulin_total': int(self.body[9])/10.0,
               # 'food_estimate': int(self.body[0]),
             }
    return wizard

def twos_comp(val, bits):
    # http://stackoverflow.com/a/9147327
    """compute the 2's compliment of int value val"""
    if( (val&(1<<(bits-1))) != 0 ):
        val = val - (1<<bits)
    return val

def decode_unabsorbed(amount, age, curve,strokes=40.0):
  unabsorbed = { 'amount': amount/strokes,
                 'age': age,
                 'curve': curve, }
  return unabsorbed

class UnabsorbedInsulinBolus(VariableHead):
  """
  This data is not made available at the time of therapy in the pump
  UI, but could easily change my dosing decision.

  >>> rec = UnabsorbedInsulinBolus( UnabsorbedInsulinBolus._test_1[:2] )
  >>> print str(rec)
  UnabsorbedInsulinBolus unknown head[2], body[0] op[0x5c]

  >>> print pformat(rec.parse( UnabsorbedInsulinBolus._test_1 ))
  [{'age': 78, 'amount': 1.25, 'curve': 4},
   {'age': 88, 'amount': 0.95, 'curve': 4}]

  >>> rec = UnabsorbedInsulinBolus( UnabsorbedInsulinBolus._test_2[:2] )
  >>> print str(rec)
  UnabsorbedInsulinBolus unknown head[2], body[0] op[0x5c]

  >>> print pformat(rec.parse( UnabsorbedInsulinBolus._test_2 ))
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
               ClearAlarm, SelectBasalProfile, TempBasalDuration, ChangeTime,
               NewTimeSet, LowBattery, Battery, PumpSuspend,
               PumpResume, CalBGForPH, Rewind, EnableDisableRemote,
               ChangeRemoteID, TempBasal, LowReservoir, BolusWizard,
               UnabsorbedInsulinBolus, ChangeUtility, ChangeTimeDisplay ]

class hack1(InvalidRecord):
  opcode = 0x6d
  head_length = 46

_confirmed.append(hack1)

for x in _confirmed:
  _known[x.opcode] = x

del x

def suggest(head):
  """
  Look in the known table of commands to find a suitable record type
  for this opcode.
  """
  klass = _known.get(head[0], Base)
  record = klass(head)
  return record

def parse_record(fd, head=bytearray( )):
  """
  Given a file-like object, and the head of a record, parse the rest
  of the record.
  Look up the type of record, read in just enough data to parse it,
  return the result.
  """
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


def describe( ):
  keys = _known.keys( )
  out  = [ ]
  for k in keys:
    out.append(_known[k].describe( ))
  return out

    

if __name__ == '__main__':
  import doctest
  doctest.testmod( )

#####
# EOF
