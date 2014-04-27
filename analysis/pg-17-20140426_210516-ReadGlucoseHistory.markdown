## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=True, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='ReadGlucoseHistory', page=17, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/20140426_210516-', save=True, saveall=False, serial='584923', verbose=None) `
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
           'errors.timeouts': 39,
           'packets.received': 530L,
           'packets.transmit': 588L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 1157L,
         'packets.transmit': 1157L}}
```
```
PowerControl SERIAL 584923
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'722'`
<class 'decocare.commands.ReadGlucoseHistory'> {'page': 17}
ERROR:decocare.stick:size (14) is less than 64 and not 15, which may cause an error.
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[3] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[3],expect[0],results[64]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[4] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[4],expect[0],results[64]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[5] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[5],expect[0],results[64]:data[0]):BAD AILING
