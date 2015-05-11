## START ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xf8 0x74                                  .t
##### DEBUG DECIMAL
            248  116
#### RECORD 0 BGReceived 2015-02-19T17:48:45 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 190, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-02-19T17:48:45)
    0000   0x2d 0xb0 0xd1 0x73 0x0f                   -..s.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 1 BolusWizard 2015-02-19T17:49:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 190,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.4,
 'carb_input': 30,
 'carb_ratio': 8.0,
 'correction_estimate': 1.7,
 'food_estimate': 3.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2015-02-19T17:49:10)
    0000   0x0a 0xb1 0x11 0x73 0x0f                   ...s.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x50 0x28 0x5a 0x44 0x00    .P.P(ZD.
    0008   0x94 0x00 0x00 0x00 0x00 0xd8 0x78         ......x
    decimal
             30   80    0   80   40   90   68    0
            148    0    0    0    0  216  120

#### RECORD 2 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 243, 'amount': 0.1},
 {'age': 253, 'amount': 0.9},
 {'age': 263, 'amount': 0.85},
 {'age': 273, 'amount': 2.8},
 {'age': 283, 'amount': 0.55},
 {'age': 333, 'amount': 1.2}]
```
    op hex (20)
    0000   0x5c 0x14 0x04 0xf3 0x04 0x24 0xfd 0x04    \....$..
    0008   0x22 0x07 0x14 0x70 0x11 0x14 0x16 0x1b    "..p....
    0010   0x14 0x30 0x4d 0x14                        .0M.
    decimal
             92   20    4  243    4   36  253    4
             34    7   20  112   17   20   22   27
             20   48   77   20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2015-02-19T17:49:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4,
 'duration': 0,
 'programmed': 5.4,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xd8 0x00 0xd8 0x00 0x00 0x00    ........
    decimal
              1    0  216    0  216    0    0    0
    datetime (2015-02-19T17:49:10)
    0000   0x0a 0xb1 0x51 0x73 0x0f                   ..Qs.
    body (0)

#### RECORD 4 BolusWizard 2015-02-19T17:53:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 190,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.7,
 'carb_input': 30,
 'carb_ratio': 8.0,
 'correction_estimate': 1.7,
 'food_estimate': 3.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 5.4}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2015-02-19T17:53:29)
    0000   0x1d 0xb5 0x11 0x73 0x0f                   ...s.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x50 0x28 0x5a 0x44 0x00    .P.P(ZD.
    0008   0x94 0x00 0x00 0xd8 0x00 0x94 0x78         ......x
    decimal
             30   80    0   80   40   90   68    0
            148    0    0  216    0  148  120

#### RECORD 5 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 5.4},
 {'age': 247, 'amount': 0.1},
 {'age': 257, 'amount': 0.9},
 {'age': 267, 'amount': 0.85},
 {'age': 277, 'amount': 2.8},
 {'age': 287, 'amount': 0.55},
 {'age': 337, 'amount': 1.2}]
```
    op hex (23)
    0000   0x5c 0x17 0xd8 0x07 0x04 0x04 0xf7 0x04    \.......
    0008   0x24 0x01 0x14 0x22 0x0b 0x14 0x70 0x15    $.."..p.
    0010   0x14 0x16 0x1f 0x14 0x30 0x51 0x14         ....0Q.
    decimal
             92   23  216    7    4    4  247    4
             36    1   20   34   11   20  112   21
             20   22   31   20   48   81   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2015-02-19T17:53:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7,
 'duration': 0,
 'programmed': 3.7,
 'type': 'normal',
 'unabsorbed': 5.4}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0xd8 0x00    ........
    decimal
              1    0  148    0  148    0  216    0
    datetime (2015-02-19T17:53:29)
    0000   0x1d 0xb5 0x51 0x73 0x0f                   ..Qs.
    body (0)

#### RECORD 7 SensorAlert 2015-02-19T20:19:27 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-19T20:19:27)
    0000   0x1b 0x93 0x34 0xb3 0x0f                   ..4..
    body (0)

#### RECORD 8 SensorAlert 2015-02-19T20:38:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-02-19T20:38:46)
    0000   0x2e 0xa6 0x34 0xb3 0x0f                   ..4..
    body (0)

