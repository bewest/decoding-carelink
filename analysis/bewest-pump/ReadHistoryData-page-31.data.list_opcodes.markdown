## START logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 192, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x54 0x78 0x5c 0x08 0x50 0xd5 0xc0 0x30    Tx\.P..0
    0008   0x25 0xd0 0x01 0x00 0x54 0x00 0x54 0x00    %...T.T.
    0010   0x00 0x00 0x5e 0xc7 0x57 0x68 0x0d 0x7b    ..^.Wh.{
    0018   0x00 0x40 0xc0 0x00 0x09 0x0d 0x00 0x1c    .@......
##### DEBUG DECIMAL
             84  120   92    8   80  213  192   48
             37  208    1    0   84    0   84    0
              0    0   94  199   87  104   13  123
              0   64  192    0    9   13    0   28
#### RECORD 0 BolusWizard 2013-07-08T14:27:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-07-08T14:27:24)
    0000   0x58 0xdb 0x0e 0x68 0x0d                   X..h.
    body (13)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x28 0x00 0x00 0x50 0x00                   (..P.
    decimal
             13   80    0  120   60  100   44    0
             40    0    0   80    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2000, 4, 13, 8, 17, 28) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x78                                  (x
    decimal
             40  120
    datetime ((2000, 4, 13, 8, 17, 28))
    0000   0x5c 0x11 0x28 0x0d 0xc0                   \.(..
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 2 Base (2000, 12, 0, 15, 44, 0) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x35                                  ,5
    decimal
             44   53
    datetime ((2000, 12, 0, 15, 44, 0))
    0000   0xc0 0x2c 0x8f 0xc0 0x40                   .,..@
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 3 ResultTotals (2000, 0, 0, 0, 0, 1) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0xd0 0x60 0x57 0xd0                   ..`W.
    decimal
              7  208   96   87  208
    datetime ((2000, 0, 0, 0, 0, 1))
    0000   0x01 0x00 0x60 0x00 0x60                   ..`.`
    body (41)
    hex
    0000   0x00 0x50 0x00 0x58 0xdb 0x4e 0x68 0x0d    .P.X.Nh.
    0008   0x0a 0x6d 0x54 0xd3 0x32 0x08 0x0d 0x5b    .mT.2..[
    0010   0x6d 0x59 0xd3 0x12 0x68 0x0d 0x0c 0x50    mY..h..P
    0018   0x00 0x64 0x3c 0x64 0x00 0x00 0x30 0x00    .d<d..0.
    0020   0x00 0x00 0x00 0x30 0x78 0x5c 0x0e 0x60    ...0x\.`
    0028   0xeb                                       .
    decimal
              0   80    0   88  219   78  104   13
             10  109   84  211   50    8   13   91
            109   89  211   18  104   13   12   80
              0  100   60  100    0    0   48    0
              0    0    0   48  120   92   14   96
            235
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 Base (2000, 15, 29, 12, 0, 53) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x28                                  .(
    decimal
            192   40
    datetime ((2000, 15, 29, 12, 0, 53))
    0000   0xf5 0xc0 0x2c 0x1d 0xd0                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 5 Base (2000, 12, 16, 0, 1, 16) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x77                                  ,w
    decimal
             44  119
    datetime ((2000, 12, 16, 0, 1, 16))
    0000   0xd0 0x01 0x00 0x30 0x00                   ...0.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 6 Base (2002, 0, 19, 26, 0, 0) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x00                                  0.
    decimal
             48    0
    datetime ((2002, 0, 19, 26, 0, 0))
    0000   0x00 0x00 0x5a 0xd3 0x52                   ..Z.R
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 7 Base (2003, 1, 2, 3, 55, 10) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x0d                                  h.
    decimal
            104   13
    datetime ((2003, 1, 2, 3, 55, 10))
    0000   0x0a 0x77 0x63 0xe2 0x33                   .wc.3
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 8 ChangeBasalProfile 2003-05-02T15:55:27 head[2], body[42] op[0x08]

    op hex (2)
    0000   0x08 0x0d                                  ..
    decimal
              8   13
    datetime (2003-05-02T15:55:27)
    0000   0x5b 0x77 0x6f 0xe2 0x13                   [wo..
    body (42)
    hex
    0000   0x08 0x0d 0x14 0x50 0x00 0x64 0x3c 0x64    ...P.d<d
    0008   0x00 0x00 0x50 0x00 0x00 0x1c 0x00 0x50    ..P....P
    0010   0x78 0x5c 0x11 0x30 0x50 0xc0 0x60 0x36    x\.0P.`6
    0018   0xd0 0x28 0x40 0xd0 0x2c 0x68 0xd0 0x2c    .(@.,h.,
    0020   0xc2 0xd0 0x01 0x00 0x50 0x00 0x50 0x00    ....P.P.
    0028   0x1c 0x00                                  ..
    decimal
              8   13   20   80    0  100   60  100
              0    0   80    0    0   28    0   80
            120   92   17   48   80  192   96   54
            208   40   64  208   44  104  208   44
            194  208    1    0   80    0   80    0
             28    0
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Base (2008, 4, 10, 13, 8, 19) head[2], body[0] op[0x6f]

    op hex (2)
    0000   0x6f 0xe2                                  o.
    decimal
            111  226
    datetime ((2008, 4, 10, 13, 8, 19))
    0000   0x53 0x08 0x0d 0x0a 0x88                   S....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 10 Base (2008, 0, 27, 13, 8, 55) head[2], body[0] op[0x51]

    op hex (2)
    0000   0x51 0xc7                                  Q.
    decimal
             81  199
    datetime ((2008, 0, 27, 13, 8, 55))
    0000   0x37 0x08 0x0d 0x5b 0x88                   7..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 11 Base (2000, 1, 19, 13, 40, 23) head[2], body[0] op[0x5d]

    op hex (2)
    0000   0x5d 0xc7                                  ].
    decimal
             93  199
    datetime ((2000, 1, 19, 13, 40, 23))
    0000   0x17 0x68 0x0d 0x13 0x50                   .h..P
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 12 Base (2012, 1, 0, 8, 36, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x64                                  .d
    decimal
              0  100
    datetime ((2012, 1, 0, 8, 36, 60))
    0000   0x3c 0x64 0x08 0x00 0x4c                   <d..L
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
`end logs/ReadHistoryData-page-31.data: 13 records`
