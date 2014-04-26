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
           'errors.timeouts': 3,
           'packets.received': 2L,
           'packets.transmit': 6L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 54L,
         'packets.transmit': 54L}}
```
```
PowerControl SERIAL 584923
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'722'`
###### sending `<class 'decocare.commands.ReadCurPageNumber'>`
response: ReadCurPageNumber:pages:20
#### decoded:
```python
20L
```
###### sending `<class 'decocare.commands.ReadCurGlucosePageNumber'>`
response: ReadCurGlucosePageNumber:size[64]:data:{'isig': 18, 'page': 17L, 'glucose': 18}
#### decoded:
```python
{'isig': 18, 'page': 17L, 'glucose': 18}
```
### end stats
```
```
```javascript
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 3,
           'packets.received': 7L,
           'packets.transmit': 11L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 68L,
         'packets.transmit': 68L}}
```
