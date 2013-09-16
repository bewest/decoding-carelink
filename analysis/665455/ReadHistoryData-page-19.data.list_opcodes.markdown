## START logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 464, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x2b 0x53 0x46 0x2e 0x0d 0x0d 0x03 0x00    +SF.....
    0008   0x05 0x00 0x05 0x6b 0x46 0x0e 0x0d 0x0d    ...kF...
    0010   0x0a 0xac 0x74 0x47 0x2e 0x0d 0x0d 0x0a    ..tG....
    0018   0xa7 0x77 0x47 0x2e 0x0d 0x0d 0x0a 0xa3    .wG.....
##### DEBUG DECIMAL
             43   83   70   46   13   13    3    0
              5    0    5  107   70   14   13   13
             10  172  116   71   46   13   13   10
            167  119   71   46   13   13   10  163
#### RECORD 0 hack1 2013-05-11T22:49:42 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x4a 0x8d 0x05 0x00 0x71 0x40 0xba    mJ...q@.
    0008   0x05 0x00 0x00 0x04 0x42 0x03 0x72 0x51    ....B.rQ
    0010   0x00 0xd0 0x13 0x00 0x33 0x00 0xd0 0x13    ....3...
    0018   0x00 0x9c 0x4b 0x00 0x34 0x19 0x00 0x00    ..K.4...
    0020   0x00 0x02 0x01 0x01 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x79              .....y
    decimal
            109   74  141    5    0  113   64  186
              5    0    0    4   66    3  114   81
              0  208   19    0   51    0  208   19
              0  156   75    0   52   25    0    0
              0    2    1    1    0    0   12    0
            232    0    0    0   10  121
    datetime (2013-05-11T22:49:42)
    0000   0x6a 0x71 0x36 0x0b 0x0d                   jq6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-05-11T22:49:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-05-11T22:49:55)
    0000   0x77 0x71 0x16 0x0b 0x0d                   wq...
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0x00 0x35 0x00    FP.-j.5.
    0008   0x00 0x00 0x00 0x35 0x7d                   ...5}
    decimal
             70   80   13   45  106    0   53    0
              0    0    0   53  125
    HOUR BITS: [0, 1, 1]
#### RECORD 2 Bolus 2013-05-11T22:49:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-05-11T22:49:55)
    0000   0x77 0x71 0x56 0x0b 0x0d                   wqV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-05-11T23:39:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-05-11T23:39:07)
    0000   0x47 0x67 0x37 0x0b 0x0d                   Gg7..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 ResultTotals 2013-06-11T13:13:11 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x58                   ....X
    decimal
              7    0    0    4   88
    datetime (2013-06-11T13:13:11)
    0000   0x4b 0x8d 0x6d 0x4b 0x8d                   K.mK.
    body (51)
    hex
    0000   0x05 0x00 0x6f 0x65 0x79 0x02 0x00 0x00    ..oey...
    0008   0x04 0x58 0x03 0x84 0x51 0x00 0xd4 0x13    .X..Q...
    0010   0x00 0x46 0x00 0xd4 0x13 0x00 0xd4 0x64    .F.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x3b 0x4e 0x45 0x29 0x0c 0x8d    ..;NE)..
    0030   0x5b 0x3b 0x51                             [;Q
    decimal
              5    0  111  101  121    2    0    0
              4   88    3  132   81    0  212   19
              0   70    0  212   19    0  212  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0   10   59   78   69   41   12  141
             91   59   81
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 Base (2013, 0, 17, 0, 13, 12) head[2], body[0] op[0x45]

    op hex (2)
    0000   0x45 0x09                                  E.
    decimal
             69    9
    datetime ((2013, 0, 17, 0, 13, 12))
    0000   0x0c 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2000, 0, 0, 0, 0, 42) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 42))
    0000   0x2a 0x00 0x00 0x00 0x00                   *....
    body (0)

