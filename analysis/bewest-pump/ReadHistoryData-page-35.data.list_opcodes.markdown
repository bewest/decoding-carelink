## START logs/ReadHistoryData-page-35.data
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 0.8, 'curve': 4},
 {'age': 68, 'amount': 5.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x5e 0x04 0xec 0x44 0x14    \. ^..D.
    decimal
             92    8   32   94    4  236   68   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-02-09T13:28:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-02-09T13:28:39)
    0000   0x27 0x9c 0x4d 0x09 0x0d                   '.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 2 CalBGForPH 2013-02-09T16:17:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 214}
```
    op hex (2)
    0000   0x0a 0xd6                                  ..
    decimal
             10  214
    datetime (2013-02-09T16:17:57)
    0000   0x39 0x91 0x30 0x09 0x0d                   9.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 BolusWizard 2013-02-09T16:18:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 214,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd6                                  [.
    decimal
             91  214
    datetime (2013-02-09T16:18:03)
    0000   0x03 0x92 0x10 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x13 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   19    0    0
              0    6    0   13  125
    HOUR BITS: [1, 0, 0]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 174, 'amount': 2.9, 'curve': 4},
 {'age': 8, 'amount': 0.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0xae 0x04 0x20 0x08 0x14    \.t.. ..
    decimal
             92    8  116  174    4   32    8   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-02-09T16:18:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-02-09T16:18:03)
    0000   0x03 0x92 0x50 0x09 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 LowReservoir 2013-02-09T19:31:34 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-02-09T19:31:34)
    0000   0x22 0x9f 0x13 0x09 0x0d                   "....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 CalBGForPH 2013-02-09T23:27:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-02-09T23:27:22)
    0000   0x16 0x9b 0x37 0x09 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 BolusWizard 2013-02-09T23:27:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-02-09T23:27:54)
    0000   0x36 0x9b 0x17 0x09 0x0d                   6....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x00 0x26 0x00    2P.-j.&.
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
             50   80   13   45  106    0   38    0
              0    0    0   38  125
    HOUR BITS: [1, 0, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 177, 'amount': 1.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x34 0xb1 0x14                   \.4..
    decimal
             92    5   52  177   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-02-09T23:27:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-02-09T23:27:54)
    0000   0x36 0x9b 0x57 0x09 0x0d                   6.W..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 BolusWizard 2013-02-09T23:54:47 head[2], body[13] op[0x5b]
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
    datetime (2013-02-09T23:54:47)
    0000   0x2f 0xb6 0x17 0x09 0x0d                   /....
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             26   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [1, 0, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 3.8, 'curve': 4},
 {'age': 204, 'amount': 1.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x98 0x1e 0x04 0x34 0xcc 0x14    \....4..
    decimal
             92    8  152   30    4   52  204   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-02-09T23:54:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-02-09T23:54:47)
    0000   0x2f 0xb6 0x57 0x09 0x0d                   /.W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 14 LowReservoir 2013-02-09T23:56:50 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-02-09T23:56:50)
    0000   0x32 0xb8 0x17 0x09 0x0d                   2....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 15 ResultTotals (2013, 0, 9, 13, 13, 41) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x02                   .....
    decimal
              7    0    0    6    2
    datetime ((2013, 0, 9, 13, 13, 41))
    0000   0x29 0x0d 0x6d 0x29 0x0d                   ).m).
    body (41)
    hex
    0000   0x05 0x10 0xa0 0x5e 0x89 0x0a 0x00 0x00    ...^....
    0008   0x06 0x02 0x03 0x66 0x39 0x02 0x9c 0x2b    ...f9..+
    0010   0x00 0x7a 0x02 0x9c 0x2b 0x01 0x68 0x36    .z..+.h6
    0018   0x01 0x34 0x2e 0x00 0x00 0x00 0x06 0x03    .4......
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  160   94  137   10    0    0
              6    2    3  102   57    2  156   43
              0  122    2  156   43    1  104   54
              1   52   46    0    0    0    6    3
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 16 PumpSuspend 2013-02-10T08:52:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-10T08:52:15)
    0000   0x0f 0xb4 0x08 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 17 PumpResume 2013-02-10T09:25:10 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-10T09:25:10)
    0000   0x0a 0x99 0x09 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 18 Rewind 2013-02-10T09:25:14 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-02-10T09:25:14)
    0000   0x0e 0x99 0x09 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 19 Prime 2013-02-10T09:26:44 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.2, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2a                   ....*
    decimal
              3    0    0    0   42
    datetime (2013-02-10T09:26:44)
    0000   0x2c 0x9a 0x29 0x0a 0x0d                   ,.)..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 Prime 2013-02-10T09:27:06 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-02-10T09:27:06)
    0000   0x06 0x9b 0x09 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 CalBGForPH 2013-02-10T09:32:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 339}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-02-10T09:32:48)
    0000   0x30 0xa0 0x29 0x0a 0x8d                   0.)..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 22 BolusWizard 2013-02-10T09:33:04 head[2], body[13] op[0x5b]
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
    datetime (2013-02-10T09:33:04)
    0000   0x04 0xa1 0x09 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2f 0x00 0x00    .Q.-j/..
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
              0   81   13   45  106   47    0    0
              0    0    0   47  125
    HOUR BITS: [1, 0, 1]
#### RECORD 23 Bolus 2013-02-10T09:33:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2013-02-10T09:33:04)
    0000   0x04 0xa1 0x49 0x0a 0x0d                   ..I..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 TempBasal 2013-02-10T10:08:05 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.1}
```
    op hex (2)
    0000   0x33 0x2c                                  3,
    decimal
             51   44
    datetime (2013-02-10T10:08:05)
    0000   0x05 0x88 0x0a 0x0a 0x0d                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 25 TempBasalDuration 2013-02-10T10:08:05 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-02-10T10:08:05)
    0000   0x05 0x88 0x0a 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 26 TempBasal 2013-02-10T10:08:16 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.1}
