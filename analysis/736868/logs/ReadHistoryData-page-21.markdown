## START analysis/736868/logs/ReadHistoryData-page-21.data
#### RECORD 0 Sara6E 2015-02-24T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-24T00:00:00)
    0000   0x37 0x0f                                  7.
    body (49)
    hex
    0000   0x05 0x10 0xeb 0x91 0x63 0x03 0x00 0x00    ....c...
    0008   0x0a 0xf7 0x03 0x25 0x1d 0x07 0xd2 0x47    ...%...G
    0010   0x00 0xb4 0x03 0xee 0x00 0xd8 0x00 0x00    ........
    0018   0x03 0x0c 0x04 0x01 0x00 0x06 0x00 0xdf    ........
    0020   0x46 0x1e 0x00 0x91 0x48 0x02 0x00 0x00    F...H...
    0028   0x00 0x00 0x07 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  235  145   99    3    0    0
             10  247    3   37   29    7  210   71
              0  180    3  238    0  216    0    0
              3   12    4    1    0    6    0  223
             70   30    0  145   72    2    0    0
              0    0    7    0    0    0    0    0
              0

#### RECORD 1 LowReservoir 2015-02-24T01:28:20 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-02-24T01:28:20)
    0000   0x14 0x9c 0x01 0x18 0x0f                   .....
    body (0)

#### RECORD 2 SensorAlert 2015-02-24T01:43:18 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-24T01:43:18)
    0000   0x12 0xab 0x21 0xb8 0x0f                   ..!..
    body (0)

#### RECORD 3 SensorAlert 2015-02-24T01:47:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-24T01:47:01)
    0000   0x01 0xaf 0x21 0xb8 0x0f                   ..!..
    body (0)

#### RECORD 4 CalBGForPH 2015-02-24T03:51:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 314}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2015-02-24T03:51:36)
    0000   0x24 0xb3 0x23 0x78 0x8f                   $.#x.
    body (0)

#### RECORD 5 BGReceived 2015-02-24T03:51:36 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x27                                  ?'
    decimal
             63   39
    datetime (2015-02-24T03:51:36)
    0000   0x24 0xb3 0x43 0x78 0x0f                   $.Cx.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 6 BolusWizard 2015-02-24T03:51:45 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 314,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.8,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': -1.6,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x3a                                  [:
    decimal
             91   58
    datetime (2015-02-24T03:51:45)
    0000   0x2d 0xb3 0x03 0x18 0x0f                   -....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xc0 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0xc0 0x78         ......x
    decimal
              0   81    0  100   40   90  192    0
              0    0    0    0    0  192  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[56], body[0] op[0x5c]
