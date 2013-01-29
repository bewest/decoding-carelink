## START logs/ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xea 0x8f                                  ..
##### DEBUG DECIMAL
            234  143
#### RECORD 0 Bolus 2012-12-02T15:50:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-02T15:50:27)
    0000   0xdb 0x32 0x4f 0x02 0x0c                   .2O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 CalBGForPH 2012-12-02T18:30:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2012-12-02T18:30:09)
    0000   0xc9 0x1e 0x32 0x02 0x0c                   ..2..
    body (0)

#### RECORD 2 BolusWizard 2012-12-02T18:30:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 190,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2012-12-02T18:30:18)
    0000   0xd2 0x1e 0x12 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    1    0   13  125

#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 166, 'amount': 0.3, 'curve': 4},
 {'age': 120, 'amount': 2.0, 'curve': 20},
 {'age': 130, 'amount': 0.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0xa6 0x04 0x50 0x78 0x14    \....Px.
    0008   0x20 0x82 0x14                              ..
    decimal
             92   11   12  166    4   80  120   20
             32  130   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2012-12-02T18:30:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'programmed': 0.9}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2012-12-02T18:30:18)
    0000   0xd2 0x1e 0x52 0x02 0x0c                   ..R..
    body (0)

#### RECORD 5 CalBGForPH 2012-12-02T21:30:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-12-02T21:30:57)
    0000   0xf9 0x1e 0x35 0x02 0x0c                   ..5..
    body (0)

#### RECORD 6 BolusWizard 2012-12-02T21:31:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2012-12-02T21:31:21)
    0000   0xd5 0x1f 0x15 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0xfe 0x21 0xf0    +P.-j.!.
    0008   0x00 0x02 0x00 0x1f 0x7d                   ....}
    decimal
             43   80   13   45  106  254   33  240
              0    2    0   31  125

