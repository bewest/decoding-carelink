## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 1008, found 14 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x58 0xd9                                  X.
##### DEBUG DECIMAL
             88  217
#### RECORD 0 Model522ResultTotals 2013-02-19T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-02-19T00:00:00)
    0000   0x33 0x8d 0x05 0x10 0xac                   3....
    body (38)
    hex
    0000   0x5f 0x18 0x06 0x00 0x00 0x05 0xb4 0x03    _.......
    0008   0x6c 0x3c 0x02 0x48 0x28 0x00 0x8a 0x02    l<.H(...
    0010   0x48 0x28 0x01 0xa0 0x47 0x00 0xa8 0x1d    H(..G...
    0018   0x00 0x00 0x00 0x06 0x04 0x02 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             95   24    6    0    0    5  180    3
            108   60    2   72   40    0  138    2
             72   40    1  160   71    0  168   29
              0    0    0    6    4    2    0    0
             12    0  232    0    0    0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 1 CalBGForPH 2013-03-20T12:14:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2013-03-20T12:14:31)
    0000   0x1f 0xce 0x2c 0x14 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2013-03-20T12:15:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 244,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf4                                  [.
    decimal
             91  244
    datetime (2013-03-20T12:15:18)
    0000   0x12 0xcf 0x0c 0x14 0x0d                   .....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x1a 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x3e 0x7d                   ...>}
    decimal
             47   80   13   45  106   26   36    0
              0    0    0   62  125
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Bolus 2013-03-20T12:15:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2, 'dual_component': '??', 'programmed': 6.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3e 0x3e 0x00                        .>>.
    decimal
              1   62   62    0
    datetime (2013-03-20T12:15:18)
    0000   0x12 0xcf 0x4c 0x14 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-03-20T16:20:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-03-20T16:20:03)
    0000   0x03 0xd4 0x30 0x14 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BolusWizard 2013-03-20T16:20:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-03-20T16:20:38)
    0000   0x26 0xd4 0x10 0x14 0x0d                   &....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             47   80   13   45  106    0   36    0
              0    0    0   36  125
    HOUR BITS: [1, 1, 0]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 246, 'amount': 6.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xf8 0xf6 0x04                   \....
    decimal
             92    5  248  246    4
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-03-20T16:20:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-03-20T16:20:38)
    0000   0x26 0xd4 0x50 0x14 0x0d                   &.P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 CalBGForPH 2013-03-20T17:15:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-20T17:15:21)
    0000   0x15 0xcf 0x31 0x14 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 CalBGForPH 2013-03-20T21:09:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 211}
