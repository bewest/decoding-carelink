## START logs/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 163, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6c 0x36 0x5c 0x08 0x38 0x31 0x04 0x54    l6\.81.T
    0008   0xdb 0x04 0x01 0x00 0x6c 0x00 0x6c 0x00    ....l.l.
    0010   0x38 0x00 0x9e 0x04 0x4c 0x61 0x0d 0x7b    8...La.{
    0018   0x03 0x80 0x00 0x0d 0x01 0x0d 0x1a 0x26    .......&
##### DEBUG DECIMAL
            108   54   92    8   56   49    4   84
            219    4    1    0  108    0  108    0
             56    0  158    4   76   97   13  123
              3  128    0   13    1   13   26   38
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
#### RECORD 3 ChangeBasalProfile (2014, 0, 0, 16, 24, 13) head[2], body[42] op[0x08]

    op hex (2)
    0000   0x08 0x61                                  .a
    decimal
              8   97
    datetime ((2014, 0, 0, 16, 24, 13))
    0000   0x0d 0x18 0x90 0x00 0x6e                   ....n
    body (42)
    hex
    0000   0x17 0x36 0x00 0x00 0x54 0x00 0x00 0x00    .6..T...
    0008   0x00 0x54 0x36 0x69 0x08 0x97 0x20 0x08    .T6i.. .
    0010   0x01 0x0d 0x0a 0x1e 0x01 0x00 0x54 0x00    ......T.
    0018   0x54 0x00 0x00 0x00 0x97 0x20 0x48 0x61    T.... Ha
    0020   0x0d 0x7b 0x02 0x80 0x1e 0x09 0x01 0x0d    .{......
    0028   0x13 0x1e                                  ..
    decimal
             23   54    0    0   84    0    0    0
              0   84   54  105    8  151   32    8
              1   13   10   30    1    0   84    0
             84    0    0    0  151   32   72   97
             13  123    2  128   30    9    1   13
             19   30
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 Base (2001, 6, 11, 7, 50, 12) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2001, 6, 11, 7, 50, 12))
    0000   0x4c 0xb2 0x07 0x2b 0x61                   L..+a
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 5 Base (2001, 2, 11, 7, 50, 9) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2001, 2, 11, 7, 50, 9))
    0000   0x09 0xb2 0x07 0x8b 0x61                   ....a
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 6 Base (2003, 6, 16, 10, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2003, 6, 16, 10, 22, 41))
    0000   0x69 0x96 0x0a 0x30 0xa3                   i..0.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 7 TempBasalDuration (2007, 0, 16, 27, 13, 1) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 2250}
```
    op hex (2)
    0000   0x16 0x4b                                  .K
    decimal
             22   75
    datetime ((2007, 0, 16, 27, 13, 1))
    0000   0x01 0x0d 0x5b 0x30 0xa7                   ..[0.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 8 TempBasalDuration 2000-04-16T19:13:33 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 330}
```
    op hex (2)
    0000   0x16 0x0b                                  ..
    decimal
             22   11
    datetime (2000-04-16T19:13:33)
    0000   0x61 0x0d 0x13 0x90 0x00                   a....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 9 Base (2008, 3, 4, 0, 52, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2008, 3, 4, 0, 52, 54))
    0000   0x36 0xf4 0x00 0x44 0xf8                   6..D.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 10 Base (2005, 0, 28, 22, 56, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x10                                  ..
    decimal
              0   16
    datetime ((2005, 0, 28, 22, 56, 0))
    0000   0x00 0x38 0x36 0x5c 0x05                   .86\.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 11 Base (2006, 1, 7, 11, 41, 4) head[2], body[0] op[0x54]

    op hex (2)
    0000   0x54 0xb1                                  T.
    decimal
             84  177
    datetime ((2006, 1, 7, 11, 41, 4))
    0000   0x04 0x69 0x0b 0xa7 0x16                   .i...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 12 Base (2000, 0, 1, 30, 14, 13) head[2], body[0] op[0x0b]

    op hex (2)
    0000   0x0b 0x01                                  ..
    decimal
             11    1
    datetime ((2000, 0, 1, 30, 14, 13))
    0000   0x0d 0x0e 0x1e 0x01 0x00                   .....
    body (0)

#### RECORD 13 Base (2007, 0, 0, 16, 0, 56) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x00                                  8.
    decimal
             56    0
    datetime ((2007, 0, 0, 16, 0, 56))
    0000   0x38 0x00 0x10 0x00 0xa7                   8....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 14 TempBasalDuration (2014, 4, 0, 27, 13, 33) head[2], body[0] op[0x16]
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
#### RECORD 15 Base (2000, 4, 16, 30, 13, 33) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x0c                                  ..
    decimal
              4   12
    datetime ((2000, 4, 16, 30, 13, 33))
    0000   0x61 0x0d 0x1e 0x90 0x00                   a....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 16 Base (2000, 0, 12, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 12, 0, 0, 54))
    0000   0x36 0x00 0x00 0x6c 0x00                   6..l.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-30.data: 17 records`
