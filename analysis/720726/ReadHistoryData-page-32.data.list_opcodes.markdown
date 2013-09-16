## START logs/ReadHistoryData-page-32.data
#### STOPPING DOUBLE NULLS @ 301, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x48 0x00 0x00 0x00 0x00 0x48 0x36 0x5c    H....H6\
    0008   0x11 0x44 0x36 0x04 0x08 0x40 0x04 0x50    .D6..@.P
    0010   0x54 0x04 0xb4 0x12 0x14 0x48 0x8a 0x14    T....H..
    0018   0x01 0x00 0x58 0x00 0x58 0x00 0x78 0x00    ..X.X.x.
##### DEBUG DECIMAL
             72    0    0    0    0   72   54   92
             17   68   54    4    8   64    4   80
             84    4  180   18   20   72  138   20
              1    0   88    0   88    0  120    0
#### RECORD 0 BolusWizard 2013-07-29T14:12:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T14:12:39)
    0000   0x67 0xcc 0x0e 0x7d 0x0d                   g..}.
    body (13)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00                   H....
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2004, 4, 9, 20, 11, 28) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x36                                  H6
    decimal
             72   54
    datetime ((2004, 4, 9, 20, 11, 28))
    0000   0x5c 0x0b 0x74 0x89 0x04                   \.t..
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 2 Base (2011, 1, 20, 17, 48, 4) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x9d                                  x.
    decimal
            120  157
    datetime ((2011, 1, 20, 17, 48, 4))
    0000   0x04 0x70 0x51 0x14 0x5b                   .pQ.[
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 3 Base (2004, 12, 13, 29, 14, 12) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x69                                  .i
    decimal
              0  105
    datetime ((2004, 12, 13, 29, 14, 12))
    0000   0xcc 0x0e 0x7d 0x0d 0x14                   ..}..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 4 Base (2000, 4, 0, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 0, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x00 0x00                   n.6..
    body (0)

#### RECORD 5 Base (2006, 0, 8, 0, 0, 0) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x00                                  H.
    decimal
             72    0
    datetime ((2006, 0, 8, 0, 0, 0))
    0000   0x00 0x00 0x00 0x48 0x36                   ...H6
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 2.9, 'curve': 4},
 {'age': 157, 'amount': 3.0, 'curve': 4},
 {'age': 81, 'amount': 2.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x74 0x89 0x04 0x78 0x9d 0x04    \.t..x..
    0008   0x70 0x51 0x14                             pQ.
    decimal
             92   11  116  137    4  120  157    4
            112   81   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus (2009, 4, 0, 12, 0, 8) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x48 0x00                        ..H.
    decimal
              1    0   72    0
    datetime ((2009, 4, 0, 12, 0, 8))
    0000   0x48 0x00 0x4c 0x00 0x69                   H.L.i
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 8 Base (2004, 4, 0, 10, 13, 61) head[2], body[0] op[0xcc]

    op hex (2)
    0000   0xcc 0x4e                                  .N
    decimal
            204   78
    datetime ((2004, 4, 0, 10, 13, 61))
    0000   0x7d 0x0d 0x0a 0x80 0x44                   }...D
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 9 Base (2004, 4, 16, 31, 13, 61) head[2], body[0] op[0xf3]

    op hex (2)
    0000   0xf3 0x2e                                  ..
    decimal
            243   46
    datetime ((2004, 4, 16, 31, 13, 61))
    0000   0x7d 0x0d 0x3f 0x10 0x44                   }.?.D
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 10 Base (2006, 4, 9, 9, 13, 61) head[2], body[0] op[0xf3]

    op hex (2)
    0000   0xf3 0x0e                                  ..
    decimal
            243   14
    datetime ((2006, 4, 9, 9, 13, 61))
    0000   0x7d 0x0d 0x69 0x69 0x96                   }.ii.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 11 CalBGForPH 2013-07-29T16:06:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2013-07-29T16:06:32)
    0000   0x60 0xc6 0x30 0x7d 0x0d                   `.0}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 Base (2013, 7, 29, 16, 6, 32) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime ((2013, 7, 29, 16, 6, 32))
    0000   0x60 0xc6 0x10 0x7d 0x0d                   `..}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 Base (2006, 9, 13, 24, 27, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2006, 9, 13, 24, 27, 22))
    0000   0x96 0x5b 0x78 0x6d 0xc6                   .[xm.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 14 Base (2014, 0, 0, 16, 20, 13) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x7d                                  .}
    decimal
             16  125
    datetime ((2014, 0, 0, 16, 20, 13))
    0000   0x0d 0x14 0x90 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 15 ChangeTime (2000, 4, 0, 8, 0, 48) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x36                                  .6
    decimal
             23   54
    datetime ((2000, 4, 0, 8, 0, 48))
    0000   0x70 0x00 0x48 0x00 0x00                   p.H..
    body (0)

