## START logs/ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xd5 0x99                                  ..
##### DEBUG DECIMAL
            213  153
#### RECORD 0 BolusWizard 2013-07-23T20:06:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-07-23T20:06:36)
    0000   0x64 0xc6 0x14 0x77 0x0d                   d..w.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x50 0x00 0x00 0x10 0x00 0x50 0x78         P....Px
    decimal
             20   80    0  100   60  100    0    0
             80    0    0   16    0   80  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 123, 'amount': 1.3, 'curve': 192},
 {'age': 143, 'amount': 0.7, 'curve': 192},
 {'age': 203, 'amount': 0.95, 'curve': 192},
 {'age': 213, 'amount': 0.35, 'curve': 192},
 {'age': 37, 'amount': 1.7, 'curve': 208},
 {'age': 137, 'amount': 1.7, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x34 0x7b 0xc0 0x1c 0x8f 0xc0    \.4{....
    0008   0x26 0xcb 0xc0 0x0e 0xd5 0xc0 0x44 0x25    &.....D%
    0010   0xd0 0x44 0x89 0xd0                        .D..
    decimal
             92   20   52  123  192   28  143  192
             38  203  192   14  213  192   68   37
            208   68  137  208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-07-23T20:06:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x10 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   16    0
    datetime (2013-07-23T20:06:36)
    0000   0x64 0xc6 0x54 0x77 0x0d                   d.Tw.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-07-23T20:37:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 187}
```
    op hex (2)
    0000   0x0a 0xbb                                  ..
    decimal
             10  187
    datetime (2013-07-23T20:37:46)
    0000   0x6e 0xe5 0x34 0x17 0x0d                   n.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 CalBGForPH 2013-07-23T21:41:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 292}
```
    op hex (2)
    0000   0x0a 0x24                                  .$
    decimal
             10   36
    datetime (2013-07-23T21:41:53)
    0000   0x75 0xe9 0x35 0x17 0x8d                   u.5..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 BolusWizard 2013-07-23T21:41:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 292,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 11.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x24                                  [$
    decimal
             91   36
    datetime (2013-07-23T21:41:56)
    0000   0x78 0xe9 0x15 0x17 0x0d                   x....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x70 0x00    .Q.d<dp.
    0008   0x00 0x00 0x00 0x20 0x00 0x50 0x78         ... .Px
    decimal
              0   81    0  100   60  100  112    0
              0    0    0   32    0   80  120
    HOUR BITS: [1, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 2.0, 'curve': 192},
 {'age': 218, 'amount': 1.3, 'curve': 192},
 {'age': 238, 'amount': 0.7, 'curve': 192},
 {'age': 42, 'amount': 0.95, 'curve': 208},
 {'age': 52, 'amount': 0.35, 'curve': 208},
 {'age': 132, 'amount': 1.7, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x50 0x62 0xc0 0x34 0xda 0xc0    \.Pb.4..
    0008   0x1c 0xee 0xc0 0x26 0x2a 0xd0 0x0e 0x34    ...&*..4
    0010   0xd0 0x44 0x84 0xd0                        .D..
    decimal
             92   20   80   98  192   52  218  192
             28  238  192   38   42  208   14   52
            208   68  132  208
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-07-23T21:41:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x20 0x00    ..P.P. .
    decimal
              1    0   80    0   80    0   32    0
    datetime (2013-07-23T21:41:56)
    0000   0x78 0xe9 0x55 0x17 0x0d                   x.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BasalProfileStart 2013-07-24T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-24T00:00:00)
    0000   0x40 0xc0 0x00 0x18 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 9 ResultTotals (2000, 6, 0, 0, 13, 55) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x00                   .....
    decimal
              7    0    0    5    0
    datetime ((2000, 6, 0, 0, 13, 55))
    0000   0x77 0x8d 0x00 0x00 0x00                   w....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x77 0x8d 0x05 0x00 0xcd 0x00 0x00    nw......
    0008   0x0a 0x00 0x00 0x05 0x00 0x02 0xdc 0x39    .......9
    0010   0x02 0x24 0x2b 0x00 0x44 0x00 0xd0 0x01    .$+.D...
    0018   0x10 0x00 0x44 0x00 0x00 0x03 0x05 0x01    ..D.....
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x61 0x24 0x00 0x00 0x00         ..a$...
    decimal
            110  119  141    5    0  205    0    0
             10    0    0    5    0    2  220   57
              2   36   43    0   68    0  208    1
             16    0   68    0    0    3    5    1
              0    4    0    0    0    0    0    0
              0    0   97   36    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 11 LowReservoir 2013-07-24T00:49:39 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-24T00:49:39)
    0000   0x67 0xf1 0x00 0x18 0x0d                   g....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 12 BasalProfileStart 2013-07-24T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-24T04:00:00)
    0000   0x40 0xc0 0x04 0x18 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [1, 1, 0]
