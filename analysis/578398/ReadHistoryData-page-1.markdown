## START ReadHistoryData-page-1.data
#### STOPPING DOUBLE NULLS @ 988, found 34 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc0 0xcf                                  ..
##### DEBUG DECIMAL
            192  207
#### RECORD 0 UnabsorbedInsulinBolus unknown head[68], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 0.05},
 {'age': 12, 'amount': 0.1},
 {'age': 22, 'amount': 0.1},
 {'age': 32, 'amount': 0.15},
 {'age': 42, 'amount': 0.1},
 {'age': 52, 'amount': 0.1},
 {'age': 62, 'amount': 0.1},
 {'age': 72, 'amount': 0.1},
 {'age': 82, 'amount': 0.15},
 {'age': 92, 'amount': 0.1},
 {'age': 102, 'amount': 0.1},
 {'age': 112, 'amount': 0.1},
 {'age': 122, 'amount': 0.15},
 {'age': 132, 'amount': 0.1},
 {'age': 142, 'amount': 1.6},
 {'age': 152, 'amount': 1.95},
 {'age': 162, 'amount': 2.15},
 {'age': 192, 'amount': 2.1},
 {'age': 202, 'amount': 0.8},
 {'age': 222, 'amount': 2.0},
 {'age': 322, 'amount': 3.0},
 {'age': 362, 'amount': 2.4}]
```
    op hex (68)
    0000   0x5c 0x44 0x02 0x02 0x04 0x04 0x0c 0x04    \D......
    0008   0x04 0x16 0x04 0x06 0x20 0x04 0x04 0x2a    .... ..*
    0010   0x04 0x04 0x34 0x04 0x04 0x3e 0x04 0x04    ..4..>..
    0018   0x48 0x04 0x06 0x52 0x04 0x04 0x5c 0x04    H..R..\.
    0020   0x04 0x66 0x04 0x04 0x70 0x04 0x06 0x7a    .f..p..z
    0028   0x04 0x04 0x84 0x04 0x40 0x8e 0x04 0x4e    ....@..N
    0030   0x98 0x04 0x56 0xa2 0x04 0x54 0xc0 0x04    ..V..T..
    0038   0x20 0xca 0x04 0x50 0xde 0x04 0x78 0x42     ..P..xB
    0040   0x14 0x60 0x6a 0x14                        .`j.
    decimal
             92   68    2    2    4    4   12    4
              4   22    4    6   32    4    4   42
              4    4   52    4    4   62    4    4
             72    4    6   82    4    4   92    4
              4  102    4    4  112    4    6  122
              4    4  132    4   64  142    4   78
            152    4   86  162    4   84  192    4
             32  202    4   80  222    4  120   66
             20   96  106   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-04-28T14:11:55 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'duration': 0, 'programmed': 2.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2015-04-28T14:11:55)
    0000   0x77 0x0b 0x4e 0x1c 0x0f                   w.N..
    body (0)

#### RECORD 2 CalBGForPH 2015-04-28T14:52:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 54}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2015-04-28T14:52:02)
    0000   0x42 0x34 0x2e 0x7c 0x0f                   B4.|.
    body (0)

#### RECORD 3 BGReceived 2015-04-28T14:52:02 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 54, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2015-04-28T14:52:02)
    0000   0x42 0x34 0xce 0x7c 0x0f                   B4.|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 4 SensorAlert 2015-04-28T15:17:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose', 'alarm_type': 102, 'amount': 79}
