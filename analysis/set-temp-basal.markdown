hi Namespace(duration=0, port='/dev/ttyUSB.Carelink0', rate=0, serial='208850')
INFO:decocare.link:Link opened serial port: Serial<id=0x7f9dc4b51dd0, open=True>(port='/dev/ttyUSB.Carelink0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.4, xonxoff=False, rtscts=False, dsrdtr=False)
INFO:decocare.stick:PROCESS:OPEN:0.007
INFO:decocare.stick:PROCESS:START:0.058:ProductInfo:0x04
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<ProductInfo:0x04:size(64)>] processing ProductInfo:0x04)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<ProductInfo:0x04:size(64)>] sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0c 0x17 0x00 0x00 0x00    .U......
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0c1700'}
INFO:decocare.stick:PROCESS:END:2.658:ProductInfo:0x04
INFO:decocare.stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0c1700'}
INFO:decocare.stick:PROCESS:START:2.817:ProductInfo:0x04
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<ProductInfo:0x04:size(64)>] processing ProductInfo:0x04)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<ProductInfo:0x04:size(64)>] sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0c 0x17 0x00 0x00 0x00    .U......
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0c1700'}
INFO:decocare.stick:PROCESS:END:5.051:ProductInfo:0x04
INFO:decocare.stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0c1700'}
INFO:decocare.stick:get signal strength of Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<ProductInfo:0x04:size(64)>]
INFO:decocare.stick:PROCESS:START:5.299:SignalStrength:0x06 0x00
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<SignalStrength:0x06 0x00:size(64)>] processing SignalStrength:0x06 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<SignalStrength:0x06 0x00:size(64)>] sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc2 0x17 0x00 0x00 0x00    .U......
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:194
INFO:decocare.stick:finished processing SignalStrength:0x06 0x00, 194
INFO:decocare.stick:PROCESS:END:7.4:SignalStrength:0x06 0x00
INFO:decocare.stick:we seem to have found a nice signal strength of: 194
INFO:decocare.session:setting up to talk with 208850
INFO:decocare.stick:PROCESS:START:7.577:UsbStats:0x05 0x01
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<UsbStats:0x05 0x01:size(64)>] processing UsbStats:0x05 0x01)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<UsbStats:0x05 0x01:size(64)>] sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x01 0x4f 0x00 0x00 0x01 0x4f 0x01    ..O...O.
0010   0x50 0x01 0x52 0x01 0x4f 0x04 0x00 0x00    P.R.O...
0018   0x05 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 335L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 335L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:9.494:UsbStats:0x05 0x01
INFO:decocare.stick:PROCESS:START:9.56:RadioStats:0x05 0x00
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<RadioStats:0x05 0x00:size(64)>] processing RadioStats:0x05 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<RadioStats:0x05 0x00:size(64)>] sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x03 0x00    .U......
0008   0x00 0x00 0x3d 0x00 0x00 0x00 0x42 0x00    ..=...B.
0010   0x00 0x00 0x17 0x00 0x14 0x00 0x20 0x00    ...... .
0018   0x29 0x00 0x0b 0x00 0x00 0x00 0x00 0x00    ).......
0020   0x00 0x01 0x00 0xc4 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 66L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 61L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:11.471:RadioStats:0x05 0x00
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 3,
           'packets.received': 61L,
           'packets.transmit': 66L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 335L,
         'packets.transmit': 335L}}
