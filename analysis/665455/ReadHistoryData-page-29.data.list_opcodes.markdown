## START logs/ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 1008, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x22 0x57 0x0c 0x34 0x09 0x0d 0x00 0x00    "W.4....
    0008   0x00 0x00 0x00 0x00 0x00 0x48 0x5a         .....HZ
##### DEBUG DECIMAL
             34   87   12   52    9   13    0    0
              0    0    0    0    0   72   90
#### RECORD 0 Bolus 2013-04-06T21:36:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-04-06T21:36:51)
    0000   0x73 0x24 0x55 0x06 0x0d                   s$U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 CalBGForPH 2013-04-06T21:46:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 261}
```
    op hex (2)
    0000   0x0a 0x05                                  ..
    decimal
             10    5
    datetime (2013-04-06T21:46:27)
    0000   0x5b 0x2e 0x35 0x06 0x8d                   [.5..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 BolusWizard 2013-04-06T21:47:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 261,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.7,
 'carb_input': 88,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 6.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x05                                  [.
    decimal
             91    5
    datetime (2013-04-06T21:47:07)
    0000   0x47 0x2f 0x15 0x06 0x0d                   G/...
    body (13)
    hex
    0000   0x58 0x51 0x0d 0x2d 0x6a 0x1e 0x43 0x00    XQ.-j.C.
    0008   0x00 0x26 0x00 0x43 0x7d                   .&.C}
    decimal
             88   81   13   45  106   30   67    0
              0   38    0   67  125
    HOUR BITS: [0, 0, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 0.4, 'curve': 4},
 {'age': 23, 'amount': 1.0, 'curve': 4},
 {'age': 73, 'amount': 0.4, 'curve': 4},
 {'age': 83, 'amount': 3.0, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x10 0x0d 0x04 0x28 0x17 0x04    \....(..
    0008   0x10 0x49 0x04 0x78 0x53 0x04              .I.xS.
    decimal
             92   14   16   13    4   40   23    4
             16   73    4  120   83    4
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-04-06T21:47:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.7, 'dual_component': '??', 'programmed': 6.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x43 0x43 0x00                        .CC.
    decimal
              1   67   67    0
    datetime (2013-04-06T21:47:07)
    0000   0x47 0x2f 0x55 0x06 0x0d                   G/U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 ResultTotals 2013-04-06T13:13:06 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x50                   ....P
    decimal
              7    0    0    5   80
    datetime (2013-04-06T13:13:06)
    0000   0x46 0x0d 0x6d 0x46 0x0d                   F.mF.
    body (51)
    hex
    0000   0x05 0x10 0xeb 0x63 0x18 0x05 0x00 0x00    ...c....
    0008   0x05 0x50 0x03 0x84 0x42 0x01 0xcc 0x22    .P..B.."
    0010   0x00 0x58 0x01 0xcc 0x22 0x01 0x0c 0x3a    .X.."..:
    0018   0x00 0xc0 0x2a 0x00 0x00 0x00 0x04 0x01    ..*.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0xbb 0x4f 0x38 0x23 0x07 0x0d    ...O8#..
    0030   0x5b 0xbb 0x52                             [.R
    decimal
              5   16  235   99   24    5    0    0
              5   80    3  132   66    1  204   34
              0   88    1  204   34    1   12   58
              0  192   42    0    0    0    4    1
              3    0    0   12    0  232    0    0
              0   10  187   79   56   35    7   13
             91  187   82
    DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2013, 0, 16, 0, 13, 7) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x03                                  8.
    decimal
             56    3
    datetime ((2013, 0, 16, 0, 13, 7))
    0000   0x07 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2000, 0, 0, 0, 0, 13) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 13))
    0000   0x0d 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 8 Base (2004, 5, 12, 17, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0d                                  ..
    decimal
              0   13
    datetime ((2004, 5, 12, 17, 28, 61))
    0000   0x7d 0x5c 0x11 0x0c 0x74                   }\..t
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 9 Base (2004, 4, 8, 8, 20, 62) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x10                                  ..
    decimal
             21   16
    datetime ((2004, 4, 8, 8, 20, 62))
    0000   0x7e 0x14 0x28 0x88 0x14                   ~.(..
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 Base (2001, 1, 20, 4, 56, 20) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0xba                                  ..
    decimal
             16  186
    datetime ((2001, 1, 20, 4, 56, 20))
    0000   0x14 0x78 0xc4 0x14 0x01                   .x...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 11 Base (2007, 1, 3, 24, 18, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0d                                  ..
    decimal
             13   13
    datetime ((2007, 1, 3, 24, 18, 0))
    0000   0x00 0x52 0x38 0x43 0x07                   .R8C.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 12 Base (2007, 5, 12, 26, 51, 17) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2007, 5, 12, 26, 51, 17))
    0000   0x51 0x73 0x3a 0x2c 0x07                   Qs:,.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1]
#### RECORD 13 Base (2007, 5, 12, 27, 8, 17) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2007, 5, 12, 27, 8, 17))
    0000   0x51 0x48 0x3b 0x0c 0x07                   QH;..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 14 Base (2010, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x22                                  ."
    decimal
             13   34
    datetime ((2010, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0xfa                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 15 Battery (2013, 0, 20, 0, 0, 0) head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0xf0                                  ..
    decimal
             26  240
    datetime ((2013, 0, 20, 0, 0, 0))
    0000   0x00 0x00 0x00 0x14 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 16 Bolus 2013-04-07T12:59:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-04-07T12:59:08)
    0000   0x48 0x3b 0x4c 0x07 0x0d                   H;L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 PumpSuspend 2013-04-07T16:46:28 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-07T16:46:28)
    0000   0x5c 0x2e 0x10 0x07 0x0d                   \....
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 PumpResume 2013-04-07T17:15:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-07T17:15:06)
    0000   0x46 0x0f 0x11 0x07 0x0d                   F....
    body (0)

#### RECORD 19 CalBGForPH 2013-04-07T19:36:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 221}
```
    op hex (2)
    0000   0x0a 0xdd                                  ..
    decimal
             10  221
    datetime (2013-04-07T19:36:43)
    0000   0x6b 0x24 0x33 0x07 0x0d                   k$3..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 BolusWizard 2013-04-07T19:36:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 221,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdd                                  [.
    decimal
             91  221
    datetime (2013-04-07T19:36:48)
    0000   0x70 0x24 0x13 0x07 0x0d                   p$...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    0    0   21  125
    HOUR BITS: [0, 0, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 146, 'amount': 2.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x92 0x14                   \.P..
    decimal
             92    5   80  146   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-04-07T19:36:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-04-07T19:36:48)
    0000   0x70 0x24 0x53 0x07 0x0d                   p$S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 23 CalBGForPH 2013-04-07T20:16:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 229}
