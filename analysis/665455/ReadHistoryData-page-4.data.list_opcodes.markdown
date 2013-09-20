## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa5 0x72                                  .r
##### DEBUG DECIMAL
            165  114
#### RECORD 0 Model522ResultTotals 2013-07-23T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-23T00:00:00)
    0000   0x76 0x8d                                  v.
    body (41)
    hex
    0000   0x05 0x10 0xc2 0x5c 0x6d 0x03 0x00 0x00    ...\m...
    0008   0x04 0xc4 0x03 0x84 0x4a 0x01 0x40 0x1a    ....J.@.
    0010   0x00 0x27 0x01 0x40 0x1a 0x00 0x6c 0x22    .'.@..l"
    0018   0x00 0xd4 0x42 0x00 0x00 0x00 0x02 0x01    ..B.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  194   92  109    3    0    0
              4  196    3  132   74    1   64   26
              0   39    1   64   26    0  108   34
              0  212   66    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2013-07-23T21:10:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-07-23T21:10:46)
    0000   0x6e 0xca 0x35 0x17 0x0d                   n.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2013-07-23T21:11:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 4.9,
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
    datetime (2013-07-23T21:11:06)
    0000   0x46 0xcb 0x15 0x17 0x0d                   F....
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0xfe 0x31 0xf0    @P.-j.1.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             64   80   13   45  106  254   49  240
              0    0    0   47  125
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Bolus 2013-07-23T21:11:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-07-23T21:11:06)
    0000   0x46 0xcb 0x55 0x17 0x0d                   F.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 LowReservoir 2013-07-23T22:50:31 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-23T22:50:31)
    0000   0x5f 0xf2 0x16 0x17 0x0d                   _....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 MResultTotals (2013, 0, 23, 0, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 23, 0, 4, 0))
    0000   0x00 0x04 0x40 0x77 0x8d                   ..@w.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 6 Model522ResultTotals 2013-07-24T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-24T00:00:00)
    0000   0x77 0x8d                                  w.
    body (41)
    hex
    0000   0x05 0x00 0x60 0x60 0x60 0x01 0x00 0x00    ..```...
    0008   0x04 0x40 0x03 0x84 0x53 0x00 0xbc 0x11    .@..S...
    0010   0x00 0x40 0x00 0xbc 0x11 0x00 0xbc 0x64    .@.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   96   96   96    1    0    0
              4   64    3  132   83    0  188   17
              0   64    0  188   17    0  188  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 7 CalBGForPH 2013-07-24T02:05:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 259}
```
    op hex (2)
    0000   0x0a 0x03                                  ..
    decimal
             10    3
    datetime (2013-07-24T02:05:56)
    0000   0x78 0xc5 0x22 0x18 0x8d                   x."..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 BolusWizard 2013-07-24T02:06:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 259,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x03                                  [.
    decimal
             91    3
    datetime (2013-07-24T02:06:12)
    0000   0x4c 0xc6 0x02 0x18 0x0d                   L....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    0    0   29  125
    HOUR BITS: [1, 1, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 0.4, 'curve': 20},
 {'age': 46, 'amount': 4.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x24 0x14 0xac 0x2e 0x14    \..$....
    decimal
             92    8   16   36   20  172   46   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-07-24T02:06:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-07-24T02:06:12)
    0000   0x4c 0xc6 0x42 0x18 0x0d                   L.B..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 LowReservoir 2013-07-24T08:00:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-07-24T08:00:00)
    0000   0x40 0xc0 0x08 0x18 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2013-07-24T22:23:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-24T22:23:48)
    0000   0x70 0xd7 0x36 0x18 0x0d                   p.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 BolusWizard 2013-07-24T22:24:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 102,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 3.6,
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
    datetime (2013-07-24T22:24:14)
    0000   0x4e 0xd8 0x16 0x18 0x0d                   N....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0xff 0x24 0xf0    /P.-j.$.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             47   80   13   45  106  255   36  240
              0    0    0   35  125
    HOUR BITS: [1, 1, 0]
