## START logs/ReadHistoryData-page-17.data
#### STOPPING DOUBLE NULLS @ 152, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x60 0x00 0x00 0x00 0x00 0x60 0x36 0x5c    `....`6\
    0008   0x23 0x58 0x45 0x04 0x24 0x77 0x04 0x2c    #XE.$w.,
    0010   0x81 0x04 0x06 0x95 0x04 0x52 0x9f 0x04    .....R..
    0018   0x38 0xbd 0x04 0x32 0x67 0x14 0x46 0x71    8..2g.Fq
##### DEBUG DECIMAL
             96    0    0    0    0   96   54   92
             35   88   69    4   36  119    4   44
            129    4    6  149    4   82  159    4
             56  189    4   50  103   20   70  113
#### RECORD 0 BolusWizard 2012-08-20T16:43:17 head[2], body[15] op[0x5b]
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
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 0.15, 'curve': 4},
 {'age': 39, 'amount': 2.05, 'curve': 4},
 {'age': 69, 'amount': 1.4, 'curve': 4},
 {'age': 239, 'amount': 1.25, 'curve': 4},
 {'age': 249, 'amount': 1.75, 'curve': 4},
 {'age': 13, 'amount': 3.1, 'curve': 20},
 {'age': 23, 'amount': 1.3, 'curve': 20},
 {'age': 93, 'amount': 1.2, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x06 0x1d 0x04 0x52 0x27 0x04    \....R'.
    0008   0x38 0x45 0x04 0x32 0xef 0x04 0x46 0xf9    8E.2..F.
    0010   0x04 0x7c 0x0d 0x14 0x34 0x17 0x14 0x30    .|..4..0
    0018   0x5d 0x14                                  ].
    decimal
             92   26    6   29    4   82   39    4
             56   69    4   50  239    4   70  249
              4  124   13   20   52   23   20   48
             93   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2012-08-20T16:43:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x80 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  128    0
    datetime (2012-08-20T16:43:17)
    0000   0x91 0x2b 0x50 0x74 0x0c                   .+Pt.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2012-08-20T17:35:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T17:35:22)
    0000   0x96 0x23 0x11 0x74 0x0c                   .#.t.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 0.9, 'curve': 4},
 {'age': 61, 'amount': 1.1, 'curve': 4},
 {'age': 81, 'amount': 0.15, 'curve': 4},
 {'age': 91, 'amount': 2.05, 'curve': 4},
 {'age': 121, 'amount': 1.4, 'curve': 4},
 {'age': 35, 'amount': 1.25, 'curve': 20},
 {'age': 45, 'amount': 1.75, 'curve': 20},
 {'age': 65, 'amount': 3.1, 'curve': 20},
 {'age': 75, 'amount': 1.3, 'curve': 20},
 {'age': 145, 'amount': 1.2, 'curve': 20}]
```
    op hex (32)
    0000   0x5c 0x20 0x24 0x33 0x04 0x2c 0x3d 0x04    \ $3.,=.
    0008   0x06 0x51 0x04 0x52 0x5b 0x04 0x38 0x79    .Q.R[.8y
    0010   0x04 0x32 0x23 0x14 0x46 0x2d 0x14 0x7c    .2#.F-.|
    0018   0x41 0x14 0x34 0x4b 0x14 0x30 0x91 0x14    A.4K.0..
    decimal
             92   32   36   51    4   44   61    4
              6   81    4   82   91    4   56  121
              4   50   35   20   70   45   20  124
             65   20   52   75   20   48  145   20
    datetime (unknown)

    body (0)

#### RECORD 5 Base (2012, 8, 20, 17, 35, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2012, 8, 20, 17, 35, 22))
    0000   0x96 0x23 0x71 0x14 0x0c                   .#q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 Base (2008, 0, 0, 24, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2008, 0, 0, 24, 0, 1))
    0000   0x01 0x00 0x58 0x00 0x58                   ..X.X
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 7 Base (2004, 2, 17, 3, 22, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x98                                  ..
    decimal
              0  152
    datetime ((2004, 2, 17, 3, 22, 0))
    0000   0x00 0x96 0x23 0x51 0x74                   ..#Qt
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 8 ClearAlarm 2004-02-18T11:02:00 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x5b                                  .[
    decimal
             12   91
    datetime (2004-02-18T11:02:00)
    0000   0x00 0x82 0x2b 0x12 0x74                   ..+.t
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 9 ClearAlarm 2006-08-23T14:00:16 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x1b                                  ..
    decimal
             12   27
    datetime (2006-08-23T14:00:16)
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-17.data: 10 records`
