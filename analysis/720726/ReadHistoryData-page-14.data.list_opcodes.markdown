## START analysis/ianj/raw/ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xd0 0xd3                                  ..
##### DEBUG DECIMAL
            208  211
#### RECORD 0 BasalProfileStart 2012-08-24T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-24T09:30:00)
    0000   0x80 0x1e 0x09 0x18 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 1 CalBGForPH 2012-08-24T09:35:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2012-08-24T09:35:06)
    0000   0x86 0x23 0x29 0x78 0x0c                   .#)x.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2012-08-24T09:35:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2012-08-24T09:35:06)
    0000   0x86 0x23 0x69 0x78 0x0c                   .#ix.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 NoDelivery 2012-08-24T09:39:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2012-08-24T09:39:00)
    0000   0x80 0x27 0x49 0xb8 0x0c                   .'I..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1]
#### RECORD 4 ClearAlarm 2012-08-24T09:41:08 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2012-08-24T09:41:08)
    0000   0x88 0x29 0x09 0x18 0x0c                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BasalProfileStart 2012-08-24T09:41:08 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-24T09:41:08)
    0000   0x88 0x29 0x09 0x18 0x0c                   .)...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 0, 1]
#### RECORD 6 CalBGForPH 2012-08-24T10:04:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 62}
```
    op hex (2)
    0000   0x0a 0x3e                                  .>
    decimal
             10   62
    datetime (2012-08-24T10:04:40)
    0000   0xa8 0x04 0x2a 0x78 0x0c                   ..*x.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2012-08-24T10:04:40 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2012-08-24T10:04:40)
    0000   0xa8 0x04 0xca 0x78 0x0c                   ...x.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 8 BolusWizard 2012-08-24T10:10:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 34,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 22.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x22                                  ["
    decimal
             91   34
    datetime (2012-08-24T10:10:04)
    0000   0x84 0x0a 0x0a 0x78 0x0c                   ...x.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0xdc 0x00    ...n.6..
    0008   0x64 0xf8 0x00 0x00 0x00 0x40 0x36         d....@6
    decimal
             28  144    0  110   23   54  220    0
            100  248    0    0    0   64   54
    DAY BITS: [0, 1, 1]
#### RECORD 9 Ian69 2012-08-24T10:10:04 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-24T10:10:04)
    0000   0x84 0x0a 0x0a 0x18 0x0c                   .....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30

#### RECORD 10 Bolus 2012-08-24T10:10:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2012-08-24T10:10:04)
    0000   0x84 0x0a 0x4a 0x78 0x0c                   ..Jx.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 11 BolusWizard 2012-08-24T10:45:18 head[2], body[15] op[0x5b]
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
    datetime (2012-08-24T10:45:18)
    0000   0x92 0x2d 0x0a 0x78 0x0c                   .-.x.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 1.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x29 0x04                   \.@).
    decimal
             92    5   64   41    4
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2012-08-24T10:45:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x3c 0x00    ..P.P.<.
    decimal
              1    0   80    0   80    0   60    0
    datetime (2012-08-24T10:45:19)
    0000   0x93 0x2d 0x4a 0x78 0x0c                   .-Jx.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 CalBGForPH 2012-08-24T11:44:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 249}
```
    op hex (2)
    0000   0x0a 0xf9                                  ..
    decimal
             10  249
    datetime (2012-08-24T11:44:34)
    0000   0xa2 0x2c 0x2b 0x78 0x0c                   .,+x.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 15 Ian3F 2012-08-24T11:44:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1f                                  ?.
    decimal
             63   31
    datetime (2012-08-24T11:44:34)
    0000   0xa2 0x2c 0x2b 0x78 0x0c                   .,+x.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2012-08-24T11:44:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 138,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 10.4,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 14.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x8a                                  [.
    decimal
             91  138
    datetime (2012-08-24T11:44:51)
    0000   0xb3 0x2c 0x0b 0x78 0x0c                   .,.x.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x90 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x68 0x00 0x90 0x36         h..h..6
    decimal
             29  144    0  110   23   54  144    0
            104    0    0  104    0  144   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 2.0, 'curve': 4},
 {'age': 100, 'amount': 1.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0x3c 0x04 0x40 0x64 0x04    \.P<.@d.
    decimal
             92    8   80   60    4   64  100    4
    datetime (unknown)

    body (0)

#### RECORD 18 Ian69 2012-08-24T11:44:51 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-24T11:44:51)
    0000   0xb3 0x2c 0x0b 0x18 0x0c                   .,...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 19 Bolus 2012-08-24T11:44:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x68 0x00    ......h.
    decimal
              1    0  144    0  144    0  104    0
    datetime (2012-08-24T11:44:51)
    0000   0xb3 0x2c 0x4b 0x78 0x0c                   .,Kx.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 BasalProfileStart 2012-08-24T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-24T13:00:00)
    0000   0x80 0x00 0x0d 0x18 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 21 CalBGForPH 2012-08-24T13:21:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2012-08-24T13:21:02)
    0000   0x82 0x15 0x2d 0x78 0x0c                   ..-x.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 22 Ian3F 2012-08-24T13:21:02 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2012-08-24T13:21:02)
    0000   0x82 0x15 0x2d 0x78 0x0c                   ..-x.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2012-08-24T13:22:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 49,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 11.6,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 24.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x31                                  [1
    decimal
             91   49
    datetime (2012-08-24T13:22:59)
    0000   0xbb 0x16 0x0d 0x78 0x0c                   ...x.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0xf8 0x00    ...n.6..
    0008   0x6c 0xf8 0x00 0x74 0x00 0x64 0x36         l..t.d6
    decimal
             30  144    0  110   23   54  248    0
            108  248    0  116    0  100   54
    DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 3.6, 'curve': 4},
 {'age': 158, 'amount': 2.0, 'curve': 4},
 {'age': 198, 'amount': 1.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x90 0x62 0x04 0x50 0x9e 0x04    \..b.P..
    0008   0x40 0xc6 0x04                             @..
    decimal
             92   11  144   98    4   80  158    4
             64  198    4
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2012-08-24T13:23:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x74 0x00    ..d.d.t.
    decimal
              1    0  100    0  100    0  116    0
    datetime (2012-08-24T13:23:00)
    0000   0x80 0x17 0x4d 0x78 0x0c                   ..Mx.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2012-08-24T15:25:10 head[2], body[15] op[0x5b]
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
    datetime (2012-08-24T15:25:10)
    0000   0x8a 0x19 0x0f 0x78 0x0c                   ...x.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    DAY BITS: [0, 1, 1]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 1.05, 'curve': 4},
 {'age': 131, 'amount': 1.45, 'curve': 4},
 {'age': 221, 'amount': 3.6, 'curve': 4},
 {'age': 25, 'amount': 2.0, 'curve': 20},
 {'age': 65, 'amount': 1.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x2a 0x79 0x04 0x3a 0x83 0x04    \.*y.:..
    0008   0x90 0xdd 0x04 0x50 0x19 0x14 0x40 0x41    ...P..@A
    0010   0x14                                       .
    decimal
             92   17   42  121    4   58  131    4
            144  221    4   80   25   20   64   65
             20
    datetime (unknown)

    body (0)

#### RECORD 28 LowReservoir 2012-08-24T15:25:10 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 13.7}
```
    op hex (2)
    0000   0x34 0x89                                  4.
    decimal
             52  137
    datetime (2012-08-24T15:25:10)
    0000   0x8a 0x19 0x4f 0x18 0x8c                   ..O..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 Bolus 2012-08-24T15:25:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x38 0x00    ..|.|.8.
    decimal
              1    0  124    0  124    0   56    0
    datetime (2012-08-24T15:25:10)
    0000   0x8a 0x19 0x4f 0x78 0x0c                   ..Ox.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 30 BolusWizard 2012-08-24T17:43:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
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
    datetime (2012-08-24T17:43:17)
    0000   0x91 0x2b 0x11 0x78 0x0c                   .+.x.
    body (15)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x36         |....|6
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0  124   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 3.1, 'curve': 4},
 {'age': 3, 'amount': 1.05, 'curve': 20},
 {'age': 13, 'amount': 1.45, 'curve': 20},
 {'age': 103, 'amount': 3.6, 'curve': 20},
 {'age': 163, 'amount': 2.0, 'curve': 20},
 {'age': 203, 'amount': 1.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x7c 0x8b 0x04 0x2a 0x03 0x14    \.|..*..
    0008   0x3a 0x0d 0x14 0x90 0x67 0x14 0x50 0xa3    :...g.P.
    0010   0x14 0x40 0xcb 0x14                        .@..
    decimal
             92   20  124  139    4   42    3   20
             58   13   20  144  103   20   80  163
             20   64  203   20
    datetime (unknown)

    body (0)

#### RECORD 32 Ian69 2012-08-24T17:43:17 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2012-08-24T17:43:17)
    0000   0x91 0x2b 0x71 0x18 0x0c                   .+q..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [0, 0, 1]
#### RECORD 33 Bolus 2012-08-24T17:43:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x2c 0x00    ..|.|.,.
    decimal
              1    0  124    0  124    0   44    0
    datetime (2012-08-24T17:43:17)
    0000   0x91 0x2b 0x51 0x78 0x0c                   .+Qx.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 CalBGForPH 2012-08-24T19:44:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-08-24T19:44:06)
    0000   0x86 0x2c 0x33 0x78 0x0c                   .,3x.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 35 Ian3F 2012-08-24T19:44:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2012-08-24T19:44:06)
    0000   0x86 0x2c 0x93 0x78 0x0c                   .,.x.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 BolusWizard 2012-08-24T19:52:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 56,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 5.2,
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
    0000   0x5b 0x38                                  [8
    decimal
             91   56
    datetime (2012-08-24T19:52:11)
    0000   0x8b 0x34 0x13 0x78 0x0c                   .4.x.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x34 0x00 0x58 0x36         X..4.X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0   52    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 128, 'amount': 2.05, 'curve': 4},
 {'age': 138, 'amount': 1.05, 'curve': 4},
 {'age': 12, 'amount': 3.1, 'curve': 20},
 {'age': 132, 'amount': 1.05, 'curve': 20},
 {'age': 142, 'amount': 1.45, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x52 0x80 0x04 0x2a 0x8a 0x04    \.R..*..
    0008   0x7c 0x0c 0x14 0x2a 0x84 0x14 0x3a 0x8e    |..*..:.
    0010   0x14                                       .
    decimal
             92   17   82  128    4   42  138    4
            124   12   20   42  132   20   58  142
             20
    datetime (unknown)

    body (0)

#### RECORD 38 LowReservoir 2012-08-24T19:52:11 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.0}
```
    op hex (2)
    0000   0x34 0x00                                  4.
    decimal
             52    0
    datetime (2012-08-24T19:52:11)
    0000   0x8b 0x34 0x13 0x18 0x8c                   .4...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 39 Bolus 2012-08-24T19:52:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x34 0x00    ......4.
    decimal
              1    0  136    0  136    0   52    0
    datetime (2012-08-24T19:52:11)
    0000   0x8b 0x34 0x53 0x78 0x0c                   .4Sx.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 CalBGForPH 2012-08-24T22:44:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 211}
