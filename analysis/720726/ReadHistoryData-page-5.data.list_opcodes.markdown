## START logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 714, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb7 0x57 0x4a 0x67 0x0d 0x0a 0x1d 0xb5    .WJg....
    0008   0x60 0x2b 0x67 0x8d 0x3f 0x23 0xb5 0x60    `+g.?#.`
    0010   0xab 0x67 0x0d 0x72 0x90 0x70 0x5b 0x9e    .g.r.p[.
    0018   0x9a 0x61 0x0b 0x67 0x0d 0x00 0x90 0x00    .a.g....
##### DEBUG DECIMAL
            183   87   74  103   13   10   29  181
             96   43  103  141   63   35  181   96
            171  103   13  114  144  112   91  158
            154   97   11  103   13    0  144    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 2.4, 'curve': 4},
 {'age': 106, 'amount': 1.4, 'curve': 4},
 {'age': 116, 'amount': 2.2, 'curve': 4},
 {'age': 70, 'amount': 2.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x60 0x42 0x04 0x38 0x6a 0x04    \.`B.8j.
    0008   0x58 0x74 0x04 0x68 0x46 0x14              Xt.hF.
    decimal
             92   14   96   66    4   56  106    4
             88  116    4  104   70   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-09-06T15:44:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x98 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  152    0
    datetime (2013-09-06T15:44:18)
    0000   0x92 0x6c 0x4f 0x66 0x0d                   .lOf.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-09-06T18:28:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-09-06T18:28:26)
    0000   0x9a 0x5c 0x32 0x66 0x0d                   .\2f.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 Base (2013, 9, 6, 18, 28, 26) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime ((2013, 9, 6, 18, 28, 26))
    0000   0x9a 0x5c 0xf2 0x66 0x0d                   .\.f.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 Base (2012, 5, 26, 20, 27, 48) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x90                                  r.
    decimal
            114  144
    datetime ((2012, 5, 26, 20, 27, 48))
    0000   0x70 0x5b 0x54 0xba 0x5c                   p[T.\
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 5 Base (2014, 0, 0, 16, 33, 13) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0x66                                  .f
    decimal
             18  102
    datetime ((2014, 0, 0, 16, 33, 13))
    0000   0x0d 0x21 0x90 0x00 0x6e                   .!..n
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 6 ChangeTime (2000, 0, 0, 24, 0, 52) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x36                                  .6
    decimal
             23   54
    datetime ((2000, 0, 0, 24, 0, 52))
    0000   0x34 0x00 0x78 0x00 0x00                   4.x..
    body (0)

#### RECORD 7 Base (2008, 8, 14, 28, 54, 28) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2008, 8, 14, 28, 54, 28))
    0000   0x9c 0x36 0x5c 0x0e 0x28                   .6\.(
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 8 Base (2014, 7, 24, 4, 38, 32) head[2], body[0] op[0xaa]

    op hex (2)
    0000   0xaa 0x04                                  ..
    decimal
            170    4
    datetime ((2014, 7, 24, 4, 38, 32))
    0000   0x60 0xe6 0x04 0x38 0x0e                   `..8.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 0, 1]
