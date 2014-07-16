## START m522-ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 718, found 304 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x0c 0xda                                  ..
##### DEBUG DECIMAL
             12  218
#### RECORD 0 Ian3F 2014-07-13T22:05:46 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2014-07-13T22:05:46)
    0000   0x6e 0xc5 0x36 0x6d 0x0e                   n.6m.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 PumpResume 2014-07-13T23:12:42 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-07-13T23:12:42)
    0000   0x6a 0xcc 0x17 0x0d 0x0e                   j....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BolusWizard 2014-07-13T23:13:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.9,
 'carb_input': 90,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 6.9,
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
    datetime (2014-07-13T23:13:08)
    0000   0x48 0xcd 0x17 0x0d 0x0e                   H....
    body (13)
    hex
    0000   0x5a 0x50 0x0d 0x2d 0x6a 0x00 0x45 0x00    ZP.-j.E.
    0008   0x00 0x00 0x00 0x45 0x7d                   ...E}
    decimal
             90   80   13   45  106    0   69    0
              0    0    0   69  125
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Bolus 2014-07-13T23:13:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'duration': 0, 'programmed': 4.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2014-07-13T23:13:09)
    0000   0x49 0xcd 0x97 0x0d 0x0e                   I....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 MResultTotals 2014-07-14T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x80                   .....
    decimal
              7    0    0    4  128
    datetime (2014-07-14T00:00:00)
    0000   0x6d 0x8e                                  m.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 Model522ResultTotals 2014-07-14T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-14T00:00:00)
    0000   0x6d 0x8e                                  m.
    body (41)
    hex
    0000   0x05 0x00 0x48 0x31 0x5f 0x02 0x00 0x00    ..H1_...
    0008   0x04 0x80 0x03 0x42 0x48 0x01 0x3e 0x1c    ...BH.>.
    0010   0x00 0x5a 0x01 0x3e 0x1c 0x01 0x3e 0x64    .Z.>..>d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   72   49   95    2    0    0
              4  128    3   66   72    1   62   28
              0   90    1   62   28    1   62  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 6 Bolus 2014-07-13T23:15:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'duration': 90, 'programmed': 2.7, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x03                        ....
    decimal
              1   27   27    3
    datetime (2014-07-13T23:15:57)
    0000   0x79 0xcf 0xb7 0x0d 0x0e                   y....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 LowReservoir 2014-07-14T21:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-07-14T21:41:03)
    0000   0x43 0xe9 0x15 0x0e 0x0e                   C....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 CalBGForPH 2014-07-14T22:30:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 55}
```
    op hex (2)
    0000   0x0a 0x37                                  .7
    decimal
             10   55
    datetime (2014-07-14T22:30:00)
    0000   0x40 0xde 0x36 0x6e 0x0e                   @.6n.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 Ian3F 2014-07-14T22:30:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2014-07-14T22:30:00)
    0000   0x40 0xde 0xf6 0x6e 0x0e                   @..n.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 PumpSuspend 2014-07-14T23:51:36 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-07-14T23:51:36)
    0000   0x64 0xf3 0x17 0x4e 0x0e                   d..N.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 11 MResultTotals 2014-07-15T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xb8                   .....
    decimal
              7    0    0    3  184
    datetime (2014-07-15T00:00:00)
    0000   0x6e 0x8e                                  n.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 12 Model522ResultTotals 2014-07-15T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-15T00:00:00)
    0000   0x6e 0x8e                                  n.
    body (41)
    hex
    0000   0x05 0x00 0x37 0x37 0x37 0x01 0x00 0x00    ..777...
    0008   0x03 0xb8 0x03 0x80 0x5e 0x00 0x38 0x06    ....^.8.
    0010   0x00 0x00 0x00 0x38 0x06 0x00 0x38 0x64    ...8..8d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   55   55   55    1    0    0
              3  184    3  128   94    0   56    6
              0    0    0   56    6    0   56  100
              0    0    0    0    0    0    0    0
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 13 PumpResume 2014-07-15T00:03:52 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-07-15T00:03:52)
    0000   0x74 0xc3 0x00 0x4f 0x0e                   t..O.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 14 BolusWizard 2014-07-15T01:38:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 62,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.7,
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
    datetime (2014-07-15T01:38:09)
    0000   0x49 0xe6 0x01 0x0f 0x0e                   I....
    body (13)
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x00 0x2f 0x00    >P.-j./.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             62   80   13   45  106    0   47    0
              0    0    0   47  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 Bolus 2014-07-15T01:38:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'duration': 0, 'programmed': 3.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2014-07-15T01:38:09)
    0000   0x49 0xe6 0x81 0x0f 0x0e                   I....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 16 Bolus 2014-07-15T01:40:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'duration': 60, 'programmed': 1.5, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x02                        ....
    decimal
              1   15   15    2
    datetime (2014-07-15T01:40:16)
    0000   0x50 0xe8 0xa1 0x0f 0x0e                   P....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 LowReservoir 2014-07-15T04:07:30 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-07-15T04:07:30)
    0000   0x5e 0xc7 0x04 0x0f 0x0e                   ^....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 CalBGForPH 2014-07-15T04:11:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 280}
```
    op hex (2)
    0000   0x0a 0x18                                  ..
    decimal
             10   24
    datetime (2014-07-15T04:11:54)
    0000   0x76 0xcb 0x24 0x6f 0x8e                   v.$o.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 19 Ian3F 2014-07-15T04:11:54 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2014-07-15T04:11:54)
    0000   0x76 0xcb 0x04 0x6f 0x0e                   v..o.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2014-07-15T04:14:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 34,
 '_byte[7]': 0,
 'bg': 280,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
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
    0000   0x5b 0x18                                  [.
    decimal
             91   24
    datetime (2014-07-15T04:14:20)
    0000   0x54 0xce 0x04 0x0f 0x0e                   T....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x22 0x00 0x00    .Q.-j"..
    0008   0x00 0x0f 0x00 0x13 0x7d                   ....}
    decimal
              0   81   13   45  106   34    0    0
              0   15    0   19  125
    HOUR BITS: [1, 1, 0]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 0.15, 'curve': 4},
 {'age': 110, 'amount': 0.25, 'curve': 4},
 {'age': 120, 'amount': 0.25, 'curve': 4},
 {'age': 130, 'amount': 0.25, 'curve': 4},
 {'age': 140, 'amount': 0.25, 'curve': 4},
 {'age': 150, 'amount': 0.25, 'curve': 4},
 {'age': 160, 'amount': 3.3, 'curve': 4}]
```
    op hex (23)
    0000   0x5c 0x17 0x06 0x64 0x04 0x0a 0x6e 0x04    \..d..n.
    0008   0x0a 0x78 0x04 0x0a 0x82 0x04 0x0a 0x8c    .x......
    0010   0x04 0x0a 0x96 0x04 0x84 0xa0 0x04         .......
    decimal
             92   23    6  100    4   10  110    4
             10  120    4   10  130    4   10  140
              4   10  150    4  132  160    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2014-07-15T04:14:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'duration': 0, 'programmed': 1.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2014-07-15T04:14:20)
    0000   0x54 0xce 0x44 0x0f 0x0e                   T.D..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 MResultTotals 2014-07-16T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x88                   .....
    decimal
              7    0    0    4  136
    datetime (2014-07-16T00:00:00)
    0000   0x6f 0x8e                                  o.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 Model522ResultTotals 2014-07-16T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-16T00:00:00)
    0000   0x6f 0x8e                                  o.
    body (41)
    hex
    0000   0x05 0x15 0x18 0x18 0x18 0x01 0x00 0x00    ........
    0008   0x04 0x88 0x03 0x80 0x4d 0x01 0x08 0x17    ....M...
    0010   0x00 0x3e 0x01 0x08 0x17 0x00 0xbc 0x47    .>.....G
    0018   0x00 0x4c 0x1d 0x00 0x00 0x00 0x02 0x01    .L......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21   24   24   24    1    0    0
              4  136    3  128   77    1    8   23
              0   62    1    8   23    0  188   71
              0   76   29    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 25 Rewind 2014-07-16T00:01:24 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-07-16T00:01:24)
    0000   0x58 0xc1 0x00 0x10 0x0e                   X....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 26 Prime 2014-07-16T00:03:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x18                   .....
    decimal
              3    0    0    0   24
    datetime (2014-07-16T00:03:30)
    0000   0x5e 0xc3 0x20 0x10 0x0e                   ^. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 Prime 2014-07-16T00:03:52 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2014-07-16T00:03:52)
    0000   0x74 0xc3 0x00 0x10 0x0e                   t....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 CalBGForPH 2014-07-16T00:10:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2014-07-16T00:10:24)
    0000   0x58 0xca 0x20 0x70 0x0e                   X. p.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 Ian3F 2014-07-16T00:10:24 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-07-16T00:10:24)
    0000   0x58 0xca 0x60 0x70 0x0e                   X.`p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 BolusWizard 2014-07-16T00:10:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 10,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2014-07-16T00:10:33)
    0000   0x61 0xca 0x00 0x10 0x0e                   a....
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x08 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             10   80   13   45  106    8    7    0
              0    0    0   15  125
    HOUR BITS: [1, 1, 0]
