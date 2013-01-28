## START logs/ReadHistoryData-page-13.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb7 0x62                                  .b
##### DEBUG DECIMAL
            183   98
#### RECORD 0 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 130, 'amount': 4.4, 'curve': 20},
 {'age': 210, 'amount': 3.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xb0 0x82 0x14 0x84 0xd2 0x14    \.......
    decimal
             92    8  176  130   20  132  210   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2012-12-06T19:10:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-12-06T19:10:46)
    0000   0xee 0x0a 0x53 0x06 0x0c                   ..S..
    body (0)

#### RECORD 2 ResultTotals 2012-12-06T13:12:06 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x3c                   ....<
    decimal
              7    0    0    5   60
    datetime (2012-12-06T13:12:06)
    0000   0xc6 0x0c 0x6d 0xc6 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xa9 0x60 0x12 0x05 0x00 0x00    ...`....
    0008   0x05 0x3c 0x03 0x78 0x42 0x01 0xc4 0x22    .<.xB.."
    0010   0x00 0x6c 0x01 0xc4 0x22 0x01 0x40 0x47    .l..".@G
    0018   0x00 0x84 0x1d 0x00 0x00 0x00 0x03 0x02    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  169   96   18    5    0    0
              5   60    3  120   66    1  196   34
              0  108    1  196   34    1   64   71
              0  132   29    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 3 LowReservoir 2012-12-07T11:02:43 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-12-07T11:02:43)
    0000   0xeb 0x02 0x0b 0x07 0x0c                   .....
    body (0)

#### RECORD 4 BolusWizard 2012-12-07T16:47:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 22,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-07T16:47:15)
    0000   0xcf 0x2f 0x10 0x07 0x0c                   ./...
    body (13)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             22   80   13   45  106    0   16    0
              0    0    0   16  125
    HOUR BITS: [0, 0, 1]
#### RECORD 5 Bolus 2012-12-07T16:47:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'programmed': 1.6}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-12-07T16:47:16)
    0000   0xd0 0x2f 0x50 0x07 0x0c                   ./P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 BolusWizard 2012-12-07T17:26:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-07T17:26:15)
    0000   0xcf 0x1a 0x11 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    <P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106    0   46    0
              0    0    0   46  125

#### RECORD 7 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 42, 'amount': 1.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x2a 0x04                   \.@*.
    decimal
             92    5   64   42    4
    datetime (unknown)

    body (0)

#### RECORD 8 LowReservoir 2012-12-07T17:27:29 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-12-07T17:27:29)
    0000   0xdd 0x1b 0x11 0x07 0x0c                   .....
    body (0)

#### RECORD 9 Bolus 2012-12-07T17:26:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'programmed': 4.6}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2012-12-07T17:26:15)
    0000   0xcf 0x1a 0x51 0x07 0x0c                   ..Q..
    body (0)

#### RECORD 10 BolusWizard 2012-12-07T17:38:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-07T17:38:30)
    0000   0xde 0x26 0x11 0x07 0x0c                   .&...
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    =P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             61   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [0, 0, 1]
#### RECORD 11 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 4.6, 'curve': 4},
 {'age': 54, 'amount': 1.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb8 0x0e 0x04 0x40 0x36 0x04    \....@6.
    decimal
             92    8  184   14    4   64   54    4
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2012-12-07T17:38:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'programmed': 4.6}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2012-12-07T17:38:31)
    0000   0xdf 0x26 0x51 0x07 0x0c                   .&Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 Rewind 2012-12-07T19:19:58 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-07T19:19:58)
    0000   0xfa 0x13 0x13 0x07 0x0c                   .....
    body (0)

#### RECORD 14 Prime 2012-12-07T19:20:28 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x28                   ....(
    decimal
              3    0    0    0   40
    datetime (2012-12-07T19:20:28)
    0000   0xdc 0x14 0x33 0x07 0x0c                   ..3..
    body (0)

#### RECORD 15 Prime 2012-12-07T19:20:52 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-07T19:20:52)
    0000   0xf4 0x14 0x13 0x07 0x0c                   .....
    body (0)

#### RECORD 16 CalForBG 2012-12-07T20:49:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-12-07T20:49:47)
    0000   0xef 0x31 0x34 0x07 0x0c                   .14..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 PumpSuspend 2012-12-07T22:14:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-07T22:14:30)
    0000   0xde 0x0e 0x16 0x07 0x0c                   .....
    body (0)

#### RECORD 18 PumpResume 2012-12-07T22:58:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-07T22:58:20)
    0000   0xd4 0x3a 0x16 0x07 0x0c                   .:...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 19 BolusWizard 2012-12-07T23:13:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-07T23:13:43)
    0000   0xeb 0x0d 0x17 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0    0    0   20  125

#### RECORD 20 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 83, 'amount': 4.6, 'curve': 20},
 {'age': 93, 'amount': 4.6, 'curve': 20},
 {'age': 133, 'amount': 1.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xb8 0x53 0x14 0xb8 0x5d 0x14    \..S..].
    0008   0x40 0x85 0x14                             @..
    decimal
             92   11  184   83   20  184   93   20
             64  133   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2012-12-07T23:13:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-12-07T23:13:43)
    0000   0xeb 0x0d 0x57 0x07 0x0c                   ..W..
    body (0)

#### RECORD 22 ResultTotals 2012-12-07T13:12:07 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x68                   ....h
    decimal
              7    0    0    5  104
    datetime (2012-12-07T13:12:07)
    0000   0xc7 0x0c 0x6d 0xc7 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x4e 0x4e 0x4e 0x01 0x00 0x00    ..NNN...
    0008   0x05 0x68 0x03 0x68 0x3f 0x02 0x00 0x25    .h.h?..%
    0010   0x00 0xaa 0x02 0x00 0x25 0x02 0x00 0x64    ....%..d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x04 0x04    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   78   78   78    1    0    0
              5  104    3  104   63    2    0   37
              0  170    2    0   37    2    0  100
              0    0    0    0    0    0    4    4
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 23 CalForBG 2012-12-08T16:18:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-12-08T16:18:48)
    0000   0xf0 0x12 0x30 0x08 0x0c                   ..0..
    body (0)

#### RECORD 24 BolusWizard 2012-12-08T16:19:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2012-12-08T16:19:25)
    0000   0xd9 0x13 0x10 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0xfe 0x0b 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             15   80   13   45  106  254   11  240
              0    0    0    9  125

#### RECORD 25 Bolus 2012-12-08T16:19:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'programmed': 0.9}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2012-12-08T16:19:25)
    0000   0xd9 0x13 0x50 0x08 0x0c                   ..P..
    body (0)

#### RECORD 26 PumpSuspend 2012-12-08T16:43:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-08T16:43:56)
    0000   0xf8 0x2b 0x10 0x08 0x0c                   .+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 27 PumpResume 2012-12-08T17:01:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-08T17:01:31)
    0000   0xdf 0x01 0x11 0x08 0x0c                   .....
    body (0)

#### RECORD 28 CalForBG 2012-12-08T18:26:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-12-08T18:26:37)
    0000   0xe5 0x1a 0x32 0x08 0x0c                   ..2..
    body (0)

#### RECORD 29 BolusWizard 2012-12-08T18:27:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2012-12-08T18:27:28)
    0000   0xdc 0x1b 0x12 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x00 0x1d 0x00    &P.-j...
    0008   0x00 0x04 0x00 0x1d 0x7d                   ....}
    decimal
             38   80   13   45  106    0   29    0
              0    4    0   29  125

#### RECORD 30 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 133, 'amount': 0.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x24 0x85 0x04                   \.$..
    decimal
             92    5   36  133    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-12-08T18:27:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-12-08T18:27:29)
    0000   0xdd 0x1b 0x52 0x08 0x0c                   ..R..
    body (0)

#### RECORD 32 CalForBG 2012-12-08T19:55:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2012-12-08T19:55:33)
    0000   0xe1 0x37 0x33 0x08 0x0c                   .73..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 BolusWizard 2012-12-08T20:04:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 8,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-08T20:04:06)
    0000   0xc6 0x04 0x14 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              8   80   13   45  106    0    6    0
              0    0    0    6  125

#### RECORD 34 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 2.9, 'curve': 4},
 {'age': 230, 'amount': 0.9, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0x64 0x04 0x24 0xe6 0x04    \.td.$..
    decimal
             92    8  116  100    4   36  230    4
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2012-12-08T20:04:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'programmed': 0.6}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-12-08T20:04:06)
    0000   0xc6 0x04 0x54 0x08 0x0c                   ..T..
    body (0)

#### RECORD 36 CalForBG 2012-12-08T21:11:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2012-12-08T21:11:07)
    0000   0xc7 0x0b 0x35 0x08 0x0c                   ..5..
    body (0)

#### RECORD 37 CalForBG 2012-12-08T21:12:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2012-12-08T21:12:18)
    0000   0xd2 0x0c 0x35 0x08 0x0c                   ..5..
    body (0)

#### RECORD 38 BolusWizard 2012-12-08T22:18:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 19,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-08T22:18:32)
    0000   0xe0 0x12 0x16 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x13 0x50 0x0d 0x2d 0x6a 0x00 0x0e 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
             19   80   13   45  106    0   14    0
              0    0    0   14  125

#### RECORD 39 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 134, 'amount': 0.6, 'curve': 4},
 {'age': 234, 'amount': 2.9, 'curve': 4},
 {'age': 108, 'amount': 0.9, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x18 0x86 0x04 0x74 0xea 0x04    \....t..
    0008   0x24 0x6c 0x14                             $l.
    decimal
             92   11   24  134    4  116  234    4
             36  108   20
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2012-12-08T22:18:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'programmed': 1.4}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2012-12-08T22:18:32)
    0000   0xe0 0x12 0x56 0x08 0x0c                   ..V..
    body (0)

#### RECORD 41 CalForBG 2012-12-08T22:53:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2012-12-08T22:53:52)
    0000   0xf4 0x35 0x36 0x08 0x0c                   .56..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 42 BolusWizard 2012-12-08T22:53:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 216,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.5}
```
    op hex (2)
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2012-12-08T22:53:54)
    0000   0xf6 0x35 0x16 0x08 0x0c                   .5...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x0f 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0   15    0    5  125
    HOUR BITS: [0, 0, 1]
