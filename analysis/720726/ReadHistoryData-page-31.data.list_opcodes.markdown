## START analysis/ianj/raw//ReadHistoryData-page-31.data
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
#### RECORD 20 Ian69 2013-07-31T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-07-31T10:30:00)
    0000   0x40 0xde 0x0a 0x1f 0x0d                   @....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30
    HOUR BITS: [1, 1, 0]
#### RECORD 21 CalBGForPH 2013-07-31T11:17:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-07-31T11:17:02)
    0000   0x42 0xd1 0x2b 0x7f 0x0d                   B.+..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 22 Ian3F 2013-07-31T11:17:02 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2013-07-31T11:17:02)
    0000   0x42 0xd1 0x8b 0x7f 0x0d                   B....
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 NoDelivery 2013-07-31T11:41:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2013-07-31T11:41:00)
    0000   0x40 0xe9 0x4b 0xbf 0x0d                   @.K..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 24 ClearAlarm 2013-07-31T11:45:04 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2013-07-31T11:45:04)
    0000   0x44 0xed 0x0b 0x1f 0x0d                   D....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 BasalProfileStart 2013-07-31T11:45:05 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-31T11:45:05)
    0000   0x45 0xed 0x0b 0x1f 0x0d                   E....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [1, 1, 1]
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
#### RECORD 30 Ian69 2013-07-31T13:03:30 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-07-31T13:03:30)
    0000   0x5e 0xc3 0x0d 0x1f 0x0d                   ^....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [1, 1, 0]