#### RECORD 7 Base (2000, 4, 10, 10, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2a                                  .*
    decimal
              0   42
    datetime ((2000, 4, 10, 10, 1, 61))
    0000   0x7d 0x01 0x2a 0x2a 0x00                   }.**.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 8 Base (2000, 4, 30, 13, 12, 9) head[2], body[0] op[0x51]

    op hex (2)
    0000   0x51 0x45                                  QE
    decimal
             81   69
    datetime ((2000, 4, 30, 13, 12, 9))
    0000   0x49 0x0c 0x0d 0x1e 0x00                   I....
    body (0)

#### RECORD 9 Base (2000, 0, 31, 13, 12, 9) head[2], body[0] op[0x55]

    op hex (2)
    0000   0x55 0x48                                  UH
    decimal
             85   72
    datetime ((2000, 0, 31, 13, 12, 9))
    0000   0x09 0x0c 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 10 Base (2011, 0, 10, 13, 12, 9) head[2], body[0] op[0x58]

    op hex (2)
    0000   0x58 0x61                                  Xa
    decimal
             88   97
    datetime ((2011, 0, 10, 13, 12, 9))
    0000   0x09 0x0c 0x0d 0x0a 0x5b                   ....[
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 11 Base (2011, 0, 10, 13, 12, 44) head[2], body[0] op[0x47]

    op hex (2)
    0000   0x47 0x50                                  GP
    decimal
             71   80
    datetime ((2011, 0, 10, 13, 12, 44))
    0000   0x2c 0x0c 0x0d 0x0a 0x5b                   ,...[
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 12 Base (2011, 0, 27, 13, 12, 44) head[2], body[0] op[0x51]

    op hex (2)
    0000   0x51 0x51                                  QQ
    decimal
             81   81
    datetime ((2011, 0, 27, 13, 12, 44))
    0000   0x2c 0x0c 0x0d 0x5b 0x5b                   ,..[[
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 13 Base (2000, 0, 17, 13, 12, 12) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x52                                  bR
    decimal
             98   82
    datetime ((2000, 0, 17, 13, 12, 12))
    0000   0x0c 0x0c 0x0d 0x31 0x50                   ...1P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 14 Base (2000, 7, 16, 5, 60, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 7, 16, 5, 60, 42))
    0000   0x6a 0xfc 0x25 0xf0 0x00                   j.%..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 1, 1]
#### RECORD 15 NoDelivery 2004-04-02T08:05:28 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x00 0x21 0x7d                        ..!}
    decimal
              6    0   33  125
    datetime (2004-04-02T08:05:28)
    0000   0x5c 0x05 0xa8 0xc2 0x04                   \....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 16 Bolus 2013-05-12T12:18:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-05-12T12:18:34)
    0000   0x62 0x52 0x4c 0x0c 0x0d                   bRL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 17 BolusWizard 2013-05-12T13:07:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
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
    datetime (2013-05-12T13:07:31)
    0000   0x5f 0x47 0x0d 0x0c 0x0d                   _G...
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 0]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 3.3, 'curve': 4},
 {'age': 243, 'amount': 4.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0x35 0x04 0xa8 0xf3 0x04    \..5....
    decimal
             92    8  132   53    4  168  243    4
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-05-12T13:07:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-05-12T13:07:31)
    0000   0x5f 0x47 0x4d 0x0c 0x0d                   _GM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 20 LowReservoir 2013-05-12T19:28:25 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-12T19:28:25)
    0000   0x59 0x5c 0x13 0x0c 0x0d                   Y\...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 21 CalBGForPH 2013-05-12T19:55:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 173}
