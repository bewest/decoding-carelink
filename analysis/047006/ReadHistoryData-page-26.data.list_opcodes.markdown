## START analysis/xiali/raw//ReadHistoryData-page-26.data
#### STOPPING DOUBLE NULLS @ 1015, found 7 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x76 0xe9                                  v.
##### DEBUG DECIMAL
            118  233
#### RECORD 0 BolusWizard 2013-03-09T18:11:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.9,
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
    datetime (2013-03-09T18:11:21)
    0000   0x15 0xcb 0x12 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125
    HOUR BITS: [1, 1, 0]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 3.6, 'curve': 4},
 {'age': 1, 'amount': 1.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x90 0x11 0x04 0x40 0x01 0x14    \....@..
    decimal
             92    8  144   17    4   64    1   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-03-09T18:11:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-03-09T18:11:21)
    0000   0x15 0xcb 0x52 0x09 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-03-09T19:42:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-03-09T19:42:07)
    0000   0x07 0xea 0x33 0x09 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 CalBGForPH 2013-03-09T19:42:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-03-09T19:42:26)
    0000   0x1a 0xea 0x33 0x09 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 BolusWizard 2013-03-09T19:42:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 199,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 33,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc7                                  [.
    decimal
             91  199
    datetime (2013-03-09T19:42:34)
    0000   0x22 0xea 0x13 0x09 0x0d                   "....
    body (13)
    hex
    0000   0x21 0x50 0x0d 0x2d 0x6a 0x10 0x19 0x00    !P.-j...
    0008   0x00 0x19 0x00 0x19 0x7d                   ....}
    decimal
             33   80   13   45  106   16   25    0
              0   25    0   25  125
    HOUR BITS: [1, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 0.9, 'curve': 4},
 {'age': 108, 'amount': 3.6, 'curve': 4},
 {'age': 92, 'amount': 1.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x24 0x62 0x04 0x90 0x6c 0x04    \.$b..l.
    0008   0x40 0x5c 0x14                             @\.
    decimal
             92   11   36   98    4  144  108    4
             64   92   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-03-09T19:42:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-03-09T19:42:34)
    0000   0x22 0xea 0x53 0x09 0x0d                   ".S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BolusWizard 2013-03-09T19:50:16 head[2], body[13] op[0x5b]
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
    datetime (2013-03-09T19:50:16)
    0000   0x10 0xf2 0x13 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [1, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 0.35, 'curve': 4},
 {'age': 16, 'amount': 2.15, 'curve': 4},
 {'age': 106, 'amount': 0.9, 'curve': 4},
 {'age': 116, 'amount': 3.6, 'curve': 4},
 {'age': 100, 'amount': 1.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x0e 0x06 0x04 0x56 0x10 0x04    \....V..
    0008   0x24 0x6a 0x04 0x90 0x74 0x04 0x40 0x64    $j..t.@d
    0010   0x14                                       .
    decimal
             92   17   14    6    4   86   16    4
             36  106    4  144  116    4   64  100
             20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-03-09T19:50:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-03-09T19:50:16)
    0000   0x10 0xf2 0x53 0x09 0x0d                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 CalBGForPH 2013-03-09T21:15:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2013-03-09T21:15:23)
    0000   0x17 0xcf 0x35 0x09 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 BolusWizard 2013-03-09T21:19:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 9,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.6,
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
    datetime (2013-03-09T21:19:03)
    0000   0x03 0xd3 0x15 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x09 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              9   80   13   45  106    0    6    0
              0    0    0    6  125
    HOUR BITS: [1, 1, 0]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 95, 'amount': 1.55, 'curve': 4},
 {'age': 105, 'amount': 2.15, 'curve': 4},
 {'age': 195, 'amount': 0.9, 'curve': 4},
 {'age': 205, 'amount': 3.6, 'curve': 4},
 {'age': 189, 'amount': 1.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x3e 0x5f 0x04 0x56 0x69 0x04    \.>_.Vi.
    0008   0x24 0xc3 0x04 0x90 0xcd 0x04 0x40 0xbd    $.....@.
    0010   0x14                                       .
    decimal
             92   17   62   95    4   86  105    4
             36  195    4  144  205    4   64  189
             20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-03-09T21:19:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-03-09T21:19:03)
    0000   0x03 0xd3 0x55 0x09 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 MResultTotals 2013-03-10T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x4a                   ....J
    decimal
              7    0    0    5   74
    datetime (2013-03-10T00:00:00)
    0000   0x29 0x8d                                  ).
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 Model522ResultTotals 2013-03-10T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-10T00:00:00)
    0000   0x29 0x8d                                  ).
    body (41)
    hex
    0000   0x05 0x00 0x9f 0x46 0xc7 0x06 0x00 0x00    ...F....
    0008   0x05 0x4a 0x03 0x76 0x41 0x01 0xd4 0x23    .J.vA..#
    0010   0x00 0x92 0x01 0xd4 0x23 0x01 0x94 0x56    ....#..V
    0018   0x00 0x40 0x0e 0x00 0x00 0x00 0x07 0x05    .@......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  159   70  199    6    0    0
              5   74    3  118   65    1  212   35
              0  146    1  212   35    1  148   86
              0   64   14    0    0    0    7    5
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 17 PumpSuspend 2013-03-10T07:50:45 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-10T07:50:45)
    0000   0x2d 0xf2 0x07 0x0a 0x0d                   -....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 PumpResume 2013-03-10T08:04:41 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-10T08:04:41)
    0000   0x29 0xc4 0x08 0x0a 0x0d                   )....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 CalBGForPH 2013-03-10T08:16:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 301}