#### RECORD 9 SelectBasalProfile (2010, 0, 17, 9, 20, 24) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x58                                  .X
    decimal
             20   88
    datetime ((2010, 0, 17, 9, 20, 24))
    0000   0x18 0x14 0x69 0xd1 0xba                   ..i..
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[114], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 0.15, 'curve': 21},
 {'age': 1, 'amount': 0.75, 'curve': 0},
 {'age': 0, 'amount': 3.9, 'curve': 156},
 {'age': 16, 'amount': 0.0, 'curve': 0},
 {'age': 92, 'amount': 4.65, 'curve': 82},
 {'age': 13, 'amount': 2.55, 'curve': 10},
 {'age': 168, 'amount': 1.525, 'curve': 107},
 {'age': 102, 'amount': 1.325, 'curve': 13},
 {'age': 7, 'amount': 1.575, 'curve': 168},
 {'age': 181, 'amount': 2.675, 'curve': 102},
 {'age': 114, 'amount': 0.325, 'curve': 144},
 {'age': 91, 'amount': 2.8, 'curve': 0},
 {'age': 108, 'amount': 3.85, 'curve': 22},
 {'age': 13, 'amount': 2.55, 'curve': 27},
 {'age': 0, 'amount': 3.6, 'curve': 110},
 {'age': 54, 'amount': 0.575, 'curve': 0},
 {'age': 96, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 54, 'amount': 2.4, 'curve': 92},
 {'age': 156, 'amount': 0.2, 'curve': 0},
 {'age': 40, 'amount': 0.5, 'curve': 170},
 {'age': 1, 'amount': 0.5, 'curve': 0},
 {'age': 0, 'amount': 2.4, 'curve': 96},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 108, 'amount': 3.875, 'curve': 86},
 {'age': 13, 'amount': 2.55, 'curve': 91},
 {'age': 129, 'amount': 0.0, 'curve': 97},
 {'age': 102, 'amount': 0.575, 'curve': 13},
 {'age': 144, 'amount': 0.55, 'curve': 0},
 {'age': 23, 'amount': 2.75, 'curve': 54},
 {'age': 0, 'amount': 0.0, 'curve': 80},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 80, 'amount': 0.0, 'curve': 54},
 {'age': 11, 'amount': 2.3, 'curve': 96},
 {'age': 4, 'amount': 1.375, 'curve': 156},
 {'age': 20, 'amount': 1.225, 'curve': 40},
 {'age': 20, 'amount': 5.475, 'curve': 1}]
```
    op hex (114)
    0000   0x5c 0x72 0x06 0x0d 0x15 0x1e 0x01 0x00    \r......
    0008   0x9c 0x00 0x9c 0x00 0x10 0x00 0xba 0x5c    .......\
    0010   0x52 0x66 0x0d 0x0a 0x3d 0xa8 0x6b 0x35    Rf..=.k5
    0018   0x66 0x0d 0x3f 0x07 0xa8 0x6b 0xb5 0x66    f.?..k.f
    0020   0x0d 0x72 0x90 0x70 0x5b 0x00 0x9a 0x6c    .r.p[..l
    0028   0x16 0x66 0x0d 0x1b 0x90 0x00 0x6e 0x17    .f....n.
    0030   0x36 0x00 0x00 0x60 0x00 0x00 0x00 0x00    6..`....
    0038   0x60 0x36 0x5c 0x08 0x9c 0x00 0x14 0x28    `6\....(
    0040   0xaa 0x14 0x01 0x00 0x60 0x00 0x60 0x00    ....`.`.
    0048   0x00 0x00 0x9b 0x6c 0x56 0x66 0x0d 0x5b    ...lVf.[
    0050   0x00 0x81 0x61 0x17 0x66 0x0d 0x16 0x90    ..a.f...
    0058   0x00 0x6e 0x17 0x36 0x00 0x00 0x50 0x00    .n.6..P.
    0060   0x00 0x00 0x00 0x50 0x36 0x5c 0x0b 0x60    ...P6\.`
    0068   0x37 0x04 0x9c 0x31 0x14 0x28 0xdb 0x14    7..1.(..
    0070   0x01 0x00                                  ..
    decimal
             92  114    6   13   21   30    1    0
            156    0  156    0   16    0  186   92
             82  102   13   10   61  168  107   53
            102   13   63    7  168  107  181  102
             13  114  144  112   91    0  154  108
             22  102   13   27  144    0  110   23
             54    0    0   96    0    0    0    0
             96   54   92    8  156    0   20   40
            170   20    1    0   96    0   96    0
              0    0  155  108   86  102   13   91
              0  129   97   23  102   13   22  144
              0  110   23   54    0    0   80    0
              0    0    0   80   54   92   11   96
             55    4  156   49   20   40  219   20
              1    0
    datetime (unknown)

    body (0)

#### RECORD 11 Base (2001, 4, 0, 20, 0, 16) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x00                                  P.
    decimal
             80    0
    datetime ((2001, 4, 0, 20, 0, 16))
    0000   0x50 0x00 0x54 0x00 0x81                   P.T..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 Base (2000, 4, 0, 27, 13, 38) head[2], body[0] op[0x61]

    op hex (2)
    0000   0x61 0x57                                  aW
    decimal
             97   87
    datetime ((2000, 4, 0, 27, 13, 38))
    0000   0x66 0x0d 0x7b 0x00 0x80                   f.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 13 Base (2000, 0, 0, 0, 13, 7) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime ((2000, 0, 0, 0, 13, 7))
    0000   0x07 0x0d 0x00 0x20 0x00                   ... .
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 14 ResultTotals (2000, 10, 0, 0, 13, 6) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xcd                   .....
    decimal
              7    0    0    6  205
    datetime ((2000, 10, 0, 0, 13, 6))
    0000   0x86 0x8d 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 15 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x86 0x8d 0x06 0x00 0x6b 0x33 0x9c    n....k3.
    0008   0x05 0x00 0x00 0x06 0xcd 0x03 0x85 0x34    .......4
    0010   0x03 0x48 0x30 0x00 0xd7 0x02 0xac 0x00    .H0.....
    0018   0x00 0x00 0x9c 0x00 0x00 0x07 0x00 0x01    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  134  141    6    0  107   51  156
              5    0    0    6  205    3  133   52
              3   72   48    0  215    2  172    0
              0    0  156    0    0    7    0    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 16 CalBGForPH 2013-09-07T01:20:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 262}
