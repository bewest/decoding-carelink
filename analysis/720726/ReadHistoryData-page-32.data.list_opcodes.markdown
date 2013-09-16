## START logs/ReadHistoryData-page-32.data
#### STOPPING DOUBLE NULLS @ 479, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x7b 0x01 0x40 0xc0 0x04 0x1e 0x0d 0x08    {.@.....
    0008   0x2e 0x00 0x0a 0xee 0x6a 0xc4 0x28 0x7e    ....j.(~
    0010   0x0d 0x3f 0x1d 0x6a 0xc4 0xc8 0x7e 0x0d    .?.j..~.
    0018   0x69 0x69 0x96 0x5b 0x84 0x72 0xc4 0x08    ii.[.r..
##### DEBUG DECIMAL
            123    1   64  192    4   30   13    8
             46    0   10  238  106  196   40  126
             13   63   29  106  196  200  126   13
            105  105  150   91  132  114  196    8
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
#### RECORD 7 Ian69 (2006, 8, 0, 24, 10, 22) head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2006, 8, 0, 24, 10, 22))
    0000   0x96 0x0a 0xd8 0x60 0xc6                   ...`.
    body (8)
    hex
    0000   0x30 0x7d 0x0d 0x3f 0x1b 0x60 0xc6 0x10    0}.?.`..
    decimal
             48  125   13   63   27   96  198   16
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 8 Base (2008, 5, 27, 22, 41, 41) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x0d                                  }.
    decimal
            125   13
    datetime ((2008, 5, 27, 22, 41, 41))
    0000   0x69 0x69 0x96 0x5b 0x78                   ii.[x
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 9 hack1 (2013, 0, 4, 12, 10, 13) head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0xc6 0x10 0x7d 0x0d 0x14 0x90 0x00    m..}....
    0008   0x6e 0x17 0x36 0x70 0x00 0x48 0x00 0x00    n.6p.H..
    0010   0x24 0x00 0x94 0x36 0x5c 0x0e 0x48 0x79    $..6\.Hy
    0018   0x04 0x74 0xfb 0x04 0x78 0x0f 0x14 0x70    .t..x..p
    0020   0xc3 0x14 0x01 0x00 0xb4 0x00 0xb4 0x00    ........
    0028   0x24 0x00 0x6d 0xc6 0x50 0x7d              $.m.P}
    decimal
            109  198   16  125   13   20  144    0
            110   23   54  112    0   72    0    0
             36    0  148   54   92   14   72  121
              4  116  251    4  120   15   20  112
            195   20    1    0  180    0  180    0
             36    0  109  198   80  125
    datetime ((2013, 0, 4, 12, 10, 13))
    0000   0x0d 0x0a 0x4c 0x44 0xcd                   ..LD.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 10 TempBasal (2013, 0, 4, 9, 63, 13) head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 3.125}