```
    op hex (2)
    0000   0x0a 0xe5                                  ..
    decimal
             10  229
    datetime (2013-04-07T20:16:45)
    0000   0x6d 0x10 0x34 0x07 0x0d                   m.4..
    body (0)

#### RECORD 24 BolusWizard 2013-04-07T20:16:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 229,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe5                                  [.
    decimal
             91  229
    datetime (2013-04-07T20:16:53)
    0000   0x75 0x10 0x14 0x07 0x0d                   u....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x17 0x00 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106   23    0    0
              0   22    0    1  125

#### RECORD 25 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 42, 'amount': 2.4, 'curve': 4},
 {'age': 186, 'amount': 2.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x60 0x2a 0x04 0x50 0xba 0x14    \.`*.P..
    decimal
             92    8   96   42    4   80  186   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-04-07T20:16:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-04-07T20:16:53)
    0000   0x75 0x10 0x54 0x07 0x0d                   u.T..
    body (0)

#### RECORD 27 BolusWizard 2013-04-07T20:26:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.9,
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
    datetime (2013-04-07T20:26:29)
    0000   0x5d 0x1a 0x14 0x07 0x0d                   ]....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125

#### RECORD 28 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 0.5, 'curve': 4},
 {'age': 52, 'amount': 2.4, 'curve': 4},
 {'age': 196, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0x0c 0x04 0x60 0x34 0x04    \....`4.
    0008   0x50 0xc4 0x14                             P..
    decimal
             92   11   20   12    4   96   52    4
             80  196   20
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-04-07T20:26:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-04-07T20:26:30)
    0000   0x5e 0x1a 0x54 0x07 0x0d                   ^.T..
    body (0)

#### RECORD 30 CalBGForPH 2013-04-07T21:09:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2013-04-07T21:09:26)
    0000   0x5a 0x09 0x35 0x07 0x0d                   Z.5..
    body (0)

#### RECORD 31 BolusWizard 2013-04-07T21:09:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 234,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 2.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xea                                  [.
    decimal
             91  234
    datetime (2013-04-07T21:09:38)
    0000   0x66 0x09 0x15 0x07 0x0d                   f....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x18 0x1c 0x00    %P.-j...
    0008   0x00 0x24 0x00 0x1c 0x7d                   .$..}
    decimal
             37   80   13   45  106   24   28    0
              0   36    0   28  125

#### RECORD 32 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 1.9, 'curve': 4},
 {'age': 55, 'amount': 0.5, 'curve': 4},
 {'age': 95, 'amount': 2.4, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0x2d 0x04 0x14 0x37 0x04    \.L-..7.
    0008   0x60 0x5f 0x04                             `_.
    decimal
             92   11   76   45    4   20   55    4
             96   95    4
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-04-07T21:09:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-04-07T21:09:39)
    0000   0x67 0x09 0x55 0x07 0x0d                   g.U..
    body (0)

