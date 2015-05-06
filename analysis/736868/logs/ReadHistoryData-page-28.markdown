## START ReadHistoryData-page-28.data
#### STOPPING DOUBLE NULLS @ 1011, found 11 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa5 0x71                                  .q
##### DEBUG DECIMAL
            165  113
#### RECORD 0 Bolus 2015-02-14T20:37:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x38 0x00    ......8.
    decimal
              1    0  160    0  160    0   56    0
    datetime (2015-02-14T20:37:04)
    0000   0x04 0xa5 0x94 0x6e 0x0f                   ...n.
    body (0)

#### RECORD 1 SensorAlert 2015-02-14T20:44:56 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-14T20:44:56)
    0000   0x38 0xac 0x34 0xae 0x0f                   8.4..
    body (0)

#### RECORD 2 SensorAlert 2015-02-14T21:01:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 182}
```
    op hex (3)
    0000   0x0b 0x65 0xb6                             .e.
    decimal
             11  101  182
    datetime (2015-02-14T21:01:30)
    0000   0x1e 0x81 0x35 0xae 0x0f                   ..5..
    body (0)

#### RECORD 3 SensorAlert 2015-02-14T21:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-14T21:36:00)
    0000   0x00 0xa4 0x35 0xae 0x0f                   ..5..
    body (0)

#### RECORD 4 CalBGForPH 2015-02-14T21:39:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2015-02-14T21:39:40)
    0000   0x28 0xa7 0x35 0x6e 0x0f                   (.5n.
    body (0)

#### RECORD 5 BGReceived 2015-02-14T21:39:40 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 202, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2015-02-14T21:39:40)
    0000   0x28 0xa7 0x55 0x6e 0x0f                   (.Un.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 6 Bolus 2015-02-14T21:40:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 5.2}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xd0 0x00    ..(.(...
    decimal
              1    0   40    0   40    0  208    0
    datetime (2015-02-14T21:40:09)
    0000   0x09 0xa8 0x55 0x6e 0x0f                   ..Un.
    body (0)

#### RECORD 7 Bolus 2015-02-14T21:47:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 6.1}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0xf4 0x00    ........
    decimal
              1    0  140    0  140    0  244    0
    datetime (2015-02-14T21:47:19)
    0000   0x13 0xaf 0x55 0x6e 0x0f                   ..Un.
    body (0)

#### RECORD 8 SensorAlert 2015-02-14T21:54:54 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 187}
```
    op hex (3)
    0000   0x0b 0x65 0xbb                             .e.
    decimal
             11  101  187
    datetime (2015-02-14T21:54:54)
    0000   0x36 0xb6 0x35 0xae 0x0f                   6.5..
    body (0)

#### RECORD 9 BasalProfileStart 2015-02-14T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-14T22:00:00)
    0000   0x00 0x80 0x16 0x0e 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 10 SensorAlert 2015-02-14T23:41:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-14T23:41:30)
    0000   0x1e 0xa9 0x37 0xae 0x0f                   ..7..
    body (0)

#### RECORD 11 PumpSuspend 2015-02-14T23:56:53 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-14T23:56:53)
    0000   0x35 0xb8 0x17 0x0e 0x0f                   5....
    body (0)

#### RECORD 12 MResultTotals 2015-02-15T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0x5e                   ....^
    decimal
              7    0    0   10   94
    datetime (2015-02-15T00:00:00)
    0000   0x2e 0x0f                                  ..
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 13 Sara6E 2015-02-15T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-15T00:00:00)
    0000   0x2e 0x0f                                  ..
    body (49)
    hex
    0000   0x05 0x00 0xcf 0xbd 0xe5 0x03 0x00 0x00    ........
    0008   0x0a 0x5e 0x03 0x1a 0x1e 0x07 0x44 0x46    .^....DF
    0010   0x00 0x96 0x03 0x2c 0x01 0x98 0x00 0x00    ...,....
    0018   0x02 0x80 0x03 0x03 0x00 0x06 0x00 0xd6    ........
    0020   0x3b 0x29 0x00 0xf1 0x56 0x03 0x00 0x00    ;)..V...
    0028   0x00 0x00 0x0a 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  207  189  229    3    0    0
             10   94    3   26   30    7   68   70
              0  150    3   44    1  152    0    0
              2  128    3    3    0    6    0  214
             59   41    0  241   86    3    0    0
              0    0   10    0    0    0    0    0
              0

