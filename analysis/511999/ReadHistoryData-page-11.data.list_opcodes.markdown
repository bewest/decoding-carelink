## START logs/ReadHistoryData-page-11.data
#### RECORD 0 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 1.8, 'curve': 192},
 {'age': 240, 'amount': 0.3, 'curve': 192},
 {'age': 14, 'amount': 1.6, 'curve': 208},
 {'age': 144, 'amount': 1.7, 'curve': 208},
 {'age': 184, 'amount': 1.4, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x96 0xc0 0x0c 0xf0 0xc0    \.H.....
    0008   0x40 0x0e 0xd0 0x44 0x90 0xd0 0x38 0xb8    @..D..8.
    0010   0xd0                                       .
    decimal
             92   17   72  150  192   12  240  192
             64   14  208   68  144  208   56  184
            208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-08-09T21:23:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x0c 0x00    ..8.8...
    decimal
              1    0   56    0   56    0   12    0
    datetime (2013-08-09T21:23:43)
    0000   0xab 0x17 0x55 0x09 0x0d                   ..U..
    body (0)

#### RECORD 2 CalBGForPH 2013-08-09T22:48:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-08-09T22:48:04)
    0000   0x84 0x30 0x36 0x09 0x0d                   .06..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 BolusWizard 2013-08-09T22:48:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-08-09T22:48:21)
    0000   0x95 0x30 0x16 0x69 0x0d                   .0.i.
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x30 0x00 0x00 0x1c 0x00 0x30 0x78         0....0x
    decimal
             12   80    0  100   60  100    0    0
             48    0    0   28    0   48  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 1.4, 'curve': 192},
 {'age': 235, 'amount': 1.8, 'curve': 192},
 {'age': 69, 'amount': 0.3, 'curve': 208},
 {'age': 99, 'amount': 1.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x55 0xc0 0x48 0xeb 0xc0    \.8U.H..
    0008   0x0c 0x45 0xd0 0x40 0x63 0xd0              .E.@c.
    decimal
             92   14   56   85  192   72  235  192
             12   69  208   64   99  208
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-08-09T22:48:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x1c 0x00    ..0.0...
    decimal
              1    0   48    0   48    0   28    0
    datetime (2013-08-09T22:48:22)
    0000   0x96 0x30 0x56 0x69 0x0d                   .0Vi.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2013-08-09T22:53:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-08-09T22:53:18)
    0000   0x92 0x35 0x16 0x09 0x0d                   .5...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x00 0x00 0x00 0x4c 0x00 0x00 0x78         ...L..x
    decimal
              0   80    0  100   60  100    0    0
              0    0    0   76    0    0  120
    HOUR BITS: [0, 0, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 1.2, 'curve': 192},
 {'age': 90, 'amount': 1.4, 'curve': 192},
 {'age': 240, 'amount': 1.8, 'curve': 192},
 {'age': 74, 'amount': 0.3, 'curve': 208},
 {'age': 104, 'amount': 1.6, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x30 0x0a 0xc0 0x38 0x5a 0xc0    \.0..8Z.
    0008   0x48 0xf0 0xc0 0x0c 0x4a 0xd0 0x40 0x68    H...J.@h
    0010   0xd0                                       .
    decimal
             92   17   48   10  192   56   90  192
             72  240  192   12   74  208   64  104
            208
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-08-09T22:53:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x4c 0x00    ..H.H.L.
    decimal
              1    0   72    0   72    0   76    0
    datetime (2013-08-09T22:53:18)
    0000   0x92 0x35 0x56 0x09 0x0d                   .5V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 9 CalBGForPH 2013-08-09T23:14:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 240}
