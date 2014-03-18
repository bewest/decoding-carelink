## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 254, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x03 0x01 0x01 0x01 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x1e 0x00 0x51 0x08 0x07    .....Q..
    0010   0x18 0x0d 0x1f 0x00 0x65 0x1a 0x07 0x18    ....e...
    0018   0x0d 0x0a 0x74 0x5b 0x22 0x2a 0x18 0x0d    ..t["*..
##### DEBUG DECIMAL
              3    1    1    1    0   12    0  232
              0    0    0   30    0   81    8    7
             24   13   31    0  101   26    7   24
             13   10  116   91   34   42   24   13
#### RECORD 0 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 0.9, 'curve': 4},
 {'age': 14, 'amount': 1.5, 'curve': 20},
 {'age': 24, 'amount': 2.3, 'curve': 20},
 {'age': 164, 'amount': 1.2, 'curve': 20},
 {'age': 204, 'amount': 0.8, 'curve': 20},
 {'age': 214, 'amount': 0.6, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x24 0x32 0x04 0x3c 0x0e 0x14    \.$2.<..
    0008   0x5c 0x18 0x14 0x30 0xa4 0x14 0x20 0xcc    \..0.. .
    0010   0x14 0x18 0xd6 0x14                        ....
    decimal
             92   20   36   50    4   60   14   20
             92   24   20   48  164   20   32  204
             20   24  214   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus (2005, 0, 0, 0, 7, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x27 0x27 0x00 0x59 0x2c 0x54 0x16    .''.Y,T.
    decimal
              1   39   39    0   89   44   84   22
    datetime ((2005, 0, 0, 0, 7, 13))
    0000   0x0d 0x07 0x00 0x00 0x05                   .....
    body (0)

#### RECORD 2 Base (2005, 1, 13, 22, 45, 13) head[2], body[0] op[0xf4]

    op hex (2)
    0000   0xf4 0x56                                  .V
    decimal
            244   86
    datetime ((2005, 1, 13, 22, 45, 13))
    0000   0x0d 0x6d 0x56 0x0d 0x05                   .mV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 Base (2000, 7, 0, 7, 48, 51) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xa4                                  ..
    decimal
              0  164
    datetime ((2000, 7, 0, 7, 48, 51))
    0000   0x73 0xf0 0x07 0x00 0x00                   s....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 Base (2012, 1, 2, 23, 8, 3) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0xf4                                  ..
    decimal
              5  244
    datetime ((2012, 1, 2, 23, 8, 3))
    0000   0x03 0x48 0x37 0x02 0xac                   .H7..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 5 Base (2002, 8, 13, 12, 2, 48) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x00                                  -.
    decimal
             45    0
    datetime ((2002, 8, 13, 12, 2, 48))
    0000   0xb0 0x02 0xac 0x2d 0x02                   ...-.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 6 SelectBasalProfile (2000, 2, 0, 22, 24, 0) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x4e                                  .N
    decimal
             20   78
    datetime ((2000, 2, 0, 22, 24, 0))
    0000   0x00 0x98 0x16 0x00 0x00                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 Base (2012, 0, 0, 2, 2, 3) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x07                                  ..
    decimal
              0    7
    datetime ((2012, 0, 0, 2, 2, 3))
    0000   0x03 0x02 0x02 0x00 0x0c                   .....
    body (0)

#### RECORD 8 Base (2000, 0, 30, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xe8                                  ..
    decimal
              0  232
    datetime ((2000, 0, 30, 0, 0, 0))
    0000   0x00 0x00 0x00 0x1e 0x00                   .....
    body (0)

#### RECORD 9 Base (2000, 0, 31, 13, 23, 13) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x23                                  e#
    decimal
            101   35
    datetime ((2000, 0, 31, 13, 23, 13))
    0000   0x0d 0x17 0x0d 0x1f 0x00                   .....
    body (0)

#### RECORD 10 ChangeUtility (2003, 0, 10, 13, 23, 14) head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x03                                  c.
    decimal
             99    3
    datetime ((2003, 0, 10, 13, 23, 14))
    0000   0x0e 0x17 0x0d 0x0a 0xa3                   .....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 11 Base (2003, 0, 27, 13, 23, 46) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x1e                                  x.
    decimal
            120   30
    datetime ((2003, 0, 27, 13, 23, 46))
    0000   0x2e 0x17 0x0d 0x5b 0xa3                   ...[.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 12 BasalProfileStart (2000, 0, 0, 13, 23, 14) head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x1e                                  {.
    decimal
            123   30
    datetime ((2000, 0, 0, 13, 23, 14))
    0000   0x0e 0x17 0x0d 0x00 0x50                   ....P
    body (3)
    hex
    0000   0x0d 0x2d 0x6a                             .-j
    decimal
             13   45  106
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 13 ChangeBasalProfile (2008, 0, 0, 0, 0, 0) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x00                                  ..
    decimal
              8    0
    datetime ((2008, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x08                   .....
    body (44)
    hex
    0000   0x7d 0x01 0x08 0x08 0x00 0x7b 0x1e 0x4e    }....{.N
    0008   0x17 0x0d 0x5b 0x00 0x65 0x32 0x0e 0x17    ..[.e2..
    0010   0x0d 0x39 0x50 0x0d 0x2d 0x6a 0x00 0x2b    .9P.-j.+
    0018   0x00 0x00 0x00 0x00 0x2b 0x7d 0x5c 0x05    ....+}\.
    0020   0x20 0x1a 0x04 0x01 0x2b 0x2b 0x00 0x65     ...++.e
    0028   0x32 0x4e 0x17 0x0d                        2N..
    decimal
            125    1    8    8    0  123   30   78
             23   13   91    0  101   50   14   23
             13   57   80   13   45  106    0   43
              0    0    0    0   43  125   92    5
             32   26    4    1   43   43    0  101
             50   78   23   13

#### RECORD 14 CalBGForPH 2013-04-23T16:54:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-04-23T16:54:32)
    0000   0x60 0x36 0x30 0x17 0x0d                   `60..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 CalBGForPH 2013-04-23T21:50:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-04-23T21:50:16)
    0000   0x50 0x32 0x35 0x17 0x0d                   P25..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 16 BolusWizard 2013-04-23T21:50:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-04-23T21:50:40)
    0000   0x68 0x32 0x15 0x17 0x0d                   h2...
    body (15)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0x02 0x2b 0x00    8P.-j.+.
    0008   0x00 0x00 0x00 0x2d 0x7d 0x5c 0x08         ...-}\.
    decimal
             56   80   13   45  106    2   43    0
              0    0    0   45  125   92    8
    HOUR BITS: [0, 0, 1]
#### RECORD 17 Base (2001, 0, 20, 30, 32, 20) head[2], body[0] op[0xac]

    op hex (2)
    0000   0xac 0xaa                                  ..
    decimal
            172  170
    datetime ((2001, 0, 20, 30, 32, 20))
    0000   0x14 0x20 0xbe 0x14 0x01                   . ...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 18 Base (2007, 1, 21, 18, 40, 0) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x2d                                  --
    decimal
             45   45
    datetime ((2007, 1, 21, 18, 40, 0))
    0000   0x00 0x68 0x32 0x55 0x17                   .h2U.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 19 Base (2007, 0, 16, 4, 0, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x07                                  ..
    decimal
             13    7
    datetime ((2007, 0, 16, 4, 0, 0))
    0000   0x00 0x00 0x04 0xf0 0x57                   ....W
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 20 Base (2004, 4, 0, 5, 13, 23) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x6d                                  .m
    decimal
             13  109
    datetime ((2004, 4, 0, 5, 13, 23))
    0000   0x57 0x0d 0x05 0x00 0xa4                   W....
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 21 Base (2000, 0, 4, 0, 0, 3) head[2], body[0] op[0x88]

    op hex (2)
    0000   0x88 0xc2                                  ..
    decimal
            136  194
    datetime ((2000, 0, 4, 0, 0, 3))
    0000   0x03 0x00 0x00 0x04 0xf0                   .....
    body (0)
    YEAR BITS: [1, 1, 1, 1]
#### RECORD 22 Prime (2000, 0, 1, 17, 0, 30) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 12.8, 'fixed': 7.0, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x70 0x46 0x01 0x80                   .pF..
    decimal
              3  112   70    1  128
    datetime ((2000, 0, 1, 17, 0, 30))
    0000   0x1e 0x00 0x71 0x01 0x80                   ..q..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 23 PumpSuspend 2010-05-08T00:26:24 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2010-05-08T00:26:24)
    0000   0x58 0x5a 0x00 0x28 0x0a                   XZ.(.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-24.data: 24 records`
