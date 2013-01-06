# capture error I'm seeing

Ok this captures the error I've been wanting to capture.

When reading data from the radio, if the size is less than 64 bytes (15 are
indicated here), the ReadRadio responses consistently fail their ACK.

However, the responses look like **VALID** `read_status` responses!
Are they getting out of order?  Do I need to wait longer?  Am I waiting in the
wrong place?

EG:

## baseline


### start a session
```
INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 2L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2L, 'errors.crc': 0}
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 2L,
           'packets.transmit': 2L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 57L,
         'packets.transmit': 57L}}
INFO:__main__:POWER CONTROL ON
INFO:__main__:execute attempt: 1
INFO:__main__:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:PowerControl>
INFO:stick:link Stick:status:None:command:<TransmitPacket:PowerControl> processing TransmitPacket:PowerControl)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 2, 85, 0, 1, 0, 93, 36, 1, 10, 162]
INFO:root:usb.write.len: 18
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x02 0x55 0x00 0x01 0x00 0x5d 0x24 0x01    .U...]$.
0010   0x0a 0xa2                                  ..
DEBUG:stick:sleeping 17
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x02 0x00 0x00 0x00 0x02 0x00    ........
0010   0x00 0x00 0x01 0x00 0x02 0x00 0x00 0x00    ........
0018   0x00 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x02 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
```

### transmit packet
everything up to this point looks good, we could try to see if we have a
response
```
INFO:stick:finished processing TransmitPacket:PowerControl, bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:__main__:proceeding with download
DEBUG:stick:<Stick:status:None:command:<TransmitPacket:PowerControl>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:None:command:<TransmitPacket:PowerControl>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:None:command:<LinkStatus:0x03> processing LinkStatus:0x03)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

INFO:stick:zero length READ, try once more sleep .100
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

ERROR:stick:ACK is zero bytes!
ERROR:__main__:ACK is 0 bytes: 
```
This usually doesn't happen, we usually get a response, (eg if we
clear out the stick, reconnect, and issue commands without the
power_control, we'll get fast responses every time! Very odd!)

### uh... ok, well maybe we'll try to download anyway

Since this will trigger another poll phase anyway, and we need it to get the
bytes.
```
INFO:__main__:proceeding with download
DEBUG:stick:<Stick:status:None:command:<LinkStatus:0x03>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:None:command:<LinkStatus:0x03>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:None:command:<LinkStatus:0x03> processing LinkStatus:0x03)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x0f    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x02 0x00    ........
0010   0x00 0x00 0x01 0x00 0x02 0x00 0x00 0x00    ........
0018   0x00 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x02 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:LinkStatus:0x03
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03, 15
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 1 attempts:size:15
```

### hello! WOW
So this is was mostly unexpected, given my previous iterations on with
sometimes working code and the analysis of the original applet's
behavior.  The analysis led me to a theory of operation that said that
responses were ALWAYS 64 bytes.  Apparently this is not true.
The radio has a response which generally should come back with in some
timeout.

Fine, it's less than 64 bytes, the assertions may need a little
adjusting, but there's no reason this can't work.  It appears that the
stick will basically tell you how many commands to read and when, if
you are sensitive enough.

Let's try to use the ReadRadio command, as usual.  What we expect to
happen here based on our naive experience thus far is:

  * transmit ReadRadio
  * read ReadRadio ACK, which starts with 0x02, and has a payload

We believe this is true because the POLL phase told use 15 bytes were
available.  We'll try to read 64 bytes in any case, just to be
careful.

It's important to note that using the model supported by analysis, we
expect the response to pass all validations against the custom
ReadRadio ACK response.  Anything else we assume is a serious error.

```
INFO:stick:download_packet:15
ERROR:stick:size is less than 64, which will cause an error. trying 64 instead
INFO:stick:link Stick:status:<LinkStatus:0x03>:command:<ReadRadio:size:15> processing ReadRadio:size:15)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x0f 0xc6                   .....
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x0f    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x02 0x00    ........
0010   0x00 0x00 0x01 0x00 0x02 0x00 0x00 0x00    ........
0018   0x00 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x02 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:readData validating remote raw[ack]: 01
INFO:stick:readData; foreign raw should be at least 14 bytes? 64 True
INFO:stick:readData; raw[retries] 0
ERROR:__main__:bad dl raw! bytearray(b'\x01U\x00\x00\x02\x01\x00\x0f\x05\x04\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
```
### you have another think coming
Notice, this response has failed ReadRadio's ACK assertions, but it
would potentially would have passed LinkStatus's assertions, and given us a
length of 15.

```python
>>> c = stick.LinkStatus( )
>>> b = bytearray(b'\x01U\x00\x00\x02\x01\x00\x0f\x05\x04\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> ack , body = c.respond( b )
>>> p = c.parse(body)
>>> p
15
>>> 
```

```
INFO:__main__:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03>:command:<ReadRadio:size:15>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03>:command:<ReadRadio:size:15>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03>:command:<LinkStatus:0x03> processing LinkStatus:0x03)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
```

### BTW, here's your 15 bytes!
```
INFO:root:usb.read.len: 15
INFO:root:usb.read.raw:
0000   0x02 0x00 0x01 0x00 0xd9 0x80 0x01 0xa7    ........
0008   0x01 0x20 0x88 0x50 0xcf 0x00 0x00         . .P...
```

