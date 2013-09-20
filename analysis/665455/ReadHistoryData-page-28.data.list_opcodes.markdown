## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-28.data
#### RECORD 0 Prime 2013-04-09T20:12:46 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-09T20:12:46)
    0000   0x6e 0x0c 0x14 0x09 0x0d                   n....
    body (0)

#### RECORD 1 CalBGForPH 2013-04-09T20:15:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 230}
```
    op hex (2)
    0000   0x0a 0xe6                                  ..
    decimal
             10  230
    datetime (2013-04-09T20:15:05)
    0000   0x45 0x0f 0x34 0x09 0x0d                   E.4..
    body (0)

#### RECORD 2 BolusWizard 2013-04-09T20:15:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 230,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 2.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe6                                  [.
    decimal
             91  230
    datetime (2013-04-09T20:15:28)
    0000   0x5c 0x0f 0x14 0x09 0x0d                   \....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x17 0x1c 0x00    %P.-j...
    0008   0x00 0x16 0x00 0x1d 0x7d                   ....}
    decimal
             37   80   13   45  106   23   28    0
              0   22    0   29  125

#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 2.0, 'curve': 4},
 {'age': 131, 'amount': 0.5, 'curve': 4},
 {'age': 5, 'amount': 2.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x15 0x04 0x14 0x83 0x04    \.P.....
    0008   0x68 0x05 0x14                             h..
    decimal
             92   11   80   21    4   20  131    4
            104    5   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-04-09T20:15:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-04-09T20:15:28)
    0000   0x5c 0x0f 0x54 0x09 0x0d                   \.T..
    body (0)

#### RECORD 5 MResultTotals 2013-04-10T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xac                   .....
    decimal
              7    0    0    4  172
    datetime (2013-04-10T00:00:00)
    0000   0x49 0x0d                                  I.
    body (0)

#### RECORD 6 Model522ResultTotals 2013-04-10T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-10T00:00:00)
    0000   0x49 0x0d                                  I.
    body (41)
    hex
    0000   0x05 0x00 0xc8 0x5b 0xf7 0x05 0x00 0x00    ...[....
    0008   0x04 0xac 0x03 0x6c 0x49 0x01 0x40 0x1b    ...lI.@.
    0010   0x00 0x4c 0x01 0x40 0x1b 0x00 0xd8 0x43    .L.@...C
    0018   0x00 0x68 0x21 0x00 0x00 0x00 0x04 0x01    .h!.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  200   91  247    5    0    0
              4  172    3  108   73    1   64   27
              0   76    1   64   27    0  216   67
              0  104   33    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0

#### RECORD 7 PumpSuspend 2013-04-10T12:52:16 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-10T12:52:16)
    0000   0x50 0x34 0x0c 0x0a 0x0d                   P4...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 PumpResume 2013-04-10T13:15:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-10T13:15:20)
    0000   0x54 0x0f 0x0d 0x0a 0x0d                   T....
    body (0)

#### RECORD 9 CalBGForPH 2013-04-10T14:26:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-04-10T14:26:56)
    0000   0x78 0x1a 0x2e 0x0a 0x0d                   x....
    body (0)

#### RECORD 10 BolusWizard 2013-04-10T14:27:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 72,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 4.5,
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
    datetime (2013-04-10T14:27:27)
    0000   0x5b 0x1b 0x0e 0x0a 0x0d                   [....
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0xf8 0x2d 0xf0    ;P.-j.-.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             59   80   13   45  106  248   45  240
              0    0    0   37  125

#### RECORD 11 Bolus 2013-04-10T14:27:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'dual_component': '??', 'programmed': 3.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2013-04-10T14:27:27)
    0000   0x5b 0x1b 0x4e 0x0a 0x0d                   [.N..
    body (0)

#### RECORD 12 CalBGForPH 2013-04-10T15:55:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 228}
```
    op hex (2)
    0000   0x0a 0xe4                                  ..
    decimal
             10  228
    datetime (2013-04-10T15:55:56)
    0000   0x78 0x37 0x2f 0x0a 0x0d                   x7/..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 BolusWizard 2013-04-10T15:56:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 228,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe4                                  [.
    decimal
             91  228
    datetime (2013-04-10T15:56:08)
    0000   0x48 0x38 0x0f 0x0a 0x0d                   H8...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0   24    0    0  125
    HOUR BITS: [0, 0, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 3.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x94 0x5c 0x04                   \..\.
    decimal
             92    5  148   92    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-04-10T15:56:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-04-10T15:56:08)
    0000   0x48 0x38 0x4f 0x0a 0x0d                   H8O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 16 CalBGForPH 2013-04-10T17:07:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 224}
