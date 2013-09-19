## START logs/ReadHistoryData-page-2.data
#### RECORD 0 Model522ResultTotals 2013-08-04T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-08-04T00:00:00)
    0000   0x84 0x0d 0x05 0x00 0x96                   .....
    body (38)
    hex
    0000   0x75 0xba 0x04 0x00 0x00 0x05 0x20 0x03    u..... .
    0008   0x70 0x43 0x01 0xb0 0x21 0x00 0x73 0x01    pC..!.s.
    0010   0xb0 0x21 0x01 0x60 0x51 0x00 0x50 0x13    .!.`Q.P.
    0018   0x00 0x00 0x00 0x04 0x02 0x02 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            117  186    4    0    0    5   32    3
            112   67    1  176   33    0  115    1
            176   33    1   96   81    0   80   19
              0    0    0    4    2    2    0    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 1 CalBGForPH 2013-08-05T09:20:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 270}
```
    op hex (2)
    0000   0x0a 0x0e                                  ..
    decimal
             10   14
    datetime (2013-08-05T09:20:35)
    0000   0xa3 0x14 0x29 0x05 0x8d                   ..)..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 2 BolusWizard 2013-08-05T09:20:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 270,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0e                                  [.
    decimal
             91   14
    datetime (2013-08-05T09:20:36)
    0000   0xa4 0x14 0x09 0x05 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
              0   81   13   45  106   32    0    0
              0    0    0   32  125

#### RECORD 3 Bolus 2013-08-05T09:20:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-08-05T09:20:37)
    0000   0xa5 0x14 0x49 0x05 0x0d                   ..I..
    body (0)

#### RECORD 4 CalBGForPH 2013-08-05T21:57:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-08-05T21:57:49)
    0000   0xb1 0x39 0x35 0x05 0x0d                   .95..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BolusWizard 2013-08-05T21:58:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 103,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 66,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-08-05T21:58:28)
    0000   0x9c 0x3a 0x15 0x05 0x0d                   .:...
    body (13)
    hex
    0000   0x42 0x50 0x0d 0x2d 0x6a 0xff 0x32 0xf0    BP.-j.2.
    0008   0x00 0x00 0x00 0x31 0x7d                   ...1}
    decimal
             66   80   13   45  106  255   50  240
              0    0    0   49  125
    HOUR BITS: [0, 0, 1]
#### RECORD 6 Bolus 2013-08-05T21:58:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2013-08-05T21:58:28)
    0000   0x9c 0x3a 0x55 0x05 0x0d                   .:U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 ResultTotals 2013-08-05T13:13:05 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xc8                   .....
    decimal
              7    0    0    4  200
    datetime (2013-08-05T13:13:05)
    0000   0x85 0x0d 0x6d 0x85 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xbb 0x67 0x0e 0x02 0x00 0x00    ...g....
    0008   0x04 0xc8 0x03 0x84 0x4a 0x01 0x44 0x1a    ....J.D.
    0010   0x00 0x42 0x01 0x44 0x1a 0x00 0xc4 0x3c    .B.D...<
    0018   0x00 0x80 0x28 0x00 0x00 0x00 0x02 0x01    ..(.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  187  103   14    2    0    0
              4  200    3  132   74    1   68   26
              0   66    1   68   26    0  196   60
              0  128   40    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 8 CalBGForPH 2013-08-06T08:35:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 298}
```
    op hex (2)
    0000   0x0a 0x2a                                  .*
    decimal
             10   42
    datetime (2013-08-06T08:35:43)
    0000   0xab 0x23 0x28 0x06 0x8d                   .#(..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 BolusWizard 2013-08-06T08:35:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 38,
 '_byte[7]': 0,
 'bg': 298,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x2a                                  [*
    decimal
             91   42
    datetime (2013-08-06T08:35:45)
    0000   0xad 0x23 0x08 0x06 0x0d                   .#...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x26 0x00 0x00    .Q.-j&..
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
              0   81   13   45  106   38    0    0
              0    0    0   38  125
    HOUR BITS: [0, 0, 1]
#### RECORD 10 Bolus 2013-08-06T08:35:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-08-06T08:35:45)
    0000   0xad 0x23 0x48 0x06 0x0d                   .#H..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 LowReservoir 2013-08-06T09:00:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-06T09:00:00)
    0000   0x80 0x00 0x09 0x06 0x0d                   .....
    body (0)

#### RECORD 12 CalBGForPH 2013-08-06T18:21:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 212}
```
    op hex (2)
    0000   0x0a 0xd4                                  ..
    decimal
             10  212
    datetime (2013-08-06T18:21:51)
    0000   0xb3 0x15 0x32 0x06 0x0d                   ..2..
    body (0)

