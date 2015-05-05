## START ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 993, found 29 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x65 0xda                                  e.
##### DEBUG DECIMAL
            101  218
#### RECORD 0 UnabsorbedInsulinBolus unknown head[47], body[0] op[0x5c]
###### DECODED
```python
[{'age': 252, 'amount': 0.2, 'curve': 4},
 {'age': 6, 'amount': 0.25, 'curve': 20},
 {'age': 16, 'amount': 0.2, 'curve': 20},
 {'age': 26, 'amount': 0.25, 'curve': 20},
 {'age': 36, 'amount': 2.0, 'curve': 20},
 {'age': 46, 'amount': 0.25, 'curve': 20},
 {'age': 56, 'amount': 0.25, 'curve': 20},
 {'age': 66, 'amount': 0.2, 'curve': 20},
 {'age': 76, 'amount': 0.25, 'curve': 20},
 {'age': 86, 'amount': 0.25, 'curve': 20},
 {'age': 96, 'amount': 1.2, 'curve': 20},
 {'age': 106, 'amount': 0.25, 'curve': 20},
 {'age': 116, 'amount': 3.45, 'curve': 20},
 {'age': 126, 'amount': 2.2, 'curve': 20},
 {'age': 196, 'amount': 2.1, 'curve': 20}]
```
    op hex (47)
    0000   0x5c 0x2f 0x08 0xfc 0x04 0x0a 0x06 0x14    \/......
    0008   0x08 0x10 0x14 0x0a 0x1a 0x14 0x50 0x24    ......P$
    0010   0x14 0x0a 0x2e 0x14 0x0a 0x38 0x14 0x08    .....8..
    0018   0x42 0x14 0x0a 0x4c 0x14 0x0a 0x56 0x14    B..L..V.
    0020   0x30 0x60 0x14 0x0a 0x6a 0x14 0x8a 0x74    0`..j..t
    0028   0x14 0x58 0x7e 0x14 0x54 0xc4 0x14         .X~.T..
    decimal
             92   47    8  252    4   10    6   20
              8   16   20   10   26   20   80   36
             20   10   46   20   10   56   20    8
             66   20   10   76   20   10   86   20
             48   96   20   10  106   20  138  116
             20   88  126   20   84  196   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-04-27T18:21:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2015-04-27T18:21:10)
    0000   0x4a 0x15 0x92 0x1b 0x0f                   J....
    body (0)

#### RECORD 2 Bolus 2015-04-27T18:23:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'duration': 60, 'programmed': 3.4, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x22 0x04 0x02                        ."..
    decimal
              1   34    4    2
    datetime (2015-04-27T18:23:26)
    0000   0x5a 0x17 0xb2 0x1b 0x0f                   Z....
    body (0)

#### RECORD 3 NoDelivery 2015-04-27T18:30:03 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xff                        ....
    decimal
              6    4   11  255
    datetime (2015-04-27T18:30:03)
    0000   0x43 0x1e 0x52 0x5b 0x0f                   C.R[.
    body (0)

#### RECORD 4 ClearAlarm 2015-04-27T18:31:09 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-04-27T18:31:09)
    0000   0x49 0x1f 0x12 0x1b 0x0f                   I....
    body (0)

#### RECORD 5 Rewind 2015-04-27T18:31:14 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-04-27T18:31:14)
    0000   0x4e 0x1f 0x12 0x1b 0x0f                   N....
    body (0)

#### RECORD 6 Prime 2015-04-27T18:48:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.9, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x45                   ....E
    decimal
              3    0    0    0   69
    datetime (2015-04-27T18:48:19)
    0000   0x53 0x30 0x32 0x1b 0x0f                   S02..
    body (0)

#### RECORD 7 Prime 2015-04-27T18:49:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2015-04-27T18:49:03)
    0000   0x43 0x31 0x12 0x1b 0x0f                   C1...
    body (0)

#### RECORD 8 BolusWizard 2015-04-27T19:16:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 6,
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
    datetime (2015-04-27T19:16:04)
    0000   0x44 0x10 0x13 0x1b 0x0f                   D....
    body (13)
    hex
    0000   0x00 0x50 0x06 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80    6   40   90    0    0    0
              0    0    0    0  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[50], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 0.05, 'curve': 4},
 {'age': 57, 'amount': 3.7, 'curve': 4},
 {'age': 51, 'amount': 0.2, 'curve': 20},
 {'age': 61, 'amount': 0.25, 'curve': 20},
 {'age': 71, 'amount': 0.2, 'curve': 20},
 {'age': 81, 'amount': 0.25, 'curve': 20},
 {'age': 91, 'amount': 2.0, 'curve': 20},
 {'age': 101, 'amount': 0.25, 'curve': 20},
 {'age': 111, 'amount': 0.25, 'curve': 20},
 {'age': 121, 'amount': 0.2, 'curve': 20},
 {'age': 131, 'amount': 0.25, 'curve': 20},
 {'age': 141, 'amount': 0.25, 'curve': 20},
 {'age': 151, 'amount': 1.2, 'curve': 20},
 {'age': 161, 'amount': 0.25, 'curve': 20},
 {'age': 171, 'amount': 3.45, 'curve': 20},
 {'age': 181, 'amount': 2.2, 'curve': 20}]
```
    op hex (50)
    0000   0x5c 0x32 0x02 0x2f 0x04 0x94 0x39 0x04    \2./..9.
    0008   0x08 0x33 0x14 0x0a 0x3d 0x14 0x08 0x47    .3..=..G
    0010   0x14 0x0a 0x51 0x14 0x50 0x5b 0x14 0x0a    ..Q.P[..
    0018   0x65 0x14 0x0a 0x6f 0x14 0x08 0x79 0x14    e..o..y.
    0020   0x0a 0x83 0x14 0x0a 0x8d 0x14 0x30 0x97    ......0.
    0028   0x14 0x0a 0xa1 0x14 0x8a 0xab 0x14 0x58    .......X
    0030   0xb5 0x14                                  ..
    decimal
             92   50    2   47    4  148   57    4
              8   51   20   10   61   20    8   71
             20   10   81   20   80   91   20   10
            101   20   10  111   20    8  121   20
             10  131   20   10  141   20   48  151
             20   10  161   20  138  171   20   88
            181   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2015-04-27T19:16:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'duration': 0, 'programmed': 3.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2015-04-27T19:16:04)
    0000   0x44 0x10 0x53 0x1b 0x0f                   D.S..
    body (0)

