## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xeb 0xaa                                  ..
##### DEBUG DECIMAL
            235  170
#### RECORD 0 BolusWizard 2013-05-01T19:02:25 head[2], body[13] op[0x5b]
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
    datetime (2013-05-01T19:02:25)
    0000   0x59 0x42 0x13 0x01 0x0d                   YB...
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125
    HOUR BITS: [0, 1, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.8, 'curve': 4},
 {'age': 98, 'amount': 0.8, 'curve': 4},
 {'age': 208, 'amount': 0.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x30 0x04 0x20 0x62 0x04    \.p0. b.
    0008   0x20 0xd0 0x04                              ..
    decimal
             92   11  112   48    4   32   98    4
             32  208    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-05-01T19:02:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-05-01T19:02:25)
    0000   0x59 0x42 0x53 0x01 0x0d                   YBS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 MResultTotals (2013, 0, 1, 24, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 1, 24, 4, 0))
    0000   0x00 0x04 0xb8 0x41 0x8d                   ...A.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 Model522ResultTotals 2013-05-02T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-02T00:00:00)
    0000   0x41 0x8d                                  A.
    body (41)
    hex
    0000   0x05 0x00 0x92 0x46 0xf7 0x06 0x00 0x00    ...F....
    0008   0x04 0xb8 0x03 0x78 0x4a 0x01 0x40 0x1a    ...xJ.@.
    0010   0x00 0x54 0x01 0x40 0x1a 0x00 0xdc 0x45    .T.@...E
    0018   0x00 0x64 0x1f 0x00 0x00 0x00 0x05 0x04    .d......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  146   70  247    6    0    0
              4  184    3  120   74    1   64   26
              0   84    1   64   26    0  220   69
              0  100   31    0    0    0    5    4
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 5 PumpSuspend 2013-05-02T17:06:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-02T17:06:30)
    0000   0x5e 0x46 0x11 0x02 0x0d                   ^F...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 PumpResume 2013-05-02T17:30:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-02T17:30:07)
    0000   0x47 0x5e 0x11 0x02 0x0d                   G^...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-05-02T18:24:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-05-02T18:24:44)
    0000   0x6c 0x58 0x32 0x02 0x0d                   lX2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 8 BolusWizard 2013-05-02T18:25:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 95,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2013-05-02T18:25:56)
    0000   0x78 0x59 0x12 0x02 0x0d                   xY...
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0xfd 0x28 0xf0    5P.-j.(.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             53   80   13   45  106  253   40  240
              0    0    0   37  125
    HOUR BITS: [0, 1, 0]
#### RECORD 9 Bolus 2013-05-02T18:25:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'dual_component': '??', 'programmed': 3.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2013-05-02T18:25:56)
    0000   0x78 0x59 0x52 0x02 0x0d                   xYR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 10 BolusWizard 2013-05-02T18:56:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
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
    datetime (2013-05-02T18:56:01)
    0000   0x41 0x78 0x12 0x02 0x0d                   Ax...
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    0    0   18  125
    HOUR BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 3.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x94 0x20 0x04                   \.. .
    decimal
             92    5  148   32    4
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-05-02T18:56:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-05-02T18:56:01)
    0000   0x41 0x78 0x52 0x02 0x0d                   AxR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2013-05-02T19:10:37 head[2], body[13] op[0x5b]
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
    datetime (2013-05-02T19:10:37)
    0000   0x65 0x4a 0x13 0x02 0x0d                   eJ...
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0    0    0   21  125
    HOUR BITS: [0, 1, 0]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 1.8, 'curve': 4},
 {'age': 46, 'amount': 3.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0x10 0x04 0x94 0x2e 0x04    \.H.....
    decimal
             92    8   72   16    4  148   46    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-05-02T19:10:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-05-02T19:10:37)
    0000   0x65 0x4a 0x53 0x02 0x0d                   eJS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 16 CalBGForPH 2013-05-02T22:03:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-05-02T22:03:00)
    0000   0x40 0x43 0x36 0x02 0x0d                   @C6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 17 MResultTotals (2013, 0, 2, 6, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 2, 6, 4, 0))
    0000   0x00 0x04 0xa6 0x42 0x8d                   ...B.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 Model522ResultTotals 2013-05-03T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-03T00:00:00)
    0000   0x42 0x8d                                  B.
    body (41)
    hex
    0000   0x05 0x00 0x5b 0x56 0x5f 0x02 0x00 0x00    ..[V_...
    0008   0x04 0xa6 0x03 0x76 0x4a 0x01 0x30 0x1a    ...vJ.0.
    0010   0x00 0x69 0x01 0x30 0x1a 0x01 0x30 0x64    .i.0..0d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   91   86   95    2    0    0
              4  166    3  118   74    1   48   26
              0  105    1   48   26    1   48  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 19 PumpSuspend 2013-05-03T14:16:41 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-03T14:16:41)
    0000   0x69 0x50 0x0e 0x03 0x0d                   iP...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 20 PumpResume 2013-05-03T14:37:42 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-03T14:37:42)
    0000   0x6a 0x65 0x0e 0x03 0x0d                   je...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 21 CalBGForPH 2013-05-03T15:04:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 138}
