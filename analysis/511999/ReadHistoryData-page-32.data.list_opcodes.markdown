## START logs/ReadHistoryData-page-32.data
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x66 0x8d 0x05 0x00 0xb5 0x00 0x00    nf......
    0008   0x0d 0x00 0x00 0x05 0x6c 0x02 0xd4 0x34    ....l..4
    0010   0x02 0x98 0x30 0x00 0x7d 0x00 0xd0 0x00    ..0.}...
    0018   0x78 0x01 0x50 0x00 0x00 0x05 0x03 0x03    x.P.....
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0x5f 0x00 0x00 0x00         ..d_...
    decimal
            110  102  141    5    0  181    0    0
             13    0    0    5  108    2  212   52
              2  152   48    0  125    0  208    0
            120    1   80    0    0    5    3    3
              0    4    0    0    0    0    0    0
              0    0  100   95    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 BasalProfileStart 2013-07-07T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-07T04:00:00)
    0000   0x40 0xc0 0x04 0x07 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BasalProfileStart 2013-07-07T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-07T08:00:00)
    0000   0x40 0xc0 0x08 0x07 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-07-07T08:20:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2013-07-07T08:20:16)
    0000   0x50 0xd4 0x28 0x07 0x0d                   P.(..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-07-07T08:20:19 head[2], body[15] op[0x5b]
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
    datetime (2013-07-07T08:20:19)
    0000   0x53 0xd4 0x08 0x67 0x0d                   S..g.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x40 0x00    .P.x<d@.
    0008   0x00 0x00 0x00 0x00 0x00 0x40 0x78         .....@x
    decimal
              0   80    0  120   60  100   64    0
              0    0    0    0    0   64  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 Bolus 2013-07-07T08:20:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-07-07T08:20:19)
    0000   0x53 0xd4 0x48 0x67 0x0d                   S.Hg.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2013-07-07T08:37:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 218}