#### RECORD 11 SensorAlert 2015-04-27T19:28:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 205}
```
    op hex (3)
    0000   0x0b 0x65 0xcd                             .e.
    decimal
             11  101  205
    datetime (2015-04-27T19:28:17)
    0000   0x51 0x1c 0x33 0xbb 0x0f                   Q.3..
    body (0)

#### RECORD 12 BolusWizard 2015-04-27T19:57:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.6,
 'carb_input': 28,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
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
    datetime (2015-04-27T19:57:10)
    0000   0x4a 0x39 0x13 0x1b 0x0f                   J9...
    body (13)
    hex
    0000   0x1c 0x50 0x06 0x28 0x5a 0x00 0x2e 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x2e 0x78                   ....x
    decimal
             28   80    6   40   90    0   46    0
              0    0    0   46  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[53], body[0] op[0x5c]
###### DECODED
```python
[{'age': 48, 'amount': 3.1, 'curve': 4},
 {'age': 88, 'amount': 0.05, 'curve': 4},
 {'age': 98, 'amount': 3.7, 'curve': 4},
 {'age': 92, 'amount': 0.2, 'curve': 20},
 {'age': 102, 'amount': 0.25, 'curve': 20},
 {'age': 112, 'amount': 0.2, 'curve': 20},
 {'age': 122, 'amount': 0.25, 'curve': 20},
 {'age': 132, 'amount': 2.0, 'curve': 20},
 {'age': 142, 'amount': 0.25, 'curve': 20},
 {'age': 152, 'amount': 0.25, 'curve': 20},
 {'age': 162, 'amount': 0.2, 'curve': 20},
 {'age': 172, 'amount': 0.25, 'curve': 20},
 {'age': 182, 'amount': 0.25, 'curve': 20},
 {'age': 192, 'amount': 1.2, 'curve': 20},
 {'age': 202, 'amount': 0.25, 'curve': 20},
 {'age': 212, 'amount': 3.45, 'curve': 20},
 {'age': 222, 'amount': 2.2, 'curve': 20}]
