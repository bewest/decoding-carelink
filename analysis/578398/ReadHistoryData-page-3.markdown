## START ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 1013, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xfa 0xf3                                  ..
##### DEBUG DECIMAL
            250  243
#### RECORD 0 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 115, 'amount': 0.05, 'curve': 4},
 {'age': 125, 'amount': 0.15, 'curve': 4},
 {'age': 135, 'amount': 0.15, 'curve': 4},
 {'age': 145, 'amount': 0.2, 'curve': 4},
 {'age': 155, 'amount': 0.15, 'curve': 4},
 {'age': 165, 'amount': 0.15, 'curve': 4},
 {'age': 175, 'amount': 3.0, 'curve': 4},
 {'age': 185, 'amount': 0.15, 'curve': 4},
 {'age': 99, 'amount': 1.1, 'curve': 20}]
```
    op hex (29)
    0000   0x5c 0x1d 0x02 0x73 0x04 0x06 0x7d 0x04    \..s..}.
    0008   0x06 0x87 0x04 0x08 0x91 0x04 0x06 0x9b    ........
    0010   0x04 0x06 0xa5 0x04 0x78 0xaf 0x04 0x06    ....x...
    0018   0xb9 0x04 0x2c 0x63 0x14                   ..,c.
    decimal
             92   29    2  115    4    6  125    4
              6  135    4    8  145    4    6  155
              4    6  165    4  120  175    4    6
            185    4   44   99   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-04-26T13:14:13 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'duration': 0, 'programmed': 1.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2015-04-26T13:14:13)
    0000   0x4d 0x0e 0x8d 0x1a 0x0f                   M....
    body (0)

#### RECORD 2 SensorAlert 2015-04-26T13:26:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 229}
```
    op hex (3)
    0000   0x0b 0x65 0xe5                             .e.
    decimal
             11  101  229
    datetime (2015-04-26T13:26:33)
    0000   0x61 0x1a 0x2d 0xba 0x0f                   a.-..
    body (0)

#### RECORD 3 SensorAlert 2015-04-26T14:55:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 317}
```
    op hex (3)
    0000   0x0b 0x65 0x3d                             .e=
    decimal
             11  101   61
    datetime (2015-04-26T14:55:44)
    0000   0x6c 0x37 0x2e 0xba 0x8f                   l7...
    body (0)

#### RECORD 4 BolusWizard 2015-04-26T14:56:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.7,
 'carb_input': 38,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 4.7,
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
    datetime (2015-04-26T14:56:08)
    0000   0x48 0x38 0x0e 0x1a 0x0f                   H8...
    body (13)
    hex
    0000   0x26 0x50 0x08 0x28 0x5a 0x00 0x2f 0x00    &P.(Z./.
    0008   0x00 0x00 0x00 0x2f 0x78                   .../x
    decimal
             38   80    8   40   90    0   47    0
              0    0    0   47  120

#### RECORD 5 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 107, 'amount': 1.9, 'curve': 4},
 {'age': 217, 'amount': 0.05, 'curve': 4},
 {'age': 227, 'amount': 0.15, 'curve': 4},
 {'age': 237, 'amount': 0.15, 'curve': 4},
 {'age': 247, 'amount': 0.2, 'curve': 4},
 {'age': 1, 'amount': 0.15, 'curve': 20},
 {'age': 11, 'amount': 0.15, 'curve': 20},
 {'age': 21, 'amount': 3.0, 'curve': 20},
 {'age': 31, 'amount': 0.15, 'curve': 20},
 {'age': 201, 'amount': 1.1, 'curve': 20}]
```
    op hex (32)
    0000   0x5c 0x20 0x4c 0x6b 0x04 0x02 0xd9 0x04    \ Lk....
    0008   0x06 0xe3 0x04 0x06 0xed 0x04 0x08 0xf7    ........
    0010   0x04 0x06 0x01 0x14 0x06 0x0b 0x14 0x78    .......x
    0018   0x15 0x14 0x06 0x1f 0x14 0x2c 0xc9 0x14    .....,..
    decimal
             92   32   76  107    4    2  217    4
              6  227    4    6  237    4    8  247
              4    6    1   20    6   11   20  120
             21   20    6   31   20   44  201   20
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2015-04-26T14:56:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'duration': 0, 'programmed': 4.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2015-04-26T14:56:08)
    0000   0x48 0x38 0x4e 0x1a 0x0f                   H8N..
    body (0)

