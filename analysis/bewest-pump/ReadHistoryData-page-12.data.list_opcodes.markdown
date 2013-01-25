WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-12.data
should eat up to null 0x5c
0000   0x5c 0x0b 0x14 0x08 0x04 0x06 0xd4 0x14    \.......
0008   0x92 0xde 0x14 0x01                        ....
special found
0000   0x3a 0x3a 0x00                             ::.
should eat up to null
#### RECORD 0 BolusGiven? 2012-12-10T03:52:35 head[15], body[0] 0x5c
    op hex (15)
    0000   0x5c 0x0b 0x14 0x08 0x04 0x06 0xd4 0x14    \.......
    0008   0x92 0xde 0x14 0x01 0x3a 0x3a 0x00         ....::.
    decimal
             92   11   20    8    4    6  212   20
            146  222   20    1   58   58    0
    datetime (2012-12-10T03:52:35)
    0000   0xe3 0x34 0x43 0x0a 0x0c                   .4C..
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 1 PumpSuspend 2012-12-10T13:08:44 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-10T13:08:44)
    0000   0xec 0x08 0x0d 0x0a 0x0c                   .....
    body (0)
    

#### RECORD 2 PumpResume 2012-12-10T13:35:13 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-10T13:35:13)
    0000   0xcd 0x23 0x0d 0x0a 0x0c                   .#...
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 3 CalForBG 2012-12-10T13:40:13 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2012-12-10T13:40:13)
    0000   0xcd 0x28 0x2d 0x0a 0x0c                   .(-..
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 4 BolusWizard 2012-12-10T13:40:21 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0x9d                                  [.
    decimal
             91  157
    datetime (2012-12-10T13:40:21)
    0000   0xd5 0x28 0x0d 0x0a 0x0c                   .(...
    body (22)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x07 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d 0x01 0x04 0x04    ....}...
    0010   0x00 0xd5 0x28 0x4d 0x0a 0x0c              ..(M..
    decimal
              0   80   13   45  106    7    0    0
              0    0    0    7  125    1    4    4
              0  213   40   77   10   12
    HOUR BITS: [0, 0, 1]

#### RECORD 5 CalForBG 2012-12-10T14:01:42 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2012-12-10T14:01:42)
    0000   0xea 0x01 0x2e 0x0a 0x0c                   .....
    body (0)
    

should eat up to null
#### RECORD 6 BolusWizard 2012-12-10T14:02:03 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2012-12-10T14:02:03)
    0000   0xc3 0x02 0x0e 0x0a 0x0c                   .....
    body (22)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x17 0x7d 0x5c 0x05 0x10    ....}\..
    0010   0x1c 0x04 0x01 0x17 0x17 0x00              ......
    decimal
             30   80   13   45  106    0   23    0
              0    4    0   23  125   92    5   16
             28    4    1   23   23    0
    

should eat up to null
found 3 extra
#### RECORD 7 BolusWizard 2012-12-10T15:08:25 head[2], body[25] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-10T15:08:25)
    0000   0xd9 0x08 0x0f 0x0a 0x0c                   .....
    body (25)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x00 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x22 0x7d 0x5c 0x08 0x5c    ..."}\.\
    0010   0x4a 0x04 0x10 0x5e 0x04 0x01 0x22 0x22    J..^..""
    0018   0x00                                       .
    decimal
             45   80   13   45  106    0   34    0
              0    0    0   34  125   92    8   92
             74    4   16   94    4    1   34   34
              0
    

#### RECORD 8 CalForBG 2012-12-10T21:04:52 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2012-12-10T21:04:52)
    0000   0xf4 0x04 0x35 0x0a 0x8c                   ..5..
    body (0)
    YEAR BITS: [1, 0, 0, 0]

should eat up to null
found 6 extra
#### RECORD 9 BolusWizard 2012-12-10T21:04:54 head[2], body[28] 0x5b
    op hex (2)
    0000   0x5b 0x45                                  [E
    decimal
             91   69
    datetime (2012-12-10T21:04:54)
    0000   0xf6 0x04 0x15 0x0a 0x0c                   .....
    body (28)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2c 0x00 0x00    .Q.-j,..
    0008   0x00 0x00 0x00 0x2c 0x7d 0x5c 0x0b 0x88    ...,}\..
    0010   0x68 0x14 0x5c 0xae 0x14 0x10 0xc2 0x14    h.\.....
    0018   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              0   81   13   45  106   44    0    0
              0    0    0   44  125   92   11  136
            104   20   92  174   20   16  194   20
              1   44   44    0
    

#### RECORD 10 ResultTotals 2012-12-10T13:12:10 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x12                   .....
    decimal
              7    0    0    6   18
    datetime (2012-12-10T13:12:10)
    0000   0xca 0x0c 0x6d 0xca 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x11 0x1d 0x7b 0x9b 0x05 0x00 0x00    ...{....
    0008   0x06 0x12 0x03 0x72 0x39 0x02 0xa0 0x2b    ...r9..+
    0010   0x00 0x4b 0x02 0xa0 0x2b 0x00 0xe4 0x22    .K..+.."
    0018   0x01 0xbc 0x42 0x00 0x00 0x00 0x06 0x02    ..B.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   17   29  123  155    5    0    0
              6   18    3  114   57    2  160   43
              0   75    2  160   43    0  228   34
              1  188   66    0    0    0    6    2
              4    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]

#### RECORD 11 PumpSuspend 2012-12-11T08:49:52 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-11T08:49:52)
    0000   0xf4 0x31 0x08 0x0b 0x0c                   .1...
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 12 PumpResume 2012-12-11T13:26:59 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-11T13:26:59)
    0000   0xfb 0x1a 0x0d 0x0b 0x0c                   .....
    body (0)
    

#### RECORD 13 CalForBG 2012-12-11T13:27:12 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xed                                  ..
    decimal
             10  237
    datetime (2012-12-11T13:27:12)
    0000   0xcc 0x1b 0x2d 0x0b 0x0c                   ..-..
    body (0)
    

#### RECORD 14 BolusWizard 2012-12-11T13:27:20 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0xed                                  [.
    decimal
             91  237
    datetime (2012-12-11T13:27:20)
    0000   0xd4 0x1b 0x0d 0x0b 0x0c                   .....
    body (22)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x18 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d 0x01 0x1a 0x1a    ....}...
    0010   0x00 0xd4 0x1b 0x4d 0x0b 0x0c              ...M..
    decimal
              0   80   13   45  106   24    0    0
              0    0    0   24  125    1   26   26
              0  212   27   77   11   12
    

