
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


fileInName = sys.argv[1]
op_code = sys.argv[2]
pack_len  = int(sys.argv[3])

# uncomment lines below to run as a test
#fileInName = "logs/analyze/20140421_030133-ReadGlucoseHistory-page-16.data"
#op_code = '08'
#pack_len = 4


myBytes = bytearray()
with open(fileInName, 'rb') as file:
    while 1:
        byte = file.read(1)
        if not byte:
            break
        myBytes.append(byte)


myHexBytes = []
myBinBytes = []
for i in range(0, len(myBytes)):
    myHexBytes.append('{0:02x}'.format(myBytes[i]))
    myBinBytes.append('{0:08b}'.format(myBytes[i]))
    
for i in range(0, len(myBytes)):
    if myHexBytes[i] == op_code:
        pack_start = i+1
        hex_str = '-'.join(myHexBytes[pack_start:pack_start+pack_len])
        bin_str = '-'.join(myBinBytes[pack_start:pack_start+pack_len])
        print "At "+str(i)+" found : ["+myHexBytes[i]+"] ["+hex_str+"] ["+bin_str+"]"
        

