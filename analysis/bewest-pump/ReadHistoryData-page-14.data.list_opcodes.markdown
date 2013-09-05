## START logs/ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 59, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x58 0x78 0x5c 0x0e 0x40 0xff 0xc0 0x3a    Xx\.@..:
    0008   0x81 0xd0 0x1e 0x8b 0xd0 0x28 0x9f 0xd0    .....(..
    0010   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    0018   0xba 0x1c 0x53 0x05 0x0d 0x0a 0x6a 0x88    ..S...j.
##### DEBUG DECIMAL
             88  120   92   14   64  255  192   58
            129  208   30  139  208   40  159  208
              1    0   88    0   88    0    0    0
            186   28   83    5   13   10  106  136
#### RECORD 0 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 130, 'amount': 1.45, 'curve': 192},
 {'age': 140, 'amount': 0.75, 'curve': 192},
 {'age': 160, 'amount': 1.0, 'curve': 192},
 {'age': 250, 'amount': 1.05, 'curve': 192},
 {'age': 4, 'amount': 1.85, 'curve': 208},
 {'age': 104, 'amount': 1.2, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x3a 0x82 0xc0 0x1e 0x8c 0xc0    \.:.....
    0008   0x28 0xa0 0xc0 0x2a 0xfa 0xc0 0x4a 0x04    (..*..J.
    0010   0xd0 0x30 0x68 0xd0                        .0h.
    decimal
             92   20   58  130  192   30  140  192
             40  160  192   42  250  192   74    4
            208   48  104  208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2006, 4, 0, 20, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x40 0x00                        ..@.
    decimal
              1    0   64    0
    datetime ((2006, 4, 0, 20, 0, 0))
    0000   0x40 0x00 0x14 0x00 0xa6                   @....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 2 Base (2001, 0, 18, 10, 13, 5) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x4f                                  .O
    decimal
             13   79
    datetime ((2001, 0, 18, 10, 13, 5))
    0000   0x05 0x0d 0x0a 0x92 0xb1                   .....
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 3 Base (2010, 0, 18, 27, 13, 5) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x33                                  .3
    decimal
             28   51
    datetime ((2010, 0, 18, 27, 13, 5))
    0000   0x05 0x0d 0x5b 0x92 0xba                   ..[..
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 4 Base (2000, 0, 16, 18, 13, 5) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x13                                  ..
    decimal
             28   19
    datetime ((2000, 0, 16, 18, 13, 5))
    0000   0x05 0x0d 0x12 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 5 ChangeTimeDisplay 2000-04-08T00:16:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-08T00:16:36)
    0000   0x64 0x10 0x00 0x48 0x00                   d..H.
    body (0)
    DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-14.data: 6 records`
