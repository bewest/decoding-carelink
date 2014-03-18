## START logs/ReadHistoryData-page-32.data
#### STOPPING DOUBLE NULLS @ 123, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0d 0x00 0x13 0x7d 0x5c 0x11 0x20 0x8f    ...}\. .
    0008   0x04 0x4c 0x99 0x04 0x64 0xb7 0x04 0x18    .L..d...
    0010   0xdf 0x04 0xbc 0x4d 0x14 0x01 0x13 0x13    ...M....
    0018   0x00 0x36 0xc7 0x55 0x1b 0x0d 0x0a 0x4b    .6.U...K
##### DEBUG DECIMAL
             13    0   19  125   92   17   32  143
              4   76  153    4  100  183    4   24
            223    4  188   77   20    1   19   19
              0   54  199   85   27   13   10   75
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 0.6, 'curve': 4},
 {'age': 158, 'amount': 4.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0x30 0x04 0xbc 0x9e 0x04    \..0....
    decimal
             92    8   24   48    4  188  158    4
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2008-01-09T00:27:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x19 0x19 0x00 0x01 0xcc 0x52 0x1b    ......R.
    decimal
              1   25   25    0    1  204   82   27
    datetime (2008-01-09T00:27:13)
    0000   0x0d 0x5b 0x00 0x09 0xe8                   .[...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 0]
#### RECORD 2 Base (2013, 0, 13, 16, 25, 13) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0x1b                                  ..
    decimal
             18   27
    datetime ((2013, 0, 13, 16, 25, 13))
    0000   0x0d 0x19 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 3 Base (2000, 0, 0, 0, 0, 19) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x00                                  j.
    decimal
            106    0
    datetime ((2000, 0, 0, 0, 0, 19))
    0000   0x13 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 4 Base (2004, 4, 4, 4, 11, 28) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x7d                                  .}
    decimal
             19  125
    datetime ((2004, 4, 4, 4, 11, 28))
    0000   0x5c 0x0b 0x64 0x24 0x04                   \.d$.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 5 NewTimeSet (2001, 2, 4, 26, 60, 4) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x4c                                  .L
    decimal
             24   76
    datetime ((2001, 2, 4, 26, 60, 4))
    0000   0x04 0xbc 0xba 0x04 0x01                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 Base (2011, 0, 18, 8, 10, 0) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x13                                  ..
    decimal
             19   19
    datetime ((2011, 0, 18, 8, 10, 0))
    0000   0x00 0x0a 0xe8 0x52 0x1b                   ...R.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 7 Base (2011, 0, 18, 15, 43, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2011, 0, 18, 15, 43, 0))
    0000   0x00 0x2b 0xef 0x12 0x1b                   .+...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 8 Base (2000, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0b                                  ..
    decimal
             13   11
    datetime ((2000, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x00                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 9 ChangeBasalProfile (2013, 0, 8, 0, 0, 0) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x00                                  ..
    decimal
              8    0
    datetime ((2013, 0, 8, 0, 0, 0))
    0000   0x00 0x00 0x00 0x08 0x7d                   ....}
    body (44)
    hex
    0000   0x5c 0x0e 0x4c 0x0d 0x04 0x64 0x2b 0x04    \.L..d+.
    0008   0x18 0x53 0x04 0xbc 0xc1 0x04 0x01 0x08    .S......
    0010   0x08 0x00 0x2b 0xef 0x52 0x1b 0x0d 0x0a    ..+.R...
    0018   0x11 0x16 0xc7 0x35 0x1b 0x8d 0x5b 0x11    ...5..[.
    0020   0x36 0xc7 0x15 0x1b 0x0d 0x00 0x51 0x0d    6.....Q.
    0028   0x2d 0x6a 0x20 0x00                        -j .
    decimal
             92   14   76   13    4  100   43    4
             24   83    4  188  193    4    1    8
              8    0   43  239   82   27   13   10
             17   22  199   53   27  141   91   17
             54  199   21   27   13    0   81   13
             45  106   32    0
    YEAR BITS: [0, 1, 1, 1]
`end logs/ReadHistoryData-page-32.data: 10 records`
