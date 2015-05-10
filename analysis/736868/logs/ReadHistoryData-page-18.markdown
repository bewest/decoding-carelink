## START ReadHistoryData-page-18.data
#### STOPPING DOUBLE NULLS @ 1018, found 4 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x1b 0x72                                  .r
##### DEBUG DECIMAL
             27  114
#### RECORD 0 BolusWizard 2015-02-27T13:52:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.7,
 'carb_input': 30,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-27T13:52:24)
    0000   0x18 0xb4 0x0d 0x7b 0x0f                   ...{.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0x94 0x00 0x00 0x00 0x00 0x94 0x78         ......x
    decimal
             30   80    0   80   40   90    0    0
            148    0    0    0    0  148  120

#### RECORD 1 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 6.0},
 {'age': 233, 'amount': 1.0},
 {'age': 283, 'amount': 1.5},
 {'age': 373, 'amount': 0.6}]
```
    op hex (14)
    0000   0x5c 0x0e 0xf0 0x21 0x04 0x28 0xe9 0x04    \..!.(..
    0008   0x3c 0x1b 0x14 0x18 0x75 0x15              <...u.
    decimal
             92   14  240   33    4   40  233    4
             60   27   20   24  117   21
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2015-02-27T13:52:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7,
 'duration': 0,
 'programmed': 3.7,
 'type': 'normal',
 'unabsorbed': 5.7}
```
    op hex (8)
    0000   0x01 0x00 0x94 0x00 0x94 0x00 0xe4 0x00    ........
    decimal
              1    0  148    0  148    0  228    0
    datetime (2015-02-27T13:52:24)
    0000   0x18 0xb4 0x4d 0x7b 0x0f                   ..M{.
    body (0)

#### RECORD 3 BolusWizard 2015-02-27T14:36:31 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 10.0,
 'carb_input': 80,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 10.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-27T14:36:31)
    0000   0x1f 0xa4 0x0e 0x7b 0x0f                   ...{.
    body (15)
    hex
    0000   0x50 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    PP.P(Z..
    0008   0x90 0x00 0x00 0x00 0x01 0x90 0x78         ......x
    decimal
             80   80    0   80   40   90    0    1
            144    0    0    0    1  144  120

#### RECORD 4 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 47, 'amount': 3.7},
 {'age': 77, 'amount': 6.0},
 {'age': 277, 'amount': 1.0},
 {'age': 327, 'amount': 1.5},
 {'age': 417, 'amount': 0.6}]
```
    op hex (17)
    0000   0x5c 0x11 0x94 0x2f 0x04 0xf0 0x4d 0x04    \../..M.
    0008   0x28 0x15 0x14 0x3c 0x47 0x14 0x18 0xa1    (..<G...
    0010   0x15                                       .
    decimal
             92   17  148   47    4  240   77    4
             40   21   20   60   71   20   24  161
             21
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2015-02-27T14:36:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6,
 'duration': 0,
 'programmed': 1.6,
 'type': 'normal',
 'unabsorbed': 1.3}
```
    op hex (8)
    0000   0x01 0x01 0x40 0x01 0x40 0x01 0x34 0x00    ..@.@.4.
    decimal
              1    1   64    1   64    1   52    0
    datetime (2015-02-27T14:36:31)
    0000   0x1f 0xa4 0x4e 0x7b 0x0f                   ..N{.
    body (0)

#### RECORD 6 BasalProfileStart 2015-02-27T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-27T15:00:00)
    0000   0x00 0x80 0x0f 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 7 BolusWizard 2015-02-27T16:59:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.5,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 7.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-27T16:59:41)
    0000   0x29 0xbb 0x10 0x7b 0x0f                   )..{.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 8 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 140, 'amount': 3.8},
 {'age': 150, 'amount': 4.2},
 {'age': 190, 'amount': 3.7},
 {'age': 220, 'amount': 6.0},
 {'age': 420, 'amount': 1.0},
 {'age': 470, 'amount': 1.5}]
