## START logs/ReadHistoryData-page-18.data
#### STOPPING DOUBLE NULLS @ 1008, found 14 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x98 0xdb                                  ..
##### DEBUG DECIMAL
            152  219
#### RECORD 0 Bolus 2012-11-15T19:43:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-11-15T19:43:57)
    0000   0xb9 0xeb 0x53 0x0f 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 BolusWizard 2012-11-15T19:55:50 head[2], body[13] op[0x5b]
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
    datetime (2012-11-15T19:55:50)
    0000   0xb2 0xf7 0x13 0x0f 0x0c                   .....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d                   ....}
    decimal
             31   80   13   45  106    0   23    0
              0    0    0   23  125
    HOUR BITS: [1, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 3.3, 'curve': 4},
 {'age': 21, 'amount': 0.1, 'curve': 4},
 {'age': 95, 'amount': 2.5, 'curve': 20},
 {'age': 165, 'amount': 0.7, 'curve': 20},
 {'age': 205, 'amount': 3.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x84 0x0b 0x04 0x04 0x15 0x04    \.......
    0008   0x64 0x5f 0x14 0x1c 0xa5 0x14 0x8c 0xcd    d_......
    0010   0x14                                       .
    decimal
             92   17  132   11    4    4   21    4
            100   95   20   28  165   20  140  205
             20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2012-11-15T19:55:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-15T19:55:50)
    0000   0xb2 0xf7 0x93 0x0f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 Bolus 2012-11-15T19:56:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x01                        ....
    decimal
              1   13   13    1
    datetime (2012-11-15T19:56:29)
    0000   0x9d 0xf8 0xb3 0x0f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 CalBGForPH 2012-11-15T21:02:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-11-15T21:02:01)
    0000   0x81 0xc2 0x35 0x0f 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2012-11-15T23:07:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 74}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2012-11-15T23:07:56)
    0000   0xb8 0xc7 0x37 0x0f 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 ResultTotals 2012-10-15T13:12:47 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x68                   ....h
    decimal
              7    0    0    5  104
    datetime (2012-10-15T13:12:47)
    0000   0xaf 0x8c 0x6d 0xaf 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x5d 0x4a 0x79 0x05 0x00 0x00    ..]Jy...
    0008   0x05 0x68 0x03 0x78 0x40 0x01 0xf0 0x24    .h.x@..$
    0010   0x00 0xb4 0x01 0xf0 0x24 0x01 0xf0 0x64    ....$..d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x05 0x05    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   93   74  121    5    0    0
              5  104    3  120   64    1  240   36
              0  180    1  240   36    1  240  100
              0    0    0    0    0    0    5    5
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 LowReservoir 2012-11-16T11:43:38 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-11-16T11:43:38)
    0000   0xa6 0xeb 0x0b 0x10 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 PumpSuspend 2012-11-16T14:20:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-16T14:20:19)
    0000   0x93 0xd4 0x0e 0x10 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 PumpResume 2012-11-16T14:40:21 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-16T14:40:21)
    0000   0x95 0xe8 0x0e 0x10 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 CalBGForPH 2012-11-16T16:15:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2012-11-16T16:15:00)
    0000   0x80 0xcf 0x30 0x10 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 BolusWizard 2012-11-16T16:15:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2012-11-16T16:15:35)
    0000   0xa3 0xcf 0x10 0x10 0x0c                   .....
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0xfe 0x25 0xf0    1P.-j.%.
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             49   80   13   45  106  254   37  240
              0    0    0   35  125
    HOUR BITS: [1, 1, 0]
