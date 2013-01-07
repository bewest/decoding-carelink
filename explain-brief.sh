#!/bin/bash
# terser explanation of log
# Useful to tell what clear_buffer has been up to.

LOG='status-quo.log'

function diagnose_crc ( ) {

  grep -n --color  -E "howdy|clear_bu|BAD|CRC|ACK|IGNORE|download|traceback|critical|(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" $LOG

}

function summarize_stick ( ) {
  if [[ 6 -eq $(grep -E "howdy" $LOG | grep stick | wc -l) ]] ; then
    echo "stick runs appear to be ok"
  else
    echo "not ok"
  fi

}

function summarize_pump ( ) {
  _error=0
  if [[ 4 -eq $(grep -E "howdy" $LOG | grep pump | wc -l) ]] ; then
    echo "howdy! pump runs appear to be OK"
  else
    _error=1
    echo "howdy! pump runs were NOT OK"
  fi

  echo -n PAGES downloaded:
  grep -E "finished.*ReadHistory" $LOG | sort | uniq | wc -l

  if [[ 0 -eq $(grep -E "BadCRC" $LOG | wc -l) ]] ; then
    echo "NO CRC ERROR FOUND"
  else
    _error=1
    echo "CRC ERROR FOUND"
    diagnose_crc
  fi
  if [[ 0 -eq $(grep -E "NAK" $LOG | wc -l) ]] ; then
    echo "NO NAK FOUND"
  else
    _error=1
    echo "NAK FOUND"
  fi

  if [[ 0 -eq $_error ]] ; then
    echo "SUCCESS, GOOD CLEAN RUN"
  else
    echo "NOT A CLEAN RUN"
  fi

}

summarize_stick
summarize_pump

#####
# EOF