###### DECODED
```python
[{'age': 9, 'amount': 0.05, 'curve': 20},
 {'age': 19, 'amount': 0.45, 'curve': 20},
 {'age': 29, 'amount': 0.45, 'curve': 20},
 {'age': 39, 'amount': 3.85, 'curve': 20},
 {'age': 49, 'amount': 0.4, 'curve': 20},
 {'age': 59, 'amount': 0.45, 'curve': 20},
 {'age': 69, 'amount': 0.45, 'curve': 20},
 {'age': 79, 'amount': 0.45, 'curve': 20},
 {'age': 89, 'amount': 0.45, 'curve': 20},
 {'age': 99, 'amount': 0.4, 'curve': 20},
 {'age': 109, 'amount': 0.45, 'curve': 20},
 {'age': 119, 'amount': 0.45, 'curve': 20},
 {'age': 129, 'amount': 0.45, 'curve': 20},
 {'age': 139, 'amount': 0.45, 'curve': 20},
 {'age': 149, 'amount': 0.4, 'curve': 20},
 {'age': 159, 'amount': 0.45, 'curve': 20},
 {'age': 169, 'amount': 0.05, 'curve': 20},
 {'age': 209, 'amount': 2.5, 'curve': 20}]
```
    op hex (56)
    0000   0x5c 0x38 0x02 0x09 0x14 0x12 0x13 0x14    \8......
    0008   0x12 0x1d 0x14 0x9a 0x27 0x14 0x10 0x31    ....'..1
    0010   0x14 0x12 0x3b 0x14 0x12 0x45 0x14 0x12    ..;..E..
    0018   0x4f 0x14 0x12 0x59 0x14 0x10 0x63 0x14    O..Y..c.
    0020   0x12 0x6d 0x14 0x12 0x77 0x14 0x12 0x81    .m..w...
    0028   0x14 0x12 0x8b 0x14 0x10 0x95 0x14 0x12    ........
    0030   0x9f 0x14 0x02 0xa9 0x14 0x64 0xd1 0x14    .....d..
    decimal
             92   56    2    9   20   18   19   20
             18   29   20  154   39   20   16   49
             20   18   59   20   18   69   20   18
             79   20   18   89   20   16   99   20
             18  109   20   18  119   20   18  129
             20   18  139   20   16  149   20   18
            159   20    2  169   20  100  209   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2015-02-24T03:51:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.8,
 'duration': 0,
 'programmed': 4.8,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xc0 0x00 0xc0 0x00 0x00 0x00    ........
    decimal
              1    0  192    0  192    0    0    0
    datetime (2015-02-24T03:51:45)
    0000   0x2d 0xb3 0x43 0x18 0x0f                   -.C..
    body (0)

#### RECORD 9 BasalProfileStart 2015-02-24T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-24T04:00:00)
    0000   0x00 0x80 0x04 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 10 SensorAlert 2015-02-24T04:47:42 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 48}
```
    op hex (3)
    0000   0x0b 0x65 0x30                             .e0
    decimal
             11  101   48
    datetime (2015-02-24T04:47:42)
    0000   0x2a 0xaf 0x24 0xb8 0x8f                   *.$..
    body (0)

#### RECORD 11 SensorAlert 2015-02-24T06:18:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 218}
```
    op hex (3)
    0000   0x0b 0x65 0xda                             .e.
    decimal
             11  101  218
    datetime (2015-02-24T06:18:30)
    0000   0x1e 0x92 0x26 0xb8 0x0f                   ..&..
    body (0)

#### RECORD 12 CalBGForPH 2015-02-24T06:50:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2015-02-24T06:50:14)
    0000   0x0e 0xb2 0x26 0x78 0x0f                   ..&x.
    body (0)

#### RECORD 13 BGReceived 2015-02-24T06:50:14 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-02-24T06:50:14)
    0000   0x0e 0xb2 0x86 0x78 0x0f                   ...x.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 14 BolusWizard 2015-02-24T06:50:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 188,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 1.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.8}
