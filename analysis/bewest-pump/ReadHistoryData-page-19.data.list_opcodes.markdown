## START logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 1016, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xd7 0x5b                                  .[
##### DEBUG DECIMAL
            215   91
#### RECORD 0 BolusWizard 2013-04-02T19:19:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 42,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-04-02T19:19:28)
    0000   0x5c 0x13 0x13 0x02 0x0d                   \....
    body (13)
    hex
    0000   0x2a 0x50 0x0d 0x2d 0x6a 0x00 0x20 0x00    *P.-j. .
    0008   0x00 0x07 0x00 0x20 0x7d                   ... }
    decimal
             42   80   13   45  106    0   32    0
              0    7    0   32  125

#### RECORD 1 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 1.2, 'curve': 4},
 {'age': 135, 'amount': 0.2, 'curve': 4},
 {'age': 205, 'amount': 1.0, 'curve': 4},
 {'age': 255, 'amount': 1.0, 'curve': 4},
 {'age': 9, 'amount': 3.2, 'curve': 20},
 {'age': 19, 'amount': 0.15, 'curve': 20},
 {'age': 29, 'amount': 0.15, 'curve': 20},
 {'age': 79, 'amount': 3.6, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x30 0x7d 0x04 0x08 0x87 0x04    \.0}....
    0008   0x28 0xcd 0x04 0x28 0xff 0x04 0x80 0x09    (..(....
    0010   0x14 0x06 0x13 0x14 0x06 0x1d 0x14 0x90    ........
    0018   0x4f 0x14                                  O.
    decimal
             92   26   48  125    4    8  135    4
             40  205    4   40  255    4  128    9
             20    6   19   20    6   29   20  144
             79   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-04-02T19:19:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2013-04-02T19:19:28)
    0000   0x5c 0x13 0x53 0x02 0x0d                   \.S..
    body (0)

#### RECORD 3 CalBGForPH 2013-04-02T23:21:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2013-04-02T23:21:27)
    0000   0x5b 0x15 0x37 0x02 0x8d                   [.7..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 4 BolusWizard 2013-04-02T23:21:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 276,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x14                                  [.
    decimal
             91   20
    datetime (2013-04-02T23:21:29)
    0000   0x5d 0x15 0x17 0x02 0x0d                   ]....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125

#### RECORD 5 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 247, 'amount': 3.2, 'curve': 4},
 {'age': 111, 'amount': 1.2, 'curve': 20},
 {'age': 121, 'amount': 0.2, 'curve': 20},
 {'age': 191, 'amount': 1.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x80 0xf7 0x04 0x30 0x6f 0x14    \....0o.
    0008   0x08 0x79 0x14 0x28 0xbf 0x14              .y.(..
    decimal
             92   14  128  247    4   48  111   20
              8  121   20   40  191   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-04-02T23:21:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-04-02T23:21:29)
    0000   0x5d 0x15 0x57 0x02 0x0d                   ].W..
    body (0)

#### RECORD 7 ResultTotals 2013-04-02T13:13:02 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x80                   .....
    decimal
              7    0    0    5  128
    datetime (2013-04-02T13:13:02)
    0000   0x42 0x0d 0x6d 0x42 0x0d                   B.mB.
    body (41)
    hex
    0000   0x05 0x10 0xe3 0x6a 0x23 0x07 0x00 0x00    ...j#...
    0008   0x05 0x80 0x02 0xd8 0x34 0x02 0xa8 0x30    ....4..0
    0010   0x00 0x81 0x02 0xa8 0x30 0x01 0x88 0x3a    ....0..:
    0018   0x01 0x20 0x2a 0x00 0x00 0x00 0x08 0x05    . *.....
    0020   0x03 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  227  106   35    7    0    0
              5  128    2  216   52    2  168   48
              0  129    2  168   48    1  136   58
              1   32   42    0    0    0    8    5
              3    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 8 PumpSuspend 2013-04-03T14:15:06 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-03T14:15:06)
    0000   0x46 0x0f 0x0e 0x03 0x0d                   F....
    body (0)

#### RECORD 9 PumpResume 2013-04-03T14:38:57 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-03T14:38:57)
    0000   0x79 0x26 0x0e 0x03 0x0d                   y&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 10 CalBGForPH 2013-04-03T14:59:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-04-03T14:59:37)
    0000   0x65 0x3b 0x2e 0x03 0x0d                   e;...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 BolusWizard 2013-04-03T14:59:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.2,
 'carb_input': 29,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-04-03T14:59:43)
    0000   0x6b 0x3b 0x0e 0x03 0x0d                   k;...
    body (13)
    hex
    0000   0x1d 0x50 0x0d 0x2d 0x6a 0x00 0x16 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x16 0x7d                   ....}
    decimal
             29   80   13   45  106    0   22    0
              0    0    0   22  125
    HOUR BITS: [0, 0, 1]
