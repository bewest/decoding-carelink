## START logs/ReadHistoryData-page-22.data
#### RECORD 0 CalForBG 2012-11-01T15:43:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 54}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2012-11-01T15:43:51)
    0000   0xb3 0xeb 0x2f 0x01 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 CalForBG 2012-11-01T16:54:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 60}
```
    op hex (2)
    0000   0x0a 0x3c                                  .<
    decimal
             10   60
    datetime (2012-11-01T16:54:55)
    0000   0xb7 0xf6 0x30 0x01 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 CalForBG 2012-11-01T18:23:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2012-11-01T18:23:40)
    0000   0xa8 0xd7 0x32 0x01 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BolusWizard 2012-11-01T18:23:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 136,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2012-11-01T18:23:49)
    0000   0xb1 0xd7 0x12 0x01 0x0c                   .....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0x02 0x16 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
             29   80   13   45  106    2   22    0
              0    0    0   24  125
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 1.2, 'curve': 20},
 {'age': 113, 'amount': 2.0, 'curve': 20},
 {'age': 123, 'amount': 4.8, 'curve': 20},
 {'age': 133, 'amount': 0.8, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x30 0x35 0x14 0x50 0x71 0x14    \.05.Pq.
    0008   0xc0 0x7b 0x14 0x20 0x85 0x14              .{. ..
    decimal
             92   14   48   53   20   80  113   20
            192  123   20   32  133   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-11-01T18:23:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2012-11-01T18:23:49)
    0000   0xb1 0xd7 0x52 0x01 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 ResultTotals 2012-10-01T13:12:33 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x3a                   ....:
    decimal
              7    0    0    5   58
    datetime (2012-10-01T13:12:33)
    0000   0xa1 0x8c 0x6d 0xa1 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x66 0x36 0x88 0x05 0x00 0x00    ..f6....
    0008   0x05 0x3a 0x03 0x7a 0x43 0x01 0xc0 0x21    .:.zC..!
    0010   0x00 0x88 0x01 0xc0 0x21 0x01 0x9c 0x5c    ....!..\
    0018   0x00 0x24 0x08 0x00 0x00 0x00 0x05 0x03    .$......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  102   54  136    5    0    0
              5   58    3  122   67    1  192   33
              0  136    1  192   33    1  156   92
              0   36    8    0    0    0    5    3
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 7 PumpSuspend 2012-11-02T13:45:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-02T13:45:01)
    0000   0x81 0xed 0x0d 0x02 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 PumpResume 2012-11-02T14:00:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-02T14:00:33)
    0000   0xa1 0xc0 0x0e 0x02 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 CalForBG 2012-11-02T14:35:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 77}
```
    op hex (2)
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2012-11-02T14:35:06)
    0000   0x86 0xe3 0x2e 0x02 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 BolusWizard 2012-11-02T14:35:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 77,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x4d                                  [M
    decimal
             91   77
    datetime (2012-11-02T14:35:29)
    0000   0x9d 0xe3 0x0e 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0xf9 0x31 0xf0    @P.-j.1.
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
             64   80   13   45  106  249   49  240
              0    0    0   42  125
    HOUR BITS: [1, 1, 1]
#### RECORD 11 Bolus 2012-11-02T14:35:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'programmed': 4.2}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2012-11-02T14:35:29)
    0000   0x9d 0xe3 0x4e 0x02 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 12 BolusWizard 2012-11-02T16:14:27 head[2], body[13] op[0x5b]
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
    datetime (2012-11-02T16:14:27)
    0000   0x9b 0xce 0x10 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [1, 1, 0]
#### RECORD 13 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 4.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0x64 0x04                   \..d.
    decimal
             92    5  168  100    4
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2012-11-02T16:14:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-11-02T16:14:27)
    0000   0x9b 0xce 0x50 0x02 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalForBG 2012-11-02T16:50:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 149}
