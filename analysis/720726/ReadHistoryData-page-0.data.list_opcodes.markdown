## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 296, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x64 0x00 0x00 0x00 0x00 0x64 0x36 0x5c    d....d6\
    0008   0x17 0x14 0x0e 0x04 0x78 0x18 0x04 0x5c    ....x..\
    0010   0xb8 0x04 0x20 0x12 0x14 0x0c 0x30 0x14    .. ...0.
    0018   0x20 0x62 0x14 0x80 0x76 0x14 0x01 0x00     b..v...
##### DEBUG DECIMAL
            100    0    0    0    0  100   54   92
             23   20   14    4  120   24    4   92
            184    4   32   18   20   12   48   20
             32   98   20  128  118   20    1    0
#### RECORD 0 BasalProfileStart 2013-09-10T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-10T13:00:00)
    0000   0x80 0x40 0x0d 0x0a 0x0d                   .@...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 1 CalBGForPH 2013-09-10T13:32:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2013-09-10T13:32:00)
    0000   0x80 0x60 0x4d 0x0a 0x0d                   .`M..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2013-09-10T13:32:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 61,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 14.0,
 'carb_input': 4,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 1.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 12}
```
    op hex (2)
    0000   0x5b 0x3d                                  [=
    decimal
             91   61
    datetime (2013-09-10T13:32:07)
    0000   0x87 0x60 0x0d 0x6a 0x0d                   .`.j.
    body (15)
    hex
    0000   0x04 0x90 0x00 0x6e 0x17 0x36 0x0c 0x00    ...n.6..
    0008   0x0c 0x00 0x00 0x8c 0x00 0x0c 0x36         ......6
    decimal
              4  144    0  110   23   54   12    0
             12    0    0  140    0   12   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 0.8, 'curve': 4},
 {'age': 74, 'amount': 3.2, 'curve': 4},
 {'age': 184, 'amount': 0.5, 'curve': 4},
 {'age': 194, 'amount': 1.8, 'curve': 4},
 {'age': 224, 'amount': 1.0, 'curve': 4},
 {'age': 18, 'amount': 1.2, 'curve': 20},
 {'age': 28, 'amount': 1.9, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x20 0x36 0x04 0x80 0x4a 0x04    \. 6..J.
    0008   0x14 0xb8 0x04 0x48 0xc2 0x04 0x28 0xe0    ...H..(.
    0010   0x04 0x30 0x12 0x14 0x4c 0x1c 0x14         .0..L..
    decimal
             92   23   32   54    4  128   74    4
             20  184    4   72  194    4   40  224
              4   48   18   20   76   28   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-09-10T13:32:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x0c 0x00 0x0c 0x00 0x8c 0x00    ........
    decimal
              1    0   12    0   12    0  140    0
    datetime (2013-09-10T13:32:07)
    0000   0x87 0x60 0x4d 0x6a 0x0d                   .`Mj.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 CalBGForPH 2013-09-10T13:59:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 56}