#### RECORD 13 Bolus 2012-11-16T16:15:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-11-16T16:15:35)
    0000   0xa3 0xcf 0x50 0x10 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 LowReservoir 2012-11-16T18:31:34 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-11-16T18:31:34)
    0000   0xa2 0xdf 0x12 0x10 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2012-11-16T21:00:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2012-11-16T21:00:31)
    0000   0x9f 0xc0 0x35 0x10 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 16 CalBGForPH 2012-11-16T21:01:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2012-11-16T21:01:30)
    0000   0x9e 0xc1 0x35 0x10 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 BolusWizard 2012-11-16T21:02:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 117,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2012-11-16T21:02:05)
    0000   0x85 0xc2 0x15 0x10 0x0c                   .....
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0x00 0x25 0x00    1P.-j.%.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             49   80   13   45  106    0   37    0
              0    0    0   37  125
    HOUR BITS: [1, 1, 0]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 3.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x20 0x14                   \.. .
    decimal
             92    5  140   32   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2012-11-16T21:02:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'programmed': 3.7}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2012-11-16T21:02:05)
    0000   0x85 0xc2 0x55 0x10 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 ResultTotals 2012-10-16T13:12:48 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x98                   .....
    decimal
              7    0    0    4  152
    datetime (2012-10-16T13:12:48)
    0000   0xb0 0x8c 0x6d 0xb0 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x6e 0x60 0x75 0x03 0x00 0x00    ..n`u...
    0008   0x04 0x98 0x03 0x78 0x4c 0x01 0x20 0x18    ...xL. .
    0010   0x00 0x62 0x01 0x20 0x18 0x01 0x20 0x64    .b. .. d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  110   96  117    3    0    0
              4  152    3  120   76    1   32   24
              0   98    1   32   24    1   32  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 Rewind 2012-11-17T17:19:06 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-11-17T17:19:06)
    0000   0x86 0xd3 0x11 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 Prime 2012-11-17T17:20:22 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x0d                   .....
    decimal
              3    0    0    0   13
    datetime (2012-11-17T17:20:22)
    0000   0x96 0xd4 0x31 0x11 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 Prime 2012-11-17T17:20:32 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-11-17T17:20:32)
    0000   0xa0 0xd4 0x11 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 Battery 2012-11-17T17:21:05 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2012-11-17T17:21:05)
    0000   0x85 0xd5 0x11 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 Battery 2012-11-17T17:21:26 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2012-11-17T17:21:26)
    0000   0x9a 0xd5 0x11 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 26 Rewind 2012-11-17T17:21:53 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-11-17T17:21:53)
    0000   0xb5 0xd5 0x11 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 Prime 2012-11-17T17:23:43 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x26                   ....&
    decimal
              3    0    0    0   38
    datetime (2012-11-17T17:23:43)
    0000   0xab 0xd7 0x31 0x11 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 Prime 2012-11-17T17:24:05 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-11-17T17:24:05)
    0000   0x85 0xd8 0x11 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 29 CalBGForPH 2012-11-17T20:59:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2012-11-17T20:59:14)
    0000   0x8e 0xfb 0x34 0x11 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 BolusWizard 2012-11-17T20:59:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 189,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2012-11-17T20:59:19)
    0000   0x93 0xfb 0x14 0x11 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125
    HOUR BITS: [1, 1, 1]
#### RECORD 31 Bolus 2012-11-17T20:59:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'programmed': 1.4}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2012-11-17T20:59:19)
    0000   0x93 0xfb 0x54 0x11 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 CalBGForPH 2012-11-17T21:35:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2012-11-17T21:35:07)
    0000   0x87 0xe3 0x35 0x11 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 33 BolusWizard 2012-11-17T21:35:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 146,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 63,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.3}
```
    op hex (2)
    0000   0x5b 0x92                                  [.
    decimal
             91  146
    datetime (2012-11-17T21:35:46)
    0000   0xae 0xe3 0x15 0x11 0x0c                   .....
    body (13)
    hex
    0000   0x3f 0x50 0x0d 0x2d 0x6a 0x04 0x30 0x00    ?P.-j.0.
    0008   0x00 0x0d 0x00 0x30 0x7d                   ...0}
    decimal
             63   80   13   45  106    4   48    0
              0   13    0   48  125
    HOUR BITS: [1, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 1.4, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0x29 0x04                   \.8).
    decimal
             92    5   56   41    4
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2012-11-17T21:35:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'programmed': 4.8}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2012-11-17T21:35:46)
    0000   0xae 0xe3 0x55 0x11 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 CalBGForPH 2012-11-17T22:33:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2012-11-17T22:33:49)
    0000   0xb1 0xe1 0x36 0x11 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 37 BolusWizard 2012-11-17T22:34:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 189,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 4.8}
