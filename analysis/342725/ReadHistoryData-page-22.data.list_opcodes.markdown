## START logs/ReadHistoryData-page-22.data
ERROR month must be in 1..12 0000   0x1d 0x32                                  .2
#### STOPPING DOUBLE NULLS @ 260, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x07 0x00 0x0f 0x7d 0x5c 0x14 0x08 0x6b    ...}\..k
    0008   0x04 0x2c 0x7f 0x04 0x1c 0xbb 0x04 0x34    .,.....4
    0010   0x0b 0x14 0x90 0x33 0x14 0x50 0x97 0x14    ...3.P..
    0018   0x01 0x11 0x11 0x00 0x4e 0x1f 0x54 0x1d    ....N.T.
##### DEBUG DECIMAL
              7    0   15  125   92   20    8  107
              4   44  127    4   28  187    4   52
             11   20  144   51   20   80  151   20
              1   17   17    0   78   31   84   29
#### RECORD 0 CalBGForPH 2013-04-29T15:31:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-04-29T15:31:22)
    0000   0x56 0x1f 0x2f 0x1d 0x0d                   V./..
    body (0)

#### RECORD 1 BolusWizard 2013-04-29T15:31:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 194,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc2                                  [.
    decimal
             91  194
    datetime (2013-04-29T15:31:33)
    0000   0x61 0x1f 0x0f 0x1d 0x0d                   a....
    body (15)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x0f 0x1e 0x00    (P.-j...
    0008   0x00 0x11 0x00 0x1e 0x7d 0x5c 0x08         ....}\.
    decimal
             40   80   13   45  106   15   30    0
              0   17    0   30  125   92    8

