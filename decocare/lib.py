"""
This module provides some basic helper/formatting utilities.


>>> hexdump( bytearray( [0x00] ) )
'0000   0x00                                       .'

>>> 0x00 == HighByte( 0x0F )
True

>>> 0x0F == LowByte( 0x0F )
True

>>> CRC16CCITT.compute( bytearray( [ 2, 6, 6, 3 ] ) )
16845

>>> CRC16CCITT.compute( bytearray( [ 0x02, 0x09, 0x00,
...                                  0x05, 0x0D, 0x02, 0x03 ] ) )
29146

>>> BangInt( bytearray( [  0x71, 0xDA ] ) )
29146

>>> BangInt( bytearray( [ 0x62, 0xC2 ] ) ) == CRC16CCITT.compute( bytearray( [ 2, 0x06, 0x08, 3 ] ) )
True


>>> CRC8.compute( bytearray( [ 0x00, 0xFF, 0x00 ] ) )
177

>>> BangInt( bytearray( [ 0x02, 0X02 ] ) )
514

>>> BangLong( bytearray( [ 0x0, 0X0, 0x02, 0x02 ] ) )
514L

"""

from pprint import pformat
from datetime import time as clocks
from datetime import datetime

import dateutil.parser
from dateutil import relativedelta
from binascii import unhexlify, hexlify

def _fmt_hex( bytez ):
  return ' '.join( [ '%#04x' % x for x in list( bytez ) ] )

def _fmt_txt( bytez ):
  return ''.join( [ chr( x ) if 0x20 <= x < 0x7F else '.' \
                    for x in bytez ] )

def basal_time (raw):
  midnight = clocks(0, 0)
  offset = relativedelta.relativedelta(minutes=30*raw)
  start = midnight.replace(hour=offset.hours, minute=offset.minutes)
  return start

class Timer(object):
  def __init__(self):
    self.begin = datetime.now( )
  def millis(self):
    dt = datetime.now() - self.begin
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    return ms

def format_filter_date (date):
  """

    >>> format_filter_date(parse.date('2014-04-09'))
    [7, 222, 4, 9]
  """
  params = [ HighByte(date.year), LowByte(date.year),
             date.month, date.day ]
  return params

def filter_date_today ( ):
  return format_filter_date(datetime.now( ))

class parse:
  @staticmethod
  def date( data ):
    """

    >>> parse.date( '2010-11-10T01:46:00' ).isoformat( )
    '2010-11-10T01:46:00'

    >>> parse.date( '2010-11-10 01:46:00' ).isoformat( )
    '2010-11-10T01:46:00'

    >>> parse.date( '2010-11-10 01:46PM' ).isoformat( )
    '2010-11-10T13:46:00'

    >>> parse.date( '2010-11-10 13:46' ).isoformat( )
    '2010-11-10T13:46:00'

    >>> parse.date( '2010-11-10 1:46AM' ).isoformat( )
    '2010-11-10T01:46:00'

    """
    return dateutil.parser.parse( data )

def hexdump( src, length=8, indent=0 ):
  """
  Return a string representing the bytes in src, length bytes per
  line.

  """
  if len( src ) == 0:
    return ''
  result = [ ]
  indent = ''.join( [ ' ' ] * indent )
  digits = 4 if isinstance( src, unicode ) else 2
  for i in xrange( 0, len( src ), length ):
    s    = src[i:i+length]
    hexa = ' '.join( [ '%#04x' %  x for x in list( s ) ] )
    text = ''.join( [ chr(x) if 0x20 <= x < 0x7F else '.' \
                    for x in s ] )
    result.append( indent + "%04X   %-*s   %s" % \
                 ( i, length * 5
                 , hexa, text ) )
  return '\n'.join(result)


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



def HighByte( arg ):
  return arg >> 8 & 0xFF


def LowByte( arg ):
  return arg & 0xFF



