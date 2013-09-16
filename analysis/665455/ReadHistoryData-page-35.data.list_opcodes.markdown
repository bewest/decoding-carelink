## START logs/ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 830, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x15 0x2b 0xee 0x2f 0x13 0x0d 0x03 0x00    .+./....
    0008   0x05 0x00 0x05 0x18 0xf0 0x0f 0x13 0x0d    ........
    0010   0x0a 0x74 0x17 0xf4 0x30 0x13 0x0d 0x0a    .t..0...
    0018   0xa5 0x08 0xdb 0x34 0x13 0x0d 0x5b 0xa5    ...4..[.
##### DEBUG DECIMAL
             21   43  238   47   19   13    3    0
              5    0    5   24  240   15   19   13
             10  116   23  244   48   19   13   10
            165    8  219   52   19   13   91  165
#### RECORD 0 CalBGForPH 2013-03-16T18:46:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-16T18:46:24)
    0000   0x18 0xee 0x32 0x10 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 PumpSuspend 2013-03-16T18:48:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-16T18:48:44)
    0000   0x2c 0xf0 0x12 0x10 0x0d                   ,....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 PumpResume 2013-03-16T19:14:27 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-16T19:14:27)
    0000   0x1b 0xce 0x13 0x10 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-16T20:13:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-16T20:13:20)
    0000   0x14 0xcd 0x34 0x10 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-03-16T20:13:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-03-16T20:13:42)
    0000   0x2a 0xcd 0x14 0x10 0x0d                   *....
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0xfc 0x35 0xf0    FP.-j.5.
    0008   0x00 0x00 0x00 0x31 0x7d                   ...1}
    decimal
             70   80   13   45  106  252   53  240
              0    0    0   49  125
    HOUR BITS: [1, 1, 0]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 123, 'amount': 0.55, 'curve': 20},
 {'age': 133, 'amount': 1.95, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x16 0x7b 0x14 0x4e 0x85 0x14    \..{.N..
    decimal
             92    8   22  123   20   78  133   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-03-16T20:13:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2013-03-16T20:13:42)
    0000   0x2a 0xcd 0x54 0x10 0x0d                   *.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2013-03-16T23:51:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2013-03-16T23:51:07)
    0000   0x07 0xf3 0x37 0x10 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BolusWizard 2013-03-16T23:51:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2013-03-16T23:51:28)
    0000   0x1c 0xf3 0x17 0x10 0x0d                   .....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x0a 0x0d 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x12 0x7d                   ....}
    decimal
             18   80   13   45  106   10   13    0
              0    5    0   18  125
    HOUR BITS: [1, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 4.45, 'curve': 4},
 {'age': 227, 'amount': 0.45, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb2 0xd9 0x04 0x12 0xe3 0x04    \.......
    decimal
             92    8  178  217    4   18  227    4
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-03-16T23:51:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-03-16T23:51:29)
    0000   0x1d 0xf3 0x57 0x10 0x0d                   ..W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 ResultTotals 2013-02-16T13:13:48 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe4                   .....
    decimal
              7    0    0    4  228
    datetime (2013-02-16T13:13:48)
    0000   0x30 0x8d 0x6d 0x30 0x8d                   0.m0.
    body (51)
    hex
    0000   0x05 0x00 0x77 0x59 0xae 0x05 0x00 0x00    ..wY....
    0008   0x04 0xe4 0x03 0x74 0x47 0x01 0x70 0x1d    ...tG.p.
    0010   0x00 0x79 0x01 0x70 0x1d 0x01 0x5c 0x5f    .y.p..\_
    0018   0x00 0x14 0x05 0x00 0x00 0x00 0x03 0x02    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x2e 0xd7 0x09 0x11 0x0d    ........
    0030   0x1f 0x00 0x1f                             ...
    decimal
              5    0  119   89  174    5    0    0
              4  228    3  116   71    1  112   29
              0  121    1  112   29    1   92   95
              0   20    5    0    0    0    3    2
              0    1    0   12    0  232    0    0
              0   30    0   46  215    9   17   13
             31    0   31
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 Base (2006, 0, 14, 10, 13, 17) head[2], body[0] op[0xd9]

    op hex (2)
    0000   0xd9 0x09                                  ..
    decimal
            217    9
    datetime ((2006, 0, 14, 10, 13, 17))
    0000   0x11 0x0d 0x0a 0x4e 0x36                   ...N6
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 13 Base (2014, 2, 14, 27, 13, 17) head[2], body[0] op[0xd9]

    op hex (2)
    0000   0xd9 0x29                                  .)
    decimal
            217   41
    datetime ((2014, 2, 14, 27, 13, 17))
    0000   0x11 0x8d 0x5b 0x4e 0x0e                   ..[N.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0]
