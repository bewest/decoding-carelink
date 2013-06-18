## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 1005, found 17 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1c 0x46                                  .F
##### DEBUG DECIMAL
             28   70
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
#### RECORD 17 ResultTotals 2013-02-27T13:13:59 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xc4                   .....
    decimal
              7    0    0    5  196
    datetime (2013-02-27T13:13:59)
    0000   0x3b 0x8d 0x6d 0x3b 0x8d                   ;.m;.
    body (41)
    hex
    0000   0x05 0x10 0xb5 0x4b 0x39 0x06 0x00 0x00    ...K9...
    0008   0x05 0xc4 0x03 0x6c 0x3b 0x02 0x58 0x29    ...l;.X)
    0010   0x00 0x93 0x02 0x58 0x29 0x01 0x90 0x43    ...X)..C
    0018   0x00 0xc8 0x21 0x00 0x00 0x00 0x07 0x04    ..!.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  181   75   57    6    0    0
              5  196    3  108   59    2   88   41
              0  147    2   88   41    1  144   67
              0  200   33    0    0    0    7    4
              3    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 PumpSuspend 2013-03-28T11:12:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-28T11:12:20)
    0000   0x14 0xcc 0x0b 0x1c 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 PumpResume 2013-03-28T11:45:10 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-28T11:45:10)
    0000   0x0a 0xed 0x0b 0x1c 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 CalBGForPH 2013-03-28T11:57:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-03-28T11:57:16)
    0000   0x10 0xf9 0x2b 0x1c 0x0d                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 BolusWizard 2013-03-28T11:57:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-03-28T11:57:18)
    0000   0x12 0xf9 0x0b 0x1c 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0    0    0   15  125
    HOUR BITS: [1, 1, 1]
#### RECORD 22 Bolus 2013-03-28T11:57:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-03-28T11:57:18)
    0000   0x12 0xf9 0x4b 0x1c 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 23 CalBGForPH 2013-03-28T13:13:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-03-28T13:13:04)
    0000   0x04 0xcd 0x2d 0x1c 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 BolusWizard 2013-03-28T13:13:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 5,
 '_byte[7]': 0,
 'bg': 151,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 2.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x97                                  [.
    decimal
             91  151
    datetime (2013-03-28T13:13:16)
    0000   0x10 0xcd 0x0d 0x1c 0x0d                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x05 0x1b 0x00    $P.-j...
    0008   0x00 0x0b 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    5   27    0
              0   11    0   27  125
    HOUR BITS: [1, 1, 0]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 1.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x4f 0x04                   \.<O.
    decimal
             92    5   60   79    4
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-03-28T13:13:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-03-28T13:13:16)
    0000   0x10 0xcd 0x4d 0x1c 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 CalBGForPH 2013-03-28T14:32:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 250}
