## START logs/ReadHistoryData-page-32.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x9e 0x79                                  .y
##### DEBUG DECIMAL
            158  121
#### RECORD 0 BolusWizard 2013-02-19T16:21:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.0,
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
    datetime (2013-02-19T16:21:28)
    0000   0x1c 0x95 0x10 0x13 0x0d                   .....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x00 0x1e 0x00    (P.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             40   80   13   45  106    0   30    0
              0    0    0   30  125
    HOUR BITS: [1, 0, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x43 0x04                   \.PC.
    decimal
             92    5   80   67    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-02-19T16:21:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-02-19T16:21:28)
    0000   0x1c 0x95 0x50 0x13 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 CalBGForPH 2013-02-19T19:03:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 83}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-02-19T19:03:21)
    0000   0x15 0x83 0x33 0x13 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 BolusWizard 2013-02-19T19:03:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 83,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x53                                  [S
    decimal
             91   83
    datetime (2013-02-19T19:03:45)
    0000   0x2d 0x83 0x13 0x13 0x0d                   -....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0xfb 0x1e 0xf0    (P.-j...
    0008   0x00 0x08 0x00 0x19 0x7d                   ....}
    decimal
             40   80   13   45  106  251   30  240
              0    8    0   25  125
    HOUR BITS: [1, 0, 0]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 169, 'amount': 3.0, 'curve': 4},
 {'age': 229, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x78 0xa9 0x04 0x50 0xe5 0x04    \.x..P..
    decimal
             92    8  120  169    4   80  229    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-02-19T19:03:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-02-19T19:03:45)
    0000   0x2d 0x83 0x53 0x13 0x0d                   -.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 ResultTotals (2013, 0, 19, 13, 13, 51) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime ((2013, 0, 19, 13, 13, 51))
    0000   0x33 0x0d 0x6d 0x33 0x0d                   3.m3.
    body (41)
    hex
    0000   0x05 0x00 0x8c 0x46 0xdb 0x07 0x00 0x00    ...F....
    0008   0x04 0xd2 0x03 0x7a 0x48 0x01 0x58 0x1c    ...zH.X.
    0010   0x00 0x5a 0x01 0x58 0x1c 0x00 0xf8 0x48    .Z.X...H
    0018   0x00 0x60 0x1c 0x00 0x00 0x00 0x05 0x03    .`......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  140   70  219    7    0    0
              4  210    3  122   72    1   88   28
              0   90    1   88   28    0  248   72
              0   96   28    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 8 CalBGForPH 2013-02-20T00:54:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 227}
```
    op hex (2)
    0000   0x0a 0xe3                                  ..
    decimal
             10  227
    datetime (2013-02-20T00:54:36)
    0000   0x24 0xb6 0x20 0x14 0x0d                   $. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 BolusWizard 2013-02-20T00:54:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 227,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
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
    0000   0x5b 0xe3                                  [.
    decimal
             91  227
    datetime (2013-02-20T00:54:39)
    0000   0x27 0xb6 0x00 0x14 0x0d                   '....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    0    0   22  125
    HOUR BITS: [1, 0, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 2.15, 'curve': 20},
 {'age': 104, 'amount': 0.35, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x56 0x5e 0x14 0x0e 0x68 0x14    \.V^..h.
    decimal
             92    8   86   94   20   14  104   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-02-20T00:54:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-02-20T00:54:39)
    0000   0x27 0xb6 0x40 0x14 0x0d                   '.@..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 CalBGForPH 2013-02-20T09:51:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-02-20T09:51:10)
    0000   0x0a 0xb3 0x29 0x14 0x0d                   ..)..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 13 BolusWizard 2013-02-20T09:51:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 106,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-02-20T09:51:21)
    0000   0x15 0xb3 0x09 0x14 0x0d                   .....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [1, 0, 1]
