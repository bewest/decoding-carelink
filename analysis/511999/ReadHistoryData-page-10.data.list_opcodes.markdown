## START logs/ReadHistoryData-page-10.data
#### RECORD 0 Bolus 2013-08-11T09:09:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x00 0x00    ........
    decimal
              1    0  140    0  140    0    0    0
    datetime (2013-08-11T09:09:14)
    0000   0x8e 0x09 0x49 0x0b 0x0d                   ..I..
    body (0)

#### RECORD 1 CalBGForPH 2013-08-11T09:46:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 321}
```
    op hex (2)
    0000   0x0a 0x41                                  .A
    decimal
             10   65
    datetime (2013-08-11T09:46:17)
    0000   0x91 0x2e 0x29 0x0b 0x8d                   ..)..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 BolusWizard 2013-08-11T09:46:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 321,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 12.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 13.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x41                                  [A
    decimal
             91   65
    datetime (2013-08-11T09:46:25)
    0000   0x99 0x2e 0x09 0x0b 0x0d                   .....
    body (15)
    hex
    0000   0x12 0x51 0x00 0x78 0x3c 0x64 0x84 0x00    .Q.x<d..
    0008   0x3c 0x00 0x00 0x78 0x00 0x48 0x78         <..x.Hx
    decimal
             18   81    0  120   60  100  132    0
             60    0    0  120    0   72  120
    HOUR BITS: [0, 0, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 3.5, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x2b 0xc0                   \..+.
    decimal
             92    5  140   43  192
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-08-11T09:46:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x78 0x00    ..H.H.x.
    decimal
              1    0   72    0   72    0  120    0
    datetime (2013-08-11T09:46:25)
    0000   0x99 0x2e 0x49 0x0b 0x0d                   ..I..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BasalProfileStart 2013-08-11T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-11T12:00:00)
    0000   0x80 0x00 0x0c 0x0b 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 6 CalBGForPH 2013-08-11T16:58:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-08-11T16:58:05)
    0000   0x85 0x3a 0x30 0x0b 0x0d                   .:0..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 BolusWizard 2013-08-11T16:58:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-08-11T16:58:14)
    0000   0x8e 0x3a 0x10 0x6b 0x0d                   .:.k.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x78         P....Px
    decimal
             25   80    0  120   60  100    0    0
             80    0    0    0    0   80  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 179, 'amount': 1.8, 'curve': 208},
 {'age': 219, 'amount': 3.5, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0xb3 0xd0 0x8c 0xdb 0xd0    \.H.....
    decimal
             92    8   72  179  208  140  219  208
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-08-11T16:58:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-08-11T16:58:14)
    0000   0x8e 0x3a 0x50 0x6b 0x0d                   .:Pk.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 CalBGForPH 2013-08-11T19:55:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-08-11T19:55:58)
    0000   0xba 0x37 0x33 0x0b 0x0d                   .73..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 BolusWizard 2013-08-11T19:56:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 110,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 8,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-08-11T19:56:07)
    0000   0x87 0x38 0x13 0x0b 0x0d                   .8...
    body (15)
    hex
    0000   0x08 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x20 0x00 0x00 0x00 0x00 0x20 0x78          .... x
    decimal
              8   80    0  100   60  100    0    0
             32    0    0    0    0   32  120
    HOUR BITS: [0, 0, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 183, 'amount': 2.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0xb7 0xc0                   \.P..
    decimal
             92    5   80  183  192
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-08-11T19:56:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x00 0x00    .. . ...
    decimal
              1    0   32    0   32    0    0    0
    datetime (2013-08-11T19:56:07)
    0000   0x87 0x38 0x53 0x0b 0x0d                   .8S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 CalBGForPH 2013-08-11T23:14:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 209}
```
    op hex (2)
    0000   0x0a 0xd1                                  ..
    decimal
             10  209
    datetime (2013-08-11T23:14:44)
    0000   0xac 0x0e 0x37 0x0b 0x0d                   ..7..
    body (0)

