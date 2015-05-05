## START ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x41 0x72                                  Ar
##### DEBUG DECIMAL
             65  114
#### RECORD 0 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 25, 'amount': 5.0, 'curve': 20},
 {'age': 125, 'amount': 0.05, 'curve': 20},
 {'age': 135, 'amount': 0.15, 'curve': 20},
 {'age': 145, 'amount': 0.15, 'curve': 20},
 {'age': 155, 'amount': 0.15, 'curve': 20},
 {'age': 165, 'amount': 0.15, 'curve': 20},
 {'age': 175, 'amount': 0.15, 'curve': 20},
 {'age': 185, 'amount': 0.15, 'curve': 20},
 {'age': 195, 'amount': 0.1, 'curve': 20},
 {'age': 205, 'amount': 0.15, 'curve': 20},
 {'age': 215, 'amount': 0.15, 'curve': 20}]
```
    op hex (35)
    0000   0x5c 0x23 0xc8 0x19 0x14 0x02 0x7d 0x14    \#....}.
    0008   0x06 0x87 0x14 0x06 0x91 0x14 0x06 0x9b    ........
    0010   0x14 0x06 0xa5 0x14 0x06 0xaf 0x14 0x06    ........
    0018   0xb9 0x14 0x04 0xc3 0x14 0x06 0xcd 0x14    ........
    0020   0x06 0xd7 0x14                             ...
    decimal
             92   35  200   25   20    2  125   20
              6  135   20    6  145   20    6  155
             20    6  165   20    6  175   20    6
            185   20    4  195   20    6  205   20
              6  215   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-04-17T21:40:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-17T21:40:22)
    0000   0x56 0x28 0x55 0x11 0x0f                   V(U..
    body (0)

#### RECORD 2 SensorAlert 2015-04-17T21:48:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-17T21:48:00)
    0000   0x40 0x30 0x35 0xb1 0x0f                   @05..
    body (0)

#### RECORD 3 SensorAlert 2015-04-17T22:31:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 273}
```
    op hex (3)
    0000   0x0b 0x65 0x11                             .e.
    decimal
             11  101   17
    datetime (2015-04-17T22:31:55)
    0000   0x77 0x1f 0x36 0xb1 0x8f                   w.6..
    body (0)

#### RECORD 4 SensorAlert 2015-04-17T22:48:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-17T22:48:00)
    0000   0x40 0x30 0x36 0xb1 0x0f                   @06..
    body (0)

#### RECORD 5 SensorAlert 2015-04-17T23:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-17T23:18:00)
    0000   0x40 0x12 0x37 0xb1 0x0f                   @.7..
    body (0)

#### RECORD 6 SensorAlert 2015-04-17T23:48:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-17T23:48:00)
    0000   0x40 0x30 0x37 0xb1 0x0f                   @07..
    body (0)

#### RECORD 7 MResultTotals 2015-04-18T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xda                   .....
    decimal
              7    0    0    5  218
    datetime (2015-04-18T00:00:00)
    0000   0x51 0x0f                                  Q.
    body (0)