```
    op hex (2)
    0000   0x0a 0xf0                                  ..
    decimal
             10  240
    datetime (2013-08-09T23:14:41)
    0000   0xa9 0x0e 0x37 0x09 0x0d                   ..7..
    body (0)

#### RECORD 10 BolusWizard 2013-08-09T23:14:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 240,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 13.2,
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
    0000   0x5b 0xf0                                  [.
    decimal
             91  240
    datetime (2013-08-09T23:14:48)
    0000   0xb0 0x0e 0x17 0x09 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x50 0x00    .P.d<dP.
    0008   0x00 0x00 0x00 0x84 0x00 0x00 0x78         ......x
    decimal
              0   80    0  100   60  100   80    0
              0    0    0  132    0    0  120

#### RECORD 11 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 1.8, 'curve': 192},
 {'age': 31, 'amount': 1.2, 'curve': 192},
 {'age': 111, 'amount': 1.4, 'curve': 192},
 {'age': 5, 'amount': 1.8, 'curve': 208},
 {'age': 95, 'amount': 0.3, 'curve': 208},
 {'age': 125, 'amount': 1.6, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x15 0xc0 0x30 0x1f 0xc0    \.H..0..
    0008   0x38 0x6f 0xc0 0x48 0x05 0xd0 0x0c 0x5f    8o.H..._
    0010   0xd0 0x40 0x7d 0xd0                        .@}.
    decimal
             92   20   72   21  192   48   31  192
             56  111  192   72    5  208   12   95
            208   64  125  208
    datetime (unknown)

    body (0)

#### RECORD 12 BasalProfileStart 2013-08-10T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-10T00:00:00)
    0000   0x80 0x00 0x00 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 13 ResultTotals (2000, 8, 0, 0, 13, 9) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime ((2000, 8, 0, 0, 13, 9))
    0000   0x89 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x89 0x0d 0x05 0x00 0x87 0x00 0x00    n.......
    0008   0x0a 0x00 0x00 0x05 0x08 0x02 0xdc 0x39    .......9
    0010   0x02 0x2c 0x2b 0x00 0x83 0x01 0xd8 0x00    .,+.....
    0018   0x54 0x00 0x00 0x00 0x00 0x08 0x02 0x00    T.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0xf0 0x00 0x00 0x00 0x00    ..d.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  137   13    5    0  135    0    0
             10    0    0    5    8    2  220   57
              2   44   43    0  131    1  216    0
             84    0    0    0    0    8    2    0
              0    0    0    0    0    0    0    0
              0    0  100  240    0    0    0    0
              0    0    0

#### RECORD 14 Base (2010, 6, 1, 20, 41, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x34                                  .4
    decimal
              0   52
    datetime ((2010, 6, 1, 20, 41, 36))
    0000   0x64 0xa9 0x14 0x01 0x0a                   d....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 15 Base (2010, 2, 4, 0, 0, 1) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x7b                                  .{
    decimal
             13  123
    datetime ((2010, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x0a                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 Base (2000, 0, 2, 16, 13, 10) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 10))
    0000   0x0a 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 18 CalBGForPH 2013-08-10T11:42:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 322}
```
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2013-08-10T11:42:00)
    0000   0x80 0x2a 0x2b 0x0a 0x8d                   .*+..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 19 BolusWizard 2013-08-10T11:42:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 322,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 1,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 13.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x42                                  [B
    decimal
             91   66
    datetime (2013-08-10T11:42:09)
    0000   0x89 0x2a 0x0b 0x0a 0x0d                   .*...
    body (15)
    hex
    0000   0x01 0x51 0x00 0x78 0x3c 0x64 0x84 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x00 0x00 0x84 0x78         ......x
    decimal
              1   81    0  120   60  100  132    0
              0    0    0    0    0  132  120
    HOUR BITS: [0, 0, 1]
#### RECORD 20 Bolus 2013-08-10T11:42:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2013-08-10T11:42:09)
    0000   0x89 0x2a 0x4b 0x0a 0x0d                   .*K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 21 Rewind 2013-08-10T11:45:29 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-10T11:45:29)
    0000   0x9d 0x2d 0x0b 0x0a 0x0d                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 Prime 2013-08-10T11:46:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x26                   ....&
    decimal
              3    0    0    0   38
    datetime (2013-08-10T11:46:18)
    0000   0x92 0x2e 0x2b 0x0a 0x0d                   ..+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 23 BasalProfileStart 2013-08-10T11:46:47 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-10T11:46:47)
    0000   0xaf 0x2e 0x0b 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [0, 0, 1]
