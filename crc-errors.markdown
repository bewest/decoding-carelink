
# What to do about CRC errors

Sometimes/often when dumping lots of pages from the ReadHistoryData
command, one of the segments will come back, passes most of the
validations for the ReadRadio ACK, but appears to be missing a CRC.

What should we do?

## After 3 or 4 runs

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

stick.py just grabs a bunch of stick stats, and attempts to flush any
radio buffer.  If there is no data on the radio buffer, nothing else
happens.

Useful to see what state the stick is in, as well as recover from any
potential error states.

session.py provides a framework for passing packets to insulin pumps
on a reliable and reproducible basis.  It turns on RF power and grabs
the serial number as a demo/test of these abilities.

commands.py defines many packets that insulin pumps response to,
including reading any error states, and performing audits and backups
of the logs.  Intended to aid in development of automatically
downloading medical records from the medical device.

Sometimes when downloading many pages, we get a CRC error.

stick.py is run several times afterwards to try and catch any
problems.

It looks like the current implementation of clear_buffer may resolve
these error states, since the counters indicate that we've actually
successfully downloaded all the data, and there are no resulting NAK.


##Output

Looks like there's lots of data still in the buffer!?
And was twice enough to catch it all?
(BTW, proceeding without clearing the buffer results in busting the
stick all over again.)
Try out a new clear_buffer method....

## stick.py, the prelude
Stick attempts to clear any residual radio buffer using the new
clear_buffer method.  It should only go into action to catch CRC
errors after a session has failed to handle the situation.  We run
```

# ./status-quo.sh 
Mon Jan  7 09:30:50 PST 2013
INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
INFO:link:Link opened serial port: Serial<id=0x2592610, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.5, xonxoff=False, rtscts=False, dsrdtr=False)
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbf 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:191
INFO:__main__:finished processing SignalStrength:0x06 0x00, 191
INFO:__main__:we seem to have found a nice signal strength of: 191
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbf 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:191
INFO:__main__:finished processing SignalStrength:0x06 0x00, 191
INFO:__main__:we seem to have found a nice signal strength of: 191
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbe 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:190
INFO:__main__:finished processing SignalStrength:0x06 0x00, 190
INFO:__main__:we seem to have found a nice signal strength of: 190
INFO:__main__:test fetching product info Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)>
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II',
 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')],
 'product.version': '0.0',
 'rf.freq': '916.5Mhz',
 'serial': '0b2c00',
 'software.version': '1.16'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc0 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:192
INFO:__main__:finished processing SignalStrength:0x06 0x00, 192
INFO:__main__:we seem to have found a nice signal strength of: 192
INFO:__main__:at this point, we could issue remote commands to a medical
    device, let's inspect the interfaces
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x28 0x00 0x00 0x00 0x28 0x00    ..(...(.
0010   0x29 0x00 0x29 0x00 0x28 0x04 0x00 0x00    ).).(...
0018   0x05 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 40L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 40L, 'errors.crc': 0}
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
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
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
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
         'packets.received': 40L,
         'packets.transmit': 40L}}
INFO:__main__:CLEAR BUFFERS
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x2a 0x00 0x00 0x00 0x2a 0x00    ..*...*.
0010   0x2b 0x00 0x2b 0x00 0x2a 0x04 0x00 0x00    +.+.*...
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 42L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 42L, 'errors.crc': 0}
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
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
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
DEBUG:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 0L,
           'packets.transmit': 0L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 42L,
         'packets.transmit': 42L}}
INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
DEBUG:__main__:<Stick:status:None:command:<RadioStats:0x05 0x00:size(64)>>:STARTING POLL PHASE:attempt:0
DEBUG:__main__:<Stick:status:None:command:<RadioStats:0x05 0x00:size(64)>>:poll:attempt:0
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:2
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:3
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
INFO:__main__:STOP POLL after 4 attempts:size:0
INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 0
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x30 0x00 0x00 0x00 0x30 0x00    ..0...0.
0010   0x31 0x00 0x31 0x00 0x30 0x04 0x00 0x00    1.1.0...
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 48L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 48L, 'errors.crc': 0}
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
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
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 0L,
           'packets.transmit': 0L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 48L,
         'packets.transmit': 48L}}
INFO:__main__:NO PENDING BUFFER
INFO:__main__:DONE CLEARING BUFFERS
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x32 0x00 0x00 0x00 0x32 0x00    ..2...2.
0010   0x33 0x00 0x33 0x00 0x32 0x04 0x00 0x00    3.3.2...
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 50L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 50L, 'errors.crc': 0}
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
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
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 0L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 0L, 'errors.crc': 0}
INFO:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 0L,
           'packets.transmit': 0L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 50L,
         'packets.transmit': 50L}}
python pump/stick.py /dev/ttyUSB0
	elapsed 0:01.38
	user 0.15
	system 0.05
	CPU 14% (0text+0data 42096max)k
```

## session.py

