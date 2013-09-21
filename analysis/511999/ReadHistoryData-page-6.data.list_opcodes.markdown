## START analysis/sarak/raw//ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x19 0xea                                  ..
##### DEBUG DECIMAL
             25  234
#### RECORD 0 Bolus 2013-08-21T19:16:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x30 0x00    ..D.D.0.
    decimal
              1    0   68    0   68    0   48    0
    datetime (2013-08-21T19:16:53)
    0000   0xb5 0x10 0x53 0x15 0x0d                   ..S..
    body (0)

#### RECORD 1 CalBGForPH 2013-08-21T22:57:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2013-08-21T22:57:39)
    0000   0xa7 0x39 0x36 0x15 0x0d                   .96..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 BolusWizard 2013-08-21T22:57:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 170,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2013-08-21T22:57:46)
    0000   0xae 0x39 0x16 0x15 0x0d                   .9...
    body (15)
    hex
    0000   0x12 0x50 0x00 0x64 0x3c 0x64 0x20 0x00    .P.d<d .
    0008   0x48 0x00 0x00 0x00 0x00 0x68 0x78         H....hx
    decimal
             18   80    0  100   60  100   32    0
             72    0    0    0    0  104  120
    HOUR BITS: [0, 0, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 224, 'amount': 1.7, 'curve': 192},
 {'age': 8, 'amount': 0.65, 'curve': 208},
 {'age': 18, 'amount': 0.85, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x44 0xe0 0xc0 0x1a 0x08 0xd0    \.D.....
    0008   0x22 0x12 0xd0                             "..
    decimal
             92   11   68  224  192   26    8  208
             34   18  208
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-08-21T22:57:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x00 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    0    0
    datetime (2013-08-21T22:57:46)
    0000   0xae 0x39 0x56 0x15 0x0d                   .9V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BolusWizard 2013-08-21T23:06:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 170,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.4,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2013-08-21T23:06:41)
    0000   0xa9 0x06 0x17 0x15 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x20 0x00    .P.d<d .
    0008   0x54 0x00 0x00 0x68 0x00 0x54 0x78         T..h.Tx
    decimal
             21   80    0  100   60  100   32    0
             84    0    0  104    0   84  120

#### RECORD 6 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 2.6, 'curve': 192},
 {'age': 233, 'amount': 1.7, 'curve': 192},
 {'age': 17, 'amount': 0.65, 'curve': 208},
 {'age': 27, 'amount': 0.85, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0x0d 0xc0 0x44 0xe9 0xc0    \.h..D..
    0008   0x1a 0x11 0xd0 0x22 0x1b 0xd0              ..."..
    decimal
             92   14  104   13  192   68  233  192
             26   17  208   34   27  208
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-08-21T23:06:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x68 0x00    ..T.T.h.
    decimal
              1    0   84    0   84    0  104    0
    datetime (2013-08-21T23:06:41)
    0000   0xa9 0x06 0x57 0x15 0x0d                   ..W..
    body (0)

#### RECORD 8 BasalProfileStart 2013-08-22T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-22T00:00:00)
    0000   0x80 0x00 0x00 0x16 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 9 MResultTotals 2013-08-22T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x8c                   .....
    decimal
              7    0    0    5  140
    datetime (2013-08-22T00:00:00)
    0000   0x95 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 10 Sara6E 2013-08-22T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-22T00:00:00)
    0000   0x95 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0xb1 0x00 0x00 0x08 0x00 0x00    ........
    0008   0x05 0x8c 0x02 0xdc 0x34 0x02 0xb0 0x30    ....4..0
    0010   0x00 0x99 0x01 0xb4 0x00 0x94 0x00 0x68    .......h
    0018   0x00 0x00 0x06 0x02 0x01 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x61    .......a
    0028   0x26 0x00 0x00 0x00 0x00 0x00 0x00 0x00    &.......
    0030   0x00                                       .
    decimal
              5    0  177    0    0    8    0    0
              5  140    2  220   52    2  176   48
              0  153    1  180    0  148    0  104
              0    0    6    2    1    0    4    0
              0    0    0    0    0    0    0   97
             38    0    0    0    0    0    0    0
              0

#### RECORD 11 BasalProfileStart 2013-08-22T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-22T04:00:00)
    0000   0x80 0x00 0x04 0x16 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 12 BasalProfileStart 2013-08-22T07:46:20 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-22T07:46:20)
    0000   0x94 0x2e 0x07 0x16 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [0, 0, 1]
