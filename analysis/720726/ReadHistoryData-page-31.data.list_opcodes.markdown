## START logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 386, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x5e 0xc3 0x4d 0x7f 0x0d 0x5b 0x00 0x79    ^.M..[.y
    0008   0xdb 0x0d 0x7f 0x0d 0x1e 0x90 0x00 0x6e    .......n
    0010   0x17 0x36 0x00 0x00 0x6c 0x00 0x00 0x00    .6..l...
    0018   0x00 0x6c 0x36 0x5c 0x08 0x30 0x16 0x04    .l6\.0..
##### DEBUG DECIMAL
             94  195   77  127   13   91    0  121
            219   13  127   13   30  144    0  110
             23   54    0    0  108    0    0    0
              0  108   54   92    8   48   22    4
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
#### RECORD 14 Ian3F 2013-07-31T07:58:14 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-07-31T07:58:14)
    0000   0x4e 0xfa 0x07 0x7f 0x0d                   N....
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 15 CalBGForPH 2013-07-31T09:11:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-07-31T09:11:08)
    0000   0x48 0xcb 0x29 0x7f 0x0d                   H.)..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 Ian3F 2013-07-31T09:11:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2013-07-31T09:11:08)
    0000   0x48 0xcb 0x89 0x7f 0x0d                   H....
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 BasalProfileStart 2013-07-31T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-31T09:30:00)
    0000   0x40 0xde 0x09 0x1f 0x0d                   @....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 18 CalBGForPH 2013-07-31T10:22:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-07-31T10:22:06)
    0000   0x46 0xd6 0x2a 0x7f 0x0d                   F.*..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 19 Ian3F 2013-07-31T10:22:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2013-07-31T10:22:06)
    0000   0x46 0xd6 0x4a 0x7f 0x0d                   F.J..
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 Ian69 2013-07-31T10:30:00 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-07-31T10:30:00)
    0000   0x40 0xde 0x0a 0x1f 0x0d                   @....
    body (8)
    hex
    0000   0x2a 0x1e 0x0a 0x7c 0x42 0xd1 0x2b 0x7f    *..|B.+.
    decimal
             42   30   10  124   66  209   43  127
    HOUR BITS: [1, 1, 0]
#### RECORD 21 Base (2015, 1, 11, 17, 2, 15) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2015, 1, 11, 17, 2, 15))
    0000   0x0f 0x42 0xd1 0x8b 0x7f                   .B...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 22 Base (2008, 6, 6, 6, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2008, 6, 6, 6, 22, 41))
    0000   0x69 0x96 0x06 0x06 0x08                   i....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 Base (2012, 13, 13, 31, 11, 41) head[2], body[0] op[0xb6]

    op hex (2)
    0000   0xb6 0x40                                  .@
    decimal
            182   64
    datetime ((2012, 13, 13, 31, 11, 41))
    0000   0xe9 0x4b 0xbf 0x0d 0x0c                   .K...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 24 NoDelivery (2005, 0, 2, 27, 13, 31) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x44 0xed 0x0b                        .D..
    decimal
              6   68  237   11
    datetime ((2005, 0, 2, 27, 13, 31))
    0000   0x1f 0x0d 0x7b 0x02 0x45                   ..{.E
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 25 Base (2000, 0, 30, 19, 13, 31) head[2], body[0] op[0xed]

    op hex (2)
    0000   0xed 0x0b                                  ..
    decimal
            237   11
    datetime ((2000, 0, 30, 19, 13, 31))
    0000   0x1f 0x0d 0x13 0x1e 0x00                   .....
    body (0)

#### RECORD 26 BasalProfileStart 2013-07-31T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-31T13:00:00)
    0000   0x40 0xc0 0x0d 0x1f 0x0d                   @....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [1, 1, 0]
#### RECORD 27 CalBGForPH 2013-07-31T13:03:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 240}
```
    op hex (2)
    0000   0x0a 0xf0                                  ..
    decimal
             10  240
    datetime (2013-07-31T13:03:20)
    0000   0x54 0xc3 0x2d 0x7f 0x0d                   T.-..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 Ian3F 2013-07-31T13:03:20 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1e                                  ?.
    decimal
             63   30
    datetime (2013-07-31T13:03:20)
    0000   0x54 0xc3 0x0d 0x7f 0x0d                   T....
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 BolusWizard 2013-07-31T13:03:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 13.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2013-07-31T13:03:30)
    0000   0x5e 0xc3 0x0d 0x7f 0x0d                   ^....
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x88 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x88 0x36         ......6
    decimal
              0  144    0  110   23   54  136    0
              0    0    0    0    0  136   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 Ian69 2013-07-31T13:03:30 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-07-31T13:03:30)
    0000   0x5e 0xc3 0x0d 0x1f 0x0d                   ^....
    body (8)
    hex
    0000   0x0e 0x1e 0x01 0x00 0x88 0x00 0x88 0x00    ........
    decimal
             14   30    1    0  136    0  136    0
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-31.data: 31 records`
