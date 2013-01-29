## START logs/ReadHistoryData-page-31.data
#### RECORD 0 hack1 2012-09-28T07:49:10 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x9b 0x8c 0x05 0x00 0x9e 0x55 0xc5    m.....U.
    0008   0x03 0x00 0x00 0x05 0x10 0x03 0x74 0x44    ......tD
    0010   0x01 0x9c 0x20 0x00 0x84 0x01 0x9c 0x20    .. .... 
    0018   0x01 0x78 0x5b 0x00 0x24 0x09 0x00 0x00    .x[.$...
    0020   0x00 0x05 0x04 0x01 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x1e 0x00              ......
    decimal
            109  155  140    5    0  158   85  197
              3    0    0    5   16    3  116   68
              1  156   32    0  132    1  156   32
              1  120   91    0   36    9    0    0
              0    5    4    1    0    0   12    0
            232    0    0    0   30    0
    datetime (2012-09-28T07:49:10)
    0000   0x8a 0x71 0x07 0x1c 0x0c                   .q...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 1 PumpResume 2012-09-28T11:16:09 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-28T11:16:09)
    0000   0x89 0x50 0x0b 0x1c 0x0c                   .P...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 2 TempBasal 2012-09-28T11:53:29 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.15}
```
    op hex (2)
    0000   0x33 0x2e                                  3.
    decimal
             51   46
    datetime (2012-09-28T11:53:29)
    0000   0x9d 0x75 0x0b 0x1c 0x0c                   .u...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 1, 1]
#### RECORD 3 TempBasalDuration 2012-09-28T11:53:29 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2012-09-28T11:53:29)
    0000   0x9d 0x75 0x0b 0x1c 0x0c                   .u...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 CalBGForPH 2012-09-28T11:53:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 353}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2012-09-28T11:53:50)
    0000   0xb2 0x75 0x2b 0x1c 0x8c                   .u+..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 BolusWizard 2012-09-28T11:53:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 353,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x61                                  [a
    decimal
             91   97
    datetime (2012-09-28T11:53:55)
    0000   0xb7 0x75 0x0b 0x1c 0x0c                   .u...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x32 0x00 0x00    .Q.-j2..
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
              0   81   13   45  106   50    0    0
              0    0    0   50  125
    HOUR BITS: [0, 1, 1]
#### RECORD 6 Bolus 2012-09-28T11:53:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'programmed': 5.0}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2012-09-28T11:53:55)
    0000   0xb7 0x75 0x4b 0x1c 0x0c                   .uK..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 CalBGForPH 2012-09-28T13:10:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 330}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2012-09-28T13:10:20)
    0000   0x94 0x4a 0x2d 0x1c 0x8c                   .J-..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 BolusWizard 2012-09-28T13:10:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 330,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 3.7}
```
    op hex (2)
    0000   0x5b 0x4a                                  [J
    decimal
             91   74
    datetime (2012-09-28T13:10:28)
    0000   0x9c 0x4a 0x0d 0x1c 0x0c                   .J...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2d 0x00 0x00    .Q.-j-..
    0008   0x00 0x25 0x00 0x08 0x7d                   .%..}
    decimal
              0   81   13   45  106   45    0    0
              0   37    0    8  125
    HOUR BITS: [0, 1, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 76, 'amount': 4.85, 'curve': 4},
 {'age': 86, 'amount': 0.15, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xc2 0x4c 0x04 0x06 0x56 0x04    \..L..V.
    decimal
             92    8  194   76    4    6   86    4
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2012-09-28T13:10:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2012-09-28T13:10:28)
    0000   0x9c 0x4a 0x4d 0x1c 0x0c                   .JM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 11 BolusWizard 2012-09-28T13:11:38 head[2], body[13] op[0x5b]
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
    datetime (2012-09-28T13:11:38)
    0000   0xa6 0x4b 0x0d 0x1c 0x0c                   .K...
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x00 0x2a 0x00    7P.-j.*.
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    0   42    0
              0    0    0   42  125
    HOUR BITS: [0, 1, 0]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 1.1, 'curve': 4},
 {'age': 77, 'amount': 4.85, 'curve': 4},
 {'age': 87, 'amount': 0.15, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2c 0x07 0x04 0xc2 0x4d 0x04    \.,...M.
    0008   0x06 0x57 0x04                             .W.
    decimal
             92   11   44    7    4  194   77    4
              6   87    4
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2012-09-28T13:11:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'programmed': 4.2}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2012-09-28T13:11:38)
    0000   0xa6 0x4b 0x4d 0x1c 0x0c                   .KM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 14 CalBGForPH 2012-09-28T17:02:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2012-09-28T17:02:41)
    0000   0xa9 0x42 0x31 0x1c 0x0c                   .B1..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 15 CalBGForPH 2012-09-28T18:36:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 77}
