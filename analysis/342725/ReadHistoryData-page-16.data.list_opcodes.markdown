## START logs/ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 141, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x38 0x64 0x00 0x00 0x00 0x01 0x00 0x01    8d......
    0008   0x00 0x00 0x0c 0x00 0xe8 0x00 0x00 0x00    ........
    0010   0x0a 0x05 0x44 0x45 0x24 0x1a 0x8d 0x5b    ..DE$..[
    0018   0x05 0x48 0x45 0x04 0x1a 0x0d 0x00 0x51    .HE....Q
##### DEBUG DECIMAL
             56  100    0    0    0    1    0    1
              0    0   12    0  232    0    0    0
             10    5   68   69   36   26  141   91
              5   72   69    4   26   13    0   81
#### RECORD 0 Model522ResultTotals 2013-05-25T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-25T00:00:00)
    0000   0x58 0x8d                                  X.
    body (41)
    hex
    0000   0x05 0x00 0x6c 0x6c 0x6c 0x01 0x00 0x00    ..lll...
    0008   0x04 0x04 0x03 0x74 0x56 0x00 0x90 0x0e    ...tV...
    0010   0x00 0x30 0x00 0x90 0x0e 0x00 0x90 0x64    .0.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  108  108  108    1    0    0
              4    4    3  116   86    0  144   14
              0   48    0  144   14    0  144  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2013-05-25T21:01:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-05-25T21:01:02)
    0000   0x42 0x41 0x35 0x19 0x0d                   BA5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 2 BolusWizard 2013-05-25T21:01:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
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
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-05-25T21:01:04)
    0000   0x44 0x41 0x15 0x19 0x0d                   DA...
    body (15)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d 0x01 0x0e         ....}..
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125    1   14
    HOUR BITS: [0, 1, 0]
#### RECORD 3 Base (2013, 5, 25, 21, 1, 4) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x00                                  ..
    decimal
             14    0
    datetime ((2013, 5, 25, 21, 1, 4))
    0000   0x44 0x41 0x55 0x19 0x0d                   DAU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 PumpSuspend 2013-05-25T21:09:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-25T21:09:57)
    0000   0x79 0x49 0x15 0x19 0x0d                   yI...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 5 PumpResume 2013-05-25T21:19:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-25T21:19:02)
    0000   0x42 0x53 0x15 0x19 0x0d                   BS...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 6 CalBGForPH 2013-05-25T22:00:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-05-25T22:00:09)
    0000   0x49 0x40 0x36 0x19 0x0d                   I@6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-05-25T22:00:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-05-25T22:00:17)
    0000   0x51 0x40 0x36 0x19 0x0d                   Q@6..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 8 MResultTotals 2013-05-26T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xb6                   .....
    decimal
              7    0    0    3  182
    datetime (2013-05-26T00:00:00)
    0000   0x59 0x8d                                  Y.
    body (3)
    hex
    0000   0x6d 0x59 0x8d                             mY.
    decimal
            109   89  141
    HOUR BITS: [1, 0, 0]
#### RECORD 9 Base (2000, 9, 3, 30, 38, 3) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 9, 3, 30, 38, 3))
    0000   0x83 0x66 0xbe 0x03 0x00                   .f...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 Base (2000, 8, 30, 30, 3, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x03                                  ..
    decimal
              0    3
    datetime ((2000, 8, 30, 30, 3, 54))
    0000   0xb6 0x03 0x7e 0x5e 0x00                   ..~^.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 11 Base (2006, 0, 24, 0, 0, 0) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x06                                  8.
    decimal
             56    6
    datetime ((2006, 0, 24, 0, 0, 0))
    0000   0x00 0x00 0x00 0x38 0x06                   ...8.
    body (0)
    DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-16.data: 12 records`
