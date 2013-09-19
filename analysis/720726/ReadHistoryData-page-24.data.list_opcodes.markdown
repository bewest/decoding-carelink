## START analysis/ianj/raw//ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 1016, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb5 0x0d                                  ..
##### DEBUG DECIMAL
            181   13
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x89 0x0d 0x06 0x10 0x9d 0x50 0x01    n.....P.
    0008   0x08 0x00 0x00 0x06 0xcd 0x03 0x89 0x34    .......4
    0010   0x03 0x44 0x30 0x00 0xbe 0x01 0xec 0x00    .D0.....
    0018   0x70 0x00 0xe8 0x00 0x00 0x07 0x02 0x01    p.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  137   13    6   16  157   80    1
              8    0    0    6  205    3  137   52
              3   68   48    0  190    1  236    0
            112    0  232    0    0    7    2    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 BolusWizard 2013-08-10T00:48:29 head[2], body[15] op[0x5b]
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
    datetime (2013-08-10T00:48:29)
    0000   0x9d 0x30 0x00 0x6a 0x0d                   .0.j.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 2.4, 'curve': 4},
 {'age': 143, 'amount': 1.4, 'curve': 4},
 {'age': 243, 'amount': 5.8, 'curve': 4},
 {'age': 147, 'amount': 1.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x60 0x67 0x04 0x38 0x8f 0x04    \.`g.8..
    0008   0xe8 0xf3 0x04 0x2c 0x93 0x14              ...,..
    decimal
             92   14   96  103    4   56  143    4
            232  243    4   44  147   20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2013-08-10T00:48:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x4c 0x00    ..@.@.L.
    decimal
              1    0   64    0   64    0   76    0
    datetime (2013-08-10T00:48:29)
    0000   0x9d 0x30 0x40 0x6a 0x0d                   .0@j.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 CalBGForPH 2013-08-10T01:21:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-08-10T01:21:45)
    0000   0xad 0x15 0x21 0x6a 0x0d                   ..!j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 5 Ian3F 2013-08-10T01:21:45 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2013-08-10T01:21:45)
    0000   0xad 0x15 0x01 0x6a 0x0d                   ...j.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2013-08-10T01:22:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 10.4,
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
    datetime (2013-08-10T01:22:09)
    0000   0x89 0x16 0x01 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    ...n.6$.
    0008   0x48 0x00 0x00 0x68 0x00 0x48 0x36         H..h.H6
    decimal
             20  144    0  110   23   54   36    0
             72    0    0  104    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 1.6, 'curve': 4},
 {'age': 137, 'amount': 2.4, 'curve': 4},
 {'age': 177, 'amount': 1.4, 'curve': 4},
 {'age': 21, 'amount': 5.8, 'curve': 20},
 {'age': 181, 'amount': 1.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x40 0x25 0x04 0x60 0x89 0x04    \.@%.`..
    0008   0x38 0xb1 0x04 0xe8 0x15 0x14 0x2c 0xb5    8.....,.
    0010   0x14                                       .
    decimal
             92   17   64   37    4   96  137    4
             56  177    4  232   21   20   44  181
             20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-08-10T01:22:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x68 0x00    ..0.0.h.
    decimal
              1    0   48    0   48    0  104    0
    datetime (2013-08-10T01:22:09)
    0000   0x89 0x16 0x41 0x6a 0x0d                   ..Aj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 9 BasalProfileStart 2013-08-10T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-10T04:00:00)
    0000   0x80 0x00 0x04 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 10 BasalProfileStart 2013-08-10T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-10T09:30:00)
    0000   0x80 0x1e 0x09 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 11 Ian69 2013-08-10T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-10T10:30:00)
    0000   0x80 0x1e 0x0a 0x0a 0x0d                   .....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30

#### RECORD 12 CalBGForPH 2013-08-10T10:45:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 59}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2013-08-10T10:45:31)
    0000   0x9f 0x2d 0x2a 0x6a 0x0d                   .-*j.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 Ian3F 2013-08-10T10:45:31 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2013-08-10T10:45:31)
    0000   0x9f 0x2d 0x6a 0x6a 0x0d                   .-jj.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 NoDelivery 2013-08-10T11:22:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2013-08-10T11:22:00)
    0000   0x80 0x16 0x4b 0xaa 0x0d                   ..K..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 15 ClearAlarm 2013-08-10T11:23:03 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2013-08-10T11:23:03)
    0000   0x83 0x17 0x0b 0x0a 0x0d                   .....
    body (0)