#### RECORD 31 Bolus 2014-07-16T00:10:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'duration': 0, 'programmed': 1.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2014-07-16T00:10:33)
    0000   0x61 0xca 0x40 0x10 0x0e                   a.@..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 32 BolusWizard 2014-07-16T01:26:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 63,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.8,
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
    datetime (2014-07-16T01:26:01)
    0000   0x41 0xda 0x01 0x10 0x0e                   A....
    body (13)
    hex
    0000   0x3f 0x50 0x0d 0x2d 0x6a 0x00 0x30 0x00    ?P.-j.0.
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
             63   80   13   45  106    0   48    0
              0    0    0   48  125
    HOUR BITS: [1, 1, 0]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 1.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x52 0x04                   \.<R.
    decimal
             92    5   60   82    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2014-07-16T01:26:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'duration': 0, 'programmed': 4.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2014-07-16T01:26:02)
    0000   0x42 0xda 0x41 0x10 0x0e                   B.A..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 35 Ian3F 2014-07-16T04:56:32 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x32                                  ?2
    decimal
             63   50
    datetime (2014-07-16T04:56:32)
    0000   0x60 0xf8 0xa4 0x70 0x0e                   `..p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 36 BolusWizard 2014-07-16T04:56:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 62,
 '_byte[7]': 0,
 'bg': 405,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x95                                  [.
    decimal
             91  149
    datetime (2014-07-16T04:56:43)
    0000   0x6b 0xf8 0x04 0x10 0x0e                   k....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3e 0x00 0x00    .Q.-j>..
    0008   0x00 0x05 0x00 0x39 0x7d                   ...9}
    decimal
              0   81   13   45  106   62    0    0
              0    5    0   57  125
    HOUR BITS: [1, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 212, 'amount': 4.8, 'curve': 4},
 {'age': 36, 'amount': 1.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0xd4 0x04 0x3c 0x24 0x14    \....<$.
    decimal
             92    8  192  212    4   60   36   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2014-07-16T04:56:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.7, 'duration': 0, 'programmed': 5.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x39 0x39 0x00                        .99.
    decimal
              1   57   57    0
    datetime (2014-07-16T04:56:43)
    0000   0x6b 0xf8 0x44 0x10 0x0e                   k.D..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 Ian3F 2014-07-16T09:06:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x37                                  ?7
    decimal
             63   55
    datetime (2014-07-16T09:06:04)
    0000   0x44 0xc6 0x89 0x70 0x0e                   D..p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 BolusWizard 2014-07-16T09:06:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 70,
 '_byte[7]': 0,
 'bg': 444,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 7.0,
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
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2014-07-16T09:06:16)
    0000   0x50 0xc6 0x09 0x10 0x0e                   P....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x46 0x00 0x00    .Q.-jF..
    0008   0x00 0x00 0x00 0x46 0x7d                   ...F}
    decimal
              0   81   13   45  106   70    0    0
              0    0    0   70  125
    HOUR BITS: [1, 1, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 252, 'amount': 5.7, 'curve': 4},
 {'age': 206, 'amount': 4.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xe4 0xfc 0x04 0xc0 0xce 0x14    \.......
    decimal
             92    8  228  252    4  192  206   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2014-07-16T09:06:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.2, 'duration': 0, 'programmed': 7.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x48 0x48 0x00                        .HH.
    decimal
              1   72   72    0
    datetime (2014-07-16T09:06:17)
    0000   0x51 0xc6 0x49 0x10 0x0e                   Q.I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 43 TempBasal 2014-07-16T09:11:33 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.25}
```
    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2014-07-16T09:11:33)
    0000   0x61 0xcb 0x09 0x10 0x0e                   a....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 0]
#### RECORD 44 TempBasalDuration 2014-07-16T09:11:33 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2014-07-16T09:11:33)
    0000   0x61 0xcb 0x09 0x10 0x0e                   a....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 BolusWizard 2014-07-16T09:45:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-16T09:45:27)
    0000   0x5b 0xed 0x09 0x10 0x0e                   [....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x00 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106    0    0    0
              0    0    0    0  125
    HOUR BITS: [1, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 0.8, 'curve': 5},
 {'age': 35, 'amount': 5.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x29 0x05 0xe4 0x23 0x14    \. )..#.
    decimal
             92    8   32   41    5  228   35   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2014-07-16T09:45:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'duration': 0, 'programmed': 0.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2014-07-16T09:45:27)
    0000   0x5b 0xed 0x49 0x10 0x0e                   [.I..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 Ian3F 2014-07-16T10:40:46 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x33                                  ?3
    decimal
             63   51
    datetime (2014-07-16T10:40:46)
    0000   0x6e 0xe8 0xea 0x70 0x0e                   n..p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2014-07-16T10:40:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 64,
 '_byte[7]': 0,
 'bg': 415,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 4.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9f                                  [.
    decimal
             91  159
    datetime (2014-07-16T10:40:59)
    0000   0x7b 0xe8 0x0a 0x10 0x0e                   {....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x40 0x00 0x00    .Q.-j@..
    0008   0x00 0x31 0x00 0x0f 0x7d                   .1..}
    decimal
              0   81   13   45  106   64    0    0
              0   49    0   15  125
    HOUR BITS: [1, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 0.6, 'curve': 4},
 {'age': 96, 'amount': 0.8, 'curve': 5},
 {'age': 90, 'amount': 5.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x18 0x38 0x04 0x20 0x60 0x05    \..8. `.
    0008   0xe4 0x5a 0x14                             .Z.
    decimal
             92   11   24   56    4   32   96    5
            228   90   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2014-07-16T10:40:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2014-07-16T10:40:59)
    0000   0x7b 0xe8 0x4a 0x10 0x0e                   {.J..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 BolusWizard 2014-07-16T10:42:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 64,
 '_byte[7]': 0,
 'bg': 415,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 7.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9f                                  [.
    decimal
             91  159
    datetime (2014-07-16T10:42:58)
    0000   0x7a 0xea 0x0a 0x10 0x0e                   z....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x40 0x00 0x00    .Q.-j@..
    0008   0x00 0x4a 0x00 0x00 0x7d                   .J..}
    decimal
              0   81   13   45  106   64    0    0
              0   74    0    0  125
    HOUR BITS: [1, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 2.6, 'curve': 4},
 {'age': 58, 'amount': 0.6, 'curve': 4},
 {'age': 98, 'amount': 0.8, 'curve': 5},
 {'age': 92, 'amount': 5.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0x08 0x04 0x18 0x3a 0x04    \.h...:.
    0008   0x20 0x62 0x05 0xe4 0x5c 0x14               b..\.
    decimal
             92   14  104    8    4   24   58    4
             32   98    5  228   92   20
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2014-07-16T10:42:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2014-07-16T10:42:58)
    0000   0x7a 0xea 0x4a 0x10 0x0e                   z.J..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 55 Ian3F 2014-07-16T12:45:10 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x35                                  ?5
    decimal
             63   53
    datetime (2014-07-16T12:45:10)
    0000   0x4a 0xed 0x2c 0x70 0x0e                   J.,p.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
`end m522-ReadHistoryData-page-0.data: 56 records`
## START m522-ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x05 0xff                                  ..
##### DEBUG DECIMAL
              5  255
#### RECORD 0 Ian3F 2014-07-06T22:05:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2014-07-06T22:05:43)
    0000   0x6b 0xc5 0x96 0x66 0x0e                   k..f.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 CalBGForPH 2014-07-06T22:48:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2014-07-06T22:48:09)
    0000   0x49 0xf0 0x36 0x66 0x0e                   I.6f.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2014-07-06T22:48:09 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2014-07-06T22:48:09)
    0000   0x49 0xf0 0x56 0x66 0x0e                   I.Vf.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2014-07-06T22:49:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 98,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.5,
 'carb_input': 88,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 6.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2014-07-06T22:49:10)
    0000   0x4a 0xf1 0x16 0x06 0x0e                   J....
    body (13)
    hex
    0000   0x58 0x50 0x0d 0x2d 0x6a 0xfe 0x43 0xf0    XP.-j.C.
    0008   0x00 0x00 0x00 0x41 0x7d                   ...A}
    decimal
             88   80   13   45  106  254   67  240
              0    0    0   65  125
    HOUR BITS: [1, 1, 1]
#### RECORD 4 Bolus 2014-07-06T22:49:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'duration': 0, 'programmed': 4.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2014-07-06T22:49:10)
    0000   0x4a 0xf1 0x96 0x06 0x0e                   J....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 MResultTotals 2014-07-07T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x82                   .....
    decimal
              7    0    0    4  130
    datetime (2014-07-07T00:00:00)
    0000   0x66 0x8e                                  f.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 Model522ResultTotals 2014-07-07T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-07T00:00:00)
    0000   0x66 0x8e                                  f.
    body (41)
    hex
    0000   0x05 0x00 0x5b 0x54 0x62 0x02 0x00 0x00    ..[Tb...
    0008   0x04 0x82 0x03 0x70 0x4c 0x01 0x12 0x18    ...pL...
    0010   0x00 0x58 0x01 0x12 0x18 0x01 0x12 0x64    .X.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   91   84   98    2    0    0
              4  130    3  112   76    1   18   24
              0   88    1   18   24    1   18  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 7 Bolus 2014-07-06T22:51:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'duration': 90, 'programmed': 2.3, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x03                        ....
    decimal
              1   23   23    3
    datetime (2014-07-06T22:51:58)
    0000   0x7a 0xf3 0xb6 0x06 0x0e                   z....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 CalBGForPH 2014-07-07T22:14:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 316}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2014-07-07T22:14:33)
    0000   0x61 0xce 0x36 0x67 0x8e                   a.6g.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 Ian3F 2014-07-07T22:14:33 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x27                                  ?'
    decimal
             63   39
    datetime (2014-07-07T22:14:33)
    0000   0x61 0xce 0x96 0x67 0x0e                   a..g.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 BolusWizard 2014-07-07T22:14:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 42,
 '_byte[7]': 0,
 'bg': 316,
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
    0000   0x5b 0x3c                                  [<
    decimal
             91   60
    datetime (2014-07-07T22:14:50)
    0000   0x72 0xce 0x16 0x07 0x0e                   r....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2a 0x00 0x00    .Q.-j*..
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
              0   81   13   45  106   42    0    0
              0    0    0   42  125
    HOUR BITS: [1, 1, 0]
#### RECORD 11 Bolus 2014-07-07T22:14:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'duration': 0, 'programmed': 4.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2014-07-07T22:14:50)
    0000   0x72 0xce 0x56 0x07 0x0e                   r.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2014-07-07T22:46:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 280}
```
    op hex (2)
    0000   0x0a 0x18                                  ..
    decimal
             10   24
    datetime (2014-07-07T22:46:27)
    0000   0x5b 0xee 0x36 0x67 0x8e                   [.6g.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 13 Ian3F 2014-07-07T22:46:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2014-07-07T22:46:27)
    0000   0x5b 0xee 0x16 0x67 0x0e                   [..g.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 BolusWizard 2014-07-07T22:47:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 34,
 '_byte[7]': 0,
 'bg': 280,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 4.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x18                                  [.
    decimal
             91   24
    datetime (2014-07-07T22:47:07)
    0000   0x47 0xef 0x16 0x07 0x0e                   G....
    body (13)
    hex
    0000   0x45 0x51 0x0d 0x2d 0x6a 0x22 0x35 0x00    EQ.-j"5.
    0008   0x00 0x2d 0x00 0x35 0x7d                   .-.5}
    decimal
             69   81   13   45  106   34   53    0
              0   45    0   53  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 4.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xbc 0x21 0x04                   \..!.
    decimal
             92    5  188   33    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2014-07-07T22:47:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2014-07-07T22:47:07)
    0000   0x47 0xef 0x96 0x07 0x0e                   G....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 MResultTotals 2014-07-08T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x1a                   .....
    decimal
              7    0    0    5   26
    datetime (2014-07-08T00:00:00)
    0000   0x67 0x8e                                  g.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 18 Model522ResultTotals 2014-07-08T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-08T00:00:00)
    0000   0x67 0x8e                                  g.
    body (41)
    hex
    0000   0x05 0x15 0x2a 0x18 0x3c 0x02 0x00 0x00    ..*.<...
    0008   0x05 0x1a 0x03 0x84 0x45 0x01 0x96 0x1f    ....E...
    0010   0x00 0x45 0x01 0x96 0x1f 0x00 0xda 0x36    .E.....6
    0018   0x00 0xbc 0x2e 0x00 0x00 0x00 0x02 0x01    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21   42   24   60    2    0    0
              5   26    3  132   69    1  150   31
              0   69    1  150   31    0  218   54
              0  188   46    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 19 Bolus 2014-07-07T22:49:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'duration': 90, 'programmed': 1.9, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x03                        ....
    decimal
              1   19   19    3
    datetime (2014-07-07T22:49:23)
    0000   0x57 0xf1 0xb6 0x07 0x0e                   W....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 CalBGForPH 2014-07-08T23:36:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 57}
```
    op hex (2)
    0000   0x0a 0x39                                  .9
    decimal
             10   57
    datetime (2014-07-08T23:36:33)
    0000   0x61 0xe4 0x37 0x68 0x0e                   a.7h.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 Ian3F 2014-07-08T23:36:33 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-07-08T23:36:33)
    0000   0x61 0xe4 0x37 0x68 0x0e                   a.7h.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 MResultTotals 2014-07-09T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x94                   .....
    decimal
              7    0    0    3  148
    datetime (2014-07-09T00:00:00)
    0000   0x68 0x8e                                  h.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 Model522ResultTotals 2014-07-09T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-09T00:00:00)
    0000   0x68 0x8e                                  h.
    body (41)
    hex
    0000   0x05 0x00 0x39 0x39 0x39 0x01 0x00 0x00    ..999...
    0008   0x03 0x94 0x03 0x84 0x62 0x00 0x10 0x02    ....b...
    0010   0x00 0x00 0x00 0x10 0x02 0x00 0x10 0x64    .......d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   57   57   57    1    0    0
              3  148    3  132   98    0   16    2
              0    0    0   16    2    0   16  100
              0    0    0    0    0    0    0    0
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 24 CalBGForPH 2014-07-09T01:01:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2014-07-09T01:01:48)
    0000   0x70 0xc1 0x21 0x09 0x0e                   p.!..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BolusWizard 2014-07-09T01:02:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.9,
 'carb_input': 77,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2014-07-09T01:02:15)
    0000   0x4f 0xc2 0x01 0x09 0x0e                   O....
    body (13)
    hex
    0000   0x4d 0x50 0x0d 0x2d 0x6a 0x00 0x3b 0x00    MP.-j.;.
    0008   0x00 0x00 0x00 0x3b 0x7d                   ...;}
    decimal
             77   80   13   45  106    0   59    0
              0    0    0   59  125
    HOUR BITS: [1, 1, 0]
#### RECORD 26 Bolus 2014-07-09T01:02:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2014-07-09T01:02:16)
    0000   0x50 0xc2 0x81 0x09 0x0e                   P....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 Bolus 2014-07-09T01:04:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'duration': 120, 'programmed': 2.5, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x04                        ....
    decimal
              1   25   25    4
    datetime (2014-07-09T01:04:32)
    0000   0x60 0xc4 0xa1 0x09 0x0e                   `....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 LowReservoir 2014-07-09T12:10:54 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-07-09T12:10:54)
    0000   0x76 0xca 0x0c 0x09 0x0e                   v....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 29 PumpSuspend 2014-07-09T21:57:42 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-07-09T21:57:42)
    0000   0x6a 0xf9 0x15 0x09 0x0e                   j....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 PumpResume 2014-07-09T22:56:54 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-07-09T22:56:54)
    0000   0x76 0xf8 0x16 0x09 0x0e                   v....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 BolusWizard 2014-07-09T22:57:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.6,
 'carb_input': 86,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 6.6,
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
    datetime (2014-07-09T22:57:40)
    0000   0x68 0xf9 0x16 0x09 0x0e                   h....
    body (13)
    hex
    0000   0x56 0x50 0x0d 0x2d 0x6a 0x00 0x42 0x00    VP.-j.B.
    0008   0x00 0x00 0x00 0x42 0x7d                   ...B}
    decimal
             86   80   13   45  106    0   66    0
              0    0    0   66  125
    HOUR BITS: [1, 1, 1]
