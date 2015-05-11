# ./status-quo.sh /dev/ttyUSB0 913995
## cat ./status-quo.sh
```bash
```
## cat logs/explain.log
OUT
## Observations
Fri Aug  8 15:25:12 PDT 2014

## stick

* not ok

## pump


## downloaded: 0

```
```


## commands session:finished: 0

```
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
184:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1833724270L, 'errors.naks': 0, 'errors.sequence': 15, 'packets.received': 82799L, 'errors.crc': 163}
204:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 103L, 'errors.naks': 5, 'errors.sequence': 0, 'packets.received': 98L, 'errors.crc': 0}
206:INFO:__main__:{'radio': {'errors.crc': 0,
207:           'errors.naks': 5,
208:           'errors.sequence': 0,
209:           'errors.timeouts': 0,
210:           'packets.received': 98L,
211:           'packets.transmit': 103L},
212: 'usb': {'errors.crc': 163,
213:         'errors.naks': 0,
214:         'errors.sequence': 15,
215:         'errors.timeouts': 0,
216:         'packets.received': 82799L,
217:         'packets.transmit': 1833724270L}}
539:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1833724270L, 'errors.naks': 0, 'errors.sequence': 15, 'packets.received': 82799L, 'errors.crc': 162}
559:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 115L, 'errors.naks': 5, 'errors.sequence': 0, 'packets.received': 110L, 'errors.crc': 0}
561:INFO:__main__:{'radio': {'errors.crc': 0,
562:           'errors.naks': 5,
563:           'errors.sequence': 0,
564:           'errors.timeouts': 0,
```
### Traceback

```
INFO:stick:zero length READ, try once more sleep .250
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

CRITICAL:stick:FAILED TO DOWNLOAD ANYTHING, after 4  expected:64
INFO:stick:process zero length READ, try once more sleep .010
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

ERROR:stick:ACK is zero bytes!
Traceback (most recent call last):
  File "decocare/session.py", line 126, in <module>
    session.power_control( )
  File "decocare/session.py", line 83, in power_control
    data = self.stick.download( )
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 718, in download
    size = self.poll_size( )
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 549, in poll_size
    size  = self.read_status( )
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 565, in read_status
    result = self.query(LinkStatus)
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 502, in query
    return self.process( )
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 489, in process
    ack, response = self.command.respond(raw)
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 65, in respond
--

INFO:stick:attempt another read
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

INFO:stick:NESTED zero length READ, try once more sleep .100
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

ERROR:stick:ACK is zero bytes!
Traceback (most recent call last):
  File "decocare/commands.py", line 1485, in <module>
    log.info('PUMP MODEL: %s' % session.read_model( ))
  File "/home/ian/diacon/decoding-carelink/decocare/session.py", line 88, in read_model
    model = self.query(commands.ReadPumpModel)
  File "/home/ian/diacon/decoding-carelink/decocare/session.py", line 103, in query
    self.execute(command)
  File "/home/ian/diacon/decoding-carelink/decocare/session.py", line 100, in execute
    return super(type(self), self).execute(command)
  File "/home/ian/diacon/decoding-carelink/decocare/session.py", line 38, in execute
    self.download( )
  File "/home/ian/diacon/decoding-carelink/decocare/session.py", line 51, in download
    data = self.stick.download( )
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 743, in download
    data = self.download_packet(size)
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 688, in download_packet
--
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xd9 0x80 0x40 0xa7    ......@.
0008   0x01 0x91 0x39 0x95 0x29 0x03 0x35 0x35    ..9.).55
0010   0x34 0x00 0x00 0x00 0x00 0x00 0x00 0x00    4.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
Traceback (most recent call last):
  File "decocare/stick.py", line 884, in <module>
    stick.open( )
  File "decocare/stick.py", line 857, in open
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
STATUS: receive in progress!|STATUS: transmit overflow!|STATUS: OK
ERROR:stick:readStatus: non-zero status: a3
Traceback (most recent call last):
  File "decocare/download.py", line 84, in <module>
    downloader.download( )
  File "decocare/download.py", line 24, in download
    self.device.execute(comm)
  File "/home/ian/diacon/decoding-carelink/decocare/session.py", line 100, in execute
    return super(type(self), self).execute(command)
  File "/home/ian/diacon/decoding-carelink/decocare/session.py", line 38, in execute
    self.download( )
  File "/home/ian/diacon/decoding-carelink/decocare/session.py", line 51, in download
    data = self.stick.download( )
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 718, in download
    size = self.poll_size( )
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 549, in poll_size
    size  = self.read_status( )
  File "/home/ian/diacon/decoding-carelink/decocare/stick.py", line 565, in read_status
```
* NO CRC ERROR FOUND
* no nak found
* NOT A CLEAN RUN
