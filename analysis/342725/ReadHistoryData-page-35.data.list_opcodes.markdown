## START logs/ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 375, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x05 0x6e 0x03 0x76 0x40 0x01 0xf8 0x24    .n.v@..$
    0008   0x00 0x6b 0x01 0xf8 0x24 0x01 0x34 0x3d    .k..$.4=
    0010   0x00 0xc4 0x27 0x00 0x00 0x00 0x04 0x03    ..'.....
    0018   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
##### DEBUG DECIMAL
              5  110    3  118   64    1  248   36
              0  107    1  248   36    1   52   61
              0  196   39    0    0    0    4    3
              1    0    0   12    0  232    0    0
#### RECORD 0 CalBGForPH 2013-03-16T18:46:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-16T18:46:24)
    0000   0x18 0xee 0x32 0x10 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 PumpSuspend 2013-03-16T18:48:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-16T18:48:44)
    0000   0x2c 0xf0 0x12 0x10 0x0d                   ,....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 PumpResume 2013-03-16T19:14:27 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-16T19:14:27)
    0000   0x1b 0xce 0x13 0x10 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-16T20:13:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-16T20:13:20)
    0000   0x14 0xcd 0x34 0x10 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-03-16T20:13:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 5.3,
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
    datetime (2013-03-16T20:13:42)
    0000   0x2a 0xcd 0x14 0x10 0x0d                   *....
    body (15)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0xfc 0x35 0xf0    FP.-j.5.
    0008   0x00 0x00 0x00 0x31 0x7d 0x5c 0x08         ...1}\.
    decimal
             70   80   13   45  106  252   53  240
              0    0    0   49  125   92    8
    HOUR BITS: [1, 1, 0]
