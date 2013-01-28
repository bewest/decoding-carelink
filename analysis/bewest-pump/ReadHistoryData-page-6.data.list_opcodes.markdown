## START logs/ReadHistoryData-page-6.data
#### RECORD 0 TempBasal 2012-12-30T21:45:37 head[2], body[1] op[0x33]

    op hex (2)
    0000   0x33 0x2a                                  3*
    decimal
             51   42
    datetime (2012-12-30T21:45:37)
    0000   0xe5 0x2d 0x15 0x1e 0x0c                   .-...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 0, 1]
#### RECORD 1 EndTempBasal 2012-12-30T21:45:37 head[2], body[0] op[0x16]

    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2012-12-30T21:45:37)
    0000   0xe5 0x2d 0x15 0x1e 0x0c                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 CalForBG 2012-12-30T21:45:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2012-12-30T21:45:54)
    0000   0xf6 0x2d 0x35 0x1e 0x0c                   .-5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalForBG 2012-12-30T21:47:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2012-12-30T21:47:53)
    0000   0xf5 0x2f 0x35 0x1e 0x0c                   ./5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BolusWizard 2012-12-30T21:48:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 184,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.9}
```
    op hex (2)
    0000   0x5b 0xb8                                  [.
    decimal
             91  184
    datetime (2012-12-30T21:48:17)
    0000   0xd1 0x30 0x15 0x1e 0x0c                   .0...
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0x0d 0x24 0x00    0P.-j.$.
    0008   0x00 0x13 0x00 0x24 0x7d                   ...$}
    decimal
             48   80   13   45  106   13   36    0
              0   19    0   36  125
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BolusGiven unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 0.3, 'curve': 4},
 {'age': 54, 'amount': 1.8, 'curve': 4},
 {'age': 98, 'amount': 0.15, 'curve': 20},
 {'age': 108, 'amount': 0.2, 'curve': 20},
 {'age': 118, 'amount': 0.25, 'curve': 20},
 {'age': 128, 'amount': 0.2, 'curve': 20},
 {'age': 138, 'amount': 0.2, 'curve': 20},
 {'age': 148, 'amount': 0.25, 'curve': 20},
 {'age': 158, 'amount': 0.2, 'curve': 20},
 {'age': 168, 'amount': 0.25, 'curve': 20},
 {'age': 178, 'amount': 0.2, 'curve': 20},
 {'age': 188, 'amount': 2.0, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x0c 0x04 0x04 0x48 0x36 0x04    \&...H6.
    0008   0x06 0x62 0x14 0x08 0x6c 0x14 0x0a 0x76    .b..l..v
    0010   0x14 0x08 0x80 0x14 0x08 0x8a 0x14 0x0a    ........
    0018   0x94 0x14 0x08 0x9e 0x14 0x0a 0xa8 0x14    ........
    0020   0x08 0xb2 0x14 0x50 0xbc 0x14              ...P..
    decimal
             92   38   12    4    4   72   54    4
              6   98   20    8  108   20   10  118
             20    8  128   20    8  138   20   10
            148   20    8  158   20   10  168   20
              8  178   20   80  188   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2012-12-30T21:48:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-12-30T21:48:17)
    0000   0xd1 0x30 0x55 0x1e 0x0c                   .0U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 ResultTotals 2012-12-30T13:12:30 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xac                   .....
    decimal
              7    0    0    5  172
    datetime (2012-12-30T13:12:30)
    0000   0xde 0x0c 0x6d 0xde 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xa2 0x54 0xd2 0x09 0x00 0x00    ...T....
    0008   0x05 0xac 0x03 0x78 0x3d 0x02 0x34 0x27    ...x=.4'
    0010   0x00 0x91 0x02 0x34 0x27 0x01 0x9e 0x49    ...4'..I
    0018   0x00 0x96 0x1b 0x00 0x00 0x00 0x06 0x03    ........
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  162   84  210    9    0    0
              5  172    3  120   61    2   52   39
              0  145    2   52   39    1  158   73
              0  150   27    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 8 CalForBG 2012-12-31T00:06:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2012-12-31T00:06:37)
    0000   0xe5 0x06 0x20 0x1f 0x0c                   .. ..
    body (0)

#### RECORD 9 CalForBG 2012-12-31T00:57:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2012-12-31T00:57:33)
    0000   0xe1 0x39 0x20 0x1f 0x0c                   .9 ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 10 CalForBG 2012-12-31T09:13:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 213}
```
    op hex (2)
    0000   0x0a 0xd5                                  ..
    decimal
             10  213
    datetime (2012-12-31T09:13:57)
    0000   0xf9 0x0d 0x29 0x1f 0x0c                   ..)..
    body (0)