INFO:decocare.session:execute attempt: 1
INFO:decocare.session:session transferring packet
INFO:decocare.stick:transmit_packet:write:<TransmitPacket:ReadPumpModel:data:unknown>
INFO:decocare.stick:PROCESS:START:12.335:TransmitPacket:ReadPumpModel:data:unknown
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<TransmitPacket:ReadPumpModel:data:unknown>] processing TransmitPacket:ReadPumpModel:data:unknown)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<TransmitPacket:ReadPumpModel:data:unknown>] sending TransmitPacket:ReadPumpModel:data:unknown)
DEBUG:decocare.stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 141, 199, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x8d 0xc7 0x00    ........
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x03 0x00    .U......
0008   0x00 0x00 0x3d 0x00 0x00 0x00 0x42 0x00    ..=...B.
0010   0x00 0x00 0x17 0x00 0x14 0x00 0x20 0x00    ...... .
0018   0x29 0x00 0x0b 0x00 0x00 0x00 0x00 0x00    ).......
0020   0x00 0x01 0x00 0xc4 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing TransmitPacket:ReadPumpModel:data:unknown, bytearray(b'\x00\x00\x00\x03\x00\x00\x00=\x00\x00\x00B\x00\x00\x00\x17\x00\x14\x00 \x00)\x00\x0b\x00\x00\x00\x00\x00\x00\x01\x00\xc4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:decocare.stick:PROCESS:END:14.794:TransmitPacket:ReadPumpModel:data:unknown
INFO:decocare.session:sleeping 0.5 before download
INFO:decocare.session:proceeding with download
INFO:decocare.stick:download:start:0
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[None] poll_i[None] command[<TransmitPacket:ReadPumpModel:data:unknown>]:download(attempts[1],expect[0],results[0]:data[0]):begin first poll first sleep .250
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[None] poll_i[None] command[<TransmitPacket:ReadPumpModel:data:unknown>]>:STARTING POLL PHASE:attempt:0
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<TransmitPacket:ReadPumpModel:data:unknown>]>:poll:attempt:0
INFO:decocare.stick:PROCESS:START:766.607:LinkStatus:0x03:status:size=64
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] processing LinkStatus:0x03:status:size=64)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] sending LinkStatus:0x03:status:size=64)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x42 0x00    ......B.
0010   0x00 0x00 0x17 0x00 0x14 0x00 0x20 0x00    ...... .
0018   0x29 0x00 0x0b 0x00 0x00 0x00 0x00 0x00    ).......
0020   0x00 0x01 0x00 0xc4 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:LinkStatus:0x03:status:size=78

INFO:decocare.stick:finished processing LinkStatus:0x03:status:size=78, 78
INFO:decocare.stick:PROCESS:END:768.818:LinkStatus:0x03:status:size=78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[0] command[<LinkStatus:0x03:status:size=78:size(78)>]:STOP POLL after 1 attempts:size:78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download(attempts[1],expect[78],results[0]:data[0]):end first poll
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download(attempts[1],expect[78],results[0]:data[0]):proceed to download packet
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download_packet:78
INFO:decocare.stick:PROCESS:START:769.271:ReadRadio:size:78
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>] sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc8 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x51 0x03 0x35 0x31    . .PQ.51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x45              .....E
INFO:decocare.stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:decocare.stick:readData validating remote raw[ack]: 02
INFO:decocare.stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:decocare.stick:readData; raw[retries] 0
INFO:decocare.stick:ReadRadio:size:78:eod:found eod (True)
INFO:decocare.stick:found packet len(64), link expects(64)
INFO:decocare.stick:PROCESS:END:771.962:ReadRadio:size:78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>]:download(attempts[1],expect[78],results[64]:data[64]):adding segment
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>]:download(attempts[1],expect[78],results[64]:data[64]):DONE
INFO:decocare.session:finished executing:ReadPumpModel:size[64]:data:'515'
INFO:decocare.commands:ReadPumpModel:size[64]:data:'515':download:done?:found[64] expected[64]
INFO:__main__:PUMP MODEL: ReadPumpModel:size[64]:data:'515'
INFO:decocare.session:execute attempt: 1
INFO:decocare.session:session transferring packet
INFO:decocare.stick:transmit_packet:write:<TransmitPacket:TempBasal:data:unknown>
INFO:decocare.stick:PROCESS:START:772.572:TransmitPacket:TempBasal:data:unknown
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[False] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>] processing TransmitPacket:TempBasal:data:unknown)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[False] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>] sending TransmitPacket:TempBasal:data:unknown)
DEBUG:decocare.stick:[1, 0, 167, 1, 32, 136, 80, 128, 3, 0, 0, 1, 0, 76, 134, 0, 0, 0, 0]
INFO:root:usb.write.len: 19
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x03 0x00 0x00 0x01 0x00 0x4c 0x86 0x00    .....L..
0010   0x00 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc8 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x51 0x03 0x35 0x31    . .PQ.51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing TransmitPacket:TempBasal:data:unknown, bytearray(b'\x00\xc8\x80@\xa7\x01 \x88PQ\x03515\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:decocare.stick:PROCESS:END:774.965:TransmitPacket:TempBasal:data:unknown
INFO:decocare.session:sleeping 0.5 before download
INFO:decocare.session:proceeding with download
INFO:decocare.stick:download:start:0
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>]:download(attempts[1],expect[0],results[0]:data[0]):begin first poll first sleep .250
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>]>:STARTING POLL PHASE:attempt:0
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<TransmitPacket:TempBasal:data:unknown>]>:poll:attempt:0
INFO:decocare.stick:PROCESS:START:1526.767:LinkStatus:0x03:status:size=64
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] processing LinkStatus:0x03:status:size=64)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] sending LinkStatus:0x03:status:size=64)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x0f    .U......
0008   0x05 0x04 0x00 0x50 0x51 0x03 0x35 0x31    ...PQ.51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:LinkStatus:0x03:status:size=15

