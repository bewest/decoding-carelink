## START logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x38 0xa2                                  8.
##### DEBUG DECIMAL
             56  162
#### RECORD 0 Bolus 2012-10-23T20:03:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'programmed': 0.9}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2012-10-23T20:03:54)
    0000   0xb6 0x83 0x54 0x17 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 1 LowReservoir 2012-10-23T20:50:31 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-10-23T20:50:31)
    0000   0x9f 0xb2 0x14 0x17 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalForBG 2012-10-23T20:53:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 208}
```
    op hex (2)
    0000   0x0a 0xd0                                  ..
    decimal
             10  208
    datetime (2012-10-23T20:53:19)
    0000   0x93 0xb5 0x34 0x17 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 3 BolusWizard 2012-10-23T20:53:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 208,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.3}
```
    op hex (2)
    0000   0x5b 0xd0                                  [.
    decimal
             91  208
    datetime (2012-10-23T20:53:34)
    0000   0xa2 0xb5 0x14 0x17 0x0c                   .....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x12 0x20 0x00    *P.-j. .
    0008   0x00 0x17 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106   18   32    0
              0   23    0   32  125
    HOUR BITS: [1, 0, 1]
#### RECORD 4 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 0.75, 'curve': 4},
 {'age': 59, 'amount': 1.95, 'curve': 4},
 {'age': 33, 'amount': 1.8, 'curve': 20},
 {'age': 223, 'amount': 2.85, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1e 0x31 0x04 0x4e 0x3b 0x04    \..1.N;.
    0008   0x48 0x21 0x14 0x72 0xdf 0x14              H!.r..
    decimal
             92   14   30   49    4   78   59    4
             72   33   20  114  223   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-10-23T20:53:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-10-23T20:53:34)
    0000   0xa2 0xb5 0x54 0x17 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 CalForBG 2012-10-23T21:06:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2012-10-23T21:06:22)
    0000   0x96 0x86 0x35 0x17 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 CalForBG 2012-10-23T23:01:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2012-10-23T23:01:11)
    0000   0x8b 0x81 0x37 0x17 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 ResultTotals 2012-08-23T13:12:55 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x70                   ....p
    decimal
              7    0    0    5  112
    datetime (2012-08-23T13:12:55)
    0000   0xb7 0x0c 0x6d 0xb7 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x95 0x4b 0xda 0x09 0x00 0x00    ...K....
    0008   0x05 0x70 0x03 0x6c 0x3f 0x02 0x04 0x25    .p.l?..%
    0010   0x00 0x73 0x02 0x04 0x25 0x01 0x5c 0x43    .s..%.\C
    0018   0x00 0xa8 0x21 0x00 0x00 0x00 0x06 0x03    ..!.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  149   75  218    9    0    0
              5  112    3  108   63    2    4   37
              0  115    2    4   37    1   92   67
              0  168   33    0    0    0    6    3
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 9 CalForBG 2012-10-24T00:51:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2012-10-24T00:51:29)
    0000   0x9d 0xb3 0x20 0x18 0x0c                   .. ..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 10 BolusWizard 2012-10-24T00:51:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 165,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0xa5                                  [.
    decimal
             91  165
    datetime (2012-10-24T00:51:32)
    0000   0xa0 0xb3 0x00 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    2    0    6  125
    HOUR BITS: [1, 0, 1]
#### RECORD 11 BolusGiven unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 237, 'amount': 2.6, 'curve': 4},
 {'age': 247, 'amount': 0.6, 'curve': 4},
 {'age': 31, 'amount': 0.75, 'curve': 20},
 {'age': 41, 'amount': 1.95, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x68 0xed 0x04 0x18 0xf7 0x04    \.h.....
    0008   0x1e 0x1f 0x14 0x4e 0x29 0x14              ...N).
    decimal
             92   14  104  237    4   24  247    4
             30   31   20   78   41   20
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2012-10-24T00:51:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'programmed': 0.6}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-10-24T00:51:32)
    0000   0xa0 0xb3 0x40 0x18 0x0c                   ..@..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 13 LowReservoir 2012-10-24T04:00:00 head[2], body[0] op[0x34]

    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-10-24T04:00:00)
    0000   0x80 0x80 0x04 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 14 PumpSuspend 2012-10-24T12:53:45 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-24T12:53:45)
    0000   0xad 0xb5 0x0c 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 15 PumpResume 2012-10-24T13:15:38 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-24T13:15:38)
    0000   0xa6 0x8f 0x0d 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 Rewind 2012-10-24T13:50:04 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-10-24T13:50:04)
    0000   0x84 0xb2 0x0d 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 17 Prime 2012-10-24T13:53:46 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x21                   ....!
    decimal
              3    0    0    0   33
    datetime (2012-10-24T13:53:46)
    0000   0xae 0xb5 0x2d 0x18 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 Prime 2012-10-24T13:54:08 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-10-24T13:54:08)
    0000   0x88 0xb6 0x0d 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 19 CalForBG 2012-10-24T13:55:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2012-10-24T13:55:33)
    0000   0xa1 0xb7 0x2d 0x18 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 20 CalForBG 2012-10-24T14:08:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2012-10-24T14:08:20)
    0000   0x94 0x88 0x2e 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 BolusWizard 2012-10-24T14:08:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2012-10-24T14:08:34)
    0000   0xa2 0x88 0x0e 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0xff 0x20 0xf0    *P.-j. .
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             42   80   13   45  106  255   32  240
              0    0    0   31  125
    HOUR BITS: [1, 0, 0]
