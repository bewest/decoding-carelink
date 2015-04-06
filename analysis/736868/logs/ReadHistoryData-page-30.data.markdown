## START analysis/736868/logs/ReadHistoryData-page-30.data
#### STOPPING DOUBLE NULLS @ 1007, found 15 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x52 0x52                                  RR
##### DEBUG DECIMAL
             82   82
#### RECORD 0 BolusWizard 2015-02-12T21:18:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 60,
 'bg_target_low': 90,
 'bolus_estimate': 1.9,
 'carb_input': 50,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.9,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-12T21:18:50)
    0000   0x32 0x92 0x15 0x6c 0x0f                   2..l.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x3c 0x28 0x5a 0x00 0x01    2P.<(Z..
    0008   0x4c 0x00 0x00 0x00 0x01 0x4c 0x78         L....Lx
    decimal
             50   80    0   60   40   90    0    1
             76    0    0    0    1   76  120

#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 5.55, 'curve': 4},
 {'age': 172, 'amount': 0.45, 'curve': 4},
 {'age': 96, 'amount': 2.0, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0xde 0xa2 0x04 0x12 0xac 0x04    \.......
    0008   0x50 0x60 0x14                             P`.
    decimal
             92   11  222  162    4   18  172    4
             80   96   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2015-02-12T21:21:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1,
 'duration': 180,
 'programmed': 4.1,
 'type': 'square',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x00 0xa4 0x00 0xa4 0x00 0x3c 0x06    ......<.
    decimal
              1    0  164    0  164    0   60    6
    datetime (2015-02-12T21:21:27)
    0000   0x1b 0x95 0xb5 0x6c 0x0f                   ...l.
    body (0)

#### RECORD 3 Ian0B 2015-02-12T21:19:16 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-12T21:19:16)
    0000   0x10 0x93 0x35 0xac 0x0f                   ..5..
    body (0)

#### RECORD 4 Bolus 2015-02-12T21:18:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9,
 'duration': 0,
 'programmed': 3.9,
 'type': 'normal',
 'unabsorbed': 1.5}
```
    op hex (8)
    0000   0x01 0x00 0x9c 0x00 0x9c 0x00 0x3c 0x00    ......<.
    decimal
              1    0  156    0  156    0   60    0
    datetime (2015-02-12T21:18:50)
    0000   0x32 0x92 0x95 0x6c 0x0f                   2..l.
    body (0)

#### RECORD 5 Ian0B 2015-02-12T21:29:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xbe                             .e.
    decimal
             11  101  190
    datetime (2015-02-12T21:29:07)
    0000   0x07 0x9d 0x35 0xac 0x0f                   ..5..
    body (0)

#### RECORD 6 BolusWizard 2015-02-12T21:29:41 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 60,
 'bg_target_low': 90,
 'bolus_estimate': 5.0,
 'carb_input': 30,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-12T21:29:41)
    0000   0x29 0x9d 0x15 0x6c 0x0f                   )..l.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x3c 0x28 0x5a 0x00 0x00    .P.<(Z..
    0008   0xc8 0x00 0x00 0x00 0x00 0xc8 0x78         ......x
    decimal
             30   80    0   60   40   90    0    0
            200    0    0    0    0  200  120

#### RECORD 7 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 3, 'amount': 0.1, 'curve': 4},
 {'age': 13, 'amount': 4.0, 'curve': 4},
 {'age': 173, 'amount': 5.55, 'curve': 4},
 {'age': 183, 'amount': 0.45, 'curve': 4},
 {'age': 107, 'amount': 2.0, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x04 0x03 0x04 0xa0 0x0d 0x04    \.......
    0008   0xde 0xad 0x04 0x12 0xb7 0x04 0x50 0x6b    ......Pk
    0010   0x14                                       .
    decimal
             92   17    4    3    4  160   13    4
            222  173    4   18  183    4   80  107
             20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2015-02-12T21:29:41 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 5.3}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0xd4 0x00    ........
    decimal
              1    0  160    0  160    0  212    0
    datetime (2015-02-12T21:29:41)
    0000   0x29 0x9d 0x55 0x6c 0x0f                   ).Ul.
    body (0)