#### RECORD 2 NewTimeSet 2001-01-04T11:16:04 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x07                                  ..
    decimal
             24    7
    datetime (2001-01-04T11:16:04)
    0000   0x04 0x50 0x6b 0x04 0x01                   .Pk..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 PumpSuspend (2013, 1, 15, 31, 33, 0) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x1e                                  ..
    decimal
             30   30
    datetime ((2013, 1, 15, 31, 33, 0))
    0000   0x00 0x61 0x1f 0x4f 0x1d                   .a.O.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 4 Base (2013, 1, 16, 11, 27, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2013, 1, 16, 11, 27, 0))
    0000   0x00 0x5b 0x0b 0x10 0x1d                   .[...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 Base (2000, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x11                                  ..
    decimal
             13   17
    datetime ((2000, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x00                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 Base (2013, 0, 13, 0, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2013, 0, 13, 0, 0, 0))
    0000   0x00 0x00 0x00 0x0d 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 3.6, 'curve': 4},
 {'age': 147, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x90 0x2f 0x04 0x50 0x93 0x04    \../.P..
    decimal
             92    8  144   47    4   80  147    4
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus (2011, 0, 3, 16, 10, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x0d 0x0d 0x00 0x5b 0x0b 0x50 0x1d    ....[.P.
    decimal
              1   13   13    0   91   11   80   29
    datetime ((2011, 0, 3, 16, 10, 13))
    0000   0x0d 0x0a 0x10 0x43 0x1b                   ...C.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Base (2011, 9, 17, 16, 27, 13) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x1d                                  1.
    decimal
             49   29
    datetime ((2011, 9, 17, 16, 27, 13))
    0000   0x8d 0x5b 0x10 0x51 0x1b                   .[.Q.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 Base (2013, 0, 13, 17, 0, 13) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x1d                                  ..
    decimal
             17   29
    datetime ((2013, 0, 13, 17, 0, 13))
    0000   0x0d 0x00 0x51 0x0d 0x2d                   ..Q.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 11 Base (2000, 0, 27, 0, 0, 0) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x20                                  j 
    decimal
            106   32
    datetime ((2000, 0, 27, 0, 0, 0))
    0000   0x00 0x00 0x00 0x1b 0x00                   .....
    body (0)

#### RECORD 12 Base (2004, 4, 19, 20, 11, 28) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x7d                                  .}
    decimal
              5  125
    datetime ((2004, 4, 19, 20, 11, 28))
    0000   0x5c 0x0b 0x34 0x53 0x04                   \.4S.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 13 Base (2001, 1, 4, 31, 16, 4) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x7b                                  .{
    decimal
            144  123
    datetime ((2001, 1, 4, 31, 16, 4))
    0000   0x04 0x50 0xdf 0x04 0x01                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 14 MResultTotals 2013-04-18T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x07 0x00 0x51 0x1b                   ...Q.
    decimal
              7    7    0   81   27
    datetime (2013-04-18T00:00:00)
    0000   0x51 0x1d                                  Q.
    body (3)
    hex
    0000   0x0d 0x0a 0xef                             ...
    decimal
             13   10  239

ERROR month must be in 1..12 0000   0x1d 0x32                                  .2
#### RECORD 15 Model522ResultTotals (2002, 0, 30, 0, 0, 0) head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime ((2002, 0, 30, 0, 0, 0))
    0000   0x1d 0x32                                  .2
    body (41)
    hex
    0000   0x1d 0x0d 0x5b 0xef 0x73 0x1d 0x12 0x1d    ..[.s...
    0008   0x0d 0x00 0x50 0x0d 0x2d 0x6a 0x19 0x00    ..P.-j..
    0010   0x00 0x00 0x10 0x00 0x09 0x7d 0x5c 0x0e    .....}\.
    0018   0x1c 0x41 0x04 0x34 0x91 0x04 0x90 0xb9    .A.4....
    0020   0x04 0x50 0x1d 0x14 0x34 0x64 0x49 0x1e    .P..4dI.
    0028   0x12                                       .
    decimal
             29   13   91  239  115   29   18   29
             13    0   80   13   45  106   25    0
              0    0   16    0    9  125   92   14
             28   65    4   52  145    4  144  185
              4   80   29   20   52  100   73   30
             18
    HOUR BITS: [0, 0, 1]
#### RECORD 16 Base (2003, 0, 0, 11, 11, 1) head[2], body[0] op[0x1d]

    op hex (2)
    0000   0x1d 0x0d                                  ..
    decimal
             29   13
    datetime ((2003, 0, 0, 11, 11, 1))
    0000   0x01 0x0b 0x0b 0x00 0x73                   ....s
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 17 Base (2002, 0, 8, 10, 13, 29) head[2], body[0] op[0x1d]

    op hex (2)
    0000   0x1d 0x52                                  .R
    decimal
             29   82
    datetime ((2002, 0, 8, 10, 13, 29))
    0000   0x1d 0x0d 0x0a 0xe8 0x72                   ....r
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 18 TempBasal (2007, 0, 8, 27, 13, 29) head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.25}
```
    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime ((2007, 0, 8, 27, 13, 29))
    0000   0x1d 0x0d 0x5b 0xe8 0x77                   ..[.w
    body (1)
    hex
    0000   0x33                                       3
    decimal
             51
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 19 Base (2013, 0, 13, 16, 0, 13) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0x1d                                  ..
    decimal
             18   29
    datetime ((2013, 0, 13, 16, 0, 13))
    0000   0x0d 0x00 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 20 Base (2000, 0, 22, 0, 0, 0) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x17                                  j.
    decimal
            106   23
    datetime ((2000, 0, 22, 0, 0, 0))
    0000   0x00 0x00 0x00 0x16 0x00                   .....
    body (0)

#### RECORD 21 Bolus 2004-04-07T20:04:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 12.5, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x7d 0x5c 0x11 0x2c 0x1b 0x04 0x1c    .}\.,...
    decimal
              1  125   92   17   44   27    4   28
    datetime (2004-04-07T20:04:23)
    0000   0x57 0x04 0x34 0xa7 0x04                   W.4..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 22 Base (2001, 1, 20, 19, 16, 4) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0xcf                                  ..
    decimal
            144  207
    datetime ((2001, 1, 20, 19, 16, 4))
    0000   0x04 0x50 0x33 0x14 0x01                   .P3..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 23 Base (2013, 1, 18, 19, 55, 0) head[2], body[0] op[0x02]

    op hex (2)
    0000   0x02 0x02                                  ..
    decimal
              2    2
    datetime ((2013, 1, 18, 19, 55, 0))
    0000   0x00 0x77 0x33 0x52 0x1d                   .w3R.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 24 Base (2013, 13, 20, 31, 6, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2013, 13, 20, 31, 6, 33))
    0000   0xe1 0x46 0x1f 0x34 0x1d                   .F.4.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 25 Base (2013, 13, 20, 31, 14, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2013, 13, 20, 31, 14, 33))
    0000   0xe1 0x4e 0x1f 0x14 0x1d                   .N...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 26 Base (2006, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2006, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x16                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
`end logs/ReadHistoryData-page-22.data: 27 records`
