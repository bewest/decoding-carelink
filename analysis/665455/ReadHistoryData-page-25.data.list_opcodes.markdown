## START logs/ReadHistoryData-page-25.data
#### RECORD 0 BolusWizard 2013-04-20T22:40:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 176,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2013-04-20T22:40:40)
    0000   0x68 0x28 0x16 0x14 0x0d                   h(...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    7    0    4  125
    HOUR BITS: [0, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 1.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x7e 0x04                   \.@~.
    decimal
             92    5   64  126    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-04-20T22:40:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-04-20T22:40:40)
    0000   0x68 0x28 0x56 0x14 0x0d                   h(V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalBGForPH 2013-04-20T22:46:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2013-04-20T22:46:50)
    0000   0x72 0x2e 0x36 0x14 0x0d                   r.6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BolusWizard 2013-04-20T22:47:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 177,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb1                                  [.
    decimal
             91  177
    datetime (2013-04-20T22:47:07)
    0000   0x47 0x2f 0x16 0x14 0x0d                   G/...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x0b 0x2e 0x00    <P.-j...
    0008   0x00 0x0b 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106   11   46    0
              0   11    0   46  125
    HOUR BITS: [0, 0, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 0.4, 'curve': 4},
 {'age': 133, 'amount': 1.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x0d 0x04 0x40 0x85 0x04    \....@..
    decimal
             92    8   16   13    4   64  133    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-04-20T22:47:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-04-20T22:47:07)
    0000   0x47 0x2f 0x56 0x14 0x0d                   G/V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 BolusWizard 2013-04-20T23:10:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
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
    datetime (2013-04-20T23:10:36)
    0000   0x64 0x0a 0x17 0x14 0x0d                   d....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125

#### RECORD 8 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 4.6, 'curve': 4},
 {'age': 36, 'amount': 0.4, 'curve': 4},
 {'age': 156, 'amount': 1.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0xb8 0x1a 0x04 0x10 0x24 0x04    \.....$.
    0008   0x40 0x9c 0x04                             @..
    decimal
             92   11  184   26    4   16   36    4
             64  156    4
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-04-20T23:10:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-04-20T23:10:36)
    0000   0x64 0x0a 0x57 0x14 0x0d                   d.W..
    body (0)

#### RECORD 10 ResultTotals 2013-04-20T13:13:20 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbc                   .....
    decimal
              7    0    0    4  188
    datetime (2013-04-20T13:13:20)
    0000   0x54 0x0d 0x6d 0x54 0x0d                   T.mT.
    body (41)
    hex
    0000   0x05 0x00 0xb9 0xb0 0xc9 0x03 0x00 0x00    ........
    0008   0x04 0xbc 0x03 0x84 0x4a 0x01 0x38 0x1a    ....J.8.
    0010   0x00 0x4c 0x01 0x38 0x1a 0x00 0xe8 0x4a    .L.8...J
    0018   0x00 0x50 0x1a 0x00 0x00 0x00 0x04 0x02    .P......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  185  176  201    3    0    0
              4  188    3  132   74    1   56   26
              0   76    1   56   26    0  232   74
              0   80   26    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 11 CalBGForPH 2013-04-21T03:11:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 327}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2013-04-21T03:11:48)
    0000   0x70 0x0b 0x23 0x15 0x8d                   p.#..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 BolusWizard 2013-04-21T03:11:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 44,
 '_byte[7]': 0,
 'bg': 327,
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
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2013-04-21T03:11:57)
    0000   0x79 0x0b 0x03 0x15 0x0d                   y....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2c 0x00 0x00    .Q.-j,..
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
              0   81   13   45  106   44    0    0
              0    0    0   44  125

#### RECORD 13 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 247, 'amount': 1.2, 'curve': 4},
 {'age': 11, 'amount': 4.6, 'curve': 20},
 {'age': 21, 'amount': 0.4, 'curve': 20},
 {'age': 141, 'amount': 1.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x30 0xf7 0x04 0xb8 0x0b 0x14    \.0.....
    0008   0x10 0x15 0x14 0x40 0x8d 0x14              ...@..
    decimal
             92   14   48  247    4  184   11   20
             16   21   20   64  141   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-04-21T03:11:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-04-21T03:11:57)
    0000   0x79 0x0b 0x43 0x15 0x0d                   y.C..
    body (0)

