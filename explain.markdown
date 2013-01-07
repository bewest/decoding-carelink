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
  echo '```'
  grep -E "finished.*ReadHistory" $LOG | sort | uniq | wc -l
  echo '```'

  if [[ 0 -eq $(grep -E "BadCRC" $LOG | wc -l) ]] ; then
    echo "* NO CRC ERROR FOUND"
  else
    _error=1
    echo "* CRC ERROR FOUND"
    echo '## Diagnose CRC'
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
Mon Jan  7 14:44:42 PST 2013
## stick
* stick runs appear to be ok
## pump
howdy! pump runs were NOT OK
### Last send command
```
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
```
### Traceback
```
0078   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
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
stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xd0:raw:
```
### stats
```
290:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 919L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 917L, 'errors.crc': 0}
308:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 473L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 446L, 'errors.crc': 0}
309:INFO:__main__:{'radio': {'errors.crc': 0,
310:           'errors.naks': 0,
311:           'errors.sequence': 2,
312:           'errors.timeouts': 4,
313:           'packets.received': 446L,
314:           'packets.transmit': 473L},
315: 'usb': {'errors.crc': 0,
316:         'errors.naks': 2,
317:         'errors.sequence': 0,
318:         'errors.timeouts': 0,
319:         'packets.received': 917L,
320:         'packets.transmit': 919L}}
339:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 921L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 919L, 'errors.crc': 0}
357:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 474L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 447L, 'errors.crc': 0}
359:{'radio': {'errors.crc': 0,
360:           'errors.naks': 0,
361:           'errors.sequence': 2,
362:           'errors.timeouts': 4,
```
* PAGES downloaded:```
1
```
* CRC ERROR FOUND
## Diagnose CRC
```
19:  echo "Was there an ACK ERROR?"
20:  echo "### DIAGNOSE CRC"
46:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
233:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 787L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 785L, 'errors.crc': 0}
251:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 427L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 403L, 'errors.crc': 0}
252:INFO:__main__:{'radio': {'errors.crc': 0,
253:           'errors.naks': 0,
254:           'errors.sequence': 2,
255:           'errors.timeouts': 3,
256:           'packets.received': 403L,
257:           'packets.transmit': 427L},
258: 'usb': {'errors.crc': 0,
259:         'errors.naks': 2,
260:         'errors.sequence': 0,
261:         'errors.timeouts': 0,
262:         'packets.received': 785L,
263:         'packets.transmit': 787L}}
282:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 789L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 787L, 'errors.crc': 0}
300:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 427L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 403L, 'errors.crc': 0}
302:{'radio': {'errors.crc': 0,
303:           'errors.naks': 0,
304:           'errors.sequence': 2,
305:           'errors.timeouts': 3,
306:           'packets.received': 403L,
307:           'packets.transmit': 427L},
308: 'usb': {'errors.crc': 0,
309:         'errors.naks': 2,
310:         'errors.sequence': 0,
311:         'errors.timeouts': 0,
312:         'packets.received': 787L,
313:         'packets.transmit': 789L}}
314:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
409:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
427:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 795L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 793L, 'errors.crc': 0}
445:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 427L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 403L, 'errors.crc': 0}
446:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
447:{'radio': {'errors.crc': 0,
448:           'errors.naks': 0,
449:           'errors.sequence': 2,
450:           'errors.timeouts': 3,
451:           'packets.received': 403L,
452:           'packets.transmit': 427L},
453: 'usb': {'errors.crc': 0,
454:         'errors.naks': 2,
455:         'errors.sequence': 0,
456:         'errors.timeouts': 0,
457:         'packets.received': 793L,
458:         'packets.transmit': 795L}}
478:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 797L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 795L, 'errors.crc': 0}
496:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 427L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 403L, 'errors.crc': 0}
498:{'radio': {'errors.crc': 0,
499:           'errors.naks': 0,
500:           'errors.sequence': 2,
501:           'errors.timeouts': 3,
502:           'packets.received': 403L,
503:           'packets.transmit': 427L},
504: 'usb': {'errors.crc': 0,
505:         'errors.naks': 2,
506:         'errors.sequence': 0,
507:         'errors.timeouts': 0,
508:         'packets.received': 795L,
509:         'packets.transmit': 797L}}
510:INFO:__main__:howdy! all done looking at the stick
516:INFO:__main__:howdy! I'm going to take a look at your pump.
656:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 805L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 803L, 'errors.crc': 0}
674:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 427L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 403L, 'errors.crc': 0}
675:INFO:__main__:{'radio': {'errors.crc': 0,
676:           'errors.naks': 0,
677:           'errors.sequence': 2,
678:           'errors.timeouts': 3,
679:           'packets.received': 403L,
680:           'packets.transmit': 427L},
681: 'usb': {'errors.crc': 0,
682:         'errors.naks': 2,
683:         'errors.sequence': 0,
684:         'errors.timeouts': 0,
685:         'packets.received': 803L,
686:         'packets.transmit': 805L}}
712:INFO:__main__:sleeping 17 before download
713:INFO:__main__:no download required
714:INFO:__main__:manually download PowerControl
744:INFO:stick:download_packet:15
760:WARNING:stick:bad zero CRC?
761:INFO:__main__:ENDING manual download:
780:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 810L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 808L, 'errors.crc': 0}
798:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 429L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 405L, 'errors.crc': 0}
799:INFO:__main__:{'radio': {'errors.crc': 0,
800:           'errors.naks': 0,
801:           'errors.sequence': 2,
802:           'errors.timeouts': 3,
803:           'packets.received': 405L,
804:           'packets.transmit': 429L},
805: 'usb': {'errors.crc': 0,
806:         'errors.naks': 2,
807:         'errors.sequence': 0,
808:         'errors.timeouts': 0,
809:         'packets.received': 808L,
810:         'packets.transmit': 810L}}
834:INFO:__main__:sleeping 0 before download
835:INFO:__main__:proceeding with download
884:INFO:stick:download_packet:78
925:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 816L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 814L, 'errors.crc': 0}
943:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 430L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 406L, 'errors.crc': 0}
944:INFO:__main__:{'radio': {'errors.crc': 0,
945:           'errors.naks': 0,
946:           'errors.sequence': 2,
947:           'errors.timeouts': 3,
948:           'packets.received': 406L,
949:           'packets.transmit': 430L},
950: 'usb': {'errors.crc': 0,
951:         'errors.naks': 2,
952:         'errors.sequence': 0,
953:         'errors.timeouts': 0,
954:         'packets.received': 814L,
955:         'packets.transmit': 816L}}
956:INFO:__main__:howdy! all done looking at pump
962:INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
1102:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 824L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 822L, 'errors.crc': 0}
1120:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 430L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 406L, 'errors.crc': 0}
1121:INFO:__main__:{'radio': {'errors.crc': 0,
1122:           'errors.naks': 0,
1123:           'errors.sequence': 2,
1124:           'errors.timeouts': 3,
1125:           'packets.received': 406L,
1126:           'packets.transmit': 430L},
1127: 'usb': {'errors.crc': 0,
1128:         'errors.naks': 2,
1129:         'errors.sequence': 0,
1130:         'errors.timeouts': 0,
1131:         'packets.received': 822L,
1132:         'packets.transmit': 824L}}
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
1956:INFO:stick:download found empty poll size, sleep 3 and try again
1982:INFO:stick:download_packet:78
2039:INFO:session:sleeping 0 before download
2040:INFO:session:proceeding with download
2089:INFO:stick:download_packet:78
2146:INFO:session:sleeping 0 before download
2147:INFO:session:proceeding with download
2196:INFO:stick:download_packet:78
2253:INFO:session:sleeping 0 before download
2254:INFO:session:proceeding with download
2303:INFO:stick:download_packet:78
2360:INFO:session:sleeping 0 before download
2361:INFO:session:proceeding with download
2410:INFO:stick:download_packet:78
2467:INFO:session:sleeping 0 before download
2468:INFO:session:proceeding with download
2517:INFO:stick:download_packet:78
2575:INFO:session:sleeping 0.1 before download
2576:INFO:session:proceeding with download
2625:INFO:stick:download_packet:78
2673:INFO:stick:download_packet:206
2737:INFO:stick:download_packet:142
2768:WARNING:stick:bad zero CRC?
2794:INFO:stick:download_packet:142
2825:WARNING:stick:bad zero CRC?
2851:INFO:stick:download_packet:142
2882:WARNING:stick:bad zero CRC?
2908:INFO:stick:download_packet:142
2939:WARNING:stick:bad zero CRC?
2965:INFO:stick:download_packet:142
2996:WARNING:stick:bad zero CRC?
3022:INFO:stick:download_packet:142
3328:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 899L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 897L, 'errors.crc': 0}
3346:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 462L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 436L, 'errors.crc': 0}
3347:INFO:__main__:{'radio': {'errors.crc': 0,
3348:           'errors.naks': 0,
3349:           'errors.sequence': 2,
3350:           'errors.timeouts': 4,
3351:           'packets.received': 436L,
3352:           'packets.transmit': 462L},
3353: 'usb': {'errors.crc': 0,
3354:         'errors.naks': 2,
3355:         'errors.sequence': 0,
3356:         'errors.timeouts': 0,
3357:         'packets.received': 897L,
3358:         'packets.transmit': 899L}}
3383:INFO:session:sleeping 0 before download
3384:INFO:session:proceeding with download
3433:INFO:stick:download_packet:78
3491:INFO:session:sleeping 0.1 before download
3492:INFO:session:proceeding with download
3541:INFO:stick:download_packet:78
3589:INFO:stick:download_packet:206
3628:WARNING:stick:bad zero CRC?
3629:INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xd0:raw:
3714:    self.download( )
3715:  File "/home/bewest/src/decoding-carelink/pump/session.py", line 52, in download
3716:    data = self.stick.download( )
3717:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 555, in download
3718:    data = self.download_packet(size)
3719:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 503, in download_packet
3722:    raise BadCRC(msg)
3723:stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xd0:raw:
3808:Was there an ACK ERROR?
3809:### DIAGNOSE CRC
3810:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
3997:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 919L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 917L, 'errors.crc': 0}
4015:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 473L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 446L, 'errors.crc': 0}
4016:INFO:__main__:{'radio': {'errors.crc': 0,
4017:           'errors.naks': 0,
4018:           'errors.sequence': 2,
4019:           'errors.timeouts': 4,
4020:           'packets.received': 446L,
4021:           'packets.transmit': 473L},
4022: 'usb': {'errors.crc': 0,
4023:         'errors.naks': 2,
4024:         'errors.sequence': 0,
4025:         'errors.timeouts': 0,
4026:         'packets.received': 917L,
4027:         'packets.transmit': 919L}}
4046:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 921L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 919L, 'errors.crc': 0}
4064:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 474L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 447L, 'errors.crc': 0}
4066:{'radio': {'errors.crc': 0,
4067:           'errors.naks': 0,
4068:           'errors.sequence': 2,
4069:           'errors.timeouts': 4,
4070:           'packets.received': 447L,
4071:           'packets.transmit': 474L},
4072: 'usb': {'errors.crc': 0,
4073:         'errors.naks': 2,
4074:         'errors.sequence': 0,
4075:         'errors.timeouts': 0,
4076:         'packets.received': 919L,
4077:         'packets.transmit': 921L}}
4078:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
4104:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 334:SHOULD DOWNLOAD :True
4105:INFO:__main__:XXX:clear_buffer[attempt][0]:download the size? 334:segments[0],total_segments[0]:raw[0]
4106:INFO:__main__:XXX:clear_buffer[attempt][0] size:334:segments[0],total_segments[0]:raw[0]:clear_buffer BUFFER self.download( )
4132:INFO:__main__:download_packet:462
4203:WARNING:__main__:bad zero CRC?
4229:INFO:__main__:download_packet:142
4260:WARNING:__main__:bad zero CRC?
4286:INFO:__main__:download_packet:142
4317:WARNING:__main__:bad zero CRC?
4343:INFO:__main__:download_packet:78
4366:INFO:__main__:XXX:clear_buffer[attempt][0]:tx:found:segments[1],total_segments[768]:raw[768]:len(raw):768:expected:334:len(segment):768
4367:INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 768 segment:segments[1],total_segments[768]:raw[768]:RAW:
4575:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 936L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 934L, 'errors.crc': 0}
4593:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 481L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 454L, 'errors.crc': 0}
4595:{'radio': {'errors.crc': 0,
4596:           'errors.naks': 0,
4597:           'errors.sequence': 2,
4598:           'errors.timeouts': 4,
4599:           'packets.received': 454L,
4600:           'packets.transmit': 481L},
4601: 'usb': {'errors.crc': 0,
4602:         'errors.naks': 2,
4603:         'errors.sequence': 0,
4604:         'errors.timeouts': 0,
4605:         'packets.received': 934L,
4606:         'packets.transmit': 936L}}
4721:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 938L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 936L, 'errors.crc': 0}
4739:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 481L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 454L, 'errors.crc': 0}
4741:{'radio': {'errors.crc': 0,
4742:           'errors.naks': 0,
4743:           'errors.sequence': 2,
4744:           'errors.timeouts': 4,
4745:           'packets.received': 454L,
4746:           'packets.transmit': 481L},
4747: 'usb': {'errors.crc': 0,
4748:         'errors.naks': 2,
4749:         'errors.sequence': 0,
4750:         'errors.timeouts': 0,
4751:         'packets.received': 936L,
4752:         'packets.transmit': 938L}}
4753:INFO:__main__:howdy! all done looking at the stick
4759:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
4946:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 948L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 946L, 'errors.crc': 0}
4964:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 481L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 454L, 'errors.crc': 0}
4965:INFO:__main__:{'radio': {'errors.crc': 0,
4966:           'errors.naks': 0,
4967:           'errors.sequence': 2,
4968:           'errors.timeouts': 4,
4969:           'packets.received': 454L,
4970:           'packets.transmit': 481L},
4971: 'usb': {'errors.crc': 0,
4972:         'errors.naks': 2,
4973:         'errors.sequence': 0,
4974:         'errors.timeouts': 0,
4975:         'packets.received': 946L,
4976:         'packets.transmit': 948L}}
4995:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 950L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 948L, 'errors.crc': 0}
5013:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 481L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 454L, 'errors.crc': 0}
5015:{'radio': {'errors.crc': 0,
5016:           'errors.naks': 0,
5017:           'errors.sequence': 2,
5018:           'errors.timeouts': 4,
5019:           'packets.received': 454L,
5020:           'packets.transmit': 481L},
5021: 'usb': {'errors.crc': 0,
5022:         'errors.naks': 2,
5023:         'errors.sequence': 0,
5024:         'errors.timeouts': 0,
5025:         'packets.received': 948L,
5026:         'packets.transmit': 950L}}
5027:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
5122:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
5140:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 956L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 954L, 'errors.crc': 0}
5158:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 481L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 454L, 'errors.crc': 0}
5159:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
5160:{'radio': {'errors.crc': 0,
5161:           'errors.naks': 0,
5162:           'errors.sequence': 2,
5163:           'errors.timeouts': 4,
5164:           'packets.received': 454L,
5165:           'packets.transmit': 481L},
5166: 'usb': {'errors.crc': 0,
5167:         'errors.naks': 2,
5168:         'errors.sequence': 0,
5169:         'errors.timeouts': 0,
5170:         'packets.received': 954L,
5171:         'packets.transmit': 956L}}
5191:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 958L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 956L, 'errors.crc': 0}
5209:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 4, 'packets.transmit': 481L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 454L, 'errors.crc': 0}
5211:{'radio': {'errors.crc': 0,
5212:           'errors.naks': 0,
5213:           'errors.sequence': 2,
5214:           'errors.timeouts': 4,
5215:           'packets.received': 454L,
5216:           'packets.transmit': 481L},
5217: 'usb': {'errors.crc': 0,
5218:         'errors.naks': 2,
5219:         'errors.sequence': 0,
5220:         'errors.timeouts': 0,
5221:         'packets.received': 956L,
5222:         'packets.transmit': 958L}}
5223:INFO:__main__:howdy! all done looking at the stick
```
* NO NAK FOUND
* NOT A CLEAN RUN
