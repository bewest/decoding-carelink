## START ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 993, found 29 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xf2 0x7f                                  ..
##### DEBUG DECIMAL
            242  127
#### RECORD 0 SensorAlert 2015-03-19T16:26:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-19T16:26:00)
    0000   0x00 0xda 0x30 0xb3 0x0f                   ..0..
    body (0)

#### RECORD 1 CalBGForPH 2015-03-19T16:26:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2015-03-19T16:26:34)
    0000   0x22 0xda 0x30 0x13 0x0f                   ".0..
    body (0)

#### RECORD 2 SensorAlert 2015-03-19T17:10:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-19T17:10:18)
    0000   0x12 0xca 0x31 0xb3 0x0f                   ..1..
    body (0)

#### RECORD 3 SensorAlert 2015-03-19T17:35:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-19T17:35:45)
    0000   0x2d 0xe3 0x31 0xb3 0x0f                   -.1..
    body (0)

#### RECORD 4 BolusWizard 2015-03-19T18:55:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.3,
 'carb_input': 50,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 8.3,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-19T18:55:45)
    0000   0x2d 0xf7 0x12 0x73 0x0f                   -..s.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    2P.<(Z..
    0008   0x4c 0x00 0x00 0x00 0x01 0x4c 0x78         L....Lx
    decimal
             50   80    0   60   40   90    0    1
             76    0    0    0    1   76  120

#### RECORD 5 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 176, 'amount': 1.0},
 {'age': 226, 'amount': 0.1},
 {'age': 236, 'amount': 2.7},
 {'age': 246, 'amount': 0.25},
 {'age': 256, 'amount': 0.25},
 {'age': 266, 'amount': 0.2},
 {'age': 276, 'amount': 0.25},
 {'age': 286, 'amount': 0.25},
 {'age': 296, 'amount': 1.2},
 {'age': 306, 'amount': 2.5},
 {'age': 346, 'amount': 1.5}]
```
    op hex (35)
    0000   0x5c 0x23 0x28 0xb0 0x04 0x04 0xe2 0x04    \#(.....
    0008   0x6c 0xec 0x04 0x0a 0xf6 0x04 0x0a 0x00    l.......
    0010   0x14 0x08 0x0a 0x14 0x0a 0x14 0x14 0x0a    ........
    0018   0x1e 0x14 0x30 0x28 0x14 0x64 0x32 0x14    ..0(.d2.
    0020   0x3c 0x5a 0x14                             <Z.
    decimal
             92   35   40  176    4    4  226    4
            108  236    4   10  246    4   10    0
             20    8   10   20   10   20   20   10
             30   20   48   40   20  100   50   20
             60   90   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2015-03-19T18:55:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6,
 'duration': 0,
 'programmed': 0.6,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x10 0x00    ........
    decimal
              1    1   24    1   24    0   16    0
    datetime (2015-03-19T18:55:45)
    0000   0x2d 0xf7 0x52 0x73 0x0f                   -.Rs.
    body (0)

#### RECORD 7 SensorAlert 2015-03-19T19:04:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 226}
```
    op hex (3)
    0000   0x0b 0x65 0xe2                             .e.
    decimal
             11  101  226
    datetime (2015-03-19T19:04:56)
    0000   0x38 0xc4 0x33 0xb3 0x0f                   8.3..
    body (0)

#### RECORD 8 Bolus 2015-03-19T19:05:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x01 0x1c 0x00    ..(.(...
    decimal
              1    0   40    0   40    1   28    0
    datetime (2015-03-19T19:05:18)
    0000   0x12 0xc5 0x53 0x73 0x0f                   ..Ss.
    body (0)

