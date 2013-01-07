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

  grep -n --color  -E "howdy|clear_bu|BAD|CRC|ACK|IGNORE|download|traceback|critical|(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" $LOG

}

function only_stats ( ) {

  grep -n -E "(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" -

}

function summarize_stick ( ) {
  if [[ 6 -eq $(grep -E "howdy" $LOG | grep stick | wc -l) ]] ; then
    echo "* stick runs appear to be ok"
  else
    echo "* not ok"
  fi

}

function summarize_pump ( ) {
  _error=0
  if [[ 4 -eq $(grep -E "howdy" $LOG | grep pump | wc -l) ]] ; then
    echo '## howdy! pump runs appear to be OK'
  else
    _error=1
    echo 'howdy! pump runs were NOT OK'
    echo "### Last send command"
    echo '```'
    grep -B 1000 -E "Traceback" $LOG | grep -A 2 -E "Transmit" | tail -n 4
    echo '```'
    echo "### Traceback"
    echo '```'
    grep -B 10 -A 15 -E "Traceback" $LOG
    echo '```'
    echo "### stats"
    echo '```'
    grep -A 1000 -E "Traceback" $LOG | only_stats | head -n 20
    echo '```'

  fi

  echo -n '* PAGES downloaded:'
  grep -E "finished.*ReadHistory" $LOG | sort | uniq | wc -l

  if [[ 0 -eq $(grep -E "BadCRC" $LOG | wc -l) ]] ; then
    echo "* NO CRC ERROR FOUND"
  else
    _error=1
    echo "* CRC ERROR FOUND"
    diagnose_crc
  fi
  if [[ 0 -eq $(grep -E "NAK" $LOG | wc -l) ]] ; then
    echo "* NO NAK FOUND"
  else
    _error=1
    echo "* NAK FOUND"
  fi

  if [[ 0 -eq $_error ]] ; then
    echo "* SUCCESS, GOOD CLEAN RUN"
  else
    echo "* NOT A CLEAN RUN"
  fi

}

echo '## Observations'
date
echo '## stick'
summarize_stick
echo '## pump'
summarize_pump

#####
# EOF
```
## cat explain.log
OUT
## Observations
Mon Jan  7 14:37:43 PST 2013
## stick
* stick runs appear to be ok
## pump
## howdy! pump runs appear to be OK
* PAGES downloaded:9
* NO CRC ERROR FOUND
* NO NAK FOUND
* SUCCESS, GOOD CLEAN RUN
