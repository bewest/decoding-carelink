## do stuff with an insulin pump over RF
using ` Namespace(begin=None, bytesPerRecord=None, command='tweak', descr=None, dryrun=False, effectTime=None, end=None, init=False, maxRecords=None, name=None, no_postlude=False, no_prelude=False, no_rf_prelude=False, other='ReadSensorHistoryData', page=34, params=None, port='/dev/ttyUSB0', postfix=None, prefix=None, prefix_path='logs/cgm-page-34-', save=True, saveall=False, serial='584923', verbose=None) `
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
           'errors.sequence': 2,
           'errors.timeouts': 11,
           'packets.received': 1399L,
           'packets.transmit': 1486L},
 'usb': {'errors.crc': 0,
         'errors.naks': 3,
         'errors.sequence': 0,
         'errors.timeouts': 0,
         'packets.received': 2731L,
         'packets.transmit': 2734L}}
```
```
```
### PUMP MODEL: `ReadPumpModel:size[64]:data:'722'`
<class 'decocare.commands.ReadSensorHistoryData'> {'page': 34}
ERROR:decocare.stick:size (14) is less than 64 and not 15, which may cause an error.
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[4] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[4],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[5] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[5],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[6] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[6],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[7] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[7],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[8] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[8],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[9] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[9],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[10] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[10],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[11] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[11],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[12] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[12],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[13] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[13],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[14] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[14],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[15] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[15],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[16] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[16],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[17] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[17],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[18] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[18],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[19] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[19],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[20] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[20],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[21] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[21],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[22] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[22],expect[0],results[192]:data[0]):BAD AILING
WARNING:decocare.stick:Stick transmit[TransmitPacket:ReadSensorHistoryData:size[1024]:[page][0]:data[0]:] reader[ReadRadio:size:14] download_i[23] status[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>] poll_size[0] poll_i[False] command[<LinkStatus:0x03:status:size=??LinkStatus:error:True:reason:[]:size(0)>]:download(attempts[23],expect[0],results[192]:data[0]):BAD AILING
