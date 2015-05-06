## START ReadHistoryData-page-32.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x4b 0x44                                  KD
##### DEBUG DECIMAL
             75   68
#### RECORD 0 BasalProfileStart 2015-02-10T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-10T12:00:00)
    0000   0x00 0x80 0x0c 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 1 SensorAlert 2015-02-10T12:53:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-10T12:53:03)
    0000   0x03 0xb5 0x2c 0xaa 0x0f                   ..,..
    body (0)

#### RECORD 2 SensorAlert 2015-02-10T13:03:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 187}
```
    op hex (3)
    0000   0x0b 0x65 0xbb                             .e.
    decimal
             11  101  187
    datetime (2015-02-10T13:03:42)
    0000   0x2a 0x83 0x2d 0xaa 0x0f                   *.-..
    body (0)

#### RECORD 3 SensorAlert 2015-02-10T14:34:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 303}
```
    op hex (3)
    0000   0x0b 0x65 0x2f                             .e/
    decimal
             11  101   47
    datetime (2015-02-10T14:34:30)
    0000   0x1e 0xa2 0x2e 0xaa 0x8f                   .....
    body (0)

#### RECORD 4 BolusWizard 2015-02-10T14:34:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.4,
 'carb_input': 55,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 6.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-10T14:34:50)
    0000   0x32 0xa2 0x0e 0x6a 0x0f                   2..j.
    body (15)
    hex
    0000   0x37 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    7P.P(Z..
    0008   0x10 0x00 0x00 0x00 0x01 0x10 0x78         ......x
    decimal
             55   80    0   80   40   90    0    1
             16    0    0    0    1   16  120

#### RECORD 5 UnabsorbedInsulinBolus unknown head[53], body[0] op[0x5c]
###### DECODED
```python
[{'age': 198, 'amount': 1.35},
 {'age': 208, 'amount': 1.15},
 {'age': 248, 'amount': 2.0},
 {'age': 288, 'amount': 0.05},
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
 {'age': 408, 'amount': 4.7},
 {'age': 418, 'amount': 0.4}]
```
    op hex (53)
    0000   0x5c 0x35 0x36 0xc6 0x04 0x2e 0xd0 0x04    \56.....
    0008   0x50 0xf8 0x04 0x02 0x20 0x14 0x06 0x2a    P... ..*
    0010   0x14 0x08 0x34 0x14 0x06 0x3e 0x14 0x06    ..4..>..
    0018   0x48 0x14 0x08 0x52 0x14 0x06 0x5c 0x14    H..R..\.
    0020   0x06 0x66 0x14 0x08 0x70 0x14 0x06 0x7a    .f..p..z
    0028   0x14 0x06 0x84 0x14 0x08 0x8e 0x14 0xbc    ........
    0030   0x98 0x14 0x10 0xa2 0x14                   .....
    decimal
             92   53   54  198    4   46  208    4
             80  248    4    2   32   20    6   42
             20    8   52   20    6   62   20    6
             72   20    8   82   20    6   92   20
              6  102   20    8  112   20    6  122
             20    6  132   20    8  142   20  188
            152   20   16  162   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2015-02-10T14:34:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4,
 'duration': 0,
 'programmed': 0.4,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x01 0x10 0x01 0x10 0x00 0x0c 0x00    ........
    decimal
              1    1   16    1   16    0   12    0
    datetime (2015-02-10T14:34:50)
    0000   0x32 0xa2 0x4e 0x6a 0x0f                   2.Nj.
    body (0)

#### RECORD 7 BasalProfileStart 2015-02-10T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-10T15:00:00)
    0000   0x00 0x80 0x0f 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 8 Bolus 2015-02-10T15:04:57 head[8], body[0] op[0x01]
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
    datetime (2015-02-10T15:04:57)
    0000   0x39 0x84 0x4f 0x6a 0x0f                   9.Oj.
    body (0)

#### RECORD 9 SensorAlert 2015-02-10T15:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-10T15:36:00)
    0000   0x00 0xa4 0x2f 0xaa 0x0f                   ../..
    body (0)

#### RECORD 10 SensorAlert 2015-02-10T16:03:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 225}
```
    op hex (3)
    0000   0x0b 0x65 0xe1                             .e.
    decimal
             11  101  225
    datetime (2015-02-10T16:03:01)
    0000   0x01 0x83 0x30 0xaa 0x0f                   ..0..
    body (0)

#### RECORD 11 SensorAlert 2015-02-10T16:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-10T16:36:00)
    0000   0x00 0xa4 0x30 0xaa 0x0f                   ..0..
    body (0)

#### RECORD 12 CalBGForPH 2015-02-10T16:37:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 179}
```
    op hex (2)
    0000   0x0a 0xb3                                  ..
    decimal
             10  179
    datetime (2015-02-10T16:37:52)
    0000   0x34 0xa5 0x30 0x6a 0x0f                   4.0j.
    body (0)

#### RECORD 13 BGReceived 2015-02-10T16:37:52 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 179, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-02-10T16:37:52)
    0000   0x34 0xa5 0x70 0x6a 0x0f                   4.pj.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 14 SensorAlert 2015-02-10T16:53:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-10T16:53:03)
    0000   0x03 0xb5 0x30 0xaa 0x0f                   ..0..
    body (0)

