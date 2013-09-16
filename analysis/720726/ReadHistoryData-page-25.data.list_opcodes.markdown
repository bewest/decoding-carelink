## START logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 254, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x07 0x7b 0x88 0x0d 0x00 0x00 0x00 0x6e    .{.....n
    0008   0x88 0x0d 0x06 0x10 0x9f 0x5f 0x11 0x03    ....._..
    0010   0x00 0x00 0x07 0x7b 0x03 0x87 0x2f 0x03    ...{../.
    0018   0xf4 0x35 0x01 0x03 0x03 0x9c 0x00 0x58    .5.....X
##### DEBUG DECIMAL
              7  123  136   13    0    0    0  110
            136   13    6   16  159   95   17    3
              0    0    7  123    3  135   47    3
            244   53    1    3    3  156    0   88
#### RECORD 0 BolusWizard 2013-08-08T18:53:12 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-08T18:53:12)
    0000   0x8c 0x35 0x12 0x68 0x0d                   .5.h.
    body (13)
    hex
    0000   0x23 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    #..n.6..
    0008   0x7c 0x00 0x00 0x00 0x00                   |....
    decimal
             35  144    0  110   23   54    0    0
            124    0    0    0    0
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2004, 4, 28, 0, 20, 28) head[2], body[0] op[0x7c]

    op hex (2)
    0000   0x7c 0x36                                  |6
    decimal
            124   54
    datetime ((2004, 4, 28, 0, 20, 28))
    0000   0x5c 0x14 0x20 0x1c 0x04                   \. ..
    body (0)

#### RECORD 2 Base (2013, 1, 4, 16, 44, 4) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x26                                  8&
    decimal
             56   38
    datetime ((2013, 1, 4, 16, 44, 4))
    0000   0x04 0x6c 0x30 0x04 0x0d                   .l0..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 3 Base (2012, 2, 16, 4, 60, 23) head[2], body[0] op[0xb2]

    op hex (2)
    0000   0xb2 0x04                                  ..
    decimal
            178    4
    datetime ((2012, 2, 16, 4, 60, 23))
    0000   0x17 0xbc 0x04 0x50 0x5c                   ...P\
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 4 SelectBasalProfile (2000, 1, 28, 0, 60, 0) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x01                                  ..
    decimal
             20    1
    datetime ((2000, 1, 28, 0, 60, 0))
    0000   0x00 0x7c 0x00 0x7c 0x00                   .|.|.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 Base (2013, 8, 8, 18, 53, 12) head[2], body[0] op[0xb8]

    op hex (2)
    0000   0xb8 0x00                                  ..
    decimal
            184    0
    datetime ((2013, 8, 8, 18, 53, 12))
    0000   0x8c 0x35 0x52 0x68 0x0d                   .5Rh.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2013-08-08T19:08:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-08T19:08:56)
    0000   0xb8 0x08 0x13 0x68 0x0d                   ...h.
    body (13)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00                   H....
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0
    DAY BITS: [0, 1, 1]
#### RECORD 7 Base (2004, 4, 13, 18, 26, 28) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x36                                  H6
    decimal
             72   54
    datetime ((2004, 4, 13, 18, 26, 28))
    0000   0x5c 0x1a 0x12 0x0d 0x04                   \....
    body (0)

