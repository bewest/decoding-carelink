## START ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 983, found 39 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x7a 0x2c                                  z,
##### DEBUG DECIMAL
            122   44
#### RECORD 0 Bolus 2015-03-08T06:28:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2015-03-08T06:28:25)
    0000   0x19 0xdc 0x46 0x68 0x0f                   ..Fh.
    body (0)

#### RECORD 1 BasalProfileStart 2015-03-08T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-08T07:00:00)
    0000   0x00 0xc0 0x07 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 2 SensorAlert 2015-03-08T07:55:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-08T07:55:00)
    0000   0x00 0xf7 0x27 0xa8 0x0f                   ..'..
    body (0)

#### RECORD 3 SensorAlert 2015-03-08T08:17:40 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-08T08:17:40)
    0000   0x28 0xd1 0x28 0xa8 0x0f                   (.(..
    body (0)

#### RECORD 4 SensorAlert 2015-03-08T08:55:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-08T08:55:00)
    0000   0x00 0xf7 0x28 0xa8 0x0f                   ..(..
    body (0)

#### RECORD 5 CalBGForPH 2015-03-08T09:07:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2015-03-08T09:07:44)
    0000   0x2c 0xc7 0x29 0x68 0x0f                   ,.)h.
    body (0)

#### RECORD 6 BGReceived 2015-03-08T09:07:44 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 75, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2015-03-08T09:07:44)
    0000   0x2c 0xc7 0x69 0x68 0x0f                   ,.ih.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 7 BasalProfileStart 2015-03-08T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-08T10:00:00)
    0000   0x00 0xc0 0x0a 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 8 SensorAlert 2015-03-08T10:22:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-08T10:22:33)
    0000   0x21 0xd6 0x2a 0xa8 0x0f                   !.*..
    body (0)

#### RECORD 9 BolusWizard 2015-03-08T10:23:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.0,
 'carb_input': 70,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 7.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-08T10:23:16)
    0000   0x10 0xd7 0x0a 0x68 0x0f                   ...h.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    FP.d(Z..
    0008   0x18 0x00 0x00 0x00 0x01 0x18 0x78         ......x
    decimal
             70   80    0  100   40   90    0    1
             24    0    0    0    1   24  120

#### RECORD 10 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 234, 'amount': 0.65}, {'age': 244, 'amount': 0.85}]
```
    op hex (8)
    0000   0x5c 0x08 0x1a 0xea 0x04 0x22 0xf4 0x04    \...."..
    decimal
             92    8   26  234    4   34  244    4
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2015-03-08T10:27:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 60,
 'programmed': 1.0,
 'type': 'square',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x04 0x02    ..(.(...
    decimal
              1    0   40    0   40    0    4    2
    datetime (2015-03-08T10:27:19)
    0000   0x13 0xdb 0xaa 0x68 0x0f                   ...h.
    body (0)

#### RECORD 12 Bolus 2015-03-08T10:23:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0x04 0x00    ........
    decimal
              1    0  240    0  240    0    4    0
    datetime (2015-03-08T10:23:17)
    0000   0x11 0xd7 0x8a 0x68 0x0f                   ...h.
    body (0)

#### RECORD 13 SensorAlert 2015-03-08T10:37:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 191}
```
    op hex (3)
    0000   0x0b 0x65 0xbf                             .e.
    decimal
             11  101  191
    datetime (2015-03-08T10:37:12)
    0000   0x0c 0xe5 0x2a 0xa8 0x0f                   ..*..
    body (0)

#### RECORD 14 BasalProfileStart 2015-03-08T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-08T12:00:00)
    0000   0x00 0xc0 0x0c 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 15 ChangeTimeDisplay 2015-03-08T12:27:03 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2015-03-08T12:27:03)
    0000   0x03 0xdb 0x0c 0x08 0x0f                   .....
    body (0)

#### RECORD 16 ChangeTime 2015-03-08T12:27:09 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2015-03-08T12:27:09)
    0000   0x09 0xdb 0x0c 0x08 0x0f                   .....
    body (0)

#### RECORD 17 NewTimeSet 2015-03-08T13:27:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2015-03-08T13:27:00)
    0000   0x00 0xdb 0x0d 0x08 0x0f                   .....
    body (0)

#### RECORD 18 SensorAlert 2015-03-08T14:47:11 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-08T14:47:11)
    0000   0x0b 0xef 0x2e 0xa8 0x0f                   .....
    body (0)

#### RECORD 19 SensorAlert 2015-03-08T14:57:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-08T14:57:02)
    0000   0x02 0xf9 0x2e 0xa8 0x0f                   .....
    body (0)

