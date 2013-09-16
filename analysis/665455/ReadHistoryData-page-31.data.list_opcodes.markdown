## START logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 432, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x08 0x7d 0x5c 0x05 0xb0 0x0f 0x04 0x01    .}\.....
    0008   0x08 0x08 0x00 0x62 0x09 0x4e 0x01 0x0d    ...b.N..
    0010   0x0a 0x6a 0x48 0x15 0x2e 0x01 0x0d 0x5b    .jH....[
    0018   0x00 0x57 0x15 0x0e 0x01 0x0d 0x07 0x50    .W.....P
##### DEBUG DECIMAL
              8  125   92    5  176   15    4    1
              8    8    0   98    9   78    1   13
             10  106   72   21   46    1   13   91
              0   87   21   14    1   13    7   80
#### RECORD 0 BolusWizard 2013-03-30T22:31:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-03-30T22:31:44)
    0000   0x2c 0xdf 0x16 0x1e 0x0d                   ,....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x0f 0x20 0x00    *P.-j. .
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             42   80   13   45  106   15   32    0
              0    0    0   47  125
    HOUR BITS: [1, 1, 0]
#### RECORD 1 LowReservoir 2013-03-30T22:32:41 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-30T22:32:41)
    0000   0x29 0xe0 0x16 0x1e 0x0d                   )....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 Bolus 2013-03-30T22:31:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-03-30T22:31:44)
    0000   0x2c 0xdf 0x56 0x1e 0x0d                   ,.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-30T23:59:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-03-30T23:59:41)
    0000   0x29 0xfb 0x37 0x1e 0x0d                   ).7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 ResultTotals (2013, 2, 30, 13, 13, 62) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x32                   ....2
    decimal
              7    0    0    4   50
    datetime ((2013, 2, 30, 13, 13, 62))
    0000   0x3e 0x8d 0x6d 0x3e 0x8d                   >.m>.
    body (51)
    hex
    0000   0x05 0x00 0x97 0x6d 0xc1 0x02 0x00 0x00    ...m....
    0008   0x04 0x32 0x03 0x76 0x52 0x00 0xbc 0x12    .2.vR...
    0010   0x00 0x2a 0x00 0xbc 0x12 0x00 0x80 0x44    .*.....D
    0018   0x00 0x3c 0x20 0x00 0x00 0x00 0x01 0x00    .< .....
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x34 0x64 0x03 0xe9 0x06 0x1f 0x0d    .4d.....
    0030   0x0a 0x06 0x37                             ..7
    decimal
              5    0  151  109  193    2    0    0
              4   50    3  118   82    0  188   18
              0   42    0  188   18    0  128   68
              0   60   32    0    0    0    1    0
              0    1    0   12    0  232    0    0
              0   52  100    3  233    6   31   13
             10    6   55
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 Base (2004, 2, 6, 27, 13, 31) head[2], body[0] op[0xf2]

    op hex (2)
    0000   0xf2 0x27                                  .'
    decimal
            242   39
    datetime ((2004, 2, 6, 27, 13, 31))
    0000   0x1f 0x8d 0x5b 0x06 0x04                   ..[..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 Base (2013, 0, 17, 0, 13, 31) head[2], body[0] op[0xf3]

    op hex (2)
    0000   0xf3 0x07                                  ..
    decimal
            243    7
    datetime ((2013, 0, 17, 0, 13, 31))
    0000   0x1f 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2000, 0, 0, 0, 0, 30) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 30))
    0000   0x1e 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 8 Base (2000, 4, 30, 30, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1e                                  ..
    decimal
              0   30
    datetime ((2000, 4, 30, 30, 1, 61))
    0000   0x7d 0x01 0x1e 0x1e 0x00                   }....
    body (0)

#### RECORD 9 Base (2000, 4, 30, 13, 31, 7) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0xf3                                  ..
    decimal
              5  243
    datetime ((2000, 4, 30, 13, 31, 7))
    0000   0x47 0x1f 0x0d 0x1e 0x00                   G....
    body (0)

