## START ReadHistoryData-page-1.data
#### RECORD 0 BasalProfileStart 2015-03-27T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-27T10:00:00)
    0000   0x00 0xc0 0x0a 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 1 SensorAlert 2015-03-27T10:08:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-27T10:08:00)
    0000   0x00 0xc8 0x2a 0xbb 0x0f                   ..*..
    body (0)

#### RECORD 2 SensorAlert 2015-03-27T10:37:57 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-27T10:37:57)
    0000   0x39 0xe5 0x2a 0xbb 0x0f                   9.*..
    body (0)

#### RECORD 3 CalBGForPH 2015-03-27T10:38:51 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2015-03-27T10:38:51)
    0000   0x33 0xe6 0x2a 0x7b 0x0f                   3.*{.
    body (0)

#### RECORD 4 BGReceived 2015-03-27T10:38:51 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 171, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2015-03-27T10:38:51)
    0000   0x33 0xe6 0x6a 0x7b 0x0f                   3.j{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 5 SensorAlert 2015-03-27T11:17:57 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-27T11:17:57)
    0000   0x39 0xd1 0x2b 0xbb 0x0f                   9.+..
    body (0)

#### RECORD 6 BolusWizard 2015-03-27T11:49:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.8,
 'carb_input': 47,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 5.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-27T11:49:07)
    0000   0x07 0xf1 0x0b 0x7b 0x0f                   ...{.
    body (15)
    hex
    0000   0x2f 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    /P.P(Z..
    0008   0xe8 0x00 0x00 0x00 0x00 0xe8 0x78         ......x
    decimal
             47   80    0   80   40   90    0    0
            232    0    0    0    0  232  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 220, 'amount': 4.0}, {'age': 310, 'amount': 1.5}]
```
    op hex (8)
    0000   0x5c 0x08 0xa0 0xdc 0x04 0x3c 0x36 0x14    \....<6.
    decimal
             92    8  160  220    4   60   54   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2015-03-27T11:51:20 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 60,
 'programmed': 2.5,
 'type': 'square',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x10 0x02    ..d.d...
    decimal
              1    0  100    0  100    0   16    2
    datetime (2015-03-27T11:51:20)
    0000   0x14 0xf3 0xab 0x7b 0x0f                   ...{.
    body (0)

#### RECORD 9 Bolus 2015-03-27T11:49:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3,
 'duration': 0,
 'programmed': 3.3,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x10 0x00    ........
    decimal
              1    0  132    0  132    0   16    0
    datetime (2015-03-27T11:49:08)
    0000   0x08 0xf1 0x8b 0x7b 0x0f                   ...{.
    body (0)

#### RECORD 10 BasalProfileStart 2015-03-27T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-27T12:00:00)
    0000   0x00 0xc0 0x0c 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 11 BasalProfileStart 2015-03-27T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-27T15:00:00)
    0000   0x00 0xc0 0x0f 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 12 SensorAlert 2015-03-27T15:01:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-27T15:01:46)
    0000   0x2e 0xc1 0x2f 0xbb 0x0f                   ../..
    body (0)

#### RECORD 13 BolusWizard 2015-03-27T15:03:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.6,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 5.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-27T15:03:24)
    0000   0x18 0xc3 0x0f 0x7b 0x0f                   ...{.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    -P.P(Z..
    0008   0xe0 0x00 0x00 0x00 0x00 0xe0 0x78         ......x
    decimal
             45   80    0   80   40   90    0    0
            224    0    0    0    0  224  120

#### RECORD 14 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 134, 'amount': 0.1},
 {'age': 144, 'amount': 0.4},
 {'age': 154, 'amount': 0.45},
 {'age': 164, 'amount': 0.4},
 {'age': 174, 'amount': 0.4},
 {'age': 184, 'amount': 0.45},
 {'age': 194, 'amount': 3.6},
 {'age': 414, 'amount': 4.0}]
```
    op hex (26)
    0000   0x5c 0x1a 0x04 0x86 0x04 0x10 0x90 0x04    \.......
    0008   0x12 0x9a 0x04 0x10 0xa4 0x04 0x10 0xae    ........
    0010   0x04 0x12 0xb8 0x04 0x90 0xc2 0x04 0xa0    ........
    0018   0x9e 0x14                                  ..
    decimal
             92   26    4  134    4   16  144    4
             18  154    4   16  164    4   16  174
              4   18  184    4  144  194    4  160
            158   20
    datetime (unknown)

    body (0)