#### RECORD 14 BasalProfileStart 2015-02-15T00:10:34 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-15T00:10:34)
    0000   0x22 0x8a 0x00 0x0f 0x0f                   "....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 15 PumpResume 2015-02-15T00:10:34 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-15T00:10:34)
    0000   0x22 0x8a 0x00 0x0f 0x0f                   "....
    body (0)

#### RECORD 16 SensorAlert 2015-02-15T01:01:30 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 181}
```
    op hex (3)
    0000   0x0b 0x65 0xb5                             .e.
    decimal
             11  101  181
    datetime (2015-02-15T01:01:30)
    0000   0x1e 0x81 0x21 0xaf 0x0f                   ..!..
    body (0)

#### RECORD 17 BasalProfileStart 2015-02-15T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-15T04:00:00)
    0000   0x00 0x80 0x04 0x0f 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 18 SensorAlert 2015-02-15T04:01:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 348}
```
    op hex (3)
    0000   0x0b 0x65 0x5c                             .e\
    decimal
             11  101   92
    datetime (2015-02-15T04:01:01)
    0000   0x01 0x81 0x24 0xaf 0x8f                   ..$..
    body (0)

#### RECORD 19 Bolus 2015-02-15T04:12:52 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6,
 'duration': 0,
 'programmed': 0.6,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x18 0x01 0x18 0x00 0x00 0x00    ........
    decimal
              1    1   24    1   24    0    0    0
    datetime (2015-02-15T04:12:52)
    0000   0x34 0x8c 0x44 0x6f 0x0f                   4.Do.
    body (0)

#### RECORD 20 Bolus 2015-02-15T04:19:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x01 0x18 0x00    ..<.<...
    decimal
              1    0   60    0   60    1   24    0
    datetime (2015-02-15T04:19:14)
    0000   0x0e 0x93 0x44 0x6f 0x0f                   ..Do.
    body (0)

#### RECORD 21 SensorAlert 2015-02-15T05:30:12 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 226}
```
    op hex (3)
    0000   0x0b 0x65 0xe2                             .e.
    decimal
             11  101  226
    datetime (2015-02-15T05:30:12)
    0000   0x0c 0x9e 0x25 0xaf 0x0f                   ..%..
    body (0)

#### RECORD 22 BasalProfileStart 2015-02-15T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-15T07:00:00)
    0000   0x00 0x80 0x07 0x0f 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 23 SensorAlert 2015-02-15T08:39:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-15T08:39:00)
    0000   0x00 0xa7 0x28 0xaf 0x0f                   ..(..
    body (0)

#### RECORD 24 BolusWizard 2015-02-15T09:11:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.5,
 'carb_input': 25,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 2.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-15T09:11:08)
    0000   0x08 0x8b 0x09 0x6f 0x0f                   ...o.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    .P.d(Z..
    0008   0x64 0x00 0x00 0x00 0x00 0x64 0x78         d....dx
    decimal
             25   80    0  100   40   90    0    0
            100    0    0    0    0  100  120

#### RECORD 25 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 295, 'amount': 3.9}, {'age': 305, 'amount': 4.6}]
```
    op hex (8)
    0000   0x5c 0x08 0x9c 0x27 0x14 0xb8 0x31 0x14    \..'..1.
    decimal
             92    8  156   39   20  184   49   20
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2015-02-15T09:11:08 head[8], body[0] op[0x01]
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
    datetime (2015-02-15T09:11:08)
    0000   0x08 0x8b 0x49 0x6f 0x0f                   ..Io.
    body (0)

#### RECORD 27 SensorAlert 2015-02-15T09:39:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-15T09:39:00)
    0000   0x00 0xa7 0x29 0xaf 0x0f                   ..)..
    body (0)

#### RECORD 28 BasalProfileStart 2015-02-15T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-15T10:00:00)
    0000   0x00 0x80 0x0a 0x0f 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 29 SensorAlert 2015-02-15T10:09:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-15T10:09:00)
    0000   0x00 0x89 0x2a 0xaf 0x0f                   ..*..
    body (0)

