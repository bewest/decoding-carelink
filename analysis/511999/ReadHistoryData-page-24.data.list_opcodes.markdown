## START analysis/sarak/raw//ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x9b 0x97                                  ..
##### DEBUG DECIMAL
            155  151
#### RECORD 0 BolusWizard 2013-07-16T11:44:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2013-07-16T11:44:50)
    0000   0x72 0xec 0x0b 0x10 0x0d                   r....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x08 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x24 0x00 0x00 0x78         ...$..x
    decimal
              0   80    0  120   60  100    8    0
              0    0    0   36    0    0  120
    HOUR BITS: [1, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 1.9, 'curve': 192},
 {'age': 201, 'amount': 2.7, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x5b 0xc0 0x6c 0xc9 0xc0    \.L[.l..
    decimal
             92    8   76   91  192  108  201  192
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-07-16T11:44:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x24 0x00    ..@.@.$.
    decimal
              1    0   64    0   64    0   36    0
    datetime (2013-07-16T11:44:50)
    0000   0x72 0xec 0x4b 0x10 0x0d                   r.K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 BasalProfileStart 2013-07-16T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-16T12:00:00)
    0000   0x40 0xc0 0x0c 0x10 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-16T12:26:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-07-16T12:26:00)
    0000   0x40 0xda 0x2c 0x10 0x0d                   @.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BolusWizard 2013-07-16T12:26:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 200,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
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
    0000   0x5b 0xc8                                  [.
    decimal
             91  200
    datetime (2013-07-16T12:26:03)
    0000   0x43 0xda 0x0c 0x10 0x0d                   C....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x34 0x00    .P.x<d4.
    0008   0x00 0x00 0x00 0x44 0x00 0x00 0x78         ...D..x
    decimal
              0   80    0  120   60  100   52    0
              0    0    0   68    0    0  120
    HOUR BITS: [1, 1, 0]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 1.6, 'curve': 192},
 {'age': 133, 'amount': 1.9, 'curve': 192},
 {'age': 243, 'amount': 2.7, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x2b 0xc0 0x4c 0x85 0xc0    \.@+.L..
    0008   0x6c 0xf3 0xc0                             l..
    decimal
             92   11   64   43  192   76  133  192
            108  243  192
    datetime (unknown)

    body (0)

#### RECORD 7 CalBGForPH 2013-07-16T13:21:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-07-16T13:21:30)
    0000   0x5e 0xd5 0x2d 0x10 0x0d                   ^.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 BolusWizard 2013-07-16T13:21:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
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
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-07-16T13:21:47)
    0000   0x6f 0xd5 0x0d 0x70 0x0d                   o..p.
    body (15)
    hex
    0000   0x1a 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x54 0x00 0x00 0x1c 0x00 0x54 0x78         T....Tx
    decimal
             26   80    0  120   60  100    0    0
             84    0    0   28    0   84  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 1.6, 'curve': 192},
 {'age': 188, 'amount': 1.9, 'curve': 192},
 {'age': 42, 'amount': 2.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x62 0xc0 0x4c 0xbc 0xc0    \.@b.L..
    0008   0x6c 0x2a 0xd0                             l*.
    decimal
             92   11   64   98  192   76  188  192
            108   42  208
    datetime (unknown)

    body (0)

#### RECORD 10 LowReservoir 2013-07-16T13:22:02 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-16T13:22:02)
    0000   0x42 0xd6 0x0d 0x10 0x0d                   B....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 Bolus 2013-07-16T13:21:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x1c 0x00    ..T.T...
    decimal
              1    0   84    0   84    0   28    0
    datetime (2013-07-16T13:21:47)
    0000   0x6f 0xd5 0x4d 0x70 0x0d                   o.Mp.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 CalBGForPH 2013-07-16T20:48:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2013-07-16T20:48:03)
    0000   0x43 0xf0 0x34 0x10 0x0d                   C.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 BolusWizard 2013-07-16T20:48:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 157,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9d                                  [.
    decimal
             91  157
    datetime (2013-07-16T20:48:05)
    0000   0x45 0xf0 0x14 0x70 0x0d                   E..p.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x18 0x00    .P.d<d..
    0008   0x00 0x00 0x00 0x00 0x00 0x18 0x78         ......x
    decimal
              0   80    0  100   60  100   24    0
              0    0    0    0    0   24  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 189, 'amount': 0.35, 'curve': 208},
 {'age': 199, 'amount': 1.75, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x0e 0xbd 0xd0 0x46 0xc7 0xd0    \....F..
    decimal
             92    8   14  189  208   70  199  208
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-07-16T20:48:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x00 0x00    ........
    decimal
              1    0   24    0   24    0    0    0
    datetime (2013-07-16T20:48:06)
    0000   0x46 0xf0 0x54 0x70 0x0d                   F.Tp.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 CalBGForPH 2013-07-16T21:21:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-07-16T21:21:01)
    0000   0x41 0xd5 0x35 0x10 0x0d                   A.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 BolusWizard 2013-07-16T21:21:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 116,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.4,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-07-16T21:21:10)
    0000   0x4a 0xd5 0x15 0x70 0x0d                   J..p.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x78 0x00 0x00 0x18 0x00 0x78 0x78         x....xx
    decimal
             30   80    0  100   60  100    0    0
            120    0    0   24    0  120  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 0.6, 'curve': 192},
 {'age': 222, 'amount': 0.35, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0x26 0xc0 0x0e 0xde 0xd0    \..&....
    decimal
             92    8   24   38  192   14  222  208
    datetime (unknown)

    body (0)

#### RECORD 19 LowReservoir 2013-07-16T21:22:24 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-07-16T21:22:24)
    0000   0x58 0xd6 0x15 0x10 0x0d                   X....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 Bolus 2013-07-16T21:21:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x18 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   24    0
    datetime (2013-07-16T21:21:10)
    0000   0x4a 0xd5 0x55 0x70 0x0d                   J.Up.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 BasalProfileStart 2013-07-17T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-17T00:00:00)
    0000   0x40 0xc0 0x00 0x11 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1f 0x00                             ...
    decimal
              0   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 22 MResultTotals 2013-07-17T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc0                   .....
    decimal
              7    0    0    4  192
    datetime (2013-07-17T00:00:00)
    0000   0x70 0x8d                                  p.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 23 Sara6E 2013-07-17T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-07-17T00:00:00)
    0000   0x70 0x8d                                  p.
    body (49)
    hex
    0000   0x05 0x00 0xa2 0x00 0x00 0x07 0x00 0x00    ........
    0008   0x04 0xc0 0x02 0xe4 0x3d 0x01 0xdc 0x27    ....=..'
    0010   0x00 0x4f 0x01 0x18 0x00 0xc4 0x00 0x00    .O......
    0018   0x00 0x00 0x03 0x03 0x00 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x71    .......q
    0028   0x1f 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  162    0    0    7    0    0
              4  192    2  228   61    1  220   39
              0   79    1   24    0  196    0    0
              0    0    3    3    0    0    4    0
              0    0    0    0    0    0    0  113
             31    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 24 BasalProfileStart 2013-07-17T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-17T04:00:00)
    0000   0x40 0xc0 0x04 0x11 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BasalProfileStart 2013-07-17T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-17T08:00:00)
    0000   0x40 0xc0 0x08 0x11 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 26 CalBGForPH 2013-07-17T09:19:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 296}
