## START logs/ReadHistoryData-page-18.data
#### STOPPING DOUBLE NULLS @ 994, found 28 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x8b 0x3a                                  .:
##### DEBUG DECIMAL
            139   58
#### RECORD 0 Bolus 2013-05-16T00:15:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-05-16T00:15:40)
    0000   0x68 0x4f 0x40 0x10 0x0d                   hO@..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 1 PumpSuspend 2013-05-16T10:57:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-16T10:57:09)
    0000   0x49 0x79 0x0a 0x10 0x0d                   Iy...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 PumpResume 2013-05-16T11:31:51 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-16T11:31:51)
    0000   0x73 0x5f 0x0b 0x10 0x0d                   s_...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 CalBGForPH 2013-05-16T11:59:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2013-05-16T11:59:31)
    0000   0x5f 0x7b 0x2b 0x10 0x0d                   _{+..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 BolusWizard 2013-05-16T11:59:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 253,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfd                                  [.
    decimal
             91  253
    datetime (2013-05-16T11:59:35)
    0000   0x63 0x7b 0x0b 0x10 0x0d                   c{...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    0    0   28  125
    HOUR BITS: [0, 1, 1]
#### RECORD 5 Bolus 2013-05-16T11:59:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-05-16T11:59:35)
    0000   0x63 0x7b 0x4b 0x10 0x0d                   c{K..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2013-05-16T12:34:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 214}
```
    op hex (2)
    0000   0x0a 0xd6                                  ..
    decimal
             10  214
    datetime (2013-05-16T12:34:49)
    0000   0x71 0x62 0x2c 0x10 0x0d                   qb,..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 BolusWizard 2013-05-16T12:35:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 214,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 10,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd6                                  [.
    decimal
             91  214
    datetime (2013-05-16T12:35:33)
    0000   0x61 0x63 0x0c 0x10 0x0d                   ac...
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x13 0x07 0x00    .P.-j...
    0008   0x00 0x1a 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106   19    7    0
              0   26    0    7  125
    HOUR BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 2.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0x29 0x04                   \.p).
    decimal
             92    5  112   41    4
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-05-16T12:35:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-05-16T12:35:33)
    0000   0x61 0x63 0x4c 0x10 0x0d                   acL..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 CalBGForPH 2013-05-16T13:13:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 152}
```
    op hex (2)
    0000   0x0a 0x98                                  ..
    decimal
             10  152
    datetime (2013-05-16T13:13:15)
    0000   0x4f 0x4d 0x2d 0x10 0x0d                   OM-..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 11 BolusWizard 2013-05-16T13:14:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 152,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 2.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x98                                  [.
    decimal
             91  152
    datetime (2013-05-16T13:14:15)
    0000   0x4f 0x4e 0x0d 0x10 0x0d                   ON...
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x06 0x1c 0x00    %P.-j...
    0008   0x00 0x1b 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106    6   28    0
              0   27    0   28  125
    HOUR BITS: [0, 1, 0]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 0.7, 'curve': 4},
 {'age': 80, 'amount': 2.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x1c 0x28 0x04 0x70 0x50 0x04    \..(.pP.
    decimal
             92    8   28   40    4  112   80    4
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-05-16T13:14:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-05-16T13:14:16)
    0000   0x50 0x4e 0x4d 0x10 0x0d                   PNM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 14 CalBGForPH 2013-05-16T13:42:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-05-16T13:42:36)
    0000   0x64 0x6a 0x2d 0x10 0x0d                   dj-..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 15 BolusWizard 2013-05-16T13:42:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
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
    datetime (2013-05-16T13:42:50)
    0000   0x72 0x6a 0x0d 0x10 0x0d                   rj...
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 2.8, 'curve': 4},
 {'age': 68, 'amount': 0.7, 'curve': 4},
 {'age': 108, 'amount': 2.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x1c 0x04 0x1c 0x44 0x04    \.p...D.
    0008   0x70 0x6c 0x04                             pl.
    decimal
             92   11  112   28    4   28   68    4
            112  108    4
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-05-16T13:42:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-05-16T13:42:50)
    0000   0x72 0x6a 0x4d 0x10 0x0d                   rjM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 18 CalBGForPH 2013-05-16T15:49:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2013-05-16T15:49:54)
    0000   0x76 0x71 0x2f 0x10 0x0d                   vq/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 19 LowReservoir 2013-05-16T22:06:18 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-16T22:06:18)
    0000   0x52 0x46 0x16 0x10 0x0d                   RF...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 20 MResultTotals 2013-05-17T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0a                   .....
    decimal
              7    0    0    5   10
    datetime (2013-05-17T00:00:00)
    0000   0x50 0x8d                                  P.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 Model522ResultTotals 2013-05-17T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-17T00:00:00)
    0000   0x50 0x8d                                  P.
    body (41)
    hex
    0000   0x05 0x00 0x9b 0x43 0xfd 0x06 0x00 0x00    ...C....
    0008   0x05 0x0a 0x03 0x6a 0x44 0x01 0xa0 0x20    ...jD.. 
    0010   0x00 0x64 0x01 0xa0 0x20 0x01 0x2c 0x48    .d.. .,H
    0018   0x00 0x74 0x1c 0x00 0x00 0x00 0x05 0x03    .t......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  155   67  253    6    0    0
              5   10    3  106   68    1  160   32
              0  100    1  160   32    1   44   72
              0  116   28    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 22 LowReservoir 2013-05-17T09:38:10 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-05-17T09:38:10)
    0000   0x4a 0x66 0x09 0x11 0x0d                   Jf...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 PumpSuspend 2013-05-17T14:36:06 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-17T14:36:06)
    0000   0x46 0x64 0x0e 0x11 0x0d                   Fd...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 24 PumpResume 2013-05-17T15:16:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-17T15:16:35)
    0000   0x63 0x50 0x0f 0x11 0x0d                   cP...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 25 Rewind 2013-05-17T20:57:51 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-05-17T20:57:51)
    0000   0x73 0x79 0x14 0x11 0x0d                   sy...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 26 Prime 2013-05-17T20:59:58 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.2, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x20                   .... 
    decimal
              3    0    0    0   32
    datetime (2013-05-17T20:59:58)
    0000   0x7a 0x7b 0x34 0x11 0x0d                   z{4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 27 Prime 2013-05-17T21:00:17 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-05-17T21:00:17)
    0000   0x51 0x40 0x15 0x11 0x0d                   Q@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 28 CalBGForPH 2013-05-17T21:43:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 87}
