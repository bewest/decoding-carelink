## START logs/ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6c 0xde                                  l.
##### DEBUG DECIMAL
            108  222
#### RECORD 0 hack1 2012-11-09T10:14:03 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0xa8 0x8c 0x05 0x00 0x75 0x4d 0x8d    m....uM.
    0008   0x05 0x00 0x00 0x05 0x34 0x03 0x6c 0x42    ....4.lB
    0010   0x01 0xc8 0x22 0x00 0x90 0x01 0xc8 0x22    .."...."
    0018   0x01 0xb4 0x60 0x00 0x14 0x04 0x00 0x00    ..`.....
    0020   0x00 0x03 0x01 0x00 0x02 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x21 0x00              ....!.
    decimal
            109  168  140    5    0  117   77  141
              5    0    0    5   52    3  108   66
              1  200   34    0  144    1  200   34
              1  180   96    0   20    4    0    0
              0    3    1    0    2    0   12    0
            232    0    0    0   33    0
    datetime (2012-11-09T10:14:03)
    0000   0x83 0xce 0x0a 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 Prime 2012-11-09T10:15:03 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x40                   ....@
    decimal
              3    0    0    0   64
    datetime (2012-11-09T10:15:03)
    0000   0x83 0xcf 0x2a 0x09 0x0c                   ..*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 Prime 2012-11-09T10:15:35 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-11-09T10:15:35)
    0000   0xa3 0xcf 0x0a 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2012-11-09T10:58:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2012-11-09T10:58:37)
    0000   0xa5 0xfa 0x2a 0x09 0x0c                   ..*..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 BolusWizard 2012-11-09T10:58:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 216,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2012-11-09T10:58:43)
    0000   0xab 0xfa 0x0a 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125
    HOUR BITS: [1, 1, 1]
#### RECORD 5 Bolus 2012-11-09T10:58:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'programmed': 2.2}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2012-11-09T10:58:43)
    0000   0xab 0xfa 0x4a 0x09 0x0c                   ..J..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 BolusWizard 2012-11-09T11:01:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-11-09T11:01:47)
    0000   0xaf 0xc1 0x0b 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125
    HOUR BITS: [1, 1, 0]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 2.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x07 0x04                   \.X..
    decimal
             92    5   88    7    4
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2012-11-09T11:01:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2012-11-09T11:01:47)
    0000   0xaf 0xc1 0x4b 0x09 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 CalBGForPH 2012-11-09T11:50:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2012-11-09T11:50:23)
    0000   0x97 0xf2 0x2b 0x09 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 BolusWizard 2012-11-09T11:50:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 216,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 62,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.8}
```
    op hex (2)
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2012-11-09T11:50:43)
    0000   0xab 0xf2 0x0b 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x14 0x2f 0x00    >P.-j./.
    0008   0x00 0x1c 0x00 0x2f 0x7d                   .../}
    decimal
             62   80   13   45  106   20   47    0
              0   28    0   47  125
    HOUR BITS: [1, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 3.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x84 0x38 0x04                   \..8.
    decimal
             92    5  132   56    4
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2012-11-09T11:50:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'programmed': 4.7}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2012-11-09T11:50:43)
    0000   0xab 0xf2 0x4b 0x09 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 CalBGForPH 2012-11-09T19:38:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-11-09T19:38:33)
    0000   0xa1 0xe6 0x33 0x09 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 BolusWizard 2012-11-09T19:39:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2012-11-09T19:39:20)
    0000   0x94 0xe7 0x13 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0x00 0x35 0x00    FP.-j.5.
    0008   0x00 0x00 0x00 0x35 0x7d                   ...5}
    decimal
             70   80   13   45  106    0   53    0
              0    0    0   53  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 219, 'amount': 4.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xbc 0xdb 0x14                   \....
    decimal
             92    5  188  219   20
    datetime (unknown)

    body (0)

#### RECORD 16 PumpSuspend 2012-11-09T19:39:23 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-09T19:39:23)
    0000   0x97 0xe7 0x13 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 Bolus 2012-11-09T19:39:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5, 'programmed': 0.1}
