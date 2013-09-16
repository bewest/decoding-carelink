## START logs/ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 1016, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xf4 0x7c                                  .|
##### DEBUG DECIMAL
            244  124
#### RECORD 0 Bolus 2013-08-07T15:20:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x0c 0x00    ..0.0...
    decimal
              1    0   48    0   48    0   12    0
    datetime (2013-08-07T15:20:38)
    0000   0xa6 0x14 0x4f 0x07 0x0d                   ..O..
    body (0)

#### RECORD 1 CalBGForPH 2013-08-07T17:04:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-08-07T17:04:16)
    0000   0x90 0x04 0x31 0x07 0x0d                   ..1..
    body (0)

#### RECORD 2 BolusWizard 2013-08-07T17:04:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 101,
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
    0000   0x5b 0x65                                  [e
    decimal
             91  101
    datetime (2013-08-07T17:04:23)
    0000   0x97 0x04 0x11 0x67 0x0d                   ...g.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x50 0x00 0x00 0x10 0x00 0x50 0x78         P....Px
    decimal
             20   80    0  100   60  100    0    0
             80    0    0   16    0   80  120
    DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 1.2, 'curve': 192},
 {'age': 221, 'amount': 1.0, 'curve': 192},
 {'age': 55, 'amount': 1.2, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x6f 0xc0 0x28 0xdd 0xc0    \.0o.(..
    0008   0x30 0x37 0xd0                             07.
    decimal
             92   11   48  111  192   40  221  192
             48   55  208
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-08-07T17:04:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x10 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   16    0
    datetime (2013-08-07T17:04:23)
    0000   0x97 0x04 0x51 0x67 0x0d                   ..Qg.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 5 CalBGForPH 2013-08-07T17:21:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-08-07T17:21:06)
    0000   0x86 0x15 0x31 0x07 0x0d                   ..1..
    body (0)

#### RECORD 6 BolusWizard 2013-08-07T17:21:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 101,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.8,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x65                                  [e
    decimal
             91  101
    datetime (2013-08-07T17:21:10)
    0000   0x8a 0x15 0x11 0x07 0x0d                   .....
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x3c 0x00 0x00 0x58 0x00 0x3c 0x78         <..X.<x
    decimal
             15   80    0  100   60  100    0    0
             60    0    0   88    0   60  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 2.0, 'curve': 192},
 {'age': 128, 'amount': 1.2, 'curve': 192},
 {'age': 238, 'amount': 1.0, 'curve': 192},
 {'age': 72, 'amount': 1.2, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x12 0xc0 0x30 0x80 0xc0    \.P..0..
    0008   0x28 0xee 0xc0 0x30 0x48 0xd0              (..0H.
    decimal
             92   14   80   18  192   48  128  192
             40  238  192   48   72  208
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-08-07T17:21:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x58 0x00    ..<.<.X.
    decimal
              1    0   60    0   60    0   88    0
    datetime (2013-08-07T17:21:11)
    0000   0x8b 0x15 0x51 0x07 0x0d                   ..Q..
    body (0)

#### RECORD 9 CalBGForPH 2013-08-07T18:47:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-08-07T18:47:29)
    0000   0x9d 0x2f 0x32 0x07 0x0d                   ./2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 10 BolusWizard 2013-08-07T18:47:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-08-07T18:47:38)
    0000   0xa6 0x2f 0x12 0x07 0x0d                   ./...
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x3c 0x64 0x2c 0x00    .P.d<d,.
    0008   0x78 0x00 0x00 0x38 0x00 0x78 0x78         x..8.xx
    decimal
             30   80    0  100   60  100   44    0
            120    0    0   56    0  120  120
    HOUR BITS: [0, 0, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 1.5, 'curve': 192},
 {'age': 104, 'amount': 2.0, 'curve': 192},
 {'age': 214, 'amount': 1.2, 'curve': 192},
 {'age': 68, 'amount': 1.0, 'curve': 208},
 {'age': 158, 'amount': 1.2, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x3c 0x5e 0xc0 0x50 0x68 0xc0    \.<^.Ph.
    0008   0x30 0xd6 0xc0 0x28 0x44 0xd0 0x30 0x9e    0..(D.0.
    0010   0xd0                                       .
    decimal
             92   17   60   94  192   80  104  192
             48  214  192   40   68  208   48  158
            208
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-08-07T18:47:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x38 0x00    ..x.x.8.
    decimal
              1    0  120    0  120    0   56    0
    datetime (2013-08-07T18:47:38)
    0000   0xa6 0x2f 0x52 0x07 0x0d                   ./R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 CalBGForPH 2013-08-07T19:05:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-07T19:05:31)
    0000   0x9f 0x05 0x33 0x07 0x0d                   ..3..
    body (0)

#### RECORD 14 BolusWizard 2013-08-07T19:05:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 15.2,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-07T19:05:44)
    0000   0xac 0x05 0x13 0x67 0x0d                   ...g.
    body (15)
    hex
    0000   0x10 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x40 0x00 0x00 0x98 0x00 0x40 0x78         @....@x
    decimal
             16   80    0  100   60  100    0    0
             64    0    0  152    0   64  120
    DAY BITS: [0, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 3.0, 'curve': 192},
 {'age': 112, 'amount': 1.5, 'curve': 192},
 {'age': 122, 'amount': 2.0, 'curve': 192},
 {'age': 232, 'amount': 1.2, 'curve': 192},
 {'age': 86, 'amount': 1.0, 'curve': 208},
 {'age': 176, 'amount': 1.2, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x78 0x16 0xc0 0x3c 0x70 0xc0    \.x..<p.
    0008   0x50 0x7a 0xc0 0x30 0xe8 0xc0 0x28 0x56    Pz.0..(V
    0010   0xd0 0x30 0xb0 0xd0                        .0..
    decimal
             92   20  120   22  192   60  112  192
             80  122  192   48  232  192   40   86
            208   48  176  208
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-08-07T19:05:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x98 0x00    ..@.@...
    decimal
              1    0   64    0   64    0  152    0
    datetime (2013-08-07T19:05:44)
    0000   0xac 0x05 0x53 0x67 0x0d                   ..Sg.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 17 CalBGForPH 2013-08-07T21:30:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2013-08-07T21:30:29)
    0000   0x9d 0x1e 0x35 0x07 0x0d                   ..5..
    body (0)

#### RECORD 18 BolusWizard 2013-08-07T21:30:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2013-08-07T21:30:50)
    0000   0xb2 0x1e 0x15 0x07 0x0d                   .....
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x08 0x00    .P.d<d..
    0008   0x58 0x00 0x00 0x14 0x00 0x58 0x78         X....Xx
    decimal
             22   80    0  100   60  100    8    0
             88    0    0   20    0   88  120

#### RECORD 19 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 147, 'amount': 1.6, 'curve': 192},
 {'age': 167, 'amount': 3.0, 'curve': 192},
 {'age': 1, 'amount': 1.5, 'curve': 208},
 {'age': 11, 'amount': 2.0, 'curve': 208},
 {'age': 121, 'amount': 1.2, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x40 0x93 0xc0 0x78 0xa7 0xc0    \.@..x..
    0008   0x3c 0x01 0xd0 0x50 0x0b 0xd0 0x30 0x79    <..P..0y
    0010   0xd0                                       .
    decimal
             92   17   64  147  192  120  167  192
             60    1  208   80   11  208   48  121
            208
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-08-07T21:30:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x14 0x00    ..X.X...
    decimal
              1    0   88    0   88    0   20    0
    datetime (2013-08-07T21:30:50)
    0000   0xb2 0x1e 0x55 0x07 0x0d                   ..U..
    body (0)

#### RECORD 21 CalBGForPH 2013-08-07T22:12:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-07T22:12:45)
    0000   0xad 0x0c 0x36 0x07 0x0d                   ..6..
    body (0)

#### RECORD 22 BolusWizard 2013-08-07T22:12:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-07T22:12:51)
    0000   0xb3 0x0c 0x16 0x07 0x0d                   .....
    body (15)
    hex
    0000   0x11 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x44 0x00 0x00 0x48 0x00 0x44 0x78         D..H.Dx
    decimal
             17   80    0  100   60  100    0    0
             68    0    0   72    0   68  120

#### RECORD 23 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 2.2, 'curve': 192},
 {'age': 189, 'amount': 1.6, 'curve': 192},
 {'age': 209, 'amount': 3.0, 'curve': 192},
 {'age': 43, 'amount': 1.5, 'curve': 208},
 {'age': 53, 'amount': 2.0, 'curve': 208},
 {'age': 163, 'amount': 1.2, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x58 0x31 0xc0 0x40 0xbd 0xc0    \.X1.@..
    0008   0x78 0xd1 0xc0 0x3c 0x2b 0xd0 0x50 0x35    x..<+.P5
    0010   0xd0 0x30 0xa3 0xd0                        .0..
    decimal
             92   20   88   49  192   64  189  192
            120  209  192   60   43  208   80   53
            208   48  163  208
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-08-07T22:12:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x48 0x00    ..D.D.H.
    decimal
              1    0   68    0   68    0   72    0
    datetime (2013-08-07T22:12:52)
    0000   0xb4 0x0c 0x56 0x07 0x0d                   ..V..
    body (0)

#### RECORD 25 CalBGForPH 2013-08-07T23:41:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-08-07T23:41:04)
    0000   0x84 0x29 0x37 0x07 0x0d                   .)7..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 BolusWizard 2013-08-07T23:41:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
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
    datetime (2013-08-07T23:41:10)
    0000   0x8a 0x29 0x17 0x07 0x0d                   .)...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x48 0x00    .P.d<dH.
    0008   0x00 0x00 0x00 0x30 0x00 0x18 0x78         ...0..x
    decimal
              0   80    0  100   60  100   72    0
              0    0    0   48    0   24  120
    HOUR BITS: [0, 0, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 1.5, 'curve': 192},
 {'age': 98, 'amount': 0.2, 'curve': 192},
 {'age': 138, 'amount': 2.2, 'curve': 192},
 {'age': 22, 'amount': 1.6, 'curve': 208},
 {'age': 42, 'amount': 3.0, 'curve': 208},
 {'age': 132, 'amount': 1.5, 'curve': 208},
 {'age': 142, 'amount': 2.0, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x3c 0x58 0xc0 0x08 0x62 0xc0    \.<X..b.
    0008   0x58 0x8a 0xc0 0x40 0x16 0xd0 0x78 0x2a    X..@..x*
    0010   0xd0 0x3c 0x84 0xd0 0x50 0x8e 0xd0         .<..P..
    decimal
             92   23   60   88  192    8   98  192
             88  138  192   64   22  208  120   42
            208   60  132  208   80  142  208
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-08-07T23:41:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x30 0x00    ......0.
    decimal
              1    0   24    0   24    0   48    0
    datetime (2013-08-07T23:41:10)
    0000   0x8a 0x29 0x57 0x07 0x0d                   .)W..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 29 BasalProfileStart 2013-08-08T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-08T00:00:00)
    0000   0x80 0x00 0x00 0x08 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 30 ResultTotals (2000, 8, 0, 0, 13, 7) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x5c                   ....\
    decimal
              7    0    0    5   92
    datetime ((2000, 8, 0, 0, 13, 7))
    0000   0x87 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 31 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x87 0x0d 0x05 0x00 0x8f 0x00 0x00    n.......
    0008   0x0a 0x00 0x00 0x05 0x5c 0x02 0xdc 0x35    ....\..5
    0010   0x02 0x80 0x2f 0x00 0x91 0x02 0x08 0x00    ../.....
    0018   0x48 0x00 0x30 0x00 0x00 0x07 0x02 0x01    H.0.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0xe7 0x00 0x00 0x00         ..d....
    decimal
            110  135   13    5    0  143    0    0
             10    0    0    5   92    2  220   53
              2  128   47    0  145    2    8    0
             72    0   48    0    0    7    2    1
              0    0    0    0    0    0    0    0
              0    0  100  231    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 32 BolusWizard 2013-08-08T00:24:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-08T00:24:24)
    0000   0x98 0x18 0x00 0x08 0x0d                   .....
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x78 0x3c 0x6e 0x00 0x00    .P.x<n..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x82         $....$.
    decimal
             11   80    0  120   60  110    0    0
             36    0    0    0    0   36  130

#### RECORD 33 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 0.6, 'curve': 192},
 {'age': 131, 'amount': 1.5, 'curve': 192},
 {'age': 141, 'amount': 0.2, 'curve': 192},
 {'age': 181, 'amount': 2.2, 'curve': 192},
 {'age': 65, 'amount': 1.6, 'curve': 208},
 {'age': 85, 'amount': 3.0, 'curve': 208},
 {'age': 175, 'amount': 1.5, 'curve': 208},
 {'age': 185, 'amount': 2.0, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x18 0x33 0xc0 0x3c 0x83 0xc0    \..3.<..
    0008   0x08 0x8d 0xc0 0x58 0xb5 0xc0 0x40 0x41    ...X..@A
    0010   0xd0 0x78 0x55 0xd0 0x3c 0xaf 0xd0 0x50    .xU.<..P
    0018   0xb9 0xd0                                  ..
    decimal
             92   26   24   51  192   60  131  192
              8  141  192   88  181  192   64   65
            208  120   85  208   60  175  208   80
            185  208
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-08-08T00:24:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x20 0x00    ..$.$. .
    decimal
              1    0   36    0   36    0   32    0
    datetime (2013-08-08T00:24:24)
    0000   0x98 0x18 0x40 0x08 0x0d                   ..@..
    body (0)

#### RECORD 35 CalBGForPH 2013-08-08T00:54:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2013-08-08T00:54:35)
    0000   0xa3 0x36 0x20 0x08 0x0d                   .6 ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 BolusWizard 2013-08-08T00:54:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 216,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 5.6,
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
    datetime (2013-08-08T00:54:37)
    0000   0xa5 0x36 0x00 0x08 0x0d                   .6...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x6e 0x38 0x00    .P.x<n8.
    0008   0x00 0x00 0x00 0x34 0x00 0x04 0x82         ...4...
    decimal
              0   80    0  120   60  110   56    0
              0    0    0   52    0    4  130
    HOUR BITS: [0, 0, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 0.9, 'curve': 192},
 {'age': 81, 'amount': 0.6, 'curve': 192},
 {'age': 161, 'amount': 1.5, 'curve': 192},
 {'age': 171, 'amount': 0.2, 'curve': 192},
 {'age': 211, 'amount': 2.2, 'curve': 192},
 {'age': 95, 'amount': 1.6, 'curve': 208},
 {'age': 115, 'amount': 3.0, 'curve': 208},
 {'age': 205, 'amount': 1.5, 'curve': 208},
 {'age': 215, 'amount': 2.0, 'curve': 208}]
```
    op hex (29)
    0000   0x5c 0x1d 0x24 0x1f 0xc0 0x18 0x51 0xc0    \.$...Q.
    0008   0x3c 0xa1 0xc0 0x08 0xab 0xc0 0x58 0xd3    <.....X.
    0010   0xc0 0x40 0x5f 0xd0 0x78 0x73 0xd0 0x3c    .@_.xs.<
    0018   0xcd 0xd0 0x50 0xd7 0xd0                   ..P..
    decimal
             92   29   36   31  192   24   81  192
             60  161  192    8  171  192   88  211
            192   64   95  208  120  115  208   60
            205  208   80  215  208
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-08-08T00:54:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x04 0x00 0x04 0x00 0x34 0x00    ......4.
    decimal
              1    0    4    0    4    0   52    0
    datetime (2013-08-08T00:54:37)
    0000   0xa5 0x36 0x40 0x08 0x0d                   .6@..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 BasalProfileStart 2013-08-08T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-08T04:00:00)
    0000   0x80 0x00 0x04 0x08 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 40 BasalProfileStart 2013-08-08T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-08T08:00:00)
    0000   0x80 0x00 0x08 0x08 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 41 CalBGForPH 2013-08-08T09:05:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2013-08-08T09:05:26)
    0000   0x9a 0x05 0x29 0x08 0x0d                   ..)..
    body (0)

#### RECORD 42 BolusWizard 2013-08-08T09:05:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 166,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0xa6                                  [.
    decimal
             91  166
    datetime (2013-08-08T09:05:35)
    0000   0xa3 0x05 0x09 0x08 0x0d                   .....
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x1c 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x00 0x00 0x44 0x78         (....Dx
    decimal
             13   80    0  120   60  100   28    0
             40    0    0    0    0   68  120

#### RECORD 43 Bolus 2013-08-08T09:05:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2013-08-08T09:05:35)
    0000   0xa3 0x05 0x49 0x08 0x0d                   ..I..
    body (0)

#### RECORD 44 LowBattery 2013-08-08T10:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-08-08T10:01:00)
    0000   0x80 0x01 0x0a 0x08 0x0d                   .....
    body (0)

#### RECORD 45 Battery 2013-08-08T10:36:50 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-08-08T10:36:50)
    0000   0xb2 0x24 0x0a 0x08 0x0d                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 46 Battery 2013-08-08T10:37:18 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-08-08T10:37:18)
    0000   0x92 0x25 0x0a 0x08 0x0d                   .%...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 47 BasalProfileStart 2013-08-08T10:37:19 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-08T10:37:19)
    0000   0x93 0x25 0x0a 0x08 0x0d                   .%...
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [0, 0, 1]
#### RECORD 48 CalBGForPH 2013-08-08T10:37:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2013-08-08T10:37:43)
    0000   0xab 0x25 0x2a 0x08 0x0d                   .%*..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 BolusWizard 2013-08-08T10:37:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 182,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0xb6                                  [.
    decimal
             91  182
    datetime (2013-08-08T10:37:51)
    0000   0xb3 0x25 0x0a 0x08 0x0d                   .%...
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x28 0x00    .P.x<d(.
    0008   0x28 0x00 0x00 0x20 0x00 0x30 0x78         (.. .0x
    decimal
             12   80    0  120   60  100   40    0
             40    0    0   32    0   48  120
    HOUR BITS: [0, 0, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 1.7, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0x5e 0xc0                   \.D^.
    decimal
             92    5   68   94  192
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-08-08T10:37:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x20 0x00    ..0.0. .
    decimal
              1    0   48    0   48    0   32    0
    datetime (2013-08-08T10:37:51)
    0000   0xb3 0x25 0x4a 0x08 0x0d                   .%J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 52 CalBGForPH 2013-08-08T11:50:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-08-08T11:50:38)
    0000   0xa6 0x32 0x2b 0x08 0x0d                   .2+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 53 BolusWizard 2013-08-08T11:50:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-08-08T11:50:44)
    0000   0xac 0x32 0x0b 0x08 0x0d                   .2...
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x30 0x00    .P.x<d0.
    0008   0x28 0x00 0x00 0x24 0x00 0x34 0x78         (..$.4x
    decimal
             12   80    0  120   60  100   48    0
             40    0    0   36    0   52  120
    HOUR BITS: [0, 0, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 77, 'amount': 1.2, 'curve': 192},
 {'age': 167, 'amount': 1.7, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x4d 0xc0 0x44 0xa7 0xc0    \.0M.D..
    decimal
             92    8   48   77  192   68  167  192
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-08-08T11:50:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x24 0x00    ..4.4.$.
    decimal
              1    0   52    0   52    0   36    0
    datetime (2013-08-08T11:50:44)
    0000   0xac 0x32 0x4b 0x08 0x0d                   .2K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 BasalProfileStart 2013-08-08T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-08T12:00:00)
    0000   0x80 0x00 0x0c 0x08 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 57 CalBGForPH 2013-08-08T13:31:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-08-08T13:31:20)
    0000   0x94 0x1f 0x2d 0x08 0x0d                   ..-..
    body (0)

#### RECORD 58 BolusWizard 2013-08-08T13:31:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
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
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-08-08T13:31:22)
    0000   0x96 0x1f 0x0d 0x08 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x00 0x00 0x00 0x14 0x00 0x18 0x78         ......x
    decimal
              0   80    0  120   60  100   44    0
              0    0    0   20    0   24  120

#### RECORD 59 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 1.3, 'curve': 192},
 {'age': 178, 'amount': 1.2, 'curve': 192},
 {'age': 12, 'amount': 1.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x6c 0xc0 0x30 0xb2 0xc0    \.4l.0..
    0008   0x44 0x0c 0xd0                             D..
    decimal
             92   11   52  108  192   48  178  192
             68   12  208
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-08-08T13:31:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x14 0x00    ........
    decimal
              1    0   24    0   24    0   20    0
    datetime (2013-08-08T13:31:22)
    0000   0x96 0x1f 0x4d 0x08 0x0d                   ..M..
    body (0)

#### RECORD 61 CalBGForPH 2013-08-08T14:13:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-08-08T14:13:58)
    0000   0xba 0x0d 0x2e 0x08 0x0d                   .....
    body (0)

#### RECORD 62 BolusWizard 2013-08-08T14:14:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
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
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-08-08T14:14:10)
    0000   0x8a 0x0e 0x0e 0x08 0x0d                   .....
    body (15)
    hex
    0000   0x1a 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x54 0x00 0x00 0x1c 0x00 0x54 0x78         T....Tx
    decimal
             26   80    0  120   60  100    0    0
             84    0    0   28    0   84  120

#### RECORD 63 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 0.6, 'curve': 192},
 {'age': 151, 'amount': 1.3, 'curve': 192},
 {'age': 221, 'amount': 1.2, 'curve': 192},
 {'age': 55, 'amount': 1.7, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x33 0xc0 0x34 0x97 0xc0    \..3.4..
    0008   0x30 0xdd 0xc0 0x44 0x37 0xd0              0..D7.
    decimal
             92   14   24   51  192   52  151  192
             48  221  192   68   55  208
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-08-08T14:14:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x1c 0x00    ..T.T...
    decimal
              1    0   84    0   84    0   28    0
    datetime (2013-08-08T14:14:11)
    0000   0x8b 0x0e 0x4e 0x08 0x0d                   ..N..
    body (0)

#### RECORD 65 CalBGForPH 2013-08-08T15:03:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-08T15:03:13)
    0000   0x8d 0x03 0x2f 0x08 0x0d                   ../..
    body (0)

#### RECORD 66 BolusWizard 2013-08-08T15:03:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.6,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-08T15:03:18)
    0000   0x92 0x03 0x0f 0x08 0x0d                   .....
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x34 0x00 0x00 0x4c 0x00 0x34 0x78         4..L.4x
    decimal
             16   80    0  120   60  100    0    0
             52    0    0   76    0   52  120

#### RECORD 67 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 2.1, 'curve': 192},
 {'age': 100, 'amount': 0.6, 'curve': 192},
 {'age': 200, 'amount': 1.3, 'curve': 192},
 {'age': 14, 'amount': 1.2, 'curve': 208},
 {'age': 104, 'amount': 1.7, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x54 0x32 0xc0 0x18 0x64 0xc0    \.T2..d.
    0008   0x34 0xc8 0xc0 0x30 0x0e 0xd0 0x44 0x68    4..0..Dh
    0010   0xd0                                       .
    decimal
             92   17   84   50  192   24  100  192
             52  200  192   48   14  208   68  104
            208
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-08-08T15:03:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x4c 0x00    ..4.4.L.
    decimal
              1    0   52    0   52    0   76    0
    datetime (2013-08-08T15:03:18)
    0000   0x92 0x03 0x4f 0x08 0x0d                   ..O..
    body (0)

#### RECORD 69 Bolus 2013-08-08T15:32:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x64 0x00    ..@.@.d.
    decimal
              1    0   64    0   64    0  100    0
    datetime (2013-08-08T15:32:28)
    0000   0x9c 0x20 0x4f 0x08 0x0d                   . O..
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-13.data: 70 records`
