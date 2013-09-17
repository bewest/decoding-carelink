## START logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 71, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x02 0x16 0x02 0x16 0x64 0x00 0x00 0x00    ....d...
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x07 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              2   22    2   22  100    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    7    0    0    0    0
#### RECORD 0 old6c (2008, 0, 0, 12, 5, 6) head[2], body[38] op[0x6c]

    op hex (2)
    0000   0x6c 0xc2                                  l.
    decimal
            108  194
    datetime ((2008, 0, 0, 12, 5, 6))
    0000   0x06 0x05 0x0c 0x00 0xe8                   .....
    body (38)
    hex
    0000   0x00 0x00 0x00 0x00 0x03 0x36 0x03 0x36    .....6.6
    0008   0x64 0x00 0x00 0x00 0x00 0x00 0x00 0x00    d.......
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x06    ........
    0020   0x3e 0x03 0x60 0xde 0x34 0x50              >.`.4P
    decimal
              0    0    0    0    3   54    3   54
            100    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    6
             62    3   96  222   52   80
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 1 Base (2005, 0, 23, 12, 0, 33) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0x06                                  C.
    decimal
             67    6
    datetime ((2005, 0, 23, 12, 0, 33))
    0000   0x21 0x00 0xcc 0x17 0x15                   !....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 2 Prime (2012, 0, 6, 3, 22, 2) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.7, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x06 0x07 0x00 0x00                   .....
    decimal
              3    6    7    0    0
    datetime ((2012, 0, 6, 3, 22, 2))
    0000   0x02 0x16 0xc3 0x06 0x6c                   ....l
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 3 Base (2000, 0, 8, 0, 12, 5) head[2], body[0] op[0xc3]

    op hex (2)
    0000   0xc3 0x06                                  ..
    decimal
            195    6
    datetime ((2000, 0, 8, 0, 12, 5))
    0000   0x05 0x0c 0x00 0xe8 0x00                   .....
    body (0)
    DAY BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-4.data: 4 records`
