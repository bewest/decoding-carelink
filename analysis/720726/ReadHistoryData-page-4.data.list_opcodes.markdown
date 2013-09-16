## START logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 194, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x38 0x36 0x5c 0x05 0x74 0xd7 0x14 0x01    86\.t...
    0008   0x00 0x38 0x00 0x38 0x00 0x00 0x00 0xaa    .8.8....
    0010   0x7b 0x47 0x68 0x0d 0x5b 0x00 0x86 0x41    {Gh.[..A
    0018   0x09 0x68 0x0d 0x1c 0x90 0x00 0x6e 0x17    .h....n.
##### DEBUG DECIMAL
             56   54   92    5  116  215   20    1
              0   56    0   56    0    0    0  170
            123   71  104   13   91    0  134   65
              9  104   13   28  144    0  110   23
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x87 0x8d 0x06 0x10 0xa3 0x41 0x1d    n.....A.
    0008   0x08 0x00 0x00 0x08 0x7e 0x04 0xf6 0x3a    ....~..:
    0010   0x03 0x88 0x2a 0x00 0x92 0x02 0x08 0x01    ..*.....
    0018   0x80 0x00 0x00 0x00 0x00 0x06 0x03 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  135  141    6   16  163   65   29
              8    0    0    8  126    4  246   58
              3  136   42    0  146    2    8    1
            128    0    0    0    0    6    3    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 CalBGForPH 2013-09-08T00:06:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 219}
```
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2013-09-08T00:06:59)
    0000   0xbb 0x46 0x20 0x68 0x0d                   .F h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2013-09-08T00:06:59 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2013-09-08T00:06:59)
    0000   0xbb 0x46 0x60 0x68 0x0d                   .F`h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2013-09-08T00:10:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 122,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 11.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7a                                  [z
    decimal
             91  122
    datetime (2013-09-08T00:10:08)
    0000   0x88 0x4a 0x00 0x68 0x0d                   .J.h.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x74 0x00    ...n.6t.
    0008   0x00 0x00 0x00 0x00 0x00 0x74 0x36         .....t6
    decimal
              0  144    0  110   23   54  116    0
              0    0    0    0    0  116   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 4.2, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xa8 0x06 0x14                   \....
    decimal
             92    5  168    6   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-09-08T00:10:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2013-09-08T00:10:08)
    0000   0x88 0x4a 0x40 0x68 0x0d                   .J@h.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 BasalProfileStart 2013-09-08T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-08T04:00:00)
    0000   0x80 0x40 0x04 0x08 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-09-08T07:59:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2013-09-08T07:59:05)
    0000   0x85 0x7b 0x27 0x68 0x0d                   .{'h.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2013-09-08T07:59:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2013-09-08T07:59:05)
    0000   0x85 0x7b 0xa7 0x68 0x0d                   .{.h.
    body (3)
    hex
    0000   0x72 0x90 0x70                             r.p
    decimal
            114  144  112
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 Base (2013, 9, 8, 7, 59, 23) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x00                                  P.
    decimal
             80    0
    datetime ((2013, 9, 8, 7, 59, 23))
    0000   0x97 0x7b 0x07 0x08 0x0d                   .{...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 10 Base (2000, 0, 20, 28, 0, 30) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x01                                  @.
    decimal
             64    1
    datetime ((2000, 0, 20, 28, 0, 30))
    0000   0x1e 0x00 0x3c 0x14 0x00                   ..<..
    body (0)

#### RECORD 11 PumpSuspend 2007-02-04T08:26:36 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x3c                                  .<
    decimal
             30   60
    datetime (2007-02-04T08:26:36)
    0000   0x24 0x9a 0xc8 0x64 0x27                   $..d'
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 12 Base (2000, 1, 30, 1, 1, 33) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x80                                  ..
    decimal
              0  128
    datetime ((2000, 1, 30, 1, 1, 33))
    0000   0x21 0x41 0x01 0x1e 0x00                   !A...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 13 Base (2010, 0, 4, 28, 30, 0) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x14                                  <.
    decimal
             60   20
    datetime ((2010, 0, 4, 28, 30, 0))
    0000   0x00 0x1e 0x3c 0x24 0x9a                   ..<$.
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 14 Base (2011, 0, 1, 0, 0, 39) head[2], body[0] op[0xc8]

    op hex (2)
    0000   0xc8 0x64                                  .d
    decimal
            200  100
    datetime ((2011, 0, 1, 0, 0, 39))
    0000   0x27 0x00 0x80 0x21 0x5b                   '..![
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 15 Base (2000, 4, 13, 8, 7, 59) head[2], body[0] op[0x57]

    op hex (2)
    0000   0x57 0xaa                                  W.
    decimal
             87  170
    datetime ((2000, 4, 13, 8, 7, 59))
    0000   0x7b 0x07 0x68 0x0d 0x00                   {.h..
    body (0)

#### RECORD 16 Base (2000, 4, 24, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 24, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x38 0x00                   n.68.
    body (0)
    DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-4.data: 17 records`