#### RECORD 14 Base (2013, 0, 17, 0, 13, 17) head[2], body[0] op[0xda]

    op hex (2)
    0000   0xda 0x09                                  ..
    decimal
            218    9
    datetime ((2013, 0, 17, 0, 13, 17))
    0000   0x11 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 15 Base (2000, 0, 0, 0, 0, 46) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 46))
    0000   0x2e 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 16 Base (2000, 4, 17, 17, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2e                                  ..
    decimal
              0   46
    datetime ((2000, 4, 17, 17, 1, 61))
    0000   0x7d 0x01 0x31 0x31 0x00                   }.11.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 17 Base (2000, 4, 30, 13, 17, 9) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0xda                                  ..
    decimal
             14  218
    datetime ((2000, 4, 30, 13, 17, 9))
    0000   0x49 0x11 0x0d 0x1e 0x00                   I....
    body (0)

#### RECORD 18 Base (2000, 0, 31, 13, 17, 9) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0xdf                                  ..
    decimal
             28  223
    datetime ((2000, 0, 31, 13, 17, 9))
    0000   0x09 0x11 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 19 Base (2014, 0, 10, 13, 17, 9) head[2], body[0] op[0x3b]

    op hex (2)
    0000   0x3b 0xef                                  ;.
    decimal
             59  239
    datetime ((2014, 0, 10, 13, 17, 9))
    0000   0x09 0x11 0x0d 0x0a 0x7e                   ....~
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 20 ChangeRemoteID (2014, 0, 10, 13, 17, 44) head[2], body[0] op[0x27]

    op hex (2)
    0000   0x27 0xcf                                  '.
    decimal
             39  207
    datetime ((2014, 0, 10, 13, 17, 44))
    0000   0x2c 0x11 0x0d 0x0a 0x7e                   ,...~
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 21 Base (2014, 0, 27, 13, 17, 44) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0xf2                                  ..
    decimal
             21  242
    datetime ((2014, 0, 27, 13, 17, 44))
    0000   0x2c 0x11 0x0d 0x5b 0x7e                   ,..[~
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 22 Base (2000, 0, 19, 13, 17, 12) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xf3                                  ..
    decimal
              0  243
    datetime ((2000, 0, 19, 13, 17, 12))
    0000   0x0c 0x11 0x0d 0x33 0x50                   ...3P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 23 Base (2000, 4, 0, 7, 0, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 7, 0, 42))
    0000   0x6a 0x00 0x27 0x00 0x00                   j.'..
    body (0)

