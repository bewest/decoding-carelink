## START logs/ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 990, found 32 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x42 0x5b                                  B[
##### DEBUG DECIMAL
             66   91
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x9e 0x0d 0x05 0x00 0xc0 0x00 0x00    n.......
    0008   0x09 0x00 0x00 0x06 0x54 0x04 0x00 0x3f    ....T..?
    0010   0x02 0x54 0x25 0x00 0x34 0x00 0xa8 0x01    .T%.4...
    0018   0xac 0x00 0x00 0x00 0x00 0x03 0x05 0x00    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x68 0x82 0x00 0x00 0x00         ..h....
    decimal
            110  158   13    5    0  192    0    0
              9    0    0    6   84    4    0   63
              2   84   37    0   52    0  168    1
            172    0    0    0    0    3    5    0
              0    4    0    0    0    0    0    0
              0    0  104  130    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 BasalProfileStart 2013-08-31T01:03:47 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-31T01:03:47)
    0000   0xaf 0x03 0x21 0x1f 0x0d                   ..!..
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 2 CalBGForPH 2013-08-31T08:45:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-31T08:45:29)
    0000   0x9d 0x2d 0x28 0x1f 0x0d                   .-(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalBGForPH 2013-08-31T08:45:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-08-31T08:45:35)
    0000   0xa3 0x2d 0x28 0x1f 0x0d                   .-(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BolusWizard 2013-08-31T08:45:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 24.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-08-31T08:45:46)
    0000   0xae 0x2d 0x08 0x1f 0x0d                   .-...
    body (15)
    hex
    0000   0x18 0x50 0x00 0x78 0x3c 0x64 0xf0 0x00    .P.x<d..
    0008   0x50 0xf8 0x00 0x00 0x00 0x40 0x78         P....@x
    decimal
             24   80    0  120   60  100  240    0
             80  248    0    0    0   64  120
    HOUR BITS: [0, 0, 1]
#### RECORD 5 Bolus 2013-08-31T08:45:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-08-31T08:45:46)
    0000   0xae 0x2d 0x48 0x1f 0x0d                   .-H..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 CalBGForPH 2013-08-31T10:25:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 248}
