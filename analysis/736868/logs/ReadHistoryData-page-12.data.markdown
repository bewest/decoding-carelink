## START analysis/736868/logs/ReadHistoryData-page-12.data
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
[{'age': 180, 'amount': 1.25, 'curve': 4},
 {'age': 190, 'amount': 1.25, 'curve': 4},
 {'age': 210, 'amount': 3.0, 'curve': 4},
 {'age': 220, 'amount': 3.0, 'curve': 4},
 {'age': 240, 'amount': 2.0, 'curve': 4},
 {'age': 104, 'amount': 0.05, 'curve': 20},
 {'age': 114, 'amount': 0.2, 'curve': 20},
 {'age': 124, 'amount': 0.2, 'curve': 20},
 {'age': 134, 'amount': 0.2, 'curve': 20},
 {'age': 144, 'amount': 0.2, 'curve': 20},
 {'age': 154, 'amount': 0.2, 'curve': 20},
 {'age': 164, 'amount': 0.2, 'curve': 20},
 {'age': 174, 'amount': 0.2, 'curve': 20},
 {'age': 184, 'amount': 0.15, 'curve': 20},
 {'age': 194, 'amount': 0.2, 'curve': 20},
 {'age': 204, 'amount': 0.2, 'curve': 20},
 {'age': 214, 'amount': 0.2, 'curve': 20}]
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
{'alarm_type': 101, 'amount_maybe': 206}
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
 'correction_maybe_estimate': 0.0,
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
[{'age': 50, 'amount': 0.2, 'curve': 4},
 {'age': 60, 'amount': 0.6, 'curve': 4},
 {'age': 70, 'amount': 0.6, 'curve': 4},
 {'age': 80, 'amount': 0.6, 'curve': 4},
 {'age': 90, 'amount': 0.6, 'curve': 4},
 {'age': 100, 'amount': 0.6, 'curve': 4},
 {'age': 110, 'amount': 4.3, 'curve': 4},
 {'age': 34, 'amount': 1.25, 'curve': 20},
 {'age': 44, 'amount': 1.25, 'curve': 20},
 {'age': 64, 'amount': 3.0, 'curve': 20},
 {'age': 74, 'amount': 3.0, 'curve': 20},
 {'age': 94, 'amount': 2.0, 'curve': 20},
 {'age': 214, 'amount': 0.05, 'curve': 20}]
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
{'amount': '???', 'link': '783436'}
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
{'alarm_type': 104, 'amount_maybe': 0}
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
{'alarm_type': 106, 'amount_maybe': 0}
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
###### 