```
    op hex (2)
    0000   0x0a 0xe0                                  ..
    decimal
             10  224
    datetime (2013-04-10T17:07:09)
    0000   0x49 0x07 0x31 0x0a 0x0d                   I.1..
    body (0)

#### RECORD 17 BolusWizard 2013-04-10T17:07:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 224,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe0                                  [.
    decimal
             91  224
    datetime (2013-04-10T17:07:12)
    0000   0x4c 0x07 0x11 0x0a 0x0d                   L....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0   11    0   11  125

#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 0.2, 'curve': 4},
 {'age': 163, 'amount': 3.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x08 0x49 0x04 0x94 0xa3 0x04    \..I....
    decimal
             92    8    8   73    4  148  163    4
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-04-10T17:07:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-04-10T17:07:13)
    0000   0x4d 0x07 0x51 0x0a 0x0d                   M.Q..
    body (0)

#### RECORD 20 CalBGForPH 2013-04-10T18:26:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 150}
```
    op hex (2)
    0000   0x0a 0x96                                  ..
    decimal
             10  150
    datetime (2013-04-10T18:26:45)
    0000   0x6d 0x1a 0x32 0x0a 0x0d                   m.2..
    body (0)

#### RECORD 21 CalBGForPH 2013-04-10T18:40:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2013-04-10T18:40:16)
    0000   0x50 0x28 0x32 0x0a 0x0d                   P(2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 BolusWizard 2013-04-10T18:40:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 142,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 1.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2013-04-10T18:40:38)
    0000   0x66 0x28 0x12 0x0a 0x0d                   f(...
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x03 0x0a 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    3   10    0
              0    9    0   10  125
    HOUR BITS: [0, 0, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 1.3, 'curve': 4},
 {'age': 166, 'amount': 0.2, 'curve': 4},
 {'age': 0, 'amount': 3.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x60 0x04 0x08 0xa6 0x04    \.4`....
    0008   0x94 0x00 0x14                             ...
    decimal
             92   11   52   96    4    8  166    4
            148    0   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-04-10T18:40:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-04-10T18:40:38)
    0000   0x66 0x28 0x52 0x0a 0x0d                   f(R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 25 CalBGForPH 2013-04-10T20:17:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 289}
```
    op hex (2)
    0000   0x0a 0x21                                  .!
    decimal
             10   33
    datetime (2013-04-10T20:17:43)
    0000   0x6b 0x11 0x34 0x0a 0x8d                   k.4..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 BolusWizard 2013-04-10T20:17:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 289,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x21                                  [!
    decimal
             91   33
    datetime (2013-04-10T20:17:44)
    0000   0x6c 0x11 0x14 0x0a 0x0d                   l....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x08 0x00 0x1c 0x7d                   ....}
    decimal
              0   81   13   45  106   36    0    0
              0    8    0   28  125

#### RECORD 27 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 1.0, 'curve': 4},
 {'age': 193, 'amount': 1.3, 'curve': 4},
 {'age': 7, 'amount': 0.2, 'curve': 20},
 {'age': 97, 'amount': 3.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x67 0x04 0x34 0xc1 0x04    \.(g.4..
    0008   0x08 0x07 0x14 0x94 0x61 0x14              ....a.
    decimal
             92   14   40  103    4   52  193    4
              8    7   20  148   97   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-04-10T20:17:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-04-10T20:17:44)
    0000   0x6c 0x11 0x54 0x0a 0x0d                   l.T..
    body (0)

#### RECORD 29 CalBGForPH 2013-04-10T21:43:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-04-10T21:43:44)
    0000   0x6c 0x2b 0x35 0x0a 0x0d                   l+5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 CalBGForPH 2013-04-10T23:07:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-04-10T23:07:41)
    0000   0x69 0x07 0x37 0x0a 0x0d                   i.7..
    body (0)

#### RECORD 31 BolusWizard 2013-04-10T23:08:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 95,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2013-04-10T23:08:06)
    0000   0x46 0x08 0x17 0x0a 0x0d                   F....
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0xfd 0x1a 0xf0    #P.-j...
    0008   0x00 0x06 0x00 0x17 0x7d                   ....}
    decimal
             35   80   13   45  106  253   26  240
              0    6    0   23  125

#### RECORD 32 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 174, 'amount': 2.8, 'curve': 4},
 {'age': 18, 'amount': 1.0, 'curve': 20},
 {'age': 108, 'amount': 1.3, 'curve': 20},
 {'age': 178, 'amount': 0.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x70 0xae 0x04 0x28 0x12 0x14    \.p..(..
    0008   0x34 0x6c 0x14 0x08 0xb2 0x14              4l....
    decimal
             92   14  112  174    4   40   18   20
             52  108   20    8  178   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-04-10T23:08:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-04-10T23:08:07)
    0000   0x47 0x08 0x57 0x0a 0x0d                   G.W..
    body (0)

#### RECORD 34 MResultTotals 2013-04-11T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x38                   ....8
    decimal
              7    0    0    5   56
    datetime (2013-04-11T00:00:00)
    0000   0x4a 0x0d                                  J.
    body (0)

#### RECORD 35 Model522ResultTotals 2013-04-11T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-11T00:00:00)
    0000   0x4a 0x0d                                  J.
    body (41)
    hex
    0000   0x05 0x10 0xa5 0x48 0x21 0x08 0x00 0x00    ...H!...
    0008   0x05 0x38 0x03 0x74 0x42 0x01 0xc4 0x22    .8.tB.."
    0010   0x00 0x6b 0x01 0xc4 0x22 0x01 0x18 0x3e    .k.."..>
    0018   0x00 0xac 0x26 0x00 0x00 0x00 0x06 0x03    ..&.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  165   72   33    8    0    0
              5   56    3  116   66    1  196   34
              0  107    1  196   34    1   24   62
              0  172   38    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0

#### RECORD 36 CalBGForPH 2013-04-11T07:16:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 374}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-04-11T07:16:35)
    0000   0x63 0x10 0x27 0x0b 0x8d                   c.'..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 BolusWizard 2013-04-11T07:16:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 55,
 '_byte[7]': 0,
 'bg': 374,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.5,
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
    0000   0x5b 0x76                                  [v
    decimal
             91  118
    datetime (2013-04-11T07:16:37)
    0000   0x65 0x10 0x07 0x0b 0x0d                   e....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x37 0x00 0x00    .Q.-j7..
    0008   0x00 0x00 0x00 0x37 0x7d                   ...7}
    decimal
              0   81   13   45  106   55    0    0
              0    0    0   55  125

#### RECORD 38 Bolus 2013-04-11T07:16:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5, 'dual_component': '??', 'programmed': 5.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x37 0x37 0x00                        .77.
    decimal
              1   55   55    0
    datetime (2013-04-11T07:16:37)
    0000   0x65 0x10 0x47 0x0b 0x0d                   e.G..
    body (0)

#### RECORD 39 PumpSuspend 2013-04-11T08:58:54 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-11T08:58:54)
    0000   0x76 0x3a 0x08 0x0b 0x0d                   v:...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 PumpResume 2013-04-11T09:27:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-11T09:27:20)
    0000   0x54 0x1b 0x09 0x0b 0x0d                   T....
    body (0)

#### RECORD 41 CalBGForPH 2013-04-11T11:11:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2013-04-11T11:11:40)
    0000   0x68 0x0b 0x2b 0x0b 0x0d                   h.+..
    body (0)

#### RECORD 42 CalBGForPH 2013-04-11T13:02:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-04-11T13:02:42)
    0000   0x6a 0x02 0x2d 0x0b 0x0d                   j.-..
    body (0)

#### RECORD 43 CalBGForPH 2013-04-11T13:03:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2013-04-11T13:03:11)
    0000   0x4b 0x03 0x2d 0x0b 0x0d                   K.-..
    body (0)

#### RECORD 44 BolusWizard 2013-04-11T13:03:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 94,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5e                                  [^
    decimal
             91   94
    datetime (2013-04-11T13:03:45)
    0000   0x6d 0x03 0x0d 0x0b 0x0d                   m....
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0xfd 0x2d 0xf0    ;P.-j.-.
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
             59   80   13   45  106  253   45  240
              0    0    0   42  125

#### RECORD 45 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 5.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xdc 0x5d 0x14                   \..].
    decimal
             92    5  220   93   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-04-11T13:03:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-04-11T13:03:45)
    0000   0x6d 0x03 0x4d 0x0b 0x0d                   m.M..
    body (0)