#### RECORD 14 Bolus 2013-07-24T22:24:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-07-24T22:24:14)
    0000   0x4e 0xd8 0x56 0x18 0x0d                   N.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 MResultTotals (2013, 0, 24, 12, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 24, 12, 4, 0))
    0000   0x00 0x04 0x6c 0x78 0x8d                   ..lx.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 Model522ResultTotals 2013-07-25T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-25T00:00:00)
    0000   0x78 0x8d                                  x.
    body (41)
    hex
    0000   0x05 0x10 0xb5 0x66 0x03 0x02 0x00 0x00    ...f....
    0008   0x04 0x6c 0x03 0x84 0x50 0x00 0xe8 0x14    .l..P...
    0010   0x00 0x2f 0x00 0xe8 0x14 0x00 0x8c 0x3c    ./.....<
    0018   0x00 0x5c 0x28 0x00 0x00 0x00 0x02 0x01    .\(.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  181  102    3    2    0    0
              4  108    3  132   80    0  232   20
              0   47    0  232   20    0  140   60
              0   92   40    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 17 Rewind 2013-07-25T10:56:09 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-25T10:56:09)
    0000   0x49 0xf8 0x0a 0x19 0x0d                   I....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 Prime 2013-07-25T10:57:36 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x21                   ....!
    decimal
              3    0    0    0   33
    datetime (2013-07-25T10:57:36)
    0000   0x64 0xf9 0x2a 0x19 0x0d                   d.*..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 Prime 2013-07-25T10:57:57 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-25T10:57:57)
    0000   0x79 0xf9 0x0a 0x19 0x0d                   y....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 CalBGForPH 2013-07-25T11:00:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 317}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2013-07-25T11:00:55)
    0000   0x77 0xc0 0x2b 0x19 0x8d                   w.+..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 BolusWizard 2013-07-25T11:00:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 42,
 '_byte[7]': 0,
 'bg': 317,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3d                                  [=
    decimal
             91   61
    datetime (2013-07-25T11:00:57)
    0000   0x79 0xc0 0x0b 0x19 0x0d                   y....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2a 0x00 0x00    .Q.-j*..
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
              0   81   13   45  106   42    0    0
              0    0    0   42  125
    HOUR BITS: [1, 1, 0]
#### RECORD 22 Bolus 2013-07-25T11:00:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-07-25T11:00:57)
    0000   0x79 0xc0 0x4b 0x19 0x0d                   y.K..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 CalBGForPH 2013-07-25T15:45:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2013-07-25T15:45:49)
    0000   0x71 0xed 0x2f 0x19 0x0d                   q./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 BolusWizard 2013-07-25T15:46:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 84,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2013-07-25T15:46:30)
    0000   0x5e 0xee 0x0f 0x19 0x0d                   ^....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0xfb 0x21 0xf0    ,P.-j.!.
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             44   80   13   45  106  251   33  240
              0    0    0   28  125
    HOUR BITS: [1, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 4.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0x24 0x14                   \..$.
    decimal
             92    5  168   36   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-07-25T15:46:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-07-25T15:46:30)
    0000   0x5e 0xee 0x4f 0x19 0x0d                   ^.O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 27 CalBGForPH 2013-07-25T20:11:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 283}
