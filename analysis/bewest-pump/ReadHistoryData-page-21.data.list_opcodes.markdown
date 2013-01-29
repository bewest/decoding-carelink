## START logs/ReadHistoryData-page-21.data
#### RECORD 0 hack1 2012-11-05T03:16:57 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0xa4 0x8c 0x05 0x00 0xda 0xaa 0xfb    m.......
    0008   0x06 0x00 0x00 0x05 0x64 0x03 0x78 0x40    ....d.x@
    0010   0x01 0xec 0x24 0x00 0x0e 0x01 0xec 0x24    ..$....$
    0018   0x00 0x28 0x08 0x01 0xc4 0x5c 0x00 0x00    .(...\..
    0020   0x00 0x07 0x01 0x06 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x49              .....I
    decimal
            109  164  140    5    0  218  170  251
              6    0    0    5  100    3  120   64
              1  236   36    0   14    1  236   36
              0   40    8    1  196   92    0    0
              0    7    1    6    0    0   12    0
            232    0    0    0   10   73
    datetime (2012-11-05T03:16:57)
    0000   0xb9 0xd0 0x23 0x05 0x0c                   ..#..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 PumpSuspend 2012-11-05T12:59:16 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-05T12:59:16)
    0000   0x90 0xfb 0x0c 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 PumpResume 2012-11-05T13:14:45 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-05T13:14:45)
    0000   0xad 0xce 0x0d 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 Rewind 2012-11-05T13:52:37 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-11-05T13:52:37)
    0000   0xa5 0xf4 0x0d 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 Prime 2012-11-05T13:54:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1d                   .....
    decimal
              3    0    0    0   29
    datetime (2012-11-05T13:54:18)
    0000   0x92 0xf6 0x2d 0x05 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 Prime 2012-11-05T13:54:39 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-11-05T13:54:39)
    0000   0xa7 0xf6 0x0d 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 CalBGForPH 2012-11-05T13:56:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2012-11-05T13:56:47)
    0000   0xaf 0xf8 0x2d 0x05 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 BolusWizard 2012-11-05T13:57:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 139,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 5.0,
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
    datetime (2012-11-05T13:57:23)
    0000   0x97 0xf9 0x0d 0x05 0x0c                   .....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x03 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x35 0x7d                   ...5}
    decimal
             65   80   13   45  106    3   50    0
              0    0    0   53  125
    HOUR BITS: [1, 1, 1]
#### RECORD 8 Bolus 2012-11-05T13:57:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6, 'programmed': 5.6}
```
    op hex (4)
    0000   0x01 0x38 0x38 0x00                        .88.
    decimal
              1   56   56    0
    datetime (2012-11-05T13:57:23)
    0000   0x97 0xf9 0x4d 0x05 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 ChangeTimeDisplay 2012-11-05T14:28:07 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2012-11-05T14:28:07)
    0000   0x87 0xdc 0x0e 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 ChangeTime 2012-11-05T14:28:11 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2012-11-05T14:28:11)
    0000   0x8b 0xdc 0x0e 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 NewTimeSet 2012-11-05T13:28:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2012-11-05T13:28:00)
    0000   0x80 0xdc 0x0d 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2012-11-05T15:40:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2012-11-05T15:40:50)
    0000   0xb2 0xe8 0x2f 0x05 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 BolusWizard 2012-11-05T15:41:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 124,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 5,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7c                                  [|
    decimal
             91  124
    datetime (2012-11-05T15:41:10)
    0000   0x8a 0xe9 0x0f 0x05 0x0c                   .....
    body (13)
    hex
    0000   0x05 0x50 0x0d 0x2d 0x6a 0x00 0x03 0x00    .P.-j...
    0008   0x00 0x0d 0x00 0x03 0x7d                   ....}
    decimal
              5   80   13   45  106    0    3    0
              0   13    0    3  125
    HOUR BITS: [1, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 167, 'amount': 5.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xe0 0xa7 0x04                   \....
    decimal
             92    5  224  167    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2012-11-05T15:41:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-11-05T15:41:10)
    0000   0x8a 0xe9 0x4f 0x05 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 16 CalBGForPH 2012-11-05T19:10:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 222}
```
    op hex (2)
    0000   0x0a 0xde                                  ..
    decimal
             10  222
    datetime (2012-11-05T19:10:10)
    0000   0x8a 0xca 0x33 0x05 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 BolusWizard 2012-11-05T19:10:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 222,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xde                                  [.
    decimal
             91  222
    datetime (2012-11-05T19:10:12)
    0000   0x8c 0xca 0x13 0x05 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    1    0   20  125
    HOUR BITS: [1, 1, 0]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 216, 'amount': 0.3, 'curve': 4},
 {'age': 120, 'amount': 5.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x0c 0xd8 0x04 0xe0 0x78 0x14    \.....x.
    decimal
             92    8   12  216    4  224  120   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2012-11-05T19:10:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-11-05T19:10:12)
    0000   0x8c 0xca 0x53 0x05 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 CalBGForPH 2012-11-05T20:34:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 138}
