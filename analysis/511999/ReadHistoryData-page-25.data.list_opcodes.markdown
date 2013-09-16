## START logs/ReadHistoryData-page-25.data
#### STOPPING DOUBLE NULLS @ 237, found 99 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x09 0x04 0x5f 0xd0 0x09 0x0f 0x0d 0x00    .._.....
    0008   0x1f 0x00 0x08 0x21 0x00 0x10 0x22 0x00    ...!..".
    0010   0x18 0x1d 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              9    4   95  208    9   15   13    0
             31    0    8   33    0   16   34    0
             24   29    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.9, 'curve': 192},
 {'age': 98, 'amount': 2.7, 'curve': 192},
 {'age': 238, 'amount': 2.9, 'curve': 192},
 {'age': 72, 'amount': 2.0, 'curve': 208},
 {'age': 182, 'amount': 1.0, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x24 0x08 0xc0 0x6c 0x62 0xc0    \.$..lb.
    0008   0x74 0xee 0xc0 0x50 0x48 0xd0 0x28 0xb6    t..PH.(.
    0010   0xd0                                       .
    decimal
             92   17   36    8  192  108   98  192
            116  238  192   80   72  208   40  182
            208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-07-14T22:21:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x50 0x00    ..X.X.P.
    decimal
              1    0   88    0   88    0   80    0
    datetime (2013-07-14T22:21:51)
    0000   0x73 0xd5 0x56 0x6e 0x0d                   s.Vn.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-07-14T22:57:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-07-14T22:57:32)
    0000   0x60 0xf9 0x36 0x0e 0x0d                   `.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 BolusWizard 2013-07-14T22:57:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 12.4,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-07-14T22:57:41)
    0000   0x69 0xf9 0x16 0x6e 0x0d                   i..n.
    body (15)
    hex
    0000   0x13 0x50 0x00 0x64 0x3c 0x64 0x2c 0x00    .P.d<d,.
    0008   0x4c 0x00 0x00 0x7c 0x00 0x4c 0x78         L..|.Lx
    decimal
             19   80    0  100   60  100   44    0
             76    0    0  124    0   76  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 0.5, 'curve': 192},
 {'age': 44, 'amount': 2.6, 'curve': 192},
 {'age': 134, 'amount': 2.7, 'curve': 192},
 {'age': 18, 'amount': 2.9, 'curve': 208},
 {'age': 108, 'amount': 2.0, 'curve': 208},
 {'age': 218, 'amount': 1.0, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x14 0x22 0xc0 0x68 0x2c 0xc0    \..".h,.
    0008   0x6c 0x86 0xc0 0x74 0x12 0xd0 0x50 0x6c    l..t..Pl
    0010   0xd0 0x28 0xda 0xd0                        .(..
    decimal
             92   20   20   34  192  104   44  192
            108  134  192  116   18  208   80  108
            208   40  218  208
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-07-14T22:57:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x7c 0x00    ..L.L.|.
    decimal
              1    0   76    0   76    0  124    0
    datetime (2013-07-14T22:57:41)
    0000   0x69 0xf9 0x56 0x6e 0x0d                   i.Vn.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 BasalProfileStart 2013-07-15T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-15T00:00:00)
    0000   0x40 0xc0 0x00 0x0f 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1f 0x00                             ...
    decimal
              0   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 7 ResultTotals (2000, 6, 0, 0, 13, 46) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x33                   ....3
    decimal
              7    0    0    7   51
    datetime ((2000, 6, 0, 0, 13, 46))
    0000   0x6e 0x8d 0x00 0x00 0x00                   n....
    body (51)
    hex
    0000   0x6e 0x6e 0x8d 0x05 0x00 0xf8 0x00 0x00    nn......
    0008   0x0b 0x00 0x00 0x07 0x33 0x02 0xcb 0x27    ....3..'
    0010   0x04 0x68 0x3d 0x00 0x9a 0x01 0xac 0x01    .h=.....
    0018   0xf8 0x00 0xc4 0x00 0x00 0x04 0x05 0x02    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x82 0x4e 0x00 0x00 0x00 0x00    ...N....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  110  141    5    0  248    0    0
             11    0    0    7   51    2  203   39
              4  104   61    0  154    1  172    1
            248    0  196    0    0    4    5    2
              0    4    0    0    0    0    0    0
              0    0  130   78    0    0    0    0
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 8 Base (2015, 1, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2015, 1, 4, 0, 0, 1))
    0000   0x01 0x40 0xc0 0x04 0x0f                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 9 Base (2000, 0, 2, 27, 0, 31) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 31))
    0000   0x1f 0x00 0x7b 0x02 0x40                   ..{.@
    body (0)
    YEAR BITS: [0, 1, 0, 0]
#### RECORD 10 Base (2000, 0, 2, 16, 13, 15) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x08                                  ..
    decimal
            192    8
    datetime ((2000, 0, 2, 16, 13, 15))
    0000   0x0f 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 11 ChangeBasalProfile 2013-07-15T09:16:31 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x04                                  ..
    decimal
              8    4
    datetime (2013-07-15T09:16:31)
    0000   0x5f 0xd0 0x09 0x0f 0x0d                   _....
    body (44)
    hex
    0000   0x00 0x1f 0x00 0x08 0x1f 0x00 0x10 0x22    ......."
    0008   0x00 0x18 0x1d 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00                        ....
    decimal
              0   31    0    8   31    0   16   34
              0   24   29    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-25.data: 12 records`
