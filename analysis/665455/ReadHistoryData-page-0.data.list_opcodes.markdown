## START logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 348, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x04 0x64 0x03 0x84 0x50 0x00 0xe0 0x14    .d..P...
    0008   0x00 0x51 0x00 0xe0 0x14 0x00 0xe0 0x64    .Q.....d
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0018   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
##### DEBUG DECIMAL
              4  100    3  132   80    0  224   20
              0   81    0  224   20    0  224  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
#### RECORD 0 hack1 2013-08-17T03:01:14 head[46], body[0] op[0x6d]

    op hex (46)
    0000   0x6d 0x90 0x0d 0x05 0x00 0x78 0x5f 0x8e    m....x_.
    0008   0x03 0x00 0x00 0x04 0x94 0x03 0x70 0x4b    ......pK
    0010   0x01 0x24 0x19 0x00 0x60 0x01 0x24 0x19    .$..`.$.
    0018   0x01 0x18 0x60 0x00 0x0c 0x04 0x00 0x00    ..`.....
    0020   0x00 0x03 0x02 0x01 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00 0x0a 0xdb              ......
    decimal
            109  144   13    5    0  120   95  142
              3    0    0    4  148    3  112   75
              1   36   25    0   96    1   36   25
              1   24   96    0   12    4    0    0
              0    3    2    1    0    0   12    0
            232    0    0    0   10  219
    datetime (2013-08-17T03:01:14)
    0000   0x8e 0x01 0x23 0x11 0x0d                   ..#..
    body (0)

#### RECORD 1 BolusWizard 2013-08-17T03:01:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 20,
 '_byte[7]': 0,
 'bg': 219,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdb                                  [.
    decimal
             91  219
    datetime (2013-08-17T03:01:23)
    0000   0x97 0x01 0x03 0x11 0x0d                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125

#### RECORD 2 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 3.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x9c 0x47 0x14                   \..G.
    decimal
             92    5  156   71   20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2013-08-17T03:01:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-08-17T03:01:23)
    0000   0x97 0x01 0x43 0x11 0x0d                   ..C..
    body (0)

#### RECORD 4 CalBGForPH 2013-08-17T13:53:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2013-08-17T13:53:11)
    0000   0x8b 0x35 0x2d 0x11 0x0d                   .5-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 BolusWizard 2013-08-17T13:53:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 25,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 1.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4b                                  [K
    decimal
             91   75
    datetime (2013-08-17T13:53:25)
    0000   0x99 0x35 0x0d 0x11 0x0d                   .5...
    body (13)
    hex
    0000   0x19 0x50 0x0d 0x2d 0x6a 0xf9 0x13 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             25   80   13   45  106  249   19  240
              0    0    0   12  125
    HOUR BITS: [0, 0, 1]
#### RECORD 6 Bolus 2013-08-17T13:53:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-08-17T13:53:25)
    0000   0x99 0x35 0x4d 0x11 0x0d                   .5M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 7 CalBGForPH 2013-08-17T20:42:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 195}
```
    op hex (2)
    0000   0x0a 0xc3                                  ..
    decimal
             10  195
    datetime (2013-08-17T20:42:16)
    0000   0x90 0x2a 0x34 0x11 0x0d                   .*4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 BolusWizard 2013-08-17T20:42:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 195,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc3                                  [.
    decimal
             91  195
    datetime (2013-08-17T20:42:19)
    0000   0x93 0x2a 0x14 0x11 0x0d                   .*...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0    0    0   15  125
    HOUR BITS: [0, 0, 1]
#### RECORD 9 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 0.3, 'curve': 20},
 {'age': 162, 'amount': 0.9, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x0c 0x98 0x14 0x24 0xa2 0x14    \....$..
    decimal
             92    8   12  152   20   36  162   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2013-08-17T20:42:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'dual_component': '??', 'programmed': 1.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2013-08-17T20:42:19)
    0000   0x93 0x2a 0x54 0x11 0x0d                   .*T..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 CalBGForPH 2013-08-17T22:39:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-08-17T22:39:55)
    0000   0xb7 0x27 0x36 0x11 0x0d                   .'6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 12 BolusWizard 2013-08-17T22:40:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 118,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x76                                  [v
    decimal
             91  118
    datetime (2013-08-17T22:40:11)
    0000   0x8b 0x28 0x16 0x11 0x0d                   .(...
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    "P.-j...
    0008   0x00 0x07 0x00 0x1a 0x7d                   ....}
    decimal
             34   80   13   45  106    0   26    0
              0    7    0   26  125
    HOUR BITS: [0, 0, 1]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 1.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x7e 0x04                   \.<~.
    decimal
             92    5   60  126    4
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-08-17T22:40:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-08-17T22:40:11)
    0000   0x8b 0x28 0x56 0x11 0x0d                   .(V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 15 ResultTotals 2013-08-17T13:13:17 head[5], body[51] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9c                   .....
    decimal
              7    0    0    4  156
    datetime (2013-08-17T13:13:17)
    0000   0x91 0x0d 0x6d 0x91 0x0d                   ..m..
    body (51)
    hex
    0000   0x05 0x00 0x98 0x4b 0xdb 0x04 0x00 0x00    ...K....
    0008   0x04 0x9c 0x03 0x84 0x4c 0x01 0x18 0x18    ....L...
    0010   0x00 0x3b 0x01 0x18 0x18 0x00 0x98 0x36    .;.....6
    0018   0x00 0x80 0x2e 0x00 0x00 0x00 0x04 0x02    ........
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00 0x0a 0x55 0xb1 0x32 0x32 0x12 0x0d    ..U.22..
    0030   0x5b 0x55 0x97                             [U.
    decimal
              5    0  152   75  219    4    0    0
              4  156    3  132   76    1   24   24
              0   59    1   24   24    0  152   54
              0  128   46    0    0    0    4    2
              2    0    0   12    0  232    0    0
              0   10   85  177   50   50   18   13
             91   85  151
    DAY BITS: [1, 0, 0]
#### RECORD 16 TempBasal (2013, 0, 16, 31, 13, 18) head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.45}
```
    op hex (2)
    0000   0x33 0x12                                  3.
    decimal
             51   18
    datetime ((2013, 0, 16, 31, 13, 18))
    0000   0x12 0x0d 0x3f 0x50 0x0d                   ..?P.
    body (1)
    hex
    0000   0x2d                                       -
    decimal
             45
    DAY BITS: [0, 1, 0]
