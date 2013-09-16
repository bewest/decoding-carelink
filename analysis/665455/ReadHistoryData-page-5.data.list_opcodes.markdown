## START logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 286, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x02 0x01 0x01 0x00 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x1e 0x00 0x53 0xe0 0x0a    .....S..
    0010   0x11 0x0d 0x1f 0x00 0x45 0xe4 0x0a 0x11    ....E...
    0018   0x0d 0x1e 0x00 0x5a 0xcd 0x0c 0x11 0x0d    ...Z....
##### DEBUG DECIMAL
              2    1    1    0    0   12    0  232
              0    0    0   30    0   83  224   10
             17   13   31    0   69  228   10   17
             13   30    0   90  205   12   17   13
#### RECORD 0 PumpSuspend 2013-07-15T13:57:04 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-15T13:57:04)
    0000   0x44 0xf9 0x0d 0x0f 0x0d                   D....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 PumpResume 2013-07-15T14:18:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-15T14:18:33)
    0000   0x61 0xd2 0x0e 0x0f 0x0d                   a....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 CalBGForPH 2013-07-15T16:21:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-07-15T16:21:20)
    0000   0x54 0xd5 0x30 0x0f 0x0d                   T.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BolusWizard 2013-07-15T16:21:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 160,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2013-07-15T16:21:32)
    0000   0x60 0xd5 0x10 0x0f 0x0d                   `....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x07 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             28   80   13   45  106    7   21    0
              0    0    0   28  125
    HOUR BITS: [1, 1, 0]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 3.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x94 0xd3 0x14                   \....
    decimal
             92    5  148  211   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-07-15T16:21:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-07-15T16:21:32)
    0000   0x60 0xd5 0x50 0x0f 0x0d                   `.P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2013-07-15T21:55:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-07-15T21:55:51)
    0000   0x73 0xf7 0x35 0x0f 0x0d                   s.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 BolusWizard 2013-07-15T21:56:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.1,
 'carb_input': 66,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-07-15T21:56:12)
    0000   0x4c 0xf8 0x15 0x0f 0x0d                   L....
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0x01 0x32 0x00    BP.-j.2.
    0008   0x00 0x00 0x00 0x33 0x7d                   ...3}
    decimal
             66   80   13   45  106    1   50    0
              0    0    0   51  125
    HOUR BITS: [1, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 2.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0x56 0x14                   \.pV.
    decimal
             92    5  112   86   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-07-15T21:56:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1, 'dual_component': '??', 'programmed': 5.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x33 0x33 0x00                        .33.
    decimal
              1   51   51    0
    datetime (2013-07-15T21:56:12)
    0000   0x4c 0xf8 0x55 0x0f 0x0d                   L.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 ResultTotals 2013-06-15T13:13:47 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xbe                   .....
    decimal
              7    0    0    5  190
    datetime (2013-06-15T13:13:47)
    0000   0x6f 0x8d 0x6d 0x6f 0x8d                   o.mo.
    body (51)
    hex
    0000   0x05 0x10 0xdd 0x82 0x2d 0x04 0x00 0x00    ....-...
    0008   0x05 0xbe 0x03 0x76 0x3c 0x02 0x48 0x28    ...v<.H(
    0010   0x00 0x5e 0x02 0x48 0x28 0x01 0x1c 0x31    .^.H(..1
    0018   0x01 0x2c 0x33 0x00 0x00 0x00 0x04 0x00    .,3.....
    0020   0x02 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x45 0xee 0x08 0x10 0x0d    ...E....
    0030   0x1f 0x00 0x78                             ..x
    decimal
              5   16  221  130   45    4    0    0
              5  190    3  118   60    2   72   40
              0   94    2   72   40    1   28   49
              1   44   51    0    0    0    4    0
              2    2    0   12    0  232    0    0
              0   30    0   69  238    8   16   13
             31    0  120
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 11 Base (2001, 0, 3, 10, 13, 16) head[2], body[0] op[0xef]

    op hex (2)
    0000   0xef 0x08                                  ..
    decimal
            239    8
    datetime ((2001, 0, 3, 10, 13, 16))
    0000   0x10 0x0d 0x0a 0x23 0x51                   ...#Q
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 12 Base (2011, 2, 3, 27, 13, 16) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x2a                                  .*
    decimal
            213   42
    datetime ((2011, 2, 3, 27, 13, 16))
    0000   0x10 0x8d 0x5b 0x23 0x5b                   ..[#[
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 13 Base (2013, 0, 17, 0, 13, 16) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x0a                                  ..
    decimal
            213   10
    datetime ((2013, 0, 17, 0, 13, 16))
    0000   0x10 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 14 Base (2000, 0, 0, 0, 0, 36) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 36))
    0000   0x24 0x00 0x00 0x00 0x00                   $....
    body (0)

#### RECORD 15 Base (2000, 4, 4, 4, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x24                                  .$
    decimal
              0   36
    datetime ((2000, 4, 4, 4, 1, 61))
    0000   0x7d 0x01 0x24 0x24 0x00                   }.$$.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 16 BolusWizard 2000-04-30T13:16:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 97,
 'bg': 1237,
 'bg_target_high': 10,
 'bg_target_low': 13,
 'bolus_estimate': 1.3,
 'carb_input': 87,
 'carb_ratio': 13,
 'correction_estimate': 11.2,
 'food_estimate': 0.0,
 'sensitivity': 16,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 16,
 'unknown_byte[8]': 243}
