## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1f 0xf2                                  ..
##### DEBUG DECIMAL
             31  242
#### RECORD 0 BolusWizard 2012-09-17T18:56:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 188,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.8}
```
    op hex (2)
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2012-09-17T18:56:02)
    0000   0x82 0x78 0x12 0x11 0x0c                   .x...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x08 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    8    0    6  125
    HOUR BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 0.6, 'curve': 4},
 {'age': 202, 'amount': 2.3, 'curve': 4},
 {'age': 242, 'amount': 0.45, 'curve': 4},
 {'age': 252, 'amount': 2.45, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x48 0x04 0x5c 0xca 0x04    \..H.\..
    0008   0x12 0xf2 0x04 0x62 0xfc 0x04              ...b..
    decimal
             92   14   24   72    4   92  202    4
             18  242    4   98  252    4
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2012-09-17T18:56:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'programmed': 0.6}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-09-17T18:56:02)
    0000   0x82 0x78 0x52 0x11 0x0c                   .xR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2012-09-17T18:58:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2012-09-17T18:58:45)
    0000   0xad 0x7a 0x32 0x11 0x0c                   .z2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 CalBGForPH 2012-09-17T18:58:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2012-09-17T18:58:48)
    0000   0xb0 0x7a 0x32 0x11 0x0c                   .z2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2012-09-17T18:59:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 188,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 1.3}
```
    op hex (2)
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2012-09-17T18:59:07)
    0000   0x87 0x7b 0x12 0x11 0x0c                   .{...
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x0e 0x1e 0x00    (P.-j...
    0008   0x00 0x0d 0x00 0x1f 0x7d                   ....}
    decimal
             40   80   13   45  106   14   30    0
              0   13    0   31  125
    HOUR BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 0.6, 'curve': 4},
 {'age': 75, 'amount': 0.6, 'curve': 4},
 {'age': 205, 'amount': 2.3, 'curve': 4},
 {'age': 245, 'amount': 0.45, 'curve': 4},
 {'age': 255, 'amount': 2.45, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x18 0x05 0x04 0x18 0x4b 0x04    \.....K.
    0008   0x5c 0xcd 0x04 0x12 0xf5 0x04 0x62 0xff    \.....b.
    0010   0x04                                       .
    decimal
             92   17   24    5    4   24   75    4
             92  205    4   18  245    4   98  255
              4
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2012-09-17T18:59:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-09-17T18:59:07)
    0000   0x87 0x7b 0x52 0x11 0x0c                   .{R..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 8 ResultTotals 2012-10-17T13:12:17 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x08                   .....
    decimal
              7    0    0    5    8
    datetime (2012-10-17T13:12:17)
    0000   0x91 0x8c 0x6d 0x91 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x9f 0x46 0xbc 0x07 0x00 0x00    ...F....
    0008   0x05 0x08 0x03 0x70 0x44 0x01 0x98 0x20    ...pD.. 
    0010   0x00 0x88 0x01 0x98 0x20 0x01 0x78 0x5c    .... .x\
    0018   0x00 0x20 0x08 0x00 0x00 0x00 0x06 0x04    . ......
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  159   70  188    7    0    0
              5    8    3  112   68    1  152   32
              0  136    1  152   32    1  120   92
              0   32    8    0    0    0    6    4
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 Rewind 2012-09-18T04:36:42 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-09-18T04:36:42)
    0000   0xaa 0x64 0x04 0x12 0x0c                   .d...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 Prime 2012-09-18T04:38:09 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x28                   ....(
    decimal
              3    0    0    0   40
    datetime (2012-09-18T04:38:09)
    0000   0x89 0x66 0x24 0x12 0x0c                   .f$..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 11 Prime 2012-09-18T04:38:36 head[5], body[0] op[0x03]

    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-09-18T04:38:36)
    0000   0xa4 0x66 0x04 0x12 0x0c                   .f...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 12 CalBGForPH 2012-09-18T04:41:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 325}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2012-09-18T04:41:07)
    0000   0x87 0x69 0x24 0x12 0x8c                   .i$..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 13 BolusWizard 2012-09-18T04:41:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 325,
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
    0000   0x5b 0x45                                  [E
    decimal
             91   69
    datetime (2012-09-18T04:41:11)
    0000   0x8b 0x69 0x04 0x12 0x0c                   .i...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2c 0x00 0x00    .Q.-j,..
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
              0   81   13   45  106   44    0    0
              0    0    0   44  125
    HOUR BITS: [0, 1, 1]
#### RECORD 14 Bolus 2012-09-18T04:41:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'programmed': 4.4}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2012-09-18T04:41:11)
    0000   0x8b 0x69 0x44 0x12 0x0c                   .iD..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 15 PumpSuspend 2012-09-18T11:58:52 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-18T11:58:52)
    0000   0xb4 0x7a 0x0b 0x12 0x0c                   .z...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 16 PumpResume 2012-09-18T12:25:16 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-18T12:25:16)
    0000   0x90 0x59 0x0c 0x12 0x0c                   .Y...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 17 CalBGForPH 2012-09-18T13:32:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 183}