#### RECORD 32 LowReservoir 2014-07-09T22:57:56 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-07-09T22:57:56)
    0000   0x78 0xf9 0x16 0x09 0x0e                   x....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 Bolus 2014-07-09T22:57:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'duration': 0, 'programmed': 4.3, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2014-07-09T22:57:40)
    0000   0x68 0xf9 0x96 0x09 0x0e                   h....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 MResultTotals 2014-07-10T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x32                   ....2
    decimal
              7    0    0    5   50
    datetime (2014-07-10T00:00:00)
    0000   0x69 0x8e                                  i.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 Model522ResultTotals 2014-07-10T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-10T00:00:00)
    0000   0x69 0x8e                                  i.
    body (41)
    hex
    0000   0x05 0x00 0x6b 0x6b 0x6b 0x01 0x00 0x00    ..kkk...
    0008   0x05 0x32 0x03 0x5e 0x41 0x01 0xd4 0x23    .2.^A..#
    0010   0x00 0xa3 0x01 0xd4 0x23 0x01 0xd4 0x64    ....#..d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  107  107  107    1    0    0
              5   50    3   94   65    1  212   35
              0  163    1  212   35    1  212  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 36 Bolus 2014-07-09T23:00:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'duration': 90, 'programmed': 2.3, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x03                        ....
    decimal
              1   23   23    3
    datetime (2014-07-09T23:00:32)
    0000   0x60 0xc0 0xb7 0x09 0x0e                   `....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 PumpSuspend 2014-07-10T19:22:52 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-07-10T19:22:52)
    0000   0x74 0xd6 0x13 0x0a 0x0e                   t....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 38 PumpResume 2014-07-10T19:43:34 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-07-10T19:43:34)
    0000   0x62 0xeb 0x13 0x0a 0x0e                   b....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 Rewind 2014-07-10T19:43:41 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-07-10T19:43:41)
    0000   0x69 0xeb 0x13 0x0a 0x0e                   i....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 Prime 2014-07-10T19:44:21 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2e                   .....
    decimal
              3    0    0    0   46
    datetime (2014-07-10T19:44:21)
    0000   0x55 0xec 0x33 0x0a 0x0e                   U.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 Prime 2014-07-10T19:44:43 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2014-07-10T19:44:43)
    0000   0x6b 0xec 0x13 0x0a 0x0e                   k....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 BolusWizard 2014-07-10T21:01:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 54,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.1,
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
    datetime (2014-07-10T21:01:13)
    0000   0x4d 0xc1 0x15 0x0a 0x0e                   M....
    body (13)
    hex
    0000   0x36 0x50 0x0d 0x2d 0x6a 0x00 0x29 0x00    6P.-j.).
    0008   0x00 0x00 0x00 0x29 0x7d                   ...)}
    decimal
             54   80   13   45  106    0   41    0
              0    0    0   41  125
    HOUR BITS: [1, 1, 0]
#### RECORD 43 Bolus 2014-07-10T21:01:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'duration': 0, 'programmed': 4.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2014-07-10T21:01:13)
    0000   0x4d 0xc1 0x55 0x0a 0x0e                   M.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 44 MResultTotals 2014-07-11T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x3a                   ....:
    decimal
              7    0    0    4   58
    datetime (2014-07-11T00:00:00)
    0000   0x6a 0x8e                                  j.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 45 Model522ResultTotals 2014-07-11T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-11T00:00:00)
    0000   0x6a 0x8e                                  j.
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x04 0x3a 0x03 0x76 0x52 0x00 0xc4 0x12    .:.vR...
    0010   0x00 0x36 0x00 0xc4 0x12 0x00 0xc4 0x64    .6.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              4   58    3  118   82    0  196   18
              0   54    0  196   18    0  196  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 46 CalBGForPH 2014-07-11T01:55:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2014-07-11T01:55:01)
    0000   0x41 0xf7 0x21 0x6b 0x0e                   A.!k.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 Ian3F 2014-07-11T01:55:01 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-07-11T01:55:01)
    0000   0x41 0xf7 0x21 0x6b 0x0e                   A.!k.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2014-07-11T01:56:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 169,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
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
    0000   0x5b 0xa9                                  [.
    decimal
             91  169
    datetime (2014-07-11T01:56:20)
    0000   0x54 0xf8 0x01 0x0b 0x0e                   T....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x09 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106    9    0    0
              0    0    0    9  125
    HOUR BITS: [1, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 4.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xa4 0x2e 0x14                   \....
    decimal
             92    5  164   46   20
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2014-07-11T01:56:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'duration': 0, 'programmed': 0.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2014-07-11T01:56:20)
    0000   0x54 0xf8 0x41 0x0b 0x0e                   T.A..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 51 BolusWizard 2014-07-11T18:56:14 head[2], body[13] op[0x5b]
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
    datetime (2014-07-11T18:56:14)
    0000   0x4e 0xf8 0x12 0x0b 0x0e                   N....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [1, 1, 1]
#### RECORD 52 Bolus 2014-07-11T18:56:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'duration': 0, 'programmed': 1.3, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2014-07-11T18:56:14)
    0000   0x4e 0xf8 0x52 0x0b 0x0e                   N.R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 53 LowBattery 2014-07-11T23:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2014-07-11T23:01:00)
    0000   0x40 0xc1 0x17 0x0b 0x0e                   @....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 54 CalBGForPH 2014-07-11T23:30:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2014-07-11T23:30:45)
    0000   0x6d 0xde 0x37 0x0b 0x0e                   m.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 BolusWizard 2014-07-11T23:31:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.5,
 'carb_input': 72,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.5,
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
    datetime (2014-07-11T23:31:51)
    0000   0x73 0xdf 0x17 0x0b 0x0e                   s....
    body (13)
    hex
    0000   0x48 0x50 0x0d 0x2d 0x6a 0x00 0x37 0x00    HP.-j.7.
    0008   0x00 0x00 0x00 0x37 0x7d                   ...7}
    decimal
             72   80   13   45  106    0   55    0
              0    0    0   55  125
    HOUR BITS: [1, 1, 0]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 1.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x34 0x15 0x14                   \.4..
    decimal
             92    5   52   21   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2014-07-11T23:31:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5, 'duration': 0, 'programmed': 5.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x37 0x37 0x00                        .77.
    decimal
              1   55   55    0
    datetime (2014-07-11T23:31:51)
    0000   0x73 0xdf 0x57 0x0b 0x0e                   s.W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 58 MResultTotals 2014-07-12T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xb8                   .....
    decimal
              7    0    0    4  184
    datetime (2014-07-12T00:00:00)
    0000   0x6b 0x8e                                  k.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 Model522ResultTotals 2014-07-12T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-12T00:00:00)
    0000   0x6b 0x8e                                  k.
    body (41)
    hex
    0000   0x05 0x00 0x8b 0x6c 0xa9 0x02 0x00 0x00    ...l....
    0008   0x04 0xb8 0x03 0x84 0x4b 0x01 0x34 0x19    ....K.4.
    0010   0x00 0x5a 0x01 0x34 0x19 0x01 0x10 0x58    .Z.4...X
    0018   0x00 0x24 0x0c 0x00 0x00 0x00 0x03 0x02    .$......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  139  108  169    2    0    0
              4  184    3  132   75    1   52   25
              0   90    1   52   25    1   16   88
              0   36   12    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 60 BolusWizard 2014-07-12T00:20:35 head[2], body[13] op[0x5b]
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
    datetime (2014-07-12T00:20:35)
    0000   0x63 0xd4 0x00 0x0c 0x0e                   c....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 1, 0]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 2.25, 'curve': 4},
 {'age': 56, 'amount': 3.25, 'curve': 4},
 {'age': 70, 'amount': 1.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x5a 0x2e 0x04 0x82 0x38 0x04    \.Z...8.
    0008   0x34 0x46 0x14                             4F.
    decimal
             92   11   90   46    4  130   56    4
             52   70   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2014-07-12T00:20:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'duration': 0, 'programmed': 1.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2014-07-12T00:20:35)
    0000   0x63 0xd4 0x40 0x0c 0x0e                   c.@..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 BolusWizard 2014-07-12T00:30:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
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
    datetime (2014-07-12T00:30:50)
    0000   0x72 0xde 0x00 0x0c 0x0e                   r....
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    0    0   18  125
    HOUR BITS: [1, 1, 0]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 1.7, 'curve': 4},
 {'age': 56, 'amount': 2.25, 'curve': 4},
 {'age': 66, 'amount': 3.25, 'curve': 4},
 {'age': 80, 'amount': 1.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x44 0x10 0x04 0x5a 0x38 0x04    \.D..Z8.
    0008   0x82 0x42 0x04 0x34 0x50 0x14              .B.4P.
    decimal
             92   14   68   16    4   90   56    4
            130   66    4   52   80   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2014-07-12T00:30:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'duration': 0, 'programmed': 1.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2014-07-12T00:30:50)
    0000   0x72 0xde 0x40 0x0c 0x0e                   r.@..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 66 Battery 2014-07-12T23:25:35 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2014-07-12T23:25:35)
    0000   0x63 0xd9 0x17 0x0c 0x0e                   c....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 Battery 2014-07-12T23:26:10 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-07-12T23:26:10)
    0000   0x4a 0xda 0x17 0x0c 0x0e                   J....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 BolusWizard 2014-07-12T23:52:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.6,
 'carb_input': 86,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 6.6,
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
    datetime (2014-07-12T23:52:36)
    0000   0x64 0xf4 0x17 0x0c 0x0e                   d....
    body (13)
    hex
    0000   0x56 0x50 0x0d 0x2d 0x6a 0x00 0x42 0x00    VP.-j.B.
    0008   0x00 0x00 0x00 0x42 0x7d                   ...B}
    decimal
             86   80   13   45  106    0   66    0
              0    0    0   66  125
    HOUR BITS: [1, 1, 1]
#### RECORD 69 Bolus 2014-07-12T23:52:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'duration': 0, 'programmed': 4.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2014-07-12T23:52:36)
    0000   0x64 0xf4 0x97 0x0c 0x0e                   d....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 70 MResultTotals 2014-07-13T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xb6                   .....
    decimal
              7    0    0    4  182
    datetime (2014-07-13T00:00:00)
    0000   0x6c 0x8e                                  l.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 71 Model522ResultTotals 2014-07-13T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-13T00:00:00)
    0000   0x6c 0x8e                                  l.
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x04 0xb6 0x03 0x84 0x4b 0x01 0x32 0x19    ....K.2.
    0010   0x00 0x85 0x01 0x32 0x19 0x01 0x32 0x64    ...2..2d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              4  182    3  132   75    1   50   25
              0  133    1   50   25    1   50  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 72 Bolus 2014-07-12T23:55:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 90, 'programmed': 2.6, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x03                        ....
    decimal
              1   26   26    3
    datetime (2014-07-12T23:55:16)
    0000   0x50 0xf7 0xb7 0x0c 0x0e                   P....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 73 CalBGForPH 2014-07-13T10:09:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2014-07-13T10:09:04)
    0000   0x44 0xc9 0x2a 0x6d 0x0e                   D.*m.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 74 Ian3F 2014-07-13T10:09:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-07-13T10:09:04)
    0000   0x44 0xc9 0xea 0x6d 0x0e                   D..m.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 75 PumpSuspend 2014-07-13T21:30:31 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-07-13T21:30:31)
    0000   0x5f 0xde 0x15 0x0d 0x0e                   _....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 CalBGForPH 2014-07-13T22:05:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 49}
```
    op hex (2)
    0000   0x0a 0x31                                  .1
    decimal
             10   49
    datetime (2014-07-13T22:05:46)
    0000   0x6e 0xc5 0x36 0x6d 0x0e                   n.6m.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
