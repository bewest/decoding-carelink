## START logs/ReadHistoryData-page-8.data
#### STOPPING DOUBLE NULLS @ 201, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x03 0x32 0x62 0x86 0x6c 0x62 0x86 0x05    .2b.lb..
    0008   0x0c 0x00 0xe8 0x00 0x00 0x00 0x00 0x03    ........
    0010   0x32 0x03 0x32 0x64 0x00 0x00 0x00 0x00    2.2d....
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              3   50   98  134  108   98  134    5
             12    0  232    0    0    0    0    3
             50    3   50  100    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 BolusWizard 2006-07-01T08:23:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 100,
 'bg_target_low': 100,
 'bolus_estimate': 0.3,
 'carb_input': 3,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 0.3,
 'sensitivity': 50,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2006-07-01T08:23:47)
    0000   0x6f 0xd7 0x08 0x01 0x06                   o....
    body (13)
    hex
    0000   0x03 0x50 0x0a 0x32 0x64 0x00 0x03 0x00    .P.2d...
    0008   0x00 0x00 0x00 0x03 0x64                   ....d
    decimal
              3   80   10   50  100    0    3    0
              0    0    0    3  100
    HOUR BITS: [1, 1, 0]
#### RECORD 1 Bolus 2006-07-01T08:23:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2006-07-01T08:23:47)
    0000   0x6f 0xd7 0x28 0x01 0x06                   o.(..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2006-07-01T08:24:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 100,
 'bg_target_low': 100,
 'bolus_estimate': 0.7,
 'carb_input': 7,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 0.7,
 'sensitivity': 50,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2006-07-01T08:24:43)
    0000   0x6b 0xd8 0x08 0x01 0x06                   k....
    body (13)
    hex
    0000   0x07 0x50 0x0a 0x32 0x64 0x00 0x07 0x00    .P.2d...
    0008   0x00 0x03 0x00 0x07 0x64                   ....d
    decimal
              7   80   10   50  100    0    7    0
              0    3    0    7  100
    HOUR BITS: [1, 1, 0]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 1, 'amount': 0.3, 'curve': 68}]
```
    op hex (5)
    0000   0x5c 0x05 0x0c 0x01 0x44                   \...D
    decimal
             92    5   12    1   68
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2006-07-01T08:24:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2006-07-01T08:24:43)
    0000   0x6b 0xd8 0x28 0x01 0x06                   k.(..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BolusWizard 2006-07-01T08:26:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 99,
 '_byte[7]': 0,
 'bg': 599,
 'bg_target_high': 100,
 'bg_target_low': 100,
 'bolus_estimate': 9.0,
 'carb_input': 1,
 'carb_ratio': 10,
 'correction_estimate': 0.3,
 'food_estimate': 0.1,
 'sensitivity': 50,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x57                                  [W
    decimal
             91   87
    datetime (2006-07-01T08:26:55)
    0000   0x77 0xda 0x08 0x01 0x06                   w....
    body (13)
    hex
    0000   0x01 0x52 0x0a 0x32 0x64 0x63 0x01 0x00    .R.2dc..
    0008   0x00 0x0a 0x00 0x5a 0x64                   ...Zd
    decimal
              1   82   10   50  100   99    1    0
              0   10    0   90  100
    HOUR BITS: [1, 1, 0]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 1.0, 'curve': 68}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x03 0x44                   \.(.D
    decimal
             92    5   40    3   68
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2006-07-01T08:26:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 9.0, 'dual_component': '??', 'programmed': 9.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x5a 0x5a 0x00                        .ZZ.
    decimal
              1   90   90    0
    datetime (2006-07-01T08:26:55)
    0000   0x77 0xda 0x28 0x01 0x06                   w.(..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 PumpSuspend 2006-07-01T08:36:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2006-07-01T08:36:21)
    0000   0x55 0xe4 0x08 0x41 0x06                   U..A.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 9 PumpResume 2006-07-01T08:36:43 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2006-07-01T08:36:43)
    0000   0x6b 0xe4 0x08 0x41 0x06                   k..A.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 10 ResultTotals 2006-06-01T12:06:33 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x52                   ....R
    decimal
              7    0    0    4   82
    datetime (2006-06-01T12:06:33)
    0000   0x61 0x86 0x6c 0x61 0x86                   a.la.
    body (41)
    hex
    0000   0x05 0x21 0x0b 0x64 0x57 0x03 0x00 0x00    .!.dW...
    0008   0x04 0x52 0x02 0xc2 0x40 0x01 0x90 0x24    .R..@..$
    0010   0x00 0x0b 0x01 0x90 0x24 0x00 0x2c 0x0b    ....$.,.
    0018   0x01 0x64 0x59 0x00 0x00 0x00 0x03 0x02    .dY.....
    0020   0x00 0x01 0x00 0x1e 0x00 0x60 0xdd 0x12    .....`..
    0028   0x42                                       B
    decimal
              5   33   11  100   87    3    0    0
              4   82    2  194   64    1  144   36
              0   11    1  144   36    0   44   11
              1  100   89    0    0    0    3    2
              0    1    0   30    0   96  221   18
             66
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 11 NoDelivery 2014-12-06T02:18:30 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x1f 0x00 0x58                        ...X
    decimal
              6   31    0   88
    datetime (2014-12-06T02:18:30)
    0000   0xde 0x12 0x42 0x06 0x1e                   ..B..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 12 Base (2015, 12, 6, 2, 18, 37) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x57                                  .W
    decimal
              0   87
    datetime ((2015, 12, 6, 2, 18, 37))
    0000   0xe5 0x12 0x42 0x06 0x1f                   ..B..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 13 Base (2014, 12, 6, 2, 18, 37) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x69                                  .i
    decimal
              0  105
    datetime ((2014, 12, 6, 2, 18, 37))
    0000   0xe5 0x12 0x42 0x06 0x1e                   ..B..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 14 Base (2015, 12, 6, 2, 18, 57) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x63                                  .c
    decimal
              0   99
    datetime ((2015, 12, 6, 2, 18, 57))
    0000   0xf9 0x12 0x42 0x06 0x1f                   ..B..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 15 Base (2007, 12, 6, 2, 18, 58) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7a                                  .z
    decimal
              0  122
    datetime ((2007, 12, 6, 2, 18, 58))
    0000   0xfa 0x12 0x42 0x06 0x07                   ..B..
    body (0)

`end logs/ReadHistoryData-page-8.data: 16 records`