#### RECORD 34 CalBGForPH 2013-04-07T23:12:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-04-07T23:12:51)
    0000   0x73 0x0c 0x37 0x07 0x0d                   s.7..
    body (0)

#### RECORD 35 ResultTotals 2013-04-07T13:13:07 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x26                   ....&
    decimal
              7    0    0    5   38
    datetime (2013-04-07T13:13:07)
    0000   0x47 0x0d 0x6d 0x47 0x0d                   G.mG.
    body (51)
    hex
    0000   0x05 0x00 0xb1 0x51 0xea 0x06 0x00 0x00    ...Q....
    0008   0x05 0x26 0x03 0x72 0x43 0x01 0xb4 0x21    .&.rC..!
    0010   0x00 0x60 0x01 0xb4 0x21 0x01 0x0c 0x3d    .`..!..=
    0018   0x00 0xa8 0x27 0x00 0x00 0x00 0x06 0x03    ..'.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x46 0x3a 0x0a 0x08 0x0d    ...F:...
    0030   0x1f 0x00 0x49                             ..I
    decimal
              5    0  177   81  234    6    0    0
              5   38    3  114   67    1  180   33
              0   96    1  180   33    1   12   61
              0  168   39    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0   30    0   70   58   10    8   13
             31    0   73
    DAY BITS: [0, 1, 0]
#### RECORD 36 Base (2011, 0, 24, 10, 13, 8) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x0b                                  ..
    decimal
             15   11
    datetime ((2011, 0, 24, 10, 13, 8))
    0000   0x08 0x0d 0x0a 0x98 0x4b                   ....K
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 37 Base (2003, 0, 24, 27, 13, 8) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2d                                  .-
    decimal
              0   45
    datetime ((2003, 0, 24, 27, 13, 8))
    0000   0x08 0x0d 0x5b 0x98 0x53                   ..[.S
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 38 Base (2013, 0, 16, 0, 13, 8) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0d                                  ..
    decimal
              0   13
    datetime ((2013, 0, 16, 0, 13, 8))
    0000   0x08 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 39 Base (2000, 0, 0, 0, 0, 6) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 6))
    0000   0x06 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 40 Base (2000, 4, 8, 8, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x06                                  ..
    decimal
              0    6
    datetime ((2000, 4, 8, 8, 1, 61))
    0000   0x7d 0x01 0x08 0x08 0x00                   }....
    body (0)

#### RECORD 41 Base (2006, 4, 10, 13, 8, 13) head[2], body[0] op[0x53]

    op hex (2)
    0000   0x53 0x00                                  S.
    decimal
             83    0
    datetime ((2006, 4, 10, 13, 8, 13))
    0000   0x4d 0x08 0x0d 0x0a 0x96                   M....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 42 BolusWizard (2006, 0, 27, 13, 8, 45) head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 37,
 '_byte[7]': 13,
 'bg': 3100,
 'bg_target_high': 0,
 'bg_target_low': 13,
 'bolus_estimate': 2.8,
 'carb_input': 123,
 'carb_ratio': 13,
 'correction_estimate': 1.8,
 'food_estimate': 8.0,
 'sensitivity': 8,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 10.6,
 'unknown_byte[10]': 5,
 'unknown_byte[8]': 45}
```
    op hex (2)
    0000   0x5b 0x1c                                  [.
    decimal
             91   28
    datetime ((2006, 0, 27, 13, 8, 45))
    0000   0x2d 0x08 0x0d 0x5b 0x96                   -..[.
    body (13)
    hex
    0000   0x7b 0x1c 0x0d 0x08 0x0d 0x25 0x50 0x0d    {....%P.
    0008   0x2d 0x6a 0x05 0x1c 0x00                   -j...
    decimal
            123   28   13    8   13   37   80   13
             45  106    5   28    0
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 43 Base (2005, 0, 28, 29, 28, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2005, 0, 28, 29, 28, 0))
    0000   0x00 0x1c 0x7d 0x5c 0x05                   ..}\.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 44 Base (2000, 0, 28, 28, 1, 4) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x22                                   "
    decimal
             32   34
    datetime ((2000, 0, 28, 28, 1, 4))
    0000   0x04 0x01 0x1c 0x1c 0x00                   .....
    body (0)

#### RECORD 45 Base (2015, 4, 10, 13, 8, 13) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x1d                                  @.
    decimal
             64   29
    datetime ((2015, 4, 10, 13, 8, 13))
    0000   0x4d 0x08 0x0d 0x0a 0x8f                   M....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 46 Base (2015, 0, 27, 13, 8, 45) head[2], body[0] op[0x67]

    op hex (2)
    0000   0x67 0x3b                                  g;
    decimal
            103   59
    datetime ((2015, 0, 27, 13, 8, 45))
    0000   0x2d 0x08 0x0d 0x5b 0x8f                   -..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 47 Base (2000, 0, 29, 13, 8, 14) head[2], body[0] op[0x45]

    op hex (2)
    0000   0x45 0x00                                  E.
    decimal
             69    0
    datetime ((2000, 0, 29, 13, 8, 14))
    0000   0x0e 0x08 0x0d 0x1d 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 48 Base (2000, 4, 0, 22, 4, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 22, 4, 42))
    0000   0x6a 0x04 0x16 0x00 0x00                   j....
    body (0)