#### RECORD 24 CalBGForPH 2013-08-10T11:51:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2013-08-10T11:51:11)
    0000   0x8b 0x33 0x2b 0x0a 0x0d                   .3+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 25 BolusWizard 2013-08-10T11:51:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 170,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2013-08-10T11:51:24)
    0000   0x98 0x33 0x0b 0x0a 0x0d                   .3...
    body (15)
    hex
    0000   0x12 0x50 0x00 0x78 0x3c 0x64 0x20 0x00    .P.x<d .
    0008   0x3c 0x00 0x00 0x44 0x00 0x3c 0x78         <..D.<x
    decimal
             18   80    0  120   60  100   32    0
             60    0    0   68    0   60  120
    HOUR BITS: [0, 0, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.45, 'curve': 192},
 {'age': 18, 'amount': 1.25, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x12 0x08 0xc0 0x32 0x12 0xc0    \....2..
    decimal
             92    8   18    8  192   50   18  192
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-08-10T11:51:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x44 0x00    ..<.<.D.
    decimal
              1    0   60    0   60    0   68    0
    datetime (2013-08-10T11:51:24)
    0000   0x98 0x33 0x4b 0x0a 0x0d                   .3K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 BasalProfileStart 2013-08-10T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-10T12:00:00)
    0000   0x80 0x00 0x0c 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 29 Rewind 2013-08-10T14:54:04 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-10T14:54:04)
    0000   0x84 0x36 0x0e 0x0a 0x0d                   .6...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 Prime 2013-08-10T14:54:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 9.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x60                   ....`
    decimal
              3    0    0    0   96
    datetime (2013-08-10T14:54:30)
    0000   0x9e 0x36 0x2e 0x0a 0x0d                   .6...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 BasalProfileStart 2013-08-10T14:55:40 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-10T14:55:40)
    0000   0xa8 0x37 0x0e 0x0a 0x0d                   .7...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 0, 1]
#### RECORD 32 Prime 2013-08-10T14:55:05 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-10T14:55:05)
    0000   0x85 0x37 0x0e 0x0a 0x0d                   .7...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 CalBGForPH 2013-08-10T14:56:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2013-08-10T14:56:37)
    0000   0xa5 0x38 0x2e 0x0a 0x8d                   .8...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 BolusWizard 2013-08-10T14:56:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 268,
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
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2013-08-10T14:56:40)
    0000   0xa8 0x38 0x0e 0x0a 0x0d                   .8...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x60 0x00    .Q.x<d`.
    0008   0x00 0x00 0x00 0x00 0x00 0x60 0x78         .....`x
    decimal
              0   81    0  120   60  100   96    0
              0    0    0    0    0   96  120
    HOUR BITS: [0, 0, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 1.95, 'curve': 192},
 {'age': 203, 'amount': 1.25, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x4e 0xc1 0xc0 0x32 0xcb 0xc0    \.N..2..
    decimal
             92    8   78  193  192   50  203  192
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-08-10T14:56:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x00 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    0    0
    datetime (2013-08-10T14:56:40)
    0000   0xa8 0x38 0x4e 0x0a 0x0d                   .8N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 CalBGForPH 2013-08-10T15:30:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-08-10T15:30:19)
    0000   0x93 0x1e 0x2f 0x0a 0x0d                   ../..
    body (0)

#### RECORD 38 BolusWizard 2013-08-10T15:30:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 115,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.4,
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
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-08-10T15:30:24)
    0000   0x98 0x1e 0x0f 0x0a 0x0d                   .....
    body (15)
    hex
    0000   0x11 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x38 0x00 0x00 0x54 0x00 0x38 0x78         8..T.8x
    decimal
             17   80    0  120   60  100    0    0
             56    0    0   84    0   56  120

#### RECORD 39 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 2.4, 'curve': 192},
 {'age': 227, 'amount': 1.95, 'curve': 192},
 {'age': 237, 'amount': 1.25, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x60 0x25 0xc0 0x4e 0xe3 0xc0    \.`%.N..
    0008   0x32 0xed 0xc0                             2..
    decimal
             92   11   96   37  192   78  227  192
             50  237  192
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-08-10T15:30:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x54 0x00    ..8.8.T.
    decimal
              1    0   56    0   56    0   84    0
    datetime (2013-08-10T15:30:24)
    0000   0x98 0x1e 0x4f 0x0a 0x0d                   ..O..
    body (0)

#### RECORD 41 CalBGForPH 2013-08-10T16:19:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-10T16:19:14)
    0000   0x8e 0x13 0x30 0x0a 0x0d                   ..0..
    body (0)

#### RECORD 42 BolusWizard 2013-08-10T16:19:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 9.2,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-10T16:19:46)
    0000   0xae 0x13 0x10 0x0a 0x0d                   .....
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x24 0x00 0x00 0x5c 0x00 0x24 0x78         $..\.$x
    decimal
             11   80    0  120   60  100    0    0
             36    0    0   92    0   36  120

