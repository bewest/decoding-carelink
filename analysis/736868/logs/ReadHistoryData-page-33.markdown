## START ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe9 0x87                                  ..
##### DEBUG DECIMAL
            233  135
#### RECORD 0 Bolus 2015-02-09T10:40:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 0,
 'programmed': 1.8,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x2c 0x00    ..H.H.,.
    decimal
              1    0   72    0   72    0   44    0
    datetime (2015-02-09T10:40:22)
    0000   0x16 0xa8 0x8a 0x09 0x0f                   .....
    body (0)

#### RECORD 1 SensorAlert 2015-02-09T10:53:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 239}
```
    op hex (3)
    0000   0x0b 0x65 0xef                             .e.
    decimal
             11  101  239
    datetime (2015-02-09T10:53:04)
    0000   0x04 0xb5 0x2a 0xa9 0x0f                   ..*..
    body (0)

#### RECORD 2 BolusWizard 2015-02-09T11:55:02 head[2], body[15] op[0x5b]
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
    datetime (2015-02-09T11:55:02)
    0000   0x02 0xb7 0x0b 0x69 0x0f                   ...i.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 3 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 1.8},
 {'age': 219, 'amount': 0.15},
 {'age': 229, 'amount': 0.65},
 {'age': 239, 'amount': 0.65},
 {'age': 249, 'amount': 3.55},
 {'age': 319, 'amount': 0.7}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x4f 0x04 0x06 0xdb 0x04    \.HO....
    0008   0x1a 0xe5 0x04 0x1a 0xef 0x04 0x8e 0xf9    ........
    0010   0x04 0x1c 0x3f 0x14                        ..?.
    decimal
             92   20   72   79    4    6  219    4
             26  229    4   26  239    4  142  249
              4   28   63   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2015-02-09T11:57:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 90,
 'programmed': 3.5,
 'type': 'square',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x38 0x03    ......8.
    decimal
              1    0  140    0  140    0   56    3
    datetime (2015-02-09T11:57:42)
    0000   0x2a 0xb9 0xab 0x69 0x0f                   *..i.
    body (0)

#### RECORD 5 Bolus 2015-02-09T11:55:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x38 0x00    ......8.
    decimal
              1    0  160    0  160    0   56    0
    datetime (2015-02-09T11:55:02)
    0000   0x02 0xb7 0x8b 0x69 0x0f                   ...i.
    body (0)

#### RECORD 6 BasalProfileStart 2015-02-09T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-09T12:00:00)
    0000   0x00 0x80 0x0c 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 7 SensorAlert 2015-02-09T12:23:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 217}
```
    op hex (3)
    0000   0x0b 0x65 0xd9                             .e.
    decimal
             11  101  217
    datetime (2015-02-09T12:23:43)
    0000   0x2b 0x97 0x2c 0xa9 0x0f                   +.,..
    body (0)

#### RECORD 8 SensorAlert 2015-02-09T13:49:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-09T13:49:38)
    0000   0x26 0xb1 0x2d 0xa9 0x0f                   &.-..
    body (0)

#### RECORD 9 SensorAlert 2015-02-09T14:39:19 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-09T14:39:19)
    0000   0x13 0xa7 0x2e 0xa9 0x0f                   .....
    body (0)

#### RECORD 10 BasalProfileStart 2015-02-09T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-09T15:00:00)
    0000   0x00 0x80 0x0f 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 11 Bolus 2015-02-09T15:01:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x48 0x00    ..x.x.H.
    decimal
              1    0  120    0  120    0   72    0
    datetime (2015-02-09T15:01:43)
    0000   0x2b 0x81 0x4f 0x69 0x0f                   +.Oi.
    body (0)

#### RECORD 12 SensorAlert 2015-02-09T15:40:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-09T15:40:00)
    0000   0x00 0xa8 0x2f 0xa9 0x0f                   ../..
    body (0)

#### RECORD 13 SensorAlert 2015-02-09T16:40:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-09T16:40:00)
    0000   0x00 0xa8 0x30 0xa9 0x0f                   ..0..
    body (0)

