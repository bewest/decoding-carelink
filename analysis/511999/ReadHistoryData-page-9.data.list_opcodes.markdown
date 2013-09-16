## START logs/ReadHistoryData-page-9.data
#### RECORD 0 CalBGForPH 2013-08-14T20:04:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 297}
```
    op hex (2)
    0000   0x0a 0x29                                  .)
    decimal
             10   41
    datetime (2013-08-14T20:04:52)
    0000   0xb4 0x04 0x34 0x0e 0x8d                   ..4..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 BolusWizard 2013-08-14T20:04:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 297,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 11.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x29                                  [)
    decimal
             91   41
    datetime (2013-08-14T20:04:55)
    0000   0xb7 0x04 0x14 0x0e 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x74 0x00    .Q.d<dt.
    0008   0x00 0x00 0x00 0x00 0x00 0x74 0x78         .....tx
    decimal
              0   81    0  100   60  100  116    0
              0    0    0    0    0  116  120

#### RECORD 2 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 181, 'amount': 0.3, 'curve': 192},
 {'age': 5, 'amount': 1.4, 'curve': 208},
 {'age': 35, 'amount': 1.4, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0xb5 0xc0 0x38 0x05 0xd0    \....8..
    0008   0x38 0x23 0xd0                             8#.
    decimal
             92   11   12  181  192   56    5  208
             56   35  208
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2013-08-14T20:04:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2013-08-14T20:04:55)
    0000   0xb7 0x04 0x54 0x0e 0x0d                   ..T..
    body (0)

#### RECORD 4 CalBGForPH 2013-08-14T21:45:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 355}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2013-08-14T21:45:41)
    0000   0xa9 0x2d 0x35 0x0e 0x8d                   .-5..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 BolusWizard 2013-08-14T21:45:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 355,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 15.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x63                                  [c
    decimal
             91   99
    datetime (2013-08-14T21:45:44)
    0000   0xac 0x2d 0x15 0x6e 0x0d                   .-.n.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x9c 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0x2c 0x00 0x70 0x78         ...,.px
    decimal
              0   81    0  100   60  100  156    0
              0    0    0   44    0  112  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 2.9, 'curve': 192},
 {'age': 26, 'amount': 0.3, 'curve': 208},
 {'age': 106, 'amount': 1.4, 'curve': 208},
 {'age': 136, 'amount': 1.4, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x74 0x66 0xc0 0x0c 0x1a 0xd0    \.tf....
    0008   0x38 0x6a 0xd0 0x38 0x88 0xd0              8j.8..
    decimal
             92   14  116  102  192   12   26  208
             56  106  208   56  136  208
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-08-14T21:45:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x2c 0x00    ..p.p.,.
    decimal
              1    0  112    0  112    0   44    0
    datetime (2013-08-14T21:45:44)
    0000   0xac 0x2d 0x55 0x6e 0x0d                   .-Un.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 BasalProfileStart 2013-08-15T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-15T00:00:00)
    0000   0x80 0x00 0x00 0x0f 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 9 ResultTotals (2000, 8, 0, 0, 13, 14) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x8c                   .....
    decimal
              7    0    0    4  140
    datetime ((2000, 8, 0, 0, 13, 14))
    0000   0x8e 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x8e 0x0d 0x05 0x00 0xc2 0x00 0x00    n.......
    0008   0x06 0x00 0x00 0x04 0x8c 0x02 0xdc 0x3f    .......?
    0010   0x01 0xb0 0x25 0x00 0x3a 0x00 0xc0 0x00    ..%.:...
    0018   0xf0 0x00 0x00 0x00 0x00 0x03 0x03 0x00    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0x63 0x00 0x00 0x00 0x00    ..dc....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  142   13    5    0  194    0    0
              6    0    0    4  140    2  220   63
              1  176   37    0   58    0  192    0
            240    0    0    0    0    3    3    0
              0    4    0    0    0    0    0    0
              0    0  100   99    0    0    0    0
              0    0    0

#### RECORD 10 Base (2015, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2015, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x0f                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 Base (2000, 0, 2, 16, 13, 15) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 15))
    0000   0x0f 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 13 CalBGForPH 2013-08-15T09:54:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-08-15T09:54:19)
    0000   0x93 0x36 0x29 0x0f 0x0d                   .6)..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 BolusWizard 2013-08-15T09:54:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-08-15T09:54:25)
    0000   0x99 0x36 0x09 0x0f 0x0d                   .6...
    body (15)
    hex
    0000   0x12 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x3c 0x00 0x00 0x00 0x00 0x3c 0x78         <....<x
    decimal
             18   80    0  120   60  100    0    0
             60    0    0    0    0   60  120
    HOUR BITS: [0, 0, 1]
#### RECORD 15 Bolus 2013-08-15T09:54:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2013-08-15T09:54:25)
    0000   0x99 0x36 0x49 0x0f 0x0d                   .6I..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 16 BasalProfileStart 2013-08-15T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-15T12:00:00)
    0000   0x80 0x00 0x0c 0x0f 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 17 CalBGForPH 2013-08-15T14:14:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2013-08-15T14:14:13)
    0000   0x8d 0x0e 0x2e 0x0f 0x0d                   .....
    body (0)

#### RECORD 18 BolusWizard 2013-08-15T14:14:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 216,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2013-08-15T14:14:16)
    0000   0x90 0x0e 0x0e 0x6f 0x0d                   ...o.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x40 0x00    .P.x<d@.
    0008   0x00 0x00 0x00 0x00 0x00 0x40 0x78         .....@x
    decimal
              0   80    0  120   60  100   64    0
              0    0    0    0    0   64  120
    DAY BITS: [0, 1, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 1.5, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x05 0xd0                   \.<..
    decimal
             92    5   60    5  208
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-08-15T14:14:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-08-15T14:14:16)
    0000   0x90 0x0e 0x4e 0x6f 0x0d                   ..No.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 21 BasalProfileStart 2013-08-16T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-16T00:00:00)
    0000   0x80 0x00 0x00 0x10 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 22 ResultTotals (2000, 8, 0, 0, 13, 15) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x58                   ....X
    decimal
              7    0    0    3   88
    datetime ((2000, 8, 0, 0, 13, 15))
    0000   0x8f 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x8f 0x0d 0x05 0x00 0xa2 0x00 0x00    n.......
    0008   0x02 0x00 0x00 0x03 0x58 0x02 0xdc 0x56    ....X..V
    0010   0x00 0x7c 0x0e 0x00 0x12 0x00 0x3c 0x00    .|....<.
    0018   0x40 0x00 0x00 0x00 0x00 0x01 0x01 0x00    @.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6b 0xd8 0x00 0x00 0x00 0x00    ..k.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  143   13    5    0  162    0    0
              2    0    0    3   88    2  220   86
              0  124   14    0   18    0   60    0
             64    0    0    0    0    1    1    0
              0    0    0    0    0    0    0    0
              0    0  107  216    0    0    0    0
              0    0    0

#### RECORD 23 Base (2000, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2000, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x10                   .....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 24 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 Base (2000, 0, 2, 16, 13, 16) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 16))
    0000   0x10 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 26 CalBGForPH 2013-08-16T11:12:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-08-16T11:12:51)
    0000   0xb3 0x0c 0x2b 0x10 0x0d                   ..+..
    body (0)

#### RECORD 27 BolusWizard 2013-08-16T11:13:00 head[2], body[15] op[0x5b]
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
    datetime (2013-08-16T11:13:00)
    0000   0x80 0x0d 0x0b 0x70 0x0d                   ...p.
    body (15)
    hex
    0000   0x11 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x38 0x00 0x00 0x00 0x00 0x38 0x78         8....8x
    decimal
             17   80    0  120   60  100    0    0
             56    0    0    0    0   56  120
    DAY BITS: [0, 1, 1]
#### RECORD 28 Bolus 2013-08-16T11:13:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-16T11:13:00)
    0000   0x80 0x0d 0x4b 0x70 0x0d                   ..Kp.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 29 BasalProfileStart 2013-08-16T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-16T12:00:00)
    0000   0x80 0x00 0x0c 0x10 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 30 CalBGForPH 2013-08-16T13:49:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-16T13:49:47)
    0000   0xaf 0x31 0x2d 0x10 0x0d                   .1-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 BolusWizard 2013-08-16T13:49:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-16T13:49:55)
    0000   0xb7 0x31 0x0d 0x10 0x0d                   .1...
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x08 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0    8    0   64  120
    HOUR BITS: [0, 0, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 156, 'amount': 1.4, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0x9c 0xc0                   \.8..
    decimal
             92    5   56  156  192
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-08-16T13:49:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x08 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    8    0
    datetime (2013-08-16T13:49:55)
    0000   0xb7 0x31 0x4d 0x10 0x0d                   .1M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 34 CalBGForPH 2013-08-16T14:02:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-08-16T14:02:40)
    0000   0xa8 0x02 0x2e 0x10 0x0d                   .....
    body (0)

#### RECORD 35 BolusWizard 2013-08-16T14:02:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 102,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
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
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-08-16T14:02:44)
    0000   0xac 0x02 0x0e 0x10 0x0d                   .....
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x44 0x00 0x28 0x78         (..D.(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0   68    0   40  120

#### RECORD 36 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 1.6, 'curve': 192},
 {'age': 169, 'amount': 1.4, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x13 0xc0 0x38 0xa9 0xc0    \.@..8..
    decimal
             92    8   64   19  192   56  169  192
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-08-16T14:02:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x44 0x00    ..(.(.D.
    decimal
              1    0   40    0   40    0   68    0
    datetime (2013-08-16T14:02:44)
    0000   0xac 0x02 0x4e 0x10 0x0d                   ..N..
    body (0)

#### RECORD 38 CalBGForPH 2013-08-16T16:45:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-16T16:45:03)
    0000   0x83 0x2d 0x30 0x10 0x0d                   .-0..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 BolusWizard 2013-08-16T16:45:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-16T16:45:09)
    0000   0x89 0x2d 0x10 0x10 0x0d                   .-...
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x44 0x00 0x00 0x04 0x00 0x44 0x78         D....Dx
    decimal
             21   80    0  120   60  100    0    0
             68    0    0    4    0   68  120
    HOUR BITS: [0, 0, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 0.6, 'curve': 192},
 {'age': 172, 'amount': 0.4, 'curve': 192},
 {'age': 182, 'amount': 1.6, 'curve': 192},
 {'age': 76, 'amount': 1.4, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0xa2 0xc0 0x10 0xac 0xc0    \.......
    0008   0x40 0xb6 0xc0 0x38 0x4c 0xd0              @..8L.
    decimal
             92   14   24  162  192   16  172  192
             64  182  192   56   76  208
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2013-08-16T16:45:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x04 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    4    0
    datetime (2013-08-16T16:45:09)
    0000   0x89 0x2d 0x50 0x10 0x0d                   .-P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 42 CalBGForPH 2013-08-16T17:44:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-08-16T17:44:45)
    0000   0xad 0x2c 0x31 0x10 0x0d                   .,1..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 BolusWizard 2013-08-16T17:44:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 102,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-08-16T17:44:55)
    0000   0xb7 0x2c 0x11 0x10 0x0d                   .,...
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x34 0x00 0x00 0x30 0x00 0x34 0x78         4..0.4x
    decimal
             13   80    0  100   60  100    0    0
             52    0    0   48    0   52  120
    HOUR BITS: [0, 0, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 1.7, 'curve': 192},
 {'age': 221, 'amount': 0.6, 'curve': 192},
 {'age': 231, 'amount': 0.4, 'curve': 192},
 {'age': 241, 'amount': 1.6, 'curve': 192},
 {'age': 135, 'amount': 1.4, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x44 0x3d 0xc0 0x18 0xdd 0xc0    \.D=....
    0008   0x10 0xe7 0xc0 0x40 0xf1 0xc0 0x38 0x87    ...@..8.
    0010   0xd0                                       .
    decimal
             92   17   68   61  192   24  221  192
             16  231  192   64  241  192   56  135
            208
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-08-16T17:44:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x30 0x00    ..4.4.0.
    decimal
              1    0   52    0   52    0   48    0
    datetime (2013-08-16T17:44:55)
    0000   0xb7 0x2c 0x51 0x10 0x0d                   .,Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 46 CalBGForPH 2013-08-16T17:57:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-16T17:57:51)
    0000   0xb3 0x39 0x31 0x10 0x0d                   .91..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 47 BolusWizard 2013-08-16T17:57:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 9.2,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-16T17:57:56)
    0000   0xb8 0x39 0x11 0x10 0x0d                   .9...
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x3c 0x00 0x00 0x5c 0x00 0x3c 0x78         <..\.<x
    decimal
             15   80    0  100   60  100    0    0
             60    0    0   92    0   60  120
    HOUR BITS: [0, 0, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 1.3, 'curve': 192},
 {'age': 74, 'amount': 1.7, 'curve': 192},
 {'age': 234, 'amount': 0.6, 'curve': 192},
 {'age': 244, 'amount': 0.4, 'curve': 192},
 {'age': 254, 'amount': 1.6, 'curve': 192},
 {'age': 148, 'amount': 1.4, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x34 0x0e 0xc0 0x44 0x4a 0xc0    \.4..DJ.
    0008   0x18 0xea 0xc0 0x10 0xf4 0xc0 0x40 0xfe    ......@.
    0010   0xc0 0x38 0x94 0xd0                        .8..
    decimal
             92   20   52   14  192   68   74  192
             24  234  192   16  244  192   64  254
            192   56  148  208
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-08-16T17:57:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x5c 0x00    ..<.<.\.
    decimal
              1    0   60    0   60    0   92    0
    datetime (2013-08-16T17:57:57)
    0000   0xb9 0x39 0x51 0x10 0x0d                   .9Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 CalBGForPH 2013-08-16T18:52:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-16T18:52:06)
    0000   0x86 0x34 0x32 0x10 0x0d                   .42..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 51 BolusWizard 2013-08-16T18:52:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 9.2,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-16T18:52:10)
    0000   0x8a 0x34 0x12 0x10 0x0d                   .4...
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x28 0x00 0x00 0x5c 0x00 0x28 0x78         (..\.(x
    decimal
             10   80    0  100   60  100    0    0
             40    0    0   92    0   40  120
    HOUR BITS: [0, 0, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 1.5, 'curve': 192},
 {'age': 69, 'amount': 1.3, 'curve': 192},
 {'age': 129, 'amount': 1.7, 'curve': 192},
 {'age': 33, 'amount': 0.6, 'curve': 208},
 {'age': 43, 'amount': 0.4, 'curve': 208},
 {'age': 53, 'amount': 1.6, 'curve': 208},
 {'age': 203, 'amount': 1.4, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x3c 0x3b 0xc0 0x34 0x45 0xc0    \.<;.4E.
    0008   0x44 0x81 0xc0 0x18 0x21 0xd0 0x10 0x2b    D...!..+
    0010   0xd0 0x40 0x35 0xd0 0x38 0xcb 0xd0         .@5.8..
    decimal
             92   23   60   59  192   52   69  192
             68  129  192   24   33  208   16   43
            208   64   53  208   56  203  208
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-08-16T18:52:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x5c 0x00    ..(.(.\.
    decimal
              1    0   40    0   40    0   92    0
    datetime (2013-08-16T18:52:10)
    0000   0x8a 0x34 0x52 0x10 0x0d                   .4R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 54 BolusWizard 2013-08-16T18:59:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 12.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-16T18:59:08)
    0000   0x88 0x3b 0x12 0x10 0x0d                   .;...
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x30 0x00 0x00 0x78 0x00 0x30 0x78         0..x.0x
    decimal
             12   80    0  100   60  100    0    0
             48    0    0  120    0   48  120
    HOUR BITS: [0, 0, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 1.0, 'curve': 192},
 {'age': 66, 'amount': 1.5, 'curve': 192},
 {'age': 76, 'amount': 1.3, 'curve': 192},
 {'age': 136, 'amount': 1.7, 'curve': 192},
 {'age': 40, 'amount': 0.6, 'curve': 208},
 {'age': 50, 'amount': 0.4, 'curve': 208},
 {'age': 60, 'amount': 1.6, 'curve': 208},
 {'age': 210, 'amount': 1.4, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x28 0x10 0xc0 0x3c 0x42 0xc0    \.(..<B.
    0008   0x34 0x4c 0xc0 0x44 0x88 0xc0 0x18 0x28    4L.D...(
    0010   0xd0 0x10 0x32 0xd0 0x40 0x3c 0xd0 0x38    ..2.@<.8
    0018   0xd2 0xd0                                  ..
    decimal
             92   26   40   16  192   60   66  192
             52   76  192   68  136  192   24   40
            208   16   50  208   64   60  208   56
            210  208
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-08-16T18:59:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x78 0x00    ..0.0.x.
    decimal
              1    0   48    0   48    0  120    0
    datetime (2013-08-16T18:59:08)
    0000   0x88 0x3b 0x52 0x10 0x0d                   .;R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 CalBGForPH 2013-08-16T19:31:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2013-08-16T19:31:24)
    0000   0x98 0x1f 0x33 0x10 0x0d                   ..3..
    body (0)

#### RECORD 58 BolusWizard 2013-08-16T19:31:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 215,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 12.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd7                                  [.
    decimal
             91  215
    datetime (2013-08-16T19:31:27)
    0000   0x9b 0x1f 0x13 0x10 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x3c 0x00    .P.d<d<.
    0008   0x00 0x00 0x00 0x78 0x00 0x00 0x78         ...x..x
    decimal
              0   80    0  100   60  100   60    0
              0    0    0  120    0    0  120

#### RECORD 59 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 1.2, 'curve': 192},
 {'age': 48, 'amount': 1.0, 'curve': 192},
 {'age': 98, 'amount': 1.5, 'curve': 192},
 {'age': 108, 'amount': 1.3, 'curve': 192},
 {'age': 168, 'amount': 1.7, 'curve': 192},
 {'age': 72, 'amount': 0.6, 'curve': 208},
 {'age': 82, 'amount': 0.4, 'curve': 208},
 {'age': 92, 'amount': 1.6, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x30 0x26 0xc0 0x28 0x30 0xc0    \.0&.(0.
    0008   0x3c 0x62 0xc0 0x34 0x6c 0xc0 0x44 0xa8    <b.4l.D.
    0010   0xc0 0x18 0x48 0xd0 0x10 0x52 0xd0 0x40    ..H..R.@
    0018   0x5c 0xd0                                  \.
    decimal
             92   26   48   38  192   40   48  192
             60   98  192   52  108  192   68  168
            192   24   72  208   16   82  208   64
             92  208
    datetime (unknown)

    body (0)

#### RECORD 60 CalBGForPH 2013-08-16T21:15:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-08-16T21:15:40)
    0000   0xa8 0x0f 0x35 0x10 0x0d                   ..5..
    body (0)

#### RECORD 61 BolusWizard 2013-08-16T21:15:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
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
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-08-16T21:15:46)
    0000   0xae 0x0f 0x15 0x70 0x0d                   ...p.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x50 0x00 0x00 0x0c 0x00 0x50 0x78         P....Px
    decimal
             20   80    0  100   60  100    0    0
             80    0    0   12    0   80  120
    DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 142, 'amount': 1.2, 'curve': 192},
 {'age': 152, 'amount': 1.0, 'curve': 192},
 {'age': 202, 'amount': 1.5, 'curve': 192},
 {'age': 212, 'amount': 1.3, 'curve': 192},
 {'age': 16, 'amount': 1.7, 'curve': 208},
 {'age': 176, 'amount': 0.6, 'curve': 208},
 {'age': 186, 'amount': 0.4, 'curve': 208},
 {'age': 196, 'amount': 1.6, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x30 0x8e 0xc0 0x28 0x98 0xc0    \.0..(..
    0008   0x3c 0xca 0xc0 0x34 0xd4 0xc0 0x44 0x10    <..4..D.
    0010   0xd0 0x18 0xb0 0xd0 0x10 0xba 0xd0 0x40    .......@
    0018   0xc4 0xd0                                  ..
    decimal
             92   26   48  142  192   40  152  192
             60  202  192   52  212  192   68   16
            208   24  176  208   16  186  208   64
            196  208
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2013-08-16T21:15:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x0c 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   12    0
    datetime (2013-08-16T21:15:46)
    0000   0xae 0x0f 0x55 0x70 0x0d                   ..Up.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 64 BasalProfileStart 2013-08-17T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-17T00:00:00)
    0000   0x80 0x00 0x00 0x11 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 65 ResultTotals (2000, 8, 0, 0, 13, 16) head[5], body[37] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd8                   .....
    decimal
              7    0    0    4  216
    datetime ((2000, 8, 0, 0, 13, 16))
    0000   0x90 0x0d 0x00 0x00 0x00                   .....
    body (37)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x9b 0xf2                   .....
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0  155  242

`end logs/ReadHistoryData-page-9.data: 66 records`