#### RECORD 15 BolusWizard 2013-08-11T23:14:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 209,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd1                                  [.
    decimal
             91  209
    datetime (2013-08-11T23:14:50)
    0000   0xb2 0x0e 0x17 0x0b 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x38 0x00    .P.d<d8.
    0008   0x00 0x00 0x00 0x00 0x00 0x38 0x78         .....8x
    decimal
              0   80    0  100   60  100   56    0
              0    0    0    0    0   56  120

#### RECORD 16 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 201, 'amount': 0.8, 'curve': 192},
 {'age': 125, 'amount': 2.0, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0xc9 0xc0 0x50 0x7d 0xd0    \. ..P}.
    decimal
             92    8   32  201  192   80  125  208
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-08-11T23:14:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-11T23:14:50)
    0000   0xb2 0x0e 0x57 0x0b 0x0d                   ..W..
    body (0)

#### RECORD 18 BasalProfileStart 2013-08-12T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-12T00:00:00)
    0000   0x80 0x00 0x00 0x0c 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 19 ResultTotals (2000, 8, 0, 0, 13, 11) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x58                   ....X
    decimal
              7    0    0    4   88
    datetime ((2000, 8, 0, 0, 13, 11))
    0000   0x8b 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x8b 0x0d 0x05 0x00 0xd8 0x00 0x00    n.......
    0008   0x05 0x00 0x00 0x04 0x58 0x02 0xdc 0x42    ....X..B
    0010   0x01 0x7c 0x22 0x00 0x33 0x00 0x70 0x00    .|".3.p.
    0018   0xc4 0x00 0x48 0x00 0x00 0x02 0x02 0x01    ..H.....
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6b 0x4b 0x00 0x00 0x00 0x00    ..kK....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  139   13    5    0  216    0    0
              5    0    0    4   88    2  220   66
              1  124   34    0   51    0  112    0
            196    0   72    0    0    2    2    1
              0    4    0    0    0    0    0    0
              0    0  107   75    0    0    0    0
              0    0    0

#### RECORD 20 Base (2012, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2012, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 22 Base (2000, 0, 2, 16, 13, 12) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 12))
    0000   0x0c 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 23 CalBGForPH 2013-08-12T09:58:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-08-12T09:58:53)
    0000   0xb5 0x3a 0x29 0x0c 0x0d                   .:)..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 24 BolusWizard 2013-08-12T09:59:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-08-12T09:59:07)
    0000   0x87 0x3b 0x09 0x0c 0x0d                   .;...
    body (15)
    hex
    0000   0x17 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x78         L....Lx
    decimal
             23   80    0  120   60  100    0    0
             76    0    0    0    0   76  120
    HOUR BITS: [0, 0, 1]
