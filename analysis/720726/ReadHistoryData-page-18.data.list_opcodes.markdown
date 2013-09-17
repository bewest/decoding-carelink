## START logs/ReadHistoryData-page-18.data
#### RECORD 0 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 0.8, 'curve': 4},
 {'age': 104, 'amount': 0.65, 'curve': 5},
 {'age': 114, 'amount': 1.15, 'curve': 4},
 {'age': 244, 'amount': 3.7, 'curve': 4},
 {'age': 38, 'amount': 2.9, 'curve': 20},
 {'age': 78, 'amount': 2.6, 'curve': 20},
 {'age': 168, 'amount': 3.1, 'curve': 20},
 {'age': 188, 'amount': 2.7, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x20 0x5e 0x04 0x1a 0x68 0x05    \. ^..h.
    0008   0x2e 0x72 0x04 0x94 0xf4 0x04 0x74 0x26    .r....t&
    0010   0x14 0x68 0x4e 0x14 0x7c 0xa8 0x14 0x6c    .hN.|..l
    0018   0xbc 0x14                                  ..
    decimal
             92   26   32   94    4   26  104    5
             46  114    4  148  244    4  116   38
             20  104   78   20  124  168   20  108
            188   20
    datetime (unknown)

    body (0)

#### RECORD 1 Ian69 2012-08-19T17:48:48 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-19T17:48:48)
    0000   0xb0 0x30 0x71 0x13 0x0c                   .0q..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 2 Bolus 2012-08-19T17:48:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0xcc 0x00    ..h.h...
    decimal
              1    0  104    0  104    0  204    0
    datetime (2012-08-19T17:48:48)
    0000   0xb0 0x30 0x51 0x73 0x0c                   .0Qs.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2012-08-19T18:40:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-19T18:40:07)
    0000   0x87 0x28 0x12 0x73 0x0c                   .(.s.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 2.6, 'curve': 4},
 {'age': 146, 'amount': 0.8, 'curve': 4},
 {'age': 156, 'amount': 0.65, 'curve': 5},
 {'age': 166, 'amount': 1.15, 'curve': 4},
 {'age': 40, 'amount': 3.7, 'curve': 20},
 {'age': 90, 'amount': 2.9, 'curve': 20},
 {'age': 130, 'amount': 2.6, 'curve': 20},
 {'age': 220, 'amount': 3.1, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x68 0x38 0x04 0x20 0x92 0x04    \.h8. ..
    0008   0x1a 0x9c 0x05 0x2e 0xa6 0x04 0x94 0x28    .......(
    0010   0x14 0x74 0x5a 0x14 0x68 0x82 0x14 0x7c    .tZ.h..|
    0018   0xdc 0x14                                  ..
    decimal
             92   26  104   56    4   32  146    4
             26  156    5   46  166    4  148   40
             20  116   90   20  104  130   20  124
            220   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-08-19T18:40:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0xb8 0x00    ........
    decimal
              1    0  144    0  144    0  184    0
    datetime (2012-08-19T18:40:07)
    0000   0x87 0x28 0x52 0x73 0x0c                   .(Rs.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2012-08-19T20:07:02 head[2], body[15] op[0x5b]
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
    datetime (2012-08-19T20:07:02)
    0000   0x82 0x07 0x14 0x73 0x0c                   ...s.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 3.6, 'curve': 4},
 {'age': 143, 'amount': 2.6, 'curve': 4},
 {'age': 233, 'amount': 0.8, 'curve': 4},
 {'age': 243, 'amount': 0.65, 'curve': 5},
 {'age': 253, 'amount': 1.15, 'curve': 4},
 {'age': 127, 'amount': 3.7, 'curve': 20},
 {'age': 177, 'amount': 2.9, 'curve': 20},
 {'age': 217, 'amount': 2.6, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x90 0x5d 0x04 0x68 0x8f 0x04    \..].h..
    0008   0x20 0xe9 0x04 0x1a 0xf3 0x05 0x2e 0xfd     .......
    0010   0x04 0x94 0x7f 0x14 0x74 0xb1 0x14 0x68    ....t..h
    0018   0xd9 0x14                                  ..
    decimal
             92   26  144   93    4  104  143    4
             32  233    4   26  243    5   46  253
              4  148  127   20  116  177   20  104
            217   20
    datetime (unknown)

    body (0)

#### RECORD 8 CalBGForPH 2012-08-19T20:08:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2012-08-19T20:08:36)
    0000   0xa4 0x08 0x34 0x73 0x0c                   ..4s.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 9 Ian3F 2012-08-19T20:08:36 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2012-08-19T20:08:36)
    0000   0xa4 0x08 0xd4 0x73 0x0c                   ...s.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 10 Bolus 2012-08-19T20:07:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x80 0x00    ..|.|...
    decimal
              1    0  124    0  124    0  128    0
    datetime (2012-08-19T20:07:03)
    0000   0x83 0x07 0x54 0x73 0x0c                   ..Ts.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 11 BolusWizard 2012-08-19T21:54:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-19T21:54:57)
    0000   0xb9 0x36 0x15 0x73 0x0c                   .6.s.
    body (15)
    hex
    0000   0x13 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x36         D....D6
    decimal
             19  144    0  110   23   54    0    0
             68    0    0    0    0   68   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 110, 'amount': 3.1, 'curve': 4},
 {'age': 200, 'amount': 3.6, 'curve': 4},
 {'age': 250, 'amount': 2.6, 'curve': 4},
 {'age': 84, 'amount': 0.8, 'curve': 20},
 {'age': 94, 'amount': 0.65, 'curve': 21},
 {'age': 104, 'amount': 1.15, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x7c 0x6e 0x04 0x90 0xc8 0x04    \.|n....
    0008   0x68 0xfa 0x04 0x20 0x54 0x14 0x1a 0x5e    h.. T..^
    0010   0x15 0x2e 0x68 0x14                        ..h.
    decimal
             92   20  124  110    4  144  200    4
            104  250    4   32   84   20   26   94
             21   46  104   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2012-08-19T21:54:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x54 0x00    ..D.D.T.
    decimal
              1    0   68    0   68    0   84    0
    datetime (2012-08-19T21:54:57)
    0000   0xb9 0x36 0x55 0x73 0x0c                   .6Us.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 BolusWizard 2012-08-19T22:02:06 head[2], body[15] op[0x5b]
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
    datetime (2012-08-19T22:02:06)
    0000   0x86 0x02 0x16 0x73 0x0c                   ...s.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    DAY BITS: [0, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 1.7, 'curve': 4},
 {'age': 118, 'amount': 3.1, 'curve': 4},
 {'age': 208, 'amount': 3.6, 'curve': 4},
 {'age': 2, 'amount': 2.6, 'curve': 20},
 {'age': 92, 'amount': 0.8, 'curve': 20},
 {'age': 102, 'amount': 0.65, 'curve': 21},
 {'age': 112, 'amount': 1.15, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x44 0x08 0x04 0x7c 0x76 0x04    \.D..|v.
    0008   0x90 0xd0 0x04 0x68 0x02 0x14 0x20 0x5c    ...h.. \
    0010   0x14 0x1a 0x66 0x15 0x2e 0x70 0x14         ..f..p.
    decimal
             92   23   68    8    4  124  118    4
            144  208    4  104    2   20   32   92
             20   26  102   21   46  112   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2012-08-19T22:02:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x90 0x00    ..4.4...
    decimal
              1    0   52    0   52    0  144    0
    datetime (2012-08-19T22:02:06)
    0000   0x86 0x02 0x56 0x73 0x0c                   ..Vs.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2012-08-19T22:23:53 head[2], body[15] op[0x5b]
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
    datetime (2012-08-19T22:23:53)
    0000   0xb5 0x17 0x16 0x73 0x0c                   ...s.
    body (15)
    hex
    0000   0x2f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    /..n.6..
    0008   0xa8 0x00 0x00 0x00 0x00 0xa8 0x36         ......6
    decimal
             47  144    0  110   23   54    0    0
            168    0    0    0    0  168   54
    DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 3.0, 'curve': 4},
 {'age': 139, 'amount': 3.1, 'curve': 4},
 {'age': 229, 'amount': 3.6, 'curve': 4},
 {'age': 23, 'amount': 2.6, 'curve': 20},
 {'age': 113, 'amount': 0.8, 'curve': 20},
 {'age': 123, 'amount': 0.65, 'curve': 21},
 {'age': 133, 'amount': 1.15, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x78 0x1d 0x04 0x7c 0x8b 0x04    \.x..|..
    0008   0x90 0xe5 0x04 0x68 0x17 0x14 0x20 0x71    ...h.. q
    0010   0x14 0x1a 0x7b 0x15 0x2e 0x85 0x14         ..{....
    decimal
             92   23  120   29    4  124  139    4
            144  229    4  104   23   20   32  113
             20   26  123   21   46  133   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2012-08-19T22:23:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0xa8 0x00    ........
    decimal
              1    0  132    0  132    0  168    0
    datetime (2012-08-19T22:23:53)
    0000   0xb5 0x17 0x56 0x73 0x0c                   ..Vs.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 20 BasalProfileStart 2012-08-20T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-20T00:00:00)
    0000   0x80 0x00 0x00 0x14 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 21 ResultTotals 2008-08-05T00:12:19 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x7b                   ....{
    decimal
              7    0    0    8  123
    datetime (2008-08-05T00:12:19)
    0000   0x93 0x0c 0x00 0x05 0x08                   .....
    body (0)

#### RECORD 22 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x93 0x0c 0x06 0x00 0x56 0x56 0x56    n....VVV
    0008   0x01 0x00 0x00 0x08 0x7b 0x02 0x4b 0x1b    ....{.K.
    0010   0x06 0x30 0x49 0x01 0x94 0x05 0x20 0x00    .0I... .
    0018   0x00 0x00 0x68 0x00 0xa8 0x0c 0x00 0x01    ..h.....
    0020   0x02 0x50 0x00 0x00 0x00 0x00 0x00 0x00    .P......
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  147   12    6    0   86   86   86
              1    0    0    8  123    2   75   27
              6   48   73    1  148    5   32    0
              0    0  104    0  168   12    0    1
              2   80    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x40                   ....@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 23 BolusWizard 2012-08-20T00:59:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 34,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T00:59:50)
    0000   0xb2 0x3b 0x00 0x74 0x0c                   .;.t.
    body (15)
    hex
    0000   0x22 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    "..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             34  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 3.1, 'curve': 4},
 {'age': 165, 'amount': 0.2, 'curve': 4},
 {'age': 185, 'amount': 3.0, 'curve': 4},
 {'age': 39, 'amount': 3.1, 'curve': 20},
 {'age': 129, 'amount': 3.6, 'curve': 20},
 {'age': 179, 'amount': 2.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x7c 0x9b 0x04 0x08 0xa5 0x04    \.|.....
    0008   0x78 0xb9 0x04 0x7c 0x27 0x14 0x90 0x81    x..|'...
    0010   0x14 0x68 0xb3 0x14                        .h..
    decimal
             92   20  124  155    4    8  165    4
            120  185    4  124   39   20  144  129
             20  104  179   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2012-08-20T00:59:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x38 0x00    ......8.
    decimal
              1    0  168    0  168    0   56    0
    datetime (2012-08-20T00:59:50)
    0000   0xb2 0x3b 0x40 0x74 0x0c                   .;@t.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 BasalProfileStart 2012-08-20T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-20T04:00:00)
    0000   0x80 0x00 0x04 0x14 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 27 CalBGForPH 2012-08-20T07:33:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2012-08-20T07:33:58)
    0000   0xba 0x21 0x27 0x74 0x0c                   .!'t.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 28 Ian3F 2012-08-20T07:33:58 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2012-08-20T07:33:58)
    0000   0xba 0x21 0xe7 0x74 0x0c                   .!.t.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 29 BolusWizard 2012-08-20T07:34:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 70,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 2.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2012-08-20T07:34:07)
    0000   0x87 0x22 0x07 0x74 0x0c                   .".t.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x18 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x18 0x36         ......6
    decimal
              0  144    0  110   23   54   24    0
              0    0    0    0    0   24   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 4.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0x90 0x14                   \....
    decimal
             92    5  168  144   20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-08-20T07:34:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x00 0x00    ........
    decimal
              1    0   24    0   24    0    0    0
    datetime (2012-08-20T07:34:07)
    0000   0x87 0x22 0x47 0x74 0x0c                   ."Gt.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2012-08-20T08:06:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T08:06:03)
    0000   0x83 0x06 0x08 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 0.6, 'curve': 4},
 {'age': 176, 'amount': 4.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0x20 0x04 0xa8 0xb0 0x14    \.. ....
    decimal
             92    8   24   32    4  168  176   20
    datetime (unknown)

    body (0)

#### RECORD 34 Ian69 2012-08-20T08:06:03 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-20T08:06:03)
    0000   0x83 0x06 0x08 0x14 0x0c                   .....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30

#### RECORD 35 Bolus 2012-08-20T08:06:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x18 0x00    ........
    decimal
              1    0  144    0  144    0   24    0
    datetime (2012-08-20T08:06:03)
    0000   0x83 0x06 0x48 0x74 0x0c                   ..Ht.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 36 BolusWizard 2012-08-20T08:31:17 head[2], body[15] op[0x5b]
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
    datetime (2012-08-20T08:31:17)
    0000   0x91 0x1f 0x08 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 3.6, 'curve': 4},
 {'age': 57, 'amount': 0.6, 'curve': 4},
 {'age': 201, 'amount': 4.2, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x90 0x1b 0x04 0x18 0x39 0x04    \.....9.
    0008   0xa8 0xc9 0x14                             ...
    decimal
             92   11  144   27    4   24   57    4
            168  201   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2012-08-20T08:31:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0xa0 0x00    ..0.0...
    decimal
              1    0   48    0   48    0  160    0
    datetime (2012-08-20T08:31:17)
    0000   0x91 0x1f 0x48 0x74 0x0c                   ..Ht.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 39 BasalProfileStart 2012-08-20T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-20T09:30:00)
    0000   0x80 0x1e 0x09 0x14 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 40 CalBGForPH 2012-08-20T09:52:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2012-08-20T09:52:22)
    0000   0x96 0x34 0x29 0x74 0x0c                   .4)t.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2012-08-20T09:52:22 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2012-08-20T09:52:22)
    0000   0x96 0x34 0xe9 0x74 0x0c                   .4.t.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 BolusWizard 2012-08-20T11:01:53 head[2], body[15] op[0x5b]
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
    datetime (2012-08-20T11:01:53)
    0000   0xb5 0x01 0x0b 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    DAY BITS: [0, 1, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 157, 'amount': 1.2, 'curve': 4},
 {'age': 177, 'amount': 3.6, 'curve': 4},
 {'age': 207, 'amount': 0.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x9d 0x04 0x90 0xb1 0x04    \.0.....
    0008   0x18 0xcf 0x04                             ...
    decimal
             92   11   48  157    4  144  177    4
             24  207    4
    datetime (unknown)

    body (0)

#### RECORD 44 Ian69 2012-08-20T11:01:53 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-20T11:01:53)
    0000   0xb5 0x01 0x0b 0x14 0x0c                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 45 Bolus 2012-08-20T11:01:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x2c 0x00    ..0.0.,.
    decimal
              1    0   48    0   48    0   44    0
    datetime (2012-08-20T11:01:53)
    0000   0xb5 0x01 0x4b 0x74 0x0c                   ..Kt.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 46 BolusWizard 2012-08-20T12:05:51 head[2], body[15] op[0x5b]
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
    datetime (2012-08-20T12:05:51)
    0000   0xb3 0x05 0x0c 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    DAY BITS: [0, 1, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 1.2, 'curve': 4},
 {'age': 221, 'amount': 1.2, 'curve': 4},
 {'age': 241, 'amount': 3.6, 'curve': 4},
 {'age': 15, 'amount': 0.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x30 0x47 0x04 0x30 0xdd 0x04    \.0G.0..
    0008   0x90 0xf1 0x04 0x18 0x0f 0x14              ......
    decimal
             92   14   48   71    4   48  221    4
            144  241    4   24   15   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2012-08-20T12:05:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x28 0x00    ..4.4.(.
    decimal
              1    0   52    0   52    0   40    0
    datetime (2012-08-20T12:05:51)
    0000   0xb3 0x05 0x4c 0x74 0x0c                   ..Lt.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2012-08-20T12:19:14 head[2], body[15] op[0x5b]
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
    datetime (2012-08-20T12:19:14)
    0000   0x8e 0x13 0x0c 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 1.3, 'curve': 4},
 {'age': 85, 'amount': 1.2, 'curve': 4},
 {'age': 235, 'amount': 1.2, 'curve': 4},
 {'age': 255, 'amount': 3.6, 'curve': 4},
 {'age': 29, 'amount': 0.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x34 0x0f 0x04 0x30 0x55 0x04    \.4..0U.
    0008   0x30 0xeb 0x04 0x90 0xff 0x04 0x18 0x1d    0.......
    0010   0x14                                       .
    decimal
             92   17   52   15    4   48   85    4
             48  235    4  144  255    4   24   29
             20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2012-08-20T12:19:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x58 0x00    ..|.|.X.
    decimal
              1    0  124    0  124    0   88    0
    datetime (2012-08-20T12:19:14)
    0000   0x8e 0x13 0x4c 0x74 0x0c                   ..Lt.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 52 BolusWizard 2012-08-20T12:42:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-20T12:42:49)
    0000   0xb1 0x2a 0x0c 0x74 0x0c                   .*.t.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 3.1, 'curve': 4},
 {'age': 38, 'amount': 1.3, 'curve': 4},
 {'age': 108, 'amount': 1.2, 'curve': 4},
 {'age': 2, 'amount': 1.2, 'curve': 20},
 {'age': 22, 'amount': 3.6, 'curve': 20},
 {'age': 52, 'amount': 0.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x7c 0x1c 0x04 0x34 0x26 0x04    \.|..4&.
    0008   0x30 0x6c 0x04 0x30 0x02 0x14 0x90 0x16    0l.0....
    0010   0x14 0x18 0x34 0x14                        ..4.
    decimal
             92   20  124   28    4   52   38    4
             48  108    4   48    2   20  144   22
             20   24   52   20
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2012-08-20T12:42:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xc0 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  192    0
    datetime (2012-08-20T12:42:50)
    0000   0xb2 0x2a 0x4c 0x74 0x0c                   .*Lt.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 BasalProfileStart 2012-08-20T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-20T13:00:00)
    0000   0x80 0x00 0x0d 0x14 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 56 CalBGForPH 2012-08-20T15:39:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 57}
