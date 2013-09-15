## START logs/ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 137, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x05 0x00 0x77 0x8d 0x00 0x00 0x00 0x6e    ..w....n
    0008   0x77 0x8d 0x05 0x00 0xcd 0x00 0x00 0x0a    w.......
    0010   0x00 0x00 0x05 0x00 0x02 0xdc 0x39 0x02    ......9.
    0018   0x24 0x2b 0x00 0x44 0x00 0xd0 0x01 0x10    $+.D....
##### DEBUG DECIMAL
              5    0  119  141    0    0    0  110
            119  141    5    0  205    0    0   10
              0    0    5    0    2  220   57    2
             36   43    0   68    0  208    1   16
#### RECORD 0 BolusWizard 2013-07-23T20:06:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-07-23T20:06:36)
    0000   0x64 0xc6 0x14 0x77 0x0d                   d..w.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x50 0x00 0x00 0x10 0x00 0x50 0x78         P....Px
    decimal
             20   80    0  100   60  100    0    0
             80    0    0   16    0   80  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 123, 'amount': 1.3, 'curve': 192},
 {'age': 143, 'amount': 0.7, 'curve': 192},
 {'age': 203, 'amount': 0.95, 'curve': 192},
 {'age': 213, 'amount': 0.35, 'curve': 192},
 {'age': 37, 'amount': 1.7, 'curve': 208},
 {'age': 137, 'amount': 1.7, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x34 0x7b 0xc0 0x1c 0x8f 0xc0    \.4{....
    0008   0x26 0xcb 0xc0 0x0e 0xd5 0xc0 0x44 0x25    &.....D%
    0010   0xd0 0x44 0x89 0xd0                        .D..
    decimal
             92   20   52  123  192   28  143  192
             38  203  192   14  213  192   68   37
            208   68  137  208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus (2004, 4, 0, 16, 0, 16) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x50 0x00                        ..P.
    decimal
              1    0   80    0
    datetime ((2004, 4, 0, 16, 0, 16))
    0000   0x50 0x00 0x10 0x00 0x64                   P...d
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 3 Base (2014, 4, 27, 10, 13, 55) head[2], body[0] op[0xc6]

    op hex (2)
    0000   0xc6 0x54                                  .T
    decimal
            198   84
    datetime ((2014, 4, 27, 10, 13, 55))
    0000   0x77 0x0d 0x0a 0xbb 0x6e                   w...n
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 Base (2005, 0, 4, 10, 13, 23) head[2], body[0] op[0xe5]

    op hex (2)
    0000   0xe5 0x34                                  .4
    decimal
            229   52
    datetime ((2005, 0, 4, 10, 13, 23))
    0000   0x17 0x0d 0x0a 0x24 0x75                   ...$u
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 5 Base (2008, 2, 4, 27, 13, 23) head[2], body[0] op[0xe9]

    op hex (2)
    0000   0xe9 0x35                                  .5
    decimal
            233   53
    datetime ((2008, 2, 4, 27, 13, 23))
    0000   0x17 0x8d 0x5b 0x24 0x78                   ..[$x
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 6 Base (2000, 0, 17, 0, 13, 23) head[2], body[0] op[0xe9]

    op hex (2)
    0000   0xe9 0x15                                  ..
    decimal
            233   21
    datetime ((2000, 0, 17, 0, 13, 23))
    0000   0x17 0x0d 0x00 0x51 0x00                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 7 ChangeTimeDisplay (2000, 5, 0, 0, 48, 36) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime ((2000, 5, 0, 0, 48, 36))
    0000   0x64 0x70 0x00 0x00 0x00                   dp...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 8 Base (2004, 1, 28, 24, 16, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x20                                  . 
    decimal
              0   32
    datetime ((2004, 1, 28, 24, 16, 0))
    0000   0x00 0x50 0x78 0x5c 0x14                   .Px\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Base (2012, 12, 0, 26, 52, 0) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x62                                  Pb
    decimal
             80   98
    datetime ((2012, 12, 0, 26, 52, 0))
    0000   0xc0 0x34 0xda 0xc0 0x1c                   .4...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 10 Base (2004, 0, 14, 16, 42, 38) head[2], body[0] op[0xee]

    op hex (2)
    0000   0xee 0xc0                                  ..
    decimal
            238  192
    datetime ((2004, 0, 14, 16, 42, 38))
    0000   0x26 0x2a 0xd0 0x0e 0x34                   &*..4
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 11 Base (2000, 11, 0, 1, 16, 4) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x44                                  .D
    decimal
            208   68
    datetime ((2000, 11, 0, 1, 16, 4))
    0000   0x84 0xd0 0x01 0x00 0x50                   ....P
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 12 Base (2009, 0, 24, 0, 32, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x50                                  .P
    decimal
              0   80
    datetime ((2009, 0, 24, 0, 32, 0))
    0000   0x00 0x20 0x00 0x78 0xe9                   . .x.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 0]
#### RECORD 13 Base (2000, 1, 0, 0, 59, 13) head[2], body[0] op[0x55]

    op hex (2)
    0000   0x55 0x17                                  U.
    decimal
             85   23
    datetime ((2000, 1, 0, 0, 59, 13))
    0000   0x0d 0x7b 0x00 0x40 0xc0                   .{.@.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 14 Base (2007, 0, 0, 29, 0, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x18                                  ..
    decimal
              0   24
    datetime ((2007, 0, 0, 29, 0, 13))
    0000   0x0d 0x00 0x1d 0x00 0x07                   .....
    body (0)

`end logs/ReadHistoryData-page-20.data: 15 records`
