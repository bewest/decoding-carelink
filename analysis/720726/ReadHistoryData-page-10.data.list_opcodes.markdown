## START analysis/ianj/raw/ReadHistoryData-page-10.data
ERROR day is out of range for month (2013, 8, 32, 0, 0, 0) 0000   0x9f 0x0d                                  ..
#### STOPPING DOUBLE NULLS @ 980, found 42 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe9 0xa9                                  ..
##### DEBUG DECIMAL
            233  169
#### RECORD 0 Bolus 2013-08-30T21:05:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x58 0x00    ......X.
    decimal
              1    0  144    0  144    0   88    0
    datetime (2013-08-30T21:05:53)
    0000   0xb5 0x05 0x55 0x7e 0x0d                   ..U~.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-08-30T21:21:15 head[2], body[15] op[0x5b]
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
    datetime (2013-08-30T21:21:15)
    0000   0x8f 0x15 0x15 0x7e 0x0d                   ...~.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 3.6, 'curve': 4},
 {'age': 150, 'amount': 4.7, 'curve': 4},
 {'age': 160, 'amount': 1.3, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x90 0x14 0x04 0xbc 0x96 0x04    \.......
    0008   0x34 0xa0 0x04                             4..
    decimal
             92   11  144   20    4  188  150    4
             52  160    4
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2013-08-30T21:21:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0xd4 0x00    ..H.H...
    decimal
              1    0   72    0   72    0  212    0
    datetime (2013-08-30T21:21:15)
    0000   0x8f 0x15 0x55 0x7e 0x0d                   ..U~.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 4 Bolus 2013-08-30T21:38:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x01 0x00 0x00    ........
    decimal
              1    0   24    0   24    1    0    0
    datetime (2013-08-30T21:38:19)
    0000   0x93 0x26 0x55 0x7e 0x0d                   .&U~.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2013-08-30T22:29:34 head[2], body[15] op[0x5b]
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
    datetime (2013-08-30T22:29:34)
    0000   0xa2 0x1d 0x16 0x7e 0x0d                   ...~.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 58, 'amount': 0.6, 'curve': 4},
 {'age': 68, 'amount': 1.8, 'curve': 4},
 {'age': 88, 'amount': 3.6, 'curve': 4},
 {'age': 218, 'amount': 4.7, 'curve': 4},
 {'age': 228, 'amount': 1.3, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x18 0x3a 0x04 0x48 0x44 0x04    \..:.HD.
    0008   0x90 0x58 0x04 0xbc 0xda 0x04 0x34 0xe4    .X....4.
    0010   0x04                                       .
    decimal
             92   17   24   58    4   72   68    4
            144   88    4  188  218    4   52  228
              4
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-08-30T22:29:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0xc0 0x00    ..|.|...
    decimal
              1    0  124    0  124    0  192    0
    datetime (2013-08-30T22:29:34)
    0000   0xa2 0x1d 0x56 0x7e 0x0d                   ..V~.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 8 BasalProfileStart 2013-08-31T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-31T00:00:00)
    0000   0x80 0x00 0x00 0x1f 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 9 MResultTotals 2013-08-31T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x88                   .....
    decimal
              7    0    0    3  136
    datetime (2013-08-31T00:00:00)
    0000   0x9e 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x05 0x10                             ...
    decimal
              0    5   16

#### RECORD 10 Sara6E 2013-08-31T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-31T00:00:00)
    0000   0x9e 0x0d                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x03 0x88 0x01 0x2c 0x21 0x02 0x5c 0x43    ...,!.\C
    0010   0x00 0x9b 0x01 0x9c 0x00 0x00 0x00 0xa8    ........
    0018   0x00 0x18 0x04 0x00 0x01 0x01 0x50 0x00    ......P.
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x80                                       .
    decimal
              6    0    0    0    0    0    0    0
              3  136    1   44   33    2   92   67
              0  155    1  156    0    0    0  168
              0   24    4    0    1    1   80    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
            128

