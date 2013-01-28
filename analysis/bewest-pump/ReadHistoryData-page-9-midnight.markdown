### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-9.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-9.data
#### RECORD 0 Rewind 2012-12-21T14:41:41 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-21T14:41:41)
    0000   0xe9 0x29 0x0e 0x15 0x0c                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Prime 2012-12-21T14:43:52 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2c                   ....,
    decimal
              3    0    0    0   44
    datetime (2012-12-21T14:43:52)
    0000   0xf4 0x2b 0x2e 0x15 0x0c                   .+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 Prime 2012-12-21T14:44:18 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-21T14:44:18)
    0000   0xd2 0x2c 0x0e 0x15 0x0c                   .,...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalForBG 2012-12-21T18:18:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-21T18:18:19)
--
    0000   0x5c 0x08 0x88 0xbe 0x04 0x5c 0xa4 0x14    \....\..
    decimal
             92    8  136  190    4   92  164   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2012-12-21T21:24:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'programmed': 2.7}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x02                        ....
    decimal
              1   27   27    2
    datetime (2012-12-21T21:24:10)
    0000   0xca 0x18 0x75 0x15 0x0c                   ..u..
    body (0)

#### RECORD 16 ResultTotals 2012-12-21T13:12:21 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc4                   .....
    decimal
              7    0    0    4  196
    datetime (2012-12-21T13:12:21)
    0000   0xd5 0x0c 0x6d 0xd5 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xa2 0x7e 0xba 0x05 0x00 0x00    ...~....
    0008   0x04 0xc4 0x03 0x74 0x48 0x01 0x50 0x1c    ...tH.P.
    0010   0x00 0x61 0x01 0x50 0x1c 0x01 0x24 0x57    .a.P..$W
    0018   0x00 0x2c 0x0d 0x00 0x00 0x00 0x04 0x03    .,......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  162  126  186    5    0    0
              4  196    3  116   72    1   80   28
              0   97    1   80   28    1   36   87
              0   44   13    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 17 CalForBG 2012-12-22T10:16:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2012-12-22T10:16:04)
    0000   0xc4 0x10 0x2a 0x16 0x0c                   ..*..
    body (0)

#### RECORD 18 BolusWizard 2012-12-22T10:16:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 116,
--
    0000   0x5c 0x08 0x52 0x0c 0x14 0xda 0x16 0x14    \.R.....
    decimal
             92    8   82   12   20  218   22   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2012-12-22T18:42:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'programmed': 3.9}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2012-12-22T18:42:27)
    0000   0xdb 0x2a 0x52 0x16 0x0c                   .*R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 ResultTotals 2012-12-22T13:12:22 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x04                   .....
    decimal
              7    0    0    6    4
    datetime (2012-12-22T13:12:22)
    0000   0xd6 0x0c 0x6d 0xd6 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x93 0x35 0x3a 0x06 0x00 0x00    ...5:...
    0008   0x06 0x04 0x03 0x78 0x3a 0x02 0x8c 0x2a    ...x:..*
    0010   0x00 0x9e 0x02 0x8c 0x2a 0x01 0xd8 0x48    ....*..H
    0018   0x00 0xb4 0x1c 0x00 0x00 0x00 0x05 0x03    ........
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  147   53   58    6    0    0
              6    4    3  120   58    2  140   42
              0  158    2  140   42    1  216   72
              0  180   28    0    0    0    5    3
              0    2    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 40 PumpSuspend 2012-12-23T08:24:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-23T08:24:49)
    0000   0xf1 0x18 0x08 0x17 0x0c                   .....
    body (0)

#### RECORD 41 PumpResume 2012-12-23T08:39:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-23T08:39:30)
--
             20  118   20   22  128   20   20  138
             20   20  148   20  158  158   20   26
            168   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2012-12-23T20:08:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'programmed': 4.5}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2012-12-23T20:08:53)
    0000   0xf5 0x08 0x54 0x17 0x0c                   ..T..
    body (0)

#### RECORD 62 ResultTotals 2012-12-23T13:12:23 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x0e                   .....
    decimal
              7    0    0    6   14
    datetime (2012-12-23T13:12:23)
    0000   0xd7 0x0c 0x6d 0xd7 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x84 0x4e 0xbf 0x06 0x00 0x00    ...N....
    0008   0x06 0x0e 0x03 0x82 0x3a 0x02 0x8c 0x2a    ....:..*
    0010   0x00 0xc1 0x02 0x8c 0x2a 0x02 0x3a 0x57    ....*.:W
    0018   0x00 0x52 0x0d 0x00 0x00 0x00 0x04 0x02    .R......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  132   78  191    6    0    0
              6   14    3  130   58    2  140   42
              0  193    2  140   42    2   58   87
              0   82   13    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 63 CalForBG 2012-12-24T00:24:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 68}
```
    op hex (2)
    0000   0x0a 0x44                                  .D
    decimal
             10   68
    datetime (2012-12-24T00:24:01)
    0000   0xc1 0x18 0x20 0x18 0x0c                   .. ..
    body (0)

#### RECORD 64 CalForBG 2012-12-24T10:07:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
--
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-12-24T19:42:52)
    0000   0xf4 0x2a 0x53 0x18 0x0c                   .*S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 81 CalForBG 2012-12-24T22:21:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2012-12-24T22:21:41)
    0000   0xe9 0x15 0x36 0x18 0x0c                   ..6..
    body (0)

#### RECORD 82 ResultTotals (2000, 12, 0, 0, 12, 24) head[5], body[25] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x82                   .....
    decimal
              7    0    0    5  130
    datetime ((2000, 12, 0, 0, 12, 24))
    0000   0xd8 0x0c 0x00 0x00 0x00                   .....
    body (25)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xac    ........
    0018   0xf6                                       .
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0  172
            246

`end logs/ReadHistoryData-page-9.data: 83 records`
