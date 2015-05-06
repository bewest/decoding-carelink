## START ReadHistoryData-page-22.data
#### STOPPING DOUBLE NULLS @ 984, found 38 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa1 0x77                                  .w
##### DEBUG DECIMAL
            161  119
#### RECORD 0 Bolus 2015-02-22T10:14:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 4.9}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0xc4 0x00    ........
    decimal
              1    0  140    0  140    0  196    0
    datetime (2015-02-22T10:14:27)
    0000   0x1b 0x8e 0x4a 0x76 0x0f                   ..Jv.
    body (0)

#### RECORD 1 SensorAlert 2015-02-22T10:19:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 233}
```
    op hex (3)
    0000   0x0b 0x65 0xe9                             .e.
    decimal
             11  101  233
    datetime (2015-02-22T10:19:25)
    0000   0x19 0x93 0x2a 0xb6 0x0f                   ..*..
    body (0)

#### RECORD 2 SensorAlert 2015-02-22T11:05:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-22T11:05:20)
    0000   0x14 0x85 0x2b 0xb6 0x0f                   ..+..
    body (0)

#### RECORD 3 SensorAlert 2015-02-22T11:50:13 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 235}
```
    op hex (3)
    0000   0x0b 0x65 0xeb                             .e.
    decimal
             11  101  235
    datetime (2015-02-22T11:50:13)
    0000   0x0d 0xb2 0x2b 0xb6 0x0f                   ..+..
    body (0)

#### RECORD 4 Bolus 2015-02-22T11:50:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 4.3}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xac 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  172    0
    datetime (2015-02-22T11:50:52)
    0000   0x34 0xb2 0x4b 0x76 0x0f                   4.Kv.
    body (0)

#### RECORD 5 BasalProfileStart 2015-02-22T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-22T12:00:00)
    0000   0x00 0x80 0x0c 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 6 SensorAlert 2015-02-22T12:30:13 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-02-22T12:30:13)
    0000   0x0d 0x9e 0x2c 0xb6 0x0f                   ..,..
    body (0)

#### RECORD 7 Bolus 2015-02-22T13:15:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x60 0x00    ..<.<.`.
    decimal
              1    0   60    0   60    0   96    0
    datetime (2015-02-22T13:15:23)
    0000   0x17 0x8f 0x4d 0x76 0x0f                   ..Mv.
    body (0)

#### RECORD 8 BasalProfileStart 2015-02-22T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-22T15:00:00)
    0000   0x00 0x80 0x0f 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 9 Bolus 2015-02-22T15:12:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x24 0x00    ..P.P.$.
    decimal
              1    0   80    0   80    0   36    0
    datetime (2015-02-22T15:12:53)
    0000   0x35 0x8c 0x4f 0x76 0x0f                   5.Ov.
    body (0)

#### RECORD 10 CalBGForPH 2015-02-22T16:16:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2015-02-22T16:16:54)
    0000   0x36 0x90 0x30 0x76 0x0f                   6.0v.
    body (0)

#### RECORD 11 BGReceived 2015-02-22T16:16:54 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 185, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-02-22T16:16:54)
    0000   0x36 0x90 0x30 0x76 0x0f                   6.0v.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 12 BolusWizard 2015-02-22T16:17:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 185,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.3,
 'carb_input': 11,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 1.6,
 'food_estimate': 1.3,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.8}
