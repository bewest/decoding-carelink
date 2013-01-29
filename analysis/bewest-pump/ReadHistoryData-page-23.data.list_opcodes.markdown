## START logs/ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x3b 0x5c                                  ;\
##### DEBUG DECIMAL
             59   92
#### RECORD 0 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 105, 'amount': 0.3, 'curve': 4},
 {'age': 215, 'amount': 0.8, 'curve': 4},
 {'age': 225, 'amount': 0.5, 'curve': 4},
 {'age': 119, 'amount': 1.5, 'curve': 20},
 {'age': 129, 'amount': 2.7, 'curve': 20},
 {'age': 169, 'amount': 1.9, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x0c 0x69 0x04 0x20 0xd7 0x04    \..i. ..
    0008   0x14 0xe1 0x04 0x3c 0x77 0x14 0x6c 0x81    ...<w.l.
    0010   0x14 0x4c 0xa9 0x14                        .L..
    decimal
             92   20   12  105    4   32  215    4
             20  225    4   60  119   20  108  129
             20   76  169   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-10-29T18:59:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2012-10-29T18:59:38)
    0000   0xa6 0xbb 0x52 0x1d 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2012-10-29T19:43:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2012-10-29T19:43:45)
    0000   0xad 0xab 0x33 0x1d 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 3 ResultTotals (2012, 8, 29, 13, 12, 61) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x8e                   .....
    decimal
              7    0    0    5  142
    datetime ((2012, 8, 29, 13, 12, 61))
    0000   0xbd 0x0c 0x6d 0xbd 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x95 0x67 0xcd 0x0a 0x00 0x00    ...g....
    0008   0x05 0x8e 0x03 0x7a 0x3f 0x02 0x14 0x25    ...z?..%
    0010   0x00 0x80 0x02 0x14 0x25 0x01 0x80 0x48    ....%..H
    0018   0x00 0x94 0x1c 0x00 0x00 0x00 0x06 0x03    ........
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  149  103  205   10    0    0
              5  142    3  122   63    2   20   37
              0  128    2   20   37    1  128   72
              0  148   28    0    0    0    6    3
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 4 CalBGForPH 2012-10-30T11:11:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 192}
```
    op hex (2)
    0000   0x0a 0xc0                                  ..
    decimal
             10  192
    datetime (2012-10-30T11:11:34)
    0000   0xa2 0x8b 0x2b 0x1e 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 BolusWizard 2012-10-30T11:11:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 192,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
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
    0000   0x5b 0xc0                                  [.
    decimal
             91  192
    datetime (2012-10-30T11:11:42)
    0000   0xaa 0x8b 0x0b 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125
    HOUR BITS: [1, 0, 0]
#### RECORD 6 Bolus 2012-10-30T11:11:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2012-10-30T11:11:42)
    0000   0xaa 0x8b 0x4b 0x1e 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 CalBGForPH 2012-10-30T12:30:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2012-10-30T12:30:27)
    0000   0x9b 0x9e 0x2c 0x1e 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 BolusWizard 2012-10-30T12:30:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 17,
 '_byte[7]': 0,
 'bg': 202,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xca                                  [.
    decimal
             91  202
    datetime (2012-10-30T12:30:33)
    0000   0xa1 0x9e 0x0c 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x11 0x00 0x00    .P.-j...
    0008   0x00 0x0a 0x00 0x07 0x7d                   ....}
    decimal
              0   80   13   45  106   17    0    0
              0   10    0    7  125
    HOUR BITS: [1, 0, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 1.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0x56 0x04                   \.8V.
    decimal
             92    5   56   86    4
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2012-10-30T12:30:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-10-30T12:30:33)
    0000   0xa1 0x9e 0x4c 0x1e 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 CalBGForPH 2012-10-30T12:34:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2012-10-30T12:34:02)
    0000   0x82 0xa2 0x2c 0x1e 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 CalBGForPH 2012-10-30T12:36:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 203}
```
    op hex (2)
    0000   0x0a 0xcb                                  ..
    decimal
             10  203
    datetime (2012-10-30T12:36:09)
    0000   0x89 0xa4 0x2c 0x1e 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 13 BolusWizard 2012-10-30T12:36:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 17,
 '_byte[7]': 0,
 'bg': 203,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcb                                  [.
    decimal
             91  203
    datetime (2012-10-30T12:36:33)
    0000   0xa1 0xa4 0x0c 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0x11 0x35 0x00    FP.-j.5.
    0008   0x00 0x13 0x00 0x35 0x7d                   ...5}
    decimal
             70   80   13   45  106   17   53    0
              0   19    0   53  125
    HOUR BITS: [1, 0, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 1.0, 'curve': 4},
 {'age': 92, 'amount': 1.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x0c 0x04 0x38 0x5c 0x04    \.(..8\.
    decimal
             92    8   40   12    4   56   92    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2012-10-30T12:36:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2012-10-30T12:36:33)
    0000   0xa1 0xa4 0x4c 0x1e 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 16 CalBGForPH 2012-10-30T13:21:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2012-10-30T13:21:43)
    0000   0xab 0x95 0x2d 0x1e 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 CalBGForPH 2012-10-30T13:40:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2012-10-30T13:40:25)
    0000   0x99 0xa8 0x2d 0x1e 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 CalBGForPH 2012-10-30T15:32:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2012-10-30T15:32:46)
    0000   0xae 0xa0 0x2f 0x1e 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 19 CalBGForPH 2012-10-30T17:33:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-10-30T17:33:44)
    0000   0xac 0xa1 0x31 0x1e 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 20 CalBGForPH 2012-10-30T17:35:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-10-30T17:35:14)
    0000   0x8e 0xa3 0x31 0x1e 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 21 BolusWizard 2012-10-30T17:35:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 70,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 1.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2012-10-30T17:35:53)
    0000   0xb5 0xa3 0x11 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0xf8 0x0c 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
             16   80   13   45  106  248   12  240
              0    0    0    4  125
    HOUR BITS: [1, 0, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 5.3, 'curve': 20},
 {'age': 55, 'amount': 1.0, 'curve': 20},
 {'age': 135, 'amount': 1.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xd4 0x2d 0x14 0x28 0x37 0x14    \..-.(7.
    0008   0x38 0x87 0x14                             8..
    decimal
             92   11  212   45   20   40   55   20
             56  135   20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2012-10-30T17:35:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2012-10-30T17:35:53)
    0000   0xb5 0xa3 0x51 0x1e 0x0c                   ..Q..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 CalBGForPH 2012-10-30T19:38:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2012-10-30T19:38:50)
    0000   0xb2 0xa6 0x33 0x1e 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 25 BolusWizard 2012-10-30T19:39:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2012-10-30T19:39:00)
    0000   0x80 0xa7 0x13 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    2    0    8  125
    HOUR BITS: [1, 0, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 0.4, 'curve': 4},
 {'age': 169, 'amount': 5.3, 'curve': 20},
 {'age': 179, 'amount': 1.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0x7d 0x04 0xd4 0xa9 0x14    \..}....
    0008   0x28 0xb3 0x14                             (..
    decimal
             92   11   16  125    4  212  169   20
             40  179   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2012-10-30T19:39:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2012-10-30T19:39:00)
    0000   0x80 0xa7 0x53 0x1e 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 28 CalBGForPH 2012-10-30T20:34:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2012-10-30T20:34:46)
    0000   0xae 0xa2 0x34 0x1e 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 29 BolusWizard 2012-10-30T20:35:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 175,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xaf                                  [.
    decimal
             91  175
    datetime (2012-10-30T20:35:07)
    0000   0x87 0xa3 0x14 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x0b 0x18 0x00     P.-j...
    0008   0x00 0x08 0x00 0x1b 0x7d                   ....}
    decimal
             32   80   13   45  106   11   24    0
              0    8    0   27  125
    HOUR BITS: [1, 0, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 0.8, 'curve': 4},
 {'age': 181, 'amount': 0.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x3d 0x04 0x10 0xb5 0x04    \. =....
    decimal
             92    8   32   61    4   16  181    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-10-30T20:35:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-10-30T20:35:07)
    0000   0x87 0xa3 0x54 0x1e 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 32 CalBGForPH 2012-10-30T21:47:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2012-10-30T21:47:29)
    0000   0x9d 0xaf 0x35 0x1e 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 BolusWizard 2012-10-30T21:48:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2012-10-30T21:48:22)
    0000   0x96 0xb0 0x15 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x00 0x26 0x00    2P.-j.&.
    0008   0x00 0x19 0x00 0x26 0x7d                   ...&}
    decimal
             50   80   13   45  106    0   38    0
              0   25    0   38  125
    HOUR BITS: [1, 0, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 74, 'amount': 2.9, 'curve': 4},
 {'age': 134, 'amount': 0.8, 'curve': 4},
 {'age': 254, 'amount': 0.4, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x74 0x4a 0x04 0x20 0x86 0x04    \.tJ. ..
    0008   0x10 0xfe 0x04                             ...
    decimal
             92   11  116   74    4   32  134    4
             16  254    4
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2012-10-30T21:48:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2012-10-30T21:48:22)
    0000   0x96 0xb0 0x55 0x1e 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 BolusWizard 2012-10-30T22:10:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 6,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.4,
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
    datetime (2012-10-30T22:10:06)
    0000   0x86 0x8a 0x16 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x06 0x50 0x0d 0x2d 0x6a 0x00 0x04 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
              6   80   13   45  106    0    4    0
              0    0    0    4  125
    HOUR BITS: [1, 0, 0]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 3.8, 'curve': 4},
 {'age': 96, 'amount': 2.9, 'curve': 4},
 {'age': 156, 'amount': 0.8, 'curve': 4},
 {'age': 20, 'amount': 0.4, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x98 0x1a 0x04 0x74 0x60 0x04    \....t`.
    0008   0x20 0x9c 0x04 0x10 0x14 0x14               .....
    decimal
             92   14  152   26    4  116   96    4
             32  156    4   16   20   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2012-10-30T22:10:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2012-10-30T22:10:06)
    0000   0x86 0x8a 0x56 0x1e 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 BolusWizard 2012-10-30T22:25:04 head[2], body[13] op[0x5b]
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
    datetime (2012-10-30T22:25:04)
    0000   0x84 0x99 0x16 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 0, 0]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 0.4, 'curve': 4},
 {'age': 41, 'amount': 3.8, 'curve': 4},
 {'age': 111, 'amount': 2.9, 'curve': 4},
 {'age': 171, 'amount': 0.8, 'curve': 4},
 {'age': 35, 'amount': 0.4, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x10 0x15 0x04 0x98 0x29 0x04    \.....).
    0008   0x74 0x6f 0x04 0x20 0xab 0x04 0x10 0x23    to. ...#
    0010   0x14                                       .
    decimal
             92   17   16   21    4  152   41    4
            116  111    4   32  171    4   16   35
             20
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2012-10-30T22:25:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-10-30T22:25:04)
    0000   0x84 0x99 0x56 0x1e 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 ResultTotals (2012, 8, 30, 13, 12, 62) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x2c                   ....,
    decimal
              7    0    0    6   44
    datetime ((2012, 8, 30, 13, 12, 62))
    0000   0xbe 0x0c 0x6d 0xbe 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x96 0x46 0xcb 0x0c 0x00 0x00    ...F....
    0008   0x06 0x2c 0x03 0x84 0x39 0x02 0xa8 0x2b    .,..9..+
    0010   0x00 0xbb 0x02 0xa8 0x2b 0x02 0x14 0x4e    ....+..N
    0018   0x00 0x94 0x16 0x00 0x00 0x00 0x09 0x05    ........
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  150   70  203   12    0    0
              6   44    3  132   57    2  168   43
              0  187    2  168   43    2   20   78
              0  148   22    0    0    0    9    5
              3    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 43 PumpSuspend 2012-10-31T13:40:36 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-31T13:40:36)
    0000   0xa4 0xa8 0x0d 0x1f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 44 PumpResume 2012-10-31T13:53:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-31T13:53:02)
    0000   0x82 0xb5 0x0d 0x1f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 45 CalBGForPH 2012-10-31T14:16:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2012-10-31T14:16:46)
    0000   0xae 0x90 0x2e 0x1f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 46 BolusWizard 2012-10-31T14:16:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 166,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
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
    0000   0x5b 0xa6                                  [.
    decimal
             91  166
    datetime (2012-10-31T14:16:50)
    0000   0xb2 0x90 0x0e 0x1f 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x09 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106    9    0    0
              0    0    0    9  125
    HOUR BITS: [1, 0, 0]
#### RECORD 47 Bolus 2012-10-31T14:16:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2012-10-31T14:16:50)
    0000   0xb2 0x90 0x4e 0x1f 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 48 CalBGForPH 2012-10-31T15:05:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2012-10-31T15:05:25)
    0000   0x99 0x85 0x2f 0x1f 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 49 BolusWizard 2012-10-31T15:05:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 165,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa5                                  [.
    decimal
             91  165
    datetime (2012-10-31T15:05:38)
    0000   0xa6 0x85 0x0f 0x1f 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x08 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    8    0    0  125
    HOUR BITS: [1, 0, 0]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 0.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x24 0x33 0x04                   \.$3.
    decimal
             92    5   36   51    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2012-10-31T15:05:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x01 0x01 0x00                        ....
    decimal
              1    1    1    0
    datetime (2012-10-31T15:05:38)
    0000   0xa6 0x85 0x4f 0x1f 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 52 BolusWizard 2012-10-31T15:33:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-31T15:33:43)
    0000   0xab 0xa1 0x0f 0x1f 0x0c                   .....
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [1, 0, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 0.1, 'curve': 4},
 {'age': 79, 'amount': 0.9, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x04 0x1d 0x04 0x24 0x4f 0x04    \....$O.
    decimal
             92    8    4   29    4   36   79    4
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2012-10-31T15:33:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-10-31T15:33:43)
    0000   0xab 0xa1 0x4f 0x1f 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 55 CalBGForPH 2012-10-31T16:07:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2012-10-31T16:07:32)
    0000   0xa0 0x87 0x30 0x1f 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 LowReservoir 2012-10-31T16:31:34 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-10-31T16:31:34)
    0000   0xa2 0x9f 0x10 0x1f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 57 CalBGForPH 2012-10-31T19:23:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2012-10-31T19:23:50)
    0000   0xb2 0x97 0x33 0x1f 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 58 BolusWizard 2012-10-31T19:24:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 71,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 63,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 4.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2012-10-31T19:24:58)
    0000   0xba 0x98 0x13 0x1f 0x0c                   .....
    body (13)
    hex
    0000   0x3f 0x50 0x0d 0x2d 0x6a 0xf8 0x30 0xf0    ?P.-j.0.
    0008   0x00 0x02 0x00 0x28 0x7d                   ...(}
    decimal
             63   80   13   45  106  248   48  240
              0    2    0   40  125
    HOUR BITS: [1, 0, 0]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 230, 'amount': 1.85, 'curve': 4},
 {'age': 240, 'amount': 0.45, 'curve': 4},
 {'age': 4, 'amount': 0.1, 'curve': 20},
 {'age': 54, 'amount': 0.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x4a 0xe6 0x04 0x12 0xf0 0x04    \.J.....
    0008   0x04 0x04 0x14 0x24 0x36 0x14              ...$6.
    decimal
             92   14   74  230    4   18  240    4
              4    4   20   36   54   20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2012-10-31T19:24:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2012-10-31T19:24:58)
    0000   0xba 0x98 0x53 0x1f 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 61 CalBGForPH 2012-10-31T22:17:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 60}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2012-10-31T22:17:35)
    0000   0xa3 0x91 0x36 0x1f 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 LowReservoir 2012-10-31T22:50:31 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-10-31T22:50:31)
    0000   0x9f 0xb2 0x16 0x1f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 63 ResultTotals (2012, 8, 31, 13, 12, 63) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9e                   .....
    decimal
              7    0    0    4  158
    datetime ((2012, 8, 31, 13, 12, 63))
    0000   0xbf 0x0c 0x6d 0xbf 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x76 0x3c 0xa6 0x05 0x00 0x00    ..v<....
    0008   0x04 0x9e 0x03 0x7a 0x4b 0x01 0x24 0x19    ...zK.$.
    0010   0x00 0x5d 0x01 0x24 0x19 0x00 0xfc 0x56    .].$...V
    0018   0x00 0x28 0x0e 0x00 0x00 0x00 0x04 0x02    .(......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  118   60  166    5    0    0
              4  158    3  122   75    1   36   25
              0   93    1   36   25    0  252   86
              0   40   14    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 64 PumpSuspend 2012-11-01T10:43:24 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-01T10:43:24)
    0000   0x98 0xeb 0x0a 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 65 PumpResume 2012-11-01T10:55:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-01T10:55:30)
    0000   0x9e 0xf7 0x0a 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 Rewind 2012-11-01T11:52:01 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-11-01T11:52:01)
    0000   0x81 0xf4 0x0b 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 Prime 2012-11-01T11:53:49 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x19                   .....
    decimal
              3    0    0    0   25
    datetime (2012-11-01T11:53:49)
    0000   0xb1 0xf5 0x2b 0x01 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 Prime 2012-11-01T11:54:11 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-11-01T11:54:11)
    0000   0x8b 0xf6 0x0b 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 CalBGForPH 2012-11-01T11:56:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2012-11-01T11:56:51)
    0000   0xb3 0xf8 0x2b 0x01 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 70 BolusWizard 2012-11-01T11:57:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
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
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2012-11-01T11:57:10)
    0000   0x8a 0xf9 0x0b 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x01 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106    1    0    0
              0    0    0    1  125
    HOUR BITS: [1, 1, 1]
#### RECORD 71 Bolus 2012-11-01T11:57:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2012-11-01T11:57:11)
    0000   0x8b 0xf9 0x4b 0x01 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 CalBGForPH 2012-11-01T12:03:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2012-11-01T12:03:40)
    0000   0xa8 0xc3 0x2c 0x01 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 73 BolusWizard 2012-11-01T12:03:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 4.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2012-11-01T12:03:56)
    0000   0xb8 0xc3 0x0c 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0x01 0x31 0x00    @P.-j.1.
    0008   0x00 0x07 0x00 0x31 0x7d                   ...1}
    decimal
             64   80   13   45  106    1   49    0
              0    7    0   49  125
    HOUR BITS: [1, 1, 0]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 0.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x1c 0x09 0x04                   \....
    decimal
             92    5   28    9    4
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2012-11-01T12:03:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2012-11-01T12:03:56)
    0000   0xb8 0xc3 0x4c 0x01 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 BolusWizard 2012-11-01T12:15:18 head[2], body[13] op[0x5b]
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
    datetime (2012-11-01T12:15:18)
    0000   0x92 0xcf 0x0c 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [1, 1, 0]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 4.8, 'curve': 4},
 {'age': 21, 'amount': 0.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0x0b 0x04 0x20 0x15 0x04    \.... ..
    decimal
             92    8  192   11    4   32   21    4
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2012-11-01T12:15:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-11-01T12:15:18)
    0000   0x92 0xcf 0x4c 0x01 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 BolusWizard 2012-11-01T13:20:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
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
    datetime (2012-11-01T13:20:44)
    0000   0xac 0xd4 0x0d 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [1, 1, 0]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 2.0, 'curve': 4},
 {'age': 76, 'amount': 4.8, 'curve': 4},
 {'age': 86, 'amount': 0.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x42 0x04 0xc0 0x4c 0x04    \.PB..L.
    0008   0x20 0x56 0x04                              V.
    decimal
             92   11   80   66    4  192   76    4
             32   86    4
    datetime (unknown)

    body (0)

#### RECORD 81 Bolus 2012-11-01T13:20:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-11-01T13:20:44)
    0000   0xac 0xd4 0x4d 0x01 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-23.data: 82 records`
