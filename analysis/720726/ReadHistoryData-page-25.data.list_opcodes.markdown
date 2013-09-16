## START logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 667, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x50 0x00 0x00 0x00 0x00 0x50 0x36 0x5c    P....P6\
    0008   0x08 0x38 0x96 0x04 0x7c 0xdc 0x04 0x01    .8..|...
    0010   0x00 0x50 0x00 0x50 0x00 0x1c 0x00 0xa9    .P.P....
    0018   0x0f 0x4e 0x69 0x0d 0x5b 0x00 0x8f 0x11    .Ni.[...
##### DEBUG DECIMAL
             80    0    0    0    0   80   54   92
              8   56  150    4  124  220    4    1
              0   80    0   80    0   28    0  169
             15   78  105   13   91    0  143   17
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

#### RECORD 13 ResultTotals (2000, 8, 0, 0, 13, 8) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x7b                   ....{
    decimal
              7    0    0    7  123
    datetime ((2000, 8, 0, 0, 13, 8))
    0000   0x88 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 14 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x88 0x0d 0x06 0x10 0x9f 0x5f 0x11    n....._.
    0008   0x03 0x00 0x00 0x07 0x7b 0x03 0x87 0x2f    ....{../
    0010   0x03 0xf4 0x35 0x01 0x03 0x03 0x9c 0x00    ..5.....
    0018   0x58 0x00 0x00 0x00 0x00 0x0b 0x01 0x00    X.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  136   13    6   16  159   95   17
              3    0    0    7  123    3  135   47
              3  244   53    1    3    3  156    0
             88    0    0    0    0   11    1    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

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
#### RECORD 16 Base (2013, 8, 9, 0, 13, 39) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime ((2013, 8, 9, 0, 13, 39))
    0000   0xa7 0x0d 0x80 0x69 0x0d                   ...i.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 17 Base (2004, 8, 3, 5, 10, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2004, 8, 3, 5, 10, 22))
    0000   0x96 0x0a 0x65 0xa3 0x14                   ..e..
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 18 Base (2004, 0, 3, 12, 63, 13) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x69                                   i
    decimal
             32  105
    datetime ((2004, 0, 3, 12, 63, 13))
    0000   0x0d 0x3f 0x0c 0xa3 0x14                   .?...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 19 Base (2011, 1, 22, 9, 41, 13) head[2], body[0] op[0xa0]

    op hex (2)
    0000   0xa0 0x69                                  .i
    decimal
            160  105
    datetime ((2011, 1, 22, 9, 41, 13))
    0000   0x0d 0x69 0x69 0x96 0x5b                   .ii.[
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 20 Base (2001, 0, 13, 9, 0, 20) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0xb7                                  8.
    decimal
             56  183
    datetime ((2001, 0, 13, 9, 0, 20))
    0000   0x14 0x00 0x69 0x0d 0x11                   ..i..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 21 Base (2000, 4, 0, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 0, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x00 0x00                   n.6..
    body (0)

#### RECORD 22 Base (2006, 1, 28, 0, 8, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x00                                  <.
    decimal
             60    0
    datetime ((2006, 1, 28, 0, 8, 0))
    0000   0x00 0x48 0x00 0x3c 0x36                   .H.<6
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
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

#### RECORD 24 Bolus 2013-08-09T00:20:55 head[8], body[0] op[0x01]
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
#### RECORD 25 BolusWizard 2013-08-09T01:39:53 head[2], body[15] op[0x5b]
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
#### RECORD 26 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
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

#### RECORD 27 Bolus 2013-08-09T01:39:54 head[8], body[0] op[0x01]
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
#### RECORD 28 BasalProfileStart 2013-08-09T04:00:00 head[2], body[3] op[0x7b]

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

#### RECORD 29 CalBGForPH 2013-08-09T09:12:21 head[2], body[0] op[0x0a]
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
#### RECORD 30 Base (2013, 8, 9, 9, 12, 21) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime ((2013, 8, 9, 9, 12, 21))
    0000   0x95 0x0c 0xe9 0x69 0x0d                   ...i.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 31 Base (2014, 9, 0, 2, 59, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2014, 9, 0, 2, 59, 22))
    0000   0x96 0x7b 0x02 0x80 0x1e                   .{...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 32 Base (2009, 0, 0, 30, 19, 13) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x09                                  ..
    decimal
              9    9
    datetime ((2009, 0, 0, 30, 19, 13))
    0000   0x0d 0x13 0x1e 0x00 0x69                   ....i
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 33 ChangeBasalProfile (2010, 0, 13, 9, 10, 30) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x80                                  ..
    decimal
              8  128
    datetime ((2010, 0, 13, 9, 10, 30))
    0000   0x1e 0x0a 0x09 0x0d 0x2a                   ....*
    body (44)
    hex
    0000   0x1e 0x5b 0x00 0xb9 0x23 0x0a 0x69 0x0d    .[..#.i.
    0008   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0010   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36 0x01    |....|6.
    0018   0x00 0x7c 0x00 0x7c 0x00 0x00 0x00 0xb9    .|.|....
    0020   0x23 0x4a 0x69 0x0d 0x0a 0x01 0x9d 0x30    #Ji....0
    0028   0x2b 0x69 0x8d 0x3f                        +i.?
    decimal
             30   91    0  185   35   10  105   13
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54    1
              0  124    0  124    0    0    0  185
             35   74  105   13   10    1  157   48
             43  105  141   63
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 34 Base (2009, 0, 13, 9, 43, 48) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x9d                                   .
    decimal
             32  157
    datetime ((2009, 0, 13, 9, 43, 48))
    0000   0x30 0x2b 0x69 0x0d 0x69                   0+i.i
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 35 Base (2011, 6, 16, 4, 15, 27) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x96                                  i.
    decimal
            105  150
    datetime ((2011, 6, 16, 4, 15, 27))
    0000   0x5b 0x8f 0xa4 0x30 0x0b                   [..0.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1]
#### RECORD 36 Base (2007, 2, 14, 0, 16, 0) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x0d                                  i.
    decimal
            105   13
    datetime ((2007, 2, 14, 0, 16, 0))
    0000   0x00 0x90 0x00 0x6e 0x17                   ...n.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 37 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x98                                  6.
    decimal
             54  152
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x60                   ....`
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 38 Base (2009, 1, 28, 5, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x38                                  .8
    decimal
              0   56
    datetime ((2009, 1, 28, 5, 28, 54))
    0000   0x36 0x5c 0x05 0x7c 0x49                   6\.|I
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 39 Base (2009, 2, 11, 16, 36, 11) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x69                                  .i
    decimal
              4  105
    datetime ((2009, 2, 11, 16, 36, 11))
    0000   0x0b 0xa4 0x30 0x0b 0x09                   ..0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 40 Base (2000, 0, 24, 0, 1, 30) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0e                                  ..
    decimal
             13   14
    datetime ((2000, 0, 24, 0, 1, 30))
    0000   0x1e 0x01 0x00 0x38 0x00                   ...8.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 41 Base (2011, 4, 16, 4, 0, 32) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x00                                  8.
    decimal
             56    0
    datetime ((2011, 4, 16, 4, 0, 32))
    0000   0x60 0x00 0xa4 0x30 0x4b                   `..0K
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 42 Base (2013, 4, 0, 0, 3, 59) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x0d                                  i.
    decimal
            105   13
    datetime ((2013, 4, 0, 0, 3, 59))
    0000   0x7b 0x03 0x80 0x00 0x0d                   {....
    body (0)

#### RECORD 43 Base (2015, 0, 10, 0, 38, 26) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x0d                                  ..
    decimal
              9   13
    datetime ((2015, 0, 10, 0, 38, 26))
    0000   0x1a 0x26 0x00 0x0a 0x9f                   .&...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 44 Base (2003, 1, 31, 13, 41, 45) head[2], body[0] op[0x83]

    op hex (2)
    0000   0x83 0x28                                  .(
    decimal
            131   40
    datetime ((2003, 1, 31, 13, 41, 45))
    0000   0x2d 0x69 0x0d 0x3f 0x13                   -i.?.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 45 Base (2009, 13, 9, 13, 41, 45) head[2], body[0] op[0x83]

    op hex (2)
    0000   0x83 0x28                                  .(
    decimal
            131   40
    datetime ((2009, 13, 9, 13, 41, 45))
    0000   0xed 0x69 0x0d 0x69 0x69                   .i.ii
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 46 Base (2009, 2, 14, 15, 41, 0) head[2], body[0] op[0x96]

    op hex (2)
    0000   0x96 0x5b                                  .[
    decimal
            150   91
    datetime ((2009, 2, 14, 15, 41, 0))
    0000   0x00 0xa9 0x0f 0x0e 0x69                   ....i
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 47 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x17                                  ..
    decimal
             13   23
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-25.data: 48 records`