```
    op hex (2)
    0000   0x5b 0xb9                                  [.
    decimal
             91  185
    datetime (2015-02-22T16:17:13)
    0000   0x0d 0x91 0x10 0x76 0x0f                   ...v.
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x50 0x28 0x5a 0x40 0x00    .P.P(Z@.
    0008   0x34 0x00 0x00 0x48 0x00 0x34 0x78         4..H.4x
    decimal
             11   80    0   80   40   90   64    0
             52    0    0   72    0   52  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 2.0},
 {'age': 181, 'amount': 0.55},
 {'age': 191, 'amount': 0.95},
 {'age': 271, 'amount': 2.0},
 {'age': 361, 'amount': 1.2},
 {'age': 371, 'amount': 5.1},
 {'age': 421, 'amount': 2.5}]
```
    op hex (23)
    0000   0x5c 0x17 0x50 0x47 0x04 0x16 0xb5 0x04    \.PG....
    0008   0x26 0xbf 0x04 0x50 0x0f 0x14 0x30 0x69    &..P..0i
    0010   0x14 0xcc 0x73 0x14 0x64 0xa5 0x14         ..s.d..
    decimal
             92   23   80   71    4   22  181    4
             38  191    4   80   15   20   48  105
             20  204  115   20  100  165   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2015-02-22T16:17:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3,
 'duration': 0,
 'programmed': 1.3,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x48 0x00    ..4.4.H.
    decimal
              1    0   52    0   52    0   72    0
    datetime (2015-02-22T16:17:13)
    0000   0x0d 0x91 0x50 0x76 0x0f                   ..Pv.
    body (0)

#### RECORD 15 Bolus 2015-02-22T18:11:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x28 0x00    ......(.
    decimal
              1    0  180    0  180    0   40    0
    datetime (2015-02-22T18:11:43)
    0000   0x2b 0x8b 0x52 0x76 0x0f                   +.Rv.
    body (0)

#### RECORD 16 BolusWizard 2015-02-22T20:21:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 10.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-22T20:21:50)
    0000   0x32 0x95 0x14 0x76 0x0f                   2..v.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    <P.<(Z..
    0008   0x90 0x00 0x00 0x00 0x01 0x90 0x78         ......x
    decimal
             60   80    0   60   40   90    0    1
            144    0    0    0    1  144  120

#### RECORD 17 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 135, 'amount': 4.5},
 {'age': 245, 'amount': 1.3},
 {'age': 315, 'amount': 2.0},
 {'age': 425, 'amount': 0.55},
 {'age': 435, 'amount': 0.95}]
