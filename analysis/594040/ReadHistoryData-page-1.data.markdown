## START analysis/594040/logs/ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x84 0xd6                                  ..
##### DEBUG DECIMAL
            132  214
#### RECORD 0 ChangeBasalProfile_new_profile 2015-05-29T17:30:53 head[2], body[145] op[0x09]
###### DECODED
```python
[{'offset': 0, 'rate': 0.9},
 {'offset': 14400000, 'rate': 0.925},
 {'offset': 25200000, 'rate': 0.8500000000000001},
 {'offset': 36000000, 'rate': 0.8500000000000001},
 {'offset': 43200000, 'rate': 0.75},
 {'offset': 54000000, 'rate': 0.8},
 {'offset': 79200000, 'rate': 0.9}]
```
    op hex (2)
    0000   0x09 0x07                                  ..
    decimal
              9    7
    datetime (2015-05-29T17:30:53)
    0000   0x75 0x5e 0x11 0x1d 0x0f                   u^...
    body (145)
    hex
    0000   0x00 0x24 0x00 0x08 0x25 0x00 0x0e 0x22    .$..%.."
    0008   0x00 0x14 0x22 0x00 0x18 0x1e 0x00 0x1e    ..".....
    0010   0x20 0x00 0x2c 0x24 0x00 0x00 0x00 0x00     .,$....
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0038   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0040   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0048   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0050   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0058   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0060   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0068   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0070   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0078   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0080   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0088   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0090   0x00                                       .
    decimal
              0   36    0    8   37    0   14   34
              0   20   34    0   24   30    0   30
             32    0   44   36    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 1 BasalProfileStart 2015-05-29T17:30:53 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-05-29T17:30:53)
    0000   0x75 0x5e 0x11 0x1d 0x0f                   u^...
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 2 ChangeTempBasalType 2015-05-29T17:31:23 head[2], body[0] op[0x62]
###### DECODED
```python
{'temp': 'percent'}
```
    op hex (2)
    0000   0x62 0x01                                  b.
    decimal
             98    1
    datetime (2015-05-29T17:31:23)
    0000   0x57 0x5f 0x11 0x1d 0x0f                   W_...
    body (0)

#### RECORD 3 Rewind 2015-05-29T17:33:27 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-05-29T17:33:27)
    0000   0x5b 0x61 0x11 0x1d 0x0f                   [a...
    body (0)

#### RECORD 4 Prime 2015-05-29T17:34:51 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x00                   .....
    decimal
              3    0    0    0    0
    datetime (2015-05-29T17:34:51)
    0000   0x73 0x62 0x31 0x1d 0x0f                   sb1..
    body (0)

#### RECORD 5 BasalProfileStart 2015-05-29T17:35:33 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-05-29T17:35:33)
    0000   0x61 0x63 0x11 0x1d 0x0f                   ac...
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 6 Prime 2015-05-29T17:35:15 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2015-05-29T17:35:15)
    0000   0x4f 0x63 0x11 0x1d 0x0f                   Oc...
    body (0)

#### RECORD 7 SensorAlert 2015-05-29T17:36:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-05-29T17:36:06)
    0000   0x46 0x64 0x31 0xbd 0x0f                   Fd1..
    body (0)

#### RECORD 8 CalBGForPH 2015-05-29T17:36:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2015-05-29T17:36:30)
    0000   0x5e 0x64 0x31 0x7d 0x0f                   ^d1}.
    body (0)

#### RECORD 9 BGReceived 2015-05-29T17:36:30 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 72, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2015-05-29T17:36:30)
    0000   0x5e 0x64 0x11 0x7d 0x0f                   ^d.}.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 10 SensorAlert 2015-05-29T17:49:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 72}
