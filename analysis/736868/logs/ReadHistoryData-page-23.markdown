## START ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 1012, found 10 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb7 0xd5                                  ..
##### DEBUG DECIMAL
            183  213
#### RECORD 0 BolusWizard 2015-02-21T06:38:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 235,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 2.8,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.9}
```
    op hex (2)
    0000   0x5b 0xeb                                  [.
    decimal
             91  235
    datetime (2015-02-21T06:38:29)
    0000   0x1d 0xa6 0x06 0x15 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x70 0x00    .P.d(Zp.
    0008   0x00 0x00 0x00 0x4c 0x00 0x24 0x78         ...L.$x
    decimal
              0   80    0  100   40   90  112    0
              0    0    0   76    0   36  120

#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 2.0},
 {'age': 202, 'amount': 3.0},
 {'age': 272, 'amount': 4.0}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x48 0x04 0x78 0xca 0x04    \.PH.x..
    0008   0xa0 0x10 0x14                             ...
    decimal
             92   11   80   72    4  120  202    4
            160   16   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2015-02-21T06:38:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x4c 0x00    ......L.
    decimal
              1    0    0    0    0    0   76    0
    datetime (2015-02-21T06:38:29)
    0000   0x1d 0xa6 0xa6 0x15 0x0f                   .....
    body (0)

#### RECORD 3 Bolus 2015-02-21T06:38:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9,
 'duration': 0,
 'programmed': 0.9,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x4c 0x00    ..$.$.L.
    decimal
              1    0   36    0   36    0   76    0
    datetime (2015-02-21T06:38:29)
    0000   0x1d 0xa6 0x86 0x15 0x0f                   .....
    body (0)

#### RECORD 4 BasalProfileStart 2015-02-21T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-21T07:00:00)
    0000   0x00 0x80 0x07 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 5 SensorAlert 2015-02-21T07:45:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 205}
```
    op hex (3)
    0000   0x0b 0x65 0xcd                             .e.
    decimal
             11  101  205
    datetime (2015-02-21T07:45:21)
    0000   0x15 0xad 0x27 0xb5 0x0f                   ..'..
    body (0)

#### RECORD 6 BolusWizard 2015-02-21T08:17:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-21T08:17:56)
    0000   0x38 0x91 0x08 0x75 0x0f                   8..u.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    (P.d(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             40   80    0  100   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 0.9},
 {'age': 171, 'amount': 2.0},
 {'age': 301, 'amount': 3.0},
 {'age': 371, 'amount': 4.0}]
```
    op hex (14)
    0000   0x5c 0x0e 0x24 0x65 0x04 0x50 0xab 0x04    \.$e.P..
    0008   0x78 0x2d 0x14 0xa0 0x73 0x14              x-..s.
    decimal
             92   14   36  101    4   80  171    4
            120   45   20  160  115   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2015-02-21T08:17:56 head[8], body[0] op[0x01]
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
    datetime (2015-02-21T08:17:56)
    0000   0x38 0x91 0x48 0x75 0x0f                   8.Hu.
    body (0)

#### RECORD 9 BolusWizard 2015-02-21T08:59:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.5,
 'carb_input': 35,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-21T08:59:36)
    0000   0x24 0xbb 0x08 0x75 0x0f                   $..u.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    #P.d(Z..
    0008   0x8c 0x00 0x00 0x00 0x00 0x8c 0x78         ......x
    decimal
             35   80    0  100   40   90    0    0
            140    0    0    0    0  140  120

#### RECORD 10 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 4.0},
 {'age': 143, 'amount': 0.9},
 {'age': 213, 'amount': 2.0},
 {'age': 343, 'amount': 3.0},
 {'age': 413, 'amount': 4.0}]
```
    op hex (17)
    0000   0x5c 0x11 0xa0 0x2b 0x04 0x24 0x8f 0x04    \..+.$..
    0008   0x50 0xd5 0x04 0x78 0x57 0x14 0xa0 0x9d    P..xW...
    0010   0x14                                       .
    decimal
             92   17  160   43    4   36  143    4
             80  213    4  120   87   20  160  157
             20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2015-02-21T08:59:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 4.1}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0xa4 0x00    ........
    decimal
              1    0  140    0  140    0  164    0
    datetime (2015-02-21T08:59:36)
    0000   0x24 0xbb 0x48 0x75 0x0f                   $.Hu.
    body (0)

