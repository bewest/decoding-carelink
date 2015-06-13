#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse

from pprint import pprint, pformat
from binascii import hexlify
from datetime import datetime
from scapy.all import *

from decocare import lib
from decocare.history import *

class MMMomentBase(XByteField):
  """
A field should be considered in different states:

i (nternal) : this is the way Scapy manipulates it.

m (achine) : this is where the truth is, that is the layer as it is
on the network.

h (uman) : how the packet is displayed to our human eyes.

This explains the mysterious methods i2h(), i2m(), m2i() and so on
available in each field: they are conversion from one state to
another, adapted to a specific use.

Other special functions:

any2i() guess the input representation and returns the internal one.
i2repr() a nicer i2h()

However, all these are "low level" functions. The functions adding or
extracting a field to the current layer are:


    class StrFixedLenField(StrField):
      def addfield(self, pkt, s, val):
        # copy the network representation of
        # field val (belonging to layer pkt)
        # to the raw string packet s
        return s+struct.pack("%is"%self.length,self.i2m(pkt, val))

      def getfield(self, pkt, s):
        # extract from the raw packet s the field
        # value belonging to layer pkt. It returns a list, the 1st element
        # is the raw packet string after having removed the extracted
        # field, the second one is the extracted field itself in internal
        # representation:

        return s[self.length:], self.m2i(pkt,s[:self.length])

When defining your own layer, you usually just need to define some
*2*() methods, and sometimes also the addfield() and getfield().




  """
  def i2h(self, pkt, pay):
    pass
  def i2m(self, pkt, pay):
    pass
  def m2i(self, pkt, pay):
    pass

class XXXStrField(Field):
    def __init__(self, name, default, fmt="H", remain=0):
        Field.__init__(self,name,default,fmt)
        self.remain = remain
    def i2len(self, pkt, i):
        return len(i)
    def i2m(self, pkt, x):
        if x is None:
            x = ""
        elif type(x) is not str:
            x=str(x)
        return x
    def addfield(self, pkt, s, val):
        return s+self.i2m(pkt, val)
    def getfield(self, pkt, s):
        if self.remain == 0:
            return "",self.m2i(pkt, s)
        else:
            return s[-self.remain:],self.m2i(pkt, s[:-self.remain])
    def randval(self):
        return RandBin(RandNum(0,1200))

class XXStrLenField(StrField):
    def __init__(self, name, default, fld=None, length_from=None):
        StrField.__init__(self, name, default)
        self.length_from = length_from
    def getfield(self, pkt, s):
        l = self.length_from(pkt)
        return s[l:], self.m2i(pkt,s[:l])

class XXXStrFixedLenField(StrField):
    def __init__(self, name, default, length=None, length_from=None):
        StrField.__init__(self, name, default)
        self.length_from  = length_from
        if length is not None:
            self.length_from = lambda pkt,length=length: length
    def i2repr(self, pkt, v):
        if type(v) is str:
            v = v.rstrip("\0")
        return repr(v)
    def getfield(self, pkt, s):
        l = self.length_from(pkt)
        return s[l:], self.m2i(pkt,s[:l])
    def addfield(self, pkt, s, val):
        l = self.length_from(pkt)
        return s+struct.pack("%is"%l,self.i2m(pkt, val))
    def randval(self):
        try:
            l = self.length_from(None)
        except:
            l = RandNum(0,200)
        return RandBin(l)


class XXXStrStopField(StrField):
    def __init__(self, name, default, stop, additionnal=0):
        Field.__init__(self, name, default)
        self.stop=stop
        self.additionnal=additionnal
    def getfield(self, pkt, s):
        l = s.find(self.stop)
        if l < 0:
            return "",s
#            raise Scapy_Exception,"StrStopField: stop value [%s] not found" %stop
        l += len(self.stop)+self.additionnal
        return s[l:],s[:l]
    def randval(self):
        return RandTermString(RandNum(0,1200),self.stop)


class MMMomentField(StrField):
  def __init__(self, name, default, fmt="B", remain=0):
      StrField.__init__(self, name, default, fmt='B', remain=remain)


class MaskedMoment(MMMomentField):
  MASK = Mask.time
  def mask_value(self, value):
    return value & self.MASK
  def remaining_value(value):
    return value & ( ~self.Mask & 0xff )

