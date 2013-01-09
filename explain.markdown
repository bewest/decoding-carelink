# ./status-quo.sh 
## cat ./status-quo.sh
```bash
#/bin/bash
# make an example of an interesting log worth sharing

export TIME="%C\n\telapsed %E\n\tuser %U\n\tsystem %S\n\tCPU %P (%Xtext+%Ddata %Mmax)k"

CMD="$*"
NAME=$0
PORT=${1-'/dev/ttyUSB0'}
SERIAL=${2-'208850'}

( 
  echo "# ${NAME} ${CMD}"
  cat $NAME
  date
  TIME="$TIME" time python pump/stick.py ${PORT}
  TIME="$TIME" time python pump/session.py ${PORT} ${SERIAL}
  TIME="$TIME" time python pump/commands.py ${PORT} ${SERIAL}
  echo "Was there an ACK ERROR?"
  echo "### DIAGNOSE CRC"
  TIME="$TIME" time -f "$TIME" python pump/stick.py ${PORT}
  TIME="$TIME" time -f "$TIME" python pump/stick.py ${PORT}
) 2>&1 | tee status-quo.log

  echo "OUT" | tee explain.log
  ./explain-brief.sh | tee -a explain.log

  echo "# ${NAME} ${CMD}" > explain.markdown

  echo "## cat ${NAME}" >> explain.markdown
  echo '```bash'        >> explain.markdown
  cat $NAME             >> explain.markdown
  echo '```'            >> explain.markdown

  echo "## cat explain-brief.sh" >> explain.markdown
  echo '```bash'                 >> explain.markdown
  cat explain-brief.sh           >> explain.markdown
  echo '```'                     >> explain.markdown

  echo "## cat explain.log" >> explain.markdown
  cat explain.log           >> explain.markdown

#####
# EOF
```
## cat explain-brief.sh
```bash
#!/bin/bash
# terser explanation of log
# Useful to get a succinct idea of what just happened.
# We're looking for more info on what happens when CRCs occur, or when
# NAKs are found, but basically nothing otherwise.
# Happens to output valid markdown.
# Useful to tell what clear_buffer has been up to.

LOG='status-quo.log'

function diagnose_crc ( ) {

  grep -n --color  -E "howdy|clear_bu|NAK|BAD|CRC|ACK|IGNORE|download|traceback|critical|(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" $LOG

}

function diagnose_nak ( ) {

  grep -n -C 20 "NAK" $LOG

}

function only_stats ( ) {

  grep -n -E "(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" -

}

function summarize_stick ( ) {
  echo ""
  if [[ 6 -eq $(grep -E "howdy" $LOG | grep stick | wc -l) ]] ; then
    echo "* stick runs appear to be ok"
  else
    echo "* not ok"
  fi
  echo ""

}

function summarize_pump ( ) {
  _error=0
  echo ""
  echo -n '## downloaded:'
  grep -E "finished.*ReadHistory" $LOG | sort | uniq | wc -l
  echo ""
  echo '```'
  grep -E "finished.*ReadHistory" $LOG | sort | uniq
  echo '```'
  echo ""

  if [[ 4 -eq $(grep -E "howdy" $LOG | grep pump | wc -l) ]] ; then
    echo '## howdy! pump runs appear to be OK'
    echo ""
  else
    _error=1
    echo 'howdy! pump runs were NOT OK'

    echo ""
    echo "### Last send command"
    echo ""
    echo '```'
    grep -B 1000 -E "Traceback" $LOG | grep -A 2 -E "Transmit" | tail -n 4
    echo '```'

    echo "### stats before traceback"
    echo ""
    echo '```'
    grep -A 1000 -E "Traceback" $LOG | only_stats | head -n 20
    echo '```'


    echo "### Traceback"
    echo ""
    echo '```'
    grep -B 10 -A 15 -E "Traceback" $LOG
    echo '```'
  fi


  if [[ 0 -eq $(grep -E "BadCRC" $LOG | wc -l) ]] ; then
    echo "* NO CRC ERROR FOUND"
  else
    _error=1
    echo ""
    echo '## Diagnose CRC'
    echo ""
    echo '```'
    diagnose_crc
    echo '```'
    echo ""
  fi
  if [[ 0 -eq $(grep -E "NAK" $LOG | wc -l) ]] ; then
    echo "* NO NAK FOUND"
  else
    _error=1
    echo ""
    echo "## NAK FOUND"
    echo ""
    echo '```'
    diagnose_nak
    echo '```'
    echo ""
  fi

  if [[ 0 -eq $_error ]] ; then
    echo "* SUCCESS, GOOD CLEAN RUN"
  else
    echo "* NOT A CLEAN RUN"
  fi

}

echo '## Observations'
date
echo ""
echo '## stick'
summarize_stick
echo ""
echo '## pump'
echo ""
summarize_pump

#####
# EOF
```
## cat explain.log
OUT
## Observations
Tue Jan  8 22:52:16 PST 2013

## stick

* stick runs appear to be ok


## pump


## downloaded:9

```
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xca\x80@\xa7\x01 \x88P\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][1], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][2], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x92\x9e\x0b\x01\x06\x07\x00\x00\x02L\xa1\x06l\xa1\x06\x05\x0c\x00\xe8\x00\x00\x00\x00\x02L\x02Ld\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][3], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x04\xda\x82\x0cl\x82\x0c\x05\x00edf\x12\x00\x00\x04\xda\x03\x9eK\x01<\x19\x00O\x01<\x19\x01<d\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x00d\x01V\xca\x06\x01\x06\x17\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][4], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x01\x12\x17\x00\x9f\x08\x14\x01\x12\x18\x00\x80\x08\x14\x01\x0c\x07\x00\x00\x00\x06\x81\x12l\x81\x12\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x06\x00\x06d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][5], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x00\x02\x00!\x00l!\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x02\x00\x02\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x0c\x9c\x13\x02\x00\x17')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][6], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x00\x00,\x00l,\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00-\x00l-')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][7], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x15\x80l\x15\x80\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][8], bytearray(b'\x00\xca\x80@\xa7\x01 \x88P&\x00\xe8\x00\x00\x00\x00\x036\x036d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x036\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
```

## howdy! pump runs appear to be OK

* NO CRC ERROR FOUND
* NO NAK FOUND
* SUCCESS, GOOD CLEAN RUN
