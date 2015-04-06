## START analysis/736868/logs/ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x9e 0xad                                  ..
##### DEBUG DECIMAL
            158  173
#### RECORD 0 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 0.55, 'curve': 4},
 {'age': 65, 'amount': 1.5, 'curve': 4},
 {'age': 145, 'amount': 1.5, 'curve': 4},
 {'age': 155, 'amount': 1.5, 'curve': 4},
 {'age': 39, 'amount': 1.0, 'curve': 20},
 {'age': 69, 'amount': 4.0, 'curve': 20},
 {'age': 79, 'amount': 4.0, 'curve': 20},
 {'age': 169, 'amount': 0.05, 'curve': 20},
 {'age': 179, 'amount': 0.95, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x16 0x2d 0x04 0x3c 0x41 0x04    \..-.<A.
    0008   0x3c 0x91 0x04 0x3c 0x9b 0x04 0x28 0x27    <..<..('
    0010   0x14 0xa0 0x45 0x14 0xa0 0x4f 0x14 0x02    ..E..O..
    0018   0xa9 0x14 0x26 0xb3 0x14                   ..&..
    decimal
             92   29   22   45    4   60   65    4
             60  145    4   60  155    4   40   39
             20  160   69   20  160   79   20    2
            169   20   38  179   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-03-06T19:09:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3,
 'duration': 60,
 'programmed': 4.3,
 'type': 'square',
 'unabsorbed': 2.6}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0x68 0x02    ......h.
    decimal
              1    0  172    0  172    0  104    2
    datetime (2015-03-06T19:09:04)
    0000   0x04 0xc9 0xb3 0x66 0x0f                   ...f.
    body (0)

#### RECORD 2 Bolus 2015-03-06T19:04:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6,
 'duration': 0,
 'programmed': 0.6,
 'type': 'normal',
 'unabsorbed': 2.6}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x68 0x00    ......h.
    decimal
              1    1   24    1   24    0  104    0
    datetime (2015-03-06T19:04:22)
    0000   0x16 0xc4 0x93 0x66 0x0f                   ...f.
    body (0)

#### RECORD 3 Ian0B 2015-03-06T19:37:41 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0x12                             .e.
    decimal
             11  101   18
    datetime (2015-03-06T19:37:41)
    0000   0x29 0xe5 0x33 0xa6 0x8f                   ).3..
    body (0)

#### RECORD 4 PumpSuspend 2015-03-06T20:20:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-06T20:20:39)
    0000   0x27 0xd4 0x14 0x06 0x0f                   '....
    body (0)

#### RECORD 5 BasalProfileStart 2015-03-06T21:00:05 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-06T21:00:05)
    0000   0x05 0xc0 0x15 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 6 PumpResume 2015-03-06T21:00:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-06T21:00:05)
    0000   0x05 0xc0 0x15 0x06 0x0f                   .....
    body (0)

#### RECORD 7 Ian0B 2015-03-06T21:40:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-06T21:40:00)
    0000   0x00 0xe8 0x35 0xa6 0x0f                   ..5..
    body (0)

#### RECORD 8 BasalProfileStart 2015-03-06T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-06T22:00:00)
    0000   0x00 0xc0 0x16 0x06 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 9 Ian0B 2015-03-06T22:17:41 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-06T22:17:41)
    0000   0x29 0xd1 0x36 0xa6 0x0f                   ).6..
    body (0)

#### RECORD 10 Ian0B 2015-03-06T22:40:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-06T22:40:00)
    0000   0x00 0xe8 0x36 0xa6 0x0f                   ..6..
    body (0)

#### RECORD 11 Ian0B 2015-03-06T23:10:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-06T23:10:00)
    0000   0x00 0xca 0x37 0xa6 0x0f                   ..7..
    body (0)