class Year(MaskedMoment):
  """
    # >>> Year( ) / str(bytearray([0x06]))
  """
  MASK = Mask.year

  def m2i(self, pkt, raw):
    candidate = raw[0]
    value = candidate & self.MASK
    result = value + 2000
    return result

    return str(bytearray(parse_years(raw)))

  def i2m(self, pkt, x):
    print "XXX: i2m %r" % repr(x)
    if x is None or x == "":
      return ""
    return str(bytearray( [ x - 2000 ] ))

  def addfield(self, pkt, s, val):
      print "XXXX: addfield: pkt: %r" % pkt
      print "XXXX: addfield: s: %r" % s
      print "XXXX: addfield: val: %r" % val
      return s+self.i2m(pkt, val)

  def getfield(self, pkt, s):
    y = s[0]
    print "XXX: getfield: s: %r len(%s)" % (s, len(s))
    val = bytearray( s[0] )
    print "XXX: getfield: %s" % repr(val)
    return s[1:], self.m2i(pkt, val)

class TestYearPacket(Packet):
  """
    >>> TestYearPacket( ) / str(bytearray( [ 0x06 ] ))

    >>> (TestYearPacket( ) / str(bytearray( [ 0x06 ] ))).show2( )

    >>> TestYearPacket( str(bytearray( [ 0x06 ] )) )

  """
  fields_desc = [
    Year('year', '')
  ]

class Month(MMMomentField):
  def __init__(self, name, default, high=None, low=None):
      MMMomentField.__init__(self, name, default, fmt='BB')
      self.high = high
      self.low = low

  def addfield(self, pkt, s, val):
    def addfield(self, pkt, s, val):
        l = self.length_from(pkt)
        return s+struct.pack("%is"%l,self.i2m(pkt, val))

class Day(MaskedMoment):
  MASK = Mask.year
  pass

class Hour(MMMomentField):
  pass

class Minute(MaskedMoment):
  MASK = Mask.invert
  pass

class Second(MMMomentField):
  MASK = Mask.invert
  pass


class TestSecondPacket(Packet):
  """
  >>> TestSecondPacket( ) / str(bytearray( [ 0x6f ] ))
  """
  fields_desc = [
    Second("second", None),
  ]

class TestMinutePacket(Packet):
  """
  >>> TestMinutePacket( ) / str(bytearray( [ 0xd7 ] ))
  """
  fields_desc = [
    Minute("minute", None),
  ]

class TestMonthPacket(Packet):
  """
  >>> TestMonthPacket( ) / str(bytearray( [ 0x6f, 0xd7 ] ))
  """
  fields_desc = [
    Month("month", None),
  ]

class TestTimeHeadPacket(Packet):
  """
  >>> TestTimeHeadPacket( ) / str(bytearray( [ 0x6f, 0xd7 ] ))
  """
  fields_desc = [
    Second("second", None),
    Minute("minute", None),
    Month("month", None, high="second", low="minute"),
  ]


class MMDateField(Field):
    """
    # >>> MMDateField[(str(bytearray([0x06])))
    """
    def __init__(self, name, default, fmt="H", remain=0):
        Field.__init__(self,name,default,fmt)
        self.remain = remain
    def i2len(self, pkt, i):
        return len(i)
    def i2m(self, pkt, x):
        if x is None:
            x = ""
        elif type(x) is not str:
            x=str(x)
        return x
    def addfield(self, pkt, s, val):
        return s+self.i2m(pkt, val)
    def getfield(self, pkt, s):
        if self.remain == 0:
            return "",self.m2i(pkt, s)
        else:
            return s[-self.remain:],self.m2i(pkt, s[:-self.remain])
    def randval(self):
        return RandBin(RandNum(0,1200))



class XXMMDate(Field):
  def i2h(self, pkt, x):
    pass
  def i2m(self, pkt, x):
    pass
  def m2i(self, pkt, x):
    if x is None:
      return None, 0

    pass

class MMDateTime(Packet):
  """
  >>> MMDateTime( ) / str(bytearray( [ 0x6f, 0xd7, 0x08, 0x01, 0x06 ] ))
  """
  name = "TIME"

  fields_desc = [
    Second("second", None),
    Minute("minute", None),
    Month("month", None, high="second", low="minute"),
    Hour("hour", None),
    Day("day", None),
    Year("year", None),
  ]

class MMAction(Packet):
  name = 'Logged Action %s' % __name__

  fields_desc = [
    PacketField('datetime', None, MMDateTime),
  ]

def main( ):
  print "I do nothing."

if __name__ == '__main__':
  import doctest
  failures, tests = doctest.testmod( )
  if failures > 0:
    print "REFUSING TO RUN DUE TO FAILED TESTS"
    sys.exit(1)
  main( )

#####
# EOF
