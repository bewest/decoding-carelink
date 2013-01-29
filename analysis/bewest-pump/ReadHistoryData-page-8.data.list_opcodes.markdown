## START logs/ReadHistoryData-page-8.data
#### RECORD 0 hack1 2012-12-25T01:33:45 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0xd8 0x0c 0x05 0x00 0x5e 0x3d 0xa3    m....^=.
    0008   0x06 0x00 0x00 0x05 0x82 0x03 0x7a 0x3f    ......z?
    0010   0x02 0x08 0x25 0x00 0xaa 0x02 0x08 0x25    ..%....%
    0018   0x01 0xf0 0x5f 0x00 0x18 0x05 0x00 0x00    .._.....
    0020   0x00 0x04 0x03 0x00 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x34 0xc8              ....4.
    decimal
            109  216   12    5    0   94   61  163
              6    0    0    5  130    3  122   63
              2    8   37    0  170    2    8   37
              1  240   95    0   24    5    0    0
              0    4    3    0    1    0   12    0
            232    0    0    0   52  200
    datetime (2012-12-25T01:33:45)
    0000   0xed 0x21 0x01 0x19 0x0c                   .!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 Rewind 2012-12-25T09:30:48 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-25T09:30:48)
    0000   0xf0 0x1e 0x09 0x19 0x0c                   .....
    body (0)

#### RECORD 2 Prime 2012-12-25T09:31:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x24                   ....$
    decimal
              3    0    0    0   36
    datetime (2012-12-25T09:31:18)
    0000   0xd2 0x1f 0x29 0x19 0x0c                   ..)..
    body (0)

#### RECORD 3 Prime 2012-12-25T09:31:44 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-25T09:31:44)
    0000   0xec 0x1f 0x09 0x19 0x0c                   .....
    body (0)

#### RECORD 4 CalBGForPH 2012-12-25T09:41:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-12-25T09:41:06)
    0000   0xc6 0x29 0x29 0x19 0x0c                   .))..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BolusWizard 2012-12-25T09:41:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 70,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 91,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2012-12-25T09:41:23)
    0000   0xd7 0x29 0x09 0x19 0x0c                   .)...
    body (13)
    hex
    0000   0x5b 0x50 0x0d 0x2d 0x6a 0xf8 0x46 0xf0    [P.-j.F.
    0008   0x00 0x00 0x00 0x3e 0x7d                   ...>}
    decimal
             91   80   13   45  106  248   70  240
              0    0    0   62  125
    HOUR BITS: [0, 0, 1]
#### RECORD 6 Bolus 2012-12-25T09:41:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2, 'programmed': 6.2}
```
    op hex (4)
    0000   0x01 0x3e 0x3e 0x00                        .>>.
    decimal
              1   62   62    0
    datetime (2012-12-25T09:41:23)
    0000   0xd7 0x29 0x49 0x19 0x0c                   .)I..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 CalBGForPH 2012-12-25T14:23:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2012-12-25T14:23:13)
    0000   0xcd 0x17 0x2e 0x19 0x0c                   .....
    body (0)

#### RECORD 8 CalBGForPH 2012-12-25T14:51:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2012-12-25T14:51:27)
    0000   0xdb 0x33 0x2e 0x19 0x0c                   .3...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 9 CalBGForPH 2012-12-25T15:05:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-12-25T15:05:57)
    0000   0xf9 0x05 0x2f 0x19 0x0c                   ../..
    body (0)

#### RECORD 10 BolusWizard 2012-12-25T15:06:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 70,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2012-12-25T15:06:57)
    0000   0xf9 0x06 0x0f 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0xf8 0x2b 0xf0    9P.-j.+.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             57   80   13   45  106  248   43  240
              0    0    0   35  125

#### RECORD 11 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 2.3, 'curve': 20},
 {'age': 76, 'amount': 3.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x5c 0x42 0x14 0x9c 0x4c 0x14    \.\B..L.
    decimal
             92    8   92   66   20  156   76   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2012-12-25T15:06:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-12-25T15:06:57)
    0000   0xf9 0x06 0x4f 0x19 0x0c                   ..O..
    body (0)

#### RECORD 13 PumpSuspend 2012-12-25T15:27:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-25T15:27:53)
    0000   0xf5 0x1b 0x0f 0x19 0x0c                   .....
    body (0)

#### RECORD 14 PumpResume 2012-12-25T15:42:23 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-25T15:42:23)
    0000   0xd7 0x2a 0x0f 0x19 0x0c                   .*...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 CalBGForPH 2012-12-25T17:35:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 294}
```
    op hex (2)
    0000   0x0a 0x26                                  .&
    decimal
             10   38
    datetime (2012-12-25T17:35:10)
    0000   0xca 0x23 0x31 0x19 0x8c                   .#1..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 BolusWizard 2012-12-25T17:35:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 294,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.1}
