## START logs/ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x52 0x91                                  R.
##### DEBUG DECIMAL
             82  145
#### RECORD 0 Bolus 2013-03-02T17:00:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-03-02T17:00:00)
    0000   0x00 0xc0 0x51 0x02 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 CalBGForPH 2013-03-02T18:03:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2013-03-02T18:03:38)
    0000   0x26 0xc3 0x32 0x02 0x0d                   &.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2013-03-02T18:03:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 161,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 2.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa1                                  [.
    decimal
             91  161
    datetime (2013-03-02T18:03:55)
    0000   0x37 0xc3 0x12 0x02 0x0d                   7....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0x08 0x16 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x1a 0x7d                   ....}
    decimal
             29   80   13   45  106    8   22    0
              0    4    0   26  125
    HOUR BITS: [1, 1, 0]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 0.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x14 0x45 0x04                   \..E.
    decimal
             92    5   20   69    4
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-03-02T18:03:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-03-02T18:03:55)
    0000   0x37 0xc3 0x52 0x02 0x0d                   7.R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 CalBGForPH 2013-03-02T19:54:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 371}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-03-02T19:54:55)
    0000   0x37 0xf6 0x33 0x02 0x8d                   7.3..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 6 BolusWizard 2013-03-02T19:54:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 371,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-03-02T19:54:59)
    0000   0x3b 0xf6 0x13 0x02 0x0d                   ;....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x36 0x00 0x00    .Q.-j6..
    0008   0x00 0x0f 0x00 0x27 0x7d                   ...'}
    decimal
              0   81   13   45  106   54    0    0
              0   15    0   39  125
    HOUR BITS: [1, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 110, 'amount': 2.45, 'curve': 4},
 {'age': 120, 'amount': 0.15, 'curve': 4},
 {'age': 180, 'amount': 0.5, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x62 0x6e 0x04 0x06 0x78 0x04    \.bn..x.
    0008   0x14 0xb4 0x04                             ...
    decimal
             92   11   98  110    4    6  120    4
             20  180    4
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-03-02T19:54:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-03-02T19:54:59)
    0000   0x3b 0xf6 0x53 0x02 0x0d                   ;.S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 CalBGForPH 2013-03-02T21:14:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 354}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2013-03-02T21:14:13)
    0000   0x0d 0xce 0x35 0x02 0x8d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 10 BolusWizard 2013-03-02T21:14:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 50,
 '_byte[7]': 0,
 'bg': 354,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2013-03-02T21:14:20)
    0000   0x14 0xce 0x15 0x02 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x32 0x00 0x00    .Q.-j2..
    0008   0x00 0x20 0x00 0x12 0x7d                   . ..}
    decimal
              0   81   13   45  106   50    0    0
              0   32    0   18  125
    HOUR BITS: [1, 1, 0]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 80, 'amount': 4.0, 'curve': 4},
 {'age': 190, 'amount': 2.45, 'curve': 4},
 {'age': 200, 'amount': 0.15, 'curve': 4},
 {'age': 4, 'amount': 0.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xa0 0x50 0x04 0x62 0xbe 0x04    \..P.b..
    0008   0x06 0xc8 0x04 0x14 0x04 0x14              ......
    decimal
             92   14  160   80    4   98  190    4
              6  200    4   20    4   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-03-02T21:14:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-03-02T21:14:20)
    0000   0x14 0xce 0x55 0x02 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 CalBGForPH 2013-03-02T22:29:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2013-03-02T22:29:01)
    0000   0x01 0xdd 0x36 0x02 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 BolusWizard 2013-03-02T22:34:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.1,
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
    datetime (2013-03-02T22:34:24)
    0000   0x18 0xe2 0x16 0x02 0x0d                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 80, 'amount': 1.8, 'curve': 4},
 {'age': 160, 'amount': 4.0, 'curve': 4},
 {'age': 14, 'amount': 2.45, 'curve': 20},
 {'age': 24, 'amount': 0.15, 'curve': 20},
 {'age': 84, 'amount': 0.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x50 0x04 0xa0 0xa0 0x04    \.HP....
    0008   0x62 0x0e 0x14 0x06 0x18 0x14 0x14 0x54    b......T
    0010   0x14                                       .
    decimal
             92   17   72   80    4  160  160    4
             98   14   20    6   24   20   20   84
             20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-03-02T22:34:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-03-02T22:34:24)
    0000   0x18 0xe2 0x56 0x02 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 ResultTotals 2013-02-02T13:13:34 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x12                   .....
    decimal
              7    0    0    5   18
    datetime (2013-02-02T13:13:34)
    0000   0x22 0x8d 0x6d 0x22 0x8d                   ".m".
    body (41)
    hex
    0000   0x05 0x10 0xd5 0x4f 0x73 0x05 0x00 0x00    ...Os...
    0008   0x05 0x12 0x03 0x82 0x45 0x01 0x90 0x1f    ....E...
    0010   0x00 0x3b 0x01 0x90 0x1f 0x00 0x98 0x26    .;.....&
    0018   0x00 0xf8 0x3e 0x00 0x00 0x00 0x05 0x02    ..>.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  213   79  115    5    0    0
              5   18    3  130   69    1  144   31
              0   59    1  144   31    0  152   38
              0  248   62    0    0    0    5    2
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 LowBattery 2013-03-03T19:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-03-03T19:01:00)
    0000   0x00 0xc1 0x13 0x03 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 Battery 2013-03-03T19:15:44 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-03-03T19:15:44)
    0000   0x2c 0xcf 0x13 0x03 0x0d                   ,....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 Battery 2013-03-03T19:16:04 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-03-03T19:16:04)
    0000   0x04 0xd0 0x13 0x03 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 21 PumpSuspend 2013-03-03T19:16:16 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-03T19:16:16)
    0000   0x10 0xd0 0x13 0x03 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 PumpResume 2013-03-03T19:38:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-03T19:38:33)
    0000   0x21 0xe6 0x13 0x03 0x0d                   !....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 23 CalBGForPH 2013-03-03T20:20:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-03-03T20:20:16)
    0000   0x10 0xd4 0x34 0x03 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 CalBGForPH 2013-03-03T20:20:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-03-03T20:20:46)
    0000   0x2e 0xd4 0x34 0x03 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BolusWizard 2013-03-03T20:21:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-03-03T20:21:19)
    0000   0x13 0xd5 0x14 0x03 0x0d                   .....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x00 0x2a 0x00    7P.-j.*.
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    0   42    0
              0    0    0   42  125
    HOUR BITS: [1, 1, 0]
