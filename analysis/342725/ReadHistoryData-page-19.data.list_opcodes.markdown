## START logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 127, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x01 0x01 0x00 0x00 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x0a 0x3b 0x4e 0x45 0x29    ....;NE)
    0010   0x0c 0x8d 0x5b 0x3b 0x51 0x45 0x09 0x0c    ..[;QE..
    0018   0x0d 0x00 0x51 0x0d 0x2d 0x6a 0x2a 0x00    ..Q.-j*.
##### DEBUG DECIMAL
              1    1    0    0    0   12    0  232
              0    0    0   10   59   78   69   41
             12  141   91   59   81   69    9   12
             13    0   81   13   45  106   42    0
#### RECORD 0 Model522ResultTotals 2013-05-11T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-11T00:00:00)
    0000   0x4a 0x8d                                  J.
    body (41)
    hex
    0000   0x05 0x00 0x71 0x40 0xba 0x05 0x00 0x00    ..q@....
    0008   0x04 0x42 0x03 0x72 0x51 0x00 0xd0 0x13    .B.rQ...
    0010   0x00 0x33 0x00 0xd0 0x13 0x00 0x9c 0x4b    .3.....K
    0018   0x00 0x34 0x19 0x00 0x00 0x00 0x02 0x01    .4......
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  113   64  186    5    0    0
              4   66    3  114   81    0  208   19
              0   51    0  208   19    0  156   75
              0   52   25    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2013-05-11T22:49:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-05-11T22:49:42)
    0000   0x6a 0x71 0x36 0x0b 0x0d                   jq6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2013-05-11T22:49:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-05-11T22:49:55)
    0000   0x77 0x71 0x16 0x0b 0x0d                   wq...
    body (15)
    hex
    0000   0x46 0x50 0x0d 0x2d 0x6a 0x00 0x35 0x00    FP.-j.5.
    0008   0x00 0x00 0x00 0x35 0x7d 0x01 0x35         ...5}.5
    decimal
             70   80   13   45  106    0   53    0
              0    0    0   53  125    1   53
    HOUR BITS: [0, 1, 1]
#### RECORD 3 Base (2013, 5, 11, 22, 49, 55) head[2], body[0] op[0x35]

    op hex (2)
    0000   0x35 0x00                                  5.
    decimal
             53    0
    datetime ((2013, 5, 11, 22, 49, 55))
    0000   0x77 0x71 0x56 0x0b 0x0d                   wqV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 CalBGForPH 2013-05-11T23:39:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-05-11T23:39:07)
    0000   0x47 0x67 0x37 0x0b 0x0d                   Gg7..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 MResultTotals 2013-05-12T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x58                   ....X
    decimal
              7    0    0    4   88
    datetime (2013-05-12T00:00:00)
    0000   0x4b 0x8d                                  K.
    body (3)
    hex
    0000   0x6d 0x4b 0x8d                             mK.
    decimal
            109   75  141
    HOUR BITS: [1, 0, 0]
#### RECORD 6 Base (2000, 5, 2, 25, 37, 47) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x00                                  ..
    decimal
              5    0
    datetime ((2000, 5, 2, 25, 37, 47))
    0000   0x6f 0x65 0x79 0x02 0x00                   oey..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 Base (2000, 4, 17, 4, 3, 24) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2000, 4, 17, 4, 3, 24))
    0000   0x58 0x03 0x84 0x51 0x00                   X..Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 8 Base (2003, 1, 20, 0, 6, 0) head[2], body[0] op[0xd4]

    op hex (2)
    0000   0xd4 0x13                                  ..
    decimal
            212   19
    datetime ((2003, 1, 20, 0, 6, 0))
    0000   0x00 0x46 0x00 0xd4 0x13                   .F...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Base (2000, 4, 0, 0, 0, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xd4                                  ..
    decimal
              0  212
    datetime ((2000, 4, 0, 0, 0, 36))
    0000   0x64 0x00 0x00 0x00 0x00                   d....
    body (0)

`end logs/ReadHistoryData-page-19.data: 10 records`