#### RECORD 43 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 1.4, 'curve': 192},
 {'age': 86, 'amount': 2.4, 'curve': 192},
 {'age': 20, 'amount': 1.95, 'curve': 208},
 {'age': 30, 'amount': 1.25, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x38 0xc0 0x60 0x56 0xc0    \.88.`V.
    0008   0x4e 0x14 0xd0 0x32 0x1e 0xd0              N..2..
    decimal
             92   14   56   56  192   96   86  192
             78   20  208   50   30  208
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-08-10T16:19:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x5c 0x00    ..$.$.\.
    decimal
              1    0   36    0   36    0   92    0
    datetime (2013-08-10T16:19:46)
    0000   0xae 0x13 0x50 0x0a 0x0d                   ..P..
    body (0)

#### RECORD 45 BolusWizard 2013-08-10T16:21:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 12.4,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-10T16:21:12)
    0000   0x8c 0x15 0x10 0x0a 0x0d                   .....
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x7c 0x00 0x28 0x78         (..|.(x
    decimal
             12   80    0  120   60  100    0    0
             40    0    0  124    0   40  120

#### RECORD 46 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.9, 'curve': 192},
 {'age': 58, 'amount': 1.4, 'curve': 92},
 {'age': 72, 'amount': 0.425, 'curve': 150},
 {'age': 12, 'amount': 4.8, 'curve': 240},
 {'age': 64, 'amount': 4.8, 'curve': 14}]
```
    op hex (17)
    0000   0x5c 0x11 0x24 0x08 0xc0 0x38 0x3a 0x5c    \.$..8:\
    0008   0x11 0x48 0x96 0xc0 0x0c 0xf0 0xc0 0x40    .H.....@
    0010   0x0e                                       .
    decimal
             92   17   36    8  192   56   58   92
             17   72  150  192   12  240  192   64
             14
    datetime (unknown)

    body (0)

#### RECORD 47 Base (2000, 11, 24, 24, 16, 16) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x44                                  .D
    decimal
            208   68
    datetime ((2000, 11, 24, 24, 16, 16))
    0000   0x90 0xd0 0x38 0xb8 0xd0                   ..8..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 48 Bolus 2013-08-09T21:23:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x0c 0x00    ..8.8...
    decimal
              1    0   56    0   56    0   12    0
    datetime (2013-08-09T21:23:43)
    0000   0xab 0x17 0x55 0x09 0x0d                   ..U..
    body (0)

#### RECORD 49 CalBGForPH 2013-08-09T22:48:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-08-09T22:48:04)
    0000   0x84 0x30 0x36 0x09 0x0d                   .06..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 BolusWizard 2013-08-09T22:48:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-08-09T22:48:21)
    0000   0x95 0x30 0x16 0x69 0x0d                   .0.i.
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x30 0x00 0x00 0x1c 0x00 0x30 0x78         0....0x
    decimal
             12   80    0  100   60  100    0    0
             48    0    0   28    0   48  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 1.4, 'curve': 192},
 {'age': 235, 'amount': 1.8, 'curve': 192},
 {'age': 69, 'amount': 0.3, 'curve': 208},
 {'age': 99, 'amount': 1.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x55 0xc0 0x48 0xeb 0xc0    \.8U.H..
    0008   0x0c 0x45 0xd0 0x40 0x63 0xd0              .E.@c.
    decimal
             92   14   56   85  192   72  235  192
             12   69  208   64   99  208
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-08-09T22:48:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x1c 0x00    ..0.0...
    decimal
              1    0   48    0   48    0   28    0
    datetime (2013-08-09T22:48:22)
    0000   0x96 0x30 0x56 0x69 0x0d                   .0Vi.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 53 BolusWizard 2013-08-09T22:53:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-08-09T22:53:18)
    0000   0x92 0x35 0x16 0x09 0x0d                   .5...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x00 0x00 0x00 0x4c 0x00 0x00 0x78         ...L..x
    decimal
              0   80    0  100   60  100    0    0
              0    0    0   76    0    0  120
    HOUR BITS: [0, 0, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 1.2, 'curve': 192},
 {'age': 90, 'amount': 1.4, 'curve': 192},
 {'age': 240, 'amount': 1.8, 'curve': 192},
 {'age': 74, 'amount': 0.3, 'curve': 208},
 {'age': 104, 'amount': 1.6, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x30 0x0a 0xc0 0x38 0x5a 0xc0    \.0..8Z.
    0008   0x48 0xf0 0xc0 0x0c 0x4a 0xd0 0x40 0x68    H...J.@h
    0010   0xd0                                       .
    decimal
             92   17   48   10  192   56   90  192
             72  240  192   12   74  208   64  104
            208
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-08-09T22:53:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x4c 0x00    ..H.H.L.
    decimal
              1    0   72    0   72    0   76    0
    datetime (2013-08-09T22:53:18)
    0000   0x92 0x35 0x56 0x09 0x0d                   .5V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 CalBGForPH 2013-08-09T23:14:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 240}
