## START logs/ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 786, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x49 0x7d 0x5c 0x0b 0x54 0x18 0x14 0x20    I}\.T.. 
    0008   0x90 0x14 0x50 0xa4 0x14 0x01 0x49 0x49    ..P...II
    0010   0x00 0x03 0xe2 0x52 0x1a 0x0d 0x0a 0xc8    ...R....
    0018   0x2f 0xcc 0x35 0x1a 0x0d 0x07 0x00 0x00    /.5.....
##### DEBUG DECIMAL
             73  125   92   11   84   24   20   32
            144   20   80  164   20    1   73   73
              0    3  226   82   26   13   10  200
             47  204   53   26   13    7    0    0
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
#### RECORD 25 ResultTotals 2013-02-24T13:13:56 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc6                   .....
    decimal
              7    0    0    4  198
    datetime (2013-02-24T13:13:56)
    0000   0x38 0x8d 0x6d 0x38 0x8d                   8.m8.
    body (51)
    hex
    0000   0x05 0x00 0x6d 0x2e 0x97 0x09 0x00 0x00    ..m.....
    0008   0x04 0xc6 0x03 0x7a 0x49 0x01 0x4c 0x1b    ...zI.L.
    0010   0x00 0x78 0x01 0x4c 0x1b 0x01 0x4c 0x64    .x.L..Ld
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x05 0x05    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x37 0xc1 0x0d 0x19 0x0d    ...7....
    0030   0x1f 0x00 0x08                             ...
    decimal
              5    0  109   46  151    9    0    0
              4  198    3  122   73    1   76   27
              0  120    1   76   27    1   76  100
              0    0    0    0    0    0    5    5
              0    0    0   12    0  232    0    0
              0   30    0   55  193   13   25   13
             31    0    8
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 Base (2015, 0, 16, 10, 13, 25) head[2], body[0] op[0xf5]

    op hex (2)
    0000   0xf5 0x0d                                  ..
    decimal
            245   13
    datetime ((2015, 0, 16, 10, 13, 25))
    0000   0x19 0x0d 0x0a 0x70 0x0f                   ...p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 27 Base (2003, 0, 17, 10, 13, 25) head[2], body[0] op[0xf5]

    op hex (2)
    0000   0xf5 0x2d                                  .-
    decimal
            245   45
    datetime ((2003, 0, 17, 10, 13, 25))
    0000   0x19 0x0d 0x0a 0x71 0x13                   ...q.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 28 Base (2002, 0, 17, 27, 13, 25) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x2d                                  .-
    decimal
            249   45
    datetime ((2002, 0, 17, 27, 13, 25))
    0000   0x19 0x0d 0x5b 0x71 0x22                   ..[q"
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 29 Base (2013, 0, 16, 13, 13, 25) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x0d                                  ..
    decimal
            249   13
    datetime ((2013, 0, 16, 13, 13, 25))
    0000   0x19 0x0d 0x2d 0x50 0x0d                   ..-P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 30 Base (2000, 0, 0, 0, 34, 0) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 34, 0))
    0000   0x00 0x22 0x00 0x00 0x00                   ."...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 Base (2000, 4, 2, 2, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x22                                  ."
    decimal
              0   34
    datetime ((2000, 4, 2, 2, 1, 61))
    0000   0x7d 0x01 0x22 0x22 0x00                   }."".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 32 Base (2000, 4, 27, 13, 25, 13) head[2], body[0] op[0x22]

    op hex (2)
    0000   0x22 0xf9                                  ".
    decimal
             34  249
    datetime ((2000, 4, 27, 13, 25, 13))
    0000   0x4d 0x19 0x0d 0x5b 0x00                   M..[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 33 NoDelivery (2013, 0, 13, 16, 12, 13) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0xf2 0x0e 0x19                        ....
    decimal
              6  242   14   25
    datetime ((2013, 0, 13, 16, 12, 13))
    0000   0x0d 0x0c 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 34 Base (2000, 0, 0, 0, 0, 9) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x00                                  j.
    decimal
            106    0
    datetime ((2000, 0, 0, 0, 0, 9))
    0000   0x09 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 35 Base (2004, 4, 24, 8, 5, 28) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x7d                                  .}
    decimal
              9  125
    datetime ((2004, 4, 24, 8, 5, 28))
    0000   0x5c 0x05 0x88 0x38 0x04                   \..8.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 36 Bolus 2013-03-25T14:50:06 head[4], body[0] op[0x01]
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
#### RECORD 37 CalBGForPH 2013-03-25T16:21:00 head[2], body[0] op[0x0a]
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
#### RECORD 38 CalBGForPH 2013-03-25T16:36:07 head[2], body[0] op[0x0a]
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
#### RECORD 39 BolusWizard 2013-03-25T16:36:12 head[2], body[13] op[0x5b]
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
#### RECORD 40 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
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