#### RECORD 15 Bolus 2015-03-27T15:05:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 30,
 'programmed': 2.0,
 'type': 'square',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x2c 0x01    ..P.P.,.
    decimal
              1    0   80    0   80    0   44    1
    datetime (2015-03-27T15:05:50)
    0000   0x32 0xc5 0xaf 0x7b 0x0f                   2..{.
    body (0)

#### RECORD 16 Bolus 2015-03-27T15:03:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6,
 'duration': 0,
 'programmed': 3.6,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x2c 0x00    ......,.
    decimal
              1    0  144    0  144    0   44    0
    datetime (2015-03-27T15:03:24)
    0000   0x18 0xc3 0x8f 0x7b 0x0f                   ...{.
    body (0)

#### RECORD 17 SensorAlert 2015-03-27T15:17:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 183}
```
    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-03-27T15:17:56)
    0000   0x38 0xd1 0x2f 0xbb 0x0f                   8./..
    body (0)

#### RECORD 18 Bolus 2015-03-27T15:17:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 5.1}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xcc 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  204    0
    datetime (2015-03-27T15:17:05)
    0000   0x05 0xd1 0x4f 0x7b 0x0f                   ..O{.
    body (0)

#### RECORD 19 SensorAlert 2015-03-27T18:37:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-27T18:37:56)
    0000   0x38 0xe5 0x32 0xbb 0x0f                   8.2..
    body (0)

#### RECORD 20 SensorAlert 2015-03-27T18:46:27 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-03-27T18:46:27)
    0000   0x1b 0xee 0x32 0xbb 0x0f                   ..2..
    body (0)

#### RECORD 21 SensorAlert 2015-03-27T20:16:29 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 304}
```
    op hex (3)
    0000   0x0b 0x65 0x30                             .e0
    decimal
             11  101   48
    datetime (2015-03-27T20:16:29)
    0000   0x1d 0xd0 0x34 0xbb 0x8f                   ..4..
    body (0)

#### RECORD 22 Bolus 2015-03-27T20:17:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x00 0x00    ........
    decimal
              1    0  200    0  200    0    0    0
    datetime (2015-03-27T20:17:32)
    0000   0x20 0xd1 0x54 0x7b 0x0f                    .T{.
    body (0)

#### RECORD 23 Bolus 2015-03-27T20:31:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xc8 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  200    0
    datetime (2015-03-27T20:31:49)
    0000   0x31 0xdf 0x54 0x7b 0x0f                   1.T{.
    body (0)

#### RECORD 24 SensorAlert 2015-03-27T21:39:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-27T21:39:00)
    0000   0x00 0xe7 0x35 0xbb 0x0f                   ..5..
    body (0)

#### RECORD 25 SensorAlert 2015-03-27T21:47:08 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-03-27T21:47:08)
    0000   0x08 0xef 0x35 0xbb 0x0f                   ..5..
    body (0)

#### RECORD 26 BasalProfileStart 2015-03-27T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-27T22:00:00)
    0000   0x00 0xc0 0x16 0x1b 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 27 SensorAlert 2015-03-27T22:39:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-27T22:39:00)
    0000   0x00 0xe7 0x36 0xbb 0x0f                   ..6..
    body (0)

#### RECORD 28 CalBGForPH 2015-03-27T22:58:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 280}
```
    op hex (2)
    0000   0x0a 0x18                                  ..
    decimal
             10   24
    datetime (2015-03-27T22:58:07)
    0000   0x07 0xfa 0x36 0x7b 0x8f                   ..6{.
    body (0)

#### RECORD 29 BGReceived 2015-03-27T22:58:07 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 280, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x23                                  ?#
    decimal
             63   35
    datetime (2015-03-27T22:58:07)
    0000   0x07 0xfa 0x16 0x7b 0x0f                   ...{.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 30 BolusWizard 2015-03-27T22:58:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 280,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_maybe_estimate': -2.4,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 1.8}
```
    op hex (2)
    0000   0x5b 0x18                                  [.
    decimal
             91   24
    datetime (2015-03-27T22:58:11)
    0000   0x0b 0xfa 0x16 0x1b 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0xa0 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x48 0x00 0x58 0x78         ...H.Xx
    decimal
              0   81    0  100   40   90  160    0
              0    0    0   72    0   88  120

#### RECORD 31 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 149, 'amount': 2.0},
 {'age': 159, 'amount': 2.85},
 {'age': 169, 'amount': 2.15},
 {'age': 449, 'amount': 0.55},
 {'age': 459, 'amount': 0.65},
 {'age': 469, 'amount': 3.1},
 {'age': 479, 'amount': 3.8}]
```
    op hex (23)
    0000   0x5c 0x17 0x50 0x95 0x04 0x72 0x9f 0x04    \.P..r..
    0008   0x56 0xa9 0x04 0x16 0xc1 0x14 0x1a 0xcb    V.......
    0010   0x14 0x7c 0xd5 0x14 0x98 0xdf 0x14         .|.....
    decimal
             92   23   80  149    4  114  159    4
             86  169    4   22  193   20   26  203
             20  124  213   20  152  223   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2015-03-27T22:58:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 0,
 'programmed': 0.0,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x00 0x00 0x00 0x00 0x48 0x00    ......H.
    decimal
              1    0    0    0    0    0   72    0
    datetime (2015-03-27T22:58:11)
    0000   0x0b 0xfa 0xb6 0x1b 0x0f                   .....
    body (0)

#### RECORD 33 Bolus 2015-03-27T22:58:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2,
 'duration': 0,
 'programmed': 2.2,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x48 0x00    ..X.X.H.
    decimal
              1    0   88    0   88    0   72    0
    datetime (2015-03-27T22:58:12)
    0000   0x0c 0xfa 0x96 0x1b 0x0f                   .....
    body (0)

#### RECORD 34 SensorAlert 2015-03-27T23:13:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 277}
```
    op hex (3)
    0000   0x0b 0x65 0x15                             .e.
    decimal
             11  101   21
    datetime (2015-03-27T23:13:03)
    0000   0x03 0xcd 0x37 0xbb 0x8f                   ..7..
    body (0)

#### RECORD 35 BasalProfileStart 2015-03-28T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-28T00:00:00)
    0000   0x00 0xc0 0x00 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 36 MResultTotals 2015-03-28T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x07 0x91                   .....
    decimal
              7    0    0    7  145
    datetime (2015-03-28T00:00:00)
    0000   0x3b 0x8f                                  ;.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 37 Sara6E 2015-03-28T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-28T00:00:00)
    0000   0x3b 0x8f                                  ;.
    body (49)
    hex
    0000   0x05 0x10 0xe2 0xab 0x18 0x02 0x00 0x00    ........
    0008   0x07 0x91 0x03 0x05 0x28 0x04 0x8c 0x3c    ....(..<
    0010   0x00 0x84 0x02 0x68 0x00 0x58 0x00 0x00    ...h.X..
    0018   0x01 0xcc 0x03 0x01 0x00 0x05 0x00 0xb7    ........
    0020   0x34 0x30 0x00 0x1a 0x36 0x05 0x00 0x00    40..6...
    0028   0x00 0x00 0x0a 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  226  171   24    2    0    0
              7  145    3    5   40    4  140   60
              0  132    2  104    0   88    0    0
              1  204    3    1    0    5    0  183
             52   48    0   26   54    5    0    0
              0    0   10    1    0    0    0    0
              0

#### RECORD 38 SensorAlert 2015-03-28T00:42:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 325}
```
    op hex (3)
    0000   0x0b 0x65 0x45                             .eE
    decimal
             11  101   69
    datetime (2015-03-28T00:42:44)
    0000   0x2c 0xea 0x20 0xbc 0x8f                   ,. ..
    body (0)

#### RECORD 39 Bolus 2015-03-28T00:54:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x28 0x00    ..d.d.(.
    decimal
              1    0  100    0  100    0   40    0
    datetime (2015-03-28T00:54:32)
    0000   0x20 0xf6 0x40 0x7c 0x0f                    .@|.
    body (0)

#### RECORD 40 SensorAlert 2015-03-28T02:12:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 315}
```
    op hex (3)
    0000   0x0b 0x65 0x3b                             .e;
    decimal
             11  101   59
    datetime (2015-03-28T02:12:35)
    0000   0x23 0xcc 0x22 0xbc 0x8f                   #."..
    body (0)

#### RECORD 41 SensorAlert 2015-03-28T03:41:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 365}
```
    op hex (3)
    0000   0x0b 0x65 0x6d                             .em
    decimal
             11  101  109
    datetime (2015-03-28T03:41:46)
    0000   0x2e 0xe9 0x23 0xbc 0x8f                   ..#..
    body (0)

#### RECORD 42 BasalProfileStart 2015-03-28T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-28T04:00:00)
    0000   0x00 0xc0 0x04 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 43 SensorAlert 2015-03-28T05:13:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 380}
```
    op hex (3)
    0000   0x0b 0x65 0x7c                             .e|
    decimal
             11  101  124
    datetime (2015-03-28T05:13:03)
    0000   0x03 0xcd 0x25 0xbc 0x8f                   ..%..
    body (0)

#### RECORD 44 LowReservoir 2015-03-28T06:33:09 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-03-28T06:33:09)
    0000   0x09 0xe1 0x06 0x1c 0x0f                   .....
    body (0)

#### RECORD 45 SensorAlert 2015-03-28T06:42:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 386}
```
    op hex (3)
    0000   0x0b 0x65 0x82                             .e.
    decimal
             11  101  130
    datetime (2015-03-28T06:42:44)
    0000   0x2c 0xea 0x26 0xbc 0x8f                   ,.&..
    body (0)

#### RECORD 46 BasalProfileStart 2015-03-28T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-28T07:00:00)
    0000   0x00 0xc0 0x07 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 47 SensorAlert 2015-03-28T08:12:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 348}
```
    op hex (3)
    0000   0x0b 0x65 0x5c                             .e\
    decimal
             11  101   92
    datetime (2015-03-28T08:12:35)
    0000   0x23 0xcc 0x28 0xbc 0x8f                   #.(..
    body (0)

#### RECORD 48 Bolus 2015-03-28T08:31:45 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x00 0x00    ........
    decimal
              1    0  200    0  200    0    0    0
    datetime (2015-03-28T08:31:45)
    0000   0x2d 0xdf 0x48 0x7c 0x0f                   -.H|.
    body (0)

#### RECORD 49 LowReservoir 2015-03-28T09:04:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-03-28T09:04:03)
    0000   0x03 0xc4 0x09 0x1c 0x0f                   .....
    body (0)

#### RECORD 50 Bolus 2015-03-28T09:02:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 4.8}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0xc0 0x00    ........
    decimal
              1    0  200    0  200    0  192    0
    datetime (2015-03-28T09:02:09)
    0000   0x09 0xc2 0x49 0x7c 0x0f                   ..I|.
    body (0)

#### RECORD 51 SensorAlert 2015-03-28T09:41:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 191}
```
    op hex (3)
    0000   0x0b 0x65 0xbf                             .e.
    decimal
             11  101  191
    datetime (2015-03-28T09:41:46)
    0000   0x2e 0xe9 0x29 0xbc 0x0f                   ..)..
    body (0)

#### RECORD 52 SensorAlert 2015-03-28T09:57:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-28T09:57:56)
    0000   0x38 0xf9 0x29 0xbc 0x0f                   8.)..
    body (0)

#### RECORD 53 SensorAlert 2015-03-28T09:58:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-28T09:58:00)
    0000   0x00 0xfa 0x29 0xbc 0x0f                   ..)..
    body (0)

#### RECORD 54 BasalProfileStart 2015-03-28T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-28T10:00:00)
    0000   0x00 0xc0 0x0a 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 55 SensorAlert 2015-03-28T10:21:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 77}
```
    op hex (3)
    0000   0x0b 0x66 0x4d                             .fM
    decimal
             11  102   77
    datetime (2015-03-28T10:21:46)
    0000   0x2e 0xd5 0x2a 0xbc 0x0f                   ..*..
    body (0)

#### RECORD 56 SensorAlert 2015-03-28T10:58:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-28T10:58:00)
    0000   0x00 0xfa 0x2a 0xbc 0x0f                   ..*..
    body (0)

#### RECORD 57 SensorAlert 2015-03-28T11:28:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-28T11:28:00)
    0000   0x00 0xdc 0x2b 0xbc 0x0f                   ..+..
    body (0)

#### RECORD 58 SensorAlert 2015-03-28T11:58:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-28T11:58:00)
    0000   0x00 0xfa 0x2b 0xbc 0x0f                   ..+..
    body (0)

#### RECORD 59 CalBGForPH 2015-03-28T11:58:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2015-03-28T11:58:45)
    0000   0x2d 0xfa 0x2b 0x7c 0x0f                   -.+|.
    body (0)

#### RECORD 60 BGReceived 2015-03-28T11:58:45 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 161, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2015-03-28T11:58:45)
    0000   0x2d 0xfa 0x2b 0x7c 0x0f                   -.+|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 61 BasalProfileStart 2015-03-28T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-28T12:00:00)
    0000   0x00 0xc0 0x0c 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 62 SensorAlert 2015-03-28T12:12:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-28T12:12:35)
    0000   0x23 0xcc 0x2c 0xbc 0x0f                   #.,..
    body (0)

#### RECORD 63 Bolus 2015-03-28T12:12:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x2c 0x00    ..<.<.,.
    decimal
              1    0   60    0   60    0   44    0
    datetime (2015-03-28T12:12:47)
    0000   0x2f 0xcc 0x4c 0x7c 0x0f                   /.L|.
    body (0)

#### RECORD 64 SensorAlert 2015-03-28T13:53:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-28T13:53:03)
    0000   0x03 0xf5 0x2d 0xbc 0x0f                   ..-..
    body (0)

#### RECORD 65 SensorAlert 2015-03-28T14:02:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-28T14:02:44)
    0000   0x2c 0xc2 0x2e 0xbc 0x0f                   ,....
    body (0)

#### RECORD 66 BasalProfileStart 2015-03-28T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-28T15:00:00)
    0000   0x00 0xc0 0x0f 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 67 SensorAlert 2015-03-28T15:32:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 218}
