## START logs/ReadHistoryData-page-35.data
#### RECORD 0 BasalProfileStart 2013-07-03T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-03T04:00:00)
    0000   0x40 0xc0 0x04 0x03 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 1 BasalProfileStart 2013-07-03T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-03T08:00:00)
    0000   0x40 0xc0 0x08 0x03 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 2 TempBasal 2013-07-03T08:12:34 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 2.0}
```
    op hex (2)
    0000   0x33 0x50                                  3P
    decimal
             51   80
    datetime (2013-07-03T08:12:34)
    0000   0x62 0xcc 0x08 0x03 0x0d                   b....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 1, 0]
#### RECORD 3 TempBasalDuration 2013-07-03T08:12:34 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 90}
```
    op hex (2)
    0000   0x16 0x03                                  ..
    decimal
             22    3
    datetime (2013-07-03T08:12:34)
    0000   0x62 0xcc 0x08 0x03 0x0d                   b....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 4 BasalProfileStart 2013-07-03T09:42:34 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-03T09:42:34)
    0000   0x62 0xea 0x09 0x03 0x0d                   b....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 1]
#### RECORD 5 CalBGForPH 2013-07-03T10:50:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-07-03T10:50:12)
    0000   0x4c 0xf2 0x2a 0x03 0x0d                   L.*..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 BolusWizard 2013-07-03T10:50:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 106,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 25,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 80}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-07-03T10:50:30)
    0000   0x5e 0xf2 0x0a 0x63 0x0d                   ^..c.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x50 0x00 0x00 0x00 0x00 0x50 0x78         P....Px
    decimal
             25   80    0  120   60  100    0    0
             80    0    0    0    0   80  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 Bolus 2013-07-03T10:50:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2013-07-03T10:50:30)
    0000   0x5e 0xf2 0x4a 0x63 0x0d                   ^.Jc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 8 CalBGForPH 2013-07-03T11:50:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 191}
