## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 626, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x03 0x00 0x08 0x7d 0x5c 0x05 0x4c 0xc6    ...}\.L.
    0008   0x04 0x01 0x0a 0x0a 0x00 0x15 0xd6 0x51    .......Q
    0010   0x16 0x0d 0x0a 0x4a 0x06 0xf5 0x35 0x16    ...J..5.
    0018   0x0d 0x5b 0x4a 0x10 0xf6 0x15 0x16 0x0d    .[J.....
##### DEBUG DECIMAL
              3    0    8  125   92    5   76  198
              4    1   10   10    0   21  214   81
             22   13   10   74    6  245   53   22
             13   91   74   16  246   21   22   13
#### RECORD 0 hack1 2013-03-20T12:14:31 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x33 0x8d 0x05 0x10 0xac 0x5f 0x18    m3...._.
    0008   0x06 0x00 0x00 0x05 0xb4 0x03 0x6c 0x3c    ......l<
    0010   0x02 0x48 0x28 0x00 0x8a 0x02 0x48 0x28    .H(...H(
    0018   0x01 0xa0 0x47 0x00 0xa8 0x1d 0x00 0x00    ..G.....
    0020   0x00 0x06 0x04 0x02 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0xf4              ......
    decimal
            109   51  141    5   16  172   95   24
              6    0    0    5  180    3  108   60
              2   72   40    0  138    2   72   40
              1  160   71    0  168   29    0    0
              0    6    4    2    0    0   12    0
            232    0    0    0   10  244
    datetime (2013-03-20T12:14:31)
    0000   0x1f 0xce 0x2c 0x14 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 BolusWizard 2013-03-20T12:15:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 244,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf4                                  [.
    decimal
             91  244
    datetime (2013-03-20T12:15:18)
    0000   0x12 0xcf 0x0c 0x14 0x0d                   .....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x1a 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x3e 0x7d                   ...>}
    decimal
             47   80   13   45  106   26   36    0
              0    0    0   62  125
    HOUR BITS: [1, 1, 0]
#### RECORD 2 Bolus 2013-03-20T12:15:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2, 'dual_component': '??', 'programmed': 6.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3e 0x3e 0x00                        .>>.
    decimal
              1   62   62    0
    datetime (2013-03-20T12:15:18)
    0000   0x12 0xcf 0x4c 0x14 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-20T16:20:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-03-20T16:20:03)
    0000   0x03 0xd4 0x30 0x14 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-03-20T16:20:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-03-20T16:20:38)
    0000   0x26 0xd4 0x10 0x14 0x0d                   &....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             47   80   13   45  106    0   36    0
              0    0    0   36  125
    HOUR BITS: [1, 1, 0]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 246, 'amount': 6.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xf8 0xf6 0x04                   \....
    decimal
             92    5  248  246    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-03-20T16:20:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-03-20T16:20:38)
    0000   0x26 0xd4 0x50 0x14 0x0d                   &.P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2013-03-20T17:15:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-20T17:15:21)
    0000   0x15 0xcf 0x31 0x14 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 CalBGForPH 2013-03-20T21:09:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 211}
