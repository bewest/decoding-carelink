
# ./status-quo.sh 

As [Thucydides said](http://en.wikipedia.org/wiki/Thucydides)
> Right, as the world goes, is only in question between
> equals in power, while the strong do what they can and
> the weak suffer what they must.

![Beaker learns he's getting a medical device he isn't allowed to control or understand.](https://gist.github.com/raw/4320444/0ab8e67a99b58c56cd5562cad88b3bede355a736/beaker-scream.jpg)

## status

If the stars align just right, you'll get this on your first run:
Should work on windows.

```bash
# `status-quo.sh <path> <serial>`
$ ./status-quo.sh /dev/ttyUSB0 208850
```
### good baseline :-(, I'm doing something slightly wrong in downloading

The goal is to reliably get pages out into a file.  It would help to
have a test that only does this thing, anyway, and then instrument the
thing to try many strategies.  Maybe the right download strategy will
become obvious with a tool designed to explicitly expose the problems
with a given download strategy, and given a way to exercise it many
times.

So, these tools are insufficient to answer the remaining questions:

  * if downloading is done correctly, do the radio sent/receive stats
    stay on par?

  * how do we correctly aggregate data across many reads?
    * if we encounter a CRC mismatch, how do we respond?
      * there is data left on the rf to read; failure to read it
        results in errors, radio sequence and timeouts, without some
        recovery strategy to clear the buffer
      * when greedily attempting to clear the RF buffer, eg blindly
        retrying, using only sizes from poll_size to format the
        ReadRadio packets, there is unexpected amounts of data in the
        buffer.
        * when doing this, there is a mismatch in radio receive/sent
          counters, with a slowly incrementing timeout




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
  echo -n '## commands session:finished:'
  grep -E "session:finished.*" $LOG | grep "data\[1024\]" | sort | uniq | wc -l
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
Thu Jan 10 09:41:51 PST 2013

## stick

* stick runs appear to be ok


## pump


## downloaded: 1

```
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][0]:data[1024]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][1]:data[1472]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][1]:data[768]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][2]:data[1472]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][2]:data[448]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][3]:data[1536]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][3]:data[512]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][4]:data[1536]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][4]:data[512]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][5]:data[1408]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][5]:data[384]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][6]:data[64]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][6]:data[832]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][7]:data[1408]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][7]:data[384]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][8]:data[1472]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][8]:data[704]:
```


## commands session:finished:1

```
INFO:session:finished executing:ReadBasalTemp:size[64]:data:{'duration': 0, 'rate': 1.9}
INFO:session:finished executing:ReadBatteryStatus:size[64]:data:{'status': 'normal', 'voltage': 1.36}
INFO:session:finished executing:ReadContrast:size[64]:data:bytearray(b'\x02\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:finished executing:ReadCurPageNumber:pages:8
INFO:session:finished executing:ReadFirmwareVersion:size[64]:data:'VER 2.1A1.1'
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][0]:data[1024]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][1]:data[1472]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][1]:data[768]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][2]:data[1472]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][2]:data[448]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][3]:data[1536]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][3]:data[512]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][4]:data[1536]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][4]:data[512]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][5]:data[1408]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][5]:data[384]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][6]:data[64]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][6]:data[832]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][7]:data[1408]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][7]:data[384]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][8]:data[1472]:
INFO:session:finished executing:ReadHistoryData:size[1024]:[page][8]:data[704]:
INFO:session:finished executing:ReadPumpID:size[64]:data:'208850'
INFO:session:finished executing:ReadPumpModel:size[64]:data:'515'
INFO:session:finished executing:ReadRadioCtrlACL:size[64]:data:['123456', '213546', '821650']
INFO:session:finished executing:ReadRemainingInsulin:size[64]:data:50.2
INFO:session:finished executing:ReadRTC:size[64]:data:'2006-10-10T9:6:28'
INFO:session:finished executing:ReadSettings:size[64]:data:{'low_reservoir_warn_point': 20, 'keypad_lock_status': 0, 'maxBasal': 2, 'low_reservoir_warn_type': 0, 'insulinConcentration': 100, 'audio_bolus_enable': True, 'variable_bolus_enable': False, 'alarm': {'volume': 3, 'mode': 2}, 'rf_enable': True, 'block_enable': False, 'timeformat': 0, 'auto_off_duration_hrs': 0, 'audio_bolus_size': 2.0, 'selected_pattern': 2, 'patterns_enabled': True, 'maxBolus': 10.0, 'insulin_action_type': 5}
INFO:session:finished executing:ReadTotalsToday:size[64]:data:{'yesterday': 20.5, 'today': 3.7}
```

## howdy! pump runs appear to be OK


## CRC errors found, caught, recovered: 17

```
10736:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
11532:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
12589:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
12825:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
14541:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
14745:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
16477:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
16681:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
18338:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
18673:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
20224:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
20841:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
21530:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
22433:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
22768:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
24401:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
25371:INFO:stick:XXX:IGNORE:BadCRC:returning empty message, sleep .100, avoid errors.
```

* no nak found
* SUCCESS, GOOD CLEAN RUN
