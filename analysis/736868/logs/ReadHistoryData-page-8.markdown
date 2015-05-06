## START ReadHistoryData-page-8.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x9c 0x21                                  .!
##### DEBUG DECIMAL
            156   33
#### RECORD 0 PumpResume 2015-03-16T07:46:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-16T07:46:05)
    0000   0x05 0xee 0x07 0x10 0x0f                   .....
    body (0)

#### RECORD 1 SensorAlert 2015-03-16T09:44:59 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-16T09:44:59)
    0000   0x3b 0xec 0x29 0xb0 0x0f                   ;.)..
    body (0)

#### RECORD 2 CalBGForPH 2015-03-16T09:47:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 338}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2015-03-16T09:47:18)
    0000   0x12 0xef 0x29 0x70 0x8f                   ..)p.
    body (0)

#### RECORD 3 BGReceived 2015-03-16T09:47:18 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 338, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x2a                                  ?*
    decimal
             63   42
    datetime (2015-03-16T09:47:18)
    0000   0x12 0xef 0x49 0x70 0x0f                   ..Ip.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 4 BolusWizard 2015-03-16T09:47:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 338,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.3,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 5.4,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0x52                                  [R
    decimal
             91   82
    datetime (2015-03-16T09:47:36)
    0000   0x24 0xef 0x09 0x10 0x0f                   $....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xd8 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x04 0x00 0xd4 0x78         ......x
    decimal
              0   81    0  100   40   90  216    0
              0    0    0    4    0  212  120

#### RECORD 5 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 218, 'amount': 1.0}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0xda 0x04                   \.(..
    decimal
             92    5   40  218    4
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2015-03-16T09:47:36 head[8], body[0] op[0x01]
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
    datetime (2015-03-16T09:47:36)
    0000   0x24 0xef 0xa9 0x10 0x0f                   $....
    body (0)

#### RECORD 7 Bolus 2015-03-16T09:47:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.3,
 'duration': 0,
 'programmed': 5.3,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0xd4 0x00 0xd4 0x00 0x04 0x00    ........
    decimal
              1    0  212    0  212    0    4    0
    datetime (2015-03-16T09:47:36)
    0000   0x24 0xef 0x89 0x10 0x0f                   $....
    body (0)

#### RECORD 8 BasalProfileStart 2015-03-16T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-16T10:00:00)
    0000   0x00 0xc0 0x0a 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 9 SensorAlert 2015-03-16T10:01:09 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-16T10:01:09)
    0000   0x09 0xc1 0x2a 0xb0 0x0f                   ..*..
    body (0)

#### RECORD 10 SensorAlert 2015-03-16T10:01:09 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 106'}
```
    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2015-03-16T10:01:09)
    0000   0x09 0xc1 0x2a 0xb0 0x0f                   ..*..
    body (0)

#### RECORD 11 CalBGForPH 2015-03-16T10:14:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 255}
```
    op hex (2)
    0000   0x0a 0xff                                  ..
    decimal
             10  255
    datetime (2015-03-16T10:14:54)
    0000   0x36 0xce 0x2a 0x70 0x0f                   6.*p.
    body (0)

#### RECORD 12 BGReceived 2015-03-16T10:14:54 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 255, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1f                                  ?.
    decimal
             63   31
    datetime (2015-03-16T10:14:54)
    0000   0x36 0xce 0xea 0x70 0x0f                   6..p.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 13 SensorAlert 2015-03-16T10:30:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 255}
