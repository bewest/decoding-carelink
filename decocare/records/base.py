from datetime import datetime
#from .. import lib
from decocare import lib
from times import *

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
  def __init__(self, head=bytearray( ), model=None, larger=False):
    self.larger = getattr(model, 'larger', larger)
    self.model = model
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

  def min_length(self):
    return self.head_length + self.date_length
  def parse(self, bolus):
    if len(bolus) < self.min_length( ):
      return
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
    """
    hour_bits = self.date[1:] and extra_hour_bits(self.date[1]) or [ ]
    year_bits = self.date[4:] and extra_year_bits(self.date[4]) or [ ]
    day_bits  = self.date[3:] and extra_hour_bits(self.date[3]) or [ ]
    if 1 in hour_bits:
      extra.append("HOUR BITS: {}".format(str(hour_bits)))
    if 1 in day_bits:
      extra.append("DAY BITS: {}".format(str(day_bits)))
    if 1 in year_bits:
      extra.append("YEAR BITS: {}".format(str(year_bits)))
    """
    decoded = None
    if len(self.head + self.date + self.body) >= self.min_length( ):
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
  def __init__(self, head, model=None):
    Base.__init__(self, head, model)
    self.head_length = head[1]

class KnownRecord(Base):
  opcode = 0x00
  decodes_date = True

  def parse_time(self):
    if len(self.date) == 5:
      self.datetime = parse_date(self.date)

  def decode(self):
    self.parse_time( )



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

if __name__ == '__main__':
  import doctest
  doctest.testmod( )
