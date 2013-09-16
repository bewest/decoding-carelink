## START logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 411, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6c 0x36 0x5c 0x08 0x30 0x16 0x04 0x58    l6\.0..X
    0008   0x20 0x04 0x01 0x00 0x6c 0x00 0x6c 0x00     ...l.l.
    0010   0x84 0x00 0x79 0xdb 0x4d 0x7f 0x0d 0x5b    ..y.M..[
    0018   0x00 0x50 0xe1 0x0d 0x7f 0x0d 0x0a 0x90    .P......
##### DEBUG DECIMAL
            108   54   92    8   48   22    4   88
             32    4    1    0  108    0  108    0
            132    0  121  219   77  127   13   91
              0   80  225   13  127   13   10  144
#### RECORD 0 ResultTotals (2000, 6, 0, 0, 13, 62) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x8d                   .....
    decimal
              7    0    0    7  141
    datetime ((2000, 6, 0, 0, 13, 62))
    0000   0x7e 0x8d 0x00 0x00 0x00                   ~....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 1 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7e 0x8d 0x06 0x10 0xf8 0xab 0x46    n~.....F
    0008   0x05 0x00 0x00 0x07 0x8d 0x03 0x69 0x2d    ......i-
    0010   0x04 0x24 0x37 0x00 0x92 0x01 0xc4 0x01    .$7.....
    0018   0x48 0x01 0x18 0x00 0x00 0x04 0x02 0x01    H.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  126  141    6   16  248  171   70
              5    0    0    7  141    3  105   45
              4   36   55    0  146    1  196    1
             72    1   24    0    0    4    2    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 2 BolusWizard 2013-07-31T00:34:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 32,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T00:34:42)
    0000   0x6a 0xe2 0x00 0x7f 0x0d                   j....
    body (15)
    hex
    0000   0x20 0x90 0x00 0x6e 0x17 0x36 0x00 0x00     ..n.6..
    0008   0x74 0x00 0x00 0x00 0x00 0x74 0x36         t....t6
    decimal
             32  144    0  110   23   54    0    0
            116    0    0    0    0  116   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 2.75, 'curve': 4},
 {'age': 119, 'amount': 4.25, 'curve': 4},
 {'age': 93, 'amount': 3.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6e 0x6d 0x04 0xaa 0x77 0x04    \.nm..w.
    0008   0x8c 0x5d 0x14                             .].
    decimal
             92   11  110  109    4  170  119    4
            140   93   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-07-31T00:34:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x8c 0x00    ..t.t...
    decimal
              1    0  116    0  116    0  140    0
    datetime (2013-07-31T00:34:42)
    0000   0x6a 0xe2 0x40 0x7f 0x0d                   j.@..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2013-07-31T00:42:14 head[2], body[15] op[0x5b]
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
    datetime (2013-07-31T00:42:14)
    0000   0x4e 0xea 0x00 0x7f 0x0d                   N....
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 2.45, 'curve': 4},
 {'age': 17, 'amount': 0.45, 'curve': 4},
 {'age': 117, 'amount': 2.75, 'curve': 4},
 {'age': 127, 'amount': 4.25, 'curve': 4},
 {'age': 101, 'amount': 3.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x62 0x07 0x04 0x12 0x11 0x04    \.b.....
    0008   0x6e 0x75 0x04 0xaa 0x7f 0x04 0x8c 0x65    nu.....e
    0010   0x14                                       .
    decimal
             92   17   98    7    4   18   17    4
            110  117    4  170  127    4  140  101
             20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-07-31T00:42:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0xf0 0x00    ..@.@...
    decimal
              1    0   64    0   64    0  240    0
    datetime (2013-07-31T00:42:14)
    0000   0x4e 0xea 0x40 0x7f 0x0d                   N.@..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Rewind 2013-07-31T01:40:33 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-31T01:40:33)
    0000   0x61 0xe8 0x01 0x1f 0x0d                   a....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 Prime 2013-07-31T01:41:15 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 5.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x35                   ....5
    decimal
              3    0    0    0   53
    datetime (2013-07-31T01:41:15)
    0000   0x4f 0xe9 0x21 0x1f 0x0d                   O.!..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 BasalProfileStart 2013-07-31T01:42:05 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-31T01:42:05)
    0000   0x45 0xea 0x01 0x1f 0x0d                   E....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 1]
#### RECORD 11 Prime 2013-07-31T01:41:31 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-07-31T01:41:31)
    0000   0x5f 0xe9 0x01 0x1f 0x0d                   _....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 12 BasalProfileStart 2013-07-31T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-31T04:00:00)
    0000   0x40 0xc0 0x04 0x1f 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 0]
