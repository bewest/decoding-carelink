## START logs/ReadHistoryData-page-8.data
#### STOPPING DOUBLE NULLS @ 113, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x54 0x64 0x5c 0x0e 0x38 0xac 0x80 0x9c    Td\.8...
    0008   0xb6 0x80 0x09 0x2e 0x90 0x0b 0x38 0x90    ......8.
    0010   0x01 0x00 0x54 0x00 0x54 0x00 0x00 0x00    ..T.T...
    0018   0x36 0xce 0x4c 0x05 0x0e 0x5b 0x00 0x0e    6.L..[..
##### DEBUG DECIMAL
             84  100   92   14   56  172  128  156
            182  128    9   46  144   11   56  144
              1    0   84    0   84    0    0    0
             54  206   76    5   14   91    0   14
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 0.225, 'curve': 128},
 {'age': 136, 'amount': 0.275, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x09 0x7e 0x80 0x0b 0x88 0x80    \..~....
    decimal
             92    8    9  126  128   11  136  128
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2001, 0, 0, 0, 0, 52) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x34 0x00                        ..4.
    decimal
              1    0   52    0
    datetime ((2001, 0, 0, 0, 0, 52))
    0000   0x34 0x00 0x00 0x00 0x21                   4...!
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 2 Base (2015, 4, 0, 27, 14, 37) head[2], body[0] op[0xd2]

    op hex (2)
    0000   0xd2 0x49                                  .I
    decimal
            210   73
    datetime ((2015, 4, 0, 27, 14, 37))
    0000   0x65 0x0e 0x5b 0x00 0x0f                   e.[..
    body (0)

#### RECORD 3 Base (2000, 4, 16, 13, 14, 37) head[2], body[0] op[0xd4]

    op hex (2)
    0000   0xd4 0x09                                  ..
    decimal
            212    9
    datetime ((2000, 4, 16, 13, 14, 37))
    0000   0x65 0x0e 0x2d 0x50 0x00                   e.-P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 4 Sara6E 2000-02-09T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2000-02-09T00:00:00)
    0000   0x28 0x50                                  (P
    body (49)
    hex
    0000   0x00 0x00 0xa0 0x00 0x00 0x00 0x00 0xa0    ........
    0008   0x64 0x5c 0x0b 0x34 0x08 0x80 0x09 0x80    d\.4....
    0010   0x80 0x0b 0x8a 0x80 0x01 0x00 0xa0 0x00    ........
    0018   0xa0 0x00 0x34 0x00 0x0f 0xd4 0x49 0x65    ..4...Ie
    0020   0x0e 0x7b 0x04 0x00 0xde 0x0a 0x05 0x0e    .{......
    0028   0x15 0x10 0x00 0x0a 0xd1 0x2f 0xce 0x2c    ...../.,
    0030   0x65                                       e
    decimal
              0    0  160    0    0    0    0  160
            100   92   11   52    8  128    9  128
            128   11  138  128    1    0  160    0
            160    0   52    0   15  212   73  101
             14  123    4    0  222   10    5   14
             21   16    0   10  209   47  206   44
            101
    HOUR BITS: [0, 1, 0]
#### RECORD 5 Base (2005, 0, 12, 14, 47, 26) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x3f                                  .?
    decimal
             14   63
    datetime ((2005, 0, 12, 14, 47, 26))
    0000   0x1a 0x2f 0xce 0x2c 0x65                   ./.,e
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 6 Base (2006, 9, 17, 27, 37, 9) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0xc2                                  ..
    decimal
             14  194
    datetime ((2006, 9, 17, 27, 37, 9))
    0000   0x89 0x65 0x5b 0xd1 0x36                   .e[.6
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 7 Base (2000, 0, 16, 0, 14, 5) head[2], body[0] op[0xce]

    op hex (2)
    0000   0xce 0x0c                                  ..
    decimal
            206   12
    datetime ((2000, 0, 16, 0, 14, 5))
    0000   0x05 0x0e 0x00 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 8 Base (2000, 5, 0, 0, 20, 16) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x32                                  x2
    decimal
            120   50
    datetime ((2000, 5, 0, 0, 20, 16))
    0000   0x50 0x54 0x00 0x00 0x00                   PT...
    body (0)
    HOUR BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-8.data: 9 records`
