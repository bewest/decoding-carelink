## START logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 1015, found 7 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xd1 0x07                                  ..
##### DEBUG DECIMAL
            209    7
#### RECORD 0 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 1.45, 'curve': 192},
 {'age': 71, 'amount': 1.25, 'curve': 192},
 {'age': 155, 'amount': 1.6, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3a 0x3d 0xc0 0x32 0x47 0xc0    \.:=.2G.
    0008   0x40 0x9b 0xd0                             @..
    decimal
             92   11   58   61  192   50   71  192
             64  155  208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-07-24T22:54:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x48 0x00    ..D.D.H.
    decimal
              1    0   68    0   68    0   72    0
    datetime (2013-07-24T22:54:56)
    0000   0x78 0xf6 0x56 0x78 0x0d                   x.Vx.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Rewind 2013-07-24T22:57:05 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-24T22:57:05)
    0000   0x45 0xf9 0x16 0x18 0x0d                   E....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 Prime 2013-07-24T22:58:02 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 10.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x67                   ....g
    decimal
              3    0    0    0  103
    datetime (2013-07-24T22:58:02)
    0000   0x42 0xfa 0x36 0x18 0x0d                   B.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 BasalProfileStart 2013-07-24T22:58:28 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-24T22:58:28)
    0000   0x5c 0xfa 0x16 0x18 0x0d                   \....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 1]
#### RECORD 5 BasalProfileStart 2013-07-25T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-25T00:00:00)
    0000   0x40 0xc0 0x00 0x19 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 ResultTotals (2000, 6, 0, 0, 13, 56) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xdf                   .....
    decimal
              7    0    0    4  223
    datetime ((2000, 6, 0, 0, 13, 56))
    0000   0x78 0x8d 0x00 0x00 0x00                   x....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x78 0x8d 0x05 0x00 0x80 0x00 0x00    nx......
    0008   0x09 0x00 0x00 0x04 0xdf 0x02 0xdb 0x3b    .......;
    0010   0x02 0x04 0x29 0x00 0x8c 0x01 0xac 0x00    ..).....
    0018   0x00 0x00 0x58 0x00 0x00 0x07 0x00 0x01    ..X.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x68 0xd3 0x00 0x00 0x00         ..h....
    decimal
            110  120  141    5    0  128    0    0
              9    0    0    4  223    2  219   59
              2    4   41    0  140    1  172    0
              0    0   88    0    0    7    0    1
              0    0    0    0    0    0    0    0
              0    0  104  211    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 8 BasalProfileStart 2013-07-25T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-25T04:00:00)
    0000   0x40 0xc0 0x04 0x19 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 9 BasalProfileStart 2013-07-25T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-25T08:00:00)
    0000   0x40 0xc0 0x08 0x19 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 10 CalBGForPH 2013-07-25T08:56:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 287}
