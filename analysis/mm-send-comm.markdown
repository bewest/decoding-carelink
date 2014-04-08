+ ./bin/mm-send-comm.py --init --prefix PushACT ManualCommand 141 --descr 'get model' --name FetchModelNumber
## do stuff with an insulin pump over RF
using ` Namespace(bytesPerRecord=64, code=141, command='ManualCommand', descr='get model', dryrun=False, effectTime=0.5, init=True, maxRecords=1, name='FetchModelNumber', no_postlude=False, no_prelude=False, no_rf_prelude=False, params=[], port='/dev/serial/by-id/usb-0a21_8001-if00-port0', postfix=None, prefix=['PushACT'], prefix_path='', save=False, saveall=False, serial='208850', verbose=None) `
```
```
```
```
```
```
```
```
```javascript
{'radio': {'errors.crc': 2,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 26,
           'packets.received': 226L,
           'packets.transmit': 262L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 1475L,
         'packets.transmit': 1475L}}
```
```
PowerControl SERIAL 208850
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'515'`
###### sending `<function PushACT at 0x203c5f0>`
response: KeypadPush:data:unknown
#### decoded:
```python

```
response: FetchModelNumber:{'retries': 0, 'effectTime': 0.5, 'code': 141, 'name': 'FetchModelNumber', 'descr': 'get model', 'bytesPerRecord': 64, 'maxRecords': 1, 'params': [], 'serial': '208850'}:size[64]:
#### decoded:
```python
0000   0x03 0x35 0x31 0x35 0x00 0x00 0x00 0x00    .515....
0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
```
### end stats
```
```
```javascript
{'radio': {'errors.crc': 2,
           'errors.naks': 0,
           'errors.sequence': 0,
           'errors.timeouts': 26,
           'packets.received': 232L,
           'packets.transmit': 268L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 1487L,
         'packets.transmit': 1487L}}
```
