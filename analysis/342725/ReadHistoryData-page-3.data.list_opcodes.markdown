## START logs/ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 437, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x30 0x64 0x5c 0x0e 0x68 0x1c 0x80 0xa0    0d\.h...
    0008   0xc6 0x80 0x64 0xac 0x90 0xb8 0xb6 0x90    ..d.....
    0010   0x01 0x00 0x30 0x00 0x30 0x00 0x58 0x00    ..0.0.X.
    0018   0x0f 0xe8 0x4e 0x6c 0x0e 0x0a 0x7c 0x0d    ..Nl..|.
##### DEBUG DECIMAL
             48  100   92   14  104   28  128  160
            198  128  100  172  144  184  182  144
              1    0   48    0   48    0   88    0
             15  232   78  108   14   10  124   13
#### RECORD 0 Bolus (2002, 4, 0, 8, 0, 4) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x44 0x00                        ..D.
    decimal
              1    0   68    0
    datetime ((2002, 4, 0, 8, 0, 4))
    0000   0x44 0x00 0x08 0x00 0x32                   D...2
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 1 Base (2000, 0, 1, 27, 14, 12) head[2], body[0] op[0xe4]

    op hex (2)
    0000   0xe4 0x40                                  .@
    decimal
            228   64
    datetime ((2000, 0, 1, 27, 14, 12))
    0000   0x0c 0x0e 0x7b 0x01 0x00                   ..{..
    body (0)

#### RECORD 2 Base (2000, 0, 26, 4, 14, 12) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x02                                  ..
    decimal
            192    2
    datetime ((2000, 0, 26, 4, 14, 12))
    0000   0x0c 0x0e 0x04 0x1a 0x00                   .....
    body (0)

#### RECORD 3 BasalProfileStart 2014-03-12T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-12T04:00:00)
    0000   0x00 0xc0 0x04 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2014-03-12T05:28:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 314}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2014-03-12T05:28:32)
    0000   0x20 0xdc 0x25 0x6c 0x8e                    .%l.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 Ian3F 2014-03-12T05:28:32 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x27                                  ?'
    decimal
             63   39
    datetime (2014-03-12T05:28:32)
    0000   0x20 0xdc 0x45 0x6c 0x0e                    .El.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2014-03-12T05:28:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 314,
 'bg_target_high': 1,
 'bg_target_low': 30,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 2.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3a                                  [:
    decimal
             91   58
    datetime (2014-03-12T05:28:55)
    0000   0x37 0xdc 0x05 0x0c 0x0e                   7....
    body (13)
    hex
    0000   0x00 0x51 0x00 0x6e 0x1e 0x50 0x1c 0x00    .Q.n.P..
    0008   0x00 0x08 0x00 0x00 0x01                   .....
    decimal
              0   81    0  110   30   80   28    0
              0    8    0    0    1
    HOUR BITS: [1, 1, 0]
#### RECORD 7 Base (2000, 4, 8, 4, 11, 28) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x64                                  .d
    decimal
             28  100
    datetime ((2000, 4, 8, 4, 11, 28))
    0000   0x5c 0x0b 0x44 0x28 0x90                   \.D(.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 8 CalBGForPH 2001-08-16T14:02:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2001-08-16T14:02:16)
    0000   0x90 0x02 0x6e 0x90 0x01                   ..n..
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 9 Bolus (2012, 0, 23, 0, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'dual_component': '??', 'programmed': 0.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1c 0x01 0x1c                        ....
    decimal
              1   28    1   28
    datetime ((2012, 0, 23, 0, 0, 0))
    0000   0x00 0x00 0x00 0x37 0xdc                   ...7.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 10 Base (2000, 1, 0, 3, 59, 14) head[2], body[0] op[0x45]

    op hex (2)
    0000   0x45 0x0c                                  E.
    decimal
             69   12
    datetime ((2000, 1, 0, 3, 59, 14))
    0000   0x0e 0x7b 0x03 0x00 0xc0                   .{...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 11 NoDelivery (2012, 0, 0, 1, 0, 25) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x0c 0x0e 0x0c                        ....
    decimal
              6   12   14   12
    datetime ((2012, 0, 0, 1, 0, 25))
    0000   0x19 0x00 0x21 0x00 0x2c                   ..!.,
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 12 Base (2000, 0, 0, 3, 14, 12) head[2], body[0] op[0xd5]

    op hex (2)
    0000   0xd5 0x07                                  ..
    decimal
            213    7
    datetime ((2000, 0, 0, 3, 14, 12))
    0000   0x0c 0x0e 0x03 0x00 0x00                   .....
    body (0)

#### RECORD 13 Base (2014, 3, 12, 7, 22, 20) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x4c                                  .L
    decimal
              0   76
    datetime ((2014, 3, 12, 7, 22, 20))
    0000   0x14 0xd6 0x27 0x0c 0x0e                   ..'..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 BasalProfileStart 2014-03-12T07:22:35 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-12T07:22:35)
    0000   0x23 0xd6 0x07 0x0c 0x0e                   #....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 15 CalBGForPH 2014-03-12T08:05:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2014-03-12T08:05:26)
    0000   0x1a 0xc5 0x28 0x6c 0x0e                   ..(l.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 Ian3F 2014-03-12T08:05:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-03-12T08:05:26)
    0000   0x1a 0xc5 0xa8 0x6c 0x0e                   ...l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 PumpSuspend 2014-03-12T08:05:45 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-12T08:05:45)
    0000   0x2d 0xc5 0x08 0x0c 0x0e                   -....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 CalBGForPH 2014-03-12T08:36:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2014-03-12T08:36:20)
    0000   0x14 0xe4 0x28 0x6c 0x0e                   ..(l.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 Ian3F 2014-03-12T08:36:20 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-03-12T08:36:20)
    0000   0x14 0xe4 0xa8 0x6c 0x0e                   ...l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 BasalProfileStart 2014-03-12T09:27:49 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-12T09:27:49)
    0000   0x31 0xdb 0x09 0x0c 0x0e                   1....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 21 PumpResume 2014-03-12T09:27:49 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-12T09:27:49)
    0000   0x31 0xdb 0x09 0x0c 0x0e                   1....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 BolusWizard 2014-03-12T09:28:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 45,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 160}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-12T09:28:00)
    0000   0x00 0xdc 0x09 0x6c 0x0e                   ...l.
    body (13)
    hex
    0000   0x2d 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    -P.n(P..
    0008   0xa0 0x00 0x00 0x00 0x00                   .....
    decimal
             45   80    0  110   40   80    0    0
            160    0    0    0    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 Base (2000, 4, 12, 4, 8, 28) head[2], body[0] op[0xa0]

    op hex (2)
    0000   0xa0 0x64                                  .d
    decimal
            160  100
    datetime ((2000, 4, 12, 4, 8, 28))
    0000   0x5c 0x08 0x64 0xec 0x80                   \.d..
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 24 Base (2000, 8, 0, 0, 1, 0) head[2], body[0] op[0xb8]

    op hex (2)
    0000   0xb8 0xf6                                  ..
    decimal
            184  246
    datetime ((2000, 8, 0, 0, 1, 0))
    0000   0x80 0x01 0x00 0xa0 0x00                   .....
    body (0)
    DAY BITS: [1, 0, 1]
#### RECORD 25 Base (2009, 0, 28, 0, 0, 0) head[2], body[0] op[0xa0]

    op hex (2)
    0000   0xa0 0x00                                  ..
    decimal
            160    0
    datetime ((2009, 0, 28, 0, 0, 0))
    0000   0x00 0x00 0x00 0xdc 0x49                   ....I
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 26 old6c (2013, 0, 8, 1, 59, 6) head[2], body[38] op[0x6c]

    op hex (2)
    0000   0x6c 0x0e                                  l.
    decimal
            108   14
    datetime ((2013, 0, 8, 1, 59, 6))
    0000   0x06 0x3b 0x01 0x08 0x1d                   .;...
    body (38)
    hex
    0000   0xc9 0x6a 0xcc 0x0e 0x0c 0x3b 0x06 0xcb    .j...;..
    0008   0x0a 0x0c 0x0e 0x7b 0x03 0x06 0xcb 0x0a    ...{....
    0010   0x0c 0x0e 0x0c 0x19 0x00 0x7b 0x04 0x00    .....{..
    0018   0xde 0x0a 0x0c 0x0e 0x15 0x10 0x00 0x0a    ........
    0020   0x59 0x0c 0xde 0x2a 0x6c 0x0e              Y..*l.
    decimal
            201  106  204   14   12   59    6  203
             10   12   14  123    3    6  203   10
             12   14   12   25    0  123    4    0
            222   10   12   14   21   16    0   10
             89   12  222   42  108   14
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 27 Ian3F 2014-03-12T10:30:12 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-03-12T10:30:12)
    0000   0x0c 0xde 0x2a 0x6c 0x0e                   ..*l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 TempBasal 2014-03-12T10:31:09 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-12T10:31:09)
    0000   0x09 0xdf 0x0a 0x0c 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 29 TempBasalDuration 2014-03-12T10:31:09 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-12T10:31:09)
    0000   0x09 0xdf 0x0a 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 TempBasal 2014-03-12T10:31:59 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-12T10:31:59)
    0000   0x3b 0xdf 0x0a 0x0c 0x0e                   ;....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 31 TempBasalDuration 2014-03-12T10:31:59 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2014-03-12T10:31:59)
    0000   0x3b 0xdf 0x0a 0x0c 0x0e                   ;....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 32 BasalProfileStart 2014-03-12T10:31:59 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-12T10:31:59)
    0000   0x3b 0xdf 0x0a 0x0c 0x0e                   ;....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 33 ChangeTimeDisplay 2014-03-12T10:32:14 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2014-03-12T10:32:14)
    0000   0x0e 0xe0 0x0a 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 34 ChangeTime 2014-03-12T10:32:19 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2014-03-12T10:32:19)
    0000   0x13 0xe0 0x0a 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 NewTimeSet 2014-03-12T12:32:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2014-03-12T12:32:00)
    0000   0x00 0xe0 0x0c 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 TempBasal 2014-03-12T12:32:15 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-12T12:32:15)
    0000   0x0f 0xe0 0x0c 0x0c 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 37 TempBasalDuration 2014-03-12T12:32:15 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-12T12:32:15)
    0000   0x0f 0xe0 0x0c 0x0c 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 BasalProfileStart 2014-03-12T13:32:15 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-12T13:32:15)
    0000   0x0f 0xe0 0x0d 0x0c 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 39 BolusWizard 2014-03-12T14:13:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 32,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-12T14:13:20)
    0000   0x14 0xcd 0x0e 0x6c 0x0e                   ...l.
    body (13)
    hex
    0000   0x20 0x50 0x00 0x78 0x32 0x50 0x00 0x00     P.x2P..
    0008   0x68 0x00 0x00 0x00 0x00                   h....
    decimal
             32   80    0  120   50   80    0    0
            104    0    0    0    0
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 Base (2000, 4, 11, 0, 11, 28) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x64                                  hd
    decimal
            104  100
    datetime ((2000, 4, 11, 0, 11, 28))
    0000   0x5c 0x0b 0xa0 0xab 0x80                   \....
    body (0)
    DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 41 ChangeTimeDisplay (2001, 10, 16, 27, 56, 16) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x91                                  d.
    decimal
            100  145
    datetime ((2001, 10, 16, 27, 56, 16))
    0000   0x90 0xb8 0x9b 0x90 0x01                   .....
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [1, 0, 0]
#### RECORD 42 Base (2000, 1, 0, 0, 40, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x68                                  .h
    decimal
              0  104
    datetime ((2000, 1, 0, 0, 40, 0))
    0000   0x00 0x68 0x00 0x00 0x00                   .h...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 43 SelectBasalProfile 2000-05-27T14:44:14 head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0xcd                                  ..
    decimal
             20  205
    datetime (2000-05-27T14:44:14)
    0000   0x4e 0x6c 0x0e 0x5b 0x00                   Nl.[.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0]
#### RECORD 44 Base (2000, 1, 15, 14, 44, 14) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0xe8                                  ..
    decimal
             15  232
    datetime ((2000, 1, 15, 14, 44, 14))
    0000   0x0e 0x6c 0x0e 0x0f 0x50                   .l..P
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 45 Base (2000, 1, 0, 0, 16, 50) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x78                                  .x
    decimal
              0  120
    datetime ((2000, 1, 0, 0, 16, 50))
    0000   0x32 0x50 0x00 0x00 0x30                   2P..0
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-3.data: 46 records`
