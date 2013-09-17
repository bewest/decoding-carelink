## START logs/ReadHistoryData-page-29.data
#### RECORD 0 Bolus 2013-02-27T20:44:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x38 0x38 0x00                        .88.
    decimal
              1   56   56    0
    datetime (2013-02-27T20:44:36)
    0000   0x24 0xac 0x54 0x1b 0x0d                   $.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 1 CalBGForPH 2013-02-27T20:52:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2013-02-27T20:52:56)
    0000   0x38 0xb4 0x34 0x1b 0x0d                   8.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 BolusWizard 2013-02-27T20:53:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 189,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 6.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2013-02-27T20:53:13)
    0000   0x0d 0xb5 0x14 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x40 0x00 0x00 0x7d                   .@..}
    decimal
              0   80   13   45  106   14    0    0
              0   64    0    0  125
    HOUR BITS: [1, 0, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 5.6, 'curve': 4},
 {'age': 19, 'amount': 0.8, 'curve': 4},
 {'age': 33, 'amount': 3.8, 'curve': 20},
 {'age': 183, 'amount': 0.5, 'curve': 20},
 {'age': 193, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0xe0 0x09 0x04 0x20 0x13 0x04    \.... ..
    0008   0x98 0x21 0x14 0x14 0xb7 0x14 0x6c 0xc1    .!....l.
    0010   0x14                                       .
    decimal
             92   17  224    9    4   32   19    4
            152   33   20   20  183   20  108  193
             20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-02-27T20:53:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-02-27T20:53:13)
    0000   0x0d 0xb5 0x54 0x1b 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 5 CalBGForPH 2013-02-27T21:01:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2013-02-27T21:01:33)
    0000   0x21 0x81 0x35 0x1b 0x0d                   !.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 BolusWizard 2013-02-27T21:02:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-02-27T21:02:29)
    0000   0x1d 0x82 0x15 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x00 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106    0    0    0
              0    0    0    0  125
    HOUR BITS: [1, 0, 0]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 5.9, 'curve': 4},
 {'age': 28, 'amount': 0.8, 'curve': 4},
 {'age': 42, 'amount': 3.8, 'curve': 20},
 {'age': 192, 'amount': 0.5, 'curve': 20},
 {'age': 202, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0xec 0x12 0x04 0x20 0x1c 0x04    \.... ..
    0008   0x98 0x2a 0x14 0x14 0xc0 0x14 0x6c 0xca    .*....l.
    0010   0x14                                       .
    decimal
             92   17  236   18    4   32   28    4
            152   42   20   20  192   20  108  202
             20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-02-27T21:02:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-02-27T21:02:29)
    0000   0x1d 0x82 0x55 0x1b 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 9 CalBGForPH 2013-02-27T21:11:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-02-27T21:11:52)
    0000   0x34 0x8b 0x35 0x1b 0x0d                   4.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 CalBGForPH 2013-02-27T21:13:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-02-27T21:13:15)
    0000   0x0f 0x8d 0x35 0x1b 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 CalBGForPH 2013-02-27T21:36:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-02-27T21:36:43)
    0000   0x2b 0xa4 0x35 0x1b 0x0d                   +.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 CalBGForPH 2013-02-27T21:48:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2013-02-27T21:48:22)
    0000   0x16 0xb0 0x35 0x1b 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 13 ResultTotals (2013, 0, 27, 13, 13, 59) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xd0                   .....
    decimal
              7    0    0    5  208
    datetime ((2013, 0, 27, 13, 13, 59))
    0000   0x3b 0x0d 0x6d 0x3b 0x0d                   ;.m;.
    body (41)
    hex
    0000   0x05 0x10 0xa1 0x28 0x4c 0x12 0x00 0x00    ...(L...
    0008   0x05 0xd0 0x03 0x74 0x3b 0x02 0x5c 0x29    ...t;.\)
    0010   0x00 0x7d 0x02 0x5c 0x29 0x01 0x70 0x3d    .}.\).p=
    0018   0x00 0xec 0x27 0x00 0x00 0x00 0x09 0x04    ..'.....
    0020   0x05 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  161   40   76   18    0    0
              5  208    3  116   59    2   92   41
              0  125    2   92   41    1  112   61
              0  236   39    0    0    0    9    4
              5    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 14 CalBGForPH 2013-02-28T00:05:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-02-28T00:05:30)
    0000   0x1e 0x85 0x20 0x1c 0x0d                   .. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 15 CalBGForPH 2013-02-28T09:33:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 265}
