#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

##############################################################################
# Edward Robinson
#
# This file is made to easily find op codes and decode their data
#
# inputs :
# argv[1] = file input name
# argv[2] = op_code
# argv[3] = package length
##############################################################################

import sys
import getopt


# uncomment lines below to run as a test
#fileInName = "logs/analyze/20140421_030133-ReadGlucoseHistory-page-16.data"
#op_code = '08'
#pack_len = 6
#reverse = True

class OpCodeFinder:
  bytes = None
  bin_bytes = None
  hex_bytes = None
  found = []
  
  def __init__(self, fileInName, op_code, pack_len, reverse):
    self.fileInName = fileInName
    self.op_code = op_code
    self.pack_len = pack_len
    self.reverse = reverse
  
  def main(self):
    self.find()
    self.pretty_print()
  
  # run without printing
  def find(self):
    self.file_to_bytes()
    if self.reverse:
      self.bytes.reverse()
    self.create_hex_bin_bytes()
    self.search_bytes()
    return self.found
    
  def create_hex_bin_bytes(self):
    self.hex_bytes = []
    self.bin_bytes = []
    for i in range(0, len(self.bytes)):
      self.hex_bytes.append('{0:02x}'.format(self.bytes[i]))
      self.bin_bytes.append('{0:08b}'.format(self.bytes[i]))
  
  def file_to_bytes(self):
    myBytes = bytearray()
    with open(self.fileInName, 'rb') as file:
      while 1:
        byte = file.read(1)
        if not byte:
          break
        myBytes.append(byte)
    self.bytes = myBytes

  def search_bytes(self):
    for i in range(0, len(self.bytes)):
      if self.hex_bytes[i] == self.op_code:
        packet = {}
        packet['start_point'] = i+1
        packet['hex_str'] = '-'.join(self.hex_bytes[i+1:i+1+self.pack_len])
        packet['bin_str'] = '-'.join(self.bin_bytes[i+1:i+1+self.pack_len])
        packet['hex_str_raw'] = ''.join(self.hex_bytes[i+1:i+1+self.pack_len])
        packet['bin_str_raw'] = ''.join(self.bin_bytes[i+1:i+1+self.pack_len])
        packet['op_code'] = self.op_code
        packet['pack_len'] = self.pack_len
        self.found.append(packet)
  
  def pretty_print(self):
    print "****START****\n\n"
    print "Searched (" + self.fileInName + ") for '" + self.op_code + "' of length (" + str(self.pack_len) + ")"
    for i in range(0, len(self.found)):
      packet = self.found[i]
      print "At "+str(packet['start_point'])+" found : ["+packet['hex_str']+"] ["+packet['bin_str']+"]"
    print "\n\n****END*****"


if __name__ == '__main__':
  fileInName = sys.argv[1]
  op_code = sys.argv[2]
  pack_len  = int(sys.argv[3])
  reverse = False
  if sys.argv[4] == "True":
    reverse = True
  op_code_finder = OpCodeFinder(fileInName, op_code, pack_len, reverse)
  op_code_finder.main()
  
#####
# EOF