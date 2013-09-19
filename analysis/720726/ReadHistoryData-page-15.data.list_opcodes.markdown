## START analysis/ianj/raw//ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xda 0x7d                                  .}
##### DEBUG DECIMAL
            218  125
#### RECORD 0 BolusWizard 2012-08-22T13:47:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 52,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 10.8,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x34                                  [4
    decimal
             91   52
    datetime (2012-08-22T13:47:06)
    0000   0x86 0x2f 0x0d 0x76 0x0c                   ./.v.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0xfc 0x00    ...n.6..
    0008   0x24 0xf8 0x00 0x6c 0x00 0x20 0x36         $..l. 6
    decimal
             10  144    0  110   23   54  252    0
             36  248    0  108    0   32   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 1.3, 'curve': 4},
 {'age': 113, 'amount': 0.9, 'curve': 4},
 {'age': 173, 'amount': 2.5, 'curve': 4},
 {'age': 193, 'amount': 3.1, 'curve': 4},
 {'age': 87, 'amount': 1.8, 'curve': 20},
 {'age': 107, 'amount': 2.7, 'curve': 20},
 {'age': 147, 'amount': 1.9, 'curve': 20},
 {'age': 207, 'amount': 4.8, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x34 0x0d 0x04 0x24 0x71 0x04    \.4..$q.
    0008   0x64 0xad 0x04 0x7c 0xc1 0x04 0x48 0x57    d..|..HW
    0010   0x14 0x6c 0x6b 0x14 0x4c 0x93 0x14 0xc0    .lk.L...
    0018   0xcf 0x14                                  ..
    decimal
             92   26   52   13    4   36  113    4
            100  173    4  124  193    4   72   87
             20  108  107   20   76  147   20  192
            207   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2012-08-22T13:47:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x6c 0x00    ..0.0.l.
    decimal
              1    0   48    0   48    0  108    0
    datetime (2012-08-22T13:47:06)
    0000   0x86 0x2f 0x4d 0x76 0x0c                   ./Mv.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2012-08-22T16:02:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-22T16:02:17)
    0000   0x91 0x02 0x10 0x76 0x0c                   ...v.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 138, 'amount': 1.2, 'curve': 4},
 {'age': 148, 'amount': 1.3, 'curve': 4},
 {'age': 248, 'amount': 0.9, 'curve': 4},
 {'age': 52, 'amount': 2.5, 'curve': 20},
 {'age': 72, 'amount': 3.1, 'curve': 20},
 {'age': 222, 'amount': 1.8, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x30 0x8a 0x04 0x34 0x94 0x04    \.0..4..
    0008   0x24 0xf8 0x04 0x64 0x34 0x14 0x7c 0x48    $..d4.|H
    0010   0x14 0x48 0xde 0x14                        .H..
    decimal
             92   20   48  138    4   52  148    4
             36  248    4  100   52   20  124   72
             20   72  222   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-08-22T16:02:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x24 0x00    ..`.`.$.
    decimal
              1    0   96    0   96    0   36    0
    datetime (2012-08-22T16:02:17)
    0000   0x91 0x02 0x50 0x76 0x0c                   ..Pv.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2012-08-22T17:36:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2012-08-22T17:36:26)
    0000   0x9a 0x24 0x31 0x76 0x0c                   .$1v.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2012-08-22T17:36:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2012-08-22T17:36:26)
    0000   0x9a 0x24 0xf1 0x76 0x0c                   .$.v.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 CalBGForPH 2012-08-22T18:32:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 205}