#### RECORD 9 BolusWizard 2015-03-19T21:25:06 head[2], body[15] op[0x5b]
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
    datetime (2015-03-19T21:25:06)
    0000   0x06 0xd9 0x15 0x73 0x0f                   ...s.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    (P.<(Z..
    0008   0x08 0x00 0x00 0x00 0x01 0x08 0x78         ......x
    decimal
             40   80    0   60   40   90    0    1
              8    0    0    0    1    8  120

#### RECORD 10 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 146, 'amount': 3.2},
 {'age': 156, 'amount': 4.8},
 {'age': 326, 'amount': 1.0},
 {'age': 376, 'amount': 0.1},
 {'age': 386, 'amount': 2.7},
 {'age': 396, 'amount': 0.25},
 {'age': 406, 'amount': 0.25},
 {'age': 416, 'amount': 0.2},
 {'age': 426, 'amount': 0.25},
 {'age': 436, 'amount': 0.25},
 {'age': 446, 'amount': 1.2},
 {'age': 456, 'amount': 2.5}]
```
    op hex (38)
    0000   0x5c 0x26 0x80 0x92 0x04 0xc0 0x9c 0x04    \&......
    0008   0x28 0x46 0x14 0x04 0x78 0x14 0x6c 0x82    (F..x.l.
    0010   0x14 0x0a 0x8c 0x14 0x0a 0x96 0x14 0x08    ........
    0018   0xa0 0x14 0x0a 0xaa 0x14 0x0a 0xb4 0x14    ........
    0020   0x30 0xbe 0x14 0x64 0xc8 0x14              0..d..
    decimal
             92   38  128  146    4  192  156    4
             40   70   20    4  120   20  108  130
             20   10  140   20   10  150   20    8
            160   20   10  170   20   10  180   20
             48  190   20  100  200   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2015-03-19T21:27:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6,
 'duration': 90,
 'programmed': 2.6,
 'type': 'square',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x60 0x03    ..h.h.`.
    decimal
              1    0  104    0  104    0   96    3
    datetime (2015-03-19T21:27:18)
    0000   0x12 0xdb 0xb5 0x73 0x0f                   ...s.
    body (0)

#### RECORD 12 Bolus 2015-03-19T21:25:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3,
 'duration': 0,
 'programmed': 3.3,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x60 0x00    ......`.
    decimal
              1    0  132    0  132    0   96    0
    datetime (2015-03-19T21:25:06)
    0000   0x06 0xd9 0x95 0x73 0x0f                   ...s.
    body (0)

#### RECORD 13 CalBGForPH 2015-03-19T21:55:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2015-03-19T21:55:55)
    0000   0x37 0xf7 0x35 0x73 0x0f                   7.5s.
    body (0)

#### RECORD 14 BGReceived 2015-03-19T21:55:55 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 120, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2015-03-19T21:55:55)
    0000   0x37 0xf7 0x15 0x73 0x0f                   7..s.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 15 BasalProfileStart 2015-03-19T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-19T22:00:00)
    0000   0x00 0xc0 0x16 0x13 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 16 SensorAlert 2015-03-19T22:59:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-19T22:59:39)
    0000   0x27 0xfb 0x36 0xb3 0x0f                   '.6..
    body (0)

#### RECORD 17 BasalProfileStart 2015-03-20T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-20T00:00:00)
    0000   0x00 0xc0 0x00 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 18 MResultTotals 2015-03-20T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0x0c                   .....
    decimal
              7    0    0    9   12
    datetime (2015-03-20T00:00:00)
    0000   0x33 0x8f                                  3.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 19 Sara6E 2015-03-20T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-20T00:00:00)
    0000   0x33 0x8f                                  3.
    body (49)
    hex
    0000   0x05 0x10 0xb3 0x72 0xa3 0x05 0x00 0x00    ...r....
    0008   0x09 0x0c 0x03 0x30 0x23 0x05 0xdc 0x41    ...0#..A
    0010   0x00 0xd7 0x03 0xc4 0x01 0x28 0x00 0x00    .....(..
    0018   0x00 0xf0 0x04 0x01 0x00 0x04 0x00 0xc9    ........
    0020   0x2b 0x37 0x02 0x13 0x63 0x02 0x02 0x78    +7..c..x
    0028   0x78 0x02 0x07 0x01 0x00 0x00 0x00 0x00    x.......
    0030   0x00                                       .
    decimal
              5   16  179  114  163    5    0    0
              9   12    3   48   35    5  220   65
              0  215    3  196    1   40    0    0
              0  240    4    1    0    4    0  201
             43   55    2   19   99    2    2  120
            120    2    7    1    0    0    0    0
              0

#### RECORD 20 BasalProfileStart 2015-03-20T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-20T04:00:00)
    0000   0x00 0xc0 0x04 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 21 PumpSuspend 2015-03-20T06:53:48 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-20T06:53:48)
    0000   0x30 0xf5 0x06 0x14 0x0f                   0....
    body (0)

#### RECORD 22 BasalProfileStart 2015-03-20T07:30:08 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-20T07:30:08)
    0000   0x08 0xde 0x07 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 23 PumpResume 2015-03-20T07:30:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-20T07:30:08)
    0000   0x08 0xde 0x07 0x14 0x0f                   .....
    body (0)

#### RECORD 24 BolusWizard 2015-03-20T07:30:28 head[2], body[15] op[0x5b]
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
    datetime (2015-03-20T07:30:28)
    0000   0x1c 0xde 0x07 0x74 0x0f                   ...t.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    <P.d(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             60   80    0  100   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 25 Bolus 2015-03-20T07:33:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.15,
 'duration': 60,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x2e 0x00 0x00 0x02    ..P.....
    decimal
              1    0   80    0   46    0    0    2
    datetime (2015-03-20T07:33:08)
    0000   0x08 0xe1 0xa7 0x74 0x0f                   ...t.
    body (0)

#### RECORD 26 Bolus 2015-03-20T07:30:28 head[8], body[0] op[0x01]
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
    datetime (2015-03-20T07:30:28)
    0000   0x1c 0xde 0x87 0x74 0x0f                   ...t.
    body (0)

#### RECORD 27 PumpSuspend 2015-03-20T08:06:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-20T08:06:56)
    0000   0x38 0xc6 0x08 0x14 0x0f                   8....
    body (0)

#### RECORD 28 BasalProfileStart 2015-03-20T08:07:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-20T08:07:00)
    0000   0x00 0xc7 0x08 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 29 PumpResume 2015-03-20T08:07:00 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-20T08:07:00)
    0000   0x00 0xc7 0x08 0x14 0x0f                   .....
    body (0)

#### RECORD 30 Bolus 2015-03-20T08:07:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 4.8}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0xc0 0x00    ........
    decimal
              1    0   20    0   20    0  192    0
    datetime (2015-03-20T08:07:30)
    0000   0x1e 0xc7 0x48 0x74 0x0f                   ..Ht.
    body (0)

#### RECORD 31 PumpSuspend 2015-03-20T08:08:10 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-20T08:08:10)
    0000   0x0a 0xc8 0x08 0x14 0x0f                   .....
    body (0)

#### RECORD 32 BasalProfileStart 2015-03-20T08:14:30 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-20T08:14:30)
    0000   0x1e 0xce 0x08 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 33 PumpResume 2015-03-20T08:14:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-20T08:14:30)
    0000   0x1e 0xce 0x08 0x14 0x0f                   .....
    body (0)

#### RECORD 34 SensorAlert 2015-03-20T08:19:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-20T08:19:39)
    0000   0x27 0xd3 0x28 0xb4 0x0f                   '.(..
    body (0)

#### RECORD 35 SensorAlert 2015-03-20T08:30:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 76}
```
    op hex (3)
    0000   0x0b 0x66 0x4c                             .fL
    decimal
             11  102   76
    datetime (2015-03-20T08:30:18)
    0000   0x12 0xde 0x28 0xb4 0x0f                   ..(..
    body (0)

#### RECORD 36 SensorAlert 2015-03-20T08:56:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-20T08:56:00)
    0000   0x00 0xf8 0x28 0xb4 0x0f                   ..(..
    body (0)

#### RECORD 37 SensorAlert 2015-03-20T08:59:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 72}
```
    op hex (3)
    0000   0x0b 0x66 0x48                             .fH
    decimal
             11  102   72
    datetime (2015-03-20T08:59:39)
    0000   0x27 0xfb 0x28 0xb4 0x0f                   '.(..
    body (0)

#### RECORD 38 SensorAlert 2015-03-20T09:29:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 63}
```
    op hex (3)
    0000   0x0b 0x66 0x3f                             .f?
    decimal
             11  102   63
    datetime (2015-03-20T09:29:37)
    0000   0x25 0xdd 0x29 0xb4 0x0f                   %.)..
    body (0)

#### RECORD 39 SensorAlert 2015-03-20T09:56:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-20T09:56:00)
    0000   0x00 0xf8 0x29 0xb4 0x0f                   ..)..
    body (0)

#### RECORD 40 BasalProfileStart 2015-03-20T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-20T10:00:00)
    0000   0x00 0xc0 0x0a 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 41 SensorAlert 2015-03-20T10:26:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-20T10:26:00)
    0000   0x00 0xda 0x2a 0xb4 0x0f                   ..*..
    body (0)

