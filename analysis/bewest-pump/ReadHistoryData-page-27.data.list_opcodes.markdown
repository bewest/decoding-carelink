## START logs/ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 1016, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xdb 0xdf                                  ..
##### DEBUG DECIMAL
            219  223
#### RECORD 0 Bolus 2013-03-06T08:05:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x38 0x38 0x00                        .88.
    decimal
              1   56   56    0
    datetime (2013-03-06T08:05:15)
    0000   0x0f 0xc5 0x48 0x06 0x0d                   ..H..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 PumpSuspend 2013-03-06T13:40:25 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-06T13:40:25)
    0000   0x19 0xe8 0x0d 0x06 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 PumpResume 2013-03-06T14:07:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-06T14:07:46)
    0000   0x2e 0xc7 0x0e 0x06 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-06T14:42:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-03-06T14:42:23)
    0000   0x17 0xea 0x2e 0x06 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 BolusWizard 2013-03-06T14:42:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 3.4,
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
    datetime (2013-03-06T14:42:55)
    0000   0x37 0xea 0x0e 0x06 0x0d                   7....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0xfe 0x22 0xf0    -P.-j.".
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             45   80   13   45  106  254   34  240
              0    0    0   32  125
    HOUR BITS: [1, 1, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 142, 'amount': 5.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xe0 0x8e 0x14                   \....
    decimal
             92    5  224  142   20
    datetime (unknown)

    body (0)

#### RECORD 6 LowReservoir 2013-03-06T14:43:04 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-03-06T14:43:04)
    0000   0x04 0xeb 0x0e 0x06 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 Bolus 2013-03-06T14:42:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-03-06T14:42:56)
    0000   0x38 0xea 0x4e 0x06 0x0d                   8.N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BolusWizard 2013-03-06T16:26:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
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
    datetime (2013-03-06T16:26:55)
    0000   0x37 0xda 0x10 0x06 0x0d                   7....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [1, 1, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 1.6, 'curve': 4},
 {'age': 112, 'amount': 1.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0x66 0x04 0x40 0x70 0x04    \.@f.@p.
    decimal
             92    8   64  102    4   64  112    4
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-03-06T16:26:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-03-06T16:26:55)
    0000   0x37 0xda 0x50 0x06 0x0d                   7.P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 CalBGForPH 2013-03-06T17:20:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-03-06T17:20:27)
    0000   0x1b 0xd4 0x31 0x06 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2013-03-06T20:15:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-03-06T20:15:04)
    0000   0x04 0xcf 0x34 0x06 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 CalBGForPH 2013-03-06T20:27:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2013-03-06T20:27:27)
    0000   0x1b 0xdb 0x34 0x06 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 BolusWizard 2013-03-06T20:28:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 125,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 17,
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
    0000   0x5b 0x7d                                  [}
    decimal
             91  125
    datetime (2013-03-06T20:28:14)
    0000   0x0e 0xdc 0x14 0x06 0x0d                   .....
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             17   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [1, 1, 0]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 244, 'amount': 1.2, 'curve': 4},
 {'age': 88, 'amount': 1.6, 'curve': 20},
 {'age': 98, 'amount': 1.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0xf4 0x04 0x40 0x58 0x14    \.0..@X.
    0008   0x40 0x62 0x14                             @b.
    decimal
             92   11   48  244    4   64   88   20
             64   98   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-03-06T20:28:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-03-06T20:28:14)
    0000   0x0e 0xdc 0x54 0x06 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 ResultTotals 2013-02-06T13:13:38 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x34                   ....4
    decimal
              7    0    0    5   52
    datetime (2013-02-06T13:13:38)
    0000   0x26 0x8d 0x6d 0x26 0x8d                   &.m&.
    body (41)
    hex
    0000   0x05 0x10 0x9f 0x48 0x79 0x05 0x00 0x00    ...Hy...
    0008   0x05 0x34 0x03 0x70 0x42 0x01 0xc4 0x22    .4.pB.."
    0010   0x00 0x4e 0x01 0xc4 0x22 0x00 0xe4 0x32    .N.."..2
    0018   0x00 0xe0 0x32 0x00 0x00 0x00 0x04 0x03    ..2.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  159   72  121    5    0    0
              5   52    3  112   66    1  196   34
              0   78    1  196   34    0  228   50
              0  224   50    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 PumpSuspend 2013-03-07T11:16:59 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-07T11:16:59)
    0000   0x3b 0xd0 0x0b 0x07 0x0d                   ;....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 PumpResume 2013-03-07T11:35:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-07T11:35:40)
    0000   0x28 0xe3 0x0b 0x07 0x0d                   (....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 Rewind 2013-03-07T12:17:02 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-03-07T12:17:02)
    0000   0x02 0xd1 0x0c 0x07 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 21 Prime 2013-03-07T12:20:17 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x19                   .....
    decimal
              3    0    0    0   25
    datetime (2013-03-07T12:20:17)
    0000   0x11 0xd4 0x2c 0x07 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 Prime 2013-03-07T12:20:38 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-03-07T12:20:38)
    0000   0x26 0xd4 0x0c 0x07 0x0d                   &....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 CalBGForPH 2013-03-07T12:21:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2013-03-07T12:21:09)
    0000   0x09 0xd5 0x2c 0x07 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 BolusWizard 2013-03-07T12:21:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 253,
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
    0000   0x5b 0xfd                                  [.
    decimal
             91  253
    datetime (2013-03-07T12:21:22)
    0000   0x16 0xd5 0x0c 0x07 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    0    0   28  125
    HOUR BITS: [1, 1, 0]
#### RECORD 25 Bolus 2013-03-07T12:21:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-03-07T12:21:22)
    0000   0x16 0xd5 0x4c 0x07 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 26 CalBGForPH 2013-03-07T13:23:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2013-03-07T13:23:57)
    0000   0x39 0xd7 0x2d 0x07 0x0d                   9.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 BolusWizard 2013-03-07T13:25:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 165,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa5                                  [.
    decimal
             91  165
    datetime (2013-03-07T13:25:11)
    0000   0x0b 0xd9 0x0d 0x07 0x0d                   .....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x08 0x15 0x00    .P.-j...
    0008   0x00 0x1a 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    8   21    0
              0   26    0   21  125
    HOUR BITS: [1, 1, 0]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 3.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x84 0x47 0x04                   \..G.
    decimal
             92    5  132   71    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-03-07T13:25:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-03-07T13:25:11)
    0000   0x0b 0xd9 0x4d 0x07 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 BolusWizard 2013-03-07T14:18:34 head[2], body[13] op[0x5b]
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
    datetime (2013-03-07T14:18:34)
    0000   0x22 0xd2 0x0e 0x07 0x0d                   "....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125
    HOUR BITS: [1, 1, 0]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 2.1, 'curve': 4},
 {'age': 124, 'amount': 3.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x54 0x36 0x04 0x84 0x7c 0x04    \.T6..|.
    decimal
             92    8   84   54    4  132  124    4
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-03-07T14:18:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-03-07T14:18:34)
    0000   0x22 0xd2 0x4e 0x07 0x0d                   ".N..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 CalBGForPH 2013-03-07T17:07:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-03-07T17:07:39)
    0000   0x27 0xc7 0x31 0x07 0x0d                   '.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 34 BolusWizard 2013-03-07T17:07:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 172,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2013-03-07T17:07:42)
    0000   0x2a 0xc7 0x11 0x07 0x0d                   *....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    5    0    5  125
    HOUR BITS: [1, 1, 0]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 1.5, 'curve': 4},
 {'age': 223, 'amount': 2.1, 'curve': 4},
 {'age': 37, 'amount': 3.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0xad 0x04 0x54 0xdf 0x04    \.<..T..
    0008   0x84 0x25 0x14                             .%.
    decimal
             92   11   60  173    4   84  223    4
            132   37   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-03-07T17:07:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-03-07T17:07:42)
    0000   0x2a 0xc7 0x51 0x07 0x0d                   *.Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 CalBGForPH 2013-03-07T17:43:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-03-07T17:43:42)
    0000   0x2a 0xeb 0x31 0x07 0x0d                   *.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 CalBGForPH 2013-03-07T17:46:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-03-07T17:46:05)
    0000   0x05 0xee 0x31 0x07 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 CalBGForPH 2013-03-07T18:38:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 173}