```
    op hex (2)
    0000   0x0a 0xcd                                  ..
    decimal
             10  205
    datetime (2012-08-22T18:32:18)
    0000   0x92 0x20 0x32 0x76 0x0c                   . 2v.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 Ian3F 2012-08-22T18:32:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2012-08-22T18:32:18)
    0000   0x92 0x20 0xb2 0x76 0x0c                   . .v.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 BolusWizard 2012-08-22T18:32:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.8,
 'carb_input': 42,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 10.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 152}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2012-08-22T18:32:39)
    0000   0xa7 0x20 0x12 0x76 0x0c                   . .v.
    body (15)
    hex
    0000   0x2a 0x90 0x00 0x6e 0x17 0x36 0x68 0x00    *..n.6h.
    0008   0x98 0x00 0x00 0x1c 0x00 0xe4 0x36         ......6
    decimal
             42  144    0  110   23   54  104    0
            152    0    0   28    0  228   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 158, 'amount': 2.4, 'curve': 4},
 {'age': 32, 'amount': 1.2, 'curve': 20},
 {'age': 42, 'amount': 1.3, 'curve': 20},
 {'age': 142, 'amount': 0.9, 'curve': 20},
 {'age': 202, 'amount': 2.5, 'curve': 20},
 {'age': 222, 'amount': 3.1, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x60 0x9e 0x04 0x30 0x20 0x14    \.`..0 .
    0008   0x34 0x2a 0x14 0x24 0x8e 0x14 0x64 0xca    4*.$..d.
    0010   0x14 0x7c 0xde 0x14                        .|..
    decimal
             92   20   96  158    4   48   32   20
             52   42   20   36  142   20  100  202
             20  124  222   20
    datetime (unknown)

    body (0)

