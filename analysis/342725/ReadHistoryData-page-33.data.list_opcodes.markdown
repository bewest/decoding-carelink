## START logs/ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 680, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x14 0x00 0x04 0x7d 0x5c 0x05 0x50 0x15    ...}\.P.
    0008   0x04 0x01 0x08 0x08 0x00 0x0a 0xf7 0x4b    .......K
    0010   0x1a 0x0d 0x0a 0xc3 0x10 0xda 0x2c 0x1a    ......,.
    0018   0x0d 0x0a 0x81 0x28 0xf6 0x2c 0x1a 0x0d    ...(.,..
##### DEBUG DECIMAL
             20    0    4  125   92    5   80   21
              4    1    8    8    0   10  247   75
             26   13   10  195   16  218   44   26
             13   10  129   40  246   44   26   13
#### RECORD 0 Model522ResultTotals 2013-03-24T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-24T00:00:00)
    0000   0x37 0x8d                                  7.
    body (41)
    hex
    0000   0x05 0x10 0xd9 0x46 0x8f 0x0b 0x00 0x00    ...F....
    0008   0x04 0xce 0x03 0x72 0x48 0x01 0x5c 0x1c    ...rH.\.
    0010   0x00 0x18 0x01 0x5c 0x1c 0x00 0x48 0x15    ...\..H.
    0018   0x01 0x14 0x4f 0x00 0x00 0x00 0x04 0x00    ..O.....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  217   70  143   11    0    0
              4  206    3  114   72    1   92   28
              0   24    1   92   28    0   72   21
              1   20   79    0    0    0    4    0
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 PumpSuspend 2013-03-24T09:20:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-24T09:20:55)
    0000   0x37 0xd4 0x09 0x18 0x0d                   7....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 PumpResume 2013-03-24T09:33:23 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-24T09:33:23)
    0000   0x17 0xe1 0x09 0x18 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 CalBGForPH 2013-03-24T13:04:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-24T13:04:47)
    0000   0x2f 0xc4 0x2d 0x18 0x0d                   /.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-03-24T13:05:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-24T13:05:29)
    0000   0x1d 0xc5 0x2d 0x18 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BolusWizard 2013-03-24T13:07:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 2.4,
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
    datetime (2013-03-24T13:07:27)
    0000   0x1b 0xc7 0x0d 0x18 0x0d                   .....
    body (15)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xfc 0x18 0xf0     P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d 0x01 0x14         ....}..
    decimal
             32   80   13   45  106  252   24  240
              0    0    0   20  125    1   20
    HOUR BITS: [1, 1, 0]
#### RECORD 6 SelectBasalProfile 2013-03-24T13:07:27 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x00                                  ..
    decimal
             20    0
    datetime (2013-03-24T13:07:27)
    0000   0x1b 0xc7 0x4d 0x18 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2013-03-24T13:15:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-03-24T13:15:28)
    0000   0x1c 0xcf 0x2d 0x18 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 BolusWizard 2013-03-24T13:15:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-03-24T13:15:48)
    0000   0x30 0xcf 0x0d 0x18 0x0d                   0....
    body (15)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x14 0x00 0x0d 0x7d 0x5c 0x05         ....}\.
    decimal
             18   80   13   45  106    0   13    0
              0   20    0   13  125   92    5
    HOUR BITS: [1, 1, 0]
#### RECORD 9 Ian50 (2000, 0, 13, 13, 1, 4) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0b                                  P.
    decimal
             80   11
    datetime ((2000, 0, 13, 13, 1, 4))
    0000   0x04 0x01 0x0d 0x0d 0x00                   .....
    body (34)
    hex
    0000   0x31 0xcf 0x4d 0x18 0x0d 0x0a 0x61 0x3b    1.M...a;
    0008   0xe0 0x2d 0x18 0x0d 0x5b 0x61 0x16 0xe1    .-..[a..
    0010   0x0d 0x18 0x0d 0x13 0x50 0x0d 0x2d 0x6a    ....P.-j
    0018   0xfe 0x0e 0xf0 0x00 0x20 0x00 0x0c 0x7d    .... ..}
    0020   0x5c 0x08                                  \.
    decimal
             49  207   77   24   13   10   97   59
            224   45   24   13   91   97   22  225
             13   24   13   19   80   13   45  106
            254   14  240    0   32    0   12  125
             92    8

