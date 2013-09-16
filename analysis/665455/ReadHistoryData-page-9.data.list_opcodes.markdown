## START logs/ReadHistoryData-page-9.data
#### STOPPING DOUBLE NULLS @ 277, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x02 0x00 0x01 0x01 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x34 0xc8 0x40 0x8f 0x01    ...4.@..
    0010   0x19 0x0d 0x1e 0x00 0x41 0x87 0x09 0x19    ....A...
    0018   0x0d 0x1f 0x00 0x43 0x80 0x0a 0x19 0x0d    ...C....
##### DEBUG DECIMAL
              2    0    1    1    0   12    0  232
              0    0    0   52  200   64  143    1
             25   13   30    0   65  135    9   25
             13   31    0   67  128   10   25   13
#### RECORD 0 BolusWizard 2013-06-23T12:58:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-06-23T12:58:04)
    0000   0x44 0xba 0x0c 0x17 0x0d                   D....
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    0P.-j.$.
    0008   0x00 0x07 0x00 0x24 0x7d                   ...$}
    decimal
             48   80   13   45  106    0   36    0
              0    7    0   36  125
    HOUR BITS: [1, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 1.5, 'curve': 4},
 {'age': 48, 'amount': 2.45, 'curve': 20},
 {'age': 58, 'amount': 4.15, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0x7c 0x04 0x62 0x30 0x14    \.<|.b0.
    0008   0xa6 0x3a 0x14                             .:.
    decimal
             92   11   60  124    4   98   48   20
            166   58   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-06-23T12:58:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-06-23T12:58:05)
    0000   0x45 0xba 0x4c 0x17 0x0d                   E.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 3 CalBGForPH 2013-06-23T14:49:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-06-23T14:49:18)
    0000   0x52 0xb1 0x2e 0x17 0x0d                   R....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 4 CalBGForPH 2013-06-23T15:30:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-06-23T15:30:07)
    0000   0x47 0x9e 0x2f 0x17 0x0d                   G./..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 CalBGForPH 2013-06-23T19:51:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-06-23T19:51:37)
    0000   0x65 0xb3 0x33 0x17 0x0d                   e.3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 BolusWizard 2013-06-23T19:52:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 105,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-06-23T19:52:24)
    0000   0x58 0xb4 0x13 0x17 0x0d                   X....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x00 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             65   80   13   45  106    0   50    0
              0    0    0   50  125
    HOUR BITS: [1, 0, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 3.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0xa2 0x14                   \....
    decimal
             92    5  144  162   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-06-23T19:52:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-06-23T19:52:24)
    0000   0x58 0xb4 0x53 0x17 0x0d                   X.S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 ResultTotals 2013-04-23T13:13:55 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x04                   .....
    decimal
              7    0    0    6    4
    datetime (2013-04-23T13:13:55)
    0000   0x77 0x0d 0x6d 0x77 0x0d                   w.mw.
    body (51)
    hex
    0000   0x05 0x10 0xab 0x69 0xa3 0x08 0x00 0x00    ...i....
    0008   0x06 0x04 0x03 0x68 0x39 0x02 0x9c 0x2b    ...h9..+
    0010   0x00 0x71 0x02 0x9c 0x2b 0x01 0x58 0x33    .q..+.X3
    0018   0x01 0x44 0x31 0x00 0x00 0x00 0x04 0x02    .D1.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x6c 0xaf 0x0d 0x18 0x0d    ...l....
    0030   0x1f 0x00 0x61                             ..a
    decimal
              5   16  171  105  163    8    0    0
              6    4    3  104   57    2  156   43
              0  113    2  156   43    1   88   51
              1   68   49    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0   30    0  108  175   13   24   13
             31    0   97
    DAY BITS: [0, 1, 1]