#### RECORD 42 CalBGForPH 2015-03-20T10:27:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2015-03-20T10:27:05)
    0000   0x05 0xdb 0x2a 0x74 0x0f                   ..*t.
    body (0)

#### RECORD 43 BGReceived 2015-03-20T10:27:05 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 143, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2015-03-20T10:27:05)
    0000   0x05 0xdb 0xea 0x74 0x0f                   ...t.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 44 SensorAlert 2015-03-20T10:49:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-20T10:49:37)
    0000   0x25 0xf1 0x2a 0xb4 0x0f                   %.*..
    body (0)

#### RECORD 45 SensorAlert 2015-03-20T11:04:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-20T11:04:56)
    0000   0x38 0xc4 0x2b 0xb4 0x0f                   8.+..
    body (0)

#### RECORD 46 BolusWizard 2015-03-20T11:58:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-20T11:58:54)
    0000   0x36 0xfa 0x0b 0x74 0x0f                   6..t.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    (P.P(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             40   80    0   80   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 47 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 239, 'amount': 0.8},
 {'age': 249, 'amount': 0.3},
 {'age': 259, 'amount': 0.35},
 {'age': 269, 'amount': 4.2}]
```
    op hex (14)
    0000   0x5c 0x0e 0x20 0xef 0x04 0x0c 0xf9 0x04    \. .....
    0008   0x0e 0x03 0x14 0xa8 0x0d 0x14              ......
    decimal
             92   14   32  239    4   12  249    4
             14    3   20  168   13   20
    datetime (unknown)

    body (0)

#### RECORD 48 BasalProfileStart 2015-03-20T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-20T12:00:00)
    0000   0x00 0xc0 0x0c 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 49 Bolus 2015-03-20T11:58:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x04 0x00    ........
    decimal
              1    0  200    0  200    0    4    0
    datetime (2015-03-20T11:58:54)
    0000   0x36 0xfa 0x4b 0x74 0x0f                   6.Kt.
    body (0)

#### RECORD 50 SensorAlert 2015-03-20T12:36:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 234}
```
    op hex (3)
    0000   0x0b 0x65 0xea                             .e.
    decimal
             11  101  234
    datetime (2015-03-20T12:36:12)
    0000   0x0c 0xe4 0x2c 0xb4 0x0f                   ..,..
    body (0)

