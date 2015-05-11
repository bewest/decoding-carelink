## START ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc6 0x84                                  ..
##### DEBUG DECIMAL
            198  132
#### RECORD 0 Bolus 2015-02-06T19:46:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 90,
 'programmed': 3.0,
 'type': 'square',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x5c 0x03    ..x.x.\.
    decimal
              1    0  120    0  120    0   92    3
    datetime (2015-02-06T19:46:18)
    0000   0x12 0xae 0xb3 0x66 0x0f                   ...f.
    body (0)

#### RECORD 1 Bolus 2015-02-06T19:43:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3,
 'duration': 0,
 'programmed': 4.3,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0x5c 0x00    ......\.
    decimal
              1    0  172    0  172    0   92    0
    datetime (2015-02-06T19:43:26)
    0000   0x1a 0xab 0x93 0x66 0x0f                   ...f.
    body (0)

#### RECORD 2 BolusWizard 2015-02-06T20:12:16 head[2], body[15] op[0x5b]
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
    datetime (2015-02-06T20:12:16)
    0000   0x10 0x8c 0x14 0x66 0x0f                   ...f.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    (P.<(Z..
    0008   0x08 0x00 0x00 0x00 0x01 0x08 0x78         ......x
    decimal
             40   80    0   60   40   90    0    1
              8    0    0    0    1    8  120

#### RECORD 3 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 0.2},
 {'age': 16, 'amount': 0.35},
 {'age': 26, 'amount': 0.8},
 {'age': 36, 'amount': 3.8},
 {'age': 46, 'amount': 2.0},
 {'age': 236, 'amount': 2.45},
 {'age': 246, 'amount': 0.55},
 {'age': 276, 'amount': 0.15},
 {'age': 286, 'amount': 2.85}]
```
    op hex (29)
    0000   0x5c 0x1d 0x08 0x06 0x04 0x0e 0x10 0x04    \.......
    0008   0x20 0x1a 0x04 0x98 0x24 0x04 0x50 0x2e     ...$.P.
    0010   0x04 0x62 0xec 0x04 0x16 0xf6 0x04 0x06    .b......
    0018   0x14 0x14 0x72 0x1e 0x14                   ..r..
    decimal
             92   29    8    6    4   14   16    4
             32   26    4  152   36    4   80   46
              4   98  236    4   22  246    4    6
             20   20  114   30   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2015-02-06T20:12:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2,
 'duration': 0,
 'programmed': 5.2,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0xd0 0x00 0xd0 0x01 0x10 0x00    ........
    decimal
              1    0  208    0  208    1   16    0
    datetime (2015-02-06T20:12:16)
    0000   0x10 0x8c 0x54 0x66 0x0f                   ..Tf.
    body (0)

#### RECORD 5 BasalProfileStart 2015-02-06T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-06T22:00:00)
    0000   0x00 0x80 0x16 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 6 BolusWizard 2015-02-06T23:34:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.6,
 'carb_input': 56,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-06T23:34:43)
    0000   0x2b 0xa2 0x17 0x66 0x0f                   +..f.
    body (15)
    hex
    0000   0x38 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    8P.d(Z..
    0008   0xe0 0x00 0x00 0x00 0x00 0xe0 0x78         ......x
    decimal
             56   80    0  100   40   90    0    0
            224    0    0    0    0  224  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[47], body[0] op[0x5c]
###### DECODED
```python
[{'age': 138, 'amount': 0.1},
 {'age': 148, 'amount': 0.35},
 {'age': 158, 'amount': 0.35},
 {'age': 168, 'amount': 0.3},
 {'age': 178, 'amount': 0.35},
 {'age': 188, 'amount': 0.35},
 {'age': 198, 'amount': 0.3},
 {'age': 208, 'amount': 5.45},
 {'age': 218, 'amount': 0.35},
 {'age': 228, 'amount': 0.8},
 {'age': 238, 'amount': 3.8},
 {'age': 248, 'amount': 2.0},
 {'age': 438, 'amount': 2.45},
 {'age': 448, 'amount': 0.55},
 {'age': 478, 'amount': 0.15}]
```
    op hex (47)
    0000   0x5c 0x2f 0x04 0x8a 0x04 0x0e 0x94 0x04    \/......
    0008   0x0e 0x9e 0x04 0x0c 0xa8 0x04 0x0e 0xb2    ........
    0010   0x04 0x0e 0xbc 0x04 0x0c 0xc6 0x04 0xda    ........
    0018   0xd0 0x04 0x0e 0xda 0x04 0x20 0xe4 0x04    ..... ..
    0020   0x98 0xee 0x04 0x50 0xf8 0x04 0x62 0xb6    ...P..b.
    0028   0x14 0x16 0xc0 0x14 0x06 0xde 0x14         .......
    decimal
             92   47    4  138    4   14  148    4
             14  158    4   12  168    4   14  178
              4   14  188    4   12  198    4  218
            208    4   14  218    4   32  228    4
            152  238    4   80  248    4   98  182
             20   22  192   20    6  222   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2015-02-06T23:34:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6,
 'duration': 0,
 'programmed': 5.6,
 'type': 'normal',
 'unabsorbed': 1.3}
```
    op hex (8)
    0000   0x01 0x00 0xe0 0x00 0xe0 0x00 0x34 0x00    ......4.
    decimal
              1    0  224    0  224    0   52    0
    datetime (2015-02-06T23:34:43)
    0000   0x2b 0xa2 0x57 0x66 0x0f                   +.Wf.
    body (0)

#### RECORD 9 TempBasal 2015-02-06T23:39:06 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 125, 'temp': 'percent'}
```
    op hex (2)
    0000   0x33 0x7d                                  3}
    decimal
             51  125
    datetime (2015-02-06T23:39:06)
    0000   0x06 0xa7 0x17 0x06 0x0f                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 10 TempBasalDuration 2015-02-06T23:39:06 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 360}
```
    op hex (2)
    0000   0x16 0x0c                                  ..
    decimal
             22   12
    datetime (2015-02-06T23:39:06)
    0000   0x06 0xa7 0x17 0x06 0x0f                   .....
    body (0)

#### RECORD 11 SensorAlert 2015-02-06T23:45:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-06T23:45:53)
    0000   0x35 0xad 0x37 0xa6 0x0f                   5.7..
    body (0)

#### RECORD 12 SensorAlert 2015-02-06T23:56:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 187}
```
    op hex (3)
    0000   0x0b 0x65 0xbb                             .e.
    decimal
             11  101  187
    datetime (2015-02-06T23:56:41)
    0000   0x29 0xb8 0x37 0xa6 0x0f                   ).7..
    body (0)

#### RECORD 13 MResultTotals 2015-02-07T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0xea                   .....
    decimal
              7    0    0   10  234
    datetime (2015-02-07T00:00:00)
    0000   0x26 0x0f                                  &.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 14 Sara6E 2015-02-07T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-07T00:00:00)
    0000   0x26 0x0f                                  &.
    body (49)
    hex
    0000   0x05 0x00 0xa3 0x58 0xed 0x02 0x00 0x00    ...X....
    0008   0x0a 0xea 0x03 0x22 0x1d 0x07 0xc8 0x47    ..."...G
    0010   0x00 0xe1 0x04 0x50 0x01 0x84 0x00 0x00    ...P....
    0018   0x01 0xf4 0x05 0x02 0x00 0x05 0x00 0xb8    ........
    0020   0x2b 0x38 0x01 0x20 0x4e 0x05 0x02 0x00    +8. N...
    0028   0x00 0x01 0x07 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  163   88  237    2    0    0
             10  234    3   34   29    7  200   71
              0  225    4   80    1  132    0    0
              1  244    5    2    0    5    0  184
             43   56    1   32   78    5    2    0
              0    1    7    1    0    0    0    0
              0

#### RECORD 15 SensorAlert 2015-02-07T01:25:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-07T01:25:12)
    0000   0x0c 0x99 0x21 0xa7 0x0f                   ..!..
    body (0)

#### RECORD 16 SensorAlert 2015-02-07T01:31:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-07T01:31:20)
    0000   0x14 0x9f 0x21 0xa7 0x0f                   ..!..
    body (0)

#### RECORD 17 CalBGForPH 2015-02-07T04:11:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 351}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2015-02-07T04:11:54)
    0000   0x36 0x8b 0x24 0x67 0x8f                   6.$g.
    body (0)

#### RECORD 18 BGReceived 2015-02-07T04:11:54 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 351, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2b                                  ?+
    decimal
             63   43
    datetime (2015-02-07T04:11:54)
    0000   0x36 0x8b 0xe4 0x67 0x0f                   6..g.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 19 BolusWizard 2015-02-07T04:12:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 351,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.7,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 5.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2015-02-07T04:12:06)
    0000   0x06 0x8c 0x04 0x07 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xe4 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0xe4 0x78         ......x
    decimal
              0   81    0  100   40   90  228    0
              0    0    0    0    0  228  120

#### RECORD 20 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 276, 'amount': 3.7},
 {'age': 286, 'amount': 1.9},
 {'age': 416, 'amount': 0.1},
 {'age': 426, 'amount': 0.35},
 {'age': 436, 'amount': 0.35},
 {'age': 446, 'amount': 0.3},
 {'age': 456, 'amount': 0.35},
 {'age': 466, 'amount': 0.35},
 {'age': 476, 'amount': 0.3}]
```
    op hex (29)
    0000   0x5c 0x1d 0x94 0x14 0x14 0x4c 0x1e 0x14    \....L..
    0008   0x04 0xa0 0x14 0x0e 0xaa 0x14 0x0e 0xb4    ........
    0010   0x14 0x0c 0xbe 0x14 0x0e 0xc8 0x14 0x0e    ........
    0018   0xd2 0x14 0x0c 0xdc 0x14                   .....
    decimal
             92   29  148   20   20   76   30   20
              4  160   20   14  170   20   14  180
             20   12  190   20   14  200   20   14
            210   20   12  220   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2015-02-07T04:12:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9,
 'duration': 0,
 'programmed': 1.9,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x4c 0x01 0x4c 0x00 0x00 0x00    ..L.L...
    decimal
              1    1   76    1   76    0    0    0
    datetime (2015-02-07T04:12:06)
    0000   0x06 0x8c 0x44 0x07 0x0f                   ..D..
    body (0)

#### RECORD 22 SensorAlert 2015-02-07T04:31:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 352}
```
    op hex (3)
    0000   0x0b 0x65 0x60                             .e`
    decimal
             11  101   96
    datetime (2015-02-07T04:31:48)
    0000   0x30 0x9f 0x24 0xa7 0x8f                   0.$..
    body (0)

#### RECORD 23 BasalProfileStart 2015-02-07T05:39:06 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-07T05:39:06)
    0000   0x06 0xa7 0x05 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 24 SensorAlert 2015-02-07T06:01:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 304}
