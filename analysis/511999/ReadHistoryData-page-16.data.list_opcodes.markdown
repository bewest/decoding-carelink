## START analysis/sarak/raw//ReadHistoryData-page-16.data
ERROR day is out of range for month 0000   0x7f 0x8d                                  ..
#### STOPPING DOUBLE NULLS @ 1008, found 14 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xf2 0xfa                                  ..
##### DEBUG DECIMAL
            242  250
ERROR day is out of range for month 0000   0x7f 0x8d                                  ..
#### RECORD 0 Sara6E (2013, 7, 32, 0, 0, 0) head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime ((2013, 7, 32, 0, 0, 0))
    0000   0x7f 0x8d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0x71 0x00 0x00 0x05 0x00 0x00    ..q.....
    0008   0x03 0xe2 0x02 0xba 0x46 0x01 0x28 0x1e    ....F.(.
    0010   0x00 0x64 0x01 0x28 0x00 0x00 0x00 0x00    .d.(....
    0018   0x00 0x00 0x05 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x66    .......f
    0028   0x85 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  113    0    0    5    0    0
              3  226    2  186   70    1   40   30
              0  100    1   40    0    0    0    0
              0    0    5    0    0    0    0    0
              0    0    0    0    0    0    0  102
            133    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 BasalProfileStart 2013-08-01T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-01T04:00:00)
    0000   0x80 0x00 0x04 0x01 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 2 BasalProfileStart 2013-08-01T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-01T08:00:00)
    0000   0x80 0x00 0x08 0x01 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 3 TempBasal 2013-08-01T09:25:45 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.0}
```
    op hex (2)
    0000   0x33 0x50                                  3P
    decimal
             51   80
    datetime (2013-08-01T09:25:45)
    0000   0xad 0x19 0x09 0x01 0x0d                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 4 TempBasalDuration 2013-08-01T09:25:45 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 1440}
```
    op hex (2)
    0000   0x16 0x30                                  .0
    decimal
             22   48
    datetime (2013-08-01T09:25:45)
    0000   0xad 0x19 0x09 0x01 0x0d                   .....
    body (0)

#### RECORD 5 CalBGForPH 2013-08-01T12:51:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 316}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2013-08-01T12:51:58)
    0000   0xba 0x33 0x2c 0x01 0x8d                   .3,..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 6 BolusWizard 2013-08-01T12:52:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 316,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 12.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3c                                  [<
    decimal
             91   60
    datetime (2013-08-01T12:52:01)
    0000   0x81 0x34 0x0c 0x61 0x0d                   .4.a.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x80 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x00 0x00 0x80 0x78         ......x
    decimal
              0   81    0  120   60  100  128    0
              0    0    0    0    0  128  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 Bolus 2013-08-01T12:52:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x00 0x00    ........
    decimal
              1    0  128    0  128    0    0    0
    datetime (2013-08-01T12:52:01)
    0000   0x81 0x34 0x4c 0x61 0x0d                   .4La.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 TempBasal 2013-08-01T12:54:24 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-08-01T12:54:24)
    0000   0x98 0x36 0x0c 0x01 0x0d                   .6...
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [0, 0, 1]
#### RECORD 9 TempBasalDuration 2013-08-01T12:54:24 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-08-01T12:54:24)
    0000   0x98 0x36 0x0c 0x01 0x0d                   .6...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 10 BasalProfileStart 2013-08-01T12:54:24 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-01T12:54:24)
    0000   0x98 0x36 0x0c 0x01 0x0d                   .6...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 0, 1]
#### RECORD 11 TempBasal 2013-08-01T14:50:56 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.025}
```
    op hex (2)
    0000   0x33 0x51                                  3Q
    decimal
             51   81
    datetime (2013-08-01T14:50:56)
    0000   0xb8 0x32 0x0e 0x01 0x0d                   .2...
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [0, 0, 1]
#### RECORD 12 TempBasalDuration 2013-08-01T14:50:56 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 120}
```
    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2013-08-01T14:50:56)
    0000   0xb8 0x32 0x0e 0x01 0x0d                   .2...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 BasalProfileStart 2013-08-01T16:50:56 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-01T16:50:56)
    0000   0xb8 0x32 0x10 0x01 0x0d                   .2...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 0, 1]
