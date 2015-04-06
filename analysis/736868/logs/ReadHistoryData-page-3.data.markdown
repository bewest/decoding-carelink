## START analysis/736868/logs/ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6c 0xf0                                  l.
##### DEBUG DECIMAL
            108  240
#### RECORD 0 Sara6E 2015-03-24T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-24T00:00:00)
    0000   0x37 0x8f                                  7.
    body (49)
    hex
    0000   0x05 0x00 0xa3 0x8d 0xb5 0x03 0x00 0x00    ........
    0008   0x07 0x5d 0x03 0x21 0x2a 0x04 0x3c 0x3a    .].!*.<:
    0010   0x00 0xc5 0x03 0xdc 0x00 0x10 0x00 0x00    ........
    0018   0x00 0x50 0x04 0x01 0x00 0x01 0x00 0xa5    .P......
    0020   0x29 0x3b 0x00 0xa9 0x20 0x04 0x00 0x00    );.. ...
    0028   0x00 0x00 0x06 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  163  141  181    3    0    0
              7   93    3   33   42    4   60   58
              0  197    3  220    0   16    0    0
              0   80    4    1    0    1    0  165
             41   59    0  169   32    4    0    0
              0    0    6    0    0    0    0    0
              0

#### RECORD 1 SensorAlert 2015-03-24T00:12:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-24T00:12:38)
    0000   0x26 0xcc 0x20 0xb8 0x0f                   &. ..
    body (0)

#### RECORD 2 SensorAlert 2015-03-24T00:16:32 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-03-24T00:16:32)
    0000   0x20 0xd0 0x20 0xb8 0x0f                    . ..
    body (0)

#### RECORD 3 SensorAlert 2015-03-24T00:46:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 61}
```
    op hex (3)
    0000   0x0b 0x66 0x3d                             .f=
    decimal
             11  102   61
    datetime (2015-03-24T00:46:30)
    0000   0x1e 0xee 0x20 0xb8 0x0f                   .. ..
    body (0)

#### RECORD 4 SensorAlert 2015-03-24T01:17:59 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 60}
```
    op hex (3)
    0000   0x0b 0x66 0x3c                             .f<
    decimal
             11  102   60
    datetime (2015-03-24T01:17:59)
    0000   0x3b 0xd1 0x21 0xb8 0x0f                   ;.!..
    body (0)

#### RECORD 5 SensorAlert 2015-03-24T01:47:11 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-03-24T01:47:11)
    0000   0x0b 0xef 0x21 0xb8 0x0f                   ..!..
    body (0)

#### RECORD 6 Bolus 2015-03-24T02:55:35 head[8], body[0] op[0x01]
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
    datetime (2015-03-24T02:55:35)
    0000   0x23 0xf7 0x42 0x78 0x0f                   #.Bx.
    body (0)

#### RECORD 7 BasalProfileStart 2015-03-24T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-24T04:00:00)
    0000   0x00 0xc0 0x04 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 8 SensorAlert 2015-03-24T04:02:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-24T04:02:47)
    0000   0x2f 0xc2 0x24 0xb8 0x0f                   /.$..
    body (0)

#### RECORD 9 Bolus 2015-03-24T04:12:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x38 0x00    ..P.P.8.
    decimal
              1    0   80    0   80    0   56    0
    datetime (2015-03-24T04:12:19)
    0000   0x13 0xcc 0x44 0x78 0x0f                   ..Dx.
    body (0)

#### RECORD 10 SensorAlert 2015-03-24T04:16:32 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-03-24T04:16:32)
    0000   0x20 0xd0 0x24 0xb8 0x0f                    .$..
    body (0)

#### RECORD 11 SensorAlert 2015-03-24T05:41:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-24T05:41:49)
    0000   0x31 0xe9 0x25 0xb8 0x0f                   1.%..
    body (0)

#### RECORD 12 SensorAlert 2015-03-24T05:47:11 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-24T05:47:11)
    0000   0x0b 0xef 0x25 0xb8 0x0f                   ..%..
    body (0)