```
    op hex (2)
    0000   0x0a 0xfa                                  ..
    decimal
             10  250
    datetime (2013-03-28T14:32:56)
    0000   0x38 0xe0 0x2e 0x1c 0x0d                   8....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 BolusWizard 2013-03-28T14:33:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 27,
 '_byte[7]': 0,
 'bg': 250,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfa                                  [.
    decimal
             91  250
    datetime (2013-03-28T14:33:18)
    0000   0x12 0xe1 0x0e 0x1c 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1b 0x00 0x00    .P.-j...
    0008   0x00 0x17 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   27    0    0
              0   23    0    4  125
    HOUR BITS: [1, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 1.65, 'curve': 4},
 {'age': 89, 'amount': 1.05, 'curve': 4},
 {'age': 159, 'amount': 1.5, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x42 0x4f 0x04 0x2a 0x59 0x04    \.BO.*Y.
    0008   0x3c 0x9f 0x04                             <..
    decimal
             92   11   66   79    4   42   89    4
             60  159    4
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-03-28T14:33:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-03-28T14:33:19)
    0000   0x13 0xe1 0x4e 0x1c 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 BolusWizard 2013-03-28T14:36:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.5,
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
    datetime (2013-03-28T14:36:54)
    0000   0x36 0xe4 0x0e 0x1c 0x0d                   6....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125
    HOUR BITS: [1, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 0.6, 'curve': 4},
 {'age': 82, 'amount': 1.65, 'curve': 4},
 {'age': 92, 'amount': 1.05, 'curve': 4},
 {'age': 162, 'amount': 1.5, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x0c 0x04 0x42 0x52 0x04    \....BR.
    0008   0x2a 0x5c 0x04 0x3c 0xa2 0x04              *\.<..
    decimal
             92   14   24   12    4   66   82    4
             42   92    4   60  162    4
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-03-28T14:36:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-03-28T14:36:54)
    0000   0x36 0xe4 0x4e 0x1c 0x0d                   6.N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 CalBGForPH 2013-03-28T15:42:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 332}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-03-28T15:42:13)
    0000   0x0d 0xea 0x2f 0x1c 0x8d                   ../..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 35 BolusWizard 2013-03-28T15:42:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 46,
 '_byte[7]': 0,
 'bg': 332,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4c                                  [L
    decimal
             91   76
    datetime (2013-03-28T15:42:37)
    0000   0x25 0xea 0x0f 0x1c 0x0d                   %....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2e 0x00 0x00    .Q.-j...
    0008   0x00 0x19 0x00 0x15 0x7d                   ....}
    decimal
              0   81   13   45  106   46    0    0
              0   25    0   21  125
    HOUR BITS: [1, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 1.5, 'curve': 4},
 {'age': 78, 'amount': 0.6, 'curve': 4},
 {'age': 148, 'amount': 1.65, 'curve': 4},
 {'age': 158, 'amount': 1.05, 'curve': 4},
 {'age': 228, 'amount': 1.5, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x3c 0x44 0x04 0x18 0x4e 0x04    \.<D..N.
    0008   0x42 0x94 0x04 0x2a 0x9e 0x04 0x3c 0xe4    B..*..<.
    0010   0x04                                       .
    decimal
             92   17   60   68    4   24   78    4
             66  148    4   42  158    4   60  228
              4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-03-28T15:42:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-03-28T15:42:38)
    0000   0x26 0xea 0x4f 0x1c 0x0d                   &.O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 CalBGForPH 2013-03-28T17:54:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 250}
```
    op hex (2)
    0000   0x0a 0xfa                                  ..
    decimal
             10  250
    datetime (2013-03-28T17:54:43)
    0000   0x2b 0xf6 0x31 0x1c 0x0d                   +.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 BolusWizard 2013-03-28T17:54:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 27,
 '_byte[7]': 0,
 'bg': 250,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfa                                  [.
    decimal
             91  250
    datetime (2013-03-28T17:54:47)
    0000   0x2f 0xf6 0x11 0x1c 0x0d                   /....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1b 0x00 0x00    .P.-j...
    0008   0x00 0x0c 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   27    0    0
              0   12    0   15  125
    HOUR BITS: [1, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 130, 'amount': 0.45, 'curve': 4},
 {'age': 140, 'amount': 2.05, 'curve': 4},
 {'age': 200, 'amount': 1.5, 'curve': 4},
 {'age': 210, 'amount': 0.6, 'curve': 4},
 {'age': 24, 'amount': 1.65, 'curve': 20},
 {'age': 34, 'amount': 1.05, 'curve': 20},
 {'age': 104, 'amount': 1.5, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x12 0x82 0x04 0x52 0x8c 0x04    \....R..
    0008   0x3c 0xc8 0x04 0x18 0xd2 0x04 0x42 0x18    <.....B.
    0010   0x14 0x2a 0x22 0x14 0x3c 0x68 0x14         .*".<h.
    decimal
             92   23   18  130    4   82  140    4
             60  200    4   24  210    4   66   24
             20   42   34   20   60  104   20
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2013-03-28T17:54:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-03-28T17:54:47)
    0000   0x2f 0xf6 0x51 0x1c 0x0d                   /.Q..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 CalBGForPH 2013-03-28T21:17:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 308}
