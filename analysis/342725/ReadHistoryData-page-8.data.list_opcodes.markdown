## START logs/ReadHistoryData-page-8.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x6d 0xa5                                  m.
##### DEBUG DECIMAL
            109  165
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 0.225, 'curve': 128},
 {'age': 136, 'amount': 0.275, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x09 0x7e 0x80 0x0b 0x88 0x80    \..~....
    decimal
             92    8    9  126  128   11  136  128
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2014-03-05T09:18:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    0    0
    datetime (2014-03-05T09:18:33)
    0000   0x21 0xd2 0x49 0x65 0x0e                   !.Ie.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 2 BolusWizard 2014-03-05T09:20:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 45,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 160}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-05T09:20:15)
    0000   0x0f 0xd4 0x09 0x65 0x0e                   ...e.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    -P.n(P..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x64         ......d
    decimal
             45   80    0  110   40   80    0    0
            160    0    0    0    0  160  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 1.3, 'curve': 128},
 {'age': 128, 'amount': 0.225, 'curve': 128},
 {'age': 138, 'amount': 0.275, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x34 0x08 0x80 0x09 0x80 0x80    \.4.....
    0008   0x0b 0x8a 0x80                             ...
    decimal
             92   11   52    8  128    9  128  128
             11  138  128
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2014-03-05T09:20:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x34 0x00    ......4.
    decimal
              1    0  160    0  160    0   52    0
    datetime (2014-03-05T09:20:15)
    0000   0x0f 0xd4 0x49 0x65 0x0e                   ..Ie.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 BasalProfileStart 2014-03-05T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-05T10:30:00)
    0000   0x00 0xde 0x0a 0x05 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 6 CalBGForPH 2014-03-05T12:14:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 209}
