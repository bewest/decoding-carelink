## START ReadHistoryData-page-16.data
#### STOPPING DOUBLE NULLS @ 981, found 41 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xbd 0xbe                                  ..
##### DEBUG DECIMAL
            189  190
#### RECORD 0 Sara6E 2015-03-03T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-03T00:00:00)
    0000   0x22 0x8f                                  ".
    body (49)
    hex
    0000   0x05 0x55 0x84 0x84 0x84 0x02 0x00 0x00    .U......
    0008   0x06 0xf5 0x03 0x2b 0x2e 0x03 0xca 0x36    ...+...6
    0010   0x00 0x91 0x02 0x44 0x01 0x0e 0x00 0x00    ...D....
    0018   0x00 0x78 0x02 0x02 0x00 0x01 0x04 0xc4    .x......
    0020   0x29 0x3b 0x00 0x1b 0x68 0x00 0x00 0x84    );..h...
    0028   0x84 0x00 0x01 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   85  132  132  132    2    0    0
              6  245    3   43   46    3  202   54
              0  145    2   68    1   14    0    0
              0  120    2    2    0    1    4  196
             41   59    0   27  104    0    0  132
            132    0    1    0    0    0    0    0
              0

#### RECORD 1 PumpSuspend 2015-03-03T00:33:06 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-03T00:33:06)
    0000   0x06 0xe1 0x00 0x03 0x0f                   .....
    body (0)

#### RECORD 2 BasalProfileStart 2015-03-03T00:33:13 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-03T00:33:13)
    0000   0x0d 0xe1 0x00 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 3 PumpResume 2015-03-03T00:33:13 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-03T00:33:13)
    0000   0x0d 0xe1 0x00 0x03 0x0f                   .....
    body (0)

#### RECORD 4 CalBGForPH 2015-03-03T00:34:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 127}
```
    op hex (2)
    0000   0x0a 0x7f                                  ..
    decimal
             10  127
    datetime (2015-03-03T00:34:00)
    0000   0x00 0xe2 0x20 0x63 0x0f                   .. c.
    body (0)

#### RECORD 5 BGReceived 2015-03-03T00:34:00 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 127, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2015-03-03T00:34:00)
    0000   0x00 0xe2 0xe0 0x63 0x0f                   ...c.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 6 SensorAlert 2015-03-03T01:07:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-03T01:07:25)
    0000   0x19 0xc7 0x21 0xa3 0x0f                   ..!..
    body (0)

#### RECORD 7 SensorAlert 2015-03-03T01:17:16 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 189}
```
    op hex (3)
    0000   0x0b 0x65 0xbd                             .e.
    decimal
             11  101  189
    datetime (2015-03-03T01:17:16)
    0000   0x10 0xd1 0x21 0xa3 0x0f                   ..!..
    body (0)

#### RECORD 8 BasalProfileStart 2015-03-03T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-03T04:00:00)
    0000   0x00 0xc0 0x04 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 9 SensorAlert 2015-03-03T04:17:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 307}
```
    op hex (3)
    0000   0x0b 0x65 0x33                             .e3
    decimal
             11  101   51
    datetime (2015-03-03T04:17:44)
    0000   0x2c 0xd1 0x24 0xa3 0x8f                   ,.$..
    body (0)

#### RECORD 10 SensorAlert 2015-03-03T05:47:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 277}
```
    op hex (3)
    0000   0x0b 0x65 0x15                             .e.
    decimal
             11  101   21
    datetime (2015-03-03T05:47:25)
    0000   0x19 0xef 0x25 0xa3 0x8f                   ..%..
    body (0)

#### RECORD 11 Bolus 2015-03-03T06:00:31 head[8], body[0] op[0x01]
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
    datetime (2015-03-03T06:00:31)
    0000   0x1f 0xc0 0x46 0x63 0x0f                   ..Fc.
    body (0)

#### RECORD 12 BasalProfileStart 2015-03-03T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-03T07:00:00)
    0000   0x00 0xc0 0x07 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 13 SensorAlert 2015-03-03T07:02:37 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose Predicted', 'alarm_type': 115}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-03T07:02:37)
    0000   0x25 0xc2 0x27 0xa3 0x0f                   %.'..
    body (0)

#### RECORD 14 BasalProfileStart 2015-03-03T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-03T10:00:00)
    0000   0x00 0xc0 0x0a 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 15 SensorAlert 2015-03-03T11:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-03T11:34:00)
    0000   0x00 0xe2 0x2b 0xa3 0x0f                   ..+..
    body (0)

