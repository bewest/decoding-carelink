## START logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x51 0xc8                                  Q.
##### DEBUG DECIMAL
             81  200
#### RECORD 0 MResultTotals 2014-03-11T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbf                   .....
    decimal
              7    0    0    4  191
    datetime (2014-03-11T00:00:00)
    0000   0x2a 0x8e                                  *.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 Sara6E 2014-03-11T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-11T00:00:00)
    0000   0x2a 0x8e                                  *.
    body (49)
    hex
    0000   0x05 0x00 0xc5 0x6a 0xa9 0x07 0x00 0x00    ...j....
    0008   0x04 0xbf 0x01 0xa7 0x23 0x03 0x18 0x41    ....#..A
    0010   0x00 0x78 0x01 0x3c 0x01 0x68 0x00 0x68    .x.<.h.h
    0018   0x00 0x0c 0x02 0x05 0x01 0x01 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x81    ........
    0028   0x22 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ".......
    0030   0x00                                       .
    decimal
              5    0  197  106  169    7    0    0
              4  191    1  167   35    3   24   65
              0  120    1   60    1  104    0  104
              0   12    2    5    1    1    4    0
              0    0    0    0    0    0    0  129
             34    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 2 TempBasal 2014-03-11T00:05:00 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-11T00:05:00)
    0000   0x00 0xc5 0x00 0x0b 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 3 TempBasalDuration 2014-03-11T00:05:00 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-11T00:05:00)
    0000   0x00 0xc5 0x00 0x0b 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BasalProfileStart 2014-03-11T01:05:01 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-11T01:05:01)
    0000   0x01 0xc5 0x01 0x0b 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BasalProfileStart 2014-03-11T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-11T02:00:00)
    0000   0x00 0xc0 0x02 0x0b 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 BasalProfileStart 2014-03-11T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-11T04:00:00)
    0000   0x00 0xc0 0x04 0x0b 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 7 BasalProfileStart 2014-03-11T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-11T06:00:00)
    0000   0x00 0xc0 0x06 0x0b 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 8 BasalProfileStart 2014-03-11T08:23:04 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-11T08:23:04)
    0000   0x04 0xd7 0x08 0x0b 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 9 Prime 2014-03-11T08:22:54 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2014-03-11T08:22:54)
    0000   0x36 0xd6 0x08 0x0b 0x0e                   6....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 BasalProfileStart 2014-03-11T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-11T10:30:00)
    0000   0x00 0xde 0x0a 0x0b 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 11 CalBGForPH 2014-03-11T12:50:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2014-03-11T12:50:18)
    0000   0x12 0xf2 0x2c 0x6b 0x0e                   ..,k.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2014-03-11T12:50:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-03-11T12:50:18)
    0000   0x12 0xf2 0x6c 0x6b 0x0e                   ..lk.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2014-03-11T12:51:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 131,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2014-03-11T12:51:33)
    0000   0x21 0xf3 0x0c 0x0b 0x0e                   !....
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x32 0x50 0x18 0x00    .P.x2P..
    0008   0x30 0x00 0x00 0x00 0x00 0x48 0x64         0....Hd
    decimal
             15   80    0  120   50   80   24    0
             48    0    0    0    0   72  100
    HOUR BITS: [1, 1, 1]
