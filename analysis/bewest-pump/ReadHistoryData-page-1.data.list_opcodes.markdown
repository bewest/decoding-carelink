## START logs/ReadHistoryData-page-1.data
#### RECORD 0 CalForBG 2013-01-14T22:11:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-01-14T22:11:48)
    0000   0x30 0x4b 0x36 0x0e 0x0d                   0K6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 1 CalForBG 2013-01-14T22:35:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-01-14T22:35:17)
    0000   0x11 0x63 0x36 0x0e 0x0d                   .c6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 CalForBG 2013-01-14T22:35:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 83}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-01-14T22:35:46)
    0000   0x2e 0x63 0x36 0x0e 0x0d                   .c6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2013-01-14T22:36:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 83,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.7,
 'carb_input': 94,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.0}
```
    op hex (2)
    0000   0x5b 0x53                                  [S
    decimal
             91   83
    datetime (2013-01-14T22:36:00)
    0000   0x00 0x64 0x16 0x0e 0x0d                   .d...
    body (13)
    hex
    0000   0x5e 0x50 0x0d 0x2d 0x6a 0xfb 0x48 0xf0    ^P.-j.H.
    0008   0x00 0x0a 0x00 0x43 0x7d                   ...C}
    decimal
             94   80   13   45  106  251   72  240
              0   10    0   67  125
    HOUR BITS: [0, 1, 1]
#### RECORD 4 BolusGiven unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 0.9, 'curve': 4},
 {'age': 132, 'amount': 0.5, 'curve': 4},
 {'age': 172, 'amount': 0.35, 'curve': 4},
 {'age': 182, 'amount': 0.15, 'curve': 4},
 {'age': 212, 'amount': 2.2, 'curve': 4},
 {'age': 36, 'amount': 2.4, 'curve': 20},
 {'age': 126, 'amount': 2.1, 'curve': 20},
 {'age': 156, 'amount': 1.1, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x24 0x70 0x04 0x14 0x84 0x04    \.$p....
    0008   0x0e 0xac 0x04 0x06 0xb6 0x04 0x58 0xd4    ......X.
    0010   0x04 0x60 0x24 0x14 0x54 0x7e 0x14 0x2c    .`$.T~.,
    0018   0x9c 0x14                                  ..
    decimal
             92   26   36  112    4   20  132    4
             14  172    4    6  182    4   88  212
              4   96   36   20   84  126   20   44
            156   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-01-14T22:36:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.7, 'programmed': 6.7}
```
    op hex (4)
    0000   0x01 0x43 0x43 0x00                        .CC.
    decimal
              1   67   67    0
    datetime (2013-01-14T22:36:00)
    0000   0x00 0x64 0x56 0x0e 0x0d                   .dV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 CalForBG 2013-01-14T23:48:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 150}
```
    op hex (2)
    0000   0x0a 0x96                                  ..
    decimal
             10  150
    datetime (2013-01-14T23:48:39)
    0000   0x27 0x70 0x37 0x0e 0x0d                   'p7..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 ResultTotals 2013-02-14T13:13:14 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0xc8                   .....
    decimal
              7    0    0   10  200
    datetime (2013-02-14T13:13:14)
    0000   0x0e 0x8d 0x6d 0x0e 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x11 0x1a 0x46 0xc7 0x19 0x00 0x00    ...F....
    0008   0x0a 0xc8 0x03 0xc6 0x23 0x07 0x02 0x41    ....#..A
    0010   0x00 0x7a 0x07 0x02 0x41 0x01 0x60 0x14    .z..A.`.
    0018   0x05 0xa2 0x50 0x00 0x00 0x00 0x12 0x02    ..P.....
    0020   0x10 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   17   26   70  199   25    0    0
             10  200    3  198   35    7    2   65
              0  122    7    2   65    1   96   20
              5  162   80    0    0    0   18    2
             16    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 CalForBG 2013-01-15T01:20:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-01-15T01:20:10)
    0000   0x0a 0x54 0x21 0x0f 0x0d                   .T!..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 9 PumpSuspend 2013-01-15T14:34:10 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-15T14:34:10)
    0000   0x0a 0x62 0x0e 0x0f 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 PumpResume 2013-01-15T14:54:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-15T14:54:09)
    0000   0x09 0x76 0x0e 0x0f 0x0d                   .v...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 11 CalForBG 2013-01-15T15:57:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-01-15T15:57:04)
    0000   0x04 0x79 0x2f 0x0f 0x0d                   .y/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 12 BolusWizard 2013-01-15T15:57:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 85,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2013-01-15T15:57:16)
    0000   0x10 0x79 0x0f 0x0f 0x0d                   .y...
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0xfb 0x16 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             29   80   13   45  106  251   22  240
              0    0    0   17  125
    HOUR BITS: [0, 1, 1]
#### RECORD 13 Bolus 2013-01-15T15:57:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'programmed': 1.7}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-01-15T15:57:16)
    0000   0x10 0x79 0x4f 0x0f 0x0d                   .yO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 14 CalForBG 2013-01-15T16:02:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-01-15T16:02:29)
    0000   0x1d 0x42 0x30 0x0f 0x0d                   .B0..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 15 BolusWizard 2013-01-15T16:02:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 107,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.8,
 'carb_input': 76,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.7}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-01-15T16:02:43)
    0000   0x2b 0x42 0x10 0x0f 0x0d                   +B...
    body (13)
    hex
    0000   0x4c 0x50 0x0d 0x2d 0x6a 0x00 0x3a 0x00    LP.-j.:.
    0008   0x00 0x11 0x00 0x3a 0x7d                   ...:}
    decimal
             76   80   13   45  106    0   58    0
              0   17    0   58  125
    HOUR BITS: [0, 1, 0]
#### RECORD 16 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 1.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0x08 0x04                   \.D..
    decimal
             92    5   68    8    4
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-01-15T16:02:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.8, 'programmed': 5.8}
```
    op hex (4)
    0000   0x01 0x3a 0x3a 0x00                        .::.
    decimal
              1   58   58    0
    datetime (2013-01-15T16:02:43)
    0000   0x2b 0x42 0x50 0x0f 0x0d                   +BP..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 18 CalForBG 2013-01-15T17:48:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 235}