```
    op hex (2)
    0000   0x0a 0x95                                  ..
    decimal
             10  149
    datetime (2012-11-02T16:50:18)
    0000   0x92 0xf2 0x30 0x02 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 16 BolusWizard 2012-11-02T16:58:28 head[2], body[13] op[0x5b]
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
    datetime (2012-11-02T16:58:28)
    0000   0x9c 0xfa 0x10 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 1, 1]
#### RECORD 17 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 1.2, 'curve': 4},
 {'age': 144, 'amount': 4.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x2c 0x04 0xa8 0x90 0x04    \.0,....
    decimal
             92    8   48   44    4  168  144    4
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2012-11-02T16:58:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-02T16:58:28)
    0000   0x9c 0xfa 0x50 0x02 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 19 CalForBG 2012-11-02T18:34:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2012-11-02T18:34:05)
    0000   0x85 0xe2 0x32 0x02 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 BolusWizard 2012-11-02T20:03:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-11-02T20:03:23)
    0000   0x97 0xc3 0x14 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    "P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             34   80   13   45  106    0   26    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 0]
#### RECORD 21 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 189, 'amount': 1.0, 'curve': 4},
 {'age': 229, 'amount': 1.2, 'curve': 4},
 {'age': 73, 'amount': 4.2, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0xbd 0x04 0x30 0xe5 0x04    \.(..0..
    0008   0xa8 0x49 0x14                             .I.
    decimal
             92   11   40  189    4   48  229    4
            168   73   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2012-11-02T20:03:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-11-02T20:03:23)
    0000   0x97 0xc3 0x54 0x02 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 CalForBG 2012-11-02T21:59:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-11-02T21:59:25)
    0000   0x99 0xfb 0x35 0x02 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 CalForBG 2012-11-02T23:32:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2012-11-02T23:32:23)
    0000   0x97 0xe0 0x37 0x02 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 BolusWizard 2012-11-02T23:32:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 106,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2012-11-02T23:32:35)
    0000   0xa3 0xe0 0x17 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0x00 0x35 0x00    FP.-j.5.
    0008   0x00 0x03 0x00 0x35 0x7d                   ...5}
    decimal
             70   80   13   45  106    0   53    0
              0    3    0   53  125
    HOUR BITS: [1, 1, 1]
#### RECORD 26 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 208, 'amount': 1.7, 'curve': 4},
 {'age': 218, 'amount': 0.9, 'curve': 4},
 {'age': 142, 'amount': 1.0, 'curve': 20},
 {'age': 182, 'amount': 1.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x44 0xd0 0x04 0x24 0xda 0x04    \.D..$..
    0008   0x28 0x8e 0x14 0x30 0xb6 0x14              (..0..
    decimal
             92   14   68  208    4   36  218    4
             40  142   20   48  182   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2012-11-02T23:32:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'programmed': 5.3}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2012-11-02T23:32:36)
    0000   0xa4 0xe0 0x57 0x02 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 ResultTotals 2012-10-02T13:12:34 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xb4                   .....
    decimal
              7    0    0    5  180
    datetime (2012-10-02T13:12:34)
    0000   0xa2 0x8c 0x6d 0xa2 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x65 0x4d 0x95 0x05 0x00 0x00    ..eM....
    0008   0x05 0xb4 0x03 0x78 0x3d 0x02 0x3c 0x27    ...x=.<'
    0010   0x00 0xc6 0x02 0x3c 0x27 0x02 0x3c 0x64    ...<'.<d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x05 0x05    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  101   77  149    5    0    0
              5  180    3  120   61    2   60   39
              0  198    2   60   39    2   60  100
              0    0    0    0    0    0    5    5
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 CalForBG 2012-11-03T03:52:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2012-11-03T03:52:28)
    0000   0x9c 0xf4 0x23 0x03 0x0c                   ..#..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 CalForBG 2012-11-03T03:53:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2012-11-03T03:53:47)
    0000   0xaf 0xf5 0x23 0x03 0x0c                   ..#..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 31 CalForBG 2012-11-03T08:39:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2012-11-03T08:39:39)
    0000   0xa7 0xe7 0x28 0x03 0x0c                   ..(..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 BolusWizard 2012-11-03T08:39:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 180,
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
    0000   0x5b 0xb4                                  [.
    decimal
             91  180
    datetime (2012-11-03T08:39:41)
    0000   0xa9 0xe7 0x08 0x03 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    0    0   12  125
    HOUR BITS: [1, 1, 1]
#### RECORD 33 Bolus 2012-11-03T08:39:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-11-03T08:39:41)
    0000   0xa9 0xe7 0x48 0x03 0x0c                   ..H..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 TempBasal 2012-11-03T11:09:08 head[2], body[1] op[0x33]

    op hex (2)
    0000   0x33 0x30                                  30
    decimal
             51   48
    datetime (2012-11-03T11:09:08)
    0000   0x88 0xc9 0x0b 0x03 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 0]
#### RECORD 35 EndTempBasal 2012-11-03T11:09:08 head[2], body[0] op[0x16]

    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2012-11-03T11:09:08)
    0000   0x88 0xc9 0x0b 0x03 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 TempBasal 2012-11-03T11:09:16 head[2], body[1] op[0x33]

    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2012-11-03T11:09:16)
    0000   0x90 0xc9 0x0b 0x03 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 0]
#### RECORD 37 EndTempBasal 2012-11-03T11:09:16 head[2], body[0] op[0x16]

    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2012-11-03T11:09:16)
    0000   0x90 0xc9 0x0b 0x03 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 38 CalForBG 2012-11-03T11:09:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 168}
```
    op hex (2)
    0000   0x0a 0xa8                                  ..
    decimal
             10  168
    datetime (2012-11-03T11:09:41)
    0000   0xa9 0xc9 0x2b 0x03 0x8c                   ..+..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 39 BolusWizard 2012-11-03T11:09:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 424,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0xa8                                  [.
    decimal
             91  168
    datetime (2012-11-03T11:09:43)
    0000   0xab 0xc9 0x0b 0x03 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x42 0x00 0x00    .Q.-jB..
    0008   0x00 0x04 0x00 0x3e 0x7d                   ...>}
    decimal
              0   81   13   45  106   66    0    0
              0    4    0   62  125
    HOUR BITS: [1, 1, 0]
