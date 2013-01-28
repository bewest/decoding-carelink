### MIDNIGHTS analysis/bewest-pump/ReadHistoryData-page-34.data.list_opcodes.markdown: 3
## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1f 0xf2                                  ..
##### DEBUG DECIMAL
             31  242
#### RECORD 0 BolusWizard 2012-09-17T18:56:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 188,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.8}
```
    op hex (2)
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2012-09-17T18:56:02)
    0000   0x82 0x78 0x12 0x11 0x0c                   .x...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x08 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    8    0    6  125
    HOUR BITS: [0, 1, 1]
#### RECORD 1 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 0.6, 'curve': 4},
 {'age': 202, 'amount': 2.3, 'curve': 4},
--
             92   17   24    5    4   24   75    4
             92  205    4   18  245    4   98  255
              4
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2012-09-17T18:59:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-09-17T18:59:07)
    0000   0x87 0x7b 0x52 0x11 0x0c                   .{R..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 8 ResultTotals 2012-10-17T13:12:17 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime (2012-10-17T13:12:17)
    0000   0x91 0x8c 0x6d 0x91 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x9f 0x46 0xbc 0x07 0x00 0x00    ...F....
    0008   0x05 0x08 0x03 0x70 0x44 0x01 0x98 0x20    ...pD.. 
    0010   0x00 0x88 0x01 0x98 0x20 0x01 0x78 0x5c    .... .x\
    0018   0x00 0x20 0x08 0x00 0x00 0x00 0x06 0x04    . ......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  159   70  188    7    0    0
              5    8    3  112   68    1  152   32
              0  136    1  152   32    1  120   92
              0   32    8    0    0    0    6    4
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 Rewind 2012-09-18T04:36:42 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-09-18T04:36:42)
    0000   0xaa 0x64 0x04 0x12 0x0c                   .d...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 Prime 2012-09-18T04:38:09 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x28                   ....(
    decimal
              3    0    0    0   40
    datetime (2012-09-18T04:38:09)
--
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0x03 0x21 0x00    ,P.-j.!.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             44   80   13   45  106    3   33    0
              0    0    0   36  125
    HOUR BITS: [0, 1, 1]
#### RECORD 28 Bolus 2012-09-18T23:51:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-09-18T23:51:48)
    0000   0xb0 0x73 0x57 0x12 0x0c                   .sW..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 29 ResultTotals 2012-10-18T13:12:18 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xb6                   .....
    decimal
              7    0    0    5  182
    datetime (2012-10-18T13:12:18)
    0000   0x92 0x8c 0x6d 0x92 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xd9 0x8e 0x45 0x03 0x00 0x00    ....E...
    0008   0x05 0xb6 0x03 0x6e 0x3c 0x02 0x48 0x28    ...n<.H(
    0010   0x00 0x75 0x02 0x48 0x28 0x01 0x5c 0x3c    .u.H(.\<
    0018   0x00 0xec 0x28 0x00 0x00 0x00 0x05 0x02    ..(.....
    0020   0x01 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  217  142   69    3    0    0
              5  182    3  110   60    2   72   40
              0  117    2   72   40    1   92   60
              0  236   40    0    0    0    5    2
              1    2    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 PumpSuspend 2012-09-19T14:12:51 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-19T14:12:51)
    0000   0xb3 0x4c 0x0e 0x13 0x0c                   .L...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 31 PumpResume 2012-09-19T14:45:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-19T14:45:08)
--
    decimal
             92   11   12   56   20   32   76   20
            208  136   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2012-09-19T21:46:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'programmed': 2.2}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2012-09-19T21:46:35)
    0000   0xa3 0x6e 0x55 0x13 0x0c                   .nU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 46 ResultTotals 2012-10-19T13:12:19 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc4                   .....
    decimal
              7    0    0    4  196
    datetime (2012-10-19T13:12:19)
    0000   0x93 0x8c 0x6d 0x93 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xc1 0x68 0x25 0x03 0x00 0x00    ...h%...
    0008   0x04 0xc4 0x03 0x70 0x48 0x01 0x54 0x1c    ...pH.T.
    0010   0x00 0x56 0x01 0x54 0x1c 0x00 0xfc 0x4a    .V.T...J
    0018   0x00 0x58 0x1a 0x00 0x00 0x00 0x04 0x03    .X......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  193  104   37    3    0    0
              4  196    3  112   72    1   84   28
              0   86    1   84   28    0  252   74
              0   88   26    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 47 CalForBG 2012-09-20T08:52:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 28}
```
    op hex (2)
    0000   0x0a 0x1c                                  ..
    decimal
             10   28
    datetime (2012-09-20T08:52:14)
    0000   0x8e 0x74 0x28 0x14 0x8c                   .t(..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 48 BolusWizard 2012-09-20T08:52:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 284,
--
    decimal
             92   14   26   52   20   78   62   20
              8  112   20   22  172   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2012-09-20T19:02:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-09-20T19:02:06)
    0000   0x86 0x42 0x53 0x14 0x0c                   .BS..
    body (0)
    HOUR BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-34.data: 79 records`
