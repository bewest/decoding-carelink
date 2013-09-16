## START logs/ReadHistoryData-page-10.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x27 0x15                                  '.
##### DEBUG DECIMAL
             39   21
#### RECORD 0 BolusWizard 2013-06-19T21:03:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 245,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf5                                  [.
    decimal
             91  245
    datetime (2013-06-19T21:03:42)
    0000   0x6a 0x83 0x15 0x13 0x0d                   j....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x02 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0   24    0    2  125
    HOUR BITS: [1, 0, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 1.9, 'curve': 4},
 {'age': 69, 'amount': 1.0, 'curve': 4},
 {'age': 63, 'amount': 0.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0x3b 0x04 0x28 0x45 0x04    \.L;.(E.
    0008   0x20 0x3f 0x14                              ?.
    decimal
             92   11   76   59    4   40   69    4
             32   63   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-06-19T21:03:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-06-19T21:03:42)
    0000   0x6a 0x83 0x55 0x13 0x0d                   j.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 BolusWizard 2013-06-19T21:28:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-06-19T21:28:31)
    0000   0x5f 0x9c 0x15 0x13 0x0d                   _....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 0]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 0.05, 'curve': 4},
 {'age': 34, 'amount': 0.45, 'curve': 4},
 {'age': 84, 'amount': 1.9, 'curve': 4},
 {'age': 94, 'amount': 1.0, 'curve': 4},
 {'age': 88, 'amount': 0.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x02 0x18 0x04 0x12 0x22 0x04    \.....".
    0008   0x4c 0x54 0x04 0x28 0x5e 0x04 0x20 0x58    LT.(^. X
    0010   0x14                                       .
    decimal
             92   17    2   24    4   18   34    4
             76   84    4   40   94    4   32   88
             20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-06-19T21:28:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-06-19T21:28:31)
    0000   0x5f 0x9c 0x55 0x13 0x0d                   _.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 CalBGForPH 2013-06-19T21:38:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2013-06-19T21:38:27)
    0000   0x5b 0xa6 0x35 0x13 0x0d                   [.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 7 CalBGForPH 2013-06-19T22:11:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 252}
```
    op hex (2)
    0000   0x0a 0xfc                                  ..
    decimal
             10  252
    datetime (2013-06-19T22:11:47)
    0000   0x6f 0x8b 0x36 0x13 0x0d                   o.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 BolusWizard 2013-06-19T22:12:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 252,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfc                                  [.
    decimal
             91  252
    datetime (2013-06-19T22:12:48)
    0000   0x70 0x8c 0x16 0x13 0x0d                   p....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x1c 0x2e 0x00    <P.-j...
    0008   0x00 0x1e 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106   28   46    0
              0   30    0   46  125
    HOUR BITS: [1, 0, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 1.7, 'curve': 4},
 {'age': 68, 'amount': 0.05, 'curve': 4},
 {'age': 78, 'amount': 0.45, 'curve': 4},
 {'age': 128, 'amount': 1.9, 'curve': 4},
 {'age': 138, 'amount': 1.0, 'curve': 4},
 {'age': 132, 'amount': 0.8, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x44 0x30 0x04 0x02 0x44 0x04    \.D0..D.
    0008   0x12 0x4e 0x04 0x4c 0x80 0x04 0x28 0x8a    .N.L..(.
    0010   0x04 0x20 0x84 0x14                        . ..
    decimal
             92   20   68   48    4    2   68    4
             18   78    4   76  128    4   40  138
              4   32  132   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-06-19T22:12:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-06-19T22:12:49)
    0000   0x71 0x8c 0x56 0x13 0x0d                   q.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 CalBGForPH 2013-06-19T22:41:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 241}
```
    op hex (2)
    0000   0x0a 0xf1                                  ..
    decimal
             10  241
    datetime (2013-06-19T22:41:16)
    0000   0x50 0xa9 0x36 0x13 0x0d                   P.6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 ResultTotals 2013-04-19T13:13:51 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x88                   .....
    decimal
              7    0    0    4  136
    datetime (2013-04-19T13:13:51)
    0000   0x73 0x0d 0x6d 0x73 0x0d                   s.ms.
    body (51)
    hex
    0000   0x05 0x10 0xcb 0x4c 0x03 0x07 0x00 0x00    ...L....
    0008   0x04 0x88 0x02 0xe4 0x40 0x01 0xa4 0x24    ....@..$
    0010   0x00 0x67 0x01 0xa4 0x24 0x01 0x1c 0x44    .g..$..D
    0018   0x00 0x88 0x20 0x00 0x00 0x00 0x05 0x03    .. .....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x4b 0xb2 0x0b 0x14 0x0d    ...K....
    0030   0x1f 0x00 0x47                             ..G
    decimal
              5   16  203   76    3    7    0    0
              4  136    2  228   64    1  164   36
              0  103    1  164   36    1   28   68
              0  136   32    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0   30    0   75  178   11   20   13
             31    0   71
    DAY BITS: [0, 1, 1]
