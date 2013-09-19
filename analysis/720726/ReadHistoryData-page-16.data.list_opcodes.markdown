## START analysis/ianj/raw//ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x2e 0x26                                  .&
##### DEBUG DECIMAL
             46   38
#### RECORD 0 Ian3F 2012-08-21T18:22:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x2d                                  ?-
    decimal
             63   45
    datetime (2012-08-21T18:22:18)
    0000   0x92 0x16 0x32 0x75 0x0c                   ..2u.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2012-08-21T18:22:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 200,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc8                                  [.
    decimal
             91  200
    datetime (2012-08-21T18:22:39)
    0000   0xa7 0x16 0x12 0x75 0x0c                   ...u.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xfc 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0xfc 0x36         ......6
    decimal
              0  144    0  110   23   54  252    0
              0    0    0    0    0  252   54
    DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 248, 'amount': 3.3, 'curve': 4},
 {'age': 82, 'amount': 1.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0xf8 0x04 0x48 0x52 0x14    \....HR.
    decimal
             92    8  132  248    4   72   82   20
    datetime (unknown)

    body (0)

#### RECORD 3 Ian69 2012-08-21T18:22:39 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-21T18:22:39)
    0000   0xa7 0x16 0x72 0x15 0x0c                   ..r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 4 Bolus 2012-08-21T18:22:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 25.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xfc 0x00 0xfc 0x00 0x00 0x00    ........
    decimal
              1    0  252    0  252    0    0    0
    datetime (2012-08-21T18:22:39)
    0000   0xa7 0x16 0x52 0x75 0x0c                   ..Ru.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 5 CalBGForPH 2012-08-21T18:37:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 339}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2012-08-21T18:37:58)
    0000   0xba 0x25 0x32 0x75 0x8c                   .%2u.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 6 Ian3F 2012-08-21T18:37:58 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x2a                                  ?*
    decimal
             63   42
    datetime (2012-08-21T18:37:58)
    0000   0xba 0x25 0x72 0x75 0x0c                   .%ru.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 CalBGForPH 2012-08-21T20:58:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2012-08-21T20:58:08)
    0000   0x88 0x3a 0x34 0x75 0x0c                   .:4u.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2012-08-21T20:58:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2012-08-21T20:58:08)
    0000   0x88 0x3a 0xd4 0x75 0x0c                   .:.u.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 BolusWizard 2012-08-21T20:59:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 92,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2012-08-21T20:59:19)
    0000   0x93 0x3b 0x14 0x75 0x0c                   .;.u.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x40 0x00    ...n.6@.
    0008   0x00 0x00 0x00 0x44 0x00 0x00 0x36         ...D..6
    decimal
              0  144    0  110   23   54   64    0
              0    0    0   68    0    0   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 4.35, 'curve': 4},
 {'age': 165, 'amount': 1.95, 'curve': 4},
 {'age': 149, 'amount': 3.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xae 0x9b 0x04 0x4e 0xa5 0x04    \....N..
    0008   0x84 0x95 0x14                             ...
    decimal
             92   11  174  155    4   78  165    4
            132  149   20
    datetime (unknown)

    body (0)

#### RECORD 11 NoDelivery 2012-08-21T21:06:18 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xfc                        ....
    decimal
              6    4   11  252
    datetime (2012-08-21T21:06:18)
    0000   0x92 0x06 0x55 0x55 0x0c                   ..UU.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 12 ClearAlarm 2012-08-21T21:11:05 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2012-08-21T21:11:05)
    0000   0x85 0x0b 0x15 0x15 0x0c                   .....
    body (0)

#### RECORD 13 BasalProfileStart 2012-08-21T22:29:46 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-21T22:29:46)
    0000   0xae 0x1d 0x16 0x15 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 14 NoDelivery 2012-08-21T22:30:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xfc                        ....
    decimal
              6    4   11  252
    datetime (2012-08-21T22:30:00)
    0000   0x80 0x1e 0x56 0x55 0x0c                   ..VU.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 15 ClearAlarm 2012-08-21T22:30:02 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2012-08-21T22:30:02)
    0000   0x82 0x1e 0x16 0x15 0x0c                   .....
    body (0)

#### RECORD 16 BasalProfileStart 2012-08-21T22:30:05 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-21T22:30:05)
    0000   0x85 0x1e 0x16 0x15 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 17 Rewind 2012-08-21T22:34:44 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-08-21T22:34:44)
    0000   0xac 0x22 0x16 0x15 0x0c                   ."...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 Prime 2012-08-21T22:35:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x0e                   .....
    decimal
              3    0    0    0   14
    datetime (2012-08-21T22:35:19)
    0000   0x93 0x23 0x36 0x15 0x0c                   .#6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 19 BasalProfileStart 2012-08-21T22:35:32 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-21T22:35:32)
    0000   0xa0 0x23 0x16 0x15 0x0c                   .#...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 0, 1]
