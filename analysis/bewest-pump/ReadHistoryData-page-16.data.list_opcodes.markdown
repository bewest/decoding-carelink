## START logs/ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xdf 0x80                                  ..
##### DEBUG DECIMAL
            223  128
#### RECORD 0 BolusWizard 2012-11-23T21:56:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 98,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 2.7,
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
    datetime (2012-11-23T21:56:59)
    0000   0xbb 0xf8 0x15 0x17 0x0c                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0xfe 0x1b 0xf0    $P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
             36   80   13   45  106  254   27  240
              0    0    0   25  125
    HOUR BITS: [1, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 156, 'amount': 5.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xdc 0x9c 0x14                   \....
    decimal
             92    5  220  156   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2012-11-23T21:56:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2012-11-23T21:56:59)
    0000   0xbb 0xf8 0x55 0x17 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 BolusWizard 2012-11-23T23:28:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.5,
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
    datetime (2012-11-23T23:28:17)
    0000   0x91 0xdc 0x17 0x17 0x0c                   .....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x00 0x05 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
              7   80   13   45  106    0    5    0
              0    0    0    5  125
    HOUR BITS: [1, 1, 0]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 2.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x64 0x5e 0x04                   \.d^.
    decimal
             92    5  100   94    4
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-11-23T23:28:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-11-23T23:28:17)
    0000   0x91 0xdc 0x57 0x17 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 ResultTotals 2012-10-23T13:12:55 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbe                   .....
    decimal
              7    0    0    4  190
    datetime (2012-10-23T13:12:55)
    0000   0xb7 0x8c 0x6d 0xb7 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x66 0x4d 0x7a 0x05 0x00 0x00    ..fMz...
    0008   0x04 0xbe 0x03 0x6a 0x48 0x01 0x54 0x1c    ...jH.T.
    0010   0x00 0x73 0x01 0x54 0x1c 0x01 0x54 0x64    .s.T..Td
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  102   77  122    5    0    0
              4  190    3  106   72    1   84   28
              0  115    1   84   28    1   84  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 7 CalBGForPH 2012-11-24T12:39:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2012-11-24T12:39:05)
    0000   0x85 0xe7 0x2c 0x18 0x8c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 BolusWizard 2012-11-24T12:39:07 head[2], body[13] op[0x5b]
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
    datetime (2012-11-24T12:39:07)
    0000   0x87 0xe7 0x0c 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    0    0   29  125
    HOUR BITS: [1, 1, 1]
#### RECORD 9 Bolus 2012-11-24T12:39:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-11-24T12:39:07)
    0000   0x87 0xe7 0x4c 0x18 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 CalBGForPH 2012-11-24T18:15:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-11-24T18:15:43)
    0000   0xab 0xcf 0x32 0x18 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 PumpSuspend 2012-11-24T20:21:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-24T20:21:18)
    0000   0x92 0xd5 0x14 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 PumpResume 2012-11-24T20:57:38 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-24T20:57:38)
    0000   0xa6 0xf9 0x14 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 CalBGForPH 2012-11-24T22:18:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2012-11-24T22:18:11)
    0000   0x8b 0xd2 0x36 0x18 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 BolusWizard 2012-11-24T22:18:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 110,
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
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2012-11-24T22:18:28)
    0000   0x9c 0xd2 0x16 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x00 0x2f 0x00    >P.-j./.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             62   80   13   45  106    0   47    0
              0    0    0   47  125
    HOUR BITS: [1, 1, 0]
