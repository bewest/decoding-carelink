## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-3.data
#### RECORD 0 Rewind 2013-07-29T14:00:16 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-29T14:00:16)
    0000   0x50 0xc0 0x0e 0x1d 0x0d                   P....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 Prime 2013-07-29T14:02:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x15                   .....
    decimal
              3    0    0    0   21
    datetime (2013-07-29T14:02:03)
    0000   0x43 0xc2 0x2e 0x1d 0x0d                   C....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 Prime 2013-07-29T14:02:26 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-29T14:02:26)
    0000   0x5a 0xc2 0x0e 0x1d 0x0d                   Z....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 3 CalBGForPH 2013-07-29T21:43:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-07-29T21:43:46)
    0000   0x6e 0xeb 0x35 0x1d 0x0d                   n.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 4 BolusWizard 2013-07-29T21:44:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 90,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5a                                  [Z
    decimal
             91   90
    datetime (2013-07-29T21:44:59)
    0000   0x7b 0xec 0x15 0x1d 0x0d                   {....
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0xfc 0x28 0xf0    5P.-j.(.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             53   80   13   45  106  252   40  240
              0    0    0   36  125
    HOUR BITS: [1, 1, 1]
#### RECORD 5 Bolus 2013-07-29T21:44:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-07-29T21:44:59)
    0000   0x7b 0xec 0x55 0x1d 0x0d                   {.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 ResultTotals (2013, 6, 29, 13, 13, 61) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x06                   .....
    decimal
              7    0    0    4    6
    datetime ((2013, 6, 29, 13, 13, 61))
    0000   0x7d 0x8d 0x6d 0x7d 0x8d                   }.m}.
    body (41)
    hex
    0000   0x05 0x00 0x5a 0x5a 0x5a 0x01 0x00 0x00    ..ZZZ...
    0008   0x04 0x06 0x03 0x76 0x56 0x00 0x90 0x0e    ...vV...
    0010   0x00 0x35 0x00 0x90 0x0e 0x00 0x90 0x64    .5.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0   90   90   90    1    0    0
              4    6    3  118   86    0  144   14
              0   53    0  144   14    0  144  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 7 CalBGForPH 2013-07-30T09:28:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2013-07-30T09:28:25)
    0000   0x59 0xdc 0x29 0x1e 0x0d                   Y.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 8 BolusWizard 2013-07-30T09:28:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 244,
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
    0000   0x5b 0xf4                                  [.
    decimal
             91  244
    datetime (2013-07-30T09:28:30)
    0000   0x5e 0xdc 0x09 0x1e 0x0d                   ^....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
              0   80   13   45  106   26    0    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 0]
#### RECORD 9 Bolus 2013-07-30T09:28:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-07-30T09:28:30)
    0000   0x5e 0xdc 0x49 0x1e 0x0d                   ^.I..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 PumpSuspend 2013-07-30T10:58:23 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-30T10:58:23)
    0000   0x57 0xfa 0x0a 0x1e 0x0d                   W....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 11 PumpResume 2013-07-30T11:24:16 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-30T11:24:16)
    0000   0x50 0xd8 0x0b 0x1e 0x0d                   P....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2013-07-30T12:01:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 59}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2013-07-30T12:01:11)
    0000   0x4b 0xc1 0x2c 0x1e 0x0d                   K.,..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 CalBGForPH 2013-07-30T13:22:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-07-30T13:22:58)
    0000   0x7a 0xd6 0x2d 0x1e 0x0d                   z.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 14 BolusWizard 2013-07-30T13:24:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-07-30T13:24:14)
    0000   0x4e 0xd8 0x0d 0x1e 0x0d                   N....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0xf9 0x21 0xf0    ,P.-j.!.
    0008   0x00 0x02 0x00 0x1a 0x7d                   ....}
    decimal
             44   80   13   45  106  249   33  240
              0    2    0   26  125
    HOUR BITS: [1, 1, 0]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 240, 'amount': 2.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x68 0xf0 0x04                   \.h..
    decimal
             92    5  104  240    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2013-07-30T13:24:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-07-30T13:24:14)
    0000   0x4e 0xd8 0x4d 0x1e 0x0d                   N.M..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 CalBGForPH 2013-07-30T22:10:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-07-30T22:10:05)
    0000   0x45 0xca 0x36 0x1e 0x0d                   E.6..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 18 BolusWizard 2013-07-30T22:10:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
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
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-07-30T22:10:10)
    0000   0x4a 0xca 0x16 0x1e 0x0d                   J....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x09 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106    9    0    0
              0    0    0    9  125
    HOUR BITS: [1, 1, 0]
