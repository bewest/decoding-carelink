## START logs/ReadHistoryData-page-17.data
#### STOPPING DOUBLE NULLS @ 604, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0x02 0x02 0x00 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x1e 0x00 0x50 0x47 0x0f    .....PG.
    0010   0x16 0x0d 0x1f 0x00 0x4f 0x59 0x0f 0x16    ....OY..
    0018   0x0d 0x0a 0x87 0x6b 0x6b 0x32 0x16 0x0d    ...kk2..
##### DEBUG DECIMAL
              4    2    2    0    0   12    0  232
              0    0    0   30    0   80   71   15
             22   13   31    0   79   89   15   22
             13   10  135  107  107   50   22   13
#### RECORD 0 Model522ResultTotals 2013-05-20T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-05-20T00:00:00)
    0000   0x53 0x8d                                  S.
    body (41)
    hex
    0000   0x05 0x10 0xa6 0x6a 0x12 0x05 0x00 0x00    ...j....
    0008   0x05 0x34 0x03 0x78 0x43 0x01 0xbc 0x21    .4.xC..!
    0010   0x00 0x62 0x01 0xbc 0x21 0x01 0x28 0x43    .b..!.(C
    0018   0x00 0x94 0x21 0x00 0x00 0x00 0x04 0x01    ..!.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  166  106   18    5    0    0
              5   52    3  120   67    1  188   33
              0   98    1  188   33    1   40   67
              0  148   33    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 CalBGForPH 2013-05-20T03:35:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2013-05-20T03:35:43)
    0000   0x6b 0x63 0x23 0x14 0x0d                   kc#..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2013-05-20T03:35:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2013-05-20T03:35:45)
    0000   0x6d 0x63 0x03 0x14 0x0d                   mc...
    body (15)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x17 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d 0x5c 0x05         ....}\.
    decimal
              0   80   13   45  106   23    0    0
              0    0    0   23  125   92    5
    HOUR BITS: [0, 1, 1]
#### RECORD 3 Base (2000, 0, 23, 23, 1, 20) head[2], body[0] op[0xb4]

    op hex (2)
    0000   0xb4 0x4b                                  .K
    decimal
            180   75
    datetime ((2000, 0, 23, 23, 1, 20))
    0000   0x14 0x01 0x17 0x17 0x00                   .....
    body (0)

#### RECORD 4 Sara6E 2003-06-04T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2003-06-04T00:00:00)
    0000   0x63 0x43                                  cC
    body (49)
    hex
    0000   0x14 0x0d 0x1e 0x00 0x70 0x75 0x09 0x14    ....pu..
    0008   0x0d 0x1f 0x00 0x47 0x51 0x0a 0x14 0x0d    ...GQ...
    0010   0x0a 0xff 0x6d 0x71 0x2a 0x14 0x0d 0x5b    ..mq*..[
    0018   0xff 0x73 0x71 0x0a 0x14 0x0d 0x00 0x50    .sq....P
    0020   0x0d 0x2d 0x6a 0x1c 0x00 0x00 0x00 0x00    .-j.....
    0028   0x00 0x1c 0x7d 0x5c 0x05 0x5c 0xb3 0x14    ..}\.\..
    0030   0x01                                       .
    decimal
             20   13   30    0  112  117    9   20
             13   31    0   71   81   10   20   13
             10  255  109  113   42   20   13   91
            255  115  113   10   20   13    0   80
             13   45  106   28    0    0    0    0
              0   28  125   92    5   92  179   20
              1
    HOUR BITS: [0, 1, 0]
