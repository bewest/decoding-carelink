## START logs/ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 636, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x06 0x7d 0x5c 0x0b 0x10 0x14 0x14 0x9a    .}\.....
    0008   0x50 0x14 0x0e 0x5a 0x14 0x01 0x06 0x06    P..Z....
    0010   0x00 0x60 0x28 0x52 0x0b 0x0d 0x0a 0x80    .`(R....
    0018   0x5e 0x3a 0x33 0x0b 0x0d 0x0a 0x80 0x6e    ^:3....n
##### DEBUG DECIMAL
              6  125   92   11   16   20   20  154
             80   20   14   90   20    1    6    6
              0   96   40   82   11   13   10  128
             94   58   51   11   13   10  128  110
#### RECORD 0 Prime 2013-04-09T20:12:46 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-09T20:12:46)
    0000   0x6e 0x0c 0x14 0x09 0x0d                   n....
    body (0)

#### RECORD 1 CalBGForPH 2013-04-09T20:15:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 230}
```
    op hex (2)
    0000   0x0a 0xe6                                  ..
    decimal
             10  230
    datetime (2013-04-09T20:15:05)
    0000   0x45 0x0f 0x34 0x09 0x0d                   E.4..
    body (0)

#### RECORD 2 BolusWizard 2013-04-09T20:15:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 230,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 2.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe6                                  [.
    decimal
             91  230
    datetime (2013-04-09T20:15:28)
    0000   0x5c 0x0f 0x14 0x09 0x0d                   \....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x17 0x1c 0x00    %P.-j...
    0008   0x00 0x16 0x00 0x1d 0x7d                   ....}
    decimal
             37   80   13   45  106   23   28    0
              0   22    0   29  125

#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 2.0, 'curve': 4},
 {'age': 131, 'amount': 0.5, 'curve': 4},
 {'age': 5, 'amount': 2.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x15 0x04 0x14 0x83 0x04    \.P.....
    0008   0x68 0x05 0x14                             h..
    decimal
             92   11   80   21    4   20  131    4
            104    5   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-04-09T20:15:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-04-09T20:15:28)
    0000   0x5c 0x0f 0x54 0x09 0x0d                   \.T..
    body (0)

