### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-0.data.list_opcodes.markdown: 2
## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 462, found 560 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x38 0x72                                  8r
##### DEBUG DECIMAL
             56  114
#### RECORD 0 hack1 2013-01-19T21:49:27 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x12 0x8d 0x05 0x00 0x73 0x58 0x8e    m....sX.
    0008   0x02 0x00 0x00 0x04 0x78 0x03 0x68 0x4c    ....x.hL
    0010   0x01 0x10 0x18 0x00 0x5b 0x01 0x10 0x18    ....[...
    0018   0x01 0x04 0x60 0x00 0x0c 0x04 0x00 0x00    ..`.....
    0020   0x00 0x03 0x02 0x00 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x4b              .....K
    decimal
            109   18  141    5    0  115   88  142
              2    0    0    4  120    3  104   76
              1   16   24    0   91    1   16   24
              1    4   96    0   12    4    0    0
              0    3    2    0    1    0   12    0
            232    0    0    0   10   75
    datetime (2013-01-19T21:49:27)
    0000   0x1b 0x71 0x35 0x13 0x0d                   .q5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-01-19T21:50:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.9,
 'carb_input': 87,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
--
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-01-19T21:50:15)
    0000   0x0f 0x72 0x95 0x13 0x0d                   .r...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 Bolus 2013-01-19T21:51:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'programmed': 3.3}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x04                        .!!.
    decimal
              1   33   33    4
    datetime (2013-01-19T21:51:59)
    0000   0x3b 0x73 0xb5 0x13 0x0d                   ;s...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 ResultTotals 2013-02-19T13:13:19 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x70                   ....p
    decimal
              7    0    0    4  112
    datetime (2013-02-19T13:13:19)
    0000   0x13 0x8d 0x6d 0x13 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x4b 0x4b 0x4b 0x01 0x00 0x00    ..KKK...
    0008   0x04 0x70 0x03 0x84 0x4f 0x00 0xec 0x15    .p..O...
    0010   0x00 0x57 0x00 0xec 0x15 0x00 0xec 0x64    .W.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   75   75   75    1    0    0
              4  112    3  132   79    0  236   21
              0   87    0  236   21    0  236  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 PumpSuspend 2013-01-20T09:36:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-20T09:36:38)
    0000   0x26 0x64 0x09 0x14 0x0d                   &d...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 PumpResume 2013-01-20T09:55:32 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-20T09:55:32)
--
    decimal
             39    0    0    0    0    0    0   40
              0    0    0    0    0    0
    HOUR BITS: [0, 1, 0]
#### RECORD 23 EnableDisableRemote 2013-01-20T16:23:29 head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0x00                                  &.
    decimal
             38    0
    datetime (2013-01-20T16:23:29)
    0000   0x1d 0x57 0x10 0x14 0x0d                   .W...
    body (14)
    hex
    0000   0x27 0x00 0x00 0x00 0x00 0x00 0x00 0x28    '......(
    0008   0x00 0x00 0x00 0x00 0x00 0x00              ......
    decimal
             39    0    0    0    0    0    0   40
              0    0    0    0    0    0
    HOUR BITS: [0, 1, 0]
#### RECORD 24 ResultTotals 2013-02-20T13:13:20 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xae                   .....
    decimal
              7    0    0    4  174
    datetime (2013-02-20T13:13:20)
    0000   0x14 0x8d 0x6d 0x14 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x9a 0x6b 0xe0 0x04 0x00 0x00    ...k....
    0008   0x04 0xae 0x03 0x76 0x4a 0x01 0x38 0x1a    ...vJ.8.
    0010   0x00 0x4b 0x01 0x38 0x1a 0x00 0xe0 0x48    .K.8...H
    0018   0x00 0x58 0x1c 0x00 0x00 0x00 0x04 0x03    .X......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  154  107  224    4    0    0
              4  174    3  118   74    1   56   26
              0   75    1   56   26    0  224   72
              0   88   28    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 CalBGForPH 2013-01-21T08:53:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 212}
```
    op hex (2)
    0000   0x0a 0xd4                                  ..
    decimal
             10  212
    datetime (2013-01-21T08:53:57)
    0000   0x39 0x75 0x28 0x15 0x0d                   9u(..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2013-01-21T08:54:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
--
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x13 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
              0   80   13   45  106   19    0    0
              0    0    0   19  125
    HOUR BITS: [0, 1, 1]
#### RECORD 27 Bolus 2013-01-21T08:54:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-01-21T08:54:05)
    0000   0x05 0x76 0x48 0x15 0x0d                   .vH..
    body (0)
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-0.data: 28 records`