```
    op hex (2)
    0000   0x0a 0xda                                  ..
    decimal
             10  218
    datetime (2013-07-07T08:37:29)
    0000   0x5d 0xe5 0x28 0x07 0x0d                   ].(..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 BolusWizard 2013-07-07T08:37:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 218,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.4,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0xda                                  [.
    decimal
             91  218
    datetime (2013-07-07T08:37:37)
    0000   0x65 0xe5 0x08 0x67 0x0d                   e..g.
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x40 0x00    .P.x<d@.
    0008   0x34 0x00 0x00 0x40 0x00 0x34 0x78         4..@.4x
    decimal
             16   80    0  120   60  100   64    0
             52    0    0   64    0   52  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 1.6, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x17 0xc0                   \.@..
    decimal
             92    5   64   23  192
    datetime (unknown)

    body (0)

#### RECORD 9 LowReservoir 2013-07-07T08:38:09 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-07T08:38:09)
    0000   0x49 0xe6 0x08 0x07 0x0d                   I....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 Bolus 2013-07-07T08:37:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x40 0x00    ..4.4.@.
    decimal
              1    0   52    0   52    0   64    0
    datetime (2013-07-07T08:37:37)
    0000   0x65 0xe5 0x48 0x67 0x0d                   e.Hg.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 11 CalBGForPH 2013-07-07T09:14:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-07-07T09:14:58)
    0000   0x7a 0xce 0x29 0x07 0x0d                   z.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 BolusWizard 2013-07-07T09:15:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 9.2,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-07-07T09:15:25)
    0000   0x59 0xcf 0x09 0x67 0x0d                   Y..g.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x20 0x00 0x00 0x5c 0x00 0x20 0x78          ..\. x
    decimal
             10   80    0  120   60  100    0    0
             32    0    0   92    0   32  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 1.3, 'curve': 192},
 {'age': 61, 'amount': 1.6, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x29 0xc0 0x40 0x3d 0xc0    \.4).@=.
    decimal
             92    8   52   41  192   64   61  192
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-07-07T09:15:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x5c 0x00    .. . .\.
    decimal
              1    0   32    0   32    0   92    0
    datetime (2013-07-07T09:15:25)
    0000   0x59 0xcf 0x49 0x67 0x0d                   Y.Ig.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 BasalProfileStart 2013-07-07T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-07T12:00:00)
    0000   0x40 0xc0 0x0c 0x07 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 16 CalBGForPH 2013-07-07T12:19:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-07-07T12:19:58)
    0000   0x7a 0xd3 0x2c 0x07 0x0d                   z.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 BolusWizard 2013-07-07T12:20:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 104,
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
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-07-07T12:20:13)
    0000   0x4d 0xd4 0x0c 0x67 0x0d                   M..g.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x78         0....0x
    decimal
             15   80    0  120   60  100    0    0
             48    0    0    0    0   48  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 186, 'amount': 0.8, 'curve': 192},
 {'age': 226, 'amount': 1.3, 'curve': 192},
 {'age': 246, 'amount': 1.6, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x20 0xba 0xc0 0x34 0xe2 0xc0    \. ..4..
    0008   0x40 0xf6 0xc0                             @..
    decimal
             92   11   32  186  192   52  226  192
             64  246  192
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-07-07T12:20:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-07-07T12:20:14)
    0000   0x4e 0xd4 0x4c 0x67 0x0d                   N.Lg.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 CalBGForPH 2013-07-07T12:40:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2013-07-07T12:40:48)
    0000   0x70 0xe8 0x2c 0x07 0x0d                   p.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 BolusWizard 2013-07-07T12:41:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 216,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2013-07-07T12:41:26)
    0000   0x5a 0xe9 0x0c 0x67 0x0d                   Z..g.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x3c 0x64 0x40 0x00    .P.x<d@.
    0008   0x50 0x00 0x00 0x30 0x00 0x60 0x78         P..0.`x
    decimal
             25   80    0  120   60  100   64    0
             80    0    0   48    0   96  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 1.2, 'curve': 192},
 {'age': 207, 'amount': 0.8, 'curve': 192},
 {'age': 247, 'amount': 1.3, 'curve': 192},
 {'age': 11, 'amount': 1.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x30 0x1b 0xc0 0x20 0xcf 0xc0    \.0.. ..
    0008   0x34 0xf7 0xc0 0x40 0x0b 0xd0              4..@..
    decimal
             92   14   48   27  192   32  207  192
             52  247  192   64   11  208
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-07-07T12:41:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x30 0x00    ..`.`.0.
    decimal
              1    0   96    0   96    0   48    0
    datetime (2013-07-07T12:41:26)
    0000   0x5a 0xe9 0x4c 0x67 0x0d                   Z.Lg.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 Rewind 2013-07-07T13:38:37 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-07T13:38:37)
    0000   0x65 0xe6 0x0d 0x07 0x0d                   e....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 Prime 2013-07-07T13:39:46 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 16.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0xa7                   .....
    decimal
              3    0    0    0  167
    datetime (2013-07-07T13:39:46)
    0000   0x6e 0xe7 0x2d 0x07 0x0d                   n.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 BasalProfileStart 2013-07-07T15:01:02 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-07T15:01:02)
    0000   0x42 0xc1 0x0f 0x07 0x0d                   B....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 27 Prime 2013-07-07T15:00:44 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-07T15:00:44)
    0000   0x6c 0xc0 0x0f 0x07 0x0d                   l....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 CalBGForPH 2013-07-07T15:26:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 291}
