## START logs/ReadHistoryData-page-17.data
#### STOPPING DOUBLE NULLS @ 990, found 32 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb7 0xd5                                  ..
##### DEBUG DECIMAL
            183  213
#### RECORD 0 Model522ResultTotals 2013-05-20T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-20T00:00:00)
    0000   0x53 0x8d                                  S.
    body (41)
    hex
    0000   0x05 0x10 0xa6 0x6a 0x12 0x05 0x00 0x00    ...j....
    0008   0x05 0x34 0x03 0x78 0x43 0x01 0xbc 0x21    .4.xC..!
    0010   0x00 0x62 0x01 0xbc 0x21 0x01 0x28 0x43    .b..!.(C
    0018   0x00 0x94 0x21 0x00 0x00 0x00 0x04 0x01    ..!.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  166  106   18    5    0    0
              5   52    3  120   67    1  188   33
              0   98    1  188   33    1   40   67
              0  148   33    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2013-05-20T03:35:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-05-20T03:35:43)
    0000   0x6b 0x63 0x23 0x14 0x0d                   kc#..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2013-05-20T03:35:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
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
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2013-05-20T03:35:45)
    0000   0x6d 0x63 0x03 0x14 0x0d                   mc...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x17 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
              0   80   13   45  106   23    0    0
              0    0    0   23  125
    HOUR BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 75, 'amount': 4.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0x4b 0x14                   \..K.
    decimal
             92    5  180   75   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-05-20T03:35:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-05-20T03:35:46)
    0000   0x6e 0x63 0x43 0x14 0x0d                   ncC..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 PumpSuspend 2013-05-20T09:53:48 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-20T09:53:48)
    0000   0x70 0x75 0x09 0x14 0x0d                   pu...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 PumpResume 2013-05-20T10:17:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-20T10:17:07)
    0000   0x47 0x51 0x0a 0x14 0x0d                   GQ...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-05-20T10:49:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 255}