```
    op hex (20)
    0000   0x5c 0x14 0x98 0x8c 0x04 0xa8 0x96 0x04    \.......
    0008   0x94 0xbe 0x04 0xf0 0xdc 0x04 0x28 0xa4    ......(.
    0010   0x14 0x3c 0xd6 0x14                        .<..
    decimal
             92   20  152  140    4  168  150    4
            148  190    4  240  220    4   40  164
             20   60  214   20
    datetime (unknown)

    body (0)

#### RECORD 9 Bolus 2015-02-27T17:02:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 150,
 'programmed': 3.5,
 'type': 'square',
 'unabsorbed': 3.6}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x90 0x05    ........
    decimal
              1    0  140    0  140    0  144    5
    datetime (2015-02-27T17:02:23)
    0000   0x17 0x82 0xb1 0x7b 0x0f                   ...{.
    body (0)

#### RECORD 10 Bolus 2015-02-27T16:59:41 head[8], body[0] op[0x01]
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
    datetime (2015-02-27T16:59:41)
    0000   0x29 0xbb 0x90 0x7b 0x0f                   )..{.
    body (0)

#### RECORD 11 CalBGForPH 2015-02-27T18:59:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2015-02-27T18:59:01)
    0000   0x01 0xbb 0x32 0x7b 0x0f                   ..2{.
    body (0)

#### RECORD 12 BGReceived 2015-02-27T18:59:01 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 92, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2015-02-27T18:59:01)
    0000   0x01 0xbb 0x92 0x7b 0x0f                   ...{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 13 SensorAlert 2015-02-27T21:01:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-27T21:01:00)
    0000   0x00 0x81 0x35 0xbb 0x0f                   ..5..
    body (0)

#### RECORD 14 SensorAlert 2015-02-27T21:15:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-27T21:15:37)
    0000   0x25 0x8f 0x35 0xbb 0x0f                   %.5..
    body (0)

#### RECORD 15 SensorAlert 2015-02-27T21:24:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-27T21:24:48)
    0000   0x30 0x98 0x35 0xbb 0x0f                   0.5..
    body (0)

#### RECORD 16 CalBGForPH 2015-02-27T21:56:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 148}
```
    op hex (2)
    0000   0x0a 0x94                                  ..
    decimal
             10  148
    datetime (2015-02-27T21:56:55)
    0000   0x37 0xb8 0x35 0x7b 0x0f                   7.5{.
    body (0)

#### RECORD 17 BGReceived 2015-02-27T21:56:55 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 148, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2015-02-27T21:56:55)
    0000   0x37 0xb8 0x95 0x7b 0x0f                   7..{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 18 BasalProfileStart 2015-02-27T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-27T22:00:00)
    0000   0x00 0x80 0x16 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 19 PumpSuspend 2015-02-27T22:13:00 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-27T22:13:00)
    0000   0x00 0x8d 0x16 0x1b 0x0f                   .....
    body (0)

#### RECORD 20 BasalProfileStart 2015-02-27T22:20:18 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-27T22:20:18)
    0000   0x12 0x94 0x16 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 21 PumpResume 2015-02-27T22:20:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-27T22:20:18)
    0000   0x12 0x94 0x16 0x1b 0x0f                   .....
    body (0)

#### RECORD 22 BasalProfileStart 2015-02-28T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-28T00:00:00)
    0000   0x00 0x80 0x00 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 23 MResultTotals 2015-02-28T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x82                   .....
    decimal
              7    0    0    8  130
    datetime (2015-02-28T00:00:00)
    0000   0x3b 0x0f                                  ;.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 24 Sara6E 2015-02-28T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-28T00:00:00)
    0000   0x3b 0x0f                                  ;.
    body (49)
    hex
    0000   0x05 0x00 0xa2 0x5c 0xf5 0x03 0x00 0x00    ...\....
    0008   0x08 0x82 0x03 0x16 0x24 0x05 0x6c 0x40    ....$.l@
    0010   0x00 0xf0 0x04 0x18 0x00 0x00 0x00 0x00    ........
    0018   0x01 0x54 0x04 0x00 0x00 0x03 0x00 0xa6    .T......
    0020   0x1e 0x43 0x03 0x1d 0x47 0x02 0x03 0x00    .C..G...
    0028   0x00 0x01 0x06 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  162   92  245    3    0    0
              8  130    3   22   36    5  108   64
              0  240    4   24    0    0    0    0
              1   84    4    0    0    3    0  166
             30   67    3   29   71    2    3    0
              0    1    6    1    0    0    0    0
              0

