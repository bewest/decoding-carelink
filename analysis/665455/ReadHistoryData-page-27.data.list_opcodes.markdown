## START logs/ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 1011, found 11 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xfe 0x96                                  ..
##### DEBUG DECIMAL
            254  150
#### RECORD 0 CalBGForPH 2013-04-13T00:51:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-04-13T00:51:27)
    0000   0x5b 0x33 0x20 0x0d 0x0d                   [3 ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 1 PumpSuspend 2013-04-13T09:34:42 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-13T09:34:42)
    0000   0x6a 0x22 0x09 0x0d 0x0d                   j"...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 PumpResume 2013-04-13T09:39:11 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-13T09:39:11)
    0000   0x4b 0x27 0x09 0x0d 0x0d                   K'...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 LowReservoir 2013-04-13T11:10:54 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-04-13T11:10:54)
    0000   0x76 0x0a 0x0b 0x0d 0x0d                   v....
    body (0)

#### RECORD 4 ResultTotals 2013-04-13T13:13:13 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x80                   .....
    decimal
              7    0    0    3  128
    datetime (2013-04-13T13:13:13)
    0000   0x4d 0x0d 0x6d 0x4d 0x0d                   M.mM.
    body (51)
    hex
    0000   0x05 0x00 0x5a 0x5a 0x5a 0x01 0x00 0x00    ..ZZZ...
    0008   0x03 0x80 0x03 0x80 0x64 0x00 0x00 0x00    ....d...
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x21 0x00 0x55 0x04 0x00 0x0e 0x0d    .!.U....
    0030   0x03 0x00 0x00                             ...
    decimal
              5    0   90   90   90    1    0    0
              3  128    3  128  100    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0   12    0  232    0    0
              0   33    0   85    4    0   14   13
              3    0    0
    DAY BITS: [0, 1, 0]
#### RECORD 5 Base (2013, 4, 14, 0, 5, 3) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2e                                  ..
    decimal
              0   46
    datetime ((2013, 4, 14, 0, 5, 3))
    0000   0x43 0x05 0x20 0x0e 0x0d                   C. ..
    body (0)

#### RECORD 6 Prime 2013-04-14T00:05:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-14T00:05:30)
    0000   0x5e 0x05 0x00 0x0e 0x0d                   ^....
    body (0)

#### RECORD 7 CalBGForPH 2013-04-14T00:07:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2013-04-14T00:07:06)
    0000   0x46 0x07 0x20 0x0e 0x0d                   F. ..
    body (0)

#### RECORD 8 BolusWizard 2013-04-14T00:07:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 154,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 33,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 2.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9a                                  [.
    decimal
             91  154
    datetime (2013-04-14T00:07:34)
    0000   0x62 0x07 0x00 0x0e 0x0d                   b....
    body (13)
    hex
    0000   0x21 0x50 0x0d 0x2d 0x6a 0x06 0x19 0x00    !P.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             33   80   13   45  106    6   25    0
              0    0    0   31  125

#### RECORD 9 Bolus 2013-04-14T00:07:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-04-14T00:07:34)
    0000   0x62 0x07 0x40 0x0e 0x0d                   b.@..
    body (0)

#### RECORD 10 CalBGForPH 2013-04-14T01:32:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2013-04-14T01:32:16)
    0000   0x50 0x20 0x21 0x0e 0x0d                   P !..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 PumpSuspend 2013-04-14T09:15:35 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-14T09:15:35)
    0000   0x63 0x0f 0x09 0x0e 0x0d                   c....
    body (0)

#### RECORD 12 PumpResume 2013-04-14T09:41:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-14T09:41:35)
    0000   0x63 0x29 0x09 0x0e 0x0d                   c)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 CalBGForPH 2013-04-14T10:25:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2013-04-14T10:25:38)
    0000   0x66 0x19 0x2a 0x0e 0x0d                   f.*..
    body (0)

#### RECORD 14 BolusWizard 2013-04-14T10:27:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 157,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 2.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9d                                  [.
    decimal
             91  157
    datetime (2013-04-14T10:27:33)
    0000   0x61 0x1b 0x0a 0x0e 0x0d                   a....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x07 0x1d 0x00    &P.-j...
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             38   80   13   45  106    7   29    0
              0    0    0   36  125