```
    op hex (2)
    0000   0x0a 0x28                                  .(
    decimal
             10   40
    datetime (2013-07-17T09:19:58)
    0000   0x7a 0xd3 0x29 0x11 0x8d                   z.)..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 27 BolusWizard 2013-07-17T09:20:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 296,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x28                                  [(
    decimal
             91   40
    datetime (2013-07-17T09:20:01)
    0000   0x41 0xd4 0x09 0x71 0x0d                   A..q.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x74 0x00    .Q.x<dt.
    0008   0x00 0x00 0x00 0x00 0x00 0x74 0x78         .....tx
    decimal
              0   81    0  120   60  100  116    0
              0    0    0    0    0  116  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 Bolus 2013-07-17T09:20:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2013-07-17T09:20:01)
    0000   0x41 0xd4 0x49 0x71 0x0d                   A.Iq.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 CalBGForPH 2013-07-17T09:38:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 298}
```
    op hex (2)
    0000   0x0a 0x2a                                  .*
    decimal
             10   42
    datetime (2013-07-17T09:38:29)
    0000   0x5d 0xe6 0x29 0x11 0x8d                   ].)..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 BolusWizard 2013-07-17T09:38:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 298,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 11.2,
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
    0000   0x5b 0x2a                                  [*
    decimal
             91   42
    datetime (2013-07-17T09:38:34)
    0000   0x62 0xe6 0x09 0x71 0x0d                   b..q.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x74 0x00    .Q.x<dt.
    0008   0x00 0x00 0x00 0x70 0x00 0x04 0x78         ...p..x
    decimal
              0   81    0  120   60  100  116    0
              0    0    0  112    0    4  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 2.9, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0x19 0xc0                   \.t..
    decimal
             92    5  116   25  192
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-07-17T09:38:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x04 0x00 0x04 0x00 0x70 0x00    ......p.
    decimal
              1    0    4    0    4    0  112    0
    datetime (2013-07-17T09:38:35)
    0000   0x63 0xe6 0x49 0x71 0x0d                   c.Iq.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 33 CalBGForPH 2013-07-17T10:41:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-07-17T10:41:45)
    0000   0x6d 0xe9 0x2a 0x11 0x0d                   m.*..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 BolusWizard 2013-07-17T10:41:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-07-17T10:41:53)
    0000   0x75 0xe9 0x0a 0x71 0x0d                   u..q.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x08 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x3c 0x00 0x00 0x78         ...<..x
    decimal
              0   80    0  120   60  100    8    0
              0    0    0   60    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 0.1, 'curve': 192},
 {'age': 88, 'amount': 2.9, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x04 0x44 0xc0 0x74 0x58 0xc0    \..D.tX.
    decimal
             92    8    4   68  192  116   88  192
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-07-17T10:41:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x3c 0x00    ..d.d.<.
    decimal
              1    0  100    0  100    0   60    0
    datetime (2013-07-17T10:41:54)
    0000   0x76 0xe9 0x4a 0x71 0x0d                   v.Jq.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 BasalProfileStart 2013-07-17T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-17T12:00:00)
    0000   0x40 0xc0 0x0c 0x11 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 38 CalBGForPH 2013-07-17T13:15:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2013-07-17T13:15:40)
    0000   0x68 0xcf 0x2d 0x11 0x0d                   h.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 39 BolusWizard 2013-07-17T13:15:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 155,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2013-07-17T13:15:58)
    0000   0x7a 0xcf 0x0d 0x71 0x0d                   z..q.
    body (15)
    hex
    0000   0x17 0x50 0x00 0x78 0x3c 0x64 0x14 0x00    .P.x<d..
    0008   0x4c 0x00 0x00 0x0c 0x00 0x54 0x78         L....Tx
    decimal
             23   80    0  120   60  100   20    0
             76    0    0   12    0   84  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 0.9, 'curve': 192},
 {'age': 162, 'amount': 1.6, 'curve': 192},
 {'age': 222, 'amount': 0.1, 'curve': 192},
 {'age': 242, 'amount': 2.9, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0x24 0x98 0xc0 0x40 0xa2 0xc0    \.$..@..
    0008   0x04 0xde 0xc0 0x74 0xf2 0xc0              ...t..
    decimal
             92   14   36  152  192   64  162  192
              4  222  192  116  242  192
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2013-07-17T13:15:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x0c 0x00    ..T.T...
    decimal
              1    0   84    0   84    0   12    0
    datetime (2013-07-17T13:15:58)
    0000   0x7a 0xcf 0x4d 0x71 0x0d                   z.Mq.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 CalBGForPH 2013-07-17T18:59:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 259}
