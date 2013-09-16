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

#### RECORD 1 Bolus 2013-05-29T22:48:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-05-29T22:48:04)
    0000   0x44 0x70 0x56 0x1d 0x0d                   DpV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 ResultTotals 2013-06-29T13:13:29 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x18                   .....
    decimal
              7    0    0    5   24
    datetime (2013-06-29T13:13:29)
    0000   0x5d 0x8d 0x6d 0x5d 0x8d                   ].m].
    body (51)
    hex
    0000   0x05 0x00 0xb8 0xa8 0xe2 0x05 0x00 0x00    ........
    0008   0x05 0x18 0x03 0x84 0x45 0x01 0x94 0x1f    ....E...
    0010   0x00 0x5c 0x01 0x94 0x1f 0x01 0x14 0x44    .\.....D
    0018   0x00 0x80 0x20 0x00 0x00 0x00 0x05 0x01    .. .....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x57 0x62 0x47 0x23 0x1e 0x0d    ..WbG#..
    0030   0x1e 0x00 0x76                             ..v
    decimal
              5    0  184  168  226    5    0    0
              5   24    3  132   69    1  148   31
              0   92    1  148   31    1   20   68
              0  128   32    0    0    0    5    1
              3    1    0   12    0  232    0    0
              0   10   87   98   71   35   30   13
             30    0  118
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 Base (2010, 0, 0, 31, 13, 30) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x0d                                  l.
    decimal
            108   13
    datetime ((2010, 0, 0, 31, 13, 30))
    0000   0x1e 0x0d 0x1f 0x00 0x7a                   ....z
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 4 Base (2011, 0, 0, 10, 13, 30) head[2], body[0] op[0x42]

    op hex (2)
    0000   0x42 0x0e                                  B.
    decimal
             66   14
    datetime ((2011, 0, 0, 10, 13, 30))
    0000   0x1e 0x0d 0x0a 0x60 0x4b                   ...`K
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 5 Base (2004, 0, 0, 27, 13, 30) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0x2e                                  t.
    decimal
            116   46
    datetime ((2004, 0, 0, 27, 13, 30))
    0000   0x1e 0x0d 0x5b 0x60 0x54                   ..[`T
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 6 Base (2013, 0, 16, 0, 13, 30) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0x0e                                  t.
    decimal
            116   14
    datetime ((2013, 0, 16, 0, 13, 30))
    0000   0x1e 0x0d 0x20 0x50 0x0d                   .. P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2000, 12, 0, 16, 24, 62) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 24, 62))
    0000   0xfe 0x18 0xf0 0x00 0x00                   .....
    body (0)

#### RECORD 8 Base (2000, 4, 22, 22, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x16                                  ..
    decimal
              0   22
    datetime ((2000, 4, 22, 22, 1, 61))
    0000   0x7d 0x01 0x16 0x16 0x00                   }....
    body (0)

#### RECORD 9 Ian54 2000-04-27T13:30:14 head[2], body[57] op[0x54]

    op hex (2)
    0000   0x54 0x74                                  Tt
    decimal
             84  116
    datetime (2000-04-27T13:30:14)
    0000   0x4e 0x1e 0x0d 0x5b 0x00                   N..[.
    body (57)
    hex
    0000   0x71 0x54 0x0f 0x1e 0x0d 0x0d 0x50 0x0d    qT....P.
    0008   0x2d 0x6a 0x00 0x0a 0x00 0x00 0x00 0x00    -j......
    0010   0x0a 0x7d 0x5c 0x05 0x58 0x24 0x04 0x01    .}\.X$..
    0018   0x0a 0x0a 0x00 0x71 0x54 0x4f 0x1e 0x0d    ...qTO..
    0020   0x0a 0xc6 0x76 0x6d 0x30 0x1e 0x0d 0x0a    ..vm0...
    0028   0x15 0x6e 0x41 0x32 0x1e 0x8d 0x5b 0x15    .nA2..[.
    0030   0x70 0x41 0x12 0x1e 0x0d 0x00 0x51 0x0d    pA....Q.
    0038   0x2d                                       -
    decimal
            113   84   15   30   13   13   80   13
             45  106    0   10    0    0    0    0
             10  125   92    5   88   36    4    1
             10   10    0  113   84   79   30   13
             10  198  118  109   48   30   13   10
             21  110   65   50   30  141   91   21
            112   65   18   30   13    0   81   13
             45
    DAY BITS: [0, 1, 0]
#### RECORD 10 Base (2000, 0, 5, 0, 0, 0) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x21                                  j!
    decimal
            106   33
    datetime ((2000, 0, 5, 0, 0, 0))
    0000   0x00 0x00 0x00 0x05 0x00                   .....
    body (0)

#### RECORD 11 Base (2004, 4, 7, 8, 8, 28) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x7d                                  .}
    decimal
             28  125
    datetime ((2004, 4, 7, 8, 8, 28))
    0000   0x5c 0x08 0x28 0xa7 0x04                   \.(..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 12 Base (2000, 0, 28, 28, 1, 4) head[2], body[0] op[0x58]

    op hex (2)
    0000   0x58 0xc5                                  X.
    decimal
             88  197
    datetime ((2000, 0, 28, 28, 1, 4))
    0000   0x04 0x01 0x1c 0x1c 0x00                   .....
    body (0)

#### RECORD 13 Base (2014, 4, 10, 13, 30, 18) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x41                                  pA
    decimal
            112   65
    datetime ((2014, 4, 10, 13, 30, 18))
    0000   0x52 0x1e 0x0d 0x0a 0xce                   R....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 14 Base (2014, 0, 27, 13, 30, 51) head[2], body[0] op[0x57]

    op hex (2)
    0000   0x57 0x6a                                  Wj
    decimal
             87  106
    datetime ((2014, 0, 27, 13, 30, 51))
    0000   0x33 0x1e 0x0d 0x5b 0xce                   3..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[106], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 0.475, 'curve': 13},
 {'age': 80, 'amount': 0.0, 'curve': 13},
 {'age': 106, 'amount': 1.125, 'curve': 18},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.375, 'curve': 3},
 {'age': 92, 'amount': 3.125, 'curve': 11},
 {'age': 108, 'amount': 2.8, 'curve': 4},
 {'age': 12, 'amount': 1.0, 'curve': 20},
 {'age': 42, 'amount': 2.2, 'curve': 20},
 {'age': 3, 'amount': 0.025, 'curve': 3},
 {'age': 92, 'amount': 0.0, 'curve': 106},
 {'age': 30, 'amount': 2.075, 'curve': 13},
 {'age': 200, 'amount': 1.3, 'curve': 92},
 {'age': 20, 'amount': 1.825, 'curve': 30},
 {'age': 10, 'amount': 0.325, 'curve': 160},
 {'age': 122, 'amount': 2.775, 'curve': 54},
 {'age': 13, 'amount': 0.75, 'curve': 91},
 {'age': 86, 'amount': 4.0, 'curve': 123},
 {'age': 30, 'amount': 0.55, 'curve': 13},
 {'age': 80, 'amount': 1.525, 'curve': 13},
 {'age': 106, 'amount': 1.125, 'curve': 7},
 {'age': 0, 'amount': 1.15, 'curve': 0},
 {'age': 0, 'amount': 0.025, 'curve': 52},
 {'age': 92, 'amount': 3.125, 'curve': 11},
 {'age': 205, 'amount': 0.3, 'curve': 4},
 {'age': 49, 'amount': 2.8, 'curve': 20},
 {'age': 209, 'amount': 1.0, 'curve': 20},
 {'age': 52, 'amount': 0.025, 'curve': 52},
 {'age': 87, 'amount': 0.0, 'curve': 123},
 {'age': 30, 'amount': 2.15, 'curve': 13},
 {'age': 0, 'amount': 0.175, 'curve': 0},
 {'age': 68, 'amount': 0.125, 'curve': 94},
 {'age': 109, 'amount': 3.525, 'curve': 94},
 {'age': 5, 'amount': 3.525, 'curve': 16}]
