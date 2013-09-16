## START logs/ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 534, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x60 0x78 0x01 0x00 0x60 0x00 0x60 0x00    `x..`.`.
    0008   0x00 0x00 0x82 0x39 0x47 0x17 0x0d 0x7b    ...9G..{
    0010   0x02 0x80 0x00 0x08 0x17 0x0d 0x10 0x22    ......."
    0018   0x00 0x0a 0x7a 0xb0 0x0f 0x2b 0x17 0x0d    ..z..+..
##### DEBUG DECIMAL
             96  120    1    0   96    0   96    0
              0    0  130   57   71   23   13  123
              2  128    0    8   23   13   16   34
              0   10  122  176   15   43   23   13
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

#### RECORD 8 Sara7B 2013-08-22T00:00:00 head[2], body[3] op[0x7b]

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

#### RECORD 9 ResultTotals (2000, 8, 0, 0, 13, 21) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x8c                   .....
    decimal
              7    0    0    5  140
    datetime ((2000, 8, 0, 0, 13, 21))
    0000   0x95 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x95 0x0d 0x05 0x00 0xb1 0x00 0x00    n.......
    0008   0x08 0x00 0x00 0x05 0x8c 0x02 0xdc 0x34    .......4
    0010   0x02 0xb0 0x30 0x00 0x99 0x01 0xb4 0x00    ..0.....
    0018   0x94 0x00 0x68 0x00 0x00 0x06 0x02 0x01    ..h.....
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x61 0x26 0x00 0x00 0x00 0x00    ..a&....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  149   13    5    0  177    0    0
              8    0    0    5  140    2  220   52
              2  176   48    0  153    1  180    0
            148    0  104    0    0    6    2    1
              0    4    0    0    0    0    0    0
              0    0   97   38    0    0    0    0
              0    0    0

#### RECORD 10 Base (2006, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2006, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x16                   .....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 11 Base (2004, 0, 1, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2004, 0, 1, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x01 0x94                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 12 Base (2000, 0, 1, 8, 13, 22) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0x07                                  ..
    decimal
             46    7
    datetime ((2000, 0, 1, 8, 13, 22))
    0000   0x16 0x0d 0x08 0x21 0x00                   ...!.
    body (0)
    DAY BITS: [0, 0, 1]
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
#### RECORD 14 Sara7B 2013-08-22T08:00:00 head[2], body[3] op[0x7b]

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

#### RECORD 18 Sara7B 2013-08-22T12:00:00 head[2], body[3] op[0x7b]

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

#### RECORD 30 Sara7B 2013-08-23T00:00:00 head[2], body[3] op[0x7b]

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

#### RECORD 31 ResultTotals (2000, 8, 0, 0, 13, 22) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x0c                   .....
    decimal
              7    0    0    4   12
    datetime ((2000, 8, 0, 0, 13, 22))
    0000   0x96 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x96 0x0d 0x05 0x00 0x80 0x00 0x00    n.......
    0008   0x04 0x00 0x00 0x04 0x0c 0x02 0xdc 0x47    .......G
    0010   0x01 0x30 0x1d 0x00 0x49 0x00 0x90 0x00    .0..I...
    0018   0x00 0x00 0xa0 0x00 0x00 0x02 0x00 0x01    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x4f 0xe7 0x00 0x00 0x00 0x00    ..O.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  150   13    5    0  128    0    0
              4    0    0    4   12    2  220   71
              1   48   29    0   73    0  144    0
              0    0  160    0    0    2    0    1
              0    0    0    0    0    0    0    0
              0    0   79  231    0    0    0    0
              0    0    0

#### RECORD 32 Base (2007, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2007, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x17                   .....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 33 Base (2005, 0, 8, 20, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2005, 0, 8, 20, 0, 33))
    0000   0x21 0x00 0x34 0xc8 0x95                   !.4..
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 34 Base (2010, 0, 9, 10, 13, 23) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x04                                  $.
    decimal
             36    4
    datetime ((2010, 0, 9, 10, 13, 23))
    0000   0x17 0x0d 0x0a 0x09 0xba                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 35 Base (2002, 2, 9, 27, 13, 23) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x27                                  8'
    decimal
             56   39
    datetime ((2002, 2, 9, 27, 13, 23))
    0000   0x17 0x8d 0x5b 0x09 0x82                   ..[..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 36 Base (2000, 0, 17, 0, 13, 23) head[2], body[0] op[0x39]

    op hex (2)
    0000   0x39 0x07                                  9.
    decimal
             57    7
    datetime ((2000, 0, 17, 0, 13, 23))
    0000   0x17 0x0d 0x00 0x51 0x00                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 37 Base (2000, 5, 0, 0, 32, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 5, 0, 0, 32, 36))
    0000   0x64 0x60 0x00 0x00 0x00                   d`...
    body (0)
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-6.data: 38 records`
