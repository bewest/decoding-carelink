## START analysis/xiali/raw//ReadHistoryData-page-25.data
#### RECORD 0 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 3.2, 'curve': 4},
 {'age': 116, 'amount': 0.5, 'curve': 4},
 {'age': 40, 'amount': 1.4, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x80 0x2e 0x04 0x14 0x74 0x04    \.....t.
    0008   0x38 0x28 0x14                             8(.
    decimal
             92   11  128   46    4   20  116    4
             56   40   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-03-12T14:30:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-03-12T14:30:37)
    0000   0x25 0xde 0x4e 0x0c 0x0d                   %.N..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 CalBGForPH 2013-03-12T15:55:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-03-12T15:55:08)
    0000   0x08 0xf7 0x2f 0x0c 0x0d                   ../..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 CalBGForPH 2013-03-12T16:41:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2013-03-12T16:41:59)
    0000   0x3b 0xe9 0x30 0x0c 0x0d                   ;.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 CalBGForPH 2013-03-12T18:29:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 310}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2013-03-12T18:29:21)
    0000   0x15 0xdd 0x32 0x0c 0x8d                   ..2..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 5 BolusWizard 2013-03-12T18:29:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 41,
 '_byte[7]': 0,
 'bg': 310,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x36                                  [6
    decimal
             91   54
    datetime (2013-03-12T18:29:23)
    0000   0x17 0xdd 0x12 0x0c 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x29 0x00 0x00    .Q.-j)..
    0008   0x00 0x00 0x00 0x29 0x7d                   ...)}
    decimal
              0   81   13   45  106   41    0    0
              0    0    0   41  125
    HOUR BITS: [1, 1, 0]
#### RECORD 6 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 245, 'amount': 3.5, 'curve': 4},
 {'age': 29, 'amount': 3.2, 'curve': 20},
 {'age': 99, 'amount': 0.5, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x8c 0xf5 0x04 0x80 0x1d 0x14    \.......
    0008   0x14 0x63 0x14                             .c.
    decimal
             92   11  140  245    4  128   29   20
             20   99   20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2013-03-12T18:29:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'dual_component': '??', 'programmed': 4.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2013-03-12T18:29:23)
    0000   0x17 0xdd 0x52 0x0c 0x0d                   ..R..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 CalBGForPH 2013-03-12T21:10:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2013-03-12T21:10:44)
    0000   0x2c 0xca 0x35 0x0c 0x8d                   ,.5..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 9 BolusWizard 2013-03-12T21:11:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 276,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x14                                  [.
    decimal
             91   20
    datetime (2013-03-12T21:11:13)
    0000   0x0d 0xcb 0x15 0x0c 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x09 0x00 0x18 0x7d                   ....}
    decimal
              0   81   13   45  106   33    0    0
              0    9    0   24  125
    HOUR BITS: [1, 1, 0]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 167, 'amount': 4.1, 'curve': 4},
 {'age': 151, 'amount': 3.5, 'curve': 20},
 {'age': 191, 'amount': 3.2, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa4 0xa7 0x04 0x8c 0x97 0x14    \.......
    0008   0x80 0xbf 0x14                             ...
    decimal
             92   11  164  167    4  140  151   20
            128  191   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-03-12T21:11:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-03-12T21:11:13)
    0000   0x0d 0xcb 0x55 0x0c 0x0d                   ..U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2013-03-12T21:36:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2013-03-12T21:36:08)
    0000   0x08 0xe4 0x35 0x0c 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 CalBGForPH 2013-03-12T21:39:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 253}
