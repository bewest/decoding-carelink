## START logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 188, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x08 0x00 0x80 0x64 0x5c 0x11 0x50 0x6e    ...d\.Pn
    0008   0x80 0x74 0x82 0x80 0x10 0x8c 0x80 0x64    .t.....d
    0010   0xc8 0x80 0x48 0xd2 0x80 0x01 0x00 0x80    ..H.....
    0018   0x00 0x80 0x00 0x08 0x00 0x1e 0xf4 0x54    .......T
##### DEBUG DECIMAL
              8    0  128  100   92   17   80  110
            128  116  130  128   16  140  128  100
            200  128   72  210  128    1    0  128
              0  128    0    8    0   30  244   84
#### RECORD 0 BolusWizard 2014-03-09T18:41:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 166,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 5.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa6                                  [.
    decimal
             91  166
    datetime (2014-03-09T18:41:05)
    0000   0x05 0xe9 0x12 0x09 0x0e                   .....
    body (13)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x34 0x00    .P.x2P4.
    0008   0x00 0x00 0x00 0x38 0x00                   ...8.
    decimal
              0   80    0  120   50   80   52    0
              0    0    0   56    0
    HOUR BITS: [1, 1, 1]
#### RECORD 1 Base (2000, 4, 5, 4, 8, 28) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x64                                  .d
    decimal
              0  100
    datetime ((2000, 4, 5, 4, 8, 28))
    0000   0x5c 0x08 0x64 0x45 0x80                   \.dE.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 Base (2000, 8, 16, 0, 1, 0) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x4f                                  HO
    decimal
             72   79
    datetime ((2000, 8, 16, 0, 1, 0))
    0000   0x80 0x01 0x00 0x10 0x00                   .....
    body (0)

#### RECORD 3 Base (2002, 0, 9, 5, 0, 56) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2002, 0, 9, 5, 0, 56))
    0000   0x38 0x00 0x05 0xe9 0x52                   8...R
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 4 Base (2002, 6, 14, 18, 38, 27) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x0e                                  ..
    decimal
              9   14
    datetime ((2002, 6, 14, 18, 38, 27))
    0000   0x5b 0xa6 0x12 0xee 0x12                   [....
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 Ian69 2002-01-24T00:16:35 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0e                                  i.
    decimal
            105   14
    datetime (2002-01-24T00:16:35)
    0000   0x23 0x50 0x00 0x78 0x32                   #P.x2
    body (2)
    hex
    0000   0x50 0x34                                  P4
    decimal
             80   52
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 6 Base (2004, 0, 0, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x74                                  .t
    decimal
              0  116
    datetime ((2004, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x40 0x00 0x74                   ..@.t
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 7 ChangeTimeDisplay (2004, 0, 0, 14, 16, 11) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x5c                                  d\
    decimal
            100   92
    datetime ((2004, 0, 0, 14, 16, 11))
    0000   0x0b 0x10 0x0e 0x80 0x64                   ....d
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 8 Base (2000, 5, 1, 0, 20, 8) head[2], body[0] op[0x4a]

    op hex (2)
    0000   0x4a 0x80                                  J.
    decimal
             74  128
    datetime ((2000, 5, 1, 0, 20, 8))
    0000   0x48 0x54 0x80 0x01 0x00                   HT...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 9 Base (2002, 4, 0, 0, 0, 52) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0x00                                  t.
    decimal
            116    0
    datetime ((2002, 4, 0, 0, 0, 52))
    0000   0x74 0x00 0x40 0x00 0x12                   t.@..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 Base (2007, 4, 0, 27, 14, 41) head[2], body[0] op[0xee]

    op hex (2)
    0000   0xee 0x52                                  .R
    decimal
            238   82
    datetime ((2007, 4, 0, 27, 14, 41))
    0000   0x69 0x0e 0x5b 0x00 0x07                   i.[..
    body (0)

#### RECORD 11 Base (2000, 4, 16, 22, 14, 41) head[2], body[0] op[0xca]

    op hex (2)
    0000   0xca 0x13                                  ..
    decimal
            202   19
    datetime ((2000, 4, 16, 22, 14, 41))
    0000   0x69 0x0e 0x16 0x50 0x00                   i..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 Sara6E 2000-02-19T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2000-02-19T00:00:00)
    0000   0x32 0x50                                  2P
    body (49)
    hex
    0000   0x00 0x00 0x50 0x00 0x00 0x00 0x00 0x50    ..P....P
    0008   0x64 0x5c 0x0e 0x74 0x1c 0x80 0x10 0x26    d\.t...&
    0010   0x80 0x64 0x62 0x80 0x48 0x6c 0x80 0x01    .db.Hl..
    0018   0x00 0x50 0x00 0x50 0x00 0x84 0x00 0x07    .P.P....
    0020   0xca 0x53 0x69 0x0e 0x06 0x3b 0x01 0x08    .Si..;..
    0028   0x1a 0xce 0x73 0xc9 0x0e 0x0c 0x3b 0x09    ..s...;.
    0030   0xd3                                       .
    decimal
              0    0   80    0    0    0    0   80
            100   92   14  116   28  128   16   38
            128  100   98  128   72  108  128    1
              0   80    0   80    0  132    0    7
            202   83  105   14    6   59    1    8
             26  206  115  201   14   12   59    9
            211
    HOUR BITS: [0, 1, 0]
#### RECORD 13 Base (2003, 1, 9, 4, 59, 14) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x09                                  ..
    decimal
             19    9
    datetime ((2003, 1, 9, 4, 59, 14))
    0000   0x0e 0x7b 0x04 0x09 0xd3                   .{...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 14 Base (2010, 0, 0, 16, 21, 14) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x09                                  ..
    decimal
             19    9
    datetime ((2010, 0, 0, 16, 21, 14))
    0000   0x0e 0x15 0x10 0x00 0x0a                   .....
    body (0)

#### RECORD 15 Base (2011, 12, 14, 9, 52, 52) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x1c                                  ..
    decimal
             15   28
    datetime ((2011, 12, 14, 9, 52, 52))
    0000   0xf4 0x34 0x09 0x8e 0x5b                   .4..[
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 16 Base (2000, 12, 14, 9, 20, 52) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x1e                                  ..
    decimal
             15   30
    datetime ((2000, 12, 14, 9, 20, 52))
    0000   0xf4 0x14 0x69 0x0e 0x00                   ..i..
    body (0)

#### RECORD 17 Base (2000, 4, 8, 16, 50, 46) head[2], body[0] op[0x51]

    op hex (2)
    0000   0x51 0x00                                  Q.
    decimal
             81    0
    datetime ((2000, 4, 8, 16, 50, 46))
    0000   0x6e 0x32 0x50 0x88 0x00                   n2P..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-5.data: 18 records`
