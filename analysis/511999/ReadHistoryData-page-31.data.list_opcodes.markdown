## START logs/ReadHistoryData-page-31.data
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
#### RECORD 15 BasalProfileStart 2013-07-09T00:00:00 head[2], body[3] op[0x7b]

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
#### RECORD 16 ResultTotals (2000, 6, 0, 0, 13, 40) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x28                   ....(
    decimal
              7    0    0    5   40
    datetime ((2000, 6, 0, 0, 13, 40))
    0000   0x68 0x8d 0x00 0x00 0x00                   h....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 17 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x68 0x8d 0x05 0x00 0xa4 0x00 0x00    nh......
    0008   0x07 0x00 0x00 0x05 0x28 0x02 0xd4 0x37    ....(..7
    0010   0x02 0x54 0x2d 0x00 0x6e 0x01 0x14 0x00    .T-.n...
    0018   0x8c 0x00 0xb4 0x00 0x00 0x05 0x02 0x02    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6d 0x0a 0x00 0x00 0x00         ..m....
    decimal
            110  104  141    5    0  164    0    0
              7    0    0    5   40    2  212   55
              2   84   45    0  110    1   20    0
            140    0  180    0    0    5    2    2
              0    4    0    0    0    0    0    0
              0    0  109   10    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 18 CalBGForPH 2013-07-09T00:08:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-07-09T00:08:57)
    0000   0x79 0xc8 0x20 0x09 0x0d                   y. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 BolusWizard 2013-07-09T00:09:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 3.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-07-09T00:09:02)
    0000   0x42 0xc9 0x00 0x69 0x0d                   B..i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x6e 0x24 0x00    .P.x<n$.
    0008   0x00 0x00 0x00 0x3c 0x00 0x00 0x82         ...<...
    decimal
              0   80    0  120   60  110   36    0
              0    0    0   60    0    0  130
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 2.1, 'curve': 192},
 {'age': 19, 'amount': 2.0, 'curve': 208},
 {'age': 99, 'amount': 1.2, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x54 0x41 0xc0 0x50 0x13 0xd0    \.TA.P..
    0008   0x30 0x63 0xd0                             0c.
    decimal
             92   11   84   65  192   80   19  208
             48   99  208
    datetime (unknown)

    body (0)

#### RECORD 21 BasalProfileStart 2013-07-09T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-09T04:00:00)
    0000   0x40 0xc0 0x04 0x09 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 22 BasalProfileStart 2013-07-09T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-09T08:00:00)
    0000   0x40 0xc0 0x08 0x09 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 23 CalBGForPH 2013-07-09T09:06:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-07-09T09:06:10)
    0000   0x4a 0xc6 0x29 0x09 0x0d                   J.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 24 BolusWizard 2013-07-09T09:06:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 104,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x68                                  [h
    decimal
             91  104
    datetime (2013-07-09T09:06:16)
    0000   0x50 0xc6 0x09 0x69 0x0d                   P..i.
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x78         (....(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0    0    0   40  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 Bolus 2013-07-09T09:06:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2013-07-09T09:06:16)
    0000   0x50 0xc6 0x49 0x69 0x0d                   P.Ii.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 CalBGForPH 2013-07-09T09:58:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 219}
```
    op hex (2)
    0000   0x0a 0xdb                                  ..
    decimal
             10  219
    datetime (2013-07-09T09:58:20)
    0000   0x54 0xfa 0x29 0x09 0x0d                   T.)..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 27 BolusWizard 2013-07-09T09:58:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 219,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdb                                  [.
    decimal
             91  219
    datetime (2013-07-09T09:58:22)
    0000   0x56 0xfa 0x09 0x69 0x0d                   V..i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x40 0x00    .P.x<d@.
    0008   0x00 0x00 0x00 0x20 0x00 0x20 0x78         ... . x
    decimal
              0   80    0  120   60  100   64    0
              0    0    0   32    0   32  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 1.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x36 0xc0                   \.(6.
    decimal
             92    5   40   54  192
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-07-09T09:58:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x20 0x00    .. . . .
    decimal
              1    0   32    0   32    0   32    0
    datetime (2013-07-09T09:58:23)
    0000   0x57 0xfa 0x49 0x69 0x0d                   W.Ii.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 CalBGForPH 2013-07-09T10:28:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-09T10:28:51)
    0000   0x73 0xdc 0x2a 0x09 0x0d                   s.*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 31 BolusWizard 2013-07-09T10:28:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 102,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 9,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 28}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-07-09T10:28:57)
    0000   0x79 0xdc 0x0a 0x69 0x0d                   y..i.
    body (15)
    hex
    0000   0x09 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x1c 0x00 0x00 0x34 0x00 0x1c 0x78         ...4..x
    decimal
              9   80    0  120   60  100    0    0
             28    0    0   52    0   28  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 0.8, 'curve': 192},
 {'age': 84, 'amount': 1.0, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x20 0x22 0xc0 0x28 0x54 0xc0    \. ".(T.
    decimal
             92    8   32   34  192   40   84  192
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-07-09T10:28:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x34 0x00    ......4.
    decimal
              1    0   28    0   28    0   52    0
    datetime (2013-07-09T10:28:57)
    0000   0x79 0xdc 0x4a 0x69 0x0d                   y.Ji.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 ChangeTimeDisplay 2013-07-09T10:57:39 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-07-09T10:57:39)
    0000   0x67 0xf9 0x0a 0x09 0x0d                   g....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 35 ChangeTime 2013-07-09T10:58:03 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-07-09T10:58:03)
    0000   0x43 0xfa 0x0a 0x09 0x0d                   C....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 NewTimeSet 2013-07-09T12:57:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-07-09T12:57:00)
    0000   0x40 0xf9 0x0c 0x09 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 37 BasalProfileStart 2013-07-09T12:57:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-09T12:57:00)
    0000   0x40 0xf9 0x0c 0x09 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 1]
#### RECORD 38 Base (2013, 7, 9, 12, 57, 17) head[2], body[0] op[0x20]

    op hex (2)
    0000   0x20 0x00                                   .
    decimal
             32    0
    datetime ((2013, 7, 9, 12, 57, 17))
    0000   0x51 0xf9 0x0c 0x09 0x0d                   Q....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 CalBGForPH 2013-07-09T13:15:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2013-07-09T13:15:13)
    0000   0x4d 0xcf 0x2d 0x09 0x0d                   M.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 40 BolusWizard 2013-07-09T13:15:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 244,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf4                                  [.
    decimal
             91  244
    datetime (2013-07-09T13:15:16)
    0000   0x50 0xcf 0x0d 0x69 0x0d                   P..i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x50 0x00    .P.x<dP.
    0008   0x00 0x00 0x00 0x30 0x00 0x20 0x78         ...0. x
    decimal
              0   80    0  120   60  100   80    0
              0    0    0   48    0   32  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 0.7, 'curve': 192},
 {'age': 82, 'amount': 0.8, 'curve': 192},
 {'age': 132, 'amount': 1.0, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x1c 0x34 0xc0 0x20 0x52 0xc0    \..4. R.
    0008   0x28 0x84 0xc0                             (..
    decimal
             92   11   28   52  192   32   82  192
             40  132  192
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-07-09T13:15:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x30 0x00    .. . .0.
    decimal
              1    0   32    0   32    0   48    0
    datetime (2013-07-09T13:15:16)
    0000   0x50 0xcf 0x4d 0x69 0x0d                   P.Mi.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 43 CalBGForPH 2013-07-09T13:39:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-07-09T13:39:24)
    0000   0x58 0xe7 0x2d 0x09 0x0d                   X.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 BolusWizard 2013-07-09T13:39:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.4,
 'carb_input': 9,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 28}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-07-09T13:39:29)
    0000   0x5d 0xe7 0x0d 0x69 0x0d                   ]..i.
    body (15)
    hex
    0000   0x09 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x1c 0x00 0x00 0x40 0x00 0x1c 0x78         ...@..x
    decimal
              9   80    0  120   60  100    0    0
             28    0    0   64    0   28  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 0.8, 'curve': 192},
 {'age': 76, 'amount': 0.7, 'curve': 192},
 {'age': 106, 'amount': 0.8, 'curve': 192},
 {'age': 156, 'amount': 1.0, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0x20 0x1a 0xc0 0x1c 0x4c 0xc0    \. ...L.
    0008   0x20 0x6a 0xc0 0x28 0x9c 0xc0               j.(..
    decimal
             92   14   32   26  192   28   76  192
             32  106  192   40  156  192
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-07-09T13:39:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x40 0x00    ......@.
    decimal
              1    0   28    0   28    0   64    0
    datetime (2013-07-09T13:39:29)
    0000   0x5d 0xe7 0x4d 0x69 0x0d                   ].Mi.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 CalBGForPH 2013-07-09T17:40:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 201}
```
    op hex (2)
    0000   0x0a 0xc9                                  ..
    decimal
             10  201
    datetime (2013-07-09T17:40:02)
    0000   0x42 0xe8 0x31 0x09 0x0d                   B.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 BolusWizard 2013-07-09T17:40:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 201,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc9                                  [.
    decimal
             91  201
    datetime (2013-07-09T17:40:09)
    0000   0x49 0xe8 0x11 0x69 0x0d                   I..i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x34 0x00    .P.d<d4.
    0008   0x00 0x00 0x00 0x00 0x00 0x34 0x78         .....4x
    decimal
              0   80    0  100   60  100   52    0
              0    0    0    0    0   52  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 247, 'amount': 0.7, 'curve': 192},
 {'age': 11, 'amount': 0.8, 'curve': 208},
 {'age': 61, 'amount': 0.7, 'curve': 208},
 {'age': 91, 'amount': 0.8, 'curve': 208},
 {'age': 141, 'amount': 1.0, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x1c 0xf7 0xc0 0x20 0x0b 0xd0    \.... ..
    0008   0x1c 0x3d 0xd0 0x20 0x5b 0xd0 0x28 0x8d    .=. [.(.
    0010   0xd0                                       .
    decimal
             92   17   28  247  192   32   11  208
             28   61  208   32   91  208   40  141
            208
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2013-07-09T17:40:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    0    0
    datetime (2013-07-09T17:40:09)
    0000   0x49 0xe8 0x51 0x69 0x0d                   I.Qi.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 CalBGForPH 2013-07-09T18:54:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-07-09T18:54:05)
    0000   0x45 0xf6 0x32 0x09 0x0d                   E.2..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 BolusWizard 2013-07-09T18:54:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 33,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2013-07-09T18:54:13)
    0000   0x4d 0xf6 0x12 0x69 0x0d                   M..i.
    body (15)
    hex
    0000   0x21 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    !P.d<d..
    0008   0x84 0x00 0x00 0x1c 0x00 0x84 0x78         ......x
    decimal
             33   80    0  100   60  100    0    0
            132    0    0   28    0  132  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 53 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 81, 'amount': 1.3, 'curve': 192},
 {'age': 65, 'amount': 0.7, 'curve': 208},
 {'age': 85, 'amount': 0.8, 'curve': 208},
 {'age': 135, 'amount': 0.7, 'curve': 208},
 {'age': 165, 'amount': 0.8, 'curve': 208},
 {'age': 215, 'amount': 1.0, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x34 0x51 0xc0 0x1c 0x41 0xd0    \.4Q..A.
    0008   0x20 0x55 0xd0 0x1c 0x87 0xd0 0x20 0xa5     U.... .
    0010   0xd0 0x28 0xd7 0xd0                        .(..
    decimal
             92   20   52   81  192   28   65  208
             32   85  208   28  135  208   32  165
            208   40  215  208
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2013-07-09T18:54:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x1c 0x00    ........
    decimal
              1    0  132    0  132    0   28    0
    datetime (2013-07-09T18:54:13)
    0000   0x4d 0xf6 0x52 0x69 0x0d                   M.Ri.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 CalBGForPH 2013-07-09T20:42:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-07-09T20:42:39)
    0000   0x67 0xea 0x34 0x09 0x0d                   g.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 56 BolusWizard 2013-07-09T20:42:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 110,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-07-09T20:42:48)
    0000   0x70 0xea 0x14 0x69 0x0d                   p..i.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x3c 0x00 0x00 0x2c 0x00 0x3c 0x78         <..,.<x
    decimal
             15   80    0  100   60  100    0    0
             60    0    0   44    0   60  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 3.3, 'curve': 192},
 {'age': 189, 'amount': 1.3, 'curve': 192},
 {'age': 173, 'amount': 0.7, 'curve': 208},
 {'age': 193, 'amount': 0.8, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x84 0x6d 0xc0 0x34 0xbd 0xc0    \..m.4..
    0008   0x1c 0xad 0xd0 0x20 0xc1 0xd0              ... ..
    decimal
             92   14  132  109  192   52  189  192
             28  173  208   32  193  208
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-07-09T20:42:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x2c 0x00    ..<.<.,.
    decimal
              1    0   60    0   60    0   44    0
    datetime (2013-07-09T20:42:48)
    0000   0x70 0xea 0x54 0x69 0x0d                   p.Ti.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 TempBasal 2013-07-09T21:09:33 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.0}
