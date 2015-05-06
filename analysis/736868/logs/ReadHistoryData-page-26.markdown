## START ReadHistoryData-page-26.data
#### STOPPING DOUBLE NULLS @ 1009, found 13 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x48 0xdd                                  H.
##### DEBUG DECIMAL
             72  221
#### RECORD 0 UnabsorbedInsulinBolus unknown head[62], body[0] op[0x5c]
###### DECODED
```python
[{'age': 273, 'amount': 0.1},
 {'age': 283, 'amount': 0.2},
 {'age': 293, 'amount': 0.25},
 {'age': 303, 'amount': 0.2},
 {'age': 313, 'amount': 0.2},
 {'age': 323, 'amount': 0.25},
 {'age': 333, 'amount': 0.2},
 {'age': 343, 'amount': 0.25},
 {'age': 353, 'amount': 0.2},
 {'age': 363, 'amount': 0.25},
 {'age': 373, 'amount': 0.2},
 {'age': 383, 'amount': 0.25},
 {'age': 393, 'amount': 0.2},
 {'age': 403, 'amount': 0.2},
 {'age': 413, 'amount': 0.25},
 {'age': 423, 'amount': 4.2},
 {'age': 433, 'amount': 0.25},
 {'age': 443, 'amount': 0.2},
 {'age': 453, 'amount': 4.75},
 {'age': 463, 'amount': 1.4}]
```
    op hex (62)
    0000   0x5c 0x3e 0x04 0x11 0x14 0x08 0x1b 0x14    \>......
    0008   0x0a 0x25 0x14 0x08 0x2f 0x14 0x08 0x39    .%../..9
    0010   0x14 0x0a 0x43 0x14 0x08 0x4d 0x14 0x0a    ..C..M..
    0018   0x57 0x14 0x08 0x61 0x14 0x0a 0x6b 0x14    W..a..k.
    0020   0x08 0x75 0x14 0x0a 0x7f 0x14 0x08 0x89    .u......
    0028   0x14 0x08 0x93 0x14 0x0a 0x9d 0x14 0xa8    ........
    0030   0xa7 0x14 0x0a 0xb1 0x14 0x08 0xbb 0x14    ........
    0038   0xbe 0xc5 0x14 0x38 0xcf 0x14              ...8..
    decimal
             92   62    4   17   20    8   27   20
             10   37   20    8   47   20    8   57
             20   10   67   20    8   77   20   10
             87   20    8   97   20   10  107   20
              8  117   20   10  127   20    8  137
             20    8  147   20   10  157   20  168
            167   20   10  177   20    8  187   20
            190  197   20   56  207   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-02-17T04:29:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8,
 'duration': 0,
 'programmed': 4.8,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xc0 0x00 0xc0 0x00 0x00 0x00    ........
    decimal
              1    0  192    0  192    0    0    0
    datetime (2015-02-17T04:29:52)
    0000   0x34 0x9d 0x44 0x71 0x0f                   4.Dq.
    body (0)

#### RECORD 2 SensorAlert 2015-02-17T04:35:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-17T04:35:05)
    0000   0x05 0xa3 0x24 0xb1 0x0f                   ..$..
    body (0)

#### RECORD 3 SensorAlert 2015-02-17T06:04:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 247}
```
    op hex (3)
    0000   0x0b 0x65 0xf7                             .e.
    decimal
             11  101  247
    datetime (2015-02-17T06:04:56)
    0000   0x38 0x84 0x26 0xb1 0x0f                   8.&..
    body (0)

#### RECORD 4 Bolus 2015-02-17T06:29:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x58 0x00    ..d.d.X.
    decimal
              1    0  100    0  100    0   88    0
    datetime (2015-02-17T06:29:26)
    0000   0x1a 0x9d 0x46 0x71 0x0f                   ..Fq.
    body (0)

#### RECORD 5 Bolus 2015-02-17T06:32:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 4.6}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xb8 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  184    0
    datetime (2015-02-17T06:32:53)
    0000   0x35 0xa0 0x46 0x71 0x0f                   5.Fq.
    body (0)

#### RECORD 6 BasalProfileStart 2015-02-17T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-17T07:00:00)
    0000   0x00 0x80 0x07 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 7 PumpSuspend 2015-02-17T07:23:59 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-17T07:23:59)
    0000   0x3b 0x97 0x07 0x11 0x0f                   ;....
    body (0)

#### RECORD 8 SensorAlert 2015-02-17T07:39:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 192}
```
    op hex (3)
    0000   0x0b 0x65 0xc0                             .e.
    decimal
             11  101  192
    datetime (2015-02-17T07:39:29)
    0000   0x1d 0xa7 0x27 0xb1 0x0f                   ..'..
    body (0)