#### RECORD 13 Base (2004, 0, 5, 10, 13, 20) head[2], body[0] op[0x8f]

    op hex (2)
    0000   0x8f 0x0c                                  ..
    decimal
            143   12
    datetime ((2004, 0, 5, 10, 13, 20))
    0000   0x14 0x0d 0x0a 0xa5 0x44                   ....D
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 14 Base (2008, 0, 5, 27, 13, 20) head[2], body[0] op[0x9d]

    op hex (2)
    0000   0x9d 0x2c                                  .,
    decimal
            157   44
    datetime ((2008, 0, 5, 27, 13, 20))
    0000   0x14 0x0d 0x5b 0xa5 0x48                   ..[.H
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 15 Base (2013, 0, 16, 0, 13, 20) head[2], body[0] op[0x9d]

    op hex (2)
    0000   0x9d 0x0c                                  ..
    decimal
            157   12
    datetime ((2013, 0, 16, 0, 13, 20))
    0000   0x14 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 16 Base (2000, 0, 0, 0, 0, 8) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 8))
    0000   0x08 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 17 Base (2000, 4, 8, 8, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 4, 8, 8, 1, 61))
    0000   0x7d 0x01 0x08 0x08 0x00                   }....
    body (0)

#### RECORD 18 Base (2012, 4, 10, 13, 20, 12) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x9d                                  H.
    decimal
             72  157
    datetime ((2012, 4, 10, 13, 20, 12))
    0000   0x4c 0x14 0x0d 0x0a 0x9c                   L....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 19 Base (2012, 0, 27, 13, 20, 45) head[2], body[0] op[0x77]

    op hex (2)
    0000   0x77 0x85                                  w.
    decimal
            119  133
    datetime ((2012, 0, 27, 13, 20, 45))
    0000   0x2d 0x14 0x0d 0x5b 0x9c                   -..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 20 Base (2000, 0, 22, 13, 20, 13) head[2], body[0] op[0x4b]

    op hex (2)
    0000   0x4b 0x86                                  K.
    decimal
             75  134
    datetime ((2000, 0, 22, 13, 20, 13))
    0000   0x0d 0x14 0x0d 0x36 0x50                   ...6P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 21 Base (2000, 4, 0, 9, 6, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 9, 6, 42))
    0000   0x6a 0x06 0x29 0x00 0x00                   j.)..
    body (0)

