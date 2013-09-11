## START logs/ReadHistoryData-page-10.data
#### STOPPING DOUBLE NULLS @ 32, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x48 0x36 0x5c 0x0b 0x90 0x14 0x04 0xbc    H6\.....
    0008   0x96 0x04 0x34 0xa0 0x04 0x01 0x00 0x48    ..4....H
    0010   0x00 0x48 0x00 0xd4 0x00 0x8f 0x15 0x55    .H.....U
    0018   0x7e 0x0d 0x01 0x00 0x18 0x00 0x18 0x01    ~.......
##### DEBUG DECIMAL
             72   54   92   11  144   20    4  188
            150    4   52  160    4    1    0   72
              0   72    0  212    0  143   21   85
            126   13    1    0   24    0   24    1
#### RECORD 0 Bolus (2005, 8, 0, 24, 0, 16) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x90 0x00                        ....
    decimal
              1    0  144    0
    datetime ((2005, 8, 0, 24, 0, 16))
    0000   0x90 0x00 0x58 0x00 0xb5                   ..X..
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 1 Base (2015, 4, 0, 27, 13, 62) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x55                                  .U
    decimal
              5   85
    datetime ((2015, 4, 0, 27, 13, 62))
    0000   0x7e 0x0d 0x5b 0x00 0x8f                   ~.[..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 Base (2000, 4, 16, 20, 13, 62) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x15                                  ..
    decimal
             21   21
    datetime ((2000, 4, 16, 20, 13, 62))
    0000   0x7e 0x0d 0x14 0x90 0x00                   ~....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 3 Base (2000, 0, 8, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 8, 0, 0, 54))
    0000   0x36 0x00 0x00 0x48 0x00                   6..H.
    body (0)
    DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-10.data: 4 records`
