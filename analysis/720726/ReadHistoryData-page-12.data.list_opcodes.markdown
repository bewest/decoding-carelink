## START logs/ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 32, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x70 0x36 0x5c 0x11 0x58 0x09 0x04 0xa8    p6\.X...
    0008   0x8b 0x04 0x48 0xa9 0x04 0x34 0x3f 0x14    ..H..4?.
    0010   0x5c 0x67 0x14 0x01 0x00 0x84 0x00 0x84    \g......
    0018   0x00 0xa4 0x00 0xac 0x2b 0x40 0x7b 0x0c    ....+@{.
##### DEBUG DECIMAL
            112   54   92   17   88    9    4  168
            139    4   72  169    4   52   63   20
             92  103   20    1    0  132    0  132
              0  164    0  172   43   64  123   12
#### RECORD 0 Bolus (2008, 4, 0, 20, 0, 24) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x58 0x00                        ..X.
    decimal
              1    0   88    0
    datetime ((2008, 4, 0, 20, 0, 24))
    0000   0x58 0x00 0x54 0x00 0xb8                   X.T..
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 1 Base (2012, 4, 0, 27, 12, 59) head[2], body[0] op[0x25]

    op hex (2)
    0000   0x25 0x40                                  %@
    decimal
             37   64
    datetime ((2012, 4, 0, 27, 12, 59))
    0000   0x7b 0x0c 0x5b 0x00 0xac                   {.[..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 2 Base (2000, 4, 16, 31, 12, 59) head[2], body[0] op[0x2b]

    op hex (2)
    0000   0x2b 0x00                                  +.
    decimal
             43    0
    datetime ((2000, 4, 16, 31, 12, 59))
    0000   0x7b 0x0c 0x1f 0x90 0x00                   {....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 3 Base (2000, 0, 16, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 16, 0, 0, 54))
    0000   0x36 0x00 0x00 0x70 0x00                   6..p.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-12.data: 4 records`
