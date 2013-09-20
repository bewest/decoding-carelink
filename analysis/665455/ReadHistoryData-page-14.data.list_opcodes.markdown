## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe8 0xa7                                  ..
##### DEBUG DECIMAL
            232  167
#### RECORD 0 Bolus 2013-06-02T12:44:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-06-02T12:44:22)
    0000   0x56 0xac 0x4c 0x02 0x0d                   V.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 1 CalBGForPH 2013-06-02T17:31:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 301}
```
    op hex (2)
    0000   0x0a 0x2d                                  .-
    decimal
             10   45
    datetime (2013-06-02T17:31:49)
    0000   0x71 0x9f 0x31 0x02 0x8d                   q.1..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 BolusWizard 2013-06-02T17:31:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 39,
 '_byte[7]': 0,
 'bg': 301,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2d                                  [-
    decimal
             91   45
    datetime (2013-06-02T17:31:53)
    0000   0x75 0x9f 0x11 0x02 0x0d                   u....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x27 0x00 0x00    .Q.-j'..
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
              0   81   13   45  106   39    0    0
              0    0    0   39  125
    HOUR BITS: [1, 0, 0]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 0.7, 'curve': 20},
 {'age': 41, 'amount': 3.0, 'curve': 20},
 {'age': 121, 'amount': 1.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x1c 0x1f 0x14 0x78 0x29 0x14    \....x).
    0008   0x28 0x79 0x14                             (y.
    decimal
             92   11   28   31   20  120   41   20
             40  121   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-06-02T17:31:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-06-02T17:31:53)
    0000   0x75 0x9f 0x51 0x02 0x0d                   u.Q..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 CalBGForPH 2013-06-02T18:30:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 246}
```
    op hex (2)
    0000   0x0a 0xf6                                  ..
    decimal
             10  246
    datetime (2013-06-02T18:30:45)
    0000   0x6d 0x9e 0x32 0x02 0x0d                   m.2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 CalBGForPH 2013-06-02T20:24:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-06-02T20:24:35)
    0000   0x63 0x98 0x34 0x02 0x0d                   c.4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 BolusWizard 2013-06-02T20:25:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 144,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x90                                  [.
    decimal
             91  144
    datetime (2013-06-02T20:25:10)
    0000   0x4a 0x99 0x14 0x02 0x0d                   J....
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0x04 0x35 0x00    EP.-j.5.
    0008   0x00 0x08 0x00 0x35 0x7d                   ...5}
    decimal
             69   80   13   45  106    4   53    0
              0    8    0   53  125
    HOUR BITS: [1, 0, 0]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 171, 'amount': 0.85, 'curve': 4},
 {'age': 181, 'amount': 3.15, 'curve': 4},
 {'age': 205, 'amount': 0.7, 'curve': 20},
 {'age': 215, 'amount': 3.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x22 0xab 0x04 0x7e 0xb5 0x04    \."..~..
    0008   0x1c 0xcd 0x14 0x78 0xd7 0x14              ...x..
    decimal
             92   14   34  171    4  126  181    4
             28  205   20  120  215   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-06-02T20:25:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-06-02T20:25:11)
    0000   0x4b 0x99 0x54 0x02 0x0d                   K.T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 MResultTotals 2013-06-03T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-06-03T00:00:00)
    0000   0x00 0x06 0x70 0x62 0x0d                   ..pb.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 11 Model522ResultTotals 2013-06-03T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-03T00:00:00)
    0000   0x62 0x0d                                  b.
    body (41)
    hex
    0000   0x05 0x10 0xdf 0x7b 0x69 0x06 0x00 0x00    ...{i...
    0008   0x06 0x70 0x03 0x78 0x36 0x02 0xf8 0x2e    .p.x6...
    0010   0x00 0x76 0x02 0xf8 0x2e 0x01 0x68 0x2f    .v....h/
    0018   0x01 0x90 0x35 0x00 0x00 0x00 0x06 0x03    ..5.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  223  123  105    6    0    0
              6  112    3  120   54    2  248   46
              0  118    2  248   46    1  104   47
              1  144   53    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0

#### RECORD 12 PumpSuspend 2013-06-03T11:14:02 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-03T11:14:02)
    0000   0x42 0x8e 0x0b 0x03 0x0d                   B....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 13 PumpResume 2013-06-03T12:11:52 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-03T12:11:52)
    0000   0x74 0x8b 0x0c 0x03 0x0d                   t....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 14 CalBGForPH 2013-06-03T13:18:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2013-06-03T13:18:10)
    0000   0x4a 0x92 0x2d 0x03 0x0d                   J.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 15 BolusWizard 2013-06-03T13:18:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 142,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2013-06-03T13:18:54)
    0000   0x76 0x92 0x0d 0x03 0x0d                   v....
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0x03 0x2b 0x00    8P.-j.+.
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             56   80   13   45  106    3   43    0
              0    0    0   46  125
    HOUR BITS: [1, 0, 0]