```
    op hex (2)
    0000   0x0a 0xfd                                  ..
    decimal
             10  253
    datetime (2013-03-12T21:39:12)
    0000   0x0c 0xe7 0x35 0x0c 0x0d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 14 BolusWizard 2013-03-12T21:39:56 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 253,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 62,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 4.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfd                                  [.
    decimal
             91  253
    datetime (2013-03-12T21:39:56)
    0000   0x38 0xe7 0x15 0x0c 0x0d                   8....
    body (13)
    hex
    0000   0x3e 0x50 0x0d 0x2d 0x6a 0x1c 0x2f 0x00    >P.-j./.
    0008   0x00 0x22 0x00 0x2f 0x7d                   ."./}
    decimal
             62   80   13   45  106   28   47    0
              0   34    0   47  125
    HOUR BITS: [1, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 3.0, 'curve': 4},
 {'age': 195, 'amount': 4.1, 'curve': 4},
 {'age': 179, 'amount': 3.5, 'curve': 20},
 {'age': 219, 'amount': 3.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0x23 0x04 0xa4 0xc3 0x04    \.x#....
    0008   0x8c 0xb3 0x14 0x80 0xdb 0x14              ......
    decimal
             92   14  120   35    4  164  195    4
            140  179   20  128  219   20
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-03-12T21:39:56 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-03-12T21:39:56)
    0000   0x38 0xe7 0x55 0x0c 0x0d                   8.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 CalBGForPH 2013-03-12T21:59:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 258}
```
    op hex (2)
    0000   0x0a 0x02                                  ..
    decimal
             10    2
    datetime (2013-03-12T21:59:00)
    0000   0x00 0xfb 0x35 0x0c 0x8d                   ..5..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 18 CalBGForPH 2013-03-12T22:27:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 239}
```
    op hex (2)
    0000   0x0a 0xef                                  ..
    decimal
             10  239
    datetime (2013-03-12T22:27:25)
    0000   0x19 0xdb 0x36 0x0c 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 MResultTotals 2013-03-13T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xa0                   .....
    decimal
              7    0    0    6  160
    datetime (2013-03-13T00:00:00)
    0000   0x2c 0x8d                                  ,.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 Model522ResultTotals 2013-03-13T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-13T00:00:00)
    0000   0x2c 0x8d                                  ,.
    body (41)
    hex
    0000   0x05 0x10 0xd1 0x5d 0x36 0x0b 0x00 0x00    ...]6...
    0008   0x06 0xa0 0x03 0x70 0x34 0x03 0x30 0x30    ...p4.00
    0010   0x00 0x96 0x03 0x30 0x30 0x01 0xc8 0x38    ...00..8
    0018   0x01 0x68 0x2c 0x00 0x00 0x00 0x07 0x03    .h,.....
    0020   0x04 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  209   93   54   11    0    0
              6  160    3  112   52    3   48   48
              0  150    3   48   48    1  200   56
              1  104   44    0    0    0    7    3
              4    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 21 CalBGForPH 2013-03-13T00:28:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-03-13T00:28:57)
    0000   0x39 0xdc 0x20 0x0d 0x0d                   9. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 22 CalBGForPH 2013-03-13T00:34:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 112}
```
    op hex (2)
    0000   0x0a 0x70                                  .p
    decimal
             10  112
    datetime (2013-03-13T00:34:43)
    0000   0x2b 0xe2 0x20 0x0d 0x0d                   +. ..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 23 BolusWizard 2013-03-13T00:35:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 112,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 11,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x70                                  [p
    decimal
             91  112
    datetime (2013-03-13T00:35:16)
    0000   0x10 0xe3 0x00 0x0d 0x0d                   .....
    body (13)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x0c 0x00 0x08 0x7d                   ....}
    decimal
             11   80   13   45  106    0    8    0
              0   12    0    8  125
    HOUR BITS: [1, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 181, 'amount': 4.7, 'curve': 4},
 {'age': 211, 'amount': 3.0, 'curve': 4},
 {'age': 115, 'amount': 4.1, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xbc 0xb5 0x04 0x78 0xd3 0x04    \....x..
    0008   0xa4 0x73 0x14                             .s.
    decimal
             92   11  188  181    4  120  211    4
            164  115   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-03-13T00:35:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-03-13T00:35:16)
    0000   0x10 0xe3 0x40 0x0d 0x0d                   ..@..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 CalBGForPH 2013-03-13T08:45:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 277}
