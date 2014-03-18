## START logs/ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x76 0x49                                  vI
##### DEBUG DECIMAL
            118   73
#### RECORD 0 Model522ResultTotals 2013-05-25T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-25T00:00:00)
    0000   0x58 0x8d                                  X.
    body (41)
    hex
    0000   0x05 0x00 0x6c 0x6c 0x6c 0x01 0x00 0x00    ..lll...
    0008   0x04 0x04 0x03 0x74 0x56 0x00 0x90 0x0e    ...tV...
    0010   0x00 0x30 0x00 0x90 0x0e 0x00 0x90 0x64    .0.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  108  108  108    1    0    0
              4    4    3  116   86    0  144   14
              0   48    0  144   14    0  144  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2013-05-25T21:01:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-05-25T21:01:02)
    0000   0x42 0x41 0x35 0x19 0x0d                   BA5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 2 BolusWizard 2013-05-25T21:01:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-05-25T21:01:04)
    0000   0x44 0x41 0x15 0x19 0x0d                   DA...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125
    HOUR BITS: [0, 1, 0]
#### RECORD 3 Bolus 2013-05-25T21:01:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-05-25T21:01:04)
    0000   0x44 0x41 0x55 0x19 0x0d                   DAU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 PumpSuspend 2013-05-25T21:09:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-25T21:09:57)
    0000   0x79 0x49 0x15 0x19 0x0d                   yI...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 5 PumpResume 2013-05-25T21:19:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-25T21:19:02)
    0000   0x42 0x53 0x15 0x19 0x0d                   BS...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 CalBGForPH 2013-05-25T22:00:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-05-25T22:00:09)
    0000   0x49 0x40 0x36 0x19 0x0d                   I@6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-05-25T22:00:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-05-25T22:00:17)
    0000   0x51 0x40 0x36 0x19 0x0d                   Q@6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 8 MResultTotals 2013-05-26T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xb6                   .....
    decimal
              7    0    0    3  182
    datetime (2013-05-26T00:00:00)
    0000   0x59 0x8d                                  Y.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 9 Model522ResultTotals 2013-05-26T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-26T00:00:00)
    0000   0x59 0x8d                                  Y.
    body (41)
    hex
    0000   0x05 0x00 0x83 0x66 0xbe 0x03 0x00 0x00    ...f....
    0008   0x03 0xb6 0x03 0x7e 0x5e 0x00 0x38 0x06    ...~^.8.
    0010   0x00 0x00 0x00 0x38 0x06 0x00 0x00 0x00    ...8....
    0018   0x00 0x38 0x64 0x00 0x00 0x00 0x01 0x00    .8d.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  131  102  190    3    0    0
              3  182    3  126   94    0   56    6
              0    0    0   56    6    0    0    0
              0   56  100    0    0    0    1    0
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 10 CalBGForPH 2013-05-26T04:05:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 261}
```
    op hex (2)
    0000   0x0a 0x05                                  ..
    decimal
             10    5
    datetime (2013-05-26T04:05:04)
    0000   0x44 0x45 0x24 0x1a 0x8d                   DE$..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 11 BolusWizard 2013-05-26T04:05:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 261,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x05                                  [.
    decimal
             91    5
    datetime (2013-05-26T04:05:08)
    0000   0x48 0x45 0x04 0x1a 0x0d                   HE...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1e 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
              0   81   13   45  106   30    0    0
              0    0    0   30  125
    HOUR BITS: [0, 1, 0]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 175, 'amount': 1.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0xaf 0x14                   \.8..
    decimal
             92    5   56  175   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-05-26T04:05:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-05-26T04:05:08)
    0000   0x48 0x45 0x44 0x1a 0x0d                   HED..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 14 LowReservoir 2013-05-26T04:30:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-26T04:30:00)
    0000   0x40 0x5e 0x04 0x1a 0x0d                   @^...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 15 LowReservoir 2013-05-26T14:37:53 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-05-26T14:37:53)
    0000   0x75 0x65 0x0e 0x1a 0x0d                   ue...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 16 CalBGForPH 2013-05-26T15:26:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-05-26T15:26:37)
    0000   0x65 0x5a 0x2f 0x1a 0x0d                   eZ/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 17 BolusWizard 2013-05-26T15:26:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 101,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x65                                  [e
    decimal
             91  101
    datetime (2013-05-26T15:26:46)
    0000   0x6e 0x5a 0x0f 0x1a 0x0d                   nZ...
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0xff 0x13 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             25   80   13   45  106  255   19  240
              0    0    0   18  125
    HOUR BITS: [0, 1, 0]
#### RECORD 18 Bolus 2013-05-26T15:26:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-05-26T15:26:46)
    0000   0x6e 0x5a 0x4f 0x1a 0x0d                   nZO..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 19 CalBGForPH 2013-05-26T20:49:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 179}
```
    op hex (2)
    0000   0x0a 0xb3                                  ..
    decimal
             10  179
    datetime (2013-05-26T20:49:44)
    0000   0x6c 0x71 0x34 0x1a 0x0d                   lq4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2013-05-26T20:49:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 179,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
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
    0000   0x5b 0xb3                                  [.
    decimal
             91  179
    datetime (2013-05-26T20:49:46)
    0000   0x6e 0x71 0x14 0x1a 0x0d                   nq...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    0    0   12  125
    HOUR BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 1.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x48 0x45 0x14                   \.HE.
    decimal
             92    5   72   69   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-05-26T20:49:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-05-26T20:49:46)
    0000   0x6e 0x71 0x54 0x1a 0x0d                   nqT..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 Rewind 2013-05-26T20:57:02 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-05-26T20:57:02)
    0000   0x42 0x79 0x14 0x1a 0x0d                   By...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 24 Prime 2013-05-26T20:58:46 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x19                   .....
    decimal
              3    0    0    0   25
    datetime (2013-05-26T20:58:46)
    0000   0x6e 0x7a 0x34 0x1a 0x0d                   nz4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 25 Prime 2013-05-26T20:59:13 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-05-26T20:59:13)
    0000   0x4d 0x7b 0x14 0x1a 0x0d                   M{...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 26 CalBGForPH 2013-05-26T22:08:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-05-26T22:08:12)
    0000   0x4c 0x48 0x36 0x1a 0x0d                   LH6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 27 CalBGForPH 2013-05-26T22:09:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-05-26T22:09:17)
    0000   0x51 0x49 0x36 0x1a 0x0d                   QI6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 28 BolusWizard 2013-05-26T22:09:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 116,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2013-05-26T22:09:36)
    0000   0x64 0x49 0x16 0x1a 0x0d                   dI...
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x00 0x21 0x00    +P.-j.!.
    0008   0x00 0x09 0x00 0x21 0x7d                   ...!}
    decimal
             43   80   13   45  106    0   33    0
              0    9    0   33  125
    HOUR BITS: [0, 1, 0]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 1.2, 'curve': 4},
 {'age': 149, 'amount': 1.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x55 0x04 0x48 0x95 0x14    \.0U.H..
    decimal
             92    8   48   85    4   72  149   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-05-26T22:09:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-05-26T22:09:36)
    0000   0x64 0x49 0x56 0x1a 0x0d                   dIV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 31 MResultTotals 2013-05-27T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xfc                   .....
    decimal
              7    0    0    4  252
    datetime (2013-05-27T00:00:00)
    0000   0x5a 0x8d                                  Z.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 Model522ResultTotals 2013-05-27T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-27T00:00:00)
    0000   0x5a 0x8d                                  Z.
    body (41)
    hex
    0000   0x05 0x10 0x9a 0x65 0x05 0x05 0x00 0x00    ...e....
    0008   0x04 0xfc 0x03 0x84 0x47 0x01 0x78 0x1d    ....G.x.
    0010   0x00 0x44 0x01 0x78 0x1d 0x00 0xcc 0x36    .D.x...6
    0018   0x00 0xac 0x2e 0x00 0x00 0x00 0x04 0x02    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  154  101    5    5    0    0
              4  252    3  132   71    1  120   29
              0   68    1  120   29    0  204   54
              0  172   46    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 33 CalBGForPH 2013-05-27T10:21:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 319}