#### RECORD 12 PumpSuspend 2015-02-21T09:07:32 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-21T09:07:32)
    0000   0x20 0x87 0x09 0x15 0x0f                    ....
    body (0)

#### RECORD 13 SensorAlert 2015-02-21T09:18:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 254}
```
    op hex (3)
    0000   0x0b 0x65 0xfe                             .e.
    decimal
             11  101  254
    datetime (2015-02-21T09:18:45)
    0000   0x2d 0x92 0x29 0xb5 0x0f                   -.)..
    body (0)

#### RECORD 14 BasalProfileStart 2015-02-21T09:30:06 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-21T09:30:06)
    0000   0x06 0x9e 0x09 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 15 PumpResume 2015-02-21T09:30:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-21T09:30:06)
    0000   0x06 0x9e 0x09 0x15 0x0f                   .....
    body (0)

#### RECORD 16 Bolus 2015-02-21T09:30:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x01 0x04 0x00    ........
    decimal
              1    0  140    0  140    1    4    0
    datetime (2015-02-21T09:30:23)
    0000   0x17 0x9e 0x49 0x75 0x0f                   ..Iu.
    body (0)

#### RECORD 17 Bolus 2015-02-21T09:45:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 2.9}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x01 0x74 0x00    ..x.x.t.
    decimal
              1    0  120    0  120    1  116    0
    datetime (2015-02-21T09:45:08)
    0000   0x08 0xad 0x49 0x75 0x0f                   ..Iu.
    body (0)

#### RECORD 18 BasalProfileStart 2015-02-21T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-21T10:00:00)
    0000   0x00 0x80 0x0a 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 19 LowReservoir 2015-02-21T10:21:19 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-02-21T10:21:19)
    0000   0x13 0x95 0x0a 0x15 0x0f                   .....
    body (0)

#### RECORD 20 Bolus 2015-02-21T10:20:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 3.6}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x01 0x90 0x00    ..d.d...
    decimal
              1    0  100    0  100    1  144    0
    datetime (2015-02-21T10:20:43)
    0000   0x2b 0x94 0x4a 0x75 0x0f                   +.Ju.
    body (0)

#### RECORD 21 BasalProfileStart 2015-02-21T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-21T12:00:00)
    0000   0x00 0x80 0x0c 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 22 SensorAlert 2015-02-21T12:04:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-21T12:04:53)
    0000   0x35 0x84 0x2c 0xb5 0x0f                   5.,..
    body (0)

#### RECORD 23 SensorAlert 2015-02-21T12:14:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-21T12:14:04)
    0000   0x04 0x8e 0x2c 0xb5 0x0f                   ..,..
    body (0)

#### RECORD 24 SensorAlert 2015-02-21T13:45:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 266}
```
    op hex (3)
    0000   0x0b 0x65 0x0a                             .e.
    decimal
             11  101   10
    datetime (2015-02-21T13:45:21)
    0000   0x15 0xad 0x2d 0xb5 0x8f                   ..-..
    body (0)

#### RECORD 25 Bolus 2015-02-21T13:45:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x10 0x00    ........
    decimal
              1    0  180    0  180    0   16    0
    datetime (2015-02-21T13:45:43)
    0000   0x2b 0xad 0x4d 0x75 0x0f                   +.Mu.
    body (0)

#### RECORD 26 BasalProfileStart 2015-02-21T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-21T15:00:00)
    0000   0x00 0x80 0x0f 0x15 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 27 LowReservoir 2015-02-21T15:16:52 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-02-21T15:16:52)
    0000   0x34 0x90 0x0f 0x15 0x0f                   4....
    body (0)

#### RECORD 28 BolusWizard 2015-02-21T16:29:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.2,
 'carb_input': 42,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-21T16:29:33)
    0000   0x21 0x9d 0x10 0x75 0x0f                   !..u.
    body (15)
    hex
    0000   0x2a 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    *P.P(Z..
    0008   0xd0 0x00 0x00 0x00 0x00 0xd0 0x78         ......x
    decimal
             42   80    0   80   40   90    0    0
            208    0    0    0    0  208  120

#### RECORD 29 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 163, 'amount': 4.05},
 {'age': 173, 'amount': 0.45},
 {'age': 373, 'amount': 2.5},
 {'age': 403, 'amount': 1.75},
 {'age': 413, 'amount': 1.25},
 {'age': 423, 'amount': 3.5},
 {'age': 453, 'amount': 3.5}]
