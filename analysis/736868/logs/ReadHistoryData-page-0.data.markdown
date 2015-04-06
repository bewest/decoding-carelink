## START analysis/736868/logs/ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 530, found 492 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc8 0x24                                  .$
##### DEBUG DECIMAL
            200   36
#### RECORD 0 BolusWizard 2015-03-28T21:29:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-28T21:29:36)
    0000   0x24 0xdd 0x15 0x7c 0x0f                   $..|.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0   60   40   90    0    0
              0    0    0    0    0    0  120

#### RECORD 1 UnabsorbedInsulinBolus unknown head[47], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 0.25, 'curve': 4},
 {'age': 20, 'amount': 0.2, 'curve': 4},
 {'age': 30, 'amount': 0.2, 'curve': 4},
 {'age': 40, 'amount': 0.25, 'curve': 4},
 {'age': 50, 'amount': 0.2, 'curve': 4},
 {'age': 60, 'amount': 0.25, 'curve': 4},
 {'age': 70, 'amount': 0.2, 'curve': 4},
 {'age': 80, 'amount': 0.25, 'curve': 4},
 {'age': 90, 'amount': 0.2, 'curve': 4},
 {'age': 100, 'amount': 1.05, 'curve': 4},
 {'age': 110, 'amount': 2.1, 'curve': 4},
 {'age': 120, 'amount': 1.0, 'curve': 4},
 {'age': 14, 'amount': 5.0, 'curve': 20},
 {'age': 74, 'amount': 2.0, 'curve': 20},
 {'age': 104, 'amount': 1.0, 'curve': 20}]
```
    op hex (47)
    0000   0x5c 0x2f 0x0a 0x0a 0x04 0x08 0x14 0x04    \/......
    0008   0x08 0x1e 0x04 0x0a 0x28 0x04 0x08 0x32    ....(..2
    0010   0x04 0x0a 0x3c 0x04 0x08 0x46 0x04 0x0a    ..<..F..
    0018   0x50 0x04 0x08 0x5a 0x04 0x2a 0x64 0x04    P..Z.*d.
    0020   0x54 0x6e 0x04 0x28 0x78 0x04 0xc8 0x0e    Tn.(x...
    0028   0x14 0x50 0x4a 0x14 0x28 0x68 0x14         .PJ.(h.
    decimal
             92   47   10   10    4    8   20    4
              8   30    4   10   40    4    8   50
              4   10   60    4    8   70    4   10
             80    4    8   90    4   42  100    4
             84  110    4   40  120    4  200   14
             20   80   74   20   40  104   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2015-03-28T21:29:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 3.9}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x9c 0x00    ........
    decimal
              1    0  160    0  160    0  156    0
    datetime (2015-03-28T21:29:36)
    0000   0x24 0xdd 0x55 0x7c 0x0f                   $.U|.
    body (0)

#### RECORD 3 SensorAlert 2015-03-28T21:32:35 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 101, 'amount_maybe': 74}
```
    op hex (3)
    0000   0x0b 0x65 0x4a                             .eJ
    decimal
             11  101   74
    datetime (2015-03-28T21:32:35)
    0000   0x23 0xe0 0x35 0xbc 0x8f                   #.5..
    body (0)

#### RECORD 4 BasalProfileStart 2015-03-28T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-28T22:00:00)
    0000   0x00 0xc0 0x16 0x1c 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 5 SensorAlert 2015-03-28T22:58:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 105, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-28T22:58:00)
    0000   0x00 0xfa 0x36 0xbc 0x0f                   ..6..
    body (0)

#### RECORD 6 CalBGForPH 2015-03-28T23:52:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2015-03-28T23:52:37)
    0000   0x25 0xf4 0x37 0x7c 0x0f                   %.7|.
    body (0)