#### RECORD 25 CalBGForPH 2015-02-28T00:01:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 158}
```
    op hex (2)
    0000   0x0a 0x9e                                  ..
    decimal
             10  158
    datetime (2015-02-28T00:01:15)
    0000   0x0f 0x81 0x20 0x7c 0x0f                   .. |.
    body (0)

#### RECORD 26 BGReceived 2015-02-28T00:01:15 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 158, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2015-02-28T00:01:15)
    0000   0x0f 0x81 0xc0 0x7c 0x0f                   ...|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 27 CalBGForPH 2015-02-28T02:01:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 165}
```
    op hex (2)
    0000   0x0a 0xa5                                  ..
    decimal
             10  165
    datetime (2015-02-28T02:01:03)
    0000   0x03 0x81 0x22 0x7c 0x0f                   .."|.
    body (0)

#### RECORD 28 BGReceived 2015-02-28T02:01:03 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 165, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2015-02-28T02:01:03)
    0000   0x03 0x81 0xa2 0x7c 0x0f                   ...|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 29 BasalProfileStart 2015-02-28T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-28T04:00:00)
    0000   0x00 0x80 0x04 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 30 CalBGForPH 2015-02-28T04:01:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2015-02-28T04:01:17)
    0000   0x11 0x81 0x24 0x7c 0x0f                   ..$|.
    body (0)

#### RECORD 31 BGReceived 2015-02-28T04:01:17 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 154, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2015-02-28T04:01:17)
    0000   0x11 0x81 0x44 0x7c 0x0f                   ..D|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 32 CalBGForPH 2015-02-28T06:36:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2015-02-28T06:36:07)
    0000   0x07 0xa4 0x26 0x7c 0x0f                   ..&|.
    body (0)

#### RECORD 33 BGReceived 2015-02-28T06:36:07 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 109, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2015-02-28T06:36:07)
    0000   0x07 0xa4 0xa6 0x7c 0x0f                   ...|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 34 BolusWizard 2015-02-28T06:45:06 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 109,
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
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2015-02-28T06:45:06)
    0000   0x06 0xad 0x06 0x7c 0x0f                   ...|.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 35 Bolus 2015-02-28T06:46:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 60,
 'programmed': 2.5,
 'type': 'square',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x00 0x02    ..d.d...
    decimal
              1    0  100    0  100    0    0    2
    datetime (2015-02-28T06:46:46)
    0000   0x2e 0xae 0xa6 0x7c 0x0f                   ...|.
    body (0)

#### RECORD 36 Bolus 2015-02-28T06:45:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x00 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    0    0
    datetime (2015-02-28T06:45:06)
    0000   0x06 0xad 0x86 0x7c 0x0f                   ...|.
    body (0)

#### RECORD 37 BasalProfileStart 2015-02-28T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-28T07:00:00)
    0000   0x00 0x80 0x07 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 38 BolusWizard 2015-02-28T09:05:49 head[2], body[15] op[0x5b]
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
    datetime (2015-02-28T09:05:49)
    0000   0x31 0x85 0x09 0x7c 0x0f                   1..|.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 39 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 86, 'amount': 0.3},
 {'age': 96, 'amount': 0.45},
 {'age': 106, 'amount': 0.4},
 {'age': 116, 'amount': 0.4},
 {'age': 126, 'amount': 0.45},
 {'age': 136, 'amount': 0.4},
 {'age': 146, 'amount': 2.6}]