```
    op hex (2)
    0000   0x0a 0x15                                  ..
    decimal
             10   21
    datetime (2013-03-13T08:45:24)
    0000   0x18 0xed 0x28 0x0d 0x8d                   ..(..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 27 BolusWizard 2013-03-13T08:45:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 277,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x15                                  [.
    decimal
             91   21
    datetime (2013-03-13T08:45:27)
    0000   0x1b 0xed 0x08 0x0d 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x21 0x00 0x00    .Q.-j!..
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   33    0    0
              0    0    0   33  125
    HOUR BITS: [1, 1, 1]
#### RECORD 28 Bolus 2013-03-13T08:45:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-03-13T08:45:27)
    0000   0x1b 0xed 0x48 0x0d 0x0d                   ..H..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 29 PumpSuspend 2013-03-13T13:32:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-13T13:32:01)
    0000   0x01 0xe0 0x0d 0x0d 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 30 PumpResume 2013-03-13T14:01:39 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-13T14:01:39)
    0000   0x27 0xc1 0x0e 0x0d 0x0d                   '....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 31 CalBGForPH 2013-03-13T14:24:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2013-03-13T14:24:54)
    0000   0x36 0xd8 0x2e 0x0d 0x0d                   6....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 32 BolusWizard 2013-03-13T14:26:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 131,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 3.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2013-03-13T14:26:03)
    0000   0x03 0xda 0x0e 0x0d 0x0d                   .....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0x01 0x23 0x00    .P.-j.#.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             46   80   13   45  106    1   35    0
              0    0    0   36  125
    HOUR BITS: [1, 1, 0]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 3.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x84 0x56 0x14                   \..V.
    decimal
             92    5  132   86   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-03-13T14:26:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-03-13T14:26:03)
    0000   0x03 0xda 0x4e 0x0d 0x0d                   ..N..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 35 CalBGForPH 2013-03-13T16:07:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-03-13T16:07:53)
    0000   0x35 0xc7 0x30 0x0d 0x0d                   5.0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 36 CalBGForPH 2013-03-13T16:10:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 163}
```
    op hex (2)
    0000   0x0a 0xa3                                  ..
    decimal
             10  163
    datetime (2013-03-13T16:10:10)
    0000   0x0a 0xca 0x30 0x0d 0x0d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 BolusWizard 2013-03-13T16:10:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 163,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.8,
 'carb_input': 50,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 3.8,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa3                                  [.
    decimal
             91  163
    datetime (2013-03-13T16:10:22)
    0000   0x16 0xca 0x10 0x0d 0x0d                   .....
    body (13)
    hex
    0000   0x32 0x50 0x0d 0x2d 0x6a 0x08 0x26 0x00    2P.-j.&.
    0008   0x00 0x14 0x00 0x26 0x7d                   ...&}
    decimal
             50   80   13   45  106    8   38    0
              0   20    0   38  125
    HOUR BITS: [1, 1, 0]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 106, 'amount': 3.6, 'curve': 4},
 {'age': 190, 'amount': 3.3, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x90 0x6a 0x04 0x84 0xbe 0x14    \..j....
    decimal
             92    8  144  106    4  132  190   20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-03-13T16:10:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8, 'dual_component': '??', 'programmed': 3.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x26 0x26 0x00                        .&&.
    decimal
              1   38   38    0
    datetime (2013-03-13T16:10:22)
    0000   0x16 0xca 0x50 0x0d 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 40 CalBGForPH 2013-03-13T17:45:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2013-03-13T17:45:05)
    0000   0x05 0xed 0x31 0x0d 0x0d                   ..1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 MResultTotals 2013-03-14T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x3a                   ....:
    decimal
              7    0    0    5   58
    datetime (2013-03-14T00:00:00)
    0000   0x2d 0x8d                                  -.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 42 Model522ResultTotals 2013-03-14T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-14T00:00:00)
    0000   0x2d 0x8d                                  -.
    body (41)
    hex
    0000   0x05 0x10 0x9f 0x70 0x15 0x07 0x00 0x00    ...p....
    0008   0x05 0x3a 0x03 0x6e 0x42 0x01 0xcc 0x22    .:.nB.."
    0010   0x00 0x6b 0x01 0xcc 0x22 0x01 0x44 0x46    .k..".DF
    0018   0x00 0x88 0x1e 0x00 0x00 0x00 0x04 0x02    ........
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  159  112   21    7    0    0
              5   58    3  110   66    1  204   34
              0  107    1  204   34    1   68   70
              0  136   30    0    0    0    4    2
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 43 PumpSuspend 2013-03-14T11:58:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-03-14T11:58:33)
    0000   0x21 0xfa 0x0b 0x0e 0x0d                   !....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 PumpResume 2013-03-14T12:25:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-03-14T12:25:04)
    0000   0x04 0xd9 0x0c 0x0e 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 45 CalBGForPH 2013-03-14T12:58:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2013-03-14T12:58:10)
    0000   0x0a 0xfa 0x2c 0x0e 0x0d                   ..,..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 46 BolusWizard 2013-03-14T12:58:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 250,
 '_byte[7]': 240,
 'bg': 80,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': -0.6,
 'food_estimate': 4.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2013-03-14T12:58:36)
    0000   0x24 0xfa 0x0c 0x0e 0x0d                   $....
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0xfa 0x31 0xf0    @P.-j.1.
    0008   0x00 0x00 0x00 0x2b 0x7d                   ...+}
    decimal
             64   80   13   45  106  250   49  240
              0    0    0   43  125
    HOUR BITS: [1, 1, 1]
