## START ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x27 0x79                                  'y
##### DEBUG DECIMAL
             39  121
#### RECORD 0 Bolus 2015-04-24T12:20:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'duration': 0, 'programmed': 4.3, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2015-04-24T12:20:24)
    0000   0x58 0x14 0x4c 0x18 0x0f                   X.L..
    body (0)

#### RECORD 1 BolusWizard 2015-04-24T14:59:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.6,
 'carb_input': 45,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 5.6,
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
    datetime (2015-04-24T14:59:49)
    0000   0x71 0x3b 0x0e 0x18 0x0f                   q;...
    body (13)
    hex
    0000   0x2d 0x50 0x08 0x28 0x5a 0x00 0x38 0x00    -P.(Z.8.
    0008   0x00 0x00 0x00 0x38 0x78                   ...8x
    decimal
             45   80    8   40   90    0   56    0
              0    0    0   56  120

#### RECORD 2 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 160, 'amount': 4.3, 'curve': 4},
 {'age': 84, 'amount': 5.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xac 0xa0 0x04 0xc8 0x54 0x14    \.....T.
    decimal
             92    8  172  160    4  200   84   20
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2015-04-24T14:59:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-24T14:59:49)
    0000   0x71 0x3b 0x8e 0x18 0x0f                   q;...
    body (0)

#### RECORD 4 Bolus 2015-04-24T15:01:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'duration': 60, 'programmed': 2.6, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x02                        ....
    decimal
              1   26   26    2
    datetime (2015-04-24T15:01:49)
    0000   0x71 0x01 0xaf 0x18 0x0f                   q....
    body (0)

#### RECORD 5 NoDelivery 2005-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x15 0x05 0x0d                        ....
    decimal
              6   21    5   13
    datetime (2005-01-01T00:00:00)
    0000   0x00 0x40 0x60 0x01 0x05                   .@`..
    body (0)

#### RECORD 6 NoDelivery 2005-01-01T00:00:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x11 0x04 0xe9                        ....
    decimal
              6   17    4  233
    datetime (2005-01-01T00:00:00)
    0000   0x00 0x40 0x40 0xa1 0x05                   .@@..
    body (0)

#### RECORD 7 ClearAlarm 2005-01-01T00:00:24 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x15                                  ..
    decimal
             12   21
    datetime (2005-01-01T00:00:24)
    0000   0x18 0x40 0x00 0x01 0x05                   .@...
    body (0)

#### RECORD 8 ChangeTimeDisplay 2005-01-01T00:00:27 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2005-01-01T00:00:27)
    0000   0x1b 0x40 0x00 0x01 0x05                   .@...
    body (0)

#### RECORD 9 ChangeTime 2005-01-01T00:01:02 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2005-01-01T00:01:02)
    0000   0x02 0x41 0x00 0x01 0x05                   .A...
    body (0)

#### RECORD 10 NewTimeSet 2015-04-24T17:40:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2015-04-24T17:40:00)
    0000   0x40 0x28 0x11 0x18 0x0f                   @(...
    body (0)

#### RECORD 11 SensorAlert 2015-04-24T17:40:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 113, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x71 0x00                             .q.
    decimal
             11  113    0
    datetime (2015-04-24T17:40:00)
    0000   0x40 0x28 0x31 0xb8 0x0f                   @(1..
    body (0)

#### RECORD 12 MResultTotals 2005-01-02T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2005-01-02T00:00:00)
    0000   0x01 0x85                                  ..
    body (0)

#### RECORD 13 Model522ResultTotals 2005-01-02T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2005-01-02T00:00:00)
    0000   0x01 0x85                                  ..
    body (41)
    hex
    0000   0x05 0x0c 0x00 0xe8 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   12    0  232    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0   12    0  232    0    0
              0

#### RECORD 14 Rewind 2015-04-24T17:40:04 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-04-24T17:40:04)
    0000   0x44 0x28 0x11 0x18 0x0f                   D(...
    body (0)

#### RECORD 15 Prime 2015-04-24T17:40:21 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x00                   .....
    decimal
              3    0    0    0    0
    datetime (2015-04-24T17:40:21)
    0000   0x55 0x28 0x31 0x18 0x0f                   U(1..
    body (0)

#### RECORD 16 SensorAlert 2015-04-24T17:41:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-24T17:41:06)
    0000   0x46 0x29 0x31 0xb8 0x0f                   F)1..
    body (0)

#### RECORD 17 SensorAlert 2015-04-24T18:11:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-24T18:11:00)
    0000   0x40 0x0b 0x32 0xb8 0x0f                   @.2..
    body (0)

#### RECORD 18 ChangeAlarmNotifyMode 2015-04-24T18:12:29 head[2], body[0] op[0x63]

    op hex (2)
    0000   0x63 0x04                                  c.
    decimal
             99    4
    datetime (2015-04-24T18:12:29)
    0000   0x5d 0x0c 0x12 0x18 0x0f                   ]....
    body (0)

#### RECORD 19 CalBGForPH 2015-04-24T18:33:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2015-04-24T18:33:40)
    0000   0x68 0x21 0x32 0x78 0x0f                   h!2x.
    body (0)

#### RECORD 20 BGReceived 2015-04-24T18:33:40 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2015-04-24T18:33:40)
    0000   0x68 0x21 0x72 0x78 0x0f                   h!rx.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 21 BolusWizard 2015-04-24T20:45:30 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 9.6,
 'carb_input': 58,
 'carb_ratio': 6,
 'correction_estimate': 0.0,
 'food_estimate': 9.6,
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
    datetime (2015-04-24T20:45:30)
    0000   0x5e 0x2d 0x14 0x18 0x0f                   ^-...
    body (13)
    hex
    0000   0x3a 0x50 0x06 0x28 0x5a 0x00 0x60 0x00    :P.(Z.`.
    0008   0x00 0x00 0x00 0x60 0x78                   ...`x
    decimal
             58   80    6   40   90    0   96    0
              0    0    0   96  120

#### RECORD 22 Bolus 2015-04-24T20:45:30 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'duration': 0, 'programmed': 2.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2015-04-24T20:45:30)
    0000   0x5e 0x2d 0x94 0x18 0x0f                   ^-...
    body (0)

#### RECORD 23 PumpSuspend 2015-04-24T21:15:08 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-24T21:15:08)
    0000   0x48 0x0f 0x15 0x18 0x0f                   H....
    body (0)

#### RECORD 24 Bolus 2015-04-24T20:46:48 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4, 'duration': 120, 'programmed': 6.0, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x3c 0x0e 0x04                        .<..
    decimal
              1   60   14    4
    datetime (2015-04-24T20:46:48)
    0000   0x70 0x2e 0xb4 0x18 0x0f                   p....
    body (0)

#### RECORD 25 PumpResume 2015-04-24T21:40:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-24T21:40:35)
    0000   0x63 0x28 0x15 0x18 0x0f                   c(...
    body (0)

#### RECORD 26 BolusWizard 2015-04-24T21:41:02 head[2], body[13] op[0x5b]
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
    datetime (2015-04-24T21:41:02)
    0000   0x42 0x29 0x15 0x18 0x0f                   B)...
    body (13)
    hex
    0000   0x1e 0x50 0x06 0x28 0x5a 0x00 0x32 0x00    .P.(Z.2.
    0008   0x00 0x00 0x00 0x32 0x78                   ...2x
    decimal
             30   80    6   40   90    0   50    0
              0    0    0   50  120

#### RECORD 27 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 32, 'amount': 0.3, 'curve': 4},
 {'age': 42, 'amount': 0.5, 'curve': 4},
 {'age': 52, 'amount': 0.5, 'curve': 4},
 {'age': 62, 'amount': 2.1, 'curve': 4}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0c 0x20 0x04 0x14 0x2a 0x04    \.. ..*.
    0008   0x14 0x34 0x04 0x54 0x3e 0x04              .4.T>.
    decimal
             92   14   12   32    4   20   42    4
             20   52    4   84   62    4
    datetime (unknown)

    body (0)

#### RECORD 28 SensorAlert 2015-04-24T23:33:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-24T23:33:00)
    0000   0x40 0x21 0x37 0xb8 0x0f                   @!7..
    body (0)

#### RECORD 29 MResultTotals 2015-04-25T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x01 0xaa                   .....
    decimal
              7    0    0    1  170
    datetime (2015-04-25T00:00:00)
    0000   0x58 0x0f                                  X.
    body (0)

#### RECORD 30 Model522ResultTotals 2015-04-25T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-25T00:00:00)
    0000   0x58 0x0f                                  X.
    body (41)
    hex
    0000   0x05 0x00 0x63 0x63 0x63 0x01 0x00 0x00    ..ccc...
    0008   0x01 0xaa 0x00 0xc6 0x2e 0x00 0xe4 0x36    .......6
    0010   0x00 0x58 0x00 0xe4 0x36 0x00 0xe4 0x64    .X..6..d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x00 0x75 0x59 0xa1 0x3f    ....uY.?
    0028   0x01                                       .
    decimal
              5    0   99   99   99    1    0    0
              1  170    0  198   46    0  228   54
              0   88    0  228   54    0  228  100
              0    0    0    0    0    0    2    2
              0    0    0    0  117   89  161   63
              1

#### RECORD 31 SensorAlert 2015-04-25T00:33:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-25T00:33:00)
    0000   0x40 0x21 0x20 0xb9 0x0f                   @! ..
    body (0)

#### RECORD 32 SensorAlert 2015-04-25T01:03:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-25T01:03:00)
    0000   0x40 0x03 0x21 0xb9 0x0f                   @.!..
    body (0)

#### RECORD 33 CalBGForPH 2015-04-25T01:14:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 76}
```
    op hex (2)
    0000   0x0a 0x4c                                  .L
    decimal
             10   76
    datetime (2015-04-25T01:14:48)
    0000   0x70 0x0e 0x21 0x79 0x0f                   p.!y.
    body (0)

#### RECORD 34 BGReceived 2015-04-25T01:14:48 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2015-04-25T01:14:48)
    0000   0x70 0x0e 0x81 0x79 0x0f                   p..y.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 35 SensorAlert 2015-04-25T01:26:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-04-25T01:26:33)
    0000   0x61 0x1a 0x21 0xb9 0x0f                   a.!..
    body (0)

