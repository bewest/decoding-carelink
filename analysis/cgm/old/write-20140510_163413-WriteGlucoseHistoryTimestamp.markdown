## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=True, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='WriteGlucoseHistoryTimestamp', page=None, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/20140510_163413-', save=True, saveall=False, serial='584923', verbose=None) `
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
           'errors.timeouts': 1,
           'packets.received': 285L,
           'packets.transmit': 296L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 458L,
         'packets.transmit': 458L}}
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
           'errors.timeouts': 1,
           'packets.received': 290L,
           'packets.transmit': 301L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 472L,
         'packets.transmit': 472L}}
```
