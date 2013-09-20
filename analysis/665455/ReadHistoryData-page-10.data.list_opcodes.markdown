## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-10.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x27 0x15                                  '.
##### DEBUG DECIMAL
             39   21
#### RECORD 0 BolusWizard 2013-06-19T21:03:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 245,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf5                                  [.
    decimal
             91  245
    datetime (2013-06-19T21:03:42)
    0000   0x6a 0x83 0x15 0x13 0x0d                   j....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x02 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0   24    0    2  125
    HOUR BITS: [1, 0, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 1.9, 'curve': 4},
 {'age': 69, 'amount': 1.0, 'curve': 4},
 {'age': 63, 'amount': 0.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0x3b 0x04 0x28 0x45 0x04    \.L;.(E.
    0008   0x20 0x3f 0x14                              ?.
    decimal
             92   11   76   59    4   40   69    4
             32   63   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-06-19T21:03:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-06-19T21:03:42)
    0000   0x6a 0x83 0x55 0x13 0x0d                   j.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 BolusWizard 2013-06-19T21:28:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.7,
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
    datetime (2013-06-19T21:28:31)
    0000   0x5f 0x9c 0x15 0x13 0x0d                   _....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 0]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 0.05, 'curve': 4},
 {'age': 34, 'amount': 0.45, 'curve': 4},
 {'age': 84, 'amount': 1.9, 'curve': 4},
 {'age': 94, 'amount': 1.0, 'curve': 4},
 {'age': 88, 'amount': 0.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x02 0x18 0x04 0x12 0x22 0x04    \.....".
    0008   0x4c 0x54 0x04 0x28 0x5e 0x04 0x20 0x58    LT.(^. X
    0010   0x14                                       .
    decimal
             92   17    2   24    4   18   34    4
             76   84    4   40   94    4   32   88
             20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-06-19T21:28:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-06-19T21:28:31)
    0000   0x5f 0x9c 0x55 0x13 0x0d                   _.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 CalBGForPH 2013-06-19T21:38:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2013-06-19T21:38:27)
    0000   0x5b 0xa6 0x35 0x13 0x0d                   [.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 7 CalBGForPH 2013-06-19T22:11:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 252}
```
    op hex (2)
    0000   0x0a 0xfc                                  ..
    decimal
             10  252
    datetime (2013-06-19T22:11:47)
    0000   0x6f 0x8b 0x36 0x13 0x0d                   o.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 BolusWizard 2013-06-19T22:12:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 252,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfc                                  [.
    decimal
             91  252
    datetime (2013-06-19T22:12:48)
    0000   0x70 0x8c 0x16 0x13 0x0d                   p....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x1c 0x2e 0x00    <P.-j...
    0008   0x00 0x1e 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106   28   46    0
              0   30    0   46  125
    HOUR BITS: [1, 0, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 1.7, 'curve': 4},
 {'age': 68, 'amount': 0.05, 'curve': 4},
 {'age': 78, 'amount': 0.45, 'curve': 4},
 {'age': 128, 'amount': 1.9, 'curve': 4},
 {'age': 138, 'amount': 1.0, 'curve': 4},
 {'age': 132, 'amount': 0.8, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x44 0x30 0x04 0x02 0x44 0x04    \.D0..D.
    0008   0x12 0x4e 0x04 0x4c 0x80 0x04 0x28 0x8a    .N.L..(.
    0010   0x04 0x20 0x84 0x14                        . ..
    decimal
             92   20   68   48    4    2   68    4
             18   78    4   76  128    4   40  138
              4   32  132   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-06-19T22:12:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-06-19T22:12:49)
    0000   0x71 0x8c 0x56 0x13 0x0d                   q.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 CalBGForPH 2013-06-19T22:41:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 241}
```
    op hex (2)
    0000   0x0a 0xf1                                  ..
    decimal
             10  241
    datetime (2013-06-19T22:41:16)
    0000   0x50 0xa9 0x36 0x13 0x0d                   P.6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 MResultTotals 2013-06-20T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-06-20T00:00:00)
    0000   0x00 0x04 0x88 0x73 0x0d                   ...s.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 13 Model522ResultTotals 2013-06-20T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-20T00:00:00)
    0000   0x73 0x0d                                  s.
    body (41)
    hex
    0000   0x05 0x10 0xcb 0x4c 0x03 0x07 0x00 0x00    ...L....
    0008   0x04 0x88 0x02 0xe4 0x40 0x01 0xa4 0x24    ....@..$
    0010   0x00 0x67 0x01 0xa4 0x24 0x01 0x1c 0x44    .g..$..D
    0018   0x00 0x88 0x20 0x00 0x00 0x00 0x05 0x03    .. .....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  203   76    3    7    0    0
              4  136    2  228   64    1  164   36
              0  103    1  164   36    1   28   68
              0  136   32    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0