```
    op hex (4)
    0000   0x01 0x37 0x01 0x00                        .7..
    decimal
              1   55    1    0
    datetime (2012-11-09T19:39:20)
    0000   0x94 0xe7 0x53 0x09 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 PumpResume 2012-11-09T19:39:24 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-09T19:39:24)
    0000   0x98 0xe7 0x13 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 CalBGForPH 2012-11-09T19:39:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-11-09T19:39:33)
    0000   0xa1 0xe7 0x33 0x09 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 CalBGForPH 2012-11-09T19:40:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2012-11-09T19:40:27)
    0000   0x9b 0xe8 0x33 0x09 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 BolusWizard 2012-11-09T19:41:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.0,
 'carb_input': 79,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2012-11-09T19:41:14)
    0000   0x8e 0xe9 0x13 0x09 0x0c                   .....
    body (13)
    hex
    0000   0x4f 0x50 0x0d 0x2d 0x6a 0x00 0x3c 0x00    OP.-j.<.
    0008   0x00 0x01 0x00 0x3c 0x7d                   ...<}
    decimal
             79   80   13   45  106    0   60    0
              0    1    0   60  125
    HOUR BITS: [1, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 0.1, 'curve': 4},
 {'age': 221, 'amount': 4.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x04 0x07 0x04 0xbc 0xdd 0x14    \.......
    decimal
             92    8    4    7    4  188  221   20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2012-11-09T19:41:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-11-09T19:41:14)
    0000   0x8e 0xe9 0x93 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 Bolus 2012-11-09T19:43:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x02                        ....
    decimal
              1   29   29    2
    datetime (2012-11-09T19:43:16)
    0000   0x90 0xeb 0xb3 0x09 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 ResultTotals 2012-10-09T13:12:41 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xb8                   .....
    decimal
              7    0    0    5  184
    datetime (2012-10-09T13:12:41)
    0000   0xa9 0x8c 0x6d 0xa9 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x97 0x6c 0xd8 0x05 0x00 0x00    ...l....
    0008   0x05 0xb8 0x03 0x84 0x3d 0x02 0x34 0x27    ....=.4'
    0010   0x00 0xe2 0x02 0x34 0x27 0x01 0xd8 0x54    ...4'..T
    0018   0x00 0x5c 0x10 0x00 0x00 0x00 0x05 0x03    .\......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  151  108  216    5    0    0
              5  184    3  132   61    2   52   39
              0  226    2   52   39    1  216   84
              0   92   16    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 26 CalBGForPH 2012-11-10T00:50:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 278}
```
    op hex (2)
    0000   0x0a 0x16                                  ..
    decimal
             10   22
    datetime (2012-11-10T00:50:24)
    0000   0x98 0xf2 0x20 0x0a 0x8c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 27 BolusWizard 2012-11-10T00:50:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 278,
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
    0000   0x5b 0x16                                  [.
    decimal
             91   22
    datetime (2012-11-10T00:50:39)
    0000   0xa7 0xf2 0x00 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x22 0x00 0x00    .Q.-j"..
    0008   0x00 0x00 0x00 0x22 0x7d                   ..."}
    decimal
              0   81   13   45  106   34    0    0
              0    0    0   34  125
    HOUR BITS: [1, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 0.45, 'curve': 20},
 {'age': 10, 'amount': 0.5, 'curve': 20},
 {'age': 20, 'amount': 0.45, 'curve': 20},
 {'age': 30, 'amount': 0.5, 'curve': 20},
 {'age': 40, 'amount': 0.5, 'curve': 20},
 {'age': 50, 'amount': 0.45, 'curve': 20},
 {'age': 60, 'amount': 3.25, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x12 0x00 0x14 0x14 0x0a 0x14    \.......
    0008   0x12 0x14 0x14 0x14 0x1e 0x14 0x14 0x28    .......(
    0010   0x14 0x12 0x32 0x14 0x82 0x3c 0x14         ..2..<.
    decimal
             92   23   18    0   20   20   10   20
             18   20   20   20   30   20   20   40
             20   18   50   20  130   60   20
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2012-11-10T00:50:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-11-10T00:50:39)
    0000   0xa7 0xf2 0x40 0x0a 0x0c                   ..@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 CalBGForPH 2012-11-10T07:12:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 275}
```
    op hex (2)
    0000   0x0a 0x13                                  ..
    decimal
             10   19
    datetime (2012-11-10T07:12:27)
    0000   0x9b 0xcc 0x27 0x0a 0x8c                   ..'..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 31 BolusWizard 2012-11-10T07:12:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 275,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x13                                  [.
    decimal
             91   19
    datetime (2012-11-10T07:12:31)
    0000   0x9f 0xcc 0x07 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125
    HOUR BITS: [1, 1, 0]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 132, 'amount': 3.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0x84 0x14                   \....
    decimal
             92    5  144  132   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2012-11-10T07:12:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-11-10T07:12:31)
    0000   0x9f 0xcc 0x47 0x0a 0x0c                   ..G..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 34 PumpSuspend 2012-11-10T07:58:45 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-10T07:58:45)
    0000   0xad 0xfa 0x07 0x0a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 PumpResume 2012-11-10T08:03:39 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-10T08:03:39)
    0000   0xa7 0xc3 0x08 0x0a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 CalBGForPH 2012-11-10T08:05:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2012-11-10T08:05:15)
    0000   0x8f 0xc5 0x28 0x0a 0x0c                   ..(..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 CalBGForPH 2012-11-10T18:47:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2012-11-10T18:47:15)
    0000   0x8f 0xef 0x32 0x0a 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 BolusWizard 2012-11-10T18:47:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 95,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2012-11-10T18:47:42)
    0000   0xaa 0xef 0x12 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0xfd 0x2b 0xf0    8P.-j.+.
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
             56   80   13   45  106  253   43  240
              0    0    0   40  125
    HOUR BITS: [1, 1, 1]
#### RECORD 39 Bolus 2012-11-10T18:47:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'programmed': 4.0}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2012-11-10T18:47:42)
    0000   0xaa 0xef 0x52 0x0a 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 CalBGForPH 2012-11-10T19:48:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2012-11-10T19:48:57)
    0000   0xb9 0xf0 0x33 0x0a 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 CalBGForPH 2012-11-10T19:49:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 149}
```
    op hex (2)
    0000   0x0a 0x95                                  ..
    decimal
             10  149
    datetime (2012-11-10T19:49:05)
    0000   0x85 0xf1 0x33 0x0a 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 BolusWizard 2012-11-10T19:49:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 149,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 66,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 3.2}