```
    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-04-28T15:17:38)
    0000   0x66 0x11 0x2f 0xbc 0x0f                   f./..
    body (0)

#### RECORD 5 BolusWizard 2015-04-28T18:39:26 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.3,
 'carb_input': 26,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 4.3,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-28T18:39:26)
    0000   0x5a 0x27 0x12 0x1c 0x0f                   Z'...
    body (13)
    hex
    0000   0x1a 0x50 0x06 0x28 0x5a 0x00 0x2b 0x00    .P.(Z.+.
    0008   0x00 0x00 0x00 0x2b 0x78                   ...+x
    decimal
             26   80    6   40   90    0   43    0
              0    0    0   43  120

#### RECORD 6 UnabsorbedInsulinBolus unknown head[65], body[0] op[0x5c]
###### DECODED
```python
[{'age': 250, 'amount': 0.1},
 {'age': 260, 'amount': 0.15},
 {'age': 270, 'amount': 2.6},
 {'age': 280, 'amount': 0.1},
 {'age': 290, 'amount': 0.1},
 {'age': 300, 'amount': 0.15},
 {'age': 310, 'amount': 0.1},
 {'age': 320, 'amount': 0.1},
 {'age': 330, 'amount': 0.1},
 {'age': 340, 'amount': 0.1},
 {'age': 350, 'amount': 0.15},
 {'age': 360, 'amount': 0.1},
 {'age': 370, 'amount': 0.1},
 {'age': 380, 'amount': 0.1},
 {'age': 390, 'amount': 0.15},
 {'age': 400, 'amount': 0.1},
 {'age': 410, 'amount': 1.6},
 {'age': 420, 'amount': 1.95},
 {'age': 430, 'amount': 2.15},
 {'age': 460, 'amount': 2.1},
 {'age': 470, 'amount': 0.8}]
```
    op hex (65)
    0000   0x5c 0x41 0x04 0xfa 0x04 0x06 0x04 0x14    \A......
    0008   0x68 0x0e 0x14 0x04 0x18 0x14 0x04 0x22    h......"
    0010   0x14 0x06 0x2c 0x14 0x04 0x36 0x14 0x04    ..,..6..
    0018   0x40 0x14 0x04 0x4a 0x14 0x04 0x54 0x14    @..J..T.
    0020   0x06 0x5e 0x14 0x04 0x68 0x14 0x04 0x72    .^..h..r
    0028   0x14 0x04 0x7c 0x14 0x06 0x86 0x14 0x04    ..|.....
    0030   0x90 0x14 0x40 0x9a 0x14 0x4e 0xa4 0x14    ..@..N..
    0038   0x56 0xae 0x14 0x54 0xcc 0x14 0x20 0xd6    V..T.. .
    0040   0x14                                       .
    decimal
             92   65    4  250    4    6    4   20
            104   14   20    4   24   20    4   34
             20    6   44   20    4   54   20    4
             64   20    4   74   20    4   84   20
              6   94   20    4  104   20    4  114
             20    4  124   20    6  134   20    4
            144   20   64  154   20   78  164   20
             86  174   20   84  204   20   32  214
             20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2015-04-28T18:39:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'duration': 0, 'programmed': 4.3, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2015-04-28T18:39:26)
    0000   0x5a 0x27 0x52 0x1c 0x0f                   Z'R..
    body (0)

#### RECORD 8 BolusWizard 2015-04-28T19:17:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.0,
 'carb_input': 48,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 8.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-28T19:17:01)
    0000   0x41 0x11 0x13 0x1c 0x0f                   A....
    body (13)
    hex
    0000   0x30 0x50 0x06 0x28 0x5a 0x00 0x50 0x00    0P.(Z.P.
    0008   0x00 0x00 0x00 0x50 0x78                   ...Px
    decimal
             48   80    6   40   90    0   80    0
              0    0    0   80  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[62], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 4.3},
 {'age': 288, 'amount': 0.1},
 {'age': 298, 'amount': 0.15},
 {'age': 308, 'amount': 2.6},
 {'age': 318, 'amount': 0.1},
 {'age': 328, 'amount': 0.1},
 {'age': 338, 'amount': 0.15},
 {'age': 348, 'amount': 0.1},
 {'age': 358, 'amount': 0.1},
 {'age': 368, 'amount': 0.1},
 {'age': 378, 'amount': 0.1},
 {'age': 388, 'amount': 0.15},
 {'age': 398, 'amount': 0.1},
 {'age': 408, 'amount': 0.1},
 {'age': 418, 'amount': 0.1},
 {'age': 428, 'amount': 0.15},
 {'age': 438, 'amount': 0.1},
 {'age': 448, 'amount': 1.6},
 {'age': 458, 'amount': 1.95},
 {'age': 468, 'amount': 2.15}]
```
    op hex (62)
    0000   0x5c 0x3e 0xac 0x26 0x04 0x04 0x20 0x14    \>.&.. .
    0008   0x06 0x2a 0x14 0x68 0x34 0x14 0x04 0x3e    .*.h4..>
    0010   0x14 0x04 0x48 0x14 0x06 0x52 0x14 0x04    ..H..R..
    0018   0x5c 0x14 0x04 0x66 0x14 0x04 0x70 0x14    \..f..p.
    0020   0x04 0x7a 0x14 0x06 0x84 0x14 0x04 0x8e    .z......
    0028   0x14 0x04 0x98 0x14 0x04 0xa2 0x14 0x06    ........
    0030   0xac 0x14 0x04 0xb6 0x14 0x40 0xc0 0x14    .....@..
    0038   0x4e 0xca 0x14 0x56 0xd4 0x14              N..V..
    decimal
             92   62  172   38    4    4   32   20
              6   42   20  104   52   20    4   62
             20    4   72   20    6   82   20    4
             92   20    4  102   20    4  112   20
              4  122   20    6  132   20    4  142
             20    4  152   20    4  162   20    6
            172   20    4  182   20   64  192   20
             78  202   20   86  212   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2015-04-28T19:17:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'duration': 0, 'programmed': 4.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2015-04-28T19:17:02)
    0000   0x42 0x11 0x93 0x1c 0x0f                   B....
    body (0)