#### RECORD 40 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 155, 'amount': 1.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0x9b 0x04                   \.0..
    decimal
             92    5   48  155    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2012-11-03T11:09:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2, 'programmed': 6.2}
```
    op hex (4)
    0000   0x01 0x3e 0x3e 0x00                        .>>.
    decimal
              1   62   62    0
    datetime (2012-11-03T11:09:44)
    0000   0xac 0xc9 0x4b 0x03 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 42 TempBasal 2012-11-03T11:27:44 head[2], body[1] op[0x33]

    op hex (2)
    0000   0x33 0x36                                  36
    decimal
             51   54
    datetime (2012-11-03T11:27:44)
    0000   0xac 0xdb 0x0b 0x03 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 0]
#### RECORD 43 EndTempBasal 2012-11-03T11:27:44 head[2], body[0] op[0x16]

    op hex (2)
    0000   0x16 0x06                                  ..
    decimal
             22    6
    datetime (2012-11-03T11:27:44)
    0000   0xac 0xdb 0x0b 0x03 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 44 CalForBG 2012-11-03T12:13:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2012-11-03T12:13:26)
    0000   0x9a 0xcd 0x2c 0x03 0x8c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 45 BolusWizard 2012-11-03T12:13:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 373,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 4.9}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2012-11-03T12:13:36)
    0000   0xa4 0xcd 0x0c 0x03 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x37 0x00 0x00    .Q.-j7..
    0008   0x00 0x31 0x00 0x06 0x7d                   .1..}
    decimal
              0   81   13   45  106   55    0    0
              0   49    0    6  125
    HOUR BITS: [1, 1, 0]
#### RECORD 46 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 6.2, 'curve': 4},
 {'age': 219, 'amount': 1.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xf8 0x45 0x04 0x30 0xdb 0x04    \..E.0..
    decimal
             92    8  248   69    4   48  219    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-11-03T12:13:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'programmed': 1.2}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2012-11-03T12:13:36)
    0000   0xa4 0xcd 0x4c 0x03 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 CalForBG 2012-11-03T14:32:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2012-11-03T14:32:49)
    0000   0xb1 0xe0 0x2e 0x03 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 CalForBG 2012-11-03T20:14:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 45}
```
    op hex (2)
    0000   0x0a 0x2d                                  .-
    decimal
             10   45
    datetime (2012-11-03T20:14:04)
    0000   0x84 0xce 0x34 0x03 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 CalForBG 2012-11-03T21:29:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2012-11-03T21:29:23)
    0000   0x97 0xdd 0x35 0x03 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 51 BolusWizard 2012-11-03T21:29:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 131,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 62,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2012-11-03T21:29:42)
    0000   0xaa 0xdd 0x15 0x03 0x0c                   .....
    body (13)
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x01 0x2f 0x00    >P.-j./.
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
             62   80   13   45  106    1   47    0
              0    0    0   48  125
    HOUR BITS: [1, 1, 0]
