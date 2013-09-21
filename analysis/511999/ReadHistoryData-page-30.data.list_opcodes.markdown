## START analysis/sarak/raw//ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 1010, found 12 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x30 0xec                                  0.
##### DEBUG DECIMAL
             48  236
#### RECORD 0 BasalProfileStart 2013-07-09T17:45:32 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-09T17:45:32)
    0000   0x60 0xed 0x11 0x09 0x0d                   `....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 1]
#### RECORD 1 Prime 2013-07-09T17:45:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2013-07-09T17:45:18)
    0000   0x52 0xed 0x11 0x09 0x0d                   R....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 TempBasal 2013-07-09T21:14:34 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.1}
```
    op hex (2)
    0000   0x33 0x54                                  3T
    decimal
             51   84
    datetime (2013-07-09T21:14:34)
    0000   0x62 0xce 0x15 0x09 0x0d                   b....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 3 TempBasalDuration 2013-07-09T21:14:34 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 240}
```
    op hex (2)
    0000   0x16 0x08                                  ..
    decimal
             22    8
    datetime (2013-07-09T21:14:34)
    0000   0x62 0xce 0x15 0x09 0x0d                   b....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-09T23:47:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 221}
```
    op hex (2)
    0000   0x0a 0xdd                                  ..
    decimal
             10  221
    datetime (2013-07-09T23:47:35)
    0000   0x63 0xef 0x37 0x09 0x0d                   c.7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 BolusWizard 2013-07-09T23:47:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 221,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdd                                  [.
    decimal
             91  221
    datetime (2013-07-09T23:47:38)
    0000   0x66 0xef 0x17 0x69 0x0d                   f..i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x40 0x00    .P.d<d@.
    0008   0x00 0x00 0x00 0x00 0x00 0x40 0x78         .....@x
    decimal
              0   80    0  100   60  100   64    0
              0    0    0    0    0   64  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 208, 'amount': 2.5, 'curve': 208},
 {'age': 218, 'amount': 1.4, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0xd0 0xd0 0x38 0xda 0xd0    \.d..8..
    decimal
             92    8  100  208  208   56  218  208
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-07-09T23:47:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-07-09T23:47:38)
    0000   0x66 0xef 0x57 0x69 0x0d                   f.Wi.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 MResultTotals 2013-07-10T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xa3                   .....
    decimal
              7    0    0    7  163
    datetime (2013-07-10T00:00:00)
    0000   0x69 0x8d                                  i.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 9 Sara6E 2013-07-10T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-07-10T00:00:00)
    0000   0x69 0x8d                                  i.
    body (49)
    hex
    0000   0x05 0x00 0xac 0x00 0x00 0x0c 0x00 0x00    ........
    0008   0x07 0xa3 0x04 0xe3 0x40 0x02 0xc0 0x24    ....@..$
    0010   0x00 0x68 0x01 0x70 0x01 0x50 0x00 0x00    .h.p.P..
    0018   0x00 0x00 0x06 0x05 0x00 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x66    .......f
    0028   0x66 0x00 0x00 0x00 0x00 0x00 0x00 0x00    f.......
    0030   0x00                                       .
    decimal
              5    0  172    0    0   12    0    0
              7  163    4  227   64    2  192   36
              0  104    1  112    1   80    0    0
              0    0    6    5    0    0    4    0
              0    0    0    0    0    0    0  102
            102    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 10 TempBasal 2013-07-10T00:00:26 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-07-10T00:00:26)
    0000   0x5a 0xc0 0x00 0x0a 0x0d                   Z....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 11 TempBasalDuration 2013-07-10T00:00:26 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-07-10T00:00:26)
    0000   0x5a 0xc0 0x00 0x0a 0x0d                   Z....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 BasalProfileStart 2013-07-10T00:00:26 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-10T00:00:26)
    0000   0x5a 0xc0 0x00 0x0a 0x0d                   Z....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 0]
