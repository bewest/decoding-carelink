## START logs/ReadHistoryData-page-4.data
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 5.9, 'curve': 4},
 {'age': 94, 'amount': 0.4, 'curve': 4},
 {'age': 134, 'amount': 0.3, 'curve': 4},
 {'age': 28, 'amount': 2.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xec 0x40 0x04 0x10 0x5e 0x04    \..@..^.
    0008   0x0c 0x86 0x04 0x58 0x1c 0x14              ...X..
    decimal
             92   14  236   64    4   16   94    4
             12  134    4   88   28   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-05-29T22:48:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-05-29T22:48:04)
    0000   0x44 0x70 0x56 0x1d 0x0d                   DpV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 ResultTotals 2013-06-29T13:13:29 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x18                   .....
    decimal
              7    0    0    5   24
    datetime (2013-06-29T13:13:29)
    0000   0x5d 0x8d 0x6d 0x5d 0x8d                   ].m].
    body (41)
    hex
    0000   0x05 0x00 0xb8 0xa8 0xe2 0x05 0x00 0x00    ........
    0008   0x05 0x18 0x03 0x84 0x45 0x01 0x94 0x1f    ....E...
    0010   0x00 0x5c 0x01 0x94 0x1f 0x01 0x14 0x44    .\.....D
    0018   0x00 0x80 0x20 0x00 0x00 0x00 0x05 0x01    .. .....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  184  168  226    5    0    0
              5   24    3  132   69    1  148   31
              0   92    1  148   31    1   20   68
              0  128   32    0    0    0    5    1
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 CalBGForPH 2013-05-30T03:07:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 87}
```
    op hex (2)
    0000   0x0a 0x57                                  .W
    decimal
             10   87
    datetime (2013-05-30T03:07:34)
    0000   0x62 0x47 0x23 0x1e 0x0d                   bG#..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 PumpSuspend 2013-05-30T13:44:54 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-30T13:44:54)
    0000   0x76 0x6c 0x0d 0x1e 0x0d                   vl...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 PumpResume 2013-05-30T14:02:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-30T14:02:58)
    0000   0x7a 0x42 0x0e 0x1e 0x0d                   zB...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 CalBGForPH 2013-05-30T14:52:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-05-30T14:52:11)
    0000   0x4b 0x74 0x2e 0x1e 0x0d                   Kt...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 BolusWizard 2013-05-30T14:52:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2013-05-30T14:52:20)
    0000   0x54 0x74 0x0e 0x1e 0x0d                   Tt...
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xfe 0x18 0xf0     P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
             32   80   13   45  106  254   24  240
              0    0    0   22  125
    HOUR BITS: [0, 1, 1]
#### RECORD 8 Bolus 2013-05-30T14:52:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-05-30T14:52:20)
    0000   0x54 0x74 0x4e 0x1e 0x0d                   TtN..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 9 BolusWizard 2013-05-30T15:20:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
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
    datetime (2013-05-30T15:20:49)
    0000   0x71 0x54 0x0f 0x1e 0x0d                   qT...
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [0, 1, 0]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 2.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x24 0x04                   \.X$.
    decimal
             92    5   88   36    4
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-05-30T15:20:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-05-30T15:20:49)
    0000   0x71 0x54 0x4f 0x1e 0x0d                   qTO..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 12 CalBGForPH 2013-05-30T16:45:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2013-05-30T16:45:54)
    0000   0x76 0x6d 0x30 0x1e 0x0d                   vm0..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 13 CalBGForPH 2013-05-30T18:01:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 277}
```
    op hex (2)
    0000   0x0a 0x15                                  ..
    decimal
             10   21
    datetime (2013-05-30T18:01:46)
    0000   0x6e 0x41 0x32 0x1e 0x8d                   nA2..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 14 BolusWizard 2013-05-30T18:01:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 277,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x15                                  [.
    decimal
             91   21
    datetime (2013-05-30T18:01:48)
    0000   0x70 0x41 0x12 0x1e 0x0d                   pA...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x05 0x00 0x1c 0x7d                   ....}
    decimal
              0   81   13   45  106   33    0    0
              0    5    0   28  125
    HOUR BITS: [0, 1, 0]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 167, 'amount': 1.0, 'curve': 4},
 {'age': 197, 'amount': 2.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0xa7 0x04 0x58 0xc5 0x04    \.(..X..
    decimal
             92    8   40  167    4   88  197    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-05-30T18:01:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-05-30T18:01:48)
    0000   0x70 0x41 0x52 0x1e 0x0d                   pAR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 17 CalBGForPH 2013-05-30T19:42:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2013-05-30T19:42:23)
    0000   0x57 0x6a 0x33 0x1e 0x0d                   Wj3..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 18 BolusWizard 2013-05-30T19:42:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 18,
 '_byte[7]': 0,
 'bg': 206,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xce                                  [.
    decimal
             91  206
    datetime (2013-05-30T19:42:28)
    0000   0x5c 0x6a 0x13 0x1e 0x0d                   \j...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x0f 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0   15    0    3  125
    HOUR BITS: [0, 1, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 2.8, 'curve': 4},
 {'age': 12, 'amount': 1.0, 'curve': 20},
 {'age': 42, 'amount': 2.2, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x6c 0x04 0x28 0x0c 0x14    \.pl.(..
    0008   0x58 0x2a 0x14                             X*.
    decimal
             92   11  112  108    4   40   12   20
             88   42   20
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-05-30T19:42:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-05-30T19:42:28)
    0000   0x5c 0x6a 0x53 0x1e 0x0d                   \jS..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 21 LowReservoir 2013-05-30T20:09:28 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-30T20:09:28)
    0000   0x5c 0x49 0x14 0x1e 0x0d                   \I...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 22 CalBGForPH 2013-05-30T22:58:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-05-30T22:58:47)
    0000   0x6f 0x7a 0x36 0x1e 0x0d                   oz6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2013-05-30T22:59:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 160,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.2,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2013-05-30T22:59:22)
    0000   0x56 0x7b 0x16 0x1e 0x0d                   V{...
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x07 0x2e 0x00    =P.-j...
    0008   0x00 0x01 0x00 0x34 0x7d                   ...4}
    decimal
             61   80   13   45  106    7   46    0
              0    1    0   52  125
    HOUR BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 205, 'amount': 0.3, 'curve': 4},
 {'age': 49, 'amount': 2.8, 'curve': 20},
 {'age': 209, 'amount': 1.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0xcd 0x04 0x70 0x31 0x14    \....p1.
    0008   0x28 0xd1 0x14                             (..
    decimal
             92   11   12  205    4  112   49   20
             40  209   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-05-30T22:59:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x34 0x34 0x00                        .44.
    decimal
              1   52   52    0
    datetime (2013-05-30T22:59:23)
    0000   0x57 0x7b 0x56 0x1e 0x0d                   W{V..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 26 ResultTotals 2013-06-30T13:13:30 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x44                   ....D
    decimal
              7    0    0    5   68
    datetime (2013-06-30T13:13:30)
    0000   0x5e 0x8d 0x6d 0x5e 0x8d                   ^.m^.
    body (41)
    hex
    0000   0x05 0x10 0xab 0x57 0x15 0x06 0x00 0x00    ...W....
    0008   0x05 0x44 0x03 0x78 0x42 0x01 0xcc 0x22    .D.xB.."
    0010   0x00 0x6a 0x01 0xcc 0x22 0x01 0x38 0x44    .j..".8D
    0018   0x00 0x94 0x20 0x00 0x00 0x00 0x05 0x02    .. .....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  171   87   21    6    0    0
              5   68    3  120   66    1  204   34
              0  106    1  204   34    1   56   68
              0  148   32    0    0    0    5    2
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 27 LowReservoir 2013-05-31T01:26:15 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-05-31T01:26:15)
    0000   0x4f 0x5a 0x01 0x1f 0x0d                   OZ...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 28 Rewind 2013-05-31T15:33:12 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-05-31T15:33:12)
    0000   0x4c 0x61 0x0f 0x1f 0x0d                   La...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 29 Prime 2013-05-31T15:35:01 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x24                   ....$
    decimal
              3    0    0    0   36
    datetime (2013-05-31T15:35:01)
    0000   0x41 0x63 0x2f 0x1f 0x0d                   Ac/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 30 Prime 2013-05-31T15:35:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-05-31T15:35:19)
    0000   0x53 0x63 0x0f 0x1f 0x0d                   Sc...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 31 CalBGForPH 2013-05-31T18:17:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-05-31T18:17:25)
    0000   0x59 0x51 0x32 0x1f 0x0d                   YQ2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 32 CalBGForPH 2013-05-31T18:18:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-05-31T18:18:13)
    0000   0x4d 0x52 0x32 0x1f 0x0d                   MR2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 33 CalBGForPH 2013-05-31T18:40:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-05-31T18:40:21)
    0000   0x55 0x68 0x32 0x1f 0x0d                   Uh2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 34 BolusWizard 2013-05-31T18:40:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 41,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-05-31T18:40:36)
    0000   0x64 0x68 0x12 0x1f 0x0d                   dh...
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x00 0x1f 0x00    )P.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             41   80   13   45  106    0   31    0
              0    0    0   31  125
    HOUR BITS: [0, 1, 1]
