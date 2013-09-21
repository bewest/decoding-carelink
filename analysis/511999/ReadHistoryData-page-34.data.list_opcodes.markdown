## START analysis/sarak/raw//ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 389, found 99 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x09 0x04 0x62 0xf7 0x07 0x05 0x0d 0x00    ..b.....
    0008   0x1c 0x00 0x08 0x1e 0x00 0x10 0x24 0x00    ......$.
    0010   0x18 0x1d 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              9    4   98  247    7    5   13    0
             28    0    8   30    0   16   36    0
             24   29    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 Bolus 2013-07-04T19:01:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x10 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   16    0
    datetime (2013-07-04T19:01:19)
    0000   0x53 0xc1 0x53 0x64 0x0d                   S.Sd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2013-07-04T19:08:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 198,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 13.2,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0xc6                                  [.
    decimal
             91  198
    datetime (2013-07-04T19:08:26)
    0000   0x5a 0xc8 0x13 0x04 0x0d                   Z....
    body (15)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x34 0x00    .P.d<d4.
    0008   0x50 0x00 0x00 0x84 0x00 0x50 0x78         P....Px
    decimal
             20   80    0  100   60  100   52    0
             80    0    0  132    0   80  120
    HOUR BITS: [1, 1, 0]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 3.0, 'curve': 192},
 {'age': 54, 'amount': 0.4, 'curve': 192},
 {'age': 8, 'amount': 1.6, 'curve': 208},
 {'age': 38, 'amount': 1.8, 'curve': 208},
 {'age': 218, 'amount': 1.7, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x78 0x0e 0xc0 0x10 0x36 0xc0    \.x...6.
    0008   0x40 0x08 0xd0 0x48 0x26 0xd0 0x44 0xda    @..H&.D.
    0010   0xd0                                       .
    decimal
             92   17  120   14  192   16   54  192
             64    8  208   72   38  208   68  218
            208
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2013-07-04T19:08:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x84 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  132    0
    datetime (2013-07-04T19:08:26)
    0000   0x5a 0xc8 0x53 0x04 0x0d                   Z.S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-04T19:25:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 282}