#### RECORD 15 PumpSuspend 2012-12-11T13:36:55 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-11T13:36:55)
    0000   0xf7 0x24 0x0d 0x0b 0x0c                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 16 PumpResume 2012-12-11T13:50:12 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-11T13:50:12)
    0000   0xcc 0x32 0x0d 0x0b 0x0c                   .2...
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 17 CalForBG 2012-12-11T14:22:21 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xe1                                  ..
    decimal
             10  225
    datetime (2012-12-11T14:22:21)
    0000   0xd5 0x16 0x2e 0x0b 0x0c                   .....
    body (0)
    

should eat up to null
#### RECORD 18 BolusWizard 2012-12-11T14:22:28 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0xe1                                  [.
    decimal
             91  225
    datetime (2012-12-11T14:22:28)
    0000   0xdc 0x16 0x0e 0x0b 0x0c                   .....
    body (22)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x00 0x7d 0x5c 0x05 0x68    ....}\.h
    0010   0x3a 0x04 0x01 0x02 0x02 0x00              :.....
    decimal
              0   80   13   45  106   22    0    0
              0   22    0    0  125   92    5  104
             58    4    1    2    2    0
    

should eat up to null
found 10 extra
#### RECORD 19 BolusWizard 2012-12-11T14:28:20 head[2], body[32] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-11T14:28:20)
    0000   0xd4 0x1c 0x0e 0x0b 0x0c                   .....
    body (32)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x00 0x1c 0x00    %P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d 0x5c 0x08 0x08    ....}\..
    0010   0x0e 0x04 0x68 0x40 0x04 0x34 0xc8 0xcd    ..h@.4..
    0018   0x1d 0x0e 0x0b 0x0c 0x01 0x1c 0x1c 0x00    ........
    decimal
             37   80   13   45  106    0   28    0
              0    0    0   28  125   92    8    8
             14    4  104   64    4   52  200  205
             29   14   11   12    1   28   28    0
    

#### RECORD 20 CalForBG 2012-12-11T16:01:46 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2012-12-11T16:01:46)
    0000   0xee 0x01 0x30 0x0b 0x0c                   ..0..
    body (0)
    

