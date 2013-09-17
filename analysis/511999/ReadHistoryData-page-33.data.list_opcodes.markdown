## START logs/ReadHistoryData-page-33.data
#### STOPPING DOUBLE NULLS @ 1011, found 11 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa4 0xc6                                  ..
##### DEBUG DECIMAL
            164  198
#### RECORD 0 BolusWizard 2013-07-05T18:51:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 120}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-05T18:51:54)
    0000   0x76 0xf3 0x12 0x65 0x0d                   v..e.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x78 0x00 0x00 0x3c 0x00 0x78 0x78         x..<.xx
    decimal
             30   80    0  100   60  100   48    0
            120    0    0   60    0  120  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 1.1, 'curve': 192},
 {'age': 97, 'amount': 1.6, 'curve': 192},
 {'age': 107, 'amount': 0.4, 'curve': 192},
 {'age': 217, 'amount': 1.2, 'curve': 192},
 {'age': 237, 'amount': 0.7, 'curve': 192},
 {'age': 21, 'amount': 0.5, 'curve': 208},
 {'age': 41, 'amount': 3.5, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x2c 0x43 0xc0 0x40 0x61 0xc0    \.,C.@a.
    0008   0x10 0x6b 0xc0 0x30 0xd9 0xc0 0x1c 0xed    .k.0....
    0010   0xc0 0x14 0x15 0xd0 0x8c 0x29 0xd0         .....).
    decimal
             92   23   44   67  192   64   97  192
             16  107  192   48  217  192   28  237
            192   20   21  208  140   41  208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-07-05T18:51:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x3c 0x00    ..x.x.<.
    decimal
              1    0  120    0  120    0   60    0
    datetime (2013-07-05T18:51:54)
    0000   0x76 0xf3 0x52 0x65 0x0d                   v.Re.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2013-07-05T19:07:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-07-05T19:07:25)
    0000   0x59 0xc7 0x33 0x05 0x0d                   Y.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BolusWizard 2013-07-05T19:07:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 16.0,
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
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-07-05T19:07:38)
    0000   0x66 0xc7 0x13 0x65 0x0d                   f..e.
    body (15)
    hex
    0000   0x10 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x40 0x00 0x00 0xa0 0x00 0x40 0x78         @....@x
    decimal
             16   80    0  100   60  100    0    0
             64    0    0  160    0   64  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 23, 'amount': 3.0, 'curve': 192},
 {'age': 83, 'amount': 1.1, 'curve': 192},
 {'age': 113, 'amount': 1.6, 'curve': 192},
 {'age': 123, 'amount': 0.4, 'curve': 192},
 {'age': 233, 'amount': 1.2, 'curve': 192},
 {'age': 253, 'amount': 0.7, 'curve': 192},
 {'age': 37, 'amount': 0.5, 'curve': 208},
 {'age': 57, 'amount': 3.5, 'curve': 208}]