```
    op hex (2)
    0000   0x5b 0xd5                                  [.
    decimal
             91  213
    datetime (2000-04-30T13:16:10)
    0000   0x4a 0x10 0x0d 0x1e 0x00                   J....
    body (13)
    hex
    0000   0x57 0xe4 0x0d 0x10 0x0d 0x1f 0x00 0x61    W......a
    0008   0xf3 0x0d 0x10 0x0d 0x0a                   .....
    decimal
             87  228   13   16   13   31    0   97
            243   13   16   13   10

#### RECORD 17 Base (2011, 12, 13, 16, 54, 21) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0x69                                  fi
    decimal
            102  105
    datetime ((2011, 12, 13, 16, 54, 21))
    0000   0xd5 0x36 0x10 0x0d 0x5b                   .6..[
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 18 Base (2011, 12, 13, 16, 22, 22) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0x6c                                  fl
    decimal
            102  108
    datetime ((2011, 12, 13, 16, 22, 22))
    0000   0xd6 0x16 0x10 0x0d 0x3b                   ....;
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 19 Ian50 (2000, 1, 13, 31, 42, 45) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime ((2000, 1, 13, 31, 42, 45))
    0000   0x2d 0x6a 0xff 0x2d 0xf0                   -j.-.
    body (34)
    hex
    0000   0x00 0x00 0x00 0x2c 0x7d 0x01 0x2c 0x2c    ...,}.,,
    0008   0x00 0x6c 0xd6 0x56 0x10 0x0d 0x07 0x00    .l.V....
    0010   0x00 0x04 0xb8 0x70 0x8d 0x6d 0x70 0x8d    ...p.mp.
    0018   0x05 0x10 0xc5 0x66 0x23 0x02 0x00 0x00    ...f#...
    0020   0x04 0xb8                                  ..
    decimal
              0    0    0   44  125    1   44   44
              0  108  214   86   16   13    7    0
              0    4  184  112  141  109  112  141
              5   16  197  102   35    2    0    0
              4  184
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 20 Prime (2000, 0, 1, 27, 0, 26) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.4, 'fixed': 7.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x78 0x4a 0x01 0x40                   .xJ.@
    decimal
              3  120   74    1   64
    datetime ((2000, 0, 1, 27, 0, 26))
    0000   0x1a 0x00 0x3b 0x01 0x40                   ..;.@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 21 Battery 2013-08-16T00:55:48 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-08-16T00:55:48)
    0000   0xb0 0x37 0x00 0x90 0x2d                   .7..-
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 0]
`end logs/ReadHistoryData-page-5.data: 22 records`
