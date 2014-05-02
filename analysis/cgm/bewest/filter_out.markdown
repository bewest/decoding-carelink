## do stuff with an insulin pump over RF
using ` Namespace(begin=datetime.datetime(2009, 1, 1, 0, 0), bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=datetime.datetime(2014, 1, 1, 0, 0), init=False, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='FilterGlucoseHistory', page=None, params=None, port='', postfix=None, prefix=None, prefix_path='', save=False, saveall=False, serial='665455', verbose=None) `
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
           'packets.received': 8L,
           'packets.transmit': 8L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 53L,
         'packets.transmit': 53L}}
```
```
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'522'`
<class 'decocare.commands.FilterGlucoseHistory'> {'begin': datetime.datetime(2009, 1, 1, 0, 0), 'end': datetime.datetime(2014, 1, 1, 0, 0)}
response: FilterGlucoseHistory:size[64]:data:{'begin': 82, 'end': 113}
hexdump:
```python
0000   0x00 0x52 0x00 0x71 0x00 0x00 0x00 0x00    .R.q....
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
```
#### decoded:
```python
{'begin': 82, 'end': 113}
```
### end stats
```
```
```javascript
{'radio': {'errors.crc': 0,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 0,
           'packets.received': 11L,
           'packets.transmit': 11L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 61L,
         'packets.transmit': 61L}}
```