#### RECORD 13 BasalProfileStart 2013-07-10T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-10T04:00:00)
    0000   0x40 0xc0 0x04 0x0a 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 14 BasalProfileStart 2013-07-10T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-10T08:00:00)
    0000   0x40 0xc0 0x08 0x0a 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2013-07-10T10:26:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-07-10T10:26:42)
    0000   0x6a 0xda 0x2a 0x0a 0x0d                   j.*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 16 BolusWizard 2013-07-10T10:27:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 106,
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
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-07-10T10:27:06)
    0000   0x46 0xdb 0x0a 0x6a 0x0d                   F..j.
    body (15)
    hex
    0000   0x12 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x3c 0x00 0x00 0x00 0x00 0x3c 0x78         <....<x
    decimal
             18   80    0  120   60  100    0    0
             60    0    0    0    0   60  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 Bolus 2013-07-10T10:27:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2013-07-10T10:27:06)
    0000   0x46 0xdb 0x4a 0x6a 0x0d                   F.Jj.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 BasalProfileStart 2013-07-10T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-10T12:00:00)
    0000   0x40 0xc0 0x0c 0x0a 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 19 CalBGForPH 2013-07-10T15:16:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-07-10T15:16:42)
    0000   0x6a 0xd0 0x2f 0x0a 0x0d                   j./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 BolusWizard 2013-07-10T15:16:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 104,
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
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-07-10T15:16:50)
    0000   0x72 0xd0 0x0f 0x6a 0x0d                   r..j.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x78         D....Dx
    decimal
             21   80    0  120   60  100    0    0
             68    0    0    0    0   68  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 1.5, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x25 0xd0                   \.<%.
    decimal
             92    5   60   37  208
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-07-10T15:16:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2013-07-10T15:16:50)
    0000   0x72 0xd0 0x4f 0x6a 0x0d                   r.Oj.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 CalBGForPH 2013-07-10T18:33:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-07-10T18:33:52)
    0000   0x74 0xe1 0x32 0x0a 0x0d                   t.2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 BolusWizard 2013-07-10T18:33:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 110,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-07-10T18:33:58)
    0000   0x7a 0xe1 0x12 0x6a 0x0d                   z..j.
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x78         4....4x
    decimal
             13   80    0  100   60  100    0    0
             52    0    0    0    0   52  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 200, 'amount': 1.7, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0xc8 0xc0                   \.D..
    decimal
             92    5   68  200  192
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-07-10T18:33:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    0    0
    datetime (2013-07-10T18:33:58)
    0000   0x7a 0xe1 0x52 0x6a 0x0d                   z.Rj.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 27 CalBGForPH 2013-07-10T22:09:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-07-10T22:09:52)
    0000   0x74 0xc9 0x36 0x0a 0x0d                   t.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 BolusWizard 2013-07-10T22:10:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-07-10T22:10:02)
    0000   0x42 0xca 0x16 0x6a 0x0d                   B..j.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x78         X....Xx
    decimal
             22   80    0  100   60  100    0    0
             88    0    0    0    0   88  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 1.3, 'curve': 192},
 {'age': 161, 'amount': 1.7, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0xd9 0xc0 0x44 0xa1 0xd0    \.4..D..
    decimal
             92    8   52  217  192   68  161  208
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-07-10T22:10:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    0    0
    datetime (2013-07-10T22:10:02)
    0000   0x42 0xca 0x56 0x6a 0x0d                   B.Vj.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 BasalProfileStart 2013-07-11T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-11T00:00:00)
    0000   0x40 0xc0 0x00 0x0b 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 0]