```
    op hex (2)
    0000   0x5b 0xbc                                  [.
    decimal
             91  188
    datetime (2015-02-24T06:50:18)
    0000   0x12 0xb2 0x06 0x18 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x44 0x00    .P.d(ZD.
    0008   0x00 0x00 0x00 0x20 0x00 0x24 0x78         ... .$x
    decimal
              0   80    0  100   40   90   68    0
              0    0    0   32    0   36  120

#### RECORD 15 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 184, 'amount': 4.8, 'curve': 4},
 {'age': 188, 'amount': 0.05, 'curve': 20},
 {'age': 198, 'amount': 0.45, 'curve': 20},
 {'age': 208, 'amount': 0.45, 'curve': 20},
 {'age': 218, 'amount': 3.85, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0xc0 0xb8 0x04 0x02 0xbc 0x14    \.......
    0008   0x12 0xc6 0x14 0x12 0xd0 0x14 0x9a 0xda    ........
    0010   0x14                                       .
    decimal
             92   17  192  184    4    2  188   20
             18  198   20   18  208   20  154  218
             20
    datetime (unknown)

    body (0)

#### RECORD 16 LowReservoir 2015-02-24T06:50:37 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-02-24T06:50:37)
    0000   0x25 0xb2 0x06 0x18 0x0f                   %....
    body (0)

#### RECORD 17 Bolus 2015-02-24T06:50:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9,
 'duration': 0,
 'programmed': 0.9,
 'type': 'normal',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x20 0x00    ..$.$. .
    decimal
              1    0   36    0   36    0   32    0
    datetime (2015-02-24T06:50:18)
    0000   0x12 0xb2 0x46 0x18 0x0f                   ..F..
    body (0)

#### RECORD 18 BasalProfileStart 2015-02-24T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-24T07:00:00)
    0000   0x00 0x80 0x07 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 19 ChangeTimeDisplay 2015-02-24T07:12:23 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2015-02-24T07:12:23)
    0000   0x17 0x8c 0x07 0x18 0x0f                   .....
    body (0)

#### RECORD 20 ChangeTime 2015-02-24T07:12:29 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2015-02-24T07:12:29)
    0000   0x1d 0x8c 0x07 0x18 0x0f                   .....
    body (0)

#### RECORD 21 NewTimeSet 2015-02-24T07:15:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2015-02-24T07:15:00)
    0000   0x00 0x8f 0x07 0x18 0x0f                   .....
    body (0)

#### RECORD 22 BolusWizard 2015-02-24T07:31:25 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.1,
 'carb_input': 65,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 0.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-24T07:31:25)
    0000   0x19 0x9f 0x07 0x78 0x0f                   ...x.
    body (15)
    hex
    0000   0x41 0x50 0x00 0x64 0x28 0x5a 0x00 0x01    AP.d(Z..
    0008   0x04 0x00 0x00 0x00 0x01 0x04 0x78         ......x
    decimal
             65   80    0  100   40   90    0    1
              4    0    0    0    1    4  120

#### RECORD 23 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 42, 'amount': 0.9, 'curve': 4},
 {'age': 222, 'amount': 4.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0x2a 0x04 0xc0 0xde 0x04    \.$*....
    decimal
             92    8   36   42    4  192  222    4
    datetime (unknown)

    body (0)

#### RECORD 24 Bolus 2015-02-24T07:31:25 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.1,
 'duration': 0,
 'programmed': 0.1,
 'type': 'normal',
 'unabsorbed': 1.2}
```
    op hex (8)
    0000   0x01 0x01 0x04 0x01 0x04 0x00 0x30 0x00    ......0.
    decimal
              1    1    4    1    4    0   48    0
    datetime (2015-02-24T07:31:25)
    0000   0x19 0x9f 0x47 0x78 0x0f                   ..Gx.
    body (0)

#### RECORD 25 PumpSuspend 2015-02-24T07:36:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-24T07:36:53)
    0000   0x35 0xa4 0x07 0x18 0x0f                   5....
    body (0)

#### RECORD 26 BasalProfileStart 2015-02-24T07:54:58 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-24T07:54:58)
    0000   0x3a 0xb6 0x07 0x18 0x0f                   :....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 27 PumpResume 2015-02-24T07:54:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-24T07:54:58)
    0000   0x3a 0xb6 0x07 0x18 0x0f                   :....
    body (0)

#### RECORD 28 SensorAlert 2015-02-24T07:55:40 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 209}
```
    op hex (3)
    0000   0x0b 0x65 0xd1                             .e.
    decimal
             11  101  209
    datetime (2015-02-24T07:55:40)
    0000   0x28 0xb7 0x27 0xb8 0x0f                   (.'..
    body (0)

#### RECORD 29 SensorAlert 2015-02-24T09:45:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 114, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-24T09:45:49)
    0000   0x31 0xad 0x29 0xb8 0x0f                   1.)..
    body (0)

#### RECORD 30 SensorAlert 2015-02-24T09:55:40 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-24T09:55:40)
    0000   0x28 0xb7 0x29 0xb8 0x0f                   (.)..
    body (0)

#### RECORD 31 BasalProfileStart 2015-02-24T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-24T10:00:00)
    0000   0x00 0x80 0x0a 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 32 SensorAlert 2015-02-24T11:24:51 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 56}
```
    op hex (3)
    0000   0x0b 0x65 0x38                             .e8
    decimal
             11  101   56
    datetime (2015-02-24T11:24:51)
    0000   0x33 0x98 0x2b 0xb8 0x8f                   3.+..
    body (0)