#### RECORD 20 BasalProfileStart 2015-03-08T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-08T15:00:00)
    0000   0x00 0xc0 0x0f 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 21 PumpSuspend 2015-03-08T16:24:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-08T16:24:21)
    0000   0x15 0xd8 0x10 0x08 0x0f                   .....
    body (0)

#### RECORD 22 SensorAlert 2015-03-08T16:47:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 244}
```
    op hex (3)
    0000   0x0b 0x65 0xf4                             .e.
    decimal
             11  101  244
    datetime (2015-03-08T16:47:25)
    0000   0x19 0xef 0x30 0xa8 0x0f                   ..0..
    body (0)

#### RECORD 23 BasalProfileStart 2015-03-08T16:48:17 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-08T16:48:17)
    0000   0x11 0xf0 0x10 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 24 PumpResume 2015-03-08T16:48:17 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-08T16:48:17)
    0000   0x11 0xf0 0x10 0x08 0x0f                   .....
    body (0)

#### RECORD 25 Bolus 2015-03-08T16:48:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2015-03-08T16:48:27)
    0000   0x1b 0xf0 0x50 0x68 0x0f                   ..Ph.
    body (0)

#### RECORD 26 PumpSuspend 2015-03-08T16:49:51 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-08T16:49:51)
    0000   0x33 0xf1 0x10 0x08 0x0f                   3....
    body (0)

#### RECORD 27 BasalProfileStart 2015-03-08T17:17:39 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-08T17:17:39)
    0000   0x27 0xd1 0x11 0x08 0x0f                   '....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 28 PumpResume 2015-03-08T17:17:39 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-08T17:17:39)
    0000   0x27 0xd1 0x11 0x08 0x0f                   '....
    body (0)

#### RECORD 29 CalBGForPH 2015-03-08T17:18:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 368}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2015-03-08T17:18:36)
    0000   0x24 0xd2 0x31 0x68 0x8f                   $.1h.
    body (0)

#### RECORD 30 BGReceived 2015-03-08T17:18:36 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 368, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2e                                  ?.
    decimal
             63   46
    datetime (2015-03-08T17:18:36)
    0000   0x24 0xd2 0x11 0x68 0x0f                   $..h.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 31 BolusWizard 2015-03-08T17:18:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 368,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.3,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 6.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.9}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2015-03-08T17:18:46)
    0000   0x2e 0xd2 0x11 0x08 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x50 0x28 0x5a 0xf8 0x00    .Q.P(Z..
    0008   0x00 0x00 0x00 0x4c 0x00 0xac 0x78         ...L..x
    decimal
              0   81    0   80   40   90  248    0
              0    0    0   76    0  172  120

#### RECORD 32 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 1.2},
 {'age': 39, 'amount': 0.8},
 {'age': 299, 'amount': 0.15},
 {'age': 309, 'amount': 0.15},
 {'age': 319, 'amount': 0.15},
 {'age': 329, 'amount': 0.2},
 {'age': 339, 'amount': 0.15},
 {'age': 349, 'amount': 0.15},
 {'age': 359, 'amount': 6.05}]
```
    op hex (29)
    0000   0x5c 0x1d 0x30 0x1d 0x04 0x20 0x27 0x04    \.0.. '.
    0008   0x06 0x2b 0x14 0x06 0x35 0x14 0x06 0x3f    .+..5..?
    0010   0x14 0x08 0x49 0x14 0x06 0x53 0x14 0x06    ..I..S..
    0018   0x5d 0x14 0xf2 0x67 0x14                   ]..g.
    decimal
             92   29   48   29    4   32   39    4
              6   43   20    6   53   20    6   63
             20    8   73   20    6   83   20    6
             93   20  242  103   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2015-03-08T17:18:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3,
 'duration': 0,
 'programmed': 4.3,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0x4c 0x00    ......L.
    decimal
              1    0  172    0  172    0   76    0
    datetime (2015-03-08T17:18:46)
    0000   0x2e 0xd2 0x51 0x08 0x0f                   ..Q..
    body (0)

#### RECORD 34 SensorAlert 2015-03-08T18:31:51 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 112'}
```
    op hex (3)
    0000   0x0b 0x70 0x00                             .p.
    decimal
             11  112    0
    datetime (2015-03-08T18:31:51)
    0000   0x33 0xdf 0x32 0xa8 0x0f                   3.2..
    body (0)

#### RECORD 35 SensorAlert 2015-03-08T18:37:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 113'}
```
    op hex (3)
    0000   0x0b 0x71 0x00                             .q.
    decimal
             11  113    0
    datetime (2015-03-08T18:37:49)
    0000   0x31 0xe5 0x32 0xa8 0x0f                   1.2..
    body (0)

