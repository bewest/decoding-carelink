### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-17.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-17.data
#### STOPPING DOUBLE NULLS @ 1015, found 7 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xdb 0x71                                  .q
##### DEBUG DECIMAL
            219  113
#### RECORD 0 BolusWizard 2012-11-19T18:28:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 93,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 0.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5d                                  []
    decimal
             91   93
    datetime (2012-11-19T18:28:21)
    0000   0x95 0xdc 0x12 0x13 0x0c                   .....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0xfd 0x05 0xf0    .P.-j...
    0008   0x00 0x06 0x00 0x02 0x7d                   ....}
    decimal
              7   80   13   45  106  253    5  240
              0    6    0    2  125
--
    0000   0x5c 0x08 0x10 0x7c 0x04 0xa0 0x4e 0x14    \..|..N.
    decimal
             92    8   16  124    4  160   78   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2012-11-19T20:28:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-11-19T20:28:38)
    0000   0xa6 0xdc 0x54 0x13 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 ResultTotals 2012-10-19T13:12:51 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xde                   .....
    decimal
              7    0    0    4  222
    datetime (2012-10-19T13:12:51)
    0000   0xb3 0x8c 0x6d 0xb3 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x87 0x5d 0x02 0x06 0x00 0x00    ...]....
    0008   0x04 0xde 0x03 0x76 0x47 0x01 0x68 0x1d    ...vG.h.
    0010   0x00 0x58 0x01 0x68 0x1d 0x00 0xf0 0x43    .X.h...C
    0018   0x00 0x78 0x21 0x00 0x00 0x00 0x05 0x04    .x!.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  135   93    2    6    0    0
              4  222    3  118   71    1  104   29
              0   88    1  104   29    0  240   67
              0  120   33    0    0    0    5    4
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 CalBGForPH 2012-11-20T00:37:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2012-11-20T00:37:23)
    0000   0x97 0xe5 0x20 0x14 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 BolusWizard 2012-11-20T00:37:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
--
    0000   0x5c 0x08 0x20 0x7b 0x04 0xc8 0xcb 0x04    \. {....
    decimal
             92    8   32  123    4  200  203    4
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2012-11-20T22:07:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-11-20T22:07:44)
    0000   0xac 0xc7 0x56 0x14 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 ResultTotals 2012-10-20T13:12:52 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc8                   .....
    decimal
              7    0    0    4  200
    datetime (2012-10-20T13:12:52)
    0000   0xb4 0x8c 0x6d 0xb4 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x97 0x5b 0x00 0x03 0x00 0x00    ...[....
    0008   0x04 0xc8 0x03 0x78 0x49 0x01 0x50 0x1b    ...xI.P.
    0010   0x00 0x5c 0x01 0x50 0x1b 0x01 0x04 0x4d    .\.P...M
    0018   0x00 0x4c 0x17 0x00 0x00 0x00 0x04 0x03    .L......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  151   91    0    3    0    0
              4  200    3  120   73    1   80   27
              0   92    1   80   27    1    4   77
              0   76   23    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 LowReservoir 2012-11-21T07:28:25 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-11-21T07:28:25)
    0000   0x99 0xdc 0x07 0x15 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 PumpSuspend 2012-11-21T11:59:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
--
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2012-11-21T19:18:24)
    0000   0x98 0xd2 0x93 0x15 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 Bolus 2012-11-21T19:18:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x03                        ....
    decimal
              1   19   19    3
    datetime (2012-11-21T19:18:50)
    0000   0xb2 0xd2 0xb3 0x15 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 51 ResultTotals 2012-10-21T13:12:53 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xba                   .....
    decimal
              7    0    0    5  186
    datetime (2012-10-21T13:12:53)
    0000   0xb5 0x8c 0x6d 0xb5 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb3 0x5e 0x07 0x02 0x00 0x00    ...^....
    0008   0x05 0xba 0x03 0x6c 0x3c 0x02 0x4e 0x28    ...l<.N(
    0010   0x00 0xb7 0x02 0x4e 0x28 0x01 0xc2 0x4c    ...N(..L
    0018   0x00 0x8c 0x18 0x00 0x00 0x00 0x05 0x03    ........
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  179   94    7    2    0    0
              5  186    3  108   60    2   78   40
              0  183    2   78   40    1  194   76
              0  140   24    0    0    0    5    3
              0    2    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 52 CalBGForPH 2012-11-22T03:19:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 263}
```
    op hex (2)
    0000   0x0a 0x07                                  ..
    decimal
             10    7
    datetime (2012-11-22T03:19:12)
    0000   0x8c 0xd3 0x23 0x16 0x8c                   ..#..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 53 BolusWizard 2012-11-22T03:19:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
--
    decimal
             92   11   78   50    4   14   60    4
            120  250    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2012-11-22T19:44:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-22T19:44:41)
    0000   0xa9 0xec 0x53 0x16 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 ResultTotals 2012-10-22T13:12:54 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf0                   .....
    decimal
              7    0    0    4  240
    datetime (2012-10-22T13:12:54)
    0000   0xb6 0x8c 0x6d 0xb6 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x95 0x47 0x07 0x04 0x00 0x00    ...G....
    0008   0x04 0xf0 0x03 0x7c 0x47 0x01 0x74 0x1d    ...|G.t.
    0010   0x00 0x5e 0x01 0x74 0x1d 0x00 0xfc 0x44    .^.t...D
    0018   0x00 0x78 0x20 0x00 0x00 0x00 0x04 0x03    .x .....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  149   71    7    4    0    0
              4  240    3  124   71    1  116   29
              0   94    1  116   29    0  252   68
              0  120   32    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 70 CalBGForPH 2012-11-23T00:42:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2012-11-23T00:42:25)
    0000   0x99 0xea 0x20 0x17 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 71 PumpSuspend 2012-11-23T12:45:13 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
--
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2012-11-23T18:41:07)
    0000   0x87 0xe9 0x32 0x17 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 78 CalBGForPH 2012-11-23T21:56:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2012-11-23T21:56:37)
    0000   0xa5 0xf8 0x35 0x17 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-17.data: 79 records`