```
    op hex (2)
    0000   0x5b 0x26                                  [&
    decimal
             91   38
    datetime (2012-12-25T17:35:12)
    0000   0xcc 0x23 0x11 0x19 0x0c                   .#...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x25 0x00 0x00    .Q.-j%..
    0008   0x00 0x0b 0x00 0x1a 0x7d                   ....}
    decimal
              0   81   13   45  106   37    0    0
              0   11    0   26  125
    HOUR BITS: [0, 0, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 151, 'amount': 3.5, 'curve': 4},
 {'age': 215, 'amount': 2.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x8c 0x97 0x04 0x5c 0xd7 0x14    \....\..
    decimal
             92    8  140  151    4   92  215   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2012-12-25T17:35:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-12-25T17:35:12)
    0000   0xcc 0x23 0x51 0x19 0x0c                   .#Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 19 CalBGForPH 2012-12-25T18:58:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 306}
```
    op hex (2)
    0000   0x0a 0x32                                  .2
    decimal
             10   50
    datetime (2012-12-25T18:58:49)
    0000   0xf1 0x3a 0x32 0x19 0x8c                   .:2..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 TempBasal 2012-12-25T19:00:30 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.05}
```
    op hex (2)
    0000   0x33 0x2a                                  3*
    decimal
             51   42
    datetime (2012-12-25T19:00:30)
    0000   0xde 0x00 0x13 0x19 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0

#### RECORD 21 TempBasalDuration 2012-12-25T19:00:30 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2012-12-25T19:00:30)
    0000   0xde 0x00 0x13 0x19 0x0c                   .....
    body (0)

#### RECORD 22 CalBGForPH 2012-12-25T19:01:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 302}
```
    op hex (2)
    0000   0x0a 0x2e                                  ..
    decimal
             10   46
    datetime (2012-12-25T19:01:07)
    0000   0xc7 0x01 0x33 0x19 0x8c                   ..3..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 23 BolusWizard 2012-12-25T19:01:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 302,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.0}
