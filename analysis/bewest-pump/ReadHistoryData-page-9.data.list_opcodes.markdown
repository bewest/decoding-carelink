## START logs/ReadHistoryData-page-9.data
#### RECORD 0 Rewind 2012-12-21T14:41:41 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-21T14:41:41)
    0000   0xe9 0x29 0x0e 0x15 0x0c                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Prime 2012-12-21T14:43:52 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2c                   ....,
    decimal
              3    0    0    0   44
    datetime (2012-12-21T14:43:52)
    0000   0xf4 0x2b 0x2e 0x15 0x0c                   .+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 Prime 2012-12-21T14:44:18 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-21T14:44:18)
    0000   0xd2 0x2c 0x0e 0x15 0x0c                   .,...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalForBG 2012-12-21T18:18:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-21T18:18:19)
    0000   0xd3 0x12 0x32 0x15 0x0c                   ..2..
    body (0)

#### RECORD 4 BolusWizard 2012-12-21T18:18:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2012-12-21T18:18:23)
    0000   0xd7 0x12 0x12 0x15 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    2    0   11  125

#### RECORD 5 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 234, 'amount': 2.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0xea 0x04                   \.\..
    decimal
             92    5   92  234    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2012-12-21T18:18:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2012-12-21T18:18:23)
    0000   0xd7 0x12 0x52 0x15 0x0c                   ..R..
    body (0)

#### RECORD 7 CalForBG 2012-12-21T18:20:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-21T18:20:31)
    0000   0xdf 0x14 0x32 0x15 0x0c                   ..2..
    body (0)

#### RECORD 8 CalForBG 2012-12-21T18:20:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-21T18:20:52)
    0000   0xf4 0x14 0x32 0x15 0x0c                   ..2..
    body (0)

#### RECORD 9 BolusWizard 2012-12-21T18:21:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.3}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2012-12-21T18:21:04)
    0000   0xc4 0x15 0x12 0x15 0x0c                   .....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x0d 0x17 0x00    .P.-j...
    0008   0x00 0x0d 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106   13   23    0
              0   13    0   23  125

#### RECORD 10 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 1.1, 'curve': 4},
 {'age': 237, 'amount': 2.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x07 0x04 0x5c 0xed 0x04    \.,..\..
    decimal
             92    8   44    7    4   92  237    4
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2012-12-21T18:21:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-12-21T18:21:04)
    0000   0xc4 0x15 0x52 0x15 0x0c                   ..R..
    body (0)

#### RECORD 12 CalForBG 2012-12-21T21:23:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2012-12-21T21:23:40)
    0000   0xe8 0x17 0x35 0x15 0x0c                   ..5..
    body (0)

#### RECORD 13 BolusWizard 2012-12-21T21:24:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2012-12-21T21:24:10)
    0000   0xca 0x18 0x15 0x15 0x0c                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x00 0x1b 0x00    $P.-j...
    0008   0x00 0x05 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    0   27    0
              0    5    0   27  125

#### RECORD 14 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 190, 'amount': 3.4, 'curve': 4},
 {'age': 164, 'amount': 2.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x88 0xbe 0x04 0x5c 0xa4 0x14    \....\..
    decimal
             92    8  136  190    4   92  164   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2012-12-21T21:24:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'programmed': 2.7}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x02                        ....
    decimal
              1   27   27    2
    datetime (2012-12-21T21:24:10)
    0000   0xca 0x18 0x75 0x15 0x0c                   ..u..
    body (0)

#### RECORD 16 ResultTotals 2012-12-21T13:12:21 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc4                   .....
    decimal
              7    0    0    4  196
    datetime (2012-12-21T13:12:21)
    0000   0xd5 0x0c 0x6d 0xd5 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xa2 0x7e 0xba 0x05 0x00 0x00    ...~....
    0008   0x04 0xc4 0x03 0x74 0x48 0x01 0x50 0x1c    ...tH.P.
    0010   0x00 0x61 0x01 0x50 0x1c 0x01 0x24 0x57    .a.P..$W
    0018   0x00 0x2c 0x0d 0x00 0x00 0x00 0x04 0x03    .,......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  162  126  186    5    0    0
              4  196    3  116   72    1   80   28
              0   97    1   80   28    1   36   87
              0   44   13    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 17 CalForBG 2012-12-22T10:16:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2012-12-22T10:16:04)
    0000   0xc4 0x10 0x2a 0x16 0x0c                   ..*..
    body (0)

