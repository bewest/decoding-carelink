## START logs/ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 863, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x84 0x00 0x00 0x00 0x00 0x84 0x36 0x5c    ......6\
    0008   0x0b 0x48 0x27 0x14 0x4a 0x31 0x14 0x3e    .H'.J1.>
    0010   0x3b 0x14 0x01 0x00 0x84 0x00 0x84 0x00    ;.......
    0018   0x00 0x00 0x5a 0xde 0x55 0x7b 0x0d 0x5b    ..Z.U{.[
##### DEBUG DECIMAL
            132    0    0    0    0  132   54   92
             11   72   39   20   74   49   20   62
             59   20    1    0  132    0  132    0
              0    0   90  222   85  123   13   91
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

#### RECORD 1 Ian69 2013-07-26T17:55:32 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-26T17:55:32)
    0000   0x60 0xf7 0x71 0x1a 0x0d                   `.q..
    body (8)
    hex
    0000   0x15 0x1e 0x01 0x00 0x50 0x00 0x50 0x00    ....P.P.
    decimal
             21   30    1    0   80    0   80    0
    HOUR BITS: [1, 1, 1]
#### RECORD 2 Base (2013, 7, 26, 17, 55, 32) head[2], body[0] op[0xa0]

    op hex (2)
    0000   0xa0 0x00                                  ..
    decimal
            160    0
    datetime ((2013, 7, 26, 17, 55, 32))
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
#### RECORD 9 Base (2013, 7, 26, 20, 21, 45) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime ((2013, 7, 26, 20, 21, 45))
    0000   0x6d 0xd5 0x54 0x7a 0x0d                   m.Tz.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 Ian69 2000-08-16T00:01:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2000-08-16T00:01:22)
    0000   0x96 0x01 0x00 0x50 0x00                   ...P.
    body (8)
    hex
    0000   0x50 0x00 0x68 0x00 0x54 0xd5 0x54 0x7a    P.h.T.Tz
    decimal
             80    0  104    0   84  213   84  122
    DAY BITS: [0, 1, 0]
#### RECORD 11 Base (2010, 9, 22, 6, 8, 62) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x0a                                  ..
    decimal
             13   10
    datetime ((2010, 9, 22, 6, 8, 62))
    0000   0xbe 0x48 0xc6 0x36 0x7a                   .H.6z
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 12 Base (2010, 1, 22, 6, 8, 23) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x3f                                  .?
    decimal
             13   63
    datetime ((2010, 1, 22, 6, 8, 23))
    0000   0x17 0x48 0xc6 0xd6 0x7a                   .H..z
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [1, 1, 0] YEAR BITS: [0, 1, 1, 1]
#### RECORD 13 Base (2013, 6, 9, 27, 22, 41) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x69                                  .i
    decimal
             13  105
    datetime ((2013, 6, 9, 27, 22, 41))
    0000   0x69 0x96 0x5b 0x69 0x5d                   i.[i]
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 1, 0, 1]
#### RECORD 14 Base (2000, 4, 16, 9, 13, 58) head[2], body[0] op[0xc6]

    op hex (2)
    0000   0xc6 0x16                                  ..
    decimal
            198   22
    datetime ((2000, 4, 16, 9, 13, 58))
    0000   0x7a 0x0d 0x29 0x90 0x00                   z.)..
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 15 Sara6E (2000, 4, 16, 30, 13, 58) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x17 0x36 0x58 0x00 0x94 0x00 0x00    n.6X....
    0008   0x3c 0x00 0xb0 0x36 0x5c 0x11 0x50 0x6f    <..6\.Po
    0010   0x04 0x48 0xa1 0x04 0x50 0xfb 0x04 0xc4    .H..P...
    0018   0x41 0x14 0x26 0xd7 0x14 0x01 0x00 0xb0    A.&.....
    0020   0x00 0xb0 0x00 0x3c 0x00 0x5d 0xc6 0x56    ...<.].V
    0028   0x7a 0x0d 0x5b 0x00 0x75 0xe8 0x17         z.[.u..
    decimal
            110   23   54   88    0  148    0    0
             60    0  176   54   92   17   80  111
              4   72  161    4   80  251    4  196
             65   20   38  215   20    1    0  176
              0  176    0   60    0   93  198   86
            122   13   91    0  117  232   23
    datetime ((2000, 4, 16, 30, 13, 58))
    0000   0x7a 0x0d 0x1e 0x90 0x00                   z....
    body (0)
    DAY BITS: [1, 0, 0]
#### RECORD 16 Sara6E (2000, 0, 0, 0, 13, 27) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x17 0x36 0x00 0x00 0x6c 0x00 0x00    n.6..l..
    0008   0x00 0x00 0x6c 0x36 0x5c 0x11 0xb0 0x5f    ..l6\.._
    0010   0x04 0x50 0xcd 0x04 0x48 0xff 0x04 0x50    .P..H..P
    0018   0x59 0x14 0xc4 0x9f 0x14 0x01 0x00 0x84    Y.......
    0020   0x00 0x84 0x00 0x78 0x00 0x76 0xe8 0x57    ...x.v.W
    0028   0x7a 0x0d 0x7b 0x00 0x40 0xc0 0x00         z.{.@..
    decimal
            110   23   54    0    0  108    0    0
              0    0  108   54   92   17  176   95
              4   80  205    4   72  255    4   80
             89   20  196  159   20    1    0  132
              0  132    0  120    0  118  232   87
            122   13  123    0   64  192    0
    datetime ((2000, 0, 0, 0, 13, 27))
    0000   0x1b 0x0d 0x00 0x20 0x00                   ... .
    body (0)
    DAY BITS: [0, 0, 1]
#### RECORD 17 ResultTotals (2000, 6, 0, 0, 13, 58) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0xea                   .....
    decimal
              7    0    0    7  234
    datetime ((2000, 6, 0, 0, 13, 58))
    0000   0x7a 0x8d 0x00 0x00 0x00                   z....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 18 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

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

#### RECORD 19 CalBGForPH 2013-07-27T01:10:08 head[2], body[0] op[0x0a]
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
#### RECORD 20 Base (2013, 7, 27, 1, 10, 8) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime ((2013, 7, 27, 1, 10, 8))
    0000   0x48 0xca 0x61 0x7b 0x0d                   H.a{.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 Ian69 2008-08-22T10:52:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2008-08-22T10:52:22)
    0000   0x96 0x34 0x0a 0x56 0xd8                   .4.V.
    body (8)
    hex
    0000   0x03 0x1b 0x8d 0x7b 0x01 0x40 0xc0 0x04    ...{.@..
    decimal
              3   27  141  123    1   64  192    4
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 0] YEAR BITS: [1, 1, 0, 1]
#### RECORD 22 Base (2004, 0, 10, 0, 46, 8) head[2], body[0] op[0x1b]

    op hex (2)
    0000   0x1b 0x0d                                  ..
    decimal
             27   13
    datetime ((2004, 0, 10, 0, 46, 8))
    0000   0x08 0x2e 0x00 0x0a 0xb4                   .....
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[219], body[0] op[0x5c]
###### DECODED
```python
[{'age': 123, 'amount': 1.0, 'curve': 13},
 {'age': 22, 'amount': 1.575, 'curve': 92},
 {'age': 136, 'amount': 5.475, 'curve': 123},
 {'age': 105, 'amount': 0.325, 'curve': 105},
 {'age': 91, 'amount': 3.75, 'curve': 100},
 {'age': 219, 'amount': 2.475, 'curve': 8},
 {'age': 13, 'amount': 3.075, 'curve': 0},
 {'age': 0, 'amount': 3.6, 'curve': 110},
 {'age': 54, 'amount': 0.575, 'curve': 80},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 54, 'amount': 2.0, 'curve': 105},
 {'age': 100, 'amount': 0.2, 'curve': 219},
 {'age': 27, 'amount': 0.2, 'curve': 13},
 {'age': 30, 'amount': 0.25, 'curve': 1},
 {'age': 80, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 2.0, 'curve': 0},
 {'age': 99, 'amount': 0.0, 'curve': 219},
 {'age': 123, 'amount': 1.8, 'curve': 13},
 {'age': 2, 'amount': 3.075, 'curve': 64},
 {'age': 9, 'amount': 5.55, 'curve': 27},
 {'age': 19, 'amount': 0.325, 'curve': 30},
 {'age': 52, 'amount': 0.0, 'curve': 1},
 {'age': 244, 'amount': 1.6, 'curve': 9},
 {'age': 141, 'amount': 0.675, 'curve': 91},
 {'age': 101, 'amount': 0.0, 'curve': 192},
 {'age': 123, 'amount': 0.25, 'curve': 13},
 {'age': 144, 'amount': 0.525, 'curve': 0},
 {'age': 23, 'amount': 2.75, 'curve': 54},
 {'age': 0, 'amount': 0.0, 'curve': 76},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 76, 'amount': 0.0, 'curve': 54},
 {'age': 5, 'amount': 2.3, 'curve': 80},
 {'age': 4, 'amount': 2.375, 'curve': 1},
 {'age': 76, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 1.9, 'curve': 52},
 {'age': 101, 'amount': 0.0, 'curve': 192},
 {'age': 123, 'amount': 1.85, 'curve': 13},
 {'age': 0, 'amount': 2.275, 'curve': 123},
 {'age': 11, 'amount': 5.85, 'curve': 123},
 {'age': 22, 'amount': 0.325, 'curve': 144},
 {'age': 110, 'amount': 0.0, 'curve': 23},
 {'age': 0, 'amount': 1.35, 'curve': 0},
 {'age': 0, 'amount': 2.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 80},
 {'age': 92, 'amount': 1.35, 'curve': 8},
 {'age': 107, 'amount': 1.9, 'curve': 4},
 {'age': 197, 'amount': 2.0, 'curve': 4},
 {'age': 11, 'amount': 2.625, 'curve': 123},
 {'age': 11, 'amount': 5.85, 'curve': 27},
 {'age': 14, 'amount': 0.325, 'curve': 30},
 {'age': 0, 'amount': 0.025, 'curve': 80},
 {'age': 80, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 1.3, 'curve': 123},
 {'age': 75, 'amount': 5.85, 'curve': 123},
 {'age': 91, 'amount': 0.325, 'curve': 0},
 {'age': 195, 'amount': 2.15, 'curve': 12},
 {'age': 13, 'amount': 3.075, 'curve': 25},
 {'age': 0, 'amount': 3.6, 'curve': 110},
 {'age': 54, 'amount': 0.575, 'curve': 0},
 {'age': 88, 'amount': 0.0, 'curve': 0},
 {'age': 0, 'amount': 0.0, 'curve': 0},
 {'age': 54, 'amount': 2.2, 'curve': 92},
 {'age': 80, 'amount': 0.275, 'curve': 28},
 {'age': 76, 'amount': 0.1, 'curve': 128},
 {'age': 80, 'amount': 0.1, 'curve': 218},
 {'age': 1, 'amount': 0.1, 'curve': 0},
 {'age': 0, 'amount': 2.7, 'curve': 108},
 {'age': 116, 'amount': 0.0, 'curve': 0},
 {'age': 195, 'amount': 2.15, 'curve': 76},
 {'age': 13, 'amount': 3.075, 'curve': 91},
 {'age': 82, 'amount': 0.0, 'curve': 245}]