#### RECORD 16 Bolus 2013-06-03T13:18:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-06-03T13:18:54)
    0000   0x76 0x92 0x4d 0x03 0x0d                   v.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 BolusWizard 2013-06-03T14:01:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.2,
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
    datetime (2013-06-03T14:01:11)
    0000   0x4b 0x81 0x0e 0x03 0x0d                   K....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0x00 0x16 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
             29   80   13   45  106    0   22    0
              0    0    0   22  125
    HOUR BITS: [1, 0, 0]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 4.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb8 0x2f 0x04                   \../.
    decimal
             92    5  184   47    4
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-06-03T14:01:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-06-03T14:01:11)
    0000   0x4b 0x81 0x4e 0x03 0x0d                   K.N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 BolusWizard 2013-06-03T14:31:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.4,
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
    datetime (2013-06-03T14:31:16)
    0000   0x50 0x9f 0x0e 0x03 0x0d                   P....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x00 0x18 0x00     P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
             32   80   13   45  106    0   24    0
              0    0    0   24  125
    HOUR BITS: [1, 0, 0]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 2.2, 'curve': 4},
 {'age': 77, 'amount': 4.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x58 0x25 0x04 0xb8 0x4d 0x04    \.X%..M.
    decimal
             92    8   88   37    4  184   77    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-06-03T14:31:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-06-03T14:31:16)
    0000   0x50 0x9f 0x4e 0x03 0x0d                   P.N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 CalBGForPH 2013-06-03T16:11:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-06-03T16:11:09)
    0000   0x49 0x8b 0x30 0x03 0x0d                   I.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 LowReservoir 2013-06-03T18:03:09 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-06-03T18:03:09)
    0000   0x49 0x83 0x12 0x03 0x0d                   I....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 25 CalBGForPH 2013-06-03T19:01:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-06-03T19:01:46)
    0000   0x6e 0x81 0x33 0x03 0x0d                   n.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 26 BolusWizard 2013-06-03T19:01:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 144,
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
    0000   0x5b 0x90                                  [.
    decimal
             91  144
    datetime (2013-06-03T19:01:52)
    0000   0x74 0x81 0x13 0x03 0x0d                   t....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x04 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106    4    0    0
              0    0    0    4  125
    HOUR BITS: [1, 0, 0]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 2.4, 'curve': 20},
 {'age': 51, 'amount': 2.2, 'curve': 20},
 {'age': 91, 'amount': 4.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x60 0x15 0x14 0x58 0x33 0x14    \.`..X3.
    0008   0xb8 0x5b 0x14                             .[.
    decimal
             92   11   96   21   20   88   51   20
            184   91   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-06-03T19:01:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-06-03T19:01:52)
    0000   0x74 0x81 0x53 0x03 0x0d                   t.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 CalBGForPH 2013-06-03T20:55:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2013-06-03T20:55:39)
    0000   0x67 0xb7 0x34 0x03 0x0d                   g.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 30 BolusWizard 2013-06-03T20:57:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 125,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7d                                  [}
    decimal
             91  125
    datetime (2013-06-03T20:57:07)
    0000   0x47 0xb9 0x14 0x03 0x0d                   G....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0    3    0   21  125
    HOUR BITS: [1, 0, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 123, 'amount': 0.6, 'curve': 4},
 {'age': 137, 'amount': 2.4, 'curve': 20},
 {'age': 167, 'amount': 2.2, 'curve': 20},
 {'age': 207, 'amount': 4.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x7b 0x04 0x60 0x89 0x14    \..{.`..
    0008   0x58 0xa7 0x14 0xb8 0xcf 0x14              X.....
    decimal
             92   14   24  123    4   96  137   20
             88  167   20  184  207   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-06-03T20:57:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-06-03T20:57:07)
    0000   0x47 0xb9 0x54 0x03 0x0d                   G.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 MResultTotals 2013-06-04T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-06-04T00:00:00)
    0000   0x00 0x05 0x36 0x63 0x0d                   ..6c.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 34 Model522ResultTotals 2013-06-04T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-04T00:00:00)
    0000   0x63 0x0d                                  c.
    body (41)
    hex
    0000   0x05 0x00 0x7e 0x5c 0x90 0x04 0x00 0x00    ..~\....
    0008   0x05 0x36 0x03 0x5a 0x40 0x01 0xdc 0x24    .6.Z@..$
    0010   0x00 0x91 0x01 0xdc 0x24 0x01 0xb8 0x5c    ....$..\
    0018   0x00 0x24 0x08 0x00 0x00 0x00 0x05 0x03    .$......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  126   92  144    4    0    0
              5   54    3   90   64    1  220   36
              0  145    1  220   36    1  184   92
              0   36    8    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0

