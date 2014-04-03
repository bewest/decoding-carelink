hi Namespace(duration=0, port='/dev/ttyUSB.Carelink0', rate=0, serial='208850')
INFO:decocare.link:Link opened serial port: Serial<id=0x7fe36f61cdd0, open=True>(port='/dev/ttyUSB.Carelink0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.4, xonxoff=False, rtscts=False, dsrdtr=False)
INFO:decocare.stick:PROCESS:OPEN:0.008
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
INFO:decocare.stick:PROCESS:END:2.725:ProductInfo:0x04
INFO:decocare.stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0c1700'}
INFO:decocare.stick:PROCESS:START:2.858:ProductInfo:0x04
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
INFO:decocare.stick:PROCESS:END:4.987:ProductInfo:0x04
INFO:decocare.stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0c1700'}
INFO:decocare.stick:get signal strength of Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<ProductInfo:0x04:size(64)>]
INFO:decocare.stick:PROCESS:START:5.268:SignalStrength:0x06 0x00
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<SignalStrength:0x06 0x00:size(64)>] processing SignalStrength:0x06 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<SignalStrength:0x06 0x00:size(64)>] sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbd 0x17 0x00 0x00 0x00    .U......
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:189
INFO:decocare.stick:finished processing SignalStrength:0x06 0x00, 189
INFO:decocare.stick:PROCESS:END:7.634:SignalStrength:0x06 0x00
INFO:decocare.stick:we seem to have found a nice signal strength of: 189
INFO:decocare.session:setting up to talk with 208850
INFO:decocare.stick:PROCESS:START:7.77:UsbStats:0x05 0x01
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<UsbStats:0x05 0x01:size(64)>] processing UsbStats:0x05 0x01)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<UsbStats:0x05 0x01:size(64)>] sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0xb6 0x00 0x00 0x00 0xb6 0x00    ........
0010   0xb7 0x00 0xb8 0x00 0xb6 0x04 0x00 0x00    ........
0018   0x05 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 182L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 182L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:9.687:UsbStats:0x05 0x01
INFO:decocare.stick:PROCESS:START:9.765:RadioStats:0x05 0x00
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<RadioStats:0x05 0x00:size(64)>] processing RadioStats:0x05 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[None] reader[None] download_i[False] status[None] poll_size[None] poll_i[None] command[<RadioStats:0x05 0x00:size(64)>] sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x3a 0x00 0x00 0x00 0x3c 0x00    ..:...<.
0010   0x00 0x00 0x12 0x00 0x0d 0x00 0x20 0x00    ...... .
0018   0x28 0x00 0x0a 0x00 0x05 0x00 0x00 0x00    (.......
0020   0x00 0x01 0x00 0x80 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 60L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 58L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:11.673:RadioStats:0x05 0x00
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 58L,
           'packets.transmit': 60L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 182L,
         'packets.transmit': 182L}}