#### RECORD 30 CalBGForPH 2015-02-15T10:09:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 181}
```
    op hex (2)
    0000   0x0a 0xb5                                  ..
    decimal
             10  181
    datetime (2015-02-15T10:09:58)
    0000   0x3a 0x89 0x2a 0x6f 0x0f                   :.*o.
    body (0)

#### RECORD 31 BGReceived 2015-02-15T10:09:58 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 181, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2015-02-15T10:09:58)
    0000   0x3a 0x89 0xaa 0x6f 0x0f                   :..o.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 32 BolusWizard 2015-02-15T10:10:15 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 181,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.1,
 'carb_input': 31,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 1.5,
 'food_estimate': 3.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 2.0}
```
    op hex (2)
    0000   0x5b 0xb5                                  [.
    decimal
             91  181
    datetime (2015-02-15T10:10:15)
    0000   0x0f 0x8a 0x0a 0x6f 0x0f                   ...o.
    body (15)
    hex
    0000   0x1f 0x50 0x00 0x64 0x28 0x5a 0x3c 0x00    .P.d(Z<.
    0008   0x7c 0x00 0x00 0x50 0x00 0x7c 0x78         |..P.|x
    decimal
             31   80    0  100   40   90   60    0
            124    0    0   80    0  124  120

#### RECORD 33 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 2.5},
 {'age': 354, 'amount': 3.9},
 {'age': 364, 'amount': 4.6}]
```
    op hex (11)
    0000   0x5c 0x0b 0x64 0x40 0x04 0x9c 0x62 0x14    \.d@..b.
    0008   0xb8 0x6c 0x14                             .l.
    decimal
             92   11  100   64    4  156   98   20
            184  108   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2015-02-15T10:10:15 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1,
 'duration': 0,
 'programmed': 3.1,
 'type': 'normal',
 'unabsorbed': 2.0}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x50 0x00    ..|.|.P.
    decimal
              1    0  124    0  124    0   80    0
    datetime (2015-02-15T10:10:15)
    0000   0x0f 0x8a 0x4a 0x6f 0x0f                   ..Jo.
    body (0)

#### RECORD 35 SensorAlert 2015-02-15T10:26:22 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-15T10:26:22)
    0000   0x16 0x9a 0x2a 0xaf 0x0f                   ..*..
    body (0)

#### RECORD 36 BolusWizard 2015-02-15T10:26:39 head[2], body[15] op[0x5b]
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
    datetime (2015-02-15T10:26:39)
    0000   0x27 0x9a 0x0a 0x6f 0x0f                   '..o.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    .P.d(Z..
    0008   0x78 0x00 0x00 0x00 0x00 0x78 0x78         x....xx
    decimal
             30   80    0  100   40   90    0    0
            120    0    0    0    0  120  120

#### RECORD 37 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 3.1},
 {'age': 80, 'amount': 2.5},
 {'age': 370, 'amount': 3.9},
 {'age': 380, 'amount': 4.6}]
```
    op hex (14)
    0000   0x5c 0x0e 0x7c 0x14 0x04 0x64 0x50 0x04    \.|..dP.
    0008   0x9c 0x72 0x14 0xb8 0x7c 0x14              .r..|.
    decimal
             92   14  124   20    4  100   80    4
            156  114   20  184  124   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2015-02-15T10:26:39 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 4.8}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0xc0 0x00    ..x.x...
    decimal
              1    0  120    0  120    0  192    0
    datetime (2015-02-15T10:26:39)
    0000   0x27 0x9a 0x4a 0x6f 0x0f                   '.Jo.
    body (0)

#### RECORD 39 Bolus 2015-02-15T11:01:29 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x01 0x0c 0x00    ..(.(...
    decimal
              1    0   40    0   40    1   12    0
    datetime (2015-02-15T11:01:29)
    0000   0x1d 0x81 0x4b 0x6f 0x0f                   ..Ko.
    body (0)

#### RECORD 40 BasalProfileStart 2015-02-15T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-15T12:00:00)
    0000   0x00 0x80 0x0c 0x0f 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 41 SensorAlert 2015-02-15T12:44:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Sensor End'}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-02-15T12:44:55)
    0000   0x37 0xac 0x2c 0xaf 0x0f                   7.,..
    body (0)

#### RECORD 42 Bolus 2015-02-15T13:53:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x20 0x00    ...... .
    decimal
              1    0  160    0  160    0   32    0
    datetime (2015-02-15T13:53:11)
    0000   0x0b 0xb5 0x4d 0x6f 0x0f                   ..Mo.
    body (0)