#### RECORD 47 Bolus 2013-03-14T12:58:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-03-14T12:58:36)
    0000   0x24 0xfa 0x4c 0x0e 0x0d                   $.L..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 48 CalBGForPH 2013-03-14T13:36:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 62}
```
    op hex (2)
    0000   0x0a 0x3e                                  .>
    decimal
             10   62
    datetime (2013-03-14T13:36:07)
    0000   0x07 0xe4 0x2d 0x0e 0x0d                   ..-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 49 LowReservoir 2013-03-14T15:47:22 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-03-14T15:47:22)
    0000   0x16 0xef 0x0f 0x0e 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 50 CalBGForPH 2013-03-14T16:45:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 289}
```
    op hex (2)
    0000   0x0a 0x21                                  .!
    decimal
             10   33
    datetime (2013-03-14T16:45:21)
    0000   0x15 0xed 0x30 0x0e 0x8d                   ..0..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 51 BolusWizard 2013-03-14T16:45:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 289,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x21                                  [!
    decimal
             91   33
    datetime (2013-03-14T16:45:24)
    0000   0x18 0xed 0x10 0x0e 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x03 0x00 0x21 0x7d                   ...!}
    decimal
              0   81   13   45  106   36    0    0
              0    3    0   33  125
    HOUR BITS: [1, 1, 1]
#### RECORD 52 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 231, 'amount': 4.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xac 0xe7 0x04                   \....
    decimal
             92    5  172  231    4
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-03-14T16:45:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-03-14T16:45:24)
    0000   0x18 0xed 0x50 0x0e 0x0d                   ..P..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 54 CalBGForPH 2013-03-14T21:32:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 250}
```
    op hex (2)
    0000   0x0a 0xfa                                  ..
    decimal
             10  250
    datetime (2013-03-14T21:32:32)
    0000   0x20 0xe0 0x35 0x0e 0x0d                    .5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 55 BolusWizard 2013-03-14T21:32:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 27,
 '_byte[7]': 0,
 'bg': 250,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfa                                  [.
    decimal
             91  250
    datetime (2013-03-14T21:32:45)
    0000   0x2d 0xe0 0x15 0x0e 0x0d                   -....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1b 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1b 0x7d                   ....}
    decimal
              0   80   13   45  106   27    0    0
              0    0    0   27  125
    HOUR BITS: [1, 1, 1]
#### RECORD 56 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 3.3, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x84 0x20 0x14                   \.. .
    decimal
             92    5  132   32   20
    datetime (unknown)

    body (0)

#### RECORD 57 LowReservoir 2013-03-14T21:33:33 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-03-14T21:33:33)
    0000   0x21 0xe1 0x15 0x0e 0x0d                   !....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 58 Bolus 2013-03-14T21:32:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'dual_component': '??', 'programmed': 3.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2013-03-14T21:32:45)
    0000   0x2d 0xe0 0x55 0x0e 0x0d                   -.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 59 BolusWizard 2013-03-14T22:12:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 8,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-03-14T22:12:27)
    0000   0x1b 0xcc 0x16 0x0e 0x0d                   .....
    body (13)
    hex
    0000   0x08 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              8   80   13   45  106    0    6    0
              0    0    0    6  125
    HOUR BITS: [1, 1, 0]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 1.1, 'curve': 4},
 {'age': 48, 'amount': 1.9, 'curve': 4},
 {'age': 72, 'amount': 3.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2c 0x26 0x04 0x4c 0x30 0x04    \.,&.L0.
    0008   0x84 0x48 0x14                             .H.
    decimal
             92   11   44   38    4   76   48    4
            132   72   20
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2013-03-14T22:12:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-03-14T22:12:27)
    0000   0x1b 0xcc 0x56 0x0e 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 62 CalBGForPH 2013-03-14T22:49:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 158}
```
    op hex (2)
    0000   0x0a 0x9e                                  ..
    decimal
             10  158
    datetime (2013-03-14T22:49:06)
    0000   0x06 0xf1 0x36 0x0e 0x0d                   ..6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 63 CalBGForPH 2013-03-14T22:51:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 158}
