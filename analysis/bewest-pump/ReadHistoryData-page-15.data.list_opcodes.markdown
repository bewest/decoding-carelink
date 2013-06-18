## START logs/ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x8c 0x43                                  .C
##### DEBUG DECIMAL
            140   67
#### RECORD 0 BolusWizard 2013-04-17T17:42:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2013-04-17T17:42:13)
    0000   0x4d 0x2a 0x11 0x11 0x0d                   M*...
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x01 0x14 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    1   20    0
              0    3    0   20  125
    HOUR BITS: [0, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 228, 'amount': 4.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0xe4 0x04                   \....
    decimal
             92    5  168  228    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-04-17T17:42:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-04-17T17:42:13)
    0000   0x4d 0x2a 0x51 0x11 0x0d                   M*Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 TempBasal 2013-04-17T21:09:01 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.6}
```
    op hex (2)
    0000   0x33 0x18                                  3.
    decimal
             51   24
    datetime (2013-04-17T21:09:01)
    0000   0x41 0x09 0x15 0x11 0x0d                   A....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0

#### RECORD 4 TempBasalDuration 2013-04-17T21:09:01 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2013-04-17T21:09:01)
    0000   0x41 0x09 0x15 0x11 0x0d                   A....
    body (0)

#### RECORD 5 CalBGForPH 2013-04-17T23:16:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-04-17T23:16:10)
    0000   0x4a 0x10 0x37 0x11 0x0d                   J.7..
    body (0)

#### RECORD 6 BolusWizard 2013-04-17T23:16:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 2.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-04-17T23:16:40)
    0000   0x68 0x10 0x17 0x11 0x0d                   h....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0xfd 0x1d 0xf0    &P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             38   80   13   45  106  253   29  240
              0    0    0   26  125

#### RECORD 7 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 2.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x56 0x14                   \.PV.
    decimal
             92    5   80   86   20
    datetime (unknown)

    body (0)

#### RECORD 8 LowReservoir 2013-04-17T23:16:40 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-04-17T23:16:40)
    0000   0x68 0x10 0x17 0x11 0x0d                   h....
    body (0)

#### RECORD 9 Bolus 2013-04-17T23:16:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-04-17T23:16:40)
    0000   0x68 0x10 0x57 0x11 0x0d                   h.W..
    body (0)

#### RECORD 10 ResultTotals 2013-04-17T13:13:17 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd6                   .....
    decimal
              7    0    0    4  214
    datetime (2013-04-17T13:13:17)
    0000   0x51 0x0d 0x6d 0x51 0x0d                   Q.mQ.
    body (41)
    hex
    0000   0x05 0x10 0xa0 0x5c 0x35 0x08 0x00 0x00    ...\5...
    0008   0x04 0xd6 0x03 0x76 0x48 0x01 0x60 0x1c    ...vH.`.
    0010   0x00 0x41 0x01 0x60 0x1c 0x00 0xb8 0x34    .A.`...4
    0018   0x00 0xa8 0x30 0x00 0x00 0x00 0x03 0x02    ..0.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  160   92   53    8    0    0
              4  214    3  118   72    1   96   28
              0   65    1   96   28    0  184   52
              0  168   48    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 11 CalBGForPH 2013-04-18T08:28:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 302}
```
    op hex (2)
    0000   0x0a 0x2e                                  ..
    decimal
             10   46
    datetime (2013-04-18T08:28:43)
    0000   0x6b 0x1c 0x28 0x12 0x8d                   k.(..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 Rewind 2013-04-18T08:33:54 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-04-18T08:33:54)
    0000   0x76 0x21 0x08 0x12 0x0d                   v!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 Prime 2013-04-18T08:36:51 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2c                   ....,
    decimal
              3    0    0    0   44
    datetime (2013-04-18T08:36:51)
    0000   0x73 0x24 0x28 0x12 0x0d                   s$(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 Prime 2013-04-18T08:37:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-18T08:37:19)
    0000   0x53 0x25 0x08 0x12 0x0d                   S%...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 PumpSuspend 2013-04-18T13:04:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-18T13:04:33)
    0000   0x61 0x04 0x0d 0x12 0x0d                   a....
    body (0)

#### RECORD 16 PumpResume 2013-04-18T13:27:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-18T13:27:04)
    0000   0x44 0x1b 0x0d 0x12 0x0d                   D....
    body (0)

