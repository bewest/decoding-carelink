## START ReadHistoryData-page-10.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xff 0xab                                  ..
##### DEBUG DECIMAL
            255  171
#### RECORD 0 UnabsorbedInsulinBolus unknown head[59], body[0] op[0x5c]
###### DECODED
```python
[{'age': 238, 'amount': 3.0},
 {'age': 288, 'amount': 0.15},
 {'age': 298, 'amount': 0.15},
 {'age': 308, 'amount': 0.2},
 {'age': 318, 'amount': 0.15},
 {'age': 328, 'amount': 0.15},
 {'age': 338, 'amount': 0.2},
 {'age': 348, 'amount': 0.15},
 {'age': 358, 'amount': 0.15},
 {'age': 368, 'amount': 0.2},
 {'age': 378, 'amount': 0.15},
 {'age': 388, 'amount': 0.15},
 {'age': 398, 'amount': 0.2},
 {'age': 408, 'amount': 0.15},
 {'age': 418, 'amount': 0.15},
 {'age': 428, 'amount': 0.2},
 {'age': 438, 'amount': 0.15},
 {'age': 448, 'amount': 0.15},
 {'age': 458, 'amount': 0.2}]
```
    op hex (59)
    0000   0x5c 0x3b 0x78 0xee 0x04 0x06 0x20 0x14    \;x... .
    0008   0x06 0x2a 0x14 0x08 0x34 0x14 0x06 0x3e    .*..4..>
    0010   0x14 0x06 0x48 0x14 0x08 0x52 0x14 0x06    ..H..R..
    0018   0x5c 0x14 0x06 0x66 0x14 0x08 0x70 0x14    \..f..p.
    0020   0x06 0x7a 0x14 0x06 0x84 0x14 0x08 0x8e    .z......
    0028   0x14 0x06 0x98 0x14 0x06 0xa2 0x14 0x08    ........
    0030   0xac 0x14 0x06 0xb6 0x14 0x06 0xc0 0x14    ........
    0038   0x08 0xca 0x14                             ...
    decimal
             92   59  120  238    4    6   32   20
              6   42   20    8   52   20    6   62
             20    6   72   20    8   82   20    6
             92   20    6  102   20    8  112   20
              6  122   20    6  132   20    8  142
             20    6  152   20    6  162   20    8
            172   20    6  182   20    6  192   20
              8  202   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-03-12T16:37:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2,
 'duration': 0,
 'programmed': 2.2,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x08 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    8    0
    datetime (2015-03-12T16:37:32)
    0000   0x20 0xe5 0x50 0x6c 0x0f                    .Pl.
    body (0)

#### RECORD 2 SensorAlert 2015-03-12T17:04:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-12T17:04:00)
    0000   0x00 0xc4 0x31 0xac 0x0f                   ..1..
    body (0)

#### RECORD 3 SensorAlert 2015-03-12T17:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-12T17:34:00)
    0000   0x00 0xe2 0x31 0xac 0x0f                   ..1..
    body (0)

#### RECORD 4 CalBGForPH 2015-03-12T17:35:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 209}
```
    op hex (2)
    0000   0x0a 0xd1                                  ..
    decimal
             10  209
    datetime (2015-03-12T17:35:00)
    0000   0x00 0xe3 0x31 0x6c 0x0f                   ..1l.
    body (0)

#### RECORD 5 BGReceived 2015-03-12T17:35:00 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 209, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2015-03-12T17:35:00)
    0000   0x00 0xe3 0x31 0x6c 0x0f                   ..1l.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 6 BolusWizard 2015-03-12T17:35:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 209,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 2.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.8}
```
    op hex (2)
    0000   0x5b 0xd1                                  [.
    decimal
             91  209
    datetime (2015-03-12T17:35:11)
    0000   0x0b 0xe3 0x11 0x0c 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x58 0x00    .P.P(ZX.
    0008   0x00 0x00 0x00 0x48 0x00 0x10 0x78         ...H..x
    decimal
              0   80    0   80   40   90   88    0
              0    0    0   72    0   16  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[50], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 2.2},
 {'age': 296, 'amount': 3.0},
 {'age': 346, 'amount': 0.15},
 {'age': 356, 'amount': 0.15},
 {'age': 366, 'amount': 0.2},
 {'age': 376, 'amount': 0.15},
 {'age': 386, 'amount': 0.15},
 {'age': 396, 'amount': 0.2},
 {'age': 406, 'amount': 0.15},
 {'age': 416, 'amount': 0.15},
 {'age': 426, 'amount': 0.2},
 {'age': 436, 'amount': 0.15},
 {'age': 446, 'amount': 0.15},
 {'age': 456, 'amount': 0.2},
 {'age': 466, 'amount': 0.15},
 {'age': 476, 'amount': 0.15}]
