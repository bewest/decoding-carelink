## START analysis/736868/logs/ReadHistoryData-page-19.data
#### STOPPING DOUBLE NULLS @ 1017, found 5 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe1 0x3f                                  .?
##### DEBUG DECIMAL
            225   63
#### RECORD 0 SensorAlert 2015-02-26T10:27:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-26T10:27:00)
    0000   0x00 0x9b 0x2a 0xba 0x0f                   ..*..
    body (0)

#### RECORD 1 SensorAlert 2015-02-26T10:57:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-26T10:57:00)
    0000   0x00 0xb9 0x2a 0xba 0x0f                   ..*..
    body (0)

#### RECORD 2 SensorAlert 2015-02-26T11:27:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-26T11:27:00)
    0000   0x00 0x9b 0x2b 0xba 0x0f                   ..+..
    body (0)

#### RECORD 3 SensorAlert 2015-02-26T11:36:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 107, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-02-26T11:36:06)
    0000   0x06 0xa4 0x2b 0xba 0x0f                   ..+..
    body (0)

#### RECORD 4 CalBGForPH 2015-02-26T11:40:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2015-02-26T11:40:31)
    0000   0x1f 0xa8 0x2b 0x7a 0x0f                   ..+z.
    body (0)

#### RECORD 5 BGReceived 2015-02-26T11:40:31 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2015-02-26T11:40:31)
    0000   0x1f 0xa8 0xeb 0x7a 0x0f                   ...z.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 6 BolusWizard 2015-02-26T11:40:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 143,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 12.0,
 'correction_estimate': 0.5,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.7}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2015-02-26T11:40:45)
    0000   0x2d 0xa8 0x0b 0x7a 0x0f                   -..z.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x14 0x00    .P.P(Z..
    0008   0x00 0x00 0x00 0x1c 0x00 0x00 0x78         ......x
    decimal
              0   80    0   80   40   90   20    0
              0    0    0   28    0    0  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 181, 'amount': 3.0, 'curve': 4},
 {'age': 221, 'amount': 1.5, 'curve': 4},
 {'age': 251, 'amount': 4.0, 'curve': 4},
 {'age': 105, 'amount': 2.5, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0xb5 0x04 0x3c 0xdd 0x04    \.x..<..
    0008   0xa0 0xfb 0x04 0x64 0x69 0x14              ...di.
    decimal
             92   14  120  181    4   60  221    4
            160  251    4  100  105   20
    datetime (unknown)

    body (0)

#### RECORD 8 SensorAlert 2015-02-26T11:40:59 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-26T11:40:59)
    0000   0x3b 0xa8 0x2b 0xba 0x0f                   ;.+..
    body (0)

#### RECORD 9 BasalProfileStart 2015-02-26T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-26T12:00:00)
    0000   0x00 0x80 0x0c 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 10 SensorAlert 2015-02-26T12:25:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-26T12:25:47)
    0000   0x2f 0x99 0x2c 0xba 0x0f                   /.,..
    body (0)

#### RECORD 11 Bolus 2015-02-26T12:26:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x08 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    8    0
    datetime (2015-02-26T12:26:18)
    0000   0x12 0x9a 0x4c 0x7a 0x0f                   ..Lz.
    body (0)

#### RECORD 12 BolusWizard 2015-02-26T13:26:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.7,
 'carb_input': 30,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-26T13:26:09)
    0000   0x09 0x9a 0x0d 0x7a 0x0f                   ...z.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x94 0x00 0x00 0x00 0x00 0x94 0x78         ......x
    decimal
             30   80    0   80   40   90    0    0
            148    0    0    0    0  148  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 2.0, 'curve': 4},
 {'age': 31, 'amount': 3.0, 'curve': 20},
 {'age': 71, 'amount': 1.5, 'curve': 20},
 {'age': 101, 'amount': 4.0, 'curve': 20},
 {'age': 211, 'amount': 2.5, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x50 0x43 0x04 0x78 0x1f 0x14    \.PC.x..
    0008   0x3c 0x47 0x14 0xa0 0x65 0x14 0x64 0xd3    <G..e.d.
    0010   0x14                                       .
    decimal
             92   17   80   67    4  120   31   20
             60   71   20  160  101   20  100  211
             20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2015-02-26T13:26:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7,
 'duration': 0,
 'programmed': 3.7,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0x40 0x00    ......@.
    decimal
              1    0  148    0  148    0   64    0
    datetime (2015-02-26T13:26:09)
    0000   0x09 0x9a 0x4d 0x7a 0x0f                   ..Mz.
    body (0)

#### RECORD 15 SensorAlert 2015-02-26T14:29:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-26T14:29:30)
    0000   0x1e 0x9d 0x2e 0xba 0x0f                   .....
    body (0)

#### RECORD 16 SensorAlert 2015-02-26T14:35:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-26T14:35:38)
    0000   0x26 0xa3 0x2e 0xba 0x0f                   &....
    body (0)

#### RECORD 17 BolusWizard 2015-02-26T14:48:54 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.7,
 'carb_input': 30,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-26T14:48:54)
    0000   0x36 0xb0 0x0e 0x7a 0x0f                   6..z.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x94 0x00 0x00 0x00 0x00 0x94 0x78         ......x
    decimal
             30   80    0   80   40   90    0    0
            148    0    0    0    0  148  120

