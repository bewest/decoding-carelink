## START logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 39, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x58 0x36 0x5c 0x11 0x70 0x7c 0x04 0x5c    X6\.p|.\
    0008   0xea 0x04 0x84 0xf4 0x04 0x50 0x26 0x14    .....P&.
    0010   0x7c 0xb2 0x14 0x01 0x00 0x70 0x00 0x70    |....p.p
    0018   0x00 0x38 0x00 0x85 0x31 0x54 0x72 0x0d    .8..1Tr.
##### DEBUG DECIMAL
             88   54   92   17  112  124    4   92
            234    4  132  244    4   80   38   20
            124  178   20    1    0  112    0  112
              0   56    0  133   49   84  114   13
#### RECORD 0 Bolus (2002, 4, 0, 28, 0, 48) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x70 0x00                        ..p.
    decimal
              1    0  112    0
    datetime ((2002, 4, 0, 28, 0, 48))
    0000   0x70 0x00 0x7c 0x00 0x82                   p.|..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 Base (2012, 4, 1, 20, 13, 50) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x52                                  0R
    decimal
             48   82
    datetime ((2012, 4, 1, 20, 13, 50))
    0000   0x72 0x0d 0x34 0x01 0xac                   r.4..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 2 Base (2005, 2, 0, 27, 13, 18) head[2], body[0] op[0x22]

    op hex (2)
    0000   0x22 0x13                                  ".
    decimal
             34   19
    datetime ((2005, 2, 0, 27, 13, 18))
    0000   0x12 0x8d 0x5b 0x00 0x85                   ..[..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 Base (2000, 4, 16, 25, 13, 50) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x14                                  1.
    decimal
             49   20
    datetime ((2000, 4, 16, 25, 13, 50))
    0000   0x72 0x0d 0x19 0x90 0x00                   r....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 4 Base (2000, 0, 24, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 24, 0, 0, 54))
    0000   0x36 0x00 0x00 0x58 0x00                   6..X.
    body (0)
    DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-19.data: 5 records`