```
    op hex (2)
    0000   0x0a 0xb7                                  ..
    decimal
             10  183
    datetime (2012-09-18T13:32:07)
    0000   0x87 0x60 0x2d 0x12 0x0c                   .`-..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 18 BolusWizard 2012-09-18T13:32:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 183,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.2,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xb7                                  [.
    decimal
             91  183
    datetime (2012-09-18T13:32:31)
    0000   0x9f 0x60 0x0d 0x12 0x0c                   .`...
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0x0c 0x28 0x00    5P.-j.(.
    0008   0x00 0x00 0x00 0x34 0x7d                   ...4}
    decimal
             53   80   13   45  106   12   40    0
              0    0    0   52  125
    HOUR BITS: [0, 1, 1]
#### RECORD 19 Bolus 2012-09-18T13:32:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2, 'programmed': 5.2}
```
    op hex (4)
    0000   0x01 0x34 0x34 0x00                        .44.
    decimal
              1   52   52    0
    datetime (2012-09-18T13:32:32)
    0000   0xa0 0x60 0x4d 0x12 0x0c                   .`M..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2012-09-18T13:41:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 10,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-18T13:41:10)
    0000   0x8a 0x69 0x0d 0x12 0x0c                   .i...
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106    0    7    0
              0    0    0    7  125
    HOUR BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 3.05, 'curve': 4},
 {'age': 17, 'amount': 2.15, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x7a 0x07 0x04 0x56 0x11 0x04    \.z..V..
    decimal
             92    8  122    7    4   86   17    4
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2012-09-18T13:41:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'programmed': 0.7}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2012-09-18T13:41:11)
    0000   0x8b 0x69 0x4d 0x12 0x0c                   .iM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2012-09-18T14:45:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 10,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-18T14:45:16)
    0000   0x90 0x6d 0x0e 0x12 0x0c                   .m...
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106    0    7    0
              0    0    0    7  125
    HOUR BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 3.75, 'curve': 4},
 {'age': 81, 'amount': 2.15, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x96 0x47 0x04 0x56 0x51 0x04    \..G.VQ.
    decimal
             92    8  150   71    4   86   81    4
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2012-09-18T14:45:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'programmed': 0.7}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2012-09-18T14:45:17)
    0000   0x91 0x6d 0x4e 0x12 0x0c                   .mN..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 26 CalBGForPH 2012-09-18T23:51:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2012-09-18T23:51:22)
    0000   0x96 0x73 0x37 0x12 0x0c                   .s7..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 27 BolusWizard 2012-09-18T23:51:48 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 142,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x8e                                  [.
    decimal
             91  142
    datetime (2012-09-18T23:51:48)
    0000   0xb0 0x73 0x17 0x12 0x0c                   .s...
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0x03 0x21 0x00    ,P.-j.!.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             44   80   13   45  106    3   33    0
              0    0    0   36  125
    HOUR BITS: [0, 1, 1]
#### RECORD 28 Bolus 2012-09-18T23:51:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-09-18T23:51:48)
    0000   0xb0 0x73 0x57 0x12 0x0c                   .sW..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 29 ResultTotals 2012-10-18T13:12:18 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xb6                   .....
    decimal
              7    0    0    5  182
    datetime (2012-10-18T13:12:18)
    0000   0x92 0x8c 0x6d 0x92 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xd9 0x8e 0x45 0x03 0x00 0x00    ....E...
    0008   0x05 0xb6 0x03 0x6e 0x3c 0x02 0x48 0x28    ...n<.H(
    0010   0x00 0x75 0x02 0x48 0x28 0x01 0x5c 0x3c    .u.H(.\<
    0018   0x00 0xec 0x28 0x00 0x00 0x00 0x05 0x02    ..(.....
    0020   0x01 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  217  142   69    3    0    0
              5  182    3  110   60    2   72   40
              0  117    2   72   40    1   92   60
              0  236   40    0    0    0    5    2
              1    2    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 PumpSuspend 2012-09-19T14:12:51 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-19T14:12:51)
    0000   0xb3 0x4c 0x0e 0x13 0x0c                   .L...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 31 PumpResume 2012-09-19T14:45:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-19T14:45:08)
    0000   0x88 0x6d 0x0e 0x13 0x0c                   .m...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 32 CalBGForPH 2012-09-19T15:16:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2012-09-19T15:16:38)
    0000   0xa6 0x50 0x2f 0x13 0x0c                   .P/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 33 BolusWizard 2012-09-19T15:17:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 104,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.2,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2012-09-19T15:17:19)
    0000   0x93 0x51 0x0f 0x13 0x0c                   .Q...
    body (13)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0xff 0x35 0xf0    FP.-j.5.
    0008   0x00 0x00 0x00 0x34 0x7d                   ...4}
    decimal
             70   80   13   45  106  255   53  240
              0    0    0   52  125
    HOUR BITS: [0, 1, 0]
#### RECORD 34 Bolus 2012-09-19T15:17:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2, 'programmed': 5.2}
```
    op hex (4)
    0000   0x01 0x34 0x34 0x00                        .44.
    decimal
              1   52   52    0
    datetime (2012-09-19T15:17:19)
    0000   0x93 0x51 0x4f 0x13 0x0c                   .QO..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 35 BolusWizard 2012-09-19T16:18:42 head[2], body[13] op[0x5b]
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
    datetime (2012-09-19T16:18:42)
    0000   0xaa 0x52 0x10 0x13 0x0c                   .R...
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0    0    0    8  125
    HOUR BITS: [0, 1, 0]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 5.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xd0 0x40 0x04                   \..@.
    decimal
             92    5  208   64    4
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2012-09-19T16:18:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'programmed': 0.8}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2012-09-19T16:18:42)
    0000   0xaa 0x52 0x50 0x13 0x0c                   .RP..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 38 BolusWizard 2012-09-19T16:38:06 head[2], body[13] op[0x5b]
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
    datetime (2012-09-19T16:38:06)
    0000   0x86 0x66 0x10 0x13 0x0c                   .f...
    body (13)
    hex
    0000   0x05 0x50 0x0d 0x2d 0x6a 0x00 0x03 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x03 0x7d                   ....}
    decimal
              5   80   13   45  106    0    3    0
              0    0    0    3  125
    HOUR BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 0.8, 'curve': 4},
 {'age': 84, 'amount': 5.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x18 0x04 0xd0 0x54 0x04    \. ...T.
    decimal
             92    8   32   24    4  208   84    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2012-09-19T16:38:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-09-19T16:38:06)
    0000   0x86 0x66 0x50 0x13 0x0c                   .fP..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 41 CalBGForPH 2012-09-19T18:24:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2012-09-19T18:24:39)
    0000   0xa7 0x58 0x32 0x13 0x0c                   .X2..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 42 CalBGForPH 2012-09-19T21:46:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 293}
