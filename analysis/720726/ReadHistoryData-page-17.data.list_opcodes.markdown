## START analysis/ianj/raw/ReadHistoryData-page-17.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xba 0x59                                  .Y
##### DEBUG DECIMAL
            186   89
#### RECORD 0 BolusWizard 2012-08-20T16:43:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T16:43:17)
    0000   0x91 0x2b 0x10 0x74 0x0c                   .+.t.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 0.15, 'curve': 4},
 {'age': 39, 'amount': 2.05, 'curve': 4},
 {'age': 69, 'amount': 1.4, 'curve': 4},
 {'age': 239, 'amount': 1.25, 'curve': 4},
 {'age': 249, 'amount': 1.75, 'curve': 4},
 {'age': 13, 'amount': 3.1, 'curve': 20},
 {'age': 23, 'amount': 1.3, 'curve': 20},
 {'age': 93, 'amount': 1.2, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x06 0x1d 0x04 0x52 0x27 0x04    \....R'.
    0008   0x38 0x45 0x04 0x32 0xef 0x04 0x46 0xf9    8E.2..F.
    0010   0x04 0x7c 0x0d 0x14 0x34 0x17 0x14 0x30    .|..4..0
    0018   0x5d 0x14                                  ].
    decimal
             92   26    6   29    4   82   39    4
             56   69    4   50  239    4   70  249
              4  124   13   20   52   23   20   48
             93   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2012-08-20T16:43:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x80 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  128    0
    datetime (2012-08-20T16:43:17)
    0000   0x91 0x2b 0x50 0x74 0x0c                   .+Pt.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2012-08-20T17:35:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T17:35:22)
    0000   0x96 0x23 0x11 0x74 0x0c                   .#.t.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 0.9, 'curve': 4},
 {'age': 61, 'amount': 1.1, 'curve': 4},
 {'age': 81, 'amount': 0.15, 'curve': 4},
 {'age': 91, 'amount': 2.05, 'curve': 4},
 {'age': 121, 'amount': 1.4, 'curve': 4},
 {'age': 35, 'amount': 1.25, 'curve': 20},
 {'age': 45, 'amount': 1.75, 'curve': 20},
 {'age': 65, 'amount': 3.1, 'curve': 20},
 {'age': 75, 'amount': 1.3, 'curve': 20},
 {'age': 145, 'amount': 1.2, 'curve': 20}]