```
    op hex (2)
    0000   0x0a 0x23                                  .#
    decimal
             10   35
    datetime (2013-07-07T15:26:58)
    0000   0x7a 0xda 0x2f 0x07 0x8d                   z./..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 BolusWizard 2013-07-07T15:27:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 291,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 11.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x23                                  [#
    decimal
             91   35
    datetime (2013-07-07T15:27:01)
    0000   0x41 0xdb 0x0f 0x67 0x0d                   A..g.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x70 0x00    .Q.x<dp.
    0008   0x00 0x00 0x00 0x08 0x00 0x68 0x78         .....hx
    decimal
              0   81    0  120   60  100  112    0
              0    0    0    8    0  104  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 2.4, 'curve': 192},
 {'age': 193, 'amount': 1.2, 'curve': 192},
 {'age': 117, 'amount': 0.8, 'curve': 208},
 {'age': 157, 'amount': 1.3, 'curve': 208},
 {'age': 177, 'amount': 1.6, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x60 0xad 0xc0 0x30 0xc1 0xc0    \.`..0..
    0008   0x20 0x75 0xd0 0x34 0x9d 0xd0 0x40 0xb1     u.4..@.
    0010   0xd0                                       .
    decimal
             92   17   96  173  192   48  193  192
             32  117  208   52  157  208   64  177
            208
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-07-07T15:27:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x08 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    8    0
    datetime (2013-07-07T15:27:01)
    0000   0x41 0xdb 0x4f 0x67 0x0d                   A.Og.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 CalBGForPH 2013-07-07T16:45:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 232}
```
    op hex (2)
    0000   0x0a 0xe8                                  ..
    decimal
             10  232
    datetime (2013-07-07T16:45:58)
    0000   0x7a 0xed 0x30 0x07 0x0d                   z.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 BolusWizard 2013-07-07T16:46:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 232,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
 'carb_input': 0,
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
    0000   0x5b 0xe8                                  [.
    decimal
             91  232
    datetime (2013-07-07T16:46:01)
    0000   0x41 0xee 0x10 0x67 0x0d                   A..g.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x48 0x00    .P.x<dH.
    0008   0x00 0x00 0x00 0x38 0x00 0x10 0x78         ...8..x
    decimal
              0   80    0  120   60  100   72    0
              0    0    0   56    0   16  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 2.6, 'curve': 192},
 {'age': 252, 'amount': 2.4, 'curve': 192},
 {'age': 16, 'amount': 1.2, 'curve': 208},
 {'age': 196, 'amount': 0.8, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0x52 0xc0 0x60 0xfc 0xc0    \.hR.`..
    0008   0x30 0x10 0xd0 0x20 0xc4 0xd0              0.. ..
    decimal
             92   14  104   82  192   96  252  192
             48   16  208   32  196  208
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-07-07T16:46:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x38 0x00    ......8.
    decimal
              1    0   16    0   16    0   56    0
    datetime (2013-07-07T16:46:02)
    0000   0x42 0xee 0x50 0x67 0x0d                   B.Pg.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 CalBGForPH 2013-07-07T17:13:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-07-07T17:13:39)
    0000   0x67 0xcd 0x31 0x07 0x0d                   g.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 CalBGForPH 2013-07-07T17:13:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 218}
