## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 78, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x44 0x00 0x00 0x78 0x5c 0x0b 0x40 0x2b    D..x\.@+
    0008   0xc0 0x4c 0x85 0xc0 0x6c 0xf3 0xc0 0x0a    .L..l...
    0010   0x71 0x5e 0xd5 0x2d 0x10 0x0d 0x5b 0x71    q^.-..[q
    0018   0x6f 0xd5 0x0d 0x70 0x0d 0x1a 0x50 0x00    o..p..P.
##### DEBUG DECIMAL
             68    0    0  120   92   11   64   43
            192   76  133  192  108  243  192   10
            113   94  213   45   16   13   91  113
            111  213   13  112   13   26   80    0
#### RECORD 0 BolusWizard 2013-07-16T11:44:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2013-07-16T11:44:50)
    0000   0x72 0xec 0x0b 0x10 0x0d                   r....
    body (13)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x08 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x24 0x00                   ...$.
    decimal
              0   80    0  120   60  100    8    0
              0    0    0   36    0
    HOUR BITS: [1, 1, 1]
#### RECORD 1 Base (2000, 4, 27, 12, 8, 28) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2000, 4, 27, 12, 8, 28))
    0000   0x5c 0x08 0x4c 0x5b 0xc0                   \.L[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 2 Base (2000, 12, 0, 0, 1, 0) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0xc9                                  l.
    decimal
            108  201
    datetime ((2000, 12, 0, 0, 1, 0))
    0000   0xc0 0x01 0x00 0x40 0x00                   ...@.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 3 Base (2011, 0, 12, 18, 0, 36) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime ((2011, 0, 12, 18, 0, 36))
    0000   0x24 0x00 0x72 0xec 0x4b                   $.r.K
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 4 Base (2012, 4, 0, 0, 3, 59) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x0d                                  ..
    decimal
             16   13
    datetime ((2012, 4, 0, 0, 3, 59))
    0000   0x7b 0x03 0x40 0xc0 0x0c                   {.@..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 5 Base (2008, 0, 10, 0, 29, 24) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x0d                                  ..
    decimal
             16   13
    datetime ((2008, 0, 10, 0, 29, 24))
    0000   0x18 0x1d 0x00 0x0a 0xc8                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 6 Base (2008, 0, 27, 13, 16, 44) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0xda                                  @.
    decimal
             64  218
    datetime ((2008, 0, 27, 13, 16, 44))
    0000   0x2c 0x10 0x0d 0x5b 0xc8                   ,..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 7 Base (2000, 0, 0, 13, 16, 12) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0xda                                  C.
    decimal
             67  218
    datetime ((2000, 0, 0, 13, 16, 12))
    0000   0x0c 0x10 0x0d 0x00 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 8 Base (2000, 1, 0, 20, 36, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2000, 1, 0, 20, 36, 60))
    0000   0x3c 0x64 0x34 0x00 0x00                   <d4..
    body (0)
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-24.data: 9 records`
