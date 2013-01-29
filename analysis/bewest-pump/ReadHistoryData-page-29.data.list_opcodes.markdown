## START logs/ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 1010, found 12 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x99 0x20                                  . 
##### DEBUG DECIMAL
            153   32
#### RECORD 0 hack1 2012-10-08T09:15:28 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0xa7 0x0c 0x05 0x00 0xb9 0x5e 0xfd    m.....^.
    0008   0x05 0x00 0x00 0x04 0x52 0x02 0xa6 0x3d    ....R..=
    0010   0x01 0xac 0x27 0x00 0x49 0x01 0xac 0x27    ..'.I..'
    0018   0x00 0xdc 0x33 0x00 0xd0 0x31 0x00 0x00    ..3..1..
    0020   0x00 0x04 0x01 0x02 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x1a              ......
    decimal
            109  167   12    5    0  185   94  253
              5    0    0    4   82    2  166   61
              1  172   39    0   73    1  172   39
              0  220   51    0  208   49    0    0
              0    4    1    2    1    0   12    0
            232    0    0    0   10   26
    datetime (2012-10-08T09:15:28)
    0000   0x9c 0x8f 0x29 0x08 0x8c                   ..)..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 1 BolusWizard 2012-10-08T09:15:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 282,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x1a                                  [.
    decimal
             91   26
    datetime (2012-10-08T09:15:30)
    0000   0x9e 0x8f 0x09 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x22 0x00 0x00    .Q.-j"..
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
              0   81   13   45  106   34    0    0
              0    0    0   34  125
    HOUR BITS: [1, 0, 0]
#### RECORD 2 Bolus 2012-10-08T09:15:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-10-08T09:15:30)
    0000   0x9e 0x8f 0x49 0x08 0x0c                   ..I..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 PumpSuspend 2012-10-08T14:08:31 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-08T14:08:31)
    0000   0x9f 0x88 0x0e 0x08 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 4 PumpResume 2012-10-08T14:26:26 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-08T14:26:26)
    0000   0x9a 0x9a 0x0e 0x08 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 CalBGForPH 2012-10-08T15:53:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2012-10-08T15:53:04)
    0000   0x84 0xb5 0x2f 0x08 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 BolusWizard 2012-10-08T15:53:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 97,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 57,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x61                                  [a
    decimal
             91   97
    datetime (2012-10-08T15:53:15)
    0000   0x8f 0xb5 0x0f 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x39 0x50 0x0d 0x2d 0x6a 0xfe 0x2b 0xf0    9P.-j.+.
    0008   0x00 0x00 0x00 0x29 0x7d                   ...)}
    decimal
             57   80   13   45  106  254   43  240
              0    0    0   41  125
    HOUR BITS: [1, 0, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 143, 'amount': 3.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x88 0x8f 0x14                   \....
    decimal
             92    5  136  143   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2012-10-08T15:53:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'programmed': 4.1}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2012-10-08T15:53:16)
    0000   0x90 0xb5 0x4f 0x08 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 CalBGForPH 2012-10-08T17:27:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2012-10-08T17:27:50)
    0000   0xb2 0x9b 0x31 0x08 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 BolusWizard 2012-10-08T20:51:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-08T20:51:37)
    0000   0xa5 0xb3 0x14 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x00 0x27 0x00    3P.-j.'.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106    0   39    0
              0    0    0   39  125
    HOUR BITS: [1, 0, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 3.05, 'curve': 20},
 {'age': 51, 'amount': 1.05, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x7a 0x29 0x14 0x2a 0x33 0x14    \.z).*3.
    decimal
             92    8  122   41   20   42   51   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2012-10-08T20:51:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'programmed': 3.9}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2012-10-08T20:51:37)
    0000   0xa5 0xb3 0x54 0x08 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 13 BolusWizard 2012-10-08T20:59:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-08T20:59:16)
    0000   0x90 0xbb 0x14 0x08 0x0c                   .....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [1, 0, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 0.35, 'curve': 4},
 {'age': 15, 'amount': 3.55, 'curve': 4},
 {'age': 49, 'amount': 3.05, 'curve': 20},
 {'age': 59, 'amount': 1.05, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0e 0x05 0x04 0x8e 0x0f 0x04    \.......
    0008   0x7a 0x31 0x14 0x2a 0x3b 0x14              z1.*;.
    decimal
             92   14   14    5    4  142   15    4
            122   49   20   42   59   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2012-10-08T20:59:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-10-08T20:59:16)
    0000   0x90 0xbb 0x54 0x08 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 16 ResultTotals 2012-08-08T13:12:40 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x9c                   .....
    decimal
              7    0    0    5  156
    datetime (2012-08-08T13:12:40)
    0000   0xa8 0x0c 0x6d 0xa8 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xab 0x61 0x1a 0x03 0x00 0x00    ...a....
    0008   0x05 0x9c 0x03 0x78 0x3e 0x02 0x24 0x26    ...x>.$&
    0010   0x00 0x8b 0x02 0x24 0x26 0x01 0x9c 0x4b    ...$&..K
    0018   0x00 0x88 0x19 0x00 0x00 0x00 0x04 0x03    ........
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  171   97   26    3    0    0
              5  156    3  120   62    2   36   38
              0  139    2   36   38    1  156   75
              0  136   25    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 17 CalBGForPH 2012-10-09T00:59:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2012-10-09T00:59:34)
    0000   0xa2 0xbb 0x20 0x09 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 BolusWizard 2012-10-09T00:59:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 182,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xb6                                  [.
    decimal
             91  182
    datetime (2012-10-09T00:59:36)
    0000   0xa4 0xbb 0x00 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    0    0   12  125
    HOUR BITS: [1, 0, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 245, 'amount': 2.65, 'curve': 4},
 {'age': 255, 'amount': 3.55, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x6a 0xf5 0x04 0x8e 0xff 0x04    \.j.....
    decimal
             92    8  106  245    4  142  255    4
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2012-10-09T00:59:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-10-09T00:59:37)
    0000   0xa5 0xbb 0x40 0x09 0x0c                   ..@..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 21 PumpSuspend 2012-10-09T01:03:42 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-09T01:03:42)
    0000   0xaa 0x83 0x01 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 22 PumpResume 2012-10-09T01:05:51 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-09T01:05:51)
    0000   0xb3 0x85 0x01 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 PumpSuspend 2012-10-09T13:20:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-09T13:20:39)
    0000   0xa7 0x94 0x0d 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 PumpResume 2012-10-09T13:37:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-09T13:37:58)
    0000   0xba 0xa5 0x0d 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 25 CalBGForPH 2012-10-09T14:17:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2012-10-09T14:17:10)
    0000   0x8a 0x91 0x2e 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 26 BolusWizard 2012-10-09T14:17:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 153,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2012-10-09T14:17:15)
    0000   0x8f 0x91 0x0e 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    0    0    6  125
    HOUR BITS: [1, 0, 0]