#### RECORD 8 Base (2008, 0, 4, 11, 32, 4) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x17                                  j.
    decimal
            106   23
    datetime ((2008, 0, 4, 11, 32, 4))
    0000   0x04 0x20 0x2b 0x04 0x38                   . +.8
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 9 Base (2001, 4, 13, 4, 63, 44) head[2], body[0] op[0x35]

    op hex (2)
    0000   0x35 0x04                                  5.
    decimal
             53    4
    datetime ((2001, 4, 13, 4, 63, 44))
    0000   0x6c 0x3f 0x04 0x0d 0xc1                   l?...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 10 Base (2004, 12, 11, 16, 4, 11) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x17                                  ..
    decimal
              4   23
    datetime ((2004, 12, 11, 16, 4, 11))
    0000   0xcb 0x04 0x50 0x6b 0x14                   ..Pk.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 11 Bolus (2008, 4, 0, 4, 1, 8) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x48 0x00                        ..H.
    decimal
              1    0   72    0
    datetime ((2008, 4, 0, 4, 1, 8))
    0000   0x48 0x01 0x24 0x00 0xb8                   H.$..
    body (0)
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 12 ChangeBasalProfile (2005, 4, 0, 27, 13, 40) head[2], body[42] op[0x08]

    op hex (2)
    0000   0x08 0x53                                  .S
    decimal
              8   83
    datetime ((2005, 4, 0, 27, 13, 40))
    0000   0x68 0x0d 0x5b 0x00 0xb5                   h.[..
    body (42)
    hex
    0000   0x28 0x15 0x68 0x0d 0x27 0x90 0x00 0x6e    (.h.'..n
    0008   0x17 0x36 0x00 0x00 0x8c 0x00 0x00 0x00    .6......
    0010   0x00 0x8c 0x36 0x5c 0x1a 0x48 0x9b 0x04    ..6\.H..
    0018   0x12 0xa5 0x04 0x6a 0xaf 0x04 0x20 0xc3    ...j.. .
    0020   0x04 0x38 0xcd 0x04 0x6c 0xd7 0x04 0x0d    .8..l...
    0028   0x59 0x14                                  Y.
    decimal
             40   21  104   13   39  144    0  110
             23   54    0    0  140    0    0    0
              0  140   54   92   26   72  155    4
             18  165    4  106  175    4   32  195
              4   56  205    4  108  215    4   13
             89   20
    YEAR BITS: [1, 0, 1, 1]
#### RECORD 13 ChangeTime (2000, 0, 12, 0, 1, 20) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x63                                  .c
    decimal
             23   99
    datetime ((2000, 0, 12, 0, 1, 20))
    0000   0x14 0x01 0x00 0x8c 0x00                   .....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 14 Base (2005, 4, 8, 21, 0, 0) head[2], body[0] op[0x8c]

    op hex (2)
    0000   0x8c 0x00                                  ..
    decimal
            140    0
    datetime ((2005, 4, 8, 21, 0, 0))
    0000   0x40 0x00 0xb5 0x28 0x55                   @..(U
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 15 Base (2006, 4, 21, 26, 0, 27) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x0d                                  h.
    decimal
            104   13
    datetime ((2006, 4, 21, 26, 0, 27))
    0000   0x5b 0x00 0xba 0x35 0x16                   [..5.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 16 Base (2007, 2, 14, 0, 16, 18) head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x0d                                  h.
    decimal
            104   13
    datetime ((2007, 2, 14, 0, 16, 18))
    0000   0x12 0x90 0x00 0x6e 0x17                   ...n.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 17 Base (2000, 1, 0, 0, 0, 0) head[2], body[0] op[0x36]

    op hex (2)
    0000   0x36 0x00                                  6.
    decimal
             54    0
    datetime ((2000, 1, 0, 0, 0, 0))
    0000   0x00 0x40 0x00 0x00 0x00                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 18 Base (2014, 1, 12, 29, 28, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x40                                  .@
    decimal
              0   64
    datetime ((2014, 1, 12, 29, 28, 54))
    0000   0x36 0x5c 0x1d 0x8c 0x4e                   6\..N
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 0]
#### RECORD 19 Base (2004, 12, 14, 18, 4, 36) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x48                                  .H
    decimal
              4   72
    datetime ((2004, 12, 14, 18, 4, 36))
    0000   0xe4 0x04 0x12 0xee 0x04                   .....
    body (0)
    DAY BITS: [1, 1, 1]
#### RECORD 20 Base (2008, 0, 20, 12, 32, 4) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xf8                                  j.
    decimal
            106  248
    datetime ((2008, 0, 20, 12, 32, 4))
    0000   0x04 0x20 0x0c 0x14 0x38                   . ..8
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 21 TempBasalDuration 2002-04-13T20:32:44 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 600}
```
    op hex (2)
    0000   0x16 0x14                                  ..
    decimal
             22   20
    datetime (2002-04-13T20:32:44)
    0000   0x6c 0x20 0x14 0x0d 0xa2                   l ...
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 0]
#### RECORD 22 SelectBasalProfile (2000, 8, 0, 1, 20, 44) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x17                                  ..
    decimal
             20   23
    datetime ((2000, 8, 0, 1, 20, 44))
    0000   0xac 0x14 0x01 0x00 0x40                   ....@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 23 Base (2005, 1, 26, 0, 44, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x40                                  .@
    decimal
              0   64
    datetime ((2005, 1, 26, 0, 44, 0))
    0000   0x00 0x6c 0x00 0xba 0x35                   .l..5
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 24 Base (2000, 1, 0, 0, 59, 13) head[2], body[0] op[0x56]

    op hex (2)
    0000   0x56 0x68                                  Vh
    decimal
             86  104
    datetime ((2000, 1, 0, 0, 59, 13))
    0000   0x0d 0x7b 0x00 0x80 0x00                   .{...
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0]
#### RECORD 25 Base (2007, 0, 0, 0, 0, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x09                                  ..
    decimal
              0    9
    datetime ((2007, 0, 0, 0, 0, 13))
    0000   0x0d 0x00 0x20 0x00 0x07                   .. ..
    body (0)

`end logs/ReadHistoryData-page-25.data: 26 records`