#### RECORD 18 BolusWizard 2012-12-22T10:16:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 116,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2012-12-22T10:16:27)
    0000   0xdb 0x10 0x0a 0x16 0x0c                   .....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x00 0x1e 0x00    (P.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             40   80   13   45  106    0   30    0
              0    0    0   30  125

#### RECORD 19 Bolus 2012-12-22T10:16:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'programmed': 3.0}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2012-12-22T10:16:27)
    0000   0xdb 0x10 0x4a 0x16 0x0c                   ..J..
    body (0)

#### RECORD 20 BolusWizard 2012-12-22T10:27:01 head[2], body[13] op[0x5b]
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
    datetime (2012-12-22T10:27:01)
    0000   0xc1 0x1b 0x0a 0x16 0x0c                   .....
    body (13)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             22   80   13   45  106    0   16    0
              0    0    0   16  125

#### RECORD 21 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 3.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x0d 0x04                   \.x..
    decimal
             92    5  120   13    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2012-12-22T10:27:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'programmed': 1.6}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-12-22T10:27:01)
    0000   0xc1 0x1b 0x4a 0x16 0x0c                   ..J..
    body (0)

#### RECORD 23 BolusWizard 2012-12-22T10:34:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 5,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-22T10:34:30)
    0000   0xde 0x22 0x0a 0x16 0x0c                   ."...
    body (13)
    hex
    0000   0x05 0x50 0x0d 0x2d 0x6a 0x00 0x03 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x03 0x7d                   ....}
    decimal
              5   80   13   45  106    0    3    0
              0    0    0    3  125
    HOUR BITS: [0, 0, 1]
#### RECORD 24 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 1.6, 'curve': 4},
 {'age': 20, 'amount': 3.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x0a 0x04 0x78 0x14 0x04    \.@..x..
    decimal
             92    8   64   10    4  120   20    4
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2012-12-22T10:34:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-22T10:34:30)
    0000   0xde 0x22 0x4a 0x16 0x0c                   ."J..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 PumpSuspend 2012-12-22T13:12:41 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-22T13:12:41)
    0000   0xe9 0x0c 0x0d 0x16 0x0c                   .....
    body (0)

#### RECORD 27 PumpResume 2012-12-22T13:29:51 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-22T13:29:51)
    0000   0xf3 0x1d 0x0d 0x16 0x0c                   .....
    body (0)

#### RECORD 28 CalForBG 2012-12-22T14:08:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 58}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2012-12-22T14:08:38)
    0000   0xe6 0x08 0x2e 0x16 0x8c                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 BolusWizard 2012-12-22T14:10:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 314,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 7.5,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0x3a                                  [:
    decimal
             91   58
    datetime (2012-12-22T14:10:20)
    0000   0xd4 0x0a 0x0e 0x16 0x0c                   .....
    body (13)
    hex
    0000   0x2f 0x51 0x0d 0x2d 0x6a 0x2a 0x24 0x00    /Q.-j*$.
    0008   0x00 0x03 0x00 0x4b 0x7d                   ...K}
    decimal
             47   81   13   45  106   42   36    0
              0    3    0   75  125

#### RECORD 30 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 216, 'amount': 0.3, 'curve': 4},
 {'age': 226, 'amount': 1.6, 'curve': 4},
 {'age': 236, 'amount': 3.0, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0xd8 0x04 0x40 0xe2 0x04    \....@..
    0008   0x78 0xec 0x04                             x..
    decimal
             92   11   12  216    4   64  226    4
            120  236    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-12-22T14:10:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.5, 'programmed': 7.5}
```
    op hex (4)
    0000   0x01 0x4b 0x4b 0x00                        .KK.
    decimal
              1   75   75    0
    datetime (2012-12-22T14:10:20)
    0000   0xd4 0x0a 0x4e 0x16 0x0c                   ..N..
    body (0)

#### RECORD 32 CalForBG 2012-12-22T16:02:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 53}
```
    op hex (2)
    0000   0x0a 0x35                                  .5
    decimal
             10   53
    datetime (2012-12-22T16:02:39)
    0000   0xe7 0x02 0x30 0x16 0x0c                   ..0..
    body (0)

#### RECORD 33 CalForBG 2012-12-22T16:42:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2012-12-22T16:42:17)
    0000   0xd1 0x2a 0x30 0x16 0x0c                   .*0..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 34 CalForBG 2012-12-22T17:21:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2012-12-22T17:21:02)
    0000   0xc2 0x15 0x31 0x16 0x0c                   ..1..
    body (0)