```
    op hex (32)
    0000   0x5c 0x20 0x24 0x33 0x04 0x2c 0x3d 0x04    \ $3.,=.
    0008   0x06 0x51 0x04 0x52 0x5b 0x04 0x38 0x79    .Q.R[.8y
    0010   0x04 0x32 0x23 0x14 0x46 0x2d 0x14 0x7c    .2#.F-.|
    0018   0x41 0x14 0x34 0x4b 0x14 0x30 0x91 0x14    A.4K.0..
    decimal
             92   32   36   51    4   44   61    4
              6   81    4   82   91    4   56  121
              4   50   35   20   70   45   20  124
             65   20   52   75   20   48  145   20
    datetime (unknown)

    body (0)

#### RECORD 5 Ian69 2012-08-20T17:35:22 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-20T17:35:22)
    0000   0x96 0x23 0x71 0x14 0x0c                   .#q..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 6 Bolus 2012-08-20T17:35:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x98 0x00    ..X.X...
    decimal
              1    0   88    0   88    0  152    0
    datetime (2012-08-20T17:35:22)
    0000   0x96 0x23 0x51 0x74 0x0c                   .#Qt.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 BolusWizard 2012-08-20T18:43:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T18:43:02)
    0000   0x82 0x2b 0x12 0x74 0x0c                   .+.t.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 2.2, 'curve': 4},
 {'age': 119, 'amount': 0.9, 'curve': 4},
 {'age': 129, 'amount': 1.1, 'curve': 4},
 {'age': 149, 'amount': 0.15, 'curve': 4},
 {'age': 159, 'amount': 2.05, 'curve': 4},
 {'age': 189, 'amount': 1.4, 'curve': 4},
 {'age': 103, 'amount': 1.25, 'curve': 20},
 {'age': 113, 'amount': 1.75, 'curve': 20},
 {'age': 133, 'amount': 3.1, 'curve': 20},
 {'age': 143, 'amount': 1.3, 'curve': 20},
 {'age': 213, 'amount': 1.2, 'curve': 20}]
```
    op hex (35)
    0000   0x5c 0x23 0x58 0x45 0x04 0x24 0x77 0x04    \#XE.$w.
    0008   0x2c 0x81 0x04 0x06 0x95 0x04 0x52 0x9f    ,.....R.
    0010   0x04 0x38 0xbd 0x04 0x32 0x67 0x14 0x46    .8..2g.F
    0018   0x71 0x14 0x7c 0x85 0x14 0x34 0x8f 0x14    q.|..4..
    0020   0x30 0xd5 0x14                             0..
    decimal
             92   35   88   69    4   36  119    4
             44  129    4    6  149    4   82  159
              4   56  189    4   50  103   20   70
            113   20  124  133   20   52  143   20
             48  213   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2012-08-20T18:43:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x88 0x00    ..t.t...
    decimal
              1    0  116    0  116    0  136    0
    datetime (2012-08-20T18:43:02)
    0000   0x82 0x2b 0x52 0x74 0x0c                   .+Rt.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 BolusWizard 2012-08-20T19:04:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T19:04:13)
    0000   0x8d 0x04 0x13 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 1.45, 'curve': 4},
 {'age': 30, 'amount': 1.45, 'curve': 4},
 {'age': 90, 'amount': 2.2, 'curve': 4},
 {'age': 140, 'amount': 0.9, 'curve': 4},
 {'age': 150, 'amount': 1.1, 'curve': 4},
 {'age': 170, 'amount': 0.15, 'curve': 4},
 {'age': 180, 'amount': 2.05, 'curve': 4},
 {'age': 210, 'amount': 1.4, 'curve': 4},
 {'age': 124, 'amount': 1.25, 'curve': 20},
 {'age': 134, 'amount': 1.75, 'curve': 20},
 {'age': 154, 'amount': 3.1, 'curve': 20},
 {'age': 164, 'amount': 1.3, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x3a 0x14 0x04 0x3a 0x1e 0x04    \&:..:..
    0008   0x58 0x5a 0x04 0x24 0x8c 0x04 0x2c 0x96    XZ.$..,.
    0010   0x04 0x06 0xaa 0x04 0x52 0xb4 0x04 0x38    ....R..8
    0018   0xd2 0x04 0x32 0x7c 0x14 0x46 0x86 0x14    ..2|.F..
    0020   0x7c 0x9a 0x14 0x34 0xa4 0x14              |..4..
    decimal
             92   38   58   20    4   58   30    4
             88   90    4   36  140    4   44  150
              4    6  170    4   82  180    4   56
            210    4   50  124   20   70  134   20
            124  154   20   52  164   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2012-08-20T19:04:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0xd8 0x00    ..H.H...
    decimal
              1    0   72    0   72    0  216    0
    datetime (2012-08-20T19:04:14)
    0000   0x8e 0x04 0x53 0x74 0x0c                   ..St.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2012-08-20T21:41:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T21:41:03)
    0000   0x83 0x29 0x15 0x74 0x0c                   .).t.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 157, 'amount': 1.8, 'curve': 4},
 {'age': 177, 'amount': 1.45, 'curve': 4},
 {'age': 187, 'amount': 1.45, 'curve': 4},
 {'age': 247, 'amount': 2.2, 'curve': 4},
 {'age': 41, 'amount': 0.9, 'curve': 20},
 {'age': 51, 'amount': 1.1, 'curve': 20},
 {'age': 71, 'amount': 0.15, 'curve': 20},
 {'age': 81, 'amount': 2.05, 'curve': 20},
 {'age': 111, 'amount': 1.4, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x48 0x9d 0x04 0x3a 0xb1 0x04    \.H..:..
    0008   0x3a 0xbb 0x04 0x58 0xf7 0x04 0x24 0x29    :..X..$)
    0010   0x14 0x2c 0x33 0x14 0x06 0x47 0x14 0x52    .,3..G.R
    0018   0x51 0x14 0x38 0x6f 0x14                   Q.8o.
    decimal
             92   29   72  157    4   58  177    4
             58  187    4   88  247    4   36   41
             20   44   51   20    6   71   20   82
             81   20   56  111   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2012-08-20T21:41:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x28 0x00    ..P.P.(.
    decimal
              1    0   80    0   80    0   40    0
    datetime (2012-08-20T21:41:03)
    0000   0x83 0x29 0x55 0x74 0x0c                   .)Ut.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2012-08-20T22:15:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T22:15:04)
    0000   0x84 0x0f 0x16 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x13 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x36         D....D6
    decimal
             19  144    0  110   23   54    0    0
             68    0    0    0    0   68   54
    DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 2.0, 'curve': 4},
 {'age': 191, 'amount': 1.8, 'curve': 4},
 {'age': 211, 'amount': 1.45, 'curve': 4},
 {'age': 221, 'amount': 1.45, 'curve': 4},
 {'age': 25, 'amount': 2.2, 'curve': 20},
 {'age': 75, 'amount': 0.9, 'curve': 20},
 {'age': 85, 'amount': 1.1, 'curve': 20},
 {'age': 105, 'amount': 0.15, 'curve': 20},
 {'age': 115, 'amount': 2.05, 'curve': 20},
 {'age': 145, 'amount': 1.4, 'curve': 20}]