#### RECORD 35 LowReservoir 2013-06-04T02:03:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-06-04T02:03:45)
    0000   0x6d 0x83 0x02 0x04 0x0d                   m....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 PumpSuspend 2013-06-04T12:27:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-04T12:27:39)
    0000   0x67 0x9b 0x0c 0x04 0x0d                   g....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 37 PumpResume 2013-06-04T12:52:12 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-04T12:52:12)
    0000   0x4c 0xb4 0x0c 0x04 0x0d                   L....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 38 Rewind 2013-06-04T12:52:17 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-06-04T12:52:17)
    0000   0x51 0xb4 0x0c 0x04 0x0d                   Q....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 39 Prime 2013-06-04T12:54:17 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x08                   .....
    decimal
              3    0    0    0    8
    datetime (2013-06-04T12:54:17)
    0000   0x51 0xb6 0x2c 0x04 0x0d                   Q.,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 40 Prime 2013-06-04T12:54:34 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-06-04T12:54:34)
    0000   0x62 0xb6 0x0c 0x04 0x0d                   b....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 41 CalBGForPH 2013-06-04T13:26:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-06-04T13:26:23)
    0000   0x57 0x9a 0x2d 0x04 0x0d                   W.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 BolusWizard 2013-06-04T13:26:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
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
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-06-04T13:26:34)
    0000   0x62 0x9a 0x0d 0x04 0x0d                   b....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125
    HOUR BITS: [1, 0, 0]
