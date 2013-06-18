## START logs/ReadHistoryData-page-22.data
#### RECORD 0 hack1 2013-03-24T09:20:55 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x37 0x8d 0x05 0x10 0xd9 0x46 0x8f    m7....F.
    0008   0x0b 0x00 0x00 0x04 0xce 0x03 0x72 0x48    ......rH
    0010   0x01 0x5c 0x1c 0x00 0x18 0x01 0x5c 0x1c    .\....\.
    0018   0x00 0x48 0x15 0x01 0x14 0x4f 0x00 0x00    .H...O..
    0020   0x00 0x04 0x00 0x03 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x1e 0x00              ......
    decimal
            109   55  141    5   16  217   70  143
             11    0    0    4  206    3  114   72
              1   92   28    0   24    1   92   28
              0   72   21    1   20   79    0    0
              0    4    0    3    1    0   12    0
            232    0    0    0   30    0
    datetime (2013-03-24T09:20:55)
    0000   0x37 0xd4 0x09 0x18 0x0d                   7....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 PumpResume 2013-03-24T09:33:23 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-24T09:33:23)
    0000   0x17 0xe1 0x09 0x18 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 CalBGForPH 2013-03-24T13:04:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-24T13:04:47)
    0000   0x2f 0xc4 0x2d 0x18 0x0d                   /.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-24T13:05:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-24T13:05:29)
    0000   0x1d 0xc5 0x2d 0x18 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-03-24T13:07:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-03-24T13:07:27)
    0000   0x1b 0xc7 0x0d 0x18 0x0d                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xfc 0x18 0xf0     P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             32   80   13   45  106  252   24  240
              0    0    0   20  125
    HOUR BITS: [1, 1, 0]
#### RECORD 5 Bolus 2013-03-24T13:07:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-03-24T13:07:27)
    0000   0x1b 0xc7 0x4d 0x18 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2013-03-24T13:15:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-03-24T13:15:28)
    0000   0x1c 0xcf 0x2d 0x18 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 BolusWizard 2013-03-24T13:15:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-03-24T13:15:48)
    0000   0x30 0xcf 0x0d 0x18 0x0d                   0....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x14 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0   20    0   13  125
    HOUR BITS: [1, 1, 0]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x0b 0x04                   \.P..
    decimal
             92    5   80   11    4
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-03-24T13:15:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-03-24T13:15:49)
    0000   0x31 0xcf 0x4d 0x18 0x0d                   1.M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 CalBGForPH 2013-03-24T13:32:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2013-03-24T13:32:59)
    0000   0x3b 0xe0 0x2d 0x18 0x0d                   ;.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 BolusWizard 2013-03-24T13:33:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 97,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 19,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 1.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x61                                  [a
    decimal
             91   97
    datetime (2013-03-24T13:33:22)
    0000   0x16 0xe1 0x0d 0x18 0x0d                   .....
    body (13)
    hex
    0000   0x13 0x50 0x0d 0x2d 0x6a 0xfe 0x0e 0xf0    .P.-j...
    0008   0x00 0x20 0x00 0x0c 0x7d                   . ..}
    decimal
             19   80   13   45  106  254   14  240
              0   32    0   12  125
    HOUR BITS: [1, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 1.3, 'curve': 4},
 {'age': 29, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x13 0x04 0x50 0x1d 0x04    \.4..P..
    decimal
             92    8   52   19    4   80   29    4
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-03-24T13:33:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-03-24T13:33:22)
    0000   0x16 0xe1 0x4d 0x18 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 CalBGForPH 2013-03-24T15:08:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 46}