INFO:decocare.session:execute attempt: 1
INFO:decocare.session:session transferring packet
INFO:decocare.stick:transmit_packet:write:<TransmitPacket:ReadPumpModel:data:unknown>
INFO:decocare.stick:PROCESS:START:12.339:TransmitPacket:ReadPumpModel:data:unknown
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
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x3a 0x00 0x00 0x00 0x3c 0x00    ..:...<.
0010   0x00 0x00 0x12 0x00 0x0d 0x00 0x20 0x00    ...... .
0018   0x28 0x00 0x0a 0x00 0x05 0x00 0x00 0x00    (.......
0020   0x00 0x01 0x00 0x80 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing TransmitPacket:ReadPumpModel:data:unknown, bytearray(b'\x00\x00\x00\x00\x00\x00\x00:\x00\x00\x00<\x00\x00\x00\x12\x00\r\x00 \x00(\x00\n\x00\x05\x00\x00\x00\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:decocare.stick:PROCESS:END:14.469:TransmitPacket:ReadPumpModel:data:unknown
INFO:decocare.session:sleeping 0.5 before download
INFO:decocare.session:proceeding with download
INFO:decocare.stick:download:start:0
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[None] poll_i[None] command[<TransmitPacket:ReadPumpModel:data:unknown>]:download(attempts[1],expect[0],results[0]:data[0]):begin first poll first sleep .250
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[None] poll_i[None] command[<TransmitPacket:ReadPumpModel:data:unknown>]>:STARTING POLL PHASE:attempt:0
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<TransmitPacket:ReadPumpModel:data:unknown>]>:poll:attempt:0
INFO:decocare.stick:PROCESS:START:766.078:LinkStatus:0x03:status:size=64
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] processing LinkStatus:0x03:status:size=64)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] sending LinkStatus:0x03:status:size=64)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x3c 0x00    ......<.
0010   0x00 0x00 0x12 0x00 0x0d 0x00 0x20 0x00    ...... .
0018   0x28 0x00 0x0a 0x00 0x05 0x00 0x00 0x00    (.......
0020   0x00 0x01 0x00 0x80 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:LinkStatus:0x03:status:size=78

INFO:decocare.stick:finished processing LinkStatus:0x03:status:size=78, 78
INFO:decocare.stick:PROCESS:END:768.113:LinkStatus:0x03:status:size=78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[0] command[<LinkStatus:0x03:status:size=78:size(78)>]:STOP POLL after 1 attempts:size:78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download(attempts[1],expect[78],results[0]:data[0]):end first poll
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download(attempts[1],expect[78],results[0]:data[0]):proceed to download packet
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[None] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<LinkStatus:0x03:status:size=78:size(78)>]:download_packet:78
INFO:decocare.stick:PROCESS:START:768.52:ReadRadio:size:78
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>] sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xd5 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x6e 0x03 0x35 0x31    . .Pn.51
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
INFO:decocare.stick:PROCESS:END:770.979:ReadRadio:size:78
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>]:download(attempts[1],expect[78],results[64]:data[64]):adding segment
INFO:decocare.stick:Stick transmit[TransmitPacket:ReadPumpModel:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<ReadRadio:size:78>]:download(attempts[1],expect[78],results[64]:data[64]):DONE
INFO:decocare.session:finished executing:ReadPumpModel:size[64]:data:'515'
INFO:decocare.commands:ReadPumpModel:size[64]:data:'515':download:done?:found[64] expected[64]
INFO:__main__:PUMP MODEL: ReadPumpModel:size[64]:data:'515'
INFO:decocare.session:execute attempt: 1
INFO:decocare.session:session transferring packet
INFO:decocare.stick:transmit_packet:write:<TransmitPacket:TempBasal:data:unknown>
INFO:decocare.stick:PROCESS:START:771.425:TransmitPacket:TempBasal:data:unknown
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[False] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>] processing TransmitPacket:TempBasal:data:unknown)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[False] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>] sending TransmitPacket:TempBasal:data:unknown)
DEBUG:decocare.stick:[1, 0, 167, 1, 32, 136, 80, 128, 3, 0, 0, 1, 0, 76, 134, 0, 32, 7, 154]
INFO:root:usb.write.len: 19
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x03 0x00 0x00 0x01 0x00 0x4c 0x86 0x00    .....L..
0010   0x20 0x07 0x9a                              ..
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xd5 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x6e 0x03 0x35 0x31    . .Pn.51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing TransmitPacket:TempBasal:data:unknown, bytearray(b'\x00\xd5\x80@\xa7\x01 \x88Pn\x03515\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:decocare.stick:PROCESS:END:773.663:TransmitPacket:TempBasal:data:unknown
INFO:decocare.session:sleeping 0.5 before download
INFO:decocare.session:proceeding with download
INFO:decocare.stick:download:start:0
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>]:download(attempts[1],expect[0],results[0]:data[0]):begin first poll first sleep .250
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[78] poll_i[False] command[<TransmitPacket:TempBasal:data:unknown>]>:STARTING POLL PHASE:attempt:0
DEBUG:decocare.stick:<Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<TransmitPacket:TempBasal:data:unknown>]>:poll:attempt:0
INFO:decocare.stick:PROCESS:START:1525.423:LinkStatus:0x03:status:size=64
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] processing LinkStatus:0x03:status:size=64)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=78:size(78)>] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] sending LinkStatus:0x03:status:size=64)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x0f    .U......
0008   0x05 0x04 0x00 0x50 0x6e 0x03 0x35 0x31    ...Pn.51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:LinkStatus:0x03:status:size=15