```
    op hex (2)
    0000   0x0a 0x57                                  .W
    decimal
             10   87
    datetime (2013-05-17T21:43:10)
    0000   0x4a 0x6b 0x35 0x11 0x0d                   Jk5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 29 CalBGForPH 2013-05-17T21:44:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 87}
```
    op hex (2)
    0000   0x0a 0x57                                  .W
    decimal
             10   87
    datetime (2013-05-17T21:44:04)
    0000   0x44 0x6c 0x35 0x11 0x0d                   Dl5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 30 BolusWizard 2013-05-17T21:44:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 87,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 67,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 5.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x57                                  [W
    decimal
             91   87
    datetime (2013-05-17T21:44:17)
    0000   0x51 0x6c 0x15 0x11 0x0d                   Ql...
    body (13)
    hex
    0000   0x43 0x50 0x0d 0x2d 0x6a 0xfc 0x33 0xf0    CP.-j.3.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             67   80   13   45  106  252   51  240
              0    0    0   47  125
    HOUR BITS: [0, 1, 1]
#### RECORD 31 Bolus 2013-05-17T21:44:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-05-17T21:44:17)
    0000   0x51 0x6c 0x55 0x11 0x0d                   QlU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 32 CalBGForPH 2013-05-17T22:21:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 54}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2013-05-17T22:21:28)
    0000   0x5c 0x55 0x36 0x11 0x0d                   \U6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 33 CalBGForPH 2013-05-17T22:57:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-05-17T22:57:01)
    0000   0x41 0x79 0x36 0x11 0x0d                   Ay6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 34 MResultTotals 2013-05-18T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x24                   ....$
    decimal
              7    0    0    4   36
    datetime (2013-05-18T00:00:00)
    0000   0x51 0x8d                                  Q.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 Model522ResultTotals 2013-05-18T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-18T00:00:00)
    0000   0x51 0x8d                                  Q.
    body (41)
    hex
    0000   0x05 0x00 0x4c 0x36 0x57 0x04 0x00 0x00    ..L6W...
    0008   0x04 0x24 0x03 0x68 0x52 0x00 0xbc 0x12    .$.hR...
    0010   0x00 0x43 0x00 0xbc 0x12 0x00 0xbc 0x64    .C.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   76   54   87    4    0    0
              4   36    3  104   82    0  188   18
              0   67    0  188   18    0  188  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 36 CalBGForPH 2013-05-18T06:50:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 211}
