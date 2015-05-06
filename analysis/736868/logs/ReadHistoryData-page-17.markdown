## START ReadHistoryData-page-17.data
#### STOPPING DOUBLE NULLS @ 1005, found 17 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0b 0x81                                  ..
##### DEBUG DECIMAL
             11  129
#### RECORD 0 SensorAlert 2015-03-01T01:59:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-01T01:59:30)
    0000   0x1e 0xfb 0x21 0xa1 0x0f                   ..!..
    body (0)

#### RECORD 1 SensorAlert 2015-03-01T02:20:57 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-01T02:20:57)
    0000   0x39 0xd4 0x22 0xa1 0x0f                   9."..
    body (0)

#### RECORD 2 SensorAlert 2015-03-01T03:49:28 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 224}
```
    op hex (3)
    0000   0x0b 0x65 0xe0                             .e.
    decimal
             11  101  224
    datetime (2015-03-01T03:49:28)
    0000   0x1c 0xf1 0x23 0xa1 0x0f                   ..#..
    body (0)

#### RECORD 3 BasalProfileStart 2015-03-01T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-01T04:00:00)
    0000   0x00 0xc0 0x04 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 4 SensorAlert 2015-03-01T04:25:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-01T04:25:45)
    0000   0x2d 0xd9 0x24 0xa1 0x0f                   -.$..
    body (0)

#### RECORD 5 SensorAlert 2015-03-01T05:19:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 187}
```
    op hex (3)
    0000   0x0b 0x65 0xbb                             .e.
    decimal
             11  101  187
    datetime (2015-03-01T05:19:30)
    0000   0x1e 0xd3 0x25 0xa1 0x0f                   ..%..
    body (0)

#### RECORD 6 SensorAlert 2015-03-01T05:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-01T05:38:00)
    0000   0x00 0xe6 0x25 0xa1 0x0f                   ..%..
    body (0)

#### RECORD 7 SensorAlert 2015-03-01T06:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-01T06:38:00)
    0000   0x00 0xe6 0x26 0xa1 0x0f                   ..&..
    body (0)

#### RECORD 8 BasalProfileStart 2015-03-01T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-01T07:00:00)
    0000   0x00 0xc0 0x07 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 9 SensorAlert 2015-03-01T07:08:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-01T07:08:00)
    0000   0x00 0xc8 0x27 0xa1 0x0f                   ..'..
    body (0)

#### RECORD 10 CalBGForPH 2015-03-01T07:19:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2015-03-01T07:19:09)
    0000   0x09 0xd3 0x27 0x61 0x0f                   ..'a.
    body (0)

