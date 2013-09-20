## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-22.data
#### RECORD 0 CalBGForPH 2013-04-29T15:31:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-04-29T15:31:22)
    0000   0x56 0x1f 0x2f 0x1d 0x0d                   V./..
    body (0)

#### RECORD 1 BolusWizard 2013-04-29T15:31:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 194,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc2                                  [.
    decimal
             91  194
    datetime (2013-04-29T15:31:33)
    0000   0x61 0x1f 0x0f 0x1d 0x0d                   a....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x0f 0x1e 0x00    (P.-j...
    0008   0x00 0x11 0x00 0x1e 0x7d                   ....}
    decimal
             40   80   13   45  106   15   30    0
              0   17    0   30  125

#### RECORD 2 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 0.6, 'curve': 4},
 {'age': 107, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0x07 0x04 0x50 0x6b 0x04    \....Pk.
    decimal
             92    8   24    7    4   80  107    4
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2013-04-29T15:31:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-04-29T15:31:33)
    0000   0x61 0x1f 0x4f 0x1d 0x0d                   a.O..
    body (0)

#### RECORD 4 BolusWizard 2013-04-29T16:11:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
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
    datetime (2013-04-29T16:11:27)
    0000   0x5b 0x0b 0x10 0x1d 0x0d                   [....
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0    0    0   13  125

#### RECORD 5 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 3.6, 'curve': 4},
 {'age': 147, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x90 0x2f 0x04 0x50 0x93 0x04    \../.P..
    decimal
             92    8  144   47    4   80  147    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-04-29T16:11:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-04-29T16:11:27)
    0000   0x5b 0x0b 0x50 0x1d 0x0d                   [.P..
    body (0)

#### RECORD 7 CalBGForPH 2013-04-29T17:27:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 272}
```
    op hex (2)
    0000   0x0a 0x10                                  ..
    decimal
             10   16
    datetime (2013-04-29T17:27:03)
    0000   0x43 0x1b 0x31 0x1d 0x8d                   C.1..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 BolusWizard 2013-04-29T17:27:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 272,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x10                                  [.
    decimal
             91   16
    datetime (2013-04-29T17:27:17)
    0000   0x51 0x1b 0x11 0x1d 0x0d                   Q....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x1b 0x00 0x05 0x7d                   ....}
    decimal
              0   81   13   45  106   32    0    0
              0   27    0    5  125

#### RECORD 9 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 83, 'amount': 1.3, 'curve': 4},
 {'age': 123, 'amount': 3.6, 'curve': 4},
 {'age': 223, 'amount': 2.0, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x53 0x04 0x90 0x7b 0x04    \.4S..{.
    0008   0x50 0xdf 0x04                             P..
    decimal
             92   11   52   83    4  144  123    4
             80  223    4
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-04-29T17:27:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-04-29T17:27:17)
    0000   0x51 0x1b 0x51 0x1d 0x0d                   Q.Q..
    body (0)

#### RECORD 11 CalBGForPH 2013-04-29T18:29:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 239}
```
    op hex (2)
    0000   0x0a 0xef                                  ..
    decimal
             10  239
    datetime (2013-04-29T18:29:45)
    0000   0x6d 0x1d 0x32 0x1d 0x0d                   m.2..
    body (0)

#### RECORD 12 BolusWizard 2013-04-29T18:29:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 25,
 '_byte[7]': 0,
 'bg': 239,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xef                                  [.
    decimal
             91  239
    datetime (2013-04-29T18:29:51)
    0000   0x73 0x1d 0x12 0x1d 0x0d                   s....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x19 0x00 0x00    .P.-j...
    0008   0x00 0x10 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106   25    0    0
              0   16    0    9  125

#### RECORD 13 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 0.7, 'curve': 4},
 {'age': 145, 'amount': 1.3, 'curve': 4},
 {'age': 185, 'amount': 3.6, 'curve': 4},
 {'age': 29, 'amount': 2.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1c 0x41 0x04 0x34 0x91 0x04    \..A.4..
    0008   0x90 0xb9 0x04 0x50 0x1d 0x14              ...P..
    decimal
             92   14   28   65    4   52  145    4
            144  185    4   80   29   20
    datetime (unknown)

    body (0)

#### RECORD 14 LowReservoir 2013-04-29T18:30:09 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-04-29T18:30:09)
    0000   0x49 0x1e 0x12 0x1d 0x0d                   I....
    body (0)

#### RECORD 15 Bolus 2013-04-29T18:29:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-04-29T18:29:51)
    0000   0x73 0x1d 0x52 0x1d 0x0d                   s.R..
    body (0)

#### RECORD 16 CalBGForPH 2013-04-29T18:51:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 232}
```
    op hex (2)
    0000   0x0a 0xe8                                  ..
    decimal
             10  232
    datetime (2013-04-29T18:51:50)
    0000   0x72 0x33 0x32 0x1d 0x0d                   r32..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 BolusWizard 2013-04-29T18:51:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 232,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe8                                  [.
    decimal
             91  232
    datetime (2013-04-29T18:51:55)
    0000   0x77 0x33 0x12 0x1d 0x0d                   w3...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x17 0x00 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106   23    0    0
              0   22    0    1  125
    HOUR BITS: [0, 0, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 1.1, 'curve': 4},
 {'age': 87, 'amount': 0.7, 'curve': 4},
 {'age': 167, 'amount': 1.3, 'curve': 4},
 {'age': 207, 'amount': 3.6, 'curve': 4},
 {'age': 51, 'amount': 2.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x2c 0x1b 0x04 0x1c 0x57 0x04    \.,...W.
    0008   0x34 0xa7 0x04 0x90 0xcf 0x04 0x50 0x33    4.....P3
    0010   0x14                                       .
    decimal
             92   17   44   27    4   28   87    4
             52  167    4  144  207    4   80   51
             20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-04-29T18:51:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-04-29T18:51:55)
    0000   0x77 0x33 0x52 0x1d 0x0d                   w3R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 CalBGForPH 2013-04-29T20:31:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 225}
```
    op hex (2)
    0000   0x0a 0xe1                                  ..
    decimal
             10  225
    datetime (2013-04-29T20:31:06)
    0000   0x46 0x1f 0x34 0x1d 0x0d                   F.4..
    body (0)

#### RECORD 21 BolusWizard 2013-04-29T20:31:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 225,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe1                                  [.
    decimal
             91  225
    datetime (2013-04-29T20:31:14)
    0000   0x4e 0x1f 0x14 0x1d 0x0d                   N....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    7    0   15  125

#### RECORD 22 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 107, 'amount': 0.2, 'curve': 4},
 {'age': 127, 'amount': 1.1, 'curve': 4},
 {'age': 187, 'amount': 0.7, 'curve': 4},
 {'age': 11, 'amount': 1.3, 'curve': 20},
 {'age': 51, 'amount': 3.6, 'curve': 20},
 {'age': 151, 'amount': 2.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x08 0x6b 0x04 0x2c 0x7f 0x04    \..k.,..
    0008   0x1c 0xbb 0x04 0x34 0x0b 0x14 0x90 0x33    ...4...3
    0010   0x14 0x50 0x97 0x14                        .P..
    decimal
             92   20    8  107    4   44  127    4
             28  187    4   52   11   20  144   51
             20   80  151   20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-04-29T20:31:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-04-29T20:31:14)
    0000   0x4e 0x1f 0x54 0x1d 0x0d                   N.T..
    body (0)

#### RECORD 24 BolusWizard 2013-04-29T20:51:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
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
    datetime (2013-04-29T20:51:19)
    0000   0x53 0x33 0x14 0x1d 0x0d                   S3...
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             47   80   13   45  106    0   36    0
              0    0    0   36  125
    HOUR BITS: [0, 0, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 1.7, 'curve': 4},
 {'age': 127, 'amount': 0.2, 'curve': 4},
 {'age': 147, 'amount': 1.1, 'curve': 4},
 {'age': 207, 'amount': 0.7, 'curve': 4},
 {'age': 31, 'amount': 1.3, 'curve': 20},
 {'age': 71, 'amount': 3.6, 'curve': 20},
 {'age': 171, 'amount': 2.0, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x44 0x1b 0x04 0x08 0x7f 0x04    \.D.....
    0008   0x2c 0x93 0x04 0x1c 0xcf 0x04 0x34 0x1f    ,.....4.
    0010   0x14 0x90 0x47 0x14 0x50 0xab 0x14         ..G.P..
    decimal
             92   23   68   27    4    8  127    4
             44  147    4   28  207    4   52   31
             20  144   71   20   80  171   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-04-29T20:51:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-04-29T20:51:20)
    0000   0x54 0x33 0x54 0x1d 0x0d                   T3T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 27 Rewind 2013-04-29T23:31:24 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-04-29T23:31:24)
    0000   0x58 0x1f 0x17 0x1d 0x0d                   X....
    body (0)

#### RECORD 28 Prime 2013-04-29T23:32:00 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x24                   ....$
    decimal
              3    0    0    0   36
    datetime (2013-04-29T23:32:00)
    0000   0x40 0x20 0x37 0x1d 0x0d                   @ 7..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 29 Prime 2013-04-29T23:32:27 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-29T23:32:27)
    0000   0x5b 0x20 0x17 0x1d 0x0d                   [ ...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 MResultTotals 2013-04-30T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-04-30T00:00:00)
    0000   0x00 0x05 0x0e 0x5d 0x0d                   ...].
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 31 Model522ResultTotals 2013-04-30T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-30T00:00:00)
    0000   0x5d 0x0d                                  ].
    body (41)
    hex
    0000   0x05 0x10 0xd2 0x67 0x10 0x08 0x00 0x00    ...g....
    0008   0x05 0x0e 0x02 0xd6 0x38 0x02 0x38 0x2c    ....8.8,
    0010   0x00 0x68 0x02 0x38 0x2c 0x01 0x3c 0x38    .h.8,.<8
    0018   0x00 0xfc 0x2c 0x00 0x00 0x00 0x09 0x03    ..,.....
    0020   0x06 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  210  103   16    8    0    0
              5   14    2  214   56    2   56   44
              0  104    2   56   44    1   60   56
              0  252   44    0    0    0    9    3
              6    0    0   12    0  232    0    0
              0

