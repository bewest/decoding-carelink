## START logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 375, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb7 0x79 0x4d 0x08 0x0d 0x0b 0x66 0x44    .yM...fD
    0008   0x87 0x67 0x4e 0xa8 0x0d 0x06 0x67 0x01    .gN...g.
    0010   0x55 0x96 0x79 0xae 0x88 0x0d 0x0b 0x66    U.y....f
    0018   0x3b 0x96 0x79 0x4e 0xa8 0x0d 0x1e 0x02    ;.yN....
##### DEBUG DECIMAL
            183  121   77    8   13   11  102   68
            135  103   78  168   13    6  103    1
             85  150  121  174  136   13   11  102
             59  150  121   78  168   13   30    2
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

#### RECORD 15 Ian69 2013-09-08T09:01:06 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-08T09:01:06)
    0000   0x86 0x41 0x09 0x08 0x0d                   .A...
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x64 0x00 0x64 0x00    ....d.d.
    decimal
             10   30    1    0  100    0  100    0
    HOUR BITS: [0, 1, 0]
#### RECORD 16 Base (2013, 9, 8, 9, 1, 6) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x00                                  0.
    decimal
             48    0
    datetime ((2013, 9, 8, 9, 1, 6))
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

#### RECORD 26 Ian69 2013-09-08T13:57:55 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-08T13:57:55)
    0000   0xb7 0x79 0x0d 0x08 0x0d                   .y...
    body (8)
    hex
    0000   0x0e 0x1e 0x01 0x00 0x60 0x00 0x60 0x00    ....`.`.
    decimal
             14   30    1    0   96    0   96    0
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-4.data: 27 records`