#### RECORD 35 Bolus 2013-05-31T18:40:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-05-31T18:40:36)
    0000   0x64 0x68 0x52 0x1f 0x0d                   dhR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 36 CalBGForPH 2013-05-31T21:19:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 266}
```
    op hex (2)
    0000   0x0a 0x0a                                  ..
    decimal
             10   10
    datetime (2013-05-31T21:19:16)
    0000   0x50 0x53 0x35 0x1f 0x8d                   PS5..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 37 BolusWizard 2013-05-31T21:19:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 266,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0a                                  [.
    decimal
             91   10
    datetime (2013-05-31T21:19:19)
    0000   0x53 0x53 0x15 0x1f 0x0d                   SS...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x07 0x00 0x18 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    7    0   24  125
    HOUR BITS: [0, 1, 0]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 165, 'amount': 3.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0xa5 0x04                   \.|..
    decimal
             92    5  124  165    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-05-31T21:19:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-05-31T21:19:19)
    0000   0x53 0x53 0x55 0x1f 0x0d                   SSU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 40 ResultTotals (2013, 6, 31, 13, 13, 31) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x5e                   ....^
    decimal
              7    0    0    4   94
    datetime ((2013, 6, 31, 13, 13, 31))
    0000   0x5f 0x8d 0x6d 0x5f 0x8d                   _.m_.
    body (41)
    hex
    0000   0x05 0x10 0x9a 0x6a 0x0a 0x04 0x00 0x00    ...j....
    0008   0x04 0x5e 0x03 0x82 0x50 0x00 0xdc 0x14    .^..P...
    0010   0x00 0x29 0x00 0xdc 0x14 0x00 0x7c 0x38    .)....|8
    0018   0x00 0x60 0x2c 0x00 0x00 0x00 0x02 0x01    .`,.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  154  106   10    4    0    0
              4   94    3  130   80    0  220   20
              0   41    0  220   20    0  124   56
              0   96   44    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 41 CalBGForPH 2013-06-01T00:32:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-06-01T00:32:57)
    0000   0x79 0xa0 0x20 0x01 0x0d                   y. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 42 BolusWizard 2013-06-01T00:33:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-06-01T00:33:19)
    0000   0x53 0xa1 0x00 0x01 0x0d                   S....
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0x00 0x25 0x00    1P.-j.%.
    0008   0x00 0x03 0x00 0x25 0x7d                   ...%}
    decimal
             49   80   13   45  106    0   37    0
              0    3    0   37  125
    HOUR BITS: [1, 0, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 199, 'amount': 2.4, 'curve': 4},
 {'age': 103, 'amount': 3.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x60 0xc7 0x04 0x7c 0x67 0x14    \.`..|g.
    decimal
             92    8   96  199    4  124  103   20
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-06-01T00:33:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'dual_component': '??', 'programmed': 3.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2013-06-01T00:33:20)
    0000   0x54 0xa1 0x40 0x01 0x0d                   T.@..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 45 CalBGForPH 2013-06-01T05:14:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2013-06-01T05:14:41)
    0000   0x69 0x8e 0x25 0x01 0x0d                   i.%..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 46 CalBGForPH 2013-06-01T10:58:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 252}
```
    op hex (2)
    0000   0x0a 0xfc                                  ..
    decimal
             10  252
    datetime (2013-06-01T10:58:15)
    0000   0x4f 0xba 0x2a 0x01 0x0d                   O.*..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 47 BolusWizard 2013-06-01T10:58:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 252,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfc                                  [.
    decimal
             91  252
    datetime (2013-06-01T10:58:18)
    0000   0x52 0xba 0x0a 0x01 0x0d                   R....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    0    0   28  125
    HOUR BITS: [1, 0, 1]
#### RECORD 48 Bolus 2013-06-01T10:58:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-06-01T10:58:18)
    0000   0x52 0xba 0x4a 0x01 0x0d                   R.J..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 CalBGForPH 2013-06-01T16:16:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-06-01T16:16:45)
    0000   0x6d 0x90 0x30 0x01 0x0d                   m.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 BolusWizard 2013-06-01T16:17:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 2.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2013-06-01T16:17:02)
    0000   0x42 0x91 0x10 0x01 0x0d                   B....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0xfa 0x16 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             29   80   13   45  106  250   22  240
              0    0    0   16  125
    HOUR BITS: [1, 0, 0]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 2.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0x43 0x14                   \.pC.
    decimal
             92    5  112   67   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2013-06-01T16:17:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-06-01T16:17:03)
    0000   0x43 0x91 0x50 0x01 0x0d                   C.P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 CalBGForPH 2013-06-01T20:20:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 313}