```
    op hex (17)
    0000   0x5c 0x11 0xb4 0x87 0x04 0x34 0xf5 0x04    \....4..
    0008   0x50 0x3b 0x14 0x16 0xa9 0x14 0x26 0xb3    P;....&.
    0010   0x14                                       .
    decimal
             92   17  180  135    4   52  245    4
             80   59   20   22  169   20   38  179
             20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2015-02-22T20:25:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4,
 'duration': 240,
 'programmed': 4.4,
 'type': 'square',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0xb0 0x00 0xb0 0x00 0x44 0x08    ......D.
    decimal
              1    0  176    0  176    0   68    8
    datetime (2015-02-22T20:25:37)
    0000   0x25 0x99 0xb4 0x76 0x0f                   %..v.
    body (0)

#### RECORD 19 Bolus 2015-02-22T20:21:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6,
 'duration': 0,
 'programmed': 5.6,
 'type': 'normal',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0xe0 0x00 0xe0 0x00 0x44 0x00    ......D.
    decimal
              1    0  224    0  224    0   68    0
    datetime (2015-02-22T20:21:51)
    0000   0x33 0x95 0x94 0x76 0x0f                   3..v.
    body (0)

#### RECORD 20 CalBGForPH 2015-02-22T21:54:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2015-02-22T21:54:48)
    0000   0x30 0xb6 0x35 0x76 0x0f                   0.5v.
    body (0)

#### RECORD 21 BGReceived 2015-02-22T21:54:48 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 180, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-02-22T21:54:48)
    0000   0x30 0xb6 0x95 0x76 0x0f                   0..v.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 22 BasalProfileStart 2015-02-22T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-22T22:00:00)
    0000   0x00 0x80 0x16 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 23 BasalProfileStart 2015-02-23T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-23T00:00:00)
    0000   0x00 0x80 0x00 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 24 MResultTotals 2015-02-23T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0x26                   ....&
    decimal
              7    0    0    9   38
    datetime (2015-02-23T00:00:00)
    0000   0x36 0x0f                                  6.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 25 Sara6E 2015-02-23T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-23T00:00:00)
    0000   0x36 0x0f                                  6.
    body (49)
    hex
    0000   0x05 0x00 0xce 0xb4 0xfe 0x03 0x00 0x00    ........
    0008   0x09 0x26 0x03 0x30 0x23 0x05 0xf6 0x41    .&.0#..A
    0010   0x00 0x47 0x01 0xb2 0x00 0x70 0x00 0x00    .G...p..
    0018   0x03 0xd4 0x02 0x01 0x00 0x09 0x00 0xc8    ........
    0020   0x45 0x1f 0x00 0x8c 0x35 0x01 0x00 0x00    E...5...
    0028   0x00 0x00 0x06 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  206  180  254    3    0    0
              9   38    3   48   35    5  246   65
              0   71    1  178    0  112    0    0
              3  212    2    1    0    9    0  200
             69   31    0  140   53    1    0    0
              0    0    6    0    0    0    0    0
              0

#### RECORD 26 BasalProfileStart 2015-02-23T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-23T04:00:00)
    0000   0x00 0x80 0x04 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 27 BasalProfileStart 2015-02-23T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-23T07:00:00)
    0000   0x00 0x80 0x07 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 28 PumpSuspend 2015-02-23T07:13:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-23T07:13:44)
    0000   0x2c 0x8d 0x07 0x17 0x0f                   ,....
    body (0)

#### RECORD 29 BasalProfileStart 2015-02-23T07:32:15 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-23T07:32:15)
    0000   0x0f 0xa0 0x07 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 30 PumpResume 2015-02-23T07:32:15 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-23T07:32:15)
    0000   0x0f 0xa0 0x07 0x17 0x0f                   .....
    body (0)

#### RECORD 31 BolusWizard 2015-02-23T07:56:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-23T07:56:43)
    0000   0x2b 0xb8 0x07 0x77 0x0f                   +..w.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    (P.d(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             40   80    0  100   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 32 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 460, 'amount': 0.2}, {'age': 470, 'amount': 0.15}]
```
    op hex (8)
    0000   0x5c 0x08 0x08 0xcc 0x14 0x06 0xd6 0x14    \.......
    decimal
             92    8    8  204   20    6  214   20
    datetime (unknown)

    body (0)

#### RECORD 33 BolusWizard 2015-02-23T07:56:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-23T07:56:45)
    0000   0x2d 0xb8 0x07 0x77 0x0f                   -..w.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    (P.d(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             40   80    0  100   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 34 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 460, 'amount': 0.2}, {'age': 470, 'amount': 0.15}]
```
    op hex (8)
    0000   0x5c 0x08 0x08 0xcc 0x14 0x06 0xd6 0x14    \.......
    decimal
             92    8    8  204   20    6  214   20
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2015-02-23T07:56:45 head[8], body[0] op[0x01]
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
    datetime (2015-02-23T07:56:45)
    0000   0x2d 0xb8 0x47 0x77 0x0f                   -.Gw.
    body (0)

#### RECORD 36 BasalProfileStart 2015-02-23T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-23T10:00:00)
    0000   0x00 0x80 0x0a 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 37 SensorAlert 2015-02-23T11:27:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-23T11:27:42)
    0000   0x2a 0x9b 0x2b 0xb7 0x0f                   *.+..
    body (0)

#### RECORD 38 CalBGForPH 2015-02-23T11:28:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 355}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2015-02-23T11:28:36)
    0000   0x24 0x9c 0x2b 0x77 0x8f                   $.+w.
    body (0)

#### RECORD 39 BGReceived 2015-02-23T11:28:36 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 355, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2c                                  ?,
    decimal
             63   44
    datetime (2015-02-23T11:28:36)
    0000   0x24 0x9c 0x6b 0x77 0x0f                   $.kw.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 40 BolusWizard 2015-02-23T11:28:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 355,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.4,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': -0.6,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0x63                                  [c
    decimal
             91   99
    datetime (2015-02-23T11:28:48)
    0000   0x30 0x9c 0x0b 0x77 0x0f                   0..w.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xe8 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x10 0x00 0xd8 0x78         ......x
    decimal
              0   81    0  100   40   90  232    0
              0    0    0   16    0  216  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 212, 'amount': 4.0}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0xd4 0x04                   \....
    decimal
             92    5  160  212    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2015-02-23T11:28:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4,
 'duration': 0,
 'programmed': 5.4,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0xd8 0x00 0xd8 0x00 0x10 0x00    ........
    decimal
              1    0  216    0  216    0   16    0
    datetime (2015-02-23T11:28:48)
    0000   0x30 0x9c 0x4b 0x77 0x0f                   0.Kw.
    body (0)

#### RECORD 43 SensorAlert 2015-02-23T11:43:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 355}
```
    op hex (3)
    0000   0x0b 0x65 0x63                             .ec
    decimal
             11  101   99
    datetime (2015-02-23T11:43:18)
    0000   0x12 0xab 0x2b 0xb7 0x8f                   ..+..
    body (0)

