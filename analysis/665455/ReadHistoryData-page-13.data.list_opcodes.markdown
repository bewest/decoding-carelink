## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x9a 0x3d                                  .=
##### DEBUG DECIMAL
            154   61
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
#### RECORD 15 MResultTotals (2013, 0, 6, 18, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 6, 18, 5, 0))
    0000   0x00 0x05 0x52 0x66 0x0d                   ..Rf.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 16 Model522ResultTotals 2013-06-07T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-07T00:00:00)
    0000   0x66 0x0d                                  f.
    body (41)
    hex
    0000   0x05 0x10 0xbc 0x44 0x27 0x06 0x00 0x00    ...D'...
    0008   0x05 0x52 0x03 0x5a 0x3f 0x01 0xf8 0x25    .R.Z?..%
    0010   0x00 0x6a 0x01 0xf8 0x25 0x01 0x44 0x40    .j..%.D@
    0018   0x00 0xb4 0x24 0x00 0x00 0x00 0x06 0x03    ..$.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  188   68   39    6    0    0
              5   82    3   90   63    1  248   37
              0  106    1  248   37    1   68   64
              0  180   36    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0

#### RECORD 17 PumpSuspend 2013-06-07T13:59:06 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-07T13:59:06)
    0000   0x46 0xbb 0x0d 0x07 0x0d                   F....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 PumpResume 2013-06-07T14:23:44 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-07T14:23:44)
    0000   0x6c 0x97 0x0e 0x07 0x0d                   l....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 19 CalBGForPH 2013-06-07T15:17:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-06-07T15:17:48)
    0000   0x70 0x91 0x2f 0x07 0x0d                   p./..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 BolusWizard 2013-06-07T15:18:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 102,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-06-07T15:18:02)
    0000   0x42 0x92 0x0f 0x07 0x0d                   B....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0xff 0x32 0xf0    AP.-j.2.
    0008   0x00 0x00 0x00 0x31 0x7d                   ...1}
    decimal
             65   80   13   45  106  255   50  240
              0    0    0   49  125
    HOUR BITS: [1, 0, 0]
#### RECORD 21 Bolus 2013-06-07T15:18:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2013-06-07T15:18:02)
    0000   0x42 0x92 0x4f 0x07 0x0d                   B.O..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 22 MResultTotals (2013, 0, 7, 24, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 7, 24, 4, 0))
    0000   0x00 0x04 0x38 0x67 0x0d                   ..8g.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 23 Model522ResultTotals 2013-06-08T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-08T00:00:00)
    0000   0x67 0x0d                                  g.
    body (41)
    hex
    0000   0x05 0x00 0x66 0x66 0x66 0x01 0x00 0x00    ..fff...
    0008   0x04 0x38 0x03 0x74 0x52 0x00 0xc4 0x12    .8.tR...
    0010   0x00 0x41 0x00 0xc4 0x12 0x00 0xc4 0x64    .A.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  102  102  102    1    0    0
              4   56    3  116   82    0  196   18
              0   65    0  196   18    0  196  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0

#### RECORD 24 CalBGForPH 2013-06-08T00:48:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-06-08T00:48:37)
    0000   0x65 0xb0 0x20 0x08 0x0d                   e. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 25 BolusWizard 2013-06-08T00:48:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 63,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-06-08T00:48:46)
    0000   0x6e 0xb0 0x00 0x08 0x0d                   n....
    body (13)
    hex
    0000   0x3f 0x50 0x0d 0x2d 0x6a 0x00 0x30 0x00    ?P.-j.0.
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
             63   80   13   45  106    0   48    0
              0    0    0   48  125
    HOUR BITS: [1, 0, 1]
#### RECORD 26 Bolus 2013-06-08T00:48:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2013-06-08T00:48:46)
    0000   0x6e 0xb0 0x40 0x08 0x0d                   n.@..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 27 LowReservoir 2013-06-08T01:37:30 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-06-08T01:37:30)
    0000   0x5e 0xa5 0x01 0x08 0x0d                   ^....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 28 LowReservoir 2013-06-08T12:27:16 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-06-08T12:27:16)
    0000   0x50 0x9b 0x0c 0x08 0x0d                   P....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 PumpSuspend 2013-06-08T20:59:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-08T20:59:09)
    0000   0x49 0xbb 0x14 0x08 0x0d                   I....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 30 PumpResume 2013-06-08T21:00:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-08T21:00:03)
    0000   0x43 0x80 0x15 0x08 0x0d                   C....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 CalBGForPH 2013-06-08T21:01:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 228}