```
    op hex (2)
    0000   0x0a 0x8a                                  ..
    decimal
             10  138
    datetime (2013-05-03T15:04:53)
    0000   0x75 0x44 0x2f 0x03 0x0d                   uD/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 22 BolusWizard 2013-05-03T15:04:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 138,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8a                                  [.
    decimal
             91  138
    datetime (2013-05-03T15:04:59)
    0000   0x7b 0x44 0x0f 0x03 0x0d                   {D...
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x02 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             12   80   13   45  106    2    9    0
              0    0    0   11  125
    HOUR BITS: [0, 1, 0]
#### RECORD 23 Bolus 2013-05-03T15:04:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-05-03T15:04:59)
    0000   0x7b 0x44 0x4f 0x03 0x0d                   {DO..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 24 CalBGForPH 2013-05-03T15:24:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2013-05-03T15:24:41)
    0000   0x69 0x58 0x2f 0x03 0x0d                   iX/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 25 BolusWizard 2013-05-03T15:25:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 139,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8b                                  [.
    decimal
             91  139
    datetime (2013-05-03T15:25:34)
    0000   0x62 0x59 0x0f 0x03 0x0d                   bY...
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x03 0x0d 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    3   13    0
              0   11    0   13  125
    HOUR BITS: [0, 1, 0]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 1.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0x15 0x04                   \.,..
    decimal
             92    5   44   21    4
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-05-03T15:25:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-05-03T15:25:34)
    0000   0x62 0x59 0x4f 0x03 0x0d                   bYO..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 28 LowReservoir 2013-05-03T18:06:18 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-03T18:06:18)
    0000   0x52 0x46 0x12 0x03 0x0d                   RF...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 29 CalBGForPH 2013-05-03T19:12:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-05-03T19:12:27)
    0000   0x5b 0x4c 0x33 0x03 0x0d                   [L3..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 30 MResultTotals (2013, 0, 3, 24, 3, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 3, 24, 3, 0))
    0000   0x00 0x03 0xd8 0x43 0x8d                   ...C.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 31 Model522ResultTotals 2013-05-04T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-04T00:00:00)
    0000   0x43 0x8d                                  C.
    body (41)
    hex
    0000   0x05 0x00 0x80 0x6c 0x8b 0x03 0x00 0x00    ...l....
    0008   0x03 0xd8 0x03 0x78 0x5a 0x00 0x60 0x0a    ...xZ.`.
    0010   0x00 0x1d 0x00 0x60 0x0a 0x00 0x58 0x5c    ...`..X\
    0018   0x00 0x08 0x08 0x00 0x00 0x00 0x02 0x01    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  128  108  139    3    0    0
              3  216    3  120   90    0   96   10
              0   29    0   96   10    0   88   92
              0    8    8    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 32 CalBGForPH 2013-05-04T00:15:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2013-05-04T00:15:30)
    0000   0x5e 0x4f 0x20 0x04 0x0d                   ^O ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 33 CalBGForPH 2013-05-04T00:16:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2013-05-04T00:16:44)
    0000   0x6c 0x50 0x20 0x04 0x0d                   lP ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 34 BolusWizard 2013-05-04T00:16:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 98,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2013-05-04T00:16:58)
    0000   0x7a 0x50 0x00 0x04 0x0d                   zP...
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0xfe 0x32 0xf0    AP.-j.2.
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
             65   80   13   45  106  254   50  240
              0    0    0   48  125
    HOUR BITS: [0, 1, 0]
#### RECORD 35 LowReservoir 2013-05-04T00:19:44 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-05-04T00:19:44)
    0000   0x6c 0x53 0x00 0x04 0x0d                   lS...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 Bolus 2013-05-04T00:16:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2013-05-04T00:16:58)
    0000   0x7a 0x50 0x40 0x04 0x0d                   zP@..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 CalBGForPH 2013-05-04T08:51:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 267}
```
    op hex (2)
    0000   0x0a 0x0b                                  ..
    decimal
             10   11
    datetime (2013-05-04T08:51:58)
    0000   0x7a 0x73 0x28 0x04 0x8d                   zs(..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 38 BolusWizard 2013-05-04T08:52:00 head[2], body[13] op[0x5b]
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
    datetime (2013-05-04T08:52:00)
    0000   0x40 0x74 0x08 0x04 0x0d                   @t...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    0    0   31  125
    HOUR BITS: [0, 1, 1]
#### RECORD 39 Bolus 2013-05-04T08:52:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-05-04T08:52:00)
    0000   0x40 0x74 0x48 0x04 0x0d                   @tH..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 40 Rewind 2013-05-04T22:45:06 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-05-04T22:45:06)
    0000   0x46 0x6d 0x16 0x04 0x0d                   Fm...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 41 Prime 2013-05-04T22:46:41 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1e                   .....
    decimal
              3    0    0    0   30
    datetime (2013-05-04T22:46:41)
    0000   0x69 0x6e 0x36 0x04 0x0d                   in6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 42 Prime 2013-05-04T22:47:07 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-05-04T22:47:07)
    0000   0x47 0x6f 0x16 0x04 0x0d                   Go...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 43 CalBGForPH 2013-05-04T23:01:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-05-04T23:01:11)
    0000   0x4b 0x41 0x37 0x04 0x0d                   KA7..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 44 BolusWizard 2013-05-04T23:01:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 76,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 3.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4c                                  [L
    decimal
             91   76
    datetime (2013-05-04T23:01:22)
    0000   0x56 0x41 0x17 0x04 0x0d                   VA...
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0xf9 0x22 0xf0    -P.-j.".
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
             45   80   13   45  106  249   34  240
              0    0    0   27  125
    HOUR BITS: [0, 1, 0]
#### RECORD 45 Bolus 2013-05-04T23:01:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-05-04T23:01:22)
    0000   0x56 0x41 0x57 0x04 0x0d                   VAW..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 46 MResultTotals (2013, 0, 4, 10, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 4, 10, 5, 0))
    0000   0x00 0x05 0x2a 0x44 0x8d                   ..*D.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 47 Model522ResultTotals 2013-05-05T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-05T00:00:00)
    0000   0x44 0x8d                                  D.
    body (41)
    hex
    0000   0x05 0x10 0x87 0x4c 0x0b 0x04 0x00 0x00    ...L....
    0008   0x05 0x2a 0x03 0x82 0x44 0x01 0xa8 0x20    .*..D.. 
    0010   0x00 0x6e 0x01 0xa8 0x20 0x01 0x2c 0x47    .n.. .,G
    0018   0x00 0x7c 0x1d 0x00 0x00 0x00 0x03 0x02    .|......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  135   76   11    4    0    0
              5   42    3  130   68    1  168   32
              0  110    1  168   32    1   44   71
              0  124   29    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 48 CalBGForPH 2013-05-05T03:33:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 321}
