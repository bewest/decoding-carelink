## START logs/ReadHistoryData-page-14.data
#### STOPPING DOUBLE NULLS @ 1013, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x60 0xb7                                  `.
##### DEBUG DECIMAL
             96  183
#### RECORD 0 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 130, 'amount': 1.45, 'curve': 192},
 {'age': 140, 'amount': 0.75, 'curve': 192},
 {'age': 160, 'amount': 1.0, 'curve': 192},
 {'age': 250, 'amount': 1.05, 'curve': 192},
 {'age': 4, 'amount': 1.85, 'curve': 208},
 {'age': 104, 'amount': 1.2, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x3a 0x82 0xc0 0x1e 0x8c 0xc0    \.:.....
    0008   0x28 0xa0 0xc0 0x2a 0xfa 0xc0 0x4a 0x04    (..*..J.
    0010   0xd0 0x30 0x68 0xd0                        .0h.
    decimal
             92   20   58  130  192   30  140  192
             40  160  192   42  250  192   74    4
            208   48  104  208
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-08-05T15:13:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x14 0x00    ..@.@...
    decimal
              1    0   64    0   64    0   20    0
    datetime (2013-08-05T15:13:38)
    0000   0xa6 0x0d 0x4f 0x05 0x0d                   ..O..
    body (0)

#### RECORD 2 CalBGForPH 2013-08-05T19:28:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-08-05T19:28:49)
    0000   0xb1 0x1c 0x33 0x05 0x0d                   ..3..
    body (0)

#### RECORD 3 BolusWizard 2013-08-05T19:28:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 146,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 18,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 1.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x92                                  [.
    decimal
             91  146
    datetime (2013-08-05T19:28:58)
    0000   0xba 0x1c 0x13 0x05 0x0d                   .....
    body (15)
    hex
    0000   0x12 0x50 0x00 0x64 0x3c 0x64 0x10 0x00    .P.d<d..
    0008   0x48 0x00 0x00 0x00 0x00 0x58 0x78         H....Xx
    decimal
             18   80    0  100   60  100   16    0
             72    0    0    0    0   88  120

#### RECORD 4 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 255, 'amount': 1.6, 'curve': 192},
 {'age': 129, 'amount': 1.45, 'curve': 208},
 {'age': 139, 'amount': 0.75, 'curve': 208},
 {'age': 159, 'amount': 1.0, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x40 0xff 0xc0 0x3a 0x81 0xd0    \.@..:..
    0008   0x1e 0x8b 0xd0 0x28 0x9f 0xd0              ...(..
    decimal
             92   14   64  255  192   58  129  208
             30  139  208   40  159  208
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-08-05T19:28:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    0    0
    datetime (2013-08-05T19:28:58)
    0000   0xba 0x1c 0x53 0x05 0x0d                   ..S..
    body (0)

#### RECORD 6 CalBGForPH 2013-08-05T20:17:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-08-05T20:17:08)
    0000   0x88 0x11 0x34 0x05 0x0d                   ..4..
    body (0)

#### RECORD 7 BolusWizard 2013-08-05T20:17:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 106,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-08-05T20:17:17)
    0000   0x91 0x11 0x14 0x05 0x0d                   .....
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x54 0x00 0x00 0x44 0x00 0x54 0x78         T..D.Tx
    decimal
             21   80    0  100   60  100    0    0
             84    0    0   68    0   84  120

#### RECORD 8 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 2.2, 'curve': 192},
 {'age': 48, 'amount': 1.6, 'curve': 208},
 {'age': 178, 'amount': 1.45, 'curve': 208},
 {'age': 188, 'amount': 0.75, 'curve': 208},
 {'age': 208, 'amount': 1.0, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x58 0x36 0xc0 0x40 0x30 0xd0    \.X6.@0.
    0008   0x3a 0xb2 0xd0 0x1e 0xbc 0xd0 0x28 0xd0    :.....(.
    0010   0xd0                                       .
    decimal
             92   17   88   54  192   64   48  208
             58  178  208   30  188  208   40  208
            208
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2013-08-05T20:17:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x44 0x00    ..T.T.D.
    decimal
              1    0   84    0   84    0   68    0
    datetime (2013-08-05T20:17:17)
    0000   0x91 0x11 0x54 0x05 0x0d                   ..T..
    body (0)

#### RECORD 10 Bolus 2013-08-05T22:05:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x24 0x00    ..(.(.$.
    decimal
              1    0   40    0   40    0   36    0
    datetime (2013-08-05T22:05:12)
    0000   0x8c 0x05 0x56 0x05 0x0d                   ..V..
    body (0)

#### RECORD 11 BasalProfileStart 2013-08-06T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-06T00:00:00)
    0000   0x80 0x00 0x00 0x06 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 12 ResultTotals (2000, 8, 0, 0, 13, 5) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x14                   .....
    decimal
              7    0    0    5   20
    datetime ((2000, 8, 0, 0, 13, 5))
    0000   0x85 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 13 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x85 0x0d 0x05 0x00 0xa9 0x00 0x00    n.......
    0008   0x07 0x00 0x00 0x05 0x14 0x02 0xdc 0x38    .......8
    0010   0x02 0x38 0x2c 0x00 0x6c 0x00 0xdc 0x00    .8,.l...
    0018   0x28 0x01 0x0c 0x00 0x28 0x03 0x01 0x03    (...(...
    0020   0x01 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6a 0x00 0x00 0x00 0x00         ..j....
    decimal
            110  133   13    5    0  169    0    0
              7    0    0    5   20    2  220   56
              2   56   44    0  108    0  220    0
             40    1   12    0   40    3    1    3
              1    4    0    0    0    0    0    0
              0    0  106    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 14 BasalProfileStart 2013-08-06T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-06T04:00:00)
    0000   0x80 0x00 0x04 0x06 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 15 BasalProfileStart 2013-08-06T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-06T08:00:00)
    0000   0x80 0x00 0x08 0x06 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 16 CalBGForPH 2013-08-06T11:57:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2013-08-06T11:57:00)
    0000   0x80 0x39 0x2b 0x06 0x8d                   .9+..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 BolusWizard 2013-08-06T11:57:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 268,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 9.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2013-08-06T11:57:52)
    0000   0xb4 0x39 0x0b 0x06 0x0d                   .9...
    body (15)
    hex
    0000   0x14 0x51 0x00 0x78 0x3c 0x64 0x60 0x00    .Q.x<d`.
    0008   0x40 0x00 0x00 0x00 0x00 0xa0 0x78         @.....x
    decimal
             20   81    0  120   60  100   96    0
             64    0    0    0    0  160  120
    HOUR BITS: [0, 0, 1]
#### RECORD 18 BasalProfileStart 2013-08-06T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-06T12:00:00)
    0000   0x80 0x00 0x0c 0x06 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 19 Bolus 2013-08-06T11:57:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x00 0x00    ........
    decimal
              1    0  160    0  160    0    0    0
    datetime (2013-08-06T11:57:53)
    0000   0xb5 0x39 0x4b 0x06 0x0d                   .9K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 CalBGForPH 2013-08-06T12:39:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-08-06T12:39:08)
    0000   0x88 0x27 0x2c 0x06 0x0d                   .',..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 21 BolusWizard 2013-08-06T12:39:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 13.2,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-08-06T12:39:13)
    0000   0x8d 0x27 0x0c 0x06 0x0d                   .'...
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x34 0x00 0x00 0x84 0x00 0x34 0x78         4....4x
    decimal
             16   80    0  120   60  100    0    0
             52    0    0  132    0   52  120
    HOUR BITS: [0, 0, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 4.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0xa0 0x2e 0xc0                   \....
    decimal
             92    5  160   46  192
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-08-06T12:39:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x84 0x00    ..4.4...
    decimal
              1    0   52    0   52    0  132    0
    datetime (2013-08-06T12:39:13)
    0000   0x8d 0x27 0x4c 0x06 0x0d                   .'L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 24 CalBGForPH 2013-08-06T13:52:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2013-08-06T13:52:17)
    0000   0x91 0x34 0x2d 0x06 0x0d                   .4-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 25 BolusWizard 2013-08-06T13:52:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 169,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.2,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0xa9                                  [.
    decimal
             91  169
    datetime (2013-08-06T13:52:28)
    0000   0x9c 0x34 0x0d 0x06 0x0d                   .4...
    body (15)
    hex
    0000   0x28 0x50 0x00 0x78 0x3c 0x64 0x20 0x00    (P.x<d .
    0008   0x84 0x00 0x00 0x48 0x00 0x84 0x78         ...H..x
    decimal
             40   80    0  120   60  100   32    0
            132    0    0   72    0  132  120
    HOUR BITS: [0, 0, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 79, 'amount': 1.3, 'curve': 192},
 {'age': 119, 'amount': 4.0, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x4f 0xc0 0xa0 0x77 0xc0    \.4O..w.
    decimal
             92    8   52   79  192  160  119  192
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-08-06T13:52:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x48 0x00    ......H.
    decimal
              1    0  132    0  132    0   72    0
    datetime (2013-08-06T13:52:28)
    0000   0x9c 0x34 0x4d 0x06 0x0d                   .4M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 CalBGForPH 2013-08-06T15:14:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-08-06T15:14:02)
    0000   0x82 0x0e 0x2f 0x06 0x0d                   ../..
    body (0)

#### RECORD 29 BolusWizard 2013-08-06T15:14:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-08-06T15:14:10)
    0000   0x8a 0x0e 0x0f 0x06 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x4c 0x00 0x00 0x78         ...L..x
    decimal
              0   80    0  120   60  100    0    0
              0    0    0   76    0    0  120

#### RECORD 30 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 81, 'amount': 2.5, 'curve': 192},
 {'age': 91, 'amount': 0.8, 'curve': 192},
 {'age': 161, 'amount': 1.3, 'curve': 192},
 {'age': 201, 'amount': 4.0, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0x64 0x51 0xc0 0x20 0x5b 0xc0    \.dQ. [.
    0008   0x34 0xa1 0xc0 0xa0 0xc9 0xc0              4.....
    decimal
             92   14  100   81  192   32   91  192
             52  161  192  160  201  192
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-08-06T15:14:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x4c 0x00    ..8.8.L.
    decimal
              1    0   56    0   56    0   76    0
    datetime (2013-08-06T15:14:10)
    0000   0x8a 0x0e 0x4f 0x06 0x0d                   ..O..
    body (0)

#### RECORD 32 CalBGForPH 2013-08-06T17:43:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 221}
```
    op hex (2)
    0000   0x0a 0xdd                                  ..
    decimal
             10  221
    datetime (2013-08-06T17:43:14)
    0000   0x8e 0x2b 0x31 0x06 0x0d                   .+1..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 BolusWizard 2013-08-06T17:43:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 221,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
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
    datetime (2013-08-06T17:43:17)
    0000   0x91 0x2b 0x11 0x06 0x0d                   .+...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x40 0x00    .P.d<d@.
    0008   0x00 0x00 0x00 0x08 0x00 0x38 0x78         .....8x
    decimal
              0   80    0  100   60  100   64    0
              0    0    0    8    0   56  120
    HOUR BITS: [0, 0, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 150, 'amount': 1.4, 'curve': 192},
 {'age': 230, 'amount': 2.5, 'curve': 192},
 {'age': 240, 'amount': 0.8, 'curve': 192},
 {'age': 54, 'amount': 1.3, 'curve': 208},
 {'age': 94, 'amount': 4.0, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x38 0x96 0xc0 0x64 0xe6 0xc0    \.8..d..
    0008   0x20 0xf0 0xc0 0x34 0x36 0xd0 0xa0 0x5e     ..46..^
    0010   0xd0                                       .
    decimal
             92   17   56  150  192  100  230  192
             32  240  192   52   54  208  160   94
            208
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-08-06T17:43:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x08 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    8    0
    datetime (2013-08-06T17:43:17)
    0000   0x91 0x2b 0x51 0x06 0x0d                   .+Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 CalBGForPH 2013-08-06T18:35:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2013-08-06T18:35:56)
    0000   0xb8 0x23 0x32 0x06 0x0d                   .#2..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 37 BolusWizard 2013-08-06T18:36:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 121,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x79                                  [y
    decimal
             91  121
    datetime (2013-08-06T18:36:02)
    0000   0x82 0x24 0x12 0x06 0x0d                   .$...
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x34 0x00 0x00 0x2c 0x00 0x34 0x78         4..,.4x
    decimal
             13   80    0  100   60  100    0    0
             52    0    0   44    0   52  120
    HOUR BITS: [0, 0, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 53, 'amount': 1.4, 'curve': 192},
 {'age': 203, 'amount': 1.4, 'curve': 192},
 {'age': 27, 'amount': 2.5, 'curve': 208},
 {'age': 37, 'amount': 0.8, 'curve': 208},
 {'age': 107, 'amount': 1.3, 'curve': 208},
 {'age': 147, 'amount': 4.0, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x38 0x35 0xc0 0x38 0xcb 0xc0    \.85.8..
    0008   0x64 0x1b 0xd0 0x20 0x25 0xd0 0x34 0x6b    d.. %.4k
    0010   0xd0 0xa0 0x93 0xd0                        ....
    decimal
             92   20   56   53  192   56  203  192
            100   27  208   32   37  208   52  107
            208  160  147  208
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-08-06T18:36:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x2c 0x00    ..4.4.,.
    decimal
              1    0   52    0   52    0   44    0
    datetime (2013-08-06T18:36:03)
    0000   0x83 0x24 0x52 0x06 0x0d                   .$R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 CalBGForPH 2013-08-06T18:54:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-08-06T18:54:58)
    0000   0xba 0x36 0x32 0x06 0x0d                   .62..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 41 BolusWizard 2013-08-06T18:55:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 110,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 8.4,
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
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-08-06T18:55:04)
    0000   0x84 0x37 0x12 0x06 0x0d                   .7...
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x30 0x00 0x00 0x54 0x00 0x30 0x78         0..T.0x
    decimal
             12   80    0  100   60  100    0    0
             48    0    0   84    0   48  120
    HOUR BITS: [0, 0, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 1.3, 'curve': 192},
 {'age': 72, 'amount': 1.4, 'curve': 192},
 {'age': 222, 'amount': 1.4, 'curve': 192},
 {'age': 46, 'amount': 2.5, 'curve': 208},
 {'age': 56, 'amount': 0.8, 'curve': 208},
 {'age': 126, 'amount': 1.3, 'curve': 208},
 {'age': 166, 'amount': 4.0, 'curve': 208}]
```
    op hex (23)
    0000   0x5c 0x17 0x34 0x16 0xc0 0x38 0x48 0xc0    \.4..8H.
    0008   0x38 0xde 0xc0 0x64 0x2e 0xd0 0x20 0x38    8..d.. 8
    0010   0xd0 0x34 0x7e 0xd0 0xa0 0xa6 0xd0         .4~....
    decimal
             92   23   52   22  192   56   72  192
             56  222  192  100   46  208   32   56
            208   52  126  208  160  166  208
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-08-06T18:55:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x54 0x00    ..0.0.T.
    decimal
              1    0   48    0   48    0   84    0
    datetime (2013-08-06T18:55:04)
    0000   0x84 0x37 0x52 0x06 0x0d                   .7R..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 44 CalBGForPH 2013-08-06T20:58:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-08-06T20:58:45)
    0000   0xad 0x3a 0x34 0x06 0x0d                   .:4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 BolusWizard 2013-08-06T20:59:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 2.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-08-06T20:59:09)
    0000   0x89 0x3b 0x14 0x06 0x0d                   .;...
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x1c 0x00    .P.d<d..
    0008   0x54 0x00 0x00 0x14 0x00 0x5c 0x78         T....\x
    decimal
             21   80    0  100   60  100   28    0
             84    0    0   20    0   92  120
    HOUR BITS: [0, 0, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 1.2, 'curve': 192},
 {'age': 146, 'amount': 1.3, 'curve': 192},
 {'age': 196, 'amount': 1.4, 'curve': 192},
 {'age': 90, 'amount': 1.4, 'curve': 208},
 {'age': 170, 'amount': 2.5, 'curve': 208},
 {'age': 180, 'amount': 0.8, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x30 0x7e 0xc0 0x34 0x92 0xc0    \.0~.4..
    0008   0x38 0xc4 0xc0 0x38 0x5a 0xd0 0x64 0xaa    8..8Z.d.
    0010   0xd0 0x20 0xb4 0xd0                        . ..
    decimal
             92   20   48  126  192   52  146  192
             56  196  192   56   90  208  100  170
            208   32  180  208
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-08-06T20:59:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x14 0x00    ..\.\...
    decimal
              1    0   92    0   92    0   20    0
    datetime (2013-08-06T20:59:09)
    0000   0x89 0x3b 0x54 0x06 0x0d                   .;T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 48 CalBGForPH 2013-08-06T23:14:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-06T23:14:08)
    0000   0x88 0x0e 0x37 0x06 0x0d                   ..7..
    body (0)

#### RECORD 49 BolusWizard 2013-08-06T23:14:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-06T23:14:14)
    0000   0x8e 0x0e 0x17 0x06 0x0d                   .....
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x3c 0x00 0x00 0x10 0x00 0x3c 0x78         <....<x
    decimal
             15   80    0  100   60  100    0    0
             60    0    0   16    0   60  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 141, 'amount': 2.3, 'curve': 192},
 {'age': 5, 'amount': 1.2, 'curve': 208},
 {'age': 25, 'amount': 1.3, 'curve': 208},
 {'age': 75, 'amount': 1.4, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x5c 0x8d 0xc0 0x30 0x05 0xd0    \.\..0..
    0008   0x34 0x19 0xd0 0x38 0x4b 0xd0              4..8K.
    decimal
             92   14   92  141  192   48    5  208
             52   25  208   56   75  208
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-08-06T23:14:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x10 0x00    ..<.<...
    decimal
              1    0   60    0   60    0   16    0
    datetime (2013-08-06T23:14:14)
    0000   0x8e 0x0e 0x57 0x06 0x0d                   ..W..
    body (0)

#### RECORD 52 CalBGForPH 2013-08-06T23:44:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2013-08-06T23:44:15)
    0000   0x8f 0x2c 0x37 0x06 0x0d                   .,7..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 53 BasalProfileStart 2013-08-07T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-07T00:00:00)
    0000   0x80 0x00 0x00 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 54 ResultTotals (2000, 8, 0, 0, 13, 6) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xa0                   .....
    decimal
              7    0    0    5  160
    datetime ((2000, 8, 0, 0, 13, 6))
    0000   0x86 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 55 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x86 0x0d 0x05 0x00 0x9a 0x00 0x00    n.......
    0008   0x0a 0x00 0x00 0x05 0xa0 0x02 0xdc 0x33    .......3
    0010   0x02 0xc4 0x31 0x00 0x89 0x01 0x58 0x00    ..1...X.
    0018   0x70 0x00 0xfc 0x00 0x00 0x05 0x02 0x02    p.......
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x64 0x0c 0x00 0x00 0x00         ..d....
    decimal
            110  134   13    5    0  154    0    0
             10    0    0    5  160    2  220   51
              2  196   49    0  137    1   88    0
            112    0  252    0    0    5    2    2
              0    4    0    0    0    0    0    0
              0    0  100   12    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 56 BasalProfileStart 2013-08-07T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-07T04:00:00)
    0000   0x80 0x00 0x04 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 57 LowBattery 2013-08-07T05:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-08-07T05:01:00)
    0000   0x80 0x01 0x05 0x07 0x0d                   .....
    body (0)

#### RECORD 58 BasalProfileStart 2013-08-07T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-07T08:00:00)
    0000   0x80 0x00 0x08 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 59 LowBattery 2013-08-07T10:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-08-07T10:01:00)
    0000   0x80 0x01 0x0a 0x07 0x0d                   .....
    body (0)

#### RECORD 60 CalBGForPH 2013-08-07T11:57:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2013-08-07T11:57:47)
    0000   0xaf 0x39 0x2b 0x07 0x0d                   .9+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 BolusWizard 2013-08-07T11:57:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 132,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2013-08-07T11:57:53)
    0000   0xb5 0x39 0x0b 0x07 0x0d                   .9...
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x08 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x00 0x00 0x30 0x78         (....0x
    decimal
             13   80    0  120   60  100    8    0
             40    0    0    0    0   48  120
    HOUR BITS: [0, 0, 1]
#### RECORD 62 Bolus 2013-08-07T11:57:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-08-07T11:57:53)
    0000   0xb5 0x39 0x4b 0x07 0x0d                   .9K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 63 BasalProfileStart 2013-08-07T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-07T12:00:00)
    0000   0x80 0x00 0x0c 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 64 CalBGForPH 2013-08-07T13:23:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 133}
```
    op hex (2)
    0000   0x0a 0x85                                  ..
    decimal
             10  133
    datetime (2013-08-07T13:23:36)
    0000   0xa4 0x17 0x2d 0x07 0x0d                   ..-..
    body (0)

#### RECORD 65 BolusWizard 2013-08-07T13:23:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 133,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.4,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x85                                  [.
    decimal
             91  133
    datetime (2013-08-07T13:23:43)
    0000   0xab 0x17 0x0d 0x07 0x0d                   .....
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x08 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x18 0x00 0x28 0x78         (....(x
    decimal
             12   80    0  120   60  100    8    0
             40    0    0   24    0   40  120

#### RECORD 66 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 90, 'amount': 1.2, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0x5a 0xc0                   \.0Z.
    decimal
             92    5   48   90  192
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-08-07T13:23:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x18 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   24    0
    datetime (2013-08-07T13:23:43)
    0000   0xab 0x17 0x4d 0x07 0x0d                   ..M..
    body (0)

#### RECORD 68 CalBGForPH 2013-08-07T15:20:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 213}
```
    op hex (2)
    0000   0x0a 0xd5                                  ..
    decimal
             10  213
    datetime (2013-08-07T15:20:35)
    0000   0xa3 0x14 0x2f 0x07 0x0d                   ../..
    body (0)

#### RECORD 69 BolusWizard 2013-08-07T15:20:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 213,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd5                                  [.
    decimal
             91  213
    datetime (2013-08-07T15:20:38)
    0000   0xa6 0x14 0x0f 0x07 0x0d                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x3c 0x00    .P.x<d<.
    0008   0x00 0x00 0x00 0x0c 0x00 0x30 0x78         .....0x
    decimal
              0   80    0  120   60  100   60    0
              0    0    0   12    0   48  120

#### RECORD 70 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 117, 'amount': 1.0, 'curve': 192},
 {'age': 207, 'amount': 1.2, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x75 0xc0 0x30 0xcf 0xc0    \.(u.0..
    decimal
             92    8   40  117  192   48  207  192
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-14.data: 71 records`
