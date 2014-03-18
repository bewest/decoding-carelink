## START logs/ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 979, found 43 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa6 0x9d                                  ..
##### DEBUG DECIMAL
            166  157
#### RECORD 0 Bolus 2014-03-13T14:51:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x04 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    4    0
    datetime (2014-03-13T14:51:18)
    0000   0x12 0xf3 0x4e 0x6d 0x0e                   ..Nm.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 CalBGForPH 2014-03-13T19:07:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 148}
```
    op hex (2)
    0000   0x0a 0x94                                  ..
    decimal
             10  148
    datetime (2014-03-13T19:07:25)
    0000   0x19 0xc7 0x33 0x6d 0x0e                   ..3m.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2014-03-13T19:07:25 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2014-03-13T19:07:25)
    0000   0x19 0xc7 0x93 0x6d 0x0e                   ...m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 TempBasal 2014-03-13T19:08:08 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-13T19:08:08)
    0000   0x08 0xc8 0x13 0x0d 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 4 TempBasalDuration 2014-03-13T19:08:08 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-13T19:08:08)
    0000   0x08 0xc8 0x13 0x0d 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BasalProfileStart 2014-03-13T20:08:08 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-13T20:08:08)
    0000   0x08 0xc8 0x14 0x0d 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2014-03-13T20:10:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2014-03-13T20:10:35)
    0000   0x23 0xca 0x34 0x6d 0x0e                   #.4m.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2014-03-13T20:10:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-03-13T20:10:35)
    0000   0x23 0xca 0x74 0x6d 0x0e                   #.tm.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 PumpSuspend 2014-03-13T20:13:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-13T20:13:21)
    0000   0x15 0xcd 0x14 0x0d 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 BasalProfileStart 2014-03-13T21:47:56 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-13T21:47:56)
    0000   0x38 0xef 0x15 0x0d 0x0e                   8....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 10 PumpResume 2014-03-13T21:47:56 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-13T21:47:56)
    0000   0x38 0xef 0x15 0x0d 0x0e                   8....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 CalBGForPH 2014-03-13T21:48:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2014-03-13T21:48:02)
    0000   0x02 0xf0 0x35 0x0d 0x0e                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 12 BolusWizard 2014-03-13T21:48:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 1,
 'bg': 85,
 'bg_target_high': 1,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 80,
 'carb_ratio': 0,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2014-03-13T21:48:12)
    0000   0x0c 0xf0 0x15 0x0d 0x0e                   .....
    body (15)
    hex
    0000   0x50 0x50 0x00 0x6e 0x32 0x50 0x00 0x01    PP.n2P..
    0008   0x20 0x00 0x00 0x00 0x01 0x20 0x64          .... d
    decimal
             80   80    0  110   50   80    0    1
             32    0    0    0    1   32  100
    HOUR BITS: [1, 1, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 160, 'amount': 0.95, 'curve': 144},
 {'age': 170, 'amount': 1.05, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x26 0xa0 0x90 0x2a 0xaa 0x90    \.&..*..
    decimal
             92    8   38  160  144   42  170  144
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2014-03-13T21:48:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x20 0x01 0x20 0x00 0x00 0x00    .. . ...
    decimal
              1    1   32    1   32    0    0    0
    datetime (2014-03-13T21:48:12)
    0000   0x0c 0xf0 0x55 0x0d 0x0e                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 15 BolusWizard 2014-03-13T21:57:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 85,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 2.4,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 1,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2014-03-13T21:57:03)
    0000   0x03 0xf9 0x15 0x0d 0x0e                   .....
    body (15)
    hex
    0000   0x28 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    (P.n2P..
    0008   0x90 0x00 0x01 0x18 0x00 0x90 0x64         ......d
    decimal
             40   80    0  110   50   80    0    0
            144    0    1   24    0  144  100
    HOUR BITS: [1, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 1.55, 'curve': 128},
 {'age': 15, 'amount': 5.65, 'curve': 128},
 {'age': 169, 'amount': 0.95, 'curve': 144},
 {'age': 179, 'amount': 1.05, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3e 0x05 0x80 0xe2 0x0f 0x80    \.>.....
    0008   0x26 0xa9 0x90 0x2a 0xb3 0x90              &..*..
    decimal
             92   14   62    5  128  226   15  128
             38  169  144   42  179  144
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2014-03-13T21:57:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x01 0x18 0x02    ........
    decimal
              1    0  144    0  144    1   24    2
    datetime (2014-03-13T21:57:03)
    0000   0x03 0xf9 0x75 0x0d 0x0e                   ..u..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 TempBasal 2014-03-13T22:18:32 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 3.0}
```
    op hex (2)
    0000   0x33 0x78                                  3x
    decimal
             51  120
    datetime (2014-03-13T22:18:32)
    0000   0x20 0xd2 0x16 0x0d 0x0e                    ....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 19 TempBasalDuration 2014-03-13T22:18:32 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-13T22:18:32)
    0000   0x20 0xd2 0x16 0x0d 0x0e                    ....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 BasalProfileStart 2014-03-13T23:18:33 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-13T23:18:33)
    0000   0x21 0xd2 0x17 0x0d 0x0e                   !....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 21 BasalProfileStart 2014-03-14T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-14T00:00:00)
    0000   0x00 0xc0 0x00 0x0e 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 22 MResultTotals 2014-03-14T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x63                   ....c
    decimal
              7    0    0    4   99
    datetime (2014-03-14T00:00:00)
    0000   0x2d 0x8e                                  -.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 23 Sara6E 2014-03-14T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-14T00:00:00)
    0000   0x2d 0x8e                                  -.
    body (49)
    hex
    0000   0x05 0x00 0x7d 0x6b 0x94 0x07 0x00 0x00    ..}k....
    0008   0x04 0x63 0x01 0xbf 0x28 0x02 0xa4 0x3c    .c..(..<
    0010   0x00 0xbb 0x02 0x88 0x00 0x10 0x00 0x0c    ........
    0018   0x00 0x00 0x06 0x01 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x55    .......U
    0028   0x6e 0x00 0x00 0x00 0x00 0x00 0x00 0x00    n.......
    0030   0x00                                       .
    decimal
              5    0  125  107  148    7    0    0
              4   99    1  191   40    2  164   60
              0  187    2  136    0   16    0   12
              0    0    6    1    1    0    0    0
              0    0    0    0    0    0    0   85
            110    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 24 TempBasal 2014-03-14T00:53:16 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-14T00:53:16)
    0000   0x10 0xf5 0x00 0x0e 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 25 TempBasalDuration 2014-03-14T00:53:16 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2014-03-14T00:53:16)
    0000   0x10 0xf5 0x00 0x0e 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 CalBGForPH 2014-03-14T01:20:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 43}
