## START logs/ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x63 0x30                                  c0
##### DEBUG DECIMAL
             99   48
#### RECORD 0 Prime 2013-07-09T16:01:42 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-09T16:01:42)
    0000   0x6a 0xc1 0x10 0x09 0x0d                   j....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 CalBGForPH 2013-07-09T16:29:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-07-09T16:29:30)
    0000   0x5e 0xdd 0x30 0x09 0x0d                   ^.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2013-07-09T16:29:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 14,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-07-09T16:29:36)
    0000   0x64 0xdd 0x10 0x09 0x0d                   d....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Bolus 2013-07-09T16:29:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-07-09T16:29:36)
    0000   0x64 0xdd 0x50 0x09 0x0d                   d.P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-09T22:04:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2013-07-09T22:04:59)
    0000   0x7b 0xc4 0x36 0x09 0x0d                   {.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BolusWizard 2013-07-09T22:05:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 94,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.2,
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
    datetime (2013-07-09T22:05:44)
    0000   0x6c 0xc5 0x16 0x09 0x0d                   l....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xfd 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             55   80   13   45  106  253   42  240
              0    0    0   39  125
    HOUR BITS: [1, 1, 0]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 1.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x55 0x14                   \.(U.
    decimal
             92    5   40   85   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-07-09T22:05:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-07-09T22:05:44)
    0000   0x6c 0xc5 0x56 0x09 0x0d                   l.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 ResultTotals 2013-06-09T13:13:41 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x3a                   ....:
    decimal
              7    0    0    4   58
    datetime (2013-06-09T13:13:41)
    0000   0x69 0x8d 0x6d 0x69 0x8d                   i.mi.
    body (41)
    hex
    0000   0x05 0x00 0x65 0x5e 0x6c 0x02 0x00 0x00    ..e^l...
    0008   0x04 0x3a 0x03 0x76 0x52 0x00 0xc4 0x12    .:.vR...
    0010   0x00 0x45 0x00 0xc4 0x12 0x00 0xc4 0x64    .E.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  101   94  108    2    0    0
              4   58    3  118   82    0  196   18
              0   69    0  196   18    0  196  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 PumpSuspend 2013-07-10T13:15:12 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-10T13:15:12)
    0000   0x4c 0xcf 0x0d 0x0a 0x0d                   L....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 PumpResume 2013-07-10T13:42:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-10T13:42:35)
    0000   0x63 0xea 0x0d 0x0a 0x0d                   c....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 CalBGForPH 2013-07-10T15:46:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 147}