```
    op hex (2)
    0000   0x0a 0x9e                                  ..
    decimal
             10  158
    datetime (2013-03-14T22:51:45)
    0000   0x2d 0xf3 0x36 0x0e 0x0d                   -.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 64 BolusWizard 2013-03-14T22:52:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 158,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.2,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x9e                                  [.
    decimal
             91  158
    datetime (2013-03-14T22:52:08)
    0000   0x08 0xf4 0x16 0x0e 0x0d                   .....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x07 0x2a 0x00    7P.-j.*.
    0008   0x00 0x1a 0x00 0x2a 0x7d                   ...*}
    decimal
             55   80   13   45  106    7   42    0
              0   26    0   42  125
    HOUR BITS: [1, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 0.6, 'curve': 4},
 {'age': 78, 'amount': 1.1, 'curve': 4},
 {'age': 88, 'amount': 1.9, 'curve': 4},
 {'age': 112, 'amount': 3.3, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x18 0x30 0x04 0x2c 0x4e 0x04    \..0.,N.
    0008   0x4c 0x58 0x04 0x84 0x70 0x14              LX..p.
    decimal
             92   14   24   48    4   44   78    4
             76   88    4  132  112   20
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2013-03-14T22:52:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'dual_component': '??', 'programmed': 4.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2013-03-14T22:52:08)
    0000   0x08 0xf4 0x56 0x0e 0x0d                   ..V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 MResultTotals 2013-03-15T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xd8                   .....
    decimal
              7    0    0    5  216
    datetime (2013-03-15T00:00:00)
    0000   0x2e 0x8d                                  ..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 68 Model522ResultTotals 2013-03-15T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-15T00:00:00)
    0000   0x2e 0x8d                                  ..
    body (41)
    hex
    0000   0x05 0x10 0xa6 0x3e 0x21 0x06 0x00 0x00    ...>!...
    0008   0x05 0xd8 0x03 0x70 0x3b 0x02 0x68 0x29    ...p;.h)
    0010   0x00 0x7f 0x02 0x68 0x29 0x01 0x6c 0x3b    ...h).l;
    0018   0x00 0xfc 0x29 0x00 0x00 0x00 0x05 0x03    ..).....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  166   62   33    6    0    0
              5  216    3  112   59    2  104   41
              0  127    2  104   41    1  108   59
              0  252   41    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 69 CalBGForPH 2013-03-15T00:18:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 97}
```
    op hex (2)
    0000   0x0a 0x61                                  .a
    decimal
             10   97
    datetime (2013-03-15T00:18:45)
    0000   0x2d 0xd2 0x20 0x0f 0x0d                   -. ..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 70 Rewind 2013-03-15T05:03:26 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-03-15T05:03:26)
    0000   0x1a 0xc3 0x05 0x0f 0x0d                   .....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 71 Prime 2013-03-15T05:05:13 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x1d                   .....
    decimal
              3    0    0    0   29
    datetime (2013-03-15T05:05:13)
    0000   0x0d 0xc5 0x25 0x0f 0x0d                   ..%..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 72 Prime 2013-03-15T05:05:39 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-03-15T05:05:39)
    0000   0x27 0xc5 0x05 0x0f 0x0d                   '....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 73 CalBGForPH 2013-03-15T05:06:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 245}
