## query or set suspend/resume status
hi ` Namespace(commands=['suspend'], dryrun=False, init=False, port='/dev/ttyUSB.Carelink0', serial='208850', verbose=None) `
```
```
```
```
```
```
```
```
```javascript
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 15,
           'packets.received': 60L,
           'packets.transmit': 77L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 2716L,
         'packets.transmit': 2716L}}
```
```
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'515'`
###  suspend
ERROR:decocare.stick:size is less than 64, which will cause an error. trying 64 instead
WARNING:decocare.stick:bad zero CRC?
ERROR:decocare.stick:size is less than 64, which will cause an error. trying 64 instead
WARNING:decocare.stick:bad zero CRC?
CRITICAL:decocare.session:this seems like a problem
response: %s PumpSuspend:size[64]:data:bytearray(b'\x00')
hexdump:
0000   0x00                                       .
```
### end stats
```
```
```javascript
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 15,
           'packets.received': 65L,
           'packets.transmit': 82L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 2727L,
         'packets.transmit': 2727L}}
```
