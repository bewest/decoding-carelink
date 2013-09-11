## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 139, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x4c 0x36 0x69 0x08 0x9b 0x0d 0x0a 0x1d    L6i.....
    0008   0x0c 0x0a 0x1e 0x01 0x00 0x4c 0x00 0x4c    .....L.L
    0010   0x00 0x00 0x00 0x9b 0x0d 0x4a 0x7d 0x0c    .....J}.
    0018   0x7b 0x03 0x80 0x00 0x0d 0x1d 0x0c 0x1a    {.......
##### DEBUG DECIMAL
             76   54  105    8  155   13   10   29
             12   10   30    1    0   76    0   76
              0    0    0  155   13   74  125   12
            123    3  128    0   13   29   12   26
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 2.7, 'curve': 4},
 {'age': 49, 'amount': 0.1, 'curve': 20},
 {'age': 59, 'amount': 3.2, 'curve': 20},
 {'age': 69, 'amount': 3.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0x9b 0x04 0x04 0x31 0x14    \.l...1.
    0008   0x80 0x3b 0x14 0x8c 0x45 0x14              .;..E.
    decimal
             92   14  108  155    4    4   49   20
            128   59   20  140   69   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2014, 0, 0, 0, 0, 4) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x04 0x00                        ....
    decimal
              1    0    4    0
    datetime ((2014, 0, 0, 0, 0, 4))
    0000   0x04 0x00 0x20 0x00 0xae                   .. ..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 2 Base (2004, 4, 0, 1, 12, 61) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x40                                  .@
    decimal
             19   64
    datetime ((2004, 4, 0, 1, 12, 61))
    0000   0x7d 0x0c 0x21 0x00 0x84                   }.!..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 Base (2000, 0, 0, 3, 12, 29) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x00                                  $.
    decimal
             36    0
    datetime ((2000, 0, 0, 3, 12, 29))
    0000   0x1d 0x0c 0x03 0x00 0x00                   .....
    body (0)

#### RECORD 4 Base (2012, 8, 29, 0, 37, 24) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2b                                  .+
    decimal
              0   43
    datetime ((2012, 8, 29, 0, 37, 24))
    0000   0x98 0x25 0x20 0x1d 0x0c                   .% ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 Base (2012, 8, 29, 0, 37, 39) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime ((2012, 8, 29, 0, 37, 39))
    0000   0xa7 0x25 0x00 0x1d 0x0c                   .%...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 Base (2000, 1, 0, 1, 59, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x20                                  . 
    decimal
              0   32
    datetime ((2000, 1, 0, 1, 59, 0))
    0000   0x00 0x7b 0x01 0x80 0x00                   .{...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 7 Base (2010, 0, 0, 14, 8, 12) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x1d                                  ..
    decimal
              4   29
    datetime ((2010, 0, 0, 14, 8, 12))
    0000   0x0c 0x08 0x2e 0x00 0x0a                   .....
    body (0)

#### RECORD 8 Base (2015, 0, 12, 29, 39, 55) head[2], body[0] op[0x35]

    op hex (2)
    0000   0x35 0xaa                                  5.
    decimal
             53  170
    datetime ((2015, 0, 12, 29, 39, 55))
    0000   0x37 0x27 0x7d 0x0c 0x3f                   7'}.?
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 9 NoDelivery (2006, 4, 9, 9, 12, 61) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0xaa 0x37 0xa7                        ..7.
    decimal
              6  170   55  167
    datetime ((2006, 4, 9, 9, 12, 61))
    0000   0x7d 0x0c 0x69 0x69 0x96                   }.ii.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 10 LowBattery 2012-08-29T08:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2012-08-29T08:01:00)
    0000   0x80 0x01 0x08 0x1d 0x0c                   .....
    body (0)

#### RECORD 11 Base (2012, 8, 29, 9, 30, 0) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime ((2012, 8, 29, 9, 30, 0))
    0000   0x80 0x1e 0x09 0x1d 0x0c                   .....
    body (0)

#### RECORD 12 Base (2001, 0, 0, 0, 25, 0) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x1e                                  ..
    decimal
             19   30
    datetime ((2001, 0, 0, 0, 25, 0))
    0000   0x00 0x19 0x00 0x80 0x01                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 13 CalBGForPH (2013, 0, 23, 17, 10, 12) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 29}
```
    op hex (2)
    0000   0x0a 0x1d                                  ..
    decimal
             10   29
    datetime ((2013, 0, 23, 17, 10, 12))
    0000   0x0c 0x0a 0xb1 0x97 0x0d                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 14 Base (2013, 0, 23, 22, 63, 12) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0x7d                                  *}
    decimal
             42  125
    datetime ((2013, 0, 23, 22, 63, 12))
    0000   0x0c 0x3f 0x16 0x97 0x0d                   .?...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 0]
#### RECORD 15 Base (2011, 1, 22, 9, 41, 12) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0x7d                                  *}
    decimal
             42  125
    datetime ((2011, 1, 22, 9, 41, 12))
    0000   0x0c 0x69 0x69 0x96 0x5b                   .ii.[
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 16 Base (2000, 0, 12, 29, 10, 13) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x9b                                  b.
    decimal
             98  155
    datetime ((2000, 0, 12, 29, 10, 13))
    0000   0x0d 0x0a 0x7d 0x0c 0x00                   ..}..
    body (0)

#### RECORD 17 Base (2000, 4, 12, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 12, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x4c 0x00                   n.6L.
    body (0)
    DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-11.data: 18 records`