#### RECORD 52 Bolus 2012-11-03T21:29:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'programmed': 4.8}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2012-11-03T21:29:42)
    0000   0xaa 0xdd 0x55 0x03 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 ResultTotals 2012-10-03T13:12:35 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xc0                   .....
    decimal
              7    0    0    5  192
    datetime (2012-10-03T13:12:35)
    0000   0xa3 0x8c 0x6d 0xa3 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb8 0x2d 0xa8 0x08 0x00 0x00    ...-....
    0008   0x05 0xc0 0x03 0xa8 0x40 0x02 0x18 0x24    ....@..$
    0010   0x00 0x3e 0x02 0x18 0x24 0x00 0xbc 0x23    .>..$..#
    0018   0x01 0x5c 0x41 0x00 0x00 0x00 0x04 0x00    .\A.....
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  184   45  168    8    0    0
              5  192    3  168   64    2   24   36
              0   62    2   24   36    0  188   35
              1   92   65    0    0    0    4    0
              3    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 54 CalForBG 2012-11-04T01:25:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 214}
```
    op hex (2)
    0000   0x0a 0xd6                                  ..
    decimal
             10  214
    datetime (2012-11-04T01:25:52)
    0000   0xb4 0xd9 0x21 0x04 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 BolusWizard 2012-11-04T01:25:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 214,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xd6                                  [.
    decimal
             91  214
    datetime (2012-11-04T01:25:59)
    0000   0xbb 0xd9 0x01 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x13 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
              0   80   13   45  106   19    0    0
              0    0    0   19  125
    HOUR BITS: [1, 1, 0]
#### RECORD 56 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 241, 'amount': 4.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xc0 0xf1 0x04                   \....
    decimal
             92    5  192  241    4
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2012-11-04T01:25:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-11-04T01:25:59)
    0000   0xbb 0xd9 0x41 0x04 0x0c                   ..A..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 58 CalForBG 2012-11-04T07:27:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 240}
```
    op hex (2)
    0000   0x0a 0xf0                                  ..
    decimal
             10  240
    datetime (2012-11-04T07:27:14)
    0000   0x8e 0xdb 0x27 0x04 0x0c                   ..'..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 59 BolusWizard 2012-11-04T07:27:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 240,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xf0                                  [.
    decimal
             91  240
    datetime (2012-11-04T07:27:26)
    0000   0x9a 0xdb 0x07 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x19 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
              0   80   13   45  106   25    0    0
              0    0    0   25  125
    HOUR BITS: [1, 1, 0]
#### RECORD 60 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 107, 'amount': 2.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x6b 0x14                   \.\k.
    decimal
             92    5   92  107   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2012-11-04T07:27:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'programmed': 2.8}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2012-11-04T07:27:26)
    0000   0x9a 0xdb 0x47 0x04 0x0c                   ..G..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 BolusWizard 2012-11-04T08:12:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-11-04T08:12:30)
    0000   0x9e 0xcc 0x08 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x00 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x00 0x7d                   ....}
    decimal
              0   80   13   45  106    0    0    0
              0    0    0    0  125
    HOUR BITS: [1, 1, 0]
#### RECORD 63 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 2.8, 'curve': 4},
 {'age': 152, 'amount': 2.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x70 0x30 0x04 0x5c 0x98 0x14    \.p0.\..
    decimal
             92    8  112   48    4   92  152   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2012-11-04T08:12:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-11-04T08:12:30)
    0000   0x9e 0xcc 0x48 0x04 0x0c                   ..H..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 CalForBG 2012-11-04T12:57:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 217}
