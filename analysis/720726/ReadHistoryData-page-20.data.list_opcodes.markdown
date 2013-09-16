## START logs/ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 43, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0a 0x48 0x97 0x10 0x21 0x71 0x0d 0x3f    .H..!q.?
    0008   0x09 0x97 0x10 0x01 0x71 0x0d 0x69 0x69    ....q.ii
    0010   0x96 0x7b 0x01 0x80 0x00 0x04 0x11 0x0d    .{......
    0018   0x08 0x2e 0x00 0x0a 0x4e 0xaf 0x02 0x29    ....N..)
##### DEBUG DECIMAL
             10   72  151   16   33  113   13   63
              9  151   16    1  113   13  105  105
            150  123    1  128    0    4   17   13
              8   46    0   10   78  175    2   41
#### RECORD 0 Base (2006, 0, 25, 0, 6, 13) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x90                                  n.
    decimal
            110  144
    datetime ((2006, 0, 25, 0, 6, 13))
    0000   0x0d 0x06 0x20 0xd9 0x56                   .. .V
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 1 NoDelivery (2007, 0, 9, 3, 25, 9) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x00 0x00                        ....
    decimal
              6    6    0    0
    datetime ((2007, 0, 9, 3, 25, 9))
    0000   0x09 0x19 0x03 0x89 0x27                   ....'
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 2 Base (2004, 0, 1, 13, 0, 61) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x90                                  ..
    decimal
              5  144
    datetime ((2004, 0, 1, 13, 0, 61))
    0000   0x3d 0x00 0xed 0x01 0xe4                   =....
    body (0)
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 3 Bolus 2003-01-01T04:08:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x02 0x54                        ...T
    decimal
              1   16    2   84
    datetime (2003-01-01T04:08:00)
    0000   0x00 0x48 0x04 0x01 0x03                   .H...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 Bolus (2000, 0, 0, 0, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x00 0x00                        ....
    decimal
              1    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-20.data: 5 records`