#### RECORD 25 Bolus 2013-08-12T09:59:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-12T09:59:07)
    0000   0x87 0x3b 0x49 0x0c 0x0d                   .;I..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 BasalProfileStart 2013-08-12T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-12T12:00:00)
    0000   0x80 0x00 0x0c 0x0c 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 27 CalBGForPH 2013-08-12T12:35:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-08-12T12:35:09)
    0000   0x89 0x23 0x2c 0x0c 0x0d                   .#,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 BolusWizard 2013-08-12T12:35:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-08-12T12:35:20)
    0000   0x94 0x23 0x0c 0x0c 0x0d                   .#...
    body (15)
    hex
    0000   0x1b 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x58 0x00 0x00 0x08 0x00 0x7c 0x78         X....|x
    decimal
             27   80    0  120   60  100   44    0
             88    0    0    8    0  124  120
    HOUR BITS: [0, 0, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 1.4, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0xa2 0xc0                   \.8..
    decimal
             92    5   56  162  192
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-08-12T12:35:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x08 0x00    ..|.|...
    decimal
              1    0  124    0  124    0    8    0
    datetime (2013-08-12T12:35:20)
    0000   0x94 0x23 0x4c 0x0c 0x0d                   .#L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 BasalProfileStart 2013-08-13T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-13T00:00:00)
    0000   0x80 0x00 0x00 0x0d 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 32 ResultTotals (2000, 8, 0, 0, 13, 12) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x90                   .....
    decimal
              7    0    0    3  144
    datetime ((2000, 8, 0, 0, 13, 12))
    0000   0x8c 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x8c 0x0d 0x05 0x00 0x99 0x00 0x00    n.......
    0008   0x02 0x00 0x00 0x03 0x90 0x02 0xdc 0x50    .......P
    0010   0x00 0xb4 0x14 0x00 0x32 0x00 0x38 0x00    ....2.8.
    0018   0x00 0x00 0x7c 0x00 0x00 0x01 0x00 0x01    ..|.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x77 0xba 0x00 0x00 0x00 0x00    ..w.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  140   13    5    0  153    0    0
              2    0    0    3  144    2  220   80
              0  180   20    0   50    0   56    0
              0    0  124    0    0    1    0    1
              0    0    0    0    0    0    0    0
              0    0  119  186    0    0    0    0
              0    0    0

#### RECORD 33 Base (2013, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2013, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 34 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 35 Base (2000, 0, 2, 16, 13, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 13))
    0000   0x0d 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 36 BasalProfileStart 2013-08-13T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-13T12:00:00)
    0000   0x80 0x00 0x0c 0x0d 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 37 CalBGForPH 2013-08-13T13:38:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-08-13T13:38:06)
    0000   0x86 0x26 0x2d 0x0d 0x0d                   .&-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 38 BolusWizard 2013-08-13T13:38:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-13T13:38:12)
    0000   0x8c 0x26 0x0d 0x0d 0x0d                   .&...
    body (15)
    hex
    0000   0x17 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x78         L....Lx
    decimal
             23   80    0  120   60  100    0    0
             76    0    0    0    0   76  120
    HOUR BITS: [0, 0, 1]
