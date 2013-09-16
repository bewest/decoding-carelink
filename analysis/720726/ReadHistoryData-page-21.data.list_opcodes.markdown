## START logs/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 168, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x81 0x35 0x48 0x6f 0x0d 0x7b 0x02 0x80    .5Ho.{..
    0008   0x1e 0x09 0x0f 0x0d 0x13 0x1e 0x00 0x21    .......!
    0010   0x00 0x87 0x1f 0x09 0x0f 0x0d 0x03 0x00    ........
    0018   0x00 0x00 0x2c 0x85 0x23 0x29 0x0f 0x0d    ..,.#)..
##### DEBUG DECIMAL
            129   53   72  111   13  123    2  128
             30    9   15   13   19   30    0   33
              0  135   31    9   15   13    3    0
              0    0   44  133   35   41   15   13
#### RECORD 0 Bolus 2013-08-14T22:00:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x98 0x00    ..0.0...
    decimal
              1    0   48    0   48    0  152    0
    datetime (2013-08-14T22:00:08)
    0000   0x88 0x00 0x56 0x6e 0x0d                   ..Vn.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 1 BasalProfileStart 2013-08-15T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-15T00:00:00)
    0000   0x80 0x00 0x00 0x0f 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 2 ResultTotals (2000, 8, 0, 0, 13, 14) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xff                   .....
    decimal
              7    0    0    6  255
    datetime ((2000, 8, 0, 0, 13, 14))
    0000   0x8e 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 3 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x8e 0x0d 0x06 0x00 0x92 0x4f 0xd4    n.....O.
    0008   0x02 0x00 0x00 0x06 0xff 0x03 0x89 0x33    .......3
    0010   0x03 0x76 0x31 0x00 0xc4 0x01 0xba 0x00    .v1.....
    0018   0x88 0x01 0x04 0x00 0x30 0x05 0x02 0x02    ....0...
    0020   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  142   13    6    0  146   79  212
              2    0    0    6  255    3  137   51
              3  118   49    0  196    1  186    0
            136    1    4    0   48    5    2    2
              1    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 4 CalBGForPH 2013-08-15T00:05:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2013-08-15T00:05:51)
    0000   0xb3 0x05 0x20 0x6f 0x0d                   .. o.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 5 Ian3F 2013-08-15T00:05:51 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2013-08-15T00:05:51)
    0000   0xb3 0x05 0xe0 0x6f 0x0d                   ...o.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2013-08-15T01:08:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-08-15T01:08:57)
    0000   0xb9 0x08 0x21 0x6f 0x0d                   ..!o.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2013-08-15T01:08:57 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2013-08-15T01:08:57)
    0000   0xb9 0x08 0xc1 0x6f 0x0d                   ...o.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 8 BasalProfileStart 2013-08-15T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-15T04:00:00)
    0000   0x80 0x00 0x04 0x0f 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 9 BolusWizard 2013-08-15T08:53:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 50,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 180}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-15T08:53:01)
    0000   0x81 0x35 0x08 0x6f 0x0d                   .5.o.
    body (15)
    hex
    0000   0x32 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    2..n.6..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x36         ......6
    decimal
             50  144    0  110   23   54    0    0
            180    0    0    0    0  180   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 Ian69 2013-08-15T08:53:01 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-15T08:53:01)
    0000   0x81 0x35 0x08 0x0f 0x0d                   .5...
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0xb4 0x00 0xb4 0x00    ........
    decimal
             10   30    1    0  180    0  180    0
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-21.data: 11 records`