#### RECORD 51 Bolus 2015-03-20T12:36:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 4.7}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xbc 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  188    0
    datetime (2015-03-20T12:36:32)
    0000   0x20 0xe4 0x4c 0x74 0x0f                    .Lt.
    body (0)

#### RECORD 52 BasalProfileStart 2015-03-20T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-20T15:00:00)
    0000   0x00 0xc0 0x0f 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 53 SensorAlert 2015-03-20T15:29:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-20T15:29:36)
    0000   0x24 0xdd 0x2f 0xb4 0x0f                   $./..
    body (0)

#### RECORD 54 Bolus 2015-03-20T15:29:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x2c 0x00    ......,.
    decimal
              1    0   20    0   20    0   44    0
    datetime (2015-03-20T15:29:48)
    0000   0x30 0xdd 0x4f 0x74 0x0f                   0.Ot.
    body (0)

#### RECORD 55 SensorAlert 2015-03-20T15:39:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-20T15:39:38)
    0000   0x26 0xe7 0x2f 0xb4 0x0f                   &./..
    body (0)

#### RECORD 56 SensorAlert 2015-03-20T17:16:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-20T17:16:12)
    0000   0x0c 0xd0 0x31 0xb4 0x0f                   ..1..
    body (0)

#### RECORD 57 Bolus 2015-03-20T17:17:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x0c 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   12    0
    datetime (2015-03-20T17:17:13)
    0000   0x0d 0xd1 0x51 0x74 0x0f                   ..Qt.
    body (0)

