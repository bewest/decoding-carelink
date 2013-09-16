## START logs/ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 206, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0d 0x7d 0x5c 0x05 0x78 0x41 0x04 0x01    .}\.xA..
    0008   0x0d 0x0d 0x00 0x4d 0xf1 0x50 0x0a 0x0d    ...M.P..
    0010   0x0a 0x8f 0x6a 0xcc 0x32 0x0a 0x0d 0x0a    ..j.2...
    0018   0x68 0x77 0xef 0x33 0x0a 0x0d 0x07 0x00    hw.3....
##### DEBUG DECIMAL
             13  125   92    5  120   65    4    1
             13   13    0   77  241   80   10   13
             10  143  106  204   50   10   13   10
            104  119  239   51   10   13    7    0
#### RECORD 0 Prime 2013-07-09T16:01:42 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-09T16:01:42)
    0000   0x6a 0xc1 0x10 0x09 0x0d                   j....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 CalBGForPH 2013-07-09T16:29:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-07-09T16:29:30)
    0000   0x5e 0xdd 0x30 0x09 0x0d                   ^.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2013-07-09T16:29:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 14,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-07-09T16:29:36)
    0000   0x64 0xdd 0x10 0x09 0x0d                   d....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Bolus 2013-07-09T16:29:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-07-09T16:29:36)
    0000   0x64 0xdd 0x50 0x09 0x0d                   d.P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-09T22:04:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2013-07-09T22:04:59)
    0000   0x7b 0xc4 0x36 0x09 0x0d                   {.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BolusWizard 2013-07-09T22:05:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 94,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5e                                  [^
    decimal
             91   94
    datetime (2013-07-09T22:05:44)
    0000   0x6c 0xc5 0x16 0x09 0x0d                   l....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xfd 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             55   80   13   45  106  253   42  240
              0    0    0   39  125
    HOUR BITS: [1, 1, 0]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 1.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x55 0x14                   \.(U.
    decimal
             92    5   40   85   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-07-09T22:05:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-07-09T22:05:44)
    0000   0x6c 0xc5 0x56 0x09 0x0d                   l.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 ResultTotals 2013-06-09T13:13:41 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x3a                   ....:
    decimal
              7    0    0    4   58
    datetime (2013-06-09T13:13:41)
    0000   0x69 0x8d 0x6d 0x69 0x8d                   i.mi.
    body (51)
    hex
    0000   0x05 0x00 0x65 0x5e 0x6c 0x02 0x00 0x00    ..e^l...
    0008   0x04 0x3a 0x03 0x76 0x52 0x00 0xc4 0x12    .:.vR...
    0010   0x00 0x45 0x00 0xc4 0x12 0x00 0xc4 0x64    .E.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x4c 0xcf 0x0d 0x0a 0x0d    ...L....
    0030   0x1f 0x00 0x63                             ..c
    decimal
              5    0  101   94  108    2    0    0
              4   58    3  118   82    0  196   18
              0   69    0  196   18    0  196  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0   30    0   76  207   13   10   13
             31    0   99
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 Base (2010, 0, 19, 10, 13, 10) head[2], body[0] op[0xea]

    op hex (2)
    0000   0xea 0x0d                                  ..
    decimal
            234   13
    datetime ((2010, 0, 19, 10, 13, 10))
    0000   0x0a 0x0d 0x0a 0x93 0x7a                   ....z
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 10 Base (2007, 0, 19, 27, 13, 10) head[2], body[0] op[0xee]

    op hex (2)
    0000   0xee 0x2f                                  ./
    decimal
            238   47
    datetime ((2007, 0, 19, 27, 13, 10))
    0000   0x0a 0x0d 0x5b 0x93 0x47                   ..[.G
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 11 Base (2013, 0, 16, 2, 13, 10) head[2], body[0] op[0xef]

    op hex (2)
    0000   0xef 0x0f                                  ..
    decimal
            239   15
    datetime ((2013, 0, 16, 2, 13, 10))
    0000   0x0a 0x0d 0x22 0x50 0x0d                   .."P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 Base (2000, 0, 0, 0, 26, 4) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 26, 4))
    0000   0x04 0x1a 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 13 Base (2000, 4, 30, 30, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1e                                  ..
    decimal
              0   30
    datetime ((2000, 4, 30, 30, 1, 61))
    0000   0x7d 0x01 0x1e 0x1e 0x00                   }....
    body (0)

#### RECORD 14 Base (2000, 4, 27, 13, 10, 15) head[2], body[0] op[0x47]

    op hex (2)
    0000   0x47 0xef                                  G.
    decimal
             71  239
    datetime ((2000, 4, 27, 13, 10, 15))
    0000   0x4f 0x0a 0x0d 0x5b 0x00                   O..[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 15 Base (2000, 0, 18, 13, 10, 16) head[2], body[0] op[0x4d]

    op hex (2)
    0000   0x4d 0xf1                                  M.
    decimal
             77  241
    datetime ((2000, 0, 18, 13, 10, 16))
    0000   0x10 0x0a 0x0d 0x12 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 16 Base (2000, 4, 0, 13, 0, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 13, 0, 42))
    0000   0x6a 0x00 0x0d 0x00 0x00                   j....
    body (0)

`end logs/ReadHistoryData-page-6.data: 17 records`
