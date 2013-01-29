## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 1013, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1a 0xd5                                  ..
##### DEBUG DECIMAL
             26  213
#### RECORD 0 BolusWizard 2012-12-13T18:36:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
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
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2012-12-13T18:36:46)
    0000   0xee 0x24 0x12 0x0d 0x0c                   .$...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x01 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106    1    0    0
              0    0    0    1  125
    HOUR BITS: [0, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 2.0, 'curve': 20},
 {'age': 46, 'amount': 2.1, 'curve': 20},
 {'age': 56, 'amount': 1.7, 'curve': 20},
 {'age': 86, 'amount': 2.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x06 0x14 0x54 0x2e 0x14    \.P..T..
    0008   0x44 0x38 0x14 0x54 0x56 0x14              D8.TV.
    decimal
             92   14   80    6   20   84   46   20
             68   56   20   84   86   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2012-12-13T18:36:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x01 0x01 0x00                        ....
    decimal
              1    1    1    0
    datetime (2012-12-13T18:36:46)
    0000   0xee 0x24 0x52 0x0d 0x0c                   .$R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalBGForPH 2012-12-13T18:41:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2012-12-13T18:41:07)
    0000   0xc7 0x29 0x32 0x0d 0x0c                   .)2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BolusWizard 2012-12-13T18:42:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 1.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2012-12-13T18:42:38)
    0000   0xe6 0x2a 0x12 0x0d 0x0c                   .*...
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x01 0x11 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    1   17    0
              0    1    0   17  125
    HOUR BITS: [0, 0, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.1, 'curve': 4},
 {'age': 12, 'amount': 2.0, 'curve': 20},
 {'age': 52, 'amount': 2.1, 'curve': 20},
 {'age': 62, 'amount': 1.7, 'curve': 20},
 {'age': 92, 'amount': 2.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x04 0x08 0x04 0x50 0x0c 0x14    \....P..
    0008   0x54 0x34 0x14 0x44 0x3e 0x14 0x54 0x5c    T4.D>.T\
    0010   0x14                                       .
    decimal
             92   17    4    8    4   80   12   20
             84   52   20   68   62   20   84   92
             20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2012-12-13T18:42:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2012-12-13T18:42:38)
    0000   0xe6 0x2a 0x52 0x0d 0x0c                   .*R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 CalBGForPH 2012-12-13T22:05:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2012-12-13T22:05:46)
    0000   0xee 0x05 0x36 0x0d 0x0c                   ..6..
    body (0)

#### RECORD 8 BolusWizard 2012-12-13T22:05:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 183,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb7                                  [.
    decimal
             91  183
    datetime (2012-12-13T22:05:53)
    0000   0xf5 0x05 0x16 0x0d 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    2    0   10  125