```
    op hex (50)
    0000   0x5c 0x32 0x58 0x42 0x04 0x78 0x28 0x14    \2XB.x(.
    0008   0x06 0x5a 0x14 0x06 0x64 0x14 0x08 0x6e    .Z..d..n
    0010   0x14 0x06 0x78 0x14 0x06 0x82 0x14 0x08    ..x.....
    0018   0x8c 0x14 0x06 0x96 0x14 0x06 0xa0 0x14    ........
    0020   0x08 0xaa 0x14 0x06 0xb4 0x14 0x06 0xbe    ........
    0028   0x14 0x08 0xc8 0x14 0x06 0xd2 0x14 0x06    ........
    0030   0xdc 0x14                                  ..
    decimal
             92   50   88   66    4  120   40   20
              6   90   20    6  100   20    8  110
             20    6  120   20    6  130   20    8
            140   20    6  150   20    6  160   20
              8  170   20    6  180   20    6  190
             20    8  200   20    6  210   20    6
            220   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2015-03-12T17:35:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4,
 'duration': 0,
 'programmed': 0.4,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x48 0x00    ......H.
    decimal
              1    0   16    0   16    0   72    0
    datetime (2015-03-12T17:35:11)
    0000   0x0b 0xe3 0x51 0x0c 0x0f                   ..Q..
    body (0)

#### RECORD 9 SensorAlert 2015-03-12T17:48:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 214}
```
    op hex (3)
    0000   0x0b 0x65 0xd6                             .e.
    decimal
             11  101  214
    datetime (2015-03-12T17:48:02)
    0000   0x02 0xf0 0x31 0xac 0x0f                   ..1..
    body (0)

#### RECORD 10 SensorAlert 2015-03-12T19:19:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 228}
```
    op hex (3)
    0000   0x0b 0x65 0xe4                             .e.
    decimal
             11  101  228
    datetime (2015-03-12T19:19:18)
    0000   0x12 0xd3 0x33 0xac 0x0f                   ..3..
    body (0)

#### RECORD 11 SensorAlert 2015-03-12T20:48:59 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 304}
```
    op hex (3)
    0000   0x0b 0x65 0x30                             .e0
    decimal
             11  101   48
    datetime (2015-03-12T20:48:59)
    0000   0x3b 0xf0 0x34 0xac 0x8f                   ;.4..
    body (0)

#### RECORD 12 BolusWizard 2015-03-12T20:49:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.2,
 'carb_input': 70,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 11.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-12T20:49:31)
    0000   0x1f 0xf1 0x14 0x6c 0x0f                   ...l.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    FP.<(Z..
    0008   0xd0 0x00 0x00 0x00 0x01 0xd0 0x78         ......x
    decimal
             70   80    0   60   40   90    0    1
            208    0    0    0    1  208  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 200, 'amount': 0.4}, {'age': 260, 'amount': 2.2}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0xc8 0x04 0x58 0x04 0x14    \....X..
    decimal
             92    8   16  200    4   88    4   20
    datetime (unknown)

    body (0)

#### RECORD 14 LowReservoir 2015-03-12T20:51:26 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-03-12T20:51:26)
    0000   0x1a 0xf3 0x14 0x0c 0x0f                   .....
    body (0)

#### RECORD 15 Bolus 2015-03-12T20:49:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2,
 'duration': 0,
 'programmed': 5.2,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x01 0xd0 0x01 0xd0 0x00 0x04 0x00    ........
    decimal
              1    1  208    1  208    0    4    0
    datetime (2015-03-12T20:49:31)
    0000   0x1f 0xf1 0x54 0x6c 0x0f                   ..Tl.
    body (0)

