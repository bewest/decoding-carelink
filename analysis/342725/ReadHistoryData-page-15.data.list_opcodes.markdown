## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 356, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x05 0x02 0x02 0x01 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x34 0x64 0x4f 0x5a 0x01    ...4dOZ.
    0010   0x1f 0x0d 0x21 0x00 0x4c 0x61 0x0f 0x1f    ..!.La..
    0018   0x0d 0x03 0x00 0x00 0x00 0x24 0x41 0x63    .....$Ac
##### DEBUG DECIMAL
              5    2    2    1    0   12    0  232
              0    0    0   52  100   79   90    1
             31   13   33    0   76   97   15   31
             13    3    0    0    0   36   65   99
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 5.9, 'curve': 4},
 {'age': 94, 'amount': 0.4, 'curve': 4},
 {'age': 134, 'amount': 0.3, 'curve': 4},
 {'age': 28, 'amount': 2.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xec 0x40 0x04 0x10 0x5e 0x04    \..@..^.
    0008   0x0c 0x86 0x04 0x58 0x1c 0x14              ...X..
    decimal
             92   14  236   64    4   16   94    4
             12  134    4   88   28   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2005, 0, 0, 0, 7, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x0d 0x0d 0x00 0x44 0x70 0x56 0x1d    ....DpV.
    decimal
              1   13   13    0   68  112   86   29
    datetime ((2005, 0, 0, 0, 7, 13))
    0000   0x0d 0x07 0x00 0x00 0x05                   .....
    body (0)

#### RECORD 2 NewTimeSet (2005, 9, 13, 29, 45, 13) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x5d                                  .]
    decimal
             24   93
    datetime ((2005, 9, 13, 29, 45, 13))
    0000   0x8d 0x6d 0x5d 0x8d 0x05                   .m]..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 3 Base (2000, 11, 0, 5, 34, 40) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xb8                                  ..
    decimal
              0  184
    datetime ((2000, 11, 0, 5, 34, 40))
    0000   0xa8 0xe2 0x05 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 Base (2004, 2, 1, 5, 4, 3) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x18                                  ..
    decimal
              5   24
    datetime ((2004, 2, 1, 5, 4, 3))
    0000   0x03 0x84 0x45 0x01 0x94                   ..E..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 5 PumpResume (2001, 4, 31, 20, 1, 28) head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime ((2001, 4, 31, 20, 1, 28))
    0000   0x5c 0x01 0x94 0x1f 0x01                   \....
    body (0)

#### RECORD 6 SelectBasalProfile (2000, 2, 0, 0, 0, 0) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x44                                  .D
    decimal
             20   68
    datetime ((2000, 2, 0, 0, 0, 0))
    0000   0x00 0x80 0x20 0x00 0x00                   .. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 Base (2012, 0, 0, 1, 3, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2012, 0, 0, 1, 3, 1))
    0000   0x01 0x03 0x01 0x00 0x0c                   .....
    body (0)

#### RECORD 8 Base (2007, 0, 10, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xe8                                  ..
    decimal
              0  232
    datetime ((2007, 0, 10, 0, 0, 0))
    0000   0x00 0x00 0x00 0x0a 0x57                   ....W
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 9 Base (2000, 0, 30, 13, 30, 35) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x47                                  bG
    decimal
             98   71
    datetime ((2000, 0, 30, 13, 30, 35))
    0000   0x23 0x1e 0x0d 0x1e 0x00                   #....
    body (0)