#### RECORD 10 Base (2000, 0, 31, 13, 31, 8) head[2], body[0] op[0x39]

    op hex (2)
    0000   0x39 0xe7                                  9.
    decimal
             57  231
    datetime ((2000, 0, 31, 13, 31, 8))
    0000   0x08 0x1f 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 11 SelectBasalProfile (2012, 0, 10, 13, 31, 9) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0xc1                                  ..
    decimal
             20  193
    datetime ((2012, 0, 10, 13, 31, 9))
    0000   0x09 0x1f 0x0d 0x0a 0xac                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 12 Base (2012, 0, 27, 13, 31, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0xdc                                  ..
    decimal
             13  220
    datetime ((2012, 0, 27, 13, 31, 42))
    0000   0x2a 0x1f 0x0d 0x5b 0xac                   *..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 13 NewTimeSet (2000, 0, 0, 13, 31, 10) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0xdc                                  ..
    decimal
             24  220
    datetime ((2000, 0, 0, 13, 31, 10))
    0000   0x0a 0x1f 0x0d 0x00 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 14 Base (2000, 4, 0, 0, 10, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 10, 42))
    0000   0x6a 0x0a 0x00 0x00 0x00                   j....
    body (0)

#### RECORD 15 ResultTotals 2001-01-04T04:56:05 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x03 0x7d 0x5c                   ...}\
    decimal
              7    0    3  125   92
    datetime (2001-01-04T04:56:05)
    0000   0x05 0x78 0xa4 0x04 0x01                   .x...
    body (51)
    hex
    0000   0x01 0x01 0x00 0x18 0xdc 0x4a 0x1f 0x0d    .....J..
    0008   0x0a 0x4d 0x0d 0xe3 0x2c 0x1f 0x0d 0x0a    .M..,...
    0010   0x50 0x1b 0xe4 0x2c 0x1f 0x0d 0x0a 0x56    P..,...V
    0018   0x2c 0xe6 0x2c 0x1f 0x0d 0x5b 0x56 0x12    ,.,..[V.
    0020   0xe7 0x0c 0x1f 0x0d 0x32 0x50 0x0d 0x2d    ....2P.-
    0028   0x6a 0xfb 0x26 0xf0 0x00 0x01 0x00 0x21    j.&....!
    0030   0x7d 0x5c 0x08                             }\.
    decimal
              1    1    0   24  220   74   31   13
             10   77   13  227   44   31   13   10
             80   27  228   44   31   13   10   86
             44  230   44   31   13   91   86   18
            231   12   31   13   50   80   13   45
            106  251   38  240    0    1    0   33
            125   92    8
    HOUR BITS: [0, 1, 1]
#### RECORD 16 Base (2001, 1, 20, 7, 56, 4) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x87                                  ..
    decimal
              4  135
    datetime ((2001, 1, 20, 7, 56, 4))
    0000   0x04 0x78 0x27 0x14 0x01                   .x'..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 17 Rewind (2015, 0, 12, 7, 18, 0) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x21                                  !!
    decimal
             33   33
    datetime ((2015, 0, 12, 7, 18, 0))
    0000   0x00 0x12 0xe7 0x4c 0x1f                   ...L.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 18 Base (2015, 0, 22, 7, 38, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x21                                  .!
    decimal
             13   33
    datetime ((2015, 0, 22, 7, 38, 0))
    0000   0x00 0x26 0xc7 0x16 0x1f                   .&...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 19 Base (2012, 0, 1, 0, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x03                                  ..
    decimal
             13    3
    datetime ((2012, 0, 1, 0, 0, 0))
    0000   0x00 0x00 0x00 0x21 0x2c                   ...!,
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 20 Base (2005, 0, 0, 3, 13, 31) head[2], body[0] op[0xc9]

    op hex (2)
    0000   0xc9 0x36                                  .6
    decimal
            201   54
    datetime ((2005, 0, 0, 3, 13, 31))
    0000   0x1f 0x0d 0x03 0x00 0x05                   .....
    body (0)

#### RECORD 21 Base (2013, 3, 31, 22, 12, 30) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2013, 3, 31, 22, 12, 30))
    0000   0x1e 0xcc 0x16 0x1f 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 CalBGForPH 2013-03-31T22:12:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-03-31T22:12:57)
    0000   0x39 0xcc 0x36 0x1f 0x0d                   9.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 BolusWizard 2013-03-31T22:13:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 102,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-03-31T22:13:26)
    0000   0x1a 0xcd 0x16 0x1f 0x0d                   .....
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0xff 0x2c 0xf0    :P.-j.,.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             58   80   13   45  106  255   44  240
              0    0    0   43  125
    HOUR BITS: [1, 1, 0]