```
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2013-01-15T17:48:28)
    0000   0x1c 0x70 0x31 0x0f 0x0d                   .p1..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 19 CalForBG 2013-01-15T18:25:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 222}
```
    op hex (2)
    0000   0x0a 0xde                                  ..
    decimal
             10  222
    datetime (2013-01-15T18:25:33)
    0000   0x21 0x59 0x32 0x0f 0x0d                   !Y2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 20 BolusWizard 2013-01-15T18:25:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 222,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.4}
```
    op hex (2)
    0000   0x5b 0xde                                  [.
    decimal
             91  222
    datetime (2013-01-15T18:25:44)
    0000   0x2c 0x59 0x12 0x0f 0x0d                   ,Y...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0   24    0    0  125
    HOUR BITS: [0, 1, 0]
#### RECORD 21 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 141, 'amount': 3.95, 'curve': 4},
 {'age': 151, 'amount': 3.55, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x9e 0x8d 0x04 0x8e 0x97 0x04    \.......
    decimal
             92    8  158  141    4  142  151    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-01-15T18:25:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-01-15T18:25:44)
    0000   0x2c 0x59 0x52 0x0f 0x0d                   ,YR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 23 CalForBG 2013-01-15T18:45:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 203}
```
    op hex (2)
    0000   0x0a 0xcb                                  ..
    decimal
             10  203
    datetime (2013-01-15T18:45:59)
    0000   0x3b 0x6d 0x32 0x0f 0x0d                   ;m2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 24 BolusWizard 2013-01-15T18:46:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 203,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.0}
