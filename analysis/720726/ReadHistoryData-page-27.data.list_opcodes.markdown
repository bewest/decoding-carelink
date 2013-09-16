## START logs/ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 462, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xb4 0x2c 0x48 0x66 0x0d 0x7b 0x02 0x80    .,Hf.{..
    0008   0x1e 0x09 0x06 0x0d 0x13 0x1e 0x00 0x0a    ........
    0010   0x8e 0xb8 0x0b 0x2c 0x66 0x0d 0x3f 0x11    ...,f.?.
    0018   0xb8 0x0b 0xcc 0x66 0x0d 0x69 0x69 0x96    ...f.ii.
##### DEBUG DECIMAL
            180   44   72  102   13  123    2  128
             30    9    6   13   19   30    0   10
            142  184   11   44  102   13   63   17
            184   11  204  102   13  105  105  150
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 97, 'amount': 5.7, 'curve': 4},
 {'age': 107, 'amount': 0.7, 'curve': 4},
 {'age': 81, 'amount': 2.5, 'curve': 20},
 {'age': 181, 'amount': 3.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xe4 0x61 0x04 0x1c 0x6b 0x04    \..a..k.
    0008   0x64 0x51 0x14 0x9c 0xb5 0x14              dQ....
    decimal
             92   14  228   97    4   28  107    4
            100   81   20  156  181   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-08-05T19:52:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x9c 0x00    ........
    decimal
              1    0  132    0  132    0  156    0
    datetime (2013-08-05T19:52:24)
    0000   0x98 0x34 0x53 0x65 0x0d                   .4Se.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-08-05T20:09:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-08-05T20:09:49)
    0000   0xb1 0x09 0x34 0x65 0x0d                   ..4e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 3 Ian3F 2013-08-05T20:09:49 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2013-08-05T20:09:49)
    0000   0xb1 0x09 0x14 0x65 0x0d                   ...e.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 4 BolusWizard 2013-08-05T20:50:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-05T20:50:19)
    0000   0x93 0x32 0x14 0x65 0x0d                   .2.e.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 65, 'amount': 3.3, 'curve': 4},
 {'age': 155, 'amount': 5.7, 'curve': 4},
 {'age': 165, 'amount': 0.7, 'curve': 4},
 {'age': 139, 'amount': 2.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x84 0x41 0x04 0xe4 0x9b 0x04    \..A....
    0008   0x1c 0xa5 0x04 0x64 0x8b 0x14              ...d..
    decimal
             92   14  132   65    4  228  155    4
             28  165    4  100  139   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2013-08-05T20:50:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0xb0 0x00    ..l.l...
    decimal
              1    0  108    0  108    0  176    0
    datetime (2013-08-05T20:50:19)
    0000   0x93 0x32 0x54 0x65 0x0d                   .2Te.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 CalBGForPH 2013-08-05T22:43:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2013-08-05T22:43:38)
    0000   0xa6 0x2b 0x36 0x65 0x0d                   .+6e.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 Ian3F 2013-08-05T22:43:38 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2013-08-05T22:43:38)
    0000   0xa6 0x2b 0x36 0x65 0x0d                   .+6e.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 CalBGForPH 2013-08-05T23:04:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 172}
```
    op hex (2)
    0000   0x0a 0xac                                  ..
    decimal
             10  172
    datetime (2013-08-05T23:04:22)
    0000   0x96 0x04 0x37 0x65 0x0d                   ..7e.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 10 Ian3F 2013-08-05T23:04:22 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2013-08-05T23:04:22)
    0000   0x96 0x04 0x97 0x65 0x0d                   ...e.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 11 BolusWizard 2013-08-05T23:48:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 26,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 92}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-05T23:48:56)
    0000   0xb8 0x30 0x17 0x65 0x0d                   .0.e.
    body (15)
    hex
    0000   0x1a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x5c 0x00 0x00 0x00 0x00 0x5c 0x36         \....\6
    decimal
             26  144    0  110   23   54    0    0
             92    0    0    0    0   92   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 183, 'amount': 2.7, 'curve': 4},
 {'age': 243, 'amount': 3.3, 'curve': 4},
 {'age': 77, 'amount': 5.7, 'curve': 20},
 {'age': 87, 'amount': 0.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x6c 0xb7 0x04 0x84 0xf3 0x04    \.l.....
    0008   0xe4 0x4d 0x14 0x1c 0x57 0x14              .M..W.
    decimal
             92   14  108  183    4  132  243    4
            228   77   20   28   87   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-08-05T23:48:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x14 0x00    ..\.\...
    decimal
              1    0   92    0   92    0   20    0
    datetime (2013-08-05T23:48:56)
    0000   0xb8 0x30 0x57 0x65 0x0d                   .0We.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 BasalProfileStart 2013-08-06T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-06T00:00:00)
    0000   0x80 0x00 0x00 0x06 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 15 ResultTotals (2000, 8, 0, 0, 13, 5) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x75                   ....u
    decimal
              7    0    0    7  117
    datetime ((2000, 8, 0, 0, 13, 5))
    0000   0x85 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 16 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x85 0x0d 0x06 0x00 0xa8 0x70 0xea    n.....p.
    0008   0x08 0x00 0x00 0x07 0x75 0x03 0x89 0x2f    ....u../
    0010   0x03 0xec 0x35 0x00 0xeb 0x02 0xc4 0x00    ..5.....
    0018   0x00 0x01 0x00 0x00 0x28 0x07 0x00 0x01    ....(...
    0020   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  133   13    6    0  168  112  234
              8    0    0    7  117    3  137   47
              3  236   53    0  235    2  196    0
              0    1    0    0   40    7    0    1
              1    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 17 BolusWizard 2013-08-06T00:19:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 72}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-06T00:19:41)
    0000   0xa9 0x13 0x00 0x66 0x0d                   ...f.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 2.3, 'curve': 4},
 {'age': 214, 'amount': 2.7, 'curve': 4},
 {'age': 18, 'amount': 3.3, 'curve': 20},
 {'age': 108, 'amount': 5.7, 'curve': 20},
 {'age': 118, 'amount': 0.7, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x5c 0x22 0x04 0x6c 0xd6 0x04    \.\".l..
    0008   0x84 0x12 0x14 0xe4 0x6c 0x14 0x1c 0x76    ....l..v
    0010   0x14                                       .
    decimal
             92   17   92   34    4  108  214    4
            132   18   20  228  108   20   28  118
             20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-08-06T00:19:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x60 0x00    ..H.H.`.
    decimal
              1    0   72    0   72    0   96    0
    datetime (2013-08-06T00:19:41)
    0000   0xa9 0x13 0x40 0x66 0x0d                   ..@f.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 20 CalBGForPH 2013-08-06T00:36:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 221}