#### RECORD 22 ChangeBasalProfile (2000, 1, 5, 28, 61, 41) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x00                                  ..
    decimal
              8    0
    datetime ((2000, 1, 5, 28, 61, 41))
    0000   0x29 0x7d 0x5c 0x05 0x20                   )}\. 
    body (44)
    hex
    0000   0x2a 0x04 0x01 0x29 0x29 0x00 0x4b 0x86    *..)).K.
    0008   0x4d 0x14 0x0d 0x0a 0xd1 0x71 0x8a 0x2f    M....q./
    0010   0x14 0x0d 0x5b 0xd1 0x76 0x8a 0x0f 0x14    ..[.v...
    0018   0x0d 0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00    ..P.-j..
    0020   0x00 0x00 0x14 0x00 0x00 0x7d 0x5c 0x08    .....}\.
    0028   0xa4 0x7e 0x04 0x20                        .~. 
    decimal
             42    4    1   41   41    0   75  134
             77   20   13   10  209  113  138   47
             20   13   91  209  118  138   15   20
             13    0   80   13   45  106   18    0
              0    0   20    0    0  125   92    8
            164  126    4   32
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 23 Base (2006, 0, 0, 3, 3, 1) head[2], body[0] op[0xa6]

    op hex (2)
    0000   0xa6 0x04                                  ..
    decimal
            166    4
    datetime ((2006, 0, 0, 3, 3, 1))
    0000   0x01 0x03 0x03 0x00 0x76                   ....v
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 24 Base (2011, 0, 25, 10, 13, 20) head[2], body[0] op[0x8a]

    op hex (2)
    0000   0x8a 0x4f                                  .O
    decimal
            138   79
    datetime ((2011, 0, 25, 10, 13, 20))
    0000   0x14 0x0d 0x0a 0xd9 0x5b                   ....[
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 25 Base (2015, 0, 25, 27, 13, 20) head[2], body[0] op[0xa5]

    op hex (2)
    0000   0xa5 0x30                                  .0
    decimal
            165   48
    datetime ((2015, 0, 25, 27, 13, 20))
    0000   0x14 0x0d 0x5b 0xd9 0x5f                   ..[._
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 26 Base (2013, 0, 16, 0, 13, 20) head[2], body[0] op[0xa5]

    op hex (2)
    0000   0xa5 0x10                                  ..
    decimal
            165   16
    datetime ((2013, 0, 16, 0, 13, 20))
    0000   0x14 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 27 Base (2006, 0, 0, 0, 0, 20) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2006, 0, 0, 0, 0, 20))
    0000   0x14 0x00 0x00 0x00 0x06                   .....
    body (0)

