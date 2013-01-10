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
  grep -E "session:finished.*ReadHistory" $LOG | grep "data\[1024\]" | sort | uniq | wc -l
  echo ""
  echo '```'
  grep -E "session:finished executing.*ReadHistory" $LOG | sort | uniq
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
    if [[ 0 -eq $(grep -E "BadCRC" $LOG | grep -v -E 'returning empty|IGNORE' | wc -l) ]] ; then
      echo ""
      echo -n '## CRC errors found, caught, recovered: '
      grep -n -E "BadCRC" $LOG | grep -E "returning empty|IGNORE" | wc -l
      echo ""
      echo '```'
      grep -n -E "BadCRC" $LOG | grep -E "returning empty|IGNORE"
      echo '```'
      echo ""
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
  fi
  if [[ 0 -eq $(grep -E "NAK" $LOG | wc -l) ]] ; then
    echo "* no nak found"
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
Wed Jan  9 23:52:25 PST 2013

## stick

* stick runs appear to be ok


## pump


## downloaded:6

```
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][0]:data[1024]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][1]:data[1024]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][2]:data[1024]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][3]:data[1024]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][4]:data[1472]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][4]:data[704]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][5]:data[1024]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][6]:data[1152]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][6]:data[384]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][7]:data[1024]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][8]:data[1152]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][8]:data[384]:
```

## howdy! pump runs appear to be OK


## CRC errors found, caught, recovered: 9

```
1848:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
14058:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
15128:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
16909:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
17244:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
18108:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
19849:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
20184:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
21048:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
```

* no nak found
* SUCCESS, GOOD CLEAN RUN