#### RECORD 36 Bolus 2015-04-24T21:41:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'duration': 240, 'programmed': 4.0, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x08                        .((.
    decimal
              1   40   40    8
    datetime (2015-04-24T21:41:02)
    0000   0x42 0x29 0x75 0x18 0x0f                   B)u..
    body (0)

#### RECORD 37 SensorAlert 2015-04-25T01:47:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 71}
```
    op hex (3)
    0000   0x0b 0x66 0x47                             .fG
    decimal
             11  102   71
    datetime (2015-04-25T01:47:01)
    0000   0x41 0x2f 0x21 0xb9 0x0f                   A/!..
    body (0)

#### RECORD 38 SensorAlert 2015-04-25T02:06:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 73}
```
    op hex (3)
    0000   0x0b 0x66 0x49                             .fI
    decimal
             11  102   73
    datetime (2015-04-25T02:06:33)
    0000   0x61 0x06 0x22 0xb9 0x0f                   a."..
    body (0)

#### RECORD 39 SensorAlert 2015-04-25T02:27:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 75}
```
    op hex (3)
    0000   0x0b 0x66 0x4b                             .fK
    decimal
             11  102   75
    datetime (2015-04-25T02:27:01)
    0000   0x41 0x1b 0x22 0xb9 0x0f                   A."..
    body (0)

#### RECORD 40 SensorAlert 2015-04-25T06:46:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-04-25T06:46:33)
    0000   0x61 0x2e 0x26 0xb9 0x0f                   a.&..
    body (0)

#### RECORD 41 SensorAlert 2015-04-25T07:07:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 73}
```
    op hex (3)
    0000   0x0b 0x66 0x49                             .fI
    decimal
             11  102   73
    datetime (2015-04-25T07:07:01)
    0000   0x41 0x07 0x27 0xb9 0x0f                   A.'..
    body (0)

