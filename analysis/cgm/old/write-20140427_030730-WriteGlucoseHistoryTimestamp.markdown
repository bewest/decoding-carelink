## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=True, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='WriteGlucoseHistoryTimestamp', page=None, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/20140427_030730-', save=True, saveall=False, serial='584923', verbose=None) `
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
           'errors.timeouts': 16,
           'packets.received': 314L,
           'packets.transmit': 349L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 816L,
         'packets.transmit': 816L}}
```
```
PowerControl SERIAL 584923
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'722'`
<class 'decocare.commands.WriteGlucoseHistoryTimestamp'> {}
CRITICAL:decocare.session:this seems like a problem
response: WriteGlucoseHistoryTimestamp:size[64]:data:bytearray(b'\x00')
hexdump:
```python
0000   0x00                                       .
```
#### decoded:
```python
bytearray(b'\x00')
```
### end stats
```
```
```javascript
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 16,
           'packets.received': 319L,
           'packets.transmit': 354L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 830L,
         'packets.transmit': 830L}}
```
