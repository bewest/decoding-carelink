## START logs/ReadHistoryData-page-9.data
#### STOPPING DOUBLE NULLS @ 124, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x89 0x7b 0x49 0x61 0x0d 0x34 0x01 0x80    .{Ia.4..
    0008   0x70 0x0a 0x01 0x8d 0x5b 0x00 0xb4 0x6c    p...[..l
    0010   0x0c 0x61 0x0d 0x28 0x90 0x00 0x6e 0x17    .a.(..n.
    0018   0x36 0x00 0x00 0x90 0x00 0x00 0x00 0x00    6.......
##### DEBUG DECIMAL
            137  123   73   97   13   52    1  128
            112   10    1  141   91    0  180  108
             12   97   13   40  144    0  110   23
             54    0    0  144    0    0    0    0
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x9f 0x0d 0x06 0x00 0x5c 0x00 0x00    n....\..
    0008   0x01 0x00 0x00 0x08 0x6d 0x03 0x87 0x2a    ....m..*
    0010   0x04 0xe6 0x3a 0x01 0x51 0x03 0x52 0x00    ..:.Q.R.
    0018   0x00 0x01 0x44 0x00 0x50 0x0a 0x00 0x02    ..D.P...
    0020   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x5c 0x5c 0x00 0x00 0x00         ..\\...
    decimal
            110  159   13    6    0   92    0    0
              1    0    0    8  109    3  135   42
              4  230   58    1   81    3   82    0
              0    1   68    0   80   10    0    2
              1    0    0    0    0    0    0    0
              0    0   92   92    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 BasalProfileStart 2013-09-01T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-01T04:00:00)
    0000   0x80 0x40 0x04 0x01 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [0, 1, 0]
#### RECORD 2 LowReservoir 2013-09-01T05:36:31 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.0}
```
    op hex (2)
    0000   0x34 0x0a                                  4.
    decimal
             52   10
    datetime (2013-09-01T05:36:31)
    0000   0x9f 0x64 0x05 0x01 0x8d                   .d...
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 3 BasalProfileStart 2013-09-01T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-01T09:30:00)
    0000   0x80 0x5e 0x09 0x01 0x0d                   .^...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 1, 0]
#### RECORD 4 CalBGForPH 2013-09-01T09:59:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 51}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2013-09-01T09:59:01)
    0000   0x81 0x7b 0x49 0x01 0x0d                   .{I..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2013-09-01T09:59:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 51,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 24.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x33                                  [3
    decimal
             91   51
    datetime (2013-09-01T09:59:09)
    0000   0x89 0x7b 0x09 0x61 0x0d                   .{.a.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0xf8 0x00    (..n.6..
    0008   0x90 0xf8 0x00 0x00 0x00 0x88 0x36         ......6
    decimal
             40  144    0  110   23   54  248    0
            144  248    0    0    0  136   54
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 Base (2013, 9, 1, 9, 59, 9) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime ((2013, 9, 1, 9, 59, 9))
    0000   0x89 0x7b 0x09 0x01 0x0d                   .{...
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 7 CalBGForPH (2008, 0, 0, 8, 0, 1) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 286}
```
    op hex (2)
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    datetime ((2008, 0, 0, 8, 0, 1))
    0000   0x01 0x00 0x88 0x00 0x88                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-9.data: 8 records`
