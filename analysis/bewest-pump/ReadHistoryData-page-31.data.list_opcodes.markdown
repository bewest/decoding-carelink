## START logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 1005, found 17 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x4a 0x5a                                  JZ
##### DEBUG DECIMAL
             74   90
#### RECORD 0 CalBGForPH 2013-02-22T21:00:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2013-02-22T21:00:31)
    0000   0x1f 0x80 0x35 0x16 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2013-02-22T21:56:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2013-02-22T21:56:58)
    0000   0x3a 0xb8 0x35 0x16 0x0d                   :.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2013-02-22T23:39:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2013-02-22T23:39:16)
    0000   0x10 0xa7 0x37 0x16 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 3 BolusWizard 2013-02-22T23:39:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 180,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb4                                  [.
    decimal
             91  180
    datetime (2013-02-22T23:39:19)
    0000   0x13 0xa7 0x17 0x16 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    3    0    9  125
    HOUR BITS: [1, 0, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 225, 'amount': 4.0, 'curve': 4},
 {'age': 209, 'amount': 2.75, 'curve': 20},
 {'age': 219, 'amount': 0.35, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa0 0xe1 0x04 0x6e 0xd1 0x14    \....n..
    0008   0x0e 0xdb 0x14                             ...
    decimal
             92   11  160  225    4  110  209   20
             14  219   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-02-22T23:39:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-02-22T23:39:19)
    0000   0x13 0xa7 0x57 0x16 0x0d                   ..W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 ResultTotals (2013, 0, 22, 13, 13, 54) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x58                   ....X
    decimal
              7    0    0    5   88
    datetime ((2013, 0, 22, 13, 13, 54))
    0000   0x36 0x0d 0x6d 0x36 0x0d                   6.m6.
    body (41)
    hex
    0000   0x05 0x00 0x99 0x5b 0xbc 0x09 0x00 0x00    ...[....
    0008   0x05 0x58 0x03 0x70 0x40 0x01 0xe8 0x24    .X.p@..$
    0010   0x00 0x80 0x01 0xe8 0x24 0x01 0x6c 0x4b    ....$.lK
    0018   0x00 0x7c 0x19 0x00 0x00 0x00 0x06 0x03    .|......
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  153   91  188    9    0    0
              5   88    3  112   64    1  232   36
              0  128    1  232   36    1  108   75
              0  124   25    0    0    0    6    3
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 7 CalBGForPH 2013-02-23T21:07:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2013-02-23T21:07:59)
    0000   0x3b 0x87 0x35 0x17 0x0d                   ;.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 BolusWizard 2013-02-23T21:08:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 3,
 '_byte[7]': 0,
 'bg': 139,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.3,
 'food_estimate': 2.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8b                                  [.
    decimal
             91  139
    datetime (2013-02-23T21:08:25)
    0000   0x19 0x88 0x15 0x17 0x0d                   .....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x03 0x1d 0x00    &P.-j...
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             38   80   13   45  106    3   29    0
              0    0    0   32  125
    HOUR BITS: [1, 0, 0]
#### RECORD 9 Bolus 2013-02-23T21:08:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-02-23T21:08:25)
    0000   0x19 0x88 0x55 0x17 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 BolusWizard 2013-02-23T21:41:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 16,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
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
    datetime (2013-02-23T21:41:11)
    0000   0x0b 0xa9 0x15 0x17 0x0d                   .....
    body (13)
    hex
    0000   0x10 0x50 0x0d 0x2d 0x6a 0x00 0x0c 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             16   80   13   45  106    0   12    0
              0    0    0   12  125
    HOUR BITS: [1, 0, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 3.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x80 0x25 0x04                   \..%.
    decimal
             92    5  128   37    4
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-02-23T21:41:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-02-23T21:41:11)
    0000   0x0b 0xa9 0x55 0x17 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 13 BolusWizard 2013-02-23T22:04:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.9,
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
    datetime (2013-02-23T22:04:21)
    0000   0x15 0x84 0x16 0x17 0x0d                   .....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125
    HOUR BITS: [1, 0, 0]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 1.2, 'curve': 4},
 {'age': 60, 'amount': 3.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x1e 0x04 0x80 0x3c 0x04    \.0...<.
    decimal
             92    8   48   30    4  128   60    4
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-02-23T22:04:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-02-23T22:04:21)
    0000   0x15 0x84 0x56 0x17 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 CalBGForPH 2013-02-23T22:42:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 229}