```
    op hex (2)
    0000   0x0a 0x3f                                  .?
    decimal
             10   63
    datetime (2013-05-27T10:21:26)
    0000   0x5a 0x55 0x2a 0x1b 0x8d                   ZU*..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 BolusWizard 2013-05-27T10:21:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 43,
 '_byte[7]': 0,
 'bg': 319,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
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
    0000   0x5b 0x3f                                  [?
    decimal
             91   63
    datetime (2013-05-27T10:21:31)
    0000   0x5f 0x55 0x0a 0x1b 0x0d                   _U...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2b 0x00 0x00    .Q.-j+..
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
              0   81   13   45  106   43    0    0
              0    0    0   43  125
    HOUR BITS: [0, 1, 0]
#### RECORD 35 Bolus 2013-05-27T10:21:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-05-27T10:21:31)
    0000   0x5f 0x55 0x4a 0x1b 0x0d                   _UJ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 36 PumpSuspend 2013-05-27T18:33:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-27T18:33:39)
    0000   0x67 0x61 0x12 0x1b 0x0d                   ga...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 37 PumpResume 2013-05-27T19:30:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-27T19:30:04)
    0000   0x44 0x5e 0x13 0x1b 0x0d                   D^...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 CalBGForPH 2013-05-27T19:55:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-05-27T19:55:29)
    0000   0x5d 0x77 0x33 0x1b 0x0d                   ]w3..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 39 BolusWizard 2013-05-27T19:55:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
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
    0000   0x5b 0x89                                  [.
    decimal
             91  137
    datetime (2013-05-27T19:55:32)
    0000   0x60 0x77 0x13 0x1b 0x0d                   `w...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x02 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x02 0x7d                   ....}
    decimal
              0   80   13   45  106    2    0    0
              0    0    0    2  125
    HOUR BITS: [0, 1, 1]