```
    op hex (2)
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2012-09-28T18:36:08)
    0000   0x88 0x64 0x32 0x1c 0x0c                   .d2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2012-09-28T18:36:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 77,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x4d                                  [M
    decimal
             91   77
    datetime (2012-09-28T18:36:54)
    0000   0xb6 0x64 0x12 0x1c 0x0c                   .d...
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0xf9 0x25 0xf0    1P.-j.%.
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             49   80   13   45  106  249   37  240
              0    0    0   30  125
    HOUR BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 0.65, 'curve': 20},
 {'age': 76, 'amount': 4.65, 'curve': 20},
 {'age': 146, 'amount': 4.85, 'curve': 20},
 {'age': 156, 'amount': 0.15, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1a 0x42 0x14 0xba 0x4c 0x14    \..B..L.
    0008   0xc2 0x92 0x14 0x06 0x9c 0x14              ......
    decimal
             92   14   26   66   20  186   76   20
            194  146   20    6  156   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2012-09-28T18:36:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'programmed': 3.0}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2012-09-28T18:36:54)
    0000   0xb6 0x64 0x52 0x1c 0x0c                   .dR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 19 ResultTotals 2012-10-28T13:12:28 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x0c                   .....
    decimal
              7    0    0    5   12
    datetime (2012-10-28T13:12:28)
    0000   0x9c 0x8c 0x6d 0x9c 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xdc 0x4d 0x61 0x04 0x00 0x00    ...Ma...
    0008   0x05 0x0c 0x02 0xf8 0x3b 0x02 0x14 0x29    ....;..)
    0010   0x00 0x68 0x02 0x14 0x29 0x01 0x20 0x36    .h..). 6
    0018   0x00 0xf4 0x2e 0x00 0x00 0x00 0x04 0x02    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  220   77   97    4    0    0
              5   12    2  248   59    2   20   41
              0  104    2   20   41    1   32   54
              0  244   46    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 CalBGForPH 2012-09-29T01:11:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 248}
```
    op hex (2)
    0000   0x0a 0xf8                                  ..
    decimal
             10  248
    datetime (2012-09-29T01:11:09)
    0000   0x89 0x4b 0x21 0x1d 0x0c                   .K!..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 21 BolusWizard 2012-09-29T01:11:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 248,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xf8                                  [.
    decimal
             91  248
    datetime (2012-09-29T01:11:10)
    0000   0x8a 0x4b 0x01 0x1d 0x0c                   .K...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1b 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
              0   80   13   45  106   27    0    0
              0    0    0   27  125
    HOUR BITS: [0, 1, 0]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 141, 'amount': 3.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x8d 0x14                   \.x..
    decimal
             92    5  120  141   20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2012-09-29T01:11:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'programmed': 2.7}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2012-09-29T01:11:10)
    0000   0x8a 0x4b 0x41 0x1d 0x0c                   .KA..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 24 PumpSuspend 2012-09-29T19:58:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-29T19:58:33)
    0000   0xa1 0x7a 0x13 0x1d 0x0c                   .z...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 25 PumpResume 2012-09-29T21:04:01 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-29T21:04:01)
    0000   0x81 0x44 0x15 0x1d 0x0c                   .D...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 26 CalBGForPH 2012-09-29T21:04:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-09-29T21:04:11)
    0000   0x8b 0x44 0x35 0x1d 0x0c                   .D5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 27 BolusWizard 2012-09-29T21:04:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 100,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2012-09-29T21:04:30)
    0000   0x9e 0x44 0x15 0x1d 0x0c                   .D...
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0xfe 0x16 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             29   80   13   45  106  254   22  240
              0    0    0   20  125
    HOUR BITS: [0, 1, 0]