```
    op hex (2)
    0000   0x0a 0xe4                                  ..
    decimal
             10  228
    datetime (2013-06-08T21:01:28)
    0000   0x5c 0x81 0x35 0x08 0x0d                   \.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 BolusWizard 2013-06-08T21:01:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 228,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe4                                  [.
    decimal
             91  228
    datetime (2013-06-08T21:01:30)
    0000   0x5e 0x81 0x15 0x08 0x0d                   ^....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    0    0   22  125
    HOUR BITS: [1, 0, 0]
#### RECORD 33 Bolus 2013-06-08T21:01:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-06-08T21:01:31)
    0000   0x5f 0x81 0x55 0x08 0x0d                   _.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 34 PumpSuspend 2013-06-08T21:03:14 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-08T21:03:14)
    0000   0x4e 0x83 0x15 0x08 0x0d                   N....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 PumpResume 2013-06-08T21:21:45 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-08T21:21:45)
    0000   0x6d 0x95 0x15 0x08 0x0d                   m....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 Rewind 2013-06-08T21:21:49 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-06-08T21:21:49)
    0000   0x71 0x95 0x15 0x08 0x0d                   q....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 37 Prime 2013-06-08T21:23:16 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1d                   .....
    decimal
              3    0    0    0   29
    datetime (2013-06-08T21:23:16)
    0000   0x50 0x97 0x35 0x08 0x0d                   P.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 38 Prime 2013-06-08T21:23:36 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-06-08T21:23:36)
    0000   0x64 0x97 0x15 0x08 0x0d                   d....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 CalBGForPH 2013-06-08T21:39:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 223}
```
    op hex (2)
    0000   0x0a 0xdf                                  ..
    decimal
             10  223
    datetime (2013-06-08T21:39:10)
    0000   0x4a 0xa7 0x35 0x08 0x0d                   J.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 40 BolusWizard 2013-06-08T21:39:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 223,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdf                                  [.
    decimal
             91  223
    datetime (2013-06-08T21:39:28)
    0000   0x5c 0xa7 0x15 0x08 0x0d                   \....
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0x15 0x2b 0x00    9P.-j.+.
    0008   0x00 0x14 0x00 0x2c 0x7d                   ...,}
    decimal
             57   80   13   45  106   21   43    0
              0   20    0   44  125
    HOUR BITS: [1, 0, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 2.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x2d 0x04                   \.X-.
    decimal
             92    5   88   45    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-06-08T21:39:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-06-08T21:39:29)
    0000   0x5d 0xa7 0x55 0x08 0x0d                   ].U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 43 CalBGForPH 2013-06-08T22:21:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 243}
```
    op hex (2)
    0000   0x0a 0xf3                                  ..
    decimal
             10  243
    datetime (2013-06-08T22:21:50)
    0000   0x72 0x95 0x36 0x08 0x0d                   r.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 44 CalBGForPH 2013-06-08T22:35:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 243}
```
    op hex (2)
    0000   0x0a 0xf3                                  ..
    decimal
             10  243
    datetime (2013-06-08T22:35:06)
    0000   0x46 0xa3 0x36 0x08 0x0d                   F.6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 45 CalBGForPH 2013-06-08T22:36:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 241}
