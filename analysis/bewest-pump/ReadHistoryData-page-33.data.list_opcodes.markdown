WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-33.data
#### RECORD 0 ResultTotals 2012-10-20T13:12:20 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime (2012-10-20T13:12:20)
    0000   0x94 0x8c 0x6d 0x94 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x91 0x43 0x1c 0x08 0x00 0x00    ...C....
    0008   0x05 0x08 0x03 0x7a 0x45 0x01 0x8e 0x1f    ...zE...
    0010   0x00 0x50 0x01 0x8e 0x1f 0x00 0xe4 0x39    .P.....9
    0018   0x00 0xaa 0x2b 0x00 0x00 0x00 0x07 0x03    ..+.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  145   67   28    8    0    0
              5    8    3  122   69    1  142   31
              0   80    1  142   31    0  228   57
              0  170   43    0    0    0    7    3
              4    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 1 CalForBG 2012-09-21T17:03:36 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-09-21T17:03:36)
    0000   0xa4 0x43 0x31 0x15 0x0c                   .C1..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 2 BolusWizard 2012-09-21T17:04:04 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2012-09-21T17:04:04)
    0000   0x84 0x44 0x11 0x15 0x0c                   .D...
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0xf8 0x2d 0xf0    ;P.-j.-.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             59   80   13   45  106  248   45  240
              0    0    0   37  125
    HOUR BITS: [0, 1, 0]

#### RECORD 3 Bolus 2012-09-21T17:04:04 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2012-09-21T17:04:04)
    0000   0x84 0x44 0x51 0x15 0x0c                   .DQ..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 4 LowReservoir 2012-09-21T18:22:06 head[2], body[0] 0x34
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-09-21T18:22:06)
    0000   0x86 0x56 0x12 0x15 0x0c                   .V...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 5 CalForBG 2012-09-21T18:36:07 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2012-09-21T18:36:07)
    0000   0x87 0x64 0x32 0x15 0x0c                   .d2..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 6 CalForBG 2012-09-21T18:45:22 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-09-21T18:45:22)
    0000   0x96 0x6d 0x32 0x15 0x0c                   .m2..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 7 BolusWizard 2012-09-21T18:45:30 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2012-09-21T18:45:30)
    0000   0x9e 0x6d 0x12 0x15 0x0c                   .m...
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0   22    0   18  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x94 0x65 0x04 0x01 0x12 0x12    \..e....
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 8 BolusGiven? 2012-09-21T18:45:31 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x94 0x65 0x04 0x01 0x12 0x12    \..e....
    0008   0x00                                       .
    decimal
             92    5  148  101    4    1   18   18
              0
    datetime (2012-09-21T18:45:31)
    0000   0x9f 0x6d 0x52 0x15 0x0c                   .mR..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 9 CalForBG 2012-09-21T22:36:03 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2012-09-21T22:36:03)
    0000   0x83 0x64 0x36 0x15 0x0c                   .d6..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 10 BolusWizard 2012-09-21T22:36:06 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xce                                  [.
    decimal
             91  206
    datetime (2012-09-21T22:36:06)
    0000   0x86 0x64 0x16 0x15 0x0c                   .d...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x11 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0    1    0   17  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x08 0x48 0xe8 0x04 0x94 0x4c 0x14    \.H...L.
0008   0x01                                       .
special found
0000   0x11 0x11 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 11 BolusGiven? 2012-09-21T22:36:06 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0x48 0xe8 0x04 0x94 0x4c 0x14    \.H...L.
    0008   0x01 0x11 0x11 0x00                        ....
    decimal
             92    8   72  232    4  148   76   20
              1   17   17    0
    datetime (2012-09-21T22:36:06)
    0000   0x86 0x64 0x56 0x15 0x0c                   .dV..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 12 BolusWizard 2012-09-21T23:03:22 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-21T23:03:22)
    0000   0x96 0x43 0x17 0x15 0x0c                   .C...
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106    0    7    0
              0    0    0    7  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0b 0x44 0x1d 0x04 0x48 0x03 0x14    \.D..H..
