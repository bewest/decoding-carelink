## START analysis/sarak/raw//ReadHistoryData-page-8.data
#### RECORD 0 Sara6E 2013-08-17T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-17T00:00:00)
    0000   0x90 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0x74 0x00 0x00 0x09 0x00 0x00    ..t.....
    0008   0x04 0xd8 0x02 0xdc 0x3b 0x01 0xfc 0x29    ....;..)
    0010   0x00 0x8d 0x01 0xfc 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x09 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x64    .......d
    0028   0xd7 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  116    0    0    9    0    0
              4  216    2  220   59    1  252   41
              0  141    1  252    0    0    0    0
              0    0    9    0    0    0    0    0
              0    0    0    0    0    0    0  100
            215    0    0    0    0    0    0    0
              0

#### RECORD 1 BasalProfileStart 2013-08-17T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-17T04:00:00)
    0000   0x80 0x00 0x04 0x11 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 2 CalBGForPH 2013-08-17T07:47:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 228}
```
    op hex (2)
    0000   0x0a 0xe4                                  ..
    decimal
             10  228
    datetime (2013-08-17T07:47:19)
    0000   0x93 0x2f 0x27 0x11 0x0d                   ./'..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 BolusWizard 2013-08-17T07:47:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 228,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 1,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 7.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe4                                  [.
    decimal
             91  228
    datetime (2013-08-17T07:47:22)
    0000   0x96 0x2f 0x07 0x11 0x0d                   ./...
    body (15)
    hex
    0000   0x01 0x50 0x00 0x78 0x3c 0x64 0x48 0x00    .P.x<dH.
    0008   0x00 0x00 0x00 0x00 0x00 0x48 0x78         .....Hx
    decimal
              1   80    0  120   60  100   72    0
              0    0    0    0    0   72  120
    HOUR BITS: [0, 0, 1]
#### RECORD 4 Bolus 2013-08-17T07:47:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2013-08-17T07:47:22)
    0000   0x96 0x2f 0x47 0x11 0x0d                   ./G..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BasalProfileStart 2013-08-17T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-17T08:00:00)
    0000   0x80 0x00 0x08 0x11 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 6 CalBGForPH 2013-08-17T10:05:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-08-17T10:05:32)
    0000   0xa0 0x05 0x2a 0x11 0x0d                   ..*..
    body (0)

#### RECORD 7 BolusWizard 2013-08-17T10:05:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
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
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-17T10:05:40)
    0000   0xa8 0x05 0x0a 0x11 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x44 0x00 0x00 0x0c 0x00 0x44 0x78         D....Dx
    decimal
             21   80    0  120   60  100    0    0
             68    0    0   12    0   68  120

#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 142, 'amount': 1.8, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x48 0x8e 0xc0                   \.H..
    decimal
             92    5   72  142  192
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-08-17T10:05:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x0c 0x00    ..D.D...
    decimal
              1    0   68    0   68    0   12    0
    datetime (2013-08-17T10:05:41)
    0000   0xa9 0x05 0x4a 0x11 0x0d                   ..J..
    body (0)

#### RECORD 10 CalBGForPH 2013-08-17T10:54:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-17T10:54:33)
    0000   0xa1 0x36 0x2a 0x11 0x0d                   .6*..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 BolusWizard 2013-08-17T10:54:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
 'carb_input': 19,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-17T10:54:39)
    0000   0xa7 0x36 0x0a 0x11 0x0d                   .6...
    body (15)
    hex
    0000   0x13 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x3c 0x00 0x00 0x38 0x00 0x3c 0x78         <..8.<x
    decimal
             19   80    0  120   60  100    0    0
             60    0    0   56    0   60  120
    HOUR BITS: [0, 0, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 1.7, 'curve': 192},
 {'age': 191, 'amount': 1.8, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x33 0xc0 0x48 0xbf 0xc0    \.D3.H..
    decimal
             92    8   68   51  192   72  191  192
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-08-17T10:54:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x38 0x00    ..<.<.8.
    decimal
              1    0   60    0   60    0   56    0
    datetime (2013-08-17T10:54:39)
    0000   0xa7 0x36 0x4a 0x11 0x0d                   .6J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 BasalProfileStart 2013-08-17T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-17T12:00:00)
    0000   0x80 0x00 0x0c 0x11 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 15 CalBGForPH 2013-08-17T13:23:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-08-17T13:23:00)
    0000   0x80 0x17 0x2d 0x11 0x0d                   ..-..
    body (0)

#### RECORD 16 CalBGForPH 2013-08-17T13:23:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 197}
```
    op hex (2)
    0000   0x0a 0xc5                                  ..
    decimal
             10  197
    datetime (2013-08-17T13:23:42)
    0000   0xaa 0x17 0x2d 0x11 0x0d                   ..-..
    body (0)