#### RECORD 19 Bolus 2013-07-30T22:10:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-07-30T22:10:10)
    0000   0x4a 0xca 0x56 0x1e 0x0d                   J.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 20 CalBGForPH 2013-07-30T22:47:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2013-07-30T22:47:09)
    0000   0x49 0xef 0x36 0x1e 0x0d                   I.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 BolusWizard 2013-07-30T22:48:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 185,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.1,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb9                                  [.
    decimal
             91  185
    datetime (2013-07-30T22:48:11)
    0000   0x4b 0xf0 0x16 0x1e 0x0d                   K....
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x0d 0x2e 0x00    =P.-j...
    0008   0x00 0x08 0x00 0x33 0x7d                   ...3}
    decimal
             61   80   13   45  106   13   46    0
              0    8    0   51  125
    HOUR BITS: [1, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 0.9, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x24 0x2c 0x04                   \.$,.
    decimal
             92    5   36   44    4
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-07-30T22:48:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1, 'dual_component': '??', 'programmed': 5.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x33 0x33 0x00                        .33.
    decimal
              1   51   51    0
    datetime (2013-07-30T22:48:11)
    0000   0x4b 0xf0 0x56 0x1e 0x0d                   K.V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 ResultTotals (2013, 6, 30, 13, 13, 62) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x32                   ....2
    decimal
              7    0    0    5   50
    datetime ((2013, 6, 30, 13, 13, 62))
    0000   0x7e 0x8d 0x6d 0x7e 0x8d                   ~.m~.
    body (41)
    hex
    0000   0x05 0x00 0x92 0x3b 0xf4 0x05 0x00 0x00    ...;....
    0008   0x05 0x32 0x03 0x72 0x42 0x01 0xc0 0x22    .2.rB.."
    0010   0x00 0x69 0x01 0xc0 0x22 0x01 0x20 0x40    .i..". @
    0018   0x00 0xa0 0x24 0x00 0x00 0x00 0x04 0x01    ..$.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  146   59  244    5    0    0
              5   50    3  114   66    1  192   34
              0  105    1  192   34    1   32   64
              0  160   36    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 25 PumpSuspend 2013-07-31T14:56:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-31T14:56:39)
    0000   0x67 0xf8 0x0e 0x1f 0x0d                   g....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 PumpResume 2013-07-31T15:14:59 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-31T15:14:59)
    0000   0x7b 0xce 0x0f 0x1f 0x0d                   {....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 27 CalBGForPH 2013-07-31T23:09:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-31T23:09:44)
    0000   0x6c 0xc9 0x37 0x1f 0x0d                   l.7..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 28 BolusWizard 2013-07-31T23:10:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 102,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-07-31T23:10:51)
    0000   0x73 0xca 0x17 0x1f 0x0d                   s....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0xff 0x2a 0xf0    7P.-j.*.
    0008   0x00 0x00 0x00 0x29 0x7d                   ...)}
    decimal
             55   80   13   45  106  255   42  240
              0    0    0   41  125
    HOUR BITS: [1, 1, 0]
#### RECORD 29 Bolus 2013-07-31T23:10:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'dual_component': '??', 'programmed': 4.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2013-07-31T23:10:51)
    0000   0x73 0xca 0x57 0x1f 0x0d                   s.W..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 ResultTotals (2013, 6, 31, 13, 13, 63) head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x1c                   .....
    decimal
              7    0    0    4   28
    datetime ((2013, 6, 31, 13, 13, 63))
    0000   0x7f 0x8d 0x6d 0x7f 0x8d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x66 0x66 0x66 0x01 0x00 0x00    ..fff...
    0008   0x04 0x1c 0x03 0x78 0x54 0x00 0xa4 0x10    ...xT...
    0010   0x00 0x37 0x00 0xa4 0x10 0x00 0xa4 0x64    .7.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  102  102  102    1    0    0
              4   28    3  120   84    0  164   16
              0   55    0  164   16    0  164  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 31 CalBGForPH 2013-08-01T07:47:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 329}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2013-08-01T07:47:59)
    0000   0xbb 0x2f 0x27 0x01 0x8d                   ./'..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 32 BolusWizard 2013-08-01T07:48:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 45,
 '_byte[7]': 0,
 'bg': 329,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x49                                  [I
    decimal
             91   73
    datetime (2013-08-01T07:48:01)
    0000   0x81 0x30 0x07 0x01 0x0d                   .0...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2d 0x00 0x00    .Q.-j-..
    0008   0x00 0x00 0x00 0x2d 0x7d                   ...-}
    decimal
              0   81   13   45  106   45    0    0
              0    0    0   45  125
    HOUR BITS: [0, 0, 1]
