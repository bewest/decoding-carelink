## START logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 105, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x07 0x33 0x6e 0x8d 0x00 0x00 0x00 0x6e    .3n....n
    0008   0x6e 0x8d 0x05 0x00 0xf8 0x00 0x00 0x0b    n.......
    0010   0x00 0x00 0x07 0x33 0x02 0xcb 0x27 0x04    ...3..'.
    0018   0x68 0x3d 0x00 0x9a 0x01 0xac 0x01 0xf8    h=......
##### DEBUG DECIMAL
              7   51  110  141    0    0    0  110
            110  141    5    0  248    0    0   11
              0    0    7   51    2  203   39    4
            104   61    0  154    1  172    1  248
#### RECORD 0 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.9, 'curve': 192},
 {'age': 98, 'amount': 2.7, 'curve': 192},
 {'age': 238, 'amount': 2.9, 'curve': 192},
 {'age': 72, 'amount': 2.0, 'curve': 208},
 {'age': 182, 'amount': 1.0, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x24 0x08 0xc0 0x6c 0x62 0xc0    \.$..lb.
    0008   0x74 0xee 0xc0 0x50 0x48 0xd0 0x28 0xb6    t..PH.(.
    0010   0xd0                                       .
    decimal
             92   17   36    8  192  108   98  192
            116  238  192   80   72  208   40  182
            208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2003, 4, 0, 16, 0, 24) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x58 0x00                        ..X.
    decimal
              1    0   88    0
    datetime ((2003, 4, 0, 16, 0, 24))
    0000   0x58 0x00 0x50 0x00 0x73                   X.P.s
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 2 Base (2000, 4, 26, 10, 13, 46) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x56                                  .V
    decimal
            213   86
    datetime ((2000, 4, 26, 10, 13, 46))
    0000   0x6e 0x0d 0x0a 0xba 0x60                   n...`
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 3 Base (2009, 0, 26, 27, 13, 14) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x36                                  .6
    decimal
            249   54
    datetime ((2009, 0, 26, 27, 13, 14))
    0000   0x0e 0x0d 0x5b 0xba 0x69                   ..[.i
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 Base (2000, 4, 16, 19, 13, 46) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x16                                  ..
    decimal
            249   22
    datetime ((2000, 4, 16, 19, 13, 46))
    0000   0x6e 0x0d 0x13 0x50 0x00                   n..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 5 ChangeTimeDisplay 2000-04-12T00:44:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-12T00:44:36)
    0000   0x64 0x2c 0x00 0x4c 0x00                   d,.L.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2004, 1, 28, 24, 12, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7c                                  .|
    decimal
              0  124
    datetime ((2004, 1, 28, 24, 12, 0))
    0000   0x00 0x4c 0x78 0x5c 0x14                   .Lx\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 7 SelectBasalProfile (2012, 13, 0, 12, 40, 0) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x22                                  ."
    decimal
             20   34
    datetime ((2012, 13, 0, 12, 40, 0))
    0000   0xc0 0x68 0x2c 0xc0 0x6c                   .h,.l
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 8 Base (2012, 4, 16, 16, 18, 52) head[2], body[0] op[0x86]

    op hex (2)
    0000   0x86 0xc0                                  ..
    decimal
            134  192
    datetime ((2012, 4, 16, 16, 18, 52))
    0000   0x74 0x12 0xd0 0x50 0x6c                   t..Pl
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 9 Base (2012, 15, 0, 1, 16, 26) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x28                                  .(
    decimal
            208   40
    datetime ((2012, 15, 0, 1, 16, 26))
    0000   0xda 0xd0 0x01 0x00 0x4c                   ....L
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 10 Base (2009, 1, 9, 0, 60, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x4c                                  .L
    decimal
              0   76
    datetime ((2009, 1, 9, 0, 60, 0))
    0000   0x00 0x7c 0x00 0x69 0xf9                   .|.i.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 11 Base (2000, 1, 0, 0, 59, 13) head[2], body[0] op[0x56]

    op hex (2)
    0000   0x56 0x6e                                  Vn
    decimal
             86  110
    datetime ((2000, 1, 0, 0, 59, 13))
    0000   0x0d 0x7b 0x00 0x40 0xc0                   .{.@.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 12 Base (2007, 0, 0, 31, 0, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0f                                  ..
    decimal
              0   15
    datetime ((2007, 0, 0, 31, 0, 13))
    0000   0x0d 0x00 0x1f 0x00 0x07                   .....
    body (0)

`end logs/ReadHistoryData-page-25.data: 13 records`
