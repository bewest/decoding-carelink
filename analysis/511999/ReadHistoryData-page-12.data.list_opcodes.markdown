## START analysis/sarak/raw//ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x08 0xa5                                  ..
##### DEBUG DECIMAL
              8  165
#### RECORD 0 Bolus 2013-08-08T16:07:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x74 0x00    ......t.
    decimal
              1    0   28    0   28    0  116    0
    datetime (2013-08-08T16:07:44)
    0000   0xac 0x07 0x50 0x08 0x0d                   ..P..
    body (0)

#### RECORD 1 CalBGForPH 2013-08-08T17:39:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2013-08-08T17:39:47)
    0000   0xaf 0x27 0x31 0x08 0x0d                   .'1..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 BolusWizard 2013-08-08T17:39:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 185,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb9                                  [.
    decimal
             91  185
    datetime (2013-08-08T17:39:51)
    0000   0xb3 0x27 0x11 0x08 0x0d                   .'...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x28 0x00    .P.d<d(.
    0008   0x00 0x00 0x00 0x20 0x00 0x08 0x78         ... ..x
    decimal
              0   80    0  100   60  100   40    0
              0    0    0   32    0    8  120
    HOUR BITS: [0, 0, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 0.7, 'curve': 192},
 {'age': 126, 'amount': 0.8, 'curve': 192},
 {'age': 136, 'amount': 0.8, 'curve': 192},
 {'age': 156, 'amount': 1.3, 'curve': 192},
 {'age': 206, 'amount': 2.1, 'curve': 192},
 {'age': 0, 'amount': 0.6, 'curve': 208},
 {'age': 100, 'amount': 1.3, 'curve': 208},
 {'age': 170, 'amount': 1.2, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x1c 0x60 0xc0 0x20 0x7e 0xc0    \..`. ~.
    0008   0x20 0x88 0xc0 0x34 0x9c 0xc0 0x54 0xce     ..4..T.
    0010   0xc0 0x18 0x00 0xd0 0x34 0x64 0xd0 0x30    ....4d.0
    0018   0xaa 0xd0                                  ..
    decimal
             92   26   28   96  192   32  126  192
             32  136  192   52  156  192   84  206
            192   24    0  208   52  100  208   48
            170  208
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-08-08T17:39:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x20 0x00    ...... .
    decimal
              1    0   20    0   20    0   32    0
    datetime (2013-08-08T17:39:51)
    0000   0xb3 0x27 0x51 0x08 0x0d                   .'Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 CalBGForPH 2013-08-08T18:45:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-08T18:45:32)
    0000   0xa0 0x2d 0x32 0x08 0x0d                   .-2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 BolusWizard 2013-08-08T18:45:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-08T18:45:37)
    0000   0xa5 0x2d 0x12 0x08 0x0d                   .-...
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x2c 0x00 0x00 0x10 0x00 0x2c 0x78         ,....,x
    decimal
             11   80    0  100   60  100    0    0
             44    0    0   16    0   44  120
    HOUR BITS: [0, 0, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 0.5, 'curve': 192},
 {'age': 162, 'amount': 0.7, 'curve': 192},
 {'age': 192, 'amount': 0.8, 'curve': 192},
 {'age': 202, 'amount': 0.8, 'curve': 192},
 {'age': 222, 'amount': 1.3, 'curve': 192},
 {'age': 16, 'amount': 2.1, 'curve': 208},
 {'age': 66, 'amount': 0.6, 'curve': 208},
 {'age': 166, 'amount': 1.3, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x14 0x48 0xc0 0x1c 0xa2 0xc0    \..H....
    0008   0x20 0xc0 0xc0 0x20 0xca 0xc0 0x34 0xde     .. ..4.
    0010   0xc0 0x54 0x10 0xd0 0x18 0x42 0xd0 0x34    .T...B.4
    0018   0xa6 0xd0                                  ..
    decimal
             92   26   20   72  192   28  162  192
             32  192  192   32  202  192   52  222
            192   84   16  208   24   66  208   52
            166  208
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-08-08T18:45:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x10 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   16    0
    datetime (2013-08-08T18:45:37)
    0000   0xa5 0x2d 0x52 0x08 0x0d                   .-R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 9 CalBGForPH 2013-08-08T18:53:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 149}
```
    op hex (2)
    0000   0x0a 0x95                                  ..
    decimal
             10  149
    datetime (2013-08-08T18:53:45)
    0000   0xad 0x35 0x32 0x08 0x0d                   .52..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 10 BolusWizard 2013-08-08T18:53:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 149,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.0,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 1.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x95                                  [.
    decimal
             91  149
    datetime (2013-08-08T18:53:52)
    0000   0xb4 0x35 0x12 0x08 0x0d                   .5...
    body (15)
    hex
    0000   0x10 0x50 0x00 0x64 0x3c 0x64 0x10 0x00    .P.d<d..
    0008   0x40 0x00 0x00 0x3c 0x00 0x40 0x78         @..<.@x
    decimal
             16   80    0  100   60  100   16    0
             64    0    0   60    0   64  120
    HOUR BITS: [0, 0, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 1.1, 'curve': 192},
 {'age': 80, 'amount': 0.5, 'curve': 192},
 {'age': 170, 'amount': 0.7, 'curve': 192},
 {'age': 200, 'amount': 0.8, 'curve': 192},
 {'age': 210, 'amount': 0.8, 'curve': 192},
 {'age': 230, 'amount': 1.3, 'curve': 192},
 {'age': 24, 'amount': 2.1, 'curve': 208},
 {'age': 74, 'amount': 0.6, 'curve': 208},
 {'age': 174, 'amount': 1.3, 'curve': 208}]
```
    op hex (29)
    0000   0x5c 0x1d 0x2c 0x0a 0xc0 0x14 0x50 0xc0    \.,...P.
    0008   0x1c 0xaa 0xc0 0x20 0xc8 0xc0 0x20 0xd2    ... .. .
    0010   0xc0 0x34 0xe6 0xc0 0x54 0x18 0xd0 0x18    .4..T...
    0018   0x4a 0xd0 0x34 0xae 0xd0                   J.4..
    decimal
             92   29   44   10  192   20   80  192
             28  170  192   32  200  192   32  210
            192   52  230  192   84   24  208   24
             74  208   52  174  208
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2013-08-08T18:53:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x3c 0x00    ..@.@.<.
    decimal
              1    0   64    0   64    0   60    0
    datetime (2013-08-08T18:53:53)
    0000   0xb5 0x35 0x52 0x08 0x0d                   .5R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 CalBGForPH 2013-08-08T19:29:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2013-08-08T19:29:59)
    0000   0xbb 0x1d 0x33 0x08 0x0d                   ..3..
    body (0)

#### RECORD 14 BolusWizard 2013-08-08T19:30:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2013-08-08T19:30:10)
    0000   0x8a 0x1e 0x13 0x08 0x0d                   .....
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x64 0x3c 0x64 0x24 0x00    .P.d<d$.
    0008   0x30 0x00 0x00 0x64 0x00 0x30 0x78         0..d.0x
    decimal
             12   80    0  100   60  100   36    0
             48    0    0  100    0   48  120

#### RECORD 15 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 37, 'amount': 1.6, 'curve': 192},
 {'age': 47, 'amount': 1.1, 'curve': 192},
 {'age': 117, 'amount': 0.5, 'curve': 192},
 {'age': 207, 'amount': 0.7, 'curve': 192},
 {'age': 237, 'amount': 0.8, 'curve': 192},
 {'age': 247, 'amount': 0.8, 'curve': 192},
 {'age': 11, 'amount': 1.3, 'curve': 208},
 {'age': 61, 'amount': 2.1, 'curve': 208},
 {'age': 111, 'amount': 0.6, 'curve': 208},
 {'age': 211, 'amount': 1.3, 'curve': 208}]
```
    op hex (32)
    0000   0x5c 0x20 0x40 0x25 0xc0 0x2c 0x2f 0xc0    \ @%.,/.
    0008   0x14 0x75 0xc0 0x1c 0xcf 0xc0 0x20 0xed    .u.... .
    0010   0xc0 0x20 0xf7 0xc0 0x34 0x0b 0xd0 0x54    . ..4..T
    0018   0x3d 0xd0 0x18 0x6f 0xd0 0x34 0xd3 0xd0    =..o.4..
    decimal
             92   32   64   37  192   44   47  192
             20  117  192   28  207  192   32  237
            192   32  247  192   52   11  208   84
             61  208   24  111  208   52  211  208
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-08-08T19:30:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x64 0x00    ..0.0.d.
    decimal
              1    0   48    0   48    0  100    0
    datetime (2013-08-08T19:30:11)
    0000   0x8b 0x1e 0x53 0x08 0x0d                   ..S..
    body (0)

#### RECORD 17 CalBGForPH 2013-08-08T20:06:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-08-08T20:06:19)
    0000   0x93 0x06 0x34 0x08 0x0d                   ..4..
    body (0)

#### RECORD 18 BolusWizard 2013-08-08T20:06:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.4,
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
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-08-08T20:06:53)
    0000   0xb5 0x06 0x14 0x08 0x0d                   .....
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x3c 0x00 0x00 0x68 0x00 0x3c 0x78         <..h.<x
    decimal
             15   80    0  100   60  100    0    0
             60    0    0  104    0   60  120

