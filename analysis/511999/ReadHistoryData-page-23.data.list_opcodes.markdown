## START logs/ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 412, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x80 0x78 0x5c 0x26 0x04 0xbd 0xc0 0x06    .x\&....
    0008   0xc7 0xc0 0x08 0xd1 0xc0 0x06 0xdb 0xc0    ........
    0010   0x08 0xe5 0xc0 0x08 0xef 0xc0 0x06 0xf9    ........
    0018   0xc0 0x08 0x03 0xd0 0x06 0x0d 0xd0 0x04    ........
##### DEBUG DECIMAL
            128  120   92   38    4  189  192    6
            199  192    8  209  192    6  219  192
              8  229  192    8  239  192    6  249
            192    8    3  208    6   13  208    4
#### RECORD 0 CalBGForPH 2013-07-18T09:19:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-07-18T09:19:47)
    0000   0x6f 0xd3 0x29 0x12 0x0d                   o.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 BolusWizard 2013-07-18T09:19:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 92,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 24.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-07-18T09:19:56)
    0000   0x78 0xd3 0x09 0x72 0x0d                   x..r.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0xf8 0x00    .P.x<d..
    0008   0x40 0xf8 0x00 0x00 0x00 0x38 0x78         @....8x
    decimal
             20   80    0  120   60  100  248    0
             64  248    0    0    0   56  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 Bolus (2008, 0, 0, 0, 0, 56) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x38 0x00                        ..8.
    decimal
              1    0   56    0
    datetime ((2008, 0, 0, 0, 0, 56))
    0000   0x38 0x00 0x00 0x00 0x78                   8...x
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 3 Base (2012, 4, 19, 10, 13, 50) head[2], body[0] op[0xd3]

    op hex (2)
    0000   0xd3 0x49                                  .I
    decimal
            211   73
    datetime ((2012, 4, 19, 10, 13, 50))
    0000   0x72 0x0d 0x0a 0x73 0x4c                   r..sL
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 4 Base (2001, 0, 19, 27, 13, 18) head[2], body[0] op[0xd4]

    op hex (2)
    0000   0xd4 0x2a                                  .*
    decimal
            212   42
    datetime ((2001, 0, 19, 27, 13, 18))
    0000   0x12 0x0d 0x5b 0x73 0x51                   ..[sQ
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 5 Base (2000, 4, 16, 11, 13, 50) head[2], body[0] op[0xd4]

    op hex (2)
    0000   0xd4 0x0a                                  ..
    decimal
            212   10
    datetime ((2000, 4, 16, 11, 13, 50))
    0000   0x72 0x0d 0x0b 0x50 0x00                   r..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2000, 4, 4, 0, 0, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 4, 4, 0, 0, 36))
    0000   0x64 0x00 0x00 0x24 0x00                   d..$.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 7 Base (2005, 0, 28, 24, 36, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x28                                  .(
    decimal
              0   40
    datetime ((2005, 0, 28, 24, 36, 0))
    0000   0x00 0x24 0x78 0x5c 0x05                   .$x\.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 8 Base (2000, 12, 4, 0, 1, 0) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x43                                  8C
    decimal
             56   67
    datetime ((2000, 12, 4, 0, 1, 0))
    0000   0xc0 0x01 0x00 0x24 0x00                   ...$.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 9 Base (2010, 0, 20, 18, 0, 40) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x00                                  $.
    decimal
             36    0
    datetime ((2010, 0, 20, 18, 0, 40))
    0000   0x28 0x00 0x52 0xd4 0x4a                   (.R.J
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 10 Base (2012, 4, 0, 0, 3, 59) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x0d                                  r.
    decimal
            114   13
    datetime ((2012, 4, 0, 0, 3, 59))
    0000   0x7b 0x03 0x40 0xc0 0x0c                   {.@..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 11 Base (2001, 0, 10, 0, 29, 24) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0x0d                                  ..
    decimal
             18   13
    datetime ((2001, 0, 10, 0, 29, 24))
    0000   0x18 0x1d 0x00 0x0a 0x51                   ....Q
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 12 Base (2001, 0, 27, 13, 18, 44) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0xe4                                  H.
    decimal
             72  228
    datetime ((2001, 0, 27, 13, 18, 44))
    0000   0x2c 0x12 0x0d 0x5b 0x51                   ,..[Q
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 13 Base (2000, 1, 19, 13, 50, 12) head[2], body[0] op[0x4f]

    op hex (2)
    0000   0x4f 0xe4                                  O.
    decimal
             79  228
    datetime ((2000, 1, 19, 13, 50, 12))
    0000   0x0c 0x72 0x0d 0x13 0x50                   .r..P
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 14 Base (2012, 1, 0, 20, 36, 60) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2012, 1, 0, 20, 36, 60))
    0000   0x3c 0x64 0xf4 0x00 0x3c                   <d..<
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 15 Base (2012, 0, 24, 16, 0, 8) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0x00                                  ..
    decimal
            248    0
    datetime ((2012, 0, 24, 16, 0, 8))
    0000   0x08 0x00 0x30 0x78 0x5c                   ..0x\
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 16 ChangeBasalProfile (2000, 11, 11, 24, 0, 15) head[2], body[42] op[0x08]

    op hex (2)
    0000   0x08 0x24                                  .$
    decimal
              8   36
    datetime ((2000, 11, 11, 24, 0, 15))
    0000   0x8f 0xc0 0x38 0xcb 0xc0                   ..8..
    body (42)
    hex
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x08 0x00    ..0.0...
    0008   0x4f 0xe4 0x4c 0x72 0x0d 0x0a 0xbc 0x6b    O.Lr...k
    0010   0xd1 0x2e 0x12 0x0d 0x5b 0xbc 0x6e 0xd1    ....[.n.
    0018   0x0e 0x72 0x0d 0x00 0x50 0x00 0x78 0x3c    .r..P.x<
    0020   0x64 0x2c 0x00 0x00 0x00 0x00 0x14 0x00    d,......
    0028   0x18 0x78                                  .x
    decimal
              1    0   48    0   48    0    8    0
             79  228   76  114   13   10  188  107
            209   46   18   13   91  188  110  209
             14  114   13    0   80    0  120   60
            100   44    0    0    0    0   20    0
             24  120
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 1.2, 'curve': 192},
 {'age': 244, 'amount': 0.9, 'curve': 192},
 {'age': 48, 'amount': 1.4, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x68 0xc0 0x24 0xf4 0xc0    \.0h.$..
    0008   0x38 0x30 0xd0                             80.
    decimal
             92   11   48  104  192   36  244  192
             56   48  208
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus (2014, 0, 0, 20, 0, 24) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x18 0x00                        ....
    decimal
              1    0   24    0
    datetime ((2014, 0, 0, 20, 0, 24))
    0000   0x18 0x00 0x14 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 Base (2005, 4, 13, 10, 13, 50) head[2], body[0] op[0xd1]

    op hex (2)
    0000   0xd1 0x4e                                  .N
    decimal
            209   78
    datetime ((2005, 4, 13, 10, 13, 50))
    0000   0x72 0x0d 0x0a 0x0d 0x45                   r...E
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 20 Base (2007, 2, 13, 27, 13, 18) head[2], body[0] op[0xc2]

    op hex (2)
    0000   0xc2 0x2f                                  ./
    decimal
            194   47
    datetime ((2007, 2, 13, 27, 13, 18))
    0000   0x12 0x8d 0x5b 0x0d 0x47                   ..[.G
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 21 Base (2000, 4, 17, 0, 13, 50) head[2], body[0] op[0xc2]

    op hex (2)
    0000   0xc2 0x0f                                  ..
    decimal
            194   15
    datetime ((2000, 4, 17, 0, 13, 50))
    0000   0x72 0x0d 0x00 0x51 0x00                   r..Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 22 Base (2000, 5, 0, 0, 32, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 5, 0, 0, 32, 36))
    0000   0x64 0x60 0x00 0x00 0x00                   d`...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 Base (2014, 1, 28, 24, 4, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2014, 1, 28, 24, 4, 0))
    0000   0x00 0x44 0x78 0x5c 0x0e                   .Dx\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 24 NewTimeSet (2004, 12, 0, 21, 48, 0) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x31                                  .1
    decimal
             24   49
    datetime ((2004, 12, 0, 21, 48, 0))
    0000   0xc0 0x30 0x95 0xc0 0x24                   .0..$
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 25 Rewind 2000-01-01T16:29:56 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0xd0                                  !.
    decimal
             33  208
    datetime (2000-01-01T16:29:56)
    0000   0x38 0x5d 0xd0 0x01 0x00                   8]...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 26 Base (2007, 4, 0, 28, 0, 4) head[2], body[0] op[0x44]

    op hex (2)
    0000   0x44 0x00                                  D.
    decimal
             68    0
    datetime ((2007, 4, 0, 28, 0, 4))
    0000   0x44 0x00 0x1c 0x00 0x47                   D...G
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 27 Base (2015, 4, 28, 10, 13, 50) head[2], body[0] op[0xc2]

    op hex (2)
    0000   0xc2 0x4f                                  .O
    decimal
            194   79
    datetime ((2015, 4, 28, 10, 13, 50))
    0000   0x72 0x0d 0x0a 0x3c 0x5f                   r..<_
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 28 Base (2001, 2, 28, 27, 13, 18) head[2], body[0] op[0xc4]

    op hex (2)
    0000   0xc4 0x30                                  .0
    decimal
            196   48
    datetime ((2001, 2, 28, 27, 13, 18))
    0000   0x12 0x8d 0x5b 0x3c 0x61                   ..[<a
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 29 Base (2000, 4, 17, 0, 13, 50) head[2], body[0] op[0xc4]

    op hex (2)
    0000   0xc4 0x10                                  ..
    decimal
            196   16
    datetime ((2000, 4, 17, 0, 13, 50))
    0000   0x72 0x0d 0x00 0x51 0x00                   r..Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 30 Base (2000, 6, 0, 0, 0, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 6, 0, 0, 0, 36))
    0000   0x64 0x80 0x00 0x00 0x00                   d....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 Base (2004, 1, 28, 24, 12, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x34                                  .4
    decimal
              0   52
    datetime ((2004, 1, 28, 24, 12, 0))
    0000   0x00 0x4c 0x78 0x5c 0x14                   .Lx\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 32 Base (2008, 12, 0, 7, 54, 0) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x3d                                  .=
    decimal
             14   61
    datetime ((2008, 12, 0, 7, 54, 0))
    0000   0xc0 0x36 0x47 0xc0 0x18                   .6G..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 33 Base (2015, 3, 4, 0, 19, 48) head[2], body[0] op[0x6f]

    op hex (2)
    0000   0x6f 0xc0                                  o.
    decimal
            111  192
    datetime ((2015, 3, 4, 0, 19, 48))
    0000   0x30 0xd3 0xc0 0x24 0x5f                   0..$_
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 34 Base (2012, 11, 0, 1, 16, 27) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x38                                  .8
    decimal
            208   56
    datetime ((2012, 11, 0, 1, 16, 27))
    0000   0x9b 0xd0 0x01 0x00 0x4c                   ....L
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 35 Base (2004, 0, 1, 0, 52, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x4c                                  .L
    decimal
              0   76
    datetime ((2004, 0, 1, 0, 52, 0))
    0000   0x00 0x34 0x00 0x61 0xc4                   .4.a.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 36 Base (2011, 0, 3, 23, 10, 13) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x72                                  Pr
    decimal
             80  114
    datetime ((2011, 0, 3, 23, 10, 13))
    0000   0x0d 0x0a 0x77 0x63 0xdb                   ..wc.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 37 Base (2011, 1, 25, 23, 27, 13) head[2], body[0] op[0x32]

    op hex (2)
    0000   0x32 0x12                                  2.
    decimal
             50   18
    datetime ((2011, 1, 25, 23, 27, 13))
    0000   0x0d 0x5b 0x77 0x79 0xdb                   .[wy.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 38 Base (2004, 0, 0, 16, 27, 13) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0x72                                  .r
    decimal
             18  114
    datetime ((2004, 0, 0, 16, 27, 13))
    0000   0x0d 0x1b 0x50 0x00 0x64                   ..P.d
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 39 Base (2000, 0, 0, 12, 0, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x64                                  <d
    decimal
             60  100
    datetime ((2000, 0, 0, 12, 0, 0))
    0000   0x00 0x00 0x6c 0x00 0x00                   ..l..
    body (0)

#### RECORD 40 ClearAlarm (2012, 5, 17, 28, 56, 44) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x00                                  ..
    decimal
             12    0
    datetime ((2012, 5, 17, 28, 56, 44))
    0000   0x6c 0x78 0x5c 0x11 0x4c                   lx\.L
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 41 Base (2006, 3, 22, 0, 12, 14) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0xc0                                  ..
    decimal
            144  192
    datetime ((2006, 3, 22, 0, 12, 14))
    0000   0x0e 0xcc 0xc0 0x36 0xd6                   ...6.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 42 Base (2000, 15, 2, 16, 0, 62) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x18                                  ..
    decimal
            192   24
    datetime ((2000, 15, 2, 16, 0, 62))
    0000   0xfe 0xc0 0x30 0x62 0xd0                   ..0b.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 43 Bolus 2009-04-03T12:00:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x40 0x00                        ..@.
    decimal
              1    0   64    0
    datetime (2009-04-03T12:00:00)
    0000   0x40 0x00 0x0c 0x03 0x79                   @...y
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 44 Base (2002, 4, 15, 10, 13, 50) head[2], body[0] op[0xdb]

    op hex (2)
    0000   0xdb 0x72                                  .r
    decimal
            219  114
    datetime ((2002, 4, 15, 10, 13, 50))
    0000   0x72 0x0d 0x0a 0x6f 0x42                   r..oB
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 45 Base (2004, 0, 27, 10, 13, 18) head[2], body[0] op[0xf9]

    op hex (2)
    0000   0xf9 0x35                                  .5
    decimal
            249   53
    datetime ((2004, 0, 27, 10, 13, 18))
    0000   0x12 0x0d 0x0a 0xfb 0x54                   ....T
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 46 Base (2009, 0, 27, 27, 13, 18) head[2], body[0] op[0xc2]

    op hex (2)
    0000   0xc2 0x37                                  .7
    decimal
            194   55
    datetime ((2009, 0, 27, 27, 13, 18))
    0000   0x12 0x0d 0x5b 0xfb 0x59                   ..[.Y
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 47 Base (2000, 4, 16, 11, 13, 50) head[2], body[0] op[0xc2]

    op hex (2)
    0000   0xc2 0x17                                  ..
    decimal
            194   23
    datetime ((2000, 4, 16, 11, 13, 50))
    0000   0x72 0x0d 0x0b 0x50 0x00                   r..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 48 ChangeTimeDisplay 2000-05-12T00:20:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-05-12T00:20:36)
    0000   0x64 0x54 0x00 0x2c 0x00                   dT.,.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-23.data: 49 records`