```
    op hex (2)
    0000   0x0a 0x2d                                  .-
    decimal
             10   45
    datetime (2013-03-10T08:16:05)
    0000   0x05 0xd0 0x28 0x0a 0x8d                   ..(..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 BolusWizard 2013-03-10T08:16:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 39,
 '_byte[7]': 0,
 'bg': 301,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
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
    0000   0x5b 0x2d                                  [-
    decimal
             91   45
    datetime (2013-03-10T08:16:07)
    0000   0x07 0xd0 0x08 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x27 0x00 0x00    .Q.-j'..
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
              0   81   13   45  106   39    0    0
              0    0    0   39  125
    HOUR BITS: [1, 1, 0]
#### RECORD 21 Bolus 2013-03-10T08:16:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-03-10T08:16:07)
    0000   0x07 0xd0 0x48 0x0a 0x0d                   ..H..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 ChangeTimeDisplay 2013-03-10T10:59:17 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-03-10T10:59:17)
    0000   0x11 0xfb 0x0a 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 23 ChangeTime 2013-03-10T10:59:26 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-03-10T10:59:26)
    0000   0x1a 0xfb 0x0a 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 NewTimeSet 2013-03-10T11:59:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-03-10T11:59:00)
    0000   0x00 0xfb 0x0b 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 CalBGForPH 2013-03-10T13:24:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-03-10T13:24:56)
    0000   0x38 0xd8 0x2d 0x0a 0x0d                   8.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 26 BolusWizard 2013-03-10T13:25:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
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
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-03-10T13:25:24)
    0000   0x18 0xd9 0x0d 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [1, 1, 0]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 251, 'amount': 3.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0xfb 0x04                   \....
    decimal
             92    5  156  251    4
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-03-10T13:25:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-03-10T13:25:24)
    0000   0x18 0xd9 0x4d 0x0a 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 29 CalBGForPH 2013-03-10T14:12:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-03-10T14:12:31)
    0000   0x1f 0xcc 0x2e 0x0a 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 BolusWizard 2013-03-10T14:13:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-03-10T14:13:00)
    0000   0x00 0xcd 0x0e 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    <P.-j...
    0008   0x00 0x0b 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106    0   46    0
              0   11    0   46  125
    HOUR BITS: [1, 1, 0]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 1.2, 'curve': 4},
 {'age': 43, 'amount': 3.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x31 0x04 0x9c 0x2b 0x14    \.01..+.
    decimal
             92    8   48   49    4  156   43   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-03-10T14:13:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-03-10T14:13:00)
    0000   0x00 0xcd 0x4e 0x0a 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 CalBGForPH 2013-03-10T15:47:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-03-10T15:47:27)
    0000   0x1b 0xef 0x2f 0x0a 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 CalBGForPH 2013-03-10T17:31:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 266}
```
    op hex (2)
    0000   0x0a 0x0a                                  ..
    decimal
             10   10
    datetime (2013-03-10T17:31:50)
    0000   0x32 0xdf 0x31 0x0a 0x8d                   2.1..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 35 BolusWizard 2013-03-10T17:31:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 266,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0a                                  [.
    decimal
             91   10
    datetime (2013-03-10T17:31:55)
    0000   0x37 0xdf 0x11 0x0a 0x0d                   7....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x06 0x00 0x19 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    6    0   25  125
    HOUR BITS: [1, 1, 0]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 197, 'amount': 3.1, 'curve': 4},
 {'age': 207, 'amount': 1.5, 'curve': 4},
 {'age': 247, 'amount': 1.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x7c 0xc5 0x04 0x3c 0xcf 0x04    \.|..<..
    0008   0x30 0xf7 0x04                             0..
    decimal
             92   11  124  197    4   60  207    4
             48  247    4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2013-03-10T17:31:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-03-10T17:31:55)
    0000   0x37 0xdf 0x51 0x0a 0x0d                   7.Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 38 LowReservoir 2013-03-10T17:33:40 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-10T17:33:40)
    0000   0x28 0xe1 0x11 0x0a 0x0d                   (....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 CalBGForPH 2013-03-10T19:40:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-03-10T19:40:51)
    0000   0x33 0xe8 0x33 0x0a 0x0d                   3.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 CalBGForPH 2013-03-10T19:41:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-03-10T19:41:14)
    0000   0x0e 0xe9 0x33 0x0a 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 BolusWizard 2013-03-10T19:41:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-03-10T19:41:31)
    0000   0x1f 0xe9 0x13 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0x00 0x16 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x16 0x7d                   ....}
    decimal
             29   80   13   45  106    0   22    0
              0    9    0   22  125
    HOUR BITS: [1, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 2.5, 'curve': 4},
 {'age': 71, 'amount': 3.1, 'curve': 20},
 {'age': 81, 'amount': 1.5, 'curve': 20},
 {'age': 121, 'amount': 1.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x64 0x89 0x04 0x7c 0x47 0x14    \.d..|G.
    0008   0x3c 0x51 0x14 0x30 0x79 0x14              <Q.0y.
    decimal
             92   14  100  137    4  124   71   20
             60   81   20   48  121   20
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-03-10T19:41:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-03-10T19:41:31)
    0000   0x1f 0xe9 0x53 0x0a 0x0d                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 CalBGForPH 2013-03-10T21:34:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2013-03-10T21:34:08)
    0000   0x08 0xe2 0x35 0x0a 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 CalBGForPH 2013-03-10T22:02:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-03-10T22:02:32)
    0000   0x20 0xc2 0x36 0x0a 0x0d                    .6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 46 MResultTotals 2013-03-11T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x90                   .....
    decimal
              7    0    0    5  144
    datetime (2013-03-11T00:00:00)
    0000   0x2a 0x8d                                  *.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 47 Model522ResultTotals 2013-03-11T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-11T00:00:00)
    0000   0x2a 0x8d                                  *.
    body (41)
    hex
    0000   0x05 0x10 0xa2 0x67 0x2d 0x09 0x00 0x00    ...g-...
    0008   0x05 0x90 0x03 0x50 0x3c 0x02 0x40 0x28    ...P<.@(
    0010   0x00 0x69 0x02 0x40 0x28 0x01 0x40 0x38    .i.@(.@8
    0018   0x01 0x00 0x2c 0x00 0x00 0x00 0x05 0x03    ..,.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  162  103   45    9    0    0
              5  144    3   80   60    2   64   40
              0  105    2   64   40    1   64   56
              1    0   44    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 48 LowReservoir 2013-03-11T02:03:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-03-11T02:03:45)
    0000   0x2d 0xc3 0x02 0x0b 0x0d                   -....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 CalBGForPH 2013-03-11T11:13:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 228}