#### RECORD 12 Bolus 2013-04-03T14:59:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'dual_component': '??', 'programmed': 2.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2013-04-03T14:59:43)
    0000   0x6b 0x3b 0x4e 0x03 0x0d                   k;N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 CalBGForPH 2013-04-03T15:32:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-04-03T15:32:57)
    0000   0x79 0x20 0x2f 0x03 0x0d                   y /..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 CalBGForPH 2013-04-03T15:47:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-04-03T15:47:21)
    0000   0x55 0x2f 0x2f 0x03 0x0d                   U//..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 BolusWizard 2013-04-03T15:47:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 41,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-04-03T15:47:42)
    0000   0x6a 0x2f 0x0f 0x03 0x0d                   j/...
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x00 0x1f 0x00    )P.-j...
    0008   0x00 0x13 0x00 0x1f 0x7d                   ....}
    decimal
             41   80   13   45  106    0   31    0
              0   19    0   31  125
    HOUR BITS: [0, 0, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 2.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x35 0x04                   \.X5.
    decimal
             92    5   88   53    4
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-04-03T15:47:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-04-03T15:47:42)
    0000   0x6a 0x2f 0x4f 0x03 0x0d                   j/O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 CalBGForPH 2013-04-03T16:56:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2013-04-03T16:56:16)
    0000   0x50 0x38 0x30 0x03 0x0d                   P80..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 19 CalBGForPH 2013-04-03T20:05:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 223}