```
    op hex (3)
    0000   0x0b 0x65 0x30                             .e0
    decimal
             11  101   48
    datetime (2015-02-07T06:01:29)
    0000   0x1d 0x81 0x26 0xa7 0x8f                   ..&..
    body (0)

#### RECORD 25 BasalProfileStart 2015-02-07T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-07T07:00:00)
    0000   0x00 0x80 0x07 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 26 SensorAlert 2015-02-07T07:31:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 298}
```
    op hex (3)
    0000   0x0b 0x65 0x2a                             .e*
    decimal
             11  101   42
    datetime (2015-02-07T07:31:20)
    0000   0x14 0x9f 0x27 0xa7 0x8f                   ..'..
    body (0)

#### RECORD 27 Bolus 2015-02-07T07:35:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0x24 0x00    ......$.
    decimal
              1    0  240    0  240    0   36    0
    datetime (2015-02-07T07:35:39)
    0000   0x27 0xa3 0x47 0x67 0x0f                   '.Gg.
    body (0)

#### RECORD 28 CalBGForPH 2015-02-07T09:50:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2015-02-07T09:50:24)
    0000   0x18 0xb2 0x29 0x67 0x0f                   ..)g.
    body (0)

#### RECORD 29 BGReceived 2015-02-07T09:50:24 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 181, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-02-07T09:50:24)
    0000   0x18 0xb2 0xa9 0x67 0x0f                   ...g.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 30 BasalProfileStart 2015-02-07T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-07T10:00:00)
    0000   0x00 0x80 0x0a 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 31 SensorAlert 2015-02-07T10:41:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-07T10:41:29)
    0000   0x1d 0xa9 0x2a 0xa7 0x0f                   ..*..
    body (0)