#### RECORD 7 SensorAlert 2015-04-26T16:27:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 293}
```
    op hex (3)
    0000   0x0b 0x65 0x25                             .e%
    decimal
             11  101   37
    datetime (2015-04-26T16:27:18)
    0000   0x52 0x1b 0x30 0xba 0x8f                   R.0..
    body (0)

#### RECORD 8 BolusWizard 2015-04-26T16:27:36 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.1,
 'carb_input': 25,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 3.1,
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
    datetime (2015-04-26T16:27:36)
    0000   0x64 0x1b 0x10 0x1a 0x0f                   d....
    body (13)
    hex
    0000   0x19 0x50 0x08 0x28 0x5a 0x00 0x1f 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x1f 0x78                   ....x
    decimal
             25   80    8   40   90    0   31    0
              0    0    0   31  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 88, 'amount': 0.4, 'curve': 4},
 {'age': 98, 'amount': 4.3, 'curve': 4},
 {'age': 198, 'amount': 1.9, 'curve': 4},
 {'age': 52, 'amount': 0.05, 'curve': 20},
 {'age': 62, 'amount': 0.15, 'curve': 20},
 {'age': 72, 'amount': 0.15, 'curve': 20},
 {'age': 82, 'amount': 0.2, 'curve': 20},
 {'age': 92, 'amount': 0.15, 'curve': 20},
 {'age': 102, 'amount': 0.15, 'curve': 20},
 {'age': 112, 'amount': 3.0, 'curve': 20},
 {'age': 122, 'amount': 0.15, 'curve': 20}]
```
    op hex (35)
    0000   0x5c 0x23 0x10 0x58 0x04 0xac 0x62 0x04    \#.X..b.
    0008   0x4c 0xc6 0x04 0x02 0x34 0x14 0x06 0x3e    L...4..>
    0010   0x14 0x06 0x48 0x14 0x08 0x52 0x14 0x06    ..H..R..
    0018   0x5c 0x14 0x06 0x66 0x14 0x78 0x70 0x14    \..f.xp.
    0020   0x06 0x7a 0x14                             .z.
    decimal
             92   35   16   88    4  172   98    4
             76  198    4    2   52   20    6   62
             20    6   72   20    8   82   20    6
             92   20    6  102   20  120  112   20
              6  122   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2015-04-26T16:27:36 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'duration': 0, 'programmed': 3.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2015-04-26T16:27:36)
    0000   0x64 0x1b 0x50 0x1a 0x0f                   d.P..
    body (0)

#### RECORD 11 CalBGForPH 2015-04-26T17:21:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 212}
```
    op hex (2)
    0000   0x0a 0xd4                                  ..
    decimal
             10  212
    datetime (2015-04-26T17:21:10)
    0000   0x4a 0x15 0x31 0x7a 0x0f                   J.1z.
    body (0)

#### RECORD 12 BGReceived 2015-04-26T17:21:10 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 212, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2015-04-26T17:21:10)
    0000   0x4a 0x15 0x91 0x7a 0x0f                   J..z.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 13 SensorAlert 2015-04-26T17:56:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-04-26T17:56:42)
    0000   0x6a 0x38 0x31 0xba 0x0f                   j81..
    body (0)

#### RECORD 14 SensorAlert 2015-04-26T19:01:23 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 112'}
```
    op hex (3)
    0000   0x0b 0x70 0x00                             .p.
    decimal
             11  112    0
    datetime (2015-04-26T19:01:23)
    0000   0x57 0x01 0x33 0xba 0x0f                   W.3..
    body (0)

