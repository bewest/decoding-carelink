## START logs/ReadHistoryData-page-3.data
#### RECORD 0 BolusWizard 2013-01-11T17:19:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 35,
 '_byte[7]': 0,
 'bg': 286,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x1e                                  [.
    decimal
             91   30
    datetime (2013-01-11T17:19:20)
    0000   0x14 0x53 0x11 0x0b 0x0d                   .S...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00 0x00    .Q.-j#..
    0008   0x00 0x0e 0x00 0x15 0x7d                   ....}
    decimal
              0   81   13   45  106   35    0    0
              0   14    0   21  125
    HOUR BITS: [0, 1, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 105, 'amount': 2.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x64 0x69 0x04                   \.di.
    decimal
             92    5  100  105    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-01-11T17:19:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-01-11T17:19:20)
    0000   0x14 0x53 0x51 0x0b 0x0d                   .SQ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 CalBGForPH 2013-01-11T18:13:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 339}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2013-01-11T18:13:50)
    0000   0x32 0x4d 0x32 0x0b 0x8d                   2M2..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 BolusWizard 2013-01-11T18:14:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 47,
 '_byte[7]': 0,
 'bg': 339,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x53                                  [S
    decimal
             91   83
    datetime (2013-01-11T18:14:05)
    0000   0x05 0x4e 0x12 0x0b 0x0d                   .N...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2f 0x00 0x00    .Q.-j/..
    0008   0x00 0x1c 0x00 0x13 0x7d                   ....}
    decimal
              0   81   13   45  106   47    0    0
              0   28    0   19  125
    HOUR BITS: [0, 1, 0]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 2.6, 'curve': 4},
 {'age': 160, 'amount': 2.5, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x68 0x3c 0x04 0x64 0xa0 0x04    \.h<.d..
    decimal
             92    8  104   60    4  100  160    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-01-11T18:14:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-01-11T18:14:05)
    0000   0x05 0x4e 0x52 0x0b 0x0d                   .NR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-01-11T18:43:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 292}
