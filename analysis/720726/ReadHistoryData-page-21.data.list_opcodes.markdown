## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 144, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb4 0x00 0x00 0x00 0x00 0xb4 0x36 0x69    ......6i
    0008   0x08 0x81 0x35 0x08 0x0f 0x0d 0x0a 0x1e    ..5.....
    0010   0x01 0x00 0xb4 0x00 0xb4 0x00 0x00 0x00    ........
    0018   0x81 0x35 0x48 0x6f 0x0d 0x7b 0x02 0x80    .5Ho.{..
##### DEBUG DECIMAL
            180    0    0    0    0  180   54  105
              8  129   53    8   15   13   10   30
              1    0  180    0  180    0    0    0
            129   53   72  111   13  123    2  128
#### RECORD 0 Bolus 2013-08-14T22:00:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x98 0x00    ..0.0...
    decimal
              1    0   48    0   48    0  152    0
    datetime (2013-08-14T22:00:08)
    0000   0x88 0x00 0x56 0x6e 0x0d                   ..Vn.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 1 BasalProfileStart 2013-08-15T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-15T00:00:00)
    0000   0x80 0x00 0x00 0x0f 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 2 ResultTotals (2000, 8, 0, 0, 13, 14) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xff                   .....
    decimal
              7    0    0    6  255
    datetime ((2000, 8, 0, 0, 13, 14))
    0000   0x8e 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 3 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x8e 0x0d 0x06 0x00 0x92 0x4f 0xd4    n.....O.
    0008   0x02 0x00 0x00 0x06 0xff 0x03 0x89 0x33    .......3
    0010   0x03 0x76 0x31 0x00 0xc4 0x01 0xba 0x00    .v1.....
    0018   0x88 0x01 0x04 0x00 0x30 0x05 0x02 0x02    ....0...
    0020   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  142   13    6    0  146   79  212
              2    0    0    6  255    3  137   51
              3  118   49    0  196    1  186    0
            136    1    4    0   48    5    2    2
              1    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 4 CalBGForPH 2013-08-15T00:05:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2013-08-15T00:05:51)
    0000   0xb3 0x05 0x20 0x6f 0x0d                   .. o.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 5 Base (2013, 8, 15, 0, 5, 51) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime ((2013, 8, 15, 0, 5, 51))
    0000   0xb3 0x05 0xe0 0x6f 0x0d                   ...o.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 Ian69 2008-08-25T22:10:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2008-08-25T22:10:22)
    0000   0x96 0x0a 0x56 0xb9 0x08                   ..V..
    body (8)
    hex
    0000   0x21 0x6f 0x0d 0x3f 0x0a 0xb9 0x08 0xc1    !o.?....
    decimal
             33  111   13   63   10  185    8  193
    DAY BITS: [1, 0, 1]
#### RECORD 7 Base (2001, 5, 27, 22, 41, 41) head[2], body[0] op[0x6f]

    op hex (2)
    0000   0x6f 0x0d                                  o.
    decimal
            111   13
    datetime ((2001, 5, 27, 22, 41, 41))
    0000   0x69 0x69 0x96 0x7b 0x01                   ii.{.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Base (2014, 0, 8, 13, 15, 4) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x00                                  ..
    decimal
            128    0
    datetime ((2014, 0, 8, 13, 15, 4))
    0000   0x04 0x0f 0x0d 0x08 0x2e                   .....
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 9 Base (2015, 2, 8, 21, 1, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x5b                                  .[
    decimal
              0   91
    datetime ((2015, 2, 8, 21, 1, 0))
    0000   0x00 0x81 0x35 0x08 0x6f                   ..5.o
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 10 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x32                                  .2
    decimal
             13   50
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-21.data: 11 records`
