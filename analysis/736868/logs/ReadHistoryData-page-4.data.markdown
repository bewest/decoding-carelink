## START analysis/736868/logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 1003, found 19 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1f 0x7a                                  .z
##### DEBUG DECIMAL
             31  122
#### RECORD 0 Ian0B 2015-03-22T04:19:37 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xca                             .e.
    decimal
             11  101  202
    datetime (2015-03-22T04:19:37)
    0000   0x25 0xd3 0x24 0xb6 0x0f                   %.$..
    body (0)

#### RECORD 1 Ian0B 2015-03-22T05:50:16 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-03-22T05:50:16)
    0000   0x10 0xf2 0x25 0xb6 0x0f                   ..%..
    body (0)

#### RECORD 2 BasalProfileStart 2015-03-22T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-22T07:00:00)
    0000   0x00 0xc0 0x07 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 3 Ian0B 2015-03-22T09:44:54 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-22T09:44:54)
    0000   0x36 0xec 0x29 0xb6 0x0f                   6.)..
    body (0)

#### RECORD 4 BolusWizard 2015-03-22T09:47:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 50,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-22T09:47:24)
    0000   0x18 0xef 0x09 0x76 0x0f                   ...v.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 5 Bolus 2015-03-22T09:47:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x00 0x00    ........
    decimal
              1    0  200    0  200    0    0    0
    datetime (2015-03-22T09:47:25)
    0000   0x19 0xef 0x49 0x76 0x0f                   ..Iv.
    body (0)

#### RECORD 6 BasalProfileStart 2015-03-22T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-22T10:00:00)
    0000   0x00 0xc0 0x0a 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 7 Ian0B 2015-03-22T10:01:04 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-22T10:01:04)
    0000   0x04 0xc1 0x2a 0xb6 0x0f                   ..*..
    body (0)

#### RECORD 8 Ian0B 2015-03-22T10:01:04 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-03-22T10:01:04)
    0000   0x04 0xc1 0x2a 0xb6 0x0f                   ..*..
    body (0)

#### RECORD 9 BasalProfileStart 2015-03-22T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-22T12:00:00)
    0000   0x00 0xc0 0x0c 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 10 BolusWizard 2015-03-22T14:21:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 1.2,
 'carb_input': 61,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-22T14:21:29)
    0000   0x1d 0xd5 0x0e 0x76 0x0f                   ...v.
    body (15)
    hex
    0000   0x3d 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    =P.P(Z..
    0008   0x30 0x00 0x00 0x00 0x01 0x30 0x78         0....0x
    decimal
             61   80    0   80   40   90    0    1
             48    0    0    0    1   48  120

#### RECORD 11 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 2.65, 'curve': 20},
 {'age': 26, 'amount': 2.35, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x6a 0x10 0x14 0x5e 0x1a 0x14    \.j..^..
    decimal
             92    8  106   16   20   94   26   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2015-03-22T14:24:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2,
 'duration': 60,
 'programmed': 3.2,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x00 0x02    ........
    decimal
              1    0  128    0  128    0    0    2
    datetime (2015-03-22T14:24:28)
    0000   0x1c 0xd8 0xae 0x76 0x0f                   ...v.
    body (0)

#### RECORD 13 Bolus 2015-03-22T14:21:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4,
 'duration': 0,
 'programmed': 4.4,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xb0 0x00 0xb0 0x00 0x00 0x00    ........
    decimal
              1    0  176    0  176    0    0    0
    datetime (2015-03-22T14:21:29)
    0000   0x1d 0xd5 0x8e 0x76 0x0f                   ...v.
    body (0)

#### RECORD 14 BasalProfileStart 2015-03-22T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-22T15:00:00)
    0000   0x00 0xc0 0x0f 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 15 PumpSuspend 2015-03-22T15:41:27 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-22T15:41:27)
    0000   0x1b 0xe9 0x0f 0x16 0x0f                   .....
    body (0)

#### RECORD 16 BasalProfileStart 2015-03-22T16:12:48 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-22T16:12:48)
    0000   0x30 0xcc 0x10 0x16 0x0f                   0....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 17 PumpResume 2015-03-22T16:12:48 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-22T16:12:48)
    0000   0x30 0xcc 0x10 0x16 0x0f                   0....
    body (0)

