## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 246, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x64 0xf0 0x00 0x00 0x00 0x00 0x00 0x00    d.......
    0008   0x00 0x00 0x34 0x64 0xa9 0x14 0x01 0x0a    ..4d....
    0010   0x0d 0x7b 0x01 0x80 0x00 0x04 0x0a 0x0d    .{......
    0018   0x08 0x21 0x00 0x7b 0x02 0x80 0x00 0x08    .!.{....
##### DEBUG DECIMAL
            100  240    0    0    0    0    0    0
              0    0   52  100  169   20    1   10
             13  123    1  128    0    4   10   13
              8   33    0  123    2  128    0    8
#### RECORD 0 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 1.8, 'curve': 192},
 {'age': 240, 'amount': 0.3, 'curve': 192},
 {'age': 14, 'amount': 1.6, 'curve': 208},
 {'age': 144, 'amount': 1.7, 'curve': 208},
 {'age': 184, 'amount': 1.4, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x96 0xc0 0x0c 0xf0 0xc0    \.H.....
    0008   0x40 0x0e 0xd0 0x44 0x90 0xd0 0x38 0xb8    @..D..8.
    0010   0xd0                                       .
    decimal
             92   17   72  150  192   12  240  192
             64   14  208   68  144  208   56  184
            208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2011, 0, 0, 12, 0, 56) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x38 0x00                        ..8.
    decimal
              1    0   56    0
    datetime ((2011, 0, 0, 12, 0, 56))
    0000   0x38 0x00 0x0c 0x00 0xab                   8....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 2 ChangeTime (2004, 0, 24, 10, 13, 9) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x55                                  .U
    decimal
             23   85
    datetime ((2004, 0, 24, 10, 13, 9))
    0000   0x09 0x0d 0x0a 0x78 0x84                   ...x.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 Base (2005, 0, 24, 27, 13, 9) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x36                                  06
    decimal
             48   54
    datetime ((2005, 0, 24, 27, 13, 9))
    0000   0x09 0x0d 0x5b 0x78 0x95                   ..[x.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 4 Base (2000, 4, 16, 12, 13, 41) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x16                                  0.
    decimal
             48   22
    datetime ((2000, 4, 16, 12, 13, 41))
    0000   0x69 0x0d 0x0c 0x50 0x00                   i..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 5 ChangeTimeDisplay 2000-04-16T00:00:36 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime (2000-04-16T00:00:36)
    0000   0x64 0x00 0x00 0x30 0x00                   d..0.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 6 Base (2014, 0, 28, 24, 48, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2014, 0, 28, 24, 48, 0))
    0000   0x00 0x30 0x78 0x5c 0x0e                   .0x\.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 7 Base (2012, 13, 0, 11, 8, 0) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x55                                  8U
    decimal
             56   85
    datetime ((2012, 13, 0, 11, 8, 0))
    0000   0xc0 0x48 0xeb 0xc0 0x0c                   .H...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 0]
#### RECORD 8 Base (2000, 5, 1, 16, 35, 0) head[2], body[0] op[0x45]

    op hex (2)
    0000   0x45 0xd0                                  E.
    decimal
             69  208
    datetime ((2000, 5, 1, 16, 35, 0))
    0000   0x40 0x63 0xd0 0x01 0x00                   @c...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 9 Base (2006, 0, 0, 28, 0, 48) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x00                                  0.
    decimal
             48    0
    datetime ((2006, 0, 0, 28, 0, 48))
    0000   0x30 0x00 0x1c 0x00 0x96                   0....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 10 Base (2002, 4, 24, 27, 13, 41) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x56                                  0V
    decimal
             48   86
    datetime ((2002, 4, 24, 27, 13, 41))
    0000   0x69 0x0d 0x5b 0x78 0x92                   i.[x.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 11 Base (2000, 0, 16, 0, 13, 9) head[2], body[0] op[0x35]

    op hex (2)
    0000   0x35 0x16                                  5.
    decimal
             53   22
    datetime ((2000, 0, 16, 0, 13, 9))
    0000   0x09 0x0d 0x00 0x50 0x00                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 ChangeTimeDisplay (2000, 4, 0, 0, 0, 36) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime ((2000, 4, 0, 0, 0, 36))
    0000   0x64 0x00 0x00 0x00 0x00                   d....
    body (0)

#### RECORD 13 Base (2001, 0, 28, 24, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x4c                                  .L
    decimal
              0   76
    datetime ((2001, 0, 28, 24, 0, 0))
    0000   0x00 0x00 0x78 0x5c 0x11                   ..x\.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 14 Base (2008, 12, 0, 26, 56, 0) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x0a                                  0.
    decimal
             48   10
    datetime ((2008, 12, 0, 26, 56, 0))
    0000   0xc0 0x38 0x5a 0xc0 0x48                   .8Z.H
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 15 Base (2008, 1, 0, 16, 10, 12) head[2], body[0] op[0xf0]

    op hex (2)
    0000   0xf0 0xc0                                  ..
    decimal
            240  192
    datetime ((2008, 1, 0, 16, 10, 12))
    0000   0x0c 0x4a 0xd0 0x40 0x68                   .J.@h
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 16 Base (2000, 1, 8, 0, 8, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x01                                  ..
    decimal
            208    1
    datetime ((2000, 1, 8, 0, 8, 0))
    0000   0x00 0x48 0x00 0x48 0x00                   .H.H.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 17 Base (2013, 8, 9, 22, 53, 18) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0x00                                  L.
    decimal
             76    0
    datetime ((2013, 8, 9, 22, 53, 18))
    0000   0x92 0x35 0x56 0x09 0x0d                   .5V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 CalBGForPH 2013-08-09T23:14:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 240}
```
    op hex (2)
    0000   0x0a 0xf0                                  ..
    decimal
             10  240
    datetime (2013-08-09T23:14:41)
    0000   0xa9 0x0e 0x37 0x09 0x0d                   ..7..
    body (0)

#### RECORD 19 BolusWizard 2013-08-09T23:14:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 240,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 13.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf0                                  [.
    decimal
             91  240
    datetime (2013-08-09T23:14:48)
    0000   0xb0 0x0e 0x17 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x50 0x00    .P.d<dP.
    0008   0x00 0x00 0x00 0x84 0x00                   .....
    decimal
              0   80    0  100   60  100   80    0
              0    0    0  132    0

#### RECORD 20 Base (2000, 4, 21, 8, 20, 28) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2000, 4, 21, 8, 20, 28))
    0000   0x5c 0x14 0x48 0x15 0xc0                   \.H..
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 21 Base (2008, 12, 0, 15, 56, 0) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x1f                                  0.
    decimal
             48   31
    datetime ((2008, 12, 0, 15, 56, 0))
    0000   0xc0 0x38 0x6f 0xc0 0x48                   .8o.H
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 22 Base (2013, 1, 0, 16, 31, 12) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0xd0                                  ..
    decimal
              5  208
    datetime ((2013, 1, 0, 16, 31, 12))
    0000   0x0c 0x5f 0xd0 0x40 0x7d                   ._.@}
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 23 Base (2010, 2, 0, 0, 0, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x7b                                  .{
    decimal
            208  123
    datetime ((2010, 2, 0, 0, 0, 0))
    0000   0x00 0x80 0x00 0x00 0x0a                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 Base (2000, 0, 0, 7, 0, 29) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2000, 0, 0, 7, 0, 29))
    0000   0x1d 0x00 0x07 0x00 0x00                   .....
    body (0)

#### RECORD 25 Base (2000, 8, 0, 0, 13, 9) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x08                                  ..
    decimal
              5    8
    datetime ((2000, 8, 0, 0, 13, 9))
    0000   0x89 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 26 Base (2000, 0, 7, 0, 5, 13) head[2], body[0] op[0x6e]

    op hex (2)
    0000   0x6e 0x89                                  n.
    decimal
            110  137
    datetime ((2000, 0, 7, 0, 5, 13))
    0000   0x0d 0x05 0x00 0x87 0x00                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 27 Base (2002, 0, 8, 5, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2002, 0, 8, 5, 0, 0))
    0000   0x00 0x00 0x05 0x08 0x02                   .....
    body (0)

#### RECORD 28 Base (2003, 0, 0, 11, 44, 2) head[2], body[0] op[0xdc]

    op hex (2)
    0000   0xdc 0x39                                  .9
    decimal
            220   57
    datetime ((2003, 0, 0, 11, 44, 2))
    0000   0x02 0x2c 0x2b 0x00 0x83                   .,+..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 Bolus (2008, 0, 0, 0, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 21.6, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0xd8 0x00 0x54                        ...T
    decimal
              1  216    0   84
    datetime ((2008, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x08                   .....
    body (0)

#### RECORD 30 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x02]

    op hex (2)
    0000   0x02 0x00                                  ..
    decimal
              2    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-11.data: 31 records`
