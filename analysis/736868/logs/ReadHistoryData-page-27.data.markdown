## START analysis/736868/logs/ReadHistoryData-page-27.data
#### STOPPING DOUBLE NULLS @ 994, found 28 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe5 0x7b                                  .{
##### DEBUG DECIMAL
            229  123
#### RECORD 0 BolusWizard 2015-02-16T09:30:00 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-16T09:30:00)
    0000   0x00 0x9e 0x09 0x70 0x0f                   ...p.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    (P.d(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             40   80    0  100   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 1 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 44, 'amount': 2.5, 'curve': 4},
 {'age': 234, 'amount': 0.05, 'curve': 4},
 {'age': 244, 'amount': 0.25, 'curve': 4},
 {'age': 254, 'amount': 0.25, 'curve': 4},
 {'age': 8, 'amount': 0.2, 'curve': 20},
 {'age': 18, 'amount': 0.25, 'curve': 20},
 {'age': 28, 'amount': 0.25, 'curve': 20},
 {'age': 38, 'amount': 0.2, 'curve': 20},
 {'age': 48, 'amount': 0.25, 'curve': 20},
 {'age': 58, 'amount': 0.25, 'curve': 20},
 {'age': 68, 'amount': 0.2, 'curve': 20},
 {'age': 78, 'amount': 0.25, 'curve': 20},
 {'age': 88, 'amount': 0.25, 'curve': 20},
 {'age': 98, 'amount': 3.15, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0x64 0x2c 0x04 0x02 0xea 0x04    \,d,....
    0008   0x0a 0xf4 0x04 0x0a 0xfe 0x04 0x08 0x08    ........
    0010   0x14 0x0a 0x12 0x14 0x0a 0x1c 0x14 0x08    ........
    0018   0x26 0x14 0x0a 0x30 0x14 0x0a 0x3a 0x14    &..0..:.
    0020   0x08 0x44 0x14 0x0a 0x4e 0x14 0x0a 0x58    .D..N..X
    0028   0x14 0x7e 0x62 0x14                        .~b.
    decimal
             92   44  100   44    4    2  234    4
             10  244    4   10  254    4    8    8
             20   10   18   20   10   28   20    8
             38   20   10   48   20   10   58   20
              8   68   20   10   78   20   10   88
             20  126   98   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2015-02-16T09:30:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x5c 0x00    ......\.
    decimal
              1    0    0    0    0    0   92    0
    datetime (2015-02-16T09:30:00)
    0000   0x00 0x9e 0xa9 0x70 0x0f                   ...p.
    body (0)

#### RECORD 3 Bolus 2015-02-16T09:30:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x5c 0x00    ......\.
    decimal
              1    0  160    0  160    0   92    0
    datetime (2015-02-16T09:30:01)
    0000   0x01 0x9e 0x89 0x70 0x0f                   ...p.
    body (0)

#### RECORD 4 PumpSuspend 2015-02-16T09:39:42 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-16T09:39:42)
    0000   0x2a 0xa7 0x09 0x10 0x0f                   *....
    body (0)

#### RECORD 5 BasalProfileStart 2015-02-16T10:16:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-16T10:16:00)
    0000   0x00 0x90 0x0a 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 6 PumpResume 2015-02-16T10:16:00 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-16T10:16:00)
    0000   0x00 0x90 0x0a 0x10 0x0f                   .....
    body (0)

#### RECORD 7 LowReservoir 2015-02-16T11:42:51 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-02-16T11:42:51)
    0000   0x33 0xaa 0x0b 0x10 0x0f                   3....
    body (0)

#### RECORD 8 BolusWizard 2015-02-16T11:43:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.2,
 'carb_input': 50,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 6.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-16T11:43:22)
    0000   0x16 0xab 0x0b 0x70 0x0f                   ...p.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    2P.P(Z..
    0008   0xf8 0x00 0x00 0x00 0x00 0xf8 0x78         ......x
    decimal
             50   80    0   80   40   90    0    0
            248    0    0    0    0  248  120

#### RECORD 9 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 4.0, 'curve': 4},
 {'age': 177, 'amount': 2.5, 'curve': 4},
 {'age': 111, 'amount': 0.05, 'curve': 20},
 {'age': 121, 'amount': 0.25, 'curve': 20},
 {'age': 131, 'amount': 0.25, 'curve': 20},
 {'age': 141, 'amount': 0.2, 'curve': 20},
 {'age': 151, 'amount': 0.25, 'curve': 20},
 {'age': 161, 'amount': 0.25, 'curve': 20},
 {'age': 171, 'amount': 0.2, 'curve': 20},
 {'age': 181, 'amount': 0.25, 'curve': 20},
 {'age': 191, 'amount': 0.25, 'curve': 20},
 {'age': 201, 'amount': 0.2, 'curve': 20},
 {'age': 211, 'amount': 0.25, 'curve': 20},
 {'age': 221, 'amount': 0.25, 'curve': 20}]