#### RECORD 14 CalBGForPH 2015-02-09T16:43:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2015-02-09T16:43:38)
    0000   0x26 0xab 0x30 0x69 0x0f                   &.0i.
    body (0)

#### RECORD 15 BGReceived 2015-02-09T16:43:38 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 86, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2015-02-09T16:43:38)
    0000   0x26 0xab 0xd0 0x69 0x0f                   &..i.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 16 SensorAlert 2015-02-09T18:03:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-09T18:03:02)
    0000   0x02 0x83 0x32 0xa9 0x0f                   ..2..
    body (0)

#### RECORD 17 SensorAlert 2015-02-09T20:29:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-09T20:29:38)
    0000   0x26 0x9d 0x34 0xa9 0x0f                   &.4..
    body (0)

#### RECORD 18 BolusWizard 2015-02-09T20:32:42 head[2], body[15] op[0x5b]
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
    datetime (2015-02-09T20:32:42)
    0000   0x2a 0xa0 0x14 0x69 0x0f                   *..i.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    FP.<(Z..
    0008   0xd0 0x00 0x00 0x00 0x01 0xd0 0x78         ......x
    decimal
             70   80    0   60   40   90    0    1
            208    0    0    0    1  208  120

#### RECORD 19 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 336, 'amount': 3.0},
 {'age': 426, 'amount': 0.05},
 {'age': 436, 'amount': 0.4},
 {'age': 446, 'amount': 0.4},
 {'age': 456, 'amount': 0.4},
 {'age': 466, 'amount': 0.35},
 {'age': 476, 'amount': 0.4}]
```
    op hex (23)
    0000   0x5c 0x17 0x78 0x50 0x14 0x02 0xaa 0x14    \.xP....
    0008   0x10 0xb4 0x14 0x10 0xbe 0x14 0x10 0xc8    ........
    0010   0x14 0x0e 0xd2 0x14 0x10 0xdc 0x14         .......
    decimal
             92   23  120   80   20    2  170   20
             16  180   20   16  190   20   16  200
             20   14  210   20   16  220   20
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2015-02-09T20:36:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6,
 'duration': 360,
 'programmed': 5.6,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xe0 0x00 0xe0 0x00 0x00 0x0c    ........
    decimal
              1    0  224    0  224    0    0   12
    datetime (2015-02-09T20:36:44)
    0000   0x2c 0xa4 0xb4 0x69 0x0f                   ,..i.
    body (0)

#### RECORD 21 Bolus 2015-02-09T20:32:42 head[8], body[0] op[0x01]
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
    datetime (2015-02-09T20:32:42)
    0000   0x2a 0xa0 0x94 0x69 0x0f                   *..i.
    body (0)

#### RECORD 22 SensorAlert 2015-02-09T21:03:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-09T21:03:43)
    0000   0x2b 0x83 0x35 0xa9 0x0f                   +.5..
    body (0)

#### RECORD 23 BasalProfileStart 2015-02-09T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-09T22:00:00)
    0000   0x00 0x80 0x16 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 24 SensorAlert 2015-02-09T22:29:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-09T22:29:38)
    0000   0x26 0x9d 0x36 0xa9 0x0f                   &.6..
    body (0)

#### RECORD 25 SensorAlert 2015-02-09T22:34:31 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-09T22:34:31)
    0000   0x1f 0xa2 0x36 0xa9 0x0f                   ..6..
    body (0)

#### RECORD 26 BolusWizard 2015-02-09T22:35:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 36,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-09T22:35:22)
    0000   0x16 0xa3 0x16 0x69 0x0f                   ...i.
    body (15)
    hex
    0000   0x24 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    $P.d(Z..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x78         ......x
    decimal
             36   80    0  100   40   90    0    0
            144    0    0    0    0  144  120

#### RECORD 27 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 0.15},
 {'age': 19, 'amount': 0.15},
 {'age': 29, 'amount': 0.15},
 {'age': 39, 'amount': 0.15},
 {'age': 49, 'amount': 0.15},
 {'age': 59, 'amount': 0.2},
 {'age': 69, 'amount': 0.15},
 {'age': 79, 'amount': 0.15},
 {'age': 89, 'amount': 0.15},
 {'age': 99, 'amount': 0.15},
 {'age': 109, 'amount': 0.15},
 {'age': 119, 'amount': 1.3},
 {'age': 129, 'amount': 4.85},
 {'age': 459, 'amount': 3.0}]
```
    op hex (44)
    0000   0x5c 0x2c 0x06 0x09 0x04 0x06 0x13 0x04    \,......
    0008   0x06 0x1d 0x04 0x06 0x27 0x04 0x06 0x31    ....'..1
    0010   0x04 0x08 0x3b 0x04 0x06 0x45 0x04 0x06    ..;..E..
    0018   0x4f 0x04 0x06 0x59 0x04 0x06 0x63 0x04    O..Y..c.
    0020   0x06 0x6d 0x04 0x34 0x77 0x04 0xc2 0x81    .m.4w...
    0028   0x04 0x78 0xcb 0x14                        .x..
    decimal
             92   44    6    9    4    6   19    4
              6   29    4    6   39    4    6   49
              4    8   59    4    6   69    4    6
             79    4    6   89    4    6   99    4
              6  109    4   52  119    4  194  129
              4  120  203   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2015-02-09T22:35:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6,
 'duration': 0,
 'programmed': 3.6,
 'type': 'normal',
 'unabsorbed': 4.0}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0xa0 0x00    ........
    decimal
              1    0  144    0  144    0  160    0
    datetime (2015-02-09T22:35:23)
    0000   0x17 0xa3 0x56 0x69 0x0f                   ..Vi.
    body (0)

