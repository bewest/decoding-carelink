## START ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x92 0x48                                  .H
##### DEBUG DECIMAL
            146   72
#### RECORD 0 BGReceived 2015-03-25T12:26:23 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 105, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2015-03-25T12:26:23)
    0000   0x17 0xda 0x2c 0x79 0x0f                   ..,y.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 1 SensorAlert 2015-03-25T14:02:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-25T14:02:46)
    0000   0x2e 0xc2 0x2e 0xb9 0x0f                   .....
    body (0)

#### RECORD 2 SensorAlert 2015-03-25T14:46:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-25T14:46:29)
    0000   0x1d 0xee 0x2e 0xb9 0x0f                   .....
    body (0)

#### RECORD 3 Bolus 2015-03-25T14:57:28 head[8], body[0] op[0x01]
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
    datetime (2015-03-25T14:57:28)
    0000   0x1c 0xf9 0x4e 0x79 0x0f                   ..Ny.
    body (0)

#### RECORD 4 BasalProfileStart 2015-03-25T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-25T15:00:00)
    0000   0x00 0xc0 0x0f 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 5 SensorAlert 2015-03-25T17:41:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-25T17:41:48)
    0000   0x30 0xe9 0x31 0xb9 0x0f                   0.1..
    body (0)

#### RECORD 6 SensorAlert 2015-03-25T18:27:10 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-25T18:27:10)
    0000   0x0a 0xdb 0x32 0xb9 0x0f                   ..2..
    body (0)

#### RECORD 7 Base (2015, 3, 25, 18, 31, 6) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2015, 3, 25, 18, 31, 6))
    0000   0x06 0xdf 0x12 0x19 0x0f                   .....
    body (0)

