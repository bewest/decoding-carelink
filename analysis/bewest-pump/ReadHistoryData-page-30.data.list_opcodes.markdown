## START logs/ReadHistoryData-page-30.data
#### RECORD 0 Bolus 2012-10-01T23:44:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'programmed': 1.1}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2012-10-01T23:44:01)
    0000   0x81 0xac 0x57 0x01 0x0c                   ..W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 1 ResultTotals 2012-08-01T13:12:33 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x62                   ....b
    decimal
              7    0    0    5   98
    datetime (2012-08-01T13:12:33)
    0000   0xa1 0x0c 0x6d 0xa1 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xaa 0x50 0xff 0x06 0x00 0x00    ...P....
    0008   0x05 0x62 0x03 0x6e 0x40 0x01 0xf4 0x24    .b.n@..$
    0010   0x00 0x8b 0x01 0xf4 0x24 0x01 0x8c 0x4f    ....$..O
    0018   0x00 0x68 0x15 0x00 0x00 0x00 0x07 0x05    .h......
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  170   80  255    6    0    0
              5   98    3  110   64    1  244   36
              0  139    1  244   36    1  140   79
              0  104   21    0    0    0    7    5
              2    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2012-10-02T07:30:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 334}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2012-10-02T07:30:41)
    0000   0xa9 0x9e 0x27 0x02 0x8c                   ..'..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 BolusWizard 2012-10-02T07:30:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 46,
 '_byte[7]': 0,
 'bg': 334,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
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
    datetime (2012-10-02T07:30:43)
    0000   0xab 0x9e 0x07 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2e 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
              0   81   13   45  106   46    0    0
              0    0    0   46  125
    HOUR BITS: [1, 0, 0]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 210, 'amount': 1.1, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0xd2 0x14                   \.,..
    decimal
             92    5   44  210   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2012-10-02T07:30:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'programmed': 4.6}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2012-10-02T07:30:43)
    0000   0xab 0x9e 0x47 0x02 0x0c                   ..G..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 PumpSuspend 2012-10-02T12:32:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-02T12:32:00)
    0000   0x80 0xa0 0x0c 0x02 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 7 PumpResume 2012-10-02T13:03:11 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-02T13:03:11)
    0000   0x8b 0x83 0x0d 0x02 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 CalBGForPH 2012-10-02T13:33:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2012-10-02T13:33:41)
    0000   0xa9 0xa1 0x2d 0x02 0x0c                   ..-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 BolusWizard 2012-10-02T13:34:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 157,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9d                                  [.
    decimal
             91  157
    datetime (2012-10-02T13:34:38)
    0000   0xa6 0xa2 0x0d 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x07 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             47   80   13   45  106    7   36    0
              0    0    0   43  125
    HOUR BITS: [1, 0, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 114, 'amount': 4.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb8 0x72 0x14                   \..r.
    decimal
             92    5  184  114   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2012-10-02T13:34:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'programmed': 4.3}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2012-10-02T13:34:38)
    0000   0xa6 0xa2 0x4d 0x02 0x0c                   ..M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 BolusWizard 2012-10-02T17:05:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.9,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.9,
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
    datetime (2012-10-02T17:05:31)
    0000   0x9f 0x85 0x11 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0x00 0x13 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x13 0x7d                   ....}
    decimal
             25   80   13   45  106    0   19    0
              0    0    0   19  125
    HOUR BITS: [1, 0, 0]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 4.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xac 0xd3 0x04                   \....
    decimal
             92    5  172  211    4
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2012-10-02T17:05:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-10-02T17:05:32)
    0000   0xa0 0x85 0x51 0x02 0x0c                   ..Q..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 15 BolusWizard 2012-10-02T18:37:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
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
    datetime (2012-10-02T18:37:21)
    0000   0x95 0xa5 0x12 0x02 0x0c                   .....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             47   80   13   45  106    0   36    0
              0    0    0   36  125
    HOUR BITS: [1, 0, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 93, 'amount': 1.9, 'curve': 4},
 {'age': 47, 'amount': 4.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x5d 0x04 0xac 0x2f 0x14    \.L]../.
    decimal
             92    8   76   93    4  172   47   20
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2012-10-02T18:37:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-10-02T18:37:21)
    0000   0x95 0xa5 0x52 0x02 0x0c                   ..R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 ResultTotals 2012-08-02T13:12:34 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xac                   .....
    decimal
              7    0    0    5  172
    datetime (2012-08-02T13:12:34)
    0000   0xa2 0x0c 0x6d 0xa2 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xf6 0x9d 0x4e 0x02 0x00 0x00    ....N...
    0008   0x05 0xac 0x03 0x6c 0x3c 0x02 0x40 0x28    ...l<.@(
    0010   0x00 0x77 0x02 0x40 0x28 0x01 0x6c 0x3f    .w.@(.l?
    0018   0x00 0xd4 0x25 0x00 0x00 0x00 0x04 0x02    ..%.....
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  246  157   78    2    0    0
              5  172    3  108   60    2   64   40
              0  119    2   64   40    1  108   63
              0  212   37    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 19 PumpSuspend 2012-10-03T21:05:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-03T21:05:18)
    0000   0x92 0x85 0x15 0x03 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 PumpResume 2012-10-03T21:43:15 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-03T21:43:15)
    0000   0x8f 0xab 0x15 0x03 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 21 CalBGForPH 2012-10-03T21:44:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2012-10-03T21:44:08)
    0000   0x88 0xac 0x35 0x03 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 BolusWizard 2012-10-03T21:44:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 76,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 32,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 2.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4c                                  [L
    decimal
             91   76
    datetime (2012-10-03T21:44:27)
    0000   0x9b 0xac 0x15 0x03 0x0c                   .....
    body (13)
    hex
    0000   0x20 0x50 0x0d 0x2d 0x6a 0xf9 0x18 0xf0     P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             32   80   13   45  106  249   24  240
              0    0    0   17  125
    HOUR BITS: [1, 0, 1]
#### RECORD 23 Bolus 2012-10-03T21:44:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'programmed': 1.7}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2012-10-03T21:44:27)
    0000   0x9b 0xac 0x55 0x03 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 ResultTotals 2012-08-03T13:12:35 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xb0                   .....
    decimal
              7    0    0    3  176
    datetime (2012-08-03T13:12:35)
    0000   0xa3 0x0c 0x6d 0xa3 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x4c 0x4c 0x4c 0x01 0x00 0x00    ..LLL...
    0008   0x03 0xb0 0x03 0x6c 0x5d 0x00 0x44 0x07    ...l].D.
    0010   0x00 0x20 0x00 0x44 0x07 0x00 0x44 0x64    . .D..Dd
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   76   76   76    1    0    0
              3  176    3  108   93    0   68    7
              0   32    0   68    7    0   68  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 25 PumpSuspend 2012-10-04T10:38:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-04T10:38:38)
    0000   0xa6 0xa6 0x0a 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 26 PumpResume 2012-10-04T10:56:54 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-04T10:56:54)
    0000   0xb6 0xb8 0x0a 0x04 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 27 BolusWizard 2012-10-04T11:52:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.5,
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
    datetime (2012-10-04T11:52:56)
    0000   0xb8 0xb4 0x0b 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125
    HOUR BITS: [1, 0, 1]