```
    op hex (2)
    0000   0x0a 0x25                                  .%
    decimal
             10   37
    datetime (2012-09-19T21:46:25)
    0000   0x99 0x6e 0x35 0x13 0x8c                   .n5..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 BolusWizard 2012-09-19T21:46:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 293,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x25                                  [%
    decimal
             91   37
    datetime (2012-09-19T21:46:35)
    0000   0xa3 0x6e 0x15 0x13 0x0c                   .n...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x25 0x00 0x00    .Q.-j%..
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
              0   81   13   45  106   37    0    0
              0    0    0   37  125
    HOUR BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 0.3, 'curve': 20},
 {'age': 76, 'amount': 0.8, 'curve': 20},
 {'age': 136, 'amount': 5.2, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x38 0x14 0x20 0x4c 0x14    \..8. L.
    0008   0xd0 0x88 0x14                             ...
    decimal
             92   11   12   56   20   32   76   20
            208  136   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2012-09-19T21:46:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'programmed': 2.2}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2012-09-19T21:46:35)
    0000   0xa3 0x6e 0x55 0x13 0x0c                   .nU..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 46 ResultTotals 2012-10-19T13:12:19 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc4                   .....
    decimal
              7    0    0    4  196
    datetime (2012-10-19T13:12:19)
    0000   0x93 0x8c 0x6d 0x93 0x8c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xc1 0x68 0x25 0x03 0x00 0x00    ...h%...
    0008   0x04 0xc4 0x03 0x70 0x48 0x01 0x54 0x1c    ...pH.T.
    0010   0x00 0x56 0x01 0x54 0x1c 0x00 0xfc 0x4a    .V.T...J
    0018   0x00 0x58 0x1a 0x00 0x00 0x00 0x04 0x03    .X......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  193  104   37    3    0    0
              4  196    3  112   72    1   84   28
              0   86    1   84   28    0  252   74
              0   88   26    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 47 CalBGForPH 2012-09-20T08:52:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 284}
```
    op hex (2)
    0000   0x0a 0x1c                                  ..
    decimal
             10   28
    datetime (2012-09-20T08:52:14)
    0000   0x8e 0x74 0x28 0x14 0x8c                   .t(..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 48 BolusWizard 2012-09-20T08:52:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 284,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x1c                                  [.
    decimal
             91   28
    datetime (2012-09-20T08:52:16)
    0000   0x90 0x74 0x08 0x14 0x0c                   .t...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00 0x00    .Q.-j#..
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
              0   81   13   45  106   35    0    0
              0    0    0   35  125
    HOUR BITS: [0, 1, 1]
#### RECORD 49 Bolus 2012-09-20T08:52:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'programmed': 3.5}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2012-09-20T08:52:16)
    0000   0x90 0x74 0x48 0x14 0x0c                   .tH..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 50 PumpSuspend 2012-09-20T11:04:04 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-20T11:04:04)
    0000   0x84 0x44 0x0b 0x14 0x0c                   .D...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 51 PumpResume 2012-09-20T11:18:01 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-20T11:18:01)
    0000   0x81 0x52 0x0b 0x14 0x0c                   .R...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 52 CalBGForPH 2012-09-20T12:00:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2012-09-20T12:00:56)
    0000   0xb8 0x40 0x2c 0x14 0x0c                   .@,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 53 BolusWizard 2012-09-20T12:01:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 177,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0xb1                                  [.
    decimal
             91  177
    datetime (2012-09-20T12:01:13)
    0000   0x8d 0x41 0x0c 0x14 0x0c                   .A...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    5    0    6  125
    HOUR BITS: [0, 1, 0]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 187, 'amount': 0.95, 'curve': 4},
 {'age': 197, 'amount': 2.55, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x26 0xbb 0x04 0x66 0xc5 0x04    \.&..f..
    decimal
             92    8   38  187    4  102  197    4
    datetime (unknown)

    body (0)

#### RECORD 55 PumpSuspend 2012-09-20T12:01:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-09-20T12:01:15)
    0000   0x8f 0x41 0x0c 0x14 0x0c                   .A...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 56 Bolus 2012-09-20T12:01:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'programmed': 0.1}