#### RECORD 9 BasalProfileStart 2015-02-12T22:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 79200000, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x06                                  {.
    decimal
            123    6
    datetime (2015-02-12T22:00:00)
    0000   0x00 0x80 0x16 0x0c 0x0f                   .....
    body (3)
    hex
    0000   0x2c 0x24 0x00                             ,$.
    decimal
             44   36    0

#### RECORD 10 Ian0B 2015-02-12T22:58:18 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-02-12T22:58:18)
    0000   0x12 0xba 0x36 0xac 0x0f                   ..6..
    body (0)

#### RECORD 11 Ian0B 2015-02-12T23:49:35 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-12T23:49:35)
    0000   0x23 0xb1 0x37 0xac 0x0f                   #.7..
    body (0)

#### RECORD 12 BasalProfileStart 2015-02-13T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.9}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2015-02-13T00:00:00)
    0000   0x00 0x80 0x00 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x00 0x24 0x00                             .$.
    decimal
              0   36    0

#### RECORD 13 MResultTotals 2015-02-13T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x0a 0x71                   ....q
    decimal
              7    0    0   10  113
    datetime (2015-02-13T00:00:00)
    0000   0x2c 0x0f                                  ,.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 14 Sara6E 2015-02-13T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2015-02-13T00:00:00)
    0000   0x2c 0x0f                                  ,.
    body (49)
    hex
    0000   0x05 0x10 0xad 0x29 0x30 0x02 0x00 0x00    ...)0...
    0008   0x0a 0x71 0x03 0x51 0x20 0x07 0x20 0x44    .q.Q . D
    0010   0x00 0xa0 0x03 0x34 0x00 0xb8 0x00 0x00    ...4....
    0018   0x03 0x34 0x04 0x01 0x00 0x06 0x00 0xd3    .4......
    0020   0x4a 0x19 0x01 0xeb 0x31 0x04 0x00 0x00    J...1...
    0028   0x00 0x01 0x0d 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5   16  173   41   48    2    0    0
             10  113    3   81   32    7   32   68
              0  160    3   52    0  184    0    0
              3   52    4    1    0    6    0  211
             74   25    1  235   49    4    0    0
              0    1   13    0    0    0    0    0
              0

#### RECORD 15 Ian0B 2015-02-13T00:29:35 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xd7                             .e.
    decimal
             11  101  215
    datetime (2015-02-13T00:29:35)
    0000   0x23 0x9d 0x20 0xad 0x0f                   #. ..
    body (0)

#### RECORD 16 Bolus 2015-02-13T00:32:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 240,
 'programmed': 4.0,
 'type': 'square',
 'unabsorbed': 3.6}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x90 0x08    ........
    decimal
              1    0  160    0  160    0  144    8
    datetime (2015-02-13T00:32:00)
    0000   0x00 0xa0 0xa0 0x0d 0x0f                   .....
    body (0)

#### RECORD 17 LowBattery 2015-02-13T00:31:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2015-02-13T00:31:00)
    0000   0x00 0x9f 0x00 0x0d 0x0f                   .....
    body (0)

