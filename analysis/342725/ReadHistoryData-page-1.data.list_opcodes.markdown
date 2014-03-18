## START logs/ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 128, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x14 0xf4 0x46 0x0f 0x0e 0x5b 0x00 0x11    ..F..[..
    0008   0xca 0x08 0x6f 0x0e 0x0f 0x50 0x00 0x6e    ..o..P.n
    0010   0x28 0x50 0x00 0x00 0x34 0x00 0x00 0x00    (P..4...
    0018   0x00 0x34 0x64 0x5c 0x05 0x80 0x4e 0x80    .4d\..N.
##### DEBUG DECIMAL
             20  244   70   15   14   91    0   17
            202    8  111   14   15   80    0  110
             40   80    0    0   52    0    0    0
              0   52  100   92    5  128   78  128
#### RECORD 0 Sara6E 2014-03-15T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-15T00:00:00)
    0000   0x2e 0x8e                                  ..
    body (49)
    hex
    0000   0x05 0x00 0x64 0x2b 0x80 0x05 0x00 0x00    ..d+....
    0008   0x06 0x66 0x01 0xc2 0x1b 0x04 0xa4 0x49    .f.....I
    0010   0x01 0x4f 0x04 0x30 0x00 0x00 0x00 0x74    .O.0...t
    0018   0x00 0x00 0x09 0x00 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x99    ........
    0028   0x99 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  100   43  128    5    0    0
              6  102    1  194   27    4  164   73
              1   79    4   48    0    0    0  116
              0    0    9    0    1    0    0    0
              0    0    0    0    0    0    0  153
            153    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 BasalProfileStart 2014-03-15T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-15T02:00:00)
    0000   0x00 0xc0 0x02 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 2 BasalProfileStart 2014-03-15T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-15T04:00:00)
    0000   0x00 0xc0 0x04 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BasalProfileStart 2014-03-15T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-15T06:00:00)
    0000   0x00 0xc0 0x06 0x0f 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2014-03-15T06:52:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 231}
```
    op hex (2)
    0000   0x0a 0xe7                                  ..
    decimal
             10  231
    datetime (2014-03-15T06:52:09)
    0000   0x09 0xf4 0x26 0x6f 0x0e                   ..&o.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 Ian3F 2014-03-15T06:52:09 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1c                                  ?.
    decimal
             63   28
    datetime (2014-03-15T06:52:09)
    0000   0x09 0xf4 0xe6 0x6f 0x0e                   ...o.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2014-03-15T06:52:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 231,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 12.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe7                                  [.
    decimal
             91  231
    datetime (2014-03-15T06:52:20)
    0000   0x14 0xf4 0x06 0x0f 0x0e                   .....
    body (13)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x80 0x00    .P.n(P..
    0008   0x00 0x00 0x00 0x00 0x00                   .....
    decimal
              0   80    0  110   40   80  128    0
              0    0    0    0    0
    HOUR BITS: [1, 1, 1]
#### RECORD 7 Base (2000, 0, 0, 0, 0, 1) head[2], body[0] op[0x80]

    op hex (2)
    0000   0x80 0x64                                  .d
    decimal
            128  100
    datetime ((2000, 0, 0, 0, 0, 1))
    0000   0x01 0x00 0x80 0x00 0x80                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-1.data: 8 records`