0008   0x94                                       .
special found
0000   0x67 0x14 0x01 0x07 0x07 0x00              g.....
should eat up to null, second bytearray(b'')
#### RECORD 13 BolusGiven? 2012-09-21T23:03:22 head[15], body[0] 0x5c
    op hex (15)
    0000   0x5c 0x0b 0x44 0x1d 0x04 0x48 0x03 0x14    \.D..H..
    0008   0x94 0x67 0x14 0x01 0x07 0x07 0x00         .g.....
    decimal
             92   11   68   29    4   72    3   20
            148  103   20    1    7    7    0
    datetime (2012-09-21T23:03:22)
    0000   0x96 0x43 0x57 0x15 0x0c                   .CW..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 14 BolusWizard 2012-09-21T23:18:04 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-21T23:18:04)
    0000   0x84 0x52 0x17 0x15 0x0c                   .R...
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0e 0x1c 0x18 0x04 0x44 0x2c 0x04    \....D,.
0008   0x48                                       H
special found
0000   0x12 0x14 0x94 0x76 0x14 0x01 0x09 0x09    ...v....
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 15 BolusGiven? 2012-09-21T23:18:04 head[18], body[0] 0x5c
    op hex (18)
    0000   0x5c 0x0e 0x1c 0x18 0x04 0x44 0x2c 0x04    \....D,.
    0008   0x48 0x12 0x14 0x94 0x76 0x14 0x01 0x09    H...v...
    0010   0x09 0x00                                  ..
    decimal
             92   14   28   24    4   68   44    4
             72   18   20  148  118   20    1    9
              9    0
    datetime (2012-09-21T23:18:04)
    0000   0x84 0x52 0x57 0x15 0x0c                   .RW..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 16 LowReservoir 2012-09-21T23:31:34 head[2], body[0] 0x34
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-09-21T23:31:34)
    0000   0xa2 0x5f 0x17 0x15 0x0c                   ._...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 17 ResultTotals 2012-10-21T13:12:21 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe4                   .....
    decimal
              7    0    0    4  228
    datetime (2012-10-21T13:12:21)
    0000   0x95 0x8c 0x6d 0x95 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x83 0x46 0xce 0x04 0x00 0x00    ...F....
    0008   0x04 0xe4 0x03 0x84 0x48 0x01 0x60 0x1c    ....H.`.
    0010   0x00 0x69 0x01 0x60 0x1c 0x01 0x1c 0x51    .i.`...Q
    0018   0x00 0x44 0x13 0x00 0x00 0x00 0x05 0x04    .D......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  131   70  206    4    0    0
              4  228    3  132   72    1   96   28
              0  105    1   96   28    1   28   81
              0   68   19    0    0    0    5    4
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 18 Rewind 2012-09-22T23:11:17 head[2], body[0] 0x21
    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-09-22T23:11:17)
    0000   0x91 0x4b 0x17 0x16 0x0c                   .K...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 19 Prime 2012-09-22T23:13:38 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x38                   ....8
    decimal
              3    0    0    0   56
    datetime (2012-09-22T23:13:38)
    0000   0xa6 0x4d 0x37 0x16 0x0c                   .M7..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 20 Prime 2012-09-22T23:14:01 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-09-22T23:14:01)
    0000   0x81 0x4e 0x17 0x16 0x0c                   .N...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 21 ResultTotals 2012-10-22T13:12:22 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x82                   .....
    decimal
              7    0    0    3  130
    datetime (2012-10-22T13:12:22)
    0000   0x96 0x8c 0x6d 0x96 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x03 0x82 0x03 0x82 0x64 0x00 0x00 0x00    ....d...
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              3  130    3  130  100    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 22 CalForBG 2012-09-23T00:08:00 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2012-09-23T00:08:00)
    0000   0x80 0x48 0x20 0x17 0x0c                   .H ..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 23 BolusWizard 2012-09-23T00:08:50 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2012-09-23T00:08:50)
    0000   0xb2 0x48 0x00 0x17 0x0c                   .H...
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0xfb 0x1e 0xf0    (P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
             40   80   13   45  106  251   30  240
              0    0    0   25  125
    HOUR BITS: [0, 1, 0]

#### RECORD 24 Bolus 2012-09-23T00:08:50 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2012-09-23T00:08:50)
    0000   0xb2 0x48 0x40 0x17 0x0c                   .H@..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 25 PumpSuspend 2012-09-23T03:08:37 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-23T03:08:37)
    0000   0xa5 0x48 0x03 0x17 0x0c                   .H...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 26 PumpResume 2012-09-23T03:08:49 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-23T03:08:49)
    0000   0xb1 0x48 0x03 0x17 0x0c                   .H...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 27 CalForBG 2012-09-23T07:47:11 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2012-09-23T07:47:11)
    0000   0x8b 0x6f 0x27 0x17 0x8c                   .o'..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]