```
    op hex (2)
    0000   0x5b 0x2e                                  [.
    decimal
             91   46
    datetime (2012-12-25T19:01:22)
    0000   0xd6 0x01 0x13 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x27 0x00 0x00    .Q.-j'..
    0008   0x00 0x14 0x00 0x13 0x7d                   ....}
    decimal
              0   81   13   45  106   39    0    0
              0   20    0   19  125

#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 87, 'amount': 2.6, 'curve': 4},
 {'age': 237, 'amount': 3.5, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x68 0x57 0x04 0x8c 0xed 0x04    \.hW....
    decimal
             92    8  104   87    4  140  237    4
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2012-12-25T19:01:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-12-25T19:01:22)
    0000   0xd6 0x01 0x53 0x19 0x0c                   ..S..
    body (0)

#### RECORD 26 BolusWizard 2012-12-25T19:27:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-25T19:27:32)
    0000   0xe0 0x1b 0x13 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0    0    0   21  125

#### RECORD 27 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 2.0, 'curve': 4},
 {'age': 113, 'amount': 2.6, 'curve': 4},
 {'age': 7, 'amount': 3.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x21 0x04 0x68 0x71 0x04    \.P!.hq.
    0008   0x8c 0x07 0x14                             ...
    decimal
             92   11   80   33    4  104  113    4
            140    7   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2012-12-25T19:27:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'programmed': 2.1}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2012-12-25T19:27:32)
    0000   0xe0 0x1b 0x53 0x19 0x0c                   ..S..
    body (0)

#### RECORD 29 CalBGForPH 2012-12-25T20:50:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 178}
```
    op hex (2)
    0000   0x0a 0xb2                                  ..
    decimal
             10  178
    datetime (2012-12-25T20:50:09)
    0000   0xc9 0x32 0x34 0x19 0x0c                   .24..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 CalBGForPH 2012-12-25T20:55:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2012-12-25T20:55:48)
    0000   0xf0 0x37 0x34 0x19 0x0c                   .74..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 BolusWizard 2012-12-25T20:56:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 166,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.6}
```
    op hex (2)
    0000   0x5b 0xa6                                  [.
    decimal
             91  166
    datetime (2012-12-25T20:56:05)
    0000   0xc5 0x38 0x14 0x19 0x0c                   .8...
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x09 0x14 0x00    .P.-j...
    0008   0x00 0x1a 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    9   20    0
              0   26    0   20  125
    HOUR BITS: [0, 0, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 2.1, 'curve': 4},
 {'age': 122, 'amount': 2.0, 'curve': 4},
 {'age': 202, 'amount': 2.6, 'curve': 4},
 {'age': 96, 'amount': 3.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x54 0x5c 0x04 0x50 0x7a 0x04    \.T\.Pz.
    0008   0x68 0xca 0x04 0x8c 0x60 0x14              h...`.
    decimal
             92   14   84   92    4   80  122    4
            104  202    4  140   96   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2012-12-25T20:56:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-12-25T20:56:05)
    0000   0xc5 0x38 0x54 0x19 0x0c                   .8T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 34 CalBGForPH 2012-12-25T22:08:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2012-12-25T22:08:46)
    0000   0xee 0x08 0x36 0x19 0x0c                   ..6..
    body (0)

#### RECORD 35 BolusWizard 2012-12-25T22:20:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 5,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-25T22:20:36)
    0000   0xe4 0x14 0x16 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x05 0x50 0x0d 0x2d 0x6a 0x00 0x03 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x03 0x7d                   ....}
    decimal
              5   80   13   45  106    0    3    0
              0    0    0    3  125

#### RECORD 36 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 2.0, 'curve': 4},
 {'age': 176, 'amount': 2.1, 'curve': 4},
 {'age': 206, 'amount': 2.0, 'curve': 4},
 {'age': 30, 'amount': 2.6, 'curve': 20},
 {'age': 180, 'amount': 3.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x56 0x04 0x54 0xb0 0x04    \.PV.T..
    0008   0x50 0xce 0x04 0x68 0x1e 0x14 0x8c 0xb4    P..h....
    0010   0x14                                       .
    decimal
             92   17   80   86    4   84  176    4
             80  206    4  104   30   20  140  180
             20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2012-12-25T22:20:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-25T22:20:36)
    0000   0xe4 0x14 0x56 0x19 0x0c                   ..V..
    body (0)

