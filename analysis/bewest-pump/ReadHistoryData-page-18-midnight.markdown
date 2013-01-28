### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-18.data.list_opcodes.markdown: 4
## START logs/ReadHistoryData-page-18.data
#### STOPPING DOUBLE NULLS @ 1008, found 14 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x98 0xdb                                  ..
##### DEBUG DECIMAL
            152  219
#### RECORD 0 Bolus 2012-11-15T19:43:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-11-15T19:43:57)
    0000   0xb9 0xeb 0x53 0x0f 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 BolusWizard 2012-11-15T19:55:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-11-15T19:55:50)
    0000   0xb2 0xf7 0x13 0x0f 0x0c                   .....
--
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-11-15T21:02:01)
    0000   0x81 0xc2 0x35 0x0f 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalForBG 2012-11-15T23:07:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 74}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2012-11-15T23:07:56)
    0000   0xb8 0xc7 0x37 0x0f 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 ResultTotals 2012-10-15T13:12:47 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x68                   ....h
    decimal
              7    0    0    5  104
    datetime (2012-10-15T13:12:47)
    0000   0xaf 0x8c 0x6d 0xaf 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x5d 0x4a 0x79 0x05 0x00 0x00    ..]Jy...
    0008   0x05 0x68 0x03 0x78 0x40 0x01 0xf0 0x24    .h.x@..$
    0010   0x00 0xb4 0x01 0xf0 0x24 0x01 0xf0 0x64    ....$..d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x05 0x05    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   93   74  121    5    0    0
              5  104    3  120   64    1  240   36
              0  180    1  240   36    1  240  100
              0    0    0    0    0    0    5    5
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 LowReservoir 2012-11-16T11:43:38 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-11-16T11:43:38)
    0000   0xa6 0xeb 0x0b 0x10 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 PumpSuspend 2012-11-16T14:20:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-16T14:20:19)
--
    0000   0x5c 0x05 0x8c 0x20 0x14                   \.. .
    decimal
             92    5  140   32   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2012-11-16T21:02:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'programmed': 3.7}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2012-11-16T21:02:05)
    0000   0x85 0xc2 0x55 0x10 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 ResultTotals 2012-10-16T13:12:48 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x98                   .....
    decimal
              7    0    0    4  152
    datetime (2012-10-16T13:12:48)
    0000   0xb0 0x8c 0x6d 0xb0 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x6e 0x60 0x75 0x03 0x00 0x00    ..n`u...
    0008   0x04 0x98 0x03 0x78 0x4c 0x01 0x20 0x18    ...xL. .
    0010   0x00 0x62 0x01 0x20 0x18 0x01 0x20 0x64    .b. .. d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  110   96  117    3    0    0
              4  152    3  120   76    1   32   24
              0   98    1   32   24    1   32  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 Rewind 2012-11-17T17:19:06 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-11-17T17:19:06)
    0000   0x86 0xd3 0x11 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 Prime 2012-11-17T17:20:22 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x0d                   .....
    decimal
              3    0    0    0   13
    datetime (2012-11-17T17:20:22)
--
    0000   0x5c 0x08 0xc0 0x3c 0x04 0x38 0x64 0x04    \..<.8d.
    decimal
             92    8  192   60    4   56  100    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2012-11-17T22:34:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-11-17T22:34:42)
    0000   0xaa 0xe2 0x96 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 ResultTotals 2012-10-17T13:12:49 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime (2012-10-17T13:12:49)
    0000   0xb1 0x8c 0x6d 0xb1 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xaf 0x92 0xbd 0x03 0x00 0x00    ........
    0008   0x05 0x08 0x03 0x82 0x46 0x01 0x86 0x1e    ....F...
    0010   0x00 0x6a 0x01 0x86 0x1e 0x01 0x4e 0x56    .j....NV
    0018   0x00 0x38 0x0e 0x00 0x00 0x00 0x03 0x02    .8......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  175  146  189    3    0    0
              5    8    3  130   70    1  134   30
              0  106    1  134   30    1   78   86
              0   56   14    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 41 Bolus 2012-11-17T22:35:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x03                        ....
    decimal
              1   24   24    3
    datetime (2012-11-17T22:35:34)
    0000   0xa2 0xe3 0xb6 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 CalForBG 2012-11-18T00:44:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
--
    0000   0x5c 0x05 0x90 0x1e 0x14                   \....
    decimal
             92    5  144   30   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2012-11-18T23:20:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-11-18T23:20:36)
    0000   0xa4 0xd4 0x57 0x12 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 ResultTotals 2012-10-18T13:12:50 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe8                   .....
    decimal
              7    0    0    5  232
    datetime (2012-10-18T13:12:50)
    0000   0xb2 0x8c 0x6d 0xb2 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb6 0x67 0x20 0x06 0x00 0x00    ...g ...
    0008   0x05 0xe8 0x03 0x7e 0x3b 0x02 0x6a 0x29    ...~;.j)
    0010   0x00 0x79 0x02 0x6a 0x29 0x01 0x6e 0x3b    .y.j).n;
    0018   0x00 0xfc 0x29 0x00 0x00 0x00 0x05 0x03    ..).....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  182  103   32    6    0    0
              5  232    3  126   59    2  106   41
              0  121    2  106   41    1  110   59
              0  252   41    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 66 PumpSuspend 2012-11-19T08:06:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-19T08:06:55)
    0000   0xb7 0xc6 0x08 0x13 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 PumpResume 2012-11-19T08:28:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-19T08:28:31)
--
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2012-11-19T18:27:18)
    0000   0x92 0xdb 0x52 0x13 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 80 CalForBG 2012-11-19T18:28:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2012-11-19T18:28:17)
    0000   0x91 0xdc 0x32 0x13 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-18.data: 81 records`
