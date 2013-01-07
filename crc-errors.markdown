
# What to do about CRC errors

Sometimes/often when dumping lots of pages from the ReadHistoryData
command, one of the segments will come back, passes most of the
validations for the ReadRadio ACK, but appears to be missing a CRC.

What should we do?

## After 3 or 4 runs

```bash
#!/bin/bash
# terser explanation of log
# Useful to tell what clear_buffer has been up to.

grep -n --color  -E "howdy|clear_bu|BAD|CRC|ACK|IGNORE|ReadHistory|traceback|critical|(errors|packets).(crc|naks|sequence|timeouts|received|transmit)" status-quo.log   

#####
# EOF
```

# Deal with it
```
17:  echo "Was there an ACK ERROR?"
18:  echo "### DIAGNOSE CRC"
27:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
214:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2499L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2497L, 'errors.crc': 0}
232:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1253L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1189L, 'errors.crc': 0}
233:INFO:__main__:{'radio': {'errors.crc': 0,
234:           'errors.naks': 0,
235:           'errors.sequence': 0,
236:           'errors.timeouts': 3,
237:           'packets.received': 1189L,
238:           'packets.transmit': 1253L},
239: 'usb': {'errors.crc': 0,
240:         'errors.naks': 2,
241:         'errors.sequence': 0,
242:         'errors.timeouts': 0,
243:         'packets.received': 2497L,
244:         'packets.transmit': 2499L}}
263:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2501L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2499L, 'errors.crc': 0}
281:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1253L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1189L, 'errors.crc': 0}
283:{'radio': {'errors.crc': 0,
284:           'errors.naks': 0,
285:           'errors.sequence': 0,
286:           'errors.timeouts': 3,
287:           'packets.received': 1189L,
288:           'packets.transmit': 1253L},
289: 'usb': {'errors.crc': 0,
290:         'errors.naks': 2,
291:         'errors.sequence': 0,
292:         'errors.timeouts': 0,
293:         'packets.received': 2499L,
294:         'packets.transmit': 2501L}}
295:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
390:INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 0
408:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2507L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2505L, 'errors.crc': 0}
426:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1253L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1189L, 'errors.crc': 0}
427:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
428:{'radio': {'errors.crc': 0,
429:           'errors.naks': 0,
430:           'errors.sequence': 0,
431:           'errors.timeouts': 3,
432:           'packets.received': 1189L,
433:           'packets.transmit': 1253L},
434: 'usb': {'errors.crc': 0,
435:         'errors.naks': 2,
436:         'errors.sequence': 0,
437:         'errors.timeouts': 0,
438:         'packets.received': 2505L,
439:         'packets.transmit': 2507L}}
459:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2509L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2507L, 'errors.crc': 0}
477:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1253L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1189L, 'errors.crc': 0}
479:{'radio': {'errors.crc': 0,
480:           'errors.naks': 0,
481:           'errors.sequence': 0,
482:           'errors.timeouts': 3,
483:           'packets.received': 1189L,
484:           'packets.transmit': 1253L},
485: 'usb': {'errors.crc': 0,
486:         'errors.naks': 2,
487:         'errors.sequence': 0,
488:         'errors.timeouts': 0,
489:         'packets.received': 2507L,
490:         'packets.transmit': 2509L}}
496:INFO:__main__:howdy! I'm going to take a look at your pump.
636:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2517L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2515L, 'errors.crc': 0}
654:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1253L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1189L, 'errors.crc': 0}
655:INFO:__main__:{'radio': {'errors.crc': 0,
656:           'errors.naks': 0,
657:           'errors.sequence': 0,
658:           'errors.timeouts': 3,
659:           'packets.received': 1189L,
660:           'packets.transmit': 1253L},
661: 'usb': {'errors.crc': 0,
662:         'errors.naks': 2,
663:         'errors.sequence': 0,
664:         'errors.timeouts': 0,
665:         'packets.received': 2515L,
666:         'packets.transmit': 2517L}}
740:WARNING:stick:bad zero CRC?
760:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2522L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2520L, 'errors.crc': 0}
778:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1255L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1191L, 'errors.crc': 0}
779:INFO:__main__:{'radio': {'errors.crc': 0,
780:           'errors.naks': 0,
781:           'errors.sequence': 0,
782:           'errors.timeouts': 3,
783:           'packets.received': 1191L,
784:           'packets.transmit': 1255L},
785: 'usb': {'errors.crc': 0,
786:         'errors.naks': 2,
787:         'errors.sequence': 0,
788:         'errors.timeouts': 0,
789:         'packets.received': 2520L,
790:         'packets.transmit': 2522L}}
905:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2528L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2526L, 'errors.crc': 0}
923:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1256L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1192L, 'errors.crc': 0}
924:INFO:__main__:{'radio': {'errors.crc': 0,
925:           'errors.naks': 0,
926:           'errors.sequence': 0,
927:           'errors.timeouts': 3,
928:           'packets.received': 1192L,
929:           'packets.transmit': 1256L},
930: 'usb': {'errors.crc': 0,
931:         'errors.naks': 2,
932:         'errors.sequence': 0,
933:         'errors.timeouts': 0,
934:         'packets.received': 2526L,
935:         'packets.transmit': 2528L}}
941:INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
1081:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2536L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2534L, 'errors.crc': 0}
1099:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1256L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1192L, 'errors.crc': 0}
1100:INFO:__main__:{'radio': {'errors.crc': 0,
1101:           'errors.naks': 0,
1102:           'errors.sequence': 0,
1103:           'errors.timeouts': 3,
1104:           'packets.received': 1192L,
1105:           'packets.transmit': 1256L},
1106: 'usb': {'errors.crc': 0,
1107:         'errors.naks': 2,
1108:         'errors.sequence': 0,
1109:         'errors.timeouts': 0,
1110:         'packets.received': 2534L,
1111:         'packets.transmit': 2536L}}
2460:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][0]>
2461:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> processing TransmitPacket:ReadHistoryData[page][0])
2463:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> sending TransmitPacket:ReadHistoryData[page][0])
2481:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xcf\x80@\xa7\x01 \x88P\xb4\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
2484:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:STARTING POLL PHASE:attempt:0
2485:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:poll:attempt:0
2675:WARNING:stick:bad zero CRC?
2732:WARNING:stick:bad zero CRC?
2789:WARNING:stick:bad zero CRC?
2846:WARNING:stick:bad zero CRC?
2903:WARNING:stick:bad zero CRC?
3235:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2608L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2606L, 'errors.crc': 0}
3253:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1287L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1222L, 'errors.crc': 0}
3254:INFO:__main__:{'radio': {'errors.crc': 0,
3255:           'errors.naks': 0,
3256:           'errors.sequence': 0,
3257:           'errors.timeouts': 3,
3258:           'packets.received': 1222L,
3259:           'packets.transmit': 1287L},
3260: 'usb': {'errors.crc': 0,
3261:         'errors.naks': 2,
3262:         'errors.sequence': 0,
3263:         'errors.timeouts': 0,
3264:         'packets.received': 2606L,
3265:         'packets.transmit': 2608L}}
3376:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][0]>
3377:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> processing TransmitPacket:ReadHistoryData[page][0])
3379:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> sending TransmitPacket:ReadHistoryData[page][0])
3397:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xcf\x80@\xa7\x01 \x88P\xb4\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
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
4158:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][1], bytearray(b'\x00\xcf\x80\x80\xa7\x01 \x88P\xf1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
4161:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]>>:STARTING POLL PHASE:attempt:0
4162:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]>>:poll:attempt:0
4893:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][2]>
4894:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]> processing TransmitPacket:ReadHistoryData[page][2])
4896:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]> sending TransmitPacket:ReadHistoryData[page][2])
4914:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][2], bytearray(b'\x00\xcf\x80\x80\xa7\x01 \x88P\xf1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x92\x9e\x0b\x01\x06\x07\x00\x00\x02L\xa1\x06l\xa1\x06\x05\x0c\x00\xe8\x00\x00\x00\x00\x02L\x02Ld\x00\x00\x00\x00\x00\x00\x00\x00\x00')
4917:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]>>:STARTING POLL PHASE:attempt:0
4918:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]>>:poll:attempt:0
5649:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][3]>
5650:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]> processing TransmitPacket:ReadHistoryData[page][3])
5652:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]> sending TransmitPacket:ReadHistoryData[page][3])
5670:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][3], bytearray(b'\x00\xcf\x80\x80\xa7\x01 \x88P\xf1\x04\xda\x82\x0cl\x82\x0c\x05\x00edf\x12\x00\x00\x04\xda\x03\x9eK\x01<\x19\x00O\x01<\x19\x01<d\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x00d\x01V\xca\x06\x01\x06\x17\x00')
5673:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]>>:STARTING POLL PHASE:attempt:0
5674:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]>>:poll:attempt:0
6405:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][4]>
6406:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][4]> processing TransmitPacket:ReadHistoryData[page][4])
6408:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][4]> sending TransmitPacket:ReadHistoryData[page][4])
6426:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][4], bytearray(b'\x00\xcf\x80\x80\xa7\x01 \x88P\xf1\x01\x12\x17\x00\x9f\x08\x14\x01\x12\x18\x00\x80\x08\x14\x01\x0c\x07\x00\x00\x00\x06\x81\x12l\x81\x12\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x06\x00\x06d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
6429:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][4]>>:STARTING POLL PHASE:attempt:0
6430:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][4]>>:poll:attempt:0
7161:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][5]>
7162:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]> processing TransmitPacket:ReadHistoryData[page][5])
7164:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]> sending TransmitPacket:ReadHistoryData[page][5])
7182:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][5], bytearray(b'\x00\xcf\x80\x80\xa7\x01 \x88P\xf1\x00\x02\x00!\x00l!\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x02\x00\x02\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x0c\x9c\x13\x02\x00\x17')
7185:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]>>:STARTING POLL PHASE:attempt:0
7186:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]>>:poll:attempt:0
7917:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][6]>
7918:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][6]> processing TransmitPacket:ReadHistoryData[page][6])
7920:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][6]> sending TransmitPacket:ReadHistoryData[page][6])
7938:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][6], bytearray(b'\x00\xcf\x80\x80\xa7\x01 \x88P\xf1\x00\x00,\x00l,\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00-\x00l-')
7941:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][6]>>:STARTING POLL PHASE:attempt:0
7942:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][6]>>:poll:attempt:0
8673:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][7]>
8674:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][7]> processing TransmitPacket:ReadHistoryData[page][7])
8676:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][7]> sending TransmitPacket:ReadHistoryData[page][7])
8694:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][7], bytearray(b'\x00\xcf\x80\x80\xa7\x01 \x88P\xf1\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x15\x80l\x15\x80\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07')
8697:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][7]>>:STARTING POLL PHASE:attempt:0
8698:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][7]>>:poll:attempt:0
8832:INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x60:expected_crc(data): 0x9c:raw:
8925:    raise BadCRC(msg)
8926:stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x60:expected_crc(data): 0x9c:raw:
9011:Was there an ACK ERROR?
9012:### DIAGNOSE CRC
9013:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
9200:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2754L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2752L, 'errors.crc': 0}
9218:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1424L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1351L, 'errors.crc': 0}
9219:INFO:__main__:{'radio': {'errors.crc': 0,
9220:           'errors.naks': 0,
9221:           'errors.sequence': 0,
9222:           'errors.timeouts': 3,
9223:           'packets.received': 1351L,
9224:           'packets.transmit': 1424L},
9225: 'usb': {'errors.crc': 0,
9226:         'errors.naks': 2,
9227:         'errors.sequence': 0,
9228:         'errors.timeouts': 0,
9229:         'packets.received': 2752L,
9230:         'packets.transmit': 2754L}}
9249:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2756L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2754L, 'errors.crc': 0}
9267:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1424L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1352L, 'errors.crc': 0}
9269:{'radio': {'errors.crc': 0,
9270:           'errors.naks': 0,
9271:           'errors.sequence': 0,
9272:           'errors.timeouts': 3,
9273:           'packets.received': 1352L,
9274:           'packets.transmit': 1424L},
9275: 'usb': {'errors.crc': 0,
9276:         'errors.naks': 2,
9277:         'errors.sequence': 0,
9278:         'errors.timeouts': 0,
9279:         'packets.received': 2754L,
9280:         'packets.transmit': 2756L}}
9281:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
9307:INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 334
9308:INFO:__main__:XXX:clear_buffer[attempt][0]:download the size? 334:segments[0],total_segments[0]:raw[0]
9309:INFO:__main__:XXX:clear_buffer[attempt][0] size:334:segments[0],total_segments[0]:raw[0]:clear_buffer BUFFER self.download( )
9566:INFO:__main__:XXX:clear_buffer[attempt][0]:tx:found:segments[1],total_segments[768]:raw[768]:len(raw):768:expected:334:len(segment):768
9567:INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 768 segment:segments[1],total_segments[768]:raw[768]:RAW:
9775:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2771L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2769L, 'errors.crc': 0}
9793:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1432L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1359L, 'errors.crc': 0}
9795:{'radio': {'errors.crc': 0,
9796:           'errors.naks': 0,
9797:           'errors.sequence': 0,
9798:           'errors.timeouts': 3,
9799:           'packets.received': 1359L,
9800:           'packets.transmit': 1432L},
9801: 'usb': {'errors.crc': 0,
9802:         'errors.naks': 2,
9803:         'errors.sequence': 0,
9804:         'errors.timeouts': 0,
9805:         'packets.received': 2769L,
9806:         'packets.transmit': 2771L}}
9921:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2773L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2771L, 'errors.crc': 0}
9939:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1432L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1359L, 'errors.crc': 0}
9941:{'radio': {'errors.crc': 0,
9942:           'errors.naks': 0,
9943:           'errors.sequence': 0,
9944:           'errors.timeouts': 3,
9945:           'packets.received': 1359L,
9946:           'packets.transmit': 1432L},
9947: 'usb': {'errors.crc': 0,
9948:         'errors.naks': 2,
9949:         'errors.sequence': 0,
9950:         'errors.timeouts': 0,
9951:         'packets.received': 2771L,
9952:         'packets.transmit': 2773L}}
9958:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
10145:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2783L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2781L, 'errors.crc': 0}
10163:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1432L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1359L, 'errors.crc': 0}
10164:INFO:__main__:{'radio': {'errors.crc': 0,
10165:           'errors.naks': 0,
10166:           'errors.sequence': 0,
10167:           'errors.timeouts': 3,
10168:           'packets.received': 1359L,
10169:           'packets.transmit': 1432L},
10170: 'usb': {'errors.crc': 0,
10171:         'errors.naks': 2,
10172:         'errors.sequence': 0,
10173:         'errors.timeouts': 0,
10174:         'packets.received': 2781L,
10175:         'packets.transmit': 2783L}}
10194:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2785L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2783L, 'errors.crc': 0}
10212:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1432L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1359L, 'errors.crc': 0}
10214:{'radio': {'errors.crc': 0,
10215:           'errors.naks': 0,
10216:           'errors.sequence': 0,
10217:           'errors.timeouts': 3,
10218:           'packets.received': 1359L,
10219:           'packets.transmit': 1432L},
10220: 'usb': {'errors.crc': 0,
10221:         'errors.naks': 2,
10222:         'errors.sequence': 0,
10223:         'errors.timeouts': 0,
10224:         'packets.received': 2783L,
10225:         'packets.transmit': 2785L}}
10226:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
10321:INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 0
10339:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2791L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2789L, 'errors.crc': 0}
10357:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1432L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1359L, 'errors.crc': 0}
10358:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
10359:{'radio': {'errors.crc': 0,
10360:           'errors.naks': 0,
10361:           'errors.sequence': 0,
10362:           'errors.timeouts': 3,
10363:           'packets.received': 1359L,
10364:           'packets.transmit': 1432L},
10365: 'usb': {'errors.crc': 0,
10366:         'errors.naks': 2,
10367:         'errors.sequence': 0,
10368:         'errors.timeouts': 0,
10369:         'packets.received': 2789L,
10370:         'packets.transmit': 2791L}}
10390:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2793L, 'errors.naks': 2, 'errors.sequence': 0, 'packets.received': 2791L, 'errors.crc': 0}
10408:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1432L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1359L, 'errors.crc': 0}
10410:{'radio': {'errors.crc': 0,
10411:           'errors.naks': 0,
10412:           'errors.sequence': 0,
10413:           'errors.timeouts': 3,
10414:           'packets.received': 1359L,
10415:           'packets.transmit': 1432L},
10416: 'usb': {'errors.crc': 0,
10417:         'errors.naks': 2,
10418:         'errors.sequence': 0,
10419:         'errors.timeouts': 0,
10420:         'packets.received': 2791L,
10421:         'packets.transmit': 2793L}}
```