```
INFO:__main__:howdy! I'm going to take a look at your pump.
INFO:link:Link opened serial port: Serial<id=0x12377d0, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.2, xonxoff=False, rtscts=False, dsrdtr=False)
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbe 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:190
INFO:stick:finished processing SignalStrength:0x06 0x00, 190
INFO:stick:we seem to have found a nice signal strength of: 190
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbc 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:188
INFO:stick:finished processing SignalStrength:0x06 0x00, 188
INFO:stick:we seem to have found a nice signal strength of: 188
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbd 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:189
INFO:stick:finished processing SignalStrength:0x06 0x00, 189
INFO:stick:we seem to have found a nice signal strength of: 189
INFO:__main__:setting up to talk with 208850
INFO:stick:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x3a 0x00 0x00 0x00 0x3a 0x00    ..:...:.
0010   0x3b 0x00 0x3b 0x00 0x3a 0x04 0x00 0x00    ;.;.:...
0018   0x05 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 58L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 58L, 'errors.crc': 0}
INFO:stick:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
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
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
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
         'packets.received': 58L,
         'packets.transmit': 58L}}
INFO:__main__:BEGIN POWER CONTROL
INFO:__main__:execute attempt: 1
INFO:__main__:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:PowerControl>
INFO:stick:link Stick:status:None:command:<TransmitPacket:PowerControl> processing TransmitPacket:PowerControl)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<TransmitPacket:PowerControl> sending TransmitPacket:PowerControl)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 2, 85, 0, 0, 0, 93, 122, 1, 10, 162]
INFO:root:usb.write.len: 18
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x02 0x55 0x00 0x00 0x00 0x5d 0x7a 0x01    .U...]z.
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
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:PowerControl, bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:__main__:sleeping 17 before download
INFO:__main__:no download required
INFO:__main__:manually download PowerControl
DEBUG:stick:<Stick:status:None:command:<TransmitPacket:PowerControl>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:None:command:<TransmitPacket:PowerControl>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 0
INFO:root:usb.read.raw:

INFO:stick:zero length READ, try once more sleep .250
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
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 15
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 1 attempts:size:15
INFO:stick:download_packet:15
ERROR:stick:size is less than 64, which will cause an error. trying 64 instead
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<ReadRadio:size:15> sending ReadRadio:size:15)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x0f 0xc6                   .....
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 15
INFO:root:usb.read.raw:
0000   0x02 0x00 0x01 0x00 0xc7 0x80 0x01 0xa7    ........
0008   0x01 0x20 0x88 0x50 0xcc 0x00 0x00         . .P...
INFO:stick:quit send_force_read, found len: 15 expected 64 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 15 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(1), link expects(1)
WARNING:stick:bad zero CRC?
INFO:__main__:ENDING manual download:
0000   0x00                                       .
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x3f 0x00 0x00 0x00 0x3f 0x00    ..?...?.
0010   0x40 0x00 0x40 0x00 0x3f 0x04 0x00 0x00    @.@.?...
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 63L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 63L, 'errors.crc': 0}
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
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
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
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
         'packets.received': 63L,
         'packets.transmit': 63L}}
INFO:__main__:execute attempt: 1
INFO:__main__:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpModel>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<TransmitPacket:ReadPumpModel> processing TransmitPacket:ReadPumpModel)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<TransmitPacket:ReadPumpModel> sending TransmitPacket:ReadPumpModel)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 141, 199, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x8d 0xc7 0x00    ........
DEBUG:stick:sleeping 0.001
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
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadPumpModel, bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:__main__:sleeping 0 before download
INFO:__main__:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(15)>:command:<TransmitPacket:ReadPumpModel>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(15)>:command:<TransmitPacket:ReadPumpModel>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x02 0x00    ........
0010   0x00 0x00 0x01 0x00 0x02 0x00 0x00 0x00    ........
0018   0x00 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x02 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x02 0x00    ........
0010   0x00 0x00 0x01 0x00 0x02 0x00 0x00 0x00    ........
0018   0x00 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x02 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc5 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x3c 0x03 0x35 0x31    . .P<.51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x45              .....E
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:PUMP MODEL: ReadPumpModel:'515'
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x45 0x00 0x00 0x00 0x45 0x00    ..E...E.
0010   0x46 0x00 0x47 0x00 0x45 0x04 0x00 0x00    F.G.E...
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 69L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 69L, 'errors.crc': 0}
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x03 0x00 0x00 0x00 0x03 0x00    ........
0010   0x00 0x00 0x02 0x00 0x02 0x00 0x00 0x00    ........
0018   0x01 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x0b 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 3L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 3L, 'errors.crc': 0}
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 3L,
           'packets.transmit': 3L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 69L,
         'packets.transmit': 69L}}
python pump/session.py /dev/ttyUSB0 208850
	elapsed 0:18.73
	user 0.14
	system 0.03
	CPU 0% (0text+0data 41776max)k
INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
INFO:link:Link opened serial port: Serial<id=0x2360990, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.2, xonxoff=False, rtscts=False, dsrdtr=False)
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc1 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:193
INFO:stick:finished processing SignalStrength:0x06 0x00, 193
INFO:stick:we seem to have found a nice signal strength of: 193
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc2 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:194
INFO:stick:finished processing SignalStrength:0x06 0x00, 194
INFO:stick:we seem to have found a nice signal strength of: 194
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc1 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:193
INFO:stick:finished processing SignalStrength:0x06 0x00, 193
INFO:stick:we seem to have found a nice signal strength of: 193
INFO:session:setting up to talk with 208850
INFO:stick:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x4d 0x00 0x00 0x00 0x4d 0x00    ..M...M.
0010   0x4e 0x00 0x4f 0x00 0x4d 0x04 0x00 0x00    N.O.M...
0018   0x05 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 77L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 77L, 'errors.crc': 0}
INFO:stick:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x03 0x00 0x00 0x00 0x03 0x00    ........
0010   0x00 0x00 0x02 0x00 0x02 0x00 0x00 0x00    ........
0018   0x01 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x0b 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 3L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 3L, 'errors.crc': 0}
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 3L,
           'packets.transmit': 3L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 77L,
         'packets.transmit': 77L}}
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpModel>
INFO:stick:link Stick:status:None:command:<TransmitPacket:ReadPumpModel> processing TransmitPacket:ReadPumpModel)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<TransmitPacket:ReadPumpModel> sending TransmitPacket:ReadPumpModel)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 141, 199, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x8d 0xc7 0x00    ........
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x03 0x00 0x00 0x00 0x03 0x00    ........
0010   0x00 0x00 0x02 0x00 0x02 0x00 0x00 0x00    ........
0018   0x01 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x0b 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadPumpModel, bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\x02\x00\x02\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:None:command:<TransmitPacket:ReadPumpModel>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:None:command:<TransmitPacket:ReadPumpModel>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x03 0x00    ........
0010   0x00 0x00 0x02 0x00 0x02 0x00 0x00 0x00    ........
0018   0x01 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x0b 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x03 0x00    ........
0010   0x00 0x00 0x02 0x00 0x02 0x00 0x00 0x00    ........
0018   0x01 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x0b 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x03 0x35 0x31    . .P..51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x45              .....E
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:PUMP MODEL: ReadPumpModel:'515'
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpModel>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpModel> processing TransmitPacket:ReadPumpModel)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpModel> sending TransmitPacket:ReadPumpModel)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 141, 199, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x8d 0xc7 0x00    ........
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x03 0x35 0x31    . .P..51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadPumpModel, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x03515\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpModel>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpModel>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x03 0x35 0x31    ...P..51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x03 0x35 0x31    ...P..51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x03 0x35 0x31    . .P..51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x45              .....E
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:comm:ReadPumpModel:'515':data:None
INFO:__main__:REMOTE PUMP MODEL NUMBER: 515
INFO:__main__:READ RTC
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadRTC>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRTC> processing TransmitPacket:ReadRTC)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRTC> sending TransmitPacket:ReadRTC)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 112, 17, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x70 0x11 0x00    .....p..
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x03 0x35 0x31    . .P..51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadRTC, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x03515\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRTC>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRTC>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x03 0x35 0x31    ...P..51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x03 0x35 0x31    ...P..51
0010   0x35 0x00 0x00 0x00 0x00 0x00 0x00 0x00    5.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x09 0x00 0x03    . .P....
0010   0x07 0xd6 0x0a 0x07 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0xd0              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:comm:RTC:2006-10-7T9:0:3
INFO:__main__:READ PUMP ID
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpID>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpID> processing TransmitPacket:ReadPumpID)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpID> sending TransmitPacket:ReadPumpID)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 113, 138, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x71 0x8a 0x00    .....q..
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x09 0x00 0x03    . .P....
0010   0x07 0xd6 0x0a 0x07 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadPumpID, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\t\x00\x03\x07\xd6\n\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpID>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpID>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x09 0x00 0x03    ...P....
0010   0x07 0xd6 0x0a 0x07 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x09 0x00 0x03    ...P....
0010   0x07 0xd6 0x0a 0x07 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x32 0x30 0x38    . .P.208
0010   0x38 0x35 0x30 0x00 0x00 0x00 0x00 0x00    850.....
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0xe3              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:comm:READ PUMP ID: ID: 208850
INFO:__main__:Battery Status
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadBatteryStatus>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBatteryStatus> processing TransmitPacket:ReadBatteryStatus)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBatteryStatus> sending TransmitPacket:ReadBatteryStatus)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 114, 188, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x72 0xbc 0x00    .....r..
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x32 0x30 0x38    . .P.208
0010   0x38 0x35 0x30 0x00 0x00 0x00 0x00 0x00    850.....
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadBatteryStatus, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00208850\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBatteryStatus>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBatteryStatus>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x32 0x30 0x38    ...P.208
0010   0x38 0x35 0x30 0x00 0x00 0x00 0x00 0x00    850.....
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x32 0x30 0x38    ...P.208
0010   0x38 0x35 0x30 0x00 0x00 0x00 0x00 0x00    850.....
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x00 0x76    . .P...v
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0xc7              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:comm:READ Battery Status: {'status': 'normal', 'voltage': 1.18}
INFO:__main__:Firmware Version
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadFirmwareVersion>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadFirmwareVersion> processing TransmitPacket:ReadFirmwareVersion)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadFirmwareVersion> sending TransmitPacket:ReadFirmwareVersion)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 116, 208, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x74 0xd0 0x00    .....t..
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x00 0x76    . .P...v
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadFirmwareVersion, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x00\x00v\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadFirmwareVersion>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadFirmwareVersion>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x00 0x76    ...P...v
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x00 0x76    ...P...v
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x56 0x45 0x52    . .P.VER
0010   0x20 0x32 0x2e 0x31 0x41 0x31 0x2e 0x31     2.1A1.1
0018   0x20 0x0b 0x0b 0x00 0x00 0x00 0x00 0x00     .......
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0xca              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
DEBUG:__main__:READ FIRMWARE HEX:
0000   0x56 0x45 0x52 0x20 0x32 0x2e 0x31 0x41    VER 2.1A
0008   0x31 0x2e 0x31 0x20 0x0b 0x0b 0x00 0x00    1.1 ....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:comm:READ Firmware Version: 'VER 2.1A1.1'
INFO:__main__:remaining insulin
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadRemainingInsulin>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRemainingInsulin> processing TransmitPacket:ReadRemainingInsulin)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRemainingInsulin> sending TransmitPacket:ReadRemainingInsulin)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 115, 39, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x73 0x27 0x00    .....s'.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x56 0x45 0x52    . .P.VER
0010   0x20 0x32 0x2e 0x31 0x41 0x31 0x2e 0x31     2.1A1.1
0018   0x20 0x0b 0x0b 0x00 0x00 0x00 0x00 0x00     .......
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadRemainingInsulin, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00VER 2.1A1.1 \x0b\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRemainingInsulin>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRemainingInsulin>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x56 0x45 0x52    ...P.VER
0010   0x20 0x32 0x2e 0x31 0x41 0x31 0x2e 0x31     2.1A1.1
0018   0x20 0x0b 0x0b 0x00 0x00 0x00 0x00 0x00     .......
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x56 0x45 0x52    ...P.VER
0010   0x20 0x32 0x2e 0x31 0x41 0x31 0x2e 0x31     2.1A1.1
0018   0x20 0x0b 0x0b 0x00 0x00 0x00 0x00 0x00     .......
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x04 0x5f 0x00    . .P.._.
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0xf7              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:READ remaining insulin:
0000   0x04 0x5f 0x00 0x00 0x00 0x00 0x00 0x00    ._......
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:comm:READ Remaining Insulin: 111.9
INFO:__main__:read totals today
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadTotalsToday>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadTotalsToday> processing TransmitPacket:ReadTotalsToday)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadTotalsToday> sending TransmitPacket:ReadTotalsToday)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 121, 147, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x79 0x93 0x00    .....y..
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x04 0x5f 0x00    . .P.._.
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadTotalsToday, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x04_\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadTotalsToday>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadTotalsToday>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x04 0x5f 0x00    ...P.._.
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x04 0x5f 0x00    ...P.._.
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x24 0x00    . .P..$.
0010   0xcd 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x91              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:READ totals today:
0000   0x00 0x24 0x00 0xcd 0x00 0x00 0x00 0x00    .$......
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:comm:READ totals today: {'yesterday': 20.5, 'today': 3.6}
INFO:__main__:read remote IDS
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadRadioCtrlACL>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRadioCtrlACL> processing TransmitPacket:ReadRadioCtrlACL)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRadioCtrlACL> sending TransmitPacket:ReadRadioCtrlACL)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 118, 125, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x76 0x7d 0x00    .....v}.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x24 0x00    . .P..$.
0010   0xcd 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadRadioCtrlACL, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x00$\x00\xcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRadioCtrlACL>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRadioCtrlACL>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x24 0x00    ...P..$.
0010   0xcd 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x24 0x00    ...P..$.
0010   0xcd 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x31 0x32 0x33    . .P.123
0010   0x34 0x35 0x36 0x32 0x31 0x33 0x35 0x34    45621354
0018   0x36 0x38 0x32 0x31 0x36 0x35 0x30 0x00    6821650.
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x5d              .....]
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:READ radio ACL:
0000   0x31 0x32 0x33 0x34 0x35 0x36 0x32 0x31    12345621
0008   0x33 0x35 0x34 0x36 0x38 0x32 0x31 0x36    35468216
0010   0x35 0x30 0x00 0x00 0x00 0x00 0x00 0x00    50......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:comm:READ radio ACL: ['123456', '213546', '821650']
INFO:__main__:read temporary basal
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadBasalTemp>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBasalTemp> processing TransmitPacket:ReadBasalTemp)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBasalTemp> sending TransmitPacket:ReadBasalTemp)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 152, 175, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x98 0xaf 0x00    ........
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x31 0x32 0x33    . .P.123
0010   0x34 0x35 0x36 0x32 0x31 0x33 0x35 0x34    45621354
0018   0x36 0x38 0x32 0x31 0x36 0x35 0x30 0x00    6821650.
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadBasalTemp, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00123456213546821650\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBasalTemp>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBasalTemp>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x31 0x32 0x33    ...P.123
0010   0x34 0x35 0x36 0x32 0x31 0x33 0x35 0x34    45621354
0018   0x36 0x38 0x32 0x31 0x36 0x35 0x30 0x00    6821650.
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x31 0x32 0x33    ...P.123
0010   0x34 0x35 0x36 0x32 0x31 0x33 0x35 0x34    45621354
0018   0x36 0x38 0x32 0x31 0x36 0x35 0x30 0x00    6821650.
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x00 0x00    . .P....
0010   0x4c 0x00 0x00 0x00 0x00 0x00 0x00 0x00    L.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x07              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:READ temporary basal:
0000   0x00 0x00 0x00 0x4c 0x00 0x00 0x00 0x00    ...L....
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:comm:READ temp basal: {'duration': 0, 'rate': 1.9}
INFO:__main__:read settings
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadSettings>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadSettings> processing TransmitPacket:ReadSettings)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadSettings> sending TransmitPacket:ReadSettings)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 192, 76, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0xc0 0x4c 0x00    ......L.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x00 0x00    . .P....
0010   0x4c 0x00 0x00 0x00 0x00 0x00 0x00 0x00    L.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadSettings, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x00\x00\x00L\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadSettings>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadSettings>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x00 0x00    ...P....
0010   0x4c 0x00 0x00 0x00 0x00 0x00 0x00 0x00    L.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x00 0x00    ...P....
0010   0x4c 0x00 0x00 0x00 0x00 0x00 0x00 0x00    L.......
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x03 0x01    . .P....
0010   0x14 0x00 0x64 0x00 0x50 0x00 0x00 0x01    ..d.P...
0018   0x02 0x01 0x00 0x00 0x64 0x00 0x05 0x00    ....d...
0020   0x14 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x9c              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:READ pump settings:
0000   0x00 0x03 0x01 0x14 0x00 0x64 0x00 0x50    .....d.P
0008   0x00 0x00 0x01 0x02 0x01 0x00 0x00 0x64    .......d
0010   0x00 0x05 0x00 0x14 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:comm:READ settings!: {'low_reservoir_warn_point': 20, 'keypad_lock_status': 0, 'maxBasal': 2, 'low_reservoir_warn_type': 0, 'insulinConcentration': 100, 'audio_bolus_enable': True, 'variable_bolus_enable': False, 'alarm': {'volume': 3, 'mode': 2}, 'rf_enable': True, 'block_enable': False, 'timeformat': 0, 'auto_off_duration_hrs': 0, 'audio_bolus_size': 2.0, 'selected_pattern': 2, 'patterns_enabled': True, 'maxBolus': 10.0, 'insulin_action_type': 5}
INFO:__main__:read contrast
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadContrast>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadContrast> processing TransmitPacket:ReadContrast)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadContrast> sending TransmitPacket:ReadContrast)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 195, 122, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0xc3 0x7a 0x00    ......z.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x03 0x01    . .P....
0010   0x14 0x00 0x64 0x00 0x50 0x00 0x00 0x01    ..d.P...
0018   0x02 0x01 0x00 0x00 0x64 0x00 0x05 0x00    ....d...
0020   0x14 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadContrast, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x00\x03\x01\x14\x00d\x00P\x00\x00\x01\x02\x01\x00\x00d\x00\x05\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadContrast>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadContrast>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x03 0x01    ...P....
0010   0x14 0x00 0x64 0x00 0x50 0x00 0x00 0x01    ..d.P...
0018   0x02 0x01 0x00 0x00 0x64 0x00 0x05 0x00    ....d...
0020   0x14 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x03 0x01    ...P....
0010   0x14 0x00 0x64 0x00 0x50 0x00 0x00 0x01    ..d.P...
0018   0x02 0x01 0x00 0x00 0x64 0x00 0x05 0x00    ....d...
0020   0x14 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x02 0x07 0x00    . .P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x5f              ....._
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:READ contrast:
0000   0x02 0x07 0x00 0x00 0x00 0x00 0x00 0x00    ........
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:comm:READ contrast: bytearray(b'\x02\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:__main__:read cur page number
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadCurPageNumber>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadCurPageNumber> processing TransmitPacket:ReadCurPageNumber)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadCurPageNumber> sending TransmitPacket:ReadCurPageNumber)
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 157, 245, 0]
INFO:root:usb.write.len: 16
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x00 0x00 0x02 0x01 0x00 0x9d 0xf5 0x00    ........
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x02 0x07 0x00    . .P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadCurPageNumber, bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x02\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadCurPageNumber>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadCurPageNumber>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x02 0x07 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x02 0x07 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x03 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x00 0x00    . .P....
0010   0x08 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0xb6              ......
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
INFO:__main__:XXX: READ cur page number:
0000   0x00 0x00 0x00 0x08 0x00 0x00 0x00 0x00    ........
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:comm:READ page number!!!: 8L
INFO:__main__:read HISTORY DATA
INFO:session:execute attempt: 1
INFO:session:session transferring packet
INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][0]>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> processing TransmitPacket:ReadHistoryData[page][0])
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> sending TransmitPacket:ReadHistoryData[page][0])
DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 1, 0, 2, 2, 0, 128, 155, 0, 0]
INFO:root:usb.write.len: 17
0000   0x01 0x00 0xa7 0x01 0x20 0x88 0x50 0x80    .... .P.
0008   0x01 0x00 0x02 0x02 0x00 0x80 0x9b 0x00    ........
0010   0x00                                       .
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0xc6 0x80 0x40 0xa7    .U....@.
0008   0x01 0x20 0x88 0x50 0x00 0x00 0x00 0x00    . .P....
0010   0x08 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xc6\x80@\xa7\x01 \x88P\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
INFO:session:sleeping 0.1 before download
INFO:session:proceeding with download
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x00 0x00    ...P....
0010   0x08 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:stick:sleeping in POLL, .100
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x03 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0x00 0x00 0x00 0x00    ...P....
0010   0x08 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: receive in progress!, STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 78
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 2 attempts:size:78
INFO:stick:download_packet:78
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x04 0x00 0xc6 0x00 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0x55 0x07 0x00 0x00    . .PU...
0010   0x03 0x36 0xa3 0x06 0x6c 0xa3 0x06 0x05    .6..l...
0018   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0020   0x36 0x03 0x36 0x64 0x00 0x00 0x00 0x00    6.6d....
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x21 0x00 0x93 0x80 0x08 0x04    ..!.....
0040   0x06 0x03 0x00 0x00 0x00 0x0d 0x95 0x8b    ........
0048   0x28 0x04 0x06 0x03 0x00 0x32              (....2
INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(64), link expects(64)
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
DEBUG:stick:read_status
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0xce    .U......
0008   0x05 0x04 0x00 0x50 0x55 0x07 0x00 0x00    ...PU...
0010   0x03 0x36 0xa3 0x06 0x6c 0xa3 0x06 0x05    .6..l...
0018   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0020   0x36 0x03 0x36 0x64 0x00 0x00 0x00 0x00    6.6d....
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x21 0x00 0x93 0x80 0x08 0x04    ..!.....
INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:stick:LinkStatus:0x03:error:
STATUS: OK
INFO:stick:finished processing LinkStatus:0x03:error:, 206
DEBUG:stick:sleeping in POLL, .100
INFO:stick:STOP POLL after 1 attempts:size:206
INFO:stick:download_packet:206
INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206> sending ReadRadio:size:206)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0xce 0x9e                   .....
DEBUG:stick:sleeping 0.001
INFO:root:usb.read.len: 206
INFO:root:usb.read.raw:
0000   0x02 0x00 0x04 0x00 0xc6 0x00 0xc0 0xa7    ........
0008   0x01 0x20 0x88 0x50 0x3e 0x03 0x00 0x03    . .P>...
0010   0x9e 0x8b 0x08 0x04 0x06 0x07 0x00 0x00    ........
0018   0x03 0x30 0xa4 0x06 0x6c 0xa4 0x06 0x05    .0..l...
0020   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0028   0x30 0x03 0x30 0x64 0x00 0x00 0x00 0x00    0.0d....
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x07 0x00 0x00 0x03 0x36 0xa5    ......6.
0048   0x06 0x6c 0xa5 0x06 0x05 0x0c 0x00 0xe8    .l......
0050   0x00 0x00 0x00 0x00 0x03 0x36 0x03 0x36    .....6.6
0058   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x07    ........
0070   0x00 0x00 0x03 0x36 0xa6 0x06 0x6c 0xa6    ...6..l.
0078   0x06 0x05 0x0c 0x00 0xe8 0x00 0x00 0x00    ........
0080   0x00 0x03 0x36 0x03 0x36 0x64 0x00 0x00    ..6.6d..
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C0   0x60 0x60 0x60 0x60 0x60 0x60 0x60 0x60    ````````
00C8   0x60 0x60 0x60 0x60 0x60 0x60              ``````
INFO:stick:quit send_force_read, found len: 206 expected 206 after 0 attempts
INFO:stick:readData validating remote raw[ack]: 02
INFO:stick:readData; foreign raw should be at least 14 bytes? 206 True
INFO:stick:readData; raw[retries] 0
INFO:stick:found packet len(192), link expects(192)
INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x60:expected_crc(data): 0x4f:raw:
0000   0x02 0x00 0x04 0x00 0xc6 0x00 0xc0 0xa7    ........
0008   0x01 0x20 0x88 0x50 0x3e 0x03 0x00 0x03    . .P>...
0010   0x9e 0x8b 0x08 0x04 0x06 0x07 0x00 0x00    ........
0018   0x03 0x30 0xa4 0x06 0x6c 0xa4 0x06 0x05    .0..l...
0020   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0028   0x30 0x03 0x30 0x64 0x00 0x00 0x00 0x00    0.0d....
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x07 0x00 0x00 0x03 0x36 0xa5    ......6.
0048   0x06 0x6c 0xa5 0x06 0x05 0x0c 0x00 0xe8    .l......
0050   0x00 0x00 0x00 0x00 0x03 0x36 0x03 0x36    .....6.6
0058   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x07    ........
0070   0x00 0x00 0x03 0x36 0xa6 0x06 0x6c 0xa6    ...6..l.
0078   0x06 0x05 0x0c 0x00 0xe8 0x00 0x00 0x00    ........
0080   0x00 0x03 0x36 0x03 0x36 0x64 0x00 0x00    ..6.6d..
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C0   0x60 0x60 0x60 0x60 0x60 0x60 0x60 0x60    ````````
00C8   0x60 0x60 0x60 0x60 0x60 0x60              ``````
:head:
0000   0x03 0x00 0x03 0x9e 0x8b 0x08 0x04 0x06    ........
0008   0x07 0x00 0x00 0x03 0x30 0xa4 0x06 0x6c    ....0..l
0010   0xa4 0x06 0x05 0x0c 0x00 0xe8 0x00 0x00    ........
0018   0x00 0x00 0x03 0x30 0x03 0x30 0x64 0x00    ...0.0d.
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x07 0x00 0x00    ........
0038   0x03 0x36 0xa5 0x06 0x6c 0xa5 0x06 0x05    .6..l...
0040   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0048   0x36 0x03 0x36 0x64 0x00 0x00 0x00 0x00    6.6d....
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x07 0x00 0x00 0x03 0x36 0xa6    ......6.
0068   0x06 0x6c 0xa6 0x06 0x05 0x0c 0x00 0xe8    .l......
0070   0x00 0x00 0x00 0x00 0x03 0x36 0x03 0x36    .....6.6
0078   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x60 0x60 0x60 0x60 0x60    ...`````
00B8   0x60 0x60 0x60 0x60 0x60 0x60 0x60 0x60    ````````
00C0   0x60                                       `
:data:
0000   0x03 0x00 0x03 0x9e 0x8b 0x08 0x04 0x06    ........
0008   0x07 0x00 0x00 0x03 0x30 0xa4 0x06 0x6c    ....0..l
0010   0xa4 0x06 0x05 0x0c 0x00 0xe8 0x00 0x00    ........
0018   0x00 0x00 0x03 0x30 0x03 0x30 0x64 0x00    ...0.0d.
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x07 0x00 0x00    ........
0038   0x03 0x36 0xa5 0x06 0x6c 0xa5 0x06 0x05    .6..l...
0040   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0048   0x36 0x03 0x36 0x64 0x00 0x00 0x00 0x00    6.6d....
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x07 0x00 0x00 0x03 0x36 0xa6    ......6.
0068   0x06 0x6c 0xa6 0x06 0x05 0x0c 0x00 0xe8    .l......
0070   0x00 0x00 0x00 0x00 0x03 0x36 0x03 0x36    .....6.6
0078   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x60 0x60 0x60 0x60 0x60    ...`````
00B8   0x60 0x60 0x60 0x60 0x60 0x60 0x60 0x60    ````````

Traceback (most recent call last):
  File "pump/commands.py", line 556, in <module>
    do_commands(session)
  File "pump/commands.py", line 516, in do_commands
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
stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x60:expected_crc(data): 0x4f:raw:
0000   0x02 0x00 0x04 0x00 0xc6 0x00 0xc0 0xa7    ........
0008   0x01 0x20 0x88 0x50 0x3e 0x03 0x00 0x03    . .P>...
0010   0x9e 0x8b 0x08 0x04 0x06 0x07 0x00 0x00    ........
0018   0x03 0x30 0xa4 0x06 0x6c 0xa4 0x06 0x05    .0..l...
0020   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0028   0x30 0x03 0x30 0x64 0x00 0x00 0x00 0x00    0.0d....
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x07 0x00 0x00 0x03 0x36 0xa5    ......6.
0048   0x06 0x6c 0xa5 0x06 0x05 0x0c 0x00 0xe8    .l......
0050   0x00 0x00 0x00 0x00 0x03 0x36 0x03 0x36    .....6.6
0058   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x07    ........
0070   0x00 0x00 0x03 0x36 0xa6 0x06 0x6c 0xa6    ...6..l.
0078   0x06 0x05 0x0c 0x00 0xe8 0x00 0x00 0x00    ........
0080   0x00 0x03 0x36 0x03 0x36 0x64 0x00 0x00    ..6.6d..
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C0   0x60 0x60 0x60 0x60 0x60 0x60 0x60 0x60    ````````
00C8   0x60 0x60 0x60 0x60 0x60 0x60              ``````
:head:
0000   0x03 0x00 0x03 0x9e 0x8b 0x08 0x04 0x06    ........
0008   0x07 0x00 0x00 0x03 0x30 0xa4 0x06 0x6c    ....0..l
0010   0xa4 0x06 0x05 0x0c 0x00 0xe8 0x00 0x00    ........
0018   0x00 0x00 0x03 0x30 0x03 0x30 0x64 0x00    ...0.0d.
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x07 0x00 0x00    ........
0038   0x03 0x36 0xa5 0x06 0x6c 0xa5 0x06 0x05    .6..l...
0040   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0048   0x36 0x03 0x36 0x64 0x00 0x00 0x00 0x00    6.6d....
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x07 0x00 0x00 0x03 0x36 0xa6    ......6.
0068   0x06 0x6c 0xa6 0x06 0x05 0x0c 0x00 0xe8    .l......
0070   0x00 0x00 0x00 0x00 0x03 0x36 0x03 0x36    .....6.6
0078   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x60 0x60 0x60 0x60 0x60    ...`````
00B8   0x60 0x60 0x60 0x60 0x60 0x60 0x60 0x60    ````````
00C0   0x60                                       `
:data:
0000   0x03 0x00 0x03 0x9e 0x8b 0x08 0x04 0x06    ........
0008   0x07 0x00 0x00 0x03 0x30 0xa4 0x06 0x6c    ....0..l
0010   0xa4 0x06 0x05 0x0c 0x00 0xe8 0x00 0x00    ........
0018   0x00 0x00 0x03 0x30 0x03 0x30 0x64 0x00    ...0.0d.
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x07 0x00 0x00    ........
0038   0x03 0x36 0xa5 0x06 0x6c 0xa5 0x06 0x05    .6..l...
0040   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
0048   0x36 0x03 0x36 0x64 0x00 0x00 0x00 0x00    6.6d....
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x07 0x00 0x00 0x03 0x36 0xa6    ......6.
0068   0x06 0x6c 0xa6 0x06 0x05 0x0c 0x00 0xe8    .l......
0070   0x00 0x00 0x00 0x00 0x03 0x36 0x03 0x36    .....6.6
0078   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x60 0x60 0x60 0x60 0x60    ...`````
00B8   0x60 0x60 0x60 0x60 0x60 0x60 0x60 0x60    ````````

```

```
Command exited with non-zero status 1
python pump/commands.py /dev/ttyUSB0 208850
	elapsed 0:08.38
	user 0.28
	system 0.12
	CPU 4% (0text+0data 61232max)k

```
Was there an ACK ERROR?