```
    op hex (3)
    0000   0x0b 0x65 0xda                             .e.
    decimal
             11  101  218
    datetime (2015-03-28T15:32:35)
    0000   0x23 0xe0 0x2f 0xbc 0x0f                   #./..
    body (0)

#### RECORD 68 Bolus 2015-03-28T15:32:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x08 0x00    ..(.(...
    decimal
              1    0   40    0   40    0    8    0
    datetime (2015-03-28T15:32:46)
    0000   0x2e 0xe0 0x4f 0x7c 0x0f                   ..O|.
    body (0)

#### RECORD 69 PumpSuspend 2015-03-28T15:33:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-28T15:33:29)
    0000   0x1d 0xe1 0x0f 0x1c 0x0f                   .....
    body (0)

#### RECORD 70 BasalProfileStart 2015-03-28T16:00:04 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-28T16:00:04)
    0000   0x04 0xc0 0x10 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 71 PumpResume 2015-03-28T16:00:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-28T16:00:04)
    0000   0x04 0xc0 0x10 0x1c 0x0f                   .....
    body (0)

#### RECORD 72 Bolus 2015-03-28T16:00:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x2c 0x00    ..P.P.,.
    decimal
              1    0   80    0   80    0   44    0
    datetime (2015-03-28T16:00:15)
    0000   0x0f 0xc0 0x50 0x7c 0x0f                   ..P|.
    body (0)

#### RECORD 73 SensorAlert 2015-03-28T17:01:46 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 283}
```
    op hex (3)
    0000   0x0b 0x65 0x1b                             .e.
    decimal
             11  101   27
    datetime (2015-03-28T17:01:46)
    0000   0x2e 0xc1 0x31 0xbc 0x8f                   ..1..
    body (0)

