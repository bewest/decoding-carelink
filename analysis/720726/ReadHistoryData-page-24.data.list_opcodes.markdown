## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 492, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x68 0x00 0x00 0x00 0x00 0x68 0x36 0x5c    h....h6\
    0008   0x0b 0xa8 0x71 0x04 0x68 0x4d 0x14 0x7c    ..q.hM.|
    0010   0x75 0x14 0x01 0x00 0x68 0x00 0x68 0x00    u...h.h.
    0018   0x58 0x00 0xa8 0x12 0x54 0x6a 0x0d 0x0a    X...Tj..
##### DEBUG DECIMAL
            104    0    0    0    0  104   54   92
             11  168  113    4  104   77   20  124
            117   20    1    0  104    0  104    0
             88    0  168   18   84  106   13   10
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
#### RECORD 6 Base (2006, 9, 9, 11, 27, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2006, 9, 9, 11, 27, 22))
    0000   0x96 0x5b 0x4b 0x89 0x16                   .[K..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 7 Bolus (2000, 0, 8, 0, 36, 54) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 10.6, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x6a 0x0d 0x14 0x90 0x00 0x6e 0x17    .j....n.
    decimal
              1  106   13   20  144    0  110   23
    datetime ((2000, 0, 8, 0, 36, 54))
    0000   0x36 0x24 0x00 0x48 0x00                   6$.H.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 8 Base (2001, 1, 28, 22, 8, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x68                                  .h
    decimal
              0  104
    datetime ((2001, 1, 28, 22, 8, 0))
    0000   0x00 0x48 0x36 0x5c 0x11                   .H6\.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Base (2008, 1, 4, 9, 32, 4) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x25                                  @%
    decimal
             64   37
    datetime ((2008, 1, 4, 9, 32, 4))
    0000   0x04 0x60 0x89 0x04 0x38                   .`..8
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 10 Base (2005, 12, 12, 20, 21, 40) head[2], body[0] op[0xb1]

    op hex (2)
    0000   0xb1 0x04                                  ..
    decimal
            177    4
    datetime ((2005, 12, 12, 20, 21, 40))
    0000   0xe8 0x15 0x14 0x2c 0xb5                   ...,.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 11 SelectBasalProfile (2000, 0, 16, 0, 48, 0) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x01                                  ..
    decimal
             20    1
    datetime ((2000, 0, 16, 0, 48, 0))
    0000   0x00 0x30 0x00 0x30 0x00                   .0.0.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1]
#### RECORD 12 Base (2013, 8, 10, 1, 22, 9) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x00                                  h.
    decimal
            104    0
    datetime ((2013, 8, 10, 1, 22, 9))
    0000   0x89 0x16 0x41 0x6a 0x0d                   ..Aj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 13 BasalProfileStart 2013-08-10T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-10T04:00:00)
    0000   0x80 0x00 0x04 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 14 BasalProfileStart 2013-08-10T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-10T09:30:00)
    0000   0x80 0x1e 0x09 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 15 Base (2013, 8, 10, 10, 30, 0) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime ((2013, 8, 10, 10, 30, 0))
    0000   0x80 0x1e 0x0a 0x0a 0x0d                   .....
    body (0)

#### RECORD 16 Base (2010, 0, 13, 31, 59, 10) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0x1e                                  *.
    decimal
             42   30
    datetime ((2010, 0, 13, 31, 59, 10))
    0000   0x0a 0x3b 0x9f 0x2d 0x2a                   .;.-*
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 17 Base (2010, 0, 13, 31, 7, 63) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x0d                                  j.
    decimal
            106   13
    datetime ((2010, 0, 13, 31, 7, 63))
    0000   0x3f 0x07 0x9f 0x2d 0x6a                   ?..-j
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 18 Base (2006, 5, 6, 22, 41, 41) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x0d                                  j.
    decimal
            106   13
    datetime ((2006, 5, 6, 22, 41, 41))
    0000   0x69 0x69 0x96 0x06 0x06                   ii...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 19 ChangeBasalProfile 2013-08-10T11:22:00 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0xb6                                  ..
    decimal
              8  182
    datetime (2013-08-10T11:22:00)
    0000   0x80 0x16 0x4b 0xaa 0x0d                   ..K..
    body (44)
    hex
    0000   0x0c 0x06 0x83 0x17 0x0b 0x0a 0x0d 0x7b    .......{
    0008   0x02 0x83 0x17 0x0b 0x0a 0x0d 0x13 0x1e    ........
    0010   0x00 0x5b 0x00 0x8e 0x17 0x0b 0x6a 0x0d    .[....j.
    0018   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0020   0x78 0x00 0x00 0x00 0x00 0x78 0x36 0x69    x....x6i
    0028   0x0b 0x8e 0x17 0x0b                        ....
    decimal
             12    6  131   23   11   10   13  123
              2  131   23   11   10   13   19   30
              0   91    0  142   23   11  106   13
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54  105
             11  142   23   11
    DAY BITS: [1, 0, 1]
#### RECORD 20 CalBGForPH (2008, 0, 0, 1, 30, 14) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime ((2008, 0, 0, 1, 30, 14))
    0000   0x0e 0x1e 0x01 0x00 0x78                   ....x
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 21 Base (2007, 0, 14, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2007, 0, 14, 0, 0, 0))
    0000   0x00 0x00 0x00 0x8e 0x17                   .....
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 22 Base (2000, 1, 0, 3, 59, 13) head[2], body[0] op[0x4b]

    op hex (2)
    0000   0x4b 0x6a                                  Kj
    decimal
             75  106
    datetime ((2000, 1, 0, 3, 59, 13))
    0000   0x0d 0x7b 0x03 0x80 0x00                   .{...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 23 Base (2011, 0, 0, 6, 26, 13) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2011, 0, 0, 6, 26, 13))
    0000   0x0d 0x1a 0x26 0x00 0x5b                   ..&.[
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 24 Base (2003, 0, 13, 10, 14, 11) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x9e                                  ..
    decimal
              0  158
    datetime ((2003, 0, 13, 10, 14, 11))
    0000   0x0b 0x0e 0x6a 0x0d 0x23                   ..j.#
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 25 Base (2000, 4, 0, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 0, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x00 0x00                   n.6..
    body (0)

#### RECORD 26 Base (2006, 0, 28, 0, 0, 0) head[2], body[0] op[0x7c]

    op hex (2)
    0000   0x7c 0x00                                  |.
    decimal
            124    0
    datetime ((2006, 0, 28, 0, 0, 0))
    0000   0x00 0x00 0x00 0x7c 0x36                   ...|6
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 166, 'amount': 0.4, 'curve': 4},
 {'age': 176, 'amount': 2.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0xa6 0x04 0x68 0xb0 0x04    \....h..
    decimal
             92    8   16  166    4  104  176    4
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-08-10T14:11:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x18 0x00    ..|.|...
    decimal
              1    0  124    0  124    0   24    0
    datetime (2013-08-10T14:11:30)
    0000   0x9e 0x0b 0x4e 0x6a 0x0d                   ..Nj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 29 BolusWizard 2013-08-10T14:51:09 head[2], body[15] op[0x5b]
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
    datetime (2013-08-10T14:51:09)
    0000   0x89 0x33 0x0e 0x6a 0x0d                   .3.j.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 3.1, 'curve': 4},
 {'age': 206, 'amount': 0.4, 'curve': 4},
 {'age': 216, 'amount': 2.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x7c 0x2e 0x04 0x10 0xce 0x04    \.|.....
    0008   0x68 0xd8 0x04                             h..
    decimal
             92   11  124   46    4   16  206    4
            104  216    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-08-10T14:51:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x7c 0x00    ..h.h.|.
    decimal
              1    0  104    0  104    0  124    0
    datetime (2013-08-10T14:51:09)
    0000   0x89 0x33 0x4e 0x6a 0x0d                   .3Nj.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 CalBGForPH 2013-08-10T17:14:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 64}
```
    op hex (2)
    0000   0x0a 0x40                                  .@
    decimal
             10   64
    datetime (2013-08-10T17:14:35)
    0000   0xa3 0x0e 0x31 0x6a 0x0d                   ..1j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 33 Base (2013, 8, 10, 17, 14, 35) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime ((2013, 8, 10, 17, 14, 35))
    0000   0xa3 0x0e 0x11 0x6a 0x0d                   ...j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 34 Base (2008, 8, 7, 19, 10, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2008, 8, 7, 19, 10, 22))
    0000   0x96 0x0a 0xb3 0xa7 0x18                   .....
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 35 Base (2008, 0, 7, 22, 63, 13) head[2], body[0] op[0x32]

    op hex (2)
    0000   0x32 0x6a                                  2j
    decimal
             50  106
    datetime ((2008, 0, 7, 22, 63, 13))
    0000   0x0d 0x3f 0x16 0xa7 0x18                   .?...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 36 Base (2011, 1, 22, 9, 41, 13) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x6a                                  rj
    decimal
            114  106
    datetime ((2011, 1, 22, 9, 41, 13))
    0000   0x0d 0x69 0x69 0x96 0x5b                   .ii.[
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 37 ChangeUtility (2012, 0, 13, 10, 18, 25) head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0xa5                                  c.
    decimal
             99  165
    datetime ((2012, 0, 13, 10, 18, 25))
    0000   0x19 0x12 0x6a 0x0d 0x1c                   ..j..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 38 Base (2000, 4, 12, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 12, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x4c 0x00                   n.6L.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 39 ChangeTimeDisplay (2006, 0, 8, 0, 8, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime ((2006, 0, 8, 0, 8, 0))
    0000   0x00 0x08 0x00 0xa8 0x36                   ....6
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 220, 'amount': 2.6, 'curve': 4},
 {'age': 4, 'amount': 3.1, 'curve': 20},
 {'age': 164, 'amount': 0.4, 'curve': 20},
 {'age': 174, 'amount': 2.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0xdc 0x04 0x7c 0x04 0x14    \.h..|..
    0008   0x10 0xa4 0x14 0x68 0xae 0x14              ...h..
    decimal
             92   14  104  220    4  124    4   20
             16  164   20  104  174   20
    datetime (unknown)

    body (0)

#### RECORD 41 Base (2013, 8, 10, 18, 25, 37) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2013, 8, 10, 18, 25, 37))
    0000   0xa5 0x19 0x72 0x0a 0x0d                   ..r..
    body (0)

#### RECORD 42 Base (2008, 0, 0, 8, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2008, 0, 0, 8, 0, 1))
    0000   0x01 0x00 0xa8 0x00 0xa8                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 43 Base (2010, 2, 18, 25, 37, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x08                                  ..
    decimal
              0    8
    datetime ((2010, 2, 18, 25, 37, 0))
    0000   0x00 0xa5 0x19 0x52 0x6a                   ...Rj
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 44 Base (2010, 2, 20, 18, 40, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2010, 2, 20, 18, 40, 0))
    0000   0x00 0xa8 0x12 0x14 0x6a                   ....j
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 45 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1d                                  ..
    decimal
             13   29
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-24.data: 46 records`
