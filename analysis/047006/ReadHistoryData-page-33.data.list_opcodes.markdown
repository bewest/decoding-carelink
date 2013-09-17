## START logs/ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa6 0xca                                  ..
##### DEBUG DECIMAL
            166  202
#### RECORD 0 BolusWizard 2013-02-16T21:17:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-02-16T21:17:13)
    0000   0x0d 0x91 0x15 0x10 0x0d                   .....
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0x09 0x2b 0x00    8P.-j.+.
    0008   0x00 0x14 0x00 0x2b 0x7d                   ...+}
    decimal
             56   80   13   45  106    9   43    0
              0   20    0   43  125
    HOUR BITS: [1, 0, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 2.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x2b 0x04                   \.X+.
    decimal
             92    5   88   43    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-02-16T21:17:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-02-16T21:17:13)
    0000   0x0d 0x91 0x95 0x10 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 Bolus 2013-02-16T21:18:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x02                        ....
    decimal
              1   25   25    2
    datetime (2013-02-16T21:18:23)
    0000   0x17 0x92 0xb5 0x10 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 CalBGForPH 2013-02-16T22:21:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 238}
```
    op hex (2)
    0000   0x0a 0xee                                  ..
    decimal
             10  238
    datetime (2013-02-16T22:21:46)
    0000   0x2e 0x95 0x36 0x10 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 CalBGForPH 2013-02-16T22:22:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 238}
```
    op hex (2)
    0000   0x0a 0xee                                  ..
    decimal
             10  238
    datetime (2013-02-16T22:22:41)
    0000   0x29 0x96 0x36 0x10 0x0d                   ).6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 BolusWizard 2013-02-16T22:23:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 25,
 '_byte[7]': 0,
 'bg': 238,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 4.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xee                                  [.
    decimal
             91  238
    datetime (2013-02-16T22:23:16)
    0000   0x10 0x97 0x16 0x10 0x0d                   .....
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0x19 0x2b 0x00    9P.-j.+.
    0008   0x00 0x31 0x00 0x2b 0x7d                   .1.+}
    decimal
             57   80   13   45  106   25   43    0
              0   49    0   43  125
    HOUR BITS: [1, 0, 0]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 0.2, 'curve': 4},
 {'age': 19, 'amount': 0.4, 'curve': 4},
 {'age': 29, 'amount': 0.4, 'curve': 4},
 {'age': 39, 'amount': 0.45, 'curve': 4},
 {'age': 49, 'amount': 0.4, 'curve': 4},
 {'age': 59, 'amount': 0.4, 'curve': 4},
 {'age': 69, 'amount': 2.05, 'curve': 4},
 {'age': 109, 'amount': 2.2, 'curve': 4}]
```
    op hex (26)
    0000   0x5c 0x1a 0x08 0x09 0x04 0x10 0x13 0x04    \.......
    0008   0x10 0x1d 0x04 0x12 0x27 0x04 0x10 0x31    ....'..1
    0010   0x04 0x10 0x3b 0x04 0x52 0x45 0x04 0x58    ..;.RE.X
    0018   0x6d 0x04                                  m.
    decimal
             92   26    8    9    4   16   19    4
             16   29    4   18   39    4   16   49
              4   16   59    4   82   69    4   88
            109    4
    datetime (unknown)

    body (0)

#### RECORD 8 PumpSuspend 2013-02-16T22:23:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-16T22:23:33)
    0000   0x21 0x97 0x16 0x10 0x0d                   !....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 9 Bolus 2013-02-16T22:23:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x05 0x00                        .+..
    decimal
              1   43    5    0
    datetime (2013-02-16T22:23:16)
    0000   0x10 0x97 0x56 0x10 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 PumpResume 2013-02-16T22:23:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-16T22:23:37)
    0000   0x25 0x97 0x16 0x10 0x0d                   %....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 CalBGForPH 2013-02-16T22:23:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 238}
```
    op hex (2)
    0000   0x0a 0xee                                  ..
    decimal
             10  238
    datetime (2013-02-16T22:23:54)
    0000   0x36 0x97 0x36 0x10 0x0d                   6.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 12 CalBGForPH 2013-02-16T22:24:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 239}