#### RECORD 18 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 89, 'amount': 3.7, 'curve': 4},
 {'age': 149, 'amount': 2.0, 'curve': 4},
 {'age': 113, 'amount': 3.0, 'curve': 20},
 {'age': 153, 'amount': 1.5, 'curve': 20},
 {'age': 183, 'amount': 4.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x94 0x59 0x04 0x50 0x95 0x04    \..Y.P..
    0008   0x78 0x71 0x14 0x3c 0x99 0x14 0xa0 0xb7    xq.<....
    0010   0x14                                       .
    decimal
             92   17  148   89    4   80  149    4
            120  113   20   60  153   20  160  183
             20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2015-02-26T14:48:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7,
 'duration': 0,
 'programmed': 3.7,
 'type': 'normal',
 'unabsorbed': 3.1}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0x7c 0x00    ......|.
    decimal
              1    0  148    0  148    0  124    0
    datetime (2015-02-26T14:48:54)
    0000   0x36 0xb0 0x4e 0x7a 0x0f                   6.Nz.
    body (0)

#### RECORD 20 BasalProfileStart 2015-02-26T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-26T15:00:00)
    0000   0x00 0x80 0x0f 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 21 SensorAlert 2015-02-26T16:04:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 201}
```
    op hex (3)
    0000   0x0b 0x65 0xc9                             .e.
    decimal
             11  101  201
    datetime (2015-02-26T16:04:49)
    0000   0x31 0x84 0x30 0xba 0x0f                   1.0..
    body (0)

#### RECORD 22 SensorAlert 2015-02-26T16:41:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-26T16:41:00)
    0000   0x00 0xa9 0x30 0xba 0x0f                   ..0..
    body (0)

#### RECORD 23 BolusWizard 2015-02-26T16:54:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.6,
 'carb_input': 45,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-26T16:54:57)
    0000   0x39 0xb6 0x10 0x7a 0x0f                   9..z.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    -P.P(Z..
    0008   0xe0 0x00 0x00 0x00 0x00 0xe0 0x78         ......x
    decimal
             45   80    0   80   40   90    0    0
            224    0    0    0    0  224  120

#### RECORD 24 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 125, 'amount': 3.55, 'curve': 4},
 {'age': 135, 'amount': 0.15, 'curve': 4},
 {'age': 215, 'amount': 3.7, 'curve': 4},
 {'age': 19, 'amount': 2.0, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x8e 0x7d 0x04 0x06 0x87 0x04    \..}....
    0008   0x94 0xd7 0x04 0x50 0x13 0x14              ...P..
    decimal
             92   14  142  125    4    6  135    4
            148  215    4   80   19   20
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2015-02-26T16:54:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.6,
 'duration': 0,
 'programmed': 5.6,
 'type': 'normal',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0xe0 0x00 0xe0 0x00 0x50 0x00    ......P.
    decimal
              1    0  224    0  224    0   80    0
    datetime (2015-02-26T16:54:57)
    0000   0x39 0xb6 0x50 0x7a 0x0f                   9.Pz.
    body (0)

#### RECORD 26 SensorAlert 2015-02-26T17:36:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 210}
```
    op hex (3)
    0000   0x0b 0x65 0xd2                             .e.
    decimal
             11  101  210
    datetime (2015-02-26T17:36:06)
    0000   0x06 0xa4 0x31 0xba 0x0f                   ..1..
    body (0)

