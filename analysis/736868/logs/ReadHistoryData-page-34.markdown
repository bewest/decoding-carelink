## START ReadHistoryData-page-34.data
#### STOPPING DOUBLE NULLS @ 1013, found 9 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x4e 0x83                                  N.
##### DEBUG DECIMAL
             78  131
#### RECORD 0 SensorAlert 2015-02-08T05:31:19 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-02-08T05:31:19)
    0000   0x13 0x9f 0x25 0xa8 0x0f                   ..%..
    body (0)

#### RECORD 1 BasalProfileStart 2015-02-08T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-08T07:00:00)
    0000   0x00 0x80 0x07 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 2 SensorAlert 2015-02-08T07:00:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 220}
```
    op hex (3)
    0000   0x0b 0x65 0xdc                             .e.
    decimal
             11  101  220
    datetime (2015-02-08T07:00:30)
    0000   0x1e 0x80 0x27 0xa8 0x0f                   ..'..
    body (0)

#### RECORD 3 LowReservoir 2015-02-08T07:24:42 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-02-08T07:24:42)
    0000   0x2a 0x98 0x07 0x08 0x0f                   *....
    body (0)

#### RECORD 4 SensorAlert 2015-02-08T08:31:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 192}
```
    op hex (3)
    0000   0x0b 0x65 0xc0                             .e.
    decimal
             11  101  192
    datetime (2015-02-08T08:31:47)
    0000   0x2f 0x9f 0x28 0xa8 0x0f                   /.(..
    body (0)

#### RECORD 5 Bolus 2015-02-08T08:57:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x00 0x00    ..P.P...
    decimal
              1    0   80    0   80    0    0    0
    datetime (2015-02-08T08:57:59)
    0000   0x3b 0xb9 0x48 0x68 0x0f                   ;.Hh.
    body (0)

#### RECORD 6 BolusWizard 2015-02-08T09:12:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 36,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-08T09:12:56)
    0000   0x38 0x8c 0x09 0x68 0x0f                   8..h.
    body (15)
    hex
    0000   0x24 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    $P.d(Z..
    0008   0x90 0x00 0x00 0x00 0x00 0x90 0x78         ......x
    decimal
             36   80    0  100   40   90    0    0
            144    0    0    0    0  144  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 2.0}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x10 0x04                   \.P..
    decimal
             92    5   80   16    4
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2015-02-08T09:12:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6,
 'duration': 0,
 'programmed': 3.6,
 'type': 'normal',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x50 0x00    ......P.
    decimal
              1    0  144    0  144    0   80    0
    datetime (2015-02-08T09:12:56)
    0000   0x38 0x8c 0x49 0x68 0x0f                   8.Ih.
    body (0)

#### RECORD 9 SensorAlert 2015-02-08T09:45:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-08T09:45:52)
    0000   0x34 0xad 0x29 0xa8 0x0f                   4.)..
    body (0)

#### RECORD 10 BolusWizard 2015-02-08T09:47:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.5,
 'carb_input': 35,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-08T09:47:03)
    0000   0x03 0xaf 0x09 0x68 0x0f                   ...h.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    #P.d(Z..
    0008   0x8c 0x00 0x00 0x00 0x00 0x8c 0x78         ......x
    decimal
             35   80    0  100   40   90    0    0
            140    0    0    0    0  140  120

#### RECORD 11 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 41, 'amount': 3.6}, {'age': 51, 'amount': 2.0}]
```
    op hex (8)
    0000   0x5c 0x08 0x90 0x29 0x04 0x50 0x33 0x04    \..).P3.
    decimal
             92    8  144   41    4   80   51    4
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2015-02-08T09:47:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 5.1}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0xcc 0x00    ........
    decimal
              1    0  140    0  140    0  204    0
    datetime (2015-02-08T09:47:03)
    0000   0x03 0xaf 0x49 0x68 0x0f                   ..Ih.
    body (0)

#### RECORD 13 BasalProfileStart 2015-02-08T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-08T10:00:00)
    0000   0x00 0x80 0x0a 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 14 SensorAlert 2015-02-08T10:01:28 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 193}
```
    op hex (3)
    0000   0x0b 0x65 0xc1                             .e.
    decimal
             11  101  193
    datetime (2015-02-08T10:01:28)
    0000   0x1c 0x81 0x2a 0xa8 0x0f                   ..*..
    body (0)