#### RECORD 33 CalBGForPH 2015-02-24T11:29:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 303}
```
    op hex (2)
    0000   0x0a 0x2f                                  ./
    decimal
             10   47
    datetime (2015-02-24T11:29:25)
    0000   0x19 0x9d 0x2b 0x78 0x8f                   ..+x.
    body (0)

#### RECORD 34 BGReceived 2015-02-24T11:29:25 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x25                                  ?%
    decimal
             63   37
    datetime (2015-02-24T11:29:25)
    0000   0x19 0x9d 0xeb 0x78 0x0f                   ...x.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 35 BolusWizard 2015-02-24T11:29:37 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 303,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.1,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': -1.9,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0x2f                                  [/
    decimal
             91   47
    datetime (2015-02-24T11:29:37)
    0000   0x25 0x9d 0x0b 0x18 0x0f                   %....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xb4 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x10 0x00 0xa4 0x78         ......x
    decimal
              0   81    0  100   40   90  180    0
              0    0    0   16    0  164  120

#### RECORD 36 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 240, 'amount': 0.1, 'curve': 5},
 {'age': 24, 'amount': 0.9, 'curve': 20},
 {'age': 204, 'amount': 4.8, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x04 0xf0 0x05 0x24 0x18 0x14    \....$..
    0008   0xc0 0xcc 0x14                             ...
    decimal
             92   11    4  240    5   36   24   20
            192  204   20
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2015-02-24T11:29:37 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1,
 'duration': 0,
 'programmed': 4.1,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x10 0x00    ........
    decimal
              1    0  164    0  164    0   16    0
    datetime (2015-02-24T11:29:37)
    0000   0x25 0x9d 0x4b 0x18 0x0f                   %.K..
    body (0)

#### RECORD 38 BasalProfileStart 2015-02-24T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-24T12:00:00)
    0000   0x00 0x80 0x0c 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 39 BolusWizard 2015-02-24T12:41:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.8,
 'carb_input': 15,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 1.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-24T12:41:51)
    0000   0x33 0xa9 0x0c 0x78 0x0f                   3..x.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x78         H....Hx
    decimal
             15   80    0   80   40   90    0    0
             72    0    0    0    0   72  120

#### RECORD 40 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 4.1, 'curve': 4},
 {'age': 56, 'amount': 0.1, 'curve': 21},
 {'age': 96, 'amount': 0.9, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xa4 0x48 0x04 0x04 0x38 0x15    \..H..8.
    0008   0x24 0x60 0x14                             $`.
    decimal
             92   11  164   72    4    4   56   21
             36   96   20
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2015-02-24T12:41:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 0,
 'programmed': 1.8,
 'type': 'normal',
 'unabsorbed': 3.1}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x7c 0x00    ..H.H.|.
    decimal
              1    0   72    0   72    0  124    0
    datetime (2015-02-24T12:41:51)
    0000   0x33 0xa9 0x4c 0x78 0x0f                   3.Lx.
    body (0)