```
    op hex (2)
    0000   0x0a 0xdf                                  ..
    decimal
             10  223
    datetime (2013-04-03T20:05:59)
    0000   0x7b 0x05 0x34 0x03 0x0d                   {.4..
    body (0)

#### RECORD 20 BolusWizard 2013-04-03T20:06:24 head[2], body[13] op[0x5b]
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
    datetime (2013-04-03T20:06:24)
    0000   0x58 0x06 0x14 0x03 0x0d                   X....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x15 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
              0   80   13   45  106   21    0    0
              0    0    0   21  125

#### RECORD 21 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 3.1, 'curve': 20},
 {'age': 56, 'amount': 2.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x7c 0x06 0x14 0x58 0x38 0x14    \.|..X8.
    decimal
             92    8  124    6   20   88   56   20
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2013-04-03T20:06:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'dual_component': '??', 'programmed': 1.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2013-04-03T20:06:24)
    0000   0x58 0x06 0x54 0x03 0x0d                   X.T..
    body (0)

#### RECORD 23 ResultTotals 2013-04-03T13:13:03 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x74                   ....t
    decimal
              7    0    0    4  116
    datetime (2013-04-03T13:13:03)
    0000   0x43 0x0d 0x6d 0x43 0x0d                   C.mC.
    body (41)
    hex
    0000   0x05 0x00 0x9b 0x6c 0xdf 0x05 0x00 0x00    ...l....
    0008   0x04 0x74 0x03 0x74 0x4e 0x01 0x00 0x16    .t.tN...
    0010   0x00 0x46 0x01 0x00 0x16 0x00 0xd4 0x53    .F.....S
    0018   0x00 0x2c 0x11 0x00 0x00 0x00 0x03 0x02    .,......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  155  108  223    5    0    0
              4  116    3  116   78    1    0   22
              0   70    1    0   22    0  212   83
              0   44   17    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 24 LowBattery 2013-04-04T09:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-04-04T09:01:00)
    0000   0x40 0x01 0x09 0x04 0x0d                   @....
    body (0)

#### RECORD 25 PumpSuspend 2013-04-04T10:39:46 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-04T10:39:46)
    0000   0x6e 0x27 0x0a 0x04 0x0d                   n'...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 PumpResume 2013-04-04T11:09:14 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-04T11:09:14)
    0000   0x4e 0x09 0x0b 0x04 0x0d                   N....
    body (0)

#### RECORD 27 Battery 2013-04-04T11:31:00 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-04-04T11:31:00)
    0000   0x40 0x1f 0x0b 0x04 0x0d                   @....
    body (0)

#### RECORD 28 Battery 2013-04-04T11:31:26 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-04-04T11:31:26)
    0000   0x5a 0x1f 0x0b 0x04 0x0d                   Z....
    body (0)

#### RECORD 29 CalBGForPH 2013-04-04T11:38:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 203}
```
    op hex (2)
    0000   0x0a 0xcb                                  ..
    decimal
             10  203
    datetime (2013-04-04T11:38:07)
    0000   0x47 0x26 0x2b 0x04 0x0d                   G&+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 BolusWizard 2013-04-04T11:38:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 17,
 '_byte[7]': 0,
 'bg': 203,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcb                                  [.
    decimal
             91  203
    datetime (2013-04-04T11:38:12)
    0000   0x4c 0x26 0x0b 0x04 0x0d                   L&...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x11 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x11 0x7d                   ....}
    decimal
              0   80   13   45  106   17    0    0
              0    0    0   17  125
    HOUR BITS: [0, 0, 1]
