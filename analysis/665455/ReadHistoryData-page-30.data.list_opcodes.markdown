## START logs/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 413, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x11 0x7d 0x01 0x11 0x11 0x00 0x4c 0x26    .}....L&
    0008   0x4b 0x04 0x0d 0x5b 0x00 0x78 0x34 0x0b    K..[.x4.
    0010   0x04 0x0d 0x06 0x50 0x0d 0x2d 0x6a 0x00    ...P.-j.
    0018   0x04 0x00 0x00 0x00 0x00 0x04 0x7d 0x5c    ......}\
##### DEBUG DECIMAL
             17  125    1   17   17    0   76   38
             75    4   13   91    0  120   52   11
              4   13    6   80   13   45  106    0
              4    0    0    0    0    4  125   92
#### RECORD 0 BolusWizard 2013-04-02T19:19:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-04-02T19:19:28)
    0000   0x5c 0x13 0x13 0x02 0x0d                   \....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x00 0x20 0x00    *P.-j. .
    0008   0x00 0x07 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106    0   32    0
              0    7    0   32  125

#### RECORD 1 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 1.2, 'curve': 4},
 {'age': 135, 'amount': 0.2, 'curve': 4},
 {'age': 205, 'amount': 1.0, 'curve': 4},
 {'age': 255, 'amount': 1.0, 'curve': 4},
 {'age': 9, 'amount': 3.2, 'curve': 20},
 {'age': 19, 'amount': 0.15, 'curve': 20},
 {'age': 29, 'amount': 0.15, 'curve': 20},
 {'age': 79, 'amount': 3.6, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x30 0x7d 0x04 0x08 0x87 0x04    \.0}....
    0008   0x28 0xcd 0x04 0x28 0xff 0x04 0x80 0x09    (..(....
    0010   0x14 0x06 0x13 0x14 0x06 0x1d 0x14 0x90    ........
    0018   0x4f 0x14                                  O.
    decimal
             92   26   48  125    4    8  135    4
             40  205    4   40  255    4  128    9
             20    6   19   20    6   29   20  144
             79   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-04-02T19:19:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-04-02T19:19:28)
    0000   0x5c 0x13 0x53 0x02 0x0d                   \.S..
    body (0)

#### RECORD 3 CalBGForPH 2013-04-02T23:21:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2013-04-02T23:21:27)
    0000   0x5b 0x15 0x37 0x02 0x8d                   [.7..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 BolusWizard 2013-04-02T23:21:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 276,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x14                                  [.
    decimal
             91   20
    datetime (2013-04-02T23:21:29)
    0000   0x5d 0x15 0x17 0x02 0x0d                   ]....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125

#### RECORD 5 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 247, 'amount': 3.2, 'curve': 4},
 {'age': 111, 'amount': 1.2, 'curve': 20},
 {'age': 121, 'amount': 0.2, 'curve': 20},
 {'age': 191, 'amount': 1.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x80 0xf7 0x04 0x30 0x6f 0x14    \....0o.
    0008   0x08 0x79 0x14 0x28 0xbf 0x14              .y.(..
    decimal
             92   14  128  247    4   48  111   20
              8  121   20   40  191   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-04-02T23:21:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-04-02T23:21:29)
    0000   0x5d 0x15 0x57 0x02 0x0d                   ].W..
    body (0)

#### RECORD 7 ResultTotals 2013-04-02T13:13:02 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x80                   .....
    decimal
              7    0    0    5  128
    datetime (2013-04-02T13:13:02)
    0000   0x42 0x0d 0x6d 0x42 0x0d                   B.mB.
    body (51)
    hex
    0000   0x05 0x10 0xe3 0x6a 0x23 0x07 0x00 0x00    ...j#...
    0008   0x05 0x80 0x02 0xd8 0x34 0x02 0xa8 0x30    ....4..0
    0010   0x00 0x81 0x02 0xa8 0x30 0x01 0x88 0x3a    ....0..:
    0018   0x01 0x20 0x2a 0x00 0x00 0x00 0x08 0x05    . *.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x46 0x0f 0x0e 0x03 0x0d    ...F....
    0030   0x1f 0x00 0x79                             ..y
    decimal
              5   16  227  106   35    7    0    0
              5  128    2  216   52    2  168   48
              0  129    2  168   48    1  136   58
              1   32   42    0    0    0    8    5
              3    0    0   12    0  232    0    0
              0   30    0   70   15   14    3   13
             31    0  121
    DAY BITS: [0, 1, 0]
#### RECORD 8 EnableDisableRemote (2005, 0, 23, 10, 13, 3) head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0x0e                                  &.
    decimal
             38   14
    datetime ((2005, 0, 23, 10, 13, 3))
    0000   0x03 0x0d 0x0a 0x77 0x65                   ...we
    body (14)
    hex
    0000   0x3b 0x2e 0x03 0x0d 0x5b 0x77 0x6b 0x3b    ;...[wk;
    0008   0x0e 0x03 0x0d 0x1d 0x50 0x0d              ....P.
    decimal
             59   46    3   13   91  119  107   59
             14    3   13   29   80   13
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 9 Base (2000, 0, 0, 0, 22, 0) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 22, 0))
    0000   0x00 0x16 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 10 Base (2000, 4, 22, 22, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x16                                  ..
    decimal
              0   22
    datetime ((2000, 4, 22, 22, 1, 61))
    0000   0x7d 0x01 0x16 0x16 0x00                   }....
    body (0)

#### RECORD 11 Base (2015, 4, 10, 13, 3, 14) head[2], body[0] op[0x6b]

    op hex (2)
    0000   0x6b 0x3b                                  k;
    decimal
            107   59
    datetime ((2015, 4, 10, 13, 3, 14))
    0000   0x4e 0x03 0x0d 0x0a 0x6f                   N...o
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 12 Base (2012, 0, 10, 13, 3, 47) head[2], body[0] op[0x79]

    op hex (2)
    0000   0x79 0x20                                  y 
    decimal
            121   32
    datetime ((2012, 0, 10, 13, 3, 47))
    0000   0x2f 0x03 0x0d 0x0a 0x6c                   /...l
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 13 Base (2012, 0, 27, 13, 3, 47) head[2], body[0] op[0x55]

    op hex (2)
    0000   0x55 0x2f                                  U/
    decimal
             85   47
    datetime ((2012, 0, 27, 13, 3, 47))
    0000   0x2f 0x03 0x0d 0x5b 0x6c                   /..[l
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 14 Base (2000, 0, 9, 13, 3, 15) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x2f                                  j/
    decimal
            106   47
    datetime ((2000, 0, 9, 13, 3, 15))
    0000   0x0f 0x03 0x0d 0x29 0x50                   ...)P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 15 Base (2000, 4, 0, 31, 0, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 31, 0, 42))
    0000   0x6a 0x00 0x1f 0x00 0x00                   j....
    body (0)