#### RECORD 11 CalForBG 2012-12-31T09:13:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 211}
```
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2012-12-31T09:13:59)
    0000   0xfb 0x0d 0x29 0x1f 0x0c                   ..)..
    body (0)

#### RECORD 12 CalForBG 2012-12-31T09:14:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 210}
```
    op hex (2)
    0000   0x0a 0xd2                                  ..
    decimal
             10  210
    datetime (2012-12-31T09:14:00)
    0000   0xc0 0x0e 0x29 0x1f 0x0c                   ..)..
    body (0)

#### RECORD 13 BolusWizard 2012-12-31T09:14:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 210,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xd2                                  [.
    decimal
             91  210
    datetime (2012-12-31T09:14:05)
    0000   0xc5 0x0e 0x09 0x1f 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0    0    0   18  125

#### RECORD 14 Bolus 2012-12-31T09:14:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-12-31T09:14:05)
    0000   0xc5 0x0e 0x49 0x1f 0x0c                   ..I..
    body (0)

#### RECORD 15 CalForBG 2012-12-31T11:43:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2012-12-31T11:43:03)
    0000   0xc3 0x2b 0x2b 0x1f 0x0c                   .++..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 16 CalForBG 2012-12-31T11:48:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2012-12-31T11:48:28)
    0000   0xdc 0x30 0x2b 0x1f 0x0c                   .0+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 CalForBG 2012-12-31T11:49:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2012-12-31T11:49:02)
    0000   0xc2 0x31 0x2b 0x1f 0x0c                   .1+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 CalForBG 2012-12-31T11:49:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2012-12-31T11:49:55)
    0000   0xf7 0x31 0x2b 0x1f 0x0c                   .1+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 19 BolusWizard 2012-12-31T11:50:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2012-12-31T11:50:13)
    0000   0xcd 0x32 0x0b 0x1f 0x0c                   .2...
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0xfd 0x09 0xf0    .P.-j...
    0008   0x00 0x05 0x00 0x06 0x7d                   ....}
    decimal
             12   80   13   45  106  253    9  240
              0    5    0    6  125
    HOUR BITS: [0, 0, 1]
#### RECORD 20 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 156, 'amount': 1.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x48 0x9c 0x04                   \.H..
    decimal
             92    5   72  156    4
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2012-12-31T11:50:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'programmed': 0.6}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-12-31T11:50:13)
    0000   0xcd 0x32 0x4b 0x1f 0x0c                   .2K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 CalForBG 2012-12-31T13:12:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2012-12-31T13:12:30)
    0000   0xde 0x0c 0x2d 0x1f 0x0c                   ..-..
    body (0)

#### RECORD 23 BolusWizard 2012-12-31T13:13:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 85,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2012-12-31T13:13:13)
    0000   0xcd 0x0d 0x0d 0x1f 0x0c                   .....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0xfb 0x16 0xf0    .P.-j...
    0008   0x00 0x05 0x00 0x11 0x7d                   ....}
    decimal
             29   80   13   45  106  251   22  240
              0    5    0   17  125

#### RECORD 24 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 89, 'amount': 0.6, 'curve': 4},
 {'age': 239, 'amount': 1.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0x59 0x04 0x48 0xef 0x04    \..Y.H..
    decimal
             92    8   24   89    4   72  239    4
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2012-12-31T13:13:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'programmed': 1.7}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2012-12-31T13:13:13)
    0000   0xcd 0x0d 0x4d 0x1f 0x0c                   ..M..
    body (0)

#### RECORD 26 BolusWizard 2012-12-31T14:19:41 head[2], body[13] op[0x5b]
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
    datetime (2012-12-31T14:19:41)
    0000   0xe9 0x13 0x0e 0x1f 0x0c                   .....
    body (13)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             22   80   13   45  106    0   16    0
              0    0    0   16  125

#### RECORD 27 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 0.55, 'curve': 4},
 {'age': 75, 'amount': 1.15, 'curve': 4},
 {'age': 155, 'amount': 0.6, 'curve': 4},
 {'age': 49, 'amount': 1.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x16 0x41 0x04 0x2e 0x4b 0x04    \..A..K.
    0008   0x18 0x9b 0x04 0x48 0x31 0x14              ...H1.
    decimal
             92   14   22   65    4   46   75    4
             24  155    4   72   49   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2012-12-31T14:19:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'programmed': 1.6}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-12-31T14:19:41)
    0000   0xe9 0x13 0x4e 0x1f 0x0c                   ..N..
    body (0)