#### RECORD 33 Bolus 2013-08-01T07:48:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-08-01T07:48:01)
    0000   0x81 0x30 0x47 0x01 0x0d                   .0G..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 34 CalBGForPH 2013-08-01T22:31:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-08-01T22:31:43)
    0000   0xab 0x1f 0x36 0x01 0x0d                   ..6..
    body (0)

#### RECORD 35 BolusWizard 2013-08-01T22:31:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.7,
 'carb_input': 67,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 5.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-08-01T22:31:58)
    0000   0xba 0x1f 0x16 0x01 0x0d                   .....
    body (13)
    hex
    0000   0x43 0x50 0x0d 0x2d 0x6a 0xfc 0x33 0xf0    CP.-j.3.
    0008   0x00 0x00 0x00 0x2f 0x7d                   .../}
    decimal
             67   80   13   45  106  252   51  240
              0    0    0   47  125

#### RECORD 36 Bolus 2013-08-01T22:31:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'dual_component': '??', 'programmed': 4.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2013-08-01T22:31:58)
    0000   0xba 0x1f 0x56 0x01 0x0d                   ..V..
    body (0)

#### RECORD 37 ResultTotals 2013-08-01T13:13:01 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf4                   .....
    decimal
              7    0    0    4  244
    datetime (2013-08-01T13:13:01)
    0000   0x81 0x0d 0x6d 0x81 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xd1 0x59 0x49 0x02 0x00 0x00    ...YI...
    0008   0x04 0xf4 0x03 0x84 0x47 0x01 0x70 0x1d    ....G.p.
    0010   0x00 0x43 0x01 0x70 0x1d 0x00 0xbc 0x33    .C.p...3
    0018   0x00 0xb4 0x31 0x00 0x00 0x00 0x02 0x01    ..1.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  209   89   73    2    0    0
              4  244    3  132   71    1  112   29
              0   67    1  112   29    0  188   51
              0  180   49    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 38 LowReservoir 2013-08-02T00:30:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-08-02T00:30:00)
    0000   0x80 0x1e 0x00 0x02 0x0d                   .....
    body (0)

#### RECORD 39 LowReservoir 2013-08-02T11:38:10 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-08-02T11:38:10)
    0000   0x8a 0x26 0x0b 0x02 0x0d                   .&...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 40 PumpSuspend 2013-08-02T14:07:42 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-08-02T14:07:42)
    0000   0xaa 0x07 0x0e 0x02 0x0d                   .....
    body (0)

#### RECORD 41 PumpResume 2013-08-02T14:22:59 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-08-02T14:22:59)
    0000   0xbb 0x16 0x0e 0x02 0x0d                   .....
    body (0)

#### RECORD 42 BolusWizard 2013-08-02T16:43:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 26,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
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
    datetime (2013-08-02T16:43:55)
    0000   0xb7 0x2b 0x10 0x02 0x0d                   .+...
    body (13)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
             26   80   13   45  106    0   20    0
              0    0    0   20  125
    HOUR BITS: [0, 0, 1]
#### RECORD 43 Bolus 2013-08-02T16:43:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-08-02T16:43:55)
    0000   0xb7 0x2b 0x50 0x02 0x0d                   .+P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 44 CalBGForPH 2013-08-02T19:13:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 65}