#### RECORD 16 BasalProfileStart 2015-03-12T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-12T22:00:00)
    0000   0x00 0xc0 0x16 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 17 CalBGForPH 2015-03-12T23:35:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2015-03-12T23:35:46)
    0000   0x2e 0xe3 0x37 0x6c 0x0f                   ..7l.
    body (0)

#### RECORD 18 BGReceived 2015-03-12T23:35:46 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 171, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2015-03-12T23:35:46)
    0000   0x2e 0xe3 0x77 0x6c 0x0f                   ..wl.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 19 LowReservoir 2015-03-12T23:37:21 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-03-12T23:37:21)
    0000   0x15 0xe5 0x17 0x0c 0x0f                   .....
    body (0)

#### RECORD 20 Bolus 2015-03-12T23:36:13 head[8], body[0] op[0x01]
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
    datetime (2015-03-12T23:36:13)
    0000   0x0d 0xe4 0x57 0x6c 0x0f                   ..Wl.
    body (0)

#### RECORD 21 BasalProfileStart 2015-03-13T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-13T00:00:00)
    0000   0x00 0xc0 0x00 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 22 MResultTotals 2015-03-13T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x03                   .....
    decimal
              7    0    0    8    3
    datetime (2015-03-13T00:00:00)
    0000   0x2c 0x8f                                  ,.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 23 Sara6E 2015-03-13T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-13T00:00:00)
    0000   0x2c 0x8f                                  ,.
    body (49)
    hex
    0000   0x05 0x00 0xa5 0x44 0xda 0x05 0x00 0x00    ...D....
    0008   0x08 0x03 0x03 0x23 0x27 0x04 0xe0 0x3d    ...#'..=
    0010   0x00 0xaa 0x03 0x24 0x00 0x68 0x00 0x00    ...$.h..
    0018   0x01 0x54 0x03 0x02 0x00 0x03 0x00 0xb7    .T......
    0020   0x3c 0x22 0x06 0xfb 0x3c 0x02 0x02 0x00    <"..<...
    0028   0x00 0x04 0x09 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  165   68  218    5    0    0
              8    3    3   35   39    4  224   61
              0  170    3   36    0  104    0    0
              1   84    3    2    0    3    0  183
             60   34    6  251   60    2    2    0
              0    4    9    0    0    0    0    0
              0

#### RECORD 24 BasalProfileStart 2015-03-13T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-13T04:00:00)
    0000   0x00 0xc0 0x04 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 25 BasalProfileStart 2015-03-13T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-13T07:00:00)
    0000   0x00 0xc0 0x07 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 26 PumpSuspend 2015-03-13T07:23:59 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-13T07:23:59)
    0000   0x3b 0xd7 0x07 0x0d 0x0f                   ;....
    body (0)

#### RECORD 27 BasalProfileStart 2015-03-13T07:45:05 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-13T07:45:05)
    0000   0x05 0xed 0x07 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 28 PumpResume 2015-03-13T07:45:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-13T07:45:06)
    0000   0x06 0xed 0x07 0x0d 0x0f                   .....
    body (0)

#### RECORD 29 SensorAlert 2015-03-13T09:28:59 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-13T09:28:59)
    0000   0x3b 0xdc 0x29 0xad 0x0f                   ;.)..
    body (0)

#### RECORD 30 BasalProfileStart 2015-03-13T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-13T10:00:00)
    0000   0x00 0xc0 0x0a 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 31 SensorAlert 2015-03-13T10:18:50 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-03-13T10:18:50)
    0000   0x32 0xd2 0x2a 0xad 0x0f                   2.*..
    body (0)

#### RECORD 32 SensorAlert 2015-03-13T10:35:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-13T10:35:00)
    0000   0x00 0xe3 0x2a 0xad 0x0f                   ..*..
    body (0)