```
    op hex (2)
    0000   0x0a 0x1a                                  ..
    decimal
             10   26
    datetime (2013-07-04T19:25:43)
    0000   0x6b 0xd9 0x33 0x04 0x8d                   k.3..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 BolusWizard 2013-07-04T19:25:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 282,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 19.6,
 'carb_input': 4,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 16}
```
    op hex (2)
    0000   0x5b 0x1a                                  [.
    decimal
             91   26
    datetime (2013-07-04T19:25:49)
    0000   0x71 0xd9 0x13 0x64 0x0d                   q..d.
    body (15)
    hex
    0000   0x04 0x51 0x00 0x64 0x3c 0x64 0x6c 0x00    .Q.d<dl.
    0008   0x10 0x00 0x00 0xc4 0x00 0x10 0x78         ......x
    decimal
              4   81    0  100   60  100  108    0
             16    0    0  196    0   16  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 2.0, 'curve': 192},
 {'age': 31, 'amount': 3.0, 'curve': 192},
 {'age': 71, 'amount': 0.4, 'curve': 192},
 {'age': 25, 'amount': 1.6, 'curve': 208},
 {'age': 55, 'amount': 1.8, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x15 0xc0 0x78 0x1f 0xc0    \.P..x..
    0008   0x10 0x47 0xc0 0x40 0x19 0xd0 0x48 0x37    .G.@..H7
    0010   0xd0                                       .
    decimal
             92   17   80   21  192  120   31  192
             16   71  192   64   25  208   72   55
            208
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-07-04T19:25:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0xc4 0x00    ........
    decimal
              1    0   16    0   16    0  196    0
    datetime (2013-07-04T19:25:49)
    0000   0x71 0xd9 0x53 0x64 0x0d                   q.Sd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 CalBGForPH 2013-07-04T20:13:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-07-04T20:13:12)
    0000   0x4c 0xcd 0x34 0x04 0x0d                   L.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 BolusWizard 2013-07-04T20:13:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 13.6,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2013-07-04T20:13:47)
    0000   0x6f 0xcd 0x14 0x64 0x0d                   o..d.
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x34 0x00 0x00 0x88 0x00 0x34 0x78         4....4x
    decimal
             13   80    0  100   60  100    0    0
             52    0    0  136    0   52  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 0.4, 'curve': 192},
 {'age': 69, 'amount': 2.0, 'curve': 192},
 {'age': 79, 'amount': 3.0, 'curve': 192},
 {'age': 119, 'amount': 0.4, 'curve': 192},
 {'age': 73, 'amount': 1.6, 'curve': 208},
 {'age': 103, 'amount': 1.8, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x10 0x31 0xc0 0x50 0x45 0xc0    \..1.PE.
    0008   0x78 0x4f 0xc0 0x10 0x77 0xc0 0x40 0x49    xO..w.@I
    0010   0xd0 0x48 0x67 0xd0                        .Hg.
    decimal
             92   20   16   49  192   80   69  192
            120   79  192   16  119  192   64   73
            208   72  103  208
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-07-04T20:13:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x88 0x00    ..4.4...
    decimal
              1    0   52    0   52    0  136    0
    datetime (2013-07-04T20:13:47)
    0000   0x6f 0xcd 0x54 0x64 0x0d                   o.Td.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 CalBGForPH 2013-07-04T21:57:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2013-07-04T21:57:08)
    0000   0x48 0xf9 0x35 0x04 0x8d                   H.5..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 13 BolusWizard 2013-07-04T21:57:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 268,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 9.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2013-07-04T21:57:20)
    0000   0x54 0xf9 0x15 0x64 0x0d                   T..d.
    body (15)
    hex
    0000   0x15 0x51 0x00 0x64 0x3c 0x64 0x60 0x00    .Q.d<d`.
    0008   0x54 0x00 0x00 0x1c 0x00 0x98 0x78         T.....x
    decimal
             21   81    0  100   60  100   96    0
             84    0    0   28    0  152  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 1.0, 'curve': 192},
 {'age': 113, 'amount': 0.3, 'curve': 192},
 {'age': 153, 'amount': 0.4, 'curve': 192},
 {'age': 173, 'amount': 2.0, 'curve': 192},
 {'age': 183, 'amount': 3.0, 'curve': 192},
 {'age': 223, 'amount': 0.4, 'curve': 192},
 {'age': 177, 'amount': 1.6, 'curve': 208},
 {'age': 207, 'amount': 1.8, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x28 0x67 0xc0 0x0c 0x71 0xc0    \.(g..q.
    0008   0x10 0x99 0xc0 0x50 0xad 0xc0 0x78 0xb7    ...P..x.
    0010   0xc0 0x10 0xdf 0xc0 0x40 0xb1 0xd0 0x48    ....@..H
    0018   0xcf 0xd0                                  ..
    decimal
             92   26   40  103  192   12  113  192
             16  153  192   80  173  192  120  183
            192   16  223  192   64  177  208   72
            207  208
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-07-04T21:57:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x1c 0x00    ........
    decimal
              1    0  152    0  152    0   28    0
    datetime (2013-07-04T21:57:20)
    0000   0x54 0xf9 0x55 0x64 0x0d                   T.Ud.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 BasalProfileStart 2013-07-05T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-05T00:00:00)
    0000   0x40 0xc0 0x00 0x05 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 17 MResultTotals 2013-07-05T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x1f                   .....
    decimal
              7    0    0    6   31
    datetime (2013-07-05T00:00:00)
    0000   0x64 0x8d                                  d.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 18 Sara6E 2013-07-05T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-07-05T00:00:00)
    0000   0x64 0x8d                                  d.
    body (49)
    hex
    0000   0x05 0x00 0xbc 0x00 0x00 0x0a 0x00 0x00    ........
    0008   0x06 0x1f 0x02 0xe3 0x2f 0x03 0x3c 0x35    ..../.<5
    0010   0x00 0xa1 0x01 0x2c 0x00 0x2c 0x01 0xa0    ...,.,..
    0018   0x00 0x44 0x06 0x01 0x03 0x01 0x04 0x00    .D......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x44    .......D
    0028   0x1a 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  188    0    0   10    0    0
              6   31    2  227   47    3   60   53
              0  161    1   44    0   44    1  160
              0   68    6    1    3    1    4    0
              0    0    0    0    0    0    0   68
             26    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 19 BasalProfileStart 2013-07-05T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-05T04:00:00)
    0000   0x40 0xc0 0x04 0x05 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 20 ChangeBasalProfile 2013-07-05T07:55:34 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x04                                  ..
    decimal
              8    4
    datetime (2013-07-05T07:55:34)
    0000   0x62 0xf7 0x07 0x05 0x0d                   b....
    body (44)
    hex
    0000   0x00 0x20 0x00 0x08 0x1e 0x00 0x10 0x24    . .....$
    0008   0x00 0x18 0x1d 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00                        ....
    decimal
              0   32    0    8   30    0   16   36
              0   24   29    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0
    HOUR BITS: [1, 1, 1]
`end analysis/sarak/raw//ReadHistoryData-page-34.data: 21 records`
