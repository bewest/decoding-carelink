#!/usr/bin/python

import user
import sys
#import scapy
from scapy.all import *

_usb_response = { 0x00: '', 'U': "Success", 'f': "Fail" }

class USBPacket(Packet):
  name = "USBPacket"

  fields_desc = [
    XByteField("code", 0),
    ByteEnumField("resp", 0x00, _usb_response),
    XByteField("error", 0),
  ]

def main(args):
  print "hello"

if __name__ == '__main__':
  main(list(sys.argv))
#####
# EOF
