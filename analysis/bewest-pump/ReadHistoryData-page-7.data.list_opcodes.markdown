## START logs/ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x68 0x81                                  h.
##### DEBUG DECIMAL
            104  129
#### RECORD 0 BolusWizard 2012-12-28T07:48:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.5,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 4.6,
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
    datetime (2012-12-28T07:48:24)
    0000   0xd8 0x30 0x07 0x1c 0x0c                   .0...
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0x09 0x2e 0x00    <P.-j...
    0008   0x00 0x00 0x00 0x37 0x7d                   ...7}
    decimal
             60   80   13   45  106    9   46    0
              0    0    0   55  125
    HOUR BITS: [0, 0, 1]
#### RECORD 1 LowReservoir 2012-12-28T07:49:08 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2012-12-28T07:49:08)
    0000   0xc8 0x31 0x07 0x1c 0x0c                   .1...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 2 Bolus 2012-12-28T07:48:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5, 'programmed': 5.5}
```
    op hex (4)
    0000   0x01 0x37 0x37 0x00                        .77.
    decimal
              1   55   55    0
    datetime (2012-12-28T07:48:24)
    0000   0xd8 0x30 0x47 0x1c 0x0c                   .0G..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 CalBGForPH 2012-12-28T09:43:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2012-12-28T09:43:32)
    0000   0xe0 0x2b 0x29 0x1c 0x0c                   .+)..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 4 CalBGForPH 2012-12-28T12:52:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2012-12-28T12:52:29)
    0000   0xdd 0x34 0x2c 0x1c 0x0c                   .4,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 5 LowReservoir 2012-12-28T13:08:10 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2012-12-28T13:08:10)
    0000   0xca 0x08 0x0d 0x1c 0x0c                   .....
    body (0)

#### RECORD 6 CalBGForPH 2012-12-28T13:30:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2012-12-28T13:30:56)
    0000   0xf8 0x1e 0x2d 0x1c 0x0c                   ..-..
    body (0)

#### RECORD 7 BolusWizard 2012-12-28T13:31:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 88,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x58                                  [X
    decimal
             91   88
    datetime (2012-12-28T13:31:16)
    0000   0xd0 0x1f 0x0d 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0xfc 0x24 0xf0    0P.-j.$.
    0008   0x00 0x00 0x00 0x20 0x7d                   ... }
    decimal
             48   80   13   45  106  252   36  240
              0    0    0   32  125

#### RECORD 8 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 5.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xdc 0x5b 0x14                   \..[.
    decimal
             92    5  220   91   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2012-12-28T13:31:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.2, 'programmed': 3.2}
```
    op hex (4)
    0000   0x01 0x20 0x20 0x00                        .  .
    decimal
              1   32   32    0
    datetime (2012-12-28T13:31:16)
    0000   0xd0 0x1f 0x4d 0x1c 0x0c                   ..M..
    body (0)

#### RECORD 10 Rewind 2012-12-28T16:50:31 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2012-12-28T16:50:31)
    0000   0xdf 0x32 0x10 0x1c 0x0c                   .2...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 11 Prime 2012-12-28T16:52:24 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.6, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x24                   ....$
    decimal
              3    0    0    0   36
    datetime (2012-12-28T16:52:24)
    0000   0xd8 0x34 0x30 0x1c 0x0c                   .40..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 12 Prime 2012-12-28T16:52:42 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2012-12-28T16:52:42)
    0000   0xea 0x34 0x10 0x1c 0x0c                   .4...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 CalBGForPH 2012-12-28T16:54:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 290}