#### RECORD 19 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 1.2, 'curve': 192},
 {'age': 73, 'amount': 1.6, 'curve': 192},
 {'age': 83, 'amount': 1.1, 'curve': 192},
 {'age': 153, 'amount': 0.5, 'curve': 192},
 {'age': 243, 'amount': 0.7, 'curve': 192},
 {'age': 17, 'amount': 0.8, 'curve': 208},
 {'age': 27, 'amount': 0.8, 'curve': 208},
 {'age': 47, 'amount': 1.3, 'curve': 208},
 {'age': 97, 'amount': 2.1, 'curve': 208},
 {'age': 147, 'amount': 0.6, 'curve': 208}]
```
    op hex (32)
    0000   0x5c 0x20 0x30 0x2b 0xc0 0x40 0x49 0xc0    \ 0+.@I.
    0008   0x2c 0x53 0xc0 0x14 0x99 0xc0 0x1c 0xf3    ,S......
    0010   0xc0 0x20 0x11 0xd0 0x20 0x1b 0xd0 0x34    . .. ..4
    0018   0x2f 0xd0 0x54 0x61 0xd0 0x18 0x93 0xd0    /.Ta....
    decimal
             92   32   48   43  192   64   73  192
             44   83  192   20  153  192   28  243
            192   32   17  208   32   27  208   52
             47  208   84   97  208   24  147  208
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2013-08-08T20:06:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x68 0x00    ..D.D.h.
    decimal
              1    0   68    0   68    0  104    0
    datetime (2013-08-08T20:06:53)
    0000   0xb5 0x06 0x54 0x08 0x0d                   ..T..
    body (0)

#### RECORD 21 CalBGForPH 2013-08-08T21:55:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2013-08-08T21:55:29)
    0000   0x9d 0x37 0x35 0x08 0x0d                   .75..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 BolusWizard 2013-08-08T21:55:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 216,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
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
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2013-08-08T21:55:31)
    0000   0x9f 0x37 0x15 0x08 0x0d                   .7...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x40 0x00    .P.d<d@.
    0008   0x00 0x00 0x00 0x1c 0x00 0x24 0x78         .....$x
    decimal
              0   80    0  100   60  100   64    0
              0    0    0   28    0   36  120
    HOUR BITS: [0, 0, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 1.7, 'curve': 192},
 {'age': 152, 'amount': 1.2, 'curve': 192},
 {'age': 182, 'amount': 1.6, 'curve': 192},
 {'age': 192, 'amount': 1.1, 'curve': 192},
 {'age': 6, 'amount': 0.5, 'curve': 208},
 {'age': 96, 'amount': 0.7, 'curve': 208},
 {'age': 126, 'amount': 0.8, 'curve': 208},
 {'age': 136, 'amount': 0.8, 'curve': 208},
 {'age': 156, 'amount': 1.3, 'curve': 208},
 {'age': 206, 'amount': 2.1, 'curve': 208}]
```
    op hex (32)
    0000   0x5c 0x20 0x44 0x70 0xc0 0x30 0x98 0xc0    \ Dp.0..
    0008   0x40 0xb6 0xc0 0x2c 0xc0 0xc0 0x14 0x06    @..,....
    0010   0xd0 0x1c 0x60 0xd0 0x20 0x7e 0xd0 0x20    ..`. ~. 
    0018   0x88 0xd0 0x34 0x9c 0xd0 0x54 0xce 0xd0    ..4..T..
    decimal
             92   32   68  112  192   48  152  192
             64  182  192   44  192  192   20    6
            208   28   96  208   32  126  208   32
            136  208   52  156  208   84  206  208
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2013-08-08T21:55:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x1c 0x00    ..$.$...
    decimal
              1    0   36    0   36    0   28    0
    datetime (2013-08-08T21:55:31)
    0000   0x9f 0x37 0x55 0x08 0x0d                   .7U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 25 CalBGForPH 2013-08-08T23:18:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-08-08T23:18:06)
    0000   0x86 0x12 0x37 0x08 0x0d                   ..7..
    body (0)

#### RECORD 26 BolusWizard 2013-08-08T23:18:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 128,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x80                                  [.
    decimal
             91  128
    datetime (2013-08-08T23:18:12)
    0000   0x8c 0x12 0x17 0x08 0x0d                   .....
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x04 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0x14 0x00 0x38 0x78         8....8x
    decimal
             14   80    0  100   60  100    4    0
             56    0    0   20    0   56  120

#### RECORD 27 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 0.9, 'curve': 192},
 {'age': 195, 'amount': 1.7, 'curve': 192},
 {'age': 235, 'amount': 1.2, 'curve': 192},
 {'age': 9, 'amount': 1.6, 'curve': 208},
 {'age': 19, 'amount': 1.1, 'curve': 208},
 {'age': 89, 'amount': 0.5, 'curve': 208},
 {'age': 179, 'amount': 0.7, 'curve': 208},
 {'age': 209, 'amount': 0.8, 'curve': 208},
 {'age': 219, 'amount': 0.8, 'curve': 208}]
```
    op hex (29)
    0000   0x5c 0x1d 0x24 0x55 0xc0 0x44 0xc3 0xc0    \.$U.D..
    0008   0x30 0xeb 0xc0 0x40 0x09 0xd0 0x2c 0x13    0..@..,.
    0010   0xd0 0x14 0x59 0xd0 0x1c 0xb3 0xd0 0x20    ..Y.... 
    0018   0xd1 0xd0 0x20 0xdb 0xd0                   .. ..
    decimal
             92   29   36   85  192   68  195  192
             48  235  192   64    9  208   44   19
            208   20   89  208   28  179  208   32
            209  208   32  219  208
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2013-08-08T23:18:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x14 0x00    ..8.8...
    decimal
              1    0   56    0   56    0   20    0
    datetime (2013-08-08T23:18:12)
    0000   0x8c 0x12 0x57 0x08 0x0d                   ..W..
    body (0)

