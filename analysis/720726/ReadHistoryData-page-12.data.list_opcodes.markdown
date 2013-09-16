## START logs/ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 229, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1c 0x00 0x00 0x36 0x5c 0x08 0x14 0x07    ...6\...
    0008   0x04 0x6c 0xed 0x04 0x0a 0x53 0xae 0x33    .l...S.3
    0010   0x4c 0xdb 0x0c 0x7b 0x03 0x80 0x00 0x0d    L..{....
    0018   0x1b 0x0c 0x1a 0x26 0x00 0x0a 0x98 0xaa    ...&....
##### DEBUG DECIMAL
             28    0    0   54   92    8   20    7
              4  108  237    4   10   83  174   51
             76  219   12  123    3  128    0   13
             27   12   26   38    0   10  152  170
#### RECORD 0 Bolus 2012-08-27T00:37:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x54 0x00    ..X.X.T.
    decimal
              1    0   88    0   88    0   84    0
    datetime (2012-08-27T00:37:56)
    0000   0xb8 0x25 0x40 0x7b 0x0c                   .%@{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2012-08-27T00:43:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 31,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 112}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-08-27T00:43:44)
    0000   0xac 0x2b 0x00 0x7b 0x0c                   .+.{.
    body (15)
    hex
    0000   0x1f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x70 0x00 0x00 0x00 0x00 0x70 0x36         p....p6
    decimal
             31  144    0  110   23   54    0    0
            112    0    0    0    0  112   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 2.2, 'curve': 4},
 {'age': 139, 'amount': 4.2, 'curve': 4},
 {'age': 169, 'amount': 1.8, 'curve': 4},
 {'age': 63, 'amount': 1.3, 'curve': 20},
 {'age': 103, 'amount': 2.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x58 0x09 0x04 0xa8 0x8b 0x04    \.X.....
    0008   0x48 0xa9 0x04 0x34 0x3f 0x14 0x5c 0x67    H..4?.\g
    0010   0x14                                       .
    decimal
             92   17   88    9    4  168  139    4
             72  169    4   52   63   20   92  103
             20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2012-08-27T00:43:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0xa4 0x00    ........
    decimal
              1    0  132    0  132    0  164    0
    datetime (2012-08-27T00:43:44)
    0000   0xac 0x2b 0x40 0x7b 0x0c                   .+@{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 BasalProfileStart 2012-08-27T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2012-08-27T04:00:00)
    0000   0x80 0x00 0x04 0x1b 0x0c                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 5 CalBGForPH 2012-08-27T08:20:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 67}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2012-08-27T08:20:52)
    0000   0xb4 0x14 0x28 0x7b 0x0c                   ..({.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 6 Base (2012, 8, 27, 8, 20, 52) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime ((2012, 8, 27, 8, 20, 52))
    0000   0xb4 0x14 0x68 0x7b 0x0c                   ..h{.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 7 Ian69 2002-09-11T00:27:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2002-09-11T00:27:22)
    0000   0x96 0x5b 0x00 0x8b 0x02                   .[...
    body (8)
    hex
    0000   0x09 0x7b 0x0c 0x1e 0x90 0x00 0x6e 0x17    .{....n.
    decimal
              9  123   12   30  144    0  110   23
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0]
#### RECORD 8 Base (2000, 1, 0, 0, 44, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x00                                  6.
    decimal
             54    0
    datetime ((2000, 1, 0, 0, 44, 0))
    0000   0x00 0x6c 0x00 0x00 0x00                   .l...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 9 Base (2002, 1, 11, 8, 41, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x6c                                  .l
    decimal
              0  108
    datetime ((2002, 1, 11, 8, 41, 54))
    0000   0x36 0x69 0x08 0x8b 0x02                   6i...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 10 Base (2000, 0, 1, 30, 10, 12) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x1b                                  ..
    decimal
              9   27
    datetime ((2000, 0, 1, 30, 10, 12))
    0000   0x0c 0x0a 0x1e 0x01 0x00                   .....
    body (0)

#### RECORD 11 Base (2011, 4, 0, 0, 0, 44) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x00                                  l.
    decimal
            108    0
    datetime ((2011, 4, 0, 0, 0, 44))
    0000   0x6c 0x00 0x00 0x00 0x8b                   l....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 12 Base (2000, 4, 2, 27, 12, 59) head[2], body[0] op[0x02]

    op hex (2)
    0000   0x02 0x49                                  .I
    decimal
              2   73
    datetime ((2000, 4, 2, 27, 12, 59))
    0000   0x7b 0x0c 0x7b 0x02 0x80                   {.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 13 PumpSuspend (2000, 0, 30, 19, 12, 27) head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x09                                  ..
    decimal
             30    9
    datetime ((2000, 0, 30, 19, 12, 27))
    0000   0x1b 0x0c 0x13 0x1e 0x00                   .....
    body (0)

#### RECORD 14 CalBGForPH 2012-08-27T12:47:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2012-08-27T12:47:46)
    0000   0xae 0x2f 0x2c 0x7b 0x0c                   ./,{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 15 Base (2012, 8, 27, 12, 47, 46) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime ((2012, 8, 27, 12, 47, 46))
    0000   0xae 0x2f 0x2c 0x7b 0x0c                   ./,{.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 Ian69 2015-09-26T08:27:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2015-09-26T08:27:22)
    0000   0x96 0x5b 0x48 0xba 0x2f                   .[H./
    body (8)
    hex
    0000   0x0c 0x7b 0x0c 0x00 0x90 0x00 0x6e 0x17    .{....n.
    decimal
             12  123   12    0  144    0  110   23
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 17 Base (2008, 0, 0, 0, 0, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x1c                                  6.
    decimal
             54   28
    datetime ((2008, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x08                   .....
    body (0)

#### RECORD 18 Base (2009, 1, 12, 5, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x14                                  ..
    decimal
              0   20
    datetime ((2009, 1, 12, 5, 28, 54))
    0000   0x36 0x5c 0x05 0x6c 0xe9                   6\.l.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 0]
#### RECORD 19 Base (2011, 2, 12, 15, 58, 11) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x69                                  .i
    decimal
              4  105
    datetime ((2011, 2, 12, 15, 58, 11))
    0000   0x0b 0xba 0x2f 0x0c 0x1b                   ../..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 20 ClearAlarm (2000, 0, 20, 0, 1, 30) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x0e                                  ..
    decimal
             12   14
    datetime ((2000, 0, 20, 0, 1, 30))
    0000   0x1e 0x01 0x00 0x14 0x00                   .....
    body (0)

#### RECORD 21 SelectBasalProfile (2012, 0, 15, 26, 0, 8) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x00                                  ..
    decimal
             20    0
    datetime ((2012, 0, 15, 26, 0, 8))
    0000   0x08 0x00 0xba 0x2f 0x4c                   .../L
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 22 BasalProfileStart 2012-05-19T09:08:27 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x0c                                  {.
    decimal
            123   12
    datetime (2012-05-19T09:08:27)
    0000   0x5b 0x48 0xa9 0x33 0x0c                   [H.3.
    body (3)
    hex
    0000   0x7b 0x0c 0x00                             {..
    decimal
            123   12    0
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
#### RECORD 23 Base (2000, 4, 28, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 28, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x1c 0x00                   n.6..
    body (0)

`end logs/ReadHistoryData-page-12.data: 24 records`
