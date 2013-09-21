## START analysis/ianj/raw/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 1001, found 21 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x85 0x12                                  ..
##### DEBUG DECIMAL
            133   18
#### RECORD 0 BolusWizard 2013-08-08T18:53:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-08T18:53:12)
    0000   0x8c 0x35 0x12 0x68 0x0d                   .5.h.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 0.8, 'curve': 4},
 {'age': 38, 'amount': 1.4, 'curve': 4},
 {'age': 48, 'amount': 2.7, 'curve': 4},
 {'age': 178, 'amount': 0.325, 'curve': 4},
 {'age': 188, 'amount': 0.575, 'curve': 4},
 {'age': 92, 'amount': 2.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x20 0x1c 0x04 0x38 0x26 0x04    \. ..8&.
    0008   0x6c 0x30 0x04 0x0d 0xb2 0x04 0x17 0xbc    l0......
    0010   0x04 0x50 0x5c 0x14                        .P\.
    decimal
             92   20   32   28    4   56   38    4
            108   48    4   13  178    4   23  188
              4   80   92   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-08-08T18:53:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0xb8 0x00    ..|.|...
    decimal
              1    0  124    0  124    0  184    0
    datetime (2013-08-08T18:53:12)
    0000   0x8c 0x35 0x52 0x68 0x0d                   .5Rh.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2013-08-08T19:08:56 head[2], body[15] op[0x5b]
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
    datetime (2013-08-08T19:08:56)
    0000   0xb8 0x08 0x13 0x68 0x0d                   ...h.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 0.45, 'curve': 4},
 {'age': 23, 'amount': 2.65, 'curve': 4},
 {'age': 43, 'amount': 0.8, 'curve': 4},
 {'age': 53, 'amount': 1.4, 'curve': 4},
 {'age': 63, 'amount': 2.7, 'curve': 4},
 {'age': 193, 'amount': 0.325, 'curve': 4},
 {'age': 203, 'amount': 0.575, 'curve': 4},
 {'age': 107, 'amount': 2.0, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x12 0x0d 0x04 0x6a 0x17 0x04    \....j..
    0008   0x20 0x2b 0x04 0x38 0x35 0x04 0x6c 0x3f     +.85.l?
    0010   0x04 0x0d 0xc1 0x04 0x17 0xcb 0x04 0x50    .......P
    0018   0x6b 0x14                                  k.
    decimal
             92   26   18   13    4  106   23    4
             32   43    4   56   53    4  108   63
              4   13  193    4   23  203    4   80
            107   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-08-08T19:08:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x01 0x24 0x00    ..H.H.$.
    decimal
              1    0   72    0   72    1   36    0
    datetime (2013-08-08T19:08:56)
    0000   0xb8 0x08 0x53 0x68 0x0d                   ..Sh.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2013-08-08T21:40:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 39,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 140}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-08T21:40:53)
    0000   0xb5 0x28 0x15 0x68 0x0d                   .(.h.
    body (15)
    hex
    0000   0x27 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    '..n.6..
    0008   0x8c 0x00 0x00 0x00 0x00 0x8c 0x36         ......6
    decimal
             39  144    0  110   23   54    0    0
            140    0    0    0    0  140   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.8, 'curve': 4},
 {'age': 165, 'amount': 0.45, 'curve': 4},
 {'age': 175, 'amount': 2.65, 'curve': 4},
 {'age': 195, 'amount': 0.8, 'curve': 4},
 {'age': 205, 'amount': 1.4, 'curve': 4},
 {'age': 215, 'amount': 2.7, 'curve': 4},
 {'age': 89, 'amount': 0.325, 'curve': 20},
 {'age': 99, 'amount': 0.575, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x48 0x9b 0x04 0x12 0xa5 0x04    \.H.....
    0008   0x6a 0xaf 0x04 0x20 0xc3 0x04 0x38 0xcd    j.. ..8.
    0010   0x04 0x6c 0xd7 0x04 0x0d 0x59 0x14 0x17    .l...Y..
    0018   0x63 0x14                                  c.
    decimal
             92   26   72  155    4   18  165    4
            106  175    4   32  195    4   56  205
              4  108  215    4   13   89   20   23
             99   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-08-08T21:40:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x40 0x00    ......@.
    decimal
              1    0  140    0  140    0   64    0
    datetime (2013-08-08T21:40:53)
    0000   0xb5 0x28 0x55 0x68 0x0d                   .(Uh.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 BolusWizard 2013-08-08T22:53:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-08T22:53:58)
    0000   0xba 0x35 0x16 0x68 0x0d                   .5.h.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 78, 'amount': 3.5, 'curve': 4},
 {'age': 228, 'amount': 1.8, 'curve': 4},
 {'age': 238, 'amount': 0.45, 'curve': 4},
 {'age': 248, 'amount': 2.65, 'curve': 4},
 {'age': 12, 'amount': 0.8, 'curve': 20},
 {'age': 22, 'amount': 1.4, 'curve': 20},
 {'age': 32, 'amount': 2.7, 'curve': 20},
 {'age': 162, 'amount': 0.325, 'curve': 20},
 {'age': 172, 'amount': 0.575, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x8c 0x4e 0x04 0x48 0xe4 0x04    \..N.H..
    0008   0x12 0xee 0x04 0x6a 0xf8 0x04 0x20 0x0c    ...j.. .
    0010   0x14 0x38 0x16 0x14 0x6c 0x20 0x14 0x0d    .8..l ..
    0018   0xa2 0x14 0x17 0xac 0x14                   .....
    decimal
             92   29  140   78    4   72  228    4
             18  238    4  106  248    4   32   12
             20   56   22   20  108   32   20   13
            162   20   23  172   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-08-08T22:53:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x6c 0x00    ..@.@.l.
    decimal
              1    0   64    0   64    0  108    0
    datetime (2013-08-08T22:53:58)
    0000   0xba 0x35 0x56 0x68 0x0d                   .5Vh.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 BasalProfileStart 2013-08-09T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-09T00:00:00)
    0000   0x80 0x00 0x00 0x09 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 13 MResultTotals 2013-08-09T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x7b                   ....{
    decimal
              7    0    0    7  123
    datetime (2013-08-09T00:00:00)
    0000   0x88 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 14 Sara6E 2013-08-09T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-09T00:00:00)
    0000   0x88 0x0d                                  ..
    body (49)
    hex
    0000   0x06 0x10 0x9f 0x5f 0x11 0x03 0x00 0x00    ..._....
    0008   0x07 0x7b 0x03 0x87 0x2f 0x03 0xf4 0x35    .{../..5
    0010   0x01 0x03 0x03 0x9c 0x00 0x58 0x00 0x00    .....X..
    0018   0x00 0x00 0x0b 0x01 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6   16  159   95   17    3    0    0
              7  123    3  135   47    3  244   53
              1    3    3  156    0   88    0    0
              0    0   11    1    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 15 CalBGForPH 2013-08-09T00:13:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-08-09T00:13:39)
    0000   0xa7 0x0d 0x20 0x69 0x0d                   .. i.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 16 Ian3F 2013-08-09T00:13:39 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2013-08-09T00:13:39)
    0000   0xa7 0x0d 0x80 0x69 0x0d                   ...i.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 17 CalBGForPH 2013-08-09T00:20:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-08-09T00:20:35)
    0000   0xa3 0x14 0x20 0x69 0x0d                   .. i.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 18 Ian3F 2013-08-09T00:20:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2013-08-09T00:20:35)
    0000   0xa3 0x14 0xa0 0x69 0x0d                   ...i.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 19 BolusWizard 2013-08-09T00:20:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 56,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 7.2,
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
    0000   0x5b 0x38                                  [8
    decimal
             91   56
    datetime (2013-08-09T00:20:55)
    0000   0xb7 0x14 0x00 0x69 0x0d                   ...i.
    body (15)
    hex
    0000   0x11 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x3c 0x00 0x00 0x48 0x00 0x3c 0x36         <..H.<6
    decimal
             17  144    0  110   23   54    0    0
             60    0    0   72    0   60   54
    DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 0.05, 'curve': 4},
 {'age': 95, 'amount': 1.55, 'curve': 4},
 {'age': 165, 'amount': 3.5, 'curve': 4},
 {'age': 59, 'amount': 1.8, 'curve': 20},
 {'age': 69, 'amount': 0.45, 'curve': 20},
 {'age': 79, 'amount': 2.65, 'curve': 20},
 {'age': 99, 'amount': 0.8, 'curve': 20},
 {'age': 109, 'amount': 1.4, 'curve': 20},
 {'age': 119, 'amount': 2.7, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x02 0x55 0x04 0x3e 0x5f 0x04    \..U.>_.
    0008   0x8c 0xa5 0x04 0x48 0x3b 0x14 0x12 0x45    ...H;..E
    0010   0x14 0x6a 0x4f 0x14 0x20 0x63 0x14 0x38    .jO. c.8
    0018   0x6d 0x14 0x6c 0x77 0x14                   m.lw.
    decimal
             92   29    2   85    4   62   95    4
            140  165    4   72   59   20   18   69
             20  106   79   20   32   99   20   56
            109   20  108  119   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-08-09T00:20:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x48 0x00    ..<.<.H.
    decimal
              1    0   60    0   60    0   72    0
    datetime (2013-08-09T00:20:55)
    0000   0xb7 0x14 0x40 0x69 0x0d                   ..@i.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2013-08-09T01:39:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-09T01:39:53)
    0000   0xb5 0x27 0x01 0x69 0x0d                   .'.i.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 84, 'amount': 1.5, 'curve': 4},
 {'age': 164, 'amount': 0.05, 'curve': 4},
 {'age': 174, 'amount': 1.55, 'curve': 4},
 {'age': 244, 'amount': 3.5, 'curve': 4},
 {'age': 138, 'amount': 1.8, 'curve': 20},
 {'age': 148, 'amount': 0.45, 'curve': 20},
 {'age': 158, 'amount': 2.65, 'curve': 20},
 {'age': 178, 'amount': 0.8, 'curve': 20},
 {'age': 188, 'amount': 1.4, 'curve': 20},
 {'age': 198, 'amount': 2.7, 'curve': 20}]