```
    op hex (2)
    0000   0x0a 0x22                                  ."
    decimal
             10   34
    datetime (2012-12-28T16:54:04)
    0000   0xc4 0x36 0x30 0x1c 0x8c                   .60..
    body (0)
    HOUR BITS: [0, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 14 BolusWizard 2012-12-28T16:54:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 290,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x22                                  ["
    decimal
             91   34
    datetime (2012-12-28T16:54:13)
    0000   0xcd 0x36 0x10 0x1c 0x0c                   .6...
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x04 0x00 0x20 0x7d                   ... }
    decimal
              0   81   13   45  106   36    0    0
              0    4    0   32  125
    HOUR BITS: [0, 0, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 210, 'amount': 3.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x80 0xd2 0x04                   \....
    decimal
             92    5  128  210    4
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2012-12-28T16:54:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'programmed': 3.3}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2012-12-28T16:54:13)
    0000   0xcd 0x36 0x50 0x1c 0x0c                   .6P..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 17 CalBGForPH 2012-12-28T18:17:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 237}
```
    op hex (2)
    0000   0x0a 0xed                                  ..
    decimal
             10  237
    datetime (2012-12-28T18:17:35)
    0000   0xe3 0x11 0x32 0x1c 0x0c                   ..2..
    body (0)

