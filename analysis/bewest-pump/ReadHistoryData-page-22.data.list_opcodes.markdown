## START logs/ReadHistoryData-page-22.data
#### STOPPING DOUBLE NULLS @ 391, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x64 0x7c 0x00 0x00 0x00 0x00 0x00 0x00    d|......
    0008   0x00 0x00 0x7b 0x01 0x40 0xc0 0x04 0x15    ..{.@...
    0010   0x0d 0x08 0x21 0x00 0x7b 0x02 0x40 0xc0    ..!.{.@.
    0018   0x08 0x15 0x0d 0x10 0x22 0x00 0x0a 0x7a    ...."..z
##### DEBUG DECIMAL
            100  124    0    0    0    0    0    0
              0    0  123    1   64  192    4   21
             13    8   33    0  123    2   64  192
              8   21   13   16   34    0   10  122
#### RECORD 0 TempBasal 2013-07-20T01:31:39 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-07-20T01:31:39)
    0000   0x67 0xdf 0x01 0x14 0x0d                   g....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 1 TempBasalDuration 2013-07-20T01:31:39 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-07-20T01:31:39)
    0000   0x67 0xdf 0x01 0x14 0x0d                   g....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 Base (2013, 7, 20, 1, 31, 40) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime ((2013, 7, 20, 1, 31, 40))
    0000   0x68 0xdf 0x01 0x14 0x0d                   h....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Base (2000, 1, 0, 1, 59, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1f                                  ..
    decimal
              0   31
    datetime ((2000, 1, 0, 1, 59, 0))
    0000   0x00 0x7b 0x01 0x40 0xc0                   .{.@.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 4 Base (2011, 0, 0, 1, 8, 13) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x14                                  ..
    decimal
              4   20
    datetime ((2011, 0, 0, 1, 8, 13))
    0000   0x0d 0x08 0x21 0x00 0x7b                   ..!.{
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 5 Base (2000, 12, 13, 20, 8, 0) head[2], body[0] op[0x02]

    op hex (2)
    0000   0x02 0x40                                  .@
    decimal
              2   64
    datetime ((2000, 12, 13, 20, 8, 0))
    0000   0xc0 0x08 0x14 0x0d 0x10                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 6 Base (2012, 4, 0, 0, 3, 59) head[2], body[0] op[0x22]

    op hex (2)
    0000   0x22 0x00                                  ".
    decimal
             34    0
    datetime ((2012, 4, 0, 0, 3, 59))
    0000   0x7b 0x03 0x40 0xc0 0x0c                   {.@..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 7 SelectBasalProfile (2001, 0, 10, 0, 29, 24) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x0d                                  ..
    decimal
             20   13
    datetime ((2001, 0, 10, 0, 29, 24))
    0000   0x18 0x1d 0x00 0x0a 0x71                   ....q
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 8 Base (2001, 0, 27, 13, 20, 46) head[2], body[0] op[0x56]

    op hex (2)
    0000   0x56 0xc5                                  V.
    decimal
             86  197
    datetime ((2001, 0, 27, 13, 20, 46))
    0000   0x2e 0x14 0x0d 0x5b 0x71                   ...[q
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[197], body[0] op[0x5c]
###### DECODED
```python
[{'age': 116, 'amount': 0.35, 'curve': 13},
 {'age': 80, 'amount': 0.525, 'curve': 0},
 {'age': 60, 'amount': 3.0, 'curve': 100},
 {'age': 0, 'amount': 0.0, 'curve': 68},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 68, 'amount': 0.0, 'curve': 120},
 {'age': 0, 'amount': 0.025, 'curve': 68},
 {'age': 68, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 92},
 {'age': 78, 'amount': 4.925, 'curve': 116},
 {'age': 10, 'amount': 0.325, 'curve': 109},
 {'age': 223, 'amount': 1.8, 'curve': 47},
 {'age': 13, 'amount': 0.5, 'curve': 91},
 {'age': 77, 'amount': 2.725, 'curve': 223},
 {'age': 116, 'amount': 0.375, 'curve': 13},
 {'age': 80, 'amount': 0.0, 'curve': 0},
 {'age': 60, 'amount': 3.0, 'curve': 100},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 36},
 {'age': 0, 'amount': 0.0, 'curve': 120},
 {'age': 5, 'amount': 2.3, 'curve': 68},
 {'age': 192, 'amount': 2.2, 'curve': 91},
 {'age': 90, 'amount': 2.725, 'curve': 223},
 {'age': 20, 'amount': 0.375, 'curve': 13},
 {'age': 80, 'amount': 0.55, 'curve': 0},
 {'age': 60, 'amount': 3.0, 'curve': 100},
 {'age': 0, 'amount': 0.0, 'curve': 72},
 {'age': 0, 'amount': 0.0, 'curve': 36},
 {'age': 72, 'amount': 0.0, 'curve': 120},
 {'age': 5, 'amount': 2.3, 'curve': 68},
 {'age': 192, 'amount': 2.2, 'curve': 1},
 {'age': 72, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 1.8, 'curve': 36},
 {'age': 90, 'amount': 0.0, 'curve': 223},
 {'age': 20, 'amount': 1.975, 'curve': 13},
 {'age': 124, 'amount': 0.25, 'curve': 66},
 {'age': 49, 'amount': 6.05, 'curve': 20},
 {'age': 91, 'amount': 0.325, 'curve': 124},
 {'age': 242, 'amount': 1.775, 'curve': 17},
 {'age': 13, 'amount': 2.9, 'curve': 18},
 {'age': 0, 'amount': 2.0, 'curve': 100},
 {'age': 100, 'amount': 1.5, 'curve': 0},
 {'age': 72, 'amount': 0.0, 'curve': 0},
 {'age': 12, 'amount': 0.0, 'curve': 0},
 {'age': 120, 'amount': 1.8, 'curve': 92},
 {'age': 72, 'amount': 0.2, 'curve': 147},
 {'age': 68, 'amount': 4.8, 'curve': 227},
 {'age': 1, 'amount': 4.8, 'curve': 0},
 {'age': 0, 'amount': 1.8, 'curve': 72},
 {'age': 12, 'amount': 0.0, 'curve': 0},
 {'age': 242, 'amount': 1.775, 'curve': 81},
 {'age': 13, 'amount': 2.9, 'curve': 10},
 {'age': 115, 'amount': 3.025, 'curve': 233},
 {'age': 20, 'amount': 1.275, 'curve': 13},
 {'age': 121, 'amount': 2.275, 'curve': 123},
 {'age': 19, 'amount': 5.825, 'curve': 116},
 {'age': 28, 'amount': 0.325, 'curve': 80},
 {'age': 100, 'amount': 0.0, 'curve': 60},
 {'age': 0, 'amount': 2.5, 'curve': 0},
 {'age': 0, 'amount': 2.8, 'curve': 0},
 {'age': 0, 'amount': 0.5, 'curve': 112},
 {'age': 92, 'amount': 3.0, 'curve': 11},
 {'age': 118, 'amount': 1.8, 'curve': 192},
 {'age': 2, 'amount': 1.8, 'curve': 208},
 {'age': 82, 'amount': 1.7, 'curve': 208}]
```
    op hex (197)
    0000   0x5c 0xc5 0x0e 0x74 0x0d 0x15 0x50 0x00    \..t..P.
    0008   0x78 0x3c 0x64 0x00 0x00 0x44 0x00 0x00    x<d..D..
    0010   0x00 0x00 0x44 0x78 0x01 0x00 0x44 0x00    ..Dx..D.
    0018   0x44 0x00 0x00 0x00 0x5c 0xc5 0x4e 0x74    D...\.Nt
    0020   0x0d 0x0a 0x6d 0x48 0xdf 0x2f 0x14 0x0d    ..mH./..
    0028   0x5b 0x6d 0x4d 0xdf 0x0f 0x74 0x0d 0x00    [mM..t..
    0030   0x50 0x00 0x78 0x3c 0x64 0x00 0x00 0x00    P.x<d...
    0038   0x00 0x00 0x24 0x00 0x00 0x78 0x5c 0x05    ..$..x\.
    0040   0x44 0x58 0xc0 0x5b 0x6d 0x5a 0xdf 0x0f    DX.[mZ..
    0048   0x14 0x0d 0x16 0x50 0x00 0x78 0x3c 0x64    ...P.x<d
    0050   0x00 0x00 0x48 0x00 0x00 0x24 0x00 0x48    ..H..$.H
    0058   0x78 0x5c 0x05 0x44 0x58 0xc0 0x01 0x00    x\.DX...
    0060   0x48 0x00 0x48 0x00 0x24 0x00 0x5a 0xdf    H.H.$.Z.
    0068   0x4f 0x14 0x0d 0x0a 0x7c 0x42 0xf2 0x31    O...|B.1
    0070   0x14 0x0d 0x5b 0x7c 0x47 0xf2 0x11 0x74    ..[|G..t
    0078   0x0d 0x12 0x50 0x00 0x64 0x3c 0x64 0x00    ..P.d<d.
    0080   0x00 0x48 0x00 0x00 0x0c 0x00 0x48 0x78    .H....Hx
    0088   0x5c 0x08 0x48 0x93 0xc0 0x44 0xe3 0xc0    \.H..D..
    0090   0x01 0x00 0x48 0x00 0x48 0x00 0x0c 0x00    ..H.H...
    0098   0x47 0xf2 0x51 0x74 0x0d 0x0a 0x79 0x73    G.Qt..ys
    00A0   0xe9 0x33 0x14 0x0d 0x5b 0x79 0x7b 0xe9    .3..[y{.
    00A8   0x13 0x74 0x0d 0x1c 0x50 0x00 0x64 0x3c    .t..P.d<
    00B0   0x64 0x00 0x00 0x70 0x00 0x00 0x14 0x00    d..p....
    00B8   0x70 0x78 0x5c 0x0b 0x48 0x76 0xc0 0x48    px\.Hv.H
    00C0   0x02 0xd0 0x44 0x52 0xd0                   ..DR.
    decimal
             92  197   14  116   13   21   80    0
            120   60  100    0    0   68    0    0
              0    0   68  120    1    0   68    0
             68    0    0    0   92  197   78  116
             13   10  109   72  223   47   20   13
             91  109   77  223   15  116   13    0
             80    0  120   60  100    0    0    0
              0    0   36    0    0  120   92    5
             68   88  192   91  109   90  223   15
             20   13   22   80    0  120   60  100
              0    0   72    0    0   36    0   72
            120   92    5   68   88  192    1    0
             72    0   72    0   36    0   90  223
             79   20   13   10  124   66  242   49
             20   13   91  124   71  242   17  116
             13   18   80    0  100   60  100    0
              0   72    0    0   12    0   72  120
             92    8   72  147  192   68  227  192
              1    0   72    0   72    0   12    0
             71  242   81  116   13   10  121  115
            233   51   20   13   91  121  123  233
             19  116   13   28   80    0  100   60
            100    0    0  112    0    0   20    0
            112  120   92   11   72  118  192   72
              2  208   68   82  208
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus (2011, 4, 0, 20, 0, 48) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x70 0x00                        ..p.
    decimal
              1    0  112    0
    datetime ((2011, 4, 0, 20, 0, 48))
    0000   0x70 0x00 0x14 0x00 0x7b                   p...{
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 11 Base (2009, 4, 4, 10, 13, 52) head[2], body[0] op[0xe9]

    op hex (2)
    0000   0xe9 0x53                                  .S
    decimal
            233   83
    datetime ((2009, 4, 4, 10, 13, 52))
    0000   0x74 0x0d 0x0a 0x64 0x69                   t..di
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 12 Base (2002, 0, 4, 27, 13, 20) head[2], body[0] op[0xdb]

    op hex (2)
    0000   0xdb 0x34                                  .4
    decimal
            219   52
    datetime ((2002, 0, 4, 27, 13, 20))
    0000   0x14 0x0d 0x5b 0x64 0x72                   ..[dr
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 13 Base (2000, 4, 16, 19, 13, 52) head[2], body[0] op[0xdb]

    op hex (2)
    0000   0xdb 0x14                                  ..
    decimal
            219   20
    datetime ((2000, 4, 16, 19, 13, 52))
    0000   0x74 0x0d 0x13 0x50 0x00                   t..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 14 ChangeTimeDisplay 2000-04-12T00:00:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-12T00:00:36)
    0000   0x64 0x00 0x00 0x4c 0x00                   d..L.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 15 Base (2001, 1, 28, 24, 12, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x60                                  .`
    decimal
              0   96
    datetime ((2001, 1, 28, 24, 12, 0))
    0000   0x00 0x4c 0x78 0x5c 0x11                   .Lx\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 16 Base (2008, 12, 0, 22, 62, 0) head[2], body[0] op[0x32]

    op hex (2)
    0000   0x32 0x2c                                  2,
    decimal
             50   44
    datetime ((2008, 12, 0, 22, 62, 0))
    0000   0xc0 0x3e 0x36 0xc0 0x48                   .>6.H
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 17 Base (2000, 4, 4, 16, 48, 8) head[2], body[0] op[0xa4]

    op hex (2)
    0000   0xa4 0xc0                                  ..
    decimal
            164  192
    datetime ((2000, 4, 4, 16, 48, 8))
    0000   0x48 0x30 0xd0 0x44 0x80                   H0.D.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 Base (2000, 1, 12, 0, 12, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 1, 12, 0, 12, 0))
    0000   0x00 0x4c 0x00 0x4c 0x00                   .L.L.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 19 Base (2013, 7, 20, 20, 27, 50) head[2], body[0] op[0x60]

    op hex (2)
    0000   0x60 0x00                                  `.
    decimal
             96    0
    datetime ((2013, 7, 20, 20, 27, 50))
    0000   0x72 0xdb 0x54 0x74 0x0d                   r.Tt.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 Base (2013, 7, 21, 0, 0, 0) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime ((2013, 7, 21, 0, 0, 0))
    0000   0x40 0xc0 0x00 0x15 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 21 Base (2004, 0, 0, 0, 7, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1f                                  ..
    decimal
              0   31
    datetime ((2004, 0, 0, 0, 7, 0))
    0000   0x00 0x07 0x00 0x00 0x04                   .....
    body (0)

#### RECORD 22 Base (2014, 8, 0, 0, 0, 13) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x74                                  rt
    decimal
            114  116
    datetime ((2014, 8, 0, 0, 0, 13))
    0000   0x8d 0x00 0x00 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 23 Base (2000, 0, 0, 17, 0, 5) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0x8d                                  t.
    decimal
            116  141
    datetime ((2000, 0, 0, 17, 0, 5))
    0000   0x05 0x00 0x71 0x00 0x00                   ..q..
    body (0)

#### RECORD 24 Base (2002, 0, 2, 18, 4, 0) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2002, 0, 2, 18, 4, 0))
    0000   0x00 0x04 0x72 0x02 0xe2                   ..r..
    body (0)
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 25 Base (2001, 8, 12, 0, 35, 16) head[2], body[0] op[0x41]

    op hex (2)
    0000   0x41 0x01                                  A.
    decimal
             65    1
    datetime ((2001, 8, 12, 0, 35, 16))
    0000   0x90 0x23 0x00 0x6c 0x01                   .#.l.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 27 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-22.data: 28 records`