#### RECORD 7 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 187, 'amount': 0.9, 'curve': 4},
 {'age': 91, 'amount': 0.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0xbb 0x04 0x0c 0x5b 0x14    \.$...[.
    decimal
             92    8   36  187    4   12   91   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2012-12-02T21:31:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-12-02T21:31:21)
    0000   0xd5 0x1f 0x55 0x02 0x0c                   ..U..
    body (0)

#### RECORD 9 CalBGForPH 2012-12-02T22:12:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2012-12-02T22:12:11)
    0000   0xcb 0x0c 0x36 0x02 0x0c                   ..6..
    body (0)

#### RECORD 10 CalBGForPH 2012-12-02T22:27:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2012-12-02T22:27:22)
    0000   0xd6 0x1b 0x36 0x02 0x0c                   ..6..
    body (0)

#### RECORD 11 BolusWizard 2012-12-02T22:41:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-02T22:41:48)
    0000   0xf0 0x29 0x16 0x02 0x0c                   .)...
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125
    HOUR BITS: [0, 0, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 77, 'amount': 3.1, 'curve': 4},
 {'age': 1, 'amount': 0.9, 'curve': 20},
 {'age': 161, 'amount': 0.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x7c 0x4d 0x04 0x24 0x01 0x14    \.|M.$..
    0008   0x0c 0xa1 0x14                             ...
    decimal
             92   11  124   77    4   36    1   20
             12  161   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2012-12-02T22:41:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-12-02T22:41:49)
    0000   0xf1 0x29 0x56 0x02 0x0c                   .)V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 ResultTotals 2012-12-02T13:12:02 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x06                   .....
    decimal
              7    0    0    6    6
    datetime (2012-12-02T13:12:02)
    0000   0xc2 0x0c 0x6d 0xc2 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb1 0x60 0x8b 0x09 0x00 0x00    ...`....
    0008   0x06 0x06 0x03 0x7c 0x3a 0x02 0x8a 0x2a    ...|:..*
    0010   0x00 0x64 0x02 0x8a 0x2a 0x01 0x2e 0x2e    .d..*...
    0018   0x01 0x5c 0x36 0x00 0x00 0x00 0x07 0x03    .\6.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  177   96  139    9    0    0
              6    6    3  124   58    2  138   42
              0  100    2  138   42    1   46   46
              1   92   54    0    0    0    7    3
              4    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2012-12-03T04:09:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2012-12-03T04:09:49)
    0000   0xf1 0x09 0x24 0x03 0x8c                   ..$..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 BolusWizard 2012-12-03T04:09:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 276,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x14                                  [.
    decimal
             91   20
    datetime (2012-12-03T04:09:59)
    0000   0xfb 0x09 0x04 0x03 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125

#### RECORD 17 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 1.5, 'curve': 20},
 {'age': 149, 'amount': 3.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x4f 0x14 0x7c 0x95 0x14    \.<O.|..
    decimal
             92    8   60   79   20  124  149   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2012-12-03T04:09:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-12-03T04:09:59)
    0000   0xfb 0x09 0x44 0x03 0x0c                   ..D..
    body (0)

#### RECORD 19 CalBGForPH 2012-12-03T05:07:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2012-12-03T05:07:32)
    0000   0xe0 0x07 0x25 0x03 0x0c                   ..%..
    body (0)

#### RECORD 20 PumpSuspend 2012-12-03T12:30:46 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-03T12:30:46)
    0000   0xee 0x1e 0x0c 0x03 0x0c                   .....
    body (0)

#### RECORD 21 PumpResume 2012-12-03T12:43:34 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-03T12:43:34)
    0000   0xe2 0x2b 0x0c 0x03 0x0c                   .+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 CalBGForPH 2012-12-03T13:40:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 77}
```
    op hex (2)
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2012-12-03T13:40:46)
    0000   0xee 0x28 0x2d 0x03 0x0c                   .(-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 23 BolusWizard 2012-12-03T13:41:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 77,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 52,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x4d                                  [M
    decimal
             91   77
    datetime (2012-12-03T13:41:18)
    0000   0xd2 0x29 0x0d 0x03 0x0c                   .)...
    body (13)
    hex
    0000   0x34 0x50 0x0d 0x2d 0x6a 0xf9 0x28 0xf0    4P.-j.(.
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
             52   80   13   45  106  249   40  240
              0    0    0   33  125
    HOUR BITS: [0, 0, 1]
#### RECORD 24 Bolus 2012-12-03T13:41:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'programmed': 3.3}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x02                        .!!.
    decimal
              1   33   33    2
    datetime (2012-12-03T13:41:19)
    0000   0xd3 0x29 0x6d 0x03 0x0c                   .)m..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 25 LowReservoir 2012-12-03T15:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-12-03T15:41:03)
    0000   0xc3 0x29 0x0f 0x03 0x0c                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 Rewind 2012-12-03T18:25:46 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-03T18:25:46)
    0000   0xee 0x19 0x12 0x03 0x0c                   .....
    body (0)

#### RECORD 27 Prime 2012-12-03T18:27:29 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x25                   ....%
    decimal
              3    0    0    0   37
    datetime (2012-12-03T18:27:29)
    0000   0xdd 0x1b 0x32 0x03 0x0c                   ..2..
    body (0)

#### RECORD 28 Prime 2012-12-03T18:27:50 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-03T18:27:50)
    0000   0xf2 0x1b 0x12 0x03 0x0c                   .....
    body (0)