#### RECORD 22 Bolus 2012-10-24T14:08:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-10-24T14:08:34)
    0000   0xa2 0x88 0x4e 0x18 0x0c                   ..N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 CalForBG 2012-10-24T14:57:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 149}
```
    op hex (2)
    0000   0x0a 0x95                                  ..
    decimal
             10  149
    datetime (2012-10-24T14:57:04)
    0000   0x84 0xb9 0x2e 0x18 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 CalForBG 2012-10-24T15:31:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2012-10-24T15:31:16)
    0000   0x90 0x9f 0x2f 0x18 0x0c                   ../..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 25 CalForBG 2012-10-24T16:04:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2012-10-24T16:04:00)
    0000   0x80 0x84 0x30 0x18 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 26 CalForBG 2012-10-24T16:37:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2012-10-24T16:37:55)
    0000   0xb7 0xa5 0x30 0x18 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 27 BolusWizard 2012-10-24T16:38:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 174,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.9}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2012-10-24T16:38:03)
    0000   0x83 0xa6 0x10 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x09 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    9    0    1  125
    HOUR BITS: [1, 0, 1]
#### RECORD 28 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 154, 'amount': 3.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x7c 0x9a 0x04                   \.|..
    decimal
             92    5  124  154    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2012-10-24T16:38:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'programmed': 0.4}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2012-10-24T16:38:03)
    0000   0x83 0xa6 0x50 0x18 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 30 CalForBG 2012-10-24T17:19:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2012-10-24T17:19:09)
    0000   0x89 0x93 0x31 0x18 0x0c                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 CalForBG 2012-10-24T18:13:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 149}
```
    op hex (2)
    0000   0x0a 0x95                                  ..
    decimal
             10  149
    datetime (2012-10-24T18:13:56)
    0000   0xb8 0x8d 0x32 0x18 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 BolusWizard 2012-10-24T18:14:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 149,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0x95                                  [.
    decimal
             91  149
    datetime (2012-10-24T18:14:00)
    0000   0x80 0x8e 0x12 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x05 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x02 0x7d                   ....}
    decimal
              0   80   13   45  106    5    0    0
              0    3    0    2  125
    HOUR BITS: [1, 0, 0]
#### RECORD 33 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 100, 'amount': 0.4, 'curve': 4},
 {'age': 250, 'amount': 3.1, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x64 0x04 0x7c 0xfa 0x04    \..d.|..
    decimal
             92    8   16  100    4  124  250    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2012-10-24T18:14:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'programmed': 0.2}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2012-10-24T18:14:00)
    0000   0x80 0x8e 0x52 0x18 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 CalForBG 2012-10-24T18:18:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2012-10-24T18:18:05)
    0000   0x85 0x92 0x32 0x18 0x0c                   ..2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 BolusWizard 2012-10-24T18:18:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 156,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 33,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2012-10-24T18:18:25)
    0000   0x99 0x92 0x12 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x21 0x50 0x0d 0x2d 0x6a 0x06 0x19 0x00    !P.-j...
    0008   0x00 0x05 0x00 0x1a 0x7d                   ....}
    decimal
             33   80   13   45  106    6   25    0
              0    5    0   26  125
    HOUR BITS: [1, 0, 0]
