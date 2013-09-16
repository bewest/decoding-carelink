## START logs/ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 170, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x50 0x82 0x5c 0x05 0x40 0xd3 0xc0 0x01    P.\.@...
    0008   0x00 0x50 0x00 0x50 0x00 0x00 0x00 0xb9    .P.P....
    0010   0x18 0x44 0x1e 0x0d 0x7b 0x02 0x80 0x00    .D..{...
    0018   0x08 0x1e 0x0d 0x10 0x22 0x00 0x0a 0x82    ...."...
##### DEBUG DECIMAL
             80  130   92    5   64  211  192    1
              0   80    0   80    0    0    0  185
             24   68   30   13  123    2  128    0
              8   30   13   16   34    0   10  130
#### RECORD 0 Bolus 2013-08-29T19:50:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x48 0x00    ..T.T.H.
    decimal
              1    0   84    0   84    0   72    0
    datetime (2013-08-29T19:50:04)
    0000   0x84 0x32 0x53 0x1d 0x0d                   .2S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Sara7B 2013-08-30T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-30T00:00:00)
    0000   0x80 0x00 0x00 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 2 ResultTotals (2000, 8, 0, 0, 13, 29) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x84                   .....
    decimal
              7    0    0    4  132
    datetime ((2000, 8, 0, 0, 13, 29))
    0000   0x9d 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x9d 0x0d 0x05 0x00 0xb0 0x00 0x00    n.......
    0008   0x07 0x00 0x00 0x04 0x84 0x02 0xdc 0x3f    .......?
    0010   0x01 0xa8 0x25 0x00 0x42 0x00 0xe4 0x00    ..%.B...
    0018   0xc4 0x00 0x00 0x00 0x00 0x04 0x03 0x00    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0x09 0x00 0x00 0x00 0x00    ..d.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  157   13    5    0  176    0    0
              7    0    0    4  132    2  220   63
              1  168   37    0   66    0  228    0
            196    0    0    0    0    4    3    0
              0    4    0    0    0    0    0    0
              0    0  100    9    0    0    0    0
              0    0    0

#### RECORD 3 Base (2014, 14, 0, 25, 6, 39) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2014, 14, 0, 25, 6, 39))
    0000   0xe7 0x86 0x39 0x20 0x1e                   ..9 .
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 4 Base (2014, 14, 0, 25, 9, 39) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2014, 14, 0, 25, 9, 39))
    0000   0xe7 0x89 0x39 0x00 0x1e                   ..9..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 Base (2014, 4, 28, 24, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2014, 4, 28, 24, 0, 16))
    0000   0x50 0x00 0x78 0x3c 0x6e                   P.x<n
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 6 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 7 Base (2000, 4, 26, 20, 8, 28) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x82                                  @.
    decimal
             64  130
    datetime ((2000, 4, 26, 20, 8, 28))
    0000   0x5c 0x08 0x54 0x3a 0xd0                   \.T:.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 8 Base (2000, 12, 0, 0, 1, 16) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0x4e                                  LN
    decimal
             76   78
    datetime ((2000, 12, 0, 0, 1, 16))
    0000   0xd0 0x01 0x00 0x40 0x00                   ...@.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 9 Base (2000, 0, 25, 9, 0, 0) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime ((2000, 0, 25, 9, 0, 0))
    0000   0x00 0x00 0x89 0x39 0x40                   ...9@
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 10 PumpSuspend (2004, 4, 0, 0, 1, 59) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x0d                                  ..
    decimal
             30   13
    datetime ((2004, 4, 0, 0, 1, 59))
    0000   0x7b 0x01 0x80 0x00 0x04                   {....
    body (0)

#### RECORD 11 PumpSuspend (2013, 0, 10, 0, 33, 8) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x0d                                  ..
    decimal
             30   13
    datetime ((2013, 0, 10, 0, 33, 8))
    0000   0x08 0x21 0x00 0x0a 0x6d                   .!..m
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 12 Base (2013, 0, 27, 13, 30, 36) head[2], body[0] op[0x89]

    op hex (2)
    0000   0x89 0x18                                  ..
    decimal
            137   24
    datetime ((2013, 0, 27, 13, 30, 36))
    0000   0x24 0x1e 0x0d 0x5b 0x6d                   $..[m
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 13 Base (2000, 0, 25, 13, 30, 4) head[2], body[0] op[0xb9]

    op hex (2)
    0000   0xb9 0x18                                  ..
    decimal
            185   24
    datetime ((2000, 0, 25, 13, 30, 4))
    0000   0x04 0x1e 0x0d 0x19 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 14 Base (2000, 1, 0, 0, 46, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2000, 1, 0, 0, 46, 60))
    0000   0x3c 0x6e 0x00 0x00 0x50                   <n..P
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
`end logs/ReadHistoryData-page-3.data: 15 records`
