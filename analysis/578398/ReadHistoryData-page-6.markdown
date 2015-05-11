## START ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 1010, found 12 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x11 0xda                                  ..
##### DEBUG DECIMAL
             17  218
#### RECORD 0 BolusWizard 2015-04-19T19:32:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.0,
 'carb_input': 48,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 8.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-19T19:32:02)
    0000   0x42 0x20 0x13 0x13 0x0f                   B ...
    body (13)
    hex
    0000   0x30 0x50 0x06 0x28 0x5a 0x00 0x50 0x00    0P.(Z.P.
    0008   0x00 0x00 0x00 0x50 0x78                   ...Px
    decimal
             48   80    6   40   90    0   80    0
              0    0    0   80  120

#### RECORD 1 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 183, 'amount': 0.05},
 {'age': 193, 'amount': 0.35},
 {'age': 203, 'amount': 0.3},
 {'age': 213, 'amount': 2.85},
 {'age': 223, 'amount': 0.35},
 {'age': 233, 'amount': 0.3},
 {'age': 243, 'amount': 2.25},
 {'age': 253, 'amount': 2.75}]
```
    op hex (26)
    0000   0x5c 0x1a 0x02 0xb7 0x04 0x0e 0xc1 0x04    \.......
    0008   0x0c 0xcb 0x04 0x72 0xd5 0x04 0x0e 0xdf    ...r....
    0010   0x04 0x0c 0xe9 0x04 0x5a 0xf3 0x04 0x6e    ....Z..n
    0018   0xfd 0x04                                  ..
    decimal
             92   26    2  183    4   14  193    4
             12  203    4  114  213    4   14  223
              4   12  233    4   90  243    4  110
            253    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2015-04-19T19:32:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'duration': 0, 'programmed': 3.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2015-04-19T19:32:02)
    0000   0x42 0x20 0x93 0x13 0x0f                   B ...
    body (0)

#### RECORD 3 CalBGForPH 2015-04-19T22:38:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 51}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2015-04-19T22:38:26)
    0000   0x5a 0x26 0x36 0x73 0x0f                   Z&6s.
    body (0)

#### RECORD 4 BGReceived 2015-04-19T22:38:26 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 51, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2015-04-19T22:38:26)
    0000   0x5a 0x26 0x76 0x73 0x0f                   Z&vs.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 5 Bolus 2015-04-19T19:34:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'duration': 210, 'programmed': 3.2, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x07                        .  .
    decimal
              1   32   32    7
    datetime (2015-04-19T19:34:34)
    0000   0x62 0x22 0xb3 0x13 0x0f                   b"...
    body (0)

#### RECORD 6 MResultTotals 2015-04-20T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xb4                   .....
    decimal
              7    0    0    5  180
    datetime (2015-04-20T00:00:00)
    0000   0x53 0x0f                                  S.
    body (0)

#### RECORD 7 Model522ResultTotals 2015-04-20T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-20T00:00:00)
    0000   0x53 0x0f                                  S.
    body (41)
    hex
    0000   0x05 0x00 0x5f 0x33 0x8a 0x02 0x00 0x00    .._3....
    0008   0x05 0xb4 0x03 0x1c 0x37 0x02 0x98 0x2d    ....7..-
    0010   0x00 0x7a 0x02 0x98 0x2d 0x02 0x88 0x62    .z..-..b
    0018   0x00 0x10 0x02 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x01 0x00 0x00 0x00 0x5c 0x35 0xa4 0xb3    ....\5..
    0028   0x01                                       .
    decimal
              5    0   95   51  138    2    0    0
              5  180    3   28   55    2  152   45
              0  122    2  152   45    2  136   98
              0   16    2    0    0    0    4    3
              1    0    0    0   92   53  164  179
              1

#### RECORD 8 PumpSuspend 2015-04-20T07:12:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-20T07:12:57)
    0000   0x79 0x0c 0x07 0x14 0x0f                   y....
    body (0)

#### RECORD 9 PumpResume 2015-04-20T07:17:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-20T07:17:04)
    0000   0x44 0x11 0x07 0x14 0x0f                   D....
    body (0)

#### RECORD 10 BolusWizard 2015-04-20T08:35:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 50,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-20T08:35:47)
    0000   0x6f 0x23 0x08 0x14 0x0f                   o#...
    body (13)
    hex
    0000   0x32 0x50 0x0a 0x28 0x5a 0x00 0x32 0x00    2P.(Z.2.
    0008   0x00 0x00 0x00 0x32 0x78                   ...2x
    decimal
             50   80   10   40   90    0   50    0
              0    0    0   50  120

#### RECORD 11 Bolus 2015-04-20T08:35:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2015-04-20T08:35:47)
    0000   0x6f 0x23 0x88 0x14 0x0f                   o#...
    body (0)

#### RECORD 12 Bolus 2015-04-20T08:38:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'duration': 90, 'programmed': 1.6, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x03                        ....
    decimal
              1   16   16    3
    datetime (2015-04-20T08:38:01)
    0000   0x41 0x26 0xa8 0x14 0x0f                   A&...
    body (0)

#### RECORD 13 SensorAlert 2015-04-20T13:47:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-20T13:47:29)
    0000   0x5d 0x2f 0x2d 0xb4 0x0f                   ]/-..
    body (0)

#### RECORD 14 CalBGForPH 2015-04-20T13:48:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2015-04-20T13:48:50)
    0000   0x72 0x30 0x2d 0x74 0x0f                   r0-t.
    body (0)

#### RECORD 15 BGReceived 2015-04-20T13:48:50 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 206, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2015-04-20T13:48:50)
    0000   0x72 0x30 0xcd 0x74 0x0f                   r0.t.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 16 BolusWizard 2015-04-20T13:49:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 206,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 8,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xce                                  [.
    decimal
             91  206
    datetime (2015-04-20T13:49:20)
    0000   0x54 0x31 0x0d 0x14 0x0f                   T1...
    body (13)
    hex
    0000   0x00 0x50 0x08 0x28 0x5a 0x15 0x00 0x00    .P.(Z...
    0008   0x00 0x01 0x00 0x14 0x78                   ....x
    decimal
              0   80    8   40   90   21    0    0
              0    1    0   20  120

#### RECORD 17 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 230, 'amount': 0.15},
 {'age': 240, 'amount': 0.2},
 {'age': 250, 'amount': 0.15},
 {'age': 260, 'amount': 0.2},
 {'age': 270, 'amount': 0.15},
 {'age': 280, 'amount': 0.2},
 {'age': 290, 'amount': 0.2},
 {'age': 300, 'amount': 0.15},
 {'age': 310, 'amount': 0.2},
 {'age': 320, 'amount': 3.4}]
```
    op hex (32)
    0000   0x5c 0x20 0x06 0xe6 0x04 0x08 0xf0 0x04    \ ......
    0008   0x06 0xfa 0x04 0x08 0x04 0x14 0x06 0x0e    ........
    0010   0x14 0x08 0x18 0x14 0x08 0x22 0x14 0x06    ....."..
    0018   0x2c 0x14 0x08 0x36 0x14 0x88 0x40 0x14    ,..6..@.
    decimal
             92   32    6  230    4    8  240    4
              6  250    4    8    4   20    6   14
             20    8   24   20    8   34   20    6
             44   20    8   54   20  136   64   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2015-04-20T13:49:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 0, 'programmed': 2.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2015-04-20T13:49:20)
    0000   0x54 0x31 0x8d 0x14 0x0f                   T1...
    body (0)

