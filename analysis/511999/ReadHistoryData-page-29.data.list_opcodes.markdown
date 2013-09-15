## START logs/ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 176, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0xb4 0x6c 0x8d 0x00 0x00 0x00 0x6e    ..l....n
    0008   0x6c 0x8d 0x05 0x00 0xc6 0x00 0x00 0x07    l.......
    0010   0x00 0x00 0x04 0xb4 0x02 0xd4 0x3c 0x01    ......<.
    0018   0xe0 0x28 0x00 0x44 0x00 0xa8 0x00 0x94    .(.D....
##### DEBUG DECIMAL
              4  180  108  141    0    0    0  110
            108  141    5    0  198    0    0    7
              0    0    4  180    2  212   60    1
            224   40    0   68    0  168    0  148
#### RECORD 0 BolusWizard 2013-07-12T19:53:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-07-12T19:53:13)
    0000   0x4d 0xf5 0x13 0x6c 0x0d                   M..l.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x2c 0x00    .P.d<d,.
    0008   0x00 0x00 0x00 0x34 0x00 0x00 0x78         ...4..x
    decimal
              0   80    0  100   60  100   44    0
              0    0    0   52    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 1.1, 'curve': 192},
 {'age': 120, 'amount': 0.05, 'curve': 192},
 {'age': 130, 'amount': 1.35, 'curve': 192},
 {'age': 220, 'amount': 0.2, 'curve': 192},
 {'age': 230, 'amount': 2.2, 'curve': 192},
 {'age': 144, 'amount': 1.7, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x2c 0x28 0xc0 0x02 0x78 0xc0    \.,(..x.
    0008   0x36 0x82 0xc0 0x08 0xdc 0xc0 0x58 0xe6    6.....X.
    0010   0xc0 0x44 0x90 0xd0                        .D..
    decimal
             92   20   44   40  192    2  120  192
             54  130  192    8  220  192   88  230
            192   68  144  208
    datetime (unknown)

    body (0)

#### RECORD 2 CalBGForPH 2013-07-12T22:04:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 243}
```
    op hex (2)
    0000   0x0a 0xf3                                  ..
    decimal
             10  243
    datetime (2013-07-12T22:04:31)
    0000   0x5f 0xc4 0x36 0x0c 0x0d                   _.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BolusWizard 2013-07-12T22:04:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 243,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0xf3                                  [.
    decimal
             91  243
    datetime (2013-07-12T22:04:40)
    0000   0x68 0xc4 0x16 0x6c 0x0d                   h..l.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x50 0x00    .P.d<dP.
    0008   0x58 0x00 0x00 0x04 0x00 0xa4 0x78         X.....x
    decimal
             22   80    0  100   60  100   80    0
             88    0    0    4    0  164  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 171, 'amount': 1.1, 'curve': 192},
 {'age': 251, 'amount': 0.05, 'curve': 192},
 {'age': 5, 'amount': 1.35, 'curve': 208},
 {'age': 95, 'amount': 0.2, 'curve': 208},
 {'age': 105, 'amount': 2.2, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x2c 0xab 0xc0 0x02 0xfb 0xc0    \.,.....
    0008   0x36 0x05 0xd0 0x08 0x5f 0xd0 0x58 0x69    6..._.Xi
    0010   0xd0                                       .
    decimal
             92   17   44  171  192    2  251  192
             54    5  208    8   95  208   88  105
            208
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus (2008, 8, 0, 4, 0, 36) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0xa4 0x00                        ....
    decimal
              1    0  164    0
    datetime ((2008, 8, 0, 4, 0, 36))
    0000   0xa4 0x00 0x04 0x00 0x68                   ....h
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 6 Base (2002, 4, 25, 10, 13, 44) head[2], body[0] op[0xc4]

    op hex (2)
    0000   0xc4 0x56                                  .V
    decimal
            196   86
    datetime ((2002, 4, 25, 10, 13, 44))
    0000   0x6c 0x0d 0x0a 0x39 0x72                   l..9r
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 7 Base (2011, 2, 25, 27, 13, 12) head[2], body[0] op[0xd2]

    op hex (2)
    0000   0xd2 0x36                                  .6
    decimal
            210   54
    datetime ((2011, 2, 25, 27, 13, 12))
    0000   0x0c 0x8d 0x5b 0x39 0x7b                   ..[9{
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 8 Base (2000, 4, 17, 0, 13, 44) head[2], body[0] op[0xd2]

    op hex (2)
    0000   0xd2 0x16                                  ..
    decimal
            210   22
    datetime ((2000, 4, 17, 0, 13, 44))
    0000   0x6c 0x0d 0x00 0x51 0x00                   l..Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 9 ChangeTimeDisplay (2000, 6, 0, 0, 0, 36) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x3c                                  d<
    decimal
            100   60
    datetime ((2000, 6, 0, 0, 0, 36))
    0000   0x64 0x80 0x00 0x00 0x00                   d....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 Base (2004, 0, 28, 24, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xa0                                  ..
    decimal
              0  160
    datetime ((2004, 0, 28, 24, 0, 0))
    0000   0x00 0x00 0x78 0x5c 0x14                   ..x\.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 11 Base (2002, 12, 0, 25, 44, 0) head[2], body[0] op[0xa4]

    op hex (2)
    0000   0xa4 0x0f                                  ..
    decimal
            164   15
    datetime ((2002, 12, 0, 25, 44, 0))
    0000   0xc0 0x2c 0xb9 0xc0 0x02                   .,...
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0]
#### RECORD 12 Base (2013, 0, 8, 16, 19, 54) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0xd0                                  ..
    decimal
              9  208
    datetime ((2013, 0, 8, 16, 19, 54))
    0000   0x36 0x13 0xd0 0x08 0x6d                   6...m
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 13 Base (2004, 7, 0, 1, 16, 55) head[2], body[0] op[0xd0]

    op hex (2)
    0000   0xd0 0x58                                  .X
    decimal
            208   88
    datetime ((2004, 7, 0, 1, 16, 55))
    0000   0x77 0xd0 0x01 0x00 0x34                   w...4
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 14 Base (2002, 2, 27, 0, 32, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x34                                  .4
    decimal
              0   52
    datetime ((2002, 2, 27, 0, 32, 0))
    0000   0x00 0xa0 0x00 0x7b 0xd2                   ...{.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 15 Base (2000, 1, 0, 0, 59, 13) head[2], body[0] op[0x56]

    op hex (2)
    0000   0x56 0x6c                                  Vl
    decimal
             86  108
    datetime ((2000, 1, 0, 0, 59, 13))
    0000   0x0d 0x7b 0x00 0x40 0xc0                   .{.@.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 16 Base (2007, 0, 0, 28, 0, 13) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0d                                  ..
    decimal
              0   13
    datetime ((2007, 0, 0, 28, 0, 13))
    0000   0x0d 0x00 0x1c 0x00 0x07                   .....
    body (0)

`end logs/ReadHistoryData-page-29.data: 17 records`