```
    op hex (32)
    0000   0x5c 0x20 0x50 0x29 0x04 0x48 0xbf 0x04    \ P).H..
    0008   0x3a 0xd3 0x04 0x3a 0xdd 0x04 0x58 0x19    :..:..X.
    0010   0x14 0x24 0x4b 0x14 0x2c 0x55 0x14 0x06    .$K.,U..
    0018   0x69 0x14 0x52 0x73 0x14 0x38 0x91 0x14    i.Rs.8..
    decimal
             92   32   80   41    4   72  191    4
             58  211    4   58  221    4   88   25
             20   36   75   20   44   85   20    6
            105   20   82  115   20   56  145   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2012-08-20T22:15:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x60 0x00    ..D.D.`.
    decimal
              1    0   68    0   68    0   96    0
    datetime (2012-08-20T22:15:04)
    0000   0x84 0x0f 0x56 0x74 0x0c                   ..Vt.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 19 BolusWizard 2012-08-20T22:25:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 31,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 112}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T22:25:50)
    0000   0xb2 0x19 0x16 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x1f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x70 0x00 0x00 0x00 0x00 0x70 0x36         p....p6
    decimal
             31  144    0  110   23   54    0    0
            112    0    0    0    0  112   54
    DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 1.7, 'curve': 4},
 {'age': 51, 'amount': 2.0, 'curve': 4},
 {'age': 201, 'amount': 1.8, 'curve': 4},
 {'age': 221, 'amount': 1.45, 'curve': 4},
 {'age': 231, 'amount': 1.45, 'curve': 4},
 {'age': 35, 'amount': 2.2, 'curve': 20},
 {'age': 85, 'amount': 0.9, 'curve': 20},
 {'age': 95, 'amount': 1.1, 'curve': 20},
 {'age': 115, 'amount': 0.15, 'curve': 20},
 {'age': 125, 'amount': 2.05, 'curve': 20},
 {'age': 155, 'amount': 1.4, 'curve': 20}]