#### RECORD 38 ResultTotals 2012-12-25T13:12:25 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x6c                   ....l
    decimal
              7    0    0    6  108
    datetime (2012-12-25T13:12:25)
    0000   0xd9 0x0c 0x6d 0xd9 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xa5 0x46 0x32 0x0a 0x00 0x00    ...F2...
    0008   0x06 0x6c 0x03 0x80 0x37 0x02 0xec 0x2d    .l..7..-
    0010   0x00 0xd0 0x02 0xec 0x2d 0x02 0x34 0x4b    ....-.4K
    0018   0x00 0xb8 0x19 0x00 0x00 0x00 0x07 0x05    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  165   70   50   10    0    0
              6  108    3  128   55    2  236   45
              0  208    2  236   45    2   52   75
              0  184   25    0    0    0    7    5
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 39 CalBGForPH 2012-12-26T00:55:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 224}
```
    op hex (2)
    0000   0x0a 0xe0                                  ..
    decimal
             10  224
    datetime (2012-12-26T00:55:44)
    0000   0xec 0x37 0x20 0x1a 0x0c                   .7 ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 BolusWizard 2012-12-26T00:55:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 224,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0xe0                                  [.
    decimal
             91  224
    datetime (2012-12-26T00:55:53)
    0000   0xf5 0x37 0x00 0x1a 0x0c                   .7...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x15 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    1    0   21  125
    HOUR BITS: [0, 0, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 161, 'amount': 0.3, 'curve': 4},
 {'age': 241, 'amount': 2.0, 'curve': 4},
 {'age': 75, 'amount': 2.1, 'curve': 20},
 {'age': 105, 'amount': 2.0, 'curve': 20},
 {'age': 185, 'amount': 2.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x0c 0xa1 0x04 0x50 0xf1 0x04    \....P..
    0008   0x54 0x4b 0x14 0x50 0x69 0x14 0x68 0xb9    TK.Pi.h.
    0010   0x14                                       .
    decimal
             92   17   12  161    4   80  241    4
             84   75   20   80  105   20  104  185
             20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2012-12-26T00:55:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-12-26T00:55:53)
    0000   0xf5 0x37 0x40 0x1a 0x0c                   .7@..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 CalBGForPH 2012-12-26T09:28:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2012-12-26T09:28:26)
    0000   0xda 0x1c 0x29 0x1a 0x0c                   ..)..
    body (0)

#### RECORD 44 BolusWizard 2012-12-26T09:28:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 131,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 7.4,
 'carb_input': 96,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2012-12-26T09:28:52)
    0000   0xf4 0x1c 0x09 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x60 0x50 0x0d 0x2d 0x6a 0x01 0x49 0x00    `P.-j.I.
    0008   0x00 0x00 0x00 0x4a 0x7d                   ...J}
    decimal
             96   80   13   45  106    1   73    0
              0    0    0   74  125