```
    op hex (2)
    0000   0x0a 0xd1                                  ..
    decimal
             10  209
    datetime (2014-03-05T12:14:47)
    0000   0x2f 0xce 0x2c 0x65 0x0e                   /.,e.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2014-03-05T12:14:47 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2014-03-05T12:14:47)
    0000   0x2f 0xce 0x2c 0x65 0x0e                   /.,e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 BolusWizard 2014-03-05T12:14:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 209,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 8.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd1                                  [.
    decimal
             91  209
    datetime (2014-03-05T12:14:54)
    0000   0x36 0xce 0x0c 0x05 0x0e                   6....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x54 0x00    .P.x2PT.
    0008   0x00 0x00 0x00 0x00 0x00 0x54 0x64         .....Td
    decimal
              0   80    0  120   50   80   84    0
              0    0    0    0    0   84  100
    HOUR BITS: [1, 1, 0]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 172, 'amount': 1.4, 'curve': 128},
 {'age': 182, 'amount': 3.9, 'curve': 128},
 {'age': 46, 'amount': 0.225, 'curve': 144},
 {'age': 56, 'amount': 0.275, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x38 0xac 0x80 0x9c 0xb6 0x80    \.8.....
    0008   0x09 0x2e 0x90 0x0b 0x38 0x90              ....8.
    decimal
             92   14   56  172  128  156  182  128
              9   46  144   11   56  144
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2014-03-05T12:14:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x00 0x00    ..T.T...
    decimal
              1    0   84    0   84    0    0    0
    datetime (2014-03-05T12:14:54)
    0000   0x36 0xce 0x4c 0x05 0x0e                   6.L..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 BolusWizard 2014-03-05T13:16:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 1,
 'bg': 0,
 'bg_target_high': 1,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 90,
 'carb_ratio': 0,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 44}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-05T13:16:14)
    0000   0x0e 0xd0 0x0d 0x65 0x0e                   ...e.
    body (15)
    hex
    0000   0x5a 0x50 0x00 0x78 0x32 0x50 0x00 0x01    ZP.x2P..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x64         ,....,d
    decimal
             90   80    0  120   50   80    0    1
             44    0    0    0    1   44  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 12 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 2.1, 'curve': 128},
 {'age': 234, 'amount': 1.4, 'curve': 128},
 {'age': 244, 'amount': 3.9, 'curve': 128},
 {'age': 108, 'amount': 0.225, 'curve': 144},
 {'age': 118, 'amount': 0.275, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x54 0x40 0x80 0x38 0xea 0x80    \.T@.8..
    0008   0x9c 0xf4 0x80 0x09 0x6c 0x90 0x0b 0x76    ....l..v
    0010   0x90                                       .
    decimal
             92   17   84   64  128   56  234  128
            156  244  128    9  108  144   11  118
            144
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2014-03-05T13:16:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x2c 0x01 0x2c 0x00 0x24 0x00    ..,.,.$.
    decimal
              1    1   44    1   44    0   36    0
    datetime (2014-03-05T13:16:15)
    0000   0x0f 0xd0 0x4d 0x65 0x0e                   ..Me.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 CalBGForPH 2014-03-05T16:17:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2014-03-05T16:17:25)
    0000   0x19 0xd1 0x30 0x65 0x0e                   ..0e.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 Ian3F 2014-03-05T16:17:25 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2014-03-05T16:17:25)
    0000   0x19 0xd1 0xf0 0x65 0x0e                   ...e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 BolusWizard 2014-03-05T18:37:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 40,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 132}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-05T18:37:22)
    0000   0x16 0xe5 0x12 0x65 0x0e                   ...e.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x78 0x32 0x50 0x00 0x00    (P.x2P..
    0008   0x84 0x00 0x00 0x00 0x00 0x84 0x64         ......d
    decimal
             40   80    0  120   50   80    0    0
            132    0    0    0    0  132  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 69, 'amount': 1.1, 'curve': 145},
 {'age': 129, 'amount': 2.1, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x45 0x91 0x54 0x81 0x90    \.,E.T..
    decimal
             92    8   44   69  145   84  129  144
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2014-03-05T18:37:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x00 0x00    ........
    decimal
              1    0  132    0  132    0    0    0
    datetime (2014-03-05T18:37:22)
    0000   0x16 0xe5 0x52 0x65 0x0e                   ..Re.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 BolusWizard 2014-03-05T20:34:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
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
    datetime (2014-03-05T20:34:50)
    0000   0x32 0xe2 0x14 0x65 0x0e                   2..e.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x64         l....ld
    decimal
             30   80    0  110   50   80    0    0
            108    0    0    0    0  108  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 122, 'amount': 3.3, 'curve': 128},
 {'age': 186, 'amount': 1.1, 'curve': 145}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0x7a 0x80 0x2c 0xba 0x91    \..z.,..
    decimal
             92    8  132  122  128   44  186  145
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2014-03-05T20:34:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x00 0x00    ..l.l...
    decimal
              1    0  108    0  108    0    0    0
    datetime (2014-03-05T20:34:50)
    0000   0x32 0xe2 0x54 0x65 0x0e                   2.Te.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 BolusWizard 2014-03-05T21:17:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
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
    datetime (2014-03-05T21:17:56)
    0000   0x38 0xd1 0x15 0x65 0x0e                   8..e.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x64         l....ld
    decimal
             30   80    0  110   50   80    0    0
            108    0    0    0    0  108  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 45, 'amount': 2.7, 'curve': 128},
 {'age': 165, 'amount': 3.3, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x2d 0x80 0x84 0xa5 0x80    \.l-....
    decimal
             92    8  108   45  128  132  165  128
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2014-03-05T21:17:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x48 0x00    ..l.l.H.
    decimal
              1    0  108    0  108    0   72    0
    datetime (2014-03-05T21:17:56)
    0000   0x38 0xd1 0x55 0x65 0x0e                   8.Ue.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 BasalProfileStart 2014-03-05T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-05T22:30:00)
    0000   0x00 0xde 0x16 0x05 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 26 BasalProfileStart 2014-03-06T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-06T00:00:00)
    0000   0x00 0xc0 0x00 0x06 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 27 MResultTotals 2014-03-06T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xf4                   .....
    decimal
              7    0    0    5  244
    datetime (2014-03-06T00:00:00)
    0000   0x25 0x8e                                  %.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 28 Sara6E 2014-03-06T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-06T00:00:00)
    0000   0x25 0x8e                                  %.
    body (49)
    hex
    0000   0x05 0x00 0xa8 0x7a 0xd1 0x06 0x00 0x00    ...z....
    0008   0x05 0xf4 0x01 0xe4 0x20 0x04 0x10 0x44    .... ..D
    0010   0x00 0xfa 0x03 0x5c 0x00 0xb4 0x00 0x00    ...\....
    0018   0x00 0x00 0x06 0x03 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  168  122  209    6    0    0
              5  244    1  228   32    4   16   68
              0  250    3   92    0  180    0    0
              0    0    6    3    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 29 CalBGForPH 2014-03-06T00:25:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 259}
```
    op hex (2)
    0000   0x0a 0x03                                  ..
    decimal
             10    3
    datetime (2014-03-06T00:25:43)
    0000   0x2b 0xd9 0x20 0x66 0x8e                   +. f.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 Ian3F 2014-03-06T00:25:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2014-03-06T00:25:43)
    0000   0x2b 0xd9 0x60 0x66 0x0e                   +.`f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 BolusWizard 2014-03-06T00:26:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 259,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 11.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x03                                  [.
    decimal
             91    3
    datetime (2014-03-06T00:26:14)
    0000   0x0e 0xda 0x00 0x06 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x6e 0x37 0x50 0x70 0x00    .Q.n7Pp.
    0008   0x00 0x00 0x00 0x00 0x00 0x70 0x64         .....pd
    decimal
              0   81    0  110   55   80  112    0
              0    0    0    0    0  112  100
    HOUR BITS: [1, 1, 0]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 194, 'amount': 2.7, 'curve': 128},
 {'age': 234, 'amount': 2.7, 'curve': 128},
 {'age': 98, 'amount': 3.3, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0xc2 0x80 0x6c 0xea 0x80    \.l..l..
    0008   0x84 0x62 0x90                             .b.
    decimal
             92   11  108  194  128  108  234  128
            132   98  144
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2014-03-06T00:26:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0xa8 0x00 0x00 0x00    ........
    decimal
              1    0  168    0  168    0    0    0
    datetime (2014-03-06T00:26:14)
    0000   0x0e 0xda 0x40 0x06 0x0e                   ..@..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 34 BasalProfileStart 2014-03-06T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-06T02:00:00)
    0000   0x00 0xc0 0x02 0x06 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 35 BasalProfileStart 2014-03-06T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-06T04:00:00)
    0000   0x00 0xc0 0x04 0x06 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 36 BasalProfileStart 2014-03-06T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-06T06:00:00)
    0000   0x00 0xc0 0x06 0x06 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 37 BasalProfileStart 2014-03-06T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-06T10:30:00)
    0000   0x00 0xde 0x0a 0x06 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 38 CalBGForPH 2014-03-06T11:54:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2014-03-06T11:54:37)
    0000   0x25 0xf6 0x2b 0x06 0x0e                   %.+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 39 BolusWizard 2014-03-06T11:54:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2014-03-06T11:54:39)
    0000   0x27 0xf6 0x0b 0x66 0x0e                   '..f.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x38 0x00    .P.x2P8.
    0008   0x00 0x00 0x00 0x00 0x00 0x38 0x64         .....8d
    decimal
              0   80    0  120   50   80   56    0
              0    0    0    0    0   56  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 Bolus 2014-03-06T11:54:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2014-03-06T11:54:39)
    0000   0x27 0xf6 0x4b 0x66 0x0e                   '.Kf.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 BolusWizard 2014-03-06T11:56:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 5.6,
 'carb_input': 15,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 48}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2014-03-06T11:56:07)
    0000   0x07 0xf8 0x0b 0x66 0x0e                   ...f.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x32 0x50 0x38 0x00    .P.x2P8.
    0008   0x30 0x00 0x00 0x38 0x00 0x30 0x64         0..8.0d
    decimal
             15   80    0  120   50   80   56    0
             48    0    0   56    0   48  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 1.4, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0x04 0x80                   \.8..
    decimal
             92    5   56    4  128
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2014-03-06T11:56:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x38 0x00    ..0.0.8.
    decimal
              1    0   48    0   48    0   56    0
    datetime (2014-03-06T11:56:07)
    0000   0x07 0xf8 0x4b 0x66 0x0e                   ..Kf.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 BolusWizard 2014-03-06T17:07:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 8,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 24}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-06T17:07:27)
    0000   0x1b 0xc7 0x11 0x66 0x0e                   ...f.
    body (15)
    hex
    0000   0x08 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x18 0x00 0x00 0x00 0x00 0x18 0x64         ......d
    decimal
              8   80    0  120   50   80    0    0
             24    0    0    0    0   24  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 45 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 2.6, 'curve': 144}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0x3b 0x90                   \.h;.
    decimal
             92    5  104   59  144
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2014-03-06T17:07:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x00 0x00    ........
    decimal
              1    0   24    0   24    0    0    0
    datetime (2014-03-06T17:07:27)
    0000   0x1b 0xc7 0x51 0x66 0x0e                   ..Qf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 47 BolusWizard 2014-03-06T19:22:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
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
    datetime (2014-03-06T19:22:36)
    0000   0x24 0xd6 0x13 0x66 0x0e                   $..f.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 140, 'amount': 0.6, 'curve': 128},
 {'age': 194, 'amount': 2.6, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x18 0x8c 0x80 0x68 0xc2 0x90    \....h..
    decimal
             92    8   24  140  128  104  194  144
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2014-03-06T19:22:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2014-03-06T19:22:36)
    0000   0x24 0xd6 0x53 0x66 0x0e                   $.Sf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 50 BolusWizard 2014-03-06T19:25:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
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
    datetime (2014-03-06T19:25:28)
    0000   0x1c 0xd9 0x13 0x66 0x0e                   ...f.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 1.8, 'curve': 128},
 {'age': 143, 'amount': 0.6, 'curve': 128},
 {'age': 197, 'amount': 2.6, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x03 0x80 0x18 0x8f 0x80    \.H.....
    0008   0x68 0xc5 0x90                             h..
    decimal
             92   11   72    3  128   24  143  128
            104  197  144
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2014-03-06T19:25:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x48 0x00    ..H.H.H.
    decimal
              1    0   72    0   72    0   72    0
    datetime (2014-03-06T19:25:28)
    0000   0x1c 0xd9 0x53 0x66 0x0e                   ..Sf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 BolusWizard 2014-03-06T19:28:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 35,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 124}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-06T19:28:53)
    0000   0x35 0xdc 0x13 0x66 0x0e                   5..f.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    #P.n2P..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x64         |....|d
    decimal
             35   80    0  110   50   80    0    0
            124    0    0    0    0  124  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 3.6, 'curve': 128},
 {'age': 146, 'amount': 0.6, 'curve': 128},
 {'age': 200, 'amount': 2.6, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x90 0x06 0x80 0x18 0x92 0x80    \.......
    0008   0x68 0xc8 0x90                             h..
    decimal
             92   11  144    6  128   24  146  128
            104  200  144
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2014-03-06T19:28:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x90 0x00    ..|.|...
    decimal
              1    0  124    0  124    0  144    0
    datetime (2014-03-06T19:28:53)
    0000   0x35 0xdc 0x53 0x66 0x0e                   5.Sf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 56 BolusWizard 2014-03-06T20:11:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 50,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 180}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-06T20:11:52)
    0000   0x34 0xcb 0x14 0x66 0x0e                   4..f.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    2P.n2P..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x64         ......d
    decimal
             50   80    0  110   50   80    0    0
            180    0    0    0    0  180  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 0.3, 'curve': 129},
 {'age': 189, 'amount': 0.6, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x0c 0x31 0x81 0x18 0xbd 0x80    \..1....
    decimal
             92    8   12   49  129   24  189  128
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2014-03-06T20:11:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 18.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0xa4 0x00    ........
    decimal
              1    0  180    0  180    0  164    0
    datetime (2014-03-06T20:11:52)
    0000   0x34 0xcb 0x54 0x66 0x0e                   4.Tf.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 59 BasalProfileStart 2014-03-06T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-06T22:30:00)
    0000   0x00 0xde 0x16 0x06 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 60 CalBGForPH 2014-03-06T23:40:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 270}
```
    op hex (2)
    0000   0x0a 0x0e                                  ..
    decimal
             10   14
    datetime (2014-03-06T23:40:05)
    0000   0x05 0xe8 0x37 0x66 0x8e                   ..7f.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 61 Ian3F 2014-03-06T23:40:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x21                                  ?!
    decimal
             63   33
    datetime (2014-03-06T23:40:05)
    0000   0x05 0xe8 0xd7 0x66 0x0e                   ...f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 BolusWizard 2014-03-06T23:40:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 270,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 12.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0e                                  [.
    decimal
             91   14
    datetime (2014-03-06T23:40:34)
    0000   0x22 0xe8 0x17 0x06 0x0e                   "....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x6e 0x37 0x50 0x78 0x00    .Q.n7Px.
    0008   0x00 0x00 0x00 0x00 0x00 0x78 0x64         .....xd
    decimal
              0   81    0  110   55   80  120    0
              0    0    0    0    0  120  100
    HOUR BITS: [1, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 208, 'amount': 4.3, 'curve': 128},
 {'age': 218, 'amount': 0.2, 'curve': 128},
 {'age': 2, 'amount': 0.3, 'curve': 145},
 {'age': 142, 'amount': 0.6, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0xac 0xd0 0x80 0x08 0xda 0x80    \.......
    0008   0x0c 0x02 0x91 0x18 0x8e 0x90              ......
    decimal
             92   14  172  208  128    8  218  128
             12    2  145   24  142  144
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2014-03-06T23:40:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 20.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x00 0x00    ........
    decimal
              1    0  200    0  200    0    0    0
    datetime (2014-03-06T23:40:34)
    0000   0x22 0xe8 0x57 0x06 0x0e                   ".W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 65 BasalProfileStart 2014-03-07T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-07T00:00:00)
    0000   0x00 0xc0 0x00 0x07 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 66 MResultTotals 2014-03-07T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x94                   .....
    decimal
              7    0    0    5  148
    datetime (2014-03-07T00:00:00)
    0000   0x26 0x8e                                  &.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 67 Sara6E 2014-03-07T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-07T00:00:00)
    0000   0x26 0x8e                                  &.
    body (49)
    hex
    0000   0x05 0x14 0xe9 0x03 0x0e 0x03 0x00 0x00    ........
    0008   0x05 0x94 0x01 0xe4 0x22 0x03 0xb0 0x42    ...."..B
    0010   0x00 0x94 0x02 0x08 0x01 0xa8 0x00 0x00    ........
    0018   0x00 0x00 0x06 0x03 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xab    ........
    0028   0xab 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   20  233    3   14    3    0    0
              5  148    1  228   34    3  176   66
              0  148    2    8    1  168    0    0
              0    0    6    3    0    0    0    0
              0    0    0    0    0    0    0  171
            171    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 68 BasalProfileStart 2014-03-07T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-07T02:00:00)
    0000   0x00 0xc0 0x02 0x07 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 69 BasalProfileStart 2014-03-07T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-07T04:00:00)
    0000   0x00 0xc0 0x04 0x07 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 70 LowReservoir 2014-03-07T04:11:06 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-03-07T04:11:06)
    0000   0x06 0xcb 0x04 0x07 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 71 BasalProfileStart 2014-03-07T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-07T06:00:00)
    0000   0x00 0xc0 0x06 0x07 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 72 CalBGForPH 2014-03-07T08:01:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2014-03-07T08:01:12)
    0000   0x0c 0xc1 0x28 0x07 0x0e                   ..(..
    body (0)
    HOUR BITS: [1, 1, 0]
`end logs/ReadHistoryData-page-8.data: 73 records`