#### RECORD 43 Bolus 2013-06-04T13:26:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-06-04T13:26:34)
    0000   0x62 0x9a 0x4d 0x04 0x0d                   b.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 44 CalBGForPH 2013-06-04T13:54:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-06-04T13:54:19)
    0000   0x53 0xb6 0x2d 0x04 0x0d                   S.-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 45 BolusWizard 2013-06-04T13:55:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.7,
 'carb_input': 75,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 5.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-06-04T13:55:00)
    0000   0x40 0xb7 0x0d 0x04 0x0d                   @....
    body (13)
    hex
    0000   0x4b 0x50 0x0d 0x2d 0x6a 0x0a 0x39 0x00    KP.-j.9.
    0008   0x00 0x0c 0x00 0x39 0x7d                   ...9}
    decimal
             75   80   13   45  106   10   57    0
              0   12    0   57  125
    HOUR BITS: [1, 0, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 1.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0x1f 0x04                   \.0..
    decimal
             92    5   48   31    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-06-04T13:55:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.7, 'dual_component': '??', 'programmed': 5.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x39 0x39 0x00                        .99.
    decimal
              1   57   57    0
    datetime (2013-06-04T13:55:00)
    0000   0x40 0xb7 0x4d 0x04 0x0d                   @.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 48 CalBGForPH 2013-06-04T16:12:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-06-04T16:12:43)
    0000   0x6b 0x8c 0x30 0x04 0x0d                   k.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 49 CalBGForPH 2013-06-04T20:56:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-06-04T20:56:07)
    0000   0x47 0xb8 0x34 0x04 0x0d                   G.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 50 BolusWizard 2013-06-04T20:56:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
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
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-06-04T20:56:20)
    0000   0x54 0xb8 0x14 0x04 0x0d                   T....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x01 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106    1    0    0
              0    0    0    1  125
    HOUR BITS: [1, 0, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 166, 'amount': 5.7, 'curve': 20},
 {'age': 196, 'amount': 1.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xe4 0xa6 0x14 0x30 0xc4 0x14    \....0..
    decimal
             92    8  228  166   20   48  196   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-06-04T20:56:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-06-04T20:56:20)
    0000   0x54 0xb8 0x54 0x04 0x0d                   T.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 53 CalBGForPH 2013-06-04T21:42:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-06-04T21:42:49)
    0000   0x71 0xaa 0x35 0x04 0x0d                   q.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 54 BolusWizard 2013-06-04T21:44:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 5,
 '_byte[7]': 0,
 'bg': 151,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.3,
 'carb_input': 79,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 6.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x97                                  [.
    decimal
             91  151
    datetime (2013-06-04T21:44:34)
    0000   0x62 0xac 0x15 0x04 0x0d                   b....
    body (13)
    hex
    0000   0x4f 0x50 0x0d 0x2d 0x6a 0x05 0x3c 0x00    OP.-j.<.
    0008   0x00 0x02 0x00 0x3f 0x7d                   ...?}
    decimal
             79   80   13   45  106    5   60    0
              0    2    0   63  125
    HOUR BITS: [1, 0, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 0.2, 'curve': 4},
 {'age': 214, 'amount': 5.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x08 0x32 0x04 0xe4 0xd6 0x14    \..2....
    decimal
             92    8    8   50    4  228  214   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-06-04T21:44:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.3, 'dual_component': '??', 'programmed': 6.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3f 0x3f 0x00                        .??.
    decimal
              1   63   63    0
    datetime (2013-06-04T21:44:34)
    0000   0x62 0xac 0x55 0x04 0x0d                   b.U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 57 MResultTotals 2013-06-05T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-06-05T00:00:00)
    0000   0x00 0x05 0x88 0x64 0x0d                   ...d.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 58 Model522ResultTotals 2013-06-05T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-05T00:00:00)
    0000   0x64 0x0d                                  d.
    body (41)
    hex
    0000   0x05 0x00 0x8d 0x52 0xab 0x05 0x00 0x00    ...R....
    0008   0x05 0x88 0x03 0x70 0x3e 0x02 0x18 0x26    ...p>..&
    0010   0x00 0x9a 0x02 0x18 0x26 0x01 0xd4 0x57    ....&..W
    0018   0x00 0x44 0x0d 0x00 0x00 0x00 0x04 0x01    .D......
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  141   82  171    5    0    0
              5  136    3  112   62    2   24   38
              0  154    2   24   38    1  212   87
              0   68   13    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0

#### RECORD 59 CalBGForPH 2013-06-05T00:37:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-06-05T00:37:27)
    0000   0x5b 0xa5 0x20 0x05 0x0d                   [. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 60 PumpSuspend 2013-06-05T14:41:46 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-05T14:41:46)
    0000   0x6e 0xa9 0x0e 0x05 0x0d                   n....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 61 PumpResume 2013-06-05T15:03:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-05T15:03:20)
    0000   0x54 0x83 0x0f 0x05 0x0d                   T....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 CalBGForPH 2013-06-05T16:03:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-06-05T16:03:22)
    0000   0x56 0x83 0x30 0x05 0x0d                   V.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 BolusWizard 2013-06-05T16:03:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-06-05T16:03:43)
    0000   0x6b 0x83 0x10 0x05 0x0d                   k....
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0xf9 0x24 0xf0    0P.-j.$.
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
             48   80   13   45  106  249   36  240
              0    0    0   29  125
    HOUR BITS: [1, 0, 0]
