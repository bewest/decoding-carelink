## START logs/ReadHistoryData-page-19.data
#### RECORD 0 hack1 2013-05-11T22:49:42 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x4a 0x8d 0x05 0x00 0x71 0x40 0xba    mJ...q@.
    0008   0x05 0x00 0x00 0x04 0x42 0x03 0x72 0x51    ....B.rQ
    0010   0x00 0xd0 0x13 0x00 0x33 0x00 0xd0 0x13    ....3...
    0018   0x00 0x9c 0x4b 0x00 0x34 0x19 0x00 0x00    ..K.4...
    0020   0x00 0x02 0x01 0x01 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x79              .....y
    decimal
            109   74  141    5    0  113   64  186
              5    0    0    4   66    3  114   81
              0  208   19    0   51    0  208   19
              0  156   75    0   52   25    0    0
              0    2    1    1    0    0   12    0
            232    0    0    0   10  121
    datetime (2013-05-11T22:49:42)
    0000   0x6a 0x71 0x36 0x0b 0x0d                   jq6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-05-11T22:49:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-05-11T22:49:55)
    0000   0x77 0x71 0x16 0x0b 0x0d                   wq...
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0x00 0x35 0x00    FP.-j.5.
    0008   0x00 0x00 0x00 0x35 0x7d                   ...5}
    decimal
             70   80   13   45  106    0   53    0
              0    0    0   53  125
    HOUR BITS: [0, 1, 1]
#### RECORD 2 Bolus 2013-05-11T22:49:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-05-11T22:49:55)
    0000   0x77 0x71 0x56 0x0b 0x0d                   wqV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-05-11T23:39:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-05-11T23:39:07)
    0000   0x47 0x67 0x37 0x0b 0x0d                   Gg7..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 ResultTotals 2013-06-11T13:13:11 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x58                   ....X
    decimal
              7    0    0    4   88
    datetime (2013-06-11T13:13:11)
    0000   0x4b 0x8d 0x6d 0x4b 0x8d                   K.mK.
    body (41)
    hex
    0000   0x05 0x00 0x6f 0x65 0x79 0x02 0x00 0x00    ..oey...
    0008   0x04 0x58 0x03 0x84 0x51 0x00 0xd4 0x13    .X..Q...
    0010   0x00 0x46 0x00 0xd4 0x13 0x00 0xd4 0x64    .F.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  111  101  121    2    0    0
              4   88    3  132   81    0  212   19
              0   70    0  212   19    0  212  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 CalBGForPH 2013-05-12T09:05:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 315}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2013-05-12T09:05:14)
    0000   0x4e 0x45 0x29 0x0c 0x8d                   NE)..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 6 BolusWizard 2013-05-12T09:05:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 42,
 '_byte[7]': 0,
 'bg': 315,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3b                                  [;
    decimal
             91   59
    datetime (2013-05-12T09:05:17)
    0000   0x51 0x45 0x09 0x0c 0x0d                   QE...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2a 0x00 0x00    .Q.-j*..
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
              0   81   13   45  106   42    0    0
              0    0    0   42  125
    HOUR BITS: [0, 1, 0]
#### RECORD 7 Bolus 2013-05-12T09:05:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-05-12T09:05:17)
    0000   0x51 0x45 0x49 0x0c 0x0d                   QEI..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 8 PumpSuspend 2013-05-12T09:08:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-12T09:08:21)
    0000   0x55 0x48 0x09 0x0c 0x0d                   UH...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 9 PumpResume 2013-05-12T09:33:24 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-12T09:33:24)
    0000   0x58 0x61 0x09 0x0c 0x0d                   Xa...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 CalBGForPH 2013-05-12T12:16:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-05-12T12:16:07)
    0000   0x47 0x50 0x2c 0x0c 0x0d                   GP,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 11 CalBGForPH 2013-05-12T12:17:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-05-12T12:17:17)
    0000   0x51 0x51 0x2c 0x0c 0x0d                   QQ,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 12 BolusWizard 2013-05-12T12:18:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 91,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 3.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2013-05-12T12:18:34)
    0000   0x62 0x52 0x0c 0x0c 0x0d                   bR...
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0xfc 0x25 0xf0    1P.-j.%.
    0008   0x00 0x06 0x00 0x21 0x7d                   ...!}
    decimal
             49   80   13   45  106  252   37  240
              0    6    0   33  125
    HOUR BITS: [0, 1, 0]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 194, 'amount': 4.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0xc2 0x04                   \....
    decimal
             92    5  168  194    4
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-05-12T12:18:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-05-12T12:18:34)
    0000   0x62 0x52 0x4c 0x0c 0x0d                   bRL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 15 BolusWizard 2013-05-12T13:07:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
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
    datetime (2013-05-12T13:07:31)
    0000   0x5f 0x47 0x0d 0x0c 0x0d                   _G...
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 0]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 3.3, 'curve': 4},
 {'age': 243, 'amount': 4.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0x35 0x04 0xa8 0xf3 0x04    \..5....
    decimal
             92    8  132   53    4  168  243    4
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-05-12T13:07:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-05-12T13:07:31)
    0000   0x5f 0x47 0x4d 0x0c 0x0d                   _GM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 18 LowReservoir 2013-05-12T19:28:25 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-12T19:28:25)
    0000   0x59 0x5c 0x13 0x0c 0x0d                   Y\...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 19 CalBGForPH 2013-05-12T19:55:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 173}