#### RECORD 13 Prime 2013-08-22T07:45:46 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-22T07:45:46)
    0000   0xae 0x2d 0x07 0x16 0x0d                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 BasalProfileStart 2013-08-22T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-22T08:00:00)
    0000   0x80 0x00 0x08 0x16 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 15 CalBGForPH 2013-08-22T09:03:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-08-22T09:03:13)
    0000   0x8d 0x03 0x29 0x16 0x0d                   ..)..
    body (0)

#### RECORD 16 BolusWizard 2013-08-22T09:03:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 7.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2013-08-22T09:03:31)
    0000   0x9f 0x03 0x09 0x16 0x0d                   .....
    body (15)
    hex
    0000   0x1b 0x50 0x00 0x78 0x3c 0x64 0x48 0x00    .P.x<dH.
    0008   0x58 0x00 0x00 0x00 0x00 0xa0 0x78         X.....x
    decimal
             27   80    0  120   60  100   72    0
             88    0    0    0    0  160  120

#### RECORD 17 Bolus 2013-08-22T09:03:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x00 0x00    ........
    decimal
              1    0  160    0  160    0    0    0
    datetime (2013-08-22T09:03:31)
    0000   0x9f 0x03 0x49 0x16 0x0d                   ..I..
    body (0)

#### RECORD 18 BasalProfileStart 2013-08-22T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-22T12:00:00)
    0000   0x80 0x00 0x0c 0x16 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 19 CalBGForPH 2013-08-22T14:32:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2013-08-22T14:32:45)
    0000   0xad 0x20 0x2e 0x16 0x0d                   . ...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 BolusWizard 2013-08-22T14:33:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 79,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 32,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 24.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x4f                                  [O
    decimal
             91   79
    datetime (2013-08-22T14:33:01)
    0000   0x81 0x21 0x0e 0x76 0x0d                   .!.v.
    body (15)
    hex
    0000   0x20 0x50 0x00 0x78 0x3c 0x64 0xf0 0x00     P.x<d..
    0008   0x68 0xf8 0x00 0x00 0x00 0x58 0x78         h....Xx
    decimal
             32   80    0  120   60  100  240    0
            104  248    0    0    0   88  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 74, 'amount': 4.0, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0x4a 0xd0                   \..J.
    decimal
             92    5  160   74  208
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-08-22T14:33:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x01    ..X.X...
    decimal
              1    0   88    0   88    0    0    1
    datetime (2013-08-22T14:33:01)
    0000   0x81 0x21 0x6e 0x76 0x0d                   .!nv.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 CalBGForPH 2013-08-22T15:11:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-08-22T15:11:55)
    0000   0xb7 0x0b 0x2f 0x16 0x0d                   ../..
    body (0)

#### RECORD 24 CalBGForPH 2013-08-22T20:04:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-22T20:04:44)
    0000   0xac 0x04 0x34 0x16 0x0d                   ..4..
    body (0)

#### RECORD 25 BolusWizard 2013-08-22T20:04:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-22T20:04:59)
    0000   0xbb 0x04 0x14 0x16 0x0d                   .....
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0x00 0x00 0x38 0x78         8....8x
    decimal
             14   80    0  100   60  100    0    0
             56    0    0    0    0   56  120

