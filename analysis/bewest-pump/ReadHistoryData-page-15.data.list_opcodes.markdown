## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc5 0x76                                  .v
##### DEBUG DECIMAL
            197  118
#### RECORD 0 BolusWizard 2012-11-28T15:02:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2012-11-28T15:02:26)
    0000   0x9a 0xc2 0x0f 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0xfc 0x0b 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             15   80   13   45  106  252   11  240
              0    0    0    7  125
    HOUR BITS: [1, 1, 0]
#### RECORD 1 Bolus 2012-11-28T15:02:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'programmed': 0.7}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2012-11-28T15:02:26)
    0000   0x9a 0xc2 0x4f 0x1c 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2012-11-28T15:41:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.2,
 'carb_input': 68,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-11-28T15:41:17)
    0000   0x91 0xe9 0x0f 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x44 0x50 0x0d 0x2d 0x6a 0x00 0x34 0x00    DP.-j.4.
    0008   0x00 0x00 0x00 0x34 0x7d                   ...4}
    decimal
             68   80   13   45  106    0   52    0
              0    0    0   52  125
    HOUR BITS: [1, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 0.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x1c 0x2f 0x04                   \../.
    decimal
             92    5   28   47    4
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2012-11-28T15:41:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2, 'programmed': 5.2}
```
    op hex (4)
    0000   0x01 0x34 0x34 0x00                        .44.
    decimal
              1   52   52    0
    datetime (2012-11-28T15:41:17)
    0000   0x91 0xe9 0x4f 0x1c 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 CalBGForPH 2012-11-28T21:28:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-11-28T21:28:10)
    0000   0x8a 0xdc 0x35 0x1c 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 BolusWizard 2012-11-28T21:28:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2012-11-28T21:28:16)
    0000   0x90 0xdc 0x15 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125
    HOUR BITS: [1, 1, 0]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 1.15, 'curve': 20},
 {'age': 98, 'amount': 4.05, 'curve': 20},
 {'age': 138, 'amount': 0.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2e 0x58 0x14 0xa2 0x62 0x14    \..X..b.
    0008   0x1c 0x8a 0x14                             ...
    decimal
             92   11   46   88   20  162   98   20
             28  138   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2012-11-28T21:28:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-11-28T21:28:16)
    0000   0x90 0xdc 0x55 0x1c 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 CalBGForPH 2012-11-28T23:45:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2012-11-28T23:45:14)
    0000   0x8e 0xed 0x37 0x1c 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 BolusWizard 2012-11-28T23:45:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 73,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0x49                                  [I
    decimal
             91   73
    datetime (2012-11-28T23:45:35)
    0000   0xa3 0xed 0x17 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0xf8 0x25 0xf0    1P.-j.%.
    0008   0x00 0x01 0x00 0x1d 0x7d                   ....}
    decimal
             49   80   13   45  106  248   37  240
              0    1    0   29  125
    HOUR BITS: [1, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 141, 'amount': 0.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x0c 0x8d 0x04                   \....
    decimal
             92    5   12  141    4
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2012-11-28T23:45:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-11-28T23:45:35)
    0000   0xa3 0xed 0x57 0x1c 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 ResultTotals (2012, 10, 28, 13, 12, 60) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe4                   .....
    decimal
              7    0    0    4  228
    datetime ((2012, 10, 28, 13, 12, 60))
    0000   0xbc 0x8c 0x6d 0xbc 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x74 0x49 0xba 0x03 0x00 0x00    ..tI....
    0008   0x04 0xe4 0x03 0x78 0x47 0x01 0x6c 0x1d    ...xG.l.
    0010   0x00 0x84 0x01 0x6c 0x1d 0x01 0x60 0x61    ...l..`a
    0018   0x00 0x0c 0x03 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  116   73  186    3    0    0
              4  228    3  120   71    1  108   29
              0  132    1  108   29    1   96   97
              0   12    3    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 14 LowReservoir 2012-11-29T10:49:05 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-11-29T10:49:05)
    0000   0x85 0xf1 0x0a 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 15 PumpSuspend 2012-11-29T10:53:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-29T10:53:09)
    0000   0x89 0xf5 0x0a 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 16 PumpResume 2012-11-29T11:08:26 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-29T11:08:26)
    0000   0x9a 0xc8 0x0b 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 CalBGForPH 2012-11-29T12:28:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 226}
