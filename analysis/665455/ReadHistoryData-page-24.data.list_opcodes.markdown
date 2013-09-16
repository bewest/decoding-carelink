## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 116, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x08 0x7d 0x01 0x08 0x08 0x00 0x7b 0x1e    .}....{.
    0008   0x4e 0x17 0x0d 0x5b 0x00 0x65 0x32 0x0e    N..[.e2.
    0010   0x17 0x0d 0x39 0x50 0x0d 0x2d 0x6a 0x00    ..9P.-j.
    0018   0x2b 0x00 0x00 0x00 0x00 0x2b 0x7d 0x5c    +....+}\
##### DEBUG DECIMAL
              8  125    1    8    8    0  123   30
             78   23   13   91    0  101   50   14
             23   13   57   80   13   45  106    0
             43    0    0    0    0   43  125   92
#### RECORD 0 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 0.9, 'curve': 4},
 {'age': 14, 'amount': 1.5, 'curve': 20},
 {'age': 24, 'amount': 2.3, 'curve': 20},
 {'age': 164, 'amount': 1.2, 'curve': 20},
 {'age': 204, 'amount': 0.8, 'curve': 20},
 {'age': 214, 'amount': 0.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x24 0x32 0x04 0x3c 0x0e 0x14    \.$2.<..
    0008   0x5c 0x18 0x14 0x30 0xa4 0x14 0x20 0xcc    \..0.. .
    0010   0x14 0x18 0xd6 0x14                        ....
    decimal
             92   20   36   50    4   60   14   20
             92   24   20   48  164   20   32  204
             20   24  214   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-04-22T20:44:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-04-22T20:44:25)
    0000   0x59 0x2c 0x54 0x16 0x0d                   Y,T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 ResultTotals 2013-04-22T13:13:22 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xf4                   .....
    decimal
              7    0    0    5  244
    datetime (2013-04-22T13:13:22)
    0000   0x56 0x0d 0x6d 0x56 0x0d                   V.mV.
    body (51)
    hex
    0000   0x05 0x00 0xa4 0x73 0xf0 0x07 0x00 0x00    ...s....
    0008   0x05 0xf4 0x03 0x48 0x37 0x02 0xac 0x2d    ...H7..-
    0010   0x00 0xb0 0x02 0xac 0x2d 0x02 0x14 0x4e    ....-..N
    0018   0x00 0x98 0x16 0x00 0x00 0x00 0x07 0x03    ........
    0020   0x02 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x65 0x23 0x0d 0x17 0x0d    ...e#...
    0030   0x1f 0x00 0x63                             ..c
    decimal
              5    0  164  115  240    7    0    0
              5  244    3   72   55    2  172   45
              0  176    2  172   45    2   20   78
              0  152   22    0    0    0    7    3
              2    2    0   12    0  232    0    0
              0   30    0  101   35   13   23   13
             31    0   99
    DAY BITS: [0, 1, 0]
#### RECORD 3 Prime (2007, 9, 14, 30, 56, 35) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.0, 'fixed': 2.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x0e 0x17 0x0d 0x0a                   .....
    decimal
              3   14   23   13   10
    datetime ((2007, 9, 14, 30, 56, 35))
    0000   0xa3 0x78 0x1e 0x2e 0x17                   .x...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 4 Base (2007, 9, 14, 30, 59, 35) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2007, 9, 14, 30, 59, 35))
    0000   0xa3 0x7b 0x1e 0x0e 0x17                   .{...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 5 Base (2008, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2008, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x08                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-24.data: 6 records`