#### RECORD 15 SensorAlert 2015-02-08T11:31:19 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 240}
```
    op hex (3)
    0000   0x0b 0x65 0xf0                             .e.
    decimal
             11  101  240
    datetime (2015-02-08T11:31:19)
    0000   0x13 0x9f 0x2b 0xa8 0x0f                   ..+..
    body (0)

#### RECORD 16 Bolus 2015-02-08T11:32:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 3.6}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x90 0x00    ........
    decimal
              1    0  160    0  160    0  144    0
    datetime (2015-02-08T11:32:37)
    0000   0x25 0xa0 0x4b 0x68 0x0f                   %.Kh.
    body (0)

#### RECORD 17 Bolus 2015-02-08T11:35:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x01 0x2c 0x00    ..P.P.,.
    decimal
              1    0   80    0   80    1   44    0
    datetime (2015-02-08T11:35:43)
    0000   0x2b 0xa3 0x4b 0x68 0x0f                   +.Kh.
    body (0)

#### RECORD 18 BasalProfileStart 2015-02-08T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-08T12:00:00)
    0000   0x00 0x80 0x0c 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 19 SensorAlert 2015-02-08T12:31:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Sensor End', 'alarm_type': 107}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-02-08T12:31:47)
    0000   0x2f 0x9f 0x2c 0xa8 0x0f                   /.,..
    body (0)

#### RECORD 20 Bolus 2015-02-08T12:44:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 5.5}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x28 0x00 0xdc 0x00    ..x.(...
    decimal
              1    0  120    0   40    0  220    0
    datetime (2015-02-08T12:44:31)
    0000   0x1f 0xac 0x4c 0x68 0x0f                   ..Lh.
    body (0)

#### RECORD 21 NoDelivery 2015-02-08T12:45:11 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-02-08T12:45:11)
    0000   0x0b 0xad 0x4c 0x48 0x0f                   ..LH.
    body (0)

#### RECORD 22 ClearAlarm 2015-02-08T12:52:06 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-02-08T12:52:06)
    0000   0x06 0xb4 0x0c 0x08 0x0f                   .....
    body (0)

#### RECORD 23 Rewind 2015-02-08T13:15:19 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-02-08T13:15:19)
    0000   0x13 0x8f 0x0d 0x08 0x0f                   .....
    body (0)

#### RECORD 24 Prime 2015-02-08T13:16:44 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 4.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x2b                   ....+
    decimal
              3    0    0    0   43
    datetime (2015-02-08T13:16:44)
    0000   0x2c 0x90 0x2d 0x08 0x0f                   ,.-..
    body (0)

#### RECORD 25 BasalProfileStart 2015-02-08T13:17:30 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-08T13:17:30)
    0000   0x1e 0x91 0x0d 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 26 Prime 2015-02-08T13:17:16 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-02-08T13:17:16)
    0000   0x10 0x91 0x0d 0x08 0x0f                   .....
    body (0)

#### RECORD 27 Bolus 2015-02-08T13:18:26 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 4.4}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xb0 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  176    0
    datetime (2015-02-08T13:18:26)
    0000   0x1a 0x92 0x4d 0x68 0x0f                   ..Mh.
    body (0)

#### RECORD 28 CalBGForPH 2015-02-08T13:56:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 102}
```
    op hex (2)
    0000   0x0a 0x66                                  .f
    decimal
             10  102
    datetime (2015-02-08T13:56:34)
    0000   0x22 0xb8 0x2d 0x68 0x0f                   ".-h.
    body (0)

#### RECORD 29 BGReceived 2015-02-08T13:56:34 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 102, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2015-02-08T13:56:34)
    0000   0x22 0xb8 0xcd 0x68 0x0f                   "..h.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 30 PumpSuspend 2015-02-08T14:35:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-08T14:35:15)
    0000   0x0f 0xa3 0x0e 0x08 0x0f                   .....
    body (0)

#### RECORD 31 BasalProfileStart 2015-02-08T15:04:03 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-08T15:04:03)
    0000   0x03 0x84 0x0f 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 32 PumpResume 2015-02-08T15:04:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-08T15:04:03)
    0000   0x03 0x84 0x0f 0x08 0x0f                   .....
    body (0)

