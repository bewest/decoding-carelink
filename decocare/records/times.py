
from datetime import datetime

class NotADate(Exception): pass

class Mask:
  """
  Some useful bit masks.
  """
  time   = 0xC0
  invert = 0x3F
  year   = 0x7F
  day    = 0x1F


def quick_hex(bb):
  return ' '.join( [ '%#04x' % x for x in bb ] )

def parse_seconds(sec):
  """
  simple mask
  >>> parse_seconds(0x92)
  18
  """
  return sec & Mask.invert

def parse_minutes(minutes):
  """
  simple mask
  >>> parse_minutes(0x9e)
  30
  """
  return minutes & Mask.invert


def parse_hours(hours):
  """
  simple mask
  >>> parse_hours(0x0b)
  11

  >>> parse_hours(0x28)
  8

  """
  return int(hours & 0x1f)

def parse_day(day):
  """
  simple mask
  >>> parse_day( 0x01 )
  1
  """
  return day & Mask.day

def parse_months(seconds, minutes):
  """
  calculate from extra bits shaved off of seconds and minutes:

  >>> parse_months( 0x92, 0x9e )
  10

  """
  high = (seconds & Mask.time) >> 4
  low  = (minutes & Mask.time) >> 6
  return high | low

def parse_years_lax(year):
  """
  simple mask plus correction
  """
  y = (year & Mask.year) + 2000
  return y


def extra_year_bits(year=0x86):
  """
  practice getting some extra bits out of the year byte
  >>> extra_year_bits( )
  [1]

  >>> extra_year_bits(0x06)
  [0]

  >>> extra_year_bits(0x86)
  [1]

  >>> extra_year_bits(0x46)
  [0]

  >>> extra_year_bits(0x26)
  [0]

  >>> extra_year_bits(0x16)
  [0]

  """
  # year = year[0]
  masks = [ ( 0x80, 7) ]
  nibbles = [ ]
  for mask, shift in masks:
    nibbles.append( ( (year & mask) >> shift ) )
  return nibbles

def extra_hour_bits(value):
  """
  practice getting extra bits out of the hours bytes

  >>> extra_hour_bits(0x28)
  [0, 0, 1]

  >>> extra_hour_bits(0x8)
  [0, 0, 0]
  """
  masks = [ ( 0x80, 7), (0x40, 6), (0x20, 5), ]
  nibbles = [ ]
  for mask, shift in masks:
    nibbles.append( ( (value & mask) >> shift ) )
  return nibbles

def parse_years(year):
  """
    simple mask plus correction
    >>> parse_years(0x06)
    2006

  """
  # if year > 0x80:
  #  year = year - 0x80
  y = (year & Mask.year) + 2000
  # if y < 0 or y < 1999 or y > 2015:
  #   raise ValueError(y)
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

def unmask_date(data):
  """
  Extract date values from a series of bytes.
  Always returns tuple given a bytearray of at least 5 bytes.

  Returns 6-tuple of scalar values year, month, day, hours, minutes,
  seconds.
  >>> unmask_date(bytearray( [ 0x6f, 0xd7, 0x08, 0x01, 0x06 ] ))
  (2006, 7, 1, 8, 23, 47)

  >>> unmask_date( bytearray( [ 0x00 ] * 5 ))
  (2000, 0, 0, 0, 0, 0)

  """
  data = data[:]
  seconds = parse_seconds(data[0])
  minutes = parse_minutes(data[1])

  hours   = parse_hours(data[2])
  day     = parse_day(data[3])
  year    = parse_years(data[4])

  month   = parse_months( data[0], data[1] )
  return (year, month, day, hours, minutes, seconds)

def parse_date(date, strict=False, loose=False):
  """
  Choose whether or not to throw an error if you get a bad date.
  """
  try:
    return parse_date_strict(date)
  except NotADate, e:
    if strict:
      raise
    if loose:
      return unmask_date(data)

  return None

def parse_date_strict(data):
  """
  Apply strict datetime validation to extract a datetime from a series
  of bytes.
  Always throws an error for bad dates.

  >>> parse_date(bytearray( [ 0x6f, 0xd7, 0x08, 0x01, 0x06 ] )).isoformat( )
  '2006-07-01T08:23:47'


  """
  (year, month, day, hours, minutes, seconds) = unmask_date(data)
  try:
    date = datetime(year, month, day, hours, minutes, seconds)
    return date
  except ValueError, e:
    raise NotADate(e)

__test__ = {
  'unmask': '''
  These examples are fixed! Thanks ehwest, robg.
  >>> unmask_date( bytearray( [ 0x93, 0xd4, 0x0e, 0x10, 0x0c ] ))
  (2012, 11, 16, 14, 20, 19)

  >>> unmask_date( bytearray( [ 0xa6, 0xeb, 0x0b, 0x10, 0x0c, ] ))
  (2012, 11, 16, 11, 43, 38)

  >>> unmask_date( bytearray( [ 0x95, 0xe8, 0x0e, 0x10, 0x0c ] ))
  (2012, 11, 16, 14, 40, 21)


  >>> unmask_date( bytearray( [ 0x80, 0xcf, 0x30, 0x10, 0x0c, ] ))
  (2012, 11, 16, 16, 15, 0)


  >>> unmask_date( bytearray( [ 0xa3, 0xcf, 0x30, 0x10, 0x0c, ] ))
  (2012, 11, 16, 16, 15, 35)

''',

  'encode_monthbyte': '''
  >>> encode_monthbyte(month=1) == bytearray(b'\x12^')
  True

  >>> encode_monthbyte(month=2) == bytearray(b'\x12\x9e')
  True

  >>> encode_monthbyte(month=3) ==  bytearray(b'\x12\xde')
  True

  >>> encode_monthbyte(month=10, minute=0, sec=0) == bytearray(b'\x80\x80')
  True

  >>> encode_monthbyte(month=10, minute=0, sec=24) == bytearray(b'\x98\x80')
  True
''',

}

if __name__ == '__main__':
  import doctest
  doctest.testmod( )