```
    op hex (2)
    0000   0x0a 0x06                                  ..
    decimal
             10    6
    datetime (2013-09-07T01:20:42)
    0000   0xaa 0x54 0x21 0x67 0x8d                   .T!g.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 Base (2013, 9, 7, 1, 20, 42) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime ((2013, 9, 7, 1, 20, 42))
    0000   0xaa 0x54 0xc1 0x67 0x0d                   .T.g.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 Base (2004, 5, 23, 17, 27, 48) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x90                                  r.
    decimal
            114  144
    datetime ((2004, 5, 23, 17, 27, 48))
    0000   0x70 0x5b 0x91 0xb7 0x54                   p[..T
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 19 Bolus (2000, 2, 0, 0, 28, 54) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 10.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x67 0x0d 0x00 0x90 0x00 0x6e 0x17    .g....n.
    decimal
              1  103   13    0  144    0  110   23
    datetime ((2000, 2, 0, 0, 28, 54))
    0000   0x36 0x9c 0x00 0x00 0x00                   6....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 Base (2011, 1, 28, 22, 28, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x40                                  .@
    decimal
              0   64
    datetime ((2011, 1, 28, 22, 28, 0))
    0000   0x00 0x5c 0x36 0x5c 0x0b                   .\6\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 21 Base (2012, 1, 4, 2, 32, 4) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x70                                  Pp
    decimal
             80  112
    datetime ((2012, 1, 4, 2, 32, 4))
    0000   0x04 0x60 0xa2 0x04 0x9c                   .`...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 22 Base (2000, 0, 0, 16, 0, 1) head[2], body[0] op[0x9c]

    op hex (2)
    0000   0x9c 0x14                                  ..
    decimal
            156   20
    datetime ((2000, 0, 0, 16, 0, 1))
    0000   0x01 0x00 0x70 0x00 0x70                   ..p.p
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 23 Base (2007, 2, 1, 20, 56, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x40                                  .@
    decimal
              0   64
    datetime ((2007, 2, 1, 20, 56, 0))
    0000   0x00 0xb8 0x54 0x41 0x67                   ..TAg
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 24 Base (2007, 6, 3, 11, 44, 31) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2007, 6, 3, 11, 44, 31))
    0000   0x5f 0xac 0x6b 0x23 0x67                   _.k#g
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 25 Base (2007, 2, 3, 11, 44, 11) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2007, 2, 3, 11, 44, 11))
    0000   0x0b 0xac 0x6b 0xe3 0x67                   ..k.g
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 26 Base (2000, 9, 1, 27, 48, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x72                                  .r
    decimal
             13  114
    datetime ((2000, 9, 1, 27, 48, 16))
    0000   0x90 0x70 0x7b 0x01 0x80                   .p{..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 27 Base (2000, 0, 14, 8, 13, 7) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x04                                  @.
    decimal
             64    4
    datetime ((2000, 0, 14, 8, 13, 7))
    0000   0x07 0x0d 0x08 0x2e 0x00                   .....
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 28 BolusWizard 2013-09-07T06:18:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T06:18:37)
    0000   0xa5 0x52 0x06 0x67 0x0d                   .R.g.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 2.8, 'curve': 20},
 {'age': 154, 'amount': 2.0, 'curve': 20},
 {'age': 204, 'amount': 2.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x2c 0x14 0x50 0x9a 0x14    \.p,.P..
    0008   0x60 0xcc 0x14                             `..
    decimal
             92   11  112   44   20   80  154   20
             96  204   20
    datetime (unknown)

    body (0)

#### RECORD 30 BolusWizard 2013-09-07T06:18:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T06:18:52)
    0000   0xb4 0x52 0x06 0x67 0x0d                   .R.g.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 2.8, 'curve': 20},
 {'age': 154, 'amount': 2.0, 'curve': 20},
 {'age': 204, 'amount': 2.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x2c 0x14 0x50 0x9a 0x14    \.p,.P..
    0008   0x60 0xcc 0x14                             `..
    decimal
             92   11  112   44   20   80  154   20
             96  204   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-09-07T06:18:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x00 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    0    0
    datetime (2013-09-07T06:18:52)
    0000   0xb4 0x52 0x46 0x67 0x0d                   .RFg.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 BasalProfileStart 2013-09-07T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-07T09:30:00)
    0000   0x80 0x5e 0x09 0x07 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 34 BolusWizard 2013-09-07T09:36:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T09:36:20)
    0000   0x94 0x64 0x09 0x67 0x0d                   .d.g.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 198, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0xc6 0x04                   \.h..
    decimal
             92    5  104  198    4
    datetime (unknown)

    body (0)