#### RECORD 9 BasalProfileStart 2015-02-19T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-19T22:00:00)
    0000   0x00 0x80 0x16 0x13 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 10 SensorAlert 2015-02-19T22:08:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 211}
```
    op hex (3)
    0000   0x0b 0x65 0xd3                             .e.
    decimal
             11  101  211
    datetime (2015-02-19T22:08:48)
    0000   0x30 0x88 0x36 0xb3 0x0f                   0.6..
    body (0)

#### RECORD 11 Bolus 2015-02-19T23:30:32 head[8], body[0] op[0x01]
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
    datetime (2015-02-19T23:30:32)
    0000   0x20 0x9e 0x57 0x73 0x0f                    .Ws.
    body (0)

#### RECORD 12 BolusWizard 2015-02-19T23:33:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-19T23:33:37)
    0000   0x25 0xa1 0x17 0x73 0x0f                   %..s.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    -P.d(Z..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x78         ......x
    decimal
             45   80    0  100   40   90    0    0
            180    0    0    0    0  180  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 4.0}, {'age': 347, 'amount': 2.7}]
```
    op hex (8)
    0000   0x5c 0x08 0xa0 0x07 0x04 0x6c 0x5b 0x15    \....l[.
    decimal
             92    8  160    7    4  108   91   21
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2015-02-19T23:33:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.9,
 'duration': 0,
 'programmed': 5.9,
 'type': 'normal',
 'unabsorbed': 4.0}
```
    op hex (8)
    0000   0x01 0x00 0xec 0x00 0xec 0x00 0xa0 0x00    ........
    decimal
              1    0  236    0  236    0  160    0
    datetime (2015-02-19T23:33:37)
    0000   0x25 0xa1 0x57 0x73 0x0f                   %.Ws.
    body (0)

#### RECORD 15 SensorAlert 2015-02-19T23:39:27 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 317}
```
    op hex (3)
    0000   0x0b 0x65 0x3d                             .e=
    decimal
             11  101   61
    datetime (2015-02-19T23:39:27)
    0000   0x1b 0xa7 0x37 0xb3 0x8f                   ..7..
    body (0)

#### RECORD 16 BasalProfileStart 2015-02-20T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-20T00:00:00)
    0000   0x00 0x80 0x00 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 17 MResultTotals 2015-02-20T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0xbd                   .....
    decimal
              7    0    0    9  189
    datetime (2015-02-20T00:00:00)
    0000   0x33 0x0f                                  3.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 18 Sara6E 2015-02-20T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-20T00:00:00)
    0000   0x33 0x0f                                  3.
    body (49)
    hex
    0000   0x05 0x00 0xb4 0xa7 0xbe 0x03 0x00 0x00    ........
    0008   0x09 0xbd 0x03 0x17 0x20 0x06 0xa6 0x44    .... ..D
    0010   0x01 0x19 0x02 0x00 0x00 0x30 0x02 0xaa    .....0..
    0018   0x01 0xcc 0x04 0x01 0x03 0x04 0x00 0xbf    ........
    0020   0x39 0x2b 0x00 0x1a 0x2e 0x05 0x00 0x00    9+......
    0028   0x00 0x00 0x0d 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  180  167  190    3    0    0
              9  189    3   23   32    6  166   68
              1   25    2    0    0   48    2  170
              1  204    4    1    3    4    0  191
             57   43    0   26   46    5    0    0
              0    0   13    1    0    0    0    0
              0

#### RECORD 19 BasalProfileStart 2015-02-20T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-20T04:00:00)
    0000   0x00 0x80 0x04 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 20 SensorAlert 2015-02-20T04:49:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-20T04:49:00)
    0000   0x00 0xb1 0x24 0xb4 0x0f                   ..$..
    body (0)

#### RECORD 21 SensorAlert 2015-02-20T05:49:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-20T05:49:00)
    0000   0x00 0xb1 0x25 0xb4 0x0f                   ..%..
    body (0)

#### RECORD 22 CalBGForPH 2015-02-20T06:41:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2015-02-20T06:41:14)
    0000   0x0e 0xa9 0x26 0x74 0x0f                   ..&t.
    body (0)

