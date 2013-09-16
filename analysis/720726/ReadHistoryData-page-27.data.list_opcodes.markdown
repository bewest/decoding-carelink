## START logs/ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 142, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x5c 0x00 0x00 0x00 0x00 0x5c 0x36 0x5c    \....\6\
    0008   0x0e 0x6c 0xb7 0x04 0x84 0xf3 0x04 0xe4    .l......
    0010   0x4d 0x14 0x1c 0x57 0x14 0x01 0x00 0x5c    M..W...\
    0018   0x00 0x5c 0x00 0x14 0x00 0xb8 0x30 0x57    .\....0W
##### DEBUG DECIMAL
             92    0    0    0    0   92   54   92
             14  108  183    4  132  243    4  228
             77   20   28   87   20    1    0   92
              0   92    0   20    0  184   48   87
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 97, 'amount': 5.7, 'curve': 4},
 {'age': 107, 'amount': 0.7, 'curve': 4},
 {'age': 81, 'amount': 2.5, 'curve': 20},
 {'age': 181, 'amount': 3.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xe4 0x61 0x04 0x1c 0x6b 0x04    \..a..k.
    0008   0x64 0x51 0x14 0x9c 0xb5 0x14              dQ....
    decimal
             92   14  228   97    4   28  107    4
            100   81   20  156  181   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-08-05T19:52:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x9c 0x00    ........
    decimal
              1    0  132    0  132    0  156    0
    datetime (2013-08-05T19:52:24)
    0000   0x98 0x34 0x53 0x65 0x0d                   .4Se.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-08-05T20:09:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-08-05T20:09:49)
    0000   0xb1 0x09 0x34 0x65 0x0d                   ..4e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 3 Base (2013, 8, 5, 20, 9, 49) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime ((2013, 8, 5, 20, 9, 49))
    0000   0xb1 0x09 0x14 0x65 0x0d                   ...e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 4 Ian69 2002-09-19T00:27:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2002-09-19T00:27:22)
    0000   0x96 0x5b 0x00 0x93 0x32                   .[..2
    body (8)
    hex
    0000   0x14 0x65 0x0d 0x1e 0x90 0x00 0x6e 0x17    .e....n.
    decimal
             20  101   13   30  144    0  110   23
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 5 Base (2000, 1, 0, 0, 44, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x00                                  6.
    decimal
             54    0
    datetime ((2000, 1, 0, 0, 44, 0))
    0000   0x00 0x6c 0x00 0x00 0x00                   .l...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 Base (2001, 1, 4, 14, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6c                                  .l
    decimal
              0  108
    datetime ((2001, 1, 4, 14, 28, 54))
    0000   0x36 0x5c 0x0e 0x84 0x41                   6\..A
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 7 Base (2004, 8, 5, 28, 4, 27) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0xe4                                  ..
    decimal
              4  228
    datetime ((2004, 8, 5, 28, 4, 27))
    0000   0x9b 0x04 0x1c 0xa5 0x04                   .....
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 8 ChangeTimeDisplay (2000, 0, 12, 0, 1, 20) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x8b                                  d.
    decimal
            100  139
    datetime ((2000, 0, 12, 0, 1, 20))
    0000   0x14 0x01 0x00 0x6c 0x00                   ...l.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 9 Base (2004, 8, 18, 19, 0, 48) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x00                                  l.
    decimal
            108    0
    datetime ((2004, 8, 18, 19, 0, 48))
    0000   0xb0 0x00 0x93 0x32 0x54                   ...2T
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 10 Base (2006, 2, 11, 6, 9, 10) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x0d                                  e.
    decimal
            101   13
    datetime ((2006, 2, 11, 6, 9, 10))
    0000   0x0a 0x89 0xa6 0x2b 0x36                   ...+6
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 11 Base (2006, 0, 11, 6, 17, 63) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x0d                                  e.
    decimal
            101   13
    datetime ((2006, 0, 11, 6, 17, 63))
    0000   0x3f 0x11 0xa6 0x2b 0x36                   ?..+6
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 12 Base (2012, 5, 10, 22, 41, 41) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x0d                                  e.
    decimal
            101   13
    datetime ((2012, 5, 10, 22, 41, 41))
    0000   0x69 0x69 0x96 0x0a 0xac                   ii...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 13 Base (2005, 1, 31, 13, 37, 55) head[2], body[0] op[0x96]

    op hex (2)
    0000   0x96 0x04                                  ..
    decimal
            150    4
    datetime ((2005, 1, 31, 13, 37, 55))
    0000   0x37 0x65 0x0d 0x3f 0x15                   7e.?.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 14 Base (2009, 9, 9, 13, 37, 23) head[2], body[0] op[0x96]

    op hex (2)
    0000   0x96 0x04                                  ..
    decimal
            150    4
    datetime ((2009, 9, 9, 13, 37, 23))
    0000   0x97 0x65 0x0d 0x69 0x69                   .e.ii
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 15 Base (2005, 2, 23, 16, 56, 0) head[2], body[0] op[0x96]

    op hex (2)
    0000   0x96 0x5b                                  .[
    decimal
            150   91
    datetime ((2005, 2, 23, 16, 56, 0))
    0000   0x00 0xb8 0x30 0x17 0x65                   ..0.e
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 16 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1a                                  ..
    decimal
             13   26
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-27.data: 17 records`
