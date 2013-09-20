## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-5.data
#### RECORD 0 PumpSuspend 2013-07-15T13:57:04 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-15T13:57:04)
    0000   0x44 0xf9 0x0d 0x0f 0x0d                   D....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 PumpResume 2013-07-15T14:18:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-15T14:18:33)
    0000   0x61 0xd2 0x0e 0x0f 0x0d                   a....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 CalBGForPH 2013-07-15T16:21:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-07-15T16:21:20)
    0000   0x54 0xd5 0x30 0x0f 0x0d                   T.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BolusWizard 2013-07-15T16:21:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 160,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2013-07-15T16:21:32)
    0000   0x60 0xd5 0x10 0x0f 0x0d                   `....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x07 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             28   80   13   45  106    7   21    0
              0    0    0   28  125
    HOUR BITS: [1, 1, 0]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 3.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x94 0xd3 0x14                   \....
    decimal
             92    5  148  211   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-07-15T16:21:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-07-15T16:21:32)
    0000   0x60 0xd5 0x50 0x0f 0x0d                   `.P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2013-07-15T21:55:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-07-15T21:55:51)
    0000   0x73 0xf7 0x35 0x0f 0x0d                   s.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 BolusWizard 2013-07-15T21:56:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.1,
 'carb_input': 66,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 5.0,
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
    datetime (2013-07-15T21:56:12)
    0000   0x4c 0xf8 0x15 0x0f 0x0d                   L....
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0x01 0x32 0x00    BP.-j.2.
    0008   0x00 0x00 0x00 0x33 0x7d                   ...3}
    decimal
             66   80   13   45  106    1   50    0
              0    0    0   51  125
    HOUR BITS: [1, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 2.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0x56 0x14                   \.pV.
    decimal
             92    5  112   86   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-07-15T21:56:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1, 'dual_component': '??', 'programmed': 5.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x33 0x33 0x00                        .33.
    decimal
              1   51   51    0
    datetime (2013-07-15T21:56:12)
    0000   0x4c 0xf8 0x55 0x0f 0x0d                   L.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 MResultTotals (2013, 0, 15, 30, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 15, 30, 5, 0))
    0000   0x00 0x05 0xbe 0x6f 0x8d                   ...o.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 11 Model522ResultTotals 2013-07-16T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-16T00:00:00)
    0000   0x6f 0x8d                                  o.
    body (41)
    hex
    0000   0x05 0x10 0xdd 0x82 0x2d 0x04 0x00 0x00    ....-...
    0008   0x05 0xbe 0x03 0x76 0x3c 0x02 0x48 0x28    ...v<.H(
    0010   0x00 0x5e 0x02 0x48 0x28 0x01 0x1c 0x31    .^.H(..1
    0018   0x01 0x2c 0x33 0x00 0x00 0x00 0x04 0x00    .,3.....
    0020   0x02 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  221  130   45    4    0    0
              5  190    3  118   60    2   72   40
              0   94    2   72   40    1   28   49
              1   44   51    0    0    0    4    0
              2    2    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 12 PumpSuspend 2013-07-16T08:46:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-16T08:46:05)
    0000   0x45 0xee 0x08 0x10 0x0d                   E....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 PumpResume 2013-07-16T08:47:56 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-16T08:47:56)
    0000   0x78 0xef 0x08 0x10 0x0d                   x....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 CalBGForPH 2013-07-16T10:21:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 291}
```
    op hex (2)
    0000   0x0a 0x23                                  .#
    decimal
             10   35
    datetime (2013-07-16T10:21:17)
    0000   0x51 0xd5 0x2a 0x10 0x8d                   Q.*..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 BolusWizard 2013-07-16T10:21:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 291,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
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
    0000   0x5b 0x23                                  [#
    decimal
             91   35
    datetime (2013-07-16T10:21:27)
    0000   0x5b 0xd5 0x0a 0x10 0x0d                   [....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
              0   81   13   45  106   36    0    0
              0    0    0   36  125
    HOUR BITS: [1, 1, 0]
#### RECORD 16 Bolus 2013-07-16T10:21:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-07-16T10:21:27)
    0000   0x5b 0xd5 0x4a 0x10 0x0d                   [.J..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 PumpSuspend 2013-07-16T13:36:23 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-16T13:36:23)
    0000   0x57 0xe4 0x0d 0x10 0x0d                   W....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 PumpResume 2013-07-16T13:51:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-16T13:51:33)
    0000   0x61 0xf3 0x0d 0x10 0x0d                   a....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 CalBGForPH 2013-07-16T22:21:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-16T22:21:41)
    0000   0x69 0xd5 0x36 0x10 0x0d                   i.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 BolusWizard 2013-07-16T22:22:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 102,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 4.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-07-16T22:22:44)
    0000   0x6c 0xd6 0x16 0x10 0x0d                   l....
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0xff 0x2d 0xf0    ;P.-j.-.
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
             59   80   13   45  106  255   45  240
              0    0    0   44  125
    HOUR BITS: [1, 1, 0]
#### RECORD 21 Bolus 2013-07-16T22:22:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-07-16T22:22:44)
    0000   0x6c 0xd6 0x56 0x10 0x0d                   l.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 MResultTotals (2013, 0, 16, 24, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 16, 24, 4, 0))
    0000   0x00 0x04 0xb8 0x70 0x8d                   ...p.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 23 Model522ResultTotals 2013-07-17T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-17T00:00:00)
    0000   0x70 0x8d                                  p.
    body (41)
    hex
    0000   0x05 0x10 0xc5 0x66 0x23 0x02 0x00 0x00    ...f#...
    0008   0x04 0xb8 0x03 0x78 0x4a 0x01 0x40 0x1a    ...xJ.@.
    0010   0x00 0x3b 0x01 0x40 0x1a 0x00 0xb0 0x37    .;.@...7
    0018   0x00 0x90 0x2d 0x00 0x00 0x00 0x02 0x01    ..-.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  197  102   35    2    0    0
              4  184    3  120   74    1   64   26
              0   59    1   64   26    0  176   55
              0  144   45    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 24 PumpSuspend 2013-07-17T10:32:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-17T10:32:19)
    0000   0x53 0xe0 0x0a 0x11 0x0d                   S....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 PumpResume 2013-07-17T10:36:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-17T10:36:05)
    0000   0x45 0xe4 0x0a 0x11 0x0d                   E....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 PumpSuspend 2013-07-17T12:13:26 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-17T12:13:26)
    0000   0x5a 0xcd 0x0c 0x11 0x0d                   Z....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 PumpResume unknown head[1], body[0] op[0x1f]

    op hex (1)
    0000   0x1f                                       .
    decimal
             31
    datetime (unknown)

    body (0)

`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-5.data: 28 records`