#### RECORD 58 SensorAlert 2015-03-20T17:21:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-20T17:21:05)
    0000   0x05 0xd5 0x31 0xb4 0x0f                   ..1..
    body (0)

#### RECORD 59 BolusWizard 2015-03-20T18:16:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 10.8,
 'carb_input': 65,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 10.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-20T18:16:20)
    0000   0x14 0xd0 0x12 0x74 0x0f                   ...t.
    body (15)
    hex
    0000   0x41 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    AP.<(Z..
    0008   0xb0 0x00 0x00 0x00 0x01 0xb0 0x78         ......x
    decimal
             65   80    0   60   40   90    0    1
            176    0    0    0    1  176  120

#### RECORD 60 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 1.0},
 {'age': 167, 'amount': 0.5},
 {'age': 347, 'amount': 3.0},
 {'age': 377, 'amount': 4.85},
 {'age': 387, 'amount': 0.15}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0x43 0x04 0x14 0xa7 0x04    \.(C....
    0008   0x78 0x5b 0x14 0xc2 0x79 0x14 0x06 0x83    x[..y...
    0010   0x14                                       .
    decimal
             92   17   40   67    4   20  167    4
            120   91   20  194  121   20    6  131
             20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2015-03-20T18:19:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6,
 'duration': 90,
 'programmed': 3.6,
 'type': 'square',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x24 0x03    ......$.
    decimal
              1    0  144    0  144    0   36    3
    datetime (2015-03-20T18:19:58)
    0000   0x3a 0xd3 0xb2 0x74 0x0f                   :..t.
    body (0)

#### RECORD 62 Bolus 2015-03-20T18:16:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4,
 'duration': 0,
 'programmed': 5.4,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0xd8 0x00 0xd8 0x00 0x24 0x00    ......$.
    decimal
              1    0  216    0  216    0   36    0
    datetime (2015-03-20T18:16:20)
    0000   0x14 0xd0 0x92 0x74 0x0f                   ...t.
    body (0)

#### RECORD 63 SensorAlert 2015-03-20T18:49:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 192}
```
    op hex (3)
    0000   0x0b 0x65 0xc0                             .e.
    decimal
             11  101  192
    datetime (2015-03-20T18:49:36)
    0000   0x24 0xf1 0x32 0xb4 0x0f                   $.2..
    body (0)

#### RECORD 64 LowReservoir 2015-03-20T20:35:37 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-03-20T20:35:37)
    0000   0x25 0xe3 0x14 0x14 0x0f                   %....
    body (0)

#### RECORD 65 Bolus 2015-03-20T20:48:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 3.5}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x8c 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  140    0
    datetime (2015-03-20T20:48:57)
    0000   0x39 0xf0 0x54 0x74 0x0f                   9.Tt.
    body (0)

#### RECORD 66 SensorAlert 2015-03-20T20:59:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-20T20:59:38)
    0000   0x26 0xfb 0x34 0xb4 0x0f                   &.4..
    body (0)

#### RECORD 67 Bolus 2015-03-20T21:00:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 5.5}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xdc 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  220    0
    datetime (2015-03-20T21:00:17)
    0000   0x11 0xc0 0x55 0x74 0x0f                   ..Ut.
    body (0)

#### RECORD 68 SensorAlert 2015-03-20T21:16:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 186}
```
    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-03-20T21:16:12)
    0000   0x0c 0xd0 0x35 0xb4 0x0f                   ..5..
    body (0)

#### RECORD 69 SensorAlert 2015-03-20T21:27:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-20T21:27:00)
    0000   0x00 0xdb 0x35 0xb4 0x0f                   ..5..
    body (0)

#### RECORD 70 BasalProfileStart 2015-03-20T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-20T22:00:00)
    0000   0x00 0xc0 0x16 0x14 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 71 SensorAlert 2015-03-20T22:27:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-20T22:27:00)
    0000   0x00 0xdb 0x36 0xb4 0x0f                   ..6..
    body (0)

#### RECORD 72 SensorAlert 2015-03-20T22:57:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-20T22:57:00)
    0000   0x00 0xf9 0x36 0xb4 0x0f                   ..6..
    body (0)

#### RECORD 73 CalBGForPH 2015-03-20T23:00:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 323}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2015-03-20T23:00:47)
    0000   0x2f 0xc0 0x37 0x74 0x8f                   /.7t.
    body (0)

#### RECORD 74 BGReceived 2015-03-20T23:00:47 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 323, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x28                                  ?(
    decimal
             63   40
    datetime (2015-03-20T23:00:47)
    0000   0x2f 0xc0 0x77 0x74 0x0f                   /.wt.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 75 BolusWizard 2015-03-20T23:01:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 323,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.4,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 5.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.6}
