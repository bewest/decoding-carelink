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
    echo ""
  else
    _error=1
    echo 'howdy! pump runs were NOT OK'

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

  echo -n '* PAGES downloaded:'
  echo ""
  echo '```'
  grep -E "finished.*ReadHistory" $LOG | sort | uniq | wc -l
  echo '```'

  if [[ 0 -eq $(grep -E "BadCRC" $LOG | wc -l) ]] ; then
    echo "* NO CRC ERROR FOUND"
  else
    _error=1
    echo "* CRC ERROR FOUND"
    echo ""
    echo '## Diagnose CRC'
    echo ""
    echo '```'
    diagnose_crc
    echo '```'
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
Mon Jan  7 22:11:48 PST 2013
## stick
* stick runs appear to be ok
## pump
howdy! pump runs were NOT OK
### Last send command

```
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
```
### Traceback

```
0078   0xdb 0x0f 0x01 0x03 0x17 0x00 0x22 0xdb    ......".
0080   0x0f 0x01 0x03 0x18 0x00 0x00 0xdb 0x0f    ........
0088   0x01 0x04 0x07 0x00 0x00 0x00 0x02 0x21    .......!
0090   0x83 0x6c 0x21 0x83 0x05 0x0c 0x00 0xe8    .l!.....
0098   0x00 0x00 0x00 0x00 0x00 0x02 0x00 0x02    ........
00A0   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
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
stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xbe:raw:
```
### stats

```
290:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 821L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 820L, 'errors.crc': 0}
308:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 494L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 469L, 'errors.crc': 0}
309:INFO:__main__:{'radio': {'errors.crc': 0,
310:           'errors.naks': 0,
311:           'errors.sequence': 0,
312:           'errors.timeouts': 0,
313:           'packets.received': 469L,
314:           'packets.transmit': 494L},
315: 'usb': {'errors.crc': 0,
316:         'errors.naks': 1,
317:         'errors.sequence': 0,
318:         'errors.timeouts': 0,
319:         'packets.received': 820L,
320:         'packets.transmit': 821L}}
339:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 823L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 822L, 'errors.crc': 0}
357:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 494L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 469L, 'errors.crc': 0}
359:{'radio': {'errors.crc': 0,
360:           'errors.naks': 0,
361:           'errors.sequence': 0,
362:           'errors.timeouts': 0,
```
* PAGES downloaded:
```
4
```
* CRC ERROR FOUND

## Diagnose CRC

