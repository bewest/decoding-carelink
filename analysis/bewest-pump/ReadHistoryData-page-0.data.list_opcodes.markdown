## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 616, found 406 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x45 0x03                                  E.
##### DEBUG DECIMAL
             69    3
#### RECORD 0 BolusWizard 2013-06-15T16:40:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 17,
 '_byte[7]': 0,
 'bg': 202,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 4.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xca                                  [.
    decimal
             91  202
    datetime (2013-06-15T16:40:15)
    0000   0x4f 0xa8 0x10 0x0f 0x0d                   O....
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0x11 0x2d 0x00    ;P.-j.-.
    0008   0x00 0x00 0x00 0x3e 0x7d                   ...>}
    decimal
             59   80   13   45  106   17   45    0
              0    0    0   62  125
    HOUR BITS: [1, 0, 1]
#### RECORD 1 Bolus 2013-06-15T16:40:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.1, 'dual_component': '??', 'programmed': 6.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3d 0x3d 0x00                        .==.
    decimal
              1   61   61    0
    datetime (2013-06-15T16:40:15)
    0000   0x4f 0xa8 0x50 0x0f 0x0d                   O.P..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2013-06-15T18:12:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-06-15T18:12:00)
    0000   0x40 0x8c 0x32 0x0f 0x0d                   @.2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 CalBGForPH 2013-06-15T19:29:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 173}
```
    op hex (2)
    0000   0x0a 0xad                                  ..
    decimal
             10  173
    datetime (2013-06-15T19:29:31)
    0000   0x5f 0x9d 0x33 0x0f 0x0d                   _.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 CalBGForPH 2013-06-15T20:58:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-06-15T20:58:47)
    0000   0x6f 0xba 0x34 0x0f 0x0d                   o.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 5 BolusWizard 2013-06-15T20:59:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 137,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 1.3,
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
    datetime (2013-06-15T20:59:47)
    0000   0x6f 0xbb 0x14 0x0f 0x0d                   o....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x02 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             18   80   13   45  106    2   13    0
              0    0    0   15  125
    HOUR BITS: [1, 0, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 255, 'amount': 0.5, 'curve': 4},
 {'age': 9, 'amount': 5.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0xff 0x04 0xe0 0x09 0x14    \.......
    decimal
             92    8   20  255    4  224    9   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-06-15T20:59:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-06-15T20:59:47)
    0000   0x6f 0xbb 0x54 0x0f 0x0d                   o.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 8 ResultTotals 2013-04-15T13:13:47 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xaa                   .....
    decimal
              7    0    0    4  170
    datetime (2013-04-15T13:13:47)
    0000   0x6f 0x0d 0x6d 0x6f 0x0d                   o.mo.
    body (41)
    hex
    0000   0x05 0x00 0xb0 0x89 0xca 0x04 0x00 0x00    ........
    0008   0x04 0xaa 0x03 0x7a 0x4b 0x01 0x30 0x19    ...zK.0.
    0010   0x00 0x4d 0x01 0x30 0x19 0x00 0xe8 0x4c    .M.0...L
    0018   0x00 0x48 0x18 0x00 0x00 0x00 0x02 0x00    .H......
    0020   0x00 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  176  137  202    4    0    0
              4  170    3  122   75    1   48   25
              0   77    1   48   25    0  232   76
              0   72   24    0    0    0    2    0
              0    2    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 1]
#### RECORD 9 PumpSuspend 2013-06-16T10:00:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-16T10:00:39)
    0000   0x67 0x80 0x0a 0x10 0x0d                   g....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 PumpResume 2013-06-16T10:16:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-16T10:16:08)
    0000   0x48 0x90 0x0a 0x10 0x0d                   H....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 CalBGForPH 2013-06-16T12:38:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-06-16T12:38:32)
    0000   0x60 0xa6 0x2c 0x10 0x0d                   `.,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 BolusWizard 2013-06-16T12:39:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.7,
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
    datetime (2013-06-16T12:39:23)
    0000   0x57 0xa7 0x0c 0x10 0x0d                   W....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x00 0x1b 0x00    $P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    0   27    0
              0    0    0   27  125
    HOUR BITS: [1, 0, 1]
