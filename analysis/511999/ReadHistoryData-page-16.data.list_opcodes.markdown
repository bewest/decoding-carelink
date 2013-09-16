## START logs/ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 419, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x82 0x5c 0x08 0x40 0x9b 0xd0 0x7c 0xaf    .\.@..|.
    0008   0xd0 0x01 0x00 0x3c 0x00 0x3c 0x00 0x00    ...<.<..
    0010   0x00 0x90 0x0e 0x42 0x02 0x0d 0x7b 0x01    ...B..{.
    0018   0x80 0x00 0x04 0x02 0x0d 0x08 0x21 0x00    ......!.
##### DEBUG DECIMAL
            130   92    8   64  155  208  124  175
            208    1    0   60    0   60    0    0
              0  144   14   66    2   13  123    1
            128    0    4    2   13    8   33    0
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7f 0x8d 0x05 0x00 0x71 0x00 0x00    n....q..
    0008   0x05 0x00 0x00 0x03 0xe2 0x02 0xba 0x46    .......F
    0010   0x01 0x28 0x1e 0x00 0x64 0x01 0x28 0x00    .(..d.(.
    0018   0x00 0x00 0x00 0x00 0x00 0x05 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x66 0x85 0x00 0x00 0x00         ..f....
    decimal
            110  127  141    5    0  113    0    0
              5    0    0    3  226    2  186   70
              1   40   30    0  100    1   40    0
              0    0    0    0    0    5    0    0
              0    0    0    0    0    0    0    0
              0    0  102  133    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

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

#### RECORD 27 ResultTotals (2000, 8, 0, 0, 13, 1) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x94                   .....
    decimal
              7    0    0    4  148
    datetime ((2000, 8, 0, 0, 13, 1))
    0000   0x81 0x0d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x81 0x0d 0x05 0x00 0xe9 0x00 0x00    n.......
    0008   0x05 0x00 0x00 0x04 0x94 0x02 0xb8 0x3b    .......;
    0010   0x01 0xdc 0x29 0x00 0x03 0x00 0x00 0x00    ..).....
    0018   0xe4 0x00 0x3c 0x00 0xbc 0x00 0x02 0x01    ..<.....
    0020   0x02 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x62 0x63 0x00 0x00 0x00 0x00    ..bc....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  129   13    5    0  233    0    0
              5    0    0    4  148    2  184   59
              1  220   41    0    3    0    0    0
            228    0   60    0  188    0    2    1
              2    4    0    0    0    0    0    0
              0    0   98   99    0    0    0    0
              0    0    0

#### RECORD 28 Base (2002, 6, 2, 14, 2, 47) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2002, 6, 2, 14, 2, 47))
    0000   0x6f 0x82 0x0e 0x22 0x02                   o..".
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1]
#### RECORD 29 Base (2002, 6, 2, 14, 16, 47) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2002, 6, 2, 14, 16, 47))
    0000   0x6f 0x90 0x0e 0x02 0x02                   o....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 Base (2014, 4, 28, 24, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x01                                  ..
    decimal
             13    1
    datetime ((2014, 4, 28, 24, 0, 16))
    0000   0x50 0x00 0x78 0x3c 0x6e                   P.x<n
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
`end logs/ReadHistoryData-page-16.data: 31 records`