#### RECORD 8 SensorAlert 2015-03-25T18:33:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 79}
```
    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-03-25T18:33:05)
    0000   0x05 0xe1 0x32 0xb9 0x0f                   ..2..
    body (0)

#### RECORD 9 SensorAlert 2015-03-25T19:47:10 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-25T19:47:10)
    0000   0x0a 0xef 0x33 0xb9 0x0f                   ..3..
    body (0)

#### RECORD 10 SensorAlert 2015-03-25T20:33:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-25T20:33:05)
    0000   0x05 0xe1 0x34 0xb9 0x0f                   ..4..
    body (0)

#### RECORD 11 Bolus 2015-03-25T20:33:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2015-03-25T20:33:18)
    0000   0x12 0xe1 0x54 0x79 0x0f                   ..Ty.
    body (0)

#### RECORD 12 BolusWizard 2015-03-25T20:40:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.5,
 'carb_input': 80,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 13.3,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-25T20:40:22)
    0000   0x16 0xe8 0x14 0x79 0x0f                   ...y.
    body (15)
    hex
    0000   0x50 0x50 0x00 0x3c 0x28 0x5a 0x00 0x02    PP.<(Z..
    0008   0x14 0x00 0x00 0x00 0x02 0x14 0x78         ......x
    decimal
             80   80    0   60   40   90    0    2
             20    0    0    0    2   20  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 1.5}, {'age': 351, 'amount': 2.0}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x0b 0x04 0x50 0x5f 0x14    \.<..P_.
    decimal
             92    8   60   11    4   80   95   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2015-03-25T20:43:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9,
 'duration': 180,
 'programmed': 3.9,
 'type': 'square',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x3c 0x06    ......<.
    decimal
              1    0  156    0  156    0   60    6
    datetime (2015-03-25T20:43:06)
    0000   0x06 0xeb 0xb4 0x79 0x0f                   ...y.
    body (0)

#### RECORD 15 Bolus 2015-03-25T20:40:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1,
 'duration': 0,
 'programmed': 4.1,
 'type': 'normal',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x3c 0x00    ......<.
    decimal
              1    0  164    0  164    0   60    0
    datetime (2015-03-25T20:40:22)
    0000   0x16 0xe8 0x94 0x79 0x0f                   ...y.
    body (0)

#### RECORD 16 BasalProfileStart 2015-03-25T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-25T22:00:00)
    0000   0x00 0xc0 0x16 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 17 SensorAlert 2015-03-25T22:12:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-25T22:12:37)
    0000   0x25 0xcc 0x36 0xb9 0x0f                   %.6..
    body (0)

#### RECORD 18 SensorAlert 2015-03-25T22:27:10 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-25T22:27:10)
    0000   0x0a 0xdb 0x36 0xb9 0x0f                   ..6..
    body (0)

#### RECORD 19 SensorAlert 2015-03-25T23:26:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-25T23:26:00)
    0000   0x00 0xda 0x37 0xb9 0x0f                   ..7..
    body (0)

#### RECORD 20 CalBGForPH 2015-03-25T23:27:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2015-03-25T23:27:21)
    0000   0x15 0xdb 0x37 0x79 0x0f                   ..7y.
    body (0)

#### RECORD 21 BGReceived 2015-03-25T23:27:21 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 127, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2015-03-25T23:27:21)
    0000   0x15 0xdb 0xf7 0x79 0x0f                   ...y.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 22 BasalProfileStart 2015-03-26T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-26T00:00:00)
    0000   0x00 0xc0 0x00 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 23 MResultTotals 2015-03-26T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x60                   ....`
    decimal
              7    0    0    6   96
    datetime (2015-03-26T00:00:00)
    0000   0x39 0x8f                                  9.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 24 Sara6E 2015-03-26T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-26T00:00:00)
    0000   0x39 0x8f                                  9.
    body (49)
    hex
    0000   0x05 0x00 0x74 0x69 0x7f 0x02 0x00 0x00    ..ti....
    0008   0x06 0x60 0x03 0x18 0x31 0x03 0x48 0x33    .`..1.H3
    0010   0x00 0x8c 0x02 0x30 0x00 0x00 0x00 0x00    ...0....
    0018   0x01 0x18 0x02 0x00 0x00 0x04 0x00 0x9f    ........
    0020   0x20 0x43 0x01 0x10 0x2e 0x04 0x03 0x00     C......
    0028   0x00 0x01 0x07 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  116  105  127    2    0    0
              6   96    3   24   49    3   72   51
              0  140    2   48    0    0    0    0
              1   24    2    0    0    4    0  159
             32   67    1   16   46    4    3    0
              0    1    7    1    0    0    0    0
              0

#### RECORD 25 SensorAlert 2015-03-26T03:07:10 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-26T03:07:10)
    0000   0x0a 0xc7 0x23 0xba 0x0f                   ..#..
    body (0)

#### RECORD 26 BasalProfileStart 2015-03-26T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-26T04:00:00)
    0000   0x00 0xc0 0x04 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 27 SensorAlert 2015-03-26T05:47:10 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-26T05:47:10)
    0000   0x0a 0xef 0x25 0xba 0x0f                   ..%..
    body (0)

#### RECORD 28 PumpSuspend 2015-03-26T06:59:42 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-26T06:59:42)
    0000   0x2a 0xfb 0x06 0x1a 0x0f                   *....
    body (0)

#### RECORD 29 BasalProfileStart 2015-03-26T08:00:27 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-26T08:00:27)
    0000   0x1b 0xc0 0x08 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 30 PumpResume 2015-03-26T08:00:27 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-26T08:00:27)
    0000   0x1b 0xc0 0x08 0x1a 0x0f                   .....
    body (0)

#### RECORD 31 BolusWizard 2015-03-26T08:00:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-26T08:00:46)
    0000   0x2e 0xc0 0x08 0x7a 0x0f                   ...z.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    <P.d(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             60   80    0  100   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 32 Bolus 2015-03-26T08:02:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 60,
 'programmed': 3.0,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x02    ..x.x...
    decimal
              1    0  120    0  120    0    0    2
    datetime (2015-03-26T08:02:47)
    0000   0x2f 0xc2 0xa8 0x7a 0x0f                   /..z.
    body (0)

#### RECORD 33 Bolus 2015-03-26T08:00:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    0    0
    datetime (2015-03-26T08:00:46)
    0000   0x2e 0xc0 0x88 0x7a 0x0f                   ...z.
    body (0)

#### RECORD 34 SensorAlert 2015-03-26T09:01:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-26T09:01:47)
    0000   0x2f 0xc1 0x29 0xba 0x0f                   /.)..
    body (0)

#### RECORD 35 SensorAlert 2015-03-26T09:13:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 76}
```
    op hex (3)
    0000   0x0b 0x66 0x4c                             .fL
    decimal
             11  102   76
    datetime (2015-03-26T09:13:04)
    0000   0x04 0xcd 0x29 0xba 0x0f                   ..)..
    body (0)