#### RECORD 28 BolusWizard 2012-09-23T07:47:13 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2012-09-23T07:47:13)
    0000   0x8d 0x6f 0x07 0x17 0x0c                   .o...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3c 0x00 0x00    .Q.-j<..
    0008   0x00 0x00 0x00 0x3c 0x7d                   ...<}
    decimal
              0   81   13   45  106   60    0    0
              0    0    0   60  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x64 0xcf 0x14 0x01 0x3c 0x3c    \.d...<<
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 29 BolusGiven? 2012-09-23T07:47:13 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x64 0xcf 0x14 0x01 0x3c 0x3c    \.d...<<
    0008   0x00                                       .
    decimal
             92    5  100  207   20    1   60   60
              0
    datetime (2012-09-23T07:47:13)
    0000   0x8d 0x6f 0x47 0x17 0x0c                   .oG..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 30 PumpSuspend 2012-09-23T08:27:42 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-23T08:27:42)
    0000   0xaa 0x5b 0x08 0x17 0x0c                   .[...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 31 PumpResume 2012-09-23T09:00:21 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-23T09:00:21)
    0000   0x95 0x40 0x09 0x17 0x0c                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 32 CalForBG 2012-09-23T10:55:06 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x40                                  .@
    decimal
             10   64
    datetime (2012-09-23T10:55:06)
    0000   0x86 0x77 0x2a 0x17 0x8c                   .w*..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]

#### RECORD 33 BolusWizard 2012-09-23T10:55:14 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x40                                  [@
    decimal
             91   64
    datetime (2012-09-23T10:55:14)
    0000   0x8e 0x77 0x0a 0x17 0x0c                   .w...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2b 0x00 0x00    .Q.-j+..
    0008   0x00 0x09 0x00 0x22 0x7d                   ..."}
    decimal
              0   81   13   45  106   43    0    0
              0    9    0   34  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x05 0xf0 0xbf 0x04 0x01 0x24 0x24    \.....$$
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 34 BolusGiven? 2012-09-23T10:55:14 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0xf0 0xbf 0x04 0x01 0x24 0x24    \.....$$
    0008   0x00                                       .
    decimal
             92    5  240  191    4    1   36   36
              0
    datetime (2012-09-23T10:55:14)
    0000   0x8e 0x77 0x4a 0x17 0x0c                   .wJ..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 35 CalForBG 2012-09-23T11:48:04 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x2f                                  ./
    decimal
             10   47
    datetime (2012-09-23T11:48:04)
    0000   0x84 0x70 0x2b 0x17 0x8c                   .p+..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]

