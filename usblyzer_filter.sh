#!/bin/bash
# Filter input file so that only useful columns are shown.
# Also only show lines with content following (in|out),.*$
# Playing around shows that each set of data is always represented exactly
# twice, uniq reliably halves it.
cut -d, -f 1,2,3,4,9,16 $1 | egrep "(,(in|out))([,]).*$" \
  | cut -d, -f5- | uniq
#####
# EOF