```
    op hex (2)
    0000   0x0a 0x2e                                  ..
    decimal
             10   46
    datetime (2013-03-24T15:08:41)
    0000   0x29 0xc8 0x2f 0x18 0x0d                   )./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2013-03-24T18:40:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-03-24T18:40:13)
    0000   0x0d 0xe8 0x32 0x18 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 16 CalBGForPH 2013-03-24T18:55:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-03-24T18:55:19)
    0000   0x13 0xf7 0x32 0x18 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 BolusWizard 2013-03-24T18:56:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-03-24T18:56:18)
    0000   0x12 0xf8 0x12 0x18 0x0d                   .....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 0.25, 'curve': 20},
 {'age': 76, 'amount': 0.95, 'curve': 20},
 {'age': 86, 'amount': 1.3, 'curve': 20},
 {'age': 96, 'amount': 2.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0a 0x42 0x14 0x26 0x4c 0x14    \..B.&L.
    0008   0x34 0x56 0x14 0x50 0x60 0x14              4V.P`.
    decimal
             92   14   10   66   20   38   76   20
             52   86   20   80   96   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-03-24T18:56:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-03-24T18:56:18)
    0000   0x12 0xf8 0x52 0x18 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 CalBGForPH 2013-03-24T19:23:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-03-24T19:23:19)
    0000   0x13 0xd7 0x33 0x18 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 21 CalBGForPH 2013-03-24T19:34:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-03-24T19:34:56)
    0000   0x38 0xe2 0x33 0x18 0x0d                   8.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 22 BolusWizard 2013-03-24T19:35:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 5,
 '_byte[7]': 0,
 'bg': 151,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x97                                  [.
    decimal
             91  151
    datetime (2013-03-24T19:35:32)
    0000   0x20 0xe3 0x13 0x18 0x0d                    ....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x05 0x15 0x00    .P.-j...
    0008   0x00 0x10 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    5   21    0
              0   16    0   21  125
    HOUR BITS: [1, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 1.7, 'curve': 4},
 {'age': 105, 'amount': 0.25, 'curve': 20},
 {'age': 115, 'amount': 0.95, 'curve': 20},
 {'age': 125, 'amount': 1.3, 'curve': 20},
 {'age': 135, 'amount': 2.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x44 0x29 0x04 0x0a 0x69 0x14    \.D)..i.
    0008   0x26 0x73 0x14 0x34 0x7d 0x14 0x50 0x87    &s.4}.P.
    0010   0x14                                       .
    decimal
             92   17   68   41    4   10  105   20
             38  115   20   52  125   20   80  135
             20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-03-24T19:35:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-03-24T19:35:32)
    0000   0x20 0xe3 0x53 0x18 0x0d                    .S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 ResultTotals 2013-02-24T13:13:56 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc6                   .....
    decimal
              7    0    0    4  198
    datetime (2013-02-24T13:13:56)
    0000   0x38 0x8d 0x6d 0x38 0x8d                   8.m8.
    body (41)
    hex
    0000   0x05 0x00 0x6d 0x2e 0x97 0x09 0x00 0x00    ..m.....
    0008   0x04 0xc6 0x03 0x7a 0x49 0x01 0x4c 0x1b    ...zI.L.
    0010   0x00 0x78 0x01 0x4c 0x1b 0x01 0x4c 0x64    .x.L..Ld
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x05 0x05    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  109   46  151    9    0    0
              4  198    3  122   73    1   76   27
              0  120    1   76   27    1   76  100
              0    0    0    0    0    0    5    5
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 PumpSuspend 2013-03-25T13:01:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-25T13:01:55)
    0000   0x37 0xc1 0x0d 0x19 0x0d                   7....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 PumpResume 2013-03-25T13:53:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-25T13:53:08)
    0000   0x08 0xf5 0x0d 0x19 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 CalBGForPH 2013-03-25T13:53:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-03-25T13:53:15)
    0000   0x0f 0xf5 0x2d 0x19 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 29 CalBGForPH 2013-03-25T13:57:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-03-25T13:57:19)
    0000   0x13 0xf9 0x2d 0x19 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 BolusWizard 2013-03-25T13:57:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-03-25T13:57:34)
    0000   0x22 0xf9 0x0d 0x19 0x0d                   "....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x00 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             45   80   13   45  106    0   34    0
              0    0    0   34  125
    HOUR BITS: [1, 1, 1]
#### RECORD 31 Bolus 2013-03-25T13:57:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-03-25T13:57:34)
    0000   0x22 0xf9 0x4d 0x19 0x0d                   ".M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 BolusWizard 2013-03-25T14:50:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-03-25T14:50:06)
    0000   0x06 0xf2 0x0e 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125
    HOUR BITS: [1, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 3.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x88 0x38 0x04                   \..8.
    decimal
             92    5  136   56    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-03-25T14:50:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-03-25T14:50:06)
    0000   0x06 0xf2 0x4e 0x19 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 CalBGForPH 2013-03-25T16:21:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 145}
