## START logs/ReadHistoryData-page-17.data
#### STOPPING DOUBLE NULLS @ 80, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x58 0x36 0x5c 0x20 0x24 0x33 0x04 0x2c    X6\ $3.,
    0008   0x3d 0x04 0x06 0x51 0x04 0x52 0x5b 0x04    =..Q.R[.
    0010   0x38 0x79 0x04 0x32 0x23 0x14 0x46 0x2d    8y.2#.F-
    0018   0x14 0x7c 0x41 0x14 0x34 0x4b 0x14 0x30    .|A.4K.0
##### DEBUG DECIMAL
             88   54   92   32   36   51    4   44
             61    4    6   81    4   82   91    4
             56  121    4   50   35   20   70   45
             20  124   65   20   52   75   20   48
#### RECORD 0 BolusWizard 2012-08-20T16:43:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T16:43:17)
    0000   0x91 0x2b 0x10 0x74 0x0c                   .+.t.
    body (13)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00                   P....
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2004, 4, 29, 6, 26, 28) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x36                                  P6
    decimal
             80   54
    datetime ((2004, 4, 29, 6, 26, 28))
    0000   0x5c 0x1a 0x06 0x1d 0x04                   \....
    body (0)

#### RECORD 2 Base (2002, 0, 4, 5, 56, 4) head[2], body[0] op[0x52]

    op hex (2)
    0000   0x52 0x27                                  R'
    decimal
             82   39
    datetime ((2002, 0, 4, 5, 56, 4))
    0000   0x04 0x38 0x45 0x04 0x32                   .8E.2
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 3 Base (2013, 7, 28, 4, 57, 6) head[2], body[0] op[0xef]

    op hex (2)
    0000   0xef 0x04                                  ..
    decimal
            239    4
    datetime ((2013, 7, 28, 4, 57, 6))
    0000   0x46 0xf9 0x04 0x7c 0x0d                   F..|.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 SelectBasalProfile (2004, 0, 29, 16, 20, 23) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x34                                  .4
    decimal
             20   52
    datetime ((2004, 0, 29, 16, 20, 23))
    0000   0x17 0x14 0x30 0x5d 0x14                   ..0].
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 Bolus (2001, 4, 0, 0, 0, 16) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x50 0x00                        ..P.
    decimal
              1    0   80    0
    datetime ((2001, 4, 0, 0, 0, 16))
    0000   0x50 0x00 0x80 0x00 0x91                   P....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 6 Base (2006, 4, 0, 27, 12, 52) head[2], body[0] op[0x2b]

    op hex (2)
    0000   0x2b 0x50                                  +P
    decimal
             43   80
    datetime ((2006, 4, 0, 27, 12, 52))
    0000   0x74 0x0c 0x5b 0x00 0x96                   t.[..
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 7 Base (2000, 4, 16, 25, 12, 52) head[2], body[0] op[0x23]

    op hex (2)
    0000   0x23 0x11                                  #.
    decimal
             35   17
    datetime ((2000, 4, 16, 25, 12, 52))
    0000   0x74 0x0c 0x19 0x90 0x00                   t....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 8 Base (2000, 0, 24, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 24, 0, 0, 54))
    0000   0x36 0x00 0x00 0x58 0x00                   6..X.
    body (0)
    DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-17.data: 9 records`
