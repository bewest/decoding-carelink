## START logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 1003, found 19 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x9a 0x4a                                  .J
##### DEBUG DECIMAL
            154   74
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 4.45, 'curve': 208},
 {'age': 147, 'amount': 0.75, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0xb2 0x89 0xd0 0x1e 0x93 0xd0    \.......
    decimal
             92    8  178  137  208   30  147  208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-08-24T11:06:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-24T11:06:44)
    0000   0xac 0x06 0x4b 0x18 0x0d                   ..K..
    body (0)

#### RECORD 2 CalBGForPH 2013-08-24T11:55:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-08-24T11:55:27)
    0000   0x9b 0x37 0x2b 0x18 0x0d                   .7+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 BolusWizard 2013-08-24T11:55:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-24T11:55:35)
    0000   0xa3 0x37 0x0b 0x18 0x0d                   .7...
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x34 0x00 0x00 0x2c 0x00 0x34 0x78         4..,.4x
    decimal
             16   80    0  120   60  100    0    0
             52    0    0   44    0   52  120
    HOUR BITS: [0, 0, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 1.4, 'curve': 192},
 {'age': 186, 'amount': 4.45, 'curve': 208},
 {'age': 196, 'amount': 0.75, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0x34 0xc0 0xb2 0xba 0xd0    \.84....
    0008   0x1e 0xc4 0xd0                             ...
    decimal
             92   11   56   52  192  178  186  208
             30  196  208
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-08-24T11:55:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x2c 0x00    ..4.4.,.
    decimal
              1    0   52    0   52    0   44    0
    datetime (2013-08-24T11:55:35)
    0000   0xa3 0x37 0x4b 0x18 0x0d                   .7K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 BasalProfileStart 2013-08-24T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-24T12:00:00)
    0000   0x80 0x00 0x0c 0x18 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 7 CalBGForPH 2013-08-24T14:31:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-08-24T14:31:49)
    0000   0xb1 0x1f 0x2e 0x18 0x0d                   .....
    body (0)