#### RECORD 35 CalForBG 2012-12-22T18:41:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2012-12-22T18:41:23)
    0000   0xd7 0x29 0x32 0x16 0x0c                   .)2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 BolusWizard 2012-12-22T18:42:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 155,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2012-12-22T18:42:27)
    0000   0xdb 0x2a 0x12 0x16 0x0c                   .*...
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0x06 0x21 0x00    ,P.-j.!.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             44   80   13   45  106    6   33    0
              0    0    0   39  125
    HOUR BITS: [0, 0, 1]
#### RECORD 37 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 2.05, 'curve': 20},
 {'age': 22, 'amount': 5.45, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x52 0x0c 0x14 0xda 0x16 0x14    \.R.....
    decimal
             92    8   82   12   20  218   22   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2012-12-22T18:42:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'programmed': 3.9}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2012-12-22T18:42:27)
    0000   0xdb 0x2a 0x52 0x16 0x0c                   .*R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 ResultTotals 2012-12-22T13:12:22 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x04                   .....
    decimal
              7    0    0    6    4
    datetime (2012-12-22T13:12:22)
    0000   0xd6 0x0c 0x6d 0xd6 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x93 0x35 0x3a 0x06 0x00 0x00    ...5:...
    0008   0x06 0x04 0x03 0x78 0x3a 0x02 0x8c 0x2a    ...x:..*
    0010   0x00 0x9e 0x02 0x8c 0x2a 0x01 0xd8 0x48    ....*..H
    0018   0x00 0xb4 0x1c 0x00 0x00 0x00 0x05 0x03    ........
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  147   53   58    6    0    0
              6    4    3  120   58    2  140   42
              0  158    2  140   42    1  216   72
              0  180   28    0    0    0    5    3
              0    2    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 40 PumpSuspend 2012-12-23T08:24:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-23T08:24:49)
    0000   0xf1 0x18 0x08 0x17 0x0c                   .....
    body (0)

#### RECORD 41 PumpResume 2012-12-23T08:39:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-23T08:39:30)
    0000   0xde 0x27 0x08 0x17 0x0c                   .'...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 42 CalForBG 2012-12-23T08:45:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-12-23T08:45:35)
    0000   0xe3 0x2d 0x28 0x17 0x0c                   .-(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 CalForBG 2012-12-23T08:51:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-12-23T08:51:56)
    0000   0xf8 0x33 0x28 0x17 0x0c                   .3(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 44 BolusWizard 2012-12-23T08:52:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 100,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2012-12-23T08:52:04)
    0000   0xc4 0x34 0x08 0x17 0x0c                   .4...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0xfe 0x2e 0xf0    <P.-j...
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
             60   80   13   45  106  254   46  240
              0    0    0   44  125
    HOUR BITS: [0, 0, 1]
#### RECORD 45 Bolus 2012-12-23T08:52:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'programmed': 4.4}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2012-12-23T08:52:05)
    0000   0xc5 0x34 0x48 0x17 0x0c                   .4H..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 46 CalForBG 2012-12-23T13:13:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 191}