```
    op hex (2)
    0000   0x0a 0x24                                  .$
    decimal
             10   36
    datetime (2013-01-11T18:43:40)
    0000   0x28 0x6b 0x32 0x0b 0x8d                   (k2..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 CalBGForPH 2013-01-11T19:12:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 214}
```
    op hex (2)
    0000   0x0a 0xd6                                  ..
    decimal
             10  214
    datetime (2013-01-11T19:12:57)
    0000   0x39 0x4c 0x33 0x0b 0x0d                   9L3..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 9 CalBGForPH 2013-01-11T19:59:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-01-11T19:59:23)
    0000   0x17 0x7b 0x33 0x0b 0x0d                   .{3..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 CalBGForPH 2013-01-11T20:00:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-01-11T20:00:10)
    0000   0x0a 0x40 0x34 0x0b 0x0d                   .@4..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 11 BolusWizard 2013-01-11T20:00:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.7,
 'carb_input': 88,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 6.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-01-11T20:00:33)
    0000   0x21 0x40 0x14 0x0b 0x0d                   !@...
    body (13)
    hex
    0000   0x58 0x50 0x0d 0x2d 0x6a 0x02 0x43 0x00    XP.-j.C.
    0008   0x00 0x13 0x00 0x43 0x7d                   ...C}
    decimal
             88   80   13   45  106    2   67    0
              0   19    0   67  125
    HOUR BITS: [0, 1, 0]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 106, 'amount': 2.4, 'curve': 4},
 {'age': 166, 'amount': 2.6, 'curve': 4},
 {'age': 10, 'amount': 2.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x60 0x6a 0x04 0x68 0xa6 0x04    \.`j.h..
    0008   0x64 0x0a 0x14                             d..
    decimal
             92   11   96  106    4  104  166    4
            100   10   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-01-11T20:00:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.7, 'programmed': 6.7}
```
    op hex (4)
    0000   0x01 0x43 0x43 0x04                        .CC.
    decimal
              1   67   67    4
    datetime (2013-01-11T20:00:33)
    0000   0x21 0x40 0x74 0x0b 0x0d                   !@t..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 14 ResultTotals 2013-02-11T13:13:11 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xa6                   .....
    decimal
              7    0    0    5  166
    datetime (2013-02-11T13:13:11)
    0000   0x0b 0x8d 0x6d 0x0b 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xde 0x88 0x53 0x07 0x00 0x00    ....S...
    0008   0x05 0xa6 0x03 0x6e 0x3d 0x02 0x38 0x27    ...n=.8'
    0010   0x00 0x72 0x02 0x38 0x27 0x01 0x5c 0x3d    .r.8'.\=
    0018   0x00 0xdc 0x27 0x00 0x00 0x00 0x04 0x01    ..'.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  222  136   83    7    0    0
              5  166    3  110   61    2   56   39
              0  114    2   56   39    1   92   61
              0  220   39    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 CalBGForPH 2013-01-12T02:12:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 379}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-01-12T02:12:46)
    0000   0x2e 0x4c 0x22 0x0c 0x8d                   .L"..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 BolusWizard 2013-01-12T02:13:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 56,
 '_byte[7]': 0,
 'bg': 379,
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
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2013-01-12T02:13:13)
    0000   0x0d 0x4d 0x02 0x0c 0x0d                   .M...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x38 0x00 0x00    .Q.-j8..
    0008   0x00 0x00 0x00 0x38 0x7d                   ...8}
    decimal
              0   81   13   45  106   56    0    0
              0    0    0   56  125
    HOUR BITS: [0, 1, 0]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 0.35, 'curve': 20},
 {'age': 13, 'amount': 0.6, 'curve': 20},
 {'age': 23, 'amount': 0.55, 'curve': 20},
 {'age': 33, 'amount': 0.55, 'curve': 20},
 {'age': 43, 'amount': 0.55, 'curve': 20},
 {'age': 53, 'amount': 0.55, 'curve': 20},
 {'age': 63, 'amount': 0.55, 'curve': 20},
 {'age': 73, 'amount': 0.6, 'curve': 20},
 {'age': 83, 'amount': 0.55, 'curve': 20},
 {'age': 93, 'amount': 0.55, 'curve': 20},
 {'age': 103, 'amount': 0.55, 'curve': 20},
 {'age': 113, 'amount': 0.55, 'curve': 20},
 {'age': 123, 'amount': 0.2, 'curve': 20},
 {'age': 223, 'amount': 2.4, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0x0e 0x03 0x14 0x18 0x0d 0x14    \,......
    0008   0x16 0x17 0x14 0x16 0x21 0x14 0x16 0x2b    ....!..+
    0010   0x14 0x16 0x35 0x14 0x16 0x3f 0x14 0x18    ..5..?..
    0018   0x49 0x14 0x16 0x53 0x14 0x16 0x5d 0x14    I..S..].
    0020   0x16 0x67 0x14 0x16 0x71 0x14 0x08 0x7b    .g..q..{
    0028   0x14 0x60 0xdf 0x14                        .`..
    decimal
             92   44   14    3   20   24   13   20
             22   23   20   22   33   20   22   43
             20   22   53   20   22   63   20   24
             73   20   22   83   20   22   93   20
             22  103   20   22  113   20    8  123
             20   96  223   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-01-12T02:13:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0, 'programmed': 6.0}
```
    op hex (4)
    0000   0x01 0x3c 0x3c 0x00                        .<<.
    decimal
              1   60   60    0
    datetime (2013-01-12T02:13:13)
    0000   0x0d 0x4d 0x42 0x0c 0x0d                   .MB..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 19 CalBGForPH 2013-01-12T08:05:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 319}
