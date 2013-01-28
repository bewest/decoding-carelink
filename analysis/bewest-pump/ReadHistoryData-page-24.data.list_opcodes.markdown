## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x76 0x5d                                  v]
##### DEBUG DECIMAL
            118   93
#### RECORD 0 CalForBG 2012-10-26T17:30:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2012-10-26T17:30:40)
    0000   0xa8 0x9e 0x31 0x1a 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalForBG 2012-10-26T22:08:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2012-10-26T22:08:57)
    0000   0xb9 0x88 0x36 0x1a 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 2 BolusWizard 2012-10-26T22:09:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 111,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2012-10-26T22:09:58)
    0000   0xba 0x89 0x16 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    <P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [1, 0, 0]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 99, 'amount': 1.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0x63 0x14                   \.Dc.
    decimal
             92    5   68   99   20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2012-10-26T22:09:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'programmed': 4.6}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2012-10-26T22:09:58)
    0000   0xba 0x89 0x56 0x1a 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 CalForBG 2012-10-26T22:43:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2012-10-26T22:43:59)
    0000   0xbb 0xab 0x36 0x1a 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 CalForBG 2012-10-26T22:53:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-10-26T22:53:00)
    0000   0x80 0xb5 0x36 0x1a 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 7 ResultTotals 2012-08-26T13:12:58 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xbc                   .....
    decimal
              7    0    0    4  188
    datetime (2012-08-26T13:12:58)
    0000   0xba 0x0c 0x6d 0xba 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0x8b 0x46 0x47 0x09 0x00 0x00    ...FG...
    0008   0x04 0xbc 0x02 0xb4 0x39 0x02 0x08 0x2b    ....9..+
    0010   0x00 0x56 0x02 0x08 0x2b 0x00 0xfc 0x30    .V..+..0
    0018   0x01 0x0c 0x34 0x00 0x00 0x00 0x04 0x02    ..4.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  139   70   71    9    0    0
              4  188    2  180   57    2    8   43
              0   86    2    8   43    0  252   48
              1   12   52    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 8 CalForBG 2012-10-27T00:20:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2012-10-27T00:20:03)
    0000   0x83 0x94 0x20 0x1b 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 9 CalForBG 2012-10-27T00:20:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-10-27T00:20:41)
    0000   0xa9 0x94 0x20 0x1b 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 CalForBG 2012-10-27T06:12:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 229}
```
    op hex (2)
    0000   0x0a 0xe5                                  ..
    decimal
             10  229
    datetime (2012-10-27T06:12:02)
    0000   0x82 0x8c 0x26 0x1b 0x0c                   ..&..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 11 BolusWizard 2012-10-27T06:12:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 229,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xe5                                  [.
    decimal
             91  229
    datetime (2012-10-27T06:12:05)
    0000   0x85 0x8c 0x06 0x1b 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x17 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
              0   80   13   45  106   23    0    0
              0    0    0   23  125
    HOUR BITS: [1, 0, 0]
#### RECORD 12 Bolus 2012-10-27T06:12:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'programmed': 2.3}
```
    op hex (4)
    0000   0x01 0x17 0x17 0x00                        ....
    decimal
              1   23   23    0
    datetime (2012-10-27T06:12:05)
    0000   0x85 0x8c 0x46 0x1b 0x0c                   ..F..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 13 PumpSuspend 2012-10-27T09:35:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-27T09:35:38)
    0000   0xa6 0xa3 0x09 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 14 PumpResume 2012-10-27T10:11:49 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-27T10:11:49)
    0000   0xb1 0x8b 0x0a 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 15 CalForBG 2012-10-27T12:11:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2012-10-27T12:11:09)
    0000   0x89 0x8b 0x2c 0x1b 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 BolusWizard 2012-10-27T12:11:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 112,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2012-10-27T12:11:38)
    0000   0xa6 0x8b 0x0c 0x1b 0x0c                   .....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 0]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 2.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x5c 0x6f 0x14                   \.\o.
    decimal
             92    5   92  111   20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2012-10-27T12:11:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'programmed': 1.7}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2012-10-27T12:11:38)
    0000   0xa6 0x8b 0x4c 0x1b 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 19 CalForBG 2012-10-27T13:26:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2012-10-27T13:26:11)
    0000   0x8b 0x9a 0x2d 0x1b 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 BolusWizard 2012-10-27T13:26:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 199,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.5,
 'carb_input': 67,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.2}