#### RECORD 13 Bolus 2013-06-16T12:39:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-06-16T12:39:23)
    0000   0x57 0xa7 0x4c 0x10 0x0d                   W.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 14 LowReservoir 2013-06-16T13:10:54 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-06-16T13:10:54)
    0000   0x76 0x8a 0x0d 0x10 0x0d                   v....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 15 CalBGForPH 2013-06-16T14:03:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-06-16T14:03:07)
    0000   0x47 0x83 0x2e 0x10 0x0d                   G....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 CalBGForPH 2013-06-16T14:04:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-06-16T14:04:48)
    0000   0x70 0x84 0x2e 0x10 0x0d                   p....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 CalBGForPH 2013-06-16T14:07:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-06-16T14:07:14)
    0000   0x4e 0x87 0x2e 0x10 0x0d                   N....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 18 BolusWizard 2013-06-16T14:07:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-06-16T14:07:47)
    0000   0x6f 0x87 0x0e 0x10 0x0d                   o....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x00 0x18 0x00     P.-j...
    0008   0x00 0x11 0x00 0x18 0x7d                   ....}
    decimal
             32   80   13   45  106    0   24    0
              0   17    0   24  125
    HOUR BITS: [1, 0, 0]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 2.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0x5d 0x04                   \.l].
    decimal
             92    5  108   93    4
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-06-16T14:07:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-06-16T14:07:47)
    0000   0x6f 0x87 0x4e 0x10 0x0d                   o.N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 CalBGForPH 2013-06-16T15:48:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-06-16T15:48:00)
    0000   0x40 0xb0 0x2f 0x10 0x0d                   @./..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 CalBGForPH 2013-06-16T16:01:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2013-06-16T16:01:53)
    0000   0x75 0x81 0x30 0x10 0x0d                   u.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 CalBGForPH 2013-06-16T16:08:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 56}
```
    op hex (2)
    0000   0x0a 0x38                                  .8
    decimal
             10   56
    datetime (2013-06-16T16:08:54)
    0000   0x76 0x88 0x30 0x10 0x0d                   v.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 CalBGForPH 2013-06-16T19:27:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-06-16T19:27:46)
    0000   0x6e 0x9b 0x33 0x10 0x0d                   n.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 25 BolusWizard 2013-06-16T19:27:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 1.1,
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
    datetime (2013-06-16T19:27:54)
    0000   0x76 0x9b 0x13 0x10 0x0d                   v....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0xfd 0x0b 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             15   80   13   45  106  253   11  240
              0    0    0    8  125
    HOUR BITS: [1, 0, 0]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 2.4, 'curve': 20},
 {'age': 157, 'amount': 2.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x60 0x43 0x14 0x6c 0x9d 0x14    \.`C.l..
    decimal
             92    8   96   67   20  108  157   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-06-16T19:27:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-06-16T19:27:54)
    0000   0x76 0x9b 0x53 0x10 0x0d                   v.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 28 LowReservoir 2013-06-16T20:12:37 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-06-16T20:12:37)
    0000   0x65 0x8c 0x14 0x10 0x0d                   e....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 CalBGForPH 2013-06-16T20:57:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 147}
