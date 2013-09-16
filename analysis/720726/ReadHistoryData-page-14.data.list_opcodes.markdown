## START logs/ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 109, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x84 0x0a 0x4a 0x78 0x0c 0x5b 0x00 0x92    ..Jx.[..
    0008   0x2d 0x0a 0x78 0x0c 0x16 0x90 0x00 0x6e    -.x....n
    0010   0x17 0x36 0x00 0x00 0x50 0x00 0x00 0x00    .6..P...
    0018   0x00 0x50 0x36 0x5c 0x05 0x40 0x29 0x04    .P6\.@).
##### DEBUG DECIMAL
            132   10   74  120   12   91    0  146
             45   10  120   12   22  144    0  110
             23   54    0    0   80    0    0    0
              0   80   54   92    5   64   41    4
#### RECORD 0 BasalProfileStart 2012-08-24T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-24T09:30:00)
    0000   0x80 0x1e 0x09 0x18 0x0c                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 1 CalBGForPH 2012-08-24T09:35:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2012-08-24T09:35:06)
    0000   0x86 0x23 0x29 0x78 0x0c                   .#)x.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2012-08-24T09:35:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2012-08-24T09:35:06)
    0000   0x86 0x23 0x69 0x78 0x0c                   .#ix.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 NoDelivery 2012-08-24T09:39:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x06 0x08 0xb6                        ....
    decimal
              6    6    8  182
    datetime (2012-08-24T09:39:00)
    0000   0x80 0x27 0x49 0xb8 0x0c                   .'I..
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 0, 1]
#### RECORD 4 ClearAlarm 2012-08-24T09:41:08 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x06                                  ..
    decimal
             12    6
    datetime (2012-08-24T09:41:08)
    0000   0x88 0x29 0x09 0x18 0x0c                   .)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BasalProfileStart 2012-08-24T09:41:08 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2012-08-24T09:41:08)
    0000   0x88 0x29 0x09 0x18 0x0c                   .)...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 0, 1]
#### RECORD 6 CalBGForPH 2012-08-24T10:04:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 62}
```
    op hex (2)
    0000   0x0a 0x3e                                  .>
    decimal
             10   62
    datetime (2012-08-24T10:04:40)
    0000   0xa8 0x04 0x2a 0x78 0x0c                   ..*x.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2012-08-24T10:04:40 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2012-08-24T10:04:40)
    0000   0xa8 0x04 0xca 0x78 0x0c                   ...x.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 8 BolusWizard 2012-08-24T10:10:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 34,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 28,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 22.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x22                                  ["
    decimal
             91   34
    datetime (2012-08-24T10:10:04)
    0000   0x84 0x0a 0x0a 0x78 0x0c                   ...x.
    body (15)
    hex
    0000   0x1c 0x90 0x00 0x6e 0x17 0x36 0xdc 0x00    ...n.6..
    0008   0x64 0xf8 0x00 0x00 0x00 0x40 0x36         d....@6
    decimal
             28  144    0  110   23   54  220    0
            100  248    0    0    0   64   54
    DAY BITS: [0, 1, 1]
#### RECORD 9 Ian69 2012-08-24T10:10:04 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2012-08-24T10:10:04)
    0000   0x84 0x0a 0x0a 0x18 0x0c                   .....
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x40 0x00 0x40 0x00    ....@.@.
    decimal
             10   30    1    0   64    0   64    0

`end logs/ReadHistoryData-page-14.data: 10 records`