```
    op hex (2)
    0000   0x0a 0xf0                                  ..
    decimal
             10  240
    datetime (2013-08-09T23:14:41)
    0000   0xa9 0x0e 0x37 0x09 0x0d                   ..7..
    body (0)

#### RECORD 57 BolusWizard 2013-08-09T23:14:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 240,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 13.2,
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
    0000   0x5b 0xf0                                  [.
    decimal
             91  240
    datetime (2013-08-09T23:14:48)
    0000   0xb0 0x0e 0x17 0x09 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x50 0x00    .P.d<dP.
    0008   0x00 0x00 0x00 0x84 0x00 0x00 0x78         ......x
    decimal
              0   80    0  100   60  100   80    0
              0    0    0  132    0    0  120

#### RECORD 58 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 1.8, 'curve': 192},
 {'age': 31, 'amount': 1.2, 'curve': 192},
 {'age': 111, 'amount': 1.4, 'curve': 192},
 {'age': 5, 'amount': 1.8, 'curve': 208},
 {'age': 95, 'amount': 0.3, 'curve': 208},
 {'age': 125, 'amount': 1.6, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x15 0xc0 0x30 0x1f 0xc0    \.H..0..
    0008   0x38 0x6f 0xc0 0x48 0x05 0xd0 0x0c 0x5f    8o.H..._
    0010   0xd0 0x40 0x7d 0xd0                        .@}.
    decimal
             92   20   72   21  192   48   31  192
             56  111  192   72    5  208   12   95
            208   64  125  208
    datetime (unknown)

    body (0)

#### RECORD 59 BasalProfileStart 2013-08-10T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-10T00:00:00)
    0000   0x80 0x00 0x00 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 60 ResultTotals (2000, 8, 0, 0, 13, 9) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime ((2000, 8, 0, 0, 13, 9))
    0000   0x89 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x89 0x0d 0x05 0x00 0x87 0x00 0x00    n.......
    0008   0x0a 0x00 0x00 0x05 0x08 0x02 0xdc 0x39    .......9
    0010   0x02 0x2c 0x2b 0x00 0x83 0x01 0xd8 0x00    .,+.....
    0018   0x54 0x00 0x00 0x00 0x00 0x08 0x02 0x00    T.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0xf0 0x00 0x00 0x00 0x00    ..d.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  137   13    5    0  135    0    0
             10    0    0    5    8    2  220   57
              2   44   43    0  131    1  216    0
             84    0    0    0    0    8    2    0
              0    0    0    0    0    0    0    0
              0    0  100  240    0    0    0    0
              0    0    0

#### RECORD 61 Base (2010, 6, 1, 20, 41, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x34                                  .4
    decimal
              0   52
    datetime ((2010, 6, 1, 20, 41, 36))
    0000   0x64 0xa9 0x14 0x01 0x0a                   d....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 62 Base (2010, 2, 4, 0, 0, 1) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x7b                                  .{
    decimal
             13  123
    datetime ((2010, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x0a                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 64 Base (2000, 0, 2, 16, 13, 10) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 10))
    0000   0x0a 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 65 CalBGForPH 2013-08-10T11:42:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 322}
```
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2013-08-10T11:42:00)
    0000   0x80 0x2a 0x2b 0x0a 0x8d                   .*+..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 66 BolusWizard 2013-08-10T11:42:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 322,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 1,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 13.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x42                                  [B
    decimal
             91   66
    datetime (2013-08-10T11:42:09)
    0000   0x89 0x2a 0x0b 0x0a 0x0d                   .*...
    body (15)
    hex
    0000   0x01 0x51 0x00 0x78 0x3c 0x64 0x84 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x00 0x00 0x84 0x78         ......x
    decimal
              1   81    0  120   60  100  132    0
              0    0    0    0    0  132  120
    HOUR BITS: [0, 0, 1]
#### RECORD 67 Bolus 2013-08-10T11:42:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2013-08-10T11:42:09)
    0000   0x89 0x2a 0x4b 0x0a 0x0d                   .*K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 68 Rewind 2013-08-10T11:45:29 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-10T11:45:29)
    0000   0x9d 0x2d 0x0b 0x0a 0x0d                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 Prime 2013-08-10T11:46:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x26                   ....&
    decimal
              3    0    0    0   38
    datetime (2013-08-10T11:46:18)
    0000   0x92 0x2e 0x2b 0x0a 0x0d                   ..+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 BasalProfileStart 2013-08-10T11:46:47 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-10T11:46:47)
    0000   0xaf 0x2e 0x0b 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [0, 0, 1]