#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 1.8, 'curve': 4},
 {'age': 215, 'amount': 2.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0xd3 0x04 0x50 0xd7 0x14    \.H..P..
    decimal
             92    8   72  211    4   80  215   20
    datetime (unknown)

    body (0)

#### RECORD 10 PumpSuspend 2012-12-13T22:05:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-13T22:05:55)
    0000   0xf7 0x05 0x16 0x0d 0x0c                   .....
    body (0)

#### RECORD 11 Bolus 2012-12-13T22:05:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x01 0x00                        ....
    decimal
              1   10    1    0
    datetime (2012-12-13T22:05:53)
    0000   0xf5 0x05 0x56 0x0d 0x0c                   ..V..
    body (0)

#### RECORD 12 PumpResume 2012-12-13T22:05:57 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-13T22:05:57)
    0000   0xf9 0x05 0x16 0x0d 0x0c                   .....
    body (0)

#### RECORD 13 CalBGForPH 2012-12-13T22:06:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2012-12-13T22:06:07)
    0000   0xc7 0x06 0x36 0x0d 0x0c                   ..6..
    body (0)

#### RECORD 14 BolusWizard 2012-12-13T22:06:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 183,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb7                                  [.
    decimal
             91  183
    datetime (2012-12-13T22:06:13)
    0000   0xcd 0x06 0x16 0x0d 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    3    0    9  125

#### RECORD 15 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 0.1, 'curve': 4},
 {'age': 212, 'amount': 1.8, 'curve': 4},
 {'age': 216, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x04 0x02 0x04 0x48 0xd4 0x04    \....H..
    0008   0x50 0xd8 0x14                             P..
    decimal
             92   11    4    2    4   72  212    4
             80  216   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2012-12-13T22:06:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-12-13T22:06:13)
    0000   0xcd 0x06 0x56 0x0d 0x0c                   ..V..
    body (0)

#### RECORD 17 ResultTotals 2012-12-13T13:12:13 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x12                   .....
    decimal
              7    0    0    5   18
    datetime (2012-12-13T13:12:13)
    0000   0xcd 0x0c 0x6d 0xcd 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8f 0x54 0xb7 0x05 0x00 0x00    ...T....
    0008   0x05 0x12 0x03 0x76 0x44 0x01 0x9c 0x20    ...vD.. 
    0010   0x00 0x86 0x01 0x9c 0x20 0x01 0x80 0x5d    .... ..]
    0018   0x00 0x1c 0x07 0x00 0x00 0x00 0x07 0x04    ........
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  143   84  183    5    0    0
              5   18    3  118   68    1  156   32
              0  134    1  156   32    1  128   93
              0   28    7    0    0    0    7    4
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 18 PumpSuspend 2012-12-14T14:22:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-14T14:22:15)
    0000   0xcf 0x16 0x0e 0x0e 0x0c                   .....
    body (0)

#### RECORD 19 PumpResume 2012-12-14T14:45:25 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-14T14:45:25)
    0000   0xd9 0x2d 0x0e 0x0e 0x0c                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 BolusWizard 2012-12-14T16:21:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
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
    datetime (2012-12-14T16:21:25)
    0000   0xd9 0x15 0x10 0x0e 0x0c                   .....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125

#### RECORD 21 Bolus 2012-12-14T16:21:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-12-14T16:21:25)
    0000   0xd9 0x15 0x50 0x0e 0x0c                   ..P..
    body (0)

#### RECORD 22 BolusWizard 2012-12-14T16:30:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
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
    datetime (2012-12-14T16:30:28)
    0000   0xdc 0x1e 0x10 0x0e 0x0c                   .....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125

#### RECORD 23 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 1.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x10 0x04                   \.(..
    decimal
             92    5   40   16    4
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2012-12-14T16:30:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-12-14T16:30:28)
    0000   0xdc 0x1e 0x50 0x0e 0x0c                   ..P..
    body (0)

#### RECORD 25 CalBGForPH 2012-12-14T19:17:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2012-12-14T19:17:03)
    0000   0xc3 0x11 0x33 0x0e 0x0c                   ..3..
    body (0)

#### RECORD 26 CalBGForPH 2012-12-14T19:17:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2012-12-14T19:17:55)
    0000   0xf7 0x11 0x33 0x0e 0x0c                   ..3..
    body (0)

#### RECORD 27 BolusWizard 2012-12-14T19:18:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 98,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2012-12-14T19:18:56)
    0000   0xf8 0x12 0x13 0x0e 0x0c                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xfe 0x26 0xf0    2P.-j.&.
    0008   0x00 0x04 0x00 0x24 0x7d                   ...$}
    decimal
             50   80   13   45  106  254   38  240
              0    4    0   36  125