#### RECORD 16 BasalProfileStart 2015-03-03T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-03T12:00:00)
    0000   0x00 0xc0 0x0c 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 17 SensorAlert 2015-03-03T12:34:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-03T12:34:00)
    0000   0x00 0xe2 0x2c 0xa3 0x0f                   ..,..
    body (0)

#### RECORD 18 SensorAlert 2015-03-03T13:04:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-03T13:04:00)
    0000   0x00 0xc4 0x2d 0xa3 0x0f                   ..-..
    body (0)

#### RECORD 19 CalBGForPH 2015-03-03T13:24:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2015-03-03T13:24:40)
    0000   0x28 0xd8 0x2d 0x63 0x0f                   (.-c.
    body (0)

#### RECORD 20 BGReceived 2015-03-03T13:24:40 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 69, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2015-03-03T13:24:40)
    0000   0x28 0xd8 0xad 0x63 0x0f                   (..c.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 21 BasalProfileStart 2015-03-03T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-03T15:00:00)
    0000   0x00 0xc0 0x0f 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 22 Bolus 2015-03-03T19:01:08 head[8], body[0] op[0x01]
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
    datetime (2015-03-03T19:01:08)
    0000   0x08 0xc1 0x53 0x63 0x0f                   ..Sc.
    body (0)

#### RECORD 23 PumpSuspend 2015-03-03T19:02:39 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-03T19:02:39)
    0000   0x27 0xc2 0x13 0x03 0x0f                   '....
    body (0)

#### RECORD 24 SensorAlert 2015-03-03T19:31:49 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-03T19:31:49)
    0000   0x31 0xdf 0x33 0xa3 0x0f                   1.3..
    body (0)

#### RECORD 25 BasalProfileStart 2015-03-03T19:45:06 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-03T19:45:06)
    0000   0x06 0xed 0x13 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 26 PumpResume 2015-03-03T19:45:06 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-03T19:45:06)
    0000   0x06 0xed 0x13 0x03 0x0f                   .....
    body (0)

#### RECORD 27 Bolus 2015-03-03T19:45:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x48 0x00    ..<.<.H.
    decimal
              1    0   60    0   60    0   72    0
    datetime (2015-03-03T19:45:20)
    0000   0x14 0xed 0x53 0x63 0x0f                   ..Sc.
    body (0)

#### RECORD 28 BasalProfileStart 2015-03-03T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-03T22:00:00)
    0000   0x00 0xc0 0x16 0x03 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 29 SensorAlert 2015-03-03T22:27:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-03T22:27:25)
    0000   0x19 0xdb 0x36 0xa3 0x0f                   ..6..
    body (0)

#### RECORD 30 SensorAlert 2015-03-03T22:37:15 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-03T22:37:15)
    0000   0x0f 0xe5 0x36 0xa3 0x0f                   ..6..
    body (0)

#### RECORD 31 BasalProfileStart 2015-03-04T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-04T00:00:00)
    0000   0x00 0xc0 0x00 0x04 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 32 MResultTotals 2015-03-04T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x31                   ....1
    decimal
              7    0    0    4   49
    datetime (2015-03-04T00:00:00)
    0000   0x23 0x8f                                  #.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 33 Sara6E 2015-03-04T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-04T00:00:00)
    0000   0x23 0x8f                                  #.
    body (49)
    hex
    0000   0x05 0x00 0x62 0x45 0x7f 0x02 0x00 0x00    ..bE....
    0008   0x04 0x31 0x03 0x19 0x4a 0x01 0x18 0x1a    .1..J...
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x01 0x18 0x00 0x00 0x00 0x03 0x00 0xa7    ........
    0020   0x1e 0x46 0x00 0x14 0x46 0x03 0x01 0x00    .F..F...
    0028   0x00 0x00 0x04 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0   98   69  127    2    0    0
              4   49    3   25   74    1   24   26
              0    0    0    0    0    0    0    0
              1   24    0    0    0    3    0  167
             30   70    0   20   70    3    1    0
              0    0    4    1    0    0    0    0
              0