```
    op hex (2)
    0000   0x0a 0xf8                                  ..
    decimal
             10  248
    datetime (2013-08-31T10:25:25)
    0000   0x99 0x19 0x2a 0x1f 0x0d                   ..*..
    body (0)

#### RECORD 7 BolusWizard 2013-08-31T10:25:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 248,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf8                                  [.
    decimal
             91  248
    datetime (2013-08-31T10:25:27)
    0000   0x9b 0x19 0x0a 0x1f 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x54 0x00    .P.x<dT.
    0008   0x00 0x00 0x00 0x18 0x00 0x3c 0x78         .....<x
    decimal
              0   80    0  120   60  100   84    0
              0    0    0   24    0   60  120

#### RECORD 8 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 99, 'amount': 1.25, 'curve': 192},
 {'age': 109, 'amount': 0.35, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x32 0x63 0xc0 0x0e 0x6d 0xc0    \.2c..m.
    decimal
             92    8   50   99  192   14  109  192
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-08-31T10:25:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x18 0x00    ..<.<...
    decimal
              1    0   60    0   60    0   24    0
    datetime (2013-08-31T10:25:28)
    0000   0x9c 0x19 0x4a 0x1f 0x0d                   ..J..
    body (0)

#### RECORD 10 CalBGForPH 2013-08-31T12:43:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-08-31T12:43:42)
    0000   0xaa 0x2b 0x2c 0x1f 0x0d                   .+,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 BolusWizard 2013-08-31T12:43:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-08-31T12:43:53)
    0000   0xb5 0x2b 0x0c 0x1f 0x0d                   .+...
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x64 0x00 0x00 0x0c 0x00 0x64 0x78         d....dx
    decimal
             30   80    0  120   60  100    0    0
            100    0    0   12    0  100  120
    HOUR BITS: [0, 0, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 0.7, 'curve': 192},
 {'age': 147, 'amount': 0.8, 'curve': 192},
 {'age': 237, 'amount': 1.25, 'curve': 192},
 {'age': 247, 'amount': 0.35, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1c 0x89 0xc0 0x20 0x93 0xc0    \.... ..
    0008   0x32 0xed 0xc0 0x0e 0xf7 0xc0              2.....
    decimal
             92   14   28  137  192   32  147  192
             50  237  192   14  247  192
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-08-31T12:43:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x0c 0x00    ..d.d...
    decimal
              1    0  100    0  100    0   12    0
    datetime (2013-08-31T12:43:53)
    0000   0xb5 0x2b 0x4c 0x1f 0x0d                   .+L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 CalBGForPH 2013-08-31T15:01:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 295}
```
    op hex (2)
    0000   0x0a 0x27                                  .'
    decimal
             10   39
    datetime (2013-08-31T15:01:17)
    0000   0x91 0x01 0x2f 0x1f 0x8d                   ../..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 BolusWizard 2013-08-31T15:01:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 295,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 11.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x27                                  ['
    decimal
             91   39
    datetime (2013-08-31T15:01:20)
    0000   0x94 0x01 0x0f 0x1f 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x74 0x00    .Q.x<dt.
    0008   0x00 0x00 0x00 0x10 0x00 0x64 0x78         .....dx
    decimal
              0   81    0  120   60  100  116    0
              0    0    0   16    0  100  120

#### RECORD 16 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 145, 'amount': 2.5, 'curve': 192},
 {'age': 19, 'amount': 0.7, 'curve': 208},
 {'age': 29, 'amount': 0.8, 'curve': 208},
 {'age': 119, 'amount': 1.25, 'curve': 208},
 {'age': 129, 'amount': 0.35, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x64 0x91 0xc0 0x1c 0x13 0xd0    \.d.....
    0008   0x20 0x1d 0xd0 0x32 0x77 0xd0 0x0e 0x81     ..2w...
    0010   0xd0                                       .
    decimal
             92   17  100  145  192   28   19  208
             32   29  208   50  119  208   14  129
            208
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-08-31T15:01:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x10 0x00    ..d.d...
    decimal
              1    0  100    0  100    0   16    0
    datetime (2013-08-31T15:01:20)
    0000   0x94 0x01 0x4f 0x1f 0x0d                   ..O..
    body (0)

#### RECORD 18 CalBGForPH 2013-08-31T15:31:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2013-08-31T15:31:59)
    0000   0xbb 0x1f 0x2f 0x1f 0x0d                   ../..
    body (0)

#### RECORD 19 BolusWizard 2013-08-31T15:32:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 198,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 9.6,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0xc6                                  [.
    decimal
             91  198
    datetime (2013-08-31T15:32:28)
    0000   0x9c 0x20 0x0f 0x1f 0x0d                   . ...
    body (15)
    hex
    0000   0x16 0x50 0x00 0x78 0x3c 0x64 0x34 0x00    .P.x<d4.
    0008   0x48 0x00 0x00 0x60 0x00 0x48 0x78         H..`.Hx
    decimal
             22   80    0  120   60  100   52    0
             72    0    0   96    0   72  120
    HOUR BITS: [0, 0, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 2.5, 'curve': 192},
 {'age': 176, 'amount': 2.5, 'curve': 192},
 {'age': 50, 'amount': 0.7, 'curve': 208},
 {'age': 60, 'amount': 0.8, 'curve': 208},
 {'age': 150, 'amount': 1.25, 'curve': 208},
 {'age': 160, 'amount': 0.35, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x64 0x24 0xc0 0x64 0xb0 0xc0    \.d$.d..
    0008   0x1c 0x32 0xd0 0x20 0x3c 0xd0 0x32 0x96    .2. <.2.
    0010   0xd0 0x0e 0xa0 0xd0                        ....
    decimal
             92   20  100   36  192  100  176  192
             28   50  208   32   60  208   50  150
            208   14  160  208
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-08-31T15:32:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x60 0x00    ..H.H.`.
    decimal
              1    0   72    0   72    0   96    0
    datetime (2013-08-31T15:32:28)
    0000   0x9c 0x20 0x4f 0x1f 0x0d                   . O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 CalBGForPH 2013-08-31T18:29:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 241}
```
    op hex (2)
    0000   0x0a 0xf1                                  ..
    decimal
             10  241
    datetime (2013-08-31T18:29:48)
    0000   0xb0 0x1d 0x32 0x1f 0x0d                   ..2..
    body (0)

#### RECORD 23 BolusWizard 2013-08-31T18:29:54 head[2], body[15] op[0x5b]
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
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf1                                  [.
    decimal
             91  241
    datetime (2013-08-31T18:29:54)
    0000   0xb6 0x1d 0x12 0x1f 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x50 0x00    .P.d<dP.
    0008   0x00 0x00 0x00 0x00 0x00 0x50 0x78         .....Px
    decimal
              0   80    0  100   60  100   80    0
              0    0    0    0    0   80  120

#### RECORD 24 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 183, 'amount': 1.8, 'curve': 192},
 {'age': 213, 'amount': 2.5, 'curve': 192},
 {'age': 97, 'amount': 2.5, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0xb7 0xc0 0x64 0xd5 0xc0    \.H..d..
    0008   0x64 0x61 0xd0                             da.
    decimal
             92   11   72  183  192  100  213  192
            100   97  208
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-08-31T18:29:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-08-31T18:29:55)
    0000   0xb7 0x1d 0x52 0x1f 0x0d                   ..R..
    body (0)

#### RECORD 26 CalBGForPH 2013-08-31T18:59:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-08-31T18:59:50)
    0000   0xb2 0x3b 0x32 0x1f 0x0d                   .;2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 27 BolusWizard 2013-08-31T18:59:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 104,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.2,
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
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-08-31T18:59:55)
    0000   0xb7 0x3b 0x12 0x1f 0x0d                   .;...
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0x48 0x00 0x38 0x78         8..H.8x
    decimal
             14   80    0  100   60  100    0    0
             56    0    0   72    0   56  120
    HOUR BITS: [0, 0, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 2.0, 'curve': 192},
 {'age': 213, 'amount': 1.8, 'curve': 192},
 {'age': 243, 'amount': 2.5, 'curve': 192},
 {'age': 127, 'amount': 2.5, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x21 0xc0 0x48 0xd5 0xc0    \.P!.H..
    0008   0x64 0xf3 0xc0 0x64 0x7f 0xd0              d..d..
    decimal
             92   14   80   33  192   72  213  192
            100  243  192  100  127  208
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-08-31T18:59:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x48 0x00    ..8.8.H.
    decimal
              1    0   56    0   56    0   72    0
    datetime (2013-08-31T18:59:55)
    0000   0xb7 0x3b 0x52 0x1f 0x0d                   .;R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 ResultTotals (2000, 8, 0, 0, 13, 31) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime ((2000, 8, 0, 0, 13, 31))
    0000   0x9f 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 31 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x9f 0x0d 0x05 0x00 0xad 0x00 0x00    n.......
    0008   0x08 0x00 0x00 0x04 0xd2 0x02 0xbe 0x39    .......9
    0010   0x02 0x14 0x2b 0x00 0x5a 0x01 0x24 0x00    ..+.Z.$.
    0018   0xf0 0x00 0x00 0x00 0x00 0x04 0x03 0x00    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x4b 0x27 0x00 0x00 0x00         ..K'...
    decimal
            110  159   13    5    0  173    0    0
              8    0    0    4  210    2  190   57
              2   20   43    0   90    1   36    0
            240    0    0    0    0    4    3    0
              0    4    0    0    0    0    0    0
              0    0   75   39    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 32 CalBGForPH 2013-09-01T09:42:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 279}
```
    op hex (2)
    0000   0x0a 0x17                                  ..
    decimal
             10   23
    datetime (2013-09-01T09:42:08)
    0000   0x88 0x6a 0x29 0x01 0x8d                   .j)..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 BolusWizard 2013-09-01T09:42:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 279,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x17                                  [.
    decimal
             91   23
    datetime (2013-09-01T09:42:20)
    0000   0x94 0x6a 0x09 0x01 0x0d                   .j...
    body (15)
    hex
    0000   0x1d 0x51 0x00 0x78 0x3c 0x64 0x68 0x00    .Q.x<dh.
    0008   0x60 0x00 0x00 0x00 0x00 0xc8 0x78         `.....x
    decimal
             29   81    0  120   60  100  104    0
             96    0    0    0    0  200  120
    HOUR BITS: [0, 1, 1]
#### RECORD 34 LowReservoir 2013-09-01T09:45:24 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-09-01T09:45:24)
    0000   0x98 0x6d 0x09 0x01 0x0d                   .m...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 35 Bolus 2013-09-01T09:42:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 20.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x00 0x00    ........
    decimal
              1    0  200    0  200    0    0    0
    datetime (2013-09-01T09:42:20)
    0000   0x94 0x6a 0x49 0x01 0x0d                   .jI..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 36 SelectBasalProfile 2013-09-01T09:46:44 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x01                                  ..
    decimal
             20    1
    datetime (2013-09-01T09:46:44)
    0000   0xac 0x6e 0x09 0x01 0x0d                   .n...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 37 BasalProfileStart 2013-09-01T09:46:44 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-01T09:46:44)
    0000   0xac 0x6e 0x09 0x01 0x0d                   .n...
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [0, 1, 1]
#### RECORD 38 CalBGForPH 2013-09-01T11:34:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2013-09-01T11:34:02)
    0000   0x82 0x62 0x2b 0x01 0x0d                   .b+..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 39 BolusWizard 2013-09-01T11:34:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 180,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb4                                  [.
    decimal
             91  180
    datetime (2013-09-01T11:34:08)
    0000   0x88 0x62 0x0b 0x01 0x0d                   .b...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x28 0x00    .P.x<d(.
    0008   0x00 0x00 0x00 0x34 0x00 0x00 0x78         ...4..x
    decimal
              0   80    0  120   60  100   40    0
              0    0    0   52    0    0  120
    HOUR BITS: [0, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 118, 'amount': 5.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0xc8 0x76 0xc0                   \..v.
    decimal
             92    5  200  118  192
    datetime (unknown)

    body (0)

#### RECORD 41 BolusWizard 2013-09-01T11:34:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 180,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb4                                  [.
    decimal
             91  180
    datetime (2013-09-01T11:34:12)
    0000   0x8c 0x62 0x0b 0x01 0x0d                   .b...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x28 0x00    .P.x<d(.
    0008   0x00 0x00 0x00 0x34 0x00 0x00 0x78         ...4..x
    decimal
              0   80    0  120   60  100   40    0
              0    0    0   52    0    0  120
    HOUR BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 118, 'amount': 5.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0xc8 0x76 0xc0                   \..v.
    decimal
             92    5  200  118  192
    datetime (unknown)

    body (0)

#### RECORD 43 CalBGForPH 2013-09-01T11:34:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 300}
```
    op hex (2)
    0000   0x0a 0x2c                                  .,
    decimal
             10   44
    datetime (2013-09-01T11:34:31)
    0000   0x9f 0x62 0x2b 0x01 0x8d                   .b+..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 44 BolusWizard 2013-09-01T11:34:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 300,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 12.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2c                                  [,
    decimal
             91   44
    datetime (2013-09-01T11:34:33)
    0000   0xa1 0x62 0x0b 0x01 0x0d                   .b...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x78 0x00    .Q.x<dx.
    0008   0x00 0x00 0x00 0x34 0x00 0x44 0x78         ...4.Dx
    decimal
              0   81    0  120   60  100  120    0
              0    0    0   52    0   68  120
    HOUR BITS: [0, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 118, 'amount': 5.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0xc8 0x76 0xc0                   \..v.
    decimal
             92    5  200  118  192
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-09-01T11:34:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x34 0x00    ..D.D.4.
    decimal
              1    0   68    0   68    0   52    0
    datetime (2013-09-01T11:34:33)
    0000   0xa1 0x62 0x4b 0x01 0x0d                   .bK..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 47 BasalProfileStart 2013-09-01T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-01T12:00:00)
    0000   0x80 0x40 0x0c 0x01 0x0d                   .@...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 48 CalBGForPH 2013-09-01T14:47:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-09-01T14:47:12)
    0000   0x8c 0x6f 0x2e 0x01 0x0d                   .o...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2013-09-01T14:47:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-09-01T14:47:31)
    0000   0x9f 0x6f 0x0e 0x01 0x0d                   .o...
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x78         P....Px
    decimal
             25   80    0  120   60  100    0    0
             80    0    0    0    0   80  120
    HOUR BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 201, 'amount': 1.7, 'curve': 192},
 {'age': 55, 'amount': 5.0, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0xc9 0xc0 0xc8 0x37 0xd0    \.D...7.
    decimal
             92    8   68  201  192  200   55  208
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-09-01T14:47:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-09-01T14:47:32)
    0000   0xa0 0x6f 0x4e 0x01 0x0d                   .oN..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 52 CalBGForPH 2013-09-01T15:33:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-09-01T15:33:58)
    0000   0xba 0x61 0x2f 0x01 0x0d                   .a/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 53 BolusWizard 2013-09-01T15:34:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.4,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2013-09-01T15:34:24)
    0000   0x98 0x62 0x0f 0x01 0x0d                   .b...
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x24 0x00 0x00 0x40 0x00 0x24 0x78         $..@.$x
    decimal
             11   80    0  120   60  100    0    0
             36    0    0   64    0   36  120
    HOUR BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.0, 'curve': 192},
 {'age': 248, 'amount': 1.7, 'curve': 192},
 {'age': 102, 'amount': 5.0, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x30 0xc0 0x44 0xf8 0xc0    \.P0.D..
    0008   0xc8 0x66 0xd0                             .f.
    decimal
             92   11   80   48  192   68  248  192
            200  102  208
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-09-01T15:34:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x40 0x00    ..$.$.@.
    decimal
              1    0   36    0   36    0   64    0
    datetime (2013-09-01T15:34:24)
    0000   0x98 0x62 0x4f 0x01 0x0d                   .bO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 56 LowReservoir 2013-09-01T16:14:28 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-09-01T16:14:28)
    0000   0x9c 0x4e 0x10 0x01 0x0d                   .N...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 CalBGForPH 2013-09-01T17:04:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 201}