```
    op hex (2)
    0000   0x0a 0xbf                                  ..
    decimal
             10  191
    datetime (2013-07-03T11:50:39)
    0000   0x67 0xf2 0x2b 0x03 0x0d                   g.+..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 BolusWizard 2013-07-03T11:51:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 191,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 5.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbf                                  [.
    decimal
             91  191
    datetime (2013-07-03T11:51:13)
    0000   0x4d 0xf3 0x0b 0x63 0x0d                   M..c.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x00 0x00 0x00 0x38 0x00 0x00 0x78         ...8..x
    decimal
              0   80    0  120   60  100   44    0
              0    0    0   56    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 2.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x43 0xc0                   \.PC.
    decimal
             92    5   80   67  192
    datetime (unknown)

    body (0)

#### RECORD 11 BasalProfileStart 2013-07-03T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-03T12:00:00)
    0000   0x40 0xc0 0x0c 0x03 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 12 CalBGForPH 2013-07-03T13:15:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-07-03T13:15:40)
    0000   0x68 0xcf 0x2d 0x03 0x0d                   h.-..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 13 BolusWizard 2013-07-03T13:15:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-07-03T13:15:45)
    0000   0x6d 0xcf 0x0d 0x63 0x0d                   m..c.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x30 0x00    .P.x<d0.
    0008   0x00 0x00 0x00 0x0c 0x00 0x24 0x78         .....$x
    decimal
              0   80    0  120   60  100   48    0
              0    0    0   12    0   36  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 151, 'amount': 2.0, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x97 0xc0                   \.P..
    decimal
             92    5   80  151  192
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2013-07-03T13:15:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x0c 0x00    ..$.$...
    decimal
              1    0   36    0   36    0   12    0
    datetime (2013-07-03T13:15:45)
    0000   0x6d 0xcf 0x4d 0x63 0x0d                   m.Mc.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 16 CalBGForPH 2013-07-03T15:09:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 64}
```
    op hex (2)
    0000   0x0a 0x40                                  .@
    decimal
             10   64
    datetime (2013-07-03T15:09:15)
    0000   0x4f 0xc9 0x2f 0x03 0x0d                   O./..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 BolusWizard 2013-07-03T15:09:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 64,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 23.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0x40                                  [@
    decimal
             91   64
    datetime (2013-07-03T15:09:43)
    0000   0x6b 0xc9 0x0f 0x63 0x0d                   k..c.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0xe8 0x00    .P.x<d..
    0008   0x40 0xf8 0x00 0x0c 0x00 0x28 0x78         @....(x
    decimal
             20   80    0  120   60  100  232    0
             64  248    0   12    0   40  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 115, 'amount': 0.9, 'curve': 192},
 {'age': 9, 'amount': 2.0, 'curve': 208}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x73 0xc0 0x50 0x09 0xd0    \.$s.P..
    decimal
             92    8   36  115  192   80    9  208
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-07-03T15:09:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x0c 0x00    ..(.(...
    decimal
              1    0   40    0   40    0   12    0
    datetime (2013-07-03T15:09:43)
    0000   0x6b 0xc9 0x4f 0x63 0x0d                   k.Oc.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 CalBGForPH 2013-07-03T15:37:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-03T15:37:33)
    0000   0x61 0xe5 0x2f 0x03 0x0d                   a./..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 21 BolusWizard 2013-07-03T15:37:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 102,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 4.4,
 'carb_input': 11,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 36}
```
    op hex (2)
    0000   0x5b 0x66                                  [f
    decimal
             91  102
    datetime (2013-07-03T15:37:40)
    0000   0x68 0xe5 0x0f 0x03 0x0d                   h....
    body (15)
    hex
    0000   0x0b 0x50 0x00 0x78 0x3c 0x64 0x00 0x00    .P.x<d..
    0008   0x24 0x00 0x00 0x2c 0x00 0x24 0x78         $..,.$x
    decimal
             11   80    0  120   60  100    0    0
             36    0    0   44    0   36  120
    HOUR BITS: [1, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 1.0, 'curve': 192},
 {'age': 143, 'amount': 0.9, 'curve': 192},
 {'age': 37, 'amount': 2.0, 'curve': 208}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0x21 0xc0 0x24 0x8f 0xc0    \.(!.$..
    0008   0x50 0x25 0xd0                             P%.
    decimal
             92   11   40   33  192   36  143  192
             80   37  208
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2013-07-03T15:37:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x2c 0x00    ..$.$.,.
    decimal
              1    0   36    0   36    0   44    0
    datetime (2013-07-03T15:37:40)
    0000   0x68 0xe5 0x4f 0x03 0x0d                   h.O..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 CalBGForPH 2013-07-03T16:49:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2013-07-03T16:49:35)
    0000   0x63 0xf1 0x30 0x03 0x0d                   c.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 BolusWizard 2013-07-03T16:49:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 180,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.0,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb4                                  [.
    decimal
             91  180
    datetime (2013-07-03T16:49:42)
    0000   0x6a 0xf1 0x10 0x63 0x0d                   j..c.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x28 0x00    .P.x<d(.
    0008   0x00 0x00 0x00 0x24 0x00 0x04 0x78         ...$..x
    decimal
              0   80    0  120   60  100   40    0
              0    0    0   36    0    4  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 75, 'amount': 0.9, 'curve': 192},
 {'age': 105, 'amount': 1.0, 'curve': 192},
 {'age': 215, 'amount': 0.9, 'curve': 192},
 {'age': 109, 'amount': 2.0, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x24 0x4b 0xc0 0x28 0x69 0xc0    \.$K.(i.
    0008   0x24 0xd7 0xc0 0x50 0x6d 0xd0              $..Pm.
    decimal
             92   14   36   75  192   40  105  192
             36  215  192   80  109  208
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2013-07-03T16:49:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x24 0x00    ......$.
    decimal
              1    0   24    0   24    0   36    0
    datetime (2013-07-03T16:49:43)
    0000   0x6b 0xf1 0x50 0x63 0x0d                   k.Pc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 28 CalBGForPH 2013-07-03T17:41:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 216}
```
    op hex (2)
    0000   0x0a 0xd8                                  ..
    decimal
             10  216
    datetime (2013-07-03T17:41:42)
    0000   0x6a 0xe9 0x31 0x03 0x0d                   j.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 29 BolusWizard 2013-07-03T17:41:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 216,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 6.4,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd8                                  [.
    decimal
             91  216
    datetime (2013-07-03T17:41:46)
    0000   0x6e 0xe9 0x11 0x63 0x0d                   n..c.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x3c 0x64 0x40 0x00    .P.d<d@.
    0008   0x00 0x00 0x00 0x20 0x00 0x20 0x78         ... . x
    decimal
              0   80    0  100   60  100   64    0
              0    0    0   32    0   32  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 30 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 57, 'amount': 0.6, 'curve': 192},
 {'age': 127, 'amount': 0.9, 'curve': 192},
 {'age': 157, 'amount': 1.0, 'curve': 192},
 {'age': 11, 'amount': 0.9, 'curve': 208},
 {'age': 161, 'amount': 2.0, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x18 0x39 0xc0 0x24 0x7f 0xc0    \..9.$..
    0008   0x28 0x9d 0xc0 0x24 0x0b 0xd0 0x50 0xa1    (..$..P.
    0010   0xd0                                       .
    decimal
             92   17   24   57  192   36  127  192
             40  157  192   36   11  208   80  161
            208
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2013-07-03T17:41:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 3.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x20 0x00    .. . . .
    decimal
              1    0   32    0   32    0   32    0
    datetime (2013-07-03T17:41:46)
    0000   0x6e 0xe9 0x51 0x63 0x0d                   n.Qc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 CalBGForPH 2013-07-03T18:26:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 228}
```
    op hex (2)
    0000   0x0a 0xe4                                  ..
    decimal
             10  228
    datetime (2013-07-03T18:26:12)
    0000   0x4c 0xda 0x32 0x03 0x0d                   L.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 BolusWizard 2013-07-03T18:26:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 228,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 14,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 7.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 56}
```
    op hex (2)
    0000   0x5b 0xe4                                  [.
    decimal
             91  228
    datetime (2013-07-03T18:26:29)
    0000   0x5d 0xda 0x12 0x63 0x0d                   ]..c.
    body (15)
    hex
    0000   0x0e 0x50 0x00 0x64 0x3c 0x64 0x48 0x00    .P.d<dH.
    0008   0x38 0x00 0x00 0x24 0x00 0x5c 0x78         8..$.\x
    decimal
             14   80    0  100   60  100   72    0
             56    0    0   36    0   92  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 0.8, 'curve': 192},
 {'age': 102, 'amount': 0.6, 'curve': 192},
 {'age': 172, 'amount': 0.9, 'curve': 192},
 {'age': 202, 'amount': 1.0, 'curve': 192},
 {'age': 56, 'amount': 0.9, 'curve': 208},
 {'age': 206, 'amount': 2.0, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x20 0x34 0xc0 0x18 0x66 0xc0    \. 4..f.
    0008   0x24 0xac 0xc0 0x28 0xca 0xc0 0x24 0x38    $..(..$8
    0010   0xd0 0x50 0xce 0xd0                        .P..
    decimal
             92   20   32   52  192   24  102  192
             36  172  192   40  202  192   36   56
            208   80  206  208
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-07-03T18:26:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 9.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x24 0x00    ..\.\.$.
    decimal
              1    0   92    0   92    0   36    0
    datetime (2013-07-03T18:26:29)
    0000   0x5d 0xda 0x52 0x63 0x0d                   ].Rc.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 CalBGForPH 2013-07-03T20:56:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2013-07-03T20:56:20)
    0000   0x54 0xf8 0x34 0x03 0x0d                   T.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 37 CalBGForPH 2013-07-03T20:56:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-07-03T20:56:28)
    0000   0x5c 0xf8 0x34 0x03 0x0d                   \.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 38 BolusWizard 2013-07-03T20:56:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 105,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.2,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-07-03T20:56:39)
    0000   0x67 0xf8 0x14 0x63 0x0d                   g..c.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x54 0x00 0x00 0x0c 0x00 0x54 0x78         T....Tx
    decimal
             21   80    0  100   60  100    0    0
             84    0    0   12    0   84  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 152, 'amount': 2.3, 'curve': 192},
 {'age': 202, 'amount': 0.8, 'curve': 192},
 {'age': 252, 'amount': 0.6, 'curve': 192},
 {'age': 66, 'amount': 0.9, 'curve': 208},
 {'age': 96, 'amount': 1.0, 'curve': 208},
 {'age': 206, 'amount': 0.9, 'curve': 208}]