### DIAGNOSE CRC
stick.py again.
```
INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
INFO:link:Link opened serial port: Serial<id=0x1220610, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.5, xonxoff=False, rtscts=False, dsrdtr=False)
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc1 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:193
INFO:__main__:finished processing SignalStrength:0x06 0x00, 193
INFO:__main__:we seem to have found a nice signal strength of: 193
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc1 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:193
INFO:__main__:finished processing SignalStrength:0x06 0x00, 193
INFO:__main__:we seem to have found a nice signal strength of: 193
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbf 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:191
INFO:__main__:finished processing SignalStrength:0x06 0x00, 191
INFO:__main__:we seem to have found a nice signal strength of: 191
INFO:__main__:test fetching product info Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)>
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II',
 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')],
 'product.version': '0.0',
 'rf.freq': '916.5Mhz',
 'serial': '0b2c00',
 'software.version': '1.16'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc7 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:199
INFO:__main__:finished processing SignalStrength:0x06 0x00, 199
INFO:__main__:we seem to have found a nice signal strength of: 199
INFO:__main__:at this point, we could issue remote commands to a medical
    device, let's inspect the interfaces
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x91 0x00 0x00 0x00 0x91 0x00    ........
0010   0x92 0x00 0xa3 0x00 0x90 0x04 0x00 0x00    ........
0018   0x05 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 145L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 145L, 'errors.crc': 0}
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x19 0x00 0x00 0x00 0x1a 0x00    ........
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x08 0x00    ........
0018   0x16 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x04 0x01 0xd2 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 26L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 25L, 'errors.crc': 0}
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 25L,
           'packets.transmit': 26L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 145L,
         'packets.transmit': 145L}}
```

Note the counters:
```javascript
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 25L,
           'packets.transmit': 26L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 145L,
         'packets.transmit': 145L}}
```


```
INFO:__main__:CLEAR BUFFERS
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x93 0x00 0x00 0x00 0x93 0x00    ........
0010   0x94 0x00 0xa5 0x00 0x92 0x04 0x00 0x00    ........
0018   0x05 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x04 0x01 0xd2 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 147L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 147L, 'errors.crc': 0}
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x1a 0x00 0x00 0x00 0x1b 0x00    ........
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x09 0x00    ........
0018   0x17 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x01 0xd2 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 27L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 26L, 'errors.crc': 0}
DEBUG:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 26L,
           'packets.transmit': 27L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 147L,
         'packets.transmit': 147L}}
```

Note the counters:
```javascript
DEBUG:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 26L,
           'packets.transmit': 27L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 147L,
         'packets.transmit': 147L}}
```

We added one to both our radio received and transmit counters.

```
INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
DEBUG:__main__:<Stick:status:None:command:<RadioStats:0x05 0x00:size(64)>>:STARTING POLL PHASE:attempt:0
DEBUG:__main__:<Stick:status:None:command:<RadioStats:0x05 0x00:size(64)>>:poll:attempt:0
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x01 0x4e    .U.....N
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x1b 0x00    ........
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x09 0x00    ........
0018   0x17 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x01 0xd2 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:
STATUS: OK
INFO:__main__:finished processing LinkStatus:0x03:error:, 334
DEBUG:__main__:sleeping in POLL, .100
INFO:__main__:STOP POLL after 1 attempts:size:334
INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 334
INFO:__main__:XXX:clear_buffer[attempt][0]:download the size? 334:segments[0],total_segments[0]:raw[0]
INFO:__main__:XXX:clear_buffer[attempt][0] size:334:segments[0],total_segments[0]:raw[0]:clear_buffer BUFFER self.download( )
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(334)>:command:<LinkStatus:0x03:error::size(334)>>:STARTING POLL PHASE:attempt:0
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(334)>:command:<LinkStatus:0x03:error::size(334)>>:poll:attempt:0
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(334)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(334)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x01 0xce    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x1b 0x00    ........
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x09 0x00    ........
0018   0x17 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x01 0xd2 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:
STATUS: OK
INFO:__main__:finished processing LinkStatus:0x03:error:, 462
DEBUG:__main__:sleeping in POLL, .100
INFO:__main__:STOP POLL after 1 attempts:size:462
INFO:__main__:download_packet:462
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(462)>:command:<ReadRadio:size:462> sending ReadRadio:size:462)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x01 0xce 0x88                   .....
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 462
INFO:root:usb.read.raw:
0000   0x02 0x00 0x04 0x00 0xc6 0x01 0xc0 0xa7    ........
0008   0x01 0x20 0x88 0x50 0xe8 0x00 0x00 0x00    . .P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0070   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0078   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00D0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00D8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00E0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00E8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00F0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00F8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0100   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0108   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0110   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0118   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0120   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0128   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0130   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0138   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0140   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0148   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0150   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0158   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0160   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0168   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0170   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0178   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0180   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0188   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0190   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0198   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01C0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01C8   0x00 0x00 0x00 0x00 0x00 0x00              ......
INFO:__main__:quit send_force_read, found len: 462 expected 462 after 0 attempts
INFO:__main__:readData validating remote raw[ack]: 02
INFO:__main__:readData; foreign raw should be at least 14 bytes? 462 True
INFO:__main__:readData; raw[retries] 0
INFO:__main__:found packet len(448), link expects(448)
WARNING:__main__:bad zero CRC?
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(462)>:command:<ReadRadio:size:462>>:STARTING POLL PHASE:attempt:0
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(462)>:command:<ReadRadio:size:462>>:poll:attempt:0
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(462)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(462)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x8e    .U......
0008   0x05 0x04 0x00 0x50 0xe8 0x00 0x00 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:
STATUS: OK
INFO:__main__:finished processing LinkStatus:0x03:error:, 142
DEBUG:__main__:sleeping in POLL, .100
INFO:__main__:STOP POLL after 1 attempts:size:142
INFO:__main__:download_packet:142
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x8e 0x56                   ....V
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 142
INFO:root:usb.read.raw:
0000   0x02 0x00 0x04 0x00 0xc6 0x00 0x80 0xa7    ........
0008   0x01 0x20 0x88 0x50 0xc6 0x00 0x00 0x00    . .P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0070   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0078   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00              ......
INFO:__main__:quit send_force_read, found len: 142 expected 142 after 0 attempts
INFO:__main__:readData validating remote raw[ack]: 02
INFO:__main__:readData; foreign raw should be at least 14 bytes? 142 True
INFO:__main__:readData; raw[retries] 0
INFO:__main__:found packet len(128), link expects(128)
WARNING:__main__:bad zero CRC?
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x8e    .U......
0008   0x05 0x04 0x00 0x50 0xc6 0x00 0x00 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:
STATUS: OK
INFO:__main__:finished processing LinkStatus:0x03:error:, 142
DEBUG:__main__:sleeping in POLL, .100
INFO:__main__:STOP POLL after 1 attempts:size:142
INFO:__main__:download_packet:142
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x8e 0x56                   ....V
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 142
INFO:root:usb.read.raw:
0000   0x02 0x00 0x04 0x00 0xc6 0x00 0x80 0xa7    ........
0008   0x01 0x20 0x88 0x50 0xc6 0x00 0x00 0x00    . .P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0070   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0078   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00              ......
INFO:__main__:quit send_force_read, found len: 142 expected 142 after 0 attempts
INFO:__main__:readData validating remote raw[ack]: 02
INFO:__main__:readData; foreign raw should be at least 14 bytes? 142 True
INFO:__main__:readData; raw[retries] 0
INFO:__main__:found packet len(128), link expects(128)
WARNING:__main__:bad zero CRC?
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x01 0x00 0x4e    .U.....N
0008   0x05 0x04 0x00 0x50 0xc6 0x00 0x00 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:
STATUS: OK
INFO:__main__:finished processing LinkStatus:0x03:error:, 78
DEBUG:__main__:sleeping in POLL, .100
INFO:__main__:STOP POLL after 1 attempts:size:78
INFO:__main__:download_packet:78
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
INFO:root:usb.write.len: 5
0000   0x0c 0x00 0x00 0x4e 0x95                   ...N.
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 78
INFO:root:usb.read.raw:
0000   0x02 0x00 0x04 0x00 0xc6 0x80 0x40 0xa7    ......@.
0008   0x01 0x20 0x88 0x50 0xd6 0x00 0x00 0x00    . .P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0xcf 0x1b 0x3a              .....:
INFO:__main__:quit send_force_read, found len: 78 expected 78 after 0 attempts
INFO:__main__:readData validating remote raw[ack]: 02
INFO:__main__:readData; foreign raw should be at least 14 bytes? 78 True
INFO:__main__:readData; raw[retries] 0
INFO:__main__:found packet len(64), link expects(64)
INFO:__main__:XXX:clear_buffer[attempt][0]:tx:found:segments[1],total_segments[768]:raw[768]:len(raw):768:expected:334:len(segment):768
INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 768 segment:segments[1],total_segments[768]:raw[768]:RAW:
0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0070   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0078   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00D0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00D8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00E0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00E8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00F0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00F8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0100   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0108   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0110   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0118   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0120   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0128   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0130   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0138   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0140   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0148   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0150   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0158   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0160   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0168   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0170   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0178   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0180   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0188   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0190   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0198   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01C0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01C8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01D0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01D8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01E0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01E8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01F0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01F8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0200   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0208   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0210   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0218   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0220   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0228   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0230   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0238   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0240   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0248   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0250   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0258   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0260   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0268   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0270   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0278   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0280   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0288   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0290   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0298   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02C0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02C8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02D0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02D8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02E0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02E8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02F0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02F8   0x00 0x00 0x00 0x00 0x00 0x00 0xcf 0x1b    ........
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0xd6 0x00 0x00 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0xd6 0x00 0x00 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:2
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0xd6 0x00 0x00 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:3
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x50 0xd6 0x00 0x00 0x00    ...P....
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
INFO:__main__:STOP POLL after 4 attempts:size:0
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0xa2 0x00 0x00 0x00 0xa2 0x00    ........
0010   0xa3 0x00 0xbf 0x00 0xa1 0x04 0x00 0x00    ........
0018   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 162L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 162L, 'errors.crc': 0}
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x21 0x00 0x00 0x00 0x22 0x00    ..!...".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 34L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 33L, 'errors.crc': 0}
DEBUG:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 33L,
           'packets.transmit': 34L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 162L,
         'packets.transmit': 162L}}
```

Note the counters:
```javascript
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 33L,
           'packets.transmit': 34L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 162L,
         'packets.transmit': 162L}}
```

We added a bunch to our radio counters, `+4`?

```
INFO:__main__:0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0048   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0070   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0078   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0090   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0098   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00C8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00D0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00D8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00E0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00E8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00F0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
00F8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0100   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0108   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0110   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0118   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0120   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0128   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0130   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0138   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0140   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0148   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0150   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0158   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0160   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0168   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0170   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0178   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0180   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0188   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0190   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0198   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01C0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01C8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01D0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01D8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01E0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01E8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01F0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
01F8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0200   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0208   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0210   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0218   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0220   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0228   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0230   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0238   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0240   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0248   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0250   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0258   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0260   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0268   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0270   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0278   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0280   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0288   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0290   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0298   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02A0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02A8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02B0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02B8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02C0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02C8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02D0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02D8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02E0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02E8   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02F0   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
02F8   0x00 0x00 0x00 0x00 0x00 0x00 0xcf 0x1b    ........
INFO:__main__:DONE CLEARING BUFFERS
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0xa4 0x00 0x00 0x00 0xa4 0x00    ........
0010   0xa5 0x00 0xc1 0x00 0xa3 0x04 0x00 0x00    ........
0018   0x05 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 164L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 164L, 'errors.crc': 0}
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x21 0x00 0x00 0x00 0x22 0x00    ..!...".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 34L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 33L, 'errors.crc': 0}
INFO:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 33L,
           'packets.transmit': 34L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 164L,
         'packets.transmit': 164L}}
```
Note the counters:
```javascript
INFO:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 33L,
           'packets.transmit': 34L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 164L,
         'packets.transmit': 164L}}
```

```
python pump/stick.py /dev/ttyUSB0
	elapsed 0:02.75
	user 0.18
	system 0.02
	CPU 7% (0text+0data 42208max)k
```

So we clearly downloaded a page of data successfully, AFTER the CRC,
simply by polling and emptying the radio buffer.

This should probably be the new standard behavior for the download
command.

### Final stick

```
INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
INFO:link:Link opened serial port: Serial<id=0x1c0d610, open=True>(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0.5, xonxoff=False, rtscts=False, dsrdtr=False)
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbd 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:189
INFO:__main__:finished processing SignalStrength:0x06 0x00, 189
INFO:__main__:we seem to have found a nice signal strength of: 189
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc3 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:195
INFO:__main__:finished processing SignalStrength:0x06 0x00, 195
INFO:__main__:we seem to have found a nice signal strength of: 195
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xbd 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:189
INFO:__main__:finished processing SignalStrength:0x06 0x00, 189
INFO:__main__:we seem to have found a nice signal strength of: 189
INFO:__main__:test fetching product info Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)>
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
INFO:root:usb.write.len: 3
0000   0x04 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x0b 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
INFO:__main__:{'description': 'ComLink II',
 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')],
 'product.version': '0.0',
 'rf.freq': '916.5Mhz',
 'serial': '0b2c00',
 'software.version': '1.16'}
INFO:__main__:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
INFO:root:usb.write.len: 3
0000   0x06 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0xc4 0x2c 0x00 0x00 0x00    .U..,...
0008   0x00 0x43 0x6f 0x6d 0x4c 0x69 0x6e 0x6b    .ComLink
0010   0x20 0x49 0x49 0x01 0x10 0x02 0x00 0x01     II.....
0018   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:196
INFO:__main__:finished processing SignalStrength:0x06 0x00, 196
INFO:__main__:we seem to have found a nice signal strength of: 196
INFO:__main__:at this point, we could issue remote commands to a medical
    device, let's inspect the interfaces
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0xae 0x00 0x00 0x00 0xae 0x00    ........
0010   0xaf 0x00 0xcb 0x00 0xad 0x04 0x00 0x00    ........
0018   0x05 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 174L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 174L, 'errors.crc': 0}
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x21 0x00 0x00 0x00 0x22 0x00    ..!...".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 34L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 33L, 'errors.crc': 0}
INFO:__main__:{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 33L,
           'packets.transmit': 34L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 174L,
         'packets.transmit': 174L}}
INFO:__main__:CLEAR BUFFERS
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0xb0 0x00 0x00 0x00 0xb0 0x00    ........
0010   0xb1 0x00 0xcd 0x00 0xaf 0x04 0x00 0x00    ........
0018   0x05 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 176L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 176L, 'errors.crc': 0}
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x21 0x00 0x00 0x00 0x22 0x00    ..!...".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 34L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 33L, 'errors.crc': 0}
DEBUG:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 33L,
           'packets.transmit': 34L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 176L,
         'packets.transmit': 176L}}
INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
DEBUG:__main__:<Stick:status:None:command:<RadioStats:0x05 0x00:size(64)>>:STARTING POLL PHASE:attempt:0
DEBUG:__main__:<Stick:status:None:command:<RadioStats:0x05 0x00:size(64)>>:poll:attempt:0
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x22 0x00    ......".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x22 0x00    ......".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:2
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x22 0x00    ......".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
DEBUG:__main__:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:3
DEBUG:__main__:read_status
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
INFO:root:usb.write.len: 3
0000   0x03 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x02 0x00 0x00 0x00    .U......
0008   0x05 0x04 0x00 0x00 0x00 0x00 0x22 0x00    ......".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:LinkStatus:0x03:error:LinkStatus:error:True:reason:

INFO:__main__:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
DEBUG:__main__:sleeping in POLL, .100
INFO:__main__:STOP POLL after 4 attempts:size:0
INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 0
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0xb6 0x00 0x00 0x00 0xb6 0x00    ........
0010   0xb7 0x00 0xd3 0x00 0xb5 0x04 0x00 0x00    ........
0018   0x05 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 182L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 182L, 'errors.crc': 0}
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x21 0x00 0x00 0x00 0x22 0x00    ..!...".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 34L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 33L, 'errors.crc': 0}
INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 33L,
           'packets.transmit': 34L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 182L,
         'packets.transmit': 182L}}
INFO:__main__:NO PENDING BUFFER
INFO:__main__:DONE CLEARING BUFFERS
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
INFO:root:usb.write.len: 3
0000   0x05 0x01 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0xb8 0x00 0x00 0x00 0xb8 0x00    ........
0010   0xb9 0x00 0xd5 0x00 0xb7 0x04 0x00 0x00    ........
0018   0x05 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 184L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 184L, 'errors.crc': 0}
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
INFO:__main__:send_force_read: attempt 0/5 send command, read until we get something within some timeout
INFO:__main__:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
INFO:root:usb.write.len: 3
0000   0x05 0x00 0x00                             ...
DEBUG:__main__:sleeping 0.001
INFO:root:usb.read.len: 64
INFO:root:usb.read.raw:
0000   0x01 0x55 0x00 0x00 0x00 0x00 0x00 0x00    .U......
0008   0x00 0x00 0x21 0x00 0x00 0x00 0x22 0x00    ..!...".
0010   0x00 0x00 0x10 0x00 0x03 0x00 0x10 0x00    ........
0018   0x1e 0x00 0x02 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x01 0x00 0x11 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
INFO:__main__:quit send_force_read, found len: 64 expected 64 after 0 attempts
INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 0, 'packets.transmit': 34L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 33L, 'errors.crc': 0}
INFO:__main__:INTERFACE STATS:
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 33L,
           'packets.transmit': 34L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 184L,
         'packets.transmit': 184L}}
python pump/stick.py /dev/ttyUSB0
	elapsed 0:01.22
	user 0.11
	system 0.02
	CPU 11% (0text+0data 42080max)k
```

Counters for radio remain the same.

### previously

```bash
$ grep -E "cleaer_bu|ACKK|ReadHistory|traceback|criticial" status-quo.log
```
```
  echo "Was there an ACK ERROR?"
INFO:__main__:XXX:clear_buffer[attempt][0]:BEGIN
INFO:__main__:XXX:clear_buffer[attempt][0] can we poll the size? 0
INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][0]>
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> processing TransmitPacket:ReadHistoryData[page][0])
INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> sending TransmitPacket:ReadHistoryData[page][0])
INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xd2\x80@\xa7\x01 \x88P\x8b\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:STARTING POLL PHASE:attempt:0
DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:poll:attempt:0
INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x7a:raw:
stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x7a:raw:
Was there an ACK ERROR?
INFO:__main__:XXX:clear_buffer[attempt][0]:BEGIN
INFO:__main__:XXX:clear_buffer[attempt][0] can we poll the size? 398
INFO:__main__:XXX:clear_buffer[attempt][0] size:398 TO clear_buffer CLEAR BUFFER
INFO:__main__:XXX:clear_buffer[attempt][0]:tx:found:len(raw):768:expected:398:len(segment):768
INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 768 segment
```