#### RECORD 17 Base (2000, 3, 0, 0, 48, 48) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0xfb                                  j.
    decimal
            106  251
    datetime ((2000, 3, 0, 0, 48, 48))
    0000   0x30 0xf0 0x00 0x00 0x00                   0....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 18 Base (2007, 0, 0, 11, 43, 1) head[2], body[0] op[0x2b]

    op hex (2)
    0000   0x2b 0x7d                                  +}
    decimal
             43  125
    datetime ((2007, 0, 0, 11, 43, 1))
    0000   0x01 0x2b 0x2b 0x00 0x97                   .++..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 19 TempBasal (2009, 0, 0, 27, 13, 18) head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.05}
```
    op hex (2)
    0000   0x33 0x52                                  3R
    decimal
             51   82
    datetime ((2009, 0, 0, 27, 13, 18))
    0000   0x12 0x0d 0x5b 0x00 0x89                   ..[..
    body (1)
    hex
    0000   0x1a                                       .
    decimal
             26
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 20 TempBasalDuration (2013, 0, 13, 16, 18, 13) head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 540}
```
    op hex (2)
    0000   0x16 0x12                                  ..
    decimal
             22   18
    datetime ((2013, 0, 13, 16, 18, 13))
    0000   0x0d 0x12 0x50 0x0d 0x2d                   ..P.-
    body (0)
    YEAR BITS: [0, 0, 1, 0]
#### RECORD 21 Base (2000, 0, 0, 0, 0, 13) head[2], body[0] op[0x6a]

    op hex (2)
    0000   0x6a 0x00                                  j.
    decimal
            106    0
    datetime ((2000, 0, 0, 0, 0, 13))
    0000   0x0d 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 22 Base (2004, 4, 20, 16, 8, 28) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x7d                                  .}
    decimal
             13  125
    datetime ((2004, 4, 20, 16, 8, 28))
    0000   0x5c 0x08 0x10 0xd4 0x04                   \....
    body (0)
    DAY BITS: [1, 1, 0]
#### RECORD 23 Base (2000, 0, 13, 13, 1, 4) head[2], body[0] op[0x9c]

    op hex (2)
    0000   0x9c 0xde                                  ..
    decimal
            156  222
    datetime ((2000, 0, 13, 13, 1, 4))
    0000   0x04 0x01 0x0d 0x0d 0x00                   .....
    body (0)

#### RECORD 24 Base (2000, 4, 7, 13, 18, 22) head[2], body[0] op[0x89]

    op hex (2)
    0000   0x89 0x1a                                  ..
    decimal
            137   26
    datetime ((2000, 4, 7, 13, 18, 22))
    0000   0x56 0x12 0x0d 0x07 0x00                   V....
    body (0)

#### RECORD 25 Base (2002, 6, 13, 13, 18, 36) head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0x04                                  ..
    decimal
              0    4
    datetime ((2002, 6, 13, 13, 18, 36))
    0000   0x64 0x92 0x0d 0x6d 0x92                   d..m.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 1]
#### RECORD 26 Base (2001, 1, 21, 21, 21, 0) head[2], body[0] op[0x0d]

    op hex (2)
    0000   0x0d 0x05                                  ..
    decimal
             13    5
    datetime ((2001, 1, 21, 21, 21, 0))
    0000   0x00 0x55 0x55 0x55 0x01                   .UUU.
    body (0)
    HOUR BITS: [0, 1, 0] DAY BITS: [0, 1, 0]
`end logs/ReadHistoryData-page-0.data: 27 records`