#### RECORD 47 CalBGForPH 2013-04-11T14:11:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-04-11T14:11:42)
    0000   0x6a 0x0b 0x2e 0x0b 0x0d                   j....
    body (0)

#### RECORD 48 CalBGForPH 2013-04-11T14:12:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-04-11T14:12:36)
    0000   0x64 0x0c 0x2e 0x0b 0x0d                   d....
    body (0)

#### RECORD 49 BolusWizard 2013-04-11T14:12:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 1.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-04-11T14:12:55)
    0000   0x77 0x0c 0x0e 0x0b 0x0d                   w....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0xf9 0x0b 0xf0    .P.-j...
    0008   0x00 0x21 0x00 0x04 0x7d                   .!..}
    decimal
             15   80   13   45  106  249   11  240
              0   33    0    4  125

#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 3.85, 'curve': 4},
 {'age': 78, 'amount': 0.35, 'curve': 4},
 {'age': 162, 'amount': 5.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x9a 0x44 0x04 0x0e 0x4e 0x04    \..D..N.
    0008   0xdc 0xa2 0x14                             ...
    decimal
             92   11  154   68    4   14   78    4
            220  162   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-04-11T14:12:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-04-11T14:12:55)
    0000   0x77 0x0c 0x4e 0x0b 0x0d                   w.N..
    body (0)