```
    op hex (2)
    0000   0x0a 0x3f                                  .?
    decimal
             10   63
    datetime (2013-01-12T08:05:27)
    0000   0x1b 0x45 0x28 0x0c 0x8d                   .E(..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 BolusWizard 2013-01-12T08:05:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 43,
 '_byte[7]': 0,
 'bg': 319,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3f                                  [?
    decimal
             91   63
    datetime (2013-01-12T08:05:32)
    0000   0x20 0x45 0x08 0x0c 0x0d                    E...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2b 0x00 0x00    .Q.-j+..
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
              0   81   13   45  106   43    0    0
              0    0    0   43  125
    HOUR BITS: [0, 1, 0]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 95, 'amount': 4.8, 'curve': 20},
 {'age': 105, 'amount': 1.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0x5f 0x14 0x30 0x69 0x14    \.._.0i.
    decimal
             92    8  192   95   20   48  105   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-01-12T08:05:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'programmed': 4.6}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-01-12T08:05:32)
    0000   0x20 0x45 0x48 0x0c 0x0d                    EH..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 23 CalBGForPH 2013-01-12T12:57:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-01-12T12:57:23)
    0000   0x17 0x79 0x2c 0x0c 0x0d                   .y,..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 24 BolusWizard 2013-01-12T12:57:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 1.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-01-12T12:57:29)
    0000   0x1d 0x79 0x0c 0x0c 0x0d                   .y...
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x09 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
             24   80   13   45  106    9   18    0
              0    0    0   27  125
    HOUR BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 4.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb8 0x25 0x14                   \..%.
    decimal
             92    5  184   37   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-01-12T12:57:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'programmed': 2.7}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-01-12T12:57:30)
    0000   0x1e 0x79 0x4c 0x0c 0x0d                   .yL..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 27 CalBGForPH 2013-01-12T15:05:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-01-12T15:05:41)
    0000   0x29 0x45 0x2f 0x0c 0x0d                   )E/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 28 BolusWizard 2013-01-12T15:05:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2013-01-12T15:05:52)
    0000   0x34 0x45 0x0f 0x0c 0x0d                   4E...
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0   11    0   13  125
    HOUR BITS: [0, 1, 0]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 131, 'amount': 2.7, 'curve': 4},
 {'age': 165, 'amount': 4.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x83 0x04 0xb8 0xa5 0x14    \.l.....
    decimal
             92    8  108  131    4  184  165   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-01-12T15:05:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-01-12T15:05:52)
    0000   0x34 0x45 0x4f 0x0c 0x0d                   4EO..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 31 CalBGForPH 2013-01-12T16:56:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-01-12T16:56:57)
    0000   0x39 0x78 0x30 0x0c 0x0d                   9x0..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2013-01-12T16:57:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 116,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-01-12T16:57:17)
    0000   0x11 0x79 0x10 0x0c 0x0d                   .y...
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0x00 0x2d 0x00    ;P.-j.-.
    0008   0x00 0x07 0x00 0x2d 0x7d                   ...-}
    decimal
             59   80   13   45  106    0   45    0
              0    7    0   45  125
    HOUR BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 113, 'amount': 1.3, 'curve': 4},
 {'age': 243, 'amount': 2.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x71 0x04 0x6c 0xf3 0x04    \.4q.l..
    decimal
             92    8   52  113    4  108  243    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-01-12T16:57:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'programmed': 4.5}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-01-12T16:57:17)
    0000   0x11 0x79 0x50 0x0c 0x0d                   .yP..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 35 LowReservoir 2013-01-12T21:28:25 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-01-12T21:28:25)
    0000   0x19 0x5c 0x15 0x0c 0x0d                   .\...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 ResultTotals 2013-02-12T13:13:12 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x80                   .....
    decimal
              7    0    0    6  128
    datetime (2013-02-12T13:13:12)
    0000   0x0c 0x8d 0x6d 0x0c 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xdb 0x72 0x7b 0x05 0x00 0x00    ...r{...
    0008   0x06 0x80 0x03 0x84 0x36 0x02 0xfc 0x2e    ....6...
    0010   0x00 0x65 0x02 0xfc 0x2e 0x01 0x30 0x28    .e....0(
    0018   0x01 0xcc 0x3c 0x00 0x00 0x00 0x05 0x02    ..<.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  219  114  123    5    0    0
              6  128    3  132   54    2  252   46
              0  101    2  252   46    1   48   40
              1  204   60    0    0    0    5    2
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 CalBGForPH 2013-01-13T00:27:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-01-13T00:27:30)
    0000   0x1e 0x5b 0x20 0x0d 0x0d                   .[ ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 BolusWizard 2013-01-13T00:27:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 123,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2013-01-13T00:27:40)
    0000   0x28 0x5b 0x00 0x0d 0x0d                   ([...
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x00 0x1c 0x00    %P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106    0   28    0
              0    0    0   28  125
    HOUR BITS: [0, 1, 0]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 197, 'amount': 4.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0xc5 0x14                   \....
    decimal
             92    5  180  197   20
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-01-13T00:27:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'programmed': 2.8}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-01-13T00:27:40)
    0000   0x28 0x5b 0x40 0x0d 0x0d                   ([@..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 41 BolusWizard 2013-01-13T01:34:32 head[2], body[13] op[0x5b]
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
    datetime (2013-01-13T01:34:32)
    0000   0x20 0x62 0x01 0x0d 0x0d                    b...
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125
    HOUR BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 70, 'amount': 2.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0x46 0x04                   \.pF.
    decimal
             92    5  112   70    4
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-01-13T01:34:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-01-13T01:34:32)
    0000   0x20 0x62 0x41 0x0d 0x0d                    bA..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 44 LowReservoir 2013-01-13T04:37:30 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-01-13T04:37:30)
    0000   0x1e 0x65 0x04 0x0d 0x0d                   .e...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 45 CalBGForPH 2013-01-13T09:23:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 331}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-01-13T09:23:56)
    0000   0x38 0x57 0x29 0x0d 0x8d                   8W)..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 46 BolusWizard 2013-01-13T09:24:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 45,
 '_byte[7]': 0,
 'bg': 331,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
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
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-01-13T09:24:00)
    0000   0x00 0x58 0x09 0x0d 0x0d                   .X...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2d 0x00 0x00    .Q.-j-..
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
              0   81   13   45  106   45    0    0
              0    0    0   45  125
    HOUR BITS: [0, 1, 0]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 214, 'amount': 1.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0xd6 0x14                   \.,..
    decimal
             92    5   44  214   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2013-01-13T09:24:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'programmed': 4.5}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-01-13T09:24:00)
    0000   0x00 0x58 0x49 0x0d 0x0d                   .XI..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 49 PumpSuspend 2013-01-13T09:27:35 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-13T09:27:35)
    0000   0x23 0x5b 0x09 0x0d 0x0d                   #[...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 50 PumpResume 2013-01-13T10:45:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-13T10:45:06)
    0000   0x06 0x6d 0x0a 0x0d 0x0d                   .m...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 51 CalBGForPH 2013-01-13T12:09:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2013-01-13T12:09:42)
    0000   0x2a 0x49 0x2c 0x0d 0x0d                   *I,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 52 BolusWizard 2013-01-13T12:09:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 127,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7f                                  [.
    decimal
             91  127
    datetime (2013-01-13T12:09:53)
    0000   0x35 0x49 0x0c 0x0d 0x0d                   5I...
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x00 0x22 0x00    -P.-j.".
    0008   0x00 0x0b 0x00 0x22 0x7d                   ..."}
    decimal
             45   80   13   45  106    0   34    0
              0   11    0   34  125
    HOUR BITS: [0, 1, 0]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 165, 'amount': 4.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0xa5 0x04                   \....
    decimal
             92    5  180  165    4
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-01-13T12:09:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-01-13T12:09:53)
    0000   0x35 0x49 0x4c 0x0d 0x0d                   5IL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 55 Rewind 2013-01-13T20:48:29 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-01-13T20:48:29)
    0000   0x1d 0x70 0x14 0x0d 0x0d                   .p...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 56 Prime 2013-01-13T20:50:26 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2d                   ....-
    decimal
              3    0    0    0   45
    datetime (2013-01-13T20:50:26)
    0000   0x1a 0x72 0x34 0x0d 0x0d                   .r4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 57 Prime 2013-01-13T20:50:55 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-01-13T20:50:55)
    0000   0x37 0x72 0x14 0x0d 0x0d                   7r...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 58 CalBGForPH 2013-01-13T21:39:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-01-13T21:39:33)
    0000   0x21 0x67 0x35 0x0d 0x0d                   !g5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 59 BolusWizard 2013-01-13T21:40:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 76,
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
    0000   0x5b 0x4c                                  [L
    decimal
             91   76
    datetime (2013-01-13T21:40:19)
    0000   0x13 0x68 0x15 0x0d 0x0d                   .h...
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0xf9 0x27 0xf0    3P.-j.'.
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             51   80   13   45  106  249   39  240
              0    0    0   32  125
    HOUR BITS: [0, 1, 1]
#### RECORD 60 Bolus 2013-01-13T21:40:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-01-13T21:40:19)
    0000   0x13 0x68 0x55 0x0d 0x0d                   .hU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 61 CalBGForPH 2013-01-13T21:59:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-01-13T21:59:30)
    0000   0x1e 0x7b 0x35 0x0d 0x0d                   .{5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 62 BolusWizard 2013-01-13T21:59:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 124,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7c                                  [|
    decimal
             91  124
    datetime (2013-01-13T21:59:53)
    0000   0x35 0x7b 0x15 0x0d 0x0d                   5{...
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x1f 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0   31    0   21  125
    HOUR BITS: [0, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 3.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x80 0x19 0x04                   \....
    decimal
             92    5  128   25    4
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-01-13T21:59:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'programmed': 2.1}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-01-13T21:59:53)
    0000   0x35 0x7b 0x55 0x0d 0x0d                   5{U..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 65 BolusWizard 2013-01-13T22:09:33 head[2], body[13] op[0x5b]
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
    datetime (2013-01-13T22:09:33)
    0000   0x21 0x49 0x16 0x0d 0x0d                   !I...
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [0, 1, 0]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 2.1, 'curve': 4},
 {'age': 35, 'amount': 3.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x54 0x0f 0x04 0x80 0x23 0x04    \.T...#.
    decimal
             92    8   84   15    4  128   35    4
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-01-13T22:09:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-01-13T22:09:33)
    0000   0x21 0x49 0x56 0x0d 0x0d                   !IV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 68 ResultTotals 2013-02-13T13:13:13 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x40                   ....@
    decimal
              7    0    0    6   64
    datetime (2013-02-13T13:13:13)
    0000   0x0d 0x8d 0x6d 0x0d 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x9c 0x4c 0x4b 0x05 0x00 0x00    ...LK...
    0008   0x06 0x40 0x03 0x48 0x34 0x02 0xf8 0x30    .@.H4..0
    0010   0x00 0xc9 0x02 0xf8 0x30 0x02 0x44 0x4c    ....0.DL
    0018   0x00 0xb4 0x18 0x00 0x00 0x00 0x07 0x06    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  156   76   75    5    0    0
              6   64    3   72   52    2  248   48
              0  201    2  248   48    2   68   76
              0  180   24    0    0    0    7    6
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 CalBGForPH 2013-01-14T02:19:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 428}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-01-14T02:19:22)
    0000   0x16 0x53 0x22 0x0e 0x8d                   .S"..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 70 BolusWizard 2013-01-14T02:19:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 67,
 '_byte[7]': 0,
 'bg': 428,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.7,
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
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2013-01-14T02:19:31)
    0000   0x1f 0x53 0x02 0x0e 0x0d                   .S...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x43 0x00 0x00    .Q.-jC..
    0008   0x00 0x00 0x00 0x43 0x7d                   ...C}
    decimal
              0   81   13   45  106   67    0    0
              0    0    0   67  125
    HOUR BITS: [0, 1, 0]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 255, 'amount': 1.9, 'curve': 4},
 {'age': 9, 'amount': 2.1, 'curve': 20},
 {'age': 29, 'amount': 3.2, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0xff 0x04 0x54 0x09 0x14    \.L..T..
    0008   0x80 0x1d 0x14                             ...
    decimal
             92   11   76  255    4   84    9   20
            128   29   20
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-01-14T02:19:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.0, 'programmed': 7.0}
```
    op hex (4)
    0000   0x01 0x46 0x46 0x00                        .FF.
    decimal
              1   70   70    0
    datetime (2013-01-14T02:19:31)
    0000   0x1f 0x53 0x42 0x0e 0x0d                   .SB..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 73 TempBasal 2013-01-14T03:57:21 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.0}