#### RECORD 7 BGReceived 2015-03-28T23:52:37 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2015-03-28T23:52:37)
    0000   0x25 0xf4 0x77 0x7c 0x0f                   %.w|.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 8 BasalProfileStart 2015-03-29T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-29T00:00:00)
    0000   0x00 0xc0 0x00 0x1d 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 9 MResultTotals 2015-03-29T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x08 0xa6                   .....
    decimal
              7    0    0    8  166
    datetime (2015-03-29T00:00:00)
    0000   0x3c 0x8f                                  <.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 10 Sara6E 2015-03-29T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-29T00:00:00)
    0000   0x3c 0x8f                                  <.
    body (49)
    hex
    0000   0x05 0x00 0x7e 0x5b 0xa1 0x02 0x00 0x00    ..~[....
    0008   0x08 0xa6 0x03 0x1c 0x24 0x05 0x8a 0x40    ....$..@
    0010   0x00 0x46 0x00 0x7c 0x01 0x9e 0x00 0x00    .F.|....
    0018   0x03 0x70 0x01 0x02 0x00 0x07 0x01 0x12    .p......
    0020   0x4f 0x13 0x02 0x12 0x54 0x02 0x01 0x00    O...T...
    0028   0x00 0x01 0x0d 0x01 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  126   91  161    2    0    0
              8  166    3   28   36    5  138   64
              0   70    0  124    1  158    0    0
              3  112    1    2    0    7    1   18
             79   19    2   18   84    2    1    0
              0    1   13    1    0    0    0    0
              0

#### RECORD 11 SensorAlert 2015-03-29T01:01:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-29T01:01:45)
    0000   0x2d 0xc1 0x21 0xbd 0x0f                   -.!..
    body (0)

#### RECORD 12 SensorAlert 2015-03-29T01:13:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-03-29T01:13:02)
    0000   0x02 0xcd 0x21 0xbd 0x0f                   ..!..
    body (0)

#### RECORD 13 BasalProfileStart 2015-03-29T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-29T04:00:00)
    0000   0x00 0xc0 0x04 0x1d 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 14 BasalProfileStart 2015-03-29T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-29T07:00:00)
    0000   0x00 0xc0 0x07 0x1d 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 15 SensorAlert 2015-03-29T09:13:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 115, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-29T09:13:02)
    0000   0x02 0xcd 0x29 0xbd 0x0f                   ..)..
    body (0)

#### RECORD 16 SensorAlert 2015-03-29T09:17:55 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 80}
```
    op hex (3)
    0000   0x0b 0x66 0x50                             .fP
    decimal
             11  102   80
    datetime (2015-03-29T09:17:55)
    0000   0x37 0xd1 0x29 0xbd 0x0f                   7.)..
    body (0)

#### RECORD 17 SensorAlert 2015-03-29T09:47:07 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 102, 'amount_maybe': 76}
```
    op hex (3)
    0000   0x0b 0x66 0x4c                             .fL
    decimal
             11  102   76
    datetime (2015-03-29T09:47:07)
    0000   0x07 0xef 0x29 0xbd 0x0f                   ..)..
    body (0)

#### RECORD 18 SensorAlert 2015-03-29T09:53:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 107, 'amount_maybe': 0}
```
    op hex (3)
    0000   0x0b 0x6b 0x00                             .k.
    decimal
             11  107    0
    datetime (2015-03-29T09:53:02)
    0000   0x02 0xf5 0x29 0xbd 0x0f                   ..)..
    body (0)

#### RECORD 19 BasalProfileStart 2015-03-29T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-29T10:00:00)
    0000   0x00 0xc0 0x0a 0x1d 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 20 Bolus 2015-03-29T11:17:55 head[8], body[0] op[0x01]
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
    datetime (2015-03-29T11:17:55)
    0000   0x37 0xd1 0x4b 0x7d 0x0f                   7.K}.
    body (0)

#### RECORD 21 BasalProfileStart 2015-03-29T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-29T12:00:00)
    0000   0x00 0xc0 0x0c 0x1d 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 22 BasalProfileStart 2015-03-29T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-29T15:00:00)
    0000   0x00 0xc0 0x0f 0x1d 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 23 BolusWizard 2015-03-29T16:43:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.7,
 'carb_input': 46,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-29T16:43:32)
    0000   0x20 0xeb 0x10 0x7d 0x0f                    ..}.
    body (15)
    hex
    0000   0x2e 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0xe4 0x00 0x00 0x00 0x00 0xe4 0x78         ......x
    decimal
             46   80    0   80   40   90    0    0
            228    0    0    0    0  228  120

#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 1.9, 'curve': 20},
 {'age': 78, 'amount': 1.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x44 0x14 0x40 0x4e 0x14    \.LD.@N.
    decimal
             92    8   76   68   20   64   78   20
    datetime (unknown)

    body (0)

#### RECORD 25 BolusWizard 2015-03-29T16:43:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.7,
 'carb_input': 46,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-29T16:43:34)
    0000   0x22 0xeb 0x10 0x7d 0x0f                   "..}.
    body (15)
    hex
    0000   0x2e 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    .P.P(Z..
    0008   0xe4 0x00 0x00 0x00 0x00 0xe4 0x78         ......x
    decimal
             46   80    0   80   40   90    0    0
            228    0    0    0    0  228  120

#### RECORD 26 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 1.9, 'curve': 20},
 {'age': 78, 'amount': 1.6, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x4c 0x44 0x14 0x40 0x4e 0x14    \.LD.@N.
    decimal
             92    8   76   68   20   64   78   20
    datetime (unknown)

    body (0)

#### RECORD 27 Bolus 2015-03-29T16:43:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.7,
 'duration': 0,
 'programmed': 5.7,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0xe4 0x00 0xe4 0x00 0x00 0x00    ........
    decimal
              1    0  228    0  228    0    0    0
    datetime (2015-03-29T16:43:34)
    0000   0x22 0xeb 0x50 0x7d 0x0f                   ".P}.
    body (0)

#### RECORD 28 CalBGForPH 2015-03-29T16:51:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 315}
```
    op hex (2)
    0000   0x0a 0x3b                                  .;
    decimal
             10   59
    datetime (2015-03-29T16:51:53)
    0000   0x35 0xf3 0x30 0x7d 0x8f                   5.0}.
    body (0)