#### RECORD 15 SensorAlert 2015-02-10T17:59:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-10T17:59:18)
    0000   0x12 0xbb 0x31 0xaa 0x0f                   ..1..
    body (0)

#### RECORD 16 SensorAlert 2015-02-10T18:23:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-02-10T18:23:42)
    0000   0x2a 0x97 0x32 0xaa 0x0f                   *.2..
    body (0)

#### RECORD 17 SensorAlert 2015-02-10T19:54:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 284}
```
    op hex (3)
    0000   0x0b 0x65 0x1c                             .e.
    decimal
             11  101   28
    datetime (2015-02-10T19:54:30)
    0000   0x1e 0xb6 0x33 0xaa 0x8f                   ..3..
    body (0)

#### RECORD 18 BolusWizard 2015-02-10T19:54:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.9,
 'carb_input': 62,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 10.3,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-10T19:54:51)
    0000   0x33 0xb6 0x13 0x6a 0x0f                   3..j.
    body (15)
    hex
    0000   0x3e 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    >P.<(Z..
    0008   0x9c 0x00 0x00 0x00 0x01 0x9c 0x78         ......x
    decimal
             62   80    0   60   40   90    0    1
            156    0    0    0    1  156  120

#### RECORD 19 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 288, 'amount': 0.5},
 {'age': 298, 'amount': 1.5},
 {'age': 318, 'amount': 5.05},
 {'age': 328, 'amount': 1.75}]
```
    op hex (14)
    0000   0x5c 0x0e 0x14 0x20 0x14 0x3c 0x2a 0x14    \.. .<*.
    0008   0xca 0x3e 0x14 0x46 0x48 0x14              .>.FH.
    decimal
             92   14   20   32   20   60   42   20
            202   62   20   70   72   20
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2015-02-10T19:58:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3,
 'duration': 60,
 'programmed': 4.3,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0x00 0x02    ........
    decimal
              1    0  172    0  172    0    0    2
    datetime (2015-02-10T19:58:54)
    0000   0x36 0xba 0xb3 0x6a 0x0f                   6..j.
    body (0)

#### RECORD 21 Bolus 2015-02-10T19:54:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0x00 0x00    ........
    decimal
              1    0  240    0  240    0    0    0
    datetime (2015-02-10T19:54:52)
    0000   0x34 0xb6 0x93 0x6a 0x0f                   4..j.
    body (0)

#### RECORD 22 LowReservoir 2015-02-10T20:00:39 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-02-10T20:00:39)
    0000   0x27 0x80 0x14 0x0a 0x0f                   '....
    body (0)