```
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2013-05-18T06:50:58)
    0000   0x7a 0x72 0x26 0x12 0x0d                   zr&..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 37 BolusWizard 2013-05-18T06:51:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 211,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd3                                  [.
    decimal
             91  211
    datetime (2013-05-18T06:51:00)
    0000   0x40 0x73 0x06 0x12 0x0d                   @s...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x13 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
              0   80   13   45  106   19    0    0
              0    0    0   19  125
    HOUR BITS: [0, 1, 1]
#### RECORD 38 Bolus 2013-05-18T06:51:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-05-18T06:51:00)
    0000   0x40 0x73 0x46 0x12 0x0d                   @sF..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 39 PumpSuspend 2013-05-18T08:11:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-18T08:11:30)
    0000   0x5e 0x4b 0x08 0x12 0x0d                   ^K...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 40 PumpResume 2013-05-18T08:34:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-18T08:34:20)
    0000   0x54 0x62 0x08 0x12 0x0d                   Tb...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 41 CalBGForPH 2013-05-18T09:08:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 270}
```
    op hex (2)
    0000   0x0a 0x0e                                  ..
    decimal
             10   14
    datetime (2013-05-18T09:08:29)
    0000   0x5d 0x48 0x29 0x12 0x8d                   ]H)..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 42 BolusWizard 2013-05-18T09:08:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 270,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0e                                  [.
    decimal
             91   14
    datetime (2013-05-18T09:08:31)
    0000   0x5f 0x48 0x09 0x12 0x0d                   _H...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x07 0x00 0x19 0x7d                   ....}
    decimal
              0   81   13   45  106   32    0    0
              0    7    0   25  125
    HOUR BITS: [0, 1, 0]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 1.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x4c 0x90 0x04                   \.L..
    decimal
             92    5   76  144    4
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-05-18T09:08:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-05-18T09:08:31)
    0000   0x5f 0x48 0x49 0x12 0x0d                   _HI..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 45 CalBGForPH 2013-05-18T09:58:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-05-18T09:58:57)
    0000   0x79 0x7a 0x29 0x12 0x0d                   yz)..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 46 BolusWizard 2013-05-18T10:00:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 26,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2013-05-18T10:00:09)
    0000   0x49 0x40 0x0a 0x12 0x0d                   I@...
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x17 0x14 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x14 0x7d                   ....}
    decimal
             26   80   13   45  106   23   20    0
              0   24    0   20  125
    HOUR BITS: [0, 1, 0]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 2.5, 'curve': 4},
 {'age': 196, 'amount': 1.9, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0x38 0x04 0x4c 0xc4 0x04    \.d8.L..
    decimal
             92    8  100   56    4   76  196    4
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-05-18T10:00:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-05-18T10:00:09)
    0000   0x49 0x40 0x4a 0x12 0x0d                   I@J..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 49 CalBGForPH 2013-05-18T11:25:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2013-05-18T11:25:24)
    0000   0x58 0x59 0x2b 0x12 0x0d                   XY+..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 50 CalBGForPH 2013-05-18T13:15:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-05-18T13:15:21)
    0000   0x55 0x4f 0x2d 0x12 0x0d                   UO-..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 51 CalBGForPH 2013-05-18T13:30:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-05-18T13:30:55)
    0000   0x77 0x5e 0x2d 0x12 0x0d                   w^-..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 52 BolusWizard 2013-05-18T13:31:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 82,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 33,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 2.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x52                                  [R
    decimal
             91   82
    datetime (2013-05-18T13:31:46)
    0000   0x6e 0x5f 0x0d 0x12 0x0d                   n_...
    body (13)
    hex
    0000   0x21 0x50 0x0d 0x2d 0x6a 0xfa 0x19 0xf0    !P.-j...
    0008   0x00 0x02 0x00 0x13 0x7d                   ....}
    decimal
             33   80   13   45  106  250   25  240
              0    2    0   19  125
    HOUR BITS: [0, 1, 0]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 2.0, 'curve': 4},
 {'age': 11, 'amount': 2.5, 'curve': 20},
 {'age': 151, 'amount': 1.9, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0xd9 0x04 0x64 0x0b 0x14    \.P..d..
    0008   0x4c 0x97 0x14                             L..
    decimal
             92   11   80  217    4  100   11   20
             76  151   20
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-05-18T13:31:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-05-18T13:31:47)
    0000   0x6f 0x5f 0x4d 0x12 0x0d                   o_M..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 55 CalBGForPH 2013-05-18T14:51:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-05-18T14:51:16)
    0000   0x50 0x73 0x2e 0x12 0x0d                   Ps...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 56 CalBGForPH 2013-05-18T16:04:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 152}
