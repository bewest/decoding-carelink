## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=True, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='ReadGlucoseHistory', page=19, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/20140510_165945-', save=True, saveall=False, serial='584923', verbose=None) `
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
           'errors.timeouts': 41,
           'packets.received': 613L,
           'packets.transmit': 684L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 2068L,
         'packets.transmit': 2068L}}
```
```
PowerControl SERIAL 584923
ERROR:decocare.stick:size (14) is less than 64 and not 15, which may cause an error.
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[2] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[2],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[3] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[3],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[4] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[4],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[5] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[5],expect[0],results[0]:data[0]):BAD AILING