#### RECORD 52 CalBGForPH 2013-04-11T18:40:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2013-04-11T18:40:29)
    0000   0x5d 0x28 0x32 0x0b 0x0d                   ](2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 53 BolusWizard 2013-04-11T18:40:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 155,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2013-04-11T18:40:32)
    0000   0x60 0x28 0x12 0x0b 0x0d                   `(...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    0    0    6  125
    HOUR BITS: [0, 0, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 0.4, 'curve': 20},
 {'age': 80, 'amount': 3.85, 'curve': 20},
 {'age': 90, 'amount': 0.35, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0x14 0x14 0x9a 0x50 0x14    \.....P.
    0008   0x0e 0x5a 0x14                             .Z.
    decimal
             92   11   16   20   20  154   80   20
             14   90   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-04-11T18:40:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-04-11T18:40:32)
    0000   0x60 0x28 0x52 0x0b 0x0d                   `(R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 CalBGForPH 2013-04-11T19:58:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-04-11T19:58:30)
    0000   0x5e 0x3a 0x33 0x0b 0x0d                   ^:3..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 CalBGForPH 2013-04-11T20:00:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-04-11T20:00:46)
    0000   0x6e 0x00 0x34 0x0b 0x0d                   n.4..
    body (0)

#### RECORD 58 CalBGForPH 2013-04-11T20:01:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-04-11T20:01:04)
    0000   0x44 0x01 0x34 0x0b 0x0d                   D.4..
    body (0)