#### RECORD 28 Bolus 2012-09-29T21:04:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-09-29T21:04:30)
    0000   0x9e 0x44 0x55 0x1d 0x0c                   .DU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 29 BolusWizard 2012-09-29T21:22:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-29T21:22:09)
    0000   0x89 0x56 0x15 0x1d 0x0c                   .V...
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    0    0   18  125
    HOUR BITS: [0, 1, 0]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x12 0x04                   \.P..
    decimal
             92    5   80   18    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-09-29T21:22:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-09-29T21:22:09)
    0000   0x89 0x56 0x55 0x1d 0x0c                   .VU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 32 ResultTotals 2012-10-29T13:12:29 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x5e                   ....^
    decimal
              7    0    0    4   94
    datetime (2012-10-29T13:12:29)
    0000   0x9d 0x8c 0x6d 0x9d 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xae 0x64 0xf8 0x02 0x00 0x00    ...d....
    0008   0x04 0x5e 0x03 0x5a 0x4d 0x01 0x04 0x17    .^.ZM...
    0010   0x00 0x35 0x01 0x04 0x17 0x00 0x98 0x3a    .5.....:
    0018   0x00 0x6c 0x2a 0x00 0x00 0x00 0x03 0x02    .l*.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  174  100  248    2    0    0
              4   94    3   90   77    1    4   23
              0   53    1    4   23    0  152   58
              0  108   42    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 CalBGForPH 2012-09-30T02:03:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 305}