#### RECORD 14 CalBGForPH 2013-08-01T17:52:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-08-01T17:52:14)
    0000   0x8e 0x34 0x31 0x01 0x0d                   .41..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 BolusWizard 2013-08-01T17:52:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 101,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 3,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 12}
```
    op hex (2)
    0000   0x5b 0x65                                  [e
    decimal
             91  101
    datetime (2013-08-01T17:52:21)
    0000   0x95 0x34 0x11 0x61 0x0d                   .4.a.
    body (15)
    hex
    0000   0x03 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x0c 0x00 0x00 0x00 0x00 0x0c 0x78         ......x
    decimal
              3   80    0  100   60  100    0    0
             12    0    0    0    0   12  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 1.75, 'curve': 208},
 {'age': 53, 'amount': 1.45, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x46 0x2b 0xd0 0x3a 0x35 0xd0    \.F+.:5.
    decimal
             92    8   70   43  208   58   53  208
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-08-01T17:52:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2013-08-01T17:52:21)
    0000   0x95 0x34 0x51 0x61 0x0d                   .4Qa.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 CalBGForPH 2013-08-01T18:16:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 355}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2013-08-01T18:16:23)
    0000   0x97 0x10 0x32 0x01 0x8d                   ..2..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 19 BolusWizard 2013-08-01T18:16:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 355,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 15.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x63                                  [c
    decimal
             91   99
    datetime (2013-08-01T18:16:25)
    0000   0x99 0x10 0x12 0x61 0x0d                   ...a.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x9c 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0x38 0x00 0x64 0x78         ...8.dx
    decimal
              0   81    0  100   60  100  156    0
              0    0    0   56    0  100  120
    DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 0.5, 'curve': 192},
 {'age': 33, 'amount': 1.0, 'curve': 192},
 {'age': 67, 'amount': 1.75, 'curve': 208},
 {'age': 77, 'amount': 1.45, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x14 0x17 0xc0 0x28 0x21 0xc0    \....(!.
    0008   0x46 0x43 0xd0 0x3a 0x4d 0xd0              FC.:M.
    decimal
             92   14   20   23  192   40   33  192
             70   67  208   58   77  208
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-08-01T18:16:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x38 0x00    ..d.d.8.
    decimal
              1    0  100    0  100    0   56    0
    datetime (2013-08-01T18:16:25)
    0000   0x99 0x10 0x52 0x61 0x0d                   ..Ra.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 22 CalBGForPH 2013-08-01T18:56:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 296}
```
    op hex (2)
    0000   0x0a 0x28                                  .(
    decimal
             10   40
    datetime (2013-08-01T18:56:49)
    0000   0xb1 0x38 0x32 0x01 0x8d                   .82..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 23 Bolus 2013-08-01T19:06:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x70 0x00    ..|.|.p.
    decimal
              1    0  124    0  124    0  112    0
    datetime (2013-08-01T19:06:24)
    0000   0x98 0x06 0x53 0x01 0x0d                   ..S..
    body (0)

#### RECORD 24 Bolus 2013-08-01T19:23:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0xd0 0x00    ..@.@...
    decimal
              1    0   64    0   64    0  208    0
    datetime (2013-08-01T19:23:21)
    0000   0x95 0x17 0x53 0x01 0x0d                   ..S..
    body (0)

#### RECORD 25 CalBGForPH 2013-08-01T22:04:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2013-08-01T22:04:27)
    0000   0x9b 0x04 0x36 0x01 0x0d                   ..6..
    body (0)

#### RECORD 26 BasalProfileStart 2013-08-02T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-02T00:00:00)
    0000   0x80 0x00 0x00 0x02 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 27 MResultTotals 2013-08-02T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x94                   .....
    decimal
              7    0    0    4  148
    datetime (2013-08-02T00:00:00)
    0000   0x81 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 28 Sara6E 2013-08-02T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-02T00:00:00)
    0000   0x81 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0xe9 0x00 0x00 0x05 0x00 0x00    ........
    0008   0x04 0x94 0x02 0xb8 0x3b 0x01 0xdc 0x29    ....;..)
    0010   0x00 0x03 0x00 0x00 0x00 0xe4 0x00 0x3c    .......<
    0018   0x00 0xbc 0x00 0x02 0x01 0x02 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x62    .......b
    0028   0x63 0x00 0x00 0x00 0x00 0x00 0x00 0x00    c.......
    0030   0x00                                       .
    decimal
              5    0  233    0    0    5    0    0
              4  148    2  184   59    1  220   41
              0    3    0    0    0  228    0   60
              0  188    0    2    1    2    4    0
              0    0    0    0    0    0    0   98
             99    0    0    0    0    0    0    0
              0

