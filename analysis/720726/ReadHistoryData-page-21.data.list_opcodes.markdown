## START analysis/ianj/raw/ReadHistoryData-page-21.data
#### STOPPING DOUBLE NULLS @ 980, found 42 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x46 0x35                                  F5
##### DEBUG DECIMAL
             70   53
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

#### RECORD 2 MResultTotals 2013-08-15T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xff                   .....
    decimal
              7    0    0    6  255
    datetime (2013-08-15T00:00:00)
    0000   0x8e 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 3 Sara6E 2013-08-15T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-15T00:00:00)
    0000   0x8e 0x0d                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x92 0x4f 0xd4 0x02 0x00 0x00    ...O....
    0008   0x06 0xff 0x03 0x89 0x33 0x03 0x76 0x31    ....3.v1
    0010   0x00 0xc4 0x01 0xba 0x00 0x88 0x01 0x04    ........
    0018   0x00 0x30 0x05 0x02 0x02 0x01 0x00 0x00    .0......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6    0  146   79  212    2    0    0
              6  255    3  137   51    3  118   49
              0  196    1  186    0  136    1    4
              0   48    5    2    2    1    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

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
#### RECORD 10 Ian69 2013-08-15T08:53:01 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-15T08:53:01)
    0000   0x81 0x35 0x08 0x0f 0x0d                   .5...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 0, 1]
#### RECORD 11 Bolus 2013-08-15T08:53:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 18.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x00 0x00    ........
    decimal
              1    0  180    0  180    0    0    0
    datetime (2013-08-15T08:53:01)
    0000   0x81 0x35 0x48 0x6f 0x0d                   .5Ho.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 BasalProfileStart 2013-08-15T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-15T09:30:00)
    0000   0x80 0x1e 0x09 0x0f 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 13 Rewind 2013-08-15T09:31:07 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-15T09:31:07)
    0000   0x87 0x1f 0x09 0x0f 0x0d                   .....
    body (0)

#### RECORD 14 Prime 2013-08-15T09:35:05 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2c                   ....,
    decimal
              3    0    0    0   44
    datetime (2013-08-15T09:35:05)
    0000   0x85 0x23 0x29 0x0f 0x0d                   .#)..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 BasalProfileStart 2013-08-15T09:35:54 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-15T09:35:54)
    0000   0xb6 0x23 0x09 0x0f 0x0d                   .#...
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [0, 0, 1]
#### RECORD 16 Prime 2013-08-15T09:35:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-15T09:35:19)
    0000   0x93 0x23 0x09 0x0f 0x0d                   .#...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 CalBGForPH 2013-08-15T12:02:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 222}
