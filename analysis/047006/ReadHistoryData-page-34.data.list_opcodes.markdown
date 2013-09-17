## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x40 0x86                                  @.
##### DEBUG DECIMAL
             64  134
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 115, 'amount': 1.9, 'curve': 20},
 {'age': 125, 'amount': 2.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x73 0x14 0x70 0x7d 0x14    \.Ls.p}.
    decimal
             92    8   76  115   20  112  125   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-02-12T21:25:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.8, 'dual_component': '??', 'programmed': 5.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3a 0x3a 0x00                        .::.
    decimal
              1   58   58    0
    datetime (2013-02-12T21:25:14)
    0000   0x0e 0x99 0x55 0x0c 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 2 ResultTotals (2013, 0, 12, 13, 13, 44) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x00                   .....
    decimal
              7    0    0    5    0
    datetime ((2013, 0, 12, 13, 13, 44))
    0000   0x2c 0x0d 0x6d 0x2c 0x0d                   ,.m,.
    body (41)
    hex
    0000   0x05 0x00 0x9e 0x71 0xdb 0x03 0x00 0x00    ...q....
    0008   0x05 0x00 0x03 0x5c 0x43 0x01 0xa4 0x21    ...\C..!
    0010   0x00 0x6c 0x01 0xa4 0x21 0x01 0x48 0x4e    .l..!.HN
    0018   0x00 0x5c 0x16 0x00 0x00 0x00 0x02 0x00    .\......
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  158  113  219    3    0    0
              5    0    3   92   67    1  164   33
              0  108    1  164   33    1   72   78
              0   92   22    0    0    0    2    0
              0    2    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 3 CalBGForPH 2013-02-13T01:09:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2013-02-13T01:09:00)
    0000   0x00 0x89 0x21 0x0d 0x0d                   ..!..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 PumpSuspend 2013-02-13T12:17:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-13T12:17:15)
    0000   0x0f 0x91 0x0c 0x0d 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 PumpResume 2013-02-13T13:09:56 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-13T13:09:56)
    0000   0x38 0x89 0x0d 0x0d 0x0d                   8....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 CalBGForPH 2013-02-13T13:10:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-02-13T13:10:50)
    0000   0x32 0x8a 0x2d 0x0d 0x0d                   2.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 BolusWizard 2013-02-13T13:11:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 199,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc7                                  [.
    decimal
             91  199
    datetime (2013-02-13T13:11:06)
    0000   0x06 0x8b 0x0d 0x0d 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125
    HOUR BITS: [1, 0, 0]
#### RECORD 8 Bolus 2013-02-13T13:11:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-02-13T13:11:06)
    0000   0x06 0x8b 0x4d 0x0d 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 9 CalBGForPH 2013-02-13T13:44:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2013-02-13T13:44:08)
    0000   0x08 0xac 0x2d 0x0d 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 10 BolusWizard 2013-02-13T13:45:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 154,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9a                                  [.
    decimal
             91  154
    datetime (2013-02-13T13:45:43)
    0000   0x2b 0xad 0x0d 0x0d 0x0d                   +....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x06 0x14 0x00    .P.-j...
    0008   0x00 0x11 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    6   20    0
              0   17    0   20  125
    HOUR BITS: [1, 0, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 1.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x48 0x29 0x04                   \.H).
    decimal
             92    5   72   41    4
    datetime (unknown)

    body (0)

#### RECORD 12 LowReservoir 2013-02-13T13:46:16 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-02-13T13:46:16)
    0000   0x10 0xae 0x0d 0x0d 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 13 Bolus 2013-02-13T13:45:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-02-13T13:45:44)
    0000   0x2c 0xad 0x4d 0x0d 0x0d                   ,.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 14 BolusWizard 2013-02-13T14:12:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.7,
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
    datetime (2013-02-13T14:12:51)
    0000   0x33 0x8c 0x0e 0x0d 0x0d                   3....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 0]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 2.0, 'curve': 4},
 {'age': 68, 'amount': 1.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0x1c 0x04 0x48 0x44 0x04    \.P..HD.
    decimal
             92    8   80   28    4   72   68    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-02-13T14:12:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-02-13T14:12:51)
    0000   0x33 0x8c 0x4e 0x0d 0x0d                   3.N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 CalBGForPH 2013-02-13T16:12:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2013-02-13T16:12:25)
    0000   0x19 0x8c 0x30 0x0d 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 18 CalBGForPH 2013-02-13T17:36:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2013-02-13T17:36:24)
    0000   0x18 0xa4 0x31 0x0d 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 19 BolusWizard 2013-02-13T17:36:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2013-02-13T17:36:28)
    0000   0x1c 0xa4 0x11 0x0d 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x07 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    3    0    7  125
    HOUR BITS: [1, 0, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 212, 'amount': 1.7, 'curve': 4},
 {'age': 232, 'amount': 2.0, 'curve': 4},
 {'age': 16, 'amount': 1.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x44 0xd4 0x04 0x50 0xe8 0x04    \.D..P..
    0008   0x48 0x10 0x14                             H..
    decimal
             92   11   68  212    4   80  232    4
             72   16   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-02-13T17:36:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-02-13T17:36:28)
    0000   0x1c 0xa4 0x51 0x0d 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 LowReservoir 2013-02-13T20:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-02-13T20:41:03)
    0000   0x03 0xa9 0x14 0x0d 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 23 CalBGForPH 2013-02-13T21:39:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2013-02-13T21:39:20)
    0000   0x14 0xa7 0x35 0x0d 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 BolusWizard 2013-02-13T21:39:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 139,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 52,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8b                                  [.
    decimal
             91  139
    datetime (2013-02-13T21:39:42)
    0000   0x2a 0xa7 0x15 0x0d 0x0d                   *....
    body (13)
    hex
    0000   0x34 0x50 0x0d 0x2d 0x6a 0x03 0x28 0x00    4P.-j.(.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             52   80   13   45  106    3   40    0
              0    0    0   43  125
    HOUR BITS: [1, 0, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 245, 'amount': 0.5, 'curve': 4},
 {'age': 199, 'amount': 1.7, 'curve': 20},
 {'age': 219, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x14 0xf5 0x04 0x44 0xc7 0x14    \....D..
    0008   0x50 0xdb 0x14                             P..
    decimal
             92   11   20  245    4   68  199   20
             80  219   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-02-13T21:39:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-02-13T21:39:42)
    0000   0x2a 0xa7 0x55 0x0d 0x0d                   *.U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 27 ResultTotals (2013, 0, 13, 13, 13, 45) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf6                   .....
    decimal
              7    0    0    4  246
    datetime ((2013, 0, 13, 13, 13, 45))
    0000   0x2d 0x0d 0x6d 0x2d 0x0d                   -.m-.
    body (41)
    hex
    0000   0x05 0x00 0x94 0x61 0xc7 0x06 0x00 0x00    ...a....
    0008   0x04 0xf6 0x03 0x5e 0x44 0x01 0x98 0x20    ...^D.. 
    0010   0x00 0x66 0x01 0x98 0x20 0x01 0x34 0x4b    .f.. .4K
    0018   0x00 0x64 0x19 0x00 0x00 0x00 0x05 0x02    .d......
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  148   97  199    6    0    0
              4  246    3   94   68    1  152   32
              0  102    1  152   32    1   52   75
              0  100   25    0    0    0    5    2
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 28 Rewind 2013-02-14T08:16:39 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-02-14T08:16:39)
    0000   0x27 0x90 0x08 0x0e 0x0d                   '....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 Prime 2013-02-14T08:18:16 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 5.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x39                   ....9
    decimal
              3    0    0    0   57
    datetime (2013-02-14T08:18:16)
    0000   0x10 0x92 0x28 0x0e 0x0d                   ..(..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 Prime 2013-02-14T08:18:40 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-02-14T08:18:40)
    0000   0x28 0x92 0x08 0x0e 0x0d                   (....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 CalBGForPH 2013-02-14T08:22:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 423}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-02-14T08:22:44)
    0000   0x2c 0x96 0x28 0x0e 0x8d                   ,.(..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 32 BolusWizard 2013-02-14T08:22:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 66,
 '_byte[7]': 0,
 'bg': 423,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-02-14T08:22:50)
    0000   0x32 0x96 0x08 0x0e 0x0d                   2....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x42 0x00 0x00    .Q.-jB..
    0008   0x00 0x00 0x00 0x42 0x7d                   ...B}
    decimal
              0   81   13   45  106   66    0    0
              0    0    0   66  125
    HOUR BITS: [1, 0, 0]