```
    op hex (3)
    0000   0x0b 0x66 0x48                             .fH
    decimal
             11  102   72
    datetime (2015-05-29T17:49:37)
    0000   0x65 0x71 0x31 0xbd 0x0f                   eq1..
    body (0)

#### RECORD 11 ChangeCaptureEventEnable 2015-05-29T18:00:53 head[2], body[0] op[0x83]

    op hex (2)
    0000   0x83 0x01                                  ..
    decimal
            131    1
    datetime (2015-05-29T18:00:53)
    0000   0x75 0x40 0x12 0x1d 0x0f                   u@...
    body (0)

#### RECORD 12 JournalEntryOtherMarker 2015-05-29T18:01:37 head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0x00                                  C.
    decimal
             67    0
    datetime (2015-05-29T18:01:37)
    0000   0x65 0x41 0x12 0x1d 0x0f                   eA...
    body (0)

#### RECORD 13 JournalEntryMealMarker 2015-05-29T18:02:02 head[2], body[2] op[0x40]
###### DECODED
```python
{'carb_input': 53}
```
    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime (2015-05-29T18:02:02)
    0000   0x42 0x42 0x12 0x1d 0x0f                   BB...
    body (2)
    hex
    0000   0x35 0x01                                  5.
    decimal
             53    1

#### RECORD 14 JournalEntryMealMarker 2015-05-29T18:05:02 head[2], body[2] op[0x40]
###### DECODED
```python
{'carb_input': 23}
```
    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime (2015-05-29T18:05:02)
    0000   0x42 0x45 0x12 0x1d 0x0f                   BE...
    body (2)
    hex
    0000   0x17 0x01                                  ..
    decimal
             23    1

#### RECORD 15 SensorAlert 2015-05-29T18:11:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 85}
```
    op hex (3)
    0000   0x0b 0x66 0x55                             .fU
    decimal
             11  102   85
    datetime (2015-05-29T18:11:04)
    0000   0x44 0x4b 0x32 0xbd 0x0f                   DK2..
    body (0)

#### RECORD 16 JournalEntryMealMarker 2015-05-29T18:59:03 head[2], body[2] op[0x40]
###### DECODED
```python
{'carb_input': 32}
```
    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime (2015-05-29T18:59:03)
    0000   0x43 0x7b 0x12 0x1d 0x0f                   C{...
    body (2)
    hex
    0000   0x20 0x01                                   .
    decimal
             32    1

#### RECORD 17 SensorAlert 2015-05-29T19:45:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-05-29T19:45:43)
    0000   0x6b 0x6d 0x33 0xbd 0x0f                   km3..
    body (0)

#### RECORD 18 BolusWizard 2015-05-29T19:47:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-05-29T19:47:10)
    0000   0x4a 0x6f 0x13 0x7d 0x0f                   Jo.}.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0   60   40   90    0    0
              0    0    0    0    0    0  120

#### RECORD 19 Bolus 2015-05-29T19:47:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x00 0x00    ........
    decimal
              1    0  160    0  160    0    0    0
    datetime (2015-05-29T19:47:10)
    0000   0x4a 0x6f 0x53 0x7d 0x0f                   JoS}.
    body (0)

#### RECORD 20 SensorAlert 2015-05-29T21:14:54 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-05-29T21:14:54)
    0000   0x76 0x4e 0x35 0xbd 0x0f                   vN5..
    body (0)