#### RECORD 33 BolusWizard 2015-02-08T16:06:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.5,
 'carb_input': 44,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-08T16:06:06)
    0000   0x06 0x86 0x10 0x68 0x0f                   ...h.
    body (15)
    hex
    0000   0x2c 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    ,P.P(Z..
    0008   0xdc 0x00 0x00 0x00 0x00 0xdc 0x78         ......x
    decimal
             44   80    0   80   40   90    0    0
            220    0    0    0    0  220  120

#### RECORD 34 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 170, 'amount': 1.5},
 {'age': 210, 'amount': 1.0},
 {'age': 270, 'amount': 1.55},
 {'age': 280, 'amount': 4.45},
 {'age': 380, 'amount': 3.5},
 {'age': 420, 'amount': 3.6},
 {'age': 430, 'amount': 2.0}]
```
    op hex (23)
    0000   0x5c 0x17 0x3c 0xaa 0x04 0x28 0xd2 0x04    \.<..(..
    0008   0x3e 0x0e 0x14 0xb2 0x18 0x14 0x8c 0x7c    >......|
    0010   0x14 0x90 0xa4 0x14 0x50 0xae 0x14         ....P..
    decimal
             92   23   60  170    4   40  210    4
             62   14   20  178   24   20  140  124
             20  144  164   20   80  174   20
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2015-02-08T16:08:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 30,
 'programmed': 2.5,
 'type': 'square',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x14 0x01    ..d.d...
    decimal
              1    0  100    0  100    0   20    1
    datetime (2015-02-08T16:08:07)
    0000   0x07 0x88 0xb0 0x68 0x0f                   ...h.
    body (0)

#### RECORD 36 Bolus 2015-02-08T16:06:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x14 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   20    0
    datetime (2015-02-08T16:06:06)
    0000   0x06 0x86 0x90 0x68 0x0f                   ...h.
    body (0)

#### RECORD 37 Bolus 2015-02-08T17:58:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 3.1}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x7c 0x00    ......|.
    decimal
              1    0  160    0  160    0  124    0
    datetime (2015-02-08T17:58:04)
    0000   0x04 0xba 0x51 0x68 0x0f                   ..Qh.
    body (0)

#### RECORD 38 Bolus 2015-02-08T20:08:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x44 0x00    ......D.
    decimal
              1    0  160    0  160    0   68    0
    datetime (2015-02-08T20:08:45)
    0000   0x2d 0x88 0x54 0x68 0x0f                   -.Th.
    body (0)

#### RECORD 39 Bolus 2015-02-08T20:12:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 5.7}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xe4 0x00    ........
    decimal
              1    0  160    0  160    0  228    0
    datetime (2015-02-08T20:12:03)
    0000   0x03 0x8c 0x54 0x68 0x0f                   ..Th.
    body (0)

#### RECORD 40 BasalProfileStart 2015-02-08T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-08T22:00:00)
    0000   0x00 0x80 0x16 0x08 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 41 BolusWizard 2015-02-08T22:18:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 11.6,
 'carb_input': 70,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 11.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-08T22:18:22)
    0000   0x16 0x92 0x16 0x68 0x0f                   ...h.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    FP.<(Z..
    0008   0xd0 0x00 0x00 0x00 0x01 0xd0 0x78         ......x
    decimal
             70   80    0   60   40   90    0    1
            208    0    0    0    1  208  120

#### RECORD 42 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 132, 'amount': 1.6},
 {'age': 262, 'amount': 4.0},
 {'age': 342, 'amount': 0.2},
 {'age': 352, 'amount': 0.8},
 {'age': 362, 'amount': 0.85},
 {'age': 372, 'amount': 3.65}]
```
    op hex (20)
    0000   0x5c 0x14 0x40 0x84 0x05 0xa0 0x06 0x14    \.@.....
    0008   0x08 0x56 0x14 0x20 0x60 0x14 0x22 0x6a    .V. `."j
    0010   0x14 0x92 0x74 0x14                        ..t.
    decimal
             92   20   64  132    5  160    6   20
              8   86   20   32   96   20   34  106
             20  146  116   20
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2015-02-08T22:21:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6,
 'duration': 300,
 'programmed': 0.6,
 'type': 'square',
 'unabsorbed': 3.2}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x80 0x0a    ........
    decimal
              1    1   24    1   24    0  128   10
    datetime (2015-02-08T22:21:02)
    0000   0x02 0x95 0xb6 0x68 0x0f                   ...h.
    body (0)

#### RECORD 44 Bolus 2015-02-08T22:18:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 3.2}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x80 0x00    ........
    decimal
              1    0  160    0  160    0  128    0
    datetime (2015-02-08T22:18:22)
    0000   0x16 0x92 0x96 0x68 0x0f                   ...h.
    body (0)

#### RECORD 45 BasalProfileStart 2015-02-09T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-09T00:00:00)
    0000   0x00 0x80 0x00 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 46 MResultTotals 2015-02-09T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0xa1                   .....
    decimal
              7    0    0   10  161
    datetime (2015-02-09T00:00:00)
    0000   0x28 0x0f                                  (.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 47 Sara6E 2015-02-09T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-09T00:00:00)
    0000   0x28 0x0f                                  (.
    body (49)
    hex
    0000   0x05 0x00 0x60 0x59 0x66 0x02 0x00 0x00    ..`Yf...
    0008   0x0a 0xa1 0x03 0x11 0x1d 0x07 0x90 0x47    .......G
    0010   0x00 0xb9 0x02 0xf4 0x00 0x00 0x00 0x00    ........
    0018   0x04 0x9c 0x04 0x00 0x00 0x0a 0x00 0xd5    ........
    0020   0x44 0x1d 0x03 0x96 0x52 0x01 0x01 0x00    D...R...
    0028   0x00 0x01 0x06 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0   96   89  102    2    0    0
             10  161    3   17   29    7  144   71
              0  185    2  244    0    0    0    0
              4  156    4    0    0   10    0  213
             68   29    3  150   82    1    1    0
              0    1    6    0    0    0    0    0
              0

