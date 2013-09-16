## START logs/ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 1012, found 10 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xca 0x79                                  .y
##### DEBUG DECIMAL
            202  121
#### RECORD 0 Ian69 2013-09-09T11:10:57 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-09T11:10:57)
    0000   0xb9 0x4a 0x0b 0x09 0x0d                   .J...
    body (8)
    hex
    0000   0x0e 0x1e 0x01 0x00 0x34 0x00 0x34 0x00    ....4.4.
    decimal
             14   30    1    0   52    0   52    0
    HOUR BITS: [0, 1, 0]
#### RECORD 1 Base (2013, 9, 9, 11, 10, 57) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2013, 9, 9, 11, 10, 57))
    0000   0xb9 0x4a 0x4b 0x69 0x0d                   .JKi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-09-09T11:15:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-09-09T11:15:34)
    0000   0xa2 0x4f 0x4b 0x09 0x0d                   .OK..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 BolusWizard 2013-09-09T11:15:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 88,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.8,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-09-09T11:15:53)
    0000   0xb5 0x4f 0x0b 0x69 0x0d                   .O.i.
    body (15)
    hex
    0000   0x11 0x90 0x00 0x6e 0x17 0x36 0x38 0x00    ...n.68.
    0008   0x3c 0x00 0x00 0x44 0x00 0x3c 0x36         <..D.<6
    decimal
             17  144    0  110   23   54   56    0
             60    0    0   68    0   60   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 1.3, 'curve': 4},
 {'age': 207, 'amount': 1.0, 'curve': 4},
 {'age': 217, 'amount': 3.0, 'curve': 4},
 {'age': 181, 'amount': 2.7, 'curve': 21},
 {'age': 191, 'amount': 0.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x34 0x07 0x04 0x28 0xcf 0x04    \.4..(..
    0008   0x78 0xd9 0x04 0x6c 0xb5 0x15 0x0c 0xbf    x..l....
    0010   0x14                                       .
    decimal
             92   17   52    7    4   40  207    4
            120  217    4  108  181   21   12  191
             20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-09-09T11:15:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x44 0x00    ..X.X.D.
    decimal
              1    0   88    0   88    0   68    0
    datetime (2013-09-09T11:15:53)
    0000   0xb5 0x4f 0x4b 0x69 0x0d                   .OKi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2013-09-09T11:29:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-09-09T11:29:28)
    0000   0x9c 0x5d 0x4b 0x09 0x0d                   .]K..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 BolusWizard 2013-09-09T11:29:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 14.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 9.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-09-09T11:29:35)
    0000   0xa3 0x5d 0x0b 0x69 0x0d                   .].i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x5c 0x00    ...n.6\.
    0008   0x00 0x00 0x00 0x94 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54   92    0
              0    0    0  148    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 3.5, 'curve': 4},
 {'age': 221, 'amount': 1.0, 'curve': 4},
 {'age': 231, 'amount': 3.0, 'curve': 4},
 {'age': 195, 'amount': 2.7, 'curve': 21},
 {'age': 205, 'amount': 0.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x8c 0x15 0x04 0x28 0xdd 0x04    \....(..
    0008   0x78 0xe7 0x04 0x6c 0xc3 0x15 0x0c 0xcd    x..l....
    0010   0x14                                       .
    decimal
             92   17  140   21    4   40  221    4
            120  231    4  108  195   21   12  205
             20
    datetime (unknown)

    body (0)

#### RECORD 9 Ian0B 2013-09-09T11:34:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2013-09-09T11:34:07)
    0000   0x87 0x62 0x4b 0xa9 0x0d                   .bK..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 10 Ian0B 2013-09-09T11:34:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2013-09-09T11:34:07)
    0000   0x87 0x62 0x4b 0xa9 0x0d                   .bK..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 11 CalBGForPH 2013-09-09T11:36:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-09-09T11:36:03)
    0000   0x83 0x64 0x2b 0x69 0x0d                   .d+i.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2013-09-09T11:36:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-09-09T11:36:03)
    0000   0x83 0x64 0x4b 0x69 0x0d                   .dKi.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 Ian0B 2013-09-09T11:47:41 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x6c 0x00                             .l.
    decimal
             11  108    0
    datetime (2013-09-09T11:47:41)
    0000   0xa9 0x6f 0x4b 0xa9 0x0d                   .oK..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 14 Ian0B 2013-09-09T11:47:41 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2013-09-09T11:47:41)
    0000   0xa9 0x6f 0x4b 0xa9 0x0d                   .oK..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 15 CalBGForPH 2013-09-09T11:49:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2013-09-09T11:49:29)
    0000   0x9d 0x71 0x2b 0x69 0x0d                   .q+i.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 Ian3F 2013-09-09T11:49:29 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2013-09-09T11:49:29)
    0000   0x9d 0x71 0xeb 0x69 0x0d                   .q.i.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2013-09-09T12:08:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T12:08:42)
    0000   0xaa 0x48 0x0c 0x69 0x0d                   .H.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 3.5, 'curve': 4},
 {'age': 4, 'amount': 1.0, 'curve': 20},
 {'age': 14, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x8c 0x3c 0x04 0x28 0x04 0x14    \..<.(..
    0008   0x78 0x0e 0x14                             x..
    decimal
             92   11  140   60    4   40    4   20
            120   14   20
    datetime (unknown)

    body (0)

#### RECORD 19 BolusWizard 2013-09-09T12:08:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T12:08:45)
    0000   0xad 0x48 0x0c 0x69 0x0d                   .H.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 3.5, 'curve': 4},
 {'age': 4, 'amount': 1.0, 'curve': 20},
 {'age': 14, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x8c 0x3c 0x04 0x28 0x04 0x14    \..<.(..
    0008   0x78 0x0e 0x14                             x..
    decimal
             92   11  140   60    4   40    4   20
            120   14   20
    datetime (unknown)

    body (0)

#### RECORD 21 BolusWizard 2013-09-09T12:08:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T12:08:53)
    0000   0xb5 0x48 0x0c 0x69 0x0d                   .H.i.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 3.5, 'curve': 4},
 {'age': 4, 'amount': 1.0, 'curve': 20},
 {'age': 14, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x8c 0x3c 0x04 0x28 0x04 0x14    \..<.(..
    0008   0x78 0x0e 0x14                             x..
    decimal
             92   11  140   60    4   40    4   20
            120   14   20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-09-09T12:08:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x74 0x00    ..X.X.t.
    decimal
              1    0   88    0   88    0  116    0
    datetime (2013-09-09T12:08:53)
    0000   0xb5 0x48 0x4c 0x69 0x0d                   .HLi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 24 BolusWizard 2013-09-09T12:20:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T12:20:30)
    0000   0x9e 0x54 0x0c 0x69 0x0d                   .T.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 2.2, 'curve': 4},
 {'age': 72, 'amount': 3.5, 'curve': 4},
 {'age': 16, 'amount': 1.0, 'curve': 20},
 {'age': 26, 'amount': 3.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x58 0x0c 0x04 0x8c 0x48 0x04    \.X...H.
    0008   0x28 0x10 0x14 0x78 0x1a 0x14              (..x..
    decimal
             92   14   88   12    4  140   72    4
             40   16   20  120   26   20
    datetime (unknown)

    body (0)

#### RECORD 26 BolusWizard 2013-09-09T12:20:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T12:20:41)
    0000   0xa9 0x54 0x0c 0x69 0x0d                   .T.i.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 2.2, 'curve': 4},
 {'age': 72, 'amount': 3.5, 'curve': 4},
 {'age': 16, 'amount': 1.0, 'curve': 20},
 {'age': 26, 'amount': 3.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x58 0x0c 0x04 0x8c 0x48 0x04    \.X...H.
    0008   0x28 0x10 0x14 0x78 0x1a 0x14              (..x..
    decimal
             92   14   88   12    4  140   72    4
             40   16   20  120   26   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-09-09T12:20:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0xc4 0x00    ..4.4...
    decimal
              1    0   52    0   52    0  196    0
    datetime (2013-09-09T12:20:42)
    0000   0xaa 0x54 0x4c 0x69 0x0d                   .TLi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 BolusWizard 2013-09-09T12:43:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T12:43:44)
    0000   0xac 0x6b 0x0c 0x69 0x0d                   .k.i.
    body (15)
    hex
    0000   0x11 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x3c 0x00 0x00 0x00 0x00 0x3c 0x36         <....<6
    decimal
             17  144    0  110   23   54    0    0
             60    0    0    0    0   60   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 1.3, 'curve': 4},
 {'age': 35, 'amount': 2.2, 'curve': 4},
 {'age': 95, 'amount': 3.5, 'curve': 4},
 {'age': 39, 'amount': 1.0, 'curve': 20},
 {'age': 49, 'amount': 3.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x34 0x19 0x04 0x58 0x23 0x04    \.4..X#.
    0008   0x8c 0x5f 0x04 0x28 0x27 0x14 0x78 0x31    ._.('.x1
    0010   0x14                                       .
    decimal
             92   17   52   25    4   88   35    4
            140   95    4   40   39   20  120   49
             20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-09-09T12:43:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xdc 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  220    0
    datetime (2013-09-09T12:43:44)
    0000   0xac 0x6b 0x4c 0x69 0x0d                   .kLi.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 BasalProfileStart 2013-09-09T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-09T13:00:00)
    0000   0x80 0x40 0x0d 0x09 0x0d                   .@...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 33 BolusWizard 2013-09-09T13:30:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T13:30:07)
    0000   0x87 0x5e 0x0d 0x69 0x0d                   .^.i.
    body (15)
    hex
    0000   0x0c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x36         (....(6
    decimal
             12  144    0  110   23   54    0    0
             40    0    0    0    0   40   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 1.5, 'curve': 4},
 {'age': 72, 'amount': 1.3, 'curve': 4},
 {'age': 82, 'amount': 2.2, 'curve': 4},
 {'age': 142, 'amount': 3.5, 'curve': 4},
 {'age': 86, 'amount': 1.0, 'curve': 20},
 {'age': 96, 'amount': 3.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x3c 0x34 0x04 0x34 0x48 0x04    \.<4.4H.
    0008   0x58 0x52 0x04 0x8c 0x8e 0x04 0x28 0x56    XR....(V
    0010   0x14 0x78 0x60 0x14                        .x`.
    decimal
             92   20   60   52    4   52   72    4
             88   82    4  140  142    4   40   86
             20  120   96   20
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-09-09T13:30:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xc8 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  200    0
    datetime (2013-09-09T13:30:07)
    0000   0x87 0x5e 0x4d 0x69 0x0d                   .^Mi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 Ian0B 2013-09-09T14:01:36 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2013-09-09T14:01:36)
    0000   0xa4 0x41 0x4e 0xa9 0x0d                   .AN..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 37 CalBGForPH 2013-09-09T14:02:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 60}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2013-09-09T14:02:50)
    0000   0xb2 0x42 0x4e 0x09 0x0d                   .BN..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 CalBGForPH 2013-09-09T16:08:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-09-09T16:08:57)
    0000   0xb9 0x48 0x50 0x09 0x0d                   .HP..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 CalBGForPH 2013-09-09T16:09:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2013-09-09T16:09:56)
    0000   0xb8 0x49 0x50 0x09 0x0d                   .IP..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 40 BolusWizard 2013-09-09T16:10:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 166,
 'bg_target_high': 1,
 'bg_target_low': 23,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 19.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0xa6                                  [.
    decimal
             91  166
    datetime (2013-09-09T16:10:04)
    0000   0x84 0x4a 0x10 0x69 0x0d                   .J.i.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0xc0 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x14 0x01 0x0c 0x36         `.....6
    decimal
             27  144    0  110   23   54  192    0
             96    0    0   20    1   12   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 1.0, 'curve': 4},
 {'age': 212, 'amount': 1.5, 'curve': 4},
 {'age': 232, 'amount': 1.3, 'curve': 4},
 {'age': 242, 'amount': 2.2, 'curve': 4},
 {'age': 46, 'amount': 3.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0xa2 0x04 0x3c 0xd4 0x04    \.(..<..
    0008   0x34 0xe8 0x04 0x58 0xf2 0x04 0x8c 0x2e    4..X....
    0010   0x14                                       .
    decimal
             92   17   40  162    4   60  212    4
             52  232    4   88  242    4  140   46
             20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-09-09T16:10:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x0c 0x01 0x0c 0x00 0x14 0x00    ........
    decimal
              1    1   12    1   12    0   20    0
    datetime (2013-09-09T16:10:04)
    0000   0x84 0x4a 0x50 0x69 0x0d                   .JPi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 43 BolusWizard 2013-09-09T16:44:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T16:44:50)
    0000   0xb2 0x6c 0x10 0x69 0x0d                   .l.i.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 0.3, 'curve': 5},
 {'age': 196, 'amount': 1.0, 'curve': 4},
 {'age': 246, 'amount': 1.5, 'curve': 4},
 {'age': 10, 'amount': 1.3, 'curve': 20},
 {'age': 20, 'amount': 2.2, 'curve': 20},
 {'age': 80, 'amount': 3.5, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x0c 0x24 0x05 0x28 0xc4 0x04    \..$.(..
    0008   0x3c 0xf6 0x04 0x34 0x0a 0x14 0x58 0x14    <..4..X.
    0010   0x14 0x8c 0x50 0x14                        ..P.
    decimal
             92   20   12   36    5   40  196    4
             60  246    4   52   10   20   88   20
             20  140   80   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-09-09T16:44:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x01 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    1    0    0
    datetime (2013-09-09T16:44:50)
    0000   0xb2 0x6c 0x50 0x69 0x0d                   .lPi.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 CalBGForPH 2013-09-09T17:33:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 225}
```
    op hex (2)
    0000   0x0a 0xe1                                  ..
    decimal
             10  225
    datetime (2013-09-09T17:33:49)
    0000   0xb1 0x61 0x31 0x69 0x0d                   .a1i.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 Ian3F 2013-09-09T17:33:49 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1c                                  ?.
    decimal
             63   28
    datetime (2013-09-09T17:33:49)
    0000   0xb1 0x61 0x31 0x69 0x0d                   .a1i.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2013-09-09T17:33:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 125,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 22.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 12.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7d                                  [}
    decimal
             91  125
    datetime (2013-09-09T17:33:58)
    0000   0xba 0x61 0x11 0x69 0x0d                   .a.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x78 0x00    ...n.6x.
    0008   0x00 0x00 0x00 0xe4 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54  120    0
              0    0    0  228    0    0   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 1.3, 'curve': 4},
 {'age': 85, 'amount': 0.3, 'curve': 5},
 {'age': 245, 'amount': 1.0, 'curve': 4},
 {'age': 39, 'amount': 1.5, 'curve': 20},
 {'age': 59, 'amount': 1.3, 'curve': 20},
 {'age': 69, 'amount': 2.2, 'curve': 20},
 {'age': 129, 'amount': 3.5, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x34 0x37 0x04 0x0c 0x55 0x05    \.47..U.
    0008   0x28 0xf5 0x04 0x3c 0x27 0x14 0x34 0x3b    (..<'.4;
    0010   0x14 0x58 0x45 0x14 0x8c 0x81 0x14         .XE....
    decimal
             92   23   52   55    4   12   85    5
             40  245    4   60   39   20   52   59
             20   88   69   20  140  129   20
    datetime (unknown)

    body (0)

#### RECORD 50 BolusWizard 2013-09-09T18:18:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T18:18:42)
    0000   0xaa 0x52 0x12 0x69 0x0d                   .R.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 1.3, 'curve': 4},
 {'age': 130, 'amount': 0.3, 'curve': 5},
 {'age': 34, 'amount': 1.0, 'curve': 20},
 {'age': 84, 'amount': 1.5, 'curve': 20},
 {'age': 104, 'amount': 1.3, 'curve': 20},
 {'age': 114, 'amount': 2.2, 'curve': 20},
 {'age': 174, 'amount': 3.5, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x34 0x64 0x04 0x0c 0x82 0x05    \.4d....
    0008   0x28 0x22 0x14 0x3c 0x54 0x14 0x34 0x68    (".<T.4h
    0010   0x14 0x58 0x72 0x14 0x8c 0xae 0x14         .Xr....
    decimal
             92   23   52  100    4   12  130    5
             40   34   20   60   84   20   52  104
             20   88  114   20  140  174   20
    datetime (unknown)

    body (0)

#### RECORD 52 BolusWizard 2013-09-09T18:18:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T18:18:44)
    0000   0xac 0x52 0x12 0x69 0x0d                   .R.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 1.3, 'curve': 4},
 {'age': 130, 'amount': 0.3, 'curve': 5},
 {'age': 34, 'amount': 1.0, 'curve': 20},
 {'age': 84, 'amount': 1.5, 'curve': 20},
 {'age': 104, 'amount': 1.3, 'curve': 20},
 {'age': 114, 'amount': 2.2, 'curve': 20},
 {'age': 174, 'amount': 3.5, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x34 0x64 0x04 0x0c 0x82 0x05    \.4d....
    0008   0x28 0x22 0x14 0x3c 0x54 0x14 0x34 0x68    (".<T.4h
    0010   0x14 0x58 0x72 0x14 0x8c 0xae 0x14         .Xr....
    decimal
             92   23   52  100    4   12  130    5
             40   34   20   60   84   20   52  104
             20   88  114   20  140  174   20
    datetime (unknown)

    body (0)

#### RECORD 54 BolusWizard 2013-09-09T18:18:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-09T18:18:56)
    0000   0xb8 0x52 0x12 0x69 0x0d                   .R.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 1.3, 'curve': 4},
 {'age': 130, 'amount': 0.3, 'curve': 5},
 {'age': 34, 'amount': 1.0, 'curve': 20},
 {'age': 84, 'amount': 1.5, 'curve': 20},
 {'age': 104, 'amount': 1.3, 'curve': 20},
 {'age': 114, 'amount': 2.2, 'curve': 20},
 {'age': 174, 'amount': 3.5, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x34 0x64 0x04 0x0c 0x82 0x05    \.4d....
    0008   0x28 0x22 0x14 0x3c 0x54 0x14 0x34 0x68    (".<T.4h
    0010   0x14 0x58 0x72 0x14 0x8c 0xae 0x14         .Xr....
    decimal
             92   23   52  100    4   12  130    5
             40   34   20   60   84   20   52  104
             20   88  114   20  140  174   20
    datetime (unknown)

    body (0)

#### RECORD 56 Ian69 2013-09-09T18:18:56 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-09T18:18:56)
    0000   0xb8 0x52 0x72 0x09 0x0d                   .Rr..
    body (8)
    hex
    0000   0x15 0x1e 0x01 0x00 0x78 0x00 0x78 0x00    ....x.x.
    decimal
             21   30    1    0  120    0  120    0
    HOUR BITS: [0, 1, 0]
#### RECORD 57 Base (2013, 9, 9, 18, 18, 56) head[2], body[0] op[0x8c]

    op hex (2)
    0000   0x8c 0x00                                  ..
    decimal
            140    0
    datetime ((2013, 9, 9, 18, 18, 56))
    0000   0xb8 0x52 0x52 0x69 0x0d                   .RRi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 58 CalBGForPH 2013-09-09T18:29:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-09-09T18:29:20)
    0000   0x94 0x5d 0x52 0x09 0x0d                   .]R..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 59 BolusWizard 2013-09-09T18:29:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 24.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 10.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-09-09T18:29:31)
    0000   0x9f 0x5d 0x12 0x69 0x0d                   .].i.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x64 0x00    ...n.6d.
    0008   0x34 0x00 0x00 0xf0 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54  100    0
             52    0    0  240    0   52   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 3.0, 'curve': 4},
 {'age': 111, 'amount': 1.3, 'curve': 4},
 {'age': 141, 'amount': 0.3, 'curve': 5},
 {'age': 45, 'amount': 1.0, 'curve': 20},
 {'age': 95, 'amount': 1.5, 'curve': 20},
 {'age': 115, 'amount': 1.3, 'curve': 20},
 {'age': 125, 'amount': 2.2, 'curve': 20},
 {'age': 185, 'amount': 3.5, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x78 0x0b 0x04 0x34 0x6f 0x04    \.x..4o.
    0008   0x0c 0x8d 0x05 0x28 0x2d 0x14 0x3c 0x5f    ...(-.<_
    0010   0x14 0x34 0x73 0x14 0x58 0x7d 0x14 0x8c    .4s.X}..
    0018   0xb9 0x14                                  ..
    decimal
             92   26  120   11    4   52  111    4
             12  141    5   40   45   20   60   95
             20   52  115   20   88  125   20  140
            185   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-09-09T18:29:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0xf0 0x00    ..H.H...
    decimal
              1    0   72    0   72    0  240    0
    datetime (2013-09-09T18:29:31)
    0000   0x9f 0x5d 0x52 0x69 0x0d                   .]Ri.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 CalBGForPH 2013-09-09T19:02:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2013-09-09T19:02:25)
    0000   0x99 0x42 0x53 0x09 0x0d                   .BS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 63 BolusWizard 2013-09-09T19:02:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 84,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 24.4,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2013-09-09T19:02:36)
    0000   0xa4 0x42 0x13 0x69 0x0d                   .B.i.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x34 0x00    (..n.64.
    0008   0x90 0x00 0x00 0xf4 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54   52    0
            144    0    0  244    0  144   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 1.8, 'curve': 4},
 {'age': 44, 'amount': 3.0, 'curve': 4},
 {'age': 144, 'amount': 1.3, 'curve': 4},
 {'age': 174, 'amount': 0.3, 'curve': 5},
 {'age': 78, 'amount': 1.0, 'curve': 20},
 {'age': 128, 'amount': 1.5, 'curve': 20},
 {'age': 148, 'amount': 1.3, 'curve': 20},
 {'age': 158, 'amount': 2.2, 'curve': 20},
 {'age': 218, 'amount': 3.5, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x48 0x22 0x04 0x78 0x2c 0x04    \.H".x,.
    0008   0x34 0x90 0x04 0x0c 0xae 0x05 0x28 0x4e    4.....(N
    0010   0x14 0x3c 0x80 0x14 0x34 0x94 0x14 0x58    .<..4..X
    0018   0x9e 0x14 0x8c 0xda 0x14                   .....
    decimal
             92   29   72   34    4  120   44    4
             52  144    4   12  174    5   40   78
             20   60  128   20   52  148   20   88
            158   20  140  218   20
    datetime (unknown)

    body (0)

#### RECORD 65 BolusWizard 2013-09-09T19:02:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 84,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 24.4,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2013-09-09T19:02:43)
    0000   0xab 0x42 0x13 0x69 0x0d                   .B.i.
    body (15)
    hex
    0000   0x1a 0x90 0x00 0x6e 0x17 0x36 0x34 0x00    ...n.64.
    0008   0x5c 0x00 0x00 0xf4 0x00 0x5c 0x36         \....\6
    decimal
             26  144    0  110   23   54   52    0
             92    0    0  244    0   92   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-2.data: 66 records`