```
    op hex (32)
    0000   0x5c 0x20 0x3c 0x54 0x04 0x02 0xa4 0x04    \ <T....
    0008   0x3e 0xae 0x04 0x8c 0xf4 0x04 0x48 0x8a    >.....H.
    0010   0x14 0x12 0x94 0x14 0x6a 0x9e 0x14 0x20    ....j.. 
    0018   0xb2 0x14 0x38 0xbc 0x14 0x6c 0xc6 0x14    ..8..l..
    decimal
             92   32   60   84    4    2  164    4
             62  174    4  140  244    4   72  138
             20   18  148   20  106  158   20   32
            178   20   56  188   20  108  198   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-08-09T01:39:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x38 0x00    ..@.@.8.
    decimal
              1    0   64    0   64    0   56    0
    datetime (2013-08-09T01:39:54)
    0000   0xb6 0x27 0x41 0x69 0x0d                   .'Ai.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 BasalProfileStart 2013-08-09T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-09T04:00:00)
    0000   0x80 0x00 0x04 0x09 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 26 CalBGForPH 2013-08-09T09:12:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-08-09T09:12:21)
    0000   0x95 0x0c 0x29 0x69 0x0d                   ..)i.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 27 Ian3F 2013-08-09T09:12:21 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2013-08-09T09:12:21)
    0000   0x95 0x0c 0xe9 0x69 0x0d                   ...i.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 28 BasalProfileStart 2013-08-09T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-09T09:30:00)
    0000   0x80 0x1e 0x09 0x09 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 29 Ian69 2013-08-09T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-09T10:30:00)
    0000   0x80 0x1e 0x0a 0x09 0x0d                   .....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30

#### RECORD 30 BolusWizard 2013-08-09T10:35:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-09T10:35:57)
    0000   0xb9 0x23 0x0a 0x69 0x0d                   .#.i.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 Bolus 2013-08-09T10:35:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x00 0x00    ..|.|...
    decimal
              1    0  124    0  124    0    0    0
    datetime (2013-08-09T10:35:57)
    0000   0xb9 0x23 0x4a 0x69 0x0d                   .#Ji.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 CalBGForPH 2013-08-09T11:48:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 257}
```
    op hex (2)
    0000   0x0a 0x01                                  ..
    decimal
             10    1
    datetime (2013-08-09T11:48:29)
    0000   0x9d 0x30 0x2b 0x69 0x8d                   .0+i.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 Ian3F 2013-08-09T11:48:29 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2013-08-09T11:48:29)
    0000   0x9d 0x30 0x2b 0x69 0x0d                   .0+i.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 BolusWizard 2013-08-09T11:48:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 9.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 15.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2013-08-09T11:48:36)
    0000   0xa4 0x30 0x0b 0x69 0x0d                   .0.i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x98 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x60 0x00 0x38 0x36         ...`.86
    decimal
              0  144    0  110   23   54  152    0
              0    0    0   96    0   56   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 3.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x49 0x04                   \.|I.
    decimal
             92    5  124   73    4
    datetime (unknown)

    body (0)

#### RECORD 36 Ian69 2013-08-09T11:48:36 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-09T11:48:36)
    0000   0xa4 0x30 0x0b 0x09 0x0d                   .0...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 37 Bolus 2013-08-09T11:48:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x60 0x00    ..8.8.`.
    decimal
              1    0   56    0   56    0   96    0
    datetime (2013-08-09T11:48:36)
    0000   0xa4 0x30 0x4b 0x69 0x0d                   .0Ki.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 BasalProfileStart 2013-08-09T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-09T13:00:00)
    0000   0x80 0x00 0x0d 0x09 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 39 CalBGForPH 2013-08-09T13:40:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2013-08-09T13:40:03)
    0000   0x83 0x28 0x2d 0x69 0x0d                   .(-i.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 Ian3F 2013-08-09T13:40:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2013-08-09T13:40:03)
    0000   0x83 0x28 0xed 0x69 0x0d                   .(.i.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 BolusWizard 2013-08-09T14:15:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 23,
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
    datetime (2013-08-09T14:15:41)
    0000   0xa9 0x0f 0x0e 0x69 0x0d                   ...i.
    body (15)
    hex
    0000   0x17 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             23  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    DAY BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 1.4, 'curve': 4},
 {'age': 220, 'amount': 3.1, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x38 0x96 0x04 0x7c 0xdc 0x04    \.8..|..
    decimal
             92    8   56  150    4  124  220    4
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-08-09T14:15:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x1c 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   28    0
    datetime (2013-08-09T14:15:41)
    0000   0xa9 0x0f 0x4e 0x69 0x0d                   ..Ni.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 44 BolusWizard 2013-08-09T14:17:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 8,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 28}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-09T14:17:15)
    0000   0x8f 0x11 0x0e 0x69 0x0d                   ...i.
    body (15)
    hex
    0000   0x08 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x1c 0x00 0x00 0x00 0x00 0x1c 0x36         ......6
    decimal
              8  144    0  110   23   54    0    0
             28    0    0    0    0   28   54
    DAY BITS: [0, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 2.0, 'curve': 4},
 {'age': 152, 'amount': 1.4, 'curve': 4},
 {'age': 222, 'amount': 3.1, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x02 0x04 0x38 0x98 0x04    \.P..8..
    0008   0x7c 0xde 0x04                             |..
    decimal
             92   11   80    2    4   56  152    4
            124  222    4
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-08-09T14:17:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x6c 0x00    ......l.
    decimal
              1    0   24    0   24    0  108    0
    datetime (2013-08-09T14:17:16)
    0000   0x90 0x11 0x4e 0x69 0x0d                   ..Ni.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 47 CalBGForPH 2013-08-09T17:58:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-08-09T17:58:21)
    0000   0x95 0x3a 0x31 0x69 0x0d                   .:1i.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 Ian3F 2013-08-09T17:58:21 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2013-08-09T17:58:21)
    0000   0x95 0x3a 0x11 0x69 0x0d                   .:.i.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2013-08-09T18:08:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 44,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 23.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x2c                                  [,
    decimal
             91   44
    datetime (2013-08-09T18:08:27)
    0000   0x9b 0x08 0x12 0x69 0x0d                   ...i.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0xec 0x00    ...n.6..
    0008   0x40 0xf8 0x00 0x08 0x00 0x2c 0x36         @....,6
    decimal
             18  144    0  110   23   54  236    0
             64  248    0    8    0   44   54
    DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 233, 'amount': 2.6, 'curve': 4},
 {'age': 127, 'amount': 1.4, 'curve': 20},
 {'age': 197, 'amount': 3.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0xe9 0x04 0x38 0x7f 0x14    \.h..8..
    0008   0x7c 0xc5 0x14                             |..
    decimal
             92   11  104  233    4   56  127   20
            124  197   20
    datetime (unknown)

    body (0)

#### RECORD 51 Ian69 2013-08-09T18:08:27 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-09T18:08:27)
    0000   0x9b 0x08 0x72 0x09 0x0d                   ..r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 52 Bolus 2013-08-09T18:08:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x08 0x00    ..,.,...
    decimal
              1    0   44    0   44    0    8    0
    datetime (2013-08-09T18:08:27)
    0000   0x9b 0x08 0x52 0x69 0x0d                   ..Ri.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 53 CalBGForPH 2013-08-09T20:49:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2013-08-09T20:49:39)
    0000   0xa7 0x31 0x34 0x69 0x0d                   .14i.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 Ian3F 2013-08-09T20:49:39 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2013-08-09T20:49:39)
    0000   0xa7 0x31 0x94 0x69 0x0d                   .1.i.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 BolusWizard 2013-08-09T20:49:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 104,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.2,
 'carb_input': 44,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 8.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 160}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-08-09T20:49:51)
    0000   0xb3 0x31 0x14 0x69 0x0d                   .1.i.
    body (15)
    hex
    0000   0x2c 0x90 0x00 0x6e 0x17 0x36 0x54 0x00    ,..n.6T.
    0008   0xa0 0x00 0x00 0x0c 0x00 0xe8 0x36         ......6
    decimal
             44  144    0  110   23   54   84    0
            160    0    0   12    0  232   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 164, 'amount': 1.1, 'curve': 4},
 {'age': 138, 'amount': 2.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0xa4 0x04 0x68 0x8a 0x14    \.,..h..
    decimal
             92    8   44  164    4  104  138   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2013-08-09T20:49:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 23.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xe8 0x00 0xe8 0x00 0x0c 0x00    ........
    decimal
              1    0  232    0  232    0   12    0
    datetime (2013-08-09T20:49:51)
    0000   0xb3 0x31 0x54 0x69 0x0d                   .1Ti.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 CalBGForPH 2013-08-09T22:27:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 250}