#### RECORD 11 BolusWizard 2013-08-31T01:35:47 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T01:35:47)
    0000   0xaf 0x23 0x01 0x7f 0x0d                   .#...
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 184, 'amount': 1.0, 'curve': 4},
 {'age': 194, 'amount': 2.1, 'curve': 4},
 {'age': 244, 'amount': 0.6, 'curve': 4},
 {'age': 254, 'amount': 1.8, 'curve': 4},
 {'age': 18, 'amount': 3.6, 'curve': 20},
 {'age': 148, 'amount': 4.7, 'curve': 20},
 {'age': 158, 'amount': 1.3, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x28 0xb8 0x04 0x54 0xc2 0x04    \.(..T..
    0008   0x18 0xf4 0x04 0x48 0xfe 0x04 0x90 0x12    ...H....
    0010   0x14 0xbc 0x94 0x14 0x34 0x9e 0x14         ....4..
    decimal
             92   23   40  184    4   84  194    4
             24  244    4   72  254    4  144   18
             20  188  148   20   52  158   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-08-31T01:35:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x14 0x00    ..|.|...
    decimal
              1    0  124    0  124    0   20    0
    datetime (2013-08-31T01:35:48)
    0000   0xb0 0x23 0x41 0x7f 0x0d                   .#A..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 BasalProfileStart 2013-08-31T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-31T04:00:00)
    0000   0x80 0x00 0x04 0x1f 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 15 BolusWizard 2013-08-31T08:49:59 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T08:49:59)
    0000   0xbb 0x31 0x08 0x7f 0x0d                   .1...
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 182, 'amount': 3.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0xb6 0x14                   \.|..
    decimal
             92    5  124  182   20
    datetime (unknown)

    body (0)

#### RECORD 17 Ian69 2013-08-31T08:50:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-31T08:50:00)
    0000   0x80 0x32 0x08 0x1f 0x0d                   .2...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 0, 1]
#### RECORD 18 Bolus 2013-08-31T08:50:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x00 0x00    ..$.$...
    decimal
              1    0   36    0   36    0    0    0
    datetime (2013-08-31T08:50:00)
    0000   0x80 0x32 0x48 0x7f 0x0d                   .2H..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 Rewind 2013-08-31T09:12:09 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-31T09:12:09)
    0000   0x89 0x0c 0x09 0x1f 0x0d                   .....
    body (0)

#### RECORD 20 Prime 2013-08-31T09:12:45 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x41                   ....A
    decimal
              3    0    0    0   65
    datetime (2013-08-31T09:12:45)
    0000   0xad 0x0c 0x29 0x1f 0x0d                   ..)..
    body (0)

#### RECORD 21 BasalProfileStart 2013-08-31T09:13:49 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-31T09:13:49)
    0000   0xb1 0x0d 0x09 0x1f 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 22 Prime 2013-08-31T09:13:15 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-31T09:13:15)
    0000   0x8f 0x0d 0x09 0x1f 0x0d                   .....
    body (0)

