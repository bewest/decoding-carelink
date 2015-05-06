## START ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 1002, found 20 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x48 0x49                                  HI
##### DEBUG DECIMAL
             72   73
#### RECORD 0 Sara6E 2015-03-11T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-11T00:00:00)
    0000   0x2a 0x8f                                  *.
    body (49)
    hex
    0000   0x05 0x10 0x9a 0x33 0x00 0x02 0x00 0x00    ...3....
    0008   0x0a 0x06 0x03 0x16 0x1f 0x06 0xf0 0x45    .......E
    0010   0x00 0x92 0x02 0xbc 0x01 0xb4 0x00 0x00    ........
    0018   0x02 0x80 0x03 0x02 0x00 0x07 0x00 0xc7    ........
    0020   0x37 0x2c 0x01 0x20 0x4e 0x02 0x01 0x00    7,. N...
    0028   0x00 0x01 0x09 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  154   51    0    2    0    0
             10    6    3   22   31    6  240   69
              0  146    2  188    1  180    0    0
              2  128    3    2    0    7    0  199
             55   44    1   32   78    2    1    0
              0    1    9    1    0    0    0    0
              0

#### RECORD 1 SensorAlert 2015-03-11T00:49:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-11T00:49:01)
    0000   0x01 0xf1 0x20 0xab 0x0f                   .. ..
    body (0)

#### RECORD 2 SensorAlert 2015-03-11T00:58:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-11T00:58:52)
    0000   0x34 0xfa 0x20 0xab 0x0f                   4. ..
    body (0)

#### RECORD 3 SensorAlert 2015-03-11T03:59:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 276}
```
    op hex (3)
    0000   0x0b 0x65 0x14                             .e.
    decimal
             11  101   20
    datetime (2015-03-11T03:59:20)
    0000   0x14 0xfb 0x23 0xab 0x8f                   ..#..
    body (0)

#### RECORD 4 BasalProfileStart 2015-03-11T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-11T04:00:00)
    0000   0x00 0xc0 0x04 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 5 SensorAlert 2015-03-11T05:29:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 346}
```
    op hex (3)
    0000   0x0b 0x65 0x5a                             .eZ
    decimal
             11  101   90
    datetime (2015-03-11T05:29:01)
    0000   0x01 0xdd 0x25 0xab 0x8f                   ..%..
    body (0)

#### RECORD 6 CalBGForPH 2015-03-11T06:44:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 392}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2015-03-11T06:44:48)
    0000   0x30 0xec 0x26 0x6b 0x8f                   0.&k.
    body (0)

#### RECORD 7 BGReceived 2015-03-11T06:44:48 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 392, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x31                                  ?1
    decimal
             63   49
    datetime (2015-03-11T06:44:48)
    0000   0x30 0xec 0x06 0x6b 0x0f                   0..k.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 8 BolusWizard 2015-03-11T06:45:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 392,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.8,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 6.8,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2015-03-11T06:45:08)
    0000   0x08 0xed 0x06 0x0b 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0x10 0x00    .Q.d(Z..
    0008   0x00 0x08 0x00 0x00 0x01 0x10 0x78         ......x
    decimal
              0   81    0  100   40   90   16    0
              0    8    0    0    1   16  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 446, 'amount': 1.5}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0xbe 0x14                   \.<..
    decimal
             92    5   60  190   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2015-03-11T06:45:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4,
 'duration': 0,
 'programmed': 0.4,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x10 0x01 0x10 0x00 0x00 0x00    ........
    decimal
              1    1   16    1   16    0    0    0
    datetime (2015-03-11T06:45:08)
    0000   0x08 0xed 0x46 0x0b 0x0f                   ..F..
    body (0)