## What happened

```bash
$ grep -n --color  -E
"clear_bu|ACK|IGNORE|ReadHistory|stick|traceback|critical|errors.(crc|naks|sequence|timeouts|received|transmit)"
status-quo.log   >> crc-errors.markdown 
```

Run a few more times with/without success, then get this:

```
14:  TIME="$TIME" time python pump/stick.py ${PORT}
17:  echo "Was there an ACK ERROR?"
19:  TIME="$TIME" time -f "$TIME" python pump/stick.py ${PORT}
20:  TIME="$TIME" time -f "$TIME" python pump/stick.py ${PORT}
27:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
214:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1953L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1953L, 'errors.crc': 0}
232:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 949L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 900L, 'errors.crc': 0}
233:INFO:__main__:{'radio': {'errors.crc': 0,
234:           'errors.naks': 0,
235:           'errors.sequence': 0,
236:           'errors.timeouts': 3,
237:           'packets.received': 900L,
238:           'packets.transmit': 949L},
239: 'usb': {'errors.crc': 0,
240:         'errors.naks': 0,
241:         'errors.sequence': 0,
242:         'errors.timeouts': 0,
243:         'packets.received': 1953L,
244:         'packets.transmit': 1953L}}
263:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1955L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1955L, 'errors.crc': 0}
281:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 949L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 900L, 'errors.crc': 0}
283:{'radio': {'errors.crc': 0,
284:           'errors.naks': 0,
285:           'errors.sequence': 0,
286:           'errors.timeouts': 3,
287:           'packets.received': 900L,
288:           'packets.transmit': 949L},
289: 'usb': {'errors.crc': 0,
290:         'errors.naks': 0,
291:         'errors.sequence': 0,
292:         'errors.timeouts': 0,
293:         'packets.received': 1955L,
294:         'packets.transmit': 1955L}}
295:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
390:INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 0
408:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1961L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1961L, 'errors.crc': 0}
426:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 949L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 900L, 'errors.crc': 0}
427:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
428:{'radio': {'errors.crc': 0,
429:           'errors.naks': 0,
430:           'errors.sequence': 0,
431:           'errors.timeouts': 3,
432:           'packets.received': 900L,
433:           'packets.transmit': 949L},
434: 'usb': {'errors.crc': 0,
435:         'errors.naks': 0,
436:         'errors.sequence': 0,
437:         'errors.timeouts': 0,
438:         'packets.received': 1961L,
439:         'packets.transmit': 1961L}}
459:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1963L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1963L, 'errors.crc': 0}
477:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 949L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 900L, 'errors.crc': 0}
479:{'radio': {'errors.crc': 0,
480:           'errors.naks': 0,
481:           'errors.sequence': 0,
482:           'errors.timeouts': 3,
483:           'packets.received': 900L,
484:           'packets.transmit': 949L},
485: 'usb': {'errors.crc': 0,
486:         'errors.naks': 0,
487:         'errors.sequence': 0,
488:         'errors.timeouts': 0,
489:         'packets.received': 1963L,
490:         'packets.transmit': 1963L}}
491:python pump/stick.py /dev/ttyUSB0
498:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
499:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
500:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
503:DEBUG:stick:sleeping 0.001
514:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
515:INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
516:INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
517:INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
518:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
519:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
520:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
523:DEBUG:stick:sleeping 0.001
534:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
535:INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:191
536:INFO:stick:finished processing SignalStrength:0x06 0x00, 191
537:INFO:stick:we seem to have found a nice signal strength of: 191
538:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
539:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
540:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
543:DEBUG:stick:sleeping 0.001
554:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
555:INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
556:INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
557:INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
558:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
559:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
560:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
563:DEBUG:stick:sleeping 0.001
574:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
575:INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:195
576:INFO:stick:finished processing SignalStrength:0x06 0x00, 195
577:INFO:stick:we seem to have found a nice signal strength of: 195
578:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
579:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
580:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
583:DEBUG:stick:sleeping 0.001
594:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
595:INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
596:INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
597:INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
598:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
599:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
600:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
603:DEBUG:stick:sleeping 0.001
614:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
615:INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:193
616:INFO:stick:finished processing SignalStrength:0x06 0x00, 193
617:INFO:stick:we seem to have found a nice signal strength of: 193
619:INFO:stick:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
620:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
621:INFO:stick:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
624:DEBUG:stick:sleeping 0.001
635:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
636:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1971L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1971L, 'errors.crc': 0}
637:INFO:stick:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
638:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
639:INFO:stick:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
642:DEBUG:stick:sleeping 0.001
653:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
654:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 949L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 900L, 'errors.crc': 0}
655:INFO:__main__:{'radio': {'errors.crc': 0,
656:           'errors.naks': 0,
657:           'errors.sequence': 0,
658:           'errors.timeouts': 3,
659:           'packets.received': 900L,
660:           'packets.transmit': 949L},
661: 'usb': {'errors.crc': 0,
662:         'errors.naks': 0,
663:         'errors.sequence': 0,
664:         'errors.timeouts': 0,
665:         'packets.received': 1971L,
666:         'packets.transmit': 1971L}}
670:INFO:stick:transmit_packet:write:<TransmitPacket:PowerControl>
671:INFO:stick:link Stick:status:None:command:<TransmitPacket:PowerControl> processing TransmitPacket:PowerControl)
672:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
673:INFO:stick:link Stick:status:None:command:<TransmitPacket:PowerControl> sending TransmitPacket:PowerControl)
674:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 2, 85, 0, 0, 0, 93, 122, 1, 10, 162]
679:DEBUG:stick:sleeping 0.001
690:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
691:INFO:stick:finished processing TransmitPacket:PowerControl, bytearray(b'\x00\x00\x00\x03\x00\x00\x03\x84\x00\x00\x03\xb5\x00\x00\x00\x9f\x00<\x02\xe1\x03H\x005\x00\x00\x00\x00\x00\x00\x01\x00\xe2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
695:DEBUG:stick:<Stick:status:None:command:<TransmitPacket:PowerControl>>:STARTING POLL PHASE:attempt:0
696:DEBUG:stick:<Stick:status:None:command:<TransmitPacket:PowerControl>>:poll:attempt:0
697:DEBUG:stick:read_status
698:INFO:stick:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
699:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
700:INFO:stick:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
703:DEBUG:stick:sleeping 0.001
707:INFO:stick:zero length READ, try once more sleep .250
718:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
719:INFO:stick:LinkStatus:0x03:error:
721:INFO:stick:finished processing LinkStatus:0x03:error:, 15
722:DEBUG:stick:sleeping in POLL, .100
723:INFO:stick:STOP POLL after 1 attempts:size:15
724:INFO:stick:download_packet:15
725:ERROR:stick:size is less than 64, which will cause an error. trying 64 instead
726:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
727:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<ReadRadio:size:15> sending ReadRadio:size:15)
730:DEBUG:stick:sleeping 0.001
735:INFO:stick:quit send_force_read, found len: 15 expected 64 after 0 attempts
736:INFO:stick:readData validating remote raw[ack]: 02
737:INFO:stick:readData; foreign raw should be at least 14 bytes? 15 True
738:INFO:stick:readData; raw[retries] 0
739:INFO:stick:found packet len(1), link expects(1)
740:WARNING:stick:bad zero CRC?
743:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
744:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
745:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
748:DEBUG:stick:sleeping 0.001
759:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
760:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1976L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1976L, 'errors.crc': 0}
761:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
762:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
763:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
766:DEBUG:stick:sleeping 0.001
777:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
778:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 951L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 902L, 'errors.crc': 0}
```


```
779:INFO:__main__:{'radio': {'errors.crc': 0,
780:           'errors.naks': 0,
781:           'errors.sequence': 0,
782:           'errors.timeouts': 3,
783:           'packets.received': 902L,
784:           'packets.transmit': 951L},
785: 'usb': {'errors.crc': 0,
786:         'errors.naks': 0,
787:         'errors.sequence': 0,
788:         'errors.timeouts': 0,
789:         'packets.received': 1976L,
790:         'packets.transmit': 1976L}}
```

## Begin pump comms notice, we have a nice baseline above
Let's start a session.

```
779:INFO:__main__:{'radio': {'errors.crc': 0,
780:           'errors.naks': 0,
781:           'errors.sequence': 0,
782:           'errors.timeouts': 3,
783:           'packets.received': 902L,
784:           'packets.transmit': 951L},
785: 'usb': {'errors.crc': 0,
786:         'errors.naks': 0,
787:         'errors.sequence': 0,
788:         'errors.timeouts': 0,
789:         'packets.received': 1976L,
790:         'packets.transmit': 1976L}}
793:INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpModel>
794:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<TransmitPacket:ReadPumpModel> processing TransmitPacket:ReadPumpModel)
795:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
796:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<TransmitPacket:ReadPumpModel> sending TransmitPacket:ReadPumpModel)
797:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 141, 199, 0]
801:DEBUG:stick:sleeping 0.001
812:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
813:INFO:stick:finished processing TransmitPacket:ReadPumpModel, bytearray(b'\x00\x00\x00\x03\x00\x00\x03\x86\x00\x00\x03\xb7\x00\x00\x00\xa0\x00>\x02\xe1\x03H\x006\x00\x00\x00\x00\x00\x00\x01\x00\xe4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
816:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(15)>:command:<TransmitPacket:ReadPumpModel>>:STARTING POLL PHASE:attempt:0
817:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(15)>:command:<TransmitPacket:ReadPumpModel>>:poll:attempt:0
818:DEBUG:stick:read_status
819:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
820:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
821:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(15)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
824:DEBUG:stick:sleeping 0.001
835:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
836:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
838:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
839:DEBUG:stick:sleeping in POLL, .100
840:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
841:DEBUG:stick:read_status
842:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
843:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
844:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
847:DEBUG:stick:sleeping 0.001
858:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
859:INFO:stick:LinkStatus:0x03:error:
861:INFO:stick:finished processing LinkStatus:0x03:error:, 78
862:DEBUG:stick:sleeping in POLL, .100
863:INFO:stick:STOP POLL after 2 attempts:size:78
864:INFO:stick:download_packet:78
865:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
866:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
869:DEBUG:stick:sleeping 0.001
882:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
883:INFO:stick:readData validating remote raw[ack]: 02
884:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
885:INFO:stick:readData; raw[retries] 0
886:INFO:stick:found packet len(64), link expects(64)
888:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
889:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
890:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
893:DEBUG:stick:sleeping 0.001
904:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
905:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1982L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1982L, 'errors.crc': 0}
906:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
907:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
908:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
911:DEBUG:stick:sleeping 0.001
922:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
923:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 952L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 903L, 'errors.crc': 0}
```

We exchanged a single packet.
Very nice.