#### RECORD 29 BolusWizard 2015-02-09T23:38:14 head[2], body[15] op[0x5b]
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
    datetime (2015-02-09T23:38:14)
    0000   0x0e 0xa6 0x17 0x69 0x0f                   ...i.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    -P.d(Z..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x78         ......x
    decimal
             45   80    0  100   40   90    0    0
            180    0    0    0    0  180  120

#### RECORD 30 UnabsorbedInsulinBolus unknown head[59], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 0.2},
 {'age': 22, 'amount': 0.15},
 {'age': 32, 'amount': 0.15},
 {'age': 42, 'amount': 0.15},
 {'age': 52, 'amount': 0.15},
 {'age': 62, 'amount': 2.8},
 {'age': 72, 'amount': 1.1},
 {'age': 82, 'amount': 0.15},
 {'age': 92, 'amount': 0.15},
 {'age': 102, 'amount': 0.15},
 {'age': 112, 'amount': 0.15},
 {'age': 122, 'amount': 0.2},
 {'age': 132, 'amount': 0.15},
 {'age': 142, 'amount': 0.15},
 {'age': 152, 'amount': 0.15},
 {'age': 162, 'amount': 0.15},
 {'age': 172, 'amount': 0.15},
 {'age': 182, 'amount': 1.3},
 {'age': 192, 'amount': 4.85}]