#### RECORD 5 TempBasalDuration 2001-01-20T05:14:20 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 3690}
```
    op hex (2)
    0000   0x16 0x7b                                  .{
    decimal
             22  123
    datetime (2001-01-20T05:14:20)
    0000   0x14 0x4e 0x85 0x14 0x01                   .N...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 Base (2000, 0, 20, 13, 42, 0) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x31                                  11
    decimal
             49   49
    datetime ((2000, 0, 20, 13, 42, 0))
    0000   0x00 0x2a 0xcd 0x54 0x10                   .*.T.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 7 Base (2000, 8, 23, 19, 7, 46) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2000, 8, 23, 19, 7, 46))
    0000   0xae 0x07 0xf3 0x37 0x10                   ...7.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 8 Base (2000, 8, 23, 19, 28, 46) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2000, 8, 23, 19, 28, 46))
    0000   0xae 0x1c 0xf3 0x17 0x10                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Base (2010, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x12                                  ..
    decimal
             13   18
    datetime ((2010, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x0a                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 10 Base (2013, 0, 18, 0, 5, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2013, 0, 18, 0, 5, 0))
    0000   0x00 0x05 0x00 0x12 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 4.45, 'curve': 4},
 {'age': 227, 'amount': 0.45, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb2 0xd9 0x04 0x12 0xe3 0x04    \.......
    decimal
             92    8  178  217    4   18  227    4
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus (2004, 0, 0, 0, 7, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x12 0x12 0x00 0x1d 0xf3 0x57 0x10    ......W.
    decimal
              1   18   18    0   29  243   87   16
    datetime ((2004, 0, 0, 0, 7, 13))
    0000   0x0d 0x07 0x00 0x00 0x04                   .....
    body (0)

#### RECORD 13 Base (2005, 9, 13, 16, 45, 13) head[2], body[0] op[0xe4]

    op hex (2)
    0000   0xe4 0x30                                  .0
    decimal
            228   48
    datetime ((2005, 9, 13, 16, 45, 13))
    0000   0x8d 0x6d 0x30 0x8d 0x05                   .m0..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 14 Base (2000, 6, 0, 5, 46, 25) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x77                                  .w
    decimal
              0  119
    datetime ((2000, 6, 0, 5, 46, 25))
    0000   0x59 0xae 0x05 0x00 0x00                   Y....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 15 Base (2000, 1, 1, 7, 52, 3) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0xe4                                  ..
    decimal
              4  228
    datetime ((2000, 1, 1, 7, 52, 3))
    0000   0x03 0x74 0x47 0x01 0x70                   .tG.p
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 16 Base (2001, 4, 29, 16, 1, 57) head[2], body[0] op[0x1d]

    op hex (2)
    0000   0x1d 0x00                                  ..
    decimal
             29    0
    datetime ((2001, 4, 29, 16, 1, 57))
    0000   0x79 0x01 0x70 0x1d 0x01                   y.p..
    body (0)

#### RECORD 17 UnabsorbedInsulinBolus unknown head[95], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 0.0, 'curve': 5},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 2, 'amount': 0.075, 'curve': 0},
 {'age': 0, 'amount': 0.025, 'curve': 12},
 {'age': 232, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 30},
 {'age': 46, 'amount': 0.0, 'curve': 215},
 {'age': 17, 'amount': 0.225, 'curve': 13},
 {'age': 0, 'amount': 0.775, 'curve': 31},
 {'age': 9, 'amount': 5.425, 'curve': 17},
 {'age': 10, 'amount': 0.325, 'curve': 78},
 {'age': 217, 'amount': 1.35, 'curve': 41},
 {'age': 141, 'amount': 0.425, 'curve': 91},
 {'age': 14, 'amount': 1.95, 'curve': 218},
 {'age': 17, 'amount': 0.225, 'curve': 13},
 {'age': 81, 'amount': 0.0, 'curve': 13},
 {'age': 106, 'amount': 1.125, 'curve': 46},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 46},
 {'age': 1, 'amount': 3.125, 'curve': 49},
 {'age': 0, 'amount': 1.225, 'curve': 14},
 {'age': 73, 'amount': 5.45, 'curve': 17},
 {'age': 30, 'amount': 0.325, 'curve': 0},
 {'age': 223, 'amount': 0.7, 'curve': 9},
 {'age': 13, 'amount': 0.425, 'curve': 31},
 {'age': 59, 'amount': 0.0, 'curve': 239},
 {'age': 17, 'amount': 0.225, 'curve': 13},
 {'age': 126, 'amount': 0.25, 'curve': 39},
 {'age': 44, 'amount': 5.175, 'curve': 17},
 {'age': 10, 'amount': 0.325, 'curve': 126},
 {'age': 242, 'amount': 0.525, 'curve': 44}]
```
    op hex (95)
    0000   0x5c 0x5f 0x00 0x14 0x05 0x00 0x00 0x00    \_......
    0008   0x03 0x02 0x00 0x01 0x00 0x0c 0x00 0xe8    ........
    0010   0x00 0x00 0x00 0x1e 0x00 0x2e 0xd7 0x09    ........
    0018   0x11 0x0d 0x1f 0x00 0x1f 0xd9 0x09 0x11    ........
    0020   0x0d 0x0a 0x4e 0x36 0xd9 0x29 0x11 0x8d    ..N6.)..
    0028   0x5b 0x4e 0x0e 0xda 0x09 0x11 0x0d 0x00    [N......
    0030   0x51 0x0d 0x2d 0x6a 0x2e 0x00 0x00 0x00    Q.-j....
    0038   0x00 0x00 0x2e 0x7d 0x01 0x31 0x31 0x00    ...}.11.
    0040   0x0e 0xda 0x49 0x11 0x0d 0x1e 0x00 0x1c    ..I.....
    0048   0xdf 0x09 0x11 0x0d 0x1f 0x00 0x3b 0xef    ......;.
    0050   0x09 0x11 0x0d 0x0a 0x7e 0x27 0xcf 0x2c    ....~'.,
    0058   0x11 0x0d 0x0a 0x7e 0x15 0xf2 0x2c         ...~..,
    decimal
             92   95    0   20    5    0    0    0
              3    2    0    1    0   12    0  232
              0    0    0   30    0   46  215    9
             17   13   31    0   31  217    9   17
             13   10   78   54  217   41   17  141
             91   78   14  218    9   17   13    0
             81   13   45  106   46    0    0    0
              0    0   46  125    1   49   49    0
             14  218   73   17   13   30    0   28
            223    9   17   13   31    0   59  239
              9   17   13   10  126   39  207   44
             17   13   10  126   21  242   44
    datetime (unknown)

    body (0)

#### RECORD 18 Base (2012, 5, 19, 0, 62, 27) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x0d                                  ..
    decimal
             17   13
    datetime ((2012, 5, 19, 0, 62, 27))
    0000   0x5b 0x7e 0x00 0xf3 0x0c                   [~...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 1]