#### RECORD 18 CalBGForPH 2015-03-22T16:13:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2015-03-22T16:13:23)
    0000   0x17 0xcd 0x30 0x76 0x0f                   ..0v.
    body (0)

#### RECORD 19 Ian3F 2015-03-22T16:13:23 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2015-03-22T16:13:23)
    0000   0x17 0xcd 0x30 0x76 0x0f                   ..0v.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 20 BolusWizard 2015-03-22T17:00:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 3.7,
 'carb_input': 30,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-22T17:00:00)
    0000   0x00 0xc0 0x11 0x76 0x0f                   ...v.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x94 0x00 0x00 0x00 0x00 0x94 0x78         ......x
    decimal
             30   80    0   80   40   90    0    0
            148    0    0    0    0  148  120

#### RECORD 21 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 0.3, 'curve': 4},
 {'age': 111, 'amount': 0.55, 'curve': 4},
 {'age': 121, 'amount': 0.5, 'curve': 4},
 {'age': 131, 'amount': 0.55, 'curve': 4},
 {'age': 141, 'amount': 0.55, 'curve': 4},
 {'age': 151, 'amount': 0.5, 'curve': 4},
 {'age': 161, 'amount': 4.65, 'curve': 4},
 {'age': 175, 'amount': 2.65, 'curve': 20},
 {'age': 185, 'amount': 2.35, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x0c 0x65 0x04 0x16 0x6f 0x04    \..e..o.
    0008   0x14 0x79 0x04 0x16 0x83 0x04 0x16 0x8d    .y......
    0010   0x04 0x14 0x97 0x04 0xba 0xa1 0x04 0x6a    .......j
    0018   0xaf 0x14 0x5e 0xb9 0x14                   ..^..
    decimal
             92   29   12  101    4   22  111    4
             20  121    4   22  131    4   22  141
              4   20  151    4  186  161    4  106
            175   20   94  185   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2015-03-22T17:00:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7,
 'duration': 0,
 'programmed': 3.7,
 'type': 'normal',
 'unabsorbed': 2.5}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0x64 0x00    ......d.
    decimal
              1    0  148    0  148    0  100    0
    datetime (2015-03-22T17:00:00)
    0000   0x00 0xc0 0x51 0x76 0x0f                   ..Qv.
    body (0)

#### RECORD 23 BasalProfileStart 2015-03-22T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-22T22:00:00)
    0000   0x00 0xc0 0x16 0x16 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 24 BolusWizard 2015-03-22T22:34:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 50,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-22T22:34:14)
    0000   0x0e 0xe2 0x16 0x76 0x0f                   ...v.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 25 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 3.7, 'curve': 20},
 {'age': 179, 'amount': 0.3, 'curve': 20},
 {'age': 189, 'amount': 0.55, 'curve': 20},
 {'age': 199, 'amount': 0.5, 'curve': 20},
 {'age': 209, 'amount': 0.55, 'curve': 20},
 {'age': 219, 'amount': 0.55, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x94 0x4f 0x14 0x0c 0xb3 0x14    \..O....
    0008   0x16 0xbd 0x14 0x14 0xc7 0x14 0x16 0xd1    ........
    0010   0x14 0x16 0xdb 0x14                        ....
    decimal
             92   20  148   79   20   12  179   20
             22  189   20   20  199   20   22  209
             20   22  219   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2015-03-22T22:34:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x00 0x00    ........
    decimal
              1    0  200    0  200    0    0    0
    datetime (2015-03-22T22:34:15)
    0000   0x0f 0xe2 0x56 0x76 0x0f                   ..Vv.
    body (0)

#### RECORD 27 BasalProfileStart 2015-03-23T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-23T00:00:00)
    0000   0x00 0xc0 0x00 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 28 MResultTotals 2015-03-23T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x74                   ....t
    decimal
              7    0    0    6  116
    datetime (2015-03-23T00:00:00)
    0000   0x36 0x8f                                  6.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 29 Sara6E 2015-03-23T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-23T00:00:00)
    0000   0x36 0x8f                                  6.
    body (49)
    hex
    0000   0x05 0x00 0x52 0x49 0x5b 0x02 0x00 0x00    ..RI[...
    0008   0x06 0x74 0x03 0x20 0x30 0x03 0x54 0x34    .t. 0.T4
    0010   0x00 0xbf 0x03 0x54 0x00 0x00 0x00 0x00    ...T....
    0018   0x00 0x00 0x04 0x00 0x00 0x00 0x00 0x9f    ........
    0020   0x23 0x41 0x00 0x6f 0x20 0x02 0x00 0x00    #A.o ...
    0028   0x00 0x00 0x04 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0   82   73   91    2    0    0
              6  116    3   32   48    3   84   52
              0  191    3   84    0    0    0    0
              0    0    4    0    0    0    0  159
             35   65    0  111   32    2    0    0
              0    0    4    0    0    0    0    0
              0

#### RECORD 30 BasalProfileStart 2015-03-23T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-23T04:00:00)
    0000   0x00 0xc0 0x04 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 31 PumpSuspend 2015-03-23T06:51:43 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-23T06:51:43)
    0000   0x2b 0xf3 0x06 0x17 0x0f                   +....
    body (0)