#### RECORD 28 Base (2013, 5, 12, 11, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0e                                  ..
    decimal
              0   14
    datetime ((2013, 5, 12, 11, 28, 61))
    0000   0x7d 0x5c 0x0b 0x0c 0x5d                   }\..]
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 29 Base (2004, 12, 29, 0, 4, 21) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0xa4                                  ..
    decimal
              4  164
    datetime ((2004, 12, 29, 0, 4, 21))
    0000   0xd5 0x04 0x20 0xfd 0x04                   .. ..
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 30 Bolus 2013-06-20T16:37:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-06-20T16:37:31)
    0000   0x5f 0xa5 0x50 0x14 0x0d                   _.P..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 31 CalBGForPH 2013-06-20T17:38:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-06-20T17:38:40)
    0000   0x68 0xa6 0x31 0x14 0x0d                   h.1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 32 CalBGForPH 2013-06-20T18:54:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-06-20T18:54:41)
    0000   0x69 0xb6 0x32 0x14 0x0d                   i.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 BolusWizard 2013-06-20T18:55:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2013-06-20T18:55:03)
    0000   0x43 0xb7 0x12 0x14 0x0d                   C....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xfa 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x06 0x00 0x24 0x7d                   ...$}
    decimal
             55   80   13   45  106  250   42  240
              0    6    0   36  125
    HOUR BITS: [1, 0, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 141, 'amount': 1.6, 'curve': 4},
 {'age': 231, 'amount': 0.3, 'curve': 4},
 {'age': 95, 'amount': 4.1, 'curve': 20},
 {'age': 135, 'amount': 0.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x40 0x8d 0x04 0x0c 0xe7 0x04    \.@.....
    0008   0xa4 0x5f 0x14 0x20 0x87 0x14              ._. ..
    decimal
             92   14   64  141    4   12  231    4
            164   95   20   32  135   20
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-06-20T18:55:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-06-20T18:55:03)
    0000   0x43 0xb7 0x52 0x14 0x0d                   C.R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 LowReservoir 2013-06-20T23:56:50 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-06-20T23:56:50)
    0000   0x72 0xb8 0x17 0x14 0x0d                   r....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 37 ResultTotals 2013-04-20T13:13:52 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x12                   .....
    decimal
              7    0    0    5   18
    datetime (2013-04-20T13:13:52)
    0000   0x74 0x0d 0x6d 0x74 0x0d                   t.mt.
    body (51)
    hex
    0000   0x05 0x00 0x99 0x50 0xd9 0x06 0x00 0x00    ...P....
    0008   0x05 0x12 0x03 0x72 0x44 0x01 0xa0 0x20    ...rD.. 
    0010   0x00 0x6d 0x01 0xa0 0x20 0x01 0x34 0x4a    .m.. .4J
    0018   0x00 0x6c 0x1a 0x00 0x00 0x00 0x05 0x02    .l......
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x34 0x64 0x66 0x8d 0x0b 0x15 0x0d    .4df....
    0030   0x1e 0x00 0x7a                             ..z
    decimal
              5    0  153   80  217    6    0    0
              5   18    3  114   68    1  160   32
              0  109    1  160   32    1   52   74
              0  108   26    0    0    0    5    2
              3    0    0   12    0  232    0    0
              0   52  100  102  141   11   21   13
             30    0  122
    DAY BITS: [0, 1, 1]