#### RECORD 21 TempBasal 2012-12-11T16:02:23 head[2], body[1] 0x33
    op hex (2)
    0000   0x33 0x28                                  3(
    decimal
             51   40
    datetime (2012-12-11T16:02:23)
    0000   0xd7 0x02 0x10 0x0b 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    

#### RECORD 22 TempBasal[eof] 2012-12-11T16:02:23 head[2], body[0] 0x16
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2012-12-11T16:02:23)
    0000   0xd7 0x02 0x10 0x0b 0x0c                   .....
    body (0)
    

#### RECORD 23 CalForBG 2012-12-11T16:02:51 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xd9                                  ..
    decimal
             10  217
    datetime (2012-12-11T16:02:51)
    0000   0xf3 0x02 0x30 0x0b 0x0c                   ..0..
    body (0)
    

#### RECORD 24 CalForBG 2012-12-11T16:06:22 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2012-12-11T16:06:22)
    0000   0xd6 0x06 0x30 0x0b 0x0c                   ..0..
    body (0)
    

should eat up to null
found 6 extra
#### RECORD 25 BolusWizard 2012-12-11T16:06:32 head[2], body[28] 0x5b
    op hex (2)
    0000   0x5b 0xdb                                  [.
    decimal
             91  219
    datetime (2012-12-11T16:06:32)
    0000   0xe0 0x06 0x10 0x0b 0x0c                   .....
    body (28)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x14 0x13 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x13 0x7d 0x5c 0x0b 0x70    ....}\.p
    0010   0x66 0x04 0x08 0x70 0x04 0x68 0xa2 0x04    f..p.h..
    0018   0x01 0x13 0x13 0x00                        ....
    decimal
             25   80   13   45  106   20   19    0
              0   24    0   19  125   92   11  112
            102    4    8  112    4  104  162    4
              1   19   19    0
    

#### RECORD 26 CalForBG 2012-12-11T17:05:19 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2012-12-11T17:05:19)
    0000   0xd3 0x05 0x31 0x0b 0x0c                   ..1..
    body (0)
    

#### RECORD 27 CalForBG 2012-12-11T17:07:21 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2012-12-11T17:07:21)
    0000   0xd5 0x07 0x31 0x0b 0x0c                   ..1..
    body (0)
    

should eat up to null
found 9 extra
#### RECORD 28 BolusWizard 2012-12-11T17:07:40 head[2], body[31] 0x5b
    op hex (2)
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2012-12-11T17:07:40)
    0000   0xe8 0x07 0x11 0x0b 0x0c                   .....
    body (31)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x06 0x0c 0x00    .P.-j...
    0008   0x00 0x19 0x00 0x0c 0x7d 0x5c 0x0e 0x4c    ....}\.L
    0010   0x3f 0x04 0x70 0xa3 0x04 0x08 0xad 0x04    ?.p.....
    0018   0x68 0xdf 0x04 0x01 0x0c 0x0c 0x00         h......
    decimal
             16   80   13   45  106    6   12    0
              0   25    0   12  125   92   14   76
             63    4  112  163    4    8  173    4
            104  223    4    1   12   12    0
    

#### RECORD 29 CalForBG 2012-12-11T19:18:24 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-12-11T19:18:24)
    0000   0xd8 0x12 0x33 0x0b 0x0c                   ..3..
    body (0)
    

should eat up to null
found 19 extra
#### RECORD 30 BolusWizard 2012-12-11T19:18:34 head[2], body[41] 0x5b
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2012-12-11T19:18:34)
    0000   0xe2 0x12 0x13 0x0b 0x0c                   .....
    body (41)
    hex
    0000   0x44 0x50 0x0d 0x2d 0x6a 0x00 0x34 0x00    DP.-j.4.
    0008   0x00 0x07 0x00 0x34 0x7d 0x5c 0x11 0x30    ...4}\.0
    0010   0x86 0x04 0x4c 0xc2 0x04 0x70 0x26 0x14    ..L..p&.
    0018   0x08 0x30 0x14 0x68 0x62 0x14 0x34 0x64    .0.hb.4d
    0020   0xc4 0x13 0x13 0x0b 0x0c 0x01 0x34 0x34    ......44
    0028   0x00                                       .
    decimal
             68   80   13   45  106    0   52    0
              0    7    0   52  125   92   17   48
            134    4   76  194    4  112   38   20
              8   48   20  104   98   20   52  100
            196   19   19   11   12    1   52   52
              0
    