#### RECORD 15 SensorAlert 2015-04-26T19:07:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 113'}
```
    op hex (3)
    0000   0x0b 0x71 0x00                             .q.
    decimal
             11  113    0
    datetime (2015-04-26T19:07:20)
    0000   0x54 0x07 0x33 0xba 0x0f                   T.3..
    body (0)

#### RECORD 16 SensorAlert 2015-04-26T19:15:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-04-26T19:15:00)
    0000   0x40 0x0f 0x33 0xba 0x0f                   @.3..
    body (0)

#### RECORD 17 BolusWizard 2015-04-26T19:33:06 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.6,
 'carb_input': 40,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 6.6,
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
    datetime (2015-04-26T19:33:06)
    0000   0x46 0x21 0x13 0x1a 0x0f                   F!...
    body (13)
    hex
    0000   0x28 0x50 0x06 0x28 0x5a 0x00 0x42 0x00    (P.(Z.B.
    0008   0x00 0x00 0x00 0x42 0x78                   ...Bx
    decimal
             40   80    6   40   90    0   66    0
              0    0    0   66  120

#### RECORD 18 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 184, 'amount': 1.0, 'curve': 4},
 {'age': 194, 'amount': 2.1, 'curve': 4},
 {'age': 18, 'amount': 0.4, 'curve': 20},
 {'age': 28, 'amount': 4.3, 'curve': 20},
 {'age': 128, 'amount': 1.9, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x28 0xb8 0x04 0x54 0xc2 0x04    \.(..T..
    0008   0x10 0x12 0x14 0xac 0x1c 0x14 0x4c 0x80    ......L.
    0010   0x14                                       .
    decimal
             92   17   40  184    4   84  194    4
             16   18   20  172   28   20   76  128
             20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2015-04-26T19:33:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'duration': 0, 'programmed': 3.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2015-04-26T19:33:06)
    0000   0x46 0x21 0x93 0x1a 0x0f                   F!...
    body (0)

#### RECORD 20 Bolus 2015-04-26T19:35:26 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'duration': 120, 'programmed': 3.1, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x04                        ....
    decimal
              1   31   31    4
    datetime (2015-04-26T19:35:26)
    0000   0x5a 0x23 0xb3 0x1a 0x0f                   Z#...
    body (0)

#### RECORD 21 CalBGForPH 2015-04-26T22:43:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 48}
```
    op hex (2)
    0000   0x0a 0x30                                  .0
    decimal
             10   48
    datetime (2015-04-26T22:43:12)
    0000   0x4c 0x2b 0x36 0x7a 0x0f                   L+6z.
    body (0)

#### RECORD 22 BGReceived 2015-04-26T22:43:12 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 48, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2015-04-26T22:43:12)
    0000   0x4c 0x2b 0x16 0x7a 0x0f                   L+.z.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 23 MResultTotals 2015-04-27T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xb6                   .....
    decimal
              7    0    0    6  182
    datetime (2015-04-27T00:00:00)
    0000   0x5a 0x0f                                  Z.
    body (0)

#### RECORD 24 Model522ResultTotals 2015-04-27T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-27T00:00:00)
    0000   0x5a 0x0f                                  Z.
    body (41)
    hex
    0000   0x05 0x00 0xa5 0x30 0xea 0x03 0x00 0x00    ...0....
    0008   0x06 0xb6 0x03 0x2c 0x2f 0x03 0x8a 0x35    ...,/..5
    0010   0x00 0x8f 0x03 0x8a 0x35 0x03 0x12 0x57    ....5..W
    0018   0x00 0x78 0x0d 0x00 0x00 0x00 0x06 0x04    .x......
    0020   0x02 0x00 0x00 0x10 0xe0 0x84 0x75 0xcb    ......u.
    0028   0x03                                       .
    decimal
              5    0  165   48  234    3    0    0
              6  182    3   44   47    3  138   53
              0  143    3  138   53    3   18   87
              0  120   13    0    0    0    6    4
              2    0    0   16  224  132  117  203
              3

#### RECORD 25 PumpSuspend 2015-04-27T07:10:58 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-27T07:10:58)
    0000   0x7a 0x0a 0x07 0x1b 0x0f                   z....
    body (0)

#### RECORD 26 PumpResume 2015-04-27T08:07:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-27T08:07:03)
    0000   0x43 0x07 0x08 0x1b 0x0f                   C....
    body (0)

