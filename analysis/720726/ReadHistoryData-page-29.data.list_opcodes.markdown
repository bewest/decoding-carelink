## START analysis/ianj/raw//ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 1016, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xdf 0xe4                                  ..
##### DEBUG DECIMAL
            223  228
#### RECORD 0 BolusWizard 2013-08-02T19:48:46 head[2], body[15] op[0x5b]
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
    datetime (2013-08-02T19:48:46)
    0000   0xae 0x30 0x13 0x62 0x0d                   .0.b.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54    0    0
              0    0    0    0    0    0   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 1.0, 'curve': 4},
 {'age': 83, 'amount': 2.7, 'curve': 4},
 {'age': 87, 'amount': 1.2, 'curve': 20},
 {'age': 187, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x35 0x04 0x6c 0x53 0x04    \.(5.lS.
    0008   0x30 0x57 0x14 0x6c 0xbb 0x14              0W.l..
    decimal
             92   14   40   53    4  108   83    4
             48   87   20  108  187   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-08-02T19:48:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x70 0x00    ..T.T.p.
    decimal
              1    0   84    0   84    0  112    0
    datetime (2013-08-02T19:48:46)
    0000   0xae 0x30 0x53 0x62 0x0d                   .0Sb.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-08-02T21:25:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-08-02T21:25:28)
    0000   0x9c 0x19 0x35 0x62 0x0d                   ..5b.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 4 Ian3F 2013-08-02T21:25:28 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2013-08-02T21:25:28)
    0000   0x9c 0x19 0xd5 0x62 0x0d                   ...b.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2013-08-02T21:41:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 31,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 112}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-02T21:41:37)
    0000   0xa5 0x29 0x15 0x62 0x0d                   .).b.
    body (15)
    hex
    0000   0x1f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x70 0x00 0x00 0x00 0x00 0x70 0x36         p....p6
    decimal
             31  144    0  110   23   54    0    0
            112    0    0    0    0  112   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 116, 'amount': 2.1, 'curve': 4},
 {'age': 166, 'amount': 1.0, 'curve': 4},
 {'age': 196, 'amount': 2.7, 'curve': 4},
 {'age': 200, 'amount': 1.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x54 0x74 0x04 0x28 0xa6 0x04    \.Tt.(..
    0008   0x6c 0xc4 0x04 0x30 0xc8 0x14              l..0..
    decimal
             92   14   84  116    4   40  166    4
            108  196    4   48  200   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-08-02T21:41:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x40 0x00    ..p.p.@.
    decimal
              1    0  112    0  112    0   64    0
    datetime (2013-08-02T21:41:37)
    0000   0xa5 0x29 0x55 0x62 0x0d                   .)Ub.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 BasalProfileStart 2013-08-03T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-03T00:00:00)
    0000   0x80 0x00 0x00 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 9 ResultTotals (2000, 8, 0, 0, 13, 2) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x4d                   ....M
    decimal
              7    0    0    6   77
    datetime ((2000, 8, 0, 0, 13, 2))
    0000   0x82 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 10 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x82 0x0d 0x06 0x00 0x70 0x46 0xa7    n....pF.
    0008   0x03 0x00 0x00 0x06 0x4d 0x03 0x89 0x38    ....M..8
    0010   0x02 0xc4 0x2c 0x00 0x9d 0x02 0x30 0x00    ..,...0.
    0018   0x94 0x00 0x00 0x00 0x00 0x07 0x02 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  130   13    6    0  112   70  167
              3    0    0    6   77    3  137   56
              2  196   44    0  157    2   48    0
            148    0    0    0    0    7    2    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 11 BolusWizard 2013-08-03T00:01:13 head[2], body[15] op[0x5b]
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
    datetime (2013-08-03T00:01:13)
    0000   0x8d 0x01 0x00 0x63 0x0d                   ...c.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 146, 'amount': 2.8, 'curve': 4},
 {'age': 0, 'amount': 2.1, 'curve': 20},
 {'age': 50, 'amount': 1.0, 'curve': 20},
 {'age': 80, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x70 0x92 0x04 0x54 0x00 0x14    \.p..T..
    0008   0x28 0x32 0x14 0x6c 0x50 0x14              (2.lP.
    decimal
             92   14  112  146    4   84    0   20
             40   50   20  108   80   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-08-03T00:01:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x24 0x00    ..|.|.$.
    decimal
              1    0  124    0  124    0   36    0
    datetime (2013-08-03T00:01:13)
    0000   0x8d 0x01 0x40 0x63 0x0d                   ..@c.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 14 CalBGForPH 2013-08-03T01:55:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 306}
```
    op hex (2)
    0000   0x0a 0x32                                  .2
    decimal
             10   50
    datetime (2013-08-03T01:55:50)
    0000   0xb2 0x37 0x21 0x63 0x8d                   .7!c.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 Ian3F 2013-08-03T01:55:50 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x26                                  ?&
    decimal
             63   38
    datetime (2013-08-03T01:55:50)
    0000   0xb2 0x37 0x41 0x63 0x0d                   .7Ac.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2013-08-03T01:55:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 170,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 20.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2013-08-03T01:55:57)
    0000   0xb9 0x37 0x01 0x63 0x0d                   .7.c.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xc8 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x3c 0x00 0x8c 0x36         ...<..6
    decimal
              0  144    0  110   23   54  200    0
              0    0    0   60    0  140   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 120, 'amount': 3.1, 'curve': 4},
 {'age': 4, 'amount': 2.8, 'curve': 20},
 {'age': 114, 'amount': 2.1, 'curve': 20},
 {'age': 164, 'amount': 1.0, 'curve': 20},
 {'age': 194, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x7c 0x78 0x04 0x70 0x04 0x14    \.|x.p..
    0008   0x54 0x72 0x14 0x28 0xa4 0x14 0x6c 0xc2    Tr.(..l.
    0010   0x14                                       .
    decimal
             92   17  124  120    4  112    4   20
             84  114   20   40  164   20  108  194
             20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-08-03T01:55:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x3c 0x00    ......<.
    decimal
              1    0  160    0  160    0   60    0
    datetime (2013-08-03T01:55:57)
    0000   0xb9 0x37 0x41 0x63 0x0d                   .7Ac.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 BasalProfileStart 2013-08-03T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-03T04:00:00)
    0000   0x80 0x00 0x04 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 20 CalBGForPH 2013-08-03T08:58:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-08-03T08:58:52)
    0000   0xb4 0x3a 0x28 0x63 0x0d                   .:(c.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 Ian3F 2013-08-03T08:58:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2013-08-03T08:58:52)
    0000   0xb4 0x3a 0x48 0x63 0x0d                   .:Hc.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2013-08-03T08:59:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-08-03T08:59:02)
    0000   0x82 0x3b 0x08 0x63 0x0d                   .;.c.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x5c 0x00    ...n.6\.
    0008   0x00 0x00 0x00 0x00 0x00 0x5c 0x36         .....\6
    decimal
              0  144    0  110   23   54   92    0
              0    0    0    0    0   92   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 168, 'amount': 4.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0xa8 0x14                   \....
    decimal
             92    5  160  168   20
    datetime (unknown)

    body (0)

#### RECORD 24 Ian69 2013-08-03T08:59:02 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-03T08:59:02)
    0000   0x82 0x3b 0x08 0x03 0x0d                   .;...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 0, 1]
#### RECORD 25 Bolus 2013-08-03T08:59:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x00 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    0    0
    datetime (2013-08-03T08:59:02)
    0000   0x82 0x3b 0x48 0x63 0x0d                   .;Hc.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 CalBGForPH 2013-08-03T09:21:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-08-03T09:21:54)
    0000   0xb6 0x15 0x29 0x63 0x0d                   ..)c.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 27 Ian3F 2013-08-03T09:21:54 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-08-03T09:21:54)
    0000   0xb6 0x15 0x49 0x63 0x0d                   ..Ic.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 28 BasalProfileStart 2013-08-03T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-03T09:30:00)
    0000   0x80 0x1e 0x09 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 29 CalBGForPH 2013-08-03T10:20:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-08-03T10:20:36)
    0000   0xa4 0x14 0x4a 0x03 0x0d                   ..J..
    body (0)

#### RECORD 30 BolusWizard 2013-08-03T10:20:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 89,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-08-03T10:20:39)
    0000   0xa7 0x14 0x0a 0x63 0x0d                   ...c.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x3c 0x00    ...n.6<.
    0008   0x00 0x00 0x00 0x40 0x00 0x00 0x36         ...@..6
    decimal
              0  144    0  110   23   54   60    0
              0    0    0   64    0    0   54
    DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 2.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x55 0x04                   \.\U.
    decimal
             92    5   92   85    4
    datetime (unknown)

    body (0)

#### RECORD 32 BolusWizard 2013-08-03T10:20:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 89,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-08-03T10:20:46)
    0000   0xae 0x14 0x0a 0x63 0x0d                   ...c.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x3c 0x00    ...n.6<.
    0008   0x00 0x00 0x00 0x40 0x00 0x00 0x36         ...@..6
    decimal
              0  144    0  110   23   54   60    0
              0    0    0   64    0    0   54
    DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 2.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x55 0x04                   \.\U.
    decimal
             92    5   92   85    4
    datetime (unknown)

    body (0)

#### RECORD 34 PumpSuspend 2013-08-03T10:20:47 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-08-03T10:20:47)
    0000   0xaf 0x14 0x0a 0x03 0x0d                   .....
    body (0)

#### RECORD 35 Bolus 2013-08-03T10:20:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x02 0x00 0x40 0x00    ..t...@.
    decimal
              1    0  116    0    2    0   64    0
    datetime (2013-08-03T10:20:46)
    0000   0xae 0x14 0x4a 0x63 0x0d                   ..Jc.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 36 BasalProfileStart 2013-08-03T10:20:51 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-03T10:20:51)
    0000   0xb3 0x14 0x0a 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 37 PumpResume 2013-08-03T10:20:51 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-08-03T10:20:51)
    0000   0xb3 0x14 0x0a 0x03 0x0d                   .....
    body (0)

#### RECORD 38 BolusWizard 2013-08-03T10:21:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 89,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.8,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-08-03T10:21:00)
    0000   0x80 0x15 0x0a 0x63 0x0d                   ...c.
    body (15)
    hex
    0000   0x17 0x90 0x00 0x6e 0x17 0x36 0x3c 0x00    ...n.6<.
    0008   0x50 0x00 0x00 0x44 0x00 0x50 0x36         P..D.P6
    decimal
             23  144    0  110   23   54   60    0
             80    0    0   68    0   80   54
    DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 0.05, 'curve': 4},
 {'age': 86, 'amount': 2.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x02 0x06 0x04 0x5c 0x56 0x04    \....\V.
    decimal
             92    8    2    6    4   92   86    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-08-03T10:21:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x44 0x00    ..P.P.D.
    decimal
              1    0   80    0   80    0   68    0
    datetime (2013-08-03T10:21:00)
    0000   0x80 0x15 0x4a 0x63 0x0d                   ..Jc.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 41 BolusWizard 2013-08-03T11:27:17 head[2], body[15] op[0x5b]
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
    datetime (2013-08-03T11:27:17)
    0000   0x91 0x1b 0x0b 0x63 0x0d                   ...c.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 2.05, 'curve': 4},
 {'age': 152, 'amount': 2.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x52 0x48 0x04 0x5c 0x98 0x04    \.RH.\..
    decimal
             92    8   82   72    4   92  152    4
    datetime (unknown)

    body (0)

#### RECORD 43 Ian69 2013-08-03T11:27:17 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-03T11:27:17)
    0000   0x91 0x1b 0x0b 0x03 0x0d                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 44 LowReservoir 2013-08-03T11:27:17 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.4}
```
    op hex (2)
    0000   0x34 0x68                                  4h
    decimal
             52  104
    datetime (2013-08-03T11:27:17)
    0000   0x91 0x1b 0x2b 0x03 0x8d                   ..+..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 45 Bolus 2013-08-03T11:27:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x58 0x00    ..l.l.X.
    decimal
              1    0  108    0  108    0   88    0
    datetime (2013-08-03T11:27:17)
    0000   0x91 0x1b 0x4b 0x63 0x0d                   ..Kc.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 46 BasalProfileStart 2013-08-03T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-03T13:00:00)
    0000   0x80 0x00 0x0d 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 47 CalBGForPH 2013-08-03T15:26:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-08-03T15:26:18)
    0000   0x92 0x1a 0x2f 0x63 0x0d                   ../c.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 48 Ian3F 2013-08-03T15:26:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2013-08-03T15:26:18)
    0000   0x92 0x1a 0xcf 0x63 0x0d                   ...c.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2013-08-03T15:56:13 head[2], body[15] op[0x5b]
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
    datetime (2013-08-03T15:56:13)
    0000   0x8d 0x38 0x0f 0x63 0x0d                   .8.c.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 2.7, 'curve': 20},
 {'age': 85, 'amount': 2.05, 'curve': 20},
 {'age': 165, 'amount': 2.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0x0f 0x14 0x52 0x55 0x14    \.l..RU.
    0008   0x5c 0xa5 0x14                             \..
    decimal
             92   11  108   15   20   82   85   20
             92  165   20
    datetime (unknown)

    body (0)

#### RECORD 51 LowReservoir 2013-08-03T15:56:13 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 6.4}
```
    op hex (2)
    0000   0x34 0x40                                  4@
    decimal
             52   64
    datetime (2013-08-03T15:56:13)
    0000   0x8d 0x38 0x0f 0x03 0x8d                   .8...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 52 Bolus 2013-08-03T15:56:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x00 0x00    ........
    decimal
              1    0  144    0  144    0    0    0
    datetime (2013-08-03T15:56:13)
    0000   0x8d 0x38 0x4f 0x63 0x0d                   .8Oc.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 53 BolusWizard 2013-08-03T18:04:45 head[2], body[15] op[0x5b]
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
    datetime (2013-08-03T18:04:45)
    0000   0xad 0x04 0x12 0x63 0x0d                   ...c.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 129, 'amount': 3.6, 'curve': 4},
 {'age': 143, 'amount': 2.7, 'curve': 20},
 {'age': 213, 'amount': 2.05, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x90 0x81 0x04 0x6c 0x8f 0x14    \....l..
    0008   0x52 0xd5 0x14                             R..
    decimal
             92   11  144  129    4  108  143   20
             82  213   20
    datetime (unknown)

    body (0)

#### RECORD 55 Ian69 2013-08-03T18:04:45 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-03T18:04:45)
    0000   0xad 0x04 0x72 0x03 0x0d                   ..r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 56 Bolus 2013-08-03T18:04:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x3c 0x00    ..P.P.<.
    decimal
              1    0   80    0   80    0   60    0
    datetime (2013-08-03T18:04:45)
    0000   0xad 0x04 0x52 0x63 0x0d                   ..Rc.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 57 CalBGForPH 2013-08-03T21:47:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2013-08-03T21:47:10)
    0000   0x8a 0x2f 0x35 0x63 0x0d                   ./5c.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 Ian3F 2013-08-03T21:47:10 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2013-08-03T21:47:10)
    0000   0x8a 0x2f 0x35 0x63 0x0d                   ./5c.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 BolusWizard 2013-08-03T21:47:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 85,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
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
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2013-08-03T21:47:26)
    0000   0x9a 0x2f 0x15 0x63 0x0d                   ./.c.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x34 0x00    (..n.64.
    0008   0x90 0x00 0x00 0x08 0x00 0xbc 0x36         ......6
    decimal
             40  144    0  110   23   54   52    0
            144    0    0    8    0  188   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 222, 'amount': 1.65, 'curve': 4},
 {'age': 232, 'amount': 0.35, 'curve': 4},
 {'age': 96, 'amount': 3.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x42 0xde 0x04 0x0e 0xe8 0x04    \.B.....
    0008   0x90 0x60 0x14                             .`.
    decimal
             92   11   66  222    4   14  232    4
            144   96   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-08-03T21:47:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 18.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xbc 0x00 0xbc 0x00 0x08 0x00    ........
    decimal
              1    0  188    0  188    0    8    0
    datetime (2013-08-03T21:47:26)
    0000   0x9a 0x2f 0x55 0x63 0x0d                   ./Uc.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 Rewind 2013-08-03T21:51:41 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-03T21:51:41)
    0000   0xa9 0x33 0x15 0x03 0x0d                   .3...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 Prime 2013-08-03T21:52:23 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x0d                   .....
    decimal
              3    0    0    0   13
    datetime (2013-08-03T21:52:23)
    0000   0x97 0x34 0x35 0x03 0x0d                   .45..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 BasalProfileStart 2013-08-03T21:52:32 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-03T21:52:32)
    0000   0xa0 0x34 0x15 0x03 0x0d                   .4...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 0, 1]