#### RECORD 42 SensorAlert 2015-02-24T12:56:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 239}
```
    op hex (3)
    0000   0x0b 0x65 0xef                             .e.
    decimal
             11  101  239
    datetime (2015-02-24T12:56:08)
    0000   0x08 0xb8 0x2c 0xb8 0x0f                   ..,..
    body (0)

#### RECORD 43 BolusWizard 2015-02-24T12:59:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.2,
 'carb_input': 34,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.2,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-24T12:59:56)
    0000   0x38 0xbb 0x0c 0x78 0x0f                   8..x.
    body (15)
    hex
    0000   0x22 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    "P.P(Z..
    0008   0xa8 0x00 0x00 0x00 0x00 0xa8 0x78         ......x
    decimal
             34   80    0   80   40   90    0    0
            168    0    0    0    0  168  120

#### RECORD 44 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 1.8, 'curve': 4},
 {'age': 90, 'amount': 4.1, 'curve': 4},
 {'age': 74, 'amount': 0.1, 'curve': 21},
 {'age': 114, 'amount': 0.9, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x14 0x04 0xa4 0x5a 0x04    \.H...Z.
    0008   0x04 0x4a 0x15 0x24 0x72 0x14              .J.$r.
    decimal
             92   14   72   20    4  164   90    4
              4   74   21   36  114   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2015-02-24T12:59:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.8,
 'duration': 0,
 'programmed': 4.2,
 'type': 'normal',
 'unabsorbed': 4.5}
```
    op hex (8)
    0000   0x01 0x00 0xa8 0x00 0x98 0x00 0xb4 0x00    ........
    decimal
              1    0  168    0  152    0  180    0
    datetime (2015-02-24T12:59:56)
    0000   0x38 0xbb 0x4c 0x78 0x0f                   8.Lx.
    body (0)

#### RECORD 46 NoDelivery 2015-02-24T13:02:32 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-02-24T13:02:32)
    0000   0x20 0x82 0x4d 0x58 0x0f                    .MX.
    body (0)

#### RECORD 47 ClearAlarm 2015-02-24T13:02:40 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-02-24T13:02:40)
    0000   0x28 0x82 0x0d 0x18 0x0f                   (....
    body (0)

#### RECORD 48 BasalProfileStart 2015-02-24T13:02:43 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-24T13:02:43)
    0000   0x2b 0x82 0x0d 0x18 0x0f                   +....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 49 NoDelivery 2015-02-24T13:08:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-02-24T13:08:00)
    0000   0x00 0x88 0x4d 0x58 0x0f                   ..MX.
    body (0)

#### RECORD 50 ClearAlarm 2015-02-24T13:11:20 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-02-24T13:11:20)
    0000   0x14 0x8b 0x0d 0x18 0x0f                   .....
    body (0)

#### RECORD 51 SensorAlert 2015-02-24T14:25:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 228}
```
    op hex (3)
    0000   0x0b 0x65 0xe4                             .e.
    decimal
             11  101  228
    datetime (2015-02-24T14:25:49)
    0000   0x31 0x99 0x2e 0xb8 0x0f                   1....
    body (0)

#### RECORD 52 Rewind 2015-02-24T15:02:31 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-02-24T15:02:31)
    0000   0x1f 0x82 0x0f 0x18 0x0f                   .....
    body (0)

#### RECORD 53 Prime 2015-02-24T15:07:00 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 7.2, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x48                   ....H
    decimal
              3    0    0    0   72
    datetime (2015-02-24T15:07:00)
    0000   0x00 0x87 0x2f 0x18 0x0f                   ../..
    body (0)

#### RECORD 54 BasalProfileStart 2015-02-24T15:08:43 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-24T15:08:43)
    0000   0x2b 0x88 0x0f 0x18 0x0f                   +....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 55 Prime 2015-02-24T15:08:29 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-02-24T15:08:29)
    0000   0x1d 0x88 0x0f 0x18 0x0f                   .....
    body (0)

#### RECORD 56 BolusWizard 2015-02-24T15:09:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 36,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-24T15:09:40)
    0000   0x28 0x89 0x0f 0x78 0x0f                   (..x.
    body (15)
    hex
    0000   0x24 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    $P.P(Z..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x78         ......x
    decimal
             36   80    0   80   40   90    0    0
            180    0    0    0    0  180  120

#### RECORD 57 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 130, 'amount': 3.8, 'curve': 4},
 {'age': 150, 'amount': 1.8, 'curve': 4},
 {'age': 220, 'amount': 4.1, 'curve': 4},
 {'age': 204, 'amount': 0.1, 'curve': 21}]
```
    op hex (14)
    0000   0x5c 0x0e 0x98 0x82 0x04 0x48 0x96 0x04    \....H..
    0008   0xa4 0xdc 0x04 0x04 0xcc 0x15              ......
    decimal
             92   14  152  130    4   72  150    4
            164  220    4    4  204   21
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2015-02-24T15:09:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x60 0x00    ......`.
    decimal
              1    0  180    0  180    0   96    0
    datetime (2015-02-24T15:09:40)
    0000   0x28 0x89 0x4f 0x78 0x0f                   (.Ox.
    body (0)

#### RECORD 59 SensorAlert 2015-02-24T15:55:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-02-24T15:55:39)
    0000   0x27 0xb7 0x2f 0xb8 0x0f                   './..
    body (0)

#### RECORD 60 SensorAlert 2015-02-24T17:24:50 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 231}
```
    op hex (3)
    0000   0x0b 0x65 0xe7                             .e.
    decimal
             11  101  231
    datetime (2015-02-24T17:24:50)
    0000   0x32 0x98 0x31 0xb8 0x0f                   2.1..
    body (0)

