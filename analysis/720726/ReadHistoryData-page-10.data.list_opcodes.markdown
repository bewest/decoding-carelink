## START logs/ReadHistoryData-page-10.data
#### STOPPING DOUBLE NULLS @ 307, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x80 0x32 0x48 0x7f 0x0d 0x21 0x00 0x89    .2H..!..
    0008   0x0c 0x09 0x1f 0x0d 0x03 0x00 0x00 0x00    ........
    0010   0x41 0xad 0x0c 0x29 0x1f 0x0d 0x7b 0x01    A..)..{.
    0018   0xb1 0x0d 0x09 0x1f 0x0d 0x08 0x2e 0x00    ........
##### DEBUG DECIMAL
            128   50   72  127   13   33    0  137
             12    9   31   13    3    0    0    0
             65  173   12   41   31   13  123    1
            177   13    9   31   13    8   46    0
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

#### RECORD 9 ResultTotals 2000-08-05T00:13:30 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x88                   .....
    decimal
              7    0    0    3  136
    datetime (2000-08-05T00:13:30)
    0000   0x9e 0x0d 0x00 0x05 0x10                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x9e 0x0d 0x06 0x00 0x00 0x00 0x00    n.......
    0008   0x00 0x00 0x00 0x03 0x88 0x01 0x2c 0x21    ......,!
    0010   0x02 0x5c 0x43 0x00 0x9b 0x01 0x9c 0x00    .\C.....
    0018   0x00 0x00 0xa8 0x00 0x18 0x04 0x00 0x01    ........
    0020   0x01 0x50 0x00 0x00 0x00 0x00 0x00 0x00    .P......
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  158   13    6    0    0    0    0
              0    0    0    3  136    1   44   33
              2   92   67    0  155    1  156    0
              0    0  168    0   24    4    0    1
              1   80    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x80                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
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

#### RECORD 17 Base (2013, 8, 31, 8, 50, 0) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime ((2013, 8, 31, 8, 50, 0))
    0000   0x80 0x32 0x08 0x1f 0x0d                   .2...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 CalBGForPH (2004, 0, 0, 4, 0, 1) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 30}
```
    op hex (2)
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    datetime ((2004, 0, 0, 4, 0, 1))
    0000   0x01 0x00 0x24 0x00 0x24                   ..$.$
    body (0)
    YEAR BITS: [0, 0, 1, 0]
`end logs/ReadHistoryData-page-10.data: 19 records`
