## START logs/ReadHistoryData-page-22.data
#### STOPPING DOUBLE NULLS @ 1012, found 10 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x02 0xec                                  ..
##### DEBUG DECIMAL
              2  236
#### RECORD 0 TempBasal 2013-07-20T01:31:39 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-07-20T01:31:39)
    0000   0x67 0xdf 0x01 0x14 0x0d                   g....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 1 TempBasalDuration 2013-07-20T01:31:39 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-07-20T01:31:39)
    0000   0x67 0xdf 0x01 0x14 0x0d                   g....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BasalProfileStart 2013-07-20T01:31:40 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-20T01:31:40)
    0000   0x68 0xdf 0x01 0x14 0x0d                   h....
    body (3)
    hex
    0000   0x00 0x1f 0x00                             ...
    decimal
              0   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BasalProfileStart 2013-07-20T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-20T04:00:00)
    0000   0x40 0xc0 0x04 0x14 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BasalProfileStart 2013-07-20T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-20T08:00:00)
    0000   0x40 0xc0 0x08 0x14 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BasalProfileStart 2013-07-20T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-20T12:00:00)
    0000   0x40 0xc0 0x0c 0x14 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2013-07-20T14:05:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-07-20T14:05:22)
    0000   0x56 0xc5 0x2e 0x14 0x0d                   V....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 BolusWizard 2013-07-20T14:05:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-07-20T14:05:28)
    0000   0x5c 0xc5 0x0e 0x74 0x0d                   \..t.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x78         D....Dx
    decimal
             21   80    0  120   60  100    0    0
             68    0    0    0    0   68  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 Bolus 2013-07-20T14:05:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2013-07-20T14:05:28)
    0000   0x5c 0xc5 0x4e 0x74 0x0d                   \.Nt.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 CalBGForPH 2013-07-20T15:31:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-07-20T15:31:08)
    0000   0x48 0xdf 0x2f 0x14 0x0d                   H./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 BolusWizard 2013-07-20T15:31:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-07-20T15:31:13)
    0000   0x4d 0xdf 0x0f 0x74 0x0d                   M..t.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x24 0x00 0x00 0x78         ...$..x
    decimal
              0   80    0  120   60  100    0    0
              0    0    0   36    0    0  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 1.7, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0x58 0xc0                   \.DX.
    decimal
             92    5   68   88  192
    datetime (unknown)

    body (0)