#### RECORD 8 Model522ResultTotals 2015-04-18T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-18T00:00:00)
    0000   0x51 0x0f                                  Q.
    body (41)
    hex
    0000   0x05 0x15 0x1b 0x1b 0x1b 0x01 0x00 0x00    ........
    0008   0x05 0xda 0x03 0x1a 0x35 0x02 0xc0 0x2f    ....5../
    0010   0x00 0x55 0x02 0xc0 0x2f 0x01 0xa8 0x3c    .U../..<
    0018   0x01 0x18 0x28 0x00 0x00 0x00 0x04 0x02    ..(.....
    0020   0x02 0x00 0x00 0x50 0x87 0x3a 0x1d 0x0d    ...P.:..
    0028   0x01                                       .
    decimal
              5   21   27   27   27    1    0    0
              5  218    3   26   53    2  192   47
              0   85    2  192   47    1  168   60
              1   24   40    0    0    0    4    2
              2    0    0   80  135   58   29   13
              1

#### RECORD 9 SensorAlert 2015-04-18T00:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-18T00:18:00)
    0000   0x40 0x12 0x20 0xb2 0x0f                   @. ..
    body (0)

#### RECORD 10 CalBGForPH 2015-04-18T00:18:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 225}
```
    op hex (2)
    0000   0x0a 0xe1                                  ..
    decimal
             10  225
    datetime (2015-04-18T00:18:44)
    0000   0x6c 0x12 0x20 0x72 0x0f                   l. r.
    body (0)

#### RECORD 11 BGReceived 2015-04-18T00:18:44 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1c                                  ?.
    decimal
             63   28
    datetime (2015-04-18T00:18:44)
    0000   0x6c 0x12 0x20 0x72 0x0f                   l. r.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 12 BolusWizard 2015-04-18T00:18:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 26,
 '_byte[7]': 0,
 'bg': 225,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 10,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xe1                                  [.
    decimal
             91  225
    datetime (2015-04-18T00:18:58)
    0000   0x7a 0x12 0x00 0x12 0x0f                   z....
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x1a 0x00 0x00    .P.(Z...
    0008   0x00 0x08 0x00 0x12 0x78                   ....x
    decimal
              0   80   10   40   90   26    0    0
              0    8    0   18  120

#### RECORD 13 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 159, 'amount': 3.0, 'curve': 4},
 {'age': 183, 'amount': 5.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x78 0x9f 0x04 0xc8 0xb7 0x14    \.x.....
    decimal
             92    8  120  159    4  200  183   20
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2015-04-18T00:18:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'duration': 0, 'programmed': 1.8, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2015-04-18T00:18:58)
    0000   0x7a 0x12 0x40 0x12 0x0f                   z.@..
    body (0)

#### RECORD 15 SensorAlert 2015-04-18T00:31:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 230}
```
    op hex (3)
    0000   0x0b 0x65 0xe6                             .e.
    decimal
             11  101  230
    datetime (2015-04-18T00:31:55)
    0000   0x77 0x1f 0x20 0xb2 0x0f                   w. ..
    body (0)

#### RECORD 16 SensorAlert 2015-04-18T02:03:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 258}
```
    op hex (3)
    0000   0x0b 0x65 0x02                             .e.
    decimal
             11  101    2
    datetime (2015-04-18T02:03:12)
    0000   0x4c 0x03 0x22 0xb2 0x8f                   L."..
    body (0)

#### RECORD 17 SensorAlert 2015-04-18T03:32:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 270}
```
    op hex (3)
    0000   0x0b 0x65 0x0e                             .e.
    decimal
             11  101   14
    datetime (2015-04-18T03:32:53)
    0000   0x75 0x20 0x23 0xb2 0x8f                   u #..
    body (0)

#### RECORD 18 BolusWizard 2015-04-18T04:21:04 head[2], body[13] op[0x5b]
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
    datetime (2015-04-18T04:21:04)
    0000   0x44 0x15 0x04 0x12 0x0f                   D....
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80   10   40   90    0    0    0
              0    0    0    0  120

#### RECORD 19 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 242, 'amount': 1.75, 'curve': 4},
 {'age': 252, 'amount': 0.05, 'curve': 4},
 {'age': 146, 'amount': 3.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x46 0xf2 0x04 0x02 0xfc 0x04    \.F.....
    0008   0x78 0x92 0x14                             x..
    decimal
             92   11   70  242    4    2  252    4
            120  146   20
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2015-04-18T04:21:04 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'duration': 0, 'programmed': 1.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0e 0x0e 0x00                        ....
    decimal
              1   14   14    0
    datetime (2015-04-18T04:21:04)
    0000   0x44 0x15 0x44 0x12 0x0f                   D.D..
    body (0)

#### RECORD 21 SensorAlert 2015-04-18T05:02:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 250}
```
    op hex (3)
    0000   0x0b 0x65 0xfa                             .e.
    decimal
             11  101  250
    datetime (2015-04-18T05:02:44)
    0000   0x6c 0x02 0x25 0xb2 0x0f                   l.%..
    body (0)

#### RECORD 22 SensorAlert 2015-04-18T06:31:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 197}
```
    op hex (3)
    0000   0x0b 0x65 0xc5                             .e.
    decimal
             11  101  197
    datetime (2015-04-18T06:31:55)
    0000   0x77 0x1f 0x26 0xb2 0x0f                   w.&..
    body (0)

#### RECORD 23 LowReservoir 2015-04-18T06:46:40 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-04-18T06:46:40)
    0000   0x68 0x2e 0x06 0x12 0x0f                   h....
    body (0)

#### RECORD 24 CalBGForPH 2015-04-18T09:09:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2015-04-18T09:09:12)
    0000   0x4c 0x09 0x29 0x72 0x0f                   L.)r.
    body (0)

#### RECORD 25 BGReceived 2015-04-18T09:09:12 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2015-04-18T09:09:12)
    0000   0x4c 0x09 0xe9 0x72 0x0f                   L..r.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 26 BolusWizard 2015-04-18T09:09:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 5,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.5,
 'carb_input': 20,
 'carb_ratio': 10,
 'correction_estimate': 0.5,
 'food_estimate': 2.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2015-04-18T09:09:23)
    0000   0x57 0x09 0x09 0x12 0x0f                   W....
    body (13)
    hex
    0000   0x14 0x50 0x0a 0x28 0x5a 0x05 0x14 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x19 0x78                   ....x
    decimal
             20   80   10   40   90    5   20    0
              0    0    0   25  120