```
    op hex (2)
    0000   0x0a 0x31                                  .1
    decimal
             10   49
    datetime (2012-09-30T02:03:54)
    0000   0xb6 0x43 0x22 0x1e 0x8c                   .C"..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 BolusWizard 2012-09-30T02:04:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 305,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x31                                  [1
    decimal
             91   49
    datetime (2012-09-30T02:04:02)
    0000   0x82 0x44 0x02 0x1e 0x0c                   .D...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x28 0x00 0x00    .Q.-j(..
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
              0   81   13   45  106   40    0    0
              0    0    0   40  125
    HOUR BITS: [0, 1, 0]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 1.8, 'curve': 20},
 {'age': 44, 'amount': 2.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0x22 0x14 0x50 0x2c 0x14    \.H".P,.
    decimal
             92    8   72   34   20   80   44   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2012-09-30T02:04:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'programmed': 4.2}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2012-09-30T02:04:02)
    0000   0x82 0x44 0x42 0x1e 0x0c                   .DB..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 37 LowReservoir 2012-09-30T04:07:30 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-09-30T04:07:30)
    0000   0x9e 0x47 0x04 0x1e 0x0c                   .G...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 LowReservoir 2012-09-30T14:18:56 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-09-30T14:18:56)
    0000   0xb8 0x52 0x0e 0x1e 0x0c                   .R...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 39 PumpSuspend 2012-09-30T17:08:40 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-30T17:08:40)
    0000   0xa8 0x48 0x11 0x1e 0x0c                   .H...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 40 PumpResume 2012-09-30T17:36:14 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-30T17:36:14)
    0000   0x8e 0x64 0x11 0x1e 0x0c                   .d...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 41 CalBGForPH 2012-09-30T20:02:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2012-09-30T20:02:19)
    0000   0x93 0x42 0x34 0x1e 0x0c                   .B4..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 42 BolusWizard 2012-09-30T20:02:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 154,
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
    0000   0x5b 0x9a                                  [.
    decimal
             91  154
    datetime (2012-09-30T20:02:25)
    0000   0x99 0x42 0x14 0x1e 0x0c                   .B...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    0    0    6  125
    HOUR BITS: [0, 1, 0]
#### RECORD 43 Bolus 2012-09-30T20:02:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'programmed': 0.6}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-09-30T20:02:25)
    0000   0x99 0x42 0x54 0x1e 0x0c                   .BT..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 44 BolusWizard 2012-09-30T20:29:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-30T20:29:35)
    0000   0xa3 0x5d 0x14 0x1e 0x0c                   .]...
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0x00 0x23 0x00    .P.-j.#.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             46   80   13   45  106    0   35    0
              0    0    0   35  125
    HOUR BITS: [0, 1, 0]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 0.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x18 0x23 0x04                   \..#.
    decimal
             92    5   24   35    4
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2012-09-30T20:29:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-09-30T20:29:35)
    0000   0xa3 0x5d 0x54 0x1e 0x0c                   .]T..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 47 ResultTotals 2012-10-30T13:12:30 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbe                   .....
    decimal
              7    0    0    4  190
    datetime (2012-10-30T13:12:30)
    0000   0x9e 0x8c 0x6d 0x9e 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xe6 0x9a 0x31 0x02 0x00 0x00    ....1...
    0008   0x04 0xbe 0x03 0x72 0x49 0x01 0x4c 0x1b    ...rI.L.
    0010   0x00 0x2e 0x01 0x4c 0x1b 0x00 0x8c 0x2a    ...L...*
    0018   0x00 0xc0 0x3a 0x00 0x00 0x00 0x03 0x01    ..:.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  230  154   49    2    0    0
              4  190    3  114   73    1   76   27
              0   46    1   76   27    0  140   42
              0  192   58    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 48 PumpSuspend 2012-10-01T14:42:35 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-01T14:42:35)
    0000   0xa3 0xaa 0x0e 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 PumpResume 2012-10-01T15:14:32 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-01T15:14:32)
    0000   0xa0 0x8e 0x0f 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 Rewind 2012-10-01T15:14:38 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-10-01T15:14:38)
    0000   0xa6 0x8e 0x0f 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 Prime 2012-10-01T15:16:42 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2d                   ....-
    decimal
              3    0    0    0   45
    datetime (2012-10-01T15:16:42)
    0000   0xaa 0x90 0x2f 0x01 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 52 Prime 2012-10-01T15:17:01 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-10-01T15:17:01)
    0000   0x81 0x91 0x0f 0x01 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 CalBGForPH 2012-10-01T15:58:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2012-10-01T15:58:56)
    0000   0xb8 0xba 0x2f 0x01 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 54 BolusWizard 2012-10-01T15:59:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 54,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2012-10-01T15:59:28)
    0000   0x9c 0xbb 0x0f 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x36 0x50 0x0d 0x2d 0x6a 0xfa 0x29 0xf0    6P.-j.).
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             54   80   13   45  106  250   41  240
              0    0    0   35  125
    HOUR BITS: [1, 0, 1]
#### RECORD 55 Bolus 2012-10-01T15:59:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-10-01T15:59:28)
    0000   0x9c 0xbb 0x4f 0x01 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 56 BolusWizard 2012-10-01T16:03:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-01T16:03:32)
    0000   0xa0 0x83 0x10 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [1, 0, 0]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 3.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x09 0x04                   \....
    decimal
             92    5  140    9    4
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2012-10-01T16:03:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-10-01T16:03:32)
    0000   0xa0 0x83 0x50 0x01 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 BolusWizard 2012-10-01T16:39:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 14,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-01T16:39:57)
    0000   0xb9 0xa7 0x10 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 0, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 0.5, 'curve': 4},
 {'age': 45, 'amount': 4.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x23 0x04 0xa8 0x2d 0x04    \..#..-.
    decimal
             92    8   20   35    4  168   45    4
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2012-10-01T16:39:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-10-01T16:39:57)
    0000   0xb9 0xa7 0x50 0x01 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 62 CalBGForPH 2012-10-01T18:08:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2012-10-01T18:08:17)
    0000   0x91 0x88 0x32 0x01 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 BolusWizard 2012-10-01T18:08:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 157,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.5}
```
    op hex (2)
    0000   0x5b 0x9d                                  [.
    decimal
             91  157
    datetime (2012-10-01T18:08:29)
    0000   0x9d 0x88 0x12 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x07 0x0a 0x00    .P.-j...
    0008   0x00 0x19 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    7   10    0
              0   25    0   10  125
    HOUR BITS: [1, 0, 0]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 1.0, 'curve': 4},
 {'age': 124, 'amount': 0.5, 'curve': 4},
 {'age': 134, 'amount': 4.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x5e 0x04 0x14 0x7c 0x04    \.(^..|.
    0008   0xa8 0x86 0x04                             ...
    decimal
             92   11   40   94    4   20  124    4
            168  134    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2012-10-01T18:08:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-10-01T18:08:30)
    0000   0x9e 0x88 0x52 0x01 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 66 CalBGForPH 2012-10-01T20:04:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 203}
