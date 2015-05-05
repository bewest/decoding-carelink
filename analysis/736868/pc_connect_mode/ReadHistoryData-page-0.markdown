## START ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 197, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x78 0x5c 0x23 0x06 0x80 0x04 0x08 0x8a    x\#.....
    0008   0x04 0x08 0x94 0x04 0x06 0x9e 0x04 0x08    ........
    0010   0xa8 0x04 0x08 0xb2 0x04 0x08 0xbc 0x04    ........
    0018   0x08 0xc6 0x04 0x08 0xd0 0x04 0xb8 0xda    ........
##### DEBUG DECIMAL
            120   92   35    6  128    4    8  138
              4    8  148    4    6  158    4    8
            168    4    8  178    4    8  188    4
              8  198    4    8  208    4  184  218
#### RECORD 0 BasalProfileStart 2015-04-12T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-04-12T12:00:00)
    0000   0x40 0x00 0x0c 0x0c 0x0f                   @....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 1 BasalProfileStart 2015-04-12T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-04-12T15:00:00)
    0000   0x40 0x00 0x0f 0x0c 0x0f                   @....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 2 CalBGForPH 2015-04-12T16:15:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 295}
```
    op hex (2)
    0000   0x0a 0x27                                  .'
    decimal
             10   39
    datetime (2015-04-12T16:15:49)
    0000   0x71 0x0f 0x30 0x6c 0x8f                   q.0l.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 Ian3F 2015-04-12T16:15:49 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x24                                  ?$
    decimal
             63   36
    datetime (2015-04-12T16:15:49)
    0000   0x71 0x0f 0xf0 0x6c 0x0f                   q..l.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54
    DAY BITS: [0, 1, 1]
#### RECORD 4 BolusWizard 2015-04-12T16:16:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 90,
 '_byte[7]': 0,
 'bg': 295,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 1.0,
 'food_estimate': 17.2,
 'sensitivity': 80,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x27                                  ['
    decimal
             91   39
    datetime (2015-04-12T16:16:01)
    0000   0x41 0x10 0x10 0x0c 0x0f                   A....
    body (13)
    hex
    0000   0x00 0x51 0x00 0x50 0x28 0x5a 0xac 0x00    .Q.P(Z..
    0008   0x00 0x00 0x00 0x00 0x00                   .....
    decimal
              0   81    0   80   40   90  172    0
              0    0    0    0    0

#### RECORD 5 Base (2004, 4, 5, 4, 11, 28) head[2], body[0] op[0xac]

    op hex (2)
    0000   0xac 0x78                                  .x
    decimal
            172  120
    datetime ((2004, 4, 5, 4, 11, 28))
    0000   0x5c 0x0b 0x64 0x65 0x14                   \.de.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 6 OldBolusWizardChange 2001-01-20T21:50:20 head[2], body[117] op[0x5a]

    op hex (2)
    0000   0x5a 0xab                                  Z.
    decimal
             90  171
    datetime (2001-01-20T21:50:20)
    0000   0x14 0x72 0xb5 0x14 0x01                   .r...
    body (117)
    hex
    0000   0x00 0xac 0x00 0xac 0x00 0x00 0x00 0x41    .......A
    0008   0x10 0x50 0x0c 0x0f 0x5b 0x00 0x63 0x1e    .P..[.c.
    0010   0x12 0x6c 0x0f 0x37 0x50 0x00 0x3c 0x28    .l.7P.<(
    0018   0x5a 0x00 0x01 0x6c 0x00 0x00 0x00 0x01    Z..l....
    0020   0x6c 0x78 0x5c 0x05 0xac 0x8d 0x04 0x01    lx\.....
    0028   0x00 0x8c 0x00 0x48 0x00 0x3c 0x06 0x63    ...H.<.c
    0030   0x21 0xb2 0x6c 0x0f 0x01 0x00 0xb4 0x00    !.l.....
    0038   0xb4 0x00 0x3c 0x00 0x63 0x1e 0x92 0x6c    ..<.c..l
    0040   0x0f 0x1e 0x01 0x4c 0x07 0x14 0x0c 0x0f    ...L....
    0048   0x7b 0x05 0x52 0x07 0x14 0x0c 0x0f 0x1e    {.R.....
    0050   0x20 0x00 0x1f 0x20 0x52 0x07 0x14 0x0c     .. R...
    0058   0x0f 0x62 0x00 0x58 0x2b 0x15 0x0c 0x0f    .b.X+...
    0060   0x7b 0x06 0x40 0x00 0x16 0x0c 0x0f 0x2c    {.@....,
    0068   0x24 0x00 0x5b 0x00 0x47 0x07 0x16 0x6c    $.[.G..l
    0070   0x0f 0x00 0x50 0x00 0x3c                   ..P.<
    decimal
              0  172    0  172    0    0    0   65
             16   80   12   15   91    0   99   30
             18  108   15   55   80    0   60   40
             90    0    1  108    0    0    0    1
            108  120   92    5  172  141    4    1
              0  140    0   72    0   60    6   99
             33  178  108   15    1    0  180    0
            180    0   60    0   99   30  146  108
             15   30    1   76    7   20   12   15
            123    5   82    7   20   12   15   30
             32    0   31   32   82    7   20   12
             15   98    0   88   43   21   12   15
            123    6   64    0   22   12   15   44
             36    0   91    0   71    7   22  108
             15    0   80    0   60
    HOUR BITS: [0, 1, 1]
#### RECORD 7 Base (2000, 0, 0, 0, 0, 0) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x5a                                  (Z
    decimal
             40   90
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

`end ReadHistoryData-page-0.data: 8 records`