```
    op hex (2)
    0000   0x5b 0xc7                                  [.
    decimal
             91  199
    datetime (2012-10-27T13:26:51)
    0000   0xb3 0x9a 0x0d 0x1b 0x0c                   .....
    body (13)
    hex
    0000   0x43 0x50 0x0d 0x2d 0x6a 0x10 0x33 0x00    CP.-j.3.
    0008   0x00 0x0c 0x00 0x37 0x7d                   ...7}
    decimal
             67   80   13   45  106   16   51    0
              0   12    0   55  125
    HOUR BITS: [1, 0, 0]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 82, 'amount': 1.7, 'curve': 4},
 {'age': 186, 'amount': 2.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x52 0x04 0x5c 0xba 0x14    \.DR.\..
    decimal
             92    8   68   82    4   92  186   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2012-10-27T13:26:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5, 'programmed': 5.5}
```
    op hex (4)
    0000   0x01 0x37 0x37 0x00                        .77.
    decimal
              1   55   55    0
    datetime (2012-10-27T13:26:51)
    0000   0xb3 0x9a 0x4d 0x1b 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 PumpSuspend 2012-10-27T18:05:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-27T18:05:18)
    0000   0x92 0x85 0x12 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 PumpResume 2012-10-27T18:10:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-27T18:10:50)
    0000   0xb2 0x8a 0x12 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 25 CalForBG 2012-10-27T19:00:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2012-10-27T19:00:14)
    0000   0x8e 0x80 0x33 0x1b 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 26 BolusWizard 2012-10-27T19:00:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 116,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x74                                  [t
    decimal
             91  116
    datetime (2012-10-27T19:00:29)
    0000   0x9d 0x80 0x13 0x1b 0x0c                   .....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    <P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             60   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [1, 0, 0]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 80, 'amount': 5.5, 'curve': 20},
 {'age': 160, 'amount': 1.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xdc 0x50 0x14 0x44 0xa0 0x14    \..P.D..
    decimal
             92    8  220   80   20   68  160   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2012-10-27T19:00:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'programmed': 4.6}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2012-10-27T19:00:29)
    0000   0x9d 0x80 0x53 0x1b 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 CalForBG 2012-10-27T19:53:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2012-10-27T19:53:10)
    0000   0x8a 0xb5 0x33 0x1b 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 30 LowReservoir 2012-10-27T21:25:15 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-10-27T21:25:15)
    0000   0x8f 0x99 0x15 0x1b 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 ResultTotals 2012-08-27T13:12:59 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x9a                   .....
    decimal
              7    0    0    5  154
    datetime (2012-08-27T13:12:59)
    0000   0xbb 0x0c 0x6d 0xbb 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8c 0x64 0xe5 0x07 0x00 0x00    ...d....
    0008   0x05 0x9a 0x03 0x66 0x3d 0x02 0x34 0x27    ...f=.4'
    0010   0x00 0x96 0x02 0x34 0x27 0x01 0xc8 0x51    ...4'..Q
    0018   0x00 0x6c 0x13 0x00 0x00 0x00 0x04 0x02    .l......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  140  100  229    7    0    0
              5  154    3  102   61    2   52   39
              0  150    2   52   39    1  200   81
              0  108   19    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 32 CalForBG 2012-10-28T01:32:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2012-10-28T01:32:35)
    0000   0xa3 0xa0 0x21 0x1c 0x0c                   ..!..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 33 PumpSuspend 2012-10-28T08:46:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-28T08:46:44)
    0000   0xac 0xae 0x08 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 34 PumpResume 2012-10-28T09:12:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-28T09:12:40)
    0000   0xa8 0x8c 0x09 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 CalForBG 2012-10-28T09:25:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2012-10-28T09:25:08)
    0000   0x88 0x99 0x29 0x1c 0x0c                   ..)..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 BolusWizard 2012-10-28T09:25:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 215,
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
    0000   0x5b 0xd7                                  [.
    decimal
             91  215
    datetime (2012-10-28T09:25:10)
    0000   0x8a 0x99 0x09 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125
    HOUR BITS: [1, 0, 0]
#### RECORD 37 LowReservoir 2012-10-28T09:25:13 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-10-28T09:25:13)
    0000   0x8d 0x99 0x09 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 38 Bolus 2012-10-28T09:25:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-10-28T09:25:10)
    0000   0x8a 0x99 0x49 0x1c 0x0c                   ..I..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 CalForBG 2012-10-28T12:29:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 147}