Is this a valid ReadRadio response?

```python
>>> c = stick.LinkStatus( )
>>> b = bytearray(b'\x01U\x00\x00\x02\x01\x00\x0f\x05\x04\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> ack , body = c.respond( b )
>>> p = c.parse(body)
>>> p
15
>>> 
>>> c = stick.ReadRadio(p)
>>> r = bytearray( [ 0x02, 0x00, 0x01, 0x00, 0xd9, 0x80, 0x01, 0xa7, 0x01, 0x20, 0x88, 0x50, 0xcf, 0x00, 0x00 ] )
>>> ack, body = c.respond(r)
>>> success = c.parse(body)
>>> success
bytearray(b'\x00')
>>> 

```
I feel confident that this would allow us to exchange more messages as
usual.

A few options seem likely:
  * it's possible to use read_status and last_status as a filler until
    ReadRadio's ACK also passes if last_status's fails?
    **complicated**
  * or is there another way to get 15 to come out?  just waiting
    longer? **moderate**
  * what if the effectTime had an effect after polling but before
    ReadRadio goes into effect? **easy**

Hmm...

## Options

```
INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 0L,
           'packets.transmit': 0L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 34L,
         'packets.transmit': 34L}}
INFO:__main__:POWER CONTROL ON
INFO:__main__:execute attempt: 1
INFO:__main__:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:PowerControl>
INFO:stick:link Stick:status:None:command:<TransmitPacket:PowerControl> processing TransmitPacket:PowerControl)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 2, 85, 0, 1, 0, 93, 36, 1, 10, 162]
INFO:root:usb.write.len: 18
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x02 0x55 0x00 0x01 0x00 0x5d 0x24 0x01    .U...]$.
0010   0x0a 0xa2                                  ..
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:finished processing TransmitPacket:PowerControl, bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:__main__:sleeping 17 before download
INFO:__main__:proceeding with download
DEBUG:stick:<Stick:status:None:command:<TransmitPacket:PowerControl>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:None:command:<TransmitPacket:PowerControl>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:None:command:<LinkStatus:0x03> processing LinkStatus:0x03)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

INFO:stick:zero length READ, try once more sleep .100
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

ERROR:stick:ACK is zero bytes!
ERROR:__main__:ACK is 0 bytes:

INFO:__main__:proceeding with download
DEBUG:stick:<Stick:status:None:command:<LinkStatus:0x03>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:None:command:<LinkStatus:0x03>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:None:command:<LinkStatus:0x03> processing LinkStatus:0x03)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x0f    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:LinkStatus:0x03
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03, 15
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 1 attempts:size:15
INFO:stick:download_packet:15
ERROR:stick:size is less than 64, which will cause an error. trying 64 instead
INFO:stick:link Stick:status:<LinkStatus:0x03>:command:<ReadRadio:size:15> processing ReadRadio:size:15)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x0f 0xc6                   .....
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x0f    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:readData validating remote raw[ack]: 01
INFO:stick:readData; foreign raw should be at least 14 bytes? 64 True
INFO:stick:readData; raw[retries] 0
INFO:stick:we failed to pass ReadRadio:size:15 ACK!?
INFO:stick:expected size was: 15
INFO:stick:XXX:JUST a bit more READ new size: 15, sleep .100
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
INFO:root:usb.read.len: 15
INFO:root:usb.read.raw:
0000   0x02 0x00 0x01 0x00 0xdc 0x80 0x01 0xa7    ........
0008   0x01 0x20 0x88 0x50 0x8b 0x00 0x00         . .P...
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 15 True
INFO:stick:readData; raw[retries] 0
INFO:stick:XXX resLength: 1
INFO:stick:found packet len(1)
0000   0x00                                       .
INFO:stick:readDeviceDataIO:msgCRC:0:expectedCRC:0:data:0000   0x00                                       .
INFO:stick:link Stick:status:<LinkStatus:0x03>:command:<UsbStats:0x05 0x01> processing UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x8b 0x00 0x00 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1351286784L, 'errors.naks': 0, 'errors.sequence': 2, 'packets.received': 328704L, 'errors.crc': 0}
INFO:stick:link Stick:status:<LinkStatus:0x03>:command:<RadioStats:0x05 0x00> processing RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x29 0x00 0x00 0x00 0x29 0x00    ..)...).
0010   0x2a 0x00 0x2a 0x00 0x29 0x04 0x00 0x00    *.*.)...
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 41L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 41L, 'errors.crc': 0}
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 41L,
           'packets.transmit': 41L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 2,
         'errors.timeouts': 0,
         'packets.received': 328704L,
         'packets.transmit': 1351286784L}}
INFO:__main__:execute attempt: 1
INFO:__main__:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpModel>
```


### alternate `last_status` and `read_status`

This configuration ensures that we won't die early checking ACKS.
Let's call this "primiscuous mode"?!  However, we see the appearance
of sequence.errors, and the counters are busted.

When this happens, it's usually fixed by re-inserting the usb stick
and re-trying.

### wait longer somewhere, shifting timing?

I shifted the timing around, but it doesn't seem to help very much.

### move effectTime effect

Tried shifting this around a bit, and it doesn't seem to matter much.
The newer configuration seems more predictable on the one hand, but
still not working on the other hand.

If Medtronic really cared about patients, they would have put this
information in the user manual.

