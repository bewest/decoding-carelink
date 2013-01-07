
# status-quo

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


More often than not it will fail during downloading the memory dump
with a CRC error.
I'm still working out how to work around this feature of the protocol
automatically.
You can rerun the commands step yourself a few times and it may or may
not go through without CRC errors.

## Terser explanation

```bash
#!/bin/bash
# terser explanation of log
# Useful to tell what clear_buffer has been up to.

grep -n --color  -E "howdy|clear_bu|BAD|CRC|ACK|IGNORE|ReadHistory|traceback|critical|(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" status-quo.log   

#####
# EOF
```

When it's more obvious that clear_buffer works, I'll use that logic
instead of the current download logic.

I want to catch it incrementing the received counters just right again
before doing so.

What I'd like to see in the explain log is lines showing commands.py
failing during download_packet with a BadCRC, stick.py picking it back
up, with attempts of running the clear_buffer method incrementing the
counters as expected.
Sometimes this works, but more consistently now I seem to be getting
NAK after these runs.

```bash
#/bin/bash
# make an example of an interesting log worth sharing

export TIME="%C\n\telapsed %E\n\tuser %U\n\tsystem %S\n\tCPU %P (%Xtext+%Ddata %Mmax)k"

CMD="$*"
NAME=$0
PORT=${1-'/dev/ttyUSB0'}
SERIAL=${2-'208850'}

( cat $NAME
  echo "# ${NAME} ${CMD}"
  date
  TIME="$TIME" time python pump/stick.py ${PORT}
  TIME="$TIME" time python pump/session.py ${PORT} ${SERIAL}
  TIME="$TIME" time python pump/commands.py ${PORT} ${SERIAL}
  echo "Was there an ACK ERROR?"
  echo "### DIAGNOSE CRC"
  TIME="$TIME" time -f "$TIME" python pump/stick.py ${PORT}
  TIME="$TIME" time -f "$TIME" python pump/stick.py ${PORT}
) 2>&1 | tee status-quo.log

#####
# EOF
```