```
    op hex (23)
    0000   0x5c 0x17 0xa2 0xa3 0x04 0x12 0xad 0x04    \.......
    0008   0x64 0x75 0x14 0x46 0x93 0x14 0x32 0x9d    du.F..2.
    0010   0x14 0x8c 0xa7 0x14 0x8c 0xc5 0x14         .......
    decimal
             92   23  162  163    4   18  173    4
            100  117   20   70  147   20   50  157
             20  140  167   20  140  197   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2015-02-21T16:29:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x2c 0x00    ......,.
    decimal
              1    0    0    0    0    0   44    0
    datetime (2015-02-21T16:29:33)
    0000   0x21 0x9d 0xb0 0x75 0x0f                   !..u.
    body (0)

#### RECORD 31 Bolus 2015-02-21T16:29:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2,
 'duration': 0,
 'programmed': 5.2,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0xd0 0x00 0xd0 0x00 0x2c 0x00    ......,.
    decimal
              1    0  208    0  208    0   44    0
    datetime (2015-02-21T16:29:33)
    0000   0x21 0x9d 0x90 0x75 0x0f                   !..u.
    body (0)

#### RECORD 32 SensorAlert 2015-02-21T16:44:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-21T16:44:53)
    0000   0x35 0xac 0x30 0xb5 0x0f                   5.0..
    body (0)

#### RECORD 33 SensorAlert 2015-02-21T17:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-21T17:38:00)
    0000   0x00 0xa6 0x31 0xb5 0x0f                   ..1..
    body (0)

#### RECORD 34 SensorAlert 2015-02-21T18:14:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-21T18:14:04)
    0000   0x04 0x8e 0x32 0xb5 0x0f                   ..2..
    body (0)

#### RECORD 35 Bolus 2015-02-21T18:20:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 2.7}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x6c 0x00    ..d.d.l.
    decimal
              1    0  100    0  100    0  108    0
    datetime (2015-02-21T18:20:06)
    0000   0x06 0x94 0x52 0x75 0x0f                   ..Ru.
    body (0)

#### RECORD 36 SensorAlert 2015-02-21T18:25:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-21T18:25:21)
    0000   0x15 0x99 0x32 0xb5 0x0f                   ..2..
    body (0)

#### RECORD 37 SensorAlert 2015-02-21T18:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-21T18:38:00)
    0000   0x00 0xa6 0x32 0xb5 0x0f                   ..2..
    body (0)

#### RECORD 38 hack53 2015-02-21T18:38:48 head[2], body[1] op[0x53]

    op hex (2)
    0000   0x53 0x08                                  S.
    decimal
             83    8
    datetime (2015-02-21T18:38:48)
    0000   0x30 0xa6 0x12 0x15 0x0f                   0....
    body (1)
    hex
    0000   0xb4                                       .
    decimal
            180

#### RECORD 39 SensorAlert 2015-02-21T19:08:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-21T19:08:00)
    0000   0x00 0x88 0x33 0xb5 0x0f                   ..3..
    body (0)

#### RECORD 40 SensorAlert 2015-02-21T19:08:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (88)', 'alarm_type': 88}
```
    op hex (3)
    0000   0x0b 0x58 0x00                             .X.
    decimal
             11   88    0
    datetime (2015-02-21T19:08:00)
    0000   0x00 0x88 0x33 0xb5 0x0f                   ..3..
    body (0)

#### RECORD 41 SensorAlert 2015-02-21T19:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-21T19:38:00)
    0000   0x00 0xa6 0x33 0xb5 0x0f                   ..3..
    body (0)

#### RECORD 42 SensorAlert 2015-02-21T20:08:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-21T20:08:00)
    0000   0x00 0x88 0x34 0xb5 0x0f                   ..4..
    body (0)

#### RECORD 43 Bolus 2015-02-21T20:14:00 head[8], body[0] op[0x01]
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
    datetime (2015-02-21T20:14:00)
    0000   0x00 0x8e 0x54 0x75 0x0f                   ..Tu.
    body (0)

#### RECORD 44 SensorAlert 2015-02-21T20:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-21T20:38:00)
    0000   0x00 0xa6 0x34 0xb5 0x0f                   ..4..
    body (0)

