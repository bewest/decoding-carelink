## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 159, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x12 0x7d 0x5c 0x05 0x94 0x20 0x04 0x01    .}\.. ..
    0008   0x12 0x12 0x00 0x41 0x78 0x52 0x02 0x0d    ...AxR..
    0010   0x5b 0x00 0x65 0x4a 0x13 0x02 0x0d 0x1c    [.eJ....
    0018   0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00 0x00    P.-j....
##### DEBUG DECIMAL
             18  125   92    5  148   32    4    1
             18   18    0   65  120   82    2   13
             91    0  101   74   19    2   13   28
             80   13   45  106    0   21    0    0
#### RECORD 0 BolusWizard 2013-05-01T19:02:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.1,
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
    datetime (2013-05-01T19:02:25)
    0000   0x59 0x42 0x13 0x01 0x0d                   YB...
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125
    HOUR BITS: [0, 1, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.8, 'curve': 4},
 {'age': 98, 'amount': 0.8, 'curve': 4},
 {'age': 208, 'amount': 0.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x30 0x04 0x20 0x62 0x04    \.p0. b.
    0008   0x20 0xd0 0x04                              ..
    decimal
             92   11  112   48    4   32   98    4
             32  208    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-05-01T19:02:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-05-01T19:02:25)
    0000   0x59 0x42 0x53 0x01 0x0d                   YBS..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 ResultTotals 2013-06-01T13:13:01 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xb8                   .....
    decimal
              7    0    0    4  184
    datetime (2013-06-01T13:13:01)
    0000   0x41 0x8d 0x6d 0x41 0x8d                   A.mA.
    body (51)
    hex
    0000   0x05 0x00 0x92 0x46 0xf7 0x06 0x00 0x00    ...F....
    0008   0x04 0xb8 0x03 0x78 0x4a 0x01 0x40 0x1a    ...xJ.@.
    0010   0x00 0x54 0x01 0x40 0x1a 0x00 0xdc 0x45    .T.@...E
    0018   0x00 0x64 0x1f 0x00 0x00 0x00 0x05 0x04    .d......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x5e 0x46 0x11 0x02 0x0d    ...^F...
    0030   0x1f 0x00 0x47                             ..G
    decimal
              5    0  146   70  247    6    0    0
              4  184    3  120   74    1   64   26
              0   84    1   64   26    0  220   69
              0  100   31    0    0    0    5    4
              1    0    0   12    0  232    0    0
              0   30    0   94   70   17    2   13
             31    0   71
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 Base (2012, 0, 31, 10, 13, 2) head[2], body[0] op[0x5e]

    op hex (2)
    0000   0x5e 0x11                                  ^.
    decimal
             94   17
    datetime ((2012, 0, 31, 10, 13, 2))
    0000   0x02 0x0d 0x0a 0x5f 0x6c                   ..._l
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 5 Base (2008, 0, 31, 27, 13, 2) head[2], body[0] op[0x58]

    op hex (2)
    0000   0x58 0x32                                  X2
    decimal
             88   50
    datetime ((2008, 0, 31, 27, 13, 2))
    0000   0x02 0x0d 0x5b 0x5f 0x78                   ..[_x
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 6 Base (2013, 0, 16, 21, 13, 2) head[2], body[0] op[0x59]

    op hex (2)
    0000   0x59 0x12                                  Y.
    decimal
             89   18
    datetime ((2013, 0, 16, 21, 13, 2))
    0000   0x02 0x0d 0x35 0x50 0x0d                   ..5P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2000, 12, 0, 16, 40, 61) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 40, 61))
    0000   0xfd 0x28 0xf0 0x00 0x00                   .(...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 Base (2000, 4, 5, 5, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x25                                  .%
    decimal
              0   37
    datetime ((2000, 4, 5, 5, 1, 61))
    0000   0x7d 0x01 0x25 0x25 0x00                   }.%%.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 9 Base (2000, 4, 27, 13, 2, 18) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x59                                  xY
    decimal
            120   89
    datetime ((2000, 4, 27, 13, 2, 18))
    0000   0x52 0x02 0x0d 0x5b 0x00                   R..[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 10 Base (2000, 0, 24, 13, 2, 18) head[2], body[0] op[0x41]

    op hex (2)
    0000   0x41 0x78                                  Ax
    decimal
             65  120
    datetime ((2000, 0, 24, 13, 2, 18))
    0000   0x12 0x02 0x0d 0x18 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 11 Base (2000, 4, 0, 18, 0, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 18, 0, 42))
    0000   0x6a 0x00 0x12 0x00 0x00                   j....
    body (0)

`end logs/ReadHistoryData-page-21.data: 12 records`