#### RECORD 21 BolusWizard 2015-05-29T21:15:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.0,
 'carb_input': 42,
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
    datetime (2015-05-29T21:15:20)
    0000   0x54 0x4f 0x15 0x7d 0x0f                   TO.}.
    body (15)
    hex
    0000   0x2a 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    *P.<(Z..
    0008   0x18 0x00 0x00 0x00 0x01 0x18 0x78         ......x
    decimal
             42   80    0   60   40   90    0    1
             24    0    0    0    1   24  120

#### RECORD 22 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 87, 'amount': 2.75}, {'age': 97, 'amount': 1.25}]
```
    op hex (8)
    0000   0x5c 0x08 0x6e 0x57 0x04 0x32 0x61 0x04    \.nW.2a.
    decimal
             92    8  110   87    4   50   97    4
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2015-05-29T21:17:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 120,
 'programmed': 2.5,
 'type': 'square',
 'unabsorbed': 2.6}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x68 0x04    ..d.d.h.
    decimal
              1    0  100    0  100    0  104    4
    datetime (2015-05-29T21:17:49)
    0000   0x71 0x51 0xb5 0x7d 0x0f                   qQ.}.
    body (0)

#### RECORD 24 Bolus 2015-05-29T21:15:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7,
 'duration': 0,
 'programmed': 3.7,
 'type': 'normal',
 'unabsorbed': 2.6}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0x68 0x00    ......h.
    decimal
              1    0  148    0  148    0  104    0
    datetime (2015-05-29T21:15:20)
    0000   0x54 0x4f 0x95 0x7d 0x0f                   TO.}.
    body (0)

#### RECORD 25 BasalProfileStart 2015-05-29T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-05-29T22:00:00)
    0000   0x40 0x40 0x16 0x1d 0x0f                   @@...
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 26 SensorAlert 2015-05-29T22:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-05-29T22:36:00)
    0000   0x40 0x64 0x36 0xbd 0x0f                   @d6..
    body (0)

#### RECORD 27 BolusWizard 2015-05-29T23:02:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.4,
 'carb_input': 44,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.4,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-05-29T23:02:22)
    0000   0x56 0x42 0x17 0x7d 0x0f                   VB.}.
    body (15)
    hex
    0000   0x2c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    ,P.d(Z..
    0008   0xb0 0x00 0x00 0x00 0x00 0xb0 0x78         ......x
    decimal
             44   80    0  100   40   90    0    0
            176    0    0    0    0  176  120

#### RECORD 28 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 0.1},
 {'age': 14, 'amount': 0.2},
 {'age': 24, 'amount': 0.25},
 {'age': 34, 'amount': 0.2},
 {'age': 44, 'amount': 0.2},
 {'age': 54, 'amount': 0.2},
 {'age': 64, 'amount': 0.2},
 {'age': 74, 'amount': 0.2},
 {'age': 84, 'amount': 0.25},
 {'age': 94, 'amount': 0.2},
 {'age': 104, 'amount': 0.2},
 {'age': 114, 'amount': 3.7},
 {'age': 194, 'amount': 2.75},
 {'age': 204, 'amount': 1.25}]
```
    op hex (44)
    0000   0x5c 0x2c 0x04 0x04 0x04 0x08 0x0e 0x04    \,......
    0008   0x0a 0x18 0x04 0x08 0x22 0x04 0x08 0x2c    ...."..,
    0010   0x04 0x08 0x36 0x04 0x08 0x40 0x04 0x08    ..6..@..
    0018   0x4a 0x04 0x0a 0x54 0x04 0x08 0x5e 0x04    J..T..^.
    0020   0x08 0x68 0x04 0x94 0x72 0x04 0x6e 0xc2    .h..r.n.
    0028   0x04 0x32 0xcc 0x04                        .2..
    decimal
             92   44    4    4    4    8   14    4
             10   24    4    8   34    4    8   44
              4    8   54    4    8   64    4    8
             74    4   10   84    4    8   94    4
              8  104    4  148  114    4  110  194
              4   50  204    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2015-05-29T23:02:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4,
 'duration': 0,
 'programmed': 4.4,
 'type': 'normal',
 'unabsorbed': 4.2}
```
    op hex (8)
    0000   0x01 0x00 0xb0 0x00 0xb0 0x00 0xa8 0x00    ........
    decimal
              1    0  176    0  176    0  168    0
    datetime (2015-05-29T23:02:23)
    0000   0x57 0x42 0x57 0x7d 0x0f                   WBW}.
    body (0)

#### RECORD 30 SensorAlert 2015-05-29T23:35:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 83}
```
    op hex (3)
    0000   0x0b 0x66 0x53                             .fS
    decimal
             11  102   83
    datetime (2015-05-29T23:35:52)
    0000   0x74 0x63 0x37 0xbd 0x0f                   tc7..
    body (0)

#### RECORD 31 SensorAlert 2015-05-29T23:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-05-29T23:36:00)
    0000   0x40 0x64 0x37 0xbd 0x0f                   @d7..
    body (0)

