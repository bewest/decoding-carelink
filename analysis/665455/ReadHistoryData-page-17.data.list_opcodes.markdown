## START logs/ReadHistoryData-page-17.data
#### STOPPING DOUBLE NULLS @ 409, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x24 0x52 0x4d 0x35 0x15 0x0d 0x03 0x00    $RM5....
    0008   0x05 0x00 0x05 0x66 0x4d 0x15 0x15 0x0d    ...fM...
    0010   0x0a 0x9a 0x6c 0x64 0x35 0x15 0x0d 0x5b    ..ld5..[
    0018   0x9a 0x75 0x64 0x15 0x15 0x0d 0x00 0x50    .ud....P
##### DEBUG DECIMAL
             36   82   77   53   21   13    3    0
              5    0    5  102   77   21   21   13
             10  154  108  100   53   21   13   91
            154  117  100   21   21   13    0   80
#### RECORD 0 hack1 2013-05-20T03:35:43 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x53 0x8d 0x05 0x10 0xa6 0x6a 0x12    mS....j.
    0008   0x05 0x00 0x00 0x05 0x34 0x03 0x78 0x43    ....4.xC
    0010   0x01 0xbc 0x21 0x00 0x62 0x01 0xbc 0x21    ..!.b..!
    0018   0x01 0x28 0x43 0x00 0x94 0x21 0x00 0x00    .(C..!..
    0020   0x00 0x04 0x01 0x02 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0xe7              ......
    decimal
            109   83  141    5   16  166  106   18
              5    0    0    5   52    3  120   67
              1  188   33    0   98    1  188   33
              1   40   67    0  148   33    0    0
              0    4    1    2    1    0   12    0
            232    0    0    0   10  231
    datetime (2013-05-20T03:35:43)
    0000   0x6b 0x63 0x23 0x14 0x0d                   kc#..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-05-20T03:35:45 head[2], body[13] op[0x5b]
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
#### RECORD 2 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
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

#### RECORD 3 Bolus 2013-05-20T03:35:46 head[4], body[0] op[0x01]
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
#### RECORD 4 PumpSuspend 2013-05-20T09:53:48 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-20T09:53:48)
    0000   0x70 0x75 0x09 0x14 0x0d                   pu...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 PumpResume 2013-05-20T10:17:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-20T10:17:07)
    0000   0x47 0x51 0x0a 0x14 0x0d                   GQ...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 CalBGForPH 2013-05-20T10:49:45 head[2], body[0] op[0x0a]
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
#### RECORD 7 BolusWizard 2013-05-20T10:49:51 head[2], body[13] op[0x5b]
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
#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
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

#### RECORD 9 Bolus 2013-05-20T10:49:51 head[4], body[0] op[0x01]
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
#### RECORD 10 CalBGForPH 2013-05-20T12:31:43 head[2], body[0] op[0x0a]
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
#### RECORD 11 BolusWizard 2013-05-20T12:32:15 head[2], body[13] op[0x5b]
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
#### RECORD 12 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
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

#### RECORD 13 Bolus 2013-05-20T12:32:16 head[4], body[0] op[0x01]
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
#### RECORD 14 CalBGForPH 2013-05-20T17:34:39 head[2], body[0] op[0x0a]
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
#### RECORD 15 CalBGForPH 2013-05-20T17:36:57 head[2], body[0] op[0x0a]
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
#### RECORD 16 BolusWizard 2013-05-20T17:37:43 head[2], body[13] op[0x5b]
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
#### RECORD 17 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
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

#### RECORD 18 Bolus 2013-05-20T17:37:43 head[4], body[0] op[0x01]
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
#### RECORD 19 CalBGForPH 2013-05-20T20:35:56 head[2], body[0] op[0x0a]
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
#### RECORD 20 CalBGForPH 2013-05-20T20:46:59 head[2], body[0] op[0x0a]
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
#### RECORD 21 BolusWizard 2013-05-20T20:47:26 head[2], body[13] op[0x5b]
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
#### RECORD 22 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
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

#### RECORD 23 Bolus 2013-05-20T20:47:26 head[4], body[0] op[0x01]
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
#### RECORD 24 ResultTotals 2013-06-20T13:13:20 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x82                   .....
    decimal
              7    0    0    5  130
    datetime (2013-06-20T13:13:20)
    0000   0x54 0x8d 0x6d 0x54 0x8d                   T.mT.
    body (51)
    hex
    0000   0x05 0x00 0x99 0x52 0xff 0x07 0x00 0x00    ...R....
    0008   0x05 0x82 0x03 0x72 0x3f 0x02 0x10 0x25    ...r?..%
    0010   0x00 0x6d 0x02 0x10 0x25 0x01 0x3c 0x3c    .m..%.<<
    0018   0x00 0xd4 0x28 0x00 0x00 0x00 0x05 0x02    ..(.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x34 0xc8 0x43 0x69 0x07 0x15 0x0d    .4.Ci...
    0030   0x1e 0x00 0x6c                             ..l
    decimal
              5    0  153   82  255    7    0    0
              5  130    3  114   63    2   16   37
              0  109    2   16   37    1   60   60
              0  212   40    0    0    0    5    2
              2    1    0   12    0  232    0    0
              0   52  200   67  105    7   21   13
             30    0  108
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 Base (2009, 0, 0, 31, 13, 21) head[2], body[0] op[0x4f]

    op hex (2)
    0000   0x4f 0x0f                                  O.
    decimal
             79   15
    datetime ((2009, 0, 0, 31, 13, 21))
    0000   0x15 0x0d 0x1f 0x00 0x49                   ....I
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 26 ChangeUtility (2015, 0, 4, 20, 13, 21) head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x0f                                  c.
    decimal
             99   15
    datetime ((2015, 0, 4, 20, 13, 21))
    0000   0x15 0x0d 0x34 0x64 0x5f                   ..4d_
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 27 Base (2001, 0, 2, 10, 13, 21) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x11                                  r.
    decimal
            114   17
    datetime ((2001, 0, 2, 10, 13, 21))
    0000   0x15 0x0d 0x0a 0x22 0x61                   ..."a
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 28 Base (2004, 2, 2, 27, 13, 21) head[2], body[0] op[0x47]

    op hex (2)
    0000   0x47 0x32                                  G2
    decimal
             71   50
    datetime ((2004, 2, 2, 27, 13, 21))
    0000   0x15 0x8d 0x5b 0x22 0x64                   ..["d
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 29 Base (2013, 0, 17, 0, 13, 21) head[2], body[0] op[0x47]

    op hex (2)
    0000   0x47 0x12                                  G.
    decimal
             71   18
    datetime ((2013, 0, 17, 0, 13, 21))
    0000   0x15 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 30 Base (2000, 0, 0, 0, 0, 36) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 36))
    0000   0x24 0x00 0x00 0x00 0x00                   $....
    body (0)

#### RECORD 31 Base (2000, 4, 4, 4, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x24                                  .$
    decimal
              0   36
    datetime ((2000, 4, 4, 4, 1, 61))
    0000   0x7d 0x01 0x24 0x24 0x00                   }.$$.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 32 ChangeTimeDisplay 2000-04-01T13:21:18 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x47                                  dG
    decimal
            100   71
    datetime (2000-04-01T13:21:18)
    0000   0x52 0x15 0x0d 0x21 0x00                   R..!.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 33 Base (2000, 0, 3, 13, 21, 21) head[2], body[0] op[0x71]

    op hex (2)
    0000   0x71 0x4a                                  qJ
    decimal
            113   74
    datetime ((2000, 0, 3, 13, 21, 21))
    0000   0x15 0x15 0x0d 0x03 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-17.data: 34 records`
