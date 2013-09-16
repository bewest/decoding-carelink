## START logs/ReadHistoryData-page-35.data
#### STOPPING DOUBLE NULLS @ 226, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x40 0x00 0x00 0x00 0x00 0x40 0x36 0x5c    @....@6\
    0008   0x08 0xe8 0x81 0x04 0x6c 0x67 0x14 0x01    ....lg..
    0010   0x00 0x40 0x00 0x40 0x00 0x60 0x00 0x54    .@.@.`.T
    0018   0xf6 0x54 0x79 0x0d 0x5b 0x00 0x59 0xf3    .Ty.[.Y.
##### DEBUG DECIMAL
             64    0    0    0    0   64   54   92
              8  232  129    4  108  103   20    1
              0   64    0   64    0   96    0   84
            246   84  121   13   91    0   89  243
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
#### RECORD 6 Base (2009, 9, 14, 30, 27, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2009, 9, 14, 30, 27, 22))
    0000   0x96 0x5b 0x5e 0x4e 0xf9                   .[^N.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 7 Base (2014, 0, 0, 16, 20, 13) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x79                                  .y
    decimal
             14  121
    datetime ((2014, 0, 0, 16, 20, 13))
    0000   0x0d 0x14 0x90 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 8 ChangeTime (2000, 4, 0, 8, 0, 4) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x36                                  .6
    decimal
             23   54
    datetime ((2000, 4, 0, 8, 0, 4))
    0000   0x44 0x00 0x48 0x00 0x00                   D.H..
    body (0)

#### RECORD 9 Base (2012, 4, 14, 28, 54, 44) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2012, 4, 14, 28, 54, 44))
    0000   0x6c 0x36 0x5c 0x0e 0x1c                   l6\..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 Base (2014, 6, 12, 4, 54, 44) head[2], body[0] op[0x84]

    op hex (2)
    0000   0x84 0x04                                  ..
    decimal
            132    4
    datetime ((2014, 6, 12, 4, 54, 44))
    0000   0x6c 0xb6 0x04 0x4c 0x7e                   l..L~
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 11 SelectBasalProfile (2012, 12, 0, 1, 20, 4) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x34                                  .4
    decimal
             20   52
    datetime ((2012, 12, 0, 1, 20, 4))
    0000   0xc4 0x14 0x01 0x00 0x6c                   ....l
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 12 Base (2009, 0, 14, 0, 32, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6c                                  .l
    decimal
              0  108
    datetime ((2009, 0, 14, 0, 32, 0))
    0000   0x00 0x20 0x00 0x4e 0xf9                   . .N.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 13 Base (2013, 0, 4, 1, 10, 13) head[2], body[0] op[0x4e]

    op hex (2)
    0000   0x4e 0x79                                  Ny
    decimal
             78  121
    datetime ((2013, 0, 4, 1, 10, 13))
    0000   0x0d 0x0a 0x41 0x44 0xed                   ..AD.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 0]
#### RECORD 14 Base (2013, 0, 4, 8, 63, 13) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x79                                  1y
    decimal
             49  121
    datetime ((2013, 0, 4, 8, 63, 13))
    0000   0x0d 0x3f 0x08 0x44 0xed                   .?.D.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 0]
#### RECORD 15 Base (2010, 1, 22, 9, 41, 13) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x79                                  1y
    decimal
             49  121
    datetime ((2010, 1, 22, 9, 41, 13))
    0000   0x0d 0x69 0x69 0x96 0x0a                   .ii..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 16 Base (2015, 12, 13, 25, 50, 45) head[2], body[0] op[0xda]

    op hex (2)
    0000   0xda 0x62                                  .b
    decimal
            218   98
    datetime ((2015, 12, 13, 25, 50, 45))
    0000   0xed 0x32 0x79 0x0d 0x3f                   .2y.?
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 17 Base (2009, 13, 13, 25, 18, 45) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x62                                  .b
    decimal
             27   98
    datetime ((2009, 13, 13, 25, 18, 45))
    0000   0xed 0x52 0x79 0x0d 0x69                   .Ry.i
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 18 Base (2002, 5, 13, 12, 57, 27) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x96                                  i.
    decimal
            105  150
    datetime ((2002, 5, 13, 12, 57, 27))
    0000   0x5b 0x79 0x6c 0xed 0x12                   [yl..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 19 Base (2007, 2, 14, 0, 16, 35) head[2], body[0] op[0x79]

    op hex (2)
    0000   0x79 0x0d                                  y.
    decimal
            121   13
    datetime ((2007, 2, 14, 0, 16, 35))
    0000   0x23 0x90 0x00 0x6e 0x17                   #..n.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 20 Base (2008, 1, 0, 0, 60, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x74                                  6t
    decimal
             54  116
    datetime ((2008, 1, 0, 0, 60, 0))
    0000   0x00 0x7c 0x00 0x00 0x08                   .|...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 21 Base (2006, 1, 12, 11, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xe8                                  ..
    decimal
              0  232
    datetime ((2006, 1, 12, 11, 28, 54))
    0000   0x36 0x5c 0x0b 0x6c 0xe6                   6\.l.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 0]
#### RECORD 22 Base (2004, 4, 26, 12, 20, 40) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x1c                                  ..
    decimal
              4   28
    datetime ((2004, 4, 26, 12, 20, 40))
    0000   0x68 0x14 0x6c 0x9a 0x14                   h.l..
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 23 Base (2013, 7, 25, 18, 45, 44) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2013, 7, 25, 18, 45, 44))
    0000   0x6c 0xed 0x72 0x19 0x0d                   l.r..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 Base (2008, 0, 0, 8, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2008, 0, 0, 8, 0, 1))
    0000   0x01 0x00 0xe8 0x00 0xe8                   .....
    body (0)
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 25 Base (2009, 1, 18, 13, 44, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2009, 1, 18, 13, 44, 0))
    0000   0x00 0x6c 0xed 0x52 0x79                   .l.Ry
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 26 Base (2009, 1, 20, 22, 20, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2009, 1, 20, 22, 20, 0))
    0000   0x00 0x54 0xf6 0x14 0x79                   .T..y
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 27 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x12                                  ..
    decimal
             13   18
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-35.data: 28 records`