```
    op hex (23)
    0000   0x5c 0x17 0x0c 0x56 0x04 0x12 0x60 0x04    \..V..`.
    0008   0x10 0x6a 0x04 0x10 0x74 0x04 0x12 0x7e    .j..t..~
    0010   0x04 0x10 0x88 0x04 0x68 0x92 0x04         ....h..
    decimal
             92   23   12   86    4   18   96    4
             16  106    4   16  116    4   18  126
              4   16  136    4  104  146    4
    datetime (unknown)

    body (0)

#### RECORD 40 Bolus 2015-02-28T09:05:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 2.1}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x54 0x00    ......T.
    decimal
              1    0  200    0  200    0   84    0
    datetime (2015-02-28T09:05:49)
    0000   0x31 0x85 0x49 0x7c 0x0f                   1.I|.
    body (0)

#### RECORD 41 BasalProfileStart 2015-02-28T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-28T10:00:00)
    0000   0x00 0x80 0x0a 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 42 BasalProfileStart 2015-02-28T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-28T12:00:00)
    0000   0x00 0x80 0x0c 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 43 BolusWizard 2015-02-28T13:03:52 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 7.5,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 7.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-28T13:03:52)
    0000   0x34 0x83 0x0d 0x7c 0x0f                   4..|.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 44 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 234, 'amount': 0.3},
 {'age': 244, 'amount': 4.7},
 {'age': 324, 'amount': 0.3},
 {'age': 334, 'amount': 0.45},
 {'age': 344, 'amount': 0.4},
 {'age': 354, 'amount': 0.4},
 {'age': 364, 'amount': 0.45},
 {'age': 374, 'amount': 0.4},
 {'age': 384, 'amount': 2.6}]
```
    op hex (29)
    0000   0x5c 0x1d 0x0c 0xea 0x04 0xbc 0xf4 0x04    \.......
    0008   0x0c 0x44 0x14 0x12 0x4e 0x14 0x10 0x58    .D..N..X
    0010   0x14 0x10 0x62 0x14 0x12 0x6c 0x14 0x10    ..b..l..
    0018   0x76 0x14 0x68 0x80 0x14                   v.h..
    decimal
             92   29   12  234    4  188  244    4
             12   68   20   18   78   20   16   88
             20   16   98   20   18  108   20   16
            118   20  104  128   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2015-02-28T13:06:54 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 60,
 'programmed': 3.0,
 'type': 'square',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x04 0x02    ..x.x...
    decimal
              1    0  120    0  120    0    4    2
    datetime (2015-02-28T13:06:54)
    0000   0x36 0x86 0xad 0x7c 0x0f                   6..|.
    body (0)

#### RECORD 46 Bolus 2015-02-28T13:03:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x04 0x00    ........
    decimal
              1    0  180    0  180    0    4    0
    datetime (2015-02-28T13:03:52)
    0000   0x34 0x83 0x8d 0x7c 0x0f                   4..|.
    body (0)

#### RECORD 47 SensorAlert 2015-02-28T13:15:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-28T13:15:36)
    0000   0x24 0x8f 0x2d 0xbc 0x0f                   $.-..
    body (0)

#### RECORD 48 BolusWizard 2015-02-28T13:17:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 40,
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
    datetime (2015-02-28T13:17:12)
    0000   0x0c 0x91 0x0d 0x7c 0x0f                   ...|.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    (P.P(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             40   80    0   80   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 49 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 8, 'amount': 0.4},
 {'age': 18, 'amount': 4.6},
 {'age': 248, 'amount': 0.3},
 {'age': 258, 'amount': 4.7},
 {'age': 338, 'amount': 0.3},
 {'age': 348, 'amount': 0.45},
 {'age': 358, 'amount': 0.4},
 {'age': 368, 'amount': 0.4},
 {'age': 378, 'amount': 0.45},
 {'age': 388, 'amount': 0.4},
 {'age': 398, 'amount': 2.6}]
```
    op hex (35)
    0000   0x5c 0x23 0x10 0x08 0x04 0xb8 0x12 0x04    \#......
    0008   0x0c 0xf8 0x04 0xbc 0x02 0x14 0x0c 0x52    .......R
    0010   0x14 0x12 0x5c 0x14 0x10 0x66 0x14 0x10    ..\..f..
    0018   0x70 0x14 0x12 0x7a 0x14 0x10 0x84 0x14    p..z....
    0020   0x68 0x8e 0x14                             h..
    decimal
             92   35   16    8    4  184   18    4
             12  248    4  188    2   20   12   82
             20   18   92   20   16  102   20   16
            112   20   18  122   20   16  132   20
            104  142   20
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2015-02-28T13:17:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6,
 'duration': 0,
 'programmed': 3.6,
 'type': 'normal',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0xc8 0x00    ........
    decimal
              1    0  144    0  144    0  200    0
    datetime (2015-02-28T13:17:12)
    0000   0x0c 0x91 0x4d 0x7c 0x0f                   ..M|.
    body (0)

