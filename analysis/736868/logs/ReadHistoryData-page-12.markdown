## START ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 975, found 47 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x8c 0x50                                  .P
##### DEBUG DECIMAL
            140   80
#### RECORD 0 UnabsorbedInsulinBolus unknown head[53], body[0] op[0x5c]
###### DECODED
```python
[{'age': 180, 'amount': 1.25},
 {'age': 190, 'amount': 1.25},
 {'age': 210, 'amount': 3.0},
 {'age': 220, 'amount': 3.0},
 {'age': 240, 'amount': 2.0},
 {'age': 360, 'amount': 0.05},
 {'age': 370, 'amount': 0.2},
 {'age': 380, 'amount': 0.2},
 {'age': 390, 'amount': 0.2},
 {'age': 400, 'amount': 0.2},
 {'age': 410, 'amount': 0.2},
 {'age': 420, 'amount': 0.2},
 {'age': 430, 'amount': 0.2},
 {'age': 440, 'amount': 0.15},
 {'age': 450, 'amount': 0.2},
 {'age': 460, 'amount': 0.2},
 {'age': 470, 'amount': 0.2}]
```
    op hex (53)
    0000   0x5c 0x35 0x32 0xb4 0x04 0x32 0xbe 0x04    \52..2..
    0008   0x78 0xd2 0x04 0x78 0xdc 0x04 0x50 0xf0    x..x..P.
    0010   0x04 0x02 0x68 0x14 0x08 0x72 0x14 0x08    ..h..r..
    0018   0x7c 0x14 0x08 0x86 0x14 0x08 0x90 0x14    |.......
    0020   0x08 0x9a 0x14 0x08 0xa4 0x14 0x08 0xae    ........
    0028   0x14 0x06 0xb8 0x14 0x08 0xc2 0x14 0x08    ........
    0030   0xcc 0x14 0x08 0xd6 0x14                   .....
    decimal
             92   53   50  180    4   50  190    4
            120  210    4  120  220    4   80  240
              4    2  104   20    8  114   20    8
            124   20    8  134   20    8  144   20
              8  154   20    8  164   20    8  174
             20    6  184   20    8  194   20    8
            204   20    8  214   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2015-03-09T21:22:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6,
 'duration': 60,
 'programmed': 3.6,
 'type': 'square',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x90 0x00 0x90 0x00 0x2c 0x02    ......,.
    decimal
              1    0  144    0  144    0   44    2
    datetime (2015-03-09T21:22:27)
    0000   0x1b 0xd6 0xb5 0x69 0x0f                   ...i.
    body (0)

#### RECORD 2 Bolus 2015-03-09T21:19:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9,
 'duration': 0,
 'programmed': 3.9,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x2c 0x00    ......,.
    decimal
              1    0  156    0  156    0   44    0
    datetime (2015-03-09T21:19:50)
    0000   0x32 0xd3 0x95 0x69 0x0f                   2..i.
    body (0)

#### RECORD 3 BasalProfileStart 2015-03-09T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-09T22:00:00)
    0000   0x00 0xc0 0x16 0x09 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 4 SensorAlert 2015-03-09T22:49:02 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 206}