#### RECORD 11 SensorAlert 2015-03-11T06:58:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 390}
```
    op hex (3)
    0000   0x0b 0x65 0x86                             .e.
    decimal
             11  101  134
    datetime (2015-03-11T06:58:52)
    0000   0x34 0xfa 0x26 0xab 0x8f                   4.&..
    body (0)

#### RECORD 12 BasalProfileStart 2015-03-11T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-11T07:00:00)
    0000   0x00 0xc0 0x07 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 13 PumpSuspend 2015-03-11T07:00:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-11T07:00:53)
    0000   0x35 0xc0 0x07 0x0b 0x0f                   5....
    body (0)

#### RECORD 14 BasalProfileStart 2015-03-11T07:20:46 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-11T07:20:46)
    0000   0x2e 0xd4 0x07 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 15 PumpResume 2015-03-11T07:20:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-11T07:20:46)
    0000   0x2e 0xd4 0x07 0x0b 0x0f                   .....
    body (0)

#### RECORD 16 BolusWizard 2015-03-11T07:32:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 36,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-11T07:32:51)
    0000   0x33 0xe0 0x07 0x6b 0x0f                   3..k.
    body (15)
    hex
    0000   0x24 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    $P.d(Z..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x78         ......x
    decimal
             36   80    0  100   40   90    0    0
            144    0    0    0    0  144  120

#### RECORD 17 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 1.15}, {'age': 53, 'amount': 5.65}]
```
    op hex (8)
    0000   0x5c 0x08 0x2e 0x2b 0x04 0xe2 0x35 0x04    \..+..5.
    decimal
             92    8   46   43    4  226   53    4
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2015-03-11T07:32:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6,
 'duration': 0,
 'programmed': 3.6,
 'type': 'normal',
 'unabsorbed': 5.9}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0xec 0x00    ........
    decimal
              1    0  144    0  144    0  236    0
    datetime (2015-03-11T07:32:51)
    0000   0x33 0xe0 0x47 0x6b 0x0f                   3.Gk.
    body (0)

#### RECORD 19 Bolus 2015-03-11T08:25:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x01 0x14 0x00    ........
    decimal
              1    0  180    0  180    1   20    0
    datetime (2015-03-11T08:25:11)
    0000   0x0b 0xd9 0x48 0x6b 0x0f                   ..Hk.
    body (0)

#### RECORD 20 SensorAlert 2015-03-11T08:52:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-11T08:52:44)
    0000   0x2c 0xf4 0x28 0xab 0x0f                   ,.(..
    body (0)

#### RECORD 21 BasalProfileStart 2015-03-11T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-11T10:00:00)
    0000   0x00 0xc0 0x0a 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 22 BasalProfileStart 2015-03-11T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-11T12:00:00)
    0000   0x00 0xc0 0x0c 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 23 SensorAlert 2015-03-11T12:58:51 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-11T12:58:51)
    0000   0x33 0xfa 0x2c 0xab 0x0f                   3.,..
    body (0)

#### RECORD 24 Bolus 2015-03-11T12:59:34 head[8], body[0] op[0x01]
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
    datetime (2015-03-11T12:59:34)
    0000   0x22 0xfb 0x4c 0x6b 0x0f                   ".Lk.
    body (0)

#### RECORD 25 SensorAlert 2015-03-11T13:08:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-11T13:08:02)
    0000   0x02 0xc8 0x2d 0xab 0x0f                   ..-..
    body (0)

#### RECORD 26 BasalProfileStart 2015-03-11T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-11T15:00:00)
    0000   0x00 0xc0 0x0f 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 27 SensorAlert 2015-03-11T17:45:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-11T17:45:00)
    0000   0x00 0xed 0x31 0xab 0x0f                   ..1..
    body (0)

#### RECORD 28 BolusWizard 2015-03-11T18:33:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.5,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 7.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-11T18:33:36)
    0000   0x24 0xe1 0x12 0x6b 0x0f                   $..k.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    -P.<(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             45   80    0   60   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 29 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 334, 'amount': 3.0}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x4e 0x14                   \.xN.
    decimal
             92    5  120   78   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2015-03-11T18:33:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1,
 'duration': 0,
 'programmed': 1.1,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x2c 0x01 0x2c 0x00 0x00 0x00    ..,.,...
    decimal
              1    1   44    1   44    0    0    0
    datetime (2015-03-11T18:33:36)
    0000   0x24 0xe1 0x52 0x6b 0x0f                   $.Rk.
    body (0)