#### RECORD 18 BolusWizard 2012-12-28T18:17:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 24,
 '_byte[7]': 0,
 'bg': 237,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xed                                  [.
    decimal
             91  237
    datetime (2012-12-28T18:17:40)
    0000   0xe8 0x11 0x12 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x18 0x00 0x00    .P.-j...
    0008   0x00 0x17 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106   24    0    0
              0   23    0    1  125

#### RECORD 19 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 83, 'amount': 3.3, 'curve': 4},
 {'age': 37, 'amount': 3.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0x53 0x04 0x80 0x25 0x14    \..S..%.
    decimal
             92    8  132   83    4  128   37   20
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2012-12-28T18:17:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-28T18:17:40)
    0000   0xe8 0x11 0x52 0x1c 0x0c                   ..R..
    body (0)

#### RECORD 21 CalBGForPH 2012-12-28T18:27:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 240}
```
    op hex (2)
    0000   0x0a 0xf0                                  ..
    decimal
             10  240
    datetime (2012-12-28T18:27:30)
    0000   0xde 0x1b 0x32 0x1c 0x0c                   ..2..
    body (0)

#### RECORD 22 BolusWizard 2012-12-28T18:28:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 25,
 '_byte[7]': 0,
 'bg': 240,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.5,
 'carb_input': 58,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 4.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xf0                                  [.
    decimal
             91  240
    datetime (2012-12-28T18:28:13)
    0000   0xcd 0x1c 0x12 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x3a 0x50 0x0d 0x2d 0x6a 0x19 0x2c 0x00    :P.-j.,.
    0008   0x00 0x18 0x00 0x2d 0x7d                   ...-}
    decimal
             58   80   13   45  106   25   44    0
              0   24    0   45  125

#### RECORD 23 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 14, 'amount': 0.3, 'curve': 4},
 {'age': 94, 'amount': 3.3, 'curve': 4},
 {'age': 48, 'amount': 3.2, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x0e 0x04 0x84 0x5e 0x04    \.....^.
    0008   0x80 0x30 0x14                             .0.
    decimal
             92   11   12   14    4  132   94    4
            128   48   20
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2012-12-28T18:28:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'programmed': 4.5}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2012-12-28T18:28:13)
    0000   0xcd 0x1c 0x52 0x1c 0x0c                   ..R..
    body (0)

#### RECORD 25 BolusWizard 2012-12-28T19:31:07 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 24,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
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
    datetime (2012-12-28T19:31:07)
    0000   0xc7 0x1f 0x13 0x1c 0x0c                   .....
    body (13)
    hex
    0000   0x18 0x50 0x0d 0x2d 0x6a 0x00 0x12 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             24   80   13   45  106    0   18    0
              0    0    0   18  125

#### RECORD 26 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 4.5, 'curve': 4},
 {'age': 77, 'amount': 0.3, 'curve': 4},
 {'age': 157, 'amount': 3.3, 'curve': 4},
 {'age': 111, 'amount': 3.2, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0xb4 0x43 0x04 0x0c 0x4d 0x04    \..C..M.
    0008   0x84 0x9d 0x04 0x80 0x6f 0x14              ....o.
    decimal
             92   14  180   67    4   12   77    4
            132  157    4  128  111   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2012-12-28T19:31:07 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-12-28T19:31:07)
    0000   0xc7 0x1f 0x53 0x1c 0x0c                   ..S..
    body (0)

#### RECORD 28 ResultTotals 2012-12-28T13:12:28 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x6c                   ....l
    decimal
              7    0    0    6  108
    datetime (2012-12-28T13:12:28)
    0000   0xdc 0x0c 0x6d 0xdc 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x10 0xb7 0x58 0x22 0x07 0x00 0x00    ...X"...
    0008   0x06 0x6c 0x03 0x84 0x37 0x02 0xe8 0x2d    .l..7..-
    0010   0x00 0xbe 0x02 0xe8 0x2d 0x02 0x30 0x4b    ....-.0K
    0018   0x00 0xb8 0x19 0x00 0x00 0x00 0x06 0x02    ........
    0020   0x02 0x02 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  183   88   34    7    0    0
              6  108    3  132   55    2  232   45
              0  190    2  232   45    2   48   75
              0  184   25    0    0    0    6    2
              2    2    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 29 CalBGForPH 2012-12-29T01:45:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2012-12-29T01:45:15)
    0000   0xcf 0x2d 0x21 0x1d 0x0c                   .-!..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 30 BolusWizard 2012-12-29T01:45:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 108,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6c                                  [l
    decimal
             91  108
    datetime (2012-12-29T01:45:24)
    0000   0xd8 0x2d 0x01 0x1d 0x0c                   .-...
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x00 0x21 0x00    +P.-j.!.
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
             43   80   13   45  106    0   33    0
              0    0    0   33  125
    HOUR BITS: [0, 0, 1]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 1.8, 'curve': 20},
 {'age': 185, 'amount': 4.5, 'curve': 20},
 {'age': 195, 'amount': 0.3, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x7d 0x14 0xb4 0xb9 0x14    \.H}....
    0008   0x0c 0xc3 0x14                             ...
    decimal
             92   11   72  125   20  180  185   20
             12  195   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2012-12-29T01:45:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'programmed': 3.3}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2012-12-29T01:45:24)
    0000   0xd8 0x2d 0x41 0x1d 0x0c                   .-A..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 33 CalBGForPH 2012-12-29T12:09:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2012-12-29T12:09:56)
    0000   0xf8 0x09 0x2c 0x1d 0x0c                   ..,..
    body (0)

#### RECORD 34 BolusWizard 2012-12-29T12:10:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 153,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2012-12-29T12:10:03)
    0000   0xc3 0x0a 0x0c 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x06 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    0    0    6  125

#### RECORD 35 Bolus 2012-12-29T12:10:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'programmed': 0.6}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2012-12-29T12:10:03)
    0000   0xc3 0x0a 0x4c 0x1d 0x0c                   ..L..
    body (0)

#### RECORD 36 PumpSuspend 2012-12-29T13:06:54 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-29T13:06:54)
    0000   0xf6 0x06 0x0d 0x1d 0x0c                   .....
    body (0)

#### RECORD 37 PumpResume 2012-12-29T13:45:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-29T13:45:03)
    0000   0xc3 0x2d 0x0d 0x1d 0x0c                   .-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 38 CalBGForPH 2012-12-29T14:46:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 75}
```
    op hex (2)
    0000   0x0a 0x4b                                  .K
    decimal
             10   75
    datetime (2012-12-29T14:46:53)
    0000   0xf5 0x2e 0x2e 0x1d 0x0c                   .....
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 39 BolusWizard 2012-12-29T14:47:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 75,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 3.6,
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
    datetime (2012-12-29T14:47:15)
    0000   0xcf 0x2f 0x0e 0x1d 0x0c                   ./...
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0xf9 0x24 0xf0    0P.-j.$.
    0008   0x00 0x02 0x00 0x1d 0x7d                   ....}
    decimal
             48   80   13   45  106  249   36  240
              0    2    0   29  125
    HOUR BITS: [0, 0, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 163, 'amount': 0.6, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x18 0xa3 0x04                   \....
    decimal
             92    5   24  163    4
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2012-12-29T14:47:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'programmed': 2.9}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2012-12-29T14:47:16)
    0000   0xd0 0x2f 0x4e 0x1d 0x0c                   ./N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 42 CalBGForPH 2012-12-29T18:14:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2012-12-29T18:14:36)
    0000   0xe4 0x0e 0x32 0x1d 0x0c                   ..2..
    body (0)