`end m522-ReadHistoryData-page-1.data: 77 records`
## START m522-ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xd7 0xc9                                  ..
##### DEBUG DECIMAL
            215  201
#### RECORD 0 CalBGForPH 2014-07-01T03:36:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 284}
```
    op hex (2)
    0000   0x0a 0x1c                                  ..
    decimal
             10   28
    datetime (2014-07-01T03:36:43)
    0000   0x6b 0xe4 0x23 0x61 0x8e                   k.#a.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 Ian3F 2014-07-01T03:36:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2014-07-01T03:36:43)
    0000   0x6b 0xe4 0x83 0x61 0x0e                   k..a.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2014-07-01T03:37:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 35,
 '_byte[7]': 0,
 'bg': 284,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x1c                                  [.
    decimal
             91   28
    datetime (2014-07-01T03:37:00)
    0000   0x40 0xe5 0x03 0x01 0x0e                   @....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00 0x00    .Q.-j#..
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
              0   81   13   45  106   35    0    0
              0    0    0   35  125
    HOUR BITS: [1, 1, 1]
#### RECORD 3 Bolus 2014-07-01T03:37:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'duration': 0, 'programmed': 3.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2014-07-01T03:37:00)
    0000   0x40 0xe5 0x43 0x01 0x0e                   @.C..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 BolusWizard 2014-07-01T21:58:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
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
    datetime (2014-07-01T21:58:28)
    0000   0x5c 0xfa 0x15 0x01 0x0e                   \....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [1, 1, 1]
#### RECORD 5 Bolus 2014-07-01T21:58:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 0, 'programmed': 2.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2014-07-01T21:58:28)
    0000   0x5c 0xfa 0x55 0x01 0x0e                   \.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 BolusWizard 2014-07-01T23:40:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
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
    datetime (2014-07-01T23:40:15)
    0000   0x4f 0xe8 0x17 0x01 0x0e                   O....
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    =P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             61   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [1, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 106, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x6a 0x04                   \.Pj.
    decimal
             92    5   80  106    4
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2014-07-01T23:40:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'duration': 0, 'programmed': 4.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2014-07-01T23:40:15)
    0000   0x4f 0xe8 0x57 0x01 0x0e                   O.W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 MResultTotals 2014-07-02T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x16                   .....
    decimal
              7    0    0    5   22
    datetime (2014-07-02T00:00:00)
    0000   0x61 0x8e                                  a.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 Model522ResultTotals 2014-07-02T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-02T00:00:00)
    0000   0x61 0x8e                                  a.
    body (41)
    hex
    0000   0x05 0x15 0x1c 0x1c 0x1c 0x01 0x00 0x00    ........
    0008   0x05 0x16 0x03 0x82 0x45 0x01 0x94 0x1f    ....E...
    0010   0x00 0x58 0x01 0x94 0x1f 0x01 0x08 0x41    .X.....A
    0018   0x00 0x8c 0x23 0x00 0x00 0x00 0x03 0x02    ..#.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21   28   28   28    1    0    0
              5   22    3  130   69    1  148   31
              0   88    1  148   31    1    8   65
              0  140   35    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 11 BolusWizard 2014-07-02T00:40:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 21,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.6,
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
    datetime (2014-07-02T00:40:09)
    0000   0x49 0xe8 0x00 0x02 0x0e                   I....
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             21   80   13   45  106    0   16    0
              0    0    0   16  125
    HOUR BITS: [1, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 4.6, 'curve': 4},
 {'age': 166, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xb8 0x42 0x04 0x50 0xa6 0x04    \..B.P..
    decimal
             92    8  184   66    4   80  166    4
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2014-07-02T00:40:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'duration': 0, 'programmed': 1.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2014-07-02T00:40:09)
    0000   0x49 0xe8 0x40 0x02 0x0e                   I.@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 BolusWizard 2014-07-02T00:55:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
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
    datetime (2014-07-02T00:55:26)
    0000   0x5a 0xf7 0x00 0x02 0x0e                   Z....
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    #P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             35   80   13   45  106    0   26    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 1.6, 'curve': 4},
 {'age': 81, 'amount': 4.6, 'curve': 4},
 {'age': 181, 'amount': 2.0, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x15 0x04 0xb8 0x51 0x04    \.@...Q.
    0008   0x50 0xb5 0x04                             P..
    decimal
             92   11   64   21    4  184   81    4
             80  181    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2014-07-02T00:55:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2014-07-02T00:55:26)
    0000   0x5a 0xf7 0x40 0x02 0x0e                   Z.@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 CalBGForPH 2014-07-02T23:06:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2014-07-02T23:06:33)
    0000   0x61 0xc6 0x37 0x02 0x0e                   a.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 BolusWizard 2014-07-02T23:07:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
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
    datetime (2014-07-02T23:07:20)
    0000   0x54 0xc7 0x17 0x02 0x0e                   T....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    <P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [1, 1, 0]
#### RECORD 19 Bolus 2014-07-02T23:07:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'duration': 0, 'programmed': 4.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2014-07-02T23:07:20)
    0000   0x54 0xc7 0x57 0x02 0x0e                   T.W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 MResultTotals 2014-07-03T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xe4                   .....
    decimal
              7    0    0    4  228
    datetime (2014-07-03T00:00:00)
    0000   0x62 0x8e                                  b.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 Model522ResultTotals 2014-07-03T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-03T00:00:00)
    0000   0x62 0x8e                                  b.
    body (41)
    hex
    0000   0x05 0x00 0x69 0x69 0x69 0x01 0x00 0x00    ..iii...
    0008   0x04 0xe4 0x03 0x84 0x48 0x01 0x60 0x1c    ....H.`.
    0010   0x00 0x74 0x01 0x60 0x1c 0x01 0x60 0x64    .t.`..`d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  105  105  105    1    0    0
              4  228    3  132   72    1   96   28
              0  116    1   96   28    1   96  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 22 BolusWizard 2014-07-03T01:36:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-07-03T01:36:58)
    0000   0x7a 0xe4 0x01 0x03 0x0e                   z....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x00 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             45   80   13   45  106    0   34    0
              0    0    0   34  125
    HOUR BITS: [1, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 4.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb8 0x98 0x04                   \....
    decimal
             92    5  184  152    4
    datetime (unknown)

    body (0)

#### RECORD 24 PumpSuspend 2014-07-03T01:37:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-07-03T01:37:17)
    0000   0x51 0xe5 0x01 0x03 0x0e                   Q....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 Bolus 2014-07-03T01:36:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x05 0x00                        ."..
    decimal
              1   34    5    0
    datetime (2014-07-03T01:36:58)
    0000   0x7a 0xe4 0x41 0x03 0x0e                   z.A..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 PumpResume 2014-07-03T01:37:19 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-07-03T01:37:19)
    0000   0x53 0xe5 0x01 0x03 0x0e                   S....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 27 BolusWizard 2014-07-03T01:37:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.3,
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
    datetime (2014-07-03T01:37:31)
    0000   0x5f 0xe5 0x01 0x03 0x0e                   _....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [1, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 0.5, 'curve': 4},
 {'age': 153, 'amount': 4.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x03 0x04 0xb8 0x99 0x04    \.......
    decimal
             92    8   20    3    4  184  153    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2014-07-03T01:37:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'duration': 0, 'programmed': 2.3, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2014-07-03T01:37:32)
    0000   0x60 0xe5 0x41 0x03 0x0e                   `.A..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 CalBGForPH 2014-07-03T09:20:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 273}
```
    op hex (2)
    0000   0x0a 0x11                                  ..
    decimal
             10   17
    datetime (2014-07-03T09:20:05)
    0000   0x45 0xd4 0x29 0x63 0x8e                   E.)c.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 31 Ian3F 2014-07-03T09:20:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x22                                  ?"
    decimal
             63   34
    datetime (2014-07-03T09:20:05)
    0000   0x45 0xd4 0x29 0x63 0x0e                   E.)c.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 BolusWizard 2014-07-03T09:20:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 273,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
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
    0000   0x5b 0x11                                  [.
    decimal
             91   17
    datetime (2014-07-03T09:20:16)
    0000   0x50 0xd4 0x09 0x03 0x0e                   P....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
              0   81   13   45  106   32    0    0
              0    0    0   32  125
    HOUR BITS: [1, 1, 0]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 210, 'amount': 2.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x70 0xd2 0x14                   \.p..
    decimal
             92    5  112  210   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2014-07-03T09:20:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2014-07-03T09:20:17)
    0000   0x51 0xd4 0x49 0x03 0x0e                   Q.I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 35 BolusWizard 2014-07-03T16:43:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
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
    datetime (2014-07-03T16:43:15)
    0000   0x4f 0xeb 0x10 0x03 0x0e                   O....
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    "P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             34   80   13   45  106    0   26    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 3.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x88 0xc1 0x14                   \....
    decimal
             92    5  136  193   20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2014-07-03T16:43:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2014-07-03T16:43:15)
    0000   0x4f 0xeb 0x50 0x03 0x0e                   O.P..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 CalBGForPH 2014-07-03T17:43:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2014-07-03T17:43:37)
    0000   0x65 0xeb 0x31 0x03 0x0e                   e.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 BolusWizard 2014-07-03T17:44:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 106,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2014-07-03T17:44:16)
    0000   0x50 0xec 0x11 0x03 0x0e                   P....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x00 0x05 0x00    .P.-j...
    0008   0x00 0x15 0x00 0x05 0x7d                   ....}
    decimal
              7   80   13   45  106    0    5    0
              0   21    0    5  125
    HOUR BITS: [1, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 1.45, 'curve': 4},
 {'age': 70, 'amount': 1.15, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x3a 0x3c 0x04 0x2e 0x46 0x04    \.:<..F.
    decimal
             92    8   58   60    4   46   70    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2014-07-03T17:44:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'duration': 0, 'programmed': 0.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2014-07-03T17:44:16)
    0000   0x50 0xec 0x91 0x03 0x0e                   P....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 Bolus 2014-07-03T17:44:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'duration': 30, 'programmed': 0.3, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x01                        ....
    decimal
              1    3    3    1
    datetime (2014-07-03T17:44:23)
    0000   0x57 0xec 0xb1 0x03 0x0e                   W....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 43 CalBGForPH 2014-07-03T18:21:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2014-07-03T18:21:00)
    0000   0x40 0xd5 0x32 0x03 0x0e                   @.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 44 BolusWizard 2014-07-03T18:21:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 106,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 3,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2014-07-03T18:21:24)
    0000   0x58 0xd5 0x12 0x03 0x0e                   X....
    body (13)
    hex
    0000   0x03 0x50 0x0d 0x2d 0x6a 0x00 0x02 0x00    .P.-j...
    0008   0x00 0x14 0x00 0x02 0x7d                   ....}
    decimal
              3   80   13   45  106    0    2    0
              0   20    0    2  125
    HOUR BITS: [1, 1, 0]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 0.1, 'curve': 4},
 {'age': 27, 'amount': 0.1, 'curve': 4},
 {'age': 37, 'amount': 0.3, 'curve': 4},
 {'age': 97, 'amount': 1.45, 'curve': 4},
 {'age': 107, 'amount': 1.15, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x04 0x11 0x04 0x04 0x1b 0x04    \.......
    0008   0x0c 0x25 0x04 0x3a 0x61 0x04 0x2e 0x6b    .%.:a..k
    0010   0x04                                       .
    decimal
             92   17    4   17    4    4   27    4
             12   37    4   58   97    4   46  107
              4
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2014-07-03T18:21:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'duration': 60, 'programmed': 0.2, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x02                        ....
    decimal
              1    2    2    2
    datetime (2014-07-03T18:21:24)
    0000   0x58 0xd5 0x72 0x03 0x0e                   X.r..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 47 CalBGForPH 2014-07-03T23:23:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2014-07-03T23:23:13)
    0000   0x4d 0xd7 0x37 0x63 0x0e                   M.7c.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 Ian3F 2014-07-03T23:23:13 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2014-07-03T23:23:13)
    0000   0x4d 0xd7 0x57 0x63 0x0e                   M.Wc.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 BolusWizard 2014-07-03T23:28:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.4,
 'carb_input': 84,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 6.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2014-07-03T23:28:49)
    0000   0x71 0xdc 0x17 0x03 0x0e                   q....
    body (13)
    hex
    0000   0x54 0x50 0x0d 0x2d 0x6a 0x00 0x40 0x00    TP.-j.@.
    0008   0x00 0x00 0x00 0x40 0x7d                   ...@}
    decimal
             84   80   13   45  106    0   64    0
              0    0    0   64  125
    HOUR BITS: [1, 1, 0]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.05, 'curve': 20},
 {'age': 18, 'amount': 0.05, 'curve': 20},
 {'age': 38, 'amount': 0.05, 'curve': 20},
 {'age': 48, 'amount': 0.05, 'curve': 20},
 {'age': 68, 'amount': 0.1, 'curve': 20},
 {'age': 78, 'amount': 0.1, 'curve': 20},
 {'age': 88, 'amount': 0.3, 'curve': 20},
 {'age': 148, 'amount': 1.45, 'curve': 20},
 {'age': 158, 'amount': 1.15, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x02 0x08 0x14 0x02 0x12 0x14    \.......
    0008   0x02 0x26 0x14 0x02 0x30 0x14 0x04 0x44    .&..0..D
    0010   0x14 0x04 0x4e 0x14 0x0c 0x58 0x14 0x3a    ..N..X.:
    0018   0x94 0x14 0x2e 0x9e 0x14                   .....
    decimal
             92   29    2    8   20    2   18   20
              2   38   20    2   48   20    4   68
             20    4   78   20   12   88   20   58
            148   20   46  158   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2014-07-03T23:28:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'duration': 0, 'programmed': 3.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2014-07-03T23:28:49)
    0000   0x71 0xdc 0x97 0x03 0x0e                   q....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 52 MResultTotals 2014-07-04T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xb4                   .....
    decimal
              7    0    0    5  180
    datetime (2014-07-04T00:00:00)
    0000   0x63 0x8e                                  c.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 Model522ResultTotals 2014-07-04T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-04T00:00:00)
    0000   0x63 0x8e                                  c.
    body (41)
    hex
    0000   0x05 0x10 0x96 0x6a 0x11 0x04 0x00 0x00    ...j....
    0008   0x05 0xb4 0x03 0x84 0x3e 0x02 0x30 0x26    ....>.0&
    0010   0x00 0xcc 0x02 0x30 0x26 0x01 0xa8 0x4c    ...0&..L
    0018   0x00 0x88 0x18 0x00 0x00 0x00 0x07 0x06    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  150  106   17    4    0    0
              5  180    3  132   62    2   48   38
              0  204    2   48   38    1  168   76
              0  136   24    0    0    0    7    6
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 54 Bolus 2014-07-03T23:31:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'duration': 90, 'programmed': 2.8, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x03                        ....
    decimal
              1   28   28    3
    datetime (2014-07-03T23:31:11)
    0000   0x4b 0xdf 0xb7 0x03 0x0e                   K....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 CalBGForPH 2014-07-04T02:55:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2014-07-04T02:55:17)
    0000   0x51 0xf7 0x22 0x64 0x0e                   Q."d.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 Ian3F 2014-07-04T02:55:17 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-07-04T02:55:17)
    0000   0x51 0xf7 0xc2 0x64 0x0e                   Q..d.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 LowReservoir 2014-07-04T16:53:41 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-07-04T16:53:41)
    0000   0x69 0xf5 0x10 0x04 0x0e                   i....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 58 CalBGForPH 2014-07-04T22:43:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2014-07-04T22:43:01)
    0000   0x41 0xeb 0x36 0x64 0x0e                   A.6d.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 Ian3F 2014-07-04T22:43:01 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-07-04T22:43:01)
    0000   0x41 0xeb 0xf6 0x64 0x0e                   A..d.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 CalBGForPH 2014-07-04T23:02:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2014-07-04T23:02:42)
    0000   0x6a 0xc2 0x37 0x04 0x0e                   j.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 61 BolusWizard 2014-07-04T23:03:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.1,
 'carb_input': 67,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2014-07-04T23:03:15)
    0000   0x4f 0xc3 0x17 0x04 0x0e                   O....
    body (13)
    hex
    0000   0x43 0x50 0x0d 0x2d 0x6a 0x00 0x33 0x00    CP.-j.3.
    0008   0x00 0x00 0x00 0x33 0x7d                   ...3}
    decimal
             67   80   13   45  106    0   51    0
              0    0    0   51  125
    HOUR BITS: [1, 1, 0]