```
    op hex (2)
    0000   0x0a 0x09                                  ..
    decimal
             10    9
    datetime (2013-02-28T09:33:21)
    0000   0x15 0xa1 0x29 0x1c 0x8d                   ..)..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 CalBGForPH 2013-02-28T09:33:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 267}
```
    op hex (2)
    0000   0x0a 0x0b                                  ..
    decimal
             10   11
    datetime (2013-02-28T09:33:24)
    0000   0x18 0xa1 0x29 0x1c 0x8d                   ..)..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 BolusWizard 2013-02-28T09:33:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 267,
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
    0000   0x5b 0x0b                                  [.
    decimal
             91   11
    datetime (2013-02-28T09:33:27)
    0000   0x1b 0xa1 0x09 0x1c 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    0    0   31  125
    HOUR BITS: [1, 0, 1]
#### RECORD 18 Bolus 2013-02-28T09:33:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-02-28T09:33:27)
    0000   0x1b 0xa1 0x49 0x1c 0x0d                   ..I..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 19 CalBGForPH 2013-02-28T11:49:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2013-02-28T11:49:00)
    0000   0x00 0xb1 0x2b 0x1c 0x8d                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 CalBGForPH 2013-02-28T11:50:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2013-02-28T11:50:28)
    0000   0x1c 0xb2 0x2b 0x1c 0x8d                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 BolusWizard 2013-02-28T11:50:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 256,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-02-28T11:50:34)
    0000   0x22 0xb2 0x0b 0x1c 0x0d                   "....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x0b 0x00 0x12 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0   11    0   18  125
    HOUR BITS: [1, 0, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 136, 'amount': 2.25, 'curve': 4},
 {'age': 146, 'amount': 0.85, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x5a 0x88 0x04 0x22 0x92 0x04    \.Z.."..
    decimal
             92    8   90  136    4   34  146    4
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-02-28T11:50:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-02-28T11:50:34)
    0000   0x22 0xb2 0x4b 0x1c 0x0d                   ".K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 CalBGForPH 2013-02-28T12:35:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 187}
