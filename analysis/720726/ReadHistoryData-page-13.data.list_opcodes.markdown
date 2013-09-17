## START logs/ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 1013, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x34 0xbb                                  4.
##### DEBUG DECIMAL
             52  187
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

#### RECORD 4 Ian69 2012-08-25T19:43:28 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-25T19:43:28)
    0000   0x9c 0x2b 0x73 0x19 0x0c                   .+s..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 5 Bolus 2012-08-25T19:43:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x20 0x00    ..P.P. .
    decimal
              1    0   80    0   80    0   32    0
    datetime (2012-08-25T19:43:28)
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
#### RECORD 27 Ian69 2012-08-26T08:55:21 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-26T08:55:21)
    0000   0x95 0x37 0x08 0x1a 0x0c                   .7...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 0, 1]
#### RECORD 28 Bolus 2012-08-26T08:55:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    0    0
    datetime (2012-08-26T08:55:21)
    0000   0x95 0x37 0x48 0x7a 0x0c                   .7Hz.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 29 BasalProfileStart 2012-08-26T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-26T09:30:00)
    0000   0x80 0x1e 0x09 0x1a 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 30 CalBGForPH 2012-08-26T12:43:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2012-08-26T12:43:18)
    0000   0x92 0x2b 0x2c 0x7a 0x0c                   .+,z.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 Ian3F 2012-08-26T12:43:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2012-08-26T12:43:18)
    0000   0x92 0x2b 0x8c 0x7a 0x0c                   .+.z.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 BasalProfileStart 2012-08-26T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-26T13:00:00)
    0000   0x80 0x00 0x0d 0x1a 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 33 BolusWizard 2012-08-26T14:28:47 head[2], body[15] op[0x5b]
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
    datetime (2012-08-26T14:28:47)
    0000   0xaf 0x1c 0x0e 0x7a 0x0c                   ...z.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 78, 'amount': 3.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x4e 0x14                   \.xN.
    decimal
             92    5  120   78   20
    datetime (unknown)

    body (0)