```
    op hex (2)
    0000   0x0a 0xe4                                  ..
    decimal
             10  228
    datetime (2013-03-11T11:13:06)
    0000   0x06 0xcd 0x2b 0x0b 0x0d                   ..+..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 BolusWizard 2013-03-11T11:13:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 228,
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
    0000   0x5b 0xe4                                  [.
    decimal
             91  228
    datetime (2013-03-11T11:13:09)
    0000   0x09 0xcd 0x0b 0x0b 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    0    0   22  125
    HOUR BITS: [1, 1, 0]
#### RECORD 51 Bolus 2013-03-11T11:13:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-03-11T11:13:09)
    0000   0x09 0xcd 0x4b 0x0b 0x0d                   ..K..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 52 Rewind 2013-03-11T14:24:21 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-03-11T14:24:21)
    0000   0x15 0xd8 0x0e 0x0b 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 Prime 2013-03-11T14:27:25 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1d                   .....
    decimal
              3    0    0    0   29
    datetime (2013-03-11T14:27:25)
    0000   0x19 0xdb 0x2e 0x0b 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 54 Prime 2013-03-11T14:27:55 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-03-11T14:27:55)
    0000   0x37 0xdb 0x0e 0x0b 0x0d                   7....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 CalBGForPH 2013-03-11T14:39:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2013-03-11T14:39:39)
    0000   0x27 0xe7 0x2e 0x0b 0x0d                   '....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 56 BolusWizard 2013-03-11T14:40:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 71,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2013-03-11T14:40:00)
    0000   0x00 0xe8 0x0e 0x0b 0x0d                   .....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0xf8 0x21 0xf0    ,P.-j.!.
    0008   0x00 0x03 0x00 0x19 0x7d                   ....}
    decimal
             44   80   13   45  106  248   33  240
              0    3    0   25  125
    HOUR BITS: [1, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 206, 'amount': 0.95, 'curve': 4},
 {'age': 216, 'amount': 1.25, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x26 0xce 0x04 0x32 0xd8 0x04    \.&..2..
    decimal
             92    8   38  206    4   50  216    4
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-03-11T14:40:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-03-11T14:40:00)
    0000   0x00 0xe8 0x4e 0x0b 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 59 CalBGForPH 2013-03-11T19:11:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-03-11T19:11:46)
    0000   0x2e 0xcb 0x33 0x0b 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 60 CalBGForPH 2013-03-11T19:15:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-03-11T19:15:06)
    0000   0x06 0xcf 0x33 0x0b 0x0d                   ..3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 61 CalBGForPH 2013-03-11T19:15:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-03-11T19:15:37)
    0000   0x25 0xcf 0x33 0x0b 0x0d                   %.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 BolusWizard 2013-03-11T19:15:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 95,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2013-03-11T19:15:50)
    0000   0x32 0xcf 0x13 0x0b 0x0d                   2....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xfd 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             55   80   13   45  106  253   42  240
              0    0    0   39  125
    HOUR BITS: [1, 1, 0]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 2.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x64 0x19 0x14                   \.d..
    decimal
             92    5  100   25   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-03-11T19:15:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-03-11T19:15:51)
    0000   0x33 0xcf 0x53 0x0b 0x0d                   3.S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 CalBGForPH 2013-03-11T20:36:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2013-03-11T20:36:19)
    0000   0x13 0xe4 0x34 0x0b 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 CalBGForPH 2013-03-11T20:39:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-03-11T20:39:14)
    0000   0x0e 0xe7 0x34 0x0b 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 CalBGForPH 2013-03-11T21:14:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 164}
```
    op hex (2)
    0000   0x0a 0xa4                                  ..
    decimal
             10  164
    datetime (2013-03-11T21:14:38)
    0000   0x26 0xce 0x35 0x0b 0x0d                   &.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 BolusWizard 2013-03-11T21:14:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 164,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 52,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa4                                  [.
    decimal
             91  164
    datetime (2013-03-11T21:14:56)
    0000   0x38 0xce 0x15 0x0b 0x0d                   8....
    body (13)
    hex
    0000   0x34 0x50 0x0d 0x2d 0x6a 0x08 0x28 0x00    4P.-j.(.
    0008   0x00 0x12 0x00 0x28 0x7d                   ...(}
    decimal
             52   80   13   45  106    8   40    0
              0   18    0   40  125
    HOUR BITS: [1, 1, 0]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 120, 'amount': 3.9, 'curve': 4},
 {'age': 144, 'amount': 2.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x9c 0x78 0x04 0x64 0x90 0x14    \..x.d..
    decimal
             92    8  156  120    4  100  144   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-03-11T21:14:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-03-11T21:14:56)
    0000   0x38 0xce 0x55 0x0b 0x0d                   8.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 71 MResultTotals 2013-03-12T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x7a                   ....z
    decimal
              7    0    0    5  122
    datetime (2013-03-12T00:00:00)
    0000   0x2b 0x8d                                  +.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 72 Model522ResultTotals 2013-03-12T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-12T00:00:00)
    0000   0x2b 0x8d                                  +.
    body (41)
    hex
    0000   0x05 0x00 0x85 0x47 0xe4 0x08 0x00 0x00    ...G....
    0008   0x05 0x7a 0x03 0x82 0x40 0x01 0xf8 0x24    .z..@..$
    0010   0x00 0x97 0x01 0xf8 0x24 0x01 0xa0 0x53    ....$..S
    0018   0x00 0x58 0x11 0x00 0x00 0x00 0x04 0x03    .X......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  133   71  228    8    0    0
              5  122    3  130   64    1  248   36
              0  151    1  248   36    1  160   83
              0   88   17    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 73 CalBGForPH 2013-03-12T09:34:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2013-03-12T09:34:49)
    0000   0x31 0xe2 0x29 0x0c 0x0d                   1.)..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 74 BolusWizard 2013-03-12T09:34:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 189,
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
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2013-03-12T09:34:52)
    0000   0x34 0xe2 0x09 0x0c 0x0d                   4....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125
    HOUR BITS: [1, 1, 1]