```
    op hex (2)
    0000   0x33 0x50                                  3P
    decimal
             51   80
    datetime (2013-07-09T21:09:33)
    0000   0x61 0xc9 0x15 0x09 0x0d                   a....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 60 TempBasalDuration 2013-07-09T21:09:33 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-07-09T21:09:33)
    0000   0x61 0xc9 0x15 0x09 0x0d                   a....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 61 TempBasal 2013-07-09T21:52:59 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2013-07-09T21:52:59)
    0000   0x7b 0xf4 0x15 0x09 0x0d                   {....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 62 TempBasalDuration 2013-07-09T21:52:59 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2013-07-09T21:52:59)
    0000   0x7b 0xf4 0x15 0x09 0x0d                   {....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 63 BasalProfileStart 2013-07-09T21:52:59 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-09T21:52:59)
    0000   0x7b 0xf4 0x15 0x09 0x0d                   {....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 1]
#### RECORD 64 ChangeTimeDisplay 2013-07-09T21:54:26 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-07-09T21:54:26)
    0000   0x5a 0xf6 0x15 0x09 0x0d                   Z....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 65 ChangeTime 2013-07-09T21:54:49 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-07-09T21:54:49)
    0000   0x71 0xf6 0x15 0x09 0x0d                   q....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 66 NewTimeSet 2013-07-09T01:54:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-07-09T01:54:00)
    0000   0x40 0xf6 0x01 0x09 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 BasalProfileStart 2013-07-09T01:54:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-09T01:54:00)
    0000   0x40 0xf6 0x01 0x09 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 1]
#### RECORD 68 BasalProfileStart 2013-07-09T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-09T04:00:00)
    0000   0x40 0xc0 0x04 0x09 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 69 BasalProfileStart 2013-07-09T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-09T08:00:00)
    0000   0x40 0xc0 0x08 0x09 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 70 BasalProfileStart 2013-07-09T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-09T12:00:00)
    0000   0x40 0xc0 0x0c 0x09 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 71 CalBGForPH 2013-07-09T12:18:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-07-09T12:18:21)
    0000   0x55 0xd2 0x2c 0x09 0x0d                   U.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 BolusWizard 2013-07-09T12:18:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-07-09T12:18:28)
    0000   0x5c 0xd2 0x0c 0x69 0x0d                   \..i.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x78         P....Px
    decimal
             25   80    0  120   60  100    0    0
             80    0    0    0    0   80  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 73 Bolus 2013-07-09T12:18:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-07-09T12:18:28)
    0000   0x5c 0xd2 0x4c 0x69 0x0d                   \.Li.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 74 CalBGForPH 2013-07-09T16:01:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 358}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-09T16:01:57)
    0000   0x79 0xc1 0x30 0x09 0x8d                   y.0..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 75 BolusWizard 2013-07-09T16:02:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 358,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 15.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-07-09T16:02:02)
    0000   0x42 0xc2 0x10 0x69 0x0d                   B..i.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x9c 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x00 0x00 0x9c 0x78         ......x
    decimal
              0   81    0  120   60  100  156    0
              0    0    0    0    0  156  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 229, 'amount': 2.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0xe5 0xc0                   \.P..
    decimal
             92    5   80  229  192
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2013-07-09T16:02:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x00 0x00    ........
    decimal
              1    0  156    0  156    0    0    0
    datetime (2013-07-09T16:02:02)
    0000   0x42 0xc2 0x50 0x69 0x0d                   B.Pi.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 78 BasalProfileStart 2013-07-09T17:44:48 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-09T17:44:48)
    0000   0x70 0xec 0x11 0x09 0x0d                   p....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 1]
#### RECORD 79 Prime 2013-07-09T17:44:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-09T17:44:30)
    0000   0x5e 0xec 0x11 0x09 0x0d                   ^....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 80 Base unknown head[2], body[0] op[0xe3]

    op hex (2)
    0000   0xe3 0xdc                                  ..
    decimal
            227  220
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-31.data: 81 records`
