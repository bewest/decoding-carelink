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
Tue Jan  8 21:22:19 PST 2013

## stick

* stick runs appear to be ok


## pump


## downloaded:10

```
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xc4\x80@\xa7\x01 \x88P\xa1\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][1], bytearray(b'\x00\xc1\x80\x80\xa7\x01 \x88P\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][2], bytearray(b'\x00\xc2\x80\x80\xa7\x01 \x88P\x9c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x92\x9e\x0b\x01\x06\x07\x00\x00\x02L\xa1\x06l\xa1\x06\x05\x0c\x00\xe8\x00\x00\x00\x00\x02L\x02Ld\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][3], bytearray(b'\x02\x00\x80\x00\xa7\x01 \x88Pf\x00\xda\x82\x0cl\x82\x0c\x05\x00edf\x12\x00\x00\x04\xda\x03\x9eK\x01<\x19\x00O\x01<\x19\x01<d\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x00d\x01V\xca\x06\x01\x06\x17\x00')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][4], bytearray(b'\x02\x00\x80\x00\xa7\x01 \x88Pf\x00&\x08\x05\x07\x00\x00\x03\x96h\x85lh\x85\x05\x00```\x01\x00\x00\x03\x96\x02\xf6S\x00\xa0\x11\x00\x00\x00\xa0\x11\x00\x00\x00\x00\x00\x00\x00\xa0d\x01\x00\x00\x00\x01[d')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][5], bytearray(b'\x00\xc5\x80\x80\xa7\x01 \x88Py\x00\x02\x00!\x00l!\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x02\x00\x02\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x0c\x9c\x13\x02\x00\x17')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][6], bytearray(b'\x00\xc3\x80\x80\xa7\x01 \x88P\x01\x00\x00,\x00l,\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00-\x00l-')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][7], bytearray(b'\x00\xc4\x80\x80\xa7\x01 \x88P\xe4\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x15\x80l\x15\x80\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07')
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][8], bytearray(b'\x00\xc2\x80\x80\xa7\x01 \x88P\x9c\x1f\x00)C\x04A\x00\x07\x00\x00\x04\xcc\x01\x80l\x01\x80\x05\x00ddd\x0b\x00\x00\x04\xcc\x03\xbeN\x01\x0e\x16\x00A\x01\x0e\x16\x01\x04`\x00\x00\x00\x00\n\x04\x0c\x0b\x00\x00')
```

## howdy! pump runs appear to be OK


## Diagnose CRC

```
19:  echo "Was there an ACK ERROR?"
20:  echo "### DIAGNOSE CRC"
46:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
233:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 773L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 773L, 'errors.crc': 0}
251:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 390L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 361L, 'errors.crc': 0}
252:INFO:__main__:{'radio': {'errors.crc': 0,
253:           'errors.naks': 0,
254:           'errors.sequence': 4,
255:           'errors.timeouts': 9,
256:           'packets.received': 361L,
257:           'packets.transmit': 390L},
258: 'usb': {'errors.crc': 0,
259:         'errors.naks': 0,
260:         'errors.sequence': 0,
261:         'errors.timeouts': 0,
262:         'packets.received': 773L,
263:         'packets.transmit': 773L}}
282:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 775L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 775L, 'errors.crc': 0}
300:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 390L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 361L, 'errors.crc': 0}
302:{'radio': {'errors.crc': 0,
303:           'errors.naks': 0,
304:           'errors.sequence': 4,
305:           'errors.timeouts': 9,
306:           'packets.received': 361L,
307:           'packets.transmit': 390L},
308: 'usb': {'errors.crc': 0,
309:         'errors.naks': 0,
310:         'errors.sequence': 0,
311:         'errors.timeouts': 0,
312:         'packets.received': 775L,
313:         'packets.transmit': 775L}}
314:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
409:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
427:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 781L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 781L, 'errors.crc': 0}
445:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 390L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 361L, 'errors.crc': 0}
446:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
447:{'radio': {'errors.crc': 0,
448:           'errors.naks': 0,
449:           'errors.sequence': 4,
450:           'errors.timeouts': 9,
451:           'packets.received': 361L,
452:           'packets.transmit': 390L},
453: 'usb': {'errors.crc': 0,
454:         'errors.naks': 0,
455:         'errors.sequence': 0,
456:         'errors.timeouts': 0,
457:         'packets.received': 781L,
458:         'packets.transmit': 781L}}
478:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 783L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 783L, 'errors.crc': 0}
496:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 390L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 361L, 'errors.crc': 0}
498:{'radio': {'errors.crc': 0,
499:           'errors.naks': 0,
500:           'errors.sequence': 4,
501:           'errors.timeouts': 9,
502:           'packets.received': 361L,
503:           'packets.transmit': 390L},
504: 'usb': {'errors.crc': 0,
505:         'errors.naks': 0,
506:         'errors.sequence': 0,
507:         'errors.timeouts': 0,
508:         'packets.received': 783L,
509:         'packets.transmit': 783L}}
510:INFO:__main__:howdy! all done looking at the stick
516:INFO:__main__:howdy! I'm going to take a look at your pump.
656:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 791L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 791L, 'errors.crc': 0}
674:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 390L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 361L, 'errors.crc': 0}
675:INFO:__main__:{'radio': {'errors.crc': 0,
676:           'errors.naks': 0,
677:           'errors.sequence': 4,
678:           'errors.timeouts': 9,
679:           'packets.received': 361L,
680:           'packets.transmit': 390L},
681: 'usb': {'errors.crc': 0,
682:         'errors.naks': 0,
683:         'errors.sequence': 0,
684:         'errors.timeouts': 0,
685:         'packets.received': 791L,
686:         'packets.transmit': 791L}}
712:INFO:__main__:sleeping 17 before download
713:INFO:__main__:no download required
714:INFO:__main__:manually download PowerControl
715:INFO:stick:download:start:0
716:INFO:stick:download(attempts[1]):begin first poll
792:INFO:stick:download(attempts[1],expect[0]):poll:
793:INFO:stick:download found empty poll size, sleep 3 and try again
888:INFO:stick:download(attempts[1],expect[0],results[0]:data[0]):DONE
889:INFO:__main__:ENDING manual download:
908:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 801L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 801L, 'errors.crc': 0}
926:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 391L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 361L, 'errors.crc': 0}
927:INFO:__main__:{'radio': {'errors.crc': 0,
928:           'errors.naks': 0,
929:           'errors.sequence': 4,
930:           'errors.timeouts': 9,
931:           'packets.received': 361L,
932:           'packets.transmit': 391L},
933: 'usb': {'errors.crc': 0,
934:         'errors.naks': 0,
935:         'errors.sequence': 0,
936:         'errors.timeouts': 0,
937:         'packets.received': 801L,
938:         'packets.transmit': 801L}}
962:INFO:__main__:sleeping 0 before download
963:INFO:__main__:proceeding with download
964:INFO:stick:download:start:0
965:INFO:stick:download(attempts[1]):begin first poll
1014:INFO:stick:download(attempts[1],expect[78]):poll:
1015:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
1016:INFO:stick:download_packet:78
1039:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
1040:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
1059:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 807L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 807L, 'errors.crc': 0}
1077:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 392L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 362L, 'errors.crc': 0}
1078:INFO:__main__:{'radio': {'errors.crc': 0,
1079:           'errors.naks': 0,
1080:           'errors.sequence': 4,
1081:           'errors.timeouts': 9,
1082:           'packets.received': 362L,
1083:           'packets.transmit': 392L},
1084: 'usb': {'errors.crc': 0,
1085:         'errors.naks': 0,
1086:         'errors.sequence': 0,
1087:         'errors.timeouts': 0,
1088:         'packets.received': 807L,
1089:         'packets.transmit': 807L}}
1090:INFO:__main__:howdy! all done looking at pump
1096:INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
1236:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 815L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 815L, 'errors.crc': 0}
1254:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 392L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 362L, 'errors.crc': 0}
1255:INFO:__main__:{'radio': {'errors.crc': 0,
1256:           'errors.naks': 0,
1257:           'errors.sequence': 4,
1258:           'errors.timeouts': 9,
1259:           'packets.received': 362L,
1260:           'packets.transmit': 392L},
1261: 'usb': {'errors.crc': 0,
1262:         'errors.naks': 0,
1263:         'errors.sequence': 0,
1264:         'errors.timeouts': 0,
1265:         'packets.received': 815L,
1266:         'packets.transmit': 815L}}
1290:INFO:session:sleeping 0 before download
1291:INFO:session:proceeding with download
1292:INFO:stick:download:start:0
1293:INFO:stick:download(attempts[1]):begin first poll
1342:INFO:stick:download(attempts[1],expect[78]):poll:
1343:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
1344:INFO:stick:download_packet:78
1367:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
1368:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
1393:INFO:session:sleeping 0 before download
1394:INFO:session:proceeding with download
1395:INFO:stick:download:start:0
1396:INFO:stick:download(attempts[1]):begin first poll
1445:INFO:stick:download(attempts[1],expect[78]):poll:
1446:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
1447:INFO:stick:download_packet:78
1470:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
1471:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
1498:INFO:session:sleeping 0 before download
1499:INFO:session:proceeding with download
1500:INFO:stick:download:start:0
1501:INFO:stick:download(attempts[1]):begin first poll
1550:INFO:stick:download(attempts[1],expect[78]):poll:
1551:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
1552:INFO:stick:download_packet:78
1575:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
1576:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
1602:INFO:session:sleeping 0 before download
1603:INFO:session:proceeding with download
1604:INFO:stick:download:start:0
1605:INFO:stick:download(attempts[1]):begin first poll
1654:INFO:stick:download(attempts[1],expect[78]):poll:
1655:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
1656:INFO:stick:download_packet:78
1679:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
1680:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
1706:INFO:session:sleeping 0 before download
1707:INFO:session:proceeding with download
1708:INFO:stick:download:start:0
1709:INFO:stick:download(attempts[1]):begin first poll
1758:INFO:stick:download(attempts[1],expect[78]):poll:
1759:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
1760:INFO:stick:download_packet:78
1783:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
1784:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
1810:INFO:session:sleeping 0 before download
1811:INFO:session:proceeding with download
1812:INFO:stick:download:start:0
1813:INFO:stick:download(attempts[1]):begin first poll
1862:INFO:stick:download(attempts[1],expect[78]):poll:
1863:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
1864:INFO:stick:download_packet:78
1887:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
1888:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
1923:INFO:session:sleeping 0 before download
1924:INFO:session:proceeding with download
1925:INFO:stick:download:start:0
1926:INFO:stick:download(attempts[1]):begin first poll
1975:INFO:stick:download(attempts[1],expect[78]):poll:
1976:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
1977:INFO:stick:download_packet:78
2000:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
2001:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
2036:INFO:session:sleeping 0 before download
2037:INFO:session:proceeding with download
2038:INFO:stick:download:start:0
2039:INFO:stick:download(attempts[1]):begin first poll
2088:INFO:stick:download(attempts[1],expect[78]):poll:
2089:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
2090:INFO:stick:download_packet:78
2113:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
2114:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
2149:INFO:session:sleeping 0 before download
2150:INFO:session:proceeding with download
2151:INFO:stick:download:start:0
2152:INFO:stick:download(attempts[1]):begin first poll
2201:INFO:stick:download(attempts[1],expect[78]):poll:
2202:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
2203:INFO:stick:download_packet:78
2226:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
2227:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
2262:INFO:session:sleeping 0 before download
2263:INFO:session:proceeding with download
2264:INFO:stick:download:start:0
2265:INFO:stick:download(attempts[1]):begin first poll
2314:INFO:stick:download(attempts[1],expect[78]):poll:
2315:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
2316:INFO:stick:download_packet:78
2339:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
2340:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
2375:INFO:session:sleeping 0 before download
2376:INFO:session:proceeding with download
2377:INFO:stick:download:start:0
2378:INFO:stick:download(attempts[1]):begin first poll
2427:INFO:stick:download(attempts[1],expect[78]):poll:
2428:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
2429:INFO:stick:download_packet:78
2452:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
2453:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
2488:INFO:session:sleeping 0 before download
2489:INFO:session:proceeding with download
2490:INFO:stick:download:start:0
2491:INFO:stick:download(attempts[1]):begin first poll
2540:INFO:stick:download(attempts[1],expect[78]):poll:
2541:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
2542:INFO:stick:download_packet:78
2565:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
2566:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
2601:INFO:session:sleeping 0 before download
2602:INFO:session:proceeding with download
2603:INFO:stick:download:start:0
2604:INFO:stick:download(attempts[1]):begin first poll
2653:INFO:stick:download(attempts[1],expect[78]):poll:
2654:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
2655:INFO:stick:download_packet:78
2678:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
2679:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
2715:INFO:session:sleeping 0.1 before download
2716:INFO:session:proceeding with download
2717:INFO:stick:download:start:0
2718:INFO:stick:download(attempts[1]):begin first poll
2767:INFO:stick:download(attempts[1],expect[78]):poll:
2768:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
2769:INFO:stick:download_packet:78
2792:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
2793:INFO:stick:download(attempts[2]):begin first poll
2819:INFO:stick:download(attempts[2],expect[206]):poll:
2820:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
2821:INFO:stick:download_packet:206
2860:INFO:stick:download(attempts[2],expect[206],results[256]:data[192]):adding segment
2861:INFO:stick:download(attempts[3]):begin first poll
2887:INFO:stick:download(attempts[3],expect[142]):poll:
2888:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
2889:INFO:stick:download_packet:142
2920:INFO:stick:download(attempts[3],expect[142],results[384]:data[128]):adding segment
2921:INFO:stick:download(attempts[4]):begin first poll
2947:INFO:stick:download(attempts[4],expect[142]):poll:
2948:INFO:stick:download(attempts[4],expect[142]):proceed to download_packet
2949:INFO:stick:download_packet:142
2980:WARNING:stick:bad zero CRC?
2981:INFO:stick:download(attempts[4],expect[142],results[512]:data[128]):adding segment
2982:INFO:stick:download(attempts[5]):begin first poll
3008:INFO:stick:download(attempts[5],expect[142]):poll:
3009:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
3010:INFO:stick:download_packet:142
3041:WARNING:stick:bad zero CRC?
3042:INFO:stick:download(attempts[5],expect[142],results[640]:data[128]):adding segment
3043:INFO:stick:download(attempts[6]):begin first poll
3069:INFO:stick:download(attempts[6],expect[142]):poll:
3070:INFO:stick:download(attempts[6],expect[142]):proceed to download_packet
3071:INFO:stick:download_packet:142
3102:WARNING:stick:bad zero CRC?
3103:INFO:stick:download(attempts[6],expect[142],results[768]:data[128]):adding segment
3104:INFO:stick:download(attempts[7]):begin first poll
3130:INFO:stick:download(attempts[7],expect[142]):poll:
3131:INFO:stick:download(attempts[7],expect[142]):proceed to download_packet
3132:INFO:stick:download_packet:142
3163:WARNING:stick:bad zero CRC?
3164:INFO:stick:download(attempts[7],expect[142],results[896]:data[128]):adding segment
3165:INFO:stick:download(attempts[8]):begin first poll
3191:INFO:stick:download(attempts[8],expect[142]):poll:
3192:INFO:stick:download(attempts[8],expect[142]):proceed to download_packet
3193:INFO:stick:download_packet:142
3224:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):adding segment
3225:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):DONE
3501:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 887L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 887L, 'errors.crc': 0}
3519:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 9, 'packets.transmit': 423L, 'errors.naks': 0, 'errors.sequence': 4, 'packets.received': 392L, 'errors.crc': 0}
3520:INFO:__main__:{'radio': {'errors.crc': 0,
3521:           'errors.naks': 0,
3522:           'errors.sequence': 4,
3523:           'errors.timeouts': 9,
3524:           'packets.received': 392L,
3525:           'packets.transmit': 423L},
3526: 'usb': {'errors.crc': 0,
3527:         'errors.naks': 0,
3528:         'errors.sequence': 0,
3529:         'errors.timeouts': 0,
3530:         'packets.received': 887L,
3531:         'packets.transmit': 887L}}
3556:INFO:session:sleeping 0 before download
3557:INFO:session:proceeding with download
3558:INFO:stick:download:start:0
3559:INFO:stick:download(attempts[1]):begin first poll
3608:INFO:stick:download(attempts[1],expect[78]):poll:
3609:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
3610:INFO:stick:download_packet:78
3633:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
3634:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):DONE
3670:INFO:session:sleeping 0.1 before download
3671:INFO:session:proceeding with download
3672:INFO:stick:download:start:0
3673:INFO:stick:download(attempts[1]):begin first poll
3722:INFO:stick:download(attempts[1],expect[78]):poll:
3723:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
3724:INFO:stick:download_packet:78
3747:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
3748:INFO:stick:download(attempts[2]):begin first poll
3774:INFO:stick:download(attempts[2],expect[206]):poll:
3775:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
3776:INFO:stick:download_packet:206
3815:WARNING:stick:bad zero CRC?
3816:INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x5f:raw:
3895:INFO:stick:XXX:BadCRC:returning empty message instead of raising errors.
3896:INFO:stick:download(attempts[2],expect[206],results[64]:data[0]):no data, try again
3897:INFO:stick:download(attempts[3]):begin first poll
3923:INFO:stick:download(attempts[3],expect[142]):poll:
3924:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
3925:INFO:stick:download_packet:142
3956:INFO:stick:download(attempts[3],expect[142],results[192]:data[128]):adding segment
3957:INFO:stick:download(attempts[4]):begin first poll
3983:INFO:stick:download(attempts[4],expect[142]):poll:
3984:INFO:stick:download(attempts[4],expect[142]):proceed to download_packet
3985:INFO:stick:download_packet:142
4016:WARNING:stick:bad zero CRC?
4017:INFO:stick:download(attempts[4],expect[142],results[320]:data[128]):adding segment
4018:INFO:stick:download(attempts[5]):begin first poll
4044:INFO:stick:download(attempts[5],expect[142]):poll:
4045:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
4046:INFO:stick:download_packet:142
4077:WARNING:stick:bad zero CRC?
4078:INFO:stick:download(attempts[5],expect[142],results[448]:data[128]):adding segment
4079:INFO:stick:download(attempts[6]):begin first poll
4105:INFO:stick:download(attempts[6],expect[142]):poll:
4106:INFO:stick:download(attempts[6],expect[142]):proceed to download_packet
4107:INFO:stick:download_packet:142
4138:WARNING:stick:bad zero CRC?
4139:INFO:stick:download(attempts[6],expect[142],results[576]:data[128]):adding segment
4140:INFO:stick:download(attempts[7]):begin first poll
4166:INFO:stick:download(attempts[7],expect[142]):poll:
4167:INFO:stick:download(attempts[7],expect[142]):proceed to download_packet
4168:INFO:stick:download_packet:142
4199:WARNING:stick:bad zero CRC?
4200:INFO:stick:download(attempts[7],expect[142],results[704]:data[128]):adding segment
4201:INFO:stick:download(attempts[8]):begin first poll
4227:INFO:stick:download(attempts[8],expect[142]):poll:
4228:INFO:stick:download(attempts[8],expect[142]):proceed to download_packet
4229:INFO:stick:download_packet:142
4260:INFO:stick:download(attempts[8],expect[142],results[832]:data[128]):adding segment
4261:INFO:stick:download(attempts[8],expect[142],results[832]:data[128]):DONE
4497:INFO:session:sleeping 0.1 before download
4498:INFO:session:proceeding with download
4499:INFO:stick:download:start:0
4500:INFO:stick:download(attempts[1]):begin first poll
4549:INFO:stick:download(attempts[1],expect[78]):poll:
4550:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
4551:INFO:stick:download_packet:78
4574:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
4575:INFO:stick:download(attempts[2]):begin first poll
4601:INFO:stick:download(attempts[2],expect[206]):poll:
4602:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
4603:INFO:stick:download_packet:206
4642:INFO:stick:download(attempts[2],expect[206],results[256]:data[192]):adding segment
4643:INFO:stick:download(attempts[3]):begin first poll
4669:INFO:stick:download(attempts[3],expect[142]):poll:
4670:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
4671:INFO:stick:download_packet:142
4702:INFO:stick:download(attempts[3],expect[142],results[384]:data[128]):adding segment
4703:INFO:stick:download(attempts[4]):begin first poll
4729:INFO:stick:download(attempts[4],expect[142]):poll:
4730:INFO:stick:download(attempts[4],expect[142]):proceed to download_packet
4731:INFO:stick:download_packet:142
4762:INFO:stick:download(attempts[4],expect[142],results[512]:data[128]):adding segment
4763:INFO:stick:download(attempts[5]):begin first poll
4789:INFO:stick:download(attempts[5],expect[142]):poll:
4790:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
4791:INFO:stick:download_packet:142
4822:INFO:stick:download(attempts[5],expect[142],results[640]:data[128]):adding segment
4823:INFO:stick:download(attempts[6]):begin first poll
4849:INFO:stick:download(attempts[6],expect[142]):poll:
4850:INFO:stick:download(attempts[6],expect[142]):proceed to download_packet
4851:INFO:stick:download_packet:142
4882:INFO:stick:download(attempts[6],expect[142],results[768]:data[128]):adding segment
4883:INFO:stick:download(attempts[7]):begin first poll
4909:INFO:stick:download(attempts[7],expect[142]):poll:
4910:INFO:stick:download(attempts[7],expect[142]):proceed to download_packet
4911:INFO:stick:download_packet:142
4942:INFO:stick:download(attempts[7],expect[142],results[896]:data[128]):adding segment
4943:INFO:stick:download(attempts[8]):begin first poll
4969:INFO:stick:download(attempts[8],expect[142]):poll:
4970:INFO:stick:download(attempts[8],expect[142]):proceed to download_packet
4971:INFO:stick:download_packet:142
5002:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):adding segment
5003:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):DONE
5287:INFO:session:sleeping 0.1 before download
5288:INFO:session:proceeding with download
5289:INFO:stick:download:start:0
5290:INFO:stick:download(attempts[1]):begin first poll
5339:INFO:stick:download(attempts[1],expect[78]):poll:
5340:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
5341:INFO:stick:download_packet:78
5364:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
5365:INFO:stick:download(attempts[2]):begin first poll
5391:INFO:stick:download(attempts[2],expect[206]):poll:
5392:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
5393:INFO:stick:download_packet:206
5432:INFO:stick:download(attempts[2],expect[206],results[256]:data[192]):adding segment
5433:INFO:stick:download(attempts[3]):begin first poll
5459:INFO:stick:download(attempts[3],expect[142]):poll:
5460:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
5461:INFO:stick:download_packet:142
5492:INFO:stick:download(attempts[3],expect[142],results[384]:data[128]):adding segment
5493:INFO:stick:download(attempts[4]):begin first poll
5519:INFO:stick:download(attempts[4],expect[142]):poll:
5520:INFO:stick:download(attempts[4],expect[142]):proceed to download_packet
5521:INFO:stick:download_packet:142
5552:INFO:stick:download(attempts[4],expect[142],results[512]:data[128]):adding segment
5553:INFO:stick:download(attempts[5]):begin first poll
5579:INFO:stick:download(attempts[5],expect[142]):poll:
5580:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
5581:INFO:stick:download_packet:142
5612:INFO:stick:download(attempts[5],expect[142],results[640]:data[128]):adding segment
5613:INFO:stick:download(attempts[6]):begin first poll
5639:INFO:stick:download(attempts[6],expect[142]):poll:
5640:INFO:stick:download(attempts[6],expect[142]):proceed to download_packet
5641:INFO:stick:download_packet:142
5672:INFO:stick:download(attempts[6],expect[142],results[768]:data[128]):adding segment
5673:INFO:stick:download(attempts[7]):begin first poll
5699:INFO:stick:download(attempts[7],expect[142]):poll:
5700:INFO:stick:download(attempts[7],expect[142]):proceed to download_packet
5701:INFO:stick:download_packet:142
5732:INFO:stick:download(attempts[7],expect[142],results[896]:data[128]):adding segment
5733:INFO:stick:download(attempts[8]):begin first poll
5759:INFO:stick:download(attempts[8],expect[78]):poll:
5760:INFO:stick:download(attempts[8],expect[78]):proceed to download_packet
5761:INFO:stick:download_packet:78
5784:INFO:stick:download(attempts[8],expect[78],results[960]:data[64]):adding segment
5785:INFO:stick:download(attempts[9]):begin first poll
5880:INFO:stick:download(attempts[9],expect[0]):poll:
5881:INFO:stick:download found empty poll size, sleep 3 and try again
5907:INFO:stick:download(attempts[9],expect[14]):proceed to download_packet
5908:INFO:stick:download_packet:14
5924:WARNING:stick:bad zero CRC?
5925:INFO:stick:download(attempts[9],expect[14],results[960]:data[0]):no data, try again
5926:INFO:stick:download(attempts[9],expect[14],results[960]:data[0]):DONE
6194:INFO:session:sleeping 0.1 before download
6195:INFO:session:proceeding with download
6196:INFO:stick:download:start:0
6197:INFO:stick:download(attempts[1]):begin first poll
6246:INFO:stick:download(attempts[1],expect[78]):poll:
6247:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
6248:INFO:stick:download_packet:78
6271:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
6272:INFO:stick:download(attempts[2]):begin first poll
6298:INFO:stick:download(attempts[2],expect[206]):poll:
6299:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
6300:INFO:stick:download_packet:206
6339:INFO:stick:download(attempts[2],expect[206],results[256]:data[192]):adding segment
6340:INFO:stick:download(attempts[3]):begin first poll
6366:INFO:stick:download(attempts[3],expect[142]):poll:
6367:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
6368:INFO:stick:download_packet:142
6399:INFO:stick:download(attempts[3],expect[142],results[384]:data[128]):adding segment
6400:INFO:stick:download(attempts[4]):begin first poll
6426:INFO:stick:download(attempts[4],expect[78]):poll:
6427:INFO:stick:download(attempts[4],expect[78]):proceed to download_packet
6428:INFO:stick:download_packet:78
6451:INFO:stick:download(attempts[4],expect[78],results[448]:data[64]):adding segment
6452:INFO:stick:download(attempts[5]):begin first poll
6547:INFO:stick:download(attempts[5],expect[0]):poll:
6548:INFO:stick:download found empty poll size, sleep 3 and try again
6574:INFO:stick:download(attempts[5],expect[14]):proceed to download_packet
6575:INFO:stick:download_packet:14
6591:WARNING:stick:bad zero CRC?
6592:INFO:stick:download(attempts[5],expect[14],results[448]:data[0]):no data, try again
6593:INFO:stick:download(attempts[5],expect[14],results[448]:data[0]):DONE
6733:INFO:session:sleeping 0.1 before download
6734:INFO:session:proceeding with download
6735:INFO:stick:download:start:0
6736:INFO:stick:download(attempts[1]):begin first poll
6785:INFO:stick:download(attempts[1],expect[78]):poll:
6786:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
6787:INFO:stick:download_packet:78
6810:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
6811:INFO:stick:download(attempts[2]):begin first poll
6837:INFO:stick:download(attempts[2],expect[206]):poll:
6838:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
6839:INFO:stick:download_packet:206
6878:INFO:stick:download(attempts[2],expect[206],results[256]:data[192]):adding segment
6879:INFO:stick:download(attempts[3]):begin first poll
6905:INFO:stick:download(attempts[3],expect[142]):poll:
6906:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
6907:INFO:stick:download_packet:142
6938:INFO:stick:download(attempts[3],expect[142],results[384]:data[128]):adding segment
6939:INFO:stick:download(attempts[4]):begin first poll
6965:INFO:stick:download(attempts[4],expect[142]):poll:
6966:INFO:stick:download(attempts[4],expect[142]):proceed to download_packet
6967:INFO:stick:download_packet:142
6998:INFO:stick:download(attempts[4],expect[142],results[512]:data[128]):adding segment
6999:INFO:stick:download(attempts[5]):begin first poll
7025:INFO:stick:download(attempts[5],expect[142]):poll:
7026:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
7027:INFO:stick:download_packet:142
7058:INFO:stick:download(attempts[5],expect[142],results[640]:data[128]):adding segment
7059:INFO:stick:download(attempts[6]):begin first poll
7085:INFO:stick:download(attempts[6],expect[142]):poll:
7086:INFO:stick:download(attempts[6],expect[142]):proceed to download_packet
7087:INFO:stick:download_packet:142
7118:INFO:stick:download(attempts[6],expect[142],results[768]:data[128]):adding segment
7119:INFO:stick:download(attempts[7]):begin first poll
7145:INFO:stick:download(attempts[7],expect[142]):poll:
7146:INFO:stick:download(attempts[7],expect[142]):proceed to download_packet
7147:INFO:stick:download_packet:142
7178:INFO:stick:download(attempts[7],expect[142],results[896]:data[128]):adding segment
7179:INFO:stick:download(attempts[8]):begin first poll
7205:INFO:stick:download(attempts[8],expect[142]):poll:
7206:INFO:stick:download(attempts[8],expect[142]):proceed to download_packet
7207:INFO:stick:download_packet:142
7238:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):adding segment
7239:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):DONE
7523:INFO:session:sleeping 0.1 before download
7524:INFO:session:proceeding with download
7525:INFO:stick:download:start:0
7526:INFO:stick:download(attempts[1]):begin first poll
7575:INFO:stick:download(attempts[1],expect[78]):poll:
7576:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
7577:INFO:stick:download_packet:78
7600:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
7601:INFO:stick:download(attempts[2]):begin first poll
7627:INFO:stick:download(attempts[2],expect[206]):poll:
7628:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
7629:INFO:stick:download_packet:206
7668:WARNING:stick:bad zero CRC?
7669:INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x06:raw:
7748:INFO:stick:XXX:BadCRC:returning empty message instead of raising errors.
7749:INFO:stick:download(attempts[2],expect[206],results[64]:data[0]):no data, try again
7750:INFO:stick:download(attempts[3]):begin first poll
7776:INFO:stick:download(attempts[3],expect[142]):poll:
7777:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
7778:INFO:stick:download_packet:142
7809:INFO:stick:download(attempts[3],expect[142],results[192]:data[128]):adding segment
7810:INFO:stick:download(attempts[4]):begin first poll
7836:INFO:stick:download(attempts[4],expect[142]):poll:
7837:INFO:stick:download(attempts[4],expect[142]):proceed to download_packet
7838:INFO:stick:download_packet:142
7869:INFO:stick:download(attempts[4],expect[142],results[320]:data[128]):adding segment
7870:INFO:stick:download(attempts[5]):begin first poll
7896:INFO:stick:download(attempts[5],expect[142]):poll:
7897:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
7898:INFO:stick:download_packet:142
7929:INFO:stick:download(attempts[5],expect[142],results[448]:data[128]):adding segment
7930:INFO:stick:download(attempts[6]):begin first poll
7956:INFO:stick:download(attempts[6],expect[142]):poll:
7957:INFO:stick:download(attempts[6],expect[142]):proceed to download_packet
7958:INFO:stick:download_packet:142
7989:INFO:stick:download(attempts[6],expect[142],results[576]:data[128]):adding segment
7990:INFO:stick:download(attempts[7]):begin first poll
8016:INFO:stick:download(attempts[7],expect[142]):poll:
8017:INFO:stick:download(attempts[7],expect[142]):proceed to download_packet
8018:INFO:stick:download_packet:142
8049:INFO:stick:download(attempts[7],expect[142],results[704]:data[128]):adding segment
8050:INFO:stick:download(attempts[8]):begin first poll
8076:INFO:stick:download(attempts[8],expect[142]):poll:
8077:INFO:stick:download(attempts[8],expect[142]):proceed to download_packet
8078:INFO:stick:download_packet:142
8109:INFO:stick:download(attempts[8],expect[142],results[832]:data[128]):adding segment
8110:INFO:stick:download(attempts[8],expect[142],results[832]:data[128]):DONE
8346:INFO:session:sleeping 0.1 before download
8347:INFO:session:proceeding with download
8348:INFO:stick:download:start:0
8349:INFO:stick:download(attempts[1]):begin first poll
8398:INFO:stick:download(attempts[1],expect[78]):poll:
8399:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
8400:INFO:stick:download_packet:78
8423:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
8424:INFO:stick:download(attempts[2]):begin first poll
8450:INFO:stick:download(attempts[2],expect[206]):poll:
8451:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
8452:INFO:stick:download_packet:206
8491:INFO:stick:download(attempts[2],expect[206],results[256]:data[192]):adding segment
8492:INFO:stick:download(attempts[3]):begin first poll
8518:INFO:stick:download(attempts[3],expect[142]):poll:
8519:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
8520:INFO:stick:download_packet:142
8551:INFO:stick:download(attempts[3],expect[142],results[384]:data[128]):adding segment
8552:INFO:stick:download(attempts[4]):begin first poll
8578:INFO:stick:download(attempts[4],expect[142]):poll:
8579:INFO:stick:download(attempts[4],expect[142]):proceed to download_packet
8580:INFO:stick:download_packet:142
8611:INFO:stick:download(attempts[4],expect[142],results[512]:data[128]):adding segment
8612:INFO:stick:download(attempts[5]):begin first poll
8638:INFO:stick:download(attempts[5],expect[142]):poll:
8639:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
8640:INFO:stick:download_packet:142
8671:INFO:stick:download(attempts[5],expect[142],results[640]:data[128]):adding segment
8672:INFO:stick:download(attempts[6]):begin first poll
8698:INFO:stick:download(attempts[6],expect[142]):poll:
8699:INFO:stick:download(attempts[6],expect[142]):proceed to download_packet
8700:INFO:stick:download_packet:142
8731:INFO:stick:download(attempts[6],expect[142],results[768]:data[128]):adding segment
8732:INFO:stick:download(attempts[7]):begin first poll
8758:INFO:stick:download(attempts[7],expect[142]):poll:
8759:INFO:stick:download(attempts[7],expect[142]):proceed to download_packet
8760:INFO:stick:download_packet:142
8791:INFO:stick:download(attempts[7],expect[142],results[896]:data[128]):adding segment
8792:INFO:stick:download(attempts[8]):begin first poll
8818:INFO:stick:download(attempts[8],expect[142]):poll:
8819:INFO:stick:download(attempts[8],expect[142]):proceed to download_packet
8820:INFO:stick:download_packet:142
8851:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):adding segment
8852:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):DONE
9136:INFO:session:sleeping 0.1 before download
9137:INFO:session:proceeding with download
9138:INFO:stick:download:start:0
9139:INFO:stick:download(attempts[1]):begin first poll
9188:INFO:stick:download(attempts[1],expect[78]):poll:
9189:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
9190:INFO:stick:download_packet:78
9213:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
9214:INFO:stick:download(attempts[2]):begin first poll
9240:INFO:stick:download(attempts[2],expect[206]):poll:
9241:INFO:stick:download(attempts[2],expect[206]):proceed to download_packet
9242:INFO:stick:download_packet:206
9281:INFO:stick:download(attempts[2],expect[206],results[256]:data[192]):adding segment
9282:INFO:stick:download(attempts[3]):begin first poll
9308:INFO:stick:download(attempts[3],expect[142]):poll:
9309:INFO:stick:download(attempts[3],expect[142]):proceed to download_packet
9310:INFO:stick:download_packet:142
9341:INFO:stick:download(attempts[3],expect[142],results[384]:data[128]):adding segment
9342:INFO:stick:download(attempts[4]):begin first poll
9368:INFO:stick:download(attempts[4],expect[142]):poll:
9369:INFO:stick:download(attempts[4],expect[142]):proceed to download_packet
9370:INFO:stick:download_packet:142
9401:INFO:stick:download(attempts[4],expect[142],results[512]:data[128]):adding segment
9402:INFO:stick:download(attempts[5]):begin first poll
9428:INFO:stick:download(attempts[5],expect[142]):poll:
9429:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
9430:INFO:stick:download_packet:142
9461:INFO:stick:download(attempts[5],expect[142],results[640]:data[128]):adding segment
9462:INFO:stick:download(attempts[6]):begin first poll
9488:INFO:stick:download(attempts[6],expect[142]):poll:
9489:INFO:stick:download(attempts[6],expect[142]):proceed to download_packet
9490:INFO:stick:download_packet:142
9521:INFO:stick:download(attempts[6],expect[142],results[768]:data[128]):adding segment
9522:INFO:stick:download(attempts[7]):begin first poll
9548:INFO:stick:download(attempts[7],expect[142]):poll:
9549:INFO:stick:download(attempts[7],expect[142]):proceed to download_packet
9550:INFO:stick:download_packet:142
9581:INFO:stick:download(attempts[7],expect[142],results[896]:data[128]):adding segment
9582:INFO:stick:download(attempts[8]):begin first poll
9608:INFO:stick:download(attempts[8],expect[142]):poll:
9609:INFO:stick:download(attempts[8],expect[142]):proceed to download_packet
9610:INFO:stick:download_packet:142
9641:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):adding segment
9642:INFO:stick:download(attempts[8],expect[142],results[1024]:data[128]):DONE
9926:INFO:session:sleeping 0.1 before download
9927:INFO:session:proceeding with download
9928:INFO:stick:download:start:0
9929:INFO:stick:download(attempts[1]):begin first poll
9978:INFO:stick:download(attempts[1],expect[78]):poll:
9979:INFO:stick:download(attempts[1],expect[78]):proceed to download_packet
9980:INFO:stick:download_packet:78
10003:INFO:stick:download(attempts[1],expect[78],results[64]:data[64]):adding segment
10004:INFO:stick:download(attempts[2]):begin first poll
10030:INFO:stick:download(attempts[2],expect[78]):poll:
10031:INFO:stick:download(attempts[2],expect[78]):proceed to download_packet
10032:INFO:stick:download_packet:78
10055:INFO:stick:download(attempts[2],expect[78],results[128]:data[64]):adding segment
10056:INFO:stick:download(attempts[3]):begin first poll
10151:INFO:stick:download(attempts[3],expect[0]):poll:
10152:INFO:stick:download found empty poll size, sleep 3 and try again
10178:INFO:stick:download(attempts[3],expect[718]):proceed to download_packet
10179:INFO:stick:download_packet:718
10282:WARNING:stick:bad zero CRC?
10283:INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0xf2:raw:
10554:INFO:stick:XXX:BadCRC:returning empty message instead of raising errors.
10555:INFO:stick:download(attempts[3],expect[718],results[128]:data[0]):no data, try again
10556:INFO:stick:download(attempts[4]):begin first poll
10582:INFO:stick:download(attempts[4],expect[78]):poll:
10583:INFO:stick:download(attempts[4],expect[78]):proceed to download_packet
10584:INFO:stick:download_packet:78
10607:INFO:stick:download(attempts[4],expect[78],results[192]:data[64]):adding segment
10608:INFO:stick:download(attempts[5]):begin first poll
10703:INFO:stick:download(attempts[5],expect[0]):poll:
10704:INFO:stick:download found empty poll size, sleep 3 and try again
10730:INFO:stick:download(attempts[5],expect[142]):proceed to download_packet
10731:INFO:stick:download_packet:142
10762:INFO:stick:download(attempts[5],expect[142],results[320]:data[128]):adding segment
10763:INFO:stick:download(attempts[5],expect[142],results[320]:data[128]):DONE
10863:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1061L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1061L, 'errors.crc': 0}
10881:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
10882:INFO:__main__:{'radio': {'errors.crc': 0,
10883:           'errors.naks': 0,
10884:           'errors.sequence': 8,
10885:           'errors.timeouts': 13,
10886:           'packets.received': 540L,
10887:           'packets.transmit': 582L},
10888: 'usb': {'errors.crc': 0,
10889:         'errors.naks': 0,
10890:         'errors.sequence': 0,
10891:         'errors.timeouts': 0,
10892:         'packets.received': 1061L,
10893:         'packets.transmit': 1061L}}
10894:INFO:__main__:howdy! we downloaded a lot of pump info successfully.
10900:Was there an ACK ERROR?
10901:### DIAGNOSE CRC
10902:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
11089:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1071L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1071L, 'errors.crc': 0}
11107:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
11108:INFO:__main__:{'radio': {'errors.crc': 0,
11109:           'errors.naks': 0,
11110:           'errors.sequence': 8,
11111:           'errors.timeouts': 13,
11112:           'packets.received': 540L,
11113:           'packets.transmit': 582L},
11114: 'usb': {'errors.crc': 0,
11115:         'errors.naks': 0,
11116:         'errors.sequence': 0,
11117:         'errors.timeouts': 0,
11118:         'packets.received': 1071L,
11119:         'packets.transmit': 1071L}}
11138:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1073L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1073L, 'errors.crc': 0}
11156:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
11158:{'radio': {'errors.crc': 0,
11159:           'errors.naks': 0,
11160:           'errors.sequence': 8,
11161:           'errors.timeouts': 13,
11162:           'packets.received': 540L,
11163:           'packets.transmit': 582L},
11164: 'usb': {'errors.crc': 0,
11165:         'errors.naks': 0,
11166:         'errors.sequence': 0,
11167:         'errors.timeouts': 0,
11168:         'packets.received': 1073L,
11169:         'packets.transmit': 1073L}}
11170:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
11265:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
11283:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1079L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1079L, 'errors.crc': 0}
11301:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
11302:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
11303:{'radio': {'errors.crc': 0,
11304:           'errors.naks': 0,
11305:           'errors.sequence': 8,
11306:           'errors.timeouts': 13,
11307:           'packets.received': 540L,
11308:           'packets.transmit': 582L},
11309: 'usb': {'errors.crc': 0,
11310:         'errors.naks': 0,
11311:         'errors.sequence': 0,
11312:         'errors.timeouts': 0,
11313:         'packets.received': 1079L,
11314:         'packets.transmit': 1079L}}
11334:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1081L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1081L, 'errors.crc': 0}
11352:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
11354:{'radio': {'errors.crc': 0,
11355:           'errors.naks': 0,
11356:           'errors.sequence': 8,
11357:           'errors.timeouts': 13,
11358:           'packets.received': 540L,
11359:           'packets.transmit': 582L},
11360: 'usb': {'errors.crc': 0,
11361:         'errors.naks': 0,
11362:         'errors.sequence': 0,
11363:         'errors.timeouts': 0,
11364:         'packets.received': 1081L,
11365:         'packets.transmit': 1081L}}
11366:INFO:__main__:howdy! all done looking at the stick
11372:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
11559:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1091L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1091L, 'errors.crc': 0}
11577:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
11578:INFO:__main__:{'radio': {'errors.crc': 0,
11579:           'errors.naks': 0,
11580:           'errors.sequence': 8,
11581:           'errors.timeouts': 13,
11582:           'packets.received': 540L,
11583:           'packets.transmit': 582L},
11584: 'usb': {'errors.crc': 0,
11585:         'errors.naks': 0,
11586:         'errors.sequence': 0,
11587:         'errors.timeouts': 0,
11588:         'packets.received': 1091L,
11589:         'packets.transmit': 1091L}}
11608:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1093L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1093L, 'errors.crc': 0}
11626:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
11628:{'radio': {'errors.crc': 0,
11629:           'errors.naks': 0,
11630:           'errors.sequence': 8,
11631:           'errors.timeouts': 13,
11632:           'packets.received': 540L,
11633:           'packets.transmit': 582L},
11634: 'usb': {'errors.crc': 0,
11635:         'errors.naks': 0,
11636:         'errors.sequence': 0,
11637:         'errors.timeouts': 0,
11638:         'packets.received': 1093L,
11639:         'packets.transmit': 1093L}}
11640:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
11735:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
11753:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1099L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1099L, 'errors.crc': 0}
11771:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
11772:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
11773:{'radio': {'errors.crc': 0,
11774:           'errors.naks': 0,
11775:           'errors.sequence': 8,
11776:           'errors.timeouts': 13,
11777:           'packets.received': 540L,
11778:           'packets.transmit': 582L},
11779: 'usb': {'errors.crc': 0,
11780:         'errors.naks': 0,
11781:         'errors.sequence': 0,
11782:         'errors.timeouts': 0,
11783:         'packets.received': 1099L,
11784:         'packets.transmit': 1099L}}
11804:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1101L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1101L, 'errors.crc': 0}
11822:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 13, 'packets.transmit': 582L, 'errors.naks': 0, 'errors.sequence': 8, 'packets.received': 540L, 'errors.crc': 0}
11824:{'radio': {'errors.crc': 0,
11825:           'errors.naks': 0,
11826:           'errors.sequence': 8,
11827:           'errors.timeouts': 13,
11828:           'packets.received': 540L,
11829:           'packets.transmit': 582L},
11830: 'usb': {'errors.crc': 0,
11831:         'errors.naks': 0,
11832:         'errors.sequence': 0,
11833:         'errors.timeouts': 0,
11834:         'packets.received': 1101L,
11835:         'packets.transmit': 1101L}}
11836:INFO:__main__:howdy! all done looking at the stick
```

* NO NAK FOUND
* NOT A CLEAN RUN