#### RECORD 11 BGReceived 2015-03-01T07:19:09 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 151, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2015-03-01T07:19:09)
    0000   0x09 0xd3 0xe7 0x61 0x0f                   ...a.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 12 BolusWizard 2015-03-01T07:19:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 151,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x97                                  [.
    decimal
             91  151
    datetime (2015-03-01T07:19:19)
    0000   0x13 0xd3 0x07 0x01 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x1c 0x00    .P.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x1c 0x78         ......x
    decimal
              0   80    0  100   40   90   28    0
              0    0    0    0    0   28  120

#### RECORD 13 Bolus 2015-03-01T07:19:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7,
 'duration': 0,
 'programmed': 0.7,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x00 0x00    ........
    decimal
              1    0   28    0   28    0    0    0
    datetime (2015-03-01T07:19:19)
    0000   0x13 0xd3 0x47 0x01 0x0f                   ..G..
    body (0)

#### RECORD 14 SensorAlert 2015-03-01T08:10:09 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-01T08:10:09)
    0000   0x09 0xca 0x28 0xa1 0x0f                   ..(..
    body (0)

#### RECORD 15 SensorAlert 2015-03-01T08:20:57 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-03-01T08:20:57)
    0000   0x39 0xd4 0x28 0xa1 0x0f                   9.(..
    body (0)

#### RECORD 16 BolusWizard 2015-03-01T08:21:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.6,
 'carb_input': 46,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-01T08:21:28)
    0000   0x1c 0xd5 0x08 0x61 0x0f                   ...a.
    body (15)
    hex
    0000   0x2e 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    .P.d(Z..
    0008   0xb8 0x00 0x00 0x00 0x00 0xb8 0x78         ......x
    decimal
             46   80    0  100   40   90    0    0
            184    0    0    0    0  184  120

#### RECORD 17 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 62, 'amount': 0.7}]
```
    op hex (5)
    0000   0x5c 0x05 0x1c 0x3e 0x04                   \..>.
    decimal
             92    5   28   62    4
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2015-03-01T08:21:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6,
 'duration': 0,
 'programmed': 4.6,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0xb8 0x00 0xb8 0x00 0x18 0x00    ........
    decimal
              1    0  184    0  184    0   24    0
    datetime (2015-03-01T08:21:28)
    0000   0x1c 0xd5 0x48 0x61 0x0f                   ..Ha.
    body (0)

#### RECORD 19 Bolus 2015-03-01T08:41:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xc8 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  200    0
    datetime (2015-03-01T08:41:42)
    0000   0x2a 0xe9 0x48 0x61 0x0f                   *.Ha.
    body (0)

#### RECORD 20 PumpSuspend 2015-03-01T08:45:37 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-01T08:45:37)
    0000   0x25 0xed 0x08 0x01 0x0f                   %....
    body (0)

#### RECORD 21 BasalProfileStart 2015-03-01T09:15:06 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-01T09:15:06)
    0000   0x06 0xcf 0x09 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 22 PumpResume 2015-03-01T09:15:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-01T09:15:06)
    0000   0x06 0xcf 0x09 0x01 0x0f                   .....
    body (0)

#### RECORD 23 BasalProfileStart 2015-03-01T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-01T10:00:00)
    0000   0x00 0xc0 0x0a 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 24 SensorAlert 2015-03-01T11:45:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-03-01T11:45:45)
    0000   0x2d 0xed 0x2b 0xa1 0x0f                   -.+..
    body (0)

#### RECORD 25 Bolus 2015-03-01T11:47:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x20 0x00    ..P.P. .
    decimal
              1    0   80    0   80    0   32    0
    datetime (2015-03-01T11:47:43)
    0000   0x2b 0xef 0x4b 0x61 0x0f                   +.Ka.
    body (0)

#### RECORD 26 BasalProfileStart 2015-03-01T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-01T12:00:00)
    0000   0x00 0xc0 0x0c 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 27 BasalProfileStart 2015-03-01T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-01T15:00:00)
    0000   0x00 0xc0 0x0f 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 28 Bolus 2015-03-01T16:03:09 head[8], body[0] op[0x01]
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
    datetime (2015-03-01T16:03:09)
    0000   0x09 0xc3 0x50 0x61 0x0f                   ..Pa.
    body (0)

#### RECORD 29 LowBattery 2015-03-01T17:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2015-03-01T17:01:00)
    0000   0x00 0xc1 0x11 0x01 0x0f                   .....
    body (0)

#### RECORD 30 Bolus 2015-03-01T20:09:52 head[8], body[0] op[0x01]
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
    datetime (2015-03-01T20:09:52)
    0000   0x34 0xc9 0x54 0x61 0x0f                   4.Ta.
    body (0)

#### RECORD 31 Bolus 2015-03-01T20:18:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 4.5}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xb4 0x00    ........
    decimal
              1    0  160    0  160    0  180    0
    datetime (2015-03-01T20:18:30)
    0000   0x1e 0xd2 0x54 0x61 0x0f                   ..Ta.
    body (0)

#### RECORD 32 BolusWizard 2015-03-01T21:44:09 head[2], body[15] op[0x5b]
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
    datetime (2015-03-01T21:44:09)
    0000   0x09 0xec 0x15 0x61 0x0f                   ...a.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    2P.<(Z..
    0008   0x4c 0x00 0x00 0x00 0x01 0x4c 0x78         L....Lx
    decimal
             50   80    0   60   40   90    0    1
             76    0    0    0    1   76  120

#### RECORD 33 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 3.3},
 {'age': 95, 'amount': 5.2},
 {'age': 345, 'amount': 4.0}]
```
    op hex (11)
    0000   0x5c 0x0b 0x84 0x55 0x04 0xd0 0x5f 0x04    \..U.._.
    0008   0xa0 0x59 0x14                             .Y.
    decimal
             92   11  132   85    4  208   95    4
            160   89   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2015-03-01T21:44:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9,
 'duration': 0,
 'programmed': 1.9,
 'type': 'normal',
 'unabsorbed': 5.5}
```
    op hex (8)
    0000   0x01 0x01 0x4c 0x01 0x4c 0x00 0xdc 0x00    ..L.L...
    decimal
              1    1   76    1   76    0  220    0
    datetime (2015-03-01T21:44:09)
    0000   0x09 0xec 0x55 0x61 0x0f                   ..Ua.
    body (0)

#### RECORD 35 BasalProfileStart 2015-03-01T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-01T22:00:00)
    0000   0x00 0xc0 0x16 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 36 CalBGForPH 2015-03-01T22:17:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 208}
```
    op hex (2)
    0000   0x0a 0xd0                                  ..
    decimal
             10  208
    datetime (2015-03-01T22:17:08)
    0000   0x08 0xd1 0x36 0x61 0x0f                   ..6a.
    body (0)

#### RECORD 37 BGReceived 2015-03-01T22:17:08 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 208, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2015-03-01T22:17:08)
    0000   0x08 0xd1 0x16 0x61 0x0f                   ...a.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 38 BolusWizard 2015-03-01T22:17:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 208,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 2.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 11.4}
```
    op hex (2)
    0000   0x5b 0xd0                                  [.
    decimal
             91  208
    datetime (2015-03-01T22:17:13)
    0000   0x0d 0xd1 0x16 0x61 0x0f                   ...a.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x3c 0x28 0x5a 0x58 0x00    .P.<(ZX.
    0008   0x00 0x00 0x01 0xc8 0x00 0x00 0x78         ......x
    decimal
              0   80    0   60   40   90   88    0
              0    0    1  200    0    0  120

#### RECORD 39 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 0.4},
 {'age': 38, 'amount': 1.5},
 {'age': 118, 'amount': 3.3},
 {'age': 128, 'amount': 5.2},
 {'age': 378, 'amount': 4.0}]
```
    op hex (17)
    0000   0x5c 0x11 0x10 0x1c 0x04 0x3c 0x26 0x05    \....<&.
    0008   0x84 0x76 0x04 0xd0 0x80 0x04 0xa0 0x7a    .v.....z
    0010   0x14                                       .
    decimal
             92   17   16   28    4   60   38    5
            132  118    4  208  128    4  160  122
             20
    datetime (unknown)

    body (0)

#### RECORD 40 Battery 2015-03-01T22:17:56 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2015-03-01T22:17:56)
    0000   0x38 0xd1 0x16 0x01 0x0f                   8....
    body (0)

#### RECORD 41 Battery 2015-03-01T22:18:21 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2015-03-01T22:18:21)
    0000   0x15 0xd2 0x16 0x01 0x0f                   .....
    body (0)

#### RECORD 42 BasalProfileStart 2015-03-01T22:18:21 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-01T22:18:21)
    0000   0x15 0xd2 0x16 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 43 BasalProfileStart 2015-03-02T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-02T00:00:00)
    0000   0x00 0xc0 0x00 0x02 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 44 MResultTotals 2015-03-02T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xd2                   .....
    decimal
              7    0    0    7  210
    datetime (2015-03-02T00:00:00)
    0000   0x21 0x8f                                  !.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 45 Sara6E 2015-03-02T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-02T00:00:00)
    0000   0x21 0x8f                                  !.
    body (49)
    hex
    0000   0x05 0x00 0xb4 0x97 0xd0 0x02 0x00 0x00    ........
    0008   0x07 0xd2 0x03 0x1e 0x28 0x04 0xb4 0x3c    ....(..<
    0010   0x00 0x60 0x02 0x04 0x00 0x1c 0x00 0x00    .`......
    0018   0x02 0x94 0x02 0x01 0x00 0x05 0x00 0xa0    ........
    0020   0x28 0x3c 0x00 0x82 0x23 0x02 0x01 0x00    (<..#...
    0028   0x00 0x00 0x04 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  180  151  208    2    0    0
              7  210    3   30   40    4  180   60
              0   96    2    4    0   28    0    0
              2  148    2    1    0    5    0  160
             40   60    0  130   35    2    1    0
              0    0    4    0    0    0    0    0
              0

#### RECORD 46 BolusWizard 2015-03-02T01:34:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.5,
 'carb_input': 65,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-02T01:34:12)
    0000   0x0c 0xe2 0x01 0x62 0x0f                   ...b.
    body (15)
    hex
    0000   0x41 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    AP.d(Z..
    0008   0x04 0x00 0x00 0x00 0x01 0x04 0x78         ......x
    decimal
             65   80    0  100   40   90    0    1
              4    0    0    0    1    4  120

#### RECORD 47 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 225, 'amount': 0.4},
 {'age': 235, 'amount': 1.5},
 {'age': 315, 'amount': 3.3},
 {'age': 325, 'amount': 5.2}]
```
    op hex (14)
    0000   0x5c 0x0e 0x10 0xe1 0x04 0x3c 0xeb 0x05    \....<..
    0008   0x84 0x3b 0x14 0xd0 0x45 0x14              .;..E.
    decimal
             92   14   16  225    4   60  235    5
            132   59   20  208   69   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2015-03-02T01:36:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3,
 'duration': 180,
 'programmed': 3.3,
 'type': 'square',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x14 0x06    ........
    decimal
              1    0  132    0  132    0   20    6
    datetime (2015-03-02T01:36:20)
    0000   0x14 0xe4 0xa1 0x62 0x0f                   ...b.
    body (0)

#### RECORD 49 Bolus 2015-03-02T01:34:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2,
 'duration': 0,
 'programmed': 3.2,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x14 0x00    ........
    decimal
              1    0  128    0  128    0   20    0
    datetime (2015-03-02T01:34:12)
    0000   0x0c 0xe2 0x81 0x62 0x0f                   ...b.
    body (0)

#### RECORD 50 LowReservoir 2015-03-02T03:10:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-03-02T03:10:00)
    0000   0x00 0xca 0x03 0x02 0x0f                   .....
    body (0)

#### RECORD 51 BasalProfileStart 2015-03-02T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-02T04:00:00)
    0000   0x00 0xc0 0x04 0x02 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 52 Bolus 2015-03-02T06:16:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x18 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   24    0
    datetime (2015-03-02T06:16:12)
    0000   0x0c 0xd0 0x46 0x62 0x0f                   ..Fb.
    body (0)

#### RECORD 53 BasalProfileStart 2015-03-02T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-02T07:00:00)
    0000   0x00 0xc0 0x07 0x02 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 54 LowReservoir 2015-03-02T09:07:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-03-02T09:07:03)
    0000   0x03 0xc7 0x09 0x02 0x0f                   .....
    body (0)