```
    op hex (20)
    0000   0x5c 0x14 0x5c 0x98 0xc0 0x20 0xca 0xc0    \.\.. ..
    0008   0x18 0xfc 0xc0 0x24 0x42 0xd0 0x28 0x60    ...$B.(`
    0010   0xd0 0x24 0xce 0xd0                        .$..
    decimal
             92   20   92  152  192   32  202  192
             24  252  192   36   66  208   40   96
            208   36  206  208
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2013-07-03T20:56:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 8.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x54 0x00 0x54 0x00 0x0c 0x00    ..T.T...
    decimal
              1    0   84    0   84    0   12    0
    datetime (2013-07-03T20:56:39)
    0000   0x67 0xf8 0x54 0x63 0x0d                   g.Tc.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 BasalProfileStart 2013-07-04T00:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2013-07-04T00:00:00)
    0000   0x40 0xc0 0x00 0x04 0x0d                   @....
    body (3)
    hex
    0000   0x00 0x20 0x00                             . .
    decimal
              0   32    0
    HOUR BITS: [1, 1, 0]
#### RECORD 42 ResultTotals (2000, 6, 0, 0, 13, 35) head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x80                   .....
    decimal
              7    0    0    4  128
    datetime ((2000, 6, 0, 0, 13, 35))
    0000   0x63 0x8d 0x00 0x00 0x00                   c....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 43 Sara6E (2000, 0, 0, 0, 0, 0) head[47], body[0] op[0x6e]

    op hex (47)
    0000   0x6e 0x63 0x8d 0x05 0x00 0x95 0x00 0x00    nc......
    0008   0x0a 0x00 0x00 0x04 0x80 0x02 0xd8 0x3f    .......?
    0010   0x01 0xa8 0x25 0x00 0x5b 0x00 0xf0 0x00    ..%.[...
    0018   0x5c 0x00 0x5c 0x00 0x00 0x04 0x03 0x01    \.\.....
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x40 0xe4 0x00 0x00 0x00         ..@....
    decimal
            110   99  141    5    0  149    0    0
             10    0    0    4  128    2  216   63
              1  168   37    0   91    0  240    0
             92    0   92    0    0    4    3    1
              0    0    0    0    0    0    0    0
              0    0   64  228    0    0    0
    datetime ((2000, 0, 0, 0, 0, 0))
    0000   0x00 0x00 0x00 0x00 0x00                   .....
    body (0)

#### RECORD 44 BasalProfileStart 2013-07-04T04:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2013-07-04T04:00:00)
    0000   0x40 0xc0 0x04 0x04 0x0d                   @....
    body (3)
    hex
    0000   0x08 0x1e 0x00                             ...
    decimal
              8   30    0
    HOUR BITS: [1, 1, 0]
#### RECORD 45 BasalProfileStart 2013-07-04T08:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-04T08:00:00)
    0000   0x40 0xc0 0x08 0x04 0x0d                   @....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 46 Rewind 2013-07-04T09:14:40 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-04T09:14:40)
    0000   0x68 0xce 0x09 0x04 0x0d                   h....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 47 Prime 2013-07-04T09:15:25 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 11.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x6e                   ....n
    decimal
              3    0    0    0  110
    datetime (2013-07-04T09:15:25)
    0000   0x59 0xcf 0x29 0x04 0x0d                   Y.)..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 BasalProfileStart 2013-07-04T09:16:36 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2013-07-04T09:16:36)
    0000   0x64 0xd0 0x09 0x04 0x0d                   d....
    body (3)
    hex
    0000   0x10 0x24 0x00                             .$.
    decimal
             16   36    0
    HOUR BITS: [1, 1, 0]