```
    op hex (3)
    0000   0x0b 0x65 0xce                             .e.
    decimal
             11  101  206
    datetime (2015-03-09T22:49:02)
    0000   0x02 0xf1 0x36 0xa9 0x0f                   ..6..
    body (0)

#### RECORD 5 BolusWizard 2015-03-09T23:09:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 2.4,
 'carb_input': 24,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 2.4,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-09T23:09:05)
    0000   0x05 0xc9 0x17 0x69 0x0f                   ...i.
    body (15)
    hex
    0000   0x18 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    .P.d(Z..
    0008   0x60 0x00 0x00 0x00 0x00 0x60 0x78         `....`x
    decimal
             24   80    0  100   40   90    0    0
             96    0    0    0    0   96  120

#### RECORD 6 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 50, 'amount': 0.2},
 {'age': 60, 'amount': 0.6},
 {'age': 70, 'amount': 0.6},
 {'age': 80, 'amount': 0.6},
 {'age': 90, 'amount': 0.6},
 {'age': 100, 'amount': 0.6},
 {'age': 110, 'amount': 4.3},
 {'age': 290, 'amount': 1.25},
 {'age': 300, 'amount': 1.25},
 {'age': 320, 'amount': 3.0},
 {'age': 330, 'amount': 3.0},
 {'age': 350, 'amount': 2.0},
 {'age': 470, 'amount': 0.05}]
```
    op hex (41)
    0000   0x5c 0x29 0x08 0x32 0x04 0x18 0x3c 0x04    \).2..<.
    0008   0x18 0x46 0x04 0x18 0x50 0x04 0x18 0x5a    .F..P..Z
    0010   0x04 0x18 0x64 0x04 0xac 0x6e 0x04 0x32    ..d..n.2
    0018   0x22 0x14 0x32 0x2c 0x14 0x78 0x40 0x14    ".2,.x@.
    0020   0x78 0x4a 0x14 0x50 0x5e 0x14 0x02 0xd6    xJ.P^...
    0028   0x14                                       .
    decimal
             92   41    8   50    4   24   60    4
             24   70    4   24   80    4   24   90
              4   24  100    4  172  110    4   50
             34   20   50   44   20  120   64   20
            120   74   20   80   94   20    2  214
             20
    datetime (unknown)

    body (0)

#### RECORD 7 Bolus 2015-03-09T23:09:06 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4,
 'duration': 0,
 'programmed': 2.4,
 'type': 'normal',
 'unabsorbed': 4.6}
```
    op hex (8)
    0000   0x01 0x00 0x60 0x00 0x60 0x00 0xb8 0x00    ..`.`...
    decimal
              1    0   96    0   96    0  184    0
    datetime (2015-03-09T23:09:06)
    0000   0x06 0xc9 0x57 0x69 0x0f                   ..Wi.
    body (0)

#### RECORD 8 CalBGForPH 2015-03-09T23:17:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 72}
```
    op hex (2)
    0000   0x0a 0x48                                  .H
    decimal
             10   72
    datetime (2015-03-09T23:17:58)
    0000   0x3a 0xd1 0x37 0x69 0x0f                   :.7i.
    body (0)

#### RECORD 9 BGReceived 2015-03-09T23:17:58 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 72, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2015-03-09T23:17:58)
    0000   0x3a 0xd1 0x17 0x69 0x0f                   :..i.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 10 SensorAlert 2015-03-09T23:32:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 104'}
```
    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-03-09T23:32:45)
    0000   0x2d 0xe0 0x37 0xa9 0x0f                   -.7..
    body (0)

#### RECORD 11 SensorAlert 2015-03-09T23:32:45 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 106'}
```
    op hex (3)
    0000   0x0b 0x6a 0x00                             .j.
    decimal
             11  106    0
    datetime (2015-03-09T23:32:45)
    0000   0x2d 0xe0 0x37 0xa9 0x0f                   -.7..
    body (0)

