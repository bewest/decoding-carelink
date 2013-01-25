WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-1.data
#### RECORD 0 CalForBG 2013-01-14T22:11:48 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-01-14T22:11:48)
    0000   0x30 0x4b 0x36 0x0e 0x0d                   0K6..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 1 CalForBG 2013-01-14T22:35:17 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-01-14T22:35:17)
    0000   0x11 0x63 0x36 0x0e 0x0d                   .c6..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 2 CalForBG 2013-01-14T22:35:46 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-01-14T22:35:46)
    0000   0x2e 0x63 0x36 0x0e 0x0d                   .c6..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 3 BolusWizard 2013-01-14T22:36:00 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x53                                  [S
    decimal
             91   83
    datetime (2013-01-14T22:36:00)
    0000   0x00 0x64 0x16 0x0e 0x0d                   .d...
    body (13)
    hex
    0000   0x5e 0x50 0x0d 0x2d 0x6a 0xfb 0x48 0xf0    ^P.-j.H.
    0008   0x00 0x0a 0x00 0x43 0x7d                   ...C}
    decimal
             94   80   13   45  106  251   72  240
              0   10    0   67  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x1a 0x24 0x70 0x04 0x14 0x84 0x04    \.$p....
0008   0x0e                                       .
special found
0000   0xac 0x04 0x06 0xb6 0x04 0x58 0xd4 0x04    .....X..
0008   0x60 0x24 0x14 0x54 0x7e 0x14 0x2c 0x9c    `$.T~.,.
0010   0x14 0x01 0x43 0x43 0x00                   ..CC.
should eat up to null, second bytearray(b'')
#### RECORD 4 BolusGiven? 2013-01-14T22:36:00 head[30], body[0] 0x5c
    op hex (30)
    0000   0x5c 0x1a 0x24 0x70 0x04 0x14 0x84 0x04    \.$p....
    0008   0x0e 0xac 0x04 0x06 0xb6 0x04 0x58 0xd4    ......X.
    0010   0x04 0x60 0x24 0x14 0x54 0x7e 0x14 0x2c    .`$.T~.,
    0018   0x9c 0x14 0x01 0x43 0x43 0x00              ...CC.
    decimal
             92   26   36  112    4   20  132    4
             14  172    4    6  182    4   88  212
              4   96   36   20   84  126   20   44
            156   20    1   67   67    0
    datetime (2013-01-14T22:36:00)
    0000   0x00 0x64 0x56 0x0e 0x0d                   .dV..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 5 CalForBG 2013-01-14T23:48:39 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x96                                  ..
    decimal
             10  150
    datetime (2013-01-14T23:48:39)
    0000   0x27 0x70 0x37 0x0e 0x0d                   'p7..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 6 ResultTotals 2013-02-14T13:13:14 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0xc8                   .....
    decimal
              7    0    0   10  200
    datetime (2013-02-14T13:13:14)
    0000   0x0e 0x8d 0x6d 0x0e 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x11 0x1a 0x46 0xc7 0x19 0x00 0x00    ...F....
    0008   0x0a 0xc8 0x03 0xc6 0x23 0x07 0x02 0x41    ....#..A
    0010   0x00 0x7a 0x07 0x02 0x41 0x01 0x60 0x14    .z..A.`.
    0018   0x05 0xa2 0x50 0x00 0x00 0x00 0x12 0x02    ..P.....
    0020   0x10 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   17   26   70  199   25    0    0
             10  200    3  198   35    7    2   65
              0  122    7    2   65    1   96   20
              5  162   80    0    0    0   18    2
             16    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 7 CalForBG 2013-01-15T01:20:10 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-01-15T01:20:10)
    0000   0x0a 0x54 0x21 0x0f 0x0d                   .T!..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 8 PumpSuspend 2013-01-15T14:34:10 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-15T14:34:10)
    0000   0x0a 0x62 0x0e 0x0f 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 9 PumpResume 2013-01-15T14:54:09 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-15T14:54:09)
    0000   0x09 0x76 0x0e 0x0f 0x0d                   .v...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 10 CalForBG 2013-01-15T15:57:04 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-01-15T15:57:04)
    0000   0x04 0x79 0x2f 0x0f 0x0d                   .y/..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 11 BolusWizard 2013-01-15T15:57:16 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2013-01-15T15:57:16)
    0000   0x10 0x79 0x0f 0x0f 0x0d                   .y...
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0xfb 0x16 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             29   80   13   45  106  251   22  240
              0    0    0   17  125
    HOUR BITS: [0, 1, 1]

#### RECORD 12 Bolus 2013-01-15T15:57:16 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-01-15T15:57:16)
    0000   0x10 0x79 0x4f 0x0f 0x0d                   .yO..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 13 CalForBG 2013-01-15T16:02:29 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-01-15T16:02:29)
    0000   0x1d 0x42 0x30 0x0f 0x0d                   .B0..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 14 BolusWizard 2013-01-15T16:02:43 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-01-15T16:02:43)
    0000   0x2b 0x42 0x10 0x0f 0x0d                   +B...
    body (13)
    hex
    0000   0x4c 0x50 0x0d 0x2d 0x6a 0x00 0x3a 0x00    LP.-j.:.
    0008   0x00 0x11 0x00 0x3a 0x7d                   ...:}
    decimal
             76   80   13   45  106    0   58    0
              0   17    0   58  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x44 0x08 0x04 0x01 0x3a 0x3a    \.D...::
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 15 BolusGiven? 2013-01-15T16:02:43 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x44 0x08 0x04 0x01 0x3a 0x3a    \.D...::
    0008   0x00                                       .
    decimal
             92    5   68    8    4    1   58   58
              0
    datetime (2013-01-15T16:02:43)
    0000   0x2b 0x42 0x50 0x0f 0x0d                   +BP..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 16 CalForBG 2013-01-15T17:48:28 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2013-01-15T17:48:28)
    0000   0x1c 0x70 0x31 0x0f 0x0d                   .p1..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 17 CalForBG 2013-01-15T18:25:33 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xde                                  ..
    decimal
             10  222
    datetime (2013-01-15T18:25:33)
    0000   0x21 0x59 0x32 0x0f 0x0d                   !Y2..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 18 BolusWizard 2013-01-15T18:25:44 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xde                                  [.
    decimal
             91  222
    datetime (2013-01-15T18:25:44)
    0000   0x2c 0x59 0x12 0x0f 0x0d                   ,Y...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0   24    0    0  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x08 0x9e 0x8d 0x04 0x8e 0x97 0x04    \.......
0008   0x01                                       .
special found
0000   0x03 0x03 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 19 BolusGiven? 2013-01-15T18:25:44 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0x9e 0x8d 0x04 0x8e 0x97 0x04    \.......
    0008   0x01 0x03 0x03 0x00                        ....
    decimal
             92    8  158  141    4  142  151    4
              1    3    3    0
    datetime (2013-01-15T18:25:44)
    0000   0x2c 0x59 0x52 0x0f 0x0d                   ,YR..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 20 CalForBG 2013-01-15T18:45:59 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xcb                                  ..
    decimal
             10  203
    datetime (2013-01-15T18:45:59)
    0000   0x3b 0x6d 0x32 0x0f 0x0d                   ;m2..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 21 BolusWizard 2013-01-15T18:46:17 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xcb                                  [.
    decimal
             91  203
    datetime (2013-01-15T18:46:17)
    0000   0x11 0x6e 0x12 0x0f 0x0d                   .n...
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x11 0x2a 0x00    7P.-j.*.
    0008   0x00 0x14 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106   17   42    0
              0   20    0   42  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x0b 0x0c 0x16 0x04 0x9e 0xa2 0x04    \.......
0008   0x8e                                       .
special found
0000   0xac 0x04 0x01 0x2a 0x2a 0x00              ...**.
should eat up to null, second bytearray(b'')
#### RECORD 22 BolusGiven? 2013-01-15T18:46:17 head[15], body[0] 0x5c
    op hex (15)
    0000   0x5c 0x0b 0x0c 0x16 0x04 0x9e 0xa2 0x04    \.......
    0008   0x8e 0xac 0x04 0x01 0x2a 0x2a 0x00         ....**.
    decimal
             92   11   12   22    4  158  162    4
            142  172    4    1   42   42    0
    datetime (2013-01-15T18:46:17)
    0000   0x11 0x6e 0x52 0x0f 0x0d                   .nR..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 23 ResultTotals 2013-02-15T13:13:15 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x56                   ....V
    decimal
              7    0    0    5   86
    datetime (2013-02-15T13:13:15)
    0000   0x0f 0x8d 0x6d 0x0f 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x9b 0x4c 0xeb 0x06 0x00 0x00    ...L....
    0008   0x05 0x56 0x03 0x76 0x41 0x01 0xe0 0x23    .V.vA..#
    0010   0x00 0xa0 0x01 0xe0 0x23 0x01 0xd4 0x61    ....#..a
    0018   0x00 0x0c 0x03 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  155   76  235    6    0    0
              5   86    3  118   65    1  224   35
              0  160    1  224   35    1  212   97
              0   12    3    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 24 CalForBG 2013-01-16T06:19:00 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xf5                                  ..
    decimal
             10  245
    datetime (2013-01-16T06:19:00)
    0000   0x00 0x53 0x26 0x10 0x0d                   .S&..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 25 BolusWizard 2013-01-16T06:19:02 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xf5                                  [.
    decimal
             91  245
    datetime (2013-01-16T06:19:02)
    0000   0x02 0x53 0x06 0x10 0x0d                   .S...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0    0    0   26  125
    HOUR BITS: [0, 1, 0]

#### RECORD 26 Bolus 2013-01-16T06:19:02 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-01-16T06:19:02)
    0000   0x02 0x53 0x46 0x10 0x0d                   .SF..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 27 CalForBG 2013-01-16T12:24:46 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-01-16T12:24:46)
    0000   0x2e 0x58 0x2c 0x10 0x0d                   .X,..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 28 BolusWizard 2013-01-16T12:24:50 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-01-16T12:24:50)
    0000   0x32 0x58 0x0c 0x10 0x0d                   2X...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x68 0x72 0x14 0x01 0x0c 0x0c    \.hr....
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 29 BolusGiven? 2013-01-16T12:24:51 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x68 0x72 0x14 0x01 0x0c 0x0c    \.hr....
    0008   0x00                                       .
    decimal
             92    5  104  114   20    1   12   12
              0
    datetime (2013-01-16T12:24:51)
    0000   0x33 0x58 0x4c 0x10 0x0d                   3XL..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 30 PumpSuspend 2013-01-16T15:50:08 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-16T15:50:08)
    0000   0x08 0x72 0x0f 0x10 0x0d                   .r...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 31 PumpResume 2013-01-16T16:11:19 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-16T16:11:19)
    0000   0x13 0x4b 0x10 0x10 0x0d                   .K...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 32 CalForBG 2013-01-16T16:29:02 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2013-01-16T16:29:02)
    0000   0x02 0x5d 0x30 0x10 0x0d                   .]0..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 33 BolusWizard 2013-01-16T16:29:23 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2013-01-16T16:29:23)
    0000   0x17 0x5d 0x10 0x10 0x0d                   .]...
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0xf8 0x14 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             27   80   13   45  106  248   20  240
              0    0    0   12  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x30 0xf5 0x04 0x01 0x0c 0x0c    \.0.....
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 34 BolusGiven? 2013-01-16T16:29:23 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x30 0xf5 0x04 0x01 0x0c 0x0c    \.0.....
    0008   0x00                                       .
    decimal
             92    5   48  245    4    1   12   12
              0
    datetime (2013-01-16T16:29:23)
    0000   0x17 0x5d 0x50 0x10 0x0d                   .]P..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 35 CalForBG 2013-01-16T17:46:01 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-01-16T17:46:01)
    0000   0x01 0x6e 0x31 0x10 0x0d                   .n1..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 36 BolusWizard 2013-01-16T17:46:44 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-01-16T17:46:44)
    0000   0x2c 0x6e 0x11 0x10 0x0d                   ,n...
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    9    0   18  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x08 0x30 0x52 0x04 0x30 0x42 0x14    \.0R.0B.
0008   0x01                                       .
special found
0000   0x12 0x12 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 37 BolusGiven? 2013-01-16T17:46:44 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0x30 0x52 0x04 0x30 0x42 0x14    \.0R.0B.
    0008   0x01 0x12 0x12 0x00                        ....
    decimal
             92    8   48   82    4   48   66   20
              1   18   18    0
    datetime (2013-01-16T17:46:44)
    0000   0x2c 0x6e 0x51 0x10 0x0d                   ,nQ..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 38 CalForBG 2013-01-16T20:42:20 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-01-16T20:42:20)
    0000   0x14 0x6a 0x34 0x10 0x0d                   .j4..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 39 BolusWizard 2013-01-16T20:42:37 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-01-16T20:42:37)
    0000   0x25 0x6a 0x14 0x10 0x0d                   %j...
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xfd 0x18 0xf0     P.-j...
    0008   0x00 0x04 0x00 0x15 0x7d                   ....}
    decimal
             32   80   13   45  106  253   24  240
              0    4    0   21  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x08 0x48 0xb2 0x04 0x30 0x02 0x14    \.H..0..
0008   0x01                                       .
special found
0000   0x15 0x15 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 40 BolusGiven? 2013-01-16T20:42:37 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0x48 0xb2 0x04 0x30 0x02 0x14    \.H..0..
    0008   0x01 0x15 0x15 0x00                        ....
    decimal
             92    8   72  178    4   48    2   20
              1   21   21    0
    datetime (2013-01-16T20:42:37)
    0000   0x25 0x6a 0x54 0x10 0x0d                   %jT..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 41 ResultTotals 2013-02-16T13:13:16 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xda                   .....
    decimal
              7    0    0    4  218
    datetime (2013-02-16T13:13:16)
    0000   0x10 0x8d 0x6d 0x10 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x89 0x47 0xf5 0x05 0x00 0x00    ...G....
    0008   0x04 0xda 0x03 0x76 0x47 0x01 0x64 0x1d    ...vG.d.
    0010   0x00 0x53 0x01 0x64 0x1d 0x00 0xcc 0x39    .S.d...9
    0018   0x00 0x98 0x2b 0x00 0x00 0x00 0x05 0x03    ..+.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  137   71  245    5    0    0
              4  218    3  118   71    1  100   29
              0   83    1  100   29    0  204   57
              0  152   43    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 42 PumpSuspend 2013-01-17T13:51:09 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-17T13:51:09)
    0000   0x09 0x73 0x0d 0x11 0x0d                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 43 PumpResume 2013-01-17T14:09:56 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-17T14:09:56)
    0000   0x38 0x49 0x0e 0x11 0x0d                   8I...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 44 CalForBG 2013-01-17T16:59:39 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-01-17T16:59:39)
    0000   0x27 0x7b 0x30 0x11 0x0d                   '{0..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 45 BolusWizard 2013-01-17T16:59:46 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-01-17T16:59:46)
    0000   0x2e 0x7b 0x10 0x11 0x0d                   .{...
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0xfc 0x06 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x02 0x7d                   ....}
    decimal
              8   80   13   45  106  252    6  240
              0    0    0    2  125
    HOUR BITS: [0, 1, 1]

#### RECORD 46 Bolus 2013-01-17T16:59:46 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-01-17T16:59:46)
    0000   0x2e 0x7b 0x50 0x11 0x0d                   .{P..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 47 LowReservoir 2013-01-17T17:12:37 head[2], body[0] 0x34
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-01-17T17:12:37)
    0000   0x25 0x4c 0x11 0x11 0x0d                   %L...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 48 CalForBG 2013-01-17T18:09:19 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xed                                  ..
    decimal
             10  237
    datetime (2013-01-17T18:09:19)
    0000   0x13 0x49 0x32 0x11 0x0d                   .I2..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 49 BolusWizard 2013-01-17T18:09:39 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xed                                  [.
    decimal
             91  237
    datetime (2013-01-17T18:09:39)
    0000   0x27 0x49 0x12 0x11 0x0d                   'I...
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0x18 0x28 0x00    5P.-j.(.
    0008   0x00 0x02 0x00 0x3e 0x7d                   ...>}
    decimal
             53   80   13   45  106   24   40    0
              0    2    0   62  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x08 0x4b 0x04 0x01 0x3e 0x3e    \..K..>>
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 50 BolusGiven? 2013-01-17T18:09:39 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x08 0x4b 0x04 0x01 0x3e 0x3e    \..K..>>
    0008   0x00                                       .
    decimal
             92    5    8   75    4    1   62   62
              0
    datetime (2013-01-17T18:09:39)
    0000   0x27 0x49 0x52 0x11 0x0d                   'IR..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 51 BolusWizard 2013-01-17T19:05:21 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-01-17T19:05:21)
    0000   0x15 0x45 0x13 0x11 0x0d                   .E...
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x08 0xf8 0x3d 0x04 0x08 0x83 0x04    \..=....
0008   0x34                                       4
super super special
special found
0000   0x46 0x13 0x11 0x0d 0x01 0x17 0x17 0x00    F.......
should eat up to null, second bytearray(b'')
#### RECORD 52 BolusGiven? 2013-01-17T19:05:21 head[19], body[0] 0x5c
    op hex (19)
    0000   0x5c 0x08 0xf8 0x3d 0x04 0x08 0x83 0x04    \..=....
    0008   0x34 0x64 0x29 0x46 0x13 0x11 0x0d 0x01    4d)F....
    0010   0x17 0x17 0x00                             ...
    decimal
             92    8  248   61    4    8  131    4
             52  100   41   70   19   17   13    1
             23   23    0
    datetime (2013-01-17T19:05:21)
    0000   0x15 0x45 0x53 0x11 0x0d                   .ES..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 53 ResultTotals 2013-02-17T13:13:17 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime (2013-02-17T13:13:17)
    0000   0x11 0x8d 0x6d 0x11 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xa3 0x58 0xed 0x02 0x00 0x00    ...X....
    0008   0x04 0xd2 0x03 0x76 0x48 0x01 0x5c 0x1c    ...vH.\.
    0010   0x00 0x5b 0x01 0x5c 0x1c 0x01 0x04 0x4b    .[.\...K
    0018   0x00 0x58 0x19 0x00 0x00 0x00 0x03 0x02    .X......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  163   88  237    2    0    0
              4  210    3  118   72    1   92   28
              0   91    1   92   28    1    4   75
              0   88   25    0    0    0    3    2
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 54 PumpSuspend 2013-01-18T14:31:19 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-18T14:31:19)
    0000   0x13 0x5f 0x0e 0x12 0x0d                   ._...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 55 PumpResume 2013-01-18T15:11:31 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-18T15:11:31)
    0000   0x1f 0x4b 0x0f 0x12 0x0d                   .K...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 56 CalForBG 2013-01-18T15:36:48 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2013-01-18T15:36:48)
    0000   0x30 0x64 0x2f 0x12 0x0d                   0d/..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 57 BolusWizard 2013-01-18T15:37:04 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2013-01-18T15:37:04)
    0000   0x04 0x65 0x0f 0x12 0x0d                   .e...
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x03 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             26   80   13   45  106    3   20    0
              0    0    0   23  125
    HOUR BITS: [0, 1, 1]

#### RECORD 58 Bolus 2013-01-18T15:37:04 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-01-18T15:37:04)
    0000   0x04 0x65 0x4f 0x12 0x0d                   .eO..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 59 Rewind 2013-01-18T18:53:14 head[2], body[0] 0x21
    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-01-18T18:53:14)
    0000   0x0e 0x75 0x12 0x12 0x0d                   .u...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 60 Prime 2013-01-18T18:55:41 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x29                   ....)
    decimal
              3    0    0    0   41
    datetime (2013-01-18T18:55:41)
    0000   0x29 0x77 0x32 0x12 0x0d                   )w2..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 61 Prime 2013-01-18T18:56:00 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-01-18T18:56:00)
    0000   0x00 0x78 0x12 0x12 0x0d                   .x...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 62 CalForBG 2013-01-18T19:07:12 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-01-18T19:07:12)
    0000   0x0c 0x47 0x33 0x12 0x0d                   .G3..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 63 BolusWizard 2013-01-18T19:08:03 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-01-18T19:08:03)
    0000   0x03 0x48 0x13 0x12 0x0d                   .H...
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0xfc 0x24 0xf0    /P.-j.$.
    0008   0x00 0x02 0x00 0x20 0x7d                   ... }
    decimal
             47   80   13   45  106  252   36  240
              0    2    0   32  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x5c 0xd6 0x04 0x01 0x20 0x20    \.\...  
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 64 BolusGiven? 2013-01-18T19:08:03 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x5c 0xd6 0x04 0x01 0x20 0x20    \.\...  
    0008   0x00                                       .
    decimal
             92    5   92  214    4    1   32   32
              0
    datetime (2013-01-18T19:08:03)
    0000   0x03 0x48 0x53 0x12 0x0d                   .HS..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 65 BolusWizard 2013-01-18T20:10:52 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-01-18T20:10:52)
    0000   0x34 0x4a 0x14 0x12 0x0d                   4J...
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x08 0x80 0x42 0x04 0x5c 0x14 0x14    \..B.\..
0008   0x01                                       .
special found
0000   0x0d 0x0d 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 66 BolusGiven? 2013-01-18T20:10:52 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0x80 0x42 0x04 0x5c 0x14 0x14    \..B.\..
    0008   0x01 0x0d 0x0d 0x00                        ....
    decimal
             92    8  128   66    4   92   20   20
              1   13   13    0
    datetime (2013-01-18T20:10:52)
    0000   0x34 0x4a 0x54 0x12 0x0d                   4JT..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 67 ResultTotals MIDNIGHT!?: (2000, 2, 0, 0, 13, 18) head[5], body[14] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x78                   ....x
    decimal
              7    0    0    4  120
    datetime (MIDNIGHT!?: (2000, 2, 0, 0, 13, 18))
    0000   0x12 0x8d 0x00 0x00 0x00                   .....
    body (14)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x2c 0xf3              ....,.
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0   44  243
    HOUR BITS: [1, 0, 0]

`end logs/ReadHistoryData-page-1.data: 68 records`