#### RECORD 15 Bolus 2013-04-14T10:27:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'dual_component': '??', 'programmed': 3.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2013-04-14T10:27:33)
    0000   0x61 0x1b 0x4a 0x0e 0x0d                   a.J..
    body (0)

#### RECORD 16 CalBGForPH 2013-04-14T11:48:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-04-14T11:48:58)
    0000   0x7a 0x30 0x2b 0x0e 0x0d                   z0+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 CalBGForPH 2013-04-14T12:17:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-04-14T12:17:24)
    0000   0x58 0x11 0x2c 0x0e 0x0d                   X.,..
    body (0)

#### RECORD 18 BolusWizard 2013-04-14T12:18:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-04-14T12:18:04)
    0000   0x44 0x12 0x0c 0x0e 0x0d                   D....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125

#### RECORD 19 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 114, 'amount': 3.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x94 0x72 0x04                   \..r.
    decimal
             92    5  148  114    4
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-04-14T12:18:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-04-14T12:18:04)
    0000   0x44 0x12 0x4c 0x0e 0x0d                   D.L..
    body (0)

#### RECORD 21 CalBGForPH 2013-04-14T15:02:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2013-04-14T15:02:18)
    0000   0x52 0x02 0x2f 0x0e 0x0d                   R./..
    body (0)

#### RECORD 22 CalBGForPH 2013-04-14T15:03:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2013-04-14T15:03:54)
    0000   0x76 0x03 0x2f 0x0e 0x0d                   v./..
    body (0)

#### RECORD 23 BolusWizard 2013-04-14T15:04:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 84,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 26,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2013-04-14T15:04:08)
    0000   0x48 0x04 0x0f 0x0e 0x0d                   H....
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0xfb 0x14 0xf0    .P.-j...
    0008   0x00 0x04 0x00 0x0f 0x7d                   ....}
    decimal
             26   80   13   45  106  251   20  240
              0    4    0   15  125

#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 170, 'amount': 1.9, 'curve': 4},
 {'age': 24, 'amount': 3.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0xaa 0x04 0x94 0x18 0x14    \.L.....
    decimal
             92    8   76  170    4  148   24   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-04-14T15:04:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-04-14T15:04:08)
    0000   0x48 0x04 0x4f 0x0e 0x0d                   H.O..
    body (0)

#### RECORD 26 CalBGForPH 2013-04-14T17:03:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-04-14T17:03:36)
    0000   0x64 0x03 0x31 0x0e 0x0d                   d.1..
    body (0)

#### RECORD 27 BolusWizard 2013-04-14T19:27:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 14,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-04-14T19:27:19)
    0000   0x53 0x1b 0x13 0x0e 0x0d                   S....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125

#### RECORD 28 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 1.5, 'curve': 20},
 {'age': 177, 'amount': 1.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x07 0x14 0x4c 0xb1 0x14    \.<..L..
    decimal
             92    8   60    7   20   76  177   20
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-04-14T19:27:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-04-14T19:27:19)
    0000   0x53 0x1b 0x53 0x0e 0x0d                   S.S..
    body (0)