#### RECORD 23 BGReceived 2015-02-20T06:41:14 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 130, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2015-02-20T06:41:14)
    0000   0x0e 0xa9 0x46 0x74 0x0f                   ..Ft.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 24 BolusWizard 2015-02-20T06:41:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 130,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2015-02-20T06:41:40)
    0000   0x28 0xa9 0x06 0x14 0x0f                   (....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x08 0x00    .P.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x08 0x78         ......x
    decimal
              0   80    0  100   40   90    8    0
              0    0    0    0    0    8  120

#### RECORD 25 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 425, 'amount': 2.4}, {'age': 435, 'amount': 1.1}]
```
    op hex (8)
    0000   0x5c 0x08 0x60 0xa9 0x14 0x2c 0xb3 0x15    \.`..,..
    decimal
             92    8   96  169   20   44  179   21
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2015-02-20T06:41:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2,
 'duration': 0,
 'programmed': 0.2,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x08 0x00 0x08 0x00 0x00 0x00    ........
    decimal
              1    0    8    0    8    0    0    0
    datetime (2015-02-20T06:41:40)
    0000   0x28 0xa9 0x46 0x14 0x0f                   (.F..
    body (0)

#### RECORD 27 BasalProfileStart 2015-02-20T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-20T07:00:00)
    0000   0x00 0x80 0x07 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 28 PumpSuspend 2015-02-20T07:49:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-20T07:49:30)
    0000   0x1e 0xb1 0x07 0x14 0x0f                   .....
    body (0)

#### RECORD 29 SensorAlert 2015-02-20T08:04:54 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-20T08:04:54)
    0000   0x36 0x84 0x28 0xb4 0x0f                   6.(..
    body (0)

#### RECORD 30 BasalProfileStart 2015-02-20T08:12:03 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-20T08:12:03)
    0000   0x03 0x8c 0x08 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 31 PumpResume 2015-02-20T08:12:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-20T08:12:04)
    0000   0x04 0x8c 0x08 0x14 0x0f                   .....
    body (0)

#### RECORD 32 Bolus 2015-02-20T08:18:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x08 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    8    0
    datetime (2015-02-20T08:18:38)
    0000   0x26 0x92 0x48 0x74 0x0f                   &.Ht.
    body (0)

#### RECORD 33 BolusWizard 2015-02-20T08:26:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-20T08:26:23)
    0000   0x17 0x9a 0x08 0x74 0x0f                   ...t.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    <P.d(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             60   80    0  100   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 34 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 2.0}, {'age': 110, 'amount': 0.2}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0x0a 0x04 0x08 0x6e 0x04    \.P...n.
    decimal
             92    8   80   10    4    8  110    4
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2015-02-20T08:26:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 2.1}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0x54 0x00    ......T.
    decimal
              1    0  240    0  240    0   84    0
    datetime (2015-02-20T08:26:23)
    0000   0x17 0x9a 0x48 0x74 0x0f                   ..Ht.
    body (0)

#### RECORD 36 BasalProfileStart 2015-02-20T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-20T10:00:00)
    0000   0x00 0x80 0x0a 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 37 SensorAlert 2015-02-20T11:24:54 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-20T11:24:54)
    0000   0x36 0x98 0x2b 0xb4 0x0f                   6.+..
    body (0)

#### RECORD 38 Bolus 2015-02-20T11:33:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 1.2}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x30 0x00    ......0.
    decimal
              1    0  140    0  140    0   48    0
    datetime (2015-02-20T11:33:28)
    0000   0x1c 0xa1 0x4b 0x74 0x0f                   ..Kt.
    body (0)

#### RECORD 39 BolusWizard 2015-02-20T11:45:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.7,
 'carb_input': 38,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-20T11:45:19)
    0000   0x13 0xad 0x0b 0x74 0x0f                   ...t.
    body (15)
    hex
    0000   0x26 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    &P.P(Z..
    0008   0xbc 0x00 0x00 0x00 0x00 0xbc 0x78         ......x
    decimal
             38   80    0   80   40   90    0    0
            188    0    0    0    0  188  120

#### RECORD 40 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 3.5},
 {'age': 199, 'amount': 6.0},
 {'age': 209, 'amount': 2.0},
 {'age': 309, 'amount': 0.2}]