```
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2013-03-20T21:09:46)
    0000   0x2e 0xc9 0x35 0x14 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 BolusWizard 2013-03-20T21:11:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 211,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 9,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd3                                  [.
    decimal
             91  211
    datetime (2013-03-20T21:11:47)
    0000   0x2f 0xcb 0x15 0x14 0x0d                   /....
    body (13)
    hex
    0000   0x09 0x50 0x0d 0x2d 0x6a 0x13 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
              9   80   13   45  106   19    6    0
              0    0    0   25  125
    HOUR BITS: [1, 1, 0]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 3.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0x29 0x14                   \..).
    decimal
             92    5  144   41   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-03-20T21:11:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-03-20T21:11:47)
    0000   0x2f 0xcb 0x55 0x14 0x0d                   /.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 CalBGForPH 2013-03-20T22:45:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-03-20T22:45:25)
    0000   0x19 0xed 0x36 0x14 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 BolusWizard 2013-03-20T22:45:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-03-20T22:45:57)
    0000   0x39 0xed 0x16 0x14 0x0d                   9....
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0xfc 0x1a 0xf0    #P.-j...
    0008   0x00 0x06 0x00 0x16 0x7d                   ....}
    decimal
             35   80   13   45  106  252   26  240
              0    6    0   22  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 0.9, 'curve': 4},
 {'age': 135, 'amount': 3.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x65 0x04 0x90 0x87 0x14    \.$e....
    decimal
             92    8   36  101    4  144  135   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-03-20T22:45:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-03-20T22:45:57)
    0000   0x39 0xed 0x56 0x14 0x0d                   9.V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 MResultTotals (2013, 0, 20, 8, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 20, 8, 5, 0))
    0000   0x00 0x05 0x88 0x34 0x8d                   ...4.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 Model522ResultTotals 2013-02-20T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-02-20T00:00:00)
    0000   0x34 0x8d 0x05 0x00 0x94                   4....
    body (38)
    hex
    0000   0x59 0xf4 0x05 0x00 0x00 0x05 0x88 0x03    Y.......
    0008   0x84 0x40 0x02 0x04 0x24 0x00 0x8a 0x02    .@..$...
    0010   0x04 0x24 0x01 0x90 0x4e 0x00 0x74 0x16    .$..N.t.
    0018   0x00 0x00 0x00 0x04 0x02 0x00 0x02 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             89  244    5    0    0    5  136    3
            132   64    2    4   36    0  138    2
              4   36    1  144   78    0  116   22
              0    0    0    4    2    0    2    0
             12    0  232    0    0    0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 19 PumpSuspend 2013-03-21T13:48:51 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-21T13:48:51)
    0000   0x33 0xf0 0x0d 0x15 0x0d                   3....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 PumpResume 2013-03-21T14:16:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-21T14:16:06)
    0000   0x06 0xd0 0x0e 0x15 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 21 CalBGForPH 2013-03-21T15:13:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-03-21T15:13:02)
    0000   0x02 0xcd 0x2f 0x15 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 BolusWizard 2013-03-21T15:13:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-03-21T15:13:49)
    0000   0x31 0xcd 0x0f 0x15 0x0d                   1....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x00 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             45   80   13   45  106    0   34    0
              0    0    0   34  125
    HOUR BITS: [1, 1, 0]
#### RECORD 23 Bolus 2013-03-21T15:13:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-03-21T15:13:49)
    0000   0x31 0xcd 0x4f 0x15 0x0d                   1.O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 CalBGForPH 2013-03-21T17:18:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-03-21T17:18:56)
    0000   0x38 0xd2 0x31 0x15 0x0d                   8.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BolusWizard 2013-03-21T17:19:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-03-21T17:19:12)
    0000   0x0c 0xd3 0x11 0x15 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x0f 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0   15    0    0  125
    HOUR BITS: [1, 1, 0]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 3.1, 'curve': 4},
 {'age': 135, 'amount': 0.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x7c 0x7d 0x04 0x0c 0x87 0x04    \.|}....
    decimal
             92    8  124  125    4   12  135    4
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-03-21T17:19:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x01 0x01 0x00                        ....
    decimal
              1    1    1    0
    datetime (2013-03-21T17:19:12)
    0000   0x0c 0xd3 0x51 0x15 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 CalBGForPH 2013-03-21T18:58:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2013-03-21T18:58:19)
    0000   0x13 0xfa 0x32 0x15 0x8d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 BolusWizard 2013-03-21T18:58:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 256,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-03-21T18:58:27)
    0000   0x1b 0xfa 0x12 0x15 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x03 0x00 0x1a 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    3    0   26  125
    HOUR BITS: [1, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 0.1, 'curve': 4},
 {'age': 224, 'amount': 3.1, 'curve': 4},
 {'age': 234, 'amount': 0.3, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x04 0x68 0x04 0x7c 0xe0 0x04    \..h.|..
    0008   0x0c 0xea 0x04                             ...
    decimal
             92   11    4  104    4  124  224    4
             12  234    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-03-21T18:58:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-03-21T18:58:27)
    0000   0x1b 0xfa 0x52 0x15 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 CalBGForPH 2013-03-21T22:00:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-03-21T22:00:26)
    0000   0x1a 0xc0 0x36 0x15 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 BolusWizard 2013-03-21T22:00:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2013-03-21T22:00:40)
    0000   0x28 0xc0 0x16 0x15 0x0d                   (....
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    =P.-j...
    0008   0x00 0x05 0x00 0x2e 0x7d                   ....}
    decimal
             61   80   13   45  106    0   46    0
              0    5    0   46  125
    HOUR BITS: [1, 1, 0]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 186, 'amount': 2.7, 'curve': 4},
 {'age': 30, 'amount': 0.1, 'curve': 20},
 {'age': 150, 'amount': 3.1, 'curve': 20},
 {'age': 160, 'amount': 0.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0xba 0x04 0x04 0x1e 0x14    \.l.....
    0008   0x7c 0x96 0x14 0x0c 0xa0 0x14              |.....
    decimal
             92   14  108  186    4    4   30   20
            124  150   20   12  160   20
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-03-21T22:00:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-03-21T22:00:40)
    0000   0x28 0xc0 0x56 0x15 0x0d                   (.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 MResultTotals (2013, 0, 21, 0, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 21, 0, 5, 0))
    0000   0x00 0x05 0x20 0x35 0x8d                   .. 5.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 Model522ResultTotals 2013-02-21T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-02-21T00:00:00)
    0000   0x35 0x8d 0x05 0x10 0xab                   5....
    body (38)
    hex
    0000   0x70 0x00 0x04 0x00 0x00 0x05 0x20 0x03    p..... .
    0008   0x70 0x43 0x01 0xb0 0x21 0x00 0x6a 0x01    pC..!.j.
    0010   0xb0 0x21 0x01 0x40 0x4a 0x00 0x70 0x1a    .!.@J.p.
    0018   0x00 0x00 0x00 0x04 0x02 0x02 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            112    0    4    0    0    5   32    3
            112   67    1  176   33    0  106    1
            176   33    1   64   74    0  112   26
              0    0    0    4    2    2    0    0
             12    0  232    0    0    0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 38 CalBGForPH 2013-03-22T00:08:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-03-22T00:08:04)
    0000   0x04 0xc8 0x20 0x16 0x0d                   .. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 39 CalBGForPH 2013-03-22T08:07:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 315}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2013-03-22T08:07:12)
    0000   0x0c 0xc7 0x28 0x16 0x8d                   ..(..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 40 BolusWizard 2013-03-22T08:07:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 42,
 '_byte[7]': 0,
 'bg': 315,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3b                                  [;
    decimal
             91   59
    datetime (2013-03-22T08:07:14)
    0000   0x0e 0xc7 0x08 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2a 0x00 0x00    .Q.-j*..
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
              0   81   13   45  106   42    0    0
              0    0    0   42  125
    HOUR BITS: [1, 1, 0]
#### RECORD 41 Bolus 2013-03-22T08:07:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-03-22T08:07:14)
    0000   0x0e 0xc7 0x48 0x16 0x0d                   ..H..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 42 PumpSuspend 2013-03-22T12:41:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-22T12:41:09)
    0000   0x09 0xe9 0x0c 0x16 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 43 PumpResume 2013-03-22T12:59:47 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-22T12:59:47)
    0000   0x2f 0xfb 0x0c 0x16 0x0d                   /....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 CalBGForPH 2013-03-22T14:09:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2013-03-22T14:09:03)
    0000   0x03 0xc9 0x2e 0x16 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 BolusWizard 2013-03-22T14:09:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 93,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 2.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5d                                  []
    decimal
             91   93
    datetime (2013-03-22T14:09:24)
    0000   0x18 0xc9 0x0e 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0xfd 0x16 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             29   80   13   45  106  253   22  240
              0    0    0   19  125
    HOUR BITS: [1, 1, 0]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 4.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0x6d 0x14                   \..m.
    decimal
             92    5  168  109   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-03-22T14:09:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-03-22T14:09:24)
    0000   0x18 0xc9 0x4e 0x16 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 CalBGForPH 2013-03-22T17:22:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2013-03-22T17:22:09)
    0000   0x09 0xd6 0x31 0x16 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 BolusWizard 2013-03-22T17:22:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 175,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xaf                                  [.
    decimal
             91  175
    datetime (2013-03-22T17:22:20)
    0000   0x14 0xd6 0x11 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    3    0    8  125
    HOUR BITS: [1, 1, 0]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 198, 'amount': 1.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x4c 0xc6 0x04                   \.L..
    decimal
             92    5   76  198    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-03-22T17:22:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-03-22T17:22:21)
    0000   0x15 0xd6 0x51 0x16 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 52 CalBGForPH 2013-03-22T21:53:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 74}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2013-03-22T21:53:06)
    0000   0x06 0xf5 0x35 0x16 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 53 BolusWizard 2013-03-22T21:54:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 74,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 54,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 4.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4a                                  [J
    decimal
             91   74
    datetime (2013-03-22T21:54:16)
    0000   0x10 0xf6 0x15 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x36 0x50 0x0d 0x2d 0x6a 0xf9 0x29 0xf0    6P.-j.).
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             54   80   13   45  106  249   41  240
              0    0    0   34  125
    HOUR BITS: [1, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 1.0, 'curve': 20},
 {'age': 214, 'amount': 1.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x18 0x14 0x4c 0xd6 0x14    \.(..L..
    decimal
             92    8   40   24   20   76  214   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2013-03-22T21:54:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-03-22T21:54:16)
    0000   0x10 0xf6 0x55 0x16 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 56 MResultTotals (2013, 0, 22, 28, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 22, 28, 5, 0))
    0000   0x00 0x05 0x1c 0x36 0x8d                   ...6.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 57 Model522ResultTotals 2013-02-22T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-02-22T00:00:00)
    0000   0x36 0x8d 0x05 0x10 0x92                   6....
    body (38)
    hex
    0000   0x4a 0x3b 0x05 0x00 0x00 0x05 0x1c 0x03    J;......
    0008   0x78 0x44 0x01 0xa4 0x20 0x00 0x53 0x01    xD.. .S.
    0010   0xa4 0x20 0x00 0xd4 0x32 0x00 0xd0 0x32    . ..2..2
    0018   0x00 0x00 0x00 0x04 0x02 0x02 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             74   59    5    0    0    5   28    3
            120   68    1  164   32    0   83    1
            164   32    0  212   50    0  208   50
              0    0    0    4    2    2    0    0
             12    0  232    0    0    0
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 1]
#### RECORD 58 LowReservoir 2013-03-23T03:18:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-23T03:18:45)
    0000   0x2d 0xd2 0x03 0x17 0x0d                   -....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 CalBGForPH 2013-03-23T09:07:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-03-23T09:07:53)
    0000   0x35 0xc7 0x29 0x17 0x0d                   5.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 60 BolusWizard 2013-03-23T09:08:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 1.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-03-23T09:08:09)
    0000   0x09 0xc8 0x09 0x17 0x0d                   .....
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x01 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             24   80   13   45  106    1   18    0
              0    0    0   19  125
    HOUR BITS: [1, 1, 0]
#### RECORD 61 Bolus 2013-03-23T09:08:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-03-23T09:08:09)
    0000   0x09 0xc8 0x49 0x17 0x0d                   ..I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 PumpSuspend 2013-03-23T11:06:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-23T11:06:00)
    0000   0x00 0xc6 0x0b 0x17 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 PumpResume 2013-03-23T11:30:01 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-23T11:30:01)
    0000   0x01 0xde 0x0b 0x17 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 Rewind 2013-03-23T11:30:12 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-03-23T11:30:12)
    0000   0x0c 0xde 0x0b 0x17 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 Prime 2013-03-23T11:31:41 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x25                   ....%
    decimal
              3    0    0    0   37
    datetime (2013-03-23T11:31:41)
    0000   0x29 0xdf 0x2b 0x17 0x0d                   ).+..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 66 Prime 2013-03-23T11:31:59 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-03-23T11:31:59)
    0000   0x3b 0xdf 0x0b 0x17 0x0d                   ;....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 CalBGForPH 2013-03-23T13:33:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-03-23T13:33:02)
    0000   0x02 0xe1 0x2d 0x17 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 CalBGForPH 2013-03-23T13:33:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-03-23T13:33:23)
    0000   0x17 0xe1 0x2d 0x17 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 CalBGForPH 2013-03-23T14:14:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-03-23T14:14:24)
    0000   0x18 0xce 0x2e 0x17 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 70 CalBGForPH 2013-03-23T14:18:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-03-23T14:18:03)
    0000   0x03 0xd2 0x2e 0x17 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 71 CalBGForPH 2013-03-23T16:46:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 372}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-03-23T16:46:39)
    0000   0x27 0xee 0x30 0x17 0x8d                   '.0..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 72 BolusWizard 2013-03-23T16:46:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 372,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-03-23T16:46:46)
    0000   0x2e 0xee 0x10 0x17 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x36 0x00 0x00    .Q.-j6..
    0008   0x00 0x00 0x00 0x36 0x7d                   ...6}
    decimal
              0   81   13   45  106   54    0    0
              0    0    0   54  125
    HOUR BITS: [1, 1, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 206, 'amount': 1.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x4c 0xce 0x14                   \.L..
    decimal
             92    5   76  206   20
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2013-03-23T16:46:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4, 'dual_component': '??', 'programmed': 5.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x36 0x36 0x00                        .66.
    decimal
              1   54   54    0
    datetime (2013-03-23T16:46:46)
    0000   0x2e 0xee 0x50 0x17 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 75 CalBGForPH 2013-03-23T17:12:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 399}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-03-23T17:12:49)
    0000   0x31 0xcc 0x31 0x17 0x8d                   1.1..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 76 BolusWizard 2013-03-23T17:12:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 60,
 '_byte[7]': 0,
 'bg': 399,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 5.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2013-03-23T17:12:59)
    0000   0x3b 0xcc 0x11 0x17 0x0d                   ;....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3c 0x00 0x00    .Q.-j<..
    0008   0x00 0x34 0x00 0x08 0x7d                   .4..}
    decimal
              0   81   13   45  106   60    0    0
              0   52    0    8  125
    HOUR BITS: [1, 1, 0]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 5.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xd8 0x1c 0x04                   \....
    decimal
             92    5  216   28    4
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2013-03-23T17:12:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-03-23T17:12:59)
    0000   0x3b 0xcc 0x51 0x17 0x0d                   ;.Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 CalBGForPH 2013-03-23T17:28:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 399}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-03-23T17:28:13)
    0000   0x0d 0xdc 0x31 0x17 0x8d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 80 BolusWizard 2013-03-23T17:28:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 60,
 '_byte[7]': 0,
 'bg': 399,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 5.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2013-03-23T17:28:26)
    0000   0x1a 0xdc 0x11 0x17 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3c 0x00 0x00    .Q.-j<..
    0008   0x00 0x3b 0x00 0x01 0x7d                   .;..}
    decimal
              0   81   13   45  106   60    0    0
              0   59    0    1  125
    HOUR BITS: [1, 1, 0]
#### RECORD 81 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 1.1, 'curve': 4},
 {'age': 44, 'amount': 5.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x18 0x04 0xd8 0x2c 0x04    \.,...,.
    decimal
             92    8   44   24    4  216   44    4
    datetime (unknown)

    body (0)

#### RECORD 82 Bolus 2013-03-23T17:28:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-03-23T17:28:26)
    0000   0x1a 0xdc 0x51 0x17 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 83 CalBGForPH 2013-03-23T17:53:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 331}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-03-23T17:53:03)
    0000   0x03 0xf5 0x31 0x17 0x8d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 84 CalBGForPH 2013-03-23T18:25:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 290}
```
    op hex (2)
    0000   0x0a 0x22                                  ."
    decimal
             10   34
    datetime (2013-03-23T18:25:02)
    0000   0x02 0xd9 0x32 0x17 0x8d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 85 CalBGForPH 2013-03-23T19:27:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-03-23T19:27:07)
    0000   0x07 0xdb 0x33 0x17 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 86 MResultTotals (2013, 0, 23, 14, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 23, 14, 4, 0))
    0000   0x00 0x04 0xce 0x37 0x8d                   ...7.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-34.data: 87 records`