```
    op hex (35)
    0000   0x5c 0x23 0x44 0x0b 0x04 0x50 0x33 0x04    \#D..P3.
    0008   0x48 0xc9 0x04 0x3a 0xdd 0x04 0x3a 0xe7    H..:..:.
    0010   0x04 0x58 0x23 0x14 0x24 0x55 0x14 0x2c    .X#.$U.,
    0018   0x5f 0x14 0x06 0x73 0x14 0x52 0x7d 0x14    _..s.R}.
    0020   0x38 0x9b 0x14                             8..
    decimal
             92   35   68   11    4   80   51    4
             72  201    4   58  221    4   58  231
              4   88   35   20   36   85   20   44
             95   20    6  115   20   82  125   20
             56  155   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2012-08-20T22:25:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x9c 0x00    ........
    decimal
              1    0  128    0  128    0  156    0
    datetime (2012-08-20T22:25:50)
    0000   0xb2 0x19 0x56 0x74 0x0c                   ..Vt.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 22 Bolus 2012-08-20T22:40:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x01 0x0c 0x00    .. . ...
    decimal
              1    0   32    0   32    1   12    0
    datetime (2012-08-20T22:40:15)
    0000   0x8f 0x28 0x56 0x74 0x0c                   .(Vt.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2012-08-20T23:58:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T23:58:00)
    0000   0x80 0x3a 0x17 0x74 0x0c                   .:.t.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 84, 'amount': 0.8, 'curve': 4},
 {'age': 94, 'amount': 3.2, 'curve': 4},
 {'age': 104, 'amount': 1.7, 'curve': 4},
 {'age': 144, 'amount': 2.0, 'curve': 4},
 {'age': 38, 'amount': 1.8, 'curve': 20},
 {'age': 58, 'amount': 1.45, 'curve': 20},
 {'age': 68, 'amount': 1.45, 'curve': 20},
 {'age': 128, 'amount': 2.2, 'curve': 20},
 {'age': 178, 'amount': 0.9, 'curve': 20},
 {'age': 188, 'amount': 1.1, 'curve': 20},
 {'age': 208, 'amount': 0.15, 'curve': 20},
 {'age': 218, 'amount': 2.05, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x20 0x54 0x04 0x80 0x5e 0x04    \& T..^.
    0008   0x44 0x68 0x04 0x50 0x90 0x04 0x48 0x26    Dh.P..H&
    0010   0x14 0x3a 0x3a 0x14 0x3a 0x44 0x14 0x58    .::.:D.X
    0018   0x80 0x14 0x24 0xb2 0x14 0x2c 0xbc 0x14    ..$..,..
    0020   0x06 0xd0 0x14 0x52 0xda 0x14              ...R..
    decimal
             92   38   32   84    4  128   94    4
             68  104    4   80  144    4   72   38
             20   58   58   20   58   68   20   88
            128   20   36  178   20   44  188   20
              6  208   20   82  218   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2012-08-20T23:58:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xa8 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  168    0
    datetime (2012-08-20T23:58:00)
    0000   0x80 0x3a 0x57 0x74 0x0c                   .:Wt.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 BasalProfileStart 2012-08-21T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-21T00:00:00)
    0000   0x80 0x00 0x00 0x15 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 27 MResultTotals 2012-08-21T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0xed                   .....
    decimal
              7    0    0    9  237
    datetime (2012-08-21T00:00:00)
    0000   0x94 0x0c                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 28 Sara6E 2012-08-21T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2012-08-21T00:00:00)
    0000   0x94 0x0c                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x6c 0x5f 0x7f 0x03 0x00 0x00    ..l_....
    0008   0x09 0xed 0x03 0x89 0x24 0x06 0x64 0x40    ....$.d@
    0010   0x01 0xa4 0x04 0x90 0x00 0x18 0x01 0x9c    ........
    0018   0x00 0x20 0x0e 0x01 0x03 0x01 0x00 0x00    . ......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x67    .......g
    0028   0x67 0x00 0x00 0x00 0x00 0x00 0x00 0x00    g.......
    0030   0x00                                       .
    decimal
              6    0  108   95  127    3    0    0
              9  237    3  137   36    6  100   64
              1  164    4  144    0   24    1  156
              0   32   14    1    3    1    0    0
              0    0    0    0    0    0    0  103
            103    0    0    0    0    0    0    0
              0

#### RECORD 29 BolusWizard 2012-08-21T00:03:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-21T00:03:42)
    0000   0xaa 0x03 0x00 0x75 0x0c                   ...u.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 2.5, 'curve': 4},
 {'age': 89, 'amount': 0.8, 'curve': 4},
 {'age': 99, 'amount': 3.2, 'curve': 4},
 {'age': 109, 'amount': 1.7, 'curve': 4},
 {'age': 149, 'amount': 2.0, 'curve': 4},
 {'age': 43, 'amount': 1.8, 'curve': 20},
 {'age': 63, 'amount': 1.45, 'curve': 20},
 {'age': 73, 'amount': 1.45, 'curve': 20},
 {'age': 133, 'amount': 2.2, 'curve': 20},
 {'age': 183, 'amount': 0.9, 'curve': 20},
 {'age': 193, 'amount': 1.1, 'curve': 20},
 {'age': 213, 'amount': 0.15, 'curve': 20},
 {'age': 223, 'amount': 2.05, 'curve': 20}]
```
    op hex (41)
    0000   0x5c 0x29 0x64 0x09 0x04 0x20 0x59 0x04    \)d.. Y.
    0008   0x80 0x63 0x04 0x44 0x6d 0x04 0x50 0x95    .c.Dm.P.
    0010   0x04 0x48 0x2b 0x14 0x3a 0x3f 0x14 0x3a    .H+.:?.:
    0018   0x49 0x14 0x58 0x85 0x14 0x24 0xb7 0x14    I.X..$..
    0020   0x2c 0xc1 0x14 0x06 0xd5 0x14 0x52 0xdf    ,.....R.
    0028   0x14                                       .
    decimal
             92   41  100    9    4   32   89    4
            128   99    4   68  109    4   80  149
              4   72   43   20   58   63   20   58
             73   20   88  133   20   36  183   20
             44  193   20    6  213   20   82  223
             20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-08-21T00:03:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x01 0x04 0x00    ..d.d...
    decimal
              1    0  100    0  100    1    4    0
    datetime (2012-08-21T00:03:43)
    0000   0xab 0x03 0x40 0x75 0x0c                   ..@u.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 32 CalBGForPH 2012-08-21T03:05:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 362}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2012-08-21T03:05:38)
    0000   0xa6 0x05 0x23 0x75 0x8c                   ..#u.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 Ian3F 2012-08-21T03:05:38 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x2d                                  ?-
    decimal
             63   45
    datetime (2012-08-21T03:05:38)
    0000   0xa6 0x05 0x43 0x75 0x0c                   ..Cu.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 34 BolusWizard 2012-08-21T03:06:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 201,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc9                                  [.
    decimal
             91  201
    datetime (2012-08-21T03:06:27)
    0000   0x9b 0x06 0x03 0x75 0x0c                   ...u.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xfc 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x20 0x00 0xdc 0x36         ... ..6
    decimal
              0  144    0  110   23   54  252    0
              0    0    0   32    0  220   54
    DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 182, 'amount': 2.1, 'curve': 4},
 {'age': 192, 'amount': 2.9, 'curve': 4},
 {'age': 16, 'amount': 0.8, 'curve': 20},
 {'age': 26, 'amount': 3.2, 'curve': 20},
 {'age': 36, 'amount': 1.7, 'curve': 20},
 {'age': 76, 'amount': 2.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x54 0xb6 0x04 0x74 0xc0 0x04    \.T..t..
    0008   0x20 0x10 0x14 0x80 0x1a 0x14 0x44 0x24     .....D$
    0010   0x14 0x50 0x4c 0x14                        .PL.
    decimal
             92   20   84  182    4  116  192    4
             32   16   20  128   26   20   68   36
             20   80   76   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2012-08-21T03:06:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 22.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xdc 0x00 0xdc 0x00 0x20 0x00    ...... .
    decimal
              1    0  220    0  220    0   32    0
    datetime (2012-08-21T03:06:27)
    0000   0x9b 0x06 0x43 0x75 0x0c                   ..Cu.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 37 BasalProfileStart 2012-08-21T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-21T04:00:00)
    0000   0x80 0x00 0x04 0x15 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 38 CalBGForPH 2012-08-21T07:49:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 224}
