## START logs/ReadHistoryData-page-24.data
#### STOPPING DOUBLE NULLS @ 281, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x8e 0x17 0x4b 0x6a 0x0d 0x7b 0x03 0x80    ..Kj.{..
    0008   0x00 0x0d 0x0a 0x0d 0x1a 0x26 0x00 0x5b    .....&.[
    0010   0x00 0x9e 0x0b 0x0e 0x6a 0x0d 0x23 0x90    ....j.#.
    0018   0x00 0x6e 0x17 0x36 0x00 0x00 0x7c 0x00    .n.6..|.
##### DEBUG DECIMAL
            142   23   75  106   13  123    3  128
              0   13   10   13   26   38    0   91
              0  158   11   14  106   13   35  144
              0  110   23   54    0    0  124    0
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x89 0x0d 0x06 0x10 0x9d 0x50 0x01    n.....P.
    0008   0x08 0x00 0x00 0x06 0xcd 0x03 0x89 0x34    .......4
    0010   0x03 0x44 0x30 0x00 0xbe 0x01 0xec 0x00    .D0.....
    0018   0x70 0x00 0xe8 0x00 0x00 0x07 0x02 0x01    p.......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  137   13    6   16  157   80    1
              8    0    0    6  205    3  137   52
              3   68   48    0  190    1  236    0
            112    0  232    0    0    7    2    1
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 BolusWizard 2013-08-10T00:48:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-10T00:48:29)
    0000   0x9d 0x30 0x00 0x6a 0x0d                   .0.j.
    body (15)
    hex
    0000   0x12 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x36         @....@6
    decimal
             18  144    0  110   23   54    0    0
             64    0    0    0    0   64   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 2.4, 'curve': 4},
 {'age': 143, 'amount': 1.4, 'curve': 4},
 {'age': 243, 'amount': 5.8, 'curve': 4},
 {'age': 147, 'amount': 1.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x60 0x67 0x04 0x38 0x8f 0x04    \.`g.8..
    0008   0xe8 0xf3 0x04 0x2c 0x93 0x14              ...,..
    decimal
             92   14   96  103    4   56  143    4
            232  243    4   44  147   20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2013-08-10T00:48:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x4c 0x00    ..@.@.L.
    decimal
              1    0   64    0   64    0   76    0
    datetime (2013-08-10T00:48:29)
    0000   0x9d 0x30 0x40 0x6a 0x0d                   .0@j.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 CalBGForPH 2013-08-10T01:21:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-08-10T01:21:45)
    0000   0xad 0x15 0x21 0x6a 0x0d                   ..!j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 5 Ian3F 2013-08-10T01:21:45 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2013-08-10T01:21:45)
    0000   0xad 0x15 0x01 0x6a 0x0d                   ...j.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2013-08-10T01:22:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 75,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 10.4,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 3.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-08-10T01:22:09)
    0000   0x89 0x16 0x01 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x24 0x00    ...n.6$.
    0008   0x48 0x00 0x00 0x68 0x00 0x48 0x36         H..h.H6
    decimal
             20  144    0  110   23   54   36    0
             72    0    0  104    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 1.6, 'curve': 4},
 {'age': 137, 'amount': 2.4, 'curve': 4},
 {'age': 177, 'amount': 1.4, 'curve': 4},
 {'age': 21, 'amount': 5.8, 'curve': 20},
 {'age': 181, 'amount': 1.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x40 0x25 0x04 0x60 0x89 0x04    \.@%.`..
    0008   0x38 0xb1 0x04 0xe8 0x15 0x14 0x2c 0xb5    8.....,.
    0010   0x14                                       .
    decimal
             92   17   64   37    4   96  137    4
             56  177    4  232   21   20   44  181
             20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-08-10T01:22:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x68 0x00    ..0.0.h.
    decimal
              1    0   48    0   48    0  104    0
    datetime (2013-08-10T01:22:09)
    0000   0x89 0x16 0x41 0x6a 0x0d                   ..Aj.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 9 BasalProfileStart 2013-08-10T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-10T04:00:00)
    0000   0x80 0x00 0x04 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 10 BasalProfileStart 2013-08-10T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-10T09:30:00)
    0000   0x80 0x1e 0x09 0x0a 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 11 Ian69 2013-08-10T10:30:00 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-10T10:30:00)
    0000   0x80 0x1e 0x0a 0x0a 0x0d                   .....
    body (8)
    hex
    0000   0x2a 0x1e 0x0a 0x3b 0x9f 0x2d 0x2a 0x6a    *..;.-*j
    decimal
             42   30   10   59  159   45   42  106

#### RECORD 12 Base (2010, 2, 10, 13, 31, 7) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2010, 2, 10, 13, 31, 7))
    0000   0x07 0x9f 0x2d 0x6a 0x6a                   ..-jj
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 13 Base (2008, 6, 6, 6, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2008, 6, 6, 6, 22, 41))
    0000   0x69 0x96 0x06 0x06 0x08                   i....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 14 Base (2012, 1, 13, 10, 11, 22) head[2], body[0] op[0xb6]

    op hex (2)
    0000   0xb6 0x80                                  ..
    decimal
            182  128
    datetime ((2012, 1, 13, 10, 11, 22))
    0000   0x16 0x4b 0xaa 0x0d 0x0c                   .K...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 15 NoDelivery (2003, 0, 2, 27, 13, 10) head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x83 0x17 0x0b                        ....
    decimal
              6  131   23   11
    datetime ((2003, 0, 2, 27, 13, 10))
    0000   0x0a 0x0d 0x7b 0x02 0x83                   ..{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 16 ChangeTime (2000, 0, 30, 19, 13, 10) head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x0b                                  ..
    decimal
             23   11
    datetime ((2000, 0, 30, 19, 13, 10))
    0000   0x0a 0x0d 0x13 0x1e 0x00                   .....
    body (0)

#### RECORD 17 BolusWizard 2013-08-10T11:23:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-10T11:23:14)
    0000   0x8e 0x17 0x0b 0x6a 0x0d                   ...j.
    body (15)
    hex
    0000   0x21 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    !..n.6..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x36         x....x6
    decimal
             33  144    0  110   23   54    0    0
            120    0    0    0    0  120   54
    DAY BITS: [0, 1, 1]
#### RECORD 18 Ian69 2013-08-10T11:23:14 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-10T11:23:14)
    0000   0x8e 0x17 0x0b 0x0a 0x0d                   .....
    body (8)
    hex
    0000   0x0e 0x1e 0x01 0x00 0x78 0x00 0x78 0x00    ....x.x.
    decimal
             14   30    1    0  120    0  120    0

`end logs/ReadHistoryData-page-24.data: 19 records`
