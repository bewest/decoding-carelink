## START logs/ReadHistoryData-page-20.data
#### STOPPING DOUBLE NULLS @ 837, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0xa4 0x03 0x70 0x4a 0x01 0x34 0x1a    ...pJ.4.
    0008   0x00 0x40 0x01 0x34 0x1a 0x00 0xa8 0x37    .@.4...7
    0010   0x00 0x8c 0x2d 0x00 0x00 0x00 0x03 0x02    ..-.....
    0018   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
##### DEBUG DECIMAL
              4  164    3  112   74    1   52   26
              0   64    1   52   26    0  168   55
              0  140   45    0    0    0    3    2
              1    0    0   12    0  232    0    0
#### RECORD 0 BolusWizard 2013-05-07T05:29:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 50,
 '_byte[7]': 0,
 'bg': 352,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2013-05-07T05:29:54)
    0000   0x76 0x5d 0x05 0x07 0x0d                   v]...
    body (15)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x32 0x00 0x00    .Q.-j2..
    0008   0x00 0x00 0x00 0x32 0x7d 0x01 0x32         ...2}.2
    decimal
              0   81   13   45  106   50    0    0
              0    0    0   50  125    1   50
    HOUR BITS: [0, 1, 0]
#### RECORD 1 Base (2013, 5, 7, 5, 29, 54) head[2], body[0] op[0x32]

    op hex (2)
    0000   0x32 0x00                                  2.
    decimal
             50    0
    datetime ((2013, 5, 7, 5, 29, 54))
    0000   0x76 0x5d 0x45 0x07 0x0d                   v]E..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 2 PumpSuspend 2013-05-07T13:48:50 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-07T13:48:50)
    0000   0x72 0x70 0x0d 0x07 0x0d                   rp...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 PumpResume 2013-05-07T14:05:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-07T14:05:35)
    0000   0x63 0x45 0x0e 0x07 0x0d                   cE...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 CalBGForPH 2013-05-07T14:28:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-05-07T14:28:02)
    0000   0x42 0x5c 0x2e 0x07 0x0d                   B\...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 5 BolusWizard 2013-05-07T14:28:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 199,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
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
    0000   0x5b 0xc7                                  [.
    decimal
             91  199
    datetime (2013-05-07T14:28:04)
    0000   0x44 0x5c 0x0e 0x07 0x0d                   D\...
    body (15)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d 0x01 0x10         ....}..
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125    1   16
    HOUR BITS: [0, 1, 0]
#### RECORD 6 Base (2013, 5, 7, 14, 28, 4) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2013, 5, 7, 14, 28, 4))
    0000   0x44 0x5c 0x4e 0x07 0x0d                   D\N..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-05-07T15:05:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-05-07T15:05:49)
    0000   0x71 0x45 0x2f 0x07 0x0d                   qE/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 8 BolusWizard 2013-05-07T15:06:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-05-07T15:06:10)
    0000   0x4a 0x46 0x0f 0x07 0x0d                   JF...
    body (15)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x0a 0x27 0x00    3P.-j.'.
    0008   0x00 0x0f 0x00 0x27 0x7d 0x5c 0x05         ...'}\.
    decimal
             51   80   13   45  106   10   39    0
              0   15    0   39  125   92    5
    HOUR BITS: [0, 1, 0]