#### RECORD 36 BolusWizard 2015-03-08T20:22:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.6,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-08T20:22:22)
    0000   0x16 0xd6 0x14 0x68 0x0f                   ...h.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    (P.<(Z..
    0008   0x08 0x00 0x00 0x00 0x01 0x08 0x78         ......x
    decimal
             40   80    0   60   40   90    0    1
              8    0    0    0    1    8  120

#### RECORD 37 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 183, 'amount': 3.95},
 {'age': 193, 'amount': 0.35},
 {'age': 213, 'amount': 1.2},
 {'age': 223, 'amount': 0.8}]
```
    op hex (14)
    0000   0x5c 0x0e 0x9e 0xb7 0x04 0x0e 0xc1 0x04    \.......
    0008   0x30 0xd5 0x04 0x20 0xdf 0x04              0.. ..
    decimal
             92   14  158  183    4   14  193    4
             48  213    4   32  223    4
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2015-03-08T20:24:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3,
 'duration': 180,
 'programmed': 3.3,
 'type': 'square',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x24 0x06    ......$.
    decimal
              1    0  132    0  132    0   36    6
    datetime (2015-03-08T20:24:37)
    0000   0x25 0xd8 0xb4 0x68 0x0f                   %..h.
    body (0)

#### RECORD 39 Bolus 2015-03-08T20:22:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3,
 'duration': 0,
 'programmed': 3.3,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x24 0x00    ......$.
    decimal
              1    0  132    0  132    0   36    0
    datetime (2015-03-08T20:22:22)
    0000   0x16 0xd6 0x94 0x68 0x0f                   ...h.
    body (0)

#### RECORD 40 BasalProfileStart 2015-03-08T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-08T22:00:00)
    0000   0x00 0xc0 0x16 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 41 SensorAlert 2015-03-08T22:03:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-03-08T22:03:00)
    0000   0x00 0xc3 0x36 0xa8 0x0f                   ..6..
    body (0)

#### RECORD 42 Bolus 2015-03-08T23:15:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 2.6}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x68 0x00    ..x.x.h.
    decimal
              1    0  120    0  120    0  104    0
    datetime (2015-03-08T23:15:44)
    0000   0x2c 0xcf 0x57 0x68 0x0f                   ,.Wh.
    body (0)

#### RECORD 43 BasalProfileStart 2015-03-09T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-09T00:00:00)
    0000   0x00 0xc0 0x00 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 44 MResultTotals 2015-03-09T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x16                   .....
    decimal
              7    0    0    7   22
    datetime (2015-03-09T00:00:00)
    0000   0x28 0x8f                                  (.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 45 Sara6E 2015-03-09T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-09T00:00:00)
    0000   0x28 0x8f                                  (.
    body (49)
    hex
    0000   0x05 0x10 0xde 0x4b 0x70 0x02 0x00 0x00    ...Kp...
    0008   0x07 0x16 0x02 0xf6 0x2a 0x04 0x20 0x3a    ....*. :
    0010   0x00 0x6e 0x02 0x20 0x00 0xac 0x00 0x00    .n. ....
    0018   0x01 0x54 0x02 0x01 0x00 0x04 0x00 0xad    .T......
    0020   0x2a 0x3a 0x00 0xc6 0x38 0x05 0x01 0x00    *:..8...
    0028   0x00 0x00 0x04 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  222   75  112    2    0    0
              7   22    2  246   42    4   32   58
              0  110    2   32    0  172    0    0
              1   84    2    1    0    4    0  173
             42   58    0  198   56    5    1    0
              0    0    4    0    0    0    0    0
              0

#### RECORD 46 BasalProfileStart 2015-03-09T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-09T04:00:00)
    0000   0x00 0xc0 0x04 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 47 Bolus 2015-03-09T06:43:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2015-03-09T06:43:54)
    0000   0x36 0xeb 0x46 0x69 0x0f                   6.Fi.
    body (0)

#### RECORD 48 BasalProfileStart 2015-03-09T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-09T07:00:00)
    0000   0x00 0xc0 0x07 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 49 BolusWizard 2015-03-09T07:53:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.0,
 'carb_input': 70,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 7.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-09T07:53:50)
    0000   0x32 0xf5 0x07 0x69 0x0f                   2..i.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    FP.d(Z..
    0008   0x18 0x00 0x00 0x00 0x01 0x18 0x78         ......x
    decimal
             70   80    0  100   40   90    0    1
             24    0    0    0    1   24  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 74, 'amount': 2.0}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x4a 0x04                   \.PJ.
    decimal
             92    5   80   74    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2015-03-09T07:53:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.7,
 'duration': 0,
 'programmed': 5.7,
 'type': 'normal',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x00 0xe4 0x00 0xe4 0x00 0x3c 0x00    ......<.
    decimal
              1    0  228    0  228    0   60    0
    datetime (2015-03-09T07:53:50)
    0000   0x32 0xf5 0x47 0x69 0x0f                   2.Gi.
    body (0)

#### RECORD 52 SensorAlert 2015-03-09T08:14:50 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 113'}
```
    op hex (3)
    0000   0x0b 0x71 0x00                             .q.
    decimal
             11  113    0
    datetime (2015-03-09T08:14:50)
    0000   0x32 0xce 0x28 0xa9 0x0f                   2.(..
    body (0)

#### RECORD 53 BasalProfileStart 2015-03-09T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-09T10:00:00)
    0000   0x00 0xc0 0x0a 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 54 SensorAlert 2015-03-09T10:28:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-09T10:28:04)
    0000   0x04 0xdc 0x2a 0xa9 0x0f                   ..*..
    body (0)

#### RECORD 55 SensorAlert 2015-03-09T10:58:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-09T10:58:00)
    0000   0x00 0xfa 0x2a 0xa9 0x0f                   ..*..
    body (0)

#### RECORD 56 SensorAlert 2015-03-09T11:28:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-09T11:28:00)
    0000   0x00 0xdc 0x2b 0xa9 0x0f                   ..+..
    body (0)

#### RECORD 57 SensorAlert 2015-03-09T11:58:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-09T11:58:00)
    0000   0x00 0xfa 0x2b 0xa9 0x0f                   ..+..
    body (0)

#### RECORD 58 BasalProfileStart 2015-03-09T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-09T12:00:00)
    0000   0x00 0xc0 0x0c 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 59 CalBGForPH 2015-03-09T12:06:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2015-03-09T12:06:40)
    0000   0x28 0xc6 0x2c 0x69 0x0f                   (.,i.
    body (0)

#### RECORD 60 BGReceived 2015-03-09T12:06:40 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 196, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2015-03-09T12:06:40)
    0000   0x28 0xc6 0x8c 0x69 0x0f                   (..i.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 61 BolusWizard 2015-03-09T12:06:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 196,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.9,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 1.9,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2015-03-09T12:06:49)
    0000   0x31 0xc6 0x0c 0x09 0x0f                   1....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x4c 0x00    .P.P(ZL.
    0008   0x00 0x00 0x00 0x00 0x00 0x4c 0x78         .....Lx
    decimal
              0   80    0   80   40   90   76    0
              0    0    0    0    0   76  120

#### RECORD 62 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 257, 'amount': 5.7}, {'age': 327, 'amount': 2.0}]
```
    op hex (8)
    0000   0x5c 0x08 0xe4 0x01 0x14 0x50 0x47 0x14    \....PG.
    decimal
             92    8  228    1   20   80   71   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2015-03-09T12:06:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9,
 'duration': 0,
 'programmed': 1.9,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x00 0x00    ..L.L...
    decimal
              1    0   76    0   76    0    0    0
    datetime (2015-03-09T12:06:50)
    0000   0x32 0xc6 0x4c 0x09 0x0f                   2.L..
    body (0)

#### RECORD 64 SensorAlert 2015-03-09T12:18:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 196}
```
    op hex (3)
    0000   0x0b 0x65 0xc4                             .e.
    decimal
             11  101  196
    datetime (2015-03-09T12:18:53)
    0000   0x35 0xd2 0x2c 0xa9 0x0f                   5.,..
    body (0)

#### RECORD 65 BolusWizard 2015-03-09T12:19:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.5,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 7.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-09T12:19:36)
    0000   0x24 0xd3 0x0c 0x69 0x0f                   $..i.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 66 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 1.9},
 {'age': 270, 'amount': 5.7},
 {'age': 340, 'amount': 2.0}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0x14 0x04 0xe4 0x0e 0x14    \.L.....
    0008   0x50 0x54 0x14                             PT.
    decimal
             92   11   76   20    4  228   14   20
             80   84   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2015-03-09T12:22:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 180,
 'programmed': 3.5,
 'type': 'square',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x4c 0x06    ......L.
    decimal
              1    0  140    0  140    0   76    6
    datetime (2015-03-09T12:22:18)
    0000   0x12 0xd6 0xac 0x69 0x0f                   ...i.
    body (0)

#### RECORD 68 Bolus 2015-03-09T12:19:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x4c 0x00    ......L.
    decimal
              1    0  160    0  160    0   76    0
    datetime (2015-03-09T12:19:36)
    0000   0x24 0xd3 0x8c 0x69 0x0f                   $..i.
    body (0)

#### RECORD 69 BasalProfileStart 2015-03-09T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-09T15:00:00)
    0000   0x00 0xc0 0x0f 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 70 SensorAlert 2015-03-09T15:24:14 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-09T15:24:14)
    0000   0x0e 0xd8 0x2f 0xa9 0x0f                   ../..
    body (0)