#### RECORD 62 Bolus 2014-07-04T23:03:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'duration': 0, 'programmed': 3.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2014-07-04T23:03:15)
    0000   0x4f 0xc3 0x97 0x04 0x0e                   O....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 LowReservoir 2014-07-04T23:30:13 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-07-04T23:30:13)
    0000   0x4d 0xde 0x17 0x04 0x0e                   M....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 MResultTotals 2014-07-05T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x7e                   ....~
    decimal
              7    0    0    4  126
    datetime (2014-07-05T00:00:00)
    0000   0x64 0x8e                                  d.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 65 Model522ResultTotals 2014-07-05T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-05T00:00:00)
    0000   0x64 0x8e                                  d.
    body (41)
    hex
    0000   0x05 0x00 0x61 0x46 0x6f 0x03 0x00 0x00    ..aFo...
    0008   0x04 0x7e 0x03 0x84 0x4e 0x00 0xfa 0x16    .~..N...
    0010   0x00 0x43 0x00 0xfa 0x16 0x00 0xfa 0x64    .C.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   97   70  111    3    0    0
              4  126    3  132   78    0  250   22
              0   67    0  250   22    0  250  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 66 Bolus 2014-07-04T23:05:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'duration': 90, 'programmed': 1.9, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x03                        ....
    decimal
              1   19   19    3
    datetime (2014-07-04T23:05:21)
    0000   0x55 0xc5 0xb7 0x04 0x0e                   U....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 Rewind 2014-07-05T22:44:32 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-07-05T22:44:32)
    0000   0x60 0xec 0x16 0x05 0x0e                   `....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 Prime 2014-07-05T22:47:10 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x31                   ....1
    decimal
              3    0    0    0   49
    datetime (2014-07-05T22:47:10)
    0000   0x4a 0xef 0x36 0x05 0x0e                   J.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 Prime 2014-07-05T22:47:40 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2014-07-05T22:47:40)
    0000   0x68 0xef 0x16 0x05 0x0e                   h....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 70 BolusWizard 2014-07-05T23:04:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.1,
 'carb_input': 80,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 6.1,
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
    datetime (2014-07-05T23:04:28)
    0000   0x5c 0xc4 0x17 0x05 0x0e                   \....
    body (13)
    hex
    0000   0x50 0x50 0x0d 0x2d 0x6a 0x00 0x3d 0x00    PP.-j.=.
    0008   0x00 0x00 0x00 0x3d 0x7d                   ...=}
    decimal
             80   80   13   45  106    0   61    0
              0    0    0   61  125
    HOUR BITS: [1, 1, 0]
#### RECORD 71 Bolus 2014-07-05T23:04:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'duration': 0, 'programmed': 3.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2014-07-05T23:04:28)
    0000   0x5c 0xc4 0x97 0x05 0x0e                   \....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 MResultTotals 2014-07-06T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x70                   ....p
    decimal
              7    0    0    4  112
    datetime (2014-07-06T00:00:00)
    0000   0x65 0x8e                                  e.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 73 Model522ResultTotals 2014-07-06T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-07-06T00:00:00)
    0000   0x65 0x8e                                  e.
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x04 0x70 0x03 0x82 0x4f 0x00 0xee 0x15    .p..O...
    0010   0x00 0x50 0x00 0xee 0x15 0x00 0xee 0x64    .P.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              4  112    3  130   79    0  238   21
              0   80    0  238   21    0  238  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 74 Bolus 2014-07-05T23:07:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'duration': 90, 'programmed': 2.2, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x03                        ....
    decimal
              1   22   22    3
    datetime (2014-07-05T23:07:05)
    0000   0x45 0xc7 0xb7 0x05 0x0e                   E....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 75 PumpSuspend 2014-07-06T21:05:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-07-06T21:05:53)
    0000   0x75 0xc5 0x15 0x06 0x0e                   u....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 PumpResume 2014-07-06T21:36:47 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-07-06T21:36:47)
    0000   0x6f 0xe4 0x15 0x06 0x0e                   o....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 77 CalBGForPH 2014-07-06T22:05:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2014-07-06T22:05:43)
    0000   0x6b 0xc5 0x36 0x66 0x0e                   k.6f.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
`end m522-ReadHistoryData-page-2.data: 78 records`
## START m522-ReadHistoryData-page-3.data
ERROR day is out of range for month (2014, 6, 31, 0, 0, 0) 0000   0x7e 0x0e                                  ~.
ERROR day is out of range for month 0000   0x7e 0x0e                                  ~.
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe2 0xab                                  ..
##### DEBUG DECIMAL
            226  171
#### RECORD 0 BolusWizard 2014-06-24T18:14:52 head[2], body[13] op[0x5b]
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
    datetime (2014-06-24T18:14:52)
    0000   0x74 0x8e 0x12 0x18 0x0e                   t....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [1, 0, 0]
#### RECORD 1 Bolus 2014-06-24T18:14:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'duration': 0, 'programmed': 1.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2014-06-24T18:14:52)
    0000   0x74 0x8e 0x52 0x18 0x0e                   t.R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 2 BolusWizard 2014-06-24T23:19:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.5,
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
    datetime (2014-06-24T23:19:27)
    0000   0x5b 0x93 0x17 0x18 0x0e                   [....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125
    HOUR BITS: [1, 0, 0]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 1.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x4c 0x31 0x14                   \.L1.
    decimal
             92    5   76   49   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2014-06-24T23:19:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'duration': 0, 'programmed': 1.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2014-06-24T23:19:28)
    0000   0x5c 0x93 0x57 0x18 0x0e                   \.W..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 MResultTotals 2014-06-25T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x62                   ....b
    decimal
              7    0    0    4   98
    datetime (2014-06-25T00:00:00)
    0000   0x78 0x0e                                  x.
    body (0)

#### RECORD 6 Model522ResultTotals 2014-06-25T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-06-25T00:00:00)
    0000   0x78 0x0e                                  x.
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x04 0x62 0x03 0x76 0x4f 0x00 0xec 0x15    .b.vO...
    0010   0x00 0x2d 0x00 0xec 0x15 0x00 0xec 0x64    .-.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              4   98    3  118   79    0  236   21
              0   45    0  236   21    0  236  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0

#### RECORD 7 LowReservoir 2014-06-25T09:51:49 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-06-25T09:51:49)
    0000   0x71 0xb3 0x09 0x19 0x0e                   q....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 8 LowReservoir 2014-06-25T19:44:12 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-06-25T19:44:12)
    0000   0x4c 0xac 0x13 0x19 0x0e                   L....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 BolusWizard 2014-06-25T21:05:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-25T21:05:49)
    0000   0x71 0x85 0x15 0x19 0x0e                   q....
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x00 0x1f 0x00    )P.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             41   80   13   45  106    0   31    0
              0    0    0   31  125
    HOUR BITS: [1, 0, 0]
#### RECORD 10 Bolus 2014-06-25T21:05:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'duration': 0, 'programmed': 3.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2014-06-25T21:05:49)
    0000   0x71 0x85 0x55 0x19 0x0e                   q.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 BolusWizard 2014-06-25T22:13:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
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
    datetime (2014-06-25T22:13:30)
    0000   0x5e 0x8d 0x16 0x19 0x0e                   ^....
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    0    0   18  125
    HOUR BITS: [1, 0, 0]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 3.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x45 0x04                   \.|E.
    decimal
             92    5  124   69    4
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2014-06-25T22:13:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'duration': 0, 'programmed': 1.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2014-06-25T22:13:30)
    0000   0x5e 0x8d 0x56 0x19 0x0e                   ^.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 14 MResultTotals 2014-06-26T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x48                   ....H
    decimal
              7    0    0    4   72
    datetime (2014-06-26T00:00:00)
    0000   0x79 0x0e                                  y.
    body (0)

#### RECORD 15 Model522ResultTotals 2014-06-26T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-06-26T00:00:00)
    0000   0x79 0x0e                                  y.
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x04 0x48 0x03 0x84 0x52 0x00 0xc4 0x12    .H..R...
    0010   0x00 0x41 0x00 0xc4 0x12 0x00 0xc4 0x64    .A.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              4   72    3  132   82    0  196   18
              0   65    0  196   18    0  196  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0

#### RECORD 16 Rewind 2014-06-26T21:30:51 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-06-26T21:30:51)
    0000   0x73 0x9e 0x15 0x1a 0x0e                   s....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 Prime 2014-06-26T21:33:15 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x10                   .....
    decimal
              3    0    0    0   16
    datetime (2014-06-26T21:33:15)
    0000   0x4f 0xa1 0x35 0x1a 0x0e                   O.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 Prime 2014-06-26T21:33:35 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2014-06-26T21:33:35)
    0000   0x63 0xa1 0x15 0x1a 0x0e                   c....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 19 BolusWizard 2014-06-26T22:21:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
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
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-26T22:21:48)
    0000   0x70 0x95 0x16 0x1a 0x0e                   p....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             47   80   13   45  106    0   36    0
              0    0    0   36  125
    HOUR BITS: [1, 0, 0]
#### RECORD 20 Bolus 2014-06-26T22:21:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'duration': 0, 'programmed': 3.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2014-06-26T22:21:48)
    0000   0x70 0x95 0x56 0x1a 0x0e                   p.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 MResultTotals 2014-06-27T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x12                   .....
    decimal
              7    0    0    4   18
    datetime (2014-06-27T00:00:00)
    0000   0x7a 0x0e                                  z.
    body (0)

#### RECORD 22 Model522ResultTotals 2014-06-27T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-06-27T00:00:00)
    0000   0x7a 0x0e                                  z.
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x04 0x12 0x03 0x82 0x56 0x00 0x90 0x0e    ....V...
    0010   0x00 0x2f 0x00 0x90 0x0e 0x00 0x90 0x64    ./.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              4   18    3  130   86    0  144   14
              0   47    0  144   14    0  144  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0

#### RECORD 23 PumpSuspend 2014-06-27T10:22:51 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-06-27T10:22:51)
    0000   0x73 0x96 0x0a 0x1b 0x0e                   s....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 PumpResume 2014-06-27T10:38:36 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-06-27T10:38:36)
    0000   0x64 0xa6 0x0a 0x1b 0x0e                   d....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 25 CalBGForPH 2014-06-27T12:06:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 299}
```
    op hex (2)
    0000   0x0a 0x2b                                  .+
    decimal
             10   43
    datetime (2014-06-27T12:06:15)
    0000   0x4f 0x86 0x2c 0x7b 0x8e                   O.,{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 Ian3F 2014-06-27T12:06:15 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x25                                  ?%
    decimal
             63   37
    datetime (2014-06-27T12:06:15)
    0000   0x4f 0x86 0x6c 0x7b 0x0e                   O.l{.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 BolusWizard 2014-06-27T12:06:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 38,
 '_byte[7]': 0,
 'bg': 299,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
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
    0000   0x5b 0x2b                                  [+
    decimal
             91   43
    datetime (2014-06-27T12:06:23)
    0000   0x57 0x86 0x0c 0x1b 0x0e                   W....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x26 0x00 0x00    .Q.-j&..
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
              0   81   13   45  106   38    0    0
              0    0    0   38  125
    HOUR BITS: [1, 0, 0]
#### RECORD 28 Bolus 2014-06-27T12:06:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'duration': 0, 'programmed': 3.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2014-06-27T12:06:23)
    0000   0x57 0x86 0x4c 0x1b 0x0e                   W.L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 CalBGForPH 2014-06-27T13:04:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 267}
```
    op hex (2)
    0000   0x0a 0x0b                                  ..
    decimal
             10   11
    datetime (2014-06-27T13:04:31)
    0000   0x5f 0x84 0x2d 0x7b 0x8e                   _.-{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 Ian3F 2014-06-27T13:04:31 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x21                                  ?!
    decimal
             63   33
    datetime (2014-06-27T13:04:31)
    0000   0x5f 0x84 0x6d 0x7b 0x0e                   _.m{.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2014-06-27T13:09:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 267,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0b                                  [.
    decimal
             91   11
    datetime (2014-06-27T13:09:37)
    0000   0x65 0x89 0x0d 0x1b 0x0e                   e....
    body (13)
    hex
    0000   0x45 0x51 0x0d 0x2d 0x6a 0x1f 0x35 0x00    EQ.-j.5.
    0008   0x00 0x1f 0x00 0x35 0x7d                   ...5}
    decimal
             69   81   13   45  106   31   53    0
              0   31    0   53  125
    HOUR BITS: [1, 0, 0]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 3.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x98 0x41 0x04                   \..A.
    decimal
             92    5  152   65    4
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2014-06-27T13:09:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'duration': 0, 'programmed': 5.3, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2014-06-27T13:09:37)
    0000   0x65 0x89 0x4d 0x1b 0x0e                   e.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 34 BolusWizard 2014-06-27T13:26:14 head[2], body[13] op[0x5b]
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
    datetime (2014-06-27T13:26:14)
    0000   0x4e 0x9a 0x0d 0x1b 0x0e                   N....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [1, 0, 0]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 5.3, 'curve': 4},
 {'age': 82, 'amount': 3.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xd4 0x16 0x04 0x98 0x52 0x04    \.....R.
    decimal
             92    8  212   22    4  152   82    4
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2014-06-27T13:26:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'duration': 0, 'programmed': 1.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2014-06-27T13:26:14)
    0000   0x4e 0x9a 0x4d 0x1b 0x0e                   N.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 37 CalBGForPH 2014-06-27T13:30:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2014-06-27T13:30:03)
    0000   0x43 0x9e 0x2d 0x1b 0x0e                   C.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 38 CalBGForPH 2014-06-27T22:45:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 58}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2014-06-27T22:45:13)
    0000   0x4d 0xad 0x36 0x7b 0x0e                   M.6{.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 Ian3F 2014-06-27T22:45:13 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-06-27T22:45:13)
    0000   0x4d 0xad 0x56 0x7b 0x0e                   M.V{.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 CalBGForPH 2014-06-27T23:22:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 60}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2014-06-27T23:22:17)
    0000   0x51 0x96 0x37 0x7b 0x0e                   Q.7{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2014-06-27T23:22:17 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-06-27T23:22:17)
    0000   0x51 0x96 0x97 0x7b 0x0e                   Q..{.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 MResultTotals 2014-06-28T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x30                   ....0
    decimal
              7    0    0    5   48
    datetime (2014-06-28T00:00:00)
    0000   0x7b 0x0e                                  {.
    body (0)

#### RECORD 43 Model522ResultTotals 2014-06-28T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-06-28T00:00:00)
    0000   0x7b 0x0e                                  {.
    body (41)
    hex
    0000   0x05 0x10 0x9e 0x3a 0x2b 0x05 0x00 0x00    ...:+...
    0008   0x05 0x30 0x03 0x78 0x43 0x01 0xb8 0x21    .0.xC..!
    0010   0x00 0x5e 0x01 0xb8 0x21 0x01 0x20 0x41    .^..!. A
    0018   0x00 0x98 0x23 0x00 0x00 0x00 0x03 0x02    ..#.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  158   58   43    5    0    0
              5   48    3  120   67    1  184   33
              0   94    1  184   33    1   32   65
              0  152   35    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0

#### RECORD 44 CalBGForPH 2014-06-28T05:31:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2014-06-28T05:31:03)
    0000   0x43 0x9f 0x25 0x7c 0x8e                   C.%|.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 45 Ian3F 2014-06-28T05:31:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2014-06-28T05:31:03)
    0000   0x43 0x9f 0x05 0x7c 0x0e                   C..|.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 46 BolusWizard 2014-06-28T05:31:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 256,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
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
    datetime (2014-06-28T05:31:26)
    0000   0x5a 0x9f 0x05 0x1c 0x0e                   Z....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    0    0   29  125
    HOUR BITS: [1, 0, 0]
#### RECORD 47 Bolus 2014-06-28T05:31:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'duration': 0, 'programmed': 2.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2014-06-28T05:31:26)
    0000   0x5a 0x9f 0x45 0x1c 0x0e                   Z.E..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 48 PumpSuspend 2014-06-28T20:00:40 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-06-28T20:00:40)
    0000   0x68 0x80 0x14 0x1c 0x0e                   h....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 49 PumpResume 2014-06-28T20:17:56 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-06-28T20:17:56)
    0000   0x78 0x91 0x14 0x1c 0x0e                   x....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 CalBGForPH 2014-06-28T20:21:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2014-06-28T20:21:33)
    0000   0x61 0x95 0x34 0x7c 0x0e                   a.4|.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 Ian3F 2014-06-28T20:21:33 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2014-06-28T20:21:33)
    0000   0x61 0x95 0x94 0x7c 0x0e                   a..|.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 BolusWizard 2014-06-28T20:22:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2014-06-28T20:22:39)
    0000   0x67 0x96 0x14 0x1c 0x0e                   g....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0    0    0   15  125
    HOUR BITS: [1, 0, 0]
#### RECORD 53 Bolus 2014-06-28T20:22:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'duration': 0, 'programmed': 1.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2014-06-28T20:22:39)
    0000   0x67 0x96 0x54 0x1c 0x0e                   g.T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 54 BolusWizard 2014-06-28T22:36:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.9,
 'carb_input': 77,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.9,
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
    datetime (2014-06-28T22:36:05)
    0000   0x45 0xa4 0x16 0x1c 0x0e                   E....
    body (13)
    hex
    0000   0x4d 0x50 0x0d 0x2d 0x6a 0x00 0x3b 0x00    MP.-j.;.
    0008   0x00 0x00 0x00 0x3b 0x7d                   ...;}
    decimal
             77   80   13   45  106    0   59    0
              0    0    0   59  125
    HOUR BITS: [1, 0, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 142, 'amount': 1.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x8e 0x04                   \.<..
    decimal
             92    5   60  142    4
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2014-06-28T22:36:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.9, 'duration': 0, 'programmed': 5.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x3b 0x3b 0x00                        .;;.
    decimal
              1   59   59    0
    datetime (2014-06-28T22:36:05)
    0000   0x45 0xa4 0x56 0x1c 0x0e                   E.V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 57 MResultTotals 2014-06-29T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x16                   .....
    decimal
              7    0    0    5   22
    datetime (2014-06-29T00:00:00)
    0000   0x7c 0x0e                                  |.
    body (0)

#### RECORD 58 Model522ResultTotals 2014-06-29T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-06-29T00:00:00)
    0000   0x7c 0x0e                                  |.
    body (41)
    hex
    0000   0x05 0x10 0xe2 0xc4 0x00 0x02 0x00 0x00    ........
    0008   0x05 0x16 0x03 0x7a 0x44 0x01 0x9c 0x20    ...zD.. 
    0010   0x00 0x4d 0x01 0x9c 0x20 0x00 0xec 0x39    .M.. ..9
    0018   0x00 0xb0 0x2b 0x00 0x00 0x00 0x03 0x01    ..+.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  226  196    0    2    0    0
              5   22    3  122   68    1  156   32
              0   77    1  156   32    0  236   57
              0  176   43    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0

#### RECORD 59 PumpSuspend 2014-06-29T18:15:46 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2014-06-29T18:15:46)
    0000   0x6e 0x8f 0x12 0x1d 0x0e                   n....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 60 PumpResume 2014-06-29T18:34:32 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2014-06-29T18:34:32)
    0000   0x60 0xa2 0x12 0x1d 0x0e                   `....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 61 CalBGForPH 2014-06-29T19:13:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2014-06-29T19:13:19)
    0000   0x53 0x8d 0x33 0x7d 0x0e                   S.3}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 Ian3F 2014-06-29T19:13:19 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2014-06-29T19:13:19)
    0000   0x53 0x8d 0x53 0x7d 0x0e                   S.S}.
    body (3)
    hex
    0000   0x83 0x47 0x87                             .G.
    decimal
            131   71  135
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 63 BolusWizard 2014-06-29T19:53:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 62,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.7,
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
    datetime (2014-06-29T19:53:21)
    0000   0x55 0xb5 0x13 0x1d 0x0e                   U....
    body (13)
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x00 0x2f 0x00    >P.-j./.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             62   80   13   45  106    0   47    0
              0    0    0   47  125
    HOUR BITS: [1, 0, 1]
