## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 188, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x74 0x78 0x5c 0x08 0x38 0xee 0xc0 0x34    tx\.8..4
    0008   0x8e 0xd0 0x01 0x00 0x74 0x00 0x74 0x00    ....t.t.
    0010   0x00 0x00 0x5e 0xf3 0x54 0x76 0x0d 0x08    ..^.Tv..
    0018   0x04 0x56 0xec 0x17 0x16 0x0d 0x00 0x1f    .V......
##### DEBUG DECIMAL
            116  120   92    8   56  238  192   52
            142  208    1    0  116    0  116    0
              0    0   94  243   84  118   13    8
              4   86  236   23   22   13    0   31
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

#### RECORD 2 Bolus (2009, 0, 0, 8, 0, 16) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x10 0x00                        ....
    decimal
              1    0   16    0
    datetime ((2009, 0, 0, 8, 0, 16))
    0000   0x10 0x00 0x28 0x00 0x79                   ..(.y
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 3 Base (2000, 4, 3, 27, 13, 54) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x4a                                  .J
    decimal
            249   74
    datetime ((2000, 4, 3, 27, 13, 54))
    0000   0x76 0x0d 0x7b 0x03 0x40                   v.{.@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 4 Base (2000, 0, 29, 24, 13, 22) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x0c                                  ..
    decimal
            192   12
    datetime ((2000, 0, 29, 24, 13, 22))
    0000   0x16 0x0d 0x18 0x1d 0x00                   .....
    body (0)

#### RECORD 5 CalBGForPH 2013-07-22T14:19:38 head[2], body[0] op[0x0a]
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
#### RECORD 6 BolusWizard 2013-07-22T14:19:40 head[2], body[15] op[0x5b]
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
#### RECORD 7 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
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

#### RECORD 8 Bolus (2008, 0, 0, 0, 0, 52) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x34 0x00                        ..4.
    decimal
              1    0   52    0
    datetime ((2008, 0, 0, 0, 0, 52))
    0000   0x34 0x00 0x00 0x00 0x68                   4...h
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 9 Base (2007, 4, 19, 10, 13, 54) head[2], body[0] op[0xd3]

    op hex (2)
    0000   0xd3 0x4e                                  .N
    decimal
            211   78
    datetime ((2007, 4, 19, 10, 13, 54))
    0000   0x76 0x0d 0x0a 0xd3 0x57                   v...W
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 10 Base (2009, 0, 19, 27, 13, 22) head[2], body[0] op[0xfb]

    op hex (2)
    0000   0xfb 0x30                                  .0
    decimal
            251   48
    datetime ((2009, 0, 19, 27, 13, 22))
    0000   0x16 0x0d 0x5b 0xd3 0x59                   ..[.Y
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 11 Base (2000, 4, 16, 0, 13, 54) head[2], body[0] op[0xfb]

    op hex (2)
    0000   0xfb 0x10                                  ..
    decimal
            251   16
    datetime ((2000, 4, 16, 0, 13, 54))
    0000   0x76 0x0d 0x00 0x50 0x00                   v..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 Base (2000, 4, 0, 0, 60, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 4, 0, 0, 60, 36))
    0000   0x64 0x3c 0x00 0x00 0x00                   d<...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 Base (2014, 0, 28, 24, 56, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2014, 0, 28, 24, 56, 0))
    0000   0x00 0x38 0x78 0x5c 0x0e                   .8x\.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 14 LowReservoir 2004-12-16T14:16:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 16.6}
```
    op hex (2)
    0000   0x34 0xa6                                  4.
    decimal
             52  166
    datetime (2004-12-16T14:16:00)
    0000   0xc0 0x10 0x6e 0xd0 0x14                   ..n..
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 15 Base (2000, 7, 1, 16, 28, 12) head[2], body[0] op[0x96]

    op hex (2)
    0000   0x96 0xd0                                  ..
    decimal
            150  208
    datetime ((2000, 7, 1, 16, 28, 12))
    0000   0x4c 0xdc 0xd0 0x01 0x00                   L....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 16 Base (2009, 0, 0, 4, 0, 56) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x00                                  8.
    decimal
             56    0
    datetime ((2009, 0, 0, 4, 0, 56))
    0000   0x38 0x00 0x04 0x00 0x59                   8...Y
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 17 Base (2004, 4, 16, 10, 13, 54) head[2], body[0] op[0xfb]

    op hex (2)
    0000   0xfb 0x50                                  .P
    decimal
            251   80
    datetime ((2004, 4, 16, 10, 13, 54))
    0000   0x76 0x0d 0x0a 0x70 0x54                   v..pT
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 18 Base (2014, 0, 16, 27, 13, 22) head[2], body[0] op[0xf3]

    op hex (2)
    0000   0xf3 0x34                                  .4
    decimal
            243   52
    datetime ((2014, 0, 16, 27, 13, 22))
    0000   0x16 0x0d 0x5b 0x70 0x5e                   ..[p^
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 19 Base (2000, 4, 16, 29, 13, 54) head[2], body[0] op[0xf3]

    op hex (2)
    0000   0xf3 0x14                                  ..
    decimal
            243   20
    datetime ((2000, 4, 16, 29, 13, 54))
    0000   0x76 0x0d 0x1d 0x50 0x00                   v..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 20 ChangeTimeDisplay 2000-04-20T00:00:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-20T00:00:36)
    0000   0x64 0x00 0x00 0x74 0x00                   d..t.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-21.data: 21 records`