```
    op hex (2)
    0000   0x5b 0x43                                  [C
    decimal
             91   67
    datetime (2015-03-20T23:01:00)
    0000   0x00 0xc1 0x17 0x14 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xc8 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x40 0x00 0x88 0x78         ...@..x
    decimal
              0   81    0  100   40   90  200    0
              0    0    0   64    0  136  120

#### RECORD 76 UnabsorbedInsulinBolus unknown head[50], body[0] op[0x5c]
###### DECODED
```python
[{'age': 122, 'amount': 1.0},
 {'age': 132, 'amount': 2.4},
 {'age': 142, 'amount': 0.1},
 {'age': 192, 'amount': 0.05},
 {'age': 202, 'amount': 0.4},
 {'age': 212, 'amount': 0.4},
 {'age': 222, 'amount': 0.4},
 {'age': 232, 'amount': 0.4},
 {'age': 242, 'amount': 0.4},
 {'age': 252, 'amount': 0.4},
 {'age': 262, 'amount': 0.4},
 {'age': 272, 'amount': 0.4},
 {'age': 282, 'amount': 1.85},
 {'age': 292, 'amount': 3.9},
 {'age': 352, 'amount': 1.0},
 {'age': 452, 'amount': 0.5}]
```
    op hex (50)
    0000   0x5c 0x32 0x28 0x7a 0x04 0x60 0x84 0x04    \2(z.`..
    0008   0x04 0x8e 0x04 0x02 0xc0 0x04 0x10 0xca    ........
    0010   0x04 0x10 0xd4 0x04 0x10 0xde 0x04 0x10    ........
    0018   0xe8 0x04 0x10 0xf2 0x04 0x10 0xfc 0x04    ........
    0020   0x10 0x06 0x14 0x10 0x10 0x14 0x4a 0x1a    ......J.
    0028   0x14 0x9c 0x24 0x14 0x28 0x60 0x14 0x14    ..$.(`..
    0030   0xc4 0x14                                  ..
    decimal
             92   50   40  122    4   96  132    4
              4  142    4    2  192    4   16  202
              4   16  212    4   16  222    4   16
            232    4   16  242    4   16  252    4
             16    6   20   16   16   20   74   26
             20  156   36   20   40   96   20   20
            196   20
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2015-03-20T23:01:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4,
 'duration': 0,
 'programmed': 3.4,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x40 0x00    ......@.
    decimal
              1    0  136    0  136    0   64    0
    datetime (2015-03-20T23:01:00)
    0000   0x00 0xc1 0x57 0x14 0x0f                   ..W..
    body (0)

#### RECORD 78 SensorAlert 2015-03-20T23:16:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 322}
```
    op hex (3)
    0000   0x0b 0x65 0x42                             .eB
    decimal
             11  101   66
    datetime (2015-03-20T23:16:12)
    0000   0x0c 0xd0 0x37 0xb4 0x8f                   ..7..
    body (0)

#### RECORD 79 BasalProfileStart 2015-03-21T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-21T00:00:00)
    0000   0x00 0xc0 0x00 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 80 MResultTotals 2015-03-21T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xf1                   .....
    decimal
              7    0    0    7  241
    datetime (2015-03-21T00:00:00)
    0000   0x34 0x8f                                  4.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end ReadHistoryData-page-6.data: 81 records`
