## START logs/ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 1013, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xff 0x20                                  . 
##### DEBUG DECIMAL
            255   32
#### RECORD 0 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x81 0x8d 0x05 0x00 0xc1 0x00 0x00    n.......
    0008   0x08 0x00 0x00 0x04 0xdb 0x02 0xc3 0x39    .......9
    0010   0x02 0x18 0x2b 0x00 0x56 0x00 0xc8 0x00    ..+.V...
    0018   0x88 0x00 0xc8 0x00 0x00 0x03 0x03 0x01    ........
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x72 0x2c 0x00 0x00 0x00         ..r,...
    decimal
            110  129  141    5    0  193    0    0
              8    0    0    4  219    2  195   57
              2   24   43    0   86    0  200    0
            136    0  200    0    0    3    3    1
              0    4    0    0    0    0    0    0
              0    0  114   44    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 1 BasalProfileStart 2013-09-02T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-09-02T04:00:00)
    0000   0x80 0x40 0x04 0x02 0x0d                   .@...
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0
    HOUR BITS: [0, 1, 0]
#### RECORD 2 BasalProfileStart 2013-09-02T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-09-02T08:00:00)
    0000   0x80 0x40 0x08 0x02 0x0d                   .@...
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0
    HOUR BITS: [0, 1, 0]
#### RECORD 3 CalBGForPH 2013-09-02T09:56:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-09-02T09:56:06)
    0000   0x86 0x78 0x29 0x02 0x0d                   .x)..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 4 BolusWizard 2013-09-02T09:56:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 110,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 19,
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
    0000   0x5b 0x6e                                  [n
    decimal
             91  110
    datetime (2013-09-02T09:56:14)
    0000   0x8e 0x78 0x09 0x02 0x0d                   .x...
    body (15)
    hex
    0000   0x13 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x3c 0x00 0x00 0x00 0x00 0x3c 0x78         <....<x
    decimal
             19   80    0  120   60  100    0    0
             60    0    0    0    0   60  120
    HOUR BITS: [0, 1, 1]
#### RECORD 5 Bolus 2013-09-02T09:56:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2013-09-02T09:56:15)
    0000   0x8f 0x78 0x49 0x02 0x0d                   .xI..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 6 BasalProfileStart 2013-09-02T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-02T12:00:00)
    0000   0x80 0x40 0x0c 0x02 0x0d                   .@...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 7 CalBGForPH 2013-09-02T15:26:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 275}