#### RECORD 40 Bolus 2013-05-27T19:55:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-05-27T19:55:32)
    0000   0x60 0x77 0x53 0x1b 0x0d                   `wS..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 41 BolusWizard 2013-05-27T20:18:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.4,
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
    datetime (2013-05-27T20:18:56)
    0000   0x78 0x52 0x14 0x1b 0x0d                   xR...
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x00 0x18 0x00     P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
             32   80   13   45  106    0   24    0
              0    0    0   24  125
    HOUR BITS: [0, 1, 0]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 0.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x08 0x18 0x04                   \....
    decimal
             92    5    8   24    4
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-05-27T20:18:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-05-27T20:18:56)
    0000   0x78 0x52 0x54 0x1b 0x0d                   xRT..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 44 CalBGForPH 2013-05-27T21:02:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 323}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2013-05-27T21:02:03)
    0000   0x43 0x42 0x35 0x1b 0x8d                   CB5..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 45 BolusWizard 2013-05-27T21:02:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 44,
 '_byte[7]': 0,
 'bg': 323,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x43                                  [C
    decimal
             91   67
    datetime (2013-05-27T21:02:11)
    0000   0x4b 0x42 0x15 0x1b 0x0d                   KB...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2c 0x00 0x00    .Q.-j,..
    0008   0x00 0x17 0x00 0x15 0x7d                   ....}
    decimal
              0   81   13   45  106   44    0    0
              0   23    0   21  125
    HOUR BITS: [0, 1, 0]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.4, 'curve': 4},
 {'age': 68, 'amount': 0.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x60 0x30 0x04 0x08 0x44 0x04    \.`0..D.
    decimal
             92    8   96   48    4    8   68    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-05-27T21:02:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-05-27T21:02:12)
    0000   0x4c 0x42 0x55 0x1b 0x0d                   LBU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 48 CalBGForPH 2013-05-27T22:01:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 264}