#### RECORD 29 CalBGForPH 2013-08-02T02:14:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-08-02T02:14:02)
    0000   0x82 0x0e 0x22 0x02 0x0d                   .."..
    body (0)

#### RECORD 30 BolusWizard 2013-08-02T02:14:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 1,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-08-02T02:14:16)
    0000   0x90 0x0e 0x02 0x02 0x0d                   .....
    body (15)
    hex
    0000   0x01 0x50 0x00 0x78 0x3c 0x6e 0x00 0x00    .P.x<n..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x82         .......
    decimal
              1   80    0  120   60  110    0    0
              0    0    0    0    0    0  130

#### RECORD 31 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.6, 'curve': 208},
 {'age': 175, 'amount': 3.1, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x9b 0xd0 0x7c 0xaf 0xd0    \.@..|..
    decimal
             92    8   64  155  208  124  175  208
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-08-02T02:14:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2013-08-02T02:14:16)
    0000   0x90 0x0e 0x42 0x02 0x0d                   ..B..
    body (0)

#### RECORD 33 BasalProfileStart 2013-08-02T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-02T04:00:00)
    0000   0x80 0x00 0x04 0x02 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 34 BasalProfileStart 2013-08-02T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-02T08:00:00)
    0000   0x80 0x00 0x08 0x02 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 35 CalBGForPH 2013-08-02T10:37:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-08-02T10:37:47)
    0000   0xaf 0x25 0x2a 0x02 0x0d                   .%*..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 CalBGForPH 2013-08-02T10:38:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2013-08-02T10:38:48)
    0000   0xb0 0x26 0x2a 0x02 0x0d                   .&*..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 CalBGForPH 2013-08-02T10:38:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2013-08-02T10:38:58)
    0000   0xba 0x26 0x2a 0x02 0x0d                   .&*..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 38 BolusWizard 2013-08-02T10:39:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 169,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 60,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 200}