#### RECORD 49 Rewind (2000, 1, 8, 28, 61, 22) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime ((2000, 1, 8, 28, 61, 22))
    0000   0x16 0x7d 0x5c 0x08 0x70                   .}\.p
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 50 Base (2006, 1, 1, 4, 2, 32) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x04                                  $.
    decimal
             36    4
    datetime ((2006, 1, 1, 4, 2, 32))
    0000   0x20 0x42 0x04 0x01 0x16                    B...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 51 TempBasalDuration 2013-04-08T14:00:05 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-04-08T14:00:05)
    0000   0x45 0x00 0x4e 0x08 0x0d                   E.N..
    body (0)

#### RECORD 52 CalBGForPH 2013-04-08T14:25:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 179}
```
    op hex (2)
    0000   0x0a 0xb3                                  ..
    decimal
             10  179
    datetime (2013-04-08T14:25:21)
    0000   0x55 0x19 0x2e 0x08 0x0d                   U....
    body (0)

#### RECORD 53 BolusWizard 2013-04-08T15:28:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 8,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.6,
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
    datetime (2013-04-08T15:28:53)
    0000   0x75 0x1c 0x0f 0x08 0x0d                   u....
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              8   80   13   45  106    0    6    0
              0    0    0    6  125

#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 2.2, 'curve': 4},
 {'age': 124, 'amount': 2.8, 'curve': 4},
 {'age': 154, 'amount': 0.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x5e 0x04 0x70 0x7c 0x04    \.X^.p|.
    0008   0x20 0x9a 0x04                              ..
    decimal
             92   11   88   94    4  112  124    4
             32  154    4
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-04-08T15:28:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-04-08T15:28:53)
    0000   0x75 0x1c 0x4f 0x08 0x0d                   u.O..
    body (0)

#### RECORD 56 BolusWizard 2013-04-08T16:10:43 head[2], body[13] op[0x5b]
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
    datetime (2013-04-08T16:10:43)
    0000   0x6b 0x0a 0x10 0x08 0x0d                   k....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125

#### RECORD 57 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 0.6, 'curve': 4},
 {'age': 136, 'amount': 2.2, 'curve': 4},
 {'age': 166, 'amount': 2.8, 'curve': 4},
 {'age': 196, 'amount': 0.8, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x2e 0x04 0x58 0x88 0x04    \....X..
    0008   0x70 0xa6 0x04 0x20 0xc4 0x04              p.. ..
    decimal
             92   14   24   46    4   88  136    4
            112  166    4   32  196    4
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-04-08T16:10:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-04-08T16:10:43)
    0000   0x6b 0x0a 0x50 0x08 0x0d                   k.P..
    body (0)

#### RECORD 59 CalBGForPH 2013-04-08T19:49:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-04-08T19:49:26)
    0000   0x5a 0x31 0x33 0x08 0x0d                   Z13..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 CalBGForPH 2013-04-08T20:15:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-04-08T20:15:40)
    0000   0x68 0x0f 0x34 0x08 0x0d                   h.4..
    body (0)

#### RECORD 61 CalBGForPH 2013-04-08T20:19:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-04-08T20:19:04)
    0000   0x44 0x13 0x34 0x08 0x0d                   D.4..
    body (0)

#### RECORD 62 BolusWizard 2013-04-08T20:19:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 128,
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
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-04-08T20:19:14)
    0000   0x4e 0x13 0x14 0x08 0x0d                   N....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0    0    0   21  125

#### RECORD 63 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 255, 'amount': 1.1, 'curve': 4},
 {'age': 39, 'amount': 0.6, 'curve': 20},
 {'age': 129, 'amount': 2.2, 'curve': 20},
 {'age': 159, 'amount': 2.8, 'curve': 20},
 {'age': 189, 'amount': 0.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x2c 0xff 0x04 0x18 0x27 0x14    \.,...'.
    0008   0x58 0x81 0x14 0x70 0x9f 0x14 0x20 0xbd    X..p.. .
    0010   0x14                                       .
    decimal
             92   17   44  255    4   24   39   20
             88  129   20  112  159   20   32  189
             20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-04-08T20:19:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-04-08T20:19:15)
    0000   0x4f 0x13 0x54 0x08 0x0d                   O.T..
    body (0)

#### RECORD 65 BolusWizard 2013-04-08T20:43:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.3,
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
    datetime (2013-04-08T20:43:08)
    0000   0x48 0x2b 0x14 0x08 0x0d                   H+...
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [0, 0, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 2.1, 'curve': 4},
 {'age': 23, 'amount': 1.1, 'curve': 20},
 {'age': 63, 'amount': 0.6, 'curve': 20},
 {'age': 153, 'amount': 2.2, 'curve': 20},
 {'age': 183, 'amount': 2.8, 'curve': 20},
 {'age': 213, 'amount': 0.8, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x54 0x1d 0x04 0x2c 0x17 0x14    \.T..,..
    0008   0x18 0x3f 0x14 0x58 0x99 0x14 0x70 0xb7    .?.X..p.
    0010   0x14 0x20 0xd5 0x14                        . ..
    decimal
             92   20   84   29    4   44   23   20
             24   63   20   88  153   20  112  183
             20   32  213   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-04-08T20:43:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-04-08T20:43:08)
    0000   0x48 0x2b 0x54 0x08 0x0d                   H+T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 68 CalBGForPH 2013-04-08T21:59:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2013-04-08T21:59:13)
    0000   0x4d 0x3b 0x35 0x08 0x0d                   M;5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 LowReservoir 2013-04-08T23:44:12 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-04-08T23:44:12)
    0000   0x4c 0x2c 0x17 0x08 0x0d                   L,...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 ResultTotals 2013-04-08T13:13:08 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x54                   ....T
    decimal
              7    0    0    5   84
    datetime (2013-04-08T13:13:08)
    0000   0x48 0x0d 0x6d 0x48 0x0d                   H.mH.
    body (51)
    hex
    0000   0x05 0x00 0x8a 0x62 0xb3 0x08 0x00 0x00    ...b....
    0008   0x05 0x54 0x03 0x78 0x41 0x01 0xdc 0x23    .T.xA..#
    0010   0x00 0x94 0x01 0xdc 0x23 0x01 0xbc 0x5d    ....#..]
    0018   0x00 0x20 0x07 0x00 0x00 0x00 0x07 0x06    . ......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x34 0x64 0x6b 0x02 0x0b 0x09 0x0d    .4dk....
    0030   0x1e 0x00 0x62                             ..b
    decimal
              5    0  138   98  179    8    0    0
              5   84    3  120   65    1  220   35
              0  148    1  220   35    1  188   93
              0   32    7    0    0    0    7    6
              1    0    0   12    0  232    0    0
              0   52  100  107    2   11    9   13
             30    0   98
    DAY BITS: [0, 1, 0]
#### RECORD 71 ChangeRemoteID (2004, 0, 0, 31, 13, 9) head[2], body[0] op[0x27]

    op hex (2)
    0000   0x27 0x0e                                  '.
    decimal
             39   14
    datetime ((2004, 0, 0, 31, 13, 9))
    0000   0x09 0x0d 0x1f 0x00 0x44                   ....D
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 72 Base (2001, 0, 27, 10, 13, 9) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x0f                                  ..
    decimal
             15   15
    datetime ((2001, 0, 27, 10, 13, 9))
    0000   0x09 0x0d 0x0a 0x5b 0x41                   ...[A
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 73 Base (2000, 0, 27, 27, 13, 9) head[2], body[0] op[0x3b]

    op hex (2)
    0000   0x3b 0x2f                                  ;/
    decimal
             59   47
    datetime ((2000, 0, 27, 27, 13, 9))
    0000   0x09 0x0d 0x5b 0x5b 0x60                   ..[[`
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 74 Base (2013, 0, 16, 7, 13, 9) head[2], body[0] op[0x3b]

    op hex (2)
    0000   0x3b 0x0f                                  ;.
    decimal
             59   15
    datetime ((2013, 0, 16, 7, 13, 9))
    0000   0x09 0x0d 0x27 0x50 0x0d                   ..'P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 75 Base (2000, 12, 0, 16, 30, 60) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 30, 60))
    0000   0xfc 0x1e 0xf0 0x00 0x00                   .....
    body (0)