#### RECORD 44 BolusWizard 2015-02-23T11:43:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 7.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-23T11:43:58)
    0000   0x3a 0xab 0x0b 0x77 0x0f                   :..w.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 45 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 5.4}, {'age': 227, 'amount': 4.0}]
```
    op hex (8)
    0000   0x5c 0x08 0xd8 0x11 0x04 0xa0 0xe3 0x04    \.......
    decimal
             92    8  216   17    4  160  227    4
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2015-02-23T11:47:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 60,
 'programmed': 2.5,
 'type': 'square',
 'unabsorbed': 5.6}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xe0 0x02    ..d.d...
    decimal
              1    0  100    0  100    0  224    2
    datetime (2015-02-23T11:47:20)
    0000   0x14 0xaf 0xab 0x77 0x0f                   ...w.
    body (0)

#### RECORD 47 Bolus 2015-02-23T11:43:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 5.6}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0xe0 0x00    ........
    decimal
              1    0  200    0  200    0  224    0
    datetime (2015-02-23T11:43:58)
    0000   0x3a 0xab 0x8b 0x77 0x0f                   :..w.
    body (0)

#### RECORD 48 BasalProfileStart 2015-02-23T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-23T12:00:00)
    0000   0x00 0x80 0x0c 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 49 Bolus 2015-02-23T12:28:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 4.1}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x01 0xa4 0x00    ........
    decimal
              1    0  140    0  140    1  164    0
    datetime (2015-02-23T12:28:37)
    0000   0x25 0x9c 0x4c 0x77 0x0f                   %.Lw.
    body (0)

#### RECORD 50 SensorAlert 2015-02-23T13:13:09 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 285}
```
    op hex (3)
    0000   0x0b 0x65 0x1d                             .e.
    decimal
             11  101   29
    datetime (2015-02-23T13:13:09)
    0000   0x09 0x8d 0x2d 0xb7 0x8f                   ..-..
    body (0)

#### RECORD 51 SensorAlert 2015-02-23T14:42:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 200}
```
    op hex (3)
    0000   0x0b 0x65 0xc8                             .e.
    decimal
             11  101  200
    datetime (2015-02-23T14:42:20)
    0000   0x14 0xaa 0x2e 0xb7 0x0f                   .....
    body (0)

#### RECORD 52 BasalProfileStart 2015-02-23T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-23T15:00:00)
    0000   0x00 0x80 0x0f 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 53 SensorAlert 2015-02-23T16:13:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 277}
```
    op hex (3)
    0000   0x0b 0x65 0x15                             .e.
    decimal
             11  101   21
    datetime (2015-02-23T16:13:37)
    0000   0x25 0x8d 0x30 0xb7 0x8f                   %.0..
    body (0)

#### RECORD 54 Bolus 2015-02-23T16:15:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x10 0x00    ........
    decimal
              1    0  200    0  200    0   16    0
    datetime (2015-02-23T16:15:30)
    0000   0x1e 0x8f 0x50 0x77 0x0f                   ..Pw.
    body (0)