#### RECORD 27 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 1.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x38 0x22 0x14                   \.8".
    decimal
             92    5   56   34   20
    datetime (unknown)

    body (0)

#### RECORD 28 Bolus 2015-04-18T09:09:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'duration': 0, 'programmed': 2.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2015-04-18T09:09:23)
    0000   0x57 0x09 0x49 0x12 0x0f                   W.I..
    body (0)

#### RECORD 29 SensorAlert 2015-04-18T11:17:17 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-18T11:17:17)
    0000   0x51 0x11 0x2b 0xb2 0x0f                   Q.+..
    body (0)

#### RECORD 30 SensorAlert 2015-04-18T12:48:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 205}
```
    op hex (3)
    0000   0x0b 0x65 0xcd                             .e.
    decimal
             11  101  205
    datetime (2015-04-18T12:48:05)
    0000   0x45 0x30 0x2c 0xb2 0x0f                   E0,..
    body (0)

#### RECORD 31 BolusWizard 2015-04-18T13:30:21 head[2], body[13] op[0x5b]
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
    datetime (2015-04-18T13:30:21)
    0000   0x55 0x1e 0x0d 0x12 0x0f                   U....
    body (13)
    hex
    0000   0x32 0x50 0x08 0x28 0x5a 0x00 0x3e 0x00    2P.(Z.>.
    0008   0x00 0x00 0x00 0x3e 0x78                   ...>x
    decimal
             50   80    8   40   90    0   62    0
              0    0    0   62  120

#### RECORD 32 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 2.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x64 0x05 0x14                   \.d..
    decimal
             92    5  100    5   20
    datetime (unknown)

    body (0)

#### RECORD 33 LowReservoir 2015-04-18T13:31:37 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-04-18T13:31:37)
    0000   0x65 0x1f 0x0d 0x12 0x0f                   e....
    body (0)

#### RECORD 34 Bolus 2015-04-18T13:30:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2, 'duration': 0, 'programmed': 6.2, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x3e 0x3e 0x00                        .>>.
    decimal
              1   62   62    0
    datetime (2015-04-18T13:30:21)
    0000   0x55 0x1e 0x4d 0x12 0x0f                   U.M..
    body (0)

#### RECORD 35 SensorAlert 2015-04-18T14:16:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 240}
```
    op hex (3)
    0000   0x0b 0x65 0xf0                             .e.
    decimal
             11  101  240
    datetime (2015-04-18T14:16:36)
    0000   0x64 0x10 0x2e 0xb2 0x0f                   d....
    body (0)

#### RECORD 36 SensorAlert 2015-04-18T16:31:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-04-18T16:31:55)
    0000   0x77 0x1f 0x30 0xb2 0x0f                   w.0..
    body (0)

