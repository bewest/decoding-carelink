## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 35, found 17 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x5b 0x00 0x9d 0x30 0x00 0x6a 0x0d 0x12    [..0.j..
    0008   0x90 0x00 0x6e 0x17 0x36 0x00 0x00 0x40    ..n.6..@
    0010   0x00 0x00 0x00 0x00 0x40 0x36 0x5c 0x0e    ....@6\.
    0018   0x60 0x67 0x04 0x38 0x8f 0x04 0xe8 0xf3    `g.8....
##### DEBUG DECIMAL
             91    0  157   48    0  106   13   18
            144    0  110   23   54    0    0   64
              0    0    0    0   64   54   92   14
             96  103    4   56  143    4  232  243
#### RECORD 0 Base (2000, 0, 29, 16, 6, 13) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x89                                  n.
    decimal
            110  137
    datetime ((2000, 0, 29, 16, 6, 13))
    0000   0x0d 0x06 0x10 0x9d 0x50                   ....P
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 1 Bolus 2004-03-09T03:13:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x00 0x00                        ....
    decimal
              1    8    0    0
    datetime (2004-03-09T03:13:06)
    0000   0x06 0xcd 0x03 0x89 0x34                   ....4
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 2 Prime 2000-03-16T00:44:01 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 19.0, 'fixed': 4.8, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x44 0x30 0x00 0xbe                   .D0..
    decimal
              3   68   48    0  190
    datetime (2000-03-16T00:44:01)
    0000   0x01 0xec 0x00 0x70 0x00                   ...p.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 Base (2000, 0, 1, 2, 7, 0) head[2], body[0] op[0xe8]

    op hex (2)
    0000   0xe8 0x00                                  ..
    decimal
            232    0
    datetime ((2000, 0, 1, 2, 7, 0))
    0000   0x00 0x07 0x02 0x01 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-24.data: 4 records`