#### RECORD 29 CalForBG 2012-12-31T16:06:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2012-12-31T16:06:43)
    0000   0xeb 0x06 0x30 0x1f 0x0c                   ..0..
    body (0)

#### RECORD 30 CalForBG 2012-12-31T19:28:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2012-12-31T19:28:02)
    0000   0xc2 0x1c 0x33 0x1f 0x0c                   ..3..
    body (0)

#### RECORD 31 BolusWizard 2012-12-31T19:28:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2012-12-31T19:28:58)
    0000   0xfa 0x1c 0x13 0x1f 0x0c                   .....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0x01 0x23 0x00    .P.-j.#.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             46   80   13   45  106    1   35    0
              0    0    0   36  125

#### RECORD 32 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 58, 'amount': 1.6, 'curve': 20},
 {'age': 118, 'amount': 0.55, 'curve': 20},
 {'age': 128, 'amount': 1.15, 'curve': 20},
 {'age': 208, 'amount': 0.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x40 0x3a 0x14 0x16 0x76 0x14    \.@:..v.
    0008   0x2e 0x80 0x14 0x18 0xd0 0x14              ......
    decimal
             92   14   64   58   20   22  118   20
             46  128   20   24  208   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2012-12-31T19:28:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-12-31T19:28:58)
    0000   0xfa 0x1c 0x53 0x1f 0x0c                   ..S..
    body (0)

#### RECORD 34 LowReservoir 2012-12-31T19:31:27 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-12-31T19:31:27)
    0000   0xdb 0x1f 0x13 0x1f 0x0c                   .....
    body (0)

#### RECORD 35 CalForBG 2012-12-31T21:52:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2012-12-31T21:52:47)
    0000   0xef 0x34 0x35 0x1f 0x0c                   .45..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 CalForBG 2012-12-31T21:53:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2012-12-31T21:53:30)
    0000   0xde 0x35 0x35 0x1f 0x0c                   .55..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 BolusWizard 2012-12-31T21:53:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 141,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.1}