#### RECORD 23 SensorAlert 2015-02-10T21:23:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 216}
```
    op hex (3)
    0000   0x0b 0x65 0xd8                             .e.
    decimal
             11  101  216
    datetime (2015-02-10T21:23:01)
    0000   0x01 0x97 0x35 0xaa 0x0f                   ..5..
    body (0)

#### RECORD 24 BasalProfileStart 2015-02-10T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-10T22:00:00)
    0000   0x00 0x80 0x16 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 25 Bolus 2015-02-10T22:09:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 4.6}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xb8 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  184    0
    datetime (2015-02-10T22:09:40)
    0000   0x28 0x89 0x56 0x6a 0x0f                   (.Vj.
    body (0)

#### RECORD 26 SensorAlert 2015-02-10T22:53:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 211}
```
    op hex (3)
    0000   0x0b 0x65 0xd3                             .e.
    decimal
             11  101  211
    datetime (2015-02-10T22:53:03)
    0000   0x03 0xb5 0x36 0xaa 0x0f                   ..6..
    body (0)

#### RECORD 27 CalBGForPH 2015-02-10T23:13:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 252}
```
    op hex (2)
    0000   0x0a 0xfc                                  ..
    decimal
             10  252
    datetime (2015-02-10T23:13:38)
    0000   0x26 0x8d 0x37 0x6a 0x0f                   &.7j.
    body (0)

#### RECORD 28 BGReceived 2015-02-10T23:13:38 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 252, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1f                                  ?.
    decimal
             63   31
    datetime (2015-02-10T23:13:38)
    0000   0x26 0x8d 0x97 0x6a 0x0f                   &..j.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 29 BolusWizard 2015-02-10T23:14:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 252,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': -3.1,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 2.9}
```
    op hex (2)
    0000   0x5b 0xfc                                  [.
    decimal
             91  252
    datetime (2015-02-10T23:14:14)
    0000   0x0e 0x8e 0x17 0x0a 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x84 0x00    .P.d(Z..
    0008   0x00 0x00 0x00 0x74 0x00 0x10 0x78         ...t..x
    decimal
              0   80    0  100   40   90  132    0
              0    0    0  116    0   16  120

#### RECORD 30 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 1.5},
 {'age': 138, 'amount': 0.2},
 {'age': 148, 'amount': 0.75},
 {'age': 158, 'amount': 0.7},
 {'age': 168, 'amount': 0.7},
 {'age': 178, 'amount': 0.75},
 {'age': 188, 'amount': 0.7},
 {'age': 198, 'amount': 4.8},
 {'age': 208, 'amount': 1.7}]
```
    op hex (29)
    0000   0x5c 0x1d 0x3c 0x44 0x04 0x08 0x8a 0x04    \.<D....
    0008   0x1e 0x94 0x04 0x1c 0x9e 0x04 0x1c 0xa8    ........
    0010   0x04 0x1e 0xb2 0x04 0x1c 0xbc 0x04 0xc0    ........
    0018   0xc6 0x04 0x44 0xd0 0x04                   ..D..
    decimal
             92   29   60   68    4    8  138    4
             30  148    4   28  158    4   28  168
              4   30  178    4   28  188    4  192
            198    4   68  208    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2015-02-10T23:14:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3,
 'duration': 180,
 'programmed': 3.3,
 'type': 'square',
 'unabsorbed': 2.9}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x74 0x06    ......t.
    decimal
              1    0  132    0  132    0  116    6
    datetime (2015-02-10T23:14:57)
    0000   0x39 0x8e 0xb7 0x0a 0x0f                   9....
    body (0)

#### RECORD 32 Bolus 2015-02-10T23:14:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1,
 'duration': 0,
 'programmed': 1.1,
 'type': 'normal',
 'unabsorbed': 2.9}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x74 0x00    ..,.,.t.
    decimal
              1    0   44    0   44    0  116    0
    datetime (2015-02-10T23:14:15)
    0000   0x0f 0x8e 0x97 0x0a 0x0f                   .....
    body (0)

#### RECORD 33 LowReservoir 2015-02-10T23:29:57 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-02-10T23:29:57)
    0000   0x39 0x9d 0x17 0x0a 0x0f                   9....
    body (0)

#### RECORD 34 BasalProfileStart 2015-02-11T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-11T00:00:00)
    0000   0x00 0x80 0x00 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 35 MResultTotals 2015-02-11T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0x0b                   .....
    decimal
              7    0    0   10   11
    datetime (2015-02-11T00:00:00)
    0000   0x2a 0x0f                                  *.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 36 Sara6E 2015-02-11T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-11T00:00:00)
    0000   0x2a 0x0f                                  *.
    body (49)
    hex
    0000   0x05 0x00 0xe1 0xb3 0xfc 0x03 0x00 0x00    ........
    0008   0x0a 0x0b 0x03 0x25 0x1f 0x06 0xe6 0x45    ...%...E
    0010   0x00 0xbb 0x04 0x28 0x00 0x8e 0x00 0x00    ...(....
    0018   0x02 0x30 0x03 0x02 0x00 0x06 0x00 0xe2    .0......
    0020   0x52 0x12 0x00 0x1d 0x2e 0x04 0x00 0x00    R.......
    0028   0x00 0x00 0x0f 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  225  179  252    3    0    0
             10   11    3   37   31    6  230   69
              0  187    4   40    0  142    0    0
              2   48    3    2    0    6    0  226
             82   18    0   29   46    4    0    0
              0    0   15    1    0    0    0    0
              0

#### RECORD 37 SensorAlert 2015-02-11T00:23:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 245}
```
    op hex (3)
    0000   0x0b 0x65 0xf5                             .e.
    decimal
             11  101  245
    datetime (2015-02-11T00:23:42)
    0000   0x2a 0x97 0x20 0xab 0x0f                   *. ..
    body (0)

#### RECORD 38 SensorAlert 2015-02-11T01:54:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 219}
```
    op hex (3)
    0000   0x0b 0x65 0xdb                             .e.
    decimal
             11  101  219
    datetime (2015-02-11T01:54:30)
    0000   0x1e 0xb6 0x21 0xab 0x0f                   ..!..
    body (0)

#### RECORD 39 SensorAlert 2015-02-11T03:23:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 204}
```
    op hex (3)
    0000   0x0b 0x65 0xcc                             .e.
    decimal
             11  101  204
    datetime (2015-02-11T03:23:01)
    0000   0x01 0x97 0x23 0xab 0x0f                   ..#..
    body (0)

#### RECORD 40 Bolus 2015-02-11T03:34:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x24 0x00    ..(.(.$.
    decimal
              1    0   40    0   40    0   36    0
    datetime (2015-02-11T03:34:26)
    0000   0x1a 0xa2 0x43 0x6b 0x0f                   ..Ck.
    body (0)

#### RECORD 41 BasalProfileStart 2015-02-11T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-11T04:00:00)
    0000   0x00 0x80 0x04 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 42 SensorAlert 2015-02-11T04:53:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 186}