#### RECORD 11 BolusWizard 2015-04-28T23:01:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.0,
 'carb_input': 30,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 3.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-28T23:01:02)
    0000   0x42 0x01 0x17 0x1c 0x0f                   B....
    body (13)
    hex
    0000   0x1e 0x50 0x0a 0x28 0x5a 0x00 0x1e 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x1e 0x78                   ....x
    decimal
             30   80   10   40   90    0   30    0
              0    0    0   30  120

#### RECORD 12 UnabsorbedInsulinBolus unknown head[74], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 0.15},
 {'age': 22, 'amount': 0.15},
 {'age': 32, 'amount': 0.15},
 {'age': 42, 'amount': 0.15},
 {'age': 52, 'amount': 0.15},
 {'age': 62, 'amount': 0.15},
 {'age': 72, 'amount': 0.15},
 {'age': 82, 'amount': 0.1},
 {'age': 92, 'amount': 0.15},
 {'age': 102, 'amount': 0.15},
 {'age': 112, 'amount': 0.15},
 {'age': 122, 'amount': 0.15},
 {'age': 132, 'amount': 0.15},
 {'age': 142, 'amount': 0.15},
 {'age': 152, 'amount': 0.15},
 {'age': 162, 'amount': 0.15},
 {'age': 172, 'amount': 0.15},
 {'age': 182, 'amount': 0.15},
 {'age': 192, 'amount': 0.15},
 {'age': 202, 'amount': 0.1},
 {'age': 212, 'amount': 0.15},
 {'age': 222, 'amount': 1.75},
 {'age': 232, 'amount': 2.9},
 {'age': 262, 'amount': 4.3}]