```
    op hex (2)
    0000   0x0a 0xef                                  ..
    decimal
             10  239
    datetime (2013-02-16T22:24:52)
    0000   0x34 0x98 0x36 0x10 0x0d                   4.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 13 CalBGForPH 2013-02-16T22:28:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 233}
```
    op hex (2)
    0000   0x0a 0xe9                                  ..
    decimal
             10  233
    datetime (2013-02-16T22:28:18)
    0000   0x12 0x9c 0x36 0x10 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 14 CalBGForPH 2013-02-16T23:46:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 265}
```
    op hex (2)
    0000   0x0a 0x09                                  ..
    decimal
             10    9
    datetime (2013-02-16T23:46:22)
    0000   0x16 0xae 0x37 0x10 0x8d                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 BolusWizard 2013-02-16T23:46:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 265,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 1.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x09                                  [.
    decimal
             91    9
    datetime (2013-02-16T23:46:48)
    0000   0x30 0xae 0x17 0x10 0x0d                   0....
    body (13)
    hex
    0000   0x14 0x51 0x0d 0x2d 0x6a 0x1f 0x0f 0x00    .Q.-j...
    0008   0x00 0x17 0x00 0x17 0x7d                   ....}
    decimal
             20   81   13   45  106   31   15    0
              0   23    0   23  125
    HOUR BITS: [1, 0, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 0.65, 'curve': 4},
 {'age': 102, 'amount': 0.4, 'curve': 4},
 {'age': 112, 'amount': 0.4, 'curve': 4},
 {'age': 122, 'amount': 0.45, 'curve': 4},
 {'age': 132, 'amount': 0.4, 'curve': 4},
 {'age': 142, 'amount': 0.4, 'curve': 4},
 {'age': 152, 'amount': 2.05, 'curve': 4},
 {'age': 192, 'amount': 2.2, 'curve': 4}]
```
    op hex (26)
    0000   0x5c 0x1a 0x1a 0x5c 0x04 0x10 0x66 0x04    \..\..f.
    0008   0x10 0x70 0x04 0x12 0x7a 0x04 0x10 0x84    .p..z...
    0010   0x04 0x10 0x8e 0x04 0x52 0x98 0x04 0x58    ....R..X
    0018   0xc0 0x04                                  ..
    decimal
             92   26   26   92    4   16  102    4
             16  112    4   18  122    4   16  132
              4   16  142    4   82  152    4   88
            192    4
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-02-16T23:46:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-02-16T23:46:48)
    0000   0x30 0xae 0x57 0x10 0x0d                   0.W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 ResultTotals (2013, 0, 16, 13, 13, 48) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf6                   .....
    decimal
              7    0    0    4  246
    datetime ((2013, 0, 16, 13, 13, 48))
    0000   0x30 0x0d 0x6d 0x30 0x0d                   0.m0.
    body (41)
    hex
    0000   0x05 0x10 0xdf 0xa7 0x09 0x09 0x00 0x00    ........
    0008   0x04 0xf6 0x03 0x84 0x47 0x01 0x72 0x1d    ....G.r.
    0010   0x00 0x85 0x01 0x72 0x1d 0x00 0xfa 0x44    ...r...D
    0018   0x00 0x78 0x20 0x00 0x00 0x00 0x04 0x02    .x .....
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  223  167    9    9    0    0
              4  246    3  132   71    1  114   29
              0  133    1  114   29    0  250   68
              0  120   32    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 19 CalBGForPH 2013-02-17T00:34:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-02-17T00:34:47)
    0000   0x2f 0xa2 0x20 0x11 0x0d                   /. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 20 TempBasal 2013-02-17T01:47:29 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-02-17T01:47:29)
    0000   0x1d 0xaf 0x01 0x11 0x0d                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 0, 1]
