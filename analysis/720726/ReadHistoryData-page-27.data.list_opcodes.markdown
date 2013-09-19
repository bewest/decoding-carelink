## START analysis/ianj/raw//ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xad 0x4e                                  .N
##### DEBUG DECIMAL
            173   78
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
#### RECORD 32 Ian69 2013-08-06T08:44:52 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-08-06T08:44:52)
    0000   0xb4 0x2c 0x08 0x06 0x0d                   .,...
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [0, 0, 1]
#### RECORD 33 Bolus 2013-08-06T08:44:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 15.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x00 0x00    ........
    decimal
              1    0  156    0  156    0    0    0
    datetime (2013-08-06T08:44:52)
    0000   0xb4 0x2c 0x48 0x66 0x0d                   .,Hf.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 BasalProfileStart 2013-08-06T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-06T09:30:00)
    0000   0x80 0x1e 0x09 0x06 0x0d                   .....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0

#### RECORD 35 CalBGForPH 2013-08-06T12:11:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2013-08-06T12:11:56)
    0000   0xb8 0x0b 0x2c 0x66 0x0d                   ..,f.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 36 Ian3F 2013-08-06T12:11:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2013-08-06T12:11:56)
    0000   0xb8 0x0b 0xcc 0x66 0x0d                   ...f.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 37 BasalProfileStart 2013-08-06T13:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-06T13:00:00)
    0000   0x80 0x00 0x0d 0x06 0x0d                   .....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0

