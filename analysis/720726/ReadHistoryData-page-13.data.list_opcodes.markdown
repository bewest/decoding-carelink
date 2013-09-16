## START logs/ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 469, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x95 0x37 0x48 0x7a 0x0c 0x7b 0x02 0x80    .7Hz.{..
    0008   0x1e 0x09 0x1a 0x0c 0x13 0x1e 0x00 0x0a    ........
    0010   0x5c 0x92 0x2b 0x2c 0x7a 0x0c 0x3f 0x0b    \.+,z.?.
    0018   0x92 0x2b 0x8c 0x7a 0x0c 0x69 0x69 0x96    .+.z.ii.
##### DEBUG DECIMAL
            149   55   72  122   12  123    2  128
             30    9   26   12   19   30    0   10
             92  146   43   44  122   12   63   11
            146   43  140  122   12  105  105  150
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 1.6, 'curve': 4},
 {'age': 114, 'amount': 0.4, 'curve': 4},
 {'age': 18, 'amount': 1.3, 'curve': 20},
 {'age': 48, 'amount': 2.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x40 0x68 0x04 0x10 0x72 0x04    \.@h..r.
    0008   0x34 0x12 0x14 0x74 0x30 0x14              4..t0.
    decimal
             92   14   64  104    4   16  114    4
             52   18   20  116   48   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-08-25T17:28:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x2c 0x00    ..P.P.,.
    decimal
              1    0   80    0   80    0   44    0
    datetime (2012-08-25T17:28:07)
    0000   0x87 0x1c 0x51 0x79 0x0c                   ..Qy.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2012-08-25T19:43:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-25T19:43:28)
    0000   0x9c 0x2b 0x13 0x79 0x0c                   .+.y.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 2.0, 'curve': 4},
 {'age': 239, 'amount': 1.6, 'curve': 4},
 {'age': 249, 'amount': 0.4, 'curve': 4},
 {'age': 153, 'amount': 1.3, 'curve': 20},
 {'age': 183, 'amount': 2.9, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x8b 0x04 0x40 0xef 0x04    \.P..@..
    0008   0x10 0xf9 0x04 0x34 0x99 0x14 0x74 0xb7    ...4..t.
    0010   0x14                                       .
    decimal
             92   17   80  139    4   64  239    4
             16  249    4   52  153   20  116  183
             20
    datetime (unknown)

    body (0)

#### RECORD 4 Ian69 2012-08-25T19:43:28 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-25T19:43:28)
    0000   0x9c 0x2b 0x73 0x19 0x0c                   .+s..
    body (8)
    hex
    0000   0x15 0x1e 0x01 0x00 0x50 0x00 0x50 0x00    ....P.P.
    decimal
             21   30    1    0   80    0   80    0
    HOUR BITS: [0, 0, 1]
#### RECORD 5 Base (2012, 8, 25, 19, 43, 28) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2012, 8, 25, 19, 43, 28))
    0000   0x9c 0x2b 0x53 0x79 0x0c                   .+Sy.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2012-08-25T19:48:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-25T19:48:43)
    0000   0xab 0x30 0x13 0x79 0x0c                   .0.y.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 1.2, 'curve': 4},
 {'age': 14, 'amount': 0.8, 'curve': 4},
 {'age': 144, 'amount': 2.0, 'curve': 4},
 {'age': 244, 'amount': 1.6, 'curve': 4},
 {'age': 254, 'amount': 0.4, 'curve': 4},
 {'age': 158, 'amount': 1.3, 'curve': 20},
 {'age': 188, 'amount': 2.9, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x30 0x04 0x04 0x20 0x0e 0x04    \.0.. ..
    0008   0x50 0x90 0x04 0x40 0xf4 0x04 0x10 0xfe    P..@....
    0010   0x04 0x34 0x9e 0x14 0x74 0xbc 0x14         .4..t..
    decimal
             92   23   48    4    4   32   14    4
             80  144    4   64  244    4   16  254
              4   52  158   20  116  188   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2012-08-25T19:48:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x6c 0x00    ..0.0.l.
    decimal
              1    0   48    0   48    0  108    0
    datetime (2012-08-25T19:48:43)
    0000   0xab 0x30 0x53 0x79 0x0c                   .0Sy.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 BolusWizard 2012-08-25T20:55:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-25T20:55:39)
    0000   0xa7 0x37 0x14 0x79 0x0c                   .7.y.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 2.4, 'curve': 4},
 {'age': 81, 'amount': 0.8, 'curve': 4},
 {'age': 211, 'amount': 2.0, 'curve': 4},
 {'age': 55, 'amount': 1.6, 'curve': 20},
 {'age': 65, 'amount': 0.4, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x60 0x47 0x04 0x20 0x51 0x04    \.`G. Q.
    0008   0x50 0xd3 0x04 0x40 0x37 0x14 0x10 0x41    P..@7..A
    0010   0x14                                       .
    decimal
             92   17   96   71    4   32   81    4
             80  211    4   64   55   20   16   65
             20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2012-08-25T20:55:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x68 0x00    ..H.H.h.
    decimal
              1    0   72    0   72    0  104    0
    datetime (2012-08-25T20:55:39)
    0000   0xa7 0x37 0x54 0x79 0x0c                   .7Ty.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 BolusWizard 2012-08-25T22:43:52 head[2], body[15] op[0x5b]
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
    datetime (2012-08-25T22:43:52)
    0000   0xb4 0x2b 0x16 0x79 0x0c                   .+.y.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 1.8, 'curve': 4},
 {'age': 179, 'amount': 2.4, 'curve': 4},
 {'age': 189, 'amount': 0.8, 'curve': 4},
 {'age': 63, 'amount': 2.0, 'curve': 20},
 {'age': 163, 'amount': 1.6, 'curve': 20},
 {'age': 173, 'amount': 0.4, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x6d 0x04 0x60 0xb3 0x04    \.Hm.`..
    0008   0x20 0xbd 0x04 0x50 0x3f 0x14 0x40 0xa3     ..P?.@.
    0010   0x14 0x10 0xad 0x14                        ....
    decimal
             92   20   72  109    4   96  179    4
             32  189    4   80   63   20   64  163
             20   16  173   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2012-08-25T22:43:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x3c 0x00    ..X.X.<.
    decimal
              1    0   88    0   88    0   60    0
    datetime (2012-08-25T22:43:52)
    0000   0xb4 0x2b 0x56 0x79 0x0c                   .+Vy.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 15 CalBGForPH 2012-08-25T23:12:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 313}