```
    op hex (2)
    0000   0x5b 0xcb                                  [.
    decimal
             91  203
    datetime (2013-01-15T18:46:17)
    0000   0x11 0x6e 0x12 0x0f 0x0d                   .n...
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x11 0x2a 0x00    7P.-j.*.
    0008   0x00 0x14 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106   17   42    0
              0   20    0   42  125
    HOUR BITS: [0, 1, 1]
#### RECORD 25 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 0.3, 'curve': 4},
 {'age': 162, 'amount': 3.95, 'curve': 4},
 {'age': 172, 'amount': 3.55, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x16 0x04 0x9e 0xa2 0x04    \.......
    0008   0x8e 0xac 0x04                             ...
    decimal
             92   11   12   22    4  158  162    4
            142  172    4
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-01-15T18:46:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'programmed': 4.2}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-01-15T18:46:17)
    0000   0x11 0x6e 0x52 0x0f 0x0d                   .nR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 27 ResultTotals 2013-02-15T13:13:15 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x56                   ....V
    decimal
              7    0    0    5   86
    datetime (2013-02-15T13:13:15)
    0000   0x0f 0x8d 0x6d 0x0f 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x9b 0x4c 0xeb 0x06 0x00 0x00    ...L....
    0008   0x05 0x56 0x03 0x76 0x41 0x01 0xe0 0x23    .V.vA..#
    0010   0x00 0xa0 0x01 0xe0 0x23 0x01 0xd4 0x61    ....#..a
    0018   0x00 0x0c 0x03 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  155   76  235    6    0    0
              5   86    3  118   65    1  224   35
              0  160    1  224   35    1  212   97
              0   12    3    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 28 CalForBG 2013-01-16T06:19:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 245}
```
    op hex (2)
    0000   0x0a 0xf5                                  ..
    decimal
             10  245
    datetime (2013-01-16T06:19:00)
    0000   0x00 0x53 0x26 0x10 0x0d                   .S&..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 29 BolusWizard 2013-01-16T06:19:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 245,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xf5                                  [.
    decimal
             91  245
    datetime (2013-01-16T06:19:02)
    0000   0x02 0x53 0x06 0x10 0x0d                   .S...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0    0    0   26  125
    HOUR BITS: [0, 1, 0]
#### RECORD 30 Bolus 2013-01-16T06:19:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-01-16T06:19:02)
    0000   0x02 0x53 0x46 0x10 0x0d                   .SF..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 31 CalForBG 2013-01-16T12:24:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-01-16T12:24:46)
    0000   0x2e 0x58 0x2c 0x10 0x0d                   .X,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 32 BolusWizard 2013-01-16T12:24:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 171,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-01-16T12:24:50)
    0000   0x32 0x58 0x0c 0x10 0x0d                   2X...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 0]
#### RECORD 33 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 114, 'amount': 2.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0x72 0x14                   \.hr.
    decimal
             92    5  104  114   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-01-16T12:24:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-01-16T12:24:51)
    0000   0x33 0x58 0x4c 0x10 0x0d                   3XL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 35 PumpSuspend 2013-01-16T15:50:08 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-16T15:50:08)
    0000   0x08 0x72 0x0f 0x10 0x0d                   .r...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 36 PumpResume 2013-01-16T16:11:19 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-16T16:11:19)
    0000   0x13 0x4b 0x10 0x10 0x0d                   .K...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 CalForBG 2013-01-16T16:29:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2013-01-16T16:29:02)
    0000   0x02 0x5d 0x30 0x10 0x0d                   .]0..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 BolusWizard 2013-01-16T16:29:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 71,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2013-01-16T16:29:23)
    0000   0x17 0x5d 0x10 0x10 0x0d                   .]...
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0xf8 0x14 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             27   80   13   45  106  248   20  240
              0    0    0   12  125
    HOUR BITS: [0, 1, 0]
#### RECORD 39 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 245, 'amount': 1.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0xf5 0x04                   \.0..
    decimal
             92    5   48  245    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-01-16T16:29:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-01-16T16:29:23)
    0000   0x17 0x5d 0x50 0x10 0x0d                   .]P..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 41 CalForBG 2013-01-16T17:46:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-01-16T17:46:01)
    0000   0x01 0x6e 0x31 0x10 0x0d                   .n1..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 42 BolusWizard 2013-01-16T17:46:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 107,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.9}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-01-16T17:46:44)
    0000   0x2c 0x6e 0x11 0x10 0x0d                   ,n...
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    9    0   18  125
    HOUR BITS: [0, 1, 1]
#### RECORD 43 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 1.2, 'curve': 4},
 {'age': 66, 'amount': 1.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x52 0x04 0x30 0x42 0x14    \.0R.0B.
    decimal
             92    8   48   82    4   48   66   20
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-01-16T17:46:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-01-16T17:46:44)
    0000   0x2c 0x6e 0x51 0x10 0x0d                   ,nQ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 45 CalForBG 2013-01-16T20:42:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-01-16T20:42:20)
    0000   0x14 0x6a 0x34 0x10 0x0d                   .j4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 46 BolusWizard 2013-01-16T20:42:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-01-16T20:42:37)
    0000   0x25 0x6a 0x14 0x10 0x0d                   %j...
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xfd 0x18 0xf0     P.-j...
    0008   0x00 0x04 0x00 0x15 0x7d                   ....}
    decimal
             32   80   13   45  106  253   24  240
              0    4    0   21  125
    HOUR BITS: [0, 1, 1]