## sent and receive  one packet
```
924:INFO:__main__:{'radio': {'errors.crc': 0,
925:           'errors.naks': 0,
926:           'errors.sequence': 0,
927:           'errors.timeouts': 3,
928:           'packets.received': 903L,
929:           'packets.transmit': 952L},
930: 'usb': {'errors.crc': 0,
931:         'errors.naks': 0,
932:         'errors.sequence': 0,
933:         'errors.timeouts': 0,
934:         'packets.received': 1982L,
935:         'packets.transmit': 1982L}}
943:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
944:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
945:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
948:DEBUG:stick:sleeping 0.001
959:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
960:INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
961:INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
962:INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
963:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
964:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
965:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
968:DEBUG:stick:sleeping 0.001
979:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
980:INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:192
981:INFO:stick:finished processing SignalStrength:0x06 0x00, 192
982:INFO:stick:we seem to have found a nice signal strength of: 192
983:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
984:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
985:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
988:DEBUG:stick:sleeping 0.001
999:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1000:INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
1001:INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
1002:INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
1003:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
1004:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1005:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
1008:DEBUG:stick:sleeping 0.001
1019:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1020:INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:192
1021:INFO:stick:finished processing SignalStrength:0x06 0x00, 192
1022:INFO:stick:we seem to have found a nice signal strength of: 192
1023:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> processing ProductInfo:0x04)
1024:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1025:INFO:stick:link Stick:status:None:command:<ProductInfo:0x04:size(64)> sending ProductInfo:0x04)
1028:DEBUG:stick:sleeping 0.001
1039:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1040:INFO:stick:finished processing ProductInfo:0x04, {'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
1041:INFO:stick:{'description': 'ComLink II', 'software.version': '1.16', 'interfaces': [(0, 'Paradigm RF'), (1, 'USB')], 'product.version': '0.0', 'rf.freq': '916.5Mhz', 'serial': '0b2c00'}
1042:INFO:stick:get signal strength of Stick:status:None:command:<ProductInfo:0x04:size(64)>
1043:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> processing SignalStrength:0x06 0x00)
1044:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1045:INFO:stick:link Stick:status:None:command:<SignalStrength:0x06 0x00:size(64)> sending SignalStrength:0x06 0x00)
1048:DEBUG:stick:sleeping 0.001
1059:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1060:INFO:stick:<SignalStrength:0x06 0x00:size(64)>:readSignalStrength:192
1061:INFO:stick:finished processing SignalStrength:0x06 0x00, 192
1062:INFO:stick:we seem to have found a nice signal strength of: 192
1064:INFO:stick:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
1065:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1066:INFO:stick:link Stick:status:None:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
1069:DEBUG:stick:sleeping 0.001
1080:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1081:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 1990L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1990L, 'errors.crc': 0}
1082:INFO:stick:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
1083:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1084:INFO:stick:link Stick:status:None:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
1087:DEBUG:stick:sleeping 0.001
1098:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1099:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 952L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 903L, 'errors.crc': 0}
1100:INFO:__main__:{'radio': {'errors.crc': 0,
1101:           'errors.naks': 0,
1102:           'errors.sequence': 0,
1103:           'errors.timeouts': 3,
1104:           'packets.received': 903L,
1105:           'packets.transmit': 952L},
1106: 'usb': {'errors.crc': 0,
1107:         'errors.naks': 0,
1108:         'errors.sequence': 0,
1109:         'errors.timeouts': 0,
1110:         'packets.received': 1990L,
1111:         'packets.transmit': 1990L}}
1114:INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpModel>
1115:INFO:stick:link Stick:status:None:command:<TransmitPacket:ReadPumpModel> processing TransmitPacket:ReadPumpModel)
1116:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1117:INFO:stick:link Stick:status:None:command:<TransmitPacket:ReadPumpModel> sending TransmitPacket:ReadPumpModel)
1118:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 141, 199, 0]
1122:DEBUG:stick:sleeping 0.001
1133:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1134:INFO:stick:finished processing TransmitPacket:ReadPumpModel, bytearray(b'\x00\x00\x00\x03\x00\x00\x03\x87\x00\x00\x03\xb8\x00\x00\x00\xa1\x00>\x02\xe1\x03I\x006\x00\x00\x00\x00\x00\x00\x01\x00\xed\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1137:DEBUG:stick:<Stick:status:None:command:<TransmitPacket:ReadPumpModel>>:STARTING POLL PHASE:attempt:0
1138:DEBUG:stick:<Stick:status:None:command:<TransmitPacket:ReadPumpModel>>:poll:attempt:0
1139:DEBUG:stick:read_status
1140:INFO:stick:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1141:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1142:INFO:stick:link Stick:status:None:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1145:DEBUG:stick:sleeping 0.001
1156:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1157:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1159:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1160:DEBUG:stick:sleeping in POLL, .100
1161:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1162:DEBUG:stick:read_status
1163:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1164:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1165:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1168:DEBUG:stick:sleeping 0.001
1179:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1180:INFO:stick:LinkStatus:0x03:error:
1182:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1183:DEBUG:stick:sleeping in POLL, .100
1184:INFO:stick:STOP POLL after 2 attempts:size:78
1185:INFO:stick:download_packet:78
1186:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1187:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
1190:DEBUG:stick:sleeping 0.001
1203:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
1204:INFO:stick:readData validating remote raw[ack]: 02
1205:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
1206:INFO:stick:readData; raw[retries] 0
1207:INFO:stick:found packet len(64), link expects(64)
1211:INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpModel>
1212:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpModel> processing TransmitPacket:ReadPumpModel)
1213:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1214:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpModel> sending TransmitPacket:ReadPumpModel)
1215:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 141, 199, 0]
1219:DEBUG:stick:sleeping 0.001
1230:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1231:INFO:stick:finished processing TransmitPacket:ReadPumpModel, bytearray(b'\x00\xcc\x80@\xa7\x01 \x88P\x88\x03515\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1234:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpModel>>:STARTING POLL PHASE:attempt:0
1235:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpModel>>:poll:attempt:0
1236:DEBUG:stick:read_status
1237:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1238:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1239:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1242:DEBUG:stick:sleeping 0.001
1253:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1254:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1256:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1257:DEBUG:stick:sleeping in POLL, .100
1258:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1259:DEBUG:stick:read_status
1260:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1261:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1262:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1265:DEBUG:stick:sleeping 0.001
1276:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1277:INFO:stick:LinkStatus:0x03:error:
1279:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1280:DEBUG:stick:sleeping in POLL, .100
1281:INFO:stick:STOP POLL after 2 attempts:size:78
1282:INFO:stick:download_packet:78
1283:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1284:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
1287:DEBUG:stick:sleeping 0.001
1300:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
1301:INFO:stick:readData validating remote raw[ack]: 02
1302:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
1303:INFO:stick:readData; raw[retries] 0
1304:INFO:stick:found packet len(64), link expects(64)
1310:INFO:stick:transmit_packet:write:<TransmitPacket:ReadRTC>
1311:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRTC> processing TransmitPacket:ReadRTC)
1312:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1313:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRTC> sending TransmitPacket:ReadRTC)
1314:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 112, 17, 0]
1318:DEBUG:stick:sleeping 0.001
1329:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1330:INFO:stick:finished processing TransmitPacket:ReadRTC, bytearray(b'\x00\xcb\x80@\xa7\x01 \x88Pm\x03515\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1333:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRTC>>:STARTING POLL PHASE:attempt:0
1334:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRTC>>:poll:attempt:0
1335:DEBUG:stick:read_status
1336:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1337:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1338:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1341:DEBUG:stick:sleeping 0.001
1352:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1353:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1355:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1356:DEBUG:stick:sleeping in POLL, .100
1357:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1358:DEBUG:stick:read_status
1359:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1360:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1361:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1364:DEBUG:stick:sleeping 0.001
1375:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1376:INFO:stick:LinkStatus:0x03:error:
1378:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1379:DEBUG:stick:sleeping in POLL, .100
1380:INFO:stick:STOP POLL after 2 attempts:size:78
1381:INFO:stick:download_packet:78
1382:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1383:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
1386:DEBUG:stick:sleeping 0.001
1399:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
1400:INFO:stick:readData validating remote raw[ack]: 02
1401:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
1402:INFO:stick:readData; raw[retries] 0
1403:INFO:stick:found packet len(64), link expects(64)
1408:INFO:stick:transmit_packet:write:<TransmitPacket:ReadPumpID>
1409:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpID> processing TransmitPacket:ReadPumpID)
1410:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1411:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpID> sending TransmitPacket:ReadPumpID)
1412:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 113, 138, 0]
1416:DEBUG:stick:sleeping 0.001
1427:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1428:INFO:stick:finished processing TransmitPacket:ReadPumpID, bytearray(b'\x00\xcb\x80@\xa7\x01 \x88Pm\t9\x1e\x07\xd6\n\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1431:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpID>>:STARTING POLL PHASE:attempt:0
1432:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadPumpID>>:poll:attempt:0
1433:DEBUG:stick:read_status
1434:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1435:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1436:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1439:DEBUG:stick:sleeping 0.001
1450:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1451:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1453:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1454:DEBUG:stick:sleeping in POLL, .100
1455:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1456:DEBUG:stick:read_status
1457:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1458:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1459:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1462:DEBUG:stick:sleeping 0.001
1473:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1474:INFO:stick:LinkStatus:0x03:error:
1476:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1477:DEBUG:stick:sleeping in POLL, .100
1478:INFO:stick:STOP POLL after 2 attempts:size:78
1479:INFO:stick:download_packet:78
1480:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1481:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
1484:DEBUG:stick:sleeping 0.001
1497:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
1498:INFO:stick:readData validating remote raw[ack]: 02
1499:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
1500:INFO:stick:readData; raw[retries] 0
1501:INFO:stick:found packet len(64), link expects(64)
1506:INFO:stick:transmit_packet:write:<TransmitPacket:ReadBatteryStatus>
1507:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBatteryStatus> processing TransmitPacket:ReadBatteryStatus)
1508:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1509:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBatteryStatus> sending TransmitPacket:ReadBatteryStatus)
1510:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 114, 188, 0]
1514:DEBUG:stick:sleeping 0.001
1525:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1526:INFO:stick:finished processing TransmitPacket:ReadBatteryStatus, bytearray(b'\x00\xcb\x80@\xa7\x01 \x88Pm208850\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1529:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBatteryStatus>>:STARTING POLL PHASE:attempt:0
1530:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBatteryStatus>>:poll:attempt:0
1531:DEBUG:stick:read_status
1532:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1533:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1534:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1537:DEBUG:stick:sleeping 0.001
1548:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1549:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1551:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1552:DEBUG:stick:sleeping in POLL, .100
1553:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1554:DEBUG:stick:read_status
1555:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1556:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1557:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1560:DEBUG:stick:sleeping 0.001
1571:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1572:INFO:stick:LinkStatus:0x03:error:
1574:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1575:DEBUG:stick:sleeping in POLL, .100
1576:INFO:stick:STOP POLL after 2 attempts:size:78
1577:INFO:stick:download_packet:78
1578:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1579:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
1582:DEBUG:stick:sleeping 0.001
1595:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
1596:INFO:stick:readData validating remote raw[ack]: 02
1597:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
1598:INFO:stick:readData; raw[retries] 0
1599:INFO:stick:found packet len(64), link expects(64)
1604:INFO:stick:transmit_packet:write:<TransmitPacket:ReadFirmwareVersion>
1605:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadFirmwareVersion> processing TransmitPacket:ReadFirmwareVersion)
1606:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1607:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadFirmwareVersion> sending TransmitPacket:ReadFirmwareVersion)
1608:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 116, 208, 0]
1612:DEBUG:stick:sleeping 0.001
1623:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1624:INFO:stick:finished processing TransmitPacket:ReadFirmwareVersion, bytearray(b'\x00\xcc\x80@\xa7\x01 \x88P\x88\x00\x00v\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1627:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadFirmwareVersion>>:STARTING POLL PHASE:attempt:0
1628:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadFirmwareVersion>>:poll:attempt:0
1629:DEBUG:stick:read_status
1630:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1631:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1632:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1635:DEBUG:stick:sleeping 0.001
1646:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1647:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1649:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1650:DEBUG:stick:sleeping in POLL, .100
1651:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1652:DEBUG:stick:read_status
1653:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1654:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1655:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1658:DEBUG:stick:sleeping 0.001
1669:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1670:INFO:stick:LinkStatus:0x03:error:
1672:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1673:DEBUG:stick:sleeping in POLL, .100
1674:INFO:stick:STOP POLL after 2 attempts:size:78
1675:INFO:stick:download_packet:78
1676:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1677:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
1680:DEBUG:stick:sleeping 0.001
1693:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
1694:INFO:stick:readData validating remote raw[ack]: 02
1695:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
1696:INFO:stick:readData; raw[retries] 0
1697:INFO:stick:found packet len(64), link expects(64)
1711:INFO:stick:transmit_packet:write:<TransmitPacket:ReadRemainingInsulin>
1712:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRemainingInsulin> processing TransmitPacket:ReadRemainingInsulin)
1713:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1714:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRemainingInsulin> sending TransmitPacket:ReadRemainingInsulin)
1715:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 115, 39, 0]
1719:DEBUG:stick:sleeping 0.001
1730:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1731:INFO:stick:finished processing TransmitPacket:ReadRemainingInsulin, bytearray(b'\x00\xcb\x80@\xa7\x01 \x88PmVER 2.1A1.1 \x0b\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1734:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRemainingInsulin>>:STARTING POLL PHASE:attempt:0
1735:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRemainingInsulin>>:poll:attempt:0
1736:DEBUG:stick:read_status
1737:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1738:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1739:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1742:DEBUG:stick:sleeping 0.001
1753:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1754:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1756:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1757:DEBUG:stick:sleeping in POLL, .100
1758:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1759:DEBUG:stick:read_status
1760:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1761:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1762:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1765:DEBUG:stick:sleeping 0.001
1776:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1777:INFO:stick:LinkStatus:0x03:error:
1779:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1780:DEBUG:stick:sleeping in POLL, .100
1781:INFO:stick:STOP POLL after 2 attempts:size:78
1782:INFO:stick:download_packet:78
1783:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1784:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
1787:DEBUG:stick:sleeping 0.001
1800:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
1801:INFO:stick:readData validating remote raw[ack]: 02
1802:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
1803:INFO:stick:readData; raw[retries] 0
1804:INFO:stick:found packet len(64), link expects(64)
1818:INFO:stick:transmit_packet:write:<TransmitPacket:ReadTotalsToday>
1819:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadTotalsToday> processing TransmitPacket:ReadTotalsToday)
1820:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1821:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadTotalsToday> sending TransmitPacket:ReadTotalsToday)
1822:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 121, 147, 0]
1826:DEBUG:stick:sleeping 0.001
1837:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1838:INFO:stick:finished processing TransmitPacket:ReadTotalsToday, bytearray(b'\x00\xcb\x80@\xa7\x01 \x88Pm\x04W\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1841:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadTotalsToday>>:STARTING POLL PHASE:attempt:0
1842:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadTotalsToday>>:poll:attempt:0
1843:DEBUG:stick:read_status
1844:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1845:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1846:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1849:DEBUG:stick:sleeping 0.001
1860:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1861:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1863:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1864:DEBUG:stick:sleeping in POLL, .100
1865:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1866:DEBUG:stick:read_status
1867:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1868:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1869:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1872:DEBUG:stick:sleeping 0.001
1883:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1884:INFO:stick:LinkStatus:0x03:error:
1886:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1887:DEBUG:stick:sleeping in POLL, .100
1888:INFO:stick:STOP POLL after 2 attempts:size:78
1889:INFO:stick:download_packet:78
1890:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1891:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
1894:DEBUG:stick:sleeping 0.001
1907:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
1908:INFO:stick:readData validating remote raw[ack]: 02
1909:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
1910:INFO:stick:readData; raw[retries] 0
1911:INFO:stick:found packet len(64), link expects(64)
1925:INFO:stick:transmit_packet:write:<TransmitPacket:ReadRadioCtrlACL>
1926:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRadioCtrlACL> processing TransmitPacket:ReadRadioCtrlACL)
1927:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1928:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRadioCtrlACL> sending TransmitPacket:ReadRadioCtrlACL)
1929:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 118, 125, 0]
1933:DEBUG:stick:sleeping 0.001
1944:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1945:INFO:stick:finished processing TransmitPacket:ReadRadioCtrlACL, bytearray(b'\x00\xcb\x80@\xa7\x01 \x88Pm\x00,\x00\xcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
1948:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRadioCtrlACL>>:STARTING POLL PHASE:attempt:0
1949:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadRadioCtrlACL>>:poll:attempt:0
1950:DEBUG:stick:read_status
1951:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1952:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1953:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1956:DEBUG:stick:sleeping 0.001
1967:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1968:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
1970:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
1971:DEBUG:stick:sleeping in POLL, .100
1972:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
1973:DEBUG:stick:read_status
1974:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
1975:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1976:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
1979:DEBUG:stick:sleeping 0.001
1990:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
1991:INFO:stick:LinkStatus:0x03:error:
1993:INFO:stick:finished processing LinkStatus:0x03:error:, 78
1994:DEBUG:stick:sleeping in POLL, .100
1995:INFO:stick:STOP POLL after 2 attempts:size:78
1996:INFO:stick:download_packet:78
1997:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
1998:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
2001:DEBUG:stick:sleeping 0.001
2014:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
2015:INFO:stick:readData validating remote raw[ack]: 02
2016:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
2017:INFO:stick:readData; raw[retries] 0
2018:INFO:stick:found packet len(64), link expects(64)
2032:INFO:stick:transmit_packet:write:<TransmitPacket:ReadBasalTemp>
2033:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBasalTemp> processing TransmitPacket:ReadBasalTemp)
2034:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2035:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBasalTemp> sending TransmitPacket:ReadBasalTemp)
2036:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 152, 175, 0]
2040:DEBUG:stick:sleeping 0.001
2051:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2052:INFO:stick:finished processing TransmitPacket:ReadBasalTemp, bytearray(b'\x00\xcc\x80@\xa7\x01 \x88P\x88123456213546821650\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
2055:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBasalTemp>>:STARTING POLL PHASE:attempt:0
2056:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadBasalTemp>>:poll:attempt:0
2057:DEBUG:stick:read_status
2058:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2059:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2060:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2063:DEBUG:stick:sleeping 0.001
2074:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2075:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
2077:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
2078:DEBUG:stick:sleeping in POLL, .100
2079:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
2080:DEBUG:stick:read_status
2081:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2082:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2083:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2086:DEBUG:stick:sleeping 0.001
2097:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2098:INFO:stick:LinkStatus:0x03:error:
2100:INFO:stick:finished processing LinkStatus:0x03:error:, 78
2101:DEBUG:stick:sleeping in POLL, .100
2102:INFO:stick:STOP POLL after 2 attempts:size:78
2103:INFO:stick:download_packet:78
2104:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2105:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
2108:DEBUG:stick:sleeping 0.001
2121:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
2122:INFO:stick:readData validating remote raw[ack]: 02
2123:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
2124:INFO:stick:readData; raw[retries] 0
2125:INFO:stick:found packet len(64), link expects(64)
2139:INFO:stick:transmit_packet:write:<TransmitPacket:ReadSettings>
2140:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadSettings> processing TransmitPacket:ReadSettings)
2141:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2142:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadSettings> sending TransmitPacket:ReadSettings)
2143:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 192, 76, 0]
2147:DEBUG:stick:sleeping 0.001
2158:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2159:INFO:stick:finished processing TransmitPacket:ReadSettings, bytearray(b'\x00\xcb\x80@\xa7\x01 \x88Pm\x00\x00\x00L\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
2162:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadSettings>>:STARTING POLL PHASE:attempt:0
2163:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadSettings>>:poll:attempt:0
2164:DEBUG:stick:read_status
2165:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2166:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2167:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2170:DEBUG:stick:sleeping 0.001
2181:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2182:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
2184:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
2185:DEBUG:stick:sleeping in POLL, .100
2186:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
2187:DEBUG:stick:read_status
2188:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2189:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2190:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2193:DEBUG:stick:sleeping 0.001
2204:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2205:INFO:stick:LinkStatus:0x03:error:
2207:INFO:stick:finished processing LinkStatus:0x03:error:, 78
2208:DEBUG:stick:sleeping in POLL, .100
2209:INFO:stick:STOP POLL after 2 attempts:size:78
2210:INFO:stick:download_packet:78
2211:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2212:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
2215:DEBUG:stick:sleeping 0.001
2228:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
2229:INFO:stick:readData validating remote raw[ack]: 02
2230:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
2231:INFO:stick:readData; raw[retries] 0
2232:INFO:stick:found packet len(64), link expects(64)
2246:INFO:stick:transmit_packet:write:<TransmitPacket:ReadContrast>
2247:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadContrast> processing TransmitPacket:ReadContrast)
2248:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2249:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadContrast> sending TransmitPacket:ReadContrast)
2250:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 195, 122, 0]
2254:DEBUG:stick:sleeping 0.001
2265:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2266:INFO:stick:finished processing TransmitPacket:ReadContrast, bytearray(b'\x00\xcc\x80@\xa7\x01 \x88P\x88\x00\x03\x01\x14\x00d\x00P\x00\x00\x01\x02\x01\x00\x00d\x00\x05\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
2269:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadContrast>>:STARTING POLL PHASE:attempt:0
2270:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadContrast>>:poll:attempt:0
2271:DEBUG:stick:read_status
2272:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2273:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2274:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2277:DEBUG:stick:sleeping 0.001
2288:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2289:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
2291:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
2292:DEBUG:stick:sleeping in POLL, .100
2293:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
2294:DEBUG:stick:read_status
2295:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2296:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2297:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2300:DEBUG:stick:sleeping 0.001
2311:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2312:INFO:stick:LinkStatus:0x03:error:
2314:INFO:stick:finished processing LinkStatus:0x03:error:, 78
2315:DEBUG:stick:sleeping in POLL, .100
2316:INFO:stick:STOP POLL after 2 attempts:size:78
2317:INFO:stick:download_packet:78
2318:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2319:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
2322:DEBUG:stick:sleeping 0.001
2335:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
2336:INFO:stick:readData validating remote raw[ack]: 02
2337:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
2338:INFO:stick:readData; raw[retries] 0
2339:INFO:stick:found packet len(64), link expects(64)
2353:INFO:stick:transmit_packet:write:<TransmitPacket:ReadCurPageNumber>
2354:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadCurPageNumber> processing TransmitPacket:ReadCurPageNumber)
2355:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2356:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadCurPageNumber> sending TransmitPacket:ReadCurPageNumber)
2357:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 157, 245, 0]
2361:DEBUG:stick:sleeping 0.001
2372:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2373:INFO:stick:finished processing TransmitPacket:ReadCurPageNumber, bytearray(b'\x00\xcc\x80@\xa7\x01 \x88P\x88\x02\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
2376:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadCurPageNumber>>:STARTING POLL PHASE:attempt:0
2377:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadCurPageNumber>>:poll:attempt:0
2378:DEBUG:stick:read_status
2379:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2380:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2381:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2384:DEBUG:stick:sleeping 0.001
2395:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2396:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
2398:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
2399:DEBUG:stick:sleeping in POLL, .100
2400:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
2401:DEBUG:stick:read_status
2402:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2403:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2404:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2407:DEBUG:stick:sleeping 0.001
2418:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2419:INFO:stick:LinkStatus:0x03:error:
2421:INFO:stick:finished processing LinkStatus:0x03:error:, 78
2422:DEBUG:stick:sleeping in POLL, .100
2423:INFO:stick:STOP POLL after 2 attempts:size:78
2424:INFO:stick:download_packet:78
2425:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2426:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
2429:DEBUG:stick:sleeping 0.001
2442:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
2443:INFO:stick:readData validating remote raw[ack]: 02
2444:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
2445:INFO:stick:readData; raw[retries] 0
2446:INFO:stick:found packet len(64), link expects(64)
2460:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][0]>
2461:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> processing TransmitPacket:ReadHistoryData[page][0])
2462:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2463:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> sending TransmitPacket:ReadHistoryData[page][0])
2464:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 1, 0, 2, 2, 0, 128, 155, 0, 0]
2469:DEBUG:stick:sleeping 0.001
2480:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2481:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xcc\x80@\xa7\x01 \x88P\x88\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
2484:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:STARTING POLL PHASE:attempt:0
2485:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:poll:attempt:0
2486:DEBUG:stick:read_status
2487:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2488:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2489:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2492:DEBUG:stick:sleeping 0.001
2503:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2504:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
2506:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
2507:DEBUG:stick:sleeping in POLL, .100
2508:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
2509:DEBUG:stick:read_status
2510:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2511:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2512:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2515:DEBUG:stick:sleeping 0.001
2526:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2527:INFO:stick:LinkStatus:0x03:error:
2529:INFO:stick:finished processing LinkStatus:0x03:error:, 78
2530:DEBUG:stick:sleeping in POLL, .100
2531:INFO:stick:STOP POLL after 2 attempts:size:78
2532:INFO:stick:download_packet:78
2533:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2534:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
2537:DEBUG:stick:sleeping 0.001
2550:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
2551:INFO:stick:readData validating remote raw[ack]: 02
2552:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
2553:INFO:stick:readData; raw[retries] 0
2554:INFO:stick:found packet len(64), link expects(64)
2555:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
2556:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
2557:DEBUG:stick:read_status
2558:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2559:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2560:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2563:DEBUG:stick:sleeping 0.001
2574:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2575:INFO:stick:LinkStatus:0x03:error:
2577:INFO:stick:finished processing LinkStatus:0x03:error:, 206
2578:DEBUG:stick:sleeping in POLL, .100
2579:INFO:stick:STOP POLL after 1 attempts:size:206
2580:INFO:stick:download_packet:206
2581:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2582:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206> sending ReadRadio:size:206)
2585:DEBUG:stick:sleeping 0.001
2614:INFO:stick:quit send_force_read, found len: 206 expected 206 after 0 attempts
2615:INFO:stick:readData validating remote raw[ack]: 02
2616:INFO:stick:readData; foreign raw should be at least 14 bytes? 206 True
2617:INFO:stick:readData; raw[retries] 0
2618:INFO:stick:found packet len(192), link expects(192)
2619:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:STARTING POLL PHASE:attempt:0
2620:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:poll:attempt:0
2621:DEBUG:stick:read_status
2622:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2623:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2624:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2627:DEBUG:stick:sleeping 0.001
2638:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2639:INFO:stick:LinkStatus:0x03:error:
2641:INFO:stick:finished processing LinkStatus:0x03:error:, 142
2642:DEBUG:stick:sleeping in POLL, .100
2643:INFO:stick:STOP POLL after 1 attempts:size:142
2644:INFO:stick:download_packet:142
2645:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2646:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
2649:DEBUG:stick:sleeping 0.001
2670:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
2671:INFO:stick:readData validating remote raw[ack]: 02
2672:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
2673:INFO:stick:readData; raw[retries] 0
2674:INFO:stick:found packet len(128), link expects(128)
2675:WARNING:stick:bad zero CRC?
2676:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
2677:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
2678:DEBUG:stick:read_status
2679:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2680:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2681:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2684:DEBUG:stick:sleeping 0.001
2695:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2696:INFO:stick:LinkStatus:0x03:error:
2698:INFO:stick:finished processing LinkStatus:0x03:error:, 142
2699:DEBUG:stick:sleeping in POLL, .100
2700:INFO:stick:STOP POLL after 1 attempts:size:142
2701:INFO:stick:download_packet:142
2702:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2703:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
2706:DEBUG:stick:sleeping 0.001
2727:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
2728:INFO:stick:readData validating remote raw[ack]: 02
2729:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
2730:INFO:stick:readData; raw[retries] 0
2731:INFO:stick:found packet len(128), link expects(128)
2732:WARNING:stick:bad zero CRC?
2733:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
2734:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
2735:DEBUG:stick:read_status
2736:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2737:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2738:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2741:DEBUG:stick:sleeping 0.001
2752:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2753:INFO:stick:LinkStatus:0x03:error:
2755:INFO:stick:finished processing LinkStatus:0x03:error:, 142
2756:DEBUG:stick:sleeping in POLL, .100
2757:INFO:stick:STOP POLL after 1 attempts:size:142
2758:INFO:stick:download_packet:142
2759:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2760:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
2763:DEBUG:stick:sleeping 0.001
2784:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
2785:INFO:stick:readData validating remote raw[ack]: 02
2786:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
2787:INFO:stick:readData; raw[retries] 0
2788:INFO:stick:found packet len(128), link expects(128)
2789:WARNING:stick:bad zero CRC?
2790:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
2791:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
2792:DEBUG:stick:read_status
2793:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2794:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2795:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2798:DEBUG:stick:sleeping 0.001
2809:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2810:INFO:stick:LinkStatus:0x03:error:
2812:INFO:stick:finished processing LinkStatus:0x03:error:, 142
2813:DEBUG:stick:sleeping in POLL, .100
2814:INFO:stick:STOP POLL after 1 attempts:size:142
2815:INFO:stick:download_packet:142
2816:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2817:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
2820:DEBUG:stick:sleeping 0.001
2841:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
2842:INFO:stick:readData validating remote raw[ack]: 02
2843:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
2844:INFO:stick:readData; raw[retries] 0
2845:INFO:stick:found packet len(128), link expects(128)
2846:WARNING:stick:bad zero CRC?
2847:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
2848:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
2849:DEBUG:stick:read_status
2850:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2851:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2852:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2855:DEBUG:stick:sleeping 0.001
2866:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2867:INFO:stick:LinkStatus:0x03:error:
2869:INFO:stick:finished processing LinkStatus:0x03:error:, 142
2870:DEBUG:stick:sleeping in POLL, .100
2871:INFO:stick:STOP POLL after 1 attempts:size:142
2872:INFO:stick:download_packet:142
2873:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2874:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
2877:DEBUG:stick:sleeping 0.001
2898:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
2899:INFO:stick:readData validating remote raw[ack]: 02
2900:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
2901:INFO:stick:readData; raw[retries] 0
2902:INFO:stick:found packet len(128), link expects(128)
2903:WARNING:stick:bad zero CRC?
2904:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
2905:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
2906:DEBUG:stick:read_status
2907:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
2908:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2909:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
2912:DEBUG:stick:sleeping 0.001
2923:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
2924:INFO:stick:LinkStatus:0x03:error:
2926:INFO:stick:finished processing LinkStatus:0x03:error:, 142
2927:DEBUG:stick:sleeping in POLL, .100
2928:INFO:stick:STOP POLL after 1 attempts:size:142
2929:INFO:stick:download_packet:142
2930:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
2931:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
2934:DEBUG:stick:sleeping 0.001
2955:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
2956:INFO:stick:readData validating remote raw[ack]: 02
2957:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
2958:INFO:stick:readData; raw[retries] 0
2959:INFO:stick:found packet len(128), link expects(128)
3218:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<UsbStats:0x05 0x01:size(64)> processing UsbStats:0x05 0x01)
3219:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3220:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<UsbStats:0x05 0x01:size(64)> sending UsbStats:0x05 0x01)
3223:DEBUG:stick:sleeping 0.001
3234:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3235:INFO:stick:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2062L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2062L, 'errors.crc': 0}
3236:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<RadioStats:0x05 0x00:size(64)> processing RadioStats:0x05 0x00)
3237:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3238:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<RadioStats:0x05 0x00:size(64)> sending RadioStats:0x05 0x00)
3241:DEBUG:stick:sleeping 0.001
3252:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3253:INFO:stick:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 983L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 933L, 'errors.crc': 0}
3254:INFO:__main__:{'radio': {'errors.crc': 0,
3255:           'errors.naks': 0,
3256:           'errors.sequence': 0,
3257:           'errors.timeouts': 3,
3258:           'packets.received': 933L,
3259:           'packets.transmit': 983L},
3260: 'usb': {'errors.crc': 0,
3261:         'errors.naks': 0,
3262:         'errors.sequence': 0,
3263:         'errors.timeouts': 0,
3264:         'packets.received': 2062L,
3265:         'packets.transmit': 2062L}}
3269:INFO:stick:transmit_packet:write:<TransmitPacket:ReadCurPageNumber>
3270:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadCurPageNumber> processing TransmitPacket:ReadCurPageNumber)
3271:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3272:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadCurPageNumber> sending TransmitPacket:ReadCurPageNumber)
3273:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 0, 0, 2, 1, 0, 157, 245, 0]
3277:DEBUG:stick:sleeping 0.001
3288:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3289:INFO:stick:finished processing TransmitPacket:ReadCurPageNumber, bytearray(b'\x00\x00\x00\x03\x00\x00\x03\xa5\x00\x00\x03\xd7\x00\x00\x00\xaf\x00?\x02\xf1\x03f\x007\x00\x00\x00\x00\x00\x00\x01\x00\xf3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
3292:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadCurPageNumber>>:STARTING POLL PHASE:attempt:0
3293:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadCurPageNumber>>:poll:attempt:0
3294:DEBUG:stick:read_status
3295:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3296:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3297:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3300:DEBUG:stick:sleeping 0.001
3311:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3312:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
3314:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
3315:DEBUG:stick:sleeping in POLL, .100
3316:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
3317:DEBUG:stick:read_status
3318:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3319:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3320:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3323:DEBUG:stick:sleeping 0.001
3334:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3335:INFO:stick:LinkStatus:0x03:error:
3337:INFO:stick:finished processing LinkStatus:0x03:error:, 78
3338:DEBUG:stick:sleeping in POLL, .100
3339:INFO:stick:STOP POLL after 2 attempts:size:78
3340:INFO:stick:download_packet:78
3341:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3342:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
3345:DEBUG:stick:sleeping 0.001
3358:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
3359:INFO:stick:readData validating remote raw[ack]: 02
3360:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
3361:INFO:stick:readData; raw[retries] 0
3362:INFO:stick:found packet len(64), link expects(64)
3376:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][0]>
3377:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> processing TransmitPacket:ReadHistoryData[page][0])
3378:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3379:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]> sending TransmitPacket:ReadHistoryData[page][0])
3380:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 1, 0, 2, 2, 0, 128, 155, 0, 0]
3385:DEBUG:stick:sleeping 0.001
3396:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3397:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][0], bytearray(b'\x00\xcc\x80@\xa7\x01 \x88P\x88\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
3400:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:STARTING POLL PHASE:attempt:0
3401:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<TransmitPacket:ReadHistoryData[page][0]>>:poll:attempt:0
3402:DEBUG:stick:read_status
3403:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3404:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3405:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3408:DEBUG:stick:sleeping 0.001
3419:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3420:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
3422:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
3423:DEBUG:stick:sleeping in POLL, .100
3424:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
3425:DEBUG:stick:read_status
3426:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3427:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3428:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3431:DEBUG:stick:sleeping 0.001
3442:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3443:INFO:stick:LinkStatus:0x03:error:
3445:INFO:stick:finished processing LinkStatus:0x03:error:, 78
3446:DEBUG:stick:sleeping in POLL, .100
3447:INFO:stick:STOP POLL after 2 attempts:size:78
3448:INFO:stick:download_packet:78
3449:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3450:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
3453:DEBUG:stick:sleeping 0.001
3466:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
3467:INFO:stick:readData validating remote raw[ack]: 02
3468:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
3469:INFO:stick:readData; raw[retries] 0
3470:INFO:stick:found packet len(64), link expects(64)
3471:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
3472:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
3473:DEBUG:stick:read_status
3474:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3475:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3476:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3479:DEBUG:stick:sleeping 0.001
3490:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3491:INFO:stick:LinkStatus:0x03:error:
3493:INFO:stick:finished processing LinkStatus:0x03:error:, 206
3494:DEBUG:stick:sleeping in POLL, .100
3495:INFO:stick:STOP POLL after 1 attempts:size:206
3496:INFO:stick:download_packet:206
3497:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3498:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206> sending ReadRadio:size:206)
3501:DEBUG:stick:sleeping 0.001
3530:INFO:stick:quit send_force_read, found len: 206 expected 206 after 0 attempts
3531:INFO:stick:readData validating remote raw[ack]: 02
3532:INFO:stick:readData; foreign raw should be at least 14 bytes? 206 True
3533:INFO:stick:readData; raw[retries] 0
3534:INFO:stick:found packet len(192), link expects(192)
3535:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:STARTING POLL PHASE:attempt:0
3536:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:poll:attempt:0
3537:DEBUG:stick:read_status
3538:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3539:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3540:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3543:DEBUG:stick:sleeping 0.001
3554:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3555:INFO:stick:LinkStatus:0x03:error:
3557:INFO:stick:finished processing LinkStatus:0x03:error:, 142
3558:DEBUG:stick:sleeping in POLL, .100
3559:INFO:stick:STOP POLL after 1 attempts:size:142
3560:INFO:stick:download_packet:142
3561:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3562:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
3565:DEBUG:stick:sleeping 0.001
3586:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
3587:INFO:stick:readData validating remote raw[ack]: 02
3588:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
3589:INFO:stick:readData; raw[retries] 0
3590:INFO:stick:found packet len(128), link expects(128)
3591:WARNING:stick:bad zero CRC?
3592:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
3593:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
3594:DEBUG:stick:read_status
3595:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3596:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3597:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3600:DEBUG:stick:sleeping 0.001
3611:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3612:INFO:stick:LinkStatus:0x03:error:
3614:INFO:stick:finished processing LinkStatus:0x03:error:, 142
3615:DEBUG:stick:sleeping in POLL, .100
3616:INFO:stick:STOP POLL after 1 attempts:size:142
3617:INFO:stick:download_packet:142
3618:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3619:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
3622:DEBUG:stick:sleeping 0.001
3643:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
3644:INFO:stick:readData validating remote raw[ack]: 02
3645:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
3646:INFO:stick:readData; raw[retries] 0
3647:INFO:stick:found packet len(128), link expects(128)
3648:WARNING:stick:bad zero CRC?
3649:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
3650:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
3651:DEBUG:stick:read_status
3652:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3653:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3654:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3657:DEBUG:stick:sleeping 0.001
3668:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3669:INFO:stick:LinkStatus:0x03:error:
3671:INFO:stick:finished processing LinkStatus:0x03:error:, 142
3672:DEBUG:stick:sleeping in POLL, .100
3673:INFO:stick:STOP POLL after 1 attempts:size:142
3674:INFO:stick:download_packet:142
3675:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3676:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
3679:DEBUG:stick:sleeping 0.001
3700:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
3701:INFO:stick:readData validating remote raw[ack]: 02
3702:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
3703:INFO:stick:readData; raw[retries] 0
3704:INFO:stick:found packet len(128), link expects(128)
3705:WARNING:stick:bad zero CRC?
3706:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
3707:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
3708:DEBUG:stick:read_status
3709:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3710:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3711:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3714:DEBUG:stick:sleeping 0.001
3725:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3726:INFO:stick:LinkStatus:0x03:error:
3728:INFO:stick:finished processing LinkStatus:0x03:error:, 142
3729:DEBUG:stick:sleeping in POLL, .100
3730:INFO:stick:STOP POLL after 1 attempts:size:142
3731:INFO:stick:download_packet:142
3732:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3733:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
3736:DEBUG:stick:sleeping 0.001
3757:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
3758:INFO:stick:readData validating remote raw[ack]: 02
3759:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
3760:INFO:stick:readData; raw[retries] 0
3761:INFO:stick:found packet len(128), link expects(128)
3762:WARNING:stick:bad zero CRC?
3763:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
3764:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
3765:DEBUG:stick:read_status
3766:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3767:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3768:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3771:DEBUG:stick:sleeping 0.001
3782:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3783:INFO:stick:LinkStatus:0x03:error:
3785:INFO:stick:finished processing LinkStatus:0x03:error:, 142
3786:DEBUG:stick:sleeping in POLL, .100
3787:INFO:stick:STOP POLL after 1 attempts:size:142
3788:INFO:stick:download_packet:142
3789:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3790:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
3793:DEBUG:stick:sleeping 0.001
3814:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
3815:INFO:stick:readData validating remote raw[ack]: 02
3816:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
3817:INFO:stick:readData; raw[retries] 0
3818:INFO:stick:found packet len(128), link expects(128)
3819:WARNING:stick:bad zero CRC?
3820:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
3821:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
3822:DEBUG:stick:read_status
3823:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
3824:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3825:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
3828:DEBUG:stick:sleeping 0.001
3839:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
3840:INFO:stick:LinkStatus:0x03:error:
3842:INFO:stick:finished processing LinkStatus:0x03:error:, 142
3843:DEBUG:stick:sleeping in POLL, .100
3844:INFO:stick:STOP POLL after 1 attempts:size:142
3845:INFO:stick:download_packet:142
3846:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
3847:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
3850:DEBUG:stick:sleeping 0.001
3871:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
3872:INFO:stick:readData validating remote raw[ack]: 02
3873:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
3874:INFO:stick:readData; raw[retries] 0
3875:INFO:stick:found packet len(128), link expects(128)
4137:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][1]>
4138:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]> processing TransmitPacket:ReadHistoryData[page][1])
4139:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4140:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]> sending TransmitPacket:ReadHistoryData[page][1])
4141:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 1, 0, 2, 2, 0, 128, 155, 1, 155]
4146:DEBUG:stick:sleeping 0.001
4157:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4158:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][1], bytearray(b'\x00\xcc\x80\x80\xa7\x01 \x88P\xcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
4161:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]>>:STARTING POLL PHASE:attempt:0
4162:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][1]>>:poll:attempt:0
4163:DEBUG:stick:read_status
4164:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4165:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4166:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4169:DEBUG:stick:sleeping 0.001
4180:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4181:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
4183:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
4184:DEBUG:stick:sleeping in POLL, .100
4185:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
4186:DEBUG:stick:read_status
4187:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4188:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4189:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4192:DEBUG:stick:sleeping 0.001
4203:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4204:INFO:stick:LinkStatus:0x03:error:
4206:INFO:stick:finished processing LinkStatus:0x03:error:, 78
4207:DEBUG:stick:sleeping in POLL, .100
4208:INFO:stick:STOP POLL after 2 attempts:size:78
4209:INFO:stick:download_packet:78
4210:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4211:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
4214:DEBUG:stick:sleeping 0.001
4227:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
4228:INFO:stick:readData validating remote raw[ack]: 02
4229:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
4230:INFO:stick:readData; raw[retries] 0
4231:INFO:stick:found packet len(64), link expects(64)
4232:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
4233:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
4234:DEBUG:stick:read_status
4235:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4236:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4237:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4240:DEBUG:stick:sleeping 0.001
4251:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4252:INFO:stick:LinkStatus:0x03:error:
4254:INFO:stick:finished processing LinkStatus:0x03:error:, 206
4255:DEBUG:stick:sleeping in POLL, .100
4256:INFO:stick:STOP POLL after 1 attempts:size:206
4257:INFO:stick:download_packet:206
4258:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4259:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206> sending ReadRadio:size:206)
4262:DEBUG:stick:sleeping 0.001
4291:INFO:stick:quit send_force_read, found len: 206 expected 206 after 0 attempts
4292:INFO:stick:readData validating remote raw[ack]: 02
4293:INFO:stick:readData; foreign raw should be at least 14 bytes? 206 True
4294:INFO:stick:readData; raw[retries] 0
4295:INFO:stick:found packet len(192), link expects(192)
4296:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:STARTING POLL PHASE:attempt:0
4297:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:poll:attempt:0
4298:DEBUG:stick:read_status
4299:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4300:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4301:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4304:DEBUG:stick:sleeping 0.001
4315:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4316:INFO:stick:LinkStatus:0x03:error:
4318:INFO:stick:finished processing LinkStatus:0x03:error:, 142
4319:DEBUG:stick:sleeping in POLL, .100
4320:INFO:stick:STOP POLL after 1 attempts:size:142
4321:INFO:stick:download_packet:142
4322:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4323:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
4326:DEBUG:stick:sleeping 0.001
4347:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
4348:INFO:stick:readData validating remote raw[ack]: 02
4349:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
4350:INFO:stick:readData; raw[retries] 0
4351:INFO:stick:found packet len(128), link expects(128)
4352:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
4353:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
4354:DEBUG:stick:read_status
4355:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4356:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4357:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4360:DEBUG:stick:sleeping 0.001
4371:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4372:INFO:stick:LinkStatus:0x03:error:
4374:INFO:stick:finished processing LinkStatus:0x03:error:, 142
4375:DEBUG:stick:sleeping in POLL, .100
4376:INFO:stick:STOP POLL after 1 attempts:size:142
4377:INFO:stick:download_packet:142
4378:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4379:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
4382:DEBUG:stick:sleeping 0.001
4403:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
4404:INFO:stick:readData validating remote raw[ack]: 02
4405:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
4406:INFO:stick:readData; raw[retries] 0
4407:INFO:stick:found packet len(128), link expects(128)
4408:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
4409:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
4410:DEBUG:stick:read_status
4411:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4412:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4413:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4416:DEBUG:stick:sleeping 0.001
4427:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4428:INFO:stick:LinkStatus:0x03:error:
4430:INFO:stick:finished processing LinkStatus:0x03:error:, 142
4431:DEBUG:stick:sleeping in POLL, .100
4432:INFO:stick:STOP POLL after 1 attempts:size:142
4433:INFO:stick:download_packet:142
4434:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4435:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
4438:DEBUG:stick:sleeping 0.001
4459:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
4460:INFO:stick:readData validating remote raw[ack]: 02
4461:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
4462:INFO:stick:readData; raw[retries] 0
4463:INFO:stick:found packet len(128), link expects(128)
4464:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
4465:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
4466:DEBUG:stick:read_status
4467:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4468:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4469:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4472:DEBUG:stick:sleeping 0.001
4483:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4484:INFO:stick:LinkStatus:0x03:error:
4486:INFO:stick:finished processing LinkStatus:0x03:error:, 142
4487:DEBUG:stick:sleeping in POLL, .100
4488:INFO:stick:STOP POLL after 1 attempts:size:142
4489:INFO:stick:download_packet:142
4490:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4491:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
4494:DEBUG:stick:sleeping 0.001
4515:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
4516:INFO:stick:readData validating remote raw[ack]: 02
4517:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
4518:INFO:stick:readData; raw[retries] 0
4519:INFO:stick:found packet len(128), link expects(128)
4520:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
4521:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
4522:DEBUG:stick:read_status
4523:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4524:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4525:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4528:DEBUG:stick:sleeping 0.001
4539:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4540:INFO:stick:LinkStatus:0x03:error:
4542:INFO:stick:finished processing LinkStatus:0x03:error:, 142
4543:DEBUG:stick:sleeping in POLL, .100
4544:INFO:stick:STOP POLL after 1 attempts:size:142
4545:INFO:stick:download_packet:142
4546:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4547:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
4550:DEBUG:stick:sleeping 0.001
4571:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
4572:INFO:stick:readData validating remote raw[ack]: 02
4573:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
4574:INFO:stick:readData; raw[retries] 0
4575:INFO:stick:found packet len(128), link expects(128)
4576:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
4577:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
4578:DEBUG:stick:read_status
4579:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4580:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4581:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4584:DEBUG:stick:sleeping 0.001
4595:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4596:INFO:stick:LinkStatus:0x03:error:
4598:INFO:stick:finished processing LinkStatus:0x03:error:, 142
4599:DEBUG:stick:sleeping in POLL, .100
4600:INFO:stick:STOP POLL after 1 attempts:size:142
4601:INFO:stick:download_packet:142
4602:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4603:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
4606:DEBUG:stick:sleeping 0.001
4627:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
4628:INFO:stick:readData validating remote raw[ack]: 02
4629:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
4630:INFO:stick:readData; raw[retries] 0
4631:INFO:stick:found packet len(128), link expects(128)
4893:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][2]>
4894:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]> processing TransmitPacket:ReadHistoryData[page][2])
4895:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4896:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]> sending TransmitPacket:ReadHistoryData[page][2])
4897:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 1, 0, 2, 2, 0, 128, 155, 2, 173]
4902:DEBUG:stick:sleeping 0.001
4913:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4914:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][2], bytearray(b'\x00\xcc\x80\x80\xa7\x01 \x88P\xcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x03\x92\x9e\x0b\x01\x06\x07\x00\x00\x02L\xa1\x06l\xa1\x06\x05\x0c\x00\xe8\x00\x00\x00\x00\x02L\x02Ld\x00\x00\x00\x00\x00\x00\x00\x00\x00')
4917:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]>>:STARTING POLL PHASE:attempt:0
4918:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][2]>>:poll:attempt:0
4919:DEBUG:stick:read_status
4920:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4921:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4922:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4925:DEBUG:stick:sleeping 0.001
4936:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4937:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
4939:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
4940:DEBUG:stick:sleeping in POLL, .100
4941:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
4942:DEBUG:stick:read_status
4943:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4944:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4945:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4948:DEBUG:stick:sleeping 0.001
4959:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
4960:INFO:stick:LinkStatus:0x03:error:
4962:INFO:stick:finished processing LinkStatus:0x03:error:, 78
4963:DEBUG:stick:sleeping in POLL, .100
4964:INFO:stick:STOP POLL after 2 attempts:size:78
4965:INFO:stick:download_packet:78
4966:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4967:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
4970:DEBUG:stick:sleeping 0.001
4983:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
4984:INFO:stick:readData validating remote raw[ack]: 02
4985:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
4986:INFO:stick:readData; raw[retries] 0
4987:INFO:stick:found packet len(64), link expects(64)
4988:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
4989:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
4990:DEBUG:stick:read_status
4991:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
4992:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
4993:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
4996:DEBUG:stick:sleeping 0.001
5007:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5008:INFO:stick:LinkStatus:0x03:error:
5010:INFO:stick:finished processing LinkStatus:0x03:error:, 206
5011:DEBUG:stick:sleeping in POLL, .100
5012:INFO:stick:STOP POLL after 1 attempts:size:206
5013:INFO:stick:download_packet:206
5014:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5015:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206> sending ReadRadio:size:206)
5018:DEBUG:stick:sleeping 0.001
5047:INFO:stick:quit send_force_read, found len: 206 expected 206 after 0 attempts
5048:INFO:stick:readData validating remote raw[ack]: 02
5049:INFO:stick:readData; foreign raw should be at least 14 bytes? 206 True
5050:INFO:stick:readData; raw[retries] 0
5051:INFO:stick:found packet len(192), link expects(192)
5052:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:STARTING POLL PHASE:attempt:0
5053:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:poll:attempt:0
5054:DEBUG:stick:read_status
5055:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5056:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5057:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5060:DEBUG:stick:sleeping 0.001
5071:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5072:INFO:stick:LinkStatus:0x03:error:
5074:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5075:DEBUG:stick:sleeping in POLL, .100
5076:INFO:stick:STOP POLL after 1 attempts:size:142
5077:INFO:stick:download_packet:142
5078:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5079:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5082:DEBUG:stick:sleeping 0.001
5103:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5104:INFO:stick:readData validating remote raw[ack]: 02
5105:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5106:INFO:stick:readData; raw[retries] 0
5107:INFO:stick:found packet len(128), link expects(128)
5108:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
5109:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
5110:DEBUG:stick:read_status
5111:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5112:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5113:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5116:DEBUG:stick:sleeping 0.001
5127:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5128:INFO:stick:LinkStatus:0x03:error:
5130:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5131:DEBUG:stick:sleeping in POLL, .100
5132:INFO:stick:STOP POLL after 1 attempts:size:142
5133:INFO:stick:download_packet:142
5134:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5135:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5138:DEBUG:stick:sleeping 0.001
5159:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5160:INFO:stick:readData validating remote raw[ack]: 02
5161:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5162:INFO:stick:readData; raw[retries] 0
5163:INFO:stick:found packet len(128), link expects(128)
5164:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
5165:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
5166:DEBUG:stick:read_status
5167:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5168:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5169:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5172:DEBUG:stick:sleeping 0.001
5183:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5184:INFO:stick:LinkStatus:0x03:error:
5186:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5187:DEBUG:stick:sleeping in POLL, .100
5188:INFO:stick:STOP POLL after 1 attempts:size:142
5189:INFO:stick:download_packet:142
5190:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5191:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5194:DEBUG:stick:sleeping 0.001
5215:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5216:INFO:stick:readData validating remote raw[ack]: 02
5217:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5218:INFO:stick:readData; raw[retries] 0
5219:INFO:stick:found packet len(128), link expects(128)
5220:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
5221:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
5222:DEBUG:stick:read_status
5223:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5224:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5225:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5228:DEBUG:stick:sleeping 0.001
5239:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5240:INFO:stick:LinkStatus:0x03:error:
5242:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5243:DEBUG:stick:sleeping in POLL, .100
5244:INFO:stick:STOP POLL after 1 attempts:size:142
5245:INFO:stick:download_packet:142
5246:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5247:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5250:DEBUG:stick:sleeping 0.001
5271:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5272:INFO:stick:readData validating remote raw[ack]: 02
5273:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5274:INFO:stick:readData; raw[retries] 0
5275:INFO:stick:found packet len(128), link expects(128)
5276:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
5277:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
5278:DEBUG:stick:read_status
5279:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5280:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5281:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5284:DEBUG:stick:sleeping 0.001
5295:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5296:INFO:stick:LinkStatus:0x03:error:
5298:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5299:DEBUG:stick:sleeping in POLL, .100
5300:INFO:stick:STOP POLL after 1 attempts:size:142
5301:INFO:stick:download_packet:142
5302:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5303:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5306:DEBUG:stick:sleeping 0.001
5327:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5328:INFO:stick:readData validating remote raw[ack]: 02
5329:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5330:INFO:stick:readData; raw[retries] 0
5331:INFO:stick:found packet len(128), link expects(128)
5332:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
5333:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
5334:DEBUG:stick:read_status
5335:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5336:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5337:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5340:DEBUG:stick:sleeping 0.001
5351:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5352:INFO:stick:LinkStatus:0x03:error:
5354:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5355:DEBUG:stick:sleeping in POLL, .100
5356:INFO:stick:STOP POLL after 1 attempts:size:142
5357:INFO:stick:download_packet:142
5358:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5359:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5362:DEBUG:stick:sleeping 0.001
5383:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5384:INFO:stick:readData validating remote raw[ack]: 02
5385:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5386:INFO:stick:readData; raw[retries] 0
5387:INFO:stick:found packet len(128), link expects(128)
5649:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][3]>
5650:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]> processing TransmitPacket:ReadHistoryData[page][3])
5651:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5652:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]> sending TransmitPacket:ReadHistoryData[page][3])
5653:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 1, 0, 2, 2, 0, 128, 155, 3, 54]
5658:DEBUG:stick:sleeping 0.001
5669:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5670:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][3], bytearray(b'\x00\xcc\x80\x80\xa7\x01 \x88P\xcd\x04\xda\x82\x0cl\x82\x0c\x05\x00edf\x12\x00\x00\x04\xda\x03\x9eK\x01<\x19\x00O\x01<\x19\x01<d\x00\x00\x00\x00\x00\x00\x10\x10\x00\x00\x00d\x01V\xca\x06\x01\x06\x17\x00')
5673:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]>>:STARTING POLL PHASE:attempt:0
5674:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][3]>>:poll:attempt:0
5675:DEBUG:stick:read_status
5676:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5677:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5678:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5681:DEBUG:stick:sleeping 0.001
5692:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5693:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
5695:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
5696:DEBUG:stick:sleeping in POLL, .100
5697:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
5698:DEBUG:stick:read_status
5699:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5700:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5701:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5704:DEBUG:stick:sleeping 0.001
5715:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5716:INFO:stick:LinkStatus:0x03:error:
5718:INFO:stick:finished processing LinkStatus:0x03:error:, 78
5719:DEBUG:stick:sleeping in POLL, .100
5720:INFO:stick:STOP POLL after 2 attempts:size:78
5721:INFO:stick:download_packet:78
5722:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5723:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
5726:DEBUG:stick:sleeping 0.001
5739:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
5740:INFO:stick:readData validating remote raw[ack]: 02
5741:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
5742:INFO:stick:readData; raw[retries] 0
5743:INFO:stick:found packet len(64), link expects(64)
5744:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
5745:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
5746:DEBUG:stick:read_status
5747:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5748:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5749:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5752:DEBUG:stick:sleeping 0.001
5763:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5764:INFO:stick:LinkStatus:0x03:error:
5766:INFO:stick:finished processing LinkStatus:0x03:error:, 206
5767:DEBUG:stick:sleeping in POLL, .100
5768:INFO:stick:STOP POLL after 1 attempts:size:206
5769:INFO:stick:download_packet:206
5770:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5771:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206> sending ReadRadio:size:206)
5774:DEBUG:stick:sleeping 0.001
5803:INFO:stick:quit send_force_read, found len: 206 expected 206 after 0 attempts
5804:INFO:stick:readData validating remote raw[ack]: 02
5805:INFO:stick:readData; foreign raw should be at least 14 bytes? 206 True
5806:INFO:stick:readData; raw[retries] 0
5807:INFO:stick:found packet len(192), link expects(192)
5808:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:STARTING POLL PHASE:attempt:0
5809:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:poll:attempt:0
5810:DEBUG:stick:read_status
5811:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5812:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5813:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5816:DEBUG:stick:sleeping 0.001
5827:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5828:INFO:stick:LinkStatus:0x03:error:
5830:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5831:DEBUG:stick:sleeping in POLL, .100
5832:INFO:stick:STOP POLL after 1 attempts:size:142
5833:INFO:stick:download_packet:142
5834:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5835:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5838:DEBUG:stick:sleeping 0.001
5859:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5860:INFO:stick:readData validating remote raw[ack]: 02
5861:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5862:INFO:stick:readData; raw[retries] 0
5863:INFO:stick:found packet len(128), link expects(128)
5864:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
5865:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
5866:DEBUG:stick:read_status
5867:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5868:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5869:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5872:DEBUG:stick:sleeping 0.001
5883:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5884:INFO:stick:LinkStatus:0x03:error:
5886:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5887:DEBUG:stick:sleeping in POLL, .100
5888:INFO:stick:STOP POLL after 1 attempts:size:142
5889:INFO:stick:download_packet:142
5890:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5891:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5894:DEBUG:stick:sleeping 0.001
5915:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5916:INFO:stick:readData validating remote raw[ack]: 02
5917:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5918:INFO:stick:readData; raw[retries] 0
5919:INFO:stick:found packet len(128), link expects(128)
5920:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
5921:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
5922:DEBUG:stick:read_status
5923:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5924:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5925:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5928:DEBUG:stick:sleeping 0.001
5939:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5940:INFO:stick:LinkStatus:0x03:error:
5942:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5943:DEBUG:stick:sleeping in POLL, .100
5944:INFO:stick:STOP POLL after 1 attempts:size:142
5945:INFO:stick:download_packet:142
5946:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5947:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
5950:DEBUG:stick:sleeping 0.001
5971:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
5972:INFO:stick:readData validating remote raw[ack]: 02
5973:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
5974:INFO:stick:readData; raw[retries] 0
5975:INFO:stick:found packet len(128), link expects(128)
5976:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
5977:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
5978:DEBUG:stick:read_status
5979:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
5980:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
5981:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
5984:DEBUG:stick:sleeping 0.001
5995:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
5996:INFO:stick:LinkStatus:0x03:error:
5998:INFO:stick:finished processing LinkStatus:0x03:error:, 142
5999:DEBUG:stick:sleeping in POLL, .100
6000:INFO:stick:STOP POLL after 1 attempts:size:142
6001:INFO:stick:download_packet:142
6002:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6003:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6006:DEBUG:stick:sleeping 0.001
6027:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6028:INFO:stick:readData validating remote raw[ack]: 02
6029:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6030:INFO:stick:readData; raw[retries] 0
6031:INFO:stick:found packet len(128), link expects(128)
6032:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
6033:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
6034:DEBUG:stick:read_status
6035:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6036:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6037:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6040:DEBUG:stick:sleeping 0.001
6051:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6052:INFO:stick:LinkStatus:0x03:error:
6054:INFO:stick:finished processing LinkStatus:0x03:error:, 142
6055:DEBUG:stick:sleeping in POLL, .100
6056:INFO:stick:STOP POLL after 1 attempts:size:142
6057:INFO:stick:download_packet:142
6058:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6059:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6062:DEBUG:stick:sleeping 0.001
6083:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6084:INFO:stick:readData validating remote raw[ack]: 02
6085:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6086:INFO:stick:readData; raw[retries] 0
6087:INFO:stick:found packet len(128), link expects(128)
6088:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
6089:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
6090:DEBUG:stick:read_status
6091:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6092:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6093:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6096:DEBUG:stick:sleeping 0.001
6107:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6108:INFO:stick:LinkStatus:0x03:error:
6110:INFO:stick:finished processing LinkStatus:0x03:error:, 142
6111:DEBUG:stick:sleeping in POLL, .100
6112:INFO:stick:STOP POLL after 1 attempts:size:142
6113:INFO:stick:download_packet:142
6114:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6115:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6118:DEBUG:stick:sleeping 0.001
6139:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6140:INFO:stick:readData validating remote raw[ack]: 02
6141:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6142:INFO:stick:readData; raw[retries] 0
6143:INFO:stick:found packet len(128), link expects(128)
6405:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][4]>
6406:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][4]> processing TransmitPacket:ReadHistoryData[page][4])
6407:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6408:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][4]> sending TransmitPacket:ReadHistoryData[page][4])
6409:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 1, 0, 2, 2, 0, 128, 155, 4, 193]
6414:DEBUG:stick:sleeping 0.001
6425:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6426:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][4], bytearray(b'\x00\xcc\x80\x80\xa7\x01 \x88P\xcd\x01\x12\x17\x00\x9f\x08\x14\x01\x12\x18\x00\x80\x08\x14\x01\x0c\x07\x00\x00\x00\x06\x81\x12l\x81\x12\x05\x0c\x00\xe8\x00\x00\x00\x00\x00\x06\x00\x06d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
6429:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][4]>>:STARTING POLL PHASE:attempt:0
6430:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][4]>>:poll:attempt:0
6431:DEBUG:stick:read_status
6432:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6433:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6434:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6437:DEBUG:stick:sleeping 0.001
6448:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6449:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
6451:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
6452:DEBUG:stick:sleeping in POLL, .100
6453:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
6454:DEBUG:stick:read_status
6455:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6456:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6457:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6460:DEBUG:stick:sleeping 0.001
6471:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6472:INFO:stick:LinkStatus:0x03:error:
6474:INFO:stick:finished processing LinkStatus:0x03:error:, 78
6475:DEBUG:stick:sleeping in POLL, .100
6476:INFO:stick:STOP POLL after 2 attempts:size:78
6477:INFO:stick:download_packet:78
6478:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6479:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
6482:DEBUG:stick:sleeping 0.001
6495:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
6496:INFO:stick:readData validating remote raw[ack]: 02
6497:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
6498:INFO:stick:readData; raw[retries] 0
6499:INFO:stick:found packet len(64), link expects(64)
6500:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
6501:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
6502:DEBUG:stick:read_status
6503:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6504:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6505:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6508:DEBUG:stick:sleeping 0.001
6519:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6520:INFO:stick:LinkStatus:0x03:error:
6522:INFO:stick:finished processing LinkStatus:0x03:error:, 206
6523:DEBUG:stick:sleeping in POLL, .100
6524:INFO:stick:STOP POLL after 1 attempts:size:206
6525:INFO:stick:download_packet:206
6526:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6527:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206> sending ReadRadio:size:206)
6530:DEBUG:stick:sleeping 0.001
6559:INFO:stick:quit send_force_read, found len: 206 expected 206 after 0 attempts
6560:INFO:stick:readData validating remote raw[ack]: 02
6561:INFO:stick:readData; foreign raw should be at least 14 bytes? 206 True
6562:INFO:stick:readData; raw[retries] 0
6563:INFO:stick:found packet len(192), link expects(192)
6564:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:STARTING POLL PHASE:attempt:0
6565:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206>>:poll:attempt:0
6566:DEBUG:stick:read_status
6567:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6568:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6569:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6572:DEBUG:stick:sleeping 0.001
6583:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6584:INFO:stick:LinkStatus:0x03:error:
6586:INFO:stick:finished processing LinkStatus:0x03:error:, 142
6587:DEBUG:stick:sleeping in POLL, .100
6588:INFO:stick:STOP POLL after 1 attempts:size:142
6589:INFO:stick:download_packet:142
6590:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6591:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6594:DEBUG:stick:sleeping 0.001
6615:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6616:INFO:stick:readData validating remote raw[ack]: 02
6617:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6618:INFO:stick:readData; raw[retries] 0
6619:INFO:stick:found packet len(128), link expects(128)
6620:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
6621:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
6622:DEBUG:stick:read_status
6623:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6624:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6625:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6628:DEBUG:stick:sleeping 0.001
6639:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6640:INFO:stick:LinkStatus:0x03:error:
6642:INFO:stick:finished processing LinkStatus:0x03:error:, 142
6643:DEBUG:stick:sleeping in POLL, .100
6644:INFO:stick:STOP POLL after 1 attempts:size:142
6645:INFO:stick:download_packet:142
6646:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6647:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6650:DEBUG:stick:sleeping 0.001
6671:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6672:INFO:stick:readData validating remote raw[ack]: 02
6673:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6674:INFO:stick:readData; raw[retries] 0
6675:INFO:stick:found packet len(128), link expects(128)
6676:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
6677:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
6678:DEBUG:stick:read_status
6679:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6680:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6681:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6684:DEBUG:stick:sleeping 0.001
6695:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6696:INFO:stick:LinkStatus:0x03:error:
6698:INFO:stick:finished processing LinkStatus:0x03:error:, 142
6699:DEBUG:stick:sleeping in POLL, .100
6700:INFO:stick:STOP POLL after 1 attempts:size:142
6701:INFO:stick:download_packet:142
6702:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6703:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6706:DEBUG:stick:sleeping 0.001
6727:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6728:INFO:stick:readData validating remote raw[ack]: 02
6729:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6730:INFO:stick:readData; raw[retries] 0
6731:INFO:stick:found packet len(128), link expects(128)
6732:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
6733:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
6734:DEBUG:stick:read_status
6735:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6736:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6737:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6740:DEBUG:stick:sleeping 0.001
6751:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6752:INFO:stick:LinkStatus:0x03:error:
6754:INFO:stick:finished processing LinkStatus:0x03:error:, 142
6755:DEBUG:stick:sleeping in POLL, .100
6756:INFO:stick:STOP POLL after 1 attempts:size:142
6757:INFO:stick:download_packet:142
6758:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6759:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6762:DEBUG:stick:sleeping 0.001
6783:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6784:INFO:stick:readData validating remote raw[ack]: 02
6785:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6786:INFO:stick:readData; raw[retries] 0
6787:INFO:stick:found packet len(128), link expects(128)
6788:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
6789:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
6790:DEBUG:stick:read_status
6791:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6792:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6793:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6796:DEBUG:stick:sleeping 0.001
6807:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6808:INFO:stick:LinkStatus:0x03:error:
6810:INFO:stick:finished processing LinkStatus:0x03:error:, 142
6811:DEBUG:stick:sleeping in POLL, .100
6812:INFO:stick:STOP POLL after 1 attempts:size:142
6813:INFO:stick:download_packet:142
6814:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6815:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6818:DEBUG:stick:sleeping 0.001
6839:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6840:INFO:stick:readData validating remote raw[ack]: 02
6841:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6842:INFO:stick:readData; raw[retries] 0
6843:INFO:stick:found packet len(128), link expects(128)
6844:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:STARTING POLL PHASE:attempt:0
6845:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142>>:poll:attempt:0
6846:DEBUG:stick:read_status
6847:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
6848:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6849:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
6852:DEBUG:stick:sleeping 0.001
6863:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
6864:INFO:stick:LinkStatus:0x03:error:
6866:INFO:stick:finished processing LinkStatus:0x03:error:, 142
6867:DEBUG:stick:sleeping in POLL, .100
6868:INFO:stick:STOP POLL after 1 attempts:size:142
6869:INFO:stick:download_packet:142
6870:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
6871:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<ReadRadio:size:142> sending ReadRadio:size:142)
6874:DEBUG:stick:sleeping 0.001
6895:INFO:stick:quit send_force_read, found len: 142 expected 142 after 0 attempts
6896:INFO:stick:readData validating remote raw[ack]: 02
6897:INFO:stick:readData; foreign raw should be at least 14 bytes? 142 True
6898:INFO:stick:readData; raw[retries] 0
6899:INFO:stick:found packet len(128), link expects(128)
```