#### RECORD 31 Bolus 2013-04-04T11:38:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-04-04T11:38:12)
    0000   0x4c 0x26 0x4b 0x04 0x0d                   L&K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 32 BolusWizard 2013-04-04T11:52:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 6,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.4,
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
    datetime (2013-04-04T11:52:56)
    0000   0x78 0x34 0x0b 0x04 0x0d                   x4...
    body (13)
    hex
    0000   0x06 0x50 0x0d 0x2d 0x6a 0x00 0x04 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x04 0x7d                   ....}
    decimal
              6   80   13   45  106    0    4    0
              0    0    0    4  125
    HOUR BITS: [0, 0, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 1.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0x12 0x04                   \.D..
    decimal
             92    5   68   18    4
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-04-04T11:52:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'dual_component': '??', 'programmed': 0.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2013-04-04T11:52:57)
    0000   0x79 0x34 0x4b 0x04 0x0d                   y4K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 CalBGForPH 2013-04-04T12:40:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-04-04T12:40:12)
    0000   0x4c 0x28 0x2c 0x04 0x0d                   L(,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 CalBGForPH 2013-04-04T12:40:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-04-04T12:40:24)
    0000   0x58 0x28 0x2c 0x04 0x0d                   X(,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 BolusWizard 2013-04-04T12:40:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 172,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xac                                  [.
    decimal
             91  172
    datetime (2013-04-04T12:40:36)
    0000   0x64 0x28 0x0c 0x04 0x0d                   d(...
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0x0a 0x2c 0x00    :P.-j.,.
    0008   0x00 0x11 0x00 0x2c 0x7d                   ...,}
    decimal
             58   80   13   45  106   10   44    0
              0   17    0   44  125
    HOUR BITS: [0, 0, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 0.4, 'curve': 4},
 {'age': 66, 'amount': 1.7, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x38 0x04 0x44 0x42 0x04    \..8.DB.
    decimal
             92    8   16   56    4   68   66    4
    datetime (unknown)

    body (0)

#### RECORD 39 LowReservoir 2013-04-04T12:41:12 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-04-04T12:41:12)
    0000   0x4c 0x29 0x0c 0x04 0x0d                   L)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 Bolus 2013-04-04T12:40:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-04-04T12:40:36)
    0000   0x64 0x28 0x4c 0x04 0x0d                   d(L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 LowReservoir 2013-04-04T19:18:56 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-04-04T19:18:56)
    0000   0x78 0x12 0x13 0x04 0x0d                   x....
    body (0)

#### RECORD 42 CalBGForPH 2013-04-04T22:08:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2013-04-04T22:08:11)
    0000   0x4b 0x08 0x36 0x04 0x0d                   K.6..
    body (0)

#### RECORD 43 BolusWizard 2013-04-04T22:08:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 82,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.2,
 'carb_input': 76,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 5.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x52                                  [R
    decimal
             91   82
    datetime (2013-04-04T22:08:25)
    0000   0x59 0x08 0x16 0x04 0x0d                   Y....
    body (13)
    hex
    0000   0x4c 0x50 0x0d 0x2d 0x6a 0xfa 0x3a 0xf0    LP.-j.:.
    0008   0x00 0x00 0x00 0x34 0x7d                   ...4}
    decimal
             76   80   13   45  106  250   58  240
              0    0    0   52  125

#### RECORD 44 Bolus 2013-04-04T22:08:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x34 0x34 0x00                        .44.
    decimal
              1   52   52    0
    datetime (2013-04-04T22:08:25)
    0000   0x59 0x08 0x56 0x04 0x0d                   Y.V..
    body (0)

#### RECORD 45 ResultTotals 2013-04-04T13:13:04 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x42                   ....B
    decimal
              7    0    0    5   66
    datetime (2013-04-04T13:13:04)
    0000   0x44 0x0d 0x6d 0x44 0x0d                   D.mD.
    body (41)
    hex
    0000   0x05 0x00 0x8e 0x52 0xcb 0x04 0x00 0x00    ...R....
    0008   0x05 0x42 0x03 0x6e 0x41 0x01 0xd4 0x23    .B.nA..#
    0010   0x00 0x8c 0x01 0xd4 0x23 0x01 0x90 0x55    ....#..U
    0018   0x00 0x44 0x0f 0x00 0x00 0x00 0x04 0x03    .D......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  142   82  203    4    0    0
              5   66    3  110   65    1  212   35
              0  140    1  212   35    1  144   85
              0   68   15    0    0    0    4    3
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 46 CalBGForPH 2013-04-05T00:39:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2013-04-05T00:39:35)
    0000   0x63 0x27 0x20 0x05 0x0d                   c' ..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 47 PumpSuspend 2013-04-05T13:33:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-05T13:33:19)
    0000   0x53 0x21 0x0d 0x05 0x0d                   S!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 PumpResume 2013-04-05T13:50:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-05T13:50:31)
    0000   0x5f 0x32 0x0d 0x05 0x0d                   _2...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 CalBGForPH 2013-04-05T14:38:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2013-04-05T14:38:59)
    0000   0x7b 0x26 0x2e 0x05 0x0d                   {&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 BolusWizard 2013-04-05T14:39:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 153,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2013-04-05T14:39:51)
    0000   0x73 0x27 0x0e 0x05 0x0d                   s'...
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x06 0x27 0x00    3P.-j.'.
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
             51   80   13   45  106    6   39    0
              0    0    0   45  125
    HOUR BITS: [0, 0, 1]
