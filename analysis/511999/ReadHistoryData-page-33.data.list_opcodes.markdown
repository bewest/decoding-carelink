## START logs/ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 247, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6c 0x64 0x00 0x00 0x00 0x00 0x00 0x00    ld......
    0008   0x00 0x00 0x0a 0xc4 0x52 0xd1 0x23 0x06    ....R.#.
    0010   0x0d 0x5b 0xc4 0x56 0xd1 0x03 0x66 0x0d    .[.V..f.
    0018   0x00 0x50 0x00 0x78 0x3c 0x6e 0x2c 0x00    .P.x<n,.
##### DEBUG DECIMAL
            108  100    0    0    0    0    0    0
              0    0   10  196   82  209   35    6
             13   91  196   86  209    3  102   13
              0   80    0  120   60  110   44    0
#### RECORD 0 BolusWizard 2013-07-05T18:51:54 head[2], body[15] op[0x5b]
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
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x78 0x00 0x00 0x3c 0x00 0x78 0x78         x..<.xx
    decimal
             30   80    0  100   60  100   48    0
            120    0    0   60    0  120  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 1.1, 'curve': 192},
 {'age': 97, 'amount': 1.6, 'curve': 192},
 {'age': 107, 'amount': 0.4, 'curve': 192},
 {'age': 217, 'amount': 1.2, 'curve': 192},
 {'age': 237, 'amount': 0.7, 'curve': 192},
 {'age': 21, 'amount': 0.5, 'curve': 208},
 {'age': 41, 'amount': 3.5, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x2c 0x43 0xc0 0x40 0x61 0xc0    \.,C.@a.
    0008   0x10 0x6b 0xc0 0x30 0xd9 0xc0 0x1c 0xed    .k.0....
    0010   0xc0 0x14 0x15 0xd0 0x8c 0x29 0xd0         .....).
    decimal
             92   23   44   67  192   64   97  192
             16  107  192   48  217  192   28  237
            192   20   21  208  140   41  208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus (2006, 4, 0, 28, 0, 56) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x78 0x00                        ..x.
    decimal
              1    0  120    0
    datetime ((2006, 4, 0, 28, 0, 56))
    0000   0x78 0x00 0x3c 0x00 0x76                   x.<.v
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 3 Base (2009, 4, 12, 10, 13, 37) head[2], body[0] op[0xf3]

    op hex (2)
    0000   0xf3 0x52                                  .R
    decimal
            243   82
    datetime ((2009, 4, 12, 10, 13, 37))
    0000   0x65 0x0d 0x0a 0x6c 0x59                   e..lY
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 4 Base (2006, 0, 12, 27, 13, 5) head[2], body[0] op[0xc7]

    op hex (2)
    0000   0xc7 0x33                                  .3
    decimal
            199   51
    datetime ((2006, 0, 12, 27, 13, 5))
    0000   0x05 0x0d 0x5b 0x6c 0x66                   ..[lf
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 5 Base (2000, 4, 16, 16, 13, 37) head[2], body[0] op[0xc7]

    op hex (2)
    0000   0xc7 0x13                                  ..
    decimal
            199   19
    datetime ((2000, 4, 16, 16, 13, 37))
    0000   0x65 0x0d 0x10 0x50 0x00                   e..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 6 ChangeTimeDisplay (2000, 4, 0, 0, 0, 36) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime ((2000, 4, 0, 0, 0, 36))
    0000   0x64 0x00 0x00 0x40 0x00                   d..@.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2010, 1, 28, 24, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xa0                                  ..
    decimal
              0  160
    datetime ((2010, 1, 28, 24, 0, 0))
    0000   0x00 0x40 0x78 0x5c 0x1a                   .@x\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 8 Base (2000, 12, 0, 19, 44, 0) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x17                                  x.
    decimal
            120   23
    datetime ((2000, 12, 0, 19, 44, 0))
    0000   0xc0 0x2c 0x53 0xc0 0x40                   .,S.@
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 9 Base (2009, 1, 16, 0, 59, 16) head[2], body[0] op[0x71]

    op hex (2)
    0000   0x71 0xc0                                  q.
    decimal
            113  192
    datetime ((2009, 1, 16, 0, 59, 16))
    0000   0x10 0x7b 0xc0 0x30 0xe9                   .{.0.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 1, 0]
#### RECORD 10 Base (2000, 15, 5, 20, 0, 61) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x1c                                  ..
    decimal
            192   28
    datetime ((2000, 15, 5, 20, 0, 61))
    0000   0xfd 0xc0 0x14 0x25 0xd0                   ...%.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 11 Base (2000, 12, 8, 0, 1, 16) head[2], body[0] op[0x8c]

    op hex (2)
    0000   0x8c 0x39                                  .9
    decimal
            140   57
    datetime ((2000, 12, 8, 0, 1, 16))
    0000   0xd0 0x01 0x00 0x28 0x00                   ...(.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 12 Base (2003, 8, 7, 6, 0, 32) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x00                                  (.
    decimal
             40    0
    datetime ((2003, 8, 7, 6, 0, 32))
    0000   0xa0 0x00 0x66 0xc7 0x53                   ..f.S
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 13 Base (2007, 3, 20, 6, 4, 10) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x0d                                  e.
    decimal
            101   13
    datetime ((2007, 3, 20, 6, 4, 10))
    0000   0x0a 0xc4 0x66 0xd4 0x37                   ..f.7
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 14 Base (2007, 7, 20, 9, 4, 27) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x0d                                  ..
    decimal
              5   13
    datetime ((2007, 7, 20, 9, 4, 27))
    0000   0x5b 0xc4 0x69 0xd4 0x17                   [.i..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 15 Base (2012, 1, 4, 0, 16, 0) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x0d                                  ..
    decimal
              5   13
    datetime ((2012, 1, 4, 0, 16, 0))
    0000   0x00 0x50 0x00 0x64 0x3c                   .P.d<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 16 ChangeTimeDisplay (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x30                                  d0
    decimal
            100   48
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 17 Base (2000, 5, 8, 17, 28, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x30                                  .0
    decimal
              0   48
    datetime ((2000, 5, 8, 17, 28, 56))
    0000   0x78 0x5c 0x11 0x28 0x00                   x\.(.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
#### RECORD 18 Base (2000, 3, 16, 12, 16, 20) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x78                                  .x
    decimal
            208  120
    datetime ((2000, 3, 16, 12, 16, 20))
    0000   0x14 0xd0 0x2c 0x50 0xd0                   ..,P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 19 Base (2001, 12, 16, 24, 16, 16) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x6e                                  @n
    decimal
             64  110
    datetime ((2001, 12, 16, 24, 16, 16))
    0000   0xd0 0x10 0x78 0xd0 0x01                   ..x..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 20 Base (2000, 0, 0, 0, 48, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x30                                  .0
    decimal
              0   48
    datetime ((2000, 0, 0, 0, 48, 0))
    0000   0x00 0x30 0x00 0x00 0x00                   .0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 21 Base (2000, 4, 27, 13, 5, 23) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd4                                  i.
    decimal
            105  212
    datetime ((2000, 4, 27, 13, 5, 23))
    0000   0x57 0x05 0x0d 0x7b 0x00                   W..{.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 22 Base (2012, 0, 0, 13, 6, 0) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0xc0                                  @.
    decimal
             64  192
    datetime ((2012, 0, 0, 13, 6, 0))
    0000   0x00 0x06 0x0d 0x00 0x1c                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 23 Base (2005, 0, 28, 5, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x07                                  ..
    decimal
              0    7
    datetime ((2005, 0, 28, 5, 0, 0))
    0000   0x00 0x00 0x05 0x1c 0x65                   ....e
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 24 Base (2013, 0, 5, 14, 0, 0) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x00                                  ..
    decimal
            141    0
    datetime ((2013, 0, 5, 14, 0, 0))
    0000   0x00 0x00 0x6e 0x65 0x8d                   ..ne.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 Base (2000, 12, 9, 0, 0, 58) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 12, 9, 0, 0, 58))
    0000   0xfa 0x00 0x00 0x09 0x00                   .....
    body (0)

#### RECORD 26 Base (2002, 0, 25, 4, 2, 28) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2002, 0, 25, 4, 2, 28))
    0000   0x1c 0x02 0xe4 0x39 0x02                   ...9.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 27 Base (2000, 1, 20, 0, 9, 0) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x2b                                  8+
    decimal
             56   43
    datetime ((2000, 1, 20, 0, 9, 0))
    0000   0x00 0x49 0x00 0xb4 0x00                   .I...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 28 Base (2005, 8, 3, 0, 0, 12) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0x00                                  ..
    decimal
            248    0
    datetime ((2005, 8, 3, 0, 0, 12))
    0000   0x8c 0x00 0x00 0x03 0x05                   .....
    body (0)

#### RECORD 29 Bolus (2000, 0, 0, 0, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x04 0x00                        ....
    decimal
              1    0    4    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-33.data: 30 records`