#### RECORD 9 BasalProfileStart 2015-02-17T07:49:45 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-17T07:49:45)
    0000   0x2d 0xb1 0x07 0x11 0x0f                   -....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 10 PumpResume 2015-02-17T07:49:45 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-17T07:49:45)
    0000   0x2d 0xb1 0x07 0x11 0x0f                   -....
    body (0)

#### RECORD 11 BolusWizard 2015-02-17T07:49:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 50,
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
    datetime (2015-02-17T07:49:57)
    0000   0x39 0xb1 0x07 0x71 0x0f                   9..q.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 12 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 83, 'amount': 4.5},
 {'age': 203, 'amount': 4.8},
 {'age': 473, 'amount': 0.1}]
```
    op hex (11)
    0000   0x5c 0x0b 0xb4 0x53 0x04 0xc0 0xcb 0x04    \..S....
    0008   0x04 0xd9 0x14                             ...
    decimal
             92   11  180   83    4  192  203    4
              4  217   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2015-02-17T07:49:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 3.7}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x94 0x00    ........
    decimal
              1    0  200    0  200    0  148    0
    datetime (2015-02-17T07:49:57)
    0000   0x39 0xb1 0x47 0x71 0x0f                   9.Gq.
    body (0)

#### RECORD 14 BasalProfileStart 2015-02-17T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-17T10:00:00)
    0000   0x00 0x80 0x0a 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 15 SensorAlert 2015-02-17T10:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-17T10:18:00)
    0000   0x00 0x92 0x2a 0xb1 0x0f                   ..*..
    body (0)

#### RECORD 16 SensorAlert 2015-02-17T11:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-17T11:18:00)
    0000   0x00 0x92 0x2b 0xb1 0x0f                   ..+..
    body (0)

#### RECORD 17 CalBGForPH 2015-02-17T11:35:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2015-02-17T11:35:38)
    0000   0x26 0xa3 0x2b 0x71 0x0f                   &.+q.
    body (0)

#### RECORD 18 BGReceived 2015-02-17T11:35:38 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 115, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2015-02-17T11:35:38)
    0000   0x26 0xa3 0x6b 0x71 0x0f                   &.kq.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 19 BasalProfileStart 2015-02-17T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-17T12:00:00)
    0000   0x00 0x80 0x0c 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 20 SensorAlert 2015-02-17T13:34:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-17T13:34:07)
    0000   0x07 0xa2 0x2d 0xb1 0x0f                   ..-..
    body (0)

#### RECORD 21 BasalProfileStart 2015-02-17T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-17T15:00:00)
    0000   0x00 0x80 0x0f 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 22 SensorAlert 2015-02-17T15:15:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-17T15:15:05)
    0000   0x05 0x8f 0x2f 0xb1 0x0f                   ../..
    body (0)

#### RECORD 23 SensorAlert 2015-02-17T15:24:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-17T15:24:56)
    0000   0x38 0x98 0x2f 0xb1 0x0f                   8./..
    body (0)

#### RECORD 24 Bolus 2015-02-17T16:04:25 head[8], body[0] op[0x01]
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
    datetime (2015-02-17T16:04:25)
    0000   0x19 0x84 0x50 0x71 0x0f                   ..Pq.
    body (0)

#### RECORD 25 Bolus 2015-02-17T17:09:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x40 0x00    ..x.x.@.
    decimal
              1    0  120    0  120    0   64    0
    datetime (2015-02-17T17:09:08)
    0000   0x08 0x89 0x51 0x71 0x0f                   ..Qq.
    body (0)

#### RECORD 26 SensorAlert 2015-02-17T17:18:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-17T17:18:48)
    0000   0x30 0x92 0x31 0xb1 0x0f                   0.1..
    body (0)

#### RECORD 27 BasalProfileStart 2015-02-17T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-17T22:00:00)
    0000   0x00 0x80 0x16 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 28 BolusWizard 2015-02-17T22:11:04 head[2], body[15] op[0x5b]
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
    datetime (2015-02-17T22:11:04)
    0000   0x04 0x8b 0x16 0x71 0x0f                   ...q.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    FP.<(Z..
    0008   0xd0 0x00 0x00 0x00 0x01 0xd0 0x78         ......x
    decimal
             70   80    0   60   40   90    0    1
            208    0    0    0    1  208  120

#### RECORD 29 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 305, 'amount': 3.0}, {'age': 375, 'amount': 2.0}]
```
    op hex (8)
    0000   0x5c 0x08 0x78 0x31 0x14 0x50 0x77 0x14    \.x1.Pw.
    decimal
             92    8  120   49   20   80  119   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2015-02-17T22:15:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6,
 'duration': 180,
 'programmed': 4.6,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xb8 0x00 0xb8 0x00 0x00 0x06    ........
    decimal
              1    0  184    0  184    0    0    6
    datetime (2015-02-17T22:15:48)
    0000   0x30 0x8f 0xb6 0x71 0x0f                   0..q.
    body (0)