#### RECORD 15 Bolus 2012-11-24T22:18:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2012-11-24T22:18:28)
    0000   0x9c 0xd2 0x56 0x18 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 16 ResultTotals 2012-10-24T13:12:56 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9c                   .....
    decimal
              7    0    0    4  156
    datetime (2012-10-24T13:12:56)
    0000   0xb8 0x8c 0x6d 0xb8 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x9a 0x60 0x00 0x03 0x00 0x00    ...`....
    0008   0x04 0x9c 0x03 0x6c 0x4a 0x01 0x30 0x1a    ...lJ.0.
    0010   0x00 0x3e 0x01 0x30 0x1a 0x00 0xbc 0x3e    .>.0...>
    0018   0x00 0x74 0x26 0x00 0x00 0x00 0x02 0x01    .t&.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  154   96    0    3    0    0
              4  156    3  108   74    1   48   26
              0   62    1   48   26    0  188   62
              0  116   38    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 CalBGForPH 2012-11-25T02:50:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 343}
```
    op hex (2)
    0000   0x0a 0x57                                  .W
    decimal
             10   87
    datetime (2012-11-25T02:50:28)
    0000   0x9c 0xf2 0x22 0x19 0x8c                   .."..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 BolusWizard 2012-11-25T02:50:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 48,
 '_byte[7]': 0,
 'bg': 343,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
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
    0000   0x5b 0x57                                  [W
    decimal
             91   87
    datetime (2012-11-25T02:50:31)
    0000   0x9f 0xf2 0x02 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x30 0x00 0x00    .Q.-j0..
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
              0   81   13   45  106   48    0    0
              0    0    0   48  125
    HOUR BITS: [1, 1, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 4.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xbc 0x14 0x14                   \....
    decimal
             92    5  188   20   20
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2012-11-25T02:50:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2012-11-25T02:50:31)
    0000   0x9f 0xf2 0x42 0x19 0x0c                   ..B..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 LowReservoir 2012-11-25T03:37:30 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-11-25T03:37:30)
    0000   0x9e 0xe5 0x03 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 22 LowReservoir 2012-11-25T13:54:32 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-11-25T13:54:32)
    0000   0xa0 0xf6 0x0d 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 23 PumpSuspend 2012-11-25T16:41:34 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-25T16:41:34)
    0000   0xa2 0xe9 0x10 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 PumpResume 2012-11-25T17:24:49 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-25T17:24:49)
    0000   0xb1 0xd8 0x11 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 TempBasal 2012-11-25T17:25:19 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.6}