#### RECORD 38 Base (2008, 0, 0, 31, 13, 21) head[2], body[0] op[0xaf]

    op hex (2)
    0000   0xaf 0x0e                                  ..
    decimal
            175   14
    datetime ((2008, 0, 0, 31, 13, 21))
    0000   0x15 0x0d 0x1f 0x00 0x58                   ....X
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 39 Base (2009, 0, 22, 10, 13, 21) head[2], body[0] op[0x83]

    op hex (2)
    0000   0x83 0x0f                                  ..
    decimal
            131   15
    datetime ((2009, 0, 22, 10, 13, 21))
    0000   0x15 0x0d 0x0a 0x56 0x49                   ...VI
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 40 Base (2012, 0, 22, 27, 13, 21) head[2], body[0] op[0x9c]

    op hex (2)
    0000   0x9c 0x30                                  .0
    decimal
            156   48
    datetime ((2012, 0, 22, 27, 13, 21))
    0000   0x15 0x0d 0x5b 0x56 0x5c                   ..[V\
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 41 Base (2013, 0, 16, 21, 13, 21) head[2], body[0] op[0x9c]

    op hex (2)
    0000   0x9c 0x10                                  ..
    decimal
            156   16
    datetime ((2013, 0, 16, 21, 13, 21))
    0000   0x15 0x0d 0x35 0x50 0x0d                   ..5P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 42 Base (2000, 12, 0, 16, 40, 59) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 40, 59))
    0000   0xfb 0x28 0xf0 0x00 0x00                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 Base (2000, 4, 3, 3, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x23                                  .#
    decimal
              0   35
    datetime ((2000, 4, 3, 3, 1, 61))
    0000   0x7d 0x01 0x23 0x23 0x00                   }.##.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[156], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 2.0, 'curve': 13},
 {'age': 0, 'amount': 0.825, 'curve': 119},
 {'age': 17, 'amount': 4.375, 'curve': 21},
 {'age': 3, 'amount': 0.325, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 17},
 {'age': 177, 'amount': 1.975, 'curve': 49},
 {'age': 13, 'amount': 0.525, 'curve': 3},
 {'age': 5, 'amount': 0.0, 'curve': 0},
 {'age': 95, 'amount': 0.125, 'curve': 177},
 {'age': 21, 'amount': 0.425, 'curve': 13},
 {'age': 204, 'amount': 0.25, 'curve': 80},
 {'age': 49, 'amount': 4.525, 'curve': 21},
 {'age': 10, 'amount': 0.325, 'curve': 162},
 {'age': 179, 'amount': 3.025, 'curve': 50},
 {'age': 13, 'amount': 0.525, 'curve': 91},
 {'age': 74, 'amount': 4.05, 'curve': 180},
 {'age': 21, 'amount': 0.45, 'curve': 13},
 {'age': 80, 'amount': 1.75, 'curve': 13},
 {'age': 106, 'amount': 1.125, 'curve': 8},
 {'age': 0, 'amount': 1.325, 'curve': 0},
 {'age': 0, 'amount': 0.275, 'curve': 53},
 {'age': 92, 'amount': 3.125, 'curve': 5},
 {'age': 148, 'amount': 3.5, 'curve': 4},
 {'age': 53, 'amount': 0.025, 'curve': 53},
 {'age': 75, 'amount': 0.0, 'curve': 180},
 {'age': 21, 'amount': 2.05, 'curve': 13},
 {'age': 0, 'amount': 0.175, 'curve': 0},
 {'age': 218, 'amount': 0.1, 'curve': 117},
 {'age': 109, 'amount': 0.325, 'curve': 117},
 {'age': 5, 'amount': 0.325, 'curve': 0},
 {'age': 86, 'amount': 3.775, 'curve': 204},
 {'age': 0, 'amount': 0.075, 'curve': 0},
 {'age': 218, 'amount': 0.1, 'curve': 3},
 {'age': 72, 'amount': 3.05, 'curve': 1},
 {'age': 28, 'amount': 2.4, 'curve': 0},
 {'age': 1, 'amount': 3.075, 'curve': 96},
 {'age': 1, 'amount': 0.7, 'curve': 96},
 {'age': 0, 'amount': 2.5, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 2, 'amount': 0.0, 'curve': 2},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.3, 'curve': 232},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 82, 'amount': 0.25, 'curve': 64},
 {'age': 45, 'amount': 4.625, 'curve': 22},
 {'age': 91, 'amount': 0.325, 'curve': 82},
 {'age': 185, 'amount': 2.4, 'curve': 13},
 {'age': 13, 'amount': 0.55, 'curve': 65},
 {'age': 13, 'amount': 2.0, 'curve': 45},
 {'age': 250, 'amount': 2.65, 'curve': 50},
 {'age': 0, 'amount': 6.0, 'curve': 0}]
