## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 138, found 4 nulls
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

#### RECORD 1 Bolus 2012-08-29T00:19:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x04 0x00 0x04 0x00 0x20 0x00    ...... .
    decimal
              1    0    4    0    4    0   32    0
    datetime (2012-08-29T00:19:46)
    0000   0xae 0x13 0x40 0x7d 0x0c                   ..@}.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 2 Rewind 2012-08-29T00:36:04 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-08-29T00:36:04)
    0000   0x84 0x24 0x00 0x1d 0x0c                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 Prime 2012-08-29T00:37:24 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2b                   ....+
    decimal
              3    0    0    0   43
    datetime (2012-08-29T00:37:24)
    0000   0x98 0x25 0x20 0x1d 0x0c                   .% ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BasalProfileStart 2012-08-29T00:37:39 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-29T00:37:39)
    0000   0xa7 0x25 0x00 0x1d 0x0c                   .%...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BasalProfileStart 2012-08-29T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-29T04:00:00)
    0000   0x80 0x00 0x04 0x1d 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 6 CalBGForPH 2012-08-29T07:55:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 53}
```
    op hex (2)
    0000   0x0a 0x35                                  .5
    decimal
             10   53
    datetime (2012-08-29T07:55:42)
    0000   0xaa 0x37 0x27 0x7d 0x0c                   .7'}.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 Base (2012, 8, 29, 7, 55, 42) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime ((2012, 8, 29, 7, 55, 42))
    0000   0xaa 0x37 0xa7 0x7d 0x0c                   .7.}.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Base (2001, 8, 0, 0, 25, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2001, 8, 0, 0, 25, 22))
    0000   0x96 0x19 0x00 0x80 0x01                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 9 ChangeBasalProfile (2014, 1, 0, 2, 59, 12) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x1d                                  ..
    decimal
              8   29
    datetime ((2014, 1, 0, 2, 59, 12))
    0000   0x0c 0x7b 0x02 0x80 0x1e                   .{...
    body (44)
    hex
    0000   0x09 0x1d 0x0c 0x13 0x1e 0x00 0x19 0x00    ........
    0008   0x80 0x01 0x0a 0x1d 0x0c 0x0a 0xb1 0x97    ........
    0010   0x0d 0x2a 0x7d 0x0c 0x3f 0x16 0x97 0x0d    .*}.?...
    0018   0x2a 0x7d 0x0c 0x69 0x69 0x96 0x5b 0x62    *}.ii.[b
    0020   0x9b 0x0d 0x0a 0x7d 0x0c 0x00 0x90 0x00    ...}....
    0028   0x6e 0x17 0x36 0x4c                        n.6L
    decimal
              9   29   12   19   30    0   25    0
            128    1   10   29   12   10  177  151
             13   42  125   12   63   22  151   13
             42  125   12  105  105  150   91   98
            155   13   10  125   12    0  144    0
            110   23   54   76
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
`end logs/ReadHistoryData-page-11.data: 10 records`
