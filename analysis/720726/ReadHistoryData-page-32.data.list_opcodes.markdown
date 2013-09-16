## START logs/ReadHistoryData-page-32.data
#### STOPPING DOUBLE NULLS @ 255, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x4c 0x36 0x5c 0x0e 0x50 0x1d 0x04 0xb4    L6\.P...
    0008   0xdb 0x04 0x48 0x53 0x14 0x74 0xd5 0x14    ..HS.t..
    0010   0x01 0x00 0x4c 0x00 0x4c 0x00 0x5c 0x00    ..L.L.\.
    0018   0x74 0xec 0x53 0x7d 0x0d 0x5b 0x00 0x6d    t.S}.[.m
##### DEBUG DECIMAL
             76   54   92   14   80   29    4  180
            219    4   72   83   20  116  213   20
              1    0   76    0   76    0   92    0
            116  236   83  125   13   91    0  109
#### RECORD 0 BolusWizard 2013-07-29T14:12:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T14:12:39)
    0000   0x67 0xcc 0x0e 0x7d 0x0d                   g..}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 2.9, 'curve': 4},
 {'age': 157, 'amount': 3.0, 'curve': 4},
 {'age': 81, 'amount': 2.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x74 0x89 0x04 0x78 0x9d 0x04    \.t..x..
    0008   0x70 0x51 0x14                             pQ.
    decimal
             92   11  116  137    4  120  157    4
            112   81   20
    datetime (unknown)

    body (0)

#### RECORD 2 BolusWizard 2013-07-29T14:12:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T14:12:41)
    0000   0x69 0xcc 0x0e 0x7d 0x0d                   i..}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 2.9, 'curve': 4},
 {'age': 157, 'amount': 3.0, 'curve': 4},
 {'age': 81, 'amount': 2.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x74 0x89 0x04 0x78 0x9d 0x04    \.t..x..
    0008   0x70 0x51 0x14                             pQ.
    decimal
             92   11  116  137    4  120  157    4
            112   81   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-07-29T14:12:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x4c 0x00    ..H.H.L.
    decimal
              1    0   72    0   72    0   76    0
    datetime (2013-07-29T14:12:41)
    0000   0x69 0xcc 0x4e 0x7d 0x0d                   i.N}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 CalBGForPH 2013-07-29T14:51:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-07-29T14:51:04)
    0000   0x44 0xf3 0x2e 0x7d 0x0d                   D..}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 Base (2013, 7, 29, 14, 51, 4) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime ((2013, 7, 29, 14, 51, 4))
    0000   0x44 0xf3 0x0e 0x7d 0x0d                   D..}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 Base (2006, 8, 0, 24, 10, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2006, 8, 0, 24, 10, 22))
    0000   0x96 0x0a 0xd8 0x60 0xc6                   ...`.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 8 Base (2006, 0, 0, 27, 63, 13) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x7d                                  0}
    decimal
             48  125
    datetime ((2006, 0, 0, 27, 63, 13))
    0000   0x0d 0x3f 0x1b 0x60 0xc6                   .?.`.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 9 Base (2011, 1, 22, 9, 41, 13) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x7d                                  .}
    decimal
             16  125
    datetime ((2011, 1, 22, 9, 41, 13))
    0000   0x0d 0x69 0x69 0x96 0x5b                   .ii.[
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 10 Base (2004, 12, 13, 29, 16, 6) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x6d                                  xm
    decimal
            120  109
    datetime ((2004, 12, 13, 29, 16, 6))
    0000   0xc6 0x10 0x7d 0x0d 0x14                   ..}..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 11 Base (2000, 4, 16, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 16, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x70 0x00                   n.6p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 12 Base (2006, 0, 20, 0, 36, 0) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x00                                  H.
    decimal
             72    0
    datetime ((2006, 0, 20, 0, 36, 0))
    0000   0x00 0x24 0x00 0x94 0x36                   .$..6
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 1.8, 'curve': 4},
 {'age': 251, 'amount': 2.9, 'curve': 4},
 {'age': 15, 'amount': 3.0, 'curve': 20},
 {'age': 195, 'amount': 2.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x79 0x04 0x74 0xfb 0x04    \.Hy.t..
    0008   0x78 0x0f 0x14 0x70 0xc3 0x14              x..p..
    decimal
             92   14   72  121    4  116  251    4
            120   15   20  112  195   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-07-29T16:06:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 18.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x24 0x00    ......$.
    decimal
              1    0  180    0  180    0   36    0
    datetime (2013-07-29T16:06:45)
    0000   0x6d 0xc6 0x50 0x7d 0x0d                   m.P}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 CalBGForPH 2013-07-29T19:13:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2013-07-29T19:13:04)
    0000   0x44 0xcd 0x33 0x7d 0x0d                   D.3}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 Base (2013, 7, 29, 19, 13, 4) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime ((2013, 7, 29, 19, 13, 4))
    0000   0x44 0xcd 0x93 0x7d 0x0d                   D..}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 Base (2005, 9, 4, 10, 27, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2005, 9, 4, 10, 27, 22))
    0000   0x96 0x5b 0x2a 0x44 0xd5                   .[*D.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 18 Base (2014, 0, 0, 16, 28, 13) head[2], body[0] op[0x13]

    op hex (2)
    0000   0x13 0x7d                                  .}
    decimal
             19  125
    datetime ((2014, 0, 0, 16, 28, 13))
    0000   0x0d 0x1c 0x90 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 ChangeTime 2000-12-24T04:00:44 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x36                                  .6
    decimal
             23   54
    datetime (2000-12-24T04:00:44)
    0000   0xec 0x00 0x64 0xf8 0x00                   ..d..
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 20 NewTimeSet (2004, 4, 14, 28, 54, 16) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime ((2004, 4, 14, 28, 54, 16))
    0000   0x50 0x36 0x5c 0x0e 0xb4                   P6\..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 21 Base (2014, 4, 20, 20, 60, 8) head[2], body[0] op[0xc4]

    op hex (2)
    0000   0xc4 0x04                                  ..
    decimal
            196    4
    datetime ((2014, 4, 20, 20, 60, 8))
    0000   0x48 0x3c 0x14 0x74 0xbe                   H<.t.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 22 SelectBasalProfile 2004-12-17T09:20:18 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x78                                  .x
    decimal
             20  120
    datetime (2004-12-17T09:20:18)
    0000   0xd2 0x14 0x69 0xd1 0x44                   ..i.D
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 23 Base (2001, 0, 30, 21, 13, 29) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x73                                  .s
    decimal
            213  115
    datetime ((2001, 0, 30, 21, 13, 29))
    0000   0x1d 0x0d 0x15 0x1e 0x01                   .....
    body (0)

#### RECORD 24 Base (2000, 1, 24, 0, 16, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x50                                  .P
    decimal
              0   80
    datetime ((2000, 1, 24, 0, 16, 0))
    0000   0x00 0x50 0x00 0x18 0x00                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 25 Base (2000, 5, 27, 13, 61, 19) head[2], body[0] op[0x44]

    op hex (2)
    0000   0x44 0xd5                                  D.
    decimal
             68  213
    datetime ((2000, 5, 27, 13, 61, 19))
    0000   0x53 0x7d 0x0d 0x5b 0x00                   S}.[.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 26 Base (2000, 1, 21, 13, 61, 19) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0xec                                  t.
    decimal
            116  236
    datetime ((2000, 1, 21, 13, 61, 19))
    0000   0x13 0x7d 0x0d 0x15 0x90                   .}...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 27 Base (2012, 0, 0, 0, 54, 23) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6e                                  .n
    decimal
              0  110
    datetime ((2012, 0, 0, 0, 54, 23))
    0000   0x17 0x36 0x00 0x00 0x4c                   .6..L
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
`end logs/ReadHistoryData-page-32.data: 28 records`
