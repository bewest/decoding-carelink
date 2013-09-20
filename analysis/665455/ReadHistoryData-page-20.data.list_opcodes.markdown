## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 994, found 28 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xf3 0xf8                                  ..
##### DEBUG DECIMAL
            243  248
#### RECORD 0 BolusWizard 2013-05-07T05:29:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 50,
 '_byte[7]': 0,
 'bg': 352,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
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
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2013-05-07T05:29:54)
    0000   0x76 0x5d 0x05 0x07 0x0d                   v]...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x32 0x00 0x00    .Q.-j2..
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
              0   81   13   45  106   50    0    0
              0    0    0   50  125
    HOUR BITS: [0, 1, 0]
#### RECORD 1 Bolus 2013-05-07T05:29:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-05-07T05:29:54)
    0000   0x76 0x5d 0x45 0x07 0x0d                   v]E..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 2 PumpSuspend 2013-05-07T13:48:50 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-07T13:48:50)
    0000   0x72 0x70 0x0d 0x07 0x0d                   rp...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 PumpResume 2013-05-07T14:05:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-07T14:05:35)
    0000   0x63 0x45 0x0e 0x07 0x0d                   cE...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 CalBGForPH 2013-05-07T14:28:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-05-07T14:28:02)
    0000   0x42 0x5c 0x2e 0x07 0x0d                   B\...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 5 BolusWizard 2013-05-07T14:28:04 head[2], body[13] op[0x5b]
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
    datetime (2013-05-07T14:28:04)
    0000   0x44 0x5c 0x0e 0x07 0x0d                   D\...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125
    HOUR BITS: [0, 1, 0]
#### RECORD 6 Bolus 2013-05-07T14:28:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-05-07T14:28:04)
    0000   0x44 0x5c 0x4e 0x07 0x0d                   D\N..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-05-07T15:05:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-05-07T15:05:49)
    0000   0x71 0x45 0x2f 0x07 0x0d                   qE/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 8 BolusWizard 2013-05-07T15:06:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-05-07T15:06:10)
    0000   0x4a 0x46 0x0f 0x07 0x0d                   JF...
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x0a 0x27 0x00    3P.-j.'.
    0008   0x00 0x0f 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106   10   39    0
              0   15    0   39  125
    HOUR BITS: [0, 1, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
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

#### RECORD 10 Bolus 2013-05-07T15:06:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-05-07T15:06:10)
    0000   0x4a 0x46 0x4f 0x07 0x0d                   JFO..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 11 CalBGForPH 2013-05-07T16:30:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 299}