```
    op hex (2)
    0000   0x0a 0x2b                                  .+
    decimal
             10   43
    datetime (2014-03-14T01:20:13)
    0000   0x0d 0xd4 0x21 0x6e 0x0e                   ..!n.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 Ian3F 2014-03-14T01:20:13 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x05                                  ?.
    decimal
             63    5
    datetime (2014-03-14T01:20:13)
    0000   0x0d 0xd4 0x61 0x6e 0x0e                   ..an.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 BasalProfileStart 2014-03-14T02:23:16 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-14T02:23:16)
    0000   0x10 0xd7 0x02 0x0e 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 29 BasalProfileStart 2014-03-14T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-14T04:00:00)
    0000   0x00 0xc0 0x04 0x0e 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 30 BasalProfileStart 2014-03-14T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-14T06:00:00)
    0000   0x00 0xc0 0x06 0x0e 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 31 CalBGForPH 2014-03-14T07:29:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2014-03-14T07:29:51)
    0000   0x33 0xdd 0x27 0x6e 0x0e                   3.'n.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 Ian3F 2014-03-14T07:29:51 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2014-03-14T07:29:51)
    0000   0x33 0xdd 0x27 0x6e 0x0e                   3.'n.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 BasalProfileStart 2014-03-14T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-14T10:30:00)
    0000   0x00 0xde 0x0a 0x0e 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 34 CalBGForPH 2014-03-14T12:22:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2014-03-14T12:22:53)
    0000   0x35 0xd6 0x2c 0x6e 0x0e                   5.,n.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 Ian3F 2014-03-14T12:22:53 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2014-03-14T12:22:53)
    0000   0x35 0xd6 0x0c 0x6e 0x0e                   5..n.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 BolusWizard 2014-03-14T12:32:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 80,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2014-03-14T12:32:41)
    0000   0x29 0xe0 0x0c 0x6e 0x0e                   )..n.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x64         d....dd
    decimal
             30   80    0  120   50   80    0    0
            100    0    0    0    0  100  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 BolusWizard 2014-03-14T12:32:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 80,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2014-03-14T12:32:43)
    0000   0x2b 0xe0 0x0c 0x6e 0x0e                   +..n.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x64         d....dd
    decimal
             30   80    0  120   50   80    0    0
            100    0    0    0    0  100  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 Bolus 2014-03-14T12:32:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x00 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    0    0
    datetime (2014-03-14T12:32:43)
    0000   0x2b 0xe0 0x4c 0x6e 0x0e                   +.Ln.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 BolusWizard 2014-03-14T16:37:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-14T16:37:34)
    0000   0x22 0xe5 0x10 0x6e 0x0e                   "..n.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x78 0x32 0x50 0x00 0x00    #P.x2P..
    0008   0x74 0x00 0x00 0x00 0x00 0x74 0x64         t....td
    decimal
             35   80    0  120   50   80    0    0
            116    0    0    0    0  116  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 245, 'amount': 2.5, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x64 0xf5 0x80                   \.d..
    decimal
             92    5  100  245  128
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2014-03-14T16:37:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2014-03-14T16:37:34)
    0000   0x22 0xe5 0x50 0x6e 0x0e                   ".Pn.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 BolusWizard 2014-03-14T17:02:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-14T17:02:38)
    0000   0x26 0xc2 0x11 0x6e 0x0e                   &..n.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x64         d....dd
    decimal
             30   80    0  120   50   80    0    0
            100    0    0    0    0  100  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 2.9, 'curve': 128},
 {'age': 14, 'amount': 2.5, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0x1e 0x80 0x64 0x0e 0x90    \.t..d..
    decimal
             92    8  116   30  128  100   14  144
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2014-03-14T17:02:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x60 0x00    ..d.d.`.
    decimal
              1    0  100    0  100    0   96    0
    datetime (2014-03-14T17:02:38)
    0000   0x26 0xc2 0x51 0x6e 0x0e                   &.Qn.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 45 BolusWizard 2014-03-14T17:16:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-14T17:16:34)
    0000   0x22 0xd0 0x11 0x6e 0x0e                   "..n.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x64         P....Pd
    decimal
             25   80    0  120   50   80    0    0
             80    0    0    0    0   80  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 2.5, 'curve': 128},
 {'age': 44, 'amount': 2.9, 'curve': 128},
 {'age': 28, 'amount': 2.5, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x64 0x0e 0x80 0x74 0x2c 0x80    \.d..t,.
    0008   0x64 0x1c 0x90                             d..
    decimal
             92   11  100   14  128  116   44  128
            100   28  144
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2014-03-14T17:16:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xb0 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  176    0
    datetime (2014-03-14T17:16:34)
    0000   0x22 0xd0 0x51 0x6e 0x0e                   ".Qn.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2014-03-14T17:29:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-14T17:29:34)
    0000   0x22 0xdd 0x11 0x6e 0x0e                   "..n.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x64         @....@d
    decimal
             20   80    0  120   50   80    0    0
             64    0    0    0    0   64  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 2.0, 'curve': 128},
 {'age': 27, 'amount': 2.5, 'curve': 128},
 {'age': 57, 'amount': 2.9, 'curve': 128},
 {'age': 41, 'amount': 2.5, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x11 0x80 0x64 0x1b 0x80    \.P..d..
    0008   0x74 0x39 0x80 0x64 0x29 0x90              t9.d).
    decimal
             92   14   80   17  128  100   27  128
            116   57  128  100   41  144
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2014-03-14T17:29:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0xdc 0x00    ..@.@...
    decimal
              1    0   64    0   64    0  220    0
    datetime (2014-03-14T17:29:35)
    0000   0x23 0xdd 0x51 0x6e 0x0e                   #.Qn.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 CalBGForPH 2014-03-14T19:06:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2014-03-14T19:06:11)
    0000   0x0b 0xc6 0x33 0x0e 0x0e                   ..3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 52 BolusWizard 2014-03-14T19:06:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 153,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 1.2,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2014-03-14T19:06:19)
    0000   0x13 0xc6 0x13 0x6e 0x0e                   ...n.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x6e 0x32 0x50 0x28 0x00    .P.n2P(.
    0008   0x58 0x00 0x00 0x0c 0x00 0x74 0x64         X....td
    decimal
             25   80    0  110   50   80   40    0
             88    0    0   12    0  116  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 1.6, 'curve': 128},
 {'age': 114, 'amount': 2.0, 'curve': 128},
 {'age': 124, 'amount': 2.5, 'curve': 128},
 {'age': 154, 'amount': 2.9, 'curve': 128},
 {'age': 138, 'amount': 2.5, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x40 0x68 0x80 0x50 0x72 0x80    \.@h.Pr.
    0008   0x64 0x7c 0x80 0x74 0x9a 0x80 0x64 0x8a    d|.t..d.
    0010   0x90                                       .
    decimal
             92   17   64  104  128   80  114  128
            100  124  128  116  154  128  100  138
            144
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2014-03-14T19:06:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x0c 0x00    ..t.t...
    decimal
              1    0  116    0  116    0   12    0
    datetime (2014-03-14T19:06:19)
    0000   0x13 0xc6 0x53 0x6e 0x0e                   ..Sn.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 BolusWizard 2014-03-14T19:28:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-14T19:28:48)
    0000   0x30 0xdc 0x13 0x6e 0x0e                   0..n.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    #P.n2P..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x64         |....|d
    decimal
             35   80    0  110   50   80    0    0
            124    0    0    0    0  124  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 2.9, 'curve': 128},
 {'age': 126, 'amount': 1.6, 'curve': 128},
 {'age': 136, 'amount': 2.0, 'curve': 128},
 {'age': 146, 'amount': 2.5, 'curve': 128},
 {'age': 176, 'amount': 2.9, 'curve': 128},
 {'age': 160, 'amount': 2.5, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0x74 0x1a 0x80 0x40 0x7e 0x80    \.t..@~.
    0008   0x50 0x88 0x80 0x64 0x92 0x80 0x74 0xb0    P..d..t.
    0010   0x80 0x64 0xa0 0x90                        .d..
    decimal
             92   20  116   26  128   64  126  128
             80  136  128  100  146  128  116  176
            128  100  160  144
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2014-03-14T19:28:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x64 0x00    ..|.|.d.
    decimal
              1    0  124    0  124    0  100    0
    datetime (2014-03-14T19:28:48)
    0000   0x30 0xdc 0x53 0x6e 0x0e                   0.Sn.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 58 BolusWizard 2014-03-14T19:49:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
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
    datetime (2014-03-14T19:49:22)
    0000   0x16 0xf1 0x13 0x6e 0x0e                   ...n.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    (P.n2P..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x64         ......d
    decimal
             40   80    0  110   50   80    0    0
            144    0    0    0    0  144  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 3.1, 'curve': 128},
 {'age': 47, 'amount': 2.9, 'curve': 128},
 {'age': 147, 'amount': 1.6, 'curve': 128},
 {'age': 157, 'amount': 2.0, 'curve': 128},
 {'age': 167, 'amount': 2.5, 'curve': 128},
 {'age': 197, 'amount': 2.9, 'curve': 128},
 {'age': 181, 'amount': 2.5, 'curve': 144}]