```
    op hex (2)
    0000   0x0a 0x98                                  ..
    decimal
             10  152
    datetime (2013-05-18T16:04:23)
    0000   0x57 0x44 0x30 0x12 0x0d                   WD0..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 BolusWizard 2013-05-18T16:04:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 152,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x98                                  [.
    decimal
             91  152
    datetime (2013-05-18T16:04:26)
    0000   0x5a 0x44 0x10 0x12 0x0d                   ZD...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    5    0    1  125
    HOUR BITS: [0, 1, 0]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 160, 'amount': 1.9, 'curve': 4},
 {'age': 114, 'amount': 2.0, 'curve': 20},
 {'age': 164, 'amount': 2.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0xa0 0x04 0x50 0x72 0x14    \.L..Pr.
    0008   0x64 0xa4 0x14                             d..
    decimal
             92   11   76  160    4   80  114   20
            100  164   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-05-18T16:04:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-05-18T16:04:26)
    0000   0x5a 0x44 0x50 0x12 0x0d                   ZDP..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 60 CalBGForPH 2013-05-18T19:54:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 220}
```
    op hex (2)
    0000   0x0a 0xdc                                  ..
    decimal
             10  220
    datetime (2013-05-18T19:54:24)
    0000   0x58 0x76 0x33 0x12 0x0d                   Xv3..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 61 BolusWizard 2013-05-18T19:54:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 220,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdc                                  [.
    decimal
             91  220
    datetime (2013-05-18T19:54:26)
    0000   0x5a 0x76 0x13 0x12 0x0d                   Zv...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    1    0   20  125
    HOUR BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 230, 'amount': 0.2, 'curve': 4},
 {'age': 134, 'amount': 1.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x08 0xe6 0x04 0x4c 0x86 0x14    \....L..
    decimal
             92    8    8  230    4   76  134   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2013-05-18T19:54:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-05-18T19:54:26)
    0000   0x5a 0x76 0x53 0x12 0x0d                   ZvS..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 64 CalBGForPH 2013-05-18T23:27:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-05-18T23:27:10)
    0000   0x4a 0x5b 0x37 0x12 0x0d                   J[7..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 65 BolusWizard 2013-05-18T23:27:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 90,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 3.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5a                                  [Z
    decimal
             91   90
    datetime (2013-05-18T23:27:28)
    0000   0x5c 0x5b 0x17 0x12 0x0d                   \[...
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0xfc 0x23 0xf0    .P.-j.#.
    0008   0x00 0x02 0x00 0x1f 0x7d                   ....}
    decimal
             46   80   13   45  106  252   35  240
              0    2    0   31  125
    HOUR BITS: [0, 1, 0]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 213, 'amount': 2.0, 'curve': 4},
 {'age': 187, 'amount': 0.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0xd5 0x04 0x08 0xbb 0x14    \.P.....
    decimal
             92    8   80  213    4    8  187   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-05-18T23:27:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-05-18T23:27:28)
    0000   0x5c 0x5b 0x57 0x12 0x0d                   \[W..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 68 MResultTotals 2013-05-19T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x96                   .....
    decimal
              7    0    0    5  150
    datetime (2013-05-19T00:00:00)
    0000   0x52 0x8d                                  R.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 Model522ResultTotals 2013-05-19T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-19T00:00:00)
    0000   0x52 0x8d                                  R.
    body (41)
    hex
    0000   0x05 0x10 0x99 0x52 0x0e 0x0a 0x00 0x00    ...R....
    0008   0x05 0x96 0x03 0x76 0x3e 0x02 0x20 0x26    ...v>. &
    0010   0x00 0x69 0x02 0x20 0x26 0x01 0x18 0x33    .i. &..3
    0018   0x01 0x08 0x31 0x00 0x00 0x00 0x07 0x03    ..1.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  153   82   14   10    0    0
              5  150    3  118   62    2   32   38
              0  105    2   32   38    1   24   51
              1    8   49    0    0    0    7    3
              4    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 70 CalBGForPH 2013-05-19T01:36:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2013-05-19T01:36:51)
    0000   0x73 0x64 0x21 0x13 0x0d                   sd!..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 71 PumpSuspend 2013-05-19T09:17:32 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-19T09:17:32)
    0000   0x60 0x51 0x09 0x13 0x0d                   `Q...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 72 PumpResume 2013-05-19T09:34:12 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-19T09:34:12)
    0000   0x4c 0x62 0x09 0x13 0x0d                   Lb...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 73 CalBGForPH 2013-05-19T09:42:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 274}
```
    op hex (2)
    0000   0x0a 0x12                                  ..
    decimal
             10   18
    datetime (2013-05-19T09:42:11)
    0000   0x4b 0x6a 0x29 0x13 0x8d                   Kj)..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 74 BolusWizard 2013-05-19T09:42:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 274,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x12                                  [.
    decimal
             91   18
    datetime (2013-05-19T09:42:13)
    0000   0x4d 0x6a 0x09 0x13 0x0d                   Mj...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125
    HOUR BITS: [0, 1, 1]
#### RECORD 75 Bolus 2013-05-19T09:42:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-05-19T09:42:13)
    0000   0x4d 0x6a 0x49 0x13 0x0d                   MjI..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 76 CalBGForPH 2013-05-19T12:01:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 192}