#### RECORD 21 TempBasalDuration 2013-02-17T01:47:29 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 30}
```
    op hex (2)
    0000   0x16 0x01                                  ..
    decimal
             22    1
    datetime (2013-02-17T01:47:29)
    0000   0x1d 0xaf 0x01 0x11 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 CalBGForPH 2013-02-17T01:50:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 68}
```
    op hex (2)
    0000   0x0a 0x44                                  .D
    decimal
             10   68
    datetime (2013-02-17T01:50:20)
    0000   0x14 0xb2 0x21 0x11 0x0d                   ..!..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 23 PumpSuspend 2013-02-17T09:37:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-17T09:37:17)
    0000   0x11 0xa5 0x09 0x11 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 PumpResume 2013-02-17T10:04:41 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-17T10:04:41)
    0000   0x29 0x84 0x0a 0x11 0x0d                   )....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 25 CalBGForPH 2013-02-17T11:50:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-02-17T11:50:10)
    0000   0x0a 0xb2 0x2b 0x11 0x0d                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 26 BolusWizard 2013-02-17T11:50:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 14,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 1.0,
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
    datetime (2013-02-17T11:50:24)
    0000   0x18 0xb2 0x0b 0x11 0x0d                   .....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0xfd 0x0a 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             14   80   13   45  106  253   10  240
              0    0    0    7  125
    HOUR BITS: [1, 0, 1]
#### RECORD 27 Bolus 2013-02-17T11:50:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-02-17T11:50:24)
    0000   0x18 0xb2 0x4b 0x11 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 28 PumpSuspend 2013-02-17T17:29:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-17T17:29:56)
    0000   0x38 0x9d 0x11 0x11 0x0d                   8....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 PumpResume 2013-02-17T18:00:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-17T18:00:04)
    0000   0x04 0x80 0x12 0x11 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 CalBGForPH 2013-02-17T18:16:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-02-17T18:16:37)
    0000   0x25 0x90 0x32 0x11 0x0d                   %.2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 BolusWizard 2013-02-17T18:16:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 2.8,
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
    datetime (2013-02-17T18:16:48)
    0000   0x30 0x90 0x12 0x11 0x0d                   0....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0xf9 0x1c 0xf0    %P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             37   80   13   45  106  249   28  240
              0    0    0   21  125
    HOUR BITS: [1, 0, 0]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 136, 'amount': 0.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x1c 0x88 0x14                   \....
    decimal
             92    5   28  136   20
    datetime (unknown)

    body (0)

#### RECORD 33 LowReservoir 2013-02-17T18:17:48 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-02-17T18:17:48)
    0000   0x30 0x91 0x12 0x11 0x0d                   0....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 34 Bolus 2013-02-17T18:16:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-02-17T18:16:48)
    0000   0x30 0x90 0x52 0x11 0x0d                   0.R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 CalBGForPH 2013-02-17T18:41:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 87}
