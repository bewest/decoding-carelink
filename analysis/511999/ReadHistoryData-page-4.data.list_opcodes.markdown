## START logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 159, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x58 0x78 0x01 0x00 0x58 0x00 0x58 0x00    Xx..X.X.
    0008   0x00 0x00 0xb2 0x18 0x57 0x1b 0x0d 0x7b    ....W..{
    0010   0x00 0x80 0x00 0x00 0x1c 0x0d 0x00 0x1d    ........
    0018   0x00 0x07 0x00 0x00 0x03 0xdc 0x9b 0x0d    ........
##### DEBUG DECIMAL
             88  120    1    0   88    0   88    0
              0    0  178   24   87   27   13  123
              0  128    0    0   28   13    0   29
              0    7    0    0    3  220  155   13
#### RECORD 0 BolusWizard 2013-08-27T12:33:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-08-27T12:33:02)
    0000   0x82 0x21 0x0c 0x1b 0x0d                   .!...
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x78         0....0x
    decimal
             15   80    0  120   60  100    0    0
             48    0    0    0    0   48  120
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Bolus (2002, 0, 0, 0, 0, 48) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x30 0x00                        ..0.
    decimal
              1    0   48    0
    datetime ((2002, 0, 0, 0, 0, 48))
    0000   0x30 0x00 0x00 0x00 0x82                   0....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 Rewind (2008, 0, 31, 10, 13, 27) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x4c                                  !L
    decimal
             33   76
    datetime ((2008, 0, 31, 10, 13, 27))
    0000   0x1b 0x0d 0x0a 0x7f 0xb8                   .....
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 3 Base (2001, 0, 31, 27, 13, 27) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0x2d                                  .-
    decimal
             18   45
    datetime ((2001, 0, 31, 27, 13, 27))
    0000   0x1b 0x0d 0x5b 0x7f 0x81                   ..[..
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 Base (2000, 0, 16, 13, 13, 27) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x0d                                  ..
    decimal
             19   13
    datetime ((2000, 0, 16, 13, 13, 27))
    0000   0x1b 0x0d 0x0d 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 5 Base (2000, 4, 8, 0, 4, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 4, 8, 0, 4, 36))
    0000   0x64 0x04 0x00 0x28 0x00                   d..(.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 6 Base (2005, 0, 28, 24, 40, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x28                                  .(
    decimal
              0   40
    datetime ((2005, 0, 28, 24, 40, 0))
    0000   0x00 0x28 0x78 0x5c 0x05                   .(x\.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2000, 12, 8, 0, 1, 0) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x2e                                  0.
    decimal
             48   46
    datetime ((2000, 12, 8, 0, 1, 0))
    0000   0xc0 0x01 0x00 0x28 0x00                   ...(.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 8 Base (2013, 0, 19, 1, 0, 40) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x00                                  (.
    decimal
             40    0
    datetime ((2013, 0, 19, 1, 0, 40))
    0000   0x28 0x00 0x81 0x13 0x4d                   (...M
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 9 Base (2014, 0, 29, 25, 38, 10) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x0d                                  ..
    decimal
             27   13
    datetime ((2014, 0, 29, 25, 38, 10))
    0000   0x0a 0x26 0xb9 0x1d 0x2e                   .&...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 10 Base (2014, 4, 29, 27, 38, 27) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x8d                                  ..
    decimal
             27  141
    datetime ((2014, 4, 29, 27, 38, 27))
    0000   0x5b 0x26 0xbb 0x1d 0x0e                   [&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 Base (2012, 1, 24, 0, 17, 0) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x0d                                  ..
    decimal
             27   13
    datetime ((2012, 1, 24, 0, 17, 0))
    0000   0x00 0x51 0x00 0x78 0x3c                   .Q.x<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 12 ChangeTimeDisplay (2004, 0, 0, 0, 0, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x74                                  dt
    decimal
            100  116
    datetime ((2004, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x24                   ....$
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 13 Base (2012, 5, 8, 8, 28, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x50                                  .P
    decimal
              0   80
    datetime ((2012, 5, 8, 8, 28, 56))
    0000   0x78 0x5c 0x08 0x28 0x4c                   x\.(L
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 14 Base (2000, 7, 0, 1, 0, 52) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x30                                  .0
    decimal
            192   48
    datetime ((2000, 7, 0, 1, 0, 52))
    0000   0x74 0xc0 0x01 0x00 0x50                   t...P
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 15 Base (2013, 0, 27, 0, 36, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x50                                  .P
    decimal
              0   80
    datetime ((2013, 0, 27, 0, 36, 0))
    0000   0x00 0x24 0x00 0xbb 0x1d                   .$...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 16 Base (2008, 0, 14, 0, 10, 13) head[2], body[0] op[0x4e]

    op hex (2)
    0000   0x4e 0x1b                                  N.
    decimal
             78   27
    datetime ((2008, 0, 14, 0, 10, 13))
    0000   0x0d 0x0a 0x00 0xae 0x18                   .....
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 17 Base (2008, 9, 18, 0, 27, 13) head[2], body[0] op[0x37]

    op hex (2)
    0000   0x37 0x1b                                  7.
    decimal
             55   27
    datetime ((2008, 9, 18, 0, 27, 13))
    0000   0x8d 0x5b 0x00 0xb2 0x18                   .[...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 18 ChangeTime (2004, 0, 0, 17, 0, 13) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x1b                                  ..
    decimal
             23   27
    datetime ((2004, 0, 0, 17, 0, 13))
    0000   0x0d 0x00 0x51 0x00 0x64                   ..Q.d
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 Base (2000, 4, 0, 0, 0, 24) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x64                                  <d
    decimal
             60  100
    datetime ((2000, 4, 0, 0, 0, 24))
    0000   0x58 0x00 0x00 0x00 0x00                   X....
    body (0)

`end logs/ReadHistoryData-page-4.data: 20 records`
