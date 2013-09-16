## START logs/ReadHistoryData-page-17.data
#### RECORD 0 Sara6E 2013-07-30T04:00:00 head[54], body[3] op[0x6e]

    op hex (54)
    0000   0x6e 0x7d 0x8d 0x05 0x00 0x9b 0x00 0x00    n}......
    0008   0x07 0x00 0x00 0x04 0xbc 0x02 0xdc 0x3c    .......<
    0010   0x01 0xe0 0x28 0x00 0x60 0x00 0xc4 0x00    ..(.`...
    0018   0x70 0x00 0xac 0x00 0x00 0x03 0x02 0x02    p.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6b 0xec 0x00 0x00 0x00 0x00    ..k.....
    0030   0x00 0x00 0x00 0x00 0x7b 0x01              ....{.
    decimal
            110  125  141    5    0  155    0    0
              7    0    0    4  188    2  220   60
              1  224   40    0   96    0  196    0
            112    0  172    0    0    3    2    2
              0    0    0    0    0    0    0    0
              0    0  107  236    0    0    0    0
              0    0    0    0  123    1
    datetime (2013-07-30T04:00:00)
    0000   0x40 0xc0 0x04 0x1e 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 1 Sara7B 2013-07-30T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-30T08:00:00)
    0000   0x40 0xc0 0x08 0x1e 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 2 CalBGForPH 2013-07-30T09:52:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-07-30T09:52:13)
    0000   0x4d 0xf4 0x29 0x1e 0x0d                   M.)..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 BolusWizard 2013-07-30T09:52:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 76,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 24.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x4c                                  [L
    decimal
             91   76
    datetime (2013-07-30T09:52:23)
    0000   0x57 0xf4 0x09 0x7e 0x0d                   W..~.
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0xf0 0x00    .P.x<d..
    0008   0x34 0xf8 0x00 0x00 0x00 0x24 0x78         4....$x
    decimal
             16   80    0  120   60  100  240    0
             52  248    0    0    0   36  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 Bolus 2013-07-30T09:52:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x00 0x00    ..$.$...
    decimal
              1    0   36    0   36    0    0    0
    datetime (2013-07-30T09:52:23)
    0000   0x57 0xf4 0x49 0x7e 0x0d                   W.I~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 Sara7B 2013-07-30T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-30T12:00:00)
    0000   0x40 0xc0 0x0c 0x1e 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2013-07-30T12:50:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-07-30T12:50:22)
    0000   0x56 0xf2 0x2c 0x1e 0x0d                   V.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 BolusWizard 2013-07-30T12:50:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-07-30T12:50:31)
    0000   0x5f 0xf2 0x0c 0x7e 0x0d                   _..~.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x04 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0    4    0   64  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 177, 'amount': 0.475, 'curve': 192},
 {'age': 187, 'amount': 0.425, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x13 0xb1 0xc0 0x11 0xbb 0xc0    \.......
    decimal
             92    8   19  177  192   17  187  192
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-07-30T12:50:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x04 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    4    0
    datetime (2013-07-30T12:50:31)
    0000   0x5f 0xf2 0x4c 0x7e 0x0d                   _.L~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 CalBGForPH 2013-07-30T13:13:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2013-07-30T13:13:40)
    0000   0x68 0xcd 0x2d 0x1e 0x0d                   h.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 BolusWizard 2013-07-30T13:13:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 253,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfd                                  [.
    decimal
             91  253
    datetime (2013-07-30T13:13:43)
    0000   0x6b 0xcd 0x0d 0x7e 0x0d                   k..~.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x58 0x00    .P.x<dX.
    0008   0x00 0x00 0x00 0x3c 0x00 0x1c 0x78         ...<..x
    decimal
              0   80    0  120   60  100   88    0
              0    0    0   60    0   28  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.6, 'curve': 192},
 {'age': 200, 'amount': 0.475, 'curve': 192},
 {'age': 210, 'amount': 0.425, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x1e 0xc0 0x13 0xc8 0xc0    \.@.....
    0008   0x11 0xd2 0xc0                             ...
    decimal
             92   11   64   30  192   19  200  192
             17  210  192
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-07-30T13:13:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x3c 0x00    ......<.
    decimal
              1    0   28    0   28    0   60    0
    datetime (2013-07-30T13:13:43)
    0000   0x6b 0xcd 0x4d 0x7e 0x0d                   k.M~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 CalBGForPH 2013-07-30T15:14:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-07-30T15:14:10)
    0000   0x4a 0xce 0x2f 0x1e 0x0d                   J./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2013-07-30T15:14:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-07-30T15:14:24)
    0000   0x58 0xce 0x2f 0x1e 0x0d                   X./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 16 BolusWizard 2013-07-30T15:14:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 72,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 23.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x48                                  [H
    decimal
             91   72
    datetime (2013-07-30T15:14:38)
    0000   0x66 0xce 0x0f 0x7e 0x0d                   f..~.
    body (15)
    hex
    0000   0x21 0x50 0x00 0x78 0x3c 0x64 0xec 0x00    !P.x<d..
    0008   0x6c 0xf8 0x00 0x10 0x00 0x58 0x78         l....Xx
    decimal
             33   80    0  120   60  100  236    0
            108  248    0   16    0   88  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 0.7, 'curve': 192},
 {'age': 151, 'amount': 1.6, 'curve': 192},
 {'age': 65, 'amount': 0.475, 'curve': 208},
 {'age': 75, 'amount': 0.425, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1c 0x79 0xc0 0x40 0x97 0xc0    \..y.@..
    0008   0x13 0x41 0xd0 0x11 0x4b 0xd0              .A..K.
    decimal
             92   14   28  121  192   64  151  192
             19   65  208   17   75  208
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-07-30T15:14:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x10 0x00    ..X.X...
    decimal
              1    0   88    0   88    0   16    0
    datetime (2013-07-30T15:14:38)
    0000   0x66 0xce 0x4f 0x7e 0x0d                   f.O~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 19 CalBGForPH 2013-07-30T15:55:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-07-30T15:55:46)
    0000   0x6e 0xf7 0x2f 0x1e 0x0d                   n./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 BolusWizard 2013-07-30T15:55:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.0,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-07-30T15:55:57)
    0000   0x79 0xf7 0x0f 0x7e 0x0d                   y..~.
    body (15)
    hex
    0000   0x17 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x4c 0x00 0x00 0x50 0x00 0x4c 0x78         L..P.Lx
    decimal
             23   80    0  120   60  100    0    0
             76    0    0   80    0   76  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 42, 'amount': 2.2, 'curve': 192},
 {'age': 162, 'amount': 0.7, 'curve': 192},
 {'age': 192, 'amount': 1.6, 'curve': 192},
 {'age': 106, 'amount': 0.475, 'curve': 208},
 {'age': 116, 'amount': 0.425, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x58 0x2a 0xc0 0x1c 0xa2 0xc0    \.X*....
    0008   0x40 0xc0 0xc0 0x13 0x6a 0xd0 0x11 0x74    @...j..t
    0010   0xd0                                       .
    decimal
             92   17   88   42  192   28  162  192
             64  192  192   19  106  208   17  116
            208
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-07-30T15:55:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x50 0x00    ..8.8.P.
    decimal
              1    0   56    0   56    0   80    0
    datetime (2013-07-30T15:55:57)
    0000   0x79 0xf7 0x4f 0x7e 0x0d                   y.O~.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 CalBGForPH 2013-07-30T18:27:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-07-30T18:27:09)
    0000   0x49 0xdb 0x32 0x1e 0x0d                   I.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 BolusWizard 2013-07-30T18:27:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-30T18:27:12)
    0000   0x4c 0xdb 0x12 0x7e 0x0d                   L..~.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x00 0x00 0x00 0x08 0x00 0x28 0x78         .....(x
    decimal
              0   80    0  100   60  100   48    0
              0    0    0    8    0   40  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 154, 'amount': 1.4, 'curve': 192},
 {'age': 194, 'amount': 2.2, 'curve': 192},
 {'age': 58, 'amount': 0.7, 'curve': 208},
 {'age': 88, 'amount': 1.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x9a 0xc0 0x58 0xc2 0xc0    \.8..X..
    0008   0x1c 0x3a 0xd0 0x40 0x58 0xd0              .:.@X.
    decimal
             92   14   56  154  192   88  194  192
             28   58  208   64   88  208
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-07-30T18:27:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x08 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    8    0
    datetime (2013-07-30T18:27:12)
    0000   0x4c 0xdb 0x52 0x7e 0x0d                   L.R~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 CalBGForPH 2013-07-30T19:04:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2013-07-30T19:04:50)
    0000   0x72 0xc4 0x33 0x1e 0x0d                   r.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 BolusWizard 2013-07-30T19:05:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 131,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2013-07-30T19:05:00)
    0000   0x40 0xc5 0x13 0x7e 0x0d                   @..~.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x04 0x00    .P.d<d..
    0008   0x58 0x00 0x00 0x24 0x00 0x58 0x78         X..$.Xx
    decimal
             22   80    0  100   60  100    4    0
             88    0    0   36    0   88  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 1.0, 'curve': 192},
 {'age': 191, 'amount': 1.4, 'curve': 192},
 {'age': 231, 'amount': 2.2, 'curve': 192},
 {'age': 95, 'amount': 0.7, 'curve': 208},
 {'age': 125, 'amount': 1.6, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0x29 0xc0 0x38 0xbf 0xc0    \.().8..
    0008   0x58 0xe7 0xc0 0x1c 0x5f 0xd0 0x40 0x7d    X..._.@}
    0010   0xd0                                       .
    decimal
             92   17   40   41  192   56  191  192
             88  231  192   28   95  208   64  125
            208
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-07-30T19:05:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x24 0x00    ..X.X.$.
    decimal
              1    0   88    0   88    0   36    0
    datetime (2013-07-30T19:05:00)
    0000   0x40 0xc5 0x53 0x7e 0x0d                   @.S~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 CalBGForPH 2013-07-30T20:22:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-07-30T20:22:24)
    0000   0x58 0xd6 0x34 0x1e 0x0d                   X.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 32 BolusWizard 2013-07-30T20:22:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-07-30T20:22:30)
    0000   0x5e 0xd6 0x14 0x7e 0x0d                   ^..~.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x20 0x00    .P.d<d .
    0008   0x3c 0x00 0x00 0x3c 0x00 0x3c 0x78         <..<.<x
    decimal
             15   80    0  100   60  100   32    0
             60    0    0   60    0   60  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 2.2, 'curve': 192},
 {'age': 119, 'amount': 1.0, 'curve': 192},
 {'age': 13, 'amount': 1.4, 'curve': 208},
 {'age': 53, 'amount': 2.2, 'curve': 208},
 {'age': 173, 'amount': 0.7, 'curve': 208},
 {'age': 203, 'amount': 1.6, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x58 0x4f 0xc0 0x28 0x77 0xc0    \.XO.(w.
    0008   0x38 0x0d 0xd0 0x58 0x35 0xd0 0x1c 0xad    8..X5...
    0010   0xd0 0x40 0xcb 0xd0                        .@..
    decimal
             92   20   88   79  192   40  119  192
             56   13  208   88   53  208   28  173
            208   64  203  208
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-07-30T20:22:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x3c 0x00    ..<.<.<.
    decimal
              1    0   60    0   60    0   60    0
    datetime (2013-07-30T20:22:30)
    0000   0x5e 0xd6 0x54 0x7e 0x0d                   ^.T~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 CalBGForPH 2013-07-30T23:21:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-07-30T23:21:38)
    0000   0x66 0xd5 0x37 0x1e 0x0d                   f.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 BolusWizard 2013-07-30T23:21:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 1.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2013-07-30T23:21:54)
    0000   0x76 0xd5 0x17 0x7e 0x0d                   v..~.
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x64 0x3c 0x64 0x0c 0x00    .P.d<d..
    0008   0x34 0x00 0x00 0x04 0x00 0x3c 0x78         4....<x
    decimal
             13   80    0  100   60  100   12    0
             52    0    0    4    0   60  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 178, 'amount': 0.8, 'curve': 192},
 {'age': 188, 'amount': 0.7, 'curve': 192},
 {'age': 2, 'amount': 2.2, 'curve': 208},
 {'age': 42, 'amount': 1.0, 'curve': 208},
 {'age': 192, 'amount': 1.4, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0xb2 0xc0 0x1c 0xbc 0xc0    \. .....
    0008   0x58 0x02 0xd0 0x28 0x2a 0xd0 0x38 0xc0    X..(*.8.
    0010   0xd0                                       .
    decimal
             92   17   32  178  192   28  188  192
             88    2  208   40   42  208   56  192
            208
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-07-30T23:21:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x04 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    4    0
    datetime (2013-07-30T23:21:54)
    0000   0x76 0xd5 0x57 0x7e 0x0d                   v.W~.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 Sara7B 2013-07-31T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-31T00:00:00)
    0000   0x40 0xc0 0x00 0x1f 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 40 ResultTotals (2000, 6, 0, 0, 13, 62) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe4                   .....
    decimal
              7    0    0    4  228
    datetime ((2000, 6, 0, 0, 13, 62))
    0000   0x7e 0x8d 0x00 0x00 0x00                   ~....
    body (51)
    hex
    0000   0x6e 0x7e 0x8d 0x05 0x00 0x8a 0x00 0x00    n~......
    0008   0x0a 0x00 0x00 0x04 0xe4 0x02 0xdc 0x3a    .......:
    0010   0x02 0x08 0x2a 0x00 0x8e 0x01 0x88 0x00    ..*.....
    0018   0x44 0x00 0x3c 0x00 0x00 0x06 0x02 0x01    D.<.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x48 0xfd 0x00 0x00 0x00 0x00    ..H.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  126  141    5    0  138    0    0
             10    0    0    4  228    2  220   58
              2    8   42    0  142    1  136    0
             68    0   60    0    0    6    2    1
              0    0    0    0    0    0    0    0
              0    0   72  253    0    0    0    0
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 41 Base (2015, 1, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2015, 1, 4, 0, 0, 1))
    0000   0x01 0x40 0xc0 0x04 0x1f                   .@...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 42 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x40                   !.{.@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 43 Base (2000, 0, 2, 16, 13, 31) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x08                                  ..
    decimal
            192    8
    datetime ((2000, 0, 2, 16, 13, 31))
    0000   0x1f 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 44 CalBGForPH 2013-07-31T08:34:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-31T08:34:48)
    0000   0x70 0xe2 0x28 0x1f 0x0d                   p.(..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BolusWizard 2013-07-31T08:35:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 102,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-07-31T08:35:01)
    0000   0x41 0xe3 0x08 0x7f 0x0d                   A....
    body (15)
    hex
    0000   0x1a 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x78         T....Tx
    decimal
             26   80    0  120   60  100    0    0
             84    0    0    0    0   84  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 Bolus 2013-07-31T08:35:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2013-07-31T08:35:01)
    0000   0x41 0xe3 0x48 0x7f 0x0d                   A.H..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 Sara7B 2013-07-31T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-31T12:00:00)
    0000   0x40 0xc0 0x0c 0x1f 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 48 CalBGForPH 2013-07-31T12:49:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-31T12:49:37)
    0000   0x65 0xf1 0x2c 0x1f 0x0d                   e.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 BolusWizard 2013-07-31T12:50:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 102,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-07-31T12:50:46)
    0000   0x6e 0xf2 0x0c 0x1f 0x0d                   n....
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x78         0....0x
    decimal
             15   80    0  120   60  100    0    0
             48    0    0    0    0   48  120
    HOUR BITS: [1, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 1, 'amount': 1.8, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x48 0x01 0xd0                   \.H..
    decimal
             92    5   72    1  208
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-07-31T12:50:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x00 0x00    ..$.$...
    decimal
              1    0   36    0   36    0    0    0
    datetime (2013-07-31T12:50:46)
    0000   0x6e 0xf2 0x4c 0x1f 0x0d                   n.L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 CalBGForPH 2013-07-31T13:27:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2013-07-31T13:27:29)
    0000   0x5d 0xdb 0x2d 0x1f 0x0d                   ].-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 BolusWizard 2013-07-31T13:27:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2013-07-31T13:27:56)
    0000   0x78 0xdb 0x0d 0x1f 0x0d                   x....
    body (15)
    hex
    0000   0x21 0x50 0x00 0x78 0x3c 0x64 0x08 0x00    !P.x<d..
    0008   0x6c 0x00 0x00 0x20 0x00 0x6c 0x78         l.. .lx
    decimal
             33   80    0  120   60  100    8    0
            108    0    0   32    0  108  120
    HOUR BITS: [1, 1, 0]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 0.9, 'curve': 192},
 {'age': 38, 'amount': 1.8, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x2c 0xc0 0x48 0x26 0xd0    \.$,.H&.
    decimal
             92    8   36   44  192   72   38  208
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-07-31T13:27:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x20 0x00    ..T.T. .
    decimal
              1    0   84    0   84    0   32    0
    datetime (2013-07-31T13:27:56)
    0000   0x78 0xdb 0x4d 0x1f 0x0d                   x.M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 TempBasal 2013-07-31T14:06:22 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.85}
```
    op hex (2)
    0000   0x33 0x4a                                  3J
    decimal
             51   74
    datetime (2013-07-31T14:06:22)
    0000   0x56 0xc6 0x0e 0x1f 0x0d                   V....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 57 TempBasalDuration 2013-07-31T14:06:22 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 120}