#### RECORD 9 Base (2000, 0, 7, 7, 1, 4) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x2a                                  @*
    decimal
             64   42
    datetime ((2000, 0, 7, 7, 1, 4))
    0000   0x04 0x01 0x27 0x27 0x00                   ..''.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 10 Base (2011, 4, 10, 13, 7, 15) head[2], body[0] op[0x4a]

    op hex (2)
    0000   0x4a 0x46                                  JF
    decimal
             74   70
    datetime ((2011, 4, 10, 13, 7, 15))
    0000   0x4f 0x07 0x0d 0x0a 0x2b                   O...+
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 11 Base (2011, 0, 27, 13, 7, 48) head[2], body[0] op[0x51]

    op hex (2)
    0000   0x51 0x5e                                  Q^
    decimal
             81   94
    datetime ((2011, 0, 27, 13, 7, 48))
    0000   0x30 0x07 0x8d 0x5b 0x2b                   0..[+
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 12 Base (2001, 0, 0, 13, 7, 16) head[2], body[0] op[0x55]

    op hex (2)
    0000   0x55 0x5e                                  U^
    decimal
             85   94
    datetime ((2001, 0, 0, 13, 7, 16))
    0000   0x10 0x07 0x0d 0x00 0x51                   ....Q
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 13 Base (2000, 4, 0, 0, 38, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 38, 42))
    0000   0x6a 0x26 0x00 0x00 0x00                   j&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 14 Rewind (2012, 1, 8, 28, 61, 5) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime ((2012, 1, 8, 28, 61, 5))
    0000   0x05 0x7d 0x5c 0x08 0x9c                   .}\..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 15 Base (2008, 5, 1, 4, 62, 0) head[2], body[0] op[0x56]

    op hex (2)
    0000   0x56 0x04                                  V.
    decimal
             86    4
    datetime ((2008, 5, 1, 4, 62, 0))
    0000   0x40 0x7e 0x04 0x01 0x08                   @~...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 16 ChangeBasalProfile 2013-05-07T16:30:21 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x00                                  ..
    decimal
              8    0
    datetime (2013-05-07T16:30:21)
    0000   0x55 0x5e 0x50 0x07 0x0d                   U^P..
    body (44)
    hex
    0000   0x0a 0x5c 0x5a 0x57 0x37 0x07 0x0d 0x5b    .\ZW7..[
    0008   0x5c 0x7a 0x57 0x17 0x07 0x0d 0x3d 0x50    \zW...=P
    0010   0x0d 0x2d 0x6a 0xfd 0x2e 0xf0 0x00 0x00    .-j.....
    0018   0x00 0x2b 0x7d 0x5c 0x05 0x20 0xa3 0x14    .+}\. ..
    0020   0x01 0x2b 0x2b 0x00 0x7a 0x57 0x57 0x07    .++.zWW.
    0028   0x0d 0x07 0x00 0x00                        ....
    decimal
             10   92   90   87   55    7   13   91
             92  122   87   23    7   13   61   80
             13   45  106  253   46  240    0    0
              0   43  125   92    5   32  163   20
              1   43   43    0  122   87   87    7
             13    7    0    0
    HOUR BITS: [0, 1, 0]
#### RECORD 17 Base (2013, 6, 7, 13, 13, 7) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0xe8                                  ..
    decimal
              5  232
    datetime ((2013, 6, 7, 13, 13, 7))
    0000   0x47 0x8d 0x6d 0x47 0x8d                   G.mG.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 Base (2000, 13, 5, 0, 28, 31) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x10                                  ..
    decimal
              5   16
    datetime ((2000, 13, 5, 0, 28, 31))
    0000   0xdf 0x5c 0x60 0x05 0x00                   .\`..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 19 Base (2002, 12, 27, 24, 3, 40) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2002, 12, 27, 24, 3, 40))
    0000   0xe8 0x03 0x78 0x3b 0x02                   ..x;.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 20 Base (2009, 1, 16, 2, 48, 0) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x29                                  p)
    decimal
            112   41
    datetime ((2009, 1, 16, 2, 48, 0))
    0000   0x00 0x70 0x02 0x70 0x29                   .p.p)
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 21 Bolus (2000, 0, 3, 2, 5, 0) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.2, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x48 0x35 0x01 0x28 0x2f 0x00 0x00    .H5.(/..
    decimal
              1   72   53    1   40   47    0    0
    datetime ((2000, 0, 3, 2, 5, 0))
    0000   0x00 0x05 0x02 0x03 0x00                   .....
    body (0)

#### RECORD 22 Base (2000, 3, 0, 0, 40, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0c                                  ..
    decimal
              0   12
    datetime ((2000, 3, 0, 0, 40, 0))
    0000   0x00 0xe8 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 23 LowReservoir 2013-05-08T10:54:32 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-05-08T10:54:32)
    0000   0x60 0x76 0x0a 0x08 0x0d                   `v...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 24 PumpSuspend 2013-05-08T12:40:26 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-08T12:40:26)
    0000   0x5a 0x68 0x0c 0x08 0x0d                   Zh...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 25 PumpResume 2013-05-08T13:02:01 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-08T13:02:01)
    0000   0x41 0x42 0x0d 0x08 0x0d                   AB...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 26 CalBGForPH 2013-05-08T13:24:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-05-08T13:24:27)
    0000   0x5b 0x58 0x2d 0x08 0x0d                   [X-..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 27 BolusWizard 2013-05-08T13:24:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2013-05-08T13:24:43)
    0000   0x6b 0x58 0x0d 0x08 0x0d                   kX...
    body (15)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x08 0x26 0x00    2P.-j.&.
    0008   0x00 0x00 0x00 0x2e 0x7d 0x01 0x2e         ....}..
    decimal
             50   80   13   45  106    8   38    0
              0    0    0   46  125    1   46
    HOUR BITS: [0, 1, 0]