#### RECORD 27 BolusWizard 2015-04-27T08:07:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.3,
 'carb_input': 53,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 5.3,
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
    datetime (2015-04-27T08:07:18)
    0000   0x52 0x07 0x08 0x1b 0x0f                   R....
    body (13)
    hex
    0000   0x35 0x50 0x0a 0x28 0x5a 0x00 0x35 0x00    5P.(Z.5.
    0008   0x00 0x00 0x00 0x35 0x78                   ...5x
    decimal
             53   80   10   40   90    0   53    0
              0    0    0   53  120

#### RECORD 28 LowReservoir 2015-04-27T08:07:36 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-04-27T08:07:36)
    0000   0x64 0x07 0x08 0x1b 0x0f                   d....
    body (0)

#### RECORD 29 Bolus 2015-04-27T08:07:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'duration': 0, 'programmed': 3.9, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2015-04-27T08:07:18)
    0000   0x52 0x07 0x88 0x1b 0x0f                   R....
    body (0)

#### RECORD 30 Bolus 2015-04-27T08:09:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'duration': 60, 'programmed': 1.4, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x02                        ....
    decimal
              1   14   14    2
    datetime (2015-04-27T08:09:52)
    0000   0x74 0x09 0xa8 0x1b 0x0f                   t....
    body (0)

#### RECORD 31 SensorAlert 2015-04-27T10:02:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-27T10:02:55)
    0000   0x77 0x02 0x2a 0xbb 0x0f                   w.*..
    body (0)

#### RECORD 32 CalBGForPH 2015-04-27T10:05:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 319}
```
    op hex (2)
    0000   0x0a 0x3f                                  .?
    decimal
             10   63
    datetime (2015-04-27T10:05:30)
    0000   0x5e 0x05 0x2a 0x7b 0x8f                   ^.*{.
    body (0)

#### RECORD 33 BGReceived 2015-04-27T10:05:30 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 319, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x27                                  ?'
    decimal
             63   39
    datetime (2015-04-27T10:05:30)
    0000   0x5e 0x05 0xea 0x7b 0x0f                   ^..{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 34 BolusWizard 2015-04-27T10:05:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 49,
 '_byte[7]': 0,
 'bg': 319,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x3f                                  [?
    decimal
             91   63
    datetime (2015-04-27T10:05:41)
    0000   0x69 0x05 0x0a 0x1b 0x0f                   i....
    body (13)
    hex
    0000   0x00 0x51 0x0a 0x28 0x5a 0x31 0x00 0x00    .Q.(Z1..
    0008   0x00 0x1b 0x00 0x16 0x78                   ....x
    decimal
              0   81   10   40   90   49    0    0
              0   27    0   22  120

#### RECORD 35 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 0.25, 'curve': 4},
 {'age': 76, 'amount': 0.25, 'curve': 4},
 {'age': 86, 'amount': 0.2, 'curve': 4},
 {'age': 96, 'amount': 0.25, 'curve': 4},
 {'age': 106, 'amount': 0.25, 'curve': 4},
 {'age': 116, 'amount': 1.55, 'curve': 4},
 {'age': 126, 'amount': 2.55, 'curve': 4}]
```
    op hex (23)
    0000   0x5c 0x17 0x0a 0x42 0x04 0x0a 0x4c 0x04    \..B..L.
    0008   0x08 0x56 0x04 0x0a 0x60 0x04 0x0a 0x6a    .V..`..j
    0010   0x04 0x3e 0x74 0x04 0x66 0x7e 0x04         .>t.f~.
    decimal
             92   23   10   66    4   10   76    4
              8   86    4   10   96    4   10  106
              4   62  116    4  102  126    4
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2015-04-27T10:05:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'duration': 0, 'programmed': 2.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2015-04-27T10:05:41)
    0000   0x69 0x05 0x8a 0x1b 0x0f                   i....
    body (0)

#### RECORD 37 SensorAlert 2015-04-27T10:19:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-27T10:19:05)
    0000   0x45 0x13 0x2a 0xbb 0x0f                   E.*..
    body (0)

#### RECORD 38 SensorAlert 2015-04-27T10:19:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 106'}
```
    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2015-04-27T10:19:05)
    0000   0x45 0x13 0x2a 0xbb 0x0f                   E.*..
    body (0)