```
    op hex (2)
    0000   0x0a 0xad                                  ..
    decimal
             10  173
    datetime (2013-05-12T19:55:50)
    0000   0x72 0x77 0x33 0x0c 0x0d                   rw3..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2013-05-12T19:55:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 173,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2013-05-12T19:55:52)
    0000   0x74 0x77 0x13 0x0c 0x0d                   tw...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.0, 'curve': 20},
 {'age': 205, 'amount': 3.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x9b 0x14 0x84 0xcd 0x14    \.(.....
    decimal
             92    8   40  155   20  132  205   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-05-12T19:55:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-05-12T19:55:52)
    0000   0x74 0x77 0x53 0x0c 0x0d                   twS..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 25 ResultTotals 2013-06-12T13:13:12 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xee                   .....
    decimal
              7    0    0    4  238
    datetime (2013-06-12T13:13:12)
    0000   0x4c 0x8d 0x6d 0x4c 0x8d                   L.mL.
    body (51)
    hex
    0000   0x05 0x10 0xa8 0x5b 0x3b 0x04 0x00 0x00    ...[;...
    0008   0x04 0xee 0x03 0x72 0x46 0x01 0x7c 0x1e    ...rF.|.
    0010   0x00 0x3e 0x01 0x7c 0x1e 0x00 0xac 0x2d    .>.|...-
    0018   0x00 0xd0 0x37 0x00 0x00 0x00 0x04 0x02    ..7.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x67 0x4a 0x42 0x20 0x0d 0x0d    ..gJB ..
    0030   0x5b 0x67 0x79                             [gy
    decimal
              5   16  168   91   59    4    0    0
              4  238    3  114   70    1  124   30
              0   62    1  124   30    0  172   45
              0  208   55    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0   10  103   74   66   32   13   13
             91  103  121
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 Base (2013, 0, 16, 18, 13, 13) head[2], body[0] op[0x44]

    op hex (2)
    0000   0x44 0x00                                  D.
    decimal
             68    0
    datetime ((2013, 0, 16, 18, 13, 13))
    0000   0x0d 0x0d 0x32 0x50 0x0d                   ..2P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 27 Base (2000, 12, 0, 16, 38, 63) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 38, 63))
    0000   0xff 0x26 0xf0 0x00 0x00                   .&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 Base (2010, 5, 8, 5, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x25                                  .%
    decimal
              0   37
    datetime ((2010, 5, 8, 5, 28, 61))
    0000   0x7d 0x5c 0x05 0x28 0xfa                   }\.(.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 29 Base (2004, 0, 25, 0, 17, 17) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x01                                  ..
    decimal
              4    1
    datetime ((2004, 0, 25, 0, 17, 17))
    0000   0x11 0x11 0x00 0x79 0x44                   ...yD
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 30 Base (2002, 0, 20, 20, 1, 13) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x0d                                  ..
    decimal
            128   13
    datetime ((2002, 0, 20, 20, 1, 13))
    0000   0x0d 0x01 0x14 0x14 0x02                   .....
    body (0)

#### RECORD 31 Base (2004, 8, 20, 13, 13, 32) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0x46                                  CF
    decimal
             67   70
    datetime ((2004, 8, 20, 13, 13, 32))
    0000   0xa0 0x0d 0x0d 0x34 0x64                   ...4d
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 32 Base (2013, 0, 10, 13, 13, 1) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x4f                                  @O
    decimal
             64   79
    datetime ((2013, 0, 10, 13, 13, 1))
    0000   0x01 0x0d 0x0d 0x0a 0x5d                   ....]
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 33 Base (2000, 0, 30, 13, 13, 35) head[2], body[0] op[0x49]

    op hex (2)
    0000   0x49 0x78                                  Ix
    decimal
             73  120
    datetime ((2000, 0, 30, 13, 13, 35))
    0000   0x23 0x0d 0x0d 0x1e 0x00                   #....
    body (0)

#### RECORD 34 Base (2000, 0, 31, 13, 13, 12) head[2], body[0] op[0x55]

    op hex (2)
    0000   0x55 0x77                                  Uw
    decimal
             85  119
    datetime ((2000, 0, 31, 13, 13, 12))
    0000   0x0c 0x0d 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 35 Base (2000, 0, 1, 13, 13, 13) head[2], body[0] op[0x75]

    op hex (2)
    0000   0x75 0x68                                  uh
    decimal
            117  104
    datetime ((2000, 0, 1, 13, 13, 13))
    0000   0x0d 0x0d 0x0d 0x21 0x00                   ...!.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 36 Base (2000, 0, 3, 13, 13, 14) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x45                                  pE
    decimal
            112   69
    datetime ((2000, 0, 3, 13, 13, 14))
    0000   0x0e 0x0d 0x0d 0x03 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-19.data: 37 records`