#### RECORD 32 SensorAlert 2015-02-07T11:05:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-07T11:05:53)
    0000   0x35 0x85 0x2b 0xa7 0x0f                   5.+..
    body (0)

#### RECORD 33 BasalProfileStart 2015-02-07T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-07T12:00:00)
    0000   0x00 0x80 0x0c 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 34 SensorAlert 2015-02-07T12:36:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 270}
```
    op hex (3)
    0000   0x0b 0x65 0x0e                             .e.
    decimal
             11  101   14
    datetime (2015-02-07T12:36:41)
    0000   0x29 0xa4 0x2c 0xa7 0x8f                   ).,..
    body (0)

#### RECORD 35 Bolus 2015-02-07T12:38:17 head[8], body[0] op[0x01]
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
    datetime (2015-02-07T12:38:17)
    0000   0x11 0xa6 0x4c 0x67 0x0f                   ..Lg.
    body (0)

#### RECORD 36 SensorAlert 2015-02-07T14:31:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-07T14:31:48)
    0000   0x30 0x9f 0x2e 0xa7 0x0f                   0....
    body (0)

#### RECORD 37 SensorAlert 2015-02-07T14:45:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-07T14:45:12)
    0000   0x0c 0xad 0x2e 0xa7 0x0f                   .....
    body (0)

#### RECORD 38 Bolus 2015-02-07T14:46:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x40 0x00    ..<.<.@.
    decimal
              1    0   60    0   60    0   64    0
    datetime (2015-02-07T14:46:17)
    0000   0x11 0xae 0x4e 0x67 0x0f                   ..Ng.
    body (0)

#### RECORD 39 BasalProfileStart 2015-02-07T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-07T15:00:00)
    0000   0x00 0x80 0x0f 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 40 SensorAlert 2015-02-07T15:11:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-07T15:11:00)
    0000   0x00 0x8b 0x2f 0xa7 0x0f                   ../..
    body (0)

#### RECORD 41 SensorAlert 2015-02-07T16:11:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-07T16:11:00)
    0000   0x00 0x8b 0x30 0xa7 0x0f                   ..0..
    body (0)

#### RECORD 42 SensorAlert 2015-02-07T16:41:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-07T16:41:00)
    0000   0x00 0xa9 0x30 0xa7 0x0f                   ..0..
    body (0)

#### RECORD 43 CalBGForPH 2015-02-07T16:45:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 368}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2015-02-07T16:45:14)
    0000   0x0e 0xad 0x30 0x67 0x8f                   ..0g.
    body (0)

#### RECORD 44 BGReceived 2015-02-07T16:45:14 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 368, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2e                                  ?.
    decimal
             63   46
    datetime (2015-02-07T16:45:14)
    0000   0x0e 0xad 0x10 0x67 0x0f                   ...g.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 45 BolusWizard 2015-02-07T16:45:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 368,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.0,
 'carb_input': 12,
 'carb_ratio': 8.1,
 'correction_estimate': 6.2,
 'food_estimate': 1.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.7}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2015-02-07T16:45:40)
    0000   0x28 0xad 0x10 0x07 0x0f                   (....
    body (15)
    hex
    0000   0x0c 0x51 0x00 0x50 0x28 0x5a 0xf8 0x00    .Q.P(Z..
    0008   0x3c 0x00 0x00 0x1c 0x01 0x18 0x78         <.....x
    decimal
             12   81    0   80   40   90  248    0
             60    0    0   28    1   24  120

#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 119, 'amount': 1.5}, {'age': 249, 'amount': 4.0}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x77 0x04 0xa0 0xf9 0x04    \.<w....
    decimal
             92    8   60  119    4  160  249    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2015-02-07T16:45:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6,
 'duration': 0,
 'programmed': 0.6,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x1c 0x00    ........
    decimal
              1    1   24    1   24    0   28    0
    datetime (2015-02-07T16:45:40)
    0000   0x28 0xad 0x50 0x07 0x0f                   (.P..
    body (0)

#### RECORD 48 SensorAlert 2015-02-07T17:00:31 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 365}
```
    op hex (3)
    0000   0x0b 0x65 0x6d                             .em
    decimal
             11  101  109
    datetime (2015-02-07T17:00:31)
    0000   0x1f 0x80 0x31 0xa7 0x8f                   ..1..
    body (0)