#### RECORD 43 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 1.4, 'curve': 4},
 {'age': 169, 'amount': 0.6, 'curve': 4},
 {'age': 13, 'amount': 2.9, 'curve': 20},
 {'age': 143, 'amount': 0.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x27 0x04 0x18 0xa9 0x04    \.8'....
    0008   0x74 0x0d 0x14 0x24 0x8f 0x14              t..$..
    decimal
             92   14   56   39    4   24  169    4
            116   13   20   36  143   20
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2012-12-08T22:53:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-12-08T22:53:54)
    0000   0xf6 0x35 0x56 0x08 0x0c                   .5V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 BolusWizard 2012-12-08T22:59:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 14,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-08T22:59:08)
    0000   0xc8 0x3b 0x16 0x08 0x0c                   .;...
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [0, 0, 1]
#### RECORD 46 BolusGiven unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 0.35, 'curve': 4},
 {'age': 15, 'amount': 0.15, 'curve': 4},
 {'age': 45, 'amount': 1.4, 'curve': 4},
 {'age': 175, 'amount': 0.6, 'curve': 4},
 {'age': 19, 'amount': 2.9, 'curve': 20},
 {'age': 149, 'amount': 0.9, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x0e 0x05 0x04 0x06 0x0f 0x04    \.......
    0008   0x38 0x2d 0x04 0x18 0xaf 0x04 0x74 0x13    8-....t.
    0010   0x14 0x24 0x95 0x14                        .$..
    decimal
             92   20   14    5    4    6   15    4
             56   45    4   24  175    4  116   19
             20   36  149   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-12-08T22:59:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-12-08T22:59:08)
    0000   0xc8 0x3b 0x56 0x08 0x0c                   .;V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 ResultTotals 2012-12-08T13:12:08 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9c                   .....
    decimal
              7    0    0    4  156
    datetime (2012-12-08T13:12:08)
    0000   0xc8 0x0c 0x6d 0xc8 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x86 0x60 0xd8 0x06 0x00 0x00    ...`....
    0008   0x04 0x9c 0x03 0x78 0x4b 0x01 0x24 0x19    ...xK.$.
    0010   0x00 0x5e 0x01 0x24 0x19 0x01 0x10 0x5d    .^.$...]
    0018   0x00 0x14 0x07 0x00 0x00 0x00 0x06 0x05    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  134   96  216    6    0    0
              4  156    3  120   75    1   36   25
              0   94    1   36   25    1   16   93
              0   20    7    0    0    0    6    5
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 49 BolusWizard 2012-12-09T10:36:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 4,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-09T10:36:41)
    0000   0xe9 0x24 0x0a 0x09 0x0c                   .$...
    body (13)
    hex
    0000   0x04 0x50 0x0d 0x2d 0x6a 0x00 0x03 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x03 0x7d                   ....}
    decimal
              4   80   13   45  106    0    3    0
              0    0    0    3  125
    HOUR BITS: [0, 0, 1]
#### RECORD 50 Bolus 2012-12-09T10:36:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-09T10:36:41)
    0000   0xe9 0x24 0x4a 0x09 0x0c                   .$J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 51 CalForBG 2012-12-09T11:42:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2012-12-09T11:42:28)
    0000   0xdc 0x2a 0x2b 0x09 0x0c                   .*+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 52 BolusWizard 2012-12-09T11:42:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 117,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2012-12-09T11:42:52)
    0000   0xf4 0x2a 0x0b 0x09 0x0c                   .*...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    <P.-j...
    0008   0x00 0x03 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106    0   46    0
              0    3    0   46  125
    HOUR BITS: [0, 0, 1]
#### RECORD 53 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 0.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x0c 0x44 0x04                   \..D.
    decimal
             92    5   12   68    4
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2012-12-09T11:42:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'programmed': 4.6}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2012-12-09T11:42:53)
    0000   0xf5 0x2a 0x4b 0x09 0x0c                   .*K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 CalForBG 2012-12-09T17:16:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2012-12-09T17:16:15)
    0000   0xcf 0x10 0x31 0x09 0x0c                   ..1..
    body (0)

#### RECORD 56 BolusWizard 2012-12-09T17:16:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 170,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2012-12-09T17:16:20)
    0000   0xd4 0x10 0x11 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125

#### RECORD 57 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 76, 'amount': 2.95, 'curve': 20},
 {'age': 86, 'amount': 1.65, 'curve': 20},
 {'age': 146, 'amount': 0.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x76 0x4c 0x14 0x42 0x56 0x14    \.vL.BV.
    0008   0x0c 0x92 0x14                             ...
    decimal
             92   11  118   76   20   66   86   20
             12  146   20
    datetime (unknown)

    body (0)

#### RECORD 58 PumpSuspend 2012-12-09T17:16:23 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-09T17:16:23)
    0000   0xd7 0x10 0x11 0x09 0x0c                   .....
    body (0)

#### RECORD 59 Bolus 2012-12-09T17:16:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'programmed': 0.1}
```
    op hex (4)
    0000   0x01 0x08 0x01 0x00                        ....
    decimal
              1    8    1    0
    datetime (2012-12-09T17:16:20)
    0000   0xd4 0x10 0x51 0x09 0x0c                   ..Q..
    body (0)