#### RECORD 39 Bolus 2013-08-13T13:38:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x00 0x00    ..L.L...
    decimal
              1    0   76    0   76    0    0    0
    datetime (2013-08-13T13:38:12)
    0000   0x8c 0x26 0x4d 0x0d 0x0d                   .&M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 CalBGForPH 2013-08-13T15:55:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-13T15:55:11)
    0000   0x8b 0x37 0x2f 0x0d 0x0d                   .7/..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 BolusWizard 2013-08-13T15:55:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-13T15:55:17)
    0000   0x91 0x37 0x0f 0x0d 0x0d                   .7...
    body (15)
    hex
    0000   0x16 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x48 0x00 0x00 0x0c 0x00 0x48 0x78         H....Hx
    decimal
             22   80    0  120   60  100    0    0
             72    0    0   12    0   72  120
    HOUR BITS: [0, 0, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 142, 'amount': 1.9, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x4c 0x8e 0xc0                   \.L..
    decimal
             92    5   76  142  192
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-08-13T15:55:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x0c 0x00    ..H.H...
    decimal
              1    0   72    0   72    0   12    0
    datetime (2013-08-13T15:55:17)
    0000   0x91 0x37 0x4f 0x0d 0x0d                   .7O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 44 CalBGForPH 2013-08-13T19:42:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2013-08-13T19:42:20)
    0000   0x94 0x2a 0x33 0x0d 0x8d                   .*3..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 45 BolusWizard 2013-08-13T19:42:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 268,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 9.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2013-08-13T19:42:28)
    0000   0x9c 0x2a 0x13 0x0d 0x0d                   .*...
    body (15)
    hex
    0000   0x12 0x51 0x00 0x64 0x3c 0x64 0x60 0x00    .Q.d<d`.
    0008   0x48 0x00 0x00 0x00 0x00 0xa8 0x78         H.....x
    decimal
             18   81    0  100   60  100   96    0
             72    0    0    0    0  168  120
    HOUR BITS: [0, 0, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 229, 'amount': 1.8, 'curve': 192},
 {'age': 113, 'amount': 1.9, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0xe5 0xc0 0x4c 0x71 0xd0    \.H..Lq.
    decimal
             92    8   72  229  192   76  113  208
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-08-13T19:42:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x00 0x00    ........
    decimal
              1    0  168    0  168    0    0    0
    datetime (2013-08-13T19:42:28)
    0000   0x9c 0x2a 0x53 0x0d 0x0d                   .*S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 CalBGForPH 2013-08-13T22:49:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-08-13T22:49:25)
    0000   0x99 0x31 0x36 0x0d 0x0d                   .16..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 BolusWizard 2013-08-13T22:49:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-08-13T22:49:32)
    0000   0xa0 0x31 0x16 0x0d 0x0d                   .1...
    body (15)
    hex
    0000   0x12 0x50 0x00 0x64 0x3c 0x64 0x2c 0x00    .P.d<d,.
    0008   0x48 0x00 0x00 0x00 0x00 0x74 0x78         H....tx
    decimal
             18   80    0  100   60  100   44    0
             72    0    0    0    0  116  120
    HOUR BITS: [0, 0, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 186, 'amount': 3.4, 'curve': 192},
 {'age': 196, 'amount': 0.8, 'curve': 192},
 {'age': 160, 'amount': 1.8, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x88 0xba 0xc0 0x20 0xc4 0xc0    \.... ..
    0008   0x48 0xa0 0xd0                             H..
    decimal
             92   11  136  186  192   32  196  192
             72  160  208
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-08-13T22:49:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2013-08-13T22:49:32)
    0000   0xa0 0x31 0x56 0x0d 0x0d                   .1V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 52 BasalProfileStart 2013-08-14T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-14T00:00:00)
    0000   0x80 0x00 0x00 0x0e 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 53 ResultTotals (2000, 8, 0, 0, 13, 13) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x8c                   .....
    decimal
              7    0    0    4  140
    datetime ((2000, 8, 0, 0, 13, 13))
    0000   0x8d 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x8d 0x0d 0x05 0x00 0xa6 0x00 0x00    n.......
    0008   0x04 0x00 0x00 0x04 0x8c 0x02 0xdc 0x3f    .......?
    0010   0x01 0xb0 0x25 0x00 0x51 0x00 0x94 0x00    ..%.Q...
    0018   0x00 0x01 0x1c 0x00 0x00 0x02 0x00 0x02    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0x0c 0x00 0x00 0x00 0x00    ..d.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  141   13    5    0  166    0    0
              4    0    0    4  140    2  220   63
              1  176   37    0   81    0  148    0
              0    1   28    0    0    2    0    2
              0    4    0    0    0    0    0    0
              0    0  100   12    0    0    0    0
              0    0    0

#### RECORD 54 Base (2014, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2014, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x00 0x04 0x0e                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 55 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 56 Base (2000, 0, 2, 16, 13, 14) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2000, 0, 2, 16, 13, 14))
    0000   0x0e 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 57 BasalProfileStart 2013-08-14T09:12:03 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-14T09:12:03)
    0000   0x83 0x0c 0x09 0x0e 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 58 Prime 2013-08-14T09:11:28 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-14T09:11:28)
    0000   0x9c 0x0b 0x09 0x0e 0x0d                   .....
    body (0)

#### RECORD 59 CalBGForPH 2013-08-14T09:12:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-14T09:12:20)
    0000   0x94 0x0c 0x29 0x0e 0x0d                   ..)..
    body (0)

#### RECORD 60 BolusWizard 2013-08-14T09:12:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-14T09:12:27)
    0000   0x9b 0x0c 0x09 0x0e 0x0d                   .....
    body (15)
    hex
    0000   0x18 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x78         P....Px
    decimal
             24   80    0  120   60  100    0    0
             80    0    0    0    0   80  120

#### RECORD 61 Bolus 2013-08-14T09:12:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-08-14T09:12:27)
    0000   0x9b 0x0c 0x49 0x0e 0x0d                   ..I..
    body (0)

#### RECORD 62 BasalProfileStart 2013-08-14T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-14T12:00:00)
    0000   0x80 0x00 0x0c 0x0e 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 63 CalBGForPH 2013-08-14T15:16:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-14T15:16:46)
    0000   0xae 0x10 0x2f 0x0e 0x0d                   ../..
    body (0)

#### RECORD 64 BolusWizard 2013-08-14T15:16:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-14T15:16:52)
    0000   0xb4 0x10 0x0f 0x6e 0x0d                   ...n.
    body (15)
    hex
    0000   0x11 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x38 0x00 0x00 0x00 0x00 0x38 0x78         8....8x
    decimal
             17   80    0  120   60  100    0    0
             56    0    0    0    0   56  120
    DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 107, 'amount': 1.15, 'curve': 208},
 {'age': 117, 'amount': 0.85, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x2e 0x6b 0xd0 0x22 0x75 0xd0    \..k."u.
    decimal
             92    8   46  107  208   34  117  208
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-08-14T15:16:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-14T15:16:52)
    0000   0xb4 0x10 0x4f 0x6e 0x0d                   ..On.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 67 CalBGForPH 2013-08-14T15:45:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-08-14T15:45:01)
    0000   0x81 0x2d 0x2f 0x0e 0x0d                   .-/..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 68 BolusWizard 2013-08-14T15:45:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-14T15:45:06)
    0000   0x86 0x2d 0x0f 0x0e 0x0d                   .-...
    body (15)
    hex
    0000   0x11 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x38 0x00 0x00 0x34 0x00 0x38 0x78         8..4.8x
    decimal
             17   80    0  120   60  100    0    0
             56    0    0   52    0   56  120
    HOUR BITS: [0, 0, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 1.4, 'curve': 192},
 {'age': 136, 'amount': 1.15, 'curve': 208},
 {'age': 146, 'amount': 0.85, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0x20 0xc0 0x2e 0x88 0xd0    \.8 ....
    0008   0x22 0x92 0xd0                             "..
    decimal
             92   11   56   32  192   46  136  208
             34  146  208
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-08-14T15:45:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x34 0x00    ..8.8.4.
    decimal
              1    0   56    0   56    0   52    0
    datetime (2013-08-14T15:45:07)
    0000   0x87 0x2d 0x4f 0x0e 0x0d                   .-O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 71 CalBGForPH 2013-08-14T17:10:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 204}
```
    op hex (2)
    0000   0x0a 0xcc                                  ..
    decimal
             10  204
    datetime (2013-08-14T17:10:38)
    0000   0xa6 0x0a 0x31 0x0e 0x0d                   ..1..
    body (0)