#### RECORD 12 CalBGForPH 2015-03-09T23:36:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 64}
```
    op hex (2)
    0000   0x0a 0x40                                  .@
    decimal
             10   64
    datetime (2015-03-09T23:36:18)
    0000   0x12 0xe4 0x37 0x69 0x0f                   ..7i.
    body (0)

#### RECORD 13 BGReceived 2015-03-09T23:36:18 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 64, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2015-03-09T23:36:18)
    0000   0x12 0xe4 0x17 0x69 0x0f                   ...i.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 14 BasalProfileStart 2015-03-10T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-10T00:00:00)
    0000   0x00 0xc0 0x00 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 15 MResultTotals 2015-03-10T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x09 0x0c                   .....
    decimal
              7    0    0    9   12
    datetime (2015-03-10T00:00:00)
    0000   0x29 0x8f                                  ).
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 16 Sara6E 2015-03-10T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-03-10T00:00:00)
    0000   0x29 0x8f                                  ).
    body (49)
    hex
    0000   0x05 0x00 0x80 0x40 0xc4 0x04 0x00 0x00    ...@....
    0008   0x09 0x0c 0x03 0x30 0x23 0x05 0xdc 0x41    ...0#..A
    0010   0x00 0xc7 0x03 0x9c 0x00 0x4c 0x00 0x00    .....L..
    0018   0x01 0xf4 0x04 0x01 0x00 0x05 0x00 0xaf    ........
    0020   0x28 0x3c 0x00 0x85 0x26 0x03 0x00 0x00    (<..&...
    0028   0x00 0x00 0x06 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  128   64  196    4    0    0
              9   12    3   48   35    5  220   65
              0  199    3  156    0   76    0    0
              1  244    4    1    0    5    0  175
             40   60    0  133   38    3    0    0
              0    0    6    0    0    0    0    0
              0

#### RECORD 17 SensorAlert 2015-03-10T02:33:26 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-10T02:33:26)
    0000   0x1a 0xe1 0x22 0xaa 0x0f                   .."..
    body (0)

#### RECORD 18 SensorAlert 2015-03-10T03:08:04 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-10T03:08:04)
    0000   0x04 0xc8 0x23 0xaa 0x0f                   ..#..
    body (0)

#### RECORD 19 BasalProfileStart 2015-03-10T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-10T04:00:00)
    0000   0x00 0xc0 0x04 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 20 SensorAlert 2015-03-10T04:39:21 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 279}
```
    op hex (3)
    0000   0x0b 0x65 0x17                             .e.
    decimal
             11  101   23
    datetime (2015-03-10T04:39:21)
    0000   0x15 0xe7 0x24 0xaa 0x8f                   ..$..
    body (0)

#### RECORD 21 NoDelivery 2015-03-10T06:04:44 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x04 0x0c 0x1e                        ....
    decimal
              6    4   12   30
    datetime (2015-03-10T06:04:44)
    0000   0x2c 0xc4 0x46 0x4a 0x0f                   ,.FJ.
    body (0)