```
    op hex (2)
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2012-11-17T22:34:42)
    0000   0xaa 0xe2 0x16 0x11 0x0c                   .....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x0e 0x21 0x00    +P.-j.!.
    0008   0x00 0x30 0x00 0x21 0x7d                   .0.!}
    decimal
             43   80   13   45  106   14   33    0
              0   48    0   33  125
    HOUR BITS: [1, 1, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 60, 'amount': 4.8, 'curve': 4},
 {'age': 100, 'amount': 1.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0x3c 0x04 0x38 0x64 0x04    \..<.8d.
    decimal
             92    8  192   60    4   56  100    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2012-11-17T22:34:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-11-17T22:34:42)
    0000   0xaa 0xe2 0x96 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 40 ResultTotals 2012-10-17T13:12:49 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime (2012-10-17T13:12:49)
    0000   0xb1 0x8c 0x6d 0xb1 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xaf 0x92 0xbd 0x03 0x00 0x00    ........
    0008   0x05 0x08 0x03 0x82 0x46 0x01 0x86 0x1e    ....F...
    0010   0x00 0x6a 0x01 0x86 0x1e 0x01 0x4e 0x56    .j....NV
    0018   0x00 0x38 0x0e 0x00 0x00 0x00 0x03 0x02    .8......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  175  146  189    3    0    0
              5    8    3  130   70    1  134   30
              0  106    1  134   30    1   78   86
              0   56   14    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 41 Bolus 2012-11-17T22:35:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'programmed': 2.4}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x03                        ....
    decimal
              1   24   24    3
    datetime (2012-11-17T22:35:34)
    0000   0xa2 0xe3 0xb6 0x11 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 42 CalBGForPH 2012-11-18T00:44:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2012-11-18T00:44:03)
    0000   0x83 0xec 0x20 0x12 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 43 CalBGForPH 2012-11-18T04:36:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 237}
```
    op hex (2)
    0000   0x0a 0xed                                  ..
    decimal
             10  237
    datetime (2012-11-18T04:36:44)
    0000   0xac 0xe4 0x24 0x12 0x0c                   ..$..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 BolusWizard 2012-11-18T04:36:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 237,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xed                                  [.
    decimal
             91  237
    datetime (2012-11-18T04:36:49)
    0000   0xb1 0xe4 0x04 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x18 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
              0   80   13   45  106   24    0    0
              0    0    0   24  125
    HOUR BITS: [1, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 0.05, 'curve': 20},
 {'age': 26, 'amount': 0.25, 'curve': 20},
 {'age': 36, 'amount': 0.3, 'curve': 20},
 {'age': 46, 'amount': 0.25, 'curve': 20},
 {'age': 56, 'amount': 0.25, 'curve': 20},
 {'age': 66, 'amount': 0.3, 'curve': 20},
 {'age': 76, 'amount': 0.25, 'curve': 20},
 {'age': 86, 'amount': 0.25, 'curve': 20},
 {'age': 96, 'amount': 0.3, 'curve': 20},
 {'age': 106, 'amount': 1.5, 'curve': 20},
 {'age': 166, 'amount': 4.8, 'curve': 20},
 {'age': 206, 'amount': 1.4, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x02 0x10 0x14 0x0a 0x1a 0x14    \&......
    0008   0x0c 0x24 0x14 0x0a 0x2e 0x14 0x0a 0x38    .$.....8
    0010   0x14 0x0c 0x42 0x14 0x0a 0x4c 0x14 0x0a    ..B..L..
    0018   0x56 0x14 0x0c 0x60 0x14 0x3c 0x6a 0x14    V..`.<j.
    0020   0xc0 0xa6 0x14 0x38 0xce 0x14              ...8..
    decimal
             92   38    2   16   20   10   26   20
             12   36   20   10   46   20   10   56
             20   12   66   20   10   76   20   10
             86   20   12   96   20   60  106   20
            192  166   20   56  206   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2012-11-18T04:36:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'programmed': 2.7}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2012-11-18T04:36:49)
    0000   0xb1 0xe4 0x44 0x12 0x0c                   ..D..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 47 PumpSuspend 2012-11-18T09:48:06 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-18T09:48:06)
    0000   0x86 0xf0 0x09 0x12 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 PumpResume 2012-11-18T09:56:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-18T09:56:46)
    0000   0xae 0xf8 0x09 0x12 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 CalBGForPH 2012-11-18T12:00:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-11-18T12:00:45)
    0000   0xad 0xc0 0x2c 0x12 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 BolusWizard 2012-11-18T12:00:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 121,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.8,
 'carb_input': 63,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2012-11-18T12:00:56)
    0000   0xb8 0xc0 0x0c 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x3f 0x50 0x0d 0x2d 0x6a 0x00 0x30 0x00    ?P.-j.0.
    0008   0x00 0x00 0x00 0x30 0x7d                   ...0}
    decimal
             63   80   13   45  106    0   48    0
              0    0    0   48  125
    HOUR BITS: [1, 1, 0]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 190, 'amount': 2.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x6c 0xbe 0x14                   \.l..
    decimal
             92    5  108  190   20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2012-11-18T12:00:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8, 'programmed': 4.8}
```
    op hex (4)
    0000   0x01 0x30 0x30 0x00                        .00.
    decimal
              1   48   48    0
    datetime (2012-11-18T12:00:57)
    0000   0xb9 0xc0 0x4c 0x12 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 BolusWizard 2012-11-18T12:39:17 head[2], body[13] op[0x5b]
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
    datetime (2012-11-18T12:39:17)
    0000   0x91 0xe7 0x0c 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x0e 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             14   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 0.25, 'curve': 4},
 {'age': 45, 'amount': 4.55, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x0a 0x23 0x04 0xb6 0x2d 0x04    \..#..-.
    decimal
             92    8   10   35    4  182   45    4
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2012-11-18T12:39:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'programmed': 1.0}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2012-11-18T12:39:17)
    0000   0x91 0xe7 0x4c 0x12 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 56 CalBGForPH 2012-11-18T18:40:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 288}