#### RECORD 13 Bolus 2015-03-24T06:53:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x14 0x00    ..<.<...
    decimal
              1    0   60    0   60    0   20    0
    datetime (2015-03-24T06:53:59)
    0000   0x3b 0xf5 0x46 0x78 0x0f                   ;.Fx.
    body (0)

#### RECORD 14 BasalProfileStart 2015-03-24T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-24T07:00:00)
    0000   0x00 0xc0 0x07 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 15 PumpSuspend 2015-03-24T07:17:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-24T07:17:49)
    0000   0x31 0xd1 0x07 0x18 0x0f                   1....
    body (0)

#### RECORD 16 SensorAlert 2015-03-24T07:17:59 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 216}
```
    op hex (3)
    0000   0x0b 0x65 0xd8                             .e.
    decimal
             11  101  216
    datetime (2015-03-24T07:17:59)
    0000   0x3b 0xd1 0x27 0xb8 0x0f                   ;.'..
    body (0)

#### RECORD 17 BasalProfileStart 2015-03-24T07:39:33 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-24T07:39:33)
    0000   0x21 0xe7 0x07 0x18 0x0f                   !....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 18 PumpResume 2015-03-24T07:39:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-24T07:39:33)
    0000   0x21 0xe7 0x07 0x18 0x0f                   !....
    body (0)

#### RECORD 19 LowReservoir 2015-03-24T08:08:49 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-03-24T08:08:49)
    0000   0x31 0xc8 0x08 0x18 0x0f                   1....
    body (0)

#### RECORD 20 BolusWizard 2015-03-24T08:15:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-24T08:15:22)
    0000   0x16 0xcf 0x08 0x78 0x0f                   ...x.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    (P.d(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             40   80    0  100   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 21 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 1.5, 'curve': 4},
 {'age': 246, 'amount': 2.0, 'curve': 4},
 {'age': 70, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0x56 0x04 0x50 0xf6 0x04    \.<V.P..
    0008   0x50 0x46 0x14                             PF.
    decimal
             92   11   60   86    4   80  246    4
             80   70   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2015-03-24T08:17:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 30,
 'programmed': 0.5,
 'type': 'square',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x28 0x01    ......(.
    decimal
              1    0   20    0   20    0   40    1
    datetime (2015-03-24T08:17:44)
    0000   0x2c 0xd1 0xa8 0x78 0x0f                   ,..x.
    body (0)

#### RECORD 23 Bolus 2015-03-24T08:15:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x28 0x00    ......(.
    decimal
              1    0  140    0  140    0   40    0
    datetime (2015-03-24T08:15:22)
    0000   0x16 0xcf 0x88 0x78 0x0f                   ...x.
    body (0)

#### RECORD 24 SensorAlert 2015-03-24T08:46:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 205}
```
    op hex (3)
    0000   0x0b 0x65 0xcd                             .e.
    decimal
             11  101  205
    datetime (2015-03-24T08:46:47)
    0000   0x2f 0xee 0x28 0xb8 0x0f                   /.(..
    body (0)

#### RECORD 25 SensorAlert 2015-03-24T09:30:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-24T09:30:00)
    0000   0x00 0xde 0x29 0xb8 0x0f                   ..)..
    body (0)

#### RECORD 26 BasalProfileStart 2015-03-24T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-24T10:00:00)
    0000   0x00 0xc0 0x0a 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 27 SensorAlert 2015-03-24T10:30:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-24T10:30:00)
    0000   0x00 0xde 0x2a 0xb8 0x0f                   ..*..
    body (0)

#### RECORD 28 CalBGForPH 2015-03-24T10:31:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2015-03-24T10:31:01)
    0000   0x01 0xdf 0x2a 0x78 0x0f                   ..*x.
    body (0)

#### RECORD 29 BGReceived 2015-03-24T10:31:01 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2015-03-24T10:31:01)
    0000   0x01 0xdf 0x2a 0x78 0x0f                   ..*x.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 30 SensorAlert 2015-03-24T10:56:32 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-24T10:56:32)
    0000   0x20 0xf8 0x2a 0xb8 0x0f                    .*..
    body (0)

