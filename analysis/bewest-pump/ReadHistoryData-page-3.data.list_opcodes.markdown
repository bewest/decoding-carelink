WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-3.data
#### RECORD 0 BolusWizard 2013-01-11T17:19:20 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x1e                                  [.
    decimal
             91   30
    datetime (2013-01-11T17:19:20)
    0000   0x14 0x53 0x11 0x0b 0x0d                   .S...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00 0x00    .Q.-j#..
    0008   0x00 0x0e 0x00 0x15 0x7d                   ....}
    decimal
              0   81   13   45  106   35    0    0
              0   14    0   21  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x64 0x69 0x04 0x01 0x1a 0x1a    \.di....
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 1 BolusGiven? 2013-01-11T17:19:20 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x64 0x69 0x04 0x01 0x1a 0x1a    \.di....
    0008   0x00                                       .
    decimal
             92    5  100  105    4    1   26   26
              0
    datetime (2013-01-11T17:19:20)
    0000   0x14 0x53 0x51 0x0b 0x0d                   .SQ..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 2 CalForBG 2013-01-11T18:13:50 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-01-11T18:13:50)
    0000   0x32 0x4d 0x32 0x0b 0x8d                   2M2..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 3 BolusWizard 2013-01-11T18:14:05 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x53                                  [S
    decimal
             91   83
    datetime (2013-01-11T18:14:05)
    0000   0x05 0x4e 0x12 0x0b 0x0d                   .N...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2f 0x00 0x00    .Q.-j/..
    0008   0x00 0x1c 0x00 0x13 0x7d                   ....}
    decimal
              0   81   13   45  106   47    0    0
              0   28    0   19  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x08 0x68 0x3c 0x04 0x64 0xa0 0x04    \.h<.d..
0008   0x01                                       .
special found
0000   0x18 0x18 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 4 BolusGiven? 2013-01-11T18:14:05 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0x68 0x3c 0x04 0x64 0xa0 0x04    \.h<.d..
    0008   0x01 0x18 0x18 0x00                        ....
    decimal
             92    8  104   60    4  100  160    4
              1   24   24    0
    datetime (2013-01-11T18:14:05)
    0000   0x05 0x4e 0x52 0x0b 0x0d                   .NR..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 5 CalForBG 2013-01-11T18:43:40 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x24                                  .$
    decimal
             10   36
    datetime (2013-01-11T18:43:40)
    0000   0x28 0x6b 0x32 0x0b 0x8d                   (k2..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]

#### RECORD 6 CalForBG 2013-01-11T19:12:57 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xd6                                  ..
    decimal
             10  214
    datetime (2013-01-11T19:12:57)
    0000   0x39 0x4c 0x33 0x0b 0x0d                   9L3..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 7 CalForBG 2013-01-11T19:59:23 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-01-11T19:59:23)
    0000   0x17 0x7b 0x33 0x0b 0x0d                   .{3..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 8 CalForBG 2013-01-11T20:00:10 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-01-11T20:00:10)
    0000   0x0a 0x40 0x34 0x0b 0x0d                   .@4..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 9 BolusWizard 2013-01-11T20:00:33 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-01-11T20:00:33)
    0000   0x21 0x40 0x14 0x0b 0x0d                   !@...
    body (13)
    hex
    0000   0x58 0x50 0x0d 0x2d 0x6a 0x02 0x43 0x00    XP.-j.C.
    0008   0x00 0x13 0x00 0x43 0x7d                   ...C}
    decimal
             88   80   13   45  106    2   67    0
              0   19    0   67  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0b 0x60 0x6a 0x04 0x68 0xa6 0x04    \.`j.h..
0008   0x64                                       d
super special
special found
0000   0x21 0x40 0x74 0x0b 0x0d 0x07 0x00         !@t....
#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x5c 0x0b 0x60 0x6a 0x04 0x68 0xa6 0x04    \.`j.h..
    0008   0x64 0x0a 0x14 0x01 0x43 0x43 0x04 0x21    d...CC.!
    0010   0x40 0x74 0x0b 0x0d 0x07 0x00 0x00 0x05    @t......
    0018   0xa6 0x0b 0x8d 0x6d 0x0b 0x8d 0x05 0x10    ...m....
    0020   0xde 0x88 0x53 0x07 0x00 0x00 0x05 0xa6    ..S.....
    0028   0x03 0x6e 0x3d 0x02 0x38 0x27 0x00 0x72    .n=.8'.r
    0030   0x02 0x38 0x27                             .8'
##### DEBUG DECIMAL
             92   11   96  106    4  104  166    4
            100   10   20    1   67   67    4   33
             64  116   11   13    7    0    0    5
            166   11  141  109   11  141    5   16
            222  136   83    7    0    0    5  166
              3  110   61    2   56   39    0  114
              2   56   39
XXX:???:XXX 2004-04-10T00:11:28
`end logs/ReadHistoryData-page-3.data: 10 records`
