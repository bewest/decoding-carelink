
##############################################################################
# Edward Robinson
#
# This file is made to convert hex files to binary files with
#
# inputs :
# argv[1] = file input name
# argv[2] = output type (bin=pure binary, hex=hexidecimal)
# argv[3] = with new characters (true or false)
##############################################################################

import sys
import getopt


lineSize = 10
#fileInName = sys.argv[1]
#outType = sys.argv[2]
#if sys.argv[3] == "true":
#    withNewLine = True
#else:
#    withNewLine = False
outType = "hex"
fileInName = "ReadHistoryData-page-0.data"
withNewLine = False
if outType == "bin":
    fileOutName = fileInName + ".bin"
else:
    fileOutName = fileInName + ".hex"

myBytes = bytearray()
with open(fileInName, 'rb') as file:
    while 1:
        byte = file.read(1)
        if not byte:
            break
        myBytes.append(byte)

#j = len(myBytes)
#print j
#j = j - 1
#print myBytes[j]
#print '{0:08b}'.format(myBytes[j])
#print hex(myBytes[j])


# myBytes=myBytes.replace("\n","")
# myBytes=myBytes.replace("\t","")
j = 0
fileOut = open(fileOutName, 'w')
# only do line by line if there will be multiple lines
if len(myBytes) > lineSize:
    for i in range(0, len(myBytes) - lineSize, lineSize):
        for j in range(0, lineSize):
            # convert byte to appropriate format
            if outType == "bin":
                out = '{0:08b}'.format(myBytes[j + i])
            else:
                out = '{0:02x}'.format(myBytes[j + i])
            fileOut.write(out)
        if withNewLine:
            fileOut.write("\n")
        j = i + lineSize

# if the last few bytes don't fill a line from the loop above print them here
if j < len(myBytes):
    for i in range(0, len(myBytes) - j):
        # convert to hex or binary and print
        if outType == "bin":
            out = '{0:08b}'.format(myBytes[i])
        else:
            out = '{0:02x}'.format(myBytes[i])
        fileOut.write(out)
        if withNewLine:
            fileOut.write("\n")
# info stuff
# print "bytes raw : " + myBytes
# print "bytes bin : " + '{0:08b}'.format(myBytes)
# print "bytes hex : " + hex(myBytes)