#### RECORD 16 Base (2008, 8, 14, 28, 54, 20) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x00                                  $.
    decimal
             36    0
    datetime ((2008, 8, 14, 28, 54, 20))
    0000   0x94 0x36 0x5c 0x0e 0x48                   .6\.H
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 17 Base (2015, 7, 24, 4, 59, 52) head[2], body[0] op[0x79]

    op hex (2)
    0000   0x79 0x04                                  y.
    decimal
            121    4
    datetime ((2015, 7, 24, 4, 59, 52))
    0000   0x74 0xfb 0x04 0x78 0x0f                   t..x.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 SelectBasalProfile (2004, 12, 0, 1, 20, 3) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x70                                  .p
    decimal
             20  112
    datetime ((2004, 12, 0, 1, 20, 3))
    0000   0xc3 0x14 0x01 0x00 0xb4                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 19 Base (2006, 0, 13, 0, 36, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xb4                                  ..
    decimal
              0  180
    datetime ((2006, 0, 13, 0, 36, 0))
    0000   0x00 0x24 0x00 0x6d 0xc6                   .$.m.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 20 Base (2013, 0, 4, 12, 10, 13) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x7d                                  P}
    decimal
             80  125
    datetime ((2013, 0, 4, 12, 10, 13))
    0000   0x0d 0x0a 0x4c 0x44 0xcd                   ..LD.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 21 TempBasal (2013, 0, 4, 9, 63, 13) head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 3.125}
```
    op hex (2)
    0000   0x33 0x7d                                  3}
    decimal
             51  125
    datetime ((2013, 0, 4, 9, 63, 13))
    0000   0x0d 0x3f 0x09 0x44 0xcd                   .?.D.
    body (1)
    hex
    0000   0x93                                       .
    decimal
            147
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 22 Base (2010, 5, 27, 22, 41, 41) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x0d                                  }.
    decimal
            125   13
    datetime ((2010, 5, 27, 22, 41, 41))
    0000   0x69 0x69 0x96 0x5b 0x2a                   ii.[*
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 23 Base (2000, 1, 28, 13, 61, 19) head[2], body[0] op[0x44]

    op hex (2)
    0000   0x44 0xd5                                  D.
    decimal
             68  213
    datetime ((2000, 1, 28, 13, 61, 19))
    0000   0x13 0x7d 0x0d 0x1c 0x90                   .}...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 24 Base (2004, 0, 0, 12, 54, 23) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6e                                  .n
    decimal
              0  110
    datetime ((2004, 0, 0, 12, 54, 23))
    0000   0x17 0x36 0xec 0x00 0x64                   .6..d
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 25 Base (2012, 0, 22, 16, 0, 24) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0x00                                  ..
    decimal
            248    0
    datetime ((2012, 0, 22, 16, 0, 24))
    0000   0x18 0x00 0x50 0x36 0x5c                   ..P6\
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 26 Base (2004, 12, 28, 8, 4, 4) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0xb4                                  ..
    decimal
             14  180
    datetime ((2004, 12, 28, 8, 4, 4))
    0000   0xc4 0x04 0x48 0x3c 0x14                   ..H<.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 27 Base (2009, 1, 20, 18, 56, 20) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0xbe                                  t.
    decimal
            116  190
    datetime ((2009, 1, 20, 18, 56, 20))
    0000   0x14 0x78 0xd2 0x14 0x69                   .x..i
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 28 Base (2005, 13, 13, 29, 51, 21) head[2], body[0] op[0xd1]

    op hex (2)
    0000   0xd1 0x44                                  .D
    decimal
            209   68
    datetime ((2005, 13, 13, 29, 51, 21))
    0000   0xd5 0x73 0x1d 0x0d 0x15                   .s...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 29 PumpSuspend 2000-01-16T00:16:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2000-01-16T00:16:00)
    0000   0x00 0x50 0x00 0x50 0x00                   .P.P.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 30 NewTimeSet 2013-07-29T19:21:04 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-07-29T19:21:04)
    0000   0x44 0xd5 0x53 0x7d 0x0d                   D.S}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2013-07-29T19:44:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T19:44:52)
    0000   0x74 0xec 0x13 0x7d 0x0d                   t..}.
    body (13)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00                   L....
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 Base (2004, 4, 29, 16, 14, 28) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0x36                                  L6
    decimal
             76   54
    datetime ((2004, 4, 29, 16, 14, 28))
    0000   0x5c 0x0e 0x50 0x1d 0x04                   \.P..
    body (0)

#### RECORD 33 Base (2004, 1, 20, 19, 8, 4) head[2], body[0] op[0xb4]

    op hex (2)
    0000   0xb4 0xdb                                  ..
    decimal
            180  219
    datetime ((2004, 1, 20, 19, 8, 4))
    0000   0x04 0x48 0x53 0x14 0x74                   .HS.t
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 34 Base (2012, 0, 0, 12, 0, 1) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x14                                  ..
    decimal
            213   20
    datetime ((2012, 0, 0, 12, 0, 1))
    0000   0x01 0x00 0x4c 0x00 0x4c                   ..L.L
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 35 Base (2013, 1, 19, 12, 52, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x5c                                  .\
    decimal
              0   92
    datetime ((2013, 1, 19, 12, 52, 0))
    0000   0x00 0x74 0xec 0x53 0x7d                   .t.S}
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 36 Base (2013, 1, 20, 7, 45, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2013, 1, 20, 7, 45, 0))
    0000   0x00 0x6d 0xe7 0x14 0x7d                   .m..}
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 37 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x14                                  ..
    decimal
             13   20
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-32.data: 38 records`