```
    op hex (2)
    0000   0x0a 0xda                                  ..
    decimal
             10  218
    datetime (2013-07-07T17:13:52)
    0000   0x74 0xcd 0x31 0x07 0x0d                   t.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 38 BolusWizard 2013-07-07T17:14:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 218,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0xda                                  [.
    decimal
             91  218
    datetime (2013-07-07T17:14:05)
    0000   0x45 0xce 0x11 0x67 0x0d                   E..g.
    body (15)
    hex
    0000   0x1b 0x50 0x00 0x64 0x3c 0x64 0x40 0x00    .P.d<d@.
    0008   0x6c 0x00 0x00 0x30 0x00 0x7c 0x78         l..0.|x
    decimal
             27   80    0  100   60  100   64    0
            108    0    0   48    0  124  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 0.4, 'curve': 192},
 {'age': 110, 'amount': 2.6, 'curve': 192},
 {'age': 24, 'amount': 2.4, 'curve': 208},
 {'age': 44, 'amount': 1.2, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x10 0x1e 0xc0 0x68 0x6e 0xc0    \....hn.
    0008   0x60 0x18 0xd0 0x30 0x2c 0xd0              `..0,.
    decimal
             92   14   16   30  192  104  110  192
             96   24  208   48   44  208
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-07-07T17:14:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x30 0x00    ..|.|.0.
    decimal
              1    0  124    0  124    0   48    0
    datetime (2013-07-07T17:14:05)
    0000   0x45 0xce 0x51 0x67 0x0d                   E.Qg.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 CalBGForPH 2013-07-07T20:06:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-07-07T20:06:04)
    0000   0x44 0xc6 0x34 0x07 0x0d                   D.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 42 BolusWizard 2013-07-07T20:06:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-07-07T20:06:08)
    0000   0x48 0xc6 0x14 0x07 0x0d                   H....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x00 0x00 0x00 0x08 0x00 0x28 0x78         .....(x
    decimal
              0   80    0  100   60  100   48    0
              0    0    0    8    0   40  120
    HOUR BITS: [1, 1, 0]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 172, 'amount': 3.1, 'curve': 192},
 {'age': 202, 'amount': 0.4, 'curve': 192},
 {'age': 26, 'amount': 2.6, 'curve': 208},
 {'age': 196, 'amount': 2.4, 'curve': 208},
 {'age': 216, 'amount': 1.2, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x7c 0xac 0xc0 0x10 0xca 0xc0    \.|.....
    0008   0x68 0x1a 0xd0 0x60 0xc4 0xd0 0x30 0xd8    h..`..0.
    0010   0xd0                                       .
    decimal
             92   17  124  172  192   16  202  192
            104   26  208   96  196  208   48  216
            208
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-07-07T20:06:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x08 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    8    0
    datetime (2013-07-07T20:06:08)
    0000   0x48 0xc6 0x54 0x07 0x0d                   H.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 CalBGForPH 2013-07-07T21:45:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-07-07T21:45:58)
    0000   0x7a 0xed 0x35 0x07 0x0d                   z.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 46 BolusWizard 2013-07-07T21:46:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 8,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-07-07T21:46:03)
    0000   0x43 0xee 0x15 0x67 0x0d                   C..g.
    body (15)
    hex
    0000   0x08 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x20 0x00 0x00 0x10 0x00 0x20 0x78          .... x
    decimal
              8   80    0  100   60  100    0    0
             32    0    0   16    0   32  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 1.0, 'curve': 192},
 {'age': 16, 'amount': 3.1, 'curve': 208},
 {'age': 46, 'amount': 0.4, 'curve': 208},
 {'age': 126, 'amount': 2.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x66 0xc0 0x7c 0x10 0xd0    \.(f.|..
    0008   0x10 0x2e 0xd0 0x68 0x7e 0xd0              ...h~.
    decimal
             92   14   40  102  192  124   16  208
             16   46  208  104  126  208
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-07-07T21:46:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x10 0x00    .. . ...
    decimal
              1    0   32    0   32    0   16    0
    datetime (2013-07-07T21:46:04)
    0000   0x44 0xee 0x55 0x67 0x0d                   D.Ug.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 BasalProfileStart 2013-07-08T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-08T00:00:00)
    0000   0x40 0xc0 0x00 0x08 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 0]
#### RECORD 50 ResultTotals (2000, 6, 0, 0, 13, 39) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime ((2000, 6, 0, 0, 13, 39))
    0000   0x67 0x8d 0x00 0x00 0x00                   g....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x67 0x8d 0x05 0x00 0xb8 0x00 0x00    ng......
    0008   0x0b 0x00 0x00 0x05 0x0c 0x02 0xac 0x35    .......5
    0010   0x02 0x60 0x2f 0x00 0x65 0x00 0xa4 0x00    .`/.e...
    0018   0xe0 0x00 0xdc 0x00 0x00 0x04 0x04 0x02    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x67 0x23 0x00 0x00 0x00         ..g#...
    decimal
            110  103  141    5    0  184    0    0
             11    0    0    5   12    2  172   53
              2   96   47    0  101    0  164    0
            224    0  220    0    0    4    4    2
              0    4    0    0    0    0    0    0
              0    0  103   35    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 52 BasalProfileStart 2013-07-08T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-08T04:00:00)
    0000   0x40 0xc0 0x04 0x08 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 53 BasalProfileStart 2013-07-08T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-08T08:00:00)
    0000   0x40 0xc0 0x08 0x08 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 54 CalBGForPH 2013-07-08T08:48:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 266}