```
    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-02-11T04:53:03)
    0000   0x03 0xb5 0x24 0xab 0x0f                   ..$..
    body (0)

#### RECORD 43 Bolus 2015-02-11T04:54:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x24 0x00    ..(.(.$.
    decimal
              1    0   40    0   40    0   36    0
    datetime (2015-02-11T04:54:23)
    0000   0x17 0xb6 0x44 0x6b 0x0f                   ..Dk.
    body (0)

#### RECORD 44 PumpSuspend 2015-02-11T06:55:03 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-11T06:55:03)
    0000   0x03 0xb7 0x06 0x0b 0x0f                   .....
    body (0)

#### RECORD 45 BasalProfileStart 2015-02-11T07:24:09 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-11T07:24:09)
    0000   0x09 0x98 0x07 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 46 PumpResume 2015-02-11T07:24:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-11T07:24:09)
    0000   0x09 0x98 0x07 0x0b 0x0f                   .....
    body (0)

#### RECORD 47 BasalProfileStart 2015-02-11T07:24:27 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-11T07:24:27)
    0000   0x1b 0x98 0x07 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 48 Prime 2015-02-11T07:24:13 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-02-11T07:24:13)
    0000   0x0d 0x98 0x07 0x0b 0x0f                   .....
    body (0)

#### RECORD 49 BolusWizard 2015-02-11T07:25:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-11T07:25:09)
    0000   0x09 0x99 0x07 0x6b 0x0f                   ...k.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    -P.d(Z..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x78         ......x
    decimal
             45   80    0  100   40   90    0    0
            180    0    0    0    0  180  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[59], body[0] op[0x5c]
###### DECODED
```python
[{'age': 159, 'amount': 1.0},
 {'age': 239, 'amount': 1.0},
 {'age': 319, 'amount': 0.15},
 {'age': 329, 'amount': 0.2},
 {'age': 339, 'amount': 0.2},
 {'age': 349, 'amount': 0.15},
 {'age': 359, 'amount': 0.2},
 {'age': 369, 'amount': 0.2},
 {'age': 379, 'amount': 0.15},
 {'age': 389, 'amount': 0.2},
 {'age': 399, 'amount': 0.2},
 {'age': 409, 'amount': 0.15},
 {'age': 419, 'amount': 0.2},
 {'age': 429, 'amount': 0.2},
 {'age': 439, 'amount': 0.15},
 {'age': 449, 'amount': 0.2},
 {'age': 459, 'amount': 0.2},
 {'age': 469, 'amount': 0.15},
 {'age': 479, 'amount': 0.2}]
