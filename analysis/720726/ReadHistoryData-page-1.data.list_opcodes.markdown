## START logs/ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 61, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x36 0x5c 0x1d 0x5c 0x16 0x04 0x48 0x34    6\.\..H4
    0008   0x04 0x78 0x3e 0x04 0x34 0xa2 0x04 0x0c    .x>.4...
    0010   0xc0 0x05 0x28 0x60 0x14 0x3c 0x92 0x14    ..(`.<..
    0018   0x34 0xa6 0x14 0x58 0xb0 0x14 0x01 0x00    4..X....
##### DEBUG DECIMAL
             54   92   29   92   22    4   72   52
              4  120   62    4   52  162    4   12
            192    5   40   96   20   60  146   20
             52  166   20   88  176   20    1    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 1.8, 'curve': 4},
 {'age': 44, 'amount': 3.0, 'curve': 4},
 {'age': 144, 'amount': 1.3, 'curve': 4},
 {'age': 174, 'amount': 0.3, 'curve': 5},
 {'age': 78, 'amount': 1.0, 'curve': 20},
 {'age': 128, 'amount': 1.5, 'curve': 20},
 {'age': 148, 'amount': 1.3, 'curve': 20},
 {'age': 158, 'amount': 2.2, 'curve': 20},
 {'age': 218, 'amount': 3.5, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x48 0x22 0x04 0x78 0x2c 0x04    \.H".x,.
    0008   0x34 0x90 0x04 0x0c 0xae 0x05 0x28 0x4e    4.....(N
    0010   0x14 0x3c 0x80 0x14 0x34 0x94 0x14 0x58    .<..4..X
    0018   0x9e 0x14 0x8c 0xda 0x14                   .....
    decimal
             92   29   72   34    4  120   44    4
             52  144    4   12  174    5   40   78
             20   60  128   20   52  148   20   88
            158   20  140  218   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2011, 4, 0, 20, 0, 28) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x5c 0x00                        ..\.
    decimal
              1    0   92    0
    datetime ((2011, 4, 0, 20, 0, 28))
    0000   0x5c 0x00 0xf4 0x00 0xab                   \....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 2 Base (2003, 4, 0, 27, 13, 41) head[2], body[0] op[0x42]

    op hex (2)
    0000   0x42 0x53                                  BS
    decimal
             66   83
    datetime ((2003, 4, 0, 27, 13, 41))
    0000   0x69 0x0d 0x5b 0x00 0x83                   i.[..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 Base (2000, 4, 16, 0, 13, 41) head[2], body[0] op[0x54]

    op hex (2)
    0000   0x54 0x13                                  T.
    decimal
             84   19
    datetime ((2000, 4, 16, 0, 13, 41))
    0000   0x69 0x0d 0x00 0x90 0x00                   i....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 4 Base (2000, 0, 0, 0, 0, 54) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x17                                  n.
    decimal
            110   23
    datetime ((2000, 0, 0, 0, 0, 54))
    0000   0x36 0x00 0x00 0x00 0x00                   6....
    body (0)

`end logs/ReadHistoryData-page-1.data: 5 records`