```
    op hex (2)
    0000   0x0a 0x39                                  .9
    decimal
             10   57
    datetime (2012-08-25T23:12:00)
    0000   0x80 0x0c 0x37 0x79 0x8c                   ..7y.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 Ian3F 2012-08-25T23:12:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x27                                  ?'
    decimal
             63   39
    datetime (2012-08-25T23:12:00)
    0000   0x80 0x0c 0x37 0x79 0x0c                   ..7y.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2012-08-25T23:12:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 12.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 20.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2012-08-25T23:12:13)
    0000   0x8d 0x0c 0x17 0x79 0x0c                   ...y.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xd0 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x7c 0x00 0x54 0x36         ...|.T6
    decimal
              0  144    0  110   23   54  208    0
              0    0    0  124    0   84   54
    DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 2.0, 'curve': 4},
 {'age': 38, 'amount': 0.2, 'curve': 4},
 {'age': 138, 'amount': 1.8, 'curve': 4},
 {'age': 208, 'amount': 2.4, 'curve': 4},
 {'age': 218, 'amount': 0.8, 'curve': 4},
 {'age': 92, 'amount': 2.0, 'curve': 20},
 {'age': 192, 'amount': 1.6, 'curve': 20},
 {'age': 202, 'amount': 0.4, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x50 0x1c 0x04 0x08 0x26 0x04    \.P...&.
    0008   0x48 0x8a 0x04 0x60 0xd0 0x04 0x20 0xda    H..`.. .
    0010   0x04 0x50 0x5c 0x14 0x40 0xc0 0x14 0x10    .P\.@...
    0018   0xca 0x14                                  ..
    decimal
             92   26   80   28    4    8   38    4
             72  138    4   96  208    4   32  218
              4   80   92   20   64  192   20   16
            202   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2012-08-25T23:12:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x7c 0x00    ..h.h.|.
    decimal
              1    0  104    0  104    0  124    0
    datetime (2012-08-25T23:12:14)
    0000   0x8e 0x0c 0x57 0x79 0x0c                   ..Wy.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 20 BasalProfileStart 2012-08-26T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-26T00:00:00)
    0000   0x80 0x00 0x00 0x1a 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 21 ResultTotals (2000, 8, 0, 0, 12, 25) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xb6                   .....
    decimal
              7    0    0    6  182
    datetime ((2000, 8, 0, 0, 12, 25))
    0000   0x99 0x0c 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 22 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x99 0x0c 0x06 0x10 0xa2 0x68 0x39    n.....h9
    0008   0x05 0x00 0x00 0x06 0xb6 0x03 0x86 0x35    .......5
    0010   0x03 0x30 0x2f 0x00 0xbd 0x02 0x78 0x00    .0/...x.
    0018   0x68 0x00 0x50 0x00 0x00 0x08 0x01 0x01    h.P.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x65 0x65 0x00 0x00 0x00         ..ee...
    decimal
            110  153   12    6   16  162  104   57
              5    0    0    6  182    3  134   53
              3   48   47    0  189    2  120    0
            104    0   80    0    0    8    1    1
              0    0    0    0    0    0    0    0
              0    0  101  101    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 23 BasalProfileStart 2012-08-26T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-26T04:00:00)
    0000   0x80 0x00 0x04 0x1a 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 24 CalBGForPH 2012-08-26T08:18:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 48}
```
    op hex (2)
    0000   0x0a 0x30                                  .0
    decimal
             10   48
    datetime (2012-08-26T08:18:02)
    0000   0x82 0x12 0x28 0x7a 0x0c                   ..(z.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 25 Ian3F 2012-08-26T08:18:02 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2012-08-26T08:18:02)
    0000   0x82 0x12 0x08 0x7a 0x0c                   ...z.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2012-08-26T08:55:21 head[2], body[15] op[0x5b]
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
    datetime (2012-08-26T08:55:21)
    0000   0x95 0x37 0x08 0x7a 0x0c                   .7.z.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 27 Ian69 2012-08-26T08:55:21 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-26T08:55:21)
    0000   0x95 0x37 0x08 0x1a 0x0c                   .7...
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x78 0x00 0x78 0x00    ....x.x.
    decimal
             10   30    1    0  120    0  120    0
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-13.data: 28 records`
