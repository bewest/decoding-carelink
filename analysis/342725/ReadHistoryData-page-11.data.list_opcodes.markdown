## START logs/ReadHistoryData-page-11.data
#### STOPPING DOUBLE NULLS @ 154, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x90 0x64 0x5c 0x05 0xa0 0x45 0x80 0x01    .d\..E..
    0008   0x00 0x90 0x00 0x90 0x00 0x3c 0x00 0x1c    .....<..
    0010   0xd5 0x4a 0x61 0x0e 0x0a 0x33 0x25 0xd8    .Ja..3%.
    0018   0x2a 0x61 0x8e 0x3f 0x26 0x25 0xd8 0x6a    *a.?&%.j
##### DEBUG DECIMAL
            144  100   92    5  160   69  128    1
              0  144    0  144    0   60    0   28
            213   74   97   14   10   51   37  216
             42   97  142   63   38   37  216  106
#### RECORD 0 Bolus (2006, 8, 0, 24, 0, 16) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x90 0x00                        ....
    decimal
              1    0  144    0
    datetime ((2006, 8, 0, 24, 0, 16))
    0000   0x90 0x00 0x18 0x00 0x06                   .....
    body (0)

#### RECORD 1 Base (2006, 4, 3, 10, 14, 33) head[2], body[0] op[0xd4]

    op hex (2)
    0000   0xd4 0x40                                  .@
    decimal
            212   64
    datetime ((2006, 4, 3, 10, 14, 33))
    0000   0x61 0x0e 0x0a 0x43 0x06                   a..C.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 2 Base (2006, 4, 8, 31, 14, 33) head[2], body[0] op[0xf5]

    op hex (2)
    0000   0xf5 0x20                                  . 
    decimal
            245   32
    datetime ((2006, 4, 8, 31, 14, 33))
    0000   0x61 0x0e 0x3f 0x08 0x06                   a.?..
    body (0)

#### RECORD 3 Base (2005, 4, 9, 2, 14, 33) head[2], body[0] op[0xf5]

    op hex (2)
    0000   0xf5 0x60                                  .`
    decimal
            245   96
    datetime ((2005, 4, 9, 2, 14, 33))
    0000   0x61 0x0e 0xc2 0x89 0x65                   a...e
    body (0)
    DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 BasalProfileStart 2014-03-01T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-01T02:00:00)
    0000   0x00 0xc0 0x02 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 5 BasalProfileStart 2014-03-01T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-01T04:00:00)
    0000   0x00 0xc0 0x04 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 BasalProfileStart 2014-03-01T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-01T06:00:00)
    0000   0x00 0xc0 0x06 0x01 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 7 CalBGForPH 2014-03-01T08:36:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 342}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2014-03-01T08:36:51)
    0000   0x33 0xe4 0x28 0x61 0x8e                   3.(a.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 Ian3F 2014-03-01T08:36:51 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x2a                                  ?*
    decimal
             63   42
    datetime (2014-03-01T08:36:51)
    0000   0x33 0xe4 0xc8 0x61 0x0e                   3..a.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 BolusWizard 2014-03-01T08:37:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 342,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 24.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x56                                  [V
    decimal
             91   86
    datetime (2014-03-01T08:37:33)
    0000   0x21 0xe5 0x08 0x61 0x0e                   !..a.
    body (13)
    hex
    0000   0x00 0x51 0x00 0x6e 0x28 0x50 0xf0 0x00    .Q.n(P..
    0008   0x00 0x00 0x00 0x00 0x00                   .....
    decimal
              0   81    0  110   40   80  240    0
              0    0    0    0    0
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 Base (2009, 4, 14, 2, 0, 27) head[2], body[0] op[0xf0]

    op hex (2)
    0000   0xf0 0x64                                  .d
    decimal
            240  100
    datetime ((2009, 4, 14, 2, 0, 27))
    0000   0x5b 0x00 0x02 0xce 0x09                   [....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 11 Base (2008, 1, 14, 0, 16, 45) head[2], body[0] op[0x61]

    op hex (2)
    0000   0x61 0x0e                                  a.
    decimal
             97   14
    datetime ((2008, 1, 14, 0, 16, 45))
    0000   0x2d 0x50 0x00 0x6e 0x28                   -P.n(
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 12 Ian50 (2000, 2, 0, 0, 32, 0) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x00                                  P.
    decimal
             80    0
    datetime ((2000, 2, 0, 0, 32, 0))
    0000   0x00 0xa0 0x00 0x00 0x00                   .....
    body (34)
    hex
    0000   0x00 0xa0 0x64 0x01 0x00 0xa0 0x00 0xa0    ..d.....
    0008   0x00 0x00 0x00 0x02 0xce 0x49 0x61 0x0e    .....Ia.
    0010   0x5b 0x00 0x1c 0xd5 0x0a 0x61 0x0e 0x28    [....a.(
    0018   0x50 0x00 0x6e 0x28 0x50 0x00 0x00 0x90    P.n(P...
    0020   0x00 0x00                                  ..
    decimal
              0  160  100    1    0  160    0  160
              0    0    0    2  206   73   97   14
             91    0   28  213   10   97   14   40
             80    0  110   40   80    0    0  144
              0    0
    HOUR BITS: [1, 0, 1]
`end logs/ReadHistoryData-page-11.data: 13 records`