```
    op hex (14)
    0000   0x5c 0x0e 0x8c 0x13 0x04 0xf0 0xc7 0x04    \.......
    0008   0x50 0xd1 0x04 0x08 0x35 0x14              P...5.
    decimal
             92   14  140   19    4  240  199    4
             80  209    4    8   53   20
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2015-02-20T11:45:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7,
 'duration': 0,
 'programmed': 4.7,
 'type': 'normal',
 'unabsorbed': 4.4}
```
    op hex (8)
    0000   0x01 0x00 0xbc 0x00 0xbc 0x00 0xb0 0x00    ........
    decimal
              1    0  188    0  188    0  176    0
    datetime (2015-02-20T11:45:19)
    0000   0x13 0xad 0x4b 0x74 0x0f                   ..Kt.
    body (0)

#### RECORD 42 BasalProfileStart 2015-02-20T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-20T12:00:00)
    0000   0x00 0x80 0x0c 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 43 SensorAlert 2015-02-20T14:19:27 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-20T14:19:27)
    0000   0x1b 0x93 0x2e 0xb4 0x0f                   .....
    body (0)

#### RECORD 44 SensorAlert 2015-02-20T14:25:22 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-20T14:25:22)
    0000   0x16 0x99 0x2e 0xb4 0x0f                   .....
    body (0)

#### RECORD 45 Bolus 2015-02-20T14:53:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x2c 0x00    ......,.
    decimal
              1    0  140    0  140    0   44    0
    datetime (2015-02-20T14:53:06)
    0000   0x06 0xb5 0x4e 0x74 0x0f                   ..Nt.
    body (0)

#### RECORD 46 BasalProfileStart 2015-02-20T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-20T15:00:00)
    0000   0x00 0x80 0x0f 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 47 Bolus 2015-02-20T15:32:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 3.5}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x8c 0x00    ........
    decimal
              1    0  160    0  160    0  140    0
    datetime (2015-02-20T15:32:03)
    0000   0x03 0xa0 0x4f 0x74 0x0f                   ..Ot.
    body (0)

#### RECORD 48 SensorAlert 2015-02-20T15:55:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 250}
```
    op hex (3)
    0000   0x0b 0x65 0xfa                             .e.
    decimal
             11  101  250
    datetime (2015-02-20T15:55:03)
    0000   0x03 0xb7 0x2f 0xb4 0x0f                   ../..
    body (0)

#### RECORD 49 Bolus 2015-02-20T15:55:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x01 0x08 0x00    ..P.P...
    decimal
              1    0   80    0   80    1    8    0
    datetime (2015-02-20T15:55:23)
    0000   0x17 0xb7 0x4f 0x74 0x0f                   ..Ot.
    body (0)

#### RECORD 50 SensorAlert 2015-02-20T17:24:54 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 186}
```
    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-02-20T17:24:54)
    0000   0x36 0x98 0x31 0xb4 0x0f                   6.1..
    body (0)

#### RECORD 51 Bolus 2015-02-20T17:25:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 4.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xa0 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  160    0
    datetime (2015-02-20T17:25:16)
    0000   0x10 0x99 0x51 0x74 0x0f                   ..Qt.
    body (0)

#### RECORD 52 SensorAlert 2015-02-20T17:43:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-20T17:43:00)
    0000   0x00 0xab 0x31 0xb4 0x0f                   ..1..
    body (0)

#### RECORD 53 SensorAlert 2015-02-20T18:43:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-20T18:43:00)
    0000   0x00 0xab 0x32 0xb4 0x0f                   ..2..
    body (0)

#### RECORD 54 CalBGForPH 2015-02-20T18:46:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2015-02-20T18:46:16)
    0000   0x10 0xae 0x32 0x74 0x0f                   ..2t.
    body (0)

#### RECORD 55 BGReceived 2015-02-20T18:46:16 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 194, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2015-02-20T18:46:16)
    0000   0x10 0xae 0x52 0x74 0x0f                   ..Rt.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 56 BolusWizard 2015-02-20T18:46:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 194,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.0,
 'carb_input': 48,
 'carb_ratio': 8.0,
 'correction_estimate': 1.8,
 'food_estimate': 8.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 2.4}