#### RECORD 32 BasalProfileStart 2015-03-23T07:16:20 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-23T07:16:20)
    0000   0x14 0xd0 0x07 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 33 PumpResume 2015-03-23T07:16:21 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-23T07:16:21)
    0000   0x15 0xd0 0x07 0x17 0x0f                   .....
    body (0)

#### RECORD 34 BolusWizard 2015-03-23T08:34:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 4.4,
 'carb_input': 44,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.4,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-23T08:34:07)
    0000   0x07 0xe2 0x08 0x77 0x0f                   ...w.
    body (15)
    hex
    0000   0x2c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    ,P.d(Z..
    0008   0xb0 0x00 0x00 0x00 0x00 0xb0 0x78         ......x
    decimal
             44   80    0  100   40   90    0    0
            176    0    0    0    0  176  120

#### RECORD 35 Bolus 2015-03-23T08:36:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9,
 'duration': 60,
 'programmed': 0.9,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x00 0x02    ..$.$...
    decimal
              1    0   36    0   36    0    0    2
    datetime (2015-03-23T08:36:28)
    0000   0x1c 0xe4 0xa8 0x77 0x0f                   ...w.
    body (0)

#### RECORD 36 Bolus 2015-03-23T08:34:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x00 0x00    ........
    decimal
              1    0  140    0  140    0    0    0
    datetime (2015-03-23T08:34:07)
    0000   0x07 0xe2 0x88 0x77 0x0f                   ...w.
    body (0)

#### RECORD 37 Ian0B 2015-03-23T09:41:50 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-23T09:41:50)
    0000   0x32 0xe9 0x29 0xb7 0x0f                   2.)..
    body (0)

#### RECORD 38 CalBGForPH 2015-03-23T09:42:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2015-03-23T09:42:49)
    0000   0x31 0xea 0x29 0x77 0x0f                   1.)w.
    body (0)

#### RECORD 39 Ian3F 2015-03-23T09:42:49 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2015-03-23T09:42:49)
    0000   0x31 0xea 0xc9 0x77 0x0f                   1..w.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 40 BasalProfileStart 2015-03-23T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-23T10:00:00)
    0000   0x00 0xc0 0x0a 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 41 Ian0B 2015-03-23T10:33:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-23T10:33:07)
    0000   0x07 0xe1 0x2a 0xb7 0x0f                   ..*..
    body (0)

#### RECORD 42 Ian0B 2015-03-23T10:42:48 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-23T10:42:48)
    0000   0x30 0xea 0x2a 0xb7 0x0f                   0.*..
    body (0)

