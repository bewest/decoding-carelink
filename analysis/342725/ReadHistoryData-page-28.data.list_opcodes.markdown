## START logs/ReadHistoryData-page-28.data
ERROR day is out of range for month (2006, 4, 32, 0, 0, 0) 0000   0x5f 0x46                                  _F
#### STOPPING DOUBLE NULLS @ 480, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x37 0x7d 0x01 0x37 0x37 0x00 0x65 0x10    7}.77.e.
    0008   0x47 0x0b 0x0d 0x1e 0x00 0x76 0x3a 0x08    G....v:.
    0010   0x0b 0x0d 0x1f 0x00 0x54 0x1b 0x09 0x0b    ....T...
    0018   0x0d 0x0a 0x85 0x68 0x0b 0x2b 0x0b 0x0d    ...h.+..
##### DEBUG DECIMAL
             55  125    1   55   55    0  101   16
             71   11   13   30    0  118   58    8
             11   13   31    0   84   27    9   11
             13   10  133  104   11   43   11   13
#### RECORD 0 Prime 2013-04-09T20:12:46 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-04-09T20:12:46)
    0000   0x6e 0x0c 0x14 0x09 0x0d                   n....
    body (0)

#### RECORD 1 CalBGForPH 2013-04-09T20:15:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 230}
```
    op hex (2)
    0000   0x0a 0xe6                                  ..
    decimal
             10  230
    datetime (2013-04-09T20:15:05)
    0000   0x45 0x0f 0x34 0x09 0x0d                   E.4..
    body (0)

#### RECORD 2 BolusWizard 2013-04-09T20:15:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 23,
 '_byte[7]': 0,
 'bg': 230,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 37,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 2.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe6                                  [.
    decimal
             91  230
    datetime (2013-04-09T20:15:28)
    0000   0x5c 0x0f 0x14 0x09 0x0d                   \....
    body (15)
    hex
    0000   0x25 0x50 0x0d 0x2d 0x6a 0x17 0x1c 0x00    %P.-j...
    0008   0x00 0x16 0x00 0x1d 0x7d 0x5c 0x0b         ....}\.
    decimal
             37   80   13   45  106   23   28    0
              0   22    0   29  125   92   11

#### RECORD 3 Ian50 (2008, 0, 4, 3, 20, 4) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x15                                  P.
    decimal
             80   21
    datetime ((2008, 0, 4, 3, 20, 4))
    0000   0x04 0x14 0x83 0x04 0x68                   ....h
    body (34)
    hex
    0000   0x05 0x14 0x01 0x1d 0x1d 0x00 0x5c 0x0f    ......\.
    0008   0x54 0x09 0x0d 0x07 0x00 0x00 0x04 0xac    T.......
    0010   0x49 0x0d 0x6d 0x49 0x0d 0x05 0x00 0xc8    I.mI....
    0018   0x5b 0xf7 0x05 0x00 0x00 0x04 0xac 0x03    [.......
    0020   0x6c 0x49                                  lI
    decimal
              5   20    1   29   29    0   92   15
             84    9   13    7    0    0    4  172
             73   13  109   73   13    5    0  200
             91  247    5    0    0    4  172    3
            108   73
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 4 Bolus (2008, 3, 0, 3, 24, 0) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.4, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x40 0x1b 0x00 0x4c 0x01 0x40 0x1b    .@..L.@.
    decimal
              1   64   27    0   76    1   64   27
    datetime ((2008, 3, 0, 3, 24, 0))
    0000   0x00 0xd8 0x43 0x00 0x68                   ..C.h
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 5 Rewind (2002, 0, 1, 4, 0, 0) head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime ((2002, 0, 1, 4, 0, 0))
    0000   0x00 0x00 0x04 0x01 0x02                   .....
    body (0)

#### RECORD 6 Bolus (2012, 0, 20, 16, 0, 30) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x0c 0x00 0xe8 0x00 0x00 0x00    ........
    decimal
              1    0   12    0  232    0    0    0
    datetime ((2012, 0, 20, 16, 0, 30))
    0000   0x1e 0x00 0x50 0x34 0x0c                   ..P4.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 7 CalBGForPH (2013, 0, 15, 20, 0, 31) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime ((2013, 0, 15, 20, 0, 31))
    0000   0x1f 0x00 0x54 0x0f 0x0d                   ..T..
    body (0)

#### RECORD 8 CalBGForPH (2014, 1, 26, 24, 8, 10) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime ((2014, 1, 26, 24, 8, 10))
    0000   0x0a 0x48 0x78 0x1a 0x2e                   .Hx..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 9 CalBGForPH (2014, 5, 27, 27, 8, 27) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime ((2014, 5, 27, 27, 8, 27))
    0000   0x5b 0x48 0x5b 0x1b 0x0e                   [H[..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 10 CalBGForPH 2010-01-13T13:16:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime (2010-01-13T13:16:59)
    0000   0x3b 0x50 0x0d 0x2d 0x6a                   ;P.-j
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 11 Base (2005, 12, 0, 0, 0, 48) head[2], body[0] op[0xf8]

    op hex (2)
    0000   0xf8 0x2d                                  .-
    decimal
            248   45
    datetime ((2005, 12, 0, 0, 0, 48))
    0000   0xf0 0x00 0x00 0x00 0x25                   ....%
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 12 Base (2011, 0, 27, 0, 37, 37) head[2], body[0] op[0x7d]

    op hex (2)
    0000   0x7d 0x01                                  }.
    decimal
            125    1
    datetime ((2011, 0, 27, 0, 37, 37))
    0000   0x25 0x25 0x00 0x5b 0x1b                   %%.[.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 13 Base (2007, 0, 24, 4, 10, 13) head[2], body[0] op[0x4e]

    op hex (2)
    0000   0x4e 0x0a                                  N.
    decimal
             78   10
    datetime ((2007, 0, 24, 4, 10, 13))
    0000   0x0d 0x0a 0xe4 0x78 0x37                   ...x7
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 14 Base (2008, 1, 8, 4, 27, 13) head[2], body[0] op[0x2f]

    op hex (2)
    0000   0x2f 0x0a                                  /.
    decimal
             47   10
    datetime ((2008, 1, 8, 4, 27, 13))
    0000   0x0d 0x5b 0xe4 0x48 0x38                   .[.H8
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 15 Base (2013, 0, 13, 16, 0, 13) head[2], body[0] op[0x0f]

    op hex (2)
    0000   0x0f 0x0a                                  ..
    decimal
             15   10
    datetime ((2013, 0, 13, 16, 0, 13))
    0000   0x0d 0x00 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 16 Base (2000, 0, 24, 0, 0, 0) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x16                                  j.
    decimal
            106   22
    datetime ((2000, 0, 24, 0, 0, 0))
    0000   0x00 0x00 0x00 0x18 0x00                   .....
    body (0)

#### RECORD 17 Base (2004, 4, 28, 20, 5, 28) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7d                                  .}
    decimal
              0  125
    datetime ((2004, 4, 28, 20, 5, 28))
    0000   0x5c 0x05 0x94 0x5c 0x04                   \..\.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 18 Bolus (2007, 0, 9, 0, 10, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x02 0x02 0x00 0x48 0x38 0x4f 0x0a    ....H8O.
    decimal
              1    2    2    0   72   56   79   10
    datetime ((2007, 0, 9, 0, 10, 13))
    0000   0x0d 0x0a 0xe0 0x49 0x07                   ...I.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 19 Base (2007, 1, 12, 0, 27, 13) head[2], body[0] op[0x31]

    op hex (2)
    0000   0x31 0x0a                                  1.
    decimal
             49   10
    datetime ((2007, 1, 12, 0, 27, 13))
    0000   0x0d 0x5b 0xe0 0x4c 0x07                   .[.L.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 20 Base (2013, 0, 13, 16, 0, 13) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x0a                                  ..
    decimal
             17   10
    datetime ((2013, 0, 13, 16, 0, 13))
    0000   0x0d 0x00 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 21 Base (2000, 0, 11, 0, 0, 0) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x16                                  j.
    decimal
            106   22
    datetime ((2000, 0, 11, 0, 0, 0))
    0000   0x00 0x00 0x00 0x0b 0x00                   .....
    body (0)

#### RECORD 22 Ian0B (2004, 0, 4, 9, 8, 8) head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x7d 0x5c                             .}\
    decimal
             11  125   92
    datetime ((2004, 0, 4, 9, 8, 8))
    0000   0x08 0x08 0x49 0x04 0x94                   ..I..
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 23 Base (2013, 0, 0, 13, 13, 1) head[2], body[0] op[0xa3]

    op hex (2)
    0000   0xa3 0x04                                  ..
    decimal
            163    4
    datetime ((2013, 0, 0, 13, 13, 1))
    0000   0x01 0x0d 0x0d 0x00 0x4d                   ....M
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 24 MResultTotals 2013-08-23T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x51 0x0a 0x0d 0x0a                   .Q...
    decimal
              7   81   10   13   10
    datetime (2013-08-23T00:00:00)
    0000   0x96 0x6d                                  .m
    body (3)
    hex
    0000   0x1a 0x32 0x0a                             .2.
    decimal
             26   50   10
    HOUR BITS: [0, 1, 1]
#### RECORD 25 Base (2010, 9, 18, 8, 16, 14) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2010, 9, 18, 8, 16, 14))
    0000   0x8e 0x50 0x28 0x32 0x0a                   .P(2.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1]
#### RECORD 26 Base (2010, 9, 18, 8, 38, 14) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2010, 9, 18, 8, 38, 14))
    0000   0x8e 0x66 0x28 0x12 0x0a                   .f(..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 27 Base (2003, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0d                                  ..
    decimal
             13   13
    datetime ((2003, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0x03                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 28 CalBGForPH (2013, 0, 10, 0, 9, 0) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 0}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime ((2013, 0, 10, 0, 9, 0))
    0000   0x00 0x09 0x00 0x0a 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 1.3, 'curve': 4},
 {'age': 166, 'amount': 0.2, 'curve': 4},
 {'age': 0, 'amount': 3.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x60 0x04 0x08 0xa6 0x04    \.4`....
    0008   0x94 0x00 0x14                             ...
    decimal
             92   11   52   96    4    8  166    4
            148    0   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus (2001, 0, 11, 1, 10, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x0a 0x0a 0x00 0x66 0x28 0x52 0x0a    ....f(R.
    decimal
              1   10   10    0  102   40   82   10
    datetime ((2001, 0, 11, 1, 10, 13))
    0000   0x0d 0x0a 0x21 0x6b 0x11                   ..!k.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 31 LowReservoir 2001-09-12T01:27:13 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.0}
```
    op hex (2)
    0000   0x34 0x0a                                  4.
    decimal
             52   10
    datetime (2001-09-12T01:27:13)
    0000   0x8d 0x5b 0x21 0x6c 0x11                   .[!l.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 32 SelectBasalProfile (2013, 0, 13, 17, 0, 13) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x0a                                  ..
    decimal
             20   10
    datetime ((2013, 0, 13, 17, 0, 13))
    0000   0x0d 0x00 0x51 0x0d 0x2d                   ..Q.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 33 Base (2000, 0, 8, 0, 0, 0) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x24                                  j$
    decimal
            106   36
    datetime ((2000, 0, 8, 0, 0, 0))
    0000   0x00 0x00 0x00 0x08 0x00                   .....
    body (0)

#### RECORD 34 Base (2004, 4, 7, 8, 14, 28) head[2], body[0] op[0x1c]

    op hex (2)
    0000   0x1c 0x7d                                  .}
    decimal
             28  125
    datetime ((2004, 4, 7, 8, 14, 28))
    0000   0x5c 0x0e 0x28 0x67 0x04                   \.(g.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 35 LowReservoir (2004, 0, 20, 7, 8, 4) head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 19.3}
```
    op hex (2)
    0000   0x34 0xc1                                  4.
    decimal
             52  193
    datetime ((2004, 0, 20, 7, 8, 4))
    0000   0x04 0x08 0x07 0x14 0x94                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 36 Base (2012, 0, 0, 28, 28, 1) head[2], body[0] op[0x61]

    op hex (2)
    0000   0x61 0x14                                  a.
    decimal
             97   20
    datetime ((2012, 0, 0, 28, 28, 1))
    0000   0x01 0x1c 0x1c 0x00 0x6c                   ....l
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 37 Base (2012, 0, 23, 10, 13, 10) head[2], body[0] op[0x11]

    op hex (2)
    0000   0x11 0x54                                  .T
    decimal
             17   84
    datetime ((2012, 0, 23, 10, 13, 10))
    0000   0x0a 0x0d 0x0a 0x77 0x6c                   ...wl
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 38 Base (2009, 0, 31, 10, 13, 10) head[2], body[0] op[0x2b]

    op hex (2)
    0000   0x2b 0x35                                  +5
    decimal
             43   53
    datetime ((2009, 0, 31, 10, 13, 10))
    0000   0x0a 0x0d 0x0a 0x5f 0x69                   ..._i
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
ERROR day is out of range for month (2006, 4, 32, 0, 0, 0) 0000   0x5f 0x46                                  _F
#### RECORD 39 MResultTotals (2006, 4, 32, 0, 0, 0) head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x37 0x0a 0x0d 0x5b                   .7..[
    decimal
              7   55   10   13   91
    datetime ((2006, 4, 32, 0, 0, 0))
    0000   0x5f 0x46                                  _F
    body (3)
    hex
    0000   0x08 0x17 0x0a                             ...
    decimal
              8   23   10
    HOUR BITS: [0, 1, 0]
#### RECORD 40 Base (2013, 4, 10, 13, 13, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x23                                  .#
    decimal
             13   35
    datetime ((2013, 4, 10, 13, 13, 16))
    0000   0x50 0x0d 0x2d 0x6a 0xfd                   P.-j.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 41 Battery (2013, 0, 23, 0, 6, 0) head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0xf0                                  ..
    decimal
             26  240
    datetime ((2013, 0, 23, 0, 6, 0))
    0000   0x00 0x06 0x00 0x17 0x7d                   ....}
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 174, 'amount': 2.8, 'curve': 4},
 {'age': 18, 'amount': 1.0, 'curve': 20},
 {'age': 108, 'amount': 1.3, 'curve': 20},
 {'age': 178, 'amount': 0.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x70 0xae 0x04 0x28 0x12 0x14    \.p..(..
    0008   0x34 0x6c 0x14 0x08 0xb2 0x14              4l....
    decimal
             92   14  112  174    4   40   18   20
             52  108   20    8  178   20
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus (2005, 0, 0, 0, 7, 13) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3, 'dual_component': '??', 'programmed': 2.3, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x17 0x17 0x00 0x47 0x08 0x57 0x0a    ....G.W.
    decimal
              1   23   23    0   71    8   87   10
    datetime ((2005, 0, 0, 0, 7, 13))
    0000   0x0d 0x07 0x00 0x00 0x05                   .....
    body (0)

#### RECORD 44 Base (2005, 1, 13, 10, 45, 13) head[2], body[0] op[0x38]

    op hex (2)
    0000   0x38 0x4a                                  8J
    decimal
             56   74
    datetime ((2005, 1, 13, 10, 45, 13))
    0000   0x0d 0x6d 0x4a 0x0d 0x05                   .mJ..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 45 Base (2000, 4, 0, 8, 33, 8) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0xa5                                  ..
    decimal
             16  165
    datetime ((2000, 4, 0, 8, 33, 8))
    0000   0x48 0x21 0x08 0x00 0x00                   H!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 46 Base (2004, 1, 1, 2, 52, 3) head[2], body[0] op[0x05]

    op hex (2)
    0000   0x05 0x38                                  .8
    decimal
              5   56
    datetime ((2004, 1, 1, 2, 52, 3))
    0000   0x03 0x74 0x42 0x01 0xc4                   .tB..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 0]
#### RECORD 47 Base (2001, 4, 2, 4, 1, 43) head[2], body[0] op[0x22]

    op hex (2)
    0000   0x22 0x00                                  ".
    decimal
             34    0
    datetime ((2001, 4, 2, 4, 1, 43))
    0000   0x6b 0x01 0xc4 0x22 0x01                   k..".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 48 NewTimeSet (2000, 2, 0, 6, 44, 0) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x3e                                  .>
    decimal
             24   62
    datetime ((2000, 2, 0, 6, 44, 0))
    0000   0x00 0xac 0x26 0x00 0x00                   ..&..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 Base (2012, 0, 0, 0, 3, 3) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x06                                  ..
    decimal
              0    6
    datetime ((2012, 0, 0, 0, 3, 3))
    0000   0x03 0x03 0x00 0x00 0x0c                   .....
    body (0)

#### RECORD 50 Base (2006, 0, 10, 0, 0, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xe8                                  ..
    decimal
              0  232
    datetime ((2006, 0, 10, 0, 0, 0))
    0000   0x00 0x00 0x00 0x0a 0x76                   ....v
    body (0)
    YEAR BITS: [0, 1, 1, 1]
#### RECORD 51 ChangeUtility (2006, 0, 27, 13, 11, 39) head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x10                                  c.
    decimal
             99   16
    datetime ((2006, 0, 27, 13, 11, 39))
    0000   0x27 0x0b 0x8d 0x5b 0x76                   '..[v
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 52 Base (2001, 0, 0, 13, 11, 7) head[2], body[0] op[0x65]

    op hex (2)
    0000   0x65 0x10                                  e.
    decimal
            101   16
    datetime ((2001, 0, 0, 13, 11, 7))
    0000   0x07 0x0b 0x0d 0x00 0x51                   ....Q
    body (0)
    YEAR BITS: [0, 1, 0, 1]
#### RECORD 53 Base (2000, 4, 0, 0, 55, 42) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x2d                                  .-
    decimal
             13   45
    datetime ((2000, 4, 0, 0, 55, 42))
    0000   0x6a 0x37 0x00 0x00 0x00                   j7...
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-28.data: 54 records`