```
    op hex (2)
    0000   0x33 0x2c                                  3,
    decimal
             51   44
    datetime (2013-02-10T10:08:16)
    0000   0x10 0x88 0x0a 0x0a 0x0d                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 27 TempBasalDuration 2013-02-10T10:08:16 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-02-10T10:08:16)
    0000   0x10 0x88 0x0a 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 28 BolusWizard 2013-02-10T10:24:54 head[2], body[13] op[0x5b]
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
    datetime (2013-02-10T10:24:54)
    0000   0x36 0x98 0x0a 0x0a 0x0d                   6....
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106    0    7    0
              0    0    0    7  125
    HOUR BITS: [1, 0, 0]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 3.4, 'curve': 4},
 {'age': 60, 'amount': 1.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x88 0x32 0x04 0x38 0x3c 0x04    \..2.8<.
    decimal
             92    8  136   50    4   56   60    4
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-02-10T10:24:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-02-10T10:24:54)
    0000   0x36 0x98 0x4a 0x0a 0x0d                   6.J..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 CalBGForPH 2013-02-10T11:56:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-02-10T11:56:37)
    0000   0x25 0xb8 0x2b 0x0a 0x0d                   %.+..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 32 BolusWizard 2013-02-10T13:06:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.5,
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
    datetime (2013-02-10T13:06:12)
    0000   0x0c 0x86 0x0d 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125
    HOUR BITS: [1, 0, 0]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 0.7, 'curve': 4},
 {'age': 212, 'amount': 3.4, 'curve': 4},
 {'age': 222, 'amount': 1.4, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x1c 0xa2 0x04 0x88 0xd4 0x04    \.......
    0008   0x38 0xde 0x04                             8..
    decimal
             92   11   28  162    4  136  212    4
             56  222    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-02-10T13:06:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-02-10T13:06:12)
    0000   0x0c 0x86 0x4d 0x0a 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 CalBGForPH 2013-02-10T16:29:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-02-10T16:29:52)
    0000   0x34 0x9d 0x30 0x0a 0x0d                   4.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 BolusWizard 2013-02-10T16:30:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 8,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-02-10T16:30:04)
    0000   0x04 0x9e 0x10 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0x02 0x06 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x06 0x7d                   ....}
    decimal
              8   80   13   45  106    2    6    0
              0    2    0    6  125
    HOUR BITS: [1, 0, 0]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 206, 'amount': 1.5, 'curve': 4},
 {'age': 110, 'amount': 0.7, 'curve': 20},
 {'age': 160, 'amount': 3.4, 'curve': 20},
 {'age': 170, 'amount': 1.4, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0xce 0x04 0x1c 0x6e 0x14    \.<...n.
    0008   0x88 0xa0 0x14 0x38 0xaa 0x14              ...8..
    decimal
             92   14   60  206    4   28  110   20
            136  160   20   56  170   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-02-10T16:30:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-02-10T16:30:04)
    0000   0x04 0x9e 0x50 0x0a 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 CalBGForPH 2013-02-10T20:02:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 236}
```
    op hex (2)
    0000   0x0a 0xec                                  ..
    decimal
             10  236
    datetime (2013-02-10T20:02:18)
    0000   0x12 0x82 0x34 0x0a 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 BolusWizard 2013-02-10T20:02:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 236,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xec                                  [.
    decimal
             91  236
    datetime (2013-02-10T20:02:26)
    0000   0x1a 0x82 0x14 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x18 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x17 0x7d                   ....}
    decimal
              0   80   13   45  106   24    0    0
              0    1    0   23  125
    HOUR BITS: [1, 0, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 218, 'amount': 0.6, 'curve': 4},
 {'age': 162, 'amount': 1.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0xda 0x04 0x3c 0xa2 0x14    \....<..
    decimal
             92    8   24  218    4   60  162   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-02-10T20:02:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-02-10T20:02:26)
    0000   0x1a 0x82 0x54 0x0a 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 43 CalBGForPH 2013-02-10T20:59:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-02-10T20:59:02)
    0000   0x02 0xbb 0x34 0x0a 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 44 BolusWizard 2013-02-10T20:59:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 146,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 3.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x92                                  [.
    decimal
             91  146
    datetime (2013-02-10T20:59:36)
    0000   0x24 0xbb 0x14 0x0a 0x0d                   $....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0x04 0x23 0x00    .P.-j.#.
    0008   0x00 0x14 0x00 0x23 0x7d                   ...#}
    decimal
             46   80   13   45  106    4   35    0
              0   20    0   35  125
    HOUR BITS: [1, 0, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 0.1, 'curve': 4},
 {'age': 65, 'amount': 2.3, 'curve': 4},
 {'age': 19, 'amount': 0.6, 'curve': 20},
 {'age': 219, 'amount': 1.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x04 0x37 0x04 0x5c 0x41 0x04    \..7.\A.
    0008   0x18 0x13 0x14 0x3c 0xdb 0x14              ...<..
    decimal
             92   14    4   55    4   92   65    4
             24   19   20   60  219   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-02-10T20:59:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-02-10T20:59:36)
    0000   0x24 0xbb 0x54 0x0a 0x0d                   $.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 47 BolusWizard 2013-02-10T21:31:23 head[2], body[13] op[0x5b]
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
    datetime (2013-02-10T21:31:23)
    0000   0x17 0x9f 0x15 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x00 0x18 0x00     P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
             32   80   13   45  106    0   24    0
              0    0    0   24  125
    HOUR BITS: [1, 0, 0]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 3.5, 'curve': 4},
 {'age': 87, 'amount': 0.1, 'curve': 4},
 {'age': 97, 'amount': 2.3, 'curve': 4},
 {'age': 51, 'amount': 0.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x8c 0x25 0x04 0x04 0x57 0x04    \..%..W.
    0008   0x5c 0x61 0x04 0x18 0x33 0x14              \a..3.
    decimal
             92   14  140   37    4    4   87    4
             92   97    4   24   51   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-02-10T21:31:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-02-10T21:31:23)
    0000   0x17 0x9f 0x55 0x0a 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 CalBGForPH 2013-02-10T23:32:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2013-02-10T23:32:08)
    0000   0x08 0xa0 0x37 0x0a 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 51 ResultTotals (2013, 0, 10, 13, 13, 42) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe8                   .....
    decimal
              7    0    0    5  232
    datetime ((2013, 0, 10, 13, 13, 42))
    0000   0x2a 0x0d 0x6d 0x2a 0x0d                   *.m*.
    body (41)
    hex
    0000   0x05 0x10 0xbd 0x5a 0x53 0x06 0x00 0x00    ...ZS...
    0008   0x05 0xe8 0x03 0x6c 0x3a 0x02 0x7c 0x2a    ...l:.|*
    0010   0x00 0x74 0x02 0x7c 0x2a 0x01 0x5c 0x37    .t.|*.\7
    0018   0x01 0x20 0x2d 0x00 0x00 0x00 0x07 0x05    . -.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  189   90   83    6    0    0
              5  232    3  108   58    2  124   42
              0  116    2  124   42    1   92   55
              1   32   45    0    0    0    7    5
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 52 CalBGForPH 2013-02-11T00:13:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-02-11T00:13:01)
    0000   0x01 0x8d 0x20 0x0b 0x0d                   .. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 PumpSuspend 2013-02-11T17:50:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-11T17:50:09)
    0000   0x09 0xb2 0x11 0x0b 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 54 PumpResume 2013-02-11T18:05:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-11T18:05:58)
    0000   0x3a 0x85 0x12 0x0b 0x0d                   :....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 55 CalBGForPH 2013-02-11T18:19:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-02-11T18:19:10)
    0000   0x0a 0x93 0x32 0x0b 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 BolusWizard 2013-02-11T18:19:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 3.4,
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
    datetime (2013-02-11T18:19:57)
    0000   0x39 0x93 0x12 0x0b 0x0d                   9....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x09 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             45   80   13   45  106    9   34    0
              0    0    0   43  125
    HOUR BITS: [1, 0, 0]
