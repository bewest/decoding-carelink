## START analysis/xiali/raw//ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 147, found 45 nulls
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

#### RECORD 3 MResultTotals 2003-01-02T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2003-01-02T00:00:00)
    0000   0x01 0x83                                  ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 Rewind 2013-08-20T09:34:49 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-20T09:34:49)
    0000   0xb1 0x22 0x09 0x14 0x0d                   ."...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 Rewind 2013-08-20T09:40:13 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-20T09:40:13)
    0000   0x8d 0x28 0x09 0x14 0x0d                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 Rewind 2013-08-20T09:40:45 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-20T09:40:45)
    0000   0xad 0x28 0x09 0x14 0x0d                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 Rewind 2013-08-20T09:41:28 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-20T09:41:28)
    0000   0x9c 0x29 0x09 0x14 0x0d                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 Rewind 2013-08-20T11:23:57 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-20T11:23:57)
    0000   0xb9 0x17 0x0b 0x14 0x0d                   .....
    body (0)

#### RECORD 9 Prime 2013-08-20T11:28:52 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 25.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0xff                   .....
    decimal
              3    0    0    0  255
    datetime (2013-08-20T11:28:52)
    0000   0xb4 0x1c 0x2b 0x14 0x0d                   ..+..
    body (0)

#### RECORD 10 Prime 2013-08-20T11:30:12 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 10.0, 'fixed': 10.0, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x64 0x00 0x64                   ..d.d
    decimal
              3    0  100    0  100
    datetime (2013-08-20T11:30:12)
    0000   0x8c 0x1e 0x0b 0x14 0x0d                   .....
    body (0)

#### RECORD 11 NoDelivery 2013-08-20T11:36:50 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0xa1 0x06 0xdd                        ....
    decimal
              6  161    6  221
    datetime (2013-08-20T11:36:50)
    0000   0xb2 0x24 0x2b 0xf4 0x0d                   .$+..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 1]
#### RECORD 12 ChangeBasalProfile 2013-08-20T11:42:19 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x00                                  ..
    decimal
              8    0
    datetime (2013-08-20T11:42:19)
    0000   0x93 0x2a 0x0b 0x14 0x0d                   .*...
    body (44)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00                        ....
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0
    HOUR BITS: [0, 0, 1]
`end analysis/xiali/raw//ReadHistoryData-page-0.data: 13 records`
