## START logs/ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 634, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x5d 0xda 0x48 0x7a 0x0d 0x7b 0x02 0x40    ].Hz.{.@
    0008   0xde 0x09 0x1a 0x0d 0x13 0x1e 0x00 0x5b    .......[
    0010   0x00 0x73 0xe4 0x09 0x7a 0x0d 0x0f 0x90    .s..z...
    0018   0x00 0x6e 0x17 0x36 0x00 0x00 0x34 0x00    .n.6..4.
##### DEBUG DECIMAL
             93  218   72  122   13  123    2   64
            222    9   26   13   19   30    0   91
              0  115  228    9  122   13   15  144
              0  110   23   54    0    0   52    0
#### RECORD 0 BolusWizard 2013-07-25T12:46:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-25T12:46:34)
    0000   0x62 0xee 0x0c 0x79 0x0d                   b..y.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 2.7, 'curve': 4},
 {'age': 251, 'amount': 1.9, 'curve': 4},
 {'age': 65, 'amount': 1.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0x33 0x04 0x4c 0xfb 0x04    \.l3.L..
    0008   0x34 0x41 0x14                             4A.
    decimal
             92   11  108   51    4   76  251    4
             52   65   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-07-25T12:46:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x60 0x00    ......`.
    decimal
              1    0   28    0   28    0   96    0
    datetime (2013-07-25T12:46:34)
    0000   0x62 0xee 0x4c 0x79 0x0d                   b.Ly.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BasalProfileStart 2013-07-25T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-25T13:00:00)
    0000   0x40 0xc0 0x0d 0x19 0x0d                   @....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-25T14:56:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2013-07-25T14:56:56)
    0000   0x78 0xf8 0x2e 0x79 0x0d                   x..y.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 Ian3F 2013-07-25T14:56:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2013-07-25T14:56:56)
    0000   0x78 0xf8 0x2e 0x79 0x0d                   x..y.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2013-07-25T14:57:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 94,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 3.2,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x5e                                  [^
    decimal
             91   94
    datetime (2013-07-25T14:57:14)
    0000   0x4e 0xf9 0x0e 0x79 0x0d                   N..y.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x44 0x00    ...n.6D.
    0008   0x48 0x00 0x00 0x20 0x00 0x6c 0x36         H.. .l6
    decimal
             20  144    0  110   23   54   68    0
             72    0    0   32    0  108   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 132, 'amount': 0.7, 'curve': 4},
 {'age': 182, 'amount': 2.7, 'curve': 4},
 {'age': 126, 'amount': 1.9, 'curve': 20},
 {'age': 196, 'amount': 1.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1c 0x84 0x04 0x6c 0xb6 0x04    \....l..
    0008   0x4c 0x7e 0x14 0x34 0xc4 0x14              L~.4..
    decimal
             92   14   28  132    4  108  182    4
             76  126   20   52  196   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-07-25T14:57:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x20 0x00    ..l.l. .
    decimal
              1    0  108    0  108    0   32    0
    datetime (2013-07-25T14:57:14)
    0000   0x4e 0xf9 0x4e 0x79 0x0d                   N.Ny.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 CalBGForPH 2013-07-25T17:45:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 65}
```
    op hex (2)
    0000   0x0a 0x41                                  .A
    decimal
             10   65
    datetime (2013-07-25T17:45:04)
    0000   0x44 0xed 0x31 0x79 0x0d                   D.1y.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 Ian3F 2013-07-25T17:45:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2013-07-25T17:45:04)
    0000   0x44 0xed 0x31 0x79 0x0d                   D.1y.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 11 CalBGForPH 2013-07-25T18:45:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 218}