```
    op hex (2)
    0000   0x0a 0x93                                  ..
    decimal
             10  147
    datetime (2012-10-28T12:29:14)
    0000   0x8e 0x9d 0x2c 0x1c 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 Rewind 2012-10-28T16:11:34 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-10-28T16:11:34)
    0000   0xa2 0x8b 0x10 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 41 Prime 2012-10-28T16:13:57 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x25                   ....%
    decimal
              3    0    0    0   37
    datetime (2012-10-28T16:13:57)
    0000   0xb9 0x8d 0x30 0x1c 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 Prime 2012-10-28T16:14:21 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-10-28T16:14:21)
    0000   0x95 0x8e 0x10 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 43 CalForBG 2012-10-28T16:16:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2012-10-28T16:16:46)
    0000   0xae 0x90 0x30 0x1c 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 44 BolusWizard 2012-10-28T16:16:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 100,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2012-10-28T16:16:56)
    0000   0xb8 0x90 0x10 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0xfe 0x0f 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             20   80   13   45  106  254   15  240
              0    0    0   13  125
    HOUR BITS: [1, 0, 0]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 156, 'amount': 2.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x9c 0x14                   \.P..
    decimal
             92    5   80  156   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2012-10-28T16:16:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-10-28T16:16:56)
    0000   0xb8 0x90 0x50 0x1c 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 47 PumpSuspend 2012-10-28T17:10:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-28T17:10:57)
    0000   0xb9 0x8a 0x11 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 48 PumpResume 2012-10-28T17:21:19 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-28T17:21:19)
    0000   0x93 0x95 0x11 0x1c 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 49 CalForBG 2012-10-28T17:33:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2012-10-28T17:33:11)
    0000   0x8b 0xa1 0x31 0x1c 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 50 CalForBG 2012-10-28T19:23:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-10-28T19:23:58)
    0000   0xba 0x97 0x33 0x1c 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 BolusWizard 2012-10-28T19:24:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2012-10-28T19:24:07)
    0000   0x87 0x98 0x13 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    2    0   11  125
    HOUR BITS: [1, 0, 0]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 190, 'amount': 1.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x34 0xbe 0x04                   \.4..
    decimal
             92    5   52  190    4
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2012-10-28T19:24:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2012-10-28T19:24:07)
    0000   0x87 0x98 0x53 0x1c 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 54 BolusWizard 2012-10-28T19:28:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-28T19:28:44)
    0000   0xac 0x9c 0x13 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x00 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             65   80   13   45  106    0   50    0
              0    0    0   50  125
    HOUR BITS: [1, 0, 0]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 1.1, 'curve': 4},
 {'age': 194, 'amount': 1.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x04 0x04 0x34 0xc2 0x04    \.,..4..
    decimal
             92    8   44    4    4   52  194    4
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2012-10-28T19:28:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'programmed': 5.0}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2012-10-28T19:28:44)
    0000   0xac 0x9c 0x53 0x1c 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 57 CalForBG 2012-10-28T19:50:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2012-10-28T19:50:04)
    0000   0x84 0xb2 0x33 0x1c 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 58 BolusWizard 2012-10-28T19:50:44 head[2], body[13] op[0x5b]
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
    datetime (2012-10-28T19:50:44)
    0000   0xac 0xb2 0x13 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    0    0   18  125
    HOUR BITS: [1, 0, 1]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 6.1, 'curve': 4},
 {'age': 216, 'amount': 1.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xf4 0x1a 0x04 0x34 0xd8 0x04    \....4..
    decimal
             92    8  244   26    4   52  216    4
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2012-10-28T19:50:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-10-28T19:50:44)
    0000   0xac 0xb2 0x53 0x1c 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 61 CalForBG 2012-10-28T20:04:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2012-10-28T20:04:03)
    0000   0x83 0x84 0x34 0x1c 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 CalForBG 2012-10-28T22:01:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 62}
```
    op hex (2)
    0000   0x0a 0x3e                                  .>
    decimal
             10   62
    datetime (2012-10-28T22:01:42)
    0000   0xaa 0x81 0x36 0x1c 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 ResultTotals (2012, 8, 28, 13, 12, 60) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x2a                   ....*
    decimal
              7    0    0    5   42
    datetime ((2012, 8, 28, 13, 12, 60))
    0000   0xbc 0x0c 0x6d 0xbc 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x91 0x3e 0xd7 0x09 0x00 0x00    ...>....
    0008   0x05 0x2a 0x03 0x6a 0x42 0x01 0xc0 0x22    .*.jB.."
    0010   0x00 0x6d 0x01 0xc0 0x22 0x01 0x44 0x48    .m..".DH
    0018   0x00 0x7c 0x1c 0x00 0x00 0x00 0x05 0x03    .|......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  145   62  215    9    0    0
              5   42    3  106   66    1  192   34
              0  109    1  192   34    1   68   72
              0  124   28    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 64 CalForBG 2012-10-29T02:55:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2012-10-29T02:55:13)
    0000   0x8d 0xb7 0x22 0x1d 0x0c                   .."..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 65 BolusWizard 2012-10-29T02:55:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 175,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xaf                                  [.
    decimal
             91  175
    datetime (2012-10-29T02:55:15)
    0000   0x8f 0xb7 0x02 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    0    0   11  125
    HOUR BITS: [1, 0, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 175, 'amount': 1.8, 'curve': 20},
 {'age': 195, 'amount': 6.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0xaf 0x14 0xf4 0xc3 0x14    \.H.....
    decimal
             92    8   72  175   20  244  195   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2012-10-29T02:55:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2012-10-29T02:55:15)
    0000   0x8f 0xb7 0x42 0x1d 0x0c                   ..B..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 68 PumpSuspend 2012-10-29T11:09:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-29T11:09:55)
    0000   0xb7 0x89 0x0b 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 PumpResume 2012-10-29T11:24:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-29T11:24:03)
    0000   0x83 0x98 0x0b 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 70 CalForBG 2012-10-29T11:57:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 205}