INFO:decocare.stick:finished processing LinkStatus:0x03:status:size=15, 15
INFO:decocare.stick:PROCESS:END:1527.683:LinkStatus:0x03:status:size=15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[0] command[<LinkStatus:0x03:status:size=15:size(15)>]:STOP POLL after 1 attempts:size:15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download(attempts[1],expect[15],results[0]:data[0]):end first poll
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download(attempts[1],expect[15],results[0]:data[0]):proceed to download packet
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:78] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<LinkStatus:0x03:status:size=15:size(15)>]:download_packet:15
ERROR:decocare.stick:size is less than 64, which will cause an error. trying 64 instead
INFO:decocare.stick:PROCESS:START:1528.213:ReadRadio:size:15
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>] sending ReadRadio:size:15)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x0f 0xc6                   .....
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 15
INFO:root:usb.read.raw:
0000   0x02 0x00 0x01 0x00 0xd6 0x80 0x01 0xa7    ........
0008   0x01 0x20 0x88 0x50 0x03 0x00 0x00         . .P...
INFO:decocare.stick:quit send_force_read, found len: 15 expected 64 after 0 attempts
INFO:decocare.stick:readData validating remote raw[ack]: 02
INFO:decocare.stick:readData; foreign raw should be at least 14 bytes? 15 True
INFO:decocare.stick:readData; raw[retries] 0
INFO:decocare.stick:ReadRadio:size:15:eod:found eod (True)
INFO:decocare.stick:found packet len(1), link expects(1)
WARNING:decocare.stick:bad zero CRC?
INFO:decocare.stick:PROCESS:END:1930.585:ReadRadio:size:15
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):adding segment
INFO:decocare.stick:Stick transmit[TransmitPacket:TempBasal:data:unknown] reader[ReadRadio:size:15] download_i[1] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<ReadRadio:size:15>]:download(attempts[1],expect[15],results[1]:data[1]):DONE
INFO:decocare.session:finished executing:TempBasal:size[64]:data:bytearray(b'\x00')
INFO:decocare.commands:TempBasal:size[64]:data:bytearray(b'\x00'):download:done?:found[1] expected[64]
CRITICAL:decocare.session:this seems like a problem
INFO:__main__:XXX: SET TempBasal!!:
0000   0x00                                       .
INFO:decocare.stick:PROCESS:START:1931.09:UsbStats:0x05 0x01
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<UsbStats:0x05 0x01:size(64)>] processing UsbStats:0x05 0x01)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<UsbStats:0x05 0x01:size(64)>] sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0xbe 0x00 0x00 0x00 0xbe 0x00    ........
0010   0xbf 0x00 0xc0 0x00 0xbe 0x04 0x00 0x00    ........
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 190L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 190L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:1933.161:UsbStats:0x05 0x01
INFO:decocare.stick:PROCESS:START:1933.24:RadioStats:0x05 0x00
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<RadioStats:0x05 0x00:size(64)>] processing RadioStats:0x05 0x00)
INFO:decocare.stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:decocare.stick:link Stick transmit[TransmitPacket:TempBasal:size[64]:data:bytearray(b'\x00')] reader[ReadRadio:size:15] download_i[False] status[<LinkStatus:0x03:status:size=15:size(15)>] poll_size[15] poll_i[False] command[<RadioStats:0x05 0x00:size(64)>] sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:decocare.stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x3d 0x00 0x00 0x00 0x3f 0x00    ..=...?.
0010   0x00 0x00 0x14 0x00 0x0f 0x00 0x20 0x00    ...... .
0018   0x29 0x00 0x0b 0x00 0x05 0x00 0x00 0x00    ).......
0020   0x00 0x01 0x00 0x8b 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:decocare.stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:decocare.stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 63L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 61L, 'errors.crc': 0}
INFO:decocare.stick:PROCESS:END:1935.194:RadioStats:0x05 0x00
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 61L,
           'packets.transmit': 63L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 190L,
         'packets.transmit': 190L}}