#### RECORD 43 BolusWizard 2015-03-23T11:47:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 5.2,
 'carb_input': 42,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-23T11:47:22)
    0000   0x16 0xef 0x0b 0x77 0x0f                   ...w.
    body (15)
    hex
    0000   0x2a 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    *P.P(Z..
    0008   0xd0 0x00 0x00 0x00 0x00 0xd0 0x78         ......x
    decimal
             42   80    0   80   40   90    0    0
            208    0    0    0    0  208  120

#### RECORD 44 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 138, 'amount': 0.1, 'curve': 4},
 {'age': 148, 'amount': 0.15, 'curve': 4},
 {'age': 158, 'amount': 0.15, 'curve': 4},
 {'age': 168, 'amount': 0.15, 'curve': 4},
 {'age': 178, 'amount': 0.15, 'curve': 4},
 {'age': 188, 'amount': 0.15, 'curve': 4},
 {'age': 198, 'amount': 3.55, 'curve': 4}]
```
    op hex (23)
    0000   0x5c 0x17 0x04 0x8a 0x04 0x06 0x94 0x04    \.......
    0008   0x06 0x9e 0x04 0x06 0xa8 0x04 0x06 0xb2    ........
    0010   0x04 0x06 0xbc 0x04 0x8e 0xc6 0x04         .......
    decimal
             92   23    4  138    4    6  148    4
              6  158    4    6  168    4    6  178
              4    6  188    4  142  198    4
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2015-03-23T11:50:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 60,
 'programmed': 1.0,
 'type': 'square',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x1c 0x02    ..(.(...
    decimal
              1    0   40    0   40    0   28    2
    datetime (2015-03-23T11:50:12)
    0000   0x0c 0xf2 0xab 0x77 0x0f                   ...w.
    body (0)

#### RECORD 46 Bolus 2015-03-23T11:47:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2,
 'duration': 0,
 'programmed': 4.2,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x1c 0x00    ........
    decimal
              1    0  168    0  168    0   28    0
    datetime (2015-03-23T11:47:22)
    0000   0x16 0xef 0x8b 0x77 0x0f                   ...w.
    body (0)

#### RECORD 47 BasalProfileStart 2015-03-23T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-23T12:00:00)
    0000   0x00 0xc0 0x0c 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 48 Ian0B 2015-03-23T12:12:39 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xc4                             .e.
    decimal
             11  101  196
    datetime (2015-03-23T12:12:39)
    0000   0x27 0xcc 0x2c 0xb7 0x0f                   '.,..
    body (0)

#### RECORD 49 Ian0B 2015-03-23T14:27:12 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-23T14:27:12)
    0000   0x0c 0xdb 0x2e 0xb7 0x0f                   .....
    body (0)

#### RECORD 50 Ian0B 2015-03-23T14:38:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-23T14:38:00)
    0000   0x00 0xe6 0x2e 0xb7 0x0f                   .....
    body (0)

#### RECORD 51 Ian0B 2015-03-23T14:43:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-23T14:43:00)
    0000   0x00 0xeb 0x2e 0xb7 0x0f                   .....
    body (0)

#### RECORD 52 CalBGForPH 2015-03-23T14:44:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2015-03-23T14:44:03)
    0000   0x03 0xec 0x2e 0x77 0x0f                   ...w.
    body (0)

#### RECORD 53 Ian3F 2015-03-23T14:44:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-03-23T14:44:03)
    0000   0x03 0xec 0xae 0x77 0x0f                   ...w.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 54 BolusWizard 2015-03-23T14:44:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 181,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 12.0,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.1}
```
    op hex (2)
    0000   0x5b 0xb5                                  [.
    decimal
             91  181
    datetime (2015-03-23T14:44:20)
    0000   0x14 0xec 0x0e 0x17 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x3c 0x00    .P.P(Z<.
    0008   0x00 0x00 0x00 0x2c 0x00 0x10 0x78         ...,..x
    decimal
              0   80    0   80   40   90   60    0
              0    0    0   44    0   16  120

#### RECORD 55 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 0.2, 'curve': 4},
 {'age': 135, 'amount': 0.15, 'curve': 4},
 {'age': 145, 'amount': 0.15, 'curve': 4},
 {'age': 155, 'amount': 0.2, 'curve': 4},
 {'age': 165, 'amount': 0.15, 'curve': 4},
 {'age': 175, 'amount': 1.95, 'curve': 4},
 {'age': 185, 'amount': 2.4, 'curve': 4},
 {'age': 59, 'amount': 0.1, 'curve': 20},
 {'age': 69, 'amount': 0.15, 'curve': 20},
 {'age': 79, 'amount': 0.15, 'curve': 20},
 {'age': 89, 'amount': 0.15, 'curve': 20},
 {'age': 99, 'amount': 0.15, 'curve': 20},
 {'age': 109, 'amount': 0.15, 'curve': 20},
 {'age': 119, 'amount': 3.55, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0x08 0x7d 0x04 0x06 0x87 0x04    \,.}....
    0008   0x06 0x91 0x04 0x08 0x9b 0x04 0x06 0xa5    ........
    0010   0x04 0x4e 0xaf 0x04 0x60 0xb9 0x04 0x04    .N..`...
    0018   0x3b 0x14 0x06 0x45 0x14 0x06 0x4f 0x14    ;..E..O.
    0020   0x06 0x59 0x14 0x06 0x63 0x14 0x06 0x6d    .Y..c..m
    0028   0x14 0x8e 0x77 0x14                        ..w.
    decimal
             92   44    8  125    4    6  135    4
              6  145    4    8  155    4    6  165
              4   78  175    4   96  185    4    4
             59   20    6   69   20    6   79   20
              6   89   20    6   99   20    6  109
             20  142  119   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2015-03-23T14:44:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x2c 0x00    ......,.
    decimal
              1    0    0    0    0    0   44    0
    datetime (2015-03-23T14:44:20)
    0000   0x14 0xec 0xae 0x17 0x0f                   .....
    body (0)

#### RECORD 57 Bolus 2015-03-23T14:44:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4,
 'duration': 0,
 'programmed': 0.4,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x2c 0x00    ......,.
    decimal
              1    0   16    0   16    0   44    0
    datetime (2015-03-23T14:44:20)
    0000   0x14 0xec 0x8e 0x17 0x0f                   .....
    body (0)

#### RECORD 58 BasalProfileStart 2015-03-23T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-23T15:00:00)
    0000   0x00 0xc0 0x0f 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 59 Ian0B 2015-03-23T16:06:31 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-03-23T16:06:31)
    0000   0x1f 0xc6 0x30 0xb7 0x0f                   ..0..
    body (0)

#### RECORD 60 Ian0B 2015-03-23T18:12:39 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-23T18:12:39)
    0000   0x27 0xcc 0x32 0xb7 0x0f                   '.2..
    body (0)

#### RECORD 61 Ian0B 2015-03-23T18:16:33 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-23T18:16:33)
    0000   0x21 0xd0 0x32 0xb7 0x0f                   !.2..
    body (0)

#### RECORD 62 Bolus 2015-03-23T18:16:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x04 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    4    0
    datetime (2015-03-23T18:16:56)
    0000   0x38 0xd0 0x52 0x77 0x0f                   8.Rw.
    body (0)

#### RECORD 63 BolusWizard 2015-03-23T18:20:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 60,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 45,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-23T18:20:06)
    0000   0x06 0xd4 0x12 0x77 0x0f                   ...w.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    -P.<(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             45   80    0   60   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 64 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 2.0, 'curve': 4},
 {'age': 221, 'amount': 0.4, 'curve': 4},
 {'age': 85, 'amount': 0.2, 'curve': 20},
 {'age': 95, 'amount': 0.15, 'curve': 20},
 {'age': 105, 'amount': 0.15, 'curve': 20},
 {'age': 115, 'amount': 0.2, 'curve': 20},
 {'age': 125, 'amount': 0.15, 'curve': 20},
 {'age': 135, 'amount': 1.95, 'curve': 20},
 {'age': 145, 'amount': 2.4, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x50 0x0b 0x04 0x10 0xdd 0x04    \.P.....
    0008   0x08 0x55 0x14 0x06 0x5f 0x14 0x06 0x69    .U.._..i
    0010   0x14 0x08 0x73 0x14 0x06 0x7d 0x14 0x4e    ..s..}.N
    0018   0x87 0x14 0x60 0x91 0x14                   ..`..
    decimal
             92   29   80   11    4   16  221    4
              8   85   20    6   95   20    6  105
             20    8  115   20    6  125   20   78
            135   20   96  145   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2015-03-23T18:20:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1,
 'duration': 0,
 'programmed': 1.1,
 'type': 'normal',
 'unabsorbed': 2.1}
```
    op hex (8)
    0000   0x01 0x01 0x2c 0x01 0x2c 0x00 0x54 0x00    ..,.,.T.
    decimal
              1    1   44    1   44    0   84    0
    datetime (2015-03-23T18:20:07)
    0000   0x07 0xd4 0x52 0x77 0x0f                   ..Rw.
    body (0)

#### RECORD 66 BasalProfileStart 2015-03-23T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-23T22:00:00)
    0000   0x00 0xc0 0x16 0x17 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 67 Ian0B 2015-03-23T22:12:38 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-23T22:12:38)
    0000   0x26 0xcc 0x36 0xb7 0x0f                   &.6..
    body (0)

#### RECORD 68 BolusWizard 2015-03-23T22:15:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 60,
 'bg_target_low': 90,
 'bolus_estimate': 4.6,
 'carb_input': 66,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-23T22:15:31)
    0000   0x1f 0xcf 0x16 0x77 0x0f                   ...w.
    body (15)
    hex
    0000   0x42 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    BP.<(Z..
    0008   0xb8 0x00 0x00 0x00 0x01 0xb8 0x78         ......x
    decimal
             66   80    0   60   40   90    0    1
            184    0    0    0    1  184  120

#### RECORD 69 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 236, 'amount': 1.1, 'curve': 5},
 {'age': 246, 'amount': 2.0, 'curve': 4},
 {'age': 200, 'amount': 0.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2c 0xec 0x05 0x50 0xf6 0x04    \.,..P..
    0008   0x10 0xc8 0x14                             ...
    decimal
             92   11   44  236    5   80  246    4
             16  200   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2015-03-23T22:19:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 120,
 'programmed': 2.5,
 'type': 'square',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x14 0x04    ..d.d...
    decimal
              1    0  100    0  100    0   20    4
    datetime (2015-03-23T22:19:14)
    0000   0x0e 0xd3 0xb6 0x77 0x0f                   ...w.
    body (0)

#### RECORD 71 Bolus 2015-03-23T22:15:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5,
 'duration': 0,
 'programmed': 5.5,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0xdc 0x00 0xdc 0x00 0x14 0x00    ........
    decimal
              1    0  220    0  220    0   20    0
    datetime (2015-03-23T22:15:31)
    0000   0x1f 0xcf 0x96 0x77 0x0f                   ...w.
    body (0)

#### RECORD 72 Ian0B 2015-03-23T22:21:49 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-03-23T22:21:49)
    0000   0x31 0xd5 0x36 0xb7 0x0f                   1.6..
    body (0)

#### RECORD 73 CalBGForPH 2015-03-23T22:30:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2015-03-23T22:30:43)
    0000   0x2b 0xde 0x36 0x77 0x0f                   +.6w.
    body (0)

#### RECORD 74 Ian3F 2015-03-23T22:30:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2015-03-23T22:30:43)
    0000   0x2b 0xde 0xb6 0x77 0x0f                   +..w.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 75 BasalProfileStart 2015-03-24T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-24T00:00:00)
    0000   0x00 0xc0 0x00 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 76 MResultTotals 2015-03-24T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x5d                   ....]
    decimal
              7    0    0    7   93
    datetime (2015-03-24T00:00:00)
    0000   0x37 0x8f                                  7.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end analysis/736868/logs/ReadHistoryData-page-4.data: 77 records`