```
    op hex (2)
    0000   0x0a 0xad                                  ..
    decimal
             10  173
    datetime (2013-05-12T19:55:50)
    0000   0x72 0x77 0x33 0x0c 0x0d                   rw3..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2013-05-12T19:55:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 173,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2013-05-12T19:55:52)
    0000   0x74 0x77 0x13 0x0c 0x0d                   tw...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.0, 'curve': 20},
 {'age': 205, 'amount': 3.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x9b 0x14 0x84 0xcd 0x14    \.(.....
    decimal
             92    8   40  155   20  132  205   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-05-12T19:55:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-05-12T19:55:52)
    0000   0x74 0x77 0x53 0x0c 0x0d                   twS..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 ResultTotals 2013-06-12T13:13:12 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xee                   .....
    decimal
              7    0    0    4  238
    datetime (2013-06-12T13:13:12)
    0000   0x4c 0x8d 0x6d 0x4c 0x8d                   L.mL.
    body (41)
    hex
    0000   0x05 0x10 0xa8 0x5b 0x3b 0x04 0x00 0x00    ...[;...
    0008   0x04 0xee 0x03 0x72 0x46 0x01 0x7c 0x1e    ...rF.|.
    0010   0x00 0x3e 0x01 0x7c 0x1e 0x00 0xac 0x2d    .>.|...-
    0018   0x00 0xd0 0x37 0x00 0x00 0x00 0x04 0x02    ..7.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  168   91   59    4    0    0
              4  238    3  114   70    1  124   30
              0   62    1  124   30    0  172   45
              0  208   55    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 24 CalBGForPH 2013-05-13T00:02:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-05-13T00:02:10)
    0000   0x4a 0x42 0x20 0x0d 0x0d                   JB ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 25 BolusWizard 2013-05-13T00:04:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 103,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-05-13T00:04:57)
    0000   0x79 0x44 0x00 0x0d 0x0d                   yD...
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xff 0x26 0xf0    2P.-j.&.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             50   80   13   45  106  255   38  240
              0    0    0   37  125
    HOUR BITS: [0, 1, 0]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 250, 'amount': 1.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0xfa 0x04                   \.(..
    decimal
             92    5   40  250    4
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-05-13T00:04:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-05-13T00:04:57)
    0000   0x79 0x44 0x80 0x0d 0x0d                   yD...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 28 Bolus 2013-05-13T00:06:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x02                        ....
    decimal
              1   20   20    2
    datetime (2013-05-13T00:06:03)
    0000   0x43 0x46 0xa0 0x0d 0x0d                   CF...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 29 LowReservoir 2013-05-13T01:15:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-05-13T01:15:00)
    0000   0x40 0x4f 0x01 0x0d 0x0d                   @O...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 30 CalBGForPH 2013-05-13T03:56:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2013-05-13T03:56:09)
    0000   0x49 0x78 0x23 0x0d 0x0d                   Ix#..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 31 PumpSuspend 2013-05-13T12:55:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-13T12:55:21)
    0000   0x55 0x77 0x0c 0x0d 0x0d                   Uw...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 32 PumpResume 2013-05-13T13:40:53 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-13T13:40:53)
    0000   0x75 0x68 0x0d 0x0d 0x0d                   uh...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 33 Rewind 2013-05-13T14:05:48 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-05-13T14:05:48)
    0000   0x70 0x45 0x0e 0x0d 0x0d                   pE...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 34 Prime 2013-05-13T14:06:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2b                   ....+
    decimal
              3    0    0    0   43
    datetime (2013-05-13T14:06:19)
    0000   0x53 0x46 0x2e 0x0d 0x0d                   SF...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 35 Prime 2013-05-13T14:06:43 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-05-13T14:06:43)
    0000   0x6b 0x46 0x0e 0x0d 0x0d                   kF...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 CalBGForPH 2013-05-13T14:07:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-05-13T14:07:52)
    0000   0x74 0x47 0x2e 0x0d 0x0d                   tG...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 CalBGForPH 2013-05-13T14:07:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-05-13T14:07:55)
    0000   0x77 0x47 0x2e 0x0d 0x0d                   wG...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 CalBGForPH 2013-05-13T14:07:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-05-13T14:07:58)
    0000   0x7a 0x47 0x2e 0x0d 0x0d                   zG...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 BolusWizard 2013-05-13T14:08:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 3.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2013-05-13T14:08:25)
    0000   0x59 0x48 0x0e 0x0d 0x0d                   YH...
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0x08 0x25 0x00    1P.-j.%.
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             49   80   13   45  106    8   37    0
              0    0    0   45  125
    HOUR BITS: [0, 1, 0]
#### RECORD 40 Bolus 2013-05-13T14:08:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-05-13T14:08:25)
    0000   0x59 0x48 0x4e 0x0d 0x0d                   YHN..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 41 CalBGForPH 2013-05-13T17:36:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-05-13T17:36:04)
    0000   0x44 0x64 0x31 0x0d 0x0d                   Dd1..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 42 CalBGForPH 2013-05-13T19:08:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-05-13T19:08:10)
    0000   0x4a 0x48 0x33 0x0d 0x0d                   JH3..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 43 BolusWizard 2013-05-13T19:08:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 21,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 1.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-05-13T19:08:22)
    0000   0x56 0x48 0x13 0x0d 0x0d                   VH...
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0xff 0x10 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             21   80   13   45  106  255   16  240
              0    0    0   15  125
    HOUR BITS: [0, 1, 0]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 4.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0x30 0x14                   \..0.
    decimal
             92    5  180   48   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-05-13T19:08:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-05-13T19:08:22)
    0000   0x56 0x48 0x53 0x0d 0x0d                   VHS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 46 CalBGForPH 2013-05-13T20:03:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2013-05-13T20:03:39)
    0000   0x67 0x43 0x34 0x0d 0x0d                   gC4..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 47 BolusWizard 2013-05-13T20:04:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 170,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 30,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2013-05-13T20:04:16)
    0000   0x50 0x44 0x14 0x0d 0x0d                   PD...
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x0a 0x17 0x00    .P.-j...
    0008   0x00 0x0d 0x00 0x17 0x7d                   ....}
    decimal
             30   80   13   45  106   10   23    0
              0   13    0   23  125
    HOUR BITS: [0, 1, 0]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 1.5, 'curve': 4},
 {'age': 104, 'amount': 4.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x3c 0x04 0xb4 0x68 0x14    \.<<..h.
    decimal
             92    8   60   60    4  180  104   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-05-13T20:04:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-05-13T20:04:16)
    0000   0x50 0x44 0x54 0x0d 0x0d                   PDT..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 50 CalBGForPH 2013-05-13T20:31:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2013-05-13T20:31:11)
    0000   0x4b 0x5f 0x34 0x0d 0x0d                   K_4..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 51 ResultTotals 2013-06-13T13:13:13 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x42                   ....B
    decimal
              7    0    0    5   66
    datetime (2013-06-13T13:13:13)
    0000   0x4d 0x8d 0x6d 0x4d 0x8d                   M.mM.
    body (41)
    hex
    0000   0x05 0x00 0x8e 0x5d 0xb5 0x09 0x00 0x00    ...]....
    0008   0x05 0x42 0x03 0x62 0x40 0x01 0xe0 0x24    .B.b@..$
    0010   0x00 0x96 0x01 0xe0 0x24 0x01 0xc0 0x5d    ....$..]
    0018   0x00 0x20 0x07 0x00 0x00 0x00 0x04 0x03    . ......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  142   93  181    9    0    0
              5   66    3   98   64    1  224   36
              0  150    1  224   36    1  192   93
              0   32    7    0    0    0    4    3
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 52 PumpSuspend 2013-05-14T14:02:34 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-14T14:02:34)
    0000   0x62 0x42 0x0e 0x0e 0x0d                   bB...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 53 PumpResume 2013-05-14T14:29:54 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-14T14:29:54)
    0000   0x76 0x5d 0x0e 0x0e 0x0d                   v]...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 54 CalBGForPH 2013-05-14T15:52:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 74}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2013-05-14T15:52:15)
    0000   0x4f 0x74 0x2f 0x0e 0x0d                   Ot/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 55 BolusWizard 2013-05-14T15:52:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 74,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4a                                  [J
    decimal
             91   74
    datetime (2013-05-14T15:52:38)
    0000   0x66 0x74 0x0f 0x0e 0x0d                   ft...
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0xf9 0x27 0xf0    3P.-j.'.
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             51   80   13   45  106  249   39  240
              0    0    0   32  125
    HOUR BITS: [0, 1, 1]
#### RECORD 56 Bolus 2013-05-14T15:52:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-05-14T15:52:38)
    0000   0x66 0x74 0x4f 0x0e 0x0d                   ftO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 57 CalBGForPH 2013-05-14T18:44:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-05-14T18:44:45)
    0000   0x6d 0x6c 0x32 0x0e 0x0d                   ml2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 58 BolusWizard 2013-05-14T18:44:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 4,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-05-14T18:44:52)
    0000   0x74 0x6c 0x12 0x0e 0x0d                   tl...
    body (13)
    hex
    0000   0x04 0x50 0x0d 0x2d 0x6a 0x0a 0x03 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x07 0x7d                   ....}
    decimal
              4   80   13   45  106   10    3    0
              0    6    0    7  125
    HOUR BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 170, 'amount': 1.2, 'curve': 4},
 {'age': 180, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0xaa 0x04 0x50 0xb4 0x04    \.0..P..
    decimal
             92    8   48  170    4   80  180    4
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-05-14T18:44:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-05-14T18:44:52)
    0000   0x74 0x6c 0x52 0x0e 0x0d                   tlR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 61 CalBGForPH 2013-05-14T21:39:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 226}
```
    op hex (2)
    0000   0x0a 0xe2                                  ..
    decimal
             10  226
    datetime (2013-05-14T21:39:39)
    0000   0x67 0x67 0x35 0x0e 0x0d                   gg5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 62 CalBGForPH 2013-05-14T21:39:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 228}