#### RECORD 15 CalBGForPH 2013-04-21T07:25:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-04-21T07:25:59)
    0000   0x7b 0x19 0x27 0x15 0x0d                   {.'..
    body (0)

#### RECORD 16 BolusWizard 2013-04-21T07:26:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-04-21T07:26:02)
    0000   0x42 0x1a 0x07 0x15 0x0d                   B....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125

#### RECORD 17 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 252, 'amount': 1.3, 'curve': 4},
 {'age': 6, 'amount': 3.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0xfc 0x04 0x7c 0x06 0x14    \.4..|..
    decimal
             92    8   52  252    4  124    6   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-04-21T07:26:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-04-21T07:26:02)
    0000   0x42 0x1a 0x47 0x15 0x0d                   B.G..
    body (0)

#### RECORD 19 PumpSuspend 2013-04-21T08:42:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-21T08:42:20)
    0000   0x54 0x2a 0x08 0x15 0x0d                   T*...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 PumpResume 2013-04-21T09:11:47 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-21T09:11:47)
    0000   0x6f 0x0b 0x09 0x15 0x0d                   o....
    body (0)

#### RECORD 21 CalBGForPH 2013-04-21T10:21:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 220}
```
    op hex (2)
    0000   0x0a 0xdc                                  ..
    decimal
             10  220
    datetime (2013-04-21T10:21:47)
    0000   0x6f 0x15 0x2a 0x15 0x0d                   o.*..
    body (0)

#### RECORD 22 BolusWizard 2013-04-21T10:21:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 220,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdc                                  [.
    decimal
             91  220
    datetime (2013-04-21T10:21:49)
    0000   0x71 0x15 0x0a 0x15 0x0d                   q....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    3    0   18  125

#### RECORD 23 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 177, 'amount': 1.3, 'curve': 4},
 {'age': 171, 'amount': 1.3, 'curve': 20},
 {'age': 181, 'amount': 3.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0xb1 0x04 0x34 0xab 0x14    \.4..4..
    0008   0x7c 0xb5 0x14                             |..
    decimal
             92   11   52  177    4   52  171   20
            124  181   20
    datetime (unknown)

    body (0)

#### RECORD 24 LowReservoir 2013-04-21T10:22:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-04-21T10:22:45)
    0000   0x6d 0x16 0x0a 0x15 0x0d                   m....
    body (0)

#### RECORD 25 Bolus 2013-04-21T10:21:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-04-21T10:21:49)
    0000   0x71 0x15 0x4a 0x15 0x0d                   q.J..
    body (0)

#### RECORD 26 BolusWizard 2013-04-21T10:32:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
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
    datetime (2013-04-21T10:32:07)
    0000   0x47 0x20 0x0a 0x15 0x0d                   G ...
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [0, 0, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 1.8, 'curve': 4},
 {'age': 188, 'amount': 1.3, 'curve': 4},
 {'age': 182, 'amount': 1.3, 'curve': 20},
 {'age': 192, 'amount': 3.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x12 0x04 0x34 0xbc 0x04    \.H..4..
    0008   0x34 0xb6 0x14 0x7c 0xc0 0x14              4..|..
    decimal
             92   14   72   18    4   52  188    4
             52  182   20  124  192   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-04-21T10:32:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-04-21T10:32:07)
    0000   0x47 0x20 0x4a 0x15 0x0d                   G J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 29 CalBGForPH 2013-04-21T11:47:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 281}
```
    op hex (2)
    0000   0x0a 0x19                                  ..
    decimal
             10   25
    datetime (2013-04-21T11:47:57)
    0000   0x79 0x2f 0x2b 0x15 0x8d                   y/+..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 BolusWizard 2013-04-21T11:48:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 34,
 '_byte[7]': 0,
 'bg': 281,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x19                                  [.
    decimal
             91   25
    datetime (2013-04-21T11:48:05)
    0000   0x45 0x30 0x0b 0x15 0x0d                   E0...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x22 0x00 0x00    .Q.-j"..
    0008   0x00 0x15 0x00 0x0d 0x7d                   ....}
    decimal
              0   81   13   45  106   34    0    0
              0   21    0   13  125
    HOUR BITS: [0, 0, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 84, 'amount': 1.3, 'curve': 4},
 {'age': 94, 'amount': 1.8, 'curve': 4},
 {'age': 8, 'amount': 1.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x54 0x04 0x48 0x5e 0x04    \.4T.H^.
    0008   0x34 0x08 0x14                             4..
    decimal
             92   11   52   84    4   72   94    4
             52    8   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-04-21T11:48:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-04-21T11:48:05)
    0000   0x45 0x30 0x4b 0x15 0x0d                   E0K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 CalBGForPH 2013-04-21T12:04:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 243}