#### RECORD 32 CalBGForPH 2015-05-29T23:44:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 52}
```
    op hex (2)
    0000   0x0a 0x34                                  .4
    decimal
             10   52
    datetime (2015-05-29T23:44:30)
    0000   0x5e 0x6c 0x37 0x7d 0x0f                   ^l7}.
    body (0)

#### RECORD 33 BGReceived 2015-05-29T23:44:30 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 52, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2015-05-29T23:44:30)
    0000   0x5e 0x6c 0x97 0x7d 0x0f                   ^l.}.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 34 JournalEntryMealMarker 2015-05-29T23:45:45 head[2], body[2] op[0x40]
###### DECODED
```python
{'carb_input': 44}
```
    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime (2015-05-29T23:45:45)
    0000   0x6d 0x6d 0x17 0x1d 0x0f                   mm...
    body (2)
    hex
    0000   0x2c 0x01                                  ,.
    decimal
             44    1

#### RECORD 35 JournalEntryMealMarker 2015-05-29T23:50:34 head[2], body[2] op[0x40]
###### DECODED
```python
{'carb_input': 20}
```
    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime (2015-05-29T23:50:34)
    0000   0x62 0x72 0x17 0x1d 0x0f                   br...
    body (2)
    hex
    0000   0x14 0x01                                  ..
    decimal
             20    1

#### RECORD 36 BasalProfileStart 2015-05-30T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-05-30T00:00:00)
    0000   0x40 0x40 0x00 0x1e 0x0f                   @@...
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 37 MResultTotals 2015-05-30T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x1a                   .....
    decimal
              7    0    0    4   26
    datetime (2015-05-30T00:00:00)
    0000   0x5d 0x8f                                  ].
    body (3)
    hex
    0000   0x00 0x1d 0x0e                             ...
    decimal
              0   29   14

#### RECORD 38 Sara6E 2015-05-30T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-05-30T00:00:00)
    0000   0x5d 0x8f                                  ].
    body (49)
    hex
    0000   0x05 0x00 0x3e 0x34 0x48 0x02 0x00 0x00    ..>4H...
    0008   0x04 0x1a 0x01 0xd2 0x2c 0x02 0x48 0x38    ....,.H8
    0010   0x01 0x02 0x01 0xa8 0x00 0xa0 0x00 0x00    ........
    0018   0x00 0x00 0x02 0x01 0x00 0x00 0xd0 0x98    ........
    0020   0x1b 0x40 0x09 0x46 0x2e 0x00 0x00 0x00    .@.F....
    0028   0x00 0x03 0x02 0x00 0x40 0x00 0x00 0x00    ....@...
    0030   0x70                                       p
    decimal
              5    0   62   52   72    2    0    0
              4   26    1  210   44    2   72   56
              1    2    1  168    0  160    0    0
              0    0    2    1    0    0  208  152
             27   64    9   70   46    0    0    0
              0    3    2    0   64    0    0    0
            112

#### RECORD 39 SensorAlert 2015-05-30T00:00:16 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 56}
```
    op hex (3)
    0000   0x0b 0x66 0x38                             .f8
    decimal
             11  102   56
    datetime (2015-05-30T00:00:16)
    0000   0x50 0x40 0x20 0xbe 0x0f                   P@ ..
    body (0)

#### RECORD 40 SensorAlert 2015-05-30T00:19:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 48}
```
    op hex (3)
    0000   0x0b 0x66 0x30                             .f0
    decimal
             11  102   48
    datetime (2015-05-30T00:19:35)
    0000   0x63 0x53 0x20 0xbe 0x0f                   cS ..
    body (0)

#### RECORD 41 SensorAlert 2015-05-30T00:40:16 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 53}
```
    op hex (3)
    0000   0x0b 0x66 0x35                             .f5
    decimal
             11  102   53
    datetime (2015-05-30T00:40:16)
    0000   0x50 0x68 0x20 0xbe 0x0f                   Ph ..
    body (0)

#### RECORD 42 SensorAlert 2015-05-30T00:59:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 62}
```
    op hex (3)
    0000   0x0b 0x66 0x3e                             .f>
    decimal
             11  102   62
    datetime (2015-05-30T00:59:35)
    0000   0x63 0x7b 0x20 0xbe 0x0f                   c{ ..
    body (0)

#### RECORD 43 SensorAlert 2015-05-30T01:20:16 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 71}
```
    op hex (3)
    0000   0x0b 0x66 0x47                             .fG
    decimal
             11  102   71
    datetime (2015-05-30T01:20:16)
    0000   0x50 0x54 0x21 0xbe 0x0f                   PT!..
    body (0)

#### RECORD 44 SensorAlert 2015-05-30T01:39:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 75}
```
    op hex (3)
    0000   0x0b 0x66 0x4b                             .fK
    decimal
             11  102   75
    datetime (2015-05-30T01:39:35)
    0000   0x63 0x67 0x21 0xbe 0x0f                   cg!..
    body (0)

#### RECORD 45 SensorAlert 2015-05-30T02:00:16 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 83}
```
    op hex (3)
    0000   0x0b 0x66 0x53                             .fS
    decimal
             11  102   83
    datetime (2015-05-30T02:00:16)
    0000   0x50 0x40 0x22 0xbe 0x0f                   P@"..
    body (0)

#### RECORD 46 BasalProfileStart 2015-05-30T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.925}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-05-30T04:00:00)
    0000   0x40 0x40 0x04 0x1e 0x0f                   @@...
    body (3)
    hex
    0000   0x08 0x25 0x00                             .%.
    decimal
              8   37    0