#### RECORD 33 Bolus 2013-02-14T08:22:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.8, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x44 0x44 0x00                        .DD.
    decimal
              1   68   68    0
    datetime (2013-02-14T08:22:50)
    0000   0x32 0x96 0x48 0x0e 0x0d                   2.H..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 34 PumpSuspend 2013-02-14T10:57:25 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-14T10:57:25)
    0000   0x19 0xb9 0x0a 0x0e 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 35 PumpResume 2013-02-14T11:10:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-14T11:10:37)
    0000   0x25 0x8a 0x0b 0x0e 0x0d                   %....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 CalBGForPH 2013-02-14T11:37:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 223}
```
    op hex (2)
    0000   0x0a 0xdf                                  ..
    decimal
             10  223
    datetime (2013-02-14T11:37:14)
    0000   0x0e 0xa5 0x2b 0x0e 0x0d                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 37 BolusWizard 2013-02-14T11:37:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 223,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdf                                  [.
    decimal
             91  223
    datetime (2013-02-14T11:37:17)
    0000   0x11 0xa5 0x0b 0x0e 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x0c 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    9    0   12  125
    HOUR BITS: [1, 0, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 5.05, 'curve': 4},
 {'age': 203, 'amount': 1.75, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xca 0xc1 0x04 0x46 0xcb 0x04    \....F..
    decimal
             92    8  202  193    4   70  203    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-02-14T11:37:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-02-14T11:37:17)
    0000   0x11 0xa5 0x4b 0x0e 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 40 CalBGForPH 2013-02-14T13:02:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-02-14T13:02:05)
    0000   0x05 0x82 0x2d 0x0e 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 41 BolusWizard 2013-02-14T13:02:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 30,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2013-02-14T13:02:43)
    0000   0x2b 0x82 0x0d 0x0e 0x0d                   +....
    body (13)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0xfa 0x17 0xf0    .P.-j...
    0008   0x00 0x08 0x00 0x11 0x7d                   ....}
    decimal
             30   80   13   45  106  250   23  240
              0    8    0   17  125
    HOUR BITS: [1, 0, 0]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 1.2, 'curve': 4},
 {'age': 22, 'amount': 5.05, 'curve': 20},
 {'age': 32, 'amount': 1.75, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x58 0x04 0xca 0x16 0x14    \.0X....
    0008   0x46 0x20 0x14                             F .
    decimal
             92   11   48   88    4  202   22   20
             70   32   20
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-02-14T13:02:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-02-14T13:02:43)
    0000   0x2b 0x82 0x4d 0x0e 0x0d                   +.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 44 CalBGForPH 2013-02-14T13:43:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-02-14T13:43:36)
    0000   0x24 0xab 0x2d 0x0e 0x0d                   $.-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 45 BolusWizard 2013-02-14T13:43:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-02-14T13:43:56)
    0000   0x38 0xab 0x0d 0x0e 0x0d                   8....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0xfd 0x15 0xf0    .P.-j...
    0008   0x00 0x14 0x00 0x12 0x7d                   ....}
    decimal
             28   80   13   45  106  253   21  240
              0   20    0   18  125
    HOUR BITS: [1, 0, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 1.7, 'curve': 4},
 {'age': 129, 'amount': 1.2, 'curve': 4},
 {'age': 63, 'amount': 5.05, 'curve': 20},
 {'age': 73, 'amount': 1.75, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x44 0x31 0x04 0x30 0x81 0x04    \.D1.0..
    0008   0xca 0x3f 0x14 0x46 0x49 0x14              .?.FI.
    decimal
             92   14   68   49    4   48  129    4
            202   63   20   70   73   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-02-14T13:43:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-02-14T13:43:56)
    0000   0x38 0xab 0x4d 0x0e 0x0d                   8.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 48 CalBGForPH 2013-02-14T23:27:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-02-14T23:27:30)
    0000   0x1e 0x9b 0x37 0x0e 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 49 BolusWizard 2013-02-14T23:27:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 14,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 1.0,
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
    datetime (2013-02-14T23:27:56)
    0000   0x38 0x9b 0x17 0x0e 0x0d                   8....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0xfa 0x0a 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
             14   80   13   45  106  250   10  240
              0    0    0    4  125
    HOUR BITS: [1, 0, 0]
#### RECORD 50 Bolus 2013-02-14T23:27:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-02-14T23:27:56)
    0000   0x38 0x9b 0x57 0x0e 0x0d                   8.W..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 ResultTotals (2013, 0, 14, 13, 13, 46) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x56                   ....V
    decimal
              7    0    0    5   86
    datetime ((2013, 0, 14, 13, 13, 46))
    0000   0x2e 0x0d 0x6d 0x2e 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb4 0x50 0xa7 0x05 0x00 0x00    ...P....
    0008   0x05 0x56 0x03 0x7a 0x41 0x01 0xdc 0x23    .V.zA..#
    0010   0x00 0x48 0x01 0xdc 0x23 0x00 0x9c 0x21    .H..#..!
    0018   0x01 0x40 0x43 0x00 0x00 0x00 0x05 0x03    .@C.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  180   80  167    5    0    0
              5   86    3  122   65    1  220   35
              0   72    1  220   35    0  156   33
              1   64   67    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 52 CalBGForPH 2013-02-15T08:59:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 249}
```
    op hex (2)
    0000   0x0a 0xf9                                  ..
    decimal
             10  249
    datetime (2013-02-15T08:59:54)
    0000   0x36 0xbb 0x28 0x0f 0x0d                   6.(..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 53 BolusWizard 2013-02-15T08:59:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 27,
 '_byte[7]': 0,
 'bg': 249,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf9                                  [.
    decimal
             91  249
    datetime (2013-02-15T08:59:58)
    0000   0x3a 0xbb 0x08 0x0f 0x0d                   :....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1b 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
              0   80   13   45  106   27    0    0
              0    0    0   27  125
    HOUR BITS: [1, 0, 1]
#### RECORD 54 Bolus 2013-02-15T08:59:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-02-15T08:59:58)
    0000   0x3a 0xbb 0x48 0x0f 0x0d                   :.H..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 55 CalBGForPH 2013-02-15T14:05:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-02-15T14:05:51)
    0000   0x33 0x85 0x2e 0x0f 0x0d                   3....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 PumpSuspend 2013-02-15T14:39:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-15T14:39:30)
    0000   0x1e 0xa7 0x0e 0x0f 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 57 PumpResume 2013-02-15T15:04:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-15T15:04:08)
    0000   0x08 0x84 0x0f 0x0f 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 58 CalBGForPH 2013-02-15T15:43:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-02-15T15:43:29)
    0000   0x1d 0xab 0x2f 0x0f 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 59 BolusWizard 2013-02-15T15:43:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 86,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 3.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x56                                  [V
    decimal
             91   86
    datetime (2013-02-15T15:43:43)
    0000   0x2b 0xab 0x0f 0x0f 0x0d                   +....
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0xfb 0x25 0xf0    1P.-j.%.
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             49   80   13   45  106  251   37  240
              0    0    0   32  125
    HOUR BITS: [1, 0, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 153, 'amount': 2.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0x99 0x14                   \.l..
    decimal
             92    5  108  153   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-02-15T15:43:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-02-15T15:43:44)
    0000   0x2c 0xab 0x4f 0x0f 0x0d                   ,.O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 62 BolusWizard 2013-02-15T15:59:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.7,
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
    datetime (2013-02-15T15:59:29)
    0000   0x1d 0xbb 0x0f 0x0f 0x0d                   .....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 2.8, 'curve': 4},
 {'age': 25, 'amount': 0.4, 'curve': 4},
 {'age': 169, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x70 0x0f 0x04 0x10 0x19 0x04    \.p.....
    0008   0x6c 0xa9 0x14                             l..
    decimal
             92   11  112   15    4   16   25    4
            108  169   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-02-15T15:59:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-02-15T15:59:29)
    0000   0x1d 0xbb 0x4f 0x0f 0x0d                   ..O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 65 CalBGForPH 2013-02-15T20:38:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-02-15T20:38:36)
    0000   0x24 0xa6 0x34 0x0f 0x0d                   $.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 66 CalBGForPH 2013-02-15T20:39:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-02-15T20:39:39)
    0000   0x27 0xa7 0x34 0x0f 0x0d                   '.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 67 BolusWizard 2013-02-15T20:40:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-02-15T20:40:03)
    0000   0x03 0xa8 0x14 0x0f 0x0d                   .....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x00 0x1d 0x00    &P.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
             38   80   13   45  106    0   29    0
              0    0    0   29  125
    HOUR BITS: [1, 0, 1]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.7, 'curve': 20},
 {'age': 40, 'amount': 2.8, 'curve': 20},
 {'age': 50, 'amount': 0.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x44 0x1e 0x14 0x70 0x28 0x14    \.D..p(.
    0008   0x10 0x32 0x14                             .2.
    decimal
             92   11   68   30   20  112   40   20
             16   50   20
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-02-15T20:40:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-02-15T20:40:03)
    0000   0x03 0xa8 0x54 0x0f 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 70 CalBGForPH 2013-02-15T23:04:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 195}
