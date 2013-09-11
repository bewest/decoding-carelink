## START logs/ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 46, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x50 0x36 0x5c 0x11 0x50 0x8b 0x04 0x40    P6\.P..@
    0008   0xef 0x04 0x10 0xf9 0x04 0x34 0x99 0x14    .....4..
    0010   0x74 0xb7 0x14 0x69 0xd1 0x9c 0x2b 0x73    t..i..+s
    0018   0x19 0x0c 0x15 0x1e 0x01 0x00 0x50 0x00    ......P.
##### DEBUG DECIMAL
             80   54   92   17   80  139    4   64
            239    4   16  249    4   52  153   20
            116  183   20  105  209  156   43  115
             25   12   21   30    1    0   80    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 1.6, 'curve': 4},
 {'age': 114, 'amount': 0.4, 'curve': 4},
 {'age': 18, 'amount': 1.3, 'curve': 20},
 {'age': 48, 'amount': 2.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x40 0x68 0x04 0x10 0x72 0x04    \.@h..r.
    0008   0x34 0x12 0x14 0x74 0x30 0x14              4..t0.
    decimal
             92   14   64  104    4   16  114    4
             52   18   20  116   48   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2007, 4, 0, 12, 0, 16) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x50 0x00                        ..P.
    decimal
              1    0   80    0
    datetime ((2007, 4, 0, 12, 0, 16))
    0000   0x50 0x00 0x2c 0x00 0x87                   P.,..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 Base (2012, 4, 0, 27, 12, 57) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x51                                  .Q
    decimal
             28   81
    datetime ((2012, 4, 0, 27, 12, 57))
    0000   0x79 0x0c 0x5b 0x00 0x9c                   y.[..
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 3 Base (2000, 4, 16, 22, 12, 57) head[2], body[0] op[0x2b]

    op hex (2)
    0000   0x2b 0x13                                  +.
    decimal
             43   19
    datetime ((2000, 4, 16, 22, 12, 57))
    0000   0x79 0x0c 0x16 0x90 0x00                   y....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 4 Base (2000, 0, 16, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 16, 0, 0, 54))
    0000   0x36 0x00 0x00 0x50 0x00                   6..P.
    body (0)
    DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-13.data: 5 records`