#### RECORD 41 Bolus 2013-03-25T16:36:13 head[4], body[0] op[0x01]
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
#### RECORD 42 CalBGForPH 2013-03-25T17:58:29 head[2], body[0] op[0x0a]
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
#### RECORD 43 CalBGForPH 2013-03-25T17:58:59 head[2], body[0] op[0x0a]
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
#### RECORD 44 BolusWizard 2013-03-25T18:00:02 head[2], body[13] op[0x5b]
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
#### RECORD 45 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
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

#### RECORD 46 Bolus 2013-03-25T18:00:02 head[4], body[0] op[0x01]
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
#### RECORD 47 ResultTotals 2013-02-25T13:13:57 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xae                   .....
    decimal
              7    0    0    4  174
    datetime (2013-02-25T13:13:57)
    0000   0x39 0x8d 0x6d 0x39 0x8d                   9.m9.
    body (51)
    hex
    0000   0x05 0x00 0x93 0x70 0xb7 0x06 0x00 0x00    ...p....
    0008   0x04 0xae 0x03 0x5e 0x48 0x01 0x50 0x1c    ...^H.P.
    0010   0x00 0x70 0x01 0x50 0x1c 0x01 0x50 0x64    .p.P..Pd
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x04 0x04    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x27 0xf0 0x0a 0x1a 0x0d    ...'....
    0030   0x1f 0x00 0x29                             ..)
    decimal
              5    0  147  112  183    6    0    0
              4  174    3   94   72    1   80   28
              0  112    1   80   28    1   80  100
              0    0    0    0    0    0    4    4
              0    0    0   12    0  232    0    0
              0   30    0   39  240   10   26   13
             31    0   41
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 48 Base (2013, 0, 21, 10, 13, 26) head[2], body[0] op[0xc9]

    op hex (2)
    0000   0xc9 0x0b                                  ..
    decimal
            201   11
    datetime ((2013, 0, 21, 10, 13, 26))
    0000   0x1a 0x0d 0x0a 0xd5 0x0d                   .....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 49 Base (2006, 0, 21, 27, 13, 26) head[2], body[0] op[0xe9]

    op hex (2)
    0000   0xe9 0x2b                                  .+
    decimal
            233   43
    datetime ((2006, 0, 21, 27, 13, 26))
    0000   0x1a 0x0d 0x5b 0xd5 0x16                   ..[..
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 50 Base (2013, 0, 16, 0, 13, 26) head[2], body[0] op[0xe9]

    op hex (2)
    0000   0xe9 0x0b                                  ..
    decimal
            233   11
    datetime ((2013, 0, 16, 0, 13, 26))
    0000   0x1a 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 51 Base (2000, 0, 0, 0, 0, 19) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 19))
    0000   0x13 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 52 Base (2000, 4, 20, 20, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x13                                  ..
    decimal
              0   19
    datetime ((2000, 4, 20, 20, 1, 61))
    0000   0x7d 0x01 0x14 0x14 0x00                   }....
    body (0)