```
    op hex (44)
    0000   0x5c 0x2c 0xa0 0x89 0x04 0x64 0xb1 0x04    \,...d..
    0008   0x02 0x6f 0x14 0x0a 0x79 0x14 0x0a 0x83    .o..y...
    0010   0x14 0x08 0x8d 0x14 0x0a 0x97 0x14 0x0a    ........
    0018   0xa1 0x14 0x08 0xab 0x14 0x0a 0xb5 0x14    ........
    0020   0x0a 0xbf 0x14 0x08 0xc9 0x14 0x0a 0xd3    ........
    0028   0x14 0x0a 0xdd 0x14                        ....
    decimal
             92   44  160  137    4  100  177    4
              2  111   20   10  121   20   10  131
             20    8  141   20   10  151   20   10
            161   20    8  171   20   10  181   20
             10  191   20    8  201   20   10  211
             20   10  221   20
    datetime (unknown)

    body (0)

#### RECORD 10 Bolus 2015-02-16T11:45:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3,
 'duration': 60,
 'programmed': 2.3,
 'type': 'square',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x50 0x02    ..\.\.P.
    decimal
              1    0   92    0   92    0   80    2
    datetime (2015-02-16T11:45:59)
    0000   0x3b 0xad 0xab 0x70 0x0f                   ;..p.
    body (0)

#### RECORD 11 Bolus 2015-02-16T11:43:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9,
 'duration': 0,
 'programmed': 3.9,
 'type': 'normal',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x50 0x00    ......P.
    decimal
              1    0  156    0  156    0   80    0
    datetime (2015-02-16T11:43:23)
    0000   0x17 0xab 0x8b 0x70 0x0f                   ...p.
    body (0)

#### RECORD 12 BasalProfileStart 2015-02-16T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-16T12:00:00)
    0000   0x00 0x80 0x0c 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 13 Bolus 2015-02-16T12:02:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 5.8}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0xe8 0x00    ........
    decimal
              1    0  140    0  140    0  232    0
    datetime (2015-02-16T12:02:57)
    0000   0x39 0x82 0x4c 0x70 0x0f                   9.Lp.
    body (0)

#### RECORD 14 Bolus 2015-02-16T12:12:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 2.9}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x01 0x74 0x00    ..x.x.t.
    decimal
              1    0  120    0  120    1  116    0
    datetime (2015-02-16T12:12:06)
    0000   0x06 0x8c 0x4c 0x70 0x0f                   ..Lp.
    body (0)

#### RECORD 15 SensorAlert 2015-02-16T12:14:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-16T12:14:08)
    0000   0x08 0x8e 0x2c 0xb0 0x0f                   ..,..
    body (0)

#### RECORD 16 CalBGForPH 2015-02-16T12:17:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 240}
```
    op hex (2)
    0000   0x0a 0xf0                                  ..
    decimal
             10  240
    datetime (2015-02-16T12:17:28)
    0000   0x1c 0x91 0x2c 0x70 0x0f                   ..,p.
    body (0)