```
    op hex (2)
    0000   0x0a 0xe2                                  ..
    decimal
             10  226
    datetime (2012-11-29T12:28:49)
    0000   0xb1 0xdc 0x2c 0x1d 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 BolusWizard 2012-11-29T12:28:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 226,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xe2                                  [.
    decimal
             91  226
    datetime (2012-11-29T12:28:58)
    0000   0xba 0xdc 0x0c 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    0    0   22  125
    HOUR BITS: [1, 1, 0]
#### RECORD 19 Bolus 2012-11-29T12:28:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'programmed': 2.2}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2012-11-29T12:28:58)
    0000   0xba 0xdc 0x4c 0x1d 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 BolusWizard 2012-11-29T12:38:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-11-29T12:38:19)
    0000   0x93 0xe6 0x0c 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x00 0x1e 0x00    (P.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             40   80   13   45  106    0   30    0
              0    0    0   30  125
    HOUR BITS: [1, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 2.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x0e 0x04                   \.X..
    decimal
             92    5   88   14    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2012-11-29T12:38:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'programmed': 3.0}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2012-11-29T12:38:19)
    0000   0x93 0xe6 0x4c 0x1d 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 23 LowReservoir 2012-11-29T15:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-11-29T15:41:03)
    0000   0x83 0xe9 0x0f 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 CalBGForPH 2012-11-29T20:25:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2012-11-29T20:25:37)
    0000   0xa5 0xd9 0x34 0x1d 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BolusWizard 2012-11-29T20:26:02 head[2], body[13] op[0x5b]
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
    datetime (2012-11-29T20:26:02)
    0000   0x82 0xda 0x14 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125
    HOUR BITS: [1, 1, 0]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 216, 'amount': 3.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0xd8 0x14                   \.x..
    decimal
             92    5  120  216   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2012-11-29T20:26:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-11-29T20:26:02)
    0000   0x82 0xda 0x54 0x1d 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 BolusWizard 2012-11-29T20:44:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-11-29T20:44:04)
    0000   0x84 0xec 0x14 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x00 0x18 0x00     P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
             32   80   13   45  106    0   24    0
              0    0    0   24  125
    HOUR BITS: [1, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 1.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0x14 0x04                   \.0..
    decimal
             92    5   48   20    4
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2012-11-29T20:44:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2012-11-29T20:44:04)
    0000   0x84 0xec 0x54 0x1d 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 ResultTotals (2012, 10, 29, 13, 12, 61) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd8                   .....
    decimal
              7    0    0    4  216
    datetime ((2012, 10, 29, 13, 12, 61))
    0000   0xbd 0x8c 0x6d 0xbd 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xd4 0xc6 0xe2 0x02 0x00 0x00    ........
    0008   0x04 0xd8 0x03 0x78 0x48 0x01 0x60 0x1c    ...xH.`.
    0010   0x00 0x48 0x01 0x60 0x1c 0x00 0xd8 0x3d    .H.`...=
    0018   0x00 0x88 0x27 0x00 0x00 0x00 0x04 0x02    ..'.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  212  198  226    2    0    0
              4  216    3  120   72    1   96   28
              0   72    1   96   28    0  216   61
              0  136   39    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 32 Rewind 2012-11-30T08:36:02 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-11-30T08:36:02)
    0000   0x82 0xe4 0x08 0x1e 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 Prime 2012-11-30T08:36:44 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x19                   .....
    decimal
              3    0    0    0   25
    datetime (2012-11-30T08:36:44)
    0000   0xac 0xe4 0x28 0x1e 0x0c                   ..(..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 Prime 2012-11-30T08:37:04 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-11-30T08:37:04)
    0000   0x84 0xe5 0x08 0x1e 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 PumpSuspend 2012-11-30T13:52:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-30T13:52:00)
    0000   0x80 0xf4 0x0d 0x1e 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 PumpResume 2012-11-30T15:00:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-30T15:00:03)
    0000   0x83 0xc0 0x0f 0x1e 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 CalBGForPH 2012-11-30T15:36:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2012-11-30T15:36:05)
    0000   0x85 0xe4 0x2f 0x1e 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 BolusWizard 2012-11-30T15:37:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 95,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2012-11-30T15:37:08)
    0000   0x88 0xe5 0x0f 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0xfd 0x22 0xf0    -P.-j.".
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             45   80   13   45  106  253   34  240
              0    0    0   31  125
    HOUR BITS: [1, 1, 1]
#### RECORD 39 Bolus 2012-11-30T15:37:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-11-30T15:37:08)
    0000   0x88 0xe5 0x4f 0x1e 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 BolusWizard 2012-11-30T16:11:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-11-30T16:11:02)
    0000   0x82 0xcb 0x10 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [1, 1, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 3.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x25 0x04                   \.|%.
    decimal
             92    5  124   37    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2012-11-30T16:11:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-11-30T16:11:02)
    0000   0x82 0xcb 0x50 0x1e 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 43 CalBGForPH 2012-11-30T17:55:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2012-11-30T17:55:51)
    0000   0xb3 0xf7 0x31 0x1e 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 CalBGForPH 2012-11-30T18:58:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2012-11-30T18:58:45)
    0000   0xad 0xfa 0x32 0x1e 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BolusWizard 2012-11-30T18:59:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 119,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 54,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.6}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2012-11-30T18:59:32)
    0000   0xa0 0xfb 0x12 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x36 0x50 0x0d 0x2d 0x6a 0x00 0x29 0x00    6P.-j.).
    0008   0x00 0x06 0x00 0x29 0x7d                   ...)}
    decimal
             54   80   13   45  106    0   41    0
              0    6    0   41  125
    HOUR BITS: [1, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 175, 'amount': 1.3, 'curve': 4},
 {'age': 205, 'amount': 3.1, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0xaf 0x04 0x7c 0xcd 0x04    \.4..|..
    decimal
             92    8   52  175    4  124  205    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-11-30T18:59:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'programmed': 4.1}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2012-11-30T18:59:32)
    0000   0xa0 0xfb 0x52 0x1e 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 ResultTotals (2012, 10, 30, 13, 12, 62) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xac                   .....
    decimal
              7    0    0    4  172
    datetime ((2012, 10, 30, 13, 12, 62))
    0000   0xbe 0x8c 0x6d 0xbe 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x76 0x5f 0x8d 0x03 0x00 0x00    ..v_....
    0008   0x04 0xac 0x03 0x58 0x48 0x01 0x54 0x1c    ...XH.T.
    0010   0x00 0x74 0x01 0x54 0x1c 0x01 0x54 0x64    .t.T..Td
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  118   95  141    3    0    0
              4  172    3   88   72    1   84   28
              0  116    1   84   28    1   84  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 CalBGForPH 2012-12-01T21:31:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2012-12-01T21:31:52)
    0000   0xf4 0x1f 0x35 0x01 0x0c                   ..5..
    body (0)

#### RECORD 50 BolusWizard 2012-12-01T21:32:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 114,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.4,
 'carb_input': 71,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2012-12-01T21:32:04)
    0000   0xc4 0x20 0x15 0x01 0x0c                   . ...
    body (13)
    hex
    0000   0x47 0x50 0x0d 0x2d 0x6a 0x00 0x36 0x00    GP.-j.6.
    0008   0x00 0x00 0x00 0x36 0x7d                   ...6}
    decimal
             71   80   13   45  106    0   54    0
              0    0    0   54  125
    HOUR BITS: [0, 0, 1]
#### RECORD 51 PumpSuspend 2012-12-01T21:32:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-01T21:32:29)
    0000   0xdd 0x20 0x15 0x01 0x0c                   . ...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 52 Bolus 2012-12-01T21:32:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4, 'programmed': 0.7}
```
    op hex (4)
    0000   0x01 0x36 0x07 0x00                        .6..
    decimal
              1   54    7    0
    datetime (2012-12-01T21:32:04)
    0000   0xc4 0x20 0x55 0x01 0x0c                   . U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 53 PumpResume 2012-12-01T21:32:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-01T21:32:31)
    0000   0xdf 0x20 0x15 0x01 0x0c                   . ...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 54 CalBGForPH 2012-12-01T21:32:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2012-12-01T21:32:40)
    0000   0xe8 0x20 0x35 0x01 0x0c                   . 5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 BolusWizard 2012-12-01T21:33:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 114,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 7.6,
 'carb_input': 100,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.7}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2012-12-01T21:33:58)
    0000   0xfa 0x21 0x15 0x01 0x0c                   .!...
    body (13)
    hex
    0000   0x64 0x50 0x0d 0x2d 0x6a 0x00 0x4c 0x00    dP.-j.L.
    0008   0x00 0x07 0x00 0x4c 0x7d                   ...L}
    decimal
            100   80   13   45  106    0   76    0
              0    7    0   76  125
    HOUR BITS: [0, 0, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 0.65, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x1a 0x09 0x04                   \....
    decimal
             92    5   26    9    4
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2012-12-01T21:33:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'programmed': 4.3}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2012-12-01T21:33:58)
    0000   0xfa 0x21 0x95 0x01 0x0c                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 ResultTotals 2012-12-01T13:12:01 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd8                   .....
    decimal
              7    0    0    4  216
    datetime (2012-12-01T13:12:01)
    0000   0xc1 0x0c 0x6d 0xc1 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x72 0x72 0x72 0x02 0x00 0x00    ..rrr...
    0008   0x04 0xd8 0x03 0x84 0x49 0x01 0x54 0x1b    ....I.T.
    0010   0x00 0xab 0x01 0x54 0x1b 0x01 0x46 0x60    ...T..F`
    0018   0x00 0x0e 0x04 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  114  114  114    2    0    0
              4  216    3  132   73    1   84   27
              0  171    1   84   27    1   70   96
              0   14    4    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 59 Bolus 2012-12-01T21:36:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'programmed': 3.7}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x05                        .%%.
    decimal
              1   37   37    5
    datetime (2012-12-01T21:36:51)
    0000   0xf3 0x24 0xb5 0x01 0x0c                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 CalBGForPH 2012-12-02T02:04:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 212}
```
    op hex (2)
    0000   0x0a 0xd4                                  ..
    decimal
             10  212
    datetime (2012-12-02T02:04:59)
    0000   0xfb 0x04 0x22 0x02 0x0c                   .."..
    body (0)

