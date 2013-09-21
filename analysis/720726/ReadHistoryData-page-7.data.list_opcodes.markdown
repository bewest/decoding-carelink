## START analysis/ianj/raw/ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 983, found 39 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x7c 0xba                                  |.
##### DEBUG DECIMAL
            124  186
#### RECORD 0 Base (2013, 9, 3, 18, 28, 51) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x01                                  <.
    decimal
             60    1
    datetime ((2013, 9, 3, 18, 28, 51))
    0000   0xb3 0x5c 0x12 0x03 0x0d                   .\...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 1 Base (2006, 1, 9, 9, 51, 0) head[2], body[0] op[0x3d]

    op hex (2)
    0000   0x3d 0x74                                  =t
    decimal
             61  116
    datetime ((2006, 1, 9, 9, 51, 0))
    0000   0x00 0x73 0x69 0x69 0x96                   .sii.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 2 Base (2000, 9, 0, 0, 48, 16) head[2], body[0] op[0x3e]

    op hex (2)
    0000   0x3e 0x72                                  >r
    decimal
             62  114
    datetime ((2000, 9, 0, 0, 48, 16))
    0000   0x90 0x70 0x00 0x00 0x00                   .p...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-09-03T18:28:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-09-03T18:28:52)
    0000   0xb4 0x5c 0x32 0x63 0x0d                   .\2c.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 Ian3F 2013-09-03T18:28:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2013-09-03T18:28:52)
    0000   0xb4 0x5c 0x92 0x63 0x0d                   .\.c.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 Base (2013, 9, 3, 18, 29, 1) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x01                                  <.
    decimal
             60    1
    datetime ((2013, 9, 3, 18, 29, 1))
    0000   0x81 0x5d 0x12 0x03 0x0d                   .]...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 Base (2000, 1, 0, 0, 51, 0) head[2], body[0] op[0x3d]

    op hex (2)
    0000   0x3d 0x74                                  =t
    decimal
             61  116
    datetime ((2000, 1, 0, 0, 51, 0))
    0000   0x00 0x73 0x00 0x00 0x00                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 Base (2000, 9, 0, 0, 48, 16) head[2], body[0] op[0x3e]

    op hex (2)
    0000   0x3e 0x72                                  >r
    decimal
             62  114
    datetime ((2000, 9, 0, 0, 48, 16))
    0000   0x90 0x70 0x00 0x00 0x00                   .p...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 8 Base (2013, 9, 3, 18, 29, 5) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x01                                  <.
    decimal
             60    1
    datetime ((2013, 9, 3, 18, 29, 5))
    0000   0x85 0x5d 0x12 0x03 0x0d                   .]...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 9 Base (2000, 1, 0, 0, 51, 0) head[2], body[0] op[0x3d]

    op hex (2)
    0000   0x3d 0x74                                  =t
    decimal
             61  116
    datetime ((2000, 1, 0, 0, 51, 0))
    0000   0x00 0x73 0x00 0x00 0x00                   .s...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x3e]

    op hex (2)
    0000   0x3e 0x00                                  >.
    decimal
             62    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 11 BolusWizard 2013-09-03T18:29:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 56,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 14.8,
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
    0000   0x5b 0x38                                  [8
    decimal
             91   56
    datetime (2013-09-03T18:29:31)
    0000   0x9f 0x5d 0x12 0x63 0x0d                   .].c.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x94 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0  148    0   76   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 1.9, 'curve': 4},
 {'age': 88, 'amount': 1.8, 'curve': 4},
 {'age': 168, 'amount': 3.3, 'curve': 4},
 {'age': 178, 'amount': 0.1, 'curve': 4},
 {'age': 22, 'amount': 0.675, 'curve': 20},
 {'age': 32, 'amount': 0.125, 'curve': 20},
 {'age': 62, 'amount': 0.8, 'curve': 20},
 {'age': 122, 'amount': 2.9, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x4c 0x26 0x04 0x48 0x58 0x04    \.L&.HX.
    0008   0x84 0xa8 0x04 0x04 0xb2 0x04 0x1b 0x16    ........
    0010   0x14 0x05 0x20 0x14 0x20 0x3e 0x14 0x74    .. . >.t
    0018   0x7a 0x14                                  z.
    decimal
             92   26   76   38    4   72   88    4
            132  168    4    4  178    4   27   22
             20    5   32   20   32   62   20  116
            122   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-09-03T18:29:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x94 0x00    ..L.L...
    decimal
              1    0   76    0   76    0  148    0
    datetime (2013-09-03T18:29:31)
    0000   0x9f 0x5d 0x52 0x63 0x0d                   .]Rc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 BolusWizard 2013-09-03T23:05:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 42,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 152}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-03T23:05:35)
    0000   0xa3 0x45 0x17 0x63 0x0d                   .E.c.
    body (15)
    hex
    0000   0x2a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    *..n.6..
    0008   0x98 0x00 0x00 0x00 0x00 0x98 0x36         ......6
    decimal
             42  144    0  110   23   54    0    0
            152    0    0    0    0  152   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 1.9, 'curve': 20},
 {'age': 58, 'amount': 1.9, 'curve': 20},
 {'age': 108, 'amount': 1.8, 'curve': 20},
 {'age': 188, 'amount': 3.3, 'curve': 20},
 {'age': 198, 'amount': 0.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x4c 0x1c 0x14 0x4c 0x3a 0x14    \.L..L:.
    0008   0x48 0x6c 0x14 0x84 0xbc 0x14 0x04 0xc6    Hl......
    0010   0x14                                       .
    decimal
             92   17   76   28   20   76   58   20
             72  108   20  132  188   20    4  198
             20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-09-03T23:05:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 17.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0x00 0x00    ........
    decimal
              1    0  172    0  172    0    0    0
    datetime (2013-09-03T23:05:35)
    0000   0xa3 0x45 0x57 0x63 0x0d                   .EWc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2013-09-03T23:09:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-03T23:09:16)
    0000   0x90 0x49 0x17 0x63 0x0d                   .I.c.
    body (15)
    hex
    0000   0x13 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x36         D....D6
    decimal
             19  144    0  110   23   54    0    0
             68    0    0    0    0   68   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 4.3, 'curve': 4},
 {'age': 32, 'amount': 1.9, 'curve': 20},
 {'age': 62, 'amount': 1.9, 'curve': 20},
 {'age': 112, 'amount': 1.8, 'curve': 20},
 {'age': 192, 'amount': 3.3, 'curve': 20},
 {'age': 202, 'amount': 0.1, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0xac 0x08 0x04 0x4c 0x20 0x14    \....L .
    0008   0x4c 0x3e 0x14 0x48 0x70 0x14 0x84 0xc0    L>.Hp...
    0010   0x14 0x04 0xca 0x14                        ....
    decimal
             92   20  172    8    4   76   32   20
             76   62   20   72  112   20  132  192
             20    4  202   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-09-03T23:09:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0xac 0x00    ..D.D...
    decimal
              1    0   68    0   68    0  172    0
    datetime (2013-09-03T23:09:16)
    0000   0x90 0x49 0x57 0x63 0x0d                   .IWc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2013-09-03T23:11:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-03T23:11:20)
    0000   0x94 0x4b 0x17 0x63 0x0d                   .K.c.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 6.0, 'curve': 4},
 {'age': 34, 'amount': 1.9, 'curve': 20},
 {'age': 64, 'amount': 1.9, 'curve': 20},
 {'age': 114, 'amount': 1.8, 'curve': 20},
 {'age': 194, 'amount': 3.3, 'curve': 20},
 {'age': 204, 'amount': 0.1, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0xf0 0x0a 0x04 0x4c 0x22 0x14    \....L".
    0008   0x4c 0x40 0x14 0x48 0x72 0x14 0x84 0xc2    L@.Hr...
    0010   0x14 0x04 0xcc 0x14                        ....
    decimal
             92   20  240   10    4   76   34   20
             76   64   20   72  114   20  132  194
             20    4  204   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-09-03T23:11:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0xf0 0x00    ..0.0...
    decimal
              1    0   48    0   48    0  240    0
    datetime (2013-09-03T23:11:20)
    0000   0x94 0x4b 0x57 0x63 0x0d                   .KWc.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2013-09-03T23:16:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-03T23:16:11)
    0000   0x8b 0x50 0x17 0x63 0x0d                   .P.c.
    body (15)
    hex
    0000   0x0e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x36         0....06
    decimal
             14  144    0  110   23   54    0    0
             48    0    0    0    0   48   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 1.2, 'curve': 4},
 {'age': 15, 'amount': 6.0, 'curve': 4},
 {'age': 39, 'amount': 1.9, 'curve': 20},
 {'age': 69, 'amount': 1.9, 'curve': 20},
 {'age': 119, 'amount': 1.8, 'curve': 20},
 {'age': 199, 'amount': 3.3, 'curve': 20},
 {'age': 209, 'amount': 0.1, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x30 0x05 0x04 0xf0 0x0f 0x04    \.0.....
    0008   0x4c 0x27 0x14 0x4c 0x45 0x14 0x48 0x77    L'.LE.Hw
    0010   0x14 0x84 0xc7 0x14 0x04 0xd1 0x14         .......
    decimal
             92   23   48    5    4  240   15    4
             76   39   20   76   69   20   72  119
             20  132  199   20    4  209   20
    datetime (unknown)

    body (0)

#### RECORD 25 BasalProfileStart 2013-09-04T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-04T00:00:00)
    0000   0x80 0x40 0x00 0x04 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 1, 0]