#### RECORD 19 SensorAlert 2015-04-20T14:00:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 206}
```
    op hex (3)
    0000   0x0b 0x65 0xce                             .e.
    decimal
             11  101  206
    datetime (2015-04-20T14:00:36)
    0000   0x64 0x00 0x2e 0xb4 0x0f                   d....
    body (0)

#### RECORD 20 SensorAlert 2015-04-20T15:30:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 192}
```
    op hex (3)
    0000   0x0b 0x65 0xc0                             .e.
    decimal
             11  101  192
    datetime (2015-04-20T15:30:38)
    0000   0x66 0x1e 0x2f 0xb4 0x0f                   f./..
    body (0)

#### RECORD 21 SensorAlert 2015-04-20T18:48:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-20T18:48:00)
    0000   0x40 0x30 0x32 0xb4 0x0f                   @02..
    body (0)

#### RECORD 22 SensorAlert 2015-04-20T19:07:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 188}
```
    op hex (3)
    0000   0x0b 0x65 0xbc                             .e.
    decimal
             11  101  188
    datetime (2015-04-20T19:07:12)
    0000   0x4c 0x07 0x33 0xb4 0x0f                   L.3..
    body (0)

#### RECORD 23 SensorAlert 2015-04-20T19:48:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-20T19:48:00)
    0000   0x40 0x30 0x33 0xb4 0x0f                   @03..
    body (0)

#### RECORD 24 SensorAlert 2015-04-20T20:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-20T20:18:00)
    0000   0x40 0x12 0x34 0xb4 0x0f                   @.4..
    body (0)

#### RECORD 25 SensorAlert 2015-04-20T20:48:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-20T20:48:00)
    0000   0x40 0x30 0x34 0xb4 0x0f                   @04..
    body (0)

#### RECORD 26 SensorAlert 2015-04-20T21:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-20T21:18:00)
    0000   0x40 0x12 0x35 0xb4 0x0f                   @.5..
    body (0)

#### RECORD 27 SensorAlert 2015-04-20T21:48:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-20T21:48:00)
    0000   0x40 0x30 0x35 0xb4 0x0f                   @05..
    body (0)

#### RECORD 28 SensorAlert 2015-04-20T22:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-20T22:18:00)
    0000   0x40 0x12 0x36 0xb4 0x0f                   @.6..
    body (0)

#### RECORD 29 CalBGForPH 2015-04-20T22:19:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 336}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2015-04-20T22:19:04)
    0000   0x44 0x13 0x36 0x74 0x8f                   D.6t.
    body (0)

#### RECORD 30 BGReceived 2015-04-20T22:19:04 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 336, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2a                                  ?*
    decimal
             63   42
    datetime (2015-04-20T22:19:04)
    0000   0x44 0x13 0x16 0x74 0x0f                   D..t.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 31 BolusWizard 2015-04-20T22:19:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 336,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.4,
 'carb_input': 0,
 'carb_ratio': 6,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2015-04-20T22:19:22)
    0000   0x56 0x13 0x16 0x14 0x0f                   V....
    body (13)
    hex
    0000   0x00 0x51 0x06 0x28 0x5a 0x36 0x00 0x00    .Q.(Z6..
    0008   0x00 0x00 0x00 0x36 0x78                   ...6x
    decimal
              0   81    6   40   90   54    0    0
              0    0    0   54  120

#### RECORD 32 Bolus 2015-04-20T22:19:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4, 'duration': 0, 'programmed': 5.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x36 0x36 0x00                        .66.
    decimal
              1   54   54    0
    datetime (2015-04-20T22:19:23)
    0000   0x57 0x13 0x96 0x14 0x0f                   W....
    body (0)

#### RECORD 33 SensorAlert 2015-04-20T22:32:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 332}
```
    op hex (3)
    0000   0x0b 0x65 0x4c                             .eL
    decimal
             11  101   76
    datetime (2015-04-20T22:32:05)
    0000   0x45 0x20 0x36 0xb4 0x8f                   E 6..
    body (0)