```
    op hex (2)
    0000   0x0a 0x03                                  ..
    decimal
             10    3
    datetime (2013-07-17T18:59:40)
    0000   0x68 0xfb 0x32 0x11 0x8d                   h.2..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 BolusWizard 2013-07-17T18:59:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 259,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 9.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x03                                  [.
    decimal
             91    3
    datetime (2013-07-17T18:59:42)
    0000   0x6a 0xfb 0x12 0x71 0x0d                   j..q.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x5c 0x00    .Q.d<d\.
    0008   0x00 0x00 0x00 0x00 0x00 0x5c 0x78         .....\x
    decimal
              0   81    0  100   60  100   92    0
              0    0    0    0    0   92  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 90, 'amount': 2.1, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x54 0x5a 0xd0                   \.TZ.
    decimal
             92    5   84   90  208
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-07-17T18:59:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x0c 0x00 0x00 0x00    ..\.....
    decimal
              1    0   92    0   12    0    0    0
    datetime (2013-07-17T18:59:42)
    0000   0x6a 0xfb 0x52 0x71 0x0d                   j.Rq.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 NoDelivery 2013-07-17T18:59:54 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2013-07-17T18:59:54)
    0000   0x76 0xfb 0x52 0x51 0x0d                   v.RQ.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 47 ClearAlarm 2013-07-17T19:00:08 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2013-07-17T19:00:08)
    0000   0x48 0xc0 0x13 0x11 0x0d                   H....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 BasalProfileStart 2013-07-17T19:00:09 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-17T19:00:09)
    0000   0x49 0xc0 0x13 0x11 0x0d                   I....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 49 Rewind 2013-07-17T19:02:39 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-17T19:02:39)
    0000   0x67 0xc2 0x13 0x11 0x0d                   g....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 Prime 2013-07-17T19:03:42 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x31                   ....1
    decimal
              3    0    0    0   49
    datetime (2013-07-17T19:03:42)
    0000   0x6a 0xc3 0x33 0x11 0x0d                   j.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 51 BasalProfileStart 2013-07-17T20:04:51 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-17T20:04:51)
    0000   0x73 0xc4 0x14 0x11 0x0d                   s....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 52 CalBGForPH 2013-07-17T20:05:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-07-17T20:05:10)
    0000   0x4a 0xc5 0x34 0x11 0x0d                   J.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 BolusWizard 2013-07-17T20:05:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 156,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2013-07-17T20:05:12)
    0000   0x4c 0xc5 0x14 0x11 0x0d                   L....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x18 0x00    .P.d<d..
    0008   0x00 0x00 0x00 0x08 0x00 0x10 0x78         ......x
    decimal
              0   80    0  100   60  100   24    0
              0    0    0    8    0   16  120
    HOUR BITS: [1, 1, 0]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 0.3, 'curve': 192},
 {'age': 156, 'amount': 2.1, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x0c 0x48 0xc0 0x54 0x9c 0xd0    \..H.T..
    decimal
             92    8   12   72  192   84  156  208
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-07-17T20:05:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x08 0x00    ........
    decimal
              1    0   16    0   16    0    8    0
    datetime (2013-07-17T20:05:13)
    0000   0x4d 0xc5 0x54 0x11 0x0d                   M.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 CalBGForPH 2013-07-17T20:47:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 246}
```
    op hex (2)
    0000   0x0a 0xf6                                  ..
    decimal
             10  246
    datetime (2013-07-17T20:47:32)
    0000   0x60 0xef 0x34 0x11 0x0d                   `.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 57 BolusWizard 2013-07-17T20:47:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 246,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf6                                  [.
    decimal
             91  246
    datetime (2013-07-17T20:47:35)
    0000   0x63 0xef 0x14 0x71 0x0d                   c..q.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x54 0x00    .P.d<dT.
    0008   0x00 0x00 0x00 0x14 0x00 0x40 0x78         .....@x
    decimal
              0   80    0  100   60  100   84    0
              0    0    0   20    0   64  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 0.4, 'curve': 192},
 {'age': 114, 'amount': 0.3, 'curve': 192},
 {'age': 198, 'amount': 2.1, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0x2c 0xc0 0x0c 0x72 0xc0    \..,..r.
    0008   0x54 0xc6 0xd0                             T..
    decimal
             92   11   16   44  192   12  114  192
             84  198  208
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-07-17T20:47:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x14 0x00    ..@.@...
    decimal
              1    0   64    0   64    0   20    0
    datetime (2013-07-17T20:47:35)
    0000   0x63 0xef 0x54 0x71 0x0d                   c.Tq.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 CalBGForPH 2013-07-17T21:37:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 346}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-07-17T21:37:14)
    0000   0x4e 0xe5 0x35 0x11 0x8d                   N.5..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 61 BolusWizard 2013-07-17T21:37:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 346,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
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
    0000   0x5b 0x5a                                  [Z
    decimal
             91   90
    datetime (2013-07-17T21:37:16)
    0000   0x50 0xe5 0x15 0x71 0x0d                   P..q.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x94 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0x38 0x00 0x5c 0x78         ...8.\x
    decimal
              0   81    0  100   60  100  148    0
              0    0    0   56    0   92  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 1.6, 'curve': 192},
 {'age': 94, 'amount': 0.4, 'curve': 192},
 {'age': 164, 'amount': 0.3, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x36 0xc0 0x10 0x5e 0xc0    \.@6..^.
    0008   0x0c 0xa4 0xc0                             ...
    decimal
             92   11   64   54  192   16   94  192
             12  164  192
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2013-07-17T21:37:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x38 0x00    ..\.\.8.
    decimal
              1    0   92    0   92    0   56    0
    datetime (2013-07-17T21:37:17)
    0000   0x51 0xe5 0x55 0x71 0x0d                   Q.Uq.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 CalBGForPH 2013-07-17T22:34:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 359}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-07-17T22:34:32)
    0000   0x60 0xe2 0x36 0x11 0x8d                   `.6..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 65 BolusWizard 2013-07-17T22:34:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 359,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 15.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-07-17T22:34:34)
    0000   0x62 0xe2 0x16 0x11 0x0d                   b....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x9c 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0x58 0x00 0x44 0x78         ...X.Dx
    decimal
              0   81    0  100   60  100  156    0
              0    0    0   88    0   68  120
    HOUR BITS: [1, 1, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 2.3, 'curve': 192},
 {'age': 111, 'amount': 1.6, 'curve': 192},
 {'age': 151, 'amount': 0.4, 'curve': 192},
 {'age': 221, 'amount': 0.3, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0x5c 0x3d 0xc0 0x40 0x6f 0xc0    \.\=.@o.
    0008   0x10 0x97 0xc0 0x0c 0xdd 0xc0              ......
    decimal
             92   14   92   61  192   64  111  192
             16  151  192   12  221  192
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-07-17T22:34:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x58 0x00    ..D.D.X.
    decimal
              1    0   68    0   68    0   88    0
    datetime (2013-07-17T22:34:34)
    0000   0x62 0xe2 0x56 0x11 0x0d                   b.V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 CalBGForPH 2013-07-17T23:10:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 341}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-07-17T23:10:04)
    0000   0x44 0xca 0x37 0x11 0x8d                   D.7..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 BolusWizard 2013-07-17T23:10:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 341,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 14.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2013-07-17T23:10:07)
    0000   0x47 0xca 0x17 0x71 0x0d                   G..q.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x90 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0x6c 0x00 0x24 0x78         ...l.$x
    decimal
              0   81    0  100   60  100  144    0
              0    0    0  108    0   36  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 1.7, 'curve': 192},
 {'age': 97, 'amount': 2.3, 'curve': 192},
 {'age': 147, 'amount': 1.6, 'curve': 192},
 {'age': 187, 'amount': 0.4, 'curve': 192},
 {'age': 1, 'amount': 0.3, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x44 0x25 0xc0 0x5c 0x61 0xc0    \.D%.\a.
    0008   0x40 0x93 0xc0 0x10 0xbb 0xc0 0x0c 0x01    @.......
    0010   0xd0                                       .
    decimal
             92   17   68   37  192   92   97  192
             64  147  192   16  187  192   12    1
            208
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-07-17T23:10:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x6c 0x00    ..$.$.l.
    decimal
              1    0   36    0   36    0  108    0
    datetime (2013-07-17T23:10:07)
    0000   0x47 0xca 0x57 0x71 0x0d                   G.Wq.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 72 BasalProfileStart 2013-07-18T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-18T00:00:00)
    0000   0x40 0xc0 0x00 0x12 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1f 0x00                             ...
    decimal
              0   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 73 MResultTotals 2013-07-18T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x15                   .....
    decimal
              7    0    0    5   21
    datetime (2013-07-18T00:00:00)
    0000   0x71 0x8d                                  q.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 74 Sara6E 2013-07-18T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-07-18T00:00:00)
    0000   0x71 0x8d                                  q.
    body (49)
    hex
    0000   0x05 0x01 0x03 0x00 0x00 0x0a 0x00 0x00    ........
    0008   0x05 0x15 0x02 0xc5 0x36 0x02 0x50 0x2e    ....6.P.
    0010   0x00 0x17 0x00 0x00 0x01 0xfc 0x00 0x54    .......T
    0018   0x00 0x00 0x00 0x09 0x01 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x88    ........
    0028   0x67 0x00 0x00 0x00 0x00 0x00 0x00 0x00    g.......
    0030   0x00                                       .
    decimal
              5    1    3    0    0   10    0    0
              5   21    2  197   54    2   80   46
              0   23    0    0    1  252    0   84
              0    0    0    9    1    0    4    0
              0    0    0    0    0    0    0  136
            103    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 75 BasalProfileStart 2013-07-18T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-18T04:00:00)
    0000   0x40 0xc0 0x04 0x12 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 76 BasalProfileStart 2013-07-18T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-18T08:00:00)
    0000   0x40 0xc0 0x08 0x12 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
`end analysis/sarak/raw//ReadHistoryData-page-24.data: 77 records`