#### RECORD 22 SensorAlert 2015-03-10T06:09:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 348}
```
    op hex (3)
    0000   0x0b 0x65 0x5c                             .e\
    decimal
             11  101   92
    datetime (2015-03-10T06:09:01)
    0000   0x01 0xc9 0x26 0xaa 0x8f                   ..&..
    body (0)

#### RECORD 23 ClearAlarm 2015-03-10T06:17:10 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x04                                  ..
    decimal
             12    4
    datetime (2015-03-10T06:17:10)
    0000   0x0a 0xd1 0x06 0x0a 0x0f                   .....
    body (0)

#### RECORD 24 Rewind 2015-03-10T06:17:46 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2015-03-10T06:17:46)
    0000   0x2e 0xd1 0x06 0x0a 0x0f                   .....
    body (0)

#### RECORD 25 Prime 2015-03-10T06:18:38 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.0, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x00                   .....
    decimal
              3    0    0    0    0
    datetime (2015-03-10T06:18:38)
    0000   0x26 0xd2 0x26 0x0a 0x0f                   &.&..
    body (0)

#### RECORD 26 BasalProfileStart 2015-03-10T06:19:18 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-03-10T06:19:18)
    0000   0x12 0xd3 0x06 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 27 Prime 2015-03-10T06:19:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.4, 'fixed': 0.4, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x04 0x00 0x04                   .....
    decimal
              3    0    4    0    4
    datetime (2015-03-10T06:19:03)
    0000   0x03 0xd3 0x06 0x0a 0x0f                   .....
    body (0)

#### RECORD 28 BolusWizard 2015-03-10T06:19:45 head[2], body[15] op[0x5b]
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
    datetime (2015-03-10T06:19:45)
    0000   0x2d 0xd3 0x06 0x6a 0x0f                   -..j.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    .P.d(Z..
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x78         ......x
    decimal
              0   80    0  100   40   90    0    0
              0    0    0    0    0    0  120

#### RECORD 29 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 430, 'amount': 2.4}]
```
    op hex (5)
    0000   0x5c 0x05 0x60 0xae 0x14                   \.`..
    decimal
             92    5   96  174   20
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2015-03-10T06:19:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x01 0x3c 0x01 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    1   60    1   60    0    0    0
    datetime (2015-03-10T06:19:46)
    0000   0x2e 0xd3 0x46 0x6a 0x0f                   ..Fj.
    body (0)

#### RECORD 31 BasalProfileStart 2015-03-10T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-10T07:00:00)
    0000   0x00 0xc0 0x07 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 32 PumpSuspend 2015-03-10T07:20:25 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-10T07:20:25)
    0000   0x19 0xd4 0x07 0x0a 0x0f                   .....
    body (0)

#### RECORD 33 BasalProfileStart 2015-03-10T07:22:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-10T07:22:00)
    0000   0x00 0xd6 0x07 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 34 PumpResume 2015-03-10T07:22:00 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-10T07:22:00)
    0000   0x00 0xd6 0x07 0x0a 0x0f                   .....
    body (0)

#### RECORD 35 BolusWizard 2015-03-10T07:26:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 45,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-10T07:26:07)
    0000   0x07 0xda 0x07 0x6a 0x0f                   ...j.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    -P.d(Z..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x78         ......x
    decimal
             45   80    0  100   40   90    0    0
            180    0    0    0    0  180  120

#### RECORD 36 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 1.5}]
```
    op hex (5)
    0000   0x5c 0x05 0x3c 0x43 0x05                   \.<C.
    decimal
             92    5   60   67    5
    datetime (unknown)

    body (0)

#### RECORD 37 Bolus 2015-03-10T07:26:07 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 6.2}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0xf8 0x00    ........
    decimal
              1    0  180    0  180    0  248    0
    datetime (2015-03-10T07:26:07)
    0000   0x07 0xda 0x47 0x6a 0x0f                   ..Gj.
    body (0)

#### RECORD 38 PumpSuspend 2015-03-10T07:29:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-03-10T07:29:19)
    0000   0x13 0xdd 0x07 0x0a 0x0f                   .....
    body (0)

#### RECORD 39 SensorAlert 2015-03-10T07:53:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 323}
```
    op hex (3)
    0000   0x0b 0x65 0x43                             .eC
    decimal
             11  101   67
    datetime (2015-03-10T07:53:25)
    0000   0x19 0xf5 0x27 0xaa 0x8f                   ..'..
    body (0)

#### RECORD 40 BasalProfileStart 2015-03-10T07:55:13 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-03-10T07:55:13)
    0000   0x0d 0xf7 0x07 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 41 PumpResume 2015-03-10T07:55:13 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-03-10T07:55:13)
    0000   0x0d 0xf7 0x07 0x0a 0x0f                   .....
    body (0)

#### RECORD 42 SensorAlert 2015-03-10T09:24:13 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 201}
```
    op hex (3)
    0000   0x0b 0x65 0xc9                             .e.
    decimal
             11  101  201
    datetime (2015-03-10T09:24:13)
    0000   0x0d 0xd8 0x29 0xaa 0x0f                   ..)..
    body (0)

#### RECORD 43 BasalProfileStart 2015-03-10T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-03-10T10:00:00)
    0000   0x00 0xc0 0x0a 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 44 SensorAlert 2015-03-10T10:36:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-10T10:36:00)
    0000   0x00 0xe4 0x2a 0xaa 0x0f                   ..*..
    body (0)