#### RECORD 28 Bolus 2012-10-04T11:52:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-10-04T11:52:56)
    0000   0xb8 0xb4 0x4b 0x04 0x0c                   ..K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 29 BolusWizard 2012-10-04T12:53:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 47,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
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
    datetime (2012-10-04T12:53:10)
    0000   0x8a 0xb5 0x0c 0x04 0x0c                   .....
    body (13)
    hex
    0000   0x2f 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    /P.-j.$.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             47   80   13   45  106    0   36    0
              0    0    0   36  125
    HOUR BITS: [1, 0, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 1.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x45 0x04                   \.<E.
    decimal
             92    5   60   69    4
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2012-10-04T12:53:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'programmed': 3.6}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2012-10-04T12:53:10)
    0000   0x8a 0xb5 0x4c 0x04 0x0c                   ..L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 32 ResultTotals 2012-08-04T13:12:36 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x44                   ....D
    decimal
              7    0    0    4   68
    datetime (2012-08-04T13:12:36)
    0000   0xa4 0x0c 0x6d 0xa4 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x04 0x44 0x03 0x78 0x51 0x00 0xcc 0x13    .D.xQ...
    0010   0x00 0x43 0x00 0xcc 0x13 0x00 0xcc 0x64    .C.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              4   68    3  120   81    0  204   19
              0   67    0  204   19    0  204  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 33 LowReservoir 2012-10-05T00:18:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-10-05T00:18:45)
    0000   0xad 0x92 0x00 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 34 LowReservoir 2012-10-05T11:30:01 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-10-05T11:30:01)
    0000   0x81 0x9e 0x0b 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 PumpSuspend 2012-10-05T14:27:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-05T14:27:18)
    0000   0x92 0x9b 0x0e 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 PumpResume 2012-10-05T14:41:19 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-05T14:41:19)
    0000   0x93 0xa9 0x0e 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 37 BolusWizard 2012-10-05T15:47:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
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
    datetime (2012-10-05T15:47:01)
    0000   0x81 0xaf 0x0f 0x05 0x0c                   .....
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    "P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             34   80   13   45  106    0   26    0
              0    0    0   26  125
    HOUR BITS: [1, 0, 1]