#### RECORD 76 Base (2000, 4, 26, 26, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1a                                  ..
    decimal
              0   26
    datetime ((2000, 4, 26, 26, 1, 61))
    0000   0x7d 0x01 0x1a 0x1a 0x00                   }....
    body (0)

#### RECORD 77 Base (2010, 4, 10, 13, 9, 15) head[2], body[0] op[0x60]

    op hex (2)
    0000   0x60 0x3b                                  `;
    decimal
             96   59
    datetime ((2010, 4, 10, 13, 9, 15))
    0000   0x4f 0x09 0x0d 0x0a 0xca                   O....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 78 Base (2010, 0, 27, 13, 9, 50) head[2], body[0] op[0x60]

    op hex (2)
    0000   0x60 0x09                                  `.
    decimal
             96    9
    datetime ((2010, 0, 27, 13, 9, 50))
    0000   0x32 0x09 0x0d 0x5b 0xca                   2..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 79 Base (2000, 0, 0, 13, 9, 18) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x09                                  e.
    decimal
            101    9
    datetime ((2000, 0, 0, 13, 9, 18))
    0000   0x12 0x09 0x0d 0x00 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 80 Base (2000, 4, 0, 0, 17, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 17, 42))
    0000   0x6a 0x11 0x00 0x00 0x00                   j....
    body (0)

