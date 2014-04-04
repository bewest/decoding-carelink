#!/bin/python

import sys

def main(ifile, ofile):
   B = ifile.read( )
   end = len(B)
   cur = 0
   while cur < end:
      ofile.write(B[cur+2:cur+10])
      cur += 10

if __name__ == '__main__':
  ifile = open(sys.argv[1], 'r', 10)
  ofile = open(sys.argv[2], 'w')
  main(ifile, ofile)

#####
# EOF
