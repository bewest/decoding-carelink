## START logs/ReadHistoryData-page-4.data
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x87 0x8d 0x06 0x10 0xa3 0x41 0x1d    n.....A.
    0008   0x08 0x00 0x00 0x08 0x7e 0x04 0xf6 0x3a    ....~..:
    0010   0x03 0x88 0x2a 0x00 0x92 0x02 0x08 0x01    ..*.....
    0018   0x80 0x00 0x00 0x00 0x00 0x06 0x03 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  135  141    6   16  163   65   29
              8    0    0    8  126    4  246   58
              3  136   42    0  146    2    8    1
            128    0    0    0    0    6    3    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 CalBGForPH 2013-09-08T00:06:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 219}
```
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2013-09-08T00:06:59)
    0000   0xbb 0x46 0x20 0x68 0x0d                   .F h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2013-09-08T00:06:59 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2013-09-08T00:06:59)
    0000   0xbb 0x46 0x60 0x68 0x0d                   .F`h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2013-09-08T00:10:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 11.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-09-08T00:10:08)
    0000   0x88 0x4a 0x00 0x68 0x0d                   .J.h.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x74 0x00    ...n.6t.
    0008   0x00 0x00 0x00 0x00 0x00 0x74 0x36         .....t6
    decimal
              0  144    0  110   23   54  116    0
              0    0    0    0    0  116   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 4.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0x06 0x14                   \....
    decimal
             92    5  168    6   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-09-08T00:10:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2013-09-08T00:10:08)
    0000   0x88 0x4a 0x40 0x68 0x0d                   .J@h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 BasalProfileStart 2013-09-08T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-08T04:00:00)
    0000   0x80 0x40 0x04 0x08 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-09-08T07:59:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2013-09-08T07:59:05)
    0000   0x85 0x7b 0x27 0x68 0x0d                   .{'h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2013-09-08T07:59:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2013-09-08T07:59:05)
    0000   0x85 0x7b 0xa7 0x68 0x0d                   .{.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 Ian50 2013-09-08T07:59:23 head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x00                                  P.
    decimal
             80    0
    datetime (2013-09-08T07:59:23)
    0000   0x97 0x7b 0x07 0x08 0x0d                   .{...
    body (34)
    hex
    0000   0x40 0x01 0x1e 0x00 0x3c 0x14 0x00 0x1e    @...<...
    0008   0x3c 0x24 0x9a 0xc8 0x64 0x27 0x00 0x80    <$..d'..
    0010   0x21 0x41 0x01 0x1e 0x00 0x3c 0x14 0x00    !A...<..
    0018   0x1e 0x3c 0x24 0x9a 0xc8 0x64 0x27 0x00    .<$..d'.
    0020   0x80 0x21                                  .!
    decimal
             64    1   30    0   60   20    0   30
             60   36  154  200  100   39    0  128
             33   65    1   30    0   60   20    0
             30   60   36  154  200  100   39    0
            128   33
    HOUR BITS: [0, 1, 1]
#### RECORD 10 BolusWizard 2013-09-08T07:59:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 87,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x57                                  [W
    decimal
             91   87
    datetime (2013-09-08T07:59:42)
    0000   0xaa 0x7b 0x07 0x68 0x0d                   .{.h.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x38 0x00    ...n.68.
    0008   0x00 0x00 0x00 0x00 0x00 0x38 0x36         .....86
    decimal
              0  144    0  110   23   54   56    0
              0    0    0    0    0   56   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 215, 'amount': 2.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0xd7 0x14                   \.t..
    decimal
             92    5  116  215   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-09-08T07:59:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-09-08T07:59:42)
    0000   0xaa 0x7b 0x47 0x68 0x0d                   .{Gh.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2013-09-08T09:01:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-08T09:01:06)
    0000   0x86 0x41 0x09 0x68 0x0d                   .A.h.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 63, 'amount': 1.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0x3f 0x04                   \.8?.
    decimal
             92    5   56   63    4
    datetime (unknown)

    body (0)

#### RECORD 15 Ian69 2013-09-08T09:01:06 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-08T09:01:06)
    0000   0x86 0x41 0x09 0x08 0x0d                   .A...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 1, 0]
#### RECORD 16 Bolus 2013-09-08T09:01:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x30 0x00    ..d.d.0.
    decimal
              1    0  100    0  100    0   48    0
    datetime (2013-09-08T09:01:06)
    0000   0x86 0x41 0x49 0x68 0x0d                   .AIh.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 BasalProfileStart 2013-09-08T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-08T09:30:00)
    0000   0x80 0x5e 0x09 0x08 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 18 Ian0B 2013-09-08T09:59:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2013-09-08T09:59:07)
    0000   0x87 0x7b 0x49 0xa8 0x0d                   .{I..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 19 CalBGForPH 2013-09-08T09:59:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2013-09-08T09:59:55)
    0000   0xb7 0x7b 0x29 0x68 0x0d                   .{)h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 Ian3F 2013-09-08T09:59:55 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2013-09-08T09:59:55)
    0000   0xb7 0x7b 0xa9 0x68 0x0d                   .{.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 BasalProfileStart 2013-09-08T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T13:00:00)
    0000   0x80 0x40 0x0d 0x08 0x0d                   .@...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 22 CalBGForPH 2013-09-08T13:52:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-09-08T13:52:37)
    0000   0xa5 0x74 0x2d 0x68 0x0d                   .t-h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 Ian3F 2013-09-08T13:52:37 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2013-09-08T13:52:37)
    0000   0xa5 0x74 0x4d 0x68 0x0d                   .tMh.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 BolusWizard 2013-09-08T13:57:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 72,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 2.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x48                                  [H
    decimal
             91   72
    datetime (2013-09-08T13:57:54)
    0000   0xb6 0x79 0x0d 0x08 0x0d                   .y...
    body (15)
    hex
    0000   0x13 0x90 0x00 0x6e 0x17 0x36 0x1c 0x00    ...n.6..
    0008   0x44 0x00 0x00 0x00 0x00 0x60 0x36         D....`6
    decimal
             19  144    0  110   23   54   28    0
             68    0    0    0    0   96   54
    HOUR BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 2.5, 'curve': 20},
 {'age': 103, 'amount': 1.4, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0x2b 0x14 0x38 0x67 0x14    \.d+.8g.
    decimal
             92    8  100   43   20   56  103   20
    datetime (unknown)

    body (0)

#### RECORD 26 Ian69 2013-09-08T13:57:55 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-08T13:57:55)
    0000   0xb7 0x79 0x0d 0x08 0x0d                   .y...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 1, 1]
#### RECORD 27 Bolus 2013-09-08T13:57:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x00 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    0    0
    datetime (2013-09-08T13:57:55)
    0000   0xb7 0x79 0x4d 0x08 0x0d                   .yM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 28 Ian0B 2013-09-08T14:39:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x44                             .fD
    decimal
             11  102   68
    datetime (2013-09-08T14:39:07)
    0000   0x87 0x67 0x4e 0xa8 0x0d                   .gN..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 29 NoDelivery 2013-09-08T14:57:22 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T14:57:22)
    0000   0x96 0x79 0xae 0x88 0x0d                   .y...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 30 Ian0B 2013-09-08T14:57:22 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x3b                             .f;
    decimal
             11  102   59
    datetime (2013-09-08T14:57:22)
    0000   0x96 0x79 0x4e 0xa8 0x0d                   .yN..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 31 PumpSuspend 2013-09-08T14:57:22 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T14:57:22)
    0000   0x96 0x79 0x0e 0x08 0x0d                   .y...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 32 ClearAlarm 2013-09-08T14:57:28 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x67                                  .g
    decimal
             12  103
    datetime (2013-09-08T14:57:28)
    0000   0x9c 0x79 0x0e 0x08 0x0d                   .y...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 33 PumpSuspend 2013-09-08T14:57:28 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x43                                  .C
    decimal
             30   67
    datetime (2013-09-08T14:57:28)
    0000   0x9c 0x79 0x0e 0x08 0x0d                   .y...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 34 PumpResume 2013-09-08T14:57:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x66                                  .f
    decimal
             31  102
    datetime (2013-09-08T14:57:30)
    0000   0x9e 0x79 0x0e 0x08 0x0d                   .y...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 35 BasalProfileStart 2013-09-08T14:57:30 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T14:57:30)
    0000   0x9e 0x79 0x0e 0x08 0x0d                   .y...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 1]
#### RECORD 36 PumpResume 2013-09-08T14:57:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime (2013-09-08T14:57:31)
    0000   0x9f 0x79 0x0e 0x08 0x0d                   .y...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 37 CalBGForPH 2013-09-08T15:03:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-09-08T15:03:11)
    0000   0x8b 0x43 0x2f 0x68 0x0d                   .C/h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 Ian3F 2013-09-08T15:03:11 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-09-08T15:03:11)
    0000   0x8b 0x43 0x8f 0x68 0x0d                   .C.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 Ian0B 2013-09-08T15:19:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x3f                             .f?
    decimal
             11  102   63
    datetime (2013-09-08T15:19:07)
    0000   0x87 0x53 0x4f 0xa8 0x0d                   .SO..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 40 Ian0B 2013-09-08T15:37:22 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x47                             .fG
    decimal
             11  102   71
    datetime (2013-09-08T15:37:22)
    0000   0x96 0x65 0x4f 0xa8 0x0d                   .eO..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 41 CalBGForPH 2013-09-08T15:38:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-09-08T15:38:05)
    0000   0x85 0x66 0x2f 0x68 0x0d                   .f/h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 Ian3F 2013-09-08T15:38:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-09-08T15:38:05)
    0000   0x85 0x66 0x0f 0x68 0x0d                   .f.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 Ian0B 2013-09-08T16:33:03 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x46                             .fF
    decimal
             11  102   70
    datetime (2013-09-08T16:33:03)
    0000   0x83 0x61 0x50 0xa8 0x0d                   .aP..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 44 Ian0B 2013-09-08T16:54:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x44                             .fD
    decimal
             11  102   68
    datetime (2013-09-08T16:54:07)
    0000   0x87 0x76 0x50 0xa8 0x0d                   .vP..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 45 NoDelivery 2013-09-08T17:03:13 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T17:03:13)
    0000   0x8d 0x43 0xb1 0x88 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0]
#### RECORD 46 PumpSuspend 2013-09-08T17:03:13 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T17:03:13)
    0000   0x8d 0x43 0x11 0x08 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 47 ClearAlarm 2013-09-08T17:03:18 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x67                                  .g
    decimal
             12  103
    datetime (2013-09-08T17:03:18)
    0000   0x92 0x43 0x11 0x08 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 48 PumpSuspend 2013-09-08T17:03:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x43                                  .C
    decimal
             30   67
    datetime (2013-09-08T17:03:18)
    0000   0x92 0x43 0x11 0x08 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 49 PumpResume 2013-09-08T17:03:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x66                                  .f
    decimal
             31  102
    datetime (2013-09-08T17:03:20)
    0000   0x94 0x43 0x11 0x08 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 50 BasalProfileStart 2013-09-08T17:03:20 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T17:03:20)
    0000   0x94 0x43 0x11 0x08 0x0d                   .C...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 51 PumpResume 2013-09-08T17:03:22 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime (2013-09-08T17:03:22)
    0000   0x96 0x43 0x11 0x08 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 52 Ian0B 2013-09-08T17:13:03 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x36                             .f6
    decimal
             11  102   54
    datetime (2013-09-08T17:13:03)
    0000   0x83 0x4d 0x51 0xa8 0x0d                   .MQ..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 53 NoDelivery 2013-09-08T17:23:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T17:23:00)
    0000   0x80 0x57 0xb1 0x88 0x0d                   .W...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0]
#### RECORD 54 PumpSuspend 2013-09-08T17:23:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T17:23:00)
    0000   0x80 0x57 0x11 0x08 0x0d                   .W...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 55 PumpSuspend 2013-09-08T17:23:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T17:23:05)
    0000   0x85 0x57 0x11 0x08 0x0d                   .W...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 56 ClearAlarm 2013-09-08T17:23:07 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x67                                  .g
    decimal
             12  103
    datetime (2013-09-08T17:23:07)
    0000   0x87 0x57 0x11 0x08 0x0d                   .W...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 PumpSuspend 2013-09-08T17:23:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x43                                  .C
    decimal
             30   67
    datetime (2013-09-08T17:23:07)
    0000   0x87 0x57 0x11 0x08 0x0d                   .W...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 58 PumpResume 2013-09-08T17:23:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x66                                  .f
    decimal
             31  102
    datetime (2013-09-08T17:23:09)
    0000   0x89 0x57 0x11 0x08 0x0d                   .W...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 59 BasalProfileStart 2013-09-08T17:23:09 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T17:23:09)
    0000   0x89 0x57 0x11 0x08 0x0d                   .W...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 60 PumpResume 2013-09-08T17:23:10 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime (2013-09-08T17:23:10)
    0000   0x8a 0x57 0x11 0x08 0x0d                   .W...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 61 CalBGForPH 2013-09-08T17:23:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-09-08T17:23:43)
    0000   0xab 0x57 0x31 0x68 0x0d                   .W1h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 Ian3F 2013-09-08T17:23:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2013-09-08T17:23:43)
    0000   0xab 0x57 0xd1 0x68 0x0d                   .W.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 63 BolusWizard 2013-09-08T17:29:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 61,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 1.2,
 'carb_input': 6,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 1.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 20}
```
    op hex (2)
    0000   0x5b 0x3d                                  [=
    decimal
             91   61
    datetime (2013-09-08T17:29:56)
    0000   0xb8 0x5d 0x11 0x68 0x0d                   .].h.
    body (15)
    hex
    0000   0x06 0x90 0x00 0x6e 0x17 0x36 0x0c 0x00    ...n.6..
    0008   0x14 0x00 0x00 0x0c 0x00 0x14 0x36         ......6
    decimal
              6  144    0  110   23   54   12    0
             20    0    0   12    0   20   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 2.25, 'curve': 4},
 {'age': 221, 'amount': 0.15, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x5a 0xd3 0x04 0x06 0xdd 0x04    \.Z.....
    decimal
             92    8   90  211    4    6  221    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-09-08T17:29:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x0c 0x00    ........
    decimal
              1    0   20    0   20    0   12    0
    datetime (2013-09-08T17:29:56)
    0000   0xb8 0x5d 0x51 0x68 0x0d                   .]Qh.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 Ian0B 2013-09-08T17:34:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x32                             .f2
    decimal
             11  102   50
    datetime (2013-09-08T17:34:07)
    0000   0x87 0x62 0x51 0xa8 0x0d                   .bQ..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 67 NoDelivery 2013-09-08T17:43:13 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T17:43:13)
    0000   0x8d 0x6b 0xb1 0x88 0x0d                   .k...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 68 PumpSuspend 2013-09-08T17:43:13 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T17:43:13)
    0000   0x8d 0x6b 0x11 0x08 0x0d                   .k...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 69 PumpSuspend 2013-09-08T17:43:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T17:43:17)
    0000   0x91 0x6b 0x11 0x08 0x0d                   .k...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 70 ClearAlarm 2013-09-08T17:43:20 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x67                                  .g
    decimal
             12  103
    datetime (2013-09-08T17:43:20)
    0000   0x94 0x6b 0x11 0x08 0x0d                   .k...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 71 PumpSuspend 2013-09-08T17:43:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x43                                  .C
    decimal
             30   67
    datetime (2013-09-08T17:43:20)
    0000   0x94 0x6b 0x11 0x08 0x0d                   .k...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 72 PumpResume 2013-09-08T17:43:21 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x66                                  .f
    decimal
             31  102
    datetime (2013-09-08T17:43:21)
    0000   0x95 0x6b 0x11 0x08 0x0d                   .k...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 73 BasalProfileStart 2013-09-08T17:43:21 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T17:43:21)
    0000   0x95 0x6b 0x11 0x08 0x0d                   .k...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 1]
