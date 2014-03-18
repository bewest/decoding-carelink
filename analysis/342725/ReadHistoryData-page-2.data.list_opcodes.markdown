## START logs/ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 239, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6e 0x2d 0x8e 0x05 0x00 0x7d 0x6b 0x94    n-...}k.
    0008   0x07 0x00 0x00 0x04 0x63 0x01 0xbf 0x28    ....c..(
    0010   0x02 0xa4 0x3c 0x00 0xbb 0x02 0x88 0x00    ..<.....
    0018   0x10 0x00 0x0c 0x00 0x00 0x06 0x01 0x01    ........
##### DEBUG DECIMAL
            110   45  142    5    0  125  107  148
              7    0    0    4   99    1  191   40
              2  164   60    0  187    2  136    0
             16    0   12    0    0    6    1    1
#### RECORD 0 Bolus (2002, 4, 0, 4, 0, 16) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x50 0x00                        ..P.
    decimal
              1    0   80    0
    datetime ((2002, 4, 0, 4, 0, 16))
    0000   0x50 0x00 0x04 0x00 0x12                   P....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 1 Base (2009, 4, 20, 10, 14, 45) head[2], body[0] op[0xf3]

    op hex (2)
    0000   0xf3 0x4e                                  .N
    decimal
            243   78
    datetime ((2009, 4, 20, 10, 14, 45))
    0000   0x6d 0x0e 0x0a 0x94 0x19                   m....
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 2 Base (2009, 4, 18, 31, 14, 45) head[2], body[0] op[0xc7]

    op hex (2)
    0000   0xc7 0x33                                  .3
    decimal
            199   51
    datetime ((2009, 4, 18, 31, 14, 45))
    0000   0x6d 0x0e 0x3f 0x12 0x19                   m.?..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 3 Base (2005, 4, 9, 2, 14, 45) head[2], body[0] op[0xc7]

    op hex (2)
    0000   0xc7 0x93                                  ..
    decimal
            199  147
    datetime ((2005, 4, 9, 2, 14, 45))
    0000   0x6d 0x0e 0xc2 0x89 0x65                   m...e
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 TempBasal 2014-03-13T19:08:08 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-13T19:08:08)
    0000   0x08 0xc8 0x13 0x0d 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 5 TempBasalDuration 2014-03-13T19:08:08 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-13T19:08:08)
    0000   0x08 0xc8 0x13 0x0d 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 6 BasalProfileStart 2014-03-13T20:08:08 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-13T20:08:08)
    0000   0x08 0xc8 0x14 0x0d 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2014-03-13T20:10:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2014-03-13T20:10:35)
    0000   0x23 0xca 0x34 0x6d 0x0e                   #.4m.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2014-03-13T20:10:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-03-13T20:10:35)
    0000   0x23 0xca 0x74 0x6d 0x0e                   #.tm.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 PumpSuspend 2014-03-13T20:13:21 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-13T20:13:21)
    0000   0x15 0xcd 0x14 0x0d 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 BasalProfileStart 2014-03-13T21:47:56 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-13T21:47:56)
    0000   0x38 0xef 0x15 0x0d 0x0e                   8....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 11 PumpResume 2014-03-13T21:47:56 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-13T21:47:56)
    0000   0x38 0xef 0x15 0x0d 0x0e                   8....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 12 CalBGForPH 2014-03-13T21:48:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2014-03-13T21:48:02)
    0000   0x02 0xf0 0x35 0x0d 0x0e                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 BolusWizard 2014-03-13T21:48:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 1,
 'bg': 85,
 'bg_target_high': 1,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 80,
 'carb_ratio': 0,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2014-03-13T21:48:12)
    0000   0x0c 0xf0 0x15 0x0d 0x0e                   .....
    body (13)
    hex
    0000   0x50 0x50 0x00 0x6e 0x32 0x50 0x00 0x01    PP.n2P..
    0008   0x20 0x00 0x00 0x00 0x01                    ....
    decimal
             80   80    0  110   50   80    0    1
             32    0    0    0    1
    HOUR BITS: [1, 1, 1]
#### RECORD 14 Base (2000, 4, 0, 6, 8, 28) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x64                                   d
    decimal
             32  100
    datetime ((2000, 4, 0, 6, 8, 28))
    0000   0x5c 0x08 0x26 0xa0 0x90                   \.&..
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 15 Base (2001, 8, 0, 1, 1, 16) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0xaa                                  *.
    decimal
             42  170
    datetime ((2001, 8, 0, 1, 1, 16))
    0000   0x90 0x01 0x01 0x20 0x01                   ... .
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 16 Base (2005, 0, 16, 12, 0, 0) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2005, 0, 16, 12, 0, 0))
    0000   0x00 0x00 0x0c 0xf0 0x55                   ....U
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 17 Base (2005, 5, 25, 3, 21, 27) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0e                                  ..
    decimal
             13   14
    datetime ((2005, 5, 25, 3, 21, 27))
    0000   0x5b 0x55 0x03 0xf9 0x15                   [U...
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 18 Base (2002, 1, 14, 0, 16, 40) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0e                                  ..
    decimal
             13   14
    datetime ((2002, 1, 14, 0, 16, 40))
    0000   0x28 0x50 0x00 0x6e 0x32                   (P.n2
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 19 Ian50 2008-02-01T00:16:00 head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x00                                  P.
    decimal
             80    0
    datetime (2008-02-01T00:16:00)
    0000   0x00 0x90 0x00 0x01 0x18                   .....
    body (34)
    hex
    0000   0x00 0x90 0x64 0x5c 0x0e 0x3e 0x05 0x80    ..d\.>..
    0008   0xe2 0x0f 0x80 0x26 0xa9 0x90 0x2a 0xb3    ...&..*.
    0010   0x90 0x01 0x00 0x90 0x00 0x90 0x01 0x18    ........
    0018   0x02 0x03 0xf9 0x75 0x0d 0x0e 0x33 0x78    ...u..3x
    0020   0x20 0xd2                                   .
    decimal
              0  144  100   92   14   62    5  128
            226   15  128   38  169  144   42  179
            144    1    0  144    0  144    1   24
              2    3  249  117   13   14   51  120
             32  210
    HOUR BITS: [1, 0, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 20 TempBasalDuration (2000, 0, 2, 22, 8, 14) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 390}
```
    op hex (2)
    0000   0x16 0x0d                                  ..
    decimal
             22   13
    datetime ((2000, 0, 2, 22, 8, 14))
    0000   0x0e 0x08 0x16 0x02 0x20                   .... 
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 21 Base (2001, 0, 5, 27, 14, 13) head[2], body[0] op[0xd2]

    op hex (2)
    0000   0xd2 0x16                                  ..
    decimal
            210   22
    datetime ((2001, 0, 5, 27, 14, 13))
    0000   0x0d 0x0e 0x7b 0x05 0x21                   ..{.!
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 22 Base (2000, 0, 21, 13, 14, 13) head[2], body[0] op[0xd2]

    op hex (2)
    0000   0xd2 0x17                                  ..
    decimal
            210   23
    datetime ((2000, 0, 21, 13, 14, 13))
    0000   0x0d 0x0e 0x2d 0x15 0x00                   ..-..
    body (0)

#### RECORD 23 BasalProfileStart 2014-03-14T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-14T00:00:00)
    0000   0x00 0xc0 0x00 0x0e 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 24 MResultTotals 2014-03-14T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x63                   ....c
    decimal
              7    0    0    4   99
    datetime (2014-03-14T00:00:00)
    0000   0x2d 0x8e                                  -.
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-2.data: 25 records`
