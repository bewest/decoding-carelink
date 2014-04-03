hi Namespace(duration=0, port='/dev/ttyUSB.Carelink0', rate=0, serial='208850')
INFO:decocare.link:Link opened serial port: Serial<id=0x7f04d0f9add0, open=True>(port='/dev/ttyUSB.Carelink0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.4, xonxoff=False, rtscts=False, dsrdtr=False)
INFO:decocare.stick:PROCESS:OPEN:0.007
INFO:decocare.stick:PROCESS:START:0.064:ProductInfo:0x04
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
INFO:decocare.stick:PROCESS:END:2.468:ProductInfo:0x04
INFO:decocare.stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0c1700'}
INFO:decocare.stick:PROCESS:START:2.596:ProductInfo:0x04
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
INFO:decocare.stick:PROCESS:END:4.843:ProductInfo:0x04
INFO:decocare.stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0c1700'}
INFO:decocare.stick:get signal strength of Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<ProductInfo:0x04:size(64)>]
INFO:decocare.stick:PROCESS:START:5.127:SignalStrength:0x06 0x00
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<SignalStrength:0x06 0x00:size(64)>] processing SignalStrength:0x06 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<SignalStrength:0x06 0x00:size(64)>] sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbe 0x17 0x00 0x00 0x00    .U......
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:190
INFO:decocare.stick:finished processing SignalStrength:0x06 0x00, 190
INFO:decocare.stick:PROCESS:END:7.18:SignalStrength:0x06 0x00
INFO:decocare.stick:we seem to have found a nice signal strength of: 190
INFO:decocare.session:setting up to talk with 208850
INFO:decocare.stick:PROCESS:START:7.371:UsbStats:0x05 0x01
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<UsbStats:0x05 0x01:size(64)>] processing UsbStats:0x05 0x01)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<UsbStats:0x05 0x01:size(64)>] sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x01 0x28 0x00 0x00 0x01 0x28 0x01    ..(...(.
0010   0x29 0x01 0x2b 0x01 0x28 0x04 0x00 0x00    ).+.(...
0018   0x05 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 296L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 296L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:9.376:UsbStats:0x05 0x01
INFO:decocare.stick:PROCESS:START:9.455:RadioStats:0x05 0x00
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<RadioStats:0x05 0x00:size(64)>] processing RadioStats:0x05 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<RadioStats:0x05 0x00:size(64)>] sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x03 0x00    .U......
0008   0x00 0x00 0x34 0x00 0x00 0x00 0x39 0x00    ..4...9.
0010   0x00 0x00 0x11 0x00 0x0e 0x00 0x20 0x00    ...... .
0018   0x26 0x00 0x08 0x00 0x00 0x00 0x00 0x00    &.......
0020   0x00 0x01 0x00 0xa3 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 57L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 52L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:11.561:RadioStats:0x05 0x00
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 3,
           'packets.received': 52L,
           'packets.transmit': 57L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 296L,
         'packets.transmit': 296L}}
INFO:decocare.session:execute attempt: 1
INFO:decocare.session:session transferring packet
INFO:decocare.stick:transmit_packet:write:<TransmitPacket:ReadPumpModel:data:unknown>
INFO:decocare.stick:PROCESS:START:12.681:TransmitPacket:ReadPumpModel:data:unknown
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
0008   0x00 0x00 0x34 0x00 0x00 0x00 0x39 0x00    ..4...9.
0010   0x00 0x00 0x11 0x00 0x0e 0x00 0x20 0x00    ...... .
0018   0x26 0x00 0x08 0x00 0x00 0x00 0x00 0x00    &.......
0020   0x00 0x01 0x00 0xa3 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing TransmitPacket:ReadPumpModel:data:unknown, bytearray(b'\x00\x00\x00\x03\x00\x00\x004\x00\x00\x009\x00\x00\x00\x11\x00\x0e\x00 \x00&\x00\x08\x00\x00\x00\x00\x00\x00\x01\x00\xa3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:decocare.stick:PROCESS:END:14.981:TransmitPacket:ReadPumpModel:data:unknown
INFO:decocare.session:sleeping 0.5 before download
INFO:decocare.session:proceeding with download
INFO:decocare.stick:download:start:0
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[None] poll_i[None] command[<TransmitPacket:ReadPumpModel:data:unknown>]:download(attempts[1],expect[0],results[0]:data[0]):begin first poll first sleep .250
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[None] poll_i[None] command[<TransmitPacket:ReadPumpModel:data:unknown>]>:STARTING POLL PHASE:attempt:0
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<TransmitPacket:ReadPumpModel:data:unknown>]>:poll:attempt:0
INFO:decocare.stick:PROCESS:START:766.723:LinkStatus:0x03:status:size=64
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] processing LinkStatus:0x03:status:size=64)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] sending LinkStatus:0x03:status:size=64)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x39 0x00    ......9.
0010   0x00 0x00 0x11 0x00 0x0e 0x00 0x20 0x00    ...... .
0018   0x26 0x00 0x08 0x00 0x00 0x00 0x00 0x00    &.......
0020   0x00 0x01 0x00 0xa3 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:LinkStatus:0x03:status:size=78