#### RECORD 10 LowReservoir (2001, 1, 4, 29, 16, 4) head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.9}
```
    op hex (2)
    0000   0x34 0x13                                  4.
    decimal
             52   19
    datetime ((2001, 1, 4, 29, 16, 4))
    0000   0x04 0x50 0x1d 0x04 0x01                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 11 ClearAlarm (2008, 0, 13, 1, 22, 0) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x0c                                  ..
    decimal
             12   12
    datetime ((2008, 0, 13, 1, 22, 0))
    0000   0x00 0x16 0xe1 0x4d 0x18                   ...M.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 12 Base (2008, 0, 15, 8, 41, 46) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2008, 0, 15, 8, 41, 46))
    0000   0x2e 0x29 0xc8 0x2f 0x18                   .)./.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 13 Base (2008, 4, 18, 8, 13, 62) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2008, 4, 18, 8, 13, 62))
    0000   0x7e 0x0d 0xe8 0x32 0x18                   ~..2.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 14 Base (2008, 4, 18, 23, 19, 62) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2008, 4, 18, 23, 19, 62))
    0000   0x7e 0x13 0xf7 0x32 0x18                   ~..2.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 15 Base (2008, 4, 18, 24, 18, 62) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2008, 4, 18, 24, 18, 62))
    0000   0x7e 0x12 0xf8 0x12 0x18                   ~....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 16 Base (2000, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x17                                  ..
    decimal
             13   23
    datetime ((2000, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x00                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 17 Base (2013, 0, 17, 0, 0, 0) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x00                                  ..
    decimal
             17    0
    datetime ((2013, 0, 17, 0, 0, 0))
    0000   0x00 0x00 0x00 0x11 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 0.25, 'curve': 20},
 {'age': 76, 'amount': 0.95, 'curve': 20},
 {'age': 86, 'amount': 1.3, 'curve': 20},
 {'age': 96, 'amount': 2.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0a 0x42 0x14 0x26 0x4c 0x14    \..B.&L.
    0008   0x34 0x56 0x14 0x50 0x60 0x14              4V.P`.
    decimal
             92   14   10   66   20   38   76   20
             52   86   20   80   96   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus (2007, 0, 19, 23, 10, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x11 0x11 0x00 0x12 0xf8 0x52 0x18    ......R.
    decimal
              1   17   17    0   18  248   82   24
    datetime ((2007, 0, 19, 23, 10, 13))
    0000   0x0d 0x0a 0x97 0x13 0xd7                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 1]