```
    op hex (2)
    0000   0x0a 0x8a                                  ..
    decimal
             10  138
    datetime (2012-11-05T20:34:13)
    0000   0x8d 0xe2 0x34 0x05 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 CalBGForPH 2012-11-05T20:43:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2012-11-05T20:43:19)
    0000   0x93 0xeb 0x34 0x05 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 22 BolusWizard 2012-11-05T20:43:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 124,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7c                                  [|
    decimal
             91  124
    datetime (2012-11-05T20:43:34)
    0000   0xa2 0xeb 0x14 0x05 0x0c                   .....
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x0c 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0   12    0   21  125
    HOUR BITS: [1, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 99, 'amount': 2.0, 'curve': 4},
 {'age': 53, 'amount': 0.3, 'curve': 20},
 {'age': 213, 'amount': 5.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x63 0x04 0x0c 0x35 0x14    \.Pc..5.
    0008   0xe0 0xd5 0x14                             ...
    decimal
             92   11   80   99    4   12   53   20
            224  213   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2012-11-05T20:43:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'programmed': 2.1}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2012-11-05T20:43:34)
    0000   0xa2 0xeb 0x54 0x05 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 ResultTotals 2012-10-05T13:12:37 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x2e                   .....
    decimal
              7    0    0    5   46
    datetime (2012-10-05T13:12:37)
    0000   0xa5 0x8c 0x6d 0xa5 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x89 0x49 0xde 0x06 0x00 0x00    ...I....
    0008   0x05 0x2e 0x03 0x9e 0x46 0x01 0x90 0x1e    ....F...
    0010   0x00 0x62 0x01 0x90 0x1e 0x01 0x28 0x4a    .b....(J
    0018   0x00 0x68 0x1a 0x00 0x00 0x00 0x04 0x02    .h......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  137   73  222    6    0    0
              5   46    3  158   70    1  144   30
              0   98    1  144   30    1   40   74
              0  104   26    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 CalBGForPH 2012-11-06T01:05:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-11-06T01:05:40)
    0000   0xa8 0xc5 0x21 0x06 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 PumpSuspend 2012-11-06T13:59:42 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-06T13:59:42)
    0000   0xaa 0xfb 0x0d 0x06 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 PumpResume 2012-11-06T14:12:23 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-06T14:12:23)
    0000   0x97 0xcc 0x0e 0x06 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 29 CalBGForPH 2012-11-06T14:35:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-11-06T14:35:35)
    0000   0xa3 0xe3 0x2e 0x06 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 CalBGForPH 2012-11-06T14:37:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-11-06T14:37:06)
    0000   0x86 0xe5 0x2e 0x06 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 CalBGForPH 2012-11-06T14:37:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-11-06T14:37:47)
    0000   0xaf 0xe5 0x2e 0x06 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 BolusWizard 2012-11-06T14:38:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 78,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4e                                  [N
    decimal
             91   78
    datetime (2012-11-06T14:38:28)
    0000   0x9c 0xe6 0x0e 0x06 0x0c                   .....
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0xfa 0x2c 0xf0    :P.-j.,.
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
             58   80   13   45  106  250   44  240
              0    0    0   38  125
    HOUR BITS: [1, 1, 1]
#### RECORD 33 Bolus 2012-11-06T14:38:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'programmed': 3.8}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2012-11-06T14:38:28)
    0000   0x9c 0xe6 0x4e 0x06 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 CalBGForPH 2012-11-06T16:47:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2012-11-06T16:47:12)
    0000   0x8c 0xef 0x30 0x06 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 BolusWizard 2012-11-06T17:34:21 head[2], body[13] op[0x5b]
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
    datetime (2012-11-06T17:34:21)
    0000   0x95 0xe2 0x11 0x06 0x0c                   .....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 1, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 180, 'amount': 3.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x98 0xb4 0x04                   \....
    decimal
             92    5  152  180    4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2012-11-06T17:34:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-06T17:34:21)
    0000   0x95 0xe2 0x51 0x06 0x0c                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 CalBGForPH 2012-11-06T18:28:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2012-11-06T18:28:22)
    0000   0x96 0xdc 0x32 0x06 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 39 CalBGForPH 2012-11-06T20:00:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 258}
```
    op hex (2)
    0000   0x0a 0x02                                  ..
    decimal
             10    2
    datetime (2012-11-06T20:00:15)
    0000   0x8f 0xc0 0x34 0x06 0x8c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 40 BolusWizard 2012-11-06T20:00:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 258,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x02                                  [.
    decimal
             91    2
    datetime (2012-11-06T20:00:17)
    0000   0x91 0xc0 0x14 0x06 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x04 0x00 0x19 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    4    0   25  125
    HOUR BITS: [1, 1, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 146, 'amount': 1.0, 'curve': 4},
 {'age': 70, 'amount': 3.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x92 0x04 0x98 0x46 0x14    \.(...F.
    decimal
             92    8   40  146    4  152   70   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2012-11-06T20:00:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'programmed': 2.5}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2012-11-06T20:00:17)
    0000   0x91 0xc0 0x54 0x06 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 43 ResultTotals 2012-10-06T13:12:38 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xa0                   .....
    decimal
              7    0    0    4  160
    datetime (2012-10-06T13:12:38)
    0000   0xa6 0x8c 0x6d 0xa6 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x76 0x4e 0x02 0x07 0x00 0x00    ..vN....
    0008   0x04 0xa0 0x03 0x7c 0x4b 0x01 0x24 0x19    ...|K.$.
    0010   0x00 0x48 0x01 0x24 0x19 0x00 0xc0 0x42    .H.$...B
    0018   0x00 0x64 0x22 0x00 0x00 0x00 0x03 0x02    .d".....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  118   78    2    7    0    0
              4  160    3  124   75    1   36   25
              0   72    1   36   25    0  192   66
              0  100   34    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 44 CalBGForPH 2012-11-07T06:45:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2012-11-07T06:45:31)
    0000   0x9f 0xed 0x26 0x07 0x0c                   ..&..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BolusWizard 2012-11-07T06:45:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 177,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
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
    0000   0x5b 0xb1                                  [.
    decimal
             91  177
    datetime (2012-11-07T06:45:33)
    0000   0xa1 0xed 0x06 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    0    0   11  125
    HOUR BITS: [1, 1, 1]
#### RECORD 46 Bolus 2012-11-07T06:45:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2012-11-07T06:45:33)
    0000   0xa1 0xed 0x46 0x07 0x0c                   ..F..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 47 PumpSuspend 2012-11-07T13:51:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-07T13:51:56)
    0000   0xb8 0xf3 0x0d 0x07 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 PumpResume 2012-11-07T14:06:54 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-07T14:06:54)
    0000   0xb6 0xc6 0x0e 0x07 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 CalBGForPH 2012-11-07T15:13:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-11-07T15:13:00)
    0000   0x80 0xcd 0x2f 0x07 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 BolusWizard 2012-11-07T15:13:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 78,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4e                                  [N
    decimal
             91   78
    datetime (2012-11-07T15:13:26)
    0000   0x9a 0xcd 0x0f 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0xfa 0x27 0xf0    3P.-j.'.
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
             51   80   13   45  106  250   39  240
              0    0    0   33  125
    HOUR BITS: [1, 1, 0]
#### RECORD 51 Bolus 2012-11-07T15:13:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'programmed': 3.3}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2012-11-07T15:13:26)
    0000   0x9a 0xcd 0x4f 0x07 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 52 BolusWizard 2012-11-07T15:24:32 head[2], body[13] op[0x5b]
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
    datetime (2012-11-07T15:24:32)
    0000   0xa0 0xd8 0x0f 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125
    HOUR BITS: [1, 1, 0]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 2.45, 'curve': 4},
 {'age': 20, 'amount': 0.85, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x62 0x0a 0x04 0x22 0x14 0x04    \.b.."..
    decimal
             92    8   98   10    4   34   20    4
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2012-11-07T15:24:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'programmed': 0.9}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2012-11-07T15:24:32)
    0000   0xa0 0xd8 0x4f 0x07 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 CalBGForPH 2012-11-07T16:41:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-11-07T16:41:49)
    0000   0xb1 0xe9 0x30 0x07 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 56 CalBGForPH 2012-11-07T16:41:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 122}