#### RECORD 45 SensorAlert 2015-03-10T10:52:44 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 234}
```
    op hex (3)
    0000   0x0b 0x65 0xea                             .e.
    decimal
             11  101  234
    datetime (2015-03-10T10:52:44)
    0000   0x2c 0xf4 0x2a 0xaa 0x0f                   ,.*..
    body (0)

#### RECORD 46 CalBGForPH 2015-03-10T10:53:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 256}
```
    op hex (2)
    0000   0x0a 0x00                                  ..
    decimal
             10    0
    datetime (2015-03-10T10:53:52)
    0000   0x34 0xf5 0x2a 0x6a 0x8f                   4.*j.
    body (0)

#### RECORD 47 BGReceived 2015-03-10T10:53:52 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 256, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x20                                  ? 
    decimal
             63   32
    datetime (2015-03-10T10:53:52)
    0000   0x34 0xf5 0x0a 0x6a 0x0f                   4..j.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 48 BolusWizard 2015-03-10T10:54:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 256,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 3.0,
 'carb_input': 0,
 'carb_ratio': 8.1,
 'correction_estimate': 3.4,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.4}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-10T10:54:08)
    0000   0x08 0xf6 0x0a 0x0a 0x0f                   .....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x64 0x28 0x5a 0x88 0x00    .Q.d(Z..
    0008   0x00 0x00 0x00 0x10 0x00 0x78 0x78         .....xx
    decimal
              0   81    0  100   40   90  136    0
              0    0    0   16    0  120  120

#### RECORD 49 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 205, 'amount': 0.25},
 {'age': 215, 'amount': 4.25},
 {'age': 275, 'amount': 1.5}]
```
    op hex (11)
    0000   0x5c 0x0b 0x0a 0xcd 0x04 0xaa 0xd7 0x04    \.......
    0008   0x3c 0x13 0x15                             <..
    decimal
             92   11   10  205    4  170  215    4
             60   19   21
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2015-03-10T10:54:08 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x10 0x00    ..x.x...
    decimal
              1    0  120    0  120    0   16    0
    datetime (2015-03-10T10:54:08)
    0000   0x08 0xf6 0x4a 0x0a 0x0f                   ..J..
    body (0)

#### RECORD 51 BolusWizard 2015-03-10T11:53:35 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 8.7,
 'carb_input': 70,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 8.7,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-10T11:53:35)
    0000   0x23 0xf5 0x0b 0x6a 0x0f                   #..j.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    FP.P(Z..
    0008   0x5c 0x00 0x00 0x00 0x01 0x5c 0x78         \....\x
    decimal
             70   80    0   80   40   90    0    1
             92    0    0    0    1   92  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 64, 'amount': 3.0},
 {'age': 264, 'amount': 0.25},
 {'age': 274, 'amount': 4.25},
 {'age': 334, 'amount': 1.5}]
```
    op hex (14)
    0000   0x5c 0x0e 0x78 0x40 0x04 0x0a 0x08 0x14    \.x@....
    0008   0xaa 0x12 0x14 0x3c 0x4e 0x15              ...<N.
    decimal
             92   14  120   64    4   10    8   20
            170   18   20   60   78   21
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2015-03-10T11:56:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3,
 'duration': 60,
 'programmed': 3.3,
 'type': 'square',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x60 0x02    ......`.
    decimal
              1    0  132    0  132    0   96    2
    datetime (2015-03-10T11:56:42)
    0000   0x2a 0xf8 0xab 0x6a 0x0f                   *..j.
    body (0)

#### RECORD 54 Bolus 2015-03-10T11:53:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6,
 'duration': 0,
 'programmed': 4.6,
 'type': 'normal',
 'unabsorbed': 2.4}
```
    op hex (8)
    0000   0x01 0x00 0xb8 0x00 0xb8 0x00 0x60 0x00    ......`.
    decimal
              1    0  184    0  184    0   96    0
    datetime (2015-03-10T11:53:35)
    0000   0x23 0xf5 0x8b 0x6a 0x0f                   #..j.
    body (0)

#### RECORD 55 BasalProfileStart 2015-03-10T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-03-10T12:00:00)
    0000   0x00 0xc0 0x0c 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 56 BasalProfileStart 2015-03-10T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-03-10T15:00:00)
    0000   0x00 0xc0 0x0f 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 57 SensorAlert 2015-03-10T16:58:52 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Unknown subtype with code 114'}
```
    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-03-10T16:58:52)
    0000   0x34 0xfa 0x30 0xaa 0x0f                   4.0..
    body (0)

