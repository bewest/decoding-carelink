## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 54, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x48 0x00 0x00 0x00 0x00 0x48 0x36 0x5c    H....H6\
    0008   0x11 0x50 0x5e 0x04 0xc4 0xa4 0x04 0x26    .P^....&
    0010   0x3a 0x14 0x46 0x44 0x14 0x58 0xa8 0x14    :.FD.X..
    0018   0x01 0x00 0x48 0x00 0x48 0x00 0x60 0x00    ..H.H.`.
##### DEBUG DECIMAL
             72    0    0    0    0   72   54   92
             17   80   94    4  196  164    4   38
             58   20   70   68   20   88  168   20
              1    0   72    0   72    0   96    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 70, 'amount': 4.9, 'curve': 4},
 {'age': 220, 'amount': 0.95, 'curve': 4},
 {'age': 230, 'amount': 1.75, 'curve': 4},
 {'age': 74, 'amount': 2.2, 'curve': 20},
 {'age': 194, 'amount': 1.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0xc4 0x46 0x04 0x26 0xdc 0x04    \..F.&..
    0008   0x46 0xe6 0x04 0x58 0x4a 0x14 0x48 0xc2    F..XJ.H.
    0010   0x14                                       .
    decimal
             92   17  196   70    4   38  220    4
             70  230    4   88   74   20   72  194
             20
    datetime (unknown)

    body (0)

#### RECORD 1 Base (2013, 7, 26, 17, 55, 32) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2013, 7, 26, 17, 55, 32))
    0000   0x60 0xf7 0x71 0x1a 0x0d                   `.q..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 Base (2000, 0, 0, 16, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2000, 0, 0, 16, 0, 1))
    0000   0x01 0x00 0x50 0x00 0x50                   ..P.P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 3 Base (2010, 1, 17, 23, 32, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xa0                                  ..
    decimal
              0  160
    datetime ((2010, 1, 17, 23, 32, 0))
    0000   0x00 0x60 0xf7 0x51 0x7a                   .`.Qz
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 4 Base (2010, 1, 19, 29, 2, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2010, 1, 19, 29, 2, 0))
    0000   0x00 0x42 0xdd 0x13 0x7a                   .B..z
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 5 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x14                                  ..
    decimal
             13   20
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-34.data: 6 records`