```
    op hex (2)
    0000   0x0a 0xc9                                  ..
    decimal
             10  201
    datetime (2013-09-01T17:04:44)
    0000   0xac 0x44 0x31 0x01 0x0d                   .D1..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 58 BolusWizard 2013-09-01T17:04:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 201,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc9                                  [.
    decimal
             91  201
    datetime (2013-09-01T17:04:46)
    0000   0xae 0x44 0x11 0x01 0x0d                   .D...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x34 0x00    .P.d<d4.
    0008   0x00 0x00 0x00 0x1c 0x00 0x18 0x78         ......x
    decimal
              0   80    0  100   60  100   52    0
              0    0    0   28    0   24  120
    HOUR BITS: [0, 1, 0]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 0.9, 'curve': 192},
 {'age': 138, 'amount': 2.0, 'curve': 192},
 {'age': 82, 'amount': 1.7, 'curve': 208},
 {'age': 192, 'amount': 5.0, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x24 0x62 0xc0 0x50 0x8a 0xc0    \.$b.P..
    0008   0x44 0x52 0xd0 0xc8 0xc0 0xd0              DR....
    decimal
             92   14   36   98  192   80  138  192
             68   82  208  200  192  208
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-09-01T17:04:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x1c 0x00    ........
    decimal
              1    0   24    0   24    0   28    0
    datetime (2013-09-01T17:04:47)
    0000   0xaf 0x44 0x51 0x01 0x0d                   .DQ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 61 CalBGForPH 2013-09-01T20:29:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-09-01T20:29:16)
    0000   0x90 0x5d 0x34 0x01 0x0d                   .]4..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 62 BolusWizard 2013-09-01T20:29:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 116,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-09-01T20:29:28)
    0000   0x9c 0x5d 0x14 0x01 0x0d                   .]...
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x78         T....Tx
    decimal
             21   80    0  100   60  100    0    0
             84    0    0    0    0   84  120
    HOUR BITS: [0, 1, 0]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 213, 'amount': 0.6, 'curve': 192},
 {'age': 47, 'amount': 0.9, 'curve': 208},
 {'age': 87, 'amount': 2.0, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x18 0xd5 0xc0 0x24 0x2f 0xd0    \....$/.
    0008   0x50 0x57 0xd0                             PW.
    decimal
             92   11   24  213  192   36   47  208
             80   87  208
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-09-01T20:29:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x00 0x00    ..T.T...
    decimal
              1    0   84    0   84    0    0    0
    datetime (2013-09-01T20:29:28)
    0000   0x9c 0x5d 0x54 0x01 0x0d                   .]T..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 65 CalBGForPH 2013-09-01T22:12:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2013-09-01T22:12:37)
    0000   0xa5 0x4c 0x36 0x01 0x0d                   .L6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 66 BolusWizard 2013-09-01T22:12:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 234,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 7.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xea                                  [.
    decimal
             91  234
    datetime (2013-09-01T22:12:41)
    0000   0xa9 0x4c 0x16 0x01 0x0d                   .L...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x4c 0x00    .P.d<dL.
    0008   0x00 0x00 0x00 0x20 0x00 0x2c 0x78         ... .,x
    decimal
              0   80    0  100   60  100   76    0
              0    0    0   32    0   44  120
    HOUR BITS: [0, 1, 0]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 106, 'amount': 2.1, 'curve': 192},
 {'age': 60, 'amount': 0.6, 'curve': 208},
 {'age': 150, 'amount': 0.9, 'curve': 208},
 {'age': 190, 'amount': 2.0, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x54 0x6a 0xc0 0x18 0x3c 0xd0    \.Tj..<.
    0008   0x24 0x96 0xd0 0x50 0xbe 0xd0              $..P..
    decimal
             92   14   84  106  192   24   60  208
             36  150  208   80  190  208
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-09-01T22:12:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x20 0x00    ..,.,. .
    decimal
              1    0   44    0   44    0   32    0
    datetime (2013-09-01T22:12:41)
    0000   0xa9 0x4c 0x56 0x01 0x0d                   .LV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 69 BasalProfileStart 2013-09-02T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-02T00:00:00)
    0000   0x80 0x40 0x00 0x02 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 70 ResultTotals (2000, 10, 0, 0, 13, 1) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xdb                   .....
    decimal
              7    0    0    4  219
    datetime ((2000, 10, 0, 0, 13, 1))
    0000   0x81 0x8d 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-2.data: 71 records`