```
    op hex (53)
    0000   0x5c 0x35 0x7c 0x30 0x04 0x02 0x58 0x04    \5|0..X.
    0008   0x94 0x62 0x04 0x08 0x5c 0x14 0x0a 0x66    .b..\..f
    0010   0x14 0x08 0x70 0x14 0x0a 0x7a 0x14 0x50    ..p..z.P
    0018   0x84 0x14 0x0a 0x8e 0x14 0x0a 0x98 0x14    ........
    0020   0x08 0xa2 0x14 0x0a 0xac 0x14 0x0a 0xb6    ........
    0028   0x14 0x30 0xc0 0x14 0x0a 0xca 0x14 0x8a    .0......
    0030   0xd4 0x14 0x58 0xde 0x14                   ..X..
    decimal
             92   53  124   48    4    2   88    4
            148   98    4    8   92   20   10  102
             20    8  112   20   10  122   20   80
            132   20   10  142   20   10  152   20
              8  162   20   10  172   20   10  182
             20   48  192   20   10  202   20  138
            212   20   88  222   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2015-04-27T19:57:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'duration': 0, 'programmed': 4.6, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2015-04-27T19:57:10)
    0000   0x4a 0x39 0x53 0x1b 0x0f                   J9S..
    body (0)

#### RECORD 15 BolusWizard 2015-04-27T20:03:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.0,
 'carb_input': 12,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
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
    datetime (2015-04-27T20:03:24)
    0000   0x58 0x03 0x14 0x1b 0x0f                   X....
    body (13)
    hex
    0000   0x0c 0x50 0x06 0x28 0x5a 0x00 0x14 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x14 0x78                   ....x
    decimal
             12   80    6   40   90    0   20    0
              0    0    0   20  120

#### RECORD 16 UnabsorbedInsulinBolus unknown head[56], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 1.85, 'curve': 4},
 {'age': 14, 'amount': 2.75, 'curve': 4},
 {'age': 54, 'amount': 3.1, 'curve': 4},
 {'age': 94, 'amount': 0.05, 'curve': 4},
 {'age': 104, 'amount': 3.7, 'curve': 4},
 {'age': 98, 'amount': 0.2, 'curve': 20},
 {'age': 108, 'amount': 0.25, 'curve': 20},
 {'age': 118, 'amount': 0.2, 'curve': 20},
 {'age': 128, 'amount': 0.25, 'curve': 20},
 {'age': 138, 'amount': 2.0, 'curve': 20},
 {'age': 148, 'amount': 0.25, 'curve': 20},
 {'age': 158, 'amount': 0.25, 'curve': 20},
 {'age': 168, 'amount': 0.2, 'curve': 20},
 {'age': 178, 'amount': 0.25, 'curve': 20},
 {'age': 188, 'amount': 0.25, 'curve': 20},
 {'age': 198, 'amount': 1.2, 'curve': 20},
 {'age': 208, 'amount': 0.25, 'curve': 20},
 {'age': 218, 'amount': 3.45, 'curve': 20}]
```
    op hex (56)
    0000   0x5c 0x38 0x4a 0x04 0x04 0x6e 0x0e 0x04    \8J..n..
    0008   0x7c 0x36 0x04 0x02 0x5e 0x04 0x94 0x68    |6..^..h
    0010   0x04 0x08 0x62 0x14 0x0a 0x6c 0x14 0x08    ..b..l..
    0018   0x76 0x14 0x0a 0x80 0x14 0x50 0x8a 0x14    v....P..
    0020   0x0a 0x94 0x14 0x0a 0x9e 0x14 0x08 0xa8    ........
    0028   0x14 0x0a 0xb2 0x14 0x0a 0xbc 0x14 0x30    .......0
    0030   0xc6 0x14 0x0a 0xd0 0x14 0x8a 0xda 0x14    ........
    decimal
             92   56   74    4    4  110   14    4
            124   54    4    2   94    4  148  104
              4    8   98   20   10  108   20    8
            118   20   10  128   20   80  138   20
             10  148   20   10  158   20    8  168
             20   10  178   20   10  188   20   48
            198   20   10  208   20  138  218   20
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2015-04-27T20:03:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 0, 'programmed': 2.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2015-04-27T20:03:25)
    0000   0x59 0x03 0x54 0x1b 0x0f                   Y.T..
    body (0)