```
    op hex (2)
    0000   0x0a 0x93                                  ..
    decimal
             10  147
    datetime (2013-06-16T20:57:36)
    0000   0x64 0xb9 0x34 0x10 0x0d                   d.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 30 ResultTotals 2013-04-16T13:13:48 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x66                   ....f
    decimal
              7    0    0    4  102
    datetime (2013-04-16T13:13:48)
    0000   0x70 0x0d 0x6d 0x70 0x0d                   p.mp.
    body (41)
    hex
    0000   0x05 0x00 0x68 0x38 0x93 0x09 0x00 0x00    ..h8....
    0008   0x04 0x66 0x03 0x7a 0x4f 0x00 0xec 0x15    .f.zO...
    0010   0x00 0x53 0x00 0xec 0x15 0x00 0xec 0x64    .S.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x03 0x03    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  104   56  147    9    0    0
              4  102    3  122   79    0  236   21
              0   83    0  236   21    0  236  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 1]
#### RECORD 31 CalBGForPH 2013-06-17T10:19:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2013-06-17T10:19:58)
    0000   0x7a 0x93 0x2a 0x11 0x0d                   z.*..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 BolusWizard 2013-06-17T10:20:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 234,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
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
    0000   0x5b 0xea                                  [.
    decimal
             91  234
    datetime (2013-06-17T10:20:00)
    0000   0x40 0x94 0x0a 0x11 0x0d                   @....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x18 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
              0   80   13   45  106   24    0    0
              0    0    0   24  125
    HOUR BITS: [1, 0, 0]
#### RECORD 33 Bolus 2013-06-17T10:20:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-06-17T10:20:01)
    0000   0x41 0x94 0x4a 0x11 0x0d                   A.J..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 34 PumpSuspend 2013-06-17T13:17:32 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-17T13:17:32)
    0000   0x60 0x91 0x0d 0x11 0x0d                   `....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 PumpResume 2013-06-17T13:51:23 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-17T13:51:23)
    0000   0x57 0xb3 0x0d 0x11 0x0d                   W....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 Rewind 2013-06-17T15:03:10 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-06-17T15:03:10)
    0000   0x4a 0x83 0x0f 0x11 0x0d                   J....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 37 Prime 2013-06-17T15:05:39 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x11                   .....
    decimal
              3    0    0    0   17
    datetime (2013-06-17T15:05:39)
    0000   0x67 0x85 0x2f 0x11 0x0d                   g./..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 38 Prime 2013-06-17T15:06:01 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-06-17T15:06:01)
    0000   0x41 0x86 0x0f 0x11 0x0d                   A....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 CalBGForPH 2013-06-17T16:12:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-06-17T16:12:26)
    0000   0x5a 0x8c 0x30 0x11 0x0d                   Z.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 CalBGForPH 2013-06-17T16:13:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2013-06-17T16:13:12)
    0000   0x4c 0x8d 0x30 0x11 0x0d                   L.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 41 BolusWizard 2013-06-17T16:13:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.2,
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
    datetime (2013-06-17T16:13:44)
    0000   0x6c 0x8d 0x10 0x11 0x0d                   l....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x00 0x2a 0x00    7P.-j.*.
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    0   42    0
              0    0    0   42  125
    HOUR BITS: [1, 0, 0]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 2.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0x67 0x14                   \.`g.
    decimal
             92    5   96  103   20
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-06-17T16:13:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-06-17T16:13:44)
    0000   0x6c 0x8d 0x50 0x11 0x0d                   l.P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 44 CalBGForPH 2013-06-17T17:10:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 254}
```
    op hex (2)
    0000   0x0a 0xfe                                  ..
    decimal
             10  254
    datetime (2013-06-17T17:10:53)
    0000   0x75 0x8a 0x31 0x11 0x0d                   u.1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 45 BolusWizard 2013-06-17T19:29:11 head[2], body[13] op[0x5b]
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
    datetime (2013-06-17T19:29:11)
    0000   0x4b 0x9d 0x13 0x11 0x0d                   K....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0x00 0x23 0x00    .P.-j.#.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             46   80   13   45  106    0   35    0
              0    0    0   35  125
    HOUR BITS: [1, 0, 0]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 195, 'amount': 3.8, 'curve': 4},
 {'age': 205, 'amount': 0.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x98 0xc3 0x04 0x10 0xcd 0x04    \.......
    decimal
             92    8  152  195    4   16  205    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-06-17T19:29:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-06-17T19:29:11)
    0000   0x4b 0x9d 0x53 0x11 0x0d                   K.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 48 CalBGForPH 2013-06-17T20:51:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-06-17T20:51:41)
    0000   0x69 0xb3 0x34 0x11 0x0d                   i.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 CalBGForPH 2013-06-17T21:06:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-06-17T21:06:49)
    0000   0x71 0x86 0x35 0x11 0x0d                   q.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 ResultTotals 2013-04-17T13:13:49 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xfe                   .....
    decimal
              7    0    0    4  254
    datetime (2013-04-17T13:13:49)
    0000   0x71 0x0d 0x6d 0x71 0x0d                   q.mq.
    body (41)
    hex
    0000   0x05 0x00 0x9e 0x6b 0xfe 0x06 0x00 0x00    ...k....
    0008   0x04 0xfe 0x03 0x6a 0x44 0x01 0x94 0x20    ...jD.. 
    0010   0x00 0x65 0x01 0x94 0x20 0x01 0x34 0x4c    .e.. .4L
    0018   0x00 0x60 0x18 0x00 0x00 0x00 0x03 0x02    .`......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  158  107  254    6    0    0
              4  254    3  106   68    1  148   32
              0  101    1  148   32    1   52   76
              0   96   24    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-0.data: 51 records`
