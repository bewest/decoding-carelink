# ./status-quo.sh /dev/ttyUSB0 511999
## cat ./status-quo.sh
```bash
```
## cat logs/explain.log
OUT
## Observations
Thu Sep  5 15:29:25 PDT 2013

## stick

* not ok

## pump


## downloaded: 0

```
```


## commands session:finished: 1

```
INFO:session:finished executing:ReadPumpModel:size[64]:data:''
```

howdy! pump runs were NOT OK

### Last send command

```
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick transmit[TransmitPacket:ReadHistoryData:size[1024]:[page][0]:data[0]:] reader[None] download_i[1] status[None] poll_size[0] poll_i[0] command[<LinkStatus:0x03:status:size=64:size(64)>] sending LinkStatus:0x03:status:size=64)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
```
### stats before traceback

```
185:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1833724270L, 'errors.naks': 0, 'errors.sequence': 23, 'packets.received': 17263L, 'errors.crc': 194}
205:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 232L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 232L, 'errors.crc': 0}
207:INFO:__main__:{'radio': {'errors.crc': 0,
208:           'errors.naks': 0,
209:           'errors.sequence': 0,
210:           'errors.timeouts': 0,
211:           'packets.received': 232L,
212:           'packets.transmit': 232L},
213: 'usb': {'errors.crc': 194,
214:         'errors.naks': 0,
215:         'errors.sequence': 23,
216:         'errors.timeouts': 0,
217:         'packets.received': 17263L,
218:         'packets.transmit': 1833724270L}}
1025:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1833724270L, 'errors.naks': 0, 'errors.sequence': 23, 'packets.received': 17263L, 'errors.crc': 189}
1045:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 264L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 264L, 'errors.crc': 0}
1047:INFO:__main__:{'radio': {'errors.crc': 0,
1048:           'errors.naks': 0,
1049:           'errors.sequence': 0,
1050:           'errors.timeouts': 0,
```
### Traceback

```
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

INFO:stick:zero length READ, try once more sleep .250
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

CRITICAL:stick:FAILED TO DOWNLOAD ANYTHING, after 4  expected:64
Traceback (most recent call last):
  File "decocare/session.py", line 127, in <module>
    session.power_control( )
  File "decocare/session.py", line 84, in power_control
    data = self.stick.download( )
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 718, in download
    size = self.poll_size( )
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 549, in poll_size
    size  = self.read_status( )
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 565, in read_status
    result = self.query(LinkStatus)
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 502, in query
    return self.process( )
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 484, in process
    if len(raw) == 0:
TypeError: object of type 'NoneType' has no len()
--

INFO:stick:attempt another read
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

INFO:stick:NESTED zero length READ, try once more sleep .100
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

ERROR:stick:ACK is zero bytes!
Traceback (most recent call last):
  File "decocare/commands.py", line 650, in <module>
    log.info('PUMP MODEL: %s' % session.read_model( ))
  File "/home/bewest/src/decoding-carelink/decocare/session.py", line 89, in read_model
    model = self.query(commands.ReadPumpModel)
  File "/home/bewest/src/decoding-carelink/decocare/session.py", line 104, in query
    self.execute(command)
  File "/home/bewest/src/decoding-carelink/decocare/session.py", line 101, in execute
    return super(type(self), self).execute(command)
  File "/home/bewest/src/decoding-carelink/decocare/session.py", line 39, in execute
    self.download( )
  File "/home/bewest/src/decoding-carelink/decocare/session.py", line 52, in download
    data = self.stick.download( )
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 734, in download
    data = self.download_packet(size)
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 688, in download_packet
--
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc2 0x80 0x40 0xa7    ......@.
0008   0x01 0x51 0x19 0x99 0x14 0x03 0x37 0x32    .Q....72
0010   0x33 0x00 0x00 0x00 0x00 0x00 0x00 0x00    3.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
Traceback (most recent call last):
  File "decocare/stick.py", line 874, in <module>
    stick.open( )
  File "decocare/stick.py", line 847, in open
    log.info('%s' % self.product_info( ))
  File "decocare/stick.py", line 508, in product_info
    return self.query(ProductInfo)
  File "decocare/stick.py", line 502, in query
    return self.process( )
  File "decocare/stick.py", line 489, in process
    ack, response = self.command.respond(raw)
  File "decocare/stick.py", line 68, in respond
    assert commStatus == 1, ('commStatus: %02x expected 0x1' % commStatus)
AssertionError: commStatus: 02 expected 0x1
Command exited with non-zero status 1
python decocare/stick.py /dev/ttyUSB0
--
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:['OK']
STATUS: receive in progress!|STATUS: transmit in progress!|STATUS: interface error!|STATUS: receive overflow!|STATUS: transmit overflow!
ERROR:stick:readStatus: non-zero status: be
Traceback (most recent call last):
  File "decocare/download.py", line 84, in <module>
    downloader.download( )
  File "decocare/download.py", line 24, in download
    self.device.execute(comm)
  File "/home/bewest/src/decoding-carelink/decocare/session.py", line 101, in execute
    return super(type(self), self).execute(command)
  File "/home/bewest/src/decoding-carelink/decocare/session.py", line 39, in execute
    self.download( )
  File "/home/bewest/src/decoding-carelink/decocare/session.py", line 52, in download
    data = self.stick.download( )
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 718, in download
    size = self.poll_size( )
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 549, in poll_size
    size  = self.read_status( )
  File "/home/bewest/src/decoding-carelink/decocare/stick.py", line 565, in read_status
```
* NO CRC ERROR FOUND
* no nak found
* NOT A CLEAN RUN
