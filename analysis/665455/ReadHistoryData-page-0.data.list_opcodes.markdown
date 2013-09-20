## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 737, found 285 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xf6 0xf7                                  ..
##### DEBUG DECIMAL
            246  247
#### RECORD 0 Model522ResultTotals 2013-08-17T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-17T00:00:00)
    0000   0x90 0x0d 0x05 0x00 0x78                   ....x
    body (38)
    hex
    0000   0x5f 0x8e 0x03 0x00 0x00 0x04 0x94 0x03    _.......
    0008   0x70 0x4b 0x01 0x24 0x19 0x00 0x60 0x01    pK.$..`.
    0010   0x24 0x19 0x01 0x18 0x60 0x00 0x0c 0x04    $...`...
    0018   0x00 0x00 0x00 0x03 0x02 0x01 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             95  142    3    0    0    4  148    3
            112   75    1   36   25    0   96    1
             36   25    1   24   96    0   12    4
              0    0    0    3    2    1    0    0
             12    0  232    0    0    0
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 1 CalBGForPH 2013-08-17T03:01:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 219}
```
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2013-08-17T03:01:14)
    0000   0x8e 0x01 0x23 0x11 0x0d                   ..#..
    body (0)

#### RECORD 2 BolusWizard 2013-08-17T03:01:23 head[2], body[13] op[0x5b]
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
    datetime (2013-08-17T03:01:23)
    0000   0x97 0x01 0x03 0x11 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125

#### RECORD 3 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 3.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0x47 0x14                   \..G.
    decimal
             92    5  156   71   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-08-17T03:01:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-08-17T03:01:23)
    0000   0x97 0x01 0x43 0x11 0x0d                   ..C..
    body (0)

#### RECORD 5 CalBGForPH 2013-08-17T13:53:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-08-17T13:53:11)
    0000   0x8b 0x35 0x2d 0x11 0x0d                   .5-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 BolusWizard 2013-08-17T13:53:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 1.9,
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
    datetime (2013-08-17T13:53:25)
    0000   0x99 0x35 0x0d 0x11 0x0d                   .5...
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0xf9 0x13 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             25   80   13   45  106  249   19  240
              0    0    0   12  125
    HOUR BITS: [0, 0, 1]
#### RECORD 7 Bolus 2013-08-17T13:53:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-08-17T13:53:25)
    0000   0x99 0x35 0x4d 0x11 0x0d                   .5M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 CalBGForPH 2013-08-17T20:42:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 195}
```
    op hex (2)
    0000   0x0a 0xc3                                  ..
    decimal
             10  195
    datetime (2013-08-17T20:42:16)
    0000   0x90 0x2a 0x34 0x11 0x0d                   .*4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 9 BolusWizard 2013-08-17T20:42:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 195,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
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
    0000   0x5b 0xc3                                  [.
    decimal
             91  195
    datetime (2013-08-17T20:42:19)
    0000   0x93 0x2a 0x14 0x11 0x0d                   .*...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0    0    0   15  125
    HOUR BITS: [0, 0, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 0.3, 'curve': 20},
 {'age': 162, 'amount': 0.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x0c 0x98 0x14 0x24 0xa2 0x14    \....$..
    decimal
             92    8   12  152   20   36  162   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-08-17T20:42:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-08-17T20:42:19)
    0000   0x93 0x2a 0x54 0x11 0x0d                   .*T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 12 CalBGForPH 2013-08-17T22:39:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-08-17T22:39:55)
    0000   0xb7 0x27 0x36 0x11 0x0d                   .'6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 BolusWizard 2013-08-17T22:40:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 118,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x76                                  [v
    decimal
             91  118
    datetime (2013-08-17T22:40:11)
    0000   0x8b 0x28 0x16 0x11 0x0d                   .(...
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    "P.-j...
    0008   0x00 0x07 0x00 0x1a 0x7d                   ....}
    decimal
             34   80   13   45  106    0   26    0
              0    7    0   26  125
    HOUR BITS: [0, 0, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 1.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x7e 0x04                   \.<~.
    decimal
             92    5   60  126    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-08-17T22:40:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-08-17T22:40:11)
    0000   0x8b 0x28 0x56 0x11 0x0d                   .(V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 16 MResultTotals (2013, 0, 17, 28, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 17, 28, 4, 0))
    0000   0x00 0x04 0x9c 0x91 0x0d                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 17 Model522ResultTotals 2013-08-18T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-18T00:00:00)
    0000   0x91 0x0d 0x05 0x00 0x98                   .....
    body (38)
    hex
    0000   0x4b 0xdb 0x04 0x00 0x00 0x04 0x9c 0x03    K.......
    0008   0x84 0x4c 0x01 0x18 0x18 0x00 0x3b 0x01    .L....;.
    0010   0x18 0x18 0x00 0x98 0x36 0x00 0x80 0x2e    ....6...
    0018   0x00 0x00 0x00 0x04 0x02 0x02 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             75  219    4    0    0    4  156    3
            132   76    1   24   24    0   59    1
             24   24    0  152   54    0  128   46
              0    0    0    4    2    2    0    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 18 CalBGForPH 2013-08-18T18:50:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-08-18T18:50:49)
    0000   0xb1 0x32 0x32 0x12 0x0d                   .22..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 19 BolusWizard 2013-08-18T18:51:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 85,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 63,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 4.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2013-08-18T18:51:23)
    0000   0x97 0x33 0x12 0x12 0x0d                   .3...
    body (13)
    hex
    0000   0x3f 0x50 0x0d 0x2d 0x6a 0xfb 0x30 0xf0    ?P.-j.0.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             63   80   13   45  106  251   48  240
              0    0    0   43  125
    HOUR BITS: [0, 0, 1]