#### RECORD 58 SensorAlert 2015-03-10T17:03:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 180}
```
    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-03-10T17:03:03)
    0000   0x03 0xc3 0x31 0xaa 0x0f                   ..1..
    body (0)

#### RECORD 59 Bolus 2015-03-10T17:11:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x00 0x00    ........
    decimal
              1    0   20    0   20    0    0    0
    datetime (2015-03-10T17:11:24)
    0000   0x18 0xcb 0x51 0x6a 0x0f                   ..Qj.
    body (0)

#### RECORD 60 SensorAlert 2015-03-10T18:33:25 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 215}
```
    op hex (3)
    0000   0x0b 0x65 0xd7                             .e.
    decimal
             11  101  215
    datetime (2015-03-10T18:33:25)
    0000   0x19 0xe1 0x32 0xaa 0x0f                   ..2..
    body (0)

#### RECORD 61 BolusWizard 2015-03-10T18:34:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 90,
 'bolus_estimate': 5.1,
 'carb_input': 31,
 'carb_ratio': 8.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.1,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-03-10T18:34:33)
    0000   0x21 0xe2 0x12 0x6a 0x0f                   !..j.
    body (15)
    hex
    0000   0x1f 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0xcc 0x00 0x00 0x00 0x00 0xcc 0x78         ......x
    decimal
             31   80    0   60   40   90    0    0
            204    0    0    0    0  204  120

#### RECORD 62 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 0.5},
 {'age': 345, 'amount': 0.4},
 {'age': 355, 'amount': 0.55},
 {'age': 365, 'amount': 0.55},
 {'age': 375, 'amount': 0.55},
 {'age': 385, 'amount': 0.55},
 {'age': 395, 'amount': 0.55},
 {'age': 405, 'amount': 4.75},
 {'age': 465, 'amount': 3.0}]
```
    op hex (29)
    0000   0x5c 0x1d 0x14 0x55 0x04 0x10 0x59 0x14    \..U..Y.
    0008   0x16 0x63 0x14 0x16 0x6d 0x14 0x16 0x77    .c..m..w
    0010   0x14 0x16 0x81 0x14 0x16 0x8b 0x14 0xbe    ........
    0018   0x95 0x14 0x78 0xd1 0x14                   ..x..
    decimal
             92   29   20   85    4   16   89   20
             22   99   20   22  109   20   22  119
             20   22  129   20   22  139   20  190
            149   20  120  209   20
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2015-03-10T18:34:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.1,
 'duration': 0,
 'programmed': 5.1,
 'type': 'normal',
 'unabsorbed': 0.4}
```
    op hex (8)
    0000   0x01 0x00 0xcc 0x00 0xcc 0x00 0x10 0x00    ........
    decimal
              1    0  204    0  204    0   16    0
    datetime (2015-03-10T18:34:34)
    0000   0x22 0xe2 0x52 0x6a 0x0f                   ".Rj.
    body (0)

#### RECORD 64 Bolus 2015-03-10T19:22:17 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 4.6}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xb8 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  184    0
    datetime (2015-03-10T19:22:17)
    0000   0x11 0xd6 0x53 0x6a 0x0f                   ..Sj.
    body (0)