#### RECORD 23 BolusWizard 2013-08-31T09:14:19 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T09:14:19)
    0000   0x93 0x0e 0x09 0x7f 0x0d                   .....
    body (15)
    hex
    0000   0x22 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    "..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             34  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 0.15, 'curve': 4},
 {'age': 33, 'amount': 0.75, 'curve': 4},
 {'age': 207, 'amount': 3.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x06 0x17 0x04 0x1e 0x21 0x04    \.....!.
    0008   0x7c 0xcf 0x14                             |..
    decimal
             92   11    6   23    4   30   33    4
            124  207   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-08-31T09:14:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 20.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x24 0x00    ......$.
    decimal
              1    0  200    0  200    0   36    0
    datetime (2013-08-31T09:14:19)
    0000   0x93 0x0e 0x49 0x7f 0x0d                   ..I..
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2013-08-31T09:19:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 52,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 188}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-31T09:19:53)
    0000   0xb5 0x13 0x09 0x7f 0x0d                   .....
    body (15)
    hex
    0000   0x34 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    4..n.6..
    0008   0xbc 0x00 0x00 0x00 0x00 0xbc 0x36         ......6
    decimal
             52  144    0  110   23   54    0    0
            188    0    0    0    0  188   54
    DAY BITS: [0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 5.0, 'curve': 4},
 {'age': 28, 'amount': 0.15, 'curve': 4},
 {'age': 38, 'amount': 0.75, 'curve': 4},
 {'age': 212, 'amount': 3.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xc8 0x08 0x04 0x06 0x1c 0x04    \.......
    0008   0x1e 0x26 0x04 0x7c 0xd4 0x14              .&.|..
    decimal
             92   14  200    8    4    6   28    4
             30   38    4  124  212   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-08-31T09:19:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0xec 0x00    ........
    decimal
              1    0  132    0  132    0  236    0
    datetime (2013-08-31T09:19:53)
    0000   0xb5 0x13 0x49 0x7f 0x0d                   ..I..
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 29 BasalProfileStart 2013-08-31T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-31T09:30:00)
    0000   0x80 0x1e 0x09 0x1f 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 30 Bolus 2013-08-31T10:38:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xf4 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  244    0
    datetime (2013-08-31T10:38:14)
    0000   0x8e 0x26 0x4a 0x7f 0x0d                   .&J..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2013-08-31T11:33:20 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T11:33:20)
    0000   0x94 0x21 0x0b 0x7f 0x0d                   .!...
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 62, 'amount': 2.0, 'curve': 4},
 {'age': 132, 'amount': 1.65, 'curve': 4},
 {'age': 142, 'amount': 0.25, 'curve': 5},
 {'age': 162, 'amount': 0.15, 'curve': 4},
 {'age': 172, 'amount': 0.75, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x3e 0x04 0x42 0x84 0x04    \.P>.B..
    0008   0x0a 0x8e 0x05 0x06 0xa2 0x04 0x1e 0xac    ........
    0010   0x04                                       .
    decimal
             92   17   80   62    4   66  132    4
             10  142    5    6  162    4   30  172
              4
    datetime (unknown)

    body (0)

#### RECORD 33 Ian69 2013-08-31T11:33:20 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-31T11:33:20)
    0000   0x94 0x21 0x0b 0x1f 0x0d                   .!...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 34 Bolus 2013-08-31T11:33:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xbc 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  188    0
    datetime (2013-08-31T11:33:20)
    0000   0x94 0x21 0x4b 0x7f 0x0d                   .!K..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2013-08-31T12:35:55 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T12:35:55)
    0000   0xb7 0x23 0x0c 0x7f 0x0d                   .#...
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 2.0, 'curve': 4},
 {'age': 124, 'amount': 2.0, 'curve': 4},
 {'age': 194, 'amount': 1.65, 'curve': 4},
 {'age': 204, 'amount': 0.25, 'curve': 5},
 {'age': 224, 'amount': 0.15, 'curve': 4},
 {'age': 234, 'amount': 0.75, 'curve': 4}]
```
    op hex (20)
    0000   0x5c 0x14 0x50 0x40 0x04 0x50 0x7c 0x04    \.P@.P|.
    0008   0x42 0xc2 0x04 0x0a 0xcc 0x05 0x06 0xe0    B.......
    0010   0x04 0x1e 0xea 0x04                        ....
    decimal
             92   20   80   64    4   80  124    4
             66  194    4   10  204    5    6  224
              4   30  234    4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-08-31T12:35:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x8c 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  140    0
    datetime (2013-08-31T12:35:55)
    0000   0xb7 0x23 0x4c 0x7f 0x0d                   .#L..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2013-08-31T12:41:13 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T12:41:13)
    0000   0x8d 0x29 0x0c 0x7f 0x0d                   .)...
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 3.0, 'curve': 4},
 {'age': 70, 'amount': 2.0, 'curve': 4},
 {'age': 130, 'amount': 2.0, 'curve': 4},
 {'age': 200, 'amount': 1.65, 'curve': 4},
 {'age': 210, 'amount': 0.25, 'curve': 5},
 {'age': 230, 'amount': 0.15, 'curve': 4},
 {'age': 240, 'amount': 0.75, 'curve': 4}]
```
    op hex (23)
    0000   0x5c 0x17 0x78 0x0a 0x04 0x50 0x46 0x04    \.x..PF.
    0008   0x50 0x82 0x04 0x42 0xc8 0x04 0x0a 0xd2    P..B....
    0010   0x05 0x06 0xe6 0x04 0x1e 0xf0 0x04         .......
    decimal
             92   23  120   10    4   80   70    4
             80  130    4   66  200    4   10  210
              5    6  230    4   30  240    4
    datetime (unknown)

    body (0)