```
    op hex (2)
    0000   0x0a 0x91                                  ..
    decimal
             10  145
    datetime (2013-03-25T16:21:00)
    0000   0x00 0xd5 0x30 0x19 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 CalBGForPH 2013-03-25T16:36:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 147}
```
    op hex (2)
    0000   0x0a 0x93                                  ..
    decimal
             10  147
    datetime (2013-03-25T16:36:07)
    0000   0x07 0xe4 0x30 0x19 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 37 BolusWizard 2013-03-25T16:36:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 147,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 1.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x93                                  [.
    decimal
             91  147
    datetime (2013-03-25T16:36:12)
    0000   0x0c 0xe4 0x10 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x04 0x11 0x00    .P.-j...
    0008   0x00 0x0d 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    4   17    0
              0   13    0   17  125
    HOUR BITS: [1, 1, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 0.9, 'curve': 4},
 {'age': 162, 'amount': 3.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x70 0x04 0x88 0xa2 0x04    \.$p....
    decimal
             92    8   36  112    4  136  162    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-03-25T16:36:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-03-25T16:36:13)
    0000   0x0d 0xe4 0x50 0x19 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 CalBGForPH 2013-03-25T17:58:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2013-03-25T17:58:29)
    0000   0x1d 0xfa 0x31 0x19 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 CalBGForPH 2013-03-25T17:58:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2013-03-25T17:58:59)
    0000   0x3b 0xfa 0x31 0x19 0x0d                   ;.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 BolusWizard 2013-03-25T18:00:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 183,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb7                                  [.
    decimal
             91  183
    datetime (2013-03-25T18:00:02)
    0000   0x02 0xc0 0x12 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x0c 0x18 0x00     P.-j...
    0008   0x00 0x0d 0x00 0x18 0x7d                   ....}
    decimal
             32   80   13   45  106   12   24    0
              0   13    0   24  125
    HOUR BITS: [1, 1, 0]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 1.7, 'curve': 4},
 {'age': 196, 'amount': 0.9, 'curve': 4},
 {'age': 246, 'amount': 3.4, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x44 0x56 0x04 0x24 0xc4 0x04    \.DV.$..
    0008   0x88 0xf6 0x04                             ...
    decimal
             92   11   68   86    4   36  196    4
            136  246    4
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-03-25T18:00:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-03-25T18:00:02)
    0000   0x02 0xc0 0x52 0x19 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 ResultTotals 2013-02-25T13:13:57 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xae                   .....
    decimal
              7    0    0    4  174
    datetime (2013-02-25T13:13:57)
    0000   0x39 0x8d 0x6d 0x39 0x8d                   9.m9.
    body (41)
    hex
    0000   0x05 0x00 0x93 0x70 0xb7 0x06 0x00 0x00    ...p....
    0008   0x04 0xae 0x03 0x5e 0x48 0x01 0x50 0x1c    ...^H.P.
    0010   0x00 0x70 0x01 0x50 0x1c 0x01 0x50 0x64    .p.P..Pd
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x04 0x04    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  147  112  183    6    0    0
              4  174    3   94   72    1   80   28
              0  112    1   80   28    1   80  100
              0    0    0    0    0    0    4    4
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 46 PumpSuspend 2013-03-26T10:48:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-26T10:48:39)
    0000   0x27 0xf0 0x0a 0x1a 0x0d                   '....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 47 PumpResume 2013-03-26T11:09:41 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-26T11:09:41)
    0000   0x29 0xc9 0x0b 0x1a 0x0d                   )....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 CalBGForPH 2013-03-26T11:41:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 213}
