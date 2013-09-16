## START logs/ReadHistoryData-page-26.data
#### STOPPING DOUBLE NULLS @ 191, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x88 0x0a 0x4e 0x67 0x0d 0x7b 0x03 0x9e    ..Ng.{..
    0008   0x0a 0x0e 0x07 0x0d 0x1a 0x26 0x00 0x1f    .....&..
    0010   0x20 0x9e 0x0a 0x0e 0x07 0x0d 0x0a 0xac     .......
    0018   0x90 0x0b 0x2e 0x67 0x0d 0x3f 0x15 0x90    ...g.?..
##### DEBUG DECIMAL
            136   10   78  103   13  123    3  158
             10   14    7   13   26   38    0   31
             32  158   10   14    7   13   10  172
            144   11   46  103   13   63   21  144
#### RECORD 0 LowBattery 2013-08-07T01:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-08-07T01:01:00)
    0000   0x80 0x01 0x01 0x07 0x0d                   .....
    body (0)

#### RECORD 1 BasalProfileStart 2013-08-07T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-07T04:00:00)
    0000   0x80 0x00 0x04 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 2 Battery 2013-08-07T07:46:16 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-08-07T07:46:16)
    0000   0x90 0x2e 0x07 0x07 0x0d                   .....
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 Battery 2013-08-07T07:46:42 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-08-07T07:46:42)
    0000   0xaa 0x2e 0x07 0x07 0x0d                   .....
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 BasalProfileStart 2013-08-07T07:46:42 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-07T07:46:42)
    0000   0xaa 0x2e 0x07 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 0, 1]
#### RECORD 5 CalBGForPH 2013-08-07T07:49:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 53}
```
    op hex (2)
    0000   0x0a 0x35                                  .5
    decimal
             10   53
    datetime (2013-08-07T07:49:25)
    0000   0x99 0x31 0x27 0x67 0x0d                   .1'g.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 Ian3F 2013-08-07T07:49:25 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2013-08-07T07:49:25)
    0000   0x99 0x31 0xa7 0x67 0x0d                   .1.g.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 BasalProfileStart 2013-08-07T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-07T09:30:00)
    0000   0x80 0x1e 0x09 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 8 Ian69 2013-08-07T10:30:00 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-07T10:30:00)
    0000   0x80 0x1e 0x0a 0x07 0x0d                   .....
    body (8)
    hex
    0000   0x2a 0x1e 0x0a 0xa3 0x81 0x35 0x2b 0x67    *....5+g
    decimal
             42   30   10  163  129   53   43  103

#### RECORD 9 Base (2007, 2, 11, 21, 1, 20) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2007, 2, 11, 21, 1, 20))
    0000   0x14 0x81 0x35 0x6b 0x67                   ..5kg
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 10 Base (2003, 6, 16, 10, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2003, 6, 16, 10, 22, 41))
    0000   0x69 0x96 0x0a 0xb0 0x83                   i....
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 11 Base (2003, 4, 22, 31, 13, 39) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x2c                                  .,
    decimal
              0   44
    datetime ((2003, 4, 22, 31, 13, 39))
    0000   0x67 0x0d 0x3f 0x16 0x83                   g.?..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 Base (2006, 4, 9, 9, 13, 39) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0c                                  ..
    decimal
              0   12
    datetime ((2006, 4, 9, 9, 13, 39))
    0000   0x67 0x0d 0x69 0x69 0x96                   g.ii.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 13 BasalProfileStart 2013-08-07T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-07T13:00:00)
    0000   0x80 0x00 0x0d 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 14 CalBGForPH 2013-08-07T13:27:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2013-08-07T13:27:29)
    0000   0x9d 0x1b 0x2d 0x67 0x0d                   ..-g.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 15 Ian3F 2013-08-07T13:27:29 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2013-08-07T13:27:29)
    0000   0x9d 0x1b 0xcd 0x67 0x0d                   ...g.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2013-08-07T14:10:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 60,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 216}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-07T14:10:08)
    0000   0x88 0x0a 0x0e 0x67 0x0d                   ...g.
    body (15)
    hex
    0000   0x3c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    <..n.6..
    0008   0xd8 0x00 0x00 0x00 0x00 0xd8 0x36         ......6
    decimal
             60  144    0  110   23   54    0    0
            216    0    0    0    0  216   54
    DAY BITS: [0, 1, 1]
#### RECORD 17 Ian69 2013-08-07T14:10:08 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-07T14:10:08)
    0000   0x88 0x0a 0x0e 0x07 0x0d                   .....
    body (8)
    hex
    0000   0x0e 0x1e 0x34 0xc7 0x88 0x0a 0x2e 0x07    ..4.....
    decimal
             14   30   52  199  136   10   46    7

#### RECORD 18 Base (2007, 2, 14, 10, 24, 1) head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x1e                                  ..
    decimal
            141   30
    datetime ((2007, 2, 14, 10, 24, 1))
    0000   0x01 0x98 0x0a 0x0e 0x07                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 19 Base (2000, 3, 18, 0, 24, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x01                                  ..
    decimal
             13    1
    datetime ((2000, 3, 18, 0, 24, 0))
    0000   0x00 0xd8 0x00 0x12 0x00                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-26.data: 20 records`