#### RECORD 18 Bolus 2015-02-13T00:30:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 3.6}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x90 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  144    0
    datetime (2015-02-13T00:30:40)
    0000   0x28 0x9e 0x80 0x0d 0x0f                   (....
    body (0)

#### RECORD 19 Ian0B 2015-02-13T01:59:16 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xd7                             .e.
    decimal
             11  101  215
    datetime (2015-02-13T01:59:16)
    0000   0x10 0xbb 0x21 0xad 0x0f                   ..!..
    body (0)

#### RECORD 20 Bolus 2015-02-13T02:32:28 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 2.9}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x74 0x00    ......t.
    decimal
              1    0  160    0  160    0  116    0
    datetime (2015-02-13T02:32:28)
    0000   0x1c 0xa0 0x42 0x6d 0x0f                   ..Bm.
    body (0)

#### RECORD 21 Bolus 2015-02-13T02:38:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x01 0x0c 0x00    ........
    decimal
              1    0  140    0  140    1   12    0
    datetime (2015-02-13T02:38:51)
    0000   0x33 0xa6 0x42 0x6d 0x0f                   3.Bm.
    body (0)

#### RECORD 22 BasalProfileStart 2015-02-13T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.9500000000000001}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2015-02-13T04:00:00)
    0000   0x00 0x80 0x04 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x08 0x26 0x00                             .&.
    decimal
              8   38    0

#### RECORD 23 Ian0B 2015-02-13T04:53:01 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-13T04:53:01)
    0000   0x01 0xb5 0x24 0xad 0x0f                   ..$..
    body (0)

#### RECORD 24 Ian0B 2015-02-13T05:03:40 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb7                             .e.
    decimal
             11  101  183
    datetime (2015-02-13T05:03:40)
    0000   0x28 0x83 0x25 0xad 0x0f                   (.%..
    body (0)

#### RECORD 25 Bolus 2015-02-13T05:33:04 head[8], body[0] op[0x01]
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
    datetime (2015-02-13T05:33:04)
    0000   0x04 0xa1 0x45 0x6d 0x0f                   ..Em.
    body (0)

#### RECORD 26 Ian0B 2015-02-13T06:34:28 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xde                             .e.
    decimal
             11  101  222
    datetime (2015-02-13T06:34:28)
    0000   0x1c 0xa2 0x26 0xad 0x0f                   ..&..
    body (0)

#### RECORD 27 Ian0B 2015-02-13T06:45:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-13T06:45:00)
    0000   0x00 0xad 0x26 0xad 0x0f                   ..&..
    body (0)

#### RECORD 28 Bolus 2015-02-13T06:57:24 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5,
 'duration': 0,
 'programmed': 3.5,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0x8c 0x00 0x8c 0x00 0x4c 0x00    ......L.
    decimal
              1    0  140    0  140    0   76    0
    datetime (2015-02-13T06:57:24)
    0000   0x18 0xb9 0x46 0x6d 0x0f                   ..Fm.
    body (0)

#### RECORD 29 BasalProfileStart 2015-02-13T07:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-13T07:00:00)
    0000   0x00 0x80 0x07 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 30 PumpSuspend 2015-02-13T07:10:22 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2015-02-13T07:10:22)
    0000   0x16 0x8a 0x07 0x0d 0x0f                   .....
    body (0)

#### RECORD 31 Battery 2015-02-13T07:28:03 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2015-02-13T07:28:03)
    0000   0x03 0x9c 0x07 0x0d 0x0f                   .....
    body (0)

#### RECORD 32 Battery 2015-02-13T07:28:25 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2015-02-13T07:28:25)
    0000   0x19 0x9c 0x07 0x0d 0x0f                   .....
    body (0)

#### RECORD 33 BasalProfileStart 2015-02-13T07:30:13 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 25200000, 'rate': 0.8500000000000001}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2015-02-13T07:30:13)
    0000   0x0d 0x9e 0x07 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x0e 0x22 0x00                             .".
    decimal
             14   34    0

#### RECORD 34 PumpResume 2015-02-13T07:30:13 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2015-02-13T07:30:13)
    0000   0x0d 0x9e 0x07 0x0d 0x0f                   .....
    body (0)

#### RECORD 35 Ian0B 2015-02-13T07:45:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-13T07:45:00)
    0000   0x00 0xad 0x27 0xad 0x0f                   ..'..
    body (0)

#### RECORD 36 Ian0B 2015-02-13T08:15:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-13T08:15:00)
    0000   0x00 0x8f 0x28 0xad 0x0f                   ..(..
    body (0)

#### RECORD 37 Ian0B 2015-02-13T08:45:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-13T08:45:00)
    0000   0x00 0xad 0x28 0xad 0x0f                   ..(..
    body (0)

#### RECORD 38 CalBGForPH 2015-02-13T08:49:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 99}
```
    op hex (2)
    0000   0x0a 0x63                                  .c
    decimal
             10   99
    datetime (2015-02-13T08:49:52)
    0000   0x34 0xb1 0x28 0x6d 0x0f                   4.(m.
    body (0)

#### RECORD 39 Ian3F 2015-02-13T08:49:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2015-02-13T08:49:52)
    0000   0x34 0xb1 0x68 0x6d 0x0f                   4.hm.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

#### RECORD 40 BolusWizard 2015-02-13T09:02:22 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 100,
 'bg_target_low': 90,
 'bolus_estimate': 4.5,
 'carb_input': 45,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-13T09:02:22)
    0000   0x16 0x82 0x09 0x6d 0x0f                   ...m.
    body (15)
    hex
    0000   0x2d 0x50 0x00 0x64 0x28 0x5a 0x00 0x00    -P.d(Z..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x78         ......x
    decimal
             45   80    0  100   40   90    0    0
            180    0    0    0    0  180  120

#### RECORD 41 UnabsorbedInsulinBolus unknown head[71], body[0] op[0x5c]
###### DECODED
```python
[{'age': 126, 'amount': 3.5, 'curve': 4},
 {'age': 216, 'amount': 2.5, 'curve': 4},
 {'age': 20, 'amount': 0.15, 'curve': 20},
 {'age': 30, 'amount': 0.15, 'curve': 20},
 {'age': 40, 'amount': 0.15, 'curve': 20},
 {'age': 50, 'amount': 0.2, 'curve': 20},
 {'age': 60, 'amount': 0.15, 'curve': 20},
 {'age': 70, 'amount': 0.15, 'curve': 20},
 {'age': 80, 'amount': 0.2, 'curve': 20},
 {'age': 90, 'amount': 0.15, 'curve': 20},
 {'age': 100, 'amount': 0.15, 'curve': 20},
 {'age': 110, 'amount': 0.2, 'curve': 20},
 {'age': 120, 'amount': 0.15, 'curve': 20},
 {'age': 130, 'amount': 3.65, 'curve': 20},
 {'age': 140, 'amount': 4.15, 'curve': 20},
 {'age': 150, 'amount': 0.15, 'curve': 20},
 {'age': 160, 'amount': 0.2, 'curve': 20},
 {'age': 170, 'amount': 0.15, 'curve': 20},
 {'age': 180, 'amount': 0.15, 'curve': 20},
 {'age': 190, 'amount': 0.2, 'curve': 20},
 {'age': 200, 'amount': 0.15, 'curve': 20},
 {'age': 210, 'amount': 0.15, 'curve': 20},
 {'age': 220, 'amount': 0.2, 'curve': 20}]
```
    op hex (71)
    0000   0x5c 0x47 0x8c 0x7e 0x04 0x64 0xd8 0x04    \G.~.d..
    0008   0x06 0x14 0x14 0x06 0x1e 0x14 0x06 0x28    .......(
    0010   0x14 0x08 0x32 0x14 0x06 0x3c 0x14 0x06    ..2..<..
    0018   0x46 0x14 0x08 0x50 0x14 0x06 0x5a 0x14    F..P..Z.
    0020   0x06 0x64 0x14 0x08 0x6e 0x14 0x06 0x78    .d..n..x
    0028   0x14 0x92 0x82 0x14 0xa6 0x8c 0x14 0x06    ........
    0030   0x96 0x14 0x08 0xa0 0x14 0x06 0xaa 0x14    ........
    0038   0x06 0xb4 0x14 0x08 0xbe 0x14 0x06 0xc8    ........
    0040   0x14 0x06 0xd2 0x14 0x08 0xdc 0x14         .......
    decimal
             92   71  140  126    4  100  216    4
              6   20   20    6   30   20    6   40
             20    8   50   20    6   60   20    6
             70   20    8   80   20    6   90   20
              6  100   20    8  110   20    6  120
             20  146  130   20  166  140   20    6
            150   20    8  160   20    6  170   20
              6  180   20    8  190   20    6  200
             20    6  210   20    8  220   20
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2015-02-13T09:03:35 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7,
 'duration': 120,
 'programmed': 2.7,
 'type': 'square',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x48 0x04    ..l.l.H.
    decimal
              1    0  108    0  108    0   72    4
    datetime (2015-02-13T09:03:35)
    0000   0x23 0x83 0xa9 0x6d 0x0f                   #..m.
    body (0)

#### RECORD 43 Bolus 2015-02-13T09:02:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 0,
 'programmed': 1.8,
 'type': 'normal',
 'unabsorbed': 1.8}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x48 0x00    ..H.H.H.
    decimal
              1    0   72    0   72    0   72    0
    datetime (2015-02-13T09:02:23)
    0000   0x17 0x82 0x89 0x6d 0x0f                   ...m.
    body (0)

#### RECORD 44 BasalProfileStart 2015-02-13T10:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 36000000, 'rate': 0.875}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2015-02-13T10:00:00)
    0000   0x00 0x80 0x0a 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x14 0x23 0x00                             .#.
    decimal
             20   35    0

#### RECORD 45 Ian0B 2015-02-13T10:39:16 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-13T10:39:16)
    0000   0x10 0xa7 0x2a 0xad 0x0f                   ..*..
    body (0)

#### RECORD 46 Ian0B 2015-02-13T10:49:07 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb4                             .e.
    decimal
             11  101  180
    datetime (2015-02-13T10:49:07)
    0000   0x07 0xb1 0x2a 0xad 0x0f                   ..*..
    body (0)

#### RECORD 47 BasalProfileStart 2015-02-13T12:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 43200000, 'rate': 0.75}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2015-02-13T12:00:00)
    0000   0x00 0x80 0x0c 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x18 0x1e 0x00                             ...
    decimal
             24   30    0

#### RECORD 48 Ian0B 2015-02-13T12:18:18 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xbc                             .e.
    decimal
             11  101  188
    datetime (2015-02-13T12:18:18)
    0000   0x12 0x92 0x2c 0xad 0x0f                   ..,..
    body (0)

#### RECORD 49 BolusWizard 2015-02-13T12:34:46 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 48,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-13T12:34:46)
    0000   0x2e 0xa2 0x0c 0x6d 0x0f                   ...m.
    body (15)
    hex
    0000   0x30 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    0P.P(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             48   80    0   80   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 50 UnabsorbedInsulinBolus unknown head[47], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 0.15, 'curve': 4},
 {'age': 108, 'amount': 0.25, 'curve': 4},
 {'age': 118, 'amount': 0.2, 'curve': 4},
 {'age': 128, 'amount': 0.25, 'curve': 4},
 {'age': 138, 'amount': 0.2, 'curve': 4},
 {'age': 148, 'amount': 0.25, 'curve': 4},
 {'age': 158, 'amount': 0.2, 'curve': 4},
 {'age': 168, 'amount': 0.25, 'curve': 4},
 {'age': 178, 'amount': 0.2, 'curve': 4},
 {'age': 188, 'amount': 0.25, 'curve': 4},
 {'age': 198, 'amount': 0.2, 'curve': 4},
 {'age': 208, 'amount': 0.25, 'curve': 4},
 {'age': 218, 'amount': 1.85, 'curve': 4},
 {'age': 82, 'amount': 3.5, 'curve': 20},
 {'age': 172, 'amount': 2.5, 'curve': 20}]
```
    op hex (47)
    0000   0x5c 0x2f 0x06 0x62 0x04 0x0a 0x6c 0x04    \/.b..l.
    0008   0x08 0x76 0x04 0x0a 0x80 0x04 0x08 0x8a    .v......
    0010   0x04 0x0a 0x94 0x04 0x08 0x9e 0x04 0x0a    ........
    0018   0xa8 0x04 0x08 0xb2 0x04 0x0a 0xbc 0x04    ........
    0020   0x08 0xc6 0x04 0x0a 0xd0 0x04 0x4a 0xda    ......J.
    0028   0x04 0x8c 0x52 0x14 0x64 0xac 0x14         ..R.d..
    decimal
             92   47    6   98    4   10  108    4
              8  118    4   10  128    4    8  138
              4   10  148    4    8  158    4   10
            168    4    8  178    4   10  188    4
              8  198    4   10  208    4   74  218
              4  140   82   20  100  172   20
    datetime (unknown)

    body (0)

#### RECORD 51 BolusWizard 2015-02-13T12:34:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 6.0,
 'carb_input': 48,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-13T12:34:48)
    0000   0x30 0xa2 0x0c 0x6d 0x0f                   0..m.
    body (15)
    hex
    0000   0x30 0x50 0x00 0x50 0x28 0x5a 0x00 0x00    0P.P(Z..
    0008   0xf0 0x00 0x00 0x00 0x00 0xf0 0x78         ......x
    decimal
             48   80    0   80   40   90    0    0
            240    0    0    0    0  240  120

#### RECORD 52 UnabsorbedInsulinBolus unknown head[47], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 0.15, 'curve': 4},
 {'age': 108, 'amount': 0.25, 'curve': 4},
 {'age': 118, 'amount': 0.2, 'curve': 4},
 {'age': 128, 'amount': 0.25, 'curve': 4},
 {'age': 138, 'amount': 0.2, 'curve': 4},
 {'age': 148, 'amount': 0.25, 'curve': 4},
 {'age': 158, 'amount': 0.2, 'curve': 4},
 {'age': 168, 'amount': 0.25, 'curve': 4},
 {'age': 178, 'amount': 0.2, 'curve': 4},
 {'age': 188, 'amount': 0.25, 'curve': 4},
 {'age': 198, 'amount': 0.2, 'curve': 4},
 {'age': 208, 'amount': 0.25, 'curve': 4},
 {'age': 218, 'amount': 1.85, 'curve': 4},
 {'age': 82, 'amount': 3.5, 'curve': 20},
 {'age': 172, 'amount': 2.5, 'curve': 20}]
```
    op hex (47)
    0000   0x5c 0x2f 0x06 0x62 0x04 0x0a 0x6c 0x04    \/.b..l.
    0008   0x08 0x76 0x04 0x0a 0x80 0x04 0x08 0x8a    .v......
    0010   0x04 0x0a 0x94 0x04 0x08 0x9e 0x04 0x0a    ........
    0018   0xa8 0x04 0x08 0xb2 0x04 0x0a 0xbc 0x04    ........
    0020   0x08 0xc6 0x04 0x0a 0xd0 0x04 0x4a 0xda    ......J.
    0028   0x04 0x8c 0x52 0x14 0x64 0xac 0x14         ..R.d..
    decimal
             92   47    6   98    4   10  108    4
              8  118    4   10  128    4    8  138
              4   10  148    4    8  158    4   10
            168    4    8  178    4   10  188    4
              8  198    4   10  208    4   74  218
              4  140   82   20  100  172   20
    datetime (unknown)

    body (0)

#### RECORD 53 BolusWizard 2015-02-13T12:34:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 80,
 'bg_target_low': 90,
 'bolus_estimate': 1.6,
 'carb_input': 64,
 'carb_ratio': 12.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.6,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2015-02-13T12:34:59)
    0000   0x3b 0xa2 0x0c 0x6d 0x0f                   ;..m.
    body (15)
    hex
    0000   0x40 0x50 0x00 0x50 0x28 0x5a 0x00 0x01    @P.P(Z..
    0008   0x40 0x00 0x00 0x00 0x01 0x40 0x78         @....@x
    decimal
             64   80    0   80   40   90    0    1
             64    0    0    0    1   64  120

#### RECORD 54 UnabsorbedInsulinBolus unknown head[47], body[0] op[0x5c]
###### DECODED
```python
[{'age': 98, 'amount': 0.15, 'curve': 4},
 {'age': 108, 'amount': 0.25, 'curve': 4},
 {'age': 118, 'amount': 0.2, 'curve': 4},
 {'age': 128, 'amount': 0.25, 'curve': 4},
 {'age': 138, 'amount': 0.2, 'curve': 4},
 {'age': 148, 'amount': 0.25, 'curve': 4},
 {'age': 158, 'amount': 0.2, 'curve': 4},
 {'age': 168, 'amount': 0.25, 'curve': 4},
 {'age': 178, 'amount': 0.2, 'curve': 4},
 {'age': 188, 'amount': 0.25, 'curve': 4},
 {'age': 198, 'amount': 0.2, 'curve': 4},
 {'age': 208, 'amount': 0.25, 'curve': 4},
 {'age': 218, 'amount': 1.85, 'curve': 4},
 {'age': 82, 'amount': 3.5, 'curve': 20},
 {'age': 172, 'amount': 2.5, 'curve': 20}]
```
    op hex (47)
    0000   0x5c 0x2f 0x06 0x62 0x04 0x0a 0x6c 0x04    \/.b..l.
    0008   0x08 0x76 0x04 0x0a 0x80 0x04 0x08 0x8a    .v......
    0010   0x04 0x0a 0x94 0x04 0x08 0x9e 0x04 0x0a    ........
    0018   0xa8 0x04 0x08 0xb2 0x04 0x0a 0xbc 0x04    ........
    0020   0x08 0xc6 0x04 0x0a 0xd0 0x04 0x4a 0xda    ......J.
    0028   0x04 0x8c 0x52 0x14 0x64 0xac 0x14         ..R.d..
    decimal
             92   47    6   98    4   10  108    4
              8  118    4   10  128    4    8  138
              4   10  148    4    8  158    4   10
            168    4    8  178    4   10  188    4
              8  198    4   10  208    4   74  218
              4  140   82   20  100  172   20
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2015-02-13T12:38:22 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 90,
 'programmed': 3.0,
 'type': 'square',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x28 0x03    ..x.x.(.
    decimal
              1    0  120    0  120    0   40    3
    datetime (2015-02-13T12:38:22)
    0000   0x16 0xa6 0xac 0x6d 0x0f                   ...m.
    body (0)

#### RECORD 56 Bolus 2015-02-13T12:35:00 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0,
 'duration': 0,
 'programmed': 5.0,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0xc8 0x00 0xc8 0x00 0x28 0x00    ......(.
    decimal
              1    0  200    0  200    0   40    0
    datetime (2015-02-13T12:35:00)
    0000   0x00 0xa3 0x8c 0x6d 0x0f                   ...m.
    body (0)

#### RECORD 57 Bolus 2015-02-13T12:46:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 6.0}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0xf0 0x00    ..<.<...
    decimal
              1    0   60    0   60    0  240    0
    datetime (2015-02-13T12:46:27)
    0000   0x1b 0xae 0x4c 0x6d 0x0f                   ..Lm.
    body (0)

#### RECORD 58 LowReservoir 2015-02-13T13:24:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2015-02-13T13:24:00)
    0000   0x00 0x98 0x0d 0x0d 0x0f                   .....
    body (0)

#### RECORD 59 BasalProfileStart 2015-02-13T15:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 54000000, 'rate': 0.8}
```
    op hex (2)
    0000   0x7b 0x05                                  {.
    decimal
            123    5
    datetime (2015-02-13T15:00:00)
    0000   0x00 0x80 0x0f 0x0d 0x0f                   .....
    body (3)
    hex
    0000   0x1e 0x20 0x00                             . .
    decimal
             30   32    0

#### RECORD 60 Ian0B 2015-02-13T16:13:01 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-13T16:13:01)
    0000   0x01 0x8d 0x30 0xad 0x0f                   ..0..
    body (0)

#### RECORD 61 Ian0B 2015-02-13T16:23:40 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xb9                             .e.
    decimal
             11  101  185
    datetime (2015-02-13T16:23:40)
    0000   0x28 0x97 0x30 0xad 0x0f                   (.0..
    body (0)

#### RECORD 62 Bolus 2015-02-13T17:23:31 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0,
 'duration': 0,
 'programmed': 4.0,
 'type': 'normal',
 'unabsorbed': 0.2}
```
    op hex (8)
    0000   0x01 0x00 0xa0 0x00 0xa0 0x00 0x08 0x00    ........
    decimal
              1    0  160    0  160    0    8    0
    datetime (2015-02-13T17:23:31)
    0000   0x1f 0x97 0x51 0x6d 0x0f                   ..Qm.
    body (0)

#### RECORD 63 Ian0B 2015-02-13T17:54:28 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x65 0xd9                             .e.
    decimal
             11  101  217
    datetime (2015-02-13T17:54:28)
    0000   0x1c 0xb6 0x31 0xad 0x0f                   ..1..
    body (0)

#### RECORD 64 LowReservoir 2015-02-13T17:55:20 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2015-02-13T17:55:20)
    0000   0x14 0xb7 0x11 0x0d 0x0f                   .....
    body (0)

#### RECORD 65 Bolus 2015-02-13T17:54:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 3.8}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x98 0x00    ..P.P...
    decimal
              1    0   80    0   80    0  152    0
    datetime (2015-02-13T17:54:42)
    0000   0x2a 0xb6 0x51 0x6d 0x0f                   *.Qm.
    body (0)

#### RECORD 66 Ian0B 2015-02-13T18:53:01 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x73 0x00                             .s.
    decimal
             11  115    0
    datetime (2015-02-13T18:53:01)
    0000   0x01 0xb5 0x32 0xad 0x0f                   ..2..
    body (0)

#### RECORD 67 Ian0B 2015-02-13T19:09:35 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x4f                             .fO
    decimal
             11  102   79
    datetime (2015-02-13T19:09:35)
    0000   0x23 0x89 0x33 0xad 0x0f                   #.3..
    body (0)

#### RECORD 68 Ian0B 2015-02-13T19:38:18 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x66 0x49                             .fI
    decimal
             11  102   73
    datetime (2015-02-13T19:38:18)
    0000   0x12 0xa6 0x33 0xad 0x0f                   ..3..
    body (0)

#### RECORD 69 Ian0B 2015-02-13T19:51:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x69 0x00                             .i.
    decimal
             11  105    0
    datetime (2015-02-13T19:51:00)
    0000   0x00 0xb3 0x33 0xad 0x0f                   ..3..
    body (0)

#### RECORD 70 Ian0B 2015-02-13T20:42:59 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x72 0x00                             .r.
    decimal
             11  114    0
    datetime (2015-02-13T20:42:59)
    0000   0x3b 0xaa 0x34 0xad 0x0f                   ;.4..
    body (0)

#### RECORD 71 Ian0B 2015-02-13T20:51:00 head[3], body[0] op[0x0b]

    op hex (3)
    0000   0x0b 0x68 0x00                             .h.
    decimal
             11  104    0
    datetime (2015-02-13T20:51:00)
    0000   0x00 0xb3 0x34 0xad 0x0f                   ..4..
    body (0)

#### RECORD 72 CalBGForPH 2015-02-13T20:53:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 245}
```
    op hex (2)
    0000   0x0a 0xf5                                  ..
    decimal
             10  245
    datetime (2015-02-13T20:53:08)
    0000   0x08 0xb5 0x34 0x6d 0x0f                   ..4m.
    body (0)

#### RECORD 73 Ian3F 2015-02-13T20:53:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1e                                  ?.
    decimal
             63   30
    datetime (2015-02-13T20:53:08)
    0000   0x08 0xb5 0xb4 0x6d 0x0f                   ...m.
    body (3)
    hex
    0000   0x78 0x34 0x36                             x46
    decimal
            120   52   54

`end analysis/736868/logs/ReadHistoryData-page-30.data: 74 records`