#### RECORD 36 Base (2013, 9, 7, 9, 36, 20) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime ((2013, 9, 7, 9, 36, 20))
    0000   0x94 0x64 0x09 0x07 0x0d                   .d...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 37 CalBGForPH (2004, 0, 0, 4, 0, 1) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 30}
```
    op hex (2)
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    datetime ((2004, 0, 0, 4, 0, 1))
    0000   0x01 0x00 0x24 0x00 0x24                   ..$.$
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 38 Base (2007, 2, 9, 4, 20, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x10                                  ..
    decimal
              0   16
    datetime ((2007, 2, 9, 4, 20, 0))
    0000   0x00 0x94 0x64 0x49 0x67                   ..dIg
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 39 Base (2007, 2, 10, 14, 17, 1) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x64                                  .d
    decimal
             13  100
    datetime ((2007, 2, 10, 14, 17, 1))
    0000   0x01 0x91 0x4e 0x0a 0x07                   ..N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 Base (2007, 2, 10, 14, 41, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x17                                  ..
    decimal
             13   23
    datetime ((2007, 2, 10, 14, 41, 0))
    0000   0x00 0xa9 0x4e 0x0a 0x07                   ..N..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 41 Base (2007, 2, 1, 14, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x18                                  ..
    decimal
             13   24
    datetime ((2007, 2, 1, 14, 0, 0))
    0000   0x00 0x80 0x4e 0x01 0x07                   ..N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 Base (2007, 2, 1, 14, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x7b                                  .{
    decimal
             13  123
    datetime ((2007, 2, 1, 14, 0, 0))
    0000   0x00 0x80 0x4e 0x01 0x07                   ..N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 43 Base (2005, 0, 21, 10, 0, 32) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2005, 0, 21, 10, 0, 32))
    0000   0x20 0x00 0x0a 0x75 0xa5                    ..u.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 44 Base (2005, 4, 14, 31, 13, 39) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x22                                  h"
    decimal
            104   34
    datetime ((2005, 4, 14, 31, 13, 39))
    0000   0x67 0x0d 0x3f 0x0e 0xa5                   g.?..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 45 Base (2000, 4, 16, 18, 13, 39) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0xa2                                  h.
    decimal
            104  162
    datetime ((2000, 4, 16, 18, 13, 39))
    0000   0x67 0x0d 0x72 0x90 0x70                   g.r.p
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 46 BolusWizard 2013-09-07T02:47:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 65,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.6,
 'carb_input': 36,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 1.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 128}
```
    op hex (2)
    0000   0x5b 0x41                                  [A
    decimal
             91   65
    datetime (2013-09-07T02:47:25)
    0000   0x99 0x6f 0x02 0x67 0x0d                   .o.g.
    body (15)
    hex
    0000   0x24 0x90 0x00 0x6e 0x17 0x36 0x10 0x00    $..n.6..
    0008   0x80 0x00 0x00 0x10 0x00 0x80 0x36         ......6
    decimal
             36  144    0  110   23   54   16    0
            128    0    0   16    0  128   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 0.9, 'curve': 4},
 {'age': 73, 'amount': 2.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x8b 0x04 0x68 0x49 0x14    \.$..hI.
    decimal
             92    8   36  139    4  104   73   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-09-07T02:47:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x10 0x00    ........
    decimal
              1    0  128    0  128    0   16    0
    datetime (2013-09-07T02:47:26)
    0000   0x9a 0x6f 0x42 0x67 0x0d                   .oBg.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2013-09-07T02:54:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 6,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 20}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T02:54:43)
    0000   0xab 0x76 0x02 0x67 0x0d                   .v.g.
    body (15)
    hex
    0000   0x06 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x14 0x00 0x00 0x00 0x00 0x14 0x36         ......6
    decimal
              6  144    0  110   23   54    0    0
             20    0    0    0    0   20   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 2.35, 'curve': 4},
 {'age': 16, 'amount': 0.85, 'curve': 4},
 {'age': 146, 'amount': 0.9, 'curve': 4},
 {'age': 80, 'amount': 2.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x5e 0x06 0x04 0x22 0x10 0x04    \.^.."..
    0008   0x24 0x92 0x04 0x68 0x50 0x14              $..hP.
    decimal
             92   14   94    6    4   34   16    4
             36  146    4  104   80   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-09-07T02:54:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x8c 0x00    ........
    decimal
              1    0   20    0   20    0  140    0
    datetime (2013-09-07T02:54:43)
    0000   0xab 0x76 0x42 0x67 0x0d                   .vBg.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 BasalProfileStart 2013-09-07T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-07T04:00:00)
    0000   0x80 0x40 0x04 0x07 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 53 BasalProfileStart 2013-09-07T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-07T09:30:00)
    0000   0x80 0x5e 0x09 0x07 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 54 BolusWizard 2013-09-07T10:23:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-07T10:23:55)
    0000   0xb7 0x57 0x0a 0x67 0x0d                   .W.g.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 199, 'amount': 2.85, 'curve': 20},
 {'age': 209, 'amount': 0.85, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x72 0xc7 0x14 0x22 0xd1 0x14    \.r.."..
    decimal
             92    8  114  199   20   34  209   20
    datetime (unknown)

    body (0)

#### RECORD 56 Base (2013, 9, 7, 10, 23, 55) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime ((2013, 9, 7, 10, 23, 55))
    0000   0xb7 0x57 0x0a 0x07 0x0d                   .W...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 CalBGForPH (2012, 0, 0, 28, 0, 1) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 30}
```
    op hex (2)
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    datetime ((2012, 0, 0, 28, 0, 1))
    0000   0x01 0x00 0x7c 0x00 0x7c                   ..|.|
    body (0)
    YEAR BITS: [0, 1, 1, 1]
`end logs/ReadHistoryData-page-5.data: 58 records`
