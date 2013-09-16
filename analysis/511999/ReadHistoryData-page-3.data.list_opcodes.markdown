## START logs/ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 424, found 99 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x09 0x01 0x8d 0x08 0x29 0x1e 0x0d 0x00    ....)...
    0008   0x1d 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              9    1  141    8   41   30   13    0
             29    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 Bolus 2013-08-29T19:50:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x48 0x00    ..T.T.H.
    decimal
              1    0   84    0   84    0   72    0
    datetime (2013-08-29T19:50:04)
    0000   0x84 0x32 0x53 0x1d 0x0d                   .2S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 BasalProfileStart 2013-08-30T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-30T00:00:00)
    0000   0x80 0x00 0x00 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 2 ResultTotals (2000, 8, 0, 0, 13, 29) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x84                   .....
    decimal
              7    0    0    4  132
    datetime ((2000, 8, 0, 0, 13, 29))
    0000   0x9d 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 3 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x9d 0x0d 0x05 0x00 0xb0 0x00 0x00    n.......
    0008   0x07 0x00 0x00 0x04 0x84 0x02 0xdc 0x3f    .......?
    0010   0x01 0xa8 0x25 0x00 0x42 0x00 0xe4 0x00    ..%.B...
    0018   0xc4 0x00 0x00 0x00 0x00 0x04 0x03 0x00    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0x09 0x00 0x00 0x00         ..d....
    decimal
            110  157   13    5    0  176    0    0
              7    0    0    4  132    2  220   63
              1  168   37    0   66    0  228    0
            196    0    0    0    0    4    3    0
              0    4    0    0    0    0    0    0
              0    0  100    9    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 4 CalBGForPH 2013-08-30T00:57:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-08-30T00:57:06)
    0000   0x86 0x39 0x20 0x1e 0x0d                   .9 ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BolusWizard 2013-08-30T00:57:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 6.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2013-08-30T00:57:09)
    0000   0x89 0x39 0x00 0x1e 0x0d                   .9...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x6e 0x40 0x00    .P.x<n@.
    0008   0x00 0x00 0x00 0x00 0x00 0x40 0x82         .....@.
    decimal
              0   80    0  120   60  110   64    0
              0    0    0    0    0   64  130
    HOUR BITS: [0, 0, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 58, 'amount': 2.1, 'curve': 208},
 {'age': 78, 'amount': 1.9, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x54 0x3a 0xd0 0x4c 0x4e 0xd0    \.T:.LN.
    decimal
             92    8   84   58  208   76   78  208
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-08-30T00:57:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-08-30T00:57:09)
    0000   0x89 0x39 0x40 0x1e 0x0d                   .9@..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 BasalProfileStart 2013-08-30T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-30T04:00:00)
    0000   0x80 0x00 0x04 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 9 CalBGForPH 2013-08-30T04:24:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-08-30T04:24:09)
    0000   0x89 0x18 0x24 0x1e 0x0d                   ..$..
    body (0)

#### RECORD 10 BolusWizard 2013-08-30T04:24:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-30T04:24:57)
    0000   0xb9 0x18 0x04 0x1e 0x0d                   .....
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x3c 0x6e 0x00 0x00    .P.x<n..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x82         P....P.
    decimal
             25   80    0  120   60  110    0    0
             80    0    0    0    0   80  130

#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 1.6, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0xd3 0xc0                   \.@..
    decimal
             92    5   64  211  192
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-08-30T04:24:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-08-30T04:24:57)
    0000   0xb9 0x18 0x44 0x1e 0x0d                   ..D..
    body (0)

#### RECORD 13 BasalProfileStart 2013-08-30T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-30T08:00:00)
    0000   0x80 0x00 0x08 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 14 CalBGForPH 2013-08-30T08:08:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 386}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-08-30T08:08:03)
    0000   0x83 0x08 0x28 0x1e 0x8d                   ..(..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 BolusWizard 2013-08-30T08:08:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 386,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 17.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-08-30T08:08:05)
    0000   0x85 0x08 0x08 0x1e 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0xb0 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x00 0x00 0xb0 0x78         ......x
    decimal
              0   81    0  120   60  100  176    0
              0    0    0    0    0  176  120

