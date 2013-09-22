## START analysis/xiali/raw//ReadHistoryData-page-13.data
#### RECORD 0 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 0.9, 'curve': 4},
 {'age': 14, 'amount': 1.5, 'curve': 20},
 {'age': 24, 'amount': 2.3, 'curve': 20},
 {'age': 164, 'amount': 1.2, 'curve': 20},
 {'age': 204, 'amount': 0.8, 'curve': 20},
 {'age': 214, 'amount': 0.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x24 0x32 0x04 0x3c 0x0e 0x14    \.$2.<..
    0008   0x5c 0x18 0x14 0x30 0xa4 0x14 0x20 0xcc    \..0.. .
    0010   0x14 0x18 0xd6 0x14                        ....
    decimal
             92   20   36   50    4   60   14   20
             92   24   20   48  164   20   32  204
             20   24  214   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-04-22T20:44:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-04-22T20:44:25)
    0000   0x59 0x2c 0x54 0x16 0x0d                   Y,T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 MResultTotals 2013-04-23T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xf4                   .....
    decimal
              7    0    0    5  244
    datetime (2013-04-23T00:00:00)
    0000   0x56 0x0d                                  V.
    body (0)

#### RECORD 3 Model522ResultTotals 2013-04-23T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-23T00:00:00)
    0000   0x56 0x0d                                  V.
    body (41)
    hex
    0000   0x05 0x00 0xa4 0x73 0xf0 0x07 0x00 0x00    ...s....
    0008   0x05 0xf4 0x03 0x48 0x37 0x02 0xac 0x2d    ...H7..-
    0010   0x00 0xb0 0x02 0xac 0x2d 0x02 0x14 0x4e    ....-..N
    0018   0x00 0x98 0x16 0x00 0x00 0x00 0x07 0x03    ........
    0020   0x02 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  164  115  240    7    0    0
              5  244    3   72   55    2  172   45
              0  176    2  172   45    2   20   78
              0  152   22    0    0    0    7    3
              2    2    0   12    0  232    0    0
              0

#### RECORD 4 PumpSuspend 2013-04-23T13:35:37 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-23T13:35:37)
    0000   0x65 0x23 0x0d 0x17 0x0d                   e#...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 PumpResume 2013-04-23T14:03:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-23T14:03:35)
    0000   0x63 0x03 0x0e 0x17 0x0d                   c....
    body (0)

#### RECORD 6 CalBGForPH 2013-04-23T14:30:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-04-23T14:30:56)
    0000   0x78 0x1e 0x2e 0x17 0x0d                   x....
    body (0)