#### RECORD 14 Bolus 2013-02-20T09:51:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-02-20T09:51:22)
    0000   0x16 0xb3 0x49 0x14 0x0d                   ..I..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 15 PumpSuspend 2013-02-20T12:50:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-20T12:50:17)
    0000   0x11 0xb2 0x0c 0x14 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 16 PumpResume 2013-02-20T13:16:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-20T13:16:07)
    0000   0x07 0x90 0x0d 0x14 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 CalBGForPH 2013-02-20T13:41:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-02-20T13:41:31)
    0000   0x1f 0xa9 0x2d 0x14 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 BolusWizard 2013-02-20T13:41:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2013-02-20T13:41:43)
    0000   0x2b 0xa9 0x0d 0x14 0x0d                   +....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x04 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106    4    0    0
              0    1    0    3  125
    HOUR BITS: [1, 0, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 237, 'amount': 1.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x4c 0xed 0x04                   \.L..
    decimal
             92    5   76  237    4
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-02-20T13:41:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-02-20T13:41:43)
    0000   0x2b 0xa9 0x4d 0x14 0x0d                   +.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 21 CalBGForPH 2013-02-20T13:42:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-02-20T13:42:16)
    0000   0x10 0xaa 0x2d 0x14 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 CalBGForPH 2013-02-20T13:44:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-02-20T13:44:07)
    0000   0x07 0xac 0x2d 0x14 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 23 BolusWizard 2013-02-20T13:45:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2013-02-20T13:45:19)
    0000   0x13 0xad 0x0d 0x14 0x0d                   .....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x04 0x1e 0x00    (P.-j...
    0008   0x00 0x03 0x00 0x1f 0x7d                   ....}
    decimal
             40   80   13   45  106    4   30    0
              0    3    0   31  125
    HOUR BITS: [1, 0, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 0.3, 'curve': 4},
 {'age': 241, 'amount': 1.9, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x0c 0x0b 0x04 0x4c 0xf1 0x04    \....L..
    decimal
             92    8   12   11    4   76  241    4
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-02-20T13:45:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-02-20T13:45:19)
    0000   0x13 0xad 0x4d 0x14 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 26 BolusWizard 2013-02-20T13:58:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-02-20T13:58:39)
    0000   0x27 0xba 0x0d 0x14 0x0d                   '....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 0, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 3.1, 'curve': 4},
 {'age': 24, 'amount': 0.3, 'curve': 4},
 {'age': 254, 'amount': 1.9, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x7c 0x0e 0x04 0x0c 0x18 0x04    \.|.....
    0008   0x4c 0xfe 0x04                             L..
    decimal
             92   11  124   14    4   12   24    4
             76  254    4
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-02-20T13:58:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-02-20T13:58:39)
    0000   0x27 0xba 0x4d 0x14 0x0d                   '.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 29 CalBGForPH 2013-02-20T15:54:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-02-20T15:54:21)
    0000   0x15 0xb6 0x2f 0x14 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 30 CalBGForPH 2013-02-20T16:40:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-02-20T16:40:00)
    0000   0x00 0xa8 0x30 0x14 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 31 CalBGForPH 2013-02-20T16:47:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-02-20T16:47:25)
    0000   0x19 0xaf 0x30 0x14 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 32 CalBGForPH 2013-02-20T17:35:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2013-02-20T17:35:57)
    0000   0x39 0xa3 0x31 0x14 0x0d                   9.1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 CalBGForPH 2013-02-20T20:45:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-02-20T20:45:36)
    0000   0x24 0xad 0x34 0x14 0x0d                   $.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 34 BolusWizard 2013-02-20T20:45:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 19,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 1.4,
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
    datetime (2013-02-20T20:45:48)
    0000   0x30 0xad 0x14 0x14 0x0d                   0....
    body (13)
    hex
    0000   0x13 0x50 0x0d 0x2d 0x6a 0xfd 0x0e 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             19   80   13   45  106  253   14  240
              0    0    0   11  125
    HOUR BITS: [1, 0, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.0, 'curve': 20},
 {'age': 165, 'amount': 3.1, 'curve': 20},
 {'age': 175, 'amount': 0.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x9b 0x14 0x7c 0xa5 0x14    \.(..|..
    0008   0x0c 0xaf 0x14                             ...
    decimal
             92   11   40  155   20  124  165   20
             12  175   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-02-20T20:45:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-02-20T20:45:48)
    0000   0x30 0xad 0x54 0x14 0x0d                   0.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 37 CalBGForPH 2013-02-20T22:04:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-02-20T22:04:15)
    0000   0x0f 0x84 0x36 0x14 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 38 CalBGForPH 2013-02-20T22:07:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-02-20T22:07:15)
    0000   0x0f 0x87 0x36 0x14 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 CalBGForPH 2013-02-20T22:18:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 74}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2013-02-20T22:18:34)
    0000   0x22 0x92 0x36 0x14 0x0d                   ".6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 ResultTotals (2013, 0, 20, 13, 13, 52) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf2                   .....
    decimal
              7    0    0    4  242
    datetime ((2013, 0, 20, 13, 13, 52))
    0000   0x34 0x0d 0x6d 0x34 0x0d                   4.m4.
    body (41)
    hex
    0000   0x05 0x00 0x72 0x49 0xe3 0x0d 0x00 0x00    ..rI....
    0008   0x04 0xf2 0x03 0x72 0x46 0x01 0x80 0x1e    ...rF...
    0010   0x00 0x62 0x01 0x80 0x1e 0x01 0x18 0x49    .b.....I
    0018   0x00 0x68 0x1b 0x00 0x00 0x00 0x06 0x03    .h......
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  114   73  227   13    0    0
              4  242    3  114   70    1  128   30
              0   98    1  128   30    1   24   73
              0  104   27    0    0    0    6    3
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 41 PumpSuspend 2013-02-21T10:39:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-21T10:39:39)
    0000   0x27 0xa7 0x0a 0x15 0x0d                   '....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 42 PumpResume 2013-02-21T11:01:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-21T11:01:29)
    0000   0x1d 0x81 0x0b 0x15 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 43 CalBGForPH 2013-02-21T11:26:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 264}