#### RECORD 31 Bolus 2015-02-17T22:11:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6,
 'duration': 0,
 'programmed': 0.6,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x00 0x00    ........
    decimal
              1    1   24    1   24    0    0    0
    datetime (2015-02-17T22:11:04)
    0000   0x04 0x8b 0x96 0x71 0x0f                   ...q.
    body (0)

#### RECORD 32 SensorAlert 2015-02-17T22:19:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-17T22:19:29)
    0000   0x1d 0x93 0x36 0xb1 0x0f                   ..6..
    body (0)

#### RECORD 33 SensorAlert 2015-02-17T22:25:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-17T22:25:24)
    0000   0x18 0x99 0x36 0xb1 0x0f                   ..6..
    body (0)

#### RECORD 34 SensorAlert 2015-02-17T22:35:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-17T22:35:00)
    0000   0x00 0xa3 0x36 0xb1 0x0f                   ..6..
    body (0)

#### RECORD 35 CalBGForPH 2015-02-17T22:36:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 236}
```
    op hex (2)
    0000   0x0a 0xec                                  ..
    decimal
             10  236
    datetime (2015-02-17T22:36:08)
    0000   0x08 0xa4 0x36 0x71 0x0f                   ..6q.
    body (0)

#### RECORD 36 BGReceived 2015-02-17T22:36:08 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 236, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2015-02-17T22:36:08)
    0000   0x08 0xa4 0x96 0x71 0x0f                   ...q.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 37 SensorAlert 2015-02-17T23:55:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 200}
```
    op hex (3)
    0000   0x0b 0x65 0xc8                             .e.
    decimal
             11  101  200
    datetime (2015-02-17T23:55:05)
    0000   0x05 0xb7 0x37 0xb1 0x0f                   ..7..
    body (0)

#### RECORD 38 BasalProfileStart 2015-02-18T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-18T00:00:00)
    0000   0x00 0x80 0x00 0x12 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 39 MResultTotals 2015-02-18T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xa7                   .....
    decimal
              7    0    0    7  167
    datetime (2015-02-18T00:00:00)
    0000   0x31 0x0f                                  1.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 40 Sara6E 2015-02-18T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-18T00:00:00)
    0000   0x31 0x0f                                  1.
    body (49)
    hex
    0000   0x05 0x00 0xb0 0x73 0xec 0x02 0x00 0x00    ...s....
    0008   0x07 0xa7 0x03 0x21 0x29 0x04 0x86 0x3b    ...!)..;
    0010   0x00 0x96 0x02 0x4a 0x00 0x00 0x00 0xc0    ...J....
    0018   0x01 0x7c 0x02 0x00 0x01 0x04 0x00 0x9a    .|......
    0020   0x1d 0x47 0x00 0x1a 0x2a 0x04 0x01 0x00    .G..*...
    0028   0x00 0x00 0x06 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  176  115  236    2    0    0
              7  167    3   33   41    4  134   59
              0  150    2   74    0    0    0  192
              1  124    2    0    1    4    0  154
             29   71    0   26   42    4    1    0
              0    0    6    1    0    0    0    0
              0

