## START logs/ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 304, found 132 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x09 0x04 0x72 0xcb 0x16 0x0d 0x0d 0x00    ..r.....
    0008   0x1d 0x00 0x08 0x1d 0x00 0x10 0x22 0x00    ......".
    0010   0x18 0x1d 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              9    4  114  203   22   13   13    0
             29    0    8   29    0   16   34    0
             24   29    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 136, 'amount': 4.45, 'curve': 192},
 {'age': 146, 'amount': 0.35, 'curve': 192},
 {'age': 236, 'amount': 1.85, 'curve': 192},
 {'age': 246, 'amount': 1.55, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0xb2 0x88 0xc0 0x0e 0x92 0xc0    \.......
    0008   0x4a 0xec 0xc0 0x3e 0xf6 0xc0              J..>..
    decimal
             92   14  178  136  192   14  146  192
             74  236  192   62  246  192
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2003, 4, 0, 0, 0, 8) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x48 0x00                        ..H.
    decimal
              1    0   72    0
    datetime ((2003, 4, 0, 0, 0, 8))
    0000   0x48 0x00 0x20 0x00 0x63                   H. .c
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 2 Base (2010, 4, 24, 10, 13, 45) head[2], body[0] op[0xc9]

    op hex (2)
    0000   0xc9 0x51                                  .Q
    decimal
            201   81
    datetime ((2010, 4, 24, 10, 13, 45))
    0000   0x6d 0x0d 0x0a 0xf8 0x6a                   m...j
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 3 Base (2005, 0, 24, 27, 13, 13) head[2], body[0] op[0xe9]

    op hex (2)
    0000   0xe9 0x32                                  .2
    decimal
            233   50
    datetime ((2005, 0, 24, 27, 13, 13))
    0000   0x0d 0x0d 0x5b 0xf8 0x55                   ..[.U
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 4 Base (2000, 0, 16, 29, 13, 13) head[2], body[0] op[0xea]

    op hex (2)
    0000   0xea 0x12                                  ..
    decimal
            234   18
    datetime ((2000, 0, 16, 29, 13, 13))
    0000   0x0d 0x0d 0x1d 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 5 ChangeTimeDisplay 2000-05-20T00:20:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-05-20T00:20:36)
    0000   0x64 0x54 0x00 0x74 0x00                   dT.t.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 Base (2001, 2, 28, 24, 44, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2001, 2, 28, 24, 44, 0))
    0000   0x00 0xac 0x78 0x5c 0x11                   ..x\.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 7 Base (2014, 14, 0, 5, 50, 0) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x63                                  Hc
    decimal
             72   99
    datetime ((2014, 14, 0, 5, 50, 0))
    0000   0xc0 0xb2 0xe5 0xc0 0x0e                   .....
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 1, 0]
#### RECORD 8 Base (2003, 5, 30, 16, 9, 10) head[2], body[0] op[0xef]

    op hex (2)
    0000   0xef 0xc0                                  ..
    decimal
            239  192
    datetime ((2003, 5, 30, 16, 9, 10))
    0000   0x4a 0x49 0xd0 0x3e 0x53                   JI.>S
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 9 Base (2000, 2, 12, 0, 44, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 2, 12, 0, 44, 0))
    0000   0x00 0xac 0x00 0xac 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 0, 1]
#### RECORD 10 Base (2013, 7, 13, 18, 42, 21) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x00                                  ..
    decimal
             28    0
    datetime ((2013, 7, 13, 18, 42, 21))
    0000   0x55 0xea 0x52 0x0d 0x0d                   U.R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 CalBGForPH 2013-07-13T19:11:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-07-13T19:11:00)
    0000   0x40 0xcb 0x33 0x0d 0x0d                   @.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 BolusWizard 2013-07-13T19:11:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 128,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 17.2,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-07-13T19:11:08)
    0000   0x48 0xcb 0x13 0x6d 0x0d                   H..m.
    body (13)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x04 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0xac 0x00                   8....
    decimal
             14   80    0  100   60  100    4    0
             56    0    0  172    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 Base (2000, 4, 28, 6, 23, 28) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x78                                  8x
    decimal
             56  120
    datetime ((2000, 4, 28, 6, 23, 28))
    0000   0x5c 0x17 0x86 0x1c 0xc0                   \....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 14 EnableDisableRemote (2002, 13, 0, 0, 8, 0) head[2], body[14] op[0x26]

    op hex (2)
    0000   0x26 0x26                                  &&
    decimal
             38   38
    datetime ((2002, 13, 0, 0, 8, 0))
    0000   0xc0 0x48 0x80 0xc0 0xb2                   .H...
    body (14)
    hex
    0000   0x02 0xd0 0x0e 0x0c 0xd0 0x4a 0x66 0xd0    .....Jf.
    0008   0x3e 0x70 0xd0 0x01 0x00 0x38              >p...8
    decimal
              2  208   14   12  208   74  102  208
             62  112  208    1    0   56
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 15 Base (2011, 2, 8, 0, 44, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x38                                  .8
    decimal
              0   56
    datetime ((2011, 2, 8, 0, 44, 0))
    0000   0x00 0xac 0x00 0x48 0xcb                   ...H.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 16 Base (2000, 0, 18, 23, 10, 13) head[2], body[0] op[0x53]

    op hex (2)
    0000   0x53 0x6d                                  Sm
    decimal
             83  109
    datetime ((2000, 0, 18, 23, 10, 13))
    0000   0x0d 0x0a 0x77 0x52 0xc0                   ..wR.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 17 LowReservoir 2000-01-26T23:27:13 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.3}