```
    op hex (2)
    0000   0x0a 0xad                                  ..
    decimal
             10  173
    datetime (2013-03-07T18:38:38)
    0000   0x26 0xe6 0x32 0x07 0x0d                   &.2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 BolusWizard 2013-03-07T18:38:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 173,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.7,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2013-03-07T18:38:54)
    0000   0x36 0xe6 0x12 0x07 0x0d                   6....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x0a 0x32 0x00    AP.-j.2.
    0008   0x00 0x03 0x00 0x39 0x7d                   ...9}
    decimal
             65   80   13   45  106   10   50    0
              0    3    0   57  125
    HOUR BITS: [1, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 0.5, 'curve': 4},
 {'age': 8, 'amount': 1.5, 'curve': 20},
 {'age': 58, 'amount': 2.1, 'curve': 20},
 {'age': 128, 'amount': 3.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x14 0x5e 0x04 0x3c 0x08 0x14    \..^.<..
    0008   0x54 0x3a 0x14 0x84 0x80 0x14              T:....
    decimal
             92   14   20   94    4   60    8   20
             84   58   20  132  128   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-03-07T18:38:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.7, 'dual_component': '??', 'programmed': 5.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x39 0x39 0x00                        .99.
    decimal
              1   57   57    0
    datetime (2013-03-07T18:38:55)
    0000   0x37 0xe6 0x52 0x07 0x0d                   7.R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 43 CalBGForPH 2013-03-07T20:43:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2013-03-07T20:43:27)
    0000   0x1b 0xeb 0x34 0x07 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 CalBGForPH 2013-03-07T22:50:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2013-03-07T22:50:48)
    0000   0x30 0xf2 0x36 0x07 0x0d                   0.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BolusWizard 2013-03-07T22:51:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 155,
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
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2013-03-07T22:51:27)
    0000   0x1b 0xf3 0x16 0x07 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    0    0    6  125
    HOUR BITS: [1, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 1, 'amount': 5.7, 'curve': 20},
 {'age': 91, 'amount': 0.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xe4 0x01 0x14 0x14 0x5b 0x14    \.....[.
    decimal
             92    8  228    1   20   20   91   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-03-07T22:51:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-03-07T22:51:27)
    0000   0x1b 0xf3 0x56 0x07 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 CalBGForPH 2013-03-07T22:58:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-03-07T22:58:38)
    0000   0x26 0xfa 0x36 0x07 0x0d                   &.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 BolusWizard 2013-03-07T22:59:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 156,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 1.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2013-03-07T22:59:16)
    0000   0x10 0xfb 0x16 0x07 0x0d                   .....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x06 0x0f 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    6   15    0
              0   11    0   15  125
    HOUR BITS: [1, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 1.1, 'curve': 4},
 {'age': 9, 'amount': 5.7, 'curve': 20},
 {'age': 99, 'amount': 0.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2c 0x0f 0x04 0xe4 0x09 0x14    \.,.....
    0008   0x14 0x63 0x14                             .c.
    decimal
             92   11   44   15    4  228    9   20
             20   99   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-03-07T22:59:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-03-07T22:59:16)
    0000   0x10 0xfb 0x56 0x07 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 ResultTotals 2013-02-07T13:13:39 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe8                   .....
    decimal
              7    0    0    5  232
    datetime (2013-02-07T13:13:39)
    0000   0x27 0x8d 0x6d 0x27 0x8d                   '.m'.
    body (41)
    hex
    0000   0x05 0x00 0xa0 0x49 0xfd 0x09 0x00 0x00    ...I....
    0008   0x05 0xe8 0x03 0x74 0x3a 0x02 0x74 0x2a    ...t:.t*
    0010   0x00 0x85 0x02 0x74 0x2a 0x01 0x94 0x40    ...t*..@
    0018   0x00 0xe0 0x24 0x00 0x00 0x00 0x07 0x03    ..$.....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  160   73  253    9    0    0
              5  232    3  116   58    2  116   42
              0  133    2  116   42    1  148   64
              0  224   36    0    0    0    7    3
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 53 CalBGForPH 2013-03-08T01:42:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 68}
```
    op hex (2)
    0000   0x0a 0x44                                  .D
    decimal
             10   68
    datetime (2013-03-08T01:42:13)
    0000   0x0d 0xea 0x21 0x08 0x0d                   ..!..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 54 CalBGForPH 2013-03-08T15:00:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2013-03-08T15:00:02)
    0000   0x02 0xc0 0x2f 0x08 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 BolusWizard 2013-03-08T15:00:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 84,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 22,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 1.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x54                                  [T
    decimal
             91   84
    datetime (2013-03-08T15:00:10)
    0000   0x0a 0xc0 0x0f 0x08 0x0d                   .....
    body (13)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0xfb 0x10 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             22   80   13   45  106  251   16  240
              0    0    0   11  125
    HOUR BITS: [1, 1, 0]
#### RECORD 56 Bolus 2013-03-08T15:00:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-03-08T15:00:10)
    0000   0x0a 0xc0 0x4f 0x08 0x0d                   ..O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 57 PumpSuspend 2013-03-08T16:56:35 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-08T16:56:35)
    0000   0x23 0xf8 0x10 0x08 0x0d                   #....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 58 PumpResume 2013-03-08T17:14:48 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-08T17:14:48)
    0000   0x30 0xce 0x11 0x08 0x0d                   0....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 CalBGForPH 2013-03-08T18:19:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2013-03-08T18:19:13)
    0000   0x0d 0xd3 0x32 0x08 0x0d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 60 BolusWizard 2013-03-08T18:19:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2013-03-08T18:19:48)
    0000   0x30 0xd3 0x12 0x08 0x0d                   0....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x01 0x09 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    1    9    0
              0    2    0    9  125
    HOUR BITS: [1, 1, 0]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 205, 'amount': 1.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0xcd 0x04                   \.,..
    decimal
             92    5   44  205    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-03-08T18:19:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-03-08T18:19:48)
    0000   0x30 0xd3 0x52 0x08 0x0d                   0.R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 CalBGForPH 2013-03-08T19:58:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 162}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2013-03-08T19:58:18)
    0000   0x12 0xfa 0x33 0x08 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 64 BolusWizard 2013-03-08T19:58:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 162,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2013-03-08T19:58:34)
    0000   0x22 0xfa 0x13 0x08 0x0d                   "....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x08 0x13 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x16 0x7d                   ....}
    decimal
             25   80   13   45  106    8   19    0
              0    5    0   22  125
    HOUR BITS: [1, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 104, 'amount': 0.9, 'curve': 4},
 {'age': 48, 'amount': 1.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x68 0x04 0x2c 0x30 0x14    \.$h.,0.
    decimal
             92    8   36  104    4   44   48   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-03-08T19:58:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-03-08T19:58:34)
    0000   0x22 0xfa 0x53 0x08 0x0d                   ".S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 CalBGForPH 2013-03-08T20:42:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2013-03-08T20:42:32)
    0000   0x20 0xea 0x34 0x08 0x0d                    .4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 CalBGForPH 2013-03-08T21:18:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2013-03-08T21:18:56)
    0000   0x38 0xd2 0x35 0x08 0x0d                   8.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 69 BolusWizard 2013-03-08T21:19:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 181,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb5                                  [.
    decimal
             91  181
    datetime (2013-03-08T21:19:46)
    0000   0x2e 0xd3 0x15 0x08 0x0d                   .....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x0c 0x20 0x00    *P.-j. .
    0008   0x00 0x11 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106   12   32    0
              0   17    0   32  125
    HOUR BITS: [1, 1, 0]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 2.2, 'curve': 4},
 {'age': 185, 'amount': 0.9, 'curve': 4},
 {'age': 129, 'amount': 1.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x55 0x04 0x24 0xb9 0x04    \.XU.$..
    0008   0x2c 0x81 0x14                             ,..
    decimal
             92   11   88   85    4   36  185    4
             44  129   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2013-03-08T21:19:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-03-08T21:19:46)
    0000   0x2e 0xd3 0x55 0x08 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 ResultTotals 2013-02-08T13:13:40 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xa0                   .....
    decimal
              7    0    0    4  160
    datetime (2013-02-08T13:13:40)
    0000   0x28 0x8d 0x6d 0x28 0x8d                   (.m(.
    body (41)
    hex
    0000   0x05 0x00 0x87 0x44 0xb5 0x06 0x00 0x00    ...D....
    0008   0x04 0xa0 0x03 0x78 0x4b 0x01 0x28 0x19    ...xK.(.
    0010   0x00 0x65 0x01 0x28 0x19 0x01 0x1c 0x60    .e.(...`
    0018   0x00 0x0c 0x04 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  135   68  181    6    0    0
              4  160    3  120   75    1   40   25
              0  101    1   40   25    1   28   96
              0   12    4    0    0    0    4    3
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 73 CalBGForPH 2013-03-09T04:28:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-03-09T04:28:58)
    0000   0x3a 0xdc 0x24 0x09 0x0d                   :.$..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 74 BolusWizard 2013-03-09T04:29:00 head[2], body[13] op[0x5b]
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
    datetime (2013-03-09T04:29:00)
    0000   0x00 0xdd 0x04 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125
    HOUR BITS: [1, 1, 0]
#### RECORD 75 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 179, 'amount': 3.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x80 0xb3 0x14                   \....
    decimal
             92    5  128  179   20
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2013-03-09T04:29:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-03-09T04:29:00)
    0000   0x00 0xdd 0x44 0x09 0x0d                   ..D..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 77 CalBGForPH 2013-03-09T13:59:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-03-09T13:59:16)
    0000   0x10 0xfb 0x2d 0x09 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 78 BolusWizard 2013-03-09T13:59:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 70,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2013-03-09T13:59:36)
    0000   0x24 0xfb 0x0d 0x09 0x0d                   $....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xf8 0x18 0xf0     P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             32   80   13   45  106  248   24  240
              0    0    0   16  125
    HOUR BITS: [1, 1, 1]
#### RECORD 79 Bolus 2013-03-09T13:59:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-03-09T13:59:36)
    0000   0x24 0xfb 0x4d 0x09 0x0d                   $.M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 80 PumpSuspend 2013-03-09T16:09:04 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-09T16:09:04)
    0000   0x04 0xc9 0x10 0x09 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 81 PumpResume 2013-03-09T16:28:32 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-09T16:28:32)
    0000   0x20 0xdc 0x10 0x09 0x0d                    ....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 82 CalBGForPH 2013-03-09T17:56:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2013-03-09T17:56:12)
    0000   0x0c 0xf8 0x31 0x09 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 83 BolusWizard 2013-03-09T17:56:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 141,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8d                                  [.
    decimal
             91  141
    datetime (2013-03-09T17:56:27)
    0000   0x1b 0xf8 0x11 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0x03 0x21 0x00    ,P.-j.!.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             44   80   13   45  106    3   33    0
              0    0    0   36  125
    HOUR BITS: [1, 1, 1]
#### RECORD 84 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 242, 'amount': 1.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0xf2 0x04                   \.@..
    decimal
             92    5   64  242    4
    datetime (unknown)

    body (0)

#### RECORD 85 Bolus 2013-03-09T17:56:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-03-09T17:56:27)
    0000   0x1b 0xf8 0x51 0x09 0x0d                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-27.data: 86 records`
