## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 332, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0x66 0x70 0x0d 0x6d 0x70 0x0d 0x05    .fp.mp..
    0008   0x00 0x68 0x38 0x93 0x09 0x00 0x00 0x04    .h8.....
    0010   0x66 0x03 0x7a 0x4f 0x00 0xec 0x15 0x00    f.zO....
    0018   0x53 0x00 0xec 0x15 0x00 0xec 0x64 0x00    S.....d.
##### DEBUG DECIMAL
              4  102  112   13  109  112   13    5
              0  104   56  147    9    0    0    4
            102    3  122   79    0  236   21    0
             83    0  236   21    0  236  100    0
#### RECORD 0 BolusWizard 2013-06-15T16:40:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 17,
 '_byte[7]': 0,
 'bg': 202,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 4.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xca                                  [.
    decimal
             91  202
    datetime (2013-06-15T16:40:15)
    0000   0x4f 0xa8 0x10 0x0f 0x0d                   O....
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0x11 0x2d 0x00    ;P.-j.-.
    0008   0x00 0x00 0x00 0x3e 0x7d                   ...>}
    decimal
             59   80   13   45  106   17   45    0
              0    0    0   62  125
    HOUR BITS: [1, 0, 1]
#### RECORD 1 Bolus 2013-06-15T16:40:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.1, 'dual_component': '??', 'programmed': 6.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3d 0x3d 0x00                        .==.
    decimal
              1   61   61    0
    datetime (2013-06-15T16:40:15)
    0000   0x4f 0xa8 0x50 0x0f 0x0d                   O.P..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2013-06-15T18:12:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-06-15T18:12:00)
    0000   0x40 0x8c 0x32 0x0f 0x0d                   @.2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 CalBGForPH 2013-06-15T19:29:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 173}
```
    op hex (2)
    0000   0x0a 0xad                                  ..
    decimal
             10  173
    datetime (2013-06-15T19:29:31)
    0000   0x5f 0x9d 0x33 0x0f 0x0d                   _.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 CalBGForPH 2013-06-15T20:58:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-06-15T20:58:47)
    0000   0x6f 0xba 0x34 0x0f 0x0d                   o.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 5 BolusWizard 2013-06-15T20:59:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-06-15T20:59:47)
    0000   0x6f 0xbb 0x14 0x0f 0x0d                   o....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x02 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             18   80   13   45  106    2   13    0
              0    0    0   15  125
    HOUR BITS: [1, 0, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 255, 'amount': 0.5, 'curve': 4},
 {'age': 9, 'amount': 5.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0xff 0x04 0xe0 0x09 0x14    \.......
    decimal
             92    8   20  255    4  224    9   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-06-15T20:59:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-06-15T20:59:47)
    0000   0x6f 0xbb 0x54 0x0f 0x0d                   o.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 8 ResultTotals 2013-04-15T13:13:47 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xaa                   .....
    decimal
              7    0    0    4  170
    datetime (2013-04-15T13:13:47)
    0000   0x6f 0x0d 0x6d 0x6f 0x0d                   o.mo.
    body (51)
    hex
    0000   0x05 0x00 0xb0 0x89 0xca 0x04 0x00 0x00    ........
    0008   0x04 0xaa 0x03 0x7a 0x4b 0x01 0x30 0x19    ...zK.0.
    0010   0x00 0x4d 0x01 0x30 0x19 0x00 0xe8 0x4c    .M.0...L
    0018   0x00 0x48 0x18 0x00 0x00 0x00 0x02 0x00    .H......
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x67 0x80 0x0a 0x10 0x0d    ...g....
    0030   0x1f 0x00 0x48                             ..H
    decimal
              5    0  176  137  202    4    0    0
              4  170    3  122   75    1   48   25
              0   77    1   48   25    0  232   76
              0   72   24    0    0    0    2    0
              0    2    0   12    0  232    0    0
              0   30    0  103  128   10   16   13
             31    0   72
    DAY BITS: [0, 1, 1]
#### RECORD 9 Base (2000, 0, 30, 10, 13, 16) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x0a                                  ..
    decimal
            144   10
    datetime ((2000, 0, 30, 10, 13, 16))
    0000   0x10 0x0d 0x0a 0x7e 0x60                   ...~`
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 10 Base (2007, 0, 30, 27, 13, 16) head[2], body[0] op[0xa6]

    op hex (2)
    0000   0xa6 0x2c                                  .,
    decimal
            166   44
    datetime ((2007, 0, 30, 27, 13, 16))
    0000   0x10 0x0d 0x5b 0x7e 0x57                   ..[~W
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 11 Base (2013, 0, 16, 4, 13, 16) head[2], body[0] op[0xa7]

    op hex (2)
    0000   0xa7 0x0c                                  ..
    decimal
            167   12
    datetime ((2013, 0, 16, 4, 13, 16))
    0000   0x10 0x0d 0x24 0x50 0x0d                   ..$P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 Base (2000, 0, 0, 0, 27, 0) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 27, 0))
    0000   0x00 0x1b 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 13 Base (2000, 4, 27, 27, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1b                                  ..
    decimal
              0   27
    datetime ((2000, 4, 27, 27, 1, 61))
    0000   0x7d 0x01 0x1b 0x1b 0x00                   }....
    body (0)