```
    op hex (2)
    0000   0x0a 0x20                                  . 
    decimal
             10   32
    datetime (2012-11-18T18:40:59)
    0000   0xbb 0xe8 0x32 0x12 0x8c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 57 BolusWizard 2012-11-18T18:41:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 288,
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
    0000   0x5b 0x20                                  [ 
    decimal
             91   32
    datetime (2012-11-18T18:41:01)
    0000   0x81 0xe9 0x12 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
              0   81   13   45  106   36    0    0
              0    0    0   36  125
    HOUR BITS: [1, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 1.0, 'curve': 20},
 {'age': 141, 'amount': 0.25, 'curve': 20},
 {'age': 151, 'amount': 4.55, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x6f 0x14 0x0a 0x8d 0x14    \.(o....
    0008   0xb6 0x97 0x14                             ...
    decimal
             92   11   40  111   20   10  141   20
            182  151   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2012-11-18T18:41:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-11-18T18:41:01)
    0000   0x81 0xe9 0x52 0x12 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 60 CalBGForPH 2012-11-18T19:48:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 213}
```
    op hex (2)
    0000   0x0a 0xd5                                  ..
    decimal
             10  213
    datetime (2012-11-18T19:48:57)
    0000   0xb9 0xf0 0x33 0x12 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 61 CalBGForPH 2012-11-18T23:20:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2012-11-18T23:20:15)
    0000   0x8f 0xd4 0x37 0x12 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 BolusWizard 2012-11-18T23:20:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 103,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2012-11-18T23:20:36)
    0000   0xa4 0xd4 0x17 0x12 0x0c                   .....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0xff 0x21 0xf0    ,P.-j.!.
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             44   80   13   45  106  255   33  240
              0    0    0   32  125
    HOUR BITS: [1, 1, 0]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 3.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0x1e 0x14                   \....
    decimal
             92    5  144   30   20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2012-11-18T23:20:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-11-18T23:20:36)
    0000   0xa4 0xd4 0x57 0x12 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 65 ResultTotals 2012-10-18T13:12:50 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe8                   .....
    decimal
              7    0    0    5  232
    datetime (2012-10-18T13:12:50)
    0000   0xb2 0x8c 0x6d 0xb2 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb6 0x67 0x20 0x06 0x00 0x00    ...g ...
    0008   0x05 0xe8 0x03 0x7e 0x3b 0x02 0x6a 0x29    ...~;.j)
    0010   0x00 0x79 0x02 0x6a 0x29 0x01 0x6e 0x3b    .y.j).n;
    0018   0x00 0xfc 0x29 0x00 0x00 0x00 0x05 0x03    ..).....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  182  103   32    6    0    0
              5  232    3  126   59    2  106   41
              0  121    2  106   41    1  110   59
              0  252   41    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 66 PumpSuspend 2012-11-19T08:06:55 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-11-19T08:06:55)
    0000   0xb7 0xc6 0x08 0x13 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 PumpResume 2012-11-19T08:28:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-11-19T08:28:31)
    0000   0x9f 0xdc 0x08 0x13 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 68 CalBGForPH 2012-11-19T08:55:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 258}
