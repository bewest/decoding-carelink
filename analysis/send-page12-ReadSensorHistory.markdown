## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=False, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='ReadSensorHistoryData', page=12, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/cgm-page-12-', save=True, saveall=False, serial='584923', verbose=None) `
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
           'errors.timeouts': 4,
           'packets.received': 203L,
           'packets.transmit': 218L},
 'usb': {'errors.crc': 0,
         'errors.naks': 3,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 421L,
         'packets.transmit': 424L}}
```
```
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'722'`
<class 'decocare.commands.ReadSensorHistoryData'> {'page': 12}
WARNING:decocare.stick:bad zero CRC?
ERROR:decocare.stick:size (14) is less than 64 and not 15, which may cause an error.
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[11] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[11],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[12] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[12],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[13] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[13],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[14] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[14],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[15] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[15],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[16] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[16],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[17] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[17],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[18] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[18],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[19] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[19],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[20] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[20],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[21] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[21],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[22] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[22],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[23] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[23],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[24] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[24],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[25] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[25],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[26] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[26],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[27] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[27],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[28] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[28],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[29] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[29],expect[0],results[960]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[30] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[30],expect[0],results[960]:data[0]):BAD AILING
