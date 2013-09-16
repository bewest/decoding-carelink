## START logs/ReadHistoryData-page-31.data
#### STOPPING DOUBLE NULLS @ 550, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x30 0x00 0x20 0x78 0x5c 0x0b 0x1c 0x34    0. x\..4
    0008   0xc0 0x20 0x52 0xc0 0x28 0x84 0xc0 0x01    . R.(...
    0010   0x00 0x20 0x00 0x20 0x00 0x30 0x00 0x50    . . .0.P
    0018   0xcf 0x4d 0x69 0x0d 0x0a 0x6b 0x58 0xe7    .Mi..kX.
##### DEBUG DECIMAL
             48    0   32  120   92   11   28   52
            192   32   82  192   40  132  192    1
              0   32    0   32    0   48    0   80
            207   77  105   13   10  107   88  231
#### RECORD 0 BolusWizard 2013-07-08T14:27:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-07-08T14:27:24)
    0000   0x58 0xdb 0x0e 0x68 0x0d                   X..h.
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x28 0x00 0x00 0x50 0x00 0x28 0x78         (..P.(x
    decimal
             13   80    0  120   60  100   44    0
             40    0    0   80    0   40  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 1.0, 'curve': 192},
 {'age': 53, 'amount': 1.1, 'curve': 192},
 {'age': 143, 'amount': 1.1, 'curve': 192},
 {'age': 7, 'amount': 1.6, 'curve': 208},
 {'age': 87, 'amount': 2.4, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0x0d 0xc0 0x2c 0x35 0xc0    \.(..,5.
    0008   0x2c 0x8f 0xc0 0x40 0x07 0xd0 0x60 0x57    ,..@..`W
    0010   0xd0                                       .
    decimal
             92   17   40   13  192   44   53  192
             44  143  192   64    7  208   96   87
            208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-07-08T14:27:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x50 0x00    ..`.`.P.
    decimal
              1    0   96    0   96    0   80    0
    datetime (2013-07-08T14:27:24)
    0000   0x58 0xdb 0x4e 0x68 0x0d                   X.Nh.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-07-08T18:19:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-07-08T18:19:20)
    0000   0x54 0xd3 0x32 0x08 0x0d                   T.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-07-08T18:19:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-07-08T18:19:25)
    0000   0x59 0xd3 0x12 0x68 0x0d                   Y..h.
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x78         0....0x
    decimal
             12   80    0  100   60  100    0    0
             48    0    0    0    0   48  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 235, 'amount': 2.4, 'curve': 192},
 {'age': 245, 'amount': 1.0, 'curve': 192},
 {'age': 29, 'amount': 1.1, 'curve': 208},
 {'age': 119, 'amount': 1.1, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x60 0xeb 0xc0 0x28 0xf5 0xc0    \.`..(..
    0008   0x2c 0x1d 0xd0 0x2c 0x77 0xd0              ,..,w.
    decimal
             92   14   96  235  192   40  245  192
             44   29  208   44  119  208
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-07-08T18:19:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-07-08T18:19:26)
    0000   0x5a 0xd3 0x52 0x68 0x0d                   Z.Rh.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 CalBGForPH 2013-07-08T19:34:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2013-07-08T19:34:35)
    0000   0x63 0xe2 0x33 0x08 0x0d                   c.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 8 BolusWizard 2013-07-08T19:34:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-07-08T19:34:47)
    0000   0x6f 0xe2 0x13 0x08 0x0d                   o....
    body (15)
    hex
    0000   0x14 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x50 0x00 0x00 0x1c 0x00 0x50 0x78         P....Px
    decimal
             20   80    0  100   60  100    0    0
             80    0    0   28    0   80  120
    HOUR BITS: [1, 1, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 80, 'amount': 1.2, 'curve': 192},
 {'age': 54, 'amount': 2.4, 'curve': 208},
 {'age': 64, 'amount': 1.0, 'curve': 208},
 {'age': 104, 'amount': 1.1, 'curve': 208},
 {'age': 194, 'amount': 1.1, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x30 0x50 0xc0 0x60 0x36 0xd0    \.0P.`6.
    0008   0x28 0x40 0xd0 0x2c 0x68 0xd0 0x2c 0xc2    (@.,h.,.
    0010   0xd0                                       .
    decimal
             92   17   48   80  192   96   54  208
             40   64  208   44  104  208   44  194
            208
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-07-08T19:34:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x1c 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   28    0
    datetime (2013-07-08T19:34:47)
    0000   0x6f 0xe2 0x53 0x08 0x0d                   o.S..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 CalBGForPH 2013-07-08T23:07:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-07-08T23:07:17)
    0000   0x51 0xc7 0x37 0x08 0x0d                   Q.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 BolusWizard 2013-07-08T23:07:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 19,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-07-08T23:07:29)
    0000   0x5d 0xc7 0x17 0x68 0x0d                   ]..h.
    body (15)
    hex
    0000   0x13 0x50 0x00 0x64 0x3c 0x64 0x08 0x00    .P.d<d..
    0008   0x4c 0x00 0x00 0x00 0x00 0x54 0x78         L....Tx
    decimal
             19   80    0  100   60  100    8    0
             76    0    0    0    0   84  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 213, 'amount': 2.0, 'curve': 192},
 {'age': 37, 'amount': 1.2, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0xd5 0xc0 0x30 0x25 0xd0    \.P..0%.
    decimal
             92    8   80  213  192   48   37  208
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-07-08T23:07:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x00 0x00    ..T.T...
    decimal
              1    0   84    0   84    0    0    0
    datetime (2013-07-08T23:07:30)
    0000   0x5e 0xc7 0x57 0x68 0x0d                   ^.Wh.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 Sara7B 2013-07-09T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-09T00:00:00)
    0000   0x40 0xc0 0x00 0x09 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 0]
#### RECORD 16 ResultTotals (2000, 6, 0, 0, 13, 40) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x28                   ....(
    decimal
              7    0    0    5   40
    datetime ((2000, 6, 0, 0, 13, 40))
    0000   0x68 0x8d 0x00 0x00 0x00                   h....
    body (51)
    hex
    0000   0x6e 0x68 0x8d 0x05 0x00 0xa4 0x00 0x00    nh......
    0008   0x07 0x00 0x00 0x05 0x28 0x02 0xd4 0x37    ....(..7
    0010   0x02 0x54 0x2d 0x00 0x6e 0x01 0x14 0x00    .T-.n...
    0018   0x8c 0x00 0xb4 0x00 0x00 0x05 0x02 0x02    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6d 0x0a 0x00 0x00 0x00 0x00    ..m.....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  104  141    5    0  164    0    0
              7    0    0    5   40    2  212   55
              2   84   45    0  110    1   20    0
            140    0  180    0    0    5    2    2
              0    4    0    0    0    0    0    0
              0    0  109   10    0    0    0    0
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 17 Base (2009, 9, 0, 8, 57, 58) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x0a                                  ..
    decimal
              0   10
    datetime ((2009, 9, 0, 8, 57, 58))
    0000   0xba 0x79 0xc8 0x20 0x09                   .y. .
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1]
#### RECORD 18 Base (2009, 9, 0, 9, 2, 58) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x5b                                  .[
    decimal
             13   91
    datetime ((2009, 9, 0, 9, 2, 58))
    0000   0xba 0x42 0xc9 0x00 0x69                   .B..i
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 Base (2014, 4, 28, 24, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2014, 4, 28, 24, 0, 16))
    0000   0x50 0x00 0x78 0x3c 0x6e                   P.x<n
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 20 Base (2000, 0, 28, 0, 0, 0) head[2], body[0] op[0x24]

    op hex (2)
    0000   0x24 0x00                                  $.
    decimal
             36    0
    datetime ((2000, 0, 28, 0, 0, 0))
    0000   0x00 0x00 0x00 0x3c 0x00                   ...<.
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 21 Base (2000, 4, 1, 20, 11, 28) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x82                                  ..
    decimal
              0  130
    datetime ((2000, 4, 1, 20, 11, 28))
    0000   0x5c 0x0b 0x54 0x41 0xc0                   \.TA.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 22 Base (2011, 12, 16, 3, 48, 16) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x13                                  P.
    decimal
             80   19
    datetime ((2011, 12, 16, 3, 48, 16))
    0000   0xd0 0x30 0x63 0xd0 0x7b                   .0c.{
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 23 Bolus (2000, 1, 0, 2, 59, 0) head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.4, 'dual_component': '??', 'programmed': 19.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x40 0xc0 0x04 0x09 0x0d 0x08 0x1e    .@......
    decimal
              1   64  192    4    9   13    8   30
    datetime ((2000, 1, 0, 2, 59, 0))
    0000   0x00 0x7b 0x02 0x40 0xc0                   .{.@.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 0]
#### RECORD 24 ChangeBasalProfile (2010, 0, 0, 4, 16, 13) head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x09                                  ..
    decimal
              8    9
    datetime ((2010, 0, 0, 4, 16, 13))
    0000   0x0d 0x10 0x24 0x00 0x0a                   ..$..
    body (44)
    hex
    0000   0x68 0x4a 0xc6 0x29 0x09 0x0d 0x5b 0x68    hJ.)..[h
    0008   0x50 0xc6 0x09 0x69 0x0d 0x0d 0x50 0x00    P..i..P.
    0010   0x78 0x3c 0x64 0x00 0x00 0x28 0x00 0x00    x<d..(..
    0018   0x00 0x00 0x28 0x78 0x01 0x00 0x28 0x00    ..(x..(.
    0020   0x28 0x00 0x00 0x00 0x50 0xc6 0x49 0x69    (...P.Ii
    0028   0x0d 0x0a 0xdb 0x54                        ...T
    decimal
            104   74  198   41    9   13   91  104
             80  198    9  105   13   13   80    0
            120   60  100    0    0   40    0    0
              0    0   40  120    1    0   40    0
             40    0    0    0   80  198   73  105
             13   10  219   84

#### RECORD 25 Base (2006, 0, 27, 27, 13, 9) head[2], body[0] op[0xfa]

    op hex (2)
    0000   0xfa 0x29                                  .)
    decimal
            250   41
    datetime ((2006, 0, 27, 27, 13, 9))
    0000   0x09 0x0d 0x5b 0xdb 0x56                   ..[.V
    body (0)
    DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 0, 1]
#### RECORD 26 Base (2000, 4, 16, 0, 13, 41) head[2], body[0] op[0xfa]

    op hex (2)
    0000   0xfa 0x09                                  ..
    decimal
            250    9
    datetime ((2000, 4, 16, 0, 13, 41))
    0000   0x69 0x0d 0x00 0x50 0x00                   i..P.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 27 Base (2000, 5, 0, 0, 0, 36) head[2], body[0] op[0x78]

    op hex (2)
    0000   0x78 0x3c                                  x<
    decimal
            120   60
    datetime ((2000, 5, 0, 0, 0, 36))
    0000   0x64 0x40 0x00 0x00 0x00                   d@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 28 Base (2005, 0, 28, 24, 32, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x20                                  . 
    decimal
              0   32
    datetime ((2005, 0, 28, 24, 32, 0))
    0000   0x00 0x20 0x78 0x5c 0x05                   . x\.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
#### RECORD 29 Base (2000, 12, 0, 0, 1, 0) head[2], body[0] op[0x28]

    op hex (2)
    0000   0x28 0x36                                  (6
    decimal
             40   54
    datetime ((2000, 12, 0, 0, 1, 0))
    0000   0xc0 0x01 0x00 0x20 0x00                   ... .
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 30 Base (2009, 0, 26, 23, 0, 32) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2009, 0, 26, 23, 0, 32))
    0000   0x20 0x00 0x57 0xfa 0x49                    .W.I
    body (0)
    DAY BITS: [1, 1, 1] YEAR BITS: [0, 1, 0, 0]
#### RECORD 31 Base (2010, 1, 28, 19, 38, 10) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x0d                                  i.
    decimal
            105   13
    datetime ((2010, 1, 28, 19, 38, 10))
    0000   0x0a 0x66 0x73 0xdc 0x2a                   .fs.*
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 0] YEAR BITS: [0, 0, 1, 0]
#### RECORD 32 Base (2010, 5, 28, 25, 38, 27) head[2], body[0] op[0x09]

    op hex (2)
    0000   0x09 0x0d                                  ..
    decimal
              9   13
    datetime ((2010, 5, 28, 25, 38, 27))
    0000   0x5b 0x66 0x79 0xdc 0x0a                   [fy..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 1, 0]
#### RECORD 33 Base (2012, 1, 24, 0, 16, 9) head[2], body[0] op[0x69]

    op hex (2)
    0000   0x69 0x0d                                  i.
    decimal
            105   13
    datetime ((2012, 1, 24, 0, 16, 9))
    0000   0x09 0x50 0x00 0x78 0x3c                   .P.x<
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 1, 1]
#### RECORD 34 ChangeTimeDisplay (2004, 0, 0, 0, 28, 0) head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime ((2004, 0, 0, 0, 28, 0))
    0000   0x00 0x1c 0x00 0x00 0x34                   ....4
    body (0)
    YEAR BITS: [0, 0, 1, 1]
#### RECORD 35 Base (2002, 5, 0, 8, 28, 56) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2002, 5, 0, 8, 28, 56))
    0000   0x78 0x5c 0x08 0x20 0x22                   x\. "
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 0]
#### RECORD 36 Base (2012, 7, 0, 1, 0, 20) head[2], body[0] op[0xc0]

    op hex (2)
    0000   0xc0 0x28                                  .(
    decimal
            192   40
    datetime ((2012, 7, 0, 1, 0, 20))
    0000   0x54 0xc0 0x01 0x00 0x1c                   T....
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [0, 0, 0, 1]
#### RECORD 37 Base (2012, 0, 25, 0, 52, 0) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x1c                                  ..
    decimal
              0   28
    datetime ((2012, 0, 25, 0, 52, 0))
    0000   0x00 0x34 0x00 0x79 0xdc                   .4.y.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 0, 1]
#### RECORD 38 Base (2009, 1, 7, 0, 36, 13) head[2], body[0] op[0x4a]

    op hex (2)
    0000   0x4a 0x69                                  Ji
    decimal
             74  105
    datetime ((2009, 1, 7, 0, 36, 13))
    0000   0x0d 0x64 0x00 0x67 0xf9                   .d.g.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 39 CalBGForPH (2010, 0, 3, 0, 23, 13) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 265}
```
    op hex (2)
    0000   0x0a 0x09                                  ..
    decimal
             10    9
    datetime ((2010, 0, 3, 0, 23, 13))
    0000   0x0d 0x17 0x00 0x43 0xfa                   ...C.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 40 CalBGForPH (2009, 0, 0, 0, 24, 13) head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 265}
```
    op hex (2)
    0000   0x0a 0x09                                  ..
    decimal
             10    9
    datetime ((2009, 0, 0, 0, 24, 13))
    0000   0x0d 0x18 0x00 0x40 0xf9                   ...@.
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 41 ClearAlarm (2009, 1, 0, 3, 59, 13) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x09                                  ..
    decimal
             12    9
    datetime ((2009, 1, 0, 3, 59, 13))
    0000   0x0d 0x7b 0x03 0x40 0xf9                   .{.@.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 1, 1]
#### RECORD 42 ClearAlarm (2000, 0, 0, 29, 24, 13) head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x09                                  ..
    decimal
             12    9
    datetime ((2000, 0, 0, 29, 24, 13))
    0000   0x0d 0x18 0x1d 0x00 0x20                   .... 
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 43 Base (2010, 12, 13, 9, 12, 57) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x51                                  .Q
    decimal
              0   81
    datetime ((2010, 12, 13, 9, 12, 57))
    0000   0xf9 0x0c 0x09 0x0d 0x0a                   .....
    body (0)

#### RECORD 44 Base (2011, 12, 13, 9, 45, 15) head[2], body[0] op[0xf4]

    op hex (2)
    0000   0xf4 0x4d                                  .M
    decimal
            244   77
    datetime ((2011, 12, 13, 9, 45, 15))
    0000   0xcf 0x2d 0x09 0x0d 0x5b                   .-..[
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 45 Base (2000, 12, 13, 9, 13, 15) head[2], body[0] op[0xf4]

    op hex (2)
    0000   0xf4 0x50                                  .P
    decimal
            244   80
    datetime ((2000, 12, 13, 9, 13, 15))
    0000   0xcf 0x0d 0x69 0x0d 0x00                   ..i..
    body (0)

#### RECORD 46 Base (2000, 4, 16, 4, 60, 56) head[2], body[0] op[0x50]

    op hex (2)
    0000   0x50 0x00                                  P.
    decimal
             80    0
    datetime ((2000, 4, 16, 4, 60, 56))
    0000   0x78 0x3c 0x64 0x50 0x00                   x<dP.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-31.data: 47 records`