```
    op hex (106)
    0000   0x5c 0x6a 0x13 0x1e 0x0d 0x00 0x50 0x0d    \j....P.
    0008   0x2d 0x6a 0x12 0x00 0x00 0x00 0x0f 0x00    -j......
    0010   0x03 0x7d 0x5c 0x0b 0x70 0x6c 0x04 0x28    .}\.pl.(
    0018   0x0c 0x14 0x58 0x2a 0x14 0x01 0x03 0x03    ..X*....
    0020   0x00 0x5c 0x6a 0x53 0x1e 0x0d 0x34 0xc8    .\jS..4.
    0028   0x5c 0x49 0x14 0x1e 0x0d 0x0a 0xa0 0x6f    \I.....o
    0030   0x7a 0x36 0x1e 0x0d 0x5b 0xa0 0x56 0x7b    z6..[.V{
    0038   0x16 0x1e 0x0d 0x3d 0x50 0x0d 0x2d 0x6a    ...=P.-j
    0040   0x07 0x2e 0x00 0x00 0x01 0x00 0x34 0x7d    ......4}
    0048   0x5c 0x0b 0x0c 0xcd 0x04 0x70 0x31 0x14    \....p1.
    0050   0x28 0xd1 0x14 0x01 0x34 0x34 0x00 0x57    (...44.W
    0058   0x7b 0x56 0x1e 0x0d 0x07 0x00 0x00 0x05    {V......
    0060   0x44 0x5e 0x8d 0x6d 0x5e 0x8d 0x05 0x10    D^.m^...
    0068   0xab 0x57                                  .W
    decimal
             92  106   19   30   13    0   80   13
             45  106   18    0    0    0   15    0
              3  125   92   11  112  108    4   40
             12   20   88   42   20    1    3    3
              0   92  106   83   30   13   52  200
             92   73   20   30   13   10  160  111
            122   54   30   13   91  160   86  123
             22   30   13   61   80   13   45  106
              7   46    0    0    1    0   52  125
             92   11   12  205    4  112   49   20
             40  209   20    1   52   52    0   87
            123   86   30   13    7    0    0    5
             68   94  141  109   94  141    5   16
            171   87
    datetime (unknown)

    body (0)

#### RECORD 16 Base (2003, 0, 4, 5, 0, 0) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x06                                  ..
    decimal
             21    6
    datetime ((2003, 0, 4, 5, 0, 0))
    0000   0x00 0x00 0x05 0x44 0x03                   ...D.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 17 Base (2010, 3, 0, 2, 12, 1) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x42                                  xB
    decimal
            120   66
    datetime ((2010, 3, 0, 2, 12, 1))
    0000   0x01 0xcc 0x22 0x00 0x6a                   ..".j
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 18 Bolus 2000-01-20T00:04:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 20.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0xcc 0x22 0x01                        ..".
    decimal
              1  204   34    1
    datetime (2000-01-20T00:04:56)
    0000   0x38 0x44 0x00 0x94 0x20                   8D.. 
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 0]
`end logs/ReadHistoryData-page-15.data: 19 records`
