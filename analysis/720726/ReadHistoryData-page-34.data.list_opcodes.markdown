## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 1014, found 8 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa0 0x94                                  ..
##### DEBUG DECIMAL
            160  148
#### RECORD 0 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 70, 'amount': 4.9, 'curve': 4},
 {'age': 220, 'amount': 0.95, 'curve': 4},
 {'age': 230, 'amount': 1.75, 'curve': 4},
 {'age': 74, 'amount': 2.2, 'curve': 20},
 {'age': 194, 'amount': 1.8, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0xc4 0x46 0x04 0x26 0xdc 0x04    \..F.&..
    0008   0x46 0xe6 0x04 0x58 0x4a 0x14 0x48 0xc2    F..XJ.H.
    0010   0x14                                       .
    decimal
             92   17  196   70    4   38  220    4
             70  230    4   88   74   20   72  194
             20
    datetime (unknown)

    body (0)

#### RECORD 1 Ian69 2013-07-26T17:55:32 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-26T17:55:32)
    0000   0x60 0xf7 0x71 0x1a 0x0d                   `.q..
    body (2)
    hex
    0000   0x15 0x1e                                  ..
    decimal
             21   30
    HOUR BITS: [1, 1, 1]
#### RECORD 2 Bolus 2013-07-26T17:55:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xa0 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  160    0
    datetime (2013-07-26T17:55:32)
    0000   0x60 0xf7 0x51 0x7a 0x0d                   `.Qz.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 BolusWizard 2013-07-26T19:29:02 head[2], body[15] op[0x5b]
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
    datetime (2013-07-26T19:29:02)
    0000   0x42 0xdd 0x13 0x7a 0x0d                   B..z.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 2.0, 'curve': 4},
 {'age': 164, 'amount': 4.9, 'curve': 4},
 {'age': 58, 'amount': 0.95, 'curve': 20},
 {'age': 68, 'amount': 1.75, 'curve': 20},
 {'age': 168, 'amount': 2.2, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x5e 0x04 0xc4 0xa4 0x04    \.P^....
    0008   0x26 0x3a 0x14 0x46 0x44 0x14 0x58 0xa8    &:.FD.X.
    0010   0x14                                       .
    decimal
             92   17   80   94    4  196  164    4
             38   58   20   70   68   20   88  168
             20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-07-26T19:29:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x60 0x00    ..H.H.`.
    decimal
              1    0   72    0   72    0   96    0
    datetime (2013-07-26T19:29:03)
    0000   0x43 0xdd 0x53 0x7a 0x0d                   C.Sz.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 BolusWizard 2013-07-26T20:21:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 23,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-26T20:21:19)
    0000   0x53 0xd5 0x14 0x7a 0x0d                   S..z.
    body (15)
    hex
    0000   0x17 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             23  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 1.8, 'curve': 4},
 {'age': 146, 'amount': 2.0, 'curve': 4},
 {'age': 216, 'amount': 4.9, 'curve': 4},
 {'age': 110, 'amount': 0.95, 'curve': 20},
 {'age': 120, 'amount': 1.75, 'curve': 20},
 {'age': 220, 'amount': 2.2, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x38 0x04 0x50 0x92 0x04    \.H8.P..
    0008   0xc4 0xd8 0x04 0x26 0x6e 0x14 0x46 0x78    ...&n.Fx
    0010   0x14 0x58 0xdc 0x14                        .X..
    decimal
             92   20   72   56    4   80  146    4
            196  216    4   38  110   20   70  120
             20   88  220   20
    datetime (unknown)

    body (0)

#### RECORD 8 CalBGForPH 2013-07-26T20:21:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2013-07-26T20:21:45)
    0000   0x6d 0xd5 0x34 0x7a 0x0d                   m.4z.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 Ian3F 2013-07-26T20:21:45 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2013-07-26T20:21:45)
    0000   0x6d 0xd5 0x54 0x7a 0x0d                   m.Tz.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 Bolus 2013-07-26T20:21:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x68 0x00    ..P.P.h.
    decimal
              1    0   80    0   80    0  104    0
    datetime (2013-07-26T20:21:20)
    0000   0x54 0xd5 0x54 0x7a 0x0d                   T.Tz.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 11 CalBGForPH 2013-07-26T22:06:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-07-26T22:06:08)
    0000   0x48 0xc6 0x36 0x7a 0x0d                   H.6z.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2013-07-26T22:06:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2013-07-26T22:06:08)
    0000   0x48 0xc6 0xd6 0x7a 0x0d                   H..z.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 BolusWizard 2013-07-26T22:06:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 105,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.0,
 'carb_input': 41,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 8.8,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 148}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-07-26T22:06:29)
    0000   0x5d 0xc6 0x16 0x7a 0x0d                   ]..z.
    body (15)
    hex
    0000   0x29 0x90 0x00 0x6e 0x17 0x36 0x58 0x00    )..n.6X.
    0008   0x94 0x00 0x00 0x3c 0x00 0xb0 0x36         ...<..6
    decimal
             41  144    0  110   23   54   88    0
            148    0    0   60    0  176   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 111, 'amount': 2.0, 'curve': 4},
 {'age': 161, 'amount': 1.8, 'curve': 4},
 {'age': 251, 'amount': 2.0, 'curve': 4},
 {'age': 65, 'amount': 4.9, 'curve': 20},
 {'age': 215, 'amount': 0.95, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x6f 0x04 0x48 0xa1 0x04    \.Po.H..
    0008   0x50 0xfb 0x04 0xc4 0x41 0x14 0x26 0xd7    P...A.&.
    0010   0x14                                       .
    decimal
             92   17   80  111    4   72  161    4
             80  251    4  196   65   20   38  215
             20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-07-26T22:06:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 17.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xb0 0x00 0xb0 0x00 0x3c 0x00    ......<.
    decimal
              1    0  176    0  176    0   60    0
    datetime (2013-07-26T22:06:29)
    0000   0x5d 0xc6 0x56 0x7a 0x0d                   ].Vz.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2013-07-26T23:40:53 head[2], body[15] op[0x5b]
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
    datetime (2013-07-26T23:40:53)
    0000   0x75 0xe8 0x17 0x7a 0x0d                   u..z.
    body (15)
    hex
    0000   0x1e 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x36         l....l6
    decimal
             30  144    0  110   23   54    0    0
            108    0    0    0    0  108   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 95, 'amount': 4.4, 'curve': 4},
 {'age': 205, 'amount': 2.0, 'curve': 4},
 {'age': 255, 'amount': 1.8, 'curve': 4},
 {'age': 89, 'amount': 2.0, 'curve': 20},
 {'age': 159, 'amount': 4.9, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0xb0 0x5f 0x04 0x50 0xcd 0x04    \.._.P..
    0008   0x48 0xff 0x04 0x50 0x59 0x14 0xc4 0x9f    H..PY...
    0010   0x14                                       .
    decimal
             92   17  176   95    4   80  205    4
             72  255    4   80   89   20  196  159
             20
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-07-26T23:40:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x78 0x00    ......x.
    decimal
              1    0  132    0  132    0  120    0
    datetime (2013-07-26T23:40:54)
    0000   0x76 0xe8 0x57 0x7a 0x0d                   v.Wz.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 BasalProfileStart 2013-07-27T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-27T00:00:00)
    0000   0x40 0xc0 0x00 0x1b 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 20 ResultTotals (2000, 6, 0, 0, 13, 58) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xea                   .....
    decimal
              7    0    0    7  234
    datetime ((2000, 6, 0, 0, 13, 58))
    0000   0x7a 0x8d 0x00 0x00 0x00                   z....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x7a 0x8d 0x06 0x00 0xa2 0x47 0xf3    nz....G.
    0008   0x06 0x00 0x00 0x07 0xea 0x03 0x72 0x2c    ......r,
    0010   0x04 0x78 0x38 0x01 0x0c 0x02 0x28 0x00    .x8...(.
    0018   0x00 0x02 0x50 0x00 0x00 0x07 0x00 0x04    ..P.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00         .......
    decimal
            110  122  141    6    0  162   71  243
              6    0    0    7  234    3  114   44
              4  120   56    1   12    2   40    0
              0    2   80    0    0    7    0    4
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 22 CalBGForPH 2013-07-27T01:10:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-07-27T01:10:08)
    0000   0x48 0xca 0x21 0x7b 0x0d                   H.!{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 Ian3F 2013-07-27T01:10:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2013-07-27T01:10:08)
    0000   0x48 0xca 0x61 0x7b 0x0d                   H.a{.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 24 LowReservoir 2013-07-27T03:24:22 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 1.0}
```
    op hex (2)
    0000   0x34 0x0a                                  4.
    decimal
             52   10
    datetime (2013-07-27T03:24:22)
    0000   0x56 0xd8 0x03 0x1b 0x8d                   V....
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 BasalProfileStart 2013-07-27T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-27T04:00:00)
    0000   0x40 0xc0 0x04 0x1b 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x2e 0x00                             ...
    decimal
              8   46    0
    HOUR BITS: [1, 1, 0]
