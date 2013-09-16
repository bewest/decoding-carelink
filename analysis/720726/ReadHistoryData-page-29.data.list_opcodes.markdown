## START logs/ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 376, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x82 0x3b 0x48 0x63 0x0d 0x0a 0x92 0xb6    .;Hc....
    0008   0x15 0x29 0x63 0x0d 0x3f 0x12 0xb6 0x15    .)c.?...
    0010   0x49 0x63 0x0d 0x69 0x69 0x96 0x7b 0x02    Ic.ii.{.
    0018   0x80 0x1e 0x09 0x03 0x0d 0x13 0x1e 0x00    ........
##### DEBUG DECIMAL
            130   59   72   99   13   10  146  182
             21   41   99   13   63   18  182   21
             73   99   13  105  105  150  123    2
            128   30    9    3   13   19   30    0
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

#### RECORD 24 Ian69 2013-08-03T08:59:02 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-03T08:59:02)
    0000   0x82 0x3b 0x08 0x03 0x0d                   .;...
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x5c 0x00 0x5c 0x00    ....\.\.
    decimal
             10   30    1    0   92    0   92    0
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-29.data: 25 records`