```
    op hex (2)
    0000   0x0a 0xf3                                  ..
    decimal
             10  243
    datetime (2013-04-21T12:04:11)
    0000   0x4b 0x04 0x2c 0x15 0x0d                   K.,..
    body (0)

#### RECORD 34 BolusWizard 2013-04-21T12:04:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 243,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf3                                  [.
    decimal
             91  243
    datetime (2013-04-21T12:04:48)
    0000   0x70 0x04 0x0c 0x15 0x0d                   p....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x20 0x00 0x00 0x7d                   . ..}
    decimal
              0   80   13   45  106   26    0    0
              0   32    0    0  125

#### RECORD 35 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 1.5, 'curve': 4},
 {'age': 100, 'amount': 1.3, 'curve': 4},
 {'age': 110, 'amount': 1.8, 'curve': 4},
 {'age': 24, 'amount': 1.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0x14 0x04 0x34 0x64 0x04    \.<..4d.
    0008   0x48 0x6e 0x04 0x34 0x18 0x14              Hn.4..
    decimal
             92   14   60   20    4   52  100    4
             72  110    4   52   24   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-04-21T12:04:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-04-21T12:04:48)
    0000   0x70 0x04 0x4c 0x15 0x0d                   p.L..
    body (0)

#### RECORD 37 CalBGForPH 2013-04-21T12:39:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 204}
```
    op hex (2)
    0000   0x0a 0xcc                                  ..
    decimal
             10  204
    datetime (2013-04-21T12:39:33)
    0000   0x61 0x27 0x2c 0x15 0x0d                   a',..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 38 BolusWizard 2013-04-21T12:41:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 17,
 '_byte[7]': 0,
 'bg': 204,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcc                                  [.
    decimal
             91  204
    datetime (2013-04-21T12:41:05)
    0000   0x45 0x29 0x0c 0x15 0x0d                   E)...
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x11 0x20 0x00    *P.-j. .
    0008   0x00 0x1c 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106   17   32    0
              0   28    0   32  125
    HOUR BITS: [0, 0, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 0.5, 'curve': 4},
 {'age': 57, 'amount': 1.5, 'curve': 4},
 {'age': 137, 'amount': 1.3, 'curve': 4},
 {'age': 147, 'amount': 1.8, 'curve': 4},
 {'age': 61, 'amount': 1.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x14 0x25 0x04 0x3c 0x39 0x04    \..%.<9.
    0008   0x34 0x89 0x04 0x48 0x93 0x04 0x34 0x3d    4..H..4=
    0010   0x14                                       .
    decimal
             92   17   20   37    4   60   57    4
             52  137    4   72  147    4   52   61
             20
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-04-21T12:41:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-04-21T12:41:05)
    0000   0x45 0x29 0x4c 0x15 0x0d                   E)L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 LowReservoir 2013-04-21T13:10:54 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-04-21T13:10:54)
    0000   0x76 0x0a 0x0d 0x15 0x0d                   v....
    body (0)

#### RECORD 42 CalBGForPH 2013-04-21T13:24:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-04-21T13:24:50)
    0000   0x72 0x18 0x2d 0x15 0x0d                   r.-..
    body (0)

#### RECORD 43 CalBGForPH 2013-04-21T15:23:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-04-21T15:23:35)
    0000   0x63 0x17 0x2f 0x15 0x0d                   c./..
    body (0)

