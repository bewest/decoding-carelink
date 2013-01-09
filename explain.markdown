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
Tue Jan  8 21:13:44 PST 2013

## stick

* stick runs appear to be ok


## pump


## downloaded:0

```
```

howdy! pump runs were NOT OK

### Last send command

```
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<TransmitPacket:ReadPumpModel>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<TransmitPacket:ReadPumpModel>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
```
### stats before traceback

```
204:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 78L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 78L, 'errors.crc': 0}
222:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 8L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1L, 'errors.crc': 0}
223:INFO:__main__:{'radio': {'errors.crc': 0,
224:           'errors.naks': 0,
225:           'errors.sequence': 0,
226:           'errors.timeouts': 4,
227:           'packets.received': 1L,
228:           'packets.transmit': 8L},
229: 'usb': {'errors.crc': 0,
230:         'errors.naks': 0,
231:         'errors.sequence': 0,
232:         'errors.timeouts': 0,
233:         'packets.received': 78L,
234:         'packets.transmit': 78L}}
253:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 80L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 80L, 'errors.crc': 0}
271:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 8L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1L, 'errors.crc': 0}
273:{'radio': {'errors.crc': 0,
274:           'errors.naks': 0,
275:           'errors.sequence': 0,
276:           'errors.timeouts': 4,
```
### Traceback

```
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 4 attempts:size:0
INFO:stick:download(attempts[1],expect[0],results[0]:data[0]):DONE
Traceback (most recent call last):
  File "pump/commands.py", line 556, in <module>
    do_commands(session)
  File "pump/commands.py", line 455, in do_commands
    log.info('comm:%s:data:%s' % (comm, getattr(comm.getData( ), 'data', None)))
  File "pump/commands.py", line 447, in getData
    length = data[0]
IndexError: bytearray index out of range
Command exited with non-zero status 1
python pump/commands.py /dev/ttyUSB0 208850
	elapsed 0:10.59
	user 0.17
	system 0.07
	CPU 2% (0text+0data 61184max)k
Was there an ACK ERROR?
### DIAGNOSE CRC
```
* NO CRC ERROR FOUND
* NO NAK FOUND
* NOT A CLEAN RUN