#### RECORD 13 BolusWizard 2013-08-06T18:22:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 19,
 '_byte[7]': 0,
 'bg': 212,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 6.3,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd4                                  [.
    decimal
             91  212
    datetime (2013-08-06T18:22:00)
    0000   0x80 0x16 0x12 0x06 0x0d                   .....
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0x13 0x2c 0x00    :P.-j.,.
    0008   0x00 0x00 0x00 0x3f 0x7d                   ...?}
    decimal
             58   80   13   45  106   19   44    0
              0    0    0   63  125

#### RECORD 14 LowReservoir 2013-08-06T18:22:16 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-08-06T18:22:16)
    0000   0x90 0x16 0x12 0x06 0x0d                   .....
    body (0)

#### RECORD 15 Bolus 2013-08-06T18:22:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.3, 'dual_component': '??', 'programmed': 6.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3f 0x3f 0x00                        .??.
    decimal
              1   63   63    0
    datetime (2013-08-06T18:22:00)
    0000   0x80 0x16 0x52 0x06 0x0d                   ..R..
    body (0)

#### RECORD 16 CalBGForPH 2013-08-06T23:34:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 297}
```
    op hex (2)
    0000   0x0a 0x29                                  .)
    decimal
             10   41
    datetime (2013-08-06T23:34:01)
    0000   0x81 0x22 0x37 0x06 0x8d                   ."7..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 BolusWizard 2013-08-06T23:34:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 38,
 '_byte[7]': 0,
 'bg': 297,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x29                                  [)
    decimal
             91   41
    datetime (2013-08-06T23:34:11)
    0000   0x8b 0x22 0x17 0x06 0x0d                   ."...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x26 0x00 0x00    .Q.-j&..
    0008   0x00 0x00 0x00 0x26 0x7d                   ...&}
    decimal
              0   81   13   45  106   38    0    0
              0    0    0   38  125
    HOUR BITS: [0, 0, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 3.35, 'curve': 20},
 {'age': 64, 'amount': 2.95, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x86 0x36 0x14 0x76 0x40 0x14    \..6.v@.
    decimal
             92    8  134   54   20  118   64   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-08-06T23:34:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-08-06T23:34:11)
    0000   0x8b 0x22 0x57 0x06 0x0d                   ."W..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 ResultTotals 2013-08-06T13:13:06 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x9c                   .....
    decimal
              7    0    0    5  156
    datetime (2013-08-06T13:13:06)
    0000   0x86 0x0d 0x6d 0x86 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x11 0x0d 0xd4 0x2a 0x03 0x00 0x00    ....*...
    0008   0x05 0x9c 0x03 0x84 0x3f 0x02 0x18 0x25    ....?..%
    0010   0x00 0x3a 0x02 0x18 0x25 0x00 0xb0 0x21    .:..%..!
    0018   0x01 0x68 0x43 0x00 0x00 0x00 0x03 0x00    .hC.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   17   13  212   42    3    0    0
              5  156    3  132   63    2   24   37
              0   58    2   24   37    0  176   33
              1  104   67    0    0    0    3    0
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 21 NoDelivery 2013-08-07T16:22:06 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xff                        ....
    decimal
              6    4   11  255
    datetime (2013-08-07T16:22:06)
    0000   0x86 0x16 0x50 0x47 0x0d                   ..PG.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 22 ClearAlarm 2013-08-07T16:25:05 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2013-08-07T16:25:05)
    0000   0x85 0x19 0x10 0x07 0x0d                   .....
    body (0)

#### RECORD 23 Rewind 2013-08-07T21:08:13 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-07T21:08:13)
    0000   0x8d 0x08 0x15 0x07 0x0d                   .....
    body (0)

#### RECORD 24 Prime 2013-08-07T21:08:57 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1a                   .....
    decimal
              3    0    0    0   26
    datetime (2013-08-07T21:08:57)
    0000   0xb9 0x08 0x35 0x07 0x0d                   ..5..
    body (0)

#### RECORD 25 Prime 2013-08-07T21:09:25 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-08-07T21:09:25)
    0000   0x99 0x09 0x15 0x07 0x0d                   .....
    body (0)

#### RECORD 26 CalBGForPH 2013-08-07T21:12:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 195}
```
    op hex (2)
    0000   0x0a 0xc3                                  ..
    decimal
             10  195
    datetime (2013-08-07T21:12:47)
    0000   0xaf 0x0c 0x35 0x07 0x0d                   ..5..
    body (0)