```
19:  echo "Was there an ACK ERROR?"
20:  echo "### DIAGNOSE CRC"
46:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
233:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 638L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 637L, 'errors.crc': 0}
251:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 394L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 374L, 'errors.crc': 0}
252:INFO:__main__:{'radio': {'errors.crc': 0,
253:           'errors.naks': 0,
254:           'errors.sequence': 0,
255:           'errors.timeouts': 0,
256:           'packets.received': 374L,
257:           'packets.transmit': 394L},
258: 'usb': {'errors.crc': 0,
259:         'errors.naks': 1,
260:         'errors.sequence': 0,
261:         'errors.timeouts': 0,
262:         'packets.received': 637L,
263:         'packets.transmit': 638L}}
282:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 640L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 639L, 'errors.crc': 0}
300:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 394L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 374L, 'errors.crc': 0}
302:{'radio': {'errors.crc': 0,
303:           'errors.naks': 0,
304:           'errors.sequence': 0,
305:           'errors.timeouts': 0,
306:           'packets.received': 374L,
307:           'packets.transmit': 394L},
308: 'usb': {'errors.crc': 0,
309:         'errors.naks': 1,
310:         'errors.sequence': 0,
311:         'errors.timeouts': 0,
312:         'packets.received': 639L,
313:         'packets.transmit': 640L}}
314:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
409:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
427:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 646L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 645L, 'errors.crc': 0}
445:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 394L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 374L, 'errors.crc': 0}
446:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
447:{'radio': {'errors.crc': 0,
448:           'errors.naks': 0,
449:           'errors.sequence': 0,
450:           'errors.timeouts': 0,
451:           'packets.received': 374L,
452:           'packets.transmit': 394L},
453: 'usb': {'errors.crc': 0,
454:         'errors.naks': 1,
455:         'errors.sequence': 0,
456:         'errors.timeouts': 0,
457:         'packets.received': 645L,
458:         'packets.transmit': 646L}}
478:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 648L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 647L, 'errors.crc': 0}
496:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 394L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 374L, 'errors.crc': 0}
498:{'radio': {'errors.crc': 0,
499:           'errors.naks': 0,
500:           'errors.sequence': 0,
501:           'errors.timeouts': 0,
502:           'packets.received': 374L,
503:           'packets.transmit': 394L},
504: 'usb': {'errors.crc': 0,
505:         'errors.naks': 1,
506:         'errors.sequence': 0,
507:         'errors.timeouts': 0,
508:         'packets.received': 647L,
509:         'packets.transmit': 648L}}
510:INFO:__main__:howdy! all done looking at the stick
516:INFO:__main__:howdy! I'm going to take a look at your pump.
656:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 656L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 655L, 'errors.crc': 0}
674:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 394L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 374L, 'errors.crc': 0}
675:INFO:__main__:{'radio': {'errors.crc': 0,
676:           'errors.naks': 0,
677:           'errors.sequence': 0,
678:           'errors.timeouts': 0,
679:           'packets.received': 374L,
680:           'packets.transmit': 394L},
681: 'usb': {'errors.crc': 0,
682:         'errors.naks': 1,
683:         'errors.sequence': 0,
684:         'errors.timeouts': 0,
685:         'packets.received': 655L,
686:         'packets.transmit': 656L}}
712:INFO:__main__:sleeping 17 before download
713:INFO:__main__:no download required
714:INFO:__main__:manually download PowerControl
744:INFO:stick:download_packet:15
760:WARNING:stick:bad zero CRC?
761:INFO:__main__:ENDING manual download:
780:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 661L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 660L, 'errors.crc': 0}
798:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 396L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 376L, 'errors.crc': 0}
799:INFO:__main__:{'radio': {'errors.crc': 0,
800:           'errors.naks': 0,
801:           'errors.sequence': 0,
802:           'errors.timeouts': 0,
803:           'packets.received': 376L,
804:           'packets.transmit': 396L},
805: 'usb': {'errors.crc': 0,
806:         'errors.naks': 1,
807:         'errors.sequence': 0,
808:         'errors.timeouts': 0,
809:         'packets.received': 660L,
810:         'packets.transmit': 661L}}
834:INFO:__main__:sleeping 0 before download
835:INFO:__main__:proceeding with download
884:INFO:stick:download_packet:78
925:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 667L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 666L, 'errors.crc': 0}
943:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 397L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 377L, 'errors.crc': 0}
944:INFO:__main__:{'radio': {'errors.crc': 0,
945:           'errors.naks': 0,
946:           'errors.sequence': 0,
947:           'errors.timeouts': 0,
948:           'packets.received': 377L,
949:           'packets.transmit': 397L},
950: 'usb': {'errors.crc': 0,
951:         'errors.naks': 1,
952:         'errors.sequence': 0,
953:         'errors.timeouts': 0,
954:         'packets.received': 666L,
955:         'packets.transmit': 667L}}
956:INFO:__main__:howdy! all done looking at pump
962:INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
1102:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 675L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 674L, 'errors.crc': 0}
1120:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 397L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 377L, 'errors.crc': 0}
1121:INFO:__main__:{'radio': {'errors.crc': 0,
1122:           'errors.naks': 0,
1123:           'errors.sequence': 0,
1124:           'errors.timeouts': 0,
1125:           'packets.received': 377L,
1126:           'packets.transmit': 397L},
1127: 'usb': {'errors.crc': 0,
1128:         'errors.naks': 1,
1129:         'errors.sequence': 0,
1130:         'errors.timeouts': 0,
1131:         'packets.received': 674L,
1132:         'packets.transmit': 675L}}
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
3256:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 747L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 746L, 'errors.crc': 0}
3274:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 428L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 407L, 'errors.crc': 0}
3275:INFO:__main__:{'radio': {'errors.crc': 0,
3276:           'errors.naks': 0,
3277:           'errors.sequence': 0,
3278:           'errors.timeouts': 0,
3279:           'packets.received': 407L,
3280:           'packets.transmit': 428L},
3281: 'usb': {'errors.crc': 0,
3282:         'errors.naks': 1,
3283:         'errors.sequence': 0,
3284:         'errors.timeouts': 0,
3285:         'packets.received': 746L,
3286:         'packets.transmit': 747L}}
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
5829:WARNING:stick:bad zero CRC?
5830:INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xbe:raw:
5915:    self.download( )
5916:  File "/home/bewest/src/decoding-carelink/pump/session.py", line 52, in download
5917:    data = self.stick.download( )
5918:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 555, in download
5919:    data = self.download_packet(size)
5920:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 503, in download_packet
5923:    raise BadCRC(msg)
5924:stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xbe:raw:
6009:Was there an ACK ERROR?
6010:### DIAGNOSE CRC
6011:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
6198:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 821L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 820L, 'errors.crc': 0}
6216:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 494L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 469L, 'errors.crc': 0}
6217:INFO:__main__:{'radio': {'errors.crc': 0,
6218:           'errors.naks': 0,
6219:           'errors.sequence': 0,
6220:           'errors.timeouts': 0,
6221:           'packets.received': 469L,
6222:           'packets.transmit': 494L},
6223: 'usb': {'errors.crc': 0,
6224:         'errors.naks': 1,
6225:         'errors.sequence': 0,
6226:         'errors.timeouts': 0,
6227:         'packets.received': 820L,
6228:         'packets.transmit': 821L}}
6247:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 823L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 822L, 'errors.crc': 0}
6265:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 494L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 469L, 'errors.crc': 0}
6267:{'radio': {'errors.crc': 0,
6268:           'errors.naks': 0,
6269:           'errors.sequence': 0,
6270:           'errors.timeouts': 0,
6271:           'packets.received': 469L,
6272:           'packets.transmit': 494L},
6273: 'usb': {'errors.crc': 0,
6274:         'errors.naks': 1,
6275:         'errors.sequence': 0,
6276:         'errors.timeouts': 0,
6277:         'packets.received': 822L,
6278:         'packets.transmit': 823L}}
6279:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
6305:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 398:SHOULD DOWNLOAD :True
6306:INFO:__main__:XXX:clear_buffer[attempt][0]:download the size? 398:segments[0],total_segments[0]:raw[0]
6307:INFO:__main__:XXX:clear_buffer[attempt][0] size:398:segments[0],total_segments[0]:raw[0]:clear_buffer BUFFER self.download( )
6333:INFO:__main__:download_packet:526
6437:INFO:__main__:download_packet:142
6493:INFO:__main__:download_packet:142
6524:INFO:__main__:XXX:clear_buffer[attempt][0]:tx:found:segments[1],total_segments[768]:raw[768]:len(raw):768:expected:398:len(segment):768
6525:INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 768 segment:segments[1],total_segments[768]:raw[768]:RAW:
6733:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 836L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 835L, 'errors.crc': 0}
6751:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
6753:{'radio': {'errors.crc': 0,
6754:           'errors.naks': 0,
6755:           'errors.sequence': 0,
6756:           'errors.timeouts': 0,
6757:           'packets.received': 476L,
6758:           'packets.transmit': 501L},
6759: 'usb': {'errors.crc': 0,
6760:         'errors.naks': 1,
6761:         'errors.sequence': 0,
6762:         'errors.timeouts': 0,
6763:         'packets.received': 835L,
6764:         'packets.transmit': 836L}}
6879:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 838L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 837L, 'errors.crc': 0}
6897:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
6899:{'radio': {'errors.crc': 0,
6900:           'errors.naks': 0,
6901:           'errors.sequence': 0,
6902:           'errors.timeouts': 0,
6903:           'packets.received': 476L,
6904:           'packets.transmit': 501L},
6905: 'usb': {'errors.crc': 0,
6906:         'errors.naks': 1,
6907:         'errors.sequence': 0,
6908:         'errors.timeouts': 0,
6909:         'packets.received': 837L,
6910:         'packets.transmit': 838L}}
6911:INFO:__main__:howdy! all done looking at the stick
6917:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
7104:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 848L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 847L, 'errors.crc': 0}
7122:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
7123:INFO:__main__:{'radio': {'errors.crc': 0,
7124:           'errors.naks': 0,
7125:           'errors.sequence': 0,
7126:           'errors.timeouts': 0,
7127:           'packets.received': 476L,
7128:           'packets.transmit': 501L},
7129: 'usb': {'errors.crc': 0,
7130:         'errors.naks': 1,
7131:         'errors.sequence': 0,
7132:         'errors.timeouts': 0,
7133:         'packets.received': 847L,
7134:         'packets.transmit': 848L}}
7153:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 850L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 849L, 'errors.crc': 0}
7171:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
7173:{'radio': {'errors.crc': 0,
7174:           'errors.naks': 0,
7175:           'errors.sequence': 0,
7176:           'errors.timeouts': 0,
7177:           'packets.received': 476L,
7178:           'packets.transmit': 501L},
7179: 'usb': {'errors.crc': 0,
7180:         'errors.naks': 1,
7181:         'errors.sequence': 0,
7182:         'errors.timeouts': 0,
7183:         'packets.received': 849L,
7184:         'packets.transmit': 850L}}
7185:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
7280:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
7298:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 856L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 855L, 'errors.crc': 0}
7316:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
7317:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
7318:{'radio': {'errors.crc': 0,
7319:           'errors.naks': 0,
7320:           'errors.sequence': 0,
7321:           'errors.timeouts': 0,
7322:           'packets.received': 476L,
7323:           'packets.transmit': 501L},
7324: 'usb': {'errors.crc': 0,
7325:         'errors.naks': 1,
7326:         'errors.sequence': 0,
7327:         'errors.timeouts': 0,
7328:         'packets.received': 855L,
7329:         'packets.transmit': 856L}}
7349:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 858L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 857L, 'errors.crc': 0}
7367:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
7369:{'radio': {'errors.crc': 0,
7370:           'errors.naks': 0,
7371:           'errors.sequence': 0,
7372:           'errors.timeouts': 0,
7373:           'packets.received': 476L,
7374:           'packets.transmit': 501L},
7375: 'usb': {'errors.crc': 0,
7376:         'errors.naks': 1,
7377:         'errors.sequence': 0,
7378:         'errors.timeouts': 0,
7379:         'packets.received': 857L,
7380:         'packets.transmit': 858L}}
7381:INFO:__main__:howdy! all done looking at the stick
```
* NO NAK FOUND
* NOT A CLEAN RUN