```
    op hex (2)
    0000   0x0a 0x08                                  ..
    decimal
             10    8
    datetime (2013-02-21T11:26:10)
    0000   0x0a 0x9a 0x2b 0x15 0x8d                   ..+..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 44 BolusWizard 2013-02-21T11:26:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 264,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
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
    0000   0x5b 0x08                                  [.
    decimal
             91    8
    datetime (2013-02-21T11:26:14)
    0000   0x0e 0x9a 0x0b 0x15 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1e 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
              0   81   13   45  106   30    0    0
              0    0    0   30  125
    HOUR BITS: [1, 0, 0]
#### RECORD 45 Bolus 2013-02-21T11:26:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-02-21T11:26:14)
    0000   0x0e 0x9a 0x4b 0x15 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 46 CalBGForPH 2013-02-21T13:05:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-02-21T13:05:16)
    0000   0x10 0x85 0x2d 0x15 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 47 BolusWizard 2013-02-21T13:06:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-02-21T13:06:02)
    0000   0x02 0x86 0x0d 0x15 0x0d                   .....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x00 0x1d 0x00    &P.-j...
    0008   0x00 0x12 0x00 0x1d 0x7d                   ....}
    decimal
             38   80   13   45  106    0   29    0
              0   18    0   29  125
    HOUR BITS: [1, 0, 0]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 3.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x66 0x04                   \.xf.
    decimal
             92    5  120  102    4
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-02-21T13:06:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-02-21T13:06:02)
    0000   0x02 0x86 0x4d 0x15 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 CalBGForPH 2013-02-21T13:52:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-02-21T13:52:26)
    0000   0x1a 0xb4 0x2d 0x15 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 51 BolusWizard 2013-02-21T13:52:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-02-21T13:52:35)
    0000   0x23 0xb4 0x0d 0x15 0x0d                   #....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x23 0x00 0x14 0x7d                   .#..}
    decimal
             27   80   13   45  106    0   20    0
              0   35    0   20  125
    HOUR BITS: [1, 0, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.9, 'curve': 4},
 {'age': 148, 'amount': 3.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0x30 0x04 0x78 0x94 0x04    \.t0.x..
    decimal
             92    8  116   48    4  120  148    4
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-02-21T13:52:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-02-21T13:52:35)
    0000   0x23 0xb4 0x4d 0x15 0x0d                   #.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 54 CalBGForPH 2013-02-21T16:05:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-02-21T16:05:29)
    0000   0x1d 0x85 0x30 0x15 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 55 CalBGForPH 2013-02-21T19:02:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2013-02-21T19:02:23)
    0000   0x17 0x82 0x33 0x15 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 BolusWizard 2013-02-21T19:02:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 94,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 2.4,
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
    datetime (2013-02-21T19:02:36)
    0000   0x24 0x82 0x13 0x15 0x0d                   $....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xfd 0x18 0xf0     P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             32   80   13   45  106  253   24  240
              0    0    0   21  125
    HOUR BITS: [1, 0, 0]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 62, 'amount': 2.0, 'curve': 20},
 {'age': 102, 'amount': 2.9, 'curve': 20},
 {'age': 202, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x3e 0x14 0x74 0x66 0x14    \.P>.tf.
    0008   0x78 0xca 0x14                             x..
    decimal
             92   11   80   62   20  116  102   20
            120  202   20
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-02-21T19:02:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-02-21T19:02:36)
    0000   0x24 0x82 0x53 0x15 0x0d                   $.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 CalBGForPH 2013-02-21T21:41:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-02-21T21:41:03)
    0000   0x03 0xa9 0x35 0x15 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 60 ResultTotals (2013, 0, 21, 13, 13, 53) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x04                   .....
    decimal
              7    0    0    5    4
    datetime ((2013, 0, 21, 13, 13, 53))
    0000   0x35 0x0d 0x6d 0x35 0x0d                   5.m5.
    body (41)
    hex
    0000   0x05 0x10 0x84 0x5e 0x08 0x06 0x00 0x00    ...^....
    0008   0x05 0x04 0x03 0x74 0x45 0x01 0x90 0x1f    ...tE...
    0010   0x00 0x61 0x01 0x90 0x1f 0x01 0x18 0x46    .a.....F
    0018   0x00 0x78 0x1e 0x00 0x00 0x00 0x04 0x03    .x......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  132   94    8    6    0    0
              5    4    3  116   69    1  144   31
              0   97    1  144   31    1   24   70
              0  120   30    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 61 CalBGForPH 2013-02-22T01:34:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2013-02-22T01:34:06)
    0000   0x06 0xa2 0x21 0x16 0x0d                   ..!..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 62 BolusWizard 2013-02-22T01:34:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 184,
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
    0000   0x5b 0xb8                                  [.
    decimal
             91  184
    datetime (2013-02-22T01:34:12)
    0000   0x0c 0xa2 0x01 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125
    HOUR BITS: [1, 0, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 134, 'amount': 0.05, 'curve': 20},
 {'age': 144, 'amount': 2.05, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x02 0x86 0x14 0x52 0x90 0x14    \....R..
    decimal
             92    8    2  134   20   82  144   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-02-22T01:34:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-02-22T01:34:12)
    0000   0x0c 0xa2 0x41 0x16 0x0d                   ..A..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 65 LowReservoir 2013-02-22T09:40:54 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-02-22T09:40:54)
    0000   0x36 0xa8 0x09 0x16 0x0d                   6....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 66 CalBGForPH 2013-02-22T09:44:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-02-22T09:44:17)
    0000   0x11 0xac 0x29 0x16 0x0d                   ..)..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 67 BolusWizard 2013-02-22T09:44:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-02-22T09:44:20)
    0000   0x14 0xac 0x09 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x09 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106    9    0    0
              0    0    0    9  125
    HOUR BITS: [1, 0, 1]
#### RECORD 68 Bolus 2013-02-22T09:44:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-02-22T09:44:20)
    0000   0x14 0xac 0x49 0x16 0x0d                   ..I..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 69 CalBGForPH 2013-02-22T11:45:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-02-22T11:45:14)
    0000   0x0e 0xad 0x2b 0x16 0x0d                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 70 BolusWizard 2013-02-22T11:45:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 26,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-02-22T11:45:34)
    0000   0x22 0xad 0x0b 0x16 0x0d                   "....
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x02 0x14 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x14 0x7d                   ....}
    decimal
             26   80   13   45  106    2   20    0
              0    4    0   20  125
    HOUR BITS: [1, 0, 1]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 0.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x24 0x79 0x04                   \.$y.
    decimal
             92    5   36  121    4
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-02-22T11:45:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-02-22T11:45:34)
    0000   0x22 0xad 0x4b 0x16 0x0d                   ".K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 73 PumpSuspend 2013-02-22T15:02:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-22T15:02:09)
    0000   0x09 0x82 0x0f 0x16 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 74 PumpResume 2013-02-22T15:25:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-22T15:25:40)
    0000   0x28 0x99 0x0f 0x16 0x0d                   (....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 75 CalBGForPH 2013-02-22T15:53:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2013-02-22T15:53:35)
    0000   0x23 0xb5 0x2f 0x16 0x0d                   #./..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 76 BolusWizard 2013-02-22T15:53:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 98,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2013-02-22T15:53:46)
    0000   0x2e 0xb5 0x0f 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0xfe 0x21 0xf0    ,P.-j.!.
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             44   80   13   45  106  254   33  240
              0    0    0   31  125
    HOUR BITS: [1, 0, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 249, 'amount': 2.0, 'curve': 4},
 {'age': 113, 'amount': 0.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0xf9 0x04 0x24 0x71 0x14    \.P..$q.
    decimal
             92    8   80  249    4   36  113   20
    datetime (unknown)

    body (0)

#### RECORD 78 LowReservoir 2013-02-22T15:54:23 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-02-22T15:54:23)
    0000   0x17 0xb6 0x0f 0x16 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 Bolus 2013-02-22T15:53:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-02-22T15:53:46)
    0000   0x2e 0xb5 0x4f 0x16 0x0d                   ..O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 80 Rewind 2013-02-22T19:43:50 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-02-22T19:43:50)
    0000   0x32 0xab 0x13 0x16 0x0d                   2....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 81 Prime 2013-02-22T19:46:50 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x15                   .....
    decimal
              3    0    0    0   21
    datetime (2013-02-22T19:46:50)
    0000   0x32 0xae 0x33 0x16 0x0d                   2.3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 82 Prime 2013-02-22T19:47:12 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-02-22T19:47:12)
    0000   0x0c 0xaf 0x13 0x16 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 83 CalBGForPH 2013-02-22T19:54:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-02-22T19:54:51)
    0000   0x33 0xb6 0x33 0x16 0x0d                   3.3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 84 BolusWizard 2013-02-22T19:55:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 91,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2013-02-22T19:55:13)
    0000   0x0d 0xb7 0x13 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0xfc 0x2c 0xf0    :P.-j.,.
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
             58   80   13   45  106  252   44  240
              0    0    0   40  125
    HOUR BITS: [1, 0, 1]
#### RECORD 85 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 241, 'amount': 2.75, 'curve': 4},
 {'age': 251, 'amount': 0.35, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x6e 0xf1 0x04 0x0e 0xfb 0x04    \.n.....
    decimal
             92    8  110  241    4   14  251    4
    datetime (unknown)

    body (0)

#### RECORD 86 Bolus 2013-02-22T19:55:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-02-22T19:55:13)
    0000   0x0d 0xb7 0x53 0x16 0x0d                   ..S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 87 CalBGForPH 2013-02-22T20:59:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2013-02-22T20:59:13)
    0000   0x0d 0xbb 0x34 0x16 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-32.data: 88 records`