```
    op hex (2)
    0000   0x0a 0x2b                                  .+
    decimal
             10   43
    datetime (2013-05-07T16:30:17)
    0000   0x51 0x5e 0x30 0x07 0x8d                   Q^0..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 BolusWizard 2013-05-07T16:30:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 38,
 '_byte[7]': 0,
 'bg': 299,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2b                                  [+
    decimal
             91   43
    datetime (2013-05-07T16:30:21)
    0000   0x55 0x5e 0x10 0x07 0x0d                   U^...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x26 0x00 0x00    .Q.-j&..
    0008   0x00 0x21 0x00 0x05 0x7d                   .!..}
    decimal
              0   81   13   45  106   38    0    0
              0   33    0    5  125
    HOUR BITS: [0, 1, 0]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 3.9, 'curve': 4},
 {'age': 126, 'amount': 1.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x9c 0x56 0x04 0x40 0x7e 0x04    \..V.@~.
    decimal
             92    8  156   86    4   64  126    4
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-05-07T16:30:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-05-07T16:30:21)
    0000   0x55 0x5e 0x50 0x07 0x0d                   U^P..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 15 CalBGForPH 2013-05-07T23:23:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-05-07T23:23:26)
    0000   0x5a 0x57 0x37 0x07 0x0d                   ZW7..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 16 BolusWizard 2013-05-07T23:23:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2013-05-07T23:23:58)
    0000   0x7a 0x57 0x17 0x07 0x0d                   zW...
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0xfd 0x2e 0xf0    =P.-j...
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             61   80   13   45  106  253   46  240
              0    0    0   43  125
    HOUR BITS: [0, 1, 0]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 163, 'amount': 0.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x20 0xa3 0x14                   \. ..
    decimal
             92    5   32  163   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-05-07T23:23:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-05-07T23:23:58)
    0000   0x7a 0x57 0x57 0x07 0x0d                   zWW..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 19 MResultTotals (2013, 0, 7, 8, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 7, 8, 5, 0))
    0000   0x00 0x05 0xe8 0x47 0x8d                   ...G.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 Model522ResultTotals 2013-05-08T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-08T00:00:00)
    0000   0x47 0x8d                                  G.
    body (41)
    hex
    0000   0x05 0x10 0xdf 0x5c 0x60 0x05 0x00 0x00    ...\`...
    0008   0x05 0xe8 0x03 0x78 0x3b 0x02 0x70 0x29    ...x;.p)
    0010   0x00 0x70 0x02 0x70 0x29 0x01 0x48 0x35    .p.p).H5
    0018   0x01 0x28 0x2f 0x00 0x00 0x00 0x05 0x02    .(/.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  223   92   96    5    0    0
              5  232    3  120   59    2  112   41
              0  112    2  112   41    1   72   53
              1   40   47    0    0    0    5    2
              3    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 21 LowReservoir 2013-05-08T10:54:32 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-08T10:54:32)
    0000   0x60 0x76 0x0a 0x08 0x0d                   `v...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 22 PumpSuspend 2013-05-08T12:40:26 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-08T12:40:26)
    0000   0x5a 0x68 0x0c 0x08 0x0d                   Zh...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 PumpResume 2013-05-08T13:02:01 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-08T13:02:01)
    0000   0x41 0x42 0x0d 0x08 0x0d                   AB...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 24 CalBGForPH 2013-05-08T13:24:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-05-08T13:24:27)
    0000   0x5b 0x58 0x2d 0x08 0x0d                   [X-..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 25 BolusWizard 2013-05-08T13:24:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 3.8,
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
    datetime (2013-05-08T13:24:43)
    0000   0x6b 0x58 0x0d 0x08 0x0d                   kX...
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x08 0x26 0x00    2P.-j.&.
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             50   80   13   45  106    8   38    0
              0    0    0   46  125
    HOUR BITS: [0, 1, 0]
#### RECORD 26 Bolus 2013-05-08T13:24:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-05-08T13:24:43)
    0000   0x6b 0x58 0x4d 0x08 0x0d                   kXM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 27 BolusWizard 2013-05-08T13:52:41 head[2], body[13] op[0x5b]
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
    datetime (2013-05-08T13:52:41)
    0000   0x69 0x74 0x0d 0x08 0x0d                   it...
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             21   80   13   45  106    0   16    0
              0    0    0   16  125
    HOUR BITS: [0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 4.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb8 0x1c 0x04                   \....
    decimal
             92    5  184   28    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-05-08T13:52:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-05-08T13:52:41)
    0000   0x69 0x74 0x4d 0x08 0x0d                   itM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 30 LowReservoir 2013-05-08T14:50:31 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-05-08T14:50:31)
    0000   0x5f 0x72 0x0e 0x08 0x0d                   _r...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 31 PumpSuspend 2013-05-08T15:30:08 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-08T15:30:08)
    0000   0x48 0x5e 0x0f 0x48 0x0d                   H^.H.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 32 PumpResume 2013-05-08T15:31:21 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-08T15:31:21)
    0000   0x55 0x5f 0x0f 0x48 0x0d                   U_.H.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 33 PumpSuspend 2013-05-08T15:32:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-08T15:32:29)
    0000   0x5d 0x60 0x0f 0x48 0x0d                   ]`.H.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 34 PumpResume 2013-05-08T15:37:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-08T15:37:55)
    0000   0x77 0x65 0x0f 0x48 0x0d                   we.H.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 35 PumpSuspend 2013-05-08T15:37:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-08T15:37:57)
    0000   0x79 0x65 0x0f 0x48 0x0d                   ye.H.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 36 PumpResume 2013-05-08T15:40:22 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-08T15:40:22)
    0000   0x56 0x68 0x0f 0x48 0x0d                   Vh.H.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 37 CalBGForPH 2013-05-08T16:03:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-05-08T16:03:20)
    0000   0x54 0x43 0x30 0x08 0x0d                   TC0..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 CalBGForPH 2013-05-08T16:15:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-05-08T16:15:21)
    0000   0x55 0x4f 0x30 0x08 0x0d                   UO0..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 BolusWizard 2013-05-08T16:15:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 85,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 21,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 1.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2013-05-08T16:15:43)
    0000   0x6b 0x4f 0x10 0x08 0x0d                   kO...
    body (13)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0xfb 0x10 0xf0    .P.-j...
    0008   0x00 0x0e 0x00 0x0b 0x7d                   ....}
    decimal
             21   80   13   45  106  251   16  240
              0   14    0   11  125
    HOUR BITS: [0, 1, 0]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 151, 'amount': 1.6, 'curve': 4},
 {'age': 171, 'amount': 4.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x97 0x04 0xb8 0xab 0x04    \.@.....
    decimal
             92    8   64  151    4  184  171    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2013-05-08T16:15:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-05-08T16:15:43)
    0000   0x6b 0x4f 0x50 0x08 0x0d                   kOP..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 42 LowBattery 2013-05-08T19:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-05-08T19:01:00)
    0000   0x40 0x41 0x13 0x08 0x0d                   @A...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 43 Battery 2013-05-08T21:05:10 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-05-08T21:05:10)
    0000   0x4a 0x45 0x15 0x08 0x0d                   JE...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 44 Battery 2013-05-08T21:05:33 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-05-08T21:05:33)
    0000   0x61 0x45 0x15 0x08 0x0d                   aE...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 45 NoDelivery 2013-05-08T21:05:10 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x37 0x07 0x94                        .7..
    decimal
              6   55    7  148
    datetime (2013-05-08T21:05:10)
    0000   0x4a 0x45 0x55 0xa8 0x0d                   JEU..
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1]
#### RECORD 46 Battery 2013-05-08T21:05:51 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-05-08T21:05:51)
    0000   0x73 0x45 0x15 0x08 0x0d                   sE...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 47 ClearAlarm 2013-05-08T21:05:51 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x37                                  .7
    decimal
             12   55
    datetime (2013-05-08T21:05:51)
    0000   0x73 0x45 0x15 0x08 0x0d                   sE...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 48 Battery 2013-05-08T21:06:15 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-05-08T21:06:15)
    0000   0x4f 0x46 0x15 0x08 0x0d                   OF...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 49 LowReservoir 2013-05-08T21:06:16 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 3.1}
```
    op hex (2)
    0000   0x34 0x1f                                  4.
    decimal
             52   31
    datetime (2013-05-08T21:06:16)
    0000   0x50 0x46 0x15 0x08 0x0d                   PF...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 50 Rewind 2013-05-08T21:09:24 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-05-08T21:09:24)
    0000   0x58 0x49 0x15 0x08 0x0d                   XI...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 51 Prime 2013-05-08T21:10:00 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1e                   .....
    decimal
              3    0    0    0   30
    datetime (2013-05-08T21:10:00)
    0000   0x40 0x4a 0x35 0x08 0x0d                   @J5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 52 Prime 2013-05-08T21:10:25 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-05-08T21:10:25)
    0000   0x59 0x4a 0x15 0x08 0x0d                   YJ...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 53 CalBGForPH 2013-05-08T21:13:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-05-08T21:13:10)
    0000   0x4a 0x4d 0x35 0x08 0x0d                   JM5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 54 BolusWizard 2013-05-08T21:13:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 156,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
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
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2013-05-08T21:13:15)
    0000   0x4f 0x4d 0x15 0x08 0x0d                   OM...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    0    0    6  125
    HOUR BITS: [0, 1, 0]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 1.1, 'curve': 20},
 {'age': 193, 'amount': 1.6, 'curve': 20},
 {'age': 213, 'amount': 4.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2c 0x2b 0x14 0x40 0xc1 0x14    \.,+.@..
    0008   0xb8 0xd5 0x14                             ...
    decimal
             92   11   44   43   20   64  193   20
            184  213   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-05-08T21:13:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-05-08T21:13:15)
    0000   0x4f 0x4d 0x55 0x08 0x0d                   OMU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 CalBGForPH 2013-05-08T21:40:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-05-08T21:40:12)
    0000   0x4c 0x68 0x35 0x08 0x0d                   Lh5..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 58 BolusWizard 2013-05-08T21:40:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 5,
 '_byte[7]': 0,
 'bg': 151,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.1,
 'carb_input': 67,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 5.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x97                                  [.
    decimal
             91  151
    datetime (2013-05-08T21:40:27)
    0000   0x5b 0x68 0x15 0x08 0x0d                   [h...
    body (13)
    hex
    0000   0x43 0x50 0x0d 0x2d 0x6a 0x05 0x33 0x00    CP.-j.3.
    0008   0x00 0x06 0x00 0x33 0x7d                   ...3}
    decimal
             67   80   13   45  106    5   51    0
              0    6    0   51  125
    HOUR BITS: [0, 1, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 0.6, 'curve': 4},
 {'age': 70, 'amount': 1.1, 'curve': 20},
 {'age': 220, 'amount': 1.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x18 0x24 0x04 0x2c 0x46 0x14    \..$.,F.
    0008   0x40 0xdc 0x14                             @..
    decimal
             92   11   24   36    4   44   70   20
             64  220   20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-05-08T21:40:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1, 'dual_component': '??', 'programmed': 5.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x33 0x33 0x00                        .33.
    decimal
              1   51   51    0
    datetime (2013-05-08T21:40:27)
    0000   0x5b 0x68 0x55 0x08 0x0d                   [hU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 61 MResultTotals (2013, 0, 8, 22, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 8, 22, 5, 0))
    0000   0x00 0x05 0x76 0x48 0x8d                   ..vH.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 Model522ResultTotals 2013-05-09T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-09T00:00:00)
    0000   0x48 0x8d                                  H.
    body (41)
    hex
    0000   0x05 0x00 0x80 0x55 0xa3 0x05 0x00 0x00    ...U....
    0008   0x05 0x76 0x03 0x6e 0x3f 0x02 0x08 0x25    .v.n?..%
    0010   0x00 0x9f 0x02 0x08 0x25 0x01 0xd0 0x59    ....%..Y
    0018   0x00 0x38 0x0b 0x00 0x00 0x00 0x05 0x03    .8......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  128   85  163    5    0    0
              5  118    3  110   63    2    8   37
              0  159    2    8   37    1  208   89
              0   56   11    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 63 CalBGForPH 2013-05-09T00:08:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2013-05-09T00:08:28)
    0000   0x5c 0x48 0x20 0x09 0x0d                   \H ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 64 PumpSuspend 2013-05-09T10:52:50 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-09T10:52:50)
    0000   0x72 0x74 0x0a 0x09 0x0d                   rt...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 65 PumpResume 2013-05-09T11:20:01 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-09T11:20:01)
    0000   0x41 0x54 0x0b 0x09 0x0d                   AT...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 66 CalBGForPH 2013-05-09T11:44:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 286}