#### RECORD 31 SensorAlert 2015-03-11T18:45:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-11T18:45:00)
    0000   0x00 0xed 0x32 0xab 0x0f                   ..2..
    body (0)

#### RECORD 32 SensorAlert 2015-03-11T19:15:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-11T19:15:00)
    0000   0x00 0xcf 0x33 0xab 0x0f                   ..3..
    body (0)

#### RECORD 33 CalBGForPH 2015-03-11T19:25:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 162}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2015-03-11T19:25:48)
    0000   0x30 0xd9 0x33 0x6b 0x0f                   0.3k.
    body (0)

#### RECORD 34 BGReceived 2015-03-11T19:25:48 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 162, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2015-03-11T19:25:48)
    0000   0x30 0xd9 0x53 0x6b 0x0f                   0.Sk.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 35 SensorAlert 2015-03-11T19:38:51 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-11T19:38:51)
    0000   0x33 0xe6 0x33 0xab 0x0f                   3.3..
    body (0)

#### RECORD 36 SensorAlert 2015-03-11T20:04:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-11T20:04:12)
    0000   0x0c 0xc4 0x34 0xab 0x0f                   ..4..
    body (0)

#### RECORD 37 BolusWizard 2015-03-11T21:18:50 head[2], body[15] op[0x5b]
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
    datetime (2015-03-11T21:18:50)
    0000   0x32 0xd2 0x15 0x6b 0x0f                   2..k.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    2P.<(Z..
    0008   0x4c 0x00 0x00 0x00 0x01 0x4c 0x78         L....Lx
    decimal
             50   80    0   60   40   90    0    1
             76    0    0    0    1   76  120

#### RECORD 38 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 169, 'amount': 1.1}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0xa9 0x05                   \.,..
    decimal
             92    5   44  169    5
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2015-03-11T21:21:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 60,
 'programmed': 1.8,
 'type': 'square',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x40 0x02    ..H.H.@.
    decimal
              1    0   72    0   72    0   64    2
    datetime (2015-03-11T21:21:38)
    0000   0x26 0xd5 0xb5 0x6b 0x0f                   &..k.
    body (0)

#### RECORD 40 Bolus 2015-03-11T21:18:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2,
 'duration': 0,
 'programmed': 4.2,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x40 0x00    ......@.
    decimal
              1    0  168    0  168    0   64    0
    datetime (2015-03-11T21:18:50)
    0000   0x32 0xd2 0x95 0x6b 0x0f                   2..k.
    body (0)

#### RECORD 41 SensorAlert 2015-03-11T21:32:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 261}
```
    op hex (3)
    0000   0x0b 0x65 0x05                             .e.
    decimal
             11  101    5
    datetime (2015-03-11T21:32:43)
    0000   0x2b 0xe0 0x35 0xab 0x8f                   +.5..
    body (0)

#### RECORD 42 BasalProfileStart 2015-03-11T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-11T22:00:00)
    0000   0x00 0xc0 0x16 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 43 SensorAlert 2015-03-11T23:42:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-11T23:42:45)
    0000   0x2d 0xea 0x37 0xab 0x0f                   -.7..
    body (0)

#### RECORD 44 BasalProfileStart 2015-03-12T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-12T00:00:00)
    0000   0x00 0xc0 0x00 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 45 MResultTotals 2015-03-12T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x0d                   .....
    decimal
              7    0    0    8   13
    datetime (2015-03-12T00:00:00)
    0000   0x2b 0x8f                                  +.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 46 Sara6E 2015-03-12T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-12T00:00:00)
    0000   0x2b 0x8f                                  +.
    body (49)
    hex
    0000   0x05 0x11 0x15 0xa2 0x88 0x02 0x00 0x00    ........
    0008   0x08 0x0d 0x03 0x25 0x27 0x04 0xe8 0x3d    ...%'..=
    0010   0x00 0x83 0x02 0xac 0x01 0x10 0x00 0x00    ........
    0018   0x01 0x2c 0x03 0x01 0x00 0x02 0x00 0xc1    .,......
    0020   0x2d 0x37 0x00 0x16 0x4d 0x04 0x01 0x00    -7..M...
    0028   0x00 0x00 0x07 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   17   21  162  136    2    0    0
              8   13    3   37   39    4  232   61
              0  131    2  172    1   16    0    0
              1   44    3    1    0    2    0  193
             45   55    0   22   77    4    1    0
              0    0    7    1    0    0    0    0
              0

#### RECORD 47 SensorAlert 2015-03-12T00:04:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-03-12T00:04:12)
    0000   0x0c 0xc4 0x20 0xac 0x0f                   .. ..
    body (0)

#### RECORD 48 SensorAlert 2015-03-12T01:32:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 204}
```
    op hex (3)
    0000   0x0b 0x65 0xcc                             .e.
    decimal
             11  101  204
    datetime (2015-03-12T01:32:43)
    0000   0x2b 0xe0 0x21 0xac 0x0f                   +.!..
    body (0)

#### RECORD 49 SensorAlert 2015-03-12T03:02:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 212}
```
    op hex (3)
    0000   0x0b 0x65 0xd4                             .e.
    decimal
             11  101  212
    datetime (2015-03-12T03:02:45)
    0000   0x2d 0xc2 0x23 0xac 0x0f                   -.#..
    body (0)

#### RECORD 50 Bolus 2015-03-12T03:28:48 head[8], body[0] op[0x01]
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
    datetime (2015-03-12T03:28:48)
    0000   0x30 0xdc 0x43 0x6c 0x0f                   0.Cl.
    body (0)

#### RECORD 51 BasalProfileStart 2015-03-12T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-12T04:00:00)
    0000   0x00 0xc0 0x04 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 52 SensorAlert 2015-03-12T06:09:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-12T06:09:00)
    0000   0x00 0xc9 0x26 0xac 0x0f                   ..&..
    body (0)

#### RECORD 53 SensorAlert 2015-03-12T06:22:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-03-12T06:22:45)
    0000   0x2d 0xd6 0x26 0xac 0x0f                   -.&..
    body (0)

#### RECORD 54 SensorAlert 2015-03-12T06:26:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-12T06:26:00)
    0000   0x00 0xda 0x26 0xac 0x0f                   ..&..
    body (0)

#### RECORD 55 SensorAlert 2015-03-12T06:52:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 76}
```
    op hex (3)
    0000   0x0b 0x66 0x4c                             .fL
    decimal
             11  102   76
    datetime (2015-03-12T06:52:43)
    0000   0x2b 0xf4 0x26 0xac 0x0f                   +.&..
    body (0)

#### RECORD 56 PumpSuspend 2015-03-12T06:59:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-12T06:59:21)
    0000   0x15 0xfb 0x06 0x0c 0x0f                   .....
    body (0)

#### RECORD 57 BasalProfileStart 2015-03-12T07:22:33 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-12T07:22:33)
    0000   0x21 0xd6 0x07 0x0c 0x0f                   !....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 58 PumpResume 2015-03-12T07:22:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-12T07:22:33)
    0000   0x21 0xd6 0x07 0x0c 0x0f                   !....
    body (0)