```
    op hex (2)
    0000   0x0a 0xe5                                  ..
    decimal
             10  229
    datetime (2013-02-23T22:42:13)
    0000   0x0d 0xaa 0x36 0x17 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 17 ResultTotals (2013, 0, 23, 13, 13, 55) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x58                   ....X
    decimal
              7    0    0    4   88
    datetime ((2013, 0, 23, 13, 13, 55))
    0000   0x37 0x0d 0x6d 0x37 0x0d                   7.m7.
    body (41)
    hex
    0000   0x05 0x00 0xb8 0x8b 0xe5 0x02 0x00 0x00    ........
    0008   0x04 0x58 0x03 0x84 0x51 0x00 0xd4 0x13    .X..Q...
    0010   0x00 0x42 0x00 0xd4 0x13 0x00 0xc8 0x5e    .B.....^
    0018   0x00 0x0c 0x06 0x00 0x00 0x00 0x03 0x02    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  184  139  229    2    0    0
              4   88    3  132   81    0  212   19
              0   66    0  212   19    0  200   94
              0   12    6    0    0    0    3    2
              0    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 18 CalBGForPH 2013-02-24T00:56:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 269}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2013-02-24T00:56:40)
    0000   0x28 0xb8 0x20 0x18 0x8d                   (. ..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 19 BolusWizard 2013-02-24T00:56:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 32,
 '_byte[7]': 0,
 'bg': 269,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0d                                  [.
    decimal
             91   13
    datetime (2013-02-24T00:56:47)
    0000   0x2f 0xb8 0x00 0x18 0x0d                   /....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x20 0x00 0x00    .Q.-j ..
    0008   0x00 0x06 0x00 0x1a 0x7d                   ....}
    decimal
              0   81   13   45  106   32    0    0
              0    6    0   26  125
    HOUR BITS: [1, 0, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 172, 'amount': 0.9, 'curve': 4},
 {'age': 202, 'amount': 1.2, 'curve': 4},
 {'age': 232, 'amount': 3.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x24 0xac 0x04 0x30 0xca 0x04    \.$..0..
    0008   0x80 0xe8 0x04                             ...
    decimal
             92   11   36  172    4   48  202    4
            128  232    4
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-02-24T00:56:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-02-24T00:56:47)
    0000   0x2f 0xb8 0x40 0x18 0x0d                   /.@..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 PumpSuspend 2013-02-24T09:33:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-24T09:33:33)
    0000   0x21 0xa1 0x09 0x18 0x0d                   !....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 23 PumpResume 2013-02-24T09:51:11 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-24T09:51:11)
    0000   0x0b 0xb3 0x09 0x18 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 24 CalBGForPH 2013-02-24T10:28:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 315}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2013-02-24T10:28:42)
    0000   0x2a 0x9c 0x2a 0x18 0x8d                   *.*..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 BolusWizard 2013-02-24T10:28:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 42,
 '_byte[7]': 0,
 'bg': 315,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
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
    0000   0x5b 0x3b                                  [;
    decimal
             91   59
    datetime (2013-02-24T10:28:52)
    0000   0x34 0x9c 0x0a 0x18 0x0d                   4....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2a 0x00 0x00    .Q.-j*..
    0008   0x00 0x00 0x00 0x2a 0x7d                   ...*}
    decimal
              0   81   13   45  106   42    0    0
              0    0    0   42  125
    HOUR BITS: [1, 0, 0]
#### RECORD 26 Bolus 2013-02-24T10:28:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-02-24T10:28:52)
    0000   0x34 0x9c 0x4a 0x18 0x0d                   4.J..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 27 CalBGForPH 2013-02-24T11:45:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2013-02-24T11:45:42)
    0000   0x2a 0xad 0x2b 0x18 0x0d                   *.+..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 28 BolusWizard 2013-02-24T11:48:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.1,
 'carb_input': 15,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.1,
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
    datetime (2013-02-24T11:48:41)
    0000   0x29 0xb0 0x0b 0x18 0x0d                   )....
    body (13)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0b 0x7d                   ....}
    decimal
             15   80   13   45  106    0   11    0
              0    0    0   11  125
    HOUR BITS: [1, 0, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 84, 'amount': 4.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0x54 0x04                   \..T.
    decimal
             92    5  168   84    4
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2013-02-24T11:48:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-02-24T11:48:41)
    0000   0x29 0xb0 0x4b 0x18 0x0d                   ).K..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 31 BolusWizard 2013-02-24T12:13:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.3,
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
    datetime (2013-02-24T12:13:01)
    0000   0x01 0x8d 0x0c 0x18 0x0d                   .....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x00 0x21 0x00    +P.-j.!.
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
             43   80   13   45  106    0   33    0
              0    0    0   33  125
    HOUR BITS: [1, 0, 0]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 1.1, 'curve': 4},
 {'age': 109, 'amount': 4.2, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x1d 0x04 0xa8 0x6d 0x04    \.,...m.
    decimal
             92    8   44   29    4  168  109    4
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-02-24T12:13:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-02-24T12:13:01)
    0000   0x01 0x8d 0x4c 0x18 0x0d                   ..L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 34 CalBGForPH 2013-02-24T12:29:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 223}
```
    op hex (2)
    0000   0x0a 0xdf                                  ..
    decimal
             10  223
    datetime (2013-02-24T12:29:13)
    0000   0x0d 0x9d 0x2c 0x18 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 CalBGForPH 2013-02-24T12:46:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 203}
