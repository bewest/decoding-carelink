## START logs/ReadHistoryData-page-30.data
#### RECORD 0 BolusWizard 2013-02-25T19:06:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 8,
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
    datetime (2013-02-25T19:06:09)
    0000   0x09 0x86 0x13 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              8   80   13   45  106    0    6    0
              0    0    0    6  125
    HOUR BITS: [1, 0, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 2.75, 'curve': 4},
 {'age': 32, 'amount': 1.45, 'curve': 4},
 {'age': 132, 'amount': 1.2, 'curve': 4},
 {'age': 46, 'amount': 1.7, 'curve': 20},
 {'age': 96, 'amount': 1.65, 'curve': 20},
 {'age': 106, 'amount': 3.55, 'curve': 20},
 {'age': 136, 'amount': 2.9, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x6e 0x16 0x04 0x3a 0x20 0x04    \.n..: .
    0008   0x30 0x84 0x04 0x44 0x2e 0x14 0x42 0x60    0..D..B`
    0010   0x14 0x8e 0x6a 0x14 0x74 0x88 0x14         ..j.t..
    decimal
             92   23  110   22    4   58   32    4
             48  132    4   68   46   20   66   96
             20  142  106   20  116  136   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-02-25T19:06:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-02-25T19:06:09)
    0000   0x09 0x86 0x53 0x19 0x0d                   ..S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 CalBGForPH 2013-02-25T20:32:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 214}
```
    op hex (2)
    0000   0x0a 0xd6                                  ..
    decimal
             10  214
    datetime (2013-02-25T20:32:29)
    0000   0x1d 0xa0 0x34 0x19 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 4 CalBGForPH 2013-02-25T20:33:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 360}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-02-25T20:33:52)
    0000   0x34 0xa1 0x34 0x19 0x8d                   4.4..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 BolusWizard 2013-02-25T20:34:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 52,
 '_byte[7]': 0,
 'bg': 360,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 1.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-02-25T20:34:20)
    0000   0x14 0xa2 0x14 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x17 0x51 0x0d 0x2d 0x6a 0x34 0x11 0x00    .Q.-j4..
    0008   0x00 0x1a 0x00 0x2b 0x7d                   ...+}
    decimal
             23   81   13   45  106   52   17    0
              0   26    0   43  125
    HOUR BITS: [1, 0, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 90, 'amount': 0.6, 'curve': 4},
 {'age': 110, 'amount': 2.75, 'curve': 4},
 {'age': 120, 'amount': 1.45, 'curve': 4},
 {'age': 220, 'amount': 1.2, 'curve': 4},
 {'age': 134, 'amount': 1.7, 'curve': 20},
 {'age': 184, 'amount': 1.65, 'curve': 20},
 {'age': 194, 'amount': 3.55, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x18 0x5a 0x04 0x6e 0x6e 0x04    \..Z.nn.
    0008   0x3a 0x78 0x04 0x30 0xdc 0x04 0x44 0x86    :x.0..D.
    0010   0x14 0x42 0xb8 0x14 0x8e 0xc2 0x14         .B.....
    decimal
             92   23   24   90    4  110  110    4
             58  120    4   48  220    4   68  134
             20   66  184   20  142  194   20
    datetime (unknown)

    body (0)

#### RECORD 7 LowReservoir 2013-02-25T20:35:11 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-02-25T20:35:11)
    0000   0x0b 0xa3 0x14 0x19 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 8 Bolus 2013-02-25T20:34:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-02-25T20:34:21)
    0000   0x15 0xa2 0x54 0x19 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 BolusWizard 2013-02-25T20:43:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.1,
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
    datetime (2013-02-25T20:43:38)
    0000   0x26 0xab 0x14 0x19 0x0d                   &....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125
    HOUR BITS: [1, 0, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 4.3, 'curve': 4},
 {'age': 99, 'amount': 0.6, 'curve': 4},
 {'age': 119, 'amount': 2.75, 'curve': 4},
 {'age': 129, 'amount': 1.45, 'curve': 4},
 {'age': 229, 'amount': 1.2, 'curve': 4},
 {'age': 143, 'amount': 1.7, 'curve': 20},
 {'age': 193, 'amount': 1.65, 'curve': 20},
 {'age': 203, 'amount': 3.55, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0xac 0x09 0x04 0x18 0x63 0x04    \.....c.
    0008   0x6e 0x77 0x04 0x3a 0x81 0x04 0x30 0xe5    nw.:..0.
    0010   0x04 0x44 0x8f 0x14 0x42 0xc1 0x14 0x8e    .D..B...
    0018   0xcb 0x14                                  ..
    decimal
             92   26  172    9    4   24   99    4
            110  119    4   58  129    4   48  229
              4   68  143   20   66  193   20  142
            203   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-02-25T20:43:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-02-25T20:43:38)
    0000   0x26 0xab 0x54 0x19 0x0d                   &.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 BolusWizard 2013-02-25T20:46:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.5,
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
    datetime (2013-02-25T20:46:42)
    0000   0x2a 0xae 0x14 0x19 0x0d                   *....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x00 0x05 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
              7   80   13   45  106    0    5    0
              0    0    0    5  125
    HOUR BITS: [1, 0, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 0.55, 'curve': 4},
 {'age': 12, 'amount': 4.85, 'curve': 4},
 {'age': 102, 'amount': 0.6, 'curve': 4},
 {'age': 122, 'amount': 2.75, 'curve': 4},
 {'age': 132, 'amount': 1.45, 'curve': 4},
 {'age': 232, 'amount': 1.2, 'curve': 4},
 {'age': 146, 'amount': 1.7, 'curve': 20},
 {'age': 196, 'amount': 1.65, 'curve': 20},
 {'age': 206, 'amount': 3.55, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x16 0x02 0x04 0xc2 0x0c 0x04    \.......
    0008   0x18 0x66 0x04 0x6e 0x7a 0x04 0x3a 0x84    .f.nz.:.
    0010   0x04 0x30 0xe8 0x04 0x44 0x92 0x14 0x42    .0..D..B
    0018   0xc4 0x14 0x8e 0xce 0x14                   .....
    decimal
             92   29   22    2    4  194   12    4
             24  102    4  110  122    4   58  132
              4   48  232    4   68  146   20   66
            196   20  142  206   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-02-25T20:46:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-02-25T20:46:42)
    0000   0x2a 0xae 0x54 0x19 0x0d                   *.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 15 CalBGForPH 2013-02-25T22:10:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2013-02-25T22:10:01)
    0000   0x01 0x8a 0x36 0x19 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 ResultTotals (2013, 0, 25, 13, 13, 57) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xdc                   .....
    decimal
              7    0    0    6  220
    datetime ((2013, 0, 25, 13, 13, 57))
    0000   0x39 0x0d 0x6d 0x39 0x0d                   9.m9.
    body (41)
    hex
    0000   0x05 0x10 0xc1 0x67 0x68 0x0c 0x00 0x00    ...gh...
    0008   0x06 0xdc 0x03 0x78 0x33 0x03 0x64 0x31    ...x3.d1
    0010   0x00 0xd9 0x03 0x64 0x31 0x02 0x88 0x4b    ...d1..K
    0018   0x00 0xdc 0x19 0x00 0x00 0x00 0x0b 0x09    ........
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  193  103  104   12    0    0
              6  220    3  120   51    3  100   49
              0  217    3  100   49    2  136   75
              0  220   25    0    0    0   11    9
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 17 CalBGForPH 2013-02-26T00:34:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-02-26T00:34:48)
    0000   0x30 0xa2 0x20 0x1a 0x0d                   0. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 BolusWizard 2013-02-26T00:34:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-02-26T00:34:55)
    0000   0x37 0xa2 0x00 0x1a 0x0d                   7....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x09 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    9    0    0
              0    3    0    6  125
    HOUR BITS: [1, 0, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 230, 'amount': 1.05, 'curve': 4},
 {'age': 240, 'amount': 4.85, 'curve': 4},
 {'age': 74, 'amount': 0.6, 'curve': 20},
 {'age': 94, 'amount': 2.75, 'curve': 20},
 {'age': 104, 'amount': 1.45, 'curve': 20},
 {'age': 204, 'amount': 1.2, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x2a 0xe6 0x04 0xc2 0xf0 0x04    \.*.....
    0008   0x18 0x4a 0x14 0x6e 0x5e 0x14 0x3a 0x68    .J.n^.:h
    0010   0x14 0x30 0xcc 0x14                        .0..
    decimal
             92   20   42  230    4  194  240    4
             24   74   20  110   94   20   58  104
             20   48  204   20
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-02-26T00:34:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-02-26T00:34:55)
    0000   0x37 0xa2 0x40 0x1a 0x0d                   7.@..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 21 LowReservoir 2013-02-26T01:52:30 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-02-26T01:52:30)
    0000   0x1e 0xb4 0x01 0x1a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 CalBGForPH 2013-02-26T11:50:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 303}