```
    op hex (2)
    0000   0x5b 0x8d                                  [.
    decimal
             91  141
    datetime (2012-12-31T21:53:41)
    0000   0xe9 0x35 0x15 0x1f 0x0c                   .5...
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0x03 0x1a 0x00    #P.-j...
    0008   0x00 0x0b 0x00 0x1a 0x7d                   ....}
    decimal
             35   80   13   45  106    3   26    0
              0   11    0   26  125
    HOUR BITS: [0, 0, 1]
#### RECORD 38 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 149, 'amount': 3.6, 'curve': 4},
 {'age': 203, 'amount': 1.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x90 0x95 0x04 0x40 0xcb 0x14    \....@..
    decimal
             92    8  144  149    4   64  203   20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2012-12-31T21:53:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-12-31T21:53:41)
    0000   0xe9 0x35 0x55 0x1f 0x0c                   .5U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 ResultTotals 2012-12-31T13:12:31 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x60                   ....`
    decimal
              7    0    0    5   96
    datetime (2012-12-31T13:12:31)
    0000   0xdf 0x0c 0x6d 0xdf 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x7f 0x4f 0xd5 0x0e 0x00 0x00    ...O....
    0008   0x05 0x60 0x03 0x84 0x41 0x01 0xdc 0x23    .`..A..#
    0010   0x00 0x90 0x01 0xdc 0x23 0x01 0x90 0x54    ....#..T
    0018   0x00 0x4c 0x10 0x00 0x00 0x00 0x06 0x04    .L......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  127   79  213   14    0    0
              5   96    3  132   65    1  220   35
              0  144    1  220   35    1  144   84
              0   76   16    0    0    0    6    4
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 41 CalForBG 2013-01-01T00:14:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2013-01-01T00:14:46)
    0000   0x2e 0x4e 0x20 0x01 0x0d                   .N ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 42 LowReservoir 2013-01-01T03:52:30 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-01-01T03:52:30)
    0000   0x1e 0x74 0x03 0x01 0x0d                   .t...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 43 PumpSuspend 2013-01-01T10:10:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-01-01T10:10:20)
    0000   0x14 0x4a 0x0a 0x01 0x0d                   .J...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 44 PumpResume 2013-01-01T10:26:17 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-01-01T10:26:17)
    0000   0x11 0x5a 0x0a 0x01 0x0d                   .Z...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 45 Rewind 2013-01-01T10:26:23 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-01-01T10:26:23)
    0000   0x17 0x5a 0x0a 0x01 0x0d                   .Z...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 46 Prime 2013-01-01T10:27:25 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x29                   ....)
    decimal
              3    0    0    0   41
    datetime (2013-01-01T10:27:25)
    0000   0x19 0x5b 0x2a 0x01 0x0d                   .[*..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 47 Prime 2013-01-01T10:27:46 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-01-01T10:27:46)
    0000   0x2e 0x5b 0x0a 0x01 0x0d                   .[...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 48 CalForBG 2013-01-01T10:46:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-01-01T10:46:21)
    0000   0x15 0x6e 0x2a 0x01 0x0d                   .n*..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2013-01-01T10:46:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 101,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 67,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x65                                  [e
    decimal
             91  101
    datetime (2013-01-01T10:46:32)
    0000   0x20 0x6e 0x0a 0x01 0x0d                    n...
    body (13)
    hex
    0000   0x43 0x50 0x0d 0x2d 0x6a 0xff 0x33 0xf0    CP.-j.3.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             67   80   13   45  106  255   51  240
              0    0    0   50  125
    HOUR BITS: [0, 1, 1]
#### RECORD 50 Bolus 2013-01-01T10:46:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'programmed': 5.0}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-01-01T10:46:32)
    0000   0x20 0x6e 0x4a 0x01 0x0d                    nJ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 51 CalForBG 2013-01-01T16:41:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-01-01T16:41:04)
    0000   0x04 0x69 0x30 0x01 0x0d                   .i0..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 52 BolusWizard 2013-01-01T16:41:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-01-01T16:41:44)
    0000   0x2c 0x69 0x10 0x01 0x0d                   ,i...
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xff 0x26 0xf0    2P.-j.&.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             50   80   13   45  106  255   38  240
              0    0    0   37  125
    HOUR BITS: [0, 1, 1]
#### RECORD 53 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 5.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xc8 0x65 0x14                   \..e.
    decimal
             92    5  200  101   20
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-01-01T16:41:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'programmed': 3.7}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2013-01-01T16:41:44)
    0000   0x2c 0x69 0x50 0x01 0x0d                   ,iP..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 55 CalForBG 2013-01-01T18:15:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-01-01T18:15:39)
    0000   0x27 0x4f 0x32 0x01 0x0d                   'O2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 56 BolusWizard 2013-01-01T18:15:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.2}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-01-01T18:15:44)
    0000   0x2c 0x4f 0x12 0x01 0x0d                   ,O...
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0   22    0   13  125
    HOUR BITS: [0, 1, 0]
#### RECORD 57 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 0.3, 'curve': 4},
 {'age': 101, 'amount': 3.4, 'curve': 4},
 {'age': 195, 'amount': 5.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x5b 0x04 0x88 0x65 0x04    \..[..e.
    0008   0xc8 0xc3 0x14                             ...
    decimal
             92   11   12   91    4  136  101    4
            200  195   20
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-01-01T18:15:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-01-01T18:15:45)
    0000   0x2d 0x4f 0x52 0x01 0x0d                   -OR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 59 ResultTotals 2013-02-01T13:13:01 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x06                   .....
    decimal
              7    0    0    5    6
    datetime (2013-02-01T13:13:01)
    0000   0x01 0x8d 0x6d 0x01 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x60 0x45 0x6c 0x04 0x00 0x00    ..`El...
    0008   0x05 0x06 0x03 0x76 0x45 0x01 0x90 0x1f    ...vE...
    0010   0x00 0x87 0x01 0x90 0x1f 0x01 0x90 0x64    .......d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   96   69  108    4    0    0
              5    6    3  118   69    1  144   31
              0  135    1  144   31    1  144  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 60 CalForBG 2013-01-02T01:25:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-01-02T01:25:50)
    0000   0x32 0x59 0x21 0x02 0x0d                   2Y!..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 61 CalForBG 2013-01-02T09:26:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2013-01-02T09:26:31)
    0000   0x1f 0x5a 0x29 0x02 0x0d                   .Z)..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 62 BolusWizard 2013-01-02T09:27:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 73,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x49                                  [I
    decimal
             91   73
    datetime (2013-01-02T09:27:35)
    0000   0x23 0x5b 0x09 0x02 0x0d                   #[...
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xf8 0x26 0xf0    2P.-j.&.
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             50   80   13   45  106  248   38  240
              0    0    0   30  125
    HOUR BITS: [0, 1, 0]
#### RECORD 63 Bolus 2013-01-02T09:27:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'programmed': 3.0}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-01-02T09:27:35)
    0000   0x23 0x5b 0x49 0x02 0x0d                   #[I..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 64 CalForBG 2013-01-02T13:37:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2013-01-02T13:37:13)
    0000   0x0d 0x65 0x2d 0x02 0x0d                   .e-..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 65 BolusWizard 2013-01-02T13:37:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 234,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.1,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xea                                  [.
    decimal
             91  234
    datetime (2013-01-02T13:37:35)
    0000   0x23 0x65 0x0d 0x02 0x0d                   #e...
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0x18 0x25 0x00    1P.-j.%.
    0008   0x00 0x00 0x00 0x3d 0x7d                   ...=}
    decimal
             49   80   13   45  106   24   37    0
              0    0    0   61  125
    HOUR BITS: [0, 1, 1]
#### RECORD 66 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 253, 'amount': 3.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0xfd 0x04                   \.x..
    decimal
             92    5  120  253    4
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-01-02T13:37:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.1, 'programmed': 6.1}
```
    op hex (4)
    0000   0x01 0x3d 0x3d 0x00                        .==.
    decimal
              1   61   61    0
    datetime (2013-01-02T13:37:35)
    0000   0x23 0x65 0x4d 0x02 0x0d                   #eM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 68 CalForBG 2013-01-02T17:15:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 197}
```
    op hex (2)
    0000   0x0a 0xc5                                  ..
    decimal
             10  197
    datetime (2013-01-02T17:15:44)
    0000   0x2c 0x4f 0x31 0x02 0x0d                   ,O1..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 69 BolusWizard 2013-01-02T17:15:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 197,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0xc5                                  [.
    decimal
             91  197
    datetime (2013-01-02T17:15:46)
    0000   0x2e 0x4f 0x11 0x02 0x0d                   .O...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    5    0   11  125
    HOUR BITS: [0, 1, 0]
#### RECORD 70 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 221, 'amount': 6.1, 'curve': 4},
 {'age': 215, 'amount': 3.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xf4 0xdd 0x04 0x78 0xd7 0x14    \....x..
    decimal
             92    8  244  221    4  120  215   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-01-02T17:15:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-01-02T17:15:47)
    0000   0x2f 0x4f 0x51 0x02 0x0d                   /OQ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 72 CalForBG 2013-01-02T18:32:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-01-02T18:32:01)
    0000   0x01 0x60 0x32 0x02 0x0d                   .`2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 73 BolusWizard 2013-01-02T18:33:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 123,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.8}
```
    op hex (2)
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2013-01-02T18:33:01)
    0000   0x01 0x61 0x12 0x02 0x0d                   .a...
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x00 0x1d 0x00    &P.-j...
    0008   0x00 0x08 0x00 0x1d 0x7d                   ....}
    decimal
             38   80   13   45  106    0   29    0
              0    8    0   29  125
    HOUR BITS: [0, 1, 1]
