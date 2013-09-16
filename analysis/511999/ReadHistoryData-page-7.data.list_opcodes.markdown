## START logs/ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x7a 0x4a                                  zJ
##### DEBUG DECIMAL
            122   74
#### RECORD 0 Bolus 2013-08-19T20:37:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x00 0x00    ..|.|...
    decimal
              1    0  124    0  124    0    0    0
    datetime (2013-08-19T20:37:53)
    0000   0xb5 0x25 0x54 0x13 0x0d                   .%T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 CalBGForPH 2013-08-19T23:12:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 342}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-08-19T23:12:34)
    0000   0xa2 0x0c 0x37 0x13 0x8d                   ..7..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 BolusWizard 2013-08-19T23:12:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 342,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 14.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x56                                  [V
    decimal
             91   86
    datetime (2013-08-19T23:12:40)
    0000   0xa8 0x0c 0x17 0x13 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x94 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0x0c 0x00 0x88 0x78         ......x
    decimal
              0   81    0  100   60  100  148    0
              0    0    0   12    0  136  120

#### RECORD 3 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 159, 'amount': 3.1, 'curve': 192},
 {'age': 183, 'amount': 3.1, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x7c 0x9f 0xc0 0x7c 0xb7 0xd0    \.|..|..
    decimal
             92    8  124  159  192  124  183  208
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-08-19T23:12:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x0c 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   12    0
    datetime (2013-08-19T23:12:41)
    0000   0xa9 0x0c 0x57 0x13 0x0d                   ..W..
    body (0)

#### RECORD 5 BasalProfileStart 2013-08-20T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-20T00:00:00)
    0000   0x80 0x00 0x00 0x14 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 6 ResultTotals (2000, 8, 0, 0, 13, 19) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xfa                   .....
    decimal
              7    0    0    4  250
    datetime ((2000, 8, 0, 0, 13, 19))
    0000   0x93 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 7 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x93 0x0d 0x05 0x00 0xe4 0x00 0x00    n.......
    0008   0x05 0x00 0x00 0x04 0xfa 0x02 0xca 0x38    .......8
    0010   0x02 0x30 0x2c 0x00 0x45 0x00 0x2c 0x00    .0,.E.,.
    0018   0xf4 0x01 0x10 0x00 0x00 0x01 0x02 0x02    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6a 0x56 0x00 0x00 0x00         ..jV...
    decimal
            110  147   13    5    0  228    0    0
              5    0    0    4  250    2  202   56
              2   48   44    0   69    0   44    0
            244    1   16    0    0    1    2    2
              0    4    0    0    0    0    0    0
              0    0  106   86    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 8 BasalProfileStart 2013-08-20T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-20T04:00:00)
    0000   0x80 0x00 0x04 0x14 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 9 BasalProfileStart 2013-08-20T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-20T08:00:00)
    0000   0x80 0x00 0x08 0x14 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 10 CalBGForPH 2013-08-20T08:04:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-08-20T08:04:21)
    0000   0x95 0x04 0x28 0x14 0x0d                   ..(..
    body (0)

#### RECORD 11 BolusWizard 2013-08-20T08:04:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 194,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0xc2                                  [.
    decimal
             91  194
    datetime (2013-08-20T08:04:30)
    0000   0x9e 0x04 0x08 0x14 0x0d                   .....
    body (15)
    hex
    0000   0x12 0x50 0x00 0x78 0x3c 0x64 0x30 0x00    .P.x<d0.
    0008   0x3c 0x00 0x00 0x00 0x00 0x6c 0x78         <....lx
    decimal
             18   80    0  120   60  100   48    0
             60    0    0    0    0  108  120

#### RECORD 12 Bolus 2013-08-20T08:04:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-08-20T08:04:30)
    0000   0x9e 0x04 0x48 0x14 0x0d                   ..H..
    body (0)

#### RECORD 13 CalBGForPH 2013-08-20T11:29:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-20T11:29:14)
    0000   0x8e 0x1d 0x2b 0x14 0x0d                   ..+..
    body (0)

#### RECORD 14 BolusWizard 2013-08-20T11:29:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    datetime (2013-08-20T11:29:20)
    0000   0x94 0x1d 0x0b 0x14 0x0d                   .....
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0    0    0   64  120

#### RECORD 15 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 206, 'amount': 2.7, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0xce 0xc0                   \.l..
    decimal
             92    5  108  206  192
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-08-20T11:29:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-08-20T11:29:20)
    0000   0x94 0x1d 0x4b 0x14 0x0d                   ..K..
    body (0)

