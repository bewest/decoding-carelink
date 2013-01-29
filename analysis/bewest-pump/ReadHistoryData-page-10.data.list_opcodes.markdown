## START logs/ReadHistoryData-page-10.data
#### RECORD 0 BolusWizard 2012-12-17T13:14:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 184,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.5,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0xb8                                  [.
    decimal
             91  184
    datetime (2012-12-17T13:14:48)
    0000   0xf0 0x0e 0x0d 0x11 0x0c                   .....
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0x0d 0x35 0x00    EP.-j.5.
    0008   0x00 0x01 0x00 0x41 0x7d                   ...A}
    decimal
             69   80   13   45  106   13   53    0
              0    1    0   65  125

#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 240, 'amount': 1.05, 'curve': 4},
 {'age': 250, 'amount': 2.85, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2a 0xf0 0x04 0x72 0xfa 0x04    \.*..r..
    decimal
             92    8   42  240    4  114  250    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2012-12-17T13:14:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.5, 'programmed': 6.5}
```
    op hex (4)
    0000   0x01 0x41 0x41 0x00                        .AA.
    decimal
              1   65   65    0
    datetime (2012-12-17T13:14:48)
    0000   0xf0 0x0e 0x4d 0x11 0x0c                   ..M..
    body (0)

#### RECORD 3 CalBGForPH 2012-12-17T19:24:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2012-12-17T19:24:18)
    0000   0xd2 0x18 0x33 0x11 0x0c                   ..3..
    body (0)

#### RECORD 4 BolusWizard 2012-12-17T19:24:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 151,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x97                                  [.
    decimal
             91  151
    datetime (2012-12-17T19:24:22)
    0000   0xd6 0x18 0x13 0x11 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x05 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106    5    0    0
              0    0    0    5  125

#### RECORD 5 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 114, 'amount': 0.1, 'curve': 21}]
```
    op hex (5)
    0000   0x5c 0x05 0x04 0x72 0x15                   \..r.
    decimal
             92    5    4  114   21
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2012-12-17T19:24:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-12-17T19:24:22)
    0000   0xd6 0x18 0x53 0x11 0x0c                   ..S..
    body (0)

#### RECORD 7 ResultTotals 2012-12-17T13:12:17 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x26                   ....&
    decimal
              7    0    0    5   38
    datetime (2012-12-17T13:12:17)
    0000   0xd1 0x0c 0x6d 0xd1 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xd5 0x97 0x31 0x03 0x00 0x00    ....1...
    0008   0x05 0x26 0x03 0x72 0x43 0x01 0xb4 0x21    .&.rC..!
    0010   0x00 0x45 0x01 0xb4 0x21 0x00 0xd4 0x31    .E..!..1
    0018   0x00 0xe0 0x33 0x00 0x00 0x00 0x03 0x00    ..3.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  213  151   49    3    0    0
              5   38    3  114   67    1  180   33
              0   69    1  180   33    0  212   49
              0  224   51    0    0    0    3    0
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 8 PumpSuspend 2012-12-18T13:34:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-18T13:34:07)
    0000   0xc7 0x22 0x0d 0x12 0x0c                   ."...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 9 PumpResume 2012-12-18T14:20:57 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-18T14:20:57)
    0000   0xf9 0x14 0x0e 0x12 0x0c                   .....
    body (0)

#### RECORD 10 CalBGForPH 2012-12-18T15:04:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2012-12-18T15:04:46)
    0000   0xee 0x04 0x2f 0x12 0x0c                   ../..
    body (0)

#### RECORD 11 BolusWizard 2012-12-18T15:05:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 139,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.6,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x8b                                  [.
    decimal
             91  139
    datetime (2012-12-18T15:05:28)
    0000   0xdc 0x05 0x0f 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0x03 0x35 0x00    EP.-j.5.
    0008   0x00 0x00 0x00 0x38 0x7d                   ...8}
    decimal
             69   80   13   45  106    3   53    0
              0    0    0   56  125