#### RECORD 32 MResultTotals 2013-07-11T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xe0                   .....
    decimal
              7    0    0    3  224
    datetime (2013-07-11T00:00:00)
    0000   0x6a 0x8d                                  j.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 33 Sara6E 2013-07-11T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-07-11T00:00:00)
    0000   0x6a 0x8d                                  j.
    body (49)
    hex
    0000   0x05 0x00 0x6b 0x00 0x00 0x04 0x00 0x00    ..k.....
    0008   0x03 0xe0 0x02 0xd4 0x49 0x01 0x0c 0x1b    ....I...
    0010   0x00 0x4a 0x01 0x0c 0x00 0x00 0x00 0x00    .J......
    0018   0x00 0x00 0x04 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x68    .......h
    0028   0x6e 0x00 0x00 0x00 0x00 0x00 0x00 0x00    n.......
    0030   0x00                                       .
    decimal
              5    0  107    0    0    4    0    0
              3  224    2  212   73    1   12   27
              0   74    1   12    0    0    0    0
              0    0    4    0    0    0    0    0
              0    0    0    0    0    0    0  104
            110    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 34 BasalProfileStart 2013-07-11T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-11T04:00:00)
    0000   0x40 0xc0 0x04 0x0b 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 35 BasalProfileStart 2013-07-11T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-11T08:00:00)
    0000   0x40 0xc0 0x08 0x0b 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 36 CalBGForPH 2013-07-11T09:05:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-07-11T09:05:47)
    0000   0x6f 0xc5 0x29 0x0b 0x0d                   o.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 BolusWizard 2013-07-11T09:05:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-07-11T09:05:55)
    0000   0x77 0xc5 0x09 0x6b 0x0d                   w..k.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x40 0x00 0x00 0x00 0x00 0x6c 0x78         @....lx
    decimal
             20   80    0  120   60  100   44    0
             64    0    0    0    0  108  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 Bolus 2013-07-11T09:05:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-07-11T09:05:55)
    0000   0x77 0xc5 0x49 0x6b 0x0d                   w.Ik.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 BasalProfileStart 2013-07-11T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-11T12:00:00)
    0000   0x40 0xc0 0x0c 0x0b 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 40 CalBGForPH 2013-07-11T16:13:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-07-11T16:13:13)
    0000   0x4d 0xcd 0x30 0x0b 0x0d                   M.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 41 BolusWizard 2013-07-11T16:13:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 206,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xce                                  [.
    decimal
             91  206
    datetime (2013-07-11T16:13:17)
    0000   0x51 0xcd 0x10 0x6b 0x0d                   Q..k.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x38 0x00    .P.x<d8.
    0008   0x00 0x00 0x00 0x00 0x00 0x38 0x78         .....8x
    decimal
              0   80    0  120   60  100   56    0
              0    0    0    0    0   56  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 174, 'amount': 2.7, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0xae 0xd0                   \.l..
    decimal
             92    5  108  174  208
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-07-11T16:13:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-07-11T16:13:17)
    0000   0x51 0xcd 0x50 0x6b 0x0d                   Q.Pk.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 44 CalBGForPH 2013-07-11T19:38:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 191}