```
    op hex (26)
    0000   0x5c 0x1a 0x78 0x17 0xc0 0x2c 0x53 0xc0    \.x..,S.
    0008   0x40 0x71 0xc0 0x10 0x7b 0xc0 0x30 0xe9    @q..{.0.
    0010   0xc0 0x1c 0xfd 0xc0 0x14 0x25 0xd0 0x8c    .....%..
    0018   0x39 0xd0                                  9.
    decimal
             92   26  120   23  192   44   83  192
             64  113  192   16  123  192   48  233
            192   28  253  192   20   37  208  140
             57  208
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-07-05T19:07:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xa0 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  160    0
    datetime (2013-07-05T19:07:38)
    0000   0x66 0xc7 0x53 0x65 0x0d                   f.Se.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 CalBGForPH 2013-07-05T23:20:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-07-05T23:20:38)
    0000   0x66 0xd4 0x37 0x05 0x0d                   f.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 BolusWizard 2013-07-05T23:20:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-05T23:20:41)
    0000   0x69 0xd4 0x17 0x05 0x0d                   i....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x00 0x00 0x00 0x00 0x00 0x30 0x78         .....0x
    decimal
              0   80    0  100   60  100   48    0
              0    0    0    0    0   48  120
    HOUR BITS: [1, 1, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 0, 'amount': 1.0, 'curve': 208},
 {'age': 20, 'amount': 3.0, 'curve': 208},
 {'age': 80, 'amount': 1.1, 'curve': 208},
 {'age': 110, 'amount': 1.6, 'curve': 208},
 {'age': 120, 'amount': 0.4, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0x00 0xd0 0x78 0x14 0xd0    \.(..x..
    0008   0x2c 0x50 0xd0 0x40 0x6e 0xd0 0x10 0x78    ,P.@n..x
    0010   0xd0                                       .
    decimal
             92   17   40    0  208  120   20  208
             44   80  208   64  110  208   16  120
            208
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-07-05T23:20:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-07-05T23:20:41)
    0000   0x69 0xd4 0x57 0x05 0x0d                   i.W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 BasalProfileStart 2013-07-06T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-06T00:00:00)
    0000   0x40 0xc0 0x00 0x06 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 0]
#### RECORD 12 ResultTotals (2000, 6, 0, 0, 13, 37) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x1c                   .....
    decimal
              7    0    0    5   28
    datetime ((2000, 6, 0, 0, 13, 37))
    0000   0x65 0x8d 0x00 0x00 0x00                   e....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 13 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x65 0x8d 0x05 0x00 0xfa 0x00 0x00    ne......
    0008   0x09 0x00 0x00 0x05 0x1c 0x02 0xe4 0x39    .......9
    0010   0x02 0x38 0x2b 0x00 0x49 0x00 0xb4 0x00    .8+.I...
    0018   0xf8 0x00 0x8c 0x00 0x00 0x03 0x05 0x01    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6c 0x64 0x00 0x00 0x00         ..ld...
    decimal
            110  101  141    5    0  250    0    0
              9    0    0    5   28    2  228   57
              2   56   43    0   73    0  180    0
            248    0  140    0    0    3    5    1
              0    4    0    0    0    0    0    0
              0    0  108  100    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 14 CalBGForPH 2013-07-06T03:17:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-07-06T03:17:18)
    0000   0x52 0xd1 0x23 0x06 0x0d                   R.#..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 15 BolusWizard 2013-07-06T03:17:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 110,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 1.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-06T03:17:22)
    0000   0x56 0xd1 0x03 0x66 0x0d                   V..f.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x6e 0x2c 0x00    .P.x<n,.
    0008   0x00 0x00 0x00 0x00 0x00 0x2c 0x82         .....,.
    decimal
              0   80    0  120   60  110   44    0
              0    0    0    0    0   44  130
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 243, 'amount': 1.2, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0xf3 0xc0                   \.0..
    decimal
             92    5   48  243  192
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2013-07-06T03:17:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x00 0x00    ..,.,...
    decimal
              1    0   44    0   44    0    0    0
    datetime (2013-07-06T03:17:23)
    0000   0x57 0xd1 0x43 0x66 0x0d                   W.Cf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 BasalProfileStart 2013-07-06T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-06T04:00:00)
    0000   0x40 0xc0 0x04 0x06 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 19 BasalProfileStart 2013-07-06T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-06T08:00:00)
    0000   0x40 0xc0 0x08 0x06 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 20 CalBGForPH 2013-07-06T09:26:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-07-06T09:26:35)
    0000   0x63 0xda 0x29 0x06 0x0d                   c.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 21 BolusWizard 2013-07-06T09:26:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 103,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x67                                  [g
    decimal
             91  103
    datetime (2013-07-06T09:26:44)
    0000   0x6c 0xda 0x09 0x66 0x0d                   l..f.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x00 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0    0    0   64  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 116, 'amount': 1.1, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0x74 0xd0                   \.,t.
    decimal
             92    5   44  116  208
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-07-06T09:26:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    0   64    0   64    0    0    0
    datetime (2013-07-06T09:26:44)
    0000   0x6c 0xda 0x49 0x66 0x0d                   l.If.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 24 CalBGForPH 2013-07-06T11:29:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-07-06T11:29:23)
    0000   0x57 0xdd 0x2b 0x06 0x0d                   W.+..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 25 BolusWizard 2013-07-06T11:29:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 105,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-07-06T11:29:32)
    0000   0x60 0xdd 0x0b 0x66 0x0d                   `..f.
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x2c 0x00 0x00 0x10 0x00 0x2c 0x78         ,....,x
    decimal
             14   80    0  120   60  100    0    0
             44    0    0   16    0   44  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 1.6, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x40 0x7d 0xc0                   \.@}.
    decimal
             92    5   64  125  192
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-07-06T11:29:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x10 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   16    0
    datetime (2013-07-06T11:29:33)
    0000   0x61 0xdd 0x4b 0x66 0x0d                   a.Kf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 BasalProfileStart 2013-07-06T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-06T12:00:00)
    0000   0x40 0xc0 0x0c 0x06 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 29 CalBGForPH 2013-07-06T12:17:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-07-06T12:17:48)
    0000   0x70 0xd1 0x2c 0x06 0x0d                   p.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 BolusWizard 2013-07-06T12:18:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 123,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2013-07-06T12:18:27)
    0000   0x5b 0xd2 0x0c 0x66 0x0d                   [..f.
    body (15)
    hex
    0000   0x12 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x3c 0x00 0x00 0x28 0x00 0x3c 0x78         <..(.<x
    decimal
             18   80    0  120   60  100    0    0
             60    0    0   40    0   60  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 1.1, 'curve': 192},
 {'age': 174, 'amount': 1.6, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x36 0xc0 0x40 0xae 0xc0    \.,6.@..
    decimal
             92    8   44   54  192   64  174  192
    datetime (unknown)

    body (0)

#### RECORD 32 CalBGForPH 2013-07-06T12:29:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 126}
```
    op hex (2)
    0000   0x0a 0x7e                                  .~
    decimal
             10  126
    datetime (2013-07-06T12:29:05)
    0000   0x45 0xdd 0x2c 0x06 0x0d                   E.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 BolusWizard 2013-07-06T12:29:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 126,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2013-07-06T12:29:11)
    0000   0x4b 0xdd 0x0c 0x66 0x0d                   K..f.
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x04 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x20 0x00 0x28 0x78         (.. .(x
    decimal
             12   80    0  120   60  100    4    0
             40    0    0   32    0   40  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 1.1, 'curve': 192},
 {'age': 185, 'amount': 1.6, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x41 0xc0 0x40 0xb9 0xc0    \.,A.@..
    decimal
             92    8   44   65  192   64  185  192
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-07-06T12:29:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x20 0x00    ..(.(. .
    decimal
              1    0   40    0   40    0   32    0
    datetime (2013-07-06T12:29:11)
    0000   0x4b 0xdd 0x4c 0x66 0x0d                   K.Lf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 CalBGForPH 2013-07-06T14:00:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-07-06T14:00:41)
    0000   0x69 0xc0 0x2e 0x06 0x0d                   i....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 BolusWizard 2013-07-06T14:00:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-06T14:00:45)
    0000   0x6d 0xc0 0x0e 0x66 0x0d                   m..f.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x30 0x00    .P.x<d0.
    0008   0x00 0x00 0x00 0x18 0x00 0x18 0x78         ......x
    decimal
              0   80    0  120   60  100   48    0
              0    0    0   24    0   24  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 96, 'amount': 1.0, 'curve': 192},
 {'age': 156, 'amount': 1.1, 'curve': 192},
 {'age': 20, 'amount': 1.6, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x60 0xc0 0x2c 0x9c 0xc0    \.(`.,..
    0008   0x40 0x14 0xd0                             @..
    decimal
             92   11   40   96  192   44  156  192
             64   20  208
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-07-06T14:00:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x18 0x00    ........
    decimal
              1    0   24    0   24    0   24    0
    datetime (2013-07-06T14:00:45)
    0000   0x6d 0xc0 0x4e 0x66 0x0d                   m.Nf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 CalBGForPH 2013-07-06T14:59:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-07-06T14:59:20)
    0000   0x54 0xfb 0x2e 0x06 0x0d                   T....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 BolusWizard 2013-07-06T14:59:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-07-06T14:59:27)
    0000   0x5b 0xfb 0x0e 0x66 0x0d                   [..f.
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x2c 0x00 0x00 0x14 0x00 0x2c 0x78         ,....,x
    decimal
             14   80    0  120   60  100    0    0
             44    0    0   20    0   44  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 0.6, 'curve': 192},
 {'age': 155, 'amount': 1.0, 'curve': 192},
 {'age': 215, 'amount': 1.1, 'curve': 192},
 {'age': 79, 'amount': 1.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x41 0xc0 0x28 0x9b 0xc0    \..A.(..
    0008   0x2c 0xd7 0xc0 0x40 0x4f 0xd0              ,..@O.
    decimal
             92   14   24   65  192   40  155  192
             44  215  192   64   79  208
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-07-06T14:59:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x14 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   20    0
    datetime (2013-07-06T14:59:27)
    0000   0x5b 0xfb 0x4e 0x66 0x0d                   [.Nf.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 CalBGForPH 2013-07-06T15:29:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-07-06T15:29:45)
    0000   0x6d 0xdd 0x2f 0x06 0x0d                   m./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 BolusWizard 2013-07-06T15:29:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 5,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 16}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-07-06T15:29:54)
    0000   0x76 0xdd 0x0f 0x66 0x0d                   v..f.
    body (15)
    hex
    0000   0x05 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x10 0x00 0x00 0x34 0x00 0x10 0x78         ...4..x
    decimal
              5   80    0  120   60  100    0    0
             16    0    0   52    0   16  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 1.1, 'curve': 192},
 {'age': 95, 'amount': 0.6, 'curve': 192},
 {'age': 185, 'amount': 1.0, 'curve': 192},
 {'age': 245, 'amount': 1.1, 'curve': 192},
 {'age': 109, 'amount': 1.6, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x2c 0x23 0xc0 0x18 0x5f 0xc0    \.,#.._.
    0008   0x28 0xb9 0xc0 0x2c 0xf5 0xc0 0x40 0x6d    (..,..@m
    0010   0xd0                                       .
    decimal
             92   17   44   35  192   24   95  192
             40  185  192   44  245  192   64  109
            208
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-07-06T15:29:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x34 0x00    ......4.
    decimal
              1    0   16    0   16    0   52    0
    datetime (2013-07-06T15:29:54)
    0000   0x76 0xdd 0x4f 0x66 0x0d                   v.Of.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 CalBGForPH 2013-07-06T16:19:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 263}
```
    op hex (2)
    0000   0x0a 0x07                                  ..
    decimal
             10    7
    datetime (2013-07-06T16:19:33)
    0000   0x61 0xd3 0x30 0x06 0x8d                   a.0..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 49 BolusWizard 2013-07-06T16:19:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 263,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 9.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x07                                  [.
    decimal
             91    7
    datetime (2013-07-06T16:19:39)
    0000   0x67 0xd3 0x10 0x66 0x0d                   g..f.
    body (15)
    hex
    0000   0x0e 0x51 0x00 0x78 0x3c 0x64 0x5c 0x00    .Q.x<d\.
    0008   0x2c 0x00 0x00 0x28 0x00 0x60 0x78         ,..(.`x
    decimal
             14   81    0  120   60  100   92    0
             44    0    0   40    0   96  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 0.4, 'curve': 192},
 {'age': 85, 'amount': 1.1, 'curve': 192},
 {'age': 145, 'amount': 0.6, 'curve': 192},
 {'age': 235, 'amount': 1.0, 'curve': 192},
 {'age': 39, 'amount': 1.1, 'curve': 208},
 {'age': 159, 'amount': 1.6, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x10 0x37 0xc0 0x2c 0x55 0xc0    \..7.,U.
    0008   0x18 0x91 0xc0 0x28 0xeb 0xc0 0x2c 0x27    ...(..,'
    0010   0xd0 0x40 0x9f 0xd0                        .@..
    decimal
             92   20   16   55  192   44   85  192
             24  145  192   40  235  192   44   39
            208   64  159  208
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-07-06T16:19:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0x28 0x00    ..`.`.(.
    decimal
              1    0   96    0   96    0   40    0
    datetime (2013-07-06T16:19:39)
    0000   0x67 0xd3 0x50 0x66 0x0d                   g.Pf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 CalBGForPH 2013-07-06T16:34:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 294}
```
    op hex (2)
    0000   0x0a 0x26                                  .&
    decimal
             10   38
    datetime (2013-07-06T16:34:45)
    0000   0x6d 0xe2 0x30 0x06 0x8d                   m.0..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 53 BolusWizard 2013-07-06T16:34:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 294,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 12.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 11.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x26                                  [&
    decimal
             91   38
    datetime (2013-07-06T16:34:49)
    0000   0x71 0xe2 0x10 0x66 0x0d                   q..f.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x74 0x00    .Q.x<dt.
    0008   0x00 0x00 0x00 0x7c 0x00 0x00 0x78         ...|..x
    decimal
              0   81    0  120   60  100  116    0
              0    0    0  124    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 2.4, 'curve': 192},
 {'age': 70, 'amount': 0.4, 'curve': 192},
 {'age': 100, 'amount': 1.1, 'curve': 192},
 {'age': 160, 'amount': 0.6, 'curve': 192},
 {'age': 250, 'amount': 1.0, 'curve': 192},
 {'age': 54, 'amount': 1.1, 'curve': 208},
 {'age': 174, 'amount': 1.6, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x60 0x14 0xc0 0x10 0x46 0xc0    \.`...F.
    0008   0x2c 0x64 0xc0 0x18 0xa0 0xc0 0x28 0xfa    ,d....(.
    0010   0xc0 0x2c 0x36 0xd0 0x40 0xae 0xd0         .,6.@..
    decimal
             92   23   96   20  192   16   70  192
             44  100  192   24  160  192   40  250
            192   44   54  208   64  174  208
    datetime (unknown)

    body (0)

#### RECORD 55 CalBGForPH 2013-07-06T16:57:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 351}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-07-06T16:57:16)
    0000   0x50 0xf9 0x30 0x06 0x8d                   P.0..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 56 BolusWizard 2013-07-06T16:57:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 351,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 15.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2013-07-06T16:57:20)
    0000   0x54 0xf9 0x10 0x66 0x0d                   T..f.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x98 0x00    .Q.x<d..
    0008   0x00 0x00 0x00 0x64 0x00 0x34 0x78         ...d.4x
    decimal
              0   81    0  120   60  100  152    0
              0    0    0  100    0   52  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 43, 'amount': 2.4, 'curve': 192},
 {'age': 93, 'amount': 0.4, 'curve': 192},
 {'age': 123, 'amount': 1.1, 'curve': 192},
 {'age': 183, 'amount': 0.6, 'curve': 192},
 {'age': 17, 'amount': 1.0, 'curve': 208},
 {'age': 77, 'amount': 1.1, 'curve': 208},
 {'age': 197, 'amount': 1.6, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x60 0x2b 0xc0 0x10 0x5d 0xc0    \.`+..].
    0008   0x2c 0x7b 0xc0 0x18 0xb7 0xc0 0x28 0x11    ,{....(.
    0010   0xd0 0x2c 0x4d 0xd0 0x40 0xc5 0xd0         .,M.@..
    decimal
             92   23   96   43  192   16   93  192
             44  123  192   24  183  192   40   17
            208   44   77  208   64  197  208
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-07-06T16:57:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x64 0x00    ..4.4.d.
    decimal
              1    0   52    0   52    0  100    0
    datetime (2013-07-06T16:57:20)
    0000   0x54 0xf9 0x50 0x66 0x0d                   T.Pf.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 CalBGForPH 2013-07-06T19:32:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-07-06T19:32:07)
    0000   0x47 0xe0 0x33 0x06 0x0d                   G.3..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 60 BolusWizard 2013-07-06T19:32:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 31,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-06T19:32:22)
    0000   0x56 0xe0 0x13 0x66 0x0d                   V..f.
    body (15)
    hex
    0000   0x1f 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x7c 0x00 0x00 0x08 0x00 0xa4 0x78         |.....x
    decimal
             31   80    0  100   60  100   48    0
            124    0    0    8    0  164  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 158, 'amount': 1.3, 'curve': 192},
 {'age': 198, 'amount': 2.4, 'curve': 192},
 {'age': 248, 'amount': 0.4, 'curve': 192},
 {'age': 22, 'amount': 1.1, 'curve': 208},
 {'age': 82, 'amount': 0.6, 'curve': 208},
 {'age': 172, 'amount': 1.0, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x34 0x9e 0xc0 0x60 0xc6 0xc0    \.4..`..
    0008   0x10 0xf8 0xc0 0x2c 0x16 0xd0 0x18 0x52    ...,...R
    0010   0xd0 0x28 0xac 0xd0                        .(..
    decimal
             92   20   52  158  192   96  198  192
             16  248  192   44   22  208   24   82
            208   40  172  208
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-07-06T19:32:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x08 0x00    ........
    decimal
              1    0  164    0  164    0    8    0
    datetime (2013-07-06T19:32:22)
    0000   0x56 0xe0 0x53 0x66 0x0d                   V.Sf.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 CalBGForPH 2013-07-06T21:41:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-07-06T21:41:38)
    0000   0x66 0xe9 0x35 0x06 0x0d                   f.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 64 BolusWizard 2013-07-06T21:41:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-07-06T21:41:47)
    0000   0x6f 0xe9 0x15 0x66 0x0d                   o..f.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x3c 0x00 0x00 0x20 0x00 0x4c 0x78         <.. .Lx
    decimal
             15   80    0  100   60  100   48    0
             60    0    0   32    0   76  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 127, 'amount': 1.7, 'curve': 192},
 {'age': 137, 'amount': 2.4, 'curve': 192},
 {'age': 31, 'amount': 1.3, 'curve': 208},
 {'age': 71, 'amount': 2.4, 'curve': 208},
 {'age': 121, 'amount': 0.4, 'curve': 208},
 {'age': 151, 'amount': 1.1, 'curve': 208},
 {'age': 211, 'amount': 0.6, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x44 0x7f 0xc0 0x60 0x89 0xc0    \.D..`..
    0008   0x34 0x1f 0xd0 0x60 0x47 0xd0 0x10 0x79    4..`G..y
    0010   0xd0 0x2c 0x97 0xd0 0x18 0xd3 0xd0         .,.....
    decimal
             92   23   68  127  192   96  137  192
             52   31  208   96   71  208   16  121
            208   44  151  208   24  211  208
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-07-06T21:41:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x20 0x00    ..L.L. .
    decimal
              1    0   76    0   76    0   32    0
    datetime (2013-07-06T21:41:47)
    0000   0x6f 0xe9 0x55 0x66 0x0d                   o.Uf.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 BasalProfileStart 2013-07-07T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-07T00:00:00)
    0000   0x40 0xc0 0x00 0x07 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x1c 0x00                             ...
    decimal
              0   28    0
    HOUR BITS: [1, 1, 0]
#### RECORD 68 ResultTotals (2000, 6, 0, 0, 13, 38) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x6c                   ....l
    decimal
              7    0    0    5  108
    datetime ((2000, 6, 0, 0, 13, 38))
    0000   0x66 0x8d 0x00 0x00 0x00                   f....
    body (0)
    HOUR BITS: [1, 0, 0]
`end logs/ReadHistoryData-page-33.data: 69 records`
