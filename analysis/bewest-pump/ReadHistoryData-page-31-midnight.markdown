### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-31.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-31.data
#### RECORD 0 hack1 2012-09-28T07:49:10 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x9b 0x8c 0x05 0x00 0x9e 0x55 0xc5    m.....U.
    0008   0x03 0x00 0x00 0x05 0x10 0x03 0x74 0x44    ......tD
    0010   0x01 0x9c 0x20 0x00 0x84 0x01 0x9c 0x20    .. .... 
    0018   0x01 0x78 0x5b 0x00 0x24 0x09 0x00 0x00    .x[.$...
    0020   0x00 0x05 0x04 0x01 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x1e 0x00              ......
    decimal
            109  155  140    5    0  158   85  197
              3    0    0    5   16    3  116   68
              1  156   32    0  132    1  156   32
              1  120   91    0   36    9    0    0
              0    5    4    1    0    0   12    0
            232    0    0    0   30    0
    datetime (2012-09-28T07:49:10)
    0000   0x8a 0x71 0x07 0x1c 0x0c                   .q...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 1 PumpResume 2012-09-28T11:16:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-28T11:16:09)
    0000   0x89 0x50 0x0b 0x1c 0x0c                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 2 TempBasal 2012-09-28T11:53:29 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.15}
```
    op hex (2)
    0000   0x33 0x2e                                  3.
    decimal
             51   46
    datetime (2012-09-28T11:53:29)
--
    decimal
             92   14   26   66   20  186   76   20
            194  146   20    6  156   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2012-09-28T18:36:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2012-09-28T18:36:54)
    0000   0xb6 0x64 0x52 0x1c 0x0c                   .dR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 19 ResultTotals 2012-10-28T13:12:28 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime (2012-10-28T13:12:28)
    0000   0x9c 0x8c 0x6d 0x9c 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xdc 0x4d 0x61 0x04 0x00 0x00    ...Ma...
    0008   0x05 0x0c 0x02 0xf8 0x3b 0x02 0x14 0x29    ....;..)
    0010   0x00 0x68 0x02 0x14 0x29 0x01 0x20 0x36    .h..). 6
    0018   0x00 0xf4 0x2e 0x00 0x00 0x00 0x04 0x02    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  220   77   97    4    0    0
              5   12    2  248   59    2   20   41
              0  104    2   20   41    1   32   54
              0  244   46    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 CalBGForPH 2012-09-29T01:11:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 248}
```
    op hex (2)
    0000   0x0a 0xf8                                  ..
    decimal
             10  248
    datetime (2012-09-29T01:11:09)
    0000   0x89 0x4b 0x21 0x1d 0x0c                   .K!..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 21 BolusWizard 2012-09-29T01:11:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 27,
--
    0000   0x5c 0x05 0x50 0x12 0x04                   \.P..
    decimal
             92    5   80   18    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-09-29T21:22:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-09-29T21:22:09)
    0000   0x89 0x56 0x55 0x1d 0x0c                   .VU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 32 ResultTotals 2012-10-29T13:12:29 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x5e                   ....^
    decimal
              7    0    0    4   94
    datetime (2012-10-29T13:12:29)
    0000   0x9d 0x8c 0x6d 0x9d 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xae 0x64 0xf8 0x02 0x00 0x00    ...d....
    0008   0x04 0x5e 0x03 0x5a 0x4d 0x01 0x04 0x17    .^.ZM...
    0010   0x00 0x35 0x01 0x04 0x17 0x00 0x98 0x3a    .5.....:
    0018   0x00 0x6c 0x2a 0x00 0x00 0x00 0x03 0x02    .l*.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  174  100  248    2    0    0
              4   94    3   90   77    1    4   23
              0   53    1    4   23    0  152   58
              0  108   42    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 CalBGForPH 2012-09-30T02:03:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 305}
```
    op hex (2)
    0000   0x0a 0x31                                  .1
    decimal
             10   49
    datetime (2012-09-30T02:03:54)
    0000   0xb6 0x43 0x22 0x1e 0x8c                   .C"..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 BolusWizard 2012-09-30T02:04:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 40,
--
    0000   0x5c 0x05 0x18 0x23 0x04                   \..#.
    decimal
             92    5   24   35    4
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2012-09-30T20:29:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-09-30T20:29:35)
    0000   0xa3 0x5d 0x54 0x1e 0x0c                   .]T..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 47 ResultTotals 2012-10-30T13:12:30 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbe                   .....
    decimal
              7    0    0    4  190
    datetime (2012-10-30T13:12:30)
    0000   0x9e 0x8c 0x6d 0x9e 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xe6 0x9a 0x31 0x02 0x00 0x00    ....1...
    0008   0x04 0xbe 0x03 0x72 0x49 0x01 0x4c 0x1b    ...rI.L.
    0010   0x00 0x2e 0x01 0x4c 0x1b 0x00 0x8c 0x2a    ...L...*
    0018   0x00 0xc0 0x3a 0x00 0x00 0x00 0x03 0x01    ..:.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  230  154   49    2    0    0
              4  190    3  114   73    1   76   27
              0   46    1   76   27    0  140   42
              0  192   58    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 48 PumpSuspend 2012-10-01T14:42:35 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-01T14:42:35)
    0000   0xa3 0xaa 0x0e 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 PumpResume 2012-10-01T15:14:32 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-01T15:14:32)
--
    0008   0x28 0x54 0x14 0x28 0xae 0x14 0x14 0xcc    (T.(....
    0010   0x14 0xa8 0xd6 0x14                        ....
    decimal
             92   20  128  190    4   60  220    4
             40   84   20   40  174   20   20  204
             20  168  214   20
    datetime (unknown)

    body (0)

#### RECORD 78 Base unknown head[2], body[0] op[0xba]

    op hex (2)
    0000   0xba 0xf8                                  ..
    decimal
            186  248
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-31.data: 79 records`