#### RECORD 17 BGReceived 2015-02-16T12:17:28 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1e                                  ?.
    decimal
             63   30
    datetime (2015-02-16T12:17:28)
    0000   0x1c 0x91 0x0c 0x70 0x0f                   ...p.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 18 SensorAlert 2015-02-16T12:30:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 240}
```
    op hex (3)
    0000   0x0b 0x65 0xf0                             .e.
    decimal
             11  101  240
    datetime (2015-02-16T12:30:18)
    0000   0x12 0x9e 0x2c 0xb0 0x0f                   ..,..
    body (0)

#### RECORD 19 PumpSuspend 2015-02-16T13:38:46 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-16T13:38:46)
    0000   0x2e 0xa6 0x0d 0x10 0x0f                   .....
    body (0)

#### RECORD 20 SensorAlert 2015-02-16T14:25:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-16T14:25:25)
    0000   0x19 0x99 0x2e 0xb0 0x0f                   .....
    body (0)

#### RECORD 21 BasalProfileStart 2015-02-16T14:27:06 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-16T14:27:06)
    0000   0x06 0x9b 0x0e 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 22 PumpResume 2015-02-16T14:27:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-16T14:27:06)
    0000   0x06 0x9b 0x0e 0x10 0x0f                   .....
    body (0)

#### RECORD 23 SensorAlert 2015-02-16T14:35:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-16T14:35:06)
    0000   0x06 0xa3 0x2e 0xb0 0x0f                   .....
    body (0)

#### RECORD 24 BasalProfileStart 2015-02-16T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-16T15:00:00)
    0000   0x00 0x80 0x0f 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 25 SensorAlert 2015-02-16T16:04:57 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 31}
```
    op hex (3)
    0000   0x0b 0x65 0x1f                             .e.
    decimal
             11  101   31
    datetime (2015-02-16T16:04:57)
    0000   0x39 0x84 0x30 0xb0 0x8f                   9.0..
    body (0)

#### RECORD 26 Bolus 2015-02-16T16:05:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x0c 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   12    0
    datetime (2015-02-16T16:05:21)
    0000   0x15 0x85 0x50 0x70 0x0f                   ..Pp.
    body (0)

#### RECORD 27 BolusWizard 2015-02-16T16:18:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 1.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-16T16:18:47)
    0000   0x2f 0x92 0x10 0x70 0x0f                   /..p.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 28 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 12, 'amount': 2.05, 'curve': 4},
 {'age': 22, 'amount': 0.95, 'curve': 4},
 {'age': 212, 'amount': 0.1, 'curve': 4},
 {'age': 222, 'amount': 0.4, 'curve': 4},
 {'age': 232, 'amount': 0.35, 'curve': 4},
 {'age': 242, 'amount': 0.4, 'curve': 4},
 {'age': 252, 'amount': 3.35, 'curve': 4},
 {'age': 6, 'amount': 3.8, 'curve': 20},
 {'age': 16, 'amount': 0.4, 'curve': 20},
 {'age': 26, 'amount': 3.9, 'curve': 20},
 {'age': 156, 'amount': 4.0, 'curve': 20},
 {'age': 196, 'amount': 2.5, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x52 0x0c 0x04 0x26 0x16 0x04    \&R..&..
    0008   0x04 0xd4 0x04 0x10 0xde 0x04 0x0e 0xe8    ........
    0010   0x04 0x10 0xf2 0x04 0x86 0xfc 0x04 0x98    ........
    0018   0x06 0x14 0x10 0x10 0x14 0x9c 0x1a 0x14    ........
    0020   0xa0 0x9c 0x14 0x64 0xc4 0x14              ...d..
    decimal
             92   38   82   12    4   38   22    4
              4  212    4   16  222    4   14  232
              4   16  242    4  134  252    4  152
              6   20   16   16   20  156   26   20
            160  156   20  100  196   20
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2015-02-16T16:18:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.25,
 'duration': 0,
 'programmed': 1.1,
 'type': 'normal',
 'unabsorbed': 3.1}