```
    op hex (2)
    0000   0x0a 0xf1                                  ..
    decimal
             10  241
    datetime (2013-06-08T22:36:55)
    0000   0x77 0xa4 0x36 0x08 0x0d                   w.6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 46 BolusWizard 2013-06-08T22:37:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 25,
 '_byte[7]': 0,
 'bg': 241,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 19,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 1.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 4.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf1                                  [.
    decimal
             91  241
    datetime (2013-06-08T22:37:09)
    0000   0x49 0xa5 0x16 0x08 0x0d                   I....
    body (13)
    hex
    0000   0x13 0x50 0x0d 0x2d 0x6a 0x19 0x0e 0x00    .P.-j...
    0008   0x00 0x30 0x00 0x0e 0x7d                   .0..}
    decimal
             19   80   13   45  106   25   14    0
              0   48    0   14  125
    HOUR BITS: [1, 0, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 63, 'amount': 4.4, 'curve': 4},
 {'age': 103, 'amount': 2.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb0 0x3f 0x04 0x58 0x67 0x04    \..?.Xg.
    decimal
             92    8  176   63    4   88  103    4
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-06-08T22:37:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-06-08T22:37:09)
    0000   0x49 0xa5 0x56 0x08 0x0d                   I.V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 MResultTotals (2013, 0, 8, 22, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 8, 22, 5, 0))
    0000   0x00 0x05 0x76 0x68 0x0d                   ..vh.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 50 Model522ResultTotals 2013-06-09T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-09T00:00:00)
    0000   0x68 0x0d                                  h.
    body (41)
    hex
    0000   0x05 0x00 0xd6 0x6b 0xf3 0x06 0x00 0x00    ...k....
    0008   0x05 0x76 0x03 0x76 0x3f 0x02 0x00 0x25    .v.v?..%
    0010   0x00 0x8b 0x02 0x00 0x25 0x01 0xa4 0x52    ....%..R
    0018   0x00 0x5c 0x12 0x00 0x00 0x00 0x04 0x02    .\......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  214  107  243    6    0    0
              5  118    3  118   63    2    0   37
              0  139    2    0   37    1  164   82
              0   92   18    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0

#### RECORD 51 CalBGForPH 2013-06-09T05:58:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 281}
```
    op hex (2)
    0000   0x0a 0x19                                  ..
    decimal
             10   25
    datetime (2013-06-09T05:58:25)
    0000   0x59 0xba 0x25 0x09 0x8d                   Y.%..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 52 BolusWizard 2013-06-09T05:58:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 34,
 '_byte[7]': 0,
 'bg': 281,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x19                                  [.
    decimal
             91   25
    datetime (2013-06-09T05:58:27)
    0000   0x5b 0xba 0x05 0x09 0x0d                   [....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x22 0x00 0x00    .Q.-j"..
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
              0   81   13   45  106   34    0    0
              0    0    0   34  125
    HOUR BITS: [1, 0, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 188, 'amount': 1.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0xbc 0x14                   \.8..
    decimal
             92    5   56  188   20
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-06-09T05:58:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-06-09T05:58:27)
    0000   0x5b 0xba 0x45 0x09 0x0d                   [.E..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 55 CalBGForPH 2013-06-09T19:17:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 81}
```
    op hex (2)
    0000   0x0a 0x51                                  .Q
    decimal
             10   81
    datetime (2013-06-09T19:17:54)
    0000   0x76 0x91 0x33 0x09 0x0d                   v.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 BolusWizard 2013-06-09T19:18:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 81,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x51                                  [Q
    decimal
             91   81
    datetime (2013-06-09T19:18:04)
    0000   0x44 0x92 0x13 0x09 0x0d                   D....
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0xfa 0x35 0xf0    EP.-j.5.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             69   80   13   45  106  250   53  240
              0    0    0   47  125
    HOUR BITS: [1, 0, 0]
#### RECORD 57 Bolus 2013-06-09T19:18:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-06-09T19:18:04)
    0000   0x44 0x92 0x53 0x09 0x0d                   D.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 58 BolusWizard 2013-06-09T21:26:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
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
    datetime (2013-06-09T21:26:55)
    0000   0x77 0x9a 0x15 0x09 0x0d                   w....
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    0    0   18  125
    HOUR BITS: [1, 0, 0]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 132, 'amount': 4.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xbc 0x84 0x04                   \....
    decimal
             92    5  188  132    4
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-06-09T21:26:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-06-09T21:26:55)
    0000   0x77 0x9a 0x55 0x09 0x0d                   w.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 61 CalBGForPH 2013-06-09T23:29:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 264}
```
    op hex (2)
    0000   0x0a 0x08                                  ..
    decimal
             10    8
    datetime (2013-06-09T23:29:31)
    0000   0x5f 0x9d 0x37 0x09 0x8d                   _.7..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 BolusWizard 2013-06-09T23:29:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 264,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x08                                  [.
    decimal
             91    8
    datetime (2013-06-09T23:29:50)
    0000   0x72 0x9d 0x17 0x09 0x0d                   r....
    body (13)
    hex
    0000   0x22 0x51 0x0d 0x2d 0x6a 0x1e 0x1a 0x00    "Q.-j...
    0008   0x00 0x08 0x00 0x30 0x7d                   ...0}
    decimal
             34   81   13   45  106   30   26    0
              0    8    0   48  125
    HOUR BITS: [1, 0, 0]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 1.8, 'curve': 4},
 {'age': 255, 'amount': 4.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0x7d 0x04 0xbc 0xff 0x04    \.H}....
    decimal
             92    8   72  125    4  188  255    4
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-06-09T23:29:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2013-06-09T23:29:50)
    0000   0x72 0x9d 0x57 0x09 0x0d                   r.W..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 65 MResultTotals (2013, 0, 9, 16, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 9, 16, 5, 0))
    0000   0x00 0x05 0xd0 0x69 0x0d                   ...i.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 66 Model522ResultTotals 2013-06-10T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-10T00:00:00)
    0000   0x69 0x0d                                  i.
    body (41)
    hex
    0000   0x05 0x10 0xd1 0x51 0x19 0x03 0x00 0x00    ...Q....
    0008   0x05 0xd0 0x03 0x84 0x3c 0x02 0x4c 0x28    ....<.L(
    0010   0x00 0x7f 0x02 0x4c 0x28 0x01 0x6c 0x3e    ...L(.l>
    0018   0x00 0xe0 0x26 0x00 0x00 0x00 0x04 0x02    ..&.....
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  209   81   25    3    0    0
              5  208    3  132   60    2   76   40
              0  127    2   76   40    1  108   62
              0  224   38    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0

#### RECORD 67 CalBGForPH 2013-06-10T01:24:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-06-10T01:24:03)
    0000   0x43 0x98 0x21 0x0a 0x0d                   C.!..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 68 PumpSuspend 2013-06-10T13:30:34 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-10T13:30:34)
    0000   0x62 0x9e 0x0d 0x0a 0x0d                   b....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 PumpResume 2013-06-10T13:50:39 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-10T13:50:39)
    0000   0x67 0xb2 0x0d 0x0a 0x0d                   g....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 70 CalBGForPH 2013-06-10T14:36:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 263}
