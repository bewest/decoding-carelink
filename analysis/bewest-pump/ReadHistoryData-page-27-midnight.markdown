WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-27.data
#### RECORD 0 PumpSuspend 2012-10-15T18:08:47 head[2], body[0] 0x1e
    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-15T18:08:47)
    0000   0xaf 0x88 0x12 0x0f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 1 PumpResume 2012-10-15T18:31:07 head[2], body[0] 0x1f
    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-15T18:31:07)
    0000   0x87 0x9f 0x12 0x0f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 2 CalForBG 2012-10-15T18:36:06 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2012-10-15T18:36:06)
    0000   0x86 0xa4 0x32 0x0f 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 0, 1]

#### RECORD 3 BolusWizard 2012-10-15T18:36:13 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0x9a                                  [.
    decimal
             91  154
    datetime (2012-10-15T18:36:13)
    0000   0x8d 0xa4 0x12 0x0f 0x0c                   .....
    body (22)
    hex
    0000   0x21 0x50 0x0d 0x2d 0x6a 0x06 0x19 0x00    !P.-j...
--
#### RECORD 17 CalForBG 2012-10-15T21:33:41 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x08                                  ..
    decimal
             10    8
    datetime (2012-10-15T21:33:41)
    0000   0xa9 0xa1 0x35 0x0f 0x8c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]

#### RECORD 18 CalForBG 2012-10-15T22:12:34 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xe3                                  ..
    decimal
             10  227
    datetime (2012-10-15T22:12:34)
    0000   0xa2 0x8c 0x36 0x0f 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 19 ResultTotals MIDNIGHT!? head[2], body[44] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x07 0xa0 0xaf 0x0c                   .....
    body (44)
    hex
    0000   0x6d 0xaf 0x0c 0x05 0x11 0x33 0x9a 0xbc    m....3..
    0008   0x0d 0x00 0x00 0x07 0xa0 0x03 0xa0 0x30    .......0
    0010   0x04 0x00 0x34 0x00 0x8a 0x04 0x00 0x34    ..4....4
    0018   0x01 0xa0 0x29 0x02 0x60 0x3b 0x00 0x00    ..).`;..
    0020   0x00 0x08 0x03 0x04 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00                        ....
    decimal
            109  175   12    5   17   51  154  188
             13    0    0    7  160    3  160   48
              4    0   52    0  138    4    0   52
              1  160   41    2   96   59    0    0
              0    8    3    4    1    0   12    0
            232    0    0    0
    

Traceback (most recent call last):
  File "list_opcodes.py", line 317, in <module>
    main( )
  File "list_opcodes.py", line 301, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 247, in find_dates
    assert datetime is not None, "\n%s" % lib.hexdump(bolus)
AssertionError: 
0000   0x0a 0x4d 0x97 0x8c 0x21 0x10 0x0c         .M..!..