```
    op hex (2)
    0000   0x5b 0xc2                                  [.
    decimal
             91  194
    datetime (2015-02-20T18:46:57)
    0000   0x39 0xae 0x12 0x74 0x0f                   9..t.
    body (15)
    hex
    0000   0x30 0x50 0x00 0x3c 0x28 0x5a 0x48 0x01    0P.<(ZH.
    0008   0x40 0x00 0x00 0x60 0x01 0x40 0x78         @..`.@x
    decimal
             48   80    0   60   40   90   72    1
             64    0    0   96    1   64  120

#### RECORD 57 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 80, 'amount': 0.9},
 {'age': 90, 'amount': 1.1},
 {'age': 170, 'amount': 1.05},
 {'age': 180, 'amount': 0.95},
 {'age': 200, 'amount': 4.0},
 {'age': 240, 'amount': 3.5},
 {'age': 420, 'amount': 3.7},
 {'age': 430, 'amount': 1.0},
 {'age': 440, 'amount': 3.5}]
```
    op hex (29)
    0000   0x5c 0x1d 0x24 0x50 0x04 0x2c 0x5a 0x04    \.$P.,Z.
    0008   0x2a 0xaa 0x04 0x26 0xb4 0x04 0xa0 0xc8    *..&....
    0010   0x04 0x8c 0xf0 0x04 0x94 0xa4 0x14 0x28    .......(
    0018   0xae 0x14 0x8c 0xb8 0x14                   .....
    decimal
             92   29   36   80    4   44   90    4
             42  170    4   38  180    4  160  200
              4  140  240    4  148  164   20   40
            174   20  140  184   20
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2015-02-20T18:50:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 90,
 'programmed': 3.0,
 'type': 'square',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x60 0x03    ..x.x.`.
    decimal
              1    0  120    0  120    0   96    3
    datetime (2015-02-20T18:50:17)
    0000   0x11 0xb2 0xb2 0x74 0x0f                   ...t.
    body (0)

#### RECORD 59 Bolus 2015-02-20T18:46:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x60 0x00    ......`.
    decimal
              1    0  200    0  200    0   96    0
    datetime (2015-02-20T18:46:57)
    0000   0x39 0xae 0x92 0x74 0x0f                   9..t.
    body (0)

#### RECORD 60 SensorAlert 2015-02-20T18:59:27 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 194}
```
    op hex (3)
    0000   0x0b 0x65 0xc2                             .e.
    decimal
             11  101  194
    datetime (2015-02-20T18:59:27)
    0000   0x1b 0xbb 0x32 0xb4 0x0f                   ..2..
    body (0)

#### RECORD 61 SensorAlert 2015-02-20T21:34:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-20T21:34:04)
    0000   0x04 0xa2 0x35 0xb4 0x0f                   ..5..
    body (0)

#### RECORD 62 Bolus 2015-02-20T21:34:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 2.5}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x64 0x00    ..x.x.d.
    decimal
              1    0  120    0  120    0  100    0
    datetime (2015-02-20T21:34:28)
    0000   0x1c 0xa2 0x55 0x74 0x0f                   ..Ut.
    body (0)

#### RECORD 63 SensorAlert 2015-02-20T21:50:14 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 188}
```
    op hex (3)
    0000   0x0b 0x65 0xbc                             .e.
    decimal
             11  101  188
    datetime (2015-02-20T21:50:14)
    0000   0x0e 0xb2 0x35 0xb4 0x0f                   ..5..
    body (0)

#### RECORD 64 Bolus 2015-02-20T21:52:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 4.8}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xc0 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  192    0
    datetime (2015-02-20T21:52:20)
    0000   0x14 0xb4 0x55 0x74 0x0f                   ..Ut.
    body (0)

