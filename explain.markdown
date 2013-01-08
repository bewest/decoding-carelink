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
Mon Jan  7 22:18:38 PST 2013
## stick
* not ok
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
--
INFO:root:usb.read.raw:
0000   0x01 0x66 0x03 0x0b 0x2c 0x00 0x00 0x00    .f..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
Traceback (most recent call last):
  File "pump/stick.py", line 661, in <module>
    signal = stick.signal_strength( )
  File "pump/stick.py", line 410, in signal_strength
    return self.query(SignalStrength)
  File "pump/stick.py", line 395, in query
    return self.process( )
  File "pump/stick.py", line 388, in process
    ack, response = self.command.respond(raw)
  File "pump/stick.py", line 51, in respond
    assert False, ("NAK!!\n%s" % lib.hexdump(raw[:3]))
AssertionError: NAK!!
0000   0x01 0x66 0x03                             .f.
Command exited with non-zero status 1
python pump/stick.py /dev/ttyUSB0
	elapsed 0:00.31
```
### stats

```
474:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1059L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 1057L, 'errors.crc': 0}
492:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 606L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 576L, 'errors.crc': 0}
493:INFO:__main__:{'radio': {'errors.crc': 0,
494:           'errors.naks': 0,
495:           'errors.sequence': 0,
496:           'errors.timeouts': 0,
497:           'packets.received': 576L,
498:           'packets.transmit': 606L},
499: 'usb': {'errors.crc': 0,
500:         'errors.naks': 2,
501:         'errors.sequence': 0,
502:         'errors.timeouts': 0,
503:         'packets.received': 1057L,
504:         'packets.transmit': 1059L}}
523:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1061L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 1059L, 'errors.crc': 0}
541:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 607L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 577L, 'errors.crc': 0}
543:{'radio': {'errors.crc': 0,
544:           'errors.naks': 0,
545:           'errors.sequence': 0,
546:           'errors.timeouts': 0,
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
233:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 868L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 867L, 'errors.crc': 0}
251:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
252:INFO:__main__:{'radio': {'errors.crc': 0,
253:           'errors.naks': 0,
254:           'errors.sequence': 0,
255:           'errors.timeouts': 0,
256:           'packets.received': 476L,
257:           'packets.transmit': 501L},
258: 'usb': {'errors.crc': 0,
259:         'errors.naks': 1,
260:         'errors.sequence': 0,
261:         'errors.timeouts': 0,
262:         'packets.received': 867L,
263:         'packets.transmit': 868L}}
282:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 870L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 869L, 'errors.crc': 0}
300:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
302:{'radio': {'errors.crc': 0,
303:           'errors.naks': 0,
304:           'errors.sequence': 0,
305:           'errors.timeouts': 0,
306:           'packets.received': 476L,
307:           'packets.transmit': 501L},
308: 'usb': {'errors.crc': 0,
309:         'errors.naks': 1,
310:         'errors.sequence': 0,
311:         'errors.timeouts': 0,
312:         'packets.received': 869L,
313:         'packets.transmit': 870L}}
314:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
409:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
427:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 876L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 875L, 'errors.crc': 0}
445:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
446:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
447:{'radio': {'errors.crc': 0,
448:           'errors.naks': 0,
449:           'errors.sequence': 0,
450:           'errors.timeouts': 0,
451:           'packets.received': 476L,
452:           'packets.transmit': 501L},
453: 'usb': {'errors.crc': 0,
454:         'errors.naks': 1,
455:         'errors.sequence': 0,
456:         'errors.timeouts': 0,
457:         'packets.received': 875L,
458:         'packets.transmit': 876L}}
478:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 878L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 877L, 'errors.crc': 0}
496:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
498:{'radio': {'errors.crc': 0,
499:           'errors.naks': 0,
500:           'errors.sequence': 0,
501:           'errors.timeouts': 0,
502:           'packets.received': 476L,
503:           'packets.transmit': 501L},
504: 'usb': {'errors.crc': 0,
505:         'errors.naks': 1,
506:         'errors.sequence': 0,
507:         'errors.timeouts': 0,
508:         'packets.received': 877L,
509:         'packets.transmit': 878L}}
510:INFO:__main__:howdy! all done looking at the stick
516:INFO:__main__:howdy! I'm going to take a look at your pump.
656:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 886L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 885L, 'errors.crc': 0}
674:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 501L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 476L, 'errors.crc': 0}
675:INFO:__main__:{'radio': {'errors.crc': 0,
676:           'errors.naks': 0,
677:           'errors.sequence': 0,
678:           'errors.timeouts': 0,
679:           'packets.received': 476L,
680:           'packets.transmit': 501L},
681: 'usb': {'errors.crc': 0,
682:         'errors.naks': 1,
683:         'errors.sequence': 0,
684:         'errors.timeouts': 0,
685:         'packets.received': 885L,
686:         'packets.transmit': 886L}}
712:INFO:__main__:sleeping 17 before download
713:INFO:__main__:no download required
714:INFO:__main__:manually download PowerControl
744:INFO:stick:download_packet:15
760:WARNING:stick:bad zero CRC?
761:INFO:__main__:ENDING manual download:
780:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 891L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 890L, 'errors.crc': 0}
798:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 503L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 478L, 'errors.crc': 0}
799:INFO:__main__:{'radio': {'errors.crc': 0,
800:           'errors.naks': 0,
801:           'errors.sequence': 0,
802:           'errors.timeouts': 0,
803:           'packets.received': 478L,
804:           'packets.transmit': 503L},
805: 'usb': {'errors.crc': 0,
806:         'errors.naks': 1,
807:         'errors.sequence': 0,
808:         'errors.timeouts': 0,
809:         'packets.received': 890L,
810:         'packets.transmit': 891L}}
834:INFO:__main__:sleeping 0 before download
835:INFO:__main__:proceeding with download
884:INFO:stick:download_packet:78
925:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 897L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 896L, 'errors.crc': 0}
943:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 504L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 479L, 'errors.crc': 0}
944:INFO:__main__:{'radio': {'errors.crc': 0,
945:           'errors.naks': 0,
946:           'errors.sequence': 0,
947:           'errors.timeouts': 0,
948:           'packets.received': 479L,
949:           'packets.transmit': 504L},
950: 'usb': {'errors.crc': 0,
951:         'errors.naks': 1,
952:         'errors.sequence': 0,
953:         'errors.timeouts': 0,
954:         'packets.received': 896L,
955:         'packets.transmit': 897L}}
956:INFO:__main__:howdy! all done looking at pump
962:INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
1102:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 905L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 904L, 'errors.crc': 0}
1120:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 504L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 479L, 'errors.crc': 0}
1121:INFO:__main__:{'radio': {'errors.crc': 0,
1122:           'errors.naks': 0,
1123:           'errors.sequence': 0,
1124:           'errors.timeouts': 0,
1125:           'packets.received': 479L,
1126:           'packets.transmit': 504L},
1127: 'usb': {'errors.crc': 0,
1128:         'errors.naks': 1,
1129:         'errors.sequence': 0,
1130:         'errors.timeouts': 0,
1131:         'packets.received': 904L,
1132:         'packets.transmit': 905L}}
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
3256:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 977L, 'errors.naks': 1, 'errors.sequence': 0, 'packets.received': 976L, 'errors.crc': 0}
3274:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 535L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 509L, 'errors.crc': 0}
3275:INFO:__main__:{'radio': {'errors.crc': 0,
3276:           'errors.naks': 0,
3277:           'errors.sequence': 0,
3278:           'errors.timeouts': 0,
3279:           'packets.received': 509L,
3280:           'packets.transmit': 535L},
3281: 'usb': {'errors.crc': 0,
3282:         'errors.naks': 1,
3283:         'errors.sequence': 0,
3284:         'errors.timeouts': 0,
3285:         'packets.received': 976L,
3286:         'packets.transmit': 977L}}
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
6195:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
6382:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1059L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 1057L, 'errors.crc': 0}
6400:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 606L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 576L, 'errors.crc': 0}
6401:INFO:__main__:{'radio': {'errors.crc': 0,
6402:           'errors.naks': 0,
6403:           'errors.sequence': 0,
6404:           'errors.timeouts': 0,
6405:           'packets.received': 576L,
6406:           'packets.transmit': 606L},
6407: 'usb': {'errors.crc': 0,
6408:         'errors.naks': 2,
6409:         'errors.sequence': 0,
6410:         'errors.timeouts': 0,
6411:         'packets.received': 1057L,
6412:         'packets.transmit': 1059L}}
6431:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1061L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 1059L, 'errors.crc': 0}
6449:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 607L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 577L, 'errors.crc': 0}
6451:{'radio': {'errors.crc': 0,
6452:           'errors.naks': 0,
6453:           'errors.sequence': 0,
6454:           'errors.timeouts': 0,
6455:           'packets.received': 577L,
6456:           'packets.transmit': 607L},
6457: 'usb': {'errors.crc': 0,
6458:         'errors.naks': 2,
6459:         'errors.sequence': 0,
6460:         'errors.timeouts': 0,
6461:         'packets.received': 1059L,
6462:         'packets.transmit': 1061L}}
6463:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
6489:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 718:SHOULD DOWNLOAD :True
6490:INFO:__main__:XXX:clear_buffer[attempt][0]:download the size? 718:segments[0],total_segments[0]:raw[0]
6491:INFO:__main__:XXX:clear_buffer[attempt][0] size:718:segments[0],total_segments[0]:raw[0]:clear_buffer BUFFER self.download( )
6517:INFO:__main__:download_packet:782
6628:WARNING:__main__:bad zero CRC?
6629:INFO:__main__:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x58:raw:
6924:CRITICAL:__main__:XXX:clear_buffer[attempt][0]:IGNORING:segments[0],total_segments[0]:raw[0]:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x58:raw:
7219:INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 0 segment:segments[0],total_segments[0]:raw[0]:RAW:
7332:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1070L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 1068L, 'errors.crc': 0}
7350:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 608L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 578L, 'errors.crc': 0}
7352:{'radio': {'errors.crc': 0,
7353:           'errors.naks': 0,
7354:           'errors.sequence': 0,
7355:           'errors.timeouts': 0,
7356:           'packets.received': 578L,
7357:           'packets.transmit': 608L},
7358: 'usb': {'errors.crc': 0,
7359:         'errors.naks': 2,
7360:         'errors.sequence': 0,
7361:         'errors.timeouts': 0,
7362:         'packets.received': 1068L,
7363:         'packets.transmit': 1070L}}
7381:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1072L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 1070L, 'errors.crc': 0}
7399:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 608L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 578L, 'errors.crc': 0}
7401:{'radio': {'errors.crc': 0,
7402:           'errors.naks': 0,
7403:           'errors.sequence': 0,
7404:           'errors.timeouts': 0,
7405:           'packets.received': 578L,
7406:           'packets.transmit': 608L},
7407: 'usb': {'errors.crc': 0,
7408:         'errors.naks': 2,
7409:         'errors.sequence': 0,
7410:         'errors.timeouts': 0,
7411:         'packets.received': 1070L,
7412:         'packets.transmit': 1072L}}
7413:INFO:__main__:XXX:clear_buffer[attempt][1]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
7508:INFO:__main__:XXX:clear_buffer[attempt][1]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
7526:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1078L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 1076L, 'errors.crc': 0}
7544:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 608L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 578L, 'errors.crc': 0}
7545:INFO:__main__:XXX:clear_buffer[attempt][1]:END:no data:INTERFACE STATS
7546:{'radio': {'errors.crc': 0,
7547:           'errors.naks': 0,
7548:           'errors.sequence': 0,
7549:           'errors.timeouts': 0,
7550:           'packets.received': 578L,
7551:           'packets.transmit': 608L},
7552: 'usb': {'errors.crc': 0,
7553:         'errors.naks': 2,
7554:         'errors.sequence': 0,
7555:         'errors.timeouts': 0,
7556:         'packets.received': 1076L,
7557:         'packets.transmit': 1078L}}
7577:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1080L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 1078L, 'errors.crc': 0}
7595:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 608L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 578L, 'errors.crc': 0}
7597:{'radio': {'errors.crc': 0,
7598:           'errors.naks': 0,
7599:           'errors.sequence': 0,
7600:           'errors.timeouts': 0,
7601:           'packets.received': 578L,
7602:           'packets.transmit': 608L},
7603: 'usb': {'errors.crc': 0,
7604:         'errors.naks': 2,
7605:         'errors.sequence': 0,
7606:         'errors.timeouts': 0,
7607:         'packets.received': 1078L,
7608:         'packets.transmit': 1080L}}
7609:INFO:__main__:howdy! all done looking at the stick
```
* NAK FOUND
* NOT A CLEAN RUN