```
    op hex (2)
    0000   0x0a 0xbf                                  ..
    decimal
             10  191
    datetime (2012-12-23T13:13:22)
    0000   0xd6 0x0d 0x2d 0x17 0x0c                   ..-..
    body (0)

#### RECORD 47 BolusWizard 2012-12-23T13:13:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 191,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xbf                                  [.
    decimal
             91  191
    datetime (2012-12-23T13:13:32)
    0000   0xe0 0x0d 0x0d 0x17 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125

#### RECORD 48 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 1.55, 'curve': 20},
 {'age': 13, 'amount': 2.85, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x3e 0x03 0x14 0x72 0x0d 0x14    \.>..r..
    decimal
             92    8   62    3   20  114   13   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2012-12-23T13:13:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'programmed': 1.6}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-12-23T13:13:32)
    0000   0xe0 0x0d 0x4d 0x17 0x0c                   ..M..
    body (0)

#### RECORD 50 TempBasal 2012-12-23T13:15:34 head[2], body[1] op[0x33]

    op hex (2)
    0000   0x33 0x2c                                  3,
    decimal
             51   44
    datetime (2012-12-23T13:15:34)
    0000   0xe2 0x0f 0x0d 0x17 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0

#### RECORD 51 EndTempBasal 2012-12-23T13:15:34 head[2], body[0] op[0x16]

    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2012-12-23T13:15:34)
    0000   0xe2 0x0f 0x0d 0x17 0x0c                   .....
    body (0)

#### RECORD 52 CalForBG 2012-12-23T13:16:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2012-12-23T13:16:03)
    0000   0xc3 0x10 0x2d 0x17 0x0c                   ..-..
    body (0)

#### RECORD 53 BolusWizard 2012-12-23T13:16:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 190,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.7,
 'carb_input': 75,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.6}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2012-12-23T13:16:43)
    0000   0xeb 0x10 0x0d 0x17 0x0c                   .....
    body (13)
    hex
    0000   0x4b 0x50 0x0d 0x2d 0x6a 0x0e 0x39 0x00    KP.-j.9.
    0008   0x00 0x10 0x00 0x39 0x7d                   ...9}
    decimal
             75   80   13   45  106   14   57    0
              0   16    0   57  125

#### RECORD 54 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 0.95, 'curve': 4},
 {'age': 12, 'amount': 0.65, 'curve': 4},
 {'age': 6, 'amount': 1.55, 'curve': 20},
 {'age': 16, 'amount': 2.85, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x26 0x02 0x04 0x1a 0x0c 0x04    \.&.....
    0008   0x3e 0x06 0x14 0x72 0x10 0x14              >..r..
    decimal
             92   14   38    2    4   26   12    4
             62    6   20  114   16   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2012-12-23T13:16:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'programmed': 2.7}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2012-12-23T13:16:43)
    0000   0xeb 0x10 0x8d 0x17 0x0c                   .....
    body (0)

#### RECORD 56 Bolus 2012-12-23T13:18:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x02                        ....
    decimal
              1   31   31    2
    datetime (2012-12-23T13:18:31)
    0000   0xdf 0x12 0xad 0x17 0x0c                   .....
    body (0)

#### RECORD 57 CalForBG 2012-12-23T17:50:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-12-23T17:50:26)
    0000   0xda 0x32 0x31 0x17 0x0c                   .21..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 CalForBG 2012-12-23T20:08:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2012-12-23T20:08:26)
    0000   0xda 0x08 0x34 0x17 0x0c                   ..4..
    body (0)

#### RECORD 59 BolusWizard 2012-12-23T20:08:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 132,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2012-12-23T20:08:53)
    0000   0xf5 0x08 0x14 0x17 0x0c                   .....
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0x01 0x2c 0x00    :P.-j.,.
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             58   80   13   45  106    1   44    0
              0    0    0   45  125

#### RECORD 60 BolusGiven unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 0.25, 'curve': 20},
 {'age': 108, 'amount': 0.5, 'curve': 20},
 {'age': 118, 'amount': 0.5, 'curve': 20},
 {'age': 128, 'amount': 0.55, 'curve': 20},
 {'age': 138, 'amount': 0.5, 'curve': 20},
 {'age': 148, 'amount': 0.5, 'curve': 20},
 {'age': 158, 'amount': 3.95, 'curve': 20},
 {'age': 168, 'amount': 0.65, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x0a 0x62 0x14 0x14 0x6c 0x14    \..b..l.
    0008   0x14 0x76 0x14 0x16 0x80 0x14 0x14 0x8a    .v......
    0010   0x14 0x14 0x94 0x14 0x9e 0x9e 0x14 0x1a    ........
    0018   0xa8 0x14                                  ..
    decimal
             92   26   10   98   20   20  108   20
             20  118   20   22  128   20   20  138
             20   20  148   20  158  158   20   26
            168   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2012-12-23T20:08:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'programmed': 4.5}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2012-12-23T20:08:53)
    0000   0xf5 0x08 0x54 0x17 0x0c                   ..T..
    body (0)

#### RECORD 62 ResultTotals 2012-12-23T13:12:23 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x0e                   .....
    decimal
              7    0    0    6   14
    datetime (2012-12-23T13:12:23)
    0000   0xd7 0x0c 0x6d 0xd7 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x84 0x4e 0xbf 0x06 0x00 0x00    ...N....
    0008   0x06 0x0e 0x03 0x82 0x3a 0x02 0x8c 0x2a    ....:..*
    0010   0x00 0xc1 0x02 0x8c 0x2a 0x02 0x3a 0x57    ....*.:W
    0018   0x00 0x52 0x0d 0x00 0x00 0x00 0x04 0x02    .R......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  132   78  191    6    0    0
              6   14    3  130   58    2  140   42
              0  193    2  140   42    2   58   87
              0   82   13    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 63 CalForBG 2012-12-24T00:24:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 68}
```
    op hex (2)
    0000   0x0a 0x44                                  .D
    decimal
             10   68
    datetime (2012-12-24T00:24:01)
    0000   0xc1 0x18 0x20 0x18 0x0c                   .. ..
    body (0)

#### RECORD 64 CalForBG 2012-12-24T10:07:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2012-12-24T10:07:02)
    0000   0xc2 0x07 0x2a 0x18 0x0c                   ..*..
    body (0)