#### RECORD 10 Base (2000, 0, 31, 13, 30, 13) head[2], body[0] op[0x76]

    op hex (2)
    0000   0x76 0x6c                                  vl
    decimal
            118  108
    datetime ((2000, 0, 31, 13, 30, 13))
    0000   0x0d 0x1e 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 11 Base (2000, 0, 10, 13, 30, 14) head[2], body[0] op[0x7a]

    op hex (2)
    0000   0x7a 0x42                                  zB
    decimal
            122   66
    datetime ((2000, 0, 10, 13, 30, 14))
    0000   0x0e 0x1e 0x0d 0x0a 0x60                   ....`
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 12 Base (2000, 0, 27, 13, 30, 46) head[2], body[0] op[0x4b]

    op hex (2)
    0000   0x4b 0x74                                  Kt
    decimal
             75  116
    datetime ((2000, 0, 27, 13, 30, 46))
    0000   0x2e 0x1e 0x0d 0x5b 0x60                   ...[`
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 13 Ian54 (2000, 0, 0, 13, 30, 14) head[2], body[57] op[0x54]

    op hex (2)
    0000   0x54 0x74                                  Tt
    decimal
             84  116
    datetime ((2000, 0, 0, 13, 30, 14))
    0000   0x0e 0x1e 0x0d 0x20 0x50                   ... P
    body (57)
    hex
    0000   0x0d 0x2d 0x6a 0xfe 0x18 0xf0 0x00 0x00    .-j.....
    0008   0x00 0x16 0x7d 0x01 0x16 0x16 0x00 0x54    ..}....T
    0010   0x74 0x4e 0x1e 0x0d 0x5b 0x00 0x71 0x54    tN..[.qT
    0018   0x0f 0x1e 0x0d 0x0d 0x50 0x0d 0x2d 0x6a    ....P.-j
    0020   0x00 0x0a 0x00 0x00 0x00 0x00 0x0a 0x7d    .......}
    0028   0x5c 0x05 0x58 0x24 0x04 0x01 0x0a 0x0a    \.X$....
    0030   0x00 0x71 0x54 0x4f 0x1e 0x0d 0x0a 0xc6    .qTO....
    0038   0x76                                       v
    decimal
             13   45  106  254   24  240    0    0
              0   22  125    1   22   22    0   84
            116   78   30   13   91    0  113   84
             15   30   13   13   80   13   45  106
              0   10    0    0    0    0   10  125
             92    5   88   36    4    1   10   10
              0  113   84   79   30   13   10  198
            118
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 14 Model522ResultTotals 2014-02-17T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-02-17T00:00:00)
    0000   0x30 0x1e                                  0.
    body (41)
    hex
    0000   0x0d 0x0a 0x15 0x6e 0x41 0x32 0x1e 0x8d    ...nA2..
    0008   0x5b 0x15 0x70 0x41 0x12 0x1e 0x0d 0x00    [.pA....
    0010   0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00 0x00    Q.-j!...
    0018   0x05 0x00 0x1c 0x7d 0x5c 0x08 0x28 0xa7    ...}\.(.
    0020   0x04 0x58 0xc5 0x04 0x01 0x1c 0x1c 0x00    .X......
    0028   0x70                                       p
    decimal
             13   10   21  110   65   50   30  141
             91   21  112   65   18   30   13    0
             81   13   45  106   33    0    0    0
              5    0   28  125   92    8   40  167
              4   88  197    4    1   28   28    0
            112

#### RECORD 15 Base (2007, 0, 14, 10, 13, 30) head[2], body[0] op[0x41]

    op hex (2)
    0000   0x41 0x52                                  AR
    decimal
             65   82
    datetime ((2007, 0, 14, 10, 13, 30))
    0000   0x1e 0x0d 0x0a 0xce 0x57                   ....W
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 16 Base (2012, 0, 14, 27, 13, 30) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x33                                  j3
    decimal
            106   51
    datetime ((2012, 0, 14, 27, 13, 30))
    0000   0x1e 0x0d 0x5b 0xce 0x5c                   ..[.\
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 17 Base (2013, 0, 16, 0, 13, 30) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x13                                  j.
    decimal
            106   19
    datetime ((2013, 0, 16, 0, 13, 30))
    0000   0x1e 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 18 Base (2015, 0, 0, 0, 0, 18) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2015, 0, 0, 0, 0, 18))
    0000   0x12 0x00 0x00 0x00 0x0f                   .....
    body (0)