#### RECORD 31 SensorAlert 2015-03-24T11:22:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-24T11:22:47)
    0000   0x2f 0xd6 0x2b 0xb8 0x0f                   /.+..
    body (0)

#### RECORD 32 BasalProfileStart 2015-03-24T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-24T12:00:00)
    0000   0x00 0xc0 0x0c 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 33 SensorAlert 2015-03-24T12:52:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 213}
```
    op hex (3)
    0000   0x0b 0x65 0xd5                             .e.
    decimal
             11  101  213
    datetime (2015-03-24T12:52:38)
    0000   0x26 0xf4 0x2c 0xb8 0x0f                   &.,..
    body (0)

#### RECORD 34 BolusWizard 2015-03-24T13:01:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.1,
 'carb_input': 52,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-24T13:01:05)
    0000   0x05 0xc1 0x0d 0x78 0x0f                   ...x.
    body (15)
    hex
    0000   0x34 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    4P.P(Z..
    0008   0x04 0x00 0x00 0x00 0x01 0x04 0x78         ......x
    decimal
             52   80    0   80   40   90    0    1
              4    0    0    0    1    4  120

#### RECORD 35 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 0.15, 'curve': 20},
 {'age': 16, 'amount': 0.15, 'curve': 20},
 {'age': 26, 'amount': 0.175, 'curve': 20},
 {'age': 36, 'amount': 3.525, 'curve': 20},
 {'age': 116, 'amount': 1.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x06 0x06 0x14 0x06 0x10 0x14    \.......
    0008   0x07 0x1a 0x14 0x8d 0x24 0x14 0x3c 0x74    ....$.<t
    0010   0x14                                       .
    decimal
             92   17    6    6   20    6   16   20
              7   26   20  141   36   20   60  116
             20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2015-03-24T13:04:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4,
 'duration': 60,
 'programmed': 1.4,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x02    ..8.8...
    decimal
              1    0   56    0   56    0    0    2
    datetime (2015-03-24T13:04:32)
    0000   0x20 0xc4 0xad 0x78 0x0f                    ..x.
    body (0)

#### RECORD 37 LowReservoir 2015-03-24T13:02:22 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-03-24T13:02:22)
    0000   0x16 0xc2 0x0d 0x18 0x0f                   .....
    body (0)

#### RECORD 38 Bolus 2015-03-24T13:01:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1,
 'duration': 0,
 'programmed': 5.1,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xcc 0x00 0xcc 0x00 0x00 0x00    ........
    decimal
              1    0  204    0  204    0    0    0
    datetime (2015-03-24T13:01:06)
    0000   0x06 0xc1 0x8d 0x78 0x0f                   ...x.
    body (0)

#### RECORD 39 BasalProfileStart 2015-03-24T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-24T15:00:00)
    0000   0x00 0xc0 0x0f 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 40 SensorAlert 2015-03-24T16:37:59 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-24T16:37:59)
    0000   0x3b 0xe5 0x30 0xb8 0x0f                   ;.0..
    body (0)

#### RECORD 41 SensorAlert 2015-03-24T17:01:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-24T17:01:49)
    0000   0x31 0xc1 0x31 0xb8 0x0f                   1.1..
    body (0)

#### RECORD 42 SensorAlert 2015-03-24T18:33:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 220}
```
    op hex (3)
    0000   0x0b 0x65 0xdc                             .e.
    decimal
             11  101  220
    datetime (2015-03-24T18:33:06)
    0000   0x06 0xe1 0x32 0xb8 0x0f                   ..2..
    body (0)

#### RECORD 43 Bolus 2015-03-24T18:33:55 head[8], body[0] op[0x01]
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
    datetime (2015-03-24T18:33:55)
    0000   0x37 0xe1 0x52 0x78 0x0f                   7.Rx.
    body (0)