#### RECORD 72 BolusWizard 2013-08-14T17:10:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 204,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcc                                  [.
    decimal
             91  204
    datetime (2013-08-14T17:10:42)
    0000   0xaa 0x0a 0x11 0x6e 0x0d                   ...n.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x38 0x00    .P.d<d8.
    0008   0x00 0x00 0x00 0x2c 0x00 0x0c 0x78         ...,..x
    decimal
              0   80    0  100   60  100   56    0
              0    0    0   44    0   12  120
    DAY BITS: [0, 1, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 87, 'amount': 1.4, 'curve': 192},
 {'age': 117, 'amount': 1.4, 'curve': 192},
 {'age': 221, 'amount': 1.15, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0x57 0xc0 0x38 0x75 0xc0    \.8W.8u.
    0008   0x2e 0xdd 0xd0                             ...
    decimal
             92   11   56   87  192   56  117  192
             46  221  208
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2013-08-14T17:10:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x0c 0x00 0x0c 0x00 0x2c 0x00    ......,.
    decimal
              1    0   12    0   12    0   44    0
    datetime (2013-08-14T17:10:42)
    0000   0xaa 0x0a 0x51 0x6e 0x0d                   ..Qn.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 75 Base unknown head[2], body[0] op[0x8a]

    op hex (2)
    0000   0x8a 0x73                                  .s
    decimal
            138  115
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-10.data: 76 records`