#### RECORD 71 SensorAlert 2015-03-09T15:32:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-03-09T15:32:45)
    0000   0x2d 0xe0 0x2f 0xa9 0x0f                   -./..
    body (0)

#### RECORD 72 LowReservoir 2015-03-09T15:46:52 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-03-09T15:46:52)
    0000   0x34 0xee 0x0f 0x09 0x0f                   4....
    body (0)

#### RECORD 73 SensorAlert 2015-03-09T17:06:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-09T17:06:00)
    0000   0x00 0xc6 0x31 0xa9 0x0f                   ..1..
    body (0)

#### RECORD 74 SensorAlert 2015-03-09T17:19:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-09T17:19:21)
    0000   0x15 0xd3 0x31 0xa9 0x0f                   ..1..
    body (0)

#### RECORD 75 Bolus 2015-03-09T17:20:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x14 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   20    0
    datetime (2015-03-09T17:20:16)
    0000   0x10 0xd4 0x51 0x69 0x0f                   ..Qi.
    body (0)

#### RECORD 76 SensorAlert 2015-03-09T17:24:14 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-09T17:24:14)
    0000   0x0e 0xd8 0x31 0xa9 0x0f                   ..1..
    body (0)

#### RECORD 77 Bolus 2015-03-09T17:46:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x58 0x00    ..x.x.X.
    decimal
              1    0  120    0  120    0   88    0
    datetime (2015-03-09T17:46:15)
    0000   0x0f 0xee 0x51 0x69 0x0f                   ..Qi.
    body (0)