#### RECORD 14 Bolus 2014-03-11T12:51:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2014-03-11T12:51:33)
    0000   0x21 0xf3 0x4c 0x0b 0x0e                   !.L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 15 BolusWizard 2014-03-11T13:00:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 131,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 7.2,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2014-03-11T13:00:56)
    0000   0x38 0xc0 0x0d 0x6b 0x0e                   8..k.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x32 0x50 0x18 0x00    .P.x2P..
    0008   0x50 0x00 0x00 0x48 0x00 0x50 0x64         P..H.Pd
    decimal
             25   80    0  120   50   80   24    0
             80    0    0   72    0   80  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 1.1, 'curve': 128},
 {'age': 18, 'amount': 0.7, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x08 0x80 0x1c 0x12 0x80    \.,.....
    decimal
             92    8   44    8  128   28   18  128
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2014-03-11T13:00:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x48 0x00    ..P.P.H.
    decimal
              1    0   80    0   80    0   72    0
    datetime (2014-03-11T13:00:56)
    0000   0x38 0xc0 0x4d 0x6b 0x0e                   8.Mk.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 CalBGForPH 2014-03-11T16:18:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2014-03-11T16:18:34)
    0000   0x22 0xd2 0x30 0x6b 0x0e                   ".0k.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 19 Ian3F 2014-03-11T16:18:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-03-11T16:18:34)
    0000   0x22 0xd2 0x70 0x6b 0x0e                   ".pk.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2014-03-11T16:24:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 67,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 24.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x43                                  [C
    decimal
             91   67
    datetime (2014-03-11T16:24:19)
    0000   0x13 0xd8 0x10 0x6b 0x0e                   ...k.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x32 0x50 0xf4 0x00    .P.x2P..
    0008   0x30 0xf8 0x00 0x00 0x00 0x24 0x64         0....$d
    decimal
             15   80    0  120   50   80  244    0
             48  248    0    0    0   36  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 202, 'amount': 0.4, 'curve': 128},
 {'age': 212, 'amount': 2.7, 'curve': 128},
 {'age': 222, 'amount': 0.7, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0xca 0x80 0x6c 0xd4 0x80    \....l..
    0008   0x1c 0xde 0x80                             ...
    decimal
             92   11   16  202  128  108  212  128
             28  222  128
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2014-03-11T16:24:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x00 0x00    ..$.$...
    decimal
              1    0   36    0   36    0    0    0
    datetime (2014-03-11T16:24:19)
    0000   0x13 0xd8 0x50 0x6b 0x0e                   ..Pk.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2014-03-11T16:55:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-11T16:55:38)
    0000   0x26 0xf7 0x10 0x6b 0x0e                   &..k.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             22   80    0  120   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 0.9, 'curve': 128},
 {'age': 233, 'amount': 0.4, 'curve': 128},
 {'age': 243, 'amount': 2.7, 'curve': 128},
 {'age': 253, 'amount': 0.7, 'curve': 128}]