#### RECORD 17 CalBGForPH 2013-04-18T13:50:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-04-18T13:50:38)
    0000   0x66 0x32 0x2d 0x12 0x0d                   f2-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 BolusWizard 2013-04-18T13:50:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 146,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x92                                  [.
    decimal
             91  146
    datetime (2013-04-18T13:50:52)
    0000   0x74 0x32 0x0d 0x12 0x0d                   t2...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x04 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106    4    0    0
              0    0    0    4  125
    HOUR BITS: [0, 0, 1]
#### RECORD 19 Bolus 2013-04-18T13:50:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-04-18T13:50:52)
    0000   0x74 0x32 0x4d 0x12 0x0d                   t2M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 CalBGForPH 2013-04-18T14:35:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-04-18T14:35:36)
    0000   0x64 0x23 0x2e 0x12 0x0d                   d#...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 21 BolusWizard 2013-04-18T14:36:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 54,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 4.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-04-18T14:36:09)
    0000   0x49 0x24 0x0e 0x12 0x0d                   I$...
    body (13)
    hex
    0000   0x36 0x50 0x0d 0x2d 0x6a 0x02 0x29 0x00    6P.-j.).
    0008   0x00 0x05 0x00 0x29 0x7d                   ...)}
    decimal
             54   80   13   45  106    2   41    0
              0    5    0   41  125
    HOUR BITS: [0, 0, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 0.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x14 0x34 0x04                   \..4.
    decimal
             92    5   20   52    4
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-04-18T14:36:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'dual_component': '??', 'programmed': 4.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2013-04-18T14:36:09)
    0000   0x49 0x24 0x4e 0x12 0x0d                   I$N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 24 CalBGForPH 2013-04-18T15:23:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-04-18T15:23:25)
    0000   0x59 0x17 0x2f 0x12 0x0d                   Y./..
    body (0)

#### RECORD 25 CalBGForPH 2013-04-18T18:09:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-04-18T18:09:36)
    0000   0x64 0x09 0x32 0x12 0x0d                   d.2..
    body (0)

#### RECORD 26 BolusWizard 2013-04-18T18:09:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2013-04-18T18:09:38)
    0000   0x66 0x09 0x12 0x12 0x0d                   f....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    4    0    4  125

#### RECORD 27 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 215, 'amount': 4.1, 'curve': 4},
 {'age': 9, 'amount': 0.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xa4 0xd7 0x04 0x14 0x09 0x14    \.......
    decimal
             92    8  164  215    4   20    9   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-04-18T18:09:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-04-18T18:09:38)
    0000   0x66 0x09 0x52 0x12 0x0d                   f.R..
    body (0)

#### RECORD 29 CalBGForPH 2013-04-18T21:26:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 212}
```
    op hex (2)
    0000   0x0a 0xd4                                  ..
    decimal
             10  212
    datetime (2013-04-18T21:26:00)
    0000   0x40 0x1a 0x35 0x12 0x0d                   @.5..
    body (0)

#### RECORD 30 BolusWizard 2013-04-18T21:26:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 212,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd4                                  [.
    decimal
             91  212
    datetime (2013-04-18T21:26:04)
    0000   0x44 0x1a 0x15 0x12 0x0d                   D....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x13 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   19    0    0
              0    1    0   18  125

#### RECORD 31 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 202, 'amount': 0.4, 'curve': 4},
 {'age': 156, 'amount': 4.1, 'curve': 20},
 {'age': 206, 'amount': 0.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0xca 0x04 0xa4 0x9c 0x14    \.......
    0008   0x14 0xce 0x14                             ...
    decimal
             92   11   16  202    4  164  156   20
             20  206   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-04-18T21:26:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-04-18T21:26:04)
    0000   0x44 0x1a 0x55 0x12 0x0d                   D.U..
    body (0)

#### RECORD 33 CalBGForPH 2013-04-18T21:57:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 217}
```
    op hex (2)
    0000   0x0a 0xd9                                  ..
    decimal
             10  217
    datetime (2013-04-18T21:57:16)
    0000   0x50 0x39 0x35 0x12 0x0d                   P95..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 34 BolusWizard 2013-04-18T21:57:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 20,
 '_byte[7]': 0,
 'bg': 217,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd9                                  [.
    decimal
             91  217
    datetime (2013-04-18T21:57:26)
    0000   0x5a 0x39 0x15 0x12 0x0d                   Z9...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x13 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0   19    0    1  125
    HOUR BITS: [0, 0, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 2.0, 'curve': 4},
 {'age': 233, 'amount': 0.4, 'curve': 4},
 {'age': 187, 'amount': 4.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x21 0x04 0x10 0xe9 0x04    \.P!....
    0008   0xa4 0xbb 0x14                             ...
    decimal
             92   11   80   33    4   16  233    4
            164  187   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-04-18T21:57:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-04-18T21:57:26)
    0000   0x5a 0x39 0x55 0x12 0x0d                   Z9U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 CalBGForPH 2013-04-18T22:17:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-04-18T22:17:20)
    0000   0x54 0x11 0x36 0x12 0x0d                   T.6..
    body (0)

