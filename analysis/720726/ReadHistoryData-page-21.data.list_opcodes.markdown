## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 18, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0f 0x0d 0x00 0x20 0x00 0x07 0x00 0x00    ... ....
    0008   0x06 0xff 0x8e 0x0d 0x00 0x00 0x00 0x6e    .......n
    0010   0x8e 0x0d 0x06 0x00 0x92 0x4f 0xd4 0x02    .....O..
    0018   0x00 0x00 0x06 0xff 0x03 0x89 0x33 0x03    ......3.
##### DEBUG DECIMAL
             15   13    0   32    0    7    0    0
              6  255  142   13    0    0    0  110
            142   13    6    0  146   79  212    2
              0    0    6  255    3  137   51    3
#### RECORD 0 Bolus (2008, 0, 0, 24, 0, 48) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x30 0x00                        ..0.
    decimal
              1    0   48    0
    datetime ((2008, 0, 0, 24, 0, 48))
    0000   0x30 0x00 0x98 0x00 0x88                   0....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 Base (2000, 4, 0, 27, 13, 46) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x56                                  .V
    decimal
              0   86
    datetime ((2000, 4, 0, 27, 13, 46))
    0000   0x6e 0x0d 0x7b 0x00 0x80                   n.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-21.data: 2 records`