```
    op hex (2)
    0000   0x0a 0x57                                  .W
    decimal
             10   87
    datetime (2013-02-17T18:41:42)
    0000   0x2a 0xa9 0x32 0x11 0x0d                   *.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 BolusWizard 2013-02-17T18:41:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 87,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x57                                  [W
    decimal
             91   87
    datetime (2013-02-17T18:41:51)
    0000   0x33 0xa9 0x12 0x11 0x0d                   3....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0xfc 0x14 0xf0    .P.-j...
    0008   0x00 0x15 0x00 0x10 0x7d                   ....}
    decimal
             27   80   13   45  106  252   20  240
              0   21    0   16  125
    HOUR BITS: [1, 0, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 2.1, 'curve': 4},
 {'age': 161, 'amount': 0.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x54 0x1b 0x04 0x1c 0xa1 0x14    \.T.....
    decimal
             92    8   84   27    4   28  161   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-02-17T18:41:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-02-17T18:41:51)
    0000   0x33 0xa9 0x52 0x11 0x0d                   3.R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 39 CalBGForPH 2013-02-17T21:02:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 222}
```
    op hex (2)
    0000   0x0a 0xde                                  ..
    decimal
             10  222
    datetime (2013-02-17T21:02:26)
    0000   0x1a 0x82 0x35 0x11 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 BolusWizard 2013-02-17T21:02:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 222,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xde                                  [.
    decimal
             91  222
    datetime (2013-02-17T21:02:40)
    0000   0x28 0x82 0x15 0x11 0x0d                   (....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x0a 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0   10    0   11  125
    HOUR BITS: [1, 0, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 148, 'amount': 1.6, 'curve': 4},
 {'age': 168, 'amount': 2.1, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x94 0x04 0x54 0xa8 0x04    \.@..T..
    decimal
             92    8   64  148    4   84  168    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-02-17T21:02:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-02-17T21:02:40)
    0000   0x28 0x82 0x55 0x11 0x0d                   (.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 43 BolusWizard 2013-02-17T21:10:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.9,
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
    datetime (2013-02-17T21:10:57)
    0000   0x39 0x8a 0x15 0x11 0x0d                   9....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125
    HOUR BITS: [1, 0, 0]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 1.2, 'curve': 4},
 {'age': 156, 'amount': 1.6, 'curve': 4},
 {'age': 176, 'amount': 2.1, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x10 0x04 0x40 0x9c 0x04    \.0..@..
    0008   0x54 0xb0 0x04                             T..
    decimal
             92   11   48   16    4   64  156    4
             84  176    4
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-02-17T21:10:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-02-17T21:10:57)
    0000   0x39 0x8a 0x55 0x11 0x0d                   9.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 46 ResultTotals (2013, 0, 17, 13, 13, 49) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x50                   ....P
    decimal
              7    0    0    4   80
    datetime ((2013, 0, 17, 13, 13, 49))
    0000   0x31 0x0d 0x6d 0x31 0x0d                   1.m1.
    body (41)
    hex
    0000   0x05 0x00 0x7d 0x44 0xde 0x06 0x00 0x00    ..}D....
    0008   0x04 0x50 0x03 0x4c 0x4c 0x01 0x04 0x18    .P.LL...
    0010   0x00 0x5a 0x01 0x04 0x18 0x00 0xd4 0x52    .Z.....R
    0018   0x00 0x30 0x12 0x00 0x00 0x00 0x05 0x04    .0......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  125   68  222    6    0    0
              4   80    3   76   76    1    4   24
              0   90    1    4   24    0  212   82
              0   48   18    0    0    0    5    4
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 47 LowReservoir 2013-02-18T00:22:30 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-02-18T00:22:30)
    0000   0x1e 0x96 0x00 0x12 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 48 CalBGForPH 2013-02-18T00:28:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-02-18T00:28:27)
    0000   0x1b 0x9c 0x20 0x12 0x0d                   .. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 49 CalBGForPH 2013-02-18T00:28:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-02-18T00:28:42)
    0000   0x2a 0x9c 0x20 0x12 0x0d                   *. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 Rewind 2013-02-18T19:16:45 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-02-18T19:16:45)
    0000   0x2d 0x90 0x13 0x12 0x0d                   -....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 Prime 2013-02-18T19:19:15 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2e                   .....
    decimal
              3    0    0    0   46
    datetime (2013-02-18T19:19:15)
    0000   0x0f 0x93 0x33 0x12 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 52 Prime 2013-02-18T19:19:47 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-02-18T19:19:47)
    0000   0x2f 0x93 0x13 0x12 0x0d                   /....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 CalBGForPH 2013-02-18T20:21:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 81}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2013-02-18T20:21:55)
    0000   0x37 0x95 0x34 0x12 0x0d                   7.4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 54 BolusWizard 2013-02-18T20:22:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 81,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 3.6,
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
    datetime (2013-02-18T20:22:30)
    0000   0x1e 0x96 0x14 0x12 0x0d                   .....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0xfa 0x24 0xf0    /P.-j.$.
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             47   80   13   45  106  250   36  240
              0    0    0   30  125
    HOUR BITS: [1, 0, 0]