```
    op hex (2)
    0000   0x0a 0x41                                  .A
    decimal
             10   65
    datetime (2013-08-02T19:13:58)
    0000   0xba 0x0d 0x33 0x02 0x0d                   ..3..
    body (0)

#### RECORD 45 Rewind 2013-08-02T21:21:38 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-08-02T21:21:38)
    0000   0xa6 0x15 0x15 0x02 0x0d                   .....
    body (0)

#### RECORD 46 Prime 2013-08-02T21:23:17 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x11                   .....
    decimal
              3    0    0    0   17
    datetime (2013-08-02T21:23:17)
    0000   0x91 0x17 0x35 0x02 0x0d                   ..5..
    body (0)

#### RECORD 47 Prime 2013-08-02T21:23:49 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-08-02T21:23:49)
    0000   0xb1 0x17 0x15 0x02 0x0d                   .....
    body (0)

#### RECORD 48 CalBGForPH 2013-08-02T21:56:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2013-08-02T21:56:26)
    0000   0x9a 0x38 0x35 0x02 0x0d                   .85..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 BolusWizard 2013-08-02T21:57:39 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 146,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.3,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 4.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x92                                  [.
    decimal
             91  146
    datetime (2013-08-02T21:57:39)
    0000   0xa7 0x39 0x15 0x02 0x0d                   .9...
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0x04 0x31 0x00    @P.-j.1.
    0008   0x00 0x00 0x00 0x35 0x7d                   ...5}
    decimal
             64   80   13   45  106    4   49    0
              0    0    0   53  125
    HOUR BITS: [0, 0, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 57, 'amount': 1.9, 'curve': 20},
 {'age': 67, 'amount': 0.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x39 0x14 0x04 0x43 0x14    \.L9..C.
    decimal
             92    8   76   57   20    4   67   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-08-02T21:57:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3, 'dual_component': '??', 'programmed': 5.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x35 0x35 0x00                        .55.
    decimal
              1   53   53    0
    datetime (2013-08-02T21:57:39)
    0000   0xa7 0x39 0x55 0x02 0x0d                   .9U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 52 ResultTotals 2013-08-02T13:13:02 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9c                   .....
    decimal
              7    0    0    4  156
    datetime (2013-08-02T13:13:02)
    0000   0x82 0x0d 0x6d 0x82 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x6a 0x41 0x92 0x02 0x00 0x00    ..jA....
    0008   0x04 0x9c 0x03 0x78 0x4b 0x01 0x24 0x19    ...xK.$.
    0010   0x00 0x5a 0x01 0x24 0x19 0x01 0x14 0x5f    .Z.$..._
    0018   0x00 0x10 0x05 0x00 0x00 0x00 0x02 0x01    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  106   65  146    2    0    0
              4  156    3  120   75    1   36   25
              0   90    1   36   25    1   20   95
              0   16    5    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 53 CalBGForPH 2013-08-03T23:30:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 233}
```
    op hex (2)
    0000   0x0a 0xe9                                  ..
    decimal
             10  233
    datetime (2013-08-03T23:30:38)
    0000   0xa6 0x1e 0x37 0x03 0x0d                   ..7..
    body (0)

#### RECORD 54 BolusWizard 2013-08-03T23:30:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 233,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe9                                  [.
    decimal
             91  233
    datetime (2013-08-03T23:30:40)
    0000   0xa8 0x1e 0x17 0x03 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x18 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x18 0x7d                   ....}
    decimal
              0   80   13   45  106   24    0    0
              0    0    0   24  125

#### RECORD 55 Bolus 2013-08-03T23:30:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-08-03T23:30:40)
    0000   0xa8 0x1e 0x57 0x03 0x0d                   ..W..
    body (0)

