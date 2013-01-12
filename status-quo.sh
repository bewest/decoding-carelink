#!/bin/bash
# make an example of an interesting log worth sharing

CMD="$*"
NAME=$0
PORT=${1-'/dev/ttyUSB0'}
SERIAL=${2-'208850'}

. bin/common

run_all 2>&1 | tee status-quo.log

echo "OUT" | tee logs/explain.log
. ./explain-brief.sh | tee -a logs/explain.log
explain_markdown


#####
# EOF