```
    op hex (2)
    0000   0x33 0x18                                  3.
    decimal
             51   24
    datetime (2012-11-25T17:25:19)
    0000   0x93 0xd9 0x11 0x19 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 0]
#### RECORD 26 TempBasalDuration 2012-11-25T17:25:19 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2012-11-25T17:25:19)
    0000   0x93 0xd9 0x11 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 CalBGForPH 2012-11-25T19:31:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 347}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2012-11-25T19:31:13)
    0000   0x8d 0xdf 0x33 0x19 0x8c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 28 BolusWizard 2012-11-25T19:31:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 49,
 '_byte[7]': 0,
 'bg': 347,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2012-11-25T19:31:20)
    0000   0x94 0xdf 0x13 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x31 0x00 0x00    .Q.-j1..
    0008   0x00 0x00 0x00 0x31 0x7d                   ...1}
    decimal
              0   81   13   45  106   49    0    0
              0    0    0   49  125
    HOUR BITS: [1, 1, 0]
#### RECORD 29 Bolus 2012-11-25T19:31:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4, 'dual_component': '??', 'programmed': 5.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x36 0x36 0x00                        .66.
    decimal
              1   54   54    0
    datetime (2012-11-25T19:31:21)
    0000   0x95 0xdf 0x53 0x19 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 PumpSuspend 2012-11-25T19:56:31 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-25T19:56:31)
    0000   0x9f 0xf8 0x13 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 PumpResume 2012-11-25T19:56:32 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-25T19:56:32)
    0000   0xa0 0xf8 0x13 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 Rewind 2012-11-25T19:56:36 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-11-25T19:56:36)
    0000   0xa4 0xf8 0x13 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 Prime 2012-11-25T19:58:14 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2d                   ....-
    decimal
              3    0    0    0   45
    datetime (2012-11-25T19:58:14)
    0000   0x8e 0xfa 0x33 0x19 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 Prime 2012-11-25T19:58:33 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-11-25T19:58:33)
    0000   0xa1 0xfa 0x13 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 CalBGForPH 2012-11-25T20:44:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 301}
```
    op hex (2)
    0000   0x0a 0x2d                                  .-
    decimal
             10   45
    datetime (2012-11-25T20:44:54)
    0000   0xb6 0xec 0x34 0x19 0x8c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 36 BolusWizard 2012-11-25T20:45:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 39,
 '_byte[7]': 0,
 'bg': 301,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 81,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 6.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2d                                  [-
    decimal
             91   45
    datetime (2012-11-25T20:45:33)
    0000   0xa1 0xed 0x14 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x51 0x51 0x0d 0x2d 0x6a 0x27 0x3e 0x00    QQ.-j'>.
    0008   0x00 0x27 0x00 0x3e 0x7d                   .'.>}
    decimal
             81   81   13   45  106   39   62    0
              0   39    0   62  125
    HOUR BITS: [1, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 1.45, 'curve': 4},
 {'age': 81, 'amount': 3.95, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x3a 0x47 0x04 0x9e 0x51 0x04    \.:G..Q.
    decimal
             92    8   58   71    4  158   81    4
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2012-11-25T20:45:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2, 'dual_component': '??', 'programmed': 6.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3e 0x3e 0x00                        .>>.
    decimal
              1   62   62    0
    datetime (2012-11-25T20:45:33)
    0000   0xa1 0xed 0x54 0x19 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 ResultTotals 2012-10-25T13:12:57 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe4                   .....
    decimal
              7    0    0    5  228
    datetime (2012-10-25T13:12:57)
    0000   0xb9 0x8c 0x6d 0xb9 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x15 0x4a 0x2d 0x5b 0x03 0x00 0x00    ..J-[...
    0008   0x05 0xe4 0x03 0x54 0x38 0x02 0x90 0x2c    ...T8..,
    0010   0x00 0x51 0x02 0x90 0x2c 0x00 0xf8 0x26    .Q..,..&
    0018   0x01 0x98 0x3e 0x00 0x00 0x00 0x03 0x01    ..>.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21   74   45   91    3    0    0
              5  228    3   84   56    2  144   44
              0   81    2  144   44    0  248   38
              1  152   62    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 40 CalBGForPH 2012-11-26T00:10:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-11-26T00:10:23)
    0000   0x97 0xca 0x20 0x1a 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 41 CalBGForPH 2012-11-26T00:19:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2012-11-26T00:19:51)
    0000   0xb3 0xd3 0x20 0x1a 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 42 BolusWizard 2012-11-26T00:20:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 95,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 1.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2012-11-26T00:20:22)
    0000   0x96 0xd4 0x00 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0xfd 0x0b 0xf0    .P.-j...
    0008   0x00 0x06 0x00 0x08 0x7d                   ....}
    decimal
             15   80   13   45  106  253   11  240
              0    6    0    8  125
    HOUR BITS: [1, 1, 0]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 216, 'amount': 6.2, 'curve': 4},
 {'age': 30, 'amount': 1.45, 'curve': 20},
 {'age': 40, 'amount': 3.95, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xf8 0xd8 0x04 0x3a 0x1e 0x14    \....:..
    0008   0x9e 0x28 0x14                             .(.
    decimal
             92   11  248  216    4   58   30   20
            158   40   20
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2012-11-26T00:20:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-11-26T00:20:22)
    0000   0x96 0xd4 0x40 0x1a 0x0c                   ..@..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 PumpSuspend 2012-11-26T13:43:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-26T13:43:20)
    0000   0x94 0xeb 0x0d 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 46 PumpResume 2012-11-26T13:59:10 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-26T13:59:10)
    0000   0x8a 0xfb 0x0d 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 47 CalBGForPH 2012-11-26T14:26:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 230}