#### RECORD 18 SensorAlert 2015-04-27T20:59:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 243}
```
    op hex (3)
    0000   0x0b 0x65 0xf3                             .e.
    decimal
             11  101  243
    datetime (2015-04-27T20:59:05)
    0000   0x45 0x3b 0x34 0xbb 0x0f                   E;4..
    body (0)

#### RECORD 19 CalBGForPH 2015-04-27T21:24:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 204}
```
    op hex (2)
    0000   0x0a 0xcc                                  ..
    decimal
             10  204
    datetime (2015-04-27T21:24:10)
    0000   0x4a 0x18 0x35 0x7b 0x0f                   J.5{.
    body (0)

#### RECORD 20 BGReceived 2015-04-27T21:24:10 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2015-04-27T21:24:10)
    0000   0x4a 0x18 0x95 0x7b 0x0f                   J..{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 21 BolusWizard 2015-04-27T22:03:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 30,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
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
    datetime (2015-04-27T22:03:42)
    0000   0x6a 0x03 0x16 0x1b 0x0f                   j....
    body (13)
    hex
    0000   0x1e 0x50 0x06 0x28 0x5a 0x00 0x32 0x00    .P.(Z.2.
    0008   0x00 0x00 0x00 0x32 0x78                   ...2x
    decimal
             30   80    6   40   90    0   50    0
              0    0    0   50  120

#### RECORD 22 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 3.85, 'curve': 4},
 {'age': 134, 'amount': 2.75, 'curve': 4},
 {'age': 174, 'amount': 3.1, 'curve': 4},
 {'age': 214, 'amount': 0.05, 'curve': 4},
 {'age': 224, 'amount': 3.7, 'curve': 4},
 {'age': 218, 'amount': 0.2, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x9a 0x7c 0x04 0x6e 0x86 0x04    \..|.n..
    0008   0x7c 0xae 0x04 0x02 0xd6 0x04 0x94 0xe0    |.......
    0010   0x04 0x08 0xda 0x14                        ....
    decimal
             92   20  154  124    4  110  134    4
            124  174    4    2  214    4  148  224
              4    8  218   20
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2015-04-27T22:03:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'duration': 0, 'programmed': 5.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2015-04-27T22:03:42)
    0000   0x6a 0x03 0x56 0x1b 0x0f                   j.V..
    body (0)

#### RECORD 24 SensorAlert 2015-04-27T22:27:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 227}
```
    op hex (3)
    0000   0x0b 0x65 0xe3                             .e.
    decimal
             11  101  227
    datetime (2015-04-27T22:27:36)
    0000   0x64 0x1b 0x36 0xbb 0x0f                   d.6..
    body (0)

#### RECORD 25 BolusWizard 2015-04-27T22:29:50 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.3,
 'carb_input': 50,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 8.3,
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
    datetime (2015-04-27T22:29:50)
    0000   0x72 0x1d 0x16 0x1b 0x0f                   r....
    body (13)
    hex
    0000   0x32 0x50 0x06 0x28 0x5a 0x00 0x53 0x00    2P.(Z.S.
    0008   0x00 0x00 0x00 0x53 0x78                   ...Sx
    decimal
             50   80    6   40   90    0   83    0
              0    0    0   83  120

#### RECORD 26 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 5.0, 'curve': 4},
 {'age': 150, 'amount': 3.85, 'curve': 4},
 {'age': 160, 'amount': 2.75, 'curve': 4},
 {'age': 200, 'amount': 3.1, 'curve': 4},
 {'age': 240, 'amount': 0.05, 'curve': 4},
 {'age': 250, 'amount': 3.7, 'curve': 4}]
```
    op hex (20)
    0000   0x5c 0x14 0xc8 0x1e 0x04 0x9a 0x96 0x04    \.......
    0008   0x6e 0xa0 0x04 0x7c 0xc8 0x04 0x02 0xf0    n..|....
    0010   0x04 0x94 0xfa 0x04                        ....
    decimal
             92   20  200   30    4  154  150    4
            110  160    4  124  200    4    2  240
              4  148  250    4
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2015-04-27T22:29:50 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'duration': 0, 'programmed': 4.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2015-04-27T22:29:50)
    0000   0x72 0x1d 0x96 0x1b 0x0f                   r....
    body (0)

#### RECORD 28 MResultTotals 2015-04-28T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0x22                   ...."
    decimal
              7    0    0   10   34
    datetime (2015-04-28T00:00:00)
    0000   0x5b 0x0f                                  [.
    body (0)

#### RECORD 29 Model522ResultTotals 2015-04-28T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-28T00:00:00)
    0000   0x5b 0x0f                                  [.
    body (41)
    hex
    0000   0x05 0x10 0xd5 0x3d 0x3f 0x06 0x00 0x00    ...=?...
    0008   0x0a 0x22 0x02 0xfe 0x1e 0x07 0x24 0x46    ."....$F
    0010   0x01 0x46 0x07 0x24 0x46 0x06 0x50 0x58    .F.$F.PX
    0018   0x00 0xd4 0x0c 0x00 0x00 0x00 0x0d 0x0b    ........
    0020   0x02 0x00 0x00 0x10 0xde 0x78 0x49 0x93    .....xI.
    0028   0x04                                       .
    decimal
              5   16  213   61   63    6    0    0
             10   34    2  254   30    7   36   70
              1   70    7   36   70    6   80   88
              0  212   12    0    0    0   13   11
              2    0    0   16  222  120   73  147
              4

#### RECORD 30 Bolus 2015-04-27T22:32:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'duration': 180, 'programmed': 3.6, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x06                        .$$.
    decimal
              1   36   36    6
    datetime (2015-04-27T22:32:58)
    0000   0x7a 0x20 0xb6 0x1b 0x0f                   z ...
    body (0)

#### RECORD 31 SensorAlert 2015-04-28T03:57:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-28T03:57:38)
    0000   0x66 0x39 0x23 0xbc 0x0f                   f9#..
    body (0)

#### RECORD 32 CalBGForPH 2015-04-28T07:27:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 51}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2015-04-28T07:27:50)
    0000   0x72 0x1b 0x27 0x7c 0x0f                   r.'|.
    body (0)

#### RECORD 33 BGReceived 2015-04-28T07:27:50 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2015-04-28T07:27:50)
    0000   0x72 0x1b 0x67 0x7c 0x0f                   r.g|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 34 SensorAlert 2015-04-28T07:43:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-28T07:43:53)
    0000   0x75 0x2b 0x27 0xbc 0x0f                   u+'..
    body (0)

#### RECORD 35 SensorAlert 2015-04-28T07:43:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 106'}
```
    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2015-04-28T07:43:53)
    0000   0x75 0x2b 0x27 0xbc 0x0f                   u+'..
    body (0)

#### RECORD 36 CalBGForPH 2015-04-28T07:50:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2015-04-28T07:50:56)
    0000   0x78 0x32 0x27 0x7c 0x0f                   x2'|.
    body (0)

#### RECORD 37 BGReceived 2015-04-28T07:50:56 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2015-04-28T07:50:56)
    0000   0x78 0x32 0x07 0x7c 0x0f                   x2.|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 38 PumpSuspend 2015-04-28T07:54:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-28T07:54:19)
    0000   0x53 0x36 0x07 0x1c 0x0f                   S6...
    body (0)

#### RECORD 39 PumpResume 2015-04-28T08:16:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-28T08:16:40)
    0000   0x68 0x10 0x08 0x1c 0x0f                   h....
    body (0)

#### RECORD 40 BolusWizard 2015-04-28T08:16:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.4,
 'carb_input': 24,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 2.4,
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
    datetime (2015-04-28T08:16:54)
    0000   0x76 0x10 0x08 0x1c 0x0f                   v....
    body (13)
    hex
    0000   0x18 0x50 0x0a 0x28 0x5a 0x00 0x18 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x18 0x78                   ....x
    decimal
             24   80   10   40   90    0   24    0
              0    0    0   24  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 151, 'amount': 0.1, 'curve': 20},
 {'age': 161, 'amount': 0.2, 'curve': 20},
 {'age': 171, 'amount': 0.2, 'curve': 20},
 {'age': 181, 'amount': 0.2, 'curve': 20},
 {'age': 191, 'amount': 0.2, 'curve': 20},
 {'age': 201, 'amount': 0.2, 'curve': 20},
 {'age': 211, 'amount': 0.2, 'curve': 20},
 {'age': 221, 'amount': 0.2, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x04 0x97 0x14 0x08 0xa1 0x14    \.......
    0008   0x08 0xab 0x14 0x08 0xb5 0x14 0x08 0xbf    ........
    0010   0x14 0x08 0xc9 0x14 0x08 0xd3 0x14 0x08    ........
    0018   0xdd 0x14                                  ..
    decimal
             92   26    4  151   20    8  161   20
              8  171   20    8  181   20    8  191
             20    8  201   20    8  211   20    8
            221   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2015-04-28T08:16:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'duration': 0, 'programmed': 2.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2015-04-28T08:16:54)
    0000   0x76 0x10 0x48 0x1c 0x0f                   v.H..
    body (0)

#### RECORD 43 SensorAlert 2015-04-28T08:33:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 191}
```
    op hex (3)
    0000   0x0b 0x65 0xbf                             .e.
    decimal
             11  101  191
    datetime (2015-04-28T08:33:44)
    0000   0x6c 0x21 0x28 0xbc 0x0f                   l!(..
    body (0)

#### RECORD 44 BolusWizard 2015-04-28T08:53:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 10,
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
    datetime (2015-04-28T08:53:14)
    0000   0x4e 0x35 0x08 0x1c 0x0f                   N5...
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80   10   40   90    0    0    0
              0    0    0    0  120

#### RECORD 45 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 2.4, 'curve': 4},
 {'age': 188, 'amount': 0.1, 'curve': 20},
 {'age': 198, 'amount': 0.2, 'curve': 20},
 {'age': 208, 'amount': 0.2, 'curve': 20},
 {'age': 218, 'amount': 0.2, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x60 0x2c 0x04 0x04 0xbc 0x14    \.`,....
    0008   0x08 0xc6 0x14 0x08 0xd0 0x14 0x08 0xda    ........
    0010   0x14                                       .
    decimal
             92   17   96   44    4    4  188   20
              8  198   20    8  208   20    8  218
             20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2015-04-28T08:53:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-28T08:53:14)
    0000   0x4e 0x35 0x48 0x1c 0x0f                   N5H..
    body (0)

#### RECORD 47 SensorAlert 2015-04-28T10:02:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 237}
```
    op hex (3)
    0000   0x0b 0x65 0xed                             .e.
    decimal
             11  101  237
    datetime (2015-04-28T10:02:55)
    0000   0x77 0x02 0x2a 0xbc 0x0f                   w.*..
    body (0)

#### RECORD 48 CalBGForPH 2015-04-28T10:37:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 297}
```
    op hex (2)
    0000   0x0a 0x29                                  .)
    decimal
             10   41
    datetime (2015-04-28T10:37:18)
    0000   0x52 0x25 0x2a 0x7c 0x8f                   R%*|.
    body (0)

#### RECORD 49 BGReceived 2015-04-28T10:37:18 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x25                                  ?%
    decimal
             63   37
    datetime (2015-04-28T10:37:18)
    0000   0x52 0x25 0x2a 0x7c 0x0f                   R%*|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 50 BolusWizard 2015-04-28T10:37:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 44,
 '_byte[7]': 0,
 'bg': 297,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x29                                  [)
    decimal
             91   41
    datetime (2015-04-28T10:37:28)
    0000   0x5c 0x25 0x0a 0x1c 0x0f                   \%...
    body (13)
    hex
    0000   0x00 0x51 0x0a 0x28 0x5a 0x2c 0x00 0x00    .Q.(Z,..
    0008   0x00 0x18 0x00 0x14 0x78                   ....x
    decimal
              0   81   10   40   90   44    0    0
              0   24    0   20  120

#### RECORD 51 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 3.0, 'curve': 4},
 {'age': 148, 'amount': 2.4, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x78 0x6c 0x04 0x60 0x94 0x04    \.xl.`..
    decimal
             92    8  120  108    4   96  148    4
    datetime (unknown)

    body (0)

#### RECORD 52 Bolus 2015-04-28T10:37:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 0, 'programmed': 2.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2015-04-28T10:37:28)
    0000   0x5c 0x25 0x4a 0x1c 0x0f                   \%J..
    body (0)

#### RECORD 53 BolusWizard 2015-04-28T10:58:28 head[2], body[13] op[0x5b]
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
    datetime (2015-04-28T10:58:28)
    0000   0x5c 0x3a 0x0a 0x1c 0x0f                   \:...
    body (13)
    hex
    0000   0x1d 0x50 0x0a 0x28 0x5a 0x00 0x1d 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x1d 0x78                   ....x
    decimal
             29   80   10   40   90    0   29    0
              0    0    0   29  120

#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 2.0, 'curve': 4},
 {'age': 129, 'amount': 3.0, 'curve': 4},
 {'age': 169, 'amount': 2.4, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0x1d 0x04 0x78 0x81 0x04    \.P..x..
    0008   0x60 0xa9 0x04                             `..
    decimal
             92   11   80   29    4  120  129    4
             96  169    4
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2015-04-28T10:58:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'duration': 0, 'programmed': 2.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2015-04-28T10:58:29)
    0000   0x5d 0x3a 0x4a 0x1c 0x0f                   ]:J..
    body (0)

#### RECORD 56 SensorAlert 2015-04-28T11:34:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 303}
```
    op hex (3)
    0000   0x0b 0x65 0x2f                             .e/
    decimal
             11  101   47
    datetime (2015-04-28T11:34:12)
    0000   0x4c 0x22 0x2b 0xbc 0x8f                   L"+..
    body (0)

#### RECORD 57 CalBGForPH 2015-04-28T11:37:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 266}
```
    op hex (2)
    0000   0x0a 0x0a                                  ..
    decimal
             10   10
    datetime (2015-04-28T11:37:02)
    0000   0x42 0x25 0x2b 0x7c 0x8f                   B%+|.
    body (0)

#### RECORD 58 BGReceived 2015-04-28T11:37:02 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x21                                  ?!
    decimal
             63   33
    datetime (2015-04-28T11:37:02)
    0000   0x42 0x25 0x4b 0x7c 0x0f                   B%K|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 59 BolusWizard 2015-04-28T11:37:32 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 266,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 48,
 'carb_ratio': 8,
 'correction_estimate': 0.4,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 5.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0a                                  [.
    decimal
             91   10
    datetime (2015-04-28T11:37:32)
    0000   0x60 0x25 0x0b 0x1c 0x0f                   `%...
    body (13)
    hex
    0000   0x30 0x51 0x08 0x28 0x5a 0x24 0x3c 0x00    0Q.(Z$<.
    0008   0x00 0x33 0x00 0x3c 0x78                   .3.<x
    decimal
             48   81    8   40   90   36   60    0
              0   51    0   60  120

#### RECORD 60 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 38, 'amount': 2.1, 'curve': 4},
 {'age': 48, 'amount': 0.8, 'curve': 4},
 {'age': 68, 'amount': 2.0, 'curve': 4},
 {'age': 168, 'amount': 3.0, 'curve': 4},
 {'age': 208, 'amount': 2.4, 'curve': 4}]
```
    op hex (17)
    0000   0x5c 0x11 0x54 0x26 0x04 0x20 0x30 0x04    \.T&. 0.
    0008   0x50 0x44 0x04 0x78 0xa8 0x04 0x60 0xd0    PD.x..`.
    0010   0x04                                       .
    decimal
             92   17   84   38    4   32   48    4
             80   68    4  120  168    4   96  208
              4
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2015-04-28T11:37:32 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'duration': 0, 'programmed': 4.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2015-04-28T11:37:32)
    0000   0x60 0x25 0x8b 0x1c 0x0f                   `%...
    body (0)

#### RECORD 62 BolusWizard 2015-04-28T11:52:46 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.5,
 'carb_input': 12,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 1.5,
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
    datetime (2015-04-28T11:52:46)
    0000   0x6e 0x34 0x0b 0x1c 0x0f                   n4...
    body (13)
    hex
    0000   0x0c 0x50 0x08 0x28 0x5a 0x00 0x0f 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x0f 0x78                   ....x
    decimal
             12   80    8   40   90    0   15    0
              0    0    0   15  120

#### RECORD 63 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 0.05, 'curve': 4},
 {'age': 13, 'amount': 1.95, 'curve': 4},
 {'age': 23, 'amount': 2.15, 'curve': 4},
 {'age': 53, 'amount': 2.1, 'curve': 4},
 {'age': 63, 'amount': 0.8, 'curve': 4},
 {'age': 83, 'amount': 2.0, 'curve': 4},
 {'age': 183, 'amount': 3.0, 'curve': 4},
 {'age': 223, 'amount': 2.4, 'curve': 4}]
```
    op hex (26)
    0000   0x5c 0x1a 0x02 0x03 0x04 0x4e 0x0d 0x04    \....N..
    0008   0x56 0x17 0x04 0x54 0x35 0x04 0x20 0x3f    V..T5. ?
    0010   0x04 0x50 0x53 0x04 0x78 0xb7 0x04 0x60    .PS.x..`
    0018   0xdf 0x04                                  ..
    decimal
             92   26    2    3    4   78   13    4
             86   23    4   84   53    4   32   63
              4   80   83    4  120  183    4   96
            223    4
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2015-04-28T11:40:12 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 180, 'programmed': 2.0, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x06                        ....
    decimal
              1   20   20    6
    datetime (2015-04-28T11:40:12)
    0000   0x4c 0x28 0xab 0x1c 0x0f                   L(...
    body (0)

#### RECORD 65 Bolus 2015-04-28T11:52:46 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5, 'duration': 0, 'programmed': 1.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0f 0x0f 0x00                        ....
    decimal
              1   15   15    0
    datetime (2015-04-28T11:52:46)
    0000   0x6e 0x34 0x4b 0x1c 0x0f                   n4K..
    body (0)

#### RECORD 66 BolusWizard 2015-04-28T14:11:55 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.5,
 'carb_input': 20,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 2.5,
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
    datetime (2015-04-28T14:11:55)
    0000   0x77 0x0b 0x0e 0x1c 0x0f                   w....
    body (13)
    hex
    0000   0x14 0x50 0x08 0x28 0x5a 0x00 0x19 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x19 0x78                   ....x
    decimal
             20   80    8   40   90    0   25    0
              0    0    0   25  120

`end ReadHistoryData-page-2.data: 67 records`