```
    op hex (2)
    0000   0x0a 0xff                                  ..
    decimal
             10  255
    datetime (2013-05-20T10:49:45)
    0000   0x6d 0x71 0x2a 0x14 0x0d                   mq*..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 8 BolusWizard 2013-05-20T10:49:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 255,
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
    0000   0x5b 0xff                                  [.
    decimal
             91  255
    datetime (2013-05-20T10:49:51)
    0000   0x73 0x71 0x0a 0x14 0x0d                   sq...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    0    0   28  125
    HOUR BITS: [0, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 179, 'amount': 2.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0xb3 0x14                   \.\..
    decimal
             92    5   92  179   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-05-20T10:49:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-05-20T10:49:51)
    0000   0x73 0x71 0x4a 0x14 0x0d                   sqJ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 11 CalBGForPH 2013-05-20T12:31:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-05-20T12:31:43)
    0000   0x6b 0x5f 0x2c 0x14 0x0d                   k_,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 12 BolusWizard 2013-05-20T12:32:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 156,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 3.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2013-05-20T12:32:15)
    0000   0x4f 0x60 0x0c 0x14 0x0d                   O`...
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x06 0x22 0x00    -P.-j.".
    0008   0x00 0x10 0x00 0x22 0x7d                   ..."}
    decimal
             45   80   13   45  106    6   34    0
              0   16    0   34  125
    HOUR BITS: [0, 1, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 2.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0x6c 0x04                   \.tl.
    decimal
             92    5  116  108    4
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-05-20T12:32:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-05-20T12:32:16)
    0000   0x50 0x60 0x4c 0x14 0x0d                   P`L..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 15 CalBGForPH 2013-05-20T17:34:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2013-05-20T17:34:39)
    0000   0x67 0x62 0x31 0x14 0x0d                   gb1..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 16 CalBGForPH 2013-05-20T17:36:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2013-05-20T17:36:57)
    0000   0x79 0x64 0x31 0x14 0x0d                   yd1..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2013-05-20T17:37:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 131,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 1.9,
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
    datetime (2013-05-20T17:37:43)
    0000   0x6b 0x65 0x11 0x14 0x0d                   ke...
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x01 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             25   80   13   45  106    1   19    0
              0    0    0   20  125
    HOUR BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 0.85, 'curve': 20},
 {'age': 57, 'amount': 2.55, 'curve': 20},
 {'age': 157, 'amount': 2.9, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x22 0x2f 0x14 0x66 0x39 0x14    \."/.f9.
    0008   0x74 0x9d 0x14                             t..
    decimal
             92   11   34   47   20  102   57   20
            116  157   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-05-20T17:37:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-05-20T17:37:43)
    0000   0x6b 0x65 0x51 0x14 0x0d                   keQ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 20 CalBGForPH 2013-05-20T20:35:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-05-20T20:35:56)
    0000   0x78 0x63 0x34 0x14 0x0d                   xc4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 21 CalBGForPH 2013-05-20T20:46:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-05-20T20:46:59)
    0000   0x7b 0x6e 0x34 0x14 0x0d                   {n4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2013-05-20T20:47:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 39,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-05-20T20:47:26)
    0000   0x5a 0x6f 0x14 0x14 0x0d                   Zo...
    body (13)
    hex
    0000   0x27 0x50 0x0d 0x2d 0x6a 0xfc 0x1e 0xf0    'P.-j...
    0008   0x00 0x03 0x00 0x1a 0x7d                   ....}
    decimal
             39   80   13   45  106  252   30  240
              0    3    0   26  125
    HOUR BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0xc1 0x04                   \.P..
    decimal
             92    5   80  193    4
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-05-20T20:47:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-05-20T20:47:26)
    0000   0x5a 0x6f 0x54 0x14 0x0d                   ZoT..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 25 MResultTotals 2013-05-21T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x82                   .....
    decimal
              7    0    0    5  130
    datetime (2013-05-21T00:00:00)
    0000   0x54 0x8d                                  T.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 26 Model522ResultTotals 2013-05-21T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-21T00:00:00)
    0000   0x54 0x8d                                  T.
    body (41)
    hex
    0000   0x05 0x00 0x99 0x52 0xff 0x07 0x00 0x00    ...R....
    0008   0x05 0x82 0x03 0x72 0x3f 0x02 0x10 0x25    ...r?..%
    0010   0x00 0x6d 0x02 0x10 0x25 0x01 0x3c 0x3c    .m..%.<<
    0018   0x00 0xd4 0x28 0x00 0x00 0x00 0x05 0x02    ..(.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  153   82  255    7    0    0
              5  130    3  114   63    2   16   37
              0  109    2   16   37    1   60   60
              0  212   40    0    0    0    5    2
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 27 LowReservoir 2013-05-21T07:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-21T07:41:03)
    0000   0x43 0x69 0x07 0x15 0x0d                   Ci...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 28 PumpSuspend 2013-05-21T15:15:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-21T15:15:44)
    0000   0x6c 0x4f 0x0f 0x15 0x0d                   lO...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 29 PumpResume 2013-05-21T15:35:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-21T15:35:09)
    0000   0x49 0x63 0x0f 0x15 0x0d                   Ic...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 30 LowReservoir 2013-05-21T17:50:31 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-05-21T17:50:31)
    0000   0x5f 0x72 0x11 0x15 0x0d                   _r...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 31 CalBGForPH 2013-05-21T18:07:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 290}
```
    op hex (2)
    0000   0x0a 0x22                                  ."
    decimal
             10   34
    datetime (2013-05-21T18:07:33)
    0000   0x61 0x47 0x32 0x15 0x8d                   aG2..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 32 BolusWizard 2013-05-21T18:07:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 290,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x22                                  ["
    decimal
             91   34
    datetime (2013-05-21T18:07:36)
    0000   0x64 0x47 0x12 0x15 0x0d                   dG...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
              0   81   13   45  106   36    0    0
              0    0    0   36  125
    HOUR BITS: [0, 1, 0]
#### RECORD 33 Bolus 2013-05-21T18:07:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-05-21T18:07:36)
    0000   0x64 0x47 0x52 0x15 0x0d                   dGR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 34 Rewind 2013-05-21T21:10:49 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-05-21T21:10:49)
    0000   0x71 0x4a 0x15 0x15 0x0d                   qJ...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 35 Prime 2013-05-21T21:13:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x24                   ....$
    decimal
              3    0    0    0   36
    datetime (2013-05-21T21:13:18)
    0000   0x52 0x4d 0x35 0x15 0x0d                   RM5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 Prime 2013-05-21T21:13:38 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-05-21T21:13:38)
    0000   0x66 0x4d 0x15 0x15 0x0d                   fM...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 CalBGForPH 2013-05-21T21:36:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2013-05-21T21:36:44)
    0000   0x6c 0x64 0x35 0x15 0x0d                   ld5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2013-05-21T21:36:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 154,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9a                                  [.
    decimal
             91  154
    datetime (2013-05-21T21:36:53)
    0000   0x75 0x64 0x15 0x15 0x0d                   ud...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x02 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    4    0    2  125
    HOUR BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 212, 'amount': 3.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0xd4 0x04                   \....
    decimal
             92    5  144  212    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-05-21T21:36:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-05-21T21:36:54)
    0000   0x76 0x64 0x55 0x15 0x0d                   vdU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 41 CalBGForPH 2013-05-21T21:57:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-05-21T21:57:24)
    0000   0x58 0x79 0x35 0x15 0x0d                   Xy5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 42 CalBGForPH 2013-05-21T21:59:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-05-21T21:59:36)
    0000   0x64 0x7b 0x35 0x15 0x0d                   d{5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 43 BolusWizard 2013-05-21T22:00:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-05-21T22:00:13)
    0000   0x4d 0x40 0x16 0x15 0x0d                   M@...
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0xff 0x17 0xf0    .P.-j...
    0008   0x00 0x04 0x00 0x16 0x7d                   ....}
    decimal
             31   80   13   45  106  255   23  240
              0    4    0   22  125
    HOUR BITS: [0, 1, 0]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 0.2, 'curve': 4},
 {'age': 236, 'amount': 3.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x08 0x1a 0x04 0x90 0xec 0x04    \.......
    decimal
             92    8    8   26    4  144  236    4
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-05-21T22:00:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-05-21T22:00:13)
    0000   0x4d 0x40 0x56 0x15 0x0d                   M@V..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 46 CalBGForPH 2013-05-21T22:40:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-05-21T22:40:22)
    0000   0x56 0x68 0x36 0x15 0x0d                   Vh6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2013-05-21T22:41:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-05-21T22:41:06)
    0000   0x46 0x69 0x16 0x15 0x0d                   Fi...
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0xff 0x0d 0xf0    .P.-j...
    0008   0x00 0x15 0x00 0x0c 0x7d                   ....}
    decimal
             18   80   13   45  106  255   13  240
              0   21    0   12  125
    HOUR BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 2.2, 'curve': 4},
 {'age': 67, 'amount': 0.2, 'curve': 4},
 {'age': 21, 'amount': 3.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x2f 0x04 0x08 0x43 0x04    \.X/..C.
    0008   0x90 0x15 0x14                             ...
    decimal
             92   11   88   47    4    8   67    4
            144   21   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-05-21T22:41:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-05-21T22:41:06)
    0000   0x46 0x69 0x56 0x15 0x0d                   FiV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 50 MResultTotals 2013-05-22T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x94                   .....
    decimal
              7    0    0    4  148
    datetime (2013-05-22T00:00:00)
    0000   0x55 0x8d                                  U.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 Model522ResultTotals 2013-05-22T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-22T00:00:00)
    0000   0x55 0x8d                                  U.
    body (41)
    hex
    0000   0x05 0x10 0x97 0x66 0x22 0x05 0x00 0x00    ...f"...
    0008   0x04 0x94 0x03 0x74 0x4b 0x01 0x20 0x19    ...tK. .
    0010   0x00 0x31 0x01 0x20 0x19 0x00 0x88 0x2f    .1. .../
    0018   0x00 0x98 0x35 0x00 0x00 0x00 0x04 0x02    ..5.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  151  102   34    5    0    0
              4  148    3  116   75    1   32   25
              0   49    1   32   25    0  136   47
              0  152   53    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 52 PumpSuspend 2013-05-22T15:07:16 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-22T15:07:16)
    0000   0x50 0x47 0x0f 0x16 0x0d                   PG...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 53 PumpResume 2013-05-22T15:25:15 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-22T15:25:15)
    0000   0x4f 0x59 0x0f 0x16 0x0d                   OY...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 54 CalBGForPH 2013-05-22T18:43:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2013-05-22T18:43:43)
    0000   0x6b 0x6b 0x32 0x16 0x0d                   kk2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 55 BolusWizard 2013-05-22T18:44:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 135,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 2.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x87                                  [.
    decimal
             91  135
    datetime (2013-05-22T18:44:12)
    0000   0x4c 0x6c 0x12 0x16 0x0d                   Ll...
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x02 0x1d 0x00    &P.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             38   80   13   45  106    2   29    0
              0    0    0   31  125
    HOUR BITS: [0, 1, 1]
#### RECORD 56 Bolus 2013-05-22T18:44:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-05-22T18:44:12)
    0000   0x4c 0x6c 0x52 0x16 0x0d                   LlR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 57 MResultTotals 2013-05-23T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xf4                   .....
    decimal
              7    0    0    3  244
    datetime (2013-05-23T00:00:00)
    0000   0x56 0x8d                                  V.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 58 Model522ResultTotals 2013-05-23T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-23T00:00:00)
    0000   0x56 0x8d                                  V.
    body (41)
    hex
    0000   0x05 0x00 0x87 0x87 0x87 0x01 0x00 0x00    ........
    0008   0x03 0xf4 0x03 0x78 0x58 0x00 0x7c 0x0c    ...xX.|.
    0010   0x00 0x26 0x00 0x7c 0x0c 0x00 0x74 0x5e    .&.|..t^
    0018   0x00 0x08 0x06 0x00 0x00 0x00 0x01 0x00    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  135  135  135    1    0    0
              3  244    3  120   88    0  124   12
              0   38    0  124   12    0  116   94
              0    8    6    0    0    0    1    0
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 59 PumpSuspend 2013-05-23T11:38:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-23T11:38:39)
    0000   0x67 0x66 0x0b 0x17 0x0d                   gf...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 60 PumpResume 2013-05-23T12:00:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-23T12:00:31)
    0000   0x5f 0x40 0x0c 0x17 0x0d                   _@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 61 CalBGForPH 2013-05-23T12:27:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2013-05-23T12:27:41)
    0000   0x69 0x5b 0x2c 0x17 0x0d                   i[,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 62 BolusWizard 2013-05-23T12:27:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 184,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb8                                  [.
    decimal
             91  184
    datetime (2013-05-23T12:27:47)
    0000   0x6f 0x5b 0x0c 0x17 0x0d                   o[...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125
    HOUR BITS: [0, 1, 0]
#### RECORD 63 Bolus 2013-05-23T12:27:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-05-23T12:27:47)
    0000   0x6f 0x5b 0x4c 0x17 0x0d                   o[L..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 64 BolusWizard 2013-05-23T12:36:46 head[2], body[13] op[0x5b]
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
    datetime (2013-05-23T12:36:46)
    0000   0x6e 0x64 0x0c 0x17 0x0d                   nd...
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125
    HOUR BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 1.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x34 0x0c 0x04                   \.4..
    decimal
             92    5   52   12    4
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-05-23T12:36:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-05-23T12:36:46)
    0000   0x6e 0x64 0x4c 0x17 0x0d                   ndL..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 67 BolusWizard 2013-05-23T13:21:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.9,
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
    datetime (2013-05-23T13:21:20)
    0000   0x54 0x55 0x0d 0x17 0x0d                   TU...
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x00 0x27 0x00    3P.-j.'.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106    0   39    0
              0    0    0   39  125
    HOUR BITS: [0, 1, 0]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 1.5, 'curve': 4},
 {'age': 57, 'amount': 1.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x2f 0x04 0x34 0x39 0x04    \.</.49.
    decimal
             92    8   60   47    4   52   57    4
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-05-23T13:21:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-05-23T13:21:20)
    0000   0x54 0x55 0x4d 0x17 0x0d                   TUM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 70 CalBGForPH 2013-05-23T15:28:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2013-05-23T15:28:43)
    0000   0x6b 0x5c 0x2f 0x17 0x0d                   k\/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 71 CalBGForPH 2013-05-23T23:14:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-05-23T23:14:31)
    0000   0x5f 0x4e 0x37 0x17 0x0d                   _N7..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 72 BolusWizard 2013-05-23T23:14:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 100,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-05-23T23:14:59)
    0000   0x7b 0x4e 0x17 0x17 0x0d                   {N...
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xfe 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
             55   80   13   45  106  254   42  240
              0    0    0   40  125
    HOUR BITS: [0, 1, 0]
#### RECORD 73 Bolus 2013-05-23T23:14:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-05-23T23:14:59)
    0000   0x7b 0x4e 0x57 0x17 0x0d                   {NW..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 74 MResultTotals 2013-05-24T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x20                   .... 
    decimal
              7    0    0    5   32
    datetime (2013-05-24T00:00:00)
    0000   0x57 0x8d                                  W.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 75 Model522ResultTotals 2013-05-24T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-24T00:00:00)
    0000   0x57 0x8d                                  W.
    body (41)
    hex
    0000   0x05 0x00 0x73 0x3d 0xb8 0x03 0x00 0x00    ..s=....
    0008   0x05 0x20 0x03 0x74 0x43 0x01 0xac 0x21    . .tC..!
    0010   0x00 0x7e 0x01 0xac 0x21 0x01 0x78 0x58    .~..!.xX
    0018   0x00 0x34 0x0c 0x00 0x00 0x00 0x04 0x03    .4......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  115   61  184    3    0    0
              5   32    3  116   67    1  172   33
              0  126    1  172   33    1  120   88
              0   52   12    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 76 PumpSuspend 2013-05-24T14:35:34 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-24T14:35:34)
    0000   0x62 0x63 0x0e 0x18 0x0d                   bc...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 77 PumpResume 2013-05-24T15:00:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-24T15:00:35)
    0000   0x63 0x40 0x0f 0x18 0x0d                   c@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 78 CalBGForPH 2013-05-24T18:11:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-05-24T18:11:24)
    0000   0x58 0x4b 0x32 0x18 0x0d                   XK2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 79 BolusWizard 2013-05-24T18:11:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-05-24T18:11:59)
    0000   0x7b 0x4b 0x12 0x18 0x0d                   {K...
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    0P.-j.$.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             48   80   13   45  106    0   36    0
              0    0    0   36  125
    HOUR BITS: [0, 1, 0]
#### RECORD 80 Bolus 2013-05-24T18:11:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-05-24T18:11:59)
    0000   0x7b 0x4b 0x52 0x18 0x0d                   {KR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 81 MResultTotals 2013-05-25T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x04                   .....
    decimal
              7    0    0    4    4
    datetime (2013-05-25T00:00:00)
    0000   0x58 0x8d                                  X.
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-17.data: 82 records`