```
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2012-08-24T22:44:00)
    0000   0x80 0x2c 0x36 0x78 0x0c                   .,6x.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2012-08-24T22:44:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2012-08-24T22:44:00)
    0000   0x80 0x2c 0x76 0x78 0x0c                   .,vx.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 Rewind 2012-08-24T22:44:13 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-08-24T22:44:13)
    0000   0x8d 0x2c 0x16 0x18 0x0c                   .,...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 Prime 2012-08-24T22:45:34 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x08                   .....
    decimal
              3    0    0    0    8
    datetime (2012-08-24T22:45:34)
    0000   0xa2 0x2d 0x36 0x18 0x0c                   .-6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 44 BasalProfileStart 2012-08-24T22:45:43 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-24T22:45:43)
    0000   0xab 0x2d 0x16 0x18 0x0c                   .-...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 0, 1]
#### RECORD 45 BolusWizard 2012-08-24T22:45:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 10.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2012-08-24T22:45:52)
    0000   0xb4 0x2d 0x16 0x78 0x0c                   .-.x.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x6c 0x00    ...n.6l.
    0008   0x00 0x00 0x00 0x18 0x00 0x54 0x36         .....T6
    decimal
              0  144    0  110   23   54  108    0
              0    0    0   24    0   84   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 171, 'amount': 0.7, 'curve': 4},
 {'age': 181, 'amount': 2.7, 'curve': 4},
 {'age': 45, 'amount': 2.05, 'curve': 20},
 {'age': 55, 'amount': 1.05, 'curve': 20},
 {'age': 185, 'amount': 3.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x1c 0xab 0x04 0x6c 0xb5 0x04    \....l..
    0008   0x52 0x2d 0x14 0x2a 0x37 0x14 0x7c 0xb9    R-.*7.|.
    0010   0x14                                       .
    decimal
             92   17   28  171    4  108  181    4
             82   45   20   42   55   20  124  185
             20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-08-24T22:45:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x18 0x00    ........
    decimal
              1    0  128    0  128    0   24    0
    datetime (2012-08-24T22:45:52)
    0000   0xb4 0x2d 0x56 0x78 0x0c                   .-Vx.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BasalProfileStart 2012-08-25T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2012-08-25T00:00:00)
    0000   0x80 0x00 0x00 0x19 0x0c                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 49 MResultTotals 2012-08-25T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x0c                   .....
    decimal
              7    0    0    7   12
    datetime (2012-08-25T00:00:00)
    0000   0x98 0x0c                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 50 Sara6E 2012-08-25T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2012-08-25T00:00:00)
    0000   0x98 0x0c                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x83 0x3e 0xf9 0x06 0x00 0x00    ...>....
    0008   0x07 0x0c 0x03 0x88 0x32 0x03 0x84 0x32    ....2..2
    0010   0x00 0xc2 0x01 0xf8 0x00 0x80 0x01 0x0c    ........
    0018   0x00 0x00 0x05 0x01 0x02 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6    0  131   62  249    6    0    0
              7   12    3  136   50    3  132   50
              0  194    1  248    0  128    1   12
              0    0    5    1    2    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 51 CalBGForPH 2012-08-25T00:29:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2012-08-25T00:29:26)
    0000   0x9a 0x1d 0x20 0x79 0x0c                   .. y.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 52 Ian3F 2012-08-25T00:29:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2012-08-25T00:29:26)
    0000   0x9a 0x1d 0x00 0x79 0x0c                   ...y.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 53 BasalProfileStart 2012-08-25T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-25T04:00:00)
    0000   0x80 0x00 0x04 0x19 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 54 BolusWizard 2012-08-25T08:48:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-25T08:48:35)
    0000   0xa3 0x30 0x08 0x79 0x0c                   .0.y.
    body (15)
    hex
    0000   0x1b 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x36         `....`6
    decimal
             27  144    0  110   23   54    0    0
             96    0    0    0    0   96   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 Ian69 2012-08-25T08:48:35 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-25T08:48:35)
    0000   0xa3 0x30 0x08 0x19 0x0c                   .0...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 0, 1]
#### RECORD 56 Bolus 2012-08-25T08:48:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x00 0x00    ..`.`...
    decimal
              1    0   96    0   96    0    0    0
    datetime (2012-08-25T08:48:35)
    0000   0xa3 0x30 0x48 0x79 0x0c                   .0Hy.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BasalProfileStart 2012-08-25T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-25T09:30:00)
    0000   0x80 0x1e 0x09 0x19 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 58 BolusWizard 2012-08-25T12:31:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 32,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 116}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-25T12:31:24)
    0000   0x98 0x1f 0x0c 0x79 0x0c                   ...y.
    body (15)
    hex
    0000   0x20 0x90 0x00 0x6e 0x17 0x36 0x00 0x00     ..n.6..
    0008   0x74 0x00 0x00 0x00 0x00 0x74 0x36         t....t6
    decimal
             32  144    0  110   23   54    0    0
            116    0    0    0    0  116   54
    DAY BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 227, 'amount': 2.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0xe3 0x04                   \.`..
    decimal
             92    5   96  227    4
    datetime (unknown)

    body (0)