#### RECORD 59 SensorAlert 2015-03-12T07:26:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-12T07:26:00)
    0000   0x00 0xda 0x27 0xac 0x0f                   ..'..
    body (0)

#### RECORD 60 BolusWizard 2015-03-12T07:39:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.5,
 'carb_input': 55,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-12T07:39:12)
    0000   0x0c 0xe7 0x07 0x6c 0x0f                   ...l.
    body (15)
    hex
    0000   0x37 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    7P.d(Z..
    0008   0xdc 0x00 0x00 0x00 0x00 0xdc 0x78         ......x
    decimal
             55   80    0  100   40   90    0    0
            220    0    0    0    0  220  120

#### RECORD 61 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 250, 'amount': 2.2}, {'age': 260, 'amount': 0.3}]
```
    op hex (8)
    0000   0x5c 0x08 0x58 0xfa 0x04 0x0c 0x04 0x14    \.X.....
    decimal
             92    8   88  250    4   12    4   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2015-03-12T07:39:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5,
 'duration': 0,
 'programmed': 5.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xdc 0x00 0xdc 0x00 0x00 0x00    ........
    decimal
              1    0  220    0  220    0    0    0
    datetime (2015-03-12T07:39:13)
    0000   0x0d 0xe7 0x47 0x6c 0x0f                   ..Gl.
    body (0)

#### RECORD 63 SensorAlert 2015-03-12T07:56:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-12T07:56:00)
    0000   0x00 0xf8 0x27 0xac 0x0f                   ..'..
    body (0)

#### RECORD 64 SensorAlert 2015-03-12T08:26:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-12T08:26:00)
    0000   0x00 0xda 0x28 0xac 0x0f                   ..(..
    body (0)

#### RECORD 65 SensorAlert 2015-03-12T08:56:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-12T08:56:00)
    0000   0x00 0xf8 0x28 0xac 0x0f                   ..(..
    body (0)

#### RECORD 66 CalBGForPH 2015-03-12T08:57:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 68}
```
    op hex (2)
    0000   0x0a 0x44                                  .D
    decimal
             10   68
    datetime (2015-03-12T08:57:16)
    0000   0x10 0xf9 0x28 0x6c 0x0f                   ..(l.
    body (0)

#### RECORD 67 BGReceived 2015-03-12T08:57:16 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 68, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2015-03-12T08:57:16)
    0000   0x10 0xf9 0x88 0x6c 0x0f                   ...l.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 68 BolusWizard 2015-03-12T08:57:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 68,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.9,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_estimate': 50.6,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 4.0}
```
    op hex (2)
    0000   0x5b 0x44                                  [D
    decimal
             91   68
    datetime (2015-03-12T08:57:47)
    0000   0x2f 0xf9 0x08 0x6c 0x0f                   /..l.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x64 0x28 0x5a 0xe8 0x00    -P.d(Z..
    0008   0xb4 0xf8 0x00 0xa0 0x00 0x9c 0x78         ......x
    decimal
             45   80    0  100   40   90  232    0
            180  248    0  160    0  156  120

#### RECORD 69 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 78, 'amount': 5.5},
 {'age': 328, 'amount': 2.2},
 {'age': 338, 'amount': 0.3}]
```
    op hex (11)
    0000   0x5c 0x0b 0xdc 0x4e 0x04 0x58 0x48 0x14    \..N.XH.
    0008   0x0c 0x52 0x14                             .R.
    decimal
             92   11  220   78    4   88   72   20
             12   82   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2015-03-12T08:57:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 180,
 'programmed': 3.0,
 'type': 'square',
 'unabsorbed': 4.0}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xa0 0x06    ..x.x...
    decimal
              1    0  120    0  120    0  160    6
    datetime (2015-03-12T08:57:47)
    0000   0x2f 0xf9 0x68 0x6c 0x0f                   /.hl.
    body (0)

#### RECORD 71 SensorAlert 2015-03-12T09:08:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-12T09:08:02)
    0000   0x02 0xc8 0x29 0xac 0x0f                   ..)..
    body (0)

