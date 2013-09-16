## START logs/ReadHistoryData-page-9.data
#### STOPPING DOUBLE NULLS @ 40, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x5c 0x5c 0x00 0x00 0x00 0x00 0x00 0x00    \\......
    0008   0x00 0x00 0x7b 0x01 0x80 0x40 0x04 0x01    ..{..@..
    0010   0x0d 0x08 0x2e 0x00 0x34 0x0a 0x9f 0x64    ....4..d
    0018   0x05 0x01 0x8d 0x7b 0x02 0x80 0x5e 0x09    ...{..^.
##### DEBUG DECIMAL
             92   92    0    0    0    0    0    0
              0    0  123    1  128   64    4    1
             13    8   46    0   52   10  159  100
              5    1  141  123    2  128   94    9
#### RECORD 0 Base (2000, 0, 28, 0, 6, 13) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x9f                                  n.
    decimal
            110  159
    datetime ((2000, 0, 28, 0, 6, 13))
    0000   0x0d 0x06 0x00 0x5c 0x00                   ...\.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 1 Base (2003, 0, 13, 8, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x01                                  ..
    decimal
              0    1
    datetime ((2003, 0, 13, 8, 0, 0))
    0000   0x00 0x00 0x08 0x6d 0x03                   ...m.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 2 Base (2001, 3, 1, 26, 38, 4) head[2], body[0] op[0x87]

    op hex (2)
    0000   0x87 0x2a                                  .*
    decimal
            135   42
    datetime ((2001, 3, 1, 26, 38, 4))
    0000   0x04 0xe6 0x3a 0x01 0x51                   ..:.Q
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 3 Prime 2000-04-10T16:00:04 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x52 0x00 0x00 0x01                   .R...
    decimal
              3   82    0    0    1
    datetime (2000-04-10T16:00:04)
    0000   0x44 0x00 0x50 0x0a 0x00                   D.P..
    body (0)

#### RECORD 4 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x02]

    op hex (2)
    0000   0x02 0x01                                  ..
    decimal
              2    1
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-9.data: 5 records`
