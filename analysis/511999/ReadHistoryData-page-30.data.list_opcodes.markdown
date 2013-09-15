## START logs/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 141, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x33 0x00 0x5a 0xc0 0x00 0x0a 0x0d 0x08    3.Z.....
    0008   0x16 0x00 0x5a 0xc0 0x00 0x0a 0x0d 0x7b    ..Z....{
    0010   0x00 0x5a 0xc0 0x00 0x0a 0x0d 0x00 0x1c    .Z......
    0018   0x00 0x7b 0x01 0x40 0xc0 0x04 0x0a 0x0d    .{.@....
##### DEBUG DECIMAL
             51    0   90  192    0   10   13    8
             22    0   90  192    0   10   13  123
              0   90  192    0   10   13    0   28
              0  123    1   64  192    4   10   13
#### RECORD 0 Base (2013, 7, 9, 17, 45, 32) head[2], body[0] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime ((2013, 7, 9, 17, 45, 32))
    0000   0x60 0xed 0x11 0x09 0x0d                   `....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 NewTimeSet (2000, 0, 4, 0, 3, 0) head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x1d                                  ..
    decimal
             24   29
    datetime ((2000, 0, 4, 0, 3, 0))
    0000   0x00 0x03 0x00 0x04 0x00                   .....
    body (0)

#### RECORD 2 Base (2003, 12, 13, 9, 17, 45) head[2], body[0] op[0x04]

    op hex (2)
    0000   0x04 0x52                                  .R
    decimal
              4   82
    datetime ((2003, 12, 13, 9, 17, 45))
    0000   0xed 0x11 0x09 0x0d 0x33                   ....3
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 3 Base (2008, 12, 13, 9, 21, 14) head[2], body[0] op[0x54]

    op hex (2)
    0000   0x54 0x62                                  Tb
    decimal
             84   98
    datetime ((2008, 12, 13, 9, 21, 14))
    0000   0xce 0x15 0x09 0x0d 0x08                   .....
    body (0)

#### RECORD 4 TempBasalDuration 2013-07-09T21:14:34 head[2], body[0] op[0x16]
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
#### RECORD 5 CalBGForPH 2013-07-09T23:47:35 head[2], body[0] op[0x0a]
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
#### RECORD 6 BolusWizard 2013-07-09T23:47:38 head[2], body[15] op[0x5b]
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
#### RECORD 7 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
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

#### RECORD 8 Bolus (2006, 4, 0, 0, 0, 0) head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x00 0x40 0x00                        ..@.
    decimal
              1    0   64    0
    datetime ((2006, 4, 0, 0, 0, 0))
    0000   0x40 0x00 0x00 0x00 0x66                   @...f
    body (0)
    YEAR BITS: [0, 1, 1, 0]
#### RECORD 9 Base (2000, 4, 0, 7, 13, 41) head[2], body[0] op[0xef]

    op hex (2)
    0000   0xef 0x57                                  .W
    decimal
            239   87
    datetime ((2000, 4, 0, 7, 13, 41))
    0000   0x69 0x0d 0x07 0x00 0x00                   i....
    body (0)

#### RECORD 10 ResultTotals (2013, 0, 9, 14, 0, 0) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0xa3 0x69 0x8d 0x00                   ..i..
    decimal
              7  163  105  141    0
    datetime ((2013, 0, 9, 14, 0, 0))
    0000   0x00 0x00 0x6e 0x69 0x8d                   ..ni.
    body (41)
    hex
    0000   0x05 0x00 0xac 0x00 0x00 0x0c 0x00 0x00    ........
    0008   0x07 0xa3 0x04 0xe3 0x40 0x02 0xc0 0x24    ....@..$
    0010   0x00 0x68 0x01 0x70 0x01 0x50 0x00 0x00    .h.p.P..
    0018   0x00 0x00 0x06 0x05 0x00 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x66    .......f
    0028   0x66                                       f
    decimal
              5    0  172    0    0   12    0    0
              7  163    4  227   64    2  192   36
              0  104    1  112    1   80    0    0
              0    0    6    5    0    0    4    0
              0    0    0    0    0    0    0  102
            102
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
`end logs/ReadHistoryData-page-30.data: 11 records`