#### RECORD 64 Bolus 2014-06-29T19:53:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'duration': 0, 'programmed': 4.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2014-06-29T19:53:21)
    0000   0x55 0xb5 0x53 0x1d 0x0e                   U.S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 65 BolusWizard 2014-06-29T20:45:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.0,
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
    datetime (2014-06-29T20:45:25)
    0000   0x59 0xad 0x14 0x1d 0x0e                   Y....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x00 0x1e 0x00    (P.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             40   80   13   45  106    0   30    0
              0    0    0   30  125
    HOUR BITS: [1, 0, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 51, 'amount': 3.75, 'curve': 4},
 {'age': 61, 'amount': 0.95, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x96 0x33 0x04 0x26 0x3d 0x04    \..3.&=.
    decimal
             92    8  150   51    4   38   61    4
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2014-06-29T20:45:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2014-06-29T20:45:26)
    0000   0x5a 0xad 0x54 0x1d 0x0e                   Z.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 68 LowReservoir 2014-06-29T23:56:50 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-06-29T23:56:50)
    0000   0x72 0xb8 0x17 0x1d 0x0e                   r....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 69 MResultTotals 2014-06-30T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xac                   .....
    decimal
              7    0    0    4  172
    datetime (2014-06-30T00:00:00)
    0000   0x7d 0x0e                                  }.
    body (0)