#### RECORD 16 BasalProfileStart 2013-08-10T11:23:03 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-10T11:23:03)
    0000   0x83 0x17 0x0b 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 17 BolusWizard 2013-08-10T11:23:14 head[2], body[15] op[0x5b]
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
    datetime (2013-08-10T11:23:14)
    0000   0x8e 0x17 0x0b 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 18 Ian69 2013-08-10T11:23:14 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-10T11:23:14)
    0000   0x8e 0x17 0x0b 0x0a 0x0d                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 19 Bolus 2013-08-10T11:23:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    0    0
    datetime (2013-08-10T11:23:14)
    0000   0x8e 0x17 0x4b 0x6a 0x0d                   ..Kj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 20 BasalProfileStart 2013-08-10T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-10T13:00:00)
    0000   0x80 0x00 0x0d 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 21 BolusWizard 2013-08-10T14:11:30 head[2], body[15] op[0x5b]
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
    datetime (2013-08-10T14:11:30)
    0000   0x9e 0x0b 0x0e 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 166, 'amount': 0.4, 'curve': 4},
 {'age': 176, 'amount': 2.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0xa6 0x04 0x68 0xb0 0x04    \....h..
    decimal
             92    8   16  166    4  104  176    4
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-08-10T14:11:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x18 0x00    ..|.|...
    decimal
              1    0  124    0  124    0   24    0
    datetime (2013-08-10T14:11:30)
    0000   0x9e 0x0b 0x4e 0x6a 0x0d                   ..Nj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 24 BolusWizard 2013-08-10T14:51:09 head[2], body[15] op[0x5b]
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
    datetime (2013-08-10T14:51:09)
    0000   0x89 0x33 0x0e 0x6a 0x0d                   .3.j.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 3.1, 'curve': 4},
 {'age': 206, 'amount': 0.4, 'curve': 4},
 {'age': 216, 'amount': 2.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x7c 0x2e 0x04 0x10 0xce 0x04    \.|.....
    0008   0x68 0xd8 0x04                             h..
    decimal
             92   11  124   46    4   16  206    4
            104  216    4
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-08-10T14:51:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x7c 0x00    ..h.h.|.
    decimal
              1    0  104    0  104    0  124    0
    datetime (2013-08-10T14:51:09)
    0000   0x89 0x33 0x4e 0x6a 0x0d                   .3Nj.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 27 CalBGForPH 2013-08-10T17:14:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 64}
