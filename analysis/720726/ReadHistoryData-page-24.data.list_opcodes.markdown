## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 281, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x8e 0x17 0x4b 0x6a 0x0d 0x7b 0x03 0x80    ..Kj.{..
    0008   0x00 0x0d 0x0a 0x0d 0x1a 0x26 0x00 0x5b    .....&.[
    0010   0x00 0x9e 0x0b 0x0e 0x6a 0x0d 0x23 0x90    ....j.#.
    0018   0x00 0x6e 0x17 0x36 0x00 0x00 0x7c 0x00    .n.6..|.
##### DEBUG DECIMAL
            142   23   75  106   13  123    3  128
              0   13   10   13   26   38    0   91
              0  158   11   14  106   13   35  144
              0  110   23   54    0    0  124    0
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x89 0x0d 0x06 0x10 0x9d 0x50 0x01    n.....P.
    0008   0x08 0x00 0x00 0x06 0xcd 0x03 0x89 0x34    .......4
    0010   0x03 0x44 0x30 0x00 0xbe 0x01 0xec 0x00    .D0.....
    0018   0x70 0x00 0xe8 0x00 0x00 0x07 0x02 0x01    p.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  137   13    6   16  157   80    1
              8    0    0    6  205    3  137   52
              3   68   48    0  190    1  236    0
            112    0  232    0    0    7    2    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 BolusWizard 2013-08-10T00:48:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-10T00:48:29)
    0000   0x9d 0x30 0x00 0x6a 0x0d                   .0.j.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 2.4, 'curve': 4},
 {'age': 143, 'amount': 1.4, 'curve': 4},
 {'age': 243, 'amount': 5.8, 'curve': 4},
 {'age': 147, 'amount': 1.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x60 0x67 0x04 0x38 0x8f 0x04    \.`g.8..
    0008   0xe8 0xf3 0x04 0x2c 0x93 0x14              ...,..
    decimal
             92   14   96  103    4   56  143    4
            232  243    4   44  147   20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2013-08-10T00:48:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x4c 0x00    ..@.@.L.
    decimal
              1    0   64    0   64    0   76    0
    datetime (2013-08-10T00:48:29)
    0000   0x9d 0x30 0x40 0x6a 0x0d                   .0@j.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 CalBGForPH 2013-08-10T01:21:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-08-10T01:21:45)
    0000   0xad 0x15 0x21 0x6a 0x0d                   ..!j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 5 Base (2013, 8, 10, 1, 21, 45) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime ((2013, 8, 10, 1, 21, 45))
    0000   0xad 0x15 0x01 0x6a 0x0d                   ...j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 Ian69 2006-09-09T11:27:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2006-09-09T11:27:22)
    0000   0x96 0x5b 0x4b 0x89 0x16                   .[K..
    body (8)
    hex
    0000   0x01 0x6a 0x0d 0x14 0x90 0x00 0x6e 0x17    .j....n.
    decimal
              1  106   13   20  144    0  110   23
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 7 Base (2008, 1, 0, 0, 8, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x24                                  6$
    decimal
             54   36
    datetime ((2008, 1, 0, 0, 8, 0))
    0000   0x00 0x48 0x00 0x00 0x68                   .H..h
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 8 Base (2005, 1, 0, 17, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x48                                  .H
    decimal
              0   72
    datetime ((2005, 1, 0, 17, 28, 54))
    0000   0x36 0x5c 0x11 0x40 0x25                   6\.@%
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 9 Base (2004, 8, 17, 24, 4, 9) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x60                                  .`
    decimal
              4   96
    datetime ((2004, 8, 17, 24, 4, 9))
    0000   0x89 0x04 0x38 0xb1 0x04                   ..8..
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 10 Base (2001, 0, 20, 21, 44, 20) head[2], body[0] op[0xe8]

    op hex (2)
    0000   0xe8 0x15                                  ..
    decimal
            232   21
    datetime ((2001, 0, 20, 21, 44, 20))
    0000   0x14 0x2c 0xb5 0x14 0x01                   .,...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 Base (2000, 0, 8, 0, 48, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x30                                  .0
    decimal
              0   48
    datetime ((2000, 0, 8, 0, 48, 0))
    0000   0x00 0x30 0x00 0x68 0x00                   .0.h.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Base (2001, 5, 27, 13, 42, 1) head[2], body[0] op[0x89]

    op hex (2)
    0000   0x89 0x16                                  ..
    decimal
            137   22
    datetime ((2001, 5, 27, 13, 42, 1))
    0000   0x41 0x6a 0x0d 0x7b 0x01                   Aj.{.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 Base (2014, 0, 8, 13, 10, 4) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x00                                  ..
    decimal
            128    0
    datetime ((2014, 0, 8, 13, 10, 4))
    0000   0x04 0x0a 0x0d 0x08 0x2e                   .....
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 14 Base (2010, 2, 9, 30, 0, 2) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2010, 2, 9, 30, 0, 2))
    0000   0x02 0x80 0x1e 0x09 0x0a                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 15 Base (2000, 0, 8, 9, 0, 30) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x13                                  ..
    decimal
             13   19
    datetime ((2000, 0, 8, 9, 0, 30))
    0000   0x1e 0x00 0x69 0x08 0x80                   ..i..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 PumpSuspend (2010, 0, 30, 10, 13, 10) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x0a                                  ..
    decimal
             30   10
    datetime ((2010, 0, 30, 10, 13, 10))
    0000   0x0a 0x0d 0x2a 0x1e 0x0a                   ..*..
    body (0)

#### RECORD 17 Base (2015, 0, 13, 10, 42, 45) head[2], body[0] op[0x3b]

    op hex (2)
    0000   0x3b 0x9f                                  ;.
    decimal
             59  159
    datetime ((2015, 0, 13, 10, 42, 45))
    0000   0x2d 0x2a 0x6a 0x0d 0x3f                   -*j.?
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 18 ResultTotals 2006-01-22T09:41:13 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x9f 0x2d 0x6a 0x6a                   ..-jj
    decimal
              7  159   45  106  106
    datetime (2006-01-22T09:41:13)
    0000   0x0d 0x69 0x69 0x96 0x06                   .ii..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 19 NoDelivery 2012-01-13T10:11:22 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x08 0xb6 0x80                        ....
    decimal
              6    8  182  128
    datetime (2012-01-13T10:11:22)
    0000   0x16 0x4b 0xaa 0x0d 0x0c                   .K...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 20 NoDelivery (2003, 0, 2, 27, 13, 10) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x83 0x17 0x0b                        ....
    decimal
              6  131   23   11
    datetime ((2003, 0, 2, 27, 13, 10))
    0000   0x0a 0x0d 0x7b 0x02 0x83                   ..{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 ChangeTime (2000, 0, 30, 19, 13, 10) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x0b                                  ..
    decimal
             23   11
    datetime ((2000, 0, 30, 19, 13, 10))
    0000   0x0a 0x0d 0x13 0x1e 0x00                   .....
    body (0)

#### RECORD 22 BolusWizard 2013-08-10T11:23:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-10T11:23:14)
    0000   0x8e 0x17 0x0b 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 23 Ian69 2013-08-10T11:23:14 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-10T11:23:14)
    0000   0x8e 0x17 0x0b 0x0a 0x0d                   .....
    body (8)
    hex
    0000   0x0e 0x1e 0x01 0x00 0x78 0x00 0x78 0x00    ....x.x.
    decimal
             14   30    1    0  120    0  120    0

`end logs/ReadHistoryData-page-24.data: 24 records`