#### RECORD 43 BolusWizard 2012-12-29T18:14:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 6,
 '_byte[7]': 0,
 'bg': 153,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.3,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.6,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2012-12-29T18:14:44)
    0000   0xec 0x0e 0x12 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x06 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x03 0x7d                   ....}
    decimal
              0   80   13   45  106    6    0    0
              0    3    0    3  125

#### RECORD 44 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 210, 'amount': 2.9, 'curve': 4},
 {'age': 114, 'amount': 0.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x74 0xd2 0x04 0x18 0x72 0x14    \.t...r.
    decimal
             92    8  116  210    4   24  114   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2012-12-29T18:14:44 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-29T18:14:44)
    0000   0xec 0x0e 0x52 0x1d 0x0c                   ..R..
    body (0)

#### RECORD 46 CalBGForPH 2012-12-29T19:11:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2012-12-29T19:11:16)
    0000   0xd0 0x0b 0x33 0x1d 0x0c                   ..3..
    body (0)

#### RECORD 47 BolusWizard 2012-12-29T19:12:33 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.9,
 'carb_input': 64,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 4.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2012-12-29T19:12:33)
    0000   0xe1 0x0c 0x13 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x40 0x50 0x0d 0x2d 0x6a 0x0d 0x31 0x00    @P.-j.1.
    0008   0x00 0x03 0x00 0x3b 0x7d                   ...;}
    decimal
             64   80   13   45  106   13   49    0
              0    3    0   59  125

#### RECORD 48 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 58, 'amount': 0.3, 'curve': 4},
 {'age': 12, 'amount': 2.9, 'curve': 20},
 {'age': 172, 'amount': 0.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0c 0x3a 0x04 0x74 0x0c 0x14    \..:.t..
    0008   0x18 0xac 0x14                             ...
    decimal
             92   11   12   58    4  116   12   20
             24  172   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2012-12-29T19:12:33 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.9, 'programmed': 5.9}