```
    op hex (219)
    0000   0x5c 0xdb 0x28 0x7b 0x0d 0x3f 0x16 0x5c    \.({.?.\
    0008   0xdb 0x88 0x7b 0x0d 0x69 0x69 0x96 0x5b    ..{.ii.[
    0010   0x64 0x63 0xdb 0x08 0x7b 0x0d 0x00 0x90    dc..{...
    0018   0x00 0x6e 0x17 0x36 0x50 0x00 0x00 0x00    .n.6P...
    0020   0x00 0x00 0x00 0x50 0x36 0x69 0x08 0x64    ...P6i.d
    0028   0xdb 0x08 0x1b 0x0d 0x0a 0x1e 0x01 0x00    ........
    0030   0x50 0x00 0x50 0x00 0x00 0x00 0x63 0xdb    P.P...c.
    0038   0x48 0x7b 0x0d 0x7b 0x02 0x40 0xde 0x09    H{.{.@..
    0040   0x1b 0x0d 0x13 0x1e 0x00 0x34 0x01 0x40    .....4.@
    0048   0xf4 0x09 0x1b 0x8d 0x5b 0x00 0x65 0xc0    ....[.e.
    0050   0x0a 0x7b 0x0d 0x15 0x90 0x00 0x6e 0x17    .{....n.
    0058   0x36 0x00 0x00 0x4c 0x00 0x00 0x00 0x00    6..L....
    0060   0x4c 0x36 0x5c 0x05 0x50 0x5f 0x04 0x01    L6\.P_..
    0068   0x00 0x4c 0x00 0x4c 0x00 0x34 0x00 0x65    .L.L.4.e
    0070   0xc0 0x4a 0x7b 0x0d 0x5b 0x00 0x7b 0xea    .J{.[.{.
    0078   0x0b 0x7b 0x0d 0x16 0x90 0x00 0x6e 0x17    .{....n.
    0080   0x36 0x00 0x00 0x50 0x00 0x00 0x00 0x00    6..P....
    0088   0x50 0x36 0x5c 0x08 0x4c 0x6b 0x04 0x50    P6\.Lk.P
    0090   0xc5 0x04 0x69 0x0b 0x7b 0xea 0x0b 0x1b    ..i.{...
    0098   0x0d 0x0e 0x1e 0x01 0x00 0x50 0x00 0x50    .....P.P
    00A0   0x00 0x34 0x00 0x7b 0xea 0x4b 0x7b 0x0d    .4.{.K{.
    00A8   0x5b 0x00 0x56 0xc3 0x0c 0x7b 0x0d 0x19    [.V..{..
    00B0   0x90 0x00 0x6e 0x17 0x36 0x00 0x00 0x58    ..n.6..X
    00B8   0x00 0x00 0x00 0x00 0x58 0x36 0x5c 0x0b    ....X6\.
    00C0   0x50 0x1c 0x04 0x4c 0x80 0x04 0x50 0xda    P..L..P.
    00C8   0x04 0x01 0x00 0x6c 0x00 0x6c 0x00 0x74    ...l.l.t
    00D0   0x00 0x56 0xc3 0x4c 0x7b 0x0d 0x5b 0x00    .V.L{.[.
    00D8   0x52 0xf5 0x0c                             R..
    decimal
             92  219   40  123   13   63   22   92
            219  136  123   13  105  105  150   91
            100   99  219    8  123   13    0  144
              0  110   23   54   80    0    0    0
              0    0    0   80   54  105    8  100
            219    8   27   13   10   30    1    0
             80    0   80    0    0    0   99  219
             72  123   13  123    2   64  222    9
             27   13   19   30    0   52    1   64
            244    9   27  141   91    0  101  192
             10  123   13   21  144    0  110   23
             54    0    0   76    0    0    0    0
             76   54   92    5   80   95    4    1
              0   76    0   76    0   52    0  101
            192   74  123   13   91    0  123  234
             11  123   13   22  144    0  110   23
             54    0    0   80    0    0    0    0
             80   54   92    8   76  107    4   80
            197    4  105   11  123  234   11   27
             13   14   30    1    0   80    0   80
              0   52    0  123  234   75  123   13
             91    0   86  195   12  123   13   25
            144    0  110   23   54    0    0   88
              0    0    0    0   88   54   92   11
             80   28    4   76  128    4   80  218
              4    1    0  108    0  108    0  116
              0   86  195   76  123   13   91    0
             82  245   12
    datetime (unknown)

    body (0)

#### RECORD 24 BasalProfileStart 2007-02-14T00:16:20 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x0d                                  {.
    decimal
            123   13
    datetime (2007-02-14T00:16:20)
    0000   0x14 0x90 0x00 0x6e 0x17                   ...n.
    body (3)
    hex
    0000   0x36 0x00 0x00                             6..
    decimal
             54    0    0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [0, 0, 0, 1]
#### RECORD 25 Base (2006, 0, 8, 0, 0, 0) head[2], body[0] op[0x48]

    op hex (2)
    0000   0x48 0x00                                  H.
    decimal
             72    0
    datetime ((2006, 0, 8, 0, 0, 0))
    0000   0x00 0x00 0x00 0x48 0x36                   ...H6
    body (0)
    DAY BITS: [0, 1, 0] YEAR BITS: [0, 0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
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

#### RECORD 27 PumpSuspend 2013-07-27T12:54:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2013-07-27T12:54:05)
    0000   0x45 0xf6 0x0c 0x1b 0x0d                   E....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 Bolus 2013-07-27T12:53:19 head[8], body[0] op[0x01]
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
#### RECORD 29 BasalProfileStart 2013-07-27T14:22:27 head[2], body[3] op[0x7b]

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
#### RECORD 30 PumpResume 2013-07-27T14:22:27 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2013-07-27T14:22:27)
    0000   0x5b 0xd6 0x0e 0x1b 0x0d                   [....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 31 CalBGForPH 2013-07-27T14:53:24 head[2], body[0] op[0x0a]
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
#### RECORD 32 Base (2013, 7, 27, 14, 53, 24) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime ((2013, 7, 27, 14, 53, 24))
    0000   0x58 0xf5 0xae 0x7b 0x0d                   X..{.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 33 Ian69 2005-08-14T00:33:22 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x69                                  ii
    decimal
            105  105
    datetime (2005-08-14T00:33:22)
    0000   0x96 0x21 0x00 0x6e 0xf5                   .!.n.
    body (8)
    hex
    0000   0x0e 0x1b 0x0d 0x03 0x00 0x00 0x00 0x13    ........
    decimal
             14   27   13    3    0    0    0   19
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 1, 1, 1]
#### RECORD 34 Ian69 (2003, 0, 27, 13, 27, 46) head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xf6                                  i.
    decimal
            105  246
    datetime ((2003, 0, 27, 13, 27, 46))
    0000   0x2e 0x1b 0x0d 0x7b 0x03                   ...{.
    body (8)
    hex
    0000   0x74 0xf6 0x0e 0x1b 0x0d 0x1a 0x26 0x00    t.....&.
    decimal
            116  246   14   27   13   26   38    0
    DAY BITS: [0, 1, 1]
#### RECORD 35 BolusWizard 2013-07-27T16:23:58 head[2], body[15] op[0x5b]
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
#### RECORD 36 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
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

#### RECORD 37 Bolus 2013-07-27T16:23:59 head[8], body[0] op[0x01]
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
#### RECORD 38 BolusWizard 2013-07-27T16:36:38 head[2], body[15] op[0x5b]
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
#### RECORD 39 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
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

#### RECORD 40 Bolus 2013-07-27T16:36:38 head[8], body[0] op[0x01]
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
#### RECORD 41 Ian69 2013-07-27T21:30:00 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0xd1                                  i.
    decimal
            105  209
    datetime (2013-07-27T21:30:00)
    0000   0x40 0xde 0x75 0x1b 0x0d                   @.u..
    body (8)
    hex
    0000   0x35 0x1e 0x5b 0x00 0x59 0xde 0x15 0x7b    5.[.Y..{
    decimal
             53   30   91    0   89  222   21  123
    HOUR BITS: [1, 1, 0]
#### RECORD 42 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x25                                  .%
    decimal
             13   37
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-34.data: 43 records`