```
    op hex (2)
    0000   0x0a 0x41                                  .A
    decimal
             10   65
    datetime (2013-05-05T03:33:00)
    0000   0x40 0x61 0x23 0x05 0x8d                   @a#..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 BolusWizard 2013-05-05T03:34:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 43,
 '_byte[7]': 0,
 'bg': 321,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
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
    0000   0x5b 0x41                                  [A
    decimal
             91   65
    datetime (2013-05-05T03:34:15)
    0000   0x4f 0x62 0x03 0x05 0x0d                   Ob...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2b 0x00 0x00    .Q.-j+..
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
              0   81   13   45  106   43    0    0
              0    0    0   43  125
    HOUR BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 2.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0x18 0x14                   \.l..
    decimal
             92    5  108   24   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-05-05T03:34:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-05-05T03:34:15)
    0000   0x4f 0x62 0x43 0x05 0x0d                   ObC..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 52 CalBGForPH 2013-05-05T11:11:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2013-05-05T11:11:36)
    0000   0x64 0x4b 0x2b 0x05 0x0d                   dK+..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 53 BolusWizard 2013-05-05T11:11:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 198,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
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
    0000   0x5b 0xc6                                  [.
    decimal
             91  198
    datetime (2013-05-05T11:11:39)
    0000   0x67 0x4b 0x0b 0x05 0x0d                   gK...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125
    HOUR BITS: [0, 1, 0]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 201, 'amount': 4.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xac 0xc9 0x14                   \....
    decimal
             92    5  172  201   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-05-05T11:11:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-05-05T11:11:39)
    0000   0x67 0x4b 0x4b 0x05 0x0d                   gKK..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 56 CalBGForPH 2013-05-05T22:00:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-05-05T22:00:43)
    0000   0x6b 0x40 0x36 0x05 0x0d                   k@6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 BolusWizard 2013-05-05T22:01:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 121,
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
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-05-05T22:01:00)
    0000   0x40 0x41 0x16 0x05 0x0d                   @A...
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x00 0x26 0x00    2P.-j.&.
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
             50   80   13   45  106    0   38    0
              0    0    0   38  125
    HOUR BITS: [0, 1, 0]
#### RECORD 58 Bolus 2013-05-05T22:01:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-05-05T22:01:00)
    0000   0x40 0x41 0x56 0x05 0x0d                   @AV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 59 MResultTotals (2013, 0, 5, 8, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 5, 8, 5, 0))
    0000   0x00 0x05 0x08 0x45 0x8d                   ...E.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 60 Model522ResultTotals 2013-05-06T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-06T00:00:00)
    0000   0x45 0x8d                                  E.
    body (41)
    hex
    0000   0x05 0x10 0xd5 0x79 0x41 0x03 0x00 0x00    ...yA...
    0008   0x05 0x08 0x03 0x84 0x46 0x01 0x84 0x1e    ....F...
    0010   0x00 0x32 0x01 0x84 0x1e 0x00 0x98 0x27    .2.....'
    0018   0x00 0xec 0x3d 0x00 0x00 0x00 0x03 0x01    ..=.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  213  121   65    3    0    0
              5    8    3  132   70    1  132   30
              0   50    1  132   30    0  152   39
              0  236   61    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 61 PumpSuspend 2013-05-06T00:22:54 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-06T00:22:54)
    0000   0x76 0x56 0x00 0x46 0x0d                   vV.F.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 62 PumpResume 2013-05-06T00:25:11 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-06T00:25:11)
    0000   0x4b 0x59 0x00 0x46 0x0d                   KY.F.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 63 PumpSuspend 2013-05-06T15:15:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-06T15:15:29)
    0000   0x5d 0x4f 0x0f 0x06 0x0d                   ]O...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 64 PumpResume 2013-05-06T15:35:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-06T15:35:33)
    0000   0x61 0x63 0x0f 0x06 0x0d                   ac...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 65 CalBGForPH 2013-05-06T16:45:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-05-06T16:45:06)
    0000   0x46 0x6d 0x30 0x06 0x0d                   Fm0..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 66 BolusWizard 2013-05-06T16:45:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 82,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 4.0,
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
    datetime (2013-05-06T16:45:18)
    0000   0x52 0x6d 0x10 0x06 0x0d                   Rm...
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0xfa 0x28 0xf0    5P.-j.(.
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             53   80   13   45  106  250   40  240
              0    0    0   34  125
    HOUR BITS: [0, 1, 1]
#### RECORD 67 Bolus 2013-05-06T16:45:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-05-06T16:45:18)
    0000   0x52 0x6d 0x50 0x06 0x0d                   RmP..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 68 CalBGForPH 2013-05-06T18:03:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 53}
```
    op hex (2)
    0000   0x0a 0x35                                  .5
    decimal
             10   53
    datetime (2013-05-06T18:03:25)
    0000   0x59 0x43 0x32 0x06 0x0d                   YC2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 69 CalBGForPH 2013-05-06T18:24:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-05-06T18:24:36)
    0000   0x64 0x58 0x32 0x06 0x0d                   dX2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 70 BolusWizard 2013-05-06T18:24:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-05-06T18:24:44)
    0000   0x6c 0x58 0x12 0x06 0x0d                   lX...
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x14 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0   20    0   13  125
    HOUR BITS: [0, 1, 0]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 3.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x88 0x64 0x04                   \..d.
    decimal
             92    5  136  100    4
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-05-06T18:24:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-05-06T18:24:44)
    0000   0x6c 0x58 0x52 0x06 0x0d                   lXR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 73 CalBGForPH 2013-05-06T20:34:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 255}
