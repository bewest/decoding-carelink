## START logs/ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 18, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1e 0x0d 0x00 0x1d 0x00 0x07 0x00 0x00    ........
    0008   0x04 0x84 0x9d 0x0d 0x00 0x00 0x00 0x6e    .......n
    0010   0x9d 0x0d 0x05 0x00 0xb0 0x00 0x00 0x07    ........
    0018   0x00 0x00 0x04 0x84 0x02 0xdc 0x3f 0x01    ......?.
##### DEBUG DECIMAL
             30   13    0   29    0    7    0    0
              4  132  157   13    0    0    0  110
            157   13    5    0  176    0    0    7
              0    0    4  132    2  220   63    1
#### RECORD 0 Bolus (2004, 4, 0, 8, 0, 20) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x54 0x00                        ..T.
    decimal
              1    0   84    0
    datetime ((2004, 4, 0, 8, 0, 20))
    0000   0x54 0x00 0x48 0x00 0x84                   T.H..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 Base (2000, 0, 0, 27, 13, 29) head[2], body[0] op[0x32]

    op hex (2)
    0000   0x32 0x53                                  2S
    decimal
             50   83
    datetime ((2000, 0, 0, 27, 13, 29))
    0000   0x1d 0x0d 0x7b 0x00 0x80                   ..{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-3.data: 2 records`