#### RECORD 65 BolusWizard 2012-12-24T10:07:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 85,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.0,
 'carb_input': 85,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2012-12-24T10:07:29)
    0000   0xdd 0x07 0x0a 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x55 0x50 0x0d 0x2d 0x6a 0xfb 0x41 0xf0    UP.-j.A.
    0008   0x00 0x00 0x00 0x3c 0x7d                   ...<}
    decimal
             85   80   13   45  106  251   65  240
              0    0    0   60  125

#### RECORD 66 Bolus 2012-12-24T10:07:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0, 'programmed': 6.0}
```
    op hex (4)
    0000   0x01 0x3c 0x3c 0x00                        .<<.
    decimal
              1   60   60    0
    datetime (2012-12-24T10:07:29)
    0000   0xdd 0x07 0x4a 0x18 0x0c                   ..J..
    body (0)

#### RECORD 67 CalForBG 2012-12-24T14:24:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2012-12-24T14:24:57)
    0000   0xf9 0x18 0x2e 0x18 0x0c                   .....
    body (0)

#### RECORD 68 CalForBG 2012-12-24T15:53:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2012-12-24T15:53:17)
    0000   0xd1 0x35 0x2f 0x18 0x0c                   .5/..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 BolusWizard 2012-12-24T15:53:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 106,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2012-12-24T15:53:53)
    0000   0xf5 0x35 0x0f 0x18 0x0c                   .5...
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [0, 0, 1]
#### RECORD 70 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 6.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xf0 0x5d 0x14                   \..].
    decimal
             92    5  240   93   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2012-12-24T15:53:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-12-24T15:53:53)
    0000   0xf5 0x35 0x4f 0x18 0x0c                   .5O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 72 PumpSuspend 2012-12-24T19:10:12 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-24T19:10:12)
    0000   0xcc 0x0a 0x13 0x18 0x0c                   .....
    body (0)

#### RECORD 73 PumpResume 2012-12-24T19:27:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-24T19:27:08)
    0000   0xc8 0x1b 0x13 0x18 0x0c                   .....
    body (0)

#### RECORD 74 CalForBG 2012-12-24T19:27:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2012-12-24T19:27:35)
    0000   0xe3 0x1b 0x33 0x18 0x0c                   ..3..
    body (0)

#### RECORD 75 BolusWizard 2012-12-24T19:27:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2012-12-24T19:27:46)
    0000   0xee 0x1b 0x13 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x08 0x1d 0x00    &P.-j...
    0008   0x00 0x02 0x00 0x23 0x7d                   ...#}
    decimal
             38   80   13   45  106    8   29    0
              0    2    0   35  125

#### RECORD 76 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 213, 'amount': 2.1, 'curve': 4},
 {'age': 223, 'amount': 0.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x54 0xd5 0x04 0x08 0xdf 0x04    \.T.....
    decimal
             92    8   84  213    4    8  223    4
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2012-12-24T19:27:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-12-24T19:27:46)
    0000   0xee 0x1b 0x53 0x18 0x0c                   ..S..
    body (0)

#### RECORD 78 BolusWizard 2012-12-24T19:42:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-24T19:42:52)
    0000   0xf4 0x2a 0x13 0x18 0x0c                   .*...
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [0, 0, 1]
#### RECORD 79 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 3.5, 'curve': 4},
 {'age': 228, 'amount': 2.1, 'curve': 4},
 {'age': 238, 'amount': 0.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x8c 0x12 0x04 0x54 0xe4 0x04    \....T..
    0008   0x08 0xee 0x04                             ...
    decimal
             92   11  140   18    4   84  228    4
              8  238    4
    datetime (unknown)

    body (0)

#### RECORD 80 Bolus 2012-12-24T19:42:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-12-24T19:42:52)
    0000   0xf4 0x2a 0x53 0x18 0x0c                   .*S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 81 CalForBG 2012-12-24T22:21:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2012-12-24T22:21:41)
    0000   0xe9 0x15 0x36 0x18 0x0c                   ..6..
    body (0)

#### RECORD 82 ResultTotals (2000, 12, 0, 0, 12, 24) head[5], body[25] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x82                   .....
    decimal
              7    0    0    5  130
    datetime ((2000, 12, 0, 0, 12, 24))
    0000   0xd8 0x0c 0x00 0x00 0x00                   .....
    body (25)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xac    ........
    0018   0xf6                                       .
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0  172
            246

`end logs/ReadHistoryData-page-9.data: 83 records`