```
    op hex (2)
    0000   0x5b 0x95                                  [.
    decimal
             91  149
    datetime (2012-11-10T19:49:31)
    0000   0x9f 0xf1 0x13 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0x05 0x32 0x00    BP.-j.2.
    0008   0x00 0x20 0x00 0x32 0x7d                   . .2}
    decimal
             66   80   13   45  106    5   50    0
              0   32    0   50  125
    HOUR BITS: [1, 1, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 4.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0x41 0x04                   \..A.
    decimal
             92    5  160   65    4
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2012-11-10T19:49:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'programmed': 5.0}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2012-11-10T19:49:31)
    0000   0x9f 0xf1 0x53 0x0a 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 45 BolusWizard 2012-11-10T20:49:10 head[2], body[13] op[0x5b]
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
    datetime (2012-11-10T20:49:10)
    0000   0x8a 0xf1 0x14 0x0a 0x0c                   .....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [1, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 5.0, 'curve': 4},
 {'age': 125, 'amount': 4.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xc8 0x41 0x04 0xa0 0x7d 0x04    \..A..}.
    decimal
             92    8  200   65    4  160  125    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-11-10T20:49:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-11-10T20:49:10)
    0000   0x8a 0xf1 0x54 0x0a 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 ResultTotals 2012-10-10T13:12:42 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x60                   ....`
    decimal
              7    0    0    6   96
    datetime (2012-10-10T13:12:42)
    0000   0xaa 0x8c 0x6d 0xaa 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xbe 0x5f 0x16 0x06 0x00 0x00    ..._....
    0008   0x06 0x60 0x03 0x80 0x37 0x02 0xe0 0x2d    .`..7..-
    0010   0x00 0x99 0x02 0xe0 0x2d 0x01 0xc4 0x3d    ....-..=
    0018   0x01 0x1c 0x27 0x00 0x00 0x00 0x05 0x03    ..'.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  190   95   22    6    0    0
              6   96    3  128   55    2  224   45
              0  153    2  224   45    1  196   61
              1   28   39    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 CalBGForPH 2012-11-11T01:59:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 224}
```
    op hex (2)
    0000   0x0a 0xe0                                  ..
    decimal
             10  224
    datetime (2012-11-11T01:59:01)
    0000   0x81 0xfb 0x21 0x0b 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 50 BolusWizard 2012-11-11T01:59:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 224,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xe0                                  [.
    decimal
             91  224
    datetime (2012-11-11T01:59:17)
    0000   0x91 0xfb 0x01 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x16 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
              0   80   13   45  106   22    0    0
              0    0    0   22  125
    HOUR BITS: [1, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 2.3, 'curve': 20},
 {'age': 119, 'amount': 5.0, 'curve': 20},
 {'age': 179, 'amount': 4.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x5c 0x3b 0x14 0xc8 0x77 0x14    \.\;..w.
    0008   0xa0 0xb3 0x14                             ...
    decimal
             92   11   92   59   20  200  119   20
            160  179   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2012-11-11T01:59:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'programmed': 2.7}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2012-11-11T01:59:17)
    0000   0x91 0xfb 0x41 0x0b 0x0c                   ..A..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 53 CalBGForPH 2012-11-11T07:03:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 339}