```
    op hex (2)
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    datetime (2013-05-09T11:44:06)
    0000   0x46 0x6c 0x2b 0x09 0x8d                   Fl+..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 67 BolusWizard 2013-05-09T11:44:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 35,
 '_byte[7]': 0,
 'bg': 286,
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
    0000   0x5b 0x1e                                  [.
    decimal
             91   30
    datetime (2013-05-09T11:44:09)
    0000   0x49 0x6c 0x0b 0x09 0x0d                   Il...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00 0x00    .Q.-j#..
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
              0   81   13   45  106   35    0    0
              0    0    0   35  125
    HOUR BITS: [0, 1, 1]
#### RECORD 68 Bolus 2013-05-09T11:44:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-05-09T11:44:10)
    0000   0x4a 0x6c 0x4b 0x09 0x0d                   JlK..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 69 BolusWizard 2013-05-09T12:12:24 head[2], body[13] op[0x5b]
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
    datetime (2013-05-09T12:12:24)
    0000   0x58 0x4c 0x0c 0x09 0x0d                   XL...
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [0, 1, 0]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 3.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x1c 0x04                   \....
    decimal
             92    5  140   28    4
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-05-09T12:12:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-05-09T12:12:24)
    0000   0x58 0x4c 0x4c 0x09 0x0d                   XLL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 72 CalBGForPH 2013-05-09T17:03:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-05-09T17:03:57)
    0000   0x79 0x43 0x31 0x09 0x0d                   yC1..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 73 BolusWizard 2013-05-09T17:04:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 39,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 3.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-05-09T17:04:09)
    0000   0x49 0x44 0x11 0x09 0x0d                   ID...
    body (13)
    hex
    0000   0x27 0x50 0x0d 0x2d 0x6a 0xf9 0x1e 0xf0    'P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             39   80   13   45  106  249   30  240
              0    0    0   23  125
    HOUR BITS: [0, 1, 0]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 1.9, 'curve': 20},
 {'age': 64, 'amount': 3.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x2c 0x14 0x8c 0x40 0x14    \.L,..@.
    decimal
             92    8   76   44   20  140   64   20
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2013-05-09T17:04:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2013-05-09T17:04:09)
    0000   0x49 0x44 0x51 0x09 0x0d                   IDQ..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 76 CalBGForPH 2013-05-09T18:28:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 66}
```
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2013-05-09T18:28:39)
    0000   0x67 0x5c 0x32 0x09 0x0d                   g\2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 77 MResultTotals (2013, 0, 9, 4, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 9, 4, 4, 0))
    0000   0x00 0x04 0xa4 0x49 0x8d                   ...I.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 78 Model522ResultTotals 2013-05-10T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-10T00:00:00)
    0000   0x49 0x8d                                  I.
    body (41)
    hex
    0000   0x05 0x10 0x93 0x42 0x1e 0x04 0x00 0x00    ...B....
    0008   0x04 0xa4 0x03 0x70 0x4a 0x01 0x34 0x1a    ...pJ.4.
    0010   0x00 0x40 0x01 0x34 0x1a 0x00 0xa8 0x37    .@.4...7
    0018   0x00 0x8c 0x2d 0x00 0x00 0x00 0x03 0x02    ..-.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  147   66   30    4    0    0
              4  164    3  112   74    1   52   26
              0   64    1   52   26    0  168   55
              0  140   45    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 79 PumpSuspend 2013-05-10T12:53:02 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-10T12:53:02)
    0000   0x42 0x75 0x0c 0x0a 0x0d                   Bu...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 80 PumpResume 2013-05-10T13:18:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-10T13:18:37)
    0000   0x65 0x52 0x0d 0x0a 0x0d                   eR...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 81 CalBGForPH 2013-05-10T13:43:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-05-10T13:43:08)
    0000   0x48 0x6b 0x2d 0x0a 0x0d                   Hk-..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 82 BolusWizard 2013-05-10T13:43:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
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
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-05-10T13:43:11)
    0000   0x4b 0x6b 0x0d 0x0a 0x0d                   Kk...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125
    HOUR BITS: [0, 1, 1]
