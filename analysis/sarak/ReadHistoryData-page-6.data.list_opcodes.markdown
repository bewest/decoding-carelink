## START logs/ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 39, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x68 0x78 0x5c 0x0b 0x44 0xe0 0xc0 0x1a    hx\.D...
    0008   0x08 0xd0 0x22 0x12 0xd0 0x01 0x00 0x68    .."....h
    0010   0x00 0x68 0x00 0x00 0x00 0xae 0x39 0x56    .h....9V
    0018   0x15 0x0d 0x5b 0xaa 0xa9 0x06 0x17 0x15    ..[.....
##### DEBUG DECIMAL
            104  120   92   11   68  224  192   26
              8  208   34   18  208    1    0  104
              0  104    0    0    0  174   57   86
             21   13   91  170  169    6   23   21
#### RECORD 0 Bolus (2005, 4, 0, 16, 0, 4) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x44 0x00                        ..D.
    decimal
              1    0   68    0
    datetime ((2005, 4, 0, 16, 0, 4))
    0000   0x44 0x00 0x30 0x00 0xb5                   D.0..
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 1 Base (2007, 0, 10, 10, 13, 21) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x53                                  .S
    decimal
             16   83
    datetime ((2007, 0, 10, 10, 13, 21))
    0000   0x15 0x0d 0x0a 0xaa 0xa7                   .....
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 2 Base (2014, 0, 10, 27, 13, 21) head[2], body[0] op[0x39]

    op hex (2)
    0000   0x39 0x36                                  96
    decimal
             57   54
    datetime ((2014, 0, 10, 27, 13, 21))
    0000   0x15 0x0d 0x5b 0xaa 0xae                   ..[..
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 3 Base (2000, 0, 16, 18, 13, 21) head[2], body[0] op[0x39]

    op hex (2)
    0000   0x39 0x16                                  9.
    decimal
             57   22
    datetime ((2000, 0, 16, 18, 13, 21))
    0000   0x15 0x0d 0x12 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 4 ChangeTimeDisplay 2000-04-08T00:32:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-08T00:32:36)
    0000   0x64 0x20 0x00 0x48 0x00                   d .H.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-6.data: 5 records`