#### RECORD 16 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 225, 'amount': 2.0, 'curve': 192},
 {'age': 179, 'amount': 1.6, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0xe1 0xc0 0x40 0xb3 0xd0    \.P..@..
    decimal
             92    8   80  225  192   64  179  208
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-08-30T08:08:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 17.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xb0 0x00 0xb0 0x00 0x00 0x00    ........
    decimal
              1    0  176    0  176    0    0    0
    datetime (2013-08-30T08:08:05)
    0000   0x85 0x08 0x48 0x1e 0x0d                   ..H..
    body (0)

#### RECORD 18 TempBasal 2013-08-30T11:00:38 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.0}
```
    op hex (2)
    0000   0x33 0x50                                  3P
    decimal
             51   80
    datetime (2013-08-30T11:00:38)
    0000   0xa6 0x00 0x0b 0x1e 0x0d                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 19 TempBasalDuration 2013-08-30T11:00:38 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 180}
```
    op hex (2)
    0000   0x16 0x06                                  ..
    decimal
             22    6
    datetime (2013-08-30T11:00:38)
    0000   0xa6 0x00 0x0b 0x1e 0x0d                   .....
    body (0)

#### RECORD 20 TempBasal 2013-08-30T11:02:17 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-08-30T11:02:17)
    0000   0x91 0x02 0x0b 0x1e 0x0d                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 21 TempBasalDuration 2013-08-30T11:02:17 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-08-30T11:02:17)
    0000   0x91 0x02 0x0b 0x1e 0x0d                   .....
    body (0)

#### RECORD 22 BasalProfileStart 2013-08-30T11:02:17 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-30T11:02:17)
    0000   0x91 0x02 0x0b 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 23 ChangeTimeDisplay 2013-08-30T11:02:37 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-08-30T11:02:37)
    0000   0xa5 0x02 0x0b 0x1e 0x0d                   .....
    body (0)

#### RECORD 24 ChangeTime 2013-08-30T11:03:24 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-08-30T11:03:24)
    0000   0x98 0x03 0x0b 0x1e 0x0d                   .....
    body (0)

#### RECORD 25 NewTimeSet 2013-08-30T02:06:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-08-30T02:06:00)
    0000   0x80 0x06 0x02 0x1e 0x0d                   .....
    body (0)

#### RECORD 26 BasalProfileStart 2013-08-30T02:06:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-30T02:06:00)
    0000   0x80 0x06 0x02 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 27 ChangeTimeDisplay 2013-08-30T02:06:16 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-08-30T02:06:16)
    0000   0x90 0x06 0x02 0x1e 0x0d                   .....
    body (0)

#### RECORD 28 ChangeTime 2013-08-30T02:06:21 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-08-30T02:06:21)
    0000   0x95 0x06 0x02 0x1e 0x0d                   .....
    body (0)

#### RECORD 29 NewTimeSet 2013-08-30T02:06:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-08-30T02:06:00)
    0000   0x80 0x06 0x02 0x1e 0x0d                   .....
    body (0)

#### RECORD 30 BasalProfileStart 2013-08-30T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-30T04:00:00)
    0000   0x80 0x00 0x04 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 31 BasalProfileStart 2013-08-30T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-30T08:00:00)
    0000   0x80 0x00 0x08 0x1e 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 32 SelectBasalProfile 2013-08-30T09:08:13 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x00                                  ..
    decimal
             20    0
    datetime (2013-08-30T09:08:13)
    0000   0x8d 0x08 0x29 0x1e 0x0d                   ..)..
    body (0)

#### RECORD 33 ChangeBasalProfile 2013-08-30T09:08:13 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x00                                  ..
    decimal
              8    0
    datetime (2013-08-30T09:08:13)
    0000   0x8d 0x08 0x29 0x1e 0x0d                   ..)..
    body (44)
    hex
    0000   0x3f 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ?.......
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00                        ....
    decimal
             63    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0

`end logs/ReadHistoryData-page-3.data: 34 records`
