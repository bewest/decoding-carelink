## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 64, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0x46 0x83 0x0d 0x00 0x00 0x00 0x6e    .F.....n
    0008   0x83 0x0d 0x05 0x00 0xa2 0x00 0x00 0x02    ........
    0010   0x00 0x00 0x04 0x46 0x02 0xbe 0x40 0x01    ...F..@.
    0018   0x88 0x24 0x00 0x32 0x00 0x58 0x00 0x00    .$.2.X..
##### DEBUG DECIMAL
              4   70  131   13    0    0    0  110
            131   13    5    0  162    0    0    2
              0    0    4   70    2  190   64    1
            136   36    0   50    0   88    0    0
#### RECORD 0 BolusWizard 2013-08-03T17:45:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-03T17:45:10)
    0000   0x8a 0x2d 0x11 0x03 0x0d                   .-...
    body (13)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x58 0x00 0x00 0x0c 0x00                   X....
    decimal
             22   80    0  100   60  100    0    0
             88    0    0   12    0
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Base (2000, 4, 16, 18, 11, 28) head[2], body[0] op[0x58]

    op hex (2)
    0000   0x58 0x78                                  Xx
    decimal
             88  120
    datetime ((2000, 4, 16, 18, 11, 28))
    0000   0x5c 0x0b 0x12 0x70 0xc0                   \..p.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 2 TempBasalDuration (2001, 14, 16, 2, 24, 0) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 3660}
```
    op hex (2)
    0000   0x16 0x7a                                  .z
    decimal
             22  122
    datetime ((2001, 14, 16, 2, 24, 0))
    0000   0xc0 0x98 0x42 0xd0 0x01                   ..B..
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 1, 0]
#### RECORD 3 Base (2000, 1, 12, 0, 24, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x58                                  .X
    decimal
              0   88
    datetime ((2000, 1, 12, 0, 24, 0))
    0000   0x00 0x58 0x00 0x0c 0x00                   .X...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 Base (2010, 4, 19, 13, 3, 17) head[2], body[0] op[0x8a]

    op hex (2)
    0000   0x8a 0x2d                                  .-
    decimal
            138   45
    datetime ((2010, 4, 19, 13, 3, 17))
    0000   0x51 0x03 0x0d 0x33 0x5a                   Q..3Z
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 5 Base (2006, 0, 8, 13, 3, 19) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x09                                  ..
    decimal
            128    9
    datetime ((2006, 0, 8, 13, 3, 19))
    0000   0x13 0x03 0x0d 0x08 0x16                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 6 Base (2007, 0, 13, 3, 19, 9) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x80                                  0.
    decimal
             48  128
    datetime ((2007, 0, 13, 3, 19, 9))
    0000   0x09 0x13 0x03 0x0d 0x07                   .....
    body (0)

`end logs/ReadHistoryData-page-15.data: 7 records`