```
    op hex (2)
    0000   0x0a 0x34                                  .4
    decimal
             10   52
    datetime (2013-03-28T21:17:17)
    0000   0x11 0xd1 0x35 0x1c 0x8d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 BolusWizard 2013-03-28T21:17:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 40,
 '_byte[7]': 0,
 'bg': 308,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x34                                  [4
    decimal
             91   52
    datetime (2013-03-28T21:17:32)
    0000   0x20 0xd1 0x15 0x1c 0x0d                    ....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x28 0x00 0x00    .Q.-j(..
    0008   0x00 0x02 0x00 0x26 0x7d                   ...&}
    decimal
              0   81   13   45  106   40    0    0
              0    2    0   38  125
    HOUR BITS: [1, 1, 0]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 203, 'amount': 1.5, 'curve': 4},
 {'age': 77, 'amount': 0.45, 'curve': 20},
 {'age': 87, 'amount': 2.05, 'curve': 20},
 {'age': 147, 'amount': 1.5, 'curve': 20},
 {'age': 157, 'amount': 0.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x3c 0xcb 0x04 0x12 0x4d 0x14    \.<...M.
    0008   0x52 0x57 0x14 0x3c 0x93 0x14 0x18 0x9d    RW.<....
    0010   0x14                                       .
    decimal
             92   17   60  203    4   18   77   20
             82   87   20   60  147   20   24  157
             20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-03-28T21:17:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-03-28T21:17:32)
    0000   0x20 0xd1 0x55 0x1c 0x0d                    .U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 46 CalBGForPH 2013-03-28T22:15:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2013-03-28T22:15:23)
    0000   0x17 0xcf 0x36 0x1c 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 47 CalBGForPH 2013-03-28T23:06:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 134}
```
    op hex (2)
    0000   0x0a 0x86                                  ..
    decimal
             10  134
    datetime (2013-03-28T23:06:54)
    0000   0x36 0xc6 0x37 0x1c 0x0d                   6.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 BolusWizard 2013-03-28T23:07:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 134,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 30,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x86                                  [.
    decimal
             91  134
    datetime (2013-03-28T23:07:07)
    0000   0x07 0xc7 0x17 0x1c 0x0d                   .....
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x02 0x17 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106    2   23    0
              0   22    0   23  125
    HOUR BITS: [1, 1, 0]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 113, 'amount': 4.3, 'curve': 4},
 {'age': 57, 'amount': 1.5, 'curve': 20},
 {'age': 187, 'amount': 0.45, 'curve': 20},
 {'age': 197, 'amount': 2.05, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xac 0x71 0x04 0x3c 0x39 0x14    \..q.<9.
    0008   0x12 0xbb 0x14 0x52 0xc5 0x14              ...R..
    decimal
             92   14  172  113    4   60   57   20
             18  187   20   82  197   20
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2013-03-28T23:07:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-03-28T23:07:07)
    0000   0x07 0xc7 0x57 0x1c 0x0d                   ..W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 51 ResultTotals (2013, 2, 28, 13, 13, 60) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x10                   .....
    decimal
              7    0    0    6   16
    datetime ((2013, 2, 28, 13, 13, 60))
    0000   0x3c 0x8d 0x6d 0x3c 0x8d                   <.m<.
    body (41)
    hex
    0000   0x05 0x10 0xda 0x81 0x4c 0x08 0x00 0x00    ....L...
    0008   0x06 0x10 0x03 0x6c 0x38 0x02 0xa4 0x2c    ...l8..,
    0010   0x00 0x56 0x02 0xa4 0x2c 0x01 0x04 0x26    .V..,..&
    0018   0x01 0xa0 0x3e 0x00 0x00 0x00 0x08 0x03    ..>.....
    0020   0x05 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  218  129   76    8    0    0
              6   16    3  108   56    2  164   44
              0   86    2  164   44    1    4   38
              1  160   62    0    0    0    8    3
              5    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 52 CalBGForPH 2013-03-29T03:03:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 191}
