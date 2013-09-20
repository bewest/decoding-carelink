## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-24.data
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
#### RECORD 2 MResultTotals (2013, 0, 22, 20, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 22, 20, 5, 0))
    0000   0x00 0x05 0xf4 0x56 0x0d                   ...V.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 3 Model522ResultTotals 2013-04-22T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-22T00:00:00)
    0000   0x56 0x0d 0x05 0x00 0xa4                   V....
    body (38)
    hex
    0000   0x73 0xf0 0x07 0x00 0x00 0x05 0xf4 0x03    s.......
    0008   0x48 0x37 0x02 0xac 0x2d 0x00 0xb0 0x02    H7..-...
    0010   0xac 0x2d 0x02 0x14 0x4e 0x00 0x98 0x16    .-..N...
    0018   0x00 0x00 0x00 0x07 0x03 0x02 0x02 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            115  240    7    0    0    5  244    3
             72   55    2  172   45    0  176    2
            172   45    2   20   78    0  152   22
              0    0    0    7    3    2    2    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 1, 0]
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
#### RECORD 17 MResultTotals (2013, 0, 23, 16, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 23, 16, 4, 0))
    0000   0x00 0x04 0xf0 0x57 0x0d                   ...W.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 18 Model522ResultTotals 2013-04-23T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-23T00:00:00)
    0000   0x57 0x0d 0x05 0x00 0xa4                   W....
    body (38)
    hex
    0000   0x88 0xc2 0x03 0x00 0x00 0x04 0xf0 0x03    ........
    0008   0x70 0x46 0x01 0x80 0x1e 0x00 0x71 0x01    pF....q.
    0010   0x80 0x1e 0x01 0x58 0x5a 0x00 0x28 0x0a    ...XZ.(.
    0018   0x00 0x00 0x00 0x03 0x01 0x01 0x01 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            136  194    3    0    0    4  240    3
            112   70    1  128   30    0  113    1
            128   30    1   88   90    0   40   10
              0    0    0    3    1    1    1    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 1, 0]
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

#### RECORD 32 Bolus unknown head[1], body[0] op[0x01]

    op hex (1)
    0000   0x01                                       .
    decimal
              1
    datetime (unknown)

    body (0)

`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-24.data: 33 records`