#### RECORD 20 Bolus 2013-08-18T18:51:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-08-18T18:51:23)
    0000   0x97 0x33 0x52 0x12 0x0d                   .3R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 21 BolusWizard 2013-08-18T22:26:09 head[2], body[13] op[0x5b]
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
    datetime (2013-08-18T22:26:09)
    0000   0x89 0x1a 0x16 0x12 0x0d                   .....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125

#### RECORD 22 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 212, 'amount': 0.4, 'curve': 4},
 {'age': 222, 'amount': 3.9, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0xd4 0x04 0x9c 0xde 0x04    \.......
    decimal
             92    8   16  212    4  156  222    4
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-08-18T22:26:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-08-18T22:26:09)
    0000   0x89 0x1a 0x56 0x12 0x0d                   ..V..
    body (0)

#### RECORD 24 MResultTotals (2013, 0, 18, 4, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 18, 4, 4, 0))
    0000   0x00 0x04 0x64 0x92 0x0d                   ..d..
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 25 Model522ResultTotals 2013-08-19T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-19T00:00:00)
    0000   0x92 0x0d 0x05 0x00 0x55                   ....U
    body (38)
    hex
    0000   0x55 0x55 0x01 0x00 0x00 0x04 0x64 0x03    UU....d.
    0008   0x84 0x50 0x00 0xe0 0x14 0x00 0x51 0x00    .P....Q.
    0010   0xe0 0x14 0x00 0xe0 0x64 0x00 0x00 0x00    ....d...
    0018   0x00 0x00 0x00 0x02 0x02 0x00 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             85   85    1    0    0    4  100    3
            132   80    0  224   20    0   81    0
            224   20    0  224  100    0    0    0
              0    0    0    2    2    0    0    0
             12    0  232    0    0    0
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 26 CalBGForPH 2013-08-19T07:18:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 223}
```
    op hex (2)
    0000   0x0a 0xdf                                  ..
    decimal
             10  223
    datetime (2013-08-19T07:18:59)
    0000   0xbb 0x12 0x27 0x13 0x0d                   ..'..
    body (0)

#### RECORD 27 BolusWizard 2013-08-19T07:19:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 223,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
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
    0000   0x5b 0xdf                                  [.
    decimal
             91  223
    datetime (2013-08-19T07:19:02)
    0000   0x82 0x13 0x07 0x13 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    0    0   21  125

#### RECORD 28 Bolus 2013-08-19T07:19:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-08-19T07:19:02)
    0000   0x82 0x13 0x47 0x13 0x0d                   ..G..
    body (0)

#### RECORD 29 CalBGForPH 2013-08-19T18:40:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-08-19T18:40:12)
    0000   0x8c 0x28 0x32 0x13 0x0d                   .(2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 CalBGForPH 2013-08-19T18:48:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2013-08-19T18:48:06)
    0000   0x86 0x30 0x32 0x13 0x0d                   .02..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 BolusWizard 2013-08-19T18:48:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 71,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2013-08-19T18:48:29)
    0000   0x9d 0x30 0x12 0x13 0x0d                   .0...
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0xf8 0x28 0xf0    5P.-j.(.
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             53   80   13   45  106  248   40  240
              0    0    0   32  125
    HOUR BITS: [0, 0, 1]
#### RECORD 32 Bolus 2013-08-19T18:48:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-08-19T18:48:29)
    0000   0x9d 0x30 0x52 0x13 0x0d                   .0R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 MResultTotals (2013, 0, 19, 20, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 19, 20, 4, 0))
    0000   0x00 0x04 0x54 0x93 0x0d                   ..T..
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 34 Model522ResultTotals 2013-08-20T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-20T00:00:00)
    0000   0x93 0x0d 0x05 0x00 0x7a                   ....z
    body (38)
    hex
    0000   0x47 0xdf 0x03 0x00 0x00 0x04 0x54 0x03    G.....T.
    0008   0x84 0x51 0x00 0xd0 0x13 0x00 0x35 0x00    .Q....5.
    0010   0xd0 0x13 0x00 0x80 0x3e 0x00 0x50 0x26    ....>.P&
    0018   0x00 0x00 0x00 0x02 0x01 0x01 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             71  223    3    0    0    4   84    3
            132   81    0  208   19    0   53    0
            208   19    0  128   62    0   80   38
              0    0    0    2    1    1    0    0
             12    0  232    0    0    0
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 35 LowReservoir 2013-08-20T02:33:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-20T02:33:45)
    0000   0xad 0x21 0x02 0x14 0x0d                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 CalBGForPH 2013-08-20T09:18:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 266}
```
    op hex (2)
    0000   0x0a 0x0a                                  ..
    decimal
             10   10
    datetime (2013-08-20T09:18:18)
    0000   0x92 0x12 0x29 0x14 0x8d                   ..)..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 BolusWizard 2013-08-20T09:18:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 266,
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
    0000   0x5b 0x0a                                  [.
    decimal
             91   10
    datetime (2013-08-20T09:18:20)
    0000   0x94 0x12 0x09 0x14 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    0    0   31  125

#### RECORD 38 Bolus 2013-08-20T09:18:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-08-20T09:18:20)
    0000   0x94 0x12 0x49 0x14 0x0d                   ..I..
    body (0)

#### RECORD 39 LowReservoir 2013-08-20T10:19:05 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-08-20T10:19:05)
    0000   0x85 0x13 0x0a 0x14 0x0d                   .....
    body (0)

#### RECORD 40 PumpSuspend 2013-08-20T12:45:12 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-08-20T12:45:12)
    0000   0x8c 0x2d 0x0c 0x14 0x0d                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 PumpResume 2013-08-20T13:05:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-08-20T13:05:31)
    0000   0x9f 0x05 0x0d 0x14 0x0d                   .....
    body (0)