```
    op hex (2)
    0000   0x0a 0x39                                  .9
    decimal
             10   57
    datetime (2012-08-20T15:39:38)
    0000   0xa6 0x27 0x4f 0x14 0x0c                   .'O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 BolusWizard 2012-08-20T15:39:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 57,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 4.0,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x39                                  [9
    decimal
             91   57
    datetime (2012-08-20T15:39:42)
    0000   0xaa 0x27 0x0f 0x74 0x0c                   .'.t.
    body (15)
    hex
    0000   0x10 0x90 0x00 0x6e 0x17 0x36 0x04 0x00    ...n.6..
    0008   0x38 0x00 0x00 0x28 0x00 0x38 0x36         8..(.86
    decimal
             16  144    0  110   23   54    4    0
             56    0    0   40    0   56   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 175, 'amount': 1.25, 'curve': 4},
 {'age': 185, 'amount': 1.75, 'curve': 4},
 {'age': 205, 'amount': 3.1, 'curve': 4},
 {'age': 215, 'amount': 1.3, 'curve': 4},
 {'age': 29, 'amount': 1.2, 'curve': 20},
 {'age': 179, 'amount': 1.2, 'curve': 20},
 {'age': 199, 'amount': 3.6, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x32 0xaf 0x04 0x46 0xb9 0x04    \.2..F..
    0008   0x7c 0xcd 0x04 0x34 0xd7 0x04 0x30 0x1d    |..4..0.
    0010   0x14 0x30 0xb3 0x14 0x90 0xc7 0x14         .0.....
    decimal
             92   23   50  175    4   70  185    4
            124  205    4   52  215    4   48   29
             20   48  179   20  144  199   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2012-08-20T15:39:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x28 0x00    ..8.8.(.
    decimal
              1    0   56    0   56    0   40    0
    datetime (2012-08-20T15:39:42)
    0000   0xaa 0x27 0x4f 0x74 0x0c                   .'Ot.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 BolusWizard 2012-08-20T16:12:39 head[2], body[15] op[0x5b]
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
    datetime (2012-08-20T16:12:39)
    0000   0xa7 0x0c 0x10 0x74 0x0c                   ...t.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    DAY BITS: [0, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 1.4, 'curve': 4},
 {'age': 208, 'amount': 1.25, 'curve': 4},
 {'age': 218, 'amount': 1.75, 'curve': 4},
 {'age': 238, 'amount': 3.1, 'curve': 4},
 {'age': 248, 'amount': 1.3, 'curve': 4},
 {'age': 62, 'amount': 1.2, 'curve': 20},
 {'age': 212, 'amount': 1.2, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x38 0x26 0x04 0x32 0xd0 0x04    \.8&.2..
    0008   0x46 0xda 0x04 0x7c 0xee 0x04 0x34 0xf8    F..|..4.
    0010   0x04 0x30 0x3e 0x14 0x30 0xd4 0x14         .0>.0..
    decimal
             92   23   56   38    4   50  208    4
             70  218    4  124  238    4   52  248
              4   48   62   20   48  212   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2012-08-20T16:12:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x48 0x00    ..X.X.H.
    decimal
              1    0   88    0   88    0   72    0
    datetime (2012-08-20T16:12:39)
    0000   0xa7 0x0c 0x50 0x74 0x0c                   ..Pt.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 63 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x60                                  .`
    decimal
              0   96
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-18.data: 64 records`