#### RECORD 48 BasalProfileStart 2015-02-09T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-09T04:00:00)
    0000   0x00 0x80 0x04 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 49 CalBGForPH 2015-02-09T06:42:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2015-02-09T06:42:46)
    0000   0x2e 0xaa 0x26 0x69 0x0f                   ..&i.
    body (0)

#### RECORD 50 BGReceived 2015-02-09T06:42:46 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 153, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2015-02-09T06:42:46)
    0000   0x2e 0xaa 0x26 0x69 0x0f                   ..&i.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 51 BolusWizard 2015-02-09T06:43:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 153,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0x99                                  [.
    decimal
             91  153
    datetime (2015-02-09T06:43:07)
    0000   0x07 0xab 0x06 0x09 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x20 0x00    .P.d(Z .
    0008   0x00 0x00 0x00 0x04 0x00 0x1c 0x78         ......x
    decimal
              0   80    0  100   40   90   32    0
              0    0    0    4    0   28  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[86], body[0] op[0x5c]
###### DECODED
```python
[{'age': 207, 'amount': 0.1},
 {'age': 217, 'amount': 0.25},
 {'age': 227, 'amount': 0.25},
 {'age': 237, 'amount': 0.2},
 {'age': 247, 'amount': 0.25},
 {'age': 257, 'amount': 0.25},
 {'age': 267, 'amount': 0.2},
 {'age': 277, 'amount': 0.25},
 {'age': 287, 'amount': 0.25},
 {'age': 297, 'amount': 0.2},
 {'age': 307, 'amount': 0.25},
 {'age': 317, 'amount': 0.25},
 {'age': 327, 'amount': 0.2},
 {'age': 337, 'amount': 0.25},
 {'age': 347, 'amount': 0.25},
 {'age': 357, 'amount': 0.2},
 {'age': 367, 'amount': 0.25},
 {'age': 377, 'amount': 0.25},
 {'age': 387, 'amount': 0.2},
 {'age': 397, 'amount': 0.25},
 {'age': 407, 'amount': 0.25},
 {'age': 417, 'amount': 0.2},
 {'age': 427, 'amount': 0.25},
 {'age': 437, 'amount': 0.25},
 {'age': 447, 'amount': 0.2},
 {'age': 457, 'amount': 0.25},
 {'age': 467, 'amount': 0.25},
 {'age': 477, 'amount': 0.2}]
```
    op hex (86)
    0000   0x5c 0x56 0x04 0xcf 0x04 0x0a 0xd9 0x04    \V......
    0008   0x0a 0xe3 0x04 0x08 0xed 0x04 0x0a 0xf7    ........
    0010   0x04 0x0a 0x01 0x14 0x08 0x0b 0x14 0x0a    ........
    0018   0x15 0x14 0x0a 0x1f 0x14 0x08 0x29 0x14    ......).
    0020   0x0a 0x33 0x14 0x0a 0x3d 0x14 0x08 0x47    .3..=..G
    0028   0x14 0x0a 0x51 0x14 0x0a 0x5b 0x14 0x08    ..Q..[..
    0030   0x65 0x14 0x0a 0x6f 0x14 0x0a 0x79 0x14    e..o..y.
    0038   0x08 0x83 0x14 0x0a 0x8d 0x14 0x0a 0x97    ........
    0040   0x14 0x08 0xa1 0x14 0x0a 0xab 0x14 0x0a    ........
    0048   0xb5 0x14 0x08 0xbf 0x14 0x0a 0xc9 0x14    ........
    0050   0x0a 0xd3 0x14 0x08 0xdd 0x14              ......
    decimal
             92   86    4  207    4   10  217    4
             10  227    4    8  237    4   10  247
              4   10    1   20    8   11   20   10
             21   20   10   31   20    8   41   20
             10   51   20   10   61   20    8   71
             20   10   81   20   10   91   20    8
            101   20   10  111   20   10  121   20
              8  131   20   10  141   20   10  151
             20    8  161   20   10  171   20   10
            181   20    8  191   20   10  201   20
             10  211   20    8  221   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2015-02-09T06:43:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x04 0x00    ........
    decimal
              1    0    0    0    0    0    4    0
    datetime (2015-02-09T06:43:07)
    0000   0x07 0xab 0xa6 0x09 0x0f                   .....
    body (0)

#### RECORD 54 Bolus 2015-02-09T06:43:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7,
 'duration': 0,
 'programmed': 0.7,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x04 0x00    ........
    decimal
              1    0   28    0   28    0    4    0
    datetime (2015-02-09T06:43:07)
    0000   0x07 0xab 0x86 0x09 0x0f                   .....
    body (0)

#### RECORD 55 PumpSuspend 2015-02-09T06:56:57 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-09T06:56:57)
    0000   0x39 0xb8 0x06 0x09 0x0f                   9....
    body (0)

#### RECORD 56 BasalProfileStart 2015-02-09T07:18:26 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-09T07:18:26)
    0000   0x1a 0x92 0x07 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 57 PumpResume 2015-02-09T07:18:26 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-09T07:18:26)
    0000   0x1a 0x92 0x07 0x09 0x0f                   .....
    body (0)

#### RECORD 58 BolusWizard 2015-02-09T07:46:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 50,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-09T07:46:03)
    0000   0x03 0xae 0x07 0x69 0x0f                   ...i.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 59 UnabsorbedInsulinBolus unknown head[68], body[0] op[0x5c]
###### DECODED
```python
[{'age': 70, 'amount': 0.7},
 {'age': 270, 'amount': 0.1},
 {'age': 280, 'amount': 0.25},
 {'age': 290, 'amount': 0.25},
 {'age': 300, 'amount': 0.2},
 {'age': 310, 'amount': 0.25},
 {'age': 320, 'amount': 0.25},
 {'age': 330, 'amount': 0.2},
 {'age': 340, 'amount': 0.25},
 {'age': 350, 'amount': 0.25},
 {'age': 360, 'amount': 0.2},
 {'age': 370, 'amount': 0.25},
 {'age': 380, 'amount': 0.25},
 {'age': 390, 'amount': 0.2},
 {'age': 400, 'amount': 0.25},
 {'age': 410, 'amount': 0.25},
 {'age': 420, 'amount': 0.2},
 {'age': 430, 'amount': 0.25},
 {'age': 440, 'amount': 0.25},
 {'age': 450, 'amount': 0.2},
 {'age': 460, 'amount': 0.25},
 {'age': 470, 'amount': 0.25}]
```
    op hex (68)
    0000   0x5c 0x44 0x1c 0x46 0x04 0x04 0x0e 0x14    \D.F....
    0008   0x0a 0x18 0x14 0x0a 0x22 0x14 0x08 0x2c    ...."..,
    0010   0x14 0x0a 0x36 0x14 0x0a 0x40 0x14 0x08    ..6..@..
    0018   0x4a 0x14 0x0a 0x54 0x14 0x0a 0x5e 0x14    J..T..^.
    0020   0x08 0x68 0x14 0x0a 0x72 0x14 0x0a 0x7c    .h..r..|
    0028   0x14 0x08 0x86 0x14 0x0a 0x90 0x14 0x0a    ........
    0030   0x9a 0x14 0x08 0xa4 0x14 0x0a 0xae 0x14    ........
    0038   0x0a 0xb8 0x14 0x08 0xc2 0x14 0x0a 0xcc    ........
    0040   0x14 0x0a 0xd6 0x14                        ....
    decimal
             92   68   28   70    4    4   14   20
             10   24   20   10   34   20    8   44
             20   10   54   20   10   64   20    8
             74   20   10   84   20   10   94   20
              8  104   20   10  114   20   10  124
             20    8  134   20   10  144   20   10
            154   20    8  164   20   10  174   20
             10  184   20    8  194   20   10  204
             20   10  214   20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2015-02-09T07:48:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 30,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x18 0x01    ..P.P...
    decimal
              1    0   80    0   80    0   24    1
    datetime (2015-02-09T07:48:03)
    0000   0x03 0xb0 0xa7 0x69 0x0f                   ...i.
    body (0)

#### RECORD 61 Bolus 2015-02-09T07:46:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x18 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   24    0
    datetime (2015-02-09T07:46:03)
    0000   0x03 0xae 0x87 0x69 0x0f                   ...i.
    body (0)

#### RECORD 62 SensorAlert 2015-02-09T09:38:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-09T09:38:21)
    0000   0x15 0xa6 0x29 0xa9 0x0f                   ..)..
    body (0)

