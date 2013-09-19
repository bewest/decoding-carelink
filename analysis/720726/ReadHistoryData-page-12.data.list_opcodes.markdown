## START analysis/ianj/raw//ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x81 0xcb                                  ..
##### DEBUG DECIMAL
            129  203
#### RECORD 0 Bolus 2012-08-27T00:37:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x54 0x00    ..X.X.T.
    decimal
              1    0   88    0   88    0   84    0
    datetime (2012-08-27T00:37:56)
    0000   0xb8 0x25 0x40 0x7b 0x0c                   .%@{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2012-08-27T00:43:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 31,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 112}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-27T00:43:44)
    0000   0xac 0x2b 0x00 0x7b 0x0c                   .+.{.
    body (15)
    hex
    0000   0x1f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x70 0x00 0x00 0x00 0x00 0x70 0x36         p....p6
    decimal
             31  144    0  110   23   54    0    0
            112    0    0    0    0  112   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 2.2, 'curve': 4},
 {'age': 139, 'amount': 4.2, 'curve': 4},
 {'age': 169, 'amount': 1.8, 'curve': 4},
 {'age': 63, 'amount': 1.3, 'curve': 20},
 {'age': 103, 'amount': 2.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x58 0x09 0x04 0xa8 0x8b 0x04    \.X.....
    0008   0x48 0xa9 0x04 0x34 0x3f 0x14 0x5c 0x67    H..4?.\g
    0010   0x14                                       .
    decimal
             92   17   88    9    4  168  139    4
             72  169    4   52   63   20   92  103
             20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2012-08-27T00:43:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0xa4 0x00    ........
    decimal
              1    0  132    0  132    0  164    0
    datetime (2012-08-27T00:43:44)
    0000   0xac 0x2b 0x40 0x7b 0x0c                   .+@{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 BasalProfileStart 2012-08-27T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-27T04:00:00)
    0000   0x80 0x00 0x04 0x1b 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 5 CalBGForPH 2012-08-27T08:20:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2012-08-27T08:20:52)
    0000   0xb4 0x14 0x28 0x7b 0x0c                   ..({.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 Ian3F 2012-08-27T08:20:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2012-08-27T08:20:52)
    0000   0xb4 0x14 0x68 0x7b 0x0c                   ..h{.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 7 BolusWizard 2012-08-27T09:02:11 head[2], body[15] op[0x5b]
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
    datetime (2012-08-27T09:02:11)
    0000   0x8b 0x02 0x09 0x7b 0x0c                   ...{.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    DAY BITS: [0, 1, 1]
#### RECORD 8 Ian69 2012-08-27T09:02:11 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-27T09:02:11)
    0000   0x8b 0x02 0x09 0x1b 0x0c                   .....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30

#### RECORD 9 Bolus 2012-08-27T09:02:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2012-08-27T09:02:11)
    0000   0x8b 0x02 0x49 0x7b 0x0c                   ..I{.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 10 BasalProfileStart 2012-08-27T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-27T09:30:00)
    0000   0x80 0x1e 0x09 0x1b 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 11 CalBGForPH 2012-08-27T12:47:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2012-08-27T12:47:46)
    0000   0xae 0x2f 0x2c 0x7b 0x0c                   ./,{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2012-08-27T12:47:46 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2012-08-27T12:47:46)
    0000   0xae 0x2f 0x2c 0x7b 0x0c                   ./,{.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2012-08-27T12:47:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 72,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 2.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x48                                  [H
    decimal
             91   72
    datetime (2012-08-27T12:47:58)
    0000   0xba 0x2f 0x0c 0x7b 0x0c                   ./.{.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x1c 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x08 0x00 0x14 0x36         ......6
    decimal
              0  144    0  110   23   54   28    0
              0    0    0    8    0   20   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 233, 'amount': 2.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0xe9 0x04                   \.l..
    decimal
             92    5  108  233    4
    datetime (unknown)

    body (0)

#### RECORD 15 Ian69 2012-08-27T12:47:58 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-27T12:47:58)
    0000   0xba 0x2f 0x0c 0x1b 0x0c                   ./...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 16 Bolus 2012-08-27T12:47:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x08 0x00    ........
    decimal
              1    0   20    0   20    0    8    0
    datetime (2012-08-27T12:47:58)
    0000   0xba 0x2f 0x4c 0x7b 0x0c                   ./L{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2012-08-27T12:51:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 72,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 2.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x48                                  [H
    decimal
             91   72
    datetime (2012-08-27T12:51:41)
    0000   0xa9 0x33 0x0c 0x7b 0x0c                   .3.{.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x1c 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x1c 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54   28    0
              0    0    0   28    0    0   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 0.5, 'curve': 4},
 {'age': 237, 'amount': 2.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x07 0x04 0x6c 0xed 0x04    \....l..
    decimal
             92    8   20    7    4  108  237    4
    datetime (unknown)

    body (0)

#### RECORD 19 CalBGForPH 2012-08-27T12:51:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 83}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2012-08-27T12:51:46)
    0000   0xae 0x33 0x4c 0xdb 0x0c                   .3L..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0]
#### RECORD 20 BasalProfileStart 2012-08-27T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-27T13:00:00)
    0000   0x80 0x00 0x0d 0x1b 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 21 CalBGForPH 2012-08-27T15:37:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 152}
```
    op hex (2)
    0000   0x0a 0x98                                  ..
    decimal
             10  152
    datetime (2012-08-27T15:37:42)
    0000   0xaa 0x25 0x2f 0x7b 0x0c                   .%/{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 Ian3F 2012-08-27T15:37:42 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2012-08-27T15:37:42)
    0000   0xaa 0x25 0x0f 0x7b 0x0c                   .%.{.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2012-08-27T15:37:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 84,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2012-08-27T15:37:56)
    0000   0xb8 0x25 0x0f 0x7b 0x0c                   .%.{.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x34 0x00    ...n.64.
    0008   0x00 0x00 0x00 0x04 0x00 0x30 0x36         .....06
    decimal
              0  144    0  110   23   54   52    0
              0    0    0    4    0   48   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 0.5, 'curve': 4},
 {'age': 147, 'amount': 2.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0xad 0x04 0x6c 0x93 0x14    \....l..
    decimal
             92    8   20  173    4  108  147   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2012-08-27T15:37:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x04 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    4    0
    datetime (2012-08-27T15:37:56)
    0000   0xb8 0x25 0x4f 0x7b 0x0c                   .%O{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 Ian69 2012-08-27T21:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-27T21:30:00)
    0000   0x80 0x1e 0x75 0x1b 0x0c                   ..u..
    body (2)
    hex
    0000   0x35 0x1e                                  5.
    decimal
             53   30

#### RECORD 27 BasalProfileStart 2012-08-28T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-28T00:00:00)
    0000   0x80 0x00 0x00 0x1c 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 28 ResultTotals (2000, 8, 0, 0, 12, 27) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x15                   .....
    decimal
              7    0    0    5   21
    datetime ((2000, 8, 0, 0, 12, 27))
    0000   0x9b 0x0c 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 29 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x9b 0x0c 0x06 0x00 0x7d 0x43 0x98    n....}C.
    0008   0x04 0x00 0x00 0x05 0x15 0x03 0x89 0x46    .......F
    0010   0x01 0x8c 0x1e 0x00 0x56 0x00 0xc4 0x00    ....V...
    0018   0x44 0x00 0x84 0x00 0x00 0x02 0x02 0x01    D.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x96 0x96 0x00 0x00 0x00         .......
    decimal
            110  155   12    6    0  125   67  152
              4    0    0    5   21    3  137   70
              1  140   30    0   86    0  196    0
             68    0  132    0    0    2    2    1
              0    0    0    0    0    0    0    0
              0    0  150  150    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 30 BasalProfileStart 2012-08-28T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-28T04:00:00)
    0000   0x80 0x00 0x04 0x1c 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 31 NoDelivery 2012-08-28T07:45:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2012-08-28T07:45:00)
    0000   0x80 0x2d 0x47 0xbc 0x0c                   .-G..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1]
#### RECORD 32 ClearAlarm 2012-08-28T07:57:37 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2012-08-28T07:57:37)
    0000   0xa5 0x39 0x07 0x1c 0x0c                   .9...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 BasalProfileStart 2012-08-28T07:57:37 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-28T07:57:37)
    0000   0xa5 0x39 0x07 0x1c 0x0c                   .9...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 0, 1]
#### RECORD 34 CalBGForPH 2012-08-28T08:04:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 145}
```
    op hex (2)
    0000   0x0a 0x91                                  ..
    decimal
             10  145
    datetime (2012-08-28T08:04:56)
    0000   0xb8 0x04 0x28 0x7c 0x0c                   ..(|.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 35 Ian3F 2012-08-28T08:04:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2012-08-28T08:04:56)
    0000   0xb8 0x04 0x28 0x7c 0x0c                   ..(|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 36 CalBGForPH 2012-08-28T09:07:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2012-08-28T09:07:02)
    0000   0x82 0x07 0x29 0x7c 0x0c                   ..)|.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 37 Ian3F 2012-08-28T09:07:02 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2012-08-28T09:07:02)
    0000   0x82 0x07 0x09 0x7c 0x0c                   ...|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2012-08-28T09:07:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 11.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2012-08-28T09:07:10)
    0000   0x8a 0x07 0x09 0x7c 0x0c                   ...|.
    body (15)
    hex
    0000   0x11 0x90 0x00 0x6e 0x17 0x36 0x70 0x00    ...n.6p.
    0008   0x3c 0x00 0x00 0x00 0x00 0xac 0x36         <.....6
    decimal
             17  144    0  110   23   54  112    0
             60    0    0    0    0  172   54
    DAY BITS: [0, 1, 1]
#### RECORD 39 Ian69 2012-08-28T09:07:10 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-28T09:07:10)
    0000   0x8a 0x07 0x09 0x1c 0x0c                   .....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30

#### RECORD 40 Bolus 2012-08-28T09:07:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 17.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0x00 0x00    ........
    decimal
              1    0  172    0  172    0    0    0
    datetime (2012-08-28T09:07:10)
    0000   0x8a 0x07 0x49 0x7c 0x0c                   ..I|.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 41 BasalProfileStart 2012-08-28T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-28T09:30:00)
    0000   0x80 0x1e 0x09 0x1c 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 42 CalBGForPH 2012-08-28T11:36:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2012-08-28T11:36:06)
    0000   0x86 0x24 0x2b 0x7c 0x0c                   .$+|.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 Ian3F 2012-08-28T11:36:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2012-08-28T11:36:06)
    0000   0x86 0x24 0xeb 0x7c 0x0c                   .$.|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 BolusWizard 2012-08-28T11:39:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 53,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 4.8,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 25.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x35                                  [5
    decimal
             91   53
    datetime (2012-08-28T11:39:38)
    0000   0xa6 0x27 0x0b 0x7c 0x0c                   .'.|.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0xfc 0x00    ...n.6..
    0008   0x64 0xf8 0x00 0x30 0x00 0x60 0x36         d..0.`6
    decimal
             28  144    0  110   23   54  252    0
            100  248    0   48    0   96   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 4.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xac 0x9b 0x04                   \....
    decimal
             92    5  172  155    4
    datetime (unknown)

    body (0)

#### RECORD 46 Ian69 2012-08-28T11:39:38 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-28T11:39:38)
    0000   0xa6 0x27 0x0b 0x1c 0x0c                   .'...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 47 Bolus 2012-08-28T11:39:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x30 0x00    ..`.`.0.
    decimal
              1    0   96    0   96    0   48    0
    datetime (2012-08-28T11:39:38)
    0000   0xa6 0x27 0x4b 0x7c 0x0c                   .'K|.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2012-08-28T11:58:17 head[2], body[15] op[0x5b]
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
    datetime (2012-08-28T11:58:17)
    0000   0x91 0x3a 0x0b 0x7c 0x0c                   .:.|.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 2.4, 'curve': 4},
 {'age': 174, 'amount': 4.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x60 0x18 0x04 0xac 0xae 0x04    \.`.....
    decimal
             92    8   96   24    4  172  174    4
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2012-08-28T11:58:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x80 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  128    0
    datetime (2012-08-28T11:58:17)
    0000   0x91 0x3a 0x4b 0x7c 0x0c                   .:K|.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 BasalProfileStart 2012-08-28T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-28T13:00:00)
    0000   0x80 0x00 0x0d 0x1c 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 52 BolusWizard 2012-08-28T18:57:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 39,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 140}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-28T18:57:10)
    0000   0x8a 0x39 0x12 0x7c 0x0c                   .9.|.
    body (15)
    hex
    0000   0x27 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    '..n.6..
    0008   0x8c 0x00 0x00 0x00 0x00 0x8c 0x36         ......6
    decimal
             39  144    0  110   23   54    0    0
            140    0    0    0    0  140   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 167, 'amount': 1.0, 'curve': 20},
 {'age': 187, 'amount': 2.4, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0xa7 0x14 0x60 0xbb 0x14    \.(..`..
    decimal
             92    8   40  167   20   96  187   20
    datetime (unknown)

    body (0)

#### RECORD 54 Ian69 2012-08-28T18:57:10 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-28T18:57:10)
    0000   0x8a 0x39 0x72 0x1c 0x0c                   .9r..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 55 Bolus 2012-08-28T18:57:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x00 0x00    ........
    decimal
              1    0  140    0  140    0    0    0
    datetime (2012-08-28T18:57:10)
    0000   0x8a 0x39 0x52 0x7c 0x0c                   .9R|.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 CalBGForPH 2012-08-28T19:02:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2012-08-28T19:02:48)
    0000   0xb0 0x02 0x33 0x7c 0x0c                   ..3|.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 57 Ian3F 2012-08-28T19:02:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2012-08-28T19:02:48)
    0000   0xb0 0x02 0x93 0x7c 0x0c                   ...|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 58 BolusWizard 2012-08-28T19:11:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 87,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 14.0,
 'carb_input': 37,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0x57                                  [W
    decimal
             91   87
    datetime (2012-08-28T19:11:51)
    0000   0xb3 0x0b 0x13 0x7c 0x0c                   ...|.
    body (15)
    hex
    0000   0x25 0x90 0x00 0x6e 0x17 0x36 0x38 0x00    %..n.68.
    0008   0x84 0x00 0x00 0x8c 0x00 0x84 0x36         ......6
    decimal
             37  144    0  110   23   54   56    0
            132    0    0  140    0  132   54
    DAY BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 3.5, 'curve': 4},
 {'age': 181, 'amount': 1.0, 'curve': 20},
 {'age': 201, 'amount': 2.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x8c 0x11 0x04 0x28 0xb5 0x14    \....(..
    0008   0x60 0xc9 0x14                             `..
    decimal
             92   11  140   17    4   40  181   20
             96  201   20
    datetime (unknown)

    body (0)

#### RECORD 60 LowReservoir 2012-08-28T19:11:52 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.8}
```
    op hex (2)
    0000   0x34 0x08                                  4.
    decimal
             52    8
    datetime (2012-08-28T19:11:52)
    0000   0xb4 0x0b 0xb3 0x1c 0x8c                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 61 Bolus 2012-08-28T19:11:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x8c 0x00    ........
    decimal
              1    0  132    0  132    0  140    0
    datetime (2012-08-28T19:11:51)
    0000   0xb3 0x0b 0x53 0x7c 0x0c                   ..S|.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 62 CalBGForPH 2012-08-28T20:01:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 247}
```
    op hex (2)
    0000   0x0a 0xf7                                  ..
    decimal
             10  247
    datetime (2012-08-28T20:01:04)
    0000   0x84 0x01 0x34 0x7c 0x0c                   ..4|.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 63 Ian3F 2012-08-28T20:01:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1e                                  ?.
    decimal
             63   30
    datetime (2012-08-28T20:01:04)
    0000   0x84 0x01 0xf4 0x7c 0x0c                   ...|.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 64 BolusWizard 2012-08-28T20:01:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 22.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 14.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2012-08-28T20:01:12)
    0000   0x8c 0x01 0x14 0x7c 0x0c                   ...|.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x90 0x00    ...n.6..
    0008   0x00 0x00 0x00 0xdc 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54  144    0
              0    0    0  220    0    0   54
    DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 0.1, 'curve': 4},
 {'age': 57, 'amount': 3.2, 'curve': 4},
 {'age': 67, 'amount': 3.5, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x04 0x2f 0x04 0x80 0x39 0x04    \../..9.
    0008   0x8c 0x43 0x04                             .C.
    decimal
             92   11    4   47    4  128   57    4
            140   67    4
    datetime (unknown)

    body (0)

#### RECORD 66 BolusWizard 2012-08-28T21:45:20 head[2], body[15] op[0x5b]
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
    datetime (2012-08-28T21:45:20)
    0000   0x94 0x2d 0x15 0x7c 0x0c                   .-.|.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 151, 'amount': 0.1, 'curve': 4},
 {'age': 161, 'amount': 3.2, 'curve': 4},
 {'age': 171, 'amount': 3.5, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x04 0x97 0x04 0x80 0xa1 0x04    \.......
    0008   0x8c 0xab 0x04                             ...
    decimal
             92   11    4  151    4  128  161    4
            140  171    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2012-08-28T21:45:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x40 0x00    ..l.l.@.
    decimal
              1    0  108    0  108    0   64    0
    datetime (2012-08-28T21:45:20)
    0000   0x94 0x2d 0x55 0x7c 0x0c                   .-U|.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 69 LowReservoir 2012-08-28T23:30:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.1}