```
    op hex (2)
    0000   0x0a 0x53                                  .S
    decimal
             10   83
    datetime (2012-11-11T07:03:49)
    0000   0xb1 0xc3 0x27 0x0b 0x8c                   ..'..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 54 BolusWizard 2012-11-11T07:03:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 339,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x53                                  [S
    decimal
             91   83
    datetime (2012-11-11T07:03:57)
    0000   0xb9 0xc3 0x07 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2f 0x00 0x00    .Q.-j/..
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
              0   81   13   45  106   47    0    0
              0    0    0   47  125
    HOUR BITS: [1, 1, 0]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 2.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0x35 0x14                   \.l5.
    decimal
             92    5  108   53   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2012-11-11T07:03:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'programmed': 5.0}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2012-11-11T07:03:57)
    0000   0xb9 0xc3 0x47 0x0b 0x0c                   ..G..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 57 PumpSuspend 2012-11-11T09:37:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-11T09:37:05)
    0000   0x85 0xe5 0x09 0x0b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 58 PumpResume 2012-11-11T10:01:07 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-11T10:01:07)
    0000   0x87 0xc1 0x0a 0x0b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 CalBGForPH 2012-11-11T11:50:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2012-11-11T11:50:06)
    0000   0x86 0xf2 0x2b 0x0b 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 60 BolusWizard 2012-11-11T11:50:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2012-11-11T11:50:12)
    0000   0x8c 0xf2 0x0b 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    0    0    8  125
    HOUR BITS: [1, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 4.9, 'curve': 20},
 {'age': 40, 'amount': 0.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xc4 0x1e 0x14 0x04 0x28 0x14    \.....(.
    decimal
             92    8  196   30   20    4   40   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2012-11-11T11:50:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-11T11:50:12)
    0000   0x8c 0xf2 0x4b 0x0b 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 63 CalBGForPH 2012-11-11T11:54:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2012-11-11T11:54:42)
    0000   0xaa 0xf6 0x2b 0x0b 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 64 BolusWizard 2012-11-11T11:55:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2012-11-11T11:55:23)
    0000   0x97 0xf7 0x0b 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x08 0x26 0x00    2P.-j.&.
    0008   0x00 0x0a 0x00 0x26 0x7d                   ...&}
    decimal
             50   80   13   45  106    8   38    0
              0   10    0   38  125
    HOUR BITS: [1, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 1.0, 'curve': 4},
 {'age': 35, 'amount': 4.9, 'curve': 20},
 {'age': 45, 'amount': 0.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x0b 0x04 0xc4 0x23 0x14    \.(...#.
    0008   0x04 0x2d 0x14                             .-.
    decimal
             92   11   40   11    4  196   35   20
              4   45   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2012-11-11T11:55:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'programmed': 3.8}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2012-11-11T11:55:23)
    0000   0x97 0xf7 0x4b 0x0b 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 BolusWizard 2012-11-11T13:13:59 head[2], body[13] op[0x5b]
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
    datetime (2012-11-11T13:13:59)
    0000   0xbb 0xcd 0x0d 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [1, 1, 0]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 3.8, 'curve': 4},
 {'age': 89, 'amount': 1.0, 'curve': 4},
 {'age': 113, 'amount': 4.9, 'curve': 20},
 {'age': 123, 'amount': 0.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x98 0x4f 0x04 0x28 0x59 0x04    \..O.(Y.
    0008   0xc4 0x71 0x14 0x04 0x7b 0x14              .q..{.
    decimal
             92   14  152   79    4   40   89    4
            196  113   20    4  123   20
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2012-11-11T13:13:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-11-11T13:13:59)
    0000   0xbb 0xcd 0x4d 0x0b 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 70 CalBGForPH 2012-11-11T20:38:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2012-11-11T20:38:17)
    0000   0x91 0xe6 0x34 0x0b 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 71 BolusWizard 2012-11-11T20:39:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 159,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x9f                                  [.
    decimal
             91  159
    datetime (2012-11-11T20:39:34)
    0000   0xa2 0xe7 0x14 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x07 0x05 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
              7   80   13   45  106    7    5    0
              0    0    0   12  125
    HOUR BITS: [1, 1, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 189, 'amount': 1.85, 'curve': 20},
 {'age': 199, 'amount': 0.05, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4a 0xbd 0x14 0x02 0xc7 0x14    \.J.....
    decimal
             92    8   74  189   20    2  199   20
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2012-11-11T20:39:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-11-11T20:39:34)
    0000   0xa2 0xe7 0x54 0x0b 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 74 CalBGForPH 2012-11-11T22:30:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2012-11-11T22:30:34)
    0000   0xa2 0xde 0x36 0x0b 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 75 BolusWizard 2012-11-11T22:31:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 71,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 39,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.6}
```
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2012-11-11T22:31:44)
    0000   0xac 0xdf 0x16 0x0b 0x0c                   .....
    body (13)
    hex
    0000   0x27 0x50 0x0d 0x2d 0x6a 0xf8 0x1e 0xf0    'P.-j...
    0008   0x00 0x06 0x00 0x16 0x7d                   ....}
    decimal
             39   80   13   45  106  248   30  240
              0    6    0   22  125
    HOUR BITS: [1, 1, 0]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 117, 'amount': 1.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0x75 0x04                   \.0u.
    decimal
             92    5   48  117    4
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2012-11-11T22:31:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'programmed': 2.2}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2012-11-11T22:31:44)
    0000   0xac 0xdf 0x56 0x0b 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 78 ResultTotals 2012-10-11T13:12:43 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x3a                   ....:
    decimal
              7    0    0    6   58
    datetime (2012-10-11T13:12:43)
    0000   0xab 0x8c 0x6d 0xab 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xbb 0x47 0x53 0x06 0x00 0x00    ...GS...
    0008   0x06 0x3a 0x03 0x72 0x37 0x02 0xc8 0x2d    .:.r7..-
    0010   0x00 0x79 0x02 0xc8 0x2d 0x01 0x50 0x2f    .y..-.P/
    0018   0x01 0x78 0x35 0x00 0x00 0x00 0x07 0x03    .x5.....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  187   71   83    6    0    0
              6   58    3  114   55    2  200   45
              0  121    2  200   45    1   80   47
              1  120   53    0    0    0    7    3
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 79 CalBGForPH 2012-11-12T00:55:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2012-11-12T00:55:31)
    0000   0x9f 0xf7 0x20 0x0c 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-20.data: 80 records`
