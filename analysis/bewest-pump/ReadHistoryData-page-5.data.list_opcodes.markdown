WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-5.data
#### RECORD 0 Record 2013-01-03T02:05:39 head[46], body[0] 0x6d
    op hex (46)
    0000   0x6d 0x02 0x8d 0x05 0x00 0x94 0x49 0xea    m.....I.
    0008   0x06 0x00 0x00 0x05 0xa4 0x03 0x84 0x3e    .......>
    0010   0x02 0x20 0x26 0x00 0x89 0x02 0x20 0x26    . &... &
    0018   0x01 0x80 0x47 0x00 0xa0 0x1d 0x00 0x00    ..G.....
    0020   0x00 0x05 0x02 0x02 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x5c              .....\
    decimal
            109    2  141    5    0  148   73  234
              6    0    0    5  164    3  132   62
              2   32   38    0  137    2   32   38
              1  128   71    0  160   29    0    0
              0    5    2    2    1    0   12    0
            232    0    0    0   10   92
    datetime (2013-01-03T02:05:39)
    0000   0x27 0x45 0x22 0x03 0x0d                   'E"..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 1 CalForBG 2013-01-03T09:59:29 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2013-01-03T09:59:29)
    0000   0x1d 0x7b 0x29 0x03 0x0d                   .{)..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 2 BolusWizard 2013-01-03T09:59:42 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x4e                                  [N
    decimal
             91   78
    datetime (2013-01-03T09:59:42)
    0000   0x2a 0x7b 0x09 0x03 0x0d                   *{...
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0xfa 0x32 0xf0    BP.-j.2.
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
             66   80   13   45  106  250   50  240
              0    0    0   44  125
    HOUR BITS: [0, 1, 1]

#### RECORD 3 Bolus 2013-01-03T09:59:42 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-01-03T09:59:42)
    0000   0x2a 0x7b 0x49 0x03 0x0d                   *{I..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 4 PumpSuspend 2013-01-03T12:38:16 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-03T12:38:16)
    0000   0x10 0x66 0x0c 0x03 0x0d                   .f...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 5 PumpResume 2013-01-03T12:59:50 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-03T12:59:50)
    0000   0x32 0x7b 0x0c 0x03 0x0d                   2{...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 6 CalForBG 2013-01-03T13:11:58 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2013-01-03T13:11:58)
    0000   0x3a 0x4b 0x2d 0x03 0x0d                   :K-..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 7 CalForBG 2013-01-03T13:58:15 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-01-03T13:58:15)
    0000   0x0f 0x7a 0x2d 0x03 0x0d                   .z-..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 8 BolusWizard 2013-01-03T13:59:34 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-01-03T13:59:34)
    0000   0x22 0x7b 0x0d 0x03 0x0d                   "{...
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0x00 0x2b 0x00    8P.-j.+.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             56   80   13   45  106    0   43    0
              0    0    0   43  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x05 0xb0 0xf5 0x04 0x01 0x2b 0x2b    \.....++
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 9 BolusGiven? 2013-01-03T13:59:34 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0xb0 0xf5 0x04 0x01 0x2b 0x2b    \.....++
    0008   0x00                                       .
    decimal
             92    5  176  245    4    1   43   43
              0
    datetime (2013-01-03T13:59:34)
    0000   0x22 0x7b 0x4d 0x03 0x0d                   "{M..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 10 BolusWizard 2013-01-03T14:30:30 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-01-03T14:30:30)
    0000   0x1e 0x5e 0x0e 0x03 0x0d                   .^...
    body (13)
    hex
    0000   0x27 0x50 0x0d 0x2d 0x6a 0x00 0x1e 0x00    'P.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             39   80   13   45  106    0   30    0
              0    0    0   30  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x08 0xac 0x24 0x04 0xb0 0x14 0x14    \..$....
0008   0x01                                       .
special found
0000   0x1e 0x1e 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 11 BolusGiven? 2013-01-03T14:30:30 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0xac 0x24 0x04 0xb0 0x14 0x14    \..$....
    0008   0x01 0x1e 0x1e 0x00                        ....
    decimal
             92    8  172   36    4  176   20   20
              1   30   30    0
    datetime (2013-01-03T14:30:30)
    0000   0x1e 0x5e 0x4e 0x03 0x0d                   .^N..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 12 CalForBG 2013-01-03T16:02:01 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x86                                  ..
    decimal
             10  134
    datetime (2013-01-03T16:02:01)
    0000   0x01 0x42 0x30 0x03 0x0d                   .B0..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 13 CalForBG 2013-01-03T17:30:25 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2013-01-03T17:30:25)
    0000   0x19 0x5e 0x31 0x03 0x0d                   .^1..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 14 BolusWizard 2013-01-03T17:30:43 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xd3                                  [.
    decimal
             91  211
    datetime (2013-01-03T17:30:43)
    0000   0x2b 0x5e 0x11 0x03 0x0d                   +^...
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x13 0x14 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x1e 0x7d                   ....}
    decimal
             27   80   13   45  106   19   20    0
              0    9    0   30  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x0b 0x78 0xba 0x04 0xac 0xd8 0x04    \.x.....