#### RECORD 51 SensorAlert 2015-02-28T13:24:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 186}
```
    op hex (3)
    0000   0x0b 0x65 0xba                             .e.
    decimal
             11  101  186
    datetime (2015-02-28T13:24:47)
    0000   0x2f 0x98 0x2d 0xbc 0x0f                   /.-..
    body (0)

#### RECORD 52 SensorAlert 2015-02-28T14:29:28 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-28T14:29:28)
    0000   0x1c 0x9d 0x2e 0xbc 0x0f                   .....
    body (0)

#### RECORD 53 SensorAlert 2015-02-28T14:39:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-02-28T14:39:30)
    0000   0x1e 0xa7 0x2e 0xbc 0x0f                   .....
    body (0)

#### RECORD 54 BasalProfileStart 2015-02-28T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-28T15:00:00)
    0000   0x00 0x80 0x0f 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 55 SensorAlert 2015-02-28T15:09:28 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 78}
```
    op hex (3)
    0000   0x0b 0x66 0x4e                             .fN
    decimal
             11  102   78
    datetime (2015-02-28T15:09:28)
    0000   0x1c 0x89 0x2f 0xbc 0x0f                   ../..
    body (0)

#### RECORD 56 SensorAlert 2015-02-28T17:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-28T17:36:00)
    0000   0x00 0xa4 0x31 0xbc 0x0f                   ..1..
    body (0)

#### RECORD 57 SensorAlert 2015-02-28T18:16:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-28T18:16:04)
    0000   0x04 0x90 0x32 0xbc 0x0f                   ..2..
    body (0)

#### RECORD 58 SensorAlert 2015-02-28T18:25:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-28T18:25:45)
    0000   0x2d 0x99 0x32 0xbc 0x0f                   -.2..
    body (0)

#### RECORD 59 Bolus 2015-02-28T18:26:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x00 0x00    ........
    decimal
              1    0  140    0  140    0    0    0
    datetime (2015-02-28T18:26:08)
    0000   0x08 0x9a 0x52 0x7c 0x0f                   ..R|.
    body (0)

#### RECORD 60 SensorAlert 2015-02-28T18:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-28T18:36:00)
    0000   0x00 0xa4 0x32 0xbc 0x0f                   ..2..
    body (0)

#### RECORD 61 CalBGForPH 2015-02-28T18:37:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 211}
```
    op hex (2)
    0000   0x0a 0xd3                                  ..
    decimal
             10  211
    datetime (2015-02-28T18:37:43)
    0000   0x2b 0xa5 0x32 0x7c 0x0f                   +.2|.
    body (0)

#### RECORD 62 BGReceived 2015-02-28T18:37:43 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 211, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2015-02-28T18:37:43)
    0000   0x2b 0xa5 0x72 0x7c 0x0f                   +.r|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 63 SensorAlert 2015-02-28T18:50:09 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 210}
```
    op hex (3)
    0000   0x0b 0x65 0xd2                             .e.
    decimal
             11  101  210
    datetime (2015-02-28T18:50:09)
    0000   0x09 0xb2 0x32 0xbc 0x0f                   ..2..
    body (0)