#### RECORD 57 Bolus 2013-02-11T18:19:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-02-11T18:19:57)
    0000   0x39 0x93 0x52 0x0b 0x0d                   9.R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 58 BolusWizard 2013-02-11T19:04:34 head[2], body[13] op[0x5b]
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
    datetime (2013-02-11T19:04:34)
    0000   0x22 0x84 0x13 0x0b 0x0d                   "....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 0, 0]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 4.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xac 0x32 0x04                   \..2.
    decimal
             92    5  172   50    4
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-02-11T19:04:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-02-11T19:04:35)
    0000   0x23 0x84 0x53 0x0b 0x0d                   #.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 61 CalBGForPH 2013-02-11T20:00:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2013-02-11T20:00:57)
    0000   0x39 0x80 0x34 0x0b 0x0d                   9.4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 CalBGForPH 2013-02-11T20:01:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 266}
```
    op hex (2)
    0000   0x0a 0x0a                                  ..
    decimal
             10   10
    datetime (2013-02-11T20:01:27)
    0000   0x1b 0x81 0x34 0x0b 0x8d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 63 BolusWizard 2013-02-11T20:01:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 266,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0a                                  [.
    decimal
             91   10
    datetime (2013-02-11T20:01:44)
    0000   0x2c 0x81 0x14 0x0b 0x0d                   ,....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x20 0x00 0x00 0x7d                   . ..}
    decimal
              0   81   13   45  106   31    0    0
              0   32    0    0  125
    HOUR BITS: [1, 0, 0]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 57, 'amount': 1.0, 'curve': 4},
 {'age': 107, 'amount': 4.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x39 0x04 0xac 0x6b 0x04    \.(9..k.
    decimal
             92    8   40   57    4  172  107    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-02-11T20:01:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-02-11T20:01:44)
    0000   0x2c 0x81 0x54 0x0b 0x0d                   ,.T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 66 BolusWizard 2013-02-11T20:26:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
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
    datetime (2013-02-11T20:26:27)
    0000   0x1b 0x9a 0x14 0x0b 0x0d                   .....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [1, 0, 0]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 0.3, 'curve': 4},
 {'age': 82, 'amount': 1.0, 'curve': 4},
 {'age': 132, 'amount': 4.3, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x20 0x04 0x28 0x52 0x04    \.. .(R.
    0008   0xac 0x84 0x04                             ...
    decimal
             92   11   12   32    4   40   82    4
            172  132    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-02-11T20:26:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-02-11T20:26:27)
    0000   0x1b 0x9a 0x54 0x0b 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 CalBGForPH 2013-02-11T20:52:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 306}
```
    op hex (2)
    0000   0x0a 0x32                                  .2
    decimal
             10   50
    datetime (2013-02-11T20:52:03)
    0000   0x03 0xb4 0x34 0x0b 0x8d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 70 CalBGForPH 2013-02-11T20:52:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 306}