```
    op hex (2)
    0000   0x0a 0xff                                  ..
    decimal
             10  255
    datetime (2013-05-06T20:34:25)
    0000   0x59 0x62 0x34 0x06 0x0d                   Yb4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 74 BolusWizard 2013-05-06T20:34:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 255,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xff                                  [.
    decimal
             91  255
    datetime (2013-05-06T20:34:40)
    0000   0x68 0x62 0x14 0x06 0x0d                   hb...
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x1c 0x21 0x00    +P.-j.!.
    0008   0x00 0x08 0x00 0x35 0x7d                   ...5}
    decimal
             43   80   13   45  106   28   33    0
              0    8    0   53  125
    HOUR BITS: [0, 1, 1]
#### RECORD 75 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 130, 'amount': 1.3, 'curve': 4},
 {'age': 230, 'amount': 3.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x82 0x04 0x88 0xe6 0x04    \.4.....
    decimal
             92    8   52  130    4  136  230    4
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2013-05-06T20:34:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-05-06T20:34:40)
    0000   0x68 0x62 0x54 0x06 0x0d                   hbT..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 77 CalBGForPH 2013-05-06T22:01:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2013-05-06T22:01:50)
    0000   0x72 0x41 0x36 0x06 0x0d                   rA6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 78 MResultTotals (2013, 0, 6, 6, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 6, 6, 5, 0))
    0000   0x00 0x05 0x06 0x46 0x8d                   ...F.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 79 Model522ResultTotals 2013-05-07T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-07T00:00:00)
    0000   0x46 0x8d                                  F.
    body (41)
    hex
    0000   0x05 0x00 0x94 0x35 0xff 0x05 0x00 0x00    ...5....
    0008   0x05 0x06 0x03 0x76 0x45 0x01 0x90 0x1f    ...vE...
    0010   0x00 0x71 0x01 0x90 0x1f 0x01 0x40 0x50    .q....@P
    0018   0x00 0x50 0x14 0x00 0x00 0x00 0x03 0x02    .P......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  148   53  255    5    0    0
              5    6    3  118   69    1  144   31
              0  113    1  144   31    1   64   80
              0   80   20    0    0    0    3    2
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 80 CalBGForPH 2013-05-07T05:29:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 352}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-05-07T05:29:52)
    0000   0x74 0x5d 0x25 0x07 0x8d                   t]%..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-21.data: 81 records`
