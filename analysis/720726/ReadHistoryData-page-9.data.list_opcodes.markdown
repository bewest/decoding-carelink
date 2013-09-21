## START analysis/ianj/raw/ReadHistoryData-page-9.data
ERROR day is out of range for month 0000   0x9f 0x0d                                  ..
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xcc 0x6e                                  .n
##### DEBUG DECIMAL
            204  110
ERROR day is out of range for month 0000   0x9f 0x0d                                  ..
#### RECORD 0 Sara6E (2013, 8, 32, 0, 0, 0) head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime ((2013, 8, 32, 0, 0, 0))
    0000   0x9f 0x0d                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x5c 0x00 0x00 0x01 0x00 0x00    ..\.....
    0008   0x08 0x6d 0x03 0x87 0x2a 0x04 0xe6 0x3a    .m..*..:
    0010   0x01 0x51 0x03 0x52 0x00 0x00 0x01 0x44    .Q.R...D
    0018   0x00 0x50 0x0a 0x00 0x02 0x01 0x00 0x00    .P......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x5c    .......\
    0028   0x5c 0x00 0x00 0x00 0x00 0x00 0x00 0x00    \.......
    0030   0x00                                       .
    decimal
              6    0   92    0    0    1    0    0
              8  109    3  135   42    4  230   58
              1   81    3   82    0    0    1   68
              0   80   10    0    2    1    0    0
              0    0    0    0    0    0    0   92
             92    0    0    0    0    0    0    0
              0

#### RECORD 1 BasalProfileStart 2013-09-01T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-01T04:00:00)
    0000   0x80 0x40 0x04 0x01 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 2 LowReservoir 2013-09-01T05:36:31 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.0}
```
    op hex (2)
    0000   0x34 0x0a                                  4.
    decimal
             52   10
    datetime (2013-09-01T05:36:31)
    0000   0x9f 0x64 0x05 0x01 0x8d                   .d...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 BasalProfileStart 2013-09-01T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-01T09:30:00)
    0000   0x80 0x5e 0x09 0x01 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 4 CalBGForPH 2013-09-01T09:59:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 51}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2013-09-01T09:59:01)
    0000   0x81 0x7b 0x49 0x01 0x0d                   .{I..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2013-09-01T09:59:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 51,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 24.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x33                                  [3
    decimal
             91   51
    datetime (2013-09-01T09:59:09)
    0000   0x89 0x7b 0x09 0x61 0x0d                   .{.a.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0xf8 0x00    (..n.6..
    0008   0x90 0xf8 0x00 0x00 0x00 0x88 0x36         ......6
    decimal
             40  144    0  110   23   54  248    0
            144  248    0    0    0  136   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 Ian69 2013-09-01T09:59:09 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-01T09:59:09)
    0000   0x89 0x7b 0x09 0x01 0x0d                   .{...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 1, 1]
#### RECORD 7 Bolus 2013-09-01T09:59:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x00 0x00    ........
    decimal
              1    0  136    0  136    0    0    0
    datetime (2013-09-01T09:59:09)
    0000   0x89 0x7b 0x49 0x61 0x0d                   .{Ia.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 LowReservoir 2013-09-01T10:48:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.1}
```
    op hex (2)
    0000   0x34 0x01                                  4.
    decimal
             52    1
    datetime (2013-09-01T10:48:00)
    0000   0x80 0x70 0x0a 0x01 0x8d                   .p...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 BolusWizard 2013-09-01T12:44:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-01T12:44:52)
    0000   0xb4 0x6c 0x0c 0x61 0x0d                   .l.a.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 163, 'amount': 0.7, 'curve': 4},
 {'age': 173, 'amount': 2.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x1c 0xa3 0x04 0x6c 0xad 0x04    \....l..
    decimal
             92    8   28  163    4  108  173    4
    datetime (unknown)

    body (0)

#### RECORD 11 Ian69 2013-09-01T12:44:52 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-01T12:44:52)
    0000   0xb4 0x6c 0x0c 0x01 0x0d                   .l...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 1, 1]