```
    op hex (2)
    0000   0x0a 0xc0                                  ..
    decimal
             10  192
    datetime (2013-05-19T12:01:42)
    0000   0x6a 0x41 0x2c 0x13 0x0d                   jA,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 77 BolusWizard 2013-05-19T12:01:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 192,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc0                                  [.
    decimal
             91  192
    datetime (2013-05-19T12:01:54)
    0000   0x76 0x41 0x0c 0x13 0x0d                   vA...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0   11    0    3  125
    HOUR BITS: [0, 1, 0]
#### RECORD 78 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 0.65, 'curve': 4},
 {'age': 147, 'amount': 2.65, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x1a 0x89 0x04 0x6a 0x93 0x04    \....j..
    decimal
             92    8   26  137    4  106  147    4
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2013-05-19T12:01:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-05-19T12:01:54)
    0000   0x76 0x41 0x4c 0x13 0x0d                   vAL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 80 CalBGForPH 2013-05-19T13:30:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-05-19T13:30:42)
    0000   0x6a 0x5e 0x2d 0x13 0x0d                   j^-..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 81 BolusWizard 2013-05-19T13:31:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 106,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-05-19T13:31:00)
    0000   0x40 0x5f 0x0d 0x13 0x0d                   @_...
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x00 0x1e 0x00    (P.-j...
    0008   0x00 0x04 0x00 0x1e 0x7d                   ....}
    decimal
             40   80   13   45  106    0   30    0
              0    4    0   30  125
    HOUR BITS: [0, 1, 0]
#### RECORD 82 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 97, 'amount': 0.3, 'curve': 4},
 {'age': 227, 'amount': 0.65, 'curve': 4},
 {'age': 237, 'amount': 2.65, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x61 0x04 0x1a 0xe3 0x04    \..a....
    0008   0x6a 0xed 0x04                             j..
    decimal
             92   11   12   97    4   26  227    4
            106  237    4
    datetime (unknown)

    body (0)

#### RECORD 83 Bolus 2013-05-19T13:31:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-05-19T13:31:00)
    0000   0x40 0x5f 0x4d 0x13 0x0d                   @_M..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 84 CalBGForPH 2013-05-19T22:05:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2013-05-19T22:05:49)
    0000   0x71 0x45 0x36 0x13 0x0d                   qE6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 85 BolusWizard 2013-05-19T22:06:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2013-05-19T22:06:00)
    0000   0x40 0x46 0x16 0x13 0x0d                   @F...
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0x01 0x2c 0x00    :P.-j.,.
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             58   80   13   45  106    1   44    0
              0    0    0   45  125
    HOUR BITS: [0, 1, 0]
#### RECORD 86 Bolus 2013-05-19T22:06:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-05-19T22:06:00)
    0000   0x40 0x46 0x56 0x13 0x0d                   @FV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 87 MResultTotals 2013-05-20T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x34                   ....4
    decimal
              7    0    0    5   52
    datetime (2013-05-20T00:00:00)
    0000   0x53 0x8d                                  S.
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-18.data: 88 records`
