## START logs/ReadHistoryData-page-32.data
#### STOPPING DOUBLE NULLS @ 470, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x19 0x00 0x15 0x7d 0x5c 0x11 0x3c 0x44    ...}\.<D
    0008   0x04 0x18 0x4e 0x04 0x42 0x94 0x04 0x2a    ..N.B..*
    0010   0x9e 0x04 0x3c 0xe4 0x04 0x01 0x19 0x19    ..<.....
    0018   0x00 0x26 0xea 0x4f 0x1c 0x0d 0x0a 0xfa    .&.O....
##### DEBUG DECIMAL
             25    0   21  125   92   17   60   68
              4   24   78    4   66  148    4   42
            158    4   60  228    4    1   25   25
              0   38  234   79   28   13   10  250
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 0.6, 'curve': 4},
 {'age': 158, 'amount': 4.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0x30 0x04 0xbc 0x9e 0x04    \..0....
    decimal
             92    8   24   48    4  188  158    4
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-03-27T18:12:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-03-27T18:12:01)
    0000   0x01 0xcc 0x52 0x1b 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2013-03-27T18:40:09 head[2], body[13] op[0x5b]
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
    datetime (2013-03-27T18:40:09)
    0000   0x09 0xe8 0x12 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [1, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 2.5, 'curve': 4},
 {'age': 76, 'amount': 0.6, 'curve': 4},
 {'age': 186, 'amount': 4.7, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x64 0x24 0x04 0x18 0x4c 0x04    \.d$..L.
    0008   0xbc 0xba 0x04                             ...
    decimal
             92   11  100   36    4   24   76    4
            188  186    4
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-03-27T18:40:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-03-27T18:40:10)
    0000   0x0a 0xe8 0x52 0x1b 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 BolusWizard 2013-03-27T18:47:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 11,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.8,
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
    datetime (2013-03-27T18:47:43)
    0000   0x2b 0xef 0x12 0x1b 0x0d                   +....
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0    0    0    8  125
    HOUR BITS: [1, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 1.9, 'curve': 4},
 {'age': 43, 'amount': 2.5, 'curve': 4},
 {'age': 83, 'amount': 0.6, 'curve': 4},
 {'age': 193, 'amount': 4.7, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x4c 0x0d 0x04 0x64 0x2b 0x04    \.L..d+.
    0008   0x18 0x53 0x04 0xbc 0xc1 0x04              .S....
    decimal
             92   14   76   13    4  100   43    4
             24   83    4  188  193    4
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-03-27T18:47:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-03-27T18:47:43)
    0000   0x2b 0xef 0x52 0x1b 0x0d                   +.R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 CalBGForPH 2013-03-27T21:07:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 273}