#### RECORD 47 SensorAlert 2015-05-30T04:19:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-05-30T04:19:35)
    0000   0x63 0x53 0x24 0xbe 0x0f                   cS$..
    body (0)

#### RECORD 48 SensorAlert 2015-05-30T05:49:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 245}
```
    op hex (3)
    0000   0x0b 0x65 0xf5                             .e.
    decimal
             11  101  245
    datetime (2015-05-30T05:49:37)
    0000   0x65 0x71 0x25 0xbe 0x0f                   eq%..
    body (0)

#### RECORD 49 CalBGForPH 2015-05-30T06:05:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 358}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2015-05-30T06:05:36)
    0000   0x64 0x45 0x26 0x7e 0x8f                   dE&~.
    body (0)

#### RECORD 50 BGReceived 2015-05-30T06:05:36 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 358, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2c                                  ?,
    decimal
             63   44
    datetime (2015-05-30T06:05:36)
    0000   0x64 0x45 0xc6 0x7e 0x0f                   dE.~.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 51 BolusWizard 2015-05-30T06:05:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 358,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.9,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 5.9,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2015-05-30T06:05:51)
    0000   0x73 0x45 0x06 0x1e 0x0f                   sE...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xec 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0xec 0x78         ......x
    decimal
              0   81    0  100   40   90  236    0
              0    0    0    0    0  236  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 417, 'amount': 0.2},
 {'age': 427, 'amount': 4.6},
 {'age': 437, 'amount': 0.2},
 {'age': 447, 'amount': 0.25},
 {'age': 457, 'amount': 0.2},
 {'age': 467, 'amount': 0.2},
 {'age': 477, 'amount': 0.2}]
```
    op hex (23)
    0000   0x5c 0x17 0x08 0xa1 0x14 0xb8 0xab 0x14    \.......
    0008   0x08 0xb5 0x14 0x0a 0xbf 0x14 0x08 0xc9    ........
    0010   0x14 0x08 0xd3 0x14 0x08 0xdd 0x14         .......
    decimal
             92   23    8  161   20  184  171   20
              8  181   20   10  191   20    8  201
             20    8  211   20    8  221   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2015-05-30T06:05:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    decimal
              1    0    0    0    0    0    0    0
    datetime (2015-05-30T06:05:51)
    0000   0x73 0x45 0xa6 0x1e 0x0f                   sE...
    body (0)

#### RECORD 54 Bolus 2015-05-30T06:05:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.9,
 'duration': 0,
 'programmed': 5.9,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xec 0x00 0xec 0x00 0x00 0x00    ........
    decimal
              1    0  236    0  236    0    0    0
    datetime (2015-05-30T06:05:52)
    0000   0x74 0x45 0x86 0x1e 0x0f                   tE...
    body (0)

#### RECORD 55 BasalProfileStart 2015-05-30T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-05-30T07:00:00)
    0000   0x40 0x40 0x07 0x1e 0x0f                   @@...
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 56 SensorAlert 2015-05-30T07:20:16 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 203}
```
    op hex (3)
    0000   0x0b 0x65 0xcb                             .e.
    decimal
             11  101  203
    datetime (2015-05-30T07:20:16)
    0000   0x50 0x54 0x27 0xbe 0x0f                   PT'..
    body (0)

#### RECORD 57 BasalProfileStart 2015-05-30T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-05-30T10:00:00)
    0000   0x40 0x40 0x0a 0x1e 0x0f                   @@...
    body (3)
    hex
    0000   0x14 0x22 0x00                             .".
    decimal
             20   34    0

#### RECORD 58 SensorAlert 2015-05-30T10:44:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-05-30T10:44:00)
    0000   0x40 0x6c 0x2a 0xbe 0x0f                   @l*..
    body (0)

#### RECORD 59 CalBGForPH 2015-05-30T10:52:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2015-05-30T10:52:08)
    0000   0x48 0x74 0x2a 0x7e 0x0f                   Ht*~.
    body (0)

#### RECORD 60 BGReceived 2015-05-30T10:52:08 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 196, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2015-05-30T10:52:08)
    0000   0x48 0x74 0x8a 0x7e 0x0f                   Ht.~.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 61 BolusWizard 2015-05-30T10:52:23 head[2], body[15] op[0x5b]
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
    datetime (2015-05-30T10:52:23)
    0000   0x57 0x74 0x0a 0x1e 0x0f                   Wt...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x4c 0x00    .P.d(ZL.
    0008   0x00 0x00 0x00 0x00 0x00 0x4c 0x78         .....Lx
    decimal
              0   80    0  100   40   90   76    0
              0    0    0    0    0   76  120

#### RECORD 62 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 284, 'amount': 2.75}, {'age': 294, 'amount': 3.15}]
```
    op hex (8)
    0000   0x5c 0x08 0x6e 0x1c 0x14 0x7e 0x26 0x14    \.n..~&.
    decimal
             92    8  110   28   20  126   38   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2015-05-30T10:52:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    decimal
              1    0    0    0    0    0    0    0
    datetime (2015-05-30T10:52:23)
    0000   0x57 0x74 0xaa 0x1e 0x0f                   Wt...
    body (0)

