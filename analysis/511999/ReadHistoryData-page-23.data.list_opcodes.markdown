## START logs/ReadHistoryData-page-23.data
#### RECORD 0 CalBGForPH 2013-07-18T09:19:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-07-18T09:19:47)
    0000   0x6f 0xd3 0x29 0x12 0x0d                   o.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 BolusWizard 2013-07-18T09:19:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 92,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 24.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-07-18T09:19:56)
    0000   0x78 0xd3 0x09 0x72 0x0d                   x..r.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0xf8 0x00    .P.x<d..
    0008   0x40 0xf8 0x00 0x00 0x00 0x38 0x78         @....8x
    decimal
             20   80    0  120   60  100  248    0
             64  248    0    0    0   56  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 Bolus 2013-07-18T09:19:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-07-18T09:19:56)
    0000   0x78 0xd3 0x49 0x72 0x0d                   x.Ir.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-07-18T10:20:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-07-18T10:20:12)
    0000   0x4c 0xd4 0x2a 0x12 0x0d                   L.*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-07-18T10:20:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 115,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
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
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-07-18T10:20:17)
    0000   0x51 0xd4 0x0a 0x72 0x0d                   Q..r.
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x24 0x00 0x00 0x28 0x00 0x24 0x78         $..(.$x
    decimal
             11   80    0  120   60  100    0    0
             36    0    0   40    0   36  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 1.4, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0x43 0xc0                   \.8C.
    decimal
             92    5   56   67  192
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-07-18T10:20:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x28 0x00    ..$.$.(.
    decimal
              1    0   36    0   36    0   40    0
    datetime (2013-07-18T10:20:18)
    0000   0x52 0xd4 0x4a 0x72 0x0d                   R.Jr.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 BasalProfileStart 2013-07-18T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-18T12:00:00)
    0000   0x40 0xc0 0x0c 0x12 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 8 CalBGForPH 2013-07-18T12:36:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 81}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2013-07-18T12:36:08)
    0000   0x48 0xe4 0x2c 0x12 0x0d                   H.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 BolusWizard 2013-07-18T12:36:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 81,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 24.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x51                                  [Q
    decimal
             91   81
    datetime (2013-07-18T12:36:15)
    0000   0x4f 0xe4 0x0c 0x72 0x0d                   O..r.
    body (15)
    hex
    0000   0x13 0x50 0x00 0x78 0x3c 0x64 0xf4 0x00    .P.x<d..
    0008   0x3c 0xf8 0x00 0x08 0x00 0x30 0x78         <....0x
    decimal
             19   80    0  120   60  100  244    0
             60  248    0    8    0   48  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 143, 'amount': 0.9, 'curve': 192},
 {'age': 203, 'amount': 1.4, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x8f 0xc0 0x38 0xcb 0xc0    \.$..8..
    decimal
             92    8   36  143  192   56  203  192
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-07-18T12:36:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x08 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    8    0
    datetime (2013-07-18T12:36:15)
    0000   0x4f 0xe4 0x4c 0x72 0x0d                   O.Lr.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 CalBGForPH 2013-07-18T14:17:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2013-07-18T14:17:43)
    0000   0x6b 0xd1 0x2e 0x12 0x0d                   k....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 BolusWizard 2013-07-18T14:17:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 188,
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
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2013-07-18T14:17:46)
    0000   0x6e 0xd1 0x0e 0x72 0x0d                   n..r.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x00 0x00 0x00 0x14 0x00 0x18 0x78         ......x
    decimal
              0   80    0  120   60  100   44    0
              0    0    0   20    0   24  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 1.2, 'curve': 192},
 {'age': 244, 'amount': 0.9, 'curve': 192},
 {'age': 48, 'amount': 1.4, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x68 0xc0 0x24 0xf4 0xc0    \.0h.$..
    0008   0x38 0x30 0xd0                             80.
    decimal
             92   11   48  104  192   36  244  192
             56   48  208
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-07-18T14:17:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x14 0x00    ........
    decimal
              1    0   24    0   24    0   20    0
    datetime (2013-07-18T14:17:46)
    0000   0x6e 0xd1 0x4e 0x72 0x0d                   n.Nr.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 CalBGForPH 2013-07-18T15:02:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 269}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2013-07-18T15:02:05)
    0000   0x45 0xc2 0x2f 0x12 0x8d                   E./..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 BolusWizard 2013-07-18T15:02:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 269,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
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
    0000   0x5b 0x0d                                  [.
    decimal
             91   13
    datetime (2013-07-18T15:02:07)
    0000   0x47 0xc2 0x0f 0x72 0x0d                   G..r.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x60 0x00    .Q.x<d`.
    0008   0x00 0x00 0x00 0x1c 0x00 0x44 0x78         .....Dx
    decimal
              0   81    0  120   60  100   96    0
              0    0    0   28    0   68  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 0.6, 'curve': 192},
 {'age': 149, 'amount': 1.2, 'curve': 192},
 {'age': 33, 'amount': 0.9, 'curve': 208},
 {'age': 93, 'amount': 1.4, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x31 0xc0 0x30 0x95 0xc0    \..1.0..
    0008   0x24 0x21 0xd0 0x38 0x5d 0xd0              $!.8].
    decimal
             92   14   24   49  192   48  149  192
             36   33  208   56   93  208
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-07-18T15:02:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x1c 0x00    ..D.D...
    decimal
              1    0   68    0   68    0   28    0
    datetime (2013-07-18T15:02:07)
    0000   0x47 0xc2 0x4f 0x72 0x0d                   G.Or.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 CalBGForPH 2013-07-18T16:04:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 316}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2013-07-18T16:04:31)
    0000   0x5f 0xc4 0x30 0x12 0x8d                   _.0..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 BolusWizard 2013-07-18T16:04:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 316,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 12.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3c                                  [<
    decimal
             91   60
    datetime (2013-07-18T16:04:33)
    0000   0x61 0xc4 0x10 0x72 0x0d                   a..r.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x80 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x34 0x00 0x4c 0x78         ...4.Lx
    decimal
              0   81    0  120   60  100  128    0
              0    0    0   52    0   76  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 0.35, 'curve': 192},
 {'age': 71, 'amount': 1.35, 'curve': 192},
 {'age': 111, 'amount': 0.6, 'curve': 192},
 {'age': 211, 'amount': 1.2, 'curve': 192},
 {'age': 95, 'amount': 0.9, 'curve': 208},
 {'age': 155, 'amount': 1.4, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x0e 0x3d 0xc0 0x36 0x47 0xc0    \..=.6G.
    0008   0x18 0x6f 0xc0 0x30 0xd3 0xc0 0x24 0x5f    .o.0..$_
    0010   0xd0 0x38 0x9b 0xd0                        .8..
    decimal
             92   20   14   61  192   54   71  192
             24  111  192   48  211  192   36   95
            208   56  155  208
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-07-18T16:04:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x34 0x00    ..L.L.4.
    decimal
              1    0   76    0   76    0   52    0
    datetime (2013-07-18T16:04:33)
    0000   0x61 0xc4 0x50 0x72 0x0d                   a.Pr.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 24 CalBGForPH 2013-07-18T18:27:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-07-18T18:27:35)
    0000   0x63 0xdb 0x32 0x12 0x0d                   c.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BolusWizard 2013-07-18T18:27:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-07-18T18:27:57)
    0000   0x79 0xdb 0x12 0x72 0x0d                   y..r.
    body (15)
    hex
    0000   0x1b 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x6c 0x00 0x00 0x0c 0x00 0x6c 0x78         l....lx
    decimal
             27   80    0  100   60  100    0    0
            108    0    0   12    0  108  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 1.9, 'curve': 192},
 {'age': 204, 'amount': 0.35, 'curve': 192},
 {'age': 214, 'amount': 1.35, 'curve': 192},
 {'age': 254, 'amount': 0.6, 'curve': 192},
 {'age': 98, 'amount': 1.2, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x4c 0x90 0xc0 0x0e 0xcc 0xc0    \.L.....
    0008   0x36 0xd6 0xc0 0x18 0xfe 0xc0 0x30 0x62    6.....0b
    0010   0xd0                                       .
    decimal
             92   17   76  144  192   14  204  192
             54  214  192   24  254  192   48   98
            208
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-07-18T18:27:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x0c 0x03    ..@.@...
    decimal
              1    0   64    0   64    0   12    3
    datetime (2013-07-18T18:27:57)
    0000   0x79 0xdb 0x72 0x72 0x0d                   y.rr.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 CalBGForPH 2013-07-18T21:57:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-07-18T21:57:02)
    0000   0x42 0xf9 0x35 0x12 0x0d                   B.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 29 CalBGForPH 2013-07-18T23:02:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 251}
```
    op hex (2)
    0000   0x0a 0xfb                                  ..
    decimal
             10  251
    datetime (2013-07-18T23:02:20)
    0000   0x54 0xc2 0x37 0x12 0x0d                   T.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 BolusWizard 2013-07-18T23:02:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 251,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0xfb                                  [.
    decimal
             91  251
    datetime (2013-07-18T23:02:25)
    0000   0x59 0xc2 0x17 0x72 0x0d                   Y..r.
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x64 0x3c 0x64 0x54 0x00    .P.d<dT.
    0008   0x2c 0x00 0x00 0x00 0x00 0x80 0x78         ,.....x
    decimal
             11   80    0  100   60  100   84    0
             44    0    0    0    0  128  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 189, 'amount': 0.1, 'curve': 192},
 {'age': 199, 'amount': 0.15, 'curve': 192},
 {'age': 209, 'amount': 0.2, 'curve': 192},
 {'age': 219, 'amount': 0.15, 'curve': 192},
 {'age': 229, 'amount': 0.2, 'curve': 192},
 {'age': 239, 'amount': 0.2, 'curve': 192},
 {'age': 249, 'amount': 0.15, 'curve': 192},
 {'age': 3, 'amount': 0.2, 'curve': 208},
 {'age': 13, 'amount': 0.15, 'curve': 208},
 {'age': 23, 'amount': 0.1, 'curve': 208},
 {'age': 163, 'amount': 1.9, 'curve': 208},
 {'age': 223, 'amount': 0.35, 'curve': 208}]