```
    op hex (2)
    0000   0x0a 0x2f                                  ./
    decimal
             10   47
    datetime (2013-02-26T11:50:25)
    0000   0x19 0xb2 0x2b 0x1a 0x8d                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 23 BolusWizard 2013-02-26T11:50:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 39,
 '_byte[7]': 0,
 'bg': 303,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2f                                  [/
    decimal
             91   47
    datetime (2013-02-26T11:50:31)
    0000   0x1f 0xb2 0x0b 0x1a 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x27 0x00 0x00    .Q.-j'..
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
              0   81   13   45  106   39    0    0
              0    0    0   39  125
    HOUR BITS: [1, 0, 1]
#### RECORD 24 Bolus 2013-02-26T11:50:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-02-26T11:50:31)
    0000   0x1f 0xb2 0x4b 0x1a 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 25 PumpSuspend 2013-02-26T15:42:40 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-26T15:42:40)
    0000   0x28 0xaa 0x0f 0x1a 0x0d                   (....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 26 PumpResume 2013-02-26T16:05:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-26T16:05:18)
    0000   0x12 0x85 0x10 0x1a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 27 Rewind 2013-02-26T16:11:20 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-02-26T16:11:20)
    0000   0x14 0x8b 0x10 0x1a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 28 Prime 2013-02-26T16:13:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1e                   .....
    decimal
              3    0    0    0   30
    datetime (2013-02-26T16:13:03)
    0000   0x03 0x8d 0x30 0x1a 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 Prime 2013-02-26T16:13:31 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-02-26T16:13:31)
    0000   0x1f 0x8d 0x10 0x1a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 CalBGForPH 2013-02-26T16:37:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-02-26T16:37:32)
    0000   0x20 0xa5 0x30 0x1a 0x0d                    .0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 31 BolusWizard 2013-02-26T16:37:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 30,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2013-02-26T16:37:46)
    0000   0x2e 0xa5 0x10 0x1a 0x0d                   .....
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0xfe 0x17 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             30   80   13   45  106  254   23  240
              0    0    0   21  125
    HOUR BITS: [1, 0, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 3.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0x25 0x14                   \..%.
    decimal
             92    5  156   37   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-02-26T16:37:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-02-26T16:37:46)
    0000   0x2e 0xa5 0x50 0x1a 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 34 CalBGForPH 2013-02-26T18:47:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 187}
```
    op hex (2)
    0000   0x0a 0xbb                                  ..
    decimal
             10  187
    datetime (2013-02-26T18:47:35)
    0000   0x23 0xaf 0x32 0x1a 0x0d                   #.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 35 BolusWizard 2013-02-26T18:47:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 187,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbb                                  [.
    decimal
             91  187
    datetime (2013-02-26T18:47:37)
    0000   0x25 0xaf 0x12 0x1a 0x0d                   %....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x08 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    8    0    5  125
    HOUR BITS: [1, 0, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 133, 'amount': 2.1, 'curve': 4},
 {'age': 167, 'amount': 3.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x54 0x85 0x04 0x9c 0xa7 0x14    \.T.....
    decimal
             92    8   84  133    4  156  167   20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-02-26T18:47:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-02-26T18:47:37)
    0000   0x25 0xaf 0x52 0x1a 0x0d                   %.R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 38 CalBGForPH 2013-02-26T19:55:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2013-02-26T19:55:55)
    0000   0x37 0xb7 0x33 0x1a 0x0d                   7.3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 39 BolusWizard 2013-02-26T19:57:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 175,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 2.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xaf                                  [.
    decimal
             91  175
    datetime (2013-02-26T19:57:03)
    0000   0x03 0xb9 0x13 0x1a 0x0d                   .....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0x0b 0x16 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x1a 0x7d                   ....}
    decimal
             29   80   13   45  106   11   22    0
              0    7    0   26  125
    HOUR BITS: [1, 0, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 0.5, 'curve': 4},
 {'age': 203, 'amount': 2.1, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x49 0x04 0x54 0xcb 0x04    \..I.T..
    decimal
             92    8   20   73    4   84  203    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2013-02-26T19:57:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-02-26T19:57:03)
    0000   0x03 0xb9 0x53 0x1a 0x0d                   ..S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 42 CalBGForPH 2013-02-26T20:39:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 246}
