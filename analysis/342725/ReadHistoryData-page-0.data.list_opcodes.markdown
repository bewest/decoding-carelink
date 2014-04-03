## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 614, found 408 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc0 0x0e                                  ..
##### DEBUG DECIMAL
            192   14
#### RECORD 0 BasalProfileStart 2014-03-16T15:53:40 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T15:53:40)
    0000   0x28 0xf5 0x0f 0x10 0x0e                   (....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 1 PumpSuspend 2014-03-16T15:55:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T15:55:20)
    0000   0x14 0xf7 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 2 PumpResume 2014-03-16T15:56:22 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T15:56:22)
    0000   0x16 0xf8 0x0f 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 3 BasalProfileStart 2014-03-16T15:56:22 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T15:56:22)
    0000   0x16 0xf8 0x0f 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 4 PumpSuspend 2014-03-16T16:05:14 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-16T16:05:14)
    0000   0x0e 0xc5 0x10 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 5 PumpResume 2014-03-16T16:06:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-16T16:06:31)
    0000   0x1f 0xc6 0x10 0x50 0x0e                   ...P.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 6 BasalProfileStart 2014-03-16T16:06:31 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T16:06:31)
    0000   0x1f 0xc6 0x10 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2014-03-16T18:32:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2014-03-16T18:32:15)
    0000   0x0f 0xe0 0x32 0x70 0x0e                   ..2p.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2014-03-16T18:32:15 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-03-16T18:32:15)
    0000   0x0f 0xe0 0xf2 0x70 0x0e                   ...p.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 CalBGForPH 2014-03-16T18:52:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2014-03-16T18:52:26)
    0000   0x1a 0xf4 0x32 0x10 0x0e                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 BolusWizard 2014-03-16T18:52:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 3.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2014-03-16T18:52:29)
    0000   0x1d 0xf4 0x12 0x10 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x20 0x00    .P.x2P .
    0008   0x00 0x00 0x00 0x00 0x00 0x20 0x64         ..... d
    decimal
              0   80    0  120   50   80   32    0
              0    0    0    0    0   32  100
    HOUR BITS: [1, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 6.3, 'curve': 144}]