#### RECORD 43 BasalProfileStart 2015-02-15T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-15T15:00:00)
    0000   0x00 0x80 0x0f 0x0f 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 44 BolusWizard 2015-02-15T16:36:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 1.1,
 'carb_input': 60,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 7.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-15T16:36:22)
    0000   0x16 0xa4 0x10 0x6f 0x0f                   ...o.
    body (15)
    hex
    0000   0x3c 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    <P.P(Z..
    0008   0x2c 0x00 0x00 0x00 0x01 0x2c 0x78         ,....,x
    decimal
             60   80    0   80   40   90    0    1
             44    0    0    0    1   44  120

#### RECORD 45 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 170, 'amount': 4.0},
 {'age': 340, 'amount': 1.0},
 {'age': 370, 'amount': 3.0},
 {'age': 390, 'amount': 3.1},
 {'age': 450, 'amount': 2.5}]
```
    op hex (17)
    0000   0x5c 0x11 0xa0 0xaa 0x04 0x28 0x54 0x14    \....(T.
    0008   0x78 0x72 0x14 0x7c 0x86 0x14 0x64 0xc2    xr.|..d.
    0010   0x14                                       .
    decimal
             92   17  160  170    4   40   84   20
            120  114   20  124  134   20  100  194
             20
    datetime (unknown)

    body (0)

#### RECORD 46 Bolus 2015-02-15T16:39:53 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3,
 'duration': 60,
 'programmed': 2.3,
 'type': 'square',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x24 0x02    ..\.\.$.
    decimal
              1    0   92    0   92    0   36    2
    datetime (2015-02-15T16:39:53)
    0000   0x35 0xa7 0xb0 0x6f 0x0f                   5..o.
    body (0)

#### RECORD 47 Bolus 2015-02-15T16:36:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.2,
 'duration': 0,
 'programmed': 5.2,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0xd0 0x00 0xd0 0x00 0x24 0x00    ......$.
    decimal
              1    0  208    0  208    0   36    0
    datetime (2015-02-15T16:36:22)
    0000   0x16 0xa4 0x90 0x6f 0x0f                   ...o.
    body (0)

#### RECORD 48 Bolus 2015-02-15T17:53:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 5.8}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xe8 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  232    0
    datetime (2015-02-15T17:53:17)
    0000   0x11 0xb5 0x51 0x6f 0x0f                   ..Qo.
    body (0)

#### RECORD 49 BolusWizard 2015-02-15T21:20:39 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.2,
 'carb_input': 40,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 6.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-15T21:20:39)
    0000   0x27 0x94 0x15 0x6f 0x0f                   '..o.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    (P.<(Z..
    0008   0x08 0x00 0x00 0x00 0x01 0x08 0x78         ......x
    decimal
             40   80    0   60   40   90    0    1
              8    0    0    0    1    8  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 214, 'amount': 2.5},
 {'age': 224, 'amount': 0.15},
 {'age': 234, 'amount': 0.4},
 {'age': 244, 'amount': 0.35},
 {'age': 254, 'amount': 0.4},
 {'age': 264, 'amount': 0.4},
 {'age': 274, 'amount': 0.35},
 {'age': 284, 'amount': 5.45},
 {'age': 454, 'amount': 4.0}]
```
    op hex (29)
    0000   0x5c 0x1d 0x64 0xd6 0x04 0x06 0xe0 0x04    \.d.....
    0008   0x10 0xea 0x04 0x0e 0xf4 0x04 0x10 0xfe    ........
    0010   0x04 0x10 0x08 0x14 0x0e 0x12 0x14 0xda    ........
    0018   0x1c 0x14 0xa0 0xc6 0x14                   .....
    decimal
             92   29  100  214    4    6  224    4
             16  234    4   14  244    4   16  254
              4   16    8   20   14   18   20  218
             28   20  160  198   20
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2015-02-15T21:23:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1,
 'duration': 90,
 'programmed': 3.1,
 'type': 'square',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x0c 0x03    ..|.|...
    decimal
              1    0  124    0  124    0   12    3
    datetime (2015-02-15T21:23:00)
    0000   0x00 0x97 0xb5 0x6f 0x0f                   ...o.
    body (0)