#### RECORD 17 BasalProfileStart 2013-08-20T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-20T12:00:00)
    0000   0x80 0x00 0x0c 0x14 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 18 CalBGForPH 2013-08-20T14:48:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-20T14:48:49)
    0000   0xb1 0x30 0x2e 0x14 0x0d                   .0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 19 BolusWizard 2013-08-20T14:48:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-20T14:48:54)
    0000   0xb6 0x30 0x0e 0x14 0x0d                   .0...
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x78         0....0x
    decimal
             15   80    0  120   60  100    0    0
             48    0    0    0    0   48  120
    HOUR BITS: [0, 0, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 205, 'amount': 1.6, 'curve': 192},
 {'age': 149, 'amount': 2.7, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0xcd 0xc0 0x6c 0x95 0xd0    \.@..l..
    decimal
             92    8   64  205  192  108  149  208
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-08-20T14:48:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-08-20T14:48:54)
    0000   0xb6 0x30 0x4e 0x14 0x0d                   .0N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 CalBGForPH 2013-08-20T15:13:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-08-20T15:13:43)
    0000   0xab 0x0d 0x2f 0x14 0x0d                   ../..
    body (0)

#### RECORD 23 BolusWizard 2013-08-20T15:13:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 118,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
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
    0000   0x5b 0x76                                  [v
    decimal
             91  118
    datetime (2013-08-20T15:13:50)
    0000   0xb2 0x0d 0x0f 0x14 0x0d                   .....
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x2c 0x00 0x40 0x78         @..,.@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0   44    0   64  120

#### RECORD 24 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.2, 'curve': 192},
 {'age': 230, 'amount': 1.6, 'curve': 192},
 {'age': 174, 'amount': 2.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x1e 0xc0 0x40 0xe6 0xc0    \.0..@..
    0008   0x6c 0xae 0xd0                             l..
    decimal
             92   11   48   30  192   64  230  192
            108  174  208
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-08-20T15:13:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x2c 0x00    ..@.@.,.
    decimal
              1    0   64    0   64    0   44    0
    datetime (2013-08-20T15:13:50)
    0000   0xb2 0x0d 0x4f 0x14 0x0d                   ..O..
    body (0)

#### RECORD 26 CalBGForPH 2013-08-20T17:41:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-08-20T17:41:41)
    0000   0xa9 0x29 0x31 0x14 0x0d                   .)1..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 27 BolusWizard 2013-08-20T17:41:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 105,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
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
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-08-20T17:41:46)
    0000   0xae 0x29 0x11 0x14 0x0d                   .)...
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x3c 0x00 0x00 0x0c 0x00 0x3c 0x78         <....<x
    decimal
             15   80    0  100   60  100    0    0
             60    0    0   12    0   60  120
    HOUR BITS: [0, 0, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 148, 'amount': 1.6, 'curve': 192},
 {'age': 178, 'amount': 1.2, 'curve': 192},
 {'age': 122, 'amount': 1.6, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x94 0xc0 0x30 0xb2 0xc0    \.@..0..
    0008   0x40 0x7a 0xd0                             @z.
    decimal
             92   11   64  148  192   48  178  192
             64  122  208
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-08-20T17:41:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x0c 0x00    ..<.<...
    decimal
              1    0   60    0   60    0   12    0
    datetime (2013-08-20T17:41:46)
    0000   0xae 0x29 0x51 0x14 0x0d                   .)Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 CalBGForPH 2013-08-20T18:35:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 162}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2013-08-20T18:35:37)
    0000   0xa5 0x23 0x32 0x14 0x0d                   .#2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 BolusWizard 2013-08-20T18:35:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 162,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2013-08-20T18:35:42)
    0000   0xaa 0x23 0x12 0x14 0x0d                   .#...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x1c 0x00    .P.d<d..
    0008   0x00 0x00 0x00 0x2c 0x00 0x00 0x78         ...,..x
    decimal
              0   80    0  100   60  100   28    0
              0    0    0   44    0    0  120
    HOUR BITS: [0, 0, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 62, 'amount': 1.5, 'curve': 192},
 {'age': 202, 'amount': 1.6, 'curve': 192},
 {'age': 232, 'amount': 1.2, 'curve': 192},
 {'age': 176, 'amount': 1.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0x3e 0xc0 0x40 0xca 0xc0    \.<>.@..
    0008   0x30 0xe8 0xc0 0x40 0xb0 0xd0              0..@..
    decimal
             92   14   60   62  192   64  202  192
             48  232  192   64  176  208
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-08-20T18:35:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x2c 0x00    ..P.P.,.
    decimal
              1    0   80    0   80    0   44    0
    datetime (2013-08-20T18:35:43)
    0000   0xab 0x23 0x52 0x14 0x0d                   .#R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 34 CalBGForPH 2013-08-20T19:06:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-08-20T19:06:17)
    0000   0x91 0x06 0x33 0x14 0x0d                   ..3..
    body (0)

#### RECORD 35 BolusWizard 2013-08-20T19:06:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.0,
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
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-08-20T19:06:53)
    0000   0xb5 0x06 0x13 0x14 0x0d                   .....
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x34 0x00 0x00 0x64 0x00 0x34 0x78         4..d.4x
    decimal
             13   80    0  100   60  100    0    0
             52    0    0  100    0   52  120