#### RECORD 49 Prime 2013-07-04T09:16:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-04T09:16:18)
    0000   0x52 0xd0 0x09 0x04 0x0d                   R....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 50 CalBGForPH 2013-07-04T10:16:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 190}
```
    op hex (2)
    0000   0x0a 0xbe                                  ..
    decimal
             10  190
    datetime (2013-07-04T10:16:25)
    0000   0x59 0xd0 0x2a 0x04 0x0d                   Y.*..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 51 BolusWizard 2013-07-04T10:16:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 190,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbe                                  [.
    decimal
             91  190
    datetime (2013-07-04T10:16:29)
    0000   0x5d 0xd0 0x0a 0x04 0x0d                   ]....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x2c 0x00    .P.x<d,.
    0008   0x00 0x00 0x00 0x00 0x00 0x2c 0x78         .....,x
    decimal
              0   80    0  120   60  100   44    0
              0    0    0    0    0   44  120
    HOUR BITS: [1, 1, 0]
#### RECORD 52 Bolus 2013-07-04T10:16:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x00 0x00    ..,.,...
    decimal
              1    0   44    0   44    0    0    0
    datetime (2013-07-04T10:16:29)
    0000   0x5d 0xd0 0x4a 0x04 0x0d                   ].J..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 53 CalBGForPH 2013-07-04T11:06:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 247}
```
    op hex (2)
    0000   0x0a 0xf7                                  ..
    decimal
             10  247
    datetime (2013-07-04T11:06:06)
    0000   0x46 0xc6 0x2b 0x04 0x0d                   F.+..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 54 BolusWizard 2013-07-04T11:06:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 247,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 3.6,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 8.4,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0xf7                                  [.
    decimal
             91  247
    datetime (2013-07-04T11:06:18)
    0000   0x52 0xc6 0x0b 0x64 0x0d                   R..d.
    body (15)
    hex
    0000   0x1d 0x50 0x00 0x78 0x3c 0x64 0x54 0x00    .P.x<dT.
    0008   0x60 0x00 0x00 0x24 0x00 0x90 0x78         `..$..x
    decimal
             29   80    0  120   60  100   84    0
             96    0    0   36    0  144  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 1.1, 'curve': 192}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0x34 0xc0                   \.,4.
    decimal
             92    5   44   52  192
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-07-04T11:06:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 14.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x24 0x00    ......$.
    decimal
              1    0  144    0  144    0   36    0
    datetime (2013-07-04T11:06:18)
    0000   0x52 0xc6 0x4b 0x64 0x0d                   R.Kd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 57 Bolus 2013-07-04T11:20:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.8, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x44 0x00 0x44 0x00 0xac 0x00    ..D.D...
    decimal
              1    0   68    0   68    0  172    0
    datetime (2013-07-04T11:20:03)
    0000   0x43 0xd4 0x4b 0x64 0x0d                   C.Kd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 58 BasalProfileStart 2013-07-04T12:00:00 head[2], body[3] op[0x7b]

    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2013-07-04T12:00:00)
    0000   0x40 0xc0 0x0c 0x04 0x0d                   @....
    body (3)
    hex
    0000   0x18 0x1d 0x00                             ...
    decimal
             24   29    0
    HOUR BITS: [1, 1, 0]
#### RECORD 59 CalBGForPH 2013-07-04T14:16:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 68}
```
    op hex (2)
    0000   0x0a 0x44                                  .D
    decimal
             10   68
    datetime (2013-07-04T14:16:42)
    0000   0x6a 0xd0 0x2e 0x04 0x0d                   j....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 60 BolusWizard 2013-07-04T14:17:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 68,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 29,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 23.2,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 24.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 96}