#### RECORD 13 BasalProfileStart 2013-07-24T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-24T08:00:00)
    0000   0x40 0xc0 0x08 0x18 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 14 CalBGForPH 2013-07-24T09:28:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-07-24T09:28:17)
    0000   0x51 0xdc 0x29 0x18 0x0d                   Q.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 BolusWizard 2013-07-24T09:28:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2013-07-24T09:28:27)
    0000   0x5b 0xdc 0x09 0x18 0x0d                   [....
    body (15)
    hex
    0000   0x11 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x38 0x00 0x00 0x00 0x00 0x38 0x78         8....8x
    decimal
             17   80    0  120   60  100    0    0
             56    0    0    0    0   56  120
    HOUR BITS: [1, 1, 0]
#### RECORD 16 Bolus 2013-07-24T09:28:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    0    0
    datetime (2013-07-24T09:28:27)
    0000   0x5b 0xdc 0x49 0x18 0x0d                   [.I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 LowReservoir 2013-07-24T10:35:17 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-07-24T10:35:17)
    0000   0x51 0xe3 0x0a 0x18 0x0d                   Q....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 CalBGForPH 2013-07-24T11:55:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-07-24T11:55:52)
    0000   0x74 0xf7 0x2b 0x18 0x0d                   t.+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 BolusWizard 2013-07-24T11:55:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 118,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 12,
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
    0000   0x5b 0x76                                  [v
    decimal
             91  118
    datetime (2013-07-24T11:55:57)
    0000   0x79 0xf7 0x0b 0x78 0x0d                   y..x.
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x0c 0x00 0x28 0x78         (....(x
    decimal
             12   80    0  120   60  100    0    0
             40    0    0   12    0   40  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 2.2, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x98 0xc0                   \.X..
    decimal
             92    5   88  152  192
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-07-24T11:55:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x0c 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   12    0
    datetime (2013-07-24T11:55:57)
    0000   0x79 0xf7 0x4b 0x78 0x0d                   y.Kx.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BasalProfileStart 2013-07-24T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-24T12:00:00)
    0000   0x40 0xc0 0x0c 0x18 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 23 Base (2013, 7, 24, 12, 24, 10) head[2], body[0] op[0x5f]

    op hex (2)
    0000   0x5f 0x05                                  _.
    decimal
             95    5
    datetime ((2013, 7, 24, 12, 24, 10))
    0000   0x4a 0xd8 0x0c 0x18 0x0d                   J....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 Base (2013, 7, 24, 12, 25, 4) head[2], body[0] op[0x67]

    op hex (2)
    0000   0x67 0x00                                  g.
    decimal
            103    0
    datetime ((2013, 7, 24, 12, 25, 4))
    0000   0x44 0xd9 0x0c 0x18 0x0d                   D....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 Base (2012, 4, 25, 4, 1, 38) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1e                                  ..
    decimal
              0   30
    datetime ((2012, 4, 25, 4, 1, 38))
    0000   0x66 0x01 0x44 0xd9 0x0c                   f.D..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 26 NewTimeSet (2012, 4, 25, 29, 0, 40) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime ((2012, 4, 25, 29, 0, 40))
    0000   0x68 0x00 0x5d 0xd9 0x0c                   h.]..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 27 NewTimeSet (2013, 0, 0, 6, 30, 0) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime ((2013, 0, 0, 6, 30, 0))
    0000   0x00 0x1e 0x66 0x00 0x5d                   ..f.]
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 28 Base (2004, 0, 1, 30, 13, 24) head[2], body[0] op[0xd9]

    op hex (2)
    0000   0xd9 0x0c                                  ..
    decimal
            217   12
    datetime ((2004, 0, 1, 30, 13, 24))
    0000   0x18 0x0d 0x1e 0x01 0x74                   ....t
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 29 Base (2007, 0, 3, 27, 13, 24) head[2], body[0] op[0xdb]

    op hex (2)
    0000   0xdb 0x0c                                  ..
    decimal
            219   12
    datetime ((2007, 0, 3, 27, 13, 24))
    0000   0x18 0x0d 0x7b 0x03 0x77                   ..{.w
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 30 Base (2000, 0, 29, 24, 13, 24) head[2], body[0] op[0xdb]

    op hex (2)
    0000   0xdb 0x0c                                  ..
    decimal
            219   12
    datetime ((2000, 0, 29, 24, 13, 24))
    0000   0x18 0x0d 0x18 0x1d 0x00                   .....
    body (0)

#### RECORD 31 PumpResume 2013-07-24T12:27:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-07-24T12:27:55)
    0000   0x77 0xdb 0x0c 0x18 0x0d                   w....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 32 CalBGForPH 2013-07-24T12:41:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-07-24T12:41:24)
    0000   0x58 0xe9 0x2c 0x18 0x0d                   X.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 BolusWizard 2013-07-24T12:41:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
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
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-07-24T12:41:34)
    0000   0x62 0xe9 0x0c 0x18 0x0d                   b....
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x20 0x00 0x28 0x78         (.. .(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0   32    0   40  120
    HOUR BITS: [1, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 1.0, 'curve': 192},
 {'age': 198, 'amount': 2.2, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x30 0xc0 0x58 0xc6 0xc0    \.(0.X..
    decimal
             92    8   40   48  192   88  198  192
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-07-24T12:41:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x20 0x01    ..(.(. .
    decimal
              1    0   40    0   40    0   32    1
    datetime (2013-07-24T12:41:35)
    0000   0x63 0xe9 0x6c 0x18 0x0d                   c.l..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 BolusWizard 2013-07-24T12:42:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.2,
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
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-07-24T12:42:10)
    0000   0x4a 0xea 0x0c 0x18 0x0d                   J....
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x48 0x00 0x28 0x78         (..H.(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0   72    0   40  120
    HOUR BITS: [1, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 1.0, 'curve': 192},
 {'age': 199, 'amount': 2.2, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x31 0xc0 0x58 0xc7 0xc0    \.(1.X..
    decimal
             92    8   40   49  192   88  199  192
    datetime (unknown)

    body (0)

#### RECORD 38 BolusWizard 2013-07-24T12:42:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.2,
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
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-07-24T12:42:53)
    0000   0x75 0xea 0x0c 0x78 0x0d                   u..x.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x20 0x00 0x00 0x48 0x00 0x20 0x78          ..H. x
    decimal
             10   80    0  120   60  100    0    0
             32    0    0   72    0   32  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 0.05, 'curve': 192},
 {'age': 49, 'amount': 1.0, 'curve': 192},
 {'age': 199, 'amount': 2.2, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x02 0x09 0xc0 0x28 0x31 0xc0    \....(1.
    0008   0x58 0xc7 0xc0                             X..
    decimal
             92   11    2    9  192   40   49  192
             88  199  192
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-07-24T12:42:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x24 0x00    ..<.<.$.
    decimal
              1    0   60    0   60    0   36    0
    datetime (2013-07-24T12:42:53)
    0000   0x75 0xea 0x4c 0x78 0x0d                   u.Lx.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 Base (2013, 7, 24, 13, 41, 57) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x00                                  P.
    decimal
             80    0
    datetime ((2013, 7, 24, 13, 41, 57))
    0000   0x79 0xe9 0x0d 0x18 0x0d                   y....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 Base (2000, 0, 20, 28, 0, 30) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x01                                   .
    decimal
             32    1
    datetime ((2000, 0, 20, 28, 0, 30))
    0000   0x1e 0x00 0x3c 0x14 0x00                   ..<..
    body (0)

#### RECORD 43 PumpSuspend (2006, 15, 20, 31, 63, 63) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x3c                                  .<
    decimal
             30   60
    datetime ((2006, 15, 20, 31, 63, 63))
    0000   0xff 0xff 0xff 0xb4 0x46                   ....F
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 44 Base (2004, 0, 28, 0, 30, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x21                                  .!
    decimal
              0   33
    datetime ((2004, 0, 28, 0, 30, 1))
    0000   0x01 0x1e 0x00 0x3c 0x14                   ...<.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 45 Base (2004, 3, 31, 31, 63, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1e                                  ..
    decimal
              0   30
    datetime ((2004, 3, 31, 31, 63, 60))
    0000   0x3c 0xff 0xff 0xff 0xb4                   <....
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 1, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 46 Base (2013, 4, 11, 19, 0, 16) head[2], body[0] op[0x46]

    op hex (2)
    0000   0x46 0x00                                  F.
    decimal
             70    0
    datetime ((2013, 4, 11, 19, 0, 16))
    0000   0x50 0x00 0x53 0xeb 0x0d                   P.S..
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 47 NewTimeSet (2012, 0, 0, 30, 1, 33) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime ((2012, 0, 0, 30, 1, 33))
    0000   0x21 0x01 0x1e 0x00 0x3c                   !...<
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 48 SelectBasalProfile (2015, 0, 31, 31, 60, 30) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x00                                  ..
    decimal
             20    0
    datetime ((2015, 0, 31, 31, 60, 30))
    0000   0x1e 0x3c 0xff 0xff 0xff                   .<...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 49 Base (2000, 0, 30, 1, 32, 0) head[2], body[0] op[0xb4]

    op hex (2)
    0000   0xb4 0x46                                  .F
    decimal
            180   70
    datetime ((2000, 0, 30, 1, 32, 0))
    0000   0x00 0x20 0x01 0x1e 0x00                   . ...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 Base (2015, 0, 31, 28, 30, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x14                                  <.
    decimal
             60   20
    datetime ((2015, 0, 31, 28, 30, 0))
    0000   0x00 0x1e 0x3c 0xff 0xff                   ..<..
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 51 Base (2011, 4, 0, 16, 0, 6) head[2], body[0] op[0xff]

    op hex (2)
    0000   0xff 0xb4                                  ..
    decimal
            255  180
    datetime ((2011, 4, 0, 16, 0, 6))
    0000   0x46 0x00 0x50 0x00 0x5b                   F.P.[
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 52 Base (2014, 0, 1, 0, 13, 24) head[2], body[0] op[0xed]

    op hex (2)
    0000   0xed 0x0d                                  ..
    decimal
            237   13
    datetime ((2014, 0, 1, 0, 13, 24))
    0000   0x18 0x0d 0x20 0x01 0x1e                   .. ..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 53 Base (2015, 0, 28, 30, 0, 20) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x3c                                  .<
    decimal
              0   60
    datetime ((2015, 0, 28, 30, 0, 20))
    0000   0x14 0x00 0x1e 0x3c 0xff                   ...<.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 54 Base (2001, 9, 1, 0, 6, 52) head[2], body[0] op[0xff]

    op hex (2)
    0000   0xff 0xff                                  ..
    decimal
            255  255
    datetime ((2001, 9, 1, 0, 6, 52))
    0000   0xb4 0x46 0x00 0x21 0x01                   .F.!.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
#### RECORD 55 PumpSuspend (2012, 0, 30, 0, 20, 60) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime ((2012, 0, 30, 0, 20, 60))
    0000   0x3c 0x14 0x00 0x1e 0x3c                   <...<
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 56 Base (2000, 14, 0, 6, 52, 63) head[2], body[0] op[0xff]

    op hex (2)
    0000   0xff 0xff                                  ..
    decimal
            255  255
    datetime ((2000, 14, 0, 6, 52, 63))
    0000   0xff 0xb4 0x46 0x00 0x50                   ..F.P
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 57 Base (2001, 12, 13, 24, 13, 49) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x70                                  .p
    decimal
              0  112
    datetime ((2001, 12, 13, 24, 13, 49))
    0000   0xf1 0x0d 0x18 0x0d 0x21                   ....!
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 58 Bolus (2006, 15, 20, 31, 63, 63) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x1e 0x00 0x3c 0x14 0x00 0x1e 0x3c    ...<...<
    decimal
              1   30    0   60   20    0   30   60
    datetime ((2006, 15, 20, 31, 63, 63))
    0000   0xff 0xff 0xff 0xb4 0x46                   ....F
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 59 Base (2004, 0, 28, 0, 30, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x20                                  . 
    decimal
              0   32
    datetime ((2004, 0, 28, 0, 30, 1))
    0000   0x01 0x1e 0x00 0x3c 0x14                   ...<.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 60 Base (2004, 3, 31, 31, 63, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1e                                  ..
    decimal
              0   30
    datetime ((2004, 3, 31, 31, 63, 60))
    0000   0x3c 0xff 0xff 0xff 0xb4                   <....
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 1, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 61 Base (2014, 1, 7, 23, 49, 10) head[2], body[0] op[0x46]

    op hex (2)
    0000   0x46 0x00                                  F.
    decimal
             70    0
    datetime ((2014, 1, 7, 23, 49, 10))
    0000   0x0a 0x71 0x57 0xc7 0x2e                   .qW..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 62 NewTimeSet 2014-01-22T19:40:10 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime (2014-01-22T19:40:10)
    0000   0x0a 0x68 0x73 0xf6 0x2e                   .hs..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 63 NewTimeSet (2014, 5, 23, 27, 40, 27) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime ((2014, 5, 23, 27, 40, 27))
    0000   0x5b 0x68 0x5b 0xf7 0x0e                   [h[..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 1]
#### RECORD 64 Base (2012, 1, 24, 0, 16, 15) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x0d                                  x.
    decimal
            120   13
    datetime ((2012, 1, 24, 0, 16, 15))
    0000   0x0f 0x50 0x00 0x78 0x3c                   .P.x<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 65 ChangeTimeDisplay (2008, 0, 0, 0, 48, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime ((2008, 0, 0, 0, 48, 0))
    0000   0x00 0x30 0x00 0x00 0x18                   .0...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 66 Base (2000, 5, 12, 20, 28, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x30                                  .0
    decimal
              0   48
    datetime ((2000, 5, 12, 20, 28, 56))
    0000   0x78 0x5c 0x14 0x0c 0x70                   x\..p
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 67 Base (2000, 7, 4, 4, 0, 58) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x0c                                  ..
    decimal
            192   12
    datetime ((2000, 7, 4, 4, 0, 58))
    0000   0x7a 0xc0 0x44 0x84 0xc0                   z.D..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 68 ChangeBasalProfile (2008, 12, 0, 22, 40, 0) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x8e                                  ..
    decimal
              8  142
    datetime ((2008, 12, 0, 22, 40, 0))
    0000   0xc0 0x28 0xb6 0xc0 0x58                   .(..X
    body (44)
    hex
    0000   0x4c 0xd0 0x5b 0x68 0x71 0xf7 0x0e 0x18    L.[hq...
    0008   0x0d 0x0f 0x50 0x00 0x78 0x3c 0x64 0x00    ..P.x<d.
    0010   0x00 0x30 0x00 0x00 0x14 0x00 0x30 0x78    .0....0x
    0018   0x5c 0x14 0x0c 0x70 0xc0 0x0c 0x7a 0xc0    \..p..z.
    0020   0x44 0x84 0xc0 0x08 0x8e 0xc0 0x28 0xb6    D.....(.
    0028   0xc0 0x58 0x4c 0xd0                        .XL.
    decimal
             76  208   91  104  113  247   14   24
             13   15   80    0  120   60  100    0
              0   48    0    0   20    0   48  120
             92   20   12  112  192   12  122  192
             68  132  192    8  142  192   40  182
            192   88   76  208
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 69 Bolus 2013-07-24T14:55:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x14 0x00    ..0.0...
    decimal
              1    0   48    0   48    0   20    0
    datetime (2013-07-24T14:55:49)
    0000   0x71 0xf7 0x4e 0x18 0x0d                   q.N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 70 CalBGForPH 2013-07-24T16:05:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-07-24T16:05:39)
    0000   0x67 0xc5 0x30 0x18 0x0d                   g.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 71 BolusWizard 2013-07-24T16:05:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 151,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x97                                  [.
    decimal
             91  151
    datetime (2013-07-24T16:05:49)
    0000   0x71 0xc5 0x10 0x78 0x0d                   q..x.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x14 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x20 0x00 0x40 0x78         @.. .@x
    decimal
             20   80    0  120   60  100   20    0
             64    0    0   32    0   64  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 1.2, 'curve': 192},
 {'age': 182, 'amount': 0.3, 'curve': 192},
 {'age': 192, 'amount': 0.3, 'curve': 192},
 {'age': 202, 'amount': 1.7, 'curve': 192},
 {'age': 212, 'amount': 0.2, 'curve': 192},
 {'age': 252, 'amount': 1.0, 'curve': 192},
 {'age': 146, 'amount': 2.2, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x30 0x48 0xc0 0x0c 0xb6 0xc0    \.0H....
    0008   0x0c 0xc0 0xc0 0x44 0xca 0xc0 0x08 0xd4    ...D....
    0010   0xc0 0x28 0xfc 0xc0 0x58 0x92 0xd0         .(..X..
    decimal
             92   23   48   72  192   12  182  192
             12  192  192   68  202  192    8  212
            192   40  252  192   88  146  208
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-07-24T16:05:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x20 0x00    ..@.@. .
    decimal
              1    0   64    0   64    0   32    0
    datetime (2013-07-24T16:05:50)
    0000   0x72 0xc5 0x50 0x78 0x0d                   r.Px.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 74 CalBGForPH 2013-07-24T16:42:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 211}
```
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2013-07-24T16:42:34)
    0000   0x62 0xea 0x30 0x18 0x0d                   b.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 75 BolusWizard 2013-07-24T16:43:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 211,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd3                                  [.
    decimal
             91  211
    datetime (2013-07-24T16:43:06)
    0000   0x46 0xeb 0x10 0x78 0x0d                   F..x.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x3c 0x00    .P.x<d<.
    0008   0x00 0x00 0x00 0x48 0x00 0x00 0x78         ...H..x
    decimal
              0   80    0  120   60  100   60    0
              0    0    0   72    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 1.6, 'curve': 192},
 {'age': 110, 'amount': 1.2, 'curve': 192},
 {'age': 220, 'amount': 0.3, 'curve': 192},
 {'age': 230, 'amount': 0.3, 'curve': 192},
 {'age': 240, 'amount': 1.7, 'curve': 192},
 {'age': 250, 'amount': 0.2, 'curve': 192},
 {'age': 34, 'amount': 1.0, 'curve': 208},
 {'age': 184, 'amount': 2.2, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x40 0x28 0xc0 0x30 0x6e 0xc0    \.@(.0n.
    0008   0x0c 0xdc 0xc0 0x0c 0xe6 0xc0 0x44 0xf0    ......D.
    0010   0xc0 0x08 0xfa 0xc0 0x28 0x22 0xd0 0x58    ....(".X
    0018   0xb8 0xd0                                  ..
    decimal
             92   26   64   40  192   48  110  192
             12  220  192   12  230  192   68  240
            192    8  250  192   40   34  208   88
            184  208
    datetime (unknown)

    body (0)

#### RECORD 77 Base (2013, 7, 24, 17, 27, 20) head[2], body[0] op[0x83]

    op hex (2)
    0000   0x83 0x01                                  ..
    decimal
            131    1
    datetime ((2013, 7, 24, 17, 27, 20))
    0000   0x54 0xdb 0x11 0x18 0x0d                   T....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 78 Base (2013, 7, 24, 17, 27, 25) head[2], body[0] op[0x83]

    op hex (2)
    0000   0x83 0x00                                  ..
    decimal
            131    0
    datetime ((2013, 7, 24, 17, 27, 25))
    0000   0x59 0xdb 0x11 0x18 0x0d                   Y....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 Base (2013, 7, 24, 17, 28, 9) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2013, 7, 24, 17, 28, 9))
    0000   0x49 0xdc 0x11 0x18 0x0d                   I....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 80 Base (2013, 7, 24, 17, 29, 22) head[2], body[0] op[0x23]

    op hex (2)
    0000   0x23 0x01                                  #.
    decimal
             35    1
    datetime ((2013, 7, 24, 17, 29, 22))
    0000   0x56 0xdd 0x11 0x18 0x0d                   V....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 81 Base (2013, 7, 24, 17, 29, 37) head[2], body[0] op[0x23]

    op hex (2)
    0000   0x23 0x00                                  #.
    decimal
             35    0
    datetime ((2013, 7, 24, 17, 29, 37))
    0000   0x65 0xdd 0x11 0x18 0x0d                   e....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 82 ChangeTimeDisplay 2013-07-24T17:31:11 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-07-24T17:31:11)
    0000   0x4b 0xdf 0x11 0x18 0x0d                   K....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 83 CalBGForPH 2013-07-24T21:51:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-07-24T21:51:57)
    0000   0x79 0xf3 0x35 0x18 0x0d                   y.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 84 BolusWizard 2013-07-24T21:52:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 36,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-07-24T21:52:11)
    0000   0x4b 0xf4 0x15 0x78 0x0d                   K..x.
    body (15)
    hex
    0000   0x24 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    $P.d<d..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x78         ......x
    decimal
             36   80    0  100   60  100    0    0
            144    0    0    0    0  144  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 85 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 1.6, 'curve': 208},
 {'age': 163, 'amount': 1.2, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x5d 0xd0 0x30 0xa3 0xd0    \.@].0..
    decimal
             92    8   64   93  208   48  163  208
    datetime (unknown)

    body (0)

#### RECORD 86 Bolus 2013-07-24T21:52:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-07-24T21:52:11)
    0000   0x4b 0xf4 0x55 0x78 0x0d                   K.Ux.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 87 CalBGForPH 2013-07-24T22:54:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-07-24T22:54:48)
    0000   0x70 0xf6 0x36 0x18 0x0d                   p.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 88 BolusWizard 2013-07-24T22:54:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.2,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2013-07-24T22:54:56)
    0000   0x78 0xf6 0x16 0x78 0x0d                   x..x.
    body (15)
    hex
    0000   0x11 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x44 0x00 0x00 0x48 0x00 0x44 0x78         D..H.Dx
    decimal
             17   80    0  100   60  100    0    0
             68    0    0   72    0   68  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-20.data: 89 records`