```
    op hex (2)
    0000   0x0a 0x40                                  .@
    decimal
             10   64
    datetime (2013-08-10T17:14:35)
    0000   0xa3 0x0e 0x31 0x6a 0x0d                   ..1j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 28 Ian3F 2013-08-10T17:14:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2013-08-10T17:14:35)
    0000   0xa3 0x0e 0x11 0x6a 0x0d                   ...j.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 29 CalBGForPH 2013-08-10T18:24:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 179}
```
    op hex (2)
    0000   0x0a 0xb3                                  ..
    decimal
             10  179
    datetime (2013-08-10T18:24:39)
    0000   0xa7 0x18 0x32 0x6a 0x0d                   ..2j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 30 Ian3F 2013-08-10T18:24:39 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2013-08-10T18:24:39)
    0000   0xa7 0x18 0x72 0x6a 0x0d                   ..rj.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2013-08-10T18:25:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 99,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 7.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x63                                  [c
    decimal
             91   99
    datetime (2013-08-10T18:25:37)
    0000   0xa5 0x19 0x12 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x4c 0x00    ...n.6L.
    0008   0x64 0x00 0x00 0x08 0x00 0xa8 0x36         d.....6
    decimal
             28  144    0  110   23   54   76    0
            100    0    0    8    0  168   54
    DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 220, 'amount': 2.6, 'curve': 4},
 {'age': 4, 'amount': 3.1, 'curve': 20},
 {'age': 164, 'amount': 0.4, 'curve': 20},
 {'age': 174, 'amount': 2.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0xdc 0x04 0x7c 0x04 0x14    \.h..|..
    0008   0x10 0xa4 0x14 0x68 0xae 0x14              ...h..
    decimal
             92   14  104  220    4  124    4   20
             16  164   20  104  174   20
    datetime (unknown)

    body (0)

#### RECORD 33 Ian69 2013-08-10T18:25:37 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-10T18:25:37)
    0000   0xa5 0x19 0x72 0x0a 0x0d                   ..r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 34 Bolus 2013-08-10T18:25:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x08 0x00    ........
    decimal
              1    0  168    0  168    0    8    0
    datetime (2013-08-10T18:25:37)
    0000   0xa5 0x19 0x52 0x6a 0x0d                   ..Rj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2013-08-10T20:18:40 head[2], body[15] op[0x5b]
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
    datetime (2013-08-10T20:18:40)
    0000   0xa8 0x12 0x14 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 113, 'amount': 4.2, 'curve': 4},
 {'age': 77, 'amount': 2.6, 'curve': 20},
 {'age': 117, 'amount': 3.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa8 0x71 0x04 0x68 0x4d 0x14    \..q.hM.
    0008   0x7c 0x75 0x14                             |u.
    decimal
             92   11  168  113    4  104   77   20
            124  117   20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-08-10T20:18:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x58 0x00    ..h.h.X.
    decimal
              1    0  104    0  104    0   88    0
    datetime (2013-08-10T20:18:40)
    0000   0xa8 0x12 0x54 0x6a 0x0d                   ..Tj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 38 CalBGForPH 2013-08-10T23:24:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-08-10T23:24:11)
    0000   0x8b 0x18 0x37 0x6a 0x0d                   ..7j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 39 Ian3F 2013-08-10T23:24:11 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-08-10T23:24:11)
    0000   0x8b 0x18 0x57 0x6a 0x0d                   ..Wj.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 40 BolusWizard 2013-08-10T23:24:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 81,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 4.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x51                                  [Q
    decimal
             91   81
    datetime (2013-08-10T23:24:57)
    0000   0xb9 0x18 0x17 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x2c 0x00    ...n.6,.
    0008   0x00 0x00 0x00 0x10 0x00 0x1c 0x36         ......6
    decimal
              0  144    0  110   23   54   44    0
              0    0    0   16    0   28   54
    DAY BITS: [0, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 189, 'amount': 2.6, 'curve': 4},
 {'age': 43, 'amount': 4.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x68 0xbd 0x04 0xa8 0x2b 0x14    \.h...+.
    decimal
             92    8  104  189    4  168   43   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-08-10T23:24:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x10 0x00    ..D.D...
    decimal
              1    0   68    0   68    0   16    0
    datetime (2013-08-10T23:24:57)
    0000   0xb9 0x18 0x57 0x6a 0x0d                   ..Wj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 43 BasalProfileStart 2013-08-11T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-11T00:00:00)
    0000   0x80 0x00 0x00 0x0b 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 44 ResultTotals (2000, 8, 0, 0, 13, 10) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xa8                   .....
    decimal
              7    0    0    6  168
    datetime ((2000, 8, 0, 0, 13, 10))
    0000   0x8a 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 45 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x8a 0x0d 0x06 0x00 0x75 0x3b 0xb3    n....u;.
    0008   0x05 0x00 0x00 0x06 0xa8 0x03 0x88 0x35    .......5
    0010   0x03 0x20 0x2f 0x00 0xc4 0x02 0x34 0x00    . /...4.
    0018   0x44 0x00 0xa8 0x00 0x00 0x06 0x01 0x01    D.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  138   13    6    0  117   59  179
              5    0    0    6  168    3  136   53
              3   32   47    0  196    2   52    0
             68    0  168    0    0    6    1    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 46 BolusWizard 2013-08-11T00:54:28 head[2], body[15] op[0x5b]
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
    datetime (2013-08-11T00:54:28)
    0000   0x9c 0x36 0x00 0x6b 0x0d                   .6.k.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 89, 'amount': 1.65, 'curve': 4},
 {'age': 99, 'amount': 0.05, 'curve': 4},
 {'age': 23, 'amount': 2.6, 'curve': 20},
 {'age': 133, 'amount': 4.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x42 0x59 0x04 0x02 0x63 0x04    \.BY..c.
    0008   0x68 0x17 0x14 0xa8 0x85 0x14              h.....
    decimal
             92   14   66   89    4    2   99    4
            104   23   20  168  133   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-08-11T00:54:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x2c 0x00    ..X.X.,.
    decimal
              1    0   88    0   88    0   44    0
    datetime (2013-08-11T00:54:28)
    0000   0x9c 0x36 0x40 0x6b 0x0d                   .6@k.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2013-08-11T01:02:02 head[2], body[15] op[0x5b]
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
    datetime (2013-08-11T01:02:02)
    0000   0x82 0x02 0x01 0x6b 0x0d                   ...k.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 1.4, 'curve': 4},
 {'age': 17, 'amount': 0.8, 'curve': 4},
 {'age': 97, 'amount': 1.65, 'curve': 4},
 {'age': 107, 'amount': 0.05, 'curve': 4},
 {'age': 31, 'amount': 2.6, 'curve': 20},
 {'age': 141, 'amount': 4.2, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x38 0x07 0x04 0x20 0x11 0x04    \.8.. ..
    0008   0x42 0x61 0x04 0x02 0x6b 0x04 0x68 0x1f    Ba..k.h.
    0010   0x14 0xa8 0x8d 0x14                        ....
    decimal
             92   20   56    7    4   32   17    4
             66   97    4    2  107    4  104   31
             20  168  141   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-08-11T01:02:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x84 0x00    ..$.$...
    decimal
              1    0   36    0   36    0  132    0
    datetime (2013-08-11T01:02:02)
    0000   0x82 0x02 0x41 0x6b 0x0d                   ..Ak.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 52 BasalProfileStart 2013-08-11T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-11T04:00:00)
    0000   0x80 0x00 0x04 0x0b 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 53 BasalProfileStart 2013-08-11T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-11T09:30:00)
    0000   0x80 0x1e 0x09 0x0b 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 54 CalBGForPH 2013-08-11T10:14:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 62}