#### RECORD 61 Bolus 2015-02-24T17:25:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 1.7}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x44 0x00    ......D.
    decimal
              1    0  140    0  140    0   68    0
    datetime (2015-02-24T17:25:13)
    0000   0x0d 0x99 0x51 0x78 0x0f                   ..Qx.
    body (0)

#### RECORD 62 BolusWizard 2015-02-24T18:15:28 head[2], body[15] op[0x5b]
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
    datetime (2015-02-24T18:15:28)
    0000   0x1c 0x8f 0x12 0x78 0x0f                   ...x.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    <P.<(Z..
    0008   0x90 0x00 0x00 0x00 0x01 0x90 0x78         ......x
    decimal
             60   80    0   60   40   90    0    1
            144    0    0    0    1  144  120

#### RECORD 63 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 56, 'amount': 3.5, 'curve': 4},
 {'age': 186, 'amount': 4.5, 'curve': 4},
 {'age': 60, 'amount': 3.8, 'curve': 20},
 {'age': 80, 'amount': 1.8, 'curve': 20},
 {'age': 150, 'amount': 4.1, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x8c 0x38 0x04 0xb4 0xba 0x04    \..8....
    0008   0x98 0x3c 0x14 0x48 0x50 0x14 0xa4 0x96    .<.HP...
    0010   0x14                                       .
    decimal
             92   17  140   56    4  180  186    4
            152   60   20   72   80   20  164  150
             20
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2015-02-24T18:19:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 240,
 'programmed': 4.0,
 'type': 'square',
 'unabsorbed': 3.7}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x94 0x08    ........
    decimal
              1    0  160    0  160    0  148    8
    datetime (2015-02-24T18:19:30)
    0000   0x1e 0x93 0xb2 0x78 0x0f                   ...x.
    body (0)

#### RECORD 65 Bolus 2015-02-24T18:15:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 0,
 'programmed': 6.0,
 'type': 'normal',
 'unabsorbed': 3.7}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0x94 0x00    ........
    decimal
              1    0  240    0  240    0  148    0
    datetime (2015-02-24T18:15:28)
    0000   0x1c 0x8f 0x92 0x78 0x0f                   ...x.
    body (0)