```
    op hex (74)
    0000   0x5c 0x4a 0x06 0x0c 0x04 0x06 0x16 0x04    \J......
    0008   0x06 0x20 0x04 0x06 0x2a 0x04 0x06 0x34    . ..*..4
    0010   0x04 0x06 0x3e 0x04 0x06 0x48 0x04 0x04    ..>..H..
    0018   0x52 0x04 0x06 0x5c 0x04 0x06 0x66 0x04    R..\..f.
    0020   0x06 0x70 0x04 0x06 0x7a 0x04 0x06 0x84    .p..z...
    0028   0x04 0x06 0x8e 0x04 0x06 0x98 0x04 0x06    ........
    0030   0xa2 0x04 0x06 0xac 0x04 0x06 0xb6 0x04    ........
    0038   0x06 0xc0 0x04 0x04 0xca 0x04 0x06 0xd4    ........
    0040   0x04 0x46 0xde 0x04 0x74 0xe8 0x04 0xac    .F..t...
    0048   0x06 0x14                                  ..
    decimal
             92   74    6   12    4    6   22    4
              6   32    4    6   42    4    6   52
              4    6   62    4    6   72    4    4
             82    4    6   92    4    6  102    4
              6  112    4    6  122    4    6  132
              4    6  142    4    6  152    4    6
            162    4    6  172    4    6  182    4
              6  192    4    4  202    4    6  212
              4   70  222    4  116  232    4  172
              6   20
    datetime (unknown)

    body (0)

#### RECORD 13 Bolus 2015-04-28T19:20:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'duration': 240, 'programmed': 3.5, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x08                        .##.
    decimal
              1   35   35    8
    datetime (2015-04-28T19:20:02)
    0000   0x42 0x14 0xb3 0x1c 0x0f                   B....
    body (0)

#### RECORD 14 Bolus 2015-04-28T23:01:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-28T23:01:02)
    0000   0x42 0x01 0x57 0x1c 0x0f                   B.W..
    body (0)

#### RECORD 15 CalBGForPH 2015-04-28T23:41:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2015-04-28T23:41:22)
    0000   0x56 0x29 0x37 0x7c 0x0f                   V)7|.
    body (0)

#### RECORD 16 BGReceived 2015-04-28T23:41:22 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 78, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2015-04-28T23:41:22)
    0000   0x56 0x29 0xd7 0x7c 0x0f                   V).|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 17 MResultTotals 2015-04-29T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0xf6                   .....
    decimal
              7    0    0    8  246
    datetime (2015-04-29T00:00:00)
    0000   0x5c 0x0f                                  \.
    body (0)

#### RECORD 18 Model522ResultTotals 2015-04-29T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-29T00:00:00)
    0000   0x5c 0x0f                                  \.
    body (41)
    hex
    0000   0x05 0x10 0x8a 0x33 0x29 0x06 0x00 0x00    ...3)...
    0008   0x08 0xf6 0x03 0x1c 0x23 0x05 0xda 0x41    ....#..A
    0010   0x00 0xed 0x05 0xda 0x41 0x05 0x12 0x57    ....A..W
    0018   0x00 0xc8 0x0d 0x00 0x00 0x00 0x0a 0x08    ........
    0020   0x02 0x00 0x00 0x50 0x8f 0x4f 0x3d 0x1c    ...P.O=.
    0028   0x05                                       .
    decimal
              5   16  138   51   41    6    0    0
              8  246    3   28   35    5  218   65
              0  237    5  218   65    5   18   87
              0  200   13    0    0    0   10    8
              2    0    0   80  143   79   61   28
              5

#### RECORD 19 SensorAlert 2015-04-29T02:59:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-04-29T02:59:05)
    0000   0x45 0x3b 0x22 0xbd 0x0f                   E;"..
    body (0)

#### RECORD 20 SensorAlert 2015-04-29T04:27:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 228}
```
    op hex (3)
    0000   0x0b 0x65 0xe4                             .e.
    decimal
             11  101  228
    datetime (2015-04-29T04:27:36)
    0000   0x64 0x1b 0x24 0xbd 0x0f                   d.$..
    body (0)