#### RECORD 29 BolusWizard 2012-12-03T20:32:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 21,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-03T20:32:05)
    0000   0xc5 0x20 0x14 0x03 0x0c                   . ...
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             21   80   13   45  106    0   16    0
              0    0    0   16  125
    HOUR BITS: [0, 0, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 0.4, 'curve': 20},
 {'age': 112, 'amount': 0.55, 'curve': 20},
 {'age': 122, 'amount': 0.55, 'curve': 20},
 {'age': 132, 'amount': 0.55, 'curve': 20},
 {'age': 142, 'amount': 0.55, 'curve': 20},
 {'age': 152, 'amount': 0.55, 'curve': 20},
 {'age': 162, 'amount': 0.15, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x10 0x66 0x14 0x16 0x70 0x14    \..f..p.
    0008   0x16 0x7a 0x14 0x16 0x84 0x14 0x16 0x8e    .z......
    0010   0x14 0x16 0x98 0x14 0x06 0xa2 0x14         .......
    decimal
             92   23   16  102   20   22  112   20
             22  122   20   22  132   20   22  142
             20   22  152   20    6  162   20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-12-03T20:32:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'programmed': 1.6}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-12-03T20:32:05)
    0000   0xc5 0x20 0x54 0x03 0x0c                   . T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 32 BolusWizard 2012-12-03T20:47:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 22,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-03T20:47:01)
    0000   0xc1 0x2f 0x14 0x03 0x0c                   ./...
    body (13)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             22   80   13   45  106    0   16    0
              0    0    0   16  125
    HOUR BITS: [0, 0, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 1.6, 'curve': 4},
 {'age': 117, 'amount': 0.4, 'curve': 20},
 {'age': 127, 'amount': 0.55, 'curve': 20},
 {'age': 137, 'amount': 0.55, 'curve': 20},
 {'age': 147, 'amount': 0.55, 'curve': 20},
 {'age': 157, 'amount': 0.55, 'curve': 20},
 {'age': 167, 'amount': 0.55, 'curve': 20},
 {'age': 177, 'amount': 0.15, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x40 0x17 0x04 0x10 0x75 0x14    \.@...u.
    0008   0x16 0x7f 0x14 0x16 0x89 0x14 0x16 0x93    ........
    0010   0x14 0x16 0x9d 0x14 0x16 0xa7 0x14 0x06    ........
    0018   0xb1 0x14                                  ..
    decimal
             92   26   64   23    4   16  117   20
             22  127   20   22  137   20   22  147
             20   22  157   20   22  167   20    6
            177   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2012-12-03T20:47:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'programmed': 1.6}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-12-03T20:47:01)
    0000   0xc1 0x2f 0x54 0x03 0x0c                   ./T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 ResultTotals 2012-12-03T13:12:03 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime (2012-12-03T13:12:03)
    0000   0xc3 0x0c 0x6d 0xc3 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb7 0x4d 0x14 0x03 0x00 0x00    ...M....
    0008   0x05 0x0c 0x03 0x7c 0x45 0x01 0x90 0x1f    ...|E...
    0010   0x00 0x5f 0x01 0x90 0x1f 0x01 0x04 0x41    ._.....A
    0018   0x00 0x8c 0x23 0x00 0x00 0x00 0x04 0x03    ..#.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  183   77   20    3    0    0
              5   12    3  124   69    1  144   31
              0   95    1  144   31    1    4   65
              0  140   35    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 36 PumpSuspend 2012-12-04T11:17:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-04T11:17:38)
    0000   0xe6 0x11 0x0b 0x04 0x0c                   .....
    body (0)

#### RECORD 37 PumpResume 2012-12-04T11:17:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-04T11:17:55)
    0000   0xf7 0x11 0x0b 0x04 0x0c                   .....
    body (0)

#### RECORD 38 PumpSuspend 2012-12-04T11:57:13 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-04T11:57:13)
    0000   0xcd 0x39 0x0b 0x04 0x0c                   .9...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 PumpResume 2012-12-04T12:15:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-04T12:15:05)
    0000   0xc5 0x0f 0x0c 0x04 0x0c                   .....
    body (0)

#### RECORD 40 CalBGForPH 2012-12-04T12:50:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2012-12-04T12:50:19)
    0000   0xd3 0x32 0x2c 0x04 0x0c                   .2,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 BolusWizard 2012-12-04T12:50:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 174,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2012-12-04T12:50:24)
    0000   0xd8 0x32 0x0c 0x04 0x0c                   .2...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125
    HOUR BITS: [0, 0, 1]
#### RECORD 42 Bolus 2012-12-04T12:50:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2012-12-04T12:50:24)
    0000   0xd8 0x32 0x4c 0x04 0x0c                   .2L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 BolusWizard 2012-12-04T13:11:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-04T13:11:10)
    0000   0xca 0x0b 0x0d 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0x00 0x2b 0x00    9P.-j.+.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             57   80   13   45  106    0   43    0
              0    0    0   43  125

#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 1.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0x1b 0x04                   \.,..
    decimal
             92    5   44   27    4
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2012-12-04T13:11:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'programmed': 4.3}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2012-12-04T13:11:10)
    0000   0xca 0x0b 0x4d 0x04 0x0c                   ..M..
    body (0)