#### RECORD 55 Bolus 2013-02-18T20:22:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-02-18T20:22:30)
    0000   0x1e 0x96 0x54 0x12 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 BolusWizard 2013-02-18T20:31:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 6,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.4,
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
    datetime (2013-02-18T20:31:59)
    0000   0x3b 0x9f 0x14 0x12 0x0d                   ;....
    body (13)
    hex
    0000   0x06 0x50 0x0d 0x2d 0x6a 0x00 0x04 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
              6   80   13   45  106    0    4    0
              0    0    0    4  125
    HOUR BITS: [1, 0, 0]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 0.75, 'curve': 4},
 {'age': 17, 'amount': 2.25, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x1e 0x07 0x04 0x5a 0x11 0x04    \....Z..
    decimal
             92    8   30    7    4   90   17    4
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-02-18T20:31:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-02-18T20:31:59)
    0000   0x3b 0x9f 0x54 0x12 0x0d                   ;.T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 CalBGForPH 2013-02-18T22:37:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-02-18T22:37:31)
    0000   0x1f 0xa5 0x36 0x12 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 60 BolusWizard 2013-02-18T22:38:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 160,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2013-02-18T22:38:06)
    0000   0x06 0xa6 0x16 0x12 0x0d                   .....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x07 0x0d 0x00    .P.-j...
    0008   0x00 0x0c 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    7   13    0
              0   12    0   13  125
    HOUR BITS: [1, 0, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 134, 'amount': 1.15, 'curve': 4},
 {'age': 144, 'amount': 2.25, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2e 0x86 0x04 0x5a 0x90 0x04    \....Z..
    decimal
             92    8   46  134    4   90  144    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-02-18T22:38:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-02-18T22:38:06)
    0000   0x06 0xa6 0x56 0x12 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 63 CalBGForPH 2013-02-18T23:55:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 192}
```
    op hex (2)
    0000   0x0a 0xc0                                  ..
    decimal
             10  192
    datetime (2013-02-18T23:55:09)
    0000   0x09 0xb7 0x37 0x12 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 64 BolusWizard 2013-02-18T23:55:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 192,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 1.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc0                                  [.
    decimal
             91  192
    datetime (2013-02-18T23:55:33)
    0000   0x21 0xb7 0x17 0x12 0x0d                   !....
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x0e 0x12 0x00    .P.-j...
    0008   0x00 0x0c 0x00 0x14 0x7d                   ....}
    decimal
             24   80   13   45  106   14   18    0
              0   12    0   20  125
    HOUR BITS: [1, 0, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 81, 'amount': 1.3, 'curve': 4},
 {'age': 211, 'amount': 1.15, 'curve': 4},
 {'age': 221, 'amount': 2.25, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x51 0x04 0x2e 0xd3 0x04    \.4Q....
    0008   0x5a 0xdd 0x04                             Z..
    decimal
             92   11   52   81    4   46  211    4
             90  221    4
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-02-18T23:55:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-02-18T23:55:33)
    0000   0x21 0xb7 0x57 0x12 0x0d                   !.W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 67 ResultTotals (2013, 0, 18, 13, 13, 50) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x8e                   .....
    decimal
              7    0    0    4  142
    datetime ((2013, 0, 18, 13, 13, 50))
    0000   0x32 0x0d 0x6d 0x32 0x0d                   2.m2.
    body (41)
    hex
    0000   0x05 0x00 0x89 0x51 0xc0 0x05 0x00 0x00    ...Q....
    0008   0x04 0x8e 0x03 0x82 0x4d 0x01 0x0c 0x17    ....M...
    0010   0x00 0x5f 0x01 0x0c 0x17 0x01 0x04 0x61    ._.....a
    0018   0x00 0x08 0x03 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  137   81  192    5    0    0
              4  142    3  130   77    1   12   23
              0   95    1   12   23    1    4   97
              0    8    3    0    0    0    4    3
              0    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 68 BolusWizard 2013-02-19T00:10:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 10,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.7,
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
    datetime (2013-02-19T00:10:58)
    0000   0x3a 0x8a 0x00 0x13 0x0d                   :....
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106    0    7    0
              0    0    0    7  125
    HOUR BITS: [1, 0, 0]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 2.0, 'curve': 4},
 {'age': 96, 'amount': 1.3, 'curve': 4},
 {'age': 226, 'amount': 1.15, 'curve': 4},
 {'age': 236, 'amount': 2.25, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x10 0x04 0x34 0x60 0x04    \.P..4`.
    0008   0x2e 0xe2 0x04 0x5a 0xec 0x04              ...Z..
    decimal
             92   14   80   16    4   52   96    4
             46  226    4   90  236    4
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-02-19T00:10:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-02-19T00:10:58)
    0000   0x3a 0x8a 0x40 0x13 0x0d                   :.@..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 71 CalBGForPH 2013-02-19T00:46:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 149}