#### RECORD 29 BGReceived 2015-03-29T16:51:53 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': '???', 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x27                                  ?'
    decimal
             63   39
    datetime (2015-03-29T16:51:53)
    0000   0x35 0xf3 0x70 0x7d 0x0f                   5.p}.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 30 BolusWizard 2015-03-29T16:52:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 315,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': -1.6,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 5.7}
```
    op hex (2)
    0000   0x5b 0x3b                                  [;
    decimal
             91   59
    datetime (2015-03-29T16:52:30)
    0000   0x1e 0xf4 0x10 0x7d 0x0f                   ...}.
    body (15)
    hex
    0000   0x00 0x51 0x00 0x50 0x28 0x5a 0xc0 0x00    .Q.P(Z..
    0008   0x00 0x00 0x00 0xe4 0x00 0x00 0x78         ......x
    decimal
              0   81    0   80   40   90  192    0
              0    0    0  228    0    0  120

#### RECORD 31 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 13, 'amount': 5.7, 'curve': 4},
 {'age': 77, 'amount': 1.9, 'curve': 20},
 {'age': 87, 'amount': 1.6, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xe4 0x0d 0x04 0x4c 0x4d 0x14    \....LM.
    0008   0x40 0x57 0x14                             @W.
    decimal
             92   11  228   13    4   76   77   20
             64   87   20
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2015-03-29T16:53:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 60,
 'programmed': 4.0,
 'type': 'square',
 'unabsorbed': 5.7}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xe4 0x02    ........
    decimal
              1    0  160    0  160    0  228    2
    datetime (2015-03-29T16:53:50)
    0000   0x32 0xf5 0xb0 0x7d 0x0f                   2..}.
    body (0)

#### RECORD 33 Bolus 2015-03-29T16:52:30 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 5.7}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0xe4 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  228    0
    datetime (2015-03-29T16:52:30)
    0000   0x1e 0xf4 0x90 0x7d 0x0f                   ...}.
    body (0)

#### RECORD 34 BolusWizard 2015-03-29T21:43:14 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.8,
 'carb_input': 35,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.8,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-29T21:43:14)
    0000   0x0e 0xeb 0x15 0x7d 0x0f                   ...}.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    #P.<(Z..
    0008   0xe8 0x00 0x00 0x00 0x00 0xe8 0x78         ......x
    decimal
             35   80    0   60   40   90    0    0
            232    0    0    0    0  232  120

#### RECORD 35 UnabsorbedInsulinBolus unknown head[26], body[0] op[0x5c]
###### DECODED
```python
[{'age': 234, 'amount': 0.3, 'curve': 4},
 {'age': 244, 'amount': 0.7, 'curve': 4},
 {'age': 254, 'amount': 0.65, 'curve': 4},
 {'age': 8, 'amount': 0.65, 'curve': 20},
 {'age': 18, 'amount': 0.7, 'curve': 20},
 {'age': 28, 'amount': 0.65, 'curve': 20},
 {'age': 38, 'amount': 2.35, 'curve': 20},
 {'age': 48, 'amount': 5.7, 'curve': 20}]
```
    op hex (26)
    0000   0x5c 0x1a 0x0c 0xea 0x04 0x1c 0xf4 0x04    \.......
    0008   0x1a 0xfe 0x04 0x1a 0x08 0x14 0x1c 0x12    ........
    0010   0x14 0x1a 0x1c 0x14 0x5e 0x26 0x14 0xe4    ....^&..
    0018   0x30 0x14                                  0.
    decimal
             92   26   12  234    4   28  244    4
             26  254    4   26    8   20   28   18
             20   26   28   20   94   38   20  228
             48   20
    datetime (unknown)

    body (0)

#### RECORD 36 Bolus 2015-03-29T21:43:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.8,
 'duration': 0,
 'programmed': 5.8,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0xe8 0x00 0xe8 0x00 0x04 0x00    ........
    decimal
              1    0  232    0  232    0    4    0
    datetime (2015-03-29T21:43:14)
    0000   0x0e 0xeb 0x55 0x7d 0x0f                   ..U}.
    body (0)

#### RECORD 37 BasalProfileStart 2015-03-29T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-29T22:00:00)
    0000   0x00 0xc0 0x16 0x1d 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

`end analysis/736868/logs/ReadHistoryData-page-0.data: 38 records`