```
    op hex (14)
    0000   0x5c 0x0e 0x24 0x21 0x80 0x10 0xe9 0x80    \.$!....
    0008   0x6c 0xf3 0x80 0x1c 0xfd 0x80              l.....
    decimal
             92   14   36   33  128   16  233  128
            108  243  128   28  253  128
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2014-03-11T16:55:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x1c 0x00    ..H.H...
    decimal
              1    0   72    0   72    0   28    0
    datetime (2014-03-11T16:55:38)
    0000   0x26 0xf7 0x50 0x6b 0x0e                   &.Pk.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 Bolus 2014-03-11T17:01:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x64 0x00    ..(.(.d.
    decimal
              1    0   40    0   40    0  100    0
    datetime (2014-03-11T17:01:09)
    0000   0x09 0xc1 0x51 0x0b 0x0e                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 CalBGForPH 2014-03-11T18:26:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2014-03-11T18:26:32)
    0000   0x20 0xda 0x32 0x0b 0x0e                    .2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 BolusWizard 2014-03-11T18:26:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 6.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2014-03-11T18:26:35)
    0000   0x23 0xda 0x12 0x6b 0x0e                   #..k.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x44 0x00    .P.x2PD.
    0008   0x00 0x00 0x00 0x14 0x00 0x30 0x64         .....0d
    decimal
              0   80    0  120   50   80   68    0
              0    0    0   20    0   48  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 2.8, 'curve': 128},
 {'age': 124, 'amount': 0.9, 'curve': 128},
 {'age': 68, 'amount': 0.4, 'curve': 144},
 {'age': 78, 'amount': 2.7, 'curve': 144},
 {'age': 88, 'amount': 0.7, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x70 0x5e 0x80 0x24 0x7c 0x80    \.p^.$|.
    0008   0x10 0x44 0x90 0x6c 0x4e 0x90 0x1c 0x58    .D.lN..X
    0010   0x90                                       .
    decimal
             92   17  112   94  128   36  124  128
             16   68  144  108   78  144   28   88
            144
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2014-03-11T18:26:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x14 0x00    ..0.0...
    decimal
              1    0   48    0   48    0   20    0
    datetime (2014-03-11T18:26:35)
    0000   0x23 0xda 0x52 0x6b 0x0e                   #.Rk.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2014-03-11T18:29:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 6.4,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 6.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2014-03-11T18:29:27)
    0000   0x1b 0xdd 0x12 0x6b 0x0e                   ...k.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x32 0x50 0x44 0x00    .P.x2PD.
    0008   0x64 0x00 0x00 0x40 0x00 0x68 0x64         d..@.hd
    decimal
             30   80    0  120   50   80   68    0
            100    0    0   64    0  104  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 1.2, 'curve': 128},
 {'age': 97, 'amount': 2.8, 'curve': 128},
 {'age': 127, 'amount': 0.9, 'curve': 128},
 {'age': 71, 'amount': 0.4, 'curve': 144},
 {'age': 81, 'amount': 2.7, 'curve': 144},
 {'age': 91, 'amount': 0.7, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0x30 0x07 0x80 0x70 0x61 0x80    \.0..pa.
    0008   0x24 0x7f 0x80 0x10 0x47 0x90 0x6c 0x51    $...G.lQ
    0010   0x90 0x1c 0x5b 0x90                        ..[.
    decimal
             92   20   48    7  128  112   97  128
             36  127  128   16   71  144  108   81
            144   28   91  144
    datetime (unknown)

    body (0)

#### RECORD 33 LowReservoir 2014-03-11T18:29:39 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-03-11T18:29:39)
    0000   0x27 0xdd 0x12 0x0b 0x0e                   '....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 34 Bolus 2014-03-11T18:29:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x40 0x00    ..h.h.@.
    decimal
              1    0  104    0  104    0   64    0
    datetime (2014-03-11T18:29:27)
    0000   0x1b 0xdd 0x52 0x6b 0x0e                   ..Rk.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2014-03-11T18:33:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 16.4,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 6.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2014-03-11T18:33:51)
    0000   0x33 0xe1 0x12 0x6b 0x0e                   3..k.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x32 0x50 0x44 0x00    .P.x2PD.
    0008   0x64 0x00 0x00 0xa4 0x00 0x64 0x64         d....dd
    decimal
             30   80    0  120   50   80   68    0
            100    0    0  164    0  100  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 3.8, 'curve': 128},
 {'age': 101, 'amount': 2.8, 'curve': 128},
 {'age': 131, 'amount': 0.9, 'curve': 128},
 {'age': 75, 'amount': 0.4, 'curve': 144},
 {'age': 85, 'amount': 2.7, 'curve': 144},
 {'age': 95, 'amount': 0.7, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0x98 0x0b 0x80 0x70 0x65 0x80    \....pe.
    0008   0x24 0x83 0x80 0x10 0x4b 0x90 0x6c 0x55    $...K.lU
    0010   0x90 0x1c 0x5f 0x90                        .._.
    decimal
             92   20  152   11  128  112  101  128
             36  131  128   16   75  144  108   85
            144   28   95  144
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2014-03-11T18:33:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xa4 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  164    0
    datetime (2014-03-11T18:33:51)
    0000   0x33 0xe1 0x52 0x6b 0x0e                   3.Rk.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2014-03-11T18:51:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 1,
 'bg': 0,
 'bg_target_high': 1,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 115,
 'carb_ratio': 0,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-11T18:51:11)
    0000   0x0b 0xf3 0x12 0x6b 0x0e                   ...k.
    body (15)
    hex
    0000   0x73 0x50 0x00 0x78 0x32 0x50 0x00 0x01    sP.x2P..
    0008   0x7c 0x00 0x00 0x00 0x01 0x7c 0x64         |....|d
    decimal
            115   80    0  120   50   80    0    1
            124    0    0    0    1  124  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 19, 'amount': 2.5, 'curve': 128},
 {'age': 29, 'amount': 3.8, 'curve': 128},
 {'age': 119, 'amount': 2.8, 'curve': 128},
 {'age': 149, 'amount': 0.9, 'curve': 128},
 {'age': 93, 'amount': 0.4, 'curve': 144},
 {'age': 103, 'amount': 2.7, 'curve': 144},
 {'age': 113, 'amount': 0.7, 'curve': 144}]
```
    op hex (23)
    0000   0x5c 0x17 0x64 0x13 0x80 0x98 0x1d 0x80    \.d.....
    0008   0x70 0x77 0x80 0x24 0x95 0x80 0x10 0x5d    pw.$...]
    0010   0x90 0x6c 0x67 0x90 0x1c 0x71 0x90         .lg..q.
    decimal
             92   23  100   19  128  152   29  128
            112  119  128   36  149  128   16   93
            144  108  103  144   28  113  144
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2014-03-11T18:56:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xe4 0x02    ..<.<...
    decimal
              1    0   60    0   60    0  228    2
    datetime (2014-03-11T18:56:11)
    0000   0x0b 0xf8 0xb2 0x6b 0x0e                   ...k.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 LowReservoir 2014-03-11T18:54:13 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-03-11T18:54:13)
    0000   0x0d 0xf6 0x12 0x0b 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 Bolus 2014-03-11T18:51:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x40 0x01 0x40 0x00 0xe4 0x00    ..@.@...
    decimal
              1    1   64    1   64    0  228    0
    datetime (2014-03-11T18:51:11)
    0000   0x0b 0xf3 0x92 0x6b 0x0e                   ...k.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 CalBGForPH 2014-03-11T19:09:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2014-03-11T19:09:00)
    0000   0x00 0xc9 0x33 0x6b 0x0e                   ..3k.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 44 Ian3F 2014-03-11T19:09:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2014-03-11T19:09:00)
    0000   0x00 0xc9 0xd3 0x6b 0x0e                   ...k.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 45 CalBGForPH 2014-03-11T21:31:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 62}
