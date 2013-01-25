WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-9.data
#### RECORD 0 Rewind 2012-12-21T14:41:41 head[2], body[0] 0x21
    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-21T14:41:41)
    0000   0xe9 0x29 0x0e 0x15 0x0c                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 1 Prime 2012-12-21T14:43:52 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2c                   ....,
    decimal
              3    0    0    0   44
    datetime (2012-12-21T14:43:52)
    0000   0xf4 0x2b 0x2e 0x15 0x0c                   .+...
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 2 Prime 2012-12-21T14:44:18 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-21T14:44:18)
    0000   0xd2 0x2c 0x0e 0x15 0x0c                   .,...
    body (0)
    HOUR BITS: [0, 0, 1]

#### RECORD 3 CalForBG 2012-12-21T18:18:19 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-21T18:18:19)
    0000   0xd3 0x12 0x32 0x15 0x0c                   ..2..
    body (0)
    

#### RECORD 4 BolusWizard 2012-12-21T18:18:23 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2012-12-21T18:18:23)
    0000   0xd7 0x12 0x12 0x15 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    2    0   11  125
    

should eat up to null first: 0x5c
0000   0x5c 0x05 0x5c 0xea 0x04 0x01 0x0b 0x0b    \.\.....
0008   0x00                                       .
should eat up to null, second bytearray(b'')
#### RECORD 5 BolusGiven? 2012-12-21T18:18:23 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x05 0x5c 0xea 0x04 0x01 0x0b 0x0b    \.\.....
    0008   0x00                                       .
    decimal
             92    5   92  234    4    1   11   11
              0
    datetime (2012-12-21T18:18:23)
    0000   0xd7 0x12 0x52 0x15 0x0c                   ..R..
    body (0)
    

#### RECORD 6 CalForBG 2012-12-21T18:20:31 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-21T18:20:31)
    0000   0xdf 0x14 0x32 0x15 0x0c                   ..2..
    body (0)
    

#### RECORD 7 CalForBG 2012-12-21T18:20:52 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-21T18:20:52)
    0000   0xf4 0x14 0x32 0x15 0x0c                   ..2..
    body (0)
    

#### RECORD 8 BolusWizard 2012-12-21T18:21:04 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2012-12-21T18:21:04)
    0000   0xc4 0x15 0x12 0x15 0x0c                   .....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x0d 0x17 0x00    .P.-j...
    0008   0x00 0x0d 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106   13   23    0
              0   13    0   23  125
    

should eat up to null first: 0x5c
0000   0x5c 0x08 0x2c 0x07 0x04 0x5c 0xed 0x04    \.,..\..
0008   0x01                                       .
special found
0000   0x17 0x17 0x00                             ...
should eat up to null, second bytearray(b'')
#### RECORD 9 BolusGiven? 2012-12-21T18:21:04 head[12], body[0] 0x5c
    op hex (12)
    0000   0x5c 0x08 0x2c 0x07 0x04 0x5c 0xed 0x04    \.,..\..
    0008   0x01 0x17 0x17 0x00                        ....
    decimal
             92    8   44    7    4   92  237    4
              1   23   23    0
    datetime (2012-12-21T18:21:04)
    0000   0xc4 0x15 0x52 0x15 0x0c                   ..R..
    body (0)
    

#### RECORD 10 CalForBG 2012-12-21T21:23:40 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2012-12-21T21:23:40)
    0000   0xe8 0x17 0x35 0x15 0x0c                   ..5..
    body (0)
    

#### RECORD 11 BolusWizard 2012-12-21T21:24:10 head[2], body[13] 0x5b
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2012-12-21T21:24:10)
    0000   0xca 0x18 0x15 0x15 0x0c                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x00 0x1b 0x00    $P.-j...
    0008   0x00 0x05 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    0   27    0
              0    5    0   27  125
    

should eat up to null first: 0x5c
0000   0x5c 0x08 0x88 0xbe 0x04 0x5c 0xa4 0x14    \....\..
0008   0x01                                       .
special found
0000   0x1b 0x1b 0x02 0xca 0x18 0x75 0x15 0x0c    .....u..
0008   0x07 0x00                                  ..
#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x5c 0x08 0x88 0xbe 0x04 0x5c 0xa4 0x14    \....\..
    0008   0x01 0x1b 0x1b 0x02 0xca 0x18 0x75 0x15    ......u.
    0010   0x0c 0x07 0x00 0x00 0x04 0xc4 0xd5 0x0c    ........
    0018   0x6d 0xd5 0x0c 0x05 0x00 0xa2 0x7e 0xba    m.....~.
    0020   0x05 0x00 0x00 0x04 0xc4 0x03 0x74 0x48    ......tH
    0028   0x01 0x50 0x1c 0x00 0x61 0x01 0x50 0x1c    .P..a.P.
##### DEBUG DECIMAL
             92    8  136  190    4   92  164   20
              1   27   27    2  202   24  117   21
             12    7    0    0    4  196  213   12
            109  213   12    5    0  162  126  186
              5    0    0    4  196    3  116   72
              1   80   28    0   97    1   80   28
XXX:???:XXX 2004-04-30T08:08:28
`end logs/ReadHistoryData-page-9.data: 12 records`