#### RECORD 49 BolusWizard 2015-02-07T17:16:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.2,
 'carb_input': 50,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-07T17:16:23)
    0000   0x17 0x90 0x11 0x67 0x0f                   ...g.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    2P.P(Z..
    0008   0xf8 0x00 0x00 0x00 0x00 0xf8 0x78         ......x
    decimal
             50   80    0   80   40   90    0    0
            248    0    0    0    0  248  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 0.1},
 {'age': 40, 'amount': 0.5},
 {'age': 150, 'amount': 1.5},
 {'age': 280, 'amount': 4.0}]
```
    op hex (14)
    0000   0x5c 0x0e 0x04 0x1e 0x05 0x14 0x28 0x04    \.....(.
    0008   0x3c 0x96 0x04 0xa0 0x18 0x14              <.....
    decimal
             92   14    4   30    5   20   40    4
             60  150    4  160   24   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2015-02-07T17:18:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.15,
 'duration': 90,
 'programmed': 2.7,
 'type': 'square',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x56 0x01 0x1c 0x03    ..l.V...
    decimal
              1    0  108    0   86    1   28    3
    datetime (2015-02-07T17:18:43)
    0000   0x2b 0x92 0xb1 0x67 0x0f                   +..g.
    body (0)

#### RECORD 52 Bolus 2015-02-07T17:16:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x01 0x1c 0x00    ........
    decimal
              1    0  140    0  140    1   28    0
    datetime (2015-02-07T17:16:23)
    0000   0x17 0x90 0x91 0x67 0x0f                   ...g.
    body (0)

#### RECORD 53 BolusWizard 2015-02-07T17:56:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.7,
 'carb_input': 30,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-07T17:56:22)
    0000   0x16 0xb8 0x11 0x67 0x0f                   ...g.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x94 0x00 0x00 0x00 0x00 0x94 0x78         ......x
    decimal
             30   80    0   80   40   90    0    0
            148    0    0    0    0  148  120

#### RECORD 54 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 0.05},
 {'age': 10, 'amount': 0.3},
 {'age': 20, 'amount': 0.3},
 {'age': 30, 'amount': 0.3},
 {'age': 40, 'amount': 3.7},
 {'age': 70, 'amount': 0.1},
 {'age': 80, 'amount': 0.5},
 {'age': 190, 'amount': 1.5},
 {'age': 320, 'amount': 4.0}]
```
    op hex (29)
    0000   0x5c 0x1d 0x02 0x00 0x04 0x0c 0x0a 0x04    \.......
    0008   0x0c 0x14 0x04 0x0c 0x1e 0x04 0x94 0x28    .......(
    0010   0x04 0x04 0x46 0x05 0x14 0x50 0x04 0x3c    ..F..P.<
    0018   0xbe 0x04 0xa0 0x40 0x14                   ...@.
    decimal
             92   29    2    0    4   12   10    4
             12   20    4   12   30    4  148   40
              4    4   70    5   20   80    4   60
            190    4  160   64   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2015-02-07T17:56:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6,
 'duration': 0,
 'programmed': 4.6,
 'type': 'normal',
 'unabsorbed': 3.5}