should eat up to null
found 15 extra
#### RECORD 31 BolusWizard 2012-12-11T19:56:16 head[2], body[37] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-11T19:56:16)
    0000   0xd0 0x38 0x13 0x0b 0x0c                   .8...
    body (37)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d 0x5c 0x14 0xd0    ....}\..
    0010   0x2a 0x04 0x30 0xac 0x04 0x4c 0xe8 0x04    *.0..L..
    0018   0x70 0x4c 0x14 0x08 0x56 0x14 0x68 0x88    pL..V.h.
    0020   0x14 0x01 0x10 0x10 0x00                   .....
    decimal
             22   80   13   45  106    0   16    0
              0    0    0   16  125   92   20  208
             42    4   48  172    4   76  232    4
            112   76   20    8   86   20  104  136
             20    1   16   16    0
    HOUR BITS: [0, 0, 1]

#### RECORD 32 CalForBG 2012-12-11T20:10:13 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x8a                                  ..
    decimal
             10  138
    datetime (2012-12-11T20:10:13)
    0000   0xcd 0x0a 0x34 0x0b 0x0c                   ..4..
    body (0)
    

#### RECORD 33 ResultTotals 2012-12-11T13:12:11 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x20                   .... 
    decimal
              7    0    0    5   32
    datetime (2012-12-11T13:12:11)
    0000   0xcb 0x0c 0x6d 0xcb 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xba 0x6c 0xed 0x09 0x00 0x00    ...l....
    0008   0x05 0x20 0x02 0xb4 0x35 0x02 0x6c 0x2f    . ..5.l/
    0010   0x00 0xa8 0x02 0x6c 0x2f 0x01 0xfc 0x52    ...l/..R
    0018   0x00 0x70 0x12 0x00 0x00 0x00 0x07 0x05    .p......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  186  108  237    9    0    0
              5   32    2  180   53    2  108   47
              0  168    2  108   47    1  252   82
              0  112   18    0    0    0    7    5
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]

#### RECORD 34 PumpSuspend 2012-12-12T15:42:30 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-12T15:42:30)
    0000   0xde 0x2a 0x0f 0x0c 0x0c                   .*...
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 35 PumpResume 2012-12-12T16:06:03 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-12T16:06:03)
    0000   0xc3 0x06 0x10 0x0c 0x0c                   .....
    body (0)
    

#### RECORD 36 Rewind 2012-12-12T16:12:34 head[2], body[0] 0x21
    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-12T16:12:34)
    0000   0xe2 0x0c 0x10 0x0c 0x0c                   .....
    body (0)
    

#### RECORD 37 Prime 2012-12-12T16:14:00 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2a                   ....*
    decimal
              3    0    0    0   42
    datetime (2012-12-12T16:14:00)
    0000   0xc0 0x0e 0x30 0x0c 0x0c                   ..0..
    body (0)
    

#### RECORD 38 Prime 2012-12-12T16:14:23 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-12T16:14:23)
    0000   0xd7 0x0e 0x10 0x0c 0x0c                   .....
    body (0)
    

#### RECORD 39 CalForBG 2012-12-12T17:07:04 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-12-12T17:07:04)
    0000   0xc4 0x07 0x31 0x0c 0x0c                   ..1..
    body (0)
    

#### RECORD 40 BolusWizard 2012-12-12T17:07:46 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2012-12-12T17:07:46)
    0000   0xee 0x07 0x11 0x0c 0x0c                   .....
    body (22)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0xf8 0x1f 0xf0    )P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d 0x01 0x17 0x17    ....}...
    0010   0x00 0xef 0x07 0x51 0x0c 0x0c              ...Q..
    decimal
             41   80   13   45  106  248   31  240
              0    0    0   23  125    1   23   23
              0  239    7   81   12   12
    

#### RECORD 41 CalForBG 2012-12-12T17:32:33 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-12-12T17:32:33)
    0000   0xe1 0x20 0x31 0x0c 0x0c                   . 1..
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 42 CalForBG 2012-12-12T19:51:33 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2012-12-12T19:51:33)
    0000   0xe1 0x33 0x33 0x0c 0x0c                   .33..
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 43 CalForBG 2012-12-12T20:55:45 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2012-12-12T20:55:45)
    0000   0xed 0x37 0x34 0x0c 0x0c                   .74..
    body (0)
    HOUR BITS: [0, 0, 1]

