## START logs/ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 294, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x22 0x64 0xf5 0x31 0x04 0x0d 0x03 0x00    "d.1....
    0008   0x05 0x00 0x05 0x43 0xf6 0x11 0x04 0x0d    ...C....
    0010   0x5b 0x00 0x5d 0xc3 0x13 0x04 0x0d 0x23    [.]....#
    0018   0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00 0x00    P.-j....
##### DEBUG DECIMAL
             34  100  245   49    4   13    3    0
              5    0    5   67  246   17    4   13
             91    0   93  195   19    4   13   35
             80   13   45  106    0   26    0    0
#### RECORD 0 CalBGForPH 2013-07-02T16:32:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2013-07-02T16:32:34)
    0000   0x62 0xe0 0x30 0x02 0x0d                   b.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 CalBGForPH 2013-07-02T17:11:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-07-02T17:11:08)
    0000   0x48 0xcb 0x31 0x02 0x0d                   H.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 CalBGForPH 2013-07-02T21:44:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-07-02T21:44:22)
    0000   0x56 0xec 0x35 0x02 0x0d                   V.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 BolusWizard 2013-07-02T21:44:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 115,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-07-02T21:44:58)
    0000   0x7a 0xec 0x15 0x02 0x0d                   z....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x00 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             65   80   13   45  106    0   50    0
              0    0    0   50  125
    HOUR BITS: [1, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 114, 'amount': 0.1, 'curve': 21}]