#### RECORD 35 Ian69 2012-08-26T14:28:48 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-26T14:28:48)
    0000   0xb0 0x1c 0x0e 0x1a 0x0c                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 36 Bolus 2012-08-26T14:28:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2012-08-26T14:28:48)
    0000   0xb0 0x1c 0x4e 0x7a 0x0c                   ..Nz.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 37 BolusWizard 2012-08-26T14:41:56 head[2], body[15] op[0x5b]
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
    datetime (2012-08-26T14:41:56)
    0000   0xb8 0x29 0x0e 0x7a 0x0c                   .).z.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 2.7, 'curve': 4},
 {'age': 91, 'amount': 3.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x11 0x04 0x78 0x5b 0x14    \.l..x[.
    decimal
             92    8  108   17    4  120   91   20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2012-08-26T14:41:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x6c 0x00    ..H.H.l.
    decimal
              1    0   72    0   72    0  108    0
    datetime (2012-08-26T14:41:56)
    0000   0xb8 0x29 0x4e 0x7a 0x0c                   .)Nz.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 CalBGForPH 2012-08-26T15:20:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2012-08-26T15:20:44)
    0000   0xac 0x14 0x2f 0x7a 0x0c                   ../z.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2012-08-26T15:20:44 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2012-08-26T15:20:44)
    0000   0xac 0x14 0x8f 0x7a 0x0c                   ...z.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 42 BolusWizard 2012-08-26T15:23:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 78,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 15.2,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 4.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x4e                                  [N
    decimal
             91   78
    datetime (2012-08-26T15:23:53)
    0000   0xb5 0x17 0x0f 0x7a 0x0c                   ...z.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x28 0x00    ...n.6(.
    0008   0x60 0x00 0x00 0x98 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54   40    0
             96    0    0  152    0   96   54
    DAY BITS: [0, 1, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 1.8, 'curve': 4},
 {'age': 59, 'amount': 2.7, 'curve': 4},
 {'age': 133, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x31 0x04 0x6c 0x3b 0x04    \.H1.l;.
    0008   0x78 0x85 0x14                             x..
    decimal
             92   11   72   49    4  108   59    4
            120  133   20
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2012-08-26T15:23:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x98 0x00    ..p.p...
    decimal
              1    0  112    0  112    0  152    0
    datetime (2012-08-26T15:23:53)
    0000   0xb5 0x17 0x4f 0x7a 0x0c                   ..Oz.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 45 CalBGForPH 2012-08-26T18:45:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2012-08-26T18:45:06)
    0000   0x86 0x2d 0x32 0x7a 0x0c                   .-2z.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 Ian3F 2012-08-26T18:45:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2012-08-26T18:45:06)
    0000   0x86 0x2d 0xf2 0x7a 0x0c                   .-.z.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2012-08-26T18:45:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.6,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2012-08-26T18:45:15)
    0000   0x8f 0x2d 0x12 0x7a 0x0c                   .-.z.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    ...n.6$.
    0008   0x48 0x00 0x00 0x10 0x00 0x5c 0x36         H....\6
    decimal
             20  144    0  110   23   54   36    0
             72    0    0   16    0   92   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 201, 'amount': 2.6, 'curve': 4},
 {'age': 211, 'amount': 0.2, 'curve': 4},
 {'age': 251, 'amount': 1.8, 'curve': 4},
 {'age': 5, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0xc9 0x04 0x08 0xd3 0x04    \.h.....
    0008   0x48 0xfb 0x04 0x6c 0x05 0x14              H..l..
    decimal
             92   14  104  201    4    8  211    4
             72  251    4  108    5   20
    datetime (unknown)

    body (0)

#### RECORD 49 Ian69 2012-08-26T18:45:15 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-26T18:45:15)
    0000   0x8f 0x2d 0x72 0x1a 0x0c                   .-r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 50 Bolus 2012-08-26T18:45:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x10 0x00    ..\.\...
    decimal
              1    0   92    0   92    0   16    0
    datetime (2012-08-26T18:45:15)
    0000   0x8f 0x2d 0x52 0x7a 0x0c                   .-Rz.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 BolusWizard 2012-08-26T19:33:06 head[2], body[15] op[0x5b]
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
    datetime (2012-08-26T19:33:06)
    0000   0x86 0x21 0x13 0x7a 0x0c                   .!.z.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 2.3, 'curve': 4},
 {'age': 249, 'amount': 2.6, 'curve': 4},
 {'age': 3, 'amount': 0.2, 'curve': 20},
 {'age': 43, 'amount': 1.8, 'curve': 20},
 {'age': 53, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x5c 0x31 0x04 0x68 0xf9 0x04    \.\1.h..
    0008   0x08 0x03 0x14 0x48 0x2b 0x14 0x6c 0x35    ...H+.l5
    0010   0x14                                       .
    decimal
             92   17   92   49    4  104  249    4
              8    3   20   72   43   20  108   53
             20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2012-08-26T19:33:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x54 0x00    ..4.4.T.
    decimal
              1    0   52    0   52    0   84    0
    datetime (2012-08-26T19:33:06)
    0000   0x86 0x21 0x53 0x7a 0x0c                   .!Sz.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 BolusWizard 2012-08-26T21:56:25 head[2], body[15] op[0x5b]
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
    datetime (2012-08-26T21:56:25)
    0000   0x99 0x38 0x15 0x7a 0x0c                   .8.z.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 1.3, 'curve': 4},
 {'age': 192, 'amount': 2.3, 'curve': 4},
 {'age': 136, 'amount': 2.6, 'curve': 20},
 {'age': 146, 'amount': 0.2, 'curve': 20},
 {'age': 186, 'amount': 1.8, 'curve': 20},
 {'age': 196, 'amount': 2.7, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x34 0x98 0x04 0x5c 0xc0 0x04    \.4..\..
    0008   0x68 0x88 0x14 0x08 0x92 0x14 0x48 0xba    h.....H.
    0010   0x14 0x6c 0xc4 0x14                        .l..
    decimal
             92   20   52  152    4   92  192    4
            104  136   20    8  146   20   72  186
             20  108  196   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2012-08-26T21:56:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x1c 0x00    ..H.H...
    decimal
              1    0   72    0   72    0   28    0
    datetime (2012-08-26T21:56:25)
    0000   0x99 0x38 0x55 0x7a 0x0c                   .8Uz.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2012-08-26T22:28:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 47,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 168}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-26T22:28:17)
    0000   0x91 0x1c 0x16 0x7a 0x0c                   ...z.
    body (15)
    hex
    0000   0x2f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    /..n.6..
    0008   0xa8 0x00 0x00 0x00 0x00 0xa8 0x36         ......6
    decimal
             47  144    0  110   23   54    0    0
            168    0    0    0    0  168   54
    DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 1.8, 'curve': 4},
 {'age': 184, 'amount': 1.3, 'curve': 4},
 {'age': 224, 'amount': 2.3, 'curve': 4},
 {'age': 168, 'amount': 2.6, 'curve': 20},
 {'age': 178, 'amount': 0.2, 'curve': 20},
 {'age': 218, 'amount': 1.8, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x22 0x04 0x34 0xb8 0x04    \.H".4..
    0008   0x5c 0xe0 0x04 0x68 0xa8 0x14 0x08 0xb2    \..h....
    0010   0x14 0x48 0xda 0x14                        .H..
    decimal
             92   20   72   34    4   52  184    4
             92  224    4  104  168   20    8  178
             20   72  218   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2012-08-26T22:28:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x54 0x00    ......T.
    decimal
              1    0  168    0  168    0   84    0
    datetime (2012-08-26T22:28:17)
    0000   0x91 0x1c 0x56 0x7a 0x0c                   ..Vz.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 60 BasalProfileStart 2012-08-27T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-27T00:00:00)
    0000   0x80 0x00 0x00 0x1b 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 61 ResultTotals (2000, 8, 0, 0, 12, 26) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xa5                   .....
    decimal
              7    0    0    6  165
    datetime ((2000, 8, 0, 0, 12, 26))
    0000   0x9a 0x0c 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 62 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x9a 0x0c 0x06 0x00 0x68 0x30 0x8c    n....h0.
    0008   0x04 0x00 0x00 0x06 0xa5 0x03 0x89 0x35    .......5
    0010   0x03 0x1c 0x2f 0x00 0xd1 0x02 0x48 0x00    ../...H.
    0018   0x00 0x00 0xd4 0x00 0x00 0x06 0x00 0x02    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  154   12    6    0  104   48  140
              4    0    0    6  165    3  137   53
              3   28   47    0  209    2   72    0
              0    0  212    0    0    6    0    2
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 63 BolusWizard 2012-08-27T00:37:56 head[2], body[15] op[0x5b]
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
    datetime (2012-08-27T00:37:56)
    0000   0xb8 0x25 0x00 0x7b 0x0c                   .%.{.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 133, 'amount': 4.2, 'curve': 4},
 {'age': 163, 'amount': 1.8, 'curve': 4},
 {'age': 57, 'amount': 1.3, 'curve': 20},
 {'age': 97, 'amount': 2.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xa8 0x85 0x04 0x48 0xa3 0x04    \....H..
    0008   0x34 0x39 0x14 0x5c 0x61 0x14              49.\a.
    decimal
             92   14  168  133    4   72  163    4
             52   57   20   92   97   20
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-13.data: 65 records`