#### RECORD 14 PumpSuspend 2013-06-20T11:50:11 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-20T11:50:11)
    0000   0x4b 0xb2 0x0b 0x14 0x0d                   K....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 15 PumpResume 2013-06-20T12:15:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-20T12:15:07)
    0000   0x47 0x8f 0x0c 0x14 0x0d                   G....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 CalBGForPH 2013-06-20T12:29:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2013-06-20T12:29:04)
    0000   0x44 0x9d 0x2c 0x14 0x0d                   D.,..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 BolusWizard 2013-06-20T12:29:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 165,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa5                                  [.
    decimal
             91  165
    datetime (2013-06-20T12:29:08)
    0000   0x48 0x9d 0x0c 0x14 0x0d                   H....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    0    0    8  125
    HOUR BITS: [1, 0, 0]
#### RECORD 18 Bolus 2013-06-20T12:29:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-06-20T12:29:08)
    0000   0x48 0x9d 0x4c 0x14 0x0d                   H.L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 19 CalBGForPH 2013-06-20T13:05:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-06-20T13:05:55)
    0000   0x77 0x85 0x2d 0x14 0x0d                   w.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 BolusWizard 2013-06-20T13:06:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 156,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 54,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 4.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2013-06-20T13:06:11)
    0000   0x4b 0x86 0x0d 0x14 0x0d                   K....
    body (13)
    hex
    0000   0x36 0x50 0x0d 0x2d 0x6a 0x06 0x29 0x00    6P.-j.).
    0008   0x00 0x08 0x00 0x29 0x7d                   ...)}
    decimal
             54   80   13   45  106    6   41    0
              0    8    0   41  125
    HOUR BITS: [1, 0, 0]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 42, 'amount': 0.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x20 0x2a 0x04                   \. *.
    decimal
             92    5   32   42    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-06-20T13:06:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'dual_component': '??', 'programmed': 4.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2013-06-20T13:06:11)
    0000   0x4b 0x86 0x4d 0x14 0x0d                   K.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 CalBGForPH 2013-06-20T15:10:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 209}