```
    op hex (3)
    0000   0x0b 0x65 0xff                             .e.
    decimal
             11  101  255
    datetime (2015-03-16T10:30:21)
    0000   0x15 0xde 0x2a 0xb0 0x0f                   ..*..
    body (0)

#### RECORD 14 BasalProfileStart 2015-03-16T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-16T12:00:00)
    0000   0x00 0xc0 0x0c 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 15 BolusWizard 2015-03-16T12:06:10 head[2], body[15] op[0x5b]
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
    datetime (2015-03-16T12:06:10)
    0000   0x0a 0xc6 0x0c 0x70 0x0f                   ...p.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    (P.P(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             40   80    0   80   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 16 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 137, 'amount': 3.25},
 {'age': 147, 'amount': 2.05},
 {'age': 357, 'amount': 1.0}]
```
    op hex (11)
    0000   0x5c 0x0b 0x82 0x89 0x04 0x52 0x93 0x04    \....R..
    0008   0x28 0x65 0x14                             (e.
    decimal
             92   11  130  137    4   82  147    4
             40  101   20
    datetime (unknown)

    body (0)

#### RECORD 17 Bolus 2015-03-16T12:06:10 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 240,
 'programmed': 5.0,
 'type': 'square',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x4c 0x08    ......L.
    decimal
              1    0  200    0  200    0   76    8
    datetime (2015-03-16T12:06:10)
    0000   0x0a 0xc6 0x6c 0x70 0x0f                   ..lp.
    body (0)

#### RECORD 18 SensorAlert 2015-03-16T12:55:48 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-16T12:55:48)
    0000   0x30 0xf7 0x2c 0xb0 0x0f                   0.,..
    body (0)

#### RECORD 19 SensorAlert 2015-03-16T13:10:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 184}
```
    op hex (3)
    0000   0x0b 0x65 0xb8                             .e.
    decimal
             11  101  184
    datetime (2015-03-16T13:10:21)
    0000   0x15 0xca 0x2d 0xb0 0x0f                   ..-..
    body (0)

#### RECORD 20 BasalProfileStart 2015-03-16T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-16T15:00:00)
    0000   0x00 0xc0 0x0f 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 21 SensorAlert 2015-03-16T15:15:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-16T15:15:00)
    0000   0x00 0xcf 0x2f 0xb0 0x0f                   ../..
    body (0)

#### RECORD 22 SensorAlert 2015-03-16T16:15:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-16T16:15:00)
    0000   0x00 0xcf 0x30 0xb0 0x0f                   ..0..
    body (0)

#### RECORD 23 SensorAlert 2015-03-16T16:45:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-16T16:45:00)
    0000   0x00 0xed 0x30 0xb0 0x0f                   ..0..
    body (0)

#### RECORD 24 CalBGForPH 2015-03-16T16:45:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2015-03-16T16:45:44)
    0000   0x2c 0xed 0x30 0x70 0x0f                   ,.0p.
    body (0)

#### RECORD 25 BGReceived 2015-03-16T16:45:44 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 61, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2015-03-16T16:45:44)
    0000   0x2c 0xed 0xb0 0x70 0x0f                   ,..p.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 26 SensorAlert 2015-03-16T18:59:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-16T18:59:41)
    0000   0x29 0xfb 0x32 0xb0 0x0f                   ).2..
    body (0)

#### RECORD 27 SensorAlert 2015-03-16T19:10:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 187}
```
    op hex (3)
    0000   0x0b 0x65 0xbb                             .e.
    decimal
             11  101  187
    datetime (2015-03-16T19:10:20)
    0000   0x14 0xca 0x33 0xb0 0x0f                   ..3..
    body (0)

#### RECORD 28 SensorAlert 2015-03-16T20:41:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 354}
```
    op hex (3)
    0000   0x0b 0x65 0x62                             .eb
    decimal
             11  101   98
    datetime (2015-03-16T20:41:08)
    0000   0x08 0xe9 0x34 0xb0 0x8f                   ..4..
    body (0)

#### RECORD 29 Bolus 2015-03-16T20:41:48 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6,
 'duration': 0,
 'programmed': 1.6,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x40 0x01 0x40 0x00 0x00 0x00    ..@.@...
    decimal
              1    1   64    1   64    0    0    0
    datetime (2015-03-16T20:41:48)
    0000   0x30 0xe9 0x54 0x70 0x0f                   0.Tp.
    body (0)

#### RECORD 30 BasalProfileStart 2015-03-16T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-16T22:00:00)
    0000   0x00 0xc0 0x16 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 31 SensorAlert 2015-03-16T22:09:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 308}
```
    op hex (3)
    0000   0x0b 0x65 0x34                             .e4
    decimal
             11  101   52
    datetime (2015-03-16T22:09:39)
    0000   0x27 0xc9 0x36 0xb0 0x8f                   '.6..
    body (0)

#### RECORD 32 BolusWizard 2015-03-16T22:10:58 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.3,
 'carb_input': 32,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.3,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-16T22:10:58)
    0000   0x3a 0xca 0x16 0x70 0x0f                   :..p.
    body (15)
    hex
    0000   0x20 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00     P.<(Z..
    0008   0xd4 0x00 0x00 0x00 0x00 0xd4 0x78         ......x
    decimal
             32   80    0   60   40   90    0    0
            212    0    0    0    0  212  120

#### RECORD 33 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 1.6},
 {'age': 371, 'amount': 0.15},
 {'age': 381, 'amount': 0.2},
 {'age': 391, 'amount': 0.2},
 {'age': 401, 'amount': 0.2},
 {'age': 411, 'amount': 0.25},
 {'age': 421, 'amount': 0.2},
 {'age': 431, 'amount': 0.2},
 {'age': 441, 'amount': 0.2},
 {'age': 451, 'amount': 0.2},
 {'age': 461, 'amount': 0.2},
 {'age': 471, 'amount': 0.25}]
