## START logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 136, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0xbc 0x03 0x84 0x4a 0x01 0x38 0x1a    ....J.8.
    0008   0x00 0x4c 0x01 0x38 0x1a 0x00 0xe8 0x4a    .L.8...J
    0010   0x00 0x50 0x1a 0x00 0x00 0x00 0x04 0x02    .P......
    0018   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
##### DEBUG DECIMAL
              4  188    3  132   74    1   56   26
              0   76    1   56   26    0  232   74
              0   80   26    0    0    0    4    2
              2    0    0   12    0  232    0    0
#### RECORD 0 BolusWizard 2013-04-20T22:40:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 176,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2013-04-20T22:40:40)
    0000   0x68 0x28 0x16 0x14 0x0d                   h(...
    body (15)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x04 0x7d 0x5c 0x05         ....}\.
    decimal
              0   80   13   45  106   11    0    0
              0    7    0    4  125   92    5
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Base (2000, 0, 4, 4, 1, 4) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x7e                                  @~
    decimal
             64  126
    datetime ((2000, 0, 4, 4, 1, 4))
    0000   0x04 0x01 0x04 0x04 0x00                   .....
    body (0)

#### RECORD 2 Base (2001, 4, 10, 13, 20, 22) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x28                                  h(
    decimal
            104   40
    datetime ((2001, 4, 10, 13, 20, 22))
    0000   0x56 0x14 0x0d 0x0a 0xb1                   V....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 3 Base (2001, 0, 27, 13, 20, 54) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x2e                                  r.
    decimal
            114   46
    datetime ((2001, 0, 27, 13, 20, 54))
    0000   0x36 0x14 0x0d 0x5b 0xb1                   6..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 4 Base (2000, 0, 28, 13, 20, 22) head[2], body[0] op[0x47]

    op hex (2)
    0000   0x47 0x2f                                  G/
    decimal
             71   47
    datetime ((2000, 0, 28, 13, 20, 22))
    0000   0x16 0x14 0x0d 0x3c 0x50                   ...<P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 5 Base (2000, 4, 0, 14, 11, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 14, 11, 42))
    0000   0x6a 0x0b 0x2e 0x00 0x00                   j....
    body (0)

#### RECORD 6 Ian0B (2013, 5, 16, 8, 28, 61) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x00 0x2e                             ...
    decimal
             11    0   46
    datetime ((2013, 5, 16, 8, 28, 61))
    0000   0x7d 0x5c 0x08 0x10 0x0d                   }\...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 Base (2014, 8, 14, 1, 4, 5) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x40                                  .@
    decimal
              4   64
    datetime ((2014, 8, 14, 1, 4, 5))
    0000   0x85 0x04 0x01 0x2e 0x2e                   .....
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 8 Base (2011, 1, 13, 20, 22, 47) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x47                                  .G
    decimal
              0   71
    datetime ((2011, 1, 13, 20, 22, 47))
    0000   0x2f 0x56 0x14 0x0d 0x5b                   /V..[
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 9 Base (2000, 0, 13, 20, 23, 10) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x64                                  .d
    decimal
              0  100
    datetime ((2000, 0, 13, 20, 23, 10))
    0000   0x0a 0x17 0x14 0x0d 0x10                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 Ian50 2000-01-12T00:42:45 head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime (2000-01-12T00:42:45)
    0000   0x2d 0x6a 0x00 0x0c 0x00                   -j...
    body (34)
    hex
    0000   0x00 0x00 0x00 0x0c 0x7d 0x5c 0x0b 0xb8    ....}\..
    0008   0x1a 0x04 0x10 0x24 0x04 0x40 0x9c 0x04    ...$.@..
    0010   0x01 0x0c 0x0c 0x00 0x64 0x0a 0x57 0x14    ....d.W.
    0018   0x0d 0x07 0x00 0x00 0x04 0xbc 0x54 0x0d    ......T.
    0020   0x6d 0x54                                  mT
    decimal
              0    0    0   12  125   92   11  184
             26    4   16   36    4   64  156    4
              1   12   12    0  100   10   87   20
             13    7    0    0    4  188   84   13
            109   84
    HOUR BITS: [0, 1, 1]
#### RECORD 11 Base (2003, 2, 9, 16, 57, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x05                                  ..
    decimal
             13    5
    datetime ((2003, 2, 9, 16, 57, 0))
    0000   0x00 0xb9 0xb0 0xc9 0x03                   .....
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-25.data: 12 records`