#### RECORD 27 CalBGForPH 2015-02-26T17:37:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 210}
```
    op hex (2)
    0000   0x0a 0xd2                                  ..
    decimal
             10  210
    datetime (2015-02-26T17:37:53)
    0000   0x35 0xa5 0x31 0x7a 0x0f                   5.1z.
    body (0)

#### RECORD 28 BGReceived 2015-02-26T17:37:53 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2015-02-26T17:37:53)
    0000   0x35 0xa5 0x51 0x7a 0x0f                   5.Qz.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 29 BolusWizard 2015-02-26T17:38:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 210,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.3,
 'carb_input': 35,
 'carb_ratio': 12.0,
 'correction_estimate': 2.2,
 'food_estimate': 4.3,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 5.7}
```
    op hex (2)
    0000   0x5b 0xd2                                  [.
    decimal
             91  210
    datetime (2015-02-26T17:38:32)
    0000   0x20 0xa6 0x11 0x7a 0x0f                    ..z.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x50 0x28 0x5a 0x58 0x00    #P.P(ZX.
    0008   0xac 0x00 0x00 0xe4 0x00 0xac 0x78         ......x
    decimal
             35   80    0   80   40   90   88    0
            172    0    0  228    0  172  120

#### RECORD 30 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 49, 'amount': 5.6, 'curve': 4},
 {'age': 169, 'amount': 3.55, 'curve': 4},
 {'age': 179, 'amount': 0.15, 'curve': 4},
 {'age': 3, 'amount': 3.7, 'curve': 20},
 {'age': 63, 'amount': 2.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0xe0 0x31 0x04 0x8e 0xa9 0x04    \..1....
    0008   0x06 0xb3 0x04 0x94 0x03 0x14 0x50 0x3f    ......P?
    0010   0x14                                       .
    decimal
             92   17  224   49    4  142  169    4
              6  179    4  148    3   20   80   63
             20
    datetime (unknown)

    body (0)

#### RECORD 31 Bolus 2015-02-26T17:38:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3,
 'duration': 0,
 'programmed': 4.3,
 'type': 'normal',
 'unabsorbed': 5.7}
```
    op hex (8)
    0000   0x01 0x00 0xac 0x00 0xac 0x00 0xe4 0x00    ........
    decimal
              1    0  172    0  172    0  228    0
    datetime (2015-02-26T17:38:32)
    0000   0x20 0xa6 0x51 0x7a 0x0f                    .Qz.
    body (0)

#### RECORD 32 LowReservoir 2015-02-26T17:42:19 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-02-26T17:42:19)
    0000   0x13 0xaa 0x11 0x1a 0x0f                   .....
    body (0)

#### RECORD 33 Bolus 2015-02-26T17:41:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 3.5}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x01 0x8c 0x00    ..(.(...
    decimal
              1    0   40    0   40    1  140    0
    datetime (2015-02-26T17:41:51)
    0000   0x33 0xa9 0x51 0x7a 0x0f                   3.Qz.
    body (0)

#### RECORD 34 SensorAlert 2015-02-26T19:09:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-26T19:09:30)
    0000   0x1e 0x89 0x33 0xba 0x0f                   ..3..
    body (0)

#### RECORD 35 SensorAlert 2015-02-26T19:24:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-26T19:24:49)
    0000   0x31 0x98 0x33 0xba 0x0f                   1.3..
    body (0)

#### RECORD 36 CalBGForPH 2015-02-26T19:26:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2015-02-26T19:26:03)
    0000   0x03 0x9a 0x33 0x7a 0x0f                   ..3z.
    body (0)

#### RECORD 37 BGReceived 2015-02-26T19:26:03 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2015-02-26T19:26:03)
    0000   0x03 0x9a 0x13 0x7a 0x0f                   ...z.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 38 CalBGForPH 2015-02-26T20:26:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 310}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2015-02-26T20:26:21)
    0000   0x15 0x9a 0x34 0x7a 0x8f                   ..4z.
    body (0)

#### RECORD 39 BGReceived 2015-02-26T20:26:21 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x26                                  ?&
    decimal
             63   38
    datetime (2015-02-26T20:26:21)
    0000   0x15 0x9a 0xd4 0x7a 0x0f                   ...z.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 40 BolusWizard 2015-02-26T20:26:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 310,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.0,
 'carb_input': 0,
 'carb_ratio': 12.0,
 'correction_estimate': -1.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.7}
```
    op hex (2)
    0000   0x5b 0x36                                  [6
    decimal
             91   54
    datetime (2015-02-26T20:26:27)
    0000   0x1b 0x9a 0x14 0x1a 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x3c 0x28 0x5a 0xbc 0x00    .Q.<(Z..
    0008   0x00 0x00 0x00 0x44 0x00 0x78 0x78         ...D.xx
    decimal
              0   81    0   60   40   90  188    0
              0    0    0   68    0  120  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 167, 'amount': 4.6, 'curve': 4},
 {'age': 177, 'amount': 0.7, 'curve': 4},
 {'age': 217, 'amount': 5.6, 'curve': 4},
 {'age': 81, 'amount': 3.55, 'curve': 20},
 {'age': 91, 'amount': 0.15, 'curve': 20},
 {'age': 171, 'amount': 3.7, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0xb8 0xa7 0x04 0x1c 0xb1 0x04    \.......
    0008   0xe0 0xd9 0x04 0x8e 0x51 0x14 0x06 0x5b    ....Q..[
    0010   0x14 0x94 0xab 0x14                        ....
    decimal
             92   20  184  167    4   28  177    4
            224  217    4  142   81   20    6   91
             20  148  171   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2015-02-26T20:26:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x44 0x00    ..x.x.D.
    decimal
              1    0  120    0  120    0   68    0
    datetime (2015-02-26T20:26:27)
    0000   0x1b 0x9a 0x54 0x1a 0x0f                   ..T..
    body (0)

#### RECORD 43 SensorAlert 2015-02-26T20:56:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 24}
```
    op hex (3)
    0000   0x0b 0x65 0x18                             .e.
    decimal
             11  101   24
    datetime (2015-02-26T20:56:06)
    0000   0x06 0xb8 0x34 0xba 0x8f                   ..4..
    body (0)

#### RECORD 44 CalBGForPH 2015-02-26T21:57:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 214}
```
    op hex (2)
    0000   0x0a 0xd6                                  ..
    decimal
             10  214
    datetime (2015-02-26T21:57:43)
    0000   0x2b 0xb9 0x35 0x7a 0x0f                   +.5z.
    body (0)

#### RECORD 45 BGReceived 2015-02-26T21:57:43 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2015-02-26T21:57:43)
    0000   0x2b 0xb9 0xd5 0x7a 0x0f                   +..z.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 46 BolusWizard 2015-02-26T21:57:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 214,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 12.0,
 'correction_estimate': 2.3,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.8}
```
    op hex (2)
    0000   0x5b 0xd6                                  [.
    decimal
             91  214
    datetime (2015-02-26T21:57:56)
    0000   0x38 0xb9 0x15 0x1a 0x0f                   8....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x3c 0x28 0x5a 0x5c 0x00    .P.<(Z\.
    0008   0x00 0x00 0x00 0x48 0x00 0x14 0x78         ...H..x
    decimal
              0   80    0   60   40   90   92    0
              0    0    0   72    0   20  120

#### RECORD 47 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 3.0, 'curve': 4},
 {'age': 2, 'amount': 4.6, 'curve': 20},
 {'age': 12, 'amount': 0.7, 'curve': 20},
 {'age': 52, 'amount': 5.6, 'curve': 20},
 {'age': 172, 'amount': 3.55, 'curve': 20},
 {'age': 182, 'amount': 0.15, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x78 0x62 0x04 0xb8 0x02 0x14    \.xb....
    0008   0x1c 0x0c 0x14 0xe0 0x34 0x14 0x8e 0xac    ....4...
    0010   0x14 0x06 0xb6 0x14                        ....
    decimal
             92   20  120   98    4  184    2   20
             28   12   20  224   52   20  142  172
             20    6  182   20
    datetime (unknown)

    body (0)

#### RECORD 48 Bolus 2015-02-26T21:57:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x48 0x00    ......H.
    decimal
              1    0   20    0   20    0   72    0
    datetime (2015-02-26T21:57:56)
    0000   0x38 0xb9 0x55 0x1a 0x0f                   8.U..
    body (0)

#### RECORD 49 BasalProfileStart 2015-02-26T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-26T22:00:00)
    0000   0x00 0x80 0x16 0x1a 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 50 LowReservoir 2015-02-26T22:14:43 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-02-26T22:14:43)
    0000   0x2b 0x8e 0x16 0x1a 0x0f                   +....
    body (0)

#### RECORD 51 Bolus 2015-02-26T22:12:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x50 0x00    ......P.
    decimal
              1    0  140    0  140    0   80    0
    datetime (2015-02-26T22:12:59)
    0000   0x3b 0x8c 0x56 0x7a 0x0f                   ;.Vz.
    body (0)

#### RECORD 52 SensorAlert 2015-02-26T22:25:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 220}
```
    op hex (3)
    0000   0x0b 0x65 0xdc                             .e.
    decimal
             11  101  220
    datetime (2015-02-26T22:25:47)
    0000   0x2f 0x99 0x36 0xba 0x0f                   /.6..
    body (0)

#### RECORD 53 BasalProfileStart 2015-02-27T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-27T00:00:00)
    0000   0x00 0x80 0x00 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 54 MResultTotals 2015-02-27T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0xc1                   .....
    decimal
              7    0    0    9  193
    datetime (2015-02-27T00:00:00)
    0000   0x3a 0x0f                                  :.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 55 Sara6E 2015-02-27T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-27T00:00:00)
    0000   0x3a 0x0f                                  :.
    body (49)
    hex
    0000   0x05 0x10 0xd7 0x8f 0x36 0x05 0x00 0x00    ....6...
    0008   0x09 0xc1 0x03 0x25 0x20 0x06 0x9c 0x44    ...% ..D
    0010   0x00 0xdc 0x03 0xcc 0x00 0x8c 0x00 0x00    ........
    0018   0x02 0x44 0x06 0x02 0x00 0x06 0x00 0xc9    .D......
    0020   0x3a 0x2a 0x00 0x09 0x35 0x05 0x00 0x00    :*..5...
    0028   0x00 0x00 0x09 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  215  143   54    5    0    0
              9  193    3   37   32    6  156   68
              0  220    3  204    0  140    0    0
              2   68    6    2    0    6    0  201
             58   42    0    9   53    5    0    0
              0    0    9    1    0    0    0    0
              0

#### RECORD 56 SensorAlert 2015-02-27T02:10:11 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-27T02:10:11)
    0000   0x0b 0x8a 0x22 0xbb 0x0f                   .."..
    body (0)

#### RECORD 57 SensorAlert 2015-02-27T02:16:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-02-27T02:16:06)
    0000   0x06 0x90 0x22 0xbb 0x0f                   .."..
    body (0)

#### RECORD 58 BasalProfileStart 2015-02-27T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-27T04:00:00)
    0000   0x00 0x80 0x04 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 59 SensorAlert 2015-02-27T05:36:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-27T05:36:05)
    0000   0x05 0xa4 0x25 0xbb 0x0f                   ..%..
    body (0)

#### RECORD 60 SensorAlert 2015-02-27T06:29:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-27T06:29:29)
    0000   0x1d 0x9d 0x26 0xbb 0x0f                   ..&..
    body (0)

#### RECORD 61 BasalProfileStart 2015-02-27T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-27T07:00:00)
    0000   0x00 0x80 0x07 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 62 SensorAlert 2015-02-27T07:36:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-27T07:36:05)
    0000   0x05 0xa4 0x27 0xbb 0x0f                   ..'..
    body (0)

