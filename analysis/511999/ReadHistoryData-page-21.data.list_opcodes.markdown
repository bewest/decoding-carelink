## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 265, found 99 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x09 0x04 0x56 0xec 0x17 0x16 0x0d 0x00    ..V.....
    0008   0x1d 0x00 0x08 0x21 0x00 0x10 0x22 0x00    ...!..".
    0010   0x18 0x1d 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              9    4   86  236   23   22   13    0
             29    0    8   33    0   16   34    0
             24   29    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 BolusWizard 2013-07-22T10:57:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 205,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
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
    0000   0x5b 0xcd                                  [.
    decimal
             91  205
    datetime (2013-07-22T10:57:56)
    0000   0x78 0xf9 0x0a 0x76 0x0d                   x..v.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x38 0x00    .P.x<d8.
    0008   0x00 0x00 0x00 0x28 0x00 0x10 0x78         ...(..x
    decimal
              0   80    0  120   60  100   56    0
              0    0    0   40    0   16  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 0.5, 'curve': 192},
 {'age': 114, 'amount': 1.9, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x2c 0xc0 0x4c 0x72 0xc0    \..,.Lr.
    decimal
             92    8   20   44  192   76  114  192
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-07-22T10:57:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x28 0x00    ......(.
    decimal
              1    0   16    0   16    0   40    0
    datetime (2013-07-22T10:57:57)
    0000   0x79 0xf9 0x4a 0x76 0x0d                   y.Jv.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BasalProfileStart 2013-07-22T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-22T12:00:00)
    0000   0x40 0xc0 0x0c 0x16 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-22T14:19:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-07-22T14:19:38)
    0000   0x66 0xd3 0x2e 0x16 0x0d                   f....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BolusWizard 2013-07-22T14:19:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 199,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0xc7                                  [.
    decimal
             91  199
    datetime (2013-07-22T14:19:40)
    0000   0x68 0xd3 0x0e 0x76 0x0d                   h..v.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x34 0x00    .P.x<d4.
    0008   0x00 0x00 0x00 0x00 0x00 0x34 0x78         .....4x
    decimal
              0   80    0  120   60  100   52    0
              0    0    0    0    0   52  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 206, 'amount': 0.4, 'curve': 192},
 {'age': 246, 'amount': 0.5, 'curve': 192},
 {'age': 60, 'amount': 1.9, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0xce 0xc0 0x14 0xf6 0xc0    \.......
    0008   0x4c 0x3c 0xd0                             L<.
    decimal
             92   11   16  206  192   20  246  192
             76   60  208
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-07-22T14:19:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    0    0
    datetime (2013-07-22T14:19:40)
    0000   0x68 0xd3 0x4e 0x76 0x0d                   h.Nv.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 CalBGForPH 2013-07-22T16:59:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 211}
```
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2013-07-22T16:59:23)
    0000   0x57 0xfb 0x30 0x16 0x0d                   W.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 BolusWizard 2013-07-22T16:59:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 211,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
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
    datetime (2013-07-22T16:59:25)
    0000   0x59 0xfb 0x10 0x76 0x0d                   Y..v.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x3c 0x00    .P.x<d<.
    0008   0x00 0x00 0x00 0x04 0x00 0x38 0x78         .....8x
    decimal
              0   80    0  120   60  100   60    0
              0    0    0    4    0   56  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 166, 'amount': 1.3, 'curve': 192},
 {'age': 110, 'amount': 0.4, 'curve': 208},
 {'age': 150, 'amount': 0.5, 'curve': 208},
 {'age': 220, 'amount': 1.9, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x34 0xa6 0xc0 0x10 0x6e 0xd0    \.4...n.
    0008   0x14 0x96 0xd0 0x4c 0xdc 0xd0              ...L..
    decimal
             92   14   52  166  192   16  110  208
             20  150  208   76  220  208
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-07-22T16:59:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x04 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    4    0
    datetime (2013-07-22T16:59:25)
    0000   0x59 0xfb 0x50 0x76 0x0d                   Y.Pv.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 CalBGForPH 2013-07-22T20:51:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-07-22T20:51:20)
    0000   0x54 0xf3 0x34 0x16 0x0d                   T.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 BolusWizard 2013-07-22T20:51:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2013-07-22T20:51:30)
    0000   0x5e 0xf3 0x14 0x76 0x0d                   ^..v.
    body (15)
    hex
    0000   0x1d 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x74 0x00 0x00 0x00 0x00 0x74 0x78         t....tx
    decimal
             29   80    0  100   60  100    0    0
            116    0    0    0    0  116  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 238, 'amount': 1.4, 'curve': 192},
 {'age': 142, 'amount': 1.3, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x38 0xee 0xc0 0x34 0x8e 0xd0    \.8..4..
    decimal
             92    8   56  238  192   52  142  208
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-07-22T20:51:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2013-07-22T20:51:30)
    0000   0x5e 0xf3 0x54 0x76 0x0d                   ^.Tv.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 ChangeBasalProfile 2013-07-22T23:44:22 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x04                                  ..
    decimal
              8    4
    datetime (2013-07-22T23:44:22)
    0000   0x56 0xec 0x17 0x16 0x0d                   V....
    body (44)
    hex
    0000   0x00 0x1f 0x00 0x08 0x21 0x00 0x10 0x22    ....!.."
    0008   0x00 0x18 0x1d 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00                        ....
    decimal
              0   31    0    8   33    0   16   34
              0   24   29    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0
    HOUR BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-21.data: 17 records`
