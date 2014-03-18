## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 369, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x80 0x8f 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x0a 0xac 0x1d 0xc1 0x21 0x11    ......!.
    0010   0x0e 0x5b 0xac 0x21 0xc1 0x01 0x71 0x0e    .[.!..q.
    0018   0x00 0x50 0x00 0x6e 0x37 0x50 0x34 0x00    .P.n7P4.
##### DEBUG DECIMAL
            128  143    0    0    0    0    0    0
              0    0   10  172   29  193   33   17
             14   91  172   33  193    1  113   14
              0   80    0  110   55   80   52    0
#### RECORD 0 BasalProfileStart 2014-03-16T15:53:40 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T15:53:40)
    0000   0x28 0xf5 0x0f 0x10 0x0e                   (....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 1 PumpSuspend 2014-03-16T15:55:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T15:55:20)
    0000   0x14 0xf7 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 2 PumpResume 2014-03-16T15:56:22 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T15:56:22)
    0000   0x16 0xf8 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 3 BasalProfileStart 2014-03-16T15:56:22 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T15:56:22)
    0000   0x16 0xf8 0x0f 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 4 PumpSuspend 2014-03-16T16:05:14 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T16:05:14)
    0000   0x0e 0xc5 0x10 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 5 PumpResume 2014-03-16T16:06:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T16:06:31)
    0000   0x1f 0xc6 0x10 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 6 BasalProfileStart 2014-03-16T16:06:31 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T16:06:31)
    0000   0x1f 0xc6 0x10 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2014-03-16T18:32:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2014-03-16T18:32:15)
    0000   0x0f 0xe0 0x32 0x70 0x0e                   ..2p.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2014-03-16T18:32:15 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-03-16T18:32:15)
    0000   0x0f 0xe0 0xf2 0x70 0x0e                   ...p.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 CalBGForPH 2014-03-16T18:52:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2014-03-16T18:52:26)
    0000   0x1a 0xf4 0x32 0x10 0x0e                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 BolusWizard 2014-03-16T18:52:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 3.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2014-03-16T18:52:29)
    0000   0x1d 0xf4 0x12 0x10 0x0e                   .....
    body (13)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x20 0x00    .P.x2P .
    0008   0x00 0x00 0x00 0x00 0x00                   .....
    decimal
              0   80    0  120   50   80   32    0
              0    0    0    0    0
    HOUR BITS: [1, 1, 1]
#### RECORD 11 Base (2000, 4, 8, 28, 5, 28) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x64                                   d
    decimal
             32  100
    datetime ((2000, 4, 8, 28, 5, 28))
    0000   0x5c 0x05 0xfc 0x68 0x90                   \..h.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 12 Bolus (2013, 0, 0, 0, 0, 32) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x20 0x00                        .. .
    decimal
              1    0   32    0
    datetime ((2013, 0, 0, 0, 0, 32))
    0000   0x20 0x00 0x00 0x00 0x1d                    ....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 13 Base (2014, 0, 15, 27, 14, 16) head[2], body[0] op[0xf4]

    op hex (2)
    0000   0xf4 0x52                                  .R
    decimal
            244   82
    datetime ((2014, 0, 15, 27, 14, 16))
    0000   0x10 0x0e 0x5b 0x8f 0x1e                   ..[..
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 14 Base (2000, 4, 16, 22, 14, 48) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x13                                  ..
    decimal
            192   19
    datetime ((2000, 4, 16, 22, 14, 48))
    0000   0x70 0x0e 0x16 0x50 0x00                   p..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 15 Sara6E 2000-02-19T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2000-02-19T00:00:00)
    0000   0x32 0x50                                  2P
    body (49)
    hex
    0000   0x20 0x00 0x50 0x00 0x00 0x20 0x00 0x50     .P.. .P
    0008   0x64 0x5c 0x08 0x20 0x08 0x80 0xfc 0x70    d\. ...p
    0010   0x90 0x01 0x00 0x50 0x00 0x50 0x00 0x20    ...P.P. 
    0018   0x00 0x1e 0xc0 0x53 0x70 0x0e 0x5b 0x00    ...Sp.[.
    0020   0x0f 0xf6 0x13 0x70 0x0e 0x3c 0x50 0x00    ...p.<P.
    0028   0x6e 0x32 0x50 0x00 0x00 0xd8 0x00 0x00    n2P.....
    0030   0x00                                       .
    decimal
             32    0   80    0    0   32    0   80
            100   92    8   32    8  128  252  112
            144    1    0   80    0   80    0   32
              0   30  192   83  112   14   91    0
             15  246   19  112   14   60   80    0
            110   50   80    0    0  216    0    0
              0
    HOUR BITS: [0, 1, 0]
#### RECORD 16 Base (2014, 5, 16, 8, 28, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xd8                                  ..
    decimal
              0  216
    datetime ((2014, 5, 16, 8, 28, 36))
    0000   0x64 0x5c 0x08 0x70 0x3e                   d\.p>
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 17 Base (2011, 10, 8, 20, 16, 38) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0xfc                                  ..
    decimal
            128  252
    datetime ((2011, 10, 8, 20, 16, 38))
    0000   0xa6 0x90 0x34 0xc8 0x1b                   ..4..
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 18 Base (2008, 0, 0, 1, 14, 16) head[2], body[0] op[0xf6]

    op hex (2)
    0000   0xf6 0x13                                  ..
    decimal
            246   19
    datetime ((2008, 0, 0, 1, 14, 16))
    0000   0x10 0x0e 0x01 0x00 0xd8                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 1]