0008   0xb0                                       .
special found
0000   0xc8 0x14 0x01 0x1e 0x1e 0x00              ......
should eat up to null, second bytearray(b'')
#### RECORD 15 BolusGiven? 2013-01-03T17:30:43 head[15], body[0] 0x5c
    op hex (15)
    0000   0x5c 0x0b 0x78 0xba 0x04 0xac 0xd8 0x04    \.x.....
    0008   0xb0 0xc8 0x14 0x01 0x1e 0x1e 0x00         .......
    decimal
             92   11  120  186    4  172  216    4
            176  200   20    1   30   30    0
    datetime (2013-01-03T17:30:43)
    0000   0x2b 0x5e 0x51 0x03 0x0d                   +^Q..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 16 CalForBG 2013-01-03T21:27:12 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-01-03T21:27:12)
    0000   0x0c 0x5b 0x35 0x03 0x0d                   .[5..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 17 ChangeTimeDisplay 2013-01-03T22:24:46 head[2], body[0] 0x64
    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-01-03T22:24:46)
    0000   0x2e 0x58 0x16 0x03 0x0d                   .X...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 18 ChangeTime 2013-01-03T22:24:53 head[2], body[0] 0x17
    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-01-03T22:24:53)
    0000   0x35 0x58 0x16 0x03 0x0d                   5X...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 19 NewTimeSet 2013-01-03T19:24:00 head[2], body[0] 0x18
    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-01-03T19:24:00)
    0000   0x00 0x58 0x13 0x03 0x0d                   .X...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 20 CalForBG 2013-01-03T21:33:31 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-01-03T21:33:31)
    0000   0x1f 0x61 0x35 0x03 0x0d                   .a5..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 21 CalForBG 2013-01-03T21:34:48 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-01-03T21:34:48)
    0000   0x30 0x62 0x35 0x03 0x0d                   0b5..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 22 CalForBG 2013-01-03T21:35:50 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-01-03T21:35:50)
    0000   0x32 0x63 0x35 0x03 0x0d                   2c5..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 23 BolusWizard 2013-01-03T21:36:09 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2013-01-03T21:36:09)
    0000   0x09 0x64 0x15 0x03 0x0d                   .d...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0xf8 0x2e 0xf0    <P.-j...
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
             60   80   13   45  106  248   46  240
              0    0    0   38  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x78 0xb0 0x14 0x01 0x26 0x26    \.x...&&
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 24 BolusGiven? 2013-01-03T21:36:09 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x78 0xb0 0x14 0x01 0x26 0x26    \.x...&&
    0008   0x00                                       .
    decimal
             92    5  120  176   20    1   38   38
              0
    datetime (2013-01-03T21:36:09)
    0000   0x09 0x64 0x55 0x03 0x0d                   .dU..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 25 ResultTotals 2013-02-03T13:13:03 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xcc                   .....
    decimal
              7    0    0    6  204
    datetime (2013-02-03T13:13:03)
    0000   0x03 0x8d 0x6d 0x03 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x61 0x42 0xd3 0x0a 0x00 0x00    ..aB....
    0008   0x06 0xcc 0x03 0xe8 0x39 0x02 0xe4 0x2b    ....9..+
    0010   0x00 0xf8 0x02 0xe4 0x2b 0x02 0xbc 0x5f    ....+.._
    0018   0x00 0x28 0x05 0x00 0x00 0x00 0x05 0x04    .(......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   97   66  211   10    0    0
              6  204    3  232   57    2  228   43
              0  248    2  228   43    2  188   95
              0   40    5    0    0    0    5    4
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]

#### RECORD 26 CalForBG 2013-01-04T03:40:08 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-01-04T03:40:08)
    0000   0x08 0x68 0x23 0x04 0x0d                   .h#..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 27 LowReservoir 2013-01-04T13:51:49 head[2], body[0] 0x34
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-01-04T13:51:49)
    0000   0x31 0x73 0x0d 0x04 0x0d                   1s...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 28 CalForBG 2013-01-04T15:44:17 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-01-04T15:44:17)
    0000   0x11 0x6c 0x2f 0x04 0x0d                   .l/..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 29 BolusWizard 2013-01-04T15:44:52 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-01-04T15:44:52)
    0000   0x34 0x6c 0x0f 0x04 0x0d                   4l...
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0xff 0x12 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             24   80   13   45  106  255   18  240
              0    0    0   17  125
    HOUR BITS: [0, 1, 1]

