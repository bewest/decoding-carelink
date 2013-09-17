## START logs/ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 72, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x50 0x78 0x01 0x00 0x50 0x00 0x50 0x00    Px..P.P.
    0008   0x00 0x00 0x5e 0xf2 0x4a 0x63 0x0d 0x0a    ..^.Jc..
    0010   0xbf 0x67 0xf2 0x2b 0x03 0x0d 0x5b 0xbf    .g.+..[.
    0018   0x4d 0xf3 0x0b 0x63 0x0d 0x00 0x50 0x00    M..c..P.
##### DEBUG DECIMAL
             80  120    1    0   80    0   80    0
              0    0   94  242   74   99   13   10
            191  103  242   43    3   13   91  191
             77  243   11   99   13    0   80    0
#### RECORD 0 Base (2013, 7, 3, 4, 0, 0) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime ((2013, 7, 3, 4, 0, 0))
    0000   0x40 0xc0 0x04 0x03 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 ChangeBasalProfile (2000, 1, 0, 2, 59, 0) head[2], body[42] op[0x08]

    op hex (2)
    0000   0x08 0x1e                                  ..
    decimal
              8   30
    datetime ((2000, 1, 0, 2, 59, 0))
    0000   0x00 0x7b 0x02 0x40 0xc0                   .{.@.
    body (42)
    hex
    0000   0x08 0x03 0x0d 0x10 0x24 0x00 0x33 0x50    ....$.3P
    0008   0x62 0xcc 0x08 0x03 0x0d 0x08 0x16 0x03    b.......
    0010   0x62 0xcc 0x08 0x03 0x0d 0x7b 0x02 0x62    b....{.b
    0018   0xea 0x09 0x03 0x0d 0x10 0x24 0x00 0x0a    .....$..
    0020   0x6a 0x4c 0xf2 0x2a 0x03 0x0d 0x5b 0x6a    jL.*..[j
    0028   0x5e 0xf2                                  ^.
    decimal
              8    3   13   16   36    0   51   80
             98  204    8    3   13    8   22    3
             98  204    8    3   13  123    2   98
            234    9    3   13   16   36    0   10
            106   76  242   42    3   13   91  106
             94  242
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 2 CalBGForPH (2008, 0, 0, 16, 25, 13) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime ((2008, 0, 0, 16, 25, 13))
    0000   0x0d 0x19 0x50 0x00 0x78                   ..P.x
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 3 Base (2000, 0, 0, 16, 0, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x64                                  <d
    decimal
             60  100
    datetime ((2000, 0, 0, 16, 0, 0))
    0000   0x00 0x00 0x50 0x00 0x00                   ..P..
    body (0)

`end logs/ReadHistoryData-page-35.data: 4 records`
