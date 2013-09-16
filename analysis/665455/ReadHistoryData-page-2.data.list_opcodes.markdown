## START logs/ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 235, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x3f 0x7d 0x34 0x64 0x90 0x16 0x12 0x06    ?}4d....
    0008   0x0d 0x01 0x3f 0x3f 0x00 0x80 0x16 0x52    ..??...R
    0010   0x06 0x0d 0x0a 0x29 0x81 0x22 0x37 0x06    ...)."7.
    0018   0x8d 0x5b 0x29 0x8b 0x22 0x17 0x06 0x0d    .[)."...
##### DEBUG DECIMAL
             63  125   52  100  144   22   18    6
             13    1   63   63    0  128   22   82
              6   13   10   41  129   34   55    6
            141   91   41  139   34   23    6   13
#### RECORD 0 hack1 2013-08-05T09:20:35 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x84 0x0d 0x05 0x00 0x96 0x75 0xba    m.....u.
    0008   0x04 0x00 0x00 0x05 0x20 0x03 0x70 0x43    .... .pC
    0010   0x01 0xb0 0x21 0x00 0x73 0x01 0xb0 0x21    ..!.s..!
    0018   0x01 0x60 0x51 0x00 0x50 0x13 0x00 0x00    .`Q.P...
    0020   0x00 0x04 0x02 0x02 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x0e              ......
    decimal
            109  132   13    5    0  150  117  186
              4    0    0    5   32    3  112   67
              1  176   33    0  115    1  176   33
              1   96   81    0   80   19    0    0
              0    4    2    2    0    0   12    0
            232    0    0    0   10   14
    datetime (2013-08-05T09:20:35)
    0000   0xa3 0x14 0x29 0x05 0x8d                   ..)..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 BolusWizard 2013-08-05T09:20:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 270,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0e                                  [.
    decimal
             91   14
    datetime (2013-08-05T09:20:36)
    0000   0xa4 0x14 0x09 0x05 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
              0   81   13   45  106   32    0    0
              0    0    0   32  125

#### RECORD 2 Bolus 2013-08-05T09:20:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-08-05T09:20:37)
    0000   0xa5 0x14 0x49 0x05 0x0d                   ..I..
    body (0)

#### RECORD 3 CalBGForPH 2013-08-05T21:57:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-08-05T21:57:49)
    0000   0xb1 0x39 0x35 0x05 0x0d                   .95..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BolusWizard 2013-08-05T21:58:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 103,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 66,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-08-05T21:58:28)
    0000   0x9c 0x3a 0x15 0x05 0x0d                   .:...
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0xff 0x32 0xf0    BP.-j.2.
    0008   0x00 0x00 0x00 0x31 0x7d                   ...1}
    decimal
             66   80   13   45  106  255   50  240
              0    0    0   49  125
    HOUR BITS: [0, 0, 1]
#### RECORD 5 Bolus 2013-08-05T21:58:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2013-08-05T21:58:28)
    0000   0x9c 0x3a 0x55 0x05 0x0d                   .:U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 ResultTotals 2013-08-05T13:13:05 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc8                   .....
    decimal
              7    0    0    4  200
    datetime (2013-08-05T13:13:05)
    0000   0x85 0x0d 0x6d 0x85 0x0d                   ..m..
    body (51)
    hex
    0000   0x05 0x10 0xbb 0x67 0x0e 0x02 0x00 0x00    ...g....
    0008   0x04 0xc8 0x03 0x84 0x4a 0x01 0x44 0x1a    ....J.D.
    0010   0x00 0x42 0x01 0x44 0x1a 0x00 0xc4 0x3c    .B.D...<
    0018   0x00 0x80 0x28 0x00 0x00 0x00 0x02 0x01    ..(.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x2a 0xab 0x23 0x28 0x06 0x8d    ..*.#(..
    0030   0x5b 0x2a 0xad                             [*.
    decimal
              5   16  187  103   14    2    0    0
              4  200    3  132   74    1   68   26
              0   66    1   68   26    0  196   60
              0  128   40    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0   10   42  171   35   40    6  141
             91   42  173
    DAY BITS: [1, 0, 0]
#### RECORD 7 Base (2013, 0, 17, 0, 13, 6) head[2], body[0] op[0x23]

    op hex (2)
    0000   0x23 0x08                                  #.
    decimal
             35    8
    datetime ((2013, 0, 17, 0, 13, 6))
    0000   0x06 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 8 Base (2000, 0, 0, 0, 0, 38) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 38))
    0000   0x26 0x00 0x00 0x00 0x00                   &....
    body (0)

#### RECORD 9 Base (2000, 4, 6, 6, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x26                                  .&
    decimal
              0   38
    datetime ((2000, 4, 6, 6, 1, 61))
    0000   0x7d 0x01 0x26 0x26 0x00                   }.&&.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 10 Base (2008, 4, 20, 13, 6, 8) head[2], body[0] op[0xad]

    op hex (2)
    0000   0xad 0x23                                  .#
    decimal
            173   35
    datetime ((2008, 4, 20, 13, 6, 8))
    0000   0x48 0x06 0x0d 0x34 0xc8                   H..4.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 11 Base (2004, 0, 10, 13, 6, 9) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x00                                  ..
    decimal
            128    0
    datetime ((2004, 0, 10, 13, 6, 9))
    0000   0x09 0x06 0x0d 0x0a 0xd4                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 1]
#### RECORD 12 Base (2004, 0, 27, 13, 6, 50) head[2], body[0] op[0xb3]

    op hex (2)
    0000   0xb3 0x15                                  ..
    decimal
            179   21
    datetime ((2004, 0, 27, 13, 6, 50))
    0000   0x32 0x06 0x0d 0x5b 0xd4                   2..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 13 Base (2000, 0, 26, 13, 6, 18) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x16                                  ..
    decimal
            128   22
    datetime ((2000, 0, 26, 13, 6, 18))
    0000   0x12 0x06 0x0d 0x3a 0x50                   ...:P
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 14 Base (2000, 4, 0, 12, 19, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 12, 19, 42))
    0000   0x6a 0x13 0x2c 0x00 0x00                   j.,..
    body (0)

`end logs/ReadHistoryData-page-2.data: 15 records`