## Failure is eminent

```
7161:INFO:stick:transmit_packet:write:<TransmitPacket:ReadHistoryData[page][5]>
7162:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]> processing TransmitPacket:ReadHistoryData[page][5])
7163:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
7164:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]> sending TransmitPacket:ReadHistoryData[page][5])
7165:DEBUG:stick:[1, 0, 167, 1, 32, 136, 80, 128, 1, 0, 2, 2, 0, 128, 155, 5, 90]
7170:DEBUG:stick:sleeping 0.001
7181:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
7182:INFO:stick:finished processing TransmitPacket:ReadHistoryData[page][5], bytearray(b'\x00\xcc\x80\x80\xa7\x01 \x88P\xcd\x00\x02\x00!\x00l!\x00\x05\x0c\x00\xe8\x00\x00\x00\x00\x02\x00\x02\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x0c\x9c\x13\x02\x00\x17')
7185:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]>>:STARTING POLL PHASE:attempt:0
7186:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(142)>:command:<TransmitPacket:ReadHistoryData[page][5]>>:poll:attempt:0
7187:DEBUG:stick:read_status
7188:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
7189:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
7190:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(142)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
7193:DEBUG:stick:sleeping 0.001
7204:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
7205:INFO:stick:LinkStatus:0x03:error:LinkStatus:error:True:reason:
7207:INFO:stick:finished processing LinkStatus:0x03:error:LinkStatus:error:True:reason:, 0
7208:DEBUG:stick:sleeping in POLL, .100
7209:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>>:poll:attempt:1
7210:DEBUG:stick:read_status
7211:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
7212:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
7213:INFO:stick:link Stick:status:<LinkStatus:0x03:error:LinkStatus:error:True:reason::size(0)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
7216:DEBUG:stick:sleeping 0.001
7227:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
7228:INFO:stick:LinkStatus:0x03:error:
7230:INFO:stick:finished processing LinkStatus:0x03:error:, 78
7231:DEBUG:stick:sleeping in POLL, .100
7232:INFO:stick:STOP POLL after 2 attempts:size:78
7233:INFO:stick:download_packet:78
7234:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
7235:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78> sending ReadRadio:size:78)
7238:DEBUG:stick:sleeping 0.001
7251:INFO:stick:quit send_force_read, found len: 78 expected 78 after 0 attempts
7252:INFO:stick:readData validating remote raw[ack]: 02
7253:INFO:stick:readData; foreign raw should be at least 14 bytes? 78 True
7254:INFO:stick:readData; raw[retries] 0
7255:INFO:stick:found packet len(64), link expects(64)
7256:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:STARTING POLL PHASE:attempt:0
7257:DEBUG:stick:<Stick:status:<LinkStatus:0x03:error::size(78)>:command:<ReadRadio:size:78>>:poll:attempt:0
7258:DEBUG:stick:read_status
7259:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> processing LinkStatus:0x03:error:)
7260:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
7261:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(78)>:command:<LinkStatus:0x03:error::size(64)> sending LinkStatus:0x03:error:)
7264:DEBUG:stick:sleeping 0.001
7275:INFO:stick:quit send_force_read, found len: 64 expected 64 after 0 attempts
7276:INFO:stick:LinkStatus:0x03:error:
7278:INFO:stick:finished processing LinkStatus:0x03:error:, 206
7279:DEBUG:stick:sleeping in POLL, .100
7280:INFO:stick:STOP POLL after 1 attempts:size:206
7281:INFO:stick:download_packet:206
7282:INFO:stick:send_force_read: attempt 0/5 send command, read until we get something within some timeout
7283:INFO:stick:link Stick:status:<LinkStatus:0x03:error::size(206)>:command:<ReadRadio:size:206> sending ReadRadio:size:206)
7286:DEBUG:stick:sleeping 0.001
7315:INFO:stick:quit send_force_read, found len: 206 expected 206 after 0 attempts
7316:INFO:stick:readData validating remote raw[ack]: 02
7317:INFO:stick:readData; foreign raw should be at least 14 bytes? 206 True
7318:INFO:stick:readData; raw[retries] 0
7319:INFO:stick:found packet len(192), link expects(192)
7320:WARNING:stick:bad zero CRC?
7321:INFO:stick:ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x06:raw:
7408:    data = self.stick.download( )
7409:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 555, in download
7411:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 503, in download_packet
7413:  File "/home/bewest/src/decoding-carelink/pump/stick.py", line 263, in parse
7415:stick.BadCRC: ReadRadio:BAD ACK:found raw[crc]: 0x00:expected_crc(data): 0x06:raw:
```