#### RECORD 30 CalBGForPH 2013-04-14T19:55:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-04-14T19:55:26)
    0000   0x5a 0x37 0x33 0x0e 0x0d                   Z73..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 BolusWizard 2013-04-14T19:55:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 39,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2013-04-14T19:55:54)
    0000   0x76 0x37 0x13 0x0e 0x0d                   v7...
    body (13)
    hex
    0000   0x27 0x50 0x0d 0x2d 0x6a 0xfa 0x1e 0xf0    'P.-j...
    0008   0x00 0x0a 0x00 0x18 0x7d                   ....}
    decimal
             39   80   13   45  106  250   30  240
              0   10    0   24  125
    HOUR BITS: [0, 0, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 1.0, 'curve': 4},
 {'age': 35, 'amount': 1.5, 'curve': 20},
 {'age': 205, 'amount': 1.9, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x1f 0x04 0x3c 0x23 0x14    \.(..<#.
    0008   0x4c 0xcd 0x14                             L..
    decimal
             92   11   40   31    4   60   35   20
             76  205   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-04-14T19:55:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-04-14T19:55:54)
    0000   0x76 0x37 0x53 0x0e 0x0d                   v7S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 34 ResultTotals 2013-04-14T13:13:14 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x90                   .....
    decimal
              7    0    0    5  144
    datetime (2013-04-14T13:13:14)
    0000   0x4e 0x0d 0x6d 0x4e 0x0d                   N.mN.
    body (51)
    hex
    0000   0x05 0x00 0x73 0x49 0xc8 0x09 0x00 0x00    ..sI....
    0008   0x05 0x90 0x03 0x70 0x3e 0x02 0x20 0x26    ...p>. &
    0010   0x00 0xaf 0x02 0x20 0x26 0x01 0xe8 0x5a    ... &..Z
    0018   0x00 0x38 0x0a 0x00 0x00 0x00 0x06 0x04    .8......
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x6f 0x25 0x0d 0x0f 0x0d    ...o%...
    0030   0x1f 0x00 0x46                             ..F
    decimal
              5    0  115   73  200    9    0    0
              5  144    3  112   62    2   32   38
              0  175    2   32   38    1  232   90
              0   56   10    0    0    0    6    4
              0    2    0   12    0  232    0    0
              0   30    0  111   37   13   15   13
             31    0   70
    DAY BITS: [0, 1, 0]
#### RECORD 35 Base (2008, 0, 10, 10, 13, 15) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x0e                                  ..
    decimal
             15   14
    datetime ((2008, 0, 10, 10, 13, 15))
    0000   0x0f 0x0d 0x0a 0x4a 0x68                   ...Jh
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 36 Base (2006, 0, 10, 27, 13, 15) head[2], body[0] op[0x32]

    op hex (2)
    0000   0x32 0x2e                                  2.
    decimal
             50   46
    datetime ((2006, 0, 10, 27, 13, 15))
    0000   0x0f 0x0d 0x5b 0x4a 0x76                   ..[Jv
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 37 Base (2013, 0, 16, 18, 13, 15) head[2], body[0] op[0x32]

    op hex (2)
    0000   0x32 0x0e                                  2.
    decimal
             50   14
    datetime ((2013, 0, 16, 18, 13, 15))
    0000   0x0f 0x0d 0x32 0x50 0x0d                   ..2P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 38 Base (2000, 12, 0, 16, 38, 57) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 38, 57))
    0000   0xf9 0x26 0xf0 0x00 0x00                   .&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 Base (2000, 4, 31, 31, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1f                                  ..
    decimal
              0   31
    datetime ((2000, 4, 31, 31, 1, 61))
    0000   0x7d 0x01 0x1f 0x1f 0x00                   }....
    body (0)

