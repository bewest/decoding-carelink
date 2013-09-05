## START logs/ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 32, found 10 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x66 0x85 0x00 0x00 0x00 0x00 0x00 0x00    f.......
    0008   0x00 0x00 0x7b 0x01 0x80 0x00 0x04 0x01    ..{.....
    0010   0x0d 0x08 0x21 0x00 0x7b 0x02 0x80 0x00    ..!.{...
    0018   0x08 0x01 0x0d 0x10 0x22 0x00 0x33 0x50    ....".3P
##### DEBUG DECIMAL
            102  133    0    0    0    0    0    0
              0    0  123    1  128    0    4    1
             13    8   33    0  123    2  128    0
              8    1   13   16   34    0   51   80
#### RECORD 0 Base (2000, 8, 17, 0, 5, 13) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x7f                                  n.
    decimal
            110  127
    datetime ((2000, 8, 17, 0, 5, 13))
    0000   0x8d 0x05 0x00 0x71 0x00                   ...q.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2002, 0, 2, 3, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2002, 0, 2, 3, 0, 0))
    0000   0x00 0x00 0x03 0xe2 0x02                   .....
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 2 Base (2004, 0, 0, 30, 40, 1) head[2], body[0] op[0xba]

    op hex (2)
    0000   0xba 0x46                                  .F
    decimal
            186   70
    datetime ((2004, 0, 0, 30, 40, 1))
    0000   0x01 0x28 0x1e 0x00 0x64                   .(..d
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 3 Bolus (2005, 0, 0, 0, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x00 0x00                        .(..
    decimal
              1   40    0    0
    datetime ((2005, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x05                   .....
    body (0)

`end logs/ReadHistoryData-page-16.data: 4 records`