#### RECORD 5 ResultTotals 2013-04-09T13:13:09 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xac                   .....
    decimal
              7    0    0    4  172
    datetime (2013-04-09T13:13:09)
    0000   0x49 0x0d 0x6d 0x49 0x0d                   I.mI.
    body (51)
    hex
    0000   0x05 0x00 0xc8 0x5b 0xf7 0x05 0x00 0x00    ...[....
    0008   0x04 0xac 0x03 0x6c 0x49 0x01 0x40 0x1b    ...lI.@.
    0010   0x00 0x4c 0x01 0x40 0x1b 0x00 0xd8 0x43    .L.@...C
    0018   0x00 0x68 0x21 0x00 0x00 0x00 0x04 0x01    .h!.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x50 0x34 0x0c 0x0a 0x0d    ...P4...
    0030   0x1f 0x00 0x54                             ..T
    decimal
              5    0  200   91  247    5    0    0
              4  172    3  108   73    1   64   27
              0   76    1   64   27    0  216   67
              0  104   33    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0   30    0   80   52   12   10   13
             31    0   84
    DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2008, 0, 8, 10, 13, 10) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x0d                                  ..
    decimal
             15   13
    datetime ((2008, 0, 8, 10, 13, 10))
    0000   0x0a 0x0d 0x0a 0x48 0x78                   ...Hx
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 7 Battery (2011, 0, 8, 27, 13, 10) head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x2e                                  ..
    decimal
             26   46
    datetime ((2011, 0, 8, 27, 13, 10))
    0000   0x0a 0x0d 0x5b 0x48 0x5b                   ..[H[
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 8 Base (2013, 0, 16, 27, 13, 10) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x0e                                  ..
    decimal
             27   14
    datetime ((2013, 0, 16, 27, 13, 10))
    0000   0x0a 0x0d 0x3b 0x50 0x0d                   ..;P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 9 Base (2000, 12, 0, 16, 45, 56) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 45, 56))
    0000   0xf8 0x2d 0xf0 0x00 0x00                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 10 Base (2000, 4, 5, 5, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x25                                  .%
    decimal
              0   37
    datetime ((2000, 4, 5, 5, 1, 61))
    0000   0x7d 0x01 0x25 0x25 0x00                   }.%%.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 11 BolusWizard 2004-04-10T13:10:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 91,
 '_byte[7]': 72,
 'bg': 1819,
 'bg_target_high': 0,
 'bg_target_low': 13,
 'bolus_estimate': 1.3,
 'carb_input': 120,
 'carb_ratio': 47,
 'correction_estimate': 8.3,
 'food_estimate': 22.8,
 'sensitivity': 10,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.5,
 'unknown_byte[10]': 10,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x1b                                  [.
    decimal
             91   27
    datetime (2004-04-10T13:10:14)
    0000   0x4e 0x0a 0x0d 0x0a 0xe4                   N....
    body (13)
    hex
    0000   0x78 0x37 0x2f 0x0a 0x0d 0x5b 0xe4 0x48    x7/..[.H
    0008   0x38 0x0f 0x0a 0x0d 0x00                   8....
    decimal
            120   55   47   10   13   91  228   72
             56   15   10   13    0
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 12 Ian50 (2000, 1, 0, 22, 42, 45) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime ((2000, 1, 0, 22, 42, 45))
    0000   0x2d 0x6a 0x16 0x00 0x00                   -j...
    body (34)
    hex
    0000   0x00 0x18 0x00 0x00 0x7d 0x5c 0x05 0x94    ....}\..
    0008   0x5c 0x04 0x01 0x02 0x02 0x00 0x48 0x38    \.....H8
    0010   0x4f 0x0a 0x0d 0x0a 0xe0 0x49 0x07 0x31    O....I.1
    0018   0x0a 0x0d 0x5b 0xe0 0x4c 0x07 0x11 0x0a    ..[.L...
    0020   0x0d 0x00                                  ..
    decimal
              0   24    0    0  125   92    5  148
             92    4    1    2    2    0   72   56
             79   10   13   10  224   73    7   49
             10   13   91  224   76    7   17   10
             13    0
    HOUR BITS: [0, 1, 1]
#### RECORD 13 Ian50 (2000, 1, 0, 22, 42, 45) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime ((2000, 1, 0, 22, 42, 45))
    0000   0x2d 0x6a 0x16 0x00 0x00                   -j...
    body (34)
    hex
    0000   0x00 0x0b 0x00 0x0b 0x7d 0x5c 0x08 0x08    ....}\..
    0008   0x49 0x04 0x94 0xa3 0x04 0x01 0x0d 0x0d    I.......
    0010   0x00 0x4d 0x07 0x51 0x0a 0x0d 0x0a 0x96    .M.Q....
    0018   0x6d 0x1a 0x32 0x0a 0x0d 0x0a 0x8e 0x50    m.2....P
    0020   0x28 0x32                                  (2
    decimal
              0   11    0   11  125   92    8    8
             73    4  148  163    4    1   13   13
              0   77    7   81   10   13   10  150
            109   26   50   10   13   10  142   80
             40   50
    HOUR BITS: [0, 1, 1]
#### RECORD 14 CalBGForPH 2002-06-08T06:14:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2002-06-08T06:14:27)
    0000   0x5b 0x8e 0x66 0x28 0x12                   [.f(.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 15 CalBGForPH 2010-01-13T13:16:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2010-01-13T13:16:13)
    0000   0x0d 0x50 0x0d 0x2d 0x6a                   .P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 16 Prime (2011, 0, 28, 29, 10, 0) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x0a 0x00 0x00 0x09                   .....
    decimal
              3   10    0    0    9
    datetime ((2011, 0, 28, 29, 10, 0))
    0000   0x00 0x0a 0x7d 0x5c 0x0b                   ..}\.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 17 LowReservoir (2004, 0, 4, 6, 8, 4) head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 9.6}
```
    op hex (2)
    0000   0x34 0x60                                  4`
    decimal
             52   96
    datetime ((2004, 0, 4, 6, 8, 4))
    0000   0x04 0x08 0xa6 0x04 0x94                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 18 Base (2006, 0, 0, 10, 10, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x14                                  ..
    decimal
              0   20
    datetime ((2006, 0, 0, 10, 10, 1))
    0000   0x01 0x0a 0x0a 0x00 0x66                   ....f
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 Base (2011, 0, 1, 10, 13, 10) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x52                                  (R
    decimal
             40   82
    datetime ((2011, 0, 1, 10, 13, 10))
    0000   0x0a 0x0d 0x0a 0x21 0x6b                   ...!k
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 20 Base (2012, 2, 1, 27, 13, 10) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x34                                  .4
    decimal
             17   52
    datetime ((2012, 2, 1, 27, 13, 10))
    0000   0x0a 0x8d 0x5b 0x21 0x6c                   ..[!l
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 21 Base (2013, 0, 17, 0, 13, 10) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x14                                  ..
    decimal
             17   20
    datetime ((2013, 0, 17, 0, 13, 10))
    0000   0x0a 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 22 Base (2008, 0, 0, 0, 0, 36) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2008, 0, 0, 0, 0, 36))
    0000   0x24 0x00 0x00 0x00 0x08                   $....
    body (0)

#### RECORD 23 Base (2007, 5, 8, 14, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2007, 5, 8, 14, 28, 61))
    0000   0x7d 0x5c 0x0e 0x28 0x67                   }\.(g
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 24 Base (2004, 12, 7, 8, 4, 1) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x34                                  .4
    decimal
              4   52
    datetime ((2004, 12, 7, 8, 4, 1))
    0000   0xc1 0x04 0x08 0x07 0x14                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 25 Base (2000, 0, 28, 28, 1, 20) head[2], body[0] op[0x94]

    op hex (2)
    0000   0x94 0x61                                  .a
    decimal
            148   97
    datetime ((2000, 0, 28, 28, 1, 20))
    0000   0x14 0x01 0x1c 0x1c 0x00                   .....
    body (0)

#### RECORD 26 Base (2007, 4, 10, 13, 10, 20) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x11                                  l.
    decimal
            108   17
    datetime ((2007, 4, 10, 13, 10, 20))
    0000   0x54 0x0a 0x0d 0x0a 0x77                   T...w
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 27 Base (2015, 0, 10, 13, 10, 53) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x2b                                  l+
    decimal
            108   43
    datetime ((2015, 0, 10, 13, 10, 53))
    0000   0x35 0x0a 0x0d 0x0a 0x5f                   5..._
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 28 Ian69 (2015, 0, 27, 13, 10, 55) head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x07                                  i.
    decimal
            105    7
    datetime ((2015, 0, 27, 13, 10, 55))
    0000   0x37 0x0a 0x0d 0x5b 0x5f                   7..[_
    body (2)
    hex
    0000   0x46 0x08                                  F.
    decimal
             70    8
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 29 ChangeTime (2013, 0, 13, 16, 35, 13) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x0a                                  ..
    decimal
             23   10
    datetime ((2013, 0, 13, 16, 35, 13))
    0000   0x0d 0x23 0x50 0x0d 0x2d                   .#P.-
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 30 Base (2000, 3, 6, 0, 48, 26) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xfd                                  j.
    decimal
            106  253
    datetime ((2000, 3, 6, 0, 48, 26))
    0000   0x1a 0xf0 0x00 0x06 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 ChangeTime 2004-04-14T16:14:28 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x7d                                  .}
    decimal
             23  125
    datetime (2004-04-14T16:14:28)
    0000   0x5c 0x0e 0x70 0xae 0x04                   \.p..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 32 Base (2008, 0, 20, 12, 52, 20) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x12                                  (.
    decimal
             40   18
    datetime ((2008, 0, 20, 12, 52, 20))
    0000   0x14 0x34 0x6c 0x14 0x08                   .4l..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 Base (2007, 0, 0, 23, 23, 1) head[2], body[0] op[0xb2]

    op hex (2)
    0000   0xb2 0x14                                  ..
    decimal
            178   20
    datetime ((2007, 0, 0, 23, 23, 1))
    0000   0x01 0x17 0x17 0x00 0x47                   ....G
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 34 ChangeBasalProfile (2000, 0, 0, 7, 13, 10) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x57                                  .W
    decimal
              8   87
    datetime ((2000, 0, 0, 7, 13, 10))
    0000   0x0a 0x0d 0x07 0x00 0x00                   .....
    body (44)
    hex
    0000   0x05 0x38 0x4a 0x0d 0x6d 0x4a 0x0d 0x05    .8J.mJ..
    0008   0x10 0xa5 0x48 0x21 0x08 0x00 0x00 0x05    ..H!....
    0010   0x38 0x03 0x74 0x42 0x01 0xc4 0x22 0x00    8.tB..".
    0018   0x6b 0x01 0xc4 0x22 0x01 0x18 0x3e 0x00    k.."..>.
    0020   0xac 0x26 0x00 0x00 0x00 0x06 0x03 0x03    .&......
    0028   0x00 0x00 0x0c 0x00                        ....
    decimal
              5   56   74   13  109   74   13    5
             16  165   72   33    8    0    0    5
             56    3  116   66    1  196   34    0
            107    1  196   34    1   24   62    0
            172   38    0    0    0    6    3    3
              0    0   12    0

#### RECORD 35 Base (2003, 0, 22, 10, 0, 0) head[2], body[0] op[0xe8]

    op hex (2)
    0000   0xe8 0x00                                  ..
    decimal
            232    0
    datetime ((2003, 0, 22, 10, 0, 0))
    0000   0x00 0x00 0x0a 0x76 0x63                   ...vc
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 36 Base (2005, 2, 22, 27, 13, 11) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x27                                  .'
    decimal
             16   39
    datetime ((2005, 2, 22, 27, 13, 11))
    0000   0x0b 0x8d 0x5b 0x76 0x65                   ..[ve
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 37 Base (2013, 0, 17, 0, 13, 11) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x07                                  ..
    decimal
             16    7
    datetime ((2013, 0, 17, 0, 13, 11))
    0000   0x0b 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 38 Base (2000, 0, 0, 0, 0, 55) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 55))
    0000   0x37 0x00 0x00 0x00 0x00                   7....
    body (0)

#### RECORD 39 Base (2000, 4, 23, 23, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x37                                  .7
    decimal
              0   55
    datetime ((2000, 4, 23, 23, 1, 61))
    0000   0x7d 0x01 0x37 0x37 0x00                   }.77.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 40 Base (2000, 4, 30, 13, 11, 7) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x10                                  e.
    decimal
            101   16
    datetime ((2000, 4, 30, 13, 11, 7))
    0000   0x47 0x0b 0x0d 0x1e 0x00                   G....
    body (0)

#### RECORD 41 Base (2000, 0, 31, 13, 11, 8) head[2], body[0] op[0x76]

    op hex (2)
    0000   0x76 0x3a                                  v:
    decimal
            118   58
    datetime ((2000, 0, 31, 13, 11, 8))
    0000   0x08 0x0b 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 42 Ian54 (2005, 0, 10, 13, 11, 9) head[2], body[57] op[0x54]

    op hex (2)
    0000   0x54 0x1b                                  T.
    decimal
             84   27
    datetime ((2005, 0, 10, 13, 11, 9))
    0000   0x09 0x0b 0x0d 0x0a 0x85                   .....
    body (57)
    hex
    0000   0x68 0x0b 0x2b 0x0b 0x0d 0x0a 0x5a 0x6a    h.+...Zj
    0008   0x02 0x2d 0x0b 0x0d 0x0a 0x5e 0x4b 0x03    .-...^K.
    0010   0x2d 0x0b 0x0d 0x5b 0x5e 0x6d 0x03 0x0d    -..[^m..
    0018   0x0b 0x0d 0x3b 0x50 0x0d 0x2d 0x6a 0xfd    ..;P.-j.
    0020   0x2d 0xf0 0x00 0x00 0x00 0x2a 0x7d 0x5c    -....*}\
    0028   0x05 0xdc 0x5d 0x14 0x01 0x2a 0x2a 0x00    ..]..**.
    0030   0x6d 0x03 0x4d 0x0b 0x0d 0x0a 0x4b 0x6a    m.M...Kj
    0038   0x0b                                       .
    decimal
            104   11   43   11   13   10   90  106
              2   45   11   13   10   94   75    3
             45   11   13   91   94  109    3   13
             11   13   59   80   13   45  106  253
             45  240    0    0    0   42  125   92
              5  220   93   20    1   42   42    0
            109    3   77   11   13   10   75  106
             11
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 Base (2012, 0, 4, 11, 10, 13) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0x0b                                  ..
    decimal
             46   11
    datetime ((2012, 0, 4, 11, 10, 13))
    0000   0x0d 0x0a 0x4b 0x64 0x0c                   ..Kd.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 44 Base (2012, 1, 23, 11, 27, 13) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0x0b                                  ..
    decimal
             46   11
    datetime ((2012, 1, 23, 11, 27, 13))
    0000   0x0d 0x5b 0x4b 0x77 0x0c                   .[Kw.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 45 Base (2013, 0, 13, 16, 15, 13) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x0b                                  ..
    decimal
             14   11
    datetime ((2013, 0, 13, 16, 15, 13))
    0000   0x0d 0x0f 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 46 Base (2000, 3, 1, 0, 48, 11) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xf9                                  j.
    decimal
            106  249
    datetime ((2000, 3, 1, 0, 48, 11))
    0000   0x0b 0xf0 0x00 0x21 0x00                   ...!.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 0, 1]
#### RECORD 47 Base (2004, 4, 4, 26, 11, 28) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x7d                                  .}
    decimal
              4  125
    datetime ((2004, 4, 4, 26, 11, 28))
    0000   0x5c 0x0b 0x9a 0x44 0x04                   \..D.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 48 Base (2001, 3, 20, 2, 28, 4) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x4e                                  .N
    decimal
             14   78
    datetime ((2001, 3, 20, 2, 28, 4))
    0000   0x04 0xdc 0xa2 0x14 0x01                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 Base (2011, 1, 14, 12, 55, 0) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x04                                  ..
    decimal
              4    4
    datetime ((2011, 1, 14, 12, 55, 0))
    0000   0x00 0x77 0x0c 0x4e 0x0b                   .w.N.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 50 Base (2011, 9, 18, 8, 29, 27) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2011, 9, 18, 8, 29, 27))
    0000   0x9b 0x5d 0x28 0x32 0x0b                   .](2.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
#### RECORD 51 Base (2011, 9, 18, 8, 32, 27) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2011, 9, 18, 8, 32, 27))
    0000   0x9b 0x60 0x28 0x12 0x0b                   .`(..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 52 Base (2006, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2006, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x06                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-28.data: 53 records`