```
    op hex (2)
    0000   0x0a 0x08                                  ..
    decimal
             10    8
    datetime (2013-05-27T22:01:19)
    0000   0x53 0x41 0x36 0x1b 0x8d                   SA6..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 BolusWizard 2013-05-27T22:17:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.8,
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
    datetime (2013-05-27T22:17:23)
    0000   0x57 0x51 0x16 0x1b 0x0d                   WQ...
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x00 0x1c 0x00    %P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106    0   28    0
              0    0    0   28  125
    HOUR BITS: [0, 1, 0]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 83, 'amount': 2.4, 'curve': 4},
 {'age': 123, 'amount': 2.4, 'curve': 4},
 {'age': 143, 'amount': 0.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x60 0x53 0x04 0x60 0x7b 0x04    \.`S.`{.
    0008   0x08 0x8f 0x04                             ...
    decimal
             92   11   96   83    4   96  123    4
              8  143    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-05-27T22:17:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-05-27T22:17:23)
    0000   0x57 0x51 0x56 0x1b 0x0d                   WQV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 52 MResultTotals 2013-05-28T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x44                   ....D
    decimal
              7    0    0    5   68
    datetime (2013-05-28T00:00:00)
    0000   0x5b 0x8d                                  [.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 Model522ResultTotals 2013-05-28T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-28T00:00:00)
    0000   0x5b 0x8d                                  [.
    body (41)
    hex
    0000   0x05 0x11 0x05 0x89 0x43 0x04 0x00 0x00    ....C...
    0008   0x05 0x44 0x03 0x60 0x40 0x01 0xe4 0x24    .D.`@..$
    0010   0x00 0x45 0x01 0xe4 0x24 0x00 0xd0 0x2b    .E..$..+
    0018   0x01 0x14 0x39 0x00 0x00 0x00 0x05 0x02    ..9.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   17    5  137   67    4    0    0
              5   68    3   96   64    1  228   36
              0   69    1  228   36    0  208   43
              1   20   57    0    0    0    5    2
              3    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 54 PumpSuspend 2013-05-28T14:40:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-28T14:40:55)
    0000   0x77 0x68 0x0e 0x1c 0x0d                   wh...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 55 PumpResume 2013-05-28T15:29:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-28T15:29:03)
    0000   0x43 0x5d 0x0f 0x1c 0x0d                   C]...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 56 CalBGForPH 2013-05-28T15:38:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-05-28T15:38:38)
    0000   0x66 0x66 0x2f 0x1c 0x0d                   ff/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2013-05-28T15:38:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 128,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-05-28T15:38:49)
    0000   0x71 0x66 0x0f 0x1c 0x0d                   qf...
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x00 0x1c 0x00    %P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106    0   28    0
              0    0    0   28  125
    HOUR BITS: [0, 1, 1]
#### RECORD 58 Bolus 2013-05-28T15:38:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2013-05-28T15:38:49)
    0000   0x71 0x66 0x4f 0x1c 0x0d                   qfO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 59 CalBGForPH 2013-05-28T18:57:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2013-05-28T18:57:10)
    0000   0x4a 0x79 0x32 0x1c 0x0d                   Jy2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 60 BolusWizard 2013-05-28T18:57:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 253,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfd                                  [.
    decimal
             91  253
    datetime (2013-05-28T18:57:12)
    0000   0x4c 0x79 0x12 0x1c 0x0d                   Ly...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x18 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    4    0   24  125
    HOUR BITS: [0, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 203, 'amount': 2.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0xcb 0x04                   \.p..
    decimal
             92    5  112  203    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-05-28T18:57:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-05-28T18:57:12)
    0000   0x4c 0x79 0x52 0x1c 0x0d                   LyR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 63 MResultTotals 2013-05-29T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x34                   ....4
    decimal
              7    0    0    4   52
    datetime (2013-05-29T00:00:00)
    0000   0x5c 0x8d                                  \.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 64 Model522ResultTotals 2013-05-29T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-29T00:00:00)
    0000   0x5c 0x8d                                  \.
    body (41)
    hex
    0000   0x05 0x00 0xbf 0x80 0xfd 0x02 0x00 0x00    ........
    0008   0x04 0x34 0x03 0x64 0x51 0x00 0xd0 0x13    .4.dQ...
    0010   0x00 0x25 0x00 0xd0 0x13 0x00 0x70 0x36    .%....p6
    0018   0x00 0x60 0x2e 0x00 0x00 0x00 0x02 0x01    .`......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  191  128  253    2    0    0
              4   52    3  100   81    0  208   19
              0   37    0  208   19    0  112   54
              0   96   46    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 65 CalBGForPH 2013-05-29T18:07:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 226}
```
    op hex (2)
    0000   0x0a 0xe2                                  ..
    decimal
             10  226
    datetime (2013-05-29T18:07:29)
    0000   0x5d 0x47 0x32 0x1d 0x0d                   ]G2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 66 BolusWizard 2013-05-29T18:07:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 226,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
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
    0000   0x5b 0xe2                                  [.
    decimal
             91  226
    datetime (2013-05-29T18:07:31)
    0000   0x5f 0x47 0x12 0x1d 0x0d                   _G...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    0    0   22  125
    HOUR BITS: [0, 1, 0]
#### RECORD 67 Bolus 2013-05-29T18:07:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-05-29T18:07:31)
    0000   0x5f 0x47 0x52 0x1d 0x0d                   _GR..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 68 CalBGForPH 2013-05-29T20:42:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 168}