#### RECORD 45 Bolus 2012-12-26T09:28:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.4, 'programmed': 7.4}
```
    op hex (4)
    0000   0x01 0x4a 0x4a 0x00                        .JJ.
    decimal
              1   74   74    0
    datetime (2012-12-26T09:28:52)
    0000   0xf4 0x1c 0x49 0x1a 0x0c                   ..I..
    body (0)

#### RECORD 46 PumpSuspend 2012-12-26T12:10:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-26T12:10:18)
    0000   0xd2 0x0a 0x0c 0x1a 0x0c                   .....
    body (0)

#### RECORD 47 PumpResume 2012-12-26T12:46:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-26T12:46:37)
    0000   0xe5 0x2e 0x0c 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 CalBGForPH 2012-12-26T12:46:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2012-12-26T12:46:42)
    0000   0xea 0x2e 0x2c 0x1a 0x0c                   ..,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 CalBGForPH 2012-12-26T15:15:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2012-12-26T15:15:33)
    0000   0xe1 0x0f 0x2f 0x1a 0x0c                   ../..
    body (0)

#### RECORD 50 BolusWizard 2012-12-26T15:15:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2012-12-26T15:15:47)
    0000   0xef 0x0f 0x0f 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0xfc 0x23 0xf0    .P.-j.#.
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             46   80   13   45  106  252   35  240
              0    0    0   31  125

#### RECORD 51 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 95, 'amount': 1.0, 'curve': 21}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x5f 0x15                   \.(_.
    decimal
             92    5   40   95   21
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2012-12-26T15:15:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-12-26T15:15:47)
    0000   0xef 0x0f 0x4f 0x1a 0x0c                   ..O..
    body (0)

#### RECORD 53 CalBGForPH 2012-12-26T19:39:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-12-26T19:39:05)
    0000   0xc5 0x27 0x33 0x1a 0x0c                   .'3..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 54 BolusWizard 2012-12-26T19:39:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 100,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2012-12-26T19:39:17)
    0000   0xd1 0x27 0x13 0x1a 0x0c                   .'...
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0xfe 0x32 0xf0    AP.-j.2.
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
             65   80   13   45  106  254   50  240
              0    0    0   48  125
    HOUR BITS: [0, 0, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 3.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x09 0x14                   \.|..
    decimal
             92    5  124    9   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2012-12-26T19:39:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'programmed': 4.8}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2012-12-26T19:39:17)
    0000   0xd1 0x27 0x53 0x1a 0x0c                   .'S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 CalBGForPH 2012-12-26T20:57:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2012-12-26T20:57:27)
    0000   0xdb 0x39 0x34 0x1a 0x0c                   .94..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 58 ResultTotals 2012-12-26T13:12:26 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x18                   .....
    decimal
              7    0    0    6   24
    datetime (2012-12-26T13:12:26)
    0000   0xda 0x0c 0x6d 0xda 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x7e 0x59 0xe0 0x06 0x00 0x00    ..~Y....
    0008   0x06 0x18 0x03 0x68 0x38 0x02 0xb0 0x2c    ...h8..,
    0010   0x00 0xcf 0x02 0xb0 0x2c 0x02 0x60 0x58    ....,.`X
    0018   0x00 0x50 0x0c 0x00 0x00 0x00 0x04 0x02    .P......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  126   89  224    6    0    0
              6   24    3  104   56    2  176   44
              0  207    2  176   44    2   96   88
              0   80   12    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 59 CalBGForPH 2012-12-27T00:30:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2012-12-27T00:30:38)
    0000   0xe6 0x1e 0x20 0x1b 0x0c                   .. ..
    body (0)

#### RECORD 60 BolusWizard 2012-12-27T00:30:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 188,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2012-12-27T00:30:41)
    0000   0xe9 0x1e 0x00 0x1b 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125

#### RECORD 61 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 4.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xc0 0x28 0x14                   \..(.
    decimal
             92    5  192   40   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2012-12-27T00:30:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'programmed': 1.4}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2012-12-27T00:30:41)
    0000   0xe9 0x1e 0x40 0x1b 0x0c                   ..@..
    body (0)

#### RECORD 63 CalBGForPH 2012-12-27T02:25:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-12-27T02:25:36)
    0000   0xe4 0x19 0x22 0x1b 0x0c                   .."..
    body (0)

#### RECORD 64 PumpSuspend 2012-12-27T11:21:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-27T11:21:30)
    0000   0xde 0x15 0x0b 0x1b 0x0c                   .....
    body (0)

#### RECORD 65 PumpResume 2012-12-27T11:31:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-27T11:31:07)
    0000   0xc7 0x1f 0x0b 0x1b 0x0c                   .....
    body (0)

#### RECORD 66 CalBGForPH 2012-12-27T12:41:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2012-12-27T12:41:11)
    0000   0xcb 0x29 0x2c 0x1b 0x0c                   .),..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 67 BolusWizard 2012-12-27T12:41:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2012-12-27T12:41:52)
    0000   0xf4 0x29 0x0c 0x1b 0x0c                   .)...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x01 0x2e 0x00    <P.-j...
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             60   80   13   45  106    1   46    0
              0    0    0   47  125
    HOUR BITS: [0, 0, 1]