```
    op hex (59)
    0000   0x5c 0x3b 0x28 0x9f 0x04 0x28 0xef 0x04    \;(..(..
    0008   0x06 0x3f 0x14 0x08 0x49 0x14 0x08 0x53    .?..I..S
    0010   0x14 0x06 0x5d 0x14 0x08 0x67 0x14 0x08    ..]..g..
    0018   0x71 0x14 0x06 0x7b 0x14 0x08 0x85 0x14    q..{....
    0020   0x08 0x8f 0x14 0x06 0x99 0x14 0x08 0xa3    ........
    0028   0x14 0x08 0xad 0x14 0x06 0xb7 0x14 0x08    ........
    0030   0xc1 0x14 0x08 0xcb 0x14 0x06 0xd5 0x14    ........
    0038   0x08 0xdf 0x14                             ...
    decimal
             92   59   40  159    4   40  239    4
              6   63   20    8   73   20    8   83
             20    6   93   20    8  103   20    8
            113   20    6  123   20    8  133   20
              8  143   20    6  153   20    8  163
             20    8  173   20    6  183   20    8
            193   20    8  203   20    6  213   20
              8  223   20
    datetime (unknown)

    body (0)

#### RECORD 51 BolusWizard 2015-02-11T07:25:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-11T07:25:10)
    0000   0x0a 0x99 0x07 0x6b 0x0f                   ...k.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    -P.d(Z..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x78         ......x
    decimal
             45   80    0  100   40   90    0    0
            180    0    0    0    0  180  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[59], body[0] op[0x5c]
###### DECODED
```python
[{'age': 159, 'amount': 1.0},
 {'age': 239, 'amount': 1.0},
 {'age': 319, 'amount': 0.15},
 {'age': 329, 'amount': 0.2},
 {'age': 339, 'amount': 0.2},
 {'age': 349, 'amount': 0.15},
 {'age': 359, 'amount': 0.2},
 {'age': 369, 'amount': 0.2},
 {'age': 379, 'amount': 0.15},
 {'age': 389, 'amount': 0.2},
 {'age': 399, 'amount': 0.2},
 {'age': 409, 'amount': 0.15},
 {'age': 419, 'amount': 0.2},
 {'age': 429, 'amount': 0.2},
 {'age': 439, 'amount': 0.15},
 {'age': 449, 'amount': 0.2},
 {'age': 459, 'amount': 0.2},
 {'age': 469, 'amount': 0.15},
 {'age': 479, 'amount': 0.2}]