#### RECORD 51 Bolus 2013-04-05T14:39:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-04-05T14:39:51)
    0000   0x73 0x27 0x4e 0x05 0x0d                   s'N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 52 BolusWizard 2013-04-05T15:44:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.1,
 'carb_input': 28,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.1,
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
    datetime (2013-04-05T15:44:07)
    0000   0x47 0x2c 0x0f 0x05 0x0d                   G,...
    body (13)
    hex
    0000   0x1c 0x50 0x0d 0x2d 0x6a 0x00 0x15 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x15 0x7d                   ....}
    decimal
             28   80   13   45  106    0   21    0
              0    0    0   21  125
    HOUR BITS: [0, 0, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 70, 'amount': 4.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0x46 0x04                   \..F.
    decimal
             92    5  180   70    4
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-04-05T15:44:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'dual_component': '??', 'programmed': 2.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2013-04-05T15:44:07)
    0000   0x47 0x2c 0x4f 0x05 0x0d                   G,O..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 NoDelivery 2013-04-05T16:09:28 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xff                        ....
    decimal
              6    4   11  255
    datetime (2013-04-05T16:09:28)
    0000   0x5c 0x09 0x50 0x45 0x0d                   \.PE.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 56 ClearAlarm 2013-04-05T16:10:06 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2013-04-05T16:10:06)
    0000   0x46 0x0a 0x10 0x05 0x0d                   F....
    body (0)

