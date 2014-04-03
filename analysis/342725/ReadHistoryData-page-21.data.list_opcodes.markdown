## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 80, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x05 0x04 0x01 0x00 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x1e 0x00 0x5e 0x46 0x11    .....^F.
    0010   0x02 0x0d 0x1f 0x00 0x47 0x5e 0x11 0x02    ....G^..
    0018   0x0d 0x0a 0x5f 0x6c 0x58 0x32 0x02 0x0d    .._lX2..
##### DEBUG DECIMAL
              5    4    1    0    0   12    0  232
              0    0    0   30    0   94   70   17
              2   13   31    0   71   94   17    2
             13   10   95  108   88   50    2   13
#### RECORD 0 BolusWizard 2013-05-01T19:02:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-05-01T19:02:25)
    0000   0x59 0x42 0x13 0x01 0x0d                   YB...
    body (15)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d 0x5c 0x0b         ....}\.
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125   92   11
    HOUR BITS: [0, 1, 0]
#### RECORD 1 Base (2000, 0, 4, 2, 32, 4) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x30                                  p0
    decimal
            112   48
    datetime ((2000, 0, 4, 2, 32, 4))
    0000   0x04 0x20 0x62 0x04 0x20                   . b. 
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 2 Base (2009, 0, 0, 11, 11, 1) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x04                                  ..
    decimal
            208    4
    datetime ((2009, 0, 0, 11, 11, 1))
    0000   0x01 0x0b 0x0b 0x00 0x59                   ....Y
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 3 Base (2000, 0, 0, 7, 13, 1) head[2], body[0] op[0x42]

    op hex (2)
    0000   0x42 0x53                                  BS
    decimal
             66   83
    datetime ((2000, 0, 0, 7, 13, 1))
    0000   0x01 0x0d 0x07 0x00 0x00                   .....
    body (0)

#### RECORD 4 Base (2013, 6, 1, 13, 13, 1) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0xb8                                  ..
    decimal
              4  184
    datetime ((2013, 6, 1, 13, 13, 1))
    0000   0x41 0x8d 0x6d 0x41 0x8d                   A.mA.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 Base (2000, 9, 6, 23, 6, 18) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 9, 6, 23, 6, 18))
    0000   0x92 0x46 0xf7 0x06 0x00                   .F...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 Base (2001, 8, 10, 24, 3, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2001, 8, 10, 24, 3, 56))
    0000   0xb8 0x03 0x78 0x4a 0x01                   ..xJ.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2010, 1, 0, 1, 20, 0) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x1a                                  @.
    decimal
             64   26
    datetime ((2010, 1, 0, 1, 20, 0))
    0000   0x00 0x54 0x01 0x40 0x1a                   .T.@.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 8 Base (2000, 4, 31, 4, 0, 5) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xdc                                  ..
    decimal
              0  220
    datetime ((2000, 4, 31, 4, 0, 5))
    0000   0x45 0x00 0x64 0x1f 0x00                   E.d..
    body (0)

`end logs/ReadHistoryData-page-21.data: 9 records`