```
    op hex (2)
    0000   0x0a 0x3e                                  .>
    decimal
             10   62
    datetime (2013-08-11T10:14:51)
    0000   0xb3 0x0e 0x2a 0x6b 0x0d                   ..*k.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 55 Ian3F 2013-08-11T10:14:51 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2013-08-11T10:14:51)
    0000   0xb3 0x0e 0xca 0x6b 0x0d                   ...k.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 56 Ian69 2013-08-11T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-11T10:30:00)
    0000   0x80 0x1e 0x0a 0x0b 0x0d                   .....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30

#### RECORD 57 NoDelivery 2013-08-11T11:02:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2013-08-11T11:02:00)
    0000   0x80 0x02 0x4b 0xab 0x0d                   ..K..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 58 ClearAlarm 2013-08-11T11:06:06 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2013-08-11T11:06:06)
    0000   0x86 0x06 0x0b 0x0b 0x0d                   .....
    body (0)

#### RECORD 59 BasalProfileStart 2013-08-11T11:06:06 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-11T11:06:06)
    0000   0x86 0x06 0x0b 0x0b 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 60 BolusWizard 2013-08-11T11:56:14 head[2], body[15] op[0x5b]
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
    datetime (2013-08-11T11:56:14)
    0000   0x8e 0x38 0x0b 0x6b 0x0d                   .8.k.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 Ian69 2013-08-11T11:56:14 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-11T11:56:14)
    0000   0x8e 0x38 0x0b 0x0b 0x0d                   .8...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 62 Bolus 2013-08-11T11:56:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2013-08-11T11:56:14)
    0000   0x8e 0x38 0x4b 0x6b 0x0d                   .8Kk.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 BasalProfileStart 2013-08-11T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-11T13:00:00)
    0000   0x80 0x00 0x0d 0x0b 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 64 CalBGForPH 2013-08-11T14:57:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2013-08-11T14:57:05)
    0000   0x85 0x39 0x2e 0x6b 0x8d                   .9.k.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 65 Ian3F 2013-08-11T14:57:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x22                                  ?"
    decimal
             63   34
    datetime (2013-08-11T14:57:05)
    0000   0x85 0x39 0x8e 0x6b 0x0d                   .9.k.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 66 BolusWizard 2013-08-11T14:57:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 153,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 17.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2013-08-11T14:57:12)
    0000   0x8c 0x39 0x0e 0x6b 0x0d                   .9.k.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xac 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x14 0x00 0x98 0x36         ......6
    decimal
              0  144    0  110   23   54  172    0
              0    0    0   20    0  152   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 182, 'amount': 2.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0xb6 0x04                   \.l..
    decimal
             92    5  108  182    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-08-11T14:57:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x14 0x00    ........
    decimal
              1    0  152    0  152    0   20    0
    datetime (2013-08-11T14:57:12)
    0000   0x8c 0x39 0x4e 0x6b 0x0d                   .9Nk.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 69 BolusWizard 2013-08-11T16:39:30 head[2], body[15] op[0x5b]
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
    datetime (2013-08-11T16:39:30)
    0000   0x9e 0x27 0x10 0x6b 0x0d                   .'.k.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 3.8, 'curve': 4},
 {'age': 28, 'amount': 2.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x98 0x68 0x04 0x6c 0x1c 0x14    \..h.l..
    decimal
             92    8  152  104    4  108   28   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-08-11T16:39:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x58 0x00    ..T.T.X.
    decimal
              1    0   84    0   84    0   88    0
    datetime (2013-08-11T16:39:30)
    0000   0x9e 0x27 0x50 0x6b 0x0d                   .'Pk.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 72 LowReservoir 2013-08-11T16:42:37 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.0}
```
    op hex (2)
    0000   0x34 0x0a                                  4.
    decimal
             52   10
    datetime (2013-08-11T16:42:37)
    0000   0xa5 0x2a 0x10 0x0b 0x8d                   .*...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 73 BolusWizard 2013-08-11T17:40:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 36,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 128}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-11T17:40:56)
    0000   0xb8 0x28 0x11 0x6b 0x0d                   .(.k.
    body (15)
    hex
    0000   0x24 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    $..n.6..
    0008   0x80 0x00 0x00 0x00 0x00 0x80 0x36         ......6
    decimal
             36  144    0  110   23   54    0    0
            128    0    0    0    0  128   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
`end analysis/ianj/raw//ReadHistoryData-page-24.data: 74 records`