```
    op hex (2)
    0000   0x0a 0xd1                                  ..
    decimal
             10  209
    datetime (2013-06-20T15:10:49)
    0000   0x71 0x8a 0x2f 0x14 0x0d                   q./..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 BolusWizard 2013-06-20T15:10:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 18,
 '_byte[7]': 0,
 'bg': 209,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd1                                  [.
    decimal
             91  209
    datetime (2013-06-20T15:10:54)
    0000   0x76 0x8a 0x0f 0x14 0x0d                   v....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x14 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0   20    0    0  125
    HOUR BITS: [1, 0, 0]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 4.1, 'curve': 4},
 {'age': 166, 'amount': 0.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xa4 0x7e 0x04 0x20 0xa6 0x04    \..~. ..
    decimal
             92    8  164  126    4   32  166    4
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-06-20T15:10:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-06-20T15:10:54)
    0000   0x76 0x8a 0x4f 0x14 0x0d                   v.O..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 27 CalBGForPH 2013-06-20T16:37:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 217}
```
    op hex (2)
    0000   0x0a 0xd9                                  ..
    decimal
             10  217
    datetime (2013-06-20T16:37:27)
    0000   0x5b 0xa5 0x30 0x14 0x0d                   [.0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 28 BolusWizard 2013-06-20T16:37:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 20,
 '_byte[7]': 0,
 'bg': 217,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd9                                  [.
    decimal
             91  217
    datetime (2013-06-20T16:37:31)
    0000   0x5f 0xa5 0x10 0x14 0x0d                   _....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    6    0   14  125
    HOUR BITS: [1, 0, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 0.3, 'curve': 4},
 {'age': 213, 'amount': 4.1, 'curve': 4},
 {'age': 253, 'amount': 0.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x5d 0x04 0xa4 0xd5 0x04    \..]....
    0008   0x20 0xfd 0x04                              ..
    decimal
             92   11   12   93    4  164  213    4
             32  253    4
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-06-20T16:37:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-06-20T16:37:31)
    0000   0x5f 0xa5 0x50 0x14 0x0d                   _.P..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 31 CalBGForPH 2013-06-20T17:38:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-06-20T17:38:40)
    0000   0x68 0xa6 0x31 0x14 0x0d                   h.1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 32 CalBGForPH 2013-06-20T18:54:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-06-20T18:54:41)
    0000   0x69 0xb6 0x32 0x14 0x0d                   i.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 BolusWizard 2013-06-20T18:55:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2013-06-20T18:55:03)
    0000   0x43 0xb7 0x12 0x14 0x0d                   C....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xfa 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x06 0x00 0x24 0x7d                   ...$}
    decimal
             55   80   13   45  106  250   42  240
              0    6    0   36  125
    HOUR BITS: [1, 0, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 141, 'amount': 1.6, 'curve': 4},
 {'age': 231, 'amount': 0.3, 'curve': 4},
 {'age': 95, 'amount': 4.1, 'curve': 20},
 {'age': 135, 'amount': 0.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x40 0x8d 0x04 0x0c 0xe7 0x04    \.@.....
    0008   0xa4 0x5f 0x14 0x20 0x87 0x14              ._. ..
    decimal
             92   14   64  141    4   12  231    4
            164   95   20   32  135   20
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-06-20T18:55:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-06-20T18:55:03)
    0000   0x43 0xb7 0x52 0x14 0x0d                   C.R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 LowReservoir 2013-06-20T23:56:50 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-06-20T23:56:50)
    0000   0x72 0xb8 0x17 0x14 0x0d                   r....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 37 MResultTotals 2013-06-21T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-06-21T00:00:00)
    0000   0x00 0x05 0x12 0x74 0x0d                   ...t.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 38 Model522ResultTotals 2013-06-21T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-21T00:00:00)
    0000   0x74 0x0d                                  t.
    body (41)
    hex
    0000   0x05 0x00 0x99 0x50 0xd9 0x06 0x00 0x00    ...P....
    0008   0x05 0x12 0x03 0x72 0x44 0x01 0xa0 0x20    ...rD.. 
    0010   0x00 0x6d 0x01 0xa0 0x20 0x01 0x34 0x4a    .m.. .4J
    0018   0x00 0x6c 0x1a 0x00 0x00 0x00 0x05 0x02    .l......
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  153   80  217    6    0    0
              5   18    3  114   68    1  160   32
              0  109    1  160   32    1   52   74
              0  108   26    0    0    0    5    2
              3    0    0   12    0  232    0    0
              0

#### RECORD 39 LowReservoir 2013-06-21T11:13:38 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-06-21T11:13:38)
    0000   0x66 0x8d 0x0b 0x15 0x0d                   f....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 PumpSuspend 2013-06-21T14:47:58 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-21T14:47:58)
    0000   0x7a 0xaf 0x0e 0x15 0x0d                   z....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 41 PumpResume 2013-06-21T15:03:24 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-21T15:03:24)
    0000   0x58 0x83 0x0f 0x15 0x0d                   X....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 CalBGForPH 2013-06-21T16:28:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-06-21T16:28:09)
    0000   0x49 0x9c 0x30 0x15 0x0d                   I.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 43 BolusWizard 2013-06-21T16:28:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 86,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x56                                  [V
    decimal
             91   86
    datetime (2013-06-21T16:28:28)
    0000   0x5c 0x9c 0x10 0x15 0x0d                   \....
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0xfb 0x28 0xf0    5P.-j.(.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             53   80   13   45  106  251   40  240
              0    0    0   35  125
    HOUR BITS: [1, 0, 0]
#### RECORD 44 Bolus 2013-06-21T16:28:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-06-21T16:28:28)
    0000   0x5c 0x9c 0x50 0x15 0x0d                   \.P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 45 Rewind 2013-06-21T17:47:55 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-06-21T17:47:55)
    0000   0x77 0xaf 0x11 0x15 0x0d                   w....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 46 Prime 2013-06-21T17:49:15 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x11                   .....
    decimal
              3    0    0    0   17
    datetime (2013-06-21T17:49:15)
    0000   0x4f 0xb1 0x31 0x15 0x0d                   O.1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 47 Prime 2013-06-21T17:49:31 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-06-21T17:49:31)
    0000   0x5f 0xb1 0x11 0x15 0x0d                   _....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 48 CalBGForPH 2013-06-21T17:53:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 204}