```
    op hex (2)
    0000   0x0a 0xcb                                  ..
    decimal
             10  203
    datetime (2013-02-24T12:46:58)
    0000   0x3a 0xae 0x2c 0x18 0x0d                   :.,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 CalBGForPH 2013-02-24T20:04:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2013-02-24T20:04:45)
    0000   0x2d 0x84 0x34 0x18 0x0d                   -.4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 37 BolusWizard 2013-02-24T20:04:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 165,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa5                                  [.
    decimal
             91  165
    datetime (2013-02-24T20:04:47)
    0000   0x2f 0x84 0x14 0x18 0x0d                   /....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x08 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106    8    0    0
              0    0    0    8  125
    HOUR BITS: [1, 0, 0]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 214, 'amount': 1.85, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x4a 0xd6 0x14                   \.J..
    decimal
             92    5   74  214   20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-02-24T20:04:47 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-02-24T20:04:47)
    0000   0x2f 0x84 0x54 0x18 0x0d                   /.T..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 40 CalBGForPH 2013-02-24T20:59:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-02-24T20:59:01)
    0000   0x01 0xbb 0x34 0x18 0x0d                   ..4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 41 BolusWizard 2013-02-24T20:59:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-02-24T20:59:31)
    0000   0x1f 0xbb 0x14 0x18 0x0d                   .....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x01 0x21 0x00    +P.-j.!.
    0008   0x00 0x07 0x00 0x21 0x7d                   ...!}
    decimal
             43   80   13   45  106    1   33    0
              0    7    0   33  125
    HOUR BITS: [1, 0, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 0.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x20 0x37 0x04                   \. 7.
    decimal
             92    5   32   55    4
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-02-24T20:59:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-02-24T20:59:31)
    0000   0x1f 0xbb 0x54 0x18 0x0d                   ..T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 44 BolusWizard 2013-02-24T21:33:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 22,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.6,
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
    datetime (2013-02-24T21:33:41)
    0000   0x29 0xa1 0x15 0x18 0x0d                   )....
    body (13)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
             22   80   13   45  106    0   16    0
              0    0    0   16  125
    HOUR BITS: [1, 0, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 3.3, 'curve': 4},
 {'age': 89, 'amount': 0.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0x27 0x04 0x20 0x59 0x04    \..'. Y.
    decimal
             92    8  132   39    4   32   89    4
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-02-24T21:33:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-02-24T21:33:41)
    0000   0x29 0xa1 0x55 0x18 0x0d                   ).U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 47 CalBGForPH 2013-02-24T22:11:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2013-02-24T22:11:24)
    0000   0x18 0x8b 0x36 0x18 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 48 CalBGForPH 2013-02-24T22:47:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 178}
```
    op hex (2)
    0000   0x0a 0xb2                                  ..
    decimal
             10  178
    datetime (2013-02-24T22:47:06)
    0000   0x06 0xaf 0x36 0x18 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 CalBGForPH 2013-02-24T23:34:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 177}