#### RECORD 20 TempBasal (2002, 0, 24, 23, 10, 13) head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.6}
```
    op hex (2)
    0000   0x33 0x18                                  3.
    decimal
             51   24
    datetime ((2002, 0, 24, 23, 10, 13))
    0000   0x0d 0x0a 0x97 0x38 0xe2                   ...8.
    body (1)
    hex
    0000   0x33                                       3
    decimal
             51
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 1, 0]
#### RECORD 21 NewTimeSet 2003-06-03T00:23:27 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime (2003-06-03T00:23:27)
    0000   0x5b 0x97 0x20 0xe3 0x13                   [. ..
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 22 NewTimeSet 2010-01-13T13:16:28 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x0d                                  ..
    decimal
             24   13
    datetime (2010-01-13T13:16:28)
    0000   0x1c 0x50 0x0d 0x2d 0x6a                   .P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 23 Base (2005, 0, 0, 16, 0, 0) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x15                                  ..
    decimal
              5   21
    datetime ((2005, 0, 0, 16, 0, 0))
    0000   0x00 0x00 0x10 0x00 0x15                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 24 Base (2010, 1, 4, 9, 4, 17) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x5c                                  }\
    decimal
            125   92
    datetime ((2010, 1, 4, 9, 4, 17))
    0000   0x11 0x44 0x29 0x04 0x0a                   .D)..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 25 Ian69 2013-01-20T20:51:38 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x14                                  i.
    decimal
            105   20
    datetime (2013-01-20T20:51:38)
    0000   0x26 0x73 0x14 0x34 0x7d                   &s.4}
    body (2)
    hex
    0000   0x14 0x50                                  .P
    decimal
             20   80
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 26 Base (2000, 0, 0, 21, 21, 1) head[2], body[0] op[0x87]

    op hex (2)
    0000   0x87 0x14                                  ..
    decimal
            135   20
    datetime ((2000, 0, 0, 21, 21, 1))
    0000   0x01 0x15 0x15 0x00 0x20                   .... 
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 27 Base (2000, 0, 0, 7, 13, 24) head[2], body[0] op[0xe3]

    op hex (2)
    0000   0xe3 0x53                                  .S
    decimal
            227   83
    datetime ((2000, 0, 0, 7, 13, 24))
    0000   0x18 0x0d 0x07 0x00 0x00                   .....
    body (0)

#### RECORD 28 Base (2013, 2, 24, 13, 13, 56) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0xc6                                  ..
    decimal
              4  198
    datetime ((2013, 2, 24, 13, 13, 56))
    0000   0x38 0x8d 0x6d 0x38 0x8d                   8.m8.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 Base (2000, 4, 9, 23, 46, 45) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 4, 9, 23, 46, 45))
    0000   0x6d 0x2e 0x97 0x09 0x00                   m....
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 Base (2001, 12, 9, 26, 3, 6) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2001, 12, 9, 26, 3, 6))
    0000   0xc6 0x03 0x7a 0x49 0x01                   ..zI.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 31 Base (2011, 1, 12, 1, 56, 0) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0x1b                                  L.
    decimal
             76   27
    datetime ((2011, 1, 12, 1, 56, 0))
    0000   0x00 0x78 0x01 0x4c 0x1b                   .x.L.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 32 Bolus (2000, 0, 0, 5, 5, 0) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.6, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x4c 0x64 0x00 0x00 0x00 0x00 0x00    .Ld.....
    decimal
              1   76  100    0    0    0    0    0
    datetime ((2000, 0, 0, 5, 5, 0))
    0000   0x00 0x05 0x05 0x00 0x00                   .....
    body (0)

#### RECORD 33 Base (2000, 3, 0, 0, 40, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0c                                  ..
    decimal
              0   12
    datetime ((2000, 3, 0, 0, 40, 0))
    0000   0x00 0xe8 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 PumpSuspend 2013-03-25T13:01:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-25T13:01:55)
    0000   0x37 0xc1 0x0d 0x19 0x0d                   7....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 35 PumpResume 2013-03-25T13:53:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-25T13:53:08)
    0000   0x08 0xf5 0x0d 0x19 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 CalBGForPH 2013-03-25T13:53:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-03-25T13:53:15)
    0000   0x0f 0xf5 0x2d 0x19 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 37 CalBGForPH 2013-03-25T13:57:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-03-25T13:57:19)
    0000   0x13 0xf9 0x2d 0x19 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 BolusWizard 2013-03-25T13:57:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2013-03-25T13:57:34)
    0000   0x22 0xf9 0x0d 0x19 0x0d                   "....
    body (15)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x00 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x22 0x7d 0x01 0x22         ..."}."
    decimal
             45   80   13   45  106    0   34    0
              0    0    0   34  125    1   34
    HOUR BITS: [1, 1, 1]
#### RECORD 39 Base (2013, 3, 25, 13, 57, 34) head[2], body[0] op[0x22]

    op hex (2)
    0000   0x22 0x00                                  ".
    decimal
             34    0
    datetime ((2013, 3, 25, 13, 57, 34))
    0000   0x22 0xf9 0x4d 0x19 0x0d                   ".M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 BolusWizard 2013-03-25T14:50:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.9,
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
    datetime (2013-03-25T14:50:06)
    0000   0x06 0xf2 0x0e 0x19 0x0d                   .....
    body (15)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d 0x5c 0x05         ....}\.
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125   92    5
    HOUR BITS: [1, 1, 1]
#### RECORD 41 Base (2000, 0, 9, 9, 1, 4) head[2], body[0] op[0x88]

    op hex (2)
    0000   0x88 0x38                                  .8
    decimal
            136   56
    datetime ((2000, 0, 9, 9, 1, 4))
    0000   0x04 0x01 0x09 0x09 0x00                   .....
    body (0)

#### RECORD 42 NoDelivery (2005, 0, 0, 17, 10, 13) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0xf2 0x4e 0x19                        ..N.
    decimal
              6  242   78   25
    datetime ((2005, 0, 0, 17, 10, 13))
    0000   0x0d 0x0a 0x91 0x00 0xd5                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 1]
#### RECORD 43 Base (2004, 0, 7, 19, 10, 13) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x19                                  0.
    decimal
             48   25
    datetime ((2004, 0, 7, 19, 10, 13))
    0000   0x0d 0x0a 0x93 0x07 0xe4                   .....
    body (0)
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 44 Base (2004, 1, 12, 19, 27, 13) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x19                                  0.
    decimal
             48   25
    datetime ((2004, 1, 12, 19, 27, 13))
    0000   0x0d 0x5b 0x93 0x0c 0xe4                   .[...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 0]
#### RECORD 45 Base (2013, 0, 13, 16, 23, 13) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x19                                  ..
    decimal
             16   25
    datetime ((2013, 0, 13, 16, 23, 13))
    0000   0x0d 0x17 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 46 Base (2000, 0, 13, 0, 0, 17) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x04                                  j.
    decimal
            106    4
    datetime ((2000, 0, 13, 0, 0, 17))
    0000   0x11 0x00 0x00 0x0d 0x00                   .....
    body (0)

#### RECORD 47 Base (2004, 4, 16, 4, 8, 28) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x7d                                  .}
    decimal
             17  125
    datetime ((2004, 4, 16, 4, 8, 28))
    0000   0x5c 0x08 0x24 0x70 0x04                   \.$p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 48 Base (2000, 0, 17, 17, 1, 4) head[2], body[0] op[0x88]

    op hex (2)
    0000   0x88 0xa2                                  ..
    decimal
            136  162
    datetime ((2000, 0, 17, 17, 1, 4))
    0000   0x04 0x01 0x11 0x11 0x00                   .....
    body (0)

#### RECORD 49 Base (2007, 4, 10, 13, 25, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0xe4                                  ..
    decimal
             13  228
    datetime ((2007, 4, 10, 13, 25, 16))
    0000   0x50 0x19 0x0d 0x0a 0xb7                   P....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 50 Base (2007, 0, 10, 13, 25, 49) head[2], body[0] op[0x1d]

    op hex (2)
    0000   0x1d 0xfa                                  ..
    decimal
             29  250
    datetime ((2007, 0, 10, 13, 25, 49))
    0000   0x31 0x19 0x0d 0x0a 0xb7                   1....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 51 Base (2007, 0, 27, 13, 25, 49) head[2], body[0] op[0x3b]

    op hex (2)
    0000   0x3b 0xfa                                  ;.
    decimal
             59  250
    datetime ((2007, 0, 27, 13, 25, 49))
    0000   0x31 0x19 0x0d 0x5b 0xb7                   1..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 52 Base (2000, 0, 0, 13, 25, 18) head[2], body[0] op[0x02]

    op hex (2)
    0000   0x02 0xc0                                  ..
    decimal
              2  192
    datetime ((2000, 0, 0, 13, 25, 18))
    0000   0x12 0x19 0x0d 0x20 0x50                   ... P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 53 Base (2000, 4, 0, 24, 12, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 24, 12, 42))
    0000   0x6a 0x0c 0x18 0x00 0x00                   j....
    body (0)

#### RECORD 54 Base (2004, 1, 11, 28, 61, 24) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2004, 1, 11, 28, 61, 24))
    0000   0x18 0x7d 0x5c 0x0b 0x44                   .}\.D
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 55 Base (2006, 3, 8, 4, 4, 36) head[2], body[0] op[0x56]

    op hex (2)
    0000   0x56 0x04                                  V.
    decimal
             86    4
    datetime ((2006, 3, 8, 4, 4, 36))
    0000   0x24 0xc4 0x04 0x88 0xf6                   $....
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 56 Base (2000, 0, 2, 0, 24, 24) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x01                                  ..
    decimal
              4    1
    datetime ((2000, 0, 2, 0, 24, 24))
    0000   0x18 0x18 0x00 0x02 0xc0                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 57 Base (2004, 0, 0, 0, 7, 13) head[2], body[0] op[0x52]

    op hex (2)
    0000   0x52 0x19                                  R.
    decimal
             82   25
    datetime ((2004, 0, 0, 0, 7, 13))
    0000   0x0d 0x07 0x00 0x00 0x04                   .....
    body (0)

#### RECORD 58 Base (2005, 9, 13, 25, 45, 13) head[2], body[0] op[0xae]

    op hex (2)
    0000   0xae 0x39                                  .9
    decimal
            174   57
    datetime ((2005, 9, 13, 25, 45, 13))
    0000   0x8d 0x6d 0x39 0x8d 0x05                   .m9..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 59 Base (2000, 6, 0, 6, 55, 48) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x93                                  ..
    decimal
              0  147
    datetime ((2000, 6, 0, 6, 55, 48))
    0000   0x70 0xb7 0x06 0x00 0x00                   p....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 60 Base (2000, 1, 1, 8, 30, 3) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0xae                                  ..
    decimal
              4  174
    datetime ((2000, 1, 1, 8, 30, 3))
    0000   0x03 0x5e 0x48 0x01 0x50                   .^H.P
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 61 Base (2001, 4, 28, 16, 1, 48) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x00                                  ..
    decimal
             28    0
    datetime ((2001, 4, 28, 16, 1, 48))
    0000   0x70 0x01 0x50 0x1c 0x01                   p.P..
    body (0)

#### RECORD 62 Ian50 (2000, 0, 0, 0, 0, 0) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x64                                  Pd
    decimal
             80  100
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (34)
    hex
    0000   0x00 0x04 0x04 0x00 0x00 0x00 0x0c 0x00    ........
    0008   0xe8 0x00 0x00 0x00 0x1e 0x00 0x27 0xf0    ......'.
    0010   0x0a 0x1a 0x0d 0x1f 0x00 0x29 0xc9 0x0b    .....)..
    0018   0x1a 0x0d 0x0a 0xd5 0x0d 0xe9 0x2b 0x1a    ......+.
    0020   0x0d 0x5b                                  .[
    decimal
              0    4    4    0    0    0   12    0
            232    0    0    0   30    0   39  240
             10   26   13   31    0   41  201   11
             26   13   10  213   13  233   43   26
             13   91

#### RECORD 63 Base (2000, 12, 13, 26, 11, 41) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x16                                  ..
    decimal
            213   22
    datetime ((2000, 12, 13, 26, 11, 41))
    0000   0xe9 0x0b 0x1a 0x0d 0x00                   .....
    body (0)

#### RECORD 64 Ian50 (2000, 1, 0, 19, 42, 45) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime ((2000, 1, 0, 19, 42, 45))
    0000   0x2d 0x6a 0x13 0x00 0x00                   -j...
    body (34)
    hex
    0000   0x00 0x00 0x00 0x13 0x7d 0x01 0x14 0x14    ....}...
    0008   0x00 0x16 0xe9 0x4b 0x1a 0x0d 0x0a 0xeb    ...K....
    0010   0x03 0xf7 0x2b 0x1a 0x0d 0x5b 0xeb 0x0a    ..+..[..
    0018   0xf7 0x0b 0x1a 0x0d 0x00 0x50 0x0d 0x2d    .....P.-
    0020   0x6a 0x18                                  j.
    decimal
              0    0    0   19  125    1   20   20
              0   22  233   75   26   13   10  235
              3  247   43   26   13   91  235   10
            247   11   26   13    0   80   13   45
            106   24
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-33.data: 65 records`