#### RECORD 28 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 174, 'amount': 1.0, 'curve': 4},
 {'age': 184, 'amount': 1.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0xae 0x04 0x28 0xb8 0x04    \.(..(..
    decimal
             92    8   40  174    4   40  184    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2012-12-14T19:18:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-12-14T19:18:56)
    0000   0xf8 0x12 0x53 0x0e 0x0c                   ..S..
    body (0)

#### RECORD 30 CalBGForPH 2012-12-14T19:30:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2012-12-14T19:30:23)
    0000   0xd7 0x1e 0x33 0x0e 0x0c                   ..3..
    body (0)

#### RECORD 31 ResultTotals 2012-12-14T13:12:14 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x56                   ....V
    decimal
              7    0    0    4   86
    datetime (2012-12-14T13:12:14)
    0000   0xce 0x0c 0x6d 0xce 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x66 0x62 0x6d 0x03 0x00 0x00    ..fbm...
    0008   0x04 0x56 0x03 0x76 0x50 0x00 0xe0 0x14    .V.vP...
    0010   0x00 0x4c 0x00 0xe0 0x14 0x00 0xe0 0x64    .L.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  102   98  109    3    0    0
              4   86    3  118   80    0  224   20
              0   76    0  224   20    0  224  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 32 PumpSuspend 2012-12-15T19:07:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-15T19:07:29)
    0000   0xdd 0x07 0x13 0x0f 0x0c                   .....
    body (0)

#### RECORD 33 PumpResume 2012-12-15T19:39:16 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-15T19:39:16)
    0000   0xd0 0x27 0x13 0x0f 0x0c                   .'...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 34 CalBGForPH 2012-12-15T20:10:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2012-12-15T20:10:32)
    0000   0xe0 0x0a 0x34 0x0f 0x0c                   ..4..
    body (0)

#### RECORD 35 BolusWizard 2012-12-15T20:11:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 123,
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
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2012-12-15T20:11:24)
    0000   0xd8 0x0b 0x14 0x0f 0x0c                   .....
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106    0   23    0
              0    0    0   23  125

#### RECORD 36 Bolus 2012-12-15T20:11:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-12-15T20:11:24)
    0000   0xd8 0x0b 0x54 0x0f 0x0c                   ..T..
    body (0)

#### RECORD 37 BolusWizard 2012-12-15T20:59:43 head[2], body[13] op[0x5b]
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
    datetime (2012-12-15T20:59:43)
    0000   0xeb 0x3b 0x14 0x0f 0x0c                   .;...
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106    0    7    0
              0    0    0    7  125
    HOUR BITS: [0, 0, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 2.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x37 0x04                   \.\7.
    decimal
             92    5   92   55    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2012-12-15T20:59:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2012-12-15T20:59:43)
    0000   0xeb 0x3b 0x54 0x0f 0x0c                   .;T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 BolusWizard 2012-12-15T21:37:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 11,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.8,
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
    datetime (2012-12-15T21:37:07)
    0000   0xc7 0x25 0x15 0x0f 0x0c                   .%...
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0    0    0    8  125
    HOUR BITS: [0, 0, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 0.7, 'curve': 4},
 {'age': 93, 'amount': 2.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x1c 0x2b 0x04 0x5c 0x5d 0x04    \..+.\].
    decimal
             92    8   28   43    4   92   93    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2012-12-15T21:37:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2012-12-15T21:37:07)
    0000   0xc7 0x25 0x55 0x0f 0x0c                   .%U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 ResultTotals 2012-12-15T13:12:15 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x08                   .....
    decimal
              7    0    0    4    8
    datetime (2012-12-15T13:12:15)
    0000   0xcf 0x0c 0x6d 0xcf 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x7b 0x7b 0x7b 0x01 0x00 0x00    ..{{{...
    0008   0x04 0x08 0x03 0x70 0x55 0x00 0x98 0x0f    ...pU...
    0010   0x00 0x33 0x00 0x98 0x0f 0x00 0x98 0x64    .3.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  123  123  123    1    0    0
              4    8    3  112   85    0  152   15
              0   51    0  152   15    0  152  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 44 PumpSuspend 2012-12-16T09:47:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-16T09:47:21)
    0000   0xd5 0x2f 0x09 0x10 0x0c                   ./...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 PumpResume 2012-12-16T10:04:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-16T10:04:29)
    0000   0xdd 0x04 0x0a 0x10 0x0c                   .....
    body (0)

#### RECORD 46 CalBGForPH 2012-12-16T10:57:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2012-12-16T10:57:57)
    0000   0xf9 0x39 0x2a 0x10 0x0c                   .9*..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 47 BolusWizard 2012-12-16T10:58:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2012-12-16T10:58:59)
    0000   0xfb 0x3a 0x0a 0x10 0x0c                   .:...
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0x04 0x2b 0x00    9P.-j.+.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             57   80   13   45  106    4   43    0
              0    0    0   47  125
    HOUR BITS: [0, 0, 1]