#### RECORD 45 SensorAlert 2015-02-21T20:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (88)', 'alarm_type': 88}
```
    op hex (3)
    0000   0x0b 0x58 0x00                             .X.
    decimal
             11   88    0
    datetime (2015-02-21T20:38:00)
    0000   0x00 0xa6 0x34 0xb5 0x0f                   ..4..
    body (0)

#### RECORD 46 SensorAlert 2015-02-21T21:08:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-21T21:08:00)
    0000   0x00 0x88 0x35 0xb5 0x0f                   ..5..
    body (0)

#### RECORD 47 CalBGForPH 2015-02-21T21:34:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 337}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2015-02-21T21:34:36)
    0000   0x24 0xa2 0x35 0x75 0x8f                   $.5u.
    body (0)

#### RECORD 48 BGReceived 2015-02-21T21:34:36 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 337, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2a                                  ?*
    decimal
             63   42
    datetime (2015-02-21T21:34:36)
    0000   0x24 0xa2 0x35 0x75 0x0f                   $.5u.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 49 BolusWizard 2015-02-21T21:35:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 337,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.1,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 5.4,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 2.3}
```
    op hex (2)
    0000   0x5b 0x51                                  [Q
    decimal
             91   81
    datetime (2015-02-21T21:35:02)
    0000   0x02 0xa3 0x15 0x75 0x0f                   ...u.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x3c 0x28 0x5a 0xd8 0x00    .Q.<(Z..
    0008   0x00 0x00 0x00 0x5c 0x00 0x7c 0x78         ...\.|x
    decimal
              0   81    0   60   40   90  216    0
              0    0    0   92    0  124  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 0.05},
 {'age': 89, 'amount': 2.95},
 {'age': 199, 'amount': 2.5},
 {'age': 309, 'amount': 5.2},
 {'age': 469, 'amount': 4.05},
 {'age': 479, 'amount': 0.45}]
```
    op hex (20)
    0000   0x5c 0x14 0x02 0x4f 0x04 0x76 0x59 0x04    \..O.vY.
    0008   0x64 0xc7 0x04 0xd0 0x35 0x14 0xa2 0xd5    d...5...
    0010   0x14 0x12 0xdf 0x14                        ....
    decimal
             92   20    2   79    4  118   89    4
            100  199    4  208   53   20  162  213
             20   18  223   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2015-02-21T21:35:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x5c 0x00    ......\.
    decimal
              1    0    0    0    0    0   92    0
    datetime (2015-02-21T21:35:02)
    0000   0x02 0xa3 0xb5 0x75 0x0f                   ...u.
    body (0)

#### RECORD 52 Bolus 2015-02-21T21:35:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1,
 'duration': 0,
 'programmed': 3.1,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x5c 0x00    ..|.|.\.
    decimal
              1    0  124    0  124    0   92    0
    datetime (2015-02-21T21:35:02)
    0000   0x02 0xa3 0x95 0x75 0x0f                   ...u.
    body (0)

#### RECORD 53 SensorAlert 2015-02-21T21:50:14 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 335}
```
    op hex (3)
    0000   0x0b 0x65 0x4f                             .eO
    decimal
             11  101   79
    datetime (2015-02-21T21:50:14)
    0000   0x0e 0xb2 0x35 0xb5 0x8f                   ..5..
    body (0)

#### RECORD 54 Bolus 2015-02-21T21:52:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0x70 0x00 0xc8 0x00    ....p...
    decimal
              1    0  160    0  112    0  200    0
    datetime (2015-02-21T21:52:15)
    0000   0x0f 0xb4 0x55 0x75 0x0f                   ..Uu.
    body (0)

#### RECORD 55 NoDelivery 2015-02-21T21:54:09 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-02-21T21:54:09)
    0000   0x09 0xb6 0x55 0x55 0x0f                   ..UU.
    body (0)

#### RECORD 56 ClearAlarm 2015-02-21T21:54:32 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-02-21T21:54:32)
    0000   0x20 0xb6 0x15 0x15 0x0f                    ....
    body (0)

#### RECORD 57 Rewind 2015-02-21T21:54:41 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-02-21T21:54:41)
    0000   0x29 0xb6 0x15 0x15 0x0f                   )....
    body (0)