#### RECORD 24 NoDelivery 2004-04-15T04:05:28 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x00 0x27 0x7d                        ..'}
    decimal
              6    0   39  125
    datetime (2004-04-15T04:05:28)
    0000   0x5c 0x05 0xc4 0xcf 0x04                   \....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 25 Bolus 2013-03-17T12:51:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-03-17T12:51:00)
    0000   0x00 0xf3 0x4c 0x11 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 CalBGForPH 2013-03-17T17:03:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-17T17:03:51)
    0000   0x33 0xc3 0x31 0x11 0x0d                   3.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 CalBGForPH 2013-03-17T19:33:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-03-17T19:33:48)
    0000   0x30 0xe1 0x33 0x11 0x0d                   0.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 BolusWizard 2013-03-17T19:34:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 2.1,
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
    datetime (2013-03-17T19:34:37)
    0000   0x25 0xe2 0x13 0x11 0x0d                   %....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0xfc 0x15 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             28   80   13   45  106  252   21  240
              0    0    0   17  125
    HOUR BITS: [1, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 154, 'amount': 3.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0x9a 0x14                   \....
    decimal
             92    5  156  154   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-03-17T19:34:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-03-17T19:34:37)
    0000   0x25 0xe2 0x53 0x11 0x0d                   %.S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 BolusWizard 2013-03-17T20:04:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.1,
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
    datetime (2013-03-17T20:04:50)
    0000   0x32 0xc4 0x14 0x11 0x0d                   2....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0    0    0   21  125
    HOUR BITS: [1, 1, 0]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.7, 'curve': 4},
 {'age': 184, 'amount': 3.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x1e 0x04 0x9c 0xb8 0x14    \.D.....
    decimal
             92    8   68   30    4  156  184   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-03-17T20:04:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-03-17T20:04:50)
    0000   0x32 0xc4 0x54 0x11 0x0d                   2.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 34 ResultTotals 2013-02-17T13:13:49 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x6e                   ....n
    decimal
              7    0    0    5  110
    datetime (2013-02-17T13:13:49)
    0000   0x31 0x8d 0x6d 0x31 0x8d                   1.m1.
    body (51)
    hex
    0000   0x05 0x10 0x98 0x58 0x4e 0x05 0x00 0x00    ...XN...
    0008   0x05 0x6e 0x03 0x76 0x40 0x01 0xf8 0x24    .n.v@..$
    0010   0x00 0x6b 0x01 0xf8 0x24 0x01 0x34 0x3d    .k..$.4=
    0018   0x00 0xc4 0x27 0x00 0x00 0x00 0x04 0x03    ..'.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x76 0x0c 0xc3 0x21 0x12 0x0d    ..v..!..
    0030   0x1e 0x00 0x06                             ...
    decimal
              5   16  152   88   78    5    0    0
              5  110    3  118   64    1  248   36
              0  107    1  248   36    1   52   61
              0  196   39    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0   10  118   12  195   33   18   13
             30    0    6
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 35 Base (2007, 0, 0, 31, 13, 18) head[2], body[0] op[0xca]

    op hex (2)
    0000   0xca 0x0e                                  ..
    decimal
            202   14
    datetime ((2007, 0, 0, 31, 13, 18))
    0000   0x12 0x0d 0x1f 0x00 0x37                   ....7
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 36 Base (2009, 0, 24, 10, 13, 18) head[2], body[0] op[0xe5]

    op hex (2)
    0000   0xe5 0x0e                                  ..
    decimal
            229   14
    datetime ((2009, 0, 24, 10, 13, 18))
    0000   0x12 0x0d 0x0a 0x58 0x29                   ...X)
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 37 Base (2003, 0, 24, 27, 13, 18) head[2], body[0] op[0xcb]

    op hex (2)
    0000   0xcb 0x2f                                  ./
    decimal
            203   47
    datetime ((2003, 0, 24, 27, 13, 18))
    0000   0x12 0x0d 0x5b 0x58 0x13                   ..[X.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 38 Base (2013, 0, 16, 24, 13, 18) head[2], body[0] op[0xcd]

    op hex (2)
    0000   0xcd 0x0f                                  ..
    decimal
            205   15
    datetime ((2013, 0, 16, 24, 13, 18))
    0000   0x12 0x0d 0x38 0x50 0x0d                   ..8P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 39 Base (2000, 12, 0, 16, 43, 60) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 43, 60))
    0000   0xfc 0x2b 0xf0 0x00 0x00                   .+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 Base (2000, 4, 7, 7, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x27                                  .'
    decimal
              0   39
    datetime ((2000, 4, 7, 7, 1, 61))
    0000   0x7d 0x01 0x27 0x27 0x00                   }.''.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 41 Base (2000, 4, 10, 13, 18, 15) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0xcd                                  ..
    decimal
             19  205
    datetime ((2000, 4, 10, 13, 18, 15))
    0000   0x4f 0x12 0x0d 0x0a 0x90                   O....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 42 Base (2000, 0, 27, 13, 18, 49) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0xdd                                  ..
    decimal
              9  221
    datetime ((2000, 0, 27, 13, 18, 49))
    0000   0x31 0x12 0x0d 0x5b 0x90                   1..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 43 Battery (2000, 0, 25, 13, 18, 17) head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0xdd                                  ..
    decimal
             26  221
    datetime ((2000, 0, 25, 13, 18, 17))
    0000   0x11 0x12 0x0d 0x19 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 44 Base (2000, 4, 0, 19, 4, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 19, 4, 42))
    0000   0x6a 0x04 0x13 0x00 0x00                   j....
    body (0)

#### RECORD 45 Base (2002, 1, 8, 28, 61, 19) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x00                                  ..
    decimal
             14    0
    datetime ((2002, 1, 8, 28, 61, 19))
    0000   0x13 0x7d 0x5c 0x08 0x72                   .}\.r
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 46 Base (2003, 2, 1, 4, 17, 42) head[2], body[0] op[0x87]

    op hex (2)
    0000   0x87 0x04                                  ..
    decimal
            135    4
    datetime ((2003, 2, 1, 4, 17, 42))
    0000   0x2a 0x91 0x04 0x01 0x13                   *....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 47 Base (2013, 3, 18, 17, 29, 26) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x00                                  ..
    decimal
             19    0
    datetime ((2013, 3, 18, 17, 29, 26))
    0000   0x1a 0xdd 0x51 0x12 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 CalBGForPH 2013-03-18T20:15:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 152}