#### RECORD 36 BolusWizard 2012-09-23T11:48:21 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x2f                                  [/
    decimal
             91   47
    datetime (2012-09-23T11:48:21)
    0000   0x95 0x70 0x0b 0x17 0x0c                   .p...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x27 0x00 0x00    .Q.-j'..
    0008   0x00 0x1f 0x00 0x08 0x7d                   ....}
    decimal
              0   81   13   45  106   39    0    0
              0   31    0    8  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x08 0x90 0x36 0x04 0xf0 0xf4 0x04    \..6....
0008   0x01                                       .
special found
0000   0x0c 0x0c 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 37 BolusGiven? 2012-09-23T11:48:21 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0x90 0x36 0x04 0xf0 0xf4 0x04    \..6....
    0008   0x01 0x0c 0x0c 0x00                        ....
    decimal
             92    8  144   54    4  240  244    4
              1   12   12    0
    datetime (2012-09-23T11:48:21)
    0000   0x95 0x70 0x4b 0x17 0x0c                   .pK..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 38 TempBasal 2012-09-23T11:51:46 head[2], body[1] 0x33
    op hex (2)
    0000   0x33 0x2e                                  3.
    decimal
             51   46
    datetime (2012-09-23T11:51:46)
    0000   0xae 0x73 0x0b 0x17 0x0c                   .s...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 1]

#### RECORD 39 TempBasal[eof] 2012-09-23T11:51:46 head[2], body[0] 0x16
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2012-09-23T11:51:46)
    0000   0xae 0x73 0x0b 0x17 0x0c                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 40 TempBasal 2012-09-23T11:51:51 head[2], body[1] 0x33
    op hex (2)
    0000   0x33 0x2e                                  3.
    decimal
             51   46
    datetime (2012-09-23T11:51:51)
    0000   0xb3 0x73 0x0b 0x17 0x0c                   .s...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 1]

#### RECORD 41 TempBasal[eof] 2012-09-23T11:51:51 head[2], body[0] 0x16
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2012-09-23T11:51:51)
    0000   0xb3 0x73 0x0b 0x17 0x0c                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 42 TempBasal 2012-09-23T12:25:26 head[2], body[1] 0x33
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2012-09-23T12:25:26)
    0000   0x9a 0x59 0x0c 0x17 0x0c                   .Y...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 0]