```
    op hex (23)
    0000   0x5c 0x17 0x7c 0x1b 0x80 0x74 0x2f 0x80    \.|..t/.
    0008   0x40 0x93 0x80 0x50 0x9d 0x80 0x64 0xa7    @..P..d.
    0010   0x80 0x74 0xc5 0x80 0x64 0xb5 0x90         .t..d..
    decimal
             92   23  124   27  128  116   47  128
             64  147  128   80  157  128  100  167
            128  116  197  128  100  181  144
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2014-03-14T19:49:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0xb4 0x00    ........
    decimal
              1    0  144    0  144    0  180    0
    datetime (2014-03-14T19:49:22)
    0000   0x16 0xf1 0x53 0x6e 0x0e                   ..Sn.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 BolusWizard 2014-03-14T19:56:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 55,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 200}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-14T19:56:28)
    0000   0x1c 0xf8 0x13 0x6e 0x0e                   ...n.
    body (15)
    hex
    0000   0x37 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    7P.n2P..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x64         ......d
    decimal
             55   80    0  110   50   80    0    0
            200    0    0    0    0  200  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 3.6, 'curve': 128},
 {'age': 34, 'amount': 3.1, 'curve': 128},
 {'age': 54, 'amount': 2.9, 'curve': 128},
 {'age': 154, 'amount': 1.6, 'curve': 128},
 {'age': 164, 'amount': 2.0, 'curve': 128},
 {'age': 174, 'amount': 2.5, 'curve': 128},
 {'age': 204, 'amount': 2.9, 'curve': 128},
 {'age': 188, 'amount': 2.5, 'curve': 144}]
```
    op hex (26)
    0000   0x5c 0x1a 0x90 0x0e 0x80 0x7c 0x22 0x80    \....|".
    0008   0x74 0x36 0x80 0x40 0x9a 0x80 0x50 0xa4    t6.@..P.
    0010   0x80 0x64 0xae 0x80 0x74 0xcc 0x80 0x64    .d..t..d
    0018   0xbc 0x90                                  ..
    decimal
             92   26  144   14  128  124   34  128
            116   54  128   64  154  128   80  164
            128  100  174  128  116  204  128  100
            188  144
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2014-03-14T19:56:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 20.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x01 0x28 0x00    ......(.
    decimal
              1    0  200    0  200    1   40    0
    datetime (2014-03-14T19:56:28)
    0000   0x1c 0xf8 0x53 0x6e 0x0e                   ..Sn.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 BolusWizard 2014-03-14T20:18:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
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
    datetime (2014-03-14T20:18:03)
    0000   0x03 0xd2 0x14 0x6e 0x0e                   ...n.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    (P.n2P..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x64         ......d
    decimal
             40   80    0  110   50   80    0    0
            144    0    0    0    0  144  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 5.0, 'curve': 128},
 {'age': 36, 'amount': 3.6, 'curve': 128},
 {'age': 56, 'amount': 3.1, 'curve': 128},
 {'age': 76, 'amount': 2.9, 'curve': 128},
 {'age': 176, 'amount': 1.6, 'curve': 128},
 {'age': 186, 'amount': 2.0, 'curve': 128},
 {'age': 196, 'amount': 2.5, 'curve': 128},
 {'age': 226, 'amount': 2.9, 'curve': 128},
 {'age': 210, 'amount': 2.5, 'curve': 144}]