```
    op hex (2)
    0000   0x0a 0x07                                  ..
    decimal
             10    7
    datetime (2013-06-10T14:36:25)
    0000   0x59 0xa4 0x2e 0x0a 0x8d                   Y....
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 71 BolusWizard 2013-06-10T14:36:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 263,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x07                                  [.
    decimal
             91    7
    datetime (2013-06-10T14:36:32)
    0000   0x60 0xa4 0x0e 0x0a 0x0d                   `....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1e 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
              0   81   13   45  106   30    0    0
              0    0    0   30  125
    HOUR BITS: [1, 0, 1]
#### RECORD 72 Bolus 2013-06-10T14:36:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-06-10T14:36:32)
    0000   0x60 0xa4 0x4e 0x0a 0x0d                   `.N..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 73 CalBGForPH 2013-06-10T16:04:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-06-10T16:04:21)
    0000   0x55 0x84 0x30 0x0a 0x0d                   U.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 74 CalBGForPH 2013-06-10T16:05:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-06-10T16:05:08)
    0000   0x48 0x85 0x30 0x0a 0x0d                   H.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 75 BolusWizard 2013-06-10T16:05:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-06-10T16:05:27)
    0000   0x5b 0x85 0x10 0x0a 0x0d                   [....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x02 0x13 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    2   19    0
              0   22    0   19  125
    HOUR BITS: [1, 0, 0]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 3.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x88 0x5b 0x04                   \..[.
    decimal
             92    5  136   91    4
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2013-06-10T16:05:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-06-10T16:05:27)
    0000   0x5b 0x85 0x50 0x0a 0x0d                   [.P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 78 CalBGForPH 2013-06-10T19:15:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-06-10T19:15:34)
    0000   0x62 0x8f 0x33 0x0a 0x0d                   b.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 79 BolusWizard 2013-06-10T19:23:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 6,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.4,
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
    datetime (2013-06-10T19:23:56)
    0000   0x78 0x97 0x13 0x0a 0x0d                   x....
    body (13)
    hex
    0000   0x06 0x50 0x0d 0x2d 0x6a 0x00 0x04 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
              6   80   13   45  106    0    4    0
              0    0    0    4  125
    HOUR BITS: [1, 0, 0]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 199, 'amount': 1.9, 'curve': 4},
 {'age': 33, 'amount': 3.4, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0xc7 0x04 0x88 0x21 0x14    \.L...!.
    decimal
             92    8   76  199    4  136   33   20
    datetime (unknown)

    body (0)

#### RECORD 81 Bolus 2013-06-10T19:23:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-06-10T19:23:56)
    0000   0x78 0x97 0x53 0x0a 0x0d                   x.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 82 CalBGForPH 2013-06-10T20:36:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-06-10T20:36:35)
    0000   0x63 0xa4 0x34 0x0a 0x0d                   c.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 83 BolusWizard 2013-06-10T20:36:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 172,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2013-06-10T20:36:39)
    0000   0x67 0xa4 0x14 0x0a 0x0d                   g....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x07 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    3    0    7  125
    HOUR BITS: [1, 0, 1]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-13.data: 84 records`