#### RECORD 37 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 0.2, 'curve': 4},
 {'age': 104, 'amount': 0.4, 'curve': 4},
 {'age': 254, 'amount': 3.1, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x08 0x04 0x04 0x10 0x68 0x04    \.....h.
    0008   0x7c 0xfe 0x04                             |..
    decimal
             92   11    8    4    4   16  104    4
            124  254    4
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2012-10-24T18:18:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-10-24T18:18:25)
    0000   0x99 0x92 0x52 0x18 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 CalForBG 2012-10-24T21:45:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2012-10-24T21:45:48)
    0000   0xb0 0xad 0x35 0x18 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 40 CalForBG 2012-10-24T23:41:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2012-10-24T23:41:41)
    0000   0xa9 0xa9 0x37 0x18 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 41 BolusWizard 2012-10-24T23:42:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 91,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2012-10-24T23:42:05)
    0000   0x85 0xaa 0x17 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0xfc 0x16 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             29   80   13   45  106  252   22  240
              0    0    0   18  125
    HOUR BITS: [1, 0, 1]
#### RECORD 42 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 2.8, 'curve': 20},
 {'age': 172, 'amount': 0.4, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x70 0x48 0x14 0x10 0xac 0x14    \.pH....
    decimal
             92    8  112   72   20   16  172   20
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2012-10-24T23:42:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-10-24T23:42:06)
    0000   0x86 0xaa 0x57 0x18 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 44 CalForBG 2012-10-24T23:44:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2012-10-24T23:44:45)
    0000   0xad 0xac 0x37 0x18 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 45 BolusWizard 2012-10-24T23:45:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 97,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.8}
```
    op hex (2)
    0000   0x5b 0x61                                  [a
    decimal
             91   97
    datetime (2012-10-24T23:45:00)
    0000   0x80 0xad 0x17 0x18 0x0c                   .....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0xfe 0x0b 0xf0    .P.-j...
    0008   0x00 0x12 0x00 0x09 0x7d                   ....}
    decimal
             15   80   13   45  106  254   11  240
              0   18    0    9  125
    HOUR BITS: [1, 0, 1]
#### RECORD 46 BolusGiven unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 1.8, 'curve': 4},
 {'age': 75, 'amount': 2.8, 'curve': 20},
 {'age': 175, 'amount': 0.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x0b 0x04 0x70 0x4b 0x14    \.H..pK.
    0008   0x10 0xaf 0x14                             ...
    decimal
             92   11   72   11    4  112   75   20
             16  175   20
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2012-10-24T23:45:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'programmed': 0.9}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2012-10-24T23:45:00)
    0000   0x80 0xad 0x57 0x18 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 48 ResultTotals 2012-08-24T13:12:56 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf2                   .....
    decimal
              7    0    0    4  242
    datetime (2012-08-24T13:12:56)
    0000   0xb8 0x0c 0x6d 0xb8 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x8c 0x56 0xc4 0x0d 0x00 0x00    ...V....
    0008   0x04 0xf2 0x03 0x72 0x46 0x01 0x80 0x1e    ...rF...
    0010   0x00 0x77 0x01 0x80 0x1e 0x01 0x4c 0x56    .w....LV
    0018   0x00 0x34 0x0e 0x00 0x00 0x00 0x07 0x03    .4......
    0020   0x03 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  140   86  196   13    0    0
              4  242    3  114   70    1  128   30
              0  119    1  128   30    1   76   86
              0   52   14    0    0    0    7    3
              3    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 49 PumpSuspend 2012-10-25T11:04:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-25T11:04:15)
    0000   0x8f 0x84 0x0b 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 PumpResume 2012-10-25T11:06:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-25T11:06:02)
    0000   0x82 0x86 0x0b 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 PumpSuspend 2012-10-25T11:06:10 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-25T11:06:10)
    0000   0x8a 0x86 0x0b 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 52 PumpResume 2012-10-25T11:20:20 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-25T11:20:20)
    0000   0x94 0x94 0x0b 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 CalForBG 2012-10-25T11:47:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 10}
```
    op hex (2)
    0000   0x0a 0x0a                                  ..
    decimal
             10   10
    datetime (2012-10-25T11:47:00)
    0000   0x80 0xaf 0x2b 0x19 0x8c                   ..+..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 54 BolusWizard 2012-10-25T11:47:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 266,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x0a                                  [.
    decimal
             91   10
    datetime (2012-10-25T11:47:07)
    0000   0x87 0xaf 0x0b 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    0    0   31  125
    HOUR BITS: [1, 0, 1]
#### RECORD 55 Bolus 2012-10-25T11:47:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-10-25T11:47:07)
    0000   0x87 0xaf 0x4b 0x19 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 56 TempBasal 2012-10-25T11:53:35 head[2], body[1] op[0x33]

    op hex (2)
    0000   0x33 0x2e                                  3.
    decimal
             51   46
    datetime (2012-10-25T11:53:35)
    0000   0xa3 0xb5 0x0b 0x19 0x0c                   .....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 0, 1]