```
    op hex (59)
    0000   0x5c 0x3b 0x08 0x0c 0x04 0x06 0x16 0x04    \;......
    0008   0x06 0x20 0x04 0x06 0x2a 0x04 0x06 0x34    . ..*..4
    0010   0x04 0x70 0x3e 0x04 0x2c 0x48 0x04 0x06    .p>.,H..
    0018   0x52 0x04 0x06 0x5c 0x04 0x06 0x66 0x04    R..\..f.
    0020   0x06 0x70 0x04 0x08 0x7a 0x04 0x06 0x84    .p..z...
    0028   0x04 0x06 0x8e 0x04 0x06 0x98 0x04 0x06    ........
    0030   0xa2 0x04 0x06 0xac 0x04 0x34 0xb6 0x04    .....4..
    0038   0xc2 0xc0 0x04                             ...
    decimal
             92   59    8   12    4    6   22    4
              6   32    4    6   42    4    6   52
              4  112   62    4   44   72    4    6
             82    4    6   92    4    6  102    4
              6  112    4    8  122    4    6  132
              4    6  142    4    6  152    4    6
            162    4    6  172    4   52  182    4
            194  192    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2015-02-09T23:38:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 5.5}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0xdc 0x00    ........
    decimal
              1    0  180    0  180    0  220    0
    datetime (2015-02-09T23:38:14)
    0000   0x0e 0xa6 0x57 0x69 0x0f                   ..Wi.
    body (0)

#### RECORD 32 BasalProfileStart 2015-02-10T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-10T00:00:00)
    0000   0x00 0x80 0x00 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 33 MResultTotals 2015-02-10T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0x60                   ....`
    decimal
              7    0    0    9   96
    datetime (2015-02-10T00:00:00)
    0000   0x29 0x0f                                  ).
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 34 Sara6E 2015-02-10T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-10T00:00:00)
    0000   0x29 0x0f                                  ).
    body (49)
    hex
    0000   0x05 0x00 0x9f 0x56 0xef 0x03 0x00 0x00    ...V....
    0008   0x09 0x60 0x03 0x24 0x21 0x06 0x3c 0x43    .`.$!.<C
    0010   0x01 0x05 0x05 0x60 0x00 0x64 0x00 0x00    ...`.d..
    0018   0x00 0x78 0x05 0x02 0x00 0x01 0x00 0xad    .x......
    0020   0x2b 0x39 0x00 0x9b 0x2f 0x03 0x01 0x00    +9../...
    0028   0x00 0x00 0x05 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  159   86  239    3    0    0
              9   96    3   36   33    6   60   67
              1    5    5   96    0  100    0    0
              0  120    5    2    0    1    0  173
             43   57    0  155   47    3    1    0
              0    0    5    0    0    0    0    0
              0

#### RECORD 35 SensorAlert 2015-02-10T00:03:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 242}
```
    op hex (3)
    0000   0x0b 0x65 0xf2                             .e.
    decimal
             11  101  242
    datetime (2015-02-10T00:03:02)
    0000   0x02 0x83 0x20 0xaa 0x0f                   .. ..
    body (0)

#### RECORD 36 SensorAlert 2015-02-10T02:49:10 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-10T02:49:10)
    0000   0x0a 0xb1 0x22 0xaa 0x0f                   .."..
    body (0)

#### RECORD 37 SensorAlert 2015-02-10T02:53:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-10T02:53:04)
    0000   0x04 0xb5 0x22 0xaa 0x0f                   .."..
    body (0)

#### RECORD 38 Bolus 2015-02-10T03:05:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x4c 0x00    ..x.x.L.
    decimal
              1    0  120    0  120    0   76    0
    datetime (2015-02-10T03:05:28)
    0000   0x1c 0x85 0x43 0x6a 0x0f                   ..Cj.
    body (0)

#### RECORD 39 SensorAlert 2015-02-10T03:43:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-10T03:43:00)
    0000   0x00 0xab 0x23 0xaa 0x0f                   ..#..
    body (0)

#### RECORD 40 BasalProfileStart 2015-02-10T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-10T04:00:00)
    0000   0x00 0x80 0x04 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 41 SensorAlert 2015-02-10T04:23:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 242}
```
    op hex (3)
    0000   0x0b 0x65 0xf2                             .e.
    decimal
             11  101  242
    datetime (2015-02-10T04:23:43)
    0000   0x2b 0x97 0x24 0xaa 0x0f                   +.$..
    body (0)