#### RECORD 58 Prime 2015-02-21T22:08:09 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 8.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x55                   ....U
    decimal
              3    0    0    0   85
    datetime (2015-02-21T22:08:09)
    0000   0x09 0x88 0x36 0x15 0x0f                   ..6..
    body (0)

#### RECORD 59 BasalProfileStart 2015-02-21T22:09:45 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-21T22:09:45)
    0000   0x2d 0x89 0x16 0x15 0x0f                   -....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 60 Prime 2015-02-21T22:09:31 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-02-21T22:09:31)
    0000   0x1f 0x89 0x16 0x15 0x0f                   .....
    body (0)

#### RECORD 61 Bolus 2015-02-21T22:10:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x01 0x1c 0x00    ..x.x...
    decimal
              1    0  120    0  120    1   28    0
    datetime (2015-02-21T22:10:18)
    0000   0x12 0x8a 0x56 0x75 0x0f                   ..Vu.
    body (0)

#### RECORD 62 Bolus 2015-02-21T23:00:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5,
 'duration': 0,
 'programmed': 5.5,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0xdc 0x00 0xdc 0x01 0x24 0x00    ......$.
    decimal
              1    0  220    0  220    1   36    0
    datetime (2015-02-21T23:00:26)
    0000   0x1a 0x80 0x57 0x75 0x0f                   ..Wu.
    body (0)

#### RECORD 63 SensorAlert 2015-02-21T23:18:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 347}
```
    op hex (3)
    0000   0x0b 0x65 0x5b                             .e[
    decimal
             11  101   91
    datetime (2015-02-21T23:18:45)
    0000   0x2d 0x92 0x37 0xb5 0x8f                   -.7..
    body (0)

#### RECORD 64 BasalProfileStart 2015-02-22T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-22T00:00:00)
    0000   0x00 0x80 0x00 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 65 MResultTotals 2015-02-22T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0b 0xda                   .....
    decimal
              7    0    0   11  218
    datetime (2015-02-22T00:00:00)
    0000   0x35 0x0f                                  5.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 66 Sara6E 2015-02-22T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-22T00:00:00)
    0000   0x35 0x0f                                  5.
    body (49)
    hex
    0000   0x05 0x11 0x1e 0xeb 0x51 0x02 0x00 0x00    ....Q...
    0008   0x0b 0xda 0x03 0x1a 0x1a 0x08 0xc0 0x4a    .......J
    0010   0x00 0x75 0x01 0xfc 0x00 0xa0 0x00 0x00    .u......
    0018   0x06 0x24 0x03 0x02 0x00 0x0c 0x00 0xea    .$......
    0020   0x4a 0x1a 0x00 0xfa 0x41 0x04 0x00 0x00    J...A...
    0028   0x00 0x00 0x0b 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   17   30  235   81    2    0    0
             11  218    3   26   26    8  192   74
              0  117    1  252    0  160    0    0
              6   36    3    2    0   12    0  234
             74   26    0  250   65    4    0    0
              0    0   11    0    0    0    0    0
              0

#### RECORD 67 SensorAlert 2015-02-22T00:48:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 229}
```
    op hex (3)
    0000   0x0b 0x65 0xe5                             .e.
    decimal
             11  101  229
    datetime (2015-02-22T00:48:47)
    0000   0x2f 0xb0 0x20 0xb6 0x0f                   /. ..
    body (0)

#### RECORD 68 SensorAlert 2015-02-22T02:19:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 239}
```
    op hex (3)
    0000   0x0b 0x65 0xef                             .e.
    decimal
             11  101  239
    datetime (2015-02-22T02:19:25)
    0000   0x19 0x93 0x22 0xb6 0x0f                   .."..
    body (0)

#### RECORD 69 Bolus 2015-02-22T03:07:57 head[8], body[0] op[0x01]
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
    datetime (2015-02-22T03:07:57)
    0000   0x39 0x87 0x43 0x76 0x0f                   9.Cv.
    body (0)

#### RECORD 70 Bolus 2015-02-22T03:12:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 3.0}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x78 0x00    ......x.
    decimal
              1    0  140    0  140    0  120    0
    datetime (2015-02-22T03:12:32)
    0000   0x20 0x8c 0x43 0x76 0x0f                    .Cv.
    body (0)

#### RECORD 71 SensorAlert 2015-02-22T03:50:13 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 270}
```
    op hex (3)
    0000   0x0b 0x65 0x0e                             .e.
    decimal
             11  101   14
    datetime (2015-02-22T03:50:13)
    0000   0x0d 0xb2 0x23 0xb6 0x8f                   ..#..
    body (0)