```
    op hex (38)
    0000   0x5c 0x26 0x04 0xbd 0xc0 0x06 0xc7 0xc0    \&......
    0008   0x08 0xd1 0xc0 0x06 0xdb 0xc0 0x08 0xe5    ........
    0010   0xc0 0x08 0xef 0xc0 0x06 0xf9 0xc0 0x08    ........
    0018   0x03 0xd0 0x06 0x0d 0xd0 0x04 0x17 0xd0    ........
    0020   0x4c 0xa3 0xd0 0x0e 0xdf 0xd0              L.....
    decimal
             92   38    4  189  192    6  199  192
              8  209  192    6  219  192    8  229
            192    8  239  192    6  249  192    8
              3  208    6   13  208    4   23  208
             76  163  208   14  223  208
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-07-18T23:02:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x00 0x00    ........
    decimal
              1    0  128    0  128    0    0    0
    datetime (2013-07-18T23:02:25)
    0000   0x59 0xc2 0x57 0x72 0x0d                   Y.Wr.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 BasalProfileStart 2013-07-19T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-19T00:00:00)
    0000   0x40 0xc0 0x00 0x13 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1f 0x00                             ...
    decimal
              0   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 34 ResultTotals (2000, 6, 0, 0, 13, 50) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd8                   .....
    decimal
              7    0    0    4  216
    datetime ((2000, 6, 0, 0, 13, 50))
    0000   0x72 0x8d 0x00 0x00 0x00                   r....
    body (51)
    hex
    0000   0x6e 0x72 0x8d 0x05 0x00 0xab 0x00 0x00    nr......
    0008   0x09 0x00 0x00 0x04 0xd8 0x02 0xe4 0x3c    .......<
    0010   0x01 0xf4 0x28 0x00 0x58 0x00 0xcc 0x00    ..(.X...
    0018   0xa8 0x00 0x80 0x00 0x00 0x04 0x03 0x01    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x51 0x3c 0x00 0x00 0x00 0x00    ..Q<....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  114  141    5    0  171    0    0
              9    0    0    4  216    2  228   60
              1  244   40    0   88    0  204    0
            168    0  128    0    0    4    3    1
              0    4    0    0    0    0    0    0
              0    0   81   60    0    0    0    0
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 35 Base (2003, 1, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2003, 1, 4, 0, 0, 1))
    0000   0x01 0x40 0xc0 0x04 0x13                   .@...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 36 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x40                   !.{.@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 37 Base (2000, 0, 2, 16, 13, 19) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x08                                  ..
    decimal
            192    8
    datetime ((2000, 0, 2, 16, 13, 19))
    0000   0x13 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 38 CalBGForPH 2013-07-19T08:57:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-07-19T08:57:25)
    0000   0x59 0xf9 0x28 0x13 0x0d                   Y.(..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 BolusWizard 2013-07-19T08:57:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-07-19T08:57:36)
    0000   0x64 0xf9 0x08 0x73 0x0d                   d..s.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x78         H....Hx
    decimal
             22   80    0  120   60  100    0    0
             72    0    0    0    0   72  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 Bolus 2013-07-19T08:57:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x00 0x00    ..$.$...
    decimal
              1    0   36    0   36    0    0    0
    datetime (2013-07-19T08:57:36)
    0000   0x64 0xf9 0x48 0x73 0x0d                   d.Hs.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 TempBasal 2013-07-19T09:35:25 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.875}
```
    op hex (2)
    0000   0x33 0x4b                                  3K
    decimal
             51   75
    datetime (2013-07-19T09:35:25)
    0000   0x59 0xe3 0x09 0x13 0x0d                   Y....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 42 TempBasalDuration 2013-07-19T09:35:25 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-07-19T09:35:25)
    0000   0x59 0xe3 0x09 0x13 0x0d                   Y....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 43 TempBasal 2013-07-19T09:36:01 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-07-19T09:36:01)
    0000   0x41 0xe4 0x09 0x13 0x0d                   A....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 44 TempBasalDuration 2013-07-19T09:36:01 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-07-19T09:36:01)
    0000   0x41 0xe4 0x09 0x13 0x0d                   A....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BasalProfileStart 2013-07-19T09:36:01 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-19T09:36:01)
    0000   0x41 0xe4 0x09 0x13 0x0d                   A....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 1]