#### RECORD 17 BolusWizard 2013-08-17T13:23:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 197,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0xc5                                  [.
    decimal
             91  197
    datetime (2013-08-17T13:23:49)
    0000   0xb1 0x17 0x0d 0x11 0x0d                   .....
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x30 0x00    .P.x<d0.
    0008   0x34 0x00 0x00 0x08 0x00 0x5c 0x78         4....\x
    decimal
             16   80    0  120   60  100   48    0
             52    0    0    8    0   92  120

#### RECORD 18 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 1.5, 'curve': 192},
 {'age': 200, 'amount': 1.7, 'curve': 192},
 {'age': 84, 'amount': 1.8, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0x96 0xc0 0x44 0xc8 0xc0    \.<..D..
    0008   0x48 0x54 0xd0                             HT.
    decimal
             92   11   60  150  192   68  200  192
             72   84  208
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-08-17T13:23:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x08 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    8    0
    datetime (2013-08-17T13:23:50)
    0000   0xb2 0x17 0x4d 0x11 0x0d                   ..M..
    body (0)

#### RECORD 20 CalBGForPH 2013-08-17T15:48:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-17T15:48:45)
    0000   0xad 0x30 0x2f 0x11 0x0d                   .0/..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 21 BolusWizard 2013-08-17T15:48:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-17T15:48:49)
    0000   0xb1 0x30 0x0f 0x11 0x0d                   .0...
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x2c 0x00 0x00 0x10 0x00 0x2c 0x78         ,....,x
    decimal
             14   80    0  120   60  100    0    0
             44    0    0   16    0   44  120
    HOUR BITS: [0, 0, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 145, 'amount': 2.3, 'curve': 192},
 {'age': 39, 'amount': 1.5, 'curve': 208},
 {'age': 89, 'amount': 1.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x5c 0x91 0xc0 0x3c 0x27 0xd0    \.\..<'.
    0008   0x44 0x59 0xd0                             DY.
    decimal
             92   11   92  145  192   60   39  208
             68   89  208
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-08-17T15:48:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x10 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   16    0
    datetime (2013-08-17T15:48:49)
    0000   0xb1 0x30 0x4f 0x11 0x0d                   .0O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 24 CalBGForPH 2013-08-17T16:28:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-08-17T16:28:36)
    0000   0xa4 0x1c 0x30 0x11 0x0d                   ..0..
    body (0)

#### RECORD 25 BolusWizard 2013-08-17T16:28:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 199,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc7                                  [.
    decimal
             91  199
    datetime (2013-08-17T16:28:38)
    0000   0xa6 0x1c 0x10 0x11 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x34 0x00    .P.x<d4.
    0008   0x00 0x00 0x00 0x24 0x00 0x10 0x78         ...$..x
    decimal
              0   80    0  120   60  100   52    0
              0    0    0   36    0   16  120

