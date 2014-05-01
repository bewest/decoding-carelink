## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=True, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='ReadGlucoseHistory', page=18, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/20140430_220621-', save=True, saveall=False, serial='584923', verbose=None) `
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
<class 'decocare.commands.ReadGlucoseHistory'> {'page': 18}
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:142] download_i[6] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[6],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:142] download_i[7] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[7],expect[0],results[512]:data[0]):BAD AILING
ERROR:decocare.stick:size (14) is less than 64 and not 15, which may cause an error.
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[9] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[9],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[10] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[10],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[11] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[11],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[12] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[12],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[13] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[13],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[14] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[14],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[15] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[15],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[16] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[16],expect[0],results[512]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadGlucoseHistory:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[17] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[17],expect[0],results[512]:data[0]):BAD AILING