```
    op hex (2)
    0000   0x33 0x7d                                  3}
    decimal
             51  125
    datetime ((2013, 0, 4, 9, 63, 13))
    0000   0x0d 0x3f 0x09 0x44 0xcd                   .?.D.
    body (1)
    hex
    0000   0x93                                       .
    decimal
            147
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 11 Base (2010, 5, 27, 22, 41, 41) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x0d                                  }.
    decimal
            125   13
    datetime ((2010, 5, 27, 22, 41, 41))
    0000   0x69 0x69 0x96 0x5b 0x2a                   ii.[*
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 12 Base (2000, 1, 28, 13, 61, 19) head[2], body[0] op[0x44]

    op hex (2)
    0000   0x44 0xd5                                  D.
    decimal
             68  213
    datetime ((2000, 1, 28, 13, 61, 19))
    0000   0x13 0x7d 0x0d 0x1c 0x90                   .}...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 13 Base (2004, 0, 0, 12, 54, 23) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6e                                  .n
    decimal
              0  110
    datetime ((2004, 0, 0, 12, 54, 23))
    0000   0x17 0x36 0xec 0x00 0x64                   .6..d
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 14 Base (2012, 0, 22, 16, 0, 24) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0x00                                  ..
    decimal
            248    0
    datetime ((2012, 0, 22, 16, 0, 24))
    0000   0x18 0x00 0x50 0x36 0x5c                   ..P6\
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 15 Base (2004, 12, 28, 8, 4, 4) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0xb4                                  ..
    decimal
             14  180
    datetime ((2004, 12, 28, 8, 4, 4))
    0000   0xc4 0x04 0x48 0x3c 0x14                   ..H<.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 16 Base (2009, 1, 20, 18, 56, 20) head[2], body[0] op[0x74]

    op hex (2)
    0000   0x74 0xbe                                  t.
    decimal
            116  190
    datetime ((2009, 1, 20, 18, 56, 20))
    0000   0x14 0x78 0xd2 0x14 0x69                   .x..i
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 17 Base (2005, 13, 13, 29, 51, 21) head[2], body[0] op[0xd1]

    op hex (2)
    0000   0xd1 0x44                                  .D
    decimal
            209   68
    datetime ((2005, 13, 13, 29, 51, 21))
    0000   0xd5 0x73 0x1d 0x0d 0x15                   .s...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 18 PumpSuspend 2000-01-16T00:16:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2000-01-16T00:16:00)
    0000   0x00 0x50 0x00 0x50 0x00                   .P.P.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 19 NewTimeSet 2013-07-29T19:21:04 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-07-29T19:21:04)
    0000   0x44 0xd5 0x53 0x7d 0x0d                   D.S}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2013-07-29T19:44:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-29T19:44:52)
    0000   0x74 0xec 0x13 0x7d 0x0d                   t..}.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 2.0, 'curve': 4},
 {'age': 219, 'amount': 4.5, 'curve': 4},
 {'age': 83, 'amount': 1.8, 'curve': 20},
 {'age': 213, 'amount': 2.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x1d 0x04 0xb4 0xdb 0x04    \.P.....
    0008   0x48 0x53 0x14 0x74 0xd5 0x14              HS.t..
    decimal
             92   14   80   29    4  180  219    4
             72   83   20  116  213   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-07-29T19:44:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x5c 0x00    ..L.L.\.
    decimal
              1    0   76    0   76    0   92    0
    datetime (2013-07-29T19:44:52)
    0000   0x74 0xec 0x53 0x7d 0x0d                   t.S}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2013-07-29T20:39:45 head[2], body[15] op[0x5b]
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
    datetime (2013-07-29T20:39:45)
    0000   0x6d 0xe7 0x14 0x7d 0x0d                   m..}.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 1.7, 'curve': 4},
 {'age': 64, 'amount': 0.2, 'curve': 4},
 {'age': 84, 'amount': 2.0, 'curve': 4},
 {'age': 18, 'amount': 4.5, 'curve': 20},
 {'age': 138, 'amount': 1.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x44 0x36 0x04 0x08 0x40 0x04    \.D6..@.
    0008   0x50 0x54 0x04 0xb4 0x12 0x14 0x48 0x8a    PT....H.
    0010   0x14                                       .
    decimal
             92   17   68   54    4    8   64    4
             80   84    4  180   18   20   72  138
             20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-07-29T20:39:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x78 0x00    ..X.X.x.
    decimal
              1    0   88    0   88    0  120    0
    datetime (2013-07-29T20:39:45)
    0000   0x6d 0xe7 0x54 0x7d 0x0d                   m.T}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2013-07-29T22:27:35 head[2], body[15] op[0x5b]
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
    datetime (2013-07-29T22:27:35)
    0000   0x63 0xdb 0x16 0x7d 0x0d                   c..}.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x36         d....d6
    decimal
             28  144    0  110   23   54    0    0
            100    0    0    0    0  100   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 2.2, 'curve': 4},
 {'age': 162, 'amount': 1.7, 'curve': 4},
 {'age': 172, 'amount': 0.2, 'curve': 4},
 {'age': 192, 'amount': 2.0, 'curve': 4},
 {'age': 126, 'amount': 4.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x58 0x70 0x04 0x44 0xa2 0x04    \.Xp.D..
    0008   0x08 0xac 0x04 0x50 0xc0 0x04 0xb4 0x7e    ...P...~
    0010   0x14                                       .
    decimal
             92   17   88  112    4   68  162    4
              8  172    4   80  192    4  180  126
             20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-07-29T22:27:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x4c 0x00    ..d.d.L.
    decimal
              1    0  100    0  100    0   76    0
    datetime (2013-07-29T22:27:35)
    0000   0x63 0xdb 0x56 0x7d 0x0d                   c.V}.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 CalBGForPH 2013-07-29T23:57:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-07-29T23:57:16)
    0000   0x50 0xf9 0x37 0x7d 0x0d                   P.7}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 Base (2013, 7, 29, 23, 57, 16) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime ((2013, 7, 29, 23, 57, 16))
    0000   0x50 0xf9 0x57 0x7d 0x0d                   P.W}.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 Ian69 (2000, 9, 0, 0, 59, 22) head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2000, 9, 0, 0, 59, 22))
    0000   0x96 0x7b 0x00 0x40 0xc0                   .{.@.
    body (8)
    hex
    0000   0x00 0x1e 0x0d 0x00 0x20 0x00 0x07 0x00    .... ...
    decimal
              0   30   13    0   32    0    7    0
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 32 Base (2000, 13, 0, 13, 61, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x07                                  ..
    decimal
              0    7
    datetime ((2000, 13, 0, 13, 61, 13))
    0000   0xcd 0x7d 0x8d 0x00 0x00                   .}...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 33 Base (2013, 6, 16, 6, 13, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6e                                  .n
    decimal
              0  110
    datetime ((2013, 6, 16, 6, 13, 61))
    0000   0x7d 0x8d 0x06 0x10 0x8d                   }....
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 Base (2013, 0, 7, 0, 0, 8) head[2], body[0] op[0x49]

    op hex (2)
    0000   0x49 0x18                                  I.
    decimal
             73   24
    datetime ((2013, 0, 7, 0, 0, 8))
    0000   0x08 0x00 0x00 0x07 0xcd                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 35 Prime (2008, 0, 2, 26, 0, 55) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.8, 'fixed': 4.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x89 0x2d 0x04 0x44                   ..-.D
    decimal
              3  137   45    4   68
    datetime ((2008, 0, 2, 26, 0, 55))
    0000   0x37 0x00 0xfa 0x02 0x98                   7....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 36 Base (2007, 2, 0, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2c                                  .,
    decimal
              0   44
    datetime ((2007, 2, 0, 0, 0, 1))
    0000   0x01 0x80 0x00 0x00 0x07                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 37 Bolus (2003, 0, 0, 0, 0, 0) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x03 0x00 0x00 0x00 0x00 0x00 0x00    ........
    decimal
              1    3    0    0    0    0    0    0
    datetime ((2003, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x63                   ....c
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 38 ChangeUtility (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x00                                  c.
    decimal
             99    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-32.data: 39 records`