#### RECORD 7 BolusWizard 2013-04-23T14:30:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
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
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2013-04-23T14:30:59)
    0000   0x7b 0x1e 0x0e 0x17 0x0d                   {....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    0    0    8  125

#### RECORD 8 Bolus 2013-04-23T14:30:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-04-23T14:30:59)
    0000   0x7b 0x1e 0x4e 0x17 0x0d                   {.N..
    body (0)

#### RECORD 9 BolusWizard 2013-04-23T14:50:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.3,
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
    datetime (2013-04-23T14:50:37)
    0000   0x65 0x32 0x0e 0x17 0x0d                   e2...
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0x00 0x2b 0x00    9P.-j.+.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             57   80   13   45  106    0   43    0
              0    0    0   43  125
    HOUR BITS: [0, 0, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 0.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x20 0x1a 0x04                   \. ..
    decimal
             92    5   32   26    4
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-04-23T14:50:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-04-23T14:50:37)
    0000   0x65 0x32 0x4e 0x17 0x0d                   e2N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 12 CalBGForPH 2013-04-23T16:54:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-04-23T16:54:32)
    0000   0x60 0x36 0x30 0x17 0x0d                   `60..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 CalBGForPH 2013-04-23T21:50:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-04-23T21:50:16)
    0000   0x50 0x32 0x35 0x17 0x0d                   P25..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 BolusWizard 2013-04-23T21:50:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-04-23T21:50:40)
    0000   0x68 0x32 0x15 0x17 0x0d                   h2...
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0x02 0x2b 0x00    8P.-j.+.
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             56   80   13   45  106    2   43    0
              0    0    0   45  125
    HOUR BITS: [0, 0, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 170, 'amount': 4.3, 'curve': 20},
 {'age': 190, 'amount': 0.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xac 0xaa 0x14 0x20 0xbe 0x14    \.... ..
    decimal
             92    8  172  170   20   32  190   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-04-23T21:50:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-04-23T21:50:40)
    0000   0x68 0x32 0x55 0x17 0x0d                   h2U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 MResultTotals 2013-04-24T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf0                   .....
    decimal
              7    0    0    4  240
    datetime (2013-04-24T00:00:00)
    0000   0x57 0x0d                                  W.
    body (0)

#### RECORD 18 Model522ResultTotals 2013-04-24T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-24T00:00:00)
    0000   0x57 0x0d                                  W.
    body (41)
    hex
    0000   0x05 0x00 0xa4 0x88 0xc2 0x03 0x00 0x00    ........
    0008   0x04 0xf0 0x03 0x70 0x46 0x01 0x80 0x1e    ...pF...
    0010   0x00 0x71 0x01 0x80 0x1e 0x01 0x58 0x5a    .q....XZ
    0018   0x00 0x28 0x0a 0x00 0x00 0x00 0x03 0x01    .(......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  164  136  194    3    0    0
              4  240    3  112   70    1  128   30
              0  113    1  128   30    1   88   90
              0   40   10    0    0    0    3    1
              1    1    0   12    0  232    0    0
              0

#### RECORD 19 PumpSuspend 2013-04-24T07:08:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-24T07:08:17)
    0000   0x51 0x08 0x07 0x18 0x0d                   Q....
    body (0)

#### RECORD 20 PumpResume 2013-04-24T07:26:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-24T07:26:37)
    0000   0x65 0x1a 0x07 0x18 0x0d                   e....
    body (0)

#### RECORD 21 CalBGForPH 2013-04-24T10:34:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-04-24T10:34:27)
    0000   0x5b 0x22 0x2a 0x18 0x0d                   ["*..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 BolusWizard 2013-04-24T10:35:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 116,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 30,
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
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-04-24T10:35:05)
    0000   0x45 0x23 0x0a 0x18 0x0d                   E#...
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [0, 0, 1]
#### RECORD 23 Bolus 2013-04-24T10:35:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-04-24T10:35:05)
    0000   0x45 0x23 0x4a 0x18 0x0d                   E#J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 24 CalBGForPH 2013-04-24T11:15:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-04-24T11:15:58)
    0000   0x7a 0x0f 0x2b 0x18 0x0d                   z.+..
    body (0)

#### RECORD 25 CalBGForPH 2013-04-24T18:19:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-04-24T18:19:58)
    0000   0x7a 0x13 0x32 0x18 0x0d                   z.2..
    body (0)

#### RECORD 26 ChangeTimeDisplay 2013-04-24T18:21:20 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-04-24T18:21:20)
    0000   0x54 0x15 0x12 0x18 0x0d                   T....
    body (0)

#### RECORD 27 ChangeTime 2013-04-24T18:21:25 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-04-24T18:21:25)
    0000   0x59 0x15 0x12 0x18 0x0d                   Y....
    body (0)

#### RECORD 28 NewTimeSet 2013-04-24T15:21:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-04-24T15:21:00)
    0000   0x40 0x15 0x0f 0x18 0x0d                   @....
    body (0)

#### RECORD 29 CalBGForPH 2013-04-24T15:21:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-04-24T15:21:31)
    0000   0x5f 0x15 0x2f 0x18 0x0d                   _./..
    body (0)

#### RECORD 30 BolusWizard 2013-04-24T15:21:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-04-24T15:21:49)
    0000   0x71 0x15 0x0f 0x18 0x0d                   q....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x00 0x1b 0x00    $P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    0   27    0
              0    0    0   27  125

#### RECORD 31 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 2.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0xd3 0x14                   \.\..
    decimal
             92    5   92  211   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-04-24T15:21:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-04-24T15:21:49)
    0000   0x71 0x15 0x4f 0x18 0x0d                   q.O..
    body (0)

#### RECORD 33 PumpSuspend 2013-04-24T16:19:22 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-24T16:19:22)
    0000   0x56 0x13 0x10 0x18 0x0d                   V....
    body (0)

#### RECORD 34 PumpResume 2013-04-24T17:56:45 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-24T17:56:45)
    0000   0x6d 0x38 0x11 0x18 0x0d                   m8...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 CalBGForPH 2013-04-24T17:56:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2013-04-24T17:56:53)
    0000   0x75 0x38 0x31 0x18 0x0d                   u81..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 CalBGForPH 2013-04-24T19:50:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-04-24T19:50:07)
    0000   0x47 0x32 0x33 0x18 0x0d                   G23..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 CalBGForPH 2013-04-24T20:17:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-04-24T20:17:29)
    0000   0x5d 0x11 0x34 0x18 0x0d                   ].4..
    body (0)

#### RECORD 38 BolusWizard 2013-04-24T20:18:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 120,
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
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-04-24T20:18:11)
    0000   0x4b 0x12 0x14 0x18 0x0d                   K....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125

#### RECORD 39 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0x30 0x14                   \.l0.
    decimal
             92    5  108   48   20
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-04-24T20:18:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-04-24T20:18:11)
    0000   0x4b 0x12 0x54 0x18 0x0d                   K.T..
    body (0)

#### RECORD 41 CalBGForPH 2013-04-24T21:01:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2013-04-24T21:01:19)
    0000   0x53 0x01 0x35 0x18 0x0d                   S.5..
    body (0)

#### RECORD 42 MResultTotals 2013-04-25T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime (2013-04-25T00:00:00)
    0000   0x58 0x0d                                  X.
    body (0)

#### RECORD 43 Model522ResultTotals 2013-04-25T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-25T00:00:00)
    0000   0x58 0x0d                                  X.
    body (41)
    hex
    0000   0x05 0x00 0x78 0x45 0xa3 0x08 0x00 0x00    ..xE....
    0008   0x04 0xd2 0x03 0xae 0x4c 0x01 0x24 0x18    ....L.$.
    0010   0x00 0x61 0x01 0x24 0x18 0x01 0x24 0x64    .a.$..$d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  120   69  163    8    0    0
              4  210    3  174   76    1   36   24
              0   97    1   36   24    1   36  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0

#### RECORD 44 PumpSuspend 2013-04-25T06:45:50 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-25T06:45:50)
    0000   0x72 0x2d 0x06 0x19 0x0d                   r-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 PumpResume 2013-04-25T06:58:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-25T06:58:29)
    0000   0x5d 0x3a 0x06 0x19 0x0d                   ]:...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 46 CalBGForPH 2013-04-25T07:08:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2013-04-25T07:08:46)
    0000   0x6e 0x08 0x27 0x19 0x0d                   n.'..
    body (0)

#### RECORD 47 BolusWizard 2013-04-25T07:08:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 140,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
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
    0000   0x5b 0x8c                                  [.
    decimal
             91  140
    datetime (2013-04-25T07:08:49)
    0000   0x71 0x08 0x07 0x19 0x0d                   q....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x03 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106    3    0    0
              0    0    0    3  125

#### RECORD 48 Bolus 2013-04-25T07:08:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-04-25T07:08:49)
    0000   0x71 0x08 0x47 0x19 0x0d                   q.G..
    body (0)

#### RECORD 49 CalBGForPH 2013-04-25T08:56:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-04-25T08:56:56)
    0000   0x78 0x38 0x28 0x19 0x0d                   x8(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 CalBGForPH 2013-04-25T09:01:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2013-04-25T09:01:59)
    0000   0x7b 0x01 0x29 0x19 0x0d                   {.)..
    body (0)

#### RECORD 51 BolusWizard 2013-04-25T09:03:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 140,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.4,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8c                                  [.
    decimal
             91  140
    datetime (2013-04-25T09:03:07)
    0000   0x47 0x03 0x09 0x19 0x0d                   G....
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0x03 0x35 0x00    EP.-j.5.
    0008   0x00 0x02 0x00 0x36 0x7d                   ...6}
    decimal
             69   80   13   45  106    3   53    0
              0    2    0   54  125

#### RECORD 52 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 119, 'amount': 0.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x0c 0x77 0x04                   \..w.
    decimal
             92    5   12  119    4
    datetime (unknown)

    body (0)

#### RECORD 53 LowReservoir 2013-04-25T09:03:52 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-04-25T09:03:52)
    0000   0x74 0x03 0x09 0x19 0x0d                   t....
    body (0)

#### RECORD 54 Bolus 2013-04-25T09:03:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4, 'dual_component': '??', 'programmed': 5.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x36 0x36 0x00                        .66.
    decimal
              1   54   54    0
    datetime (2013-04-25T09:03:07)
    0000   0x47 0x03 0x49 0x19 0x0d                   G.I..
    body (0)

#### RECORD 55 CalBGForPH 2013-04-25T12:24:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 59}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2013-04-25T12:24:21)
    0000   0x55 0x18 0x2c 0x19 0x0d                   U.,..
    body (0)

#### RECORD 56 CalBGForPH 2013-04-25T14:03:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 83}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-04-25T14:03:54)
    0000   0x76 0x03 0x2e 0x19 0x0d                   v....
    body (0)

#### RECORD 57 BolusWizard 2013-04-25T14:04:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 83,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 39,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 3.0,
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
    datetime (2013-04-25T14:04:16)
    0000   0x50 0x04 0x0e 0x19 0x0d                   P....
    body (13)
    hex
    0000   0x27 0x50 0x0d 0x2d 0x6a 0xfb 0x1e 0xf0    'P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
             39   80   13   45  106  251   30  240
              0    0    0   25  125

#### RECORD 58 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 4.15, 'curve': 20},
 {'age': 54, 'amount': 1.25, 'curve': 20},
 {'age': 164, 'amount': 0.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa6 0x2c 0x14 0x32 0x36 0x14    \..,.26.
    0008   0x0c 0xa4 0x14                             ...
    decimal
             92   11  166   44   20   50   54   20
             12  164   20
    datetime (unknown)

    body (0)

#### RECORD 59 LowReservoir 2013-04-25T14:04:24 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-04-25T14:04:24)
    0000   0x58 0x04 0x0e 0x19 0x0d                   X....
    body (0)

#### RECORD 60 Bolus 2013-04-25T14:04:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-04-25T14:04:16)
    0000   0x50 0x04 0x4e 0x19 0x0d                   P.N..
    body (0)

#### RECORD 61 BolusWizard 2013-04-25T15:12:07 head[2], body[13] op[0x5b]
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
    datetime (2013-04-25T15:12:07)
    0000   0x47 0x0c 0x0f 0x19 0x0d                   G....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125

#### RECORD 62 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 2.5, 'curve': 4},
 {'age': 112, 'amount': 4.15, 'curve': 20},
 {'age': 122, 'amount': 1.25, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x64 0x44 0x04 0xa6 0x70 0x14    \.dD..p.
    0008   0x32 0x7a 0x14                             2z.
    decimal
             92   11  100   68    4  166  112   20
             50  122   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2013-04-25T15:12:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-04-25T15:12:07)
    0000   0x47 0x0c 0x4f 0x19 0x0d                   G.O..
    body (0)

#### RECORD 64 Rewind 2013-04-25T16:36:17 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-04-25T16:36:17)
    0000   0x51 0x24 0x10 0x19 0x0d                   Q$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 65 Rewind 2013-04-25T16:39:18 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-04-25T16:39:18)
    0000   0x52 0x27 0x10 0x19 0x0d                   R'...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 66 Prime 2013-04-25T16:40:09 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x15                   .....
    decimal
              3    0    0    0   21
    datetime (2013-04-25T16:40:09)
    0000   0x49 0x28 0x30 0x19 0x0d                   I(0..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 67 Prime 2013-04-25T16:40:34 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-25T16:40:34)
    0000   0x62 0x28 0x10 0x19 0x0d                   b(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 68 CalBGForPH 2013-04-25T17:16:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-04-25T17:16:53)
    0000   0x75 0x10 0x31 0x19 0x0d                   u.1..
    body (0)

#### RECORD 69 CalBGForPH 2013-04-25T20:24:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2013-04-25T20:24:49)
    0000   0x71 0x18 0x34 0x19 0x0d                   q.4..
    body (0)

#### RECORD 70 CalBGForPH 2013-04-25T21:15:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 208}
```
    op hex (2)
    0000   0x0a 0xd0                                  ..
    decimal
             10  208
    datetime (2013-04-25T21:15:46)
    0000   0x6e 0x0f 0x35 0x19 0x0d                   n.5..
    body (0)

#### RECORD 71 CalBGForPH 2013-04-25T21:15:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-04-25T21:15:49)
    0000   0x71 0x0f 0x35 0x19 0x0d                   q.5..
    body (0)

#### RECORD 72 BolusWizard 2013-04-25T21:17:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 18,
 '_byte[7]': 0,
 'bg': 206,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 2.1,
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
    datetime (2013-04-25T21:17:32)
    0000   0x60 0x11 0x15 0x19 0x0d                   `....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x12 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             28   80   13   45  106   18   21    0
              0    0    0   39  125

#### RECORD 73 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 117, 'amount': 0.9, 'curve': 20},
 {'age': 177, 'amount': 2.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x75 0x14 0x64 0xb1 0x14    \.$u.d..
    decimal
             92    8   36  117   20  100  177   20
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2013-04-25T21:17:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-04-25T21:17:32)
    0000   0x60 0x11 0x55 0x19 0x0d                   `.U..
    body (0)

#### RECORD 75 CalBGForPH 2013-04-25T22:31:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 49}
```
    op hex (2)
    0000   0x0a 0x31                                  .1
    decimal
             10   49
    datetime (2013-04-25T22:31:43)
    0000   0x6b 0x1f 0x36 0x19 0x0d                   k.6..
    body (0)

#### RECORD 76 CalBGForPH 2013-04-25T22:55:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-04-25T22:55:09)
    0000   0x49 0x37 0x36 0x19 0x0d                   I76..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 77 MResultTotals 2013-04-26T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x82                   .....
    decimal
              7    0    0    5  130
    datetime (2013-04-26T00:00:00)
    0000   0x59 0x0d                                  Y.
    body (0)

#### RECORD 78 Model522ResultTotals 2013-04-26T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-26T00:00:00)
    0000   0x59 0x0d                                  Y.
    body (41)
    hex
    0000   0x05 0x00 0x7c 0x31 0xd0 0x0b 0x00 0x00    ..|1....
    0008   0x05 0x82 0x03 0x7a 0x3f 0x02 0x08 0x25    ...z?..%
    0010   0x00 0x94 0x02 0x08 0x25 0x01 0xb0 0x53    ....%..S
    0018   0x00 0x58 0x11 0x00 0x00 0x00 0x05 0x02    .X......
    0020   0x01 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  124   49  208   11    0    0
              5  130    3  122   63    2    8   37
              0  148    2    8   37    1  176   83
              0   88   17    0    0    0    5    2
              1    2    0   12    0  232    0    0
              0

#### RECORD 79 CalBGForPH 2013-04-26T05:51:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2013-04-26T05:51:54)
    0000   0x76 0x33 0x25 0x1a 0x0d                   v3%..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 80 BolusWizard 2013-04-26T05:51:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 180,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
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
    0000   0x5b 0xb4                                  [.
    decimal
             91  180
    datetime (2013-04-26T05:51:56)
    0000   0x78 0x33 0x05 0x1a 0x0d                   x3...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    0    0   12  125
    HOUR BITS: [0, 0, 1]
#### RECORD 81 Bolus 2013-04-26T05:51:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-04-26T05:51:56)
    0000   0x78 0x33 0x45 0x1a 0x0d                   x3E..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 82 CalBGForPH 2013-04-26T08:34:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-04-26T08:34:44)
    0000   0x6c 0x22 0x28 0x1a 0x0d                   l"(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 83 CalBGForPH 2013-04-26T08:35:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 150}
```
    op hex (2)
    0000   0x0a 0x96                                  ..
    decimal
             10  150
    datetime (2013-04-26T08:35:41)
    0000   0x69 0x23 0x28 0x1a 0x0d                   i#(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 84 BolusWizard 2013-04-26T08:36:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 5,
 '_byte[7]': 0,
 'bg': 150,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x96                                  [.
    decimal
             91  150
    datetime (2013-04-26T08:36:07)
    0000   0x47 0x24 0x08 0x1a 0x0d                   G$...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x05 0x2e 0x00    <P.-j...
    0008   0x00 0x03 0x00 0x30 0x7d                   ...0}
    decimal
             60   80   13   45  106    5   46    0
              0    3    0   48  125
    HOUR BITS: [0, 0, 1]
#### RECORD 85 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 172, 'amount': 1.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0xac 0x04                   \.0..
    decimal
             92    5   48  172    4
    datetime (unknown)

    body (0)

#### RECORD 86 Bolus 2013-04-26T08:36:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2013-04-26T08:36:07)
    0000   0x47 0x24 0x48 0x1a 0x0d                   G$H..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 87 CalBGForPH 2013-04-26T10:13:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-04-26T10:13:27)
    0000   0x5b 0x0d 0x2a 0x1a 0x0d                   [.*..
    body (0)

#### RECORD 88 CalBGForPH 2013-04-26T11:12:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-04-26T11:12:20)
    0000   0x54 0x0c 0x2b 0x1a 0x0d                   T.+..
    body (0)

#### RECORD 89 CalBGForPH 2013-04-26T13:24:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-04-26T13:24:15)
    0000   0x4f 0x18 0x2d 0x1a 0x0d                   O.-..
    body (0)

#### RECORD 90 CalBGForPH 2013-04-26T13:24:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 150}
```
    op hex (2)
    0000   0x0a 0x96                                  ..
    decimal
             10  150
    datetime (2013-04-26T13:24:20)
    0000   0x54 0x18 0x2d 0x1a 0x0d                   T.-..
    body (0)

#### RECORD 91 BolusWizard 2013-04-26T13:24:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 5,
 '_byte[7]': 0,
 'bg': 150,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
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
    0000   0x5b 0x96                                  [.
    decimal
             91  150
    datetime (2013-04-26T13:24:23)
    0000   0x57 0x18 0x0d 0x1a 0x0d                   W....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x05 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106    5    0    0
              0    0    0    5  125

#### RECORD 92 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x92                                  ..
    decimal
              0  146
    datetime (unknown)

    body (0)

`end analysis/xiali/raw//ReadHistoryData-page-13.data: 93 records`