```
    op hex (2)
    0000   0x0a 0x39                                  .9
    decimal
             10   57
    datetime (2013-06-01T20:20:50)
    0000   0x72 0x94 0x34 0x01 0x8d                   r.4..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 54 BolusWizard 2013-06-01T20:20:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 41,
 '_byte[7]': 0,
 'bg': 313,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x39                                  [9
    decimal
             91   57
    datetime (2013-06-01T20:20:52)
    0000   0x74 0x94 0x14 0x01 0x0d                   t....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x29 0x00 0x00    .Q.-j)..
    0008   0x00 0x00 0x00 0x29 0x7d                   ...)}
    decimal
              0   81   13   45  106   41    0    0
              0    0    0   41  125
    HOUR BITS: [1, 0, 0]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 246, 'amount': 1.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0xf6 0x04                   \.@..
    decimal
             92    5   64  246    4
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-06-01T20:20:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'dual_component': '??', 'programmed': 4.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2013-06-01T20:20:52)
    0000   0x74 0x94 0x54 0x01 0x0d                   t.T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 57 CalBGForPH 2013-06-01T21:10:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 307}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2013-06-01T21:10:49)
    0000   0x71 0x8a 0x35 0x01 0x8d                   q.5..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 58 BolusWizard 2013-06-01T21:11:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 40,
 '_byte[7]': 0,
 'bg': 307,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x33                                  [3
    decimal
             91   51
    datetime (2013-06-01T21:11:01)
    0000   0x41 0x8b 0x15 0x01 0x0d                   A....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x28 0x00 0x00    .Q.-j(..
    0008   0x00 0x23 0x00 0x05 0x7d                   .#..}
    decimal
              0   81   13   45  106   40    0    0
              0   35    0    5  125
    HOUR BITS: [1, 0, 0]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 57, 'amount': 4.1, 'curve': 4},
 {'age': 41, 'amount': 1.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xa4 0x39 0x04 0x40 0x29 0x14    \..9.@).
    decimal
             92    8  164   57    4   64   41   20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-06-01T21:11:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-06-01T21:11:01)
    0000   0x41 0x8b 0x55 0x01 0x0d                   A.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 61 CalBGForPH 2013-06-01T22:49:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-06-01T22:49:58)
    0000   0x7a 0xb1 0x36 0x01 0x0d                   z.6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 62 BolusWizard 2013-06-01T22:50:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-06-01T22:50:24)
    0000   0x58 0xb2 0x16 0x01 0x0d                   X....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0x00 0x16 0x00    .P.-j...
    0008   0x00 0x10 0x00 0x16 0x7d                   ....}
    decimal
             29   80   13   45  106    0   22    0
              0   16    0   22  125
    HOUR BITS: [1, 0, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 106, 'amount': 0.9, 'curve': 4},
 {'age': 156, 'amount': 4.1, 'curve': 4},
 {'age': 140, 'amount': 1.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x24 0x6a 0x04 0xa4 0x9c 0x04    \.$j....
    0008   0x40 0x8c 0x14                             @..
    decimal
             92   11   36  106    4  164  156    4
             64  140   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-06-01T22:50:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-06-01T22:50:24)
    0000   0x58 0xb2 0x56 0x01 0x0d                   X.V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 65 ResultTotals 2013-04-01T13:13:33 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe8                   .....
    decimal
              7    0    0    5  232
    datetime (2013-04-01T13:13:33)
    0000   0x61 0x0d 0x6d 0x61 0x0d                   a.ma.
    body (41)
    hex
    0000   0x05 0x10 0xb3 0x43 0x39 0x07 0x00 0x00    ...C9...
    0008   0x05 0xe8 0x03 0x84 0x3c 0x02 0x64 0x28    ....<.d(
    0010   0x00 0x6b 0x02 0x64 0x28 0x01 0x2c 0x31    .k.d(.,1
    0018   0x01 0x38 0x33 0x00 0x00 0x00 0x06 0x03    .83.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  179   67   57    7    0    0
              5  232    3  132   60    2  100   40
              0  107    2  100   40    1   44   49
              1   56   51    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 1]
#### RECORD 66 CalBGForPH 2013-06-02T02:21:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 361}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-06-02T02:21:17)
    0000   0x51 0x95 0x22 0x02 0x8d                   Q."..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 67 BolusWizard 2013-06-02T02:21:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 52,
 '_byte[7]': 0,
 'bg': 361,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-06-02T02:21:20)
    0000   0x54 0x95 0x02 0x02 0x0d                   T....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x34 0x00 0x00    .Q.-j4..
    0008   0x00 0x02 0x00 0x32 0x7d                   ...2}
    decimal
              0   81   13   45  106   52    0    0
              0    2    0   50  125
    HOUR BITS: [1, 0, 0]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 2.2, 'curve': 4},
 {'age': 61, 'amount': 0.9, 'curve': 20},
 {'age': 111, 'amount': 4.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0xd9 0x04 0x24 0x3d 0x14    \.X..$=.
    0008   0xa4 0x6f 0x14                             .o.
    decimal
             92   11   88  217    4   36   61   20
            164  111   20
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-06-02T02:21:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-06-02T02:21:20)
    0000   0x54 0x95 0x42 0x02 0x0d                   T.B..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 70 PumpSuspend 2013-06-02T09:21:25 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-02T09:21:25)
    0000   0x59 0x95 0x09 0x02 0x0d                   Y....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 71 PumpResume 2013-06-02T09:37:13 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-02T09:37:13)
    0000   0x4d 0xa5 0x09 0x02 0x0d                   M....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 72 CalBGForPH 2013-06-02T11:20:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 164}
```
    op hex (2)
    0000   0x0a 0xa4                                  ..
    decimal
             10  164
    datetime (2013-06-02T11:20:53)
    0000   0x75 0x94 0x2b 0x02 0x0d                   u.+..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 73 BolusWizard 2013-06-02T11:21:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 164,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa4                                  [.
    decimal
             91  164
    datetime (2013-06-02T11:21:03)
    0000   0x43 0x95 0x0b 0x02 0x0d                   C....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    0    0    8  125
    HOUR BITS: [1, 0, 0]
#### RECORD 74 Bolus 2013-06-02T11:21:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-06-02T11:21:03)
    0000   0x43 0x95 0x4b 0x02 0x0d                   C.K..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 75 CalBGForPH 2013-06-02T12:34:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-06-02T12:34:22)
    0000   0x56 0xa2 0x2c 0x02 0x0d                   V.,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 76 BolusWizard 2013-06-02T12:35:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 123,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 39,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2013-06-02T12:35:08)
    0000   0x48 0xa3 0x0c 0x02 0x0d                   H....
    body (13)
    hex
    0000   0x27 0x50 0x0d 0x2d 0x6a 0x00 0x1e 0x00    'P.-j...
    0008   0x00 0x07 0x00 0x1e 0x7d                   ....}
    decimal
             39   80   13   45  106    0   30    0
              0    7    0   30  125
    HOUR BITS: [1, 0, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 81, 'amount': 1.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x51 0x04                   \.(Q.
    decimal
             92    5   40   81    4
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2013-06-02T12:35:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-06-02T12:35:08)
    0000   0x48 0xa3 0x4c 0x02 0x0d                   H.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 BolusWizard 2013-06-02T12:44:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 10,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.7,
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
    datetime (2013-06-02T12:44:22)
    0000   0x56 0xac 0x0c 0x02 0x0d                   V....
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106    0    7    0
              0    0    0    7  125
    HOUR BITS: [1, 0, 1]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 3.0, 'curve': 4},
 {'age': 90, 'amount': 1.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x78 0x0a 0x04 0x28 0x5a 0x04    \.x..(Z.
    decimal
             92    8  120   10    4   40   90    4
    datetime (unknown)

    body (0)

#### RECORD 81 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x8f                                  ..
    decimal
              0  143
    datetime (unknown)
    0000   0xed                                       .
    body (0)

`end logs/ReadHistoryData-page-4.data: 82 records`
