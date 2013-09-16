## START logs/ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 534, found 17 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x7b 0x01 0x40 0xc0 0x04 0x1a 0x0d 0x08    {.@.....
    0008   0x2e 0x00 0x0a 0x90 0x5a 0xd2 0x28 0x7a    ....Z.(z
    0010   0x0d 0x3f 0x12 0x5a 0xd2 0x08 0x7a 0x0d    .?.Z..z.
    0018   0x69 0x69 0x96 0x0a 0x97 0x4c 0xda 0x28    ii...L.(
##### DEBUG DECIMAL
            123    1   64  192    4   26   13    8
             46    0   10  144   90  210   40  122
             13   63   18   90  210    8  122   13
            105  105  150   10  151   76  218   40
#### RECORD 0 BolusWizard 2013-07-25T12:46:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-25T12:46:34)
    0000   0x62 0xee 0x0c 0x79 0x0d                   b..y.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 2.7, 'curve': 4},
 {'age': 251, 'amount': 1.9, 'curve': 4},
 {'age': 65, 'amount': 1.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0x33 0x04 0x4c 0xfb 0x04    \.l3.L..
    0008   0x34 0x41 0x14                             4A.
    decimal
             92   11  108   51    4   76  251    4
             52   65   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-07-25T12:46:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x60 0x00    ......`.
    decimal
              1    0   28    0   28    0   96    0
    datetime (2013-07-25T12:46:34)
    0000   0x62 0xee 0x4c 0x79 0x0d                   b.Ly.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BasalProfileStart 2013-07-25T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-25T13:00:00)
    0000   0x40 0xc0 0x0d 0x19 0x0d                   @....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-25T14:56:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2013-07-25T14:56:56)
    0000   0x78 0xf8 0x2e 0x79 0x0d                   x..y.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 Base (2013, 7, 25, 14, 56, 56) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime ((2013, 7, 25, 14, 56, 56))
    0000   0x78 0xf8 0x2e 0x79 0x0d                   x..y.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 Ian69 (2009, 9, 14, 30, 27, 22) head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2009, 9, 14, 30, 27, 22))
    0000   0x96 0x5b 0x5e 0x4e 0xf9                   .[^N.
    body (8)
    hex
    0000   0x0e 0x79 0x0d 0x14 0x90 0x00 0x6e 0x17    .y....n.
    decimal
             14  121   13   20  144    0  110   23
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 7 Base (2000, 1, 0, 0, 8, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x44                                  6D
    decimal
             54   68
    datetime ((2000, 1, 0, 0, 8, 0))
    0000   0x00 0x48 0x00 0x00 0x20                   .H.. 
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 8 Base (2004, 1, 28, 14, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6c                                  .l
    decimal
              0  108
    datetime ((2004, 1, 28, 14, 28, 54))
    0000   0x36 0x5c 0x0e 0x1c 0x84                   6\...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 Base (2004, 8, 30, 12, 4, 54) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x6c                                  .l
    decimal
              4  108
    datetime ((2004, 8, 30, 12, 4, 54))
    0000   0xb6 0x04 0x4c 0x7e 0x14                   ..L~.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 LowReservoir (2000, 0, 12, 0, 1, 20) head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 19.6}
```
    op hex (2)
    0000   0x34 0xc4                                  4.
    decimal
             52  196
    datetime ((2000, 0, 12, 0, 1, 20))
    0000   0x14 0x01 0x00 0x6c 0x00                   ...l.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 11 Base (2014, 0, 25, 14, 0, 32) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x00                                  l.
    decimal
            108    0
    datetime ((2014, 0, 25, 14, 0, 32))
    0000   0x20 0x00 0x4e 0xf9 0x4e                    .N.N
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 12 Base (2001, 1, 13, 4, 1, 10) head[2], body[0] op[0x79]

    op hex (2)
    0000   0x79 0x0d                                  y.
    decimal
            121   13
    datetime ((2001, 1, 13, 4, 1, 10))
    0000   0x0a 0x41 0x44 0xed 0x31                   .AD.1
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 13 Base (2001, 0, 13, 4, 8, 63) head[2], body[0] op[0x79]

    op hex (2)
    0000   0x79 0x0d                                  y.
    decimal
            121   13
    datetime ((2001, 0, 13, 4, 8, 63))
    0000   0x3f 0x08 0x44 0xed 0x31                   ?.D.1
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 14 Base (2010, 5, 10, 22, 41, 41) head[2], body[0] op[0x79]

    op hex (2)
    0000   0x79 0x0d                                  y.
    decimal
            121   13
    datetime ((2010, 5, 10, 22, 41, 41))
    0000   0x69 0x69 0x96 0x0a 0xda                   ii...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 15 Base (2011, 1, 31, 13, 57, 50) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0xed                                  b.
    decimal
             98  237
    datetime ((2011, 1, 31, 13, 57, 50))
    0000   0x32 0x79 0x0d 0x3f 0x1b                   2y.?.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 16 Base (2009, 5, 9, 13, 57, 18) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0xed                                  b.
    decimal
             98  237
    datetime ((2009, 5, 9, 13, 57, 18))
    0000   0x52 0x79 0x0d 0x69 0x69                   Ry.ii
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 17 Base (2009, 5, 18, 13, 44, 57) head[2], body[0] op[0x96]

    op hex (2)
    0000   0x96 0x5b                                  .[
    decimal
            150   91
    datetime ((2009, 5, 18, 13, 44, 57))
    0000   0x79 0x6c 0xed 0x12 0x79                   yl..y
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 18 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x23                                  .#
    decimal
             13   35
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 19 Base (2000, 4, 8, 0, 0, 60) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0x00                                  t.
    decimal
            116    0
    datetime ((2000, 4, 8, 0, 0, 60))
    0000   0x7c 0x00 0x00 0x08 0x00                   |....
    body (0)

#### RECORD 20 Base (2004, 4, 6, 12, 11, 28) head[2], body[0] op[0xe8]

    op hex (2)
    0000   0xe8 0x36                                  .6
    decimal
            232   54
    datetime ((2004, 4, 6, 12, 11, 28))
    0000   0x5c 0x0b 0x6c 0xe6 0x04                   \.l..
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 21 Base (2009, 1, 20, 26, 44, 20) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x68                                  .h
    decimal
             28  104
    datetime ((2009, 1, 20, 26, 44, 20))
    0000   0x14 0x6c 0x9a 0x14 0x69                   .l..i
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 22 Base (2005, 13, 13, 25, 50, 45) head[2], body[0] op[0xd1]

    op hex (2)
    0000   0xd1 0x6c                                  .l
    decimal
            209  108
    datetime ((2005, 13, 13, 25, 50, 45))
    0000   0xed 0x72 0x19 0x0d 0x15                   .r...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 23 PumpSuspend 2000-03-08T00:40:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2000-03-08T00:40:00)
    0000   0x00 0xe8 0x00 0xe8 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 1, 1]
#### RECORD 24 ChangeBasalProfile 2013-07-25T18:45:44 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x00                                  ..
    decimal
              8    0
    datetime (2013-07-25T18:45:44)
    0000   0x6c 0xed 0x52 0x79 0x0d                   l.Ry.
    body (44)
    hex
    0000   0x5b 0x00 0x54 0xf6 0x14 0x79 0x0d 0x12    [.T..y..
    0008   0x90 0x00 0x6e 0x17 0x36 0x00 0x00 0x40    ..n.6..@
    0010   0x00 0x00 0x00 0x00 0x40 0x36 0x5c 0x08    ....@6\.
    0018   0xe8 0x81 0x04 0x6c 0x67 0x14 0x01 0x00    ...lg...
    0020   0x40 0x00 0x40 0x00 0x60 0x00 0x54 0xf6    @.@.`.T.
    0028   0x54 0x79 0x0d 0x5b                        Ty.[
    decimal
             91    0   84  246   20  121   13   18
            144    0  110   23   54    0    0   64
              0    0    0    0   64   54   92    8
            232  129    4  108  103   20    1    0
             64    0   64    0   96    0   84  246
             84  121   13   91
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 Base (2013, 12, 13, 25, 21, 51) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x59                                  .Y
    decimal
              0   89
    datetime ((2013, 12, 13, 25, 21, 51))
    0000   0xf3 0x15 0x79 0x0d 0x0d                   ..y..
    body (0)

#### RECORD 26 Base (2000, 4, 0, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 0, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x00 0x00                   n.6..
    body (0)

#### RECORD 27 Base (2006, 0, 12, 0, 0, 0) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x00                                  ,.
    decimal
             44    0
    datetime ((2006, 0, 12, 0, 0, 0))
    0000   0x00 0x00 0x00 0x2c 0x36                   ...,6
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 0.6, 'curve': 4},
 {'age': 66, 'amount': 1.0, 'curve': 4},
 {'age': 186, 'amount': 5.8, 'curve': 4},
 {'age': 160, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x38 0x04 0x28 0x42 0x04    \..8.(B.
    0008   0xe8 0xba 0x04 0x6c 0xa0 0x14              ...l..
    decimal
             92   14   24   56    4   40   66    4
            232  186    4  108  160   20
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-07-25T21:51:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x58 0x00    ..,.,.X.
    decimal
              1    0   44    0   44    0   88    0
    datetime (2013-07-25T21:51:25)
    0000   0x59 0xf3 0x55 0x79 0x0d                   Y.Uy.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 BolusWizard 2013-07-25T22:11:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-25T22:11:21)
    0000   0x55 0xcb 0x16 0x79 0x0d                   U..y.
    body (15)
    hex
    0000   0x1a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x5c 0x00 0x00 0x00 0x00 0x5c 0x36         \....\6
    decimal
             26  144    0  110   23   54    0    0
             92    0    0    0    0   92   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 1.1, 'curve': 4},
 {'age': 76, 'amount': 0.6, 'curve': 4},
 {'age': 86, 'amount': 1.0, 'curve': 4},
 {'age': 206, 'amount': 5.8, 'curve': 4},
 {'age': 180, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x2c 0x1a 0x04 0x18 0x4c 0x04    \.,...L.
    0008   0x28 0x56 0x04 0xe8 0xce 0x04 0x6c 0xb4    (V....l.
    0010   0x14                                       .
    decimal
             92   17   44   26    4   24   76    4
             40   86    4  232  206    4  108  180
             20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-07-25T22:11:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x70 0x00    ..p.p.p.
    decimal
              1    0  112    0  112    0  112    0
    datetime (2013-07-25T22:11:21)
    0000   0x55 0xcb 0x56 0x79 0x0d                   U.Vy.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 CalBGForPH 2013-07-25T23:17:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 248}
```
    op hex (2)
    0000   0x0a 0xf8                                  ..
    decimal
             10  248
    datetime (2013-07-25T23:17:30)
    0000   0x5e 0xd1 0x37 0x79 0x0d                   ^.7y.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 Base (2013, 7, 25, 23, 17, 30) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x1f                                  ?.
    decimal
             63   31
    datetime ((2013, 7, 25, 23, 17, 30))
    0000   0x5e 0xd1 0x17 0x79 0x0d                   ^..y.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 Ian69 2001-09-14T10:27:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2001-09-14T10:27:22)
    0000   0x96 0x5b 0x8a 0x6e 0xd1                   .[.n.
    body (8)
    hex
    0000   0x17 0x79 0x0d 0x00 0x90 0x00 0x6e 0x17    .y....n.
    decimal
             23  121   13    0  144    0  110   23
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 36 Base (2004, 0, 0, 0, 0, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x90                                  6.
    decimal
             54  144
    datetime ((2004, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x84                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 Base (2008, 1, 16, 17, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0c                                  ..
    decimal
              0   12
    datetime ((2008, 1, 16, 17, 28, 54))
    0000   0x36 0x5c 0x11 0x70 0x48                   6\.pH
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 38 Base (2004, 4, 14, 24, 4, 28) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x2c                                  .,
    decimal
              4   44
    datetime ((2004, 4, 14, 24, 4, 28))
    0000   0x5c 0x04 0x18 0x8e 0x04                   \....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 39 Base (2001, 3, 20, 16, 40, 4) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x98                                  (.
    decimal
             40  152
    datetime ((2001, 3, 20, 16, 40, 4))
    0000   0x04 0xe8 0x10 0x14 0x01                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 Base (2000, 0, 4, 0, 12, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0c                                  ..
    decimal
              0   12
    datetime ((2000, 0, 4, 0, 12, 0))
    0000   0x00 0x0c 0x00 0x84 0x00                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 41 Sara6E (2004, 0, 0, 4, 0, 1) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0xd1 0x57 0x79 0x0d 0x5b 0x8a 0x70    n.Wy.[.p
    0008   0xd6 0x17 0x79 0x0d 0x00 0x90 0x00 0x6e    ..y....n
    0010   0x17 0x36 0x90 0x00 0x00 0x00 0x00 0x8c    .6......
    0018   0x00 0x04 0x36 0x5c 0x14 0x0c 0x07 0x04    ..6\....
    0020   0x70 0x4d 0x04 0x2c 0x61 0x04 0x18 0x93    pM.,a...
    0028   0x04 0x28 0x9d 0x04 0xe8 0x15 0x14         .(.....
    decimal
            110  209   87  121   13   91  138  112
            214   23  121   13    0  144    0  110
             23   54  144    0    0    0    0  140
              0    4   54   92   20   12    7    4
            112   77    4   44   97    4   24  147
              4   40  157    4  232   21   20
    datetime ((2004, 0, 0, 4, 0, 1))
    0000   0x01 0x00 0x04 0x00 0x04                   .....
    body (0)

#### RECORD 42 Base (2009, 1, 23, 22, 48, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x8c                                  ..
    decimal
              0  140
    datetime ((2009, 1, 23, 22, 48, 0))
    0000   0x00 0x70 0xd6 0x57 0x79                   .p.Wy
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 43 Base (2010, 1, 0, 0, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x7b                                  .{
    decimal
             13  123
    datetime ((2010, 1, 0, 0, 0, 0))
    0000   0x00 0x40 0xc0 0x00 0x1a                   .@...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 44 Base (2000, 0, 0, 7, 0, 32) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2000, 0, 0, 7, 0, 32))
    0000   0x20 0x00 0x07 0x00 0x00                    ....
    body (0)

#### RECORD 45 ResultTotals (2013, 0, 25, 14, 0, 0) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0xa1 0x79 0x8d 0x00                   ..y..
    decimal
              7  161  121  141    0
    datetime ((2013, 0, 25, 14, 0, 0))
    0000   0x00 0x00 0x6e 0x79 0x8d                   ..ny.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 46 NoDelivery (2007, 12, 0, 0, 8, 56) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x00 0xa6 0x41                        ...A
    decimal
              6    0  166   65
    datetime ((2007, 12, 0, 0, 8, 56))
    0000   0xf8 0x08 0x00 0x00 0x07                   .....
    body (0)

#### RECORD 47 Base (2006, 8, 24, 4, 46, 9) head[2], body[0] op[0xa1]

    op hex (2)
    0000   0xa1 0x03                                  ..
    decimal
            161    3
    datetime ((2006, 8, 24, 4, 46, 9))
    0000   0x89 0x2e 0x04 0x18 0x36                   ....6
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 48 Base (2002, 1, 12, 0, 48, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xd0                                  ..
    decimal
              0  208
    datetime ((2002, 1, 12, 0, 48, 1))
    0000   0x01 0x70 0x00 0x8c 0x02                   .p...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 49 Base (2000, 0, 4, 5, 6, 0) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x00                                  ..
    decimal
             28    0
    datetime ((2000, 0, 4, 5, 6, 0))
    0000   0x00 0x06 0x05 0x04 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-35.data: 50 records`