#### RECORD 26 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 1.1, 'curve': 192},
 {'age': 185, 'amount': 2.3, 'curve': 192},
 {'age': 79, 'amount': 1.5, 'curve': 208},
 {'age': 129, 'amount': 1.7, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x2c 0x2d 0xc0 0x5c 0xb9 0xc0    \.,-.\..
    0008   0x3c 0x4f 0xd0 0x44 0x81 0xd0              <O.D..
    decimal
             92   14   44   45  192   92  185  192
             60   79  208   68  129  208
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-08-17T16:28:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x24 0x00    ......$.
    decimal
              1    0   16    0   16    0   36    0
    datetime (2013-08-17T16:28:38)
    0000   0xa6 0x1c 0x50 0x11 0x0d                   ..P..
    body (0)

#### RECORD 28 CalBGForPH 2013-08-17T16:46:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-17T16:46:40)
    0000   0xa8 0x2e 0x30 0x11 0x0d                   ..0..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 29 BolusWizard 2013-08-17T16:46:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
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
    datetime (2013-08-17T16:46:50)
    0000   0xb2 0x2e 0x10 0x11 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x44 0x00 0x00 0x30 0x00 0x44 0x78         D..0.Dx
    decimal
             21   80    0  120   60  100    0    0
             68    0    0   48    0   68  120
    HOUR BITS: [0, 0, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 0.4, 'curve': 192},
 {'age': 63, 'amount': 1.1, 'curve': 192},
 {'age': 203, 'amount': 2.3, 'curve': 192},
 {'age': 97, 'amount': 1.5, 'curve': 208},
 {'age': 147, 'amount': 1.7, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x10 0x17 0xc0 0x2c 0x3f 0xc0    \....,?.
    0008   0x5c 0xcb 0xc0 0x3c 0x61 0xd0 0x44 0x93    \..<a.D.
    0010   0xd0                                       .
    decimal
             92   17   16   23  192   44   63  192
             92  203  192   60   97  208   68  147
            208
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-08-17T16:46:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x30 0x00    ..X.X.0.
    decimal
              1    0   88    0   88    0   48    0
    datetime (2013-08-17T16:46:50)
    0000   0xb2 0x2e 0x50 0x11 0x0d                   ..P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 32 CalBGForPH 2013-08-17T18:21:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 279}
```
    op hex (2)
    0000   0x0a 0x17                                  ..
    decimal
             10   23
    datetime (2013-08-17T18:21:07)
    0000   0x87 0x15 0x32 0x11 0x8d                   ..2..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 BasalProfileStart 2013-08-18T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-18T00:00:00)
    0000   0x80 0x00 0x00 0x12 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 34 MResultTotals 2013-08-18T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x94                   .....
    decimal
              7    0    0    4  148
    datetime (2013-08-18T00:00:00)
    0000   0x91 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 35 Sara6E 2013-08-18T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-18T00:00:00)
    0000   0x91 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0xa8 0x00 0x00 0x09 0x00 0x00    ........
    0008   0x04 0x94 0x02 0xdc 0x3e 0x01 0xb8 0x26    ....>..&
    0010   0x00 0x5c 0x01 0x04 0x00 0x58 0x00 0x5c    .\...X.\
    0018   0x00 0x00 0x04 0x02 0x01 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x64    .......d
    0028   0x17 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  168    0    0    9    0    0
              4  148    2  220   62    1  184   38
              0   92    1    4    0   88    0   92
              0    0    4    2    1    0    4    0
              0    0    0    0    0    0    0  100
             23    0    0    0    0    0    0    0
              0

#### RECORD 36 CalBGForPH 2013-08-18T01:17:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 269}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2013-08-18T01:17:35)
    0000   0xa3 0x11 0x21 0x12 0x8d                   ..!..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 BolusWizard 2013-08-18T01:17:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 269,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 9.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0d                                  [.
    decimal
             91   13
    datetime (2013-08-18T01:17:38)
    0000   0xa6 0x11 0x01 0x12 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x6e 0x5c 0x00    .Q.x<n\.
    0008   0x00 0x00 0x00 0x00 0x00 0x5c 0x82         .....\.
    decimal
              0   81    0  120   60  110   92    0
              0    0    0    0    0   92  130

#### RECORD 38 Bolus 2013-08-18T01:17:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x00 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    0    0
    datetime (2013-08-18T01:17:38)
    0000   0xa6 0x11 0x41 0x12 0x0d                   ..A..
    body (0)

#### RECORD 39 BasalProfileStart 2013-08-18T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-18T04:00:00)
    0000   0x80 0x00 0x04 0x12 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 40 BasalProfileStart 2013-08-18T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-18T08:00:00)
    0000   0x80 0x00 0x08 0x12 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 41 CalBGForPH 2013-08-18T10:35:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-08-18T10:35:13)
    0000   0x8d 0x23 0x2a 0x12 0x0d                   .#*..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 42 BolusWizard 2013-08-18T10:35:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 116,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-08-18T10:35:21)
    0000   0x95 0x23 0x0a 0x12 0x0d                   .#...
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x78         (....(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0    0    0   40  120
    HOUR BITS: [0, 0, 1]
#### RECORD 43 Bolus 2013-08-18T10:35:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2013-08-18T10:35:21)
    0000   0x95 0x23 0x4a 0x12 0x0d                   .#J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 44 LowReservoir 2013-08-18T11:12:21 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-18T11:12:21)
    0000   0x95 0x0c 0x0b 0x12 0x0d                   .....
    body (0)

#### RECORD 45 BasalProfileStart 2013-08-18T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-18T12:00:00)
    0000   0x80 0x00 0x0c 0x12 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 46 CalBGForPH 2013-08-18T14:48:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-08-18T14:48:10)
    0000   0x8a 0x30 0x2e 0x12 0x0d                   .0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 47 CalBGForPH 2013-08-18T17:45:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-08-18T17:45:09)
    0000   0x89 0x2d 0x31 0x12 0x0d                   .-1..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 BolusWizard 2013-08-18T17:45:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 7.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2013-08-18T17:45:14)
    0000   0x8e 0x2d 0x11 0x72 0x0d                   .-.r.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x64 0x3c 0x64 0x48 0x00    .P.d<dH.
    0008   0x28 0x00 0x00 0x00 0x00 0x70 0x78         (....px
    decimal
             10   80    0  100   60  100   72    0
             40    0    0    0    0  112  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 176, 'amount': 1.0, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0xb0 0xd0                   \.(..
    decimal
             92    5   40  176  208
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2013-08-18T17:45:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x00 0x00    ..p.p...
    decimal
              1    0  112    0  112    0    0    0
    datetime (2013-08-18T17:45:15)
    0000   0x8f 0x2d 0x51 0x72 0x0d                   .-Qr.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 LowReservoir 2013-08-18T21:00:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-08-18T21:00:00)
    0000   0x80 0x00 0x15 0x12 0x0d                   .....
    body (0)

#### RECORD 52 BasalProfileStart 2013-08-19T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-19T00:00:00)
    0000   0x80 0x00 0x00 0x13 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 53 MResultTotals 2013-08-19T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xd0                   .....
    decimal
              7    0    0    3  208
    datetime (2013-08-19T00:00:00)
    0000   0x92 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 54 Sara6E 2013-08-19T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-19T00:00:00)
    0000   0x92 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0xb2 0x00 0x00 0x04 0x00 0x00    ........
    0008   0x03 0xd0 0x02 0xdc 0x4b 0x00 0xf4 0x19    ....K...
    0010   0x00 0x17 0x00 0x28 0x00 0x5c 0x00 0x70    ...(.\.p
    0018   0x00 0x00 0x01 0x01 0x01 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x5f    ......._
    0028   0x0d 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  178    0    0    4    0    0
              3  208    2  220   75    0  244   25
              0   23    0   40    0   92    0  112
              0    0    1    1    1    0    4    0
              0    0    0    0    0    0    0   95
             13    0    0    0    0    0    0    0
              0

#### RECORD 55 BasalProfileStart 2013-08-19T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-19T04:00:00)
    0000   0x80 0x00 0x04 0x13 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 56 BasalProfileStart 2013-08-19T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-19T08:00:00)
    0000   0x80 0x00 0x08 0x13 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 57 Rewind 2013-08-19T08:59:47 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-19T08:59:47)
    0000   0xaf 0x3b 0x08 0x13 0x0d                   .;...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 Prime 2013-08-19T09:01:42 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x22                   ...."
    decimal
              3    0    0    0   34
    datetime (2013-08-19T09:01:42)
    0000   0xaa 0x01 0x29 0x13 0x0d                   ..)..
    body (0)

#### RECORD 59 BasalProfileStart 2013-08-19T09:30:18 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-19T09:30:18)
    0000   0x92 0x1e 0x09 0x13 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 60 CalBGForPH 2013-08-19T09:38:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-08-19T09:38:19)
    0000   0x93 0x26 0x29 0x13 0x0d                   .&)..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 BolusWizard 2013-08-19T09:38:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 106,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-08-19T09:38:25)
    0000   0x99 0x26 0x09 0x13 0x0d                   .&...
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x2c 0x00 0x00 0x00 0x00 0x2c 0x78         ,....,x
    decimal
             14   80    0  120   60  100    0    0
             44    0    0    0    0   44  120
    HOUR BITS: [0, 0, 1]
#### RECORD 62 Bolus 2013-08-19T09:38:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x00 0x00    ..,.,...
    decimal
              1    0   44    0   44    0    0    0
    datetime (2013-08-19T09:38:25)
    0000   0x99 0x26 0x49 0x13 0x0d                   .&I..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 BasalProfileStart 2013-08-19T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-19T12:00:00)
    0000   0x80 0x00 0x0c 0x13 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 64 CalBGForPH 2013-08-19T13:30:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2013-08-19T13:30:35)
    0000   0xa3 0x1e 0x2d 0x13 0x0d                   ..-..
    body (0)

#### RECORD 65 BolusWizard 2013-08-19T13:30:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 181,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0xb5                                  [.
    decimal
             91  181
    datetime (2013-08-19T13:30:53)
    0000   0xb5 0x1e 0x0d 0x13 0x0d                   .....
    body (15)
    hex
    0000   0x21 0x50 0x00 0x78 0x3c 0x64 0x28 0x00    !P.x<d(.
    0008   0x6c 0x00 0x00 0x00 0x00 0x94 0x78         l.....x
    decimal
             33   80    0  120   60  100   40    0
            108    0    0    0    0  148  120

#### RECORD 66 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 237, 'amount': 1.1, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0xed 0xc0                   \.,..
    decimal
             92    5   44  237  192
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-08-19T13:30:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0x00 0x00    ........
    decimal
              1    0  148    0  148    0    0    0
    datetime (2013-08-19T13:30:53)
    0000   0xb5 0x1e 0x4d 0x13 0x0d                   ..M..
    body (0)

#### RECORD 68 CalBGForPH 2013-08-19T15:54:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 337}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2013-08-19T15:54:48)
    0000   0xb0 0x36 0x2f 0x13 0x8d                   .6/..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 BolusWizard 2013-08-19T15:54:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 337,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 14.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x51                                  [Q
    decimal
             91   81
    datetime (2013-08-19T15:54:51)
    0000   0xb3 0x36 0x0f 0x13 0x0d                   .6...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x90 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x14 0x00 0x7c 0x78         .....|x
    decimal
              0   81    0  120   60  100  144    0
              0    0    0   20    0  124  120
    HOUR BITS: [0, 0, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 141, 'amount': 0.6, 'curve': 192},
 {'age': 151, 'amount': 3.1, 'curve': 192},
 {'age': 125, 'amount': 1.1, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x18 0x8d 0xc0 0x7c 0x97 0xc0    \....|..
    0008   0x2c 0x7d 0xd0                             ,}.
    decimal
             92   11   24  141  192  124  151  192
             44  125  208
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-08-19T15:54:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x14 0x00    ..|.|...
    decimal
              1    0  124    0  124    0   20    0
    datetime (2013-08-19T15:54:51)
    0000   0xb3 0x36 0x4f 0x13 0x0d                   .6O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 72 CalBGForPH 2013-08-19T20:37:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2013-08-19T20:37:46)
    0000   0xae 0x25 0x34 0x13 0x0d                   .%4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 73 BolusWizard 2013-08-19T20:37:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 176,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2013-08-19T20:37:53)
    0000   0xb5 0x25 0x14 0x13 0x0d                   .%...
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x24 0x00    .P.d<d$.
    0008   0x58 0x00 0x00 0x00 0x00 0x7c 0x78         X....|x
    decimal
             22   80    0  100   60  100   36    0
             88    0    0    0    0  124  120
    HOUR BITS: [0, 0, 1]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 3.1, 'curve': 208},
 {'age': 168, 'amount': 0.6, 'curve': 208},
 {'age': 178, 'amount': 3.1, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x7c 0x1c 0xd0 0x18 0xa8 0xd0    \.|.....
    0008   0x7c 0xb2 0xd0                             |..
    decimal
             92   11  124   28  208   24  168  208
            124  178  208
    datetime (unknown)

    body (0)

#### RECORD 75 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x8d                                  ..
    decimal
              0  141
    datetime (unknown)

    body (0)

`end analysis/sarak/raw//ReadHistoryData-page-8.data: 76 records`
