## START logs/ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 599, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x34 0x00 0x00 0x78 0x5c 0x05 0xc8 0x76    4..x\..v
    0008   0xc0 0x5b 0xb4 0x8c 0x62 0x0b 0x01 0x0d    .[..b...
    0010   0x00 0x50 0x00 0x78 0x3c 0x64 0x28 0x00    .P.x<d(.
    0018   0x00 0x00 0x00 0x34 0x00 0x00 0x78 0x5c    ...4..x\
##### DEBUG DECIMAL
             52    0    0  120   92    5  200  118
            192   91  180  140   98   11    1   13
              0   80    0  120   60  100   40    0
              0    0    0   52    0    0  120   92
#### RECORD 0 Sara6E 2013-08-31T01:03:47 head[54], body[3] op[0x6e]

    op hex (54)
    0000   0x6e 0x9e 0x0d 0x05 0x00 0xc0 0x00 0x00    n.......
    0008   0x09 0x00 0x00 0x06 0x54 0x04 0x00 0x3f    ....T..?
    0010   0x02 0x54 0x25 0x00 0x34 0x00 0xa8 0x01    .T%.4...
    0018   0xac 0x00 0x00 0x00 0x00 0x03 0x05 0x00    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x68 0x82 0x00 0x00 0x00 0x00    ..h.....
    0030   0x00 0x00 0x00 0x00 0x7b 0x00              ....{.
    decimal
            110  158   13    5    0  192    0    0
              9    0    0    6   84    4    0   63
              2   84   37    0   52    0  168    1
            172    0    0    0    0    3    5    0
              0    4    0    0    0    0    0    0
              0    0  104  130    0    0    0    0
              0    0    0    0  123    0
    datetime (2013-08-31T01:03:47)
    0000   0xaf 0x03 0x21 0x1f 0x0d                   ..!..
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 1 CalBGForPH 2013-08-31T08:45:29 head[2], body[0] op[0x0a]
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
#### RECORD 2 CalBGForPH 2013-08-31T08:45:35 head[2], body[0] op[0x0a]
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
#### RECORD 3 BolusWizard 2013-08-31T08:45:46 head[2], body[15] op[0x5b]
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
#### RECORD 4 Bolus 2013-08-31T08:45:46 head[8], body[0] op[0x01]
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
#### RECORD 5 CalBGForPH 2013-08-31T10:25:25 head[2], body[0] op[0x0a]
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

#### RECORD 6 BolusWizard 2013-08-31T10:25:27 head[2], body[15] op[0x5b]
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

#### RECORD 7 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
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

#### RECORD 8 Bolus 2013-08-31T10:25:28 head[8], body[0] op[0x01]
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

#### RECORD 9 CalBGForPH 2013-08-31T12:43:42 head[2], body[0] op[0x0a]
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
#### RECORD 10 BolusWizard 2013-08-31T12:43:53 head[2], body[15] op[0x5b]
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
#### RECORD 11 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
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

#### RECORD 12 Bolus 2013-08-31T12:43:53 head[8], body[0] op[0x01]
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
#### RECORD 13 CalBGForPH 2013-08-31T15:01:17 head[2], body[0] op[0x0a]
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
#### RECORD 14 BolusWizard 2013-08-31T15:01:20 head[2], body[15] op[0x5b]
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

#### RECORD 15 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
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

#### RECORD 16 Bolus 2013-08-31T15:01:20 head[8], body[0] op[0x01]
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

#### RECORD 17 CalBGForPH 2013-08-31T15:31:59 head[2], body[0] op[0x0a]
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

#### RECORD 18 BolusWizard 2013-08-31T15:32:28 head[2], body[15] op[0x5b]
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
#### RECORD 19 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
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

#### RECORD 20 Bolus 2013-08-31T15:32:28 head[8], body[0] op[0x01]
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
#### RECORD 21 CalBGForPH 2013-08-31T18:29:48 head[2], body[0] op[0x0a]
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

#### RECORD 22 BolusWizard 2013-08-31T18:29:54 head[2], body[15] op[0x5b]
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

#### RECORD 23 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
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

#### RECORD 24 Bolus 2013-08-31T18:29:55 head[8], body[0] op[0x01]
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

#### RECORD 25 CalBGForPH 2013-08-31T18:59:50 head[2], body[0] op[0x0a]
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
#### RECORD 26 BolusWizard 2013-08-31T18:59:55 head[2], body[15] op[0x5b]
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
#### RECORD 27 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
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

#### RECORD 28 Bolus 2013-08-31T18:59:55 head[8], body[0] op[0x01]
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
#### RECORD 29 ResultTotals (2000, 8, 0, 0, 13, 31) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime ((2000, 8, 0, 0, 13, 31))
    0000   0x9f 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x9f 0x0d 0x05 0x00 0xad 0x00 0x00    n.......
    0008   0x08 0x00 0x00 0x04 0xd2 0x02 0xbe 0x39    .......9
    0010   0x02 0x14 0x2b 0x00 0x5a 0x01 0x24 0x00    ..+.Z.$.
    0018   0xf0 0x00 0x00 0x00 0x00 0x04 0x03 0x00    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x4b 0x27 0x00 0x00 0x00 0x00    ..K'....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  159   13    5    0  173    0    0
              8    0    0    4  210    2  190   57
              2   20   43    0   90    1   36    0
            240    0    0    0    0    4    3    0
              0    4    0    0    0    0    0    0
              0    0   75   39    0    0    0    0
              0    0    0

#### RECORD 30 Base (2001, 2, 9, 10, 8, 23) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2001, 2, 9, 10, 8, 23))
    0000   0x17 0x88 0x6a 0x29 0x01                   ..j).
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1]
#### RECORD 31 Base (2001, 2, 9, 10, 20, 23) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x5b                                  .[
    decimal
            141   91
    datetime ((2001, 2, 9, 10, 20, 23))
    0000   0x17 0x94 0x6a 0x09 0x01                   ..j..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 Base (2004, 4, 28, 24, 0, 17) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1d                                  ..
    decimal
             13   29
    datetime ((2004, 4, 28, 24, 0, 17))
    0000   0x51 0x00 0x78 0x3c 0x64                   Q.x<d
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 33 Base (2000, 4, 0, 0, 0, 32) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x00                                  h.
    decimal
            104    0
    datetime ((2000, 4, 0, 0, 0, 32))
    0000   0x60 0x00 0x00 0x00 0x00                   `....
    body (0)

#### RECORD 34 Base (2009, 3, 13, 24, 8, 52) head[2], body[0] op[0xc8]

    op hex (2)
    0000   0xc8 0x78                                  .x
    decimal
            200  120
    datetime ((2009, 3, 13, 24, 8, 52))
    0000   0x34 0xc8 0x98 0x6d 0x09                   4..m.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 Bolus (2009, 0, 10, 20, 0, 0) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x0d 0x01 0x00 0xc8 0x00 0xc8 0x00    ........
    decimal
              1   13    1    0  200    0  200    0
    datetime ((2009, 0, 10, 20, 0, 0))
    0000   0x00 0x00 0x94 0x6a 0x49                   ...jI
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 36 Bolus 2014-01-12T02:59:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x0d 0x14 0x01 0xac 0x6e 0x09 0x01    .....n..
    decimal
              1   13   20    1  172  110    9    1
    datetime (2014-01-12T02:59:13)
    0000   0x0d 0x7b 0x02 0xac 0x6e                   .{..n
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 37 Base (2010, 0, 0, 2, 16, 13) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x01                                  ..
    decimal
              9    1
    datetime ((2010, 0, 0, 2, 16, 13))
    0000   0x0d 0x10 0x22 0x00 0x0a                   .."..
    body (0)

#### RECORD 38 Base (2011, 4, 13, 1, 43, 34) head[2], body[0] op[0xb4]

    op hex (2)
    0000   0xb4 0x82                                  ..
    decimal
            180  130
    datetime ((2011, 4, 13, 1, 43, 34))
    0000   0x62 0x2b 0x01 0x0d 0x5b                   b+..[
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 39 Base (2000, 4, 13, 1, 11, 34) head[2], body[0] op[0xb4]

    op hex (2)
    0000   0xb4 0x88                                  ..
    decimal
            180  136
    datetime ((2000, 4, 13, 1, 11, 34))
    0000   0x62 0x0b 0x01 0x0d 0x00                   b....
    body (0)

#### RECORD 40 Base (2000, 4, 8, 4, 60, 56) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x00                                  P.
    decimal
             80    0
    datetime ((2000, 4, 8, 4, 60, 56))
    0000   0x78 0x3c 0x64 0x28 0x00                   x<d(.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-2.data: 41 records`