#### RECORD 36 SensorAlert 2015-03-26T09:41:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 72}
```
    op hex (3)
    0000   0x0b 0x66 0x48                             .fH
    decimal
             11  102   72
    datetime (2015-03-26T09:41:47)
    0000   0x2f 0xe9 0x29 0xba 0x0f                   /.)..
    body (0)

#### RECORD 37 SensorAlert 2015-03-26T09:47:09 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-03-26T09:47:09)
    0000   0x09 0xef 0x29 0xba 0x0f                   ..)..
    body (0)

#### RECORD 38 SensorAlert 2015-03-26T09:47:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-26T09:47:24)
    0000   0x18 0xef 0x29 0xba 0x0f                   ..)..
    body (0)

#### RECORD 39 CalBGForPH 2015-03-26T09:48:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 57}
```
    op hex (2)
    0000   0x0a 0x39                                  .9
    decimal
             10   57
    datetime (2015-03-26T09:48:51)
    0000   0x33 0xf0 0x29 0x7a 0x0f                   3.)z.
    body (0)

#### RECORD 40 BGReceived 2015-03-26T09:48:51 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 57, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2015-03-26T09:48:51)
    0000   0x33 0xf0 0x29 0x7a 0x0f                   3.)z.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 41 BasalProfileStart 2015-03-26T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-26T10:00:00)
    0000   0x00 0xc0 0x0a 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 42 SensorAlert 2015-03-26T10:02:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 57}
```
    op hex (3)
    0000   0x0b 0x66 0x39                             .f9
    decimal
             11  102   57
    datetime (2015-03-26T10:02:45)
    0000   0x2d 0xc2 0x2a 0xba 0x0f                   -.*..
    body (0)

#### RECORD 43 SensorAlert 2015-03-26T10:33:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 63}
```
    op hex (3)
    0000   0x0b 0x66 0x3f                             .f?
    decimal
             11  102   63
    datetime (2015-03-26T10:33:04)
    0000   0x04 0xe1 0x2a 0xba 0x0f                   ..*..
    body (0)

#### RECORD 44 SensorAlert 2015-03-26T11:01:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 73}
```
    op hex (3)
    0000   0x0b 0x66 0x49                             .fI
    decimal
             11  102   73
    datetime (2015-03-26T11:01:47)
    0000   0x2f 0xc1 0x2b 0xba 0x0f                   /.+..
    body (0)

#### RECORD 45 SensorAlert 2015-03-26T11:32:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 78}
```
    op hex (3)
    0000   0x0b 0x66 0x4e                             .fN
    decimal
             11  102   78
    datetime (2015-03-26T11:32:36)
    0000   0x24 0xe0 0x2b 0xba 0x0f                   $.+..
    body (0)

#### RECORD 46 BasalProfileStart 2015-03-26T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-26T12:00:00)
    0000   0x00 0xc0 0x0c 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 47 SensorAlert 2015-03-26T12:02:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 76}
