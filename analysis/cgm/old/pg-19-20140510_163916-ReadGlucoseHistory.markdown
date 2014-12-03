## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=True, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='ReadGlucoseHistory', page=19, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/20140510_163916-', save=True, saveall=False, serial='584923', verbose=None) `
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
           'errors.timeouts': 9,
           'packets.received': 375L,
           'packets.transmit': 398L},
 'usb': {'errors.crc': 0,
         'errors.naks': 0,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 867L,
         'packets.transmit': 867L}}
```
```
PowerControl SERIAL 584923
ERROR:decocare.stick:size (14) is less than 64 and not 15, which may cause an error.
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[2] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[2],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[3] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[3],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[4] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[4],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[5] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[5],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[6] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[6],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[7] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[7],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[8] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[8],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[9] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[9],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[10] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[10],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[11] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[11],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[12] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[12],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[13] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[13],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[14] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[14],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[15] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[15],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[16] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[16],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[17] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[17],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[18] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[18],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[19] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[19],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[20] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[20],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[21] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[21],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[22] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[22],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[23] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[23],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[24] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[24],expect[0],results[0]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:PowerControl:data:unknown] reader[ReadRadio:size:14] download_i[25] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[25],expect[0],results[0]:data[0]):BAD AILING