```
    op hex (2)
    0000   0x0a 0xfa                                  ..
    decimal
             10  250
    datetime (2013-08-09T22:27:27)
    0000   0x9b 0x1b 0x36 0x69 0x0d                   ..6i.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 59 Ian3F 2013-08-09T22:27:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1f                                  ?.
    decimal
             63   31
    datetime (2013-08-09T22:27:27)
    0000   0x9b 0x1b 0x56 0x69 0x0d                   ..Vi.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 60 BolusWizard 2013-08-09T22:27:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 139,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 13.6,
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
    0000   0x5b 0x8b                                  [.
    decimal
             91  139
    datetime (2013-08-09T22:27:38)
    0000   0xa6 0x1b 0x16 0x69 0x0d                   ...i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x90 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x88 0x00 0x08 0x36         ......6
    decimal
              0  144    0  110   23   54  144    0
              0    0    0  136    0    8   54
    DAY BITS: [0, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 5.8, 'curve': 4},
 {'age': 6, 'amount': 1.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xe8 0x66 0x04 0x2c 0x06 0x14    \..f.,..
    decimal
             92    8  232  102    4   44    6   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-08-09T22:27:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x88 0x00    ..8.8...
    decimal
              1    0   56    0   56    0  136    0
    datetime (2013-08-09T22:27:38)
    0000   0xa6 0x1b 0x56 0x69 0x0d                   ..Vi.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 63 BolusWizard 2013-08-09T23:13:09 head[2], body[15] op[0x5b]
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
    datetime (2013-08-09T23:13:09)
    0000   0x89 0x0d 0x17 0x69 0x0d                   ...i.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    DAY BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 1.4, 'curve': 4},
 {'age': 148, 'amount': 5.8, 'curve': 4},
 {'age': 52, 'amount': 1.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0x30 0x04 0xe8 0x94 0x04    \.80....
    0008   0x2c 0x34 0x14                             ,4.
    decimal
             92   11   56   48    4  232  148    4
             44   52   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-08-09T23:13:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x78 0x00    ..`.`.x.
    decimal
              1    0   96    0   96    0  120    0
    datetime (2013-08-09T23:13:09)
    0000   0x89 0x0d 0x57 0x69 0x0d                   ..Wi.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 66 BasalProfileStart 2013-08-10T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-10T00:00:00)
    0000   0x80 0x00 0x00 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 67 MResultTotals 2013-08-10T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xcd                   .....
    decimal
              7    0    0    6  205
    datetime (2013-08-10T00:00:00)
    0000   0x89 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end analysis/ianj/raw/ReadHistoryData-page-25.data: 68 records`