#### RECORD 39 CalBGForPH 2015-04-27T10:19:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 301}
```
    op hex (2)
    0000   0x0a 0x2d                                  .-
    decimal
             10   45
    datetime (2015-04-27T10:19:48)
    0000   0x70 0x13 0x2a 0x7b 0x8f                   p.*{.
    body (0)

#### RECORD 40 BGReceived 2015-04-27T10:19:48 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 301, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x25                                  ?%
    decimal
             63   37
    datetime (2015-04-27T10:19:48)
    0000   0x70 0x13 0xaa 0x7b 0x0f                   p..{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 41 SensorAlert 2015-04-27T10:33:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 301}
```
    op hex (3)
    0000   0x0b 0x65 0x2d                             .e-
    decimal
             11  101   45
    datetime (2015-04-27T10:33:44)
    0000   0x6c 0x21 0x2a 0xbb 0x8f                   l!*..
    body (0)

#### RECORD 42 BolusWizard 2015-04-27T10:54:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.1,
 'carb_input': 21,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 2.1,
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
    datetime (2015-04-27T10:54:35)
    0000   0x63 0x36 0x0a 0x1b 0x0f                   c6...
    body (13)
    hex
    0000   0x15 0x50 0x0a 0x28 0x5a 0x00 0x15 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x15 0x78                   ....x
    decimal
             21   80   10   40   90    0   21    0
              0    0    0   21  120

#### RECORD 43 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 2.2, 'curve': 4},
 {'age': 115, 'amount': 0.25, 'curve': 4},
 {'age': 125, 'amount': 0.25, 'curve': 4},
 {'age': 135, 'amount': 0.2, 'curve': 4},
 {'age': 145, 'amount': 0.25, 'curve': 4},
 {'age': 155, 'amount': 0.25, 'curve': 4},
 {'age': 165, 'amount': 1.55, 'curve': 4},
 {'age': 175, 'amount': 2.55, 'curve': 4}]
