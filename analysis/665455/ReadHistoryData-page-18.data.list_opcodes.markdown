## START logs/ReadHistoryData-page-18.data
#### STOPPING DOUBLE NULLS @ 436, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x13 0x7d 0x01 0x13 0x13 0x00 0x40 0x73    .}....@s
    0008   0x46 0x12 0x0d 0x1e 0x00 0x5e 0x4b 0x08    F....^K.
    0010   0x12 0x0d 0x1f 0x00 0x54 0x62 0x08 0x12    ....Tb..
    0018   0x0d 0x0a 0x0e 0x5d 0x48 0x29 0x12 0x8d    ...]H)..
##### DEBUG DECIMAL
             19  125    1   19   19    0   64  115
             70   18   13   30    0   94   75    8
             18   13   31    0   84   98    8   18
             13   10   14   93   72   41   18  141
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
#### RECORD 20 ResultTotals 2013-06-16T13:13:16 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0a                   .....
    decimal
              7    0    0    5   10
    datetime (2013-06-16T13:13:16)
    0000   0x50 0x8d 0x6d 0x50 0x8d                   P.mP.
    body (51)
    hex
    0000   0x05 0x00 0x9b 0x43 0xfd 0x06 0x00 0x00    ...C....
    0008   0x05 0x0a 0x03 0x6a 0x44 0x01 0xa0 0x20    ...jD.. 
    0010   0x00 0x64 0x01 0xa0 0x20 0x01 0x2c 0x48    .d.. .,H
    0018   0x00 0x74 0x1c 0x00 0x00 0x00 0x05 0x03    .t......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x34 0x64 0x4a 0x66 0x09 0x11 0x0d    .4dJf...
    0030   0x1e 0x00 0x46                             ..F
    decimal
              5    0  155   67  253    6    0    0
              5   10    3  106   68    1  160   32
              0  100    1  160   32    1   44   72
              0  116   28    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0   52  100   74  102    9   17   13
             30    0   70
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 ChangeTimeDisplay (2003, 0, 0, 31, 13, 17) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x0e                                  d.
    decimal
            100   14
    datetime ((2003, 0, 0, 31, 13, 17))
    0000   0x11 0x0d 0x1f 0x00 0x63                   ....c
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 22 Ian50 (2003, 0, 0, 1, 13, 17) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0f                                  P.
    decimal
             80   15
    datetime ((2003, 0, 0, 1, 13, 17))
    0000   0x11 0x0d 0x21 0x00 0x73                   ..!.s
    body (34)
    hex
    0000   0x79 0x14 0x11 0x0d 0x03 0x00 0x00 0x00    y.......
    0008   0x20 0x7a 0x7b 0x34 0x11 0x0d 0x03 0x00     z{4....
    0010   0x05 0x00 0x05 0x51 0x40 0x15 0x11 0x0d    ...Q@...
    0018   0x0a 0x57 0x4a 0x6b 0x35 0x11 0x0d 0x0a    .WJk5...
    0020   0x57 0x44                                  WD
    decimal
            121   20   17   13    3    0    0    0
             32  122  123   52   17   13    3    0
              5    0    5   81   64   21   17   13
             10   87   74  107   53   17   13   10
             87   68
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 23 Base (2001, 0, 23, 27, 13, 17) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x35                                  l5
    decimal
            108   53
    datetime ((2001, 0, 23, 27, 13, 17))
    0000   0x11 0x0d 0x5b 0x57 0x51                   ..[WQ
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 24 Base (2013, 0, 16, 3, 13, 17) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x15                                  l.
    decimal
            108   21
    datetime ((2013, 0, 16, 3, 13, 17))
    0000   0x11 0x0d 0x43 0x50 0x0d                   ..CP.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 25 Base (2000, 12, 0, 16, 51, 60) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 51, 60))
    0000   0xfc 0x33 0xf0 0x00 0x00                   .3...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 Base (2000, 4, 15, 15, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2f                                  ./
    decimal
              0   47
    datetime ((2000, 4, 15, 15, 1, 61))
    0000   0x7d 0x01 0x2f 0x2f 0x00                   }.//.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 27 Base (2006, 4, 10, 13, 17, 21) head[2], body[0] op[0x51]

    op hex (2)
    0000   0x51 0x6c                                  Ql
    decimal
             81  108
    datetime ((2006, 4, 10, 13, 17, 21))
    0000   0x55 0x11 0x0d 0x0a 0x36                   U...6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[85], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 1.35, 'curve': 13},
 {'age': 75, 'amount': 0.25, 'curve': 65},
 {'age': 54, 'amount': 3.025, 'curve': 17},
 {'age': 7, 'amount': 0.325, 'curve': 0},
 {'age': 4, 'amount': 0.0, 'curve': 36},
 {'age': 141, 'amount': 2.025, 'curve': 109},
 {'age': 141, 'amount': 2.025, 'curve': 5},
 {'age': 76, 'amount': 0.0, 'curve': 54},
 {'age': 4, 'amount': 2.175, 'curve': 0},
 {'age': 4, 'amount': 0.0, 'curve': 36},
 {'age': 104, 'amount': 0.075, 'curve': 82},
 {'age': 188, 'amount': 0.0, 'curve': 18},
 {'age': 67, 'amount': 0.0, 'curve': 0},
 {'age': 18, 'amount': 4.7, 'curve': 0},
 {'age': 100, 'amount': 4.7, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 1},
 {'age': 0, 'amount': 0.025, 'curve': 0},
 {'age': 12, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 5.8, 'curve': 0},
 {'age': 10, 'amount': 0.0, 'curve': 211},
 {'age': 114, 'amount': 3.05, 'curve': 38},
 {'age': 13, 'amount': 0.45, 'curve': 91},
 {'age': 64, 'amount': 5.275, 'curve': 115},
 {'age': 18, 'amount': 0.15, 'curve': 13},
 {'age': 80, 'amount': 0.0, 'curve': 13},
 {'age': 106, 'amount': 1.125, 'curve': 19}]