#### RECORD 29 BasalProfileStart 2013-08-09T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-09T00:00:00)
    0000   0x80 0x00 0x00 0x09 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 30 MResultTotals 2013-08-09T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xf7                   .....
    decimal
              7    0    0    5  247
    datetime (2013-08-09T00:00:00)
    0000   0x88 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 31 Sara6E 2013-08-09T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-09T00:00:00)
    0000   0x88 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0x9f 0x00 0x00 0x0e 0x00 0x00    ........
    0008   0x05 0xf7 0x02 0xdb 0x30 0x03 0x1c 0x34    ....0..4
    0010   0x00 0x9e 0x01 0xc4 0x00 0x54 0x00 0xa8    .....T..
    0018   0x00 0x5c 0x08 0x04 0x03 0x02 0x00 0x00    .\......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x64    .......d
    0028   0xd8 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  159    0    0   14    0    0
              5  247    2  219   48    3   28   52
              0  158    1  196    0   84    0  168
              0   92    8    4    3    2    0    0
              0    0    0    0    0    0    0  100
            216    0    0    0    0    0    0    0
              0

#### RECORD 32 BasalProfileStart 2013-08-09T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-09T04:00:00)
    0000   0x80 0x00 0x04 0x09 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 33 BasalProfileStart 2013-08-09T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-09T08:00:00)
    0000   0x80 0x00 0x08 0x09 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 34 CalBGForPH 2013-08-09T10:19:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-08-09T10:19:25)
    0000   0x99 0x13 0x2a 0x09 0x0d                   ..*..
    body (0)