#### RECORD 33 CalBGForPH 2015-03-13T10:36:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 246}
```
    op hex (2)
    0000   0x0a 0xf6                                  ..
    decimal
             10  246
    datetime (2015-03-13T10:36:08)
    0000   0x08 0xe4 0x2a 0x6d 0x0f                   ..*m.
    body (0)

#### RECORD 34 BGReceived 2015-03-13T10:36:08 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 246, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1e                                  ?.
    decimal
             63   30
    datetime (2015-03-13T10:36:08)
    0000   0x08 0xe4 0xca 0x6d 0x0f                   ...m.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 35 BolusWizard 2015-03-13T10:36:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 246,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.1,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 3.1,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xf6                                  [.
    decimal
             91  246
    datetime (2015-03-13T10:36:26)
    0000   0x1a 0xe4 0x0a 0x0d 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x7c 0x00    .P.d(Z|.
    0008   0x00 0x00 0x00 0x00 0x00 0x7c 0x78         .....|x
    decimal
              0   80    0  100   40   90  124    0
              0    0    0    0    0  124  120

#### RECORD 36 Bolus 2015-03-13T10:36:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1,
 'duration': 0,
 'programmed': 3.1,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x00 0x00    ..|.|...
    decimal
              1    0  124    0  124    0    0    0
    datetime (2015-03-13T10:36:27)
    0000   0x1b 0xe4 0x4a 0x0d 0x0f                   ..J..
    body (0)

#### RECORD 37 SensorAlert 2015-03-13T11:48:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 237}
```
    op hex (3)
    0000   0x0b 0x65 0xed                             .e.
    decimal
             11  101  237
    datetime (2015-03-13T11:48:01)
    0000   0x01 0xf0 0x2b 0xad 0x0f                   ..+..
    body (0)

#### RECORD 38 Bolus 2015-03-13T11:55:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 2.1}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x54 0x00    ..P.P.T.
    decimal
              1    0   80    0   80    0   84    0
    datetime (2015-03-13T11:55:54)
    0000   0x36 0xf7 0x4b 0x6d 0x0f                   6.Km.
    body (0)