```
    op hex (5)
    0000   0x5c 0x05 0x04 0x72 0x15                   \..r.
    decimal
             92    5    4  114   21
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-07-02T21:44:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-07-02T21:44:58)
    0000   0x7a 0xec 0x55 0x02 0x0d                   z.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 CalBGForPH 2013-07-02T22:40:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-07-02T22:40:42)
    0000   0x6a 0xe8 0x36 0x02 0x0d                   j.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 ResultTotals 2013-06-02T13:13:34 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x40                   ....@
    decimal
              7    0    0    5   64
    datetime (2013-06-02T13:13:34)
    0000   0x62 0x8d 0x6d 0x62 0x8d                   b.mb.
    body (51)
    hex
    0000   0x05 0x00 0xa3 0x6c 0xea 0x06 0x00 0x00    ...l....
    0008   0x05 0x40 0x03 0x74 0x42 0x01 0xcc 0x22    .@.tB.."
    0010   0x00 0x8d 0x01 0xcc 0x22 0x01 0xb0 0x5e    ...."..^
    0018   0x00 0x1c 0x06 0x00 0x00 0x00 0x02 0x01    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x34 0xc8 0x71 0xd5 0x0b 0x03 0x0d    .4.q....
    0030   0x1e 0x00 0x43                             ..C
    decimal
              5    0  163  108  234    6    0    0
              5   64    3  116   66    1  204   34
              0  141    1  204   34    1  176   94
              0   28    6    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0   52  200  113  213   11    3   13
             30    0   67
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 Base (2000, 0, 0, 31, 13, 3) head[2], body[0] op[0xdb]

    op hex (2)
    0000   0xdb 0x0e                                  ..
    decimal
            219   14
    datetime ((2000, 0, 0, 31, 13, 3))
    0000   0x03 0x0d 0x1f 0x00 0x70                   ....p
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 9 Base (2008, 0, 31, 10, 13, 3) head[2], body[0] op[0xea]

    op hex (2)
    0000   0xea 0x0e                                  ..
    decimal
            234   14
    datetime ((2008, 0, 31, 10, 13, 3))
    0000   0x03 0x0d 0x0a 0xff 0x78                   ....x
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 10 Base (2003, 0, 31, 27, 13, 3) head[2], body[0] op[0xe5]

    op hex (2)
    0000   0xe5 0x31                                  .1
    decimal
            229   49
    datetime ((2003, 0, 31, 27, 13, 3))
    0000   0x03 0x0d 0x5b 0xff 0x43                   ..[.C
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 11 Base (2013, 0, 16, 0, 13, 3) head[2], body[0] op[0xe6]

    op hex (2)
    0000   0xe6 0x11                                  ..
    decimal
            230   17
    datetime ((2013, 0, 16, 0, 13, 3))
    0000   0x03 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 Base (2000, 0, 0, 0, 0, 28) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 28))
    0000   0x1c 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 13 Base (2000, 4, 29, 29, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2000, 4, 29, 29, 1, 61))
    0000   0x7d 0x01 0x1d 0x1d 0x00                   }....
    body (0)

#### RECORD 14 Base (2004, 4, 20, 13, 3, 17) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0xe6                                  C.
    decimal
             67  230
    datetime ((2004, 4, 20, 13, 3, 17))
    0000   0x51 0x03 0x0d 0x34 0x64                   Q..4d
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 15 Base (2010, 0, 10, 13, 3, 18) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0xe9                                  C.
    decimal
             67  233
    datetime ((2010, 0, 10, 13, 3, 18))
    0000   0x12 0x03 0x0d 0x0a 0x6a                   ....j
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 16 Base (2010, 0, 27, 13, 3, 54) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0xf1                                  H.
    decimal
             72  241
    datetime ((2010, 0, 27, 13, 3, 54))
    0000   0x36 0x03 0x0d 0x5b 0x6a                   6..[j
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 17 Ian54 (2000, 0, 17, 13, 3, 22) head[2], body[57] op[0x54]

    op hex (2)
    0000   0x54 0xf1                                  T.
    decimal
             84  241
    datetime ((2000, 0, 17, 13, 3, 22))
    0000   0x16 0x03 0x0d 0x31 0x50                   ...1P
    body (57)
    hex
    0000   0x0d 0x2d 0x6a 0x00 0x25 0x00 0x00 0x00    .-j.%...
    0008   0x00 0x25 0x7d 0x5c 0x05 0x74 0x3b 0x14    .%}\.t;.
    0010   0x01 0x25 0x25 0x00 0x54 0xf1 0x56 0x03    .%%.T.V.
    0018   0x0d 0x07 0x00 0x00 0x04 0x82 0x63 0x8d    ......c.
    0020   0x6d 0x63 0x8d 0x05 0x00 0xb5 0x6a 0xff    mc....j.
    0028   0x02 0x00 0x00 0x04 0x82 0x03 0x7a 0x4d    ......zM
    0030   0x01 0x08 0x17 0x00 0x31 0x01 0x08 0x17    ....1...
    0038   0x00                                       .
    decimal
             13   45  106    0   37    0    0    0
              0   37  125   92    5  116   59   20
              1   37   37    0   84  241   86    3
             13    7    0    0    4  130   99  141
            109   99  141    5    0  181  106  255
              2    0    0    4  130    3  122   77
              1    8   23    0   49    1    8   23
              0
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 18 Base (2000, 1, 0, 12, 52, 0) head[2], body[0] op[0x94]

    op hex (2)
    0000   0x94 0x38                                  .8
    decimal
            148   56
    datetime ((2000, 1, 0, 12, 52, 0))
    0000   0x00 0x74 0x2c 0x00 0x00                   .t,..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 19 Base (2012, 0, 0, 0, 1, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x02                                  ..
    decimal
              0    2
    datetime ((2012, 0, 0, 0, 1, 1))
    0000   0x01 0x01 0x00 0x00 0x0c                   .....
    body (0)

#### RECORD 20 Base (2000, 0, 30, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xe8                                  ..
    decimal
              0  232
    datetime ((2000, 0, 30, 0, 0, 0))
    0000   0x00 0x00 0x00 0x1e 0x00                   .....
    body (0)

#### RECORD 21 Base (2000, 0, 31, 13, 4, 17) head[2], body[0] op[0x52]

    op hex (2)
    0000   0x52 0xdf                                  R.
    decimal
             82  223
    datetime ((2000, 0, 31, 13, 4, 17))
    0000   0x11 0x04 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 22 Base (2000, 0, 1, 13, 4, 17) head[2], body[0] op[0x4e]

    op hex (2)
    0000   0x4e 0xf4                                  N.
    decimal
             78  244
    datetime ((2000, 0, 1, 13, 4, 17))
    0000   0x11 0x04 0x0d 0x21 0x00                   ...!.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 23 Base (2000, 0, 3, 13, 4, 17) head[2], body[0] op[0x52]

    op hex (2)
    0000   0x52 0xf4                                  R.
    decimal
             82  244
    datetime ((2000, 0, 3, 13, 4, 17))
    0000   0x11 0x04 0x0d 0x03 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-7.data: 24 records`