#### RECORD 12 CalBGForPH 2015-03-06T23:11:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 210}
```
    op hex (2)
    0000   0x0a 0xd2                                  ..
    decimal
             10  210
    datetime (2015-03-06T23:11:36)
    0000   0x24 0xcb 0x37 0x66 0x0f                   $.7f.
    body (0)

#### RECORD 13 Ian3F 2015-03-06T23:11:36 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2015-03-06T23:11:36)
    0000   0x24 0xcb 0x57 0x66 0x0f                   $.Wf.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 14 BolusWizard 2015-03-06T23:11:44 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 210,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 12.0,
 'correction_estimate': 2.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0xd2                                  [.
    decimal
             91  210
    datetime (2015-03-06T23:11:44)
    0000   0x2c 0xcb 0x17 0x06 0x0f                   ,....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x58 0x00    .P.d(ZX.
    0008   0x00 0x00 0x00 0x10 0x00 0x48 0x78         .....Hx
    decimal
              0   80    0  100   40   90   88    0
              0    0    0   16    0   72  120

#### RECORD 15 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 192, 'amount': 0.7, 'curve': 4},
 {'age': 202, 'amount': 0.75, 'curve': 4},
 {'age': 212, 'amount': 0.7, 'curve': 4},
 {'age': 222, 'amount': 0.7, 'curve': 4},
 {'age': 232, 'amount': 0.75, 'curve': 4},
 {'age': 242, 'amount': 0.85, 'curve': 4},
 {'age': 252, 'amount': 0.45, 'curve': 5},
 {'age': 36, 'amount': 0.55, 'curve': 20},
 {'age': 56, 'amount': 1.5, 'curve': 20},
 {'age': 136, 'amount': 1.5, 'curve': 20},
 {'age': 146, 'amount': 1.5, 'curve': 20}]
```
    op hex (35)
    0000   0x5c 0x23 0x1c 0xc0 0x04 0x1e 0xca 0x04    \#......
    0008   0x1c 0xd4 0x04 0x1c 0xde 0x04 0x1e 0xe8    ........
    0010   0x04 0x22 0xf2 0x04 0x12 0xfc 0x05 0x16    ."......
    0018   0x24 0x14 0x3c 0x38 0x14 0x3c 0x88 0x14    $.<8.<..
    0020   0x3c 0x92 0x14                             <..
    decimal
             92   35   28  192    4   30  202    4
             28  212    4   28  222    4   30  232
              4   34  242    4   18  252    5   22
             36   20   60   56   20   60  136   20
             60  146   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2015-03-06T23:11:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x10 0x00    ........
    decimal
              1    0    0    0    0    0   16    0
    datetime (2015-03-06T23:11:44)
    0000   0x2c 0xcb 0xb7 0x06 0x0f                   ,....
    body (0)

#### RECORD 17 Bolus 2015-03-06T23:11:44 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 0,
 'programmed': 1.8,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x10 0x00    ..H.H...
    decimal
              1    0   72    0   72    0   16    0
    datetime (2015-03-06T23:11:44)
    0000   0x2c 0xcb 0x97 0x06 0x0f                   ,....
    body (0)

#### RECORD 18 Ian0B 2015-03-06T23:26:24 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xd2                             .e.
    decimal
             11  101  210
    datetime (2015-03-06T23:26:24)
    0000   0x18 0xda 0x37 0xa6 0x0f                   ..7..
    body (0)