#### RECORD 42 CalBGForPH 2015-02-10T04:36:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 243}
```
    op hex (2)
    0000   0x0a 0xf3                                  ..
    decimal
             10  243
    datetime (2015-02-10T04:36:40)
    0000   0x28 0xa4 0x24 0x6a 0x0f                   (.$j.
    body (0)

#### RECORD 43 BGReceived 2015-02-10T04:36:40 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 243, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1e                                  ?.
    decimal
             63   30
    datetime (2015-02-10T04:36:40)
    0000   0x28 0xa4 0x64 0x6a 0x0f                   (.dj.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 44 BolusWizard 2015-02-10T04:36:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 243,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 3.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 2.3}
```
    op hex (2)
    0000   0x5b 0xf3                                  [.
    decimal
             91  243
    datetime (2015-02-10T04:36:47)
    0000   0x2f 0xa4 0x04 0x0a 0x0f                   /....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x78 0x00    .P.d(Zx.
    0008   0x00 0x00 0x00 0x5c 0x00 0x1c 0x78         ...\..x
    decimal
              0   80    0  100   40   90  120    0
              0    0    0   92    0   28  120

#### RECORD 45 UnabsorbedInsulinBolus unknown head[116], body[0] op[0x5c]
###### DECODED
```python
[{'age': 90, 'amount': 2.2},
 {'age': 100, 'amount': 0.8},
 {'age': 120, 'amount': 0.05},
 {'age': 130, 'amount': 0.15},
 {'age': 140, 'amount': 0.15},
 {'age': 150, 'amount': 0.15},
 {'age': 160, 'amount': 0.2},
 {'age': 170, 'amount': 0.15},
 {'age': 180, 'amount': 0.15},
 {'age': 190, 'amount': 0.15},
 {'age': 200, 'amount': 0.15},
 {'age': 210, 'amount': 0.15},
 {'age': 220, 'amount': 0.15},
 {'age': 230, 'amount': 0.15},
 {'age': 240, 'amount': 0.15},
 {'age': 250, 'amount': 0.2},
 {'age': 260, 'amount': 0.15},
 {'age': 270, 'amount': 0.15},
 {'age': 280, 'amount': 0.15},
 {'age': 290, 'amount': 0.15},
 {'age': 300, 'amount': 4.6},
 {'age': 310, 'amount': 0.2},
 {'age': 320, 'amount': 0.15},
 {'age': 330, 'amount': 0.15},
 {'age': 340, 'amount': 0.15},
 {'age': 350, 'amount': 0.15},
 {'age': 360, 'amount': 2.8},
 {'age': 370, 'amount': 1.1},
 {'age': 380, 'amount': 0.15},
 {'age': 390, 'amount': 0.15},
 {'age': 400, 'amount': 0.15},
 {'age': 410, 'amount': 0.15},
 {'age': 420, 'amount': 0.2},
 {'age': 430, 'amount': 0.15},
 {'age': 440, 'amount': 0.15},
 {'age': 450, 'amount': 0.15},
 {'age': 460, 'amount': 0.15},
 {'age': 470, 'amount': 0.15}]
```
    op hex (116)
    0000   0x5c 0x74 0x58 0x5a 0x04 0x20 0x64 0x04    \tXZ. d.
    0008   0x02 0x78 0x04 0x06 0x82 0x04 0x06 0x8c    .x......
    0010   0x04 0x06 0x96 0x04 0x08 0xa0 0x04 0x06    ........
    0018   0xaa 0x04 0x06 0xb4 0x04 0x06 0xbe 0x04    ........
    0020   0x06 0xc8 0x04 0x06 0xd2 0x04 0x06 0xdc    ........
    0028   0x04 0x06 0xe6 0x04 0x06 0xf0 0x04 0x08    ........
    0030   0xfa 0x04 0x06 0x04 0x14 0x06 0x0e 0x14    ........
    0038   0x06 0x18 0x14 0x06 0x22 0x14 0xb8 0x2c    ...."..,
    0040   0x14 0x08 0x36 0x14 0x06 0x40 0x14 0x06    ..6..@..
    0048   0x4a 0x14 0x06 0x54 0x14 0x06 0x5e 0x14    J..T..^.
    0050   0x70 0x68 0x14 0x2c 0x72 0x14 0x06 0x7c    ph.,r..|
    0058   0x14 0x06 0x86 0x14 0x06 0x90 0x14 0x06    ........
    0060   0x9a 0x14 0x08 0xa4 0x14 0x06 0xae 0x14    ........
    0068   0x06 0xb8 0x14 0x06 0xc2 0x14 0x06 0xcc    ........
    0070   0x14 0x06 0xd6 0x14                        ....
    decimal
             92  116   88   90    4   32  100    4
              2  120    4    6  130    4    6  140
              4    6  150    4    8  160    4    6
            170    4    6  180    4    6  190    4
              6  200    4    6  210    4    6  220
              4    6  230    4    6  240    4    8
            250    4    6    4   20    6   14   20
              6   24   20    6   34   20  184   44
             20    8   54   20    6   64   20    6
             74   20    6   84   20    6   94   20
            112  104   20   44  114   20    6  124
             20    6  134   20    6  144   20    6
            154   20    8  164   20    6  174   20
              6  184   20    6  194   20    6  204
             20    6  214   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2015-02-10T04:36:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6,
 'duration': 0,
 'programmed': 1.6,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x5c 0x00    ..@.@.\.
    decimal
              1    0   64    0   64    0   92    0
    datetime (2015-02-10T04:36:48)
    0000   0x30 0xa4 0x44 0x0a 0x0f                   0.D..
    body (0)

#### RECORD 47 SensorAlert 2015-02-10T05:54:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 276}
```
    op hex (3)
    0000   0x0b 0x65 0x14                             .e.
    decimal
             11  101   20
    datetime (2015-02-10T05:54:30)
    0000   0x1e 0xb6 0x25 0xaa 0x8f                   ..%..
    body (0)

#### RECORD 48 Bolus 2015-02-10T06:33:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x2c 0x00    ..x.x.,.
    decimal
              1    0  120    0  120    0   44    0
    datetime (2015-02-10T06:33:13)
    0000   0x0d 0xa1 0x46 0x6a 0x0f                   ..Fj.
    body (0)

#### RECORD 49 BasalProfileStart 2015-02-10T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-10T07:00:00)
    0000   0x00 0x80 0x07 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 50 PumpSuspend 2015-02-10T07:12:32 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-10T07:12:32)
    0000   0x20 0x8c 0x07 0x0a 0x0f                    ....
    body (0)

#### RECORD 51 BasalProfileStart 2015-02-10T07:32:23 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-10T07:32:23)
    0000   0x17 0xa0 0x07 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 52 PumpResume 2015-02-10T07:32:24 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-10T07:32:24)
    0000   0x18 0xa0 0x07 0x0a 0x0f                   .....
    body (0)

#### RECORD 53 SensorAlert 2015-02-10T07:33:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 290}
```
    op hex (3)
    0000   0x0b 0x65 0x22                             .e"
    decimal
             11  101   34
    datetime (2015-02-10T07:33:03)
    0000   0x03 0xa1 0x27 0xaa 0x8f                   ..'..
    body (0)

#### RECORD 54 BolusWizard 2015-02-10T07:45:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.6,
 'carb_input': 70,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 7.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-10T07:45:41)
    0000   0x29 0xad 0x07 0x6a 0x0f                   )..j.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    FP.d(Z..
    0008   0x18 0x00 0x00 0x00 0x01 0x18 0x78         ......x
    decimal
             70   80    0  100   40   90    0    1
             24    0    0    0    1   24  120

#### RECORD 55 UnabsorbedInsulinBolus unknown head[68], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 3.0},
 {'age': 189, 'amount': 1.6},
 {'age': 279, 'amount': 2.2},
 {'age': 289, 'amount': 0.8},
 {'age': 309, 'amount': 0.05},
 {'age': 319, 'amount': 0.15},
 {'age': 329, 'amount': 0.15},
 {'age': 339, 'amount': 0.15},
 {'age': 349, 'amount': 0.2},
 {'age': 359, 'amount': 0.15},
 {'age': 369, 'amount': 0.15},
 {'age': 379, 'amount': 0.15},
 {'age': 389, 'amount': 0.15},
 {'age': 399, 'amount': 0.15},
 {'age': 409, 'amount': 0.15},
 {'age': 419, 'amount': 0.15},
 {'age': 429, 'amount': 0.15},
 {'age': 439, 'amount': 0.2},
 {'age': 449, 'amount': 0.15},
 {'age': 459, 'amount': 0.15},
 {'age': 469, 'amount': 0.15},
 {'age': 479, 'amount': 0.15}]