```
    op hex (2)
    0000   0x0a 0x93                                  ..
    decimal
             10  147
    datetime (2013-07-10T15:46:58)
    0000   0x7a 0xee 0x2f 0x0a 0x0d                   z./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 12 BolusWizard 2013-07-10T15:47:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 147,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x93                                  [.
    decimal
             91  147
    datetime (2013-07-10T15:47:07)
    0000   0x47 0xef 0x0f 0x0a 0x0d                   G....
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x04 0x1a 0x00    "P.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             34   80   13   45  106    4   26    0
              0    0    0   30  125
    HOUR BITS: [1, 1, 1]
#### RECORD 13 Bolus 2013-07-10T15:47:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-07-10T15:47:07)
    0000   0x47 0xef 0x4f 0x0a 0x0d                   G.O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 BolusWizard 2013-07-10T16:49:13 head[2], body[13] op[0x5b]
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
    datetime (2013-07-10T16:49:13)
    0000   0x4d 0xf1 0x10 0x0a 0x0d                   M....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 3.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x41 0x04                   \.xA.
    decimal
             92    5  120   65    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-07-10T16:49:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-07-10T16:49:13)
    0000   0x4d 0xf1 0x50 0x0a 0x0d                   M.P..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 CalBGForPH 2013-07-10T18:12:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-07-10T18:12:42)
    0000   0x6a 0xcc 0x32 0x0a 0x0d                   j.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 CalBGForPH 2013-07-10T19:47:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-07-10T19:47:55)
    0000   0x77 0xef 0x33 0x0a 0x0d                   w.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 ResultTotals 2013-06-10T13:13:42 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x1c                   .....
    decimal
              7    0    0    4   28
    datetime (2013-06-10T13:13:42)
    0000   0x6a 0x8d 0x6d 0x6a 0x8d                   j.mj.
    body (41)
    hex
    0000   0x05 0x00 0x83 0x68 0x93 0x03 0x00 0x00    ...h....
    0008   0x04 0x1c 0x03 0x70 0x54 0x00 0xac 0x10    ...pT...
    0010   0x00 0x34 0x00 0xac 0x10 0x00 0x9c 0x5b    .4.....[
    0018   0x00 0x10 0x09 0x00 0x00 0x00 0x02 0x01    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  131  104  147    3    0    0
              4   28    3  112   84    0  172   16
              0   52    0  172   16    0  156   91
              0   16    9    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 PumpSuspend 2013-07-11T12:56:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-11T12:56:39)
    0000   0x67 0xf8 0x0c 0x0b 0x0d                   g....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 PumpResume 2013-07-11T13:26:53 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-11T13:26:53)
    0000   0x75 0xda 0x0d 0x0b 0x0d                   u....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 CalBGForPH 2013-07-11T14:16:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2013-07-11T14:16:23)
    0000   0x57 0xd0 0x2e 0x0b 0x0d                   W....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 BolusWizard 2013-07-11T14:16:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 188,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2013-07-11T14:16:26)
    0000   0x5a 0xd0 0x0e 0x0b 0x0d                   Z....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125
    HOUR BITS: [1, 1, 0]
#### RECORD 24 Bolus 2013-07-11T14:16:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-07-11T14:16:26)
    0000   0x5a 0xd0 0x4e 0x0b 0x0d                   Z.N..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 CalBGForPH 2013-07-11T15:24:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-07-11T15:24:09)
    0000   0x49 0xd8 0x2f 0x0b 0x0d                   I./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 26 CalBGForPH 2013-07-11T15:25:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2013-07-11T15:25:01)
    0000   0x41 0xd9 0x2f 0x0b 0x0d                   A./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 BolusWizard 2013-07-11T15:25:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2013-07-11T15:25:48)
    0000   0x70 0xd9 0x0f 0x0b 0x0d                   p....
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0x01 0x1a 0x00    #P.-j...
    0008   0x00 0x0b 0x00 0x1a 0x7d                   ....}
    decimal
             35   80   13   45  106    1   26    0
              0   11    0   26  125
    HOUR BITS: [1, 1, 0]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 1.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0x47 0x04                   \.8G.
    decimal
             92    5   56   71    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-07-11T15:25:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-07-11T15:25:48)
    0000   0x70 0xd9 0x4f 0x0b 0x0d                   p.O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 CalBGForPH 2013-07-11T18:55:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 81}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2013-07-11T18:55:52)
    0000   0x74 0xf7 0x32 0x0b 0x0d                   t.2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 CalBGForPH 2013-07-11T19:23:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-07-11T19:23:54)
    0000   0x76 0xd7 0x33 0x0b 0x0d                   v.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 32 BolusWizard 2013-07-11T19:24:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 110,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-07-11T19:24:07)
    0000   0x47 0xd8 0x13 0x0b 0x0d                   G....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x00 0x1b 0x00    $P.-j...
    0008   0x00 0x02 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    0   27    0
              0    2    0   27  125
    HOUR BITS: [1, 1, 0]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 240, 'amount': 2.6, 'curve': 4},
 {'age': 54, 'amount': 1.4, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x68 0xf0 0x04 0x38 0x36 0x14    \.h..86.
    decimal
             92    8  104  240    4   56   54   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-07-11T19:24:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-07-11T19:24:07)
    0000   0x47 0xd8 0x53 0x0b 0x0d                   G.S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 35 ResultTotals 2013-06-11T13:13:43 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x7a                   ....z
    decimal
              7    0    0    4  122
    datetime (2013-06-11T13:13:43)
    0000   0x6b 0x8d 0x6d 0x6b 0x8d                   k.mk.
    body (41)
    hex
    0000   0x05 0x00 0x7b 0x51 0xbc 0x05 0x00 0x00    ..{Q....
    0008   0x04 0x7a 0x03 0x6e 0x4d 0x01 0x0c 0x17    .z.nM...
    0010   0x00 0x47 0x01 0x0c 0x17 0x00 0xd4 0x4f    .G.....O
    0018   0x00 0x38 0x15 0x00 0x00 0x00 0x03 0x02    .8......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  123   81  188    5    0    0
              4  122    3  110   77    1   12   23
              0   71    1   12   23    0  212   79
              0   56   21    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 36 PumpSuspend 2013-07-12T12:20:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-12T12:20:07)
    0000   0x47 0xd4 0x0c 0x0c 0x0d                   G....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 PumpResume 2013-07-12T12:48:59 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-12T12:48:59)
    0000   0x7b 0xf0 0x0c 0x0c 0x0d                   {....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 CalBGForPH 2013-07-12T14:35:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 81}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2013-07-12T14:35:59)
    0000   0x7b 0xe3 0x2e 0x0c 0x0d                   {....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 BolusWizard 2013-07-12T14:36:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 81,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 52,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x51                                  [Q
    decimal
             91   81
    datetime (2013-07-12T14:36:42)
    0000   0x6a 0xe4 0x0e 0x0c 0x0d                   j....
    body (13)
    hex
    0000   0x34 0x50 0x0d 0x2d 0x6a 0xfa 0x28 0xf0    4P.-j.(.
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             52   80   13   45  106  250   40  240
              0    0    0   34  125
    HOUR BITS: [1, 1, 1]
#### RECORD 40 Bolus 2013-07-12T14:36:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-07-12T14:36:42)
    0000   0x6a 0xe4 0x4e 0x0c 0x0d                   j.N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 CalBGForPH 2013-07-12T17:15:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-07-12T17:15:46)
    0000   0x6e 0xcf 0x31 0x0c 0x0d                   n.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 42 ResultTotals 2013-06-12T13:13:44 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xf8                   .....
    decimal
              7    0    0    3  248
    datetime (2013-06-12T13:13:44)
    0000   0x6c 0x8d 0x6d 0x6c 0x8d                   l.ml.
    body (41)
    hex
    0000   0x05 0x00 0x52 0x51 0x52 0x02 0x00 0x00    ..RQR...
    0008   0x03 0xf8 0x03 0x70 0x57 0x00 0x88 0x0d    ...pW...
    0010   0x00 0x34 0x00 0x88 0x0d 0x00 0x88 0x64    .4.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   82   81   82    2    0    0
              3  248    3  112   87    0  136   13
              0   52    0  136   13    0  136  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 PumpSuspend 2013-07-13T15:22:23 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-13T15:22:23)
    0000   0x57 0xd6 0x0f 0x0d 0x0d                   W....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 44 PumpResume 2013-07-13T15:48:44 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-13T15:48:44)
    0000   0x6c 0xf0 0x0f 0x0d 0x0d                   l....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 CalBGForPH 2013-07-13T19:10:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2013-07-13T19:10:06)
    0000   0x46 0xca 0x33 0x0d 0x0d                   F.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 46 BolusWizard 2013-07-13T19:10:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 153,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 2.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2013-07-13T19:10:17)
    0000   0x51 0xca 0x13 0x0d 0x0d                   Q....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0x06 0x16 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             29   80   13   45  106    6   22    0
              0    0    0   28  125
    HOUR BITS: [1, 1, 0]
#### RECORD 47 LowReservoir 2013-07-13T19:10:20 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-13T19:10:20)
    0000   0x54 0xca 0x13 0x0d 0x0d                   T....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 Bolus 2013-07-13T19:10:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-07-13T19:10:17)
    0000   0x51 0xca 0x53 0x0d 0x0d                   Q.S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 CalBGForPH 2013-07-13T21:31:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2013-07-13T21:31:50)
    0000   0x72 0xdf 0x35 0x0d 0x0d                   r.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 BolusWizard 2013-07-13T21:32:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 153,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2013-07-13T21:32:06)
    0000   0x46 0xe0 0x15 0x0d 0x0d                   F....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x06 0x17 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    6   23    0
              0    9    0   23  125
    HOUR BITS: [1, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 148, 'amount': 2.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0x94 0x04                   \.p..
    decimal
             92    5  112  148    4
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-07-13T21:32:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-07-13T21:32:06)
    0000   0x46 0xe0 0x55 0x0d 0x0d                   F.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 53 ResultTotals 2013-06-13T13:13:45 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x40                   ....@
    decimal
              7    0    0    4   64
    datetime (2013-06-13T13:13:45)
    0000   0x6d 0x8d 0x6d 0x6d 0x8d                   m.mm.
    body (41)
    hex
    0000   0x05 0x00 0x99 0x99 0x99 0x02 0x00 0x00    ........
    0008   0x04 0x40 0x03 0x74 0x51 0x00 0xcc 0x13    .@.tQ...
    0010   0x00 0x3c 0x00 0xcc 0x13 0x00 0xb4 0x58    .<.....X
    0018   0x00 0x18 0x0c 0x00 0x00 0x00 0x02 0x01    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  153  153  153    2    0    0
              4   64    3  116   81    0  204   19
              0   60    0  204   19    0  180   88
              0   24   12    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 54 LowReservoir 2013-07-14T00:30:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-07-14T00:30:00)
    0000   0x40 0xde 0x00 0x0e 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 CalBGForPH 2013-07-14T11:12:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-07-14T11:12:49)
    0000   0x71 0xcc 0x2b 0x0e 0x0d                   q.+..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 BolusWizard 2013-07-14T11:12:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 18,
 '_byte[7]': 0,
 'bg': 206,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xce                                  [.
    decimal
             91  206
    datetime (2013-07-14T11:12:52)
    0000   0x74 0xcc 0x0b 0x0e 0x0d                   t....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0    0    0   18  125
    HOUR BITS: [1, 1, 0]
#### RECORD 57 Bolus 2013-07-14T11:12:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-07-14T11:12:52)
    0000   0x74 0xcc 0x4b 0x0e 0x0d                   t.K..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 58 BolusWizard 2013-07-14T12:14:55 head[2], body[13] op[0x5b]
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
    datetime (2013-07-14T12:14:55)
    0000   0x77 0xce 0x0c 0x0e 0x0d                   w....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [1, 1, 0]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 0.15, 'curve': 4},
 {'age': 70, 'amount': 1.65, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x06 0x3c 0x04 0x42 0x46 0x04    \..<.BF.
    decimal
             92    8    6   60    4   66   70    4
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-07-14T12:14:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-07-14T12:14:55)
    0000   0x77 0xce 0x4c 0x0e 0x0d                   w.L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 61 Rewind 2013-07-14T20:08:14 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-14T20:08:14)
    0000   0x4e 0xc8 0x14 0x0e 0x0d                   N....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 Prime 2013-07-14T20:09:58 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x24                   ....$
    decimal
              3    0    0    0   36
    datetime (2013-07-14T20:09:58)
    0000   0x7a 0xc9 0x34 0x0e 0x0d                   z.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 Prime 2013-07-14T20:10:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-14T20:10:19)
    0000   0x53 0xca 0x14 0x0e 0x0d                   S....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 CalBGForPH 2013-07-14T21:31:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2013-07-14T21:31:04)
    0000   0x44 0xdf 0x35 0x0e 0x0d                   D.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 BolusWizard 2013-07-14T21:31:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 129,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x81                                  [.
    decimal
             91  129
    datetime (2013-07-14T21:31:53)
    0000   0x75 0xdf 0x15 0x0e 0x0d                   u....
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0x00 0x31 0x00    @P.-j.1.
    0008   0x00 0x00 0x00 0x31 0x7d                   ...1}
    decimal
             64   80   13   45  106    0   49    0
              0    0    0   49  125
    HOUR BITS: [1, 1, 0]
#### RECORD 66 Bolus 2013-07-14T21:31:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2013-07-14T21:31:53)
    0000   0x75 0xdf 0x55 0x0e 0x0d                   u.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 ResultTotals 2013-06-14T13:13:46 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xea                   .....
    decimal
              7    0    0    4  234
    datetime (2013-06-14T13:13:46)
    0000   0x6e 0x8d 0x6d 0x6e 0x8d                   n.mn.
    body (41)
    hex
    0000   0x05 0x00 0xa8 0x81 0xce 0x02 0x00 0x00    ........
    0008   0x04 0xea 0x03 0x82 0x47 0x01 0x68 0x1d    ....G.h.
    0010   0x00 0x5f 0x01 0x68 0x1d 0x01 0x20 0x50    ._.h.. P
    0018   0x00 0x48 0x14 0x00 0x00 0x00 0x03 0x02    .H......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  168  129  206    2    0    0
              4  234    3  130   71    1  104   29
              0   95    1  104   29    1   32   80
              0   72   20    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 68 CalBGForPH 2013-07-15T00:24:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 301}
```
    op hex (2)
    0000   0x0a 0x2d                                  .-
    decimal
             10   45
    datetime (2013-07-15T00:24:03)
    0000   0x43 0xd8 0x20 0x0f 0x8d                   C. ..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 BolusWizard 2013-07-15T00:24:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 39,
 '_byte[7]': 0,
 'bg': 301,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2d                                  [-
    decimal
             91   45
    datetime (2013-07-15T00:24:08)
    0000   0x48 0xd8 0x00 0x0f 0x0d                   H....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x27 0x00 0x00    .Q.-j'..
    0008   0x00 0x0a 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   39    0    0
              0   10    0   29  125
    HOUR BITS: [1, 1, 0]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 170, 'amount': 1.7, 'curve': 4},
 {'age': 180, 'amount': 3.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0xaa 0x04 0x80 0xb4 0x04    \.D.....
    decimal
             92    8   68  170    4  128  180    4
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-07-15T00:24:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-07-15T00:24:08)
    0000   0x48 0xd8 0x40 0x0f 0x0d                   H.@..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 CalBGForPH 2013-07-15T08:40:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 294}
```
    op hex (2)
    0000   0x0a 0x26                                  .&
    decimal
             10   38
    datetime (2013-07-15T08:40:22)
    0000   0x56 0xe8 0x28 0x0f 0x8d                   V.(..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 73 BolusWizard 2013-07-15T08:40:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 37,
 '_byte[7]': 0,
 'bg': 294,
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
    0000   0x5b 0x26                                  [&
    decimal
             91   38
    datetime (2013-07-15T08:40:25)
    0000   0x59 0xe8 0x08 0x0f 0x0d                   Y....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x25 0x00 0x00    .Q.-j%..
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
              0   81   13   45  106   37    0    0
              0    0    0   37  125
    HOUR BITS: [1, 1, 1]
#### RECORD 74 Bolus 2013-07-15T08:40:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'dual_component': '??', 'programmed': 3.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2013-07-15T08:40:25)
    0000   0x59 0xe8 0x48 0x0f 0x0d                   Y.H..
    body (0)
    HOUR BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-6.data: 75 records`
