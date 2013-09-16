## START logs/ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 208, found 6 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x36 0x5c 0x0b 0x8c 0x3c 0x04 0x28 0x04    6\..<.(.
    0008   0x14 0x78 0x0e 0x14 0x5b 0x00 0xad 0x48    .x..[..H
    0010   0x0c 0x69 0x0d 0x00 0x90 0x00 0x6e 0x17    .i....n.
    0018   0x36 0x00 0x00 0x00 0x00 0x00 0x00 0x00    6.......
##### DEBUG DECIMAL
             54   92   11  140   60    4   40    4
             20  120   14   20   91    0  173   72
             12  105   13    0  144    0  110   23
             54    0    0    0    0    0    0    0
#### RECORD 0 Ian69 2013-09-09T11:10:57 head[2], body[8] op[0x69]

    op hex (2)
    0000   0x69 0x0b                                  i.
    decimal
            105   11
    datetime (2013-09-09T11:10:57)
    0000   0xb9 0x4a 0x0b 0x09 0x0d                   .J...
    body (8)
    hex
    0000   0x0e 0x1e 0x01 0x00 0x34 0x00 0x34 0x00    ....4.4.
    decimal
             14   30    1    0   52    0   52    0
    HOUR BITS: [0, 1, 0]
#### RECORD 1 Base (2013, 9, 9, 11, 10, 57) head[2], body[0] op[0x10]

    op hex (2)
    0000   0x10 0x00                                  ..
    decimal
             16    0
    datetime ((2013, 9, 9, 11, 10, 57))
    0000   0xb9 0x4a 0x4b 0x69 0x0d                   .JKi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 CalBGForPH 2013-09-09T11:15:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2013-09-09T11:15:34)
    0000   0xa2 0x4f 0x4b 0x09 0x0d                   .OK..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 3 BolusWizard 2013-09-09T11:15:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 88,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 6.8,
 'carb_input': 17,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 5.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 60}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2013-09-09T11:15:53)
    0000   0xb5 0x4f 0x0b 0x69 0x0d                   .O.i.
    body (15)
    hex
    0000   0x11 0x90 0x00 0x6e 0x17 0x36 0x38 0x00    ...n.68.
    0008   0x3c 0x00 0x00 0x44 0x00 0x3c 0x36         <..D.<6
    decimal
             17  144    0  110   23   54   56    0
             60    0    0   68    0   60   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 1.3, 'curve': 4},
 {'age': 207, 'amount': 1.0, 'curve': 4},
 {'age': 217, 'amount': 3.0, 'curve': 4},
 {'age': 181, 'amount': 2.7, 'curve': 21},
 {'age': 191, 'amount': 0.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x34 0x07 0x04 0x28 0xcf 0x04    \.4..(..
    0008   0x78 0xd9 0x04 0x6c 0xb5 0x15 0x0c 0xbf    x..l....
    0010   0x14                                       .
    decimal
             92   17   52    7    4   40  207    4
            120  217    4  108  181   21   12  191
             20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-09-09T11:15:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x44 0x00    ..X.X.D.
    decimal
              1    0   88    0   88    0   68    0
    datetime (2013-09-09T11:15:53)
    0000   0xb5 0x4f 0x4b 0x69 0x0d                   .OKi.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2013-09-09T11:29:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-09-09T11:29:28)
    0000   0x9c 0x5d 0x4b 0x09 0x0d                   .]K..
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 7 BolusWizard 2013-09-09T11:29:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 54,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 0,
 'bg_target_low': 23,
 'bolus_estimate': 14.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.6,
 'food_estimate': 9.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-09-09T11:29:35)
    0000   0xa3 0x5d 0x0b 0x69 0x0d                   .].i.
    body (15)
    hex
    0000   0x00 0x90 0x00 0x6e 0x17 0x36 0x5c 0x00    ...n.6\.
    0008   0x00 0x00 0x00 0x94 0x00 0x00 0x36         ......6
    decimal
              0  144    0  110   23   54   92    0
              0    0    0  148    0    0   54
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 21, 'amount': 3.5, 'curve': 4},
 {'age': 221, 'amount': 1.0, 'curve': 4},
 {'age': 231, 'amount': 3.0, 'curve': 4},
 {'age': 195, 'amount': 2.7, 'curve': 21},
 {'age': 205, 'amount': 0.3, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x8c 0x15 0x04 0x28 0xdd 0x04    \....(..
    0008   0x78 0xe7 0x04 0x6c 0xc3 0x15 0x0c 0xcd    x..l....
    0010   0x14                                       .
    decimal
             92   17  140   21    4   40  221    4
            120  231    4  108  195   21   12  205
             20
    datetime (unknown)

    body (0)

#### RECORD 9 Ian0B 2013-09-09T11:34:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2013-09-09T11:34:07)
    0000   0x87 0x62 0x4b 0xa9 0x0d                   .bK..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 10 Ian0B 2013-09-09T11:34:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2013-09-09T11:34:07)
    0000   0x87 0x62 0x4b 0xa9 0x0d                   .bK..
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [1, 0, 1]
#### RECORD 11 CalBGForPH 2013-09-09T11:36:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-09-09T11:36:03)
    0000   0x83 0x64 0x2b 0x69 0x0d                   .d+i.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Base (2013, 9, 9, 11, 36, 3) head[2], body[0] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime ((2013, 9, 9, 11, 36, 3))
    0000   0x83 0x64 0x4b 0x69 0x0d                   .dKi.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 Base (2009, 4, 0, 12, 11, 48) head[2], body[0] op[0x72]

    op hex (2)
    0000   0x72 0x90                                  r.
    decimal
            114  144
    datetime ((2009, 4, 0, 12, 11, 48))
    0000   0x70 0x0b 0x6c 0x00 0xa9                   p.l..
    body (0)
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 14 Base (2000, 8, 10, 11, 13, 41) head[2], body[0] op[0x6f]

    op hex (2)
    0000   0x6f 0x4b                                  oK
    decimal
            111   75
    datetime ((2000, 8, 10, 11, 13, 41))
    0000   0xa9 0x0d 0x0b 0x6a 0x00                   ...j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 15 Base (2015, 6, 10, 13, 41, 11) head[2], body[0] op[0xa9]

    op hex (2)
    0000   0xa9 0x6f                                  .o
    decimal
            169  111
    datetime ((2015, 6, 10, 13, 41, 11))
    0000   0x4b 0xa9 0x0d 0x0a 0x7f                   K....
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 1]
#### RECORD 16 Base (2015, 1, 31, 13, 41, 43) head[2], body[0] op[0x9d]

    op hex (2)
    0000   0x9d 0x71                                  .q
    decimal
            157  113
    datetime ((2015, 1, 31, 13, 41, 43))
    0000   0x2b 0x69 0x0d 0x3f 0x0f                   +i.?.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 0, 1]
#### RECORD 17 Base (2000, 13, 18, 13, 41, 43) head[2], body[0] op[0x9d]

    op hex (2)
    0000   0x9d 0x71                                  .q
    decimal
            157  113
    datetime ((2000, 13, 18, 13, 41, 43))
    0000   0xeb 0x69 0x0d 0x72 0x90                   .i.r.
    body (0)
    HOUR BITS: [0, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 18 Base (2009, 2, 12, 8, 42, 0) head[2], body[0] op[0x70]

    op hex (2)
    0000   0x70 0x5b                                  p[
    decimal
            112   91
    datetime ((2009, 2, 12, 8, 42, 0))
    0000   0x00 0xaa 0x48 0x0c 0x69                   ..H.i
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [0, 1, 1, 0]
#### RECORD 19 Base (2006, 8, 23, 14, 0, 16) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x00                                  ..
    decimal
             13    0
    datetime ((2006, 8, 23, 14, 0, 16))
    0000   0x90 0x00 0x6e 0x17 0x36                   ..n.6
    body (0)
    YEAR BITS: [0, 0, 1, 1]
`end logs/ReadHistoryData-page-2.data: 20 records`