```
    op hex (3)
    0000   0x0b 0x66 0x4c                             .fL
    decimal
             11  102   76
    datetime (2015-03-26T12:02:45)
    0000   0x2d 0xc2 0x2c 0xba 0x0f                   -.,..
    body (0)

#### RECORD 48 SensorAlert 2015-03-26T14:16:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-26T14:16:30)
    0000   0x1e 0xd0 0x2e 0xba 0x0f                   .....
    body (0)

#### RECORD 49 SensorAlert 2015-03-26T14:49:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-26T14:49:00)
    0000   0x00 0xf1 0x2e 0xba 0x0f                   .....
    body (0)

#### RECORD 50 SensorAlert 2015-03-26T14:56:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-03-26T14:56:30)
    0000   0x1e 0xf8 0x2e 0xba 0x0f                   .....
    body (0)

#### RECORD 51 BasalProfileStart 2015-03-26T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-26T15:00:00)
    0000   0x00 0xc0 0x0f 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 52 SensorAlert 2015-03-26T15:49:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-26T15:49:00)
    0000   0x00 0xf1 0x2f 0xba 0x0f                   ../..
    body (0)

#### RECORD 53 CalBGForPH 2015-03-26T15:49:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 285}
```
    op hex (2)
    0000   0x0a 0x1d                                  ..
    decimal
             10   29
    datetime (2015-03-26T15:49:51)
    0000   0x33 0xf1 0x2f 0x7a 0x8f                   3./z.
    body (0)

#### RECORD 54 BGReceived 2015-03-26T15:49:51 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 285, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2015-03-26T15:49:51)
    0000   0x33 0xf1 0xaf 0x7a 0x0f                   3..z.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 55 BolusWizard 2015-03-26T15:50:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 285,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.1,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': -2.3,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x1d                                  [.
    decimal
             91   29
    datetime (2015-03-26T15:50:04)
    0000   0x04 0xf2 0x0f 0x1a 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x50 0x28 0x5a 0xa4 0x00    .Q.P(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0xa4 0x78         ......x
    decimal
              0   81    0   80   40   90  164    0
              0    0    0    0    0  164  120

#### RECORD 56 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 411, 'amount': 0.2},
 {'age': 421, 'amount': 0.5},
 {'age': 431, 'amount': 0.5},
 {'age': 441, 'amount': 0.5},
 {'age': 451, 'amount': 0.5},
 {'age': 461, 'amount': 0.5},
 {'age': 471, 'amount': 3.3}]
```
    op hex (23)
    0000   0x5c 0x17 0x08 0x9b 0x14 0x14 0xa5 0x14    \.......
    0008   0x14 0xaf 0x14 0x14 0xb9 0x14 0x14 0xc3    ........
    0010   0x14 0x14 0xcd 0x14 0x84 0xd7 0x14         .......
    decimal
             92   23    8  155   20   20  165   20
             20  175   20   20  185   20   20  195
             20   20  205   20  132  215   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2015-03-26T15:50:04 head[8], body[0] op[0x01]
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
    datetime (2015-03-26T15:50:04)
    0000   0x04 0xf2 0xaf 0x1a 0x0f                   .....
    body (0)

#### RECORD 58 Bolus 2015-03-26T15:50:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1,
 'duration': 0,
 'programmed': 4.1,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x00 0x00    ........
    decimal
              1    0  164    0  164    0    0    0
    datetime (2015-03-26T15:50:04)
    0000   0x04 0xf2 0x8f 0x1a 0x0f                   .....
    body (0)

#### RECORD 59 SensorAlert 2015-03-26T16:02:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 282}
```
    op hex (3)
    0000   0x0b 0x65 0x1a                             .e.
    decimal
             11  101   26
    datetime (2015-03-26T16:02:45)
    0000   0x2d 0xc2 0x30 0xba 0x8f                   -.0..
    body (0)

#### RECORD 60 SensorAlert 2015-03-26T18:27:09 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-26T18:27:09)
    0000   0x09 0xdb 0x32 0xba 0x0f                   ..2..
    body (0)

#### RECORD 61 BolusWizard 2015-03-26T18:29:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 30,
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
    datetime (2015-03-26T18:29:20)
    0000   0x14 0xdd 0x12 0x7a 0x0f                   ...z.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             30   80    0   60   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 62 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 160, 'amount': 4.1}]
