## START logs/ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 255, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0a 0xc4 0x52 0xd1 0x23 0x06 0x0d 0x5b    ..R.#..[
    0008   0xc4 0x56 0xd1 0x03 0x66 0x0d 0x00 0x50    .V..f..P
    0010   0x00 0x78 0x3c 0x6e 0x2c 0x00 0x00 0x00    .x<n,...
    0018   0x00 0x00 0x00 0x2c 0x82 0x5c 0x05 0x30    ...,.\.0
##### DEBUG DECIMAL
             10  196   82  209   35    6   13   91
            196   86  209    3  102   13    0   80
              0  120   60  110   44    0    0    0
              0    0    0   44  130   92    5   48
#### RECORD 0 BolusWizard 2013-07-05T18:51:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-05T18:51:54)
    0000   0x76 0xf3 0x12 0x65 0x0d                   v..e.
    body (13)
    hex
    0000   0x1e 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x78 0x00 0x00 0x3c 0x00                   x..<.
    decimal
             30   80    0  100   60  100   48    0
            120    0    0   60    0
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2000, 4, 3, 12, 23, 28) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x78                                  xx
    decimal
            120  120
    datetime ((2000, 4, 3, 12, 23, 28))
    0000   0x5c 0x17 0x2c 0x43 0xc0                   \.,C.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 2 Base (2000, 12, 0, 11, 16, 0) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x61                                  @a
    decimal
             64   97
    datetime ((2000, 12, 0, 11, 16, 0))
    0000   0xc0 0x10 0x6b 0xc0 0x30                   ..k.0
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 3 Base (2005, 3, 20, 0, 45, 28) head[2], body[0] op[0xd9]

    op hex (2)
    0000   0xd9 0xc0                                  ..
    decimal
            217  192
    datetime ((2005, 3, 20, 0, 45, 28))
    0000   0x1c 0xed 0xc0 0x14 0x15                   .....
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 4 Base (2008, 3, 0, 1, 16, 41) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x8c                                  ..
    decimal
            208  140
    datetime ((2008, 3, 0, 1, 16, 41))
    0000   0x29 0xd0 0x01 0x00 0x78                   )...x
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 5 Base (2003, 0, 22, 0, 60, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2003, 0, 22, 0, 60, 0))
    0000   0x00 0x3c 0x00 0x76 0xf3                   .<.v.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 6 Base (2007, 0, 25, 12, 10, 13) head[2], body[0] op[0x52]

    op hex (2)
    0000   0x52 0x65                                  Re
    decimal
             82  101
    datetime ((2007, 0, 25, 12, 10, 13))
    0000   0x0d 0x0a 0x6c 0x59 0xc7                   ..lY.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 7 TempBasal 2007-01-06T12:27:13 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.125}
