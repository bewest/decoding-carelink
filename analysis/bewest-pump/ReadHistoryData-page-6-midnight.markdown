### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-6.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-6.data
#### RECORD 0 TempBasal 2012-12-30T21:45:37 head[2], body[1] op[0x33]

    op hex (2)
    0000   0x33 0x2a                                  3*
    decimal
             51   42
    datetime (2012-12-30T21:45:37)
    0000   0xe5 0x2d 0x15 0x1e 0x0c                   .-...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 0, 1]
#### RECORD 1 EndTempBasal 2012-12-30T21:45:37 head[2], body[0] op[0x16]

    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2012-12-30T21:45:37)
    0000   0xe5 0x2d 0x15 0x1e 0x0c                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 CalForBG 2012-12-30T21:45:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2012-12-30T21:45:54)
    0000   0xf6 0x2d 0x35 0x1e 0x0c                   .-5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalForBG 2012-12-30T21:47:53 head[2], body[0] op[0x0a]
###### DECODED
```python
--
             20    8  128   20    8  138   20   10
            148   20    8  158   20   10  168   20
              8  178   20   80  188   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2012-12-30T21:48:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-12-30T21:48:17)
    0000   0xd1 0x30 0x55 0x1e 0x0c                   .0U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 ResultTotals 2012-12-30T13:12:30 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xac                   .....
    decimal
              7    0    0    5  172
    datetime (2012-12-30T13:12:30)
    0000   0xde 0x0c 0x6d 0xde 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xa2 0x54 0xd2 0x09 0x00 0x00    ...T....
    0008   0x05 0xac 0x03 0x78 0x3d 0x02 0x34 0x27    ...x=.4'
    0010   0x00 0x91 0x02 0x34 0x27 0x01 0x9e 0x49    ...4'..I
    0018   0x00 0x96 0x1b 0x00 0x00 0x00 0x06 0x03    ........
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  162   84  210    9    0    0
              5  172    3  120   61    2   52   39
              0  145    2   52   39    1  158   73
              0  150   27    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 8 CalForBG 2012-12-31T00:06:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2012-12-31T00:06:37)
    0000   0xe5 0x06 0x20 0x1f 0x0c                   .. ..
    body (0)

#### RECORD 9 CalForBG 2012-12-31T00:57:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
--
    0000   0x5c 0x08 0x90 0x95 0x04 0x40 0xcb 0x14    \....@..
    decimal
             92    8  144  149    4   64  203   20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2012-12-31T21:53:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-12-31T21:53:41)
    0000   0xe9 0x35 0x55 0x1f 0x0c                   .5U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 ResultTotals 2012-12-31T13:12:31 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x60                   ....`
    decimal
              7    0    0    5   96
    datetime (2012-12-31T13:12:31)
    0000   0xdf 0x0c 0x6d 0xdf 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x7f 0x4f 0xd5 0x0e 0x00 0x00    ...O....
    0008   0x05 0x60 0x03 0x84 0x41 0x01 0xdc 0x23    .`..A..#
    0010   0x00 0x90 0x01 0xdc 0x23 0x01 0x90 0x54    ....#..T
    0018   0x00 0x4c 0x10 0x00 0x00 0x00 0x06 0x04    .L......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  127   79  213   14    0    0
              5   96    3  132   65    1  220   35
              0  144    1  220   35    1  144   84
              0   76   16    0    0    0    6    4
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 41 CalForBG 2013-01-01T00:14:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2013-01-01T00:14:46)
    0000   0x2e 0x4e 0x20 0x01 0x0d                   .N ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 42 LowReservoir 2013-01-01T03:52:30 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
--
    decimal
             92   11   12   91    4  136  101    4
            200  195   20
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-01-01T18:15:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-01-01T18:15:45)
    0000   0x2d 0x4f 0x52 0x01 0x0d                   -OR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 59 ResultTotals 2013-02-01T13:13:01 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x06                   .....
    decimal
              7    0    0    5    6
    datetime (2013-02-01T13:13:01)
    0000   0x01 0x8d 0x6d 0x01 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x60 0x45 0x6c 0x04 0x00 0x00    ..`El...
    0008   0x05 0x06 0x03 0x76 0x45 0x01 0x90 0x1f    ...vE...
    0010   0x00 0x87 0x01 0x90 0x1f 0x01 0x90 0x64    .......d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   96   69  108    4    0    0
              5    6    3  118   69    1  144   31
              0  135    1  144   31    1  144  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 60 CalForBG 2013-01-02T01:25:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-01-02T01:25:50)
    0000   0x32 0x59 0x21 0x02 0x0d                   2Y!..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 61 CalForBG 2013-01-02T09:26:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
--
    decimal
             92   14   56  166    4   60  176    4
             44  246    4  244  210   20
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2013-01-02T21:20:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-01-02T21:20:55)
    0000   0x37 0x54 0x55 0x02 0x0d                   7TU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 80 ResultTotals (2000, 2, 0, 0, 13, 2) head[5], body[36] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xa4                   .....
    decimal
              7    0    0    5  164
    datetime ((2000, 2, 0, 0, 13, 2))
    0000   0x02 0x8d 0x00 0x00 0x00                   .....
    body (36)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0xe1 0x1f                        ....
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0  225   31
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-6.data: 81 records`
