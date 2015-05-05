## do stuff with an insulin pump over RF
using ` Namespace(command='sleep', dryrun=False, init=True, no_postlude=False, no_prelude=False, no_rf_prelude=False, port='/dev/ttyUSB0', postfix=None, prefix=['ReadCurPageNumber', 'ReadCurGlucosePageNumber'], prefix_path='', saveall=False, serial='584923', timeout=0.0, verbose=None) `
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
           'errors.timeouts': 0,
           'packets.received': 14L,
           'packets.transmit': 14L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 57L,
         'packets.transmit': 57L}}
```
```
PowerControl SERIAL 584923
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'722'`
###### sending `<class 'decocare.commands.ReadCurPageNumber'>`
response: ReadCurPageNumber:pages:23
#### decoded:
```python
23L
```
###### sending `<class 'decocare.commands.ReadCurGlucosePageNumber'>`
response: ReadCurGlucosePageNumber:size[64]:data:{'isig': 20, 'page': 19L, 'glucose': 20}
#### decoded:
```python
{'isig': 20, 'page': 19L, 'glucose': 20}
```
### end stats
```
```
```javascript
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 19L,
           'packets.transmit': 19L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 71L,
         'packets.transmit': 71L}}
```