#### RECORD 72 BasalProfileStart 2015-02-22T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-22T04:00:00)
    0000   0x00 0x80 0x04 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 73 SensorAlert 2015-02-22T05:18:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 212}
```
    op hex (3)
    0000   0x0b 0x65 0xd4                             .e.
    decimal
             11  101  212
    datetime (2015-02-22T05:18:44)
    0000   0x2c 0x92 0x25 0xb6 0x0f                   ,.%..
    body (0)

#### RECORD 74 Bolus 2015-02-22T05:31:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 2.1}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x54 0x00    ..P.P.T.
    decimal
              1    0   80    0   80    0   84    0
    datetime (2015-02-22T05:31:25)
    0000   0x19 0x9f 0x45 0x76 0x0f                   ..Ev.
    body (0)

#### RECORD 75 BasalProfileStart 2015-02-22T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-22T07:00:00)
    0000   0x00 0x80 0x07 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 76 SensorAlert 2015-02-22T08:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-22T08:34:00)
    0000   0x00 0xa2 0x28 0xb6 0x0f                   ..(..
    body (0)

#### RECORD 77 Bolus 2015-02-22T09:19:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x08 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    8    0
    datetime (2015-02-22T09:19:31)
    0000   0x1f 0x93 0x49 0x76 0x0f                   ..Iv.
    body (0)

#### RECORD 78 SensorAlert 2015-02-22T09:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-22T09:34:00)
    0000   0x00 0xa2 0x29 0xb6 0x0f                   ..)..
    body (0)

#### RECORD 79 BasalProfileStart 2015-02-22T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-22T10:00:00)
    0000   0x00 0x80 0x0a 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 80 SensorAlert 2015-02-22T10:04:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-22T10:04:00)
    0000   0x00 0x84 0x2a 0xb6 0x0f                   ..*..
    body (0)

#### RECORD 81 CalBGForPH 2015-02-22T10:06:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 254}
```
    op hex (2)
    0000   0x0a 0xfe                                  ..
    decimal
             10  254
    datetime (2015-02-22T10:06:00)
    0000   0x00 0x86 0x2a 0x76 0x0f                   ..*v.
    body (0)

#### RECORD 82 BGReceived 2015-02-22T10:06:00 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 254, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1f                                  ?.
    decimal
             63   31
    datetime (2015-02-22T10:06:00)
    0000   0x00 0x86 0xca 0x76 0x0f                   ...v.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 83 BolusWizard 2015-02-22T10:06:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 254,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 3.3,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 2.2}
```
    op hex (2)
    0000   0x5b 0xfe                                  [.
    decimal
             91  254
    datetime (2015-02-22T10:06:20)
    0000   0x14 0x86 0x0a 0x16 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x84 0x00    .P.d(Z..
    0008   0x00 0x00 0x00 0x58 0x00 0x2c 0x78         ...X.,x
    decimal
              0   80    0  100   40   90  132    0
              0    0    0   88    0   44  120

#### RECORD 84 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 2.5},
 {'age': 280, 'amount': 2.0},
 {'age': 420, 'amount': 0.1}]
```
    op hex (11)
    0000   0x5c 0x0b 0x64 0x32 0x04 0x50 0x18 0x14    \.d2.P..
    0008   0x04 0xa4 0x15                             ...
    decimal
             92   11  100   50    4   80   24   20
              4  164   21
    datetime (unknown)

    body (0)

#### RECORD 85 Bolus 2015-02-22T10:06:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x58 0x00    ......X.
    decimal
              1    0    0    0    0    0   88    0
    datetime (2015-02-22T10:06:20)
    0000   0x14 0x86 0xaa 0x16 0x0f                   .....
    body (0)

#### RECORD 86 Bolus 2015-02-22T10:06:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8,
 'duration': 0,
 'programmed': 2.8,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x58 0x00    ..p.p.X.
    decimal
              1    0  112    0  112    0   88    0
    datetime (2015-02-22T10:06:20)
    0000   0x14 0x86 0x8a 0x16 0x0f                   .....
    body (0)

`end ReadHistoryData-page-23.data: 87 records`
