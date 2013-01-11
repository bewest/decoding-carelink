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
  echo -n '## downloaded: '
  grep -E "session:finished.*ReadHistory" $LOG | grep "data\[1024\]" | sort | uniq | wc -l
  echo ""
  echo '```'
  grep -E "session:finished executing.*ReadHistory" $LOG | sort | uniq
  echo '```'
  echo ""
  echo ""
  echo -n '## commands session:finished: '
  grep -E "session:finished executing" $LOG | grep "data\[1024\]" | sort | uniq | wc -l
  echo ""
  echo '```'
  grep -E "session:finished executing" $LOG | sort | uniq
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
Thu Jan 10 19:30:55 PST 2013

## stick

* stick runs appear to be ok


## pump


## downloaded: 0

```
```


## commands session:finished: 0

```
INFO:session:finished executing:ReadBatteryStatus:size[64]:data:{'status': 'normal', 'voltage': 1.34}
INFO:session:finished executing:ReadFirmwareVersion:size[64]:data:'VER 2.1A1.1'
INFO:session:finished executing:ReadPumpID:size[64]:data:'208850'
INFO:session:finished executing:ReadPumpModel:size[64]:data:'515'
INFO:session:finished executing:ReadRemainingInsulin:size[64]:data:36.8
INFO:session:finished executing:ReadRTC:size[64]:data:'2006-10-10T18:59:37'
```

howdy! pump runs were NOT OK

### Last send command

```
CRITICAL:stick:Stick transmit[TransmitPacket:ReadTotalsToday:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>]:download(attempts[1],expect[0],results[0]:data[0]):BAD AILING
INFO:stick:Stick transmit[TransmitPacket:ReadTotalsToday:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>]:download(attempts[1],expect[0],results[0]:data[0]):DONE
INFO:__main__:READ totals today:

```
### stats before traceback

```
214:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 3377L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 3377L, 'errors.crc': 0}
232:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 1, 'packets.transmit': 1964L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1862L, 'errors.crc': 0}
233:INFO:__main__:{'radio': {'errors.crc': 0,
234:           'errors.naks': 0,
235:           'errors.sequence': 0,
236:           'errors.timeouts': 1,
237:           'packets.received': 1862L,
238:           'packets.transmit': 1964L},
239: 'usb': {'errors.crc': 0,
240:         'errors.naks': 0,
241:         'errors.sequence': 0,
242:         'errors.timeouts': 0,
243:         'packets.received': 3377L,
244:         'packets.transmit': 3377L}}
263:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 3379L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 3379L, 'errors.crc': 0}
281:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 1, 'packets.transmit': 1964L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1862L, 'errors.crc': 0}
283:{'radio': {'errors.crc': 0,
284:           'errors.naks': 0,
285:           'errors.sequence': 0,
286:           'errors.timeouts': 1,
```
### Traceback

```
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
STATUS: receive in progress!
INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:poll zero, sleeping in POLL, .100
INFO:stick:Stick transmit[TransmitPacket:ReadTotalsToday:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>] poll_size[0] poll_i[8] command[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>]:STOP POLL after 9 attempts:size:0
CRITICAL:stick:Stick transmit[TransmitPacket:ReadTotalsToday:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>]:download(attempts[1],expect[0],results[0]:data[0]):BAD AILING
INFO:stick:Stick transmit[TransmitPacket:ReadTotalsToday:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>]:download(attempts[1],expect[0],results[0]:data[0]):DONE
INFO:__main__:READ totals today:

Traceback (most recent call last):
  File "pump/commands.py", line 606, in <module>
    do_commands(session)
  File "pump/commands.py", line 536, in do_commands
    device.execute(comm)
  File "/home/bewest/src/decoding-carelink/pump/session.py", line 100, in execute
    return super(type(self), self).execute(command)
  File "/home/bewest/src/decoding-carelink/pump/session.py", line 39, in execute
    self.download( )
  File "/home/bewest/src/decoding-carelink/pump/session.py", line 54, in download
    self.command.respond(data)
  File "pump/commands.py", line 40, in respond
    self.getData( )
  File "pump/commands.py", line 336, in getData
    'today': lib.BangInt(data[0:2]) / 10.0,
  File "/home/bewest/src/decoding-carelink/pump/lib.py", line 185, in BangInt
```
* NO CRC ERROR FOUND
* no nak found
* NOT A CLEAN RUN