```
    op hex (2)
    0000   0x0a 0xcc                                  ..
    decimal
             10  204
    datetime (2013-06-21T17:53:16)
    0000   0x50 0xb5 0x31 0x15 0x0d                   P.1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 CalBGForPH 2013-06-21T18:51:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 162}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2013-06-21T18:51:57)
    0000   0x79 0xb3 0x32 0x15 0x0d                   y.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 50 BolusWizard 2013-06-21T18:52:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 162,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2013-06-21T18:52:10)
    0000   0x4a 0xb4 0x12 0x15 0x0d                   J....
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0x08 0x35 0x00    FP.-j.5.
    0008   0x00 0x0b 0x00 0x35 0x7d                   ...5}
    decimal
             70   80   13   45  106    8   53    0
              0   11    0   53  125
    HOUR BITS: [1, 0, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 148, 'amount': 3.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x94 0x04                   \....
    decimal
             92    5  140  148    4
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-06-21T18:52:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-06-21T18:52:11)
    0000   0x4b 0xb4 0x52 0x15 0x0d                   K.R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 53 MResultTotals 2013-06-22T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-06-22T00:00:00)
    0000   0x00 0x04 0xda 0x75 0x0d                   ...u.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 54 Model522ResultTotals 2013-06-22T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-22T00:00:00)
    0000   0x75 0x0d                                  u.
    body (41)
    hex
    0000   0x05 0x00 0x97 0x56 0xcc 0x03 0x00 0x00    ...V....
    0008   0x04 0xda 0x03 0x7a 0x48 0x01 0x60 0x1c    ...zH.`.
    0010   0x00 0x7b 0x01 0x60 0x1c 0x01 0x60 0x64    .{.`..`d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  151   86  204    3    0    0
              4  218    3  122   72    1   96   28
              0  123    1   96   28    1   96  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0

#### RECORD 55 CalBGForPH 2013-06-22T13:57:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-06-22T13:57:00)
    0000   0x40 0xb9 0x2d 0x16 0x0d                   @.-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 56 BolusWizard 2013-06-22T13:57:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 82,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x52                                  [R
    decimal
             91   82
    datetime (2013-06-22T13:57:32)
    0000   0x60 0xb9 0x0d 0x16 0x0d                   `....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0xfa 0x32 0xf0    AP.-j.2.
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
             65   80   13   45  106  250   50  240
              0    0    0   44  125
    HOUR BITS: [1, 0, 1]
#### RECORD 57 Bolus 2013-06-22T13:57:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-06-22T13:57:32)
    0000   0x60 0xb9 0x4d 0x16 0x0d                   `.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 58 CalBGForPH 2013-06-22T19:47:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 362}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-06-22T19:47:28)
    0000   0x5c 0xaf 0x33 0x16 0x8d                   \.3..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 59 BolusWizard 2013-06-22T19:47:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 52,
 '_byte[7]': 0,
 'bg': 362,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.2,
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
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-06-22T19:47:32)
    0000   0x60 0xaf 0x13 0x16 0x0d                   `....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x34 0x00 0x00    .Q.-j4..
    0008   0x00 0x00 0x00 0x34 0x7d                   ...4}
    decimal
              0   81   13   45  106   52    0    0
              0    0    0   52  125
    HOUR BITS: [1, 0, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 97, 'amount': 4.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb0 0x61 0x14                   \..a.
    decimal
             92    5  176   97   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-06-22T19:47:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4, 'dual_component': '??', 'programmed': 5.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x36 0x36 0x00                        .66.
    decimal
              1   54   54    0
    datetime (2013-06-22T19:47:32)
    0000   0x60 0xaf 0x53 0x16 0x0d                   `.S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 62 CalBGForPH 2013-06-22T21:46:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2013-06-22T21:46:53)
    0000   0x75 0xae 0x35 0x16 0x0d                   u.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 63 CalBGForPH 2013-06-22T22:34:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2013-06-22T22:34:04)
    0000   0x44 0xa2 0x36 0x16 0x0d                   D.6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 64 BolusWizard 2013-06-22T22:34:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 142,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2013-06-22T22:34:47)
    0000   0x6f 0xa2 0x16 0x16 0x0d                   o....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x03 0x27 0x00    3P.-j.'.
    0008   0x00 0x0c 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106    3   39    0
              0   12    0   39  125
    HOUR BITS: [1, 0, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 170, 'amount': 5.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xd8 0xaa 0x04                   \....
    decimal
             92    5  216  170    4
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-06-22T22:34:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-06-22T22:34:47)
    0000   0x6f 0xa2 0x56 0x16 0x0d                   o.V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 67 BolusWizard 2013-06-22T22:58:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.7,
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
    datetime (2013-06-22T22:58:55)
    0000   0x77 0xba 0x16 0x16 0x0d                   w....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 1]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 3.9, 'curve': 4},
 {'age': 194, 'amount': 5.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x9c 0x18 0x04 0xd8 0xc2 0x04    \.......
    decimal
             92    8  156   24    4  216  194    4
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-06-22T22:58:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-06-22T22:58:55)
    0000   0x77 0xba 0x56 0x16 0x0d                   w.V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 70 MResultTotals 2013-06-23T00:00:00 head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2013-06-23T00:00:00)
    0000   0x00 0x05 0xec 0x76 0x0d                   ...v.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 71 Model522ResultTotals 2013-06-23T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-23T00:00:00)
    0000   0x76 0x0d                                  v.
    body (41)
    hex
    0000   0x05 0x10 0xbc 0x52 0x6a 0x04 0x00 0x00    ...Rj...
    0008   0x05 0xec 0x03 0x84 0x3b 0x02 0x68 0x29    ....;.h)
    0010   0x00 0x8b 0x02 0x68 0x29 0x01 0x90 0x41    ...h)..A
    0018   0x00 0xd8 0x23 0x00 0x00 0x00 0x04 0x03    ..#.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  188   82  106    4    0    0
              5  236    3  132   59    2  104   41
              0  139    2  104   41    1  144   65
              0  216   35    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0