#### RECORD 5 Base (2004, 1, 10, 17, 51, 0) head[2], body[0] op[0x1d]

    op hex (2)
    0000   0x1d 0x1d                                  ..
    decimal
             29   29
    datetime ((2004, 1, 10, 17, 51, 0))
    0000   0x00 0x73 0x71 0x4a 0x14                   .sqJ.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 6 Base (2004, 9, 12, 31, 43, 28) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2004, 9, 12, 31, 43, 28))
    0000   0x9c 0x6b 0x5f 0x2c 0x14                   .k_,.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 7 Base (2004, 9, 12, 0, 15, 28) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2004, 9, 12, 0, 15, 28))
    0000   0x9c 0x4f 0x60 0x0c 0x14                   .O`..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 8 Base (2006, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2006, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x06                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 9 Base (2013, 0, 2, 0, 16, 0) head[2], body[0] op[0x22]

    op hex (2)
    0000   0x22 0x00                                  ".
    decimal
             34    0
    datetime ((2013, 0, 2, 0, 16, 0))
    0000   0x00 0x10 0x00 0x22 0x7d                   ..."}
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 2.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0x6c 0x04                   \.tl.
    decimal
             92    5  116  108    4
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus (2002, 0, 7, 3, 10, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x22 0x22 0x00 0x50 0x60 0x4c 0x14    ."".P`L.
    decimal
              1   34   34    0   80   96   76   20
    datetime ((2002, 0, 7, 3, 10, 13))
    0000   0x0d 0x0a 0x83 0x67 0x62                   ...gb
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 12 Base (2004, 0, 25, 3, 10, 13) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x14                                  1.
    decimal
             49   20
    datetime ((2004, 0, 25, 3, 10, 13))
    0000   0x0d 0x0a 0x83 0x79 0x64                   ...yd
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 13 Base (2005, 1, 11, 3, 27, 13) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x14                                  1.
    decimal
             49   20
    datetime ((2005, 1, 11, 3, 27, 13))
    0000   0x0d 0x5b 0x83 0x6b 0x65                   .[.ke
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 14 Base (2013, 0, 13, 16, 25, 13) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x14                                  ..
    decimal
             17   20
    datetime ((2013, 0, 13, 16, 25, 13))
    0000   0x0d 0x19 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 15 Base (2000, 0, 0, 0, 0, 19) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x01                                  j.
    decimal
            106    1
    datetime ((2000, 0, 0, 0, 0, 19))
    0000   0x13 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 16 SelectBasalProfile 2004-04-15T02:11:28 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x7d                                  .}
    decimal
             20  125
    datetime (2004-04-15T02:11:28)
    0000   0x5c 0x0b 0x22 0x2f 0x14                   \."/.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 17 Base (2001, 1, 20, 29, 52, 20) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0x39                                  f9
    decimal
            102   57
    datetime ((2001, 1, 20, 29, 52, 20))
    0000   0x14 0x74 0x9d 0x14 0x01                   .t...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 18 SelectBasalProfile 2004-01-17T05:43:00 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x14                                  ..
    decimal
             20   20
    datetime (2004-01-17T05:43:00)
    0000   0x00 0x6b 0x65 0x51 0x14                   .keQ.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 19 Base (2004, 5, 20, 3, 56, 18) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2004, 5, 20, 3, 56, 18))
    0000   0x52 0x78 0x63 0x34 0x14                   Rxc4.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 20 Base (2004, 5, 20, 14, 59, 24) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2004, 5, 20, 14, 59, 24))
    0000   0x58 0x7b 0x6e 0x34 0x14                   X{n4.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 21 Base (2004, 5, 20, 15, 26, 24) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2004, 5, 20, 15, 26, 24))
    0000   0x58 0x5a 0x6f 0x14 0x14                   XZo..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 22 Base (2012, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x27                                  .'
    decimal
             13   39
    datetime ((2012, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0xfc                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 23 PumpSuspend (2013, 0, 26, 0, 3, 0) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0xf0                                  ..
    decimal
             30  240
    datetime ((2013, 0, 26, 0, 3, 0))
    0000   0x00 0x03 0x00 0x1a 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0xc1 0x04                   \.P..
    decimal
             92    5   80  193    4
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus (2005, 0, 0, 0, 7, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x1a 0x1a 0x00 0x5a 0x6f 0x54 0x14    ....ZoT.
    decimal
              1   26   26    0   90  111   84   20
    datetime ((2005, 0, 0, 0, 7, 13))
    0000   0x0d 0x07 0x00 0x00 0x05                   .....
    body (0)

#### RECORD 26 Base (2005, 9, 13, 20, 45, 13) head[2], body[0] op[0x82]

    op hex (2)
    0000   0x82 0x54                                  .T
    decimal
            130   84
    datetime ((2005, 9, 13, 20, 45, 13))
    0000   0x8d 0x6d 0x54 0x8d 0x05                   .mT..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 27 Base (2000, 7, 0, 7, 63, 18) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x99                                  ..
    decimal
              0  153
    datetime ((2000, 7, 0, 7, 63, 18))
    0000   0x52 0xff 0x07 0x00 0x00                   R....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 Base (2000, 1, 2, 31, 50, 3) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x82                                  ..
    decimal
              5  130
    datetime ((2000, 1, 2, 31, 50, 3))
    0000   0x03 0x72 0x3f 0x02 0x10                   .r?..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 29 Base (2001, 4, 5, 16, 2, 45) head[2], body[0] op[0x25]

    op hex (2)
    0000   0x25 0x00                                  %.
    decimal
             37    0
    datetime ((2001, 4, 5, 16, 2, 45))
    0000   0x6d 0x02 0x10 0x25 0x01                   m..%.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 30 Base (2000, 3, 0, 8, 20, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x3c                                  <<
    decimal
             60   60
    datetime ((2000, 3, 0, 8, 20, 0))
    0000   0x00 0xd4 0x28 0x00 0x00                   ..(..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 31 Base (2012, 0, 0, 1, 2, 2) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2012, 0, 0, 1, 2, 2))
    0000   0x02 0x02 0x01 0x00 0x0c                   .....
    body (0)

#### RECORD 32 Base (2008, 0, 20, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xe8                                  ..
    decimal
              0  232
    datetime ((2008, 0, 20, 0, 0, 0))
    0000   0x00 0x00 0x00 0x34 0xc8                   ...4.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 33 Base (2000, 0, 30, 13, 21, 7) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0x69                                  Ci
    decimal
             67  105
    datetime ((2000, 0, 30, 13, 21, 7))
    0000   0x07 0x15 0x0d 0x1e 0x00                   .....
    body (0)

#### RECORD 34 old6c (2000, 0, 31, 13, 21, 15) head[2], body[38] op[0x6c]

    op hex (2)
    0000   0x6c 0x4f                                  lO
    decimal
            108   79
    datetime ((2000, 0, 31, 13, 21, 15))
    0000   0x0f 0x15 0x0d 0x1f 0x00                   .....
    body (38)
    hex
    0000   0x49 0x63 0x0f 0x15 0x0d 0x34 0x64 0x5f    Ic...4d_
    0008   0x72 0x11 0x15 0x0d 0x0a 0x22 0x61 0x47    r...."aG
    0010   0x32 0x15 0x8d 0x5b 0x22 0x64 0x47 0x12    2..["dG.
    0018   0x15 0x0d 0x00 0x51 0x0d 0x2d 0x6a 0x24    ...Q.-j$
    0020   0x00 0x00 0x00 0x00 0x00 0x24              .....$
    decimal
             73   99   15   21   13   52  100   95
            114   17   21   13   10   34   97   71
             50   21  141   91   34  100   71   18
             21   13    0   81   13   45  106   36
              0    0    0    0    0   36

#### RECORD 35 Base (2007, 0, 4, 0, 36, 36) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x01                                  }.
    decimal
            125    1
    datetime ((2007, 0, 4, 0, 36, 36))
    0000   0x24 0x24 0x00 0x64 0x47                   $$.dG
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 36 Base (2010, 0, 17, 0, 33, 13) head[2], body[0] op[0x52]

    op hex (2)
    0000   0x52 0x15                                  R.
    decimal
             82   21
    datetime ((2010, 0, 17, 0, 33, 13))
    0000   0x0d 0x21 0x00 0x71 0x4a                   .!.qJ
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 37 Base (2000, 0, 0, 0, 3, 13) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x15                                  ..
    decimal
             21   21
    datetime ((2000, 0, 0, 0, 3, 13))
    0000   0x0d 0x03 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 38 Base (2003, 4, 13, 21, 53, 13) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x52                                  $R
    decimal
             36   82
    datetime ((2003, 4, 13, 21, 53, 13))
    0000   0x4d 0x35 0x15 0x0d 0x03                   M5...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 Base (2005, 0, 13, 6, 5, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x05                                  ..
    decimal
              0    5
    datetime ((2005, 0, 13, 6, 5, 0))
    0000   0x00 0x05 0x66 0x4d 0x15                   ..fM.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 40 Base (2005, 2, 4, 12, 26, 10) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x0d                                  ..
    decimal
             21   13
    datetime ((2005, 2, 4, 12, 26, 10))
    0000   0x0a 0x9a 0x6c 0x64 0x35                   ..ld5
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 41 Base (2005, 6, 4, 21, 26, 27) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x0d                                  ..
    decimal
             21   13
    datetime ((2005, 6, 4, 21, 26, 27))
    0000   0x5b 0x9a 0x75 0x64 0x15                   [.ud.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 42 Base (2010, 1, 13, 13, 16, 0) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x0d                                  ..
    decimal
             21   13
    datetime ((2010, 1, 13, 13, 16, 0))
    0000   0x00 0x50 0x0d 0x2d 0x6a                   .P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 43 NoDelivery (2012, 0, 29, 2, 0, 4) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x00 0x00 0x00                        ....
    decimal
              6    0    0    0
    datetime ((2012, 0, 29, 2, 0, 4))
    0000   0x04 0x00 0x02 0x7d 0x5c                   ...}\
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 44 Base (2002, 12, 2, 1, 4, 20) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x90                                  ..
    decimal
              5  144
    datetime ((2002, 12, 2, 1, 4, 20))
    0000   0xd4 0x04 0x01 0x02 0x02                   .....
    body (0)

#### RECORD 45 Base (2010, 5, 13, 21, 21, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x76                                  .v
    decimal
              0  118
    datetime ((2010, 5, 13, 21, 21, 36))
    0000   0x64 0x55 0x15 0x0d 0x0a                   dU...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 46 Base (2010, 4, 13, 21, 53, 57) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0x58                                  fX
    decimal
            102   88
    datetime ((2010, 4, 13, 21, 53, 57))
    0000   0x79 0x35 0x15 0x0d 0x0a                   y5...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 47 Base (2011, 4, 13, 21, 53, 59) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x64                                  hd
    decimal
            104  100
    datetime ((2011, 4, 13, 21, 53, 59))
    0000   0x7b 0x35 0x15 0x0d 0x5b                   {5..[
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 48 Base (2015, 4, 13, 21, 22, 0) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x4d                                  hM
    decimal
            104   77
    datetime ((2015, 4, 13, 21, 22, 0))
    0000   0x40 0x16 0x15 0x0d 0x1f                   @....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 49 Ian50 (2000, 1, 23, 31, 42, 45) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime ((2000, 1, 23, 31, 42, 45))
    0000   0x2d 0x6a 0xff 0x17 0xf0                   -j...
    body (34)
    hex
    0000   0x00 0x04 0x00 0x16 0x7d 0x5c 0x08 0x08    ....}\..
    0008   0x1a 0x04 0x90 0xec 0x04 0x01 0x16 0x16    ........
    0010   0x00 0x4d 0x40 0x56 0x15 0x0d 0x0a 0x68    .M@V...h
    0018   0x56 0x68 0x36 0x15 0x0d 0x5b 0x68 0x46    Vh6..[hF
    0020   0x69 0x16                                  i.
    decimal
              0    4    0   22  125   92    8    8
             26    4  144  236    4    1   22   22
              0   77   64   86   21   13   10  104
             86  104   54   21   13   91  104   70
            105   22
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 50 Base (2010, 1, 13, 13, 16, 18) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x0d                                  ..
    decimal
             21   13
    datetime ((2010, 1, 13, 13, 16, 18))
    0000   0x12 0x50 0x0d 0x2d 0x6a                   .P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 51 Base (2012, 12, 0, 21, 0, 48) head[2], body[0] op[0xff]

    op hex (2)
    0000   0xff 0x0d                                  ..
    decimal
            255   13
    datetime ((2012, 12, 0, 21, 0, 48))
    0000   0xf0 0x00 0x15 0x00 0x0c                   .....
    body (0)

#### RECORD 52 Base (2008, 1, 4, 15, 24, 11) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x5c                                  }\
    decimal
            125   92
    datetime ((2008, 1, 4, 15, 24, 11))
    0000   0x0b 0x58 0x2f 0x04 0x08                   .X/..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 53 Base (2012, 8, 1, 20, 21, 16) head[2], body[0] op[0x43]

    op hex (2)
    0000   0x43 0x04                                  C.
    decimal
             67    4
    datetime ((2012, 8, 1, 20, 21, 16))
    0000   0x90 0x15 0x14 0x01 0x0c                   .....
    body (0)

#### RECORD 54 ClearAlarm 2013-05-21T22:41:06 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x00                                  ..
    decimal
             12    0
    datetime (2013-05-21T22:41:06)
    0000   0x46 0x69 0x56 0x15 0x0d                   FiV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 55 MResultTotals 2013-05-22T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x94                   .....
    decimal
              7    0    0    4  148
    datetime (2013-05-22T00:00:00)
    0000   0x55 0x8d                                  U.
    body (3)
    hex
    0000   0x6d 0x55 0x8d                             mU.
    decimal
            109   85  141
    HOUR BITS: [1, 0, 0]
#### RECORD 56 Base (2000, 9, 5, 2, 38, 23) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x10                                  ..
    decimal
              5   16
    datetime ((2000, 9, 5, 2, 38, 23))
    0000   0x97 0x66 0x22 0x05 0x00                   .f"..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 57 Base (2001, 8, 11, 20, 3, 20) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2001, 8, 11, 20, 3, 20))
    0000   0x94 0x03 0x74 0x4b 0x01                   ..tK.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 58 Base (2009, 0, 0, 1, 49, 0) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x19                                   .
    decimal
             32   25
    datetime ((2009, 0, 0, 1, 49, 0))
    0000   0x00 0x31 0x01 0x20 0x19                   .1. .
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 59 Base (2000, 0, 21, 24, 0, 47) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x88                                  ..
    decimal
              0  136
    datetime ((2000, 0, 21, 24, 0, 47))
    0000   0x2f 0x00 0x98 0x35 0x00                   /..5.
    body (0)
    DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-17.data: 60 records`
