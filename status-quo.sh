#/bin/bash
# make an example of an interesting log worth sharing

export TIME="%C\n\telapsed %E\n\tuser %U\n\tsystem %S\n\tCPU %P (%Xtext+%Ddata %Mmax)k"

SERIAL=${1-'208850'}
CMD="$*"
NAME=$0

( cat $NAME
  echo $NAME $CMD
  date
  export TIME="%C\n\telapsed %E\n\tuser %U\n\tsystem %S\n\tCPU %P (%Xtext+%Ddata %Mmax)k"
  time (
  export TIME="%C\n\telapsed %E\n\tuser %U\n\tsystem %S\n\tCPU %P (%Xtext+%Ddata %Mmax)k"
  time python pump/stick.py /dev/ttyUSB0
  time python pump/session.py /dev/ttyUSB0 ${SERIAL}
  time python pump/commands.py /dev/ttyUSB0 ${SERIAL}
  echo "Was there an ACK ERROR?"
  echo "### DIAGNOSE CRC"
  time python pump/stick.py /dev/ttyUSB0
  time python pump/stick.py /dev/ttyUSB0
) 2>&1 ) 2>&1 | tee status-quo.log

#####
# EOF