```
    op hex (26)
    0000   0x5c 0x1a 0x58 0x37 0x04 0x0a 0x73 0x04    \.X7..s.
    0008   0x0a 0x7d 0x04 0x08 0x87 0x04 0x0a 0x91    .}......
    0010   0x04 0x0a 0x9b 0x04 0x3e 0xa5 0x04 0x66    ....>..f
    0018   0xaf 0x04                                  ..
    decimal
             92   26   88   55    4   10  115    4
             10  125    4    8  135    4   10  145
              4   10  155    4   62  165    4  102
            175    4
    datetime (unknown)

    body (0)

#### RECORD 44 LowReservoir 2015-04-27T10:54:59 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-04-27T10:54:59)
    0000   0x7b 0x36 0x0a 0x1b 0x0f                   {6...
    body (0)

#### RECORD 45 Bolus 2015-04-27T10:54:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.1, 'duration': 0, 'programmed': 2.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x15 0x15 0x00                        ....
    decimal
              1   21   21    0
    datetime (2015-04-27T10:54:35)
    0000   0x63 0x36 0x4a 0x1b 0x0f                   c6J..
    body (0)

#### RECORD 46 CalBGForPH 2015-04-27T11:24:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 290}
```
    op hex (2)
    0000   0x0a 0x22                                  ."
    decimal
             10   34
    datetime (2015-04-27T11:24:24)
    0000   0x58 0x18 0x2b 0x7b 0x8f                   X.+{.
    body (0)

#### RECORD 47 BGReceived 2015-04-27T11:24:24 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 290, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x24                                  ?$
    decimal
             63   36
    datetime (2015-04-27T11:24:24)
    0000   0x58 0x18 0x4b 0x7b 0x0f                   X.K{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 48 SensorAlert 2015-04-27T12:02:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 323}
```
    op hex (3)
    0000   0x0b 0x65 0x43                             .eC
    decimal
             11  101   67
    datetime (2015-04-27T12:02:55)
    0000   0x77 0x02 0x2c 0xbb 0x8f                   w.,..
    body (0)

#### RECORD 49 BolusWizard 2015-04-27T12:03:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.2,
 'carb_input': 18,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 2.2,
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
    datetime (2015-04-27T12:03:30)
    0000   0x5e 0x03 0x0c 0x1b 0x0f                   ^....
    body (13)
    hex
    0000   0x12 0x50 0x08 0x28 0x5a 0x00 0x16 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x16 0x78                   ....x
    decimal
             18   80    8   40   90    0   22    0
              0    0    0   22  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 74, 'amount': 2.1, 'curve': 4},
 {'age': 124, 'amount': 2.2, 'curve': 4},
 {'age': 184, 'amount': 0.25, 'curve': 4},
 {'age': 194, 'amount': 0.25, 'curve': 4},
 {'age': 204, 'amount': 0.2, 'curve': 4},
 {'age': 214, 'amount': 0.25, 'curve': 4},
 {'age': 224, 'amount': 0.25, 'curve': 4},
 {'age': 234, 'amount': 1.55, 'curve': 4},
 {'age': 244, 'amount': 2.55, 'curve': 4}]
```
    op hex (29)
    0000   0x5c 0x1d 0x54 0x4a 0x04 0x58 0x7c 0x04    \.TJ.X|.
    0008   0x0a 0xb8 0x04 0x0a 0xc2 0x04 0x08 0xcc    ........
    0010   0x04 0x0a 0xd6 0x04 0x0a 0xe0 0x04 0x3e    .......>
    0018   0xea 0x04 0x66 0xf4 0x04                   ..f..
    decimal
             92   29   84   74    4   88  124    4
             10  184    4   10  194    4    8  204
              4   10  214    4   10  224    4   62
            234    4  102  244    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2015-04-27T12:03:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2, 'duration': 0, 'programmed': 2.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x16 0x16 0x00                        ....
    decimal
              1   22   22    0
    datetime (2015-04-27T12:03:30)
    0000   0x5e 0x03 0x4c 0x1b 0x0f                   ^.L..
    body (0)

#### RECORD 52 BolusWizard 2015-04-27T12:14:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.2,
 'carb_input': 50,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 6.2,
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
    datetime (2015-04-27T12:14:21)
    0000   0x55 0x0e 0x0c 0x1b 0x0f                   U....
    body (13)
    hex
    0000   0x32 0x50 0x08 0x28 0x5a 0x00 0x3e 0x00    2P.(Z.>.
    0008   0x00 0x00 0x00 0x3e 0x78                   ...>x
    decimal
             50   80    8   40   90    0   62    0
              0    0    0   62  120

#### RECORD 53 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 15, 'amount': 2.2, 'curve': 4},
 {'age': 85, 'amount': 2.1, 'curve': 4},
 {'age': 135, 'amount': 2.2, 'curve': 4},
 {'age': 195, 'amount': 0.25, 'curve': 4},
 {'age': 205, 'amount': 0.25, 'curve': 4},
 {'age': 215, 'amount': 0.2, 'curve': 4},
 {'age': 225, 'amount': 0.25, 'curve': 4},
 {'age': 235, 'amount': 0.25, 'curve': 4},
 {'age': 245, 'amount': 1.55, 'curve': 4},
 {'age': 255, 'amount': 2.55, 'curve': 4}]
```
    op hex (32)
    0000   0x5c 0x20 0x58 0x0f 0x04 0x54 0x55 0x04    \ X..TU.
    0008   0x58 0x87 0x04 0x0a 0xc3 0x04 0x0a 0xcd    X.......
    0010   0x04 0x08 0xd7 0x04 0x0a 0xe1 0x04 0x0a    ........
    0018   0xeb 0x04 0x3e 0xf5 0x04 0x66 0xff 0x04    ..>..f..
    decimal
             92   32   88   15    4   84   85    4
             88  135    4   10  195    4   10  205
              4    8  215    4   10  225    4   10
            235    4   62  245    4  102  255    4
    datetime (unknown)

    body (0)

#### RECORD 54 Bolus 2015-04-27T12:14:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'duration': 0, 'programmed': 3.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2015-04-27T12:14:21)
    0000   0x55 0x0e 0x8c 0x1b 0x0f                   U....
    body (0)

#### RECORD 55 BolusWizard 2015-04-27T12:31:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.0,
 'carb_input': 8,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
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
    datetime (2015-04-27T12:31:30)
    0000   0x5e 0x1f 0x0c 0x1b 0x0f                   ^....
    body (13)
    hex
    0000   0x08 0x50 0x08 0x28 0x5a 0x00 0x0a 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x0a 0x78                   ....x
    decimal
              8   80    8   40   90    0   10    0
              0    0    0   10  120

#### RECORD 56 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 2, 'amount': 0.05, 'curve': 4},
 {'age': 12, 'amount': 0.25, 'curve': 4},
 {'age': 22, 'amount': 3.45, 'curve': 4},
 {'age': 32, 'amount': 2.2, 'curve': 4},
 {'age': 102, 'amount': 2.1, 'curve': 4},
 {'age': 152, 'amount': 2.2, 'curve': 4},
 {'age': 212, 'amount': 0.25, 'curve': 4},
 {'age': 222, 'amount': 0.25, 'curve': 4},
 {'age': 232, 'amount': 0.2, 'curve': 4},
 {'age': 242, 'amount': 0.25, 'curve': 4},
 {'age': 252, 'amount': 0.25, 'curve': 4},
 {'age': 6, 'amount': 1.55, 'curve': 20},
 {'age': 16, 'amount': 2.55, 'curve': 20}]
```
    op hex (41)
    0000   0x5c 0x29 0x02 0x02 0x04 0x0a 0x0c 0x04    \)......
    0008   0x8a 0x16 0x04 0x58 0x20 0x04 0x54 0x66    ...X .Tf
    0010   0x04 0x58 0x98 0x04 0x0a 0xd4 0x04 0x0a    .X......
    0018   0xde 0x04 0x08 0xe8 0x04 0x0a 0xf2 0x04    ........
    0020   0x0a 0xfc 0x04 0x3e 0x06 0x14 0x66 0x10    ...>..f.
    0028   0x14                                       .
    decimal
             92   41    2    2    4   10   12    4
            138   22    4   88   32    4   84  102
              4   88  152    4   10  212    4   10
            222    4    8  232    4   10  242    4
             10  252    4   62    6   20  102   16
             20
    datetime (unknown)

    body (0)