```
    op hex (2)
    0000   0x0a 0x11                                  ..
    decimal
             10   17
    datetime (2013-03-27T21:07:22)
    0000   0x16 0xc7 0x35 0x1b 0x8d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 BolusWizard 2013-03-27T21:07:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 273,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x11                                  [.
    decimal
             91   17
    datetime (2013-03-27T21:07:54)
    0000   0x36 0xc7 0x15 0x1b 0x0d                   6....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x0d 0x00 0x13 0x7d                   ....}
    decimal
              0   81   13   45  106   32    0    0
              0   13    0   19  125
    HOUR BITS: [1, 1, 0]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 143, 'amount': 0.8, 'curve': 4},
 {'age': 153, 'amount': 1.9, 'curve': 4},
 {'age': 183, 'amount': 2.5, 'curve': 4},
 {'age': 223, 'amount': 0.6, 'curve': 4},
 {'age': 77, 'amount': 4.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x8f 0x04 0x4c 0x99 0x04    \. ..L..
    0008   0x64 0xb7 0x04 0x18 0xdf 0x04 0xbc 0x4d    d......M
    0010   0x14                                       .
    decimal
             92   17   32  143    4   76  153    4
            100  183    4   24  223    4  188   77
             20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-03-27T21:07:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-03-27T21:07:54)
    0000   0x36 0xc7 0x55 0x1b 0x0d                   6.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2013-03-27T23:05:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-03-27T23:05:04)
    0000   0x04 0xc5 0x37 0x1b 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 CalBGForPH 2013-03-27T23:16:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-03-27T23:16:53)
    0000   0x35 0xd0 0x37 0x1b 0x0d                   5.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 BolusWizard 2013-03-27T23:17:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-03-27T23:17:07)
    0000   0x07 0xd1 0x17 0x1b 0x0d                   .....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0xf9 0x21 0xf0    ,P.-j.!.
    0008   0x00 0x08 0x00 0x1a 0x7d                   ....}
    decimal
             44   80   13   45  106  249   33  240
              0    8    0   26  125
    HOUR BITS: [1, 1, 0]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 133, 'amount': 1.9, 'curve': 4},
 {'age': 17, 'amount': 0.8, 'curve': 20},
 {'age': 27, 'amount': 1.9, 'curve': 20},
 {'age': 57, 'amount': 2.5, 'curve': 20},
 {'age': 97, 'amount': 0.6, 'curve': 20},
 {'age': 207, 'amount': 4.7, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x4c 0x85 0x04 0x20 0x11 0x14    \.L.. ..
    0008   0x4c 0x1b 0x14 0x64 0x39 0x14 0x18 0x61    L..d9..a
    0010   0x14 0xbc 0xcf 0x14                        ....
    decimal
             92   20   76  133    4   32   17   20
             76   27   20  100   57   20   24   97
             20  188  207   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-03-27T23:17:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-03-27T23:17:07)
    0000   0x07 0xd1 0x57 0x1b 0x0d                   ..W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 ResultTotals 2013-02-27T13:13:59 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xc4                   .....
    decimal
              7    0    0    5  196
    datetime (2013-02-27T13:13:59)
    0000   0x3b 0x8d 0x6d 0x3b 0x8d                   ;.m;.
    body (51)
    hex
    0000   0x05 0x10 0xb5 0x4b 0x39 0x06 0x00 0x00    ...K9...
    0008   0x05 0xc4 0x03 0x6c 0x3b 0x02 0x58 0x29    ...l;.X)
    0010   0x00 0x93 0x02 0x58 0x29 0x01 0x90 0x43    ...X)..C
    0018   0x00 0xc8 0x21 0x00 0x00 0x00 0x07 0x04    ..!.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x14 0xcc 0x0b 0x1c 0x0d    ........
    0030   0x1f 0x00 0x0a                             ...
    decimal
              5   16  181   75   57    6    0    0
              5  196    3  108   59    2   88   41
              0  147    2   88   41    1  144   67
              0  200   33    0    0    0    7    4
              3    0    0   12    0  232    0    0
              0   30    0   20  204   11   28   13
             31    0   10
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 Base (2000, 0, 1, 10, 13, 28) head[2], body[0] op[0xed]

    op hex (2)
    0000   0xed 0x0b                                  ..
    decimal
            237   11
    datetime ((2000, 0, 1, 10, 13, 28))
    0000   0x1c 0x0d 0x0a 0xc1 0x10                   .....
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 19 Base (2002, 0, 1, 27, 13, 28) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x2b                                  .+
    decimal
            249   43
    datetime ((2002, 0, 1, 27, 13, 28))
    0000   0x1c 0x0d 0x5b 0xc1 0x12                   ..[..
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 20 Base (2013, 0, 16, 0, 13, 28) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x0b                                  ..
    decimal
            249   11
    datetime ((2013, 0, 16, 0, 13, 28))
    0000   0x1c 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 21 Base (2000, 0, 0, 0, 0, 15) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 15))
    0000   0x0f 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 22 Base (2000, 4, 15, 15, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0f                                  ..
    decimal
              0   15
    datetime ((2000, 4, 15, 15, 1, 61))
    0000   0x7d 0x01 0x0f 0x0f 0x00                   }....
    body (0)

#### RECORD 23 Base (2007, 4, 10, 13, 28, 11) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0xf9                                  ..
    decimal
             18  249
    datetime ((2007, 4, 10, 13, 28, 11))
    0000   0x4b 0x1c 0x0d 0x0a 0x97                   K....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 24 Base (2007, 0, 27, 13, 28, 45) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0xcd                                  ..
    decimal
              4  205
    datetime ((2007, 0, 27, 13, 28, 45))
    0000   0x2d 0x1c 0x0d 0x5b 0x97                   -..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 25 Base (2000, 0, 4, 13, 28, 13) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0xcd                                  ..
    decimal
             16  205
    datetime ((2000, 0, 4, 13, 28, 13))
    0000   0x0d 0x1c 0x0d 0x24 0x50                   ...$P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 26 Base (2000, 4, 0, 27, 5, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 27, 5, 42))
    0000   0x6a 0x05 0x1b 0x00 0x00                   j....
    body (0)

#### RECORD 27 Ian0B (2015, 5, 28, 5, 28, 61) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x00 0x1b                             ...
    decimal
             11    0   27
    datetime ((2015, 5, 28, 5, 28, 61))
    0000   0x7d 0x5c 0x05 0x3c 0x4f                   }\.<O
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 28 Base (2013, 0, 16, 0, 27, 27) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x01                                  ..
    decimal
              4    1
    datetime ((2013, 0, 16, 0, 27, 27))
    0000   0x1b 0x1b 0x00 0x10 0xcd                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 29 Base (2000, 0, 24, 26, 10, 13) head[2], body[0] op[0x4d]

    op hex (2)
    0000   0x4d 0x1c                                  M.
    decimal
             77   28
    datetime ((2000, 0, 24, 26, 10, 13))
    0000   0x0d 0x0a 0xfa 0x38 0xe0                   ...8.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 1, 0]
#### RECORD 30 Base (2001, 1, 18, 26, 27, 13) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0x1c                                  ..
    decimal
             46   28
    datetime ((2001, 1, 18, 26, 27, 13))
    0000   0x0d 0x5b 0xfa 0x12 0xe1                   .[...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 0]
#### RECORD 31 Base (2013, 0, 13, 16, 0, 13) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x1c                                  ..
    decimal
             14   28
    datetime ((2013, 0, 13, 16, 0, 13))
    0000   0x0d 0x00 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 32 Base (2000, 0, 23, 0, 0, 0) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x1b                                  j.
    decimal
            106   27
    datetime ((2000, 0, 23, 0, 0, 0))
    0000   0x00 0x00 0x00 0x17 0x00                   .....
    body (0)

#### RECORD 33 Base (2004, 4, 15, 2, 11, 28) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x7d                                  .}
    decimal
              4  125
    datetime ((2004, 4, 15, 2, 11, 28))
    0000   0x5c 0x0b 0x42 0x4f 0x04                   \.BO.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 34 Base (2001, 0, 4, 31, 60, 4) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0x59                                  *Y
    decimal
             42   89
    datetime ((2001, 0, 4, 31, 60, 4))
    0000   0x04 0x3c 0x9f 0x04 0x01                   .<...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 NoDelivery (2011, 13, 13, 28, 14, 33) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x00 0x13                        ....
    decimal
              6    6    0   19
    datetime ((2011, 13, 13, 28, 14, 33))
    0000   0xe1 0x4e 0x1c 0x0d 0x5b                   .N..[
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 36 Base (2004, 12, 13, 28, 14, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x36                                  .6
    decimal
              0   54
    datetime ((2004, 12, 13, 28, 14, 36))
    0000   0xe4 0x0e 0x1c 0x0d 0x14                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 37 Ian50 2000-01-15T00:42:45 head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime (2000-01-15T00:42:45)
    0000   0x2d 0x6a 0x00 0x0f 0x00                   -j...
    body (34)
    hex
    0000   0x00 0x00 0x00 0x0f 0x7d 0x5c 0x0e 0x18    ....}\..
    0008   0x0c 0x04 0x42 0x52 0x04 0x2a 0x5c 0x04    ..BR.*\.
    0010   0x3c 0xa2 0x04 0x01 0x0f 0x0f 0x00 0x36    <......6
    0018   0xe4 0x4e 0x1c 0x0d 0x0a 0x4c 0x0d 0xea    .N...L..
    0020   0x2f 0x1c                                  /.
    decimal
              0    0    0   15  125   92   14   24
             12    4   66   82    4   42   92    4
             60  162    4    1   15   15    0   54
            228   78   28   13   10   76   13  234
             47   28
    HOUR BITS: [0, 1, 1]
#### RECORD 38 Base (2012, 4, 15, 10, 37, 12) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x5b                                  .[
    decimal
            141   91
    datetime ((2012, 4, 15, 10, 37, 12))
    0000   0x4c 0x25 0xea 0x0f 0x1c                   L%...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 39 Base (2014, 4, 10, 13, 13, 17) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2014, 4, 10, 13, 13, 17))
    0000   0x51 0x0d 0x2d 0x6a 0x2e                   Q.-j.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 0]
`end logs/ReadHistoryData-page-32.data: 40 records`