#### RECORD 46 Base (2013, 7, 19, 9, 36, 12) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x01                                  b.
    decimal
             98    1
    datetime ((2013, 7, 19, 9, 36, 12))
    0000   0x4c 0xe4 0x09 0x13 0x0d                   L....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 47 Base (2013, 7, 19, 9, 36, 18) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x01                                  b.
    decimal
             98    1
    datetime ((2013, 7, 19, 9, 36, 18))
    0000   0x52 0xe4 0x09 0x13 0x0d                   R....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 TempBasal 2013-07-19T09:36:37 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.0}
```
    op hex (2)
    0000   0x33 0x50                                  3P
    decimal
             51   80
    datetime (2013-07-19T09:36:37)
    0000   0x65 0xe4 0x09 0x13 0x0d                   e....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 49 TempBasalDuration 2013-07-19T09:36:37 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-07-19T09:36:37)
    0000   0x65 0xe4 0x09 0x13 0x0d                   e....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 50 BasalProfileStart 2013-07-19T11:06:37 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-19T11:06:37)
    0000   0x65 0xc6 0x0b 0x13 0x0d                   e....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [1, 1, 0]
#### RECORD 51 BasalProfileStart 2013-07-19T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-19T12:00:00)
    0000   0x40 0xc0 0x0c 0x13 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 52 CalBGForPH 2013-07-19T14:15:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-07-19T14:15:27)
    0000   0x5b 0xcf 0x2e 0x13 0x0d                   [....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 BolusWizard 2013-07-19T14:15:30 head[2], body[15] op[0x5b]
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
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2013-07-19T14:15:30)
    0000   0x5e 0xcf 0x0e 0x73 0x0d                   ^..s.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x48 0x00    .P.x<dH.
    0008   0x00 0x00 0x00 0x00 0x00 0x48 0x78         .....Hx
    decimal
              0   80    0  120   60  100   72    0
              0    0    0    0    0   72  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 0.9, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x24 0x42 0xd0                   \.$B.
    decimal
             92    5   36   66  208
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-07-19T14:15:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2013-07-19T14:15:30)
    0000   0x5e 0xcf 0x4e 0x73 0x0d                   ^.Ns.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 56 CalBGForPH 2013-07-19T15:15:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 221}
```
    op hex (2)
    0000   0x0a 0xdd                                  ..
    decimal
             10  221
    datetime (2013-07-19T15:15:56)
    0000   0x78 0xcf 0x2f 0x13 0x0d                   x./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 57 BolusWizard 2013-07-19T15:16:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 221,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
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
    0000   0x5b 0xdd                                  [.
    decimal
             91  221
    datetime (2013-07-19T15:16:17)
    0000   0x51 0xd0 0x0f 0x73 0x0d                   Q..s.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x40 0x00    .P.x<d@.
    0008   0x00 0x00 0x00 0x34 0x00 0x0c 0x78         ...4..x
    decimal
              0   80    0  120   60  100   64    0
              0    0    0   52    0   12  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 63, 'amount': 1.8, 'curve': 192},
 {'age': 127, 'amount': 0.9, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0x3f 0xc0 0x24 0x7f 0xd0    \.H?.$..
    decimal
             92    8   72   63  192   36  127  208
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-07-19T15:16:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x34 0x00    ..p.p.4.
    decimal
              1    0  112    0  112    0   52    0
    datetime (2013-07-19T15:16:17)
    0000   0x51 0xd0 0x4f 0x73 0x0d                   Q.Os.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 Rewind 2013-07-19T18:23:32 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-19T18:23:32)
    0000   0x60 0xd7 0x12 0x13 0x0d                   `....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 61 Prime 2013-07-19T18:24:02 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 10.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x6a                   ....j
    decimal
              3    0    0    0  106
    datetime (2013-07-19T18:24:02)
    0000   0x42 0xd8 0x32 0x13 0x0d                   B.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 BasalProfileStart 2013-07-19T18:27:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-19T18:27:00)
    0000   0x40 0xdb 0x12 0x13 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 63 Prime 2013-07-19T18:26:26 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-07-19T18:26:26)
    0000   0x5a 0xda 0x12 0x13 0x0d                   Z....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 CalBGForPH 2013-07-19T19:12:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-07-19T19:12:15)
    0000   0x4f 0xcc 0x33 0x13 0x0d                   O.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 BolusWizard 2013-07-19T19:12:22 head[2], body[15] op[0x5b]
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
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-07-19T19:12:22)
    0000   0x56 0xcc 0x13 0x73 0x0d                   V..s.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x78         T....Tx
    decimal
             21   80    0  100   60  100    0    0
             84    0    0    0    0   84  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 239, 'amount': 2.8, 'curve': 192},
 {'age': 43, 'amount': 1.8, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x70 0xef 0xc0 0x48 0x2b 0xd0    \.p..H+.
    decimal
             92    8  112  239  192   72   43  208
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-07-19T19:12:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x00 0x00    ..T.T...
    decimal
              1    0   84    0   84    0    0    0
    datetime (2013-07-19T19:12:22)
    0000   0x56 0xcc 0x53 0x73 0x0d                   V.Ss.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 CalBGForPH 2013-07-19T19:36:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-07-19T19:36:30)
    0000   0x5e 0xe4 0x33 0x13 0x0d                   ^.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 BolusWizard 2013-07-19T19:36:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.0,
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
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-07-19T19:36:36)
    0000   0x64 0xe4 0x13 0x73 0x0d                   d..s.
    body (15)
    hex
    0000   0x13 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x4c 0x00 0x00 0x50 0x00 0x4c 0x78         L..P.Lx
    decimal
             19   80    0  100   60  100    0    0
             76    0    0   80    0   76  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 1.2, 'curve': 192},
 {'age': 33, 'amount': 0.9, 'curve': 192},
 {'age': 7, 'amount': 2.8, 'curve': 208},
 {'age': 67, 'amount': 1.8, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x30 0x17 0xc0 0x24 0x21 0xc0    \.0..$!.
    0008   0x70 0x07 0xd0 0x48 0x43 0xd0              p..HC.
    decimal
             92   14   48   23  192   36   33  192
            112    7  208   72   67  208
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-07-19T19:36:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x50 0x00    ..L.L.P.
    decimal
              1    0   76    0   76    0   80    0
    datetime (2013-07-19T19:36:36)
    0000   0x64 0xe4 0x53 0x73 0x0d                   d.Ss.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 72 BasalProfileStart 2013-07-20T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-20T00:00:00)
    0000   0x40 0xc0 0x00 0x14 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1f 0x00                             ...
    decimal
              0   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 73 ResultTotals (2000, 6, 0, 0, 13, 51) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x54                   ....T
    decimal
              7    0    0    4   84
    datetime ((2000, 6, 0, 0, 13, 51))
    0000   0x73 0x8d 0x00 0x00 0x00                   s....
    body (51)
    hex
    0000   0x6e 0x73 0x8d 0x05 0x00 0x98 0x00 0x00    ns......
    0008   0x05 0x00 0x00 0x04 0x54 0x02 0xd8 0x42    ....T..B
    0010   0x01 0x7c 0x22 0x00 0x3e 0x00 0xc4 0x00    .|".>...
    0018   0xb8 0x00 0x00 0x00 0x00 0x03 0x02 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0xe7 0x00 0x00 0x00 0x00    ..d.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  115  141    5    0  152    0    0
              5    0    0    4   84    2  216   66
              1  124   34    0   62    0  196    0
            184    0    0    0    0    3    2    0
              0    0    0    0    0    0    0    0
              0    0  100  231    0    0    0    0
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 74 Base (2004, 5, 1, 21, 14, 11) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x33                                  .3
    decimal
              0   51
    datetime ((2004, 5, 1, 21, 14, 11))
    0000   0x4b 0x4e 0xd5 0x01 0x14                   KN...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 75 Base (2001, 0, 21, 14, 4, 22) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2001, 0, 21, 14, 4, 22))
    0000   0x16 0x04 0x4e 0xd5 0x01                   ..N..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 76 SelectBasalProfile (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x0d                                  ..
    decimal
             20   13
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 77 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x35                                  .5
    decimal
              0   53
    datetime (unknown)
    0000   0xf0                                       .
    body (0)

`end logs/ReadHistoryData-page-23.data: 78 records`