#### RECORD 72 SensorAlert 2015-03-12T09:13:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 79}
```
    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-03-12T09:13:24)
    0000   0x18 0xcd 0x29 0xac 0x0f                   ..)..
    body (0)

#### RECORD 73 SensorAlert 2015-03-12T09:42:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 79}
```
    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-03-12T09:42:45)
    0000   0x2d 0xea 0x29 0xac 0x0f                   -.)..
    body (0)

#### RECORD 74 BasalProfileStart 2015-03-12T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-12T10:00:00)
    0000   0x00 0xc0 0x0a 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 75 SensorAlert 2015-03-12T10:33:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-03-12T10:33:24)
    0000   0x18 0xe1 0x2a 0xac 0x0f                   ..*..
    body (0)

#### RECORD 76 SensorAlert 2015-03-12T10:33:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-12T10:33:39)
    0000   0x27 0xe1 0x2a 0xac 0x0f                   '.*..
    body (0)

#### RECORD 77 CalBGForPH 2015-03-12T10:34:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2015-03-12T10:34:38)
    0000   0x26 0xe2 0x2a 0x6c 0x0f                   &.*l.
    body (0)

#### RECORD 78 BGReceived 2015-03-12T10:34:38 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 160, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2015-03-12T10:34:38)
    0000   0x26 0xe2 0x0a 0x6c 0x0f                   &..l.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 79 SensorAlert 2015-03-12T10:58:51 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-12T10:58:51)
    0000   0x33 0xfa 0x2a 0xac 0x0f                   3.*..
    body (0)