#### RECORD 10 Base (2013, 0, 4, 10, 13, 24) head[2], body[0] op[0x89]

    op hex (2)
    0000   0x89 0x0e                                  ..
    decimal
            137   14
    datetime ((2013, 0, 4, 10, 13, 24))
    0000   0x18 0x0d 0x0a 0xa4 0x4d                   ....M
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 11 Base (2008, 0, 4, 27, 13, 24) head[2], body[0] op[0xb8]

    op hex (2)
    0000   0xb8 0x2f                                  ./
    decimal
            184   47
    datetime ((2008, 0, 4, 27, 13, 24))
    0000   0x18 0x0d 0x5b 0xa4 0x68                   ..[.h
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 12 Base (2013, 0, 16, 23, 13, 24) head[2], body[0] op[0xb8]

    op hex (2)
    0000   0xb8 0x0f                                  ..
    decimal
            184   15
    datetime ((2013, 0, 16, 23, 13, 24))
    0000   0x18 0x0d 0x37 0x50 0x0d                   ..7P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 13 Base (2000, 0, 0, 0, 42, 8) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 42, 8))
    0000   0x08 0x2a 0x00 0x00 0x00                   .*...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 Base (2000, 4, 18, 18, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x32                                  .2
    decimal
              0   50
    datetime ((2000, 4, 18, 18, 1, 61))
    0000   0x7d 0x01 0x32 0x32 0x00                   }.22.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 15 Base (2012, 4, 10, 13, 24, 15) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0xb8                                  h.
    decimal
            104  184
    datetime ((2012, 4, 10, 13, 24, 15))
    0000   0x4f 0x18 0x0d 0x0a 0x0c                   O....
    body (0)

#### RECORD 16 Base (2012, 0, 27, 13, 24, 50) head[2], body[0] op[0x5a]

    op hex (2)
    0000   0x5a 0x8f                                  Z.
    decimal
             90  143
    datetime ((2012, 0, 27, 13, 24, 50))
    0000   0x32 0x18 0x8d 0x5b 0x0c                   2..[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 17 Base (2001, 0, 0, 13, 24, 18) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x8f                                  b.
    decimal
             98  143
    datetime ((2001, 0, 0, 13, 24, 18))
    0000   0x12 0x18 0x0d 0x00 0x51                   ....Q
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 18 Base (2000, 4, 0, 0, 31, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 31, 42))
    0000   0x6a 0x1f 0x00 0x00 0x00                   j....
    body (0)

#### RECORD 19 Base (2008, 1, 5, 28, 61, 14) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x00                                  ..
    decimal
             17    0
    datetime ((2008, 1, 5, 28, 61, 14))
    0000   0x0e 0x7d 0x5c 0x05 0xc8                   .}\..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 20 Base (2002, 0, 0, 12, 12, 1) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x04                                  ..
    decimal
            141    4
    datetime ((2002, 0, 0, 12, 12, 1))
    0000   0x01 0x0c 0x0c 0x00 0x62                   ....b
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 21 Base (2000, 0, 0, 7, 13, 24) head[2], body[0] op[0x8f]

    op hex (2)
    0000   0x8f 0x52                                  .R
    decimal
            143   82
    datetime ((2000, 0, 0, 7, 13, 24))
    0000   0x18 0x0d 0x07 0x00 0x00                   .....
    body (0)

#### RECORD 22 Base (2013, 4, 24, 13, 13, 56) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x6c                                  .l
    decimal
              4  108
    datetime ((2013, 4, 24, 13, 13, 56))
    0000   0x78 0x0d 0x6d 0x78 0x0d                   x.mx.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 23 Base (2000, 14, 2, 12, 36, 24) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x10                                  ..
    decimal
              5   16
    datetime ((2000, 14, 2, 12, 36, 24))
    0000   0xd8 0xa4 0x0c 0x02 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 Base (2000, 4, 14, 20, 3, 44) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2000, 4, 14, 20, 3, 44))
    0000   0x6c 0x03 0x74 0x4e 0x00                   l.tN.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 25 Base (2006, 0, 24, 0, 55, 0) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0x16                                  ..
    decimal
            248   22
    datetime ((2006, 0, 24, 0, 55, 0))
    0000   0x00 0x37 0x00 0xf8 0x16                   .7...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 26 Base (2000, 4, 0, 16, 0, 4) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xa8                                  ..
    decimal
              0  168
    datetime ((2000, 4, 0, 16, 0, 4))
    0000   0x44 0x00 0x50 0x20 0x00                   D.P .
    body (0)
    DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-9.data: 27 records`