#### RECORD 39 BasalProfileStart 2015-03-13T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-13T12:00:00)
    0000   0x00 0xc0 0x0c 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 40 BolusWizard 2015-03-13T13:23:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.0,
 'carb_input': 8,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 1.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-13T13:23:36)
    0000   0x24 0xd7 0x0d 0x6d 0x0f                   $..m.
    body (15)
    hex
    0000   0x08 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x78         (....(x
    decimal
              8   80    0   80   40   90    0    0
             40    0    0    0    0   40  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 2.0}, {'age': 174, 'amount': 3.1}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0x5e 0x04 0x7c 0xae 0x04    \.P^.|..
    decimal
             92    8   80   94    4  124  174    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2015-03-13T13:23:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x4c 0x00    ..(.(.L.
    decimal
              1    0   40    0   40    0   76    0
    datetime (2015-03-13T13:23:36)
    0000   0x24 0xd7 0x4d 0x6d 0x0f                   $.Mm.
    body (0)

#### RECORD 43 BolusWizard 2015-03-13T14:12:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-13T14:12:03)
    0000   0x03 0xcc 0x0e 0x6d 0x0f                   ...m.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    (P.P(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             40   80    0   80   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 44 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 1.0},
 {'age': 143, 'amount': 2.0},
 {'age': 223, 'amount': 3.1}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x35 0x04 0x50 0x8f 0x04    \.(5.P..
    0008   0x7c 0xdf 0x04                             |..
    decimal
             92   11   40   53    4   80  143    4
            124  223    4
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2015-03-13T14:12:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0x74 0x00 0x48 0x00    ....t.H.
    decimal
              1    0  200    0  116    0   72    0
    datetime (2015-03-13T14:12:04)
    0000   0x04 0xcc 0x4e 0x6d 0x0f                   ..Nm.
    body (0)

#### RECORD 46 NoDelivery 2015-03-13T14:14:02 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-13T14:14:02)
    0000   0x02 0xce 0x4e 0x4d 0x0f                   ..NM.
    body (0)

#### RECORD 47 ClearAlarm 2015-03-13T14:16:06 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-13T14:16:06)
    0000   0x06 0xd0 0x0e 0x0d 0x0f                   .....
    body (0)

#### RECORD 48 BasalProfileStart 2015-03-13T14:16:06 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-13T14:16:06)
    0000   0x06 0xd0 0x0e 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 49 Rewind 2015-03-13T14:16:19 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-03-13T14:16:19)
    0000   0x13 0xd0 0x0e 0x0d 0x0f                   .....
    body (0)

#### RECORD 50 Prime 2015-03-13T14:47:52 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 7.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x49                   ....I
    decimal
              3    0    0    0   73
    datetime (2015-03-13T14:47:52)
    0000   0x34 0xef 0x2e 0x0d 0x0f                   4....
    body (0)

#### RECORD 51 SensorAlert 2015-03-13T14:52:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-13T14:52:42)
    0000   0x2a 0xf4 0x2e 0xad 0x0f                   *....
    body (0)

#### RECORD 52 SensorAlert 2015-03-13T14:58:50 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 196}
```
    op hex (3)
    0000   0x0b 0x65 0xc4                             .e.
    decimal
             11  101  196
    datetime (2015-03-13T14:58:50)
    0000   0x32 0xfa 0x2e 0xad 0x0f                   2....
    body (0)

#### RECORD 53 NoDelivery 2015-03-13T15:13:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x4a 0x09 0x3f                        .J.?
    decimal
              6   74    9   63
    datetime (2015-03-13T15:13:00)
    0000   0x00 0xcd 0x4f 0xad 0x0f                   ..O..
    body (0)

#### RECORD 54 ClearAlarm 2015-03-13T15:13:50 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x4a                                  .J
    decimal
             12   74
    datetime (2015-03-13T15:13:50)
    0000   0x32 0xcd 0x0f 0x0d 0x0f                   2....
    body (0)

#### RECORD 55 BasalProfileStart 2015-03-13T15:13:50 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-13T15:13:50)
    0000   0x32 0xcd 0x0f 0x0d 0x0f                   2....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 56 BasalProfileStart 2015-03-13T15:13:51 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-13T15:13:51)
    0000   0x33 0xcd 0x0f 0x0d 0x0f                   3....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 57 BasalProfileStart 2015-03-13T15:14:06 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-13T15:14:06)
    0000   0x06 0xce 0x0f 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 58 Prime 2015-03-13T15:13:52 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-03-13T15:13:52)
    0000   0x34 0xcd 0x0f 0x0d 0x0f                   4....
    body (0)

#### RECORD 59 Bolus 2015-03-13T15:14:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 3.1}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x7c 0x00    ..d.d.|.
    decimal
              1    0  100    0  100    0  124    0
    datetime (2015-03-13T15:14:37)
    0000   0x25 0xce 0x4f 0x6d 0x0f                   %.Om.
    body (0)

#### RECORD 60 SensorAlert 2015-03-13T16:28:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 256}
```
    op hex (3)
    0000   0x0b 0x65 0x00                             .e.
    decimal
             11  101    0
    datetime (2015-03-13T16:28:01)
    0000   0x01 0xdc 0x30 0xad 0x8f                   ..0..
    body (0)

#### RECORD 61 Bolus 2015-03-13T16:28:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 3.0}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x78 0x00    ......x.
    decimal
              1    0  140    0  140    0  120    0
    datetime (2015-03-13T16:28:29)
    0000   0x1d 0xdc 0x50 0x6d 0x0f                   ..Pm.
    body (0)

#### RECORD 62 Bolus 2015-03-13T17:07:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xc8 0x00    ........
    decimal
              1    0  160    0  160    0  200    0
    datetime (2015-03-13T17:07:06)
    0000   0x06 0xc7 0x51 0x6d 0x0f                   ..Qm.
    body (0)

#### RECORD 63 SensorAlert 2015-03-13T20:15:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-13T20:15:12)
    0000   0x0c 0xcf 0x34 0xad 0x0f                   ..4..
    body (0)

#### RECORD 64 SensorAlert 2015-03-13T20:45:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-13T20:45:00)
    0000   0x00 0xed 0x34 0xad 0x0f                   ..4..
    body (0)

#### RECORD 65 CalBGForPH 2015-03-13T20:46:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2015-03-13T20:46:52)
    0000   0x34 0xee 0x34 0x6d 0x0f                   4.4m.
    body (0)

#### RECORD 66 BGReceived 2015-03-13T20:46:52 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 118, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2015-03-13T20:46:52)
    0000   0x34 0xee 0xd4 0x6d 0x0f                   4..m.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 67 BasalProfileStart 2015-03-13T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-13T22:00:00)
    0000   0x00 0xc0 0x16 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 68 CalBGForPH 2015-03-13T22:27:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2015-03-13T22:27:30)
    0000   0x1e 0xdb 0x36 0x6d 0x0f                   ..6m.
    body (0)

#### RECORD 69 BGReceived 2015-03-13T22:27:30 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 172, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2015-03-13T22:27:30)
    0000   0x1e 0xdb 0x96 0x6d 0x0f                   ...m.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 70 BolusWizard 2015-03-13T22:27:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 172,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2015-03-13T22:27:45)
    0000   0x2d 0xdb 0x16 0x0d 0x0f                   -....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x3c 0x28 0x5a 0x34 0x00    .P.<(Z4.
    0008   0x00 0x00 0x00 0x00 0x00 0x34 0x78         .....4x
    decimal
              0   80    0   60   40   90   52    0
              0    0    0    0    0   52  120

#### RECORD 71 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 318, 'amount': 1.2},
 {'age': 328, 'amount': 2.8},
 {'age': 358, 'amount': 2.7},
 {'age': 368, 'amount': 0.8},
 {'age': 438, 'amount': 2.5}]
```
    op hex (17)
    0000   0x5c 0x11 0x30 0x3e 0x14 0x70 0x48 0x14    \.0>.pH.
    0008   0x6c 0x66 0x14 0x20 0x70 0x14 0x64 0xb6    lf. p.d.
    0010   0x14                                       .
    decimal
             92   17   48   62   20  112   72   20
            108  102   20   32  112   20  100  182
             20
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2015-03-13T22:27:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3,
 'duration': 0,
 'programmed': 1.3,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    0    0
    datetime (2015-03-13T22:27:45)
    0000   0x2d 0xdb 0x56 0x0d 0x0f                   -.V..
    body (0)

#### RECORD 73 BasalProfileStart 2015-03-14T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-14T00:00:00)
    0000   0x00 0xc0 0x00 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 74 MResultTotals 2015-03-14T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x32                   ....2
    decimal
              7    0    0    6   50
    datetime (2015-03-14T00:00:00)
    0000   0x2d 0x8f                                  -.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 75 Sara6E 2015-03-14T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-14T00:00:00)
    0000   0x2d 0x8f                                  -.
    body (49)
    hex
    0000   0x05 0x00 0xb3 0x76 0xf6 0x03 0x00 0x00    ...v....
    0008   0x06 0x32 0x03 0x06 0x31 0x03 0x2c 0x33    .2..1.,3
    0010   0x00 0x30 0x00 0x9c 0x00 0xb0 0x00 0x00    .0......
    0018   0x01 0xe0 0x02 0x02 0x00 0x04 0x00 0xaa    ........
    0020   0x19 0x4b 0x00 0x00 0x2d 0x02 0x00 0x00    .K..-...
    0028   0x00 0x00 0x04 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  179  118  246    3    0    0
              6   50    3    6   49    3   44   51
              0   48    0  156    0  176    0    0
              1  224    2    2    0    4    0  170
             25   75    0    0   45    2    0    0
              0    0    4    1    0    0    0    0
              0

#### RECORD 76 SensorAlert 2015-03-14T01:46:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-14T01:46:29)
    0000   0x1d 0xee 0x21 0xae 0x0f                   ..!..
    body (0)

#### RECORD 77 SensorAlert 2015-03-14T01:59:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-14T01:59:53)
    0000   0x35 0xfb 0x21 0xae 0x0f                   5.!..
    body (0)

#### RECORD 78 Bolus 2015-03-14T02:42:13 head[8], body[0] op[0x01]
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
    datetime (2015-03-14T02:42:13)
    0000   0x0d 0xea 0x42 0x6e 0x0f                   ..Bn.
    body (0)

#### RECORD 79 SensorAlert 2015-03-14T03:29:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 188}
```
    op hex (3)
    0000   0x0b 0x65 0xbc                             .e.
    decimal
             11  101  188
    datetime (2015-03-14T03:29:55)
    0000   0x37 0xdd 0x23 0xae 0x0f                   7.#..
    body (0)

`end ReadHistoryData-page-10.data: 80 records`