#### RECORD 57 Bolus 2015-04-27T12:16:37 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8, 'duration': 120, 'programmed': 2.8, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x1c 0x1c 0x04                        ....
    decimal
              1   28   28    4
    datetime (2015-04-27T12:16:37)
    0000   0x65 0x10 0xac 0x1b 0x0f                   e....
    body (0)

#### RECORD 58 Bolus 2015-04-27T12:31:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'duration': 0, 'programmed': 1.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2015-04-27T12:31:30)
    0000   0x5e 0x1f 0x4c 0x1b 0x0f                   ^.L..
    body (0)

#### RECORD 59 SensorAlert 2015-04-27T13:34:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 246}
```
    op hex (3)
    0000   0x0b 0x65 0xf6                             .e.
    decimal
             11  101  246
    datetime (2015-04-27T13:34:12)
    0000   0x4c 0x22 0x2d 0xbb 0x0f                   L"-..
    body (0)

#### RECORD 60 BolusWizard 2015-04-27T13:34:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.8,
 'carb_input': 15,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
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
    datetime (2015-04-27T13:34:27)
    0000   0x5b 0x22 0x0d 0x1b 0x0f                   ["...
    body (13)
    hex
    0000   0x0f 0x50 0x08 0x28 0x5a 0x00 0x12 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x12 0x78                   ....x
    decimal
             15   80    8   40   90    0   18    0
              0    0    0   18  120

#### RECORD 61 UnabsorbedInsulinBolus unknown head[59], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 0.1, 'curve': 4},
 {'age': 15, 'amount': 0.25, 'curve': 4},
 {'age': 25, 'amount': 0.25, 'curve': 4},
 {'age': 35, 'amount': 0.2, 'curve': 4},
 {'age': 45, 'amount': 0.25, 'curve': 4},
 {'age': 55, 'amount': 0.25, 'curve': 4},
 {'age': 65, 'amount': 1.2, 'curve': 4},
 {'age': 75, 'amount': 0.25, 'curve': 4},
 {'age': 85, 'amount': 3.45, 'curve': 4},
 {'age': 95, 'amount': 2.2, 'curve': 4},
 {'age': 165, 'amount': 2.1, 'curve': 4},
 {'age': 215, 'amount': 2.2, 'curve': 4},
 {'age': 19, 'amount': 0.25, 'curve': 20},
 {'age': 29, 'amount': 0.25, 'curve': 20},
 {'age': 39, 'amount': 0.2, 'curve': 20},
 {'age': 49, 'amount': 0.25, 'curve': 20},
 {'age': 59, 'amount': 0.25, 'curve': 20},
 {'age': 69, 'amount': 1.55, 'curve': 20},
 {'age': 79, 'amount': 2.55, 'curve': 20}]
```
    op hex (59)
    0000   0x5c 0x3b 0x04 0x05 0x04 0x0a 0x0f 0x04    \;......
    0008   0x0a 0x19 0x04 0x08 0x23 0x04 0x0a 0x2d    ....#..-
    0010   0x04 0x0a 0x37 0x04 0x30 0x41 0x04 0x0a    ..7.0A..
    0018   0x4b 0x04 0x8a 0x55 0x04 0x58 0x5f 0x04    K..U.X_.
    0020   0x54 0xa5 0x04 0x58 0xd7 0x04 0x0a 0x13    T..X....
    0028   0x14 0x0a 0x1d 0x14 0x08 0x27 0x14 0x0a    .....'..
    0030   0x31 0x14 0x0a 0x3b 0x14 0x3e 0x45 0x14    1..;.>E.
    0038   0x66 0x4f 0x14                             fO.
    decimal
             92   59    4    5    4   10   15    4
             10   25    4    8   35    4   10   45
              4   10   55    4   48   65    4   10
             75    4  138   85    4   88   95    4
             84  165    4   88  215    4   10   19
             20   10   29   20    8   39   20   10
             49   20   10   59   20   62   69   20
            102   79   20
    datetime (unknown)

    body (0)