```
    op hex (2)
    0000   0x0a 0xa8                                  ..
    decimal
             10  168
    datetime (2013-05-29T20:42:29)
    0000   0x5d 0x6a 0x34 0x1d 0x0d                   ]j4..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 69 BolusWizard 2013-05-29T20:42:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 168,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa8                                  [.
    decimal
             91  168
    datetime (2013-05-29T20:42:33)
    0000   0x61 0x6a 0x14 0x1d 0x0d                   aj...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x09 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106    9    0    0
              0    6    0    3  125
    HOUR BITS: [0, 1, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 158, 'amount': 2.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x9e 0x04                   \.X..
    decimal
             92    5   88  158    4
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-05-29T20:42:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'dual_component': '??', 'programmed': 0.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2013-05-29T20:42:33)
    0000   0x61 0x6a 0x54 0x1d 0x0d                   ajT..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 72 CalBGForPH 2013-05-29T21:14:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-05-29T21:14:57)
    0000   0x79 0x4e 0x35 0x1d 0x0d                   yN5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 73 BolusWizard 2013-05-29T21:15:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 172,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2013-05-29T21:15:00)
    0000   0x40 0x4f 0x15 0x1d 0x0d                   @O...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    6    0    4  125
    HOUR BITS: [0, 1, 0]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 0.3, 'curve': 4},
 {'age': 191, 'amount': 2.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x0c 0x29 0x04 0x58 0xbf 0x04    \..).X..
    decimal
             92    8   12   41    4   88  191    4
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2013-05-29T21:15:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-05-29T21:15:00)
    0000   0x40 0x4f 0x55 0x1d 0x0d                   @OU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 76 CalBGForPH 2013-05-29T21:44:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 178}
```
    op hex (2)
    0000   0x0a 0xb2                                  ..
    decimal
             10  178
    datetime (2013-05-29T21:44:19)
    0000   0x53 0x6c 0x35 0x1d 0x0d                   Sl5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 77 CalBGForPH 2013-05-29T21:44:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 178}
```
    op hex (2)
    0000   0x0a 0xb2                                  ..
    decimal
             10  178
    datetime (2013-05-29T21:44:56)
    0000   0x78 0x6c 0x35 0x1d 0x0d                   xl5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 78 BolusWizard 2013-05-29T21:45:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 178,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.9,
 'carb_input': 74,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 5.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb2                                  [.
    decimal
             91  178
    datetime (2013-05-29T21:45:33)
    0000   0x61 0x6d 0x15 0x1d 0x0d                   am...
    body (13)
    hex
    0000   0x4a 0x50 0x0d 0x2d 0x6a 0x0b 0x38 0x00    JP.-j.8.
    0008   0x00 0x08 0x00 0x3b 0x7d                   ...;}
    decimal
             74   80   13   45  106   11   56    0
              0    8    0   59  125
    HOUR BITS: [0, 1, 1]
#### RECORD 79 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 0.4, 'curve': 4},
 {'age': 71, 'amount': 0.3, 'curve': 4},
 {'age': 221, 'amount': 2.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0x1f 0x04 0x0c 0x47 0x04    \.....G.
    0008   0x58 0xdd 0x04                             X..
    decimal
             92   11   16   31    4   12   71    4
             88  221    4
    datetime (unknown)

    body (0)

#### RECORD 80 Bolus 2013-05-29T21:45:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.9, 'dual_component': '??', 'programmed': 5.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3b 0x3b 0x00                        .;;.
    decimal
              1   59   59    0
    datetime (2013-05-29T21:45:33)
    0000   0x61 0x6d 0x55 0x1d 0x0d                   amU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 81 BolusWizard 2013-05-29T22:48:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
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
    datetime (2013-05-29T22:48:04)
    0000   0x44 0x70 0x16 0x1d 0x0d                   Dp...
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-16.data: 82 records`