#### RECORD 12 Ian69 2012-08-22T18:32:39 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-22T18:32:39)
    0000   0xa7 0x20 0x72 0x16 0x0c                   . r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 13 Bolus 2012-08-22T18:32:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 22.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xe4 0x00 0xe4 0x00 0x1c 0x00    ........
    decimal
              1    0  228    0  228    0   28    0
    datetime (2012-08-22T18:32:39)
    0000   0xa7 0x20 0x52 0x76 0x0c                   . Rv.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 CalBGForPH 2012-08-22T23:05:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2012-08-22T23:05:02)
    0000   0x82 0x05 0x37 0x76 0x0c                   ..7v.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 15 Ian3F 2012-08-22T23:05:02 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2012-08-22T23:05:02)
    0000   0x82 0x05 0xf7 0x76 0x0c                   ...v.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2012-08-22T23:05:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 102,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 8.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2012-08-22T23:05:09)
    0000   0x89 0x05 0x17 0x76 0x0c                   ...v.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x50 0x00    ...n.6P.
    0008   0x00 0x00 0x00 0x00 0x00 0x50 0x36         .....P6
    decimal
              0  144    0  110   23   54   80    0
              0    0    0    0    0   80   54
    DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 3.7, 'curve': 20},
 {'age': 25, 'amount': 2.0, 'curve': 20},
 {'age': 175, 'amount': 2.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x94 0x0f 0x14 0x50 0x19 0x14    \....P..
    0008   0x60 0xaf 0x14                             `..
    decimal
             92   11  148   15   20   80   25   20
             96  175   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2012-08-22T23:05:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2012-08-22T23:05:09)
    0000   0x89 0x05 0x57 0x76 0x0c                   ..Wv.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 19 BasalProfileStart 2012-08-23T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-23T00:00:00)
    0000   0x80 0x00 0x00 0x17 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 20 ResultTotals (2000, 8, 0, 0, 12, 22) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x45                   ....E
    decimal
              7    0    0    8   69
    datetime ((2000, 8, 0, 0, 12, 22))
    0000   0x96 0x0c 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 21 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x96 0x0c 0x06 0x10 0xb2 0x5d 0x2a    n.....]*
    0008   0x07 0x00 0x00 0x08 0x45 0x03 0x89 0x2b    ....E..+
    0010   0x04 0xbc 0x39 0x00 0xe5 0x02 0x64 0x01    ..9...d.
    0018   0x10 0x01 0x48 0x00 0x00 0x08 0x02 0x02    ..H.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  150   12    6   16  178   93   42
              7    0    0    8   69    3  137   43
              4  188   57    0  229    2  100    1
             16    1   72    0    0    8    2    2
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 22 BolusWizard 2012-08-23T00:02:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 44,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 160}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-23T00:02:26)
    0000   0x9a 0x02 0x00 0x77 0x0c                   ...w.
    body (15)
    hex
    0000   0x2c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ,..n.6..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x36         ......6
    decimal
             44  144    0  110   23   54    0    0
            160    0    0    0    0  160   54
    DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 58, 'amount': 2.0, 'curve': 4},
 {'age': 72, 'amount': 3.7, 'curve': 20},
 {'age': 82, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x3a 0x04 0x94 0x48 0x14    \.P:..H.
    0008   0x50 0x52 0x14                             PR.
    decimal
             92   11   80   58    4  148   72   20
             80   82   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2012-08-23T00:02:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 21.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xd8 0x00 0xd8 0x00 0x44 0x00    ......D.
    decimal
              1    0  216    0  216    0   68    0
    datetime (2012-08-23T00:02:26)
    0000   0x9a 0x02 0x40 0x77 0x0c                   ..@w.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 25 BolusWizard 2012-08-23T00:59:03 head[2], body[15] op[0x5b]
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
    datetime (2012-08-23T00:59:03)
    0000   0x83 0x3b 0x00 0x77 0x0c                   .;.w.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 3.1, 'curve': 4},
 {'age': 65, 'amount': 2.3, 'curve': 4},
 {'age': 115, 'amount': 2.0, 'curve': 4},
 {'age': 129, 'amount': 3.7, 'curve': 20},
 {'age': 139, 'amount': 2.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x7c 0x37 0x04 0x5c 0x41 0x04    \.|7.\A.
    0008   0x50 0x73 0x04 0x94 0x81 0x14 0x50 0x8b    Ps....P.
    0010   0x14                                       .
    decimal
             92   17  124   55    4   92   65    4
             80  115    4  148  129   20   80  139
             20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2012-08-23T00:59:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0xdc 0x00    ..X.X...
    decimal
              1    0   88    0   88    0  220    0
    datetime (2012-08-23T00:59:04)
    0000   0x84 0x3b 0x40 0x77 0x0c                   .;@w.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 28 BasalProfileStart 2012-08-23T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-23T04:00:00)
    0000   0x80 0x00 0x04 0x17 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 29 CalBGForPH 2012-08-23T08:25:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2012-08-23T08:25:34)
    0000   0xa2 0x19 0x28 0x77 0x0c                   ..(w.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 30 Ian3F 2012-08-23T08:25:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2012-08-23T08:25:34)
    0000   0xa2 0x19 0xa8 0x77 0x0c                   ...w.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2012-08-23T09:14:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-23T09:14:45)
    0000   0xad 0x0e 0x09 0x77 0x0c                   ...w.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    DAY BITS: [0, 1, 1]
#### RECORD 32 Ian69 2012-08-23T09:14:45 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-23T09:14:45)
    0000   0xad 0x0e 0x09 0x17 0x0c                   .....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30

#### RECORD 33 Bolus 2012-08-23T09:14:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x00 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    0    0
    datetime (2012-08-23T09:14:45)
    0000   0xad 0x0e 0x49 0x77 0x0c                   ..Iw.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 34 BasalProfileStart 2012-08-23T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-23T09:30:00)
    0000   0x80 0x1e 0x09 0x17 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 35 BolusWizard 2012-08-23T09:44:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-23T09:44:24)
    0000   0x98 0x2c 0x09 0x77 0x0c                   .,.w.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0x1e 0x04                   \.h..
    decimal
             92    5  104   30    4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2012-08-23T09:44:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x64 0x00    ..T.T.d.
    decimal
              1    0   84    0   84    0  100    0
    datetime (2012-08-23T09:44:24)
    0000   0x98 0x2c 0x49 0x77 0x0c                   .,Iw.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2012-08-23T10:30:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-23T10:30:52)
    0000   0xb4 0x1e 0x0a 0x77 0x0c                   ...w.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 2.1, 'curve': 4},
 {'age': 76, 'amount': 2.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x54 0x2e 0x04 0x68 0x4c 0x04    \.T..hL.
    decimal
             92    8   84   46    4  104   76    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2012-08-23T10:30:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x98 0x00    ..h.h...
    decimal
              1    0  104    0  104    0  152    0
    datetime (2012-08-23T10:30:52)
    0000   0xb4 0x1e 0x4a 0x77 0x0c                   ..Jw.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 41 BasalProfileStart 2012-08-23T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-23T13:00:00)
    0000   0x80 0x00 0x0d 0x17 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 42 CalBGForPH 2012-08-23T14:07:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2012-08-23T14:07:52)
    0000   0xb4 0x07 0x2e 0x77 0x0c                   ...w.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 43 Ian3F 2012-08-23T14:07:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2012-08-23T14:07:52)
    0000   0xb4 0x07 0xae 0x77 0x0c                   ...w.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 44 Ian69 2012-08-23T14:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-23T14:30:00)
    0000   0x80 0x1e 0x0e 0x17 0x0c                   .....
    body (2)
    hex
    0000   0x2e 0x1e                                  ..
    decimal
             46   30

#### RECORD 45 CalBGForPH 2012-08-23T15:28:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-08-23T15:28:50)
    0000   0xb2 0x1c 0x4f 0x17 0x0c                   ..O..
    body (0)

#### RECORD 46 BolusWizard 2012-08-23T15:28:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 42,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 8.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 152}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2012-08-23T15:28:58)
    0000   0xba 0x1c 0x0f 0x77 0x0c                   ...w.
    body (15)
    hex
    0000   0x2a 0x90 0x00 0x6e 0x17 0x36 0x50 0x00    *..n.6P.
    0008   0x98 0x00 0x00 0x00 0x00 0xe8 0x36         ......6
    decimal
             42  144    0  110   23   54   80    0
            152    0    0    0    0  232   54
    DAY BITS: [0, 1, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.6, 'curve': 20},
 {'age': 88, 'amount': 2.1, 'curve': 20},
 {'age': 118, 'amount': 2.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0x30 0x14 0x54 0x58 0x14    \.h0.TX.
    0008   0x68 0x76 0x14                             hv.
    decimal
             92   11  104   48   20   84   88   20
            104  118   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2012-08-23T15:28:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 23.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xe8 0x00 0xe8 0x00 0x00 0x00    ........
    decimal
              1    0  232    0  232    0    0    0
    datetime (2012-08-23T15:28:58)
    0000   0xba 0x1c 0x4f 0x77 0x0c                   ..Ow.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 49 CalBGForPH 2012-08-23T18:41:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2012-08-23T18:41:36)
    0000   0xa4 0x29 0x32 0x77 0x0c                   .)2w.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 Ian3F 2012-08-23T18:41:36 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2012-08-23T18:41:36)
    0000   0xa4 0x29 0xd2 0x77 0x0c                   .).w.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 BolusWizard 2012-08-23T18:41:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 3.2,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 10.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2012-08-23T18:41:50)
    0000   0xb2 0x29 0x12 0x77 0x0c                   .).w.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x68 0x00    ...n.6h.
    0008   0x58 0x00 0x00 0x20 0x00 0xa0 0x36         X.. ..6
    decimal
             25  144    0  110   23   54  104    0
             88    0    0   32    0  160   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 197, 'amount': 5.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xe8 0xc5 0x04                   \....
    decimal
             92    5  232  197    4
    datetime (unknown)

    body (0)

#### RECORD 53 Ian69 2012-08-23T18:41:50 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-23T18:41:50)
    0000   0xb2 0x29 0x72 0x17 0x0c                   .)r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 54 Bolus 2012-08-23T18:41:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x20 0x00    ...... .
    decimal
              1    0  160    0  160    0   32    0
    datetime (2012-08-23T18:41:50)
    0000   0xb2 0x29 0x52 0x77 0x0c                   .)Rw.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 BolusWizard 2012-08-23T22:23:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 48,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 172}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-23T22:23:36)
    0000   0xa4 0x17 0x16 0x77 0x0c                   ...w.
    body (15)
    hex
    0000   0x30 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    0..n.6..
    0008   0xac 0x00 0x00 0x00 0x00 0xac 0x36         ......6
    decimal
             48  144    0  110   23   54    0    0
            172    0    0    0    0  172   54
    DAY BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 219, 'amount': 0.8, 'curve': 4},
 {'age': 229, 'amount': 3.2, 'curve': 4},
 {'age': 163, 'amount': 5.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x20 0xdb 0x04 0x80 0xe5 0x04    \. .....
    0008   0xe8 0xa3 0x14                             ...
    decimal
             92   11   32  219    4  128  229    4
            232  163   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2012-08-23T22:23:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 17.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0x0c 0x00    ........
    decimal
              1    0  172    0  172    0   12    0
    datetime (2012-08-23T22:23:36)
    0000   0xa4 0x17 0x56 0x77 0x0c                   ..Vw.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 58 BolusWizard 2012-08-23T22:27:06 head[2], body[15] op[0x5b]
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
    datetime (2012-08-23T22:27:06)
    0000   0x86 0x1b 0x16 0x77 0x0c                   ...w.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    DAY BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 3.75, 'curve': 4},
 {'age': 13, 'amount': 0.55, 'curve': 4},
 {'age': 223, 'amount': 0.8, 'curve': 4},
 {'age': 233, 'amount': 3.2, 'curve': 4},
 {'age': 167, 'amount': 5.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x96 0x03 0x04 0x16 0x0d 0x04    \.......
    0008   0x20 0xdf 0x04 0x80 0xe9 0x04 0xe8 0xa7     .......
    0010   0x14                                       .
    decimal
             92   17  150    3    4   22   13    4
             32  223    4  128  233    4  232  167
             20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2012-08-23T22:27:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0xb8 0x00    ..4.4...
    decimal
              1    0   52    0   52    0  184    0
    datetime (2012-08-23T22:27:06)
    0000   0x86 0x1b 0x56 0x77 0x0c                   ..Vw.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 61 BolusWizard 2012-08-23T22:37:05 head[2], body[15] op[0x5b]
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
    datetime (2012-08-23T22:37:05)
    0000   0x85 0x25 0x16 0x77 0x0c                   .%.w.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 5.05, 'curve': 4},
 {'age': 23, 'amount': 0.55, 'curve': 4},
 {'age': 233, 'amount': 0.8, 'curve': 4},
 {'age': 243, 'amount': 3.2, 'curve': 4},
 {'age': 177, 'amount': 5.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0xca 0x0d 0x04 0x16 0x17 0x04    \.......
    0008   0x20 0xe9 0x04 0x80 0xf3 0x04 0xe8 0xb1     .......
    0010   0x14                                       .
    decimal
             92   17  202   13    4   22   23    4
             32  233    4  128  243    4  232  177
             20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2012-08-23T22:37:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xe0 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  224    0
    datetime (2012-08-23T22:37:05)
    0000   0x85 0x25 0x56 0x77 0x0c                   .%Vw.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 CalBGForPH 2012-08-23T23:38:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2012-08-23T23:38:48)
    0000   0xb0 0x26 0x37 0x77 0x0c                   .&7w.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 Ian3F 2012-08-23T23:38:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2012-08-23T23:38:48)
    0000   0xb0 0x26 0x57 0x77 0x0c                   .&Ww.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 66 BasalProfileStart 2012-08-24T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-24T00:00:00)
    0000   0x80 0x00 0x00 0x18 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 67 ResultTotals (2000, 8, 0, 0, 12, 23) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x95                   .....
    decimal
              7    0    0    8  149
    datetime ((2000, 8, 0, 0, 12, 23))
    0000   0x97 0x0c 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 68 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x97 0x0c 0x06 0x00 0xa6 0x55 0xce    n.....U.
    0008   0x05 0x00 0x00 0x08 0x95 0x03 0x89 0x29    .......)
    0010   0x05 0x0c 0x3b 0x01 0x28 0x01 0xf4 0x00    ..;.(...
    0018   0x00 0x03 0x18 0x00 0x00 0x05 0x00 0x05    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0xb4 0xb4 0x00 0x00 0x00         .......
    decimal
            110  151   12    6    0  166   85  206
              5    0    0    8  149    3  137   41
              5   12   59    1   40    1  244    0
              0    3   24    0    0    5    0    5
              0    0    0    0    0    0    0    0
              0    0  180  180    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 69 BasalProfileStart 2012-08-24T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-24T04:00:00)
    0000   0x80 0x00 0x04 0x18 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

`end analysis/ianj/raw//ReadHistoryData-page-15.data: 70 records`