#### RECORD 74 Bolus 2015-03-28T17:02:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 2.3}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x5c 0x00    ......\.
    decimal
              1    0  200    0  200    0   92    0
    datetime (2015-03-28T17:02:12)
    0000   0x0c 0xc2 0x51 0x7c 0x0f                   ..Q|.
    body (0)

#### RECORD 75 SensorAlert 2015-03-28T18:33:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 197}
```
    op hex (3)
    0000   0x0b 0x65 0xc5                             .e.
    decimal
             11  101  197
    datetime (2015-03-28T18:33:03)
    0000   0x03 0xe1 0x32 0xbc 0x0f                   ..2..
    body (0)

#### RECORD 76 BolusWizard 2015-03-28T19:38:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.2,
 'carb_input': 70,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 11.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-28T19:38:21)
    0000   0x15 0xe6 0x13 0x7c 0x0f                   ...|.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    FP.<(Z..
    0008   0xd0 0x00 0x00 0x00 0x01 0xd0 0x78         ......x
    decimal
             70   80    0   60   40   90    0    1
            208    0    0    0    1  208  120

#### RECORD 77 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 159, 'amount': 5.0},
 {'age': 219, 'amount': 2.0},
 {'age': 249, 'amount': 1.0},
 {'age': 449, 'amount': 1.5}]
```
    op hex (14)
    0000   0x5c 0x0e 0xc8 0x9f 0x04 0x50 0xdb 0x04    \....P..
    0008   0x28 0xf9 0x04 0x3c 0xc1 0x14              (..<..
    decimal
             92   14  200  159    4   80  219    4
             40  249    4   60  193   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2015-03-28T19:38:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.0,
 'duration': 330,
 'programmed': 0.2,
 'type': 'square',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x01 0x08 0x00 0x00 0x00 0x3c 0x0b    ......<.
    decimal
              1    1    8    0    0    0   60   11
    datetime (2015-03-28T19:38:21)
    0000   0x15 0xe6 0xb3 0x7c 0x0f                   ...|.
    body (0)

#### RECORD 79 Bolus 2015-03-28T19:38:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0x7c 0x00 0x3c 0x00    ....|.<.
    decimal
              1    0  200    0  124    0   60    0
    datetime (2015-03-28T19:38:21)
    0000   0x15 0xe6 0x93 0x7c 0x0f                   ...|.
    body (0)

#### RECORD 80 NoDelivery 2015-03-28T19:40:27 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-28T19:40:27)
    0000   0x1b 0xe8 0x53 0x5c 0x0f                   ..S\.
    body (0)

#### RECORD 81 ClearAlarm 2015-03-28T19:40:39 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-28T19:40:39)
    0000   0x27 0xe8 0x13 0x1c 0x0f                   '....
    body (0)

#### RECORD 82 Rewind 2015-03-28T19:40:45 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-03-28T19:40:45)
    0000   0x2d 0xe8 0x13 0x1c 0x0f                   -....
    body (0)

#### RECORD 83 Prime 2015-03-28T19:48:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 6.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x44                   ....D
    decimal
              3    0    0    0   68
    datetime (2015-03-28T19:48:19)
    0000   0x13 0xf0 0x33 0x1c 0x0f                   ..3..
    body (0)

#### RECORD 84 BasalProfileStart 2015-03-28T19:50:17 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-28T19:50:17)
    0000   0x11 0xf2 0x13 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 85 Prime 2015-03-28T19:50:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-03-28T19:50:03)
    0000   0x03 0xf2 0x13 0x1c 0x0f                   .....
    body (0)