```
    op hex (2)
    0000   0x0a 0xbb                                  ..
    decimal
             10  187
    datetime (2013-02-28T12:35:21)
    0000   0x15 0xa3 0x2c 0x1c 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 25 BolusWizard 2013-02-28T12:35:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 187,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbb                                  [.
    decimal
             91  187
    datetime (2013-02-28T12:35:53)
    0000   0x35 0xa3 0x0c 0x1c 0x0d                   5....
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0x0d 0x2b 0x00    9P.-j.+.
    0008   0x00 0x15 0x00 0x2b 0x7d                   ...+}
    decimal
             57   80   13   45  106   13   43    0
              0   21    0   43  125
    HOUR BITS: [1, 0, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 1.8, 'curve': 4},
 {'age': 181, 'amount': 2.25, 'curve': 4},
 {'age': 191, 'amount': 0.85, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x33 0x04 0x5a 0xb5 0x04    \.H3.Z..
    0008   0x22 0xbf 0x04                             "..
    decimal
             92   11   72   51    4   90  181    4
             34  191    4
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-02-28T12:35:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-02-28T12:35:54)
    0000   0x36 0xa3 0x4c 0x1c 0x0d                   6.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 28 CalBGForPH 2013-02-28T13:58:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2013-02-28T13:58:38)
    0000   0x26 0xba 0x2d 0x1c 0x0d                   &.-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 29 CalBGForPH 2013-02-28T14:17:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2013-02-28T14:17:06)
    0000   0x06 0x91 0x2e 0x1c 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 CalBGForPH 2013-02-28T14:23:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2013-02-28T14:23:10)
    0000   0x0a 0x97 0x2e 0x1c 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 BolusWizard 2013-02-28T14:36:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 26,
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
    datetime (2013-02-28T14:36:20)
    0000   0x14 0xa4 0x0e 0x1c 0x0d                   .....
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             26   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [1, 0, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 122, 'amount': 4.3, 'curve': 4},
 {'age': 172, 'amount': 1.8, 'curve': 4},
 {'age': 46, 'amount': 2.25, 'curve': 20},
 {'age': 56, 'amount': 0.85, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xac 0x7a 0x04 0x48 0xac 0x04    \..z.H..
    0008   0x5a 0x2e 0x14 0x22 0x38 0x14              Z.."8.
    decimal
             92   14  172  122    4   72  172    4
             90   46   20   34   56   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-02-28T14:36:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-02-28T14:36:20)
    0000   0x14 0xa4 0x4e 0x1c 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 34 BolusWizard 2013-02-28T14:39:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 9,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.6,
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
    datetime (2013-02-28T14:39:30)
    0000   0x1e 0xa7 0x0e 0x1c 0x0d                   .....
    body (13)
    hex
    0000   0x09 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              9   80   13   45  106    0    6    0
              0    0    0    6  125
    HOUR BITS: [1, 0, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 2.0, 'curve': 4},
 {'age': 125, 'amount': 4.3, 'curve': 4},
 {'age': 175, 'amount': 1.8, 'curve': 4},
 {'age': 49, 'amount': 2.25, 'curve': 20},
 {'age': 59, 'amount': 0.85, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x05 0x04 0xac 0x7d 0x04    \.P...}.
    0008   0x48 0xaf 0x04 0x5a 0x31 0x14 0x22 0x3b    H..Z1.";
    0010   0x14                                       .
    decimal
             92   17   80    5    4  172  125    4
             72  175    4   90   49   20   34   59
             20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-02-28T14:39:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-02-28T14:39:30)
    0000   0x1e 0xa7 0x4e 0x1c 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 37 CalBGForPH 2013-02-28T18:32:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-02-28T18:32:26)
    0000   0x1a 0xa0 0x32 0x1c 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 38 BolusWizard 2013-02-28T18:33:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-02-28T18:33:29)
    0000   0x1d 0xa1 0x12 0x1c 0x0d                   .....
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0xfd 0x2d 0xf0    ;P.-j.-.
    0008   0x00 0x02 0x00 0x2a 0x7d                   ...*}
    decimal
             59   80   13   45  106  253   45  240
              0    2    0   42  125
    HOUR BITS: [1, 0, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 239, 'amount': 2.6, 'curve': 4},
 {'age': 103, 'amount': 4.3, 'curve': 20},
 {'age': 153, 'amount': 1.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0xef 0x04 0xac 0x67 0x14    \.h...g.
    0008   0x48 0x99 0x14                             H..
    decimal
             92   11  104  239    4  172  103   20
             72  153   20
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-02-28T18:33:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-02-28T18:33:30)
    0000   0x1e 0xa1 0x52 0x1c 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 41 ResultTotals (2013, 0, 28, 13, 13, 60) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x04                   .....
    decimal
              7    0    0    6    4
    datetime ((2013, 0, 28, 13, 13, 60))
    0000   0x3c 0x0d 0x6d 0x3c 0x0d                   <.m<.
    body (41)
    hex
    0000   0x05 0x10 0xc3 0x5c 0x0b 0x0a 0x00 0x00    ...\....
    0008   0x06 0x04 0x03 0x84 0x3a 0x02 0x80 0x2a    ....:..*
    0010   0x00 0x97 0x02 0x80 0x2a 0x01 0xbc 0x45    ....*..E
    0018   0x00 0xc4 0x1f 0x00 0x00 0x00 0x06 0x04    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  195   92   11   10    0    0
              6    4    3  132   58    2  128   42
              0  151    2  128   42    1  188   69
              0  196   31    0    0    0    6    4
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 42 CalBGForPH 2013-03-01T00:32:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 212}
```
    op hex (2)
    0000   0x0a 0xd4                                  ..
    decimal
             10  212
    datetime (2013-03-01T00:32:38)
    0000   0x26 0xe0 0x20 0x01 0x0d                   &. ..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 43 BolusWizard 2013-03-01T00:32:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 212,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
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
    0000   0x5b 0xd4                                  [.
    decimal
             91  212
    datetime (2013-03-01T00:32:41)
    0000   0x29 0xe0 0x00 0x01 0x0d                   )....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x13 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
              0   80   13   45  106   19    0    0
              0    0    0   19  125
    HOUR BITS: [1, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 3.45, 'curve': 20},
 {'age': 112, 'amount': 0.75, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x8a 0x66 0x14 0x1e 0x70 0x14    \..f..p.
    decimal
             92    8  138  102   20   30  112   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-03-01T00:32:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-03-01T00:32:41)
    0000   0x29 0xe0 0x40 0x01 0x0d                   ).@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 46 CalBGForPH 2013-03-01T11:35:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 250}
