## START analysis/sarak/raw//ReadHistoryData-page-15.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1b 0x34                                  .4
##### DEBUG DECIMAL
             27   52
#### RECORD 0 BolusWizard 2013-08-03T17:45:10 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-08-03T17:45:10)
    0000   0x8a 0x2d 0x11 0x03 0x0d                   .-...
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x58 0x00 0x00 0x0c 0x00 0x58 0x78         X....Xx
    decimal
             22   80    0  100   60  100    0    0
             88    0    0   12    0   88  120
    HOUR BITS: [0, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 112, 'amount': 0.45, 'curve': 192},
 {'age': 122, 'amount': 0.55, 'curve': 192},
 {'age': 66, 'amount': 3.8, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x12 0x70 0xc0 0x16 0x7a 0xc0    \..p..z.
    0008   0x98 0x42 0xd0                             .B.
    decimal
             92   11   18  112  192   22  122  192
            152   66  208
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-08-03T17:45:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x0c 0x00    ..X.X...
    decimal
              1    0   88    0   88    0   12    0
    datetime (2013-08-03T17:45:10)
    0000   0x8a 0x2d 0x51 0x03 0x0d                   .-Q..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 TempBasal 2013-08-03T19:09:00 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.25}
```
    op hex (2)
    0000   0x33 0x5a                                  3Z
    decimal
             51   90
    datetime (2013-08-03T19:09:00)
    0000   0x80 0x09 0x13 0x03 0x0d                   .....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8

#### RECORD 4 TempBasalDuration 2013-08-03T19:09:00 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 1440}
```
    op hex (2)
    0000   0x16 0x30                                  .0
    decimal
             22   48
    datetime (2013-08-03T19:09:00)
    0000   0x80 0x09 0x13 0x03 0x0d                   .....
    body (0)

#### RECORD 5 MResultTotals 2013-08-04T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x46                   ....F
    decimal
              7    0    0    4   70
    datetime (2013-08-04T00:00:00)
    0000   0x83 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 6 Sara6E 2013-08-04T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-04T00:00:00)
    0000   0x83 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0xa2 0x00 0x00 0x02 0x00 0x00    ........
    0008   0x04 0x46 0x02 0xbe 0x40 0x01 0x88 0x24    .F..@..$
    0010   0x00 0x32 0x00 0x58 0x00 0x00 0x00 0x98    .2.X....
    0018   0x00 0x98 0x01 0x00 0x01 0x03 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x6d    .......m
    0028   0xd7 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  162    0    0    2    0    0
              4   70    2  190   64    1  136   36
              0   50    0   88    0    0    0  152
              0  152    1    0    1    3    0    0
              0    0    0    0    0    0    0  109
            215    0    0    0    0    0    0    0
              0

#### RECORD 7 CalBGForPH 2013-08-04T09:57:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2013-08-04T09:57:02)
    0000   0x82 0x39 0x29 0x04 0x0d                   .9)..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 BolusWizard 2013-08-04T09:57:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 125,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 30,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 100}
```
    op hex (2)
    0000   0x5b 0x7d                                  [}
    decimal
             91  125
    datetime (2013-08-04T09:57:11)
    0000   0x8b 0x39 0x09 0x64 0x0d                   .9.d.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x78         d....dx
    decimal
             30   80    0  120   60  100    0    0
            100    0    0    0    0  100  120
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 Bolus 2013-08-04T09:57:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 10.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x00 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    0    0
    datetime (2013-08-04T09:57:11)
    0000   0x8b 0x39 0x49 0x64 0x0d                   .9Id.
    body (0)
    HOUR BITS: [0, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 Bolus 2013-08-04T10:28:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0x5c 0x00    ..D.D.\.
    decimal
              1    0   68    0   68    0   92    0
    datetime (2013-08-04T10:28:47)
    0000   0xaf 0x1c 0x4a 0x04 0x0d                   ..J..
    body (0)

#### RECORD 11 CalBGForPH 2013-08-04T12:27:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2013-08-04T12:27:07)
    0000   0x87 0x1b 0x2c 0x04 0x0d                   ..,..
    body (0)

#### RECORD 12 BolusWizard 2013-08-04T12:27:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 114,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2013-08-04T12:27:15)
    0000   0x8f 0x1b 0x0c 0x04 0x0d                   .....
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x40 0x00 0x00 0x1c 0x00 0x40 0x78         @....@x
    decimal
             20   80    0  120   60  100    0    0
             64    0    0   28    0   64  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 1.7, 'curve': 192},
 {'age': 154, 'amount': 2.5, 'curve': 192}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x7c 0xc0 0x64 0x9a 0xc0    \.D|.d..
    decimal
             92    8   68  124  192  100  154  192
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-08-04T12:27:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x1c 0x00    ..@.@...
    decimal
              1    0   64    0   64    0   28    0
    datetime (2013-08-04T12:27:15)
    0000   0x8f 0x1b 0x4c 0x04 0x0d                   ..L..
    body (0)

#### RECORD 15 CalBGForPH 2013-08-04T14:16:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 221}
```
    op hex (2)
    0000   0x0a 0xdd                                  ..
    decimal
             10  221
    datetime (2013-08-04T14:16:26)
    0000   0x9a 0x10 0x2e 0x04 0x0d                   .....
    body (0)