```
    op hex (2)
    0000   0x0a 0x1b                                  ..
    decimal
             10   27
    datetime (2013-07-25T20:11:34)
    0000   0x62 0xcb 0x34 0x19 0x8d                   b.4..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 28 BolusWizard 2013-07-25T20:11:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 35,
 '_byte[7]': 0,
 'bg': 283,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
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
    0000   0x5b 0x1b                                  [.
    decimal
             91   27
    datetime (2013-07-25T20:11:36)
    0000   0x64 0xcb 0x14 0x19 0x0d                   d....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00 0x00    .Q.-j#..
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
              0   81   13   45  106   35    0    0
              0    0    0   35  125
    HOUR BITS: [1, 1, 0]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 2.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0x0b 0x14                   \.p..
    decimal
             92    5  112   11   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-07-25T20:11:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-07-25T20:11:36)
    0000   0x64 0xcb 0x54 0x19 0x0d                   d.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 31 CalBGForPH 2013-07-25T21:38:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2013-07-25T21:38:51)
    0000   0x73 0xe6 0x35 0x19 0x0d                   s.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 CalBGForPH 2013-07-25T22:58:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-25T22:58:11)
    0000   0x4b 0xfa 0x36 0x19 0x0d                   K.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 BolusWizard 2013-07-25T22:58:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 102,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-07-25T22:58:41)
    0000   0x69 0xfa 0x16 0x19 0x0d                   i....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0xff 0x24 0xf0    /P.-j.$.
    0008   0x00 0x07 0x00 0x23 0x7d                   ...#}
    decimal
             47   80   13   45  106  255   36  240
              0    7    0   35  125
    HOUR BITS: [1, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 174, 'amount': 3.5, 'curve': 4},
 {'age': 178, 'amount': 2.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x8c 0xae 0x04 0x70 0xb2 0x14    \....p..
    decimal
             92    8  140  174    4  112  178   20
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-07-25T22:58:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-07-25T22:58:41)
    0000   0x69 0xfa 0x56 0x19 0x0d                   i.V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 MResultTotals (2013, 0, 25, 18, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 25, 18, 5, 0))
    0000   0x00 0x05 0xb2 0x79 0x8d                   ...y.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 Model522ResultTotals 2013-07-26T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-26T00:00:00)
    0000   0x79 0x8d                                  y.
    body (41)
    hex
    0000   0x05 0x10 0xc0 0x54 0x3d 0x05 0x00 0x00    ...T=...
    0008   0x05 0xb2 0x03 0x82 0x3e 0x02 0x30 0x26    ....>.0&
    0010   0x00 0x5b 0x02 0x30 0x26 0x00 0xfc 0x2d    .[.0&..-
    0018   0x01 0x34 0x37 0x00 0x00 0x00 0x04 0x02    .47.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  192   84   61    5    0    0
              5  178    3  130   62    2   48   38
              0   91    2   48   38    0  252   45
              1   52   55    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 38 CalBGForPH 2013-07-26T07:54:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 241}
```
    op hex (2)
    0000   0x0a 0xf1                                  ..
    decimal
             10  241
    datetime (2013-07-26T07:54:08)
    0000   0x48 0xf6 0x27 0x1a 0x0d                   H.'..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 BolusWizard 2013-07-26T07:54:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 25,
 '_byte[7]': 0,
 'bg': 241,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf1                                  [.
    decimal
             91  241
    datetime (2013-07-26T07:54:10)
    0000   0x4a 0xf6 0x07 0x1a 0x0d                   J....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x19 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
              0   80   13   45  106   25    0    0
              0    0    0   25  125
    HOUR BITS: [1, 1, 1]
#### RECORD 40 Bolus 2013-07-26T07:54:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-07-26T07:54:10)
    0000   0x4a 0xf6 0x47 0x1a 0x0d                   J.G..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 CalBGForPH 2013-07-26T19:32:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 230}