#### RECORD 34 SensorAlert 2015-03-04T00:06:26 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 228}
```
    op hex (3)
    0000   0x0b 0x65 0xe4                             .e.
    decimal
             11  101  228
    datetime (2015-03-04T00:06:26)
    0000   0x1a 0xc6 0x20 0xa4 0x0f                   .. ..
    body (0)

#### RECORD 35 SensorAlert 2015-03-04T00:24:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-04T00:24:00)
    0000   0x00 0xd8 0x20 0xa4 0x0f                   .. ..
    body (0)

#### RECORD 36 SensorAlert 2015-03-04T01:24:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-04T01:24:00)
    0000   0x00 0xd8 0x21 0xa4 0x0f                   ..!..
    body (0)

#### RECORD 37 SensorAlert 2015-03-04T01:54:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-04T01:54:00)
    0000   0x00 0xf6 0x21 0xa4 0x0f                   ..!..
    body (0)

#### RECORD 38 CalBGForPH 2015-03-04T02:18:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 371}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2015-03-04T02:18:16)
    0000   0x10 0xd2 0x22 0x64 0x8f                   .."d.
    body (0)

#### RECORD 39 BGReceived 2015-03-04T02:18:16 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 371, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2e                                  ?.
    decimal
             63   46
    datetime (2015-03-04T02:18:16)
    0000   0x10 0xd2 0x62 0x64 0x0f                   ..bd.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 40 BolusWizard 2015-03-04T02:18:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 371,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.2,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 6.2,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2015-03-04T02:18:30)
    0000   0x1e 0xd2 0x02 0x04 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xf8 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0xf8 0x78         ......x
    decimal
              0   81    0  100   40   90  248    0
              0    0    0    0    0  248  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 399, 'amount': 1.5}, {'age': 439, 'amount': 2.0}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x8f 0x14 0x50 0xb7 0x14    \.<..P..
    decimal
             92    8   60  143   20   80  183   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2015-03-04T02:18:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    decimal
              1    0    0    0    0    0    0    0
    datetime (2015-03-04T02:18:30)
    0000   0x1e 0xd2 0xa2 0x04 0x0f                   .....
    body (0)

#### RECORD 43 Bolus 2015-03-04T02:18:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.2,
 'duration': 0,
 'programmed': 6.2,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xf8 0x00 0xf8 0x00 0x00 0x00    ........
    decimal
              1    0  248    0  248    0    0    0
    datetime (2015-03-04T02:18:30)
    0000   0x1e 0xd2 0x82 0x04 0x0f                   .....
    body (0)

#### RECORD 44 SensorAlert 2015-03-04T02:31:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 369}
```
    op hex (3)
    0000   0x0b 0x65 0x71                             .eq
    decimal
             11  101  113
    datetime (2015-03-04T02:31:07)
    0000   0x07 0xdf 0x22 0xa4 0x8f                   .."..
    body (0)

#### RECORD 45 BasalProfileStart 2015-03-04T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-04T04:00:00)
    0000   0x00 0xc0 0x04 0x04 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 46 SensorAlert 2015-03-04T04:01:09 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-04T04:01:09)
    0000   0x09 0xc1 0x24 0xa4 0x0f                   ..$..
    body (0)

#### RECORD 47 SensorAlert 2015-03-04T05:57:15 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose Predicted', 'alarm_type': 115}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-04T05:57:15)
    0000   0x0f 0xf9 0x25 0xa4 0x0f                   ..%..
    body (0)

#### RECORD 48 BasalProfileStart 2015-03-04T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-04T07:00:00)
    0000   0x00 0xc0 0x07 0x04 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 49 SensorAlert 2015-03-04T07:37:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-04T07:37:43)
    0000   0x2b 0xe5 0x27 0xa4 0x0f                   +.'..
    body (0)

#### RECORD 50 SensorAlert 2015-03-04T07:47:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-04T07:47:24)
    0000   0x18 0xef 0x27 0xa4 0x0f                   ..'..
    body (0)

#### RECORD 51 Bolus 2015-03-04T08:42:45 head[8], body[0] op[0x01]
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
    datetime (2015-03-04T08:42:45)
    0000   0x2d 0xea 0x48 0x64 0x0f                   -.Hd.
    body (0)