#### RECORD 61 BolusWizard 2012-12-02T02:05:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 212,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.6}
```
    op hex (2)
    0000   0x5b 0xd4                                  [.
    decimal
             91  212
    datetime (2012-12-02T02:05:20)
    0000   0xd4 0x05 0x02 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x13 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   19    0    0
              0    6    0   13  125

#### RECORD 62 UnabsorbedInsulinBolus unknown head[53], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 0.05, 'curve': 4},
 {'age': 131, 'amount': 0.25, 'curve': 4},
 {'age': 141, 'amount': 0.25, 'curve': 4},
 {'age': 151, 'amount': 0.25, 'curve': 4},
 {'age': 161, 'amount': 0.25, 'curve': 4},
 {'age': 171, 'amount': 0.25, 'curve': 4},
 {'age': 181, 'amount': 0.25, 'curve': 4},
 {'age': 191, 'amount': 0.25, 'curve': 4},
 {'age': 201, 'amount': 0.25, 'curve': 4},
 {'age': 211, 'amount': 0.25, 'curve': 4},
 {'age': 221, 'amount': 0.25, 'curve': 4},
 {'age': 231, 'amount': 0.25, 'curve': 4},
 {'age': 241, 'amount': 0.25, 'curve': 4},
 {'age': 251, 'amount': 0.25, 'curve': 4},
 {'age': 5, 'amount': 0.2, 'curve': 20},
 {'age': 15, 'amount': 4.45, 'curve': 20},
 {'age': 25, 'amount': 0.7, 'curve': 20}]
```
    op hex (53)
    0000   0x5c 0x35 0x02 0x79 0x04 0x0a 0x83 0x04    \5.y....
    0008   0x0a 0x8d 0x04 0x0a 0x97 0x04 0x0a 0xa1    ........
    0010   0x04 0x0a 0xab 0x04 0x0a 0xb5 0x04 0x0a    ........
    0018   0xbf 0x04 0x0a 0xc9 0x04 0x0a 0xd3 0x04    ........
    0020   0x0a 0xdd 0x04 0x0a 0xe7 0x04 0x0a 0xf1    ........
    0028   0x04 0x0a 0xfb 0x04 0x08 0x05 0x14 0xb2    ........
    0030   0x0f 0x14 0x1c 0x19 0x14                   .....
    decimal
             92   53    2  121    4   10  131    4
             10  141    4   10  151    4   10  161
              4   10  171    4   10  181    4   10
            191    4   10  201    4   10  211    4
             10  221    4   10  231    4   10  241
              4   10  251    4    8    5   20  178
             15   20   28   25   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2012-12-02T02:05:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-12-02T02:05:20)
    0000   0xd4 0x05 0x42 0x02 0x0c                   ..B..
    body (0)