class CRC16CCITT:
  lookup = [ 0, 4129, 8258, 12387, 16516, 20645, 24774,
    28903, 33032, 37161, 41290, 45419, 49548, 53677, 57806,
    61935, 4657, 528, 12915, 8786, 21173, 17044, 29431, 25302,
    37689, 33560, 45947, 41818, 54205, 50076, 62463, 58334,
    9314, 13379, 1056, 5121, 25830, 29895, 17572, 21637,
    42346, 46411, 34088, 38153, 58862, 62927, 50604, 54669,
    13907, 9842, 5649, 1584, 30423, 26358, 22165, 18100,
    46939, 42874, 38681, 34616, 63455, 59390, 55197, 51132,
    18628, 22757, 26758, 30887, 2112, 6241, 10242, 14371,
    51660, 55789, 59790, 63919, 35144, 39273, 43274, 47403,
    23285, 19156, 31415, 27286, 6769, 2640, 14899, 10770,
    56317, 52188, 64447, 60318, 39801, 35672, 47931, 43802,
    27814, 31879, 19684, 23749, 11298, 15363, 3168, 7233,
    60846, 64911, 52716, 56781, 44330, 48395, 36200, 40265,
    32407, 28342, 24277, 20212, 15891, 11826, 7761, 3696,
    65439, 61374, 57309, 53244, 48923, 44858, 40793, 36728,
    37256, 33193, 45514, 41451, 53516, 49453, 61774, 57711,
    4224, 161, 12482, 8419, 20484, 16421, 28742, 24679, 33721,
    37784, 41979, 46042, 49981, 54044, 58239, 62302, 689,
    4752, 8947, 13010, 16949, 21012, 25207, 29270, 46570,
    42443, 38312, 34185, 62830, 58703, 54572, 50445, 13538,
    9411, 5280, 1153, 29798, 25671, 21540, 17413, 42971,
    47098, 34713, 38840, 59231, 63358, 50973, 55100, 9939,
    14066, 1681, 5808, 26199, 30326, 17941, 22068, 55628,
    51565, 63758, 59695, 39368, 35305, 47498, 43435, 22596,
    18533, 30726, 26663, 6336, 2273, 14466, 10403, 52093,
    56156, 60223, 64286, 35833, 39896, 43963, 48026, 19061,
    23124, 27191, 31254, 2801, 6864, 10931, 14994, 64814,
    60687, 56684, 52557, 48554, 44427, 40424, 36297, 31782,
    27655, 23652, 19525, 15522, 11395, 7392, 3265, 61215,
    65342, 53085, 57212, 44955, 49082, 36825, 40952, 28183,
    32310, 20053, 24180, 11923, 16050, 3793, 7920 ]
  @classmethod
  def compute( klass, block ):
    result = 65535
    #result = 0
    for i in xrange( len( block ) ):
      tmp = block[ i ] ^ result >> 8
      result = ( klass.lookup[ tmp ] ^ result << 8 ) & 0xFFFF
    return result


class CRC8:
  lookup = [ 0, 155, 173, 54, 193, 90, 108, 247, 25, 130, 180, 47,
    216, 67, 117, 238, 50, 169, 159, 4, 243, 104, 94, 197, 43, 176,
    134, 29, 234, 113, 71, 220, 100, 255, 201, 82, 165, 62, 8, 147,
    125, 230, 208, 75, 188, 39, 17, 138, 86, 205, 251, 96, 151, 12,
    58, 161, 79, 212, 226, 121, 142, 21, 35, 184, 200, 83, 101, 254,
    9, 146, 164, 63, 209, 74, 124, 231, 16, 139, 189, 38, 250, 97,
    87, 204, 59, 160, 150, 13, 227, 120, 78, 213, 34, 185, 143, 20,
    172, 55, 1, 154, 109, 246, 192, 91, 181, 46, 24, 131, 116, 239,
    217, 66, 158, 5, 51, 168, 95, 196, 242, 105, 135, 28, 42, 177,
    70, 221, 235, 112, 11, 144, 166, 61, 202, 81, 103, 252, 18, 137,
    191, 36, 211, 72, 126, 229, 57, 162, 148, 15, 248, 99, 85, 206,
    32, 187, 141, 22, 225, 122, 76, 215, 111, 244, 194, 89, 174, 53,
    3, 152, 118, 237, 219, 64, 183, 44, 26, 129, 93, 198, 240, 107,
    156, 7, 49, 170, 68, 223, 233, 114, 133, 30, 40, 179, 195, 88,
    110, 245, 2, 153, 175, 52, 218, 65, 119, 236, 27, 128, 182, 45,
    241, 106, 92, 199, 48, 171, 157, 6, 232, 115, 69, 222, 41, 178,
    132, 31, 167, 60, 10, 145, 102, 253, 203, 80, 190, 37, 19, 136,
    127, 228, 210, 73, 149, 14, 56, 163, 84, 207, 249, 98, 140, 23,
    33, 186, 77, 214, 224, 123 ]

  @classmethod
  def compute( klass, block ):
    result = 0
    for i in xrange( len( block ) ):
      result = klass.lookup[ ( result ^ block[ i ] & 0xFF ) ]
    return result


def BangLong( bytez ):
  ( a, b, c, d ) = bytez
  l = a << 24 | b << 16 | c << 8 | d;
  return long( l )