should eat up to null
#### RECORD 44 BolusWizard 2012-12-12T20:55:56 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2012-12-12T20:55:56)
    0000   0xf8 0x37 0x14 0x0c 0x0c                   .7...
    body (22)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x0a 0x22 0x00    -P.-j.".
    0008   0x00 0x02 0x00 0x2a 0x7d 0x5c 0x05 0x5c    ...*}\.\
    0010   0xe7 0x04 0x01 0x2a 0x2a 0x00              ...**.
    decimal
             45   80   13   45  106   10   34    0
              0    2    0   42  125   92    5   92
            231    4    1   42   42    0
    HOUR BITS: [0, 0, 1]

#### RECORD 45 ResultTotals 2012-12-12T13:12:12 head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x78                   ....x
    decimal
              7    0    0    4  120
    datetime (2012-12-12T13:12:12)
    0000   0xcc 0x0c 0x6d 0xcc 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x70 0x46 0xab 0x04 0x00 0x00    ..pF....
    0008   0x04 0x78 0x03 0x74 0x4d 0x01 0x04 0x17    .x.tM...
    0010   0x00 0x56 0x01 0x04 0x17 0x00 0xe4 0x58    .V.....X
    0018   0x00 0x20 0x0c 0x00 0x00 0x00 0x02 0x01    . ......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  112   70  171    4    0    0
              4  120    3  116   77    1    4   23
              0   86    1    4   23    0  228   88
              0   32   12    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]

#### RECORD 46 PumpSuspend 2012-12-13T11:03:12 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-13T11:03:12)
    0000   0xcc 0x03 0x0b 0x0d 0x0c                   .....
    body (0)
    

#### RECORD 47 PumpResume 2012-12-13T11:23:22 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-13T11:23:22)
    0000   0xd6 0x17 0x0b 0x0d 0x0c                   .....
    body (0)
    

#### RECORD 48 CalForBG 2012-12-13T12:57:59 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2012-12-13T12:57:59)
    0000   0xfb 0x39 0x2c 0x0d 0x0c                   .9,..
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 49 BolusWizard 2012-12-13T12:58:07 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2012-12-13T12:58:07)
    0000   0xc7 0x3a 0x0c 0x0d 0x0c                   .:...
    body (22)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0xfb 0x1a 0xf0    #P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d 0x01 0x15 0x15    ....}...
    0010   0x00 0xc7 0x3a 0x4c 0x0d 0x0c              ..:L..
    decimal
             35   80   13   45  106  251   26  240
              0    0    0   21  125    1   21   21
              0  199   58   76   13   12
    HOUR BITS: [0, 0, 1]

should eat up to null
#### RECORD 50 BolusWizard 2012-12-13T13:32:52 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-13T13:32:52)
    0000   0xf4 0x20 0x0d 0x0d 0x0c                   . ...
    body (22)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x00 0x26 0x00    2P.-j.&.
    0008   0x00 0x00 0x00 0x26 0x7d 0x5c 0x05 0x54    ...&}\.T
    0010   0x26 0x04 0x01 0x26 0x26 0x00              &..&&.
    decimal
             50   80   13   45  106    0   38    0
              0    0    0   38  125   92    5   84
             38    4    1   38   38    0
    HOUR BITS: [0, 0, 1]

should eat up to null
found 6 extra
#### RECORD 51 BolusWizard 2012-12-13T14:14:34 head[2], body[28] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-13T14:14:34)
    0000   0xe2 0x0e 0x0e 0x0d 0x0c                   .....
    body (28)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d 0x5c 0x0b 0x54    ....}\.T
    0010   0x28 0x04 0x44 0x32 0x04 0x54 0x50 0x04    (.D2.TP.
    0018   0x01 0x14 0x14 0x00                        ....
    decimal
             26   80   13   45  106    0   20    0
              0    0    0   20  125   92   11   84
             40    4   68   50    4   84   80    4
              1   20   20    0
    

#### RECORD 52 CalForBG 2012-12-13T18:36:00 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2012-12-13T18:36:00)
    0000   0xc0 0x24 0x32 0x0d 0x0c                   .$2..
    body (0)
    HOUR BITS: [0, 0, 1]

found 6 nulls
`end logs/ReadHistoryData-page-12.data: 53 records`