#### RECORD 75 Bolus 2013-03-12T09:34:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-03-12T09:34:52)
    0000   0x34 0xe2 0x49 0x0c 0x0d                   4.I..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 76 CalBGForPH 2013-03-12T12:38:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 162}
```
    op hex (2)
    0000   0x0a 0xa2                                  ..
    decimal
             10  162
    datetime (2013-03-12T12:38:02)
    0000   0x02 0xe6 0x2c 0x0c 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 77 BolusWizard 2013-03-12T12:38:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 162,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa2                                  [.
    decimal
             91  162
    datetime (2013-03-12T12:38:06)
    0000   0x06 0xe6 0x0c 0x0c 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    3    0    5  125
    HOUR BITS: [1, 1, 1]
#### RECORD 78 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 184, 'amount': 1.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0xb8 0x04                   \.8..
    decimal
             92    5   56  184    4
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2013-03-12T12:38:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-03-12T12:38:06)
    0000   0x06 0xe6 0x4c 0x0c 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 80 PumpSuspend 2013-03-12T12:46:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-12T12:46:30)
    0000   0x1e 0xee 0x0c 0x0c 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 81 PumpResume 2013-03-12T13:14:24 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-12T13:14:24)
    0000   0x18 0xce 0x0d 0x0c 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 82 CalBGForPH 2013-03-12T13:43:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-03-12T13:43:49)
    0000   0x31 0xeb 0x2d 0x0c 0x0d                   1.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 83 BolusWizard 2013-03-12T13:44:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2013-03-12T13:44:22)
    0000   0x16 0xec 0x0d 0x0c 0x0d                   .....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x04 0x20 0x00    *P.-j. .
    0008   0x00 0x04 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106    4   32    0
              0    4    0   32  125
    HOUR BITS: [1, 1, 1]
#### RECORD 84 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 70, 'amount': 0.5, 'curve': 4},
 {'age': 250, 'amount': 1.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x46 0x04 0x38 0xfa 0x04    \..F.8..
    decimal
             92    8   20   70    4   56  250    4
    datetime (unknown)

    body (0)

#### RECORD 85 Bolus 2013-03-12T13:44:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-03-12T13:44:22)
    0000   0x16 0xec 0x4d 0x0c 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 86 BolusWizard 2013-03-12T14:30:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.5,
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
    datetime (2013-03-12T14:30:37)
    0000   0x25 0xde 0x0e 0x0c 0x0d                   %....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0x00 0x23 0x00    .P.-j.#.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             46   80   13   45  106    0   35    0
              0    0    0   35  125
    HOUR BITS: [1, 1, 0]
`end analysis/xiali/raw//ReadHistoryData-page-26.data: 87 records`