#### RECORD 59 BolusWizard 2013-04-11T20:01:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-04-11T20:01:12)
    0000   0x4c 0x01 0x14 0x0b 0x0d                   L....
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    "P.-j...
    0008   0x00 0x04 0x00 0x1a 0x7d                   ....}
    decimal
             34   80   13   45  106    0   26    0
              0    4    0   26  125

#### RECORD 60 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 87, 'amount': 0.6, 'curve': 4},
 {'age': 101, 'amount': 0.4, 'curve': 20},
 {'age': 161, 'amount': 3.85, 'curve': 20},
 {'age': 171, 'amount': 0.35, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x57 0x04 0x10 0x65 0x14    \..W..e.
    0008   0x9a 0xa1 0x14 0x0e 0xab 0x14              ......
    decimal
             92   14   24   87    4   16  101   20
            154  161   20   14  171   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-04-11T20:01:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-04-11T20:01:12)
    0000   0x4c 0x01 0x54 0x0b 0x0d                   L.T..
    body (0)

#### RECORD 62 MResultTotals 2013-04-12T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x86                   .....
    decimal
              7    0    0    5  134
    datetime (2013-04-12T00:00:00)
    0000   0x4b 0x0d                                  K.
    body (0)

#### RECORD 63 Model522ResultTotals 2013-04-12T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-12T00:00:00)
    0000   0x4b 0x0d                                  K.
    body (41)
    hex
    0000   0x05 0x10 0x89 0x4b 0x76 0x0a 0x00 0x00    ...Kv...
    0008   0x05 0x86 0x03 0x72 0x3e 0x02 0x14 0x26    ...r>..&
    0010   0x00 0x6c 0x02 0x14 0x26 0x01 0x20 0x36    .l..&. 6
    0018   0x00 0xf4 0x2e 0x00 0x00 0x00 0x05 0x03    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  137   75  118   10    0    0
              5  134    3  114   62    2   20   38
              0  108    2   20   38    1   32   54
              0  244   46    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0

#### RECORD 64 PumpSuspend 2013-04-12T12:02:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-12T12:02:30)
    0000   0x5e 0x02 0x0c 0x0c 0x0d                   ^....
    body (0)

#### RECORD 65 PumpResume 2013-04-12T12:21:17 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-12T12:21:17)
    0000   0x51 0x15 0x0c 0x0c 0x0d                   Q....
    body (0)

#### RECORD 66 CalBGForPH 2013-04-12T13:50:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-04-12T13:50:55)
    0000   0x77 0x32 0x2d 0x0c 0x0d                   w2-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 67 BolusWizard 2013-04-12T13:51:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-04-12T13:51:13)
    0000   0x4d 0x33 0x0d 0x0c 0x0d                   M3...
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x00 0x2a 0x00    7P.-j.*.
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    0   42    0
              0    0    0   42  125
    HOUR BITS: [0, 0, 1]
#### RECORD 68 Bolus 2013-04-12T13:51:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-04-12T13:51:13)
    0000   0x4d 0x33 0x4d 0x0c 0x0d                   M3M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 CalBGForPH 2013-04-12T15:15:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-04-12T15:15:26)
    0000   0x5a 0x0f 0x2f 0x0c 0x0d                   Z./..
    body (0)

#### RECORD 70 BolusWizard 2013-04-12T15:15:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 9,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-04-12T15:15:37)
    0000   0x65 0x0f 0x0f 0x0c 0x0d                   e....
    body (13)
    hex
    0000   0x09 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x1b 0x00 0x06 0x7d                   ....}
    decimal
              9   80   13   45  106    0    6    0
              0   27    0    6  125