```
    op hex (2)
    0000   0x0a 0x95                                  ..
    decimal
             10  149
    datetime (2013-02-19T00:46:40)
    0000   0x28 0xae 0x20 0x13 0x0d                   (. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 72 CalBGForPH 2013-02-19T01:53:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2013-02-19T01:53:09)
    0000   0x09 0xb5 0x21 0x13 0x0d                   ..!..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 73 CalBGForPH 2013-02-19T02:31:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-02-19T02:31:17)
    0000   0x11 0x9f 0x22 0x13 0x0d                   .."..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 74 CalBGForPH 2013-02-19T03:51:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-02-19T03:51:50)
    0000   0x32 0xb3 0x23 0x13 0x0d                   2.#..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 75 BolusWizard 2013-02-19T03:51:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-02-19T03:51:59)
    0000   0x3b 0xb3 0x03 0x13 0x0d                   ;....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x09 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x07 0x7d                   ....}
    decimal
              0   80   13   45  106    9    0    0
              0    2    0    7  125
    HOUR BITS: [1, 0, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 227, 'amount': 0.7, 'curve': 4},
 {'age': 237, 'amount': 2.0, 'curve': 4},
 {'age': 61, 'amount': 1.3, 'curve': 20},
 {'age': 191, 'amount': 1.15, 'curve': 20},
 {'age': 201, 'amount': 2.25, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x1c 0xe3 0x04 0x50 0xed 0x04    \....P..
    0008   0x34 0x3d 0x14 0x2e 0xbf 0x14 0x5a 0xc9    4=....Z.
    0010   0x14                                       .
    decimal
             92   17   28  227    4   80  237    4
             52   61   20   46  191   20   90  201
             20
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2013-02-19T03:51:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-02-19T03:51:59)
    0000   0x3b 0xb3 0x43 0x13 0x0d                   ;.C..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 78 PumpSuspend 2013-02-19T14:37:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-19T14:37:53)
    0000   0x35 0xa5 0x0e 0x13 0x0d                   5....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 PumpResume 2013-02-19T14:56:14 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-19T14:56:14)
    0000   0x0e 0xb8 0x0e 0x13 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 80 CalBGForPH 2013-02-19T15:20:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 219}
```
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2013-02-19T15:20:02)
    0000   0x02 0x94 0x2f 0x13 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 81 BolusWizard 2013-02-19T15:20:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 20,
 '_byte[7]': 0,
 'bg': 219,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
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
    0000   0x5b 0xdb                                  [.
    decimal
             91  219
    datetime (2013-02-19T15:20:07)
    0000   0x07 0x94 0x0f 0x13 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125
    HOUR BITS: [1, 0, 0]
#### RECORD 82 Bolus 2013-02-19T15:20:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-02-19T15:20:07)
    0000   0x07 0x94 0x4f 0x13 0x0d                   ..O..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 83 CalBGForPH 2013-02-19T16:15:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 192}
```
    op hex (2)
    0000   0x0a 0xc0                                  ..
    decimal
             10  192
    datetime (2013-02-19T16:15:13)
    0000   0x0d 0x8f 0x30 0x13 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-33.data: 84 records`