#### RECORD 38 CalBGForPH 2013-04-18T22:31:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2013-04-18T22:31:28)
    0000   0x5c 0x1f 0x36 0x12 0x0d                   \.6..
    body (0)

#### RECORD 39 CalBGForPH 2013-04-18T22:32:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2013-04-18T22:32:45)
    0000   0x6d 0x20 0x36 0x12 0x0d                   m 6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 BolusWizard 2013-04-18T22:34:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2013-04-18T22:34:17)
    0000   0x51 0x22 0x16 0x12 0x0d                   Q"...
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x01 0x2a 0x00    7P.-j.*.
    0008   0x00 0x14 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    1   42    0
              0   20    0   42  125
    HOUR BITS: [0, 0, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 0.5, 'curve': 4},
 {'age': 70, 'amount': 2.0, 'curve': 4},
 {'age': 14, 'amount': 0.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x28 0x04 0x50 0x46 0x04    \..(.PF.
    0008   0x10 0x0e 0x14                             ...
    decimal
             92   11   20   40    4   80   70    4
             16   14   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-04-18T22:34:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-04-18T22:34:17)
    0000   0x51 0x22 0x56 0x12 0x0d                   Q"V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 ResultTotals 2013-04-18T13:13:18 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xee                   .....
    decimal
              7    0    0    4  238
    datetime (2013-04-18T13:13:18)
    0000   0x52 0x0d 0x6d 0x52 0x0d                   R.mR.
    body (41)
    hex
    0000   0x05 0x10 0xac 0x76 0x2e 0x0a 0x00 0x00    ...v....
    0008   0x04 0xee 0x03 0x72 0x46 0x01 0x7c 0x1e    ...rF.|.
    0010   0x00 0x6d 0x01 0x7c 0x1e 0x00 0xf4 0x40    .m.|...@
    0018   0x00 0x88 0x24 0x00 0x00 0x00 0x06 0x02    ..$.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  172  118   46   10    0    0
              4  238    3  114   70    1  124   30
              0  109    1  124   30    0  244   64
              0  136   36    0    0    0    6    2
              4    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 44 CalBGForPH 2013-04-19T02:48:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 339}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-04-19T02:48:29)
    0000   0x5d 0x30 0x22 0x13 0x8d                   ]0"..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 45 BolusWizard 2013-04-19T02:48:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 47,
 '_byte[7]': 0,
 'bg': 339,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x53                                  [S
    decimal
             91   83
    datetime (2013-04-19T02:48:34)
    0000   0x62 0x30 0x02 0x13 0x0d                   b0...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2f 0x00 0x00    .Q.-j/..
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
              0   81   13   45  106   47    0    0
              0    0    0   47  125
    HOUR BITS: [0, 0, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 254, 'amount': 2.0, 'curve': 4},
 {'age': 38, 'amount': 0.5, 'curve': 20},
 {'age': 68, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0xfe 0x04 0x14 0x26 0x14    \.P...&.
    0008   0x50 0x44 0x14                             PD.
    decimal
             92   11   80  254    4   20   38   20
             80   68   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-04-19T02:48:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-04-19T02:48:34)
    0000   0x62 0x30 0x42 0x13 0x0d                   b0B..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 CalBGForPH 2013-04-19T09:04:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2013-04-19T09:04:32)
    0000   0x60 0x04 0x29 0x13 0x8d                   `.)..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 BolusWizard 2013-04-19T09:04:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 268,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2013-04-19T09:04:35)
    0000   0x63 0x04 0x09 0x13 0x0d                   c....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    0    0   31  125

#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 4.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xbc 0x7c 0x14                   \..|.
    decimal
             92    5  188  124   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-04-19T09:04:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-04-19T09:04:35)
    0000   0x63 0x04 0x49 0x13 0x0d                   c.I..
    body (0)

#### RECORD 52 PumpSuspend 2013-04-19T13:38:04 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-19T13:38:04)
    0000   0x44 0x26 0x0d 0x13 0x0d                   D&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 53 PumpResume 2013-04-19T14:15:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-19T14:15:05)
    0000   0x45 0x0f 0x0e 0x13 0x0d                   E....
    body (0)

#### RECORD 54 CalBGForPH 2013-04-19T14:43:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-04-19T14:43:09)
    0000   0x49 0x2b 0x2e 0x13 0x0d                   I+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 CalBGForPH 2013-04-19T14:45:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-04-19T14:45:15)
    0000   0x4f 0x2d 0x2e 0x13 0x0d                   O-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 BolusWizard 2013-04-19T14:46:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 72,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 3.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x48                                  [H
    decimal
             91   72
    datetime (2013-04-19T14:46:26)
    0000   0x5a 0x2e 0x0e 0x13 0x0d                   Z....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0xf8 0x23 0xf0    .P.-j.#.
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
             46   80   13   45  106  248   35  240
              0    0    0   27  125
    HOUR BITS: [0, 0, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 3.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x56 0x14                   \.|V.
    decimal
             92    5  124   86   20
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-04-19T14:46:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-04-19T14:46:26)
    0000   0x5a 0x2e 0x4e 0x13 0x0d                   Z.N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 59 CalBGForPH 2013-04-19T15:10:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-04-19T15:10:30)
    0000   0x5e 0x0a 0x2f 0x13 0x0d                   ^./..
    body (0)

#### RECORD 60 BolusWizard 2013-04-19T15:10:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 72,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 1.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x48                                  [H
    decimal
             91   72
    datetime (2013-04-19T15:10:42)
    0000   0x6a 0x0a 0x0f 0x13 0x0d                   j....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0xf8 0x0a 0xf0    .P.-j...
    0008   0x00 0x1a 0x00 0x02 0x7d                   ....}
    decimal
             13   80   13   45  106  248   10  240
              0   26    0    2  125

#### RECORD 61 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 2.7, 'curve': 4},
 {'age': 110, 'amount': 3.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x1a 0x04 0x7c 0x6e 0x14    \.l..|n.
    decimal
             92    8  108   26    4  124  110   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-04-19T15:10:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-04-19T15:10:42)
    0000   0x6a 0x0a 0x4f 0x13 0x0d                   j.O..
    body (0)

#### RECORD 63 BolusWizard 2013-04-19T15:47:49 head[2], body[13] op[0x5b]
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
    datetime (2013-04-19T15:47:49)
    0000   0x71 0x2f 0x0f 0x13 0x0d                   q/...
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [0, 0, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 0.2, 'curve': 4},
 {'age': 63, 'amount': 2.7, 'curve': 4},
 {'age': 147, 'amount': 3.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x08 0x2b 0x04 0x6c 0x3f 0x04    \..+.l?.
    0008   0x7c 0x93 0x14                             |..
    decimal
             92   11    8   43    4  108   63    4
            124  147   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-04-19T15:47:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-04-19T15:47:50)
    0000   0x72 0x2f 0x4f 0x13 0x0d                   r/O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 66 BolusWizard 2013-04-19T16:03:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 22,
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
    datetime (2013-04-19T16:03:49)
    0000   0x71 0x03 0x10 0x13 0x0d                   q....
    body (13)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             22   80   13   45  106    0   16    0
              0    0    0   16  125

#### RECORD 67 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 1.3, 'curve': 4},
 {'age': 59, 'amount': 0.2, 'curve': 4},
 {'age': 79, 'amount': 2.7, 'curve': 4},
 {'age': 163, 'amount': 3.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x34 0x13 0x04 0x08 0x3b 0x04    \.4...;.
    0008   0x6c 0x4f 0x04 0x7c 0xa3 0x14              lO.|..
    decimal
             92   14   52   19    4    8   59    4
            108   79    4  124  163   20
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-04-19T16:03:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-04-19T16:03:49)
    0000   0x71 0x03 0x50 0x13 0x0d                   q.P..
    body (0)

#### RECORD 69 CalBGForPH 2013-04-19T16:23:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-04-19T16:23:27)
    0000   0x5b 0x17 0x30 0x13 0x0d                   [.0..
    body (0)

#### RECORD 70 CalBGForPH 2013-04-19T18:03:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-04-19T18:03:08)
    0000   0x48 0x03 0x32 0x13 0x0d                   H.2..
    body (0)

#### RECORD 71 CalBGForPH 2013-04-19T18:26:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-04-19T18:26:41)
    0000   0x69 0x1a 0x32 0x13 0x0d                   i.2..
    body (0)

#### RECORD 72 BolusWizard 2013-04-19T18:26:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 115,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-04-19T18:26:55)
    0000   0x77 0x1a 0x12 0x13 0x0d                   w....
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0   11    0   13  125

#### RECORD 73 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 142, 'amount': 1.3, 'curve': 4},
 {'age': 152, 'amount': 0.3, 'curve': 4},
 {'age': 162, 'amount': 1.3, 'curve': 4},
 {'age': 202, 'amount': 0.2, 'curve': 4},
 {'age': 222, 'amount': 2.7, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x34 0x8e 0x04 0x0c 0x98 0x04    \.4.....
    0008   0x34 0xa2 0x04 0x08 0xca 0x04 0x6c 0xde    4.....l.
    0010   0x04                                       .
    decimal
             92   17   52  142    4   12  152    4
             52  162    4    8  202    4  108  222
              4
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2013-04-19T18:26:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-04-19T18:26:55)
    0000   0x77 0x1a 0x52 0x13 0x0d                   w.R..
    body (0)

#### RECORD 75 CalBGForPH 2013-04-19T23:06:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 323}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2013-04-19T23:06:57)
    0000   0x79 0x06 0x37 0x13 0x8d                   y.7..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 76 BolusWizard 2013-04-19T23:06:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 44,
 '_byte[7]': 0,
 'bg': 323,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x43                                  [C
    decimal
             91   67
    datetime (2013-04-19T23:06:59)
    0000   0x7b 0x06 0x17 0x13 0x0d                   {....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2c 0x00 0x00    .Q.-j,..
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
              0   81   13   45  106   44    0    0
              0    0    0   44  125

#### RECORD 77 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 1.3, 'curve': 20},
 {'age': 166, 'amount': 1.3, 'curve': 20},
 {'age': 176, 'amount': 0.3, 'curve': 20},
 {'age': 186, 'amount': 1.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x34 0x1a 0x14 0x34 0xa6 0x14    \.4..4..
    0008   0x0c 0xb0 0x14 0x34 0xba 0x14              ...4..
    decimal
             92   14   52   26   20   52  166   20
             12  176   20   52  186   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2013-04-19T23:06:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-04-19T23:06:59)
    0000   0x7b 0x06 0x57 0x13 0x0d                   {.W..
    body (0)

#### RECORD 79 ResultTotals 2013-04-19T13:13:19 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x6e                   ....n
    decimal
              7    0    0    6  110
    datetime (2013-04-19T13:13:19)
    0000   0x53 0x0d 0x6d 0x53 0x0d                   S.mS.
    body (41)
    hex
    0000   0x05 0x10 0xa5 0x48 0x53 0x09 0x00 0x00    ...HS...
    0008   0x06 0x6e 0x03 0x6a 0x35 0x03 0x04 0x2f    .n.j5../
    0010   0x00 0x73 0x03 0x04 0x2f 0x01 0x1c 0x25    .s../..%
    0018   0x01 0xe8 0x3f 0x00 0x00 0x00 0x08 0x05    ..?.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  165   72   83    9    0    0
              6  110    3  106   53    3    4   47
              0  115    3    4   47    1   28   37
              1  232   63    0    0    0    8    5
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 80 CalBGForPH 2013-04-20T20:38:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 201}
```
    op hex (2)
    0000   0x0a 0xc9                                  ..
    decimal
             10  201
    datetime (2013-04-20T20:38:44)
    0000   0x6c 0x26 0x34 0x14 0x0d                   l&4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 81 BolusWizard 2013-04-20T20:38:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 201,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
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
    0000   0x5b 0xc9                                  [.
    decimal
             91  201
    datetime (2013-04-20T20:38:47)
    0000   0x6f 0x26 0x14 0x14 0x0d                   o&...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125
    HOUR BITS: [0, 0, 1]
#### RECORD 82 Bolus 2013-04-20T20:38:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-04-20T20:38:47)
    0000   0x6f 0x26 0x54 0x14 0x0d                   o&T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 83 CalBGForPH 2013-04-20T22:40:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2013-04-20T22:40:37)
    0000   0x65 0x28 0x36 0x14 0x0d                   e(6..
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-15.data: 84 records`