```
    op hex (5)
    0000   0x5c 0x05 0xa4 0xa0 0x04                   \....
    decimal
             92    5  164  160    4
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2015-03-26T18:29:20 head[8], body[0] op[0x01]
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
    datetime (2015-03-26T18:29:20)
    0000   0x14 0xdd 0x52 0x7a 0x0f                   ..Rz.
    body (0)

#### RECORD 64 BolusWizard 2015-03-26T21:04:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.7,
 'carb_input': 55,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 9.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-26T21:04:01)
    0000   0x01 0xc4 0x15 0x7a 0x0f                   ...z.
    body (15)
    hex
    0000   0x37 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    7P.<(Z..
    0008   0x6c 0x00 0x00 0x00 0x01 0x6c 0x78         l....lx
    decimal
             55   80    0   60   40   90    0    1
            108    0    0    0    1  108  120

#### RECORD 65 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 5.0}, {'age': 315, 'amount': 4.1}]
```
    op hex (8)
    0000   0x5c 0x08 0xc8 0x9b 0x04 0xa4 0x3b 0x14    \.....;.
    decimal
             92    8  200  155    4  164   59   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2015-03-26T21:07:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9,
 'duration': 60,
 'programmed': 2.9,
 'type': 'square',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x38 0x02    ..t.t.8.
    decimal
              1    0  116    0  116    0   56    2
    datetime (2015-03-26T21:07:14)
    0000   0x0e 0xc7 0xb5 0x7a 0x0f                   ...z.
    body (0)

#### RECORD 67 Bolus 2015-03-26T21:04:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8,
 'duration': 0,
 'programmed': 4.8,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0xc0 0x00 0xc0 0x00 0x38 0x00    ......8.
    decimal
              1    0  192    0  192    0   56    0
    datetime (2015-03-26T21:04:01)
    0000   0x01 0xc4 0x95 0x7a 0x0f                   ...z.
    body (0)

#### RECORD 68 BasalProfileStart 2015-03-26T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-26T22:00:00)
    0000   0x00 0xc0 0x16 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 69 SensorAlert 2015-03-26T22:56:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-26T22:56:30)
    0000   0x1e 0xf8 0x36 0xba 0x0f                   ..6..
    body (0)

#### RECORD 70 CalBGForPH 2015-03-26T23:08:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 58}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2015-03-26T23:08:27)
    0000   0x1b 0xc8 0x37 0x7a 0x0f                   ..7z.
    body (0)

#### RECORD 71 BGReceived 2015-03-26T23:08:27 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 58, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2015-03-26T23:08:27)
    0000   0x1b 0xc8 0x57 0x7a 0x0f                   ..Wz.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 72 BasalProfileStart 2015-03-27T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-27T00:00:00)
    0000   0x00 0xc0 0x00 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 73 MResultTotals 2015-03-27T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x9d                   .....
    decimal
              7    0    0    6  157
    datetime (2015-03-27T00:00:00)
    0000   0x3a 0x8f                                  :.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 74 Sara6E 2015-03-27T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-27T00:00:00)
    0000   0x3a 0x8f                                  :.
    body (49)
    hex
    0000   0x05 0x10 0x85 0x39 0x1d 0x03 0x00 0x00    ...9....
    0008   0x06 0x9d 0x03 0x0d 0x2e 0x03 0x90 0x36    .......6
    0010   0x00 0x91 0x02 0xec 0x00 0xa4 0x00 0x00    ........
    0018   0x00 0x00 0x03 0x01 0x00 0x00 0x00 0x8c    ........
    0020   0x08 0x51 0x0b 0x1b 0x2a 0x04 0x02 0x00    .Q..*...
    0028   0x00 0x07 0x02 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  133   57   29    3    0    0
              6  157    3   13   46    3  144   54
              0  145    2  236    0  164    0    0
              0    0    3    1    0    0    0  140
              8   81   11   27   42    4    2    0
              0    7    2    1    0    0    0    0
              0

