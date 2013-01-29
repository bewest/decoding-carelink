### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-5.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-5.data
#### RECORD 0 hack1 2013-01-03T02:05:39 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x02 0x8d 0x05 0x00 0x94 0x49 0xea    m.....I.
    0008   0x06 0x00 0x00 0x05 0xa4 0x03 0x84 0x3e    .......>
    0010   0x02 0x20 0x26 0x00 0x89 0x02 0x20 0x26    . &... &
    0018   0x01 0x80 0x47 0x00 0xa0 0x1d 0x00 0x00    ..G.....
    0020   0x00 0x05 0x02 0x02 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x5c              .....\
    decimal
            109    2  141    5    0  148   73  234
              6    0    0    5  164    3  132   62
              2   32   38    0  137    2   32   38
              1  128   71    0  160   29    0    0
              0    5    2    2    1    0   12    0
            232    0    0    0   10   92
    datetime (2013-01-03T02:05:39)
    0000   0x27 0x45 0x22 0x03 0x0d                   'E"..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 1 CalBGForPH 2013-01-03T09:59:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2013-01-03T09:59:29)
    0000   0x1d 0x7b 0x29 0x03 0x0d                   .{)..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2013-01-03T09:59:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 78,
 'bg_target_high': 125,
--
    0000   0x5c 0x05 0x78 0xb0 0x14                   \.x..
    decimal
             92    5  120  176   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-01-03T21:36:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-01-03T21:36:09)
    0000   0x09 0x64 0x55 0x03 0x0d                   .dU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 29 ResultTotals 2013-02-03T13:13:03 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xcc                   .....
    decimal
              7    0    0    6  204
    datetime (2013-02-03T13:13:03)
    0000   0x03 0x8d 0x6d 0x03 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x61 0x42 0xd3 0x0a 0x00 0x00    ..aB....
    0008   0x06 0xcc 0x03 0xe8 0x39 0x02 0xe4 0x2b    ....9..+
    0010   0x00 0xf8 0x02 0xe4 0x2b 0x02 0xbc 0x5f    ....+.._
    0018   0x00 0x28 0x05 0x00 0x00 0x00 0x05 0x04    .(......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   97   66  211   10    0    0
              6  204    3  232   57    2  228   43
              0  248    2  228   43    2  188   95
              0   40    5    0    0    0    5    4
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 CalBGForPH 2013-01-04T03:40:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-01-04T03:40:08)
    0000   0x08 0x68 0x23 0x04 0x0d                   .h#..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 31 LowReservoir 2013-01-04T13:51:49 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
--
    0000   0x5c 0x08 0xc4 0x43 0x14 0x44 0x61 0x14    \..C.Da.
    decimal
             92    8  196   67   20   68   97   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-01-04T21:37:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x38 0x38 0x03                        .88.
    decimal
              1   56   56    3
    datetime (2013-01-04T21:37:22)
    0000   0x16 0x65 0x75 0x04 0x0d                   .eu..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 47 ResultTotals 2013-02-04T13:13:04 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x6c                   ....l
    decimal
              7    0    0    5  108
    datetime (2013-02-04T13:13:04)
    0000   0x04 0x8d 0x6d 0x04 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x6e 0x66 0x75 0x04 0x00 0x00    ..nfu...
    0008   0x05 0x6c 0x03 0x84 0x41 0x01 0xe8 0x23    .l..A..#
    0010   0x00 0xa4 0x01 0xe8 0x23 0x01 0xe8 0x64    ....#..d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  110  102  117    4    0    0
              5  108    3  132   65    1  232   35
              0  164    1  232   35    1  232  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 48 CalBGForPH 2013-01-05T01:01:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 222}
```
    op hex (2)
    0000   0x0a 0xde                                  ..
    decimal
             10  222
    datetime (2013-01-05T01:01:10)
    0000   0x0a 0x41 0x21 0x05 0x0d                   .A!..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 49 BolusWizard 2013-01-05T01:01:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
--
    0000   0x5c 0x08 0x04 0xb1 0x04 0x6c 0xbb 0x04    \....l..
    decimal
             92    8    4  177    4  108  187    4
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-01-05T23:21:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.7, 'dual_component': '??', 'programmed': 6.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x43 0x43 0x00                        .CC.
    decimal
              1   67   67    0
    datetime (2013-01-05T23:21:11)
    0000   0x0b 0x55 0x57 0x05 0x0d                   .UW..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 68 ResultTotals 2013-02-05T13:13:05 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xc4                   .....
    decimal
              7    0    0    6  196
    datetime (2013-02-05T13:13:05)
    0000   0x05 0x8d 0x6d 0x05 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xfb 0x6a 0x47 0x05 0x00 0x00    ...jG...
    0008   0x06 0xc4 0x03 0x84 0x34 0x03 0x40 0x30    ....4.@0
    0010   0x00 0x77 0x03 0x40 0x30 0x01 0x68 0x2b    .w.@0.h+
    0018   0x01 0xd8 0x39 0x00 0x00 0x00 0x05 0x01    ..9.....
    0020   0x02 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  251  106   71    5    0    0
              6  196    3  132   52    3   64   48
              0  119    3   64   48    1  104   43
              1  216   57    0    0    0    5    1
              2    2    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 CalBGForPH 2013-01-06T01:12:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-01-06T01:12:30)
    0000   0x1e 0x4c 0x21 0x06 0x0d                   .L!..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 70 CalBGForPH 2013-01-06T04:56:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
--
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0xfb 0x27 0xf0    3P.-j.'.
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             51   80   13   45  106  251   39  240
              0    0    0   34  125
    HOUR BITS: [0, 1, 1]
#### RECORD 73 Bolus 2013-01-06T19:47:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-01-06T19:47:16)
    0000   0x10 0x6f 0x53 0x06 0x0d                   .oS..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 74 ResultTotals (2000, 2, 0, 0, 13, 6) head[5], body[17] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x0c                   .....
    decimal
              7    0    0    4   12
    datetime ((2000, 2, 0, 0, 13, 6))
    0000   0x06 0x8d 0x00 0x00 0x00                   .....
    body (17)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x98    ........
    0010   0xed                                       .
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0  152
            237
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-5.data: 75 records`