#### RECORD 21 CalBGForPH 2015-04-29T04:57:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 330}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2015-04-29T04:57:32)
    0000   0x60 0x39 0x24 0x7d 0x8f                   `9$}.
    body (0)

#### RECORD 22 BGReceived 2015-04-29T04:57:32 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 330, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x29                                  ?)
    decimal
             63   41
    datetime (2015-04-29T04:57:32)
    0000   0x60 0x39 0x44 0x7d 0x0f                   `9D}.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 23 BolusWizard 2015-04-29T04:57:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 52,
 '_byte[7]': 0,
 'bg': 330,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.2,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4a                                  [J
    decimal
             91   74
    datetime (2015-04-29T04:57:38)
    0000   0x66 0x39 0x04 0x1d 0x0f                   f9...
    body (13)
    hex
    0000   0x00 0x51 0x0a 0x28 0x5a 0x34 0x00 0x00    .Q.(Z4..
    0008   0x00 0x00 0x00 0x34 0x78                   ...4x
    decimal
              0   81   10   40   90   52    0    0
              0    0    0   52  120

#### RECORD 24 UnabsorbedInsulinBolus unknown head[47], body[0] op[0x5c]
###### DECODED
```python
[{'age': 338, 'amount': 0.05},
 {'age': 348, 'amount': 0.15},
 {'age': 358, 'amount': 3.1},
 {'age': 368, 'amount': 0.15},
 {'age': 378, 'amount': 0.15},
 {'age': 388, 'amount': 0.15},
 {'age': 398, 'amount': 0.15},
 {'age': 408, 'amount': 0.15},
 {'age': 418, 'amount': 0.15},
 {'age': 428, 'amount': 0.15},
 {'age': 438, 'amount': 0.1},
 {'age': 448, 'amount': 0.15},
 {'age': 458, 'amount': 0.15},
 {'age': 468, 'amount': 0.15},
 {'age': 478, 'amount': 0.15}]
```
    op hex (47)
    0000   0x5c 0x2f 0x02 0x52 0x14 0x06 0x5c 0x14    \/.R..\.
    0008   0x7c 0x66 0x14 0x06 0x70 0x14 0x06 0x7a    |f..p..z
    0010   0x14 0x06 0x84 0x14 0x06 0x8e 0x14 0x06    ........
    0018   0x98 0x14 0x06 0xa2 0x14 0x06 0xac 0x14    ........
    0020   0x04 0xb6 0x14 0x06 0xc0 0x14 0x06 0xca    ........
    0028   0x14 0x06 0xd4 0x14 0x06 0xde 0x14         .......
    decimal
             92   47    2   82   20    6   92   20
            124  102   20    6  112   20    6  122
             20    6  132   20    6  142   20    6
            152   20    6  162   20    6  172   20
              4  182   20    6  192   20    6  202
             20    6  212   20    6  222   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2015-04-29T04:57:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2, 'duration': 0, 'programmed': 5.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x34 0x34 0x00                        .44.
    decimal
              1   52   52    0
    datetime (2015-04-29T04:57:38)
    0000   0x66 0x39 0x84 0x1d 0x0f                   f9...
    body (0)

#### RECORD 26 SensorAlert 2015-04-29T05:57:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 293}
```
    op hex (3)
    0000   0x0b 0x65 0x25                             .e%
    decimal
             11  101   37
    datetime (2015-04-29T05:57:38)
    0000   0x66 0x39 0x25 0xbd 0x8f                   f9%..
    body (0)

#### RECORD 27 PumpSuspend 2015-04-29T06:47:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-29T06:47:49)
    0000   0x71 0x2f 0x06 0x1d 0x0f                   q/...
    body (0)

#### RECORD 28 PumpResume 2015-04-29T06:47:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-29T06:47:55)
    0000   0x77 0x2f 0x06 0x1d 0x0f                   w/...
    body (0)

#### RECORD 29 PumpSuspend 2015-04-29T07:01:51 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-29T07:01:51)
    0000   0x73 0x01 0x07 0x1d 0x0f                   s....
    body (0)

#### RECORD 30 SensorAlert 2015-04-29T07:34:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 225}
```
    op hex (3)
    0000   0x0b 0x65 0xe1                             .e.
    decimal
             11  101  225
    datetime (2015-04-29T07:34:12)
    0000   0x4c 0x22 0x27 0xbd 0x0f                   L"'..
    body (0)

#### RECORD 31 PumpResume 2015-04-29T07:40:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-29T07:40:08)
    0000   0x48 0x28 0x07 0x1d 0x0f                   H(...
    body (0)

#### RECORD 32 CalBGForPH 2015-04-29T07:41:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2015-04-29T07:41:12)
    0000   0x4c 0x29 0x27 0x7d 0x0f                   L)'}.
    body (0)

#### RECORD 33 BGReceived 2015-04-29T07:41:12 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 186, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-04-29T07:41:12)
    0000   0x4c 0x29 0x47 0x7d 0x0f                   L)G}.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 34 BolusWizard 2015-04-29T07:41:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2015-04-29T07:41:25)
    0000   0x59 0x29 0x07 0x1d 0x0f                   Y)...
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x10 0x00 0x00    .P.(Z...
    0008   0x00 0x0c 0x00 0x04 0x78                   ....x
    decimal
              0   80   10   40   90   16    0    0
              0   12    0    4  120

#### RECORD 35 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 3.15}, {'age': 172, 'amount': 2.05}]
```
    op hex (8)
    0000   0x5c 0x08 0x7e 0xa2 0x04 0x52 0xac 0x04    \.~..R..
    decimal
             92    8  126  162    4   82  172    4
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2015-04-29T07:41:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'duration': 0, 'programmed': 0.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2015-04-29T07:41:25)
    0000   0x59 0x29 0x87 0x1d 0x0f                   Y)...
    body (0)

#### RECORD 37 BolusWizard 2015-04-29T07:48:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.2,
 'carb_input': 41,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 4.1,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2015-04-29T07:48:53)
    0000   0x75 0x30 0x07 0x1d 0x0f                   u0...
    body (13)
    hex
    0000   0x29 0x50 0x0a 0x28 0x5a 0x10 0x29 0x00    )P.(Z.).
    0008   0x00 0x0f 0x00 0x2a 0x78                   ...*x
    decimal
             41   80   10   40   90   16   41    0
              0   15    0   42  120

#### RECORD 38 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 0.4},
 {'age': 169, 'amount': 3.15},
 {'age': 179, 'amount': 2.05}]
```
    op hex (11)
    0000   0x5c 0x0b 0x10 0x09 0x04 0x7e 0xa9 0x04    \....~..
    0008   0x52 0xb3 0x04                             R..
    decimal
             92   11   16    9    4  126  169    4
             82  179    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2015-04-29T07:48:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.2, 'duration': 0, 'programmed': 4.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2a 0x2a 0x00                        .**.
    decimal
              1   42   42    0
    datetime (2015-04-29T07:48:54)
    0000   0x76 0x30 0x47 0x1d 0x0f                   v0G..
    body (0)

#### RECORD 40 BolusWizard 2015-04-29T07:59:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.8,
 'carb_input': 28,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 2.8,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-29T07:59:54)
    0000   0x76 0x3b 0x07 0x1d 0x0f                   v;...
    body (13)
    hex
    0000   0x1c 0x50 0x0a 0x28 0x5a 0x00 0x1c 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x1c 0x78                   ....x
    decimal
             28   80   10   40   90    0   28    0
              0    0    0   28  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 4.05},
 {'age': 20, 'amount': 0.55},
 {'age': 180, 'amount': 3.15},
 {'age': 190, 'amount': 2.05}]
