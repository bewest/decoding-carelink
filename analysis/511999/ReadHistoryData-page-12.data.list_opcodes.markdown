## START logs/ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 245, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x64 0x00 0x30 0x78 0x5c 0x20 0x40 0x25    d.0x\ @%
    0008   0xc0 0x2c 0x2f 0xc0 0x14 0x75 0xc0 0x1c    .,/..u..
    0010   0xcf 0xc0 0x20 0xed 0xc0 0x20 0xf7 0xc0    .. .. ..
    0018   0x34 0x0b 0xd0 0x54 0x3d 0xd0 0x18 0x6f    4..T=..o
##### DEBUG DECIMAL
            100    0   48  120   92   32   64   37
            192   44   47  192   20  117  192   28
            207  192   32  237  192   32  247  192
             52   11  208   84   61  208   24  111
#### RECORD 0 Bolus (2012, 0, 0, 20, 0, 28) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x1c 0x00                        ....
    decimal
              1    0   28    0
    datetime ((2012, 0, 0, 20, 0, 28))
    0000   0x1c 0x00 0x74 0x00 0xac                   ..t..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 1 ResultTotals 2008-10-17T07:47:57 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x50 0x08 0x0d 0x0a                   .P...
    decimal
              7   80    8   13   10
    datetime (2008-10-17T07:47:57)
    0000   0xb9 0xaf 0x27 0x31 0x08                   ..'1.
    body (41)
    hex
    0000   0x0d 0x5b 0xb9 0xb3 0x27 0x11 0x08 0x0d    .[..'...
    0008   0x00 0x50 0x00 0x64 0x3c 0x64 0x28 0x00    .P.d<d(.
    0010   0x00 0x00 0x00 0x20 0x00 0x08 0x78 0x5c    ... ..x\
    0018   0x1a 0x1c 0x60 0xc0 0x20 0x7e 0xc0 0x20    ..`. ~. 
    0020   0x88 0xc0 0x34 0x9c 0xc0 0x54 0xce 0xc0    ..4..T..
    0028   0x18                                       .
    decimal
             13   91  185  179   39   17    8   13
              0   80    0  100   60  100   40    0
              0    0    0   32    0    8  120   92
             26   28   96  192   32  126  192   32
            136  192   52  156  192   84  206  192
             24
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 0, 1]
#### RECORD 2 Base (2010, 1, 16, 16, 36, 52) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xd0                                  ..
    decimal
              0  208
    datetime ((2010, 1, 16, 16, 36, 52))
    0000   0x34 0x64 0xd0 0x30 0xaa                   4d.0.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 3 Base (2000, 0, 20, 0, 20, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 0, 20, 0, 20, 0))
    0000   0x00 0x14 0x00 0x14 0x00                   .....
    body (0)

#### RECORD 4 Base (2013, 8, 8, 17, 39, 51) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2013, 8, 8, 17, 39, 51))
    0000   0xb3 0x27 0x51 0x08 0x0d                   .'Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 CalBGForPH 2013-08-08T18:45:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-08T18:45:32)
    0000   0xa0 0x2d 0x32 0x08 0x0d                   .-2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 BolusWizard 2013-08-08T18:45:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-08T18:45:37)
    0000   0xa5 0x2d 0x12 0x08 0x0d                   .-...
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x2c 0x00 0x00 0x10 0x00 0x2c 0x78         ,....,x
    decimal
             11   80    0  100   60  100    0    0
             44    0    0   16    0   44  120
    HOUR BITS: [0, 0, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 0.5, 'curve': 192},
 {'age': 162, 'amount': 0.7, 'curve': 192},
 {'age': 192, 'amount': 0.8, 'curve': 192},
 {'age': 202, 'amount': 0.8, 'curve': 192},
 {'age': 222, 'amount': 1.3, 'curve': 192},
 {'age': 16, 'amount': 2.1, 'curve': 208},
 {'age': 66, 'amount': 0.6, 'curve': 208},
 {'age': 166, 'amount': 1.3, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x14 0x48 0xc0 0x1c 0xa2 0xc0    \..H....
    0008   0x20 0xc0 0xc0 0x20 0xca 0xc0 0x34 0xde     .. ..4.
    0010   0xc0 0x54 0x10 0xd0 0x18 0x42 0xd0 0x34    .T...B.4
    0018   0xa6 0xd0                                  ..
    decimal
             92   26   20   72  192   28  162  192
             32  192  192   32  202  192   52  222
            192   84   16  208   24   66  208   52
            166  208
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus (2005, 0, 0, 16, 0, 44) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x2c 0x00                        ..,.
    decimal
              1    0   44    0
    datetime ((2005, 0, 0, 16, 0, 44))
    0000   0x2c 0x00 0x10 0x00 0xa5                   ,....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 9 Base (2013, 0, 21, 10, 13, 8) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x52                                  -R
    decimal
             45   82
    datetime ((2013, 0, 21, 10, 13, 8))
    0000   0x08 0x0d 0x0a 0x95 0xad                   .....
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 10 Base (2004, 0, 21, 27, 13, 8) head[2], body[0] op[0x35]

    op hex (2)
    0000   0x35 0x32                                  52
    decimal
             53   50
    datetime ((2004, 0, 21, 27, 13, 8))
    0000   0x08 0x0d 0x5b 0x95 0xb4                   ..[..
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 11 Base (2000, 0, 16, 16, 13, 8) head[2], body[0] op[0x35]

    op hex (2)
    0000   0x35 0x12                                  5.
    decimal
             53   18
    datetime ((2000, 0, 16, 16, 13, 8))
    0000   0x08 0x0d 0x10 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 ChangeTimeDisplay (2000, 4, 0, 0, 16, 36) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime ((2000, 4, 0, 0, 16, 36))
    0000   0x64 0x10 0x00 0x40 0x00                   d..@.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 13 Base (2013, 1, 28, 24, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x3c                                  .<
    decimal
              0   60
    datetime ((2013, 1, 28, 24, 0, 0))
    0000   0x00 0x40 0x78 0x5c 0x1d                   .@x\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 14 Base (2012, 12, 0, 16, 20, 0) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x0a                                  ,.
    decimal
             44   10
    datetime ((2012, 12, 0, 16, 20, 0))
    0000   0xc0 0x14 0x50 0xc0 0x1c                   ..P..
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 15 Base (2002, 3, 0, 0, 8, 32) head[2], body[0] op[0xaa]

    op hex (2)
    0000   0xaa 0xc0                                  ..
    decimal
            170  192
    datetime ((2002, 3, 0, 0, 8, 32))
    0000   0x20 0xc8 0xc0 0x20 0xd2                    .. .
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 16 Base (2000, 15, 24, 20, 0, 38) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x34                                  .4
    decimal
            192   52
    datetime ((2000, 15, 24, 20, 0, 38))
    0000   0xe6 0xc0 0x54 0x18 0xd0                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 17 NewTimeSet 2001-12-16T14:52:16 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x4a                                  .J
    decimal
             24   74
    datetime (2001-12-16T14:52:16)
    0000   0xd0 0x34 0xae 0xd0 0x01                   .4...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0]
#### RECORD 18 Base (2000, 1, 28, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x40                                  .@
    decimal
              0   64
    datetime ((2000, 1, 28, 0, 0, 0))
    0000   0x00 0x40 0x00 0x3c 0x00                   .@.<.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
#### RECORD 19 Base (2014, 4, 10, 13, 8, 18) head[2], body[0] op[0xb5]

    op hex (2)
    0000   0xb5 0x35                                  .5
    decimal
            181   53
    datetime ((2014, 4, 10, 13, 8, 18))
    0000   0x52 0x08 0x0d 0x0a 0xae                   R....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 20 Base (2014, 0, 27, 13, 8, 51) head[2], body[0] op[0xbb]

    op hex (2)
    0000   0xbb 0x1d                                  ..
    decimal
            187   29
    datetime ((2014, 0, 27, 13, 8, 51))
    0000   0x33 0x08 0x0d 0x5b 0xae                   3..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 21 Base (2000, 0, 12, 13, 8, 19) head[2], body[0] op[0x8a]

    op hex (2)
    0000   0x8a 0x1e                                  ..
    decimal
            138   30
    datetime ((2000, 0, 12, 13, 8, 19))
    0000   0x13 0x08 0x0d 0x0c 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 22 Base (2000, 1, 0, 4, 36, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x64                                  .d
    decimal
              0  100
    datetime ((2000, 1, 0, 4, 36, 60))
    0000   0x3c 0x64 0x24 0x00 0x30                   <d$.0
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-12.data: 23 records`