#### RECORD 31 Bolus 2013-07-31T13:03:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x00 0x00    ........
    decimal
              1    0  136    0  136    0    0    0
    datetime (2013-07-31T13:03:30)
    0000   0x5e 0xc3 0x4d 0x7f 0x0d                   ^.M..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2013-07-31T13:27:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T13:27:57)
    0000   0x79 0xdb 0x0d 0x7f 0x0d                   y....
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 1.2, 'curve': 4},
 {'age': 32, 'amount': 2.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x16 0x04 0x58 0x20 0x04    \.0..X .
    decimal
             92    8   48   22    4   88   32    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-07-31T13:27:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x84 0x00    ..l.l...
    decimal
              1    0  108    0  108    0  132    0
    datetime (2013-07-31T13:27:57)
    0000   0x79 0xdb 0x4d 0x7f 0x0d                   y.M..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2013-07-31T13:33:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T13:33:16)
    0000   0x50 0xe1 0x0d 0x7f 0x0d                   P....
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 2.7, 'curve': 4},
 {'age': 28, 'amount': 1.2, 'curve': 4},
 {'age': 38, 'amount': 2.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0x08 0x04 0x30 0x1c 0x04    \.l..0..
    0008   0x58 0x26 0x04                             X&.
    decimal
             92   11  108    8    4   48   28    4
             88   38    4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-07-31T13:33:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0xec 0x00    ..$.$...
    decimal
              1    0   36    0   36    0  236    0
    datetime (2013-07-31T13:33:16)
    0000   0x50 0xe1 0x4d 0x7f 0x0d                   P.M..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2013-07-31T16:47:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T16:47:15)
    0000   0x4f 0xef 0x10 0x7f 0x0d                   O....
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 202, 'amount': 3.6, 'curve': 4},
 {'age': 222, 'amount': 1.2, 'curve': 4},
 {'age': 232, 'amount': 2.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x90 0xca 0x04 0x30 0xde 0x04    \....0..
    0008   0x58 0xe8 0x04                             X..
    decimal
             92   11  144  202    4   48  222    4
             88  232    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-07-31T16:47:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x1c 0x00    ..l.l...
    decimal
              1    0  108    0  108    0   28    0
    datetime (2013-07-31T16:47:15)
    0000   0x4f 0xef 0x50 0x7f 0x0d                   O.P..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 CalBGForPH 2013-07-31T17:51:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 74}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2013-07-31T17:51:28)
    0000   0x5c 0xf3 0x31 0x7f 0x0d                   \.1..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 Ian3F 2013-07-31T17:51:28 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-07-31T17:51:28)
    0000   0x5c 0xf3 0x51 0x7f 0x0d                   \.Q..
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 BolusWizard 2013-07-31T17:56:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 41,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 8.4,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 23.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x29                                  [)
    decimal
             91   41
    datetime (2013-07-31T17:56:21)
    0000   0x55 0xf8 0x11 0x7f 0x0d                   U....
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0xe8 0x00    ...n.6..
    0008   0x40 0xf8 0x00 0x54 0x00 0x28 0x36         @..T.(6
    decimal
             18  144    0  110   23   54  232    0
             64  248    0   84    0   40   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 2.7, 'curve': 4},
 {'age': 15, 'amount': 3.6, 'curve': 20},
 {'age': 35, 'amount': 1.2, 'curve': 20},
 {'age': 45, 'amount': 2.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0x47 0x04 0x90 0x0f 0x14    \.lG....
    0008   0x30 0x23 0x14 0x58 0x2d 0x14              0#.X-.
    decimal
             92   14  108   71    4  144   15   20
             48   35   20   88   45   20
    datetime (unknown)

    body (0)

#### RECORD 45 Ian69 2013-07-31T17:56:22 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-31T17:56:22)
    0000   0x56 0xf8 0x71 0x1f 0x0d                   V.q..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [1, 1, 1]
#### RECORD 46 Bolus 2013-07-31T17:56:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x54 0x00    ..(.(.T.
    decimal
              1    0   40    0   40    0   84    0
    datetime (2013-07-31T17:56:21)
    0000   0x55 0xf8 0x51 0x7f 0x0d                   U.Q..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2013-07-31T18:29:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T18:29:00)
    0000   0x40 0xdd 0x12 0x7f 0x0d                   @....
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 1.0, 'curve': 4},
 {'age': 104, 'amount': 2.7, 'curve': 4},
 {'age': 48, 'amount': 3.6, 'curve': 20},
 {'age': 68, 'amount': 1.2, 'curve': 20},
 {'age': 78, 'amount': 2.2, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0x22 0x04 0x6c 0x68 0x04    \.(".lh.
    0008   0x90 0x30 0x14 0x30 0x44 0x14 0x58 0x4e    .0.0D.XN
    0010   0x14                                       .
    decimal
             92   17   40   34    4  108  104    4
            144   48   20   48   68   20   88   78
             20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-07-31T18:29:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x64 0x00    ......d.
    decimal
              1    0  144    0  144    0  100    0
    datetime (2013-07-31T18:29:00)
    0000   0x40 0xdd 0x52 0x7f 0x0d                   @.R..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 50 BolusWizard 2013-07-31T20:36:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T20:36:18)
    0000   0x52 0xe4 0x14 0x7f 0x0d                   R....
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 131, 'amount': 3.6, 'curve': 4},
 {'age': 161, 'amount': 1.0, 'curve': 4},
 {'age': 231, 'amount': 2.7, 'curve': 4},
 {'age': 175, 'amount': 3.6, 'curve': 20},
 {'age': 195, 'amount': 1.2, 'curve': 20},
 {'age': 205, 'amount': 2.2, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x90 0x83 0x04 0x28 0xa1 0x04    \....(..
    0008   0x6c 0xe7 0x04 0x90 0xaf 0x14 0x30 0xc3    l.....0.
    0010   0x14 0x58 0xcd 0x14                        .X..
    decimal
             92   20  144  131    4   40  161    4
            108  231    4  144  175   20   48  195
             20   88  205   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-07-31T20:36:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x4c 0x00    ..d.d.L.
    decimal
              1    0  100    0  100    0   76    0
    datetime (2013-07-31T20:36:18)
    0000   0x52 0xe4 0x54 0x7f 0x0d                   R.T..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 53 BolusWizard 2013-07-31T20:40:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T20:40:10)
    0000   0x4a 0xe8 0x14 0x7f 0x0d                   J....
    body (15)
    hex
    0000   0x11 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x3c 0x00 0x00 0x00 0x00 0x3c 0x36         <....<6
    decimal
             17  144    0  110   23   54    0    0
             60    0    0    0    0   60   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 2.5, 'curve': 4},
 {'age': 135, 'amount': 3.6, 'curve': 4},
 {'age': 165, 'amount': 1.0, 'curve': 4},
 {'age': 235, 'amount': 2.7, 'curve': 4},
 {'age': 179, 'amount': 3.6, 'curve': 20},
 {'age': 199, 'amount': 1.2, 'curve': 20},
 {'age': 209, 'amount': 2.2, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x64 0x05 0x04 0x90 0x87 0x04    \.d.....
    0008   0x28 0xa5 0x04 0x6c 0xeb 0x04 0x90 0xb3    (..l....
    0010   0x14 0x30 0xc7 0x14 0x58 0xd1 0x14         .0..X..
    decimal
             92   23  100    5    4  144  135    4
             40  165    4  108  235    4  144  179
             20   48  199   20   88  209   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-07-31T20:40:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xac 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  172    0
    datetime (2013-07-31T20:40:10)
    0000   0x4a 0xe8 0x54 0x7f 0x0d                   J.T..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 BolusWizard 2013-07-31T22:47:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T22:47:25)
    0000   0x59 0xef 0x16 0x7f 0x0d                   Y....
    body (15)
    hex
    0000   0x17 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             23  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 132, 'amount': 4.0, 'curve': 4},
 {'age': 6, 'amount': 3.6, 'curve': 20},
 {'age': 36, 'amount': 1.0, 'curve': 20},
 {'age': 106, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xa0 0x84 0x04 0x90 0x06 0x14    \.......
    0008   0x28 0x24 0x14 0x6c 0x6a 0x14              ($.lj.
    decimal
             92   14  160  132    4  144    6   20
             40   36   20  108  106   20
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-07-31T22:47:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x40 0x00    ..P.P.@.
    decimal
              1    0   80    0   80    0   64    0
    datetime (2013-07-31T22:47:25)
    0000   0x59 0xef 0x56 0x7f 0x0d                   Y.V..
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 BolusWizard 2013-07-31T23:02:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-31T23:02:42)
    0000   0x6a 0xc2 0x17 0x7f 0x0d                   j....
    body (15)
    hex
    0000   0x17 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             23  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 2.0, 'curve': 4},
 {'age': 147, 'amount': 4.0, 'curve': 4},
 {'age': 21, 'amount': 3.6, 'curve': 20},
 {'age': 51, 'amount': 1.0, 'curve': 20},
 {'age': 121, 'amount': 2.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x11 0x04 0xa0 0x93 0x04    \.P.....
    0008   0x90 0x15 0x14 0x28 0x33 0x14 0x6c 0x79    ...(3.ly
    0010   0x14                                       .
    decimal
             92   17   80   17    4  160  147    4
            144   21   20   40   51   20  108  121
             20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-07-31T23:02:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x84 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  132    0
    datetime (2013-07-31T23:02:42)
    0000   0x6a 0xc2 0x57 0x7f 0x0d                   j.W..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 BasalProfileStart 2013-08-01T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-01T00:00:00)
    0000   0x80 0x00 0x00 0x01 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 63 ResultTotals (2000, 6, 0, 0, 13, 63) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xb6                   .....
    decimal
              7    0    0    7  182
    datetime ((2000, 6, 0, 0, 13, 63))
    0000   0x7f 0x8d 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 64 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7f 0x8d 0x06 0x00 0x7a 0x48 0xf0    n....zH.
    0008   0x06 0x00 0x00 0x07 0xb6 0x03 0x86 0x2e    ........
    0010   0x04 0x30 0x36 0x01 0x0d 0x03 0xa8 0x00    .06.....
    0018   0x88 0x00 0x00 0x00 0x00 0x0b 0x01 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  127  141    6    0  122   72  240
              6    0    0    7  182    3  134   46
              4   48   54    1   13    3  168    0
            136    0    0    0    0   11    1    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 65 BolusWizard 2013-08-01T00:02:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 24,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-01T00:02:57)
    0000   0xb9 0x02 0x00 0x61 0x0d                   ...a.
    body (15)
    hex
    0000   0x18 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x54 0x00 0x00 0x00 0x00 0x54 0x36         T....T6
    decimal
             24  144    0  110   23   54    0    0
             84    0    0    0    0   84   54
    DAY BITS: [0, 1, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 2.0, 'curve': 4},
 {'age': 77, 'amount': 2.0, 'curve': 4},
 {'age': 207, 'amount': 4.0, 'curve': 4},
 {'age': 81, 'amount': 3.6, 'curve': 20},
 {'age': 111, 'amount': 1.0, 'curve': 20},
 {'age': 181, 'amount': 2.7, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x50 0x43 0x04 0x50 0x4d 0x04    \.PC.PM.
    0008   0xa0 0xcf 0x04 0x90 0x51 0x14 0x28 0x6f    ....Q.(o
    0010   0x14 0x6c 0xb5 0x14                        .l..
    decimal
             92   20   80   67    4   80   77    4
            160  207    4  144   81   20   40  111
             20  108  181   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-08-01T00:02:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x8c 0x00    ..T.T...
    decimal
              1    0   84    0   84    0  140    0
    datetime (2013-08-01T00:02:57)
    0000   0xb9 0x02 0x40 0x61 0x0d                   ..@a.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 68 BasalProfileStart 2013-08-01T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-01T04:00:00)
    0000   0x80 0x00 0x04 0x01 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 69 CalBGForPH 2013-08-01T07:59:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-08-01T07:59:34)
    0000   0xa2 0x3b 0x27 0x61 0x0d                   .;'a.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 Ian3F 2013-08-01T07:59:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2013-08-01T07:59:34)
    0000   0xa2 0x3b 0x67 0x61 0x0d                   .;ga.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 71 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x67                                  .g
    decimal
              0  103
    datetime (unknown)

    body (0)

`end analysis/ianj/raw//ReadHistoryData-page-31.data: 72 records`
