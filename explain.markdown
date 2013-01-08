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

  grep -n --color  -E "howdy|clear_bu|NAK|CRC|ACK|IGNORE|(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" $LOG
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

    echo "### Traceback"
    echo ""
    echo '```'
    grep -B 10 -A 15 -E "Traceback" $LOG
    echo '```'

    echo "### stats"
    echo ""
    echo '```'
    grep -A 1000 -E "Traceback" $LOG | only_stats | head -n 20
    echo '```'

  fi

  echo -n '## downloaded:'
  grep -E "finished.*ReadHistory" $LOG | sort | uniq | wc -l
  echo ""
  echo '```'
  grep -E "finished.*ReadHistory" $LOG | sort | uniq
  echo '```'

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
echo '## stick'
summarize_stick
echo '## pump'
echo ""
summarize_pump

#####
# EOF
```
## cat explain.log
OUT
## Observations
Mon Jan  7 23:26:58 PST 2013
## stick

* stick runs appear to be ok

## pump


howdy! pump runs were NOT OK

### Last send command

```
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
```
### Traceback

```
0078   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x00    ........
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x07 0x00 0x00 0x00 0x00 0x1c    ........
00A0   0x80 0x6c 0x1c 0x80 0x05 0x0c 0x00 0xe8    .l......
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........

Traceback (most recent call last):
  File "pump/commands.py", line 558, in <module>
    get_pages(session)
  File "pump/commands.py", line 529, in get_pages
    device.execute(comm)
  File "/home/bewest/src/decoding-carelink/pump/session.py", line 39, in execute
    self.download( )
  File "/home/bewest/src/decoding-carelink/pump/session.py", line 52, in download
    data = self.stick.download( )
  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 555, in download
    data = self.download_packet(size)
  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 503, in download_packet
    info = self.command.parse(response)
  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 263, in parse
    raise BadCRC(msg)
stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x06:raw:
```
### stats

```
290:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 227L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 227L, 'errors.crc': 0}
308:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 136L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 129L, 'errors.crc': 0}
309:INFO:__main__:{'radio': {'errors.crc': 0,
310:           'errors.naks': 0,
311:           'errors.sequence': 0,
312:           'errors.timeouts': 0,
313:           'packets.received': 129L,
314:           'packets.transmit': 136L},
315: 'usb': {'errors.crc': 0,
316:         'errors.naks': 0,
317:         'errors.sequence': 0,
318:         'errors.timeouts': 0,
319:         'packets.received': 227L,
320:         'packets.transmit': 227L}}
339:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 229L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 229L, 'errors.crc': 0}
357:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 136L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 129L, 'errors.crc': 0}
359:{'radio': {'errors.crc': 0,
360:           'errors.naks': 0,
361:           'errors.sequence': 0,
362:           'errors.timeouts': 0,
```
## downloaded:6

```
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xd1\x80@\xa7\x01 \x88P\xb7\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][1], bytearray(b'\x00\xd1\x80\x80\xa7\x01 \x88P\xf2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][2], bytearray(b'\x00\xd1\x80\x80\xa7\x01 \x88P\xf2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x92\x9e\x0b\x01\x06\x07\x00\x00\x02L\xa1\x06l\xa1\x06\x05\x0c\x00\xe8\x00\x00\x00\x00\x02L\x02Ld\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][3], bytearray(b'\x00\xd1\x80\x80\xa7\x01 \x88P\xf2\x04\xda\x82\x0cl\x82\x0c\x05\x00edf\x12\x00\x00\x04\xda\x03\x9eK\x01<\x19\x00O\x01<\x19\x01<d\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x00d\x01V\xca\x06\x01\x06\x17\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][4], bytearray(b'\x00\xd1\x80\x80\xa7\x01 \x88P\xf2\x01\x12\x17\x00\x9f\x08\x14\x01\x12\x18\x00\x80\x08\x14\x01\x0c\x07\x00\x00\x00\x06\x81\x12l\x81\x12\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x06\x00\x06d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][5], bytearray(b'\x00\xd1\x80\x80\xa7\x01 \x88P\xf2\x00\x02\x00!\x00l!\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x02\x00\x02\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x0c\x9c\x13\x02\x00\x17')
```

## Diagnose CRC

```
19:  echo "Was there an ACK ERROR?"
20:  echo "### DIAGNOSE CRC"
46:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
233:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 8L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 8L, 'errors.crc': 0}
251:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
252:INFO:__main__:{'radio': {'errors.crc': 0,
253:           'errors.naks': 0,
254:           'errors.sequence': 0,
255:           'errors.timeouts': 0,
256:           'packets.received': 0L,
257:           'packets.transmit': 0L},
258: 'usb': {'errors.crc': 0,
259:         'errors.naks': 0,
260:         'errors.sequence': 0,
261:         'errors.timeouts': 0,
262:         'packets.received': 8L,
263:         'packets.transmit': 8L}}
282:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 10L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 10L, 'errors.crc': 0}
300:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
302:{'radio': {'errors.crc': 0,
303:           'errors.naks': 0,
304:           'errors.sequence': 0,
305:           'errors.timeouts': 0,
306:           'packets.received': 0L,
307:           'packets.transmit': 0L},
308: 'usb': {'errors.crc': 0,
309:         'errors.naks': 0,
310:         'errors.sequence': 0,
311:         'errors.timeouts': 0,
312:         'packets.received': 10L,
313:         'packets.transmit': 10L}}
314:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
409:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
427:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 16L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 16L, 'errors.crc': 0}
445:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
446:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
447:{'radio': {'errors.crc': 0,
448:           'errors.naks': 0,
449:           'errors.sequence': 0,
450:           'errors.timeouts': 0,
451:           'packets.received': 0L,
452:           'packets.transmit': 0L},
453: 'usb': {'errors.crc': 0,
454:         'errors.naks': 0,
455:         'errors.sequence': 0,
456:         'errors.timeouts': 0,
457:         'packets.received': 16L,
458:         'packets.transmit': 16L}}
478:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 18L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 18L, 'errors.crc': 0}
496:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
498:{'radio': {'errors.crc': 0,
499:           'errors.naks': 0,
500:           'errors.sequence': 0,
501:           'errors.timeouts': 0,
502:           'packets.received': 0L,
503:           'packets.transmit': 0L},
504: 'usb': {'errors.crc': 0,
505:         'errors.naks': 0,
506:         'errors.sequence': 0,
507:         'errors.timeouts': 0,
508:         'packets.received': 18L,
509:         'packets.transmit': 18L}}
510:INFO:__main__:howdy! all done looking at the stick
516:INFO:__main__:howdy! I'm going to take a look at your pump.
656:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 26L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 26L, 'errors.crc': 0}
674:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
675:INFO:__main__:{'radio': {'errors.crc': 0,
676:           'errors.naks': 0,
677:           'errors.sequence': 0,
678:           'errors.timeouts': 0,
679:           'packets.received': 0L,
680:           'packets.transmit': 0L},
681: 'usb': {'errors.crc': 0,
682:         'errors.naks': 0,
683:         'errors.sequence': 0,
684:         'errors.timeouts': 0,
685:         'packets.received': 26L,
686:         'packets.transmit': 26L}}
712:INFO:__main__:sleeping 17 before download
713:INFO:__main__:no download required
714:INFO:__main__:manually download PowerControl
744:INFO:stick:download_packet:15
760:WARNING:stick:bad zero CRC?
761:INFO:__main__:ENDING manual download:
780:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 31L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 31L, 'errors.crc': 0}
798:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 2L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2L, 'errors.crc': 0}
799:INFO:__main__:{'radio': {'errors.crc': 0,
800:           'errors.naks': 0,
801:           'errors.sequence': 0,
802:           'errors.timeouts': 0,
803:           'packets.received': 2L,
804:           'packets.transmit': 2L},
805: 'usb': {'errors.crc': 0,
806:         'errors.naks': 0,
807:         'errors.sequence': 0,
808:         'errors.timeouts': 0,
809:         'packets.received': 31L,
810:         'packets.transmit': 31L}}
834:INFO:__main__:sleeping 0 before download
835:INFO:__main__:proceeding with download
884:INFO:stick:download_packet:78
925:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 37L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 37L, 'errors.crc': 0}
943:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 3L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 3L, 'errors.crc': 0}
944:INFO:__main__:{'radio': {'errors.crc': 0,
945:           'errors.naks': 0,
946:           'errors.sequence': 0,
947:           'errors.timeouts': 0,
948:           'packets.received': 3L,
949:           'packets.transmit': 3L},
950: 'usb': {'errors.crc': 0,
951:         'errors.naks': 0,
952:         'errors.sequence': 0,
953:         'errors.timeouts': 0,
954:         'packets.received': 37L,
955:         'packets.transmit': 37L}}
956:INFO:__main__:howdy! all done looking at pump
962:INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
1102:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 45L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 45L, 'errors.crc': 0}
1120:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 3L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 3L, 'errors.crc': 0}
1121:INFO:__main__:{'radio': {'errors.crc': 0,
1122:           'errors.naks': 0,
1123:           'errors.sequence': 0,
1124:           'errors.timeouts': 0,
1125:           'packets.received': 3L,
1126:           'packets.transmit': 3L},
1127: 'usb': {'errors.crc': 0,
1128:         'errors.naks': 0,
1129:         'errors.sequence': 0,
1130:         'errors.timeouts': 0,
1131:         'packets.received': 45L,
1132:         'packets.transmit': 45L}}
1156:INFO:session:sleeping 0 before download
1157:INFO:session:proceeding with download
1206:INFO:stick:download_packet:78
1253:INFO:session:sleeping 0 before download
1254:INFO:session:proceeding with download
1303:INFO:stick:download_packet:78
1352:INFO:session:sleeping 0 before download
1353:INFO:session:proceeding with download
1402:INFO:stick:download_packet:78
1450:INFO:session:sleeping 0 before download
1451:INFO:session:proceeding with download
1500:INFO:stick:download_packet:78
1548:INFO:session:sleeping 0 before download
1549:INFO:session:proceeding with download
1598:INFO:stick:download_packet:78
1646:INFO:session:sleeping 0 before download
1647:INFO:session:proceeding with download
1696:INFO:stick:download_packet:78
1753:INFO:session:sleeping 0 before download
1754:INFO:session:proceeding with download
1803:INFO:stick:download_packet:78
1860:INFO:session:sleeping 0 before download
1861:INFO:session:proceeding with download
1910:INFO:stick:download_packet:78
1967:INFO:session:sleeping 0 before download
1968:INFO:session:proceeding with download
2017:INFO:stick:download_packet:78
2074:INFO:session:sleeping 0 before download
2075:INFO:session:proceeding with download
2124:INFO:stick:download_packet:78
2181:INFO:session:sleeping 0 before download
2182:INFO:session:proceeding with download
2231:INFO:stick:download_packet:78
2288:INFO:session:sleeping 0 before download
2289:INFO:session:proceeding with download
2338:INFO:stick:download_packet:78
2395:INFO:session:sleeping 0 before download
2396:INFO:session:proceeding with download
2445:INFO:stick:download_packet:78
2503:INFO:session:sleeping 0.1 before download
2504:INFO:session:proceeding with download
2553:INFO:stick:download_packet:78
2601:INFO:stick:download_packet:206
2665:INFO:stick:download_packet:142
2696:WARNING:stick:bad zero CRC?
2722:INFO:stick:download_packet:142
2753:WARNING:stick:bad zero CRC?
2779:INFO:stick:download_packet:142
2810:WARNING:stick:bad zero CRC?
2836:INFO:stick:download_packet:142
2867:WARNING:stick:bad zero CRC?
2893:INFO:stick:download_packet:142
2924:WARNING:stick:bad zero CRC?
2950:INFO:stick:download_packet:142
3256:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 117L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 117L, 'errors.crc': 0}
3274:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 34L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 33L, 'errors.crc': 0}
3275:INFO:__main__:{'radio': {'errors.crc': 0,
3276:           'errors.naks': 0,
3277:           'errors.sequence': 0,
3278:           'errors.timeouts': 0,
3279:           'packets.received': 33L,
3280:           'packets.transmit': 34L},
3281: 'usb': {'errors.crc': 0,
3282:         'errors.naks': 0,
3283:         'errors.sequence': 0,
3284:         'errors.timeouts': 0,
3285:         'packets.received': 117L,
3286:         'packets.transmit': 117L}}
3311:INFO:session:sleeping 0 before download
3312:INFO:session:proceeding with download
3361:INFO:stick:download_packet:78
3419:INFO:session:sleeping 0.1 before download
3420:INFO:session:proceeding with download
3469:INFO:stick:download_packet:78
3517:INFO:stick:download_packet:206
3581:INFO:stick:download_packet:142
3612:WARNING:stick:bad zero CRC?
3638:INFO:stick:download_packet:142
3669:WARNING:stick:bad zero CRC?
3695:INFO:stick:download_packet:142
3726:WARNING:stick:bad zero CRC?
3752:INFO:stick:download_packet:142
3783:WARNING:stick:bad zero CRC?
3809:INFO:stick:download_packet:142
3840:WARNING:stick:bad zero CRC?
3866:INFO:stick:download_packet:142
4180:INFO:session:sleeping 0.1 before download
4181:INFO:session:proceeding with download
4230:INFO:stick:download_packet:78
4278:INFO:stick:download_packet:206
4342:INFO:stick:download_packet:142
4398:INFO:stick:download_packet:142
4454:INFO:stick:download_packet:142
4510:INFO:stick:download_packet:142
4566:INFO:stick:download_packet:142
4622:INFO:stick:download_packet:142
4936:INFO:session:sleeping 0.1 before download
4937:INFO:session:proceeding with download
4986:INFO:stick:download_packet:78
5034:INFO:stick:download_packet:206
5098:INFO:stick:download_packet:142
5154:INFO:stick:download_packet:142
5210:INFO:stick:download_packet:142
5266:INFO:stick:download_packet:142
5322:INFO:stick:download_packet:142
5378:INFO:stick:download_packet:142
5692:INFO:session:sleeping 0.1 before download
5693:INFO:session:proceeding with download
5742:INFO:stick:download_packet:78
5790:INFO:stick:download_packet:206
5854:INFO:stick:download_packet:142
5910:INFO:stick:download_packet:142
5966:INFO:stick:download_packet:142
6022:INFO:stick:download_packet:142
6078:INFO:stick:download_packet:142
6134:INFO:stick:download_packet:142
6448:INFO:session:sleeping 0.1 before download
6449:INFO:session:proceeding with download
6498:INFO:stick:download_packet:78
6546:INFO:stick:download_packet:206
6610:INFO:stick:download_packet:142
6666:INFO:stick:download_packet:142
6722:INFO:stick:download_packet:142
6778:INFO:stick:download_packet:142
6834:INFO:stick:download_packet:142
6890:INFO:stick:download_packet:142
7204:INFO:session:sleeping 0.1 before download
7205:INFO:session:proceeding with download
7254:INFO:stick:download_packet:78
7302:INFO:stick:download_packet:206
7341:WARNING:stick:bad zero CRC?
7342:INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x06:raw:
7427:    self.download( )
7428:  File "/home/bewest/src/decoding-carelink/pump/session.py", line 52, in download
7429:    data = self.stick.download( )
7430:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 555, in download
7431:    data = self.download_packet(size)
7432:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 503, in download_packet
7435:    raise BadCRC(msg)
7436:stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x06:raw:
7521:Was there an ACK ERROR?
7522:### DIAGNOSE CRC
7523:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
7710:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 227L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 227L, 'errors.crc': 0}
7728:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 136L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 129L, 'errors.crc': 0}
7729:INFO:__main__:{'radio': {'errors.crc': 0,
7730:           'errors.naks': 0,
7731:           'errors.sequence': 0,
7732:           'errors.timeouts': 0,
7733:           'packets.received': 129L,
7734:           'packets.transmit': 136L},
7735: 'usb': {'errors.crc': 0,
7736:         'errors.naks': 0,
7737:         'errors.sequence': 0,
7738:         'errors.timeouts': 0,
7739:         'packets.received': 227L,
7740:         'packets.transmit': 227L}}
7759:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 229L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 229L, 'errors.crc': 0}
7777:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 136L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 129L, 'errors.crc': 0}
7779:{'radio': {'errors.crc': 0,
7780:           'errors.naks': 0,
7781:           'errors.sequence': 0,
7782:           'errors.timeouts': 0,
7783:           'packets.received': 129L,
7784:           'packets.transmit': 136L},
7785: 'usb': {'errors.crc': 0,
7786:         'errors.naks': 0,
7787:         'errors.sequence': 0,
7788:         'errors.timeouts': 0,
7789:         'packets.received': 229L,
7790:         'packets.transmit': 229L}}
7791:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
7817:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 334:SHOULD DOWNLOAD :True
7818:INFO:__main__:XXX:clear_buffer[attempt][0]:download the size? 334:segments[0],total_segments[0]:raw[0]
7819:INFO:__main__:XXX:clear_buffer[attempt][0] size:334:segments[0],total_segments[0]:raw[0]:clear_buffer BUFFER self.download( )
7845:INFO:__main__:download_packet:462
7916:WARNING:__main__:bad zero CRC?
7917:INFO:__main__:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xe6:raw:
8092:CRITICAL:__main__:XXX:clear_buffer[attempt][0]:IGNORING:segments[0],total_segments[0]:raw[0]:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xe6:raw:
8267:INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 0 segment:segments[0],total_segments[0]:raw[0]:RAW:
8294:INFO:__main__:XXX:clear_buffer[attempt][0] size:142:segments[0],total_segments[0]:raw[0]:clear_buffer BUFFER self.download( )
8320:INFO:__main__:download_packet:270
8392:INFO:__main__:download_packet:78
8415:INFO:__main__:XXX:clear_buffer[attempt][0]:tx:found:segments[1],total_segments[320]:raw[320]:len(raw):320:expected:142:len(segment):320
8416:INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 320 segment:segments[1],total_segments[320]:raw[320]:RAW:
8568:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 243L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 243L, 'errors.crc': 0}
8586:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 143L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 136L, 'errors.crc': 0}
8588:{'radio': {'errors.crc': 0,
8589:           'errors.naks': 0,
8590:           'errors.sequence': 0,
8591:           'errors.timeouts': 0,
8592:           'packets.received': 136L,
8593:           'packets.transmit': 143L},
8594: 'usb': {'errors.crc': 0,
8595:         'errors.naks': 0,
8596:         'errors.sequence': 0,
8597:         'errors.timeouts': 0,
8598:         'packets.received': 243L,
8599:         'packets.transmit': 243L}}
8658:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 245L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 245L, 'errors.crc': 0}
8676:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 143L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 136L, 'errors.crc': 0}
8678:{'radio': {'errors.crc': 0,
8679:           'errors.naks': 0,
8680:           'errors.sequence': 0,
8681:           'errors.timeouts': 0,
8682:           'packets.received': 136L,
8683:           'packets.transmit': 143L},
8684: 'usb': {'errors.crc': 0,
8685:         'errors.naks': 0,
8686:         'errors.sequence': 0,
8687:         'errors.timeouts': 0,
8688:         'packets.received': 245L,
8689:         'packets.transmit': 245L}}
8690:INFO:__main__:howdy! all done looking at the stick
8696:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
8883:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 255L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 255L, 'errors.crc': 0}
8901:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 143L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 136L, 'errors.crc': 0}
8902:INFO:__main__:{'radio': {'errors.crc': 0,
8903:           'errors.naks': 0,
8904:           'errors.sequence': 0,
8905:           'errors.timeouts': 0,
8906:           'packets.received': 136L,
8907:           'packets.transmit': 143L},
8908: 'usb': {'errors.crc': 0,
8909:         'errors.naks': 0,
8910:         'errors.sequence': 0,
8911:         'errors.timeouts': 0,
8912:         'packets.received': 255L,
8913:         'packets.transmit': 255L}}
8932:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 257L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 257L, 'errors.crc': 0}
8950:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 143L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 136L, 'errors.crc': 0}
8952:{'radio': {'errors.crc': 0,
8953:           'errors.naks': 0,
8954:           'errors.sequence': 0,
8955:           'errors.timeouts': 0,
8956:           'packets.received': 136L,
8957:           'packets.transmit': 143L},
8958: 'usb': {'errors.crc': 0,
8959:         'errors.naks': 0,
8960:         'errors.sequence': 0,
8961:         'errors.timeouts': 0,
8962:         'packets.received': 257L,
8963:         'packets.transmit': 257L}}
8964:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
9059:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
9077:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 263L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 263L, 'errors.crc': 0}
9095:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 143L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 136L, 'errors.crc': 0}
9096:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
9097:{'radio': {'errors.crc': 0,
9098:           'errors.naks': 0,
9099:           'errors.sequence': 0,
9100:           'errors.timeouts': 0,
9101:           'packets.received': 136L,
9102:           'packets.transmit': 143L},
9103: 'usb': {'errors.crc': 0,
9104:         'errors.naks': 0,
9105:         'errors.sequence': 0,
9106:         'errors.timeouts': 0,
9107:         'packets.received': 263L,
9108:         'packets.transmit': 263L}}
9128:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 265L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 265L, 'errors.crc': 0}
9146:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 143L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 136L, 'errors.crc': 0}
9148:{'radio': {'errors.crc': 0,
9149:           'errors.naks': 0,
9150:           'errors.sequence': 0,
9151:           'errors.timeouts': 0,
9152:           'packets.received': 136L,
9153:           'packets.transmit': 143L},
9154: 'usb': {'errors.crc': 0,
9155:         'errors.naks': 0,
9156:         'errors.sequence': 0,
9157:         'errors.timeouts': 0,
9158:         'packets.received': 265L,
9159:         'packets.transmit': 265L}}
9160:INFO:__main__:howdy! all done looking at the stick
```

* NO NAK FOUND
* NOT A CLEAN RUN