```
    op hex (2)
    0000   0x0a 0xcd                                  ..
    decimal
             10  205
    datetime (2012-10-29T11:57:33)
    0000   0xa1 0xb9 0x2b 0x1d 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 71 BolusWizard 2012-10-29T11:57:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 205,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xcd                                  [.
    decimal
             91  205
    datetime (2012-10-29T11:57:37)
    0000   0xa5 0xb9 0x0b 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x11 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
              0   80   13   45  106   17    0    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 1]
#### RECORD 72 Bolus 2012-10-29T11:57:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-10-29T11:57:37)
    0000   0xa5 0xb9 0x4b 0x1d 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 73 CalForBG 2012-10-29T12:41:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2012-10-29T12:41:46)
    0000   0xae 0xa9 0x2c 0x1d 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 74 BolusWizard 2012-10-29T12:42:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 169,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.7}
```
    op hex (2)
    0000   0x5b 0xa9                                  [.
    decimal
             91  169
    datetime (2012-10-29T12:42:10)
    0000   0x8a 0xaa 0x0c 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x09 0x2a 0x00    7P.-j.*.
    0008   0x00 0x11 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    9   42    0
              0   17    0   42  125
    HOUR BITS: [1, 0, 1]
#### RECORD 75 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 1.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x4c 0x30 0x04                   \.L0.
    decimal
             92    5   76   48    4
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2012-10-29T12:42:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'programmed': 4.2}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2012-10-29T12:42:10)
    0000   0x8a 0xaa 0x4c 0x1d 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 77 CalForBG 2012-10-29T13:43:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2012-10-29T13:43:03)
    0000   0x83 0xab 0x2d 0x1d 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 78 CalForBG 2012-10-29T14:44:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2012-10-29T14:44:27)
    0000   0x9b 0xac 0x2e 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 BolusWizard 2012-10-29T15:23:40 head[2], body[13] op[0x5b]
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
    datetime (2012-10-29T15:23:40)
    0000   0xa8 0x97 0x0f 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x12 0x50 0x0d 0x2d 0x6a 0x00 0x0d 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
             18   80   13   45  106    0   13    0
              0    0    0   13  125
    HOUR BITS: [1, 0, 0]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 159, 'amount': 1.5, 'curve': 4},
 {'age': 169, 'amount': 2.7, 'curve': 4},
 {'age': 209, 'amount': 1.9, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0x9f 0x04 0x6c 0xa9 0x04    \.<..l..
    0008   0x4c 0xd1 0x04                             L..
    decimal
             92   11   60  159    4  108  169    4
             76  209    4
    datetime (unknown)

    body (0)

#### RECORD 81 Bolus 2012-10-29T15:23:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-10-29T15:23:40)
    0000   0xa8 0x97 0x4f 0x1d 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 82 CalForBG 2012-10-29T16:47:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2012-10-29T16:47:39)
    0000   0xa7 0xaf 0x30 0x1d 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 83 CalForBG 2012-10-29T17:05:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 138}