```
    op hex (2)
    0000   0x0a 0x7a                                  .z
    decimal
             10  122
    datetime (2012-11-07T16:41:59)
    0000   0xbb 0xe9 0x30 0x07 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 57 BolusWizard 2012-11-07T17:13:03 head[2], body[13] op[0x5b]
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
    datetime (2012-11-07T17:13:03)
    0000   0x83 0xcd 0x11 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x00 0x05 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x05 0x7d                   ....}
    decimal
              7   80   13   45  106    0    5    0
              0    0    0    5  125
    HOUR BITS: [1, 1, 0]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 0.9, 'curve': 4},
 {'age': 119, 'amount': 2.45, 'curve': 4},
 {'age': 129, 'amount': 0.85, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x24 0x6d 0x04 0x62 0x77 0x04    \.$m.bw.
    0008   0x22 0x81 0x04                             "..
    decimal
             92   11   36  109    4   98  119    4
             34  129    4
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2012-11-07T17:13:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-11-07T17:13:03)
    0000   0x83 0xcd 0x51 0x07 0x0c                   ..Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 60 CalBGForPH 2012-11-07T17:37:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 83}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2012-11-07T17:37:43)
    0000   0xab 0xe5 0x31 0x07 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 61 CalBGForPH 2012-11-07T19:47:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2012-11-07T19:47:31)
    0000   0x9f 0xef 0x33 0x07 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 62 CalBGForPH 2012-11-07T20:50:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2012-11-07T20:50:46)
    0000   0xae 0xf2 0x34 0x07 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 63 BolusWizard 2012-11-07T20:51:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 180,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb4                                  [.
    decimal
             91  180
    datetime (2012-11-07T20:51:10)
    0000   0x8a 0xf3 0x14 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    1    0   11  125
    HOUR BITS: [1, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 227, 'amount': 0.5, 'curve': 4},
 {'age': 71, 'amount': 0.9, 'curve': 20},
 {'age': 81, 'amount': 2.45, 'curve': 20},
 {'age': 91, 'amount': 0.85, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x14 0xe3 0x04 0x24 0x47 0x14    \....$G.
    0008   0x62 0x51 0x14 0x22 0x5b 0x14              bQ."[.
    decimal
             92   14   20  227    4   36   71   20
             98   81   20   34   91   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2012-11-07T20:51:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'programmed': 0.4}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2012-11-07T20:51:10)
    0000   0x8a 0xf3 0x54 0x07 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 ResultTotals 2012-10-07T13:12:39 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x72                   ....r
    decimal
              7    0    0    4  114
    datetime (2012-10-07T13:12:39)
    0000   0xa7 0x8c 0x6d 0xa7 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x7f 0x4e 0xb4 0x07 0x00 0x00    ...N....
    0008   0x04 0x72 0x03 0x7a 0x4e 0x00 0xf8 0x16    .r.zN...
    0010   0x00 0x46 0x00 0xf8 0x16 0x00 0xbc 0x4c    .F.....L
    0018   0x00 0x3c 0x18 0x00 0x00 0x00 0x05 0x03    .<......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  127   78  180    7    0    0
              4  114    3  122   78    0  248   22
              0   70    0  248   22    0  188   76
              0   60   24    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 67 PumpSuspend 2012-11-08T10:27:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-08T10:27:56)
    0000   0xb8 0xdb 0x0a 0x08 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 PumpResume 2012-11-08T11:00:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-08T11:00:04)
    0000   0x84 0xc0 0x0b 0x08 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 69 CalBGForPH 2012-11-08T11:34:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2012-11-08T11:34:42)
    0000   0xaa 0xe2 0x2b 0x08 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 70 BolusWizard 2012-11-08T11:36:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 141,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 3.4,
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
    datetime (2012-11-08T11:36:10)
    0000   0x8a 0xe4 0x0b 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x03 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             45   80   13   45  106    3   34    0
              0    0    0   37  125
    HOUR BITS: [1, 1, 1]
#### RECORD 71 Bolus 2012-11-08T11:36:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'programmed': 3.7}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2012-11-08T11:36:10)
    0000   0x8a 0xe4 0x4b 0x08 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 CalBGForPH 2012-11-08T12:34:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-11-08T12:34:19)
    0000   0x93 0xe2 0x2c 0x08 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 73 CalBGForPH 2012-11-08T12:59:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2012-11-08T12:59:12)
    0000   0x8c 0xfb 0x2c 0x08 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 74 BolusWizard 2012-11-08T13:01:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2012-11-08T13:01:32)
    0000   0xa0 0xc1 0x0d 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0x00 0x18 0x00     P.-j...
    0008   0x00 0x19 0x00 0x18 0x7d                   ....}
    decimal
             32   80   13   45  106    0   24    0
              0   25    0   24  125
    HOUR BITS: [1, 1, 0]
#### RECORD 75 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 87, 'amount': 3.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x94 0x57 0x04                   \..W.
    decimal
             92    5  148   87    4
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2012-11-08T13:01:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2012-11-08T13:01:32)
    0000   0xa0 0xc1 0x4d 0x08 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 77 LowReservoir 2012-11-08T18:18:56 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-11-08T18:18:56)
    0000   0xb8 0xd2 0x12 0x08 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 78 CalBGForPH 2012-11-08T20:09:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2012-11-08T20:09:18)
    0000   0x92 0xc9 0x34 0x08 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 BolusWizard 2012-11-08T20:10:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 67,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 5.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2012-11-08T20:10:11)
    0000   0x8b 0xca 0x14 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x43 0x50 0x0d 0x2d 0x6a 0x02 0x33 0x00    CP.-j.3.
    0008   0x00 0x00 0x00 0x35 0x7d                   ...5}
    decimal
             67   80   13   45  106    2   51    0
              0    0    0   53  125
    HOUR BITS: [1, 1, 0]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 180, 'amount': 2.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0xb4 0x14                   \.`..
    decimal
             92    5   96  180   20
    datetime (unknown)

    body (0)

#### RECORD 81 Bolus 2012-11-08T20:10:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'programmed': 5.3}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2012-11-08T20:10:11)
    0000   0x8b 0xca 0x54 0x08 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 82 CalBGForPH 2012-11-08T21:36:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 77}
```
    op hex (2)
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2012-11-08T21:36:41)
    0000   0xa9 0xe4 0x35 0x08 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 83 LowReservoir 2012-11-08T23:15:47 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-11-08T23:15:47)
    0000   0xaf 0xcf 0x17 0x08 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 84 ResultTotals (2000, 10, 0, 0, 12, 40) head[5], body[9] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x34                   ....4
    decimal
              7    0    0    5   52
    datetime ((2000, 10, 0, 0, 12, 40))
    0000   0xa8 0x8c 0x00 0x00 0x00                   .....
    body (9)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x02    ........
    0008   0x0e                                       .
    decimal
              0    0    0    0    0    0    0    2
             14
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-21.data: 85 records`