```
    op hex (2)
    0000   0x0a 0xb1                                  ..
    decimal
             10  177
    datetime (2013-02-24T23:34:31)
    0000   0x1f 0xa2 0x37 0x18 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 50 ResultTotals (2013, 0, 24, 13, 13, 56) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x1c                   .....
    decimal
              7    0    0    6   28
    datetime ((2013, 0, 24, 13, 13, 56))
    0000   0x38 0x0d 0x6d 0x38 0x0d                   8.m8.
    body (41)
    hex
    0000   0x05 0x10 0xd0 0x82 0x3b 0x0a 0x00 0x00    ....;...
    0008   0x06 0x1c 0x03 0x78 0x39 0x02 0xa4 0x2b    ...x9..+
    0010   0x00 0x7b 0x02 0xa4 0x2b 0x01 0x74 0x37    .{..+.t7
    0018   0x01 0x30 0x2d 0x00 0x00 0x00 0x07 0x04    .0-.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  208  130   59   10    0    0
              6   28    3  120   57    2  164   43
              0  123    2  164   43    1  116   55
              1   48   45    0    0    0    7    4
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 0, 1]
#### RECORD 51 PumpSuspend 2013-02-25T12:13:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-02-25T12:13:29)
    0000   0x1d 0x8d 0x0c 0x19 0x0d                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 52 PumpResume 2013-02-25T12:29:45 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-02-25T12:29:45)
    0000   0x2d 0x9d 0x0c 0x19 0x0d                   -....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 CalBGForPH 2013-02-25T12:41:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 251}
```
    op hex (2)
    0000   0x0a 0xfb                                  ..
    decimal
             10  251
    datetime (2013-02-25T12:41:35)
    0000   0x23 0xa9 0x2c 0x19 0x0d                   #.,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 54 BolusWizard 2013-02-25T12:41:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 251,
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
    0000   0x5b 0xfb                                  [.
    decimal
             91  251
    datetime (2013-02-25T12:41:42)
    0000   0x2a 0xa9 0x0c 0x19 0x0d                   *....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    0    0   28  125
    HOUR BITS: [1, 0, 1]
#### RECORD 55 Bolus 2013-02-25T12:41:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-02-25T12:41:42)
    0000   0x2a 0xa9 0x4c 0x19 0x0d                   *.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 56 CalBGForPH 2013-02-25T13:06:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 233}