#### RECORD 12 Bolus 2012-12-18T15:05:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6, 'programmed': 5.6}
```
    op hex (4)
    0000   0x01 0x38 0x38 0x00                        .88.
    decimal
              1   56   56    0
    datetime (2012-12-18T15:05:28)
    0000   0xdc 0x05 0x4f 0x12 0x0c                   ..O..
    body (0)

#### RECORD 13 BolusWizard 2012-12-18T16:30:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-18T16:30:43)
    0000   0xeb 0x1e 0x10 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0    0    0   13  125

#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 5.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xe0 0x56 0x04                   \..V.
    decimal
             92    5  224   86    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2012-12-18T16:30:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-12-18T16:30:43)
    0000   0xeb 0x1e 0x50 0x12 0x0c                   ..P..
    body (0)

#### RECORD 16 CalBGForPH 2012-12-18T16:54:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2012-12-18T16:54:43)
    0000   0xeb 0x36 0x30 0x12 0x0c                   .60..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 CalBGForPH 2012-12-18T18:31:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2012-12-18T18:31:38)
    0000   0xe6 0x1f 0x32 0x12 0x0c                   ..2..
    body (0)

#### RECORD 18 CalBGForPH 2012-12-18T20:19:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2012-12-18T20:19:12)
    0000   0xcc 0x13 0x34 0x12 0x0c                   ..4..
    body (0)

#### RECORD 19 BolusWizard 2012-12-18T20:19:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 151,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 2,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0x97                                  [.
    decimal
             91  151
    datetime (2012-12-18T20:19:28)
    0000   0xdc 0x13 0x14 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x02 0x50 0x0d 0x2d 0x6a 0x05 0x01 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x05 0x7d                   ....}
    decimal
              2   80   13   45  106    5    1    0
              0    1    0    5  125

#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 235, 'amount': 1.3, 'curve': 4},
 {'age': 59, 'amount': 5.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0xeb 0x04 0xe0 0x3b 0x14    \.4...;.
    decimal
             92    8   52  235    4  224   59   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2012-12-18T20:19:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-12-18T20:19:28)
    0000   0xdc 0x13 0x54 0x12 0x0c                   ..T..
    body (0)

#### RECORD 22 BolusWizard 2012-12-18T20:30:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-18T20:30:41)
    0000   0xe9 0x1e 0x14 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x00 0x20 0x00    *P.-j. .
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106    0   32    0
              0    0    0   32  125

#### RECORD 23 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 0.5, 'curve': 4},
 {'age': 246, 'amount': 1.3, 'curve': 4},
 {'age': 70, 'amount': 5.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x10 0x04 0x34 0xf6 0x04    \....4..
    0008   0xe0 0x46 0x14                             .F.
    decimal
             92   11   20   16    4   52  246    4
            224   70   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2012-12-18T20:30:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-12-18T20:30:41)
    0000   0xe9 0x1e 0x54 0x12 0x0c                   ..T..
    body (0)

#### RECORD 25 CalBGForPH 2012-12-18T21:38:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2012-12-18T21:38:59)
    0000   0xfb 0x26 0x35 0x12 0x0c                   .&5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 BolusWizard 2012-12-18T21:39:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 105,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 11,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.7}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2012-12-18T21:39:26)
    0000   0xda 0x27 0x15 0x12 0x0c                   .'...
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x1b 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0   27    0    8  125
    HOUR BITS: [0, 0, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 75, 'amount': 3.2, 'curve': 4},
 {'age': 85, 'amount': 0.5, 'curve': 4},
 {'age': 59, 'amount': 1.3, 'curve': 20},
 {'age': 139, 'amount': 5.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x80 0x4b 0x04 0x14 0x55 0x04    \..K..U.
    0008   0x34 0x3b 0x14 0xe0 0x8b 0x14              4;....
    decimal
             92   14  128   75    4   20   85    4
             52   59   20  224  139   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2012-12-18T21:39:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'programmed': 0.8}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2012-12-18T21:39:26)
    0000   0xda 0x27 0x55 0x12 0x0c                   .'U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 29 BolusWizard 2012-12-18T22:05:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 5,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-18T22:05:19)
    0000   0xd3 0x05 0x16 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x05 0x50 0x0d 0x2d 0x6a 0x00 0x03 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x03 0x7d                   ....}
    decimal
              5   80   13   45  106    0    3    0
              0    0    0    3  125

#### RECORD 30 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 0.8, 'curve': 4},
 {'age': 101, 'amount': 3.2, 'curve': 4},
 {'age': 111, 'amount': 0.5, 'curve': 4},
 {'age': 85, 'amount': 1.3, 'curve': 20},
 {'age': 165, 'amount': 5.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x1f 0x04 0x80 0x65 0x04    \. ...e.
    0008   0x14 0x6f 0x04 0x34 0x55 0x14 0xe0 0xa5    .o.4U...
    0010   0x14                                       .
    decimal
             92   17   32   31    4  128  101    4
             20  111    4   52   85   20  224  165
             20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-12-18T22:05:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-18T22:05:19)
    0000   0xd3 0x05 0x56 0x12 0x0c                   ..V..
    body (0)

#### RECORD 32 CalBGForPH 2012-12-18T22:11:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 59}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2012-12-18T22:11:12)
    0000   0xcc 0x0b 0x36 0x12 0x0c                   ..6..
    body (0)

#### RECORD 33 ResultTotals 2012-12-18T13:12:18 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x38                   ....8
    decimal
              7    0    0    5   56
    datetime (2012-12-18T13:12:18)
    0000   0xd2 0x0c 0x6d 0xd2 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x71 0x3b 0x97 0x06 0x00 0x00    ..q;....
    0008   0x05 0x38 0x03 0x64 0x41 0x01 0xd4 0x23    .8.dA..#
    0010   0x00 0x92 0x01 0xd4 0x23 0x01 0xb8 0x5e    ....#..^
    0018   0x00 0x1c 0x06 0x00 0x00 0x00 0x06 0x04    ........
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  113   59  151    6    0    0
              5   56    3  100   65    1  212   35
              0  146    1  212   35    1  184   94
              0   28    6    0    0    0    6    4
              0    2    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 34 BolusWizard 2012-12-19T00:34:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-19T00:34:15)
    0000   0xcf 0x22 0x00 0x13 0x0c                   ."...
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [0, 0, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 0.3, 'curve': 4},
 {'age': 180, 'amount': 0.8, 'curve': 4},
 {'age': 250, 'amount': 3.2, 'curve': 4},
 {'age': 4, 'amount': 0.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0c 0x96 0x04 0x20 0xb4 0x04    \.... ..
    0008   0x80 0xfa 0x04 0x14 0x04 0x14              ......
    decimal
             92   14   12  150    4   32  180    4
            128  250    4   20    4   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2012-12-19T00:34:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-12-19T00:34:16)
    0000   0xd0 0x22 0x40 0x13 0x0c                   ."@..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 CalBGForPH 2012-12-19T09:18:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2012-12-19T09:18:55)
    0000   0xf7 0x12 0x29 0x13 0x8c                   ..)..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 38 BolusWizard 2012-12-19T09:18:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 268,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2012-12-19T09:18:58)
    0000   0xfa 0x12 0x09 0x13 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    0    0   31  125

#### RECORD 39 Bolus 2012-12-19T09:18:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-12-19T09:18:58)
    0000   0xfa 0x12 0x49 0x13 0x0c                   ..I..
    body (0)

#### RECORD 40 PumpSuspend 2012-12-19T14:38:04 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-19T14:38:04)
    0000   0xc4 0x26 0x0e 0x13 0x0c                   .&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 PumpResume 2012-12-19T14:58:12 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-19T14:58:12)
    0000   0xcc 0x3a 0x0e 0x13 0x0c                   .:...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 42 BolusWizard 2012-12-19T15:47:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-19T15:47:30)
    0000   0xde 0x2f 0x0f 0x13 0x0c                   ./...
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0x00 0x25 0x00    1P.-j.%.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             49   80   13   45  106    0   37    0
              0    0    0   37  125
    HOUR BITS: [0, 0, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 3.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x89 0x14                   \.|..
    decimal
             92    5  124  137   20
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2012-12-19T15:47:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'programmed': 3.7}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2012-12-19T15:47:30)
    0000   0xde 0x2f 0x4f 0x13 0x0c                   ./O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 CalBGForPH 2012-12-19T17:19:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2012-12-19T17:19:52)
    0000   0xf4 0x13 0x31 0x13 0x0c                   ..1..
    body (0)

#### RECORD 46 CalBGForPH 2012-12-19T19:14:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2012-12-19T19:14:09)
    0000   0xc9 0x0e 0x33 0x13 0x0c                   ..3..
    body (0)

#### RECORD 47 BolusWizard 2012-12-19T19:15:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-19T19:15:51)
    0000   0xf3 0x0f 0x13 0x13 0x0c                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x00 0x18 0x00     P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
             32   80   13   45  106    0   24    0
              0    0    0   24  125

#### RECORD 48 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 3.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x94 0xd3 0x04                   \....
    decimal
             92    5  148  211    4
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2012-12-19T19:15:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2012-12-19T19:15:51)
    0000   0xf3 0x0f 0x53 0x13 0x0c                   ..S..
    body (0)

#### RECORD 50 CalBGForPH 2012-12-19T21:14:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-12-19T21:14:53)
    0000   0xf5 0x0e 0x35 0x13 0x0c                   ..5..
    body (0)

#### RECORD 51 CalBGForPH 2012-12-19T21:15:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-12-19T21:15:43)
    0000   0xeb 0x0f 0x35 0x13 0x0c                   ..5..
    body (0)

#### RECORD 52 PumpSuspend 2012-12-19T23:47:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-19T23:47:01)
    0000   0xc1 0x2f 0x17 0x13 0x0c                   ./...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 53 PumpResume 2012-12-19T23:56:22 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-19T23:56:22)
    0000   0xd6 0x38 0x17 0x13 0x0c                   .8...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 54 CalBGForPH 2012-12-19T23:57:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2012-12-19T23:57:05)
    0000   0xc5 0x39 0x37 0x13 0x8c                   .97..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 55 BolusWizard 2012-12-19T23:57:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 256,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-19T23:57:19)
    0000   0xd3 0x39 0x17 0x13 0x0c                   .9...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    0    0   29  125
    HOUR BITS: [0, 0, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 2.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0x1b 0x14                   \.`..
    decimal
             92    5   96   27   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2012-12-19T23:57:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-12-19T23:57:19)
    0000   0xd3 0x39 0x57 0x13 0x0c                   .9W..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 ResultTotals 2012-12-19T13:12:19 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x86                   .....
    decimal
              7    0    0    5  134
    datetime (2012-12-19T13:12:19)
    0000   0xd3 0x0c 0x6d 0xd3 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xa2 0x6a 0x0c 0x06 0x00 0x00    ...j....
    0008   0x05 0x86 0x03 0x72 0x3e 0x02 0x14 0x26    ...r>..&
    0010   0x00 0x61 0x02 0x14 0x26 0x01 0x24 0x37    .a..&.$7
    0018   0x00 0xf0 0x2d 0x00 0x00 0x00 0x05 0x03    ..-.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  162  106   12    6    0    0
              5  134    3  114   62    2   20   38
              0   97    2   20   38    1   36   55
              0  240   45    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 59 CalBGForPH 2012-12-20T04:04:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2012-12-20T04:04:49)
    0000   0xf1 0x04 0x24 0x14 0x0c                   ..$..
    body (0)