#### RECORD 71 CalBGForPH 2013-08-10T11:51:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2013-08-10T11:51:11)
    0000   0x8b 0x33 0x2b 0x0a 0x0d                   .3+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 72 BolusWizard 2013-08-10T11:51:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 170,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2013-08-10T11:51:24)
    0000   0x98 0x33 0x0b 0x0a 0x0d                   .3...
    body (15)
    hex
    0000   0x12 0x50 0x00 0x78 0x3c 0x64 0x20 0x00    .P.x<d .
    0008   0x3c 0x00 0x00 0x44 0x00 0x3c 0x78         <..D.<x
    decimal
             18   80    0  120   60  100   32    0
             60    0    0   68    0   60  120
    HOUR BITS: [0, 0, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.45, 'curve': 192},
 {'age': 18, 'amount': 1.25, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x12 0x08 0xc0 0x32 0x12 0xc0    \....2..
    decimal
             92    8   18    8  192   50   18  192
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2013-08-10T11:51:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x44 0x00    ..<.<.D.
    decimal
              1    0   60    0   60    0   68    0
    datetime (2013-08-10T11:51:24)
    0000   0x98 0x33 0x4b 0x0a 0x0d                   .3K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 75 BasalProfileStart 2013-08-10T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-10T12:00:00)
    0000   0x80 0x00 0x0c 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 76 Rewind 2013-08-10T14:54:04 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-10T14:54:04)
    0000   0x84 0x36 0x0e 0x0a 0x0d                   .6...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 77 Prime 2013-08-10T14:54:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 9.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x60                   ....`
    decimal
              3    0    0    0   96
    datetime (2013-08-10T14:54:30)
    0000   0x9e 0x36 0x2e 0x0a 0x0d                   .6...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 78 BasalProfileStart 2013-08-10T14:55:40 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-10T14:55:40)
    0000   0xa8 0x37 0x0e 0x0a 0x0d                   .7...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 0, 1]
#### RECORD 79 Prime 2013-08-10T14:55:05 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-10T14:55:05)
    0000   0x85 0x37 0x0e 0x0a 0x0d                   .7...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 80 CalBGForPH 2013-08-10T14:56:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2013-08-10T14:56:37)
    0000   0xa5 0x38 0x2e 0x0a 0x8d                   .8...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 81 BolusWizard 2013-08-10T14:56:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 268,
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
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2013-08-10T14:56:40)
    0000   0xa8 0x38 0x0e 0x0a 0x0d                   .8...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x60 0x00    .Q.x<d`.
    0008   0x00 0x00 0x00 0x00 0x00 0x60 0x78         .....`x
    decimal
              0   81    0  120   60  100   96    0
              0    0    0    0    0   96  120
    HOUR BITS: [0, 0, 1]
#### RECORD 82 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 1.95, 'curve': 192},
 {'age': 203, 'amount': 1.25, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x4e 0xc1 0xc0 0x32 0xcb 0xc0    \.N..2..
    decimal
             92    8   78  193  192   50  203  192
    datetime (unknown)

    body (0)

#### RECORD 83 Bolus 2013-08-10T14:56:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x00 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    0    0
    datetime (2013-08-10T14:56:40)
    0000   0xa8 0x38 0x4e 0x0a 0x0d                   .8N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 84 CalBGForPH 2013-08-10T15:30:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-08-10T15:30:19)
    0000   0x93 0x1e 0x2f 0x0a 0x0d                   ../..
    body (0)

#### RECORD 85 BolusWizard 2013-08-10T15:30:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 115,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.4,
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
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-08-10T15:30:24)
    0000   0x98 0x1e 0x0f 0x0a 0x0d                   .....
    body (15)
    hex
    0000   0x11 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x38 0x00 0x00 0x54 0x00 0x38 0x78         8..T.8x
    decimal
             17   80    0  120   60  100    0    0
             56    0    0   84    0   56  120

#### RECORD 86 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 2.4, 'curve': 192},
 {'age': 227, 'amount': 1.95, 'curve': 192},
 {'age': 237, 'amount': 1.25, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x60 0x25 0xc0 0x4e 0xe3 0xc0    \.`%.N..
    0008   0x32 0xed 0xc0                             2..
    decimal
             92   11   96   37  192   78  227  192
             50  237  192
    datetime (unknown)

    body (0)

#### RECORD 87 Bolus 2013-08-10T15:30:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x54 0x00    ..8.8.T.
    decimal
              1    0   56    0   56    0   84    0
    datetime (2013-08-10T15:30:24)
    0000   0x98 0x1e 0x4f 0x0a 0x0d                   ..O..
    body (0)

#### RECORD 88 CalBGForPH 2013-08-10T16:19:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-10T16:19:14)
    0000   0x8e 0x13 0x30 0x0a 0x0d                   ..0..
    body (0)

#### RECORD 89 BolusWizard 2013-08-10T16:19:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 9.2,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-10T16:19:46)
    0000   0xae 0x13 0x10 0x0a 0x0d                   .....
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x24 0x00 0x00 0x5c 0x00 0x24 0x78         $..\.$x
    decimal
             11   80    0  120   60  100    0    0
             36    0    0   92    0   36  120