```
    op hex (2)
    0000   0x0a 0x98                                  ..
    decimal
             10  152
    datetime (2013-03-18T20:15:46)
    0000   0x2e 0xcf 0x34 0x12 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 BolusWizard 2013-03-18T20:15:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 152,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x98                                  [.
    decimal
             91  152
    datetime (2013-03-18T20:15:55)
    0000   0x37 0xcf 0x14 0x12 0x0d                   7....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x02 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    4    0    2  125
    HOUR BITS: [1, 1, 0]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 171, 'amount': 1.9, 'curve': 4},
 {'age': 45, 'amount': 2.85, 'curve': 20},
 {'age': 55, 'amount': 1.05, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0xab 0x04 0x72 0x2d 0x14    \.L..r-.
    0008   0x2a 0x37 0x14                             *7.
    decimal
             92   11   76  171    4  114   45   20
             42   55   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-03-18T20:15:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-03-18T20:15:55)
    0000   0x37 0xcf 0x54 0x12 0x0d                   7.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 52 CalBGForPH 2013-03-18T20:59:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-03-18T20:59:40)
    0000   0x28 0xfb 0x34 0x12 0x0d                   (.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 53 BolusWizard 2013-03-18T20:59:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-03-18T20:59:54)
    0000   0x36 0xfb 0x14 0x12 0x0d                   6....
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0x02 0x24 0x00    0P.-j.$.
    0008   0x00 0x04 0x00 0x24 0x7d                   ...$}
    decimal
             48   80   13   45  106    2   36    0
              0    4    0   36  125
    HOUR BITS: [1, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 0.2, 'curve': 4},
 {'age': 215, 'amount': 1.9, 'curve': 4},
 {'age': 89, 'amount': 2.85, 'curve': 20},
 {'age': 99, 'amount': 1.05, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x08 0x2d 0x04 0x4c 0xd7 0x04    \..-.L..
    0008   0x72 0x59 0x14 0x2a 0x63 0x14              rY.*c.
    decimal
             92   14    8   45    4   76  215    4
            114   89   20   42   99   20
    datetime (unknown)

    body (0)

#### RECORD 55 LowReservoir 2013-03-18T21:00:28 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-18T21:00:28)
    0000   0x1c 0xc0 0x15 0x12 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 Bolus 2013-03-18T20:59:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-03-18T20:59:54)
    0000   0x36 0xfb 0x54 0x12 0x0d                   6.T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 57 CalBGForPH 2013-03-18T21:12:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-03-18T21:12:14)
    0000   0x0e 0xcc 0x35 0x12 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 58 CalBGForPH 2013-03-18T23:13:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-03-18T23:13:35)
    0000   0x23 0xcd 0x37 0x12 0x0d                   #.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 ResultTotals 2013-02-18T13:13:50 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf2                   .....
    decimal
              7    0    0    4  242
    datetime (2013-02-18T13:13:50)
    0000   0x32 0x8d 0x6d 0x32 0x8d                   2.m2.
    body (51)
    hex
    0000   0x05 0x00 0x7f 0x58 0x98 0x07 0x00 0x00    ...X....
    0008   0x04 0xf2 0x03 0x72 0x46 0x01 0x80 0x1e    ...rF...
    0010   0x00 0x81 0x01 0x80 0x1e 0x01 0x78 0x62    ......xb
    0018   0x00 0x08 0x02 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x34 0x64 0x00 0xde 0x05 0x13 0x0d    .4d.....
    0030   0x1e 0x00 0x18                             ...
    decimal
              5    0  127   88  152    7    0    0
              4  242    3  114   70    1  128   30
              0  129    1  128   30    1  120   98
              0    8    2    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0   52  100    0  222    5   19   13
             30    0   24
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 60 Base (2012, 0, 0, 31, 13, 19) head[2], body[0] op[0xea]

    op hex (2)
    0000   0xea 0x0b                                  ..
    decimal
            234   11
    datetime ((2012, 0, 0, 31, 13, 19))
    0000   0x13 0x0d 0x1f 0x00 0x2c                   ....,
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 61 Base (2006, 0, 24, 10, 13, 19) head[2], body[0] op[0xcb]

    op hex (2)
    0000   0xcb 0x0c                                  ..
    decimal
            203   12
    datetime ((2006, 0, 24, 10, 13, 19))
    0000   0x13 0x0d 0x0a 0x18 0x06                   .....
    body (0)

#### RECORD 62 Base (2011, 2, 24, 27, 13, 19) head[2], body[0] op[0xea]

    op hex (2)
    0000   0xea 0x2c                                  .,
    decimal
            234   44
    datetime ((2011, 2, 24, 27, 13, 19))
    0000   0x13 0x8d 0x5b 0x18 0x0b                   ..[..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 Base (2013, 0, 17, 0, 13, 19) head[2], body[0] op[0xea]

    op hex (2)
    0000   0xea 0x0c                                  ..
    decimal
            234   12
    datetime ((2013, 0, 17, 0, 13, 19))
    0000   0x13 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 64 Base (2000, 0, 0, 0, 0, 34) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 34))
    0000   0x22 0x00 0x00 0x00 0x00                   "....
    body (0)

#### RECORD 65 Base (2000, 4, 2, 2, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x22                                  ."
    decimal
              0   34
    datetime ((2000, 4, 2, 2, 1, 61))
    0000   0x7d 0x01 0x22 0x22 0x00                   }."".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 66 Ian0B (2010, 0, 21, 10, 13, 19) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0xea 0x4c                             ..L
    decimal
             11  234   76
    datetime ((2010, 0, 21, 10, 13, 19))
    0000   0x13 0x0d 0x0a 0xf5 0x3a                   ....:
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 67 Base (2008, 0, 21, 27, 13, 19) head[2], body[0] op[0xc7]

    op hex (2)
    0000   0xc7 0x2d                                  .-
    decimal
            199   45
    datetime ((2008, 0, 21, 27, 13, 19))
    0000   0x13 0x0d 0x5b 0xf5 0x18                   ..[..
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 68 Base (2013, 0, 16, 8, 13, 19) head[2], body[0] op[0xc8]

    op hex (2)
    0000   0xc8 0x0d                                  ..
    decimal
            200   13
    datetime ((2013, 0, 16, 8, 13, 19))
    0000   0x13 0x0d 0x28 0x50 0x0d                   ..(P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 69 Base (2000, 0, 0, 0, 30, 26) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 30, 26))
    0000   0x1a 0x1e 0x00 0x00 0x20                   .... 
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 70 Base (2008, 5, 28, 8, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1e                                  ..
    decimal
              0   30
    datetime ((2008, 5, 28, 8, 28, 61))
    0000   0x7d 0x5c 0x08 0x1c 0x18                   }\...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 71 Base (2014, 0, 30, 1, 4, 34) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x6c                                  .l
    decimal
              4  108
    datetime ((2014, 0, 30, 1, 4, 34))
    0000   0x22 0x04 0x01 0x1e 0x1e                   "....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 72 Base (2011, 13, 13, 19, 13, 8) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x18                                  ..
    decimal
              0   24
    datetime ((2011, 13, 13, 19, 13, 8))
    0000   0xc8 0x4d 0x13 0x0d 0x5b                   .M..[
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 73 Base (2004, 12, 13, 19, 13, 52) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x12                                  ..
    decimal
              0   18
    datetime ((2004, 12, 13, 19, 13, 52))
    0000   0xf4 0x0d 0x13 0x0d 0x24                   ....$
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 74 Ian50 2000-01-27T00:42:45 head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime (2000-01-27T00:42:45)
    0000   0x2d 0x6a 0x00 0x1b 0x00                   -j...
    body (34)
    hex
    0000   0x00 0x00 0x00 0x1b 0x7d 0x5c 0x0b 0x78    ....}\.x
    0008   0x30 0x04 0x1c 0x44 0x04 0x6c 0x4e 0x04    0..D.lN.
    0010   0x01 0x1b 0x1b 0x00 0x12 0xf4 0x4d 0x13    ......M.
    0018   0x0d 0x21 0x00 0x29 0xec 0x0f 0x13 0x0d    .!.)....
    0020   0x03 0x00                                  ..
    decimal
              0    0    0   27  125   92   11  120
             48    4   28   68    4  108   78    4
              1   27   27    0   18  244   77   19
             13   33    0   41  236   15   19   13
              3    0
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-35.data: 75 records`