def BangInt( ints ):
  ( x, y ) = ints
  return ( x & 0xFF ) << 8 | y & 0xFF;

def makeByte(highNibble, lowNibble):
  """
    0 <= highNibble <= 15
    0 <= lowNibble  <= 15
    0 <= result     <= 255
  """
  result = highNibble << 4 | lowNibble & 0xF
  return result

ENCODE_TABLE = [ 21, 49, 50, 35, 52, 37, 38, 22,
                 26, 25, 42, 11, 44, 13, 14, 28 ]

_enc_test_1 = [ 0xA7, 0x47, 0x33, 0x62, 0x5D, 0x02, 0x01, 0x01, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x0C ]
_enc_result_1 = [ 0xA9, 0x6D, 0x16, 0x8E, 0x39, 0xB2, 0x94, 0xD5, 0x72, 0x57,
                  0x15, 0x71, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x56, 0xC5 ]

_enc_test_2 = [0xA7, 0x47, 0x33, 0x62, 0x8D, 0x00, 0xA6]
_enc_result_2 = [0xA9, 0x6D, 0x16, 0x8E, 0x39, 0xB2, 0x68, 0xD5, 0x55, 0xAA,
                 0x65]

def encodeDC(msg):
  """
    >>> encodeDC(_enc_test_1) == bytearray(_enc_result_1)
    True
    >>> encodeDC(_enc_test_2) == bytearray(_enc_result_2)
    True


  """
  msg = bytearray(msg)
  # realign bytes
  nibbles = [ ]
  result = [ ]
  # collect nibbles
  for b in msg:
    highNibble = b >> 4 & 0xF
    lowNibble  = b & 0xF
    dcValue1   = ENCODE_TABLE[highNibble]
    dcValue2   = ENCODE_TABLE[lowNibble]
    nibbles.append(dcValue1 >> 2)

    high2Bits = dcValue1 & 0x3
    low2Bits  = dcValue2 >> 4 & 0x3
    nibbles.append( high2Bits << 2 | low2Bits )
    nibbles.append( dcValue2 & 0xF )

  for i in xrange(0, len(nibbles), 2):
    # last item gets a padding terminator
    high, low = nibbles[i], 5
    # most elide the next item
    if i < len(nibbles) - 1:
      low = nibbles[i+1]
    result.append(makeByte(high, low))
  return bytearray(result)


_decode_test_1 = [0xA9, 0x6D, 0x16, 0x8E, 0x39, 0xB2, 0x68, 0xD5, 0x59, 0x56,
                  0x38, 0xD6, 0x8F, 0x28, 0xF2, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55, 0x55,
                  0x55, 0x55, 0x55, 0x55, 0x55, 0xB3, 0x25]
_decode_result_1 = [0xA7, 0x47, 0x33, 0x62, 0x8D, 0x09, 0x03, 0x37, 0x32, 0x32,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0xC2]
_decode_test_2 = [0xA9, 0x6D, 0x16, 0x8E, 0x39, 0xB2, 0x56, 0x65, 0x55, 0x56,
                  0x35]
_decode_result_2 = [0xA7, 0x47, 0x33, 0x62, 0x06, 0x00, 0x03]
def decodeDC(msg):
  """
    >>> decodeDC(_decode_test_1) == bytearray(_decode_result_1)
    True
    >>> decodeDC(_decode_test_2) == bytearray(_decode_result_2)
    True
  """
  msg = bytearray(msg)
  result      = [ ]
  nibbleCount =  0
  bitCount    =  0
  sixBitValue =  0
  highValue   =  0
  highNibble  =  0
  #
  for B in msg:
    bP = 7
    while bP >= 0:
      bitValue = B >> bP & 0x1
      sixBitValue = sixBitValue << 1 | bitValue
      bitCount += 1
      if bitCount != 6:
        bP -= 1
        continue; # next
      nibbleCount += 1
      if nibbleCount == 1:
        highNibble = decodeDCByte(sixBitValue)
      else:
        lowNibble = decodeDCByte(sixBitValue)
        byteValue = makeByte(highNibble, lowNibble)
        # append to result
        result.append(byteValue)
        nibbleCount = 0
      sixBitValue = 0
      bitCount    = 0
      bP -= 1

  return bytearray(result)

def decodeDCByte(B):
  # B should be 0 < B && B < 63
  # look up in decode table
  return ENCODE_TABLE.index(B)


def decode_hexline (line):
  return bytearray(str(''.join(line.split( ))).decode('hex'))


def hexbytes (hexstr):
    return bytearray(unhexlify(hexstr))

if __name__ == '__main__':
  import doctest
  doctest.testmod( )

#####
# EOF