#### RECORD 64 Bolus 2013-06-05T16:03:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-06-05T16:03:43)
    0000   0x6b 0x83 0x50 0x05 0x0d                   k.P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 65 BolusWizard 2013-06-05T16:08:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.8,
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
    datetime (2013-06-05T16:08:02)
    0000   0x42 0x88 0x10 0x05 0x0d                   B....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x00 0x1c 0x00    %P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106    0   28    0
              0    0    0   28  125
    HOUR BITS: [1, 0, 0]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 2.45, 'curve': 4},
 {'age': 14, 'amount': 0.45, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x62 0x04 0x04 0x12 0x0e 0x04    \.b.....
    decimal
             92    8   98    4    4   18   14    4
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-06-05T16:08:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-06-05T16:08:02)
    0000   0x42 0x88 0x50 0x05 0x0d                   B.P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 68 CalBGForPH 2013-06-05T18:12:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-06-05T18:12:17)
    0000   0x51 0x8c 0x32 0x05 0x0d                   Q.2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 CalBGForPH 2013-06-05T19:53:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-06-05T19:53:00)
    0000   0x40 0xb5 0x33 0x05 0x0d                   @.3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 70 BolusWizard 2013-06-05T19:53:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-06-05T19:53:44)
    0000   0x6c 0xb5 0x13 0x05 0x0d                   l....
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    0P.-j.$.
    0008   0x00 0x04 0x00 0x24 0x7d                   ...$}
    decimal
             48   80   13   45  106    0   36    0
              0    4    0   36  125
    HOUR BITS: [1, 0, 1]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 229, 'amount': 5.25, 'curve': 4},
 {'age': 239, 'amount': 0.45, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xd2 0xe5 0x04 0x12 0xef 0x04    \.......
    decimal
             92    8  210  229    4   18  239    4
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-06-05T19:53:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-06-05T19:53:44)
    0000   0x6c 0xb5 0x53 0x05 0x0d                   l.S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 73 MResultTotals 2013-06-06T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-06-06T00:00:00)
    0000   0x00 0x04 0xea 0x65 0x0d                   ...e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 74 Model522ResultTotals 2013-06-06T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-06T00:00:00)
    0000   0x65 0x0d                                  e.
    body (41)
    hex
    0000   0x05 0x00 0x60 0x4b 0x70 0x04 0x00 0x00    ..`Kp...
    0008   0x04 0xea 0x03 0x76 0x46 0x01 0x74 0x1e    ...vF.t.
    0010   0x00 0x85 0x01 0x74 0x1e 0x01 0x74 0x64    ...t..td
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   96   75  112    4    0    0
              4  234    3  118   70    1  116   30
              0  133    1  116   30    1  116  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0

#### RECORD 75 PumpSuspend 2013-06-06T09:56:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-06T09:56:30)
    0000   0x5e 0xb8 0x09 0x06 0x0d                   ^....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 76 PumpResume 2013-06-06T10:53:34 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-06T10:53:34)
    0000   0x62 0xb5 0x0a 0x06 0x0d                   b....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 77 CalBGForPH 2013-06-06T10:53:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 295}
```
    op hex (2)
    0000   0x0a 0x27                                  .'
    decimal
             10   39
    datetime (2013-06-06T10:53:50)
    0000   0x72 0xb5 0x2a 0x06 0x8d                   r.*..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 78 BolusWizard 2013-06-06T10:53:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 37,
 '_byte[7]': 0,
 'bg': 295,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x27                                  ['
    decimal
             91   39
    datetime (2013-06-06T10:53:52)
    0000   0x74 0xb5 0x0a 0x06 0x0d                   t....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x25 0x00 0x00    .Q.-j%..
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
              0   81   13   45  106   37    0    0
              0    0    0   37  125
    HOUR BITS: [1, 0, 1]
#### RECORD 79 Bolus 2013-06-06T10:53:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'dual_component': '??', 'programmed': 3.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2013-06-06T10:53:52)
    0000   0x74 0xb5 0x4a 0x06 0x0d                   t.J..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 80 CalBGForPH 2013-06-06T12:11:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 242}
```
    op hex (2)
    0000   0x0a 0xf2                                  ..
    decimal
             10  242
    datetime (2013-06-06T12:11:34)
    0000   0x62 0x8b 0x2c 0x06 0x0d                   b.,..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 81 BolusWizard 2013-06-06T12:11:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 242,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf2                                  [.
    decimal
             91  242
    datetime (2013-06-06T12:11:45)
    0000   0x6d 0x8b 0x0c 0x06 0x0d                   m....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x1b 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0   27    0    0  125
    HOUR BITS: [1, 0, 0]
#### RECORD 82 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 77, 'amount': 3.5, 'curve': 4},
 {'age': 87, 'amount': 0.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x8c 0x4d 0x04 0x08 0x57 0x04    \..M..W.
    decimal
             92    8  140   77    4    8   87    4
    datetime (unknown)

    body (0)

#### RECORD 83 Bolus 2013-06-06T12:11:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x01 0x01 0x00                        ....
    decimal
              1    1    1    0
    datetime (2013-06-06T12:11:46)
    0000   0x6e 0x8b 0x4c 0x06 0x0d                   n.L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 84 CalBGForPH 2013-06-06T12:28:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 235}
```
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2013-06-06T12:28:46)
    0000   0x6e 0x9c 0x2c 0x06 0x0d                   n.,..
    body (0)
    HOUR BITS: [1, 0, 0]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-14.data: 85 records`