```
    op hex (2)
    0000   0x0a 0xe9                                  ..
    decimal
             10  233
    datetime (2013-02-25T13:06:29)
    0000   0x1d 0x86 0x2d 0x19 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 57 BolusWizard 2013-02-25T13:07:31 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 233,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe9                                  [.
    decimal
             91  233
    datetime (2013-02-25T13:07:31)
    0000   0x1f 0x87 0x0d 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0x18 0x21 0x00    ,P.-j.!.
    0008   0x00 0x1c 0x00 0x21 0x7d                   ...!}
    decimal
             44   80   13   45  106   24   33    0
              0   28    0   33  125
    HOUR BITS: [1, 0, 0]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 2.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0x21 0x04                   \.t!.
    decimal
             92    5  116   33    4
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-02-25T13:07:31 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-02-25T13:07:31)
    0000   0x1f 0x87 0x4d 0x19 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 60 BolusWizard 2013-02-25T13:13:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 13,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
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
    datetime (2013-02-25T13:13:51)
    0000   0x33 0x8d 0x0d 0x19 0x0d                   3....
    body (13)
    hex
    0000   0x0d 0x50 0x0d 0x2d 0x6a 0x00 0x0a 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
             13   80   13   45  106    0   10    0
              0    0    0   10  125
    HOUR BITS: [1, 0, 0]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 3.3, 'curve': 4}, {'age': 39, 'amount': 2.9, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0x09 0x04 0x74 0x27 0x04    \....t'.
    decimal
             92    8  132    9    4  116   39    4
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-02-25T13:13:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-02-25T13:13:51)
    0000   0x33 0x8d 0x4d 0x19 0x0d                   3.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 63 BolusWizard 2013-02-25T13:16:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 12,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.9,
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
    datetime (2013-02-25T13:16:23)
    0000   0x17 0x90 0x0d 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x0c 0x50 0x0d 0x2d 0x6a 0x00 0x09 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
             12   80   13   45  106    0    9    0
              0    0    0    9  125
    HOUR BITS: [1, 0, 0]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 0.75, 'curve': 4},
 {'age': 12, 'amount': 3.55, 'curve': 4},
 {'age': 42, 'amount': 2.9, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x1e 0x02 0x04 0x8e 0x0c 0x04    \.......
    0008   0x74 0x2a 0x04                             t*.
    decimal
             92   11   30    2    4  142   12    4
            116   42    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-02-25T13:16:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-02-25T13:16:23)
    0000   0x17 0x90 0x4d 0x19 0x0d                   ..M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 66 BolusWizard 2013-02-25T14:11:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 23,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.7,
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
    datetime (2013-02-25T14:11:01)
    0000   0x01 0x8b 0x0e 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x17 0x50 0x0d 0x2d 0x6a 0x00 0x11 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
             23   80   13   45  106    0   17    0
              0    0    0   17  125
    HOUR BITS: [1, 0, 0]
#### RECORD 67 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 57, 'amount': 1.65, 'curve': 4},
 {'age': 67, 'amount': 3.55, 'curve': 4},
 {'age': 97, 'amount': 2.9, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x42 0x39 0x04 0x8e 0x43 0x04    \.B9..C.
    0008   0x74 0x61 0x04                             ta.
    decimal
             92   11   66   57    4  142   67    4
            116   97    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2013-02-25T14:11:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-02-25T14:11:01)
    0000   0x01 0x8b 0x4e 0x19 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 CalBGForPH 2013-02-25T15:04:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2013-02-25T15:04:36)
    0000   0x24 0x84 0x2f 0x19 0x0d                   $./..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 70 CalBGForPH 2013-02-25T15:05:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2013-02-25T15:05:25)
    0000   0x19 0x85 0x2f 0x19 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 71 CalBGForPH 2013-02-25T15:57:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2013-02-25T15:57:02)
    0000   0x02 0xb9 0x2f 0x19 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 72 CalBGForPH 2013-02-25T16:10:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-02-25T16:10:02)
    0000   0x02 0x8a 0x30 0x19 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 73 CalBGForPH 2013-02-25T17:00:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-02-25T17:00:57)
    0000   0x39 0x80 0x31 0x19 0x0d                   9.1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 74 CalBGForPH 2013-02-25T17:02:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-02-25T17:02:11)
    0000   0x0b 0x82 0x31 0x19 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 75 BolusWizard 2013-02-25T17:02:37 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 103,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 17,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 1.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-02-25T17:02:37)
    0000   0x25 0x82 0x11 0x19 0x0d                   %....
    body (13)
    hex
    0000   0x11 0x50 0x0d 0x2d 0x6a 0xff 0x0d 0xf0    .P.-j...
    0008   0x00 0x06 0x00 0x0c 0x7d                   ....}
    decimal
             17   80   13   45  106  255   13  240
              0    6    0   12  125
    HOUR BITS: [1, 0, 0]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 178, 'amount': 1.7, 'curve': 4},
 {'age': 228, 'amount': 1.65, 'curve': 4},
 {'age': 238, 'amount': 3.55, 'curve': 4},
 {'age': 12, 'amount': 2.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x44 0xb2 0x04 0x42 0xe4 0x04    \.D..B..
    0008   0x8e 0xee 0x04 0x74 0x0c 0x14              ...t..
    decimal
             92   14   68  178    4   66  228    4
            142  238    4  116   12   20
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2013-02-25T17:02:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-02-25T17:02:37)
    0000   0x25 0x82 0x51 0x19 0x0d                   %.Q..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 78 CalBGForPH 2013-02-25T18:42:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-02-25T18:42:42)
    0000   0x2a 0xaa 0x32 0x19 0x0d                   *.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 BolusWizard 2013-02-25T18:43:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 156,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2013-02-25T18:43:03)
    0000   0x03 0xab 0x12 0x19 0x0d                   .....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x06 0x2a 0x00    7P.-j.*.
    0008   0x00 0x07 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    6   42    0
              0    7    0   42  125
    HOUR BITS: [1, 0, 1]
#### RECORD 80 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 1.2, 'curve': 4},
 {'age': 23, 'amount': 1.7, 'curve': 20},
 {'age': 73, 'amount': 1.65, 'curve': 20},
 {'age': 83, 'amount': 3.55, 'curve': 20},
 {'age': 113, 'amount': 2.9, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x30 0x6d 0x04 0x44 0x17 0x14    \.0m.D..
    0008   0x42 0x49 0x14 0x8e 0x53 0x14 0x74 0x71    BI..S.tq
    0010   0x14                                       .
    decimal
             92   17   48  109    4   68   23   20
             66   73   20  142   83   20  116  113
             20
    datetime (unknown)

    body (0)

#### RECORD 81 Bolus 2013-02-25T18:43:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-02-25T18:43:03)
    0000   0x03 0xab 0x52 0x19 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-31.data: 82 records`