```
    op hex (2)
    0000   0x0a 0xe6                                  ..
    decimal
             10  230
    datetime (2012-11-26T14:26:21)
    0000   0x95 0xda 0x2e 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 BolusWizard 2012-11-26T14:26:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 230,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe6                                  [.
    decimal
             91  230
    datetime (2012-11-26T14:26:27)
    0000   0x9b 0xda 0x0e 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x17 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
              0   80   13   45  106   23    0    0
              0    0    0   23  125
    HOUR BITS: [1, 1, 0]
#### RECORD 49 Bolus 2012-11-26T14:26:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-11-26T14:26:27)
    0000   0x9b 0xda 0x4e 0x1a 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 CalBGForPH 2012-11-26T15:08:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2012-11-26T15:08:29)
    0000   0x9d 0xc8 0x2f 0x1a 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 51 BolusWizard 2012-11-26T15:31:53 head[2], body[13] op[0x5b]
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
    datetime (2012-11-26T15:31:53)
    0000   0xb5 0xdf 0x0f 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x00 0x1c 0x00    %P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106    0   28    0
              0    0    0   28  125
    HOUR BITS: [1, 1, 0]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0x43 0x04                   \.hC.
    decimal
             92    5  104   67    4
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2012-11-26T15:31:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2012-11-26T15:31:53)
    0000   0xb5 0xdf 0x4f 0x1a 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 54 CalBGForPH 2012-11-26T17:53:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2012-11-26T17:53:44)
    0000   0xac 0xf5 0x31 0x1a 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 55 BolusWizard 2012-11-26T17:54:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 141,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8d                                  [.
    decimal
             91  141
    datetime (2012-11-26T17:54:00)
    0000   0x80 0xf6 0x11 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x03 0x21 0x00    +P.-j.!.
    0008   0x00 0x0b 0x00 0x21 0x7d                   ...!}
    decimal
             43   80   13   45  106    3   33    0
              0   11    0   33  125
    HOUR BITS: [1, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 2.8, 'curve': 4},
 {'age': 210, 'amount': 2.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x70 0x96 0x04 0x68 0xd2 0x04    \.p..h..
    decimal
             92    8  112  150    4  104  210    4
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2012-11-26T17:54:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2012-11-26T17:54:01)
    0000   0x81 0xf6 0x51 0x1a 0x0c                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 58 CalBGForPH 2012-11-26T20:24:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2012-11-26T20:24:06)
    0000   0x86 0xd8 0x34 0x1a 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 BolusWizard 2012-11-26T20:24:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 253,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfd                                  [.
    decimal
             91  253
    datetime (2012-11-26T20:24:13)
    0000   0x8d 0xd8 0x14 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x0a 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0   10    0   18  125
    HOUR BITS: [1, 1, 0]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 3.3, 'curve': 4},
 {'age': 44, 'amount': 2.8, 'curve': 20},
 {'age': 104, 'amount': 2.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x84 0x96 0x04 0x70 0x2c 0x14    \....p,.
    0008   0x68 0x68 0x14                             hh.
    decimal
             92   11  132  150    4  112   44   20
            104  104   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2012-11-26T20:24:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-11-26T20:24:13)
    0000   0x8d 0xd8 0x54 0x1a 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 BolusWizard 2012-11-26T20:40:45 head[2], body[13] op[0x5b]
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
    datetime (2012-11-26T20:40:45)
    0000   0xad 0xe8 0x14 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x00 0x1c 0x00    %P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106    0   28    0
              0    0    0   28  125
    HOUR BITS: [1, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 2.0, 'curve': 4},
 {'age': 166, 'amount': 3.3, 'curve': 4},
 {'age': 60, 'amount': 2.8, 'curve': 20},
 {'age': 120, 'amount': 2.6, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x10 0x04 0x84 0xa6 0x04    \.P.....
    0008   0x70 0x3c 0x14 0x68 0x78 0x14              p<.hx.
    decimal
             92   14   80   16    4  132  166    4
            112   60   20  104  120   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2012-11-26T20:40:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2012-11-26T20:40:45)
    0000   0xad 0xe8 0x54 0x1a 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 65 CalBGForPH 2012-11-26T22:02:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2012-11-26T22:02:02)
    0000   0x82 0xc2 0x36 0x1a 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 66 ResultTotals 2012-10-26T13:12:58 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xa8                   .....
    decimal
              7    0    0    5  168
    datetime (2012-10-26T13:12:58)
    0000   0xba 0x8c 0x6d 0xba 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xa8 0x5f 0xfd 0x07 0x00 0x00    ..._....
    0008   0x05 0xa8 0x03 0x78 0x3d 0x02 0x30 0x27    ...x=.0'
    0010   0x00 0x84 0x02 0x30 0x27 0x01 0x78 0x43    ...0'.xC
    0018   0x00 0xb8 0x21 0x00 0x00 0x00 0x06 0x04    ..!.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  168   95  253    7    0    0
              5  168    3  120   61    2   48   39
              0  132    2   48   39    1  120   67
              0  184   33    0    0    0    6    4
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 67 PumpSuspend 2012-11-27T13:46:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-27T13:46:56)
    0000   0xb8 0xee 0x0d 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 PumpResume 2012-11-27T14:39:28 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-27T14:39:28)
    0000   0x9c 0xe7 0x0e 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 CalBGForPH 2012-11-27T14:41:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2012-11-27T14:41:12)
    0000   0x8c 0xe9 0x2e 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 70 BolusWizard 2012-11-27T14:41:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 198,
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
    0000   0x5b 0xc6                                  [.
    decimal
             91  198
    datetime (2012-11-27T14:41:19)
    0000   0x93 0xe9 0x0e 0x1b 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125
    HOUR BITS: [1, 1, 1]
#### RECORD 71 Bolus 2012-11-27T14:41:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2012-11-27T14:41:19)
    0000   0x93 0xe9 0x4e 0x1b 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 CalBGForPH 2012-11-27T18:49:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2012-11-27T18:49:56)
    0000   0xb8 0xf1 0x32 0x1b 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 73 BolusWizard 2012-11-27T18:50:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2012-11-27T18:50:42)
    0000   0xaa 0xf2 0x12 0x1b 0x0c                   .....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0xfc 0x24 0xf0    /P.-j.$.
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             47   80   13   45  106  252   36  240
              0    0    0   32  125
    HOUR BITS: [1, 1, 1]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 1.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x00 0x14                   \.@..
    decimal
             92    5   64    0   20
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2012-11-27T18:50:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-11-27T18:50:43)
    0000   0xab 0xf2 0x52 0x1b 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 76 ResultTotals 2012-10-27T13:12:59 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x22                   ...."
    decimal
              7    0    0    4   34
    datetime (2012-10-27T13:12:59)
    0000   0xbb 0x8c 0x6d 0xbb 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8f 0x58 0xc6 0x02 0x00 0x00    ...X....
    0008   0x04 0x22 0x03 0x62 0x52 0x00 0xc0 0x12    .".bR...
    0010   0x00 0x2f 0x00 0xc0 0x12 0x00 0x80 0x43    ./.....C
    0018   0x00 0x40 0x21 0x00 0x00 0x00 0x02 0x01    .@!.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  143   88  198    2    0    0
              4   34    3   98   82    0  192   18
              0   47    0  192   18    0  128   67
              0   64   33    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 77 PumpSuspend 2012-11-28T13:58:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-28T13:58:29)
    0000   0x9d 0xfa 0x0d 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 78 PumpResume 2012-11-28T14:16:48 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-28T14:16:48)
    0000   0xb0 0xd0 0x0e 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 CalBGForPH 2012-11-28T15:02:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2012-11-28T15:02:16)
    0000   0x90 0xc2 0x2f 0x1c 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-16.data: 80 records`