```
    op hex (2)
    0000   0x0a 0x32                                  .2
    decimal
             10   50
    datetime (2013-02-11T20:52:33)
    0000   0x21 0xb4 0x34 0x0b 0x8d                   !.4..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 71 BolusWizard 2013-02-11T20:53:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 40,
 '_byte[7]': 0,
 'bg': 306,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 3.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x32                                  [2
    decimal
             91   50
    datetime (2013-02-11T20:53:17)
    0000   0x11 0xb5 0x14 0x0b 0x0d                   .....
    body (13)
    hex
    0000   0x31 0x51 0x0d 0x2d 0x6a 0x28 0x25 0x00    1Q.-j(%.
    0008   0x00 0x26 0x00 0x27 0x7d                   .&.'}
    decimal
             49   81   13   45  106   40   37    0
              0   38    0   39  125
    HOUR BITS: [1, 0, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 2.0, 'curve': 4},
 {'age': 59, 'amount': 0.3, 'curve': 4},
 {'age': 109, 'amount': 1.0, 'curve': 4},
 {'age': 159, 'amount': 4.3, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x1d 0x04 0x0c 0x3b 0x04    \.P...;.
    0008   0x28 0x6d 0x04 0xac 0x9f 0x04              (m....
    decimal
             92   14   80   29    4   12   59    4
             40  109    4  172  159    4
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-02-11T20:53:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-02-11T20:53:17)
    0000   0x11 0xb5 0x54 0x0b 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 74 CalBGForPH 2013-02-11T21:50:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 270}
```
    op hex (2)
    0000   0x0a 0x0e                                  ..
    decimal
             10   14
    datetime (2013-02-11T21:50:59)
    0000   0x3b 0xb2 0x35 0x0b 0x8d                   ;.5..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 75 ResultTotals (2013, 0, 11, 13, 13, 43) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x46                   ....F
    decimal
              7    0    0    5   70
    datetime ((2013, 0, 11, 13, 13, 43))
    0000   0x2b 0x0d 0x6d 0x2b 0x0d                   +.m+.
    body (41)
    hex
    0000   0x05 0x10 0xdf 0x46 0x32 0x07 0x00 0x00    ...F2...
    0008   0x05 0x46 0x03 0x7a 0x42 0x01 0xcc 0x22    .F.zB.."
    0010   0x00 0x87 0x01 0xcc 0x22 0x01 0x94 0x58    ...."..X
    0018   0x00 0x38 0x0c 0x00 0x00 0x00 0x05 0x02    .8......
    0020   0x01 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  223   70   50    7    0    0
              5   70    3  122   66    1  204   34
              0  135    1  204   34    1  148   88
              0   56   12    0    0    0    5    2
              1    2    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 76 PumpSuspend 2013-02-12T13:46:40 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-12T13:46:40)
    0000   0x28 0xae 0x0d 0x0c 0x0d                   (....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 77 PumpResume 2013-02-12T14:50:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-12T14:50:04)
    0000   0x04 0xb2 0x0e 0x0c 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 78 CalBGForPH 2013-02-12T15:10:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2013-02-12T15:10:58)
    0000   0x3a 0x8a 0x2f 0x0c 0x0d                   :./..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 79 BolusWizard 2013-02-12T15:12:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 141,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8d                                  [.
    decimal
             91  141
    datetime (2013-02-12T15:12:06)
    0000   0x06 0x8c 0x0f 0x0c 0x0d                   .....
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0x03 0x2c 0x00    :P.-j.,.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             58   80   13   45  106    3   44    0
              0    0    0   47  125
    HOUR BITS: [1, 0, 0]
#### RECORD 80 Bolus 2013-02-12T15:12:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-02-12T15:12:06)
    0000   0x06 0x8c 0x4f 0x0c 0x0d                   ..O..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 81 CalBGForPH 2013-02-12T16:58:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-02-12T16:58:35)
    0000   0x23 0xba 0x30 0x0c 0x0d                   #.0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 82 CalBGForPH 2013-02-12T21:24:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 219}
```
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2013-02-12T21:24:26)
    0000   0x1a 0x98 0x35 0x0c 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 83 BolusWizard 2013-02-12T21:25:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 20,
 '_byte[7]': 0,
 'bg': 219,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.8,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 3.8,
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
    datetime (2013-02-12T21:25:14)
    0000   0x0e 0x99 0x15 0x0c 0x0d                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x14 0x26 0x00    2P.-j.&.
    0008   0x00 0x00 0x00 0x3a 0x7d                   ...:}
    decimal
             50   80   13   45  106   20   38    0
              0    0    0   58  125
    HOUR BITS: [1, 0, 0]
#### RECORD 84 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xbb                                  ..
    decimal
              0  187
    datetime (unknown)
    0000   0xb7                                       .
    body (0)

`end logs/ReadHistoryData-page-35.data: 85 records`