#### RECORD 53 TempBasalDuration 2011-04-10T13:26:11 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 6990}
```
    op hex (2)
    0000   0x16 0xe9                                  ..
    decimal
             22  233
    datetime (2011-04-10T13:26:11)
    0000   0x4b 0x1a 0x0d 0x0a 0xeb                   K....
    body (0)
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 54 Prime 2011-07-23T10:43:27 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.3, 'fixed': 4.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0xf7 0x2b 0x1a 0x0d                   ..+..
    decimal
              3  247   43   26   13
    datetime (2011-07-23T10:43:27)
    0000   0x5b 0xeb 0x0a 0xf7 0x0b                   [....
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 1, 1]
#### RECORD 55 Battery 2010-01-13T13:16:00 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x0d                                  ..
    decimal
             26   13
    datetime (2010-01-13T13:16:00)
    0000   0x00 0x50 0x0d 0x2d 0x6a                   .P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 56 NewTimeSet (2004, 0, 0, 20, 0, 0) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime ((2004, 0, 0, 20, 0, 0))
    0000   0x00 0x00 0x14 0x00 0x04                   .....
    body (0)

#### RECORD 57 Base (2001, 1, 4, 21, 16, 5) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x5c                                  }\
    decimal
            125   92
    datetime ((2001, 1, 4, 21, 16, 5))
    0000   0x05 0x50 0x15 0x04 0x01                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 58 ChangeBasalProfile (2010, 0, 11, 23, 10, 0) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x08                                  ..
    decimal
              8    8
    datetime ((2010, 0, 11, 23, 10, 0))
    0000   0x00 0x0a 0xf7 0x4b 0x1a                   ...K.
    body (44)
    hex
    0000   0x0d 0x0a 0xc3 0x10 0xda 0x2c 0x1a 0x0d    .....,..
    0008   0x0a 0x81 0x28 0xf6 0x2c 0x1a 0x0d 0x0a    ..(.,...
    0010   0x75 0x31 0xfb 0x2d 0x1a 0x0d 0x5b 0x75    u1.-..[u
    0018   0x37 0xfb 0x0d 0x1a 0x0d 0x1c 0x50 0x0d    7.....P.
    0020   0x2d 0x6a 0x00 0x15 0x00 0x00 0x0a 0x00    -j......
    0028   0x15 0x7d 0x5c 0x08                        .}\.
    decimal
             13   10  195   16  218   44   26   13
             10  129   40  246   44   26   13   10
            117   49  251   45   26   13   91  117
             55  251   13   26   13   28   80   13
             45  106    0   21    0    0   10    0
             21  125   92    8
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 59 Base (2001, 1, 4, 17, 16, 4) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x7d                                   }
    decimal
             32  125
    datetime ((2001, 1, 4, 17, 16, 4))
    0000   0x04 0x50 0x91 0x04 0x01                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 60 Base (2010, 0, 13, 27, 55, 0) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x15                                  ..
    decimal
             21   21
    datetime ((2010, 0, 13, 27, 55, 0))
    0000   0x00 0x37 0xfb 0x4d 0x1a                   .7.M.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 61 Base (2010, 12, 15, 7, 30, 14) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2010, 12, 15, 7, 30, 14))
    0000   0xce 0x1e 0xc7 0x2f 0x1a                   .../.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 62 Base (2010, 12, 18, 2, 0, 9) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2010, 12, 18, 2, 0, 9))
    0000   0xc9 0x00 0xe2 0x32 0x1a                   ...2.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 63 Base (2010, 12, 18, 2, 3, 9) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x5b                                  .[
    decimal
            141   91
    datetime ((2010, 12, 18, 2, 3, 9))
    0000   0xc9 0x03 0xe2 0x12 0x1a                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 64 Base (2009, 4, 10, 13, 13, 17) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2009, 4, 10, 13, 13, 17))
    0000   0x51 0x0d 0x2d 0x6a 0x49                   Q.-jI
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
`end logs/ReadHistoryData-page-33.data: 65 records`