#### RECORD 75 SensorAlert 2015-03-27T01:22:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-27T01:22:45)
    0000   0x2d 0xd6 0x21 0xbb 0x0f                   -.!..
    body (0)

#### RECORD 76 SensorAlert 2015-03-27T01:32:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-27T01:32:36)
    0000   0x24 0xe0 0x21 0xbb 0x0f                   $.!..
    body (0)

#### RECORD 77 Bolus 2015-03-27T02:18:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x00 0x00    ........
    decimal
              1    0   20    0   20    0    0    0
    datetime (2015-03-27T02:18:42)
    0000   0x2a 0xd2 0x42 0x7b 0x0f                   *.B{.
    body (0)

#### RECORD 78 SensorAlert 2015-03-27T03:01:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 231}
```
    op hex (3)
    0000   0x0b 0x65 0xe7                             .e.
    decimal
             11  101  231
    datetime (2015-03-27T03:01:47)
    0000   0x2f 0xc1 0x23 0xbb 0x0f                   /.#..
    body (0)

#### RECORD 79 BasalProfileStart 2015-03-27T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-27T04:00:00)
    0000   0x00 0xc0 0x04 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 80 SensorAlert 2015-03-27T04:33:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 219}
```
    op hex (3)
    0000   0x0b 0x65 0xdb                             .e.
    decimal
             11  101  219
    datetime (2015-03-27T04:33:04)
    0000   0x04 0xe1 0x24 0xbb 0x0f                   ..$..
    body (0)

#### RECORD 81 SensorAlert 2015-03-27T06:02:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 224}
```
    op hex (3)
    0000   0x0b 0x65 0xe0                             .e.
    decimal
             11  101  224
    datetime (2015-03-27T06:02:45)
    0000   0x2d 0xc2 0x26 0xbb 0x0f                   -.&..
    body (0)

#### RECORD 82 Bolus 2015-03-27T06:46:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2015-03-27T06:46:24)
    0000   0x18 0xee 0x46 0x7b 0x0f                   ..F{.
    body (0)

#### RECORD 83 PumpSuspend 2015-03-27T06:59:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-27T06:59:44)
    0000   0x2c 0xfb 0x06 0x1b 0x0f                   ,....
    body (0)

#### RECORD 84 BasalProfileStart 2015-03-27T08:15:20 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-27T08:15:20)
    0000   0x14 0xcf 0x08 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 85 PumpResume 2015-03-27T08:15:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-27T08:15:20)
    0000   0x14 0xcf 0x08 0x1b 0x0f                   .....
    body (0)

#### RECORD 86 BolusWizard 2015-03-27T08:15:35 head[2], body[15] op[0x5b]
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
    datetime (2015-03-27T08:15:35)
    0000   0x23 0xcf 0x08 0x7b 0x0f                   #..{.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    (P.d(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             40   80    0  100   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 87 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 1.5},
 {'age': 356, 'amount': 0.275},
 {'age': 366, 'amount': 0.225}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0x60 0x04 0x0b 0x64 0x14    \.<`..d.
    0008   0x09 0x6e 0x14                             .n.
    decimal
             92   11   60   96    4   11  100   20
              9  110   20
    datetime (unknown)

    body (0)

#### RECORD 88 Bolus 2015-03-27T08:15:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x28 0x00    ......(.
    decimal
              1    0    0    0    0    0   40    0
    datetime (2015-03-27T08:15:35)
    0000   0x23 0xcf 0xa8 0x7b 0x0f                   #..{.
    body (0)

#### RECORD 89 Bolus 2015-03-27T08:15:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x28 0x00    ......(.
    decimal
              1    0  160    0  160    0   40    0
    datetime (2015-03-27T08:15:35)
    0000   0x23 0xcf 0x88 0x7b 0x0f                   #..{.
    body (0)

#### RECORD 90 SensorAlert 2015-03-27T08:21:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-27T08:21:47)
    0000   0x2f 0xd5 0x28 0xbb 0x0f                   /.(..
    body (0)

`end ReadHistoryData-page-2.data: 91 records`