#### RECORD 38 Bolus 2012-10-05T15:47:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-10-05T15:47:01)
    0000   0x81 0xaf 0x4f 0x05 0x0c                   ..O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 39 Rewind 2012-10-05T19:20:00 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-10-05T19:20:00)
    0000   0x80 0x94 0x13 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 Prime 2012-10-05T19:22:05 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x28                   ....(
    decimal
              3    0    0    0   40
    datetime (2012-10-05T19:22:05)
    0000   0x85 0x96 0x33 0x05 0x0c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 41 Prime 2012-10-05T19:22:33 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-10-05T19:22:33)
    0000   0xa1 0x96 0x13 0x05 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 CalBGForPH 2012-10-05T19:25:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2012-10-05T19:25:11)
    0000   0x8b 0x99 0x33 0x05 0x8c                   ..3..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 BolusWizard 2012-10-05T19:25:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 268,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2012-10-05T19:25:13)
    0000   0x8d 0x99 0x13 0x05 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x02 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0    2    0   29  125
    HOUR BITS: [1, 0, 0]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 221, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0xdd 0x04                   \.h..
    decimal
             92    5  104  221    4
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2012-10-05T19:25:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-10-05T19:25:13)
    0000   0x8d 0x99 0x53 0x05 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 46 BolusWizard 2012-10-05T19:33:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.8,
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
    datetime (2012-10-05T19:33:21)
    0000   0x95 0xa1 0x13 0x05 0x0c                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x00 0x26 0x00    2P.-j.&.
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
             50   80   13   45  106    0   38    0
              0    0    0   38  125
    HOUR BITS: [1, 0, 1]
#### RECORD 47 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 2.9, 'curve': 4},
 {'age': 229, 'amount': 2.6, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0x09 0x04 0x68 0xe5 0x04    \.t..h..
    decimal
             92    8  116    9    4  104  229    4
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2012-10-05T19:33:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'programmed': 3.8}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2012-10-05T19:33:21)
    0000   0x95 0xa1 0x53 0x05 0x0c                   ..S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 ResultTotals 2012-08-05T13:12:37 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xec                   .....
    decimal
              7    0    0    4  236
    datetime (2012-08-05T13:12:37)
    0000   0xa5 0x0c 0x6d 0xa5 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x15 0x0c 0x0c 0x0c 0x01 0x00 0x00    ........
    0008   0x04 0xec 0x03 0x78 0x46 0x01 0x74 0x1e    ...xF.t.
    0010   0x00 0x54 0x01 0x74 0x1e 0x01 0x00 0x45    .T.t...E
    0018   0x00 0x74 0x1f 0x00 0x00 0x00 0x03 0x02    .t......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21   12   12   12    1    0    0
              4  236    3  120   70    1  116   30
              0   84    1  116   30    1    0   69
              0  116   31    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 50 PumpSuspend 2012-10-06T21:24:08 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-06T21:24:08)
    0000   0x88 0x98 0x15 0x06 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 PumpResume 2012-10-06T21:41:30 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-06T21:41:30)
    0000   0x9e 0xa9 0x15 0x06 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 52 BolusWizard 2012-10-06T22:38:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 54,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.1,
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
    datetime (2012-10-06T22:38:49)
    0000   0xb1 0xa6 0x16 0x06 0x0c                   .....
    body (13)
    hex
    0000   0x36 0x50 0x0d 0x2d 0x6a 0x00 0x29 0x00    6P.-j.).
    0008   0x00 0x00 0x00 0x29 0x7d                   ...)}
    decimal
             54   80   13   45  106    0   41    0
              0    0    0   41  125
    HOUR BITS: [1, 0, 1]
#### RECORD 53 Bolus 2012-10-06T22:38:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'programmed': 4.1}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2012-10-06T22:38:49)
    0000   0xb1 0xa6 0x56 0x06 0x0c                   ..V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 54 CalBGForPH 2012-10-06T23:44:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 250}