```
    op hex (29)
    0000   0x5c 0x1d 0xc8 0x1a 0x80 0x90 0x24 0x80    \.....$.
    0008   0x7c 0x38 0x80 0x74 0x4c 0x80 0x40 0xb0    |8.tL.@.
    0010   0x80 0x50 0xba 0x80 0x64 0xc4 0x80 0x74    .P..d..t
    0018   0xe2 0x80 0x64 0xd2 0x90                   ..d..
    decimal
             92   29  200   26  128  144   36  128
            124   56  128  116   76  128   64  176
            128   80  186  128  100  196  128  116
            226  128  100  210  144
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2014-03-14T20:18:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x01 0x80 0x05    ........
    decimal
              1    0  144    0  144    1  128    5
    datetime (2014-03-14T20:18:03)
    0000   0x03 0xd2 0x74 0x6e 0x0e                   ..tn.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 67 BasalProfileStart 2014-03-14T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-14T22:30:00)
    0000   0x00 0xde 0x16 0x0e 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 68 CalBGForPH 2014-03-14T23:27:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2014-03-14T23:27:25)
    0000   0x19 0xdb 0x37 0x6e 0x0e                   ..7n.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 69 Ian3F 2014-03-14T23:27:25 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-03-14T23:27:25)
    0000   0x19 0xdb 0x17 0x6e 0x0e                   ...n.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 70 BasalProfileStart 2014-03-15T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-15T00:00:00)
    0000   0x00 0xc0 0x00 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 71 MResultTotals 2014-03-15T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x66                   ....f
    decimal
              7    0    0    6  102
    datetime (2014-03-15T00:00:00)
    0000   0x2e 0x8e                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-2.data: 72 records`