#### RECORD 60 CalBGForPH 2012-12-20T07:52:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2012-12-20T07:52:41)
    0000   0xe9 0x34 0x27 0x14 0x0c                   .4'..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 BolusWizard 2012-12-20T07:52:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 94,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x5e                                  [^
    decimal
             91   94
    datetime (2012-12-20T07:52:50)
    0000   0xf2 0x34 0x07 0x14 0x0c                   .4...
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0xfd 0x1b 0xf0    $P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
             36   80   13   45  106  253   27  240
              0    0    0   24  125
    HOUR BITS: [0, 0, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 222, 'amount': 2.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0xde 0x14                   \.t..
    decimal
             92    5  116  222   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2012-12-20T07:52:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2012-12-20T07:52:50)
    0000   0xf2 0x34 0x47 0x14 0x0c                   .4G..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 CalBGForPH 2012-12-20T14:57:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2012-12-20T14:57:25)
    0000   0xd9 0x39 0x2e 0x14 0x0c                   .9...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 65 BolusWizard 2012-12-20T14:59:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 128,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2012-12-20T14:59:02)
    0000   0xc2 0x3b 0x0e 0x14 0x0c                   .;...
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x00 0x26 0x00    2P.-j.&.
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
             50   80   13   45  106    0   38    0
              0    0    0   38  125
    HOUR BITS: [0, 0, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 169, 'amount': 0.7, 'curve': 20},
 {'age': 179, 'amount': 1.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x1c 0xa9 0x14 0x44 0xb3 0x14    \....D..
    decimal
             92    8   28  169   20   68  179   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2012-12-20T14:59:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'programmed': 3.8}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2012-12-20T14:59:02)
    0000   0xc2 0x3b 0x4e 0x14 0x0c                   .;N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 68 LowReservoir 2012-12-20T15:28:25 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-12-20T15:28:25)
    0000   0xd9 0x1c 0x0f 0x14 0x0c                   .....
    body (0)