```
    op hex (2)
    0000   0x0a 0xcb                                  ..
    decimal
             10  203
    datetime (2012-10-01T20:04:19)
    0000   0x93 0x84 0x34 0x01 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 67 BolusWizard 2012-10-01T20:04:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 203,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.6}
```
    op hex (2)
    0000   0x5b 0xcb                                  [.
    decimal
             91  203
    datetime (2012-10-01T20:04:25)
    0000   0x99 0x84 0x14 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x11 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   17    0    0
              0    6    0   11  125
    HOUR BITS: [1, 0, 0]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 120, 'amount': 1.0, 'curve': 4},
 {'age': 210, 'amount': 1.0, 'curve': 4},
 {'age': 240, 'amount': 0.5, 'curve': 4},
 {'age': 250, 'amount': 4.2, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x78 0x04 0x28 0xd2 0x04    \.(x.(..
    0008   0x14 0xf0 0x04 0xa8 0xfa 0x04              ......
    decimal
             92   14   40  120    4   40  210    4
             20  240    4  168  250    4
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2012-10-01T20:04:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-10-01T20:04:26)
    0000   0x9a 0x84 0x54 0x01 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 70 CalBGForPH 2012-10-01T20:34:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2012-10-01T20:34:27)
    0000   0x9b 0xa2 0x34 0x01 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 71 BolusWizard 2012-10-01T20:34:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-01T20:34:40)
    0000   0xa8 0xa2 0x14 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x00 0x20 0x00    *P.-j. .
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106    0   32    0
              0    0    0   32  125
    HOUR BITS: [1, 0, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.5, 'curve': 4},
 {'age': 150, 'amount': 1.0, 'curve': 4},
 {'age': 240, 'amount': 1.0, 'curve': 4},
 {'age': 14, 'amount': 0.5, 'curve': 20},
 {'age': 24, 'amount': 4.2, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x3c 0x1e 0x04 0x28 0x96 0x04    \.<..(..
    0008   0x28 0xf0 0x04 0x14 0x0e 0x14 0xa8 0x18    (.......
    0010   0x14                                       .
    decimal
             92   17   60   30    4   40  150    4
             40  240    4   20   14   20  168   24
             20
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2012-10-01T20:34:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-10-01T20:34:40)
    0000   0xa8 0xa2 0x54 0x01 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 74 CalBGForPH 2012-10-01T21:19:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 255}
```
    op hex (2)
    0000   0x0a 0xff                                  ..
    decimal
             10  255
    datetime (2012-10-01T21:19:22)
    0000   0x96 0x93 0x35 0x01 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 75 CalBGForPH 2012-10-01T23:43:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2012-10-01T23:43:58)
    0000   0xba 0xab 0x37 0x01 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 76 BolusWizard 2012-10-01T23:44:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 202,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.6}
```
    op hex (2)
    0000   0x5b 0xca                                  [.
    decimal
             91  202
    datetime (2012-10-01T23:44:01)
    0000   0x81 0xac 0x17 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x11 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   17    0    0
              0    6    0   11  125
    HOUR BITS: [1, 0, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 190, 'amount': 3.2, 'curve': 4},
 {'age': 220, 'amount': 1.5, 'curve': 4},
 {'age': 84, 'amount': 1.0, 'curve': 20},
 {'age': 174, 'amount': 1.0, 'curve': 20},
 {'age': 204, 'amount': 0.5, 'curve': 20},
 {'age': 214, 'amount': 4.2, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x80 0xbe 0x04 0x3c 0xdc 0x04    \....<..
    0008   0x28 0x54 0x14 0x28 0xae 0x14 0x14 0xcc    (T.(....
    0010   0x14 0xa8 0xd6 0x14                        ....
    decimal
             92   20  128  190    4   60  220    4
             40   84   20   40  174   20   20  204
             20  168  214   20
    datetime (unknown)

    body (0)

#### RECORD 78 Base unknown head[2], body[0] op[0xba]

    op hex (2)
    0000   0xba 0xf8                                  ..
    decimal
            186  248
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-31.data: 79 records`
