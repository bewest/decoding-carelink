## START logs/ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 312, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0x38 0x03 0x74 0x52 0x00 0xc4 0x12    .8.tR...
    0008   0x00 0x41 0x00 0xc4 0x12 0x00 0xc4 0x64    .A.....d
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0018   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
##### DEBUG DECIMAL
              4   56    3  116   82    0  196   18
              0   65    0  196   18    0  196  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
#### RECORD 0 BolusWizard 2013-06-06T12:29:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 235,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xeb                                  [.
    decimal
             91  235
    datetime (2013-06-06T12:29:25)
    0000   0x59 0x9d 0x0c 0x06 0x0d                   Y....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x18 0x27 0x00    3P.-j.'.
    0008   0x00 0x18 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106   24   39    0
              0   24    0   39  125
    HOUR BITS: [1, 0, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 0.1, 'curve': 4},
 {'age': 95, 'amount': 3.5, 'curve': 4},
 {'age': 105, 'amount': 0.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x04 0x19 0x04 0x8c 0x5f 0x04    \....._.
    0008   0x08 0x69 0x04                             .i.
    decimal
             92   11    4   25    4  140   95    4
              8  105    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-06-06T12:29:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-06-06T12:29:25)
    0000   0x59 0x9d 0x4c 0x06 0x0d                   Y.L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 BolusWizard 2013-06-06T12:45:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-06-06T12:45:02)
    0000   0x42 0xad 0x0c 0x06 0x0d                   B....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [1, 0, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 3.9, 'curve': 4},
 {'age': 41, 'amount': 0.1, 'curve': 4},
 {'age': 111, 'amount': 3.5, 'curve': 4},
 {'age': 121, 'amount': 0.2, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x9c 0x15 0x04 0x04 0x29 0x04    \.....).
    0008   0x8c 0x6f 0x04 0x08 0x79 0x04              .o..y.
    decimal
             92   14  156   21    4    4   41    4
            140  111    4    8  121    4
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-06-06T12:45:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-06-06T12:45:02)
    0000   0x42 0xad 0x4c 0x06 0x0d                   B.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 CalBGForPH 2013-06-06T13:31:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 68}