#### RECORD 16 BolusWizard 2013-08-04T14:16:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 221,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xdd                                  [.
    decimal
             91  221
    datetime (2013-08-04T14:16:29)
    0000   0x9d 0x10 0x0e 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x40 0x00    .P.x<d@.
    0008   0x00 0x00 0x00 0x14 0x00 0x2c 0x78         .....,x
    decimal
              0   80    0  120   60  100   64    0
              0    0    0   20    0   44  120
    DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 113, 'amount': 1.6, 'curve': 192},
 {'age': 233, 'amount': 1.7, 'curve': 192},
 {'age': 7, 'amount': 2.5, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x40 0x71 0xc0 0x44 0xe9 0xc0    \.@q.D..
    0008   0x64 0x07 0xd0                             d..
    decimal
             92   11   64  113  192   68  233  192
            100    7  208
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2013-08-04T14:16:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x14 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   20    0
    datetime (2013-08-04T14:16:29)
    0000   0x9d 0x10 0x4e 0x64 0x0d                   ..Nd.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 19 Bolus 2013-08-04T16:19:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x0c 0x00    .. . ...
    decimal
              1    0   32    0   32    0   12    0
    datetime (2013-08-04T16:19:06)
    0000   0x86 0x13 0x50 0x04 0x0d                   ..P..
    body (0)

#### RECORD 20 CalBGForPH 2013-08-04T16:29:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-04T16:29:02)
    0000   0x82 0x1d 0x30 0x04 0x0d                   ..0..
    body (0)

#### RECORD 21 BolusWizard 2013-08-04T16:29:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.0,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-04T16:29:38)
    0000   0xa6 0x1d 0x10 0x04 0x0d                   .....
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x28 0x00 0x28 0x78         (..(.(x
    decimal
             12   80    0  120   60  100    0    0
             40    0    0   40    0   40  120

#### RECORD 22 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 0.8, 'curve': 192},
 {'age': 136, 'amount': 1.1, 'curve': 192},
 {'age': 246, 'amount': 1.6, 'curve': 192},
 {'age': 110, 'amount': 1.7, 'curve': 208},
 {'age': 140, 'amount': 2.5, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x10 0xc0 0x2c 0x88 0xc0    \. ..,..
    0008   0x40 0xf6 0xc0 0x44 0x6e 0xd0 0x64 0x8c    @..Dn.d.
    0010   0xd0                                       .
    decimal
             92   17   32   16  192   44  136  192
             64  246  192   68  110  208  100  140
            208
    datetime (unknown)

    body (0)

#### RECORD 23 CalBGForPH 2013-08-04T16:48:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 100}
```
    op hex (2)
    0000   0x0a 0x64                                  .d
    decimal
             10  100
    datetime (2013-08-04T16:48:46)
    0000   0xae 0x30 0x30 0x04 0x0d                   .00..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 24 BolusWizard 2013-08-04T16:48:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 100,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
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
    0000   0x5b 0x64                                  [d
    decimal
             91  100
    datetime (2013-08-04T16:48:53)
    0000   0xb5 0x30 0x10 0x04 0x0d                   .0...
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x28 0x00 0x00 0x24 0x00 0x28 0x78         (..$.(x
    decimal
             12   80    0  120   60  100    0    0
             40    0    0   36    0   40  120
    HOUR BITS: [0, 0, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 0.8, 'curve': 192},
 {'age': 155, 'amount': 1.1, 'curve': 192},
 {'age': 9, 'amount': 1.6, 'curve': 208},
 {'age': 129, 'amount': 1.7, 'curve': 208},
 {'age': 159, 'amount': 2.5, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x20 0x23 0xc0 0x2c 0x9b 0xc0    \. #.,..
    0008   0x40 0x09 0xd0 0x44 0x81 0xd0 0x64 0x9f    @..D..d.
    0010   0xd0                                       .
    decimal
             92   17   32   35  192   44  155  192
             64    9  208   68  129  208  100  159
            208
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2013-08-04T16:48:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x24 0x00    ..(.(.$.
    decimal
              1    0   40    0   40    0   36    0
    datetime (2013-08-04T16:48:53)
    0000   0xb5 0x30 0x50 0x04 0x0d                   .0P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 27 CalBGForPH 2013-08-04T17:33:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 173}
```
    op hex (2)
    0000   0x0a 0xad                                  ..
    decimal
             10  173
    datetime (2013-08-04T17:33:44)
    0000   0xac 0x21 0x31 0x04 0x0d                   .!1..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 28 BolusWizard 2013-08-04T17:33:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 173,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 3.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xad                                  [.
    decimal
             91  173
    datetime (2013-08-04T17:33:47)
    0000   0xaf 0x21 0x11 0x04 0x0d                   .!...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x20 0x00    .P.d<d .
    0008   0x00 0x00 0x00 0x34 0x00 0x00 0x78         ...4..x
    decimal
              0   80    0  100   60  100   32    0
              0    0    0   52    0    0  120
    HOUR BITS: [0, 0, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 1.0, 'curve': 192},
 {'age': 80, 'amount': 0.8, 'curve': 192},
 {'age': 200, 'amount': 1.1, 'curve': 192},
 {'age': 54, 'amount': 1.6, 'curve': 208},
 {'age': 174, 'amount': 1.7, 'curve': 208},
 {'age': 204, 'amount': 2.5, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x28 0x32 0xc0 0x20 0x50 0xc0    \.(2. P.
    0008   0x2c 0xc8 0xc0 0x40 0x36 0xd0 0x44 0xae    ,..@6.D.
    0010   0xd0 0x64 0xcc 0xd0                        .d..
    decimal
             92   20   40   50  192   32   80  192
             44  200  192   64   54  208   68  174
            208  100  204  208
    datetime (unknown)

    body (0)

#### RECORD 30 CalBGForPH 2013-08-04T19:11:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-08-04T19:11:42)
    0000   0xaa 0x0b 0x33 0x04 0x0d                   ..3..
    body (0)

#### RECORD 31 BolusWizard 2013-08-04T19:11:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.8,
 'carb_input': 22,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-08-04T19:11:48)
    0000   0xb0 0x0b 0x13 0x64 0x0d                   ...d.
    body (15)
    hex
    0000   0x16 0x50 0x00 0x64 0x3c 0x64 0x2c 0x00    .P.d<d,.
    0008   0x58 0x00 0x00 0x08 0x00 0x7c 0x78         X....|x
    decimal
             22   80    0  100   60  100   44    0
             88    0    0    8    0  124  120
    DAY BITS: [0, 1, 1]
#### RECORD 32 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 148, 'amount': 1.0, 'curve': 192},
 {'age': 178, 'amount': 0.8, 'curve': 192},
 {'age': 42, 'amount': 1.1, 'curve': 208},
 {'age': 152, 'amount': 1.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x94 0xc0 0x20 0xb2 0xc0    \.(.. ..
    0008   0x2c 0x2a 0xd0 0x40 0x98 0xd0              ,*.@..
    decimal
             92   14   40  148  192   32  178  192
             44   42  208   64  152  208
    datetime (unknown)

    body (0)

#### RECORD 33 Bolus 2013-08-04T19:11:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 12.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x08 0x00    ..|.|...
    decimal
              1    0  124    0  124    0    8    0
    datetime (2013-08-04T19:11:48)
    0000   0xb0 0x0b 0x53 0x64 0x0d                   ..Sd.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 34 CalBGForPH 2013-08-04T20:42:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 205}
```
    op hex (2)
    0000   0x0a 0xcd                                  ..
    decimal
             10  205
    datetime (2013-08-04T20:42:29)
    0000   0x9d 0x2a 0x34 0x04 0x0d                   .*4..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 BolusWizard 2013-08-04T20:42:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 205,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.6,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcd                                  [.
    decimal
             91  205
    datetime (2013-08-04T20:42:33)
    0000   0xa1 0x2a 0x14 0x04 0x0d                   .*...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x38 0x00    .P.d<d8.
    0008   0x00 0x00 0x00 0x38 0x00 0x00 0x78         ...8..x
    decimal
              0   80    0  100   60  100   56    0
              0    0    0   56    0    0  120
    HOUR BITS: [0, 0, 1]
#### RECORD 36 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 89, 'amount': 1.35, 'curve': 192},
 {'age': 99, 'amount': 1.75, 'curve': 192},
 {'age': 239, 'amount': 1.0, 'curve': 192},
 {'age': 13, 'amount': 0.8, 'curve': 208},
 {'age': 133, 'amount': 1.1, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x36 0x59 0xc0 0x46 0x63 0xc0    \.6Y.Fc.
    0008   0x28 0xef 0xc0 0x20 0x0d 0xd0 0x2c 0x85    (.. ..,.
    0010   0xd0                                       .
    decimal
             92   17   54   89  192   70   99  192
             40  239  192   32   13  208   44  133
            208
    datetime (unknown)

    body (0)

#### RECORD 37 CalBGForPH 2013-08-04T21:14:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-08-04T21:14:00)
    0000   0x80 0x0e 0x35 0x04 0x0d                   ..5..
    body (0)

#### RECORD 38 BolusWizard 2013-08-04T21:14:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.8,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 52}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-08-04T21:14:08)
    0000   0x88 0x0e 0x15 0x04 0x0d                   .....
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x64 0x3c 0x64 0x30 0x00    .P.d<d0.
    0008   0x34 0x00 0x00 0x1c 0x00 0x48 0x78         4....Hx
    decimal
             13   80    0  100   60  100   48    0
             52    0    0   28    0   72  120

#### RECORD 39 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 121, 'amount': 1.35, 'curve': 192},
 {'age': 131, 'amount': 1.75, 'curve': 192},
 {'age': 15, 'amount': 1.0, 'curve': 208},
 {'age': 45, 'amount': 0.8, 'curve': 208},
 {'age': 165, 'amount': 1.1, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x36 0x79 0xc0 0x46 0x83 0xc0    \.6y.F..
    0008   0x28 0x0f 0xd0 0x20 0x2d 0xd0 0x2c 0xa5    (.. -.,.
    0010   0xd0                                       .
    decimal
             92   17   54  121  192   70  131  192
             40   15  208   32   45  208   44  165
            208
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-08-04T21:14:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x1c 0x00    ..H.H...
    decimal
              1    0   72    0   72    0   28    0
    datetime (2013-08-04T21:14:08)
    0000   0x88 0x0e 0x55 0x04 0x0d                   ..U..
    body (0)

#### RECORD 41 CalBGForPH 2013-08-04T21:53:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 317}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2013-08-04T21:53:37)
    0000   0xa5 0x35 0x35 0x04 0x8d                   .55..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 42 BolusWizard 2013-08-04T21:53:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 317,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 12.8,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3d                                  [=
    decimal
             91   61
    datetime (2013-08-04T21:53:40)
    0000   0xa8 0x35 0x15 0x04 0x0d                   .5...
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x3c 0x64 0x80 0x00    .Q.d<d..
    0008   0x00 0x00 0x00 0x48 0x00 0x38 0x78         ...H.8x
    decimal
              0   81    0  100   60  100  128    0
              0    0    0   72    0   56  120
    HOUR BITS: [0, 0, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 1.8, 'curve': 192},
 {'age': 160, 'amount': 1.35, 'curve': 192},
 {'age': 170, 'amount': 1.75, 'curve': 192},
 {'age': 54, 'amount': 1.0, 'curve': 208},
 {'age': 84, 'amount': 0.8, 'curve': 208},
 {'age': 204, 'amount': 1.1, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x28 0xc0 0x36 0xa0 0xc0    \.H(.6..
    0008   0x46 0xaa 0xc0 0x28 0x36 0xd0 0x20 0x54    F..(6. T
    0010   0xd0 0x2c 0xcc 0xd0                        .,..
    decimal
             92   20   72   40  192   54  160  192
             70  170  192   40   54  208   32   84
            208   44  204  208
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2013-08-04T21:53:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 5.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x48 0x00    ..8.8.H.
    decimal
              1    0   56    0   56    0   72    0
    datetime (2013-08-04T21:53:40)
    0000   0xa8 0x35 0x55 0x04 0x0d                   .5U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 45 BasalProfileStart 2013-08-05T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-08-05T00:00:00)
    0000   0x80 0x00 0x00 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x00 0x1d 0x00                             ...
    decimal
              0   29    0

#### RECORD 46 MResultTotals 2013-08-05T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xf3                   .....
    decimal
              7    0    0    4  243
    datetime (2013-08-05T00:00:00)
    0000   0x84 0x0d                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 47 Sara6E 2013-08-05T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2013-08-05T00:00:00)
    0000   0x84 0x0d                                  ..
    body (49)
    hex
    0000   0x05 0x00 0xad 0x00 0x00 0x0a 0x00 0x00    ........
    0008   0x04 0xf3 0x02 0x9b 0x35 0x02 0x58 0x2f    ....5.X/
    0010   0x00 0x61 0x00 0xcc 0x00 0x64 0x00 0xc4    .a...d..
    0018   0x00 0x64 0x03 0x02 0x02 0x02 0x04 0x00    .d......
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x64    .......d
    0028   0x3d 0x00 0x00 0x00 0x00 0x00 0x00 0x00    =.......
    0030   0x00                                       .
    decimal
              5    0  173    0    0   10    0    0
              4  243    2  155   53    2   88   47
              0   97    0  204    0  100    0  196
              0  100    3    2    2    2    4    0
              0    0    0    0    0    0    0  100
             61    0    0    0    0    0    0    0
              0

#### RECORD 48 BasalProfileStart 2013-08-05T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-08-05T04:00:00)
    0000   0x80 0x00 0x04 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x08 0x21 0x00                             .!.
    decimal
              8   33    0

#### RECORD 49 BasalProfileStart 2013-08-05T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-05T08:00:00)
    0000   0x80 0x00 0x08 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 50 BasalProfileStart 2013-08-05T09:11:11 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-08-05T09:11:11)
    0000   0x8b 0x0b 0x09 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x10 0x22 0x00                             .".
    decimal
             16   34    0

#### RECORD 51 Prime 2013-08-05T09:10:36 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.9, 'fixed': 0.9, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x09 0x00 0x09                   .....
    decimal
              3    0    9    0    9
    datetime (2013-08-05T09:10:36)
    0000   0xa4 0x0a 0x09 0x05 0x0d                   .....
    body (0)

#### RECORD 52 CalBGForPH 2013-08-05T09:12:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 111}
```
    op hex (2)
    0000   0x0a 0x6f                                  .o
    decimal
             10  111
    datetime (2013-08-05T09:12:59)
    0000   0xbb 0x0c 0x29 0x05 0x0d                   ..)..
    body (0)

#### RECORD 53 BolusWizard 2013-08-05T09:13:16 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 111,
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
    0000   0x5b 0x6f                                  [o
    decimal
             91  111
    datetime (2013-08-05T09:13:16)
    0000   0x90 0x0d 0x09 0x65 0x0d                   ...e.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x78         0....0x
    decimal
             15   80    0  120   60  100    0    0
             48    0    0    0    0   48  120
    DAY BITS: [0, 1, 1]
#### RECORD 54 Bolus 2013-08-05T09:13:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2013-08-05T09:13:16)
    0000   0x90 0x0d 0x49 0x65 0x0d                   ..Ie.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 55 CalBGForPH 2013-08-05T11:01:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2013-08-05T11:01:38)
    0000   0xa6 0x01 0x2b 0x05 0x8d                   ..+..
    body (0)
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 56 BolusWizard 2013-08-05T11:01:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 256,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.8,
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
    datetime (2013-08-05T11:01:45)
    0000   0xad 0x01 0x0b 0x05 0x0d                   .....
    body (15)
    hex
    0000   0x0e 0x51 0x00 0x78 0x3c 0x64 0x58 0x00    .Q.x<dX.
    0008   0x2c 0x00 0x00 0x10 0x00 0x74 0x78         ,....tx
    decimal
             14   81    0  120   60  100   88    0
             44    0    0   16    0  116  120

#### RECORD 57 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 1.2, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0x6c 0xc0                   \.0l.
    decimal
             92    5   48  108  192
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2013-08-05T11:01:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 11.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x10 0x00    ..t.t...
    decimal
              1    0  116    0  116    0   16    0
    datetime (2013-08-05T11:01:46)
    0000   0xae 0x01 0x4b 0x05 0x0d                   ..K..
    body (0)

#### RECORD 59 BasalProfileStart 2013-08-05T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-08-05T12:00:00)
    0000   0x80 0x00 0x0c 0x05 0x0d                   .....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0

#### RECORD 60 CalBGForPH 2013-08-05T12:37:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 250}
```
    op hex (2)
    0000   0x0a 0xfa                                  ..
    decimal
             10  250
    datetime (2013-08-05T12:37:11)
    0000   0x8b 0x25 0x2c 0x05 0x0d                   .%,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 BolusWizard 2013-08-05T12:37:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 250,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xfa                                  [.
    decimal
             91  250
    datetime (2013-08-05T12:37:14)
    0000   0x8e 0x25 0x0c 0x05 0x0d                   .%...
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x54 0x00    .P.x<dT.
    0008   0x00 0x00 0x00 0x2c 0x00 0x28 0x78         ...,.(x
    decimal
              0   80    0  120   60  100   84    0
              0    0    0   44    0   40  120
    HOUR BITS: [0, 0, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 1.05, 'curve': 192},
 {'age': 104, 'amount': 1.85, 'curve': 192},
 {'age': 204, 'amount': 1.2, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2a 0x5e 0xc0 0x4a 0x68 0xc0    \.*^.Jh.
    0008   0x30 0xcc 0xc0                             0..
    decimal
             92   11   42   94  192   74  104  192
             48  204  192
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2013-08-05T12:37:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x2c 0x00    ..(.(.,.
    decimal
              1    0   40    0   40    0   44    0
    datetime (2013-08-05T12:37:14)
    0000   0x8e 0x25 0x4c 0x05 0x0d                   .%L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 64 CalBGForPH 2013-08-05T13:02:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2013-08-05T13:02:20)
    0000   0x94 0x02 0x2d 0x05 0x0d                   ..-..
    body (0)

#### RECORD 65 BolusWizard 2013-08-05T13:02:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 127,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.4,
 'carb_input': 27,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 88}
```
    op hex (2)
    0000   0x5b 0x7f                                  [.
    decimal
             91  127
    datetime (2013-08-05T13:02:31)
    0000   0x9f 0x02 0x0d 0x05 0x0d                   .....
    body (15)
    hex
    0000   0x1b 0x50 0x00 0x78 0x3c 0x64 0x04 0x00    .P.x<d..
    0008   0x58 0x00 0x00 0x40 0x00 0x58 0x78         X..@.Xx
    decimal
             27   80    0  120   60  100    4    0
             88    0    0   64    0   88  120

#### RECORD 66 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 1.0, 'curve': 192},
 {'age': 119, 'amount': 1.05, 'curve': 192},
 {'age': 129, 'amount': 1.85, 'curve': 192},
 {'age': 229, 'amount': 1.2, 'curve': 192}]
```
    op hex (14)
    0000   0x5c 0x0e 0x28 0x1d 0xc0 0x2a 0x77 0xc0    \.(..*w.
    0008   0x4a 0x81 0xc0 0x30 0xe5 0xc0              J..0..
    decimal
             92   14   40   29  192   42  119  192
             74  129  192   48  229  192
    datetime (unknown)

    body (0)

#### RECORD 67 Bolus 2013-08-05T13:02:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x40 0x00    ..X.X.@.
    decimal
              1    0   88    0   88    0   64    0
    datetime (2013-08-05T13:02:31)
    0000   0x9f 0x02 0x4d 0x05 0x0d                   ..M..
    body (0)

#### RECORD 68 CalBGForPH 2013-08-05T15:13:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-08-05T15:13:32)
    0000   0xa0 0x0d 0x2f 0x05 0x0d                   ../..
    body (0)

#### RECORD 69 BolusWizard 2013-08-05T15:13:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 2.0,
 'carb_input': 13,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 40}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-08-05T15:13:38)
    0000   0xa6 0x0d 0x0f 0x05 0x0d                   .....
    body (15)
    hex
    0000   0x0d 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x28 0x00 0x00 0x14 0x00 0x40 0x78         (....@x
    decimal
             13   80    0  120   60  100   44    0
             40    0    0   20    0   64  120

`end analysis/sarak/raw//ReadHistoryData-page-15.data: 70 records`
