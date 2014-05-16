##############################################################################
# Edward Robinson
#
# This file is made to easily find some data in the file to help decode data files
#
# inputs :
# argv[1] = file input name
# argv[2] = op_code
# argv[3] = package length
##############################################################################

import sys
import getopt


file_in_name = sys.argv[1]
data_to_find = sys.argv[2]

# uncomment lines below to run as a test
file_in_name = "logs/analyze/20140421_030133-ReadGlucoseHistory-page-16.data"
data_to_find = ""
print_data_before = false # if true will print data before , if false will print after


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
        