#### RECORD 27 BolusWizard 2013-08-07T21:13:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 195,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc3                                  [.
    decimal
             91  195
    datetime (2013-08-07T21:13:01)
    0000   0x81 0x0d 0x15 0x07 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0    0    0   15  125

#### RECORD 28 Bolus 2013-08-07T21:13:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-08-07T21:13:01)
    0000   0x81 0x0d 0x55 0x07 0x0d                   ..U..
    body (0)

#### RECORD 29 CalBGForPH 2013-08-07T21:48:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2013-08-07T21:48:11)
    0000   0x8b 0x30 0x35 0x07 0x0d                   .05..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 BolusWizard 2013-08-07T21:48:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 11,
 '_byte[7]': 0,
 'bg': 177,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb1                                  [.
    decimal
             91  177
    datetime (2013-08-07T21:48:36)
    0000   0xa4 0x30 0x15 0x07 0x0d                   .0...
    body (13)
    hex
    0000   0x45 0x50 0x0d 0x2d 0x6a 0x0b 0x35 0x00    EP.-j.5.
    0008   0x00 0x0e 0x00 0x35 0x7d                   ...5}
    decimal
             69   80   13   45  106   11   53    0
              0   14    0   53  125
    HOUR BITS: [0, 0, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 1.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x2c 0x04                   \.<,.
    decimal
             92    5   60   44    4
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-08-07T21:48:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-08-07T21:48:37)
    0000   0xa5 0x30 0x55 0x07 0x0d                   .0U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 ResultTotals 2013-08-07T13:13:07 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xdc                   .....
    decimal
              7    0    0    3  220
    datetime (2013-08-07T13:13:07)
    0000   0x87 0x0d 0x6d 0x87 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xba 0xb1 0xc3 0x02 0x00 0x00    ........
    0008   0x03 0xdc 0x02 0xcc 0x48 0x01 0x10 0x1c    ....H...
    0010   0x00 0x45 0x01 0x10 0x1c 0x00 0xd4 0x4e    .E.....N
    0018   0x00 0x3c 0x16 0x00 0x00 0x00 0x02 0x01    .<......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  186  177  195    2    0    0
              3  220    2  204   72    1   16   28
              0   69    1   16   28    0  212   78
              0   60   22    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 34 CalBGForPH 2013-08-08T20:35:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2013-08-08T20:35:35)
    0000   0xa3 0x23 0x34 0x08 0x8d                   .#4..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 35 BolusWizard 2013-08-08T20:35:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 256,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
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
    datetime (2013-08-08T20:35:40)
    0000   0xa8 0x23 0x14 0x08 0x0d                   .#...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1d 0x7d                   ....}
    decimal
              0   81   13   45  106   29    0    0
              0    0    0   29  125
    HOUR BITS: [0, 0, 1]
#### RECORD 36 Bolus 2013-08-08T20:35:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-08-08T20:35:40)
    0000   0xa8 0x23 0x54 0x08 0x0d                   .#T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 CalBGForPH 2013-08-08T20:59:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 267}
```
    op hex (2)
    0000   0x0a 0x0b                                  ..
    decimal
             10   11
    datetime (2013-08-08T20:59:46)
    0000   0xae 0x3b 0x34 0x08 0x8d                   .;4..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 38 BolusWizard 2013-08-08T20:59:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 267,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0b                                  [.
    decimal
             91   11
    datetime (2013-08-08T20:59:53)
    0000   0xb5 0x3b 0x14 0x08 0x0d                   .;...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x1d 0x00 0x02 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0   29    0    2  125
    HOUR BITS: [0, 0, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 3.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x19 0x04                   \.x..
    decimal
             92    5  120   25    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-08-08T20:59:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-08-08T20:59:53)
    0000   0xb5 0x3b 0x54 0x08 0x0d                   .;T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 CalBGForPH 2013-08-08T22:00:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 273}
```
    op hex (2)
    0000   0x0a 0x11                                  ..
    decimal
             10   17
    datetime (2013-08-08T22:00:25)
    0000   0x99 0x00 0x36 0x08 0x8d                   ..6..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 42 BolusWizard 2013-08-08T22:00:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 273,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.8,
 'carb_input': 66,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x11                                  [.
    decimal
             91   17
    datetime (2013-08-08T22:00:41)
    0000   0xa9 0x00 0x16 0x08 0x0d                   .....
    body (13)
    hex
    0000   0x42 0x51 0x0d 0x2d 0x6a 0x20 0x32 0x00    BQ.-j 2.
    0008   0x00 0x18 0x00 0x3a 0x7d                   ...:}
    decimal
             66   81   13   45  106   32   50    0
              0   24    0   58  125