#### RECORD 64 Bolus 2015-05-30T10:52:23 head[8], body[0] op[0x01]
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
    datetime (2015-05-30T10:52:23)
    0000   0x57 0x74 0x8a 0x1e 0x0f                   Wt...
    body (0)

#### RECORD 65 SensorAlert 2015-05-30T11:05:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 193}
```
    op hex (3)
    0000   0x0b 0x65 0xc1                             .e.
    decimal
             11  101  193
    datetime (2015-05-30T11:05:43)
    0000   0x6b 0x45 0x2b 0xbe 0x0f                   kE+..
    body (0)

#### RECORD 66 BolusWizard 2015-05-30T11:06:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.4,
 'carb_input': 44,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.4,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-05-30T11:06:20)
    0000   0x54 0x46 0x0b 0x7e 0x0f                   TF.~.
    body (15)
    hex
    0000   0x2c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    ,P.d(Z..
    0008   0xb0 0x00 0x00 0x00 0x00 0xb0 0x78         ......x
    decimal
             44   80    0  100   40   90    0    0
            176    0    0    0    0  176  120

#### RECORD 67 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 1.9},
 {'age': 298, 'amount': 2.75},
 {'age': 308, 'amount': 3.15}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0x12 0x04 0x6e 0x2a 0x14    \.L..n*.
    0008   0x7e 0x34 0x14                             ~4.
    decimal
             92   11   76   18    4  110   42   20
            126   52   20
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2015-05-30T11:06:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4,
 'duration': 0,
 'programmed': 4.4,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0xb0 0x00 0xb0 0x00 0x4c 0x00    ......L.
    decimal
              1    0  176    0  176    0   76    0
    datetime (2015-05-30T11:06:20)
    0000   0x54 0x46 0x4b 0x7e 0x0f                   TFK~.
    body (0)

#### RECORD 69 BasalProfileStart 2015-05-30T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-05-30T12:00:00)
    0000   0x40 0x40 0x0c 0x1e 0x0f                   @@...
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 70 BolusWizard 2015-05-30T12:40:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.8,
 'carb_input': 31,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-05-30T12:40:11)
    0000   0x4b 0x68 0x0c 0x7e 0x0f                   Kh.~.
    body (15)
    hex
    0000   0x1f 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x98 0x00 0x00 0x00 0x00 0x98 0x78         ......x
    decimal
             31   80    0   80   40   90    0    0
            152    0    0    0    0  152  120

#### RECORD 71 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 1.95},
 {'age': 102, 'amount': 2.45},
 {'age': 112, 'amount': 1.9},
 {'age': 392, 'amount': 2.75},
 {'age': 402, 'amount': 3.15}]
```
    op hex (17)
    0000   0x5c 0x11 0x4e 0x5c 0x04 0x62 0x66 0x04    \.N\.bf.
    0008   0x4c 0x70 0x04 0x6e 0x88 0x14 0x7e 0x92    Lp.n..~.
    0010   0x14                                       .
    decimal
             92   17   78   92    4   98  102    4
             76  112    4  110  136   20  126  146
             20
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2015-05-30T12:40:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8,
 'duration': 0,
 'programmed': 3.8,
 'type': 'normal',
 'unabsorbed': 3.7}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x94 0x00    ........
    decimal
              1    0  152    0  152    0  148    0
    datetime (2015-05-30T12:40:12)
    0000   0x4c 0x68 0x4c 0x7e 0x0f                   LhL~.
    body (0)

#### RECORD 73 BasalProfileStart 2015-05-30T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-05-30T15:00:00)
    0000   0x40 0x40 0x0f 0x1e 0x0f                   @@...
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

`end analysis/594040/logs/ReadHistoryData-page-1.data: 74 records`