#### RECORD 36 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 2.0, 'curve': 192},
 {'age': 93, 'amount': 1.5, 'curve': 192},
 {'age': 233, 'amount': 1.6, 'curve': 192},
 {'age': 7, 'amount': 1.2, 'curve': 208},
 {'age': 207, 'amount': 1.6, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x21 0xc0 0x3c 0x5d 0xc0    \.P!.<].
    0008   0x40 0xe9 0xc0 0x30 0x07 0xd0 0x40 0xcf    @..0..@.
    0010   0xd0                                       .
    decimal
             92   17   80   33  192   60   93  192
             64  233  192   48    7  208   64  207
            208
    datetime (unknown)

    body (0)

#### RECORD 37 CalBGForPH 2013-08-20T21:54:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 158}
```
    op hex (2)
    0000   0x0a 0x9e                                  ..
    decimal
             10  158
    datetime (2013-08-20T21:54:10)
    0000   0x8a 0x36 0x35 0x14 0x0d                   .65..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 38 BolusWizard 2013-08-20T21:54:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 158,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x9e                                  [.
    decimal
             91  158
    datetime (2013-08-20T21:54:17)
    0000   0x91 0x36 0x15 0x14 0x0d                   .6...
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x18 0x00    .P.d<d..
    0008   0x58 0x00 0x00 0x00 0x00 0x70 0x78         X....px
    decimal
             22   80    0  100   60  100   24    0
             88    0    0    0    0  112  120
    HOUR BITS: [0, 0, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 201, 'amount': 2.0, 'curve': 192},
 {'age': 5, 'amount': 1.5, 'curve': 208},
 {'age': 145, 'amount': 1.6, 'curve': 208},
 {'age': 175, 'amount': 1.2, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0xc9 0xc0 0x3c 0x05 0xd0    \.P..<..
    0008   0x40 0x91 0xd0 0x30 0xaf 0xd0              @..0..
    decimal
             92   14   80  201  192   60    5  208
             64  145  208   48  175  208
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-08-20T21:54:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x00 0x00    ..p.p...
    decimal
              1    0  112    0  112    0    0    0
    datetime (2013-08-20T21:54:17)
    0000   0x91 0x36 0x55 0x14 0x0d                   .6U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 BasalProfileStart 2013-08-21T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-21T00:00:00)
    0000   0x80 0x00 0x00 0x15 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 42 ResultTotals (2000, 8, 0, 0, 13, 20) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf4                   .....
    decimal
              7    0    0    4  244
    datetime ((2000, 8, 0, 0, 13, 20))
    0000   0x94 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 43 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x94 0x0d 0x05 0x00 0x84 0x00 0x00    n.......
    0008   0x08 0x00 0x00 0x04 0xf4 0x02 0xdc 0x3a    .......:
    0010   0x02 0x18 0x2a 0x00 0x6e 0x00 0xec 0x00    ..*.n...
    0018   0x50 0x00 0xdc 0x00 0x00 0x04 0x01 0x02    P.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0xc2 0x00 0x00 0x00         ..d....
    decimal
            110  148   13    5    0  132    0    0
              8    0    0    4  244    2  220   58
              2   24   42    0  110    0  236    0
             80    0  220    0    0    4    1    2
              0    0    0    0    0    0    0    0
              0    0  100  194    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 44 BasalProfileStart 2013-08-21T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-21T04:00:00)
    0000   0x80 0x00 0x04 0x15 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 45 BasalProfileStart 2013-08-21T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-21T08:00:00)
    0000   0x80 0x00 0x08 0x15 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 46 CalBGForPH 2013-08-21T09:14:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 241}
```
    op hex (2)
    0000   0x0a 0xf1                                  ..
    decimal
             10  241
    datetime (2013-08-21T09:14:14)
    0000   0x8e 0x0e 0x29 0x15 0x0d                   ..)..
    body (0)