```
    op hex (2)
    0000   0x0a 0xdd                                  ..
    decimal
             10  221
    datetime (2013-08-06T00:36:10)
    0000   0x8a 0x24 0x20 0x66 0x0d                   .$ f.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 Ian3F 2013-08-06T00:36:10 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1b                                  ?.
    decimal
             63   27
    datetime (2013-08-06T00:36:10)
    0000   0x8a 0x24 0xa0 0x66 0x0d                   .$.f.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2013-08-06T00:36:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 123,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 16.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 12.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x7b                                  [{
    decimal
             91  123
    datetime (2013-08-06T00:36:36)
    0000   0xa4 0x24 0x00 0x66 0x0d                   .$.f.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x78 0x00    ...n.6x.
    0008   0x58 0x00 0x00 0xa0 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54  120    0
             88    0    0  160    0   88   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 1.8, 'curve': 4},
 {'age': 51, 'amount': 2.3, 'curve': 4},
 {'age': 231, 'amount': 2.7, 'curve': 4},
 {'age': 35, 'amount': 3.3, 'curve': 20},
 {'age': 125, 'amount': 5.7, 'curve': 20},
 {'age': 135, 'amount': 0.7, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x15 0x04 0x5c 0x33 0x04    \.H..\3.
    0008   0x6c 0xe7 0x04 0x84 0x23 0x14 0xe4 0x7d    l...#..}
    0010   0x14 0x1c 0x87 0x14                        ....
    decimal
             92   20   72   21    4   92   51    4
            108  231    4  132   35   20  228  125
             20   28  135   20
    datetime (unknown)

    body (0)

#### RECORD 24 PumpSuspend 2013-08-06T00:36:41 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-08-06T00:36:41)
    0000   0xa9 0x24 0x00 0x06 0x0d                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 25 Bolus 2013-08-06T00:36:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x06 0x00 0xa0 0x00    ..X.....
    decimal
              1    0   88    0    6    0  160    0
    datetime (2013-08-06T00:36:36)
    0000   0xa4 0x24 0x40 0x66 0x0d                   .$@f.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 BasalProfileStart 2013-08-06T00:36:46 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-06T00:36:46)
    0000   0xae 0x24 0x00 0x06 0x0d                   .$...
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [0, 0, 1]
#### RECORD 27 PumpResume 2013-08-06T00:36:46 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-08-06T00:36:46)
    0000   0xae 0x24 0x00 0x06 0x0d                   .$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 BasalProfileStart 2013-08-06T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-06T04:00:00)
    0000   0x80 0x00 0x04 0x06 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0

#### RECORD 29 CalBGForPH 2013-08-06T08:44:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 259}
```
    op hex (2)
    0000   0x0a 0x03                                  ..
    decimal
             10    3
    datetime (2013-08-06T08:44:40)
    0000   0xa8 0x2c 0x28 0x66 0x8d                   .,(f.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 Ian3F 2013-08-06T08:44:40 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2013-08-06T08:44:40)
    0000   0xa8 0x2c 0x68 0x66 0x0d                   .,hf.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2013-08-06T08:44:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 144,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 15.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x90                                  [.
    decimal
             91  144
    datetime (2013-08-06T08:44:52)
    0000   0xb4 0x2c 0x08 0x66 0x0d                   .,.f.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x9c 0x00    ...n.6..
    0008   0x00 0x00 0x00 0x00 0x00 0x9c 0x36         ......6
    decimal
              0  144    0  110   23   54  156    0
              0    0    0    0    0  156   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 Ian69 2013-08-06T08:44:52 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-06T08:44:52)
    0000   0xb4 0x2c 0x08 0x06 0x0d                   .,...
    body (8)
    hex
    0000   0x0a 0x1e 0x01 0x00 0x9c 0x00 0x9c 0x00    ........
    decimal
             10   30    1    0  156    0  156    0
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-27.data: 33 records`
