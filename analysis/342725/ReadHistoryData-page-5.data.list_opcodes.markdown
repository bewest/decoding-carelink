## START logs/ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x4f 0xe9                                  O.
##### DEBUG DECIMAL
             79  233
#### RECORD 0 BolusWizard 2014-03-09T18:41:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 166,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 5.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa6                                  [.
    decimal
             91  166
    datetime (2014-03-09T18:41:05)
    0000   0x05 0xe9 0x12 0x09 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x34 0x00    .P.x2P4.
    0008   0x00 0x00 0x00 0x38 0x00 0x00 0x64         ...8..d
    decimal
              0   80    0  120   50   80   52    0
              0    0    0   56    0    0  100
    HOUR BITS: [1, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 2.5, 'curve': 128},
 {'age': 79, 'amount': 1.8, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0x45 0x80 0x48 0x4f 0x80    \.dE.HO.
    decimal
             92    8  100   69  128   72   79  128
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2014-03-09T18:41:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x38 0x00    ......8.
    decimal
              1    0   16    0   16    0   56    0
    datetime (2014-03-09T18:41:05)
    0000   0x05 0xe9 0x52 0x09 0x0e                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 BolusWizard 2014-03-09T18:46:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 166,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 6.4,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0xa6                                  [.
    decimal
             91  166
    datetime (2014-03-09T18:46:18)
    0000   0x12 0xee 0x12 0x69 0x0e                   ...i.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x78 0x32 0x50 0x34 0x00    #P.x2P4.
    0008   0x74 0x00 0x00 0x40 0x00 0x74 0x64         t..@.td
    decimal
             35   80    0  120   50   80   52    0
            116    0    0   64    0  116  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 0.4, 'curve': 128},
 {'age': 74, 'amount': 2.5, 'curve': 128},
 {'age': 84, 'amount': 1.8, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0x0e 0x80 0x64 0x4a 0x80    \....dJ.
    0008   0x48 0x54 0x80                             HT.
    decimal
             92   11   16   14  128  100   74  128
             72   84  128
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2014-03-09T18:46:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x40 0x00    ..t.t.@.
    decimal
              1    0  116    0  116    0   64    0
    datetime (2014-03-09T18:46:18)
    0000   0x12 0xee 0x52 0x69 0x0e                   ..Ri.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2014-03-09T19:10:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
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
    datetime (2014-03-09T19:10:07)
    0000   0x07 0xca 0x13 0x69 0x0e                   ...i.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x64         P....Pd
    decimal
             22   80    0  110   50   80    0    0
             80    0    0    0    0   80  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 2.9, 'curve': 128},
 {'age': 38, 'amount': 0.4, 'curve': 128},
 {'age': 98, 'amount': 2.5, 'curve': 128},
 {'age': 108, 'amount': 1.8, 'curve': 128}]
```
    op hex (14)
    0000   0x5c 0x0e 0x74 0x1c 0x80 0x10 0x26 0x80    \.t...&.
    0008   0x64 0x62 0x80 0x48 0x6c 0x80              db.Hl.
    decimal
             92   14  116   28  128   16   38  128
            100   98  128   72  108  128
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2014-03-09T19:10:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x84 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  132    0
    datetime (2014-03-09T19:10:07)
    0000   0x07 0xca 0x53 0x69 0x0e                   ..Si.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 NoDelivery 2014-03-09T19:14:26 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x3b 0x01 0x08                        .;..
    decimal
              6   59    1    8
    datetime (2014-03-09T19:14:26)
    0000   0x1a 0xce 0x73 0xc9 0x0e                   ..s..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 1, 0]
#### RECORD 10 ClearAlarm 2014-03-09T19:19:09 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x3b                                  .;
    decimal
             12   59
    datetime (2014-03-09T19:19:09)
    0000   0x09 0xd3 0x13 0x09 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 BasalProfileStart 2014-03-09T19:19:09 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-09T19:19:09)
    0000   0x09 0xd3 0x13 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2014-03-09T20:52:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 271}
```
    op hex (2)
    0000   0x0a 0x0f                                  ..
    decimal
             10   15
    datetime (2014-03-09T20:52:28)
    0000   0x1c 0xf4 0x34 0x09 0x8e                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 13 BolusWizard 2014-03-09T20:52:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 271,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 13.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0f                                  [.
    decimal
             91   15
    datetime (2014-03-09T20:52:30)
    0000   0x1e 0xf4 0x14 0x69 0x0e                   ...i.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x6e 0x32 0x50 0x88 0x00    .Q.n2P..
    0008   0x00 0x00 0x00 0x08 0x00 0x80 0x64         ......d
    decimal
              0   81    0  110   50   80  136    0
              0    0    0    8    0  128  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 110, 'amount': 2.0, 'curve': 128},
 {'age': 130, 'amount': 2.9, 'curve': 128},
 {'age': 140, 'amount': 0.4, 'curve': 128},
 {'age': 200, 'amount': 2.5, 'curve': 128},
 {'age': 210, 'amount': 1.8, 'curve': 128}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x6e 0x80 0x74 0x82 0x80    \.Pn.t..
    0008   0x10 0x8c 0x80 0x64 0xc8 0x80 0x48 0xd2    ...d..H.
    0010   0x80                                       .
    decimal
             92   17   80  110  128  116  130  128
             16  140  128  100  200  128   72  210
            128
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2014-03-09T20:52:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x08 0x00    ........
    decimal
              1    0  128    0  128    0    8    0
    datetime (2014-03-09T20:52:30)
    0000   0x1e 0xf4 0x54 0x69 0x0e                   ..Ti.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 CalBGForPH 2014-03-09T22:22:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 241}