#### RECORD 60 PumpResume 2012-12-09T17:16:25 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-09T17:16:25)
    0000   0xd9 0x10 0x11 0x09 0x0c                   .....
    body (0)

#### RECORD 61 CalForBG 2012-12-09T17:16:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2012-12-09T17:16:38)
    0000   0xe6 0x10 0x31 0x09 0x0c                   ..1..
    body (0)

#### RECORD 62 BolusWizard 2012-12-09T17:16:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 170,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2012-12-09T17:16:59)
    0000   0xfb 0x10 0x11 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    1    0    9  125

#### RECORD 63 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 0.1, 'curve': 4},
 {'age': 76, 'amount': 2.95, 'curve': 20},
 {'age': 86, 'amount': 1.65, 'curve': 20},
 {'age': 146, 'amount': 0.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x04 0x02 0x04 0x76 0x4c 0x14    \....vL.
    0008   0x42 0x56 0x14 0x0c 0x92 0x14              BV....
    decimal
             92   14    4    2    4  118   76   20
             66   86   20   12  146   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2012-12-09T17:16:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'programmed': 0.7}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2012-12-09T17:16:59)
    0000   0xfb 0x10 0x51 0x09 0x0c                   ..Q..
    body (0)

#### RECORD 65 CalForBG 2012-12-09T20:01:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2012-12-09T20:01:10)
    0000   0xca 0x01 0x34 0x09 0x0c                   ..4..
    body (0)