```
    op hex (156)
    0000   0x5c 0x9c 0x50 0x15 0x0d 0x21 0x00 0x77    \.P..!.w
    0008   0xaf 0x11 0x15 0x0d 0x03 0x00 0x00 0x00    ........
    0010   0x11 0x4f 0xb1 0x31 0x15 0x0d 0x03 0x00    .O.1....
    0018   0x05 0x00 0x05 0x5f 0xb1 0x11 0x15 0x0d    ..._....
    0020   0x0a 0xcc 0x50 0xb5 0x31 0x15 0x0d 0x0a    ..P.1...
    0028   0xa2 0x79 0xb3 0x32 0x15 0x0d 0x5b 0xa2    .y.2..[.
    0030   0x4a 0xb4 0x12 0x15 0x0d 0x46 0x50 0x0d    J....FP.
    0038   0x2d 0x6a 0x08 0x35 0x00 0x00 0x0b 0x00    -j.5....
    0040   0x35 0x7d 0x5c 0x05 0x8c 0x94 0x04 0x01    5}\.....
    0048   0x35 0x35 0x00 0x4b 0xb4 0x52 0x15 0x0d    55.K.R..
    0050   0x07 0x00 0x00 0x04 0xda 0x75 0x0d 0x6d    .....u.m
    0058   0x75 0x0d 0x05 0x00 0x97 0x56 0xcc 0x03    u....V..
    0060   0x00 0x00 0x04 0xda 0x03 0x7a 0x48 0x01    .....zH.
    0068   0x60 0x1c 0x00 0x7b 0x01 0x60 0x1c 0x01    `..{.`..
    0070   0x60 0x64 0x00 0x00 0x00 0x00 0x00 0x00    `d......
    0078   0x02 0x02 0x00 0x00 0x00 0x0c 0x00 0xe8    ........
    0080   0x00 0x00 0x00 0x0a 0x52 0x40 0xb9 0x2d    ....R@.-
    0088   0x16 0x0d 0x5b 0x52 0x60 0xb9 0x0d 0x16    ..[R`...
    0090   0x0d 0x41 0x50 0x0d 0x2d 0x6a 0xfa 0x32    .AP.-j.2
    0098   0xf0 0x00 0x00 0x00                        ....
    decimal
             92  156   80   21   13   33    0  119
            175   17   21   13    3    0    0    0
             17   79  177   49   21   13    3    0
              5    0    5   95  177   17   21   13
             10  204   80  181   49   21   13   10
            162  121  179   50   21   13   91  162
             74  180   18   21   13   70   80   13
             45  106    8   53    0    0   11    0
             53  125   92    5  140  148    4    1
             53   53    0   75  180   82   21   13
              7    0    0    4  218  117   13  109
            117   13    5    0  151   86  204    3
              0    0    4  218    3  122   72    1
             96   28    0  123    1   96   28    1
             96  100    0    0    0    0    0    0
              2    2    0    0    0   12    0  232
              0    0    0   10   82   64  185   45
             22   13   91   82   96  185   13   22
             13   65   80   13   45  106  250   50
            240    0    0    0
    datetime (unknown)

    body (0)

#### RECORD 45 Base (2000, 0, 0, 12, 44, 1) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x7d                                  ,}
    decimal
             44  125
    datetime ((2000, 0, 0, 12, 44, 1))
    0000   0x01 0x2c 0x2c 0x00 0x60                   .,,.`
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 46 Base (2012, 0, 10, 10, 13, 22) head[2], body[0] op[0xb9]

    op hex (2)
    0000   0xb9 0x4d                                  .M
    decimal
            185   77
    datetime ((2012, 0, 10, 10, 13, 22))
    0000   0x16 0x0d 0x0a 0x6a 0x5c                   ...j\
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 47 Base (2000, 2, 10, 27, 13, 22) head[2], body[0] op[0xaf]

    op hex (2)
    0000   0xaf 0x33                                  .3
    decimal
            175   51
    datetime ((2000, 2, 10, 27, 13, 22))
    0000   0x16 0x8d 0x5b 0x6a 0x60                   ..[j`
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 48 Base (2013, 0, 17, 0, 13, 22) head[2], body[0] op[0xaf]

    op hex (2)
    0000   0xaf 0x13                                  ..
    decimal
            175   19
    datetime ((2013, 0, 17, 0, 13, 22))
    0000   0x16 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 49 Base (2000, 0, 0, 0, 0, 52) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 52))
    0000   0x34 0x00 0x00 0x00 0x00                   4....
    body (0)

#### RECORD 50 Base (2001, 5, 16, 5, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x34                                  .4
    decimal
              0   52
    datetime ((2001, 5, 16, 5, 28, 61))
    0000   0x7d 0x5c 0x05 0xb0 0x61                   }\..a
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 51 SelectBasalProfile (2015, 0, 0, 0, 54, 54) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x01                                  ..
    decimal
             20    1
    datetime ((2015, 0, 0, 0, 54, 54))
    0000   0x36 0x36 0x00 0x60 0xaf                   66.`.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 52 Base (2014, 0, 21, 5, 10, 13) head[2], body[0] op[0x53]

    op hex (2)
    0000   0x53 0x16                                  S.
    decimal
             83   22
    datetime ((2014, 0, 21, 5, 10, 13))
    0000   0x0d 0x0a 0xa5 0x75 0xae                   ...u.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 53 Base (2002, 0, 4, 14, 10, 13) head[2], body[0] op[0x35]

    op hex (2)
    0000   0x35 0x16                                  5.
    decimal
             53   22
    datetime ((2002, 0, 4, 14, 10, 13))
    0000   0x0d 0x0a 0x8e 0x44 0xa2                   ...D.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 54 Base (2002, 1, 15, 14, 27, 13) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x16                                  6.
    decimal
             54   22
    datetime ((2002, 1, 15, 14, 27, 13))
    0000   0x0d 0x5b 0x8e 0x6f 0xa2                   .[.o.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 55 TempBasalDuration (2013, 0, 13, 16, 51, 13) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 660}
```
    op hex (2)
    0000   0x16 0x16                                  ..
    decimal
             22   22
    datetime ((2013, 0, 13, 16, 51, 13))
    0000   0x0d 0x33 0x50 0x0d 0x2d                   .3P.-
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 56 Base (2000, 0, 12, 0, 0, 39) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x03                                  j.
    decimal
            106    3
    datetime ((2000, 0, 12, 0, 0, 39))
    0000   0x27 0x00 0x00 0x0c 0x00                   '....
    body (0)

#### RECORD 57 ChangeRemoteID (2004, 4, 10, 24, 5, 28) head[2], body[0] op[0x27]

    op hex (2)
    0000   0x27 0x7d                                  '}
    decimal
             39  125
    datetime ((2004, 4, 10, 24, 5, 28))
    0000   0x5c 0x05 0xd8 0xaa 0x04                   \....
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 58 Bolus 2013-06-22T22:34:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-06-22T22:34:47)
    0000   0x6f 0xa2 0x56 0x16 0x0d                   o.V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 59 BolusWizard 2013-06-22T22:58:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-06-22T22:58:55)
    0000   0x77 0xba 0x16 0x16 0x0d                   w....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 3.9, 'curve': 4},
 {'age': 194, 'amount': 5.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x9c 0x18 0x04 0xd8 0xc2 0x04    \.......
    decimal
             92    8  156   24    4  216  194    4
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-06-22T22:58:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-06-22T22:58:55)
    0000   0x77 0xba 0x56 0x16 0x0d                   w.V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 62 ResultTotals 2013-04-22T13:13:54 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xec                   .....
    decimal
              7    0    0    5  236
    datetime (2013-04-22T13:13:54)
    0000   0x76 0x0d 0x6d 0x76 0x0d                   v.mv.
    body (51)
    hex
    0000   0x05 0x10 0xbc 0x52 0x6a 0x04 0x00 0x00    ...Rj...
    0008   0x05 0xec 0x03 0x84 0x3b 0x02 0x68 0x29    ....;.h)
    0010   0x00 0x8b 0x02 0x68 0x29 0x01 0x90 0x41    ...h)..A
    0018   0x00 0xd8 0x23 0x00 0x00 0x00 0x04 0x03    ..#.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x86 0x6a 0x90 0x21 0x17 0x0d    ...j.!..
    0030   0x0a 0xa3 0x48                             ..H
    decimal
              5   16  188   82  106    4    0    0
              5  236    3  132   59    2  104   41
              0  139    2  104   41    1  144   65
              0  216   35    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0   10  134  106  144   33   23   13
             10  163   72
    DAY BITS: [0, 1, 1]
#### RECORD 63 Base (2012, 2, 3, 27, 13, 23) head[2], body[0] op[0xb3]

    op hex (2)
    0000   0xb3 0x27                                  .'
    decimal
            179   39
    datetime ((2012, 2, 3, 27, 13, 23))
    0000   0x17 0x8d 0x5b 0xa3 0x4c                   ..[.L
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 64 Base (2013, 0, 17, 0, 13, 23) head[2], body[0] op[0xb3]

    op hex (2)
    0000   0xb3 0x07                                  ..
    decimal
            179    7
    datetime ((2013, 0, 17, 0, 13, 23))
    0000   0x17 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 65 Base (2000, 4, 0, 0, 0, 1) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 4, 0, 0, 0, 1))
    0000   0x41 0x00 0x00 0x00 0x00                   A....
    body (0)

#### RECORD 66 Base (2000, 4, 2, 2, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x41                                  .A
    decimal
              0   65
    datetime ((2000, 4, 2, 2, 1, 61))
    0000   0x7d 0x01 0x42 0x42 0x00                   }.BB.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 67 Base (2000, 4, 30, 13, 23, 7) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0xb3                                  L.
    decimal
             76  179
    datetime ((2000, 4, 30, 13, 23, 7))
    0000   0x47 0x17 0x0d 0x1e 0x00                   G....
    body (0)

#### RECORD 68 Base (2000, 0, 31, 13, 23, 9) head[2], body[0] op[0x6b]

    op hex (2)
    0000   0x6b 0x9c                                  k.
    decimal
            107  156
    datetime ((2000, 0, 31, 13, 23, 9))
    0000   0x09 0x17 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 69 Base (2006, 0, 10, 13, 23, 10) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x87                                  H.
    decimal
             72  135
    datetime ((2006, 0, 10, 13, 23, 10))
    0000   0x0a 0x17 0x0d 0x0a 0xf6                   .....
    body (0)
    YEAR BITS: [1, 1, 1, 1]
#### RECORD 70 Base (2006, 0, 27, 13, 23, 42) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0xb6                                  r.
    decimal
            114  182
    datetime ((2006, 0, 27, 13, 23, 42))
    0000   0x2a 0x17 0x0d 0x5b 0xf6                   *..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 71 Base (2000, 0, 0, 13, 23, 10) head[2], body[0] op[0x7a]

    op hex (2)
    0000   0x7a 0xb6                                  z.
    decimal
            122  182
    datetime ((2000, 0, 0, 13, 23, 10))
    0000   0x0a 0x17 0x0d 0x00 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 72 Base (2000, 4, 0, 0, 26, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 26, 42))
    0000   0x6a 0x1a 0x00 0x00 0x00                   j....
    body (0)

#### RECORD 73 Ian0B (2004, 5, 2, 8, 28, 61) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x00 0x0f                             ...
    decimal
             11    0   15
    datetime ((2004, 5, 2, 8, 28, 61))
    0000   0x7d 0x5c 0x08 0x62 0xb4                   }\.b.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 74 Base (2015, 8, 15, 1, 4, 62) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0xa6                                  ..
    decimal
              4  166
    datetime ((2015, 8, 15, 1, 4, 62))
    0000   0xbe 0x04 0x01 0x0f 0x0f                   .....
    body (0)

#### RECORD 75 Base (2010, 9, 13, 23, 10, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7a                                  .z
    decimal
              0  122
    datetime ((2010, 9, 13, 23, 10, 54))
    0000   0xb6 0x4a 0x17 0x0d 0x0a                   .J...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 76 BasalProfileStart 2010-08-13T23:44:56 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x66                                  {f
    decimal
            123  102
    datetime (2010-08-13T23:44:56)
    0000   0xb8 0x2c 0x17 0x0d 0x0a                   .,...
    body (3)
    hex
    0000   0x6d 0x6d 0xb8                             mm.
    decimal
            109  109  184
    HOUR BITS: [0, 0, 1]
#### RECORD 77 Base (2000, 0, 0, 0, 0, 13) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x17                                  ,.
    decimal
             44   23
    datetime ((2000, 0, 0, 0, 0, 13))
    0000   0x0d 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-10.data: 78 records`