```
    op hex (2)
    0000   0x33 0x28                                  3(
    decimal
             51   40
    datetime (2013-01-14T03:57:21)
    0000   0x15 0x79 0x03 0x0e 0x0d                   .y...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 1]
#### RECORD 74 TempBasalDuration 2013-01-14T03:57:21 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-01-14T03:57:21)
    0000   0x15 0x79 0x03 0x0e 0x0d                   .y...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 75 CalBGForPH 2013-01-14T03:58:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 455}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-01-14T03:58:01)
    0000   0x01 0x7a 0x23 0x0e 0x8d                   .z#..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 76 BolusWizard 2013-01-14T03:58:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 73,
 '_byte[7]': 0,
 'bg': 455,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 4.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc7                                  [.
    decimal
             91  199
    datetime (2013-01-14T03:58:49)
    0000   0x31 0x7a 0x03 0x0e 0x0d                   1z...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x49 0x00 0x00    .Q.-jI..
    0008   0x00 0x28 0x00 0x21 0x7d                   .(.!}
    decimal
              0   81   13   45  106   73    0    0
              0   40    0   33  125
    HOUR BITS: [0, 1, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 0.3, 'curve': 4},
 {'age': 104, 'amount': 0.3, 'curve': 5},
 {'age': 98, 'amount': 1.9, 'curve': 20},
 {'age': 108, 'amount': 2.1, 'curve': 20},
 {'age': 128, 'amount': 3.2, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x0c 0x5e 0x04 0x0c 0x68 0x05    \..^..h.
    0008   0x4c 0x62 0x14 0x54 0x6c 0x14 0x80 0x80    Lb.Tl...
    0010   0x14                                       .
    decimal
             92   17   12   94    4   12  104    5
             76   98   20   84  108   20  128  128
             20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2013-01-14T03:58:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-01-14T03:58:49)
    0000   0x31 0x7a 0x43 0x0e 0x0d                   1zC..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 79 CalBGForPH 2013-01-14T05:42:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 372}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-01-14T05:42:25)
    0000   0x19 0x6a 0x25 0x0e 0x8d                   .j%..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 80 TempBasal 2013-01-14T05:43:56 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.0}
```
    op hex (2)
    0000   0x33 0x28                                  3(
    decimal
             51   40
    datetime (2013-01-14T05:43:56)
    0000   0x38 0x6b 0x05 0x0e 0x0d                   8k...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 1]
#### RECORD 81 TempBasalDuration 2013-01-14T05:43:56 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-01-14T05:43:56)
    0000   0x38 0x6b 0x05 0x0e 0x0d                   8k...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 82 CalBGForPH 2013-01-14T05:44:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 372}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-01-14T05:44:25)
    0000   0x19 0x6c 0x25 0x0e 0x8d                   .l%..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 83 Base unknown head[2], body[0] op[0xf6]

    op hex (2)
    0000   0xf6 0xb1                                  ..
    decimal
            246  177
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-3.data: 84 records`