#### RECORD 48 Bolus 2012-12-16T10:58:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2012-12-16T10:58:59)
    0000   0xfb 0x3a 0x4a 0x10 0x0c                   .:J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 LowReservoir 2012-12-16T13:35:27 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-12-16T13:35:27)
    0000   0xdb 0x23 0x0d 0x10 0x0c                   .#...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 CalBGForPH 2012-12-16T16:44:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 270}
```
    op hex (2)
    0000   0x0a 0x0e                                  ..
    decimal
             10   14
    datetime (2012-12-16T16:44:24)
    0000   0xd8 0x2c 0x30 0x10 0x8c                   .,0..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 51 BolusWizard 2012-12-16T16:44:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 270,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
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
    0000   0x5b 0x0e                                  [.
    decimal
             91   14
    datetime (2012-12-16T16:44:41)
    0000   0xe9 0x2c 0x10 0x10 0x0c                   .,...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
              0   81   13   45  106   32    0    0
              0    0    0   32  125
    HOUR BITS: [0, 0, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 4.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xbc 0x5e 0x14                   \..^.
    decimal
             92    5  188   94   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2012-12-16T16:44:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-12-16T16:44:41)
    0000   0xe9 0x2c 0x50 0x10 0x0c                   .,P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 54 LowReservoir 2012-12-16T20:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-12-16T20:41:03)
    0000   0xc3 0x29 0x14 0x10 0x0c                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 CalBGForPH 2012-12-16T20:56:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2012-12-16T20:56:19)
    0000   0xd3 0x38 0x34 0x10 0x0c                   .84..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 CalBGForPH 2012-12-16T20:56:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2012-12-16T20:56:31)
    0000   0xdf 0x38 0x34 0x10 0x0c                   .84..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 BolusWizard 2012-12-16T20:57:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 103,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2012-12-16T20:57:39)
    0000   0xe7 0x39 0x14 0x10 0x0c                   .9...
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xff 0x26 0xf0    2P.-j.&.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             50   80   13   45  106  255   38  240
              0    0    0   37  125
    HOUR BITS: [0, 0, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 253, 'amount': 3.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x80 0xfd 0x04                   \....
    decimal
             92    5  128  253    4
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2012-12-16T20:57:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2012-12-16T20:57:39)
    0000   0xe7 0x39 0x94 0x10 0x0c                   .9...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 BolusWizard 2012-12-16T21:35:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 11,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.8,
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
    datetime (2012-12-16T21:35:46)
    0000   0xee 0x23 0x15 0x10 0x0c                   .#...
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0    0    0    8  125
    HOUR BITS: [0, 0, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 1, 'amount': 0.05, 'curve': 4},
 {'age': 11, 'amount': 0.3, 'curve': 4},
 {'age': 21, 'amount': 0.3, 'curve': 4},
 {'age': 31, 'amount': 0.25, 'curve': 4},
 {'age': 41, 'amount': 2.25, 'curve': 4},
 {'age': 35, 'amount': 3.2, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x02 0x01 0x04 0x0c 0x0b 0x04    \.......
    0008   0x0c 0x15 0x04 0x0a 0x1f 0x04 0x5a 0x29    ......Z)
    0010   0x04 0x80 0x23 0x14                        ..#.
    decimal
             92   20    2    1    4   12   11    4
             12   21    4   10   31    4   90   41
              4  128   35   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2012-12-16T20:59:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x02                        ....
    decimal
              1   17   17    2
    datetime (2012-12-16T20:59:01)
    0000   0xc1 0x3b 0xb4 0x10 0x0c                   .;...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 Bolus 2012-12-16T21:35:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2012-12-16T21:35:46)
    0000   0xee 0x23 0x55 0x10 0x0c                   .#U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 BolusWizard 2012-12-16T22:29:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
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
    datetime (2012-12-16T22:29:45)
    0000   0xed 0x1d 0x16 0x10 0x0c                   .....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125

#### RECORD 65 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 0.15, 'curve': 4},
 {'age': 45, 'amount': 0.3, 'curve': 4},
 {'age': 55, 'amount': 1.05, 'curve': 4},
 {'age': 65, 'amount': 0.3, 'curve': 4},
 {'age': 75, 'amount': 0.3, 'curve': 4},
 {'age': 85, 'amount': 0.25, 'curve': 4},
 {'age': 95, 'amount': 2.25, 'curve': 4},
 {'age': 89, 'amount': 3.2, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x06 0x23 0x04 0x0c 0x2d 0x04    \..#..-.
    0008   0x2a 0x37 0x04 0x0c 0x41 0x04 0x0c 0x4b    *7..A..K
    0010   0x04 0x0a 0x55 0x04 0x5a 0x5f 0x04 0x80    ..U.Z_..
    0018   0x59 0x14                                  Y.
    decimal
             92   26    6   35    4   12   45    4
             42   55    4   12   65    4   12   75
              4   10   85    4   90   95    4  128
             89   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2012-12-16T22:29:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-12-16T22:29:45)
    0000   0xed 0x1d 0x56 0x10 0x0c                   ..V..
    body (0)

#### RECORD 67 ResultTotals 2012-12-16T13:12:16 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x94                   .....
    decimal
              7    0    0    5  148
    datetime (2012-12-16T13:12:16)
    0000   0xd0 0x0c 0x6d 0xd0 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x9b 0x67 0x0e 0x04 0x00 0x00    ...g....
    0008   0x05 0x94 0x03 0x78 0x3e 0x02 0x1c 0x26    ...x>..&
    0010   0x00 0x83 0x02 0x1c 0x26 0x01 0x7e 0x47    ....&.~G
    0018   0x00 0x9e 0x1d 0x00 0x00 0x00 0x05 0x03    ........
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  155  103   14    4    0    0
              5  148    3  120   62    2   28   38
              0  131    2   28   38    1  126   71
              0  158   29    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 68 Rewind 2012-12-17T09:08:30 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-17T09:08:30)
    0000   0xde 0x08 0x09 0x11 0x0c                   .....
    body (0)

#### RECORD 69 Prime 2012-12-17T09:10:40 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x22                   ...."
    decimal
              3    0    0    0   34
    datetime (2012-12-17T09:10:40)
    0000   0xe8 0x0a 0x29 0x11 0x0c                   ..)..
    body (0)

#### RECORD 70 Prime 2012-12-17T09:11:01 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-17T09:11:01)
    0000   0xc1 0x0b 0x09 0x11 0x0c                   .....
    body (0)

#### RECORD 71 CalBGForPH 2012-12-17T09:12:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 305}
```
    op hex (2)
    0000   0x0a 0x31                                  .1
    decimal
             10   49
    datetime (2012-12-17T09:12:00)
    0000   0xc0 0x0c 0x29 0x11 0x8c                   ..)..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 72 BolusWizard 2012-12-17T09:12:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 40,
 '_byte[7]': 0,
 'bg': 305,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
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
    0000   0x5b 0x31                                  [1
    decimal
             91   49
    datetime (2012-12-17T09:12:05)
    0000   0xc5 0x0c 0x09 0x11 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x28 0x00 0x00    .Q.-j(..
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
              0   81   13   45  106   40    0    0
              0    0    0   40  125

#### RECORD 73 Bolus 2012-12-17T09:12:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2012-12-17T09:12:05)
    0000   0xc5 0x0c 0x49 0x11 0x0c                   ..I..
    body (0)

#### RECORD 74 PumpSuspend 2012-12-17T12:25:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-17T12:25:30)
    0000   0xde 0x19 0x0c 0x11 0x0c                   .....
    body (0)

#### RECORD 75 PumpResume 2012-12-17T12:48:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-17T12:48:58)
    0000   0xfa 0x30 0x0c 0x11 0x0c                   .0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 76 CalBGForPH 2012-12-17T13:14:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2012-12-17T13:14:31)
    0000   0xdf 0x0e 0x2d 0x11 0x0c                   ..-..
    body (0)

`end logs/ReadHistoryData-page-11.data: 77 records`
