## START logs/ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 48, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x78 0x00 0x00 0x00 0x00 0x78 0x36 0x5c    x....x6\
    0008   0x0e 0xc0 0x48 0x04 0x54 0x84 0x04 0x98    ..H.T...
    0010   0xe8 0x04 0x6c 0x9c 0x14 0x5b 0x00 0x83    ..l..[..
    0018   0x2f 0x12 0x6b 0x0d 0x21 0x90 0x00 0x6e    /.k.!..n
##### DEBUG DECIMAL
            120    0    0    0    0  120   54   92
             14  192   72    4   84  132    4  152
            232    4  108  156   20   91    0  131
             47   18  107   13   33  144    0  110
#### RECORD 0 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 2.1, 'curve': 4},
 {'age': 165, 'amount': 3.8, 'curve': 4},
 {'age': 89, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x54 0x41 0x04 0x98 0xa5 0x04    \.TA....
    0008   0x6c 0x59 0x14                             lY.
    decimal
             92   11   84   65    4  152  165    4
            108   89   20
    datetime (unknown)

    body (0)

#### RECORD 1 Base (2013, 8, 11, 17, 40, 56) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2013, 8, 11, 17, 40, 56))
    0000   0xb8 0x28 0x71 0x0b 0x0d                   .(q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 Base (2000, 0, 0, 0, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2000, 0, 0, 0, 0, 1))
    0000   0x01 0x00 0xc0 0x00 0xc0                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 3 Base (2011, 2, 17, 8, 56, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x68                                  .h
    decimal
              0  104
    datetime ((2011, 2, 17, 8, 56, 0))
    0000   0x00 0xb8 0x28 0x51 0x6b                   ..(Qk
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 Base (2011, 2, 18, 15, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2011, 2, 18, 15, 0, 0))
    0000   0x00 0x80 0x2f 0x12 0x6b                   ../.k
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 5 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x21                                  .!
    decimal
             13   33
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-23.data: 6 records`