#### RECORD 57 EndTempBasal 2012-10-25T11:53:35 head[2], body[0] op[0x16]

    op hex (2)
    0000   0x16 0x01                                  ..
    decimal
             22    1
    datetime (2012-10-25T11:53:35)
    0000   0xa3 0xb5 0x0b 0x19 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 58 CalForBG 2012-10-25T13:09:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2012-10-25T13:09:44)
    0000   0xac 0x89 0x2d 0x19 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 CalForBG 2012-10-25T13:17:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2012-10-25T13:17:47)
    0000   0xaf 0x91 0x2d 0x19 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 60 BolusWizard 2012-10-25T13:18:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 140,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 9,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.2}
```
    op hex (2)
    0000   0x5b 0x8c                                  [.
    decimal
             91  140
    datetime (2012-10-25T13:18:32)
    0000   0xa0 0x92 0x0d 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x09 0x50 0x0d 0x2d 0x6a 0x03 0x06 0x00    .P.-j...
    0008   0x00 0x16 0x00 0x06 0x7d                   ....}
    decimal
              9   80   13   45  106    3    6    0
              0   22    0    6  125
    HOUR BITS: [1, 0, 0]
#### RECORD 61 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 3.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x5e 0x04                   \..^.
    decimal
             92    5  140   94    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2012-10-25T13:18:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'programmed': 0.6}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-10-25T13:18:32)
    0000   0xa0 0x92 0x4d 0x19 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 CalForBG 2012-10-25T16:21:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 240}
```
    op hex (2)
    0000   0x0a 0xf0                                  ..
    decimal
             10  240
    datetime (2012-10-25T16:21:44)
    0000   0xac 0x95 0x30 0x19 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 64 BolusWizard 2012-10-25T16:21:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 240,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0xf0                                  [.
    decimal
             91  240
    datetime (2012-10-25T16:21:50)
    0000   0xb2 0x95 0x10 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x19 0x00 0x00    .P.-j...
    0008   0x00 0x01 0x00 0x18 0x7d                   ....}
    decimal
              0   80   13   45  106   25    0    0
              0    1    0   24  125
    HOUR BITS: [1, 0, 0]
#### RECORD 65 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 187, 'amount': 0.6, 'curve': 4},
 {'age': 21, 'amount': 3.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0xbb 0x04 0x8c 0x15 0x14    \.......
    decimal
             92    8   24  187    4  140   21   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2012-10-25T16:21:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'programmed': 2.5}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2012-10-25T16:21:50)
    0000   0xb2 0x95 0x50 0x19 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 67 CalForBG 2012-10-25T20:37:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2012-10-25T20:37:49)
    0000   0xb1 0xa5 0x34 0x19 0x0c                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 68 BolusWizard 2012-10-25T20:38:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 107,
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
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2012-10-25T20:38:24)
    0000   0x98 0xa6 0x14 0x19 0x0c                   .....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x00 0x20 0x00    *P.-j. .
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106    0   32    0
              0    0    0   32  125
    HOUR BITS: [1, 0, 1]
