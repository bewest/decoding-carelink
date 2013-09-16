## START logs/ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 495, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x02 0x7d 0x01 0x02 0x02 0x00 0x60 0x77    .}....`w
    0008   0x53 0x1b 0x0d 0x5b 0x00 0x78 0x52 0x14    S..[.xR.
    0010   0x1b 0x0d 0x20 0x50 0x0d 0x2d 0x6a 0x00    .. P.-j.
    0018   0x18 0x00 0x00 0x00 0x00 0x18 0x7d 0x5c    ......}\
##### DEBUG DECIMAL
              2  125    1    2    2    0   96  119
             83   27   13   91    0  120   82   20
             27   13   32   80   13   45  106    0
             24    0    0    0    0   24  125   92
#### RECORD 0 hack1 2013-05-25T21:01:02 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x58 0x8d 0x05 0x00 0x6c 0x6c 0x6c    mX...lll
    0008   0x01 0x00 0x00 0x04 0x04 0x03 0x74 0x56    ......tV
    0010   0x00 0x90 0x0e 0x00 0x30 0x00 0x90 0x0e    ....0...
    0018   0x00 0x90 0x64 0x00 0x00 0x00 0x00 0x00    ..d.....
    0020   0x00 0x01 0x01 0x00 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0xbe              ......
    decimal
            109   88  141    5    0  108  108  108
              1    0    0    4    4    3  116   86
              0  144   14    0   48    0  144   14
              0  144  100    0    0    0    0    0
              0    1    1    0    0    0   12    0
            232    0    0    0   10  190
    datetime (2013-05-25T21:01:02)
    0000   0x42 0x41 0x35 0x19 0x0d                   BA5..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 1 BolusWizard 2013-05-25T21:01:04 head[2], body[13] op[0x5b]
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
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125
    HOUR BITS: [0, 1, 0]