#### RECORD 66 BolusWizard 2012-12-09T20:01:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 103,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2012-12-09T20:01:32)
    0000   0xe0 0x01 0x14 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0xff 0x27 0xf0    3P.-j.'.
    0008   0x00 0x02 0x00 0x26 0x7d                   ...&}
    decimal
             51   80   13   45  106  255   39  240
              0    2    0   38  125

#### RECORD 67 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 167, 'amount': 0.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x20 0xa7 0x04                   \. ..
    decimal
             92    5   32  167    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2012-12-09T20:01:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'programmed': 3.8}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2012-12-09T20:01:32)
    0000   0xe0 0x01 0x54 0x09 0x0c                   ..T..
    body (0)

#### RECORD 69 ResultTotals 2012-12-09T13:12:09 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x00                   .....
    decimal
              7    0    0    5    0
    datetime (2012-12-09T13:12:09)
    0000   0xc9 0x0c 0x6d 0xc9 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8c 0x67 0xaa 0x04 0x00 0x00    ...g....
    0008   0x05 0x00 0x03 0x84 0x46 0x01 0x7c 0x1e    ....F.|.
    0010   0x00 0x73 0x01 0x7c 0x1e 0x01 0x5c 0x5c    .s.|..\\
    0018   0x00 0x20 0x08 0x00 0x00 0x00 0x05 0x03    . ......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  140  103  170    4    0    0
              5    0    3  132   70    1  124   30
              0  115    1  124   30    1   92   92
              0   32    8    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 70 CalForBG 2012-12-10T03:50:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2012-12-10T03:50:27)
    0000   0xdb 0x32 0x23 0x0a 0x8c                   .2#..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 71 BolusWizard 2012-12-10T03:50:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 411,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2012-12-10T03:50:31)
    0000   0xdf 0x32 0x03 0x0a 0x0c                   .2...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3f 0x00 0x00    .Q.-j?..
    0008   0x00 0x00 0x00 0x3f 0x7d                   ...?}
    decimal
              0   81   13   45  106   63    0    0
              0    0    0   63  125
    HOUR BITS: [0, 0, 1]