```
    op hex (4)
    0000   0x01 0x3b 0x3b 0x00                        .;;.
    decimal
              1   59   59    0
    datetime (2012-12-29T19:12:33)
    0000   0xe1 0x0c 0x53 0x1d 0x0c                   ..S..
    body (0)

#### RECORD 50 BolusWizard 2012-12-29T19:40:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.5,
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
    datetime (2012-12-29T19:40:01)
    0000   0xc1 0x28 0x13 0x1d 0x0c                   .(...
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125
    HOUR BITS: [0, 0, 1]
#### RECORD 51 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 26, 'amount': 3.75, 'curve': 4},
 {'age': 36, 'amount': 2.15, 'curve': 4},
 {'age': 86, 'amount': 0.3, 'curve': 4},
 {'age': 40, 'amount': 2.9, 'curve': 20},
 {'age': 200, 'amount': 0.6, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x96 0x1a 0x04 0x56 0x24 0x04    \....V$.
    0008   0x0c 0x56 0x04 0x74 0x28 0x14 0x18 0xc8    .V.t(...
    0010   0x14                                       .
    decimal
             92   17  150   26    4   86   36    4
             12   86    4  116   40   20   24  200
             20
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2012-12-29T19:40:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-12-29T19:40:01)
    0000   0xc1 0x28 0x53 0x1d 0x0c                   .(S..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 53 BolusWizard 2012-12-29T21:23:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 1.5,
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
    datetime (2012-12-29T21:23:46)
    0000   0xee 0x17 0x15 0x1d 0x0c                   .....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0x00 0x0f 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
             20   80   13   45  106    0   15    0
              0    0    0   15  125

#### RECORD 54 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 109, 'amount': 1.5, 'curve': 4},
 {'age': 129, 'amount': 3.75, 'curve': 4},
 {'age': 139, 'amount': 2.15, 'curve': 4},
 {'age': 189, 'amount': 0.3, 'curve': 4},
 {'age': 143, 'amount': 2.9, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x3c 0x6d 0x04 0x96 0x81 0x04    \.<m....
    0008   0x56 0x8b 0x04 0x0c 0xbd 0x04 0x74 0x8f    V.....t.
    0010   0x14                                       .
    decimal
             92   17   60  109    4  150  129    4
             86  139    4   12  189    4  116  143
             20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2012-12-29T21:23:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'programmed': 1.5}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2012-12-29T21:23:46)
    0000   0xee 0x17 0x55 0x1d 0x0c                   ..U..
    body (0)

#### RECORD 56 ResultTotals 2012-12-29T13:12:29 head[5], body[41] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xe8                   .....
    decimal
              7    0    0    5  232
    datetime (2012-12-29T13:12:29)
    0000   0xdd 0x0c 0x6d 0xdd 0x0c                   ..m..
    body (41)
    hex
    0000   0x05 0x00 0x87 0x4b 0xba 0x05 0x00 0x00    ...K....
    0008   0x05 0xe8 0x03 0x68 0x3a 0x02 0x80 0x2a    ...h:..*
    0010   0x00 0xc3 0x02 0x80 0x2a 0x02 0x34 0x58    ....*.4X
    0018   0x00 0x4c 0x0c 0x00 0x00 0x00 0x07 0x04    .L......
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  135   75  186    5    0    0
              5  232    3  104   58    2  128   42
              0  195    2  128   42    2   52   88
              0   76   12    0    0    0    7    4
              2    1    0   12    0  232    0    0
              0
    DAY BITS: [1, 1, 0]
#### RECORD 57 CalBGForPH 2012-12-30T11:31:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 187}
```
    op hex (2)
    0000   0x0a 0xbb                                  ..
    decimal
             10  187
    datetime (2012-12-30T11:31:25)
    0000   0xd9 0x1f 0x2b 0x1e 0x0c                   ..+..
    body (0)

#### RECORD 58 BolusWizard 2012-12-30T11:32:00 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 187,
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
    0000   0x5b 0xbb                                  [.
    decimal
             91  187
    datetime (2012-12-30T11:32:00)
    0000   0xc0 0x20 0x0b 0x1e 0x0c                   . ...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0d 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0d 0x7d                   ....}
    decimal
              0   80   13   45  106   13    0    0
              0    0    0   13  125
    HOUR BITS: [0, 0, 1]
#### RECORD 59 Bolus 2012-12-30T11:32:00 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'programmed': 1.3}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2012-12-30T11:32:00)
    0000   0xc0 0x20 0x4b 0x1e 0x0c                   . K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 PumpSuspend 2012-12-30T11:48:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2012-12-30T11:48:01)
    0000   0xc1 0x30 0x0b 0x1e 0x0c                   .0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 61 PumpResume 2012-12-30T12:15:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2012-12-30T12:15:05)
    0000   0xc5 0x0f 0x0c 0x1e 0x0c                   .....
    body (0)