```
    op hex (2)
    0000   0x0a 0x3e                                  .>
    decimal
             10   62
    datetime (2014-03-11T21:31:26)
    0000   0x1a 0xdf 0x35 0x6b 0x0e                   ..5k.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 46 Ian3F 2014-03-11T21:31:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-03-11T21:31:26)
    0000   0x1a 0xdf 0xd5 0x6b 0x0e                   ...k.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 47 PumpSuspend 2014-03-11T21:32:10 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-11T21:32:10)
    0000   0x0a 0xe0 0x15 0x0b 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 CalBGForPH 2014-03-11T22:14:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2014-03-11T22:14:24)
    0000   0x18 0xce 0x36 0x6b 0x0e                   ..6k.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 Ian3F 2014-03-11T22:14:24 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2014-03-11T22:14:24)
    0000   0x18 0xce 0x96 0x6b 0x0e                   ...k.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 50 CalBGForPH 2014-03-11T23:31:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2014-03-11T23:31:48)
    0000   0x30 0xdf 0x37 0x6b 0x0e                   0.7k.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 Ian3F 2014-03-11T23:31:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2014-03-11T23:31:48)
    0000   0x30 0xdf 0xb7 0x6b 0x0e                   0..k.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 BasalProfileStart 2014-03-11T23:31:50 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-11T23:31:50)
    0000   0x32 0xdf 0x17 0x0b 0x0e                   2....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 53 PumpResume 2014-03-11T23:31:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-11T23:31:50)
    0000   0x32 0xdf 0x17 0x0b 0x0e                   2....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 54 BolusWizard 2014-03-11T23:31:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2014-03-11T23:31:54)
    0000   0x36 0xdf 0x17 0x0b 0x0e                   6....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x0c 0x00    .P.n7P..
    0008   0x00 0x00 0x00 0x00 0x00 0x0c 0x64         ......d
    decimal
              0   80    0  110   55   80   12    0
              0    0    0    0    0   12  100
    HOUR BITS: [1, 1, 0]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 219, 'amount': 0.1, 'curve': 128},
 {'age': 229, 'amount': 0.25, 'curve': 128},
 {'age': 239, 'amount': 0.25, 'curve': 128},
 {'age': 249, 'amount': 0.25, 'curve': 128},
 {'age': 3, 'amount': 0.25, 'curve': 144},
 {'age': 13, 'amount': 0.25, 'curve': 144},
 {'age': 23, 'amount': 0.0, 'curve': 145},
 {'age': 33, 'amount': 1.75, 'curve': 144},
 {'age': 43, 'amount': 2.5, 'curve': 144},
 {'age': 53, 'amount': 3.8, 'curve': 144},
 {'age': 143, 'amount': 2.8, 'curve': 144},
 {'age': 173, 'amount': 0.9, 'curve': 144}]
```
    op hex (38)
    0000   0x5c 0x26 0x04 0xdb 0x80 0x0a 0xe5 0x80    \&......
    0008   0x0a 0xef 0x80 0x0a 0xf9 0x80 0x0a 0x03    ........
    0010   0x90 0x0a 0x0d 0x90 0x00 0x17 0x91 0x46    .......F
    0018   0x21 0x90 0x64 0x2b 0x90 0x98 0x35 0x90    !.d+..5.
    0020   0x70 0x8f 0x90 0x24 0xad 0x90              p..$..
    decimal
             92   38    4  219  128   10  229  128
             10  239  128   10  249  128   10    3
            144   10   13  144    0   23  145   70
             33  144  100   43  144  152   53  144
            112  143  144   36  173  144
    datetime (unknown)

    body (0)

