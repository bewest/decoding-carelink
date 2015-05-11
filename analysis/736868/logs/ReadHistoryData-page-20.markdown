## START ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe9 0x77                                  .w
##### DEBUG DECIMAL
            233  119
#### RECORD 0 SensorAlert 2015-02-25T02:25:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose Predicted', 'alarm_type': 115}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-25T02:25:48)
    0000   0x30 0x99 0x22 0xb9 0x0f                   0."..
    body (0)

#### RECORD 1 SensorAlert 2015-02-25T02:35:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 76}
```
    op hex (3)
    0000   0x0b 0x66 0x4c                             .fL
    decimal
             11  102   76
    datetime (2015-02-25T02:35:39)
    0000   0x27 0xa3 0x22 0xb9 0x0f                   '."..
    body (0)

#### RECORD 2 BasalProfileStart 2015-02-25T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-25T04:00:00)
    0000   0x00 0x80 0x04 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 3 SensorAlert 2015-02-25T06:29:31 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose Predicted', 'alarm_type': 115}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-25T06:29:31)
    0000   0x1f 0x9d 0x26 0xb9 0x0f                   ..&..
    body (0)

#### RECORD 4 PumpSuspend 2015-02-25T06:54:48 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-25T06:54:48)
    0000   0x30 0xb6 0x06 0x19 0x0f                   0....
    body (0)

#### RECORD 5 SensorAlert 2015-02-25T07:19:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-25T07:19:33)
    0000   0x21 0x93 0x27 0xb9 0x0f                   !.'..
    body (0)

#### RECORD 6 BasalProfileStart 2015-02-25T07:19:46 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-25T07:19:46)
    0000   0x2e 0x93 0x07 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 7 PumpResume 2015-02-25T07:19:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-25T07:19:46)
    0000   0x2e 0x93 0x07 0x19 0x0f                   .....
    body (0)

#### RECORD 8 BolusWizard 2015-02-25T07:35:06 head[2], body[15] op[0x5b]
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
    datetime (2015-02-25T07:35:06)
    0000   0x06 0xa3 0x07 0x79 0x0f                   ...y.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    <P.d(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             60   80    0  100   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 336, 'amount': 2.0}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x50 0x14                   \.PP.
    decimal
             92    5   80   80   20
    datetime (unknown)

    body (0)

#### RECORD 10 SensorAlert 2015-02-25T07:36:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-25T07:36:07)
    0000   0x07 0xa4 0x27 0xb9 0x0f                   ..'..
    body (0)

#### RECORD 11 Bolus 2015-02-25T07:35:07 head[8], body[0] op[0x01]
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
    datetime (2015-02-25T07:35:07)
    0000   0x07 0xa3 0x47 0x79 0x0f                   ..Gy.
    body (0)

#### RECORD 12 Bolus 2015-02-25T07:52:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 5.9}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xec 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  236    0
    datetime (2015-02-25T07:52:38)
    0000   0x26 0xb4 0x47 0x79 0x0f                   &.Gy.
    body (0)

#### RECORD 13 SensorAlert 2015-02-25T09:59:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-25T09:59:33)
    0000   0x21 0xbb 0x29 0xb9 0x0f                   !.)..
    body (0)

#### RECORD 14 BasalProfileStart 2015-02-25T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-25T10:00:00)
    0000   0x00 0x80 0x0a 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 15 SensorAlert 2015-02-25T10:10:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-25T10:10:12)
    0000   0x0c 0x8a 0x2a 0xb9 0x0f                   ..*..
    body (0)

#### RECORD 16 SensorAlert 2015-02-25T10:31:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-25T10:31:00)
    0000   0x00 0x9f 0x2a 0xb9 0x0f                   ..*..
    body (0)

#### RECORD 17 SensorAlert 2015-02-25T11:31:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-25T11:31:00)
    0000   0x00 0x9f 0x2b 0xb9 0x0f                   ..+..
    body (0)

#### RECORD 18 CalBGForPH 2015-02-25T11:32:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 207}
```
    op hex (2)
    0000   0x0a 0xcf                                  ..
    decimal
             10  207
    datetime (2015-02-25T11:32:05)
    0000   0x05 0xa0 0x2b 0x79 0x0f                   ..+y.
    body (0)