```
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2013-03-20T21:09:46)
    0000   0x2e 0xc9 0x35 0x14 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 BolusWizard 2013-03-20T21:11:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 211,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 9,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd3                                  [.
    decimal
             91  211
    datetime (2013-03-20T21:11:47)
    0000   0x2f 0xcb 0x15 0x14 0x0d                   /....
    body (13)
    hex
    0000   0x09 0x50 0x0d 0x2d 0x6a 0x13 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
              9   80   13   45  106   19    6    0
              0    0    0   25  125
    HOUR BITS: [1, 1, 0]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 3.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0x29 0x14                   \..).
    decimal
             92    5  144   41   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-03-20T21:11:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-03-20T21:11:47)
    0000   0x2f 0xcb 0x55 0x14 0x0d                   /.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2013-03-20T22:45:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-20T22:45:25)
    0000   0x19 0xed 0x36 0x14 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 BolusWizard 2013-03-20T22:45:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-03-20T22:45:57)
    0000   0x39 0xed 0x16 0x14 0x0d                   9....
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0xfc 0x1a 0xf0    #P.-j...
    0008   0x00 0x06 0x00 0x16 0x7d                   ....}
    decimal
             35   80   13   45  106  252   26  240
              0    6    0   22  125
    HOUR BITS: [1, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 0.9, 'curve': 4},
 {'age': 135, 'amount': 3.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x65 0x04 0x90 0x87 0x14    \.$e....
    decimal
             92    8   36  101    4  144  135   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-03-20T22:45:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-03-20T22:45:57)
    0000   0x39 0xed 0x56 0x14 0x0d                   9.V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 16 ResultTotals 2013-02-20T13:13:52 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x88                   .....
    decimal
              7    0    0    5  136
    datetime (2013-02-20T13:13:52)
    0000   0x34 0x8d 0x6d 0x34 0x8d                   4.m4.
    body (51)
    hex
    0000   0x05 0x00 0x94 0x59 0xf4 0x05 0x00 0x00    ...Y....
    0008   0x05 0x88 0x03 0x84 0x40 0x02 0x04 0x24    ....@..$
    0010   0x00 0x8a 0x02 0x04 0x24 0x01 0x90 0x4e    ....$..N
    0018   0x00 0x74 0x16 0x00 0x00 0x00 0x04 0x02    .t......
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x33 0xf0 0x0d 0x15 0x0d    ...3....
    0030   0x1f 0x00 0x06                             ...
    decimal
              5    0  148   89  244    5    0    0
              5  136    3  132   64    2    4   36
              0  138    2    4   36    1  144   78
              0  116   22    0    0    0    4    2
              0    2    0   12    0  232    0    0
              0   30    0   51  240   13   21   13
             31    0    6
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 Base (2002, 0, 30, 10, 13, 21) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x0e                                  ..
    decimal
            208   14
    datetime ((2002, 0, 30, 10, 13, 21))
    0000   0x15 0x0d 0x0a 0x7e 0x02                   ...~.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 18 Base (2001, 0, 30, 27, 13, 21) head[2], body[0] op[0xcd]

    op hex (2)
    0000   0xcd 0x2f                                  ./
    decimal
            205   47
    datetime ((2001, 0, 30, 27, 13, 21))
    0000   0x15 0x0d 0x5b 0x7e 0x31                   ..[~1
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 19 Base (2013, 0, 16, 13, 13, 21) head[2], body[0] op[0xcd]

    op hex (2)
    0000   0xcd 0x0f                                  ..
    decimal
            205   15
    datetime ((2013, 0, 16, 13, 13, 21))
    0000   0x15 0x0d 0x2d 0x50 0x0d                   ..-P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 20 Base (2000, 0, 0, 0, 34, 0) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 34, 0))
    0000   0x00 0x22 0x00 0x00 0x00                   ."...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 21 Base (2000, 4, 2, 2, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x22                                  ."
    decimal
              0   34
    datetime ((2000, 4, 2, 2, 1, 61))
    0000   0x7d 0x01 0x22 0x22 0x00                   }."".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 22 Base (2014, 4, 10, 13, 21, 15) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0xcd                                  1.
    decimal
             49  205
    datetime ((2014, 4, 10, 13, 21, 15))
    0000   0x4f 0x15 0x0d 0x0a 0xbe                   O....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 23 Base (2014, 0, 27, 13, 21, 49) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0xd2                                  8.
    decimal
             56  210
    datetime ((2014, 0, 27, 13, 21, 49))
    0000   0x31 0x15 0x0d 0x5b 0xbe                   1..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 24 ClearAlarm (2000, 0, 0, 13, 21, 17) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0xd3                                  ..
    decimal
             12  211
    datetime ((2000, 0, 0, 13, 21, 17))
    0000   0x11 0x15 0x0d 0x00 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 25 Base (2000, 4, 0, 0, 14, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 14, 42))
    0000   0x6a 0x0e 0x00 0x00 0x00                   j....
    body (0)

#### RECORD 26 Base (2012, 1, 8, 28, 61, 0) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x00                                  ..
    decimal
             15    0
    datetime ((2012, 1, 8, 28, 61, 0))
    0000   0x00 0x7d 0x5c 0x08 0x7c                   .}\.|
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 27 Base (2001, 2, 1, 4, 7, 12) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x04                                  }.
    decimal
            125    4
    datetime ((2001, 2, 1, 4, 7, 12))
    0000   0x0c 0x87 0x04 0x01 0x01                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 28 Bolus 2000-04-10T13:21:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x0c 0xd3                        ....
    decimal
              1    0   12  211
    datetime (2000-04-10T13:21:17)
    0000   0x51 0x15 0x0d 0x0a 0x00                   Q....
    body (0)

#### RECORD 29 Base (2000, 0, 27, 13, 21, 50) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0xfa                                  ..
    decimal
             19  250
    datetime ((2000, 0, 27, 13, 21, 50))
    0000   0x32 0x15 0x8d 0x5b 0x00                   2..[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 30 Base (2001, 0, 0, 13, 21, 18) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0xfa                                  ..
    decimal
             27  250
    datetime ((2001, 0, 0, 13, 21, 18))
    0000   0x12 0x15 0x0d 0x00 0x51                   ....Q
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 31 Base (2000, 4, 0, 0, 29, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 29, 42))
    0000   0x6a 0x1d 0x00 0x00 0x00                   j....
    body (0)

#### RECORD 32 Prime (2012, 0, 4, 8, 4, 11) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 9.2, 'fixed': 2.6, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x1a 0x7d 0x5c                   ...}\
    decimal
              3    0   26  125   92
    datetime ((2012, 0, 4, 8, 4, 11))
    0000   0x0b 0x04 0x68 0x04 0x7c                   ..h.|
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 33 Base (2011, 3, 1, 4, 42, 12) head[2], body[0] op[0xe0]

    op hex (2)
    0000   0xe0 0x04                                  ..
    decimal
            224    4
    datetime ((2011, 3, 1, 4, 42, 12))
    0000   0x0c 0xea 0x04 0x01 0x1b                   .....
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 34 Base (2013, 3, 21, 18, 58, 27) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x00                                  ..
    decimal
             27    0
    datetime ((2013, 3, 21, 18, 58, 27))
    0000   0x1b 0xfa 0x52 0x15 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 CalBGForPH 2013-03-21T22:00:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-03-21T22:00:26)
    0000   0x1a 0xc0 0x36 0x15 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 BolusWizard 2013-03-21T22:00:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2013-03-21T22:00:40)
    0000   0x28 0xc0 0x16 0x15 0x0d                   (....
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    =P.-j...
    0008   0x00 0x05 0x00 0x2e 0x7d                   ....}
    decimal
             61   80   13   45  106    0   46    0
              0    5    0   46  125
    HOUR BITS: [1, 1, 0]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 186, 'amount': 2.7, 'curve': 4},
 {'age': 30, 'amount': 0.1, 'curve': 20},
 {'age': 150, 'amount': 3.1, 'curve': 20},
 {'age': 160, 'amount': 0.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0xba 0x04 0x04 0x1e 0x14    \.l.....
    0008   0x7c 0x96 0x14 0x0c 0xa0 0x14              |.....
    decimal
             92   14  108  186    4    4   30   20
            124  150   20   12  160   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-03-21T22:00:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-03-21T22:00:40)
    0000   0x28 0xc0 0x56 0x15 0x0d                   (.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 39 ResultTotals 2013-02-21T13:13:53 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x20                   .... 
    decimal
              7    0    0    5   32
    datetime (2013-02-21T13:13:53)
    0000   0x35 0x8d 0x6d 0x35 0x8d                   5.m5.
    body (51)
    hex
    0000   0x05 0x10 0xab 0x70 0x00 0x04 0x00 0x00    ...p....
    0008   0x05 0x20 0x03 0x70 0x43 0x01 0xb0 0x21    . .pC..!
    0010   0x00 0x6a 0x01 0xb0 0x21 0x01 0x40 0x4a    .j..!.@J
    0018   0x00 0x70 0x1a 0x00 0x00 0x00 0x04 0x02    .p......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x4b 0x04 0xc8 0x20 0x16 0x0d    ..K.. ..
    0030   0x0a 0x3b 0x0c                             .;.
    decimal
              5   16  171  112    0    4    0    0
              5   32    3  112   67    1  176   33
              0  106    1  176   33    1   64   74
              0  112   26    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0   10   75    4  200   32   22   13
             10   59   12
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 40 Base (2014, 2, 27, 27, 13, 22) head[2], body[0] op[0xc7]

    op hex (2)
    0000   0xc7 0x28                                  .(
    decimal
            199   40
    datetime ((2014, 2, 27, 27, 13, 22))
    0000   0x16 0x8d 0x5b 0x3b 0x0e                   ..[;.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1]
#### RECORD 41 Base (2013, 0, 17, 0, 13, 22) head[2], body[0] op[0xc7]

    op hex (2)
    0000   0xc7 0x08                                  ..
    decimal
            199    8
    datetime ((2013, 0, 17, 0, 13, 22))
    0000   0x16 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 42 Base (2000, 0, 0, 0, 0, 42) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 42))
    0000   0x2a 0x00 0x00 0x00 0x00                   *....
    body (0)

#### RECORD 43 Base (2000, 4, 10, 10, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2a                                  .*
    decimal
              0   42
    datetime ((2000, 4, 10, 10, 1, 61))
    0000   0x7d 0x01 0x2a 0x2a 0x00                   }.**.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 44 Base (2000, 4, 30, 13, 22, 8) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0xc7                                  ..
    decimal
             14  199
    datetime ((2000, 4, 30, 13, 22, 8))
    0000   0x48 0x16 0x0d 0x1e 0x00                   H....
    body (0)

#### RECORD 45 Base (2000, 0, 31, 13, 22, 12) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0xe9                                  ..
    decimal
              9  233
    datetime ((2000, 0, 31, 13, 22, 12))
    0000   0x0c 0x16 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 46 Base (2013, 0, 10, 13, 22, 12) head[2], body[0] op[0x2f]

    op hex (2)
    0000   0x2f 0xfb                                  /.
    decimal
             47  251
    datetime ((2013, 0, 10, 13, 22, 12))
    0000   0x0c 0x16 0x0d 0x0a 0x5d                   ....]
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 47 Prime (2014, 5, 9, 24, 29, 27) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.3, 'fixed': 4.6, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0xc9 0x2e 0x16 0x0d                   .....
    decimal
              3  201   46   22   13
    datetime ((2014, 5, 9, 24, 29, 27))
    0000   0x5b 0x5d 0x18 0xc9 0x0e                   []...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 0]
#### RECORD 48 TempBasalDuration 2010-01-13T13:16:29 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 390}
```
    op hex (2)
    0000   0x16 0x0d                                  ..
    decimal
             22   13
    datetime (2010-01-13T13:16:29)
    0000   0x1d 0x50 0x0d 0x2d 0x6a                   .P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 49 Base (2003, 12, 0, 0, 0, 48) head[2], body[0] op[0xfd]

    op hex (2)
    0000   0xfd 0x16                                  ..
    decimal
            253   22
    datetime ((2003, 12, 0, 0, 0, 48))
    0000   0xf0 0x00 0x00 0x00 0x13                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 50 Base (2001, 2, 20, 13, 40, 5) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x5c                                  }\
    decimal
            125   92
    datetime ((2001, 2, 20, 13, 40, 5))
    0000   0x05 0xa8 0x6d 0x14 0x01                   ..m..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 51 Base (2006, 0, 14, 9, 24, 0) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x13                                  ..
    decimal
             19   19
    datetime ((2006, 0, 14, 9, 24, 0))
    0000   0x00 0x18 0xc9 0x4e 0x16                   ...N.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 52 Base (2006, 8, 17, 22, 9, 47) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2006, 8, 17, 22, 9, 47))
    0000   0xaf 0x09 0xd6 0x31 0x16                   ...1.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 53 Base (2006, 8, 17, 22, 20, 47) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2006, 8, 17, 22, 20, 47))
    0000   0xaf 0x14 0xd6 0x11 0x16                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 54 Base (2011, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2011, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x0b                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-34.data: 55 records`
