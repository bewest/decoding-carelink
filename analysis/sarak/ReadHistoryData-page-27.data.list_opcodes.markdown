## START logs/ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 39, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x77 0x49 0x00 0x00 0x00 0x00 0x00 0x00    wI......
    0008   0x00 0x00 0x7b 0x01 0x40 0xc0 0x04 0x0e    ..{.@...
    0010   0x0d 0x08 0x1d 0x00 0x7b 0x02 0x40 0xc0    ....{.@.
    0018   0x08 0x0e 0x0d 0x10 0x22 0x00 0x08 0x04    ...."...
##### DEBUG DECIMAL
            119   73    0    0    0    0    0    0
              0    0  123    1   64  192    4   14
             13    8   29    0  123    2   64  192
              8   14   13   16   34    0    8    4
#### RECORD 0 Base (2000, 8, 25, 0, 5, 13) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x6d                                  nm
    decimal
            110  109
    datetime ((2000, 8, 25, 0, 5, 13))
    0000   0x8d 0x05 0x00 0xd9 0x00                   .....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 1 Base (2002, 0, 2, 6, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2002, 0, 2, 6, 0, 0))
    0000   0x00 0x00 0x06 0x02 0x02                   .....
    body (0)

#### RECORD 2 Base (2011, 1, 0, 22, 4, 3) head[2], body[0] op[0xbe]

    op hex (2)
    0000   0xbe 0x2e                                  ..
    decimal
            190   46
    datetime ((2011, 1, 0, 22, 4, 3))
    0000   0x03 0x44 0x36 0x00 0x7b                   .D6.{
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 3 Bolus (2003, 2, 0, 0, 44, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 8.0, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x50 0x01 0x48                        .P.H
    decimal
              1   80    1   72
    datetime ((2003, 2, 0, 0, 44, 0))
    0000   0x00 0xac 0x00 0x00 0x03                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 4 Base (2000, 0, 0, 0, 4, 0) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x01                                  ..
    decimal
              4    1
    datetime ((2000, 0, 0, 0, 4, 0))
    0000   0x00 0x04 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-27.data: 5 records`