#### RECORD 64 CalBGForPH 2012-12-02T09:35:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 395}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2012-12-02T09:35:43)
    0000   0xeb 0x23 0x29 0x02 0x8c                   .#)..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 65 BolusWizard 2012-12-02T09:35:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 395,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x8b                                  [.
    decimal
             91  139
    datetime (2012-12-02T09:35:51)
    0000   0xf3 0x23 0x09 0x02 0x0c                   .#...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3c 0x00 0x00    .Q.-j<..
    0008   0x00 0x00 0x00 0x3c 0x7d                   ...<}
    decimal
              0   81   13   45  106   60    0    0
              0    0    0   60  125
    HOUR BITS: [0, 0, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 195, 'amount': 1.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0xc3 0x14                   \.<..
    decimal
             92    5   60  195   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2012-12-02T09:35:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0, 'programmed': 6.0}
```
    op hex (4)
    0000   0x01 0x3c 0x3c 0x00                        .<<.
    decimal
              1   60   60    0
    datetime (2012-12-02T09:35:51)
    0000   0xf3 0x23 0x49 0x02 0x0c                   .#I..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 68 PumpSuspend 2012-12-02T09:40:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-02T09:40:01)
    0000   0xc1 0x28 0x09 0x02 0x0c                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 PumpResume 2012-12-02T09:49:47 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-02T09:49:47)
    0000   0xef 0x31 0x09 0x02 0x0c                   .1...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 CalBGForPH 2012-12-02T12:12:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-02T12:12:16)
    0000   0xd0 0x0c 0x2c 0x02 0x0c                   ..,..
    body (0)

#### RECORD 71 BolusWizard 2012-12-02T12:13:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.6}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2012-12-02T12:13:27)
    0000   0xdb 0x0d 0x0c 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x0d 0x1c 0x00    %P.-j...
    0008   0x00 0x10 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106   13   28    0
              0   16    0   28  125

#### RECORD 72 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 159, 'amount': 6.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xf0 0x9f 0x04                   \....
    decimal
             92    5  240  159    4
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2012-12-02T12:13:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'programmed': 2.8}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2012-12-02T12:13:27)
    0000   0xdb 0x0d 0x4c 0x02 0x0c                   ..L..
    body (0)

#### RECORD 74 CalBGForPH 2012-12-02T14:14:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2012-12-02T14:14:22)
    0000   0xd6 0x0e 0x2e 0x02 0x0c                   .....
    body (0)

#### RECORD 75 CalBGForPH 2012-12-02T15:50:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2012-12-02T15:50:18)
    0000   0xd2 0x32 0x2f 0x02 0x0c                   .2/..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 76 BolusWizard 2012-12-02T15:50:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 172,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2012-12-02T15:50:27)
    0000   0xdb 0x32 0x0f 0x02 0x0c                   .2...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x07 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    3    0    7  125
    HOUR BITS: [0, 0, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 216, 'amount': 2.0, 'curve': 4},
 {'age': 226, 'amount': 0.8, 'curve': 4},
 {'age': 120, 'amount': 6.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0xd8 0x04 0x20 0xe2 0x04    \.P.. ..
    0008   0xf0 0x78 0x14                             .x.
    decimal
             92   11   80  216    4   32  226    4
            240  120   20
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-15.data: 78 records`