```
    op hex (2)
    0000   0x5b 0xa9                                  [.
    decimal
             91  169
    datetime (2013-08-02T10:39:28)
    0000   0x9c 0x27 0x0a 0x02 0x0d                   .'...
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x78 0x3c 0x64 0x20 0x00    <P.x<d .
    0008   0xc8 0x00 0x00 0x00 0x00 0xe8 0x78         ......x
    decimal
             60   80    0  120   60  100   32    0
            200    0    0    0    0  232  120
    HOUR BITS: [0, 0, 1]
#### RECORD 39 Bolus 2013-08-02T10:39:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-08-02T10:39:28)
    0000   0x9c 0x27 0x4a 0x02 0x0d                   .'J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 Bolus 2013-08-02T11:50:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x30 0x00    ......0.
    decimal
              1    0   28    0   28    0   48    0
    datetime (2013-08-02T11:50:13)
    0000   0x8d 0x32 0x4b 0x02 0x0d                   .2K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 BasalProfileStart 2013-08-02T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-02T12:00:00)
    0000   0x80 0x00 0x0c 0x02 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 42 Bolus 2013-08-02T12:16:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x38 0x00    ..H.H.8.
    decimal
              1    0   72    0   72    0   56    0
    datetime (2013-08-02T12:16:56)
    0000   0xb8 0x10 0x4c 0x02 0x0d                   ..L..
    body (0)

#### RECORD 43 CalBGForPH 2013-08-02T14:58:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-02T14:58:04)
    0000   0x84 0x3a 0x2e 0x02 0x0d                   .:...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 44 BolusWizard 2013-08-02T14:58:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-02T14:58:11)
    0000   0x8b 0x3a 0x0e 0x62 0x0d                   .:.b.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x08 0x00 0x00 0x78         ......x
    decimal
              0   80    0  120   60  100    0    0
              0    0    0    8    0    0  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 165, 'amount': 1.8, 'curve': 192},
 {'age': 195, 'amount': 0.7, 'curve': 192},
 {'age': 9, 'amount': 2.0, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0xa5 0xc0 0x1c 0xc3 0xc0    \.H.....
    0008   0x50 0x09 0xd0                             P..
    decimal
             92   11   72  165  192   28  195  192
             80    9  208
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-08-02T14:58:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x08 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    8    0
    datetime (2013-08-02T14:58:11)
    0000   0x8b 0x3a 0x4e 0x62 0x0d                   .:Nb.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 LowReservoir 2013-08-02T15:16:33 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-02T15:16:33)
    0000   0xa1 0x10 0x0f 0x02 0x0d                   .....
    body (0)

#### RECORD 48 Rewind 2013-08-02T16:34:16 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-02T16:34:16)
    0000   0x90 0x22 0x10 0x02 0x0d                   ."...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 Prime 2013-08-02T16:40:21 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 20.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0xc9                   .....
    decimal
              3    0    0    0  201
    datetime (2013-08-02T16:40:21)
    0000   0x95 0x28 0x30 0x02 0x0d                   .(0..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 BasalProfileStart 2013-08-02T16:41:37 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-02T16:41:37)
    0000   0xa5 0x29 0x10 0x02 0x0d                   .)...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 0, 1]
#### RECORD 51 Prime 2013-08-02T16:41:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-02T16:41:03)
    0000   0x83 0x29 0x10 0x02 0x0d                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 52 CalBGForPH 2013-08-02T16:57:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 298}
```
    op hex (2)
    0000   0x0a 0x2a                                  .*
    decimal
             10   42
    datetime (2013-08-02T16:57:22)
    0000   0x96 0x39 0x30 0x02 0x8d                   .90..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 53 BolusWizard 2013-08-02T16:57:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 298,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 11.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2a                                  [*
    decimal
             91   42
    datetime (2013-08-02T16:57:25)
    0000   0x99 0x39 0x10 0x02 0x0d                   .9...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x74 0x00    .Q.x<dt.
    0008   0x00 0x00 0x00 0x10 0x00 0x64 0x78         .....dx
    decimal
              0   81    0  120   60  100  116    0
              0    0    0   16    0  100  120
    HOUR BITS: [0, 0, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 1.5, 'curve': 192},
 {'age': 28, 'amount': 1.8, 'curve': 208},
 {'age': 58, 'amount': 0.7, 'curve': 208},
 {'age': 128, 'amount': 2.0, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0x7c 0xc0 0x48 0x1c 0xd0    \.<|.H..
    0008   0x1c 0x3a 0xd0 0x50 0x80 0xd0              .:.P..
    decimal
             92   14   60  124  192   72   28  208
             28   58  208   80  128  208
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-08-02T16:57:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x10 0x00    ..d.d...
    decimal
              1    0  100    0  100    0   16    0
    datetime (2013-08-02T16:57:25)
    0000   0x99 0x39 0x50 0x02 0x0d                   .9P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 CalBGForPH 2013-08-02T19:12:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-08-02T19:12:01)
    0000   0x81 0x0c 0x33 0x02 0x0d                   ..3..
    body (0)

#### RECORD 57 BolusWizard 2013-08-02T19:12:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 124,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x7c                                  [|
    decimal
             91  124
    datetime (2013-08-02T19:12:12)
    0000   0x8c 0x0c 0x13 0x62 0x0d                   ...b.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x78 0x00 0x00 0x10 0x00 0x78 0x78         x....xx
    decimal
             30   80    0  100   60  100    0    0
            120    0    0   16    0  120  120
    DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 2.5, 'curve': 192},
 {'age': 3, 'amount': 1.5, 'curve': 208},
 {'age': 163, 'amount': 1.8, 'curve': 208},
 {'age': 193, 'amount': 0.7, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x64 0x8b 0xc0 0x3c 0x03 0xd0    \.d..<..
    0008   0x48 0xa3 0xd0 0x1c 0xc1 0xd0              H.....
    decimal
             92   14  100  139  192   60    3  208
             72  163  208   28  193  208
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-08-02T19:12:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x10 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   16    0
    datetime (2013-08-02T19:12:12)
    0000   0x8c 0x0c 0x53 0x62 0x0d                   ..Sb.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 60 Bolus 2013-08-02T19:43:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x74 0x00    ..(.(.t.
    decimal
              1    0   40    0   40    0  116    0
    datetime (2013-08-02T19:43:49)
    0000   0xb1 0x2b 0x53 0x02 0x0d                   .+S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 BasalProfileStart 2013-08-03T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-03T00:00:00)
    0000   0x80 0x00 0x00 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 62 MResultTotals 2013-08-03T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime (2013-08-03T00:00:00)
    0000   0x82 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 63 Sara6E 2013-08-03T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-03T00:00:00)
    0000   0x82 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0x9a 0x00 0x00 0x07 0x00 0x00    ........
    0008   0x05 0x08 0x02 0xd8 0x39 0x02 0x30 0x2b    ....9.0+
    0010   0x00 0x5b 0x00 0xc8 0x00 0xdc 0x00 0x00    .[......
    0018   0x00 0x8c 0x02 0x03 0x00 0x03 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x64    .......d
    0028   0x2a 0x00 0x00 0x00 0x00 0x00 0x00 0x00    *.......
    0030   0x00                                       .
    decimal
              5    0  154    0    0    7    0    0
              5    8    2  216   57    2   48   43
              0   91    0  200    0  220    0    0
              0  140    2    3    0    3    4    0
              0    0    0    0    0    0    0  100
             42    0    0    0    0    0    0    0
              0

#### RECORD 64 Bolus 2013-08-03T00:53:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-03T00:53:10)
    0000   0x8a 0x35 0x40 0x03 0x0d                   .5@..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 65 BasalProfileStart 2013-08-03T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-03T04:00:00)
    0000   0x80 0x00 0x04 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 66 TempBasal 2013-08-03T06:51:42 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.25}