#### RECORD 26 MResultTotals 2013-09-04T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x5c                   ....\
    decimal
              7    0    0    7   92
    datetime (2013-09-04T00:00:00)
    0000   0x83 0x8d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 27 Sara6E 2013-09-04T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-09-04T00:00:00)
    0000   0x83 0x8d                                  ..
    body (49)
    hex
    0000   0x06 0x00 0xc2 0x64 0x64 0x03 0x00 0x00    ...dd...
    0008   0x07 0x5c 0x03 0x60 0x2e 0x03 0xfc 0x36    .\.`...6
    0010   0x00 0xe8 0x02 0xa8 0x00 0xa8 0x00 0xac    ........
    0018   0x00 0x00 0x09 0x02 0x01 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xc8    ........
    0028   0x1b 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6    0  194  100  100    3    0    0
              7   92    3   96   46    3  252   54
              0  232    2  168    0  168    0  172
              0    0    9    2    1    0    4    0
              0    0    0    0    0    0    0  200
             27    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 28 BasalProfileStart 2013-09-04T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-04T04:00:00)
    0000   0x80 0x40 0x04 0x04 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 29 BolusWizard 2013-09-04T08:45:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-04T08:45:49)
    0000   0xb1 0x6d 0x08 0x64 0x0d                   .m.d.
    body (15)
    hex
    0000   0x1a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x5c 0x00 0x00 0x00 0x00 0x5c 0x36         \....\6
    decimal
             26  144    0  110   23   54    0    0
             92    0    0    0    0   92   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 Ian69 2013-09-04T08:45:49 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-09-04T08:45:49)
    0000   0xb1 0x6d 0x08 0x04 0x0d                   .m...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 1, 1]
#### RECORD 31 Bolus 2013-09-04T08:45:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x00 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    0    0
    datetime (2013-09-04T08:45:49)
    0000   0xb1 0x6d 0x48 0x64 0x0d                   .mHd.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2013-09-04T09:23:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-04T09:23:01)
    0000   0x81 0x57 0x09 0x64 0x0d                   .W.d.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 42, 'amount': 2.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x2a 0x04                   \.\*.
    decimal
             92    5   92   42    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-09-04T09:23:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x54 0x00    ..4.4.T.
    decimal
              1    0   52    0   52    0   84    0
    datetime (2013-09-04T09:23:02)
    0000   0x82 0x57 0x49 0x64 0x0d                   .WId.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 BasalProfileStart 2013-09-04T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-04T09:30:00)
    0000   0x80 0x5e 0x09 0x04 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 36 BolusWizard 2013-09-04T10:41:50 head[2], body[15] op[0x5b]
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
    datetime (2013-09-04T10:41:50)
    0000   0xb2 0x69 0x0a 0x64 0x0d                   .i.d.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 80, 'amount': 1.3, 'curve': 4},
 {'age': 120, 'amount': 2.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x50 0x04 0x5c 0x78 0x04    \.4P.\x.
    decimal
             92    8   52   80    4   92  120    4
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-09-04T10:41:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x50 0x00    ..H.H.P.
    decimal
              1    0   72    0   72    0   80    0
    datetime (2013-09-04T10:41:50)
    0000   0xb2 0x69 0x4a 0x64 0x0d                   .iJd.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 BolusWizard 2013-09-04T11:26:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-04T11:26:48)
    0000   0xb0 0x5a 0x0b 0x64 0x0d                   .Z.d.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 1.8, 'curve': 4},
 {'age': 125, 'amount': 1.3, 'curve': 4},
 {'age': 165, 'amount': 2.3, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x2d 0x04 0x34 0x7d 0x04    \.H-.4}.
    0008   0x5c 0xa5 0x04                             \..
    decimal
             92   11   72   45    4   52  125    4
             92  165    4
    datetime (unknown)

    body (0)

#### RECORD 41 Ian69 2013-09-04T11:26:48 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-04T11:26:48)
    0000   0xb0 0x5a 0x0b 0x04 0x0d                   .Z...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 1, 0]
#### RECORD 42 Bolus 2013-09-04T11:26:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x6c 0x00    ..d.d.l.
    decimal
              1    0  100    0  100    0  108    0
    datetime (2013-09-04T11:26:48)
    0000   0xb0 0x5a 0x4b 0x64 0x0d                   .ZKd.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 43 BasalProfileStart 2013-09-04T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-04T13:00:00)
    0000   0x80 0x40 0x0d 0x04 0x0d                   .@...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 1, 0]
#### RECORD 44 CalBGForPH 2013-09-04T13:04:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-09-04T13:04:45)
    0000   0xad 0x44 0x4d 0x04 0x0d                   .DM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 45 BolusWizard 2013-09-04T13:04:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 124,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 8.4,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 12.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x7c                                  [|
    decimal
             91  124
    datetime (2013-09-04T13:04:51)
    0000   0xb3 0x44 0x0d 0x64 0x0d                   .D.d.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x78 0x00    ...n.6x.
    0008   0x60 0x00 0x00 0x54 0x00 0x84 0x36         `..T..6
    decimal
             27  144    0  110   23   54  120    0
             96    0    0   84    0  132   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 2.5, 'curve': 4},
 {'age': 143, 'amount': 1.8, 'curve': 4},
 {'age': 223, 'amount': 1.3, 'curve': 4},
 {'age': 7, 'amount': 2.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x64 0x67 0x04 0x48 0x8f 0x04    \.dg.H..
    0008   0x34 0xdf 0x04 0x5c 0x07 0x14              4..\..
    decimal
             92   14  100  103    4   72  143    4
             52  223    4   92    7   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-09-04T13:04:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x54 0x00    ......T.
    decimal
              1    0  132    0  132    0   84    0
    datetime (2013-09-04T13:04:51)
    0000   0xb3 0x44 0x4d 0x64 0x0d                   .DMd.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2013-09-04T17:49:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
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
    datetime (2013-09-04T17:49:46)
    0000   0xae 0x71 0x11 0x64 0x0d                   .q.d.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 3.3, 'curve': 20},
 {'age': 132, 'amount': 2.5, 'curve': 20},
 {'age': 172, 'amount': 1.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x84 0x20 0x14 0x64 0x84 0x14    \.. .d..
    0008   0x48 0xac 0x14                             H..
    decimal
             92   11  132   32   20  100  132   20
             72  172   20
    datetime (unknown)

    body (0)

#### RECORD 50 BolusWizard 2013-09-04T17:49:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
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
    datetime (2013-09-04T17:49:50)
    0000   0xb2 0x71 0x11 0x64 0x0d                   .q.d.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 3.3, 'curve': 20},
 {'age': 132, 'amount': 2.5, 'curve': 20},
 {'age': 172, 'amount': 1.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x84 0x20 0x14 0x64 0x84 0x14    \.. .d..
    0008   0x48 0xac 0x14                             H..
    decimal
             92   11  132   32   20  100  132   20
             72  172   20
    datetime (unknown)

    body (0)

#### RECORD 52 Ian69 2013-09-04T17:49:51 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-09-04T17:49:51)
    0000   0xb3 0x71 0x71 0x04 0x0d                   .qq..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 1, 1]