#### RECORD 37 BolusWizard 2015-04-18T16:37:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.5,
 'carb_input': 28,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 3.5,
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
    datetime (2015-04-18T16:37:22)
    0000   0x56 0x25 0x10 0x12 0x0f                   V%...
    body (13)
    hex
    0000   0x1c 0x50 0x08 0x28 0x5a 0x00 0x23 0x00    .P.(Z.#.
    0008   0x00 0x00 0x00 0x23 0x78                   ...#x
    decimal
             28   80    8   40   90    0   35    0
              0    0    0   35  120

#### RECORD 38 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 188, 'amount': 6.2, 'curve': 4},
 {'age': 192, 'amount': 2.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xf8 0xbc 0x04 0x64 0xc0 0x14    \....d..
    decimal
             92    8  248  188    4  100  192   20
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2015-04-18T16:37:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'duration': 0, 'programmed': 3.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2015-04-18T16:37:22)
    0000   0x56 0x25 0x50 0x12 0x0f                   V%P..
    body (0)

#### RECORD 40 SensorAlert 2015-04-18T20:09:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-18T20:09:00)
    0000   0x40 0x09 0x34 0xb2 0x0f                   @.4..
    body (0)

#### RECORD 41 SensorAlert 2015-04-18T20:43:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-04-18T20:43:12)
    0000   0x4c 0x2b 0x34 0xb2 0x0f                   L+4..
    body (0)

#### RECORD 42 SensorAlert 2015-04-18T21:09:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-18T21:09:00)
    0000   0x40 0x09 0x35 0xb2 0x0f                   @.5..
    body (0)

#### RECORD 43 SensorAlert 2015-04-18T21:39:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-18T21:39:00)
    0000   0x40 0x27 0x35 0xb2 0x0f                   @'5..
    body (0)

#### RECORD 44 BolusWizard 2015-04-18T21:39:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.5,
 'carb_input': 45,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 7.5,
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
    datetime (2015-04-18T21:39:54)
    0000   0x76 0x27 0x15 0x12 0x0f                   v'...
    body (13)
    hex
    0000   0x2d 0x50 0x06 0x28 0x5a 0x00 0x4b 0x00    -P.(Z.K.
    0008   0x00 0x00 0x00 0x4b 0x78                   ...Kx
    decimal
             45   80    6   40   90    0   75    0
              0    0    0   75  120

#### RECORD 45 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 1.1, 'curve': 20},
 {'age': 54, 'amount': 2.4, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x2c 0x2c 0x14 0x60 0x36 0x14    \.,,.`6.
    decimal
             92    8   44   44   20   96   54   20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2015-04-18T21:39:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'duration': 0, 'programmed': 3.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2015-04-18T21:39:54)
    0000   0x76 0x27 0x95 0x12 0x0f                   v'...
    body (0)

#### RECORD 47 SensorAlert 2015-04-18T22:09:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-18T22:09:00)
    0000   0x40 0x09 0x36 0xb2 0x0f                   @.6..
    body (0)

#### RECORD 48 CalBGForPH 2015-04-18T22:09:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2015-04-18T22:09:46)
    0000   0x6e 0x09 0x36 0x72 0x0f                   n.6r.
    body (0)

#### RECORD 49 BGReceived 2015-04-18T22:09:46 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2015-04-18T22:09:46)
    0000   0x6e 0x09 0x56 0x72 0x0f                   n.Vr.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 50 SensorAlert 2015-04-18T22:22:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 198}
```
    op hex (3)
    0000   0x0b 0x65 0xc6                             .e.
    decimal
             11  101  198
    datetime (2015-04-18T22:22:44)
    0000   0x6c 0x16 0x36 0xb2 0x0f                   l.6..
    body (0)

#### RECORD 51 Bolus 2015-04-18T21:42:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'duration': 90, 'programmed': 3.8, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x26 0x1f 0x03                        .&..
    decimal
              1   38   31    3
    datetime (2015-04-18T21:42:22)
    0000   0x56 0x2a 0xb5 0x12 0x0f                   V*...
    body (0)

#### RECORD 52 NoDelivery 2015-04-18T22:56:23 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0b 0xff                        ....
    decimal
              6    4   11  255
    datetime (2015-04-18T22:56:23)
    0000   0x57 0x38 0x56 0x52 0x0f                   W8VR.
    body (0)

#### RECORD 53 ClearAlarm 2015-04-18T22:56:32 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-04-18T22:56:32)
    0000   0x60 0x38 0x16 0x12 0x0f                   `8...
    body (0)

#### RECORD 54 Rewind 2015-04-18T22:56:58 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-04-18T22:56:58)
    0000   0x7a 0x38 0x16 0x12 0x0f                   z8...
    body (0)

#### RECORD 55 Prime 2015-04-18T22:57:48 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 5.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x39                   ....9
    decimal
              3    0    0    0   57
    datetime (2015-04-18T22:57:48)
    0000   0x70 0x39 0x36 0x12 0x0f                   p96..
    body (0)

#### RECORD 56 Prime 2015-04-18T22:58:16 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2015-04-18T22:58:16)
    0000   0x50 0x3a 0x16 0x12 0x0f                   P:...
    body (0)

#### RECORD 57 SensorAlert 2015-04-18T23:11:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 79}
```
    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-04-18T23:11:55)
    0000   0x77 0x0b 0x37 0xb2 0x0f                   w.7..
    body (0)

#### RECORD 58 SensorAlert 2015-04-18T23:32:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 66}
```
    op hex (3)
    0000   0x0b 0x66 0x42                             .fB
    decimal
             11  102   66
    datetime (2015-04-18T23:32:53)
    0000   0x75 0x20 0x37 0xb2 0x0f                   u 7..
    body (0)

#### RECORD 59 SensorAlert 2015-04-18T23:51:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 59}
```
    op hex (3)
    0000   0x0b 0x66 0x3b                             .f;
    decimal
             11  102   59
    datetime (2015-04-18T23:51:55)
    0000   0x77 0x33 0x37 0xb2 0x0f                   w37..
    body (0)

#### RECORD 60 MResultTotals 2015-04-19T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0x9e                   .....
    decimal
              7    0    0    6  158
    datetime (2015-04-19T00:00:00)
    0000   0x52 0x0f                                  R.
    body (0)

#### RECORD 61 Model522ResultTotals 2015-04-19T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-19T00:00:00)
    0000   0x52 0x0f                                  R.
    body (41)
    hex
    0000   0x05 0x00 0xbb 0x8f 0xe1 0x03 0x00 0x00    ........
    0008   0x06 0x9e 0x03 0x26 0x30 0x03 0x78 0x34    ...&0.x4
    0010   0x00 0x8f 0x03 0x78 0x34 0x02 0xe4 0x53    ...x4..S
    0018   0x00 0x94 0x11 0x00 0x00 0x00 0x06 0x03    ........
    0020   0x02 0x01 0x00 0x50 0xbe 0x3a 0x0f 0x0c    ...P.:..
    0028   0x03                                       .
    decimal
              5    0  187  143  225    3    0    0
              6  158    3   38   48    3  120   52
              0  143    3  120   52    2  228   83
              0  148   17    0    0    0    6    3
              2    1    0   80  190   58   15   12
              3

#### RECORD 62 SensorAlert 2015-04-19T00:12:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 56}
```
    op hex (3)
    0000   0x0b 0x66 0x38                             .f8
    decimal
             11  102   56
    datetime (2015-04-19T00:12:53)
    0000   0x75 0x0c 0x20 0xb3 0x0f                   u. ..
    body (0)

#### RECORD 63 SensorAlert 2015-04-19T00:31:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 55}
```
    op hex (3)
    0000   0x0b 0x66 0x37                             .f7
    decimal
             11  102   55
    datetime (2015-04-19T00:31:55)
    0000   0x77 0x1f 0x20 0xb3 0x0f                   w. ..
    body (0)

#### RECORD 64 SensorAlert 2015-04-19T00:52:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 59}
```
    op hex (3)
    0000   0x0b 0x66 0x3b                             .f;
    decimal
             11  102   59
    datetime (2015-04-19T00:52:53)
    0000   0x75 0x34 0x20 0xb3 0x0f                   u4 ..
    body (0)

#### RECORD 65 SensorAlert 2015-04-19T01:11:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 66}
```
    op hex (3)
    0000   0x0b 0x66 0x42                             .fB
    decimal
             11  102   66
    datetime (2015-04-19T01:11:55)
    0000   0x77 0x0b 0x21 0xb3 0x0f                   w.!..
    body (0)

#### RECORD 66 SensorAlert 2015-04-19T01:32:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 72}
```
    op hex (3)
    0000   0x0b 0x66 0x48                             .fH
    decimal
             11  102   72
    datetime (2015-04-19T01:32:53)
    0000   0x75 0x20 0x21 0xb3 0x0f                   u !..
    body (0)

#### RECORD 67 SensorAlert 2015-04-19T01:51:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 73}
```
    op hex (3)
    0000   0x0b 0x66 0x49                             .fI
    decimal
             11  102   73
    datetime (2015-04-19T01:51:55)
    0000   0x77 0x33 0x21 0xb3 0x0f                   w3!..
    body (0)

#### RECORD 68 SensorAlert 2015-04-19T02:12:53 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 79}
```
    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-04-19T02:12:53)
    0000   0x75 0x0c 0x22 0xb3 0x0f                   u."..
    body (0)

#### RECORD 69 SensorAlert 2015-04-19T02:48:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-19T02:48:05)
    0000   0x45 0x30 0x22 0xb3 0x0f                   E0"..
    body (0)

#### RECORD 70 SensorAlert 2015-04-19T03:28:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-19T03:28:05)
    0000   0x45 0x1c 0x23 0xb3 0x0f                   E.#..
    body (0)

#### RECORD 71 SensorAlert 2015-04-19T03:46:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-04-19T03:46:38)
    0000   0x66 0x2e 0x23 0xb3 0x0f                   f.#..
    body (0)

#### RECORD 72 SensorAlert 2015-04-19T04:08:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-04-19T04:08:05)
    0000   0x45 0x08 0x24 0xb3 0x0f                   E.$..
    body (0)

#### RECORD 73 SensorAlert 2015-04-19T04:26:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-04-19T04:26:55)
    0000   0x77 0x1a 0x24 0xb3 0x0f                   w.$..
    body (0)

#### RECORD 74 SensorAlert 2015-04-19T04:48:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-04-19T04:48:05)
    0000   0x45 0x30 0x24 0xb3 0x0f                   E0$..
    body (0)

#### RECORD 75 SensorAlert 2015-04-19T05:06:38 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-04-19T05:06:38)
    0000   0x66 0x06 0x25 0xb3 0x0f                   f.%..
    body (0)

#### RECORD 76 SensorAlert 2015-04-19T05:28:05 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 76}
```
    op hex (3)
    0000   0x0b 0x66 0x4c                             .fL
    decimal
             11  102   76
    datetime (2015-04-19T05:28:05)
    0000   0x45 0x1c 0x25 0xb3 0x0f                   E.%..
    body (0)

#### RECORD 77 SensorAlert 2015-04-19T09:09:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-19T09:09:00)
    0000   0x40 0x09 0x29 0xb3 0x0f                   @.)..
    body (0)

#### RECORD 78 SensorAlert 2015-04-19T10:09:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-19T10:09:00)
    0000   0x40 0x09 0x2a 0xb3 0x0f                   @.*..
    body (0)

#### RECORD 79 SensorAlert 2015-04-19T10:39:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-19T10:39:00)
    0000   0x40 0x27 0x2a 0xb3 0x0f                   @'*..
    body (0)

#### RECORD 80 CalBGForPH 2015-04-19T10:40:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 138}
```
    op hex (2)
    0000   0x0a 0x8a                                  ..
    decimal
             10  138
    datetime (2015-04-19T10:40:34)
    0000   0x62 0x28 0x2a 0x73 0x0f                   b(*s.
    body (0)

#### RECORD 81 BGReceived 2015-04-19T10:40:34 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2015-04-19T10:40:34)
    0000   0x62 0x28 0x4a 0x73 0x0f                   b(Js.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 82 BolusWizard 2015-04-19T10:41:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 138,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.4,
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
    0000   0x5b 0x8a                                  [.
    decimal
             91  138
    datetime (2015-04-19T10:41:05)
    0000   0x45 0x29 0x0a 0x13 0x0f                   E)...
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x04 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x04 0x78                   ....x
    decimal
              0   80   10   40   90    4    0    0
              0    0    0    4  120

#### RECORD 83 Bolus 2015-04-19T10:41:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4, 'duration': 0, 'programmed': 0.4, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x04 0x04 0x00                        ....
    decimal
              1    4    4    0
    datetime (2015-04-19T10:41:05)
    0000   0x45 0x29 0x8a 0x13 0x0f                   E)...
    body (0)

#### RECORD 84 SensorAlert 2015-04-19T12:43:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-04-19T12:43:12)
    0000   0x4c 0x2b 0x2c 0xb3 0x0f                   L+,..
    body (0)

#### RECORD 85 SensorAlert 2015-04-19T13:02:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 68}
```
    op hex (3)
    0000   0x0b 0x66 0x44                             .fD
    decimal
             11  102   68
    datetime (2015-04-19T13:02:44)
    0000   0x6c 0x02 0x2d 0xb3 0x0f                   l.-..
    body (0)

#### RECORD 86 SensorAlert 2015-04-19T13:23:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 66}
```
    op hex (3)
    0000   0x0b 0x66 0x42                             .fB
    decimal
             11  102   66
    datetime (2015-04-19T13:23:12)
    0000   0x4c 0x17 0x2d 0xb3 0x0f                   L.-..
    body (0)

#### RECORD 87 SensorAlert 2015-04-19T13:42:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-04-19T13:42:44)
    0000   0x6c 0x2a 0x2d 0xb3 0x0f                   l*-..
    body (0)

#### RECORD 88 SensorAlert 2015-04-19T14:03:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-19T14:03:12)
    0000   0x4c 0x03 0x2e 0xb3 0x0f                   L....
    body (0)

#### RECORD 89 PumpSuspend 2015-04-19T14:53:09 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-19T14:53:09)
    0000   0x49 0x35 0x0e 0x13 0x0f                   I5...
    body (0)

#### RECORD 90 PumpResume 2015-04-19T15:15:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-19T15:15:55)
    0000   0x77 0x0f 0x0f 0x13 0x0f                   w....
    body (0)

#### RECORD 91 BolusWizard 2015-04-19T15:27:09 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.7,
 'carb_input': 54,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 6.7,
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
    datetime (2015-04-19T15:27:09)
    0000   0x49 0x1b 0x0f 0x13 0x0f                   I....
    body (13)
    hex
    0000   0x36 0x50 0x08 0x28 0x5a 0x00 0x43 0x00    6P.(Z.C.
    0008   0x00 0x00 0x00 0x43 0x78                   ...Cx
    decimal
             54   80    8   40   90    0   67    0
              0    0    0   67  120

#### RECORD 92 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 0.4, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x10 0x20 0x14                   \.. .
    decimal
             92    5   16   32   20
    datetime (unknown)

    body (0)

#### RECORD 93 Bolus 2015-04-19T15:27:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.7, 'duration': 0, 'programmed': 4.7, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2f 0x2f 0x00                        .//.
    decimal
              1   47   47    0
    datetime (2015-04-19T15:27:09)
    0000   0x49 0x1b 0x8f 0x13 0x0f                   I....
    body (0)

#### RECORD 94 SensorAlert 2015-04-19T15:36:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-04-19T15:36:36)
    0000   0x64 0x24 0x2f 0xb3 0x0f                   d$/..
    body (0)

#### RECORD 95 BolusWizard 2015-04-19T16:07:05 head[2], body[13] op[0x5b]
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
    datetime (2015-04-19T16:07:05)
    0000   0x45 0x07 0x10 0x13 0x0f                   E....
    body (13)
    hex
    0000   0x14 0x50 0x08 0x28 0x5a 0x00 0x19 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x19 0x78                   ....x
    decimal
             20   80    8   40   90    0   25    0
              0    0    0   25  120

#### RECORD 96 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.3, 'curve': 4},
 {'age': 18, 'amount': 0.35, 'curve': 4},
 {'age': 28, 'amount': 0.3, 'curve': 4},
 {'age': 38, 'amount': 2.25, 'curve': 4},
 {'age': 48, 'amount': 2.75, 'curve': 4},
 {'age': 72, 'amount': 0.4, 'curve': 20}]
```
    op hex (20)
    0000   0x5c 0x14 0x0c 0x08 0x04 0x0e 0x12 0x04    \.......
    0008   0x0c 0x1c 0x04 0x5a 0x26 0x04 0x6e 0x30    ...Z&.n0
    0010   0x04 0x10 0x48 0x14                        ..H.
    decimal
             92   20   12    8    4   14   18    4
             12   28    4   90   38    4  110   48
              4   16   72   20
    datetime (unknown)

    body (0)

#### RECORD 97 Bolus 2015-04-19T15:30:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 60, 'programmed': 2.0, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x02                        ....
    decimal
              1   20   20    2
    datetime (2015-04-19T15:30:18)
    0000   0x52 0x1e 0xaf 0x13 0x0f                   R....
    body (0)

#### RECORD 98 Bolus 2015-04-19T16:07:06 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5, 'duration': 0, 'programmed': 2.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x19 0x19 0x00                        ....
    decimal
              1   25   25    0
    datetime (2015-04-19T16:07:06)
    0000   0x46 0x07 0x50 0x13 0x0f                   F.P..
    body (0)

`end ReadHistoryData-page-7.data: 99 records`