#### RECORD 90 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 1.4, 'curve': 192},
 {'age': 86, 'amount': 2.4, 'curve': 192},
 {'age': 20, 'amount': 1.95, 'curve': 208},
 {'age': 30, 'amount': 1.25, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x38 0xc0 0x60 0x56 0xc0    \.88.`V.
    0008   0x4e 0x14 0xd0 0x32 0x1e 0xd0              N..2..
    decimal
             92   14   56   56  192   96   86  192
             78   20  208   50   30  208
    datetime (unknown)

    body (0)

#### RECORD 91 Bolus 2013-08-10T16:19:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x5c 0x00    ..$.$.\.
    decimal
              1    0   36    0   36    0   92    0
    datetime (2013-08-10T16:19:46)
    0000   0xae 0x13 0x50 0x0a 0x0d                   ..P..
    body (0)

#### RECORD 92 BolusWizard 2013-08-10T16:21:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 12.4,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-10T16:21:12)
    0000   0x8c 0x15 0x10 0x0a 0x0d                   .....
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x7c 0x00 0x28 0x78         (..|.(x
    decimal
             12   80    0  120   60  100    0    0
             40    0    0  124    0   40  120

#### RECORD 93 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.9, 'curve': 192},
 {'age': 58, 'amount': 1.4, 'curve': 192},
 {'age': 88, 'amount': 2.4, 'curve': 192},
 {'age': 22, 'amount': 1.95, 'curve': 208},
 {'age': 32, 'amount': 1.25, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x24 0x08 0xc0 0x38 0x3a 0xc0    \.$..8:.
    0008   0x60 0x58 0xc0 0x4e 0x16 0xd0 0x32 0x20    `X.N..2 
    0010   0xd0                                       .
    decimal
             92   17   36    8  192   56   58  192
             96   88  192   78   22  208   50   32
            208
    datetime (unknown)

    body (0)

#### RECORD 94 Bolus 2013-08-10T16:21:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x7c 0x00    ..(.(.|.
    decimal
              1    0   40    0   40    0  124    0
    datetime (2013-08-10T16:21:12)
    0000   0x8c 0x15 0x50 0x0a 0x0d                   ..P..
    body (0)

#### RECORD 95 CalBGForPH 2013-08-10T16:59:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-08-10T16:59:51)
    0000   0xb3 0x3b 0x30 0x0a 0x0d                   .;0..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 96 BolusWizard 2013-08-10T16:59:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-08-10T16:59:58)
    0000   0xba 0x3b 0x10 0x0a 0x0d                   .;...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x00 0x00 0x00 0x6c 0x00 0x00 0x78         ...l..x
    decimal
              0   80    0  120   60  100   44    0
              0    0    0  108    0    0  120
    HOUR BITS: [0, 0, 1]