#### RECORD 8 BolusWizard 2013-08-24T14:31:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-08-24T14:31:59)
    0000   0xbb 0x1f 0x0e 0x18 0x0d                   .....
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x34 0x00 0x00 0x08 0x00 0x34 0x78         4....4x
    decimal
             16   80    0  120   60  100    0    0
             52    0    0    8    0   52  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 158, 'amount': 1.3, 'curve': 192},
 {'age': 208, 'amount': 1.4, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x9e 0xc0 0x38 0xd0 0xc0    \.4..8..
    decimal
             92    8   52  158  192   56  208  192
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-08-24T14:31:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x08 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    8    0
    datetime (2013-08-24T14:31:59)
    0000   0xbb 0x1f 0x4e 0x18 0x0d                   ..N..
    body (0)

#### RECORD 11 BolusWizard 2013-08-24T17:40:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-24T17:40:33)
    0000   0xa1 0x28 0x11 0x18 0x0d                   .(...
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x2c 0x00 0x00 0x00 0x00 0x2c 0x78         ,....,x
    decimal
             11   80    0  100   60  100    0    0
             44    0    0    0    0   44  120
    HOUR BITS: [0, 0, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 197, 'amount': 1.3, 'curve': 192},
 {'age': 91, 'amount': 1.3, 'curve': 208},
 {'age': 141, 'amount': 1.4, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0xc5 0xc0 0x34 0x5b 0xd0    \.4..4[.
    0008   0x38 0x8d 0xd0                             8..
    decimal
             92   11   52  197  192   52   91  208
             56  141  208
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-08-24T17:40:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x00 0x00    ..,.,...
    decimal
              1    0   44    0   44    0    0    0
    datetime (2013-08-24T17:40:33)
    0000   0xa1 0x28 0x51 0x18 0x0d                   .(Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 CalBGForPH 2013-08-24T18:35:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-08-24T18:35:51)
    0000   0xb3 0x23 0x32 0x18 0x0d                   .#2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 BolusWizard 2013-08-24T18:35:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-24T18:35:57)
    0000   0xb9 0x23 0x12 0x18 0x0d                   .#...
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x54 0x00 0x00 0x20 0x00 0x54 0x78         T.. .Tx
    decimal
             21   80    0  100   60  100    0    0
             84    0    0   32    0   84  120
    HOUR BITS: [0, 0, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 62, 'amount': 1.1, 'curve': 192},
 {'age': 252, 'amount': 1.3, 'curve': 192},
 {'age': 146, 'amount': 1.3, 'curve': 208},
 {'age': 196, 'amount': 1.4, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x2c 0x3e 0xc0 0x34 0xfc 0xc0    \.,>.4..
    0008   0x34 0x92 0xd0 0x38 0xc4 0xd0              4..8..
    decimal
             92   14   44   62  192   52  252  192
             52  146  208   56  196  208
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-08-24T18:35:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x20 0x00    ..T.T. .
    decimal
              1    0   84    0   84    0   32    0
    datetime (2013-08-24T18:35:57)
    0000   0xb9 0x23 0x52 0x18 0x0d                   .#R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 CalBGForPH 2013-08-24T20:41:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-08-24T20:41:31)
    0000   0x9f 0x29 0x34 0x18 0x0d                   .)4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 19 BolusWizard 2013-08-24T20:41:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 118,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
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
    0000   0x5b 0x76                                  [v
    decimal
             91  118
    datetime (2013-08-24T20:41:48)
    0000   0xb0 0x29 0x14 0x18 0x0d                   .)...
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0x14 0x00 0x38 0x78         8....8x
    decimal
             14   80    0  100   60  100    0    0
             56    0    0   20    0   56  120
    HOUR BITS: [0, 0, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 128, 'amount': 2.1, 'curve': 192},
 {'age': 188, 'amount': 1.1, 'curve': 192},
 {'age': 122, 'amount': 1.3, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x54 0x80 0xc0 0x2c 0xbc 0xc0    \.T..,..
    0008   0x34 0x7a 0xd0                             4z.
    decimal
             92   11   84  128  192   44  188  192
             52  122  208
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-08-24T20:41:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x14 0x00    ..8.8...
    decimal
              1    0   56    0   56    0   20    0
    datetime (2013-08-24T20:41:48)
    0000   0xb0 0x29 0x54 0x18 0x0d                   .)T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 CalBGForPH 2013-08-24T23:13:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 284}
```
    op hex (2)
    0000   0x0a 0x1c                                  ..
    decimal
             10   28
    datetime (2013-08-24T23:13:40)
    0000   0xa8 0x0d 0x37 0x18 0x8d                   ..7..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 23 BolusWizard 2013-08-24T23:13:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 284,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x1c                                  [.
    decimal
             91   28
    datetime (2013-08-24T23:13:42)
    0000   0xaa 0x0d 0x17 0x18 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x6c 0x00    .Q.d<dl.
    0008   0x00 0x00 0x00 0x08 0x00 0x64 0x78         .....dx
    decimal
              0   81    0  100   60  100  108    0
              0    0    0    8    0  100  120

#### RECORD 24 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 160, 'amount': 1.4, 'curve': 192},
 {'age': 24, 'amount': 2.1, 'curve': 208},
 {'age': 84, 'amount': 1.1, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0xa0 0xc0 0x54 0x18 0xd0    \.8..T..
    0008   0x2c 0x54 0xd0                             ,T.
    decimal
             92   11   56  160  192   84   24  208
             44   84  208
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-08-24T23:13:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x08 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    8    0
    datetime (2013-08-24T23:13:42)
    0000   0xaa 0x0d 0x57 0x18 0x0d                   ..W..
    body (0)

#### RECORD 26 BasalProfileStart 2013-08-25T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-25T00:00:00)
    0000   0x80 0x00 0x00 0x19 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 27 ResultTotals (2000, 8, 0, 0, 13, 24) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe2                   .....
    decimal
              7    0    0    4  226
    datetime ((2000, 8, 0, 0, 13, 24))
    0000   0x98 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x98 0x0d 0x05 0x00 0xb9 0x00 0x00    n.......
    0008   0x07 0x00 0x00 0x04 0xe2 0x02 0x56 0x30    ......V0
    0010   0x02 0x8c 0x34 0x00 0x5f 0x01 0x58 0x01    ..4._.X.
    0018   0x34 0x00 0x00 0x00 0x00 0x06 0x02 0x00    4.......
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6d 0xbb 0x00 0x00 0x00 0x00    ..m.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  152   13    5    0  185    0    0
              7    0    0    4  226    2   86   48
              2  140   52    0   95    1   88    1
             52    0    0    0    0    6    2    0
              0    4    0    0    0    0    0    0
              0    0  109  187    0    0    0    0
              0    0    0

#### RECORD 28 Base (2009, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2009, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x19                   .....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 29 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 Base (2000, 0, 2, 16, 13, 25) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 25))
    0000   0x19 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 31 BasalProfileStart 2013-08-25T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-25T12:00:00)
    0000   0x80 0x00 0x0c 0x19 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 32 CalBGForPH 2013-08-25T14:29:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2013-08-25T14:29:17)
    0000   0x91 0x1d 0x2e 0x19 0x8d                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 BolusWizard 2013-08-25T14:29:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 256,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-25T14:29:21)
    0000   0x95 0x1d 0x0e 0x79 0x0d                   ...y.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x58 0x00    .Q.x<dX.
    0008   0x00 0x00 0x00 0x00 0x00 0x58 0x78         .....Xx
    decimal
              0   81    0  120   60  100   88    0
              0    0    0    0    0   88  120
    DAY BITS: [0, 1, 1]
#### RECORD 34 Bolus 2013-08-25T14:29:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    0    0
    datetime (2013-08-25T14:29:21)
    0000   0x95 0x1d 0x4e 0x79 0x0d                   ..Ny.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 35 CalBGForPH 2013-08-25T21:54:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-08-25T21:54:16)
    0000   0x90 0x36 0x35 0x19 0x0d                   .65..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 BolusWizard 2013-08-25T21:54:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2013-08-25T21:54:23)
    0000   0x97 0x36 0x15 0x79 0x0d                   .6.y.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x1c 0x00    .P.d<d..
    0008   0x54 0x00 0x00 0x00 0x00 0x70 0x78         T....px
    decimal
             21   80    0  100   60  100   28    0
             84    0    0    0    0  112  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 195, 'amount': 2.2, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0xc3 0xd0                   \.X..
    decimal
             92    5   88  195  208
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-08-25T21:54:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x00 0x00    ..p.p...
    decimal
              1    0  112    0  112    0    0    0
    datetime (2013-08-25T21:54:23)
    0000   0x97 0x36 0x55 0x79 0x0d                   .6Uy.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 BasalProfileStart 2013-08-26T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-26T00:00:00)
    0000   0x80 0x00 0x00 0x1a 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 40 ResultTotals (2000, 8, 0, 0, 13, 25) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xa4                   .....
    decimal
              7    0    0    3  164
    datetime ((2000, 8, 0, 0, 13, 25))
    0000   0x99 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x99 0x0d 0x05 0x00 0xd2 0x00 0x00    n.......
    0008   0x02 0x00 0x00 0x03 0xa4 0x02 0xdc 0x4f    .......O
    0010   0x00 0xc8 0x15 0x00 0x15 0x00 0x00 0x00    ........
    0018   0x58 0x00 0x70 0x00 0x00 0x00 0x01 0x01    X.p.....
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0xa3 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00 0x00 0x00                             ...
    decimal
            110  153   13    5    0  210    0    0
              2    0    0    3  164    2  220   79
              0  200   21    0   21    0    0    0
             88    0  112    0    0    0    1    1
              0    4    0    0    0    0    0    0
              0    0  163    0    0    0    0    0
              0    0    0

#### RECORD 41 Base (2010, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2010, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x1a                   .....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 42 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 Base (2000, 0, 2, 16, 13, 26) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 26))
    0000   0x1a 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 44 CalBGForPH 2013-08-26T10:42:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-08-26T10:42:17)
    0000   0x91 0x2a 0x2a 0x1a 0x0d                   .**..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 BolusWizard 2013-08-26T10:42:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 110,
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
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-08-26T10:42:25)
    0000   0x99 0x2a 0x0a 0x1a 0x0d                   .*...
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0    0    0   64  120
    HOUR BITS: [0, 0, 1]
#### RECORD 46 Bolus 2013-08-26T10:42:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-08-26T10:42:25)
    0000   0x99 0x2a 0x4a 0x1a 0x0d                   .*J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 47 BasalProfileStart 2013-08-26T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-26T12:00:00)
    0000   0x80 0x00 0x0c 0x1a 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 48 CalBGForPH 2013-08-26T13:23:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2013-08-26T13:23:39)
    0000   0xa7 0x17 0x2d 0x1a 0x0d                   ..-..
    body (0)

#### RECORD 49 BolusWizard 2013-08-26T13:23:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 125,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
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
    0000   0x5b 0x7d                                  [}
    decimal
             91  125
    datetime (2013-08-26T13:23:46)
    0000   0xae 0x17 0x0d 0x1a 0x0d                   .....
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x08 0x00 0x30 0x78         0....0x
    decimal
             15   80    0  120   60  100    0    0
             48    0    0    8    0   48  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 160, 'amount': 0.75, 'curve': 192},
 {'age': 170, 'amount': 0.85, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x1e 0xa0 0xc0 0x22 0xaa 0xc0    \...."..
    decimal
             92    8   30  160  192   34  170  192
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-08-26T13:23:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x08 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    8    0
    datetime (2013-08-26T13:23:46)
    0000   0xae 0x17 0x4d 0x1a 0x0d                   ..M..
    body (0)

#### RECORD 52 CalBGForPH 2013-08-26T14:08:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-08-26T14:08:14)
    0000   0x8e 0x08 0x2e 0x1a 0x0d                   .....
    body (0)

#### RECORD 53 BolusWizard 2013-08-26T14:08:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
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
    datetime (2013-08-26T14:08:19)
    0000   0x93 0x08 0x0e 0x1a 0x0d                   .....
    body (15)
    hex
    0000   0x12 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x3c 0x00 0x00 0x28 0x00 0x3c 0x78         <..(.<x
    decimal
             18   80    0  120   60  100    0    0
             60    0    0   40    0   60  120

#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 1.2, 'curve': 192},
 {'age': 205, 'amount': 0.75, 'curve': 192},
 {'age': 215, 'amount': 0.85, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x2d 0xc0 0x1e 0xcd 0xc0    \.0-....
    0008   0x22 0xd7 0xc0                             "..
    decimal
             92   11   48   45  192   30  205  192
             34  215  192
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-08-26T14:08:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x28 0x00    ..<.<.(.
    decimal
              1    0   60    0   60    0   40    0
    datetime (2013-08-26T14:08:19)
    0000   0x93 0x08 0x4e 0x1a 0x0d                   ..N..
    body (0)

#### RECORD 56 CalBGForPH 2013-08-26T16:52:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 286}
```
    op hex (2)
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    datetime (2013-08-26T16:52:07)
    0000   0x87 0x34 0x30 0x1a 0x8d                   .40..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 57 BolusWizard 2013-08-26T16:52:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 286,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x1e                                  [.
    decimal
             91   30
    datetime (2013-08-26T16:52:09)
    0000   0x89 0x34 0x10 0x1a 0x0d                   .4...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x6c 0x00    .Q.x<dl.
    0008   0x00 0x00 0x00 0x04 0x00 0x68 0x78         .....hx
    decimal
              0   81    0  120   60  100  108    0
              0    0    0    4    0  104  120
    HOUR BITS: [0, 0, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 169, 'amount': 1.5, 'curve': 192},
 {'age': 209, 'amount': 1.2, 'curve': 192},
 {'age': 113, 'amount': 0.75, 'curve': 208},
 {'age': 123, 'amount': 0.85, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0xa9 0xc0 0x30 0xd1 0xc0    \.<..0..
    0008   0x1e 0x71 0xd0 0x22 0x7b 0xd0              .q."{.
    decimal
             92   14   60  169  192   48  209  192
             30  113  208   34  123  208
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-08-26T16:52:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x04 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    4    0
    datetime (2013-08-26T16:52:10)
    0000   0x8a 0x34 0x50 0x1a 0x0d                   .4P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 CalBGForPH 2013-08-26T20:42:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-08-26T20:42:21)
    0000   0x95 0x2a 0x34 0x1a 0x0d                   .*4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 BolusWizard 2013-08-26T20:42:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 9,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2013-08-26T20:42:32)
    0000   0xa0 0x2a 0x14 0x1a 0x0d                   .*...
    body (15)
    hex
    0000   0x09 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x78         $....$x
    decimal
              9   80    0  100   60  100    0    0
             36    0    0    0    0   36  120
    HOUR BITS: [0, 0, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 229, 'amount': 1.35, 'curve': 192},
 {'age': 239, 'amount': 1.25, 'curve': 192},
 {'age': 143, 'amount': 1.5, 'curve': 208},
 {'age': 183, 'amount': 1.2, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x36 0xe5 0xc0 0x32 0xef 0xc0    \.6..2..
    0008   0x3c 0x8f 0xd0 0x30 0xb7 0xd0              <..0..
    decimal
             92   14   54  229  192   50  239  192
             60  143  208   48  183  208
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2013-08-26T20:42:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x00 0x00    ..$.$...
    decimal
              1    0   36    0   36    0    0    0
    datetime (2013-08-26T20:42:32)
    0000   0xa0 0x2a 0x54 0x1a 0x0d                   .*T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 BasalProfileStart 2013-08-27T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-27T00:00:00)
    0000   0x80 0x00 0x00 0x1b 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 65 ResultTotals (2000, 8, 0, 0, 13, 26) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x14                   .....
    decimal
              7    0    0    4   20
    datetime ((2000, 8, 0, 0, 13, 26))
    0000   0x9a 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x9a 0x0d 0x05 0x00 0x94 0x00 0x00    n.......
    0008   0x05 0x00 0x00 0x04 0x14 0x02 0xdc 0x46    .......F
    0010   0x01 0x38 0x1e 0x00 0x3e 0x00 0xd0 0x00    .8..>...
    0018   0x68 0x00 0x00 0x00 0x00 0x04 0x01 0x00    h.......
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6b 0x1e 0x00 0x00 0x00 0x00    ..k.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  154   13    5    0  148    0    0
              5    0    0    4   20    2  220   70
              1   56   30    0   62    0  208    0
            104    0    0    0    0    4    1    0
              0    4    0    0    0    0    0    0
              0    0  107   30    0    0    0    0
              0    0    0

#### RECORD 66 Base (2011, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2011, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x1b                   .....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 67 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 68 Base (2000, 0, 2, 16, 13, 27) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 27))
    0000   0x1b 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 69 BasalProfileStart 2013-08-27T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-27T12:00:00)
    0000   0x80 0x00 0x0c 0x1b 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 70 CalBGForPH 2013-08-27T12:32:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-08-27T12:32:56)
    0000   0xb8 0x20 0x2c 0x1b 0x0d                   . ,..
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-5.data: 71 records`
