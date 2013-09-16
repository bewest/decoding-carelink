## START logs/ReadHistoryData-page-29.data
#### STOPPING DOUBLE NULLS @ 288, found 99 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x09 0x04 0x5a 0xef 0x00 0x0d 0x0d 0x00    ..Z.....
    0008   0x1c 0x00 0x08 0x1e 0x00 0x10 0x24 0x00    ......$.
    0010   0x18 0x1d 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
##### DEBUG DECIMAL
              9    4   90  239    0   13   13    0
             28    0    8   30    0   16   36    0
             24   29    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
#### RECORD 0 BolusWizard 2013-07-12T19:53:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-07-12T19:53:13)
    0000   0x4d 0xf5 0x13 0x6c 0x0d                   M..l.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x2c 0x00    .P.d<d,.
    0008   0x00 0x00 0x00 0x34 0x00 0x00 0x78         ...4..x
    decimal
              0   80    0  100   60  100   44    0
              0    0    0   52    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 1.1, 'curve': 192},
 {'age': 120, 'amount': 0.05, 'curve': 192},
 {'age': 130, 'amount': 1.35, 'curve': 192},
 {'age': 220, 'amount': 0.2, 'curve': 192},
 {'age': 230, 'amount': 2.2, 'curve': 192},
 {'age': 144, 'amount': 1.7, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x2c 0x28 0xc0 0x02 0x78 0xc0    \.,(..x.
    0008   0x36 0x82 0xc0 0x08 0xdc 0xc0 0x58 0xe6    6.....X.
    0010   0xc0 0x44 0x90 0xd0                        .D..
    decimal
             92   20   44   40  192    2  120  192
             54  130  192    8  220  192   88  230
            192   68  144  208
    datetime (unknown)

    body (0)

#### RECORD 2 CalBGForPH 2013-07-12T22:04:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 243}
```
    op hex (2)
    0000   0x0a 0xf3                                  ..
    decimal
             10  243
    datetime (2013-07-12T22:04:31)
    0000   0x5f 0xc4 0x36 0x0c 0x0d                   _.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 BolusWizard 2013-07-12T22:04:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 243,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0xf3                                  [.
    decimal
             91  243
    datetime (2013-07-12T22:04:40)
    0000   0x68 0xc4 0x16 0x6c 0x0d                   h..l.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x50 0x00    .P.d<dP.
    0008   0x58 0x00 0x00 0x04 0x00 0xa4 0x78         X.....x
    decimal
             22   80    0  100   60  100   80    0
             88    0    0    4    0  164  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 171, 'amount': 1.1, 'curve': 192},
 {'age': 251, 'amount': 0.05, 'curve': 192},
 {'age': 5, 'amount': 1.35, 'curve': 208},
 {'age': 95, 'amount': 0.2, 'curve': 208},
 {'age': 105, 'amount': 2.2, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x2c 0xab 0xc0 0x02 0xfb 0xc0    \.,.....
    0008   0x36 0x05 0xd0 0x08 0x5f 0xd0 0x58 0x69    6..._.Xi
    0010   0xd0                                       .
    decimal
             92   17   44  171  192    2  251  192
             54    5  208    8   95  208   88  105
            208
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-07-12T22:04:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x04 0x00    ........
    decimal
              1    0  164    0  164    0    4    0
    datetime (2013-07-12T22:04:40)
    0000   0x68 0xc4 0x56 0x6c 0x0d                   h.Vl.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2013-07-12T22:18:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 313}
```
    op hex (2)
    0000   0x0a 0x39                                  .9
    decimal
             10   57
    datetime (2013-07-12T22:18:50)
    0000   0x72 0xd2 0x36 0x0c 0x8d                   r.6..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 7 BolusWizard 2013-07-12T22:18:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 313,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 16.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 12.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x39                                  [9
    decimal
             91   57
    datetime (2013-07-12T22:18:59)
    0000   0x7b 0xd2 0x16 0x6c 0x0d                   {..l.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x80 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0xa0 0x00 0x00 0x78         ......x
    decimal
              0   81    0  100   60  100  128    0
              0    0    0  160    0    0  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 4.1, 'curve': 192},
 {'age': 185, 'amount': 1.1, 'curve': 192},
 {'age': 9, 'amount': 0.05, 'curve': 208},
 {'age': 19, 'amount': 1.35, 'curve': 208},
 {'age': 109, 'amount': 0.2, 'curve': 208},
 {'age': 119, 'amount': 2.2, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0xa4 0x0f 0xc0 0x2c 0xb9 0xc0    \....,..
    0008   0x02 0x09 0xd0 0x36 0x13 0xd0 0x08 0x6d    ...6...m
    0010   0xd0 0x58 0x77 0xd0                        .Xw.
    decimal
             92   20  164   15  192   44  185  192
              2    9  208   54   19  208    8  109
            208   88  119  208
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-07-12T22:18:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0xa0 0x00    ..4.4...
    decimal
              1    0   52    0   52    0  160    0
    datetime (2013-07-12T22:18:59)
    0000   0x7b 0xd2 0x56 0x6c 0x0d                   {.Vl.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 BasalProfileStart 2013-07-13T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-13T00:00:00)
    0000   0x40 0xc0 0x00 0x0d 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 0]
#### RECORD 11 ResultTotals (2000, 6, 0, 0, 13, 44) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xb4                   .....
    decimal
              7    0    0    4  180
    datetime ((2000, 6, 0, 0, 13, 44))
    0000   0x6c 0x8d 0x00 0x00 0x00                   l....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 12 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x6c 0x8d 0x05 0x00 0xc6 0x00 0x00    nl......
    0008   0x07 0x00 0x00 0x04 0xb4 0x02 0xd4 0x3c    .......<
    0010   0x01 0xe0 0x28 0x00 0x44 0x00 0xa8 0x00    ..(.D...
    0018   0x94 0x00 0xa4 0x00 0x00 0x03 0x02 0x01    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x68 0x39 0x00 0x00 0x00         ..h9...
    decimal
            110  108  141    5    0  198    0    0
              7    0    0    4  180    2  212   60
              1  224   40    0   68    0  168    0
            148    0  164    0    0    3    2    1
              0    4    0    0    0    0    0    0
              0    0  104   57    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 13 ChangeBasalProfile 2013-07-13T00:47:26 head[2], body[44] op[0x08]

    op hex (2)
    0000   0x08 0x04                                  ..
    decimal
              8    4
    datetime (2013-07-13T00:47:26)
    0000   0x5a 0xef 0x00 0x0d 0x0d                   Z....
    body (44)
    hex
    0000   0x00 0x1c 0x00 0x08 0x1e 0x00 0x10 0x24    .......$
    0008   0x00 0x18 0x1d 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00                        ....
    decimal
              0   28    0    8   30    0   16   36
              0   24   29    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0
    HOUR BITS: [1, 1, 1]
`end logs/ReadHistoryData-page-29.data: 14 records`