#### RECORD 30 Bolus 2013-01-04T15:44:52 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-01-04T15:44:52)
    0000   0x34 0x6c 0x4f 0x04 0x0d                   4lO..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 31 CalForBG 2013-01-04T16:15:44 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-01-04T16:15:44)
    0000   0x2c 0x4f 0x30 0x04 0x0d                   ,O0..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 32 BolusWizard 2013-01-04T16:16:10 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-01-04T16:16:10)
    0000   0x0a 0x50 0x10 0x04 0x0d                   .P...
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0xff 0x32 0xf0    BP.-j.2.
    0008   0x00 0x10 0x00 0x31 0x7d                   ...1}
    decimal
             66   80   13   45  106  255   50  240
              0   16    0   49  125
    HOUR BITS: [0, 1, 0]

should eat up to null first: 0x5c
0000   0x5c 0x05 0x44 0x20 0x04 0x01 0x31 0x31    \.D ..11
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 33 BolusGiven? 2013-01-04T16:16:10 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x44 0x20 0x04 0x01 0x31 0x31    \.D ..11
    0008   0x00                                       .
    decimal
             92    5   68   32    4    1   49   49
              0
    datetime (2013-01-04T16:16:10)
    0000   0x0a 0x50 0x50 0x04 0x0d                   .PP..
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 34 LowReservoir 2013-01-04T17:25:15 head[2], body[0] 0x34
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-01-04T17:25:15)
    0000   0x0f 0x59 0x11 0x04 0x0d                   .Y...
    body (0)
    HOUR BITS: [0, 1, 0]

#### RECORD 35 Rewind 2013-01-04T19:47:46 head[2], body[0] 0x21
    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-01-04T19:47:46)
    0000   0x2e 0x6f 0x13 0x04 0x0d                   .o...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 36 Prime 2013-01-04T19:49:25 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x28                   ....(
    decimal
              3    0    0    0   40
    datetime (2013-01-04T19:49:25)
    0000   0x19 0x71 0x33 0x04 0x0d                   .q3..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 37 Prime 2013-01-04T19:49:50 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-01-04T19:49:50)
    0000   0x32 0x71 0x13 0x04 0x0d                   2q...
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 38 CalForBG 2013-01-04T21:36:57 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-01-04T21:36:57)
    0000   0x39 0x64 0x35 0x04 0x0d                   9d5..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 39 BolusWizard 2013-01-04T21:37:22 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-01-04T21:37:22)
    0000   0x16 0x65 0x15 0x04 0x0d                   .e...
    body (13)
    hex
    0000   0x4a 0x50 0x0d 0x2d 0x6a 0x00 0x38 0x00    JP.-j.8.
    0008   0x00 0x00 0x00 0x38 0x7d                   ...8}
    decimal
             74   80   13   45  106    0   56    0
              0    0    0   56  125
    HOUR BITS: [0, 1, 1]

should eat up to null first: 0x5c
0000   0x5c 0x08 0xc4 0x43 0x14 0x44 0x61 0x14    \..C.Da.
0008   0x01                                       .
special found
0000   0x38 0x38 0x03 0x16 0x65 0x75 0x04 0x0d    88..eu..
0008   0x07 0x00                                  ..
#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x5c 0x08 0xc4 0x43 0x14 0x44 0x61 0x14    \..C.Da.
    0008   0x01 0x38 0x38 0x03 0x16 0x65 0x75 0x04    .88..eu.
    0010   0x0d 0x07 0x00 0x00 0x05 0x6c 0x04 0x8d    .....l..
    0018   0x6d 0x04 0x8d 0x05 0x00 0x6e 0x66 0x75    m....nfu
    0020   0x04 0x00 0x00 0x05 0x6c 0x03 0x84 0x41    ....l..A
    0028   0x01 0xe8 0x23 0x00 0xa4 0x01 0xe8 0x23    ..#....#
##### DEBUG DECIMAL
             92    8  196   67   20   68   97   20
              1   56   56    3   22  101  117    4
             13    7    0    0    5  108    4  141
            109    4  141    5    0  110  102  117
              4    0    0    5  108    3  132   65
              1  232   35    0  164    1  232   35
XXX:???:XXX 2004-04-03T04:08:28
`end logs/ReadHistoryData-page-5.data: 40 records`
