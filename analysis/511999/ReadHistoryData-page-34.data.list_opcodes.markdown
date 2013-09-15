## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 314, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x44 0x1a 0x00 0x00 0x00 0x00 0x00 0x00    D.......
    0008   0x00 0x00 0x7b 0x01 0x40 0xc0 0x04 0x05    ..{.@...
    0010   0x0d 0x08 0x1e 0x00 0x08 0x04 0x62 0xf7    ......b.
    0018   0x07 0x05 0x0d 0x00 0x20 0x00 0x08 0x1e    .... ...
##### DEBUG DECIMAL
             68   26    0    0    0    0    0    0
              0    0  123    1   64  192    4    5
             13    8   30    0    8    4   98  247
              7    5   13    0   32    0    8   30
#### RECORD 0 Bolus (2003, 4, 0, 16, 0, 56) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x78 0x00                        ..x.
    decimal
              1    0  120    0
    datetime ((2003, 4, 0, 16, 0, 56))
    0000   0x78 0x00 0x10 0x00 0x53                   x...S
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 1 Base (2010, 4, 6, 27, 13, 36) head[2], body[0] op[0xc1]

    op hex (2)
    0000   0xc1 0x53                                  .S
    decimal
            193   83
    datetime ((2010, 4, 6, 27, 13, 36))
    0000   0x64 0x0d 0x5b 0xc6 0x5a                   d.[.Z
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 2 Base (2000, 0, 16, 20, 13, 4) head[2], body[0] op[0xc8]

    op hex (2)
    0000   0xc8 0x13                                  ..
    decimal
            200   19
    datetime ((2000, 0, 16, 20, 13, 4))
    0000   0x04 0x0d 0x14 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 3 ChangeTimeDisplay 2000-04-16T00:52:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-16T00:52:36)
    0000   0x64 0x34 0x00 0x50 0x00                   d4.P.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 4 Base (2001, 1, 28, 24, 16, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x84                                  ..
    decimal
              0  132
    datetime ((2001, 1, 28, 24, 16, 0))
    0000   0x00 0x50 0x78 0x5c 0x11                   .Px\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 Base (2000, 12, 0, 22, 16, 0) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x0e                                  x.
    decimal
            120   14
    datetime ((2000, 12, 0, 22, 16, 0))
    0000   0xc0 0x10 0x36 0xc0 0x40                   ..6.@
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 6 ChangeBasalProfile 2010-04-04T16:38:08 head[2], body[42] op[0x08]

    op hex (2)
    0000   0x08 0xd0                                  ..
    decimal
              8  208
    datetime (2010-04-04T16:38:08)
    0000   0x48 0x26 0xd0 0x44 0xda                   H&.D.
    body (42)
    hex
    0000   0xd0 0x01 0x00 0x50 0x00 0x50 0x00 0x84    ...P.P..
    0008   0x00 0x5a 0xc8 0x53 0x04 0x0d 0x0a 0x1a    .Z.S....
    0010   0x6b 0xd9 0x33 0x04 0x8d 0x5b 0x1a 0x71    k.3..[.q
    0018   0xd9 0x13 0x64 0x0d 0x04 0x51 0x00 0x64    ..d..Q.d
    0020   0x3c 0x64 0x6c 0x00 0x10 0x00 0x00 0xc4    <dl.....
    0028   0x00 0x10                                  ..
    decimal
            208    1    0   80    0   80    0  132
              0   90  200   83    4   13   10   26
            107  217   51    4  141   91   26  113
            217   19  100   13    4   81    0  100
             60  100  108    0   16    0    0  196
              0   16
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 7 Base (2008, 1, 0, 21, 16, 17) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x5c                                  x\
    decimal
            120   92
    datetime ((2008, 1, 0, 21, 16, 17))
    0000   0x11 0x50 0x15 0xc0 0x78                   .P..x
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 8 PumpResume (2009, 1, 0, 0, 7, 16) head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime ((2009, 1, 0, 0, 7, 16))
    0000   0x10 0x47 0xc0 0x40 0x19                   .G.@.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Base (2000, 3, 0, 1, 16, 55) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x48                                  .H
    decimal
            208   72
    datetime ((2000, 3, 0, 1, 16, 55))
    0000   0x37 0xd0 0x01 0x00 0x10                   7....
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 Base (2009, 3, 17, 0, 4, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x10                                  ..
    decimal
              0   16
    datetime ((2009, 3, 17, 0, 4, 0))
    0000   0x00 0xc4 0x00 0x71 0xd9                   ...q.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 11 Base (2013, 0, 12, 18, 10, 13) head[2], body[0] op[0x53]

    op hex (2)
    0000   0x53 0x64                                  Sd
    decimal
             83  100
    datetime ((2013, 0, 12, 18, 10, 13))
    0000   0x0d 0x0a 0x72 0x4c 0xcd                   ..rL.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 12 LowReservoir 2013-01-15T18:27:13 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.4}
```
    op hex (2)
    0000   0x34 0x04                                  4.
    decimal
             52    4
    datetime (2013-01-15T18:27:13)
    0000   0x0d 0x5b 0x72 0x6f 0xcd                   .[ro.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 13 SelectBasalProfile (2004, 0, 0, 16, 13, 13) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x64                                  .d
    decimal
             20  100
    datetime ((2004, 0, 0, 16, 13, 13))
    0000   0x0d 0x0d 0x50 0x00 0x64                   ..P.d
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 14 Base (2000, 0, 0, 20, 0, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x64                                  <d
    decimal
             60  100
    datetime ((2000, 0, 0, 20, 0, 0))
    0000   0x00 0x00 0x34 0x00 0x00                   ..4..
    body (0)

#### RECORD 15 Base (2000, 1, 20, 28, 56, 52) head[2], body[0] op[0x88]

    op hex (2)
    0000   0x88 0x00                                  ..
    decimal
            136    0
    datetime ((2000, 1, 20, 28, 56, 52))
    0000   0x34 0x78 0x5c 0x14 0x10                   4x\..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 16 Base (2015, 5, 24, 0, 5, 16) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0xc0                                  1.
    decimal
             49  192
    datetime ((2015, 5, 24, 0, 5, 16))
    0000   0x50 0x45 0xc0 0x78 0x4f                   PE.xO
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 17 Base (2000, 7, 9, 0, 0, 55) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x10                                  ..
    decimal
            192   16
    datetime ((2000, 7, 9, 0, 0, 55))
    0000   0x77 0xc0 0x40 0x49 0xd0                   w.@I.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 18 Base (2000, 12, 20, 0, 1, 16) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x67                                  Hg
    decimal
             72  103
    datetime ((2000, 12, 20, 0, 1, 16))
    0000   0xd0 0x01 0x00 0x34 0x00                   ...4.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 19 LowReservoir 2004-08-13T15:00:08 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.0}
```
    op hex (2)
    0000   0x34 0x00                                  4.
    decimal
             52    0
    datetime (2004-08-13T15:00:08)
    0000   0x88 0x00 0x6f 0xcd 0x54                   ..o.T
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 20 ChangeTimeDisplay (2005, 0, 25, 8, 12, 10) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x0d                                  d.
    decimal
            100   13
    datetime ((2005, 0, 25, 8, 12, 10))
    0000   0x0a 0x0c 0x48 0xf9 0x35                   ..H.5
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 21 Base (2005, 4, 25, 20, 12, 27) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x8d                                  ..
    decimal
              4  141
    datetime ((2005, 4, 25, 20, 12, 27))
    0000   0x5b 0x0c 0x54 0xf9 0x15                   [.T..
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 22 ChangeTimeDisplay 2012-01-04T00:17:21 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x0d                                  d.
    decimal
            100   13
    datetime (2012-01-04T00:17:21)
    0000   0x15 0x51 0x00 0x64 0x3c                   .Q.d<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 23 ChangeTimeDisplay (2012, 1, 0, 0, 20, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x60                                  d`
    decimal
            100   96
    datetime ((2012, 1, 0, 0, 20, 0))
    0000   0x00 0x54 0x00 0x00 0x1c                   .T...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 24 Base (2007, 5, 8, 26, 28, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x98                                  ..
    decimal
              0  152
    datetime ((2007, 5, 8, 26, 28, 56))
    0000   0x78 0x5c 0x1a 0x28 0x67                   x\.(g
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 25 Base (2000, 7, 25, 16, 0, 49) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x0c                                  ..
    decimal
            192   12
    datetime ((2000, 7, 25, 16, 0, 49))
    0000   0x71 0xc0 0x10 0x99 0xc0                   q....
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 26 Base (2000, 13, 0, 23, 56, 0) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0xad                                  P.
    decimal
             80  173
    datetime ((2000, 13, 0, 23, 56, 0))
    0000   0xc0 0x78 0xb7 0xc0 0x10                   .x...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 27 Base (2015, 6, 8, 16, 49, 0) head[2], body[0] op[0xdf]

    op hex (2)
    0000   0xdf 0xc0                                  ..
    decimal
            223  192
    datetime ((2015, 6, 8, 16, 49, 0))
    0000   0x40 0xb1 0xd0 0x48 0xcf                   @..H.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 28 Base (2000, 2, 24, 0, 24, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 2, 24, 0, 24, 0))
    0000   0x00 0x98 0x00 0x98 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0]
#### RECORD 29 Base (2013, 7, 4, 21, 57, 20) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x00                                  ..
    decimal
             28    0
    datetime ((2013, 7, 4, 21, 57, 20))
    0000   0x54 0xf9 0x55 0x64 0x0d                   T.Ud.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 Base (2013, 7, 5, 0, 0, 0) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime ((2013, 7, 5, 0, 0, 0))
    0000   0x40 0xc0 0x00 0x05 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 31 Base (2006, 0, 0, 0, 7, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x20                                  . 
    decimal
              0   32
    datetime ((2006, 0, 0, 0, 7, 0))
    0000   0x00 0x07 0x00 0x00 0x06                   .....
    body (0)

#### RECORD 32 PumpResume (2014, 8, 0, 0, 0, 13) head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x64                                  .d
    decimal
             31  100
    datetime ((2014, 8, 0, 0, 0, 13))
    0000   0x8d 0x00 0x00 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 33 ChangeTimeDisplay (2000, 0, 0, 28, 0, 5) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x8d                                  d.
    decimal
            100  141
    datetime ((2000, 0, 0, 28, 0, 5))
    0000   0x05 0x00 0xbc 0x00 0x00                   .....
    body (0)

#### RECORD 34 CalBGForPH (2003, 0, 2, 31, 6, 0) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime ((2003, 0, 2, 31, 6, 0))
    0000   0x00 0x06 0x1f 0x02 0xe3                   .....
    body (0)
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 35 Base (2001, 0, 1, 0, 53, 60) head[2], body[0] op[0x2f]

    op hex (2)
    0000   0x2f 0x03                                  /.
    decimal
             47    3
    datetime ((2001, 0, 1, 0, 53, 60))
    0000   0x3c 0x35 0x00 0xa1 0x01                   <5...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1]
#### RECORD 36 Base (2004, 0, 0, 0, 1, 44) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x00                                  ,.
    decimal
             44    0
    datetime ((2004, 0, 0, 0, 1, 44))
    0000   0x2c 0x01 0xa0 0x00 0x44                   ,...D
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 37 NoDelivery (2000, 0, 0, 0, 0, 4) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x01 0x03 0x01                        ....
    decimal
              6    1    3    1
    datetime ((2000, 0, 0, 0, 0, 4))
    0000   0x04 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-34.data: 38 records`