```
    op hex (59)
    0000   0x5c 0x3b 0x28 0x9f 0x04 0x28 0xef 0x04    \;(..(..
    0008   0x06 0x3f 0x14 0x08 0x49 0x14 0x08 0x53    .?..I..S
    0010   0x14 0x06 0x5d 0x14 0x08 0x67 0x14 0x08    ..]..g..
    0018   0x71 0x14 0x06 0x7b 0x14 0x08 0x85 0x14    q..{....
    0020   0x08 0x8f 0x14 0x06 0x99 0x14 0x08 0xa3    ........
    0028   0x14 0x08 0xad 0x14 0x06 0xb7 0x14 0x08    ........
    0030   0xc1 0x14 0x08 0xcb 0x14 0x06 0xd5 0x14    ........
    0038   0x08 0xdf 0x14                             ...
    decimal
             92   59   40  159    4   40  239    4
              6   63   20    8   73   20    8   83
             20    6   93   20    8  103   20    8
            113   20    6  123   20    8  133   20
              8  143   20    6  153   20    8  163
             20    8  173   20    6  183   20    8
            193   20    8  203   20    6  213   20
              8  223   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2015-02-11T07:25:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x0c 0x00    ........
    decimal
              1    0  180    0  180    0   12    0
    datetime (2015-02-11T07:25:10)
    0000   0x0a 0x99 0x47 0x6b 0x0f                   ..Gk.
    body (0)

#### RECORD 54 BolusWizard 2015-02-11T07:34:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.5,
 'carb_input': 35,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 3.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-11T07:34:28)
    0000   0x1c 0xa2 0x07 0x6b 0x0f                   ...k.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    #P.d(Z..
    0008   0x8c 0x00 0x00 0x00 0x00 0x8c 0x78         ......x
    decimal
             35   80    0  100   40   90    0    0
            140    0    0    0    0  140  120

#### RECORD 55 UnabsorbedInsulinBolus unknown head[62], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 3.25},
 {'age': 18, 'amount': 1.25},
 {'age': 168, 'amount': 1.0},
 {'age': 248, 'amount': 1.0},
 {'age': 328, 'amount': 0.15},
 {'age': 338, 'amount': 0.2},
 {'age': 348, 'amount': 0.2},
 {'age': 358, 'amount': 0.15},
 {'age': 368, 'amount': 0.2},
 {'age': 378, 'amount': 0.2},
 {'age': 388, 'amount': 0.15},
 {'age': 398, 'amount': 0.2},
 {'age': 408, 'amount': 0.2},
 {'age': 418, 'amount': 0.15},
 {'age': 428, 'amount': 0.2},
 {'age': 438, 'amount': 0.2},
 {'age': 448, 'amount': 0.15},
 {'age': 458, 'amount': 0.2},
 {'age': 468, 'amount': 0.2},
 {'age': 478, 'amount': 0.15}]
```
    op hex (62)
    0000   0x5c 0x3e 0x82 0x08 0x04 0x32 0x12 0x04    \>...2..
    0008   0x28 0xa8 0x04 0x28 0xf8 0x04 0x06 0x48    (..(...H
    0010   0x14 0x08 0x52 0x14 0x08 0x5c 0x14 0x06    ..R..\..
    0018   0x66 0x14 0x08 0x70 0x14 0x08 0x7a 0x14    f..p..z.
    0020   0x06 0x84 0x14 0x08 0x8e 0x14 0x08 0x98    ........
    0028   0x14 0x06 0xa2 0x14 0x08 0xac 0x14 0x08    ........
    0030   0xb6 0x14 0x06 0xc0 0x14 0x08 0xca 0x14    ........
    0038   0x08 0xd4 0x14 0x06 0xde 0x14              ......
    decimal
             92   62  130    8    4   50   18    4
             40  168    4   40  248    4    6   72
             20    8   82   20    8   92   20    6
            102   20    8  112   20    8  122   20
              6  132   20    8  142   20    8  152
             20    6  162   20    8  172   20    8
            182   20    6  192   20    8  202   20
              8  212   20    6  222   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2015-02-11T07:34:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 4.7}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0xbc 0x00    ........
    decimal
              1    0  140    0  140    0  188    0
    datetime (2015-02-11T07:34:28)
    0000   0x1c 0xa2 0x47 0x6b 0x0f                   ..Gk.
    body (0)

#### RECORD 57 PumpSuspend 2015-02-11T07:38:52 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-11T07:38:52)
    0000   0x34 0xa6 0x07 0x0b 0x0f                   4....
    body (0)

#### RECORD 58 BasalProfileStart 2015-02-11T07:39:18 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-11T07:39:18)
    0000   0x12 0xa7 0x07 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 59 PumpResume 2015-02-11T07:39:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-11T07:39:18)
    0000   0x12 0xa7 0x07 0x0b 0x0f                   .....
    body (0)