#### RECORD 19 BGReceived 2015-02-25T11:32:05 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 207, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2015-02-25T11:32:05)
    0000   0x05 0xa0 0xeb 0x79 0x0f                   ...y.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 20 BolusWizard 2015-02-25T11:32:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 207,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 2.1,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0xcf                                  [.
    decimal
             91  207
    datetime (2015-02-25T11:32:25)
    0000   0x19 0xa0 0x0b 0x19 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x54 0x00    .P.P(ZT.
    0008   0x00 0x00 0x00 0x0c 0x00 0x48 0x78         .....Hx
    decimal
              0   80    0   80   40   90   84    0
              0    0    0   12    0   72  120

#### RECORD 21 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 223, 'amount': 3.0},
 {'age': 233, 'amount': 0.3},
 {'age': 243, 'amount': 5.7}]
```
    op hex (11)
    0000   0x5c 0x0b 0x78 0xdf 0x04 0x0c 0xe9 0x04    \.x.....
    0008   0xe4 0xf3 0x04                             ...
    decimal
             92   11  120  223    4   12  233    4
            228  243    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2015-02-25T11:32:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 0,
 'programmed': 1.8,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x0c 0x00    ..H.H...
    decimal
              1    0   72    0   72    0   12    0
    datetime (2015-02-25T11:32:25)
    0000   0x19 0xa0 0x4b 0x19 0x0f                   ..K..
    body (0)

#### RECORD 23 SensorAlert 2015-02-25T11:45:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 206}
```
    op hex (3)
    0000   0x0b 0x65 0xce                             .e.
    decimal
             11  101  206
    datetime (2015-02-25T11:45:48)
    0000   0x30 0xad 0x2b 0xb9 0x0f                   0.+..
    body (0)

#### RECORD 24 BasalProfileStart 2015-02-25T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-25T12:00:00)
    0000   0x00 0x80 0x0c 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 25 BolusWizard 2015-02-25T12:13:13 head[2], body[15] op[0x5b]
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
    datetime (2015-02-25T12:13:13)
    0000   0x0d 0x8d 0x0c 0x79 0x0f                   ...y.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    (P.P(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             40   80    0   80   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 26 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 1.8},
 {'age': 264, 'amount': 3.0},
 {'age': 274, 'amount': 0.3},
 {'age': 284, 'amount': 5.7}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x2c 0x04 0x78 0x08 0x14    \.H,.x..
    0008   0x0c 0x12 0x14 0xe4 0x1c 0x14              ......
    decimal
             92   14   72   44    4  120    8   20
             12   18   20  228   28   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2015-02-25T12:13:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x44 0x00    ......D.
    decimal
              1    0  200    0  200    0   68    0
    datetime (2015-02-25T12:13:13)
    0000   0x0d 0x8d 0x4c 0x79 0x0f                   ..Ly.
    body (0)

#### RECORD 28 SensorAlert 2015-02-25T14:10:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-25T14:10:12)
    0000   0x0c 0x8a 0x2e 0xb9 0x0f                   .....
    body (0)

#### RECORD 29 Bolus 2015-02-25T14:11:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 2.7}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x6c 0x00    ..P.P.l.
    decimal
              1    0   80    0   80    0  108    0
    datetime (2015-02-25T14:11:18)
    0000   0x12 0x8b 0x4e 0x79 0x0f                   ..Ny.
    body (0)

#### RECORD 30 SensorAlert 2015-02-25T14:21:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-25T14:21:00)
    0000   0x00 0x95 0x2e 0xb9 0x0f                   .....
    body (0)

#### RECORD 31 BasalProfileStart 2015-02-25T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-25T15:00:00)
    0000   0x00 0x80 0x0f 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 32 CalBGForPH 2015-02-25T16:54:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2015-02-25T16:54:55)
    0000   0x37 0xb6 0x30 0x79 0x0f                   7.0y.
    body (0)

#### RECORD 33 BGReceived 2015-02-25T16:54:55 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 182, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-02-25T16:54:55)
    0000   0x37 0xb6 0xd0 0x79 0x0f                   7..y.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 34 BolusWizard 2015-02-25T16:55:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 182,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0xb6                                  [.
    decimal
             91  182
    datetime (2015-02-25T16:55:19)
    0000   0x13 0xb7 0x10 0x19 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x3c 0x00    .P.P(Z<.
    0008   0x00 0x00 0x00 0x14 0x00 0x28 0x78         .....(x
    decimal
              0   80    0   80   40   90   60    0
              0    0    0   20    0   40  120

#### RECORD 35 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 166, 'amount': 2.0},
 {'age': 286, 'amount': 5.0},
 {'age': 326, 'amount': 1.8}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0xa6 0x04 0xc8 0x1e 0x14    \.P.....
    0008   0x48 0x46 0x14                             HF.
    decimal
             92   11   80  166    4  200   30   20
             72   70   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2015-02-25T16:55:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x14 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   20    0
    datetime (2015-02-25T16:55:19)
    0000   0x13 0xb7 0x50 0x19 0x0f                   ..P..
    body (0)

#### RECORD 37 SensorAlert 2015-02-25T16:56:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-25T16:56:07)
    0000   0x07 0xb8 0x30 0xb9 0x0f                   ..0..
    body (0)

#### RECORD 38 BolusWizard 2015-02-25T17:06:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 182,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.1,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_estimate': 1.5,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.4}
```
    op hex (2)
    0000   0x5b 0xb6                                  [.
    decimal
             91  182
    datetime (2015-02-25T17:06:11)
    0000   0x0b 0x86 0x11 0x79 0x0f                   ...y.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x50 0x28 0x5a 0x3c 0x00    (P.P(Z<.
    0008   0xc8 0x00 0x00 0x38 0x00 0xcc 0x78         ...8..x
    decimal
             40   80    0   80   40   90   60    0
            200    0    0   56    0  204  120

#### RECORD 39 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 1.0},
 {'age': 177, 'amount': 2.0},
 {'age': 297, 'amount': 5.0},
 {'age': 337, 'amount': 1.8}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x11 0x04 0x50 0xb1 0x04    \.(..P..
    0008   0xc8 0x29 0x14 0x48 0x51 0x14              .).HQ.
    decimal
             92   14   40   17    4   80  177    4
            200   41   20   72   81   20
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2015-02-25T17:08:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2,
 'duration': 60,
 'programmed': 1.2,
 'type': 'square',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x38 0x02    ..0.0.8.
    decimal
              1    0   48    0   48    0   56    2
    datetime (2015-02-25T17:08:11)
    0000   0x0b 0x88 0xb1 0x79 0x0f                   ...y.
    body (0)

#### RECORD 41 Bolus 2015-02-25T17:06:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x38 0x00    ..x.x.8.
    decimal
              1    0  120    0  120    0   56    0
    datetime (2015-02-25T17:06:11)
    0000   0x0b 0x86 0x91 0x79 0x0f                   ...y.
    body (0)

#### RECORD 42 SensorAlert 2015-02-25T17:09:31 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-25T17:09:31)
    0000   0x1f 0x89 0x31 0xb9 0x0f                   ..1..
    body (0)

#### RECORD 43 SensorAlert 2015-02-25T19:36:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-25T19:36:07)
    0000   0x07 0xa4 0x33 0xb9 0x0f                   ..3..
    body (0)

#### RECORD 44 CalBGForPH 2015-02-25T19:37:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2015-02-25T19:37:21)
    0000   0x15 0xa5 0x33 0x79 0x0f                   ..3y.
    body (0)

#### RECORD 45 BGReceived 2015-02-25T19:37:21 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 184, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-02-25T19:37:21)
    0000   0x15 0xa5 0x13 0x79 0x0f                   ...y.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 46 Bolus 2015-02-25T19:37:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x40 0x00    ......@.
    decimal
              1    0   20    0   20    0   64    0
    datetime (2015-02-25T19:37:49)
    0000   0x31 0xa5 0x53 0x79 0x0f                   1.Sy.
    body (0)

#### RECORD 47 SensorAlert 2015-02-25T19:55:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-25T19:55:39)
    0000   0x27 0xb7 0x33 0xb9 0x0f                   '.3..
    body (0)

#### RECORD 48 SensorAlert 2015-02-25T21:24:50 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 207}
```
    op hex (3)
    0000   0x0b 0x65 0xcf                             .e.
    decimal
             11  101  207
    datetime (2015-02-25T21:24:50)
    0000   0x32 0x98 0x35 0xb9 0x0f                   2.5..
    body (0)

#### RECORD 49 CalBGForPH 2015-02-25T21:56:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 220}
```
    op hex (2)
    0000   0x0a 0xdc                                  ..
    decimal
             10  220
    datetime (2015-02-25T21:56:41)
    0000   0x29 0xb8 0x35 0x79 0x0f                   ).5y.
    body (0)

#### RECORD 50 BGReceived 2015-02-25T21:56:41 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 220, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2015-02-25T21:56:41)
    0000   0x29 0xb8 0x95 0x79 0x0f                   )..y.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 51 BolusWizard 2015-02-25T21:57:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 220,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.3,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 2.5,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0xdc                                  [.
    decimal
             91  220
    datetime (2015-02-25T21:57:07)
    0000   0x07 0xb9 0x15 0x19 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x3c 0x28 0x5a 0x64 0x00    .P.<(Zd.
    0008   0x00 0x00 0x00 0x08 0x00 0x5c 0x78         .....\x
    decimal
              0   80    0   60   40   90  100    0
              0    0    0    8    0   92  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 148, 'amount': 0.5},
 {'age': 238, 'amount': 0.2},
 {'age': 248, 'amount': 0.2},
 {'age': 258, 'amount': 0.2},
 {'age': 268, 'amount': 0.2},
 {'age': 278, 'amount': 0.2},
 {'age': 288, 'amount': 0.2},
 {'age': 298, 'amount': 3.0},
 {'age': 308, 'amount': 1.0},
 {'age': 468, 'amount': 2.0}]
```
    op hex (32)
    0000   0x5c 0x20 0x14 0x94 0x04 0x08 0xee 0x04    \ ......
    0008   0x08 0xf8 0x04 0x08 0x02 0x14 0x08 0x0c    ........
    0010   0x14 0x08 0x16 0x14 0x08 0x20 0x14 0x78    ..... .x
    0018   0x2a 0x14 0x28 0x34 0x14 0x50 0xd4 0x14    *.(4.P..
    decimal
             92   32   20  148    4    8  238    4
              8  248    4    8    2   20    8   12
             20    8   22   20    8   32   20  120
             42   20   40   52   20   80  212   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2015-02-25T21:57:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x08 0x00    ........
    decimal
              1    0    0    0    0    0    8    0
    datetime (2015-02-25T21:57:07)
    0000   0x07 0xb9 0xb5 0x19 0x0f                   .....
    body (0)

#### RECORD 54 Bolus 2015-02-25T21:57:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3,
 'duration': 0,
 'programmed': 2.3,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x08 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    8    0
    datetime (2015-02-25T21:57:07)
    0000   0x07 0xb9 0x95 0x19 0x0f                   .....
    body (0)

#### RECORD 55 BasalProfileStart 2015-02-25T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-25T22:00:00)
    0000   0x00 0x80 0x16 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 56 BolusWizard 2015-02-25T22:10:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.6,
 'carb_input': 46,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 7.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-25T22:10:23)
    0000   0x17 0x8a 0x16 0x79 0x0f                   ...y.
    body (15)
    hex
    0000   0x2e 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    .P.<(Z..
    0008   0x30 0x00 0x00 0x00 0x01 0x30 0x78         0....0x
    decimal
             46   80    0   60   40   90    0    1
             48    0    0    0    1   48  120

#### RECORD 57 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 2.3},
 {'age': 161, 'amount': 0.5},
 {'age': 251, 'amount': 0.2},
 {'age': 261, 'amount': 0.2},
 {'age': 271, 'amount': 0.2},
 {'age': 281, 'amount': 0.2},
 {'age': 291, 'amount': 0.2},
 {'age': 301, 'amount': 0.2},
 {'age': 311, 'amount': 3.0},
 {'age': 321, 'amount': 1.0}]
```
    op hex (32)
    0000   0x5c 0x20 0x5c 0x15 0x04 0x14 0xa1 0x04    \ \.....
    0008   0x08 0xfb 0x04 0x08 0x05 0x14 0x08 0x0f    ........
    0010   0x14 0x08 0x19 0x14 0x08 0x23 0x14 0x08    .....#..
    0018   0x2d 0x14 0x78 0x37 0x14 0x28 0x41 0x14    -.x7.(A.
    decimal
             92   32   92   21    4   20  161    4
              8  251    4    8    5   20    8   15
             20    8   25   20    8   35   20    8
             45   20  120   55   20   40   65   20
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2015-02-25T22:10:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2,
 'duration': 0,
 'programmed': 1.2,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x01 0x30 0x01 0x30 0x00 0x60 0x00    ..0.0.`.
    decimal
              1    1   48    1   48    0   96    0
    datetime (2015-02-25T22:10:24)
    0000   0x18 0x8a 0x56 0x79 0x0f                   ..Vy.
    body (0)

#### RECORD 59 BasalProfileStart 2015-02-26T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-26T00:00:00)
    0000   0x00 0x80 0x00 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 60 MResultTotals 2015-02-26T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0xa9                   .....
    decimal
              7    0    0    8  169
    datetime (2015-02-26T00:00:00)
    0000   0x39 0x0f                                  9.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 61 Sara6E 2015-02-26T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-26T00:00:00)
    0000   0x39 0x0f                                  9.
    body (49)
    hex
    0000   0x05 0x00 0xc6 0xb6 0xdc 0x04 0x00 0x00    ........
    0008   0x08 0xa9 0x03 0x21 0x24 0x05 0x88 0x40    ...!$..@
    0010   0x00 0xba 0x03 0x90 0x00 0xcc 0x00 0x00    ........
    0018   0x01 0x2c 0x04 0x03 0x00 0x04 0x00 0x96    .,......
    0020   0x1d 0x45 0x02 0x1e 0x29 0x05 0x03 0x00    .E..)...
    0028   0x00 0x02 0x07 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  198  182  220    4    0    0
              8  169    3   33   36    5  136   64
              0  186    3  144    0  204    0    0
              1   44    4    3    0    4    0  150
             29   69    2   30   41    5    3    0
              0    2    7    1    0    0    0    0
              0

#### RECORD 62 SensorAlert 2015-02-26T00:56:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-26T00:56:06)
    0000   0x06 0xb8 0x20 0xba 0x0f                   .. ..
    body (0)

#### RECORD 63 SensorAlert 2015-02-26T01:09:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-26T01:09:30)
    0000   0x1e 0x89 0x21 0xba 0x0f                   ..!..
    body (0)

#### RECORD 64 SensorAlert 2015-02-26T02:39:32 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 302}
```
    op hex (3)
    0000   0x0b 0x65 0x2e                             .e.
    decimal
             11  101   46
    datetime (2015-02-26T02:39:32)
    0000   0x20 0xa7 0x22 0xba 0x8f                    ."..
    body (0)

#### RECORD 65 Bolus 2015-02-26T02:52:45 head[8], body[0] op[0x01]
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
    datetime (2015-02-26T02:52:45)
    0000   0x2d 0xb4 0x42 0x7a 0x0f                   -.Bz.
    body (0)

#### RECORD 66 BasalProfileStart 2015-02-26T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-26T04:00:00)
    0000   0x00 0x80 0x04 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 67 SensorAlert 2015-02-26T04:10:11 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 283}
```
    op hex (3)
    0000   0x0b 0x65 0x1b                             .e.
    decimal
             11  101   27
    datetime (2015-02-26T04:10:11)
    0000   0x0b 0x8a 0x24 0xba 0x8f                   ..$..
    body (0)

#### RECORD 68 Bolus 2015-02-26T05:41:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x20 0x00    ..d.d. .
    decimal
              1    0  100    0  100    0   32    0
    datetime (2015-02-26T05:41:40)
    0000   0x28 0xa9 0x45 0x7a 0x0f                   (.Ez.
    body (0)

#### RECORD 69 BasalProfileStart 2015-02-26T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-26T07:00:00)
    0000   0x00 0x80 0x07 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 70 PumpSuspend 2015-02-26T07:00:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-26T07:00:39)
    0000   0x27 0x80 0x07 0x1a 0x0f                   '....
    body (0)

#### RECORD 71 BasalProfileStart 2015-02-26T07:19:58 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-26T07:19:58)
    0000   0x3a 0x93 0x07 0x1a 0x0f                   :....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 72 PumpResume 2015-02-26T07:19:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-26T07:19:58)
    0000   0x3a 0x93 0x07 0x1a 0x0f                   :....
    body (0)

#### RECORD 73 BolusWizard 2015-02-26T07:36:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 50,
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
    datetime (2015-02-26T07:36:08)
    0000   0x08 0xa4 0x07 0x7a 0x0f                   ...z.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 74 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 117, 'amount': 2.5}, {'age': 287, 'amount': 4.0}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0x75 0x04 0xa0 0x1f 0x14    \.du....
    decimal
             92    8  100  117    4  160   31   20
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2015-02-26T07:36:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.2}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x30 0x00    ......0.
    decimal
              1    0  160    0  160    0   48    0
    datetime (2015-02-26T07:36:08)
    0000   0x08 0xa4 0x47 0x7a 0x0f                   ..Gz.
    body (0)