## There was a Bad CRC.

```
7500:Was there an ACK ERROR?
7502:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
7689:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2172L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2172L, 'errors.crc': 0}
7707:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1084L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1028L, 'errors.crc': 0}
7708:INFO:__main__:{'radio': {'errors.crc': 0,
7709:           'errors.naks': 0,
7710:           'errors.sequence': 0,
7711:           'errors.timeouts': 3,
7712:           'packets.received': 1028L,
7713:           'packets.transmit': 1084L},
7714: 'usb': {'errors.crc': 0,
7715:         'errors.naks': 0,
7716:         'errors.sequence': 0,
7717:         'errors.timeouts': 0,
7718:         'packets.received': 2172L,
7719:         'packets.transmit': 2172L}}
7738:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2174L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2174L, 'errors.crc': 0}
7756:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1084L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1028L, 'errors.crc': 0}
7758:{'radio': {'errors.crc': 0,
7759:           'errors.naks': 0,
7760:           'errors.sequence': 0,
7761:           'errors.timeouts': 3,
7762:           'packets.received': 1028L,
7763:           'packets.transmit': 1084L},
7764: 'usb': {'errors.crc': 0,
7765:         'errors.naks': 0,
7766:         'errors.sequence': 0,
7767:         'errors.timeouts': 0,
7768:         'packets.received': 2174L,
7769:         'packets.transmit': 2174L}}
7770:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
7796:INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 270
7797:INFO:__main__:XXX:clear_buffer[attempt][0]:download the size? 270:segments[0],total_segments[0]:raw[0]
7798:INFO:__main__:XXX:clear_buffer[attempt][0] size:270:segments[0],total_segments[0]:raw[0]:clear_buffer BUFFER self.download( )
8055:INFO:__main__:XXX:clear_buffer[attempt][0]:tx:found:segments[1],total_segments[768]:raw[768]:len(raw):768:expected:270:len(segment):768
8056:INFO:__main__:XXX:clear_buffer[attempt][0] downloaded 768 segment:segments[1],total_segments[768]:raw[768]:RAW:
8264:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2189L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2189L, 'errors.crc': 0}
8282:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1092L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1036L, 'errors.crc': 0}
8284:{'radio': {'errors.crc': 0,
8285:           'errors.naks': 0,
8286:           'errors.sequence': 0,
8287:           'errors.timeouts': 3,
8288:           'packets.received': 1036L,
8289:           'packets.transmit': 1092L},
8290: 'usb': {'errors.crc': 0,
8291:         'errors.naks': 0,
8292:         'errors.sequence': 0,
8293:         'errors.timeouts': 0,
8294:         'packets.received': 2189L,
8295:         'packets.transmit': 2189L}}
```