```
    op hex (2)
    0000   0x0a 0xf6                                  ..
    decimal
             10  246
    datetime (2013-02-26T20:39:06)
    0000   0x06 0xa7 0x34 0x1a 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 43 CalBGForPH 2013-02-26T21:07:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2013-02-26T21:07:36)
    0000   0x24 0x87 0x35 0x1a 0x0d                   $.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 44 BolusWizard 2013-02-26T21:07:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 244,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf4                                  [.
    decimal
             91  244
    datetime (2013-02-26T21:07:45)
    0000   0x2d 0x87 0x15 0x1a 0x0d                   -....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0   22    0    4  125
    HOUR BITS: [1, 0, 0]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 2.6, 'curve': 4},
 {'age': 143, 'amount': 0.5, 'curve': 4},
 {'age': 17, 'amount': 2.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0x49 0x04 0x14 0x8f 0x04    \.hI....
    0008   0x54 0x11 0x14                             T..
    decimal
             92   11  104   73    4   20  143    4
             84   17   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-02-26T21:07:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-02-26T21:07:45)
    0000   0x2d 0x87 0x55 0x1a 0x0d                   -.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 47 ResultTotals (2013, 0, 26, 13, 13, 58) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime ((2013, 0, 26, 13, 13, 58))
    0000   0x3a 0x0d 0x6d 0x3a 0x0d                   :.m:.
    body (41)
    hex
    0000   0x05 0x10 0xcb 0x60 0x2f 0x07 0x00 0x00    ...`/...
    0008   0x05 0x08 0x03 0x74 0x45 0x01 0x94 0x1f    ...tE...
    0010   0x00 0x3b 0x01 0x94 0x1f 0x00 0xac 0x2b    .;.....+
    0018   0x00 0xe8 0x39 0x00 0x00 0x00 0x06 0x01    ..9.....
    0020   0x04 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  203   96   47    7    0    0
              5    8    3  116   69    1  148   31
              0   59    1  148   31    0  172   43
              0  232   57    0    0    0    6    1
              4    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 48 CalBGForPH 2013-02-27T00:31:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-02-27T00:31:23)
    0000   0x17 0x9f 0x20 0x1b 0x0d                   .. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 49 CalBGForPH 2013-02-27T01:20:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-02-27T01:20:38)
    0000   0x26 0x94 0x21 0x1b 0x0d                   &.!..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 BolusWizard 2013-02-27T01:20:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 8,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 0.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2013-02-27T01:20:53)
    0000   0x35 0x94 0x01 0x1b 0x0d                   5....
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0xfe 0x06 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
              8   80   13   45  106  254    6  240
              0    0    0    4  125
    HOUR BITS: [1, 0, 0]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 0.4, 'curve': 20},
 {'age': 70, 'amount': 2.6, 'curve': 20},
 {'age': 140, 'amount': 0.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0x00 0x14 0x68 0x46 0x14    \....hF.
    0008   0x14 0x8c 0x14                             ...
    decimal
             92   11   16    0   20  104   70   20
             20  140   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-02-27T01:20:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-02-27T01:20:53)
    0000   0x35 0x94 0x41 0x1b 0x0d                   5.A..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 CalBGForPH 2013-02-27T09:25:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2013-02-27T09:25:58)
    0000   0x3a 0x99 0x29 0x1b 0x0d                   :.)..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 54 BolusWizard 2013-02-27T09:26:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 154,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
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
    0000   0x5b 0x9a                                  [.
    decimal
             91  154
    datetime (2013-02-27T09:26:01)
    0000   0x01 0x9a 0x09 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    0    0    6  125
    HOUR BITS: [1, 0, 0]
#### RECORD 55 Bolus 2013-02-27T09:26:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-02-27T09:26:01)
    0000   0x01 0x9a 0x49 0x1b 0x0d                   ..I..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 PumpSuspend 2013-02-27T12:28:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-27T12:28:15)
    0000   0x0f 0x9c 0x0c 0x1b 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 57 PumpResume 2013-02-27T12:50:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-27T12:50:35)
    0000   0x23 0xb2 0x0c 0x1b 0x0d                   #....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 58 CalBGForPH 2013-02-27T13:25:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 148}