#### RECORD 86 BolusWizard 2015-03-28T19:56:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-28T19:56:13)
    0000   0x0d 0xf8 0x13 0x7c 0x0f                   ...|.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0   60   40   90    0    0
              0    0    0    0    0    0  120

#### RECORD 87 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 2.1},
 {'age': 27, 'amount': 1.0},
 {'age': 177, 'amount': 5.0},
 {'age': 237, 'amount': 2.0},
 {'age': 267, 'amount': 1.0},
 {'age': 467, 'amount': 1.5}]
```
    op hex (20)
    0000   0x5c 0x14 0x54 0x11 0x04 0x28 0x1b 0x04    \.T..(..
    0008   0xc8 0xb1 0x04 0x50 0xed 0x04 0x28 0x0b    ...P..(.
    0010   0x14 0x3c 0xd3 0x14                        .<..
    decimal
             92   20   84   17    4   40   27    4
            200  177    4   80  237    4   40   11
             20   60  211   20
    datetime (unknown)

    body (0)

#### RECORD 88 Bolus 2015-03-28T19:56:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.0,
 'duration': 270,
 'programmed': 6.0,
 'type': 'square',
 'unabsorbed': 4.1}
```
    op hex (8)
    0000   0x01 0x00 0xf0 0x00 0xf0 0x00 0xa4 0x09    ........
    decimal
              1    0  240    0  240    0  164    9
    datetime (2015-03-28T19:56:53)
    0000   0x35 0xf8 0xb3 0x7c 0x0f                   5..|.
    body (0)

#### RECORD 89 Bolus 2015-03-28T19:56:13 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 4.1}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xa4 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  164    0
    datetime (2015-03-28T19:56:13)
    0000   0x0d 0xf8 0x93 0x7c 0x0f                   ...|.
    body (0)

#### RECORD 90 SensorAlert 2015-03-28T20:02:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 310}
```
    op hex (3)
    0000   0x0b 0x65 0x36                             .e6
    decimal
             11  101   54
    datetime (2015-03-28T20:02:44)
    0000   0x2c 0xc2 0x34 0xbc 0x8f                   ,.4..
    body (0)

#### RECORD 91 Base unknown head[2], body[0] op[0x00]

    op hex (2)
    0000   0x00 0xb7                                  ..
    decimal
              0  183
    datetime (unknown)

    body (0)

`end ReadHistoryData-page-1.data: 92 records`