#### RECORD 42 SensorAlert 2015-04-25T07:26:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 69}
```
    op hex (3)
    0000   0x0b 0x66 0x45                             .fE
    decimal
             11  102   69
    datetime (2015-04-25T07:26:33)
    0000   0x61 0x1a 0x27 0xb9 0x0f                   a.'..
    body (0)

#### RECORD 43 SensorAlert 2015-04-25T07:47:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 68}
```
    op hex (3)
    0000   0x0b 0x66 0x44                             .fD
    decimal
             11  102   68
    datetime (2015-04-25T07:47:01)
    0000   0x41 0x2f 0x27 0xb9 0x0f                   A/'..
    body (0)

#### RECORD 44 SensorAlert 2015-04-25T08:06:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 71}
```
    op hex (3)
    0000   0x0b 0x66 0x47                             .fG
    decimal
             11  102   71
    datetime (2015-04-25T08:06:33)
    0000   0x61 0x06 0x28 0xb9 0x0f                   a.(..
    body (0)

#### RECORD 45 SensorAlert 2015-04-25T09:26:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 185}
```
    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-04-25T09:26:33)
    0000   0x61 0x1a 0x29 0xb9 0x0f                   a.)..
    body (0)

#### RECORD 46 BolusWizard 2015-04-25T10:19:25 head[2], body[13] op[0x5b]
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
    datetime (2015-04-25T10:19:25)
    0000   0x59 0x13 0x0a 0x19 0x0f                   Y....
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80   10   40   90    0    0    0
              0    0    0    0  120