#### RECORD 74 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 1.1, 'curve': 4},
 {'age': 43, 'amount': 6.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x4f 0x04 0xf4 0x2b 0x14    \.,O..+.
    decimal
             92    8   44   79    4  244   43   20
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2013-01-02T18:33:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-01-02T18:33:01)
    0000   0x01 0x61 0x52 0x02 0x0d                   .aR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 76 CalForBG 2013-01-02T21:20:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2013-01-02T21:20:53)
    0000   0x35 0x54 0x35 0x02 0x0d                   5T5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 77 BolusWizard 2013-01-02T21:20:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 176,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.6}
```
    op hex (2)
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2013-01-02T21:20:55)
    0000   0x37 0x54 0x15 0x02 0x0d                   7T...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    6    0    5  125
    HOUR BITS: [0, 1, 0]
#### RECORD 78 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 166, 'amount': 1.4, 'curve': 4},
 {'age': 176, 'amount': 1.5, 'curve': 4},
 {'age': 246, 'amount': 1.1, 'curve': 4},
 {'age': 210, 'amount': 6.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0xa6 0x04 0x3c 0xb0 0x04    \.8..<..
    0008   0x2c 0xf6 0x04 0xf4 0xd2 0x14              ,.....
    decimal
             92   14   56  166    4   60  176    4
             44  246    4  244  210   20
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2013-01-02T21:20:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-01-02T21:20:55)
    0000   0x37 0x54 0x55 0x02 0x0d                   7TU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 80 ResultTotals (2000, 2, 0, 0, 13, 2) head[5], body[36] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xa4                   .....
    decimal
              7    0    0    5  164
    datetime ((2000, 2, 0, 0, 13, 2))
    0000   0x02 0x8d 0x00 0x00 0x00                   .....
    body (36)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0xe1 0x1f                        ....
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0  225   31
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-6.data: 81 records`
