## START analysis/ianj/raw/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 459, found 563 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x7d 0x65                                  }e
##### DEBUG DECIMAL
            125  101
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

#### RECORD 15 Ian69 2013-09-10T18:15:58 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-10T18:15:58)
    0000   0xba 0x4f 0x72 0x0a 0x0d                   .Or..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 1, 0]
#### RECORD 16 Bolus 2013-09-10T18:15:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x14 0x00    ........
    decimal
              1    0  140    0  140    0   20    0
    datetime (2013-09-10T18:15:58)
    0000   0xba 0x4f 0x52 0x6a 0x0d                   .ORj.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2013-09-10T18:32:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-10T18:32:40)
    0000   0xa8 0x60 0x12 0x6a 0x0d                   .`.j.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 0.5, 'curve': 4},
 {'age': 24, 'amount': 3.0, 'curve': 4},
 {'age': 184, 'amount': 2.3, 'curve': 4},
 {'age': 18, 'amount': 0.8, 'curve': 20},
 {'age': 48, 'amount': 0.3, 'curve': 20},
 {'age': 98, 'amount': 0.8, 'curve': 20},
 {'age': 118, 'amount': 3.2, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x14 0x0e 0x04 0x78 0x18 0x04    \....x..
    0008   0x5c 0xb8 0x04 0x20 0x12 0x14 0x0c 0x30    \.. ...0
    0010   0x14 0x20 0x62 0x14 0x80 0x76 0x14         . b..v.
    decimal
             92   23   20   14    4  120   24    4
             92  184    4   32   18   20   12   48
             20   32   98   20  128  118   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-09-10T18:32:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x98 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  152    0
    datetime (2013-09-10T18:32:40)
    0000   0xa8 0x60 0x52 0x6a 0x0d                   .`Rj.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 TempBasal 2013-09-10T19:15:43 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-09-10T19:15:43)
    0000   0xab 0x4f 0x13 0x0a 0x0d                   .O...
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [0, 1, 0]
#### RECORD 21 TempBasalDuration 2013-09-10T19:15:43 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 30}
```
    op hex (2)
    0000   0x16 0x01                                  ..
    decimal
             22    1
    datetime (2013-09-10T19:15:43)
    0000   0xab 0x4f 0x13 0x0a 0x0d                   .O...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 22 BasalProfileStart 2013-09-10T19:45:43 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-10T19:45:43)
    0000   0xab 0x6d 0x13 0x0a 0x0d                   .m...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2013-09-10T19:50:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-10T19:50:57)
    0000   0xb9 0x72 0x13 0x6a 0x0d                   .r.j.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 2.5, 'curve': 4},
 {'age': 92, 'amount': 0.5, 'curve': 4},
 {'age': 102, 'amount': 3.0, 'curve': 4},
 {'age': 6, 'amount': 2.3, 'curve': 20},
 {'age': 96, 'amount': 0.8, 'curve': 20},
 {'age': 126, 'amount': 0.3, 'curve': 20},
 {'age': 176, 'amount': 0.8, 'curve': 20},
 {'age': 196, 'amount': 3.2, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x64 0x52 0x04 0x14 0x5c 0x04    \.dR..\.
    0008   0x78 0x66 0x04 0x5c 0x06 0x14 0x20 0x60    xf.\.. `
    0010   0x14 0x0c 0x7e 0x14 0x20 0xb0 0x14 0x80    ..~. ...
    0018   0xc4 0x14                                  ..
    decimal
             92   26  100   82    4   20   92    4
            120  102    4   92    6   20   32   96
             20   12  126   20   32  176   20  128
            196   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-09-10T19:50:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x98 0x00    ..l.l...
    decimal
              1    0  108    0  108    0  152    0
    datetime (2013-09-10T19:50:57)
    0000   0xb9 0x72 0x53 0x6a 0x0d                   .rSj.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 CalBGForPH 2013-09-10T20:24:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 37}
```
    op hex (2)
    0000   0x0a 0x25                                  .%
    decimal
             10   37
    datetime (2013-09-10T20:24:39)
    0000   0xa7 0x58 0x54 0x0a 0x0d                   .XT..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 27 TempBasal 2013-09-10T20:25:05 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-09-10T20:25:05)
    0000   0x85 0x59 0x14 0x0a 0x0d                   .Y...
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [0, 1, 0]
#### RECORD 28 TempBasalDuration 2013-09-10T20:25:05 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 30}
```
    op hex (2)
    0000   0x16 0x01                                  ..
    decimal
             22    1
    datetime (2013-09-10T20:25:05)
    0000   0x85 0x59 0x14 0x0a 0x0d                   .Y...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 29 BasalProfileStart 2013-09-10T20:55:05 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-10T20:55:05)
    0000   0x85 0x77 0x14 0x0a 0x0d                   .w...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 1]
`end analysis/ianj/raw/ReadHistoryData-page-0.data: 30 records`