#### RECORD 42 Rewind 2013-08-20T13:06:39 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-20T13:06:39)
    0000   0xa7 0x06 0x0d 0x14 0x0d                   .....
    body (0)

#### RECORD 43 Prime 2013-08-20T13:09:37 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1c                   .....
    decimal
              3    0    0    0   28
    datetime (2013-08-20T13:09:37)
    0000   0xa5 0x09 0x2d 0x14 0x0d                   ..-..
    body (0)

#### RECORD 44 Prime 2013-08-20T13:09:59 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-08-20T13:09:59)
    0000   0xbb 0x09 0x0d 0x14 0x0d                   .....
    body (0)

#### RECORD 45 CalBGForPH 2013-08-20T13:59:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-08-20T13:59:15)
    0000   0x8f 0x3b 0x2d 0x14 0x0d                   .;-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 46 BolusWizard 2013-08-20T13:59:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 102,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-08-20T13:59:48)
    0000   0xb0 0x3b 0x0d 0x14 0x0d                   .;...
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0xff 0x2e 0xf0    =P.-j...
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             61   80   13   45  106  255   46  240
              0    0    0   45  125
    HOUR BITS: [0, 0, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 3.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x1d 0x14                   \.|..
    decimal
             92    5  124   29   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-08-20T13:59:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-08-20T13:59:48)
    0000   0xb0 0x3b 0x4d 0x14 0x0d                   .;M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 CalBGForPH 2013-08-20T21:28:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-08-20T21:28:00)
    0000   0x80 0x1c 0x35 0x14 0x0d                   ..5..
    body (0)

#### RECORD 50 BolusWizard 2013-08-20T21:29:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 160,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.0,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2013-08-20T21:29:45)
    0000   0xad 0x1d 0x15 0x14 0x0d                   .....
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0x07 0x35 0x00    EP.-j.5.
    0008   0x00 0x00 0x00 0x3c 0x7d                   ...<}
    decimal
             69   80   13   45  106    7   53    0
              0    0    0   60  125

#### RECORD 51 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 199, 'amount': 4.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0xc7 0x14                   \....
    decimal
             92    5  180  199   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-08-20T21:29:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3c 0x3c 0x00                        .<<.
    decimal
              1   60   60    0
    datetime (2013-08-20T21:29:45)
    0000   0xad 0x1d 0x55 0x14 0x0d                   ..U..
    body (0)

#### RECORD 53 MResultTotals (2013, 0, 20, 18, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 20, 18, 5, 0))
    0000   0x00 0x05 0x92 0x94 0x0d                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 54 Model522ResultTotals 2013-08-21T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-21T00:00:00)
    0000   0x94 0x0d 0x05 0x10 0xb0                   .....
    body (38)
    hex
    0000   0x66 0x0a 0x03 0x00 0x00 0x05 0x92 0x03    f.......
    0008   0x72 0x3e 0x02 0x20 0x26 0x00 0x82 0x02    r>. &...
    0010   0x20 0x26 0x01 0x88 0x48 0x00 0x98 0x1c     &..H...
    0018   0x00 0x00 0x00 0x03 0x01 0x01 0x01 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            102   10    3    0    0    5  146    3
            114   62    2   32   38    0  130    2
             32   38    1  136   72    0  152   28
              0    0    0    3    1    1    1    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 1, 1]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-0.data: 55 records`