#### RECORD 16 Base (2008, 1, 5, 28, 61, 31) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x00                                  ..
    decimal
             19    0
    datetime ((2008, 1, 5, 28, 61, 31))
    0000   0x1f 0x7d 0x5c 0x05 0x58                   .}\.X
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 17 Base (2010, 0, 0, 31, 31, 1) head[2], body[0] op[0x35]

    op hex (2)
    0000   0x35 0x04                                  5.
    decimal
             53    4
    datetime ((2010, 0, 0, 31, 31, 1))
    0000   0x01 0x1f 0x1f 0x00 0x6a                   ....j
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 18 Base (2000, 0, 23, 10, 13, 3) head[2], body[0] op[0x2f]

    op hex (2)
    0000   0x2f 0x4f                                  /O
    decimal
             47   79
    datetime ((2000, 0, 23, 10, 13, 3))
    0000   0x03 0x0d 0x0a 0xd7 0x50                   ....P
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 19 Base (2011, 0, 31, 10, 13, 3) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x30                                  80
    decimal
             56   48
    datetime ((2011, 0, 31, 10, 13, 3))
    0000   0x03 0x0d 0x0a 0xdf 0x7b                   ....{
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 20 Base (2008, 0, 31, 27, 13, 3) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x34                                  .4
    decimal
              5   52
    datetime ((2008, 0, 31, 27, 13, 3))
    0000   0x03 0x0d 0x5b 0xdf 0x58                   ..[.X
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 21 NoDelivery 2010-01-13T13:16:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x14 0x03 0x0d                        ....
    decimal
              6   20    3   13
    datetime (2010-01-13T13:16:00)
    0000   0x00 0x50 0x0d 0x2d 0x6a                   .P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 22 Base (2005, 0, 0, 0, 0, 0) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x00                                  ..
    decimal
             21    0
    datetime ((2005, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x15                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 23 Base (2008, 1, 20, 6, 60, 8) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x5c                                  }\
    decimal
            125   92
    datetime ((2008, 1, 20, 6, 60, 8))
    0000   0x08 0x7c 0x06 0x14 0x58                   .|..X
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 24 Base (2008, 0, 0, 11, 11, 1) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x14                                  8.
    decimal
             56   20
    datetime ((2008, 0, 0, 11, 11, 1))
    0000   0x01 0x0b 0x0b 0x00 0x58                   ....X
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 25 NoDelivery (2004, 0, 4, 0, 0, 7) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x54 0x03 0x0d                        .T..
    decimal
              6   84    3   13
    datetime ((2004, 0, 4, 0, 0, 7))
    0000   0x07 0x00 0x00 0x04 0x74                   ....t
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 26 Base (2000, 5, 5, 13, 3, 45) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0x0d                                  C.
    decimal
             67   13
    datetime ((2000, 5, 5, 13, 3, 45))
    0000   0x6d 0x43 0x0d 0x05 0x00                   mC...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 27 Base (2004, 12, 0, 0, 5, 31) head[2], body[0] op[0x9b]

    op hex (2)
    0000   0x9b 0x6c                                  .l
    decimal
            155  108
    datetime ((2004, 12, 0, 0, 5, 31))
    0000   0xdf 0x05 0x00 0x00 0x04                   .....
    body (0)

#### RECORD 28 Base (2006, 5, 0, 1, 14, 52) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0x03                                  t.
    decimal
            116    3
    datetime ((2006, 5, 0, 1, 14, 52))
    0000   0x74 0x4e 0x01 0x00 0x16                   tN...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 29 Base (2004, 0, 0, 22, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x46                                  .F
    decimal
              0   70
    datetime ((2004, 0, 0, 22, 0, 1))
    0000   0x01 0x00 0x16 0x00 0xd4                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 1]
#### RECORD 30 Base (2000, 0, 0, 0, 17, 44) head[2], body[0] op[0x53]

    op hex (2)
    0000   0x53 0x00                                  S.
    decimal
             83    0
    datetime ((2000, 0, 0, 0, 17, 44))
    0000   0x2c 0x11 0x00 0x00 0x00                   ,....
    body (0)

#### RECORD 31 Prime (2000, 0, 0, 8, 0, 12) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.1, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x02 0x01 0x00 0x00                   .....
    decimal
              3    2    1    0    0
    datetime ((2000, 0, 0, 8, 0, 12))
    0000   0x0c 0x00 0xe8 0x00 0x00                   .....
    body (0)

#### RECORD 32 Base (2004, 1, 9, 1, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x19                                  ..
    decimal
              0   25
    datetime ((2004, 1, 9, 1, 0, 0))
    0000   0x00 0x40 0x01 0x09 0x04                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 33 Base (2004, 1, 10, 7, 46, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1e                                  ..
    decimal
             13   30
    datetime ((2004, 1, 10, 7, 46, 0))
    0000   0x00 0x6e 0x27 0x0a 0x04                   .n'..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 34 Base (2004, 1, 11, 9, 14, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1f                                  ..
    decimal
             13   31
    datetime ((2004, 1, 11, 9, 14, 0))
    0000   0x00 0x4e 0x09 0x0b 0x04                   .N...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 35 Base (2004, 1, 11, 31, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1a                                  ..
    decimal
             13   26
    datetime ((2004, 1, 11, 31, 0, 0))
    0000   0x00 0x40 0x1f 0x0b 0x04                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 Base (2004, 1, 11, 31, 26, 1) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1a                                  ..
    decimal
             13   26
    datetime ((2004, 1, 11, 31, 26, 1))
    0000   0x01 0x5a 0x1f 0x0b 0x04                   .Z...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 Base (2004, 13, 11, 6, 7, 11) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2004, 13, 11, 6, 7, 11))
    0000   0xcb 0x47 0x26 0x2b 0x04                   .G&+.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
#### RECORD 38 Base (2004, 13, 11, 6, 12, 11) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2004, 13, 11, 6, 12, 11))
    0000   0xcb 0x4c 0x26 0x0b 0x04                   .L&..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 Base (2001, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2001, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x11                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
`end logs/ReadHistoryData-page-30.data: 40 records`