```
    op hex (8)
    0000   0x01 0x00 0xb8 0x00 0xb8 0x01 0x8c 0x00    ........
    decimal
              1    0  184    0  184    1  140    0
    datetime (2015-02-07T17:56:22)
    0000   0x16 0xb8 0x51 0x67 0x0f                   ..Qg.
    body (0)

#### RECORD 56 PumpSuspend 2015-02-07T18:31:40 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-07T18:31:40)
    0000   0x28 0x9f 0x12 0x07 0x0f                   (....
    body (0)

#### RECORD 57 SensorAlert 2015-02-07T18:31:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 248}
```
    op hex (3)
    0000   0x0b 0x65 0xf8                             .e.
    decimal
             11  101  248
    datetime (2015-02-07T18:31:48)
    0000   0x30 0x9f 0x32 0xa7 0x0f                   0.2..
    body (0)

#### RECORD 58 BasalProfileStart 2015-02-07T18:59:25 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-07T18:59:25)
    0000   0x19 0xbb 0x12 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 59 PumpResume 2015-02-07T18:59:25 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-07T18:59:25)
    0000   0x19 0xbb 0x12 0x07 0x0f                   .....
    body (0)

#### RECORD 60 SensorAlert 2015-02-07T20:31:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-07T20:31:48)
    0000   0x30 0x9f 0x34 0xa7 0x0f                   0.4..
    body (0)

#### RECORD 61 SensorAlert 2015-02-07T20:41:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-07T20:41:29)
    0000   0x1d 0xa9 0x34 0xa7 0x0f                   ..4..
    body (0)

#### RECORD 62 BasalProfileStart 2015-02-07T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-07T22:00:00)
    0000   0x00 0x80 0x16 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 63 SensorAlert 2015-02-07T22:11:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 288}
```
    op hex (3)
    0000   0x0b 0x65 0x20                             .e 
    decimal
             11  101   32
    datetime (2015-02-07T22:11:20)
    0000   0x14 0x8b 0x36 0xa7 0x8f                   ..6..
    body (0)

#### RECORD 64 Bolus 2015-02-07T23:07:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x00 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    0    0
    datetime (2015-02-07T23:07:39)
    0000   0x27 0x87 0x57 0x67 0x0f                   '.Wg.
    body (0)

#### RECORD 65 SensorAlert 2015-02-07T23:40:31 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 402}
```
    op hex (3)
    0000   0x0b 0x65 0x92                             .e.
    decimal
             11  101  146
    datetime (2015-02-07T23:40:31)
    0000   0x1f 0xa8 0x37 0xa7 0x8f                   ..7..
    body (0)