```
    op hex (2)
    0000   0x34 0x0d                                  4.
    decimal
             52   13
    datetime (2000-01-26T23:27:13)
    0000   0x0d 0x5b 0x77 0x5a 0xc0                   .[wZ.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 18 SelectBasalProfile (2004, 0, 0, 16, 22, 13) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x6d                                  .m
    decimal
             20  109
    datetime ((2004, 0, 0, 16, 22, 13))
    0000   0x0d 0x16 0x50 0x00 0x64                   ..P.d
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 Base (2000, 0, 0, 24, 0, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x64                                  <d
    decimal
             60  100
    datetime ((2000, 0, 0, 24, 0, 0))
    0000   0x00 0x00 0x58 0x00 0x00                   ..X..
    body (0)

#### RECORD 20 Base (2008, 5, 26, 28, 56, 24) head[2], body[0] op[0x8c]

    op hex (2)
    0000   0x8c 0x00                                  ..
    decimal
            140    0
    datetime ((2008, 5, 26, 28, 56, 24))
    0000   0x58 0x78 0x5c 0x1a 0x38                   Xx\.8
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 21 Base (2007, 9, 6, 0, 13, 6) head[2], body[0] op[0x39]

    op hex (2)
    0000   0x39 0xc0                                  9.
    decimal
             57  192
    datetime ((2007, 9, 6, 0, 13, 6))
    0000   0x86 0x4d 0xc0 0x26 0x57                   .M.&W
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 22 Base (2000, 11, 19, 18, 0, 49) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x48                                  .H
    decimal
            192   72
    datetime ((2000, 11, 19, 18, 0, 49))
    0000   0xb1 0xc0 0xb2 0x33 0xd0                   ...3.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 23 Base (2014, 13, 16, 23, 10, 16) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x3d                                  .=
    decimal
             14   61
    datetime ((2014, 13, 16, 23, 10, 16))
    0000   0xd0 0x4a 0x97 0xd0 0x3e                   .J..>
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 24 Base (2008, 0, 0, 24, 0, 1) head[2], body[0] op[0xa1]

    op hex (2)
    0000   0xa1 0xd0                                  ..
    decimal
            161  208
    datetime ((2008, 0, 0, 24, 0, 1))
    0000   0x01 0x00 0x58 0x00 0x58                   ..X.X
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 25 Base (2013, 1, 20, 0, 26, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x8c                                  ..
    decimal
              0  140
    datetime ((2013, 1, 20, 0, 26, 0))
    0000   0x00 0x5a 0xc0 0x54 0x6d                   .Z.Tm
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 26 Base (2013, 13, 21, 10, 17, 29) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2013, 13, 21, 10, 17, 29))
    0000   0xdd 0x51 0xea 0x35 0x0d                   .Q.5.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
#### RECORD 27 Base (2013, 13, 21, 10, 21, 29) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2013, 13, 21, 10, 21, 29))
    0000   0xdd 0x55 0xea 0x15 0x6d                   .U..m
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 28 Base (2004, 4, 28, 4, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2004, 4, 28, 4, 0, 16))
    0000   0x50 0x00 0x64 0x3c 0x64                   P.d<d
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 29 Base (2000, 0, 8, 0, 0, 0) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x00                                  @.
    decimal
             64    0
    datetime ((2000, 0, 8, 0, 0, 0))
    0000   0x00 0x00 0x00 0x28 0x00                   ...(.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 30 NewTimeSet (2000, 4, 13, 24, 23, 28) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x78                                  .x
    decimal
             24  120
    datetime ((2000, 4, 13, 24, 23, 28))
    0000   0x5c 0x17 0x58 0x6d 0xc0                   \.Xm.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 31 Base (2006, 14, 0, 19, 6, 0) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x9f                                  8.
    decimal
             56  159
    datetime ((2006, 14, 0, 19, 6, 0))
    0000   0xc0 0x86 0xb3 0xc0 0x26                   ....&
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 32 Base (2009, 4, 18, 16, 23, 8) head[2], body[0] op[0xbd]

    op hex (2)
    0000   0xbd 0xc0                                  ..
    decimal
            189  192
    datetime ((2009, 4, 18, 16, 23, 8))
    0000   0x48 0x17 0xd0 0xb2 0x99                   H....
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 33 Base (2008, 11, 0, 1, 16, 35) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x0e                                  ..
    decimal
            208   14
    datetime ((2008, 11, 0, 1, 16, 35))
    0000   0xa3 0xd0 0x01 0x00 0x18                   .....
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 34 Base (2010, 0, 21, 0, 40, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x18                                  ..
    decimal
              0   24
    datetime ((2010, 0, 21, 0, 40, 0))
    0000   0x00 0x28 0x00 0x55 0xea                   .(.U.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 0]
#### RECORD 35 Base (2011, 0, 18, 4, 8, 13) head[2], body[0] op[0x55]

    op hex (2)
    0000   0x55 0x6d                                  Um
    decimal
             85  109
    datetime ((2011, 0, 18, 4, 8, 13))
    0000   0x0d 0x08 0x04 0x72 0xcb                   ...r.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 36 TempBasalDuration (2008, 0, 0, 28, 0, 13) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 390}
```
    op hex (2)
    0000   0x16 0x0d                                  ..
    decimal
             22   13
    datetime ((2008, 0, 0, 28, 0, 13))
    0000   0x0d 0x00 0x1c 0x00 0x08                   .....
    body (0)

#### RECORD 37 Base (2012, 0, 24, 0, 35, 16) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x00                                  ..
    decimal
             28    0
    datetime ((2012, 0, 24, 0, 35, 16))
    0000   0x10 0x23 0x00 0x18 0x1c                   .#...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
`end logs/ReadHistoryData-page-28.data: 38 records`