#### RECORD 27 Bolus 2012-10-09T14:17:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'programmed': 0.6}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-10-09T14:17:15)
    0000   0x8f 0x91 0x4e 0x09 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 28 BolusWizard 2012-10-09T14:25:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-09T14:25:14)
    0000   0x8e 0x99 0x0e 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [1, 0, 0]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 0.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x18 0x0b 0x04                   \....
    decimal
             92    5   24   11    4
    datetime (unknown)

    body (0)

#### RECORD 30 LowReservoir 2012-10-09T14:26:22 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-10-09T14:26:22)
    0000   0x96 0x9a 0x0e 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 Bolus 2012-10-09T14:25:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-10-09T14:25:14)
    0000   0x8e 0x99 0x4e 0x09 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 BolusWizard 2012-10-09T14:41:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-09T14:41:02)
    0000   0x82 0xa9 0x0e 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [1, 0, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 2.0, 'curve': 4},
 {'age': 27, 'amount': 0.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0x11 0x04 0x18 0x1b 0x04    \.P.....
    decimal
             92    8   80   17    4   24   27    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2012-10-09T14:41:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-10-09T14:41:02)
    0000   0x82 0xa9 0x4e 0x09 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 35 BolusWizard 2012-10-09T15:14:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 11,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-09T15:14:10)
    0000   0x8a 0x8e 0x0f 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0    0    0    8  125
    HOUR BITS: [1, 0, 0]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 1.9, 'curve': 4},
 {'age': 50, 'amount': 2.0, 'curve': 4},
 {'age': 60, 'amount': 0.6, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x4c 0x28 0x04 0x50 0x32 0x04    \.L(.P2.
    0008   0x18 0x3c 0x04                             .<.
    decimal
             92   11   76   40    4   80   50    4
             24   60    4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2012-10-09T15:14:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'programmed': 0.8}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2012-10-09T15:14:10)
    0000   0x8a 0x8e 0x4f 0x09 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 38 CalBGForPH 2012-10-09T18:20:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2012-10-09T18:20:03)
    0000   0x83 0x94 0x32 0x09 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 BolusWizard 2012-10-09T18:20:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 115,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2012-10-09T18:20:32)
    0000   0xa0 0x94 0x12 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x00 0x1c 0x00    %P.-j...
    0008   0x00 0x04 0x00 0x1c 0x7d                   ....}
    decimal
             37   80   13   45  106    0   28    0
              0    4    0   28  125
    HOUR BITS: [1, 0, 0]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 186, 'amount': 0.8, 'curve': 4},
 {'age': 226, 'amount': 1.9, 'curve': 4},
 {'age': 236, 'amount': 2.0, 'curve': 4},
 {'age': 246, 'amount': 0.6, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x20 0xba 0x04 0x4c 0xe2 0x04    \. ..L..
    0008   0x50 0xec 0x04 0x18 0xf6 0x04              P.....
    decimal
             92   14   32  186    4   76  226    4
             80  236    4   24  246    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2012-10-09T18:20:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'programmed': 2.8}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2012-10-09T18:20:32)
    0000   0xa0 0x94 0x52 0x09 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 BolusWizard 2012-10-09T18:26:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-09T18:26:45)
    0000   0xad 0x9a 0x12 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x00 0x22 0x00    -P.-j.".
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
             45   80   13   45  106    0   34    0
              0    0    0   34  125
    HOUR BITS: [1, 0, 0]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 2.8, 'curve': 4},
 {'age': 192, 'amount': 0.8, 'curve': 4},
 {'age': 232, 'amount': 1.9, 'curve': 4},
 {'age': 242, 'amount': 2.0, 'curve': 4},
 {'age': 252, 'amount': 0.6, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x70 0x0c 0x04 0x20 0xc0 0x04    \.p.. ..
    0008   0x4c 0xe8 0x04 0x50 0xf2 0x04 0x18 0xfc    L..P....
    0010   0x04                                       .
    decimal
             92   17  112   12    4   32  192    4
             76  232    4   80  242    4   24  252
              4
    datetime (unknown)

    body (0)

#### RECORD 44 LowReservoir 2012-10-09T18:26:59 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-10-09T18:26:59)
    0000   0xbb 0x9a 0x12 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 45 Bolus 2012-10-09T18:26:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-10-09T18:26:45)
    0000   0xad 0x9a 0x52 0x09 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 46 ResultTotals 2012-08-09T13:12:41 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x72                   ....r
    decimal
              7    0    0    5  114
    datetime (2012-08-09T13:12:41)
    0000   0xa9 0x0c 0x6d 0xa9 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x96 0x73 0xb6 0x03 0x00 0x00    ...s....
    0008   0x05 0x72 0x03 0x76 0x40 0x01 0xfc 0x24    .r.v@..$
    0010   0x00 0x91 0x01 0xfc 0x24 0x01 0xb4 0x56    ....$..V
    0018   0x00 0x48 0x0e 0x00 0x00 0x00 0x07 0x05    .H......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  150  115  182    3    0    0
              5  114    3  118   64    1  252   36
              0  145    1  252   36    1  180   86
              0   72   14    0    0    0    7    5
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 47 CalBGForPH 2012-10-10T01:48:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2012-10-10T01:48:14)
    0000   0x8e 0xb0 0x21 0x0a 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 48 BolusWizard 2012-10-10T01:48:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 181,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xb5                                  [.
    decimal
             91  181
    datetime (2012-10-10T01:48:16)
    0000   0x90 0xb0 0x01 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    0    0   12  125
    HOUR BITS: [1, 0, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 188, 'amount': 3.4, 'curve': 20},
 {'age': 198, 'amount': 2.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x88 0xbc 0x14 0x70 0xc6 0x14    \....p..
    decimal
             92    8  136  188   20  112  198   20
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2012-10-10T01:48:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-10-10T01:48:16)
    0000   0x90 0xb0 0x41 0x0a 0x0c                   ..A..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 51 Rewind 2012-10-10T09:02:21 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-10-10T09:02:21)
    0000   0x95 0x82 0x09 0x0a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 52 Prime 2012-10-10T09:03:56 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x32                   ....2
    decimal
              3    0    0    0   50
    datetime (2012-10-10T09:03:56)
    0000   0xb8 0x83 0x29 0x0a 0x0c                   ..)..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 Prime 2012-10-10T09:04:20 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-10-10T09:04:20)
    0000   0x94 0x84 0x09 0x0a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 54 CalBGForPH 2012-10-10T09:17:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 291}