#### RECORD 81 CalBGForPH (2008, 1, 5, 28, 61, 7) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 0}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime ((2008, 1, 5, 28, 61, 7))
    0000   0x07 0x7d 0x5c 0x05 0x68                   .}\.h
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 82 Base (2005, 0, 0, 5, 5, 1) head[2], body[0] op[0x87]

    op hex (2)
    0000   0x87 0x04                                  ..
    decimal
            135    4
    datetime ((2005, 0, 0, 5, 5, 1))
    0000   0x01 0x05 0x05 0x00 0x65                   ....e
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 83 Base (2003, 0, 23, 10, 13, 9) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x52                                  .R
    decimal
              9   82
    datetime ((2003, 0, 23, 10, 13, 9))
    0000   0x09 0x0d 0x0a 0xf7 0x73                   ....s
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 84 Base (2003, 0, 6, 10, 13, 9) head[2], body[0] op[0x37]

    op hex (2)
    0000   0x37 0x33                                  73
    decimal
             55   51
    datetime ((2003, 0, 6, 10, 13, 9))
    0000   0x09 0x0d 0x0a 0xe6 0x43                   ....C
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 85 Base (2014, 0, 6, 27, 13, 9) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x33                                  83
    decimal
             56   51
    datetime ((2014, 0, 6, 27, 13, 9))
    0000   0x09 0x0d 0x5b 0xe6 0x5e                   ..[.^
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 86 Base (2013, 0, 16, 0, 13, 9) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x13                                  8.
    decimal
             56   19
    datetime ((2013, 0, 16, 0, 13, 9))
    0000   0x09 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 87 Base (2003, 0, 0, 0, 0, 23) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2003, 0, 0, 0, 0, 23))
    0000   0x17 0x00 0x00 0x00 0x03                   .....
    body (0)

#### RECORD 88 Base (2000, 5, 20, 8, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x14                                  ..
    decimal
              0   20
    datetime ((2000, 5, 20, 8, 28, 61))
    0000   0x7d 0x5c 0x08 0x14 0x70                   }\..p
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 89 Base (2004, 12, 20, 1, 4, 50) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x68                                  .h
    decimal
              4  104
    datetime ((2004, 12, 20, 1, 4, 50))
    0000   0xf2 0x04 0x01 0x14 0x14                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 90 Base (2001, 1, 13, 9, 19, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x5e                                  .^
    decimal
              0   94
    datetime ((2001, 1, 13, 9, 19, 56))
    0000   0x38 0x53 0x09 0x0d 0x21                   8S..!
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 91 Base (2003, 0, 13, 9, 20, 11) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x74                                  .t
    decimal
              0  116
    datetime ((2003, 0, 13, 9, 20, 11))
    0000   0x0b 0x14 0x09 0x0d 0x03                   .....
    body (0)

`end logs/ReadHistoryData-page-29.data: 92 records`