#### RECORD 80 SensorAlert 2015-03-12T11:08:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-03-12T11:08:02)
    0000   0x02 0xc8 0x2b 0xac 0x0f                   ..+..
    body (0)

#### RECORD 81 BasalProfileStart 2015-03-12T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-12T12:00:00)
    0000   0x00 0xc0 0x0c 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 82 SensorAlert 2015-03-12T12:39:19 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 209}
```
    op hex (3)
    0000   0x0b 0x65 0xd1                             .e.
    decimal
             11  101  209
    datetime (2015-03-12T12:39:19)
    0000   0x13 0xe7 0x2c 0xac 0x0f                   ..,..
    body (0)

#### RECORD 83 Bolus 2015-03-12T12:41:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.2}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x30 0x00    ..x.x.0.
    decimal
              1    0  120    0  120    0   48    0
    datetime (2015-03-12T12:41:36)
    0000   0x24 0xe9 0x4c 0x6c 0x0f                   $.Ll.
    body (0)

#### RECORD 84 BasalProfileStart 2015-03-12T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-12T15:00:00)
    0000   0x00 0xc0 0x0f 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 85 SensorAlert 2015-03-12T15:13:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-12T15:13:24)
    0000   0x18 0xcd 0x2f 0xac 0x0f                   ../..
    body (0)

#### RECORD 86 SensorAlert 2015-03-12T15:24:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-12T15:24:12)
    0000   0x0c 0xd8 0x2f 0xac 0x0f                   ../..
    body (0)

#### RECORD 87 SensorAlert 2015-03-12T15:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-12T15:34:00)
    0000   0x00 0xe2 0x2f 0xac 0x0f                   ../..
    body (0)

#### RECORD 88 SensorAlert 2015-03-12T16:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-12T16:34:00)
    0000   0x00 0xe2 0x30 0xac 0x0f                   ..0..
    body (0)

#### RECORD 89 CalBGForPH 2015-03-12T16:37:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 218}
```
    op hex (2)
    0000   0x0a 0xda                                  ..
    decimal
             10  218
    datetime (2015-03-12T16:37:00)
    0000   0x00 0xe5 0x30 0x6c 0x0f                   ..0l.
    body (0)

#### RECORD 90 BGReceived 2015-03-12T16:37:00 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 218, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2015-03-12T16:37:00)
    0000   0x00 0xe5 0x50 0x6c 0x0f                   ..Pl.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 91 BolusWizard 2015-03-12T16:37:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 218,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 2.4,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0xda                                  [.
    decimal
             91  218
    datetime (2015-03-12T16:37:32)
    0000   0x20 0xe5 0x10 0x6c 0x0f                    ..l.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x60 0x00    .P.P(Z`.
    0008   0x00 0x00 0x00 0x08 0x00 0x58 0x78         .....Xx
    decimal
              0   80    0   80   40   90   96    0
              0    0    0    8    0   88  120

`end ReadHistoryData-page-11.data: 92 records`