#### RECORD 20 CalBGForPH 2012-08-21T22:38:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 291}
```
    op hex (2)
    0000   0x0a 0x23                                  .#
    decimal
             10   35
    datetime (2012-08-21T22:38:30)
    0000   0x9e 0x26 0x36 0x75 0x8c                   .&6u.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 Ian3F 2012-08-21T22:38:30 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x24                                  ?$
    decimal
             63   36
    datetime (2012-08-21T22:38:30)
    0000   0x9e 0x26 0x76 0x75 0x0c                   .&vu.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2012-08-21T22:38:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 162,
 'bg_target_high': 1,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 32,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 18.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2012-08-21T22:38:42)
    0000   0xaa 0x26 0x16 0x75 0x0c                   .&.u.
    body (15)
    hex
    0000   0x20 0x90 0x00 0x6e 0x17 0x36 0xb8 0x00     ..n.6..
    0008   0x74 0x00 0x00 0x00 0x01 0x2c 0x36         t....,6
    decimal
             32  144    0  110   23   54  184    0
            116    0    0    0    1   44   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 254, 'amount': 4.35, 'curve': 4},
 {'age': 8, 'amount': 1.95, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xae 0xfe 0x04 0x4e 0x08 0x14    \....N..
    decimal
             92    8  174  254    4   78    8   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2012-08-21T22:38:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x2c 0x01 0x2c 0x00 0x00 0x00    ..,.,...
    decimal
              1    1   44    1   44    0    0    0
    datetime (2012-08-21T22:38:42)
    0000   0xaa 0x26 0x56 0x75 0x0c                   .&Vu.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 Bolus 2012-08-21T22:51:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x01 0x28 0x00    ..P.P.(.
    decimal
              1    0   80    0   80    1   40    0
    datetime (2012-08-21T22:51:33)
    0000   0xa1 0x33 0x56 0x75 0x0c                   .3Vu.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2012-08-21T23:19:39 head[2], body[15] op[0x5b]
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
    datetime (2012-08-21T23:19:39)
    0000   0xa7 0x13 0x17 0x75 0x0c                   ...u.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    DAY BITS: [0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 2.0, 'curve': 4},
 {'age': 45, 'amount': 1.1, 'curve': 5},
 {'age': 39, 'amount': 4.35, 'curve': 20},
 {'age': 49, 'amount': 1.95, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x23 0x04 0x2c 0x2d 0x05    \.P#.,-.
    0008   0xae 0x27 0x14 0x4e 0x31 0x14              .'.N1.
    decimal
             92   14   80   35    4   44   45    5
            174   39   20   78   49   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2012-08-21T23:19:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x01 0x58 0x00    ......X.
    decimal
              1    0  132    0  132    1   88    0
    datetime (2012-08-21T23:19:39)
    0000   0xa7 0x13 0x57 0x75 0x0c                   ..Wu.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 29 BasalProfileStart 2012-08-22T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-22T00:00:00)
    0000   0x80 0x00 0x00 0x16 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 30 ResultTotals (2000, 8, 0, 0, 12, 21) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0xd3                   .....
    decimal
              7    0    0    8  211
    datetime ((2000, 8, 0, 0, 12, 21))
    0000   0x95 0x0c 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 31 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x95 0x0c 0x06 0x11 0x0a 0x74 0x6a    n.....tj
    0008   0x07 0x00 0x00 0x08 0xd3 0x03 0x53 0x26    ......S&
    0010   0x05 0x80 0x3e 0x00 0x9d 0x01 0xb4 0x02    ..>.....
    0018   0x50 0x01 0x2c 0x00 0x50 0x04 0x03 0x01    P.,.P...
    0020   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  149   12    6   17   10  116  106
              7    0    0    8  211    3   83   38
              5  128   62    0  157    1  180    2
             80    1   44    0   80    4    3    1
              1    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 32 BasalProfileStart 2012-08-22T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-22T04:00:00)
    0000   0x80 0x00 0x04 0x16 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 33 CalBGForPH 2012-08-22T06:07:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 298}
```
    op hex (2)
    0000   0x0a 0x2a                                  .*
    decimal
             10   42
    datetime (2012-08-22T06:07:40)
    0000   0xa8 0x07 0x26 0x76 0x8c                   ..&v.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 Ian3F 2012-08-22T06:07:40 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x25                                  ?%
    decimal
             63   37
    datetime (2012-08-22T06:07:40)
    0000   0xa8 0x07 0x46 0x76 0x0c                   ..Fv.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2012-08-22T06:07:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 165,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 19.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa5                                  [.
    decimal
             91  165
    datetime (2012-08-22T06:07:50)
    0000   0xb2 0x07 0x06 0x76 0x0c                   ...v.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0xc0 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0xc0 0x36         ......6
    decimal
              0  144    0  110   23   54  192    0
              0    0    0    0    0  192   54
    DAY BITS: [0, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 157, 'amount': 3.3, 'curve': 20},
 {'age': 187, 'amount': 2.0, 'curve': 20},
 {'age': 197, 'amount': 1.1, 'curve': 21}]