```
    op hex (2)
    0000   0x0a 0x1f                                  ..
    decimal
             10   31
    datetime (2013-07-25T08:56:50)
    0000   0x72 0xf8 0x28 0x19 0x8d                   r.(..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 11 BolusWizard 2013-07-25T08:56:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 287,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x1f                                  [.
    decimal
             91   31
    datetime (2013-07-25T08:56:53)
    0000   0x75 0xf8 0x08 0x79 0x0d                   u..y.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x6c 0x00    .Q.x<dl.
    0008   0x00 0x00 0x00 0x00 0x00 0x6c 0x78         .....lx
    decimal
              0   81    0  120   60  100  108    0
              0    0    0    0    0  108  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Bolus 2013-07-25T08:56:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-07-25T08:56:53)
    0000   0x75 0xf8 0x48 0x79 0x0d                   u.Hy.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 CalBGForPH 2013-07-25T10:18:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-07-25T10:18:53)
    0000   0x75 0xd2 0x2a 0x19 0x0d                   u.*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 BolusWizard 2013-07-25T10:20:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-07-25T10:20:12)
    0000   0x4c 0xd4 0x0a 0x79 0x0d                   L..y.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x08 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x34 0x00 0x40 0x78         @..4.@x
    decimal
             20   80    0  120   60  100    8    0
             64    0    0   52    0   64  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 87, 'amount': 2.7, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0x57 0xc0                   \.lW.
    decimal
             92    5  108   87  192
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-07-25T10:20:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x34 0x00    ..@.@.4.
    decimal
              1    0   64    0   64    0   52    0
    datetime (2013-07-25T10:20:13)
    0000   0x4d 0xd4 0x4a 0x79 0x0d                   M.Jy.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 BasalProfileStart 2013-07-25T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-25T12:00:00)
    0000   0x40 0xc0 0x0c 0x19 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 18 CalBGForPH 2013-07-25T13:53:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-07-25T13:53:15)
    0000   0x4f 0xf5 0x2d 0x19 0x0d                   O.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 BolusWizard 2013-07-25T13:53:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 34,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 112}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-07-25T13:53:37)
    0000   0x65 0xf5 0x0d 0x79 0x0d                   e..y.
    body (15)
    hex
    0000   0x22 0x50 0x00 0x78 0x3c 0x64 0x04 0x00    "P.x<d..
    0008   0x70 0x00 0x00 0x00 0x00 0x74 0x78         p....tx
    decimal
             34   80    0  120   60  100    4    0
            112    0    0    0    0  116  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 220, 'amount': 1.6, 'curve': 192},
 {'age': 44, 'amount': 2.7, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0xdc 0xc0 0x6c 0x2c 0xd0    \.@..l,.
    decimal
             92    8   64  220  192  108   44  208
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-07-25T13:53:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2013-07-25T13:53:37)
    0000   0x65 0xf5 0x4d 0x79 0x0d                   e.My.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 CalBGForPH 2013-07-25T15:07:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 207}
```
    op hex (2)
    0000   0x0a 0xcf                                  ..
    decimal
             10  207
    datetime (2013-07-25T15:07:48)
    0000   0x70 0xc7 0x2f 0x19 0x0d                   p./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 BolusWizard 2013-07-25T15:08:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 207,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
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
    0000   0x5b 0xcf                                  [.
    decimal
             91  207
    datetime (2013-07-25T15:08:37)
    0000   0x65 0xc8 0x0f 0x19 0x0d                   e....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x38 0x00    .P.x<d8.
    0008   0x00 0x00 0x00 0x44 0x00 0x00 0x78         ...D..x
    decimal
              0   80    0  120   60  100   56    0
              0    0    0   68    0    0  120
    HOUR BITS: [1, 1, 0]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 75, 'amount': 2.9, 'curve': 192},
 {'age': 39, 'amount': 1.6, 'curve': 208},
 {'age': 119, 'amount': 2.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x74 0x4b 0xc0 0x40 0x27 0xd0    \.tK.@'.
    0008   0x6c 0x77 0xd0                             lw.
    decimal
             92   11  116   75  192   64   39  208
            108  119  208
    datetime (unknown)

    body (0)

#### RECORD 25 CalBGForPH 2013-07-25T15:27:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2013-07-25T15:27:22)
    0000   0x56 0xdb 0x2f 0x19 0x8d                   V./..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 BolusWizard 2013-07-25T15:27:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 276,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x14                                  [.
    decimal
             91   20
    datetime (2013-07-25T15:27:24)
    0000   0x58 0xdb 0x0f 0x79 0x0d                   X..y.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x68 0x00    .Q.x<dh.
    0008   0x00 0x00 0x00 0x34 0x00 0x34 0x78         ...4.4x
    decimal
              0   81    0  120   60  100  104    0
              0    0    0   52    0   52  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 2.9, 'curve': 192},
 {'age': 58, 'amount': 1.6, 'curve': 208},
 {'age': 138, 'amount': 2.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x74 0x5e 0xc0 0x40 0x3a 0xd0    \.t^.@:.
    0008   0x6c 0x8a 0xd0                             l..
    decimal
             92   11  116   94  192   64   58  208
            108  138  208
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-07-25T15:27:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x34 0x00    ..4.4.4.
    decimal
              1    0   52    0   52    0   52    0
    datetime (2013-07-25T15:27:24)
    0000   0x58 0xdb 0x4f 0x79 0x0d                   X.Oy.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 CalBGForPH 2013-07-25T16:42:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 337}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2013-07-25T16:42:34)
    0000   0x62 0xea 0x30 0x19 0x8d                   b.0..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 BolusWizard 2013-07-25T16:42:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 337,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
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
    datetime (2013-07-25T16:42:38)
    0000   0x66 0xea 0x10 0x79 0x0d                   f..y.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x90 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x28 0x00 0x68 0x78         ...(.hx
    decimal
              0   81    0  120   60  100  144    0
              0    0    0   40    0  104  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 1.3, 'curve': 192},
 {'age': 169, 'amount': 2.9, 'curve': 192},
 {'age': 133, 'amount': 1.6, 'curve': 208},
 {'age': 213, 'amount': 2.7, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x34 0x4f 0xc0 0x74 0xa9 0xc0    \.4O.t..
    0008   0x40 0x85 0xd0 0x6c 0xd5 0xd0              @..l..
    decimal
             92   14   52   79  192  116  169  192
             64  133  208  108  213  208
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-07-25T16:42:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x28 0x00    ..h.h.(.
    decimal
              1    0  104    0  104    0   40    0
    datetime (2013-07-25T16:42:38)
    0000   0x66 0xea 0x50 0x79 0x0d                   f.Py.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 33 CalBGForPH 2013-07-25T20:19:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-07-25T20:19:52)
    0000   0x74 0xd3 0x34 0x19 0x0d                   t.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 34 BolusWizard 2013-07-25T20:20:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-07-25T20:20:01)
    0000   0x41 0xd4 0x14 0x19 0x0d                   A....
    body (15)
    hex
    0000   0x17 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x5c 0x00 0x00 0x00 0x00 0x5c 0x78         \....\x
    decimal
             23   80    0  100   60  100    0    0
             92    0    0    0    0   92  120
    HOUR BITS: [1, 1, 0]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 2.05, 'curve': 192},
 {'age': 227, 'amount': 0.55, 'curve': 192},
 {'age': 41, 'amount': 1.3, 'curve': 208},
 {'age': 131, 'amount': 2.9, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x52 0xd9 0xc0 0x16 0xe3 0xc0    \.R.....
    0008   0x34 0x29 0xd0 0x74 0x83 0xd0              4).t..
    decimal
             92   14   82  217  192   22  227  192
             52   41  208  116  131  208
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-07-25T20:20:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x00 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    0    0
    datetime (2013-07-25T20:20:01)
    0000   0x41 0xd4 0x54 0x19 0x0d                   A.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 BasalProfileStart 2013-07-26T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-26T00:00:00)
    0000   0x40 0xc0 0x00 0x1a 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 38 ResultTotals (2000, 6, 0, 0, 13, 57) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf4                   .....
    decimal
              7    0    0    4  244
    datetime ((2000, 6, 0, 0, 13, 57))
    0000   0x79 0x8d 0x00 0x00 0x00                   y....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x79 0x8d 0x05 0x00 0xd3 0x00 0x00    ny......
    0008   0x07 0x00 0x00 0x04 0xf4 0x02 0xdc 0x3a    .......:
    0010   0x02 0x18 0x2a 0x00 0x4d 0x00 0x9c 0x01    ..*.M...
    0018   0x08 0x00 0x74 0x00 0x00 0x02 0x03 0x01    ..t.....
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6b 0x51 0x00 0x00 0x00         ..kQ...
    decimal
            110  121  141    5    0  211    0    0
              7    0    0    4  244    2  220   58
              2   24   42    0   77    0  156    1
              8    0  116    0    0    2    3    1
              0    4    0    0    0    0    0    0
              0    0  107   81    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 40 CalBGForPH 2013-07-26T01:29:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 335}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2013-07-26T01:29:55)
    0000   0x77 0xdd 0x21 0x1a 0x8d                   w.!..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 41 BolusWizard 2013-07-26T01:29:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 335,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 13.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4f                                  [O
    decimal
             91   79
    datetime (2013-07-26T01:29:59)
    0000   0x7b 0xdd 0x01 0x7a 0x0d                   {..z.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x6e 0x88 0x00    .Q.x<n..
    0008   0x00 0x00 0x00 0x00 0x00 0x88 0x82         .......
    decimal
              0   81    0  120   60  110  136    0
              0    0    0    0    0  136  130
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 2.3, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x3c 0xd0                   \.\<.
    decimal
             92    5   92   60  208
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-07-26T01:29:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x00 0x00    ........
    decimal
              1    0  136    0  136    0    0    0
    datetime (2013-07-26T01:29:59)
    0000   0x7b 0xdd 0x41 0x7a 0x0d                   {.Az.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 44 BasalProfileStart 2013-07-26T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-26T04:00:00)
    0000   0x40 0xc0 0x04 0x1a 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 45 BasalProfileStart 2013-07-26T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-26T08:00:00)
    0000   0x40 0xc0 0x08 0x1a 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 46 BasalProfileStart 2013-07-26T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-26T12:00:00)
    0000   0x40 0xc0 0x0c 0x1a 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 47 CalBGForPH 2013-07-26T13:37:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-07-26T13:37:05)
    0000   0x45 0xe5 0x2d 0x1a 0x0d                   E.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 BolusWizard 2013-07-26T13:37:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 110,
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
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-07-26T13:37:11)
    0000   0x4b 0xe5 0x0d 0x7a 0x0d                   K..z.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0  120   60  100    0    0
              0    0    0    0    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 Bolus 2013-07-26T13:37:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2013-07-26T13:37:11)
    0000   0x4b 0xe5 0x4d 0x7a 0x0d                   K.Mz.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 CalBGForPH 2013-07-26T17:42:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-07-26T17:42:48)
    0000   0x70 0xea 0x31 0x1a 0x0d                   p.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 51 BolusWizard 2013-07-26T17:42:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 7.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2013-07-26T17:42:54)
    0000   0x76 0xea 0x11 0x7a 0x0d                   v..z.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x48 0x00    .P.d<dH.
    0008   0x00 0x00 0x00 0x00 0x00 0x48 0x78         .....Hx
    decimal
              0   80    0  100   60  100   72    0
              0    0    0    0    0   72  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 249, 'amount': 1.8, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x48 0xf9 0xc0                   \.H..
    decimal
             92    5   72  249  192
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-07-26T17:42:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2013-07-26T17:42:54)
    0000   0x76 0xea 0x51 0x7a 0x0d                   v.Qz.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 BasalProfileStart 2013-07-27T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-27T00:00:00)
    0000   0x40 0xc0 0x00 0x1b 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 55 ResultTotals (2000, 6, 0, 0, 13, 58) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xd4                   .....
    decimal
              7    0    0    3  212
    datetime ((2000, 6, 0, 0, 13, 58))
    0000   0x7a 0x8d 0x00 0x00 0x00                   z....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7a 0x8d 0x05 0x00 0xe1 0x00 0x00    nz......
    0008   0x03 0x00 0x00 0x03 0xd4 0x02 0xdc 0x4b    .......K
    0010   0x00 0xf8 0x19 0x00 0x00 0x00 0x00 0x00    ........
    0018   0xf8 0x00 0x00 0x00 0x00 0x00 0x03 0x00    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6e 0x4f 0x00 0x00 0x00         ..nO...
    decimal
            110  122  141    5    0  225    0    0
              3    0    0    3  212    2  220   75
              0  248   25    0    0    0    0    0
            248    0    0    0    0    0    3    0
              0    4    0    0    0    0    0    0
              0    0  110   79    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 57 CalBGForPH 2013-07-27T00:04:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2013-07-27T00:04:50)
    0000   0x72 0xc4 0x20 0x1b 0x0d                   r. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 58 BolusWizard 2013-07-27T00:05:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 2,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 4}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2013-07-27T00:05:00)
    0000   0x40 0xc5 0x00 0x7b 0x0d                   @..{.
    body (15)
    hex
    0000   0x02 0x50 0x00 0x78 0x3c 0x6e 0x00 0x00    .P.x<n..
    0008   0x04 0x00 0x00 0x00 0x00 0x04 0x82         .......
    decimal
              2   80    0  120   60  110    0    0
              4    0    0    0    0    4  130
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 0.85, 'curve': 208},
 {'age': 136, 'amount': 0.15, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x22 0x7e 0xd0 0x06 0x88 0xd0    \."~....
    decimal
             92    8   34  126  208    6  136  208
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-07-27T00:05:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-07-27T00:05:00)
    0000   0x40 0xc5 0x40 0x7b 0x0d                   @.@{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 61 BasalProfileStart 2013-07-27T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-27T04:00:00)
    0000   0x40 0xc0 0x04 0x1b 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 62 BasalProfileStart 2013-07-27T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-27T08:00:00)
    0000   0x40 0xc0 0x08 0x1b 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 63 CalBGForPH 2013-07-27T11:35:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-07-27T11:35:37)
    0000   0x65 0xe3 0x2b 0x1b 0x0d                   e.+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 64 BolusWizard 2013-07-27T11:35:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-07-27T11:35:51)
    0000   0x73 0xe3 0x0b 0x7b 0x0d                   s..{.
    body (15)
    hex
    0000   0x1c 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x5c 0x00 0x00 0x00 0x00 0x5c 0x78         \....\x
    decimal
             28   80    0  120   60  100    0    0
             92    0    0    0    0   92  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 Bolus 2013-07-27T11:35:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x00 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    0    0
    datetime (2013-07-27T11:35:51)
    0000   0x73 0xe3 0x4b 0x7b 0x0d                   s.K{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 66 BasalProfileStart 2013-07-27T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-27T12:00:00)
    0000   0x40 0xc0 0x0c 0x1b 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 67 CalBGForPH 2013-07-27T15:49:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-07-27T15:49:35)
    0000   0x63 0xf1 0x2f 0x1b 0x0d                   c./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 BolusWizard 2013-07-27T15:49:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 113,
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
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-07-27T15:49:43)
    0000   0x6b 0xf1 0x0f 0x7b 0x0d                   k..{.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0    0    0   64  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 2.3, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x00 0xd0                   \.\..
    decimal
             92    5   92    0  208
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-07-27T15:49:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-07-27T15:49:43)
    0000   0x6b 0xf1 0x4f 0x7b 0x0d                   k.O{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 71 CalBGForPH 2013-07-27T16:43:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-07-27T16:43:18)
    0000   0x52 0xeb 0x30 0x1b 0x0d                   R.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 BolusWizard 2013-07-27T16:43:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
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
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-07-27T16:43:22)
    0000   0x56 0xeb 0x10 0x7b 0x0d                   V..{.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x30 0x00 0x30 0x78         0..0.0x
    decimal
             15   80    0  120   60  100    0    0
             48    0    0   48    0   48  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 1.6, 'curve': 192},
 {'age': 54, 'amount': 2.3, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x3c 0xc0 0x5c 0x36 0xd0    \.@<.\6.
    decimal
             92    8   64   60  192   92   54  208
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-19.data: 74 records`