#### RECORD 65 SensorAlert 2015-03-10T20:04:13 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'High Glucose', 'glucose': 250}
```
    op hex (3)
    0000   0x0b 0x65 0xfa                             .e.
    decimal
             11  101  250
    datetime (2015-03-10T20:04:13)
    0000   0x0d 0xc4 0x34 0xaa 0x0f                   ..4..
    body (0)

#### RECORD 66 Bolus 2015-03-10T20:04:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 5.5}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x00 0xdc 0x00    ..d.d...
    decimal
              1    0  100    0  100    0  220    0
    datetime (2015-03-10T20:04:46)
    0000   0x2e 0xc4 0x54 0x6a 0x0f                   ..Tj.
    body (0)

#### RECORD 67 Bolus 2015-03-10T20:19:11 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x01 0x24 0x00    ......$.
    decimal
              1    0  160    0  160    1   36    0
    datetime (2015-03-10T20:19:11)
    0000   0x0b 0xd3 0x54 0x6a 0x0f                   ..Tj.
    body (0)

#### RECORD 68 Bolus 2015-03-10T20:29:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 4.4}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x01 0xb0 0x00    ..d.d...
    decimal
              1    0  100    0  100    1  176    0
    datetime (2015-03-10T20:29:05)
    0000   0x05 0xdd 0x54 0x6a 0x0f                   ..Tj.
    body (0)

#### RECORD 69 Bolus 2015-03-10T21:21:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.5,
 'duration': 0,
 'programmed': 2.5,
 'type': 'normal',
 'unabsorbed': 3.0}
```
    op hex (8)
    0000   0x01 0x00 0x64 0x00 0x64 0x01 0x78 0x00    ..d.d.x.
    decimal
              1    0  100    0  100    1  120    0
    datetime (2015-03-10T21:21:05)
    0000   0x05 0xd5 0x55 0x6a 0x0f                   ..Uj.
    body (0)

#### RECORD 70 SensorAlert 2015-03-10T21:54:00 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Cal Reminder'}
```
    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-03-10T21:54:00)
    0000   0x00 0xf6 0x35 0xaa 0x0f                   ..5..
    body (0)

#### RECORD 71 BasalProfileStart 2015-03-10T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-03-10T22:00:00)
    0000   0x00 0xc0 0x16 0x0a 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 72 SensorAlert 2015-03-10T22:28:03 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose Predicted'}
```
    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-03-10T22:28:03)
    0000   0x03 0xdc 0x36 0xaa 0x0f                   ..6..
    body (0)

#### RECORD 73 CalBGForPH 2015-03-10T22:33:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 51}
```
    op hex (2)
    0000   0x0a 0x33                                  .3
    decimal
             10   51
    datetime (2015-03-10T22:33:22)
    0000   0x16 0xe1 0x36 0x6a 0x0f                   ..6j.
    body (0)

#### RECORD 74 BGReceived 2015-03-10T22:33:22 head[2], body[3] op[0x3f]
###### DECODED
```python
{'amount': 51, 'link': '783436'}
```
    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2015-03-10T22:33:22)
    0000   0x16 0xe1 0x76 0x6a 0x0f                   ..vj.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 75 SensorAlert 2015-03-10T22:49:01 head[3], body[0] op[0x0b]
###### DECODED
```python
{'alarm_type': 'Low Glucose', 'glucose': 74}
```
    op hex (3)
    0000   0x0b 0x66 0x4a                             .fJ
    decimal
             11  102   74
    datetime (2015-03-10T22:49:01)
    0000   0x01 0xf1 0x36 0xaa 0x0f                   ..6..
    body (0)

#### RECORD 76 Bolus 2015-03-10T23:23:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 2.5}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x64 0x00    ..<.<.d.
    decimal
              1    0   60    0   60    0  100    0
    datetime (2015-03-10T23:23:40)
    0000   0x28 0xd7 0x57 0x6a 0x0f                   (.Wj.
    body (0)

#### RECORD 77 BasalProfileStart 2015-03-11T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-03-11T00:00:00)
    0000   0x00 0xc0 0x00 0x0b 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 78 MResultTotals 2015-03-11T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0x06                   .....
    decimal
              7    0    0   10    6
    datetime (2015-03-11T00:00:00)
    0000   0x2a 0x8f                                  *.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end ReadHistoryData-page-12.data: 79 records`
