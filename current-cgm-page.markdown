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
<<<<<<< HEAD
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 51L,
           'packets.transmit': 53L},
 'usb': {'errors.crc': 0,
         'errors.naks': 6,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 118L,
         'packets.transmit': 124L}}
=======
           'errors.sequence': 2,
           'errors.timeouts': 10,
           'packets.received': 777L,
           'packets.transmit': 829L},
 'usb': {'errors.crc': 0,
         'errors.naks': 3,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 1681L,
         'packets.transmit': 1684L}}
>>>>>>> 6a884cff54ebd2eff5ea802055e7af0281b44421
```
```
PowerControl SERIAL 584923
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'722'`
###### sending `<class 'decocare.commands.ReadCurPageNumber'>`
response: ReadCurPageNumber:pages:18
#### decoded:
```python
18L
```
###### sending `<class 'decocare.commands.ReadCurGlucosePageNumber'>`
response: ReadCurGlucosePageNumber:size[64]:data:{'isig': 14, 'page': 13L, 'glucose': 14}
#### decoded:
```python
{'isig': 14, 'page': 13L, 'glucose': 14}
```
### end stats
```
```
```javascript
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
<<<<<<< HEAD
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 56L,
           'packets.transmit': 58L},
 'usb': {'errors.crc': 0,
         'errors.naks': 6,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 132L,
         'packets.transmit': 138L}}
=======
           'errors.sequence': 2,
           'errors.timeouts': 10,
           'packets.received': 782L,
           'packets.transmit': 834L},
 'usb': {'errors.crc': 0,
         'errors.naks': 3,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 1695L,
         'packets.transmit': 1698L}}
>>>>>>> 6a884cff54ebd2eff5ea802055e7af0281b44421
```