#### RECORD 38 CalBGForPH 2013-08-06T13:10:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-08-06T13:10:18)
    0000   0x92 0x0a 0x2d 0x66 0x0d                   ..-f.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 39 Ian3F 2013-08-06T13:10:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2013-08-06T13:10:18)
    0000   0x92 0x0a 0x8d 0x66 0x0d                   ...f.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 40 BolusWizard 2013-08-06T13:13:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 69,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 2.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x45                                  [E
    decimal
             91   69
    datetime (2013-08-06T13:13:11)
    0000   0x8b 0x0d 0x0d 0x66 0x0d                   ...f.
    body (15)
    hex
    0000   0x28 0x90 0x00 0x6e 0x17 0x36 0x18 0x00    (..n.6..
    0008   0x90 0x00 0x00 0x00 0x00 0xa8 0x36         ......6
    decimal
             40  144    0  110   23   54   24    0
            144    0    0    0    0  168   54
    DAY BITS: [0, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 3.7, 'curve': 20},
 {'age': 22, 'amount': 0.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x94 0x0c 0x14 0x08 0x16 0x14    \.......
    decimal
             92    8  148   12   20    8   22   20
    datetime (unknown)

    body (0)

#### RECORD 42 Ian69 2013-08-06T13:13:11 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-08-06T13:13:11)
    0000   0x8b 0x0d 0x0d 0x06 0x0d                   .....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30

#### RECORD 43 Bolus 2013-08-06T13:13:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x00 0x00    ........
    decimal
              1    0  168    0  168    0    0    0
    datetime (2013-08-06T13:13:11)
    0000   0x8b 0x0d 0x4d 0x66 0x0d                   ..Mf.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 44 BolusWizard 2013-08-06T13:55:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-06T13:55:47)
    0000   0xaf 0x37 0x0d 0x66 0x0d                   .7.f.
    body (15)
    hex
    0000   0x0c 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x36         (....(6
    decimal
             12  144    0  110   23   54    0    0
             40    0    0    0    0   40   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 1.5, 'curve': 4},
 {'age': 50, 'amount': 2.7, 'curve': 4},
 {'age': 54, 'amount': 3.7, 'curve': 20},
 {'age': 64, 'amount': 0.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x3c 0x28 0x04 0x6c 0x32 0x04    \.<(.l2.
    0008   0x94 0x36 0x14 0x08 0x40 0x14              .6..@.
    decimal
             92   14   60   40    4  108   50    4
            148   54   20    8   64   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2013-08-06T13:55:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x98 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  152    0
    datetime (2013-08-06T13:55:47)
    0000   0xaf 0x37 0x4d 0x66 0x0d                   .7Mf.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2013-08-06T19:06:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 37,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-06T19:06:10)
    0000   0x8a 0x06 0x13 0x66 0x0d                   ...f.
    body (15)
    hex
    0000   0x25 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    %..n.6..
    0008   0x84 0x00 0x00 0x00 0x00 0x84 0x36         ......6
    decimal
             37  144    0  110   23   54    0    0
            132    0    0    0    0  132   54
    DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 1.0, 'curve': 20},
 {'age': 95, 'amount': 1.5, 'curve': 20},
 {'age': 105, 'amount': 2.7, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x37 0x14 0x3c 0x5f 0x14    \.(7.<_.
    0008   0x6c 0x69 0x14                             li.
    decimal
             92   11   40   55   20   60   95   20
            108  105   20
    datetime (unknown)

    body (0)

#### RECORD 49 Ian69 2013-08-06T19:06:10 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-08-06T19:06:10)
    0000   0x8a 0x06 0x73 0x06 0x0d                   ..s..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30

#### RECORD 50 Bolus 2013-08-06T19:06:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x00 0x00    ........
    decimal
              1    0  132    0  132    0    0    0
    datetime (2013-08-06T19:06:10)
    0000   0x8a 0x06 0x53 0x66 0x0d                   ..Sf.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 51 BolusWizard 2013-08-06T19:21:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-06T19:21:15)
    0000   0x8f 0x15 0x13 0x66 0x0d                   ...f.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    DAY BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 3.3, 'curve': 4},
 {'age': 70, 'amount': 1.0, 'curve': 20},
 {'age': 110, 'amount': 1.5, 'curve': 20},
 {'age': 120, 'amount': 2.7, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x84 0x10 0x04 0x28 0x46 0x14    \....(F.
    0008   0x3c 0x6e 0x14 0x6c 0x78 0x14              <n.lx.
    decimal
             92   14  132   16    4   40   70   20
             60  110   20  108  120   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-08-06T19:21:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x84 0x00    ..$.$...
    decimal
              1    0   36    0   36    0  132    0
    datetime (2013-08-06T19:21:15)
    0000   0x8f 0x15 0x53 0x66 0x0d                   ..Sf.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 54 BolusWizard 2013-08-06T21:30:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-08-06T21:30:51)
    0000   0xb3 0x1e 0x15 0x66 0x0d                   ...f.
    body (15)
    hex
    0000   0x0f 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x36         4....46
    decimal
             15  144    0  110   23   54    0    0
             52    0    0    0    0   52   54
    DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 135, 'amount': 0.9, 'curve': 4},
 {'age': 145, 'amount': 3.3, 'curve': 4},
 {'age': 199, 'amount': 1.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x24 0x87 0x04 0x84 0x91 0x04    \.$.....
    0008   0x28 0xc7 0x14                             (..
    decimal
             92   11   36  135    4  132  145    4
             40  199   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-08-06T21:30:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x38 0x00    ..4.4.8.
    decimal
              1    0   52    0   52    0   56    0
    datetime (2013-08-06T21:30:51)
    0000   0xb3 0x1e 0x55 0x66 0x0d                   ..Uf.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 57 CalBGForPH 2013-08-06T22:06:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 191}
```
    op hex (2)
    0000   0x0a 0xbf                                  ..
    decimal
             10  191
    datetime (2013-08-06T22:06:26)
    0000   0x9a 0x06 0x36 0x66 0x0d                   ..6f.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 58 Ian3F 2013-08-06T22:06:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2013-08-06T22:06:26)
    0000   0x9a 0x06 0xf6 0x66 0x0d                   ...f.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 59 CalBGForPH 2013-08-06T23:15:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 233}
```
    op hex (2)
    0000   0x0a 0xe9                                  ..
    decimal
             10  233
    datetime (2013-08-06T23:15:30)
    0000   0x9e 0x0f 0x37 0x66 0x0d                   ..7f.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 60 Ian3F 2013-08-06T23:15:30 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2013-08-06T23:15:30)
    0000   0x9e 0x0f 0x37 0x66 0x0d                   ..7f.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 61 CalBGForPH 2013-08-06T23:23:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2013-08-06T23:23:10)
    0000   0x8a 0x17 0x37 0x66 0x0d                   ..7f.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 62 Ian3F 2013-08-06T23:23:10 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2013-08-06T23:23:10)
    0000   0x8a 0x17 0xf7 0x66 0x0d                   ...f.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    DAY BITS: [0, 1, 1]
#### RECORD 63 BolusWizard 2013-08-06T23:23:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 119,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 2.8,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 11.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x77                                  [w
    decimal
             91  119
    datetime (2013-08-06T23:23:26)
    0000   0x9a 0x17 0x17 0x66 0x0d                   ...f.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x70 0x00    ...n.6p.
    0008   0x50 0x00 0x00 0x1c 0x00 0xa4 0x36         P.....6
    decimal
             22  144    0  110   23   54  112    0
             80    0    0   28    0  164   54
    DAY BITS: [0, 1, 1]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 118, 'amount': 1.3, 'curve': 4},
 {'age': 248, 'amount': 0.9, 'curve': 4},
 {'age': 2, 'amount': 3.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x76 0x04 0x24 0xf8 0x04    \.4v.$..
    0008   0x84 0x02 0x14                             ...
    decimal
             92   11   52  118    4   36  248    4
            132    2   20
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-08-06T23:23:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x1c 0x00    ........
    decimal
              1    0  164    0  164    0   28    0
    datetime (2013-08-06T23:23:27)
    0000   0x9b 0x17 0x57 0x66 0x0d                   ..Wf.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 66 CalBGForPH 2013-08-06T23:36:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-08-06T23:36:22)
    0000   0x96 0x24 0x37 0x66 0x0d                   .$7f.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 Ian3F 2013-08-06T23:36:22 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2013-08-06T23:36:22)
    0000   0x96 0x24 0x17 0x66 0x0d                   .$.f.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 68 BolusWizard 2013-08-06T23:36:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 111,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 18.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 9.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-08-06T23:36:33)
    0000   0xa1 0x24 0x17 0x66 0x0d                   .$.f.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x60 0x00    ...n.6`.
    0008   0x00 0x00 0x00 0xb8 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54   96    0
              0    0    0  184    0    0   54
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 1.8, 'curve': 4},
 {'age': 21, 'amount': 2.3, 'curve': 4},
 {'age': 131, 'amount': 1.3, 'curve': 4},
 {'age': 5, 'amount': 0.9, 'curve': 20},
 {'age': 15, 'amount': 3.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x48 0x0b 0x04 0x5c 0x15 0x04    \.H..\..
    0008   0x34 0x83 0x04 0x24 0x05 0x14 0x84 0x0f    4..$....
    0010   0x14                                       .
    decimal
             92   17   72   11    4   92   21    4
             52  131    4   36    5   20  132   15
             20
    datetime (unknown)

    body (0)

#### RECORD 70 BasalProfileStart 2013-08-07T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-07T00:00:00)
    0000   0x80 0x00 0x00 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 71 ResultTotals (2000, 8, 0, 0, 13, 6) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xc3                   .....
    decimal
              7    0    0    6  195
    datetime ((2000, 8, 0, 0, 13, 6))
    0000   0x86 0x0d 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 72 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x86 0x0d 0x06 0x10 0xc6 0x7c 0x03    n.....|.
    0008   0x08 0x00 0x00 0x06 0xc3 0x03 0x89 0x34    .......4
    0010   0x03 0x3a 0x30 0x00 0xb5 0x01 0x52 0x00    .:0...R.
    0018   0x9c 0x01 0x4c 0x00 0x00 0x06 0x01 0x02    ..L.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  134   13    6   16  198  124    3
              8    0    0    6  195    3  137   52
              3   58   48    0  181    1   82    0
            156    1   76    0    0    6    1    2
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 73 BasalProfileStart 2013-08-07T00:17:37 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-07T00:17:37)
    0000   0xa5 0x11 0x00 0x07 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0

#### RECORD 74 Prime 2013-08-07T00:17:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-07T00:17:03)
    0000   0x83 0x11 0x00 0x07 0x0d                   .....
    body (0)

`end analysis/ianj/raw//ReadHistoryData-page-27.data: 75 records`