```
    op hex (68)
    0000   0x5c 0x44 0x78 0x4f 0x04 0x40 0xbd 0x04    \DxO.@..
    0008   0x58 0x17 0x14 0x20 0x21 0x14 0x02 0x35    X.. !..5
    0010   0x14 0x06 0x3f 0x14 0x06 0x49 0x14 0x06    ..?..I..
    0018   0x53 0x14 0x08 0x5d 0x14 0x06 0x67 0x14    S..]..g.
    0020   0x06 0x71 0x14 0x06 0x7b 0x14 0x06 0x85    .q..{...
    0028   0x14 0x06 0x8f 0x14 0x06 0x99 0x14 0x06    ........
    0030   0xa3 0x14 0x06 0xad 0x14 0x08 0xb7 0x14    ........
    0038   0x06 0xc1 0x14 0x06 0xcb 0x14 0x06 0xd5    ........
    0040   0x14 0x06 0xdf 0x14                        ....
    decimal
             92   68  120   79    4   64  189    4
             88   23   20   32   33   20    2   53
             20    6   63   20    6   73   20    6
             83   20    8   93   20    6  103   20
              6  113   20    6  123   20    6  133
             20    6  143   20    6  153   20    6
            163   20    6  173   20    8  183   20
              6  193   20    6  203   20    6  213
             20    6  223   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2015-02-10T07:49:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 120,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x60 0x04    ..P.P.`.
    decimal
              1    0   80    0   80    0   96    4
    datetime (2015-02-10T07:49:04)
    0000   0x04 0xb1 0xa7 0x6a 0x0f                   ...j.
    body (0)