#### RECORD 26 Bolus 2013-03-03T20:21:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-03-03T20:21:20)
    0000   0x14 0xd5 0x54 0x03 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 CalBGForPH 2013-03-03T21:12:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2013-03-03T21:12:38)
    0000   0x26 0xcc 0x35 0x03 0x0d                   &.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 CalBGForPH 2013-03-03T21:38:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-03-03T21:38:39)
    0000   0x27 0xe6 0x35 0x03 0x0d                   '.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 29 BolusWizard 2013-03-03T21:38:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 100,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-03-03T21:38:46)
    0000   0x2e 0xe6 0x15 0x03 0x0d                   .....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0xfe 0x0d 0xf0    .P.-j...
    0008   0x00 0x1d 0x00 0x0b 0x7d                   ....}
    decimal
             18   80   13   45  106  254   13  240
              0   29    0   11  125
    HOUR BITS: [1, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 74, 'amount': 0.25, 'curve': 4},
 {'age': 84, 'amount': 3.95, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x0a 0x4a 0x04 0x9e 0x54 0x04    \..J..T.
    decimal
             92    8   10   74    4  158   84    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-03-03T21:38:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-03-03T21:38:46)
    0000   0x2e 0xe6 0x55 0x03 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 ResultTotals 2013-02-03T13:13:35 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x48                   ....H
    decimal
              7    0    0    4   72
    datetime (2013-02-03T13:13:35)
    0000   0x23 0x8d 0x6d 0x23 0x8d                   #.m#.
    body (41)
    hex
    0000   0x05 0x00 0x6e 0x61 0x7a 0x04 0x00 0x00    ..naz...
    0008   0x04 0x48 0x03 0x74 0x51 0x00 0xd4 0x13    .H.tQ...
    0010   0x00 0x49 0x00 0xd4 0x13 0x00 0xd4 0x64    .I.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  110   97  122    4    0    0
              4   72    3  116   81    0  212   19
              0   73    0  212   19    0  212  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 PumpSuspend 2013-03-04T12:58:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-04T12:58:07)
    0000   0x07 0xfa 0x0c 0x04 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 PumpResume 2013-03-04T14:20:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-04T14:20:55)
    0000   0x37 0xd4 0x0e 0x04 0x0d                   7....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 35 CalBGForPH 2013-03-04T14:58:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-03-04T14:58:24)
    0000   0x18 0xfa 0x2e 0x04 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 BolusWizard 2013-03-04T14:58:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 128,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-03-04T14:58:35)
    0000   0x23 0xfa 0x0e 0x04 0x0d                   #....
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    #P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             35   80   13   45  106    0   26    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 1]
#### RECORD 37 Bolus 2013-03-04T14:58:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-03-04T14:58:35)
    0000   0x23 0xfa 0x4e 0x04 0x0d                   #.N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 CalBGForPH 2013-03-04T15:08:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-03-04T15:08:34)
    0000   0x22 0xc8 0x2f 0x04 0x0d                   "./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 39 BolusWizard 2013-03-04T15:09:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 21,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-03-04T15:09:10)
    0000   0x0a 0xc9 0x0f 0x04 0x0d                   .....
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x1a 0x00 0x10 0x7d                   ....}
    decimal
             21   80   13   45  106    0   16    0
              0   26    0   16  125
    HOUR BITS: [1, 1, 0]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0x0f 0x04                   \.h..
    decimal
             92    5  104   15    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2013-03-04T15:09:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-03-04T15:09:10)
    0000   0x0a 0xc9 0x4f 0x04 0x0d                   ..O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 42 CalBGForPH 2013-03-04T17:00:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2013-03-04T17:00:46)
    0000   0x2e 0xc0 0x31 0x04 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 43 BolusWizard 2013-03-04T17:01:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 97,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 21,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 1.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x61                                  [a
    decimal
             91   97
    datetime (2013-03-04T17:01:14)
    0000   0x0e 0xc1 0x11 0x04 0x0d                   .....
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0xfe 0x10 0xf0    .P.-j...
    0008   0x00 0x13 0x00 0x0e 0x7d                   ....}
    decimal
             21   80   13   45  106  254   16  240
              0   19    0   14  125
    HOUR BITS: [1, 1, 0]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 117, 'amount': 1.6, 'curve': 4},
 {'age': 127, 'amount': 2.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x75 0x04 0x68 0x7f 0x04    \.@u.h..
    decimal
             92    8   64  117    4  104  127    4
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-03-04T17:01:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-03-04T17:01:14)
    0000   0x0e 0xc1 0x51 0x04 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 46 CalBGForPH 2013-03-04T17:20:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-03-04T17:20:18)
    0000   0x12 0xd4 0x31 0x04 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 47 CalBGForPH 2013-03-04T18:29:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2013-03-04T18:29:15)
    0000   0x0f 0xdd 0x32 0x04 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 CalBGForPH 2013-03-04T18:29:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-03-04T18:29:30)
    0000   0x1e 0xdd 0x32 0x04 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 BolusWizard 2013-03-04T18:30:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 70,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 0.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2013-03-04T18:30:12)
    0000   0x0c 0xde 0x12 0x04 0x0d                   .....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0xf8 0x09 0xf0    .P.-j...
    0008   0x00 0x0d 0x00 0x01 0x7d                   ....}
    decimal
             12   80   13   45  106  248    9  240
              0   13    0    1  125
    HOUR BITS: [1, 1, 0]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 1.4, 'curve': 4},
 {'age': 206, 'amount': 1.6, 'curve': 4},
 {'age': 216, 'amount': 2.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0x60 0x04 0x40 0xce 0x04    \.8`.@..
    0008   0x68 0xd8 0x04                             h..
    decimal
             92   11   56   96    4   64  206    4
            104  216    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-03-04T18:30:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x01 0x01 0x00                        ....
    decimal
              1    1    1    0
    datetime (2013-03-04T18:30:12)
    0000   0x0c 0xde 0x52 0x04 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 52 CalBGForPH 2013-03-04T19:02:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2013-03-04T19:02:49)
    0000   0x31 0xc2 0x33 0x04 0x0d                   1.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 BolusWizard 2013-03-04T19:03:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 71,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2013-03-04T19:03:18)
    0000   0x12 0xc3 0x13 0x04 0x0d                   .....
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0xf8 0x2b 0xf0    9P.-j.+.
    0008   0x00 0x08 0x00 0x23 0x7d                   ...#}
    decimal
             57   80   13   45  106  248   43  240
              0    8    0   35  125
    HOUR BITS: [1, 1, 0]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 0.1, 'curve': 4},
 {'age': 129, 'amount': 1.4, 'curve': 4},
 {'age': 239, 'amount': 1.6, 'curve': 4},
 {'age': 249, 'amount': 2.6, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x04 0x27 0x04 0x38 0x81 0x04    \..'.8..
    0008   0x40 0xef 0x04 0x68 0xf9 0x04              @..h..
    decimal
             92   14    4   39    4   56  129    4
             64  239    4  104  249    4
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-03-04T19:03:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-03-04T19:03:19)
    0000   0x13 0xc3 0x53 0x04 0x0d                   ..S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 CalBGForPH 2013-03-04T20:44:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-03-04T20:44:38)
    0000   0x26 0xec 0x34 0x04 0x0d                   &.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 57 BolusWizard 2013-03-04T20:55:35 head[2], body[13] op[0x5b]
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
    datetime (2013-03-04T20:55:35)
    0000   0x23 0xf7 0x14 0x04 0x0d                   #....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [1, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 2.45, 'curve': 4},
 {'age': 121, 'amount': 1.05, 'curve': 4},
 {'age': 151, 'amount': 0.1, 'curve': 4},
 {'age': 241, 'amount': 1.4, 'curve': 4},
 {'age': 95, 'amount': 1.6, 'curve': 20},
 {'age': 105, 'amount': 2.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x62 0x6f 0x04 0x2a 0x79 0x04    \.bo.*y.
    0008   0x04 0x97 0x04 0x38 0xf1 0x04 0x40 0x5f    ...8..@_
    0010   0x14 0x68 0x69 0x14                        .hi.
    decimal
             92   20   98  111    4   42  121    4
              4  151    4   56  241    4   64   95
             20  104  105   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-03-04T20:55:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-03-04T20:55:35)
    0000   0x23 0xf7 0x54 0x04 0x0d                   #.T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 60 ResultTotals 2013-02-04T13:13:36 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0a                   .....
    decimal
              7    0    0    5   10
    datetime (2013-02-04T13:13:36)
    0000   0x24 0x8d 0x6d 0x24 0x8d                   $.m$.
    body (41)
    hex
    0000   0x05 0x00 0x5d 0x45 0x80 0x08 0x00 0x00    ..]E....
    0008   0x05 0x0a 0x03 0x4a 0x41 0x01 0xc0 0x23    ...JA..#
    0010   0x00 0xad 0x01 0xc0 0x23 0x01 0xc0 0x64    ....#..d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x06 0x06    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   93   69  128    8    0    0
              5   10    3   74   65    1  192   35
              0  173    1  192   35    1  192  100
              0    0    0    0    0    0    6    6
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 61 PumpSuspend 2013-03-05T14:27:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-05T14:27:05)
    0000   0x05 0xdb 0x0e 0x05 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 PumpResume 2013-03-05T14:50:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-05T14:50:30)
    0000   0x1e 0xf2 0x0e 0x05 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 63 CalBGForPH 2013-03-05T15:19:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-03-05T15:19:26)
    0000   0x1a 0xd3 0x2f 0x05 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 BolusWizard 2013-03-05T15:20:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-03-05T15:20:53)
    0000   0x35 0xd4 0x0f 0x05 0x0d                   5....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x00 0x1d 0x00    &P.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
             38   80   13   45  106    0   29    0
              0    0    0   29  125
    HOUR BITS: [1, 1, 0]
#### RECORD 65 Bolus 2013-03-05T15:20:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-03-05T15:20:53)
    0000   0x35 0xd4 0x4f 0x05 0x0d                   5.O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 66 CalBGForPH 2013-03-05T16:33:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 46}
```
    op hex (2)
    0000   0x0a 0x2e                                  ..
    decimal
             10   46
    datetime (2013-03-05T16:33:23)
    0000   0x17 0xe1 0x30 0x05 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 CalBGForPH 2013-03-05T18:31:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2013-03-05T18:31:13)
    0000   0x0d 0xdf 0x32 0x05 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 CalBGForPH 2013-03-05T18:31:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2013-03-05T18:31:34)
    0000   0x22 0xdf 0x32 0x05 0x0d                   ".2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 69 BolusWizard 2013-03-05T18:31:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 185,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb9                                  [.
    decimal
             91  185
    datetime (2013-03-05T18:31:43)
    0000   0x2b 0xdf 0x12 0x05 0x0d                   +....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    4    0    9  125
    HOUR BITS: [1, 1, 0]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 197, 'amount': 2.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0xc5 0x04                   \.t..
    decimal
             92    5  116  197    4
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-03-05T18:31:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-03-05T18:31:43)
    0000   0x2b 0xdf 0x52 0x05 0x0d                   +.R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 CalBGForPH 2013-03-05T19:23:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 162}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2013-03-05T19:23:23)
    0000   0x17 0xd7 0x33 0x05 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 73 BolusWizard 2013-03-05T19:24:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 162,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2013-03-05T19:24:02)
    0000   0x02 0xd8 0x13 0x05 0x0d                   .....
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0x08 0x35 0x00    FP.-j.5.
    0008   0x00 0x09 0x00 0x35 0x7d                   ...5}
    decimal
             70   80   13   45  106    8   53    0
              0    9    0   53  125
    HOUR BITS: [1, 1, 0]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 1.1, 'curve': 4},
 {'age': 250, 'amount': 2.9, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x3c 0x04 0x74 0xfa 0x04    \.,<.t..
    decimal
             92    8   44   60    4  116  250    4
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2013-03-05T19:24:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-03-05T19:24:02)
    0000   0x02 0xd8 0x53 0x05 0x0d                   ..S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 ResultTotals 2013-02-05T13:13:37 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xea                   .....
    decimal
              7    0    0    4  234
    datetime (2013-02-05T13:13:37)
    0000   0x25 0x8d 0x6d 0x25 0x8d                   %.m%.
    body (41)
    hex
    0000   0x05 0x00 0x8c 0x2e 0xb9 0x05 0x00 0x00    ........
    0008   0x04 0xea 0x03 0x76 0x46 0x01 0x74 0x1e    ...vF.t.
    0010   0x00 0x6c 0x01 0x74 0x1e 0x01 0x48 0x58    .l.t..HX
    0018   0x00 0x2c 0x0c 0x00 0x00 0x00 0x03 0x02    .,......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  140   46  185    5    0    0
              4  234    3  118   70    1  116   30
              0  108    1  116   30    1   72   88
              0   44   12    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 77 CalBGForPH 2013-03-06T08:05:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 377}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-03-06T08:05:13)
    0000   0x0d 0xc5 0x28 0x06 0x8d                   ..(..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 78 BolusWizard 2013-03-06T08:05:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 56,
 '_byte[7]': 0,
 'bg': 377,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
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
    datetime (2013-03-06T08:05:15)
    0000   0x0f 0xc5 0x08 0x06 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x38 0x00 0x00    .Q.-j8..
    0008   0x00 0x00 0x00 0x38 0x7d                   ...8}
    decimal
              0   81   13   45  106   56    0    0
              0    0    0   56  125
    HOUR BITS: [1, 1, 0]
#### RECORD 79 LowReservoir 2013-03-06T08:06:47 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-06T08:06:47)
    0000   0x2f 0xc6 0x08 0x06 0x0d                   /....
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-28.data: 80 records`