#### RECORD 35 BolusWizard 2013-08-09T10:19:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 118,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x76                                  [v
    decimal
             91  118
    datetime (2013-08-09T10:19:31)
    0000   0x9f 0x13 0x0a 0x09 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x44 0x00 0x00 0x00 0x00 0x44 0x78         D....Dx
    decimal
             21   80    0  120   60  100    0    0
             68    0    0    0    0   68  120

#### RECORD 36 Bolus 2013-08-09T10:19:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2013-08-09T10:19:31)
    0000   0x9f 0x13 0x4a 0x09 0x0d                   ..J..
    body (0)

#### RECORD 37 CalBGForPH 2013-08-09T11:58:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-08-09T11:58:44)
    0000   0xac 0x3a 0x2b 0x09 0x0d                   .:+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 38 BolusWizard 2013-08-09T11:58:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.4,
 'carb_input': 12,
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
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-08-09T11:58:52)
    0000   0xb4 0x3a 0x0b 0x09 0x0d                   .:...
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x18 0x00 0x28 0x78         (....(x
    decimal
             12   80    0  120   60  100    0    0
             40    0    0   24    0   40  120
    HOUR BITS: [0, 0, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 105, 'amount': 1.7, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x44 0x69 0xc0                   \.Di.
    decimal
             92    5   68  105  192
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-08-09T11:58:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x18 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   24    0
    datetime (2013-08-09T11:58:52)
    0000   0xb4 0x3a 0x4b 0x09 0x0d                   .:K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 BasalProfileStart 2013-08-09T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-09T12:00:00)
    0000   0x80 0x00 0x0c 0x09 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 42 CalBGForPH 2013-08-09T14:07:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-09T14:07:22)
    0000   0x96 0x07 0x2e 0x09 0x0d                   .....
    body (0)

#### RECORD 43 BolusWizard 2013-08-09T14:07:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-09T14:07:28)
    0000   0x9c 0x07 0x0e 0x09 0x0d                   .....
    body (15)
    hex
    0000   0x11 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x38 0x00 0x00 0x08 0x00 0x38 0x78         8....8x
    decimal
             17   80    0  120   60  100    0    0
             56    0    0    8    0   56  120

#### RECORD 44 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 134, 'amount': 1.0, 'curve': 192},
 {'age': 234, 'amount': 1.7, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x86 0xc0 0x44 0xea 0xc0    \.(..D..
    decimal
             92    8   40  134  192   68  234  192
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-08-09T14:07:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x08 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    8    0
    datetime (2013-08-09T14:07:28)
    0000   0x9c 0x07 0x4e 0x09 0x0d                   ..N..
    body (0)

#### RECORD 46 CalBGForPH 2013-08-09T14:47:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-08-09T14:47:20)
    0000   0x94 0x2f 0x2e 0x09 0x0d                   ./...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 47 BolusWizard 2013-08-09T14:47:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 68}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2013-08-09T14:47:42)
    0000   0xaa 0x2f 0x0e 0x09 0x0d                   ./...
    body (15)
    hex
    0000   0x15 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x44 0x00 0x00 0x34 0x00 0x44 0x78         D..4.Dx
    decimal
             21   80    0  120   60  100    0    0
             68    0    0   52    0   68  120
    HOUR BITS: [0, 0, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 1.4, 'curve': 192},
 {'age': 174, 'amount': 1.0, 'curve': 192},
 {'age': 18, 'amount': 1.7, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0x2c 0xc0 0x28 0xae 0xc0    \.8,.(..
    0008   0x44 0x12 0xd0                             D..
    decimal
             92   11   56   44  192   40  174  192
             68   18  208
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-08-09T14:47:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x34 0x00    ..D.D.4.
    decimal
              1    0   68    0   68    0   52    0
    datetime (2013-08-09T14:47:43)
    0000   0xab 0x2f 0x4e 0x09 0x0d                   ./N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 CalBGForPH 2013-08-09T17:01:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-09T17:01:33)
    0000   0xa1 0x01 0x31 0x09 0x0d                   ..1..
    body (0)

#### RECORD 51 BolusWizard 2013-08-09T17:01:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-09T17:01:41)
    0000   0xa9 0x01 0x11 0x09 0x0d                   .....
    body (15)
    hex
    0000   0x10 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x40 0x00 0x00 0x10 0x00 0x40 0x78         @....@x
    decimal
             16   80    0  100   60  100    0    0
             64    0    0   16    0   64  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 138, 'amount': 1.7, 'curve': 192},
 {'age': 178, 'amount': 1.4, 'curve': 192},
 {'age': 52, 'amount': 1.0, 'curve': 208},
 {'age': 152, 'amount': 1.7, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x44 0x8a 0xc0 0x38 0xb2 0xc0    \.D..8..
    0008   0x28 0x34 0xd0 0x44 0x98 0xd0              (4.D..
    decimal
             92   14   68  138  192   56  178  192
             40   52  208   68  152  208
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-08-09T17:01:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x10 0x00    ..@.@...
    decimal
              1    0   64    0   64    0   16    0
    datetime (2013-08-09T17:01:41)
    0000   0xa9 0x01 0x51 0x09 0x0d                   ..Q..
    body (0)

#### RECORD 54 CalBGForPH 2013-08-09T17:28:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 235}
```
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2013-08-09T17:28:45)
    0000   0xad 0x1c 0x31 0x09 0x0d                   ..1..
    body (0)

#### RECORD 55 BolusWizard 2013-08-09T17:28:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 235,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 7.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xeb                                  [.
    decimal
             91  235
    datetime (2013-08-09T17:28:48)
    0000   0xb0 0x1c 0x11 0x69 0x0d                   ...i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x4c 0x00    .P.d<dL.
    0008   0x00 0x00 0x00 0x40 0x00 0x0c 0x78         ...@..x
    decimal
              0   80    0  100   60  100   76    0
              0    0    0   64    0   12  120
    DAY BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 1.6, 'curve': 192},
 {'age': 165, 'amount': 1.7, 'curve': 192},
 {'age': 205, 'amount': 1.4, 'curve': 192},
 {'age': 79, 'amount': 1.0, 'curve': 208},
 {'age': 179, 'amount': 1.7, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x40 0x23 0xc0 0x44 0xa5 0xc0    \.@#.D..
    0008   0x38 0xcd 0xc0 0x28 0x4f 0xd0 0x44 0xb3    8..(O.D.
    0010   0xd0                                       .
    decimal
             92   17   64   35  192   68  165  192
             56  205  192   40   79  208   68  179
            208
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2013-08-09T17:28:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x0c 0x00 0x0c 0x00 0x40 0x00    ......@.
    decimal
              1    0   12    0   12    0   64    0
    datetime (2013-08-09T17:28:48)
    0000   0xb0 0x1c 0x51 0x69 0x0d                   ..Qi.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 58 CalBGForPH 2013-08-09T18:54:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-09T18:54:38)
    0000   0xa6 0x36 0x32 0x09 0x0d                   .62..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 59 BolusWizard 2013-08-09T18:55:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.4,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-09T18:55:02)
    0000   0x82 0x37 0x12 0x09 0x0d                   .7...
    body (15)
    hex
    0000   0x12 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x48 0x00 0x00 0x18 0x00 0x48 0x78         H....Hx
    decimal
             18   80    0  100   60  100    0    0
             72    0    0   24    0   72  120
    HOUR BITS: [0, 0, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 0.3, 'curve': 192},
 {'age': 122, 'amount': 1.6, 'curve': 192},
 {'age': 252, 'amount': 1.7, 'curve': 192},
 {'age': 36, 'amount': 1.4, 'curve': 208},
 {'age': 166, 'amount': 1.0, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x0c 0x5c 0xc0 0x40 0x7a 0xc0    \..\.@z.
    0008   0x44 0xfc 0xc0 0x38 0x24 0xd0 0x28 0xa6    D..8$.(.
    0010   0xd0                                       .
    decimal
             92   17   12   92  192   64  122  192
             68  252  192   56   36  208   40  166
            208
    datetime (unknown)

    body (0)

#### RECORD 61 LowReservoir 2013-08-09T18:55:36 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-09T18:55:36)
    0000   0xa4 0x37 0x12 0x09 0x0d                   .7...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 62 Bolus 2013-08-09T18:55:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x18 0x00    ..H.H...
    decimal
              1    0   72    0   72    0   24    0
    datetime (2013-08-09T18:55:02)
    0000   0x82 0x37 0x52 0x09 0x0d                   .7R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 CalBGForPH 2013-08-09T21:23:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-08-09T21:23:34)
    0000   0xa2 0x17 0x35 0x09 0x0d                   ..5..
    body (0)

#### RECORD 64 BolusWizard 2013-08-09T21:23:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-08-09T21:23:42)
    0000   0xaa 0x17 0x15 0x09 0x0d                   .....
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x38 0x00 0x00 0x0c 0x00 0x38 0x78         8....8x
    decimal
             14   80    0  100   60  100    0    0
             56    0    0   12    0   56  120

`end analysis/sarak/raw//ReadHistoryData-page-12.data: 65 records`