#### RECORD 44 BolusWizard 2015-03-24T20:17:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 30,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-24T20:17:41)
    0000   0x29 0xd1 0x14 0x78 0x0f                   )..x.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             30   80    0   60   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 45 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 2.0, 'curve': 4},
 {'age': 122, 'amount': 0.15, 'curve': 20},
 {'age': 132, 'amount': 0.2, 'curve': 20},
 {'age': 142, 'amount': 0.25, 'curve': 20},
 {'age': 152, 'amount': 0.25, 'curve': 20},
 {'age': 162, 'amount': 0.2, 'curve': 20},
 {'age': 172, 'amount': 0.25, 'curve': 20},
 {'age': 182, 'amount': 5.2, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x50 0x6c 0x04 0x06 0x7a 0x14    \.Pl..z.
    0008   0x08 0x84 0x14 0x0a 0x8e 0x14 0x0a 0x98    ........
    0010   0x14 0x08 0xa2 0x14 0x0a 0xac 0x14 0xd0    ........
    0018   0xb6 0x14                                  ..
    decimal
             92   26   80  108    4    6  122   20
              8  132   20   10  142   20   10  152
             20    8  162   20   10  172   20  208
            182   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2015-03-24T20:17:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x2c 0x00    ......,.
    decimal
              1    0  200    0  200    0   44    0
    datetime (2015-03-24T20:17:41)
    0000   0x29 0xd1 0x54 0x78 0x0f                   ).Tx.
    body (0)

#### RECORD 47 SensorAlert 2015-03-24T20:27:11 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-24T20:27:11)
    0000   0x0b 0xdb 0x34 0xb8 0x0f                   ..4..
    body (0)

#### RECORD 48 SensorAlert 2015-03-24T21:31:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-24T21:31:00)
    0000   0x00 0xdf 0x35 0xb8 0x0f                   ..5..
    body (0)

#### RECORD 49 BasalProfileStart 2015-03-24T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-24T22:00:00)
    0000   0x00 0xc0 0x16 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 50 SensorAlert 2015-03-24T22:21:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-24T22:21:49)
    0000   0x31 0xd5 0x36 0xb8 0x0f                   1.6..
    body (0)

#### RECORD 51 Bolus 2015-03-24T22:22:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x5c 0x00    ..<.<.\.
    decimal
              1    0   60    0   60    0   92    0
    datetime (2015-03-24T22:22:06)
    0000   0x06 0xd6 0x56 0x78 0x0f                   ..Vx.
    body (0)

#### RECORD 52 SensorAlert 2015-03-24T22:31:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-24T22:31:00)
    0000   0x00 0xdf 0x36 0xb8 0x0f                   ..6..
    body (0)

#### RECORD 53 Bolus 2015-03-24T22:32:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 3.3}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x84 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  132    0
    datetime (2015-03-24T22:32:26)
    0000   0x1a 0xe0 0x56 0x78 0x0f                   ..Vx.
    body (0)

#### RECORD 54 SensorAlert 2015-03-24T23:01:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-24T23:01:00)
    0000   0x00 0xc1 0x37 0xb8 0x0f                   ..7..
    body (0)