#### RECORD 43 TempBasal[eof] 2012-09-23T12:25:26 head[2], body[0] 0x16
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2012-09-23T12:25:26)
    0000   0x9a 0x59 0x0c 0x17 0x0c                   .Y...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 44 CalForBG 2012-09-23T13:04:18 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2012-09-23T13:04:18)
    0000   0x92 0x44 0x2d 0x17 0x0c                   .D-..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 45 BolusWizard 2012-09-23T13:29:19 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-23T13:29:19)
    0000   0x93 0x5d 0x0d 0x17 0x0c                   .]...
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0    0    0    8  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0b 0x30 0x69 0x04 0x90 0x9b 0x04    \.0i....
0008   0xf0                                       .
special found
0000   0x59 0x14 0x01 0x08 0x08 0x00              Y.....
should eat up to null, second bytearray(b'')
#### RECORD 46 BolusGiven? 2012-09-23T13:29:19 head[15], body[0] 0x5c
    op hex (15)
    0000   0x5c 0x0b 0x30 0x69 0x04 0x90 0x9b 0x04    \.0i....
    0008   0xf0 0x59 0x14 0x01 0x08 0x08 0x00         .Y.....
    decimal
             92   11   48  105    4  144  155    4
            240   89   20    1    8    8    0
    datetime (2012-09-23T13:29:19)
    0000   0x93 0x5d 0x4d 0x17 0x0c                   .]M..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 47 CalForBG 2012-09-23T17:23:01 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2012-09-23T17:23:01)
    0000   0x81 0x57 0x31 0x17 0x0c                   .W1..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 48 BolusWizard 2012-09-23T17:23:07 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xc7                                  [.
    decimal
             91  199
    datetime (2012-09-23T17:23:07)
    0000   0x87 0x57 0x11 0x17 0x0c                   .W...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    1    0   15  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0b 0x20 0xef 0x04 0x30 0x53 0x14    \. ..0S.
0008   0x90                                       .
special found
0000   0x85 0x14 0x01 0x09 0x09 0x00              ......
should eat up to null, second bytearray(b'')
#### RECORD 49 BolusGiven? 2012-09-23T17:23:07 head[15], body[0] 0x5c
    op hex (15)
    0000   0x5c 0x0b 0x20 0xef 0x04 0x30 0x53 0x14    \. ..0S.
    0008   0x90 0x85 0x14 0x01 0x09 0x09 0x00         .......
    decimal
             92   11   32  239    4   48   83   20
            144  133   20    1    9    9    0
    datetime (2012-09-23T17:23:07)
    0000   0x87 0x57 0x51 0x17 0x0c                   .WQ..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 50 CalForBG 2012-09-23T18:54:10 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-09-23T18:54:10)
    0000   0x8a 0x76 0x32 0x17 0x0c                   .v2..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 51 CalForBG 2012-09-23T19:06:34 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-09-23T19:06:34)
    0000   0xa2 0x46 0x33 0x17 0x0c                   .F3..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 52 BolusWizard 2012-09-23T19:06:41 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x4e                                  [N
    decimal
             91   78
    datetime (2012-09-23T19:06:41)
    0000   0xa9 0x46 0x13 0x17 0x0c                   .F...
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0xfa 0x17 0xf0    .P.-j...
    0008   0x00 0x05 0x00 0x11 0x7d                   ....}
    decimal
             31   80   13   45  106  250   23  240
              0    5    0   17  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0b 0x24 0x70 0x04 0x20 0x56 0x14    \.$p. V.
0008   0x30                                       0
special found
0000   0xba 0x14 0x01 0x11 0x11 0x00              ......
should eat up to null, second bytearray(b'')
#### RECORD 53 BolusGiven? 2012-09-23T19:06:41 head[15], body[0] 0x5c
    op hex (15)
    0000   0x5c 0x0b 0x24 0x70 0x04 0x20 0x56 0x14    \.$p. V.
    0008   0x30 0xba 0x14 0x01 0x11 0x11 0x00         0......
    decimal
             92   11   36  112    4   32   86   20
             48  186   20    1   17   17    0
    datetime (2012-09-23T19:06:41)
    0000   0xa9 0x46 0x53 0x17 0x0c                   .FS..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 54 BolusWizard 2012-09-23T19:25:40 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-23T19:25:40)
    0000   0xa8 0x59 0x13 0x17 0x0c                   .Y...
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             21   80   13   45  106    0   16    0
              0    0    0   16  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0e 0x44 0x15 0x04 0x24 0x83 0x04    \.D..$..