```
    op hex (2)
    0000   0x0a 0x38                                  .8
    decimal
             10   56
    datetime (2013-09-10T13:59:42)
    0000   0xaa 0x7b 0x4d 0x0a 0x0d                   .{M..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2013-09-10T13:59:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 56,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 11.6,
 'carb_input': 9,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x38                                  [8
    decimal
             91   56
    datetime (2013-09-10T13:59:48)
    0000   0xb0 0x7b 0x0d 0x6a 0x0d                   .{.j.
    body (15)
    hex
    0000   0x09 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x20 0x00 0x00 0x74 0x00 0x20 0x36          ..t. 6
    decimal
              9  144    0  110   23   54    0    0
             32    0    0  116    0   32   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 0.3, 'curve': 4},
 {'age': 81, 'amount': 0.8, 'curve': 4},
 {'age': 101, 'amount': 3.2, 'curve': 4},
 {'age': 211, 'amount': 0.5, 'curve': 4},
 {'age': 221, 'amount': 1.8, 'curve': 4},
 {'age': 251, 'amount': 1.0, 'curve': 4},
 {'age': 45, 'amount': 1.2, 'curve': 20},
 {'age': 55, 'amount': 1.9, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x0c 0x1f 0x04 0x20 0x51 0x04    \.... Q.
    0008   0x80 0x65 0x04 0x14 0xd3 0x04 0x48 0xdd    .e....H.
    0010   0x04 0x28 0xfb 0x04 0x30 0x2d 0x14 0x4c    .(..0-.L
    0018   0x37 0x14                                  7.
    decimal
             92   26   12   31    4   32   81    4
            128  101    4   20  211    4   72  221
              4   40  251    4   48   45   20   76
             55   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-09-10T13:59:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x74 0x00    .. . .t.
    decimal
              1    0   32    0   32    0  116    0
    datetime (2013-09-10T13:59:49)
    0000   0xb1 0x7b 0x4d 0x6a 0x0d                   .{Mj.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 BolusWizard 2013-09-10T15:32:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-10T15:32:03)
    0000   0x83 0x60 0x0f 0x6a 0x0d                   .`.j.
    body (15)
    hex
    0000   0x1a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x5c 0x00 0x00 0x00 0x00 0x5c 0x36         \....\6
    decimal
             26  144    0  110   23   54    0    0
             92    0    0    0    0   92   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 0.8, 'curve': 4},
 {'age': 124, 'amount': 0.3, 'curve': 4},
 {'age': 174, 'amount': 0.8, 'curve': 4},
 {'age': 194, 'amount': 3.2, 'curve': 4},
 {'age': 48, 'amount': 0.5, 'curve': 20},
 {'age': 58, 'amount': 1.8, 'curve': 20},
 {'age': 88, 'amount': 1.0, 'curve': 20},
 {'age': 138, 'amount': 1.2, 'curve': 20},
 {'age': 148, 'amount': 1.9, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x20 0x5e 0x04 0x0c 0x7c 0x04    \. ^..|.
    0008   0x20 0xae 0x04 0x80 0xc2 0x04 0x14 0x30     ......0
    0010   0x14 0x48 0x3a 0x14 0x28 0x58 0x14 0x30    .H:.(X.0
    0018   0x8a 0x14 0x4c 0x94 0x14                   ..L..
    decimal
             92   29   32   94    4   12  124    4
             32  174    4  128  194    4   20   48
             20   72   58   20   40   88   20   48
            138   20   76  148   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-09-10T15:32:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x34 0x00    ..\.\.4.
    decimal
              1    0   92    0   92    0   52    0
    datetime (2013-09-10T15:32:03)
    0000   0x83 0x60 0x4f 0x6a 0x0d                   .`Oj.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 CalBGForPH 2013-09-10T18:15:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2013-09-10T18:15:43)
    0000   0xab 0x4f 0x52 0x0a 0x0d                   .OR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 13 BolusWizard 2013-09-10T18:15:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 94,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.0,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x5e                                  [^
    decimal
             91   94
    datetime (2013-09-10T18:15:58)
    0000   0xba 0x4f 0x12 0x6a 0x0d                   .O.j.
    body (15)
    hex
    0000   0x1a 0x90 0x00 0x6e 0x17 0x36 0x44 0x00    ...n.6D.
    0008   0x5c 0x00 0x00 0x14 0x00 0x8c 0x36         \.....6
    decimal
             26  144    0  110   23   54   68    0
             92    0    0   20    0  140   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 167, 'amount': 2.3, 'curve': 4},
 {'age': 1, 'amount': 0.8, 'curve': 20},
 {'age': 31, 'amount': 0.3, 'curve': 20},
 {'age': 81, 'amount': 0.8, 'curve': 20},
 {'age': 101, 'amount': 3.2, 'curve': 20},
 {'age': 211, 'amount': 0.5, 'curve': 20},
 {'age': 221, 'amount': 1.8, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x5c 0xa7 0x04 0x20 0x01 0x14    \.\.. ..
    0008   0x0c 0x1f 0x14 0x20 0x51 0x14 0x80 0x65    ... Q..e
    0010   0x14 0x14 0xd3 0x14 0x48 0xdd 0x14         ....H..
    decimal
             92   23   92  167    4   32    1   20
             12   31   20   32   81   20  128  101
             20   20  211   20   72  221   20
    datetime (unknown)

    body (0)

#### RECORD 15 Base (2013, 9, 10, 18, 15, 58) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2013, 9, 10, 18, 15, 58))
    0000   0xba 0x4f 0x72 0x0a 0x0d                   .Or..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 16 Base (2012, 0, 0, 12, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2012, 0, 0, 12, 0, 1))
    0000   0x01 0x00 0x8c 0x00 0x8c                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 Base (2010, 2, 18, 15, 58, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x14                                  ..
    decimal
              0   20
    datetime ((2010, 2, 18, 15, 58, 0))
    0000   0x00 0xba 0x4f 0x52 0x6a                   ..ORj
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 18 Base (2010, 2, 18, 0, 40, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2010, 2, 18, 0, 40, 0))
    0000   0x00 0xa8 0x60 0x12 0x6a                   ..`.j
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1c                                  ..
    decimal
             13   28
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-0.data: 20 records`
