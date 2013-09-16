## START logs/ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 41, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xdf 0xdf 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x0a 0x66 0xa2 0x4f 0x21 0x65    ...f.O!e
    0010   0x0d 0x3f 0x0c 0xa2 0x4f 0xc1 0x65 0x0d    .?..O.e.
    0018   0x72 0x90 0x70 0x0a 0xa5 0x84 0x70 0x22    r.p...p"
##### DEBUG DECIMAL
            223  223    0    0    0    0    0    0
              0    0   10  102  162   79   33  101
             13   63   12  162   79  193  101   13
            114  144  112   10  165  132  112   34
#### RECORD 0 Base (2010, 8, 13, 0, 6, 13) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x84                                  n.
    decimal
            110  132
    datetime ((2010, 8, 13, 0, 6, 13))
    0000   0x8d 0x06 0x00 0xcd 0xba                   .....
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 1 Base (2003, 0, 17, 6, 0, 0) head[2], body[0] op[0xba]

    op hex (2)
    0000   0xba 0x02                                  ..
    decimal
            186    2
    datetime ((2003, 0, 17, 6, 0, 0))
    0000   0x00 0x00 0x06 0xb1 0x03                   .....
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 2 Base (2008, 0, 0, 15, 40, 3) head[2], body[0] op[0x89]

    op hex (2)
    0000   0x89 0x35                                  .5
    decimal
            137   53
    datetime ((2008, 0, 0, 15, 40, 3))
    0000   0x03 0x28 0x2f 0x00 0xa8                   .(/..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 3 Bolus (2005, 1, 0, 0, 44, 1) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.6, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x4c 0x00 0x70                        .L.p
    decimal
              1   76    0  112
    datetime ((2005, 1, 0, 0, 44, 1))
    0000   0x01 0x6c 0x00 0x00 0x05                   .l...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 Bolus (2000, 0, 0, 0, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x00 0x00                        ....
    decimal
              1    3    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-6.data: 5 records`