#### RECORD 65 BasalProfileStart 2015-02-20T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-20T22:00:00)
    0000   0x00 0x80 0x16 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 66 BasalProfileStart 2015-02-21T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-21T00:00:00)
    0000   0x00 0x80 0x00 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 67 MResultTotals 2015-02-21T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0x74                   ....t
    decimal
              7    0    0    9  116
    datetime (2015-02-21T00:00:00)
    0000   0x34 0x0f                                  4.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 68 Sara6E 2015-02-21T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-21T00:00:00)
    0000   0x34 0x0f                                  4.
    body (49)
    hex
    0000   0x05 0x00 0xa2 0x82 0xc2 0x02 0x00 0x00    ........
    0008   0x09 0x74 0x03 0x24 0x21 0x06 0x50 0x43    .t.$!.PC
    0010   0x00 0x92 0x02 0xec 0x00 0x08 0x00 0x00    ........
    0018   0x03 0x5c 0x03 0x01 0x00 0x08 0x00 0xa6    .\......
    0020   0x24 0x40 0x00 0x10 0x27 0x03 0x00 0x00    $@..'...
    0028   0x00 0x00 0x06 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  162  130  194    2    0    0
              9  116    3   36   33    6   80   67
              0  146    2  236    0    8    0    0
              3   92    3    1    0    8    0  166
             36   64    0   16   39    3    0    0
              0    0    6    1    0    0    0    0
              0

#### RECORD 69 SensorAlert 2015-02-21T00:04:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-21T00:04:53)
    0000   0x35 0x84 0x20 0xb5 0x0f                   5. ..
    body (0)

#### RECORD 70 SensorAlert 2015-02-21T00:14:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-21T00:14:04)
    0000   0x04 0x8e 0x20 0xb5 0x0f                   .. ..
    body (0)

#### RECORD 71 Bolus 2015-02-21T02:12:35 head[8], body[0] op[0x01]
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
    datetime (2015-02-21T02:12:35)
    0000   0x23 0x8c 0x42 0x75 0x0f                   #.Bu.
    body (0)

#### RECORD 72 SensorAlert 2015-02-21T03:15:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 292}
```
    op hex (3)
    0000   0x0b 0x65 0x24                             .e$
    decimal
             11  101   36
    datetime (2015-02-21T03:15:02)
    0000   0x02 0x8f 0x23 0xb5 0x8f                   ..#..
    body (0)

#### RECORD 73 Bolus 2015-02-21T03:21:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 3.0}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x78 0x00    ..x.x.x.
    decimal
              1    0  120    0  120    0  120    0
    datetime (2015-02-21T03:21:53)
    0000   0x35 0x95 0x43 0x75 0x0f                   5.Cu.
    body (0)

#### RECORD 74 BasalProfileStart 2015-02-21T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-21T04:00:00)
    0000   0x00 0x80 0x04 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 75 SensorAlert 2015-02-21T04:44:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 257}
```
    op hex (3)
    0000   0x0b 0x65 0x01                             .e.
    decimal
             11  101    1
    datetime (2015-02-21T04:44:53)
    0000   0x35 0xac 0x24 0xb5 0x8f                   5.$..
    body (0)

#### RECORD 76 Bolus 2015-02-21T05:29:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x40 0x00    ..P.P.@.
    decimal
              1    0   80    0   80    0   64    0
    datetime (2015-02-21T05:29:20)
    0000   0x14 0x9d 0x45 0x75 0x0f                   ..Eu.
    body (0)

#### RECORD 77 SensorAlert 2015-02-21T05:46:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-21T05:46:00)
    0000   0x00 0xae 0x25 0xb5 0x0f                   ..%..
    body (0)

#### RECORD 78 SensorAlert 2015-02-21T06:14:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 237}
```
    op hex (3)
    0000   0x0b 0x65 0xed                             .e.
    decimal
             11  101  237
    datetime (2015-02-21T06:14:04)
    0000   0x04 0x8e 0x26 0xb5 0x0f                   ..&..
    body (0)

#### RECORD 79 CalBGForPH 2015-02-21T06:38:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 235}
```
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2015-02-21T06:38:24)
    0000   0x18 0xa6 0x26 0x75 0x0f                   ..&u.
    body (0)

#### RECORD 80 BGReceived 2015-02-21T06:38:24 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 235, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2015-02-21T06:38:24)
    0000   0x18 0xa6 0x66 0x75 0x0f                   ..fu.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

`end ReadHistoryData-page-24.data: 81 records`