```
    op hex (2)
    0000   0x0a 0x02                                  ..
    decimal
             10    2
    datetime (2012-11-19T08:55:12)
    0000   0x8c 0xf7 0x28 0x13 0x8c                   ..(..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 69 BolusWizard 2012-11-19T08:55:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 258,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x02                                  [.
    decimal
             91    2
    datetime (2012-11-19T08:55:21)
    0000   0x95 0xf7 0x08 0x13 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    0    0   29  125
    HOUR BITS: [1, 1, 1]
#### RECORD 70 Bolus 2012-11-19T08:55:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'programmed': 3.0}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2012-11-19T08:55:21)
    0000   0x95 0xf7 0x48 0x13 0x0c                   ..H..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 71 CalBGForPH 2012-11-19T11:18:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2012-11-19T11:18:26)
    0000   0x9a 0xd2 0x2b 0x13 0x0c                   ..+..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 CalBGForPH 2012-11-19T15:00:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2012-11-19T15:00:47)
    0000   0xaf 0xc0 0x2f 0x13 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 73 BolusWizard 2012-11-19T15:01:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 52,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2012-11-19T15:01:06)
    0000   0x86 0xc1 0x0f 0x13 0x0c                   .....
    body (13)
    hex
    0000   0x34 0x50 0x0d 0x2d 0x6a 0x00 0x28 0x00    4P.-j.(.
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
             52   80   13   45  106    0   40    0
              0    0    0   40  125
    HOUR BITS: [1, 1, 0]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 3.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x6f 0x14                   \.xo.
    decimal
             92    5  120  111   20
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2012-11-19T15:01:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'programmed': 4.0}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2012-11-19T15:01:06)
    0000   0x86 0xc1 0x4f 0x13 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 CalBGForPH 2012-11-19T18:25:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2012-11-19T18:25:58)
    0000   0xba 0xd9 0x32 0x13 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 77 BolusWizard 2012-11-19T18:27:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 93,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0x5d                                  []
    decimal
             91   93
    datetime (2012-11-19T18:27:18)
    0000   0x92 0xdb 0x12 0x13 0x0c                   .....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0xfd 0x05 0xf0    .P.-j...
    0008   0x00 0x04 0x00 0x02 0x7d                   ....}
    decimal
              7   80   13   45  106  253    5  240
              0    4    0    2  125
    HOUR BITS: [1, 1, 0]
#### RECORD 78 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 213, 'amount': 4.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0xd5 0x04                   \....
    decimal
             92    5  160  213    4
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2012-11-19T18:27:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'programmed': 0.2}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2012-11-19T18:27:18)
    0000   0x92 0xdb 0x52 0x13 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 80 CalBGForPH 2012-11-19T18:28:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2012-11-19T18:28:17)
    0000   0x91 0xdc 0x32 0x13 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-18.data: 81 records`