#### RECORD 57 Bolus 2015-02-10T07:45:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x60 0x00    ......`.
    decimal
              1    0  200    0  200    0   96    0
    datetime (2015-02-10T07:45:42)
    0000   0x2a 0xad 0x87 0x6a 0x0f                   *..j.
    body (0)

#### RECORD 58 SensorAlert 2015-02-10T09:33:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-10T09:33:03)
    0000   0x03 0xa1 0x29 0xaa 0x0f                   ..)..
    body (0)

#### RECORD 59 SensorAlert 2015-02-10T09:43:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-02-10T09:43:42)
    0000   0x2a 0xab 0x29 0xaa 0x0f                   *.)..
    body (0)

#### RECORD 60 BasalProfileStart 2015-02-10T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-10T10:00:00)
    0000   0x00 0x80 0x0a 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 61 Bolus 2015-02-10T10:32:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x58 0x00    ..P.P.X.
    decimal
              1    0   80    0   80    0   88    0
    datetime (2015-02-10T10:32:33)
    0000   0x21 0xa0 0x4a 0x6a 0x0f                   !.Jj.
    body (0)

#### RECORD 62 SensorAlert 2015-02-10T11:14:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 239}
```
    op hex (3)
    0000   0x0b 0x65 0xef                             .e.
    decimal
             11  101  239
    datetime (2015-02-10T11:14:30)
    0000   0x1e 0x8e 0x2b 0xaa 0x0f                   ..+..
    body (0)

#### RECORD 63 Bolus 2015-02-10T11:15:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 2.9}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x74 0x00    ..d.d.t.
    decimal
              1    0  100    0  100    0  116    0
    datetime (2015-02-10T11:15:13)
    0000   0x0d 0x8f 0x4b 0x6a 0x0f                   ..Kj.
    body (0)

`end ReadHistoryData-page-33.data: 64 records`
