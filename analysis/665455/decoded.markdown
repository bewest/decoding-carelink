## START bewest-ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 496, found 526 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xd7 0x52                                  .R
##### DEBUG DECIMAL
            215   82
#### RECORD 0 CalBGForPH 2014-07-01T03:36:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 284}
```
    op hex (2)
    0000   0x0a 0x1c                                  ..
    decimal
             10   28
    datetime (2014-07-01T03:36:43)
    0000   0x6b 0xe4 0x23 0x61 0x8e                   k.#a.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 Ian3F 2014-07-01T03:36:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2014-07-01T03:36:43)
    0000   0x6b 0xe4 0x83 0x61 0x0e                   k..a.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2014-07-01T03:37:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 35,
 '_byte[7]': 0,
 'bg': 284,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x1c                                  [.
    decimal
             91   28
    datetime (2014-07-01T03:37:00)
    0000   0x40 0xe5 0x03 0x01 0x0e                   @....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00 0x00    .Q.-j#..
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
              0   81   13   45  106   35    0    0
              0    0    0   35  125
    HOUR BITS: [1, 1, 1]
#### RECORD 3 Bolus 2014-07-01T03:37:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'duration': 0, 'programmed': 3.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2014-07-01T03:37:00)
    0000   0x40 0xe5 0x43 0x01 0x0e                   @.C..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 BolusWizard 2014-07-01T21:58:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-01T21:58:28)
    0000   0x5c 0xfa 0x15 0x01 0x0e                   \....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [1, 1, 1]
#### RECORD 5 Bolus 2014-07-01T21:58:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 0, 'programmed': 2.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2014-07-01T21:58:28)
    0000   0x5c 0xfa 0x55 0x01 0x0e                   \.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 BolusWizard 2014-07-01T23:40:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-01T23:40:15)
    0000   0x4f 0xe8 0x17 0x01 0x0e                   O....
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    =P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             61   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [1, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 106, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x6a 0x04                   \.Pj.
    decimal
             92    5   80  106    4
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2014-07-01T23:40:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'duration': 0, 'programmed': 4.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2014-07-01T23:40:15)
    0000   0x4f 0xe8 0x57 0x01 0x0e                   O.W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 MResultTotals 2014-07-02T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x16                   .....
    decimal
              7    0    0    5   22
    datetime (2014-07-02T00:00:00)
    0000   0x61 0x8e                                  a.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 Model522ResultTotals 2014-07-02T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-02T00:00:00)
    0000   0x61 0x8e                                  a.
    body (41)
    hex
    0000   0x05 0x15 0x1c 0x1c 0x1c 0x01 0x00 0x00    ........
    0008   0x05 0x16 0x03 0x82 0x45 0x01 0x94 0x1f    ....E...
    0010   0x00 0x58 0x01 0x94 0x1f 0x01 0x08 0x41    .X.....A
    0018   0x00 0x8c 0x23 0x00 0x00 0x00 0x03 0x02    ..#.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21   28   28   28    1    0    0
              5   22    3  130   69    1  148   31
              0   88    1  148   31    1    8   65
              0  140   35    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 11 BolusWizard 2014-07-02T00:40:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 21,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-02T00:40:09)
    0000   0x49 0xe8 0x00 0x02 0x0e                   I....
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             21   80   13   45  106    0   16    0
              0    0    0   16  125
    HOUR BITS: [1, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 4.6, 'curve': 4},
 {'age': 166, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb8 0x42 0x04 0x50 0xa6 0x04    \..B.P..
    decimal
             92    8  184   66    4   80  166    4
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2014-07-02T00:40:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'duration': 0, 'programmed': 1.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2014-07-02T00:40:09)
    0000   0x49 0xe8 0x40 0x02 0x0e                   I.@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 BolusWizard 2014-07-02T00:55:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-02T00:55:26)
    0000   0x5a 0xf7 0x00 0x02 0x0e                   Z....
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    #P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             35   80   13   45  106    0   26    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 1.6, 'curve': 4},
 {'age': 81, 'amount': 4.6, 'curve': 4},
 {'age': 181, 'amount': 2.0, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x15 0x04 0xb8 0x51 0x04    \.@...Q.
    0008   0x50 0xb5 0x04                             P..
    decimal
             92   11   64   21    4  184   81    4
             80  181    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2014-07-02T00:55:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2014-07-02T00:55:26)
    0000   0x5a 0xf7 0x40 0x02 0x0e                   Z.@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 CalBGForPH 2014-07-02T23:06:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2014-07-02T23:06:33)
    0000   0x61 0xc6 0x37 0x02 0x0e                   a.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 BolusWizard 2014-07-02T23:07:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-02T23:07:20)
    0000   0x54 0xc7 0x17 0x02 0x0e                   T....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    <P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [1, 1, 0]
#### RECORD 19 Bolus 2014-07-02T23:07:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'duration': 0, 'programmed': 4.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2014-07-02T23:07:20)
    0000   0x54 0xc7 0x57 0x02 0x0e                   T.W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 MResultTotals 2014-07-03T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe4                   .....
    decimal
              7    0    0    4  228
    datetime (2014-07-03T00:00:00)
    0000   0x62 0x8e                                  b.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 Model522ResultTotals 2014-07-03T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-03T00:00:00)
    0000   0x62 0x8e                                  b.
    body (41)
    hex
    0000   0x05 0x00 0x69 0x69 0x69 0x01 0x00 0x00    ..iii...
    0008   0x04 0xe4 0x03 0x84 0x48 0x01 0x60 0x1c    ....H.`.
    0010   0x00 0x74 0x01 0x60 0x1c 0x01 0x60 0x64    .t.`..`d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  105  105  105    1    0    0
              4  228    3  132   72    1   96   28
              0  116    1   96   28    1   96  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 22 BolusWizard 2014-07-03T01:36:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-03T01:36:58)
    0000   0x7a 0xe4 0x01 0x03 0x0e                   z....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x00 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             45   80   13   45  106    0   34    0
              0    0    0   34  125
    HOUR BITS: [1, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 4.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb8 0x98 0x04                   \....
    decimal
             92    5  184  152    4
    datetime (unknown)

    body (0)

#### RECORD 24 PumpSuspend 2014-07-03T01:37:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-07-03T01:37:17)
    0000   0x51 0xe5 0x01 0x03 0x0e                   Q....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 Bolus 2014-07-03T01:36:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x05 0x00                        ."..
    decimal
              1   34    5    0
    datetime (2014-07-03T01:36:58)
    0000   0x7a 0xe4 0x41 0x03 0x0e                   z.A..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 PumpResume 2014-07-03T01:37:19 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-07-03T01:37:19)
    0000   0x53 0xe5 0x01 0x03 0x0e                   S....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 27 BolusWizard 2014-07-03T01:37:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-03T01:37:31)
    0000   0x5f 0xe5 0x01 0x03 0x0e                   _....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [1, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 0.5, 'curve': 4},
 {'age': 153, 'amount': 4.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x03 0x04 0xb8 0x99 0x04    \.......
    decimal
             92    8   20    3    4  184  153    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2014-07-03T01:37:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'duration': 0, 'programmed': 2.3, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2014-07-03T01:37:32)
    0000   0x60 0xe5 0x41 0x03 0x0e                   `.A..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 CalBGForPH 2014-07-03T09:20:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 273}
```
    op hex (2)
    0000   0x0a 0x11                                  ..
    decimal
             10   17
    datetime (2014-07-03T09:20:05)
    0000   0x45 0xd4 0x29 0x63 0x8e                   E.)c.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 31 Ian3F 2014-07-03T09:20:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x22                                  ?"
    decimal
             63   34
    datetime (2014-07-03T09:20:05)
    0000   0x45 0xd4 0x29 0x63 0x0e                   E.)c.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2014-07-03T09:20:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 273,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x11                                  [.
    decimal
             91   17
    datetime (2014-07-03T09:20:16)
    0000   0x50 0xd4 0x09 0x03 0x0e                   P....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
              0   81   13   45  106   32    0    0
              0    0    0   32  125
    HOUR BITS: [1, 1, 0]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 210, 'amount': 2.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0xd2 0x14                   \.p..
    decimal
             92    5  112  210   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2014-07-03T09:20:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2014-07-03T09:20:17)
    0000   0x51 0xd4 0x49 0x03 0x0e                   Q.I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 35 BolusWizard 2014-07-03T16:43:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-03T16:43:15)
    0000   0x4f 0xeb 0x10 0x03 0x0e                   O....
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    "P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             34   80   13   45  106    0   26    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 3.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x88 0xc1 0x14                   \....
    decimal
             92    5  136  193   20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2014-07-03T16:43:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2014-07-03T16:43:15)
    0000   0x4f 0xeb 0x50 0x03 0x0e                   O.P..
    body (0)
    HOUR BITS: [1, 1, 1]
`end bewest-ReadHistoryData-page-0.data: 38 records`
