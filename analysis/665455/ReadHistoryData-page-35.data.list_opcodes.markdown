## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x8b 0x8c                                  ..
##### DEBUG DECIMAL
            139  140
#### RECORD 0 CalBGForPH 2013-03-16T18:46:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-16T18:46:24)
    0000   0x18 0xee 0x32 0x10 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 PumpSuspend 2013-03-16T18:48:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-16T18:48:44)
    0000   0x2c 0xf0 0x12 0x10 0x0d                   ,....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 PumpResume 2013-03-16T19:14:27 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-16T19:14:27)
    0000   0x1b 0xce 0x13 0x10 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-16T20:13:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-16T20:13:20)
    0000   0x14 0xcd 0x34 0x10 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-03-16T20:13:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-03-16T20:13:42)
    0000   0x2a 0xcd 0x14 0x10 0x0d                   *....
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0xfc 0x35 0xf0    FP.-j.5.
    0008   0x00 0x00 0x00 0x31 0x7d                   ...1}
    decimal
             70   80   13   45  106  252   53  240
              0    0    0   49  125
    HOUR BITS: [1, 1, 0]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 123, 'amount': 0.55, 'curve': 20},
 {'age': 133, 'amount': 1.95, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x16 0x7b 0x14 0x4e 0x85 0x14    \..{.N..
    decimal
             92    8   22  123   20   78  133   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-03-16T20:13:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2013-03-16T20:13:42)
    0000   0x2a 0xcd 0x54 0x10 0x0d                   *.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2013-03-16T23:51:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2013-03-16T23:51:07)
    0000   0x07 0xf3 0x37 0x10 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BolusWizard 2013-03-16T23:51:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2013-03-16T23:51:28)
    0000   0x1c 0xf3 0x17 0x10 0x0d                   .....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x0a 0x0d 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x12 0x7d                   ....}
    decimal
             18   80   13   45  106   10   13    0
              0    5    0   18  125
    HOUR BITS: [1, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 4.45, 'curve': 4},
 {'age': 227, 'amount': 0.45, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb2 0xd9 0x04 0x12 0xe3 0x04    \.......
    decimal
             92    8  178  217    4   18  227    4
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-03-16T23:51:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-03-16T23:51:29)
    0000   0x1d 0xf3 0x57 0x10 0x0d                   ..W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 MResultTotals (2013, 0, 16, 4, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 16, 4, 4, 0))
    0000   0x00 0x04 0xe4 0x30 0x8d                   ...0.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 Model522ResultTotals 2013-03-17T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-17T00:00:00)
    0000   0x30 0x8d 0x05 0x00 0x77                   0...w
    body (38)
    hex
    0000   0x59 0xae 0x05 0x00 0x00 0x04 0xe4 0x03    Y.......
    0008   0x74 0x47 0x01 0x70 0x1d 0x00 0x79 0x01    tG.p..y.
    0010   0x70 0x1d 0x01 0x5c 0x5f 0x00 0x14 0x05    p..\_...
    0018   0x00 0x00 0x00 0x03 0x02 0x00 0x01 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             89  174    5    0    0    4  228    3
            116   71    1  112   29    0  121    1
            112   29    1   92   95    0   20    5
              0    0    0    3    2    0    1    0
             12    0  232    0    0    0
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 13 PumpSuspend 2013-03-17T09:23:46 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-17T09:23:46)
    0000   0x2e 0xd7 0x09 0x11 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 PumpResume 2013-03-17T09:25:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-17T09:25:31)
    0000   0x1f 0xd9 0x09 0x11 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2013-03-17T09:25:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 334}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2013-03-17T09:25:54)
    0000   0x36 0xd9 0x29 0x11 0x8d                   6.)..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 BolusWizard 2013-03-17T09:26:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 46,
 '_byte[7]': 0,
 'bg': 334,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
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
    0000   0x5b 0x4e                                  [N
    decimal
             91   78
    datetime (2013-03-17T09:26:14)
    0000   0x0e 0xda 0x09 0x11 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2e 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
              0   81   13   45  106   46    0    0
              0    0    0   46  125
    HOUR BITS: [1, 1, 0]
#### RECORD 17 Bolus 2013-03-17T09:26:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2013-03-17T09:26:14)
    0000   0x0e 0xda 0x49 0x11 0x0d                   ..I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 PumpSuspend 2013-03-17T09:31:28 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-17T09:31:28)
    0000   0x1c 0xdf 0x09 0x11 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 PumpResume 2013-03-17T09:47:59 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-17T09:47:59)
    0000   0x3b 0xef 0x09 0x11 0x0d                   ;....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 CalBGForPH 2013-03-17T12:15:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-03-17T12:15:39)
    0000   0x27 0xcf 0x2c 0x11 0x0d                   '.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 21 CalBGForPH 2013-03-17T12:50:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-03-17T12:50:21)
    0000   0x15 0xf2 0x2c 0x11 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 22 BolusWizard 2013-03-17T12:51:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-03-17T12:51:00)
    0000   0x00 0xf3 0x0c 0x11 0x0d                   .....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x00 0x27 0x00    3P.-j.'.
    0008   0x00 0x06 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106    0   39    0
              0    6    0   39  125
    HOUR BITS: [1, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 207, 'amount': 4.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xc4 0xcf 0x04                   \....
    decimal
             92    5  196  207    4
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-03-17T12:51:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-03-17T12:51:00)
    0000   0x00 0xf3 0x4c 0x11 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 CalBGForPH 2013-03-17T17:03:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-17T17:03:51)
    0000   0x33 0xc3 0x31 0x11 0x0d                   3.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 26 CalBGForPH 2013-03-17T19:33:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-17T19:33:48)
    0000   0x30 0xe1 0x33 0x11 0x0d                   0.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 27 BolusWizard 2013-03-17T19:34:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-03-17T19:34:37)
    0000   0x25 0xe2 0x13 0x11 0x0d                   %....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0xfc 0x15 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             28   80   13   45  106  252   21  240
              0    0    0   17  125
    HOUR BITS: [1, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 154, 'amount': 3.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0x9a 0x14                   \....
    decimal
             92    5  156  154   20
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-03-17T19:34:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-03-17T19:34:37)
    0000   0x25 0xe2 0x53 0x11 0x0d                   %.S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 BolusWizard 2013-03-17T20:04:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.1,
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
    datetime (2013-03-17T20:04:50)
    0000   0x32 0xc4 0x14 0x11 0x0d                   2....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0    0    0   21  125
    HOUR BITS: [1, 1, 0]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.7, 'curve': 4},
 {'age': 184, 'amount': 3.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x1e 0x04 0x9c 0xb8 0x14    \.D.....
    decimal
             92    8   68   30    4  156  184   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-03-17T20:04:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-03-17T20:04:50)
    0000   0x32 0xc4 0x54 0x11 0x0d                   2.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 MResultTotals (2013, 0, 17, 14, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 17, 14, 5, 0))
    0000   0x00 0x05 0x6e 0x31 0x8d                   ..n1.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 Model522ResultTotals 2013-03-18T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-18T00:00:00)
    0000   0x31 0x8d 0x05 0x10 0x98                   1....
    body (38)
    hex
    0000   0x58 0x4e 0x05 0x00 0x00 0x05 0x6e 0x03    XN....n.
    0008   0x76 0x40 0x01 0xf8 0x24 0x00 0x6b 0x01    v@..$.k.
    0010   0xf8 0x24 0x01 0x34 0x3d 0x00 0xc4 0x27    .$.4=..'
    0018   0x00 0x00 0x00 0x04 0x03 0x01 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             88   78    5    0    0    5  110    3
            118   64    1  248   36    0  107    1
            248   36    1   52   61    0  196   39
              0    0    0    4    3    1    0    0
             12    0  232    0    0    0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 35 CalBGForPH 2013-03-18T01:03:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-03-18T01:03:12)
    0000   0x0c 0xc3 0x21 0x12 0x0d                   ..!..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 PumpSuspend 2013-03-18T14:10:06 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-18T14:10:06)
    0000   0x06 0xca 0x0e 0x12 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 PumpResume 2013-03-18T14:37:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-18T14:37:55)
    0000   0x37 0xe5 0x0e 0x12 0x0d                   7....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 CalBGForPH 2013-03-18T15:11:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-18T15:11:41)
    0000   0x29 0xcb 0x2f 0x12 0x0d                   )./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 39 BolusWizard 2013-03-18T15:13:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-03-18T15:13:19)
    0000   0x13 0xcd 0x0f 0x12 0x0d                   .....
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0xfc 0x2b 0xf0    8P.-j.+.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             56   80   13   45  106  252   43  240
              0    0    0   39  125
    HOUR BITS: [1, 1, 0]