```
    op hex (2)
    0000   0x0a 0x94                                  ..
    decimal
             10  148
    datetime (2013-02-27T13:25:57)
    0000   0x39 0x99 0x2d 0x1b 0x0d                   9.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 CalBGForPH 2013-02-27T13:31:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-02-27T13:31:20)
    0000   0x14 0x9f 0x2d 0x1b 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 60 BolusWizard 2013-02-27T13:32:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 128,
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
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-02-27T13:32:02)
    0000   0x02 0xa0 0x0d 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x00 0x1b 0x00    $P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    0   27    0
              0    0    0   27  125
    HOUR BITS: [1, 0, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 248, 'amount': 0.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x18 0xf8 0x04                   \....
    decimal
             92    5   24  248    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-02-27T13:32:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-02-27T13:32:02)
    0000   0x02 0xa0 0x4d 0x1b 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 63 BolusWizard 2013-02-27T13:43:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.5,
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
    datetime (2013-02-27T13:43:32)
    0000   0x20 0xab 0x0d 0x1b 0x0d                    ....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x00 0x05 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
              7   80   13   45  106    0    5    0
              0    0    0    5  125
    HOUR BITS: [1, 0, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 2.7, 'curve': 4},
 {'age': 3, 'amount': 0.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x13 0x04 0x18 0x03 0x14    \.l.....
    decimal
             92    8  108   19    4   24    3   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-02-27T13:43:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-02-27T13:43:32)
    0000   0x20 0xab 0x4d 0x1b 0x0d                    .M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 66 CalBGForPH 2013-02-27T16:06:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 332}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-02-27T16:06:14)
    0000   0x0e 0x86 0x30 0x1b 0x8d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 67 BolusWizard 2013-02-27T16:06:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 46,
 '_byte[7]': 0,
 'bg': 332,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4c                                  [L
    decimal
             91   76
    datetime (2013-02-27T16:06:18)
    0000   0x12 0x86 0x10 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2e 0x00 0x00    .Q.-j...
    0008   0x00 0x08 0x00 0x26 0x7d                   ...&}
    decimal
              0   81   13   45  106   46    0    0
              0    8    0   38  125
    HOUR BITS: [1, 0, 0]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 0.5, 'curve': 4},
 {'age': 162, 'amount': 2.7, 'curve': 4},
 {'age': 146, 'amount': 0.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x98 0x04 0x6c 0xa2 0x04    \....l..
    0008   0x18 0x92 0x14                             ...
    decimal
             92   11   20  152    4  108  162    4
             24  146   20
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-02-27T16:06:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-02-27T16:06:18)
    0000   0x12 0x86 0x50 0x1b 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 70 CalBGForPH 2013-02-27T16:45:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-02-27T16:45:19)
    0000   0x13 0xad 0x30 0x1b 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 71 CalBGForPH 2013-02-27T17:38:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2013-02-27T17:38:57)
    0000   0x39 0xa6 0x31 0x1b 0x0d                   9.1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 72 CalBGForPH 2013-02-27T17:39:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2013-02-27T17:39:10)
    0000   0x0a 0xa7 0x31 0x1b 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 73 CalBGForPH 2013-02-27T18:08:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 40}
```
    op hex (2)
    0000   0x0a 0x28                                  .(
    decimal
             10   40
    datetime (2013-02-27T18:08:21)
    0000   0x15 0x88 0x32 0x1b 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 74 CalBGForPH 2013-02-27T20:38:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 162}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2013-02-27T20:38:28)
    0000   0x1c 0xa6 0x34 0x1b 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 75 BolusWizard 2013-02-27T20:38:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 162,
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
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2013-02-27T20:38:33)
    0000   0x21 0xa6 0x14 0x1b 0x0d                   !....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    0    0    8  125
    HOUR BITS: [1, 0, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 3.8, 'curve': 20},
 {'age': 168, 'amount': 0.5, 'curve': 20},
 {'age': 178, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x98 0x12 0x14 0x14 0xa8 0x14    \.......
    0008   0x6c 0xb2 0x14                             l..
    decimal
             92   11  152   18   20   20  168   20
            108  178   20
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2013-02-27T20:38:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-02-27T20:38:33)
    0000   0x21 0xa6 0x54 0x1b 0x0d                   !.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 78 CalBGForPH 2013-02-27T20:44:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 162}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2013-02-27T20:44:01)
    0000   0x01 0xac 0x34 0x1b 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 BolusWizard 2013-02-27T20:44:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 162,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.6,
 'carb_input': 74,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 5.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2013-02-27T20:44:36)
    0000   0x24 0xac 0x14 0x1b 0x0d                   $....
    body (13)
    hex
    0000   0x4a 0x50 0x0d 0x2d 0x6a 0x08 0x38 0x00    JP.-j.8.
    0008   0x00 0x08 0x00 0x38 0x7d                   ...8}
    decimal
             74   80   13   45  106    8   56    0
              0    8    0   56  125
    HOUR BITS: [1, 0, 1]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 0.8, 'curve': 4},
 {'age': 24, 'amount': 3.8, 'curve': 20},
 {'age': 174, 'amount': 0.5, 'curve': 20},
 {'age': 184, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x20 0x0a 0x04 0x98 0x18 0x14    \. .....
    0008   0x14 0xae 0x14 0x6c 0xb8 0x14              ...l..
    decimal
             92   14   32   10    4  152   24   20
             20  174   20  108  184   20
    datetime (unknown)

    body (0)

#### RECORD 81 Base unknown head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x7c                                  P|
    decimal
             80  124
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-30.data: 82 records`