#### RECORD 47 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 178, 'amount': 1.8, 'curve': 4},
 {'age': 2, 'amount': 1.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0xb2 0x04 0x30 0x02 0x14    \.H..0..
    decimal
             92    8   72  178    4   48    2   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-01-16T20:42:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'programmed': 2.1}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-01-16T20:42:37)
    0000   0x25 0x6a 0x54 0x10 0x0d                   %jT..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 49 ResultTotals 2013-02-16T13:13:16 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xda                   .....
    decimal
              7    0    0    4  218
    datetime (2013-02-16T13:13:16)
    0000   0x10 0x8d 0x6d 0x10 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x89 0x47 0xf5 0x05 0x00 0x00    ...G....
    0008   0x04 0xda 0x03 0x76 0x47 0x01 0x64 0x1d    ...vG.d.
    0010   0x00 0x53 0x01 0x64 0x1d 0x00 0xcc 0x39    .S.d...9
    0018   0x00 0x98 0x2b 0x00 0x00 0x00 0x05 0x03    ..+.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  137   71  245    5    0    0
              4  218    3  118   71    1  100   29
              0   83    1  100   29    0  204   57
              0  152   43    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 50 PumpSuspend 2013-01-17T13:51:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-17T13:51:09)
    0000   0x09 0x73 0x0d 0x11 0x0d                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 51 PumpResume 2013-01-17T14:09:56 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-17T14:09:56)
    0000   0x38 0x49 0x0e 0x11 0x0d                   8I...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 52 CalForBG 2013-01-17T16:59:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-01-17T16:59:39)
    0000   0x27 0x7b 0x30 0x11 0x0d                   '{0..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 53 BolusWizard 2013-01-17T16:59:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 8,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-01-17T16:59:46)
    0000   0x2e 0x7b 0x10 0x11 0x0d                   .{...
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0xfc 0x06 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x02 0x7d                   ....}
    decimal
              8   80   13   45  106  252    6  240
              0    0    0    2  125
    HOUR BITS: [0, 1, 1]
#### RECORD 54 Bolus 2013-01-17T16:59:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'programmed': 0.2}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-01-17T16:59:46)
    0000   0x2e 0x7b 0x50 0x11 0x0d                   .{P..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 55 LowReservoir 2013-01-17T17:12:37 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-01-17T17:12:37)
    0000   0x25 0x4c 0x11 0x11 0x0d                   %L...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 56 CalForBG 2013-01-17T18:09:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 237}