#### RECORD 76 SensorAlert 2015-02-26T08:04:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-26T08:04:49)
    0000   0x31 0x84 0x28 0xba 0x0f                   1.(..
    body (0)

#### RECORD 77 Bolus 2015-02-26T08:05:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 4.5}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xb4 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  180    0
    datetime (2015-02-26T08:05:27)
    0000   0x1b 0x85 0x48 0x7a 0x0f                   ..Hz.
    body (0)

#### RECORD 78 BolusWizard 2015-02-26T08:46:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.0,
 'carb_input': 30,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-26T08:46:51)
    0000   0x33 0xae 0x08 0x7a 0x0f                   3..z.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    .P.d(Z..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x78         x....xx
    decimal
             30   80    0  100   40   90    0    0
            120    0    0    0    0  120  120

#### RECORD 79 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 1.5},
 {'age': 77, 'amount': 4.0},
 {'age': 187, 'amount': 2.5},
 {'age': 357, 'amount': 4.0}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0x2f 0x04 0xa0 0x4d 0x04    \.</..M.
    0008   0x64 0xbb 0x04 0xa0 0x65 0x14              d...e.
    decimal
             92   14   60   47    4  160   77    4
            100  187    4  160  101   20
    datetime (unknown)

    body (0)

#### RECORD 80 Bolus 2015-02-26T08:46:51 head[8], body[0] op[0x01]
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
    datetime (2015-02-26T08:46:51)
    0000   0x33 0xae 0x48 0x7a 0x0f                   3.Hz.
    body (0)

#### RECORD 81 SensorAlert 2015-02-26T08:57:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-26T08:57:00)
    0000   0x00 0xb9 0x28 0xba 0x0f                   ..(..
    body (0)

#### RECORD 82 SensorAlert 2015-02-26T09:57:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-26T09:57:00)
    0000   0x00 0xb9 0x29 0xba 0x0f                   ..)..
    body (0)

#### RECORD 83 BasalProfileStart 2015-02-26T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-26T10:00:00)
    0000   0x00 0x80 0x0a 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

`end ReadHistoryData-page-20.data: 84 records`