INFO:decocare.stick:finished processing LinkStatus:0x03:status:size=15, 15
INFO:decocare.stick:PROCESS:END:1528.944:LinkStatus:0x03:status:size=15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[0] command[<LinkStatus:0x03:status:size=15:size(15)>]:STOP POLL after 1 attempts:size:15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download(attempts[1],expect[15],results[0]:data[0]):end first poll
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download(attempts[1],expect[15],results[0]:data[0]):proceed to download packet
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download_packet:15
ERROR:decocare.stick:size is less than 64, which will cause an error. trying 64 instead
INFO:decocare.stick:PROCESS:START:1529.446:ReadRadio:size:15
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>] sending ReadRadio:size:15)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x0f 0xc6                   .....
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 15
INFO:root:usb.read.raw:
0000   0x02 0x00 0x01 0x00 0xc4 0x80 0x01 0xa7    ........
0008   0x01 0x20 0x88 0x50 0xf0 0x00 0x00         . .P...
INFO:decocare.stick:quit send_force_read, found len: 15 expected 64 after 0 attempts
INFO:decocare.stick:readData validating remote raw[ack]: 02
INFO:decocare.stick:readData; foreign raw should be at least 14 bytes? 15 True
INFO:decocare.stick:readData; raw[retries] 0
INFO:decocare.stick:ReadRadio:size:15:eod:found eod (True)
INFO:decocare.stick:found packet len(1), link expects(1)
WARNING:decocare.stick:bad zero CRC?
INFO:decocare.stick:PROCESS:END:1931.755:ReadRadio:size:15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):adding segment
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):DONE
INFO:decocare.session:finished executing:TempBasal:size[64]:data:bytearray(b'\x00')
INFO:decocare.commands:TempBasal:size[64]:data:bytearray(b'\x00'):download:done?:found[1] expected[64]
CRITICAL:decocare.session:this seems like a problem
INFO:__main__:XXX: SET TempBasal!!:
0000   0x00                                       .
INFO:decocare.stick:PROCESS:START:1932.262:UsbStats:0x05 0x01
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<UsbStats:0x05 0x01:size(64)>] processing UsbStats:0x05 0x01)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<UsbStats:0x05 0x01:size(64)>] sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x01 0x57 0x00 0x00 0x01 0x57 0x01    ..W...W.
0010   0x58 0x01 0x5a 0x01 0x57 0x04 0x00 0x00    X.Z.W...
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 343L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 343L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:1934.141:UsbStats:0x05 0x01
INFO:decocare.stick:PROCESS:START:1934.198:RadioStats:0x05 0x00
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<RadioStats:0x05 0x00:size(64)>] processing RadioStats:0x05 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<RadioStats:0x05 0x00:size(64)>] sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x03 0x00    .U......
0008   0x00 0x00 0x40 0x00 0x00 0x00 0x45 0x00    ..@...E.
0010   0x00 0x00 0x19 0x00 0x16 0x00 0x20 0x00    ...... .
0018   0x2a 0x00 0x0c 0x00 0x00 0x00 0x00 0x00    *.......
0020   0x00 0x01 0x00 0xcf 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 69L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 64L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:1936.124:RadioStats:0x05 0x00
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 3,
           'packets.received': 64L,
           'packets.transmit': 69L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 343L,
         'packets.transmit': 343L}}