#### RECORD 12 Bolus 2013-09-01T12:44:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x1c 0x00    ........
    decimal
              1    0  144    0  144    0   28    0
    datetime (2013-09-01T12:44:52)
    0000   0xb4 0x6c 0x4c 0x61 0x0d                   .lLa.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 BasalProfileStart 2013-09-01T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-01T13:00:00)
    0000   0x80 0x40 0x0d 0x01 0x0d                   .@...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 14 BolusWizard 2013-09-01T13:11:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-01T13:11:17)
    0000   0x91 0x4b 0x0d 0x61 0x0d                   .K.a.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 3.6, 'curve': 4},
 {'age': 190, 'amount': 0.7, 'curve': 4},
 {'age': 200, 'amount': 2.7, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x90 0x1e 0x04 0x1c 0xbe 0x04    \.......
    0008   0x6c 0xc8 0x04                             l..
    decimal
             92   11  144   30    4   28  190    4
            108  200    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-09-01T13:11:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x9c 0x00    ..T.T...
    decimal
              1    0   84    0   84    0  156    0
    datetime (2013-09-01T13:11:17)
    0000   0x91 0x4b 0x4d 0x61 0x0d                   .KMa.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2013-09-01T14:47:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2013-09-01T14:47:24)
    0000   0x98 0x6f 0x0e 0x61 0x0d                   .o.a.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 2.1, 'curve': 4},
 {'age': 126, 'amount': 3.6, 'curve': 4},
 {'age': 30, 'amount': 0.7, 'curve': 20},
 {'age': 40, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x54 0x60 0x04 0x90 0x7e 0x04    \.T`..~.
    0008   0x1c 0x1e 0x14 0x6c 0x28 0x14              ...l(.
    decimal
             92   14   84   96    4  144  126    4
             28   30   20  108   40   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-09-01T14:47:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x74 0x00    ..H.H.t.
    decimal
              1    0   72    0   72    0  116    0
    datetime (2013-09-01T14:47:24)
    0000   0x98 0x6f 0x4e 0x61 0x0d                   .oNa.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 Rewind 2013-09-01T15:30:40 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-09-01T15:30:40)
    0000   0xa8 0x5e 0x0f 0x01 0x0d                   .^...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 21 Prime 2013-09-01T15:31:10 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x09                   .....
    decimal
              3    0    0    0    9
    datetime (2013-09-01T15:31:10)
    0000   0x8a 0x5f 0x2f 0x01 0x0d                   ._/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 22 BasalProfileStart 2013-09-01T15:31:18 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-01T15:31:18)
    0000   0x92 0x5f 0x0f 0x01 0x0d                   ._...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 23 CalBGForPH 2013-09-01T15:31:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-09-01T15:31:30)
    0000   0x9e 0x5f 0x4f 0x01 0x0d                   ._O..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 24 BolusWizard 2013-09-01T15:31:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 91,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 12.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2013-09-01T15:31:33)
    0000   0xa1 0x5f 0x0f 0x61 0x0d                   ._.a.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x40 0x00    ...n.6@.
    0008   0x00 0x00 0x00 0x7c 0x00 0x00 0x36         ...|..6
    decimal
              0  144    0  110   23   54   64    0
              0    0    0  124    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 1.8, 'curve': 4},
 {'age': 140, 'amount': 2.1, 'curve': 4},
 {'age': 170, 'amount': 3.6, 'curve': 4},
 {'age': 74, 'amount': 0.7, 'curve': 20},
 {'age': 84, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x32 0x04 0x54 0x8c 0x04    \.H2.T..
    0008   0x90 0xaa 0x04 0x1c 0x4a 0x14 0x6c 0x54    ....J.lT
    0010   0x14                                       .
    decimal
             92   17   72   50    4   84  140    4
            144  170    4   28   74   20  108   84
             20
    datetime (unknown)

    body (0)

#### RECORD 26 BolusWizard 2013-09-01T15:31:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 91,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 12.4,
 'carb_input': 8,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 28}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2013-09-01T15:31:39)
    0000   0xa7 0x5f 0x0f 0x61 0x0d                   ._.a.
    body (15)
    hex
    0000   0x08 0x90 0x00 0x6e 0x17 0x36 0x40 0x00    ...n.6@.
    0008   0x1c 0x00 0x00 0x7c 0x00 0x1c 0x36         ...|..6
    decimal
              8  144    0  110   23   54   64    0
             28    0    0  124    0   28   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 1.8, 'curve': 4},
 {'age': 140, 'amount': 2.1, 'curve': 4},
 {'age': 170, 'amount': 3.6, 'curve': 4},
 {'age': 74, 'amount': 0.7, 'curve': 20},
 {'age': 84, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x32 0x04 0x54 0x8c 0x04    \.H2.T..
    0008   0x90 0xaa 0x04 0x1c 0x4a 0x14 0x6c 0x54    ....J.lT
    0010   0x14                                       .
    decimal
             92   17   72   50    4   84  140    4
            144  170    4   28   74   20  108   84
             20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-09-01T15:31:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x7c 0x00    ......|.
    decimal
              1    0   28    0   28    0  124    0
    datetime (2013-09-01T15:31:40)
    0000   0xa8 0x5f 0x4f 0x61 0x0d                   ._Oa.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 BolusWizard 2013-09-01T17:01:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-01T17:01:55)
    0000   0xb7 0x41 0x11 0x61 0x0d                   .A.a.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 90, 'amount': 0.7, 'curve': 4},
 {'age': 140, 'amount': 1.8, 'curve': 4},
 {'age': 230, 'amount': 2.1, 'curve': 4},
 {'age': 4, 'amount': 3.6, 'curve': 20},
 {'age': 164, 'amount': 0.7, 'curve': 20},
 {'age': 174, 'amount': 2.7, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x1c 0x5a 0x04 0x48 0x8c 0x04    \..Z.H..
    0008   0x54 0xe6 0x04 0x90 0x04 0x14 0x1c 0xa4    T.......
    0010   0x14 0x6c 0xae 0x14                        .l..
    decimal
             92   20   28   90    4   72  140    4
             84  230    4  144    4   20   28  164
             20  108  174   20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-09-01T17:01:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x34 0x00    ..@.@.4.
    decimal
              1    0   64    0   64    0   52    0
    datetime (2013-09-01T17:01:55)
    0000   0xb7 0x41 0x51 0x61 0x0d                   .AQa.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2013-09-01T17:57:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-01T17:57:57)
    0000   0xb9 0x79 0x11 0x61 0x0d                   .y.a.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 1.6, 'curve': 4},
 {'age': 146, 'amount': 0.7, 'curve': 4},
 {'age': 196, 'amount': 1.8, 'curve': 4},
 {'age': 30, 'amount': 2.1, 'curve': 20},
 {'age': 60, 'amount': 3.6, 'curve': 20},
 {'age': 220, 'amount': 0.7, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x40 0x38 0x04 0x1c 0x92 0x04    \.@8....
    0008   0x48 0xc4 0x04 0x54 0x1e 0x14 0x90 0x3c    H..T...<
    0010   0x14 0x1c 0xdc 0x14                        ....
    decimal
             92   20   64   56    4   28  146    4
             72  196    4   84   30   20  144   60
             20   28  220   20
    datetime (unknown)

    body (0)

#### RECORD 34 Ian69 2013-09-01T17:57:57 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-01T17:57:57)
    0000   0xb9 0x79 0x71 0x01 0x0d                   .yq..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 1, 1]
#### RECORD 35 Bolus 2013-09-01T17:57:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x48 0x00    ..p.p.H.
    decimal
              1    0  112    0  112    0   72    0
    datetime (2013-09-01T17:57:57)
    0000   0xb9 0x79 0x51 0x61 0x0d                   .yQa.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 BolusWizard 2013-09-01T18:05:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-01T18:05:12)
    0000   0x8c 0x45 0x12 0x61 0x0d                   .E.a.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 2.8, 'curve': 4},
 {'age': 64, 'amount': 1.6, 'curve': 4},
 {'age': 154, 'amount': 0.7, 'curve': 4},
 {'age': 204, 'amount': 1.8, 'curve': 4},
 {'age': 38, 'amount': 2.1, 'curve': 20},
 {'age': 68, 'amount': 3.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x70 0x0e 0x04 0x40 0x40 0x04    \.p..@@.
    0008   0x1c 0x9a 0x04 0x48 0xcc 0x04 0x54 0x26    ...H..T&
    0010   0x14 0x90 0x44 0x14                        ..D.
    decimal
             92   20  112   14    4   64   64    4
             28  154    4   72  204    4   84   38
             20  144   68   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-09-01T18:05:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0xb4 0x00    ..T.T...
    decimal
              1    0   84    0   84    0  180    0
    datetime (2013-09-01T18:05:12)
    0000   0x8c 0x45 0x52 0x61 0x0d                   .ERa.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 BolusWizard 2013-09-01T18:12:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-01T18:12:58)
    0000   0xba 0x4c 0x12 0x61 0x0d                   .L.a.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 2.1, 'curve': 4},
 {'age': 21, 'amount': 2.8, 'curve': 4},
 {'age': 71, 'amount': 1.6, 'curve': 4},
 {'age': 161, 'amount': 0.7, 'curve': 4},
 {'age': 211, 'amount': 1.8, 'curve': 4},
 {'age': 45, 'amount': 2.1, 'curve': 20},
 {'age': 75, 'amount': 3.6, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x54 0x0b 0x04 0x70 0x15 0x04    \.T..p..
    0008   0x40 0x47 0x04 0x1c 0xa1 0x04 0x48 0xd3    @G....H.
    0010   0x04 0x54 0x2d 0x14 0x90 0x4b 0x14         .T-..K.
    decimal
             92   23   84   11    4  112   21    4
             64   71    4   28  161    4   72  211
              4   84   45   20  144   75   20
    datetime (unknown)

    body (0)

#### RECORD 41 PumpSuspend 2013-09-01T18:13:03 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-09-01T18:13:03)
    0000   0x83 0x4d 0x12 0x01 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 42 Bolus 2013-09-01T18:12:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x03 0x01 0x00 0x00    ..$.....
    decimal
              1    0   36    0    3    1    0    0
    datetime (2013-09-01T18:12:58)
    0000   0xba 0x4c 0x52 0x61 0x0d                   .LRa.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 43 BasalProfileStart 2013-09-01T18:13:04 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-01T18:13:04)
    0000   0x84 0x4d 0x12 0x01 0x0d                   .M...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 44 PumpResume 2013-09-01T18:13:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-09-01T18:13:04)
    0000   0x84 0x4d 0x12 0x01 0x0d                   .M...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 45 BolusWizard 2013-09-01T19:23:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-01T19:23:17)
    0000   0x91 0x57 0x13 0x61 0x0d                   .W.a.
    body (15)
    hex
    0000   0x1a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x5c 0x00 0x00 0x00 0x00 0x5c 0x36         \....\6
    decimal
             26  144    0  110   23   54    0    0
             92    0    0    0    0   92   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 0.075, 'curve': 4},
 {'age': 82, 'amount': 2.1, 'curve': 4},
 {'age': 92, 'amount': 2.8, 'curve': 4},
 {'age': 142, 'amount': 1.6, 'curve': 4},
 {'age': 232, 'amount': 0.7, 'curve': 4},
 {'age': 26, 'amount': 1.8, 'curve': 20},
 {'age': 116, 'amount': 2.1, 'curve': 20},
 {'age': 146, 'amount': 3.6, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x03 0x48 0x04 0x54 0x52 0x04    \..H.TR.
    0008   0x70 0x5c 0x04 0x40 0x8e 0x04 0x1c 0xe8    p\.@....
    0010   0x04 0x48 0x1a 0x14 0x54 0x74 0x14 0x90    .H..Tt..
    0018   0x92 0x14                                  ..
    decimal
             92   26    3   72    4   84   82    4
            112   92    4   64  142    4   28  232
              4   72   26   20   84  116   20  144
            146   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-09-01T19:23:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x9c 0x00    ..\.\...
    decimal
              1    0   92    0   92    0  156    0
    datetime (2013-09-01T19:23:17)
    0000   0x91 0x57 0x53 0x61 0x0d                   .WSa.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2013-09-01T20:43:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2013-09-01T20:43:48)
    0000   0xb0 0x6b 0x14 0x61 0x0d                   .k.a.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 2.3, 'curve': 4},
 {'age': 152, 'amount': 0.075, 'curve': 4},
 {'age': 162, 'amount': 2.1, 'curve': 4},
 {'age': 172, 'amount': 2.8, 'curve': 4},
 {'age': 222, 'amount': 1.6, 'curve': 4},
 {'age': 56, 'amount': 0.7, 'curve': 20},
 {'age': 106, 'amount': 1.8, 'curve': 20},
 {'age': 196, 'amount': 2.1, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x5c 0x52 0x04 0x03 0x98 0x04    \.\R....
    0008   0x54 0xa2 0x04 0x70 0xac 0x04 0x40 0xde    T..p..@.
    0010   0x04 0x1c 0x38 0x14 0x48 0x6a 0x14 0x54    ..8.Hj.T
    0018   0xc4 0x14                                  ..
    decimal
             92   26   92   82    4    3  152    4
             84  162    4  112  172    4   64  222
              4   28   56   20   72  106   20   84
            196   20
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2013-09-01T20:43:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x74 0x00    ..H.H.t.
    decimal
              1    0   72    0   72    0  116    0
    datetime (2013-09-01T20:43:48)
    0000   0xb0 0x6b 0x54 0x61 0x0d                   .kTa.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 BolusWizard 2013-09-01T20:48:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-01T20:48:18)
    0000   0x92 0x70 0x14 0x61 0x0d                   .p.a.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 1.8, 'curve': 4},
 {'age': 87, 'amount': 2.3, 'curve': 4},
 {'age': 157, 'amount': 0.075, 'curve': 4},
 {'age': 167, 'amount': 2.1, 'curve': 4},
 {'age': 177, 'amount': 2.8, 'curve': 4},
 {'age': 227, 'amount': 1.6, 'curve': 4},
 {'age': 61, 'amount': 0.7, 'curve': 20},
 {'age': 111, 'amount': 1.8, 'curve': 20},
 {'age': 201, 'amount': 2.1, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x48 0x07 0x04 0x5c 0x57 0x04    \.H..\W.
    0008   0x03 0x9d 0x04 0x54 0xa7 0x04 0x70 0xb1    ...T..p.
    0010   0x04 0x40 0xe3 0x04 0x1c 0x3d 0x14 0x48    .@...=.H
    0018   0x6f 0x14 0x54 0xc9 0x14                   o.T..
    decimal
             92   29   72    7    4   92   87    4
              3  157    4   84  167    4  112  177
              4   64  227    4   28   61   20   72
            111   20   84  201   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-09-01T20:48:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0xb4 0x00    ..0.0...
    decimal
              1    0   48    0   48    0  180    0
    datetime (2013-09-01T20:48:18)
    0000   0x92 0x70 0x54 0x61 0x0d                   .pTa.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 BolusWizard 2013-09-01T23:42:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2013-09-01T23:42:28)
    0000   0x9c 0x6a 0x17 0x61 0x0d                   .j.a.
    body (15)
    hex
    0000   0x0c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x36         (....(6
    decimal
             12  144    0  110   23   54    0    0
             40    0    0    0    0   40   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 181, 'amount': 3.0, 'curve': 4},
 {'age': 5, 'amount': 2.3, 'curve': 20},
 {'age': 75, 'amount': 0.075, 'curve': 20},
 {'age': 85, 'amount': 2.1, 'curve': 20},
 {'age': 95, 'amount': 2.8, 'curve': 20},
 {'age': 145, 'amount': 1.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x78 0xb5 0x04 0x5c 0x05 0x14    \.x..\..
    0008   0x03 0x4b 0x14 0x54 0x55 0x14 0x70 0x5f    .K.TU.p_
    0010   0x14 0x40 0x91 0x14                        .@..
    decimal
             92   20  120  181    4   92    5   20
              3   75   20   84   85   20  112   95
             20   64  145   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-09-01T23:42:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x18 0x00    ..L.L...
    decimal
              1    0   76    0   76    0   24    0
    datetime (2013-09-01T23:42:29)
    0000   0x9d 0x6a 0x57 0x61 0x0d                   .jWa.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BasalProfileStart 2013-09-02T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-02T00:00:00)
    0000   0x80 0x40 0x00 0x02 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 1, 0]
#### RECORD 58 MResultTotals 2013-09-02T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x80                   .....
    decimal
              7    0    0    7  128
    datetime (2013-09-02T00:00:00)
    0000   0x81 0x8d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 59 Sara6E 2013-09-02T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-09-02T00:00:00)
    0000   0x81 0x8d                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x80 0x00 0x00 0x02 0x00 0x00    ........
    0008   0x07 0x80 0x03 0x89 0x2f 0x03 0xf7 0x35    ..../..5
    0010   0x01 0x15 0x03 0x3b 0x00 0x00 0x00 0xbc    ...;....
    0018   0x00 0x00 0x0b 0x00 0x02 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x5c    .......\
    0028   0xa4 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6    0  128    0    0    2    0    0
              7  128    3  137   47    3  247   53
              1   21    3   59    0    0    0  188
              0    0   11    0    2    0    0    0
              0    0    0    0    0    0    0   92
            164    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 60 BasalProfileStart 2013-09-02T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-02T04:00:00)
    0000   0x80 0x40 0x04 0x02 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 61 BolusWizard 2013-09-02T09:23:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-02T09:23:26)
    0000   0x9a 0x57 0x09 0x62 0x0d                   .W.b.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
`end analysis/ianj/raw/ReadHistoryData-page-9.data: 62 records`