#### RECORD 47 BolusWizard 2013-08-21T09:14:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 241,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf1                                  [.
    decimal
             91  241
    datetime (2013-08-21T09:14:17)
    0000   0x91 0x0e 0x09 0x15 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x50 0x00    .P.x<dP.
    0008   0x00 0x00 0x00 0x00 0x00 0x50 0x78         .....Px
    decimal
              0   80    0  120   60  100   80    0
              0    0    0    0    0   80  120

#### RECORD 48 Bolus 2013-08-21T09:14:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-08-21T09:14:17)
    0000   0x91 0x0e 0x49 0x15 0x0d                   ..I..
    body (0)

#### RECORD 49 CalBGForPH 2013-08-21T09:29:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 226}
```
    op hex (2)
    0000   0x0a 0xe2                                  ..
    decimal
             10  226
    datetime (2013-08-21T09:29:01)
    0000   0x81 0x1d 0x29 0x15 0x0d                   ..)..
    body (0)

#### RECORD 50 BolusWizard 2013-08-21T09:29:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 226,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.0,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0xe2                                  [.
    decimal
             91  226
    datetime (2013-08-21T09:29:06)
    0000   0x86 0x1d 0x09 0x15 0x0d                   .....
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x44 0x00    .P.x<dD.
    0008   0x34 0x00 0x00 0x50 0x00 0x34 0x78         4..P.4x
    decimal
             16   80    0  120   60  100   68    0
             52    0    0   80    0   52  120

#### RECORD 51 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 2.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x10 0xc0                   \.P..
    decimal
             92    5   80   16  192
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-08-21T09:29:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x50 0x00    ..4.4.P.
    decimal
              1    0   52    0   52    0   80    0
    datetime (2013-08-21T09:29:07)
    0000   0x87 0x1d 0x49 0x15 0x0d                   ..I..
    body (0)

#### RECORD 53 BasalProfileStart 2013-08-21T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-21T12:00:00)
    0000   0x80 0x00 0x0c 0x15 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 54 CalBGForPH 2013-08-21T12:31:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2013-08-21T12:31:10)
    0000   0x8a 0x1f 0x2c 0x15 0x0d                   ..,..
    body (0)

#### RECORD 55 BolusWizard 2013-08-21T12:31:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 97,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 25.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x61                                  [a
    decimal
             91   97
    datetime (2013-08-21T12:31:20)
    0000   0x94 0x1f 0x0c 0x15 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0xfc 0x00    .P.x<d..
    0008   0x44 0xf8 0x00 0x00 0x00 0x40 0x78         D....@x
    decimal
             21   80    0  120   60  100  252    0
             68  248    0    0    0   64  120

#### RECORD 56 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 188, 'amount': 1.3, 'curve': 192},
 {'age': 198, 'amount': 2.0, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0xbc 0xc0 0x50 0xc6 0xc0    \.4..P..
    decimal
             92    8   52  188  192   80  198  192
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2013-08-21T12:31:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-08-21T12:31:20)
    0000   0x94 0x1f 0x4c 0x15 0x0d                   ..L..
    body (0)

#### RECORD 58 CalBGForPH 2013-08-21T13:08:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 150}
```
    op hex (2)
    0000   0x0a 0x96                                  ..
    decimal
             10  150
    datetime (2013-08-21T13:08:48)
    0000   0xb0 0x08 0x2d 0x15 0x0d                   ..-..
    body (0)

#### RECORD 59 BolusWizard 2013-08-21T13:09:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 150,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 36,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x96                                  [.
    decimal
             91  150
    datetime (2013-08-21T13:09:08)
    0000   0x88 0x09 0x0d 0x15 0x0d                   .....
    body (15)
    hex
    0000   0x24 0x50 0x00 0x78 0x3c 0x64 0x14 0x00    $P.x<d..
    0008   0x78 0x00 0x00 0x34 0x00 0x78 0x78         x..4.xx
    decimal
             36   80    0  120   60  100   20    0
            120    0    0   52    0  120  120