#### RECORD 2 Bolus 2013-05-25T21:01:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'dual_component': '??', 'programmed': 1.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2013-05-25T21:01:04)
    0000   0x44 0x41 0x55 0x19 0x0d                   DAU..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 PumpSuspend 2013-05-25T21:09:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-05-25T21:09:57)
    0000   0x79 0x49 0x15 0x19 0x0d                   yI...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 4 PumpResume 2013-05-25T21:19:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-05-25T21:19:02)
    0000   0x42 0x53 0x15 0x19 0x0d                   BS...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 5 CalBGForPH 2013-05-25T22:00:09 head[2], body[0] op[0x0a]
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
#### RECORD 6 CalBGForPH 2013-05-25T22:00:17 head[2], body[0] op[0x0a]
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
#### RECORD 7 ResultTotals 2013-06-25T13:13:25 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xb6                   .....
    decimal
              7    0    0    3  182
    datetime (2013-06-25T13:13:25)
    0000   0x59 0x8d 0x6d 0x59 0x8d                   Y.mY.
    body (51)
    hex
    0000   0x05 0x00 0x83 0x66 0xbe 0x03 0x00 0x00    ...f....
    0008   0x03 0xb6 0x03 0x7e 0x5e 0x00 0x38 0x06    ...~^.8.
    0010   0x00 0x00 0x00 0x38 0x06 0x00 0x00 0x00    ...8....
    0018   0x00 0x38 0x64 0x00 0x00 0x00 0x01 0x00    .8d.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x05 0x44 0x45 0x24 0x1a 0x8d    ...DE$..
    0030   0x5b 0x05 0x48                             [.H
    decimal
              5    0  131  102  190    3    0    0
              3  182    3  126   94    0   56    6
              0    0    0   56    6    0    0    0
              0   56  100    0    0    0    1    0
              1    0    0   12    0  232    0    0
              0   10    5   68   69   36   26  141
             91    5   72
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 Base (2013, 0, 17, 0, 13, 26) head[2], body[0] op[0x45]

    op hex (2)
    0000   0x45 0x04                                  E.
    decimal
             69    4
    datetime ((2013, 0, 17, 0, 13, 26))
    0000   0x1a 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 9 Base (2000, 0, 0, 0, 0, 30) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 30))
    0000   0x1e 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 10 Base (2015, 5, 24, 5, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1e                                  ..
    decimal
              0   30
    datetime ((2015, 5, 24, 5, 28, 61))
    0000   0x7d 0x5c 0x05 0x38 0xaf                   }\.8.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 11 SelectBasalProfile (2005, 0, 8, 0, 31, 31) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x01                                  ..
    decimal
             20    1
    datetime ((2005, 0, 8, 0, 31, 31))
    0000   0x1f 0x1f 0x00 0x48 0x45                   ...HE
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 12 Base (2014, 0, 0, 8, 52, 13) head[2], body[0] op[0x44]

    op hex (2)
    0000   0x44 0x1a                                  D.
    decimal
             68   26
    datetime ((2014, 0, 0, 8, 52, 13))
    0000   0x0d 0x34 0xc8 0x40 0x5e                   .4.@^
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 13 Base (2005, 0, 21, 4, 52, 13) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x1a                                  ..
    decimal
              4   26
    datetime ((2005, 0, 21, 4, 52, 13))
    0000   0x0d 0x34 0x64 0x75 0x65                   .4due
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 14 Base (2010, 0, 5, 5, 10, 13) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x1a                                  ..
    decimal
             14   26
    datetime ((2010, 0, 5, 5, 10, 13))
    0000   0x0d 0x0a 0x65 0x65 0x5a                   ..eeZ
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 15 Base (2010, 1, 14, 5, 27, 13) head[2], body[0] op[0x2f]

    op hex (2)
    0000   0x2f 0x1a                                  /.
    decimal
             47   26
    datetime ((2010, 1, 14, 5, 27, 13))
    0000   0x0d 0x5b 0x65 0x6e 0x5a                   .[enZ
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 16 Base (2013, 0, 13, 16, 25, 13) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x1a                                  ..
    decimal
             15   26
    datetime ((2013, 0, 13, 16, 25, 13))
    0000   0x0d 0x19 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 17 Base (2000, 3, 0, 0, 48, 19) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xff                                  j.
    decimal
            106  255
    datetime ((2000, 3, 0, 0, 48, 19))
    0000   0x13 0xf0 0x00 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 Base (2014, 0, 0, 18, 18, 1) head[2], body[0] op[0x12]

    op hex (2)
    0000   0x12 0x7d                                  .}
    decimal
             18  125
    datetime ((2014, 0, 0, 18, 18, 1))
    0000   0x01 0x12 0x12 0x00 0x6e                   ....n
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 Base (2012, 0, 19, 10, 13, 26) head[2], body[0] op[0x5a]

    op hex (2)
    0000   0x5a 0x4f                                  ZO
    decimal
             90   79
    datetime ((2012, 0, 19, 10, 13, 26))
    0000   0x1a 0x0d 0x0a 0xb3 0x6c                   ....l
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 20 Base (2014, 0, 19, 27, 13, 26) head[2], body[0] op[0x71]

    op hex (2)
    0000   0x71 0x34                                  q4
    decimal
            113   52
    datetime ((2014, 0, 19, 27, 13, 26))
    0000   0x1a 0x0d 0x5b 0xb3 0x6e                   ..[.n
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 21 Base (2013, 0, 16, 0, 13, 26) head[2], body[0] op[0x71]

    op hex (2)
    0000   0x71 0x14                                  q.
    decimal
            113   20
    datetime ((2013, 0, 16, 0, 13, 26))
    0000   0x1a 0x0d 0x00 0x50 0x0d                   ...P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 22 Base (2000, 0, 0, 0, 0, 12) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 12))
    0000   0x0c 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 23 Base (2005, 5, 8, 5, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0c                                  ..
    decimal
              0   12
    datetime ((2005, 5, 8, 5, 28, 61))
    0000   0x7d 0x5c 0x05 0x48 0x45                   }\.HE
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 24 SelectBasalProfile (2001, 0, 14, 0, 12, 12) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x01                                  ..
    decimal
             20    1
    datetime ((2001, 0, 14, 0, 12, 12))
    0000   0x0c 0x0c 0x00 0x6e 0x71                   ...nq
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 25 Ian54 (2009, 0, 2, 0, 33, 13) head[2], body[57] op[0x54]

    op hex (2)
    0000   0x54 0x1a                                  T.
    decimal
             84   26
    datetime ((2009, 0, 2, 0, 33, 13))
    0000   0x0d 0x21 0x00 0x42 0x79                   .!.By
    body (57)
    hex
    0000   0x14 0x1a 0x0d 0x03 0x00 0x00 0x00 0x19    ........
    0008   0x6e 0x7a 0x34 0x1a 0x0d 0x03 0x00 0x05    nz4.....
    0010   0x00 0x05 0x4d 0x7b 0x14 0x1a 0x0d 0x0a    ..M{....
    0018   0x73 0x4c 0x48 0x36 0x1a 0x0d 0x0a 0x74    sLH6...t
    0020   0x51 0x49 0x36 0x1a 0x0d 0x5b 0x74 0x64    QI6..[td
    0028   0x49 0x16 0x1a 0x0d 0x2b 0x50 0x0d 0x2d    I...+P.-
    0030   0x6a 0x00 0x21 0x00 0x00 0x09 0x00 0x21    j.!....!
    0038   0x7d                                       }
    decimal
             20   26   13    3    0    0    0   25
            110  122   52   26   13    3    0    5
              0    5   77  123   20   26   13   10
            115   76   72   54   26   13   10  116
             81   73   54   26   13   91  116  100
             73   22   26   13   43   80   13   45
            106    0   33    0    0    9    0   33
            125
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 1.2, 'curve': 4},
 {'age': 149, 'amount': 1.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x30 0x55 0x04 0x48 0x95 0x14    \.0U.H..
    decimal
             92    8   48   85    4   72  149   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-05-26T22:09:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-05-26T22:09:36)
    0000   0x64 0x49 0x56 0x1a 0x0d                   dIV..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 28 ResultTotals 2013-06-26T13:13:26 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xfc                   .....
    decimal
              7    0    0    4  252
    datetime (2013-06-26T13:13:26)
    0000   0x5a 0x8d 0x6d 0x5a 0x8d                   Z.mZ.
    body (51)
    hex
    0000   0x05 0x10 0x9a 0x65 0x05 0x05 0x00 0x00    ...e....
    0008   0x04 0xfc 0x03 0x84 0x47 0x01 0x78 0x1d    ....G.x.
    0010   0x00 0x44 0x01 0x78 0x1d 0x00 0xcc 0x36    .D.x...6
    0018   0x00 0xac 0x2e 0x00 0x00 0x00 0x04 0x02    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x3f 0x5a 0x55 0x2a 0x1b 0x8d    ..?ZU*..
    0030   0x5b 0x3f 0x5f                             [?_
    decimal
              5   16  154  101    5    5    0    0
              4  252    3  132   71    1  120   29
              0   68    1  120   29    0  204   54
              0  172   46    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0   10   63   90   85   42   27  141
             91   63   95
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 29 Base (2013, 0, 17, 0, 13, 27) head[2], body[0] op[0x55]

    op hex (2)
    0000   0x55 0x0a                                  U.
    decimal
             85   10
    datetime ((2013, 0, 17, 0, 13, 27))
    0000   0x1b 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 30 Base (2000, 0, 0, 0, 0, 43) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 43))
    0000   0x2b 0x00 0x00 0x00 0x00                   +....
    body (0)