```
    op hex (2)
    0000   0x0a 0xf5                                  ..
    decimal
             10  245
    datetime (2013-03-15T05:06:26)
    0000   0x1a 0xc6 0x25 0x0f 0x0d                   ..%..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 74 BolusWizard 2013-03-15T05:06:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 245,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf5                                  [.
    decimal
             91  245
    datetime (2013-03-15T05:06:28)
    0000   0x1c 0xc6 0x05 0x0f 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 0]
#### RECORD 75 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 116, 'amount': 1.45, 'curve': 20},
 {'age': 126, 'amount': 2.75, 'curve': 20},
 {'age': 166, 'amount': 0.6, 'curve': 20},
 {'age': 196, 'amount': 1.1, 'curve': 20},
 {'age': 206, 'amount': 1.9, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x3a 0x74 0x14 0x6e 0x7e 0x14    \.:t.n~.
    0008   0x18 0xa6 0x14 0x2c 0xc4 0x14 0x4c 0xce    ...,..L.
    0010   0x14                                       .
    decimal
             92   17   58  116   20  110  126   20
             24  166   20   44  196   20   76  206
             20
    datetime (unknown)

    body (0)

#### RECORD 76 Bolus 2013-03-15T05:06:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-03-15T05:06:28)
    0000   0x1c 0xc6 0x45 0x0f 0x0d                   ..E..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 77 CalBGForPH 2013-03-15T23:54:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 124}
```
    op hex (2)
    0000   0x0a 0x7c                                  .|
    decimal
             10  124
    datetime (2013-03-15T23:54:13)
    0000   0x0d 0xf6 0x37 0x0f 0x0d                   ..7..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 78 BolusWizard 2013-03-15T23:54:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 124,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.6,
 'carb_input': 73,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x7c                                  [|
    decimal
             91  124
    datetime (2013-03-15T23:54:26)
    0000   0x1a 0xf6 0x17 0x0f 0x0d                   .....
    body (13)
    hex
    0000   0x49 0x50 0x0d 0x2d 0x6a 0x00 0x38 0x00    IP.-j.8.
    0008   0x00 0x00 0x00 0x38 0x7d                   ...8}
    decimal
             73   80   13   45  106    0   56    0
              0    0    0   56  125
    HOUR BITS: [1, 1, 1]
#### RECORD 79 Bolus 2013-03-15T23:54:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x38 0x38 0x00                        .88.
    decimal
              1   56   56    0
    datetime (2013-03-15T23:54:26)
    0000   0x1a 0xf6 0x57 0x0f 0x0d                   ..W..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 80 MResultTotals 2013-03-16T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xca                   .....
    decimal
              7    0    0    4  202
    datetime (2013-03-16T00:00:00)
    0000   0x2f 0x8d                                  /.
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 81 Model522ResultTotals 2013-03-16T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-03-16T00:00:00)
    0000   0x2f 0x8d                                  /.
    body (41)
    hex
    0000   0x05 0x00 0x9b 0x61 0xf5 0x03 0x00 0x00    ...a....
    0008   0x04 0xca 0x03 0x82 0x49 0x01 0x48 0x1b    ....I.H.
    0010   0x00 0x49 0x01 0x48 0x1b 0x00 0xe0 0x44    .I.H...D
    0018   0x00 0x68 0x20 0x00 0x00 0x00 0x02 0x01    .h .....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  155   97  245    3    0    0
              4  202    3  130   73    1   72   27
              0   73    1   72   27    0  224   68
              0  104   32    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 82 CalBGForPH 2013-03-16T01:32:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-03-16T01:32:24)
    0000   0x18 0xe0 0x21 0x10 0x0d                   ..!..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 83 CalBGForPH 2013-03-16T13:51:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-03-16T13:51:43)
    0000   0x2b 0xf3 0x2d 0x10 0x0d                   +.-..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 84 BolusWizard 2013-03-16T13:52:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.5,
 'carb_input': 33,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-03-16T13:52:41)
    0000   0x29 0xf4 0x0d 0x10 0x0d                   )....
    body (13)
    hex
    0000   0x21 0x50 0x0d 0x2d 0x6a 0x00 0x19 0x00    !P.-j...
    0008   0x00 0x00 0x00 0x19 0x7d                   ....}
    decimal
             33   80   13   45  106    0   25    0
              0    0    0   25  125
    HOUR BITS: [1, 1, 1]
#### RECORD 85 Bolus 2013-03-16T13:52:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'dual_component': '??', 'programmed': 2.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2013-03-16T13:52:41)
    0000   0x29 0xf4 0x4d 0x10 0x0d                   ).M..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 86 Base unknown head[2], body[0] op[0x68]

    op hex (2)
    0000   0x68 0x94                                  h.
    decimal
            104  148
    datetime (unknown)

    body (0)

`end analysis/xiali/raw//ReadHistoryData-page-25.data: 87 records`
