## START logs/ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 264, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x02 0x01 0x01 0x00 0x00 0x0c 0x00 0xe8    ........
    0008   0x00 0x00 0x00 0x21 0x00 0x49 0xf8 0x0a    ...!.I..
    0010   0x19 0x0d 0x03 0x00 0x00 0x00 0x21 0x64    ......!d
    0018   0xf9 0x2a 0x19 0x0d 0x03 0x00 0x05 0x00    .*......
##### DEBUG DECIMAL
              2    1    1    0    0   12    0  232
              0    0    0   33    0   73  248   10
             25   13    3    0    0    0   33  100
            249   42   25   13    3    0    5    0
#### RECORD 0 hack1 2013-07-23T21:10:46 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x76 0x8d 0x05 0x10 0xc2 0x5c 0x6d    mv....\m
    0008   0x03 0x00 0x00 0x04 0xc4 0x03 0x84 0x4a    .......J
    0010   0x01 0x40 0x1a 0x00 0x27 0x01 0x40 0x1a    .@..'.@.
    0018   0x00 0x6c 0x22 0x00 0xd4 0x42 0x00 0x00    .l"..B..
    0020   0x00 0x02 0x01 0x01 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0x60              .....`
    decimal
            109  118  141    5   16  194   92  109
              3    0    0    4  196    3  132   74
              1   64   26    0   39    1   64   26
              0  108   34    0  212   66    0    0
              0    2    1    1    0    0   12    0
            232    0    0    0   10   96
    datetime (2013-07-23T21:10:46)
    0000   0x6e 0xca 0x35 0x17 0x0d                   n.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 BolusWizard 2013-07-23T21:11:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 4.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2013-07-23T21:11:06)
    0000   0x46 0xcb 0x15 0x17 0x0d                   F....
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0xfe 0x31 0xf0    @P.-j.1.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             64   80   13   45  106  254   49  240
              0    0    0   47  125
    HOUR BITS: [1, 1, 0]
#### RECORD 2 Bolus 2013-07-23T21:11:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-07-23T21:11:06)
    0000   0x46 0xcb 0x55 0x17 0x0d                   F.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 LowReservoir 2013-07-23T22:50:31 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-23T22:50:31)
    0000   0x5f 0xf2 0x16 0x17 0x0d                   _....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 ResultTotals 2013-06-23T13:13:55 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x40                   ....@
    decimal
              7    0    0    4   64
    datetime (2013-06-23T13:13:55)
    0000   0x77 0x8d 0x6d 0x77 0x8d                   w.mw.
    body (51)
    hex
    0000   0x05 0x00 0x60 0x60 0x60 0x01 0x00 0x00    ..```...
    0008   0x04 0x40 0x03 0x84 0x53 0x00 0xbc 0x11    .@..S...
    0010   0x00 0x40 0x00 0xbc 0x11 0x00 0xbc 0x64    .@.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x03 0x78 0xc5 0x22 0x18 0x8d    ...x."..
    0030   0x5b 0x03 0x4c                             [.L
    decimal
              5    0   96   96   96    1    0    0
              4   64    3  132   83    0  188   17
              0   64    0  188   17    0  188  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0   10    3  120  197   34   24  141
             91    3   76
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 Base (2013, 0, 17, 0, 13, 24) head[2], body[0] op[0xc6]

    op hex (2)
    0000   0xc6 0x02                                  ..
    decimal
            198    2
    datetime ((2013, 0, 17, 0, 13, 24))
    0000   0x18 0x0d 0x00 0x51 0x0d                   ...Q.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 6 Base (2000, 0, 0, 0, 0, 29) head[2], body[0] op[0x2d]

    op hex (2)
    0000   0x2d 0x6a                                  -j
    decimal
             45  106
    datetime ((2000, 0, 0, 0, 0, 29))
    0000   0x1d 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 7 Base (2004, 5, 16, 8, 28, 61) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1d                                  ..
    decimal
              0   29
    datetime ((2004, 5, 16, 8, 28, 61))
    0000   0x7d 0x5c 0x08 0x10 0x24                   }\..$
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 8 SelectBasalProfile (2007, 0, 23, 1, 20, 46) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0xac                                  ..
    decimal
             20  172
    datetime ((2007, 0, 23, 1, 20, 46))
    0000   0x2e 0x14 0x01 0x17 0x17                   .....
    body (0)
    YEAR BITS: [0, 0, 0, 1]
#### RECORD 9 Base (2004, 13, 13, 24, 2, 6) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x4c                                  .L
    decimal
              0   76
    datetime ((2004, 13, 13, 24, 2, 6))
    0000   0xc6 0x42 0x18 0x0d 0x34                   .B..4
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 10 ChangeTimeDisplay (2010, 12, 13, 24, 8, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x40                                  d@
    decimal
            100   64
    datetime ((2010, 12, 13, 24, 8, 0))
    0000   0xc0 0x08 0x18 0x0d 0x0a                   .....
    body (0)

#### RECORD 11 Base (2011, 12, 13, 24, 54, 23) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0x70                                  fp
    decimal
            102  112
    datetime ((2011, 12, 13, 24, 54, 23))
    0000   0xd7 0x36 0x18 0x0d 0x5b                   .6..[
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 12 Base (2015, 12, 13, 24, 22, 24) head[2], body[0] op[0x66]

    op hex (2)
    0000   0x66 0x4e                                  fN
    decimal
            102   78
    datetime ((2015, 12, 13, 24, 22, 24))
    0000   0xd8 0x16 0x18 0x0d 0x2f                   ..../
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 13 Ian50 (2000, 1, 4, 31, 42, 45) head[2], body[34] op[0x50]

    op hex (2)
    0000   0x50 0x0d                                  P.
    decimal
             80   13
    datetime ((2000, 1, 4, 31, 42, 45))
    0000   0x2d 0x6a 0xff 0x24 0xf0                   -j.$.
    body (34)
    hex
    0000   0x00 0x00 0x00 0x23 0x7d 0x01 0x23 0x23    ...#}.##
    0008   0x00 0x4e 0xd8 0x56 0x18 0x0d 0x07 0x00    .N.V....
    0010   0x00 0x04 0x6c 0x78 0x8d 0x6d 0x78 0x8d    ..lx.mx.
    0018   0x05 0x10 0xb5 0x66 0x03 0x02 0x00 0x00    ...f....
    0020   0x04 0x6c                                  .l
    decimal
              0    0    0   35  125    1   35   35
              0   78  216   86   24   13    7    0
              0    4  108  120  141  109  120  141
              5   16  181  102    3    2    0    0
              4  108
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 14 Prime (2008, 0, 0, 15, 0, 20) head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 23.2, 'fixed': 8.0, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x84 0x50 0x00 0xe8                   ..P..
    decimal
              3  132   80    0  232
    datetime ((2008, 0, 0, 15, 0, 20))
    0000   0x14 0x00 0x2f 0x00 0xe8                   ../..
    body (0)
    YEAR BITS: [1, 1, 1, 0]
#### RECORD 15 SelectBasalProfile (2008, 8, 28, 0, 60, 12) head[2], body[0] op[0x14]

    op hex (2)
    0000   0x14 0x00                                  ..
    decimal
             20    0
    datetime ((2008, 8, 28, 0, 60, 12))
    0000   0x8c 0x3c 0x00 0x5c 0x28                   .<.\(
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 0]
`end logs/ReadHistoryData-page-4.data: 16 records`
