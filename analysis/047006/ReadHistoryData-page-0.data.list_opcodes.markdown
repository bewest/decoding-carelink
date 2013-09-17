## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 104, found 88 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x06 0x11 0x01 0xee 0x00 0x40 0x40 0xa1    .....@@.
    0008   0x03 0x17 0x00 0x15 0x41 0x00 0x01 0x03    ....A...
    0010   0x18 0x00 0x80 0x14 0x09 0x14 0x0d 0x07    ........
    0018   0x00 0x00 0x00 0x00 0x01 0x83 0x21 0x00    ......!.
##### DEBUG DECIMAL
              6   17    1  238    0   64   64  161
              3   23    0   21   65    0    1    3
             24    0  128   20    9   20   13    7
              0    0    0    0    1  131   33    0
#### RECORD 0 NoDelivery 2003-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x11 0x01 0xee                        ....
    decimal
              6   17    1  238
    datetime (2003-01-01T00:00:00)
    0000   0x00 0x40 0x40 0xa1 0x03                   .@@..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 1 ChangeTime 2003-01-01T00:01:21 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2003-01-01T00:01:21)
    0000   0x15 0x41 0x00 0x01 0x03                   .A...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 2 NewTimeSet 2013-08-20T09:20:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-08-20T09:20:00)
    0000   0x80 0x14 0x09 0x14 0x0d                   .....
    body (0)

#### RECORD 3 ResultTotals (2001, 2, 0, 1, 3, 1) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime ((2001, 2, 0, 1, 3, 1))
    0000   0x01 0x83 0x21 0x00 0xb1                   ..!..
    body (41)
    hex
    0000   0x22 0x09 0x14 0x0d 0x21 0x00 0x8d 0x28    "...!..(
    0008   0x09 0x14 0x0d 0x21 0x00 0xad 0x28 0x09    ...!..(.
    0010   0x14 0x0d 0x21 0x00 0x9c 0x29 0x09 0x14    ..!..)..
    0018   0x0d 0x21 0x00 0xb9 0x17 0x0b 0x14 0x0d    .!......
    0020   0x03 0x00 0x00 0x00 0xff 0xb4 0x1c 0x2b    .......+
    0028   0x14                                       .
    decimal
             34    9   20   13   33    0  141   40
              9   20   13   33    0  173   40    9
             20   13   33    0  156   41    9   20
             13   33    0  185   23   11   20   13
              3    0    0    0  255  180   28   43
             20
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 4 Base (2012, 1, 4, 0, 36, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x03                                  ..
    decimal
             13    3
    datetime ((2012, 1, 4, 0, 36, 0))
    0000   0x00 0x64 0x00 0x64 0x8c                   .d.d.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 PumpSuspend (2006, 0, 1, 6, 13, 20) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x0b                                  ..
    decimal
             30   11
    datetime ((2006, 0, 1, 6, 13, 20))
    0000   0x14 0x0d 0x06 0xa1 0x06                   .....
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 6 Base (2008, 0, 13, 20, 43, 36) head[2], body[0] op[0xdd]

    op hex (2)
    0000   0xdd 0xb2                                  ..
    decimal
            221  178
    datetime ((2008, 0, 13, 20, 43, 36))
    0000   0x24 0x2b 0xf4 0x0d 0x08                   $+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 Base (2000, 0, 13, 20, 11, 42) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x93                                  ..
    decimal
              0  147
    datetime ((2000, 0, 13, 20, 11, 42))
    0000   0x2a 0x0b 0x14 0x0d 0x00                   *....
    body (0)

`end logs/ReadHistoryData-page-0.data: 8 records`