#### RECORD 19 BasalProfileStart 2015-03-07T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-07T00:00:00)
    0000   0x00 0xc0 0x00 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 20 MResultTotals 2015-03-07T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0x82                   .....
    decimal
              7    0    0    9  130
    datetime (2015-03-07T00:00:00)
    0000   0x26 0x8f                                  &.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 21 Sara6E 2015-03-07T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-07T00:00:00)
    0000   0x26 0x8f                                  &.
    body (49)
    hex
    0000   0x05 0x00 0x99 0x60 0xd2 0x02 0x00 0x00    ...`....
    0008   0x09 0x82 0x03 0x14 0x20 0x06 0x6e 0x44    .... .nD
    0010   0x00 0x8f 0x02 0xf0 0x00 0x48 0x00 0x00    .....H..
    0018   0x03 0x36 0x02 0x01 0x00 0x09 0x00 0xce    .6......
    0020   0x40 0x24 0x00 0x15 0x39 0x02 0x00 0x00    @$..9...
    0028   0x00 0x00 0x0b 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  153   96  210    2    0    0
              9  130    3   20   32    6  110   68
              0  143    2  240    0   72    0    0
              3   54    2    1    0    9    0  206
             64   36    0   21   57    2    0    0
              0    0   11    1    0    0    0    0
              0

#### RECORD 22 Ian0B 2015-03-07T00:57:41 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xf4                             .e.
    decimal
             11  101  244
    datetime (2015-03-07T00:57:41)
    0000   0x29 0xf9 0x20 0xa7 0x0f                   ). ..
    body (0)

#### RECORD 23 Ian0B 2015-03-07T02:27:22 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0x25                             .e%
    decimal
             11  101   37
    datetime (2015-03-07T02:27:22)
    0000   0x16 0xdb 0x22 0xa7 0x8f                   .."..
    body (0)

#### RECORD 24 Bolus 2015-03-07T03:50:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    0    0
    datetime (2015-03-07T03:50:25)
    0000   0x19 0xf2 0x43 0x67 0x0f                   ..Cg.
    body (0)

#### RECORD 25 Ian0B 2015-03-07T03:57:13 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0x2f                             .e/
    decimal
             11  101   47
    datetime (2015-03-07T03:57:13)
    0000   0x0d 0xf9 0x23 0xa7 0x8f                   ..#..
    body (0)

#### RECORD 26 BasalProfileStart 2015-03-07T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-07T04:00:00)
    0000   0x00 0xc0 0x04 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 27 Ian0B 2015-03-07T06:57:41 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-03-07T06:57:41)
    0000   0x29 0xf9 0x26 0xa7 0x0f                   ).&..
    body (0)

#### RECORD 28 BasalProfileStart 2015-03-07T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-07T07:00:00)
    0000   0x00 0xc0 0x07 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 29 CalBGForPH 2015-03-07T08:53:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2015-03-07T08:53:44)
    0000   0x2c 0xf5 0x28 0x67 0x0f                   ,.(g.
    body (0)

#### RECORD 30 Ian3F 2015-03-07T08:53:44 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2015-03-07T08:53:44)
    0000   0x2c 0xf5 0x48 0x67 0x0f                   ,.Hg.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 31 BolusWizard 2015-03-07T08:53:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 130,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 12.0,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2015-03-07T08:53:55)
    0000   0x37 0xf5 0x08 0x07 0x0f                   7....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x08 0x00    .P.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x08 0x78         ......x
    decimal
              0   80    0  100   40   90    8    0
              0    0    0    0    0    8  120

#### RECORD 32 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 3.0, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x30 0x14                   \.x0.
    decimal
             92    5  120   48   20
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2015-03-07T08:53:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    decimal
              1    0    0    0    0    0    0    0
    datetime (2015-03-07T08:53:55)
    0000   0x37 0xf5 0xa8 0x07 0x0f                   7....
    body (0)

#### RECORD 34 Bolus 2015-03-07T08:53:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2,
 'duration': 0,
 'programmed': 0.2,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x08 0x00 0x08 0x00 0x00 0x00    ........
    decimal
              1    0    8    0    8    0    0    0
    datetime (2015-03-07T08:53:55)
    0000   0x37 0xf5 0x88 0x07 0x0f                   7....
    body (0)

#### RECORD 35 BolusWizard 2015-03-07T09:37:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 0.1,
 'carb_input': 65,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-07T09:37:37)
    0000   0x25 0xe5 0x09 0x67 0x0f                   %..g.
    body (15)
    hex
    0000   0x41 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    AP.d(Z..
    0008   0x04 0x00 0x00 0x00 0x01 0x04 0x78         ......x
    decimal
             65   80    0  100   40   90    0    1
              4    0    0    0    1    4  120

#### RECORD 36 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 0.2, 'curve': 4},
 {'age': 92, 'amount': 3.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x08 0x30 0x04 0x78 0x5c 0x14    \..0.x\.
    decimal
             92    8    8   48    4  120   92   20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2015-03-07T09:37:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 60,
 'programmed': 1.6,
 'type': 'square',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x00 0x00 0x08 0x02    ..@.....
    decimal
              1    0   64    0    0    0    8    2
    datetime (2015-03-07T09:37:37)
    0000   0x25 0xe5 0xa9 0x67 0x0f                   %..g.
    body (0)

#### RECORD 38 Bolus 2015-03-07T09:37:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.75,
 'duration': 0,
 'programmed': 4.9,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0xc4 0x00 0xbe 0x00 0x08 0x00    ........
    decimal
              1    0  196    0  190    0    8    0
    datetime (2015-03-07T09:37:37)
    0000   0x25 0xe5 0x89 0x67 0x0f                   %..g.
    body (0)

#### RECORD 39 NoDelivery 2015-03-07T09:40:51 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-07T09:40:51)
    0000   0x33 0xe8 0x49 0x47 0x0f                   3.IG.
    body (0)

#### RECORD 40 ClearAlarm 2015-03-07T09:40:57 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-07T09:40:57)
    0000   0x39 0xe8 0x09 0x07 0x0f                   9....
    body (0)

#### RECORD 41 BasalProfileStart 2015-03-07T09:41:07 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-07T09:41:07)
    0000   0x07 0xe9 0x09 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 42 Bolus 2015-03-07T09:41:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 4.9}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xc4 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  196    0
    datetime (2015-03-07T09:41:16)
    0000   0x10 0xe9 0x49 0x67 0x0f                   ..Ig.
    body (0)

#### RECORD 43 BasalProfileStart 2015-03-07T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-07T10:00:00)
    0000   0x00 0xc0 0x0a 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 44 BasalProfileStart 2015-03-07T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-07T12:00:00)
    0000   0x00 0xc0 0x0c 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 45 Ian0B 2015-03-07T12:41:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-07T12:41:07)
    0000   0x07 0xe9 0x2c 0xa7 0x0f                   ..,..
    body (0)

#### RECORD 46 Ian0B 2015-03-07T12:51:46 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-03-07T12:51:46)
    0000   0x2e 0xf3 0x2c 0xa7 0x0f                   ..,..
    body (0)

#### RECORD 47 BolusWizard 2015-03-07T12:52:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 60,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-07T12:52:12)
    0000   0x0c 0xf4 0x0c 0x67 0x0f                   ...g.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 48 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 193, 'amount': 4.2, 'curve': 4},
 {'age': 203, 'amount': 2.05, 'curve': 4},
 {'age': 243, 'amount': 0.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa8 0xc1 0x04 0x52 0xcb 0x04    \....R..
    0008   0x08 0xf3 0x04                             ...
    decimal
             92   11  168  193    4   82  203    4
              8  243    4
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2015-03-07T12:54:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 120,
 'programmed': 4.5,
 'type': 'square',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x20 0x04    ...... .
    decimal
              1    0  180    0  180    0   32    4
    datetime (2015-03-07T12:54:13)
    0000   0x0d 0xf6 0xac 0x67 0x0f                   ...g.
    body (0)

#### RECORD 50 Bolus 2015-03-07T12:52:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x20 0x00    ..x.x. .
    decimal
              1    0  120    0  120    0   32    0
    datetime (2015-03-07T12:52:12)
    0000   0x0c 0xf4 0x8c 0x67 0x0f                   ...g.
    body (0)

#### RECORD 51 Ian0B 2015-03-07T13:42:34 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-03-07T13:42:34)
    0000   0x22 0xea 0x2d 0xa7 0x0f                   ".-..
    body (0)

#### RECORD 52 Ian0B 2015-03-07T14:11:46 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x4b                             .fK
    decimal
             11  102   75
    datetime (2015-03-07T14:11:46)
    0000   0x2e 0xcb 0x2e 0xa7 0x0f                   .....
    body (0)

#### RECORD 53 BasalProfileStart 2015-03-07T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-07T15:00:00)
    0000   0x00 0xc0 0x0f 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 54 Ian0B 2015-03-07T15:07:22 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-07T15:07:22)
    0000   0x16 0xc7 0x2f 0xa7 0x0f                   ../..
    body (0)

#### RECORD 55 Ian0B 2015-03-07T15:11:05 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x4e                             .fN
    decimal
             11  102   78
    datetime (2015-03-07T15:11:05)
    0000   0x05 0xcb 0x2f 0xa7 0x0f                   ../..
    body (0)

#### RECORD 56 Ian0B 2015-03-07T15:42:34 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x49                             .fI
    decimal
             11  102   73
    datetime (2015-03-07T15:42:34)
    0000   0x22 0xea 0x2f 0xa7 0x0f                   "./..
    body (0)

#### RECORD 57 BolusWizard 2015-03-07T17:43:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 48,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-07T17:43:16)
    0000   0x10 0xeb 0x11 0x67 0x0f                   ...g.
    body (15)
    hex
    0000   0x30 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    0P.P(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             48   80    0   80   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 58 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 174, 'amount': 0.2, 'curve': 4},
 {'age': 184, 'amount': 0.35, 'curve': 4},
 {'age': 194, 'amount': 0.4, 'curve': 4},
 {'age': 204, 'amount': 0.35, 'curve': 4},
 {'age': 214, 'amount': 0.4, 'curve': 4},
 {'age': 224, 'amount': 0.35, 'curve': 4},
 {'age': 234, 'amount': 0.4, 'curve': 4},
 {'age': 244, 'amount': 0.35, 'curve': 4},
 {'age': 254, 'amount': 0.4, 'curve': 4},
 {'age': 8, 'amount': 0.35, 'curve': 20},
 {'age': 18, 'amount': 0.4, 'curve': 20},
 {'age': 28, 'amount': 0.35, 'curve': 20},
 {'age': 38, 'amount': 3.2, 'curve': 20}]
```
    op hex (41)
    0000   0x5c 0x29 0x08 0xae 0x04 0x0e 0xb8 0x04    \)......
    0008   0x10 0xc2 0x04 0x0e 0xcc 0x04 0x10 0xd6    ........
    0010   0x04 0x0e 0xe0 0x04 0x10 0xea 0x04 0x0e    ........
    0018   0xf4 0x04 0x10 0xfe 0x04 0x0e 0x08 0x14    ........
    0020   0x10 0x12 0x14 0x0e 0x1c 0x14 0x80 0x26    .......&
    0028   0x14                                       .
    decimal
             92   41    8  174    4   14  184    4
             16  194    4   14  204    4   16  214
              4   14  224    4   16  234    4   14
            244    4   16  254    4   14    8   20
             16   18   20   14   28   20  128   38
             20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2015-03-07T17:46:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 60,
 'programmed': 1.0,
 'type': 'square',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x0c 0x02    ..(.(...
    decimal
              1    0   40    0   40    0   12    2
    datetime (2015-03-07T17:46:37)
    0000   0x25 0xee 0xb1 0x67 0x0f                   %..g.
    body (0)

#### RECORD 60 Bolus 2015-03-07T17:43:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x0c 0x00    ........
    decimal
              1    0  200    0  200    0   12    0
    datetime (2015-03-07T17:43:16)
    0000   0x10 0xeb 0x91 0x67 0x0f                   ...g.
    body (0)

#### RECORD 61 Ian0B 2015-03-07T17:51:05 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-07T17:51:05)
    0000   0x05 0xf3 0x31 0xa7 0x0f                   ..1..
    body (0)

#### RECORD 62 Ian0B 2015-03-07T18:01:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xbc                             .e.
    decimal
             11  101  188
    datetime (2015-03-07T18:01:07)
    0000   0x07 0xc1 0x32 0xa7 0x0f                   ..2..
    body (0)

#### RECORD 63 Ian0B 2015-03-07T19:53:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-07T19:53:00)
    0000   0x00 0xf5 0x33 0xa7 0x0f                   ..3..
    body (0)

#### RECORD 64 Bolus 2015-03-07T20:32:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x38 0x00    ..(.(.8.
    decimal
              1    0   40    0   40    0   56    0
    datetime (2015-03-07T20:32:22)
    0000   0x16 0xe0 0x54 0x67 0x0f                   ..Tg.
    body (0)

#### RECORD 65 Bolus 2015-03-07T20:33:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x60 0x00    ..x.x.`.
    decimal
              1    0  120    0  120    0   96    0
    datetime (2015-03-07T20:33:27)
    0000   0x1b 0xe1 0x54 0x67 0x0f                   ..Tg.
    body (0)

#### RECORD 66 Ian0B 2015-03-07T20:53:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-07T20:53:00)
    0000   0x00 0xf5 0x34 0xa7 0x0f                   ..4..
    body (0)

#### RECORD 67 CalBGForPH 2015-03-07T20:55:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2015-03-07T20:55:28)
    0000   0x1c 0xf7 0x34 0x67 0x0f                   ..4g.
    body (0)

#### RECORD 68 Ian3F 2015-03-07T20:55:28 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-03-07T20:55:28)
    0000   0x1c 0xf7 0xb4 0x67 0x0f                   ...g.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 69 Ian0B 2015-03-07T21:07:21 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-03-07T21:07:21)
    0000   0x15 0xc7 0x35 0xa7 0x0f                   ..5..
    body (0)

#### RECORD 70 Bolus 2015-03-07T21:07:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 4.4}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xb0 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  176    0
    datetime (2015-03-07T21:07:36)
    0000   0x24 0xc7 0x55 0x67 0x0f                   $.Ug.
    body (0)

#### RECORD 71 Bolus 2015-03-07T21:55:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 4.5}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xb4 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  180    0
    datetime (2015-03-07T21:55:13)
    0000   0x0d 0xf7 0x55 0x67 0x0f                   ..Ug.
    body (0)

#### RECORD 72 BasalProfileStart 2015-03-07T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-07T22:00:00)
    0000   0x00 0xc0 0x16 0x07 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 73 BasalProfileStart 2015-03-08T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-08T00:00:00)
    0000   0x00 0xc0 0x00 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 74 MResultTotals 2015-03-08T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x06                   .....
    decimal
              7    0    0    8    6
    datetime (2015-03-08T00:00:00)
    0000   0x27 0x8f                                  '.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 75 Sara6E 2015-03-08T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-08T00:00:00)
    0000   0x27 0x8f                                  '.
    body (49)
    hex
    0000   0x05 0x00 0xa0 0x82 0xbd 0x02 0x00 0x00    ........
    0008   0x08 0x06 0x03 0x30 0x28 0x04 0xd6 0x3c    ...0(..<
    0010   0x00 0xad 0x02 0xda 0x00 0x08 0x00 0x00    ........
    0018   0x01 0xf4 0x03 0x01 0x00 0x06 0x00 0xa5    ........
    0020   0x21 0x3c 0x07 0x1e 0x42 0x01 0x02 0x00    !<..B...
    0028   0x00 0x05 0x06 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  160  130  189    2    0    0
              8    6    3   48   40    4  214   60
              0  173    2  218    0    8    0    0
              1  244    3    1    0    6    0  165
             33   60    7   30   66    1    2    0
              0    5    6    1    0    0    0    0
              0

#### RECORD 76 Ian0B 2015-03-08T00:06:23 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-08T00:06:23)
    0000   0x17 0xc6 0x20 0xa8 0x0f                   .. ..
    body (0)

#### RECORD 77 Bolus 2015-03-08T00:07:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x38 0x00    ..P.P.8.
    decimal
              1    0   80    0   80    0   56    0
    datetime (2015-03-08T00:07:28)
    0000   0x1c 0xc7 0x40 0x68 0x0f                   ..@h.
    body (0)

#### RECORD 78 Ian0B 2015-03-08T02:17:40 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-08T02:17:40)
    0000   0x28 0xd1 0x22 0xa8 0x0f                   (."..
    body (0)

#### RECORD 79 Ian0B 2015-03-08T02:41:06 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-08T02:41:06)
    0000   0x06 0xe9 0x22 0xa8 0x0f                   .."..
    body (0)

#### RECORD 80 BasalProfileStart 2015-03-08T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-08T04:00:00)
    0000   0x00 0xc0 0x04 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 81 Ian0B 2015-03-08T06:11:45 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-08T06:11:45)
    0000   0x2d 0xcb 0x26 0xa8 0x0f                   -.&..
    body (0)

`end analysis/736868/logs/ReadHistoryData-page-14.data: 82 records`