```
    op hex (4)
    0000   0x01 0x08 0x01 0x00                        ....
    decimal
              1    8    1    0
    datetime (2012-09-20T12:01:14)
    0000   0x8e 0x41 0x4c 0x14 0x0c                   .AL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 PumpResume 2012-09-20T12:01:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-09-20T12:01:18)
    0000   0x92 0x41 0x0c 0x14 0x0c                   .A...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 58 CalBGForPH 2012-09-20T12:01:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2012-09-20T12:01:42)
    0000   0xaa 0x41 0x2c 0x14 0x0c                   .A,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 59 BolusWizard 2012-09-20T12:01:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 177,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.6}
```
    op hex (2)
    0000   0x5b 0xb1                                  [.
    decimal
             91  177
    datetime (2012-09-20T12:01:49)
    0000   0xb1 0x41 0x0c 0x14 0x0c                   .A...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0b 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106   11    0    0
              0    6    0    5  125
    HOUR BITS: [0, 1, 0]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 0.05, 'curve': 4},
 {'age': 187, 'amount': 0.95, 'curve': 4},
 {'age': 197, 'amount': 2.55, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x02 0x07 0x04 0x26 0xbb 0x04    \....&..
    0008   0x66 0xc5 0x04                             f..
    decimal
             92   11    2    7    4   38  187    4
            102  197    4
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2012-09-20T12:01:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'programmed': 0.5}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2012-09-20T12:01:49)
    0000   0xb1 0x41 0x4c 0x14 0x0c                   .AL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 62 CalBGForPH 2012-09-20T13:03:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 155}
