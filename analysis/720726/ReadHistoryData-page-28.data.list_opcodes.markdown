## START logs/ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 437, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x24 0x00 0x00 0x00 0x00 0x24 0x36 0x5c    $....$6\
    0008   0x11 0x78 0x05 0x04 0x68 0x69 0x04 0x34    .x..hi.4
    0010   0xf5 0x04 0x5c 0xff 0x04 0x38 0x13 0x14    ..\..8..
    0018   0x01 0x00 0x24 0x00 0x24 0x00 0xb4 0x00    ..$.$...
##### DEBUG DECIMAL
             36    0    0    0    0   36   54   92
             17  120    5    4  104  105    4   52
            245    4   92  255    4   56   19   20
              1    0   36    0   36    0  180    0
#### RECORD 0 Base (2013, 8, 4, 8, 35, 50) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime ((2013, 8, 4, 8, 35, 50))
    0000   0xb2 0x23 0x08 0x64 0x0d                   .#.d.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 Base (2003, 9, 26, 14, 27, 22) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime ((2003, 9, 26, 14, 27, 22))
    0000   0x96 0x5b 0x8e 0xba 0x23                   .[..#
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 2 ChangeBasalProfile (2014, 0, 0, 16, 0, 13) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x64                                  .d
    decimal
              8  100
    datetime ((2014, 0, 0, 16, 0, 13))
    0000   0x0d 0x00 0x90 0x00 0x6e                   ....n
    body (44)
    hex
    0000   0x17 0x36 0x98 0x00 0x00 0x00 0x00 0x00    .6......
    0008   0x00 0x98 0x36 0x69 0x08 0xba 0x23 0x08    ..6i..#.
    0010   0x04 0x0d 0x0a 0x1e 0x01 0x00 0x98 0x00    ........
    0018   0x98 0x00 0x00 0x00 0xba 0x23 0x48 0x64    .....#Hd
    0020   0x0d 0x7b 0x02 0x80 0x1e 0x09 0x04 0x0d    .{......
    0028   0x13 0x1e 0x00 0x0a                        ....
    decimal
             23   54  152    0    0    0    0    0
              0  152   54  105    8  186   35    8
              4   13   10   30    1    0  152    0
            152    0    0    0  186   35   72  100
             13  123    2  128   30    9    4   13
             19   30    0   10
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 3 Base (2015, 0, 13, 4, 41, 34) head[2], body[0] op[0x3c]

    op hex (2)
    0000   0x3c 0x92                                  <.
    decimal
             60  146
    datetime ((2015, 0, 13, 4, 41, 34))
    0000   0x22 0x29 0x64 0x0d 0x3f                   ")d.?
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 4 ResultTotals 2011-01-22T09:41:13 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x92 0x22 0x89 0x64                   ..".d
    decimal
              7  146   34  137  100
    datetime (2011-01-22T09:41:13)
    0000   0x0d 0x69 0x69 0x96 0x5b                   .ii.[
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 5 Base (2014, 0, 13, 4, 10, 54) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xb9                                  ..
    decimal
              0  185
    datetime ((2014, 0, 13, 4, 10, 54))
    0000   0x36 0x0a 0x64 0x0d 0x1e                   6.d..
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 6 Base (2000, 4, 0, 22, 23, 46) head[2], body[0] op[0x90]

    op hex (2)
    0000   0x90 0x00                                  ..
    decimal
            144    0
    datetime ((2000, 4, 0, 22, 23, 46))
    0000   0x6e 0x17 0x36 0x00 0x00                   n.6..
    body (0)

#### RECORD 7 Base (2006, 0, 12, 0, 0, 0) head[2], body[0] op[0x6c]

    op hex (2)
    0000   0x6c 0x00                                  l.
    decimal
            108    0
    datetime ((2006, 0, 12, 0, 0, 0))
    0000   0x00 0x00 0x00 0x6c 0x36                   ...l6
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 139, 'amount': 3.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x98 0x8b 0x04                   \....
    decimal
             92    5  152  139    4
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-08-04T10:54:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x38 0x00    ..l.l.8.
    decimal
              1    0  108    0  108    0   56    0
    datetime (2013-08-04T10:54:57)
    0000   0xb9 0x36 0x4a 0x64 0x0d                   .6Jd.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 BolusWizard 2013-08-04T12:08:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 36,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 128}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-04T12:08:32)
    0000   0xa0 0x08 0x0c 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x24 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    $..n.6..
    0008   0x80 0x00 0x00 0x00 0x00 0x80 0x36         ......6
    decimal
             36  144    0  110   23   54    0    0
            128    0    0    0    0  128   54
    DAY BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 2.6, 'curve': 4},
 {'age': 83, 'amount': 0.1, 'curve': 4},
 {'age': 213, 'amount': 3.8, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x68 0x49 0x04 0x04 0x53 0x04    \.hI..S.
    0008   0x98 0xd5 0x04                             ...
    decimal
             92   11  104   73    4    4   83    4
            152  213    4
    datetime (unknown)

    body (0)

#### RECORD 12 Base (2013, 8, 4, 12, 8, 32) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime ((2013, 8, 4, 12, 8, 32))
    0000   0xa0 0x08 0x0c 0x04 0x0d                   .....
    body (0)

#### RECORD 13 Base (2000, 0, 0, 0, 0, 1) head[2], body[0] op[0x0e]

    op hex (2)
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    datetime ((2000, 0, 0, 0, 0, 1))
    0000   0x01 0x00 0x80 0x00 0x80                   .....
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 14 Base (2004, 2, 12, 8, 32, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x60                                  .`
    decimal
              0   96
    datetime ((2004, 2, 12, 8, 32, 0))
    0000   0x00 0xa0 0x08 0x4c 0x64                   ...Ld
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 15 Base (2004, 2, 13, 0, 0, 3) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x7b                                  .{
    decimal
             13  123
    datetime ((2004, 2, 13, 0, 0, 3))
    0000   0x03 0x80 0x00 0x0d 0x04                   .....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 Base (2014, 0, 13, 10, 0, 38) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x1a                                  ..
    decimal
             13   26
    datetime ((2014, 0, 13, 10, 0, 38))
    0000   0x26 0x00 0x0a 0x4d 0xae                   &..M.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 0, 1, 0]
#### RECORD 17 Base (2014, 4, 9, 31, 13, 36) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0x30                                  *0
    decimal
             42   48
    datetime ((2014, 4, 9, 31, 13, 36))
    0000   0x64 0x0d 0x3f 0x09 0xae                   d.?..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 18 Base (2006, 4, 9, 9, 13, 36) head[2], body[0] op[0x2a]

    op hex (2)
    0000   0x2a 0xb0                                  *.
    decimal
             42  176
    datetime ((2006, 4, 9, 9, 13, 36))
    0000   0x64 0x0d 0x69 0x69 0x96                   d.ii.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 19 BolusWizard 2013-08-04T16:52:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 43,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 23.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x2b                                  [+
    decimal
             91   43
    datetime (2013-08-04T16:52:13)
    0000   0x8d 0x34 0x10 0x64 0x0d                   .4.d.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0xec 0x00    ...n.6..
    0008   0x4c 0xf8 0x00 0x00 0x00 0x38 0x36         L....86
    decimal
             21  144    0  110   23   54  236    0
             76  248    0    0    0   56   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 31, 'amount': 3.2, 'curve': 20},
 {'age': 101, 'amount': 2.6, 'curve': 20},
 {'age': 111, 'amount': 0.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x80 0x1f 0x14 0x68 0x65 0x14    \....he.
    0008   0x04 0x6f 0x14                             .o.
    decimal
             92   11  128   31   20  104  101   20
              4  111   20
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2013-08-04T16:52:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2013-08-04T16:52:14)
    0000   0x8e 0x34 0x50 0x64 0x0d                   .4Pd.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2013-08-04T17:13:26 head[2], body[15] op[0x5b]
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
    datetime (2013-08-04T17:13:26)
    0000   0x9a 0x0d 0x11 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x36         ......6
    decimal
             40  144    0  110   23   54    0    0
            144    0    0    0    0  144   54
    DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 1.4, 'curve': 4},
 {'age': 52, 'amount': 3.2, 'curve': 20},
 {'age': 122, 'amount': 2.6, 'curve': 20},
 {'age': 132, 'amount': 0.1, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0x1c 0x04 0x80 0x34 0x14    \.8...4.
    0008   0x68 0x7a 0x14 0x04 0x84 0x14              hz....
    decimal
             92   14   56   28    4  128   52   20
            104  122   20    4  132   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-08-04T17:13:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x38 0x00    ......8.
    decimal
              1    0  144    0  144    0   56    0
    datetime (2013-08-04T17:13:26)
    0000   0x9a 0x0d 0x51 0x64 0x0d                   ..Qd.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 25 BolusWizard 2013-08-04T19:41:47 head[2], body[15] op[0x5b]
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
    datetime (2013-08-04T19:41:47)
    0000   0xaf 0x29 0x13 0x64 0x0d                   .).d.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 146, 'amount': 1.3, 'curve': 4},
 {'age': 156, 'amount': 2.3, 'curve': 4},
 {'age': 176, 'amount': 1.4, 'curve': 4},
 {'age': 200, 'amount': 3.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x34 0x92 0x04 0x5c 0x9c 0x04    \.4..\..
    0008   0x38 0xb0 0x04 0x80 0xc8 0x14              8.....
    decimal
             92   14   52  146    4   92  156    4
             56  176    4  128  200   20
    datetime (unknown)

    body (0)

#### RECORD 27 Base (2013, 8, 4, 19, 41, 47) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime ((2013, 8, 4, 19, 41, 47))
    0000   0xaf 0x29 0x73 0x04 0x0d                   .)s..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 Base (2008, 0, 0, 8, 0, 1) head[2], body[0] op[0x15]

    op hex (2)
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    datetime ((2008, 0, 0, 8, 0, 1))
    0000   0x01 0x00 0x68 0x00 0x68                   ..h.h
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 29 Base (2004, 2, 19, 9, 47, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x34                                  .4
    decimal
              0   52
    datetime ((2004, 2, 19, 9, 47, 0))
    0000   0x00 0xaf 0x29 0x53 0x64                   ..)Sd
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 30 Base (2004, 6, 20, 16, 10, 9) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2004, 6, 20, 16, 10, 9))
    0000   0x49 0x8a 0x30 0x34 0x64                   I.04d
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 31 Base (2004, 2, 20, 16, 10, 9) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2004, 2, 20, 16, 10, 9))
    0000   0x09 0x8a 0x30 0x34 0x64                   ..04d
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 32 Base (2012, 6, 0, 27, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2012, 6, 0, 27, 22, 41))
    0000   0x69 0x96 0x5b 0x00 0x8c                   i.[..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 Base (2000, 4, 16, 1, 13, 36) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x15                                  ..
    decimal
             16   21
    datetime ((2000, 4, 16, 1, 13, 36))
    0000   0x64 0x0d 0x21 0x90 0x00                   d.!..
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 34 Sara6E 2006-08-23T14:00:16 head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x17 0x36 0x00 0x00 0x78 0x00 0x00    n.6..x..
    0008   0x00 0x00 0x78 0x36 0x5c 0x0e 0x68 0x65    ..x6\.he
    0010   0x04 0x34 0xf1 0x04 0x5c 0xfb 0x04 0x38    .4..\..8
    0018   0x0f 0x14 0x01 0x00 0x78 0x00 0x78 0x00    ....x.x.
    0020   0x3c 0x00 0x8d 0x10 0x55 0x64 0x0d 0x5b    <...Ud.[
    0028   0x00 0x8b 0x14 0x15 0x64 0x0d 0x0a         ....d..
    decimal
            110   23   54    0    0  120    0    0
              0    0  120   54   92   14  104  101
              4   52  241    4   92  251    4   56
             15   20    1    0  120    0  120    0
             60    0  141   16   85  100   13   91
              0  139   20   21  100   13   10
    datetime (2006-08-23T14:00:16)
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-28.data: 35 records`