#### RECORD 19 Base (2006, 0, 15, 0, 52, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xd8                                  ..
    decimal
              0  216
    datetime ((2006, 0, 15, 0, 52, 0))
    0000   0x00 0x34 0x00 0x0f 0xf6                   .4...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 20 Base (2008, 0, 1, 27, 6, 14) head[2], body[0] op[0x53]

    op hex (2)
    0000   0x53 0x70                                  Sp
    decimal
             83  112
    datetime ((2008, 0, 1, 27, 6, 14))
    0000   0x0e 0x06 0x3b 0x01 0x08                   ..;..
    body (0)

#### RECORD 21 Base (2011, 7, 12, 14, 16, 52) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0xdf                                  ..
    decimal
             28  223
    datetime ((2011, 7, 12, 14, 16, 52))
    0000   0x74 0xd0 0x0e 0x0c 0x3b                   t...;
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 22 Base (2004, 0, 27, 14, 16, 20) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0xea                                  ..
    decimal
             14  234
    datetime ((2004, 0, 27, 14, 16, 20))
    0000   0x14 0x10 0x0e 0x7b 0x04                   ...{.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 23 Base (2000, 0, 21, 14, 16, 20) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0xea                                  ..
    decimal
             15  234
    datetime ((2000, 0, 21, 14, 16, 20))
    0000   0x14 0x10 0x0e 0x15 0x10                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 24 Base (2000, 0, 22, 30, 0, 5) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2000, 0, 22, 30, 0, 5))
    0000   0x05 0x00 0xde 0x16 0x10                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 25 Base (2011, 0, 19, 10, 0, 21) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x2d                                  .-
    decimal
             14   45
    datetime ((2011, 0, 19, 10, 0, 21))
    0000   0x15 0x00 0x0a 0xb3 0x2b                   ....+
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 26 Base (2011, 4, 22, 31, 14, 48) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0x37                                  .7
    decimal
            248   55
    datetime ((2011, 4, 22, 31, 14, 48))
    0000   0x70 0x0e 0x3f 0x16 0x2b                   p.?.+
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 27 Base (2005, 4, 9, 2, 14, 48) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0x77                                  .w
    decimal
            248  119
    datetime ((2005, 4, 9, 2, 14, 48))
    0000   0x70 0x0e 0xc2 0x89 0x65                   p...e
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 28 BolusWizard 2014-03-16T23:56:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 179,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb3                                  [.
    decimal
             91  179
    datetime (2014-03-16T23:56:54)
    0000   0x36 0xf8 0x17 0x10 0x0e                   6....
    body (13)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x38 0x00    .P.n7P8.
    0008   0x00 0x00 0x00 0x00 0x00                   .....
    decimal
              0   80    0  110   55   80   56    0
              0    0    0    0    0
    HOUR BITS: [1, 1, 1]
#### RECORD 29 Base (2000, 4, 20, 24, 8, 28) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x64                                  8d
    decimal
             56  100
    datetime ((2000, 4, 20, 24, 8, 28))
    0000   0x5c 0x08 0xd8 0xf4 0x80                   \....
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 Base (2000, 8, 24, 0, 1, 16) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x30                                  p0
    decimal
            112   48
    datetime ((2000, 8, 24, 0, 1, 16))
    0000   0x90 0x01 0x00 0x58 0x00                   ...X.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 31 Base (2007, 0, 24, 22, 0, 0) head[2], body[0] op[0x58]

    op hex (2)
    0000   0x58 0x00                                  X.
    decimal
             88    0
    datetime ((2007, 0, 24, 22, 0, 0))
    0000   0x00 0x00 0x36 0xf8 0x57                   ..6.W
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 32 Base (2000, 4, 0, 0, 0, 59) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x0e                                  ..
    decimal
             16   14
    datetime ((2000, 4, 0, 0, 0, 59))
    0000   0x7b 0x00 0x00 0xc0 0x00                   {....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 33 Base (2000, 0, 7, 0, 21, 0) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x0e                                  ..
    decimal
             17   14
    datetime ((2000, 0, 7, 0, 21, 0))
    0000   0x00 0x15 0x00 0x07 0x00                   .....
    body (0)

#### RECORD 34 Base (2000, 4, 0, 14, 48, 58) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2000, 4, 0, 14, 48, 58))
    0000   0x7a 0x30 0x8e 0x00 0x00                   z0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 Base (2004, 2, 0, 5, 14, 48) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6e                                  .n
    decimal
              0  110
    datetime ((2004, 2, 0, 5, 14, 48))
    0000   0x30 0x8e 0x05 0x00 0x94                   0....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 36 Base (2010, 0, 4, 0, 0, 4) head[2], body[0] op[0x8f]

    op hex (2)
    0000   0x8f 0xb3                                  ..
    decimal
            143  179
    datetime ((2010, 0, 4, 0, 0, 4))
    0000   0x04 0x00 0x00 0x04 0x7a                   ....z
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 37 Bolus 2001-08-24T00:58:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 22.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0xde 0x2a 0x02                        ..*.
    decimal
              1  222   42    2
    datetime (2001-08-24T00:58:28)
    0000   0x9c 0x3a 0x00 0x98 0x01                   .:...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 0]
#### RECORD 38 Base (2000, 4, 0, 28, 0, 56) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x00                                  (.
    decimal
             40    0
    datetime ((2000, 4, 0, 28, 0, 56))
    0000   0x78 0x00 0xfc 0x00 0x00                   x....
    body (0)

#### RECORD 39 Base (2000, 0, 0, 0, 0, 1) head[2], body[0] op[0x02]

    op hex (2)
    0000   0x02 0x02                                  ..
    decimal
              2    2
    datetime ((2000, 0, 0, 0, 0, 1))
    0000   0x01 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-0.data: 40 records`