#### RECORD 34 MResultTotals 2015-04-21T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x16                   .....
    decimal
              7    0    0    5   22
    datetime (2015-04-21T00:00:00)
    0000   0x54 0x0f                                  T.
    body (0)

#### RECORD 35 Model522ResultTotals 2015-04-21T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-21T00:00:00)
    0000   0x54 0x0f                                  T.
    body (41)
    hex
    0000   0x05 0x11 0x0f 0xce 0x50 0x02 0x00 0x00    ....P...
    0008   0x05 0x16 0x03 0x26 0x3e 0x01 0xf0 0x26    ...&>..&
    0010   0x00 0x32 0x01 0xf0 0x26 0x00 0xc8 0x28    .2..&..(
    0018   0x01 0x28 0x3c 0x00 0x00 0x00 0x03 0x01    .(<.....
    0020   0x02 0x00 0x00 0x10 0xcd 0x99 0x54 0x58    ......TX
    0028   0x02                                       .
    decimal
              5   17   15  206   80    2    0    0
              5   22    3   38   62    1  240   38
              0   50    1  240   38    0  200   40
              1   40   60    0    0    0    3    1
              2    0    0   16  205  153   84   88
              2

#### RECORD 36 SensorAlert 2015-04-21T02:36:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-04-21T02:36:53)
    0000   0x75 0x24 0x22 0xb5 0x0f                   u$"..
    body (0)

#### RECORD 37 SensorAlert 2015-04-21T02:55:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 67}
```
    op hex (3)
    0000   0x0b 0x66 0x43                             .fC
    decimal
             11  102   67
    datetime (2015-04-21T02:55:55)
    0000   0x77 0x37 0x22 0xb5 0x0f                   w7"..
    body (0)

#### RECORD 38 SensorAlert 2015-04-21T03:16:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 63}
```
    op hex (3)
    0000   0x0b 0x66 0x3f                             .f?
    decimal
             11  102   63
    datetime (2015-04-21T03:16:53)
    0000   0x75 0x10 0x23 0xb5 0x0f                   u.#..
    body (0)

#### RECORD 39 BolusWizard 2015-04-21T07:33:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-21T07:33:22)
    0000   0x56 0x21 0x07 0x15 0x0f                   V!...
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80   10   40   90    0    0    0
              0    0    0    0  120

#### RECORD 40 Bolus 2015-04-21T07:33:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'duration': 0, 'programmed': 1.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2015-04-21T07:33:22)
    0000   0x56 0x21 0x47 0x15 0x0f                   V!G..
    body (0)

#### RECORD 41 SensorAlert 2015-04-21T07:41:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 193}
```
    op hex (3)
    0000   0x0b 0x65 0xc1                             .e.
    decimal
             11  101  193
    datetime (2015-04-21T07:41:17)
    0000   0x51 0x29 0x27 0xb5 0x0f                   Q)'..
    body (0)

#### RECORD 42 PumpSuspend 2015-04-21T07:42:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-21T07:42:01)
    0000   0x41 0x2a 0x07 0x15 0x0f                   A*...
    body (0)

#### RECORD 43 PumpResume 2015-04-21T08:30:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-21T08:30:08)
    0000   0x48 0x1e 0x08 0x15 0x0f                   H....
    body (0)

#### RECORD 44 BolusWizard 2015-04-21T08:30:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 50,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-21T08:30:23)
    0000   0x57 0x1e 0x08 0x15 0x0f                   W....
    body (13)
    hex
    0000   0x32 0x50 0x0a 0x28 0x5a 0x00 0x32 0x00    2P.(Z.2.
    0008   0x00 0x00 0x00 0x32 0x78                   ...2x
    decimal
             50   80   10   40   90    0   50    0
              0    0    0   50  120

#### RECORD 45 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 1.0}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x3d 0x04                   \.(=.
    decimal
             92    5   40   61    4
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2015-04-21T08:30:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-21T08:30:23)
    0000   0x57 0x1e 0x88 0x15 0x0f                   W....
    body (0)

#### RECORD 47 SensorAlert 2015-04-21T09:19:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-21T09:19:00)
    0000   0x40 0x13 0x29 0xb5 0x0f                   @.)..
    body (0)

#### RECORD 48 SensorAlert 2015-04-21T10:19:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-21T10:19:00)
    0000   0x40 0x13 0x2a 0xb5 0x0f                   @.*..
    body (0)

#### RECORD 49 CalBGForPH 2015-04-21T10:20:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 87}
```
    op hex (2)
    0000   0x0a 0x57                                  .W
    decimal
             10   87
    datetime (2015-04-21T10:20:48)
    0000   0x70 0x14 0x2a 0x75 0x0f                   p.*u.
    body (0)

#### RECORD 50 BGReceived 2015-04-21T10:20:48 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 87, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2015-04-21T10:20:48)
    0000   0x70 0x14 0xea 0x75 0x0f                   p..u.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 51 Bolus 2015-04-21T08:32:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 120, 'programmed': 2.0, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x04                        ....
    decimal
              1   20   20    4
    datetime (2015-04-21T08:32:23)
    0000   0x57 0x20 0xa8 0x15 0x0f                   W ...
    body (0)

#### RECORD 52 SensorAlert 2015-04-21T12:06:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-21T12:06:44)
    0000   0x6c 0x06 0x2c 0xb5 0x0f                   l.,..
    body (0)

#### RECORD 53 SensorAlert 2015-04-21T16:50:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-04-21T16:50:38)
    0000   0x66 0x32 0x30 0xb5 0x0f                   f20..
    body (0)

#### RECORD 54 SensorAlert 2015-04-21T19:56:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-21T19:56:53)
    0000   0x75 0x38 0x33 0xb5 0x0f                   u83..
    body (0)

#### RECORD 55 BolusWizard 2015-04-21T20:22:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 9.0,
 'carb_input': 54,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 9.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-21T20:22:43)
    0000   0x6b 0x16 0x14 0x15 0x0f                   k....
    body (13)
    hex
    0000   0x36 0x50 0x06 0x28 0x5a 0x00 0x5a 0x00    6P.(Z.Z.
    0008   0x00 0x00 0x00 0x5a 0x78                   ...Zx
    decimal
             54   80    6   40   90    0   90    0
              0    0    0   90  120

#### RECORD 56 Bolus 2015-04-21T20:22:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'duration': 0, 'programmed': 4.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2015-04-21T20:22:43)
    0000   0x6b 0x16 0x94 0x15 0x0f                   k....
    body (0)

#### RECORD 57 SensorAlert 2015-04-21T21:20:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-21T21:20:00)
    0000   0x40 0x14 0x35 0xb5 0x0f                   @.5..
    body (0)

#### RECORD 58 SensorAlert 2015-04-21T21:26:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 245}
```
    op hex (3)
    0000   0x0b 0x65 0xf5                             .e.
    decimal
             11  101  245
    datetime (2015-04-21T21:26:44)
    0000   0x6c 0x1a 0x35 0xb5 0x0f                   l.5..
    body (0)

#### RECORD 59 SensorAlert 2015-04-21T22:20:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-21T22:20:00)
    0000   0x40 0x14 0x36 0xb5 0x0f                   @.6..
    body (0)

#### RECORD 60 CalBGForPH 2015-04-21T22:44:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 54}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2015-04-21T22:44:32)
    0000   0x60 0x2c 0x36 0x75 0x0f                   `,6u.
    body (0)

#### RECORD 61 BGReceived 2015-04-21T22:44:32 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 54, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2015-04-21T22:44:32)
    0000   0x60 0x2c 0xd6 0x75 0x0f                   `,.u.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 62 PumpSuspend 2015-04-21T22:45:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-21T22:45:00)
    0000   0x40 0x2d 0x16 0x15 0x0f                   @-...
    body (0)

#### RECORD 63 Bolus 2015-04-21T20:25:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'duration': 150, 'programmed': 2.5, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x19 0x17 0x05                        ....
    decimal
              1   25   23    5
    datetime (2015-04-21T20:25:41)
    0000   0x69 0x19 0xb4 0x15 0x0f                   i....
    body (0)

#### RECORD 64 PumpResume 2015-04-21T22:45:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-21T22:45:05)
    0000   0x45 0x2d 0x16 0x15 0x0f                   E-...
    body (0)

#### RECORD 65 SensorAlert 2015-04-21T22:55:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 62}
```
    op hex (3)
    0000   0x0b 0x66 0x3e                             .f>
    decimal
             11  102   62
    datetime (2015-04-21T22:55:55)
    0000   0x77 0x37 0x36 0xb5 0x0f                   w76..
    body (0)

#### RECORD 66 SensorAlert 2015-04-21T23:16:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 51}
```
    op hex (3)
    0000   0x0b 0x66 0x33                             .f3
    decimal
             11  102   51
    datetime (2015-04-21T23:16:53)
    0000   0x75 0x10 0x37 0xb5 0x0f                   u.7..
    body (0)

#### RECORD 67 SensorAlert 2015-04-21T23:35:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 68}
```
    op hex (3)
    0000   0x0b 0x66 0x44                             .fD
    decimal
             11  102   68
    datetime (2015-04-21T23:35:55)
    0000   0x77 0x23 0x37 0xb5 0x0f                   w#7..
    body (0)

#### RECORD 68 SensorAlert 2015-04-21T23:56:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 71}
```
    op hex (3)
    0000   0x0b 0x66 0x47                             .fG
    decimal
             11  102   71
    datetime (2015-04-21T23:56:53)
    0000   0x75 0x38 0x37 0xb5 0x0f                   u87..
    body (0)

#### RECORD 69 MResultTotals 2015-04-22T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime (2015-04-22T00:00:00)
    0000   0x55 0x0f                                  U.
    body (0)

#### RECORD 70 Model522ResultTotals 2015-04-22T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-22T00:00:00)
    0000   0x55 0x0f                                  U.
    body (41)
    hex
    0000   0x05 0x00 0x47 0x36 0x57 0x02 0x00 0x00    ..G6W...
    0008   0x05 0x0c 0x03 0x0c 0x3c 0x02 0x00 0x28    ....<..(
    0010   0x00 0x68 0x02 0x00 0x28 0x01 0xd8 0x5c    .h..(..\
    0018   0x00 0x28 0x08 0x00 0x00 0x00 0x03 0x02    .(......
    0020   0x01 0x00 0x00 0x40 0x89 0x33 0xff 0x16    ...@.3..
    0028   0x02                                       .
    decimal
              5    0   71   54   87    2    0    0
              5   12    3   12   60    2    0   40
              0  104    2    0   40    1  216   92
              0   40    8    0    0    0    3    2
              1    0    0   64  137   51  255   22
              2

#### RECORD 71 SensorAlert 2015-04-22T00:15:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 65}
```
    op hex (3)
    0000   0x0b 0x66 0x41                             .fA
    decimal
             11  102   65
    datetime (2015-04-22T00:15:55)
    0000   0x77 0x0f 0x20 0xb6 0x0f                   w. ..
    body (0)

#### RECORD 72 SensorAlert 2015-04-22T00:36:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 64}
```
    op hex (3)
    0000   0x0b 0x66 0x40                             .f@
    decimal
             11  102   64
    datetime (2015-04-22T00:36:53)
    0000   0x75 0x24 0x20 0xb6 0x0f                   u$ ..
    body (0)

#### RECORD 73 SensorAlert 2015-04-22T00:55:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 66}
```
    op hex (3)
    0000   0x0b 0x66 0x42                             .fB
    decimal
             11  102   66
    datetime (2015-04-22T00:55:55)
    0000   0x77 0x37 0x20 0xb6 0x0f                   w7 ..
    body (0)

#### RECORD 74 SensorAlert 2015-04-22T01:16:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 50}
```
    op hex (3)
    0000   0x0b 0x66 0x32                             .f2
    decimal
             11  102   50
    datetime (2015-04-22T01:16:53)
    0000   0x75 0x10 0x21 0xb6 0x0f                   u.!..
    body (0)

#### RECORD 75 SensorAlert 2015-04-22T01:35:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 48}
```
    op hex (3)
    0000   0x0b 0x66 0x30                             .f0
    decimal
             11  102   48
    datetime (2015-04-22T01:35:55)
    0000   0x77 0x23 0x21 0xb6 0x0f                   w#!..
    body (0)

#### RECORD 76 SensorAlert 2015-04-22T01:56:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 66}
```
    op hex (3)
    0000   0x0b 0x66 0x42                             .fB
    decimal
             11  102   66
    datetime (2015-04-22T01:56:53)
    0000   0x75 0x38 0x21 0xb6 0x0f                   u8!..
    body (0)

#### RECORD 77 SensorAlert 2015-04-22T04:27:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-22T04:27:12)
    0000   0x4c 0x1b 0x24 0xb6 0x0f                   L.$..
    body (0)

#### RECORD 78 SensorAlert 2015-04-22T06:36:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-22T06:36:53)
    0000   0x75 0x24 0x26 0xb6 0x0f                   u$&..
    body (0)

#### RECORD 79 PumpSuspend 2015-04-22T07:07:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-22T07:07:09)
    0000   0x49 0x07 0x07 0x16 0x0f                   I....
    body (0)

#### RECORD 80 PumpResume 2015-04-22T07:55:56 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-22T07:55:56)
    0000   0x78 0x37 0x07 0x16 0x0f                   x7...
    body (0)

#### RECORD 81 CalBGForPH 2015-04-22T07:57:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 327}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2015-04-22T07:57:10)
    0000   0x4a 0x39 0x27 0x76 0x8f                   J9'v.
    body (0)

#### RECORD 82 BGReceived 2015-04-22T07:57:10 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 327, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x28                                  ?(
    decimal
             63   40
    datetime (2015-04-22T07:57:10)
    0000   0x4a 0x39 0xe7 0x76 0x0f                   J9.v.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 83 BolusWizard 2015-04-22T07:57:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 51,
 '_byte[7]': 0,
 'bg': 327,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.1,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2015-04-22T07:57:27)
    0000   0x5b 0x39 0x07 0x16 0x0f                   [9...
    body (13)
    hex
    0000   0x00 0x51 0x0a 0x28 0x5a 0x33 0x00 0x00    .Q.(Z3..
    0008   0x00 0x00 0x00 0x33 0x78                   ...3x
    decimal
              0   81   10   40   90   51    0    0
              0    0    0   51  120

#### RECORD 84 Bolus 2015-04-22T07:57:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1, 'duration': 0, 'programmed': 5.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x33 0x33 0x00                        .33.
    decimal
              1   51   51    0
    datetime (2015-04-22T07:57:27)
    0000   0x5b 0x39 0x87 0x16 0x0f                   [9...
    body (0)

#### RECORD 85 SensorAlert 2015-04-22T08:06:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 254}
```
    op hex (3)
    0000   0x0b 0x65 0xfe                             .e.
    decimal
             11  101  254
    datetime (2015-04-22T08:06:44)
    0000   0x6c 0x06 0x28 0xb6 0x0f                   l.(..
    body (0)

#### RECORD 86 SensorAlert 2015-04-22T09:35:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 213}
```
    op hex (3)
    0000   0x0b 0x65 0xd5                             .e.
    decimal
             11  101  213
    datetime (2015-04-22T09:35:55)
    0000   0x77 0x23 0x29 0xb6 0x0f                   w#)..
    body (0)

#### RECORD 87 SensorAlert 2015-04-22T11:07:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 262}
```
    op hex (3)
    0000   0x0b 0x65 0x06                             .e.
    decimal
             11  101    6
    datetime (2015-04-22T11:07:12)
    0000   0x4c 0x07 0x2b 0xb6 0x8f                   L.+..
    body (0)

#### RECORD 88 CalBGForPH 2015-04-22T11:54:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 365}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2015-04-22T11:54:50)
    0000   0x72 0x36 0x2b 0x76 0x8f                   r6+v.
    body (0)

#### RECORD 89 BGReceived 2015-04-22T11:54:50 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 365, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2d                                  ?-
    decimal
             63   45
    datetime (2015-04-22T11:54:50)
    0000   0x72 0x36 0xab 0x76 0x0f                   r6.v.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 90 BolusWizard 2015-04-22T11:55:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 61,
 '_byte[7]': 0,
 'bg': 365,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 9.0,
 'carb_input': 25,
 'carb_ratio': 8,
 'correction_estimate': 1.3,
 'food_estimate': 3.1,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2015-04-22T11:55:26)
    0000   0x5a 0x37 0x0b 0x16 0x0f                   Z7...
    body (13)
    hex
    0000   0x19 0x51 0x08 0x28 0x5a 0x3d 0x1f 0x00    .Q.(Z=..
    0008   0x00 0x02 0x00 0x5a 0x78                   ...Zx
    decimal
             25   81    8   40   90   61   31    0
              0    2    0   90  120

#### RECORD 91 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 236, 'amount': 2.8}, {'age': 246, 'amount': 2.3}]
```
    op hex (8)
    0000   0x5c 0x08 0x70 0xec 0x04 0x5c 0xf6 0x04    \.p..\..
    decimal
             92    8  112  236    4   92  246    4
    datetime (unknown)

    body (0)

#### RECORD 92 Bolus 2015-04-22T11:55:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.4, 'duration': 0, 'programmed': 7.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x4a 0x4a 0x00                        .JJ.
    decimal
              1   74   74    0
    datetime (2015-04-22T11:55:26)
    0000   0x5a 0x37 0x8b 0x16 0x0f                   Z7...
    body (0)

`end ReadHistoryData-page-6.data: 93 records`