#### RECORD 44 CalBGForPH 2013-04-21T21:28:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 246}
```
    op hex (2)
    0000   0x0a 0xf6                                  ..
    decimal
             10  246
    datetime (2013-04-21T21:28:43)
    0000   0x6b 0x1c 0x35 0x15 0x0d                   k.5..
    body (0)

#### RECORD 45 BolusWizard 2013-04-21T21:28:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 246,
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
    0000   0x5b 0xf6                                  [.
    decimal
             91  246
    datetime (2013-04-21T21:28:45)
    0000   0x6d 0x1c 0x15 0x15 0x0d                   m....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0    0    0   26  125

#### RECORD 46 Bolus 2013-04-21T21:28:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-04-21T21:28:45)
    0000   0x6d 0x1c 0x55 0x15 0x0d                   m.U..
    body (0)

#### RECORD 47 Rewind 2013-04-21T22:52:51 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-04-21T22:52:51)
    0000   0x73 0x34 0x16 0x15 0x0d                   s4...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 Prime 2013-04-21T22:54:43 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 5.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x39                   ....9
    decimal
              3    0    0    0   57
    datetime (2013-04-21T22:54:43)
    0000   0x6b 0x36 0x36 0x15 0x0d                   k66..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 Prime 2013-04-21T22:55:13 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-21T22:55:13)
    0000   0x4d 0x37 0x16 0x15 0x0d                   M7...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 CalBGForPH 2013-04-21T23:00:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 134}
```
    op hex (2)
    0000   0x0a 0x86                                  ..
    decimal
             10  134
    datetime (2013-04-21T23:00:26)
    0000   0x5a 0x00 0x37 0x15 0x0d                   Z.7..
    body (0)

#### RECORD 51 BolusWizard 2013-04-21T23:00:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 134,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 3.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x86                                  [.
    decimal
             91  134
    datetime (2013-04-21T23:00:37)
    0000   0x65 0x00 0x17 0x15 0x0d                   e....
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0x02 0x25 0x00    1P.-j.%.
    0008   0x00 0x10 0x00 0x25 0x7d                   ...%}
    decimal
             49   80   13   45  106    2   37    0
              0   16    0   37  125

#### RECORD 52 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0x60 0x04                   \.h`.
    decimal
             92    5  104   96    4
    datetime (unknown)

    body (0)

#### RECORD 53 BolusWizard 2013-04-20T22:40:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 176,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2013-04-20T22:40:40)
    0000   0x68 0x28 0x16 0x14 0x0d                   h(...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    7    0    4  125
    HOUR BITS: [0, 0, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 1.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x7e 0x04                   \.@~.
    decimal
             92    5   64  126    4
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-04-20T22:40:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-04-20T22:40:40)
    0000   0x68 0x28 0x56 0x14 0x0d                   h(V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 CalBGForPH 2013-04-20T22:46:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2013-04-20T22:46:50)
    0000   0x72 0x2e 0x36 0x14 0x0d                   r.6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 BolusWizard 2013-04-20T22:47:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 177,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb1                                  [.
    decimal
             91  177
    datetime (2013-04-20T22:47:07)
    0000   0x47 0x2f 0x16 0x14 0x0d                   G/...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x0b 0x2e 0x00    <P.-j...
    0008   0x00 0x0b 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106   11   46    0
              0   11    0   46  125
    HOUR BITS: [0, 0, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 0.4, 'curve': 4},
 {'age': 133, 'amount': 1.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x0d 0x04 0x40 0x85 0x04    \....@..
    decimal
             92    8   16   13    4   64  133    4
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-04-20T22:47:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-04-20T22:47:07)
    0000   0x47 0x2f 0x56 0x14 0x0d                   G/V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 BolusWizard 2013-04-20T23:10:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
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
    datetime (2013-04-20T23:10:36)
    0000   0x64 0x0a 0x17 0x14 0x0d                   d....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125

#### RECORD 61 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 4.6, 'curve': 4},
 {'age': 36, 'amount': 0.4, 'curve': 4},
 {'age': 156, 'amount': 1.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0xb8 0x1a 0x04 0x10 0x24 0x04    \.....$.
    0008   0x40 0x9c 0x04                             @..
    decimal
             92   11  184   26    4   16   36    4
             64  156    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-04-20T23:10:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-04-20T23:10:36)
    0000   0x64 0x0a 0x57 0x14 0x0d                   d.W..
    body (0)

#### RECORD 63 ResultTotals 2013-04-20T13:13:20 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbc                   .....
    decimal
              7    0    0    4  188
    datetime (2013-04-20T13:13:20)
    0000   0x54 0x0d 0x6d 0x54 0x0d                   T.mT.
    body (41)
    hex
    0000   0x05 0x00 0xb9 0xb0 0xc9 0x03 0x00 0x00    ........
    0008   0x04 0xbc 0x03 0x84 0x4a 0x01 0x38 0x1a    ....J.8.
    0010   0x00 0x4c 0x01 0x38 0x1a 0x00 0xe8 0x4a    .L.8...J
    0018   0x00 0x50 0x1a 0x00 0x00 0x00 0x04 0x02    .P......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  185  176  201    3    0    0
              4  188    3  132   74    1   56   26
              0   76    1   56   26    0  232   74
              0   80   26    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 64 CalBGForPH 2013-04-21T03:11:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 327}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2013-04-21T03:11:48)
    0000   0x70 0x0b 0x23 0x15 0x8d                   p.#..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 65 BolusWizard 2013-04-21T03:11:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 44,
 '_byte[7]': 0,
 'bg': 327,
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
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2013-04-21T03:11:57)
    0000   0x79 0x0b 0x03 0x15 0x0d                   y....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2c 0x00 0x00    .Q.-j,..
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
              0   81   13   45  106   44    0    0
              0    0    0   44  125