```
    op hex (8)
    0000   0x01 0x01 0x2c 0x00 0x5a 0x00 0x7c 0x00    ..,.Z.|.
    decimal
              1    1   44    0   90    0  124    0
    datetime (2015-02-16T16:18:47)
    0000   0x2f 0x92 0x50 0x70 0x0f                   /.Pp.
    body (0)

#### RECORD 30 NoDelivery 2015-02-16T16:20:17 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-02-16T16:20:17)
    0000   0x11 0x94 0x50 0x50 0x0f                   ..PP.
    body (0)

#### RECORD 31 ClearAlarm 2015-02-16T16:21:06 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-02-16T16:21:06)
    0000   0x06 0x95 0x10 0x10 0x0f                   .....
    body (0)

#### RECORD 32 Rewind 2015-02-16T16:21:12 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-02-16T16:21:12)
    0000   0x0c 0x95 0x10 0x10 0x0f                   .....
    body (0)

#### RECORD 33 Prime 2015-02-16T16:23:25 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 8.1, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x51                   ....Q
    decimal
              3    0    0    0   81
    datetime (2015-02-16T16:23:25)
    0000   0x19 0x97 0x30 0x10 0x0f                   ..0..
    body (0)

#### RECORD 34 BasalProfileStart 2015-02-16T16:23:42 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-16T16:23:42)
    0000   0x2a 0x97 0x10 0x10 0x0f                   *....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 35 Bolus 2015-02-16T16:24:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 5.3}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xd4 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  212    0
    datetime (2015-02-16T16:24:41)
    0000   0x29 0x98 0x50 0x70 0x0f                   ).Pp.
    body (0)

#### RECORD 36 SensorAlert 2015-02-16T17:17:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-16T17:17:00)
    0000   0x00 0x91 0x31 0xb0 0x0f                   ..1..
    body (0)

#### RECORD 37 CalBGForPH 2015-02-16T17:24:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 63}
```
    op hex (2)
    0000   0x0a 0x3f                                  .?
    decimal
             10   63
    datetime (2015-02-16T17:24:20)
    0000   0x14 0x98 0x31 0x70 0x0f                   ..1p.
    body (0)

#### RECORD 38 BGReceived 2015-02-16T17:24:20 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2015-02-16T17:24:20)
    0000   0x14 0x98 0xf1 0x70 0x0f                   ...p.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 39 SensorAlert 2015-02-16T17:34:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 190}
```
    op hex (3)
    0000   0x0b 0x65 0xbe                             .e.
    decimal
             11  101  190
    datetime (2015-02-16T17:34:08)
    0000   0x08 0xa2 0x31 0xb0 0x0f                   ..1..
    body (0)

#### RECORD 40 SensorAlert 2015-02-16T17:39:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-16T17:39:30)
    0000   0x1e 0xa7 0x31 0xb0 0x0f                   ..1..
    body (0)

#### RECORD 41 SensorAlert 2015-02-16T17:39:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 106, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2015-02-16T17:39:30)
    0000   0x1e 0xa7 0x31 0xb0 0x0f                   ..1..
    body (0)

#### RECORD 42 CalBGForPH 2015-02-16T17:42:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 65}
```
    op hex (2)
    0000   0x0a 0x41                                  .A
    decimal
             10   65
    datetime (2015-02-16T17:42:26)
    0000   0x1a 0xaa 0x31 0x70 0x0f                   ..1p.
    body (0)

#### RECORD 43 BGReceived 2015-02-16T17:42:26 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2015-02-16T17:42:26)
    0000   0x1a 0xaa 0x31 0x70 0x0f                   ..1p.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 44 SensorAlert 2015-02-16T18:48:51 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-16T18:48:51)
    0000   0x33 0xb0 0x32 0xb0 0x0f                   3.2..
    body (0)