#### RECORD 69 ChangeTimeDisplay 2012-12-20T16:40:13 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2012-12-20T16:40:13)
    0000   0xcd 0x28 0x10 0x14 0x0c                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 ChangeTime 2012-12-20T16:40:18 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2012-12-20T16:40:18)
    0000   0xd2 0x28 0x10 0x14 0x0c                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 71 NewTimeSet 2012-12-20T19:40:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2012-12-20T19:40:00)
    0000   0xc0 0x28 0x13 0x14 0x0c                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 72 BolusWizard 2012-12-20T19:48:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-20T19:48:05)
    0000   0xc5 0x30 0x13 0x14 0x0c                   .0...
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [0, 0, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 114, 'amount': 3.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x98 0x72 0x04                   \..r.
    decimal
             92    5  152  114    4
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2012-12-20T19:48:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-12-20T19:48:05)
    0000   0xc5 0x30 0x53 0x14 0x0c                   .0S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 75 ResultTotals 2012-12-20T13:12:20 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x3e                   ....>
    decimal
              7    0    0    4   62
    datetime (2012-12-20T13:12:20)
    0000   0xd4 0x0c 0x6d 0xd4 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x63 0x4c 0x80 0x03 0x00 0x00    ..cL....
    0008   0x04 0x3e 0x03 0x12 0x48 0x01 0x2c 0x1c    .>..H.,.
    0010   0x00 0x67 0x01 0x2c 0x1c 0x01 0x2c 0x64    .g.,..,d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   99   76  128    3    0    0
              4   62    3   18   72    1   44   28
              0  103    1   44   28    1   44  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 76 LowReservoir 2012-12-21T04:18:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-12-21T04:18:45)
    0000   0xed 0x12 0x04 0x15 0x0c                   .....
    body (0)

#### RECORD 77 PumpSuspend 2012-12-21T12:56:50 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-21T12:56:50)
    0000   0xf2 0x38 0x0c 0x15 0x0c                   .8...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 78 PumpResume 2012-12-21T13:14:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-21T13:14:09)
    0000   0xc9 0x0e 0x0d 0x15 0x0c                   .....
    body (0)

#### RECORD 79 CalBGForPH 2012-12-21T14:30:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2012-12-21T14:30:46)
    0000   0xee 0x1e 0x2e 0x15 0x0c                   .....
    body (0)

#### RECORD 80 BolusWizard 2012-12-21T14:30:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 30,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2012-12-21T14:30:58)
    0000   0xfa 0x1e 0x0e 0x15 0x0c                   .....
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106    0   23    0
              0    0    0   23  125

#### RECORD 81 Bolus 2012-12-21T14:30:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-12-21T14:30:58)
    0000   0xfa 0x1e 0x4e 0x15 0x0c                   ..N..
    body (0)

#### RECORD 82 Base unknown head[2], body[0] op[0xdf]

    op hex (2)
    0000   0xdf 0x9a                                  ..
    decimal
            223  154
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-10.data: 83 records`