#### RECORD 13 CalBGForPH 2013-07-31T07:58:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-07-31T07:58:14)
    0000   0x4e 0xfa 0x27 0x7f 0x0d                   N.'..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 Base (2013, 7, 31, 7, 58, 14) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime ((2013, 7, 31, 7, 58, 14))
    0000   0x4e 0xfa 0x07 0x7f 0x0d                   N....
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 15 Ian69 2011-08-08T20:10:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2011-08-08T20:10:22)
    0000   0x96 0x0a 0x74 0x48 0xcb                   ..tH.
    body (8)
    hex
    0000   0x29 0x7f 0x0d 0x3f 0x0e 0x48 0xcb 0x89    )..?.H..
    decimal
             41  127   13   63   14   72  203  137
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 16 Base (2002, 5, 27, 22, 41, 41) head[2], body[0] op[0x7f]

    op hex (2)
    0000   0x7f 0x0d                                  ..
    decimal
            127   13
    datetime ((2002, 5, 27, 22, 41, 41))
    0000   0x69 0x69 0x96 0x7b 0x02                   ii.{.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 Base (2014, 0, 19, 13, 31, 9) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0xde                                  @.
    decimal
             64  222
    datetime ((2014, 0, 19, 13, 31, 9))
    0000   0x09 0x1f 0x0d 0x13 0x1e                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 18 Base (2015, 5, 10, 22, 6, 42) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2015, 5, 10, 22, 6, 42))
    0000   0x6a 0x46 0xd6 0x2a 0x7f                   jF.*.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 19 Base (2015, 1, 10, 22, 6, 13) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2015, 1, 10, 22, 6, 13))
    0000   0x0d 0x46 0xd6 0x4a 0x7f                   .F.J.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 20 Base (2000, 6, 8, 9, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2000, 6, 8, 9, 22, 41))
    0000   0x69 0x96 0x69 0x08 0x40                   i.i.@
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 21 Base (2010, 0, 30, 10, 13, 31) head[2], body[0] op[0xde]

    op hex (2)
    0000   0xde 0x0a                                  ..
    decimal
            222   10
    datetime ((2010, 0, 30, 10, 13, 31))
    0000   0x1f 0x0d 0x2a 0x1e 0x0a                   ..*..
    body (0)

#### RECORD 22 Base (2015, 12, 13, 31, 43, 17) head[2], body[0] op[0x7c]

    op hex (2)
    0000   0x7c 0x42                                  |B
    decimal
            124   66
    datetime ((2015, 12, 13, 31, 43, 17))
    0000   0xd1 0x2b 0x7f 0x0d 0x3f                   .+..?
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 23 Base (2009, 14, 13, 31, 11, 17) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x42                                  .B
    decimal
             15   66
    datetime ((2009, 14, 13, 31, 11, 17))
    0000   0xd1 0x8b 0x7f 0x0d 0x69                   ....i
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 24 Ian69 (2000, 0, 22, 8, 6, 6) head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x96                                  i.
    decimal
            105  150
    datetime ((2000, 0, 22, 8, 6, 6))
    0000   0x06 0x06 0x08 0xb6 0x40                   ....@
    body (8)
    hex
    0000   0xe9 0x4b 0xbf 0x0d 0x0c 0x06 0x44 0xed    .K....D.
    decimal
            233   75  191   13   12    6   68  237
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 25 Ian0B 2011-04-13T05:02:59 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x1f 0x0d                             ...
    decimal
             11   31   13
    datetime (2011-04-13T05:02:59)
    0000   0x7b 0x02 0x45 0xed 0x0b                   {.E..
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 26 PumpResume (2003, 0, 27, 0, 30, 19) head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x0d                                  ..
    decimal
             31   13
    datetime ((2003, 0, 27, 0, 30, 19))
    0000   0x13 0x1e 0x00 0x7b 0x03                   ...{.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 27 Base (2006, 0, 26, 13, 31, 13) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0xc0                                  @.
    decimal
             64  192
    datetime ((2006, 0, 26, 13, 31, 13))
    0000   0x0d 0x1f 0x0d 0x1a 0x26                   ....&
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 28 Base (2015, 13, 13, 3, 20, 48) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2015, 13, 13, 3, 20, 48))
    0000   0xf0 0x54 0xc3 0x2d 0x7f                   .T.-.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 29 Base (2015, 1, 13, 3, 20, 30) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2015, 1, 13, 3, 20, 30))
    0000   0x1e 0x54 0xc3 0x0d 0x7f                   .T...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 30 Base (2014, 6, 5, 27, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2014, 6, 5, 27, 22, 41))
    0000   0x69 0x96 0x5b 0x85 0x5e                   i.[.^
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 31 Base (2000, 4, 16, 0, 13, 63) head[2], body[0] op[0xc3]

    op hex (2)
    0000   0xc3 0x0d                                  ..
    decimal
            195   13
    datetime ((2000, 4, 16, 0, 13, 63))
    0000   0x7f 0x0d 0x00 0x90 0x00                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 32 Sara6E (2000, 0, 0, 12, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x17 0x36 0x88 0x00 0x00 0x00 0x00    n.6.....
    0008   0x00 0x00 0x88 0x36 0x69 0x0b 0x5e 0xc3    ...6i.^.
    0010   0x0d 0x1f 0x0d 0x0e 0x1e 0x01 0x00 0x88    ........
    0018   0x00 0x88 0x00 0x00 0x00 0x5e 0xc3 0x4d    .....^.M
    0020   0x7f 0x0d 0x5b 0x00 0x79 0xdb 0x0d 0x7f    ..[.y...
    0028   0x0d 0x1e 0x90 0x00 0x6e 0x17 0x36         ....n.6
    decimal
            110   23   54  136    0    0    0    0
              0    0  136   54  105   11   94  195
             13   31   13   14   30    1    0  136
              0  136    0    0    0   94  195   77
            127   13   91    0  121  219   13  127
             13   30  144    0  110   23   54
    datetime ((2000, 0, 0, 12, 0, 0))
    0000   0x00 0x00 0x6c 0x00 0x00                   ..l..
    body (0)

`end logs/ReadHistoryData-page-31.data: 33 records`