```
    op hex (2)
    0000   0x0a 0xbf                                  ..
    decimal
             10  191
    datetime (2013-07-11T19:38:25)
    0000   0x59 0xe6 0x33 0x0b 0x0d                   Y.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BolusWizard 2013-07-11T19:38:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 191,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbf                                  [.
    decimal
             91  191
    datetime (2013-07-11T19:38:34)
    0000   0x62 0xe6 0x13 0x6b 0x0d                   b..k.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x2c 0x00    .P.d<d,.
    0008   0x00 0x00 0x00 0x00 0x00 0x2c 0x78         .....,x
    decimal
              0   80    0  100   60  100   44    0
              0    0    0    0    0   44  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 205, 'amount': 1.4, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0xcd 0xc0                   \.8..
    decimal
             92    5   56  205  192
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-07-11T19:38:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x00 0x00    ..,.,...
    decimal
              1    0   44    0   44    0    0    0
    datetime (2013-07-11T19:38:34)
    0000   0x62 0xe6 0x53 0x6b 0x0d                   b.Sk.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 CalBGForPH 2013-07-11T19:56:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 201}
```
    op hex (2)
    0000   0x0a 0xc9                                  ..
    decimal
             10  201
    datetime (2013-07-11T19:56:37)
    0000   0x65 0xf8 0x33 0x0b 0x0d                   e.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 BolusWizard 2013-07-11T19:56:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 201,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
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
    datetime (2013-07-11T19:56:40)
    0000   0x68 0xf8 0x13 0x6b 0x0d                   h..k.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x34 0x00    .P.d<d4.
    0008   0x00 0x00 0x00 0x2c 0x00 0x08 0x78         ...,..x
    decimal
              0   80    0  100   60  100   52    0
              0    0    0   44    0    8  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 1.1, 'curve': 192},
 {'age': 223, 'amount': 1.4, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x17 0xc0 0x38 0xdf 0xc0    \.,..8..
    decimal
             92    8   44   23  192   56  223  192
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-07-11T19:56:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x08 0x00 0x08 0x00 0x2c 0x00    ......,.
    decimal
              1    0    8    0    8    0   44    0
    datetime (2013-07-11T19:56:40)
    0000   0x68 0xf8 0x53 0x6b 0x0d                   h.Sk.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 BasalProfileStart 2013-07-12T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-12T00:00:00)
    0000   0x40 0xc0 0x00 0x0c 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 0]
#### RECORD 53 MResultTotals 2013-07-12T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xac                   .....
    decimal
              7    0    0    3  172
    datetime (2013-07-12T00:00:00)
    0000   0x6b 0x8d                                  k.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 54 Sara6E 2013-07-12T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-07-12T00:00:00)
    0000   0x6b 0x8d                                  k.
    body (49)
    hex
    0000   0x05 0x00 0xc4 0x00 0x00 0x04 0x00 0x00    ........
    0008   0x03 0xac 0x02 0xd4 0x4d 0x00 0xd8 0x17    ....M...
    0010   0x00 0x14 0x00 0x00 0x00 0x6c 0x00 0x6c    .....l.l
    0018   0x00 0x00 0x00 0x03 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xba    ........
    0028   0xce 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  196    0    0    4    0    0
              3  172    2  212   77    0  216   23
              0   20    0    0    0  108    0  108
              0    0    0    3    1    0    0    0
              0    0    0    0    0    0    0  186
            206    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 55 BasalProfileStart 2013-07-12T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-12T04:00:00)
    0000   0x40 0xc0 0x04 0x0c 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 56 BasalProfileStart 2013-07-12T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-12T08:00:00)
    0000   0x40 0xc0 0x08 0x0c 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 57 BasalProfileStart 2013-07-12T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-12T12:00:00)
    0000   0x40 0xc0 0x0c 0x0c 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 58 CalBGForPH 2013-07-12T13:16:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-07-12T13:16:20)
    0000   0x54 0xd0 0x2d 0x0c 0x0d                   T.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 BolusWizard 2013-07-12T13:16:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
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
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-07-12T13:16:36)
    0000   0x64 0xd0 0x0d 0x6c 0x0d                   d..l.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0  120   60  100    0    0
              0    0    0    0    0    0  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 BolusWizard 2013-07-12T13:17:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
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
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-07-12T13:17:07)
    0000   0x47 0xd1 0x0d 0x6c 0x0d                   G..l.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x78         D....Dx
    decimal
             21   80    0  120   60  100    0    0
             68    0    0    0    0   68  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 61 Bolus 2013-07-12T13:17:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2013-07-12T13:17:07)
    0000   0x47 0xd1 0x4d 0x6c 0x0d                   G.Ml.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 CalBGForPH 2013-07-12T16:11:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 274}