```
    op hex (2)
    0000   0x0a 0x13                                  ..
    decimal
             10   19
    datetime (2013-09-02T15:26:15)
    0000   0x8f 0x5a 0x2f 0x02 0x8d                   .Z/..
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 BolusWizard 2013-09-02T15:26:17 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 275,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x13                                  [.
    decimal
             91   19
    datetime (2013-09-02T15:26:17)
    0000   0x91 0x5a 0x0f 0x02 0x0d                   .Z...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x64 0x00    .Q.x<dd.
    0008   0x00 0x00 0x00 0x00 0x00 0x64 0x78         .....dx
    decimal
              0   81    0  120   60  100  100    0
              0    0    0    0    0  100  120
    HOUR BITS: [0, 1, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 74, 'amount': 1.5, 'curve': 208}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x4a 0xd0                   \.<J.
    decimal
             92    5   60   74  208
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-09-02T15:26:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x00 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    0    0
    datetime (2013-09-02T15:26:17)
    0000   0x91 0x5a 0x4f 0x02 0x0d                   .ZO..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 11 BolusWizard 2013-09-02T15:28:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 275,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 10.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 10.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x13                                  [.
    decimal
             91   19
    datetime (2013-09-02T15:28:50)
    0000   0xb2 0x5c 0x0f 0x02 0x0d                   .\...
    body (15)
    hex
    0000   0x0f 0x51 0x00 0x78 0x3c 0x64 0x64 0x00    .Q.x<dd.
    0008   0x30 0x00 0x00 0x64 0x00 0x30 0x78         0..d.0x
    decimal
             15   81    0  120   60  100  100    0
             48    0    0  100    0   48  120
    HOUR BITS: [0, 1, 0]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 2.5, 'curve': 192},
 {'age': 76, 'amount': 1.5, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0x02 0xc0 0x3c 0x4c 0xd0    \.d..<L.
    decimal
             92    8  100    2  192   60   76  208
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2013-09-02T15:28:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x08 0x00 0x64 0x00    ..0...d.
    decimal
              1    0   48    0    8    0  100    0
    datetime (2013-09-02T15:28:50)
    0000   0xb2 0x5c 0x4f 0x02 0x0d                   .\O..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 14 NoDelivery 2013-09-02T15:29:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2013-09-02T15:29:00)
    0000   0x80 0x5d 0x4f 0x42 0x0d                   .]OB.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 15 ClearAlarm 2013-09-02T15:29:14 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2013-09-02T15:29:14)
    0000   0x8e 0x5d 0x0f 0x02 0x0d                   .]...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 16 BasalProfileStart 2013-09-02T15:29:18 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-02T15:29:18)
    0000   0x92 0x5d 0x0f 0x02 0x0d                   .]...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 17 NoDelivery 2013-09-02T16:06:12 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2013-09-02T16:06:12)
    0000   0x8c 0x46 0x50 0x42 0x0d                   .FPB.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
#### RECORD 18 ClearAlarm 2013-09-02T16:07:49 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2013-09-02T16:07:49)
    0000   0xb1 0x47 0x10 0x02 0x0d                   .G...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 19 Rewind 2013-09-02T16:07:58 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-09-02T16:07:58)
    0000   0xba 0x47 0x10 0x02 0x0d                   .G...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 20 Prime 2013-09-02T16:11:46 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1a                   .....
    decimal
              3    0    0    0   26
    datetime (2013-09-02T16:11:46)
    0000   0xae 0x4b 0x30 0x02 0x0d                   .K0..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 21 BasalProfileStart 2013-09-02T16:12:35 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-02T16:12:35)
    0000   0xa3 0x4c 0x10 0x02 0x0d                   .L...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 22 CalBGForPH 2013-09-02T16:39:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-09-02T16:39:02)
    0000   0x82 0x67 0x30 0x02 0x0d                   .g0..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2013-09-02T16:39:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
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
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-09-02T16:39:08)
    0000   0x88 0x67 0x10 0x02 0x0d                   .g...
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x44 0x00 0x28 0x78         (..D.(x
    decimal
             12   80    0  120   60  100    0    0
             40    0    0   68    0   40  120
    HOUR BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 2.7, 'curve': 192},
 {'age': 147, 'amount': 1.5, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x49 0xc0 0x3c 0x93 0xd0    \.lI.<..
    decimal
             92    8  108   73  192   60  147  208
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-09-02T16:39:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x44 0x00    ..(.(.D.
    decimal
              1    0   40    0   40    0   68    0
    datetime (2013-09-02T16:39:08)
    0000   0x88 0x67 0x50 0x02 0x0d                   .gP..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 26 CalBGForPH 2013-09-02T18:34:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 331}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-09-02T18:34:17)
    0000   0x91 0x62 0x32 0x02 0x8d                   .b2..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 27 BolusWizard 2013-09-02T18:34:20 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 331,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 14.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-09-02T18:34:20)
    0000   0x94 0x62 0x12 0x02 0x0d                   .b...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x8c 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0x0c 0x00 0x80 0x78         ......x
    decimal
              0   81    0  100   60  100  140    0
              0    0    0   12    0  128  120
    HOUR BITS: [0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 118, 'amount': 1.0, 'curve': 192},
 {'age': 188, 'amount': 2.7, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x76 0xc0 0x6c 0xbc 0xc0    \.(v.l..
    decimal
             92    8   40  118  192  108  188  192
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-09-02T18:34:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x80 0x00 0x80 0x00 0x0c 0x00    ........
    decimal
              1    0  128    0  128    0   12    0
    datetime (2013-09-02T18:34:20)
    0000   0x94 0x62 0x52 0x02 0x0d                   .bR..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 30 CalBGForPH 2013-09-02T22:39:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 241}
```
    op hex (2)
    0000   0x0a 0xf1                                  ..
    decimal
             10  241
    datetime (2013-09-02T22:39:08)
    0000   0x88 0x67 0x36 0x02 0x0d                   .g6..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2013-09-02T22:39:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 241,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf1                                  [.
    decimal
             91  241
    datetime (2013-09-02T22:39:11)
    0000   0x8b 0x67 0x16 0x02 0x0d                   .g...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x50 0x00    .P.d<dP.
    0008   0x00 0x00 0x00 0x00 0x00 0x50 0x78         .....Px
    decimal
              0   80    0  100   60  100   80    0
              0    0    0    0    0   80  120
    HOUR BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 243, 'amount': 0.75, 'curve': 192},
 {'age': 253, 'amount': 2.45, 'curve': 192},
 {'age': 107, 'amount': 1.0, 'curve': 208},
 {'age': 177, 'amount': 2.7, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x1e 0xf3 0xc0 0x62 0xfd 0xc0    \....b..
    0008   0x28 0x6b 0xd0 0x6c 0xb1 0xd0              (k.l..
    decimal
             92   14   30  243  192   98  253  192
             40  107  208  108  177  208
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-09-02T22:39:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-09-02T22:39:11)
    0000   0x8b 0x67 0x56 0x02 0x0d                   .gV..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 34 BasalProfileStart 2013-09-03T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-03T00:00:00)
    0000   0x80 0x40 0x00 0x03 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 35 ResultTotals (2000, 10, 0, 0, 13, 2) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x78                   ....x
    decimal
              7    0    0    4  120
    datetime ((2000, 10, 0, 0, 13, 2))
    0000   0x82 0x8d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x82 0x8d 0x05 0x00 0xd5 0x00 0x00    n.......
    0008   0x05 0x00 0x00 0x04 0x78 0x02 0xd8 0x40    ....x..@
    0010   0x01 0xa0 0x24 0x00 0x2e 0x00 0x6c 0x01    ..$...l.
    0018   0x34 0x00 0x00 0x00 0x00 0x03 0x03 0x00    4.......
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x6b 0x4b 0x00 0x00 0x00 0x00    ..kK....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  130  141    5    0  213    0    0
              5    0    0    4  120    2  216   64
              1  160   36    0   46    0  108    1
             52    0    0    0    0    3    3    0
              0    4    0    0    0    0    0    0
              0    0  107   75    0    0    0    0
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 36 Base (2003, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2003, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x40 0x04 0x03                   ..@..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 37 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 38 Base (2000, 0, 2, 16, 13, 3) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x08                                  @.
    decimal
             64    8
    datetime ((2000, 0, 2, 16, 13, 3))
    0000   0x03 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 39 CalBGForPH 2013-09-03T08:08:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2013-09-03T08:08:00)
    0000   0x80 0x48 0x28 0x03 0x0d                   .H(..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 40 BolusWizard 2013-09-03T08:08:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 101,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
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
    0000   0x5b 0x65                                  [e
    decimal
             91  101
    datetime (2013-09-03T08:08:07)
    0000   0x87 0x48 0x08 0x03 0x0d                   .H...
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x78         4....4x
    decimal
             16   80    0  120   60  100    0    0
             52    0    0    0    0   52  120
    HOUR BITS: [0, 1, 0]
#### RECORD 41 Bolus 2013-09-03T08:08:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    0    0
    datetime (2013-09-03T08:08:07)
    0000   0x87 0x48 0x48 0x03 0x0d                   .HH..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 42 CalBGForPH 2013-09-03T10:59:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 297}
```
    op hex (2)
    0000   0x0a 0x29                                  .)
    decimal
             10   41
    datetime (2013-09-03T10:59:13)
    0000   0x8d 0x7b 0x2a 0x03 0x8d                   .{*..
    body (0)
    HOUR BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 43 BolusWizard 2013-09-03T10:59:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 297,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.4,
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
    0000   0x5b 0x29                                  [)
    decimal
             91   41
    datetime (2013-09-03T10:59:15)
    0000   0x8f 0x7b 0x0a 0x03 0x0d                   .{...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x78 0x3c 0x64 0x74 0x00    .Q.x<dt.
    0008   0x00 0x00 0x00 0x04 0x00 0x70 0x78         .....px
    decimal
              0   81    0  120   60  100  116    0
              0    0    0    4    0  112  120
    HOUR BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 173, 'amount': 1.3, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x34 0xad 0xc0                   \.4..
    decimal
             92    5   52  173  192
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-09-03T10:59:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x04 0x00    ..p.p...
    decimal
              1    0  112    0  112    0    4    0
    datetime (2013-09-03T10:59:15)
    0000   0x8f 0x7b 0x4a 0x03 0x0d                   .{J..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 46 BasalProfileStart 2013-09-03T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-03T12:00:00)
    0000   0x80 0x40 0x0c 0x03 0x0d                   .@...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 47 CalBGForPH 2013-09-03T14:26:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-09-03T14:26:39)
    0000   0xa7 0x5a 0x2e 0x03 0x0d                   .Z...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 48 BolusWizard 2013-09-03T14:26:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-09-03T14:26:50)
    0000   0xb2 0x5a 0x0e 0x03 0x0d                   .Z...
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x78         0....0x
    decimal
             15   80    0  120   60  100    0    0
             48    0    0    0    0   48  120
    HOUR BITS: [0, 1, 0]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 210, 'amount': 2.8, 'curve': 192},
 {'age': 124, 'amount': 1.3, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x70 0xd2 0xc0 0x34 0x7c 0xd0    \.p..4|.
    decimal
             92    8  112  210  192   52  124  208
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2013-09-03T14:26:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-09-03T14:26:50)
    0000   0xb2 0x5a 0x4e 0x03 0x0d                   .ZN..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 51 BolusWizard 2013-09-03T14:32:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.8,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-09-03T14:32:31)
    0000   0x9f 0x60 0x0e 0x03 0x0d                   .`...
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x20 0x00 0x00 0x30 0x00 0x20 0x78          ..0. x
    decimal
             10   80    0  120   60  100    0    0
             32    0    0   48    0   32  120
    HOUR BITS: [0, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 1.2, 'curve': 192},
 {'age': 216, 'amount': 2.8, 'curve': 192},
 {'age': 130, 'amount': 1.3, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x30 0x06 0xc0 0x70 0xd8 0xc0    \.0..p..
    0008   0x34 0x82 0xd0                             4..
    decimal
             92   11   48    6  192  112  216  192
             52  130  208
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-09-03T14:32:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x30 0x00    .. . .0.
    decimal
              1    0   32    0   32    0   48    0
    datetime (2013-09-03T14:32:31)
    0000   0x9f 0x60 0x4e 0x03 0x0d                   .`N..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 54 CalBGForPH 2013-09-03T16:54:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-09-03T16:54:49)
    0000   0xb1 0x76 0x30 0x03 0x0d                   .v0..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 55 BolusWizard 2013-09-03T16:54:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
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
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-09-03T16:54:58)
    0000   0xba 0x76 0x10 0x03 0x0d                   .v...
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x0c 0x00 0x28 0x78         (....(x
    decimal
             13   80    0  120   60  100    0    0
             40    0    0   12    0   40  120
    HOUR BITS: [0, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 148, 'amount': 2.0, 'curve': 192},
 {'age': 102, 'amount': 2.8, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0x94 0xc0 0x70 0x66 0xd0    \.P..pf.
    decimal
             92    8   80  148  192  112  102  208
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2013-09-03T16:54:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x0c 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   12    0
    datetime (2013-09-03T16:54:58)
    0000   0xba 0x76 0x50 0x03 0x0d                   .vP..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 58 BasalProfileStart 2013-09-04T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-09-04T00:00:00)
    0000   0x80 0x40 0x00 0x04 0x0d                   .@...
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 59 ResultTotals (2000, 10, 0, 0, 13, 3) head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xf8                   .....
    decimal
              7    0    0    3  248
    datetime ((2000, 10, 0, 0, 13, 3))
    0000   0x83 0x8d 0x00 0x00 0x00                   .....
    body (51)
    hex
    0000   0x6e 0x83 0x8d 0x05 0x00 0x9c 0x00 0x00    n.......
    0008   0x04 0x00 0x00 0x03 0xf8 0x02 0xdc 0x48    .......H
    0010   0x01 0x1c 0x1c 0x00 0x36 0x00 0xac 0x00    ....6...
    0018   0x70 0x00 0x00 0x00 0x00 0x04 0x01 0x00    p.......
    0020   0x00 0x04 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x65 0x29 0x00 0x00 0x00 0x00    ..e)....
    0030   0x00 0x00 0x00                             ...
    decimal
            110  131  141    5    0  156    0    0
              4    0    0    3  248    2  220   72
              1   28   28    0   54    0  172    0
            112    0    0    0    0    4    1    0
              0    4    0    0    0    0    0    0
              0    0  101   41    0    0    0    0
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 60 Base (2004, 2, 4, 0, 0, 1) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x7b                                  .{
    decimal
              0  123
    datetime ((2004, 2, 4, 0, 0, 1))
    0000   0x01 0x80 0x40 0x04 0x04                   ..@..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 61 Base (2000, 0, 2, 27, 0, 33) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x08                                  ..
    decimal
             13    8
    datetime ((2000, 0, 2, 27, 0, 33))
    0000   0x21 0x00 0x7b 0x02 0x80                   !.{..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 Base (2000, 0, 2, 16, 13, 4) head[2], body[0] op[0x40]

    op hex (2)
    0000   0x40 0x08                                  @.
    decimal
             64    8
    datetime ((2000, 0, 2, 16, 13, 4))
    0000   0x04 0x0d 0x10 0x22 0x00                   ...".
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 63 CalBGForPH 2013-09-04T08:50:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-09-04T08:50:11)
    0000   0x8b 0x72 0x28 0x04 0x0d                   .r(..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 64 BolusWizard 2013-09-04T08:50:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 19,
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
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-09-04T08:50:16)
    0000   0x90 0x72 0x08 0x04 0x0d                   .r...
    body (15)
    hex
    0000   0x13 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x3c 0x00 0x00 0x00 0x00 0x3c 0x78         <....<x
    decimal
             19   80    0  120   60  100    0    0
             60    0    0    0    0   60  120
    HOUR BITS: [0, 1, 1]
#### RECORD 65 Bolus 2013-09-04T08:50:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2013-09-04T08:50:16)
    0000   0x90 0x72 0x48 0x04 0x0d                   .rH..
    body (0)
    HOUR BITS: [0, 1, 1]
#### RECORD 66 BasalProfileStart 2013-09-04T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-09-04T12:00:00)
    0000   0x80 0x40 0x0c 0x04 0x0d                   .@...
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [0, 1, 0]
#### RECORD 67 CalBGForPH 2013-09-04T12:21:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 147}
```
    op hex (2)
    0000   0x0a 0x93                                  ..
    decimal
             10  147
    datetime (2013-09-04T12:21:16)
    0000   0x90 0x55 0x2c 0x04 0x0d                   .U,..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 68 BolusWizard 2013-09-04T12:21:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 147,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 16,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 1.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0x93                                  [.
    decimal
             91  147
    datetime (2013-09-04T12:21:23)
    0000   0x97 0x55 0x0c 0x04 0x0d                   .U...
    body (15)
    hex
    0000   0x10 0x50 0x00 0x78 0x3c 0x64 0x10 0x00    .P.x<d..
    0008   0x34 0x00 0x00 0x00 0x00 0x44 0x78         4....Dx
    decimal
             16   80    0  120   60  100   16    0
             52    0    0    0    0   68  120
    HOUR BITS: [0, 1, 0]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 215, 'amount': 1.5, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0xd7 0xc0                   \.<..
    decimal
             92    5   60  215  192
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-09-04T12:21:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x00 0x00    ..D.D...
    decimal
              1    0   68    0   68    0    0    0
    datetime (2013-09-04T12:21:23)
    0000   0x97 0x55 0x4c 0x04 0x0d                   .UL..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 71 CalBGForPH 2013-09-04T13:30:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 144}
```
    op hex (2)
    0000   0x0a 0x90                                  ..
    decimal
             10  144
    datetime (2013-09-04T13:30:36)
    0000   0xa4 0x5e 0x2d 0x04 0x0d                   .^-..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 72 BolusWizard 2013-09-04T13:30:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 144,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 1.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x90                                  [.
    decimal
             91  144
    datetime (2013-09-04T13:30:41)
    0000   0xa9 0x5e 0x0d 0x04 0x0d                   .^...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x10 0x00    .P.x<d..
    0008   0x00 0x00 0x00 0x28 0x00 0x00 0x78         ...(..x
    decimal
              0   80    0  120   60  100   16    0
              0    0    0   40    0    0  120
    HOUR BITS: [0, 1, 0]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 74, 'amount': 1.7, 'curve': 192},
 {'age': 28, 'amount': 1.5, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x4a 0xc0 0x3c 0x1c 0xd0    \.DJ.<..
    decimal
             92    8   68   74  192   60   28  208
    datetime (unknown)

    body (0)

#### RECORD 74 CalBGForPH 2013-09-04T14:17:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-09-04T14:17:27)
    0000   0x9b 0x51 0x2e 0x04 0x0d                   .Q...
    body (0)
    HOUR BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-1.data: 75 records`