#### RECORD 41 SensorAlert 2015-02-18T01:24:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 198}
```
    op hex (3)
    0000   0x0b 0x65 0xc6                             .e.
    decimal
             11  101  198
    datetime (2015-02-18T01:24:56)
    0000   0x38 0x98 0x21 0xb2 0x0f                   8.!..
    body (0)

#### RECORD 42 SensorAlert 2015-02-18T02:54:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 211}
```
    op hex (3)
    0000   0x0b 0x65 0xd3                             .e.
    decimal
             11  101  211
    datetime (2015-02-18T02:54:07)
    0000   0x07 0xb6 0x22 0xb2 0x0f                   .."..
    body (0)

#### RECORD 43 Bolus 2015-02-18T03:40:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x10 0x00    ........
    decimal
              1    0  160    0  160    0   16    0
    datetime (2015-02-18T03:40:14)
    0000   0x0e 0xa8 0x43 0x72 0x0f                   ..Cr.
    body (0)

#### RECORD 44 Bolus 2015-02-18T03:44:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 4.4}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xb0 0x00    ........
    decimal
              1    0  160    0  160    0  176    0
    datetime (2015-02-18T03:44:18)
    0000   0x12 0xac 0x43 0x72 0x0f                   ..Cr.
    body (0)

#### RECORD 45 BasalProfileStart 2015-02-18T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-18T04:00:00)
    0000   0x00 0x80 0x04 0x12 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 46 SensorAlert 2015-02-18T04:25:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 192}
```
    op hex (3)
    0000   0x0b 0x65 0xc0                             .e.
    decimal
             11  101  192
    datetime (2015-02-18T04:25:24)
    0000   0x18 0x99 0x24 0xb2 0x0f                   ..$..
    body (0)

#### RECORD 47 BasalProfileStart 2015-02-18T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-18T07:00:00)
    0000   0x00 0x80 0x07 0x12 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 48 PumpSuspend 2015-02-18T07:04:43 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-18T07:04:43)
    0000   0x2b 0x84 0x07 0x12 0x0f                   +....
    body (0)

#### RECORD 49 BasalProfileStart 2015-02-18T07:30:04 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-18T07:30:04)
    0000   0x04 0x9e 0x07 0x12 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 50 PumpResume 2015-02-18T07:30:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-18T07:30:04)
    0000   0x04 0x9e 0x07 0x12 0x0f                   .....
    body (0)

#### RECORD 51 BolusWizard 2015-02-18T07:44:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 75,
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
    datetime (2015-02-18T07:44:45)
    0000   0x2d 0xac 0x07 0x72 0x0f                   -..r.
    body (15)
    hex
    0000   0x4b 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    KP.d(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             75   80    0  100   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 238, 'amount': 1.5},
 {'age': 248, 'amount': 0.1},
 {'age': 398, 'amount': 0.25},
 {'age': 408, 'amount': 0.25},
 {'age': 418, 'amount': 0.25},
 {'age': 428, 'amount': 0.25},
 {'age': 438, 'amount': 0.25},
 {'age': 448, 'amount': 0.3},
 {'age': 458, 'amount': 0.25},
 {'age': 468, 'amount': 0.25},
 {'age': 478, 'amount': 0.25}]
```
    op hex (35)
    0000   0x5c 0x23 0x3c 0xee 0x04 0x04 0xf8 0x05    \#<.....
    0008   0x0a 0x8e 0x14 0x0a 0x98 0x14 0x0a 0xa2    ........
    0010   0x14 0x0a 0xac 0x14 0x0a 0xb6 0x14 0x0c    ........
    0018   0xc0 0x14 0x0a 0xca 0x14 0x0a 0xd4 0x14    ........
    0020   0x0a 0xde 0x14                             ...
    decimal
             92   35   60  238    4    4  248    5
             10  142   20   10  152   20   10  162
             20   10  172   20   10  182   20   12
            192   20   10  202   20   10  212   20
             10  222   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2015-02-18T07:44:45 head[8], body[0] op[0x01]
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
    datetime (2015-02-18T07:44:45)
    0000   0x2d 0xac 0x47 0x72 0x0f                   -.Gr.
    body (0)