```
    op hex (14)
    0000   0x5c 0x0e 0xa2 0x0a 0x04 0x16 0x14 0x04    \.......
    0008   0x7e 0xb4 0x04 0x52 0xbe 0x04              ~..R..
    decimal
             92   14  162   10    4   22   20    4
            126  180    4   82  190    4
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2015-04-29T07:59:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'duration': 0, 'programmed': 2.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x00                        ....
    decimal
              1   28   28    0
    datetime (2015-04-29T07:59:54)
    0000   0x76 0x3b 0x47 0x1d 0x0f                   v;G..
    body (0)

#### RECORD 43 BolusWizard 2015-04-29T09:23:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.9,
 'carb_input': 29,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 2.9,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-29T09:23:14)
    0000   0x4e 0x17 0x09 0x1d 0x0f                   N....
    body (13)
    hex
    0000   0x1d 0x50 0x0a 0x28 0x5a 0x00 0x1d 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x1d 0x78                   ....x
    decimal
             29   80   10   40   90    0   29    0
              0    0    0   29  120

#### RECORD 44 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 84, 'amount': 2.8},
 {'age': 94, 'amount': 4.05},
 {'age': 104, 'amount': 0.55},
 {'age': 264, 'amount': 3.15},
 {'age': 274, 'amount': 2.05}]
```
    op hex (17)
    0000   0x5c 0x11 0x70 0x54 0x04 0xa2 0x5e 0x04    \.pT..^.
    0008   0x16 0x68 0x04 0x7e 0x08 0x14 0x52 0x12    .h.~..R.
    0010   0x14                                       .
    decimal
             92   17  112   84    4  162   94    4
             22  104    4  126    8   20   82   18
             20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2015-04-29T09:23:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'duration': 0, 'programmed': 1.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2015-04-29T09:23:14)
    0000   0x4e 0x17 0x49 0x1d 0x0f                   N.I..
    body (0)

#### RECORD 46 SensorAlert 2015-04-29T11:28:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-04-29T11:28:17)
    0000   0x51 0x1c 0x2b 0xbd 0x0f                   Q.+..
    body (0)

#### RECORD 47 BolusWizard 2015-04-29T11:44:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 48,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-29T11:44:45)
    0000   0x6d 0x2c 0x0b 0x1d 0x0f                   m,...
    body (13)
    hex
    0000   0x30 0x50 0x08 0x28 0x5a 0x00 0x3c 0x00    0P.(Z.<.
    0008   0x00 0x00 0x00 0x3c 0x78                   ...<x
    decimal
             48   80    8   40   90    0   60    0
              0    0    0   60  120

#### RECORD 48 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 145, 'amount': 1.8},
 {'age': 225, 'amount': 2.8},
 {'age': 235, 'amount': 4.05},
 {'age': 245, 'amount': 0.55},
 {'age': 405, 'amount': 3.15},
 {'age': 415, 'amount': 2.05}]