#### RECORD 66 Bolus 2015-02-07T23:53:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6,
 'duration': 0,
 'programmed': 1.6,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x01 0x40 0x01 0x40 0x00 0x58 0x00    ..@.@.X.
    decimal
              1    1   64    1   64    0   88    0
    datetime (2015-02-07T23:53:59)
    0000   0x3b 0xb5 0x57 0x67 0x0f                   ;.Wg.
    body (0)

#### RECORD 67 BasalProfileStart 2015-02-08T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-08T00:00:00)
    0000   0x00 0x80 0x00 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 68 MResultTotals 2015-02-08T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0xbc                   .....
    decimal
              7    0    0   10  188
    datetime (2015-02-08T00:00:00)
    0000   0x27 0x0f                                  '.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 69 Sara6E 2015-02-08T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-08T00:00:00)
    0000   0x27 0x0f                                  '.
    body (49)
    hex
    0000   0x05 0x11 0x2c 0xb5 0x70 0x03 0x00 0x00    ..,.p...
    0008   0x0a 0xbc 0x03 0x4e 0x1f 0x07 0x6e 0x45    ...N..nE
    0010   0x00 0x5c 0x00 0xe2 0x01 0x4c 0x01 0xd0    .\...L..
    0018   0x03 0x70 0x01 0x01 0x02 0x05 0x00 0xf8    .p......
    0020   0x4d 0x17 0x00 0x16 0x48 0x04 0x00 0x00    M...H...
    0028   0x00 0x00 0x0c 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   17   44  181  112    3    0    0
             10  188    3   78   31    7  110   69
              0   92    0  226    1   76    1  208
              3  112    1    1    2    5    0  248
             77   23    0   22   72    4    0    0
              0    0   12    1    0    0    0    0
              0

#### RECORD 70 Bolus 2015-02-08T00:22:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 3.1}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x01 0x7c 0x00    ..x.x.|.
    decimal
              1    0  120    0  120    1  124    0
    datetime (2015-02-08T00:22:53)
    0000   0x35 0x96 0x40 0x68 0x0f                   5.@h.
    body (0)

#### RECORD 71 LowReservoir 2015-02-08T00:43:24 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-02-08T00:43:24)
    0000   0x18 0xab 0x00 0x08 0x0f                   .....
    body (0)

#### RECORD 72 Bolus 2015-02-08T00:43:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 4.9}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x01 0xc4 0x00    ........
    decimal
              1    0  160    0  160    1  196    0
    datetime (2015-02-08T00:43:18)
    0000   0x12 0xab 0x40 0x68 0x0f                   ..@h.
    body (0)

#### RECORD 73 SensorAlert 2015-02-08T01:11:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 389}
```
    op hex (3)
    0000   0x0b 0x65 0x85                             .e.
    decimal
             11  101  133
    datetime (2015-02-08T01:11:48)
    0000   0x30 0x8b 0x21 0xa8 0x8f                   0.!..
    body (0)

#### RECORD 74 CalBGForPH 2015-02-08T02:27:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2015-02-08T02:27:42)
    0000   0x2a 0x9b 0x22 0x68 0x0f                   *."h.
    body (0)

#### RECORD 75 BGReceived 2015-02-08T02:27:42 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 89, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2015-02-08T02:27:42)
    0000   0x2a 0x9b 0x22 0x68 0x0f                   *."h.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 76 SensorAlert 2015-02-08T02:45:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose Predicted', 'alarm_type': 115}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-08T02:45:12)
    0000   0x0c 0xad 0x22 0xa8 0x0f                   .."..
    body (0)

#### RECORD 77 SensorAlert 2015-02-08T03:00:31 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 76}
```
    op hex (3)
    0000   0x0b 0x66 0x4c                             .fL
    decimal
             11  102   76
    datetime (2015-02-08T03:00:31)
    0000   0x1f 0x80 0x23 0xa8 0x0f                   ..#..
    body (0)

#### RECORD 78 BasalProfileStart 2015-02-08T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-08T04:00:00)
    0000   0x00 0x80 0x04 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

`end ReadHistoryData-page-35.data: 79 records`