#### RECORD 78 Bolus 2015-03-09T17:56:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 5.1}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xcc 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  204    0
    datetime (2015-03-09T17:56:07)
    0000   0x07 0xf8 0x51 0x69 0x0f                   ..Qi.
    body (0)

#### RECORD 79 SensorAlert 2015-03-09T18:06:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-09T18:06:00)
    0000   0x00 0xc6 0x32 0xa9 0x0f                   ..2..
    body (0)

#### RECORD 80 LowReservoir 2015-03-09T18:16:52 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-03-09T18:16:52)
    0000   0x34 0xd0 0x12 0x09 0x0f                   4....
    body (0)

#### RECORD 81 CalBGForPH 2015-03-09T18:17:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 179}
```
    op hex (2)
    0000   0x0a 0xb3                                  ..
    decimal
             10  179
    datetime (2015-03-09T18:17:36)
    0000   0x24 0xd1 0x32 0x69 0x0f                   $.2i.
    body (0)

#### RECORD 82 BGReceived 2015-03-09T18:17:36 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 179, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-03-09T18:17:36)
    0000   0x24 0xd1 0x72 0x69 0x0f                   $.ri.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 83 Bolus 2015-03-09T18:18:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x01 0x2c 0x00    ..d.d.,.
    decimal
              1    0  100    0  100    1   44    0
    datetime (2015-03-09T18:18:08)
    0000   0x08 0xd2 0x52 0x69 0x0f                   ..Ri.
    body (0)

#### RECORD 84 SensorAlert 2015-03-09T18:33:26 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 193}
```
    op hex (3)
    0000   0x0b 0x65 0xc1                             .e.
    decimal
             11  101  193
    datetime (2015-03-09T18:33:26)
    0000   0x1a 0xe1 0x32 0xa9 0x0f                   ..2..
    body (0)

#### RECORD 85 SensorAlert 2015-03-09T20:52:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-09T20:52:45)
    0000   0x2d 0xf4 0x34 0xa9 0x0f                   -.4..
    body (0)

#### RECORD 86 SensorAlert 2015-03-09T21:19:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-09T21:19:21)
    0000   0x15 0xd3 0x35 0xa9 0x0f                   ..5..
    body (0)

#### RECORD 87 BolusWizard 2015-03-09T21:19:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.5,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 7.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-09T21:19:50)
    0000   0x32 0xd3 0x15 0x69 0x0f                   2..i.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    -P.<(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             45   80    0   60   40   90    0    1
             44    0    0    0    1   44  120

`end ReadHistoryData-page-13.data: 88 records`