#### RECORD 40 Bolus 2013-03-18T15:13:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-03-18T15:13:19)
    0000   0x13 0xcd 0x4f 0x12 0x0d                   ..O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 41 CalBGForPH 2013-03-18T17:29:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-03-18T17:29:09)
    0000   0x09 0xdd 0x31 0x12 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 42 BolusWizard 2013-03-18T17:29:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 144,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x90                                  [.
    decimal
             91  144
    datetime (2013-03-18T17:29:26)
    0000   0x1a 0xdd 0x11 0x12 0x0d                   .....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x04 0x13 0x00    .P.-j...
    0008   0x00 0x0e 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    4   19    0
              0   14    0   19  125
    HOUR BITS: [1, 1, 0]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 135, 'amount': 2.85, 'curve': 4},
 {'age': 145, 'amount': 1.05, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x72 0x87 0x04 0x2a 0x91 0x04    \.r..*..
    decimal
             92    8  114  135    4   42  145    4
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-03-18T17:29:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-03-18T17:29:26)
    0000   0x1a 0xdd 0x51 0x12 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 CalBGForPH 2013-03-18T20:15:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 152}
```
    op hex (2)
    0000   0x0a 0x98                                  ..
    decimal
             10  152
    datetime (2013-03-18T20:15:46)
    0000   0x2e 0xcf 0x34 0x12 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 46 BolusWizard 2013-03-18T20:15:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 152,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x98                                  [.
    decimal
             91  152
    datetime (2013-03-18T20:15:55)
    0000   0x37 0xcf 0x14 0x12 0x0d                   7....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x02 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    4    0    2  125
    HOUR BITS: [1, 1, 0]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 171, 'amount': 1.9, 'curve': 4},
 {'age': 45, 'amount': 2.85, 'curve': 20},
 {'age': 55, 'amount': 1.05, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0xab 0x04 0x72 0x2d 0x14    \.L..r-.
    0008   0x2a 0x37 0x14                             *7.
    decimal
             92   11   76  171    4  114   45   20
             42   55   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-03-18T20:15:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-03-18T20:15:55)
    0000   0x37 0xcf 0x54 0x12 0x0d                   7.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 CalBGForPH 2013-03-18T20:59:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-03-18T20:59:40)
    0000   0x28 0xfb 0x34 0x12 0x0d                   (.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 50 BolusWizard 2013-03-18T20:59:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 3.6,
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
    datetime (2013-03-18T20:59:54)
    0000   0x36 0xfb 0x14 0x12 0x0d                   6....
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0x02 0x24 0x00    0P.-j.$.
    0008   0x00 0x04 0x00 0x24 0x7d                   ...$}
    decimal
             48   80   13   45  106    2   36    0
              0    4    0   36  125
    HOUR BITS: [1, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 0.2, 'curve': 4},
 {'age': 215, 'amount': 1.9, 'curve': 4},
 {'age': 89, 'amount': 2.85, 'curve': 20},
 {'age': 99, 'amount': 1.05, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x08 0x2d 0x04 0x4c 0xd7 0x04    \..-.L..
    0008   0x72 0x59 0x14 0x2a 0x63 0x14              rY.*c.
    decimal
             92   14    8   45    4   76  215    4
            114   89   20   42   99   20
    datetime (unknown)

    body (0)

#### RECORD 52 LowReservoir 2013-03-18T21:00:28 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-18T21:00:28)
    0000   0x1c 0xc0 0x15 0x12 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 Bolus 2013-03-18T20:59:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-03-18T20:59:54)
    0000   0x36 0xfb 0x54 0x12 0x0d                   6.T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 54 CalBGForPH 2013-03-18T21:12:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-03-18T21:12:14)
    0000   0x0e 0xcc 0x35 0x12 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 CalBGForPH 2013-03-18T23:13:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-03-18T23:13:35)
    0000   0x23 0xcd 0x37 0x12 0x0d                   #.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 MResultTotals (2013, 0, 18, 18, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 18, 18, 4, 0))
    0000   0x00 0x04 0xf2 0x32 0x8d                   ...2.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 57 Model522ResultTotals 2013-03-19T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-19T00:00:00)
    0000   0x32 0x8d 0x05 0x00 0x7f                   2....
    body (38)
    hex
    0000   0x58 0x98 0x07 0x00 0x00 0x04 0xf2 0x03    X.......
    0008   0x72 0x46 0x01 0x80 0x1e 0x00 0x81 0x01    rF......
    0010   0x80 0x1e 0x01 0x78 0x62 0x00 0x08 0x02    ...xb...
    0018   0x00 0x00 0x00 0x04 0x03 0x01 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             88  152    7    0    0    4  242    3
            114   70    1  128   30    0  129    1
            128   30    1  120   98    0    8    2
              0    0    0    4    3    1    0    0
             12    0  232    0    0    0
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 58 LowReservoir 2013-03-19T05:30:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-03-19T05:30:00)
    0000   0x00 0xde 0x05 0x13 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 PumpSuspend 2013-03-19T11:42:24 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-19T11:42:24)
    0000   0x18 0xea 0x0b 0x13 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 60 PumpResume 2013-03-19T12:11:44 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-19T12:11:44)
    0000   0x2c 0xcb 0x0c 0x13 0x0d                   ,....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 61 CalBGForPH 2013-03-19T12:42:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 280}
```
    op hex (2)
    0000   0x0a 0x18                                  ..
    decimal
             10   24
    datetime (2013-03-19T12:42:06)
    0000   0x06 0xea 0x2c 0x13 0x8d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 BolusWizard 2013-03-19T12:42:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 34,
 '_byte[7]': 0,
 'bg': 280,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x18                                  [.
    decimal
             91   24
    datetime (2013-03-19T12:42:11)
    0000   0x0b 0xea 0x0c 0x13 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x22 0x00 0x00    .Q.-j"..
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
              0   81   13   45  106   34    0    0
              0    0    0   34  125
    HOUR BITS: [1, 1, 1]
#### RECORD 63 Bolus 2013-03-19T12:42:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-03-19T12:42:11)
    0000   0x0b 0xea 0x4c 0x13 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 64 CalBGForPH 2013-03-19T13:07:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 245}