```
    op hex (2)
    0000   0x5b 0x44                                  [D
    decimal
             91   68
    datetime (2013-07-04T14:17:06)
    0000   0x46 0xd1 0x0e 0x64 0x0d                   F..d.
    body (15)
    hex
    0000   0x1d 0x50 0x00 0x78 0x3c 0x64 0xe8 0x00    .P.x<d..
    0008   0x60 0xf8 0x00 0x00 0x00 0x48 0x78         `....Hx
    decimal
             29   80    0  120   60  100  232    0
             96  248    0    0    0   72  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 61 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 183, 'amount': 1.7, 'curve': 192},
 {'age': 193, 'amount': 3.6, 'curve': 192},
 {'age': 243, 'amount': 1.1, 'curve': 192}]
```
    op hex (11)
    0000   0x5c 0x0b 0x44 0xb7 0xc0 0x90 0xc1 0xc0    \.D.....
    0008   0x2c 0xf3 0xc0                             ,..
    decimal
             92   11   68  183  192  144  193  192
             44  243  192
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2013-07-04T14:17:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 7.2, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2013-07-04T14:17:06)
    0000   0x46 0xd1 0x4e 0x64 0x0d                   F.Nd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 63 CalBGForPH 2013-07-04T14:35:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 207}
```
    op hex (2)
    0000   0x0a 0xcf                                  ..
    decimal
             10  207
    datetime (2013-07-04T14:35:45)
    0000   0x6d 0xe3 0x2e 0x04 0x0d                   m....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 64 BolusWizard 2013-07-04T14:36:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 207,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 7.2,
 'carb_input': 0,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.6,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcf                                  [.
    decimal
             91  207
    datetime (2013-07-04T14:36:04)
    0000   0x44 0xe4 0x0e 0x64 0x0d                   D..d.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x3c 0x64 0x38 0x00    .P.x<d8.
    0008   0x00 0x00 0x00 0x48 0x00 0x00 0x78         ...H..x
    decimal
              0   80    0  120   60  100   56    0
              0    0    0   72    0    0  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 1.8, 'curve': 192},
 {'age': 202, 'amount': 1.7, 'curve': 192},
 {'age': 212, 'amount': 3.6, 'curve': 192},
 {'age': 6, 'amount': 1.1, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x16 0xc0 0x44 0xca 0xc0    \.H..D..
    0008   0x90 0xd4 0xc0 0x2c 0x06 0xd0              ...,..
    decimal
             92   14   72   22  192   68  202  192
            144  212  192   44    6  208
    datetime (unknown)

    body (0)

#### RECORD 66 CalBGForPH 2013-07-04T14:45:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-07-04T14:45:49)
    0000   0x71 0xed 0x2e 0x04 0x0d                   q....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 67 BolusWizard 2013-07-04T14:46:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 196,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 6.8,
 'carb_input': 20,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 4.8,
 'sensitivity': 120,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 64}