#### RECORD 55 CalBGForPH 2015-03-24T23:21:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 205}
```
    op hex (2)
    0000   0x0a 0xcd                                  ..
    decimal
             10  205
    datetime (2015-03-24T23:21:25)
    0000   0x19 0xd5 0x37 0x78 0x0f                   ..7x.
    body (0)

#### RECORD 56 BGReceived 2015-03-24T23:21:25 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2015-03-24T23:21:25)
    0000   0x19 0xd5 0xb7 0x78 0x0f                   ...x.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 57 NoDelivery 2015-03-24T23:21:44 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-24T23:21:44)
    0000   0x2c 0xd5 0x57 0x58 0x0f                   ,.WX.
    body (0)

#### RECORD 58 ClearAlarm 2015-03-24T23:21:48 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-24T23:21:48)
    0000   0x30 0xd5 0x17 0x18 0x0f                   0....
    body (0)

#### RECORD 59 Rewind 2015-03-24T23:21:56 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-03-24T23:21:56)
    0000   0x38 0xd5 0x17 0x18 0x0f                   8....
    body (0)

#### RECORD 60 Prime 2015-03-24T23:23:12 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x43                   ....C
    decimal
              3    0    0    0   67
    datetime (2015-03-24T23:23:12)
    0000   0x0c 0xd7 0x37 0x18 0x0f                   ..7..
    body (0)

#### RECORD 61 BasalProfileStart 2015-03-24T23:23:55 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-24T23:23:55)
    0000   0x37 0xd7 0x17 0x18 0x0f                   7....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 62 Prime 2015-03-24T23:23:41 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-03-24T23:23:41)
    0000   0x29 0xd7 0x17 0x18 0x0f                   )....
    body (0)

#### RECORD 63 Bolus 2015-03-24T23:25:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 2.8}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x70 0x00    ......p.
    decimal
              1    0   20    0   20    0  112    0
    datetime (2015-03-24T23:25:40)
    0000   0x28 0xd9 0x57 0x78 0x0f                   (.Wx.
    body (0)

#### RECORD 64 SensorAlert 2015-03-24T23:36:32 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 202}
```
    op hex (3)
    0000   0x0b 0x65 0xca                             .e.
    decimal
             11  101  202
    datetime (2015-03-24T23:36:32)
    0000   0x20 0xe4 0x37 0xb8 0x0f                    .7..
    body (0)

#### RECORD 65 BasalProfileStart 2015-03-25T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-25T00:00:00)
    0000   0x00 0xc0 0x00 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 66 MResultTotals 2015-03-25T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x43                   ....C
    decimal
              7    0    0    7   67
    datetime (2015-03-25T00:00:00)
    0000   0x38 0x8f                                  8.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 67 Sara6E 2015-03-25T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-25T00:00:00)
    0000   0x38 0x8f                                  8.
    body (49)
    hex
    0000   0x05 0x00 0xb7 0xa1 0xcd 0x02 0x00 0x00    ........
    0008   0x07 0x43 0x03 0x23 0x2b 0x04 0x20 0x39    .C.#+. 9
    0010   0x00 0x7a 0x02 0x7c 0x00 0x00 0x00 0x00    .z.|....
    0018   0x01 0xa4 0x03 0x00 0x00 0x07 0x00 0xa4    ........
    0020   0x26 0x37 0x07 0x11 0x30 0x06 0x01 0x00    &7..0...
    0028   0x00 0x04 0x09 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  183  161  205    2    0    0
              7   67    3   35   43    4   32   57
              0  122    2  124    0    0    0    0
              1  164    3    0    0    7    0  164
             38   55    7   17   48    6    1    0
              0    4    9    1    0    0    0    0
              0

#### RECORD 68 SensorAlert 2015-03-25T01:07:11 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 246}
```
    op hex (3)
    0000   0x0b 0x65 0xf6                             .e.
    decimal
             11  101  246
    datetime (2015-03-25T01:07:11)
    0000   0x0b 0xc7 0x21 0xb9 0x0f                   ..!..
    body (0)

#### RECORD 69 Bolus 2015-03-25T01:42:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x14 0x00    ..<.<...
    decimal
              1    0   60    0   60    0   20    0
    datetime (2015-03-25T01:42:20)
    0000   0x14 0xea 0x41 0x79 0x0f                   ..Ay.
    body (0)

#### RECORD 70 Bolus 2015-03-25T01:45:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x50 0x00    ..P.P.P.
    decimal
              1    0   80    0   80    0   80    0
    datetime (2015-03-25T01:45:00)
    0000   0x00 0xed 0x41 0x79 0x0f                   ..Ay.
    body (0)

#### RECORD 71 SensorAlert 2015-03-25T02:37:58 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 232}
```
    op hex (3)
    0000   0x0b 0x65 0xe8                             .e.
    decimal
             11  101  232
    datetime (2015-03-25T02:37:58)
    0000   0x3a 0xe5 0x22 0xb9 0x0f                   :."..
    body (0)

