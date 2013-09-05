## START logs/ReadHistoryData-page-8.data
#### STOPPING DOUBLE NULLS @ 32, found 10 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x64 0xd7 0x00 0x00 0x00 0x00 0x00 0x00    d.......
    0008   0x00 0x00 0x7b 0x01 0x80 0x00 0x04 0x11    ..{.....
    0010   0x0d 0x08 0x21 0x00 0x0a 0xe4 0x93 0x2f    ..!..../
    0018   0x27 0x11 0x0d 0x5b 0xe4 0x96 0x2f 0x07    '..[../.
##### DEBUG DECIMAL
            100  215    0    0    0    0    0    0
              0    0  123    1  128    0    4   17
             13    8   33    0   10  228  147   47
             39   17   13   91  228  150   47    7
#### RECORD 0 Base (2000, 0, 20, 0, 5, 13) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x90                                  n.
    decimal
            110  144
    datetime ((2000, 0, 20, 0, 5, 13))
    0000   0x0d 0x05 0x00 0x74 0x00                   ...t.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2002, 0, 24, 4, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x09                                  ..
    decimal
              0    9
    datetime ((2002, 0, 24, 4, 0, 0))
    0000   0x00 0x00 0x04 0xd8 0x02                   .....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 2 Base (2013, 3, 0, 9, 60, 1) head[2], body[0] op[0xdc]

    op hex (2)
    0000   0xdc 0x3b                                  .;
    decimal
            220   59
    datetime ((2013, 3, 0, 9, 60, 1))
    0000   0x01 0xfc 0x29 0x00 0x8d                   ..)..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 Bolus (2009, 0, 0, 0, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 25.2, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0xfc 0x00 0x00                        ....
    decimal
              1  252    0    0
    datetime ((2009, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x09                   .....
    body (0)

`end logs/ReadHistoryData-page-8.data: 4 records`