#### RECORD 47 Bolus 2015-04-25T10:19:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-25T10:19:25)
    0000   0x59 0x13 0x4a 0x19 0x0f                   Y.J..
    body (0)

#### RECORD 48 SensorAlert 2015-04-25T10:55:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 6}
```
    op hex (3)
    0000   0x0b 0x65 0x06                             .e.
    decimal
             11  101    6
    datetime (2015-04-25T10:55:44)
    0000   0x6c 0x37 0x2a 0xb9 0x8f                   l7*..
    body (0)

#### RECORD 49 BolusWizard 2015-04-25T11:01:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.1,
 'carb_input': 31,
 'carb_ratio': 10,
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
    datetime (2015-04-25T11:01:21)
    0000   0x55 0x01 0x0b 0x19 0x0f                   U....
    body (13)
    hex
    0000   0x1f 0x50 0x0a 0x28 0x5a 0x00 0x1f 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x1f 0x78                   ....x
    decimal
             31   80   10   40   90    0   31    0
              0    0    0   31  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 42, 'amount': 3.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x78 0x2a 0x04                   \.x*.
    decimal
             92    5  120   42    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2015-04-25T11:01:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'duration': 0, 'programmed': 3.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2015-04-25T11:01:21)
    0000   0x55 0x01 0x4b 0x19 0x0f                   U.K..
    body (0)

#### RECORD 52 SensorAlert 2015-04-25T12:14:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-25T12:14:00)
    0000   0x40 0x0e 0x2c 0xb9 0x0f                   @.,..
    body (0)

#### RECORD 53 SensorAlert 2015-04-25T13:14:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-25T13:14:00)
    0000   0x40 0x0e 0x2d 0xb9 0x0f                   @.-..
    body (0)

#### RECORD 54 CalBGForPH 2015-04-25T13:35:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 137}
```
    op hex (2)
    0000   0x0a 0x89                                  ..
    decimal
             10  137
    datetime (2015-04-25T13:35:02)
    0000   0x42 0x23 0x2d 0x79 0x0f                   B#-y.
    body (0)

#### RECORD 55 BGReceived 2015-04-25T13:35:02 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2015-04-25T13:35:02)
    0000   0x42 0x23 0x2d 0x79 0x0f                   B#-y.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 56 SensorAlert 2015-04-25T16:06:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-25T16:06:33)
    0000   0x61 0x06 0x30 0xb9 0x0f                   a.0..
    body (0)