```
    op hex (38)
    0000   0x5c 0x26 0x40 0x5b 0x05 0x06 0x73 0x14    \&@[..s.
    0008   0x08 0x7d 0x14 0x08 0x87 0x14 0x08 0x91    .}......
    0010   0x14 0x0a 0x9b 0x14 0x08 0xa5 0x14 0x08    ........
    0018   0xaf 0x14 0x08 0xb9 0x14 0x08 0xc3 0x14    ........
    0020   0x08 0xcd 0x14 0x0a 0xd7 0x14              ......
    decimal
             92   38   64   91    5    6  115   20
              8  125   20    8  135   20    8  145
             20   10  155   20    8  165   20    8
            175   20    8  185   20    8  195   20
              8  205   20   10  215   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2015-03-16T22:12:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7,
 'duration': 120,
 'programmed': 2.7,
 'type': 'square',
 'unabsorbed': 5.2}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0xd0 0x04    ..l.l...
    decimal
              1    0  108    0  108    0  208    4
    datetime (2015-03-16T22:12:42)
    0000   0x2a 0xcc 0xb6 0x70 0x0f                   *..p.
    body (0)

#### RECORD 35 Bolus 2015-03-16T22:10:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6,
 'duration': 0,
 'programmed': 2.6,
 'type': 'normal',
 'unabsorbed': 5.2}
```
    op hex (8)
    0000   0x01 0x00 0x68 0x00 0x68 0x00 0xd0 0x00    ..h.h...
    decimal
              1    0  104    0  104    0  208    0
    datetime (2015-03-16T22:10:58)
    0000   0x3a 0xca 0x96 0x70 0x0f                   :..p.
    body (0)

#### RECORD 36 LowReservoir 2015-03-16T22:49:22 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-03-16T22:49:22)
    0000   0x16 0xf1 0x16 0x10 0x0f                   .....
    body (0)

#### RECORD 37 SensorAlert 2015-03-16T23:39:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 235}
```
    op hex (3)
    0000   0x0b 0x65 0xeb                             .e.
    decimal
             11  101  235
    datetime (2015-03-16T23:39:41)
    0000   0x29 0xe7 0x37 0xb0 0x0f                   ).7..
    body (0)

#### RECORD 38 BasalProfileStart 2015-03-17T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-17T00:00:00)
    0000   0x00 0xc0 0x00 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 39 MResultTotals 2015-03-17T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x06 0xe1                   .....
    decimal
              7    0    0    6  225
    datetime (2015-03-17T00:00:00)
    0000   0x30 0x8f                                  0.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 40 Sara6E 2015-03-17T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-17T00:00:00)
    0000   0x30 0x8f                                  0.
    body (49)
    hex
    0000   0x05 0x10 0xda 0x3d 0x52 0x03 0x00 0x00    ...=R...
    0008   0x06 0xe1 0x03 0x15 0x2d 0x03 0xcc 0x37    ....-..7
    0010   0x00 0x48 0x01 0x90 0x00 0xd4 0x00 0x00    .H......
    0018   0x01 0x68 0x02 0x01 0x00 0x02 0x00 0xce    .h......
    0020   0x38 0x2c 0x00 0x99 0x53 0x02 0x00 0x00    8,..S...
    0028   0x00 0x00 0x06 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  218   61   82    3    0    0
              6  225    3   21   45    3  204   55
              0   72    1  144    0  212    0    0
              1  104    2    1    0    2    0  206
             56   44    0  153   83    2    0    0
              0    0    6    0    0    0    0    0
              0

#### RECORD 41 SensorAlert 2015-03-17T01:10:20 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 218}
```
    op hex (3)
    0000   0x0b 0x65 0xda                             .e.
    decimal
             11  101  218
    datetime (2015-03-17T01:10:20)
    0000   0x14 0xca 0x21 0xb1 0x0f                   ..!..
    body (0)