```
    op hex (2)
    0000   0x0a 0xe0                                  ..
    decimal
             10  224
    datetime (2012-08-21T07:49:42)
    0000   0xaa 0x31 0x27 0x75 0x0c                   .1'u.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 Ian3F 2012-08-21T07:49:42 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1c                                  ?.
    decimal
             63   28
    datetime (2012-08-21T07:49:42)
    0000   0xaa 0x31 0x07 0x75 0x0c                   .1.u.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 BolusWizard 2012-08-21T07:49:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 124,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 12.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7c                                  [|
    decimal
             91  124
    datetime (2012-08-21T07:49:58)
    0000   0xba 0x31 0x07 0x75 0x0c                   .1.u.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x78 0x00    ...n.6x.
    0008   0x00 0x00 0x00 0x00 0x00 0x78 0x36         .....x6
    decimal
              0  144    0  110   23   54  120    0
              0    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 5.5, 'curve': 20},
 {'age': 209, 'amount': 2.1, 'curve': 20},
 {'age': 219, 'amount': 2.9, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xdc 0x1d 0x14 0x54 0xd1 0x14    \....T..
    0008   0x74 0xdb 0x14                             t..
    decimal
             92   11  220   29   20   84  209   20
            116  219   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2012-08-21T07:49:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    0    0
    datetime (2012-08-21T07:49:58)
    0000   0xba 0x31 0x47 0x75 0x0c                   .1Gu.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 BasalProfileStart 2012-08-21T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-21T09:30:00)
    0000   0x80 0x1e 0x09 0x15 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 44 CalBGForPH 2012-08-21T09:46:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2012-08-21T09:46:48)
    0000   0xb0 0x2e 0x29 0x75 0x0c                   ..)u.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 Ian3F 2012-08-21T09:46:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2012-08-21T09:46:48)
    0000   0xb0 0x2e 0x89 0x75 0x0c                   ...u.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 LowReservoir 2012-08-21T10:10:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.0}
```
    op hex (2)
    0000   0x34 0x0a                                  4.
    decimal
             52   10
    datetime (2012-08-21T10:10:00)
    0000   0x80 0x0a 0x0a 0x15 0x8c                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 47 Ian69 2012-08-21T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-21T10:30:00)
    0000   0x80 0x1e 0x0a 0x15 0x0c                   .....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30