```
    op hex (20)
    0000   0x5c 0x14 0x48 0x91 0x04 0x70 0xe1 0x04    \.H..p..
    0008   0xa2 0xeb 0x04 0x16 0xf5 0x04 0x7e 0x95    ......~.
    0010   0x14 0x52 0x9f 0x14                        .R..
    decimal
             92   20   72  145    4  112  225    4
            162  235    4   22  245    4  126  149
             20   82  159   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2015-04-29T11:44:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'duration': 0, 'programmed': 4.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2015-04-29T11:44:45)
    0000   0x6d 0x2c 0x8b 0x1d 0x0f                   m,...
    body (0)

#### RECORD 50 SensorAlert 2015-04-29T12:59:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 244}
```
    op hex (3)
    0000   0x0b 0x65 0xf4                             .e.
    decimal
             11  101  244
    datetime (2015-04-29T12:59:05)
    0000   0x45 0x3b 0x2c 0xbd 0x0f                   E;,..
    body (0)

#### RECORD 51 BolusWizard 2015-04-29T13:13:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-29T13:13:25)
    0000   0x59 0x0d 0x0d 0x1d 0x0f                   Y....
    body (13)
    hex
    0000   0x00 0x50 0x08 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80    8   40   90    0    0    0
              0    0    0    0  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 0.1},
 {'age': 14, 'amount': 0.15},
 {'age': 24, 'amount': 0.15},
 {'age': 34, 'amount': 0.2},
 {'age': 44, 'amount': 0.15},
 {'age': 54, 'amount': 0.15},
 {'age': 64, 'amount': 0.2},
 {'age': 74, 'amount': 0.15},
 {'age': 84, 'amount': 0.15},
 {'age': 94, 'amount': 4.05},
 {'age': 234, 'amount': 1.8},
 {'age': 314, 'amount': 2.8},
 {'age': 324, 'amount': 4.05},
 {'age': 334, 'amount': 0.55}]
```
    op hex (44)
    0000   0x5c 0x2c 0x04 0x04 0x04 0x06 0x0e 0x04    \,......
    0008   0x06 0x18 0x04 0x08 0x22 0x04 0x06 0x2c    ...."..,
    0010   0x04 0x06 0x36 0x04 0x08 0x40 0x04 0x06    ..6..@..
    0018   0x4a 0x04 0x06 0x54 0x04 0xa2 0x5e 0x04    J..T..^.
    0020   0x48 0xea 0x04 0x70 0x3a 0x14 0xa2 0x44    H..p:..D
    0028   0x14 0x16 0x4e 0x14                        ..N.
    decimal
             92   44    4    4    4    6   14    4
              6   24    4    8   34    4    6   44
              4    6   54    4    8   64    4    6
             74    4    6   84    4  162   94    4
             72  234    4  112   58   20  162   68
             20   22   78   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2015-04-29T11:47:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 120, 'programmed': 2.0, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x04                        ....
    decimal
              1   20   20    4
    datetime (2015-04-29T11:47:25)
    0000   0x59 0x2f 0xab 0x1d 0x0f                   Y/...
    body (0)

#### RECORD 54 Bolus 2015-04-29T13:13:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'duration': 0, 'programmed': 2.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2015-04-29T13:13:25)
    0000   0x59 0x0d 0x4d 0x1d 0x0f                   Y.M..
    body (0)

#### RECORD 55 SensorAlert 2015-04-29T14:27:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 246}
```
    op hex (3)
    0000   0x0b 0x65 0xf6                             .e.
    decimal
             11  101  246
    datetime (2015-04-29T14:27:36)
    0000   0x64 0x1b 0x2e 0xbd 0x0f                   d....
    body (0)

#### RECORD 56 SensorAlert 2015-04-29T15:57:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 257}
```
    op hex (3)
    0000   0x0b 0x65 0x01                             .e.
    decimal
             11  101    1
    datetime (2015-04-29T15:57:38)
    0000   0x66 0x39 0x2f 0xbd 0x8f                   f9/..
    body (0)

#### RECORD 57 BolusWizard 2015-04-29T17:03:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-04-29T17:03:32)
    0000   0x60 0x03 0x11 0x1d 0x0f                   `....
    body (13)
    hex
    0000   0x00 0x50 0x08 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80    8   40   90    0    0    0
              0    0    0    0  120

`end ReadHistoryData-page-1.data: 58 records`