```
    op hex (2)
    0000   0x33 0x05                                  3.
    decimal
             51    5
    datetime (2007-01-06T12:27:13)
    0000   0x0d 0x5b 0x6c 0x66 0xc7                   .[lf.
    body (1)
    hex
    0000   0x13                                       .
    decimal
             19
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 8 Base (2012, 1, 4, 0, 16, 16) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x0d                                  e.
    decimal
            101   13
    datetime ((2012, 1, 4, 0, 16, 16))
    0000   0x10 0x50 0x00 0x64 0x3c                   .P.d<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 9 ChangeTimeDisplay (2000, 1, 0, 0, 0, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime ((2000, 1, 0, 0, 0, 0))
    0000   0x00 0x40 0x00 0x00 0xa0                   .@...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 10 Base (2007, 5, 24, 26, 28, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x40                                  .@
    decimal
              0   64
    datetime ((2007, 5, 24, 26, 28, 56))
    0000   0x78 0x5c 0x1a 0x78 0x17                   x\.x.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 11 Base (2000, 7, 17, 0, 0, 19) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x2c                                  .,
    decimal
            192   44
    datetime ((2000, 7, 17, 0, 0, 19))
    0000   0x53 0xc0 0x40 0x71 0xc0                   S.@q.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 12 Base (2012, 12, 0, 9, 48, 0) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x7b                                  .{
    decimal
             16  123
    datetime ((2012, 12, 0, 9, 48, 0))
    0000   0xc0 0x30 0xe9 0xc0 0x1c                   .0...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 13 Base (2009, 0, 12, 16, 37, 20) head[2], body[0] op[0xfd]

    op hex (2)
    0000   0xfd 0xc0                                  ..
    decimal
            253  192
    datetime ((2009, 0, 12, 16, 37, 20))
    0000   0x14 0x25 0xd0 0x8c 0x39                   .%..9
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 14 Base (2000, 0, 8, 0, 40, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 0, 8, 0, 40, 0))
    0000   0x00 0x28 0x00 0x28 0x00                   .(.(.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1]
#### RECORD 15 Base (2013, 7, 5, 19, 7, 38) head[2], body[0] op[0xa0]

    op hex (2)
    0000   0xa0 0x00                                  ..
    decimal
            160    0
    datetime ((2013, 7, 5, 19, 7, 38))
    0000   0x66 0xc7 0x53 0x65 0x0d                   f.Se.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 CalBGForPH 2013-07-05T23:20:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-07-05T23:20:38)
    0000   0x66 0xd4 0x37 0x05 0x0d                   f.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 BolusWizard 2013-07-05T23:20:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-05T23:20:41)
    0000   0x69 0xd4 0x17 0x05 0x0d                   i....
    body (13)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x00 0x00 0x00 0x00 0x00                   .....
    decimal
              0   80    0  100   60  100   48    0
              0    0    0    0    0
    HOUR BITS: [1, 1, 0]
#### RECORD 18 Base (2000, 4, 0, 8, 17, 28) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x78                                  0x
    decimal
             48  120
    datetime ((2000, 4, 0, 8, 17, 28))
    0000   0x5c 0x11 0x28 0x00 0xd0                   \.(..
    body (0)
    YEAR BITS: [1, 1, 0, 1]
#### RECORD 19 Base (2000, 12, 16, 16, 44, 16) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x14                                  x.
    decimal
            120   20
    datetime ((2000, 12, 16, 16, 44, 16))
    0000   0xd0 0x2c 0x50 0xd0 0x40                   .,P.@
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 20 Base (2000, 1, 1, 16, 56, 16) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0xd0                                  n.
    decimal
            110  208
    datetime ((2000, 1, 1, 16, 56, 16))
    0000   0x10 0x78 0xd0 0x01 0x00                   .x...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 21 Base (2009, 0, 0, 0, 0, 48) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x00                                  0.
    decimal
             48    0
    datetime ((2009, 0, 0, 0, 0, 48))
    0000   0x30 0x00 0x00 0x00 0x69                   0...i
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 22 Base (2000, 0, 0, 27, 13, 5) head[2], body[0] op[0xd4]

    op hex (2)
    0000   0xd4 0x57                                  .W
    decimal
            212   87
    datetime ((2000, 0, 0, 27, 13, 5))
    0000   0x05 0x0d 0x7b 0x00 0x40                   ..{.@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 23 Base (2000, 0, 28, 0, 13, 6) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x00                                  ..
    decimal
            192    0
    datetime ((2000, 0, 28, 0, 13, 6))
    0000   0x06 0x0d 0x00 0x1c 0x00                   .....
    body (0)

#### RECORD 24 ResultTotals (2000, 6, 0, 0, 13, 37) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x1c                   .....
    decimal
              7    0    0    5   28
    datetime ((2000, 6, 0, 0, 13, 37))
    0000   0x65 0x8d 0x00 0x00 0x00                   e....
    body (41)
    hex
    0000   0x6e 0x65 0x8d 0x05 0x00 0xfa 0x00 0x00    ne......
    0008   0x09 0x00 0x00 0x05 0x1c 0x02 0xe4 0x39    .......9
    0010   0x02 0x38 0x2b 0x00 0x49 0x00 0xb4 0x00    .8+.I...
    0018   0xf8 0x00 0x8c 0x00 0x00 0x03 0x05 0x01    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00                                       .
    decimal
            110  101  141    5    0  250    0    0
              9    0    0    5   28    2  228   57
              2   56   43    0   73    0  180    0
            248    0  140    0    0    3    5    1
              0    4    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 25 Base (2000, 4, 0, 0, 0, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6c                                  .l
    decimal
              0  108
    datetime ((2000, 4, 0, 0, 0, 36))
    0000   0x64 0x00 0x00 0x00 0x00                   d....
    body (0)

`end logs/ReadHistoryData-page-33.data: 26 records`