#### RECORD 31 Base (2000, 4, 11, 11, 1, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2b                                  .+
    decimal
              0   43
    datetime ((2000, 4, 11, 11, 1, 61))
    0000   0x7d 0x01 0x2b 0x2b 0x00                   }.++.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 32 Base (2000, 4, 30, 13, 27, 10) head[2], body[0] op[0x5f]

    op hex (2)
    0000   0x5f 0x55                                  _U
    decimal
             95   85
    datetime ((2000, 4, 30, 13, 27, 10))
    0000   0x4a 0x1b 0x0d 0x1e 0x00                   J....
    body (0)

#### RECORD 33 Base (2000, 0, 31, 13, 27, 18) head[2], body[0] op[0x67]

    op hex (2)
    0000   0x67 0x61                                  ga
    decimal
            103   97
    datetime ((2000, 0, 31, 13, 27, 18))
    0000   0x12 0x1b 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 34 Base (2009, 0, 10, 13, 27, 19) head[2], body[0] op[0x44]

    op hex (2)
    0000   0x44 0x5e                                  D^
    decimal
             68   94
    datetime ((2009, 0, 10, 13, 27, 19))
    0000   0x13 0x1b 0x0d 0x0a 0x89                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 35 Base (2009, 0, 27, 13, 27, 51) head[2], body[0] op[0x5d]

    op hex (2)
    0000   0x5d 0x77                                  ]w
    decimal
             93  119
    datetime ((2009, 0, 27, 13, 27, 51))
    0000   0x33 0x1b 0x0d 0x5b 0x89                   3..[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 36 Base (2000, 0, 0, 13, 27, 19) head[2], body[0] op[0x60]

    op hex (2)
    0000   0x60 0x77                                  `w
    decimal
             96  119
    datetime ((2000, 0, 0, 13, 27, 19))
    0000   0x13 0x1b 0x0d 0x00 0x50                   ....P
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 37 Base (2000, 4, 0, 0, 2, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 2, 42))
    0000   0x6a 0x02 0x00 0x00 0x00                   j....
    body (0)

`end logs/ReadHistoryData-page-16.data: 38 records`
