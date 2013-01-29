### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-19.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1d 0xc0                                  ..
##### DEBUG DECIMAL
             29  192
#### RECORD 0 BolusWizard 2012-11-12T00:55:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.7}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2012-11-12T00:55:42)
    0000   0xaa 0xf7 0x00 0x0c 0x0c                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    7    0   11  125
    HOUR BITS: [1, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 151, 'amount': 2.2, 'curve': 4},
 {'age': 5, 'amount': 1.2, 'curve': 20}]
--
             92   17  208   26    4   94   66    4
             14   76    4   40  140   20   88  150
             20
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2012-11-12T21:40:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-11-12T21:40:51)
    0000   0xb3 0xe8 0x55 0x0c 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 ResultTotals 2012-10-12T13:12:44 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x00                   .....
    decimal
              7    0    0    6    0
    datetime (2012-10-12T13:12:44)
    0000   0xac 0x8c 0x6d 0xac 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xcd 0x46 0x0c 0x07 0x00 0x00    ...F....
    0008   0x06 0x00 0x03 0x60 0x38 0x02 0xa0 0x2c    ...`8..,
    0010   0x00 0xa9 0x02 0xa0 0x2c 0x01 0x78 0x38    ....,.x8
    0018   0x01 0x28 0x2c 0x00 0x00 0x00 0x08 0x04    .(,.....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  205   70   12    7    0    0
              6    0    3   96   56    2  160   44
              0  169    2  160   44    1  120   56
              1   40   44    0    0    0    8    4
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 CalBGForPH 2012-11-13T05:21:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 356}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-11-13T05:21:45)
    0000   0xad 0xd5 0x25 0x0d 0x8c                   ..%..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 44 BolusWizard 2012-11-13T05:21:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 356,
--
    0000   0x5c 0x08 0x2c 0x22 0x04 0x40 0x94 0x14    \.,".@..
    decimal
             92    8   44   34    4   64  148   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2012-11-13T21:38:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-13T21:38:27)
    0000   0x9b 0xe6 0x55 0x0d 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 65 ResultTotals 2012-10-13T13:12:45 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x68                   ....h
    decimal
              7    0    0    5  104
    datetime (2012-10-13T13:12:45)
    0000   0xad 0x8c 0x6d 0xad 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x8f 0x53 0x64 0x06 0x00 0x00    ...Sd...
    0008   0x05 0x68 0x03 0x7c 0x40 0x01 0xec 0x24    .h.|@..$
    0010   0x00 0x6a 0x01 0xec 0x24 0x01 0x18 0x39    .j..$..9
    0018   0x00 0xd4 0x2b 0x00 0x00 0x00 0x05 0x04    ..+.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  143   83  100    6    0    0
              5  104    3  124   64    1  236   36
              0  106    1  236   36    1   24   57
              0  212   43    0    0    0    5    4
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 66 PumpSuspend 2012-11-14T13:09:13 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-14T13:09:13)
    0000   0x8d 0xc9 0x0d 0x0e 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 PumpResume 2012-11-14T13:22:16 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-14T13:22:16)
    0000   0x90 0xd6 0x0d 0x0e 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 ResultTotals 2012-10-14T13:12:46 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x7a                   ....z
    decimal
              7    0    0    3  122
    datetime (2012-10-14T13:12:46)
    0000   0xae 0x8c 0x6d 0xae 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x03 0x7a 0x03 0x7a 0x64 0x00 0x00 0x00    .z.zd...
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              3  122    3  122  100    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 PumpSuspend 2012-11-15T11:15:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-15T11:15:15)
    0000   0x8f 0xcf 0x0b 0x0f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 70 PumpResume 2012-11-15T11:31:12 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-15T11:31:12)
--
             52   80   13   45  106  250   40  240
              0    0    0   34  125
    HOUR BITS: [1, 1, 1]
#### RECORD 83 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 83, 'amount': 2.5, 'curve': 20},
 {'age': 153, 'amount': 0.7, 'curve': 20},
 {'age': 193, 'amount': 3.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x64 0x53 0x14 0x1c 0x99 0x14    \.dS....
    0008   0x8c 0xc1 0x14                             ...
    decimal
             92   11  100   83   20   28  153   20
            140  193   20
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-19.data: 84 records`
