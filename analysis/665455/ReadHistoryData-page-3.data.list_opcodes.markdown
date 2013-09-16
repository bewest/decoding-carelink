## START logs/ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 237, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x09 0x7d 0x01 0x09 0x09 0x00 0x4a 0xca    .}....J.
    0008   0x56 0x1e 0x0d 0x0a 0xb9 0x49 0xef 0x36    V....I.6
    0010   0x1e 0x0d 0x5b 0xb9 0x4b 0xf0 0x16 0x1e    ..[.K...
    0018   0x0d 0x3d 0x50 0x0d 0x2d 0x6a 0x0d 0x2e    .=P.-j..
##### DEBUG DECIMAL
              9  125    1    9    9    0   74  202
             86   30   13   10  185   73  239   54
             30   13   91  185   75  240   22   30
             13   61   80   13   45  106   13   46
#### RECORD 0 Rewind 2013-07-29T14:00:16 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-29T14:00:16)
    0000   0x50 0xc0 0x0e 0x1d 0x0d                   P....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 Prime 2013-07-29T14:02:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x15                   .....
    decimal
              3    0    0    0   21
    datetime (2013-07-29T14:02:03)
    0000   0x43 0xc2 0x2e 0x1d 0x0d                   C....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 Prime 2013-07-29T14:02:26 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-29T14:02:26)
    0000   0x5a 0xc2 0x0e 0x1d 0x0d                   Z....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-07-29T21:43:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-07-29T21:43:46)
    0000   0x6e 0xeb 0x35 0x1d 0x0d                   n.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 BolusWizard 2013-07-29T21:44:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 90,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5a                                  [Z
    decimal
             91   90
    datetime (2013-07-29T21:44:59)
    0000   0x7b 0xec 0x15 0x1d 0x0d                   {....
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0xfc 0x28 0xf0    5P.-j.(.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             53   80   13   45  106  252   40  240
              0    0    0   36  125
    HOUR BITS: [1, 1, 1]
#### RECORD 5 Bolus 2013-07-29T21:44:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-07-29T21:44:59)
    0000   0x7b 0xec 0x55 0x1d 0x0d                   {.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 ResultTotals (2013, 6, 29, 13, 13, 61) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x06                   .....
    decimal
              7    0    0    4    6
    datetime ((2013, 6, 29, 13, 13, 61))
    0000   0x7d 0x8d 0x6d 0x7d 0x8d                   }.m}.
    body (51)
    hex
    0000   0x05 0x00 0x5a 0x5a 0x5a 0x01 0x00 0x00    ..ZZZ...
    0008   0x04 0x06 0x03 0x76 0x56 0x00 0x90 0x0e    ...vV...
    0010   0x00 0x35 0x00 0x90 0x0e 0x00 0x90 0x64    .5.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0xf4 0x59 0xdc 0x29 0x1e 0x0d    ...Y.)..
    0030   0x5b 0xf4 0x5e                             [.^
    decimal
              5    0   90   90   90    1    0    0
              4    6    3  118   86    0  144   14
              0   53    0  144   14    0  144  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0   10  244   89  220   41   30   13
             91  244   94
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 7 Base (2013, 0, 16, 0, 13, 30) head[2], body[0] op[0xdc]

    op hex (2)
    0000   0xdc 0x09                                  ..
    decimal
            220    9
    datetime ((2013, 0, 16, 0, 13, 30))
    0000   0x1e 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 8 Base (2000, 0, 0, 0, 0, 26) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 26))
    0000   0x1a 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 9 Base (2000, 4, 26, 26, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1a                                  ..
    decimal
              0   26
    datetime ((2000, 4, 26, 26, 1, 61))
    0000   0x7d 0x01 0x1a 0x1a 0x00                   }....
    body (0)

#### RECORD 10 Base (2000, 4, 30, 13, 30, 9) head[2], body[0] op[0x5e]

    op hex (2)
    0000   0x5e 0xdc                                  ^.
    decimal
             94  220
    datetime ((2000, 4, 30, 13, 30, 9))
    0000   0x49 0x1e 0x0d 0x1e 0x00                   I....
    body (0)

#### RECORD 11 Base (2000, 0, 31, 13, 30, 10) head[2], body[0] op[0x57]

    op hex (2)
    0000   0x57 0xfa                                  W.
    decimal
             87  250
    datetime ((2000, 0, 31, 13, 30, 10))
    0000   0x0a 0x1e 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 12 Ian50 (2011, 0, 10, 13, 30, 11) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0xd8                                  P.
    decimal
             80  216
    datetime ((2011, 0, 10, 13, 30, 11))
    0000   0x0b 0x1e 0x0d 0x0a 0x3b                   ....;
    body (34)
    hex
    0000   0x4b 0xc1 0x2c 0x1e 0x0d 0x0a 0x4b 0x7a    K.,...Kz
    0008   0xd6 0x2d 0x1e 0x0d 0x5b 0x4b 0x4e 0xd8    .-..[KN.
    0010   0x0d 0x1e 0x0d 0x2c 0x50 0x0d 0x2d 0x6a    ...,P.-j
    0018   0xf9 0x21 0xf0 0x00 0x02 0x00 0x1a 0x7d    .!.....}
    0020   0x5c 0x05                                  \.
    decimal
             75  193   44   30   13   10   75  122
            214   45   30   13   91   75   78  216
             13   30   13   44   80   13   45  106
            249   33  240    0    2    0   26  125
             92    5
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 13 Base (2000, 0, 26, 26, 1, 4) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0xf0                                  h.
    decimal
            104  240
    datetime ((2000, 0, 26, 26, 1, 4))
    0000   0x04 0x01 0x1a 0x1a 0x00                   .....
    body (0)

#### RECORD 14 Base (2007, 4, 10, 13, 30, 13) head[2], body[0] op[0x4e]

    op hex (2)
    0000   0x4e 0xd8                                  N.
    decimal
             78  216
    datetime ((2007, 4, 10, 13, 30, 13))
    0000   0x4d 0x1e 0x0d 0x0a 0xa7                   M....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 15 Base (2007, 0, 27, 13, 30, 54) head[2], body[0] op[0x45]

    op hex (2)
    0000   0x45 0xca                                  E.
    decimal
             69  202
    datetime ((2007, 0, 27, 13, 30, 54))
    0000   0x36 0x1e 0x0d 0x5b 0xa7                   6..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 16 Base (2000, 0, 0, 13, 30, 22) head[2], body[0] op[0x4a]

    op hex (2)
    0000   0x4a 0xca                                  J.
    decimal
             74  202
    datetime ((2000, 0, 0, 13, 30, 22))
    0000   0x16 0x1e 0x0d 0x00 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 17 Base (2000, 4, 0, 0, 9, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 9, 42))
    0000   0x6a 0x09 0x00 0x00 0x00                   j....
    body (0)

`end logs/ReadHistoryData-page-3.data: 18 records`
