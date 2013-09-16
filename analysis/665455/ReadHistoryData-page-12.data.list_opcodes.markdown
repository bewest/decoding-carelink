## START logs/ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 471, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x05 0x34 0x6c 0x0d 0x6d 0x6c 0x0d 0x05    .4l.ml..
    0008   0x10 0xc3 0x60 0x20 0x04 0x00 0x00 0x05    ..` ....
    0010   0x34 0x03 0x70 0x42 0x01 0xc4 0x22 0x00    4.pB..".
    0018   0x69 0x01 0xc4 0x22 0x01 0x34 0x44 0x00    i..".4D.
##### DEBUG DECIMAL
              5   52  108   13  109  108   13    5
             16  195   96   32    4    0    0    5
             52    3  112   66    1  196   34    0
            105    1  196   34    1   52   68    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 0.3, 'curve': 4},
 {'age': 82, 'amount': 0.1, 'curve': 4},
 {'age': 16, 'amount': 1.9, 'curve': 20},
 {'age': 106, 'amount': 3.4, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0c 0x48 0x04 0x04 0x52 0x04    \..H..R.
    0008   0x4c 0x10 0x14 0x88 0x6a 0x14              L...j.
    decimal
             92   14   12   72    4    4   82    4
             76   16   20  136  106   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-06-10T20:36:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-06-10T20:36:39)
    0000   0x67 0xa4 0x54 0x0a 0x0d                   g.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 BolusWizard 2013-06-10T20:40:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 41,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.1,
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
    datetime (2013-06-10T20:40:53)
    0000   0x75 0xa8 0x14 0x0a 0x0d                   u....
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x00 0x1f 0x00    )P.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             41   80   13   45  106    0   31    0
              0    0    0   31  125
    HOUR BITS: [1, 0, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 0.9, 'curve': 4},
 {'age': 76, 'amount': 0.3, 'curve': 4},
 {'age': 86, 'amount': 0.1, 'curve': 4},
 {'age': 20, 'amount': 1.9, 'curve': 20},
 {'age': 110, 'amount': 3.4, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x24 0x06 0x04 0x0c 0x4c 0x04    \.$...L.
    0008   0x04 0x56 0x04 0x4c 0x14 0x14 0x88 0x6e    .V.L...n
    0010   0x14                                       .
    decimal
             92   17   36    6    4   12   76    4
              4   86    4   76   20   20  136  110
             20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-06-10T20:40:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-06-10T20:40:54)
    0000   0x76 0xa8 0x54 0x0a 0x0d                   v.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 5 CalBGForPH 2013-06-10T22:30:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-06-10T22:30:20)
    0000   0x54 0x9e 0x36 0x0a 0x0d                   T.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 ResultTotals 2013-04-10T13:13:42 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xfa                   .....
    decimal
              7    0    0    4  250
    datetime (2013-04-10T13:13:42)
    0000   0x6a 0x0d 0x6d 0x6a 0x0d                   j.mj.
    body (51)
    hex
    0000   0x05 0x10 0x9a 0x6f 0x07 0x07 0x00 0x00    ...o....
    0008   0x04 0xfa 0x03 0x76 0x46 0x01 0x84 0x1e    ...vF...
    0010   0x00 0x48 0x01 0x84 0x1e 0x00 0xd8 0x38    .H.....8
    0018   0x00 0xac 0x2c 0x00 0x00 0x00 0x05 0x03    ..,.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x62 0x6a 0xbb 0x31 0x0b 0x0d    ..bj.1..
    0030   0x5b 0x62 0x7b                             [b{
    decimal
              5   16  154  111    7    7    0    0
              4  250    3  118   70    1  132   30
              0   72    1  132   30    0  216   56
              0  172   44    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0   10   98  106  187   49   11   13
             91   98  123
    DAY BITS: [0, 1, 1]
#### RECORD 7 Base (2013, 0, 16, 14, 13, 11) head[2], body[0] op[0xbb]

    op hex (2)
    0000   0xbb 0x11                                  ..
    decimal
            187   17
    datetime ((2013, 0, 16, 14, 13, 11))
    0000   0x0b 0x0d 0x2e 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 8 Base (2000, 12, 0, 16, 35, 62) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 35, 62))
    0000   0xfe 0x23 0xf0 0x00 0x00                   .#...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 9 Base (2000, 4, 1, 1, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x21                                  .!
    decimal
              0   33
    datetime ((2000, 4, 1, 1, 1, 61))
    0000   0x7d 0x01 0x21 0x21 0x00                   }.!!.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 10 BasalProfileStart 2013-04-10T13:11:17 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0xbb                                  {.
    decimal
            123  187
    datetime (2013-04-10T13:11:17)
    0000   0x51 0x0b 0x0d 0x0a 0x6d                   Q...m
    body (3)
    hex
    0000   0x69 0x84 0x33                             i.3
    decimal
            105  132   51
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 11 Ian0B 2011-05-19T05:11:45 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x0d 0x5b                             ..[
    decimal
             11   13   91
    datetime (2011-05-19T05:11:45)
    0000   0x6d 0x4b 0x85 0x13 0x0b                   mK...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 12 Base (2000, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1b                                  ..
    decimal
             13   27
    datetime ((2000, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x00                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 13 SelectBasalProfile (2013, 0, 20, 0, 26, 0) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x00                                  ..
    decimal
             20    0
    datetime ((2013, 0, 20, 0, 26, 0))
    0000   0x00 0x1a 0x00 0x14 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 3.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x84 0x47 0x04                   \..G.
    decimal
             92    5  132   71    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-06-11T19:05:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-06-11T19:05:11)
    0000   0x4b 0x85 0x53 0x0b 0x0d                   K.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 CalBGForPH 2013-06-11T20:32:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-06-11T20:32:02)
    0000   0x42 0xa0 0x34 0x0b 0x0d                   B.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 17 ResultTotals 2013-04-11T13:13:43 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x58                   ....X
    decimal
              7    0    0    4   88
    datetime (2013-04-11T13:13:43)
    0000   0x6b 0x0d 0x6d 0x6b 0x0d                   k.mk.
    body (51)
    hex
    0000   0x05 0x00 0x68 0x62 0x6d 0x03 0x00 0x00    ..hbm...
    0008   0x04 0x58 0x03 0x84 0x51 0x00 0xd4 0x13    .X..Q...
    0010   0x00 0x49 0x00 0xd4 0x13 0x00 0xd4 0x64    .I.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x34 0xc8 0x6d 0x92 0x00 0x0c 0x0d    .4.m....
    0030   0x34 0x64 0x41                             4dA
    decimal
              5    0  104   98  109    3    0    0
              4   88    3  132   81    0  212   19
              0   73    0  212   19    0  212  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0   52  200  109  146    0   12   13
             52  100   65
    DAY BITS: [0, 1, 1]
#### RECORD 18 Base (2011, 0, 0, 30, 13, 12) head[2], body[0] op[0x9e]

    op hex (2)
    0000   0x9e 0x0b                                  ..
    decimal
            158   11
    datetime ((2011, 0, 0, 30, 13, 12))
    0000   0x0c 0x0d 0x1e 0x00 0x4b                   ....K
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 19 Base (2004, 0, 0, 31, 13, 12) head[2], body[0] op[0xa2]

    op hex (2)
    0000   0xa2 0x0d                                  ..
    decimal
            162   13
    datetime ((2004, 0, 0, 31, 13, 12))
    0000   0x0c 0x0d 0x1f 0x00 0x74                   ....t
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 20 Base (2011, 0, 0, 10, 13, 12) head[2], body[0] op[0xba]

    op hex (2)
    0000   0xba 0x0d                                  ..
    decimal
            186   13
    datetime ((2011, 0, 0, 10, 13, 12))
    0000   0x0c 0x0d 0x0a 0x60 0x4b                   ...`K
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 21 Base (2007, 0, 0, 27, 13, 12) head[2], body[0] op[0xa1]

    op hex (2)
    0000   0xa1 0x2f                                  ./
    decimal
            161   47
    datetime ((2007, 0, 0, 27, 13, 12))
    0000   0x0c 0x0d 0x5b 0x60 0x57                   ..[`W
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 22 Base (2013, 0, 16, 12, 13, 12) head[2], body[0] op[0xa1]

    op hex (2)
    0000   0xa1 0x0f                                  ..
    decimal
            161   15
    datetime ((2013, 0, 16, 12, 13, 12))
    0000   0x0c 0x0d 0x2c 0x50 0x0d                   ..,P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 23 Base (2000, 12, 0, 16, 33, 62) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 33, 62))
    0000   0xfe 0x21 0xf0 0x00 0x00                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 24 Base (2000, 4, 31, 31, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1f                                  ..
    decimal
              0   31
    datetime ((2000, 4, 31, 31, 1, 61))
    0000   0x7d 0x01 0x1f 0x1f 0x00                   }....
    body (0)

#### RECORD 25 Base (2013, 4, 10, 13, 12, 15) head[2], body[0] op[0x57]

    op hex (2)
    0000   0x57 0xa1                                  W.
    decimal
             87  161
    datetime ((2013, 4, 10, 13, 12, 15))
    0000   0x4f 0x0c 0x0d 0x0a 0xbd                   O....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 26 Base (2000, 0, 30, 13, 12, 49) head[2], body[0] op[0x6f]

    op hex (2)
    0000   0x6f 0x8a                                  o.
    decimal
            111  138
    datetime ((2000, 0, 30, 13, 12, 49))
    0000   0x31 0x0c 0x0d 0x1e 0x00                   1....
    body (0)

#### RECORD 27 Ian54 (2000, 0, 31, 13, 12, 21) head[2], body[57] op[0x54]

    op hex (2)
    0000   0x54 0x90                                  T.
    decimal
             84  144
    datetime ((2000, 0, 31, 13, 12, 21))
    0000   0x15 0x0c 0x0d 0x1f 0x00                   .....
    body (57)
    hex
    0000   0x59 0x90 0x15 0x0c 0x0d 0x21 0x00 0x5f    Y....!._
    0008   0x90 0x15 0x0c 0x0d 0x03 0x00 0x00 0x00    ........
    0010   0x19 0x65 0x92 0x35 0x0c 0x0d 0x03 0x00    .e.5....
    0018   0x05 0x00 0x05 0x77 0x92 0x15 0x0c 0x0d    ...w....
    0020   0x0a 0x20 0x65 0x95 0x35 0x0c 0x8d 0x5b    . e.5..[
    0028   0x20 0x71 0x95 0x15 0x0c 0x0d 0x00 0x51     q.....Q
    0030   0x0d 0x2d 0x6a 0x24 0x00 0x00 0x00 0x00    .-j$....
    0038   0x00                                       .
    decimal
             89  144   21   12   13   33    0   95
            144   21   12   13    3    0    0    0
             25  101  146   53   12   13    3    0
              5    0    5  119  146   21   12   13
             10   32  101  149   53   12  141   91
             32  113  149   21   12   13    0   81
             13   45  106   36    0    0    0    0
              0

#### RECORD 28 Base (2004, 4, 27, 22, 8, 28) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x7d                                  $}
    decimal
             36  125
    datetime ((2004, 4, 27, 22, 8, 28))
    0000   0x5c 0x08 0x56 0x5b 0x14                   \.V[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 29 EnableDisableRemote (2000, 0, 4, 4, 1, 20) head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0x65                                  &e
    decimal
             38  101
    datetime ((2000, 0, 4, 4, 1, 20))
    0000   0x14 0x01 0x24 0x24 0x00                   ..$$.
    body (14)
    hex
    0000   0x71 0x95 0x55 0x0c 0x0d 0x0a 0xcd 0x44    q.U....D
    0008   0x98 0x36 0x0c 0x0d 0x5b 0xcd              .6..[.
    decimal
            113  149   85   12   13   10  205   68
            152   54   12   13   91  205
    DAY BITS: [0, 0, 1]
#### RECORD 30 Base (2000, 0, 29, 13, 12, 22) head[2], body[0] op[0x41]

    op hex (2)
    0000   0x41 0x99                                  A.
    decimal
             65  153
    datetime ((2000, 0, 29, 13, 12, 22))
    0000   0x16 0x0c 0x0d 0x3d 0x50                   ...=P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 31 Base (2000, 4, 0, 14, 17, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 14, 17, 42))
    0000   0x6a 0x11 0x2e 0x00 0x00                   j....
    body (0)

#### RECORD 32 Base (2014, 1, 14, 28, 61, 46) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x00                                  ..
    decimal
             28    0
    datetime ((2014, 1, 14, 28, 61, 46))
    0000   0x2e 0x7d 0x5c 0x0e 0x0e                   .}\..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 33 Base (2011, 9, 22, 4, 7, 2) head[2], body[0] op[0x3d]

    op hex (2)
    0000   0x3d 0x04                                  =.
    decimal
             61    4
    datetime ((2011, 9, 22, 4, 7, 2))
    0000   0x82 0x47 0x04 0x56 0x9b                   .G.V.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 34 SelectBasalProfile 2014-08-14T01:20:37 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x26                                  .&
    decimal
             20   38
    datetime (2014-08-14T01:20:37)
    0000   0xa5 0x14 0x01 0x2e 0x2e                   .....
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 35 Base (2007, 9, 13, 12, 22, 25) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x41                                  .A
    decimal
              0   65
    datetime ((2007, 9, 13, 12, 22, 25))
    0000   0x99 0x56 0x0c 0x0d 0x07                   .V...
    body (0)
    HOUR BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-12.data: 36 records`