#### RECORD 53 Bolus 2013-09-04T17:49:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x00 0x00    ........
    decimal
              1    0  132    0  132    0    0    0
    datetime (2013-09-04T17:49:50)
    0000   0xb2 0x71 0x51 0x64 0x0d                   .qQd.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 BolusWizard 2013-09-04T18:03:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-09-04T18:03:29)
    0000   0x9d 0x43 0x12 0x64 0x0d                   .C.d.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 1.6, 'curve': 4},
 {'age': 22, 'amount': 1.7, 'curve': 4},
 {'age': 46, 'amount': 3.3, 'curve': 20},
 {'age': 146, 'amount': 2.5, 'curve': 20},
 {'age': 186, 'amount': 1.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x40 0x0c 0x04 0x44 0x16 0x04    \.@..D..
    0008   0x84 0x2e 0x14 0x64 0x92 0x14 0x48 0xba    ...d..H.
    0010   0x14                                       .
    decimal
             92   17   64   12    4   68   22    4
            132   46   20  100  146   20   72  186
             20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-09-04T18:03:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x84 0x00    ..4.4...
    decimal
              1    0   52    0   52    0  132    0
    datetime (2013-09-04T18:03:29)
    0000   0x9d 0x43 0x52 0x64 0x0d                   .CRd.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 57 Base (2013, 9, 4, 22, 7, 33) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x01                                  <.
    decimal
             60    1
    datetime ((2013, 9, 4, 22, 7, 33))
    0000   0xa1 0x47 0x16 0x04 0x0d                   .G...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 58 Base (2000, 1, 16, 18, 51, 0) head[2], body[0] op[0x3d]

    op hex (2)
    0000   0x3d 0x74                                  =t
    decimal
             61  116
    datetime ((2000, 1, 16, 18, 51, 0))
    0000   0x00 0x73 0x72 0x90 0x70                   .sr.p
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 59 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x3e]

    op hex (2)
    0000   0x3e 0x00                                  >.
    decimal
             62    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 60 CalBGForPH 2013-09-04T22:07:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-09-04T22:07:34)
    0000   0xa2 0x47 0x36 0x64 0x0d                   .G6d.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 61 Ian3F 2013-09-04T22:07:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2013-09-04T22:07:34)
    0000   0xa2 0x47 0x56 0x64 0x0d                   .GVd.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 BolusWizard 2013-09-04T22:07:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 8.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-09-04T22:07:41)
    0000   0xa9 0x47 0x16 0x64 0x0d                   .G.d.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x54 0x00    ...n.6T.
    0008   0x00 0x00 0x00 0x00 0x00 0x54 0x36         .....T6
    decimal
              0  144    0  110   23   54   84    0
              0    0    0    0    0   84   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 246, 'amount': 1.3, 'curve': 4},
 {'age': 0, 'amount': 1.6, 'curve': 20},
 {'age': 10, 'amount': 1.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0xf6 0x04 0x40 0x00 0x14    \.4..@..
    0008   0x44 0x0a 0x14                             D..
    decimal
             92   11   52  246    4   64    0   20
             68   10   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-09-04T22:07:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x00 0x00    ..p.p...
    decimal
              1    0  112    0  112    0    0    0
    datetime (2013-09-04T22:07:41)
    0000   0xa9 0x47 0x56 0x64 0x0d                   .GVd.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 65 BolusWizard 2013-09-04T22:24:37 head[2], body[15] op[0x5b]
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
    datetime (2013-09-04T22:24:37)
    0000   0xa5 0x58 0x16 0x64 0x0d                   .X.d.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 2.8, 'curve': 4},
 {'age': 7, 'amount': 1.3, 'curve': 20},
 {'age': 17, 'amount': 1.6, 'curve': 20},
 {'age': 27, 'amount': 1.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x70 0x17 0x04 0x34 0x07 0x14    \.p..4..
    0008   0x40 0x11 0x14 0x44 0x1b 0x14              @..D..
    decimal
             92   14  112   23    4   52    7   20
             64   17   20   68   27   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-09-04T22:24:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x70 0x00    ..@.@.p.
    decimal
              1    0   64    0   64    0  112    0
    datetime (2013-09-04T22:24:37)
    0000   0xa5 0x58 0x56 0x64 0x0d                   .XVd.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 BasalProfileStart 2013-09-05T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-05T00:00:00)
    0000   0x80 0x40 0x00 0x05 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 1, 0]
#### RECORD 69 MResultTotals 2013-09-05T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xb1                   .....
    decimal
              7    0    0    6  177
    datetime (2013-09-05T00:00:00)
    0000   0x84 0x8d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
`end analysis/ianj/raw/ReadHistoryData-page-7.data: 70 records`