#### RECORD 19 Base (2012, 5, 16, 11, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x03                                  ..
    decimal
              0    3
    datetime ((2012, 5, 16, 11, 28, 61))
    0000   0x7d 0x5c 0x0b 0x70 0x6c                   }\.pl
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 20 Base (2004, 0, 10, 24, 20, 12) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x28                                  .(
    decimal
              4   40
    datetime ((2004, 0, 10, 24, 20, 12))
    0000   0x0c 0x14 0x58 0x2a 0x14                   ..X*.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 21 Bolus (2009, 0, 28, 8, 52, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x03 0x03 0x00 0x5c 0x6a 0x53 0x1e    ....\jS.
    decimal
              1    3    3    0   92  106   83   30
    datetime ((2009, 0, 28, 8, 52, 13))
    0000   0x0d 0x34 0xc8 0x5c 0x49                   .4.\I
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 22 SelectBasalProfile (2010, 0, 15, 0, 10, 13) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x1e                                  ..
    decimal
             20   30
    datetime ((2010, 0, 15, 0, 10, 13))
    0000   0x0d 0x0a 0xa0 0x6f 0x7a                   ...oz
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 23 Base (2011, 1, 22, 0, 27, 13) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x1e                                  6.
    decimal
             54   30
    datetime ((2011, 1, 22, 0, 27, 13))
    0000   0x0d 0x5b 0xa0 0x56 0x7b                   .[.V{
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 24 TempBasalDuration (2013, 0, 13, 16, 61, 13) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 900}
```
    op hex (2)
    0000   0x16 0x1e                                  ..
    decimal
             22   30
    datetime ((2013, 0, 13, 16, 61, 13))
    0000   0x0d 0x3d 0x50 0x0d 0x2d                   .=P.-
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 25 Base (2000, 0, 1, 0, 0, 46) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x07                                  j.
    decimal
            106    7
    datetime ((2000, 0, 1, 0, 0, 46))
    0000   0x2e 0x00 0x00 0x01 0x00                   .....
    body (0)

#### RECORD 26 LowReservoir 2004-04-13T12:11:28 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 12.5}
```
    op hex (2)
    0000   0x34 0x7d                                  4}
    decimal
             52  125
    datetime (2004-04-13T12:11:28)
    0000   0x5c 0x0b 0x0c 0xcd 0x04                   \....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 27 Base (2001, 0, 20, 17, 40, 20) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x31                                  p1
    decimal
            112   49
    datetime ((2001, 0, 20, 17, 40, 20))
    0000   0x14 0x28 0xd1 0x14 0x01                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 LowReservoir (2014, 1, 22, 27, 23, 0) head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 5.2}
```
    op hex (2)
    0000   0x34 0x34                                  44
    decimal
             52   52
    datetime ((2014, 1, 22, 27, 23, 0))
    0000   0x00 0x57 0x7b 0x56 0x1e                   .W{V.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 29 Base (2014, 0, 4, 5, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x07                                  ..
    decimal
             13    7
    datetime ((2014, 0, 4, 5, 0, 0))
    0000   0x00 0x00 0x05 0x44 0x5e                   ...D^
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 30 Base (2011, 6, 16, 5, 13, 30) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x6d                                  .m
    decimal
            141  109
    datetime ((2011, 6, 16, 5, 13, 30))
    0000   0x5e 0x8d 0x05 0x10 0xab                   ^....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 31 Base (2004, 0, 5, 0, 0, 6) head[2], body[0] op[0x57]

    op hex (2)
    0000   0x57 0x15                                  W.
    decimal
             87   21
    datetime ((2004, 0, 5, 0, 0, 6))
    0000   0x06 0x00 0x00 0x05 0x44                   ....D
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 32 Prime (2012, 0, 1, 10, 0, 34) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 20.4, 'fixed': 6.6, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x78 0x42 0x01 0xcc                   .xB..
    decimal
              3  120   66    1  204
    datetime ((2012, 0, 1, 10, 0, 34))
    0000   0x22 0x00 0x6a 0x01 0xcc                   ".j..
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 33 Base (2000, 1, 20, 0, 4, 56) head[2], body[0] op[0x22]

    op hex (2)
    0000   0x22 0x01                                  ".
    decimal
             34    1
    datetime ((2000, 1, 20, 0, 4, 56))
    0000   0x38 0x44 0x00 0x94 0x20                   8D.. 
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 0]
`end logs/ReadHistoryData-page-15.data: 34 records`