```
    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2013-07-31T14:06:22)
    0000   0x56 0xc6 0x0e 0x1f 0x0d                   V....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 58 Sara7B 2013-07-31T16:06:23 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-31T16:06:23)
    0000   0x57 0xc6 0x10 0x1f 0x0d                   W....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 59 TempBasal 2013-07-31T18:25:34 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.75}
```
    op hex (2)
    0000   0x33 0x46                                  3F
    decimal
             51   70
    datetime (2013-07-31T18:25:34)
    0000   0x62 0xd9 0x12 0x1f 0x0d                   b....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 60 TempBasalDuration 2013-07-31T18:25:34 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 120}
```
    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2013-07-31T18:25:34)
    0000   0x62 0xd9 0x12 0x1f 0x0d                   b....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 61 Sara7B 2013-07-31T20:25:34 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-31T20:25:34)
    0000   0x62 0xd9 0x14 0x1f 0x0d                   b....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 62 CalBGForPH 2013-07-31T22:11:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-07-31T22:11:29)
    0000   0x5d 0xcb 0x36 0x1f 0x0d                   ].6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 BolusWizard 2013-07-31T22:11:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-07-31T22:11:50)
    0000   0x72 0xcb 0x16 0x1f 0x0d                   r....
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x3c 0x00 0x00 0x00 0x00 0x3c 0x78         <....<x
    decimal
             15   80    0  100   60  100    0    0
             60    0    0    0    0   60  120
    HOUR BITS: [1, 1, 0]
#### RECORD 64 Bolus 2013-07-31T22:11:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2013-07-31T22:11:50)
    0000   0x72 0xcb 0x56 0x1f 0x0d                   r.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 CalBGForPH 2013-07-31T22:33:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-07-31T22:33:12)
    0000   0x4c 0xe1 0x36 0x1f 0x0d                   L.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 BolusWizard 2013-07-31T22:33:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-07-31T22:33:20)
    0000   0x54 0xe1 0x16 0x1f 0x0d                   T....
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x2c 0x00 0x00 0x38 0x00 0x2c 0x78         ,..8.,x
    decimal
             11   80    0  100   60  100    0    0
             44    0    0   56    0   44  120
    HOUR BITS: [1, 1, 1]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.5, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x1e 0xc0                   \.<..
    decimal
             92    5   60   30  192
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-07-31T22:33:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x38 0x00    ..,.,.8.
    decimal
              1    0   44    0   44    0   56    0
    datetime (2013-07-31T22:33:21)
    0000   0x55 0xe1 0x56 0x1f 0x0d                   U.V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 Sara7B 2013-08-01T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-01T00:00:00)
    0000   0x80 0x00 0x00 0x01 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 70 ResultTotals (2000, 6, 0, 0, 13, 63) head[5], body[39] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xe2                   .....
    decimal
              7    0    0    3  226
    datetime ((2000, 6, 0, 0, 13, 63))
    0000   0x7f 0x8d 0x00 0x00 0x00                   .....
    body (39)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0xe9 0xb8         .......
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0  233  184
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-17.data: 71 records`