```
    op hex (2)
    0000   0x0a 0xfa                                  ..
    decimal
             10  250
    datetime (2013-03-01T11:35:25)
    0000   0x19 0xe3 0x2b 0x01 0x0d                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 47 BolusWizard 2013-03-01T11:35:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 27,
 '_byte[7]': 0,
 'bg': 250,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfa                                  [.
    decimal
             91  250
    datetime (2013-03-01T11:35:27)
    0000   0x1b 0xe3 0x0b 0x01 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1b 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
              0   80   13   45  106   27    0    0
              0    0    0   27  125
    HOUR BITS: [1, 1, 1]
#### RECORD 48 Bolus 2013-03-01T11:35:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-03-01T11:35:27)
    0000   0x1b 0xe3 0x4b 0x01 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 PumpSuspend 2013-03-01T11:37:31 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-01T11:37:31)
    0000   0x1f 0xe5 0x0b 0x01 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 50 PumpResume 2013-03-01T12:03:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-01T12:03:50)
    0000   0x32 0xc3 0x0c 0x01 0x0d                   2....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 51 CalBGForPH 2013-03-01T12:35:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2013-03-01T12:35:41)
    0000   0x29 0xe3 0x2c 0x01 0x0d                   ).,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 CalBGForPH 2013-03-01T12:48:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2013-03-01T12:48:34)
    0000   0x22 0xf0 0x2c 0x01 0x0d                   ".,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 53 BolusWizard 2013-03-01T12:48:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 189,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 4.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2013-03-01T12:48:53)
    0000   0x35 0xf0 0x0c 0x01 0x0d                   5....
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0x0e 0x2d 0x00    ;P.-j.-.
    0008   0x00 0x15 0x00 0x2d 0x7d                   ...-}
    decimal
             59   80   13   45  106   14   45    0
              0   21    0   45  125
    HOUR BITS: [1, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 74, 'amount': 2.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0x4a 0x04                   \.lJ.
    decimal
             92    5  108   74    4
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-03-01T12:48:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-03-01T12:48:54)
    0000   0x36 0xf0 0x4c 0x01 0x0d                   6.L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 56 CalBGForPH 2013-03-01T14:12:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-03-01T14:12:14)
    0000   0x0e 0xcc 0x2e 0x01 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 57 BolusWizard 2013-03-01T14:12:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-03-01T14:12:22)
    0000   0x16 0xcc 0x0e 0x01 0x0d                   .....
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x25 0x00 0x12 0x7d                   .%..}
    decimal
             24   80   13   45  106    0   18    0
              0   37    0   18  125
    HOUR BITS: [1, 1, 0]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 4.5, 'curve': 4},
 {'age': 158, 'amount': 2.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb4 0x58 0x04 0x6c 0x9e 0x04    \..X.l..
    decimal
             92    8  180   88    4  108  158    4
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-03-01T14:12:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-03-01T14:12:22)
    0000   0x16 0xcc 0x4e 0x01 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 60 TempBasal 2013-03-01T14:23:53 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.0}
```
    op hex (2)
    0000   0x33 0x28                                  3(
    decimal
             51   40
    datetime (2013-03-01T14:23:53)
    0000   0x35 0xd7 0x0e 0x01 0x0d                   5....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 0]