#### RECORD 60 Ian69 2012-08-25T12:31:24 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2012-08-25T12:31:24)
    0000   0x98 0x1f 0x0c 0x19 0x0c                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 61 Bolus 2012-08-25T12:31:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x08 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    8    0
    datetime (2012-08-25T12:31:24)
    0000   0x98 0x1f 0x4c 0x79 0x0c                   ..Ly.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 62 BolusWizard 2012-08-25T12:54:02 head[2], body[15] op[0x5b]
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
    datetime (2012-08-25T12:54:02)
    0000   0x82 0x36 0x0c 0x79 0x0c                   .6.y.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 2.9, 'curve': 4},
 {'age': 250, 'amount': 2.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0x1e 0x04 0x60 0xfa 0x04    \.t..`..
    decimal
             92    8  116   30    4   96  250    4
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2012-08-25T12:54:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x70 0x00    ..4.4.p.
    decimal
              1    0   52    0   52    0  112    0
    datetime (2012-08-25T12:54:02)
    0000   0x82 0x36 0x4c 0x79 0x0c                   .6Ly.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 BasalProfileStart 2012-08-25T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-25T13:00:00)
    0000   0x80 0x00 0x0d 0x19 0x0c                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 66 CalBGForPH 2012-08-25T13:55:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-08-25T13:55:02)
    0000   0x82 0x37 0x2d 0x79 0x0c                   .7-y.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 Ian3F 2012-08-25T13:55:02 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2012-08-25T13:55:02)
    0000   0x82 0x37 0x2d 0x79 0x0c                   .7-y.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 68 Rewind 2012-08-25T14:45:19 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-08-25T14:45:19)
    0000   0x93 0x2d 0x0e 0x19 0x0c                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 Prime 2012-08-25T14:49:32 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x19                   .....
    decimal
              3    0    0    0   25
    datetime (2012-08-25T14:49:32)
    0000   0xa0 0x31 0x2e 0x19 0x0c                   .1...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 BasalProfileStart 2012-08-25T14:50:12 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2012-08-25T14:50:12)
    0000   0x8c 0x32 0x0e 0x19 0x0c                   .2...
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [0, 0, 1]
#### RECORD 71 CalBGForPH 2012-08-25T14:50:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 56}
```
    op hex (2)
    0000   0x0a 0x38                                  .8
    decimal
             10   56
    datetime (2012-08-25T14:50:21)
    0000   0x95 0x32 0x4e 0x19 0x0c                   .2N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 72 BolusWizard 2012-08-25T14:50:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 56,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.4,
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
    0000   0x5b 0x38                                  [8
    decimal
             91   56
    datetime (2012-08-25T14:50:30)
    0000   0x9e 0x32 0x0e 0x79 0x0c                   .2.y.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x40 0x00 0x24 0x36         $..@.$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0   64    0   36   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 116, 'amount': 1.3, 'curve': 4},
 {'age': 146, 'amount': 2.9, 'curve': 4},
 {'age': 110, 'amount': 2.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x74 0x04 0x74 0x92 0x04    \.4t.t..
    0008   0x60 0x6e 0x14                             `n.
    decimal
             92   11   52  116    4  116  146    4
             96  110   20
    datetime (unknown)

    body (0)

#### RECORD 74 CalBGForPH 2012-08-25T15:43:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2012-08-25T15:43:32)
    0000   0xa0 0x2b 0x2f 0x79 0x0c                   .+/y.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 75 Ian3F 2012-08-25T15:43:32 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2012-08-25T15:43:32)
    0000   0xa0 0x2b 0x2f 0x79 0x0c                   .+/y.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 76 BolusWizard 2012-08-25T15:43:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 94,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.8,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 6.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x5e                                  [^
    decimal
             91   94
    datetime (2012-08-25T15:43:44)
    0000   0xac 0x2b 0x0f 0x79 0x0c                   .+.y.
    body (15)
    hex
    0000   0x0b 0x90 0x00 0x6e 0x17 0x36 0x44 0x00    ...n.6D.
    0008   0x28 0x00 0x00 0x1c 0x00 0x50 0x36         (....P6
    decimal
             11  144    0  110   23   54   68    0
             40    0    0   28    0   80   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 169, 'amount': 1.3, 'curve': 4},
 {'age': 199, 'amount': 2.9, 'curve': 4},
 {'age': 163, 'amount': 2.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0xa9 0x04 0x74 0xc7 0x04    \.4..t..
    0008   0x60 0xa3 0x14                             `..
    decimal
             92   11   52  169    4  116  199    4
             96  163   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2012-08-25T15:43:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x1c 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   28    0
    datetime (2012-08-25T15:43:44)
    0000   0xac 0x2b 0x4f 0x79 0x0c                   .+Oy.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 79 BolusWizard 2012-08-25T17:28:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 23,
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
    datetime (2012-08-25T17:28:07)
    0000   0x87 0x1c 0x11 0x79 0x0c                   ...y.
    body (15)
    hex
    0000   0x17 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             23  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    DAY BITS: [0, 1, 1]
`end analysis/ianj/raw/ReadHistoryData-page-14.data: 80 records`