#### RECORD 26 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 0.75, 'curve': 208},
 {'age': 65, 'amount': 0.7, 'curve': 208},
 {'age': 75, 'amount': 0.75, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x1e 0x37 0xd0 0x1c 0x41 0xd0    \..7..A.
    0008   0x1e 0x4b 0xd0                             .K.
    decimal
             92   11   30   55  208   28   65  208
             30   75  208
    datetime (unknown)

    body (0)

#### RECORD 27 BolusWizard 2013-08-22T20:05:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-22T20:05:02)
    0000   0x82 0x05 0x14 0x16 0x0d                   .....
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0x00 0x00 0x38 0x78         8....8x
    decimal
             14   80    0  100   60  100    0    0
             56    0    0    0    0   56  120

#### RECORD 28 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 0.75, 'curve': 208},
 {'age': 66, 'amount': 0.7, 'curve': 208},
 {'age': 76, 'amount': 0.75, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x1e 0x38 0xd0 0x1c 0x42 0xd0    \..8..B.
    0008   0x1e 0x4c 0xd0                             .L.
    decimal
             92   11   30   56  208   28   66  208
             30   76  208
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-08-22T20:05:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-22T20:05:02)
    0000   0x82 0x05 0x54 0x16 0x0d                   ..T..
    body (0)

#### RECORD 30 BasalProfileStart 2013-08-23T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-23T00:00:00)
    0000   0x80 0x00 0x00 0x17 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 31 MResultTotals 2013-08-23T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x0c                   .....
    decimal
              7    0    0    4   12
    datetime (2013-08-23T00:00:00)
    0000   0x96 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 32 Sara6E 2013-08-23T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-23T00:00:00)
    0000   0x96 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0x80 0x00 0x00 0x04 0x00 0x00    ........
    0008   0x04 0x0c 0x02 0xdc 0x47 0x01 0x30 0x1d    ....G.0.
    0010   0x00 0x49 0x00 0x90 0x00 0x00 0x00 0xa0    .I......
    0018   0x00 0x00 0x02 0x00 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x4f    .......O
    0028   0xe7 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  128    0    0    4    0    0
              4   12    2  220   71    1   48   29
              0   73    0  144    0    0    0  160
              0    0    2    0    1    0    0    0
              0    0    0    0    0    0    0   79
            231    0    0    0    0    0    0    0
              0

#### RECORD 33 BasalProfileStart 2013-08-23T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-23T04:00:00)
    0000   0x80 0x00 0x04 0x17 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 34 LowReservoir 2013-08-23T04:36:21 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-23T04:36:21)
    0000   0x95 0x24 0x04 0x17 0x0d                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 CalBGForPH 2013-08-23T07:56:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 265}
```
    op hex (2)
    0000   0x0a 0x09                                  ..
    decimal
             10    9
    datetime (2013-08-23T07:56:58)
    0000   0xba 0x38 0x27 0x17 0x8d                   .8'..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 36 BolusWizard 2013-08-23T07:57:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 265,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 9.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x09                                  [.
    decimal
             91    9
    datetime (2013-08-23T07:57:02)
    0000   0x82 0x39 0x07 0x17 0x0d                   .9...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x60 0x00    .Q.x<d`.
    0008   0x00 0x00 0x00 0x00 0x00 0x60 0x78         .....`x
    decimal
              0   81    0  120   60  100   96    0
              0    0    0    0    0   96  120
    HOUR BITS: [0, 0, 1]
#### RECORD 37 Bolus 2013-08-23T07:57:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x00 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    0    0
    datetime (2013-08-23T07:57:02)
    0000   0x82 0x39 0x47 0x17 0x0d                   .9G..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 38 BasalProfileStart 2013-08-23T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-23T08:00:00)
    0000   0x80 0x00 0x08 0x17 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 39 CalBGForPH 2013-08-23T11:15:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-08-23T11:15:48)
    0000   0xb0 0x0f 0x2b 0x17 0x0d                   ..+..
    body (0)

#### RECORD 40 BolusWizard 2013-08-23T11:15:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-08-23T11:15:58)
    0000   0xba 0x0f 0x0b 0x17 0x0d                   .....
    body (15)
    hex
    0000   0x21 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    !P.x<d..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x78         l....lx
    decimal
             33   80    0  120   60  100    0    0
            108    0    0    0    0  108  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 202, 'amount': 2.4, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0xca 0xc0                   \.`..
    decimal
             92    5   96  202  192
    datetime (unknown)

    body (0)

#### RECORD 42 LowReservoir 2013-08-23T11:17:18 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-08-23T11:17:18)
    0000   0x92 0x11 0x0b 0x17 0x0d                   .....
    body (0)

#### RECORD 43 Bolus 2013-08-23T11:15:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-08-23T11:15:58)
    0000   0xba 0x0f 0x4b 0x17 0x0d                   ..K..
    body (0)