#### RECORD 61 TempBasalDuration 2013-03-01T14:23:53 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 120}
```
    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2013-03-01T14:23:53)
    0000   0x35 0xd7 0x0e 0x01 0x0d                   5....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 PumpSuspend 2013-03-01T15:30:43 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-01T15:30:43)
    0000   0x2b 0xde 0x0f 0x01 0x0d                   +....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 PumpResume 2013-03-01T15:30:49 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-01T15:30:49)
    0000   0x31 0xde 0x0f 0x01 0x0d                   1....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 TempBasal 2013-03-01T15:30:57 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-03-01T15:30:57)
    0000   0x39 0xde 0x0f 0x01 0x0d                   9....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 0]
#### RECORD 65 TempBasalDuration 2013-03-01T15:30:57 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-03-01T15:30:57)
    0000   0x39 0xde 0x0f 0x01 0x0d                   9....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 66 CalBGForPH 2013-03-01T15:32:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 48}
```
    op hex (2)
    0000   0x0a 0x30                                  .0
    decimal
             10   48
    datetime (2013-03-01T15:32:43)
    0000   0x2b 0xe0 0x2f 0x01 0x0d                   +./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 CalBGForPH 2013-03-01T16:12:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-03-01T16:12:57)
    0000   0x39 0xcc 0x30 0x01 0x0d                   9.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 LowReservoir 2013-03-01T16:34:44 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-01T16:34:44)
    0000   0x2c 0xe2 0x10 0x01 0x0d                   ,....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 CalBGForPH 2013-03-01T16:57:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2013-03-01T16:57:34)
    0000   0x22 0xf9 0x30 0x01 0x0d                   ".0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 70 CalBGForPH 2013-03-01T18:52:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-03-01T18:52:14)
    0000   0x0e 0xf4 0x32 0x01 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 71 BolusWizard 2013-03-01T18:52:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 144,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 4.2,
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
    datetime (2013-03-01T18:52:37)
    0000   0x25 0xf4 0x12 0x01 0x0d                   %....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x04 0x2a 0x00    7P.-j.*.
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             55   80   13   45  106    4   42    0
              0    0    0   46  125
    HOUR BITS: [1, 1, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 1.8, 'curve': 20},
 {'age': 112, 'amount': 4.5, 'curve': 20},
 {'age': 182, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x20 0x14 0xb4 0x70 0x14    \.H ..p.
    0008   0x6c 0xb6 0x14                             l..
    decimal
             92   11   72   32   20  180  112   20
            108  182   20
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-03-01T18:52:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-03-01T18:52:37)
    0000   0x25 0xf4 0x52 0x01 0x0d                   %.R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 74 CalBGForPH 2013-03-01T20:47:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2013-03-01T20:47:19)
    0000   0x13 0xef 0x34 0x01 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 75 BolusWizard 2013-03-01T20:51:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
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
    datetime (2013-03-01T20:51:19)
    0000   0x13 0xf3 0x14 0x01 0x0d                   .....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 1, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 117, 'amount': 2.55, 'curve': 4},
 {'age': 127, 'amount': 2.05, 'curve': 4},
 {'age': 151, 'amount': 1.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x66 0x75 0x04 0x52 0x7f 0x04    \.fu.R..
    0008   0x48 0x97 0x14                             H..
    decimal
             92   11  102  117    4   82  127    4
             72  151   20
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2013-03-01T20:51:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-03-01T20:51:20)
    0000   0x14 0xf3 0x54 0x01 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 78 LowReservoir 2013-03-01T21:12:37 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-03-01T21:12:37)
    0000   0x25 0xcc 0x15 0x01 0x0d                   %....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 CalBGForPH 2013-03-01T23:57:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 138}
```
    op hex (2)
    0000   0x0a 0x8a                                  ..
    decimal
             10  138
    datetime (2013-03-01T23:57:28)
    0000   0x1c 0xf9 0x37 0x01 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 80 ResultTotals 2013-02-01T13:13:33 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x06                   .....
    decimal
              7    0    0    6    6
    datetime (2013-02-01T13:13:33)
    0000   0x21 0x8d 0x6d 0x21 0x8d                   !.m!.
    body (41)
    hex
    0000   0x05 0x00 0x97 0x30 0xfa 0x0b 0x00 0x00    ...0....
    0008   0x06 0x06 0x03 0x72 0x39 0x02 0x94 0x2b    ...r9..+
    0010   0x00 0x97 0x02 0x94 0x2b 0x01 0xcc 0x46    ....+..F
    0018   0x00 0xc8 0x1e 0x00 0x00 0x00 0x06 0x03    ........
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  151   48  250   11    0    0
              6    6    3  114   57    2  148   43
              0  151    2  148   43    1  204   70
              0  200   30    0    0    0    6    3
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 81 Rewind 2013-03-02T16:55:01 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-03-02T16:55:01)
    0000   0x01 0xf7 0x10 0x02 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 82 Prime 2013-03-02T16:56:57 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x26                   ....&
    decimal
              3    0    0    0   38
    datetime (2013-03-02T16:56:57)
    0000   0x39 0xf8 0x30 0x02 0x0d                   9.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 83 Prime 2013-03-02T16:57:17 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-03-02T16:57:17)
    0000   0x11 0xf9 0x10 0x02 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 84 CalBGForPH 2013-03-02T16:59:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2013-03-02T16:59:40)
    0000   0x28 0xfb 0x30 0x02 0x0d                   (.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 85 BolusWizard 2013-03-02T17:00:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 79,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 1.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4f                                  [O
    decimal
             91   79
    datetime (2013-03-02T17:00:00)
    0000   0x00 0xc0 0x11 0x02 0x0d                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0xfa 0x0b 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
             15   80   13   45  106  250   11  240
              0    0    0    5  125
    HOUR BITS: [1, 1, 0]
#### RECORD 86 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0e                                  ..
    decimal
              0   14
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-29.data: 87 records`