#### RECORD 97 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 1.9, 'curve': 192},
 {'age': 96, 'amount': 1.4, 'curve': 192},
 {'age': 126, 'amount': 2.4, 'curve': 192},
 {'age': 60, 'amount': 1.95, 'curve': 208},
 {'age': 70, 'amount': 1.25, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x4c 0x2e 0xc0 0x38 0x60 0xc0    \.L..8`.
    0008   0x60 0x7e 0xc0 0x4e 0x3c 0xd0 0x32 0x46    `~.N<.2F
    0010   0xd0                                       .
    decimal
             92   17   76   46  192   56   96  192
             96  126  192   78   60  208   50   70
            208
    datetime (unknown)

    body (0)

#### RECORD 98 CalBGForPH 2013-08-10T17:19:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 134}
```
    op hex (2)
    0000   0x0a 0x86                                  ..
    decimal
             10  134
    datetime (2013-08-10T17:19:37)
    0000   0xa5 0x13 0x31 0x0a 0x0d                   ..1..
    body (0)

#### RECORD 99 BolusWizard 2013-08-10T17:19:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 134,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x86                                  [.
    decimal
             91  134
    datetime (2013-08-10T17:19:46)
    0000   0xae 0x13 0x11 0x0a 0x0d                   .....
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x3c 0x64 0x08 0x00    .P.d<d..
    0008   0x78 0x00 0x00 0x50 0x00 0x78 0x78         x..P.xx
    decimal
             30   80    0  100   60  100    8    0
            120    0    0   80    0  120  120

#### RECORD 100 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 1.9, 'curve': 192},
 {'age': 116, 'amount': 1.4, 'curve': 192},
 {'age': 146, 'amount': 2.4, 'curve': 192},
 {'age': 80, 'amount': 1.95, 'curve': 208},
 {'age': 90, 'amount': 1.25, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x4c 0x42 0xc0 0x38 0x74 0xc0    \.LB.8t.
    0008   0x60 0x92 0xc0 0x4e 0x50 0xd0 0x32 0x5a    `..NP.2Z
    0010   0xd0                                       .
    decimal
             92   17   76   66  192   56  116  192
             96  146  192   78   80  208   50   90
            208
    datetime (unknown)

    body (0)

#### RECORD 101 Bolus 2013-08-10T17:19:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x50 0x00    ..x.x.P.
    decimal
              1    0  120    0  120    0   80    0
    datetime (2013-08-10T17:19:46)
    0000   0xae 0x13 0x51 0x0a 0x0d                   ..Q..
    body (0)

#### RECORD 102 CalBGForPH 2013-08-10T18:06:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-10T18:06:57)
    0000   0xb9 0x06 0x32 0x0a 0x0d                   ..2..
    body (0)

#### RECORD 103 BolusWizard 2013-08-10T18:07:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 12.0,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-10T18:07:04)
    0000   0x84 0x07 0x12 0x0a 0x0d                   .....
    body (15)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x50 0x00 0x00 0x78 0x00 0x50 0x78         P..x.Px
    decimal
             20   80    0  100   60  100    0    0
             80    0    0  120    0   80  120

#### RECORD 104 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 3.0, 'curve': 192},
 {'age': 114, 'amount': 1.9, 'curve': 192},
 {'age': 164, 'amount': 1.4, 'curve': 192},
 {'age': 194, 'amount': 2.4, 'curve': 192},
 {'age': 128, 'amount': 1.95, 'curve': 208},
 {'age': 138, 'amount': 1.25, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x78 0x36 0xc0 0x4c 0x72 0xc0    \.x6.Lr.
    0008   0x38 0xa4 0xc0 0x60 0xc2 0xc0 0x4e 0x80    8..`..N.
    0010   0xd0 0x32 0x8a 0xd0                        .2..
    decimal
             92   20  120   54  192   76  114  192
             56  164  192   96  194  192   78  128
            208   50  138  208
    datetime (unknown)

    body (0)

#### RECORD 105 Bolus 2013-08-10T18:07:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x78 0x00    ..P.P.x.
    decimal
              1    0   80    0   80    0  120    0
    datetime (2013-08-10T18:07:04)
    0000   0x84 0x07 0x52 0x0a 0x0d                   ..R..
    body (0)

#### RECORD 106 CalBGForPH 2013-08-10T22:41:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2013-08-10T22:41:29)
    0000   0x9d 0x29 0x36 0x0a 0x0d                   .)6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 107 BolusWizard 2013-08-10T22:41:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 131,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2013-08-10T22:41:36)
    0000   0xa4 0x29 0x16 0x0a 0x0d                   .)...
    body (15)
    hex
    0000   0x12 0x50 0x00 0x64 0x3c 0x64 0x04 0x00    .P.d<d..
    0008   0x48 0x00 0x00 0x00 0x00 0x4c 0x78         H....Lx
    decimal
             18   80    0  100   60  100    4    0
             72    0    0    0    0   76  120
    HOUR BITS: [0, 0, 1]
#### RECORD 108 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 2.0, 'curve': 208},
 {'age': 72, 'amount': 3.0, 'curve': 208},
 {'age': 132, 'amount': 1.9, 'curve': 208},
 {'age': 182, 'amount': 1.4, 'curve': 208},
 {'age': 212, 'amount': 2.4, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x16 0xd0 0x78 0x48 0xd0    \.P..xH.
    0008   0x4c 0x84 0xd0 0x38 0xb6 0xd0 0x60 0xd4    L..8..`.
    0010   0xd0                                       .
    decimal
             92   17   80   22  208  120   72  208
             76  132  208   56  182  208   96  212
            208
    datetime (unknown)

    body (0)

#### RECORD 109 Bolus 2013-08-10T22:41:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x00 0x00    ..L.L...
    decimal
              1    0   76    0   76    0    0    0
    datetime (2013-08-10T22:41:37)
    0000   0xa5 0x29 0x56 0x0a 0x0d                   .)V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 110 BasalProfileStart 2013-08-11T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-11T00:00:00)
    0000   0x80 0x00 0x00 0x0b 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 111 ResultTotals (2000, 8, 0, 0, 13, 10) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x53                   ....S
    decimal
              7    0    0    5   83
    datetime ((2000, 8, 0, 0, 13, 10))
    0000   0x8a 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x8a 0x0d 0x05 0x00 0xaa 0x00 0x00    n.......
    0008   0x09 0x00 0x00 0x05 0x53 0x02 0xdb 0x36    ....S..6
    0010   0x02 0x78 0x2e 0x00 0x7f 0x01 0x88 0x00    .x......
    0018   0xa4 0x00 0x4c 0x00 0x00 0x06 0x02 0x01    ..L.....
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0x42 0x00 0x00 0x00 0x00    ..dB....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  138   13    5    0  170    0    0
              9    0    0    5   83    2  219   54
              2  120   46    0  127    1  136    0
            164    0   76    0    0    6    2    1
              0    4    0    0    0    0    0    0
              0    0  100   66    0    0    0    0
              0    0    0

`end logs/ReadHistoryData-page-11.data: 112 records`
