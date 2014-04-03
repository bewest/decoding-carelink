## START logs/ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xac 0x62                                  .b
##### DEBUG DECIMAL
            172   98
#### RECORD 0 Sara6E 2014-03-15T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-15T00:00:00)
    0000   0x2e 0x8e                                  ..
    body (49)
    hex
    0000   0x05 0x00 0x64 0x2b 0x80 0x05 0x00 0x00    ..d+....
    0008   0x06 0x66 0x01 0xc2 0x1b 0x04 0xa4 0x49    .f.....I
    0010   0x01 0x4f 0x04 0x30 0x00 0x00 0x00 0x74    .O.0...t
    0018   0x00 0x00 0x09 0x00 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x99    ........
    0028   0x99 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  100   43  128    5    0    0
              6  102    1  194   27    4  164   73
              1   79    4   48    0    0    0  116
              0    0    9    0    1    0    0    0
              0    0    0    0    0    0    0  153
            153    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 BasalProfileStart 2014-03-15T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-15T02:00:00)
    0000   0x00 0xc0 0x02 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BasalProfileStart 2014-03-15T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-15T04:00:00)
    0000   0x00 0xc0 0x04 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BasalProfileStart 2014-03-15T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-15T06:00:00)
    0000   0x00 0xc0 0x06 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2014-03-15T06:52:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2014-03-15T06:52:09)
    0000   0x09 0xf4 0x26 0x6f 0x0e                   ..&o.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 Ian3F 2014-03-15T06:52:09 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1c                                  ?.
    decimal
             63   28
    datetime (2014-03-15T06:52:09)
    0000   0x09 0xf4 0xe6 0x6f 0x0e                   ...o.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2014-03-15T06:52:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 12.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2014-03-15T06:52:20)
    0000   0x14 0xf4 0x06 0x0f 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x80 0x00    .P.n(P..
    0008   0x00 0x00 0x00 0x00 0x00 0x80 0x64         ......d
    decimal
              0   80    0  110   40   80  128    0
              0    0    0    0    0  128  100
    HOUR BITS: [1, 1, 1]
#### RECORD 7 Bolus 2014-03-15T06:52:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x00 0x00    ........
    decimal
              1    0  128    0  128    0    0    0
    datetime (2014-03-15T06:52:20)
    0000   0x14 0xf4 0x46 0x0f 0x0e                   ..F..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BolusWizard 2014-03-15T08:10:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-15T08:10:17)
    0000   0x11 0xca 0x08 0x6f 0x0e                   ...o.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    .P.n(P..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x64         4....4d
    decimal
             15   80    0  110   40   80    0    0
             52    0    0    0    0   52  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 78, 'amount': 3.2, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x80 0x4e 0x80                   \..N.
    decimal
             92    5  128   78  128
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2014-03-15T08:10:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x24 0x00    ..4.4.$.
    decimal
              1    0   52    0   52    0   36    0
    datetime (2014-03-15T08:10:17)
    0000   0x11 0xca 0x48 0x6f 0x0e                   ..Ho.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 11 BasalProfileStart 2014-03-15T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T10:30:00)
    0000   0x00 0xde 0x0a 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 12 BolusWizard 2014-03-15T10:51:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-15T10:51:17)
    0000   0x11 0xf3 0x0a 0x6f 0x0e                   ...o.
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    .P.n(P..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x64         (....(d
    decimal
             12   80    0  110   40   80    0    0
             40    0    0    0    0   40  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 169, 'amount': 1.3, 'curve': 128},
 {'age': 239, 'amount': 3.2, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0xa9 0x80 0x80 0xef 0x80    \.4.....
    decimal
             92    8   52  169  128  128  239  128
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2014-03-15T10:51:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2014-03-15T10:51:17)
    0000   0x11 0xf3 0x4a 0x6f 0x0e                   ..Jo.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 15 BolusWizard 2014-03-15T12:48:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 55,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 180}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-15T12:48:06)
    0000   0x06 0xf0 0x0c 0x6f 0x0e                   ...o.
    body (15)
    hex
    0000   0x37 0x50 0x00 0x78 0x32 0x50 0x00 0x00    7P.x2P..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x64         ......d
    decimal
             55   80    0  120   50   80    0    0
            180    0    0    0    0  180  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 1.0, 'curve': 128},
 {'age': 30, 'amount': 1.3, 'curve': 144},
 {'age': 100, 'amount': 3.2, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x7e 0x80 0x34 0x1e 0x90    \.(~.4..
    0008   0x80 0x64 0x90                             .d.
    decimal
             92   11   40  126  128   52   30  144
            128  100  144
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2014-03-15T12:48:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 18.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x00 0x00    ........
    decimal
              1    0  180    0  180    0    0    0
    datetime (2014-03-15T12:48:06)
    0000   0x06 0xf0 0x4c 0x6f 0x0e                   ..Lo.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 BolusWizard 2014-03-15T14:04:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-15T14:04:43)
    0000   0x2b 0xc4 0x0e 0x6f 0x0e                   +..o.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x64         0....0d
    decimal
             15   80    0  120   50   80    0    0
             48    0    0    0    0   48  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 4.5, 'curve': 128},
 {'age': 202, 'amount': 1.0, 'curve': 128},
 {'age': 106, 'amount': 1.3, 'curve': 144},
 {'age': 176, 'amount': 3.2, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0xb4 0x52 0x80 0x28 0xca 0x80    \..R.(..
    0008   0x34 0x6a 0x90 0x80 0xb0 0x90              4j....
    decimal
             92   14  180   82  128   40  202  128
             52  106  144  128  176  144
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2014-03-15T14:04:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x2c 0x00    ..0.0.,.
    decimal
              1    0   48    0   48    0   44    0
    datetime (2014-03-15T14:04:43)
    0000   0x2b 0xc4 0x4e 0x6f 0x0e                   +.No.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 CalBGForPH 2014-03-15T15:54:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 251}
```
    op hex (2)
    0000   0x0a 0xfb                                  ..
    decimal
             10  251
    datetime (2014-03-15T15:54:55)
    0000   0x37 0xf6 0x2f 0x0f 0x0e                   7./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 22 BolusWizard 2014-03-15T15:55:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 251,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.4,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 12.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0xfb                                  [.
    decimal
             91  251
    datetime (2014-03-15T15:55:03)
    0000   0x03 0xf7 0x0f 0x6f 0x0e                   ...o.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x78 0x32 0x50 0x78 0x00    (P.x2Px.
    0008   0x84 0x00 0x00 0x04 0x00 0xf8 0x64         ......d
    decimal
             40   80    0  120   50   80  120    0
            132    0    0    4    0  248  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 113, 'amount': 1.2, 'curve': 128},
 {'age': 193, 'amount': 4.5, 'curve': 128},
 {'age': 57, 'amount': 1.0, 'curve': 144},
 {'age': 217, 'amount': 1.3, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x30 0x71 0x80 0xb4 0xc1 0x80    \.0q....
    0008   0x28 0x39 0x90 0x34 0xd9 0x90              (9.4..
    decimal
             92   14   48  113  128  180  193  128
             40   57  144   52  217  144
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2014-03-15T15:55:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 24.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xf8 0x00 0xf8 0x00 0x04 0x00    ........
    decimal
              1    0  248    0  248    0    4    0
    datetime (2014-03-15T15:55:03)
    0000   0x03 0xf7 0x4f 0x6f 0x0e                   ..Oo.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 TempBasal 2014-03-15T18:14:18 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-15T18:14:18)
    0000   0x12 0xce 0x12 0x0f 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 26 TempBasalDuration 2014-03-15T18:14:18 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-15T18:14:18)
    0000   0x12 0xce 0x12 0x0f 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 CalBGForPH 2014-03-15T18:15:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 51}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2014-03-15T18:15:01)
    0000   0x01 0xcf 0x32 0x6f 0x0e                   ..2o.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 Ian3F 2014-03-15T18:15:01 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2014-03-15T18:15:01)
    0000   0x01 0xcf 0x72 0x6f 0x0e                   ..ro.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 BasalProfileStart 2014-03-15T19:14:18 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T19:14:18)
    0000   0x12 0xce 0x13 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 30 PumpSuspend 2014-03-15T19:56:52 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-15T19:56:52)
    0000   0x34 0xf8 0x13 0x4f 0x0e                   4..O.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 31 PumpResume 2014-03-15T19:57:51 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-15T19:57:51)
    0000   0x33 0xf9 0x13 0x4f 0x0e                   3..O.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 32 BasalProfileStart 2014-03-15T19:57:51 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T19:57:51)
    0000   0x33 0xf9 0x13 0x0f 0x0e                   3....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 33 PumpSuspend 2014-03-15T19:58:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-15T19:58:30)
    0000   0x1e 0xfa 0x13 0x4f 0x0e                   ...O.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 34 PumpResume 2014-03-15T19:59:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-15T19:59:29)
    0000   0x1d 0xfb 0x13 0x4f 0x0e                   ...O.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 35 BasalProfileStart 2014-03-15T19:59:29 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T19:59:29)
    0000   0x1d 0xfb 0x13 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 36 PumpSuspend 2014-03-15T20:00:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-15T20:00:01)
    0000   0x01 0xc0 0x14 0x4f 0x0e                   ...O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 37 PumpResume 2014-03-15T20:01:00 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-15T20:01:00)
    0000   0x00 0xc1 0x14 0x4f 0x0e                   ...O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 38 BasalProfileStart 2014-03-15T20:01:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T20:01:00)
    0000   0x00 0xc1 0x14 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 39 Battery 2014-03-15T20:01:22 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2014-03-15T20:01:22)
    0000   0x16 0xc1 0x14 0x0f 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 40 Battery 2014-03-15T20:02:47 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-03-15T20:02:47)
    0000   0x2f 0xc2 0x14 0x0f 0x0e                   /....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 41 BasalProfileStart 2014-03-15T20:02:48 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T20:02:48)
    0000   0x30 0xc2 0x14 0x0f 0x0e                   0....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 42 PumpSuspend 2014-03-15T20:03:46 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-15T20:03:46)
    0000   0x2e 0xc3 0x14 0x4f 0x0e                   ...O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 43 PumpResume 2014-03-15T20:04:45 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-15T20:04:45)
    0000   0x2d 0xc4 0x14 0x4f 0x0e                   -..O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 44 BasalProfileStart 2014-03-15T20:04:45 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T20:04:45)
    0000   0x2d 0xc4 0x14 0x0f 0x0e                   -....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 45 PumpSuspend 2014-03-15T20:05:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-15T20:05:38)
    0000   0x26 0xc5 0x14 0x4f 0x0e                   &..O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 46 PumpResume 2014-03-15T20:06:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-15T20:06:37)
    0000   0x25 0xc6 0x14 0x4f 0x0e                   %..O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 47 BasalProfileStart 2014-03-15T20:06:37 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T20:06:37)
    0000   0x25 0xc6 0x14 0x0f 0x0e                   %....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 48 PumpSuspend 2014-03-15T20:09:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-15T20:09:55)
    0000   0x37 0xc9 0x14 0x4f 0x0e                   7..O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 49 PumpResume 2014-03-15T20:11:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-15T20:11:37)
    0000   0x25 0xcb 0x14 0x4f 0x0e                   %..O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 50 BasalProfileStart 2014-03-15T20:11:37 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T20:11:37)
    0000   0x25 0xcb 0x14 0x0f 0x0e                   %....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 51 PumpSuspend 2014-03-15T20:13:27 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-15T20:13:27)
    0000   0x1b 0xcd 0x14 0x4f 0x0e                   ...O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 52 PumpResume 2014-03-15T20:15:10 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-15T20:15:10)
    0000   0x0a 0xcf 0x14 0x4f 0x0e                   ...O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 53 BasalProfileStart 2014-03-15T20:15:10 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-15T20:15:10)
    0000   0x0a 0xcf 0x14 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 54 BolusWizard 2014-03-15T21:35:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-15T21:35:57)
    0000   0x39 0xe3 0x15 0x6f 0x0e                   9..o.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 87, 'amount': 6.2, 'curve': 144},
 {'age': 197, 'amount': 1.2, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0xf8 0x57 0x90 0x30 0xc5 0x90    \..W.0..
    decimal
             92    8  248   87  144   48  197  144
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2014-03-15T21:35:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2014-03-15T21:35:57)
    0000   0x39 0xe3 0x55 0x6f 0x0e                   9.Uo.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2014-03-15T22:25:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-15T22:25:56)
    0000   0x38 0xd9 0x16 0x6f 0x0e                   8..o.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 1.8, 'curve': 128},
 {'age': 137, 'amount': 6.2, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0x35 0x80 0xf8 0x89 0x90    \.H5....
    decimal
             92    8   72   53  128  248  137  144
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2014-03-15T22:25:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x28 0x00    ..H.H.(.
    decimal
              1    0   72    0   72    0   40    0
    datetime (2014-03-15T22:25:56)
    0000   0x38 0xd9 0x56 0x6f 0x0e                   8.Vo.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 BasalProfileStart 2014-03-15T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-15T22:30:00)
    0000   0x00 0xde 0x16 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 61 BolusWizard 2014-03-15T22:40:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-15T22:40:27)
    0000   0x1b 0xe8 0x16 0x6f 0x0e                   ...o.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x6e 0x37 0x50 0x00 0x00    .P.n7P..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x64         X....Xd
    decimal
             25   80    0  110   55   80    0    0
             88    0    0    0    0   88  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 1.8, 'curve': 128},
 {'age': 68, 'amount': 1.8, 'curve': 128},
 {'age': 152, 'amount': 6.2, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x12 0x80 0x48 0x44 0x80    \.H..HD.
    0008   0xf8 0x98 0x90                             ...
    decimal
             92   11   72   18  128   72   68  128
            248  152  144
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2014-03-15T22:40:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x60 0x00    ..X.X.`.
    decimal
              1    0   88    0   88    0   96    0
    datetime (2014-03-15T22:40:27)
    0000   0x1b 0xe8 0x56 0x6f 0x0e                   ..Vo.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 BasalProfileStart 2014-03-16T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-16T00:00:00)
    0000   0x00 0xc0 0x00 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 65 MResultTotals 2014-03-16T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x72                   ....r
    decimal
              7    0    0    5  114
    datetime (2014-03-16T00:00:00)
    0000   0x2f 0x8e                                  /.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 66 Sara6E 2014-03-16T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-16T00:00:00)
    0000   0x2f 0x8e                                  /.
    body (49)
    hex
    0000   0x05 0x00 0xb2 0x33 0xe7 0x03 0x00 0x00    ...3....
    0008   0x05 0x72 0x01 0xd2 0x21 0x03 0xa0 0x43    .r..!..C
    0010   0x00 0xca 0x02 0x28 0x00 0x80 0x00 0xf8    ...(....
    0018   0x00 0x00 0x07 0x01 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xfb    ........
    0028   0xfb 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  178   51  231    3    0    0
              5  114    1  210   33    3  160   67
              0  202    2   40    0  128    0  248
              0    0    7    1    1    0    0    0
              0    0    0    0    0    0    0  251
            251    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 67 BasalProfileStart 2014-03-16T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-16T02:00:00)
    0000   0x00 0xc0 0x02 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 68 BasalProfileStart 2014-03-16T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-16T04:00:00)
    0000   0x00 0xc0 0x04 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 69 BasalProfileStart 2014-03-16T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-16T06:00:00)
    0000   0x00 0xc0 0x06 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 70 BasalProfileStart 2014-03-16T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T10:30:00)
    0000   0x00 0xde 0x0a 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 71 CalBGForPH 2014-03-16T12:54:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2014-03-16T12:54:58)
    0000   0x3a 0xf6 0x2c 0x10 0x0e                   :.,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 BolusWizard 2014-03-16T12:55:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 128,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 70,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 232}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2014-03-16T12:55:06)
    0000   0x06 0xf7 0x0c 0x70 0x0e                   ...p.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x78 0x32 0x50 0x14 0x00    FP.x2P..
    0008   0xe8 0x00 0x00 0x00 0x00 0xfc 0x64         ......d
    decimal
             70   80    0  120   50   80   20    0
            232    0    0    0    0  252  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 Bolus 2014-03-16T12:55:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 25.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xfc 0x00 0xfc 0x00 0x00 0x00    ........
    decimal
              1    0  252    0  252    0    0    0
    datetime (2014-03-16T12:55:06)
    0000   0x06 0xf7 0x4c 0x70 0x0e                   ..Lp.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 74 PumpSuspend 2014-03-16T14:17:54 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T14:17:54)
    0000   0x36 0xd1 0x0e 0x50 0x0e                   6..P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 75 PumpResume 2014-03-16T14:18:52 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T14:18:52)
    0000   0x34 0xd2 0x0e 0x50 0x0e                   4..P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 76 BasalProfileStart 2014-03-16T14:18:52 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T14:18:52)
    0000   0x34 0xd2 0x0e 0x10 0x0e                   4....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 77 PumpSuspend 2014-03-16T15:00:12 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T15:00:12)
    0000   0x0c 0xc0 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 78 PumpResume 2014-03-16T15:05:39 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T15:05:39)
    0000   0x27 0xc5 0x0f 0x50 0x0e                   '..P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 79 BasalProfileStart 2014-03-16T15:05:39 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T15:05:39)
    0000   0x27 0xc5 0x0f 0x10 0x0e                   '....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 80 PumpSuspend 2014-03-16T15:20:02 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T15:20:02)
    0000   0x02 0xd4 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 81 PumpResume 2014-03-16T15:21:16 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T15:21:16)
    0000   0x10 0xd5 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 82 BasalProfileStart 2014-03-16T15:21:16 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T15:21:16)
    0000   0x10 0xd5 0x0f 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 83 PumpSuspend 2014-03-16T15:23:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T15:23:29)
    0000   0x1d 0xd7 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 84 PumpResume 2014-03-16T15:24:28 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T15:24:28)
    0000   0x1c 0xd8 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 85 BasalProfileStart 2014-03-16T15:24:28 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T15:24:28)
    0000   0x1c 0xd8 0x0f 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 86 PumpSuspend 2014-03-16T15:52:41 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T15:52:41)
    0000   0x29 0xf4 0x0f 0x50 0x0e                   )..P.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 87 PumpResume 2014-03-16T15:53:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T15:53:40)
    0000   0x28 0xf5 0x0f 0x50 0x0e                   (..P.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-1.data: 88 records`