#### RECORD 63 BolusWizard 2015-02-27T07:40:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.6,
 'carb_input': 70,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-27T07:40:32)
    0000   0x20 0xa8 0x07 0x7b 0x0f                    ..{.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    FP.d(Z..
    0008   0x18 0x00 0x00 0x00 0x01 0x18 0x78         ......x
    decimal
             70   80    0  100   40   90    0    1
             24    0    0    0    1   24  120

#### RECORD 64 Bolus 2015-02-27T07:40:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6,
 'duration': 0,
 'programmed': 0.6,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x00 0x00    ........
    decimal
              1    1   24    1   24    0    0    0
    datetime (2015-02-27T07:40:32)
    0000   0x20 0xa8 0x47 0x7b 0x0f                    .G{.
    body (0)

#### RECORD 65 SensorAlert 2015-02-27T07:45:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 189}
```
    op hex (3)
    0000   0x0b 0x65 0xbd                             .e.
    decimal
             11  101  189
    datetime (2015-02-27T07:45:46)
    0000   0x2e 0xad 0x27 0xbb 0x0f                   ..'..
    body (0)

#### RECORD 66 PumpSuspend 2015-02-27T08:12:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-27T08:12:49)
    0000   0x31 0x8c 0x08 0x1b 0x0f                   1....
    body (0)

#### RECORD 67 BasalProfileStart 2015-02-27T08:38:03 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-27T08:38:03)
    0000   0x03 0xa6 0x08 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 68 PumpResume 2015-02-27T08:38:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-27T08:38:04)
    0000   0x04 0xa6 0x08 0x1b 0x0f                   .....
    body (0)

#### RECORD 69 SensorAlert 2015-02-27T08:57:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-27T08:57:00)
    0000   0x00 0xb9 0x28 0xbb 0x0f                   ..(..
    body (0)

#### RECORD 70 SensorAlert 2015-02-27T09:15:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 233}
```
    op hex (3)
    0000   0x0b 0x65 0xe9                             .e.
    decimal
             11  101  233
    datetime (2015-02-27T09:15:37)
    0000   0x25 0x8f 0x29 0xbb 0x0f                   %.)..
    body (0)

#### RECORD 71 Bolus 2015-02-27T09:15:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 4.3}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xac 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  172    0
    datetime (2015-02-27T09:15:16)
    0000   0x10 0x8f 0x49 0x7b 0x0f                   ..I{.
    body (0)

#### RECORD 72 SensorAlert 2015-02-27T09:57:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-27T09:57:00)
    0000   0x00 0xb9 0x29 0xbb 0x0f                   ..)..
    body (0)

#### RECORD 73 BasalProfileStart 2015-02-27T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-27T10:00:00)
    0000   0x00 0x80 0x0a 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 74 CalBGForPH 2015-02-27T10:01:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 245}
```
    op hex (2)
    0000   0x0a 0xf5                                  ..
    decimal
             10  245
    datetime (2015-02-27T10:01:53)
    0000   0x35 0x81 0x2a 0x7b 0x0f                   5.*{.
    body (0)

#### RECORD 75 BGReceived 2015-02-27T10:01:53 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1e                                  ?.
    decimal
             63   30
    datetime (2015-02-27T10:01:53)
    0000   0x35 0x81 0xaa 0x7b 0x0f                   5..{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 76 Bolus 2015-02-27T10:02:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 3.7}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x94 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  148    0
    datetime (2015-02-27T10:02:03)
    0000   0x03 0x82 0x4a 0x7b 0x0f                   ..J{.
    body (0)

#### RECORD 77 SensorAlert 2015-02-27T10:16:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 253}
```
    op hex (3)
    0000   0x0b 0x65 0xfd                             .e.
    decimal
             11  101  253
    datetime (2015-02-27T10:16:05)
    0000   0x05 0x90 0x2a 0xbb 0x0f                   ..*..
    body (0)

#### RECORD 78 NoDelivery 2015-02-27T11:39:25 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-02-27T11:39:25)
    0000   0x19 0xa7 0x4b 0x5b 0x0f                   ..K[.
    body (0)

#### RECORD 79 ClearAlarm 2015-02-27T11:39:49 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-02-27T11:39:49)
    0000   0x31 0xa7 0x0b 0x1b 0x0f                   1....
    body (0)

#### RECORD 80 Rewind 2015-02-27T11:45:44 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-02-27T11:45:44)
    0000   0x2c 0xad 0x0b 0x1b 0x0f                   ,....
    body (0)

#### RECORD 81 SensorAlert 2015-02-27T11:45:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 46}
```
    op hex (3)
    0000   0x0b 0x65 0x2e                             .e.
    decimal
             11  101   46
    datetime (2015-02-27T11:45:46)
    0000   0x2e 0xad 0x2b 0xbb 0x8f                   ..+..
    body (0)

#### RECORD 82 Prime 2015-02-27T11:49:31 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 5.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x33                   ....3
    decimal
              3    0    0    0   51
    datetime (2015-02-27T11:49:31)
    0000   0x1f 0xb1 0x2b 0x1b 0x0f                   ..+..
    body (0)

#### RECORD 83 BasalProfileStart 2015-02-27T11:50:11 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-27T11:50:11)
    0000   0x0b 0xb2 0x0b 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 84 Prime 2015-02-27T11:49:57 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-02-27T11:49:57)
    0000   0x39 0xb1 0x0b 0x1b 0x0f                   9....
    body (0)

#### RECORD 85 BasalProfileStart 2015-02-27T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-27T12:00:00)
    0000   0x00 0x80 0x0c 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 86 SensorAlert 2015-02-27T13:15:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 71}
```
    op hex (3)
    0000   0x0b 0x65 0x47                             .eG
    decimal
             11  101   71
    datetime (2015-02-27T13:15:37)
    0000   0x25 0x8f 0x2d 0xbb 0x8f                   %.-..
    body (0)

#### RECORD 87 Bolus 2015-02-27T13:19:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0x08 0x00    ........
    decimal
              1    0  240    0  240    0    8    0
    datetime (2015-02-27T13:19:51)
    0000   0x33 0x93 0x4d 0x7b 0x0f                   3.M{.
    body (0)

`end analysis/736868/logs/ReadHistoryData-page-19.data: 88 records`