```
    op hex (2)
    0000   0x0a 0xe4                                  ..
    decimal
             10  228
    datetime (2013-05-14T21:39:43)
    0000   0x6b 0x67 0x35 0x0e 0x0d                   kg5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 63 BolusWizard 2013-05-14T21:39:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 228,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 7.2,
 'carb_input': 68,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 5.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe4                                  [.
    decimal
             91  228
    datetime (2013-05-14T21:39:54)
    0000   0x76 0x67 0x15 0x0e 0x0d                   vg...
    body (13)
    hex
    0000   0x44 0x50 0x0d 0x2d 0x6a 0x16 0x34 0x00    DP.-j.4.
    0008   0x00 0x02 0x00 0x48 0x7d                   ...H}
    decimal
             68   80   13   45  106   22   52    0
              0    2    0   72  125
    HOUR BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 175, 'amount': 0.7, 'curve': 4},
 {'age': 89, 'amount': 1.2, 'curve': 20},
 {'age': 99, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x1c 0xaf 0x04 0x30 0x59 0x14    \....0Y.
    0008   0x50 0x63 0x14                             Pc.
    decimal
             92   11   28  175    4   48   89   20
             80   99   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-05-14T21:39:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.2, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x48 0x48 0x00                        .HH.
    decimal
              1   72   72    0
    datetime (2013-05-14T21:39:54)
    0000   0x76 0x67 0x55 0x0e 0x0d                   vgU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 66 CalBGForPH 2013-05-14T22:16:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 201}
```
    op hex (2)
    0000   0x0a 0xc9                                  ..
    decimal
             10  201
    datetime (2013-05-14T22:16:32)
    0000   0x60 0x50 0x36 0x0e 0x0d                   `P6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 67 ResultTotals 2013-06-14T13:13:14 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x2e                   .....
    decimal
              7    0    0    5   46
    datetime (2013-06-14T13:13:14)
    0000   0x4e 0x8d 0x6d 0x4e 0x8d                   N.mN.
    body (41)
    hex
    0000   0x05 0x00 0xb4 0x4a 0xe4 0x05 0x00 0x00    ...J....
    0008   0x05 0x2e 0x03 0x72 0x43 0x01 0xbc 0x21    ...rC..!
    0010   0x00 0x7b 0x01 0xbc 0x21 0x01 0x5c 0x4e    .{..!.\N
    0018   0x00 0x60 0x16 0x00 0x00 0x00 0x03 0x01    .`......
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  180   74  228    5    0    0
              5   46    3  114   67    1  188   33
              0  123    1  188   33    1   92   78
              0   96   22    0    0    0    3    1
              0    2    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 68 PumpSuspend 2013-05-15T13:33:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-15T13:33:20)
    0000   0x54 0x61 0x0d 0x0f 0x0d                   Ta...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 69 PumpResume 2013-05-15T13:52:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-15T13:52:35)
    0000   0x63 0x74 0x0d 0x0f 0x0d                   ct...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 70 CalBGForPH 2013-05-15T14:52:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-05-15T14:52:52)
    0000   0x74 0x74 0x2e 0x0f 0x0d                   tt...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 71 CalBGForPH 2013-05-15T14:53:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-05-15T14:53:45)
    0000   0x6d 0x75 0x2e 0x0f 0x0d                   mu...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 72 BolusWizard 2013-05-15T14:54:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-05-15T14:54:25)
    0000   0x59 0x76 0x0e 0x0f 0x0d                   Yv...
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0xfc 0x21 0xf0    +P.-j.!.
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
             43   80   13   45  106  252   33  240
              0    0    0   29  125
    HOUR BITS: [0, 1, 1]