## several packets
> 7758:{'radio': {'errors.crc': 0,
> 7759:           'errors.naks': 0,
> 7760:           'errors.sequence': 0,
> 7761:           'errors.timeouts': 3,
> 7762:           'packets.received': 1028L,
> 7763:           'packets.transmit': 1084L},
> [...]
> 8284:{'radio': {'errors.crc': 0,
> 8285:           'errors.naks': 0,
> 8286:           'errors.sequence': 0,
> 8287:           'errors.timeouts': 3,
> 8288:           'packets.received': 1036L,
> 8289:           'packets.transmit': 1092L},

```
8410:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2191L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2191L, 'errors.crc': 0}
8428:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1092L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1036L, 'errors.crc': 0}
8430:{'radio': {'errors.crc': 0,
8431:           'errors.naks': 0,
8432:           'errors.sequence': 0,
8433:           'errors.timeouts': 3,
8434:           'packets.received': 1036L,
8435:           'packets.transmit': 1092L},
8436: 'usb': {'errors.crc': 0,
8437:         'errors.naks': 0,
8438:         'errors.sequence': 0,
8439:         'errors.timeouts': 0,
8440:         'packets.received': 2191L,
8441:         'packets.transmit': 2191L}}
8442:python pump/stick.py /dev/ttyUSB0
8447:INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
8634:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2201L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2201L, 'errors.crc': 0}
8652:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1092L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1036L, 'errors.crc': 0}
8653:INFO:__main__:{'radio': {'errors.crc': 0,
8654:           'errors.naks': 0,
8655:           'errors.sequence': 0,
8656:           'errors.timeouts': 3,
8657:           'packets.received': 1036L,
8658:           'packets.transmit': 1092L},
8659: 'usb': {'errors.crc': 0,
8660:         'errors.naks': 0,
8661:         'errors.sequence': 0,
8662:         'errors.timeouts': 0,
8663:         'packets.received': 2201L,
8664:         'packets.transmit': 2201L}}
8683:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2203L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2203L, 'errors.crc': 0}
8701:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1092L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1036L, 'errors.crc': 0}
8703:{'radio': {'errors.crc': 0,
8704:           'errors.naks': 0,
8705:           'errors.sequence': 0,
8706:           'errors.timeouts': 3,
8707:           'packets.received': 1036L,
8708:           'packets.transmit': 1092L},
8709: 'usb': {'errors.crc': 0,
8710:         'errors.naks': 0,
8711:         'errors.sequence': 0,
8712:         'errors.timeouts': 0,
8713:         'packets.received': 2203L,
8714:         'packets.transmit': 2203L}}
8715:INFO:__main__:XXX:clear_buffer[attempt][0]:segments[0],total_segments[0]:raw[0]:BEGIN :first poll
8810:INFO:__main__:XXX:clear_buffer[attempt][0]:END first poll: poll the size? 0
8828:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2209L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2209L, 'errors.crc': 0}
8846:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1092L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1036L, 'errors.crc': 0}
8847:INFO:__main__:XXX:clear_buffer[attempt][0]:END:no data:INTERFACE STATS
8848:{'radio': {'errors.crc': 0,
8849:           'errors.naks': 0,
8850:           'errors.sequence': 0,
8851:           'errors.timeouts': 3,
8852:           'packets.received': 1036L,
8853:           'packets.transmit': 1092L},
8854: 'usb': {'errors.crc': 0,
8855:         'errors.naks': 0,
8856:         'errors.sequence': 0,
8857:         'errors.timeouts': 0,
8858:         'packets.received': 2209L,
8859:         'packets.transmit': 2209L}}
8879:INFO:__main__:finished processing UsbStats:0x05 0x01, {'errors.timeouts': 0, 'packets.transmit': 2211L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 2211L, 'errors.crc': 0}
8897:INFO:__main__:finished processing RadioStats:0x05 0x00, {'errors.timeouts': 3, 'packets.transmit': 1092L, 'errors.naks': 0, 'errors.sequence': 0, 'packets.received': 1036L, 'errors.crc': 0}
8899:{'radio': {'errors.crc': 0,
8900:           'errors.naks': 0,
8901:           'errors.sequence': 0,
8902:           'errors.timeouts': 3,
8903:           'packets.received': 1036L,
8904:           'packets.transmit': 1092L},
8905: 'usb': {'errors.crc': 0,
8906:         'errors.naks': 0,
8907:         'errors.sequence': 0,
8908:         'errors.timeouts': 0,
8909:         'packets.received': 2211L,
8910:         'packets.transmit': 2211L}}
8911:python pump/stick.py /dev/ttyUSB0
```

Second time there's no data left.