0008   0x20                                        
special found
0000   0x69 0x14 0x30 0xcd 0x14 0x01 0x10 0x10    i.0.....
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 55 BolusGiven? 2012-09-23T19:25:41 head[18], body[0] 0x5c
    op hex (18)
    0000   0x5c 0x0e 0x44 0x15 0x04 0x24 0x83 0x04    \.D..$..
    0008   0x20 0x69 0x14 0x30 0xcd 0x14 0x01 0x10     i.0....
    0010   0x10 0x00                                  ..
    decimal
             92   14   68   21    4   36  131    4
             32  105   20   48  205   20    1   16
             16    0
    datetime (2012-09-23T19:25:41)
    0000   0xa9 0x59 0x53 0x17 0x0c                   .YS..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 56 BolusWizard 2012-09-23T22:26:12 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-23T22:26:12)
    0000   0x8c 0x5a 0x16 0x17 0x0c                   .Z...
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0b 0x40 0xb6 0x04 0x44 0xca 0x04    \.@..D..
0008   0x24                                       $
special found
0000   0x38 0x14 0x01 0x0a 0x0a 0x00              8.....
should eat up to null, second bytearray(b'')
#### RECORD 57 BolusGiven? 2012-09-23T22:26:12 head[15], body[0] 0x5c
    op hex (15)
    0000   0x5c 0x0b 0x40 0xb6 0x04 0x44 0xca 0x04    \.@..D..
    0008   0x24 0x38 0x14 0x01 0x0a 0x0a 0x00         $8.....
    decimal
             92   11   64  182    4   68  202    4
             36   56   20    1   10   10    0
    datetime (2012-09-23T22:26:12)
    0000   0x8c 0x5a 0x56 0x17 0x0c                   .ZV..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 58 ResultTotals 2012-10-23T13:12:23 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x72                   ....r
    decimal
              7    0    0    6  114
    datetime (2012-10-23T13:12:23)
    0000   0x97 0x8c 0x6d 0x97 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xc5 0x4e 0x8e 0x08 0x00 0x00    ...N....
    0008   0x06 0x72 0x03 0x6e 0x35 0x03 0x04 0x2f    .r.n5../
    0010   0x00 0x74 0x03 0x04 0x2f 0x01 0x30 0x27    .t../.0'
    0018   0x01 0xd4 0x3d 0x00 0x00 0x00 0x09 0x05    ..=.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  197   78  142    8    0    0
              6  114    3  110   53    3    4   47
              0  116    3    4   47    1   48   39
              1  212   61    0    0    0    9    5
              4    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 59 PumpSuspend 2012-09-24T12:34:30 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-24T12:34:30)
    0000   0x9e 0x62 0x0c 0x18 0x0c                   .b...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 60 PumpResume 2012-09-24T12:51:34 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-24T12:51:34)
    0000   0xa2 0x73 0x0c 0x18 0x0c                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 61 CalForBG 2012-09-24T13:25:34 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2012-09-24T13:25:34)
    0000   0xa2 0x59 0x2d 0x18 0x0c                   .Y-..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 62 BolusWizard 2012-09-24T13:26:18 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2012-09-24T13:26:18)
    0000   0x92 0x5a 0x0d 0x18 0x0c                   .Z...
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x0a 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x3c 0x7d                   ...<}
    decimal
             65   80   13   45  106   10   50    0
              0    0    0   60  125
    HOUR BITS: [0, 1, 0]

#### RECORD 63 Bolus 2012-09-24T13:26:18 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x3c 0x3c 0x00                        .<<.
    decimal
              1   60   60    0
    datetime (2012-09-24T13:26:18)
    0000   0x92 0x5a 0x4d 0x18 0x0c                   .ZM..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 64 CalForBG 2012-09-24T16:23:41 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-09-24T16:23:41)
    0000   0xa9 0x57 0x30 0x18 0x0c                   .W0..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 65 BolusWizard 2012-09-24T17:04:10 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-24T17:04:10)
    0000   0x8a 0x44 0x11 0x18 0x0c                   .D...
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x05 0xf0 0xdc 0x04 0x01 0x0a 0x0a    \.......
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 66 BolusGiven? 2012-09-24T17:04:10 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0xf0 0xdc 0x04 0x01 0x0a 0x0a    \.......
    0008   0x00                                       .
    decimal
             92    5  240  220    4    1   10   10
              0
    datetime (2012-09-24T17:04:10)
    0000   0x8a 0x44 0x51 0x18 0x0c                   .DQ..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 67 CalForBG 2012-09-24T19:10:00 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x94                                  ..
    decimal
             10  148
    datetime (2012-09-24T19:10:00)
    0000   0x80 0x4a 0x33 0x18 0x0c                   .J3..
    body (0)
    HOUR BITS: [0, 1, 0]

`end logs/ReadHistoryData-page-33.data: 68 records`