#### RECORD 70 Model522ResultTotals 2014-06-30T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2014-06-30T00:00:00)
    0000   0x7d 0x0e                                  }.
    body (41)
    hex
    0000   0x05 0x00 0x62 0x62 0x62 0x01 0x00 0x00    ..bbb...
    0008   0x04 0xac 0x03 0x78 0x4a 0x01 0x34 0x1a    ...xJ.4.
    0010   0x00 0x66 0x01 0x34 0x1a 0x01 0x34 0x64    .f.4..4d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   98   98   98    1    0    0
              4  172    3  120   74    1   52   26
              0  102    1   52   26    1   52  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0

#### RECORD 71 LowReservoir 2014-06-30T11:13:38 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-06-30T11:13:38)
    0000   0x66 0x8d 0x0b 0x1e 0x0e                   f....
    body (0)
    HOUR BITS: [1, 0, 0]
ERROR day is out of range for month (2014, 6, 31, 0, 0, 0) 0000   0x7e 0x0e                                  ~.
#### RECORD 72 MResultTotals (2014, 6, 31, 0, 0, 0) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x84                   .....
    decimal
              7    0    0    3  132
    datetime ((2014, 6, 31, 0, 0, 0))
    0000   0x7e 0x0e                                  ~.
    body (0)

ERROR day is out of range for month 0000   0x7e 0x0e                                  ~.
#### RECORD 73 Model522ResultTotals (2014, 6, 31, 0, 0, 0) head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime ((2014, 6, 31, 0, 0, 0))
    0000   0x7e 0x0e                                  ~.
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x03 0x84 0x03 0x84 0x64 0x00 0x00 0x00    ....d...
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              3  132    3  132  100    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0   12    0  232    0    0
              0

#### RECORD 74 Rewind 2014-07-01T03:29:47 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-07-01T03:29:47)
    0000   0x6f 0xdd 0x03 0x01 0x0e                   o....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 75 Prime 2014-07-01T03:31:40 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x21                   ....!
    decimal
              3    0    0    0   33
    datetime (2014-07-01T03:31:40)
    0000   0x68 0xdf 0x23 0x01 0x0e                   h.#..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 Prime 2014-07-01T03:32:02 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2014-07-01T03:32:02)
    0000   0x42 0xe0 0x03 0x01 0x0e                   B....
    body (0)
    HOUR BITS: [1, 1, 1]
`end m522-ReadHistoryData-page-3.data: 77 records`
