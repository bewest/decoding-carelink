## START logs/ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 102, found 15 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x07 0x00 0x00 0x03 0x36 0xa5 0x06 0x6c    ....6..l
    0008   0xa5 0x06 0x05 0x0c 0x00 0xe8 0x00 0x00    ........
    0010   0x00 0x00 0x03 0x36 0x03 0x36 0x64 0x00    ...6.6d.
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              7    0    0    3   54  165    6  108
            165    6    5   12    0  232    0    0
              0    0    3   54    3   54  100    0
              0    0    0    0    0    0    0    0
#### RECORD 0 ResultTotals 2006-08-03T12:06:35 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x36                   ....6
    decimal
              7    0    0    3   54
    datetime (2006-08-03T12:06:35)
    0000   0xa3 0x06 0x6c 0xa3 0x06                   ..l..
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x03 0x36 0x03 0x36 0x64 0x00 0x00 0x00    .6.6d...
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x21 0x00 0x93 0x80 0x08    ...!....
    0028   0x04                                       .
    decimal
              5   12    0  232    0    0    0    0
              3   54    3   54  100    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0   33    0  147  128    8
              4
    DAY BITS: [1, 0, 1]
#### RECORD 1 NoDelivery (2008, 0, 11, 21, 13, 0) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x03 0x00 0x00                        ....
    decimal
              6    3    0    0
    datetime ((2008, 0, 11, 21, 13, 0))
    0000   0x00 0x0d 0x95 0x8b 0x28                   ....(
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 2 Base (2003, 0, 0, 3, 0, 3) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x06                                  ..
    decimal
              4    6
    datetime ((2003, 0, 0, 3, 0, 3))
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    body (0)

#### RECORD 3 Base (2000, 0, 7, 6, 4, 8) head[2], body[0] op[0x9e]

    op hex (2)
    0000   0x9e 0x8b                                  ..
    decimal
            158  139
    datetime ((2000, 0, 7, 6, 4, 8))
    0000   0x08 0x04 0x06 0x07 0x00                   .....
    body (0)

#### RECORD 4 Base (2004, 2, 12, 6, 36, 48) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x03                                  ..
    decimal
              0    3
    datetime ((2004, 2, 12, 6, 36, 48))
    0000   0x30 0xa4 0x06 0x6c 0xa4                   0..l.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 5 NoDelivery (2000, 12, 0, 0, 0, 40) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x05 0x0c 0x00                        ....
    decimal
              6    5   12    0
    datetime ((2000, 12, 0, 0, 0, 40))
    0000   0xe8 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 6 Prime (2000, 0, 0, 0, 0, 0) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 10.0, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x30 0x03 0x30 0x64                   .0.0d
    decimal
              3   48    3   48  100
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-7.data: 7 records`