```
    op hex (2)
    0000   0x0a 0x9b                                  ..
    decimal
             10  155
    datetime (2012-09-20T13:03:38)
    0000   0xa6 0x43 0x2d 0x14 0x0c                   .C-..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 63 BolusWizard 2012-09-20T13:03:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 155,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0x9b                                  [.
    decimal
             91  155
    datetime (2012-09-20T13:03:44)
    0000   0xac 0x43 0x0d 0x14 0x0c                   .C...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    5    0    1  125
    HOUR BITS: [0, 1, 0]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 0.55, 'curve': 4},
 {'age': 249, 'amount': 0.95, 'curve': 4},
 {'age': 3, 'amount': 2.55, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x16 0x45 0x04 0x26 0xf9 0x04    \..E.&..
    0008   0x66 0x03 0x14                             f..
    decimal
             92   11   22   69    4   38  249    4
            102    3   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2012-09-20T13:03:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'programmed': 0.2}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2012-09-20T13:03:44)
    0000   0xac 0x43 0x4d 0x14 0x0c                   .CM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 66 CalBGForPH 2012-09-20T13:42:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2012-09-20T13:42:58)
    0000   0xba 0x6a 0x2d 0x14 0x0c                   .j-..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 67 CalBGForPH 2012-09-20T13:44:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2012-09-20T13:44:13)
    0000   0x8d 0x6c 0x2d 0x14 0x0c                   .l-..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 68 BolusWizard 2012-09-20T13:44:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 94,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 24.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.5}
```
    op hex (2)
    0000   0x5b 0x5e                                  [^
    decimal
             91   94
    datetime (2012-09-20T13:44:20)
    0000   0x94 0x6c 0x0d 0x14 0x0c                   .l...
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0xfd 0x16 0xf0    .P.-j...
    0008   0x00 0x05 0x00 0x13 0x7d                   ....}
    decimal
             29   80   13   45  106  253   22  240
              0    5    0   19  125
    HOUR BITS: [0, 1, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 0.2, 'curve': 4},
 {'age': 110, 'amount': 0.55, 'curve': 4},
 {'age': 34, 'amount': 0.95, 'curve': 20},
 {'age': 44, 'amount': 2.55, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x08 0x32 0x04 0x16 0x6e 0x04    \..2..n.
    0008   0x26 0x22 0x14 0x66 0x2c 0x14              &".f,.
    decimal
             92   14    8   50    4   22  110    4
             38   34   20  102   44   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2012-09-20T13:44:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-09-20T13:44:20)
    0000   0x94 0x6c 0x4d 0x14 0x0c                   .lM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 71 CalBGForPH 2012-09-20T13:53:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2012-09-20T13:53:30)
    0000   0x9e 0x75 0x2d 0x14 0x0c                   .u-..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 72 BolusWizard 2012-09-20T13:53:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 115,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 10,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 2.4}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2012-09-20T13:53:58)
    0000   0xba 0x75 0x0d 0x14 0x0c                   .u...
    body (13)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x07 0x7d                   ....}
    decimal
             10   80   13   45  106    0    7    0
              0   24    0    7  125
    HOUR BITS: [0, 1, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 1.9, 'curve': 4},
 {'age': 59, 'amount': 0.2, 'curve': 4},
 {'age': 119, 'amount': 0.55, 'curve': 4},
 {'age': 43, 'amount': 0.95, 'curve': 20},
 {'age': 53, 'amount': 2.55, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x4c 0x09 0x04 0x08 0x3b 0x04    \.L...;.
    0008   0x16 0x77 0x04 0x26 0x2b 0x14 0x66 0x35    .w.&+.f5
    0010   0x14                                       .
    decimal
             92   17   76    9    4    8   59    4
             22  119    4   38   43   20  102   53
             20
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2012-09-20T13:53:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'programmed': 0.7}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2012-09-20T13:53:58)
    0000   0xba 0x75 0x4d 0x14 0x0c                   .uM..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 75 CalBGForPH 2012-09-20T18:37:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2012-09-20T18:37:12)
    0000   0x8c 0x65 0x32 0x14 0x0c                   .e2..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 76 BolusWizard 2012-09-20T19:02:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 41,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-20T19:02:06)
    0000   0x86 0x42 0x13 0x14 0x0c                   .B...
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x00 0x1f 0x00    )P.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             41   80   13   45  106    0   31    0
              0    0    0   31  125
    HOUR BITS: [0, 1, 0]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 0.65, 'curve': 20},
 {'age': 62, 'amount': 1.95, 'curve': 20},
 {'age': 112, 'amount': 0.2, 'curve': 20},
 {'age': 172, 'amount': 0.55, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1a 0x34 0x14 0x4e 0x3e 0x14    \..4.N>.
    0008   0x08 0x70 0x14 0x16 0xac 0x14              .p....
    decimal
             92   14   26   52   20   78   62   20
              8  112   20   22  172   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2012-09-20T19:02:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'programmed': 3.1}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2012-09-20T19:02:06)
    0000   0x86 0x42 0x53 0x14 0x0c                   .BS..
    body (0)
    HOUR BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-34.data: 79 records`
