#!/bin/bash
#
# Author: Ben West
# My hexdumps are apparently in a weird format, many apologies.
# In order for xxd to convert them to binary, all the non-hex data must be
# stripped out, and then passed to xxd -r -p.
# It's important to note that with the -p, xxd will convert everything
# it sees into binary from hex, because it will assume there are no
# columns that are not hexadecimal.

infile=$1
out=$2

cat $infile | tr -s ' ' | cut -d' ' -f 2-9 | xxd -r -p - $out

#####
# EOF