#### RECORD 40 PumpSuspend 2013-08-31T12:41:22 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-08-31T12:41:22)
    0000   0x96 0x29 0x0c 0x1f 0x0d                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 Bolus 2013-08-31T12:41:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x0a 0x00 0xfc 0x00    ..T.....
    decimal
              1    0   84    0   10    0  252    0
    datetime (2013-08-31T12:41:13)
    0000   0x8d 0x29 0x4c 0x7f 0x0d                   .)L..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 BasalProfileStart 2013-08-31T12:41:23 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-31T12:41:23)
    0000   0x97 0x29 0x0c 0x1f 0x0d                   .)...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 0, 1]
#### RECORD 43 PumpResume 2013-08-31T12:41:24 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-08-31T12:41:24)
    0000   0x98 0x29 0x0c 0x1f 0x0d                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 44 BasalProfileStart 2013-08-31T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-31T13:00:00)
    0000   0x80 0x00 0x0d 0x1f 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 45 CalBGForPH 2013-08-31T16:23:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 51}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2013-08-31T16:23:02)
    0000   0x82 0x17 0x50 0x1f 0x0d                   ..P..
    body (0)

#### RECORD 46 BolusWizard 2013-08-31T19:21:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 52,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 188}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-31T19:21:57)
    0000   0xb9 0x15 0x13 0x7f 0x0d                   .....
    body (15)
    hex
    0000   0x34 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    4..n.6..
    0008   0xbc 0x00 0x00 0x00 0x00 0xbc 0x36         ......6
    decimal
             52  144    0  110   23   54    0    0
            188    0    0    0    0  188   54
    DAY BITS: [0, 1, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 0.25, 'curve': 20},
 {'age': 154, 'amount': 3.0, 'curve': 20},
 {'age': 214, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0a 0x90 0x14 0x78 0x9a 0x14    \....x..
    0008   0x50 0xd6 0x14                             P..
    decimal
             92   11   10  144   20  120  154   20
             80  214   20
    datetime (unknown)

    body (0)

#### RECORD 48 Ian69 2013-08-31T19:21:57 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-31T19:21:57)
    0000   0xb9 0x15 0x73 0x1f 0x0d                   ..s..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 49 Bolus 2013-08-31T19:21:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 18.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xbc 0x00 0xbc 0x00 0x00 0x00    ........
    decimal
              1    0  188    0  188    0    0    0
    datetime (2013-08-31T19:21:57)
    0000   0xb9 0x15 0x53 0x7f 0x0d                   ..S..
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 50 BolusWizard 2013-08-31T20:07:28 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T20:07:28)
    0000   0x9c 0x07 0x14 0x7f 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    DAY BITS: [0, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 4.7, 'curve': 4},
 {'age': 190, 'amount': 0.25, 'curve': 20},
 {'age': 200, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xbc 0x2e 0x04 0x0a 0xbe 0x14    \.......
    0008   0x78 0xc8 0x14                             x..
    decimal
             92   11  188   46    4   10  190   20
            120  200   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-08-31T20:07:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0xa8 0x00    ..L.L...
    decimal
              1    0   76    0   76    0  168    0
    datetime (2013-08-31T20:07:29)
    0000   0x9d 0x07 0x54 0x7f 0x0d                   ..T..
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 53 BolusWizard 2013-08-31T22:18:49 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T22:18:49)
    0000   0xb1 0x12 0x16 0x7f 0x0d                   .....
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 1.9, 'curve': 4},
 {'age': 177, 'amount': 4.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x89 0x04 0xbc 0xb1 0x04    \.L.....
    decimal
             92    8   76  137    4  188  177    4
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-08-31T22:18:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x40 0x00    ..X.X.@.
    decimal
              1    0   88    0   88    0   64    0
    datetime (2013-08-31T22:18:49)
    0000   0xb1 0x12 0x56 0x7f 0x0d                   ..V..
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 56 BolusWizard 2013-08-31T22:21:18 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T22:21:18)
    0000   0x92 0x15 0x16 0x7f 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 2.2, 'curve': 4},
 {'age': 140, 'amount': 1.9, 'curve': 4},
 {'age': 180, 'amount': 4.7, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x0a 0x04 0x4c 0x8c 0x04    \.X..L..
    0008   0xbc 0xb4 0x04                             ...
    decimal
             92   11   88   10    4   76  140    4
            188  180    4
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-08-31T22:21:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x94 0x00    ..L.L...
    decimal
              1    0   76    0   76    0  148    0
    datetime (2013-08-31T22:21:18)
    0000   0x92 0x15 0x56 0x7f 0x0d                   ..V..
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 59 BolusWizard 2013-08-31T22:26:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-31T22:26:27)
    0000   0x9b 0x1a 0x16 0x7f 0x0d                   .....
    body (15)
    hex
    0000   0x0d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x2c 0x00 0x00 0x00 0x00 0x2c 0x36         ,....,6
    decimal
             13  144    0  110   23   54    0    0
             44    0    0    0    0   44   54
    DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 1.9, 'curve': 4},
 {'age': 15, 'amount': 2.2, 'curve': 4},
 {'age': 145, 'amount': 1.9, 'curve': 4},
 {'age': 185, 'amount': 4.7, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x4c 0x05 0x04 0x58 0x0f 0x04    \.L..X..
    0008   0x4c 0x91 0x04 0xbc 0xb9 0x04              L.....
    decimal
             92   14   76    5    4   88   15    4
             76  145    4  188  185    4
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-08-31T22:26:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0xdc 0x00    ..,.,...
    decimal
              1    0   44    0   44    0  220    0
    datetime (2013-08-31T22:26:27)
    0000   0x9b 0x1a 0x56 0x7f 0x0d                   ..V..
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 62 BolusWizard 2013-08-31T23:23:06 head[2], body[15] op[0x5b]
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
    datetime (2013-08-31T23:23:06)
    0000   0x86 0x17 0x17 0x7f 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    DAY BITS: [0, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 62, 'amount': 3.0, 'curve': 4},
 {'age': 72, 'amount': 2.2, 'curve': 4},
 {'age': 202, 'amount': 1.9, 'curve': 4},
 {'age': 242, 'amount': 4.7, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0x3e 0x04 0x58 0x48 0x04    \.x>.XH.
    0008   0x4c 0xca 0x04 0xbc 0xf2 0x04              L.....
    decimal
             92   14  120   62    4   88   72    4
             76  202    4  188  242    4
    datetime (unknown)

    body (0)

#### RECORD 64 BasalProfileStart 2013-09-01T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-01T00:00:00)
    0000   0x80 0x40 0x00 0x01 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 1, 0]
ERROR day is out of range for month (2013, 8, 32, 0, 0, 0) 0000   0x9f 0x0d                                  ..
#### RECORD 65 MResultTotals (2013, 8, 32, 0, 0, 0) head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x6d                   ....m
    decimal
              7    0    0    8  109
    datetime ((2013, 8, 32, 0, 0, 0))
    0000   0x9f 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end analysis/ianj/raw/ReadHistoryData-page-10.data: 66 records`