#### RECORD 66 SensorAlert 2015-02-24T18:56:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 218}
```
    op hex (3)
    0000   0x0b 0x65 0xda                             .e.
    decimal
             11  101  218
    datetime (2015-02-24T18:56:07)
    0000   0x07 0xb8 0x32 0xb8 0x0f                   ..2..
    body (0)

#### RECORD 67 Bolus 2015-02-24T20:11:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5,
 'duration': 0,
 'programmed': 5.5,
 'type': 'normal',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0xdc 0x00 0xdc 0x00 0xc8 0x00    ........
    decimal
              1    0  220    0  220    0  200    0
    datetime (2015-02-24T20:11:43)
    0000   0x2b 0x8b 0x54 0x78 0x0f                   +.Tx.
    body (0)

#### RECORD 68 Bolus 2015-02-24T20:54:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x01 0x50 0x00    ......P.
    decimal
              1    0  140    0  140    1   80    0
    datetime (2015-02-24T20:54:12)
    0000   0x0c 0xb6 0x54 0x78 0x0f                   ..Tx.
    body (0)

#### RECORD 69 BasalProfileStart 2015-02-24T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-24T22:00:00)
    0000   0x00 0x80 0x16 0x18 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 70 SensorAlert 2015-02-24T22:29:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-24T22:29:00)
    0000   0x00 0x9d 0x36 0xb8 0x0f                   ..6..
    body (0)

#### RECORD 71 SensorAlert 2015-02-24T23:29:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 104, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-24T23:29:00)
    0000   0x00 0x9d 0x37 0xb8 0x0f                   ..7..
    body (0)

#### RECORD 72 CalBGForPH 2015-02-24T23:31:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2015-02-24T23:31:41)
    0000   0x29 0x9f 0x37 0x78 0x0f                   ).7x.
    body (0)

#### RECORD 73 BGReceived 2015-02-24T23:31:41 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2015-02-24T23:31:41)
    0000   0x29 0x9f 0x57 0x78 0x0f                   ).Wx.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 74 Bolus 2015-02-24T23:32:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x60 0x00    ..d.d.`.
    decimal
              1    0  100    0  100    0   96    0
    datetime (2015-02-24T23:32:17)
    0000   0x11 0xa0 0x57 0x78 0x0f                   ..Wx.
    body (0)

#### RECORD 75 BasalProfileStart 2015-02-25T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-25T00:00:00)
    0000   0x00 0x80 0x00 0x19 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 76 MResultTotals 2015-02-25T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0xef                   .....
    decimal
              7    0    0   10  239
    datetime (2015-02-25T00:00:00)
    0000   0x38 0x0f                                  8.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 77 Sara6E 2015-02-25T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-25T00:00:00)
    0000   0x38 0x0f                                  8.
    body (49)
    hex
    0000   0x05 0x10 0xe0 0x5a 0x3a 0x04 0x00 0x00    ...Z:...
    0008   0x0a 0xef 0x02 0xe7 0x1b 0x08 0x08 0x49    .......I
    0010   0x00 0xd2 0x04 0x28 0x01 0x88 0x00 0x00    ...(....
    0018   0x02 0x58 0x05 0x03 0x00 0x04 0x00 0xd1    .X......
    0020   0x45 0x1f 0x00 0x1d 0x37 0x02 0x00 0x00    E...7...
    0028   0x00 0x00 0x0b 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  224   90   58    4    0    0
             10  239    2  231   27    8    8   73
              0  210    4   40    1  136    0    0
              2   88    5    3    0    4    0  209
             69   31    0   29   55    2    0    0
              0    0   11    1    0    0    0    0
              0

#### RECORD 78 SensorAlert 2015-02-25T00:50:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 78}
```
    op hex (3)
    0000   0x0b 0x66 0x4e                             .fN
    decimal
             11  102   78
    datetime (2015-02-25T00:50:12)
    0000   0x0c 0xb2 0x20 0xb9 0x0f                   .. ..
    body (0)

#### RECORD 79 SensorAlert 2015-02-25T00:56:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-25T00:56:07)
    0000   0x07 0xb8 0x20 0xb9 0x0f                   .. ..
    body (0)

#### RECORD 80 Bolus 2015-02-25T02:04:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.7}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x1c 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   28    0
    datetime (2015-02-25T02:04:50)
    0000   0x32 0x84 0x42 0x79 0x0f                   2.By.
    body (0)

#### RECORD 81 Base unknown head[2], body[0] op[0xe9]

    op hex (2)
    0000   0xe9 0x1b                                  ..
    decimal
            233   27
    datetime (unknown)

    body (0)

`end analysis/736868/logs/ReadHistoryData-page-21.data: 82 records`