#### RECORD 48 BolusWizard 2012-08-21T12:47:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-21T12:47:20)
    0000   0x94 0x2f 0x0c 0x75 0x0c                   ./.u.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 3.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x2f 0x14                   \.x/.
    decimal
             92    5  120   47   20
    datetime (unknown)

    body (0)

#### RECORD 50 Ian69 2012-08-21T12:47:20 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-21T12:47:20)
    0000   0x94 0x2f 0x0c 0x15 0x0c                   ./...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 51 Bolus 2012-08-21T12:47:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2012-08-21T12:47:20)
    0000   0x94 0x2f 0x4c 0x75 0x0c                   ./Lu.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 BasalProfileStart 2012-08-21T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-21T13:00:00)
    0000   0x80 0x00 0x0d 0x15 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 53 BolusWizard 2012-08-21T14:20:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 37,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-21T14:20:06)
    0000   0x86 0x14 0x0e 0x75 0x0c                   ...u.
    body (15)
    hex
    0000   0x25 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    %..n.6..
    0008   0x84 0x00 0x00 0x00 0x00 0x84 0x36         ......6
    decimal
             37  144    0  110   23   54    0    0
            132    0    0    0    0  132   54
    DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 1.8, 'curve': 4},
 {'age': 140, 'amount': 3.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0x60 0x04 0x78 0x8c 0x14    \.H`.x..
    decimal
             92    8   72   96    4  120  140   20
    datetime (unknown)

    body (0)

#### RECORD 55 LowReservoir 2012-08-21T14:20:07 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 9.6}
```
    op hex (2)
    0000   0x34 0x60                                  4`
    decimal
             52   96
    datetime (2012-08-21T14:20:07)
    0000   0x87 0x14 0x6e 0x15 0x8c                   ..n..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 56 Bolus 2012-08-21T14:20:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x2c 0x00    ......,.
    decimal
              1    0  132    0  132    0   44    0
    datetime (2012-08-21T14:20:06)
    0000   0x86 0x14 0x4e 0x75 0x0c                   ..Nu.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 57 CalBGForPH 2012-08-21T18:22:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 361}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2012-08-21T18:22:18)
    0000   0x92 0x16 0x32 0x75 0x8c                   ..2u.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
`end analysis/ianj/raw/ReadHistoryData-page-17.data: 58 records`