#### RECORD 43 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 0.4, 'curve': 4},
 {'age': 86, 'amount': 3.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x42 0x04 0x78 0x56 0x04    \..B.xV.
    decimal
             92    8   16   66    4  120   86    4
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-08-08T22:00:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.8, 'dual_component': '??', 'programmed': 5.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3a 0x3a 0x00                        .::.
    decimal
              1   58   58    0
    datetime (2013-08-08T22:00:41)
    0000   0xa9 0x00 0x56 0x08 0x0d                   ..V..
    body (0)

#### RECORD 45 ResultTotals 2013-08-08T13:13:08 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf4                   .....
    decimal
              7    0    0    4  244
    datetime (2013-08-08T13:13:08)
    0000   0x88 0x0d 0x6d 0x88 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x15 0x09 0x00 0x11 0x03 0x00 0x00    ........
    0008   0x04 0xf4 0x03 0x84 0x47 0x01 0x70 0x1d    ....G.p.
    0010   0x00 0x42 0x01 0x70 0x1d 0x00 0xc8 0x36    .B.p...6
    0018   0x00 0xa8 0x2e 0x00 0x00 0x00 0x03 0x00    ........
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21    9    0   17    3    0    0
              4  244    3  132   71    1  112   29
              0   66    1  112   29    0  200   54
              0  168   46    0    0    0    3    0
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 46 CalBGForPH 2013-08-09T08:10:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 247}
```
    op hex (2)
    0000   0x0a 0xf7                                  ..
    decimal
             10  247
    datetime (2013-08-09T08:10:18)
    0000   0x92 0x0a 0x28 0x09 0x0d                   ..(..
    body (0)

#### RECORD 47 BolusWizard 2013-08-09T08:10:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 27,
 '_byte[7]': 0,
 'bg': 247,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
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
    0000   0x5b 0xf7                                  [.
    decimal
             91  247
    datetime (2013-08-09T08:10:20)
    0000   0x94 0x0a 0x08 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1b 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
              0   80   13   45  106   27    0    0
              0    0    0   27  125

#### RECORD 48 Bolus 2013-08-09T08:10:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-08-09T08:10:20)
    0000   0x94 0x0a 0x48 0x09 0x0d                   ..H..
    body (0)

#### RECORD 49 CalBGForPH 2013-08-09T21:03:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-08-09T21:03:59)
    0000   0xbb 0x03 0x35 0x09 0x0d                   ..5..
    body (0)

#### RECORD 50 CalBGForPH 2013-08-09T21:06:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2013-08-09T21:06:26)
    0000   0x9a 0x06 0x35 0x09 0x0d                   ..5..
    body (0)

#### RECORD 51 CalBGForPH 2013-08-09T21:07:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2013-08-09T21:07:33)
    0000   0xa1 0x07 0x35 0x09 0x0d                   ..5..
    body (0)

#### RECORD 52 BolusWizard 2013-08-09T21:07:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 248,
 '_byte[7]': 240,
 'bg': 70,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': -0.8,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x46                                  [F
    decimal
             91   70
    datetime (2013-08-09T21:07:44)
    0000   0xac 0x07 0x15 0x09 0x0d                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0xf8 0x26 0xf0    2P.-j.&.
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             50   80   13   45  106  248   38  240
              0    0    0   30  125

#### RECORD 53 Bolus 2013-08-09T21:07:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-08-09T21:07:45)
    0000   0xad 0x07 0x55 0x09 0x0d                   ..U..
    body (0)

#### RECORD 54 ResultTotals 2013-08-09T13:13:09 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x68                   ....h
    decimal
              7    0    0    4  104
    datetime (2013-08-09T13:13:09)
    0000   0x89 0x0d 0x6d 0x89 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x7c 0x46 0xf7 0x04 0x00 0x00    ..|F....
    0008   0x04 0x68 0x03 0x84 0x50 0x00 0xe4 0x14    .h..P...
    0010   0x00 0x32 0x00 0xe4 0x14 0x00 0x78 0x35    .2....x5
    0018   0x00 0x6c 0x2f 0x00 0x00 0x00 0x02 0x01    .l/.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  124   70  247    4    0    0
              4  104    3  132   80    0  228   20
              0   50    0  228   20    0  120   53
              0  108   47    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 55 CalBGForPH 2013-08-10T08:30:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 386}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-08-10T08:30:19)
    0000   0x93 0x1e 0x28 0x0a 0x8d                   ..(..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 56 BolusWizard 2013-08-10T08:30:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 58,
 '_byte[7]': 0,
 'bg': 386,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-08-10T08:30:22)
    0000   0x96 0x1e 0x08 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x3a 0x00 0x00    .Q.-j:..
    0008   0x00 0x00 0x00 0x3a 0x7d                   ...:}
    decimal
              0   81   13   45  106   58    0    0
              0    0    0   58  125

#### RECORD 57 Bolus 2013-08-10T08:30:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.8, 'dual_component': '??', 'programmed': 5.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x3a 0x3a 0x00                        .::.
    decimal
              1   58   58    0
    datetime (2013-08-10T08:30:22)
    0000   0x96 0x1e 0x48 0x0a 0x0d                   ..H..
    body (0)

#### RECORD 58 CalBGForPH 2013-08-10T20:24:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-08-10T20:24:41)
    0000   0xa9 0x18 0x34 0x0a 0x0d                   ..4..
    body (0)

#### RECORD 59 BolusWizard 2013-08-10T20:25:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 118,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x76                                  [v
    decimal
             91  118
    datetime (2013-08-10T20:25:13)
    0000   0x8d 0x19 0x14 0x0a 0x0d                   .....
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0x00 0x2b 0x00    8P.-j.+.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             56   80   13   45  106    0   43    0
              0    0    0   43  125

#### RECORD 60 Bolus 2013-08-10T20:25:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-08-10T20:25:13)
    0000   0x8d 0x19 0x54 0x0a 0x0d                   ..T..
    body (0)

#### RECORD 61 ResultTotals 2013-08-10T13:13:10 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x18                   .....
    decimal
              7    0    0    5   24
    datetime (2013-08-10T13:13:10)
    0000   0x8a 0x0d 0x6d 0x8a 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xfc 0x76 0x82 0x02 0x00 0x00    ...v....
    0008   0x05 0x18 0x03 0x84 0x45 0x01 0x94 0x1f    ....E...
    0010   0x00 0x38 0x01 0x94 0x1f 0x00 0xac 0x2b    .8.....+
    0018   0x00 0xe8 0x39 0x00 0x00 0x00 0x02 0x01    ..9.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  252  118  130    2    0    0
              5   24    3  132   69    1  148   31
              0   56    1  148   31    0  172   43
              0  232   57    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 62 CalBGForPH 2013-08-11T01:35:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-08-11T01:35:06)
    0000   0x86 0x23 0x21 0x0b 0x0d                   .#!..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 LowReservoir 2013-08-11T02:45:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-11T02:45:00)
    0000   0x80 0x2d 0x02 0x0b 0x0d                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 LowReservoir 2013-08-11T13:16:21 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-08-11T13:16:21)
    0000   0x95 0x10 0x0d 0x0b 0x0d                   .....
    body (0)

#### RECORD 65 CalBGForPH 2013-08-11T20:06:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-08-11T20:06:35)
    0000   0xa3 0x06 0x34 0x0b 0x0d                   ..4..
    body (0)

#### RECORD 66 CalBGForPH 2013-08-11T20:09:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-08-11T20:09:12)
    0000   0x8c 0x09 0x34 0x0b 0x0d                   ..4..
    body (0)

#### RECORD 67 BolusWizard 2013-08-11T20:10:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.9,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-08-11T20:10:14)
    0000   0x8e 0x0a 0x14 0x0b 0x0d                   .....
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0x00 0x31 0x00    @P.-j.1.
    0008   0x00 0x00 0x00 0x31 0x7d                   ...1}
    decimal
             64   80   13   45  106    0   49    0
              0    0    0   49  125

#### RECORD 68 Bolus 2013-08-11T20:10:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9, 'dual_component': '??', 'programmed': 4.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x31 0x31 0x00                        .11.
    decimal
              1   49   49    0
    datetime (2013-08-11T20:10:14)
    0000   0x8e 0x0a 0x54 0x0b 0x0d                   ..T..
    body (0)

#### RECORD 69 ResultTotals unknown head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x48                   ....H
    decimal
              7    0    0    4   72
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-2.data: 70 records`