```
    op hex (85)
    0000   0x5c 0x55 0x36 0x11 0x0d 0x0a 0x4b 0x41    \U6...KA
    0008   0x79 0x36 0x11 0x0d 0x07 0x00 0x00 0x04    y6......
    0010   0x24 0x51 0x8d 0x6d 0x51 0x8d 0x05 0x00    $Q.mQ...
    0018   0x4c 0x36 0x57 0x04 0x00 0x00 0x04 0x24    L6W....$
    0020   0x03 0x68 0x52 0x00 0xbc 0x12 0x00 0x43    .hR....C
    0028   0x00 0xbc 0x12 0x00 0xbc 0x64 0x00 0x00    .....d..
    0030   0x00 0x00 0x00 0x00 0x01 0x01 0x00 0x00    ........
    0038   0x00 0x0c 0x00 0xe8 0x00 0x00 0x00 0x0a    ........
    0040   0xd3 0x7a 0x72 0x26 0x12 0x0d 0x5b 0xd3    .zr&..[.
    0048   0x40 0x73 0x06 0x12 0x0d 0x00 0x50 0x0d    @s....P.
    0050   0x2d 0x6a 0x13 0x00 0x00                   -j...
    decimal
             92   85   54   17   13   10   75   65
            121   54   17   13    7    0    0    4
             36   81  141  109   81  141    5    0
             76   54   87    4    0    0    4   36
              3  104   82    0  188   18    0   67
              0  188   18    0  188  100    0    0
              0    0    0    0    1    1    0    0
              0   12    0  232    0    0    0   10
            211  122  114   38   18   13   91  211
             64  115    6   18   13    0   80   13
             45  106   19    0    0
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-18.data: 29 records`
