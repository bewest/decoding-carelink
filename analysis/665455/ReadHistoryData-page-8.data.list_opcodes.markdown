## START logs/ReadHistoryData-page-8.data
#### STOPPING DOUBLE NULLS @ 242, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x2d 0x7d 0x01 0x2d 0x2d 0x00 0x5e 0x91    -}.--.^.
    0008   0x56 0x1d 0x0d 0x5b 0x00 0x6a 0x82 0x17    V..[.j..
    0010   0x1d 0x0d 0x10 0x50 0x0d 0x2d 0x6a 0x00    ...P.-j.
    0018   0x0c 0x00 0x00 0x00 0x00 0x0c 0x7d 0x5c    ......}\
##### DEBUG DECIMAL
             45  125    1   45   45    0   94  145
             86   29   13   91    0  106  130   23
             29   13   16   80   13   45  106    0
             12    0    0    0    0   12  125   92
#### RECORD 0 BolusWizard 2013-06-28T13:33:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-06-28T13:33:58)
    0000   0x7a 0xa1 0x0d 0x1c 0x0d                   z....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0xff 0x2e 0xf0    <P.-j...
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             60   80   13   45  106  255   46  240
              0    0    0   45  125
    HOUR BITS: [1, 0, 1]
#### RECORD 1 Bolus 2013-06-28T13:33:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-06-28T13:33:58)
    0000   0x7a 0xa1 0x4d 0x1c 0x0d                   z.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2013-06-28T15:45:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-06-28T15:45:24)
    0000   0x58 0xad 0x2f 0x1c 0x0d                   X./..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 3 CalBGForPH 2013-06-28T22:03:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-06-28T22:03:00)
    0000   0x40 0x83 0x36 0x1c 0x0d                   @.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 CalBGForPH 2013-06-28T22:11:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-06-28T22:11:40)
    0000   0x68 0x8b 0x36 0x1c 0x0d                   h.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 BolusWizard 2013-06-28T22:11:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-06-28T22:11:52)
    0000   0x74 0x8b 0x16 0x1c 0x0d                   t....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x02 0x21 0x00    +P.-j.!.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             43   80   13   45  106    2   33    0
              0    0    0   35  125
    HOUR BITS: [1, 0, 0]
#### RECORD 6 Bolus 2013-06-28T22:11:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-06-28T22:11:52)
    0000   0x74 0x8b 0x56 0x1c 0x0d                   t.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 ResultTotals (2013, 4, 28, 13, 13, 60) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xb4                   .....
    decimal
              7    0    0    4  180
    datetime ((2013, 4, 28, 13, 13, 60))
    0000   0x7c 0x0d 0x6d 0x7c 0x0d                   |.m|.
    body (51)
    hex
    0000   0x05 0x00 0x7a 0x68 0x88 0x04 0x00 0x00    ..zh....
    0008   0x04 0xb4 0x03 0x74 0x49 0x01 0x40 0x1b    ...tI.@.
    0010   0x00 0x67 0x01 0x40 0x1b 0x01 0x38 0x61    .g.@..8a
    0018   0x00 0x08 0x03 0x00 0x00 0x00 0x02 0x01    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x0d 0x6e 0xab 0x28 0x1d 0x8d    ...n.(..
    0030   0x5b 0x0d 0x70                             [.p
    decimal
              5    0  122  104  136    4    0    0
              4  180    3  116   73    1   64   27
              0  103    1   64   27    1   56   97
              0    8    3    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0   10   13  110  171   40   29  141
             91   13  112
    DAY BITS: [0, 1, 1]
#### RECORD 8 Base (2013, 0, 17, 0, 13, 29) head[2], body[0] op[0xab]

    op hex (2)
    0000   0xab 0x08                                  ..
    decimal
            171    8
    datetime ((2013, 0, 17, 0, 13, 29))
    0000   0x1d 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 9 Base (2000, 0, 0, 0, 0, 32) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 32))
    0000   0x20 0x00 0x00 0x00 0x00                    ....
    body (0)

#### RECORD 10 Base (2013, 4, 21, 8, 52, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x20                                  . 
    decimal
              0   32
    datetime ((2013, 4, 21, 8, 52, 61))
    0000   0x7d 0x34 0xc8 0x75 0xad                   }4.u.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 11 ChangeBasalProfile (2000, 0, 0, 0, 1, 13) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x1d                                  ..
    decimal
              8   29
    datetime ((2000, 0, 0, 0, 1, 13))
    0000   0x0d 0x01 0x20 0x20 0x00                   ..  .
    body (44)
    hex
    0000   0x70 0xab 0x48 0x1d 0x0d 0x5b 0x00 0x6c    p.H..[.l
    0008   0xb7 0x0c 0x1d 0x0d 0x12 0x50 0x0d 0x2d    .....P.-
    0010   0x6a 0x00 0x0d 0x00 0x00 0x00 0x00 0x0d    j.......
    0018   0x7d 0x5c 0x08 0x74 0xfb 0x04 0x0c 0x05    }\.t....
    0020   0x14 0x01 0x0d 0x0d 0x00 0x6d 0xb7 0x4c    .....m.L
    0028   0x1d 0x0d 0x34 0x64                        ..4d
    decimal
            112  171   72   29   13   91    0  108
            183   12   29   13   18   80   13   45
            106    0   13    0    0    0    0   13
            125   92    8  116  251    4   12    5
             20    1   13   13    0  109  183   76
             29   13   52  100
    DAY BITS: [0, 0, 1]
#### RECORD 12 Base (2008, 0, 10, 13, 29, 17) head[2], body[0] op[0x49]

    op hex (2)
    0000   0x49 0x83                                  I.
    decimal
             73  131
    datetime ((2008, 0, 10, 13, 29, 17))
    0000   0x11 0x1d 0x0d 0x0a 0x88                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 13 ChangeUtility (2008, 0, 27, 13, 29, 54) head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x90                                  c.
    decimal
             99  144
    datetime ((2008, 0, 27, 13, 29, 54))
    0000   0x36 0x1d 0x0d 0x5b 0x88                   6..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 14 Base (2000, 0, 24, 13, 29, 22) head[2], body[0] op[0x5e]

    op hex (2)
    0000   0x5e 0x91                                  ^.
    decimal
             94  145
    datetime ((2000, 0, 24, 13, 29, 22))
    0000   0x16 0x1d 0x0d 0x38 0x50                   ...8P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 15 Base (2000, 4, 0, 11, 2, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 11, 2, 42))
    0000   0x6a 0x02 0x2b 0x00 0x00                   j.+..
    body (0)

`end logs/ReadHistoryData-page-8.data: 16 records`