```
    op hex (2)
    0000   0x0a 0xc3                                  ..
    decimal
             10  195
    datetime (2013-02-15T23:04:40)
    0000   0x28 0x84 0x37 0x0f 0x0d                   (.7..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 71 BolusWizard 2013-02-15T23:04:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 195,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc3                                  [.
    decimal
             91  195
    datetime (2013-02-15T23:04:52)
    0000   0x34 0x84 0x17 0x0f 0x0d                   4....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0    9    0    6  125
    HOUR BITS: [1, 0, 0]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 2.9, 'curve': 4},
 {'age': 174, 'amount': 1.7, 'curve': 20},
 {'age': 184, 'amount': 2.8, 'curve': 20},
 {'age': 194, 'amount': 0.4, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x74 0x96 0x04 0x44 0xae 0x14    \.t..D..
    0008   0x70 0xb8 0x14 0x10 0xc2 0x14              p.....
    decimal
             92   14  116  150    4   68  174   20
            112  184   20   16  194   20
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-02-15T23:04:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-02-15T23:04:52)
    0000   0x34 0x84 0x57 0x0f 0x0d                   4.W..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 74 ResultTotals (2013, 0, 15, 13, 13, 47) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x38                   ....8
    decimal
              7    0    0    5   56
    datetime ((2013, 0, 15, 13, 13, 47))
    0000   0x2f 0x0d 0x6d 0x2f 0x0d                   /.m/.
    body (41)
    hex
    0000   0x05 0x00 0x91 0x56 0xf9 0x06 0x00 0x00    ...V....
    0008   0x05 0x38 0x03 0x74 0x42 0x01 0xc4 0x22    .8.tB.."
    0010   0x00 0x6e 0x01 0xc4 0x22 0x01 0x38 0x45    .n..".8E
    0018   0x00 0x8c 0x1f 0x00 0x00 0x00 0x05 0x03    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  145   86  249    6    0    0
              5   56    3  116   66    1  196   34
              0  110    1  196   34    1   56   69
              0  140   31    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 75 CalBGForPH 2013-02-16T20:35:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2013-02-16T20:35:44)
    0000   0x2c 0xa3 0x34 0x10 0x0d                   ,.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 76 BolusWizard 2013-02-16T20:35:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 20,
 '_byte[7]': 0,
 'bg': 215,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd7                                  [.
    decimal
             91  215
    datetime (2013-02-16T20:35:50)
    0000   0x32 0xa3 0x14 0x10 0x0d                   2....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125
    HOUR BITS: [1, 0, 1]
#### RECORD 77 Bolus 2013-02-16T20:35:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-02-16T20:35:50)
    0000   0x32 0xa3 0x54 0x10 0x0d                   2.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 78 CalBGForPH 2013-02-16T21:09:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 173}
```
    op hex (2)
    0000   0x0a 0xad                                  ..
    decimal
             10  173
    datetime (2013-02-16T21:09:08)
    0000   0x08 0x89 0x35 0x10 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 79 CalBGForPH 2013-02-16T21:16:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-02-16T21:16:44)
    0000   0x2c 0x90 0x35 0x10 0x0d                   ,.5..
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-34.data: 80 records`