```
    op hex (2)
    0000   0x0a 0xd9                                  ..
    decimal
             10  217
    datetime (2012-11-04T12:57:01)
    0000   0x81 0xf9 0x2c 0x04 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 TempBasal 2012-11-04T12:57:35 head[2], body[1] op[0x33]

    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2012-11-04T12:57:35)
    0000   0xa3 0xf9 0x0c 0x04 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 1, 1]
#### RECORD 67 EndTempBasal 2012-11-04T12:57:35 head[2], body[0] op[0x16]

    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2012-11-04T12:57:35)
    0000   0xa3 0xf9 0x0c 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 68 CalForBG 2012-11-04T12:57:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 217}
```
    op hex (2)
    0000   0x0a 0xd9                                  ..
    decimal
             10  217
    datetime (2012-11-04T12:57:57)
    0000   0xb9 0xf9 0x2c 0x04 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 69 BolusWizard 2012-11-04T12:58:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 217,
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
    0000   0x5b 0xd9                                  [.
    decimal
             91  217
    datetime (2012-11-04T12:58:06)
    0000   0x86 0xfa 0x0c 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125
    HOUR BITS: [1, 1, 1]
#### RECORD 70 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 0.5, 'curve': 20},
 {'age': 78, 'amount': 2.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x26 0x14 0x70 0x4e 0x14    \..&.pN.
    decimal
             92    8   20   38   20  112   78   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2012-11-04T12:58:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'programmed': 2.1}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2012-11-04T12:58:06)
    0000   0x86 0xfa 0x4c 0x04 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 72 LowReservoir 2012-11-04T17:44:12 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-11-04T17:44:12)
    0000   0x8c 0xec 0x11 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 73 PumpSuspend 2012-11-04T17:50:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-04T17:50:00)
    0000   0x80 0xf2 0x11 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 74 PumpResume 2012-11-04T18:17:43 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-04T18:17:43)
    0000   0xab 0xd1 0x12 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 75 CalForBG 2012-11-04T19:40:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2012-11-04T19:40:57)
    0000   0xb9 0xe8 0x33 0x04 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 76 BolusWizard 2012-11-04T19:40:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 170,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2012-11-04T19:40:59)
    0000   0xbb 0xe8 0x13 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125
    HOUR BITS: [1, 1, 1]
#### RECORD 77 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 2.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x54 0x96 0x14                   \.T..
    decimal
             92    5   84  150   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2012-11-04T19:40:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-04T19:40:59)
    0000   0xbb 0xe8 0x53 0x04 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 79 CalForBG 2012-11-04T21:53:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 251}
```
    op hex (2)
    0000   0x0a 0xfb                                  ..
    decimal
             10  251
    datetime (2012-11-04T21:53:35)
    0000   0xa3 0xf5 0x35 0x04 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 80 BolusWizard 2012-11-04T21:53:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 251,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0xfb                                  [.
    decimal
             91  251
    datetime (2012-11-04T21:53:40)
    0000   0xa8 0xf5 0x15 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x04 0x00 0x18 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    4    0   24  125
    HOUR BITS: [1, 1, 1]
#### RECORD 81 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 1.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x8b 0x04                   \.(..
    decimal
             92    5   40  139    4
    datetime (unknown)

    body (0)

#### RECORD 82 Bolus 2012-11-04T21:53:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-11-04T21:53:40)
    0000   0xa8 0xf5 0x55 0x04 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 83 BolusWizard 2012-11-04T22:39:51 head[2], body[13] op[0x5b]
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
    datetime (2012-11-04T22:39:51)
    0000   0xb3 0xe7 0x16 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 1, 1]
#### RECORD 84 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 2.15, 'curve': 4},
 {'age': 55, 'amount': 0.45, 'curve': 4},
 {'age': 185, 'amount': 1.0, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x56 0x2d 0x04 0x12 0x37 0x04    \.V-..7.
    0008   0x28 0xb9 0x04                             (..
    decimal
             92   11   86   45    4   18   55    4
             40  185    4
    datetime (unknown)

    body (0)

#### RECORD 85 Bolus 2012-11-04T22:39:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-04T22:39:51)
    0000   0xb3 0xe7 0x56 0x04 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 86 LowReservoir 2012-11-04T23:53:41 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-11-04T23:53:41)
    0000   0xa9 0xf5 0x17 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 87 ResultTotals 2005-10-03T00:12:36 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x64                   ....d
    decimal
              7    0    0    5  100
    datetime (2005-10-03T00:12:36)
    0000   0xa4 0x8c 0x00 0x23 0x85                   ...#.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-22.data: 88 records`