#### RECORD 56 BolusWizard 2014-03-11T23:31:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2014-03-11T23:31:56)
    0000   0x38 0xdf 0x17 0x0b 0x0e                   8....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x0c 0x00    .P.n7P..
    0008   0x00 0x00 0x00 0x00 0x00 0x0c 0x64         ......d
    decimal
              0   80    0  110   55   80   12    0
              0    0    0    0    0   12  100
    HOUR BITS: [1, 1, 0]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 219, 'amount': 0.1, 'curve': 128},
 {'age': 229, 'amount': 0.25, 'curve': 128},
 {'age': 239, 'amount': 0.25, 'curve': 128},
 {'age': 249, 'amount': 0.25, 'curve': 128},
 {'age': 3, 'amount': 0.25, 'curve': 144},
 {'age': 13, 'amount': 0.25, 'curve': 144},
 {'age': 23, 'amount': 0.0, 'curve': 145},
 {'age': 33, 'amount': 1.75, 'curve': 144},
 {'age': 43, 'amount': 2.5, 'curve': 144},
 {'age': 53, 'amount': 3.8, 'curve': 144},
 {'age': 143, 'amount': 2.8, 'curve': 144},
 {'age': 173, 'amount': 0.9, 'curve': 144}]
```
    op hex (38)
    0000   0x5c 0x26 0x04 0xdb 0x80 0x0a 0xe5 0x80    \&......
    0008   0x0a 0xef 0x80 0x0a 0xf9 0x80 0x0a 0x03    ........
    0010   0x90 0x0a 0x0d 0x90 0x00 0x17 0x91 0x46    .......F
    0018   0x21 0x90 0x64 0x2b 0x90 0x98 0x35 0x90    !.d+..5.
    0020   0x70 0x8f 0x90 0x24 0xad 0x90              p..$..
    decimal
             92   38    4  219  128   10  229  128
             10  239  128   10  249  128   10    3
            144   10   13  144    0   23  145   70
             33  144  100   43  144  152   53  144
            112  143  144   36  173  144
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2014-03-11T23:31:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x0c 0x00 0x0c 0x00 0x00 0x00    ........
    decimal
              1    0   12    0   12    0    0    0
    datetime (2014-03-11T23:31:56)
    0000   0x38 0xdf 0x57 0x0b 0x0e                   8.W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 BasalProfileStart 2014-03-12T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-12T00:00:00)
    0000   0x00 0xc0 0x00 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 60 MResultTotals 2014-03-12T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x5a                   ....Z
    decimal
              7    0    0    5   90
    datetime (2014-03-12T00:00:00)
    0000   0x2b 0x8e                                  +.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 61 Sara6E 2014-03-12T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-12T00:00:00)
    0000   0x2b 0x8e                                  +.
    body (49)
    hex
    0000   0x05 0x00 0x75 0x3e 0xb6 0x07 0x00 0x00    ..u>....
    0008   0x05 0x5a 0x01 0xaa 0x1f 0x03 0xb0 0x45    .Z.....E
    0010   0x00 0xfc 0x02 0x9c 0x00 0x3c 0x00 0xb0    .....<..
    0018   0x00 0x28 0x05 0x02 0x02 0x01 0x00 0x00    .(......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xba    ........
    0028   0xba 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  117   62  182    7    0    0
              5   90    1  170   31    3  176   69
              0  252    2  156    0   60    0  176
              0   40    5    2    2    1    0    0
              0    0    0    0    0    0    0  186
            186    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 62 CalBGForPH 2014-03-12T00:35:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 178}
```
    op hex (2)
    0000   0x0a 0xb2                                  ..
    decimal
             10  178
    datetime (2014-03-12T00:35:18)
    0000   0x12 0xe3 0x20 0x6c 0x0e                   .. l.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 Ian3F 2014-03-12T00:35:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2014-03-12T00:35:18)
    0000   0x12 0xe3 0x40 0x6c 0x0e                   ..@l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 CalBGForPH 2014-03-12T00:35:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2014-03-12T00:35:56)
    0000   0x38 0xe3 0x20 0x6c 0x0e                   8. l.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 Ian3F 2014-03-12T00:35:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2014-03-12T00:35:56)
    0000   0x38 0xe3 0x80 0x6c 0x0e                   8..l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 66 BolusWizard 2014-03-12T00:36:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 188,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 6.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2014-03-12T00:36:50)
    0000   0x32 0xe4 0x00 0x0c 0x0e                   2....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x40 0x00    .P.n7P@.
    0008   0x00 0x00 0x00 0x08 0x00 0x38 0x64         .....8d
    decimal
              0   80    0  110   55   80   64    0
              0    0    0    8    0   56  100
    HOUR BITS: [1, 1, 1]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 0.25, 'curve': 128},
 {'age': 74, 'amount': 0.05, 'curve': 128},
 {'age': 28, 'amount': 0.1, 'curve': 144},
 {'age': 38, 'amount': 0.25, 'curve': 144},
 {'age': 48, 'amount': 0.25, 'curve': 144},
 {'age': 58, 'amount': 0.25, 'curve': 144},
 {'age': 68, 'amount': 0.25, 'curve': 144},
 {'age': 78, 'amount': 0.25, 'curve': 144},
 {'age': 88, 'amount': 0.0, 'curve': 145},
 {'age': 98, 'amount': 1.75, 'curve': 144},
 {'age': 108, 'amount': 2.5, 'curve': 144},
 {'age': 118, 'amount': 3.8, 'curve': 144},
 {'age': 208, 'amount': 2.8, 'curve': 144}]
```
    op hex (41)
    0000   0x5c 0x29 0x0a 0x40 0x80 0x02 0x4a 0x80    \).@..J.
    0008   0x04 0x1c 0x90 0x0a 0x26 0x90 0x0a 0x30    ....&..0
    0010   0x90 0x0a 0x3a 0x90 0x0a 0x44 0x90 0x0a    ..:..D..
    0018   0x4e 0x90 0x00 0x58 0x91 0x46 0x62 0x90    N..X.Fb.
    0020   0x64 0x6c 0x90 0x98 0x76 0x90 0x70 0xd0    dl..v.p.
    0028   0x90                                       .
    decimal
             92   41   10   64  128    2   74  128
              4   28  144   10   38  144   10   48
            144   10   58  144   10   68  144   10
             78  144    0   88  145   70   98  144
            100  108  144  152  118  144  112  208
            144
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-4.data: 68 records`