#### RECORD 72 BasalProfileStart 2015-03-25T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-25T04:00:00)
    0000   0x00 0xc0 0x04 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 73 SensorAlert 2015-03-25T04:06:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-25T04:06:29)
    0000   0x1d 0xc6 0x24 0xb9 0x0f                   ..$..
    body (0)

#### RECORD 74 SensorAlert 2015-03-25T04:33:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-25T04:33:05)
    0000   0x05 0xe1 0x24 0xb9 0x0f                   ..$..
    body (0)

#### RECORD 75 SensorAlert 2015-03-25T06:02:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-25T06:02:46)
    0000   0x2e 0xc2 0x26 0xb9 0x0f                   ..&..
    body (0)

#### RECORD 76 BasalProfileStart 2015-03-25T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-25T07:00:00)
    0000   0x00 0xc0 0x07 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 77 PumpSuspend 2015-03-25T07:02:47 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-25T07:02:47)
    0000   0x2f 0xc2 0x07 0x19 0x0f                   /....
    body (0)

#### RECORD 78 BasalProfileStart 2015-03-25T07:45:09 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-25T07:45:09)
    0000   0x09 0xed 0x07 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 79 PumpResume 2015-03-25T07:45:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-25T07:45:09)
    0000   0x09 0xed 0x07 0x19 0x0f                   .....
    body (0)

#### RECORD 80 BolusWizard 2015-03-25T07:45:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 60,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-25T07:45:26)
    0000   0x1a 0xed 0x07 0x79 0x0f                   ...y.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    <P.d(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             60   80    0  100   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 81 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 110, 'amount': 3.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x6e 0x14                   \..n.
    decimal
             92    5  140  110   20
    datetime (unknown)

    body (0)

#### RECORD 82 Bolus 2015-03-25T07:48:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 60,
 'programmed': 1.5,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x02    ..<.<...
    decimal
              1    0   60    0   60    0    0    2
    datetime (2015-03-25T07:48:28)
    0000   0x1c 0xf0 0xa7 0x79 0x0f                   ...y.
    body (0)

#### RECORD 83 Bolus 2015-03-25T07:45:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x00 0x00    ........
    decimal
              1    0  180    0  180    0    0    0
    datetime (2015-03-25T07:45:26)
    0000   0x1a 0xed 0x87 0x79 0x0f                   ...y.
    body (0)

#### RECORD 84 SensorAlert 2015-03-25T09:01:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-25T09:01:48)
    0000   0x30 0xc1 0x29 0xb9 0x0f                   0.)..
    body (0)

#### RECORD 85 BasalProfileStart 2015-03-25T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-25T10:00:00)
    0000   0x00 0xc0 0x0a 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 86 SensorAlert 2015-03-25T10:21:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-25T10:21:00)
    0000   0x00 0xd5 0x2a 0xb9 0x0f                   ..*..
    body (0)

#### RECORD 87 SensorAlert 2015-03-25T11:21:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-25T11:21:00)
    0000   0x00 0xd5 0x2b 0xb9 0x0f                   ..+..
    body (0)

#### RECORD 88 SensorAlert 2015-03-25T11:51:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-25T11:51:00)
    0000   0x00 0xf3 0x2b 0xb9 0x0f                   ..+..
    body (0)

#### RECORD 89 BasalProfileStart 2015-03-25T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-25T12:00:00)
    0000   0x00 0xc0 0x0c 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 90 SensorAlert 2015-03-25T12:21:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-25T12:21:00)
    0000   0x00 0xd5 0x2c 0xb9 0x0f                   ..,..
    body (0)

#### RECORD 91 CalBGForPH 2015-03-25T12:26:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2015-03-25T12:26:23)
    0000   0x17 0xda 0x2c 0x79 0x0f                   ..,y.
    body (0)

`end analysis/736868/logs/ReadHistoryData-page-3.data: 92 records`