#### RECORD 60 Rewind 2015-02-11T07:39:22 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-02-11T07:39:22)
    0000   0x16 0xa7 0x07 0x0b 0x0f                   .....
    body (0)

#### RECORD 61 Prime 2015-02-11T07:39:57 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1e                   .....
    decimal
              3    0    0    0   30
    datetime (2015-02-11T07:39:57)
    0000   0x39 0xa7 0x27 0x0b 0x0f                   9.'..
    body (0)

#### RECORD 62 SensorAlert 2015-02-11T07:43:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-11T07:43:42)
    0000   0x2a 0xab 0x27 0xab 0x0f                   *.'..
    body (0)

#### RECORD 63 SensorAlert 2015-02-11T07:54:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-02-11T07:54:30)
    0000   0x1e 0xb6 0x27 0xab 0x0f                   ..'..
    body (0)

#### RECORD 64 NoDelivery 2015-02-11T08:05:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x4a 0x09 0x3f                        .J.?
    decimal
              6   74    9   63
    datetime (2015-02-11T08:05:00)
    0000   0x00 0x85 0x48 0xab 0x0f                   ..H..
    body (0)

#### RECORD 65 ClearAlarm 2015-02-11T08:19:19 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x4a                                  .J
    decimal
             12   74
    datetime (2015-02-11T08:19:19)
    0000   0x13 0x93 0x08 0x0b 0x0f                   .....
    body (0)

#### RECORD 66 BasalProfileStart 2015-02-11T08:19:19 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-11T08:19:19)
    0000   0x13 0x93 0x08 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 67 BasalProfileStart 2015-02-11T08:19:19 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-11T08:19:19)
    0000   0x13 0x93 0x08 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 68 BasalProfileStart 2015-02-11T08:19:35 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-11T08:19:35)
    0000   0x23 0x93 0x08 0x0b 0x0f                   #....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 69 Prime 2015-02-11T08:19:21 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-02-11T08:19:21)
    0000   0x15 0x93 0x08 0x0b 0x0f                   .....
    body (0)

#### RECORD 70 Bolus 2015-02-11T08:20:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x01 0x14 0x00    ..<.<...
    decimal
              1    0   60    0   60    1   20    0
    datetime (2015-02-11T08:20:12)
    0000   0x0c 0x94 0x48 0x6b 0x0f                   ..Hk.
    body (0)

#### RECORD 71 SensorAlert 2015-02-11T09:23:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-11T09:23:01)
    0000   0x01 0x97 0x29 0xab 0x0f                   ..)..
    body (0)

`end ReadHistoryData-page-32.data: 72 records`