```
    op hex (2)
    0000   0x0a 0xf5                                  ..
    decimal
             10  245
    datetime (2013-03-19T13:07:58)
    0000   0x3a 0xc7 0x2d 0x13 0x0d                   :.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 BolusWizard 2013-03-19T13:08:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 245,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf5                                  [.
    decimal
             91  245
    datetime (2013-03-19T13:08:24)
    0000   0x18 0xc8 0x0d 0x13 0x0d                   .....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x1a 0x1e 0x00    (P.-j...
    0008   0x00 0x20 0x00 0x1e 0x7d                   . ..}
    decimal
             40   80   13   45  106   26   30    0
              0   32    0   30  125
    HOUR BITS: [1, 1, 0]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 0.7, 'curve': 4},
 {'age': 34, 'amount': 2.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x1c 0x18 0x04 0x6c 0x22 0x04    \....l".
    decimal
             92    8   28   24    4  108   34    4
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-03-19T13:08:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-03-19T13:08:24)
    0000   0x18 0xc8 0x4d 0x13 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 BolusWizard 2013-03-19T13:52:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-03-19T13:52:18)
    0000   0x12 0xf4 0x0d 0x13 0x0d                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x00 0x1b 0x00    $P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    0   27    0
              0    0    0   27  125
    HOUR BITS: [1, 1, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 3.0, 'curve': 4},
 {'age': 68, 'amount': 0.7, 'curve': 4},
 {'age': 78, 'amount': 2.7, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x78 0x30 0x04 0x1c 0x44 0x04    \.x0..D.
    0008   0x6c 0x4e 0x04                             lN.
    decimal
             92   11  120   48    4   28   68    4
            108   78    4
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-03-19T13:52:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-03-19T13:52:18)
    0000   0x12 0xf4 0x4d 0x13 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 71 Rewind 2013-03-19T15:44:41 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-03-19T15:44:41)
    0000   0x29 0xec 0x0f 0x13 0x0d                   )....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 Prime 2013-03-19T15:46:43 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x15                   .....
    decimal
              3    0    0    0   21
    datetime (2013-03-19T15:46:43)
    0000   0x2b 0xee 0x2f 0x13 0x0d                   +./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 73 Prime 2013-03-19T15:48:24 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-03-19T15:48:24)
    0000   0x18 0xf0 0x0f 0x13 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 74 CalBGForPH 2013-03-19T16:52:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-03-19T16:52:23)
    0000   0x17 0xf4 0x30 0x13 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 75 CalBGForPH 2013-03-19T20:27:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2013-03-19T20:27:08)
    0000   0x08 0xdb 0x34 0x13 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 BolusWizard 2013-03-19T20:27:10 head[2], body[13] op[0x5b]
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
    datetime (2013-03-19T20:27:10)
    0000   0x0a 0xdb 0x14 0x13 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    0    0    8  125
    HOUR BITS: [1, 1, 0]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 0.15, 'curve': 20},
 {'age': 147, 'amount': 2.55, 'curve': 20},
 {'age': 187, 'amount': 3.0, 'curve': 20},
 {'age': 207, 'amount': 0.7, 'curve': 20},
 {'age': 217, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x06 0x89 0x14 0x66 0x93 0x14    \....f..
    0008   0x78 0xbb 0x14 0x1c 0xcf 0x14 0x6c 0xd9    x.....l.
    0010   0x14                                       .
    decimal
             92   17    6  137   20  102  147   20
            120  187   20   28  207   20  108  217
             20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2013-03-19T20:27:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-03-19T20:27:11)
    0000   0x0b 0xdb 0x54 0x13 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 BolusWizard 2013-03-19T20:43:36 head[2], body[13] op[0x5b]
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
    datetime (2013-03-19T20:43:36)
    0000   0x24 0xeb 0x14 0x13 0x0d                   $....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125
    HOUR BITS: [1, 1, 1]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 0.8, 'curve': 4},
 {'age': 153, 'amount': 0.15, 'curve': 20},
 {'age': 163, 'amount': 2.55, 'curve': 20},
 {'age': 203, 'amount': 3.0, 'curve': 20},
 {'age': 223, 'amount': 0.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x13 0x04 0x06 0x99 0x14    \. .....
    0008   0x66 0xa3 0x14 0x78 0xcb 0x14 0x1c 0xdf    f..x....
    0010   0x14                                       .
    decimal
             92   17   32   19    4    6  153   20
            102  163   20  120  203   20   28  223
             20
    datetime (unknown)

    body (0)

#### RECORD 81 Bolus 2013-03-19T20:43:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-03-19T20:43:36)
    0000   0x24 0xeb 0x54 0x13 0x0d                   $.T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 82 CalBGForPH 2013-03-19T21:16:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2013-03-19T21:16:23)
    0000   0x17 0xd0 0x35 0x13 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 83 BolusWizard 2013-03-19T21:17:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 129,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x81                                  [.
    decimal
             91  129
    datetime (2013-03-19T21:17:34)
    0000   0x22 0xd1 0x15 0x13 0x0d                   "....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x00 0x26 0x00    2P.-j.&.
    0008   0x00 0x0f 0x00 0x26 0x7d                   ...&}
    decimal
             50   80   13   45  106    0   38    0
              0   15    0   38  125
    HOUR BITS: [1, 1, 0]
#### RECORD 84 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 0.3, 'curve': 4},
 {'age': 43, 'amount': 0.6, 'curve': 4},
 {'age': 53, 'amount': 0.8, 'curve': 4},
 {'age': 187, 'amount': 0.15, 'curve': 20},
 {'age': 197, 'amount': 2.55, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x0c 0x21 0x04 0x18 0x2b 0x04    \..!..+.
    0008   0x20 0x35 0x04 0x06 0xbb 0x14 0x66 0xc5     5....f.
    0010   0x14                                       .
    decimal
             92   17   12   33    4   24   43    4
             32   53    4    6  187   20  102  197
             20
    datetime (unknown)

    body (0)

#### RECORD 85 Bolus 2013-03-19T21:17:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-03-19T21:17:34)
    0000   0x22 0xd1 0x55 0x13 0x0d                   ".U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 86 CalBGForPH 2013-03-19T21:54:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-03-19T21:54:25)
    0000   0x19 0xf6 0x35 0x13 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 87 MResultTotals (2013, 0, 19, 20, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 19, 20, 5, 0))
    0000   0x00 0x05 0xb4 0x33 0x8d                   ...3.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-35.data: 88 records`