#### RECORD 45 Bolus 2015-02-16T18:49:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x5c 0x00    ..d.d.\.
    decimal
              1    0  100    0  100    0   92    0
    datetime (2015-02-16T18:49:08)
    0000   0x08 0xb1 0x52 0x70 0x0f                   ..Rp.
    body (0)

#### RECORD 46 SensorAlert 2015-02-16T18:54:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 193}
```
    op hex (3)
    0000   0x0b 0x65 0xc1                             .e.
    decimal
             11  101  193
    datetime (2015-02-16T18:54:08)
    0000   0x08 0xb6 0x32 0xb0 0x0f                   ..2..
    body (0)

#### RECORD 47 SensorAlert 2015-02-16T20:25:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 135}
```
    op hex (3)
    0000   0x0b 0x65 0x87                             .e.
    decimal
             11  101  135
    datetime (2015-02-16T20:25:25)
    0000   0x19 0x99 0x34 0xb0 0x8f                   ..4..
    body (0)

#### RECORD 48 BolusWizard 2015-02-16T20:25:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.9,
 'carb_input': 50,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 1.9,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-16T20:25:42)
    0000   0x2a 0x99 0x14 0x70 0x0f                   *..p.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    2P.<(Z..
    0008   0x4c 0x00 0x00 0x00 0x01 0x4c 0x78         L....Lx
    decimal
             50   80    0   60   40   90    0    1
             76    0    0    0    1   76  120

#### RECORD 49 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 99, 'amount': 2.5, 'curve': 4},
 {'age': 239, 'amount': 1.0, 'curve': 4},
 {'age': 249, 'amount': 4.25, 'curve': 4},
 {'age': 3, 'amount': 2.05, 'curve': 20},
 {'age': 13, 'amount': 0.95, 'curve': 20},
 {'age': 203, 'amount': 0.1, 'curve': 20},
 {'age': 213, 'amount': 0.4, 'curve': 20},
 {'age': 223, 'amount': 0.35, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x64 0x63 0x04 0x28 0xef 0x04    \.dc.(..
    0008   0xaa 0xf9 0x04 0x52 0x03 0x14 0x26 0x0d    ...R..&.
    0010   0x14 0x04 0xcb 0x14 0x10 0xd5 0x14 0x0e    ........
    0018   0xdf 0x14                                  ..
    decimal
             92   26  100   99    4   40  239    4
            170  249    4   82    3   20   38   13
             20    4  203   20   16  213   20   14
            223   20
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2015-02-16T20:25:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9,
 'duration': 0,
 'programmed': 1.9,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x01 0x4c 0x01 0x4c 0x00 0x40 0x00    ..L.L.@.
    decimal
              1    1   76    1   76    0   64    0
    datetime (2015-02-16T20:25:43)
    0000   0x2b 0x99 0x54 0x70 0x0f                   +.Tp.
    body (0)

#### RECORD 51 BolusWizard 2015-02-16T20:54:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-16T20:54:50)
    0000   0x32 0xb6 0x14 0x70 0x0f                   2..p.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    <P.<(Z..
    0008   0x90 0x00 0x00 0x00 0x01 0x90 0x78         ......x
    decimal
             60   80    0   60   40   90    0    1
            144    0    0    0    1  144  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 28, 'amount': 1.0, 'curve': 5},
 {'age': 38, 'amount': 0.9, 'curve': 4},
 {'age': 128, 'amount': 2.5, 'curve': 4},
 {'age': 12, 'amount': 1.0, 'curve': 20},
 {'age': 22, 'amount': 4.25, 'curve': 20},
 {'age': 32, 'amount': 2.05, 'curve': 20},
 {'age': 42, 'amount': 0.95, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x28 0x1c 0x05 0x24 0x26 0x04    \.(..$&.
    0008   0x64 0x80 0x04 0x28 0x0c 0x14 0xaa 0x16    d..(....
    0010   0x14 0x52 0x20 0x14 0x26 0x2a 0x14         .R .&*.
    decimal
             92   23   40   28    5   36   38    4
            100  128    4   40   12   20  170   22
             20   82   32   20   38   42   20
    datetime (unknown)

    body (0)

#### RECORD 53 BolusWizard 2015-02-16T20:55:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.6,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-16T20:55:05)
    0000   0x05 0xb7 0x14 0x70 0x0f                   ...p.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    <P.<(Z..
    0008   0x90 0x00 0x00 0x00 0x01 0x90 0x78         ......x
    decimal
             60   80    0   60   40   90    0    1
            144    0    0    0    1  144  120

#### RECORD 54 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 1.0, 'curve': 5},
 {'age': 39, 'amount': 0.9, 'curve': 4},
 {'age': 129, 'amount': 2.5, 'curve': 4},
 {'age': 13, 'amount': 1.0, 'curve': 20},
 {'age': 23, 'amount': 4.25, 'curve': 20},
 {'age': 33, 'amount': 2.05, 'curve': 20},
 {'age': 43, 'amount': 0.95, 'curve': 20}]
```
    op hex (23)
    0000   0x5c 0x17 0x28 0x1d 0x05 0x24 0x27 0x04    \.(..$'.
    0008   0x64 0x81 0x04 0x28 0x0d 0x14 0xaa 0x17    d..(....
    0010   0x14 0x52 0x21 0x14 0x26 0x2b 0x14         .R!.&+.
    decimal
             92   23   40   29    5   36   39    4
            100  129    4   40   13   20  170   23
             20   82   33   20   38   43   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2015-02-16T20:59:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 180,
 'programmed': 4.0,
 'type': 'square',
 'unabsorbed': 2.6}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x01 0x68 0x06    ......h.
    decimal
              1    0  160    0  160    1  104    6
    datetime (2015-02-16T20:59:07)
    0000   0x07 0xbb 0xb4 0x70 0x0f                   ...p.
    body (0)

#### RECORD 56 Bolus 2015-02-16T20:55:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 2.6}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x01 0x68 0x00    ......h.
    decimal
              1    0  240    0  240    1  104    0
    datetime (2015-02-16T20:55:05)
    0000   0x05 0xb7 0x94 0x70 0x0f                   ...p.
    body (0)

#### RECORD 57 BolusWizard 2015-02-16T21:31:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.0,
 'carb_input': 24,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-16T21:31:45)
    0000   0x2d 0x9f 0x15 0x70 0x0f                   -..p.
    body (15)
    hex
    0000   0x18 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0xa0 0x00 0x00 0x00 0x00 0xa0 0x78         ......x
    decimal
             24   80    0   60   40   90    0    0
            160    0    0    0    0  160  120

#### RECORD 58 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 0.1, 'curve': 4},
 {'age': 15, 'amount': 0.25, 'curve': 4},
 {'age': 25, 'amount': 0.2, 'curve': 4},
 {'age': 35, 'amount': 4.75, 'curve': 4},
 {'age': 45, 'amount': 1.4, 'curve': 4},
 {'age': 65, 'amount': 1.0, 'curve': 5},
 {'age': 75, 'amount': 0.9, 'curve': 4},
 {'age': 165, 'amount': 2.5, 'curve': 4},
 {'age': 49, 'amount': 1.0, 'curve': 20},
 {'age': 59, 'amount': 4.25, 'curve': 20},
 {'age': 69, 'amount': 2.05, 'curve': 20},
 {'age': 79, 'amount': 0.95, 'curve': 20}]
```
    op hex (38)
    0000   0x5c 0x26 0x04 0x05 0x04 0x0a 0x0f 0x04    \&......
    0008   0x08 0x19 0x04 0xbe 0x23 0x04 0x38 0x2d    ....#.8-
    0010   0x04 0x28 0x41 0x05 0x24 0x4b 0x04 0x64    .(A.$K.d
    0018   0xa5 0x04 0x28 0x31 0x14 0xaa 0x3b 0x14    ..(1..;.
    0020   0x52 0x45 0x14 0x26 0x4f 0x14              RE.&O.
    decimal
             92   38    4    5    4   10   15    4
              8   25    4  190   35    4   56   45
              4   40   65    5   36   75    4  100
            165    4   40   49   20  170   59   20
             82   69   20   38   79   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2015-02-16T21:31:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x02 0x18 0x00    ........
    decimal
              1    0  160    0  160    2   24    0
    datetime (2015-02-16T21:31:45)
    0000   0x2d 0x9f 0x55 0x70 0x0f                   -.Up.
    body (0)

#### RECORD 60 SensorAlert 2015-02-16T21:55:06 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 38}
```
    op hex (3)
    0000   0x0b 0x65 0x26                             .e&
    decimal
             11  101   38
    datetime (2015-02-16T21:55:06)
    0000   0x06 0xb7 0x35 0xb0 0x8f                   ..5..
    body (0)

#### RECORD 61 BasalProfileStart 2015-02-16T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-16T22:00:00)
    0000   0x00 0x80 0x16 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 62 CalBGForPH 2015-02-16T23:18:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2015-02-16T23:18:42)
    0000   0x2a 0x92 0x37 0x70 0x0f                   *.7p.
    body (0)

#### RECORD 63 BGReceived 2015-02-16T23:18:42 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2015-02-16T23:18:42)
    0000   0x2a 0x92 0x77 0x70 0x0f                   *.wp.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 64 SensorAlert 2015-02-16T23:24:57 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-16T23:24:57)
    0000   0x39 0x98 0x37 0xb0 0x0f                   9.7..
    body (0)

#### RECORD 65 BasalProfileStart 2015-02-17T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-17T00:00:00)
    0000   0x00 0x80 0x00 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 66 MResultTotals 2015-02-17T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0c 0x63                   ....c
    decimal
              7    0    0   12   99
    datetime (2015-02-17T00:00:00)
    0000   0x30 0x0f                                  0.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 67 Sara6E 2015-02-17T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-17T00:00:00)
    0000   0x30 0x0f                                  0.
    body (49)
    hex
    0000   0x05 0x00 0x9f 0x3f 0xf0 0x06 0x00 0x00    ...?....
    0008   0x0c 0x63 0x03 0x01 0x18 0x09 0x62 0x4c    .c....bL
    0010   0x01 0x42 0x05 0x6e 0x00 0x64 0x00 0xe8    .B.n.d..
    0018   0x02 0xa8 0x06 0x01 0x01 0x06 0x00 0xf5    ........
    0020   0x4f 0x15 0x00 0x88 0x50 0x02 0x00 0x00    O...P...
    0028   0x00 0x00 0x08 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  159   63  240    6    0    0
             12   99    3    1   24    9   98   76
              1   66    5  110    0  100    0  232
              2  168    6    1    1    6    0  245
             79   21    0  136   80    2    0    0
              0    0    8    0    0    0    0    0
              0

#### RECORD 68 BasalProfileStart 2015-02-17T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-17T04:00:00)
    0000   0x00 0x80 0x04 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 69 SensorAlert 2015-02-17T04:14:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-17T04:14:07)
    0000   0x07 0x8e 0x24 0xb1 0x0f                   ..$..
    body (0)

#### RECORD 70 BolusWizard 2015-02-17T04:29:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.0,
 'carb_input': 30,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 3.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-17T04:29:52)
    0000   0x34 0x9d 0x04 0x71 0x0f                   4..q.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    .P.d(Z..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x78         x....xx
    decimal
             30   80    0  100   40   90    0    0
            120    0    0    0    0  120  120

`end analysis/736868/logs/ReadHistoryData-page-27.data: 71 records`