#### RECORD 12 BolusWizard 2013-07-20T15:31:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-07-20T15:31:26)
    0000   0x5a 0xdf 0x0f 0x14 0x0d                   Z....
    body (15)
    hex
    0000   0x16 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x48 0x00 0x00 0x24 0x00 0x48 0x78         H..$.Hx
    decimal
             22   80    0  120   60  100    0    0
             72    0    0   36    0   72  120
    HOUR BITS: [1, 1, 0]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 1.7, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0x58 0xc0                   \.DX.
    decimal
             92    5   68   88  192
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-07-20T15:31:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x24 0x00    ..H.H.$.
    decimal
              1    0   72    0   72    0   36    0
    datetime (2013-07-20T15:31:26)
    0000   0x5a 0xdf 0x4f 0x14 0x0d                   Z.O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2013-07-20T17:50:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-07-20T17:50:02)
    0000   0x42 0xf2 0x31 0x14 0x0d                   B.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 16 BolusWizard 2013-07-20T17:50:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 124,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x7c                                  [|
    decimal
             91  124
    datetime (2013-07-20T17:50:07)
    0000   0x47 0xf2 0x11 0x74 0x0d                   G..t.
    body (15)
    hex
    0000   0x12 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x48 0x00 0x00 0x0c 0x00 0x48 0x78         H....Hx
    decimal
             18   80    0  100   60  100    0    0
             72    0    0   12    0   72  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 147, 'amount': 1.8, 'curve': 192},
 {'age': 227, 'amount': 1.7, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0x93 0xc0 0x44 0xe3 0xc0    \.H..D..
    decimal
             92    8   72  147  192   68  227  192
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-07-20T17:50:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x0c 0x00    ..H.H...
    decimal
              1    0   72    0   72    0   12    0
    datetime (2013-07-20T17:50:07)
    0000   0x47 0xf2 0x51 0x74 0x0d                   G.Qt.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 CalBGForPH 2013-07-20T19:41:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-07-20T19:41:51)
    0000   0x73 0xe9 0x33 0x14 0x0d                   s.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 BolusWizard 2013-07-20T19:41:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 112}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-07-20T19:41:59)
    0000   0x7b 0xe9 0x13 0x74 0x0d                   {..t.
    body (15)
    hex
    0000   0x1c 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x70 0x00 0x00 0x14 0x00 0x70 0x78         p....px
    decimal
             28   80    0  100   60  100    0    0
            112    0    0   20    0  112  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 118, 'amount': 1.8, 'curve': 192},
 {'age': 2, 'amount': 1.8, 'curve': 208},
 {'age': 82, 'amount': 1.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x76 0xc0 0x48 0x02 0xd0    \.Hv.H..
    0008   0x44 0x52 0xd0                             DR.
    decimal
             92   11   72  118  192   72    2  208
             68   82  208
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-07-20T19:41:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x14 0x00    ..p.p...
    decimal
              1    0  112    0  112    0   20    0
    datetime (2013-07-20T19:41:59)
    0000   0x7b 0xe9 0x53 0x74 0x0d                   {.St.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 CalBGForPH 2013-07-20T20:27:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-07-20T20:27:41)
    0000   0x69 0xdb 0x34 0x14 0x0d                   i.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 BolusWizard 2013-07-20T20:27:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 9.6,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-07-20T20:27:50)
    0000   0x72 0xdb 0x14 0x74 0x0d                   r..t.
    body (15)
    hex
    0000   0x13 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x4c 0x00 0x00 0x60 0x00 0x4c 0x78         L..`.Lx
    decimal
             19   80    0  100   60  100    0    0
             76    0    0   96    0   76  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 1.25, 'curve': 192},
 {'age': 54, 'amount': 1.55, 'curve': 192},
 {'age': 164, 'amount': 1.8, 'curve': 192},
 {'age': 48, 'amount': 1.8, 'curve': 208},
 {'age': 128, 'amount': 1.7, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x32 0x2c 0xc0 0x3e 0x36 0xc0    \.2,.>6.
    0008   0x48 0xa4 0xc0 0x48 0x30 0xd0 0x44 0x80    H..H0.D.
    0010   0xd0                                       .
    decimal
             92   17   50   44  192   62   54  192
             72  164  192   72   48  208   68  128
            208
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-07-20T20:27:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x60 0x00    ..L.L.`.
    decimal
              1    0   76    0   76    0   96    0
    datetime (2013-07-20T20:27:50)
    0000   0x72 0xdb 0x54 0x74 0x0d                   r.Tt.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 BasalProfileStart 2013-07-21T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-21T00:00:00)
    0000   0x40 0xc0 0x00 0x15 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1f 0x00                             ...
    decimal
              0   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 28 ResultTotals (2000, 6, 0, 0, 13, 52) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x72                   ....r
    decimal
              7    0    0    4  114
    datetime ((2000, 6, 0, 0, 13, 52))
    0000   0x74 0x8d 0x00 0x00 0x00                   t....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x74 0x8d 0x05 0x00 0x71 0x00 0x00    nt...q..
    0008   0x05 0x00 0x00 0x04 0x72 0x02 0xe2 0x41    ....r..A
    0010   0x01 0x90 0x23 0x00 0x6c 0x01 0x90 0x00    ..#.l...
    0018   0x00 0x00 0x00 0x00 0x00 0x05 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0x7c 0x00 0x00 0x00         ..d|...
    decimal
            110  116  141    5    0  113    0    0
              5    0    0    4  114    2  226   65
              1  144   35    0  108    1  144    0
              0    0    0    0    0    5    0    0
              0    0    0    0    0    0    0    0
              0    0  100  124    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 30 BasalProfileStart 2013-07-21T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-21T04:00:00)
    0000   0x40 0xc0 0x04 0x15 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 31 BasalProfileStart 2013-07-21T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-21T08:00:00)
    0000   0x40 0xc0 0x08 0x15 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 32 CalBGForPH 2013-07-21T09:52:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-07-21T09:52:56)
    0000   0x78 0xf4 0x29 0x15 0x0d                   x.)..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 BolusWizard 2013-07-21T09:53:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 122,
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
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-07-21T09:53:18)
    0000   0x52 0xf5 0x09 0x75 0x0d                   R..u.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0    0    0   64  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 Bolus 2013-07-21T09:53:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-07-21T09:53:18)
    0000   0x52 0xf5 0x49 0x75 0x0d                   R.Iu.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 35 CalBGForPH 2013-07-21T11:03:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-07-21T11:03:17)
    0000   0x51 0xc3 0x2b 0x15 0x0d                   Q.+..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 BolusWizard 2013-07-21T11:03:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-07-21T11:03:26)
    0000   0x5a 0xc3 0x0b 0x75 0x0d                   Z..u.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x30 0x00    .P.x<d0.
    0008   0x00 0x00 0x00 0x28 0x00 0x08 0x78         ...(..x
    decimal
              0   80    0  120   60  100   48    0
              0    0    0   40    0    8  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 70, 'amount': 1.6, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x46 0xc0                   \.@F.
    decimal
             92    5   64   70  192
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-07-21T11:03:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x08 0x00 0x08 0x00 0x28 0x00    ......(.
    decimal
              1    0    8    0    8    0   40    0
    datetime (2013-07-21T11:03:26)
    0000   0x5a 0xc3 0x4b 0x75 0x0d                   Z.Ku.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 CalBGForPH 2013-07-21T11:18:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2013-07-21T11:18:43)
    0000   0x6b 0xd2 0x2b 0x15 0x0d                   k.+..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 40 BolusWizard 2013-07-21T11:18:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 127,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x7f                                  [.
    decimal
             91  127
    datetime (2013-07-21T11:18:51)
    0000   0x73 0xd2 0x0b 0x15 0x0d                   s....
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x04 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x28 0x00 0x28 0x78         (..(.(x
    decimal
             12   80    0  120   60  100    4    0
             40    0    0   40    0   40  120
    HOUR BITS: [1, 1, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 0.2, 'curve': 192},
 {'age': 85, 'amount': 1.6, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x08 0x0f 0xc0 0x40 0x55 0xc0    \....@U.
    decimal
             92    8    8   15  192   64   85  192
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-07-21T11:18:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x28 0x00    ..(.(.(.
    decimal
              1    0   40    0   40    0   40    0
    datetime (2013-07-21T11:18:51)
    0000   0x73 0xd2 0x4b 0x15 0x0d                   s.K..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 43 BasalProfileStart 2013-07-21T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-21T12:00:00)
    0000   0x40 0xc0 0x0c 0x15 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 44 CalBGForPH 2013-07-21T12:33:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 226}
```
    op hex (2)
    0000   0x0a 0xe2                                  ..
    decimal
             10  226
    datetime (2013-07-21T12:33:32)
    0000   0x60 0xe1 0x2c 0x15 0x0d                   `.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BolusWizard 2013-07-21T12:33:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 226,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe2                                  [.
    decimal
             91  226
    datetime (2013-07-21T12:33:35)
    0000   0x63 0xe1 0x0c 0x75 0x0d                   c..u.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x44 0x00    .P.x<dD.
    0008   0x00 0x00 0x00 0x20 0x00 0x24 0x78         ... .$x
    decimal
              0   80    0  120   60  100   68    0
              0    0    0   32    0   36  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 80, 'amount': 1.0, 'curve': 192},
 {'age': 90, 'amount': 0.2, 'curve': 192},
 {'age': 160, 'amount': 1.6, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x50 0xc0 0x08 0x5a 0xc0    \.(P..Z.
    0008   0x40 0xa0 0xc0                             @..
    decimal
             92   11   40   80  192    8   90  192
             64  160  192
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-07-21T12:33:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x20 0x00    ..$.$. .
    decimal
              1    0   36    0   36    0   32    0
    datetime (2013-07-21T12:33:35)
    0000   0x63 0xe1 0x4c 0x75 0x0d                   c.Lu.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 CalBGForPH 2013-07-21T12:52:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-07-21T12:52:47)
    0000   0x6f 0xf4 0x2c 0x15 0x0d                   o.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 BolusWizard 2013-07-21T12:52:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 128,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-07-21T12:52:57)
    0000   0x79 0xf4 0x0c 0x75 0x0d                   y..u.
    body (15)
    hex
    0000   0x17 0x50 0x00 0x78 0x3c 0x64 0x04 0x00    .P.x<d..
    0008   0x4c 0x00 0x00 0x38 0x00 0x4c 0x78         L..8.Lx
    decimal
             23   80    0  120   60  100    4    0
             76    0    0   56    0   76  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 0.9, 'curve': 192},
 {'age': 99, 'amount': 1.0, 'curve': 192},
 {'age': 109, 'amount': 0.2, 'curve': 192},
 {'age': 179, 'amount': 1.6, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0x24 0x13 0xc0 0x28 0x63 0xc0    \.$..(c.
    0008   0x08 0x6d 0xc0 0x40 0xb3 0xc0              .m.@..
    decimal
             92   14   36   19  192   40   99  192
              8  109  192   64  179  192
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-07-21T12:52:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x38 0x00    ..L.L.8.
    decimal
              1    0   76    0   76    0   56    0
    datetime (2013-07-21T12:52:57)
    0000   0x79 0xf4 0x4c 0x75 0x0d                   y.Lu.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 CalBGForPH 2013-07-21T15:24:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-07-21T15:24:38)
    0000   0x66 0xd8 0x2f 0x15 0x0d                   f./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 BolusWizard 2013-07-21T15:24:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
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
    datetime (2013-07-21T15:24:43)
    0000   0x6b 0xd8 0x0f 0x75 0x0d                   k..u.
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x0c 0x00 0x28 0x78         (....(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0   12    0   40  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 151, 'amount': 1.8, 'curve': 192},
 {'age': 161, 'amount': 0.1, 'curve': 192},
 {'age': 171, 'amount': 0.9, 'curve': 192},
 {'age': 251, 'amount': 1.0, 'curve': 192},
 {'age': 5, 'amount': 0.2, 'curve': 208},
 {'age': 75, 'amount': 1.6, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x97 0xc0 0x04 0xa1 0xc0    \.H.....
    0008   0x24 0xab 0xc0 0x28 0xfb 0xc0 0x08 0x05    $..(....
    0010   0xd0 0x40 0x4b 0xd0                        .@K.
    decimal
             92   20   72  151  192    4  161  192
             36  171  192   40  251  192    8    5
            208   64   75  208
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-07-21T15:24:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x0c 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   12    0
    datetime (2013-07-21T15:24:43)
    0000   0x6b 0xd8 0x4f 0x75 0x0d                   k.Ou.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 56 CalBGForPH 2013-07-21T21:30:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-07-21T21:30:11)
    0000   0x4b 0xde 0x35 0x15 0x0d                   K.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 57 BolusWizard 2013-07-21T21:30:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 110,
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
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-07-21T21:30:33)
    0000   0x61 0xde 0x15 0x75 0x0d                   a..u.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x78         T....Tx
    decimal
             21   80    0  100   60  100    0    0
             84    0    0    0    0   84  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 1.0, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x6f 0xd0                   \.(o.
    decimal
             92    5   40  111  208
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-07-21T21:30:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x00 0x00    ..T.T...
    decimal
              1    0   84    0   84    0    0    0
    datetime (2013-07-21T21:30:33)
    0000   0x61 0xde 0x55 0x75 0x0d                   a.Uu.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 BasalProfileStart 2013-07-22T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-22T00:00:00)
    0000   0x40 0xc0 0x00 0x16 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1f 0x00                             ...
    decimal
              0   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 61 ResultTotals (2000, 6, 0, 0, 13, 53) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x40                   ....@
    decimal
              7    0    0    4   64
    datetime ((2000, 6, 0, 0, 13, 53))
    0000   0x75 0x8d 0x00 0x00 0x00                   u....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x75 0x8d 0x05 0x00 0x91 0x00 0x00    nu......
    0008   0x07 0x00 0x00 0x04 0x40 0x02 0xe4 0x44    ....@..D
    0010   0x01 0x5c 0x20 0x00 0x59 0x01 0x30 0x00    .\ .Y.0.
    0018   0x2c 0x00 0x00 0x00 0x00 0x05 0x02 0x00    ,.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6e 0xe2 0x00 0x00 0x00         ..n....
    decimal
            110  117  141    5    0  145    0    0
              7    0    0    4   64    2  228   68
              1   92   32    0   89    1   48    0
             44    0    0    0    0    5    2    0
              0    0    0    0    0    0    0    0
              0    0  110  226    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 63 BasalProfileStart 2013-07-22T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-22T04:00:00)
    0000   0x40 0xc0 0x04 0x16 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 64 BasalProfileStart 2013-07-22T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-22T08:00:00)
    0000   0x40 0xc0 0x08 0x16 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 65 CalBGForPH 2013-07-22T09:11:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-07-22T09:11:15)
    0000   0x4f 0xcb 0x29 0x16 0x0d                   O.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 66 BolusWizard 2013-07-22T09:11:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 128,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-07-22T09:11:23)
    0000   0x57 0xcb 0x09 0x76 0x0d                   W..v.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x78 0x3c 0x64 0x04 0x00    .P.x<d..
    0008   0x48 0x00 0x00 0x00 0x00 0x4c 0x78         H....Lx
    decimal
             22   80    0  120   60  100    4    0
             72    0    0    0    0   76  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 67 Bolus 2013-07-22T09:11:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x00 0x00    ..L.L...
    decimal
              1    0   76    0   76    0    0    0
    datetime (2013-07-22T09:11:23)
    0000   0x57 0xcb 0x49 0x76 0x0d                   W.Iv.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 CalBGForPH 2013-07-22T10:21:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-07-22T10:21:25)
    0000   0x59 0xd5 0x2a 0x16 0x0d                   Y.*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 69 BolusWizard 2013-07-22T10:21:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 6,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 20}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-07-22T10:21:36)
    0000   0x64 0xd5 0x0a 0x76 0x0d                   d..v.
    body (15)
    hex
    0000   0x06 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x14 0x00 0x00 0x2c 0x00 0x14 0x78         ...,..x
    decimal
              6   80    0  120   60  100    0    0
             20    0    0   44    0   20  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 78, 'amount': 1.9, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x4c 0x4e 0xc0                   \.LN.
    decimal
             92    5   76   78  192
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-07-22T10:21:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x2c 0x00    ......,.
    decimal
              1    0   20    0   20    0   44    0
    datetime (2013-07-22T10:21:36)
    0000   0x64 0xd5 0x4a 0x76 0x0d                   d.Jv.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 72 BolusWizard 2013-07-22T10:47:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
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
    datetime (2013-07-22T10:47:07)
    0000   0x47 0xef 0x0a 0x76 0x0d                   G..v.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0  120   60  100    0    0
              0    0    0    0    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 0.5, 'curve': 192},
 {'age': 104, 'amount': 1.9, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x22 0xc0 0x4c 0x68 0xc0    \..".Lh.
    decimal
             92    8   20   34  192   76  104  192
    datetime (unknown)

    body (0)

#### RECORD 74 CalBGForPH 2013-07-22T10:57:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 205}
```
    op hex (2)
    0000   0x0a 0xcd                                  ..
    decimal
             10  205
    datetime (2013-07-22T10:57:53)
    0000   0x75 0xf9 0x2a 0x16 0x0d                   u.*..
    body (0)
    HOUR BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-22.data: 75 records`
