## START logs/ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 1012, found 10 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc1 0x42                                  .B
##### DEBUG DECIMAL
            193   66
#### RECORD 0 BolusWizard 2014-03-08T12:08:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 173,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 4.4,
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
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2014-03-08T12:08:30)
    0000   0x1e 0xc8 0x0c 0x68 0x0e                   ...h.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x38 0x00    .P.x2P8.
    0008   0x00 0x00 0x00 0x2c 0x00 0x0c 0x64         ...,..d
    decimal
              0   80    0  120   50   80   56    0
              0    0    0   44    0   12  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 2.7, 'curve': 128},
 {'age': 96, 'amount': 3.6, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x6c 0x56 0x80 0x90 0x60 0x80    \.lV..`.
    decimal
             92    8  108   86  128  144   96  128
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2014-03-08T12:08:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x2c 0x00    ..<.<.,.
    decimal
              1    0   60    0   60    0   44    0
    datetime (2014-03-08T12:08:30)
    0000   0x1e 0xc8 0x4c 0x68 0x0e                   ..Lh.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2014-03-08T15:11:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2014-03-08T15:11:23)
    0000   0x17 0xcb 0x2f 0x68 0x0e                   ../h.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 Ian3F 2014-03-08T15:11:23 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-03-08T15:11:23)
    0000   0x17 0xcb 0xef 0x68 0x0e                   ...h.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 BolusWizard 2014-03-08T15:11:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 5.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2014-03-08T15:11:57)
    0000   0x39 0xcb 0x0f 0x08 0x0e                   9....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x34 0x00    .P.x2P4.
    0008   0x00 0x00 0x00 0x00 0x00 0x34 0x64         .....4d
    decimal
              0   80    0  120   50   80   52    0
              0    0    0    0    0   52  100
    HOUR BITS: [1, 1, 0]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 189, 'amount': 1.5, 'curve': 128},
 {'age': 13, 'amount': 2.7, 'curve': 144},
 {'age': 23, 'amount': 3.6, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0xbd 0x80 0x6c 0x0d 0x90    \.<..l..
    0008   0x90 0x17 0x90                             ...
    decimal
             92   11   60  189  128  108   13  144
            144   23  144
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2014-03-08T15:11:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x00 0x00    ..4.4...
    decimal
              1    0   52    0   52    0    0    0
    datetime (2014-03-08T15:11:57)
    0000   0x39 0xcb 0x4f 0x08 0x0e                   9.O..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 CalBGForPH 2014-03-08T16:09:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2014-03-08T16:09:06)
    0000   0x06 0xc9 0x30 0x08 0x0e                   ..0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 9 CalBGForPH 2014-03-08T16:58:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2014-03-08T16:58:27)
    0000   0x1b 0xfa 0x30 0x08 0x0e                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 10 BolusWizard 2014-03-08T16:58:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 4.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2014-03-08T16:58:29)
    0000   0x1d 0xfa 0x10 0x68 0x0e                   ...h.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x30 0x00    .P.x2P0.
    0008   0x00 0x00 0x00 0x08 0x00 0x28 0x64         .....(d
    decimal
              0   80    0  120   50   80   48    0
              0    0    0    8    0   40  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 106, 'amount': 1.2, 'curve': 128},
 {'age': 116, 'amount': 0.1, 'curve': 128},
 {'age': 40, 'amount': 1.5, 'curve': 144},
 {'age': 120, 'amount': 2.7, 'curve': 144},
 {'age': 130, 'amount': 3.6, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x30 0x6a 0x80 0x04 0x74 0x80    \.0j..t.
    0008   0x3c 0x28 0x90 0x6c 0x78 0x90 0x90 0x82    <(.lx...
    0010   0x90                                       .
    decimal
             92   17   48  106  128    4  116  128
             60   40  144  108  120  144  144  130
            144
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2014-03-08T16:58:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x08 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    8    0
    datetime (2014-03-08T16:58:29)
    0000   0x1d 0xfa 0x50 0x68 0x0e                   ..Ph.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 CalBGForPH 2014-03-08T20:33:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2014-03-08T20:33:15)
    0000   0x0f 0xe1 0x34 0x68 0x0e                   ..4h.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 Ian3F 2014-03-08T20:33:15 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2014-03-08T20:33:15)
    0000   0x0f 0xe1 0xb4 0x68 0x0e                   ...h.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 15 BolusWizard 2014-03-08T20:56:45 head[2], body[15] op[0x5b]
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
    datetime (2014-03-08T20:56:45)
    0000   0x2d 0xf8 0x14 0x68 0x0e                   -..h.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 244, 'amount': 1.0, 'curve': 128},
 {'age': 88, 'amount': 1.2, 'curve': 144},
 {'age': 98, 'amount': 0.1, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0xf4 0x80 0x30 0x58 0x90    \.(..0X.
    0008   0x04 0x62 0x90                             .b.
    decimal
             92   11   40  244  128   48   88  144
              4   98  144
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2014-03-08T20:56:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2014-03-08T20:56:45)
    0000   0x2d 0xf8 0x54 0x68 0x0e                   -.Th.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 BolusWizard 2014-03-08T21:21:55 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 1,
 'bg': 0,
 'bg_target_high': 1,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 110,
 'carb_ratio': 0,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 144}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-08T21:21:55)
    0000   0x37 0xd5 0x15 0x68 0x0e                   7..h.
    body (15)
    hex
    0000   0x6e 0x50 0x00 0x6e 0x32 0x50 0x00 0x01    nP.n2P..
    0008   0x90 0x00 0x00 0x00 0x01 0x90 0x64         ......d
    decimal
            110   80    0  110   50   80    0    1
            144    0    0    0    1  144  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 1.8, 'curve': 128},
 {'age': 13, 'amount': 1.0, 'curve': 144},
 {'age': 113, 'amount': 1.2, 'curve': 144},
 {'age': 123, 'amount': 0.1, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x1d 0x80 0x28 0x0d 0x90    \.H..(..
    0008   0x30 0x71 0x90 0x04 0x7b 0x90              0q..{.
    decimal
             92   14   72   29  128   40   13  144
             48  113  144    4  123  144
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2014-03-08T21:21:55 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x01 0x90 0x01 0x90 0x00 0x3c 0x00    ......<.
    decimal
              1    1  144    1  144    0   60    0
    datetime (2014-03-08T21:21:55)
    0000   0x37 0xd5 0x55 0x68 0x0e                   7.Uh.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 BasalProfileStart 2014-03-08T22:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2014-03-08T22:30:00)
    0000   0x00 0xde 0x16 0x08 0x0e                   .....
    body (3)
    hex
    0000   0x2d 0x15 0x00                             -..
    decimal
             45   21    0
    HOUR BITS: [1, 1, 0]
#### RECORD 22 Bolus 2014-03-08T22:31:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x98 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  152    0
    datetime (2014-03-08T22:31:17)
    0000   0x11 0xdf 0x56 0x08 0x0e                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 PumpSuspend 2014-03-08T22:36:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-03-08T22:36:53)
    0000   0x35 0xe4 0x16 0x08 0x0e                   5....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 MResultTotals 2014-03-09T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x8b                   .....
    decimal
              7    0    0    6  139
    datetime (2014-03-09T00:00:00)
    0000   0x28 0x8e                                  (.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 25 Sara6E 2014-03-09T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-03-09T00:00:00)
    0000   0x28 0x8e                                  (.
    body (49)
    hex
    0000   0x05 0x00 0x92 0x49 0xb9 0x08 0x00 0x00    ...I....
    0008   0x06 0x8b 0x01 0xaf 0x1a 0x04 0xdc 0x4a    .......J
    0010   0x00 0xfa 0x02 0xd4 0x00 0xd4 0x00 0xbc    ........
    0018   0x00 0x78 0x04 0x04 0x01 0x01 0x00 0x00    .x......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x6a    .......j
    0028   0xc8 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  146   73  185    8    0    0
              6  139    1  175   26    4  220   74
              0  250    2  212    0  212    0  188
              0  120    4    4    1    1    0    0
              0    0    0    0    0    0    0  106
            200    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 26 BasalProfileStart 2014-03-09T00:33:03 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-03-09T00:33:03)
    0000   0x03 0xe1 0x00 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x00 0x15 0x00                             ...
    decimal
              0   21    0
    HOUR BITS: [1, 1, 1]
#### RECORD 27 PumpResume 2014-03-09T00:33:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-03-09T00:33:03)
    0000   0x03 0xe1 0x00 0x09 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 28 CalBGForPH 2014-03-09T00:33:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2014-03-09T00:33:22)
    0000   0x16 0xe1 0x20 0x09 0x0e                   .. ..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 29 BolusWizard 2014-03-09T00:33:28 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2014-03-09T00:33:28)
    0000   0x1c 0xe1 0x00 0x09 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x3c 0x00    .P.n7P<.
    0008   0x00 0x00 0x00 0x00 0x00 0x3c 0x64         .....<d
    decimal
              0   80    0  110   55   80   60    0
              0    0    0    0    0   60  100
    HOUR BITS: [1, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 1.95, 'curve': 128},
 {'age': 131, 'amount': 1.05, 'curve': 128},
 {'age': 191, 'amount': 3.3, 'curve': 129},
 {'age': 201, 'amount': 0.3, 'curve': 128},
 {'age': 221, 'amount': 1.8, 'curve': 128},
 {'age': 205, 'amount': 1.0, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0x4e 0x79 0x80 0x2a 0x83 0x80    \.Ny.*..
    0008   0x84 0xbf 0x81 0x0c 0xc9 0x80 0x48 0xdd    ......H.
    0010   0x80 0x28 0xcd 0x90                        .(..
    decimal
             92   20   78  121  128   42  131  128
            132  191  129   12  201  128   72  221
            128   40  205  144
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2014-03-09T00:33:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x00 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    0    0
    datetime (2014-03-09T00:33:28)
    0000   0x1c 0xe1 0x40 0x09 0x0e                   ..@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 32 BasalProfileStart 2014-03-09T02:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-03-09T02:00:00)
    0000   0x00 0xc0 0x02 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x04 0x1a 0x00                             ...
    decimal
              4   26    0
    HOUR BITS: [1, 1, 0]
#### RECORD 33 CalBGForPH 2014-03-09T02:01:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2014-03-09T02:01:02)
    0000   0x02 0xc1 0x22 0x09 0x0e                   .."..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 34 BolusWizard 2014-03-09T02:01:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 216,
 'bg_target_high': 0,
 'bg_target_low': 55,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 8.4,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2014-03-09T02:01:11)
    0000   0x0b 0xc1 0x02 0x69 0x0e                   ...i.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x37 0x50 0x54 0x00    .P.n7PT.
    0008   0x00 0x00 0x00 0x14 0x00 0x40 0x64         .....@d
    decimal
              0   80    0  110   55   80   84    0
              0    0    0   20    0   64  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 89, 'amount': 2.5, 'curve': 128},
 {'age': 209, 'amount': 1.95, 'curve': 128},
 {'age': 219, 'amount': 1.05, 'curve': 128},
 {'age': 23, 'amount': 3.3, 'curve': 145},
 {'age': 33, 'amount': 0.3, 'curve': 144},
 {'age': 53, 'amount': 1.8, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0x64 0x59 0x80 0x4e 0xd1 0x80    \.dY.N..
    0008   0x2a 0xdb 0x80 0x84 0x17 0x91 0x0c 0x21    *......!
    0010   0x90 0x48 0x35 0x90                        .H5.
    decimal
             92   20  100   89  128   78  209  128
             42  219  128  132   23  145   12   33
            144   72   53  144
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2014-03-09T02:01:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 13.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x88 0x00 0x88 0x00 0x14 0x00    ........
    decimal
              1    0  136    0  136    0   20    0
    datetime (2014-03-09T02:01:12)
    0000   0x0c 0xc1 0x42 0x69 0x0e                   ..Bi.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 BasalProfileStart 2014-03-09T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-03-09T04:00:00)
    0000   0x00 0xc0 0x04 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x08 0x1b 0x00                             ...
    decimal
              8   27    0
    HOUR BITS: [1, 1, 0]
#### RECORD 38 BasalProfileStart 2014-03-09T06:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-03-09T06:00:00)
    0000   0x00 0xc0 0x06 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x0c 0x19 0x00                             ...
    decimal
             12   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 39 CalBGForPH 2014-03-09T08:00:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2014-03-09T08:00:38)
    0000   0x26 0xc0 0x28 0x09 0x0e                   &.(..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 40 BolusWizard 2014-03-09T08:00:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 161,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa1                                  [.
    decimal
             91  161
    datetime (2014-03-09T08:00:41)
    0000   0x29 0xc0 0x08 0x09 0x0e                   )....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x3c 0x00    .P.n(P<.
    0008   0x00 0x00 0x00 0x00 0x00 0x3c 0x64         .....<d
    decimal
              0   80    0  110   40   80   60    0
              0    0    0    0    0   60  100
    HOUR BITS: [1, 1, 0]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 2.2, 'curve': 144},
 {'age': 112, 'amount': 1.2, 'curve': 144},
 {'age': 192, 'amount': 2.5, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x66 0x90 0x30 0x70 0x90    \.Xf.0p.
    0008   0x64 0xc0 0x90                             d..
    decimal
             92   11   88  102  144   48  112  144
            100  192  144
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2014-03-09T08:00:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2014-03-09T08:00:41)
    0000   0x29 0xc0 0x48 0x09 0x0e                   ).H..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 43 CalBGForPH 2014-03-09T09:00:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2014-03-09T09:00:23)
    0000   0x17 0xc0 0x29 0x69 0x0e                   ..)i.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 44 Ian3F 2014-03-09T09:00:23 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2014-03-09T09:00:23)
    0000   0x17 0xc0 0x09 0x69 0x0e                   ...i.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 45 BolusWizard 2014-03-09T09:08:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 176,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 2.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 7.6,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 108}
```
    op hex (2)
    0000   0x5b 0xb0                                  [.
    decimal
             91  176
    datetime (2014-03-09T09:08:53)
    0000   0x35 0xc8 0x09 0x69 0x0e                   5..i.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x6e 0x28 0x50 0x4c 0x00    .P.n(PL.
    0008   0x6c 0x00 0x00 0x14 0x00 0xa4 0x64         l.....d
    decimal
             30   80    0  110   40   80   76    0
            108    0    0   20    0  164  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 76, 'amount': 1.5, 'curve': 128},
 {'age': 170, 'amount': 2.2, 'curve': 144},
 {'age': 180, 'amount': 1.2, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0x4c 0x80 0x58 0xaa 0x90    \.<L.X..
    0008   0x30 0xb4 0x90                             0..
    decimal
             92   11   60   76  128   88  170  144
             48  180  144
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2014-03-09T09:08:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x14 0x00    ........
    decimal
              1    0  164    0  164    0   20    0
    datetime (2014-03-09T09:08:53)
    0000   0x35 0xc8 0x49 0x69 0x0e                   5.Ii.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2014-03-09T09:56:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 40,
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
    datetime (2014-03-09T09:56:07)
    0000   0x07 0xf8 0x09 0x69 0x0e                   ...i.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x28 0x50 0x00 0x00    .P.n(P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   40   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 54, 'amount': 4.1, 'curve': 128},
 {'age': 124, 'amount': 1.5, 'curve': 128},
 {'age': 218, 'amount': 2.2, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa4 0x36 0x80 0x3c 0x7c 0x80    \..6.<|.
    0008   0x58 0xda 0x90                             X..
    decimal
             92   11  164   54  128   60  124  128
             88  218  144
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2014-03-09T09:56:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x58 0x00    ..H.H.X.
    decimal
              1    0   72    0   72    0   88    0
    datetime (2014-03-09T09:56:07)
    0000   0x07 0xf8 0x49 0x69 0x0e                   ..Ii.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 CalBGForPH 2014-03-09T10:20:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 294}
```
    op hex (2)
    0000   0x0a 0x26                                  .&
    decimal
             10   38
    datetime (2014-03-09T10:20:55)
    0000   0x37 0xd4 0x2a 0x69 0x8e                   7.*i.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 52 Ian3F 2014-03-09T10:20:55 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x24                                  ?$
    decimal
             63   36
    datetime (2014-03-09T10:20:55)
    0000   0x37 0xd4 0xca 0x69 0x0e                   7..i.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 BolusWizard 2014-03-09T10:21:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 294,
 'bg_target_high': 0,
 'bg_target_low': 40,
 'bolus_estimate': 10.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 19.2,
 'sensitivity': 110,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x26                                  [&
    decimal
             91   38
    datetime (2014-03-09T10:21:29)
    0000   0x1d 0xd5 0x0a 0x09 0x0e                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x6e 0x28 0x50 0xc0 0x00    .Q.n(P..
    0008   0x00 0x00 0x00 0x68 0x00 0x58 0x64         ...h.Xd
    decimal
              0   81    0  110   40   80  192    0
              0    0    0  104    0   88  100
    HOUR BITS: [1, 1, 0]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 1.8, 'curve': 128},
 {'age': 79, 'amount': 4.1, 'curve': 128},
 {'age': 149, 'amount': 1.5, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x1d 0x80 0xa4 0x4f 0x80    \.H...O.
    0008   0x3c 0x95 0x80                             <..
    decimal
             92   11   72   29  128  164   79  128
             60  149  128
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2014-03-09T10:21:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 16.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x68 0x00    ......h.
    decimal
              1    0  160    0  160    0  104    0
    datetime (2014-03-09T10:21:29)
    0000   0x1d 0xd5 0x4a 0x09 0x0e                   ..J..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 BasalProfileStart 2014-03-09T10:30:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-09T10:30:00)
    0000   0x00 0xde 0x0a 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 57 TempBasal 2014-03-09T14:41:52 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-09T14:41:52)
    0000   0x34 0xe9 0x0e 0x09 0x0e                   4....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 1]
#### RECORD 58 TempBasalDuration 2014-03-09T14:41:52 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-09T14:41:52)
    0000   0x34 0xe9 0x0e 0x09 0x0e                   4....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 59 BasalProfileStart 2014-03-09T15:41:52 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-09T15:41:52)
    0000   0x34 0xe9 0x0f 0x09 0x0e                   4....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 1]
#### RECORD 60 CalBGForPH 2014-03-09T16:02:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2014-03-09T16:02:55)
    0000   0x37 0xc2 0x30 0x69 0x0e                   7.0i.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 61 Ian3F 2014-03-09T16:02:55 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-03-09T16:02:55)
    0000   0x37 0xc2 0xf0 0x69 0x0e                   7..i.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 TempBasal 2014-03-09T16:03:20 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-03-09T16:03:20)
    0000   0x14 0xc3 0x10 0x09 0x0e                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 63 TempBasalDuration 2014-03-09T16:03:20 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2014-03-09T16:03:20)
    0000   0x14 0xc3 0x10 0x09 0x0e                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 BasalProfileStart 2014-03-09T17:03:20 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-03-09T17:03:20)
    0000   0x14 0xc3 0x11 0x09 0x0e                   .....
    body (3)
    hex
    0000   0x15 0x10 0x00                             ...
    decimal
             21   16    0
    HOUR BITS: [1, 1, 0]
#### RECORD 65 BolusWizard 2014-03-09T17:27:26 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 10,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 32}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-09T17:27:26)
    0000   0x1a 0xdb 0x11 0x69 0x0e                   ...i.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x20 0x00 0x00 0x00 0x00 0x20 0x64          .... d
    decimal
             10   80    0  120   50   80    0    0
             32    0    0    0    0   32  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 169, 'amount': 3.25, 'curve': 144},
 {'age': 179, 'amount': 0.75, 'curve': 144},
 {'age': 199, 'amount': 1.8, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x82 0xa9 0x90 0x1e 0xb3 0x90    \.......
    0008   0x48 0xc7 0x90                             H..
    decimal
             92   11  130  169  144   30  179  144
             72  199  144
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2014-03-09T17:27:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x00 0x00    .. . ...
    decimal
              1    0   32    0   32    0    0    0
    datetime (2014-03-09T17:27:26)
    0000   0x1a 0xdb 0x51 0x69 0x0e                   ..Qi.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 BolusWizard 2014-03-09T17:28:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 80,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 0,
 'bg_target_low': 50,
 'bolus_estimate': 0.0,
 'carb_input': 12,
 'carb_ratio': 0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-09T17:28:54)
    0000   0x36 0xdc 0x11 0x69 0x0e                   6..i.
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x64         (....(d
    decimal
             12   80    0  120   50   80    0    0
             40    0    0    0    0   40  100
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 0.8, 'curve': 128},
 {'age': 170, 'amount': 3.25, 'curve': 144},
 {'age': 180, 'amount': 0.75, 'curve': 144},
 {'age': 200, 'amount': 1.8, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x20 0x06 0x80 0x82 0xaa 0x90    \. .....
    0008   0x1e 0xb4 0x90 0x48 0xc8 0x90              ...H..
    decimal
             92   14   32    6  128  130  170  144
             30  180  144   72  200  144
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2014-03-09T17:28:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x20 0x00    ..(.(. .
    decimal
              1    0   40    0   40    0   32    0
    datetime (2014-03-09T17:28:54)
    0000   0x36 0xdc 0x51 0x69 0x0e                   6.Qi.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 71 BolusWizard 2014-03-09T17:37:26 head[2], body[15] op[0x5b]
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
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-03-09T17:37:26)
    0000   0x1a 0xe5 0x11 0x69 0x0e                   ...i.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x64         d....dd
    decimal
             30   80    0  120   50   80    0    0
            100    0    0    0    0  100  100
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 1.8, 'curve': 128},
 {'age': 179, 'amount': 3.25, 'curve': 144},
 {'age': 189, 'amount': 0.75, 'curve': 144},
 {'age': 209, 'amount': 1.8, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x0f 0x80 0x82 0xb3 0x90    \.H.....
    0008   0x1e 0xbd 0x90 0x48 0xd1 0x90              ...H..
    decimal
             92   14   72   15  128  130  179  144
             30  189  144   72  209  144
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2014-03-09T17:37:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x48 0x00    ..d.d.H.
    decimal
              1    0  100    0  100    0   72    0
    datetime (2014-03-09T17:37:26)
    0000   0x1a 0xe5 0x51 0x69 0x0e                   ..Qi.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 74 CalBGForPH 2014-03-09T18:40:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 166}
```
    op hex (2)
    0000   0x0a 0xa6                                  ..
    decimal
             10  166
    datetime (2014-03-09T18:40:13)
    0000   0x0d 0xe8 0x32 0x69 0x0e                   ..2i.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 75 Ian3F 2014-03-09T18:40:13 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-03-09T18:40:13)
    0000   0x0d 0xe8 0xd2 0x69 0x0e                   ...i.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
`end logs/ReadHistoryData-page-6.data: 76 records`