```
    op hex (2)
    0000   0x0a 0x0a                                  ..
    decimal
             10   10
    datetime (2013-07-08T08:48:07)
    0000   0x47 0xf0 0x28 0x08 0x8d                   G.(..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 55 BolusWizard 2013-07-08T08:48:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 266,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 9.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0a                                  [.
    decimal
             91   10
    datetime (2013-07-08T08:48:11)
    0000   0x4b 0xf0 0x08 0x68 0x0d                   K..h.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x60 0x00    .Q.x<d`.
    0008   0x00 0x00 0x00 0x00 0x00 0x60 0x78         .....`x
    decimal
              0   81    0  120   60  100   96    0
              0    0    0    0    0   96  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 Bolus 2013-07-08T08:48:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x00 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    0    0
    datetime (2013-07-08T08:48:11)
    0000   0x4b 0xf0 0x48 0x68 0x0d                   K.Hh.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2013-07-08T10:12:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-08T10:12:55)
    0000   0x77 0xcc 0x0a 0x68 0x0d                   w..h.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0    0    0   64  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 2.4, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0x58 0xc0                   \.`X.
    decimal
             92    5   96   88  192
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-07-08T10:12:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x30 0x00    ..@.@.0.
    decimal
              1    0   64    0   64    0   48    0
    datetime (2013-07-08T10:12:55)
    0000   0x77 0xcc 0x4a 0x68 0x0d                   w.Jh.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 BasalProfileStart 2013-07-08T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-08T12:00:00)
    0000   0x40 0xc0 0x0c 0x08 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 61 CalBGForPH 2013-07-08T12:08:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-07-08T12:08:52)
    0000   0x74 0xc8 0x2c 0x08 0x0d                   t.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 BolusWizard 2013-07-08T12:09:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
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
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-07-08T12:09:01)
    0000   0x41 0xc9 0x0c 0x68 0x0d                   A..h.
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x2c 0x00 0x00 0x10 0x00 0x2c 0x78         ,....,x
    decimal
             14   80    0  120   60  100    0    0
             44    0    0   16    0   44  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 1.6, 'curve': 192},
 {'age': 205, 'amount': 2.4, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x7d 0xc0 0x60 0xcd 0xc0    \.@}.`..
    decimal
             92    8   64  125  192   96  205  192
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-07-08T12:09:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x10 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   16    0
    datetime (2013-07-08T12:09:01)
    0000   0x41 0xc9 0x4c 0x68 0x0d                   A.Lh.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 65 CalBGForPH 2013-07-08T13:42:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 219}
```
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2013-07-08T13:42:33)
    0000   0x61 0xea 0x2d 0x08 0x0d                   a.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 BolusWizard 2013-07-08T13:42:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 219,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
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
    0000   0x5b 0xdb                                  [.
    decimal
             91  219
    datetime (2013-07-08T13:42:35)
    0000   0x63 0xea 0x0d 0x68 0x0d                   c..h.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x40 0x00    .P.x<d@.
    0008   0x00 0x00 0x00 0x14 0x00 0x2c 0x78         .....,x
    decimal
              0   80    0  120   60  100   64    0
              0    0    0   20    0   44  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 1.1, 'curve': 192},
 {'age': 218, 'amount': 1.6, 'curve': 192},
 {'age': 42, 'amount': 2.4, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2c 0x62 0xc0 0x40 0xda 0xc0    \.,b.@..
    0008   0x60 0x2a 0xd0                             `*.
    decimal
             92   11   44   98  192   64  218  192
             96   42  208
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-07-08T13:42:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x14 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   20    0
    datetime (2013-07-08T13:42:35)
    0000   0x63 0xea 0x4d 0x68 0x0d                   c.Mh.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
Traceback (most recent call last):
  File "list_history.py", line 99, in <module>
    main( )
  File "list_history.py", line 88, in main
    print record.pformat(prefix)
  File "/home/bewest/src/decoding-carelink/decocare/records/base.py", line 89, in pformat
    decoded = self.decode( )
  File "/home/bewest/src/decoding-carelink/decocare/records/bolus.py", line 177, in decode
    year_bits = extra_year_bits(self.date[4])
IndexError: bytearray index out of range