```
    op hex (2)
    0000   0x34 0x01                                  4.
    decimal
             52    1
    datetime (2012-08-28T23:30:00)
    0000   0x80 0x1e 0x17 0x1c 0x8c                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 70 BasalProfileStart 2012-08-29T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-29T00:00:00)
    0000   0x80 0x00 0x00 0x1d 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 71 ResultTotals (2000, 8, 0, 0, 12, 28) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x2f                   ..../
    decimal
              7    0    0    6   47
    datetime ((2000, 8, 0, 0, 12, 28))
    0000   0x9c 0x0c 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 72 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x9c 0x0c 0x06 0x00 0xac 0x5f 0xf7    n....._.
    0008   0x05 0x00 0x00 0x06 0x2f 0x03 0x7f 0x39    ..../..9
    0010   0x02 0xb0 0x2b 0x00 0xa1 0x01 0xdc 0x00    ..+.....
    0018   0x00 0x00 0xd4 0x00 0x00 0x04 0x00 0x02    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  156   12    6    0  172   95  247
              5    0    0    6   47    3  127   57
              2  176   43    0  161    1  220    0
              0    0  212    0    0    4    0    2
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 73 CalBGForPH 2012-08-29T00:19:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2012-08-29T00:19:34)
    0000   0xa2 0x13 0x20 0x7d 0x0c                   .. }.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 74 Ian3F 2012-08-29T00:19:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2012-08-29T00:19:34)
    0000   0xa2 0x13 0xe0 0x7d 0x0c                   ...}.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 75 BolusWizard 2012-08-29T00:19:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2012-08-29T00:19:44)
    0000   0xac 0x13 0x00 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    ...n.6$.
    0008   0x00 0x00 0x00 0x20 0x00 0x04 0x36         ... ..6
    decimal
              0  144    0  110   23   54   36    0
              0    0    0   32    0    4   54
    DAY BITS: [0, 1, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 2.7, 'curve': 4},
 {'age': 49, 'amount': 0.1, 'curve': 20},
 {'age': 59, 'amount': 3.2, 'curve': 20},
 {'age': 69, 'amount': 3.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0x9b 0x04 0x04 0x31 0x14    \.l...1.
    0008   0x80 0x3b 0x14 0x8c 0x45 0x14              .;..E.
    decimal
             92   14  108  155    4    4   49   20
            128   59   20  140   69   20
    datetime (unknown)

    body (0)

#### RECORD 77 BolusWizard 2012-08-29T00:19:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2012-08-29T00:19:46)
    0000   0xae 0x13 0x00 0x7d 0x0c                   ...}.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    ...n.6$.
    0008   0x00 0x00 0x00 0x20 0x00 0x04 0x36         ... ..6
    decimal
              0  144    0  110   23   54   36    0
              0    0    0   32    0    4   54
    DAY BITS: [0, 1, 1]
`end analysis/ianj/raw//ReadHistoryData-page-12.data: 78 records`