#### RECORD 42 SensorAlert 2015-03-17T02:41:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 197}
```
    op hex (3)
    0000   0x0b 0x65 0xc5                             .e.
    decimal
             11  101  197
    datetime (2015-03-17T02:41:08)
    0000   0x08 0xe9 0x22 0xb1 0x0f                   .."..
    body (0)

#### RECORD 43 SensorAlert 2015-03-17T03:45:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-17T03:45:00)
    0000   0x00 0xed 0x23 0xb1 0x0f                   ..#..
    body (0)

#### RECORD 44 BasalProfileStart 2015-03-17T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-17T04:00:00)
    0000   0x00 0xc0 0x04 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 45 SensorAlert 2015-03-17T04:09:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 210}
```
    op hex (3)
    0000   0x0b 0x65 0xd2                             .e.
    decimal
             11  101  210
    datetime (2015-03-17T04:09:39)
    0000   0x27 0xc9 0x24 0xb1 0x0f                   '.$..
    body (0)

#### RECORD 46 CalBGForPH 2015-03-17T04:25:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2015-03-17T04:25:24)
    0000   0x18 0xd9 0x24 0x71 0x0f                   ..$q.
    body (0)

#### RECORD 47 BGReceived 2015-03-17T04:25:24 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 161, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2015-03-17T04:25:24)
    0000   0x18 0xd9 0x24 0x71 0x0f                   ..$q.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 48 BolusWizard 2015-03-17T04:25:29 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 161,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xa1                                  [.
    decimal
             91  161
    datetime (2015-03-17T04:25:29)
    0000   0x1d 0xd9 0x04 0x11 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x28 0x00    .P.d(Z(.
    0008   0x00 0x00 0x00 0x00 0x00 0x28 0x78         .....(x
    decimal
              0   80    0  100   40   90   40    0
              0    0    0    0    0   40  120

#### RECORD 49 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 256, 'amount': 0.1},
 {'age': 266, 'amount': 0.2},
 {'age': 276, 'amount': 0.25},
 {'age': 286, 'amount': 0.2},
 {'age': 296, 'amount': 0.25},
 {'age': 306, 'amount': 0.2},
 {'age': 316, 'amount': 0.25},
 {'age': 326, 'amount': 0.2},
 {'age': 336, 'amount': 0.25},
 {'age': 346, 'amount': 0.2},
 {'age': 356, 'amount': 0.25},
 {'age': 366, 'amount': 0.2},
 {'age': 376, 'amount': 2.75},
 {'age': 466, 'amount': 1.6}]
```
    op hex (44)
    0000   0x5c 0x2c 0x04 0x00 0x14 0x08 0x0a 0x14    \,......
    0008   0x0a 0x14 0x14 0x08 0x1e 0x14 0x0a 0x28    .......(
    0010   0x14 0x08 0x32 0x14 0x0a 0x3c 0x14 0x08    ..2..<..
    0018   0x46 0x14 0x0a 0x50 0x14 0x08 0x5a 0x14    F..P..Z.
    0020   0x0a 0x64 0x14 0x08 0x6e 0x14 0x6e 0x78    .d..n.nx
    0028   0x14 0x40 0xd2 0x15                        .@..
    decimal
             92   44    4    0   20    8   10   20
             10   20   20    8   30   20   10   40
             20    8   50   20   10   60   20    8
             70   20   10   80   20    8   90   20
             10  100   20    8  110   20  110  120
             20   64  210   21
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2015-03-17T04:25:29 head[8], body[0] op[0x01]
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
    datetime (2015-03-17T04:25:29)
    0000   0x1d 0xd9 0xa4 0x11 0x0f                   .....
    body (0)

#### RECORD 51 Bolus 2015-03-17T04:25:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x00 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    0    0
    datetime (2015-03-17T04:25:29)
    0000   0x1d 0xd9 0x84 0x11 0x0f                   .....
    body (0)

#### RECORD 52 LowReservoir 2015-03-17T06:34:44 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-03-17T06:34:44)
    0000   0x2c 0xe2 0x06 0x11 0x0f                   ,....
    body (0)

#### RECORD 53 BasalProfileStart 2015-03-17T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-17T07:00:00)
    0000   0x00 0xc0 0x07 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 54 PumpSuspend 2015-03-17T07:19:56 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-17T07:19:56)
    0000   0x38 0xd3 0x07 0x11 0x0f                   8....
    body (0)

#### RECORD 55 BasalProfileStart 2015-03-17T07:37:38 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-17T07:37:38)
    0000   0x26 0xe5 0x07 0x11 0x0f                   &....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 56 PumpResume 2015-03-17T07:37:38 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-17T07:37:38)
    0000   0x26 0xe5 0x07 0x11 0x0f                   &....
    body (0)

#### RECORD 57 BolusWizard 2015-03-17T07:56:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-17T07:56:23)
    0000   0x17 0xf8 0x07 0x71 0x0f                   ...q.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    <P.d(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             60   80    0  100   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 58 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 217, 'amount': 1.0},
 {'age': 467, 'amount': 0.1},
 {'age': 477, 'amount': 0.2}]
```
    op hex (11)
    0000   0x5c 0x0b 0x28 0xd9 0x04 0x04 0xd3 0x14    \.(.....
    0008   0x08 0xdd 0x14                             ...
    decimal
             92   11   40  217    4    4  211   20
              8  221   20
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2015-03-17T07:59:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 60,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x04 0x02    ..P.P...
    decimal
              1    0   80    0   80    0    4    2
    datetime (2015-03-17T07:59:06)
    0000   0x06 0xfb 0xa7 0x71 0x0f                   ...q.
    body (0)

#### RECORD 60 Bolus 2015-03-17T07:56:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x04 0x00    ........
    decimal
              1    0  160    0  160    0    4    0
    datetime (2015-03-17T07:56:24)
    0000   0x18 0xf8 0x87 0x71 0x0f                   ...q.
    body (0)

#### RECORD 61 SensorAlert 2015-03-17T08:59:41 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-17T08:59:41)
    0000   0x29 0xfb 0x28 0xb1 0x0f                   ).(..
    body (0)

#### RECORD 62 SensorAlert 2015-03-17T09:16:15 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 79}
```
    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-03-17T09:16:15)
    0000   0x0f 0xd0 0x29 0xb1 0x0f                   ..)..
    body (0)

#### RECORD 63 BasalProfileStart 2015-03-17T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-17T10:00:00)
    0000   0x00 0xc0 0x0a 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 64 BasalProfileStart 2015-03-17T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-17T12:00:00)
    0000   0x00 0xc0 0x0c 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 65 SensorAlert 2015-03-17T12:45:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-17T12:45:56)
    0000   0x38 0xed 0x2c 0xb1 0x0f                   8.,..
    body (0)

#### RECORD 66 SensorAlert 2015-03-17T12:55:47 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-17T12:55:47)
    0000   0x2f 0xf7 0x2c 0xb1 0x0f                   /.,..
    body (0)

#### RECORD 67 Bolus 2015-03-17T14:21:38 head[8], body[0] op[0x01]
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
    datetime (2015-03-17T14:21:38)
    0000   0x26 0xd5 0x4e 0x71 0x0f                   &.Nq.
    body (0)

#### RECORD 68 SensorAlert 2015-03-17T14:24:58 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 207}
```
    op hex (3)
    0000   0x0b 0x65 0xcf                             .e.
    decimal
             11  101  207
    datetime (2015-03-17T14:24:58)
    0000   0x3a 0xd8 0x2e 0xb1 0x0f                   :....
    body (0)

#### RECORD 69 BasalProfileStart 2015-03-17T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-17T15:00:00)
    0000   0x00 0xc0 0x0f 0x11 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 70 SensorAlert 2015-03-17T15:25:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-17T15:25:00)
    0000   0x00 0xd9 0x2f 0xb1 0x0f                   ../..
    body (0)

#### RECORD 71 SensorAlert 2015-03-17T15:56:15 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-17T15:56:15)
    0000   0x0f 0xf8 0x2f 0xb1 0x0f                   ../..
    body (0)

#### RECORD 72 SensorAlert 2015-03-17T16:01:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-03-17T16:01:08)
    0000   0x08 0xc1 0x30 0xb1 0x0f                   ..0..
    body (0)

#### RECORD 73 CalBGForPH 2015-03-17T16:19:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 184}
```
    op hex (2)
    0000   0x0a 0xb8                                  ..
    decimal
             10  184
    datetime (2015-03-17T16:19:52)
    0000   0x34 0xd3 0x30 0x71 0x0f                   4.0q.
    body (0)

#### RECORD 74 BGReceived 2015-03-17T16:19:52 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 184, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2015-03-17T16:19:52)
    0000   0x34 0xd3 0x10 0x71 0x0f                   4..q.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 75 BolusWizard 2015-03-17T16:19:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 184,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.6,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 1.6,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.0}
```
    op hex (2)
    0000   0x5b 0xb8                                  [.
    decimal
             91  184
    datetime (2015-03-17T16:19:59)
    0000   0x3b 0xd3 0x10 0x11 0x0f                   ;....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x50 0x28 0x5a 0x40 0x00    .P.P(Z@.
    0008   0x00 0x00 0x00 0x28 0x00 0x18 0x78         ...(..x
    decimal
              0   80    0   80   40   90   64    0
              0    0    0   40    0   24  120

#### RECORD 76 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 120, 'amount': 2.0},
 {'age': 450, 'amount': 0.35},
 {'age': 460, 'amount': 0.3},
 {'age': 470, 'amount': 0.35}]
```
    op hex (14)
    0000   0x5c 0x0e 0x50 0x78 0x04 0x0e 0xc2 0x14    \.Px....
    0008   0x0c 0xcc 0x14 0x0e 0xd6 0x14              ......
    decimal
             92   14   80  120    4   14  194   20
             12  204   20   14  214   20
    datetime (unknown)

    body (0)

#### RECORD 77 Bolus 2015-03-17T16:19:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x28 0x00    ......(.
    decimal
              1    0    0    0    0    0   40    0
    datetime (2015-03-17T16:19:59)
    0000   0x3b 0xd3 0xb0 0x11 0x0f                   ;....
    body (0)

#### RECORD 78 Bolus 2015-03-17T16:20:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6,
 'duration': 0,
 'programmed': 0.6,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x18 0x00 0x18 0x00 0x28 0x00    ......(.
    decimal
              1    0   24    0   24    0   40    0
    datetime (2015-03-17T16:20:00)
    0000   0x00 0xd4 0x90 0x11 0x0f                   .....
    body (0)

#### RECORD 79 Bolus 2015-03-17T20:20:58 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.15,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0x56 0x00 0x00 0x00    ....V...
    decimal
              1    0  160    0   86    0    0    0
    datetime (2015-03-17T20:20:58)
    0000   0x3a 0xd4 0x54 0x71 0x0f                   :.Tq.
    body (0)

#### RECORD 80 NoDelivery 2015-03-17T20:22:24 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-17T20:22:24)
    0000   0x18 0xd6 0x54 0x51 0x0f                   ..TQ.
    body (0)

#### RECORD 81 ClearAlarm 2015-03-17T20:22:30 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-17T20:22:30)
    0000   0x1e 0xd6 0x14 0x11 0x0f                   .....
    body (0)

#### RECORD 82 Rewind 2015-03-17T20:26:13 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-03-17T20:26:13)
    0000   0x0d 0xda 0x14 0x11 0x0f                   .....
    body (0)

#### RECORD 83 Prime 2015-03-17T20:28:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.3, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x3f                   ....?
    decimal
              3    0    0    0   63
    datetime (2015-03-17T20:28:19)
    0000   0x13 0xdc 0x34 0x11 0x0f                   ..4..
    body (0)

#### RECORD 84 BasalProfileStart 2015-03-17T20:29:33 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-17T20:29:33)
    0000   0x21 0xdd 0x14 0x11 0x0f                   !....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 85 Prime 2015-03-17T20:29:18 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-03-17T20:29:18)
    0000   0x12 0xdd 0x14 0x11 0x0f                   .....
    body (0)

#### RECORD 86 Bolus 2015-03-17T20:31:16 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x58 0x00    ..d.d.X.
    decimal
              1    0  100    0  100    0   88    0
    datetime (2015-03-17T20:31:16)
    0000   0x10 0xdf 0x54 0x71 0x0f                   ..Tq.
    body (0)

#### RECORD 87 SensorAlert 2015-03-17T20:45:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-17T20:45:56)
    0000   0x38 0xed 0x34 0xb1 0x0f                   8.4..
    body (0)

#### RECORD 88 SensorAlert 2015-03-17T20:49:39 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-17T20:49:39)
    0000   0x27 0xf1 0x34 0xb1 0x0f                   '.4..
    body (0)

`end ReadHistoryData-page-8.data: 89 records`