```
    op hex (2)
    0000   0x0a 0xda                                  ..
    decimal
             10  218
    datetime (2013-07-25T18:45:34)
    0000   0x62 0xed 0x32 0x79 0x0d                   b.2y.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2013-07-25T18:45:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2013-07-25T18:45:34)
    0000   0x62 0xed 0x52 0x79 0x0d                   b.Ry.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2013-07-25T18:45:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 11.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-07-25T18:45:44)
    0000   0x6c 0xed 0x12 0x79 0x0d                   l..y.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x74 0x00    #..n.6t.
    0008   0x7c 0x00 0x00 0x08 0x00 0xe8 0x36         |.....6
    decimal
             35  144    0  110   23   54  116    0
            124    0    0    8    0  232   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 230, 'amount': 2.7, 'curve': 4},
 {'age': 104, 'amount': 0.7, 'curve': 20},
 {'age': 154, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0xe6 0x04 0x1c 0x68 0x14    \.l...h.
    0008   0x6c 0x9a 0x14                             l..
    decimal
             92   11  108  230    4   28  104   20
            108  154   20
    datetime (unknown)

    body (0)

#### RECORD 15 Ian69 2013-07-25T18:45:44 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-25T18:45:44)
    0000   0x6c 0xed 0x72 0x19 0x0d                   l.r..
    body (8)
    hex
    0000   0x15 0x1e 0x01 0x00 0xe8 0x00 0xe8 0x00    ........
    decimal
             21   30    1    0  232    0  232    0
    HOUR BITS: [1, 1, 1]
#### RECORD 16 ChangeBasalProfile 2013-07-25T18:45:44 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x00                                  ..
    decimal
              8    0
    datetime (2013-07-25T18:45:44)
    0000   0x6c 0xed 0x52 0x79 0x0d                   l.Ry.
    body (44)
    hex
    0000   0x5b 0x00 0x54 0xf6 0x14 0x79 0x0d 0x12    [.T..y..
    0008   0x90 0x00 0x6e 0x17 0x36 0x00 0x00 0x40    ..n.6..@
    0010   0x00 0x00 0x00 0x00 0x40 0x36 0x5c 0x08    ....@6\.
    0018   0xe8 0x81 0x04 0x6c 0x67 0x14 0x01 0x00    ...lg...
    0020   0x40 0x00 0x40 0x00 0x60 0x00 0x54 0xf6    @.@.`.T.
    0028   0x54 0x79 0x0d 0x5b                        Ty.[
    decimal
             91    0   84  246   20  121   13   18
            144    0  110   23   54    0    0   64
              0    0    0    0   64   54   92    8
            232  129    4  108  103   20    1    0
             64    0   64    0   96    0   84  246
             84  121   13   91
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 Base (2013, 12, 13, 25, 21, 51) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x59                                  .Y
    decimal
              0   89
    datetime ((2013, 12, 13, 25, 21, 51))
    0000   0xf3 0x15 0x79 0x0d 0x0d                   ..y..
    body (0)

#### RECORD 18 Base (2000, 4, 0, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 0, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x00 0x00                   n.6..
    body (0)

#### RECORD 19 Base (2006, 0, 12, 0, 0, 0) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x00                                  ,.
    decimal
             44    0
    datetime ((2006, 0, 12, 0, 0, 0))
    0000   0x00 0x00 0x00 0x2c 0x36                   ...,6
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 0.6, 'curve': 4},
 {'age': 66, 'amount': 1.0, 'curve': 4},
 {'age': 186, 'amount': 5.8, 'curve': 4},
 {'age': 160, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x38 0x04 0x28 0x42 0x04    \..8.(B.
    0008   0xe8 0xba 0x04 0x6c 0xa0 0x14              ...l..
    decimal
             92   14   24   56    4   40   66    4
            232  186    4  108  160   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-07-25T21:51:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x58 0x00    ..,.,.X.
    decimal
              1    0   44    0   44    0   88    0
    datetime (2013-07-25T21:51:25)
    0000   0x59 0xf3 0x55 0x79 0x0d                   Y.Uy.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2013-07-25T22:11:21 head[2], body[15] op[0x5b]
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
    datetime (2013-07-25T22:11:21)
    0000   0x55 0xcb 0x16 0x79 0x0d                   U..y.
    body (15)
    hex
    0000   0x1a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x5c 0x00 0x00 0x00 0x00 0x5c 0x36         \....\6
    decimal
             26  144    0  110   23   54    0    0
             92    0    0    0    0   92   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 1.1, 'curve': 4},
 {'age': 76, 'amount': 0.6, 'curve': 4},
 {'age': 86, 'amount': 1.0, 'curve': 4},
 {'age': 206, 'amount': 5.8, 'curve': 4},
 {'age': 180, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x2c 0x1a 0x04 0x18 0x4c 0x04    \.,...L.
    0008   0x28 0x56 0x04 0xe8 0xce 0x04 0x6c 0xb4    (V....l.
    0010   0x14                                       .
    decimal
             92   17   44   26    4   24   76    4
             40   86    4  232  206    4  108  180
             20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-07-25T22:11:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x70 0x00    ..p.p.p.
    decimal
              1    0  112    0  112    0  112    0
    datetime (2013-07-25T22:11:21)
    0000   0x55 0xcb 0x56 0x79 0x0d                   U.Vy.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 CalBGForPH 2013-07-25T23:17:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 248}
```
    op hex (2)
    0000   0x0a 0xf8                                  ..
    decimal
             10  248
    datetime (2013-07-25T23:17:30)
    0000   0x5e 0xd1 0x37 0x79 0x0d                   ^.7y.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 Ian3F 2013-07-25T23:17:30 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1f                                  ?.
    decimal
             63   31
    datetime (2013-07-25T23:17:30)
    0000   0x5e 0xd1 0x17 0x79 0x0d                   ^..y.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 BolusWizard 2013-07-25T23:17:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 138,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 13.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 14.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8a                                  [.
    decimal
             91  138
    datetime (2013-07-25T23:17:46)
    0000   0x6e 0xd1 0x17 0x79 0x0d                   n..y.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x90 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x84 0x00 0x0c 0x36         ......6
    decimal
              0  144    0  110   23   54  144    0
              0    0    0  132    0   12   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 2.8, 'curve': 4},
 {'age': 92, 'amount': 1.1, 'curve': 4},
 {'age': 142, 'amount': 0.6, 'curve': 4},
 {'age': 152, 'amount': 1.0, 'curve': 4},
 {'age': 16, 'amount': 5.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x70 0x48 0x04 0x2c 0x5c 0x04    \.pH.,\.
    0008   0x18 0x8e 0x04 0x28 0x98 0x04 0xe8 0x10    ...(....
    0010   0x14                                       .
    decimal
             92   17  112   72    4   44   92    4
             24  142    4   40  152    4  232   16
             20
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-07-25T23:17:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x0c 0x00 0x0c 0x00 0x84 0x00    ........
    decimal
              1    0   12    0   12    0  132    0
    datetime (2013-07-25T23:17:46)
    0000   0x6e 0xd1 0x57 0x79 0x0d                   n.Wy.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 BolusWizard 2013-07-25T23:22:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 138,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 14.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 14.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8a                                  [.
    decimal
             91  138
    datetime (2013-07-25T23:22:48)
    0000   0x70 0xd6 0x17 0x79 0x0d                   p..y.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x90 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x8c 0x00 0x04 0x36         ......6
    decimal
              0  144    0  110   23   54  144    0
              0    0    0  140    0    4   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 0.3, 'curve': 4},
 {'age': 77, 'amount': 2.8, 'curve': 4},
 {'age': 97, 'amount': 1.1, 'curve': 4},
 {'age': 147, 'amount': 0.6, 'curve': 4},
 {'age': 157, 'amount': 1.0, 'curve': 4},
 {'age': 21, 'amount': 5.8, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x0c 0x07 0x04 0x70 0x4d 0x04    \....pM.
    0008   0x2c 0x61 0x04 0x18 0x93 0x04 0x28 0x9d    ,a....(.
    0010   0x04 0xe8 0x15 0x14                        ....
    decimal
             92   20   12    7    4  112   77    4
             44   97    4   24  147    4   40  157
              4  232   21   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-07-25T23:22:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x04 0x00 0x04 0x00 0x8c 0x00    ........
    decimal
              1    0    4    0    4    0  140    0
    datetime (2013-07-25T23:22:48)
    0000   0x70 0xd6 0x57 0x79 0x0d                   p.Wy.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 BasalProfileStart 2013-07-26T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-26T00:00:00)
    0000   0x40 0xc0 0x00 0x1a 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 34 ResultTotals (2000, 6, 0, 0, 13, 57) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xa1                   .....
    decimal
              7    0    0    7  161
    datetime ((2000, 6, 0, 0, 13, 57))
    0000   0x79 0x8d 0x00 0x00 0x00                   y....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x79 0x8d 0x06 0x00 0xa6 0x41 0xf8    ny....A.
    0008   0x08 0x00 0x00 0x07 0xa1 0x03 0x89 0x2e    ........
    0010   0x04 0x18 0x36 0x00 0xd0 0x01 0x70 0x00    ..6...p.
    0018   0x8c 0x02 0x1c 0x00 0x00 0x06 0x05 0x04    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  121  141    6    0  166   65  248
              8    0    0    7  161    3  137   46
              4   24   54    0  208    1  112    0
            140    2   28    0    0    6    5    4
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 36 BasalProfileStart 2013-07-26T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-26T04:00:00)
    0000   0x40 0xc0 0x04 0x1a 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 0]
#### RECORD 37 CalBGForPH 2013-07-26T08:18:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-07-26T08:18:26)
    0000   0x5a 0xd2 0x28 0x7a 0x0d                   Z.(z.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 Ian3F 2013-07-26T08:18:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-07-26T08:18:26)
    0000   0x5a 0xd2 0x08 0x7a 0x0d                   Z..z.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 CalBGForPH 2013-07-26T08:26:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-07-26T08:26:12)
    0000   0x4c 0xda 0x28 0x7a 0x0d                   L.(z.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 Ian3F 2013-07-26T08:26:12 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-07-26T08:26:12)
    0000   0x4c 0xda 0xe8 0x7a 0x0d                   L..z.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 BolusWizard 2013-07-26T08:26:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 84,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2013-07-26T08:26:29)
    0000   0x5d 0xda 0x08 0x7a 0x0d                   ]..z.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x34 0x00    ...n.64.
    0008   0x24 0x00 0x00 0x00 0x00 0x58 0x36         $....X6
    decimal
             10  144    0  110   23   54   52    0
             36    0    0    0    0   88   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 Ian69 2013-07-26T08:26:29 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-07-26T08:26:29)
    0000   0x5d 0xda 0x08 0x1a 0x0d                   ]....
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x58 0x00 0x58 0x00    ....X.X.
    decimal
             10   30    1    0   88    0   88    0
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-35.data: 43 records`