```
    op hex (2)
    0000   0x0a 0xbf                                  ..
    decimal
             10  191
    datetime (2013-03-29T03:03:18)
    0000   0x12 0xc3 0x23 0x1d 0x0d                   ..#..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 BolusWizard 2013-03-29T03:03:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 191,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbf                                  [.
    decimal
             91  191
    datetime (2013-03-29T03:03:21)
    0000   0x15 0xc3 0x03 0x1d 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x0c 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    2    0   12  125
    HOUR BITS: [1, 1, 0]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 239, 'amount': 2.3, 'curve': 4},
 {'age': 93, 'amount': 4.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x5c 0xef 0x04 0xac 0x5d 0x14    \.\...].
    decimal
             92    8   92  239    4  172   93   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-03-29T03:03:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-03-29T03:03:21)
    0000   0x15 0xc3 0x43 0x1d 0x0d                   ..C..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 PumpSuspend 2013-03-29T13:46:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-29T13:46:49)
    0000   0x31 0xee 0x0d 0x1d 0x0d                   1....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 57 PumpResume 2013-03-29T14:08:01 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-29T14:08:01)
    0000   0x01 0xc8 0x0e 0x1d 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 58 CalBGForPH 2013-03-29T15:40:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-03-29T15:40:33)
    0000   0x21 0xe8 0x2f 0x1d 0x0d                   !./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 59 CalBGForPH 2013-03-29T16:07:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-03-29T16:07:51)
    0000   0x33 0xc7 0x30 0x1d 0x0d                   3.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 60 BolusWizard 2013-03-29T16:08:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
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
    datetime (2013-03-29T16:08:37)
    0000   0x25 0xc8 0x10 0x1d 0x0d                   %....
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0x00 0x28 0x00    5P.-j.(.
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
             53   80   13   45  106    0   40    0
              0    0    0   40  125
    HOUR BITS: [1, 1, 0]
#### RECORD 61 Bolus 2013-03-29T16:08:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-03-29T16:08:37)
    0000   0x25 0xc8 0x50 0x1d 0x0d                   %.P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 CalBGForPH 2013-03-29T18:15:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-03-29T18:15:28)
    0000   0x1c 0xcf 0x32 0x1d 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 CalBGForPH 2013-03-29T21:41:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-03-29T21:41:42)
    0000   0x2a 0xe9 0x35 0x1d 0x0d                   *.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 64 BolusWizard 2013-03-29T21:41:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 72,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x48                                  [H
    decimal
             91   72
    datetime (2013-03-29T21:41:59)
    0000   0x3b 0xe9 0x15 0x1d 0x0d                   ;....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0xf8 0x27 0xf0    3P.-j.'.
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             51   80   13   45  106  248   39  240
              0    0    0   31  125
    HOUR BITS: [1, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 81, 'amount': 4.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0x51 0x14                   \..Q.
    decimal
             92    5  160   81   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-03-29T21:42:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-03-29T21:42:00)
    0000   0x00 0xea 0x55 0x1d 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 CalBGForPH 2013-03-29T22:34:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-03-29T22:34:35)
    0000   0x23 0xe2 0x36 0x1d 0x0d                   #.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 CalBGForPH 2013-03-29T22:36:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-03-29T22:36:20)
    0000   0x14 0xe4 0x36 0x1d 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 BolusWizard 2013-03-29T22:37:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-03-29T22:37:18)
    0000   0x12 0xe5 0x16 0x1d 0x0d                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xff 0x18 0xf0     P.-j...
    0008   0x00 0x19 0x00 0x17 0x7d                   ....}
    decimal
             32   80   13   45  106  255   24  240
              0   25    0   23  125
    HOUR BITS: [1, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 0.1, 'curve': 4},
 {'age': 63, 'amount': 3.0, 'curve': 4},
 {'age': 137, 'amount': 4.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x04 0x35 0x04 0x78 0x3f 0x04    \..5.x?.
    0008   0xa0 0x89 0x14                             ...
    decimal
             92   11    4   53    4  120   63    4
            160  137   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-03-29T22:37:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-03-29T22:37:18)
    0000   0x12 0xe5 0x56 0x1d 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 CalBGForPH 2013-03-29T23:54:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-03-29T23:54:57)
    0000   0x39 0xf6 0x37 0x1d 0x0d                   9.7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 73 ResultTotals (2013, 2, 29, 13, 13, 61) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x1e                   .....
    decimal
              7    0    0    5   30
    datetime ((2013, 2, 29, 13, 13, 61))
    0000   0x3d 0x8d 0x6d 0x3d 0x8d                   =.m=.
    body (41)
    hex
    0000   0x05 0x00 0x73 0x48 0xbf 0x08 0x00 0x00    ..sH....
    0008   0x05 0x1e 0x03 0x76 0x44 0x01 0xa8 0x20    ...vD.. 
    0010   0x00 0x88 0x01 0xa8 0x20 0x01 0x78 0x59    .... .xY
    0018   0x00 0x30 0x0b 0x00 0x00 0x00 0x04 0x03    .0......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  115   72  191    8    0    0
              5   30    3  118   68    1  168   32
              0  136    1  168   32    1  120   89
              0   48   11    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 74 PumpSuspend 2013-03-30T14:42:43 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-30T14:42:43)
    0000   0x2b 0xea 0x0e 0x1e 0x0d                   +....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 75 PumpResume 2013-03-30T15:03:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-30T15:03:40)
    0000   0x28 0xc3 0x0f 0x1e 0x0d                   (....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 CalBGForPH 2013-03-30T22:31:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-03-30T22:31:13)
    0000   0x0d 0xdf 0x36 0x1e 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-21.data: 77 records`