```
    op hex (2)
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-07-04T14:46:04)
    0000   0x44 0xee 0x0e 0x64 0x0d                   D..d.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x3c 0x64 0x30 0x00    .P.x<d0.
    0008   0x40 0x00 0x00 0x44 0x00 0x40 0x78         @..D.@x
    decimal
             20   80    0  120   60  100   48    0
             64    0    0   68    0   64  120
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 68 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 1.8, 'curve': 192},
 {'age': 212, 'amount': 1.7, 'curve': 192},
 {'age': 222, 'amount': 3.6, 'curve': 192},
 {'age': 16, 'amount': 1.1, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x20 0xc0 0x44 0xd4 0xc0    \.H .D..
    0008   0x90 0xde 0xc0 0x2c 0x10 0xd0              ...,..
    decimal
             92   14   72   32  192   68  212  192
            144  222  192   44   16  208
    datetime (unknown)

    body (0)

#### RECORD 69 Bolus 2013-07-04T14:46:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 6.4, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x40 0x00 0x40 0x00 0x44 0x00    ..@.@.D.
    decimal
              1    0   64    0   64    0   68    0
    datetime (2013-07-04T14:46:04)
    0000   0x44 0xee 0x4e 0x64 0x0d                   D.Nd.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 CalBGForPH 2013-07-04T18:22:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-07-04T18:22:41)
    0000   0x69 0xd6 0x32 0x04 0x0d                   i.2..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 71 BolusWizard 2013-07-04T18:22:53 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 0.0,
 'carb_input': 4,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 16}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2013-07-04T18:22:53)
    0000   0x75 0xd6 0x12 0x64 0x0d                   u..d.
    body (15)
    hex
    0000   0x04 0x50 0x00 0x64 0x3c 0x64 0x00 0x00    .P.d<d..
    0008   0x10 0x00 0x00 0x00 0x00 0x10 0x78         ......x
    decimal
              4   80    0  100   60  100    0    0
             16    0    0    0    0   16  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 218, 'amount': 1.6, 'curve': 192},
 {'age': 248, 'amount': 1.8, 'curve': 192},
 {'age': 172, 'amount': 1.7, 'curve': 208},
 {'age': 182, 'amount': 3.6, 'curve': 208}]
```
    op hex (14)
    0000   0x5c 0x0e 0x40 0xda 0xc0 0x48 0xf8 0xc0    \.@..H..
    0008   0x44 0xac 0xd0 0x90 0xb6 0xd0              D.....
    decimal
             92   14   64  218  192   72  248  192
             68  172  208  144  182  208
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-07-04T18:22:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x00 0x00    ........
    decimal
              1    0   16    0   16    0    0    0
    datetime (2013-07-04T18:22:53)
    0000   0x75 0xd6 0x52 0x64 0x0d                   u.Rd.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 74 CalBGForPH 2013-07-04T19:00:59 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 198}
