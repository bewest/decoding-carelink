## START logs/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 218, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x3c 0x78 0x01 0x00 0x3c 0x00 0x3c 0x00    <x..<.<.
    0008   0x00 0x00 0x46 0xdb 0x4a 0x6a 0x0d 0x7b    ..F.Jj.{
    0010   0x03 0x40 0xc0 0x0c 0x0a 0x0d 0x18 0x1d    .@......
    0018   0x00 0x0a 0x68 0x6a 0xd0 0x2f 0x0a 0x0d    ..hj./..
##### DEBUG DECIMAL
             60  120    1    0   60    0   60    0
              0    0   70  219   74  106   13  123
              3   64  192   12   10   13   24   29
              0   10  104  106  208   47   10   13
#### RECORD 0 Sara7B 2013-07-09T17:45:32 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-09T17:45:32)
    0000   0x60 0xed 0x11 0x09 0x0d                   `....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 1]
#### RECORD 1 Prime 2013-07-09T17:45:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2013-07-09T17:45:18)
    0000   0x52 0xed 0x11 0x09 0x0d                   R....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 2 TempBasal 2013-07-09T21:14:34 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.1}
```
    op hex (2)
    0000   0x33 0x54                                  3T
    decimal
             51   84
    datetime (2013-07-09T21:14:34)
    0000   0x62 0xce 0x15 0x09 0x0d                   b....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 3 TempBasalDuration 2013-07-09T21:14:34 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 240}
```
    op hex (2)
    0000   0x16 0x08                                  ..
    decimal
             22    8
    datetime (2013-07-09T21:14:34)
    0000   0x62 0xce 0x15 0x09 0x0d                   b....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 CalBGForPH 2013-07-09T23:47:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 221}
```
    op hex (2)
    0000   0x0a 0xdd                                  ..
    decimal
             10  221
    datetime (2013-07-09T23:47:35)
    0000   0x63 0xef 0x37 0x09 0x0d                   c.7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 5 BolusWizard 2013-07-09T23:47:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 221,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdd                                  [.
    decimal
             91  221
    datetime (2013-07-09T23:47:38)
    0000   0x66 0xef 0x17 0x69 0x0d                   f..i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x40 0x00    .P.d<d@.
    0008   0x00 0x00 0x00 0x00 0x00 0x40 0x78         .....@x
    decimal
              0   80    0  100   60  100   64    0
              0    0    0    0    0   64  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 208, 'amount': 2.5, 'curve': 208},
 {'age': 218, 'amount': 1.4, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0xd0 0xd0 0x38 0xda 0xd0    \.d..8..
    decimal
             92    8  100  208  208   56  218  208
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-07-09T23:47:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-07-09T23:47:38)
    0000   0x66 0xef 0x57 0x69 0x0d                   f.Wi.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 ResultTotals (2000, 6, 0, 0, 13, 41) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xa3                   .....
    decimal
              7    0    0    7  163
    datetime ((2000, 6, 0, 0, 13, 41))
    0000   0x69 0x8d 0x00 0x00 0x00                   i....
    body (51)
    hex
    0000   0x6e 0x69 0x8d 0x05 0x00 0xac 0x00 0x00    ni......
    0008   0x0c 0x00 0x00 0x07 0xa3 0x04 0xe3 0x40    .......@
    0010   0x02 0xc0 0x24 0x00 0x68 0x01 0x70 0x01    ..$.h.p.
    0018   0x50 0x00 0x00 0x00 0x00 0x06 0x05 0x00    P.......
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x66 0x66 0x00 0x00 0x00 0x00    ..ff....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  105  141    5    0  172    0    0
             12    0    0    7  163    4  227   64
              2  192   36    0  104    1  112    1
             80    0    0    0    0    6    5    0
              0    4    0    0    0    0    0    0
              0    0  102  102    0    0    0    0
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 9 Base (2010, 1, 0, 0, 26, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x33                                  .3
    decimal
              0   51
    datetime ((2010, 1, 0, 0, 26, 0))
    0000   0x00 0x5a 0xc0 0x00 0x0a                   .Z...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 10 Base (2000, 0, 0, 26, 0, 22) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 0, 26, 0, 22))
    0000   0x16 0x00 0x5a 0xc0 0x00                   ..Z..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 11 CalBGForPH (2000, 4, 0, 26, 0, 59) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime ((2000, 4, 0, 26, 0, 59))
    0000   0x7b 0x00 0x5a 0xc0 0x00                   {.Z..
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH (2001, 0, 27, 0, 28, 0) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 13}
```
    op hex (2)
    0000   0x0a 0x0d                                  ..
    decimal
             10   13
    datetime ((2001, 0, 27, 0, 28, 0))
    0000   0x00 0x1c 0x00 0x7b 0x01                   ...{.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 13 Base (2014, 0, 8, 13, 10, 4) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0xc0                                  @.
    decimal
             64  192
    datetime ((2014, 0, 8, 13, 10, 4))
    0000   0x04 0x0a 0x0d 0x08 0x1e                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 14 Base (2010, 1, 8, 0, 0, 2) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2010, 1, 8, 0, 0, 2))
    0000   0x02 0x40 0xc0 0x08 0x0a                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 15 Base (2010, 0, 10, 10, 0, 36) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x10                                  ..
    decimal
             13   16
    datetime ((2010, 0, 10, 10, 0, 36))
    0000   0x24 0x00 0x0a 0x6a 0x6a                   $..jj
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 16 Base (2006, 0, 10, 27, 13, 10) head[2], body[0] op[0xda]

    op hex (2)
    0000   0xda 0x2a                                  .*
    decimal
            218   42
    datetime ((2006, 0, 10, 27, 13, 10))
    0000   0x0a 0x0d 0x5b 0x6a 0x46                   ..[jF
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 17 Base (2000, 4, 16, 18, 13, 42) head[2], body[0] op[0xdb]

    op hex (2)
    0000   0xdb 0x0a                                  ..
    decimal
            219   10
    datetime ((2000, 4, 16, 18, 13, 42))
    0000   0x6a 0x0d 0x12 0x50 0x00                   j..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 18 Base (2000, 4, 28, 0, 0, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 4, 28, 0, 0, 36))
    0000   0x64 0x00 0x00 0x3c 0x00                   d..<.
    body (0)
    DAY BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-30.data: 19 records`
