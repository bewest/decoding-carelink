## START logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 138, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x60 0x36 0x5c 0x08 0x9c 0x00 0x14 0x28    `6\....(
    0008   0xaa 0x14 0x01 0x00 0x60 0x00 0x60 0x00    ....`.`.
    0010   0x00 0x00 0x9b 0x6c 0x56 0x66 0x0d 0x5b    ...lVf.[
    0018   0x00 0x81 0x61 0x17 0x66 0x0d 0x16 0x90    ..a.f...
##### DEBUG DECIMAL
             96   54   92    8  156    0   20   40
            170   20    1    0   96    0   96    0
              0    0  155  108   86  102   13   91
              0  129   97   23  102   13   22  144
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 2.4, 'curve': 4},
 {'age': 106, 'amount': 1.4, 'curve': 4},
 {'age': 116, 'amount': 2.2, 'curve': 4},
 {'age': 70, 'amount': 2.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x60 0x42 0x04 0x38 0x6a 0x04    \.`B.8j.
    0008   0x58 0x74 0x04 0x68 0x46 0x14              Xt.hF.
    decimal
             92   14   96   66    4   56  106    4
             88  116    4  104   70   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2002, 0, 0, 24, 0, 40) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x28 0x00                        ..(.
    decimal
              1    0   40    0
    datetime ((2002, 0, 0, 24, 0, 40))
    0000   0x28 0x00 0x98 0x00 0x92                   (....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 2 Base (2010, 4, 23, 10, 13, 38) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x4f                                  lO
    decimal
            108   79
    datetime ((2010, 4, 23, 10, 13, 38))
    0000   0x66 0x0d 0x0a 0x97 0x9a                   f....
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[50], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 2.55, 'curve': 63},
 {'age': 154, 'amount': 0.45, 'curve': 92},
 {'age': 102, 'amount': 6.05, 'curve': 13},
 {'age': 144, 'amount': 2.85, 'curve': 112},
 {'age': 84, 'amount': 2.275, 'curve': 186},
 {'age': 18, 'amount': 2.3, 'curve': 102},
 {'age': 33, 'amount': 0.325, 'curve': 144},
 {'age': 110, 'amount': 0.0, 'curve': 23},
 {'age': 52, 'amount': 1.35, 'curve': 0},
 {'age': 0, 'amount': 3.0, 'curve': 0},
 {'age': 0, 'amount': 0.4, 'curve': 156},
 {'age': 92, 'amount': 1.35, 'curve': 14},
 {'age': 170, 'amount': 1.0, 'curve': 4},
 {'age': 230, 'amount': 2.4, 'curve': 4},
 {'age': 14, 'amount': 1.4, 'curve': 20},
 {'age': 24, 'amount': 2.2, 'curve': 20}]
```
    op hex (50)
    0000   0x5c 0x32 0x66 0x0d 0x3f 0x12 0x9a 0x5c    \2f.?..\
    0008   0xf2 0x66 0x0d 0x72 0x90 0x70 0x5b 0x54    .f.r.p[T
    0010   0xba 0x5c 0x12 0x66 0x0d 0x21 0x90 0x00    .\.f.!..
    0018   0x6e 0x17 0x36 0x34 0x00 0x78 0x00 0x00    n.64.x..
    0020   0x10 0x00 0x9c 0x36 0x5c 0x0e 0x28 0xaa    ...6\.(.
    0028   0x04 0x60 0xe6 0x04 0x38 0x0e 0x14 0x58    .`..8..X
    0030   0x18 0x14                                  ..
    decimal
             92   50  102   13   63   18  154   92
            242  102   13  114  144  112   91   84
            186   92   18  102   13   33  144    0
            110   23   54   52    0  120    0    0
             16    0  156   54   92   14   40  170
              4   96  230    4   56   14   20   88
             24   20
    datetime (unknown)

    body (0)

#### RECORD 4 Base (2013, 9, 6, 18, 28, 58) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2013, 9, 6, 18, 28, 58))
    0000   0xba 0x5c 0x72 0x06 0x0d                   .\r..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 5 Base (2012, 0, 0, 28, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2012, 0, 0, 28, 0, 1))
    0000   0x01 0x00 0x9c 0x00 0x9c                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 6 Base (2006, 2, 18, 28, 58, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x10                                  ..
    decimal
              0   16
    datetime ((2006, 2, 18, 28, 58, 0))
    0000   0x00 0xba 0x5c 0x52 0x66                   ..\Rf
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 7 Base (2006, 2, 21, 11, 40, 61) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2006, 2, 21, 11, 40, 61))
    0000   0x3d 0xa8 0x6b 0x35 0x66                   =.k5f
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 8 Base (2006, 2, 21, 11, 40, 7) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2006, 2, 21, 11, 40, 7))
    0000   0x07 0xa8 0x6b 0xb5 0x66                   ..k.f
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 9 Base (2010, 9, 0, 27, 48, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x72                                  .r
    decimal
             13  114
    datetime ((2010, 9, 0, 27, 48, 16))
    0000   0x90 0x70 0x5b 0x00 0x9a                   .p[..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 10 Base (2000, 4, 16, 27, 13, 38) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x16                                  l.
    decimal
            108   22
    datetime ((2000, 4, 16, 27, 13, 38))
    0000   0x66 0x0d 0x1b 0x90 0x00                   f....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 11 Base (2000, 0, 0, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 0, 0, 0, 54))
    0000   0x36 0x00 0x00 0x60 0x00                   6..`.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-5.data: 12 records`