#### RECORD 55 BasalProfileStart 2015-03-02T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-02T10:00:00)
    0000   0x00 0xc0 0x0a 0x02 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 56 BolusWizard 2015-03-02T10:08:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.0,
 'carb_input': 80,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 8.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-02T10:08:30)
    0000   0x1e 0xc8 0x0a 0x62 0x0f                   ...b.
    body (15)
    hex
    0000   0x50 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    PP.d(Z..
    0008   0x40 0x00 0x00 0x00 0x01 0x40 0x78         @....@x
    decimal
             80   80    0  100   40   90    0    1
             64    0    0    0    1   64  120

#### RECORD 57 UnabsorbedInsulinBolus unknown head[50], body[0] op[0x5c]
###### DECODED
```python
[{'age': 239, 'amount': 3.0},
 {'age': 339, 'amount': 0.15},
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
    op hex (50)
    0000   0x5c 0x32 0x78 0xef 0x04 0x06 0x53 0x14    \2x...S.
    0008   0x06 0x5d 0x14 0x08 0x67 0x14 0x08 0x71    .]..g..q
    0010   0x14 0x06 0x7b 0x14 0x08 0x85 0x14 0x08    ..{.....
    0018   0x8f 0x14 0x06 0x99 0x14 0x08 0xa3 0x14    ........
    0020   0x08 0xad 0x14 0x06 0xb7 0x14 0x08 0xc1    ........
    0028   0x14 0x08 0xcb 0x14 0x06 0xd5 0x14 0x08    ........
    0030   0xdf 0x14                                  ..
    decimal
             92   50  120  239    4    6   83   20
              6   93   20    8  103   20    8  113
             20    6  123   20    8  133   20    8
            143   20    6  153   20    8  163   20
              8  173   20    6  183   20    8  193
             20    8  203   20    6  213   20    8
            223   20
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2015-03-02T10:12:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 60,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x08 0x02    ..P.P...
    decimal
              1    0   80    0   80    0    8    2
    datetime (2015-03-02T10:12:35)
    0000   0x23 0xcc 0xaa 0x62 0x0f                   #..b.
    body (0)

#### RECORD 59 Bolus 2015-03-02T10:08:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0x08 0x00    ........
    decimal
              1    0  240    0  240    0    8    0
    datetime (2015-03-02T10:08:30)
    0000   0x1e 0xc8 0x8a 0x62 0x0f                   ...b.
    body (0)

#### RECORD 60 BasalProfileStart 2015-03-02T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-02T12:00:00)
    0000   0x00 0xc0 0x0c 0x02 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 61 BasalProfileStart 2015-03-02T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-02T15:00:00)
    0000   0x00 0xc0 0x0f 0x02 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 62 SensorAlert 2015-03-02T20:51:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-02T20:51:49)
    0000   0x31 0xf3 0x34 0xa2 0x0f                   1.4..
    body (0)

#### RECORD 63 SensorAlert 2015-03-02T21:21:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-02T21:21:00)
    0000   0x00 0xd5 0x35 0xa2 0x0f                   ..5..
    body (0)

#### RECORD 64 CalBGForPH 2015-03-02T21:35:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 388}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2015-03-02T21:35:34)
    0000   0x22 0xe3 0x35 0x62 0x8f                   ".5b.
    body (0)

#### RECORD 65 BGReceived 2015-03-02T21:35:34 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 388, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x30                                  ?0
    decimal
             63   48
    datetime (2015-03-02T21:35:34)
    0000   0x22 0xe3 0x95 0x62 0x0f                   "..b.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 66 BolusWizard 2015-03-02T21:35:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 388,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.7,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 6.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2015-03-02T21:35:54)
    0000   0x36 0xe3 0x15 0x02 0x0f                   6....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x3c 0x28 0x5a 0x0c 0x00    .Q.<(Z..
    0008   0x00 0x08 0x00 0x00 0x01 0x0c 0x78         ......x
    decimal
              0   81    0   60   40   90   12    0
              0    8    0    0    1   12  120

#### RECORD 67 Bolus 2015-03-02T21:35:54 head[8], body[0] op[0x01]
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
    datetime (2015-03-02T21:35:54)
    0000   0x36 0xe3 0xb5 0x02 0x0f                   6....
    body (0)

#### RECORD 68 Bolus 2015-03-02T21:35:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.55,
 'duration': 0,
 'programmed': 0.3,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x0c 0x00 0xb6 0x00 0x00 0x00    ........
    decimal
              1    1   12    0  182    0    0    0
    datetime (2015-03-02T21:35:54)
    0000   0x36 0xe3 0x95 0x02 0x0f                   6....
    body (0)

#### RECORD 69 NoDelivery 2015-03-02T21:38:59 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-02T21:38:59)
    0000   0x3b 0xe6 0x55 0x42 0x0f                   ;.UB.
    body (0)

#### RECORD 70 ClearAlarm 2015-03-02T21:40:16 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-02T21:40:16)
    0000   0x10 0xe8 0x15 0x02 0x0f                   .....
    body (0)

#### RECORD 71 Rewind 2015-03-02T21:40:19 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-03-02T21:40:19)
    0000   0x13 0xe8 0x15 0x02 0x0f                   .....
    body (0)

#### RECORD 72 Prime 2015-03-02T21:47:17 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x00                   .....
    decimal
              3    0    0    0    0
    datetime (2015-03-02T21:47:17)
    0000   0x11 0xef 0x35 0x02 0x0f                   ..5..
    body (0)

#### RECORD 73 SensorAlert 2015-03-02T21:47:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 388}
```
    op hex (3)
    0000   0x0b 0x65 0x84                             .e.
    decimal
             11  101  132
    datetime (2015-03-02T21:47:25)
    0000   0x19 0xef 0x35 0xa2 0x8f                   ..5..
    body (0)

#### RECORD 74 BasalProfileStart 2015-03-02T21:47:51 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-02T21:47:51)
    0000   0x33 0xef 0x15 0x02 0x0f                   3....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 75 Prime 2015-03-02T21:47:37 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-03-02T21:47:37)
    0000   0x25 0xef 0x15 0x02 0x0f                   %....
    body (0)

