### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-20.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6c 0xde                                  l.
##### DEBUG DECIMAL
            108  222
#### RECORD 0 hack1 2012-11-09T10:14:03 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0xa8 0x8c 0x05 0x00 0x75 0x4d 0x8d    m....uM.
    0008   0x05 0x00 0x00 0x05 0x34 0x03 0x6c 0x42    ....4.lB
    0010   0x01 0xc8 0x22 0x00 0x90 0x01 0xc8 0x22    .."...."
    0018   0x01 0xb4 0x60 0x00 0x14 0x04 0x00 0x00    ..`.....
    0020   0x00 0x03 0x01 0x00 0x02 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x21 0x00              ....!.
    decimal
            109  168  140    5    0  117   77  141
              5    0    0    5   52    3  108   66
              1  200   34    0  144    1  200   34
              1  180   96    0   20    4    0    0
              0    3    1    0    2    0   12    0
            232    0    0    0   33    0
    datetime (2012-11-09T10:14:03)
    0000   0x83 0xce 0x0a 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 Prime 2012-11-09T10:15:03 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x40                   ....@
    decimal
              3    0    0    0   64
    datetime (2012-11-09T10:15:03)
    0000   0x83 0xcf 0x2a 0x09 0x0c                   ..*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 Prime 2012-11-09T10:15:35 head[5], body[0] op[0x03]

--
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-11-09T19:41:14)
    0000   0x8e 0xe9 0x93 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 Bolus 2012-11-09T19:43:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x02                        ....
    decimal
              1   29   29    2
    datetime (2012-11-09T19:43:16)
    0000   0x90 0xeb 0xb3 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 ResultTotals 2012-10-09T13:12:41 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xb8                   .....
    decimal
              7    0    0    5  184
    datetime (2012-10-09T13:12:41)
    0000   0xa9 0x8c 0x6d 0xa9 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x97 0x6c 0xd8 0x05 0x00 0x00    ...l....
    0008   0x05 0xb8 0x03 0x84 0x3d 0x02 0x34 0x27    ....=.4'
    0010   0x00 0xe2 0x02 0x34 0x27 0x01 0xd8 0x54    ...4'..T
    0018   0x00 0x5c 0x10 0x00 0x00 0x00 0x05 0x03    .\......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  151  108  216    5    0    0
              5  184    3  132   61    2   52   39
              0  226    2   52   39    1  216   84
              0   92   16    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 CalBGForPH 2012-11-10T00:50:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 278}
```
    op hex (2)
    0000   0x0a 0x16                                  ..
    decimal
             10   22
    datetime (2012-11-10T00:50:24)
    0000   0x98 0xf2 0x20 0x0a 0x8c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 27 BolusWizard 2012-11-10T00:50:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 278,
--
    0000   0x5c 0x08 0xc8 0x41 0x04 0xa0 0x7d 0x04    \..A..}.
    decimal
             92    8  200   65    4  160  125    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-11-10T20:49:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-11-10T20:49:10)
    0000   0x8a 0xf1 0x54 0x0a 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 ResultTotals 2012-10-10T13:12:42 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x60                   ....`
    decimal
              7    0    0    6   96
    datetime (2012-10-10T13:12:42)
    0000   0xaa 0x8c 0x6d 0xaa 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xbe 0x5f 0x16 0x06 0x00 0x00    ..._....
    0008   0x06 0x60 0x03 0x80 0x37 0x02 0xe0 0x2d    .`..7..-
    0010   0x00 0x99 0x02 0xe0 0x2d 0x01 0xc4 0x3d    ....-..=
    0018   0x01 0x1c 0x27 0x00 0x00 0x00 0x05 0x03    ..'.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  190   95   22    6    0    0
              6   96    3  128   55    2  224   45
              0  153    2  224   45    1  196   61
              1   28   39    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 CalBGForPH 2012-11-11T01:59:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 224}
```
    op hex (2)
    0000   0x0a 0xe0                                  ..
    decimal
             10  224
    datetime (2012-11-11T01:59:01)
    0000   0x81 0xfb 0x21 0x0b 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 50 BolusWizard 2012-11-11T01:59:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 224,
--
    0000   0x5c 0x05 0x30 0x75 0x04                   \.0u.
    decimal
             92    5   48  117    4
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2012-11-11T22:31:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'programmed': 2.2}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2012-11-11T22:31:44)
    0000   0xac 0xdf 0x56 0x0b 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 78 ResultTotals 2012-10-11T13:12:43 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x3a                   ....:
    decimal
              7    0    0    6   58
    datetime (2012-10-11T13:12:43)
    0000   0xab 0x8c 0x6d 0xab 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xbb 0x47 0x53 0x06 0x00 0x00    ...GS...
    0008   0x06 0x3a 0x03 0x72 0x37 0x02 0xc8 0x2d    .:.r7..-
    0010   0x00 0x79 0x02 0xc8 0x2d 0x01 0x50 0x2f    .y..-.P/
    0018   0x01 0x78 0x35 0x00 0x00 0x00 0x07 0x03    .x5.....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  187   71   83    6    0    0
              6   58    3  114   55    2  200   45
              0  121    2  200   45    1   80   47
              1  120   53    0    0    0    7    3
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 79 CalBGForPH 2012-11-12T00:55:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2012-11-12T00:55:31)
    0000   0x9f 0xf7 0x20 0x0c 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-20.data: 80 records`
