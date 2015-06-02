#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

################################################################################
#
# Edward Robinson
#
# This file is built to be able to test parsing MM raw data files.
#
################################################################################

# inputs file name, op_code, pack_len, bin to interpret, 
# get the packets from the file
# for each packet convert the requested bits to an integer
# 

import sys
import getopt
from find_print_op_codes import OpCodeFinder

class ParserTest:
  
  def main(self, packets, bin_to_read_start, bin_to_read_end, reverse):
    self.packets = packets
    for i in range(0, len(self.packets)):
      if reverse:
        packet = self.packets[len(self.packets) - i - 1]
      else:
        packet = self.packets[i]
      bin = packet['bin_str_raw'][bin_to_read_start:bin_to_read_end]
      dec = int(bin, 2)
      print_str = "At "+str(packet['start_point'])+":  "
      print_str += "bin[" + str(bin_to_read_start) + ":" + str(bin_to_read_end) + "] "
      print_str += "= " + str(dec) + "  ["+packet['hex_str']+"] ["+packet['bin_str']+"]"
      print print_str




if __name__ == '__main__':
  fileInName = sys.argv[1]
  op_code = sys.argv[2]
  pack_len  = int(sys.argv[3])
  reverse = False
  if sys.argv[4] == "True":
    reverse = True
    
  bin_to_read_start = int(sys.argv[5])
  bin_to_read_end = int(sys.argv[6])
  
  op_code_finder = OpCodeFinder(fileInName, op_code, pack_len, reverse)
  packets = op_code_finder.find()
  parser = ParserTest()
  parser.main(packets, bin_to_read_start, bin_to_read_end, reverse)
  
  
#####
# EOF