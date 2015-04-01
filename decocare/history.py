#!/usr/bin/python
"""
This module provides some basic helper/formatting utilities,
specifically targeted at decoding ReadHistoryData data.

"""
import io
from binascii import hexlify

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

class NoDelivery(KnownRecord):
  opcode = 0x06
  head_length = 4
#class ResultTotals(KnownRecord):
class MResultTotals(InvalidRecord):
  """On 722 this seems like two records."""
  opcode = 0x07
  #head_length = 5
  head_length = 5
  date_length = 2
  #body_length = 37 + 4
  #body_length = 2
  def __init__(self, head, larger=False):
    super(type(self), self).__init__(head, larger)
    if larger:
      self.body_length = 3
  def parse_time(self):
    mid = unmask_m_midnight(self.date)
    try:
      self.datetime = date = datetime(*mid)
      return date
    except ValueError, e:
      print "ERROR", e, mid, lib.hexdump(self.date)
      pass
    return mid


  def date_str(self):
    result = 'unknown'
    if self.datetime is not None:
      result = self.datetime.isoformat( )
    else:
      if len(self.date) >=2:
        result = "{}".format(unmask_m_midnight(self.date))
    return result

class ChangeBasalProfile_old_profile (KnownRecord):
  opcode = 0x08
  # old/bad
  # body_length = 46
  # XXX: on LeDanaScott's, 522, this seems right
  body_length = 145
  def __init__(self, head, larger=False):
    super(type(self), self).__init__(head, larger)
    if larger:
      self.body_length = 145
  def decode (self):
    self.parse_time( )
    rates = [ ]
    i = 0
    for x in range(47):
      start = x * 3
      end = start + 3
      (offset, rate, q) = self.body[start:end]
      if [offset, rate, q] == [ 0x00, 0x00, 0x00]:
        break
      try:
        rates.append(describe_rate(offset, rate, q))
      except TypeError, e:
        remainder = [ offset, rate, q ]
        rates.append(remainder)
    return rates

def describe_rate (offset, rate, q):
  return (dict(offset=(30*1000*60)*offset, rate=rate*0.025))


class ChangeBasalProfile_new_profile (KnownRecord):
  opcode = 0x09
  body_length = 145
  def decode (self):
    self.parse_time( )
    rates = [ ]
    i = 0
    for x in range(47):
      start = x * 3
      end = start + 3
      (offset, rate, q) = self.body[start:end]
      if [offset, rate, q] == [ 0x00, 0x00, 0x00]:
        break
      rates.append(describe_rate(offset, rate, q))
    return rates
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


class ChangeUtility(KnownRecord):
  opcode = 0x63
class ChangeTimeDisplay(KnownRecord):
  opcode = 0x64

_confirmed = [ Bolus, Prime, NoDelivery, MResultTotals,
               ChangeBasalProfile_old_profile,
               ChangeBasalProfile_new_profile,
               ClearAlarm, SelectBasalProfile, TempBasalDuration, ChangeTime,
               NewTimeSet, LowBattery, Battery, PumpSuspend,
               PumpResume, CalBGForPH, Rewind, EnableDisableRemote,
               ChangeRemoteID, TempBasal, LowReservoir, BolusWizard,
               UnabsorbedInsulinBolus, ChangeUtility, ChangeTimeDisplay ]

# _confirmed.append(DanaScott0x09)

class Ian69(KnownRecord):
  opcode = 0x69
  body_length = 2
_confirmed.append(Ian69)

class Ian50(KnownRecord):
  opcode = 0x50
  body_length = 34
_confirmed.append(Ian50)

class Ian54(KnownRecord):
  opcode = 0x54
  body_length = 34 + 23
  body_length = 57
_confirmed.append(Ian54)

class Ian0B(KnownRecord):
  opcode = 0x0B
  head_length = 3
_confirmed.append(Ian0B)

class Ian3F(KnownRecord):
  opcode = 0x3F
  body_length = 3
_confirmed.append(Ian3F)

class IanA8(KnownRecord):
  opcode = 0xA8
  head_length = 10
_confirmed.append(IanA8)

class BasalProfileStart(KnownRecord):
  opcode = 0x7b
  body_length = 3
  def __init__(self, head, larger=False):
    super(type(self), self).__init__(head, larger)
    if larger:
      # body_length = 1
      pass
      # self.body_length = 48
  def decode (self):
    self.parse_time( )
    if (len(self.body) % 3 == 0):
      return describe_rate(*self.body)
    else:
      return dict(raw=hexlify(self.body))
_confirmed.append(BasalProfileStart)

# 123, 143
class OldBolusWizardChange (KnownRecord):
  opcode = 0x5a
  body_length = 117
_confirmed.append(OldBolusWizardChange)

class BigBolusWizardChange (KnownRecord):
  opcode = 0x5a
  body_length = 143
  