#### RECORD 69 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 2.5, 'curve': 20},
 {'age': 188, 'amount': 0.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0x08 0x14 0x18 0xbc 0x14    \.d.....
    decimal
             92    8  100    8   20   24  188   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2012-10-25T20:38:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-10-25T20:38:24)
    0000   0x98 0xa6 0x54 0x19 0x0c                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 71 CalForBG 2012-10-25T21:53:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2012-10-25T21:53:35)
    0000   0xa3 0xb5 0x35 0x19 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 72 ResultTotals 2012-08-25T13:12:57 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x00                   .....
    decimal
              7    0    0    5    0
    datetime (2012-08-25T13:12:57)
    0000   0xb9 0x0c 0x6d 0xb9 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xa6 0x61 0x0a 0x06 0x00 0x00    ...a....
    0008   0x05 0x00 0x03 0x78 0x45 0x01 0x88 0x1f    ...xE...
    0010   0x00 0x33 0x01 0x88 0x1f 0x00 0x98 0x27    .3.....'
    0018   0x00 0xf0 0x3d 0x00 0x00 0x00 0x04 0x02    ..=.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  166   97   10    6    0    0
              5    0    3  120   69    1  136   31
              0   51    1  136   31    0  152   39
              0  240   61    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 73 PumpSuspend 2012-10-26T03:57:03 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-26T03:57:03)
    0000   0x83 0xb9 0x03 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 74 PumpResume 2012-10-26T09:34:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-26T09:34:18)
    0000   0x92 0xa2 0x09 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 75 CalForBG 2012-10-26T09:40:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2012-10-26T09:40:17)
    0000   0x91 0xa8 0x29 0x1a 0x8c                   ..)..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 76 BolusWizard 2012-10-26T09:40:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 327,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x47                                  [G
    decimal
             91   71
    datetime (2012-10-26T09:40:24)
    0000   0x98 0xa8 0x09 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2c 0x00 0x00    .Q.-j,..
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
              0   81   13   45  106   44    0    0
              0    0    0   44  125
    HOUR BITS: [1, 0, 1]
#### RECORD 77 Bolus 2012-10-26T09:40:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'programmed': 4.7}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2012-10-26T09:40:24)
    0000   0x98 0xa8 0x49 0x1a 0x0c                   ..I..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 78 PumpSuspend 2012-10-26T11:57:03 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-26T11:57:03)
    0000   0x83 0xb9 0x0b 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 PumpResume 2012-10-26T12:09:54 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-26T12:09:54)
    0000   0xb6 0x89 0x0c 0x1a 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 80 CalForBG 2012-10-26T12:40:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 237}
```
    op hex (2)
    0000   0x0a 0xed                                  ..
    decimal
             10  237
    datetime (2012-10-26T12:40:41)
    0000   0xa9 0xa8 0x2c 0x1a 0x0c                   ..,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 81 BolusWizard 2012-10-26T12:41:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 237,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.8}
```
    op hex (2)
    0000   0x5b 0xed                                  [.
    decimal
             91  237
    datetime (2012-10-26T12:41:17)
    0000   0x91 0xa9 0x0c 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x18 0x00 0x00    .P.-j...
    0008   0x00 0x08 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   24    0    0
              0    8    0   16  125
    HOUR BITS: [1, 0, 1]
#### RECORD 82 BolusGiven unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 187, 'amount': 4.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xbc 0xbb 0x04                   \....
    decimal
             92    5  188  187    4
    datetime (unknown)

    body (0)

#### RECORD 83 Bolus 2012-10-26T12:41:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2012-10-26T12:41:17)
    0000   0x91 0xa9 0x4c 0x1a 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 84 CalForBG 2012-10-26T16:11:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-10-26T16:11:18)
    0000   0x92 0x8b 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 85 CalForBG 2012-10-26T16:14:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2012-10-26T16:14:35)
    0000   0xa3 0x8e 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 86 CalForBG 2012-10-26T16:15:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2012-10-26T16:15:40)
    0000   0xa8 0x8f 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 87 BolusWizard 2012-10-26T16:15:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 92,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 26,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.2}
```
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2012-10-26T16:15:54)
    0000   0xb6 0x8f 0x10 0x1a 0x0c                   .....
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0xfd 0x14 0xf0    .P.-j...
    0008   0x00 0x02 0x00 0x11 0x7d                   ....}
    decimal
             26   80   13   45  106  253   20  240
              0    2    0   17  125
    HOUR BITS: [1, 0, 0]
#### RECORD 88 BolusGiven unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 221, 'amount': 2.0, 'curve': 4},
 {'age': 145, 'amount': 4.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0xdd 0x04 0xbc 0x91 0x14    \.P.....
    decimal
             92    8   80  221    4  188  145   20
    datetime (unknown)

    body (0)

#### RECORD 89 Bolus 2012-10-26T16:15:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'programmed': 1.7}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2012-10-26T16:15:54)
    0000   0xb6 0x8f 0x50 0x1a 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-25.data: 90 records`