#### RECORD 76 CalBGForPH 2015-03-02T21:48:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 388}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2015-03-02T21:48:18)
    0000   0x12 0xf0 0x35 0x02 0x8f                   ..5..
    body (0)

#### RECORD 77 BolusWizard 2015-03-02T21:48:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 388,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 6.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 4.5}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2015-03-02T21:48:27)
    0000   0x1b 0xf0 0x15 0x62 0x0f                   ...b.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x3c 0x28 0x5a 0x0c 0x00    .Q.<(Z..
    0008   0x00 0x08 0x00 0xb4 0x00 0x58 0x78         .....Xx
    decimal
              0   81    0   60   40   90   12    0
              0    8    0  180    0   88  120

#### RECORD 78 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 4.55}]
```
    op hex (5)
    0000   0x5c 0x05 0xb6 0x13 0x04                   \....
    decimal
             92    5  182   19    4
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2015-03-02T21:48:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 4.5}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0xb4 0x00    ........
    decimal
              1    0    0    0    0    0  180    0
    datetime (2015-03-02T21:48:27)
    0000   0x1b 0xf0 0xb5 0x62 0x0f                   ...b.
    body (0)

#### RECORD 80 Bolus 2015-03-02T21:48:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2,
 'duration': 0,
 'programmed': 2.2,
 'type': 'normal',
 'unabsorbed': 4.5}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0xb4 0x00    ..X.X...
    decimal
              1    0   88    0   88    0  180    0
    datetime (2015-03-02T21:48:27)
    0000   0x1b 0xf0 0x95 0x62 0x0f                   ...b.
    body (0)

#### RECORD 81 BasalProfileStart 2015-03-02T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-02T22:00:00)
    0000   0x00 0xc0 0x16 0x02 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 82 BasalProfileStart 2015-03-03T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-03T00:00:00)
    0000   0x00 0xc0 0x00 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 83 MResultTotals 2015-03-03T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xf5                   .....
    decimal
              7    0    0    6  245
    datetime (2015-03-03T00:00:00)
    0000   0x22 0x8f                                  ".
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end ReadHistoryData-page-17.data: 84 records`