#### RECORD 65 BolusWizard 2013-08-03T22:13:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-03T22:13:50)
    0000   0xb2 0x0d 0x16 0x63 0x0d                   ...c.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    DAY BITS: [0, 1, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 4.7, 'curve': 4},
 {'age': 248, 'amount': 1.65, 'curve': 4},
 {'age': 2, 'amount': 0.35, 'curve': 20},
 {'age': 122, 'amount': 3.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xbc 0x1c 0x04 0x42 0xf8 0x04    \....B..
    0008   0x0e 0x02 0x14 0x90 0x7a 0x14              ....z.
    decimal
             92   14  188   28    4   66  248    4
             14    2   20  144  122   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-08-03T22:13:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0xb4 0x00    ..L.L...
    decimal
              1    0   76    0   76    0  180    0
    datetime (2013-08-03T22:13:50)
    0000   0xb2 0x0d 0x56 0x63 0x0d                   ..Vc.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 68 BasalProfileStart 2013-08-04T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-04T00:00:00)
    0000   0x80 0x00 0x00 0x04 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 69 ResultTotals (2000, 8, 0, 0, 13, 3) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xa6                   .....
    decimal
              7    0    0    7  166
    datetime ((2000, 8, 0, 0, 13, 3))
    0000   0x83 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 70 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x83 0x0d 0x06 0x10 0xb4 0x76 0x32    n.....v2
    0008   0x06 0x00 0x00 0x07 0xa6 0x03 0x88 0x2e    ........
    0010   0x04 0x1e 0x36 0x00 0xd3 0x02 0x64 0x00    ..6...d.
    0018   0xfe 0x00 0xbc 0x00 0x00 0x06 0x03 0x01    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0xa0 0xa0 0x00 0x00 0x00         .......
    decimal
            110  131   13    6   16  180  118   50
              6    0    0    7  166    3  136   46
              4   30   54    0  211    2  100    0
            254    0  188    0    0    6    3    1
              0    0    0    0    0    0    0    0
              0    0  160  160    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 71 CalBGForPH 2013-08-04T00:04:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-08-04T00:04:04)
    0000   0x84 0x04 0x20 0x64 0x0d                   .. d.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 72 Ian3F 2013-08-04T00:04:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2013-08-04T00:04:04)
    0000   0x84 0x04 0x60 0x64 0x0d                   ..`d.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 73 BasalProfileStart 2013-08-04T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-04T04:00:00)
    0000   0x80 0x00 0x04 0x04 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 74 NoDelivery 2013-08-04T08:13:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2013-08-04T08:13:00)
    0000   0x80 0x0d 0x48 0xa4 0x0d                   ..H..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 75 ClearAlarm 2013-08-04T08:19:12 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2013-08-04T08:19:12)
    0000   0x8c 0x13 0x08 0x04 0x0d                   .....
    body (0)

#### RECORD 76 BasalProfileStart 2013-08-04T08:19:12 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-04T08:19:12)
    0000   0x8c 0x13 0x08 0x04 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 77 CalBGForPH 2013-08-04T08:35:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2013-08-04T08:35:50)
    0000   0xb2 0x23 0x28 0x64 0x8d                   .#(d.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
`end analysis/ianj/raw//ReadHistoryData-page-29.data: 78 records`
