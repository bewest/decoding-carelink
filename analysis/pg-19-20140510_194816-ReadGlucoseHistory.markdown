## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=True, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='ReadGlucoseHistory', page=19, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/20140510_194816-', save=True, saveall=False, serial='584923', verbose=None) `
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
           'packets.received': 0L,
           'packets.transmit': 0L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 3L,
         'packets.transmit': 3L}}
```
```
PowerControl SERIAL 584923
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'722'`
<class 'decocare.commands.ReadGlucoseHistory'> {'page': 19}
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][19]:data[0]:] reader[ReadRadio:size:206] download_i[4] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[4],expect[0],results[320]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][19]:data[0]:] reader[ReadRadio:size:334] download_i[7] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[7],expect[0],results[768]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][19]:data[0]:] reader[ReadRadio:size:334] download_i[8] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[8],expect[0],results[768]:data[0]):BAD AILING
ERROR:decocare.stick:size (14) is less than 64 and not 15, which may cause an error.
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][19]:data[0]:] reader[ReadRadio:size:14] download_i[10] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[10],expect[0],results[768]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][19]:data[0]:] reader[ReadRadio:size:14] download_i[11] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[11],expect[0],results[768]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][19]:data[0]:] reader[ReadRadio:size:14] download_i[12] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[12],expect[0],results[768]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][19]:data[0]:] reader[ReadRadio:size:14] download_i[13] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[13],expect[0],results[768]:data[0]):BAD AILING