```
    op hex (2)
    0000   0x33 0x5a                                  3Z
    decimal
             51   90
    datetime (2013-08-03T06:51:42)
    0000   0xaa 0x33 0x06 0x03 0x0d                   .3...
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [0, 0, 1]
#### RECORD 67 TempBasalDuration 2013-08-03T06:51:42 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 660}
```
    op hex (2)
    0000   0x16 0x16                                  ..
    decimal
             22   22
    datetime (2013-08-03T06:51:42)
    0000   0xaa 0x33 0x06 0x03 0x0d                   .3...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 68 Bolus 2013-08-03T09:10:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-03T09:10:17)
    0000   0x91 0x0a 0x49 0x03 0x0d                   ..I..
    body (0)

#### RECORD 69 TempBasal 2013-08-03T11:00:37 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-08-03T11:00:37)
    0000   0xa5 0x00 0x0b 0x03 0x0d                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 70 TempBasalDuration 2013-08-03T11:00:37 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-08-03T11:00:37)
    0000   0xa5 0x00 0x0b 0x03 0x0d                   .....
    body (0)

#### RECORD 71 BasalProfileStart 2013-08-03T11:00:37 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-03T11:00:37)
    0000   0xa5 0x00 0x0b 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 72 BasalProfileStart 2013-08-03T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-03T12:00:00)
    0000   0x80 0x00 0x0c 0x03 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 73 CalBGForPH 2013-08-03T12:28:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2013-08-03T12:28:21)
    0000   0x95 0x1c 0x2c 0x03 0x0d                   ..,..
    body (0)

#### RECORD 74 BolusWizard 2013-08-03T12:28:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 215,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0xd7                                  [.
    decimal
             91  215
    datetime (2013-08-03T12:28:35)
    0000   0xa3 0x1c 0x0c 0x03 0x0d                   .....
    body (15)
    hex
    0000   0x1c 0x50 0x00 0x78 0x3c 0x64 0x3c 0x00    .P.x<d<.
    0008   0x5c 0x00 0x00 0x00 0x00 0x98 0x78         \.....x
    decimal
             28   80    0  120   60  100   60    0
             92    0    0    0    0  152  120

#### RECORD 75 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 205, 'amount': 1.4, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0xcd 0xc0                   \.8..
    decimal
             92    5   56  205  192
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2013-08-03T12:28:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x98 0x00 0x98 0x00 0x00 0x00    ........
    decimal
              1    0  152    0  152    0    0    0
    datetime (2013-08-03T12:28:35)
    0000   0xa3 0x1c 0x4c 0x03 0x0d                   ..L..
    body (0)

#### RECORD 77 Bolus 2013-08-03T15:52:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2013-08-03T15:52:38)
    0000   0xa6 0x34 0x4f 0x03 0x0d                   .4O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 78 CalBGForPH 2013-08-03T17:45:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-08-03T17:45:01)
    0000   0x81 0x2d 0x31 0x03 0x0d                   .-1..
    body (0)
    HOUR BITS: [0, 0, 1]
`end analysis/sarak/raw//ReadHistoryData-page-16.data: 79 records`