class old6c(InvalidRecord):
  opcode = 0x6c
  #head_length = 45
  body_length = 38
  # body_length = 34
_confirmed.append(old6c)

class Model522ResultTotals(KnownRecord):
  opcode = 0x6d
  head_length = 1
  date_length = 2
  body_length = 40
  def parse_time(self):
    mid = unmask_m_midnight(self.date)
    try:
      self.datetime = date = datetime(*mid)
      return date
    except ValueError, e:
      print "ERROR", e, lib.hexdump(self.date)
      pass
    return mid
      
    
  def date_str(self):
    result = 'unknown'
    if self.datetime is not None:
      result = self.datetime.isoformat( )
    else:
      if len(self.date) >=2:
        result = "{}".format(unmask_m_midnight(self.date))
    return result

def unmask_m_midnight(data):
  """
  Extract date values from a series of bytes.
  Always returns tuple given a bytearray of at least 3 bytes.

  Returns 6-tuple of scalar values year, month, day, hours, minutes,
  seconds.

  """
  data = data[:]
  seconds = 0
  minutes = 0
  hours   = 0

  day     = parse_day(data[0])

  high = data[0] >> 4
  low  = data[0] & 0x1F

  year_high = data[1] >> 4
  # month = int(high) #+ year_high
  # month   = parse_months( data[0], data[1] )
  mhigh = (data[0] & 0xE0) >> 4
  mlow  = (data[1] & 0x80) >> 7
  month =  int(mhigh + mlow)
  day = int(low) + 1

  year = parse_years(data[1])
  return (year, month, day, hours, minutes, seconds)

_confirmed.append(Model522ResultTotals)

class Sara6E(Model522ResultTotals):
  """Seems specific to 722?"""
  opcode = 0x6e
  #head_length = 52 - 5
  # body_length = 1
  body_length = 48
  #body_length = 0
  def __init__(self, head, larger=False):
    super(type(self), self).__init__(head, larger)
    if larger:
      self.body_length = 48
_confirmed.append(Sara6E)

_known = { }

_variant = { }

for x in _confirmed:
  _known[x.opcode] = x

del x

def suggest(head, larger=False):
  """
  Look in the known table of commands to find a suitable record type
  for this opcode.
  """
  klass = _known.get(head[0], Base)
  record = klass(head, larger)
  return record

def parse_record(fd, head=bytearray( ), larger=False):
  """
  Given a file-like object, and the head of a record, parse the rest
  of the record.
  Look up the type of record, read in just enough data to parse it,
  return the result.
  """
  # head    = bytearray(fd.read(2))
  date    = bytearray( )
  body    = bytearray( )
  record  = suggest(head, larger)
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

class PagedData (object):
  """
    PagedData - context for parsing a page of cgm data.
  """

  def __init__ (self, raw):
    data, crc = raw[0:1022], raw[1022:]
    computed = lib.CRC16CCITT.compute(bytearray(data))
    if lib.BangInt(crc) != computed:
      assert lib.BangInt(crc) == computed, "CRC does not match page data"

    self.raw = raw
    self.clean(data)

  def clean (self, data):
    data.reverse( )
    self.data = self.eat_nulls(data)
    self.stream = io.BufferedReader(io.BytesIO(self.data))

  def eat_nulls (self, data):
    i = 0
    while data[i] == 0x00:
      i = i+1
    return data[i:]

class HistoryPage (PagedData):
  def clean (self, data):
    data.reverse( )
    self.data = self.eat_nulls(data)
    self.data.reverse( )
    # XXX: under some circumstances, zero is the correct value and
    # eat_nulls actually eats valid data.  This ugly hack restores two
    # nulls back ot the end.
    self.data.append(0x00)
    self.data.append(0x00)
    self.data.append(0x00)
    self.data.append(0x00)
    self.stream = io.BufferedReader(io.BytesIO(self.data))
  def decode (self, larger=False):
    records = [ ]
    skipped = [ ]
    for B in iter(lambda: bytearray(self.stream.read(2)), bytearray("")):
      if B == bytearray( [ 0x00, 0x00 ] ):
        break
      record = parse_record(self.stream, B, larger=larger )
      if record.datetime:
        rec = dict(timestamp=record.datetime.isoformat( ),
                   date=lib.epochize(record.datetime),
                   _type=str(record.__class__.__name__),
                   _description=str(record))
        data = record.decode( )
        if data is not None:
          rec.update(data)
          if skipped:
            rec.update(appended=skipped)
            skipped = [ ]
          records.append(rec)
      else:
        rec = dict(_type=str(record.__class__.__name__),
                   _description=str(record))
        data = record.decode( )
        if data is not None:
          rec.update(data=data)
        skipped.append(rec)
    return records

if __name__ == '__main__':
  import doctest
  doctest.testmod( )

#####
# EOF