```
    op hex (2)
    0000   0x0a 0xd5                                  ..
    decimal
             10  213
    datetime (2013-03-26T11:41:13)
    0000   0x0d 0xe9 0x2b 0x1a 0x0d                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 BolusWizard 2013-03-26T11:41:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 213,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd5                                  [.
    decimal
             91  213
    datetime (2013-03-26T11:41:22)
    0000   0x16 0xe9 0x0b 0x1a 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x13 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
              0   80   13   45  106   19    0    0
              0    0    0   19  125
    HOUR BITS: [1, 1, 1]
#### RECORD 50 Bolus 2013-03-26T11:41:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-03-26T11:41:22)
    0000   0x16 0xe9 0x4b 0x1a 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 51 CalBGForPH 2013-03-26T11:55:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 235}
```
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2013-03-26T11:55:03)
    0000   0x03 0xf7 0x2b 0x1a 0x0d                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 BolusWizard 2013-03-26T11:55:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 235,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xeb                                  [.
    decimal
             91  235
    datetime (2013-03-26T11:55:10)
    0000   0x0a 0xf7 0x0b 0x1a 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x18 0x00 0x00    .P.-j...
    0008   0x00 0x14 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   24    0    0
              0   20    0    4  125
    HOUR BITS: [1, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x15 0x04                   \.P..
    decimal
             92    5   80   21    4
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-03-26T11:55:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-03-26T11:55:10)
    0000   0x0a 0xf7 0x4b 0x1a 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 55 CalBGForPH 2013-03-26T12:26:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 195}
```
    op hex (2)
    0000   0x0a 0xc3                                  ..
    decimal
             10  195
    datetime (2013-03-26T12:26:16)
    0000   0x10 0xda 0x2c 0x1a 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 CalBGForPH 2013-03-26T12:54:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2013-03-26T12:54:40)
    0000   0x28 0xf6 0x2c 0x1a 0x0d                   (.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 57 CalBGForPH 2013-03-26T13:59:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-03-26T13:59:49)
    0000   0x31 0xfb 0x2d 0x1a 0x0d                   1.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 58 BolusWizard 2013-03-26T13:59:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-03-26T13:59:55)
    0000   0x37 0xfb 0x0d 0x1a 0x0d                   7....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x0a 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0   10    0   21  125
    HOUR BITS: [1, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 0.8, 'curve': 4},
 {'age': 145, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x7d 0x04 0x50 0x91 0x04    \. }.P..
    decimal
             92    8   32  125    4   80  145    4
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-03-26T13:59:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-03-26T13:59:55)
    0000   0x37 0xfb 0x4d 0x1a 0x0d                   7.M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 61 CalBGForPH 2013-03-26T15:07:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-03-26T15:07:30)
    0000   0x1e 0xc7 0x2f 0x1a 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 CalBGForPH 2013-03-26T18:34:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 457}
```
    op hex (2)
    0000   0x0a 0xc9                                  ..
    decimal
             10  201
    datetime (2013-03-26T18:34:00)
    0000   0x00 0xe2 0x32 0x1a 0x8d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 63 BolusWizard 2013-03-26T18:34:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 73,
 '_byte[7]': 0,
 'bg': 457,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 7.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc9                                  [.
    decimal
             91  201
    datetime (2013-03-26T18:34:03)
    0000   0x03 0xe2 0x12 0x1a 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x49 0x00 0x00    .Q.-jI..
    0008   0x00 0x00 0x00 0x49 0x7d                   ...I}
    decimal
              0   81   13   45  106   73    0    0
              0    0    0   73  125
    HOUR BITS: [1, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 2.1, 'curve': 20},
 {'age': 144, 'amount': 0.8, 'curve': 20},
 {'age': 164, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x54 0x18 0x14 0x20 0x90 0x14    \.T.. ..
    0008   0x50 0xa4 0x14                             P..
    decimal
             92   11   84   24   20   32  144   20
             80  164   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-03-26T18:34:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.3, 'dual_component': '??', 'programmed': 7.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x49 0x49 0x00                        .II.
    decimal
              1   73   73    0
    datetime (2013-03-26T18:34:03)
    0000   0x03 0xe2 0x52 0x1a 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 CalBGForPH 2013-03-26T21:12:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-03-26T21:12:47)
    0000   0x2f 0xcc 0x35 0x1a 0x0d                   /.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 ResultTotals 2013-02-26T13:13:58 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x5c                   ....\
    decimal
              7    0    0    5   92
    datetime (2013-02-26T13:13:58)
    0000   0x3a 0x8d 0x6d 0x3a 0x8d                   :.m:.
    body (41)
    hex
    0000   0x05 0x10 0xdb 0x75 0xc9 0x08 0x00 0x00    ...u....
    0008   0x05 0x5c 0x03 0x74 0x40 0x01 0xe8 0x24    .\.t@..$
    0010   0x00 0x1c 0x01 0xe8 0x24 0x00 0x54 0x11    ....$.T.
    0018   0x01 0x94 0x53 0x00 0x00 0x00 0x04 0x01    ..S.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  219  117  201    8    0    0
              5   92    3  116   64    1  232   36
              0   28    1  232   36    0   84   17
              1  148   83    0    0    0    4    1
              3    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 68 LowReservoir 2013-03-27T07:56:50 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-27T07:56:50)
    0000   0x32 0xf8 0x07 0x1b 0x0d                   2....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 PumpSuspend 2013-03-27T13:24:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-27T13:24:56)
    0000   0x38 0xd8 0x0d 0x1b 0x0d                   8....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 70 PumpResume 2013-03-27T13:56:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-27T13:56:35)
    0000   0x23 0xf8 0x0d 0x1b 0x0d                   #....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 71 Rewind 2013-03-27T15:31:24 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-03-27T15:31:24)
    0000   0x18 0xdf 0x0f 0x1b 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 Prime 2013-03-27T15:33:29 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x0d                   .....
    decimal
              3    0    0    0   13
    datetime (2013-03-27T15:33:29)
    0000   0x1d 0xe1 0x2f 0x1b 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 73 Prime 2013-03-27T15:33:47 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-03-27T15:33:47)
    0000   0x2f 0xe1 0x0f 0x1b 0x0d                   /....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 74 CalBGForPH 2013-03-27T15:37:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-27T15:37:53)
    0000   0x35 0xe5 0x2f 0x1b 0x0d                   5./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 75 BolusWizard 2013-03-27T15:38:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 67,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 5.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-03-27T15:38:20)
    0000   0x14 0xe6 0x0f 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x43 0x50 0x0d 0x2d 0x6a 0xfc 0x33 0xf0    CP.-j.3.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             67   80   13   45  106  252   51  240
              0    0    0   47  125
    HOUR BITS: [1, 1, 1]