#### RECORD 62 CalBGForPH 2012-12-30T13:00:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 101}
```
    op hex (2)
    0000   0x0a 0x65                                  .e
    decimal
             10  101
    datetime (2012-12-30T13:00:29)
    0000   0xdd 0x00 0x2d 0x1e 0x0c                   ..-..
    body (0)

#### RECORD 63 BolusWizard 2012-12-30T13:01:16 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 255,
 '_byte[7]': 240,
 'bg': 101,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': -0.1,
 'food_estimate': 3.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x65                                  [e
    decimal
             91  101
    datetime (2012-12-30T13:01:16)
    0000   0xd0 0x01 0x0d 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0xff 0x23 0xf0    .P.-j.#.
    0008   0x00 0x08 0x00 0x22 0x7d                   ..."}
    decimal
             46   80   13   45  106  255   35  240
              0    8    0   34  125

#### RECORD 64 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 97, 'amount': 1.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x34 0x61 0x04                   \.4a.
    decimal
             92    5   52   97    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2012-12-30T13:01:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'programmed': 3.4}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2012-12-30T13:01:16)
    0000   0xd0 0x01 0x4d 0x1e 0x0c                   ..M..
    body (0)

#### RECORD 66 BolusWizard 2012-12-30T14:28:47 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.9,
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
    datetime (2012-12-30T14:28:47)
    0000   0xef 0x1c 0x0e 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x00 0x27 0x00    3P.-j.'.
    0008   0x00 0x00 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106    0   39    0
              0    0    0   39  125

#### RECORD 67 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 94, 'amount': 3.4, 'curve': 4},
 {'age': 184, 'amount': 1.3, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x88 0x5e 0x04 0x34 0xb8 0x04    \..^.4..
    decimal
             92    8  136   94    4   52  184    4
    datetime (unknown)

    body (0)

#### RECORD 68 Bolus 2012-12-30T14:28:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'programmed': 1.9}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2012-12-30T14:28:48)
    0000   0xf0 0x1c 0x8e 0x1e 0x0c                   .....
    body (0)

#### RECORD 69 Bolus 2012-12-30T14:30:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'programmed': 2.0}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x03                        ....
    decimal
              1   20   20    3
    datetime (2012-12-30T14:30:02)
    0000   0xc2 0x1e 0xae 0x1e 0x0c                   .....
    body (0)

#### RECORD 70 CalBGForPH 2012-12-30T17:18:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2012-12-30T17:18:17)
    0000   0xd1 0x12 0x31 0x1e 0x0c                   ..1..
    body (0)

#### RECORD 71 CalBGForPH 2012-12-30T19:43:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2012-12-30T19:43:55)
    0000   0xf7 0x2b 0x33 0x1e 0x0c                   .+3..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 72 CalBGForPH 2012-12-30T21:00:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 191}
```
    op hex (2)
    0000   0x0a 0xbf                                  ..
    decimal
             10  191
    datetime (2012-12-30T21:00:20)
    0000   0xd4 0x00 0x35 0x1e 0x0c                   ..5..
    body (0)

#### RECORD 73 BolusWizard 2012-12-30T21:00:43 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 191,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbf                                  [.
    decimal
             91  191
    datetime (2012-12-30T21:00:43)
    0000   0xeb 0x00 0x15 0x1e 0x0c                   .....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    0    0   14  125

#### RECORD 74 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 0.15, 'curve': 20},
 {'age': 60, 'amount': 0.2, 'curve': 20},
 {'age': 70, 'amount': 0.25, 'curve': 20},
 {'age': 80, 'amount': 0.2, 'curve': 20},
 {'age': 90, 'amount': 0.2, 'curve': 20},
 {'age': 100, 'amount': 0.25, 'curve': 20},
 {'age': 110, 'amount': 0.2, 'curve': 20},
 {'age': 120, 'amount': 0.25, 'curve': 20},
 {'age': 130, 'amount': 0.2, 'curve': 20},
 {'age': 140, 'amount': 2.0, 'curve': 20}]