#### RECORD 28 Base (2013, 5, 8, 13, 24, 43) head[2], body[0] op[0x2e]

    op hex (2)
    0000   0x2e 0x00                                  ..
    decimal
             46    0
    datetime ((2013, 5, 8, 13, 24, 43))
    0000   0x6b 0x58 0x4d 0x08 0x0d                   kXM..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 29 BolusWizard 2013-05-08T13:52:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 21,
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
    datetime (2013-05-08T13:52:41)
    0000   0x69 0x74 0x0d 0x08 0x0d                   it...
    body (15)
    hex
    0000   0x15 0x50 0x0d 0x2d 0x6a 0x00 0x10 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d 0x5c 0x05         ....}\.
    decimal
             21   80   13   45  106    0   16    0
              0    0    0   16  125   92    5
    HOUR BITS: [0, 1, 1]
#### RECORD 30 Base (2000, 0, 16, 16, 1, 4) head[2], body[0] op[0xb8]

    op hex (2)
    0000   0xb8 0x1c                                  ..
    decimal
            184   28
    datetime ((2000, 0, 16, 16, 1, 4))
    0000   0x04 0x01 0x10 0x10 0x00                   .....
    body (0)

#### RECORD 31 Ian69 2004-04-20T13:08:13 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x74                                  it
    decimal
            105  116
    datetime (2004-04-20T13:08:13)
    0000   0x4d 0x08 0x0d 0x34 0x64                   M..4d
    body (2)
    hex
    0000   0x5f 0x72                                  _r
    decimal
             95  114
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 32 Base (2014, 0, 8, 0, 30, 13) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x08                                  ..
    decimal
             14    8
    datetime ((2014, 0, 8, 0, 30, 13))
    0000   0x0d 0x1e 0x00 0x48 0x5e                   ...H^
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 33 Base (2015, 0, 21, 0, 31, 13) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x48                                  .H
    decimal
             15   72
    datetime ((2015, 0, 21, 0, 31, 13))
    0000   0x0d 0x1f 0x00 0x55 0x5f                   ...U_
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 34 Base (2000, 0, 29, 0, 30, 13) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x48                                  .H
    decimal
             15   72
    datetime ((2000, 0, 29, 0, 30, 13))
    0000   0x0d 0x1e 0x00 0x5d 0x60                   ...]`
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 35 Base (2005, 0, 23, 0, 31, 13) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x48                                  .H
    decimal
             15   72
    datetime ((2005, 0, 23, 0, 31, 13))
    0000   0x0d 0x1f 0x00 0x77 0x65                   ...we
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 36 Base (2005, 0, 25, 0, 30, 13) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x48                                  .H
    decimal
             15   72
    datetime ((2005, 0, 25, 0, 30, 13))
    0000   0x0d 0x1e 0x00 0x79 0x65                   ...ye
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 37 Base (2008, 0, 22, 0, 31, 13) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x48                                  .H
    decimal
             15   72
    datetime ((2008, 0, 22, 0, 31, 13))
    0000   0x0d 0x1f 0x00 0x56 0x68                   ...Vh
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 38 Base (2003, 0, 20, 21, 10, 13) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x48                                  .H
    decimal
             15   72
    datetime ((2003, 0, 20, 21, 10, 13))
    0000   0x0d 0x0a 0x55 0x54 0x43                   ..UTC
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 39 Base (2015, 0, 21, 21, 10, 13) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x08                                  0.
    decimal
             48    8
    datetime ((2015, 0, 21, 21, 10, 13))
    0000   0x0d 0x0a 0x55 0x55 0x4f                   ..UUO
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 40 Base (2015, 1, 11, 21, 27, 13) head[2], body[0] op[0x30]

    op hex (2)
    0000   0x30 0x08                                  0.
    decimal
             48    8
    datetime ((2015, 1, 11, 21, 27, 13))
    0000   0x0d 0x5b 0x55 0x6b 0x4f                   .[UkO
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 41 Base (2013, 0, 13, 16, 21, 13) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x08                                  ..
    decimal
             16    8
    datetime ((2013, 0, 13, 16, 21, 13))
    0000   0x0d 0x15 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 42 Base (2000, 3, 14, 0, 48, 16) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xfb                                  j.
    decimal
            106  251
    datetime ((2000, 3, 14, 0, 48, 16))
    0000   0x10 0xf0 0x00 0x0e 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 43 Ian0B 2008-01-04T23:00:08 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x7d 0x5c                             .}\
    decimal
             11  125   92
    datetime (2008-01-04T23:00:08)
    0000   0x08 0x40 0x97 0x04 0xb8                   .@...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 44 Base (2011, 0, 0, 11, 11, 1) head[2], body[0] op[0xab]

    op hex (2)
    0000   0xab 0x04                                  ..
    decimal
            171    4
    datetime ((2011, 0, 0, 11, 11, 1))
    0000   0x01 0x0b 0x0b 0x00 0x6b                   ....k
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 45 Base (2000, 0, 0, 25, 13, 8) head[2], body[0] op[0x4f]

    op hex (2)
    0000   0x4f 0x50                                  OP
    decimal
             79   80
    datetime ((2000, 0, 0, 25, 13, 8))
    0000   0x08 0x0d 0x19 0x00 0x40                   ....@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 46 Base (2010, 0, 0, 26, 13, 8) head[2], body[0] op[0x41]

    op hex (2)
    0000   0x41 0x13                                  A.
    decimal
             65   19
    datetime ((2010, 0, 0, 26, 13, 8))
    0000   0x08 0x0d 0x1a 0x00 0x4a                   ....J
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 47 Base (2001, 0, 1, 26, 13, 8) head[2], body[0] op[0x45]

    op hex (2)
    0000   0x45 0x15                                  E.
    decimal
             69   21
    datetime ((2001, 0, 1, 26, 13, 8))
    0000   0x08 0x0d 0x1a 0x01 0x61                   ....a
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 48 Base (2007, 0, 23, 6, 13, 8) head[2], body[0] op[0x45]

    op hex (2)
    0000   0x45 0x15                                  E.
    decimal
             69   21
    datetime ((2007, 0, 23, 6, 13, 8))
    0000   0x08 0x0d 0x06 0x37 0x07                   ...7.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 49 Base (2010, 5, 13, 8, 21, 5) head[2], body[0] op[0x94]

    op hex (2)
    0000   0x94 0x4a                                  .J
    decimal
            148   74
    datetime ((2010, 5, 13, 8, 21, 5))
    0000   0x45 0x55 0xa8 0x0d 0x1a                   EU...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 50 Base (2012, 4, 13, 8, 21, 5) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x73                                  .s
    decimal
              0  115
    datetime ((2012, 4, 13, 8, 21, 5))
    0000   0x45 0x15 0x08 0x0d 0x0c                   E....
    body (0)

#### RECORD 51 Base (2010, 4, 13, 8, 21, 5) head[2], body[0] op[0x37]

    op hex (2)
    0000   0x37 0x73                                  7s
    decimal
             55  115
    datetime ((2010, 4, 13, 8, 21, 5))
    0000   0x45 0x15 0x08 0x0d 0x1a                   E....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 52 Bolus 2013-05-08T21:06:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 7.9, 'dual_component': '??', 'programmed': 7.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x4f 0x46 0x15 0x08 0x0d 0x34 0x1f    .OF...4.
    decimal
              1   79   70   21    8   13   52   31
    datetime (2013-05-08T21:06:16)
    0000   0x50 0x46 0x15 0x08 0x0d                   PF...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 53 Rewind 2013-05-08T21:09:24 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-05-08T21:09:24)
    0000   0x58 0x49 0x15 0x08 0x0d                   XI...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 54 Prime 2013-05-08T21:10:00 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1e                   .....
    decimal
              3    0    0    0   30
    datetime (2013-05-08T21:10:00)
    0000   0x40 0x4a 0x35 0x08 0x0d                   @J5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 55 Prime 2013-05-08T21:10:25 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-05-08T21:10:25)
    0000   0x59 0x4a 0x15 0x08 0x0d                   YJ...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 56 CalBGForPH 2013-05-08T21:13:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-05-08T21:13:10)
    0000   0x4a 0x4d 0x35 0x08 0x0d                   JM5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 57 BolusWizard 2013-05-08T21:13:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 156,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
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
    0000   0x5b 0x9c                                  [.
    decimal
             91  156
    datetime (2013-05-08T21:13:15)
    0000   0x4f 0x4d 0x15 0x08 0x0d                   OM...
    body (15)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d 0x5c 0x0b         ....}\.
    decimal
              0   80   13   45  106    6    0    0
              0    0    0    6  125   92   11
    HOUR BITS: [0, 1, 0]
#### RECORD 58 Base (2008, 1, 20, 1, 0, 20) head[2], body[0] op[0x2c]

    op hex (2)
    0000   0x2c 0x2b                                  ,+
    decimal
             44   43
    datetime ((2008, 1, 20, 1, 0, 20))
    0000   0x14 0x40 0xc1 0x14 0xb8                   .@...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 1]
#### RECORD 59 Base (2015, 0, 0, 6, 6, 1) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x14                                  ..
    decimal
            213   20
    datetime ((2015, 0, 0, 6, 6, 1))
    0000   0x01 0x06 0x06 0x00 0x4f                   ....O
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 60 Base (2012, 0, 23, 10, 13, 8) head[2], body[0] op[0x4d]

    op hex (2)
    0000   0x4d 0x55                                  MU
    decimal
             77   85
    datetime ((2012, 0, 23, 10, 13, 8))
    0000   0x08 0x0d 0x0a 0x97 0x4c                   ....L
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 61 Base (2011, 0, 23, 27, 13, 8) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x35                                  h5
    decimal
            104   53
    datetime ((2011, 0, 23, 27, 13, 8))
    0000   0x08 0x0d 0x5b 0x97 0x5b                   ..[.[
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 62 Base (2013, 0, 16, 3, 13, 8) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x15                                  h.
    decimal
            104   21
    datetime ((2013, 0, 16, 3, 13, 8))
    0000   0x08 0x0d 0x43 0x50 0x0d                   ..CP.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 63 Base (2006, 0, 0, 0, 51, 5) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2006, 0, 0, 0, 51, 5))
    0000   0x05 0x33 0x00 0x00 0x06                   .3...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 Base (2004, 5, 24, 11, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x33                                  .3
    decimal
              0   51
    datetime ((2004, 5, 24, 11, 28, 61))
    0000   0x7d 0x5c 0x0b 0x18 0x24                   }\..$
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 65 Base (2004, 4, 28, 0, 20, 6) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x2c                                  .,
    decimal
              4   44
    datetime ((2004, 4, 28, 0, 20, 6))
    0000   0x46 0x14 0x40 0xdc 0x14                   F.@..
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 66 Bolus (2005, 0, 0, 0, 7, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1, 'dual_component': '??', 'programmed': 5.1, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x33 0x33 0x00 0x5b 0x68 0x55 0x08    .33.[hU.
    decimal
              1   51   51    0   91  104   85    8
    datetime ((2005, 0, 0, 0, 7, 13))
    0000   0x0d 0x07 0x00 0x00 0x05                   .....
    body (0)

#### RECORD 67 Base (2005, 9, 13, 8, 45, 13) head[2], body[0] op[0x76]

    op hex (2)
    0000   0x76 0x48                                  vH
    decimal
            118   72
    datetime ((2005, 9, 13, 8, 45, 13))
    0000   0x8d 0x6d 0x48 0x8d 0x05                   .mH..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 68 Base (2000, 6, 0, 5, 35, 21) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x80                                  ..
    decimal
              0  128
    datetime ((2000, 6, 0, 5, 35, 21))
    0000   0x55 0xa3 0x05 0x00 0x00                   U....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 69 Base (2008, 1, 2, 31, 46, 3) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x76                                  .v
    decimal
              5  118
    datetime ((2008, 1, 2, 31, 46, 3))
    0000   0x03 0x6e 0x3f 0x02 0x08                   .n?..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 70 Base (2001, 8, 5, 8, 2, 31) head[2], body[0] op[0x25]

    op hex (2)
    0000   0x25 0x00                                  %.
    decimal
             37    0
    datetime ((2001, 8, 5, 8, 2, 31))
    0000   0x9f 0x02 0x08 0x25 0x01                   ...%.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 71 Base (2000, 0, 0, 11, 56, 0) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x59                                  .Y
    decimal
            208   89
    datetime ((2000, 0, 0, 11, 56, 0))
    0000   0x00 0x38 0x0b 0x00 0x00                   .8...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 72 Base (2012, 0, 0, 1, 1, 3) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2012, 0, 0, 1, 1, 3))
    0000   0x03 0x01 0x01 0x00 0x0c                   .....
    body (0)

#### RECORD 73 Base (2001, 0, 10, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xe8                                  ..
    decimal
              0  232
    datetime ((2001, 0, 10, 0, 0, 0))
    0000   0x00 0x00 0x00 0x0a 0xa1                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 74 UnabsorbedInsulinBolus unknown head[72], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 0.8, 'curve': 13},
 {'age': 0, 'amount': 0.75, 'curve': 114},
 {'age': 10, 'amount': 2.9, 'curve': 9},
 {'age': 31, 'amount': 0.325, 'curve': 0},
 {'age': 84, 'amount': 1.625, 'curve': 11},
 {'age': 13, 'amount': 0.225, 'curve': 10},
 {'age': 70, 'amount': 0.75, 'curve': 108},
 {'age': 9, 'amount': 1.075, 'curve': 141},
 {'age': 30, 'amount': 2.275, 'curve': 73},
 {'age': 11, 'amount': 2.7, 'curve': 9},
 {'age': 0, 'amount': 0.325, 'curve': 81},
 {'age': 45, 'amount': 0.325, 'curve': 106},
 {'age': 0, 'amount': 0.875, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 125, 'amount': 0.875, 'curve': 1},
 {'age': 35, 'amount': 0.875, 'curve': 0},
 {'age': 108, 'amount': 1.85, 'curve': 75},
 {'age': 13, 'amount': 0.225, 'curve': 91},
 {'age': 88, 'amount': 0.0, 'curve': 76},
 {'age': 9, 'amount': 0.3, 'curve': 13},
 {'age': 80, 'amount': 0.625, 'curve': 13},
 {'age': 106, 'amount': 1.125, 'curve': 0},
 {'age': 0, 'amount': 0.475, 'curve': 0}]
```
    op hex (72)
    0000   0x5c 0x48 0x20 0x09 0x0d 0x1e 0x00 0x72    \H ....r
    0008   0x74 0x0a 0x09 0x0d 0x1f 0x00 0x41 0x54    t.....AT
    0010   0x0b 0x09 0x0d 0x0a 0x1e 0x46 0x6c 0x2b    .....Fl+
    0018   0x09 0x8d 0x5b 0x1e 0x49 0x6c 0x0b 0x09    ..[.Il..
    0020   0x0d 0x00 0x51 0x0d 0x2d 0x6a 0x23 0x00    ..Q.-j#.
    0028   0x00 0x00 0x00 0x00 0x23 0x7d 0x01 0x23    ....#}.#
    0030   0x23 0x00 0x4a 0x6c 0x4b 0x09 0x0d 0x5b    #.JlK..[
    0038   0x00 0x58 0x4c 0x0c 0x09 0x0d 0x19 0x50    .XL....P
    0040   0x0d 0x2d 0x6a 0x00 0x13 0x00 0x00 0x00    .-j.....
    decimal
             92   72   32    9   13   30    0  114
            116   10    9   13   31    0   65   84
             11    9   13   10   30   70  108   43
              9  141   91   30   73  108   11    9
             13    0   81   13   45  106   35    0
              0    0    0    0   35  125    1   35
             35    0   74  108   75    9   13   91
              0   88   76   12    9   13   25   80
             13   45  106    0   19    0    0    0
    datetime (unknown)

    body (0)

#### RECORD 75 Base (2012, 5, 12, 5, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x13                                  ..
    decimal
              0   19
    datetime ((2012, 5, 12, 5, 28, 61))
    0000   0x7d 0x5c 0x05 0x8c 0x1c                   }\...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 76 Base (2012, 0, 24, 0, 19, 19) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x01                                  ..
    decimal
              4    1
    datetime ((2012, 0, 24, 0, 19, 19))
    0000   0x13 0x13 0x00 0x58 0x4c                   ...XL
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 77 Base (2003, 0, 25, 11, 10, 13) head[2], body[0] op[0x4c]

    op hex (2)
    0000   0x4c 0x09                                  L.
    decimal
             76    9
    datetime ((2003, 0, 25, 11, 10, 13))
    0000   0x0d 0x0a 0x4b 0x79 0x43                   ..KyC
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 78 Base (2004, 1, 9, 11, 27, 13) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x09                                  1.
    decimal
             49    9
    datetime ((2004, 1, 9, 11, 27, 13))
    0000   0x0d 0x5b 0x4b 0x49 0x44                   .[KID
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 79 Base (2013, 0, 13, 16, 39, 13) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x09                                  ..
    decimal
             17    9
    datetime ((2013, 0, 13, 16, 39, 13))
    0000   0x0d 0x27 0x50 0x0d 0x2d                   .'P.-
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 80 Base (2000, 3, 0, 0, 48, 30) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xf9                                  j.
    decimal
            106  249
    datetime ((2000, 3, 0, 0, 48, 30))
    0000   0x1e 0xf0 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 81 ChangeTime 2004-04-12T12:08:28 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x7d                                  .}
    decimal
             23  125
    datetime (2004-04-12T12:08:28)
    0000   0x5c 0x08 0x4c 0x2c 0x14                   \.L,.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 82 Base (2000, 0, 23, 23, 1, 20) head[2], body[0] op[0x8c]

    op hex (2)
    0000   0x8c 0x40                                  .@
    decimal
            140   64
    datetime ((2000, 0, 23, 23, 1, 20))
    0000   0x14 0x01 0x17 0x17 0x00                   .....
    body (0)

#### RECORD 83 Base (2002, 4, 10, 13, 9, 17) head[2], body[0] op[0x49]

    op hex (2)
    0000   0x49 0x44                                  ID
    decimal
             73   68
    datetime ((2002, 4, 10, 13, 9, 17))
    0000   0x51 0x09 0x0d 0x0a 0x42                   Q...B
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 84 Base (2000, 0, 7, 13, 9, 50) head[2], body[0] op[0x67]

    op hex (2)
    0000   0x67 0x5c                                  g\
    decimal
            103   92
    datetime ((2000, 0, 7, 13, 9, 50))
    0000   0x32 0x09 0x0d 0x07 0x00                   2....
    body (0)

#### RECORD 85 Base (2009, 9, 13, 13, 9, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2009, 9, 13, 13, 9, 36))
    0000   0xa4 0x49 0x8d 0x6d 0x49                   .I.mI
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 86 Base (2004, 2, 30, 2, 19, 16) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x05                                  ..
    decimal
            141    5
    datetime ((2004, 2, 30, 2, 19, 16))
    0000   0x10 0x93 0x42 0x1e 0x04                   ..B..
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-20.data: 87 records`