#### RECORD 52 Bolus 2015-02-15T21:20:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x0c 0x00    ........
    decimal
              1    0  140    0  140    0   12    0
    datetime (2015-02-15T21:20:40)
    0000   0x28 0x94 0x95 0x6f 0x0f                   (..o.
    body (0)

#### RECORD 53 BasalProfileStart 2015-02-15T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-15T22:00:00)
    0000   0x00 0x80 0x16 0x0f 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 54 Bolus 2015-02-15T22:23:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 4.7}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xbc 0x00    ........
    decimal
              1    0  160    0  160    0  188    0
    datetime (2015-02-15T22:23:21)
    0000   0x15 0x97 0x56 0x6f 0x0f                   ..Vo.
    body (0)

#### RECORD 55 BasalProfileStart 2015-02-16T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-16T00:00:00)
    0000   0x00 0x80 0x00 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 56 MResultTotals 2015-02-16T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0xd5                   .....
    decimal
              7    0    0    9  213
    datetime (2015-02-16T00:00:00)
    0000   0x2f 0x0f                                  /.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 57 Sara6E 2015-02-16T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-16T00:00:00)
    0000   0x2f 0x0f                                  /.
    body (49)
    hex
    0000   0x05 0x00 0xb5 0xb5 0xb5 0x01 0x00 0x00    ........
    0008   0x09 0xd5 0x03 0x29 0x20 0x06 0xac 0x44    ...) ..D
    0010   0x00 0xba 0x03 0x8c 0x00 0x00 0x00 0x00    ........
    0018   0x03 0x20 0x05 0x00 0x00 0x06 0x00 0xcf    . ......
    0020   0x2f 0x35 0x00 0x90 0x4d 0x00 0x00 0x00    /5..M...
    0028   0x00 0x00 0x04 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  181  181  181    1    0    0
              9  213    3   41   32    6  172   68
              0  186    3  140    0    0    0    0
              3   32    5    0    0    6    0  207
             47   53    0  144   77    0    0    0
              0    0    4    0    0    0    0    0
              0

#### RECORD 58 CalBGForPH 2015-02-16T00:10:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 238}
```
    op hex (2)
    0000   0x0a 0xee                                  ..
    decimal
             10  238
    datetime (2015-02-16T00:10:56)
    0000   0x38 0x8a 0x20 0x70 0x0f                   8. p.
    body (0)

#### RECORD 59 BGReceived 2015-02-16T00:10:56 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 238, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2015-02-16T00:10:56)
    0000   0x38 0x8a 0xc0 0x70 0x0f                   8..p.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 60 Bolus 2015-02-16T00:11:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 4.0}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xa0 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  160    0
    datetime (2015-02-16T00:11:36)
    0000   0x24 0x8b 0x40 0x70 0x0f                   $.@p.
    body (0)

#### RECORD 61 BolusWizard 2015-02-16T03:37:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.8,
 'carb_input': 38,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 0.0,
 'food_estimate': 3.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-16T03:37:09)
    0000   0x09 0xa5 0x03 0x70 0x0f                   ...p.
    body (15)
    hex
    0000   0x26 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    &P.d(Z..
    0008   0x98 0x00 0x00 0x00 0x00 0x98 0x78         ......x
    decimal
             38   80    0  100   40   90    0    0
            152    0    0    0    0  152  120

#### RECORD 62 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 2.0},
 {'age': 291, 'amount': 0.3},
 {'age': 301, 'amount': 0.35},
 {'age': 311, 'amount': 0.45},
 {'age': 321, 'amount': 4.15},
 {'age': 331, 'amount': 0.35},
 {'age': 341, 'amount': 0.35},
 {'age': 351, 'amount': 0.35},
 {'age': 361, 'amount': 0.35},
 {'age': 371, 'amount': 0.35},
 {'age': 381, 'amount': 3.6}]
```
    op hex (35)
    0000   0x5c 0x23 0x50 0xd3 0x04 0x0c 0x23 0x14    \#P...#.
    0008   0x0e 0x2d 0x14 0x12 0x37 0x14 0xa6 0x41    .-..7..A
    0010   0x14 0x0e 0x4b 0x14 0x0e 0x55 0x14 0x0e    ..K..U..
    0018   0x5f 0x14 0x0e 0x69 0x14 0x0e 0x73 0x14    _..i..s.
    0020   0x90 0x7d 0x14                             .}.
    decimal
             92   35   80  211    4   12   35   20
             14   45   20   18   55   20  166   65
             20   14   75   20   14   85   20   14
             95   20   14  105   20   14  115   20
            144  125   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2015-02-16T03:39:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.8,
 'duration': 120,
 'programmed': 2.8,
 'type': 'square',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x70 0x00 0x70 0x00 0x08 0x04    ..p.p...
    decimal
              1    0  112    0  112    0    8    4
    datetime (2015-02-16T03:39:09)
    0000   0x09 0xa7 0xa3 0x70 0x0f                   ...p.
    body (0)