#### RECORD 73 Bolus 2013-05-15T14:54:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-05-15T14:54:25)
    0000   0x59 0x76 0x4e 0x0f 0x0d                   YvN..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 74 ResultTotals 2013-06-15T13:13:15 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xea                   .....
    decimal
              7    0    0    3  234
    datetime (2013-06-15T13:13:15)
    0000   0x4f 0x8d 0x6d 0x4f 0x8d                   O.mO.
    body (41)
    hex
    0000   0x05 0x00 0x58 0x58 0x58 0x02 0x00 0x00    ..XXX...
    0008   0x03 0xea 0x03 0x76 0x58 0x00 0x74 0x0c    ...vX.t.
    0010   0x00 0x2b 0x00 0x74 0x0c 0x00 0x74 0x64    .+.t..td
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   88   88   88    2    0    0
              3  234    3  118   88    0  116   12
              0   43    0  116   12    0  116  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 75 CalBGForPH 2013-05-16T00:14:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2013-05-16T00:14:55)
    0000   0x77 0x4e 0x20 0x10 0x0d                   wN ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 76 BolusWizard 2013-05-16T00:15:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 131,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 26,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2013-05-16T00:15:40)
    0000   0x68 0x4f 0x00 0x10 0x0d                   hO...
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x01 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             26   80   13   45  106    1   20    0
              0    0    0   21  125
    HOUR BITS: [0, 1, 0]
#### RECORD 77 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xe7                                  ..
    decimal
              0  231
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-19.data: 78 records`