#### RECORD 76 Bolus 2013-03-27T15:38:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-03-27T15:38:20)
    0000   0x14 0xe6 0x4f 0x1b 0x0d                   ..O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 77 CalBGForPH 2013-03-27T17:27:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 258}
```
    op hex (2)
    0000   0x0a 0x02                                  ..
    decimal
             10    2
    datetime (2013-03-27T17:27:43)
    0000   0x2b 0xdb 0x31 0x1b 0x8d                   +.1..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 78 BolusWizard 2013-03-27T17:27:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 258,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x02                                  [.
    decimal
             91    2
    datetime (2013-03-27T17:27:47)
    0000   0x2f 0xdb 0x11 0x1b 0x0d                   /....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x18 0x00 0x05 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0   24    0    5  125
    HOUR BITS: [1, 1, 0]
#### RECORD 79 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 113, 'amount': 4.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xbc 0x71 0x04                   \..q.
    decimal
             92    5  188  113    4
    datetime (unknown)

    body (0)

#### RECORD 80 Bolus 2013-03-27T17:27:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-03-27T17:27:47)
    0000   0x2f 0xdb 0x51 0x1b 0x0d                   /.Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 81 CalBGForPH 2013-03-27T18:11:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 313}
```
    op hex (2)
    0000   0x0a 0x39                                  .9
    decimal
             10   57
    datetime (2013-03-27T18:11:54)
    0000   0x36 0xcb 0x32 0x1b 0x8d                   6.2..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 82 BolusWizard 2013-03-27T18:12:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 41,
 '_byte[7]': 0,
 'bg': 313,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x39                                  [9
    decimal
             91   57
    datetime (2013-03-27T18:12:01)
    0000   0x01 0xcc 0x12 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x29 0x00 0x00    .Q.-j)..
    0008   0x00 0x12 0x00 0x17 0x7d                   ....}
    decimal
              0   81   13   45  106   41    0    0
              0   18    0   23  125
    HOUR BITS: [1, 1, 0]
#### RECORD 83 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x02                                  ..
    decimal
              0    2
    datetime (unknown)
    0000   0x20                                        
    body (0)

`end logs/ReadHistoryData-page-22.data: 84 records`