#### RECORD 26 CalBGForPH 2013-07-27T08:27:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2013-07-27T08:27:28)
    0000   0x5c 0xdb 0x28 0x7b 0x0d                   \.({.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 Ian3F 2013-07-27T08:27:28 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2013-07-27T08:27:28)
    0000   0x5c 0xdb 0x88 0x7b 0x0d                   \..{.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 BolusWizard 2013-07-27T08:27:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 8.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-07-27T08:27:35)
    0000   0x63 0xdb 0x08 0x7b 0x0d                   c..{.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x50 0x00    ...n.6P.
    0008   0x00 0x00 0x00 0x00 0x00 0x50 0x36         .....P6
    decimal
              0  144    0  110   23   54   80    0
              0    0    0    0    0   80   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 Ian69 2013-07-27T08:27:36 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x08                                  i.
    decimal
            105    8
    datetime (2013-07-27T08:27:36)
    0000   0x64 0xdb 0x08 0x1b 0x0d                   d....
    body (2)
    hex
    0000   0x0a 0x1e                                  ..
    decimal
             10   30
    HOUR BITS: [1, 1, 0]
#### RECORD 30 Bolus 2013-07-27T08:27:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-07-27T08:27:35)
    0000   0x63 0xdb 0x48 0x7b 0x0d                   c.H{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 BasalProfileStart 2013-07-27T09:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-27T09:30:00)
    0000   0x40 0xde 0x09 0x1b 0x0d                   @....
    body (3)
    hex
    0000   0x13 0x1e 0x00                             ...
    decimal
             19   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 32 LowReservoir 2013-07-27T09:52:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 0.1}
```
    op hex (2)
    0000   0x34 0x01                                  4.
    decimal
             52    1
    datetime (2013-07-27T09:52:00)
    0000   0x40 0xf4 0x09 0x1b 0x8d                   @....
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 33 BolusWizard 2013-07-27T10:00:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 76}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-27T10:00:37)
    0000   0x65 0xc0 0x0a 0x7b 0x0d                   e..{.
    body (15)
    hex
    0000   0x15 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x4c 0x00 0x00 0x00 0x00 0x4c 0x36         L....L6
    decimal
             21  144    0  110   23   54    0    0
             76    0    0    0    0   76   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 95, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x5f 0x04                   \.P_.
    decimal
             92    5   80   95    4
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-07-27T10:00:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x4c 0x00 0x4c 0x00 0x34 0x00    ..L.L.4.
    decimal
              1    0   76    0   76    0   52    0
    datetime (2013-07-27T10:00:37)
    0000   0x65 0xc0 0x4a 0x7b 0x0d                   e.J{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 BolusWizard 2013-07-27T11:42:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-27T11:42:59)
    0000   0x7b 0xea 0x0b 0x7b 0x0d                   {..{.
    body (15)
    hex
    0000   0x16 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x36         P....P6
    decimal
             22  144    0  110   23   54    0    0
             80    0    0    0    0   80   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 107, 'amount': 1.9, 'curve': 4},
 {'age': 197, 'amount': 2.0, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x6b 0x04 0x50 0xc5 0x04    \.Lk.P..
    decimal
             92    8   76  107    4   80  197    4
    datetime (unknown)

    body (0)

#### RECORD 38 Ian69 2013-07-27T11:42:59 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-07-27T11:42:59)
    0000   0x7b 0xea 0x0b 0x1b 0x0d                   {....
    body (2)
    hex
    0000   0x0e 0x1e                                  ..
    decimal
             14   30
    HOUR BITS: [1, 1, 1]
#### RECORD 39 Bolus 2013-07-27T11:42:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x34 0x00    ..P.P.4.
    decimal
              1    0   80    0   80    0   52    0
    datetime (2013-07-27T11:42:59)
    0000   0x7b 0xea 0x4b 0x7b 0x0d                   {.K{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 BolusWizard 2013-07-27T12:03:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-27T12:03:22)
    0000   0x56 0xc3 0x0c 0x7b 0x0d                   V..{.
    body (15)
    hex
    0000   0x19 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x36         X....X6
    decimal
             25  144    0  110   23   54    0    0
             88    0    0    0    0   88   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 2.0, 'curve': 4},
 {'age': 128, 'amount': 1.9, 'curve': 4},
 {'age': 218, 'amount': 2.0, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x1c 0x04 0x4c 0x80 0x04    \.P..L..
    0008   0x50 0xda 0x04                             P..
    decimal
             92   11   80   28    4   76  128    4
             80  218    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2013-07-27T12:03:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x74 0x00    ..l.l.t.
    decimal
              1    0  108    0  108    0  116    0
    datetime (2013-07-27T12:03:22)
    0000   0x56 0xc3 0x4c 0x7b 0x0d                   V.L{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 43 BolusWizard 2013-07-27T12:53:18 head[2], body[15] op[0x5b]
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
    datetime (2013-07-27T12:53:18)
    0000   0x52 0xf5 0x0c 0x7b 0x0d                   R..{.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 0.3, 'curve': 4},
 {'age': 58, 'amount': 2.4, 'curve': 4},
 {'age': 78, 'amount': 2.0, 'curve': 4},
 {'age': 178, 'amount': 1.9, 'curve': 4},
 {'age': 12, 'amount': 2.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x0c 0x30 0x04 0x60 0x3a 0x04    \..0.`:.
    0008   0x50 0x4e 0x04 0x4c 0xb2 0x04 0x50 0x0c    PN.L..P.
    0010   0x14                                       .
    decimal
             92   17   12   48    4   96   58    4
             80   78    4   76  178    4   80   12
             20
    datetime (unknown)

    body (0)

#### RECORD 45 PumpSuspend 2013-07-27T12:54:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-07-27T12:54:05)
    0000   0x45 0xf6 0x0c 0x1b 0x0d                   E....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 46 Bolus 2013-07-27T12:53:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x2e 0x00 0xa4 0x00    ..H.....
    decimal
              1    0   72    0   46    0  164    0
    datetime (2013-07-27T12:53:19)
    0000   0x53 0xf5 0x4c 0x7b 0x0d                   S.L{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 BasalProfileStart 2013-07-27T14:22:27 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-27T14:22:27)
    0000   0x5b 0xd6 0x0e 0x1b 0x0d                   [....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [1, 1, 0]
#### RECORD 48 PumpResume 2013-07-27T14:22:27 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-07-27T14:22:27)
    0000   0x5b 0xd6 0x0e 0x1b 0x0d                   [....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 CalBGForPH 2013-07-27T14:53:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-07-27T14:53:24)
    0000   0x58 0xf5 0x2e 0x7b 0x0d                   X..{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 Ian3F 2013-07-27T14:53:24 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2013-07-27T14:53:24)
    0000   0x58 0xf5 0xae 0x7b 0x0d                   X..{.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 Rewind 2013-07-27T14:53:46 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-27T14:53:46)
    0000   0x6e 0xf5 0x0e 0x1b 0x0d                   n....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 52 Prime 2013-07-27T14:54:41 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x13                   .....
    decimal
              3    0    0    0   19
    datetime (2013-07-27T14:54:41)
    0000   0x69 0xf6 0x2e 0x1b 0x0d                   i....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 53 BasalProfileStart 2013-07-27T14:54:52 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-27T14:54:52)
    0000   0x74 0xf6 0x0e 0x1b 0x0d                   t....
    body (3)
    hex
    0000   0x1a 0x26 0x00                             .&.
    decimal
             26   38    0
    HOUR BITS: [1, 1, 1]
#### RECORD 54 BolusWizard 2013-07-27T16:23:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 38,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 136}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-27T16:23:58)
    0000   0x7a 0xd7 0x10 0x7b 0x0d                   z..{.
    body (15)
    hex
    0000   0x26 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    &..n.6..
    0008   0x88 0x00 0x00 0x00 0x00 0x88 0x36         ......6
    decimal
             38  144    0  110   23   54    0    0
            136    0    0    0    0  136   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 218, 'amount': 1.15, 'curve': 4},
 {'age': 2, 'amount': 0.3, 'curve': 20},
 {'age': 12, 'amount': 2.4, 'curve': 20},
 {'age': 32, 'amount': 2.0, 'curve': 20},
 {'age': 132, 'amount': 1.9, 'curve': 20},
 {'age': 222, 'amount': 2.0, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x2e 0xda 0x04 0x0c 0x02 0x14    \.......
    0008   0x60 0x0c 0x14 0x50 0x20 0x14 0x4c 0x84    `..P .L.
    0010   0x14 0x50 0xde 0x14                        .P..
    decimal
             92   20   46  218    4   12    2   20
             96   12   20   80   32   20   76  132
             20   80  222   20
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-07-27T16:23:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x04 0x00    ........
    decimal
              1    0  136    0  136    0    4    0
    datetime (2013-07-27T16:23:59)
    0000   0x7b 0xd7 0x50 0x7b 0x0d                   {.P{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2013-07-27T16:36:38 head[2], body[15] op[0x5b]
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
    datetime (2013-07-27T16:36:38)
    0000   0x66 0xe4 0x10 0x7b 0x0d                   f..{.
    body (15)
    hex
    0000   0x14 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x36         H....H6
    decimal
             20  144    0  110   23   54    0    0
             72    0    0    0    0   72   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 1.85, 'curve': 4},
 {'age': 21, 'amount': 1.55, 'curve': 4},
 {'age': 231, 'amount': 1.15, 'curve': 4},
 {'age': 15, 'amount': 0.3, 'curve': 20},
 {'age': 25, 'amount': 2.4, 'curve': 20},
 {'age': 45, 'amount': 2.0, 'curve': 20},
 {'age': 145, 'amount': 1.9, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x4a 0x0b 0x04 0x3e 0x15 0x04    \.J..>..
    0008   0x2e 0xe7 0x04 0x0c 0x0f 0x14 0x60 0x19    ......`.
    0010   0x14 0x50 0x2d 0x14 0x4c 0x91 0x14         .P-.L..
    decimal
             92   23   74   11    4   62   21    4
             46  231    4   12   15   20   96   25
             20   80   45   20   76  145   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-07-27T16:36:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x8c 0x00    ..H.H...
    decimal
              1    0   72    0   72    0  140    0
    datetime (2013-07-27T16:36:38)
    0000   0x66 0xe4 0x50 0x7b 0x0d                   f.P{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 Ian69 2013-07-27T21:30:00 head[2], body[2] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-27T21:30:00)
    0000   0x40 0xde 0x75 0x1b 0x0d                   @.u..
    body (2)
    hex
    0000   0x35 0x1e                                  5.
    decimal
             53   30
    HOUR BITS: [1, 1, 0]
#### RECORD 61 BolusWizard 2013-07-27T21:30:25 head[2], body[15] op[0x5b]
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
    datetime (2013-07-27T21:30:25)
    0000   0x59 0xde 0x15 0x7b 0x0d                   Y..{.
    body (15)
    hex
    0000   0x25 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    %..n.6..
    0008   0x84 0x00 0x00 0x00 0x00 0x84 0x36         ......6
    decimal
             37  144    0  110   23   54    0    0
            132    0    0    0    0  132   54
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 1.8, 'curve': 20},
 {'age': 49, 'amount': 1.85, 'curve': 20},
 {'age': 59, 'amount': 1.55, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x27 0x14 0x4a 0x31 0x14    \.H'.J1.
    0008   0x3e 0x3b 0x14                             >;.
    decimal
             92   11   72   39   20   74   49   20
             62   59   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2013-07-27T21:30:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x00 0x00    ........
    decimal
              1    0  132    0  132    0    0    0
    datetime (2013-07-27T21:30:26)
    0000   0x5a 0xde 0x55 0x7b 0x0d                   Z.U{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 64 BolusWizard 2013-07-27T21:34:42 head[2], body[15] op[0x5b]
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
    datetime (2013-07-27T21:34:42)
    0000   0x6a 0xe2 0x15 0x7b 0x0d                   j..{.
    body (15)
    hex
    0000   0x0a 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x36         $....$6
    decimal
             10  144    0  110   23   54    0    0
             36    0    0    0    0   36   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 3.3, 'curve': 4},
 {'age': 43, 'amount': 1.8, 'curve': 20},
 {'age': 53, 'amount': 1.85, 'curve': 20},
 {'age': 63, 'amount': 1.55, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x84 0x09 0x04 0x48 0x2b 0x14    \....H+.
    0008   0x4a 0x35 0x14 0x3e 0x3f 0x14              J5.>?.
    decimal
             92   14  132    9    4   72   43   20
             74   53   20   62   63   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-07-27T21:34:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x84 0x00    ..$.$...
    decimal
              1    0   36    0   36    0  132    0
    datetime (2013-07-27T21:34:42)
    0000   0x6a 0xe2 0x55 0x7b 0x0d                   j.U{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 BolusWizard 2013-07-27T21:46:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 104}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-07-27T21:46:33)
    0000   0x61 0xee 0x15 0x7b 0x0d                   a..{.
    body (15)
    hex
    0000   0x1d 0x90 0x00 0x6e 0x17 0x36 0x00 0x00    ...n.6..
    0008   0x68 0x00 0x00 0x00 0x00 0x68 0x36         h....h6
    decimal
             29  144    0  110   23   54    0    0
            104    0    0    0    0  104   54
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 11, 'amount': 0.7, 'curve': 4},
 {'age': 21, 'amount': 3.5, 'curve': 4},
 {'age': 55, 'amount': 1.8, 'curve': 20},
 {'age': 65, 'amount': 1.85, 'curve': 20},
 {'age': 75, 'amount': 1.55, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x1c 0x0b 0x04 0x8c 0x15 0x04    \.......
    0008   0x48 0x37 0x14 0x4a 0x41 0x14 0x3e 0x4b    H7.JA.>K
    0010   0x14                                       .
    decimal
             92   17   28   11    4  140   21    4
             72   55   20   74   65   20   62   75
             20
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-07-27T21:46:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xa8 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  168    0
    datetime (2013-07-27T21:46:33)
    0000   0x61 0xee 0x55 0x7b 0x0d                   a.U{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 CalBGForPH 2013-07-27T22:29:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 248}
```
    op hex (2)
    0000   0x0a 0xf8                                  ..
    decimal
             10  248
    datetime (2013-07-27T22:29:40)
    0000   0x68 0xdd 0x36 0x7b 0x0d                   h.6{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 71 Ian3F 2013-07-27T22:29:40 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1f                                  ?.
    decimal
             63   31
    datetime (2013-07-27T22:29:40)
    0000   0x68 0xdd 0x16 0x7b 0x0d                   h..{.
    body (3)
    hex
    0000   0x69 0x69 0x96                             ii.
    decimal
            105  105  150
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-34.data: 72 records`