#### RECORD 83 Bolus 2013-05-10T13:43:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-05-10T13:43:11)
    0000   0x4b 0x6b 0x4d 0x0a 0x0d                   KkM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 84 CalBGForPH 2013-05-10T15:50:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2013-05-10T15:50:20)
    0000   0x54 0x72 0x2f 0x0a 0x0d                   Tr/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 85 CalBGForPH 2013-05-10T15:50:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-05-10T15:50:55)
    0000   0x77 0x72 0x2f 0x0a 0x0d                   wr/..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 86 BolusWizard 2013-05-10T15:51:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-05-10T15:51:20)
    0000   0x54 0x73 0x0f 0x0a 0x0d                   Ts...
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x00 0x27 0x00    3P.-j.'.
    0008   0x00 0x05 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106    0   39    0
              0    5    0   39  125
    HOUR BITS: [0, 1, 1]
#### RECORD 87 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 127, 'amount': 0.1, 'curve': 4},
 {'age': 137, 'amount': 1.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x04 0x7f 0x04 0x30 0x89 0x04    \....0..
    decimal
             92    8    4  127    4   48  137    4
    datetime (unknown)

    body (0)

#### RECORD 88 Bolus 2013-05-10T15:51:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-05-10T15:51:20)
    0000   0x54 0x73 0x4f 0x0a 0x0d                   TsO..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 89 CalBGForPH 2013-05-10T18:48:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 64}
```
    op hex (2)
    0000   0x0a 0x40                                  .@
    decimal
             10   64
    datetime (2013-05-10T18:48:34)
    0000   0x62 0x70 0x32 0x0a 0x0d                   bp2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 90 CalBGForPH 2013-05-10T18:48:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 64}
```
    op hex (2)
    0000   0x0a 0x40                                  .@
    decimal
             10   64
    datetime (2013-05-10T18:48:59)
    0000   0x7b 0x70 0x32 0x0a 0x0d                   {p2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 91 MResultTotals (2013, 0, 10, 2, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 10, 2, 4, 0))
    0000   0x00 0x04 0x42 0x4a 0x8d                   ..BJ.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-20.data: 92 records`