#### RECORD 71 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 81, 'amount': 0.05, 'curve': 4},
 {'age': 91, 'amount': 4.15, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x02 0x51 0x04 0xa6 0x5b 0x04    \..Q..[.
    decimal
             92    8    2   81    4  166   91    4
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-04-12T15:15:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-04-12T15:15:37)
    0000   0x65 0x0f 0x4f 0x0c 0x0d                   e.O..
    body (0)

#### RECORD 73 BolusWizard 2013-04-12T15:49:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.5,
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
    datetime (2013-04-12T15:49:59)
    0000   0x7b 0x31 0x0f 0x0c 0x0d                   {1...
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x00 0x05 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
              7   80   13   45  106    0    5    0
              0    0    0    5  125
    HOUR BITS: [0, 0, 1]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 0.6, 'curve': 4},
 {'age': 115, 'amount': 0.05, 'curve': 4},
 {'age': 125, 'amount': 4.15, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x18 0x23 0x04 0x02 0x73 0x04    \..#..s.
    0008   0xa6 0x7d 0x04                             .}.
    decimal
             92   11   24   35    4    2  115    4
            166  125    4
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2013-04-12T15:49:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-04-12T15:49:59)
    0000   0x7b 0x31 0x4f 0x0c 0x0d                   {1O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 76 CalBGForPH 2013-04-12T21:51:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2013-04-12T21:51:16)
    0000   0x50 0x33 0x35 0x0c 0x0d                   P35..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 77 BolusWizard 2013-04-12T21:51:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 157,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.4,
 'carb_input': 75,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 5.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9d                                  [.
    decimal
             91  157
    datetime (2013-04-12T21:51:39)
    0000   0x67 0x33 0x15 0x0c 0x0d                   g3...
    body (13)
    hex
    0000   0x4b 0x50 0x0d 0x2d 0x6a 0x07 0x39 0x00    KP.-j.9.
    0008   0x00 0x00 0x00 0x40 0x7d                   ...@}
    decimal
             75   80   13   45  106    7   57    0
              0    0    0   64  125
    HOUR BITS: [0, 0, 1]
#### RECORD 78 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 0.5, 'curve': 20},
 {'age': 141, 'amount': 0.6, 'curve': 20},
 {'age': 221, 'amount': 0.05, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x6f 0x14 0x18 0x8d 0x14    \..o....
    0008   0x02 0xdd 0x14                             ...
    decimal
             92   11   20  111   20   24  141   20
              2  221   20
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2013-04-12T21:51:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.4, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x40 0x40 0x00                        .@@.
    decimal
              1   64   64    0
    datetime (2013-04-12T21:51:40)
    0000   0x68 0x33 0x55 0x0c 0x0d                   h3U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 80 CalBGForPH 2013-04-12T22:24:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 147}
```
    op hex (2)
    0000   0x0a 0x93                                  ..
    decimal
             10  147
    datetime (2013-04-12T22:24:31)
    0000   0x5f 0x18 0x36 0x0c 0x0d                   _.6..
    body (0)

#### RECORD 81 LowReservoir 2013-04-12T23:47:22 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-04-12T23:47:22)
    0000   0x56 0x2f 0x17 0x0c 0x0d                   V/...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 82 MResultTotals 2013-04-13T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x4a                   ....J
    decimal
              7    0    0    5   74
    datetime (2013-04-13T00:00:00)
    0000   0x4c 0x0d                                  L.
    body (0)

#### RECORD 83 Model522ResultTotals 2013-04-13T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-13T00:00:00)
    0000   0x4c 0x0d                                  L.
    body (41)
    hex
    0000   0x05 0x00 0x83 0x6c 0x9d 0x04 0x00 0x00    ...l....
    0008   0x05 0x4a 0x03 0x76 0x41 0x01 0xd4 0x23    .J.vA..#
    0010   0x00 0x92 0x01 0xd4 0x23 0x01 0xb8 0x5e    ....#..^
    0018   0x00 0x1c 0x06 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  131  108  157    4    0    0
              5   74    3  118   65    1  212   35
              0  146    1  212   35    1  184   94
              0   28    6    0    0    0    4    3
              0    1    0   12    0  232    0    0
              0

#### RECORD 84 Base unknown head[2], body[0] op[0x4a]

    op hex (2)
    0000   0x4a 0x9b                                  J.
    decimal
             74  155
    datetime (unknown)

    body (0)

`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-28.data: 85 records`