#### RECORD 72 CalBGForPH 2013-06-23T01:16:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 134}
```
    op hex (2)
    0000   0x0a 0x86                                  ..
    decimal
             10  134
    datetime (2013-06-23T01:16:42)
    0000   0x6a 0x90 0x21 0x17 0x0d                   j.!..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 73 CalBGForPH 2013-06-23T07:51:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 419}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-06-23T07:51:08)
    0000   0x48 0xb3 0x27 0x17 0x8d                   H.'..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 74 BolusWizard 2013-06-23T07:51:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 65,
 '_byte[7]': 0,
 'bg': 419,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.5,
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
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2013-06-23T07:51:12)
    0000   0x4c 0xb3 0x07 0x17 0x0d                   L....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x41 0x00 0x00    .Q.-jA..
    0008   0x00 0x00 0x00 0x41 0x7d                   ...A}
    decimal
              0   81   13   45  106   65    0    0
              0    0    0   65  125
    HOUR BITS: [1, 0, 1]
#### RECORD 75 Bolus 2013-06-23T07:51:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.6, 'dual_component': '??', 'programmed': 6.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x42 0x42 0x00                        .BB.
    decimal
              1   66   66    0
    datetime (2013-06-23T07:51:12)
    0000   0x4c 0xb3 0x47 0x17 0x0d                   L.G..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 76 PumpSuspend 2013-06-23T09:28:43 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-23T09:28:43)
    0000   0x6b 0x9c 0x09 0x17 0x0d                   k....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 77 PumpResume 2013-06-23T10:07:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-23T10:07:08)
    0000   0x48 0x87 0x0a 0x17 0x0d                   H....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 78 CalBGForPH 2013-06-23T10:54:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 246}
```
    op hex (2)
    0000   0x0a 0xf6                                  ..
    decimal
             10  246
    datetime (2013-06-23T10:54:50)
    0000   0x72 0xb6 0x2a 0x17 0x0d                   r.*..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 BolusWizard 2013-06-23T10:54:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 246,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf6                                  [.
    decimal
             91  246
    datetime (2013-06-23T10:54:58)
    0000   0x7a 0xb6 0x0a 0x17 0x0d                   z....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0   11    0   15  125
    HOUR BITS: [1, 0, 1]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 180, 'amount': 2.45, 'curve': 4},
 {'age': 190, 'amount': 4.15, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x62 0xb4 0x04 0xa6 0xbe 0x04    \.b.....
    decimal
             92    8   98  180    4  166  190    4
    datetime (unknown)

    body (0)

#### RECORD 81 Bolus 2013-06-23T10:54:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-06-23T10:54:58)
    0000   0x7a 0xb6 0x4a 0x17 0x0d                   z.J..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 82 CalBGForPH 2013-06-23T12:56:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-06-23T12:56:38)
    0000   0x66 0xb8 0x2c 0x17 0x0d                   f.,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 83 CalBGForPH 2013-06-23T12:56:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-06-23T12:56:45)
    0000   0x6d 0xb8 0x2c 0x17 0x0d                   m.,..
    body (0)
    HOUR BITS: [1, 0, 1]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-10.data: 84 records`