#### RECORD 55 SensorAlert 2015-02-23T16:28:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-23T16:28:00)
    0000   0x00 0x9c 0x30 0xb7 0x0f                   ..0..
    body (0)

#### RECORD 56 SensorAlert 2015-02-23T17:28:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-23T17:28:00)
    0000   0x00 0x9c 0x31 0xb7 0x0f                   ..1..
    body (0)

#### RECORD 57 CalBGForPH 2015-02-23T17:31:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 205}
```
    op hex (2)
    0000   0x0a 0xcd                                  ..
    decimal
             10  205
    datetime (2015-02-23T17:31:46)
    0000   0x2e 0x9f 0x31 0x77 0x0f                   ..1w.
    body (0)

#### RECORD 58 BGReceived 2015-02-23T17:31:46 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 205, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2015-02-23T17:31:46)
    0000   0x2e 0x9f 0xb1 0x77 0x0f                   ...w.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 59 Bolus 2015-02-23T17:32:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 3.7}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x94 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  148    0
    datetime (2015-02-23T17:32:26)
    0000   0x1a 0xa0 0x51 0x77 0x0f                   ..Qw.
    body (0)

#### RECORD 60 SensorAlert 2015-02-23T17:47:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 237}
```
    op hex (3)
    0000   0x0b 0x65 0xed                             .e.
    decimal
             11  101  237
    datetime (2015-02-23T17:47:01)
    0000   0x01 0xaf 0x31 0xb7 0x0f                   ..1..
    body (0)

#### RECORD 61 Bolus 2015-02-23T18:02:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 4.6}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xb8 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  184    0
    datetime (2015-02-23T18:02:08)
    0000   0x08 0x82 0x52 0x77 0x0f                   ..Rw.
    body (0)

