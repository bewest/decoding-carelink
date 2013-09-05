## START logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 64, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0xdf 0x78 0x8d 0x00 0x00 0x00 0x6e    ..x....n
    0008   0x78 0x8d 0x05 0x00 0x80 0x00 0x00 0x09    x.......
    0010   0x00 0x00 0x04 0xdf 0x02 0xdb 0x3b 0x02    ......;.
    0018   0x04 0x29 0x00 0x8c 0x01 0xac 0x00 0x00    .)......
##### DEBUG DECIMAL
              4  223  120  141    0    0    0  110
            120  141    5    0  128    0    0    9
              0    0    4  223    2  219   59    2
              4   41    0  140    1  172    0    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 1.45, 'curve': 192},
 {'age': 71, 'amount': 1.25, 'curve': 192},
 {'age': 155, 'amount': 1.6, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3a 0x3d 0xc0 0x32 0x47 0xc0    \.:=.2G.
    0008   0x40 0x9b 0xd0                             @..
    decimal
             92   11   58   61  192   50   71  192
             64  155  208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2008, 4, 0, 8, 0, 4) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x44 0x00                        ..D.
    decimal
              1    0   68    0
    datetime ((2008, 4, 0, 8, 0, 4))
    0000   0x44 0x00 0x48 0x00 0x78                   D.H.x
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 2 Base (2005, 4, 0, 1, 13, 56) head[2], body[0] op[0xf6]

    op hex (2)
    0000   0xf6 0x56                                  .V
    decimal
            246   86
    datetime ((2005, 4, 0, 1, 13, 56))
    0000   0x78 0x0d 0x21 0x00 0x45                   x.!.E
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 3 Base (2000, 0, 0, 3, 13, 24) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x16                                  ..
    decimal
            249   22
    datetime ((2000, 0, 0, 3, 13, 24))
    0000   0x18 0x0d 0x03 0x00 0x00                   .....
    body (0)

#### RECORD 4 Base (2013, 7, 24, 22, 58, 2) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x67                                  .g
    decimal
              0  103
    datetime ((2013, 7, 24, 22, 58, 2))
    0000   0x42 0xfa 0x36 0x18 0x0d                   B.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 Base (2013, 7, 24, 22, 58, 28) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime ((2013, 7, 24, 22, 58, 28))
    0000   0x5c 0xfa 0x16 0x18 0x0d                   \....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 NewTimeSet (2000, 1, 0, 0, 59, 0) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x1d                                  ..
    decimal
             24   29
    datetime ((2000, 1, 0, 0, 59, 0))
    0000   0x00 0x7b 0x00 0x40 0xc0                   .{.@.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 7 Base (2007, 0, 0, 29, 0, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x19                                  ..
    decimal
              0   25
    datetime ((2007, 0, 0, 29, 0, 13))
    0000   0x0d 0x00 0x1d 0x00 0x07                   .....
    body (0)

`end logs/ReadHistoryData-page-19.data: 8 records`