#### RECORD 72 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 210, 'amount': 0.15, 'curve': 20},
 {'age': 220, 'amount': 3.65, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x06 0xd2 0x14 0x92 0xdc 0x14    \.......
    decimal
             92    8    6  210   20  146  220   20
    datetime (unknown)

    body (0)

#### RECORD 73 PumpSuspend 2012-12-10T03:50:51 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-10T03:50:51)
    0000   0xf3 0x32 0x03 0x0a 0x0c                   .2...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 74 Bolus 2012-12-10T03:50:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.3, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x3f 0x05 0x00                        .?..
    decimal
              1   63    5    0
    datetime (2012-12-10T03:50:31)
    0000   0xdf 0x32 0x43 0x0a 0x0c                   .2C..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 75 PumpResume 2012-12-10T03:51:21 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-10T03:51:21)
    0000   0xd5 0x33 0x03 0x0a 0x0c                   .3...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 76 CalForBG 2012-12-10T03:52:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2012-12-10T03:52:28)
    0000   0xdc 0x34 0x23 0x0a 0x8c                   .4#..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 77 BolusWizard 2012-12-10T03:52:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 411,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2012-12-10T03:52:35)
    0000   0xe3 0x34 0x03 0x0a 0x0c                   .4...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3f 0x00 0x00    .Q.-j?..
    0008   0x00 0x05 0x00 0x3a 0x7d                   ...:}
    decimal
              0   81   13   45  106   63    0    0
              0    5    0   58  125
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-13.data: 78 records`