#### RECORD 40 Base (2013, 4, 10, 13, 15, 14) head[2], body[0] op[0x76]

    op hex (2)
    0000   0x76 0x32                                  v2
    decimal
            118   50
    datetime ((2013, 4, 10, 13, 15, 14))
    0000   0x4e 0x0f 0x0d 0x0a 0x4d                   N...M
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 41 Base (2000, 0, 27, 13, 15, 47) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x05                                  r.
    decimal
            114    5
    datetime ((2000, 0, 27, 13, 15, 47))
    0000   0x2f 0x0f 0x0d 0x5b 0x00                   /..[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 42 BasalProfileStart (2000, 0, 20, 13, 15, 16) head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x08                                  {.
    decimal
            123    8
    datetime ((2000, 0, 20, 13, 15, 16))
    0000   0x10 0x0f 0x0d 0x14 0x50                   ....P
    body (3)
    hex
    0000   0x0d 0x2d 0x6a                             .-j
    decimal
             13   45  106
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 43 Base (2015, 0, 0, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0f                                  ..
    decimal
              0   15
    datetime ((2015, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x0f                   .....
    body (0)

#### RECORD 44 Base (2001, 1, 4, 20, 60, 5) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x5c                                  }\
    decimal
            125   92
    datetime ((2001, 1, 4, 20, 60, 5))
    0000   0x05 0x7c 0x54 0x04 0x01                   .|T..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 45 Base (2015, 1, 16, 9, 0, 0) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x0f                                  ..
    decimal
             15   15
    datetime ((2015, 1, 16, 9, 0, 0))
    0000   0x00 0x40 0x09 0x50 0x0f                   .@.P.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 46 Base (2015, 5, 19, 14, 42, 11) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2015, 5, 19, 14, 42, 11))
    0000   0x4b 0x6a 0x0e 0x33 0x0f                   Kj.3.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1]
#### RECORD 47 Base (2015, 5, 19, 15, 5, 11) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2015, 5, 19, 15, 5, 11))
    0000   0x4b 0x45 0x0f 0x13 0x0f                   KE...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 48 Base (2009, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1e                                  ..
    decimal
             13   30
    datetime ((2009, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0xf9                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 49 ChangeTime (2013, 0, 16, 0, 3, 0) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0xf0                                  ..
    decimal
             23  240
    datetime ((2013, 0, 16, 0, 3, 0))
    0000   0x00 0x03 0x00 0x10 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 191, 'amount': 1.5, 'curve': 4},
 {'age': 15, 'amount': 3.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0xbf 0x04 0x7c 0x0f 0x14    \.<..|..
    decimal
             92    8   60  191    4  124   15   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-04-15T19:15:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-04-15T19:15:05)
    0000   0x45 0x0f 0x53 0x0f 0x0d                   E.S..
    body (0)

#### RECORD 52 CalBGForPH 2013-04-15T20:29:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2013-04-15T20:29:59)
    0000   0x7b 0x1d 0x34 0x0f 0x0d                   {.4..
    body (0)

#### RECORD 53 CalBGForPH 2013-04-15T20:50:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2013-04-15T20:50:01)
    0000   0x41 0x32 0x34 0x0f 0x0d                   A24..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 54 BolusWizard 2013-04-15T20:50:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 125,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7d                                  [}
    decimal
             91  125
    datetime (2013-04-15T20:50:11)
    0000   0x4b 0x32 0x14 0x0f 0x0d                   K2...
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x0a 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0   10    0   19  125
    HOUR BITS: [0, 0, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 1.6, 'curve': 4},
 {'age': 30, 'amount': 1.5, 'curve': 20},
 {'age': 110, 'amount': 3.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x60 0x04 0x3c 0x1e 0x14    \.@`.<..
    0008   0x7c 0x6e 0x14                             |n.
    decimal
             92   11   64   96    4   60   30   20
            124  110   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-04-15T20:50:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-04-15T20:50:12)
    0000   0x4c 0x32 0x54 0x0f 0x0d                   L2T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 ResultTotals 2013-04-15T13:13:15 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xae                   .....
    decimal
              7    0    0    4  174
    datetime (2013-04-15T13:13:15)
    0000   0x4f 0x0d 0x6d 0x4f 0x0d                   O.mO.
    body (51)
    hex
    0000   0x05 0x00 0x5f 0x4a 0x7d 0x05 0x00 0x00    .._J}...
    0008   0x04 0xae 0x03 0x6a 0x49 0x01 0x44 0x1b    ...jI.D.
    0010   0x00 0x7d 0x01 0x44 0x1b 0x01 0x44 0x64    .}.D..Dd
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x04 0x04    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x1e 0x00 0x4f 0x2a 0x0c 0x10 0x0d    ...O*...
    0030   0x1f 0x00 0x73                             ..s
    decimal
              5    0   95   74  125    5    0    0
              4  174    3  106   73    1   68   27
              0  125    1   68   27    1   68  100
              0    0    0    0    0    0    4    4
              0    0    0   12    0  232    0    0
              0   30    0   79   42   12   16   13
             31    0  115
    DAY BITS: [0, 1, 0]
#### RECORD 58 Base (2011, 0, 18, 10, 13, 16) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x0c                                  8.
    decimal
             56   12
    datetime ((2011, 0, 18, 10, 13, 16))
    0000   0x10 0x0d 0x0a 0x52 0x6b                   ...Rk
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 59 Base (2014, 0, 18, 27, 13, 16) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x2d                                  8-
    decimal
             56   45
    datetime ((2014, 0, 18, 27, 13, 16))
    0000   0x10 0x0d 0x5b 0x52 0x5e                   ..[R^
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 60 Base (2013, 0, 16, 16, 13, 16) head[2], body[0] op[0x39]

    op hex (2)
    0000   0x39 0x0d                                  9.
    decimal
             57   13
    datetime ((2013, 0, 16, 16, 13, 16))
    0000   0x10 0x0d 0x30 0x50 0x0d                   ..0P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 61 Base (2000, 12, 0, 16, 36, 58) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 12, 0, 16, 36, 58))
    0000   0xfa 0x24 0xf0 0x00 0x00                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 62 Base (2000, 4, 30, 30, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1e                                  ..
    decimal
              0   30
    datetime ((2000, 4, 30, 30, 1, 61))
    0000   0x7d 0x01 0x1e 0x1e 0x00                   }....
    body (0)

#### RECORD 63 Base (2009, 4, 10, 13, 16, 13) head[2], body[0] op[0x5e]

    op hex (2)
    0000   0x5e 0x39                                  ^9
    decimal
             94   57
    datetime ((2009, 4, 10, 13, 16, 13))
    0000   0x4d 0x10 0x0d 0x0a 0x49                   M...I
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 64 Base (2008, 0, 10, 13, 16, 48) head[2], body[0] op[0x47]

    op hex (2)
    0000   0x47 0x08                                  G.
    decimal
             71    8
    datetime ((2008, 0, 10, 13, 16, 48))
    0000   0x30 0x10 0x0d 0x0a 0xb8                   0....
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 65 Base (2001, 0, 10, 13, 16, 49) head[2], body[0] op[0x75]

    op hex (2)
    0000   0x75 0x35                                  u5
    decimal
            117   53
    datetime ((2001, 0, 10, 13, 16, 49))
    0000   0x31 0x10 0x0d 0x0a 0xe1                   1....
    body (0)
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 66 Base (2001, 0, 27, 13, 16, 51) head[2], body[0] op[0x6b]

    op hex (2)
    0000   0x6b 0x24                                  k$
    decimal
            107   36
    datetime ((2001, 0, 27, 13, 16, 51))
    0000   0x33 0x10 0x0d 0x5b 0xe1                   3..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 0]
#### RECORD 67 Sara6E 2000-05-22T06:34:51 head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x24 0x13 0x10 0x0d 0x00 0x50 0x0d    n$....P.
    0008   0x2d 0x6a 0x16 0x00 0x00 0x00 0x00 0x00    -j......
    0010   0x16 0x7d 0x5c 0x05 0x78 0x56 0x14 0x01    .}\.xV..
    0018   0x18 0x18 0x00 0x6e 0x24 0x53 0x10 0x0d    ...n$S..
    0020   0x0a 0x9b 0x6d 0x0e 0x35 0x10 0x0d 0x0a    ..m.5...
    0028   0x73 0x7b 0x24 0x35 0x10 0x0d 0x0a         s{$5...
    decimal
            110   36   19   16   13    0   80   13
             45  106   22    0    0    0    0    0
             22  125   92    5  120   86   20    1
             24   24    0  110   36   83   16   13
             10  155  109   14   53   16   13   10
            115  123   36   53   16   13   10
    datetime (2000-05-22T06:34:51)
    0000   0x73 0x62 0x06 0x36 0x10                   sb.6.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 68 Base (2000, 5, 22, 10, 29, 51) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2000, 5, 22, 10, 29, 51))
    0000   0x73 0x5d 0x0a 0x36 0x10                   s].6.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 69 Base (2000, 5, 22, 11, 22, 51) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2000, 5, 22, 11, 22, 51))
    0000   0x73 0x56 0x0b 0x36 0x10                   sV.6.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 70 Base (2000, 5, 22, 13, 41, 51) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2000, 5, 22, 13, 41, 51))
    0000   0x73 0x69 0x0d 0x36 0x10                   si.6.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 71 Base (2000, 5, 22, 14, 29, 51) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2000, 5, 22, 14, 29, 51))
    0000   0x73 0x5d 0x0e 0x36 0x10                   s].6.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 72 Base (2000, 5, 22, 15, 24, 51) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2000, 5, 22, 15, 24, 51))
    0000   0x73 0x58 0x0f 0x16 0x10                   sX...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 73 Base (2000, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3c                                  .<
    decimal
             13   60
    datetime ((2000, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x00                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 74 Base (2013, 0, 14, 0, 6, 0) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0x00                                  ..
    decimal
             46    0
    datetime ((2013, 0, 14, 0, 6, 0))
    0000   0x00 0x06 0x00 0x2e 0x7d                   ....}
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 75 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 161, 'amount': 2.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0xa1 0x04                   \.`..
    decimal
             92    5   96  161    4
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2013-04-16T22:15:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-04-16T22:15:24)
    0000   0x58 0x0f 0x56 0x10 0x0d                   X.V..
    body (0)

#### RECORD 77 ResultTotals 2013-04-16T13:13:16 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0a                   .....
    decimal
              7    0    0    5   10
    datetime (2013-04-16T13:13:16)
    0000   0x50 0x0d 0x6d 0x50 0x0d                   P.mP.
    body (51)
    hex
    0000   0x05 0x00 0x80 0x49 0xe1 0x0b 0x00 0x00    ...I....
    0008   0x05 0x0a 0x03 0x7a 0x45 0x01 0x90 0x1f    ...zE...
    0010   0x00 0x6c 0x01 0x90 0x1f 0x01 0x30 0x4c    .l....0L
    0018   0x00 0x60 0x18 0x00 0x00 0x00 0x03 0x02    .`......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x69 0x59 0x10 0x21 0x11 0x0d    ..iY.!..
    0030   0x0a 0x35 0x60                             .5`
    decimal
              5    0  128   73  225   11    0    0
              5   10    3  122   69    1  144   31
              0  108    1  144   31    1   48   76
              0   96   24    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0   10  105   89   16   33   17   13
             10   53   96
    DAY BITS: [0, 1, 0]
#### RECORD 78 Base (2004, 2, 21, 27, 13, 17) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2e                                  ..
    decimal
              0   46
    datetime ((2004, 2, 21, 27, 13, 17))
    0000   0x11 0x8d 0x5b 0x35 0x64                   ..[5d
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 79 Base (2013, 0, 17, 0, 13, 17) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0e                                  ..
    decimal
              0   14
    datetime ((2013, 0, 17, 0, 13, 17))
    0000   0x11 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 80 Base (2000, 0, 0, 0, 0, 40) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 40))
    0000   0x28 0x00 0x00 0x00 0x00                   (....
    body (0)

#### RECORD 81 Base (2000, 4, 10, 10, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x28                                  .(
    decimal
              0   40
    datetime ((2000, 4, 10, 10, 1, 61))
    0000   0x7d 0x01 0x2a 0x2a 0x00                   }.**.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 82 ChangeTimeDisplay 2008-04-20T13:17:14 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2008-04-20T13:17:14)
    0000   0x4e 0x11 0x0d 0x34 0xc8                   N..4.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 83 Base (2014, 0, 10, 13, 17, 14) head[2], body[0] op[0x62]

    op hex (2)
    0000   0x62 0x1f                                  b.
    decimal
             98   31
    datetime ((2014, 0, 10, 13, 17, 14))
    0000   0x0e 0x11 0x0d 0x0a 0xce                   .....
    body (0)
    YEAR BITS: [1, 1, 0, 0]
#### RECORD 84 BasalProfileStart (2012, 0, 10, 13, 17, 47) head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x33                                  {3
    decimal
            123   51
    datetime ((2012, 0, 10, 13, 17, 47))
    0000   0x2f 0x11 0x0d 0x0a 0xac                   /....
    body (3)
    hex
    0000   0x45 0x0a 0x30                             E.0
    decimal
             69   10   48
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 85 Base (2000, 2, 14, 18, 1, 10) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x0d                                  ..
    decimal
             17   13
    datetime ((2000, 2, 14, 18, 1, 10))
    0000   0x0a 0x81 0x72 0x2e 0x30                   ..r.0
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 86 Base (2001, 2, 13, 1, 3, 10) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x0d                                  ..
    decimal
             17   13
    datetime ((2001, 2, 13, 1, 3, 10))
    0000   0x0a 0x83 0x61 0x0d 0x31                   ..a.1
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 87 Base (2001, 2, 10, 2, 4, 10) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x0d                                  ..
    decimal
             17   13
    datetime ((2001, 2, 10, 2, 4, 10))
    0000   0x0a 0x84 0x42 0x2a 0x31                   ..B*1
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 88 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x0d                                  ..
    decimal
             17   13
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end logs/ReadHistoryData-page-27.data: 89 records`