```
    op hex (2)
    0000   0x0a 0xc6                                  ..
    decimal
             10  198
    datetime (2013-07-04T19:00:59)
    0000   0x7b 0xc0 0x33 0x04 0x0d                   {.3..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 75 BolusWizard 2013-07-04T19:01:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'_byte[5]': 100,
 '_byte[7]': 0,
 'bg': 198,
 'bg_target_high': 0,
 'bg_target_low': 60,
 'bolus_estimate': 1.6,
 'carb_input': 21,
 'carb_ratio': 0,
 'correction_estimate': 0.4,
 'food_estimate': 5.2,
 'sensitivity': 100,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 84}
```
    op hex (2)
    0000   0x5b 0xc6                                  [.
    decimal
             91  198
    datetime (2013-07-04T19:01:19)
    0000   0x53 0xc1 0x13 0x64 0x0d                   S..d.
    body (15)
    hex
    0000   0x15 0x50 0x00 0x64 0x3c 0x64 0x34 0x00    .P.d<d4.
    0008   0x54 0x00 0x00 0x10 0x00 0x78 0x78         T....xx
    decimal
             21   80    0  100   60  100   52    0
             84    0    0   16    0  120  120
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 76 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 0.4, 'curve': 192},
 {'age': 1, 'amount': 1.6, 'curve': 208},
 {'age': 31, 'amount': 1.8, 'curve': 208},
 {'age': 211, 'amount': 1.7, 'curve': 208},
 {'age': 221, 'amount': 3.6, 'curve': 208}]
```
    op hex (17)
    0000   0x5c 0x11 0x10 0x2f 0xc0 0x40 0x01 0xd0    \../.@..
    0008   0x48 0x1f 0xd0 0x44 0xd3 0xd0 0x90 0xdd    H..D....
    0010   0xd0                                       .
    decimal
             92   17   16   47  192   64    1  208
             72   31  208   68  211  208  144  221
            208
    datetime (unknown)

    body (0)

#### RECORD 77 Base unknown head[2], body[0] op[0x8d]

    op hex (2)
    0000   0x8d 0x56                                  .V
    decimal
            141   86
    datetime (unknown)

    body (0)

`end logs/ReadHistoryData-page-35.data: 78 records`