```
    op hex (5)
    0000   0x5c 0x05 0xfc 0x68 0x90                   \..h.
    decimal
             92    5  252  104  144
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2014-03-16T18:52:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x00 0x00    .. . ...
    decimal
              1    0   32    0   32    0    0    0
    datetime (2014-03-16T18:52:29)
    0000   0x1d 0xf4 0x52 0x10 0x0e                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 BolusWizard 2014-03-16T19:00:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 3.2,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 3.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2014-03-16T19:00:30)
    0000   0x1e 0xc0 0x13 0x70 0x0e                   ...p.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x6e 0x32 0x50 0x20 0x00    .P.n2P .
    0008   0x50 0x00 0x00 0x20 0x00 0x50 0x64         P.. .Pd
    decimal
             22   80    0  110   50   80   32    0
             80    0    0   32    0   80  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.8, 'curve': 128},
 {'age': 112, 'amount': 6.3, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x08 0x80 0xfc 0x70 0x90    \. ...p.
    decimal
             92    8   32    8  128  252  112  144
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2014-03-16T19:00:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x20 0x00    ..P.P. .
    decimal
              1    0   80    0   80    0   32    0
    datetime (2014-03-16T19:00:30)
    0000   0x1e 0xc0 0x53 0x70 0x0e                   ..Sp.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2014-03-16T19:54:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 60,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 216}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-16T19:54:15)
    0000   0x0f 0xf6 0x13 0x70 0x0e                   ...p.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    <P.n2P..
    0008   0xd8 0x00 0x00 0x00 0x00 0xd8 0x64         ......d
    decimal
             60   80    0  110   50   80    0    0
            216    0    0    0    0  216  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 62, 'amount': 2.8, 'curve': 128},
 {'age': 166, 'amount': 6.3, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x70 0x3e 0x80 0xfc 0xa6 0x90    \.p>....
    decimal
             92    8  112   62  128  252  166  144
    datetime (unknown)

    body (0)

#### RECORD 18 LowReservoir 2014-03-16T19:54:27 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-03-16T19:54:27)
    0000   0x1b 0xf6 0x13 0x10 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 Bolus 2014-03-16T19:54:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 21.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xd8 0x00 0xd8 0x00 0x34 0x00    ......4.
    decimal
              1    0  216    0  216    0   52    0
    datetime (2014-03-16T19:54:15)
    0000   0x0f 0xf6 0x53 0x70 0x0e                   ..Sp.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 NoDelivery 2014-03-16T20:31:28 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x3b 0x01 0x08                        .;..
    decimal
              6   59    1    8
    datetime (2014-03-16T20:31:28)
    0000   0x1c 0xdf 0x74 0xd0 0x0e                   ..t..
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [1, 1, 0]
#### RECORD 21 ClearAlarm 2014-03-16T20:42:14 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x3b                                  .;
    decimal
             12   59
    datetime (2014-03-16T20:42:14)
    0000   0x0e 0xea 0x14 0x10 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 22 BasalProfileStart 2014-03-16T20:42:15 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-16T20:42:15)
    0000   0x0f 0xea 0x14 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 23 BasalProfileStart 2014-03-16T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-16T22:30:00)
    0000   0x00 0xde 0x16 0x10 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 24 CalBGForPH 2014-03-16T23:56:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 179}
```
    op hex (2)
    0000   0x0a 0xb3                                  ..
    decimal
             10  179
    datetime (2014-03-16T23:56:43)
    0000   0x2b 0xf8 0x37 0x70 0x0e                   +.7p.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 Ian3F 2014-03-16T23:56:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2014-03-16T23:56:43)
    0000   0x2b 0xf8 0x77 0x70 0x0e                   +.wp.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2014-03-16T23:56:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 179,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb3                                  [.
    decimal
             91  179
    datetime (2014-03-16T23:56:54)
    0000   0x36 0xf8 0x17 0x10 0x0e                   6....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x38 0x00    .P.n7P8.
    0008   0x00 0x00 0x00 0x00 0x00 0x38 0x64         .....8d
    decimal
              0   80    0  110   55   80   56    0
              0    0    0    0    0   56  100
    HOUR BITS: [1, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 244, 'amount': 5.4, 'curve': 128},
 {'age': 48, 'amount': 2.8, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0xd8 0xf4 0x80 0x70 0x30 0x90    \....p0.
    decimal
             92    8  216  244  128  112   48  144
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2014-03-16T23:56:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    0    0
    datetime (2014-03-16T23:56:54)
    0000   0x36 0xf8 0x57 0x10 0x0e                   6.W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 29 BasalProfileStart 2014-03-17T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-17T00:00:00)
    0000   0x00 0xc0 0x00 0x11 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 30 MResultTotals 2014-03-17T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x7a                   ....z
    decimal
              7    0    0    4  122
    datetime (2014-03-17T00:00:00)
    0000   0x30 0x8e                                  0.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 31 Sara6E 2014-03-17T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-17T00:00:00)
    0000   0x30 0x8e                                  0.
    body (49)
    hex
    0000   0x05 0x00 0x94 0x8f 0xb3 0x04 0x00 0x00    ........
    0008   0x04 0x7a 0x01 0xde 0x2a 0x02 0x9c 0x3a    .z..*..:
    0010   0x00 0x98 0x01 0x28 0x00 0x78 0x00 0xfc    ...(.x..
    0018   0x00 0x00 0x02 0x02 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x80    ........
    0028   0x8f 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  148  143  179    4    0    0
              4  122    1  222   42    2  156   58
              0  152    1   40    0  120    0  252
              0    0    2    2    1    0    0    0
              0    0    0    0    0    0    0  128
            143    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 32 CalBGForPH 2014-03-17T01:01:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2014-03-17T01:01:29)
    0000   0x1d 0xc1 0x21 0x11 0x0e                   ..!..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 BolusWizard 2014-03-17T01:01:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 172,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2014-03-17T01:01:33)
    0000   0x21 0xc1 0x01 0x71 0x0e                   !..q.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x34 0x00    .P.n7P4.
    0008   0x00 0x00 0x00 0x20 0x00 0x14 0x64         ... ..d
    decimal
              0   80    0  110   55   80   52    0
              0    0    0   32    0   20  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 2.2, 'curve': 128},
 {'age': 53, 'amount': 5.4, 'curve': 144},
 {'age': 113, 'amount': 2.8, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x45 0x80 0xd8 0x35 0x90    \.XE..5.
    0008   0x70 0x71 0x90                             pq.
    decimal
             92   11   88   69  128  216   53  144
            112  113  144
    datetime (unknown)

    body (0)

#### RECORD 35 LowReservoir 2014-03-17T01:01:49 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-03-17T01:01:49)
    0000   0x31 0xc1 0x01 0x11 0x0e                   1....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 Bolus 2014-03-17T01:01:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x20 0x00    ..(.(. .
    decimal
              1    0   40    0   40    0   32    0
    datetime (2014-03-17T01:01:33)
    0000   0x21 0xc1 0x41 0x71 0x0e                   !.Aq.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 BasalProfileStart 2014-03-17T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-17T02:00:00)
    0000   0x00 0xc0 0x02 0x11 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 38 BasalProfileStart 2014-03-17T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-17T04:00:00)
    0000   0x00 0xc0 0x04 0x11 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 39 BasalProfileStart 2014-03-17T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-17T06:00:00)
    0000   0x00 0xc0 0x06 0x11 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 40 CalBGForPH 2014-03-17T07:56:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2014-03-17T07:56:33)
    0000   0x21 0xf8 0x27 0x71 0x0e                   !.'q.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2014-03-17T07:56:33 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-03-17T07:56:33)
    0000   0x21 0xf8 0xc7 0x71 0x0e                   !..q.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 BasalProfileStart 2014-03-17T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-17T10:30:00)
    0000   0x00 0xde 0x0a 0x11 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 43 PumpSuspend 2014-03-17T11:26:16 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-17T11:26:16)
    0000   0x10 0xda 0x0b 0x51 0x0e                   ...Q.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 44 PumpResume 2014-03-17T11:26:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-17T11:26:58)
    0000   0x3a 0xda 0x0b 0x51 0x0e                   :..Q.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 45 BasalProfileStart 2014-03-17T11:26:58 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-17T11:26:58)
    0000   0x3a 0xda 0x0b 0x11 0x0e                   :....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 46 BolusWizard 2014-03-17T13:34:27 head[2], body[15] op[0x5b]
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
    datetime (2014-03-17T13:34:27)
    0000   0x1b 0xe2 0x0d 0x71 0x0e                   ...q.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x78 0x32 0x50 0x00 0x00    #P.x2P..
    0008   0x74 0x00 0x00 0x00 0x00 0x74 0x64         t....td
    decimal
             35   80    0  120   50   80    0    0
            116    0    0    0    0  116  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 Bolus 2014-03-17T13:34:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2014-03-17T13:34:27)
    0000   0x1b 0xe2 0x4d 0x71 0x0e                   ..Mq.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2014-03-17T15:07:10 head[2], body[15] op[0x5b]
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
    datetime (2014-03-17T15:07:10)
    0000   0x0a 0xc7 0x0f 0x71 0x0e                   ...q.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x64         d....dd
    decimal
             30   80    0  120   50   80    0    0
            100    0    0    0    0  100  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 95, 'amount': 2.9, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0x5f 0x80                   \.t_.
    decimal
             92    5  116   95  128
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2014-03-17T15:07:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x14 0x00    ..d.d...
    decimal
              1    0  100    0  100    0   20    0
    datetime (2014-03-17T15:07:10)
    0000   0x0a 0xc7 0x4f 0x71 0x0e                   ..Oq.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 Bolus 2014-03-17T15:59:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x08 0x00 0x08 0x00 0x34 0x00    ......4.
    decimal
              1    0    8    0    8    0   52    0
    datetime (2014-03-17T15:59:00)
    0000   0x00 0xfb 0x4f 0x71 0x0e                   ..Oq.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-0.data: 52 records`