#### RECORD 24 Bolus 2013-03-31T22:13:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-03-31T22:13:27)
    0000   0x1b 0xcd 0x56 0x1f 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 ResultTotals (2013, 2, 31, 13, 13, 63) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x1e                   .....
    decimal
              7    0    0    5   30
    datetime ((2013, 2, 31, 13, 13, 63))
    0000   0x3f 0x8d 0x6d 0x3f 0x8d                   ?.m?.
    body (51)
    hex
    0000   0x05 0x10 0x82 0x4d 0x06 0x06 0x00 0x00    ...M....
    0008   0x05 0x1e 0x03 0x72 0x43 0x01 0xac 0x21    ...rC..!
    0010   0x00 0x6c 0x01 0xac 0x21 0x01 0x30 0x47    .l..!.0G
    0018   0x00 0x7c 0x1d 0x00 0x00 0x00 0x04 0x02    .|......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x5d 0x30 0x0b 0x01 0x0d    ...]0...
    0030   0x1f 0x00 0x47                             ..G
    decimal
              5   16  130   77    6    6    0    0
              5   30    3  114   67    1  172   33
              0  108    1  172   33    1   48   71
              0  124   29    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0   30    0   93   48   11    1   13
             31    0   71
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 Base (2008, 0, 30, 10, 13, 1) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x0d                                  ..
    decimal
             15   13
    datetime ((2008, 0, 30, 10, 13, 1))
    0000   0x01 0x0d 0x0a 0x5e 0x48                   ...^H
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 27 Base (2005, 0, 30, 27, 13, 1) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x2d                                  6-
    decimal
             54   45
    datetime ((2005, 0, 30, 27, 13, 1))
    0000   0x01 0x0d 0x5b 0x5e 0x65                   ..[^e
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 28 Base (2013, 0, 16, 30, 13, 1) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x0d                                  6.
    decimal
             54   13
    datetime ((2013, 0, 16, 30, 13, 1))
    0000   0x01 0x0d 0x3e 0x50 0x0d                   ..>P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 29 Base (2000, 12, 0, 16, 47, 61) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 47, 61))
    0000   0xfd 0x2f 0xf0 0x00 0x00                   ./...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 Base (2000, 4, 12, 12, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2c                                  .,
    decimal
              0   44
    datetime ((2000, 4, 12, 12, 1, 61))
    0000   0x7d 0x01 0x2c 0x2c 0x00                   }.,,.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 31 Base (2000, 4, 27, 13, 1, 13) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x36                                  e6
    decimal
            101   54
    datetime ((2000, 4, 27, 13, 1, 13))
    0000   0x4d 0x01 0x0d 0x5b 0x00                   M..[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 32 Base (2000, 0, 11, 13, 1, 14) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x09                                  b.
    decimal
             98    9
    datetime ((2000, 0, 11, 13, 1, 14))
    0000   0x0e 0x01 0x0d 0x0b 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 33 Base (2000, 4, 0, 8, 0, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 8, 0, 42))
    0000   0x6a 0x00 0x08 0x00 0x00                   j....
    body (0)

`end logs/ReadHistoryData-page-31.data: 34 records`