#### RECORD 52 SensorAlert 2015-03-04T09:17:15 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 244}
```
    op hex (3)
    0000   0x0b 0x65 0xf4                             .e.
    decimal
             11  101  244
    datetime (2015-03-04T09:17:15)
    0000   0x0f 0xd1 0x29 0xa4 0x0f                   ..)..
    body (0)

#### RECORD 53 Bolus 2015-03-04T09:17:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x4c 0x00    ......L.
    decimal
              1    0  160    0  160    0   76    0
    datetime (2015-03-04T09:17:40)
    0000   0x28 0xd1 0x49 0x64 0x0f                   (.Id.
    body (0)

#### RECORD 54 BasalProfileStart 2015-03-04T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-04T10:00:00)
    0000   0x00 0xc0 0x0a 0x04 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 55 SensorAlert 2015-03-04T10:27:24 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose Predicted', 'alarm_type': 115}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-04T10:27:24)
    0000   0x18 0xdb 0x2a 0xa4 0x0f                   ..*..
    body (0)

#### RECORD 56 SensorAlert 2015-03-04T11:57:15 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-04T11:57:15)
    0000   0x0f 0xf9 0x2b 0xa4 0x0f                   ..+..
    body (0)

#### RECORD 57 BasalProfileStart 2015-03-04T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-04T12:00:00)
    0000   0x00 0xc0 0x0c 0x04 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 58 SensorAlert 2015-03-04T12:06:26 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-04T12:06:26)
    0000   0x1a 0xc6 0x2c 0xa4 0x0f                   ..,..
    body (0)

#### RECORD 59 BolusWizard 2015-03-04T12:08:50 head[2], body[15] op[0x5b]
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
    datetime (2015-03-04T12:08:50)
    0000   0x32 0xc8 0x0c 0x64 0x0f                   2..d.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 60 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 169, 'amount': 2.0},
 {'age': 179, 'amount': 2.0},
 {'age': 209, 'amount': 2.0}]
```
    op hex (11)
    0000   0x5c 0x0b 0x50 0xa9 0x04 0x50 0xb3 0x04    \.P..P..
    0008   0x50 0xd1 0x04                             P..
    decimal
             92   11   80  169    4   80  179    4
             80  209    4
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2015-03-04T12:12:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 30,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x28 0x01    ..P.P.(.
    decimal
              1    0   80    0   80    0   40    1
    datetime (2015-03-04T12:12:33)
    0000   0x21 0xcc 0xac 0x64 0x0f                   !..d.
    body (0)

#### RECORD 62 Bolus 2015-03-04T12:08:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.5,
 'duration': 0,
 'programmed': 5.5,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0xdc 0x00 0xdc 0x00 0x28 0x00    ......(.
    decimal
              1    0  220    0  220    0   40    0
    datetime (2015-03-04T12:08:50)
    0000   0x32 0xc8 0x8c 0x64 0x0f                   2..d.
    body (0)

#### RECORD 63 SensorAlert 2015-03-04T13:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Cal Reminder', 'alarm_type': 105}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-04T13:18:00)
    0000   0x00 0xd2 0x2d 0xa4 0x0f                   ..-..
    body (0)

#### RECORD 64 SensorAlert 2015-03-04T14:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-04T14:18:00)
    0000   0x00 0xd2 0x2e 0xa4 0x0f                   .....
    body (0)

#### RECORD 65 SensorAlert 2015-03-04T14:48:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-04T14:48:00)
    0000   0x00 0xf0 0x2e 0xa4 0x0f                   .....
    body (0)

#### RECORD 66 BasalProfileStart 2015-03-04T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-04T15:00:00)
    0000   0x00 0xc0 0x0f 0x04 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 67 SensorAlert 2015-03-04T15:18:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Meter BG Now', 'alarm_type': 104}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-04T15:18:00)
    0000   0x00 0xd2 0x2f 0xa4 0x0f                   ../..
    body (0)

#### RECORD 68 CalBGForPH 2015-03-04T15:20:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2015-03-04T15:20:34)
    0000   0x22 0xd4 0x2f 0x64 0x0f                   "./d.
    body (0)

#### RECORD 69 BGReceived 2015-03-04T15:20:34 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 139, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2015-03-04T15:20:34)
    0000   0x22 0xd4 0x6f 0x64 0x0f                   ".od.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 70 Bolus 2015-03-04T15:26:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x2c 0x00    ..d.d.,.
    decimal
              1    0  100    0  100    0   44    0
    datetime (2015-03-04T15:26:38)
    0000   0x26 0xda 0x4f 0x64 0x0f                   &.Od.
    body (0)

#### RECORD 71 SensorAlert 2015-03-04T15:42:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-04T15:42:36)
    0000   0x24 0xea 0x2f 0xa4 0x0f                   $./..
    body (0)

#### RECORD 72 Bolus 2015-03-04T15:43:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 3.2}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x80 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  128    0
    datetime (2015-03-04T15:43:00)
    0000   0x00 0xeb 0x4f 0x64 0x0f                   ..Od.
    body (0)

#### RECORD 73 Bolus 2015-03-04T16:44:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 3.3}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x84 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  132    0
    datetime (2015-03-04T16:44:59)
    0000   0x3b 0xec 0x50 0x64 0x0f                   ;.Pd.
    body (0)

#### RECORD 74 Bolus 2015-03-04T18:25:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x58 0x00    ..x.x.X.
    decimal
              1    0  120    0  120    0   88    0
    datetime (2015-03-04T18:25:23)
    0000   0x17 0xd9 0x52 0x64 0x0f                   ..Rd.
    body (0)

#### RECORD 75 SensorAlert 2015-03-04T21:26:26 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Unknown sensor alarm (114)', 'alarm_type': 114}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-04T21:26:26)
    0000   0x1a 0xda 0x35 0xa4 0x0f                   ..5..
    body (0)

#### RECORD 76 BolusWizard 2015-03-04T21:27:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.0,
 'carb_input': 48,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 8.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-04T21:27:32)
    0000   0x20 0xdb 0x15 0x64 0x0f                    ..d.
    body (15)
    hex
    0000   0x30 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    0P.<(Z..
    0008   0x40 0x00 0x00 0x00 0x01 0x40 0x78         @....@x
    decimal
             48   80    0   60   40   90    0    1
             64    0    0    0    1   64  120

#### RECORD 77 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 188, 'amount': 3.0},
 {'age': 288, 'amount': 2.5},
 {'age': 348, 'amount': 2.0},
 {'age': 368, 'amount': 2.5}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0xbc 0x04 0x64 0x20 0x14    \.x..d .
    0008   0x50 0x5c 0x14 0x64 0x70 0x14              P\.dp.
    decimal
             92   14  120  188    4  100   32   20
             80   92   20  100  112   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2015-03-04T21:30:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9,
 'duration': 120,
 'programmed': 4.0,
 'type': 'square',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0x24 0x00 0x14 0x04    ....$...
    decimal
              1    0  160    0   36    0   20    4
    datetime (2015-03-04T21:30:14)
    0000   0x0e 0xde 0xb5 0x64 0x0f                   ...d.
    body (0)

#### RECORD 79 Bolus 2015-03-04T21:27:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x14 0x00    ........
    decimal
              1    0  160    0  160    0   20    0
    datetime (2015-03-04T21:27:32)
    0000   0x20 0xdb 0x95 0x64 0x0f                    ..d.
    body (0)

#### RECORD 80 SensorAlert 2015-03-04T21:37:43 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'High Glucose', 'alarm_type': 101, 'amount': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-04T21:37:43)
    0000   0x2b 0xe5 0x35 0xa4 0x0f                   +.5..
    body (0)

#### RECORD 81 CalBGForPH 2015-03-04T21:56:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2015-03-04T21:56:58)
    0000   0x3a 0xf8 0x35 0x64 0x0f                   :.5d.
    body (0)

#### RECORD 82 BGReceived 2015-03-04T21:56:58 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 107, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2015-03-04T21:56:58)
    0000   0x3a 0xf8 0x75 0x64 0x0f                   :.ud.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 83 PumpSuspend 2015-03-04T21:57:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-04T21:57:17)
    0000   0x11 0xf9 0x15 0x04 0x0f                   .....
    body (0)

#### RECORD 84 BasalProfileStart 2015-03-04T21:57:21 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-04T21:57:21)
    0000   0x15 0xf9 0x15 0x04 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 85 PumpResume 2015-03-04T21:57:21 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-04T21:57:21)
    0000   0x15 0xf9 0x15 0x04 0x0f                   .....
    body (0)

#### RECORD 86 BasalProfileStart 2015-03-04T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-04T22:00:00)
    0000   0x00 0xc0 0x16 0x04 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 87 SensorAlert 2015-03-04T22:22:36 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose Predicted', 'alarm_type': 115}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-04T22:22:36)
    0000   0x24 0xd6 0x36 0xa4 0x0f                   $.6..
    body (0)

#### RECORD 88 SensorAlert 2015-03-04T22:51:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_description': 'Low Glucose Predicted', 'alarm_type': 115}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-04T22:51:48)
    0000   0x30 0xf3 0x36 0xa4 0x0f                   0.6..
    body (0)

#### RECORD 89 BasalProfileStart 2015-03-05T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-05T00:00:00)
    0000   0x00 0xc0 0x00 0x05 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 90 MResultTotals 2015-03-05T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0x98                   .....
    decimal
              7    0    0    8  152
    datetime (2015-03-05T00:00:00)
    0000   0x24 0x8f                                  $.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end ReadHistoryData-page-16.data: 91 records`