#### RECORD 64 Bolus 2015-02-16T03:37:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x08 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    8    0
    datetime (2015-02-16T03:37:09)
    0000   0x09 0xa5 0x83 0x70 0x0f                   ...p.
    body (0)

#### RECORD 65 BasalProfileStart 2015-02-16T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-16T04:00:00)
    0000   0x00 0x80 0x04 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 66 BasalProfileStart 2015-02-16T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-16T07:00:00)
    0000   0x00 0x80 0x07 0x10 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 67 LowReservoir 2015-02-16T07:01:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-02-16T07:01:45)
    0000   0x2d 0x81 0x07 0x10 0x0f                   -....
    body (0)

#### RECORD 68 CalBGForPH 2015-02-16T08:48:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 226}
```
    op hex (2)
    0000   0x0a 0xe2                                  ..
    decimal
             10  226
    datetime (2015-02-16T08:48:36)
    0000   0x24 0xb0 0x28 0x70 0x0f                   $.(p.
    body (0)

#### RECORD 69 BGReceived 2015-02-16T08:48:36 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 226, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x1c                                  ?.
    decimal
             63   28
    datetime (2015-02-16T08:48:36)
    0000   0x24 0xb0 0x48 0x70 0x0f                   $.Hp.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 70 BolusWizard 2015-02-16T08:48:43 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 226,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.5,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_maybe_estimate': 2.6,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0xe2                                  [.
    decimal
             91  226
    datetime (2015-02-16T08:48:43)
    0000   0x2b 0xb0 0x08 0x70 0x0f                   +..p.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x68 0x00    .P.d(Zh.
    0008   0x00 0x00 0x00 0x04 0x00 0x64 0x78         .....dx
    decimal
              0   80    0  100   40   90  104    0
              0    0    0    4    0  100  120

#### RECORD 71 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 192, 'amount': 0.05},
 {'age': 202, 'amount': 0.25},
 {'age': 212, 'amount': 0.25},
 {'age': 222, 'amount': 0.2},
 {'age': 232, 'amount': 0.25},
 {'age': 242, 'amount': 0.25},
 {'age': 252, 'amount': 0.2},
 {'age': 262, 'amount': 0.25},
 {'age': 272, 'amount': 0.25},
 {'age': 282, 'amount': 0.2},
 {'age': 292, 'amount': 0.25},
 {'age': 302, 'amount': 0.25},
 {'age': 312, 'amount': 3.15}]
```
    op hex (41)
    0000   0x5c 0x29 0x02 0xc0 0x04 0x0a 0xca 0x04    \)......
    0008   0x0a 0xd4 0x04 0x08 0xde 0x04 0x0a 0xe8    ........
    0010   0x04 0x0a 0xf2 0x04 0x08 0xfc 0x04 0x0a    ........
    0018   0x06 0x14 0x0a 0x10 0x14 0x08 0x1a 0x14    ........
    0020   0x0a 0x24 0x14 0x0a 0x2e 0x14 0x7e 0x38    .$....~8
    0028   0x14                                       .
    decimal
             92   41    2  192    4   10  202    4
             10  212    4    8  222    4   10  232
              4   10  242    4    8  252    4   10
              6   20   10   16   20    8   26   20
             10   36   20   10   46   20  126   56
             20
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2015-02-16T08:48:43 head[8], body[0] op[0x01]
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
    datetime (2015-02-16T08:48:43)
    0000   0x2b 0xb0 0xa8 0x70 0x0f                   +..p.
    body (0)

#### RECORD 73 Bolus 2015-02-16T08:48:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0x04 0x00    ..d.d...
    decimal
              1    0  100    0  100    0    4    0
    datetime (2015-02-16T08:48:43)
    0000   0x2b 0xb0 0x88 0x70 0x0f                   +..p.
    body (0)

`end ReadHistoryData-page-28.data: 74 records`