#### RECORD 57 Rewind 2013-04-05T16:21:32 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-04-05T16:21:32)
    0000   0x60 0x15 0x10 0x05 0x0d                   `....
    body (0)

#### RECORD 58 Prime 2013-04-05T16:23:43 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x15                   .....
    decimal
              3    0    0    0   21
    datetime (2013-04-05T16:23:43)
    0000   0x6b 0x17 0x30 0x05 0x0d                   k.0..
    body (0)

#### RECORD 59 Prime 2013-04-05T16:24:01 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-05T16:24:01)
    0000   0x41 0x18 0x10 0x05 0x0d                   A....
    body (0)

#### RECORD 60 CalBGForPH 2013-04-05T16:56:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 187}
```
    op hex (2)
    0000   0x0a 0xbb                                  ..
    decimal
             10  187
    datetime (2013-04-05T16:56:37)
    0000   0x65 0x38 0x30 0x05 0x0d                   e80..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 CalBGForPH 2013-04-05T18:16:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 347}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-04-05T18:16:06)
    0000   0x46 0x10 0x32 0x05 0x8d                   F.2..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 BolusWizard 2013-04-05T18:16:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 49,
 '_byte[7]': 0,
 'bg': 347,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5b                                  [[
    decimal
             91   91
    datetime (2013-04-05T18:16:17)
    0000   0x51 0x10 0x12 0x05 0x0d                   Q....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x31 0x00 0x00    .Q.-j1..
    0008   0x00 0x0a 0x00 0x27 0x7d                   ...'}
    decimal
              0   81   13   45  106   49    0    0
              0   10    0   39  125

#### RECORD 63 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 2.1, 'curve': 4},
 {'age': 222, 'amount': 4.5, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x54 0x98 0x04 0xb4 0xde 0x04    \.T.....
    decimal
             92    8   84  152    4  180  222    4
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2013-04-05T18:16:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-04-05T18:16:17)
    0000   0x51 0x10 0x52 0x05 0x0d                   Q.R..
    body (0)

#### RECORD 65 BolusWizard 2013-04-05T19:01:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
 'carb_input': 40,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.0,
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
    datetime (2013-04-05T19:01:50)
    0000   0x72 0x01 0x13 0x05 0x0d                   r....
    body (13)
    hex
    0000   0x28 0x50 0x0d 0x2d 0x6a 0x00 0x1e 0x00    (P.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
             40   80   13   45  106    0   30    0
              0    0    0   30  125

#### RECORD 66 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 4.2, 'curve': 4},
 {'age': 197, 'amount': 2.1, 'curve': 4},
 {'age': 11, 'amount': 4.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa8 0x2f 0x04 0x54 0xc5 0x04    \../.T..
    0008   0xb4 0x0b 0x14                             ...
    decimal
             92   11  168   47    4   84  197    4
            180   11   20
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-04-05T19:01:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-04-05T19:01:50)
    0000   0x72 0x01 0x53 0x05 0x0d                   r.S..
    body (0)

#### RECORD 68 ResultTotals 2013-04-05T13:13:05 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x96                   .....
    decimal
              7    0    0    5  150
    datetime (2013-04-05T13:13:05)
    0000   0x45 0x0d 0x6d 0x45 0x0d                   E.mE.
    body (41)
    hex
    0000   0x05 0x10 0xc3 0x5d 0x5b 0x04 0x00 0x00    ...][...
    0008   0x05 0x96 0x03 0x6e 0x3d 0x02 0x28 0x27    ...n=.('
    0010   0x00 0x77 0x02 0x28 0x27 0x01 0x68 0x41    .w.('.hA
    0018   0x00 0xc0 0x23 0x00 0x00 0x00 0x04 0x02    ..#.....
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  195   93   91    4    0    0
              5  150    3  110   61    2   40   39
              0  119    2   40   39    1  104   65
              0  192   35    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    DAY BITS: [0, 1, 0]
#### RECORD 69 CalBGForPH 2013-04-06T00:26:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2013-04-06T00:26:30)
    0000   0x5e 0x1a 0x20 0x06 0x0d                   ^. ..
    body (0)

#### RECORD 70 CalBGForPH 2013-04-06T20:31:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2013-04-06T20:31:54)
    0000   0x76 0x1f 0x34 0x06 0x8d                   v.4..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 71 BolusWizard 2013-04-06T20:32:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 276,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x14                                  [.
    decimal
             91   20
    datetime (2013-04-06T20:32:01)
    0000   0x41 0x20 0x14 0x06 0x0d                   A ...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125
    HOUR BITS: [0, 0, 1]
#### RECORD 72 Bolus 2013-04-06T20:32:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-04-06T20:32:01)
    0000   0x41 0x20 0x54 0x06 0x0d                   A T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 73 CalBGForPH 2013-04-06T21:30:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 280}
```
    op hex (2)
    0000   0x0a 0x18                                  ..
    decimal
             10   24
    datetime (2013-04-06T21:30:11)
    0000   0x4b 0x1e 0x35 0x06 0x8d                   K.5..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 74 BolusWizard 2013-04-06T21:30:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 34,
 '_byte[7]': 0,
 'bg': 280,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x18                                  [.
    decimal
             91   24
    datetime (2013-04-06T21:30:19)
    0000   0x53 0x1e 0x15 0x06 0x0d                   S....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x22 0x00 0x00    .Q.-j"..
    0008   0x00 0x1b 0x00 0x07 0x7d                   ....}
    decimal
              0   81   13   45  106   34    0    0
              0   27    0    7  125

#### RECORD 75 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 0.4, 'curve': 4},
 {'age': 66, 'amount': 3.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x38 0x04 0x78 0x42 0x04    \..8.xB.
    decimal
             92    8   16   56    4  120   66    4
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2013-04-06T21:30:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-04-06T21:30:20)
    0000   0x54 0x1e 0x55 0x06 0x0d                   T.U..
    body (0)

#### RECORD 77 CalBGForPH 2013-04-06T21:36:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 258}
```
    op hex (2)
    0000   0x0a 0x02                                  ..
    decimal
             10    2
    datetime (2013-04-06T21:36:29)
    0000   0x5d 0x24 0x35 0x06 0x8d                   ]$5..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 78 BolusWizard 2013-04-06T21:36:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 29,
 '_byte[7]': 0,
 'bg': 258,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x02                                  [.
    decimal
             91    2
    datetime (2013-04-06T21:36:51)
    0000   0x73 0x24 0x15 0x06 0x0d                   s$...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1d 0x00 0x00    .Q.-j...
    0008   0x00 0x24 0x00 0x00 0x7d                   .$..}
    decimal
              0   81   13   45  106   29    0    0
              0   36    0    0  125
    HOUR BITS: [0, 0, 1]
#### RECORD 79 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 1.0, 'curve': 4},
 {'age': 62, 'amount': 0.4, 'curve': 4},
 {'age': 72, 'amount': 3.0, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x0c 0x04 0x10 0x3e 0x04    \.(...>.
    0008   0x78 0x48 0x04                             xH.
    decimal
             92   11   40   12    4   16   62    4
            120   72    4
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-19.data: 80 records`