#### RECORD 32 CalBGForPH 2013-04-30T02:08:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 277}
```
    op hex (2)
    0000   0x0a 0x15                                  ..
    decimal
             10   21
    datetime (2013-04-30T02:08:46)
    0000   0x6e 0x08 0x22 0x1e 0x8d                   n."..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 BolusWizard 2013-04-30T02:08:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 277,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x15                                  [.
    decimal
             91   21
    datetime (2013-04-30T02:08:48)
    0000   0x70 0x08 0x02 0x1e 0x0d                   p....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125

#### RECORD 34 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 3.6, 'curve': 20},
 {'age': 88, 'amount': 1.7, 'curve': 20},
 {'age': 188, 'amount': 0.2, 'curve': 20},
 {'age': 208, 'amount': 1.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x90 0x44 0x14 0x44 0x58 0x14    \..D.DX.
    0008   0x08 0xbc 0x14 0x2c 0xd0 0x14              ...,..
    decimal
             92   14  144   68   20   68   88   20
              8  188   20   44  208   20
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-04-30T02:08:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-04-30T02:08:48)
    0000   0x70 0x08 0x42 0x1e 0x0d                   p.B..
    body (0)

#### RECORD 36 CalBGForPH 2013-04-30T08:36:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 242}
```
    op hex (2)
    0000   0x0a 0xf2                                  ..
    decimal
             10  242
    datetime (2013-04-30T08:36:22)
    0000   0x56 0x24 0x28 0x1e 0x0d                   V$(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 BolusWizard 2013-04-30T08:36:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 242,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf2                                  [.
    decimal
             91  242
    datetime (2013-04-30T08:36:24)
    0000   0x58 0x24 0x08 0x1e 0x0d                   X$...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0    0    0   26  125
    HOUR BITS: [0, 0, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 136, 'amount': 3.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x84 0x88 0x14                   \....
    decimal
             92    5  132  136   20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-04-30T08:36:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-04-30T08:36:25)
    0000   0x59 0x24 0x48 0x1e 0x0d                   Y$H..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 PumpSuspend 2013-04-30T13:49:47 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-30T13:49:47)
    0000   0x6f 0x31 0x0d 0x1e 0x0d                   o1...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 PumpResume 2013-04-30T14:07:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-30T14:07:46)
    0000   0x6e 0x07 0x0e 0x1e 0x0d                   n....
    body (0)

#### RECORD 42 CalBGForPH 2013-04-30T15:28:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-04-30T15:28:06)
    0000   0x46 0x1c 0x2f 0x1e 0x0d                   F./..
    body (0)

#### RECORD 43 BolusWizard 2013-04-30T15:28:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-04-30T15:28:29)
    0000   0x5d 0x1c 0x0f 0x1e 0x0d                   ]....
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0x00 0x28 0x00    5P.-j.(.
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
             53   80   13   45  106    0   40    0
              0    0    0   40  125

#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 158, 'amount': 2.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0x9e 0x14                   \.h..
    decimal
             92    5  104  158   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-04-30T15:28:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-04-30T15:28:29)
    0000   0x5d 0x1c 0x4f 0x1e 0x0d                   ].O..
    body (0)

#### RECORD 46 CalBGForPH unknown head[2], body[0] op[0x0a]

    op hex (2)
    0000   0x0a 0xcb                                  ..
    decimal
             10  203
    datetime (unknown)

    body (0)

`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-22.data: 47 records`