#### RECORD 44 CalBGForPH 2013-08-23T11:39:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-08-23T11:39:50)
    0000   0xb2 0x27 0x2b 0x17 0x0d                   .'+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 BolusWizard 2013-08-23T11:39:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.4,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2013-08-23T11:39:55)
    0000   0xb7 0x27 0x0b 0x17 0x0d                   .'...
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x68 0x00 0x28 0x78         (..h.(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0  104    0   40  120
    HOUR BITS: [0, 0, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 2.7, 'curve': 192},
 {'age': 226, 'amount': 2.4, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x1a 0xc0 0x60 0xe2 0xc0    \.l..`..
    decimal
             92    8  108   26  192   96  226  192
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-08-23T11:39:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x68 0x00    ..(.(.h.
    decimal
              1    0   40    0   40    0  104    0
    datetime (2013-08-23T11:39:55)
    0000   0xb7 0x27 0x4b 0x17 0x0d                   .'K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 BasalProfileStart 2013-08-23T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-23T12:00:00)
    0000   0x80 0x00 0x0c 0x17 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 49 CalBGForPH 2013-08-23T15:20:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 299}
```
    op hex (2)
    0000   0x0a 0x2b                                  .+
    decimal
             10   43
    datetime (2013-08-23T15:20:07)
    0000   0x87 0x14 0x2f 0x17 0x8d                   ../..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 50 CalBGForPH 2013-08-23T15:21:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 283}
```
    op hex (2)
    0000   0x0a 0x1b                                  ..
    decimal
             10   27
    datetime (2013-08-23T15:21:38)
    0000   0xa6 0x15 0x2f 0x17 0x8d                   ../..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 51 BolusWizard 2013-08-23T15:21:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 283,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x1b                                  [.
    decimal
             91   27
    datetime (2013-08-23T15:21:44)
    0000   0xac 0x15 0x0f 0x17 0x0d                   .....
    body (15)
    hex
    0000   0x0f 0x51 0x00 0x78 0x3c 0x64 0x6c 0x00    .Q.x<dl.
    0008   0x30 0x00 0x00 0x00 0x00 0x9c 0x78         0.....x
    decimal
             15   81    0  120   60  100  108    0
             48    0    0    0    0  156  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 228, 'amount': 1.0, 'curve': 192},
 {'age': 248, 'amount': 2.7, 'curve': 192},
 {'age': 192, 'amount': 2.4, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0xe4 0xc0 0x6c 0xf8 0xc0    \.(..l..
    0008   0x60 0xc0 0xd0                             `..
    decimal
             92   11   40  228  192  108  248  192
             96  192  208
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-08-23T15:21:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x00 0x00    ........
    decimal
              1    0  156    0  156    0    0    0
    datetime (2013-08-23T15:21:44)
    0000   0xac 0x15 0x4f 0x17 0x0d                   ..O..
    body (0)

#### RECORD 54 Base (2013, 8, 23, 15, 52, 8) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2013, 8, 23, 15, 52, 8))
    0000   0x88 0x34 0x0f 0x17 0x0d                   .4...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 CalBGForPH 2013-08-23T17:48:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 311}
```
    op hex (2)
    0000   0x0a 0x37                                  .7
    decimal
             10   55
    datetime (2013-08-23T17:48:01)
    0000   0x81 0x30 0x31 0x17 0x8d                   .01..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 56 BolusWizard 2013-08-23T17:48:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 311,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 12.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x37                                  [7
    decimal
             91   55
    datetime (2013-08-23T17:48:03)
    0000   0x83 0x30 0x11 0x17 0x0d                   .0...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x7c 0x00    .Q.d<d|.
    0008   0x00 0x00 0x00 0x14 0x00 0x68 0x78         .....hx
    decimal
              0   81    0  100   60  100  124    0
              0    0    0   20    0  104  120
    HOUR BITS: [0, 0, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 145, 'amount': 2.05, 'curve': 192},
 {'age': 155, 'amount': 1.85, 'curve': 192},
 {'age': 119, 'amount': 1.0, 'curve': 208},
 {'age': 139, 'amount': 2.7, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x52 0x91 0xc0 0x4a 0x9b 0xc0    \.R..J..
    0008   0x28 0x77 0xd0 0x6c 0x8b 0xd0              (w.l..
    decimal
             92   14   82  145  192   74  155  192
             40  119  208  108  139  208
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-08-23T17:48:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x14 0x00    ..h.h...
    decimal
              1    0  104    0  104    0   20    0
    datetime (2013-08-23T17:48:03)
    0000   0x83 0x30 0x51 0x17 0x0d                   .0Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 59 BolusWizard 2013-08-23T20:35:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-23T20:35:28)
    0000   0x9c 0x23 0x14 0x77 0x0d                   .#.w.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x78         P....Px
    decimal
             20   80    0  100   60  100    0    0
             80    0    0    0    0   80  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 172, 'amount': 2.6, 'curve': 192},
 {'age': 56, 'amount': 2.05, 'curve': 208},
 {'age': 66, 'amount': 1.85, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0xac 0xc0 0x52 0x38 0xd0    \.h..R8.
    0008   0x4a 0x42 0xd0                             JB.
    decimal
             92   11  104  172  192   82   56  208
             74   66  208
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-08-23T20:35:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x08 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    8    0
    datetime (2013-08-23T20:35:28)
    0000   0x9c 0x23 0x54 0x77 0x0d                   .#Tw.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 Rewind 2013-08-23T23:40:48 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-23T23:40:48)
    0000   0xb0 0x28 0x17 0x17 0x0d                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 Prime 2013-08-23T23:41:45 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2c                   ....,
    decimal
              3    0    0    0   44
    datetime (2013-08-23T23:41:45)
    0000   0xad 0x29 0x37 0x17 0x0d                   .)7..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 MResultTotals 2013-08-24T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x1b                   .....
    decimal
              7    0    0    5   27
    datetime (2013-08-24T00:00:00)
    0000   0x97 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 65 Sara6E 2013-08-24T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-24T00:00:00)
    0000   0x97 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0xe8 0x00 0x00 0x06 0x00 0x00    ........
    0008   0x05 0x1b 0x02 0xd3 0x37 0x02 0x48 0x2d    ....7.H-
    0010   0x00 0x51 0x00 0xe4 0x00 0xc8 0x00 0x9c    .Q......
    0018   0x00 0x00 0x03 0x02 0x01 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x70    .......p
    0028   0x37 0x00 0x00 0x00 0x00 0x00 0x00 0x00    7.......
    0030   0x00                                       .
    decimal
              5    0  232    0    0    6    0    0
              5   27    2  211   55    2   72   45
              0   81    0  228    0  200    0  156
              0    0    3    2    1    0    4    0
              0    0    0    0    0    0    0  112
             55    0    0    0    0    0    0    0
              0

#### RECORD 66 BasalProfileStart 2013-08-24T04:31:30 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-24T04:31:30)
    0000   0x9e 0x1f 0x04 0x18 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 67 CalBGForPH 2013-08-24T04:32:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 443}
```
    op hex (2)
    0000   0x0a 0xbb                                  ..
    decimal
             10  187
    datetime (2013-08-24T04:32:27)
    0000   0x9b 0x20 0x24 0x18 0x8d                   . $..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 68 BolusWizard 2013-08-24T04:32:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 443,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 20.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbb                                  [.
    decimal
             91  187
    datetime (2013-08-24T04:32:29)
    0000   0x9d 0x20 0x04 0x18 0x0d                   . ...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x6e 0xd0 0x00    .Q.x<n..
    0008   0x00 0x00 0x00 0x00 0x00 0xd0 0x82         .......
    decimal
              0   81    0  120   60  110  208    0
              0    0    0    0    0  208  130
    HOUR BITS: [0, 0, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 223, 'amount': 2.0, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0xdf 0xd0                   \.P..
    decimal
             92    5   80  223  208
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-08-24T04:32:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 20.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xd0 0x00 0xd0 0x00 0x00 0x00    ........
    decimal
              1    0  208    0  208    0    0    0
    datetime (2013-08-24T04:32:29)
    0000   0x9d 0x20 0x44 0x18 0x0d                   . D..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 71 BasalProfileStart 2013-08-24T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-24T08:00:00)
    0000   0x80 0x00 0x08 0x18 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 72 CalBGForPH 2013-08-24T11:06:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-08-24T11:06:35)
    0000   0xa3 0x06 0x2b 0x18 0x0d                   ..+..
    body (0)

#### RECORD 73 BolusWizard 2013-08-24T11:06:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 115,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-08-24T11:06:44)
    0000   0xac 0x06 0x0b 0x18 0x0d                   .....
    body (15)
    hex
    0000   0x11 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x38 0x00 0x00 0x00 0x00 0x38 0x78         8....8x
    decimal
             17   80    0  120   60  100    0    0
             56    0    0    0    0   56  120

`end analysis/sarak/raw//ReadHistoryData-page-6.data: 74 records`