```
    op hex (2)
    0000   0x0a 0xe6                                  ..
    decimal
             10  230
    datetime (2013-07-26T19:32:51)
    0000   0x73 0xe0 0x33 0x1a 0x0d                   s.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 BolusWizard 2013-07-26T19:32:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 230,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
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
    0000   0x5b 0xe6                                  [.
    decimal
             91  230
    datetime (2013-07-26T19:32:59)
    0000   0x7b 0xe0 0x13 0x1a 0x0d                   {....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x17 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
              0   80   13   45  106   23    0    0
              0    0    0   23  125
    HOUR BITS: [1, 1, 1]
#### RECORD 43 Bolus 2013-07-26T19:32:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-07-26T19:32:59)
    0000   0x7b 0xe0 0x53 0x1a 0x0d                   {.S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 CalBGForPH 2013-07-26T21:14:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2013-07-26T21:14:24)
    0000   0x58 0xce 0x35 0x1a 0x0d                   X.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 BolusWizard 2013-07-26T21:15:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 181,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 66,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb5                                  [.
    decimal
             91  181
    datetime (2013-07-26T21:15:16)
    0000   0x50 0xcf 0x15 0x1a 0x0d                   P....
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0x0c 0x32 0x00    BP.-j.2.
    0008   0x00 0x0d 0x00 0x32 0x7d                   ...2}
    decimal
             66   80   13   45  106   12   50    0
              0   13    0   50  125
    HOUR BITS: [1, 1, 0]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 0.8, 'curve': 4},
 {'age': 111, 'amount': 1.5, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x65 0x04 0x3c 0x6f 0x04    \. e.<o.
    decimal
             92    8   32  101    4   60  111    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-07-26T21:15:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-07-26T21:15:16)
    0000   0x50 0xcf 0x55 0x1a 0x0d                   P.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 MResultTotals (2013, 0, 26, 12, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 26, 12, 5, 0))
    0000   0x00 0x05 0x0c 0x7a 0x8d                   ...z.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 Model522ResultTotals 2013-07-27T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-27T00:00:00)
    0000   0x7a 0x8d                                  z.
    body (41)
    hex
    0000   0x05 0x00 0xd9 0xb5 0xf1 0x03 0x00 0x00    ........
    0008   0x05 0x0c 0x03 0x84 0x46 0x01 0x88 0x1e    ....F...
    0010   0x00 0x42 0x01 0x88 0x1e 0x00 0xc8 0x33    .B.....3
    0018   0x00 0xc0 0x31 0x00 0x00 0x00 0x03 0x01    ..1.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  217  181  241    3    0    0
              5   12    3  132   70    1  136   30
              0   66    1  136   30    0  200   51
              0  192   49    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 50 CalBGForPH 2013-07-27T08:48:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 397}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2013-07-27T08:48:46)
    0000   0x6e 0xf0 0x28 0x1b 0x8d                   n.(..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 51 BolusWizard 2013-07-27T08:48:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 60,
 '_byte[7]': 0,
 'bg': 397,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.0,
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
    0000   0x5b 0x8d                                  [.
    decimal
             91  141
    datetime (2013-07-27T08:48:48)
    0000   0x70 0xf0 0x08 0x1b 0x0d                   p....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3c 0x00 0x00    .Q.-j<..
    0008   0x00 0x00 0x00 0x3c 0x7d                   ...<}
    decimal
              0   81   13   45  106   60    0    0
              0    0    0   60  125
    HOUR BITS: [1, 1, 1]
#### RECORD 52 Bolus 2013-07-27T08:48:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3c 0x3c 0x00                        .<<.
    decimal
              1   60   60    0
    datetime (2013-07-27T08:48:48)
    0000   0x70 0xf0 0x48 0x1b 0x0d                   p.H..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 53 CalBGForPH 2013-07-27T15:24:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 83}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-07-27T15:24:36)
    0000   0x64 0xd8 0x2f 0x1b 0x0d                   d./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 54 BolusWizard 2013-07-27T15:24:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 83,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 30,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 2.3,
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
    datetime (2013-07-27T15:24:58)
    0000   0x7a 0xd8 0x0f 0x1b 0x0d                   z....
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0xfb 0x17 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             30   80   13   45  106  251   23  240
              0    0    0   18  125
    HOUR BITS: [1, 1, 0]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 6.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xf0 0x90 0x14                   \....
    decimal
             92    5  240  144   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-07-27T15:24:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-07-27T15:24:58)
    0000   0x7a 0xd8 0x4f 0x1b 0x0d                   z.O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 57 CalBGForPH 2013-07-27T22:32:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-07-27T22:32:57)
    0000   0x79 0xe0 0x36 0x1b 0x0d                   y.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 58 BolusWizard 2013-07-27T22:33:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.4,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 4.6,
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
    datetime (2013-07-27T22:33:12)
    0000   0x4c 0xe1 0x16 0x1b 0x0d                   L....
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x08 0x2e 0x00    =P.-j...
    0008   0x00 0x00 0x00 0x36 0x7d                   ...6}
    decimal
             61   80   13   45  106    8   46    0
              0    0    0   54  125
    HOUR BITS: [1, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 1.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x48 0xad 0x14                   \.H..
    decimal
             92    5   72  173   20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-07-27T22:33:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4, 'dual_component': '??', 'programmed': 5.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x36 0x36 0x00                        .66.
    decimal
              1   54   54    0
    datetime (2013-07-27T22:33:12)
    0000   0x4c 0xe1 0x56 0x1b 0x0d                   L.V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 61 MResultTotals (2013, 0, 27, 20, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 27, 20, 5, 0))
    0000   0x00 0x05 0x94 0x7b 0x8d                   ...{.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 Model522ResultTotals 2013-07-28T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-28T00:00:00)
    0000   0x7b 0x8d                                  {.
    body (41)
    hex
    0000   0x05 0x10 0xd6 0x53 0x8d 0x03 0x00 0x00    ...S....
    0008   0x05 0x94 0x03 0x84 0x3f 0x02 0x10 0x25    ....?..%
    0010   0x00 0x5b 0x02 0x10 0x25 0x01 0x00 0x30    .[..%..0
    0018   0x01 0x10 0x34 0x00 0x00 0x00 0x03 0x01    ..4.....
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  214   83  141    3    0    0
              5  148    3  132   63    2   16   37
              0   91    2   16   37    1    0   48
              1   16   52    0    0    0    3    1
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 63 CalBGForPH 2013-07-28T03:58:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 257}
```
    op hex (2)
    0000   0x0a 0x01                                  ..
    decimal
             10    1
    datetime (2013-07-28T03:58:03)
    0000   0x43 0xfa 0x23 0x1c 0x8d                   C.#..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 64 BolusWizard 2013-07-28T03:58:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 257,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x01                                  [.
    decimal
             91    1
    datetime (2013-07-28T03:58:16)
    0000   0x50 0xfa 0x03 0x1c 0x0d                   P....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    0    0   29  125
    HOUR BITS: [1, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 4.2, 'curve': 20},
 {'age': 78, 'amount': 1.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xa8 0x44 0x14 0x30 0x4e 0x14    \..D.0N.
    decimal
             92    8  168   68   20   48   78   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-07-28T03:58:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-07-28T03:58:16)
    0000   0x50 0xfa 0x43 0x1c 0x0d                   P.C..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 LowReservoir 2013-07-28T11:24:32 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-28T11:24:32)
    0000   0x60 0xd8 0x0b 0x1c 0x0d                   `....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 LowReservoir 2013-07-28T21:31:34 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-07-28T21:31:34)
    0000   0x62 0xdf 0x15 0x1c 0x0d                   b....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 69 CalBGForPH 2013-07-28T22:23:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2013-07-28T22:23:53)
    0000   0x75 0xd7 0x36 0x1c 0x0d                   u.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 70 BolusWizard 2013-07-28T22:24:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 99,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.8,
 'carb_input': 78,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 6.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x63                                  [c
    decimal
             91   99
    datetime (2013-07-28T22:24:05)
    0000   0x45 0xd8 0x16 0x1c 0x0d                   E....
    body (13)
    hex
    0000   0x4e 0x50 0x0d 0x2d 0x6a 0xfe 0x3c 0xf0    NP.-j.<.
    0008   0x00 0x00 0x00 0x3a 0x7d                   ...:}
    decimal
             78   80   13   45  106  254   60  240
              0    0    0   58  125
    HOUR BITS: [1, 1, 0]
#### RECORD 71 Bolus 2013-07-28T22:24:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.8, 'dual_component': '??', 'programmed': 5.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3a 0x3a 0x00                        .::.
    decimal
              1   58   58    0
    datetime (2013-07-28T22:24:05)
    0000   0x45 0xd8 0x56 0x1c 0x0d                   E.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 MResultTotals (2013, 0, 28, 16, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 28, 16, 4, 0))
    0000   0x00 0x04 0xd0 0x7c 0x8d                   ...|.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 73 Model522ResultTotals 2013-07-29T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-29T00:00:00)
    0000   0x7c 0x8d                                  |.
    body (41)
    hex
    0000   0x05 0x10 0xb2 0x63 0x01 0x02 0x00 0x00    ...c....
    0008   0x04 0xd0 0x03 0x84 0x49 0x01 0x4c 0x1b    ....I.L.
    0010   0x00 0x4e 0x01 0x4c 0x1b 0x00 0xe8 0x46    .N.L...F
    0018   0x00 0x64 0x1e 0x00 0x00 0x00 0x02 0x01    .d......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  178   99    1    2    0    0
              4  208    3  132   73    1   76   27
              0   78    1   76   27    0  232   70
              0  100   30    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 74 PumpSuspend 2013-07-29T13:40:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-29T13:40:56)
    0000   0x78 0xe8 0x0d 0x1d 0x0d                   x....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 75 PumpResume 2013-07-29T14:00:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-29T14:00:09)
    0000   0x49 0xc0 0x0e 0x1d 0x0d                   I....
    body (0)
    HOUR BITS: [1, 1, 0]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-4.data: 76 records`
