## START logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 300, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x03 0x00 0x12 0x7d 0x5c 0x0b 0x34 0xb1    ...}\.4.
    0008   0x04 0x34 0xab 0x14 0x7c 0xb5 0x14 0x34    .4..|..4
    0010   0xc8 0x6d 0x16 0x0a 0x15 0x0d 0x01 0x12    .m......
    0018   0x12 0x00 0x71 0x15 0x4a 0x15 0x0d 0x5b    ..q.J..[
##### DEBUG DECIMAL
              3    0   18  125   92   11   52  177
              4   52  171   20  124  181   20   52
            200  109   22   10   21   13    1   18
             18    0  113   21   74   21   13   91
#### RECORD 0 BolusWizard 2013-04-20T22:40:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 176,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2013-04-20T22:40:40)
    0000   0x68 0x28 0x16 0x14 0x0d                   h(...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    7    0    4  125
    HOUR BITS: [0, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 1.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x7e 0x04                   \.@~.
    decimal
             92    5   64  126    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-04-20T22:40:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-04-20T22:40:40)
    0000   0x68 0x28 0x56 0x14 0x0d                   h(V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalBGForPH 2013-04-20T22:46:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2013-04-20T22:46:50)
    0000   0x72 0x2e 0x36 0x14 0x0d                   r.6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BolusWizard 2013-04-20T22:47:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 177,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb1                                  [.
    decimal
             91  177
    datetime (2013-04-20T22:47:07)
    0000   0x47 0x2f 0x16 0x14 0x0d                   G/...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x0b 0x2e 0x00    <P.-j...
    0008   0x00 0x0b 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106   11   46    0
              0   11    0   46  125
    HOUR BITS: [0, 0, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 0.4, 'curve': 4},
 {'age': 133, 'amount': 1.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x0d 0x04 0x40 0x85 0x04    \....@..
    decimal
             92    8   16   13    4   64  133    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-04-20T22:47:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-04-20T22:47:07)
    0000   0x47 0x2f 0x56 0x14 0x0d                   G/V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 BolusWizard 2013-04-20T23:10:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-04-20T23:10:36)
    0000   0x64 0x0a 0x17 0x14 0x0d                   d....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125

#### RECORD 8 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 4.6, 'curve': 4},
 {'age': 36, 'amount': 0.4, 'curve': 4},
 {'age': 156, 'amount': 1.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0xb8 0x1a 0x04 0x10 0x24 0x04    \.....$.
    0008   0x40 0x9c 0x04                             @..
    decimal
             92   11  184   26    4   16   36    4
             64  156    4
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-04-20T23:10:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-04-20T23:10:36)
    0000   0x64 0x0a 0x57 0x14 0x0d                   d.W..
    body (0)

#### RECORD 10 ResultTotals 2013-04-20T13:13:20 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbc                   .....
    decimal
              7    0    0    4  188
    datetime (2013-04-20T13:13:20)
    0000   0x54 0x0d 0x6d 0x54 0x0d                   T.mT.
    body (51)
    hex
    0000   0x05 0x00 0xb9 0xb0 0xc9 0x03 0x00 0x00    ........
    0008   0x04 0xbc 0x03 0x84 0x4a 0x01 0x38 0x1a    ....J.8.
    0010   0x00 0x4c 0x01 0x38 0x1a 0x00 0xe8 0x4a    .L.8...J
    0018   0x00 0x50 0x1a 0x00 0x00 0x00 0x04 0x02    .P......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x47 0x70 0x0b 0x23 0x15 0x8d    ..Gp.#..
    0030   0x5b 0x47 0x79                             [Gy
    decimal
              5    0  185  176  201    3    0    0
              4  188    3  132   74    1   56   26
              0   76    1   56   26    0  232   74
              0   80   26    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0   10   71  112   11   35   21  141
             91   71  121
    DAY BITS: [0, 1, 0]
#### RECORD 11 Ian0B (2013, 0, 13, 17, 0, 13) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x03 0x15                             ...
    decimal
             11    3   21
    datetime ((2013, 0, 13, 17, 0, 13))
    0000   0x0d 0x00 0x51 0x0d 0x2d                   ..Q.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 12 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x2c                                  j,
    decimal
            106   44
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 13 Base (2004, 4, 23, 16, 14, 28) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x7d                                  ,}
    decimal
             44  125
    datetime ((2004, 4, 23, 16, 14, 28))
    0000   0x5c 0x0e 0x30 0xf7 0x04                   \.0..
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 14 Base (2000, 0, 20, 21, 16, 20) head[2], body[0] op[0xb8]

    op hex (2)
    0000   0xb8 0x0b                                  ..
    decimal
            184   11
    datetime ((2000, 0, 20, 21, 16, 20))
    0000   0x14 0x10 0x15 0x14 0x40                   ....@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 15 Base (2009, 0, 0, 12, 44, 1) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x14                                  ..
    decimal
            141   20
    datetime ((2009, 0, 0, 12, 44, 1))
    0000   0x01 0x2c 0x2c 0x00 0x79                   .,,.y
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 16 Ian0B (2009, 0, 27, 26, 10, 13) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x43 0x15                             .C.
    decimal
             11   67   21
    datetime ((2009, 0, 27, 26, 10, 13))
    0000   0x0d 0x0a 0xba 0x7b 0x19                   ...{.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 17 ChangeRemoteID (2010, 1, 2, 26, 27, 13) head[2], body[0] op[0x27]

    op hex (2)
    0000   0x27 0x15                                  '.
    decimal
             39   21
    datetime ((2010, 1, 2, 26, 27, 13))
    0000   0x0d 0x5b 0xba 0x42 0x1a                   .[.B.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 18 ResultTotals (2000, 0, 13, 10, 45, 13) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x15 0x0d 0x00 0x50                   ....P
    decimal
              7   21   13    0   80
    datetime ((2000, 0, 13, 10, 45, 13))
    0000   0x0d 0x2d 0x6a 0x0d 0x00                   .-j..
    body (51)
    hex
    0000   0x00 0x00 0x00 0x00 0x0d 0x7d 0x5c 0x08    .....}\.
    0008   0x34 0xfc 0x04 0x7c 0x06 0x14 0x01 0x0d    4..|....
    0010   0x0d 0x00 0x42 0x1a 0x47 0x15 0x0d 0x1e    ..B.G...
    0018   0x00 0x54 0x2a 0x08 0x15 0x0d 0x1f 0x00    .T*.....
    0020   0x6f 0x0b 0x09 0x15 0x0d 0x0a 0xdc 0x6f    o......o
    0028   0x15 0x2a 0x15 0x0d 0x5b 0xdc 0x71 0x15    .*..[.q.
    0030   0x0a 0x15 0x0d                             ...
    decimal
              0    0    0    0   13  125   92    8
             52  252    4  124    6   20    1   13
             13    0   66   26   71   21   13   30
              0   84   42    8   21   13   31    0
            111   11    9   21   13   10  220  111
             21   42   21   13   91  220  113   21
             10   21   13
    HOUR BITS: [0, 0, 1]
#### RECORD 19 Base (2000, 0, 21, 10, 45, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x50                                  .P
    decimal
              0   80
    datetime ((2000, 0, 21, 10, 45, 13))
    0000   0x0d 0x2d 0x6a 0x15 0x00                   .-j..
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-25.data: 20 records`