#### RECORD 14 Base (2008, 4, 20, 13, 16, 12) head[2], body[0] op[0x57]

    op hex (2)
    0000   0x57 0xa7                                  W.
    decimal
             87  167
    datetime ((2008, 4, 20, 13, 16, 12))
    0000   0x4c 0x10 0x0d 0x34 0xc8                   L..4.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 15 Base (2011, 0, 10, 13, 16, 13) head[2], body[0] op[0x76]

    op hex (2)
    0000   0x76 0x8a                                  v.
    decimal
            118  138
    datetime ((2011, 0, 10, 13, 16, 13))
    0000   0x0d 0x10 0x0d 0x0a 0x6b                   ....k
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 16 Base (2011, 0, 10, 13, 16, 46) head[2], body[0] op[0x47]

    op hex (2)
    0000   0x47 0x83                                  G.
    decimal
             71  131
    datetime ((2011, 0, 10, 13, 16, 46))
    0000   0x2e 0x10 0x0d 0x0a 0x7b                   ....{
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 17 Base (2005, 0, 10, 13, 16, 46) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x84                                  p.
    decimal
            112  132
    datetime ((2005, 0, 10, 13, 16, 46))
    0000   0x2e 0x10 0x0d 0x0a 0x75                   ....u
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 18 Base (2005, 0, 27, 13, 16, 46) head[2], body[0] op[0x4e]

    op hex (2)
    0000   0x4e 0x87                                  N.
    decimal
             78  135
    datetime ((2005, 0, 27, 13, 16, 46))
    0000   0x2e 0x10 0x0d 0x5b 0x75                   ...[u
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 19 Base (2000, 0, 0, 13, 16, 14) head[2], body[0] op[0x6f]

    op hex (2)
    0000   0x6f 0x87                                  o.
    decimal
            111  135
    datetime ((2000, 0, 0, 13, 16, 14))
    0000   0x0e 0x10 0x0d 0x20 0x50                   ... P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 20 Base (2000, 4, 0, 24, 0, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 24, 0, 42))
    0000   0x6a 0x00 0x18 0x00 0x00                   j....
    body (0)

#### RECORD 21 Base (2012, 1, 5, 28, 61, 24) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x00                                  ..
    decimal
             17    0
    datetime ((2012, 1, 5, 28, 61, 24))
    0000   0x18 0x7d 0x5c 0x05 0x6c                   .}\.l
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 22 Base (2015, 0, 0, 24, 24, 1) head[2], body[0] op[0x5d]

    op hex (2)
    0000   0x5d 0x04                                  ].
    decimal
             93    4
    datetime ((2015, 0, 0, 24, 24, 1))
    0000   0x01 0x18 0x18 0x00 0x6f                   ....o
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 23 Base (2000, 0, 8, 10, 13, 16) head[2], body[0] op[0x87]

    op hex (2)
    0000   0x87 0x4e                                  .N
    decimal
            135   78
    datetime ((2000, 0, 8, 10, 13, 16))
    0000   0x10 0x0d 0x0a 0x68 0x40                   ...h@
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 24 Base (2005, 0, 29, 10, 13, 16) head[2], body[0] op[0xb0]

    op hex (2)
    0000   0xb0 0x2f                                  ./
    decimal
            176   47
    datetime ((2005, 0, 29, 10, 13, 16))
    0000   0x10 0x0d 0x0a 0x3d 0x75                   ...=u
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 25 Base (2006, 0, 24, 10, 13, 16) head[2], body[0] op[0x81]

    op hex (2)
    0000   0x81 0x30                                  .0
    decimal
            129   48
    datetime ((2006, 0, 24, 10, 13, 16))
    0000   0x10 0x0d 0x0a 0x38 0x76                   ...8v
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 26 Base (2014, 0, 28, 10, 13, 16) head[2], body[0] op[0x88]

    op hex (2)
    0000   0x88 0x30                                  .0
    decimal
            136   48
    datetime ((2014, 0, 28, 10, 13, 16))
    0000   0x10 0x0d 0x0a 0x5c 0x6e                   ...\n
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 27 Base (2006, 0, 28, 27, 13, 16) head[2], body[0] op[0x9b]

    op hex (2)
    0000   0x9b 0x33                                  .3
    decimal
            155   51
    datetime ((2006, 0, 28, 27, 13, 16))
    0000   0x10 0x0d 0x5b 0x5c 0x76                   ..[\v
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 28 Base (2013, 0, 16, 15, 13, 16) head[2], body[0] op[0x9b]

    op hex (2)
    0000   0x9b 0x13                                  ..
    decimal
            155   19
    datetime ((2013, 0, 16, 15, 13, 16))
    0000   0x10 0x0d 0x0f 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 29 Base (2000, 12, 0, 16, 11, 61) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 11, 61))
    0000   0xfd 0x0b 0xf0 0x00 0x00                   .....
    body (0)

#### RECORD 30 Base (2003, 5, 0, 8, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2003, 5, 0, 8, 28, 61))
    0000   0x7d 0x5c 0x08 0x60 0x43                   }\.`C
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 31 SelectBasalProfile 2008-08-08T01:20:29 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x6c                                  .l
    decimal
             20  108
    datetime (2008-08-08T01:20:29)
    0000   0x9d 0x14 0x01 0x08 0x08                   .....
    body (0)

#### RECORD 32 Base (2004, 9, 13, 16, 19, 27) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x76                                  .v
    decimal
              0  118
    datetime ((2004, 9, 13, 16, 19, 27))
    0000   0x9b 0x53 0x10 0x0d 0x34                   .S..4
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 33 ChangeTimeDisplay 2010-08-13T16:20:12 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x65                                  de
    decimal
            100  101
    datetime (2010-08-13T16:20:12)
    0000   0x8c 0x14 0x10 0x0d 0x0a                   .....
    body (0)

#### RECORD 34 Base (2007, 8, 13, 16, 52, 57) head[2], body[0] op[0x93]

    op hex (2)
    0000   0x93 0x64                                  .d
    decimal
            147  100
    datetime ((2007, 8, 13, 16, 52, 57))
    0000   0xb9 0x34 0x10 0x0d 0x07                   .4...
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-11.data: 35 records`