```
    op hex (2)
    0000   0x0a 0x23                                  .#
    decimal
             10   35
    datetime (2012-10-10T09:17:10)
    0000   0x8a 0x91 0x29 0x0a 0x8c                   ..)..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 55 BolusWizard 2012-10-10T09:17:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 291,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x23                                  [#
    decimal
             91   35
    datetime (2012-10-10T09:17:12)
    0000   0x8c 0x91 0x09 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
              0   81   13   45  106   36    0    0
              0    0    0   36  125
    HOUR BITS: [1, 0, 0]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 197, 'amount': 1.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0xc5 0x14                   \.0..
    decimal
             92    5   48  197   20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2012-10-10T09:17:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-10-10T09:17:12)
    0000   0x8c 0x91 0x49 0x0a 0x0c                   ..I..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 58 PumpSuspend 2012-10-10T12:20:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-10T12:20:57)
    0000   0xb9 0x94 0x0c 0x0a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 PumpResume 2012-10-10T12:43:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-10T12:43:29)
    0000   0x9d 0xab 0x0c 0x0a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 60 BolusWizard 2012-10-10T13:14:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-10T13:14:47)
    0000   0xaf 0x8e 0x0d 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x00 0x1b 0x00    $P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    0   27    0
              0    0    0   27  125
    HOUR BITS: [1, 0, 0]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 240, 'amount': 3.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0xf0 0x04                   \....
    decimal
             92    5  144  240    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2012-10-10T13:14:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'programmed': 2.7}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2012-10-10T13:14:47)
    0000   0xaf 0x8e 0x4d 0x0a 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 BolusWizard 2012-10-10T13:32:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 18,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-10T13:32:00)
    0000   0x80 0xa0 0x0d 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [1, 0, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 2.7, 'curve': 4},
 {'age': 2, 'amount': 3.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x12 0x04 0x90 0x02 0x14    \.l.....
    decimal
             92    8  108   18    4  144    2   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2012-10-10T13:32:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-10-10T13:32:00)
    0000   0x80 0xa0 0x4d 0x0a 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 66 CalBGForPH 2012-10-10T15:49:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2012-10-10T15:49:57)
    0000   0xb9 0xb1 0x2f 0x0a 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 67 CalBGForPH 2012-10-10T17:13:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2012-10-10T17:13:57)
    0000   0xb9 0x8d 0x31 0x0a 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 68 CalBGForPH 2012-10-10T17:14:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2012-10-10T17:14:01)
    0000   0x81 0x8e 0x31 0x0a 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 ResultTotals 2012-08-10T13:12:42 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xd2                   .....
    decimal
              7    0    0    4  210
    datetime (2012-08-10T13:12:42)
    0000   0xaa 0x0c 0x6d 0xaa 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb6 0x8d 0x23 0x05 0x00 0x00    ....#...
    0008   0x04 0xd2 0x03 0x72 0x47 0x01 0x60 0x1d    ...rG.`.
    0010   0x00 0x36 0x01 0x60 0x1d 0x00 0xa0 0x2d    .6.`...-
    0018   0x00 0xc0 0x37 0x00 0x00 0x00 0x04 0x02    ..7.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  182  141   35    5    0    0
              4  210    3  114   71    1   96   29
              0   54    1   96   29    0  160   45
              0  192   55    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 70 PumpSuspend 2012-10-11T10:51:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-11T10:51:33)
    0000   0xa1 0xb3 0x0a 0x0b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 71 PumpResume 2012-10-11T11:06:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-11T11:06:50)
    0000   0xb2 0x86 0x0b 0x0b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 72 BolusWizard 2012-10-11T12:36:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-11T12:36:45)
    0000   0xad 0xa4 0x0c 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x00 0x2a 0x00    7P.-j.*.
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    0   42    0
              0    0    0   42  125
    HOUR BITS: [1, 0, 1]
#### RECORD 73 Bolus 2012-10-11T12:36:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'programmed': 4.2}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x02                        .**.
    decimal
              1   42   42    2
    datetime (2012-10-11T12:36:45)
    0000   0xad 0xa4 0x6c 0x0b 0x0c                   ..l..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 74 CalBGForPH 2012-10-11T15:02:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2012-10-11T15:02:07)
    0000   0x87 0x82 0x2f 0x0b 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 75 CalBGForPH 2012-10-11T21:36:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 209}
```
    op hex (2)
    0000   0x0a 0xd1                                  ..
    decimal
             10  209
    datetime (2012-10-11T21:36:59)
    0000   0xbb 0xa4 0x35 0x0b 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 76 BolusWizard 2012-10-11T21:37:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 209,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xd1                                  [.
    decimal
             91  209
    datetime (2012-10-11T21:37:04)
    0000   0x84 0xa5 0x15 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0    0    0   18  125
    HOUR BITS: [1, 0, 1]
#### RECORD 77 Bolus 2012-10-11T21:37:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'programmed': 1.4}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2012-10-11T21:37:04)
    0000   0x84 0xa5 0x55 0x0b 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-29.data: 78 records`