#### RECORD 54 SensorAlert 2015-02-18T09:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-18T09:36:00)
    0000   0x00 0xa4 0x29 0xb2 0x0f                   ..)..
    body (0)

#### RECORD 55 SensorAlert 2015-02-18T09:45:23 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-18T09:45:23)
    0000   0x17 0xad 0x29 0xb2 0x0f                   ..)..
    body (0)

#### RECORD 56 SensorAlert 2015-02-18T09:58:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-02-18T09:58:47)
    0000   0x2f 0xba 0x29 0xb2 0x0f                   /.)..
    body (0)

#### RECORD 57 BasalProfileStart 2015-02-18T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-18T10:00:00)
    0000   0x00 0x80 0x0a 0x12 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 58 SensorAlert 2015-02-18T10:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-18T10:36:00)
    0000   0x00 0xa4 0x2a 0xb2 0x0f                   ..*..
    body (0)

#### RECORD 59 CalBGForPH 2015-02-18T10:39:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 348}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2015-02-18T10:39:32)
    0000   0x20 0xa7 0x2a 0x72 0x8f                    .*r.
    body (0)

#### RECORD 60 BGReceived 2015-02-18T10:39:32 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 348, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2b                                  ?+
    decimal
             63   43
    datetime (2015-02-18T10:39:32)
    0000   0x20 0xa7 0x8a 0x72 0x0f                    ..r.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 61 BolusWizard 2015-02-18T10:39:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 348,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': -0.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.2}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2015-02-18T10:39:51)
    0000   0x33 0xa7 0x0a 0x12 0x0f                   3....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xe4 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x30 0x00 0xb4 0x78         ...0..x
    decimal
              0   81    0  100   40   90  228    0
              0    0    0   48    0  180  120

#### RECORD 62 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 4.15},
 {'age': 183, 'amount': 1.85},
 {'age': 413, 'amount': 1.5},
 {'age': 423, 'amount': 0.1}]
```
    op hex (14)
    0000   0x5c 0x0e 0xa6 0xad 0x04 0x4a 0xb7 0x04    \....J..
    0008   0x3c 0x9d 0x14 0x04 0xa7 0x15              <.....
    decimal
             92   14  166  173    4   74  183    4
             60  157   20    4  167   21
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2015-02-18T10:39:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 1.2}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x30 0x00    ......0.
    decimal
              1    0  180    0  180    0   48    0
    datetime (2015-02-18T10:39:51)
    0000   0x33 0xa7 0x4a 0x12 0x0f                   3.J..
    body (0)

#### RECORD 64 Bolus 2015-02-18T10:44:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 5.6}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xe0 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  224    0
    datetime (2015-02-18T10:44:39)
    0000   0x27 0xac 0x4a 0x72 0x0f                   '.Jr.
    body (0)

#### RECORD 65 SensorAlert 2015-02-18T10:54:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 341}
```
    op hex (3)
    0000   0x0b 0x65 0x55                             .eU
    decimal
             11  101   85
    datetime (2015-02-18T10:54:06)
    0000   0x06 0xb6 0x2a 0xb2 0x8f                   ..*..
    body (0)

#### RECORD 66 Bolus 2015-02-18T10:54:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x01 0x38 0x00    ..x.x.8.
    decimal
              1    0  120    0  120    1   56    0
    datetime (2015-02-18T10:54:49)
    0000   0x31 0xb6 0x4a 0x72 0x0f                   1.Jr.
    body (0)

#### RECORD 67 BolusWizard 2015-02-18T11:56:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.6,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-18T11:56:17)
    0000   0x11 0xb8 0x0b 0x72 0x0f                   ...r.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    -P.P(Z..
    0008   0xe0 0x00 0x00 0x00 0x00 0xe0 0x78         ......x
    decimal
             45   80    0   80   40   90    0    0
            224    0    0    0    0  224  120

#### RECORD 68 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 1.25},
 {'age': 70, 'amount': 2.2},
 {'age': 80, 'amount': 0.15},
 {'age': 250, 'amount': 4.15},
 {'age': 260, 'amount': 1.85}]