#### RECORD 57 BolusWizard 2015-04-25T16:10:22 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 36,
 'carb_ratio': 8,
 'correction_estimate': 0.0,
 'food_estimate': 4.5,
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
    datetime (2015-04-25T16:10:22)
    0000   0x56 0x0a 0x10 0x19 0x0f                   V....
    body (13)
    hex
    0000   0x24 0x50 0x08 0x28 0x5a 0x00 0x2d 0x00    $P.(Z.-.
    0008   0x00 0x00 0x00 0x2d 0x78                   ...-x
    decimal
             36   80    8   40   90    0   45    0
              0    0    0   45  120

#### RECORD 58 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 55, 'amount': 3.1, 'curve': 20},
 {'age': 95, 'amount': 3.0, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x7c 0x37 0x14 0x78 0x5f 0x14    \.|7.x_.
    decimal
             92    8  124   55   20  120   95   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2015-04-25T16:10:22 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5, 'duration': 0, 'programmed': 4.5, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x2d 0x2d 0x00                        .--.
    decimal
              1   45   45    0
    datetime (2015-04-25T16:10:22)
    0000   0x56 0x0a 0x50 0x19 0x0f                   V.P..
    body (0)

#### RECORD 60 SensorAlert 2015-04-25T21:35:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-25T21:35:44)
    0000   0x6c 0x23 0x35 0xb9 0x0f                   l#5..
    body (0)

#### RECORD 61 BolusWizard 2015-04-25T21:36:09 head[2], body[13] op[0x5b]
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
    datetime (2015-04-25T21:36:09)
    0000   0x49 0x24 0x15 0x19 0x0f                   I$...
    body (13)
    hex
    0000   0x2d 0x50 0x06 0x28 0x5a 0x00 0x4b 0x00    -P.(Z.K.
    0008   0x00 0x00 0x00 0x4b 0x78                   ...Kx
    decimal
             45   80    6   40   90    0   75    0
              0    0    0   75  120

#### RECORD 62 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 4.5, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0xb4 0x47 0x14                   \..G.
    decimal
             92    5  180   71   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2015-04-25T21:36:09 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'duration': 0, 'programmed': 4.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2015-04-25T21:36:09)
    0000   0x49 0x24 0x95 0x19 0x0f                   I$...
    body (0)

#### RECORD 64 SensorAlert 2015-04-25T23:07:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-04-25T23:07:01)
    0000   0x41 0x07 0x37 0xb9 0x0f                   A.7..
    body (0)

#### RECORD 65 CalBGForPH 2015-04-25T23:52:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2015-04-25T23:52:56)
    0000   0x78 0x34 0x37 0x79 0x0f                   x47y.
    body (0)

#### RECORD 66 BGReceived 2015-04-25T23:52:56 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2015-04-25T23:52:56)
    0000   0x78 0x34 0x57 0x79 0x0f                   x4Wy.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 67 MResultTotals 2015-04-26T00:00:00 head[5], body[0] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x05 0xfe                   .....
    decimal
              7    0    0    5  254
    datetime (2015-04-26T00:00:00)
    0000   0x59 0x0f                                  Y.
    body (0)

#### RECORD 68 Model522ResultTotals 2015-04-26T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2015-04-26T00:00:00)
    0000   0x59 0x0f                                  Y.
    body (41)
    hex
    0000   0x05 0x00 0x80 0x4c 0xaa 0x03 0x00 0x00    ...L....
    0008   0x05 0xfe 0x03 0x28 0x35 0x02 0xd6 0x2f    ...(5../
    0010   0x00 0x70 0x02 0xd6 0x2f 0x02 0x5e 0x53    .p../.^S
    0018   0x00 0x78 0x11 0x00 0x00 0x00 0x04 0x03    .x......
    0020   0x01 0x00 0x00 0x50 0x8c 0x43 0x06 0x10    ...P.C..
    0028   0x02                                       .
    decimal
              5    0  128   76  170    3    0    0
              5  254    3   40   53    2  214   47
              0  112    2  214   47    2   94   83
              0  120   17    0    0    0    4    3
              1    0    0   80  140   67    6   16
              2

#### RECORD 69 SensorAlert 2015-04-26T01:16:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-04-26T01:16:42)
    0000   0x6a 0x10 0x21 0xba 0x0f                   j.!..
    body (0)

#### RECORD 70 Bolus 2015-04-25T21:38:53 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 240, 'programmed': 3.0, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x08                        ....
    decimal
              1   30   30    8
    datetime (2015-04-25T21:38:53)
    0000   0x75 0x26 0xb5 0x19 0x0f                   u&...
    body (0)

#### RECORD 71 SensorAlert 2015-04-26T02:46:33 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 221}
```
    op hex (3)
    0000   0x0b 0x65 0xdd                             .e.
    decimal
             11  101  221
    datetime (2015-04-26T02:46:33)
    0000   0x61 0x2e 0x22 0xba 0x0f                   a."..
    body (0)

#### RECORD 72 TempBasal 2015-04-26T03:01:24 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.3}
```
    op hex (2)
    0000   0x33 0x34                                  34
    decimal
             51   52
    datetime (2015-04-26T03:01:24)
    0000   0x58 0x01 0x03 0x1a 0x0f                   X....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0

#### RECORD 73 TempBasalDuration 2015-04-26T03:01:24 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 60}
```
    op hex (2)
    0000   0x16 0x02                                  ..
    decimal
             22    2
    datetime (2015-04-26T03:01:24)
    0000   0x58 0x01 0x03 0x1a 0x0f                   X....
    body (0)

#### RECORD 74 SensorAlert 2015-04-26T04:15:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 251}
```
    op hex (3)
    0000   0x0b 0x65 0xfb                             .e.
    decimal
             11  101  251
    datetime (2015-04-26T04:15:44)
    0000   0x6c 0x0f 0x24 0xba 0x0f                   l.$..
    body (0)

#### RECORD 75 SensorAlert 2015-04-26T05:47:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 237}
```
    op hex (3)
    0000   0x0b 0x65 0xed                             .e.
    decimal
             11  101  237
    datetime (2015-04-26T05:47:01)
    0000   0x41 0x2f 0x25 0xba 0x0f                   A/%..
    body (0)

#### RECORD 76 SensorAlert 2015-04-26T07:16:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 220}
```
    op hex (3)
    0000   0x0b 0x65 0xdc                             .e.
    decimal
             11  101  220
    datetime (2015-04-26T07:16:42)
    0000   0x6a 0x10 0x27 0xba 0x0f                   j.'..
    body (0)

#### RECORD 77 BolusWizard 2015-04-26T07:27:19 head[2], body[13] op[0x5b]
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
    datetime (2015-04-26T07:27:19)
    0000   0x53 0x1b 0x07 0x1a 0x0f                   S....
    body (13)
    hex
    0000   0x00 0x50 0x0a 0x28 0x5a 0x00 0x00 0x00    .P.(Z...
    0008   0x00 0x00 0x00 0x00 0x78                   ....x
    decimal
              0   80   10   40   90    0    0    0
              0    0    0    0  120

#### RECORD 78 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 102, 'amount': 0.1, 'curve': 20},
 {'age': 112, 'amount': 0.15, 'curve': 20},
 {'age': 122, 'amount': 0.1, 'curve': 20},
 {'age': 132, 'amount': 0.15, 'curve': 20},
 {'age': 142, 'amount': 0.1, 'curve': 20},
 {'age': 152, 'amount': 0.15, 'curve': 20},
 {'age': 162, 'amount': 0.1, 'curve': 20},
 {'age': 172, 'amount': 0.15, 'curve': 20},
 {'age': 182, 'amount': 0.1, 'curve': 20},
 {'age': 192, 'amount': 0.15, 'curve': 20},
 {'age': 202, 'amount': 0.1, 'curve': 20},
 {'age': 212, 'amount': 0.15, 'curve': 20},
 {'age': 222, 'amount': 0.1, 'curve': 20}]
```
    op hex (41)
    0000   0x5c 0x29 0x04 0x66 0x14 0x06 0x70 0x14    \).f..p.
    0008   0x04 0x7a 0x14 0x06 0x84 0x14 0x04 0x8e    .z......
    0010   0x14 0x06 0x98 0x14 0x04 0xa2 0x14 0x06    ........
    0018   0xac 0x14 0x04 0xb6 0x14 0x06 0xc0 0x14    ........
    0020   0x04 0xca 0x14 0x06 0xd4 0x14 0x04 0xde    ........
    0028   0x14                                       .
    decimal
             92   41    4  102   20    6  112   20
              4  122   20    6  132   20    4  142
             20    6  152   20    4  162   20    6
            172   20    4  182   20    6  192   20
              4  202   20    6  212   20    4  222
             20
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2015-04-26T07:27:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1, 'duration': 0, 'programmed': 1.1, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x0b 0x0b 0x00                        ....
    decimal
              1   11   11    0
    datetime (2015-04-26T07:27:20)
    0000   0x54 0x1b 0x47 0x1a 0x0f                   T.G..
    body (0)

#### RECORD 80 PumpSuspend 2015-04-26T08:50:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2015-04-26T08:50:44)
    0000   0x6c 0x32 0x08 0x1a 0x0f                   l2...
    body (0)

#### RECORD 81 PumpResume 2015-04-26T09:11:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2015-04-26T09:11:35)
    0000   0x63 0x0b 0x09 0x1a 0x0f                   c....
    body (0)

#### RECORD 82 BolusWizard 2015-04-26T10:18:54 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 10,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
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
    datetime (2015-04-26T10:18:54)
    0000   0x76 0x12 0x0a 0x1a 0x0f                   v....
    body (13)
    hex
    0000   0x28 0x50 0x0a 0x28 0x5a 0x00 0x28 0x00    (P.(Z.(.
    0008   0x00 0x00 0x00 0x28 0x78                   ...(x
    decimal
             40   80   10   40   90    0   40    0
              0    0    0   40  120

#### RECORD 83 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 179, 'amount': 1.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0xb3 0x04                   \.,..
    decimal
             92    5   44  179    4
    datetime (unknown)

    body (0)

#### RECORD 84 Bolus 2015-04-26T10:18:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0, 'duration': 0, 'programmed': 3.0, 'type': 'normal'}
```
    op hex (4)
    0000   0x01 0x1e 0x1e 0x00                        ....
    decimal
              1   30   30    0
    datetime (2015-04-26T10:18:54)
    0000   0x76 0x12 0x8a 0x1a 0x0f                   v....
    body (0)

#### RECORD 85 SensorAlert 2015-04-26T10:52:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-04-26T10:52:00)
    0000   0x40 0x34 0x2a 0xba 0x0f                   @4*..
    body (0)

#### RECORD 86 SensorAlert 2015-04-26T11:11:54 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-04-26T11:11:54)
    0000   0x76 0x0b 0x2b 0xba 0x0f                   v.+..
    body (0)

#### RECORD 87 Bolus 2015-04-26T10:20:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'duration': 60, 'programmed': 1.0, 'type': 'square'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x02                        ....
    decimal
              1   10   10    2
    datetime (2015-04-26T10:20:52)
    0000   0x74 0x14 0xaa 0x1a 0x0f                   t....
    body (0)

#### RECORD 88 SensorAlert 2015-04-26T11:52:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-26T11:52:00)
    0000   0x40 0x34 0x2b 0xba 0x0f                   @4+..
    body (0)

#### RECORD 89 SensorAlert 2015-04-26T12:22:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-26T12:22:00)
    0000   0x40 0x16 0x2c 0xba 0x0f                   @.,..
    body (0)

#### RECORD 90 SensorAlert 2015-04-26T12:52:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-04-26T12:52:00)
    0000   0x40 0x34 0x2c 0xba 0x0f                   @4,..
    body (0)

#### RECORD 91 CalBGForPH 2015-04-26T13:14:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2015-04-26T13:14:00)
    0000   0x40 0x0e 0x2d 0x7a 0x0f                   @.-z.
    body (0)

#### RECORD 92 BGReceived 2015-04-26T13:14:00 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2015-04-26T13:14:00)
    0000   0x40 0x0e 0x4d 0x7a 0x0f                   @.Mz.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 93 BolusWizard 2015-04-26T13:14:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 234,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.9,
 'carb_input': 0,
 'carb_ratio': 8,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xea                                  [.
    decimal
             91  234
    datetime (2015-04-26T13:14:13)
    0000   0x4d 0x0e 0x0d 0x1a 0x0f                   M....
    body (13)
    hex
    0000   0x00 0x50 0x08 0x28 0x5a 0x1c 0x00 0x00    .P.(Z...
    0008   0x00 0x09 0x00 0x13 0x78                   ....x
    decimal
              0   80    8   40   90   28    0    0
              0    9    0   19  120

`end ReadHistoryData-page-4.data: 94 records`