```
    op hex (32)
    0000   0x5c 0x20 0x06 0x32 0x14 0x08 0x3c 0x14    \ .2..<.
    0008   0x0a 0x46 0x14 0x08 0x50 0x14 0x08 0x5a    .F..P..Z
    0010   0x14 0x0a 0x64 0x14 0x08 0x6e 0x14 0x0a    ..d..n..
    0018   0x78 0x14 0x08 0x82 0x14 0x50 0x8c 0x14    x....P..
    decimal
             92   32    6   50   20    8   60   20
             10   70   20    8   80   20    8   90
             20   10  100   20    8  110   20   10
            120   20    8  130   20   80  140   20
    datetime (unknown)

    body (0)

#### RECORD 75 Bolus 2012-12-30T21:00:43 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'programmed': 1.8}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2012-12-30T21:00:43)
    0000   0xeb 0x00 0x55 0x1e 0x0c                   ..U..
    body (0)

#### RECORD 76 CalBGForPH 2012-12-30T21:43:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2012-12-30T21:43:14)
    0000   0xce 0x2b 0x35 0x1e 0x0c                   .+5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 77 CalBGForPH 2012-12-30T21:44:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 210}
```
    op hex (2)
    0000   0x0a 0xd2                                  ..
    decimal
             10  210
    datetime (2012-12-30T21:44:49)
    0000   0xf1 0x2c 0x35 0x1e 0x0c                   .,5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 78 BolusWizard 2012-12-30T21:44:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 18,
 '_byte[7]': 0,
 'bg': 210,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.2,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd2                                  [.
    decimal
             91  210
    datetime (2012-12-30T21:44:54)
    0000   0xf6 0x2c 0x15 0x1e 0x0c                   .,...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x10 0x00 0x02 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0   16    0    2  125
    HOUR BITS: [0, 0, 1]
#### RECORD 79 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 1.8, 'curve': 4},
 {'age': 94, 'amount': 0.15, 'curve': 20},
 {'age': 104, 'amount': 0.2, 'curve': 20},
 {'age': 114, 'amount': 0.25, 'curve': 20},
 {'age': 124, 'amount': 0.2, 'curve': 20},
 {'age': 134, 'amount': 0.2, 'curve': 20},
 {'age': 144, 'amount': 0.25, 'curve': 20},
 {'age': 154, 'amount': 0.2, 'curve': 20},
 {'age': 164, 'amount': 0.25, 'curve': 20},
 {'age': 174, 'amount': 0.2, 'curve': 20},
 {'age': 184, 'amount': 2.0, 'curve': 20}]
```
    op hex (35)
    0000   0x5c 0x23 0x48 0x32 0x04 0x06 0x5e 0x14    \#H2..^.
    0008   0x08 0x68 0x14 0x0a 0x72 0x14 0x08 0x7c    .h..r..|
    0010   0x14 0x08 0x86 0x14 0x0a 0x90 0x14 0x08    ........
    0018   0x9a 0x14 0x0a 0xa4 0x14 0x08 0xae 0x14    ........
    0020   0x50 0xb8 0x14                             P..
    decimal
             92   35   72   50    4    6   94   20
              8  104   20   10  114   20    8  124
             20    8  134   20   10  144   20    8
            154   20   10  164   20    8  174   20
             80  184   20
    datetime (unknown)

    body (0)

#### RECORD 80 Bolus 2012-12-30T21:44:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.3, 'programmed': 0.3}
```
    op hex (4)
    0000   0x01 0x03 0x03 0x00                        ....
    decimal
              1    3    3    0
    datetime (2012-12-30T21:44:54)
    0000   0xf6 0x2c 0x55 0x1e 0x0c                   .,U..
    body (0)
    HOUR BITS: [0, 0, 1]
`end logs/ReadHistoryData-page-7.data: 81 records`