#### RECORD 63 BasalProfileStart 2015-02-09T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-09T10:00:00)
    0000   0x00 0x80 0x0a 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 64 SensorAlert 2015-02-09T10:08:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-09T10:08:00)
    0000   0x00 0x88 0x2a 0xa9 0x0f                   ..*..
    body (0)

#### RECORD 65 SensorAlert 2015-02-09T10:38:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-09T10:38:00)
    0000   0x00 0xa6 0x2a 0xa9 0x0f                   ..*..
    body (0)

#### RECORD 66 CalBGForPH 2015-02-09T10:40:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 239}
```
    op hex (2)
    0000   0x0a 0xef                                  ..
    decimal
             10  239
    datetime (2015-02-09T10:40:08)
    0000   0x08 0xa8 0x2a 0x69 0x0f                   ..*i.
    body (0)

#### RECORD 67 BGReceived 2015-02-09T10:40:08 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 239, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2015-02-09T10:40:08)
    0000   0x08 0xa8 0xea 0x69 0x0f                   ...i.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 68 BolusWizard 2015-02-09T10:40:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 239,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 2.9,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.1}
```
    op hex (2)
    0000   0x5b 0xef                                  [.
    decimal
             91  239
    datetime (2015-02-09T10:40:21)
    0000   0x15 0xa8 0x0a 0x09 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x74 0x00    .P.d(Zt.
    0008   0x00 0x00 0x00 0x2c 0x00 0x48 0x78         ...,.Hx
    decimal
              0   80    0  100   40   90  116    0
              0    0    0   44    0   72  120

#### RECORD 69 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 144, 'amount': 0.15},
 {'age': 154, 'amount': 0.65},
 {'age': 164, 'amount': 0.65},
 {'age': 174, 'amount': 3.55},
 {'age': 244, 'amount': 0.7},
 {'age': 444, 'amount': 0.1},
 {'age': 454, 'amount': 0.25},
 {'age': 464, 'amount': 0.25},
 {'age': 474, 'amount': 0.2}]
```
    op hex (29)
    0000   0x5c 0x1d 0x06 0x90 0x04 0x1a 0x9a 0x04    \.......
    0008   0x1a 0xa4 0x04 0x8e 0xae 0x04 0x1c 0xf4    ........
    0010   0x04 0x04 0xbc 0x14 0x0a 0xc6 0x14 0x0a    ........
    0018   0xd0 0x14 0x08 0xda 0x14                   .....
    decimal
             92   29    6  144    4   26  154    4
             26  164    4  142  174    4   28  244
              4    4  188   20   10  198   20   10
            208   20    8  218   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2015-02-09T10:40:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x2c 0x00    ......,.
    decimal
              1    0    0    0    0    0   44    0
    datetime (2015-02-09T10:40:21)
    0000   0x15 0xa8 0xaa 0x09 0x0f                   .....
    body (0)

`end ReadHistoryData-page-34.data: 71 records`
