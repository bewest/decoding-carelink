## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 193, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x2c 0x85 0x23 0x29 0x0f 0x0d 0x7b 0x02    ,.#)..{.
    0008   0xb6 0x23 0x09 0x0f 0x0d 0x13 0x1e 0x00    .#......
    0010   0x03 0x00 0x09 0x00 0x09 0x93 0x23 0x09    ......#.
    0018   0x0f 0x0d 0x0a 0xde 0xb5 0x02 0x2c 0x6f    ......,o
##### DEBUG DECIMAL
             44  133   35   41   15   13  123    2
            182   35    9   15   13   19   30    0
              3    0    9    0    9  147   35    9
             15   13   10  222  181    2   44  111
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
#### RECORD 6 Base (2008, 8, 25, 22, 10, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2008, 8, 25, 22, 10, 22))
    0000   0x96 0x0a 0x56 0xb9 0x08                   ..V..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 7 Rewind (2008, 0, 25, 10, 63, 13) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x6f                                  !o
    decimal
             33  111
    datetime ((2008, 0, 25, 10, 63, 13))
    0000   0x0d 0x3f 0x0a 0xb9 0x08                   .?...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1]
#### RECORD 8 Base (2011, 1, 22, 9, 41, 13) head[2], body[0] op[0xc1]

    op hex (2)
    0000   0xc1 0x6f                                  .o
    decimal
            193  111
    datetime ((2011, 1, 22, 9, 41, 13))
    0000   0x0d 0x69 0x69 0x96 0x7b                   .ii.{
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 9 Bolus 2005-01-01T00:27:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 12.8, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x80 0x00 0x04 0x0f 0x0d 0x08 0x2e    ........
    decimal
              1  128    0    4   15   13    8   46
    datetime (2005-01-01T00:27:00)
    0000   0x00 0x5b 0x00 0x81 0x35                   .[..5
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 10 ChangeBasalProfile (2014, 0, 0, 16, 50, 13) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x6f                                  .o
    decimal
              8  111
    datetime ((2014, 0, 0, 16, 50, 13))
    0000   0x0d 0x32 0x90 0x00 0x6e                   .2..n
    body (44)
    hex
    0000   0x17 0x36 0x00 0x00 0xb4 0x00 0x00 0x00    .6......
    0008   0x00 0xb4 0x36 0x69 0x08 0x81 0x35 0x08    ..6i..5.
    0010   0x0f 0x0d 0x0a 0x1e 0x01 0x00 0xb4 0x00    ........
    0018   0xb4 0x00 0x00 0x00 0x81 0x35 0x48 0x6f    .....5Ho
    0020   0x0d 0x7b 0x02 0x80 0x1e 0x09 0x0f 0x0d    .{......
    0028   0x13 0x1e 0x00 0x21                        ...!
    decimal
             23   54    0    0  180    0    0    0
              0  180   54  105    8  129   53    8
             15   13   10   30    1    0  180    0
            180    0    0    0  129   53   72  111
             13  123    2  128   30    9   15   13
             19   30    0   33
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 11 Base (2003, 0, 13, 15, 9, 31) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x87                                  ..
    decimal
              0  135
    datetime ((2003, 0, 13, 15, 9, 31))
    0000   0x1f 0x09 0x0f 0x0d 0x03                   .....
    body (0)

`end logs/ReadHistoryData-page-21.data: 12 records`