```
    op hex (2)
    0000   0x0a 0x44                                  .D
    decimal
             10   68
    datetime (2013-06-06T13:31:15)
    0000   0x4f 0x9f 0x2d 0x06 0x0d                   O.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 CalBGForPH 2013-06-06T17:43:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2013-06-06T17:43:00)
    0000   0x40 0xab 0x31 0x06 0x0d                   @.1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 8 BolusWizard 2013-06-06T17:43:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 159,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9f                                  [.
    decimal
             91  159
    datetime (2013-06-06T17:43:04)
    0000   0x44 0xab 0x11 0x06 0x0d                   D....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x07 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
              0   80   13   45  106    7    0    0
              0    0    0    7  125
    HOUR BITS: [1, 0, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 1.9, 'curve': 20},
 {'age': 63, 'amount': 3.9, 'curve': 20},
 {'age': 83, 'amount': 0.1, 'curve': 20},
 {'age': 153, 'amount': 3.5, 'curve': 20},
 {'age': 163, 'amount': 0.2, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x4c 0x2b 0x14 0x9c 0x3f 0x14    \.L+..?.
    0008   0x04 0x53 0x14 0x8c 0x99 0x14 0x08 0xa3    .S......
    0010   0x14                                       .
    decimal
             92   17   76   43   20  156   63   20
              4   83   20  140  153   20    8  163
             20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-06-06T17:43:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-06-06T17:43:04)
    0000   0x44 0xab 0x51 0x06 0x0d                   D.Q..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 11 CalBGForPH 2013-06-06T19:57:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-06-06T19:57:51)
    0000   0x73 0xb9 0x33 0x06 0x0d                   s.3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 BolusWizard 2013-06-06T19:58:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 30,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-06-06T19:58:05)
    0000   0x45 0xba 0x13 0x06 0x0d                   E....
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106    0   23    0
              0    3    0   23  125
    HOUR BITS: [1, 0, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 0.7, 'curve': 4},
 {'age': 178, 'amount': 1.9, 'curve': 20},
 {'age': 198, 'amount': 3.9, 'curve': 20},
 {'age': 218, 'amount': 0.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1c 0x90 0x04 0x4c 0xb2 0x14    \....L..
    0008   0x9c 0xc6 0x14 0x04 0xda 0x14              ......
    decimal
             92   14   28  144    4   76  178   20
            156  198   20    4  218   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-06-06T19:58:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-06-06T19:58:05)
    0000   0x45 0xba 0x53 0x06 0x0d                   E.S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 15 ResultTotals 2013-04-06T13:13:38 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x52                   ....R
    decimal
              7    0    0    5   82
    datetime (2013-04-06T13:13:38)
    0000   0x66 0x0d 0x6d 0x66 0x0d                   f.mf.
    body (51)
    hex
    0000   0x05 0x10 0xbc 0x44 0x27 0x06 0x00 0x00    ...D'...
    0008   0x05 0x52 0x03 0x5a 0x3f 0x01 0xf8 0x25    .R.Z?..%
    0010   0x00 0x6a 0x01 0xf8 0x25 0x01 0x44 0x40    .j..%.D@
    0018   0x00 0xb4 0x24 0x00 0x00 0x00 0x06 0x03    ..$.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x46 0xbb 0x0d 0x07 0x0d    ...F....
    0030   0x1f 0x00 0x6c                             ..l
    decimal
              5   16  188   68   39    6    0    0
              5   82    3   90   63    1  248   37
              0  106    1  248   37    1   68   64
              0  180   36    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0   30    0   70  187   13    7   13
             31    0  108
    DAY BITS: [0, 1, 1]
#### RECORD 16 Base (2000, 0, 6, 10, 13, 7) head[2], body[0] op[0x97]

    op hex (2)
    0000   0x97 0x0e                                  ..
    decimal
            151   14
    datetime ((2000, 0, 6, 10, 13, 7))
    0000   0x07 0x0d 0x0a 0x66 0x70                   ...fp
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 17 Base (2002, 0, 6, 27, 13, 7) head[2], body[0] op[0x91]

    op hex (2)
    0000   0x91 0x2f                                  ./
    decimal
            145   47
    datetime ((2002, 0, 6, 27, 13, 7))
    0000   0x07 0x0d 0x5b 0x66 0x42                   ..[fB
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 18 Base (2013, 0, 16, 1, 13, 7) head[2], body[0] op[0x92]

    op hex (2)
    0000   0x92 0x0f                                  ..
    decimal
            146   15
    datetime ((2013, 0, 16, 1, 13, 7))
    0000   0x07 0x0d 0x41 0x50 0x0d                   ..AP.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 19 Base (2000, 12, 0, 16, 50, 63) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 50, 63))
    0000   0xff 0x32 0xf0 0x00 0x00                   .2...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 Base (2000, 4, 17, 17, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x31                                  .1
    decimal
              0   49
    datetime ((2000, 4, 17, 17, 1, 61))
    0000   0x7d 0x01 0x31 0x31 0x00                   }.11.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 21 Base (2000, 4, 7, 13, 7, 15) head[2], body[0] op[0x42]

    op hex (2)
    0000   0x42 0x92                                  B.
    decimal
             66  146
    datetime ((2000, 4, 7, 13, 7, 15))
    0000   0x4f 0x07 0x0d 0x07 0x00                   O....
    body (0)

#### RECORD 22 Base (2007, 1, 13, 13, 39, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2007, 1, 13, 13, 39, 56))
    0000   0x38 0x67 0x0d 0x6d 0x67                   8g.mg
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 23 Base (2001, 1, 6, 6, 38, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x05                                  ..
    decimal
             13    5
    datetime ((2001, 1, 6, 6, 38, 0))
    0000   0x00 0x66 0x66 0x66 0x01                   .fff.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-13.data: 24 records`