```
    op hex (2)
    0000   0x0a 0x8a                                  ..
    decimal
             10  138
    datetime (2012-10-29T17:05:04)
    0000   0x84 0x85 0x31 0x1d 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 84 BolusWizard 2012-10-29T17:14:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 5,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-10-29T17:14:09)
    0000   0x89 0x8e 0x11 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x05 0x50 0x0d 0x2d 0x6a 0x00 0x03 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x03 0x7d                   ....}
    decimal
              5   80   13   45  106    0    3    0
              0    0    0    3  125
    HOUR BITS: [1, 0, 0]
#### RECORD 85 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 110, 'amount': 0.8, 'curve': 4},
 {'age': 120, 'amount': 0.5, 'curve': 4},
 {'age': 14, 'amount': 1.5, 'curve': 20},
 {'age': 24, 'amount': 2.7, 'curve': 20},
 {'age': 64, 'amount': 1.9, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x6e 0x04 0x14 0x78 0x04    \. n..x.
    0008   0x3c 0x0e 0x14 0x6c 0x18 0x14 0x4c 0x40    <..l..L@
    0010   0x14                                       .
    decimal
             92   17   32  110    4   20  120    4
             60   14   20  108   24   20   76   64
             20
    datetime (unknown)

    body (0)

#### RECORD 86 Bolus 2012-10-29T17:14:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-10-29T17:14:09)
    0000   0x89 0x8e 0x51 0x1d 0x0c                   ..Q..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 87 CalForBG 2012-10-29T18:58:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2012-10-29T18:58:35)
    0000   0xa3 0xba 0x32 0x1d 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 88 CalForBG 2012-10-29T18:58:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 173}
```
    op hex (2)
    0000   0x0a 0xad                                  ..
    decimal
             10  173
    datetime (2012-10-29T18:58:44)
    0000   0xac 0xba 0x32 0x1d 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 89 BolusWizard 2012-10-29T18:59:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 173,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2012-10-29T18:59:38)
    0000   0xa6 0xbb 0x12 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x0a 0x26 0x00    2P.-j.&.
    0008   0x00 0x03 0x00 0x2d 0x7d                   ...-}
    decimal
             50   80   13   45  106   10   38    0
              0    3    0   45  125
    HOUR BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-24.data: 90 records`