## Should have 8 pages of ReadHistoryData, no CRC errors, no NAK
```
17:  echo "Was there an ACK ERROR?"
18:  echo "### DIAGNOSE CRC"
27:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
214:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 979L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 979L, 'errors.crc': 0}
232:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 539L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 510L, 'errors.crc': 0}
233:INFO:__main__:{'radio': {'errors.crc': 0,
234:           'errors.naks': 0,
235:           'errors.sequence': 0,
236:           'errors.timeouts': 2,
237:           'packets.received': 510L,
238:           'packets.transmit': 539L},
239: 'usb': {'errors.crc': 0,
240:         'errors.naks': 0,
241:         'errors.sequence': 0,
242:         'errors.timeouts': 0,
243:         'packets.received': 979L,
244:         'packets.transmit': 979L}}
263:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 981L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 981L, 'errors.crc': 0}
281:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 539L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 510L, 'errors.crc': 0}
283:{'radio': {'errors.crc': 0,
284:           'errors.naks': 0,
285:           'errors.sequence': 0,
286:           'errors.timeouts': 2,
287:           'packets.received': 510L,
288:           'packets.transmit': 539L},
289: 'usb': {'errors.crc': 0,
290:         'errors.naks': 0,
291:         'errors.sequence': 0,
292:         'errors.timeouts': 0,
293:         'packets.received': 981L,
294:         'packets.transmit': 981L}}
295:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
390:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
408:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 987L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 987L, 'errors.crc': 0}
426:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 539L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 510L, 'errors.crc': 0}
427:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
428:{'radio': {'errors.crc': 0,
429:           'errors.naks': 0,
430:           'errors.sequence': 0,
431:           'errors.timeouts': 2,
432:           'packets.received': 510L,
433:           'packets.transmit': 539L},
434: 'usb': {'errors.crc': 0,
435:         'errors.naks': 0,
436:         'errors.sequence': 0,
437:         'errors.timeouts': 0,
438:         'packets.received': 987L,
439:         'packets.transmit': 987L}}
459:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 989L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 989L, 'errors.crc': 0}
477:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 539L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 510L, 'errors.crc': 0}
479:{'radio': {'errors.crc': 0,
480:           'errors.naks': 0,
481:           'errors.sequence': 0,
482:           'errors.timeouts': 2,
483:           'packets.received': 510L,
484:           'packets.transmit': 539L},
485: 'usb': {'errors.crc': 0,
486:         'errors.naks': 0,
487:         'errors.sequence': 0,
488:         'errors.timeouts': 0,
489:         'packets.received': 989L,
490:         'packets.transmit': 989L}}
496:INFO:__main__:howdy! I'm going to take a look at your pump.
636:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 997L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 997L, 'errors.crc': 0}
654:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 539L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 510L, 'errors.crc': 0}
655:INFO:__main__:{'radio': {'errors.crc': 0,
656:           'errors.naks': 0,
657:           'errors.sequence': 0,
658:           'errors.timeouts': 2,
659:           'packets.received': 510L,
660:           'packets.transmit': 539L},
661: 'usb': {'errors.crc': 0,
662:         'errors.naks': 0,
663:         'errors.sequence': 0,
664:         'errors.timeouts': 0,
665:         'packets.received': 997L,
666:         'packets.transmit': 997L}}
740:WARNING:stick:bad zero CRC?
760:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1002L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1002L, 'errors.crc': 0}
778:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 541L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 512L, 'errors.crc': 0}
779:INFO:__main__:{'radio': {'errors.crc': 0,
780:           'errors.naks': 0,
781:           'errors.sequence': 0,
782:           'errors.timeouts': 2,
783:           'packets.received': 512L,
784:           'packets.transmit': 541L},
785: 'usb': {'errors.crc': 0,
786:         'errors.naks': 0,
787:         'errors.sequence': 0,
788:         'errors.timeouts': 0,
789:         'packets.received': 1002L,
790:         'packets.transmit': 1002L}}
905:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1008L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1008L, 'errors.crc': 0}
923:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 542L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 513L, 'errors.crc': 0}
924:INFO:__main__:{'radio': {'errors.crc': 0,
925:           'errors.naks': 0,
926:           'errors.sequence': 0,
927:           'errors.timeouts': 2,
928:           'packets.received': 513L,
929:           'packets.transmit': 542L},
930: 'usb': {'errors.crc': 0,
931:         'errors.naks': 0,
932:         'errors.sequence': 0,
933:         'errors.timeouts': 0,
934:         'packets.received': 1008L,
935:         'packets.transmit': 1008L}}
941:INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
1081:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1016L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1016L, 'errors.crc': 0}
1099:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 542L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 513L, 'errors.crc': 0}
1100:INFO:__main__:{'radio': {'errors.crc': 0,
1101:           'errors.naks': 0,
1102:           'errors.sequence': 0,
1103:           'errors.timeouts': 2,
1104:           'packets.received': 513L,
1105:           'packets.transmit': 542L},
1106: 'usb': {'errors.crc': 0,
1107:         'errors.naks': 0,
1108:         'errors.sequence': 0,
1109:         'errors.timeouts': 0,
1110:         'packets.received': 1016L,
1111:         'packets.transmit': 1016L}}
2460:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][0]>
2461:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> processing TransmitPacket:ReadHistoryData[page][0])
2463:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> sending TransmitPacket:ReadHistoryData[page][0])
2481:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xc9\x80@\xa7\x01 \x88P\xcc\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
2484:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:STARTING POLL PHASE:attempt:0
2485:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:poll:attempt:0
2675:WARNING:stick:bad zero CRC?
2732:WARNING:stick:bad zero CRC?
2789:WARNING:stick:bad zero CRC?
2846:WARNING:stick:bad zero CRC?
2903:WARNING:stick:bad zero CRC?
3235:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1088L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1088L, 'errors.crc': 0}
3253:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 2, 'packets.transmit': 573L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 543L, 'errors.crc': 0}
3254:INFO:__main__:{'radio': {'errors.crc': 0,
3255:           'errors.naks': 0,
3256:           'errors.sequence': 0,
3257:           'errors.timeouts': 2,
3258:           'packets.received': 543L,
3259:           'packets.transmit': 573L},
3260: 'usb': {'errors.crc': 0,
3261:         'errors.naks': 0,
3262:         'errors.sequence': 0,
3263:         'errors.timeouts': 0,
3264:         'packets.received': 1088L,
3265:         'packets.transmit': 1088L}}
3376:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][0]>
3377:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> processing TransmitPacket:ReadHistoryData[page][0])
3379:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> sending TransmitPacket:ReadHistoryData[page][0])
3397:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xc9\x80@\xa7\x01 \x88P\xcc\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
3400:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:STARTING POLL PHASE:attempt:0
3401:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:poll:attempt:0
3591:WARNING:stick:bad zero CRC?
3648:WARNING:stick:bad zero CRC?
3705:WARNING:stick:bad zero CRC?
3762:WARNING:stick:bad zero CRC?
3819:WARNING:stick:bad zero CRC?
4137:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][1]>
4138:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]> processing TransmitPacket:ReadHistoryData[page][1])
4140:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]> sending TransmitPacket:ReadHistoryData[page][1])
4158:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][1], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
4161:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]>>:STARTING POLL PHASE:attempt:0
4162:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]>>:poll:attempt:0
4893:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][2]>
4894:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]> processing TransmitPacket:ReadHistoryData[page][2])
4896:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]> sending TransmitPacket:ReadHistoryData[page][2])
4914:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][2], bytearray(b'\x00\xc9\x80\x80\xa7\x01 \x88P\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x92\x9e\x0b\x01\x06\x07\x00\x00\x02L\xa1\x06l\xa1\x06\x05\x0c\x00\xe8\x00\x00\x00\x00\x02L\x02Ld\x00\x00\x00\x00\x00\x00\x00\x00\x00')
4917:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]>>:STARTING POLL PHASE:attempt:0
4918:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]>>:poll:attempt:0
5649:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][3]>
5650:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]> processing TransmitPacket:ReadHistoryData[page][3])
5652:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]> sending TransmitPacket:ReadHistoryData[page][3])
5670:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][3], bytearray(b'\x00\xc9\x80\x80\xa7\x01 \x88P\x89\x04\xda\x82\x0cl\x82\x0c\x05\x00edf\x12\x00\x00\x04\xda\x03\x9eK\x01<\x19\x00O\x01<\x19\x01<d\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x00d\x01V\xca\x06\x01\x06\x17\x00')
5673:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]>>:STARTING POLL PHASE:attempt:0
5674:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]>>:poll:attempt:0
6112:WARNING:stick:bad zero CRC?
6278:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][4]>
6279:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(14)>:command:<TransmitPacket:ReadHistoryData[page][4]> processing TransmitPacket:ReadHistoryData[page][4])
6281:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(14)>:command:<TransmitPacket:ReadHistoryData[page][4]> sending TransmitPacket:ReadHistoryData[page][4])
6299:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][4], bytearray(b'\x02\x00\x80\x00\xa7\x01 \x88Pf\x00\x00\x03d\\\x05\x0c\x03D\x01\x03\x03\x00X\xee%\t\x05\x07\x00\x00\x03Ni\x85li\x85\x05\x00dde\x04\x00\x00\x03N\x036a\x00\x18\x03\x00\x06\x00\x18\x03\x00\x18')
6302:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(14)>:command:<TransmitPacket:ReadHistoryData[page][4]>>:STARTING POLL PHASE:attempt:0
6303:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(14)>:command:<TransmitPacket:ReadHistoryData[page][4]>>:poll:attempt:0
7034:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][5]>
7035:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]> processing TransmitPacket:ReadHistoryData[page][5])
7037:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]> sending TransmitPacket:ReadHistoryData[page][5])
7055:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][5], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x00\x02\x00!\x00l!\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x02\x00\x02\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x0c\x9c\x13\x02\x00\x17')
7058:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]>>:STARTING POLL PHASE:attempt:0
7059:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]>>:poll:attempt:0
7790:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][6]>
7791:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][6]> processing TransmitPacket:ReadHistoryData[page][6])
7793:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][6]> sending TransmitPacket:ReadHistoryData[page][6])
7811:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][6], bytearray(b'\x00\xca\x80\x80\xa7\x01 \x88P\xb5\x00\x00,\x00l,\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00-\x00l-')
7814:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][6]>>:STARTING POLL PHASE:attempt:0
7815:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][6]>>:poll:attempt:0
8546:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][7]>
8547:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][7]> processing TransmitPacket:ReadHistoryData[page][7])
8549:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][7]> sending TransmitPacket:ReadHistoryData[page][7])
8567:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][7], bytearray(b'\x00\xc9\x80\x80\xa7\x01 \x88P\x89\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x15\x80l\x15\x80\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07')
8570:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][7]>>:STARTING POLL PHASE:attempt:0
8571:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][7]>>:poll:attempt:0
9302:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][8]>
9303:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][8]> processing TransmitPacket:ReadHistoryData[page][8])
9305:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][8]> sending TransmitPacket:ReadHistoryData[page][8])
9323:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][8], bytearray(b'\x00\xc9\x80\x80\xa7\x01 \x88P\x89\x1f\x00)C\x04A\x00\x07\x00\x00\x04\xcc\x01\x80l\x01\x80\x05\x00ddd\x0b\x00\x00\x04\xcc\x03\xbeN\x01\x0e\x16\x00A\x01\x0e\x16\x01\x04`\x00\x00\x00\x00\n\x04\x0c\x0b\x00\x00')
9326:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][8]>>:STARTING POLL PHASE:attempt:0
9327:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][8]>>:poll:attempt:0
10072:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1256L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1256L, 'errors.crc': 0}
10090:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
10091:INFO:__main__:{'radio': {'errors.crc': 0,
10092:           'errors.naks': 0,
10093:           'errors.sequence': 2,
10094:           'errors.timeouts': 3,
10095:           'packets.received': 693L,
10096:           'packets.transmit': 732L},
10097: 'usb': {'errors.crc': 0,
10098:         'errors.naks': 0,
10099:         'errors.sequence': 0,
10100:         'errors.timeouts': 0,
10101:         'packets.received': 1256L,
10102:         'packets.transmit': 1256L}}
10108:Was there an ACK ERROR?
10109:### DIAGNOSE CRC
10110:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
10297:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1266L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1266L, 'errors.crc': 0}
10315:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
10316:INFO:__main__:{'radio': {'errors.crc': 0,
10317:           'errors.naks': 0,
10318:           'errors.sequence': 2,
10319:           'errors.timeouts': 3,
10320:           'packets.received': 693L,
10321:           'packets.transmit': 732L},
10322: 'usb': {'errors.crc': 0,
10323:         'errors.naks': 0,
10324:         'errors.sequence': 0,
10325:         'errors.timeouts': 0,
10326:         'packets.received': 1266L,
10327:         'packets.transmit': 1266L}}
10346:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1268L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1268L, 'errors.crc': 0}
10364:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
10366:{'radio': {'errors.crc': 0,
10367:           'errors.naks': 0,
10368:           'errors.sequence': 2,
10369:           'errors.timeouts': 3,
10370:           'packets.received': 693L,
10371:           'packets.transmit': 732L},
10372: 'usb': {'errors.crc': 0,
10373:         'errors.naks': 0,
10374:         'errors.sequence': 0,
10375:         'errors.timeouts': 0,
10376:         'packets.received': 1268L,
10377:         'packets.transmit': 1268L}}
10378:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
10473:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
10491:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1274L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1274L, 'errors.crc': 0}
10509:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
10510:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
10511:{'radio': {'errors.crc': 0,
10512:           'errors.naks': 0,
10513:           'errors.sequence': 2,
10514:           'errors.timeouts': 3,
10515:           'packets.received': 693L,
10516:           'packets.transmit': 732L},
10517: 'usb': {'errors.crc': 0,
10518:         'errors.naks': 0,
10519:         'errors.sequence': 0,
10520:         'errors.timeouts': 0,
10521:         'packets.received': 1274L,
10522:         'packets.transmit': 1274L}}
10542:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1276L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1276L, 'errors.crc': 0}
10560:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
10562:{'radio': {'errors.crc': 0,
10563:           'errors.naks': 0,
10564:           'errors.sequence': 2,
10565:           'errors.timeouts': 3,
10566:           'packets.received': 693L,
10567:           'packets.transmit': 732L},
10568: 'usb': {'errors.crc': 0,
10569:         'errors.naks': 0,
10570:         'errors.sequence': 0,
10571:         'errors.timeouts': 0,
10572:         'packets.received': 1276L,
10573:         'packets.transmit': 1276L}}
10579:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
10766:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1286L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1286L, 'errors.crc': 0}
10784:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
10785:INFO:__main__:{'radio': {'errors.crc': 0,
10786:           'errors.naks': 0,
10787:           'errors.sequence': 2,
10788:           'errors.timeouts': 3,
10789:           'packets.received': 693L,
10790:           'packets.transmit': 732L},
10791: 'usb': {'errors.crc': 0,
10792:         'errors.naks': 0,
10793:         'errors.sequence': 0,
10794:         'errors.timeouts': 0,
10795:         'packets.received': 1286L,
10796:         'packets.transmit': 1286L}}
10815:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1288L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1288L, 'errors.crc': 0}
10833:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
10835:{'radio': {'errors.crc': 0,
10836:           'errors.naks': 0,
10837:           'errors.sequence': 2,
10838:           'errors.timeouts': 3,
10839:           'packets.received': 693L,
10840:           'packets.transmit': 732L},
10841: 'usb': {'errors.crc': 0,
10842:         'errors.naks': 0,
10843:         'errors.sequence': 0,
10844:         'errors.timeouts': 0,
10845:         'packets.received': 1288L,
10846:         'packets.transmit': 1288L}}
10847:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
10942:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:END first poll 0:SHOULD DOWNLOAD :False
10960:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1294L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1294L, 'errors.crc': 0}
10978:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
10979:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
10980:{'radio': {'errors.crc': 0,
10981:           'errors.naks': 0,
10982:           'errors.sequence': 2,
10983:           'errors.timeouts': 3,
10984:           'packets.received': 693L,
10985:           'packets.transmit': 732L},
10986: 'usb': {'errors.crc': 0,
10987:         'errors.naks': 0,
10988:         'errors.sequence': 0,
10989:         'errors.timeouts': 0,
10990:         'packets.received': 1294L,
10991:         'packets.transmit': 1294L}}
11011:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1296L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1296L, 'errors.crc': 0}
11029:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 732L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 693L, 'errors.crc': 0}
11031:{'radio': {'errors.crc': 0,
11032:           'errors.naks': 0,
11033:           'errors.sequence': 2,
11034:           'errors.timeouts': 3,
11035:           'packets.received': 693L,
11036:           'packets.transmit': 732L},
11037: 'usb': {'errors.crc': 0,
11038:         'errors.naks': 0,
11039:         'errors.sequence': 0,
11040:         'errors.timeouts': 0,
11041:         'packets.received': 1296L,
11042:         'packets.transmit': 1296L}}
```