#### RECORD 19 Base (2010, 1, 13, 13, 16, 51) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x0d                                  ..
    decimal
             17   13
    datetime ((2010, 1, 13, 13, 16, 51))
    0000   0x33 0x50 0x0d 0x2d 0x6a                   3P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 20 Base (2007, 0, 0, 6, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x27                                  .'
    decimal
              0   39
    datetime ((2007, 0, 0, 6, 0, 0))
    0000   0x00 0x00 0x06 0x00 0x27                   ....'
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 21 Base (2001, 3, 4, 15, 4, 5) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x5c                                  }\
    decimal
            125   92
    datetime ((2001, 3, 4, 15, 4, 5))
    0000   0x05 0xc4 0xcf 0x04 0x01                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 ChangeRemoteID (2001, 0, 12, 19, 0, 0) head[2], body[0] op[0x27]

    op hex (2)
    0000   0x27 0x27                                  ''
    decimal
             39   39
    datetime ((2001, 0, 12, 19, 0, 0))
    0000   0x00 0x00 0xf3 0x4c 0x11                   ...L.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 23 Base (2001, 4, 17, 3, 51, 24) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2001, 4, 17, 3, 51, 24))
    0000   0x58 0x33 0xc3 0x31 0x11                   X3.1.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 24 Base (2001, 4, 19, 1, 48, 24) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2001, 4, 19, 1, 48, 24))
    0000   0x58 0x30 0xe1 0x33 0x11                   X0.3.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 25 Base (2001, 4, 19, 2, 37, 24) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2001, 4, 19, 2, 37, 24))
    0000   0x58 0x25 0xe2 0x13 0x11                   X%...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 26 Base (2012, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1c                                  ..
    decimal
             13   28
    datetime ((2012, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0xfc                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 27 Base (2013, 0, 17, 0, 0, 0) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0xf0                                  ..
    decimal
             21  240
    datetime ((2013, 0, 17, 0, 0, 0))
    0000   0x00 0x00 0x00 0x11 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 154, 'amount': 3.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0x9a 0x14                   \....
    decimal
             92    5  156  154   20
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2004-01-18T00:27:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x11 0x11 0x00 0x25 0xe2 0x53 0x11    ....%.S.
    decimal
              1   17   17    0   37  226   83   17
    datetime (2004-01-18T00:27:13)
    0000   0x0d 0x5b 0x00 0x32 0xc4                   .[.2.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 30 SelectBasalProfile (2013, 0, 13, 16, 28, 13) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x11                                  ..
    decimal
             20   17
    datetime ((2013, 0, 13, 16, 28, 13))
    0000   0x0d 0x1c 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 31 Base (2000, 0, 0, 0, 0, 21) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x00                                  j.
    decimal
            106    0
    datetime ((2000, 0, 0, 0, 0, 21))
    0000   0x15 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 32 Base (2004, 4, 30, 4, 8, 28) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x7d                                  .}
    decimal
             21  125
    datetime ((2004, 4, 30, 4, 8, 28))
    0000   0x5c 0x08 0x44 0x1e 0x04                   \.D..
    body (0)

#### RECORD 33 Base (2000, 0, 21, 21, 1, 20) head[2], body[0] op[0x9c]

    op hex (2)
    0000   0x9c 0xb8                                  ..
    decimal
            156  184
    datetime ((2000, 0, 21, 21, 1, 20))
    0000   0x14 0x01 0x15 0x15 0x00                   .....
    body (0)

#### RECORD 34 Base (2000, 4, 7, 13, 17, 20) head[2], body[0] op[0x32]

    op hex (2)
    0000   0x32 0xc4                                  2.
    decimal
             50  196
    datetime ((2000, 4, 7, 13, 17, 20))
    0000   0x54 0x11 0x0d 0x07 0x00                   T....
    body (0)

#### RECORD 35 Base (2001, 4, 13, 13, 49, 46) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2001, 4, 13, 13, 49, 46))
    0000   0x6e 0x31 0x8d 0x6d 0x31                   n1.m1
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 36 Base (2005, 2, 14, 24, 24, 16) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x05                                  ..
    decimal
            141    5
    datetime ((2005, 2, 14, 24, 24, 16))
    0000   0x10 0x98 0x58 0x4e 0x05                   ..XN.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-35.data: 37 records`