#### RECORD 68 Bolus 2012-12-27T12:41:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'programmed': 4.7}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2012-12-27T12:41:52)
    0000   0xf4 0x29 0x4c 0x1b 0x0c                   .)L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 CalBGForPH 2012-12-27T19:37:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2012-12-27T19:37:59)
    0000   0xfb 0x25 0x33 0x1b 0x0c                   .%3..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 BolusWizard 2012-12-27T19:38:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 72,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate?': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x48                                  [H
    decimal
             91   72
    datetime (2012-12-27T19:38:54)
    0000   0xf6 0x26 0x13 0x1b 0x0c                   .&...
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0xf8 0x22 0xf0    -P.-j.".
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             45   80   13   45  106  248   34  240
              0    0    0   26  125
    HOUR BITS: [0, 0, 1]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 158, 'amount': 1.55, 'curve': 20},
 {'age': 168, 'amount': 3.15, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x3e 0x9e 0x14 0x7e 0xa8 0x14    \.>..~..
    decimal
             92    8   62  158   20  126  168   20
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2012-12-27T19:38:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-12-27T19:38:54)
    0000   0xf6 0x26 0x53 0x1b 0x0c                   .&S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 73 CalBGForPH 2012-12-27T20:06:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2012-12-27T20:06:29)
    0000   0xdd 0x06 0x34 0x1b 0x0c                   ..4..
    body (0)

#### RECORD 74 BolusWizard 2012-12-27T20:06:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 107,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate?': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.5}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2012-12-27T20:06:35)
    0000   0xe3 0x06 0x14 0x1b 0x0c                   .....
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x19 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0   25    0   13  125

#### RECORD 75 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 2.6, 'curve': 4},
 {'age': 186, 'amount': 1.55, 'curve': 20},
 {'age': 196, 'amount': 3.15, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0x20 0x04 0x3e 0xba 0x14    \.h .>..
    0008   0x7e 0xc4 0x14                             ~..
    decimal
             92   11  104   32    4   62  186   20
            126  196   20
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2012-12-27T20:06:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-12-27T20:06:35)
    0000   0xe3 0x06 0x54 0x1b 0x0c                   ..T..
    body (0)

#### RECORD 77 CalBGForPH 2012-12-27T22:23:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2012-12-27T22:23:38)
    0000   0xe6 0x17 0x36 0x1b 0x0c                   ..6..
    body (0)

#### RECORD 78 ResultTotals 2012-12-27T13:12:27 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime (2012-12-27T13:12:27)
    0000   0xdb 0x0c 0x6d 0xdb 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x78 0x48 0xbc 0x06 0x00 0x00    ..xH....
    0008   0x05 0x0c 0x03 0x7c 0x45 0x01 0x90 0x1f    ...|E...
    0010   0x00 0x7a 0x01 0x90 0x1f 0x01 0x54 0x55    .z....TU
    0018   0x00 0x3c 0x0f 0x00 0x00 0x00 0x04 0x02    .<......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  120   72  188    6    0    0
              5   12    3  124   69    1  144   31
              0  122    1  144   31    1   84   85
              0   60   15    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 79 LowBattery 2012-12-28T01:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2012-12-28T01:01:00)
    0000   0xc0 0x01 0x01 0x1c 0x0c                   .....
    body (0)

#### RECORD 80 Battery 2012-12-28T07:36:44 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2012-12-28T07:36:44)
    0000   0xec 0x24 0x07 0x1c 0x0c                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 81 Battery 2012-12-28T07:37:06 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2012-12-28T07:37:06)
    0000   0xc6 0x25 0x07 0x1c 0x0c                   .%...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 82 CalBGForPH 2012-12-28T07:47:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2012-12-28T07:47:54)
    0000   0xf6 0x2f 0x27 0x1c 0x0c                   ./'..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 83 Base unknown head[2], body[0] op[0x9d]

    op hex (2)
    0000   0x9d 0x8a                                  ..
    decimal
            157  138
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-8.data: 84 records`