#### RECORD 60 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 1.6, 'curve': 192},
 {'age': 226, 'amount': 1.3, 'curve': 192},
 {'age': 236, 'amount': 2.0, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x2e 0xc0 0x34 0xe2 0xc0    \.@..4..
    0008   0x50 0xec 0xc0                             P..
    decimal
             92   11   64   46  192   52  226  192
             80  236  192
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-08-21T13:09:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x34 0x00    ..x.x.4.
    decimal
              1    0  120    0  120    0   52    0
    datetime (2013-08-21T13:09:08)
    0000   0x88 0x09 0x4d 0x15 0x0d                   ..M..
    body (0)

#### RECORD 62 CalBGForPH 2013-08-21T14:46:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-08-21T14:46:24)
    0000   0x98 0x2e 0x2e 0x15 0x0d                   .....
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 BolusWizard 2013-08-21T14:46:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 116,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
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
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-08-21T14:46:33)
    0000   0xa1 0x2e 0x0e 0x15 0x0d                   .....
    body (15)
    hex
    0000   0x1a 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x54 0x00 0x00 0x38 0x00 0x54 0x78         T..8.Tx
    decimal
             26   80    0  120   60  100    0    0
             84    0    0   56    0   84  120
    HOUR BITS: [0, 0, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 3.0, 'curve': 192},
 {'age': 143, 'amount': 1.6, 'curve': 192},
 {'age': 67, 'amount': 1.3, 'curve': 208},
 {'age': 77, 'amount': 2.0, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0x67 0xc0 0x40 0x8f 0xc0    \.xg.@..
    0008   0x34 0x43 0xd0 0x50 0x4d 0xd0              4C.PM.
    decimal
             92   14  120  103  192   64  143  192
             52   67  208   80   77  208
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-08-21T14:46:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x38 0x00    ..8.8.8.
    decimal
              1    0   56    0   56    0   56    0
    datetime (2013-08-21T14:46:33)
    0000   0xa1 0x2e 0x4e 0x15 0x0d                   ..N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 66 CalBGForPH 2013-08-21T18:32:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-08-21T18:32:19)
    0000   0x93 0x20 0x32 0x15 0x0d                   . 2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 67 BolusWizard 2013-08-21T18:32:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
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
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-08-21T18:32:27)
    0000   0x9b 0x20 0x12 0x15 0x0d                   . ...
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x3c 0x00 0x00 0x00 0x00 0x3c 0x78         <....<x
    decimal
             15   80    0  100   60  100    0    0
             60    0    0    0    0   60  120
    HOUR BITS: [0, 0, 1]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 229, 'amount': 1.4, 'curve': 192},
 {'age': 73, 'amount': 3.0, 'curve': 208},
 {'age': 113, 'amount': 1.6, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0xe5 0xc0 0x78 0x49 0xd0    \.8..xI.
    0008   0x40 0x71 0xd0                             @q.
    decimal
             92   11   56  229  192  120   73  208
             64  113  208
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-08-21T18:32:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2013-08-21T18:32:27)
    0000   0x9b 0x20 0x52 0x15 0x0d                   . R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 CalBGForPH 2013-08-21T19:16:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 294}
```
    op hex (2)
    0000   0x0a 0x26                                  .&
    decimal
             10   38
    datetime (2013-08-21T19:16:50)
    0000   0xb2 0x10 0x33 0x15 0x8d                   ..3..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 71 BolusWizard 2013-08-21T19:16:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 294,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
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
    0000   0x5b 0x26                                  [&
    decimal
             91   38
    datetime (2013-08-21T19:16:53)
    0000   0xb5 0x10 0x13 0x15 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x74 0x00    .Q.d<dt.
    0008   0x00 0x00 0x00 0x30 0x00 0x44 0x78         ...0.Dx
    decimal
              0   81    0  100   60  100  116    0
              0    0    0   48    0   68  120

#### RECORD 72 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 0.65, 'curve': 192},
 {'age': 53, 'amount': 0.85, 'curve': 192},
 {'age': 17, 'amount': 1.4, 'curve': 208},
 {'age': 117, 'amount': 3.0, 'curve': 208},
 {'age': 157, 'amount': 1.6, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x1a 0x2b 0xc0 0x22 0x35 0xc0    \..+."5.
    0008   0x38 0x11 0xd0 0x78 0x75 0xd0 0x40 0x9d    8..xu.@.
    0010   0xd0                                       .
    decimal
             92   17   26   43  192   34   53  192
             56   17  208  120  117  208   64  157
            208
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-7.data: 73 records`