```
    op hex (2)
    0000   0x0a 0xf1                                  ..
    decimal
             10  241
    datetime (2014-03-09T22:22:44)
    0000   0x2c 0xd6 0x36 0x09 0x0e                   ,.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 BolusWizard 2014-03-09T22:22:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 241,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 11.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf1                                  [.
    decimal
             91  241
    datetime (2014-03-09T22:22:51)
    0000   0x33 0xd6 0x16 0x69 0x0e                   3..i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x32 0x50 0x70 0x00    .P.n2Pp.
    0008   0x00 0x00 0x00 0x18 0x00 0x58 0x64         .....Xd
    decimal
              0   80    0  110   50   80  112    0
              0    0    0   24    0   88  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 90, 'amount': 3.2, 'curve': 128},
 {'age': 200, 'amount': 2.0, 'curve': 128},
 {'age': 220, 'amount': 2.9, 'curve': 128},
 {'age': 230, 'amount': 0.4, 'curve': 128},
 {'age': 34, 'amount': 2.5, 'curve': 144},
 {'age': 44, 'amount': 1.8, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0x80 0x5a 0x80 0x50 0xc8 0x80    \..Z.P..
    0008   0x74 0xdc 0x80 0x10 0xe6 0x80 0x64 0x22    t.....d"
    0010   0x90 0x48 0x2c 0x90                        .H,.
    decimal
             92   20  128   90  128   80  200  128
            116  220  128   16  230  128  100   34
            144   72   44  144
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2014-03-09T22:22:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x18 0x00    ........
    decimal
              1    0  168    0  168    0   24    0
    datetime (2014-03-09T22:22:51)
    0000   0x33 0xd6 0x56 0x69 0x0e                   3.Vi.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 BasalProfileStart 2014-03-09T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-09T22:30:00)
    0000   0x00 0xde 0x16 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 21 BasalProfileStart 2014-03-09T23:19:20 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-09T23:19:20)
    0000   0x14 0xd3 0x17 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 22 Prime 2014-03-09T23:19:10 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2014-03-09T23:19:10)
    0000   0x0a 0xd3 0x17 0x09 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 BasalProfileStart 2014-03-10T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-10T00:00:00)
    0000   0x00 0xc0 0x00 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 24 MResultTotals 2014-03-10T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x12                   .....
    decimal
              7    0    0    7   18
    datetime (2014-03-10T00:00:00)
    0000   0x29 0x8e                                  ).
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 25 Sara6E 2014-03-10T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-10T00:00:00)
    0000   0x29 0x8e                                  ).
    body (49)
    hex
    0000   0x05 0x10 0xc6 0x47 0x26 0x09 0x00 0x00    ...G&...
    0008   0x07 0x12 0x01 0xb6 0x18 0x05 0x5c 0x4c    ......\L
    0010   0x00 0x9f 0x01 0xb8 0x03 0x00 0x00 0xa4    ........
    0018   0x00 0x00 0x06 0x07 0x01 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xa1    ........
    0028   0x0f 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  198   71   38    9    0    0
              7   18    1  182   24    5   92   76
              0  159    1  184    3    0    0  164
              0    0    6    7    1    0    4    0
              0    0    0    0    0    0    0  161
             15    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 26 BasalProfileStart 2014-03-10T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-10T02:00:00)
    0000   0x00 0xc0 0x02 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 27 BasalProfileStart 2014-03-10T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-10T04:00:00)
    0000   0x00 0xc0 0x04 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 28 BasalProfileStart 2014-03-10T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-10T06:00:00)
    0000   0x00 0xc0 0x06 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 29 CalBGForPH 2014-03-10T07:08:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2014-03-10T07:08:33)
    0000   0x21 0xc8 0x27 0x6a 0x0e                   !.'j.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 Ian3F 2014-03-10T07:08:33 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-03-10T07:08:33)
    0000   0x21 0xc8 0x87 0x6a 0x0e                   !..j.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2014-03-10T07:08:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 140,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8c                                  [.
    decimal
             91  140
    datetime (2014-03-10T07:08:44)
    0000   0x2c 0xc8 0x07 0x0a 0x0e                   ,....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x28 0x00    .P.n(P(.
    0008   0x00 0x00 0x00 0x00 0x00 0x28 0x64         .....(d
    decimal
              0   80    0  110   40   80   40    0
              0    0    0    0    0   40  100
    HOUR BITS: [1, 1, 0]
#### RECORD 32 Bolus 2014-03-10T07:08:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2014-03-10T07:08:44)
    0000   0x2c 0xc8 0x47 0x0a 0x0e                   ,.G..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 PumpSuspend 2014-03-10T07:52:25 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-10T07:52:25)
    0000   0x19 0xf4 0x07 0x0a 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 BasalProfileStart 2014-03-10T08:42:27 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-10T08:42:27)
    0000   0x1b 0xea 0x08 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 1]
#### RECORD 35 PumpResume 2014-03-10T08:42:27 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-10T08:42:27)
    0000   0x1b 0xea 0x08 0x0a 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 CalBGForPH 2014-03-10T10:07:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2014-03-10T10:07:03)
    0000   0x03 0xc7 0x2a 0x6a 0x0e                   ..*j.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 Ian3F 2014-03-10T10:07:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-03-10T10:07:03)
    0000   0x03 0xc7 0x2a 0x6a 0x0e                   ..*j.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2014-03-10T10:07:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 169,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 6.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0xa9                                  [.
    decimal
             91  169
    datetime (2014-03-10T10:07:38)
    0000   0x26 0xc7 0x0a 0x0a 0x0e                   &....
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x6e 0x28 0x50 0x44 0x00    .P.n(PD.
    0008   0x24 0x00 0x00 0x00 0x00 0x68 0x64         $....hd
    decimal
             10   80    0  110   40   80   68    0
             36    0    0    0    0  104  100
    HOUR BITS: [1, 1, 0]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 185, 'amount': 1.0, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0xb9 0x80                   \.(..
    decimal
             92    5   40  185  128
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2014-03-10T10:07:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x00 0x00    ..h.h...
    decimal
              1    0  104    0  104    0    0    0
    datetime (2014-03-10T10:07:38)
    0000   0x26 0xc7 0x4a 0x0a 0x0e                   &.J..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 41 ChangeTimeDisplay 2014-03-10T10:14:15 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2014-03-10T10:14:15)
    0000   0x0f 0xce 0x0a 0x0a 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 42 ChangeTime 2014-03-10T10:14:19 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2014-03-10T10:14:19)
    0000   0x13 0xce 0x0a 0x0a 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 43 NewTimeSet 2014-03-10T09:14:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2014-03-10T09:14:00)
    0000   0x00 0xce 0x09 0x0a 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 44 BolusWizard 2014-03-10T09:38:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 70,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 252}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-10T09:38:01)
    0000   0x01 0xe6 0x09 0x6a 0x0e                   ...j.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    FP.n(P..
    0008   0xfc 0x00 0x00 0x00 0x00 0xfc 0x64         ......d
    decimal
             70   80    0  110   40   80    0    0
            252    0    0    0    0  252  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 2.6, 'curve': 128},
 {'age': 216, 'amount': 1.0, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x68 0x24 0x80 0x28 0xd8 0x80    \.h$.(..
    decimal
             92    8  104   36  128   40  216  128
    datetime (unknown)

    body (0)

#### RECORD 46 PumpSuspend 2014-03-10T09:40:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-10T09:40:56)
    0000   0x38 0xe8 0x09 0x0a 0x0e                   8....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 47 Bolus 2014-03-10T09:38:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 25.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xfc 0x00 0xac 0x00 0x50 0x00    ......P.
    decimal
              1    0  252    0  172    0   80    0
    datetime (2014-03-10T09:38:01)
    0000   0x01 0xe6 0x49 0x6a 0x0e                   ..Ij.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BasalProfileStart 2014-03-10T09:40:59 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-10T09:40:59)
    0000   0x3b 0xe8 0x09 0x0a 0x0e                   ;....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 1]
#### RECORD 49 PumpResume 2014-03-10T09:40:59 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-10T09:40:59)
    0000   0x3b 0xe8 0x09 0x0a 0x0e                   ;....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 50 BasalProfileStart 2014-03-10T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-10T10:30:00)
    0000   0x00 0xde 0x0a 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 51 CalBGForPH 2014-03-10T11:30:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 290}
```
    op hex (2)
    0000   0x0a 0x22                                  ."
    decimal
             10   34
    datetime (2014-03-10T11:30:12)
    0000   0x0c 0xde 0x2b 0x0a 0x8e                   ..+..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 52 BolusWizard 2014-03-10T11:30:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 290,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 15.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x22                                  ["
    decimal
             91   34
    datetime (2014-03-10T11:30:15)
    0000   0x0f 0xde 0x0b 0x6a 0x0e                   ...j.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x32 0x50 0x98 0x00    .Q.x2P..
    0008   0x00 0x00 0x00 0x0c 0x00 0x8c 0x64         ......d
    decimal
              0   81    0  120   50   80  152    0
              0    0    0   12    0  140  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 118, 'amount': 4.3, 'curve': 128},
 {'age': 148, 'amount': 2.6, 'curve': 128},
 {'age': 72, 'amount': 1.0, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0xac 0x76 0x80 0x68 0x94 0x80    \..v.h..
    0008   0x28 0x48 0x90                             (H.
    decimal
             92   11  172  118  128  104  148  128
             40   72  144
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2014-03-10T11:30:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x0c 0x00    ........
    decimal
              1    0  140    0  140    0   12    0
    datetime (2014-03-10T11:30:15)
    0000   0x0f 0xde 0x4b 0x6a 0x0e                   ..Kj.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 CalBGForPH 2014-03-10T13:32:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 272}
```
    op hex (2)
    0000   0x0a 0x10                                  ..
    decimal
             10   16
    datetime (2014-03-10T13:32:04)
    0000   0x04 0xe0 0x2d 0x0a 0x8e                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 56 BolusWizard 2014-03-10T13:32:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 272,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 13.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x10                                  [.
    decimal
             91   16
    datetime (2014-03-10T13:32:12)
    0000   0x0c 0xe0 0x0d 0x6a 0x0e                   ...j.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x32 0x50 0x88 0x00    .Q.x2P..
    0008   0x00 0x00 0x00 0x04 0x00 0x84 0x64         ......d
    decimal
              0   81    0  120   50   80  136    0
              0    0    0    4    0  132  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 120, 'amount': 0.85, 'curve': 128},
 {'age': 130, 'amount': 2.65, 'curve': 128},
 {'age': 240, 'amount': 4.3, 'curve': 128},
 {'age': 14, 'amount': 2.6, 'curve': 144},
 {'age': 194, 'amount': 1.0, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x22 0x78 0x80 0x6a 0x82 0x80    \."x.j..
    0008   0xac 0xf0 0x80 0x68 0x0e 0x90 0x28 0xc2    ...h..(.
    0010   0x90                                       .
    decimal
             92   17   34  120  128  106  130  128
            172  240  128  104   14  144   40  194
            144
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2014-03-10T13:32:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x04 0x00    ..T.T...
    decimal
              1    0   84    0   84    0    4    0
    datetime (2014-03-10T13:32:12)
    0000   0x0c 0xe0 0x4d 0x6a 0x0e                   ..Mj.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 CalBGForPH 2014-03-10T14:37:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2014-03-10T14:37:42)
    0000   0x2a 0xe5 0x2e 0x0a 0x8e                   *....
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 60 BolusWizard 2014-03-10T14:37:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 276,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 14.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x14                                  [.
    decimal
             91   20
    datetime (2014-03-10T14:37:47)
    0000   0x2f 0xe5 0x0e 0x6a 0x0e                   /..j.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x32 0x50 0x8c 0x00    .Q.x2P..
    0008   0x00 0x00 0x00 0x24 0x00 0x68 0x64         ...$.hd
    decimal
              0   81    0  120   50   80  140    0
              0    0    0   36    0  104  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 2.1, 'curve': 128},
 {'age': 185, 'amount': 0.85, 'curve': 128},
 {'age': 195, 'amount': 2.65, 'curve': 128},
 {'age': 49, 'amount': 4.3, 'curve': 144},
 {'age': 79, 'amount': 2.6, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x54 0x41 0x80 0x22 0xb9 0x80    \.TA."..
    0008   0x6a 0xc3 0x80 0xac 0x31 0x90 0x68 0x4f    j...1.hO
    0010   0x90                                       .
    decimal
             92   17   84   65  128   34  185  128
            106  195  128  172   49  144  104   79
            144
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2014-03-10T14:37:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x24 0x00    ..P.P.$.
    decimal
              1    0   80    0   80    0   36    0
    datetime (2014-03-10T14:37:47)
    0000   0x2f 0xe5 0x4e 0x6a 0x0e                   /.Nj.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 PumpSuspend 2014-03-10T17:07:54 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-10T17:07:54)
    0000   0x36 0xc7 0x11 0x0a 0x0e                   6....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 CalBGForPH 2014-03-10T19:08:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2014-03-10T19:08:48)
    0000   0x30 0xc8 0x33 0x6a 0x0e                   0.3j.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 65 Ian3F 2014-03-10T19:08:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-03-10T19:08:48)
    0000   0x30 0xc8 0x53 0x6a 0x0e                   0.Sj.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 BasalProfileStart 2014-03-10T19:50:06 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-10T19:50:06)
    0000   0x06 0xf2 0x13 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 67 PumpResume 2014-03-10T19:50:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-10T19:50:06)
    0000   0x06 0xf2 0x13 0x0a 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 Bolus 2014-03-10T19:50:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x0c 0x00 0x0c 0x00 0x00 0x00    ........
    decimal
              1    0   12    0   12    0    0    0
    datetime (2014-03-10T19:50:14)
    0000   0x0e 0xf2 0x53 0x0a 0x0e                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 PumpSuspend 2014-03-10T19:52:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-10T19:52:01)
    0000   0x01 0xf4 0x13 0x0a 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 70 BasalProfileStart 2014-03-10T21:12:23 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-10T21:12:23)
    0000   0x17 0xcc 0x15 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 71 PumpResume 2014-03-10T21:12:23 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-10T21:12:23)
    0000   0x17 0xcc 0x15 0x0a 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 CalBGForPH 2014-03-10T21:18:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2014-03-10T21:18:10)
    0000   0x0a 0xd2 0x35 0x0a 0x0e                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 73 BolusWizard 2014-03-10T21:18:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 129,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x81                                  [.
    decimal
             91  129
    datetime (2014-03-10T21:18:12)
    0000   0x0c 0xd2 0x15 0x0a 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x32 0x50 0x14 0x00    .P.n2P..
    0008   0x00 0x00 0x00 0x04 0x00 0x10 0x64         ......d
    decimal
              0   80    0  110   50   80   20    0
              0    0    0    4    0   16  100
    HOUR BITS: [1, 1, 0]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 0.3, 'curve': 128},
 {'age': 150, 'amount': 2.0, 'curve': 144},
 {'age': 210, 'amount': 2.1, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x60 0x80 0x50 0x96 0x90    \..`.P..
    0008   0x54 0xd2 0x90                             T..
    decimal
             92   11   12   96  128   80  150  144
             84  210  144
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2014-03-10T21:18:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x04 0x00    ........
    decimal
              1    0   16    0   16    0    4    0
    datetime (2014-03-10T21:18:12)
    0000   0x0c 0xd2 0x55 0x0a 0x0e                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 BolusWizard 2014-03-10T21:22:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 129,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 2.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x81                                  [.
    decimal
             91  129
    datetime (2014-03-10T21:22:16)
    0000   0x10 0xd6 0x15 0x6a 0x0e                   ...j.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x6e 0x32 0x50 0x14 0x00    (P.n2P..
    0008   0x90 0x00 0x00 0x14 0x00 0x90 0x64         ......d
    decimal
             40   80    0  110   50   80   20    0
            144    0    0   20    0  144  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 0.4, 'curve': 128},
 {'age': 100, 'amount': 0.3, 'curve': 128},
 {'age': 154, 'amount': 2.0, 'curve': 144},
 {'age': 214, 'amount': 2.1, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x10 0x0a 0x80 0x0c 0x64 0x80    \.....d.
    0008   0x50 0x9a 0x90 0x54 0xd6 0x90              P..T..
    decimal
             92   14   16   10  128   12  100  128
             80  154  144   84  214  144
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2014-03-10T21:22:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x14 0x00    ........
    decimal
              1    0  144    0  144    0   20    0
    datetime (2014-03-10T21:22:16)
    0000   0x10 0xd6 0x55 0x6a 0x0e                   ..Uj.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 79 BasalProfileStart 2014-03-10T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-10T22:30:00)
    0000   0x00 0xde 0x16 0x0a 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 80 BasalProfileStart 2014-03-11T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-11T00:00:00)
    0000   0x00 0xc0 0x00 0x0b 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-5.data: 81 records`