#### RECORD 62 BolusWizard 2015-02-23T19:29:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.2,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 6.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-23T19:29:09)
    0000   0x09 0x9d 0x13 0x77 0x0f                   ...w.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    (P.<(Z..
    0008   0x08 0x00 0x00 0x00 0x01 0x08 0x78         ......x
    decimal
             40   80    0   60   40   90    0    1
              8    0    0    0    1    8  120

#### RECORD 63 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 3.0},
 {'age': 123, 'amount': 2.0},
 {'age': 193, 'amount': 4.25},
 {'age': 203, 'amount': 0.75},
 {'age': 403, 'amount': 0.15},
 {'age': 413, 'amount': 0.4},
 {'age': 423, 'amount': 3.85},
 {'age': 433, 'amount': 0.4},
 {'age': 443, 'amount': 0.4},
 {'age': 453, 'amount': 0.45},
 {'age': 463, 'amount': 2.35},
 {'age': 473, 'amount': 3.0}]
```
    op hex (38)
    0000   0x5c 0x26 0x78 0x5d 0x04 0x50 0x7b 0x04    \&x].P{.
    0008   0xaa 0xc1 0x04 0x1e 0xcb 0x04 0x06 0x93    ........
    0010   0x14 0x10 0x9d 0x14 0x9a 0xa7 0x14 0x10    ........
    0018   0xb1 0x14 0x10 0xbb 0x14 0x12 0xc5 0x14    ........
    0020   0x5e 0xcf 0x14 0x78 0xd9 0x14              ^..x..
    decimal
             92   38  120   93    4   80  123    4
            170  193    4   30  203    4    6  147
             20   16  157   20  154  167   20   16
            177   20   16  187   20   18  197   20
             94  207   20  120  217   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2015-02-23T19:29:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2,
 'duration': 0,
 'programmed': 0.2,
 'type': 'normal',
 'unabsorbed': 3.5}
```
    op hex (8)
    0000   0x01 0x01 0x08 0x01 0x08 0x00 0x8c 0x00    ........
    decimal
              1    1    8    1    8    0  140    0
    datetime (2015-02-23T19:29:09)
    0000   0x09 0x9d 0x53 0x77 0x0f                   ..Sw.
    body (0)

#### RECORD 65 SensorAlert 2015-02-23T19:43:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-23T19:43:18)
    0000   0x12 0xab 0x33 0xb7 0x0f                   ..3..
    body (0)

#### RECORD 66 Bolus 2015-02-23T20:13:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 1.2}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x01 0x30 0x00    ..d.d.0.
    decimal
              1    0  100    0  100    1   48    0
    datetime (2015-02-23T20:13:27)
    0000   0x1b 0x8d 0x54 0x77 0x0f                   ..Tw.
    body (0)

#### RECORD 67 BolusWizard 2015-02-23T20:55:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.2,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 6.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-23T20:55:11)
    0000   0x0b 0xb7 0x14 0x77 0x0f                   ...w.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    (P.<(Z..
    0008   0x08 0x00 0x00 0x00 0x01 0x08 0x78         ......x
    decimal
             40   80    0   60   40   90    0    1
              8    0    0    0    1    8  120

#### RECORD 68 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 2.5},
 {'age': 89, 'amount': 0.2},
 {'age': 179, 'amount': 3.0},
 {'age': 209, 'amount': 2.0},
 {'age': 279, 'amount': 4.25},
 {'age': 289, 'amount': 0.75}]
```
    op hex (20)
    0000   0x5c 0x14 0x64 0x31 0x04 0x08 0x59 0x05    \.d1..Y.
    0008   0x78 0xb3 0x04 0x50 0xd1 0x04 0xaa 0x17    x..P....
    0010   0x14 0x1e 0x21 0x14                        ..!.
    decimal
             92   20  100   49    4    8   89    5
            120  179    4   80  209    4  170   23
             20   30   33   20
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2015-02-23T20:55:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2,
 'duration': 150,
 'programmed': 0.2,
 'type': 'square',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x01 0x08 0x01 0x08 0x01 0x24 0x05    ......$.
    decimal
              1    1    8    1    8    1   36    5
    datetime (2015-02-23T20:55:11)
    0000   0x0b 0xb7 0x74 0x77 0x0f                   ..tw.
    body (0)

#### RECORD 70 SensorAlert 2015-02-23T21:17:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-23T21:17:03)
    0000   0x03 0x91 0x35 0xb7 0x0f                   ..5..
    body (0)

#### RECORD 71 SensorAlert 2015-02-23T21:27:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-23T21:27:42)
    0000   0x2a 0x9b 0x35 0xb7 0x0f                   *.5..
    body (0)

#### RECORD 72 BasalProfileStart 2015-02-23T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-23T22:00:00)
    0000   0x00 0x80 0x16 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 73 SensorAlert 2015-02-23T22:58:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 233}
```
    op hex (3)
    0000   0x0b 0x65 0xe9                             .e.
    decimal
             11  101  233
    datetime (2015-02-23T22:58:47)
    0000   0x2f 0xba 0x36 0xb7 0x0f                   /.6..
    body (0)

#### RECORD 74 Bolus 2015-02-23T22:59:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 5.3}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0xd4 0x00    ........
    decimal
              1    0  140    0  140    0  212    0
    datetime (2015-02-23T22:59:19)
    0000   0x13 0xbb 0x56 0x77 0x0f                   ..Vw.
    body (0)

#### RECORD 75 CalBGForPH 2015-02-23T23:18:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 145}
```
    op hex (2)
    0000   0x0a 0x91                                  ..
    decimal
             10  145
    datetime (2015-02-23T23:18:24)
    0000   0x18 0x92 0x37 0x77 0x0f                   ..7w.
    body (0)

#### RECORD 76 BGReceived 2015-02-23T23:18:24 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 145, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2015-02-23T23:18:24)
    0000   0x18 0x92 0x37 0x77 0x0f                   ..7w.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 77 BasalProfileStart 2015-02-24T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-24T00:00:00)
    0000   0x00 0x80 0x00 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 78 MResultTotals 2015-02-24T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0xf7                   .....
    decimal
              7    0    0   10  247
    datetime (2015-02-24T00:00:00)
    0000   0x37 0x0f                                  7.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end ReadHistoryData-page-22.data: 79 records`
