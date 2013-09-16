## START logs/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 249, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x38 0x36 0x5c 0x0b 0x4e 0x64 0x14 0x1e    86\.Nd..
    0008   0x6e 0x14 0x38 0x96 0x14 0x69 0xd1 0x82    n.8..i..
    0010   0x01 0x72 0x01 0x0d 0x15 0x1e 0x01 0x00    .r......
    0018   0x38 0x00 0x38 0x00 0x00 0x00 0x81 0x01    8.8.....
##### DEBUG DECIMAL
             56   54   92   11   78  100   20   30
            110   20   56  150   20  105  209  130
              1  114    1   13   21   30    1    0
             56    0   56    0    0    0  129    1
#### RECORD 0 CalBGForPH 2013-08-01T08:32:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-01T08:32:07)
    0000   0x87 0x20 0x28 0x61 0x0d                   . (a.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2013, 8, 1, 8, 32, 7) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime ((2013, 8, 1, 8, 32, 7))
    0000   0x87 0x20 0x88 0x61 0x0d                   . .a.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Base (2000, 9, 23, 24, 27, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2000, 9, 23, 24, 27, 22))
    0000   0x96 0x5b 0x38 0x97 0x20                   .[8. 
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 3 ChangeBasalProfile (2014, 0, 0, 16, 24, 13) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x61                                  .a
    decimal
              8   97
    datetime ((2014, 0, 0, 16, 24, 13))
    0000   0x0d 0x18 0x90 0x00 0x6e                   ....n
    body (44)
    hex
    0000   0x17 0x36 0x00 0x00 0x54 0x00 0x00 0x00    .6..T...
    0008   0x00 0x54 0x36 0x69 0x08 0x97 0x20 0x08    .T6i.. .
    0010   0x01 0x0d 0x0a 0x1e 0x01 0x00 0x54 0x00    ......T.
    0018   0x54 0x00 0x00 0x00 0x97 0x20 0x48 0x61    T.... Ha
    0020   0x0d 0x7b 0x02 0x80 0x1e 0x09 0x01 0x0d    .{......
    0028   0x13 0x1e 0x00 0x0a                        ....
    decimal
             23   54    0    0   84    0    0    0
              0   84   54  105    8  151   32    8
              1   13   10   30    1    0   84    0
             84    0    0    0  151   32   72   97
             13  123    2  128   30    9    1   13
             19   30    0   10
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 Base (2015, 0, 13, 1, 43, 7) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0xb2                                  L.
    decimal
             76  178
    datetime ((2015, 0, 13, 1, 43, 7))
    0000   0x07 0x2b 0x61 0x0d 0x3f                   .+a.?
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 5 Base (2009, 2, 13, 1, 11, 7) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0xb2                                  ..
    decimal
              9  178
    datetime ((2009, 2, 13, 1, 11, 7))
    0000   0x07 0x8b 0x61 0x0d 0x69                   ..a.i
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 6 Base (2011, 0, 22, 3, 48, 10) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x96                                  i.
    decimal
            105  150
    datetime ((2011, 0, 22, 3, 48, 10))
    0000   0x0a 0x30 0xa3 0x16 0x4b                   .0..K
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 7 Bolus (2014, 0, 0, 16, 19, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 9.1, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x0d 0x5b 0x30 0xa7 0x16 0x0b 0x61    ..[0...a
    decimal
              1   13   91   48  167   22   11   97
    datetime ((2014, 0, 0, 16, 19, 13))
    0000   0x0d 0x13 0x90 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 8 ChangeTime 2000-12-24T04:00:52 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x36                                  .6
    decimal
             23   54
    datetime (2000-12-24T04:00:52)
    0000   0xf4 0x00 0x44 0xf8 0x00                   ..D..
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 9 Base (2004, 0, 5, 28, 54, 56) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2004, 0, 5, 28, 54, 56))
    0000   0x38 0x36 0x5c 0x05 0x54                   86\.T
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 10 Base (2011, 4, 22, 7, 11, 41) head[2], body[0] op[0xb1]

    op hex (2)
    0000   0xb1 0x04                                  ..
    decimal
            177    4
    datetime ((2011, 4, 22, 7, 11, 41))
    0000   0x69 0x0b 0xa7 0x16 0x0b                   i....
    body (0)

#### RECORD 11 Bolus (2007, 0, 0, 16, 0, 56) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x0d 0x0e 0x1e 0x01 0x00 0x38 0x00    ......8.
    decimal
              1   13   14   30    1    0   56    0
    datetime ((2007, 0, 0, 16, 0, 56))
    0000   0x38 0x00 0x10 0x00 0xa7                   8....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 12 TempBasalDuration (2014, 4, 0, 27, 13, 33) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 2250}
```
    op hex (2)
    0000   0x16 0x4b                                  .K
    decimal
             22   75
    datetime ((2014, 4, 0, 27, 13, 33))
    0000   0x61 0x0d 0x5b 0x00 0x9e                   a.[..
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 13 Base (2000, 4, 16, 30, 13, 33) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x0c                                  ..
    decimal
              4   12
    datetime ((2000, 4, 16, 30, 13, 33))
    0000   0x61 0x0d 0x1e 0x90 0x00                   a....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 14 Sara6E 2009-01-31T13:33:45 head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x17 0x36 0x00 0x00 0x6c 0x00 0x00    n.6..l..
    0008   0x00 0x00 0x6c 0x36 0x5c 0x08 0x38 0x31    ..l6\.81
    0010   0x04 0x54 0xdb 0x04 0x01 0x00 0x6c 0x00    .T....l.
    0018   0x6c 0x00 0x38 0x00 0x9e 0x04 0x4c 0x61    l.8...La
    0020   0x0d 0x7b 0x03 0x80 0x00 0x0d 0x01 0x0d    .{......
    0028   0x1a 0x26 0x00 0x0a 0x4d 0x8e 0x10         .&..M..
    decimal
            110   23   54    0    0  108    0    0
              0    0  108   54   92    8   56   49
              4   84  219    4    1    0  108    0
            108    0   56    0  158    4   76   97
             13  123    3  128    0   13    1   13
             26   38    0   10   77  142   16
    datetime (2009-01-31T13:33:45)
    0000   0x2d 0x61 0x0d 0x3f 0x09                   -a.?.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1]
#### RECORD 15 Base (2009, 9, 9, 13, 33, 45) head[2], body[0] op[0x8e]

    op hex (2)
    0000   0x8e 0x10                                  ..
    decimal
            142   16
    datetime ((2009, 9, 9, 13, 33, 45))
    0000   0xad 0x61 0x0d 0x69 0x69                   .a.ii
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 16 Base (2001, 6, 18, 0, 16, 55) head[2], body[0] op[0x96]

    op hex (2)
    0000   0x96 0x0a                                  ..
    decimal
            150   10
    datetime ((2001, 6, 18, 0, 16, 55))
    0000   0x77 0x90 0x00 0x32 0x61                   w..2a
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 17 Base (2001, 2, 18, 0, 16, 14) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2001, 2, 18, 0, 16, 14))
    0000   0x0e 0x90 0x00 0xf2 0x61                   ....a
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 18 Base (2001, 6, 2, 27, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2001, 6, 2, 27, 22, 41))
    0000   0x69 0x96 0x5b 0x42 0x81                   i.[B.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 19 Bolus (2004, 0, 0, 20, 54, 23) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 9.7, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x12 0x61 0x0d 0x0a 0x90 0x00 0x6e    ..a....n
    decimal
              1   18   97   13   10  144    0  110
    datetime ((2004, 0, 0, 20, 54, 23))
    0000   0x17 0x36 0x14 0x00 0x24                   .6..$
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
`end logs/ReadHistoryData-page-30.data: 20 records`