#### RECORD 62 Bolus 2015-04-27T13:34:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'duration': 0, 'programmed': 1.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2015-04-27T13:34:27)
    0000   0x5b 0x22 0x4d 0x1b 0x0f                   ["M..
    body (0)

#### RECORD 63 CalBGForPH 2015-04-27T15:38:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2015-04-27T15:38:40)
    0000   0x68 0x26 0x2f 0x7b 0x0f                   h&/{.
    body (0)

#### RECORD 64 BGReceived 2015-04-27T15:38:40 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 61, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2015-04-27T15:38:40)
    0000   0x68 0x26 0xaf 0x7b 0x0f                   h&.{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 65 SensorAlert 2015-04-27T15:53:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-27T15:53:44)
    0000   0x6c 0x35 0x2f 0xbb 0x0f                   l5/..
    body (0)

#### RECORD 66 SensorAlert 2015-04-27T15:53:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 106'}
```
    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2015-04-27T15:53:44)
    0000   0x6c 0x35 0x2f 0xbb 0x0f                   l5/..
    body (0)

#### RECORD 67 SensorAlert 2015-04-27T16:23:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-27T16:23:00)
    0000   0x40 0x17 0x30 0xbb 0x0f                   @.0..
    body (0)

#### RECORD 68 SensorAlert 2015-04-27T16:53:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-27T16:53:00)
    0000   0x40 0x35 0x30 0xbb 0x0f                   @50..
    body (0)

#### RECORD 69 CalBGForPH 2015-04-27T16:53:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2015-04-27T16:53:58)
    0000   0x7a 0x35 0x30 0x7b 0x0f                   z50{.
    body (0)

#### RECORD 70 BGReceived 2015-04-27T16:53:58 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 104, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2015-04-27T16:53:58)
    0000   0x7a 0x35 0x10 0x7b 0x0f                   z5.{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 71 SensorAlert 2015-04-27T17:57:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-04-27T17:57:38)
    0000   0x66 0x39 0x31 0xbb 0x0f                   f91..
    body (0)

#### RECORD 72 BolusWizard 2015-04-27T18:21:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.8,
 'carb_input': 41,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 6.8,
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
    datetime (2015-04-27T18:21:10)
    0000   0x4a 0x15 0x12 0x1b 0x0f                   J....
    body (13)
    hex
    0000   0x29 0x50 0x06 0x28 0x5a 0x00 0x44 0x00    )P.(Z.D.
    0008   0x00 0x00 0x00 0x44 0x78                   ...Dx
    decimal
             41   80    6   40   90    0   68    0
              0    0    0   68  120

`end ReadHistoryData-page-3.data: 73 records`