```
    op hex (17)
    0000   0x5c 0x11 0x32 0x3c 0x04 0x58 0x46 0x04    \.2<.XF.
    0008   0x06 0x50 0x05 0xa6 0xfa 0x04 0x4a 0x04    .P....J.
    0010   0x14                                       .
    decimal
             92   17   50   60    4   88   70    4
              6   80    5  166  250    4   74    4
             20
    datetime (unknown)

    body (0)

#### RECORD 69 BasalProfileStart 2015-02-18T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-18T12:00:00)
    0000   0x00 0x80 0x0c 0x12 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 70 Bolus 2015-02-18T11:56:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6,
 'duration': 0,
 'programmed': 5.6,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0xe0 0x00 0xe0 0x01 0x28 0x00    ......(.
    decimal
              1    0  224    0  224    1   40    0
    datetime (2015-02-18T11:56:17)
    0000   0x11 0xb8 0x4b 0x72 0x0f                   ..Kr.
    body (0)

#### RECORD 71 SensorAlert 2015-02-18T12:25:23 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 300}
```
    op hex (3)
    0000   0x0b 0x65 0x2c                             .e,
    decimal
             11  101   44
    datetime (2015-02-18T12:25:23)
    0000   0x17 0x99 0x2c 0xb2 0x8f                   ..,..
    body (0)

#### RECORD 72 SensorAlert 2015-02-18T13:55:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 271}
```
    op hex (3)
    0000   0x0b 0x65 0x0f                             .e.
    decimal
             11  101   15
    datetime (2015-02-18T13:55:04)
    0000   0x04 0xb7 0x2d 0xb2 0x8f                   ..-..
    body (0)

#### RECORD 73 BasalProfileStart 2015-02-18T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-18T15:00:00)
    0000   0x00 0x80 0x0f 0x12 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 74 BolusWizard 2015-02-18T16:11:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.8,
 'carb_input': 31,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 3.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-18T16:11:42)
    0000   0x2a 0x8b 0x10 0x72 0x0f                   *..r.
    body (15)
    hex
    0000   0x1f 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x98 0x00 0x00 0x00 0x00 0x98 0x78         ......x
    decimal
             31   80    0   80   40   90    0    0
            152    0    0    0    0  152  120

#### RECORD 75 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 255, 'amount': 5.6},
 {'age': 315, 'amount': 1.25},
 {'age': 325, 'amount': 2.2},
 {'age': 335, 'amount': 0.15}]
```
    op hex (14)
    0000   0x5c 0x0e 0xe0 0xff 0x04 0x32 0x3b 0x14    \....2;.
    0008   0x58 0x45 0x14 0x06 0x4f 0x15              XE..O.
    decimal
             92   14  224  255    4   50   59   20
             88   69   20    6   79   21
    datetime (unknown)

    body (0)

#### RECORD 76 SensorAlert 2015-02-18T16:14:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-18T16:14:06)
    0000   0x06 0x8e 0x30 0xb2 0x0f                   ..0..
    body (0)

#### RECORD 77 Bolus 2015-02-18T16:11:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8,
 'duration': 0,
 'programmed': 3.8,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x00 0x00    ........
    decimal
              1    0  152    0  152    0    0    0
    datetime (2015-02-18T16:11:42)
    0000   0x2a 0x8b 0x50 0x72 0x0f                   *.Pr.
    body (0)

#### RECORD 78 SensorAlert 2015-02-18T16:25:23 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-18T16:25:23)
    0000   0x17 0x99 0x30 0xb2 0x0f                   ..0..
    body (0)

#### RECORD 79 Bolus 2015-02-18T16:26:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 3.8}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x98 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  152    0
    datetime (2015-02-18T16:26:38)
    0000   0x26 0x9a 0x50 0x72 0x0f                   &.Pr.
    body (0)

#### RECORD 80 BolusWizard 2015-02-18T16:31:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 36,
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
    datetime (2015-02-18T16:31:22)
    0000   0x16 0x9f 0x10 0x72 0x0f                   ...r.
    body (15)
    hex
    0000   0x24 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    $P.P(Z..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x78         ......x
    decimal
             36   80    0   80   40   90    0    0
            180    0    0    0    0  180  120

`end ReadHistoryData-page-26.data: 81 records`