#### RECORD 66 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 247, 'amount': 1.2, 'curve': 4},
 {'age': 11, 'amount': 4.6, 'curve': 20},
 {'age': 21, 'amount': 0.4, 'curve': 20},
 {'age': 141, 'amount': 1.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x30 0xf7 0x04 0xb8 0x0b 0x14    \.0.....
    0008   0x10 0x15 0x14 0x40 0x8d 0x14              ...@..
    decimal
             92   14   48  247    4  184   11   20
             16   21   20   64  141   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-04-21T03:11:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-04-21T03:11:57)
    0000   0x79 0x0b 0x43 0x15 0x0d                   y.C..
    body (0)

#### RECORD 68 CalBGForPH 2013-04-21T07:25:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-04-21T07:25:59)
    0000   0x7b 0x19 0x27 0x15 0x0d                   {.'..
    body (0)

#### RECORD 69 BolusWizard 2013-04-21T07:26:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-04-21T07:26:02)
    0000   0x42 0x1a 0x07 0x15 0x0d                   B....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125

#### RECORD 70 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 252, 'amount': 1.3, 'curve': 4},
 {'age': 6, 'amount': 3.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0xfc 0x04 0x7c 0x06 0x14    \.4..|..
    decimal
             92    8   52  252    4  124    6   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-04-21T07:26:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-04-21T07:26:02)
    0000   0x42 0x1a 0x47 0x15 0x0d                   B.G..
    body (0)

#### RECORD 72 PumpSuspend 2013-04-21T08:42:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-21T08:42:20)
    0000   0x54 0x2a 0x08 0x15 0x0d                   T*...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 73 PumpResume 2013-04-21T09:11:47 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-21T09:11:47)
    0000   0x6f 0x0b 0x09 0x15 0x0d                   o....
    body (0)

#### RECORD 74 CalBGForPH 2013-04-21T10:21:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 220}
```
    op hex (2)
    0000   0x0a 0xdc                                  ..
    decimal
             10  220
    datetime (2013-04-21T10:21:47)
    0000   0x6f 0x15 0x2a 0x15 0x0d                   o.*..
    body (0)

#### RECORD 75 BolusWizard 2013-04-21T10:21:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 220,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdc                                  [.
    decimal
             91  220
    datetime (2013-04-21T10:21:49)
    0000   0x71 0x15 0x0a 0x15 0x0d                   q....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    3    0   18  125

#### RECORD 76 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 177, 'amount': 1.3, 'curve': 4},
 {'age': 171, 'amount': 1.3, 'curve': 20},
 {'age': 181, 'amount': 3.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0xb1 0x04 0x34 0xab 0x14    \.4..4..
    0008   0x7c 0xb5 0x14                             |..
    decimal
             92   11   52  177    4   52  171   20
            124  181   20
    datetime (unknown)

    body (0)

#### RECORD 77 LowReservoir unknown head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-25.data: 78 records`