#### RECORD 46 BolusWizard 2012-12-04T13:49:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 14,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-04T13:49:20)
    0000   0xd4 0x31 0x0d 0x04 0x0c                   .1...
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [0, 0, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 0.1, 'curve': 4},
 {'age': 45, 'amount': 4.2, 'curve': 4},
 {'age': 65, 'amount': 1.1, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x04 0x23 0x04 0xa8 0x2d 0x04    \..#..-.
    0008   0x2c 0x41 0x04                             ,A.
    decimal
             92   11    4   35    4  168   45    4
             44   65    4
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2012-12-04T13:49:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-12-04T13:49:20)
    0000   0xd4 0x31 0x4d 0x04 0x0c                   .1M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 CalBGForPH 2012-12-04T18:47:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2012-12-04T18:47:14)
    0000   0xce 0x2f 0x32 0x04 0x0c                   ./2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 BolusWizard 2012-12-04T18:47:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 198,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xc6                                  [.
    decimal
             91  198
    datetime (2012-12-04T18:47:21)
    0000   0xd5 0x2f 0x12 0x04 0x0c                   ./...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125
    HOUR BITS: [0, 0, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 1.0, 'curve': 20},
 {'age': 77, 'amount': 0.1, 'curve': 20},
 {'age': 87, 'amount': 4.2, 'curve': 20},
 {'age': 107, 'amount': 1.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x2f 0x14 0x04 0x4d 0x14    \.(/..M.
    0008   0xa8 0x57 0x14 0x2c 0x6b 0x14              .W.,k.
    decimal
             92   14   40   47   20    4   77   20
            168   87   20   44  107   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2012-12-04T18:47:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-12-04T18:47:21)
    0000   0xd5 0x2f 0x52 0x04 0x0c                   ./R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 53 CalBGForPH 2012-12-04T20:32:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2012-12-04T20:32:32)
    0000   0xe0 0x20 0x34 0x04 0x0c                   . 4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 54 BolusWizard 2012-12-04T20:32:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.5,
 'carb_input': 72,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.1}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2012-12-04T20:32:54)
    0000   0xf6 0x20 0x14 0x04 0x0c                   . ...
    body (13)
    hex
    0000   0x48 0x50 0x0d 0x2d 0x6a 0x02 0x37 0x00    HP.-j.7.
    0008   0x00 0x0b 0x00 0x37 0x7d                   ...7}
    decimal
             72   80   13   45  106    2   55    0
              0   11    0   55  125
    HOUR BITS: [0, 0, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 1.9, 'curve': 4},
 {'age': 152, 'amount': 1.0, 'curve': 20},
 {'age': 182, 'amount': 0.1, 'curve': 20},
 {'age': 192, 'amount': 4.2, 'curve': 20},
 {'age': 212, 'amount': 1.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x4c 0x6c 0x04 0x28 0x98 0x14    \.Ll.(..
    0008   0x04 0xb6 0x14 0xa8 0xc0 0x14 0x2c 0xd4    ......,.
    0010   0x14                                       .
    decimal
             92   17   76  108    4   40  152   20
              4  182   20  168  192   20   44  212
             20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2012-12-04T20:32:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5, 'programmed': 5.5}
```
    op hex (4)
    0000   0x01 0x37 0x37 0x00                        .77.
    decimal
              1   55   55    0
    datetime (2012-12-04T20:32:54)
    0000   0xf6 0x20 0x54 0x04 0x0c                   . T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 ResultTotals 2012-12-04T13:12:04 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x9e                   .....
    decimal
              7    0    0    5  158
    datetime (2012-12-04T13:12:04)
    0000   0xc4 0x0c 0x6d 0xc4 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xaa 0x89 0xc6 0x03 0x00 0x00    ........
    0008   0x05 0x9e 0x03 0x76 0x3e 0x02 0x28 0x26    ...v>.(&
    0010   0x00 0x8f 0x02 0x28 0x26 0x01 0xb0 0x4e    ...(&..N
    0018   0x00 0x78 0x16 0x00 0x00 0x00 0x05 0x03    .x......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  170  137  198    3    0    0
              5  158    3  118   62    2   40   38
              0  143    2   40   38    1  176   78
              0  120   22    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 58 CalBGForPH 2012-12-05T00:08:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2012-12-05T00:08:18)
    0000   0xd2 0x08 0x20 0x05 0x0c                   .. ..
    body (0)

#### RECORD 59 CalBGForPH 2012-12-05T23:56:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2012-12-05T23:56:01)
    0000   0xc1 0x38 0x37 0x05 0x0c                   .87..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 BolusWizard 2012-12-05T23:56:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 52,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2012-12-05T23:56:51)
    0000   0xf3 0x38 0x17 0x05 0x0c                   .8...
    body (13)
    hex
    0000   0x34 0x50 0x0d 0x2d 0x6a 0xfa 0x28 0xf0    4P.-j.(.
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             52   80   13   45  106  250   40  240
              0    0    0   34  125
    HOUR BITS: [0, 0, 1]
#### RECORD 61 Bolus 2012-12-05T23:56:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-12-05T23:56:51)
    0000   0xf3 0x38 0x57 0x05 0x0c                   .8W..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 62 ResultTotals 2012-12-05T13:12:05 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x0c                   .....
    decimal
              7    0    0    4   12
    datetime (2012-12-05T13:12:05)
    0000   0xc5 0x0c 0x6d 0xc5 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x4a 0x43 0x50 0x02 0x00 0x00    ..JCP...
    0008   0x04 0x0c 0x03 0x84 0x57 0x00 0x88 0x0d    ....W...
    0010   0x00 0x34 0x00 0x88 0x0d 0x00 0x88 0x64    .4.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   74   67   80    2    0    0
              4   12    3  132   87    0  136   13
              0   52    0  136   13    0  136  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 63 CalBGForPH 2012-12-06T02:56:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2012-12-06T02:56:25)
    0000   0xd9 0x38 0x22 0x06 0x0c                   .8"..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 PumpSuspend 2012-12-06T10:47:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-06T10:47:49)
    0000   0xf1 0x2f 0x0a 0x06 0x0c                   ./...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 65 PumpResume 2012-12-06T11:04:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-06T11:04:29)
    0000   0xdd 0x04 0x0b 0x06 0x0c                   .....
    body (0)

#### RECORD 66 CalBGForPH 2012-12-06T11:28:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 274}
```
    op hex (2)
    0000   0x0a 0x12                                  ..
    decimal
             10   18
    datetime (2012-12-06T11:28:50)
    0000   0xf2 0x1c 0x2b 0x06 0x8c                   ..+..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 67 BolusWizard 2012-12-06T11:28:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 274,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x12                                  [.
    decimal
             91   18
    datetime (2012-12-06T11:28:53)
    0000   0xf5 0x1c 0x0b 0x06 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125

#### RECORD 68 Bolus 2012-12-06T11:28:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'programmed': 3.3}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2012-12-06T11:28:53)
    0000   0xf5 0x1c 0x4b 0x06 0x0c                   ..K..
    body (0)

#### RECORD 69 CalBGForPH 2012-12-06T12:49:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 168}
```
    op hex (2)
    0000   0x0a 0xa8                                  ..
    decimal
             10  168
    datetime (2012-12-06T12:49:41)
    0000   0xe9 0x31 0x2c 0x06 0x0c                   .1,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 CalBGForPH 2012-12-06T12:50:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2012-12-06T12:50:05)
    0000   0xc5 0x32 0x2c 0x06 0x0c                   .2,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 71 BolusWizard 2012-12-06T12:50:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.3}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2012-12-06T12:50:49)
    0000   0xf1 0x32 0x0c 0x06 0x0c                   .2...
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0x09 0x2c 0x00    :P.-j.,.
    0008   0x00 0x17 0x00 0x2c 0x7d                   ...,}
    decimal
             58   80   13   45  106    9   44    0
              0   23    0   44  125
    HOUR BITS: [0, 0, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 3.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x84 0x56 0x04                   \..V.
    decimal
             92    5  132   86    4
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2012-12-06T12:50:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'programmed': 4.4}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2012-12-06T12:50:49)
    0000   0xf1 0x32 0x4c 0x06 0x0c                   .2L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 74 CalBGForPH 2012-12-06T19:09:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-12-06T19:09:37)
    0000   0xe5 0x09 0x33 0x06 0x0c                   ..3..
    body (0)

#### RECORD 75 BolusWizard 2012-12-06T19:10:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2012-12-06T19:10:46)
    0000   0xee 0x0a 0x13 0x06 0x0c                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xfe 0x26 0xf0    2P.-j.&.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             50   80   13   45  106  254   38  240
              0    0    0   36  125

`end logs/ReadHistoryData-page-14.data: 76 records`