```
    op hex (2)
    0000   0x0a 0xed                                  ..
    decimal
             10  237
    datetime (2013-01-17T18:09:19)
    0000   0x13 0x49 0x32 0x11 0x0d                   .I2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 BolusWizard 2013-01-17T18:09:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 237,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0xed                                  [.
    decimal
             91  237
    datetime (2013-01-17T18:09:39)
    0000   0x27 0x49 0x12 0x11 0x0d                   'I...
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0x18 0x28 0x00    5P.-j.(.
    0008   0x00 0x02 0x00 0x3e 0x7d                   ...>}
    decimal
             53   80   13   45  106   24   40    0
              0    2    0   62  125
    HOUR BITS: [0, 1, 0]
#### RECORD 58 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 75, 'amount': 0.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x08 0x4b 0x04                   \..K.
    decimal
             92    5    8   75    4
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-01-17T18:09:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2, 'programmed': 6.2}
```
    op hex (4)
    0000   0x01 0x3e 0x3e 0x00                        .>>.
    decimal
              1   62   62    0
    datetime (2013-01-17T18:09:39)
    0000   0x27 0x49 0x52 0x11 0x0d                   'IR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 60 BolusWizard 2013-01-17T19:05:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 30,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-01-17T19:05:21)
    0000   0x15 0x45 0x13 0x11 0x0d                   .E...
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [0, 1, 0]
#### RECORD 61 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 6.2, 'curve': 4},
 {'age': 131, 'amount': 0.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xf8 0x3d 0x04 0x08 0x83 0x04    \..=....
    decimal
             92    8  248   61    4    8  131    4
    datetime (unknown)

    body (0)

#### RECORD 62 LowReservoir 2013-01-17T19:06:41 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-01-17T19:06:41)
    0000   0x29 0x46 0x13 0x11 0x0d                   )F...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 63 Bolus 2013-01-17T19:05:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-01-17T19:05:21)
    0000   0x15 0x45 0x53 0x11 0x0d                   .ES..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 64 ResultTotals 2013-02-17T13:13:17 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime (2013-02-17T13:13:17)
    0000   0x11 0x8d 0x6d 0x11 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xa3 0x58 0xed 0x02 0x00 0x00    ...X....
    0008   0x04 0xd2 0x03 0x76 0x48 0x01 0x5c 0x1c    ...vH.\.
    0010   0x00 0x5b 0x01 0x5c 0x1c 0x01 0x04 0x4b    .[.\...K
    0018   0x00 0x58 0x19 0x00 0x00 0x00 0x03 0x02    .X......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  163   88  237    2    0    0
              4  210    3  118   72    1   92   28
              0   91    1   92   28    1    4   75
              0   88   25    0    0    0    3    2
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 65 PumpSuspend 2013-01-18T14:31:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-18T14:31:19)
    0000   0x13 0x5f 0x0e 0x12 0x0d                   ._...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 66 PumpResume 2013-01-18T15:11:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-18T15:11:31)
    0000   0x1f 0x4b 0x0f 0x12 0x0d                   .K...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 67 CalForBG 2013-01-18T15:36:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2013-01-18T15:36:48)
    0000   0x30 0x64 0x2f 0x12 0x0d                   0d/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 68 BolusWizard 2013-01-18T15:37:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 142,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 26,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2013-01-18T15:37:04)
    0000   0x04 0x65 0x0f 0x12 0x0d                   .e...
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x03 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             26   80   13   45  106    3   20    0
              0    0    0   23  125
    HOUR BITS: [0, 1, 1]
#### RECORD 69 Bolus 2013-01-18T15:37:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-01-18T15:37:04)
    0000   0x04 0x65 0x4f 0x12 0x0d                   .eO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 70 Rewind 2013-01-18T18:53:14 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-01-18T18:53:14)
    0000   0x0e 0x75 0x12 0x12 0x0d                   .u...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 71 Prime 2013-01-18T18:55:41 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x29                   ....)
    decimal
              3    0    0    0   41
    datetime (2013-01-18T18:55:41)
    0000   0x29 0x77 0x32 0x12 0x0d                   )w2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 72 Prime 2013-01-18T18:56:00 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-01-18T18:56:00)
    0000   0x00 0x78 0x12 0x12 0x0d                   .x...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 73 CalForBG 2013-01-18T19:07:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-01-18T19:07:12)
    0000   0x0c 0x47 0x33 0x12 0x0d                   .G3..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 74 BolusWizard 2013-01-18T19:08:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-01-18T19:08:03)
    0000   0x03 0x48 0x13 0x12 0x0d                   .H...
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0xfc 0x24 0xf0    /P.-j.$.
    0008   0x00 0x02 0x00 0x20 0x7d                   ... }
    decimal
             47   80   13   45  106  252   36  240
              0    2    0   32  125
    HOUR BITS: [0, 1, 0]
#### RECORD 75 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 214, 'amount': 2.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0xd6 0x04                   \.\..
    decimal
             92    5   92  214    4
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2013-01-18T19:08:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-01-18T19:08:03)
    0000   0x03 0x48 0x53 0x12 0x0d                   .HS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 77 BolusWizard 2013-01-18T20:10:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-01-18T20:10:52)
    0000   0x34 0x4a 0x14 0x12 0x0d                   4J...
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [0, 1, 0]
#### RECORD 78 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 3.2, 'curve': 4},
 {'age': 20, 'amount': 2.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x80 0x42 0x04 0x5c 0x14 0x14    \..B.\..
    decimal
             92    8  128   66    4   92   20   20
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2013-01-18T20:10:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-01-18T20:10:52)
    0000   0x34 0x4a 0x54 0x12 0x0d                   4JT..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 80 ResultTotals (2000, 2, 0, 0, 13, 18) head[5], body[14] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x78                   ....x
    decimal
              7    0    0    4  120
    datetime ((2000, 2, 0, 0, 13, 18))
    0000   0x12 0x8d 0x00 0x00 0x00                   .....
    body (14)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x2c 0xf3              ....,.
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0   44  243
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-1.data: 81 records`