```
    op hex (2)
    0000   0x0a 0xfa                                  ..
    decimal
             10  250
    datetime (2012-10-06T23:44:36)
    0000   0xa4 0xac 0x37 0x06 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 55 ResultTotals 2012-08-06T13:12:38 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x1c                   .....
    decimal
              7    0    0    4   28
    datetime (2012-08-06T13:12:38)
    0000   0xa6 0x0c 0x6d 0xa6 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xfa 0xfa 0xfa 0x01 0x00 0x00    ........
    0008   0x04 0x1c 0x03 0x78 0x54 0x00 0xa4 0x10    ...xT...
    0010   0x00 0x36 0x00 0xa4 0x10 0x00 0xa4 0x64    .6.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  250  250  250    1    0    0
              4   28    3  120   84    0  164   16
              0   54    0  164   16    0  164  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 1]
#### RECORD 56 CalBGForPH 2012-10-07T08:04:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2012-10-07T08:04:00)
    0000   0x80 0x84 0x28 0x07 0x0c                   ..(..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 57 BolusWizard 2012-10-07T08:04:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 253,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfd                                  [.
    decimal
             91  253
    datetime (2012-10-07T08:04:02)
    0000   0x82 0x84 0x08 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    0    0   28  125
    HOUR BITS: [1, 0, 0]
#### RECORD 58 Bolus 2012-10-07T08:04:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'programmed': 2.8}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2012-10-07T08:04:02)
    0000   0x82 0x84 0x48 0x07 0x0c                   ..H..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 PumpSuspend 2012-10-07T09:08:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-10-07T09:08:49)
    0000   0xb1 0x88 0x09 0x07 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 60 PumpResume 2012-10-07T14:15:26 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-10-07T14:15:26)
    0000   0x9a 0x8f 0x0e 0x07 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 61 CalBGForPH 2012-10-07T16:16:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 223}
```
    op hex (2)
    0000   0x0a 0xdf                                  ..
    decimal
             10  223
    datetime (2012-10-07T16:16:08)
    0000   0x88 0x90 0x30 0x07 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 BolusWizard 2012-10-07T16:16:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 21,
 '_byte[7]': 0,
 'bg': 223,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdf                                  [.
    decimal
             91  223
    datetime (2012-10-07T16:16:20)
    0000   0x94 0x90 0x10 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    0    0   21  125
    HOUR BITS: [1, 0, 0]
#### RECORD 63 Bolus 2012-10-07T16:16:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'programmed': 2.1}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2012-10-07T16:16:20)
    0000   0x94 0x90 0x50 0x07 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 64 CalBGForPH 2012-10-07T16:58:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 227}
```
    op hex (2)
    0000   0x0a 0xe3                                  ..
    decimal
             10  227
    datetime (2012-10-07T16:58:14)
    0000   0x8e 0xba 0x30 0x07 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 65 BolusWizard 2012-10-07T16:58:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 22,
 '_byte[7]': 0,
 'bg': 227,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 31,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 2.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe3                                  [.
    decimal
             91  227
    datetime (2012-10-07T16:58:56)
    0000   0xb8 0xba 0x10 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x1f 0x50 0x0d 0x2d 0x6a 0x16 0x17 0x00    .P.-j...
    0008   0x00 0x13 0x00 0x1a 0x7d                   ....}
    decimal
             31   80   13   45  106   22   23    0
              0   19    0   26  125
    HOUR BITS: [1, 0, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 2.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x54 0x2c 0x04                   \.T,.
    decimal
             92    5   84   44    4
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2012-10-07T16:58:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'programmed': 2.6}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2012-10-07T16:58:56)
    0000   0xb8 0xba 0x50 0x07 0x0c                   ..P..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 68 CalBGForPH 2012-10-07T21:32:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2012-10-07T21:32:18)
    0000   0x92 0xa0 0x35 0x07 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 69 BolusWizard 2012-10-07T21:32:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 127,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7f                                  [.
    decimal
             91  127
    datetime (2012-10-07T21:32:39)
    0000   0xa7 0xa0 0x15 0x07 0x0c                   .....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x00 0x20 0x00    *P.-j. .
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106    0   32    0
              0    0    0   32  125
    HOUR BITS: [1, 0, 1]
#### RECORD 70 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 2.6, 'curve': 20},
 {'age': 62, 'amount': 2.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x68 0x16 0x14 0x54 0x3e 0x14    \.h..T>.
    decimal
             92    8  104   22   20   84   62   20
    datetime (unknown)

    body (0)

#### RECORD 71 Bolus 2012-10-07T21:32:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-10-07T21:32:40)
    0000   0xa8 0xa0 0x55 0x07 0x0c                   ..U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 72 CalBGForPH 2012-10-07T23:22:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2012-10-07T23:22:11)
    0000   0x8b 0x96 0x37 0x07 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 73 ResultTotals (2000, 8, 0, 0, 12, 39) head[5], body[15] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x52                   ....R
    decimal
              7    0    0    4   82
    datetime ((2000, 8, 0, 0, 12, 39))
    0000   0xa7 0x0c 0x00 0x00 0x00                   .....
    body (15)
    hex
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0xf9 0xc4         .......
    decimal
              0    0    0    0    0    0    0    0
              0    0    0    0    0  249  196

`end logs/ReadHistoryData-page-30.data: 74 records`