#### RECORD 74 Ian0B 2013-09-08T17:53:03 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x31                             .f1
    decimal
             11  102   49
    datetime (2013-09-08T17:53:03)
    0000   0x83 0x75 0x51 0xa8 0x0d                   .uQ..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 75 CalBGForPH 2013-09-08T17:57:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 65}
```
    op hex (2)
    0000   0x0a 0x41                                  .A
    decimal
             10   65
    datetime (2013-09-08T17:57:45)
    0000   0xad 0x79 0x31 0x68 0x0d                   .y1h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 76 Ian3F 2013-09-08T17:57:45 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2013-09-08T17:57:45)
    0000   0xad 0x79 0x31 0x68 0x0d                   .y1h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 77 NoDelivery 2013-09-08T18:03:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T18:03:00)
    0000   0x80 0x43 0xb2 0x88 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0]
#### RECORD 78 PumpSuspend 2013-09-08T18:03:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T18:03:00)
    0000   0x80 0x43 0x12 0x08 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 79 PumpSuspend 2013-09-08T18:03:41 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T18:03:41)
    0000   0xa9 0x43 0x12 0x08 0x0d                   .C...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 80 PumpSuspend 2013-09-08T18:05:41 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x44                                  .D
    decimal
             30   68
    datetime (2013-09-08T18:05:41)
    0000   0xa9 0x45 0x12 0x08 0x0d                   .E...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 81 PumpSuspend 2013-09-08T18:08:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x85                                  ..
    decimal
             30  133
    datetime (2013-09-08T18:08:05)
    0000   0x85 0x48 0x12 0x08 0x0d                   .H...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 82 CalBGForPH 2013-09-08T18:10:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 53}
```
    op hex (2)
    0000   0x0a 0x35                                  .5
    decimal
             10   53
    datetime (2013-09-08T18:10:31)
    0000   0x9f 0x4a 0x32 0x68 0x0d                   .J2h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 83 Ian3F 2013-09-08T18:10:31 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2013-09-08T18:10:31)
    0000   0x9f 0x4a 0xb2 0x68 0x0d                   .J.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 84 Ian0B 2013-09-08T18:14:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x2e                             .f.
    decimal
             11  102   46
    datetime (2013-09-08T18:14:07)
    0000   0x87 0x4e 0x52 0xa8 0x0d                   .NR..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 85 CalBGForPH 2013-09-08T18:14:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2013-09-08T18:14:31)
    0000   0x9f 0x4e 0x32 0x68 0x0d                   .N2h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 86 Ian3F 2013-09-08T18:14:31 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2013-09-08T18:14:31)
    0000   0x9f 0x4e 0x72 0x68 0x0d                   .Nrh.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 87 PumpResume 2013-09-08T18:16:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xa6                                  ..
    decimal
             31  166
    datetime (2013-09-08T18:16:37)
    0000   0xa5 0x50 0x12 0x08 0x0d                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 88 BasalProfileStart 2013-09-08T18:16:37 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T18:16:37)
    0000   0xa5 0x50 0x12 0x08 0x0d                   .P...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 89 PumpResume 2013-09-08T18:16:38 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime (2013-09-08T18:16:38)
    0000   0xa6 0x50 0x12 0x08 0x0d                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 90 ChangeUtility 2013-09-08T18:17:30 head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x04                                  c.
    decimal
             99    4
    datetime (2013-09-08T18:17:30)
    0000   0x9e 0x51 0x12 0x08 0x0d                   .Q...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 91 Ian0B 2013-09-08T18:33:03 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x30                             .f0
    decimal
             11  102   48
    datetime (2013-09-08T18:33:03)
    0000   0x83 0x61 0x52 0xa8 0x0d                   .aR..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 92 NoDelivery 2013-09-08T18:39:07 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T18:39:07)
    0000   0x87 0x67 0xb2 0x88 0x0d                   .g...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 93 PumpSuspend 2013-09-08T18:39:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x02                                  ..
    decimal
             30    2
    datetime (2013-09-08T18:39:07)
    0000   0x87 0x67 0x12 0x08 0x0d                   .g...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 94 PumpSuspend 2013-09-08T18:41:13 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x44                                  .D
    decimal
             30   68
    datetime (2013-09-08T18:41:13)
    0000   0x8d 0x69 0x12 0x08 0x0d                   .i...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 95 PumpSuspend 2013-09-08T18:41:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x85                                  ..
    decimal
             30  133
    datetime (2013-09-08T18:41:15)
    0000   0x8f 0x69 0x12 0x08 0x0d                   .i...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 96 PumpSuspend 2013-09-08T18:51:23 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0xa4                                  ..
    decimal
             30  164
    datetime (2013-09-08T18:51:23)
    0000   0x97 0x73 0x12 0x08 0x0d                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 97 PumpSuspend 2013-09-08T18:51:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x85                                  ..
    decimal
             30  133
    datetime (2013-09-08T18:51:29)
    0000   0x9d 0x73 0x12 0x08 0x0d                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 98 Ian0B 2013-09-08T18:54:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x31                             .f1
    decimal
             11  102   49
    datetime (2013-09-08T18:54:07)
    0000   0x87 0x76 0x52 0xa8 0x0d                   .vR..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 99 CalBGForPH 2013-09-08T18:55:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2013-09-08T18:55:27)
    0000   0x9b 0x77 0x32 0x68 0x0d                   .w2h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 100 Ian3F 2013-09-08T18:55:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2013-09-08T18:55:27)
    0000   0x9b 0x77 0xb2 0x68 0x0d                   .w.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 101 PumpSuspend 2013-09-08T19:10:07 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0xa5                                  ..
    decimal
             30  165
    datetime (2013-09-08T19:10:07)
    0000   0x87 0x4a 0x13 0x08 0x0d                   .J...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 102 PumpResume 2013-09-08T19:10:12 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xa6                                  ..
    decimal
             31  166
    datetime (2013-09-08T19:10:12)
    0000   0x8c 0x4a 0x13 0x08 0x0d                   .J...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 103 BasalProfileStart 2013-09-08T19:10:12 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-08T19:10:12)
    0000   0x8c 0x4a 0x13 0x08 0x0d                   .J...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 104 PumpResume 2013-09-08T19:10:13 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0xc0                                  ..
    decimal
             31  192
    datetime (2013-09-08T19:10:13)
    0000   0x8d 0x4a 0x13 0x08 0x0d                   .J...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 105 Ian0B 2013-09-08T19:13:03 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x2e                             .f.
    decimal
             11  102   46
    datetime (2013-09-08T19:13:03)
    0000   0x83 0x4d 0x53 0xa8 0x0d                   .MS..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 106 NoDelivery 2013-09-08T19:34:07 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x67 0x01 0x55                        .g.U
    decimal
              6  103    1   85
    datetime (2013-09-08T19:34:07)
    0000   0x87 0x62 0xb3 0x88 0x0d                   .b...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 107 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xcd                                  ..
    decimal
              0  205
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-4.data: 108 records`