```
    op hex (2)
    0000   0x0a 0x12                                  ..
    decimal
             10   18
    datetime (2013-07-12T16:11:28)
    0000   0x5c 0xcb 0x30 0x0c 0x8d                   \.0..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 63 BolusWizard 2013-07-12T16:11:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 274,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x12                                  [.
    decimal
             91   18
    datetime (2013-07-12T16:11:31)
    0000   0x5f 0xcb 0x10 0x6c 0x0d                   _..l.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x64 0x00    .Q.x<dd.
    0008   0x00 0x00 0x00 0x04 0x00 0x60 0x78         .....`x
    decimal
              0   81    0  120   60  100  100    0
              0    0    0    4    0   96  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 178, 'amount': 1.7, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0xb2 0xc0                   \.D..
    decimal
             92    5   68  178  192
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-07-12T16:11:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x04 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    4    0
    datetime (2013-07-12T16:11:31)
    0000   0x5f 0xcb 0x50 0x6c 0x0d                   _.Pl.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 CalBGForPH 2013-07-12T17:52:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-07-12T17:52:01)
    0000   0x41 0xf4 0x31 0x0c 0x0d                   A.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 BolusWizard 2013-07-12T17:52:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 104,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
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
    datetime (2013-07-12T17:52:07)
    0000   0x47 0xf4 0x11 0x6c 0x0d                   G..l.
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0x20 0x00 0x38 0x78         8.. .8x
    decimal
             14   80    0  100   60  100    0    0
             56    0    0   32    0   56  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 99, 'amount': 0.2, 'curve': 192},
 {'age': 109, 'amount': 2.2, 'curve': 192},
 {'age': 23, 'amount': 1.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x08 0x63 0xc0 0x58 0x6d 0xc0    \..c.Xm.
    0008   0x44 0x17 0xd0                             D..
    decimal
             92   11    8   99  192   88  109  192
             68   23  208
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-07-12T17:52:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x20 0x00    ..8.8. .
    decimal
              1    0   56    0   56    0   32    0
    datetime (2013-07-12T17:52:07)
    0000   0x47 0xf4 0x51 0x6c 0x0d                   G.Ql.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 CalBGForPH 2013-07-12T19:18:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-07-12T19:18:53)
    0000   0x75 0xd2 0x33 0x0c 0x0d                   u.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 71 BolusWizard 2013-07-12T19:18:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 146,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.4,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 1.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x92                                  [.
    decimal
             91  146
    datetime (2013-07-12T19:18:59)
    0000   0x7b 0xd2 0x13 0x6c 0x0d                   {..l.
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x64 0x3c 0x64 0x10 0x00    .P.d<d..
    0008   0x2c 0x00 0x00 0x18 0x00 0x2c 0x78         ,....,x
    decimal
             11   80    0  100   60  100   16    0
             44    0    0   24    0   44  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 0.05, 'curve': 192},
 {'age': 95, 'amount': 1.35, 'curve': 192},
 {'age': 185, 'amount': 0.2, 'curve': 192},
 {'age': 195, 'amount': 2.2, 'curve': 192},
 {'age': 109, 'amount': 1.7, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x02 0x55 0xc0 0x36 0x5f 0xc0    \..U.6_.
    0008   0x08 0xb9 0xc0 0x58 0xc3 0xc0 0x44 0x6d    ...X..Dm
    0010   0xd0                                       .
    decimal
             92   17    2   85  192   54   95  192
              8  185  192   88  195  192   68  109
            208
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-07-12T19:18:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x18 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   24    0
    datetime (2013-07-12T19:18:59)
    0000   0x7b 0xd2 0x53 0x6c 0x0d                   {.Sl.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 74 CalBGForPH 2013-07-12T19:53:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-07-12T19:53:09)
    0000   0x49 0xf5 0x33 0x0c 0x0d                   I.3..
    body (0)
    HOUR BITS: [1, 1, 1]
`end analysis/sarak/raw//ReadHistoryData-page-30.data: 75 records`