```
    op hex (2)
    0000   0x0a 0xde                                  ..
    decimal
             10  222
    datetime (2013-08-15T12:02:53)
    0000   0xb5 0x02 0x2c 0x6f 0x0d                   ..,o.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 18 Ian3F 2013-08-15T12:02:53 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2013-08-15T12:02:53)
    0000   0xb5 0x02 0xcc 0x6f 0x0d                   ...o.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 19 BolusWizard 2013-08-15T12:03:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 123,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.4,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 12.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2013-08-15T12:03:01)
    0000   0x81 0x03 0x0c 0x6f 0x0d                   ...o.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x78 0x00    ...n.6x.
    0008   0x48 0x00 0x00 0x18 0x00 0xa8 0x36         H.....6
    decimal
             20  144    0  110   23   54  120    0
             72    0    0   24    0  168   54
    DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 188, 'amount': 1.6, 'curve': 4},
 {'age': 198, 'amount': 2.9, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x40 0xbc 0x04 0x74 0xc6 0x04    \.@..t..
    decimal
             92    8   64  188    4  116  198    4
    datetime (unknown)

    body (0)

#### RECORD 21 Ian69 2013-08-15T12:03:01 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-15T12:03:01)
    0000   0x81 0x03 0x0c 0x0f 0x0d                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 22 Bolus 2013-08-15T12:03:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x18 0x00    ........
    decimal
              1    0  168    0  168    0   24    0
    datetime (2013-08-15T12:03:01)
    0000   0x81 0x03 0x4c 0x6f 0x0d                   ..Lo.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 23 BasalProfileStart 2013-08-15T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-15T13:00:00)
    0000   0x80 0x00 0x0d 0x0f 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 24 CalBGForPH 2013-08-15T15:55:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-08-15T15:55:49)
    0000   0xb1 0x37 0x2f 0x6f 0x0d                   .7/o.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 Ian3F 2013-08-15T15:55:49 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-08-15T15:55:49)
    0000   0xb1 0x37 0x0f 0x6f 0x0d                   .7.o.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 Ian69 2013-08-15T21:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-15T21:30:00)
    0000   0x80 0x1e 0x75 0x0f 0x0d                   ..u..
    body (2)
    hex
    0000   0x35 0x1e                                  5.
    decimal
             53   30

#### RECORD 27 BolusWizard 2013-08-15T22:38:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 41,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 148}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-15T22:38:29)
    0000   0x9d 0x26 0x16 0x6f 0x0d                   .&.o.
    body (15)
    hex
    0000   0x29 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    )..n.6..
    0008   0x94 0x00 0x00 0x00 0x00 0x94 0x36         ......6
    decimal
             41  144    0  110   23   54    0    0
            148    0    0    0    0  148   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 28 Bolus 2013-08-15T22:38:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 24.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xf4 0x00 0xf4 0x00 0x00 0x00    ........
    decimal
              1    0  244    0  244    0    0    0
    datetime (2013-08-15T22:38:29)
    0000   0x9d 0x26 0x56 0x6f 0x0d                   .&Vo.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 29 BasalProfileStart 2013-08-16T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-16T00:00:00)
    0000   0x80 0x00 0x00 0x10 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 30 MResultTotals 2013-08-16T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xd7                   .....
    decimal
              7    0    0    5  215
    datetime (2013-08-16T00:00:00)
    0000   0x8f 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 31 Sara6E 2013-08-16T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-16T00:00:00)
    0000   0x8f 0x0d                                  ..
    body (49)
    hex
    0000   0x06 0x00 0x85 0x4f 0xde 0x04 0x00 0x00    ...O....
    0008   0x05 0xd7 0x03 0x87 0x3c 0x02 0x50 0x28    ....<.P(
    0010   0x00 0x6f 0x00 0xb4 0x00 0x00 0x01 0x9c    .o......
    0018   0x00 0x00 0x01 0x00 0x02 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              6    0  133   79  222    4    0    0
              5  215    3  135   60    2   80   40
              0  111    0  180    0    0    1  156
              0    0    1    0    2    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 32 CalBGForPH 2013-08-16T00:24:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 6}
```
    op hex (2)
    0000   0x0a 0x06                                  ..
    decimal
             10    6
    datetime (2013-08-16T00:24:27)
    0000   0x9b 0x18 0xa0 0x70 0x0d                   ...p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 33 Ian3F 2013-08-16T00:24:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x40                                  ?@
    decimal
             63   64
    datetime (2013-08-16T00:24:27)
    0000   0x9b 0x18 0xc0 0x70 0x0d                   ...p.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 34 BolusWizard 2013-08-16T00:24:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 288,
 'bg_target_high': 1,
 'bg_target_low': 23,
 'bolus_estimate': 13.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 14.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x20                                  [ 
    decimal
             91   32
    datetime (2013-08-16T00:24:35)
    0000   0xa3 0x18 0x00 0x70 0x0d                   ...p.
    body (15)
    hex
    0000   0x00 0x91 0x00 0x6e 0x17 0x36 0x94 0x00    ...n.6..
    0008   0x00 0x08 0x00 0x84 0x01 0x10 0x36         ......6
    decimal
              0  145    0  110   23   54  148    0
              0    8    0  132    1   16   54
    DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 6.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xf4 0x6d 0x04                   \..m.
    decimal
             92    5  244  109    4
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2013-08-16T00:24:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x10 0x01 0x10 0x00 0x84 0x00    ........
    decimal
              1    1   16    1   16    0  132    0
    datetime (2013-08-16T00:24:36)
    0000   0xa4 0x18 0x40 0x70 0x0d                   ..@p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 37 Bolus 2013-08-16T00:29:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x01 0x8c 0x00    ..H.H...
    decimal
              1    0   72    0   72    1  140    0
    datetime (2013-08-16T00:29:31)
    0000   0x9f 0x1d 0x40 0x70 0x0d                   ..@p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 38 BolusWizard 2013-08-16T03:11:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-16T03:11:53)
    0000   0xb5 0x0b 0x03 0x70 0x0d                   ...p.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 166, 'amount': 1.6, 'curve': 5},
 {'age': 176, 'amount': 0.6, 'curve': 4},
 {'age': 20, 'amount': 6.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0xa6 0x05 0x18 0xb0 0x04    \.@.....
    0008   0xf4 0x14 0x14                             ...
    decimal
             92   11   64  166    5   24  176    4
            244   20   20
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-08-16T03:11:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x4c 0x00    ......L.
    decimal
              1    0  156    0  156    0   76    0
    datetime (2013-08-16T03:11:53)
    0000   0xb5 0x0b 0x43 0x70 0x0d                   ..Cp.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 41 BasalProfileStart 2013-08-16T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-16T04:00:00)
    0000   0x80 0x00 0x04 0x10 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 42 CalBGForPH 2013-08-16T07:15:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-08-16T07:15:09)
    0000   0x89 0x0f 0x27 0x70 0x0d                   ..'p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 43 Ian3F 2013-08-16T07:15:09 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2013-08-16T07:15:09)
    0000   0x89 0x0f 0x47 0x70 0x0d                   ..Gp.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 44 BasalProfileStart 2013-08-16T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-16T09:30:00)
    0000   0x80 0x1e 0x09 0x10 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 45 Ian69 2013-08-16T10:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-16T10:30:00)
    0000   0x80 0x1e 0x0a 0x10 0x0d                   .....
    body (2)
    hex
    0000   0x2a 0x1e                                  *.
    decimal
             42   30