```
    op hex (11)
    0000   0x5c 0x0b 0x84 0x9d 0x14 0x50 0xbb 0x14    \....P..
    0008   0x2c 0xc5 0x15                             ,..
    decimal
             92   11  132  157   20   80  187   20
             44  197   21
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2012-08-22T06:07:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 19.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc0 0x00 0xc0 0x00 0x00 0x00    ........
    decimal
              1    0  192    0  192    0    0    0
    datetime (2012-08-22T06:07:50)
    0000   0xb2 0x07 0x46 0x76 0x0c                   ..Fv.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 38 Rewind 2012-08-22T06:46:57 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-08-22T06:46:57)
    0000   0xb9 0x2e 0x06 0x16 0x0c                   .....
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 Prime 2012-08-22T06:47:13 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x40                   ....@
    decimal
              3    0    0    0   64
    datetime (2012-08-22T06:47:13)
    0000   0x8d 0x2f 0x26 0x16 0x0c                   ./&..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 BasalProfileStart 2012-08-22T06:48:07 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-22T06:48:07)
    0000   0x87 0x30 0x06 0x16 0x0c                   .0...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 0, 1]
#### RECORD 41 Prime 2012-08-22T06:47:32 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2012-08-22T06:47:32)
    0000   0xa0 0x2f 0x06 0x16 0x0c                   ./...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 42 BolusWizard 2012-08-22T07:04:40 head[2], body[15] op[0x5b]
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
    datetime (2012-08-22T07:04:40)
    0000   0xa8 0x04 0x07 0x76 0x0c                   ...v.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    DAY BITS: [0, 1, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 4.8, 'curve': 4},
 {'age': 214, 'amount': 3.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0x3c 0x04 0x84 0xd6 0x14    \..<....
    decimal
             92    8  192   60    4  132  214   20
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2012-08-22T07:04:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0xa0 0x00    ..L.L...
    decimal
              1    0   76    0   76    0  160    0
    datetime (2012-08-22T07:04:41)
    0000   0xa9 0x04 0x47 0x76 0x0c                   ..Gv.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 45 BolusWizard 2012-08-22T07:48:26 head[2], body[15] op[0x5b]
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
    datetime (2012-08-22T07:48:26)
    0000   0x9a 0x30 0x07 0x76 0x0c                   .0.v.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 1.9, 'curve': 4},
 {'age': 104, 'amount': 4.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x2c 0x04 0xc0 0x68 0x04    \.L,..h.
    decimal
             92    8   76   44    4  192  104    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-08-22T07:48:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0xb0 0x00    ..l.l...
    decimal
              1    0  108    0  108    0  176    0
    datetime (2012-08-22T07:48:26)
    0000   0x9a 0x30 0x47 0x76 0x0c                   .0Gv.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2012-08-22T08:09:59 head[2], body[15] op[0x5b]
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
    datetime (2012-08-22T08:09:59)
    0000   0xbb 0x09 0x08 0x76 0x0c                   ...v.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 2.7, 'curve': 4},
 {'age': 65, 'amount': 1.9, 'curve': 4},
 {'age': 125, 'amount': 4.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0x19 0x04 0x4c 0x41 0x04    \.l..LA.
    0008   0xc0 0x7d 0x04                             .}.
    decimal
             92   11  108   25    4   76   65    4
            192  125    4
    datetime (unknown)

    body (0)

#### RECORD 50 Ian69 2012-08-22T08:10:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-22T08:10:00)
    0000   0x80 0x0a 0x08 0x16 0x0c                   .....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30

#### RECORD 51 Bolus 2012-08-22T08:10:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0xf8 0x00    ..H.H...
    decimal
              1    0   72    0   72    0  248    0
    datetime (2012-08-22T08:10:00)
    0000   0x80 0x0a 0x48 0x76 0x0c                   ..Hv.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 52 BasalProfileStart 2012-08-22T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-22T09:30:00)
    0000   0x80 0x1e 0x09 0x16 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 53 CalBGForPH 2012-08-22T10:38:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2012-08-22T10:38:48)
    0000   0xb0 0x26 0x2a 0x76 0x0c                   .&*v.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 Ian3F 2012-08-22T10:38:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2012-08-22T10:38:48)
    0000   0xb0 0x26 0xea 0x76 0x0c                   .&.v.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 BolusWizard 2012-08-22T10:39:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 4.8,
 'carb_input': 50,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 180}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2012-08-22T10:39:05)
    0000   0x85 0x27 0x0a 0x76 0x0c                   .'.v.
    body (15)
    hex
    0000   0x32 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    2..n.6$.
    0008   0xb4 0x00 0x00 0x30 0x00 0xb4 0x36         ...0..6
    decimal
             50  144    0  110   23   54   36    0
            180    0    0   48    0  180   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.8, 'curve': 4},
 {'age': 175, 'amount': 2.7, 'curve': 4},
 {'age': 215, 'amount': 1.9, 'curve': 4},
 {'age': 19, 'amount': 4.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x9b 0x04 0x6c 0xaf 0x04    \.H..l..
    0008   0x4c 0xd7 0x04 0xc0 0x13 0x14              L.....
    decimal
             92   14   72  155    4  108  175    4
             76  215    4  192   19   20
    datetime (unknown)

    body (0)

#### RECORD 57 BolusWizard 2012-08-22T10:39:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 4.8,
 'carb_input': 50,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 180}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2012-08-22T10:39:09)
    0000   0x89 0x27 0x0a 0x76 0x0c                   .'.v.
    body (15)
    hex
    0000   0x32 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    2..n.6$.
    0008   0xb4 0x00 0x00 0x30 0x00 0xb4 0x36         ...0..6
    decimal
             50  144    0  110   23   54   36    0
            180    0    0   48    0  180   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.8, 'curve': 4},
 {'age': 175, 'amount': 2.7, 'curve': 4},
 {'age': 215, 'amount': 1.9, 'curve': 4},
 {'age': 19, 'amount': 4.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x9b 0x04 0x6c 0xaf 0x04    \.H..l..
    0008   0x4c 0xd7 0x04 0xc0 0x13 0x14              L.....
    decimal
             92   14   72  155    4  108  175    4
             76  215    4  192   19   20
    datetime (unknown)

    body (0)

#### RECORD 59 BolusWizard 2012-08-22T10:39:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 4.8,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2012-08-22T10:39:15)
    0000   0x8f 0x27 0x0a 0x76 0x0c                   .'.v.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    #..n.6$.
    0008   0x7c 0x00 0x00 0x30 0x00 0x7c 0x36         |..0.|6
    decimal
             35  144    0  110   23   54   36    0
            124    0    0   48    0  124   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.8, 'curve': 4},
 {'age': 175, 'amount': 2.7, 'curve': 4},
 {'age': 215, 'amount': 1.9, 'curve': 4},
 {'age': 19, 'amount': 4.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x9b 0x04 0x6c 0xaf 0x04    \.H..l..
    0008   0x4c 0xd7 0x04 0xc0 0x13 0x14              L.....
    decimal
             92   14   72  155    4  108  175    4
             76  215    4  192   19   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2012-08-22T10:39:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x30 0x00    ..|.|.0.
    decimal
              1    0  124    0  124    0   48    0
    datetime (2012-08-22T10:39:15)
    0000   0x8f 0x27 0x4a 0x76 0x0c                   .'Jv.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 BolusWizard 2012-08-22T11:00:16 head[2], body[15] op[0x5b]
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
    datetime (2012-08-22T11:00:16)
    0000   0x90 0x00 0x0b 0x76 0x0c                   ...v.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    DAY BITS: [0, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 3.1, 'curve': 4},
 {'age': 176, 'amount': 1.8, 'curve': 4},
 {'age': 196, 'amount': 2.7, 'curve': 4},
 {'age': 236, 'amount': 1.9, 'curve': 4},
 {'age': 40, 'amount': 4.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x7c 0x1a 0x04 0x48 0xb0 0x04    \.|..H..
    0008   0x6c 0xc4 0x04 0x4c 0xec 0x04 0xc0 0x28    l..L...(
    0010   0x14                                       .
    decimal
             92   17  124   26    4   72  176    4
            108  196    4   76  236    4  192   40
             20
    datetime (unknown)

    body (0)

#### RECORD 64 Ian69 2012-08-22T11:00:16 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-22T11:00:16)
    0000   0x90 0x00 0x0b 0x16 0x0c                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 65 Bolus 2012-08-22T11:00:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x98 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  152    0
    datetime (2012-08-22T11:00:16)
    0000   0x90 0x00 0x4b 0x76 0x0c                   ..Kv.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 66 CalBGForPH 2012-08-22T12:00:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 204}
```
    op hex (2)
    0000   0x0a 0xcc                                  ..
    decimal
             10  204
    datetime (2012-08-22T12:00:17)
    0000   0x91 0x00 0x2c 0x76 0x0c                   ..,v.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 67 Ian3F 2012-08-22T12:00:17 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2012-08-22T12:00:17)
    0000   0x91 0x00 0x8c 0x76 0x0c                   ...v.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 68 BolusWizard 2012-08-22T12:00:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 113,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 16.8,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 10.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x71                                  [q
    decimal
             91  113
    datetime (2012-08-22T12:00:23)
    0000   0x97 0x00 0x0c 0x76 0x0c                   ...v.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x64 0x00    ...n.6d.
    0008   0x24 0x00 0x00 0xa8 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54  100    0
             36    0    0  168    0   36   54
    DAY BITS: [0, 1, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 2.5, 'curve': 4},
 {'age': 86, 'amount': 3.1, 'curve': 4},
 {'age': 236, 'amount': 1.8, 'curve': 4},
 {'age': 0, 'amount': 2.7, 'curve': 20},
 {'age': 40, 'amount': 1.9, 'curve': 20},
 {'age': 100, 'amount': 4.8, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x64 0x42 0x04 0x7c 0x56 0x04    \.dB.|V.
    0008   0x48 0xec 0x04 0x6c 0x00 0x14 0x4c 0x28    H..l..L(
    0010   0x14 0xc0 0x64 0x14                        ..d.
    decimal
             92   20  100   66    4  124   86    4
             72  236    4  108    0   20   76   40
             20  192  100   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2012-08-22T12:00:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0xa8 0x00    ..$.$...
    decimal
              1    0   36    0   36    0  168    0
    datetime (2012-08-22T12:00:24)
    0000   0x98 0x00 0x4c 0x76 0x0c                   ..Lv.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 71 BasalProfileStart 2012-08-22T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-22T13:00:00)
    0000   0x80 0x00 0x0d 0x16 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 72 CalBGForPH 2012-08-22T13:37:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2012-08-22T13:37:16)
    0000   0x90 0x25 0x2d 0x76 0x0c                   .%-v.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 Ian3F 2012-08-22T13:37:16 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2012-08-22T13:37:16)
    0000   0x90 0x25 0xad 0x76 0x0c                   .%.v.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 74 BolusWizard 2012-08-22T13:37:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 52,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.4,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x34                                  [4
    decimal
             91   52
    datetime (2012-08-22T13:37:26)
    0000   0x9a 0x25 0x0d 0x76 0x0c                   .%.v.
    body (15)
    hex
    0000   0x10 0x90 0x00 0x6e 0x17 0x36 0xfc 0x00    ...n.6..
    0008   0x38 0xf8 0x00 0x40 0x00 0x34 0x36         8..@.46
    decimal
             16  144    0  110   23   54  252    0
             56  248    0   64    0   52   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 75 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 0.9, 'curve': 4},
 {'age': 163, 'amount': 2.5, 'curve': 4},
 {'age': 183, 'amount': 3.1, 'curve': 4},
 {'age': 77, 'amount': 1.8, 'curve': 20},
 {'age': 97, 'amount': 2.7, 'curve': 20},
 {'age': 137, 'amount': 1.9, 'curve': 20},
 {'age': 197, 'amount': 4.8, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x24 0x67 0x04 0x64 0xa3 0x04    \.$g.d..
    0008   0x7c 0xb7 0x04 0x48 0x4d 0x14 0x6c 0x61    |..HM.la
    0010   0x14 0x4c 0x89 0x14 0xc0 0xc5 0x14         .L.....
    decimal
             92   23   36  103    4  100  163    4
            124  183    4   72   77   20  108   97
             20   76  137   20  192  197   20
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2012-08-22T13:37:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x40 0x00    ..4.4.@.
    decimal
              1    0   52    0   52    0   64    0
    datetime (2012-08-22T13:37:26)
    0000   0x9a 0x25 0x4d 0x76 0x0c                   .%Mv.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
`end analysis/ianj/raw//ReadHistoryData-page-16.data: 77 records`