INFO:decocare.stick:finished processing LinkStatus:0x03:status:size=78, 78
INFO:decocare.stick:PROCESS:END:768.858:LinkStatus:0x03:status:size=78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[0] command[<LinkStatus:0x03:status:size=78:size(78)>]:STOP POLL after 1 attempts:size:78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download(attempts[1],expect[78],results[0]:data[0]):end first poll
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download(attempts[1],expect[78],results[0]:data[0]):proceed to download packet
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download_packet:78
INFO:decocare.stick:PROCESS:START:769.336:ReadRadio:size:78
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>] sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xe1 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x41 0x03 0x35 0x31    . .PA.51
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
INFO:decocare.stick:PROCESS:END:771.975:ReadRadio:size:78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>]:download(attempts[1],expect[78],results[64]:data[64]):adding segment
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>]:download(attempts[1],expect[78],results[64]:data[64]):DONE
INFO:decocare.session:finished executing:ReadPumpModel:size[64]:data:'515'
INFO:decocare.commands:ReadPumpModel:size[64]:data:'515':download:done?:found[64] expected[64]
INFO:__main__:PUMP MODEL: ReadPumpModel:size[64]:data:'515'
INFO:decocare.session:execute attempt: 1
INFO:decocare.session:session transferring packet
INFO:decocare.stick:transmit_packet:write:<TransmitPacket:TempBasal:data:unknown>
INFO:decocare.stick:PROCESS:START:772.578:TransmitPacket:TempBasal:data:unknown
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
0000   0x01 0x55 0x00 0x00 0xe1 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x41 0x03 0x35 0x31    . .PA.51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing TransmitPacket:TempBasal:data:unknown, bytearray(b'\x00\xe1\x80@\xa7\x01 \x88PA\x03515\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:decocare.stick:PROCESS:END:774.935:TransmitPacket:TempBasal:data:unknown
INFO:decocare.session:sleeping 0.5 before download
INFO:decocare.session:proceeding with download
INFO:decocare.stick:download:start:0
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>]:download(attempts[1],expect[0],results[0]:data[0]):begin first poll first sleep .250
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>]>:STARTING POLL PHASE:attempt:0
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<TransmitPacket:TempBasal:data:unknown>]>:poll:attempt:0
INFO:decocare.stick:PROCESS:START:1526.656:LinkStatus:0x03:status:size=64
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] processing LinkStatus:0x03:status:size=64)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] sending LinkStatus:0x03:status:size=64)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x0f    .U......
0008   0x05 0x04 0x00 0x50 0x41 0x03 0x35 0x31    ...PA.51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:LinkStatus:0x03:status:size=15

INFO:decocare.stick:finished processing LinkStatus:0x03:status:size=15, 15
INFO:decocare.stick:PROCESS:END:1528.792:LinkStatus:0x03:status:size=15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[0] command[<LinkStatus:0x03:status:size=15:size(15)>]:STOP POLL after 1 attempts:size:15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download(attempts[1],expect[15],results[0]:data[0]):end first poll
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download(attempts[1],expect[15],results[0]:data[0]):proceed to download packet
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download_packet:15
ERROR:decocare.stick:size is less than 64, which will cause an error. trying 64 instead
INFO:decocare.stick:PROCESS:START:1529.326:ReadRadio:size:15
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>] sending ReadRadio:size:15)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x0f 0xc6                   .....
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 15
INFO:root:usb.read.raw:
0000   0x02 0x00 0x01 0x00 0xe1 0x80 0x01 0xa7    ........
0008   0x01 0x20 0x88 0x50 0x10 0x00 0x00         . .P...
INFO:decocare.stick:quit send_force_read, found len: 15 expected 64 after 0 attempts
INFO:decocare.stick:readData validating remote raw[ack]: 02
INFO:decocare.stick:readData; foreign raw should be at least 14 bytes? 15 True
INFO:decocare.stick:readData; raw[retries] 0
INFO:decocare.stick:ReadRadio:size:15:eod:found eod (True)
INFO:decocare.stick:found packet len(1), link expects(1)
WARNING:decocare.stick:bad zero CRC?
INFO:decocare.stick:PROCESS:END:1931.692:ReadRadio:size:15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):adding segment
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):DONE
INFO:decocare.session:finished executing:TempBasal:size[64]:data:bytearray(b'\x00')
INFO:decocare.commands:TempBasal:size[64]:data:bytearray(b'\x00'):download:done?:found[1] expected[64]
CRITICAL:decocare.session:this seems like a problem
INFO:__main__:XXX: SET TempBasal!!:
0000   0x00                                       .
INFO:decocare.stick:PROCESS:START:1932.253:UsbStats:0x05 0x01
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<UsbStats:0x05 0x01:size(64)>] processing UsbStats:0x05 0x01)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<UsbStats:0x05 0x01:size(64)>] sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x01 0x30 0x00 0x00 0x01 0x30 0x01    ..0...0.
0010   0x31 0x01 0x33 0x01 0x30 0x04 0x00 0x00    1.3.0...
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 304L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 304L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:1934.269:UsbStats:0x05 0x01
INFO:decocare.stick:PROCESS:START:1934.34:RadioStats:0x05 0x00
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<RadioStats:0x05 0x00:size(64)>] processing RadioStats:0x05 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<RadioStats:0x05 0x00:size(64)>] sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x03 0x00    .U......
0008   0x00 0x00 0x37 0x00 0x00 0x00 0x3c 0x00    ..7...<.
0010   0x00 0x00 0x13 0x00 0x10 0x00 0x20 0x00    ...... .
0018   0x27 0x00 0x09 0x00 0x00 0x00 0x00 0x00    '.......
0020   0x00 0x01 0x00 0xae 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 60L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 55L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:1936.31:RadioStats:0x05 0x00
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 3,
           'packets.received': 55L,
           'packets.transmit': 60L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 304L,
         'packets.transmit': 304L}}