#### RECORD 46 CalBGForPH 2013-08-16T11:32:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 312}
```
    op hex (2)
    0000   0x0a 0x38                                  .8
    decimal
             10   56
    datetime (2013-08-16T11:32:59)
    0000   0xbb 0x20 0x2b 0x70 0x8d                   . +p.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 47 Ian3F 2013-08-16T11:32:59 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x27                                  ?'
    decimal
             63   39
    datetime (2013-08-16T11:32:59)
    0000   0xbb 0x20 0x0b 0x70 0x0d                   . .p.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2013-08-16T11:33:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 173,
 'bg_target_high': 1,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 20.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2013-08-16T11:33:26)
    0000   0x9a 0x21 0x0b 0x70 0x0d                   .!.p.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0xcc 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x01 0x18 0x36         L.....6
    decimal
             21  144    0  110   23   54  204    0
             76    0    0    0    1   24   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 Ian69 2013-08-16T11:33:26 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-16T11:33:26)
    0000   0x9a 0x21 0x0b 0x10 0x0d                   .!...
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [0, 0, 1]
#### RECORD 50 Bolus 2013-08-16T11:33:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x00 0x00    ........
    decimal
              1    1   24    1   24    0    0    0
    datetime (2013-08-16T11:33:26)
    0000   0x9a 0x21 0x4b 0x70 0x0d                   .!Kp.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 BasalProfileStart 2013-08-16T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-16T13:00:00)
    0000   0x80 0x00 0x0d 0x10 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 52 CalBGForPH 2013-08-16T13:37:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 129}
```
    op hex (2)
    0000   0x0a 0x81                                  ..
    decimal
             10  129
    datetime (2013-08-16T13:37:45)
    0000   0xad 0x25 0x2d 0x70 0x0d                   .%-p.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 53 Ian3F 2013-08-16T13:37:45 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2013-08-16T13:37:45)
    0000   0xad 0x25 0x2d 0x70 0x0d                   .%-p.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 BolusWizard 2013-08-16T14:49:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-16T14:49:53)
    0000   0xb5 0x31 0x0e 0x70 0x0d                   .1.p.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 194, 'amount': 4.7, 'curve': 4},
 {'age': 204, 'amount': 2.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0xbc 0xc2 0x04 0x5c 0xcc 0x04    \....\..
    decimal
             92    8  188  194    4   92  204    4
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-08-16T14:49:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0x24 0x00    ..h.h.$.
    decimal
              1    0  104    0  104    0   36    0
    datetime (2013-08-16T14:49:53)
    0000   0xb5 0x31 0x4e 0x70 0x0d                   .1Np.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2013-08-16T16:17:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-16T16:17:21)
    0000   0x95 0x11 0x10 0x70 0x0d                   ...p.
    body (15)
    hex
    0000   0x0d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x2c 0x00 0x00 0x00 0x00 0x2c 0x36         ,....,6
    decimal
             13  144    0  110   23   54    0    0
             44    0    0    0    0   44   54
    DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 2.6, 'curve': 4},
 {'age': 26, 'amount': 4.7, 'curve': 20},
 {'age': 36, 'amount': 2.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0x5c 0x04 0xbc 0x1a 0x14    \.h\....
    0008   0x5c 0x24 0x14                             \$.
    decimal
             92   11  104   92    4  188   26   20
             92   36   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-08-16T16:17:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x44 0x00    ..,.,.D.
    decimal
              1    0   44    0   44    0   68    0
    datetime (2013-08-16T16:17:22)
    0000   0x96 0x11 0x50 0x70 0x0d                   ..Pp.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 60 CalBGForPH 2013-08-16T16:42:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-08-16T16:42:01)
    0000   0x81 0x2a 0x30 0x70 0x0d                   .*0p.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 Ian3F 2013-08-16T16:42:01 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2013-08-16T16:42:01)
    0000   0x81 0x2a 0x10 0x70 0x0d                   .*.p.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 BolusWizard 2013-08-16T19:14:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 47,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 168}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-16T19:14:40)
    0000   0xa8 0x0e 0x13 0x70 0x0d                   ...p.
    body (15)
    hex
    0000   0x2f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    /..n.6..
    0008   0xa8 0x00 0x00 0x00 0x00 0xa8 0x36         ......6
    decimal
             47  144    0  110   23   54    0    0
            168    0    0    0    0  168   54
    DAY BITS: [0, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 179, 'amount': 1.1, 'curve': 4},
 {'age': 13, 'amount': 2.6, 'curve': 20},
 {'age': 203, 'amount': 4.7, 'curve': 20},
 {'age': 213, 'amount': 2.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x2c 0xb3 0x04 0x68 0x0d 0x14    \.,..h..
    0008   0xbc 0xcb 0x14 0x5c 0xd5 0x14              ...\..
    decimal
             92   14   44  179    4  104   13   20
            188  203   20   92  213   20
    datetime (unknown)

    body (0)

#### RECORD 64 Ian69 2013-08-16T19:14:40 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-16T19:14:40)
    0000   0xa8 0x0e 0x73 0x10 0x0d                   ..s..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 65 Bolus 2013-08-16T19:14:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x08 0x00    ........
    decimal
              1    0  168    0  168    0    8    0
    datetime (2013-08-16T19:14:40)
    0000   0xa8 0x0e 0x53 0x70 0x0d                   ..Sp.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 66 CalBGForPH 2013-08-16T20:19:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-08-16T20:19:07)
    0000   0x87 0x13 0x34 0x70 0x0d                   ..4p.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 67 Ian3F 2013-08-16T20:19:07 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2013-08-16T20:19:07)
    0000   0x87 0x13 0xd4 0x70 0x0d                   ...p.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 68 BolusWizard 2013-08-16T23:18:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 47,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 168}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-16T23:18:44)
    0000   0xac 0x12 0x17 0x70 0x0d                   ...p.
    body (15)
    hex
    0000   0x2f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    /..n.6..
    0008   0xa8 0x00 0x00 0x00 0x00 0xa8 0x36         ......6
    decimal
             47  144    0  110   23   54    0    0
            168    0    0    0    0  168   54
    DAY BITS: [0, 1, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 243, 'amount': 3.7, 'curve': 4},
 {'age': 253, 'amount': 0.5, 'curve': 4},
 {'age': 167, 'amount': 1.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x94 0xf3 0x04 0x14 0xfd 0x04    \.......
    0008   0x2c 0xa7 0x14                             ,..
    decimal
             92   11  148  243    4   20  253    4
             44  167   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-08-16T23:18:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x00 0x00    ........
    decimal
              1    0  168    0  168    0    0    0
    datetime (2013-08-16T23:18:45)
    0000   0xad 0x12 0x57 0x70 0x0d                   ..Wp.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 71 BolusWizard 2013-08-16T23:37:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-16T23:37:08)
    0000   0x88 0x25 0x17 0x70 0x0d                   .%.p.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 4.2, 'curve': 4},
 {'age': 6, 'amount': 3.7, 'curve': 20},
 {'age': 16, 'amount': 0.5, 'curve': 20},
 {'age': 186, 'amount': 1.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xa8 0x16 0x04 0x94 0x06 0x14    \.......
    0008   0x14 0x10 0x14 0x2c 0xba 0x14              ...,..
    decimal
             92   14  168   22    4  148    6   20
             20   16   20   44  186   20
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-08-16T23:37:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xa4 0x00    ........
    decimal
              1    0  160    0  160    0  164    0
    datetime (2013-08-16T23:37:09)
    0000   0x89 0x25 0x57 0x70 0x0d                   .%Wp.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 74 BasalProfileStart 2013-08-17T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-17T00:00:00)
    0000   0x80 0x00 0x00 0x11 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 75 MResultTotals 2013-08-17T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0x19                   .....
    decimal
              7    0    0    9   25
    datetime (2013-08-17T00:00:00)
    0000   0x90 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end analysis/ianj/raw/ReadHistoryData-page-21.data: 76 records`