#### RECORD 64 SensorAlert 2015-02-28T20:56:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-28T20:56:04)
    0000   0x04 0xb8 0x34 0xbc 0x0f                   ..4..
    body (0)

#### RECORD 65 SensorAlert 2015-02-28T21:05:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-02-28T21:05:45)
    0000   0x2d 0x85 0x35 0xbc 0x0f                   -.5..
    body (0)

#### RECORD 66 BasalProfileStart 2015-02-28T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-28T22:00:00)
    0000   0x00 0x80 0x16 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 67 SensorAlert 2015-02-28T22:35:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 255}
```
    op hex (3)
    0000   0x0b 0x65 0xff                             .e.
    decimal
             11  101  255
    datetime (2015-02-28T22:35:36)
    0000   0x24 0xa3 0x36 0xbc 0x0f                   $.6..
    body (0)

#### RECORD 68 Bolus 2015-02-28T22:36:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x00 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    0    0
    datetime (2015-02-28T22:36:07)
    0000   0x07 0xa4 0x56 0x7c 0x0f                   ..V|.
    body (0)

#### RECORD 69 BolusWizard 2015-02-28T23:02:03 head[2], body[15] op[0x5b]
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
    datetime (2015-02-28T23:02:03)
    0000   0x03 0x82 0x17 0x7c 0x0f                   ...|.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 70 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 2.5}, {'age': 283, 'amount': 3.5}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0x21 0x04 0x8c 0x1b 0x14    \.d!....
    decimal
             92    8  100   33    4  140   27   20
    datetime (unknown)

    body (0)

#### RECORD 71 BolusWizard 2015-02-28T23:02:09 head[2], body[15] op[0x5b]
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
    datetime (2015-02-28T23:02:09)
    0000   0x09 0x82 0x17 0x7c 0x0f                   ...|.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    2P.d(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             50   80    0  100   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 72 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 33, 'amount': 2.5}, {'age': 283, 'amount': 3.5}]
```
    op hex (8)
    0000   0x5c 0x08 0x64 0x21 0x04 0x8c 0x1b 0x14    \.d!....
    decimal
             92    8  100   33    4  140   27   20
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2015-02-28T23:02:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x60 0x00    ......`.
    decimal
              1    0  200    0  200    0   96    0
    datetime (2015-02-28T23:02:09)
    0000   0x09 0x82 0x57 0x7c 0x0f                   ..W|.
    body (0)

#### RECORD 74 BasalProfileStart 2015-03-01T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-01T00:00:00)
    0000   0x00 0xc0 0x00 0x01 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 75 MResultTotals 2015-03-01T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x34                   ....4
    decimal
              7    0    0    8   52
    datetime (2015-03-01T00:00:00)
    0000   0x3c 0x0f                                  <.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 76 Sara6E 2015-03-01T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-01T00:00:00)
    0000   0x3c 0x0f                                  <.
    body (49)
    hex
    0000   0x05 0x00 0x9f 0x6d 0xd3 0x05 0x00 0x00    ...m....
    0008   0x08 0x34 0x03 0x30 0x27 0x05 0x04 0x3d    .4.0'..=
    0010   0x00 0xfa 0x04 0x14 0x00 0x00 0x00 0x00    ........
    0018   0x00 0xf0 0x05 0x00 0x00 0x02 0x00 0x94    ........
    0020   0x0f 0x52 0x02 0x1e 0x27 0x03 0x01 0x00    .R..'...
    0028   0x00 0x02 0x05 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  159  109  211    5    0    0
              8   52    3   48   39    5    4   61
              0  250    4   20    0    0    0    0
              0  240    5    0    0    2    0  148
             15   82    2   30   39    3    1    0
              0    2    5    1    0    0    0    0
              0

`end ReadHistoryData-page-18.data: 77 records`