#### RECORD 56 ResultTotals 2013-08-03T13:13:03 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0xe4                   .....
    decimal
              7    0    0    3  228
    datetime (2013-08-03T13:13:03)
    0000   0x83 0x0d 0x6d 0x83 0x0d                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0xe9 0xe9 0xe9 0x01 0x00 0x00    ........
    0008   0x03 0xe4 0x03 0x84 0x5a 0x00 0x60 0x0a    ....Z.`.
    0010   0x00 0x00 0x00 0x60 0x0a 0x00 0x00 0x00    ...`....
    0018   0x00 0x60 0x64 0x00 0x00 0x00 0x01 0x00    .`d.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  233  233  233    1    0    0
              3  228    3  132   90    0   96   10
              0    0    0   96   10    0    0    0
              0   96  100    0    0    0    1    0
              1    0    0   12    0  232    0    0
              0
    DAY BITS: [1, 0, 0]
#### RECORD 57 PumpSuspend 2013-08-04T09:21:59 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-08-04T09:21:59)
    0000   0xbb 0x15 0x09 0x04 0x0d                   .....
    body (0)

#### RECORD 58 PumpResume 2013-08-04T09:48:49 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-08-04T09:48:49)
    0000   0xb1 0x30 0x09 0x04 0x0d                   .0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 59 CalBGForPH 2013-08-04T11:21:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-08-04T11:21:56)
    0000   0xb8 0x15 0x2b 0x04 0x0d                   ..+..
    body (0)

#### RECORD 60 BolusWizard 2013-08-04T11:21:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-08-04T11:21:59)
    0000   0xbb 0x15 0x0b 0x04 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125

#### RECORD 61 Bolus 2013-08-04T11:22:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-08-04T11:22:00)
    0000   0x80 0x16 0x4b 0x04 0x0d                   ..K..
    body (0)

#### RECORD 62 CalBGForPH 2013-08-04T12:28:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-08-04T12:28:49)
    0000   0xb1 0x1c 0x2c 0x04 0x0d                   ..,..
    body (0)

#### RECORD 63 BolusWizard 2013-08-04T12:29:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 136,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 59,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 4.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x88                                  [.
    decimal
             91  136
    datetime (2013-08-04T12:29:32)
    0000   0xa0 0x1d 0x0c 0x04 0x0d                   .....
    body (13)
    hex
    0000   0x3b 0x50 0x0d 0x2d 0x6a 0x02 0x2d 0x00    ;P.-j.-.
    0008   0x00 0x0a 0x00 0x2d 0x7d                   ...-}
    decimal
             59   80   13   45  106    2   45    0
              0   10    0   45  125

#### RECORD 64 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 75, 'amount': 1.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x34 0x4b 0x04                   \.4K.
    decimal
             92    5   52   75    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-08-04T12:29:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'dual_component': '??', 'programmed': 4.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2013-08-04T12:29:32)
    0000   0xa0 0x1d 0x4c 0x04 0x0d                   ..L..
    body (0)

#### RECORD 66 CalBGForPH 2013-08-04T19:38:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2013-08-04T19:38:25)
    0000   0x99 0x26 0x33 0x04 0x0d                   .&3..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 67 BolusWizard 2013-08-04T19:38:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 7,
 '_byte[7]': 0,
 'bg': 160,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2013-08-04T19:38:27)
    0000   0x9b 0x26 0x13 0x04 0x0d                   .&...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x07 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d                   ....}
    decimal
              0   80   13   45  106    7    0    0
              0    0    0    7  125
    HOUR BITS: [0, 0, 1]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 178, 'amount': 4.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0xb2 0x14                   \....
    decimal
             92    5  180  178   20
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-08-04T19:38:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-08-04T19:38:27)
    0000   0x9b 0x26 0x53 0x04 0x0d                   .&S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 CalBGForPH 2013-08-04T20:47:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 117}
```
    op hex (2)
    0000   0x0a 0x75                                  .u
    decimal
             10  117
    datetime (2013-08-04T20:47:15)
    0000   0x8f 0x2f 0x34 0x04 0x0d                   ./4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 71 BolusWizard 2013-08-04T20:47:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 117,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 56,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x75                                  [u
    decimal
             91  117
    datetime (2013-08-04T20:47:29)
    0000   0x9d 0x2f 0x14 0x04 0x0d                   ./...
    body (13)
    hex
    0000   0x38 0x50 0x0d 0x2d 0x6a 0x00 0x2b 0x00    8P.-j.+.
    0008   0x00 0x06 0x00 0x2b 0x7d                   ...+}
    decimal
             56   80   13   45  106    0   43    0
              0    6    0   43  125
    HOUR BITS: [0, 0, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 73, 'amount': 0.7, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x1c 0x49 0x04                   \..I.
    decimal
             92    5   28   73    4
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-08-04T20:47:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-08-04T20:47:29)
    0000   0x9d 0x2f 0x54 0x04 0x0d                   ./T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 74 ResultTotals (2000, 8, 0, 0, 13, 4) head[5], body[4] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0x20                   .... 
    decimal
              7    0    0    5   32
    datetime ((2000, 8, 0, 0, 13, 4))
    0000   0x84 0x0d 0x00 0x00 0x00                   .....
    body (4)
    hex
    0000   0x00 0x00 0x30 0x7f                        ..0.
    decimal
              0    0   48  127

`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-3.data: 75 records`
