## all of ~ba's data

```
+ for x in 'brandon-ReadHistoryData-page-*.data'
+ echo brandon-ReadHistoryData-page-0.data
brandon-ReadHistoryData-page-0.data
+ python list_history.py --larger brandon-ReadHistoryData-page-0.data
```
## START brandon-ReadHistoryData-page-0.data
#### STOPPING DOUBLE NULLS @ 475, found 547 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x10 0x33                                  .3
##### DEBUG DECIMAL
             16   51
#### RECORD 0 Bolus 2014-07-01T01:28:30 head[8], body[0] op[0x01]
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
    datetime (2014-07-01T01:28:30)
    0000   0x5e 0xdc 0x41 0x01 0x0e                   ^.A..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 1 BasalProfileStart 2014-07-01T06:48:22 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-07-01T06:48:22)
    0000   0x56 0xf0 0x06 0x01 0x0e                   V....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 1, 1]
#### RECORD 2 CalBGForPH 2014-07-01T09:47:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2014-07-01T09:47:11)
    0000   0x4b 0xef 0x29 0x61 0x0e                   K.)a.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 Ian3F 2014-07-01T09:47:11 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-07-01T09:47:11)
    0000   0x4b 0xef 0x69 0x61 0x0e                   K.ia.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 BolusWizard 2014-07-01T09:50:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 131,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 0.7,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x83                                  [.
    decimal
             91  131
    datetime (2014-07-01T09:50:30)
    0000   0x5e 0xf2 0x09 0x01 0x0e                   ^....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x28 0x50 0x1c 0x00    .P.n(P..
    0008   0x00 0x00 0x00 0x00 0x00 0x1c 0x64         ......d
    decimal
              0   80    0  110   40   80   28    0
              0    0    0    0    0   28  100
    HOUR BITS: [1, 1, 1]
#### RECORD 5 Bolus 2014-07-01T09:50:30 head[8], body[0] op[0x01]
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
    datetime (2014-07-01T09:50:30)
    0000   0x5e 0xf2 0x49 0x01 0x0e                   ^.I..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 LowReservoir 2014-07-01T10:11:36 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2014-07-01T10:11:36)
    0000   0x64 0xcb 0x0a 0x01 0x0e                   d....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 7 BasalProfileStart 2014-07-01T10:30:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-07-01T10:30:00)
    0000   0x40 0xde 0x0a 0x01 0x0e                   @....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 1, 0]
#### RECORD 8 PumpSuspend 2014-07-01T12:51:40 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-07-01T12:51:40)
    0000   0x68 0xf3 0x0c 0x01 0x0e                   h....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 9 BasalProfileStart 2014-07-01T14:25:57 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-07-01T14:25:57)
    0000   0x79 0xd9 0x0e 0x01 0x0e                   y....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 1, 0]
#### RECORD 10 PumpResume 2014-07-01T14:25:57 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-07-01T14:25:57)
    0000   0x79 0xd9 0x0e 0x01 0x0e                   y....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 PumpSuspend 2014-07-01T16:41:32 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-07-01T16:41:32)
    0000   0x60 0xe9 0x10 0x01 0x0e                   `....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 12 CalBGForPH 2014-07-01T18:16:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2014-07-01T18:16:11)
    0000   0x4b 0xd0 0x32 0x61 0x0e                   K.2a.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 Ian3F 2014-07-01T18:16:11 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-07-01T18:16:11)
    0000   0x4b 0xd0 0x12 0x61 0x0e                   K..a.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 BasalProfileStart 2014-07-01T20:01:31 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-07-01T20:01:31)
    0000   0x5f 0xc1 0x14 0x01 0x0e                   _....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 1, 0]
#### RECORD 15 PumpResume 2014-07-01T20:01:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-07-01T20:01:31)
    0000   0x5f 0xc1 0x14 0x01 0x0e                   _....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 16 CalBGForPH 2014-07-01T20:02:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 210}
```
    op hex (2)
    0000   0x0a 0xd2                                  ..
    decimal
             10  210
    datetime (2014-07-01T20:02:06)
    0000   0x46 0xc2 0x34 0x01 0x0e                   F.4..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 17 BolusWizard 2014-07-01T20:02:12 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 210,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.2,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 2.2,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xd2                                  [.
    decimal
             91  210
    datetime (2014-07-01T20:02:12)
    0000   0x4c 0xc2 0x14 0x01 0x0e                   L....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x32 0x50 0x58 0x00    .P.n2PX.
    0008   0x00 0x00 0x00 0x00 0x00 0x58 0x64         .....Xd
    decimal
              0   80    0  110   50   80   88    0
              0    0    0    0    0   88  100
    HOUR BITS: [1, 1, 0]
#### RECORD 18 Bolus 2014-07-01T20:02:12 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1,
 'duration': 0,
 'programmed': 1.1,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x00 0x00    ..,.,...
    decimal
              1    0   44    0   44    0    0    0
    datetime (2014-07-01T20:02:12)
    0000   0x4c 0xc2 0x54 0x01 0x0e                   L.T..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 19 CalBGForPH 2014-07-01T20:39:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 208}
```
    op hex (2)
    0000   0x0a 0xd0                                  ..
    decimal
             10  208
    datetime (2014-07-01T20:39:27)
    0000   0x5b 0xe7 0x34 0x61 0x0e                   [.4a.
    body (0)
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 Ian3F 2014-07-01T20:39:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1a                                  ?.
    decimal
             63   26
    datetime (2014-07-01T20:39:27)
    0000   0x5b 0xe7 0x14 0x61 0x0e                   [..a.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 BolusWizard 2014-07-01T20:39:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 208,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 4.9,
 'carb_input': 40,
 'carb_ratio': 10.0,
 'correction_estimate': 2.1,
 'food_estimate': 3.6,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.8}
```
    op hex (2)
    0000   0x5b 0xd0                                  [.
    decimal
             91  208
    datetime (2014-07-01T20:39:50)
    0000   0x72 0xe7 0x14 0x01 0x0e                   r....
    body (15)
    hex
    0000   0x28 0x50 0x00 0x6e 0x32 0x50 0x54 0x00    (P.n2PT.
    0008   0x90 0x00 0x00 0x20 0x00 0xc4 0x64         ... ..d
    decimal
             40   80    0  110   50   80   84    0
            144    0    0   32    0  196  100
    HOUR BITS: [1, 1, 1]
#### RECORD 22 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 39, 'amount': 1.1, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x2c 0x27 0x80                   \.,'.
    decimal
             92    5   44   39  128
    datetime (unknown)

    body (0)

#### RECORD 23 Bolus 2014-07-01T20:39:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.9,
 'duration': 0,
 'programmed': 4.9,
 'type': 'normal',
 'unabsorbed': 0.8}
```
    op hex (8)
    0000   0x01 0x00 0xc4 0x00 0xc4 0x00 0x20 0x00    ...... .
    decimal
              1    0  196    0  196    0   32    0
    datetime (2014-07-01T20:39:50)
    0000   0x72 0xe7 0x54 0x01 0x0e                   r.T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 CalBGForPH 2014-07-01T22:01:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2014-07-01T22:01:37)
    0000   0x65 0xc1 0x36 0x61 0x0e                   e.6a.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 Ian3F 2014-07-01T22:01:37 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2014-07-01T22:01:37)
    0000   0x65 0xc1 0xd6 0x61 0x0e                   e..a.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 BolusWizard 2014-07-01T22:01:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 206,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 2.1,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 1.2}
```
    op hex (2)
    0000   0x5b 0xce                                  [.
    decimal
             91  206
    datetime (2014-07-01T22:01:57)
    0000   0x79 0xc1 0x16 0x01 0x0e                   y....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x32 0x50 0x54 0x00    .P.n2PT.
    0008   0x00 0x00 0x00 0x30 0x00 0x24 0x64         ...0.$d
    decimal
              0   80    0  110   50   80   84    0
              0    0    0   48    0   36  100
    HOUR BITS: [1, 1, 0]
#### RECORD 27 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 81, 'amount': 4.65, 'curve': 128},
 {'age': 91, 'amount': 0.25, 'curve': 128},
 {'age': 121, 'amount': 1.1, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0xba 0x51 0x80 0x0a 0x5b 0x80    \..Q..[.
    0008   0x2c 0x79 0x80                             ,y.
    decimal
             92   11  186   81  128   10   91  128
             44  121  128
    datetime (unknown)

    body (0)

#### RECORD 28 LowReservoir 2014-07-01T22:02:21 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2014-07-01T22:02:21)
    0000   0x55 0xc2 0x16 0x01 0x0e                   U....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 29 Bolus 2014-07-01T22:01:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 1.2}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x30 0x00    ..<.<.0.
    decimal
              1    0   60    0   60    0   48    0
    datetime (2014-07-01T22:01:57)
    0000   0x79 0xc1 0x56 0x01 0x0e                   y.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 30 PumpSuspend 2014-07-01T22:11:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-07-01T22:11:29)
    0000   0x5d 0xcb 0x16 0x01 0x0e                   ]....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 31 MResultTotals 2014-07-02T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x02 0xd9                   .....
    decimal
              7    0    0    2  217
    datetime (2014-07-02T00:00:00)
    0000   0x61 0x8e                                  a.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0
    HOUR BITS: [1, 0, 0]
#### RECORD 32 Sara6E 2014-07-02T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-07-02T00:00:00)
    0000   0x61 0x8e                                  a.
    body (49)
    hex
    0000   0x05 0x00 0xaf 0x83 0xd0 0x06 0x00 0x00    ........
    0008   0x02 0xd9 0x01 0x49 0x2d 0x01 0x90 0x37    ...I-..7
    0010   0x00 0x28 0x00 0x00 0x00 0xcc 0x00 0xc4    .(......
    0018   0x00 0x00 0x00 0x04 0x01 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xa1    ........
    0028   0xd2 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  175  131  208    6    0    0
              2  217    1   73   45    1  144   55
              0   40    0    0    0  204    0  196
              0    0    0    4    1    0    0    0
              0    0    0    0    0    0    0  161
            210    0    0    0    0    0    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 33 CalBGForPH 2014-07-02T00:13:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 131}
```
    op hex (2)
    0000   0x0a 0x83                                  ..
    decimal
             10  131
    datetime (2014-07-02T00:13:47)
    0000   0x6f 0xcd 0x20 0x62 0x0e                   o. b.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 Ian3F 2014-07-02T00:13:47 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-07-02T00:13:47)
    0000   0x6f 0xcd 0x60 0x62 0x0e                   o.`b.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 BasalProfileStart 2014-07-02T01:16:35 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-07-02T01:16:35)
    0000   0x63 0xd0 0x01 0x02 0x0e                   c....
    body (3)
    hex
    0000   0x00 0x19 0x00                             ...
    decimal
              0   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 36 PumpResume 2014-07-02T01:16:35 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-07-02T01:16:35)
    0000   0x63 0xd0 0x01 0x02 0x0e                   c....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 37 BasalProfileStart 2014-07-02T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-07-02T04:00:00)
    0000   0x40 0xc0 0x04 0x02 0x0e                   @....
    body (3)
    hex
    0000   0x08 0x19 0x00                             ...
    decimal
              8   25    0
    HOUR BITS: [1, 1, 0]
#### RECORD 38 BasalProfileStart 2014-07-02T06:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-07-02T06:00:00)
    0000   0x40 0xc0 0x06 0x02 0x0e                   @....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 1, 0]
#### RECORD 39 PumpSuspend 2014-07-02T09:00:23 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-07-02T09:00:23)
    0000   0x57 0xc0 0x09 0x02 0x0e                   W....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 40 CalBGForPH 2014-07-02T09:04:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2014-07-02T09:04:43)
    0000   0x6b 0xc4 0x29 0x62 0x0e                   k.)b.
    body (0)
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2014-07-02T09:04:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2014-07-02T09:04:43)
    0000   0x6b 0xc4 0x09 0x62 0x0e                   k..b.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 1, 0] DAY BITS: [0, 1, 1]
`end brandon-ReadHistoryData-page-0.data: 42 records`
```
+ for x in 'brandon-ReadHistoryData-page-*.data'
+ echo brandon-ReadHistoryData-page-1.data
brandon-ReadHistoryData-page-1.data
+ python list_history.py --larger brandon-ReadHistoryData-page-1.data
```
## START brandon-ReadHistoryData-page-1.data
ERROR day is out of range for month (2014, 6, 31, 0, 0, 0) 0000   0x7e 0x0e                                  ~.
ERROR day is out of range for month 0000   0x7e 0x0e                                  ~.
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xa0 0x1a                                  ..
##### DEBUG DECIMAL
            160   26
#### RECORD 0 Sara6E 2014-06-30T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-30T00:00:00)
    0000   0x7d 0x0e                                  }.
    body (49)
    hex
    0000   0x05 0x00 0x9e 0x4e 0xce 0x09 0x00 0x00    ...N....
    0008   0x04 0x54 0x01 0xa4 0x26 0x02 0xb0 0x3e    .T..&..>
    0010   0x00 0x6e 0x01 0x8c 0x01 0x14 0x00 0x00    .n......
    0018   0x00 0x10 0x04 0x04 0x00 0x01 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xb6    ........
    0028   0xb6 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  158   78  206    9    0    0
              4   84    1  164   38    2  176   62
              0  110    1  140    1   20    0    0
              0   16    4    4    0    1    0    0
              0    0    0    0    0    0    0  182
            182    0    0    0    0    0    0    0
              0

#### RECORD 1 TempBasal 2014-06-30T02:00:43 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-06-30T02:00:43)
    0000   0x6b 0x80 0x02 0x1e 0x0e                   k....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 0, 0]
#### RECORD 2 TempBasalDuration 2014-06-30T02:00:43 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2014-06-30T02:00:43)
    0000   0x6b 0x80 0x02 0x1e 0x0e                   k....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 BasalProfileStart 2014-06-30T02:00:43 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-06-30T02:00:43)
    0000   0x6b 0x80 0x02 0x1e 0x0e                   k....
    body (3)
    hex
    0000   0x00 0x19 0x00                             ...
    decimal
              0   25    0
    HOUR BITS: [1, 0, 0]
#### RECORD 4 TempBasal 2014-06-30T02:00:57 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.25}
```
    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2014-06-30T02:00:57)
    0000   0x79 0x80 0x02 0x1e 0x0e                   y....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 0, 0]
#### RECORD 5 TempBasalDuration 2014-06-30T02:00:57 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 360}
```
    op hex (2)
    0000   0x16 0x0c                                  ..
    decimal
             22   12
    datetime (2014-06-30T02:00:57)
    0000   0x79 0x80 0x02 0x1e 0x0e                   y....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 BasalProfileStart 2014-06-30T08:00:57 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-06-30T08:00:57)
    0000   0x79 0x80 0x08 0x1e 0x0e                   y....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 0, 0]
#### RECORD 7 BasalProfileStart 2014-06-30T10:30:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-30T10:30:00)
    0000   0x40 0x9e 0x0a 0x1e 0x0e                   @....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 8 PumpSuspend 2014-06-30T10:44:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-30T10:44:49)
    0000   0x71 0xac 0x0a 0x1e 0x0e                   q....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 CalBGForPH 2014-06-30T12:25:09 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 88}
```
    op hex (2)
    0000   0x0a 0x58                                  .X
    decimal
             10   88
    datetime (2014-06-30T12:25:09)
    0000   0x49 0x99 0x2c 0x7e 0x0e                   I.,~.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 Ian3F 2014-06-30T12:25:09 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-06-30T12:25:09)
    0000   0x49 0x99 0x0c 0x7e 0x0e                   I..~.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 11 BasalProfileStart 2014-06-30T13:23:02 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-30T13:23:02)
    0000   0x42 0x97 0x0d 0x1e 0x0e                   B....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 12 PumpResume 2014-06-30T13:23:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-30T13:23:02)
    0000   0x42 0x97 0x0d 0x1e 0x0e                   B....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 13 CalBGForPH 2014-06-30T13:23:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2014-06-30T13:23:12)
    0000   0x4c 0x97 0x2d 0x1e 0x0e                   L.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 14 BolusWizard 2014-06-30T13:23:21 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 132,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 2.2,
 'carb_input': 20,
 'carb_ratio': 10.0,
 'correction_estimate': 0.6,
 'food_estimate': 1.6,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2014-06-30T13:23:21)
    0000   0x55 0x97 0x0d 0x1e 0x0e                   U....
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x32 0x50 0x18 0x00    .P.x2P..
    0008   0x40 0x00 0x00 0x00 0x00 0x58 0x64         @....Xd
    decimal
             20   80    0  120   50   80   24    0
             64    0    0    0    0   88  100
    HOUR BITS: [1, 0, 0]
#### RECORD 15 Bolus 2014-06-30T13:23:21 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2,
 'duration': 0,
 'programmed': 2.2,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x00 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    0    0
    datetime (2014-06-30T13:23:21)
    0000   0x55 0x97 0x4d 0x1e 0x0e                   U.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 16 BolusWizard 2014-06-30T13:36:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 132,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 3.3,
 'carb_input': 40,
 'carb_ratio': 10.0,
 'correction_estimate': 0.6,
 'food_estimate': 3.3,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 2.1}
```
    op hex (2)
    0000   0x5b 0x84                                  [.
    decimal
             91  132
    datetime (2014-06-30T13:36:04)
    0000   0x44 0xa4 0x0d 0x7e 0x0e                   D..~.
    body (15)
    hex
    0000   0x28 0x50 0x00 0x78 0x32 0x50 0x18 0x00    (P.x2P..
    0008   0x84 0x00 0x00 0x54 0x00 0x84 0x64         ...T..d
    decimal
             40   80    0  120   50   80   24    0
            132    0    0   84    0  132  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 2.2, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x58 0x10 0x80                   \.X..
    decimal
             92    5   88   16  128
    datetime (unknown)

    body (0)

#### RECORD 18 Bolus 2014-06-30T13:36:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3,
 'duration': 0,
 'programmed': 3.3,
 'type': 'normal',
 'unabsorbed': 2.1}
```
    op hex (8)
    0000   0x01 0x00 0x84 0x00 0x84 0x00 0x54 0x00    ......T.
    decimal
              1    0  132    0  132    0   84    0
    datetime (2014-06-30T13:36:04)
    0000   0x44 0xa4 0x4d 0x7e 0x0e                   D.M~.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 19 BolusWizard 2014-06-30T13:47:13 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 3.3,
 'carb_input': 40,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.3,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-30T13:47:13)
    0000   0x4d 0xaf 0x0d 0x1e 0x0e                   M....
    body (15)
    hex
    0000   0x28 0x50 0x00 0x78 0x32 0x50 0x00 0x00    (P.x2P..
    0008   0x84 0x00 0x00 0x00 0x00 0x84 0x64         ......d
    decimal
             40   80    0  120   50   80    0    0
            132    0    0    0    0  132  100
    HOUR BITS: [1, 0, 1]
#### RECORD 20 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 3.3, 'curve': 128},
 {'age': 27, 'amount': 2.2, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x84 0x11 0x80 0x58 0x1b 0x80    \....X..
    decimal
             92    8  132   17  128   88   27  128
    datetime (unknown)

    body (0)

#### RECORD 21 Bolus 2014-06-30T13:48:46 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 60,
 'programmed': 1.0,
 'type': 'square',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0xc8 0x02    ..(.(...
    decimal
              1    0   40    0   40    0  200    2
    datetime (2014-06-30T13:48:46)
    0000   0x6e 0xb0 0xad 0x1e 0x0e                   n....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 Bolus 2014-06-30T13:47:14 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3,
 'duration': 0,
 'programmed': 2.3,
 'type': 'normal',
 'unabsorbed': 5.0}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0xc8 0x00    ..\.\...
    decimal
              1    0   92    0   92    0  200    0
    datetime (2014-06-30T13:47:14)
    0000   0x4e 0xaf 0x8d 0x1e 0x0e                   N....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 23 BolusWizard 2014-06-30T14:44:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 0.8,
 'carb_input': 10,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.8,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-30T14:44:49)
    0000   0x71 0xac 0x0e 0x7e 0x0e                   q..~.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x20 0x00 0x00 0x00 0x00 0x20 0x64          .... d
    decimal
             10   80    0  120   50   80    0    0
             32    0    0    0    0   32  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 4, 'amount': 0.1, 'curve': 128},
 {'age': 14, 'amount': 0.15, 'curve': 128},
 {'age': 24, 'amount': 0.2, 'curve': 128},
 {'age': 34, 'amount': 0.15, 'curve': 128},
 {'age': 44, 'amount': 0.15, 'curve': 128},
 {'age': 54, 'amount': 0.2, 'curve': 128},
 {'age': 64, 'amount': 2.3, 'curve': 128},
 {'age': 74, 'amount': 3.3, 'curve': 128},
 {'age': 84, 'amount': 2.2, 'curve': 128}]
```
    op hex (29)
    0000   0x5c 0x1d 0x04 0x04 0x80 0x06 0x0e 0x80    \.......
    0008   0x08 0x18 0x80 0x06 0x22 0x80 0x06 0x2c    ...."..,
    0010   0x80 0x08 0x36 0x80 0x5c 0x40 0x80 0x84    ..6.\@..
    0018   0x4a 0x80 0x58 0x54 0x80                   J.XT.
    decimal
             92   29    4    4  128    6   14  128
              8   24  128    6   34  128    6   44
            128    8   54  128   92   64  128  132
             74  128   88   84  128
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2014-06-30T14:44:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8,
 'duration': 0,
 'programmed': 0.8,
 'type': 'normal',
 'unabsorbed': 3.2}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x80 0x00    .. . ...
    decimal
              1    0   32    0   32    0  128    0
    datetime (2014-06-30T14:44:50)
    0000   0x72 0xac 0x4e 0x7e 0x0e                   r.N~.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 26 CalBGForPH 2014-06-30T15:31:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 204}
```
    op hex (2)
    0000   0x0a 0xcc                                  ..
    decimal
             10  204
    datetime (2014-06-30T15:31:03)
    0000   0x43 0x9f 0x2f 0x7e 0x0e                   C./~.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 Ian3F 2014-06-30T15:31:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2014-06-30T15:31:03)
    0000   0x43 0x9f 0x8f 0x7e 0x0e                   C..~.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 BolusWizard 2014-06-30T15:32:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 204,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 2.0,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 1.0}
```
    op hex (2)
    0000   0x5b 0xcc                                  [.
    decimal
             91  204
    datetime (2014-06-30T15:32:05)
    0000   0x45 0xa0 0x0f 0x1e 0x0e                   E....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x50 0x00    .P.x2PP.
    0008   0x00 0x00 0x00 0x28 0x00 0x28 0x64         ...(.(d
    decimal
              0   80    0  120   50   80   80    0
              0    0    0   40    0   40  100
    HOUR BITS: [1, 0, 1]
#### RECORD 29 UnabsorbedInsulinBolus unknown head[29], body[0] op[0x5c]
###### DECODED
```python
[{'age': 52, 'amount': 0.95, 'curve': 128},
 {'age': 62, 'amount': 0.15, 'curve': 128},
 {'age': 72, 'amount': 0.2, 'curve': 128},
 {'age': 82, 'amount': 0.15, 'curve': 128},
 {'age': 92, 'amount': 0.15, 'curve': 128},
 {'age': 102, 'amount': 0.2, 'curve': 128},
 {'age': 112, 'amount': 2.3, 'curve': 128},
 {'age': 122, 'amount': 3.3, 'curve': 128},
 {'age': 132, 'amount': 2.2, 'curve': 128}]
```
    op hex (29)
    0000   0x5c 0x1d 0x26 0x34 0x80 0x06 0x3e 0x80    \.&4..>.
    0008   0x08 0x48 0x80 0x06 0x52 0x80 0x06 0x5c    .H..R..\
    0010   0x80 0x08 0x66 0x80 0x5c 0x70 0x80 0x84    ..f.\p..
    0018   0x7a 0x80 0x58 0x84 0x80                   z.X..
    decimal
             92   29   38   52  128    6   62  128
              8   72  128    6   82  128    6   92
            128    8  102  128   92  112  128  132
            122  128   88  132  128
    datetime (unknown)

    body (0)

#### RECORD 30 Bolus 2014-06-30T15:32:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3,
 'duration': 0,
 'programmed': 1.3,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x28 0x00    ..4.4.(.
    decimal
              1    0   52    0   52    0   40    0
    datetime (2014-06-30T15:32:05)
    0000   0x45 0xa0 0x4f 0x1e 0x0e                   E.O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 31 CalBGForPH 2014-06-30T17:01:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2014-06-30T17:01:48)
    0000   0x70 0x81 0x31 0x1e 0x0e                   p.1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 BolusWizard 2014-06-30T17:01:50 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 171,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2014-06-30T17:01:50)
    0000   0x72 0x81 0x11 0x7e 0x0e                   r..~.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x38 0x00    .P.x2P8.
    0008   0x00 0x00 0x00 0x0c 0x00 0x2c 0x64         .....,d
    decimal
              0   80    0  120   50   80   56    0
              0    0    0   12    0   44  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[32], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 1.3, 'curve': 128},
 {'age': 141, 'amount': 0.95, 'curve': 128},
 {'age': 151, 'amount': 0.15, 'curve': 128},
 {'age': 161, 'amount': 0.2, 'curve': 128},
 {'age': 171, 'amount': 0.15, 'curve': 128},
 {'age': 181, 'amount': 0.15, 'curve': 128},
 {'age': 191, 'amount': 0.2, 'curve': 128},
 {'age': 201, 'amount': 2.3, 'curve': 128},
 {'age': 211, 'amount': 3.3, 'curve': 128},
 {'age': 221, 'amount': 2.2, 'curve': 128}]
```
    op hex (32)
    0000   0x5c 0x20 0x34 0x5b 0x80 0x26 0x8d 0x80    \ 4[.&..
    0008   0x06 0x97 0x80 0x08 0xa1 0x80 0x06 0xab    ........
    0010   0x80 0x06 0xb5 0x80 0x08 0xbf 0x80 0x5c    .......\
    0018   0xc9 0x80 0x84 0xd3 0x80 0x58 0xdd 0x80    .....X..
    decimal
             92   32   52   91  128   38  141  128
              6  151  128    8  161  128    6  171
            128    6  181  128    8  191  128   92
            201  128  132  211  128   88  221  128
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2014-06-30T17:01:50 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.1,
 'duration': 0,
 'programmed': 1.1,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x2c 0x00 0x2c 0x00 0x0c 0x00    ..,.,...
    decimal
              1    0   44    0   44    0   12    0
    datetime (2014-06-30T17:01:50)
    0000   0x72 0x81 0x51 0x7e 0x0e                   r.Q~.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 CalBGForPH 2014-06-30T18:48:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2014-06-30T18:48:18)
    0000   0x52 0xb0 0x32 0x1e 0x0e                   R.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 BolusWizard 2014-06-30T18:48:23 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 135,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 2.2,
 'carb_input': 20,
 'carb_ratio': 10.0,
 'correction_estimate': 0.7,
 'food_estimate': 1.6,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0x87                                  [.
    decimal
             91  135
    datetime (2014-06-30T18:48:23)
    0000   0x57 0xb0 0x12 0x7e 0x0e                   W..~.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x78 0x32 0x50 0x1c 0x00    .P.x2P..
    0008   0x40 0x00 0x00 0x04 0x00 0x58 0x64         @....Xd
    decimal
             20   80    0  120   50   80   28    0
             64    0    0    4    0   88  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[35], body[0] op[0x5c]
###### DECODED
```python
[{'age': 108, 'amount': 1.1, 'curve': 128},
 {'age': 198, 'amount': 1.3, 'curve': 128},
 {'age': 248, 'amount': 0.95, 'curve': 128},
 {'age': 2, 'amount': 0.15, 'curve': 144},
 {'age': 12, 'amount': 0.2, 'curve': 144},
 {'age': 22, 'amount': 0.15, 'curve': 144},
 {'age': 32, 'amount': 0.15, 'curve': 144},
 {'age': 42, 'amount': 0.2, 'curve': 144},
 {'age': 52, 'amount': 2.3, 'curve': 144},
 {'age': 62, 'amount': 3.3, 'curve': 144},
 {'age': 72, 'amount': 2.2, 'curve': 144}]
```
    op hex (35)
    0000   0x5c 0x23 0x2c 0x6c 0x80 0x34 0xc6 0x80    \#,l.4..
    0008   0x26 0xf8 0x80 0x06 0x02 0x90 0x08 0x0c    &.......
    0010   0x90 0x06 0x16 0x90 0x06 0x20 0x90 0x08    ..... ..
    0018   0x2a 0x90 0x5c 0x34 0x90 0x84 0x3e 0x90    *.\4..>.
    0020   0x58 0x48 0x90                             XH.
    decimal
             92   35   44  108  128   52  198  128
             38  248  128    6    2  144    8   12
            144    6   22  144    6   32  144    8
             42  144   92   52  144  132   62  144
             88   72  144
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2014-06-30T18:48:23 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2,
 'duration': 0,
 'programmed': 2.2,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0x04 0x00    ..X.X...
    decimal
              1    0   88    0   88    0    4    0
    datetime (2014-06-30T18:48:23)
    0000   0x57 0xb0 0x52 0x7e 0x0e                   W.R~.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 BolusWizard 2014-06-30T19:07:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 1.0,
 'carb_input': 12,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-30T19:07:03)
    0000   0x43 0x87 0x13 0x7e 0x0e                   C..~.
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x64         (....(d
    decimal
             12   80    0  110   50   80    0    0
             40    0    0    0    0   40  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 UnabsorbedInsulinBolus unknown head[38], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 2.2, 'curve': 128},
 {'age': 127, 'amount': 1.1, 'curve': 128},
 {'age': 217, 'amount': 1.3, 'curve': 128},
 {'age': 11, 'amount': 0.95, 'curve': 144},
 {'age': 21, 'amount': 0.15, 'curve': 144},
 {'age': 31, 'amount': 0.2, 'curve': 144},
 {'age': 41, 'amount': 0.15, 'curve': 144},
 {'age': 51, 'amount': 0.15, 'curve': 144},
 {'age': 61, 'amount': 0.2, 'curve': 144},
 {'age': 71, 'amount': 2.3, 'curve': 144},
 {'age': 81, 'amount': 3.3, 'curve': 144},
 {'age': 91, 'amount': 2.2, 'curve': 144}]
```
    op hex (38)
    0000   0x5c 0x26 0x58 0x1b 0x80 0x2c 0x7f 0x80    \&X..,..
    0008   0x34 0xd9 0x80 0x26 0x0b 0x90 0x06 0x15    4..&....
    0010   0x90 0x08 0x1f 0x90 0x06 0x29 0x90 0x06    .....)..
    0018   0x33 0x90 0x08 0x3d 0x90 0x5c 0x47 0x90    3..=.\G.
    0020   0x84 0x51 0x90 0x58 0x5b 0x90              .Q.X[.
    decimal
             92   38   88   27  128   44  127  128
             52  217  128   38   11  144    6   21
            144    8   31  144    6   41  144    6
             51  144    8   61  144   92   71  144
            132   81  144   88   91  144
    datetime (unknown)

    body (0)

#### RECORD 41 Bolus 2014-06-30T19:07:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0,
 'duration': 0,
 'programmed': 1.0,
 'type': 'normal',
 'unabsorbed': 1.9}
```
    op hex (8)
    0000   0x01 0x00 0x28 0x00 0x28 0x00 0x4c 0x00    ..(.(.L.
    decimal
              1    0   40    0   40    0   76    0
    datetime (2014-06-30T19:07:03)
    0000   0x43 0x87 0x53 0x7e 0x0e                   C.S~.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 42 BolusWizard 2014-06-30T19:20:49 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 6.3,
 'carb_input': 70,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 6.3,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-30T19:20:49)
    0000   0x71 0x94 0x13 0x7e 0x0e                   q..~.
    body (15)
    hex
    0000   0x46 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    FP.n2P..
    0008   0xfc 0x00 0x00 0x00 0x00 0xfc 0x64         ......d
    decimal
             70   80    0  110   50   80    0    0
            252    0    0    0    0  252  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 43 UnabsorbedInsulinBolus unknown head[41], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 1.0, 'curve': 128},
 {'age': 40, 'amount': 2.2, 'curve': 128},
 {'age': 140, 'amount': 1.1, 'curve': 128},
 {'age': 230, 'amount': 1.3, 'curve': 128},
 {'age': 24, 'amount': 0.95, 'curve': 144},
 {'age': 34, 'amount': 0.15, 'curve': 144},
 {'age': 44, 'amount': 0.2, 'curve': 144},
 {'age': 54, 'amount': 0.15, 'curve': 144},
 {'age': 64, 'amount': 0.15, 'curve': 144},
 {'age': 74, 'amount': 0.2, 'curve': 144},
 {'age': 84, 'amount': 2.3, 'curve': 144},
 {'age': 94, 'amount': 3.3, 'curve': 144},
 {'age': 104, 'amount': 2.2, 'curve': 144}]
```
    op hex (41)
    0000   0x5c 0x29 0x28 0x14 0x80 0x58 0x28 0x80    \)(..X(.
    0008   0x2c 0x8c 0x80 0x34 0xe6 0x80 0x26 0x18    ,..4..&.
    0010   0x90 0x06 0x22 0x90 0x08 0x2c 0x90 0x06    .."..,..
    0018   0x36 0x90 0x06 0x40 0x90 0x08 0x4a 0x90    6..@..J.
    0020   0x5c 0x54 0x90 0x84 0x5e 0x90 0x58 0x68    \T..^.Xh
    0028   0x90                                       .
    decimal
             92   41   40   20  128   88   40  128
             44  140  128   52  230  128   38   24
            144    6   34  144    8   44  144    6
             54  144    6   64  144    8   74  144
             92   84  144  132   94  144   88  104
            144
    datetime (unknown)

    body (0)

#### RECORD 44 Bolus 2014-06-30T19:20:49 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 6.3,
 'duration': 0,
 'programmed': 6.3,
 'type': 'normal',
 'unabsorbed': 2.5}
```
    op hex (8)
    0000   0x01 0x00 0xfc 0x00 0xfc 0x00 0x64 0x00    ......d.
    decimal
              1    0  252    0  252    0  100    0
    datetime (2014-06-30T19:20:49)
    0000   0x71 0x94 0x53 0x7e 0x0e                   q.S~.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 45 BolusWizard 2014-06-30T19:47:32 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 0.9,
 'carb_input': 10,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.9,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-30T19:47:32)
    0000   0x60 0xaf 0x13 0x7e 0x0e                   `..~.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x64         $....$d
    decimal
             10   80    0  110   50   80    0    0
             36    0    0    0    0   36  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[44], body[0] op[0x5c]
###### DECODED
```python
[{'age': 27, 'amount': 6.3, 'curve': 128},
 {'age': 47, 'amount': 1.0, 'curve': 128},
 {'age': 67, 'amount': 2.2, 'curve': 128},
 {'age': 167, 'amount': 1.1, 'curve': 128},
 {'age': 1, 'amount': 1.3, 'curve': 144},
 {'age': 51, 'amount': 0.95, 'curve': 144},
 {'age': 61, 'amount': 0.15, 'curve': 144},
 {'age': 71, 'amount': 0.2, 'curve': 144},
 {'age': 81, 'amount': 0.15, 'curve': 144},
 {'age': 91, 'amount': 0.15, 'curve': 144},
 {'age': 101, 'amount': 0.2, 'curve': 144},
 {'age': 111, 'amount': 2.3, 'curve': 144},
 {'age': 121, 'amount': 3.3, 'curve': 144},
 {'age': 131, 'amount': 2.2, 'curve': 144}]
```
    op hex (44)
    0000   0x5c 0x2c 0xfc 0x1b 0x80 0x28 0x2f 0x80    \,...(/.
    0008   0x58 0x43 0x80 0x2c 0xa7 0x80 0x34 0x01    XC.,..4.
    0010   0x90 0x26 0x33 0x90 0x06 0x3d 0x90 0x08    .&3..=..
    0018   0x47 0x90 0x06 0x51 0x90 0x06 0x5b 0x90    G..Q..[.
    0020   0x08 0x65 0x90 0x5c 0x6f 0x90 0x84 0x79    .e.\o..y
    0028   0x90 0x58 0x83 0x90                        .X..
    decimal
             92   44  252   27  128   40   47  128
             88   67  128   44  167  128   52    1
            144   38   51  144    6   61  144    8
             71  144    6   81  144    6   91  144
              8  101  144   92  111  144  132  121
            144   88  131  144
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2014-06-30T19:47:32 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9,
 'duration': 0,
 'programmed': 0.9,
 'type': 'normal',
 'unabsorbed': 0.5}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x01 0x14 0x00    ..$.$...
    decimal
              1    0   36    0   36    1   20    0
    datetime (2014-06-30T19:47:32)
    0000   0x60 0xaf 0x53 0x7e 0x0e                   `.S~.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 CalBGForPH 2014-06-30T20:24:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2014-06-30T20:24:01)
    0000   0x41 0x98 0x34 0x7e 0x0e                   A.4~.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 Ian3F 2014-06-30T20:24:01 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2014-06-30T20:24:01)
    0000   0x41 0x98 0x34 0x7e 0x0e                   A.4~.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 50 PumpSuspend 2014-06-30T20:25:08 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-30T20:25:08)
    0000   0x48 0x99 0x14 0x1e 0x0e                   H....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 51 BasalProfileStart 2014-06-30T22:32:39 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 81000000, 'rate': 0.65}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-06-30T22:32:39)
    0000   0x67 0xa0 0x16 0x1e 0x0e                   g....
    body (3)
    hex
    0000   0x2d 0x1a 0x00                             -..
    decimal
             45   26    0
    HOUR BITS: [1, 0, 1]
#### RECORD 52 PumpResume 2014-06-30T22:32:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-30T22:32:40)
    0000   0x68 0xa0 0x16 0x1e 0x0e                   h....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 53 PumpSuspend 2014-06-30T22:41:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-30T22:41:38)
    0000   0x66 0xa9 0x16 0x1e 0x0e                   f....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 54 BasalProfileStart 2014-06-30T22:48:08 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 81000000, 'rate': 0.65}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-06-30T22:48:08)
    0000   0x48 0xb0 0x16 0x1e 0x0e                   H....
    body (3)
    hex
    0000   0x2d 0x1a 0x00                             -..
    decimal
             45   26    0
    HOUR BITS: [1, 0, 1]
#### RECORD 55 PumpResume 2014-06-30T22:48:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-30T22:48:08)
    0000   0x48 0xb0 0x16 0x1e 0x0e                   H....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 56 TempBasal 2014-06-30T22:48:22 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.25}
```
    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2014-06-30T22:48:22)
    0000   0x56 0xb0 0x16 0x1e 0x0e                   V....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 0, 1]
#### RECORD 57 TempBasalDuration 2014-06-30T22:48:22 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 480}
```
    op hex (2)
    0000   0x16 0x10                                  ..
    decimal
             22   16
    datetime (2014-06-30T22:48:22)
    0000   0x56 0xb0 0x16 0x1e 0x0e                   V....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 58 CalBGForPH 2014-06-30T23:15:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 121}
```
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2014-06-30T23:15:23)
    0000   0x57 0x8f 0x37 0x7e 0x0e                   W.7~.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 59 Ian3F 2014-06-30T23:15:23 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2014-06-30T23:15:23)
    0000   0x57 0x8f 0x37 0x7e 0x0e                   W.7~.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
ERROR day is out of range for month (2014, 6, 31, 0, 0, 0) 0000   0x7e 0x0e                                  ~.
#### RECORD 60 MResultTotals (2014, 6, 31, 0, 0, 0) head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0xb8                   .....
    decimal
              7    0    0    4  184
    datetime ((2014, 6, 31, 0, 0, 0))
    0000   0x7e 0x0e                                  ~.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

ERROR day is out of range for month 0000   0x7e 0x0e                                  ~.
#### RECORD 61 Sara6E (2014, 6, 31, 0, 0, 0) head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime ((2014, 6, 31, 0, 0, 0))
    0000   0x7e 0x0e                                  ~.
    body (49)
    hex
    0000   0x05 0x00 0x84 0x49 0xcc 0x07 0x00 0x00    ...I....
    0008   0x04 0xb8 0x01 0x38 0x1a 0x03 0x80 0x4a    ...8...J
    0010   0x00 0xde 0x02 0x70 0x00 0x60 0x00 0xb0    ...p.`..
    0018   0x00 0x00 0x06 0x02 0x02 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x84    ........
    0028   0xab 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  132   73  204    7    0    0
              4  184    1   56   26    3  128   74
              0  222    2  112    0   96    0  176
              0    0    6    2    2    0    0    0
              0    0    0    0    0    0    0  132
            171    0    0    0    0    0    0    0
              0

#### RECORD 62 CalBGForPH 2014-07-01T01:28:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 161}
```
    op hex (2)
    0000   0x0a 0xa1                                  ..
    decimal
             10  161
    datetime (2014-07-01T01:28:27)
    0000   0x5b 0xdc 0x21 0x01 0x0e                   [.!..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 63 BolusWizard 2014-07-01T01:28:30 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 161,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 2.0,
 'food_estimate': 0.0,
 'sensitivity': 30,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xa1                                  [.
    decimal
             91  161
    datetime (2014-07-01T01:28:30)
    0000   0x5e 0xdc 0x01 0x01 0x0e                   ^....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x1e 0x50 0x50 0x00    .P.n.PP.
    0008   0x00 0x00 0x00 0x00 0x00 0x50 0x64         .....Pd
    decimal
              0   80    0  110   30   80   80    0
              0    0    0    0    0   80  100
    HOUR BITS: [1, 1, 0]
#### RECORD 64 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 92, 'amount': 0.9, 'curve': 144},
 {'age': 112, 'amount': 6.3, 'curve': 144},
 {'age': 132, 'amount': 1.0, 'curve': 144},
 {'age': 152, 'amount': 2.2, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x24 0x5c 0x90 0xfc 0x70 0x90    \.$\..p.
    0008   0x28 0x84 0x90 0x58 0x98 0x90              (..X..
    decimal
             92   14   36   92  144  252  112  144
             40  132  144   88  152  144
    datetime (unknown)

    body (0)

`end brandon-ReadHistoryData-page-1.data: 65 records`
```
+ for x in 'brandon-ReadHistoryData-page-*.data'
+ echo brandon-ReadHistoryData-page-2.data
brandon-ReadHistoryData-page-2.data
+ python list_history.py --larger brandon-ReadHistoryData-page-2.data
```
## START brandon-ReadHistoryData-page-2.data
#### STOPPING DOUBLE NULLS @ 991, found 31 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xc4 0x95                                  ..
##### DEBUG DECIMAL
            196  149
#### RECORD 0 Bolus 2014-06-28T21:40:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2,
 'duration': 0,
 'programmed': 2.2,
 'type': 'normal',
 'unabsorbed': 4.9}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x00 0xc4 0x00    ..X.X...
    decimal
              1    0   88    0   88    0  196    0
    datetime (2014-06-28T21:40:34)
    0000   0x62 0xa8 0x55 0x7c 0x0e                   b.U|.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 1 BolusWizard 2014-06-28T21:45:59 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.2,
 'carb_input': 25,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 2.2,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-28T21:45:59)
    0000   0x7b 0xad 0x15 0x7c 0x0e                   {..|.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x64         X....Xd
    decimal
             25   80    0  110   50   80    0    0
             88    0    0    0    0   88  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 5, 'amount': 2.2, 'curve': 128},
 {'age': 35, 'amount': 5.0, 'curve': 128},
 {'age': 45, 'amount': 1.0, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x58 0x05 0x80 0xc8 0x23 0x80    \.X...#.
    0008   0x28 0x2d 0x80                             (-.
    decimal
             92   11   88    5  128  200   35  128
             40   45  128
    datetime (unknown)

    body (0)

#### RECORD 3 Bolus 2014-06-28T21:45:59 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.2,
 'duration': 0,
 'programmed': 2.2,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x58 0x00 0x58 0x01 0x0c 0x00    ..X.X...
    decimal
              1    0   88    0   88    1   12    0
    datetime (2014-06-28T21:45:59)
    0000   0x7b 0xad 0x55 0x7c 0x0e                   {.U|.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 4 BolusWizard 2014-06-28T22:00:51 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 1.8,
 'carb_input': 20,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-28T22:00:51)
    0000   0x73 0x80 0x16 0x7c 0x0e                   s..|.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 20, 'amount': 4.4, 'curve': 128},
 {'age': 50, 'amount': 5.0, 'curve': 128},
 {'age': 60, 'amount': 1.0, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0xb0 0x14 0x80 0xc8 0x32 0x80    \.....2.
    0008   0x28 0x3c 0x80                             (<.
    decimal
             92   11  176   20  128  200   50  128
             40   60  128
    datetime (unknown)

    body (0)

#### RECORD 6 Bolus 2014-06-28T22:00:51 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 0,
 'programmed': 1.8,
 'type': 'normal',
 'unabsorbed': 1.1}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x01 0x2c 0x00    ..H.H.,.
    decimal
              1    0   72    0   72    1   44    0
    datetime (2014-06-28T22:00:51)
    0000   0x73 0x80 0x56 0x7c 0x0e                   s.V|.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 BasalProfileStart 2014-06-28T22:30:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 81000000, 'rate': 0.65}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-06-28T22:30:00)
    0000   0x40 0x9e 0x16 0x1c 0x0e                   @....
    body (3)
    hex
    0000   0x2d 0x1a 0x00                             -..
    decimal
             45   26    0
    HOUR BITS: [1, 0, 0]
#### RECORD 8 CalBGForPH 2014-06-28T23:06:49 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2014-06-28T23:06:49)
    0000   0x71 0x86 0x37 0x7c 0x0e                   q.7|.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 9 Ian3F 2014-06-28T23:06:49 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-06-28T23:06:49)
    0000   0x71 0x86 0xf7 0x7c 0x0e                   q..|.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 BolusWizard 2014-06-28T23:11:47 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 167,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 1.9,
 'food_estimate': 0.0,
 'sensitivity': 35,
 'unabsorbed_insulin_total': 1.4}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2014-06-28T23:11:47)
    0000   0x6f 0x8b 0x17 0x1c 0x0e                   o....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x23 0x50 0x4c 0x00    .P.n#PL.
    0008   0x00 0x00 0x00 0x38 0x00 0x14 0x64         ...8..d
    decimal
              0   80    0  110   35   80   76    0
              0    0    0   56    0   20  100
    HOUR BITS: [1, 0, 0]
#### RECORD 11 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 1.8, 'curve': 128},
 {'age': 91, 'amount': 4.4, 'curve': 128},
 {'age': 121, 'amount': 5.0, 'curve': 128},
 {'age': 131, 'amount': 1.0, 'curve': 128}]
```
    op hex (14)
    0000   0x5c 0x0e 0x48 0x47 0x80 0xb0 0x5b 0x80    \.HG..[.
    0008   0xc8 0x79 0x80 0x28 0x83 0x80              .y.(..
    decimal
             92   14   72   71  128  176   91  128
            200  121  128   40  131  128
    datetime (unknown)

    body (0)

#### RECORD 12 Bolus 2014-06-28T23:11:47 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5,
 'duration': 0,
 'programmed': 0.5,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x14 0x00 0x14 0x00 0x38 0x00    ......8.
    decimal
              1    0   20    0   20    0   56    0
    datetime (2014-06-28T23:11:47)
    0000   0x6f 0x8b 0x57 0x1c 0x0e                   o.W..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 13 BasalProfileStart 2014-06-29T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-06-29T00:00:00)
    0000   0x40 0x80 0x00 0x1d 0x0e                   @....
    body (3)
    hex
    0000   0x00 0x19 0x00                             ...
    decimal
              0   25    0
    HOUR BITS: [1, 0, 0]
#### RECORD 14 MResultTotals 2014-06-29T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x9c                   .....
    decimal
              7    0    0    4  156
    datetime (2014-06-29T00:00:00)
    0000   0x7c 0x0e                                  |.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 15 Sara6E 2014-06-29T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-29T00:00:00)
    0000   0x7c 0x0e                                  |.
    body (49)
    hex
    0000   0x05 0x00 0x92 0x31 0xef 0x0d 0x00 0x00    ...1....
    0008   0x04 0x9c 0x01 0x44 0x1b 0x03 0x58 0x49    ...D..XI
    0010   0x00 0x89 0x01 0xe8 0x01 0x70 0x00 0x00    .....p..
    0018   0x00 0x00 0x05 0x05 0x00 0x00 0x04 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x50    .......P
    0028   0x1c 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  146   49  239   13    0    0
              4  156    1   68   27    3   88   73
              0  137    1  232    1  112    0    0
              0    0    5    5    0    0    4    0
              0    0    0    0    0    0    0   80
             28    0    0    0    0    0    0    0
              0

#### RECORD 16 CalBGForPH 2014-06-29T01:05:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 206}
```
    op hex (2)
    0000   0x0a 0xce                                  ..
    decimal
             10  206
    datetime (2014-06-29T01:05:03)
    0000   0x43 0x85 0x21 0x7d 0x0e                   C.!}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 Ian3F 2014-06-29T01:05:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2014-06-29T01:05:03)
    0000   0x43 0x85 0xc1 0x7d 0x0e                   C..}.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 BolusWizard 2014-06-29T01:05:11 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 206,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 3.4,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': -2.9,
 'food_estimate': 0.0,
 'sensitivity': 30,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0xce                                  [.
    decimal
             91  206
    datetime (2014-06-29T01:05:11)
    0000   0x4b 0x85 0x01 0x1d 0x0e                   K....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x1e 0x50 0x8c 0x00    .P.n.P..
    0008   0x00 0x00 0x00 0x04 0x00 0x88 0x64         ......d
    decimal
              0   80    0  110   30   80  140    0
              0    0    0    4    0  136  100
    HOUR BITS: [1, 0, 0]
#### RECORD 19 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 115, 'amount': 0.5, 'curve': 128},
 {'age': 185, 'amount': 1.8, 'curve': 128},
 {'age': 205, 'amount': 4.4, 'curve': 128},
 {'age': 235, 'amount': 5.0, 'curve': 128},
 {'age': 245, 'amount': 1.0, 'curve': 128}]
```
    op hex (17)
    0000   0x5c 0x11 0x14 0x73 0x80 0x48 0xb9 0x80    \..s.H..
    0008   0xb0 0xcd 0x80 0xc8 0xeb 0x80 0x28 0xf5    ......(.
    0010   0x80                                       .
    decimal
             92   17   20  115  128   72  185  128
            176  205  128  200  235  128   40  245
            128
    datetime (unknown)

    body (0)

#### RECORD 20 Bolus 2014-06-29T01:05:11 head[8], body[0] op[0x01]
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
    datetime (2014-06-29T01:05:11)
    0000   0x4b 0x85 0x41 0x1d 0x0e                   K.A..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 21 CalBGForPH 2014-06-29T03:44:01 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2014-06-29T03:44:01)
    0000   0x41 0xac 0x23 0x7d 0x0e                   A.#}.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 Ian3F 2014-06-29T03:44:01 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2014-06-29T03:44:01)
    0000   0x41 0xac 0x43 0x7d 0x0e                   A.C}.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 BolusWizard 2014-06-29T03:44:27 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 202,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 3.4,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': -3.0,
 'food_estimate': 0.0,
 'sensitivity': 30,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xca                                  [.
    decimal
             91  202
    datetime (2014-06-29T03:44:27)
    0000   0x5b 0xac 0x03 0x1d 0x0e                   [....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x1e 0x50 0x88 0x00    .P.n.P..
    0008   0x00 0x00 0x00 0x00 0x00 0x88 0x64         ......d
    decimal
              0   80    0  110   30   80  136    0
              0    0    0    0    0  136  100
    HOUR BITS: [1, 0, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 164, 'amount': 2.5, 'curve': 128},
 {'age': 18, 'amount': 0.5, 'curve': 144},
 {'age': 88, 'amount': 1.8, 'curve': 144},
 {'age': 108, 'amount': 4.4, 'curve': 144},
 {'age': 138, 'amount': 5.0, 'curve': 144},
 {'age': 148, 'amount': 1.0, 'curve': 144}]
```
    op hex (20)
    0000   0x5c 0x14 0x64 0xa4 0x80 0x14 0x12 0x90    \.d.....
    0008   0x48 0x58 0x90 0xb0 0x6c 0x90 0xc8 0x8a    HX..l...
    0010   0x90 0x28 0x94 0x90                        .(..
    decimal
             92   20  100  164  128   20   18  144
             72   88  144  176  108  144  200  138
            144   40  148  144
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2014-06-29T03:44:27 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3,
 'duration': 0,
 'programmed': 2.3,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x00 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    0    0
    datetime (2014-06-29T03:44:27)
    0000   0x5b 0xac 0x43 0x1d 0x0e                   [.C..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 26 BasalProfileStart 2014-06-29T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-06-29T04:00:00)
    0000   0x40 0x80 0x04 0x1d 0x0e                   @....
    body (3)
    hex
    0000   0x08 0x19 0x00                             ...
    decimal
              8   25    0
    HOUR BITS: [1, 0, 0]
#### RECORD 27 BasalProfileStart 2014-06-29T06:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-06-29T06:00:00)
    0000   0x40 0x80 0x06 0x1d 0x0e                   @....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 0, 0]
#### RECORD 28 PumpSuspend 2014-06-29T10:26:28 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-29T10:26:28)
    0000   0x5c 0x9a 0x0a 0x1d 0x0e                   \....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 CalBGForPH 2014-06-29T11:27:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2014-06-29T11:27:33)
    0000   0x61 0x9b 0x2b 0x7d 0x0e                   a.+}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 Ian3F 2014-06-29T11:27:33 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-06-29T11:27:33)
    0000   0x61 0x9b 0x8b 0x7d 0x0e                   a..}.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 CalBGForPH 2014-06-29T14:26:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 140}
```
    op hex (2)
    0000   0x0a 0x8c                                  ..
    decimal
             10  140
    datetime (2014-06-29T14:26:17)
    0000   0x51 0x9a 0x2e 0x7d 0x0e                   Q..}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 Ian3F 2014-06-29T14:26:17 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-06-29T14:26:17)
    0000   0x51 0x9a 0x8e 0x7d 0x0e                   Q..}.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 BasalProfileStart 2014-06-29T15:32:03 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-29T15:32:03)
    0000   0x43 0xa0 0x0f 0x1d 0x0e                   C....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 1]
#### RECORD 34 PumpResume 2014-06-29T15:32:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-29T15:32:03)
    0000   0x43 0xa0 0x0f 0x1d 0x0e                   C....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 35 CalBGForPH 2014-06-29T15:32:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 182}
```
    op hex (2)
    0000   0x0a 0xb6                                  ..
    decimal
             10  182
    datetime (2014-06-29T15:32:13)
    0000   0x4d 0xa0 0x2f 0x1d 0x0e                   M./..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 36 BolusWizard 2014-06-29T15:32:18 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 182,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 1.6,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xb6                                  [.
    decimal
             91  182
    datetime (2014-06-29T15:32:18)
    0000   0x52 0xa0 0x0f 0x1d 0x0e                   R....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x40 0x00    .P.x2P@.
    0008   0x00 0x00 0x00 0x00 0x00 0x40 0x64         .....@d
    decimal
              0   80    0  120   50   80   64    0
              0    0    0    0    0   64  100
    HOUR BITS: [1, 0, 1]
#### RECORD 37 Bolus 2014-06-29T15:32:18 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7,
 'duration': 0,
 'programmed': 0.7,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x1c 0x00 0x1c 0x00 0x00 0x00    ........
    decimal
              1    0   28    0   28    0    0    0
    datetime (2014-06-29T15:32:18)
    0000   0x52 0xa0 0x4f 0x1d 0x0e                   R.O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 38 Bolus 2014-06-29T15:55:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.4,
 'duration': 0,
 'programmed': 0.4,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0x10 0x00 0x10 0x00 0x18 0x00    ........
    decimal
              1    0   16    0   16    0   24    0
    datetime (2014-06-29T15:55:19)
    0000   0x53 0xb7 0x4f 0x1d 0x0e                   S.O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 39 PumpSuspend 2014-06-29T15:56:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-29T15:56:29)
    0000   0x5d 0xb8 0x0f 0x1d 0x0e                   ]....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 40 CalBGForPH 2014-06-29T15:58:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2014-06-29T15:58:13)
    0000   0x4d 0xba 0x2f 0x7d 0x0e                   M./}.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2014-06-29T15:58:13 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2014-06-29T15:58:13)
    0000   0x4d 0xba 0x8f 0x7d 0x0e                   M..}.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 BasalProfileStart 2014-06-29T16:32:29 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-29T16:32:29)
    0000   0x5d 0xa0 0x10 0x1d 0x0e                   ]....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 1]
#### RECORD 43 PumpResume 2014-06-29T16:32:29 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-29T16:32:29)
    0000   0x5d 0xa0 0x10 0x1d 0x0e                   ]....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 44 BasalProfileStart 2014-06-29T16:33:03 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-29T16:33:03)
    0000   0x43 0xa1 0x10 0x1d 0x0e                   C....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 1]
#### RECORD 45 Prime 2014-06-29T16:32:53 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2014-06-29T16:32:53)
    0000   0x75 0xa0 0x10 0x1d 0x0e                   u....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 46 CalBGForPH 2014-06-29T18:26:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 170}
```
    op hex (2)
    0000   0x0a 0xaa                                  ..
    decimal
             10  170
    datetime (2014-06-29T18:26:03)
    0000   0x43 0x9a 0x32 0x7d 0x0e                   C.2}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 47 Ian3F 2014-06-29T18:26:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-06-29T18:26:03)
    0000   0x43 0x9a 0x52 0x7d 0x0e                   C.R}.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 BolusWizard 2014-06-29T18:26:08 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 170,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xaa                                  [.
    decimal
             91  170
    datetime (2014-06-29T18:26:08)
    0000   0x48 0x9a 0x12 0x1d 0x0e                   H....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x38 0x00    .P.x2P8.
    0008   0x00 0x00 0x00 0x00 0x00 0x38 0x64         .....8d
    decimal
              0   80    0  120   50   80   56    0
              0    0    0    0    0   56  100
    HOUR BITS: [1, 0, 0]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 156, 'amount': 0.4, 'curve': 128},
 {'age': 176, 'amount': 0.7, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x10 0x9c 0x80 0x1c 0xb0 0x80    \.......
    decimal
             92    8   16  156  128   28  176  128
    datetime (unknown)

    body (0)

#### RECORD 50 CalBGForPH 2014-06-29T18:26:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 175}
```
    op hex (2)
    0000   0x0a 0xaf                                  ..
    decimal
             10  175
    datetime (2014-06-29T18:26:47)
    0000   0x6f 0x9a 0x32 0x7d 0x0e                   o.2}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 Ian3F 2014-06-29T18:26:47 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-06-29T18:26:47)
    0000   0x6f 0x9a 0xf2 0x7d 0x0e                   o..}.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 Bolus 2014-06-29T18:26:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4,
 'duration': 0,
 'programmed': 1.4,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2014-06-29T18:26:09)
    0000   0x49 0x9a 0x52 0x1d 0x0e                   I.R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 53 BolusWizard 2014-06-29T19:06:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 0.9,
 'carb_input': 10,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 0.9,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-29T19:06:01)
    0000   0x41 0x86 0x13 0x7d 0x0e                   A..}.
    body (15)
    hex
    0000   0x0a 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x24 0x00 0x00 0x00 0x00 0x24 0x64         $....$d
    decimal
             10   80    0  110   50   80    0    0
             36    0    0    0    0   36  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 46, 'amount': 1.4, 'curve': 128},
 {'age': 196, 'amount': 0.4, 'curve': 128},
 {'age': 216, 'amount': 0.7, 'curve': 128}]
```
    op hex (11)
    0000   0x5c 0x0b 0x38 0x2e 0x80 0x10 0xc4 0x80    \.8.....
    0008   0x1c 0xd8 0x80                             ...
    decimal
             92   11   56   46  128   16  196  128
             28  216  128
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2014-06-29T19:06:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9,
 'duration': 0,
 'programmed': 0.9,
 'type': 'normal',
 'unabsorbed': 0.9}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x24 0x00    ..$.$.$.
    decimal
              1    0   36    0   36    0   36    0
    datetime (2014-06-29T19:06:01)
    0000   0x41 0x86 0x53 0x7d 0x0e                   A.S}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 56 BolusWizard 2014-06-29T19:18:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.7,
 'carb_input': 30,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 2.7,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-29T19:18:34)
    0000   0x62 0x92 0x13 0x7d 0x0e                   b..}.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x64         l....ld
    decimal
             30   80    0  110   50   80    0    0
            108    0    0    0    0  108  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 57 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 0.9, 'curve': 128},
 {'age': 58, 'amount': 1.4, 'curve': 128},
 {'age': 208, 'amount': 0.4, 'curve': 128},
 {'age': 228, 'amount': 0.7, 'curve': 128}]
```
    op hex (14)
    0000   0x5c 0x0e 0x24 0x12 0x80 0x38 0x3a 0x80    \.$..8:.
    0008   0x10 0xd0 0x80 0x1c 0xe4 0x80              ......
    decimal
             92   14   36   18  128   56   58  128
             16  208  128   28  228  128
    datetime (unknown)

    body (0)

#### RECORD 58 Bolus 2014-06-29T19:18:34 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7,
 'duration': 0,
 'programmed': 2.7,
 'type': 'normal',
 'unabsorbed': 1.6}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x40 0x00    ..l.l.@.
    decimal
              1    0  108    0  108    0   64    0
    datetime (2014-06-29T19:18:34)
    0000   0x62 0x92 0x53 0x7d 0x0e                   b.S}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 59 BolusWizard 2014-06-29T19:27:05 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 4.5,
 'carb_input': 50,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 4.5,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-29T19:27:05)
    0000   0x45 0x9b 0x13 0x7d 0x0e                   E..}.
    body (15)
    hex
    0000   0x32 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    2P.n2P..
    0008   0xb4 0x00 0x00 0x00 0x00 0xb4 0x64         ......d
    decimal
             50   80    0  110   50   80    0    0
            180    0    0    0    0  180  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 UnabsorbedInsulinBolus unknown head[20], body[0] op[0x5c]
###### DECODED
```python
[{'age': 7, 'amount': 0.6, 'curve': 128},
 {'age': 17, 'amount': 2.1, 'curve': 128},
 {'age': 27, 'amount': 0.9, 'curve': 128},
 {'age': 67, 'amount': 1.4, 'curve': 128},
 {'age': 217, 'amount': 0.4, 'curve': 128},
 {'age': 237, 'amount': 0.7, 'curve': 128}]
```
    op hex (20)
    0000   0x5c 0x14 0x18 0x07 0x80 0x54 0x11 0x80    \....T..
    0008   0x24 0x1b 0x80 0x38 0x43 0x80 0x10 0xd9    $..8C...
    0010   0x80 0x1c 0xed 0x80                        ....
    decimal
             92   20   24    7  128   84   17  128
             36   27  128   56   67  128   16  217
            128   28  237  128
    datetime (unknown)

    body (0)

#### RECORD 61 Bolus 2014-06-29T19:27:05 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.5,
 'duration': 0,
 'programmed': 4.5,
 'type': 'normal',
 'unabsorbed': 3.9}
```
    op hex (8)
    0000   0x01 0x00 0xb4 0x00 0xb4 0x00 0x9c 0x00    ........
    decimal
              1    0  180    0  180    0  156    0
    datetime (2014-06-29T19:27:05)
    0000   0x45 0x9b 0x53 0x7d 0x0e                   E.S}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 BolusWizard 2014-06-29T19:40:56 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 1.8,
 'carb_input': 20,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-29T19:40:56)
    0000   0x78 0xa8 0x13 0x7d 0x0e                   x..}.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 UnabsorbedInsulinBolus unknown head[23], body[0] op[0x5c]
###### DECODED
```python
[{'age': 10, 'amount': 0.15, 'curve': 128},
 {'age': 20, 'amount': 4.95, 'curve': 128},
 {'age': 30, 'amount': 2.1, 'curve': 128},
 {'age': 40, 'amount': 0.9, 'curve': 128},
 {'age': 80, 'amount': 1.4, 'curve': 128},
 {'age': 230, 'amount': 0.4, 'curve': 128},
 {'age': 250, 'amount': 0.7, 'curve': 128}]
```
    op hex (23)
    0000   0x5c 0x17 0x06 0x0a 0x80 0xc6 0x14 0x80    \.......
    0008   0x54 0x1e 0x80 0x24 0x28 0x80 0x38 0x50    T..$(.8P
    0010   0x80 0x10 0xe6 0x80 0x1c 0xfa 0x80         .......
    decimal
             92   23    6   10  128  198   20  128
             84   30  128   36   40  128   56   80
            128   16  230  128   28  250  128
    datetime (unknown)

    body (0)

#### RECORD 64 Bolus 2014-06-29T19:40:56 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 0,
 'programmed': 1.8,
 'type': 'normal',
 'unabsorbed': 1.0}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x01 0x28 0x00    ..H.H.(.
    decimal
              1    0   72    0   72    1   40    0
    datetime (2014-06-29T19:40:56)
    0000   0x78 0xa8 0x53 0x7d 0x0e                   x.S}.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 PumpSuspend 2014-06-29T21:05:23 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-29T21:05:23)
    0000   0x57 0x85 0x15 0x1d 0x0e                   W....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 66 CalBGForPH 2014-06-29T21:09:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 78}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2014-06-29T21:09:11)
    0000   0x4b 0x89 0x35 0x7d 0x0e                   K.5}.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 67 Ian3F 2014-06-29T21:09:11 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2014-06-29T21:09:11)
    0000   0x4b 0x89 0xd5 0x7d 0x0e                   K..}.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 BasalProfileStart 2014-06-29T21:28:41 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-29T21:28:41)
    0000   0x69 0x9c 0x15 0x1d 0x0e                   i....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 69 PumpResume 2014-06-29T21:28:41 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-29T21:28:41)
    0000   0x69 0x9c 0x15 0x1d 0x0e                   i....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 70 BasalProfileStart 2014-06-29T22:30:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 81000000, 'rate': 0.65}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-06-29T22:30:00)
    0000   0x40 0x9e 0x16 0x1d 0x0e                   @....
    body (3)
    hex
    0000   0x2d 0x1a 0x00                             -..
    decimal
             45   26    0
    HOUR BITS: [1, 0, 0]
#### RECORD 71 TempBasal 2014-06-29T22:41:22 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 1.25}
```
    op hex (2)
    0000   0x33 0x32                                  32
    decimal
             51   50
    datetime (2014-06-29T22:41:22)
    0000   0x56 0xa9 0x16 0x1d 0x0e                   V....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 0, 1]
#### RECORD 72 TempBasalDuration 2014-06-29T22:41:22 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 420}
```
    op hex (2)
    0000   0x16 0x0e                                  ..
    decimal
             22   14
    datetime (2014-06-29T22:41:22)
    0000   0x56 0xa9 0x16 0x1d 0x0e                   V....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 73 TempBasal 2014-06-29T23:48:29 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-06-29T23:48:29)
    0000   0x5d 0xb0 0x17 0x1d 0x0e                   ]....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 0, 1]
#### RECORD 74 TempBasalDuration 2014-06-29T23:48:29 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 0}
```
    op hex (2)
    0000   0x16 0x00                                  ..
    decimal
             22    0
    datetime (2014-06-29T23:48:29)
    0000   0x5d 0xb0 0x17 0x1d 0x0e                   ]....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 75 BasalProfileStart 2014-06-29T23:48:29 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 81000000, 'rate': 0.65}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-06-29T23:48:29)
    0000   0x5d 0xb0 0x17 0x1d 0x0e                   ]....
    body (3)
    hex
    0000   0x2d 0x1a 0x00                             -..
    decimal
             45   26    0
    HOUR BITS: [1, 0, 1]
#### RECORD 76 TempBasal 2014-06-29T23:48:43 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.0}
```
    op hex (2)
    0000   0x33 0x00                                  3.
    decimal
             51    0
    datetime (2014-06-29T23:48:43)
    0000   0x6b 0xb0 0x17 0x1d 0x0e                   k....
    body (1)
    hex
    0000   0x08                                       .
    decimal
              8
    HOUR BITS: [1, 0, 1]
#### RECORD 77 TempBasalDuration 2014-06-29T23:48:43 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 240}
```
    op hex (2)
    0000   0x16 0x08                                  ..
    decimal
             22    8
    datetime (2014-06-29T23:48:43)
    0000   0x6b 0xb0 0x17 0x1d 0x0e                   k....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 78 MResultTotals 2014-06-30T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x04 0x54                   ....T
    decimal
              7    0    0    4   84
    datetime (2014-06-30T00:00:00)
    0000   0x7d 0x0e                                  }.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end brandon-ReadHistoryData-page-2.data: 79 records`
```
+ for x in 'brandon-ReadHistoryData-page-*.data'
+ echo brandon-ReadHistoryData-page-3.data
brandon-ReadHistoryData-page-3.data
+ python list_history.py --larger brandon-ReadHistoryData-page-3.data
```
## START brandon-ReadHistoryData-page-3.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x44 0x44                                  DD
##### DEBUG DECIMAL
             68   68
#### RECORD 0 BasalProfileStart 2014-06-27T06:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-06-27T06:00:00)
    0000   0x40 0x80 0x06 0x1b 0x0e                   @....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 PumpSuspend 2014-06-27T08:40:38 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-27T08:40:38)
    0000   0x66 0xa8 0x08 0x1b 0x0e                   f....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 CalBGForPH 2014-06-27T09:19:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 71}
```
    op hex (2)
    0000   0x0a 0x47                                  .G
    decimal
             10   71
    datetime (2014-06-27T09:19:35)
    0000   0x63 0x93 0x29 0x7b 0x0e                   c.){.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 3 Ian3F 2014-06-27T09:19:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-06-27T09:19:35)
    0000   0x63 0x93 0xe9 0x7b 0x0e                   c..{.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 CalBGForPH 2014-06-27T13:03:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2014-06-27T13:03:03)
    0000   0x43 0x83 0x2d 0x7b 0x0e                   C.-{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 Ian3F 2014-06-27T13:03:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-06-27T13:03:03)
    0000   0x43 0x83 0x8d 0x7b 0x0e                   C..{.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 6 CalBGForPH 2014-06-27T17:25:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2014-06-27T17:25:05)
    0000   0x45 0x99 0x31 0x7b 0x0e                   E.1{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2014-06-27T17:25:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-27T17:25:05)
    0000   0x45 0x99 0xb1 0x7b 0x0e                   E..{.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 BasalProfileStart 2014-06-27T17:25:13 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-27T17:25:13)
    0000   0x4d 0x99 0x11 0x1b 0x0e                   M....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 9 PumpResume 2014-06-27T17:25:13 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-27T17:25:13)
    0000   0x4d 0x99 0x11 0x1b 0x0e                   M....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 BolusWizard 2014-06-27T17:25:19 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 157,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 1.1,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 1.1,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x9d                                  [.
    decimal
             91  157
    datetime (2014-06-27T17:25:19)
    0000   0x53 0x99 0x11 0x1b 0x0e                   S....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x2c 0x00    .P.x2P,.
    0008   0x00 0x00 0x00 0x00 0x00 0x2c 0x64         .....,d
    decimal
              0   80    0  120   50   80   44    0
              0    0    0    0    0   44  100
    HOUR BITS: [1, 0, 0]
#### RECORD 11 Bolus 2014-06-27T17:25:19 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8,
 'duration': 0,
 'programmed': 0.8,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x20 0x00 0x20 0x00 0x00 0x00    .. . ...
    decimal
              1    0   32    0   32    0    0    0
    datetime (2014-06-27T17:25:19)
    0000   0x53 0x99 0x51 0x1b 0x0e                   S.Q..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 12 CalBGForPH 2014-06-27T19:11:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2014-06-27T19:11:35)
    0000   0x63 0x8b 0x33 0x7b 0x0e                   c.3{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 13 Ian3F 2014-06-27T19:11:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-27T19:11:35)
    0000   0x63 0x8b 0x53 0x7b 0x0e                   c.S{.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 14 BolusWizard 2014-06-27T19:17:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 154,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.1}
```
    op hex (2)
    0000   0x5b 0x9a                                  [.
    decimal
             91  154
    datetime (2014-06-27T19:17:42)
    0000   0x6a 0x91 0x13 0x7b 0x0e                   j..{.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x32 0x50 0x28 0x00    .P.n2P(.
    0008   0x00 0x00 0x00 0x04 0x00 0x24 0x64         .....$d
    decimal
              0   80    0  110   50   80   40    0
              0    0    0    4    0   36  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 15 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 117, 'amount': 0.8, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x20 0x75 0x80                   \. u.
    decimal
             92    5   32  117  128
    datetime (unknown)

    body (0)

#### RECORD 16 Bolus 2014-06-27T19:17:42 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9,
 'duration': 0,
 'programmed': 0.9,
 'type': 'normal',
 'unabsorbed': 0.1}
```
    op hex (8)
    0000   0x01 0x00 0x24 0x00 0x24 0x00 0x04 0x00    ..$.$...
    decimal
              1    0   36    0   36    0    4    0
    datetime (2014-06-27T19:17:42)
    0000   0x6a 0x91 0x53 0x7b 0x0e                   j.S{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 BolusWizard 2014-06-27T21:54:04 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 1.8,
 'carb_input': 20,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.8,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-27T21:54:04)
    0000   0x44 0xb6 0x15 0x7b 0x0e                   D..{.
    body (15)
    hex
    0000   0x14 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x48 0x00 0x00 0x00 0x00 0x48 0x64         H....Hd
    decimal
             20   80    0  110   50   80    0    0
             72    0    0    0    0   72  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 164, 'amount': 0.9, 'curve': 128},
 {'age': 18, 'amount': 0.8, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x24 0xa4 0x80 0x20 0x12 0x90    \.$.. ..
    decimal
             92    8   36  164  128   32   18  144
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2014-06-27T21:54:04 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8,
 'duration': 0,
 'programmed': 1.8,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x48 0x00 0x48 0x00 0x00 0x00    ..H.H...
    decimal
              1    0   72    0   72    0    0    0
    datetime (2014-06-27T21:54:04)
    0000   0x44 0xb6 0x55 0x7b 0x0e                   D.U{.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 20 BolusWizard 2014-06-27T22:24:36 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 1.3,
 'carb_input': 15,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.3,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-27T22:24:36)
    0000   0x64 0x98 0x16 0x7b 0x0e                   d..{.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x34 0x00 0x00 0x00 0x00 0x34 0x64         4....4d
    decimal
             15   80    0  110   50   80    0    0
             52    0    0    0    0   52  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 1.8, 'curve': 128},
 {'age': 194, 'amount': 0.9, 'curve': 128},
 {'age': 48, 'amount': 0.8, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x48 0x22 0x80 0x24 0xc2 0x80    \.H".$..
    0008   0x20 0x30 0x90                              0.
    decimal
             92   11   72   34  128   36  194  128
             32   48  144
    datetime (unknown)

    body (0)

#### RECORD 22 Bolus 2014-06-27T22:24:36 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3,
 'duration': 0,
 'programmed': 1.3,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x38 0x00    ..4.4.8.
    decimal
              1    0   52    0   52    0   56    0
    datetime (2014-06-27T22:24:36)
    0000   0x64 0x98 0x56 0x7b 0x0e                   d.V{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 23 BasalProfileStart 2014-06-27T22:30:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 81000000, 'rate': 0.65}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-06-27T22:30:00)
    0000   0x40 0x9e 0x16 0x1b 0x0e                   @....
    body (3)
    hex
    0000   0x2d 0x1a 0x00                             -..
    decimal
             45   26    0
    HOUR BITS: [1, 0, 0]
#### RECORD 24 BolusWizard 2014-06-27T22:42:40 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 3.1,
 'carb_input': 35,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 3.1,
 'sensitivity': 35,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-27T22:42:40)
    0000   0x68 0xaa 0x16 0x7b 0x0e                   h..{.
    body (15)
    hex
    0000   0x23 0x50 0x00 0x6e 0x23 0x50 0x00 0x00    #P.n#P..
    0008   0x7c 0x00 0x00 0x00 0x00 0x7c 0x64         |....|d
    decimal
             35   80    0  110   35   80    0    0
            124    0    0    0    0  124  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 25 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 22, 'amount': 1.3, 'curve': 128},
 {'age': 52, 'amount': 1.8, 'curve': 128},
 {'age': 212, 'amount': 0.9, 'curve': 128},
 {'age': 66, 'amount': 0.8, 'curve': 144}]
```
    op hex (14)
    0000   0x5c 0x0e 0x34 0x16 0x80 0x48 0x34 0x80    \.4..H4.
    0008   0x24 0xd4 0x80 0x20 0x42 0x90              $.. B.
    decimal
             92   14   52   22  128   72   52  128
             36  212  128   32   66  144
    datetime (unknown)

    body (0)

#### RECORD 26 Bolus 2014-06-27T22:42:40 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1,
 'duration': 0,
 'programmed': 3.1,
 'type': 'normal',
 'unabsorbed': 2.2}
```
    op hex (8)
    0000   0x01 0x00 0x7c 0x00 0x7c 0x00 0x58 0x00    ..|.|.X.
    decimal
              1    0  124    0  124    0   88    0
    datetime (2014-06-27T22:42:40)
    0000   0x68 0xaa 0x56 0x7b 0x0e                   h.V{.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 27 BolusWizard 2014-06-27T23:16:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.7,
 'carb_input': 30,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 2.7,
 'sensitivity': 35,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-27T23:16:09)
    0000   0x49 0x90 0x17 0x7b 0x0e                   I..{.
    body (15)
    hex
    0000   0x1e 0x50 0x00 0x6e 0x23 0x50 0x00 0x00    .P.n#P..
    0008   0x6c 0x00 0x00 0x00 0x00 0x6c 0x64         l....ld
    decimal
             30   80    0  110   35   80    0    0
            108    0    0    0    0  108  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 36, 'amount': 3.1, 'curve': 128},
 {'age': 56, 'amount': 1.3, 'curve': 128},
 {'age': 86, 'amount': 1.8, 'curve': 128},
 {'age': 246, 'amount': 0.9, 'curve': 128},
 {'age': 100, 'amount': 0.8, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x7c 0x24 0x80 0x34 0x38 0x80    \.|$.48.
    0008   0x48 0x56 0x80 0x24 0xf6 0x80 0x20 0x64    HV.$.. d
    0010   0x90                                       .
    decimal
             92   17  124   36  128   52   56  128
             72   86  128   36  246  128   32  100
            144
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2014-06-27T23:16:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7,
 'duration': 0,
 'programmed': 2.7,
 'type': 'normal',
 'unabsorbed': 3.4}
```
    op hex (8)
    0000   0x01 0x00 0x6c 0x00 0x6c 0x00 0x88 0x00    ..l.l...
    decimal
              1    0  108    0  108    0  136    0
    datetime (2014-06-27T23:16:09)
    0000   0x49 0x90 0x57 0x7b 0x0e                   I.W{.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 BasalProfileStart 2014-06-28T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-06-28T00:00:00)
    0000   0x40 0x80 0x00 0x1c 0x0e                   @....
    body (3)
    hex
    0000   0x00 0x19 0x00                             ...
    decimal
              0   25    0
    HOUR BITS: [1, 0, 0]
#### RECORD 31 MResultTotals 2014-06-28T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x03 0x87                   .....
    decimal
              7    0    0    3  135
    datetime (2014-06-28T00:00:00)
    0000   0x7b 0x0e                                  {.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 32 Sara6E 2014-06-28T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-28T00:00:00)
    0000   0x7b 0x0e                                  {.
    body (49)
    hex
    0000   0x05 0x00 0x88 0x47 0xbd 0x05 0x00 0x00    ...G....
    0008   0x03 0x87 0x01 0x6b 0x28 0x02 0x1c 0x3c    ...k(..<
    0010   0x00 0x64 0x01 0x64 0x00 0xb8 0x00 0x00    .d.d....
    0018   0x00 0x00 0x04 0x03 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  136   71  189    5    0    0
              3  135    1  107   40    2   28   60
              0  100    1  100    0  184    0    0
              0    0    4    3    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 33 CalBGForPH 2014-06-28T00:16:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 49}
```
    op hex (2)
    0000   0x0a 0x31                                  .1
    decimal
             10   49
    datetime (2014-06-28T00:16:03)
    0000   0x43 0x90 0x20 0x7c 0x0e                   C. |.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 Ian3F 2014-06-28T00:16:03 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2014-06-28T00:16:03)
    0000   0x43 0x90 0x20 0x7c 0x0e                   C. |.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 PumpSuspend 2014-06-28T00:25:29 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-28T00:25:29)
    0000   0x5d 0x99 0x00 0x1c 0x0e                   ]....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 CalBGForPH 2014-06-28T00:51:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 58}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2014-06-28T00:51:41)
    0000   0x69 0xb3 0x20 0x7c 0x0e                   i. |.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 37 Ian3F 2014-06-28T00:51:41 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-06-28T00:51:41)
    0000   0x69 0xb3 0x40 0x7c 0x0e                   i.@|.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 38 CalBGForPH 2014-06-28T01:35:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 54}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2014-06-28T01:35:05)
    0000   0x45 0xa3 0x21 0x7c 0x0e                   E.!|.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 39 Ian3F 2014-06-28T01:35:05 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2014-06-28T01:35:05)
    0000   0x45 0xa3 0xc1 0x7c 0x0e                   E..|.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 BasalProfileStart 2014-06-28T02:53:42 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-06-28T02:53:42)
    0000   0x6a 0xb5 0x02 0x1c 0x0e                   j....
    body (3)
    hex
    0000   0x00 0x19 0x00                             ...
    decimal
              0   25    0
    HOUR BITS: [1, 0, 1]
#### RECORD 41 PumpResume 2014-06-28T02:53:42 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-28T02:53:42)
    0000   0x6a 0xb5 0x02 0x1c 0x0e                   j....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 42 CalBGForPH 2014-06-28T02:53:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2014-06-28T02:53:56)
    0000   0x78 0xb5 0x22 0x1c 0x0e                   x."..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 43 BolusWizard 2014-06-28T02:54:03 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 160,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.0,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 2.0,
 'food_estimate': 0.0,
 'sensitivity': 30,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xa0                                  [.
    decimal
             91  160
    datetime (2014-06-28T02:54:03)
    0000   0x43 0xb6 0x02 0x1c 0x0e                   C....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x1e 0x50 0x50 0x00    .P.n.PP.
    0008   0x00 0x00 0x00 0x00 0x00 0x50 0x64         .....Pd
    decimal
              0   80    0  110   30   80   80    0
              0    0    0    0    0   80  100
    HOUR BITS: [1, 0, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 224, 'amount': 2.7, 'curve': 128},
 {'age': 254, 'amount': 3.1, 'curve': 128},
 {'age': 18, 'amount': 1.3, 'curve': 144},
 {'age': 48, 'amount': 1.8, 'curve': 144},
 {'age': 208, 'amount': 0.9, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x6c 0xe0 0x80 0x7c 0xfe 0x80    \.l..|..
    0008   0x34 0x12 0x90 0x48 0x30 0x90 0x24 0xd0    4..H0.$.
    0010   0x90                                       .
    decimal
             92   17  108  224  128  124  254  128
             52   18  144   72   48  144   36  208
            144
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2014-06-28T02:54:03 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.0,
 'duration': 0,
 'programmed': 3.0,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x78 0x00 0x78 0x00 0x00 0x00    ..x.x...
    decimal
              1    0  120    0  120    0    0    0
    datetime (2014-06-28T02:54:03)
    0000   0x43 0xb6 0x42 0x1c 0x0e                   C.B..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 46 BasalProfileStart 2014-06-28T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-06-28T04:00:00)
    0000   0x40 0x80 0x04 0x1c 0x0e                   @....
    body (3)
    hex
    0000   0x08 0x19 0x00                             ...
    decimal
              8   25    0
    HOUR BITS: [1, 0, 0]
#### RECORD 47 CalBGForPH 2014-06-28T05:25:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 239}
```
    op hex (2)
    0000   0x0a 0xef                                  ..
    decimal
             10  239
    datetime (2014-06-28T05:25:50)
    0000   0x72 0x99 0x25 0x1c 0x0e                   r.%..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 48 BolusWizard 2014-06-28T05:26:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 239,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 4.6,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': -1.8,
 'food_estimate': 0.0,
 'sensitivity': 30,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xef                                  [.
    decimal
             91  239
    datetime (2014-06-28T05:26:02)
    0000   0x42 0x9a 0x05 0x7c 0x0e                   B..|.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x1e 0x50 0xb8 0x00    .P.n.P..
    0008   0x00 0x00 0x00 0x00 0x00 0xb8 0x64         ......d
    decimal
              0   80    0  110   30   80  184    0
              0    0    0    0    0  184  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 156, 'amount': 3.0, 'curve': 128},
 {'age': 120, 'amount': 2.7, 'curve': 144},
 {'age': 150, 'amount': 3.1, 'curve': 144},
 {'age': 170, 'amount': 1.3, 'curve': 144},
 {'age': 200, 'amount': 1.8, 'curve': 144}]
```
    op hex (17)
    0000   0x5c 0x11 0x78 0x9c 0x80 0x6c 0x78 0x90    \.x..lx.
    0008   0x7c 0x96 0x90 0x34 0xaa 0x90 0x48 0xc8    |..4..H.
    0010   0x90                                       .
    decimal
             92   17  120  156  128  108  120  144
            124  150  144   52  170  144   72  200
            144
    datetime (unknown)

    body (0)

#### RECORD 50 Bolus 2014-06-28T05:26:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.3,
 'duration': 0,
 'programmed': 2.3,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x5c 0x00 0x5c 0x00 0x00 0x00    ..\.\...
    decimal
              1    0   92    0   92    0    0    0
    datetime (2014-06-28T05:26:02)
    0000   0x42 0x9a 0x45 0x7c 0x0e                   B.E|.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 BasalProfileStart 2014-06-28T06:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-06-28T06:00:00)
    0000   0x40 0x80 0x06 0x1c 0x0e                   @....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 0, 0]
#### RECORD 52 CalBGForPH 2014-06-28T07:00:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 284}
```
    op hex (2)
    0000   0x0a 0x1c                                  ..
    decimal
             10   28
    datetime (2014-06-28T07:00:53)
    0000   0x75 0x80 0x27 0x1c 0x8e                   u.'..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 53 BolusWizard 2014-06-28T07:01:02 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 284,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 4.3,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': -1.8,
 'food_estimate': 0.0,
 'sensitivity': 40,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0x1c                                  [.
    decimal
             91   28
    datetime (2014-06-28T07:01:02)
    0000   0x42 0x81 0x07 0x1c 0x0e                   B....
    body (15)
    hex
    0000   0x00 0x51 0x00 0x6e 0x28 0x50 0xb8 0x00    .Q.n(P..
    0008   0x00 0x00 0x00 0x0c 0x00 0xac 0x64         ......d
    decimal
              0   81    0  110   40   80  184    0
              0    0    0   12    0  172  100
    HOUR BITS: [1, 0, 0]
#### RECORD 54 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 101, 'amount': 2.3, 'curve': 128},
 {'age': 251, 'amount': 3.0, 'curve': 128},
 {'age': 215, 'amount': 2.7, 'curve': 144}]
```
    op hex (11)
    0000   0x5c 0x0b 0x5c 0x65 0x80 0x78 0xfb 0x80    \.\e.x..
    0008   0x6c 0xd7 0x90                             l..
    decimal
             92   11   92  101  128  120  251  128
            108  215  144
    datetime (unknown)

    body (0)

#### RECORD 55 Bolus 2014-06-28T07:01:02 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0,
 'duration': 0,
 'programmed': 2.0,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x50 0x00 0x50 0x00 0x0c 0x00    ..P.P...
    decimal
              1    0   80    0   80    0   12    0
    datetime (2014-06-28T07:01:02)
    0000   0x42 0x81 0x47 0x1c 0x0e                   B.G..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 56 CalBGForPH 2014-06-28T08:18:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 188}
```
    op hex (2)
    0000   0x0a 0xbc                                  ..
    decimal
             10  188
    datetime (2014-06-28T08:18:53)
    0000   0x75 0x92 0x28 0x7c 0x0e                   u.(|.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 57 Ian3F 2014-06-28T08:18:53 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2014-06-28T08:18:53)
    0000   0x75 0x92 0x88 0x7c 0x0e                   u..|.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 58 PumpSuspend 2014-06-28T08:19:30 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-28T08:19:30)
    0000   0x5e 0x93 0x08 0x1c 0x0e                   ^....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 CalBGForPH 2014-06-28T09:40:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 58}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2014-06-28T09:40:25)
    0000   0x59 0xa8 0x29 0x7c 0x0e                   Y.)|.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 60 Ian3F 2014-06-28T09:40:25 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-06-28T09:40:25)
    0000   0x59 0xa8 0x49 0x7c 0x0e                   Y.I|.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 BasalProfileStart 2014-06-28T10:53:49 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-28T10:53:49)
    0000   0x71 0xb5 0x0a 0x1c 0x0e                   q....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 1]
#### RECORD 62 PumpResume 2014-06-28T10:53:49 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-28T10:53:49)
    0000   0x71 0xb5 0x0a 0x1c 0x0e                   q....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 63 CalBGForPH 2014-06-28T10:54:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 244}
```
    op hex (2)
    0000   0x0a 0xf4                                  ..
    decimal
             10  244
    datetime (2014-06-28T10:54:03)
    0000   0x43 0xb6 0x2a 0x1c 0x0e                   C.*..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 64 BolusWizard 2014-06-28T10:54:09 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 244,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 2.8,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xf4                                  [.
    decimal
             91  244
    datetime (2014-06-28T10:54:09)
    0000   0x49 0xb6 0x0a 0x7c 0x0e                   I..|.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x70 0x00    .P.x2Pp.
    0008   0x00 0x00 0x00 0x00 0x00 0x70 0x64         .....pd
    decimal
              0   80    0  120   50   80  112    0
              0    0    0    0    0  112  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 65 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 234, 'amount': 2.0, 'curve': 128},
 {'age': 78, 'amount': 2.3, 'curve': 144}]
```
    op hex (8)
    0000   0x5c 0x08 0x50 0xea 0x80 0x5c 0x4e 0x90    \.P..\N.
    decimal
             92    8   80  234  128   92   78  144
    datetime (unknown)

    body (0)

#### RECORD 66 Bolus 2014-06-28T10:54:09 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.4,
 'duration': 0,
 'programmed': 1.4,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x38 0x00 0x38 0x00 0x00 0x00    ..8.8...
    decimal
              1    0   56    0   56    0    0    0
    datetime (2014-06-28T10:54:09)
    0000   0x49 0xb6 0x4a 0x7c 0x0e                   I.J|.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 PumpSuspend 2014-06-28T10:55:15 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-28T10:55:15)
    0000   0x4f 0xb7 0x0a 0x1c 0x0e                   O....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 68 CalBGForPH 2014-06-28T11:53:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 239}
```
    op hex (2)
    0000   0x0a 0xef                                  ..
    decimal
             10  239
    datetime (2014-06-28T11:53:37)
    0000   0x65 0xb5 0x2b 0x7c 0x0e                   e.+|.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 69 Ian3F 2014-06-28T11:53:37 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2014-06-28T11:53:37)
    0000   0x65 0xb5 0xeb 0x7c 0x0e                   e..|.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 BasalProfileStart 2014-06-28T14:02:56 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-28T14:02:56)
    0000   0x78 0x82 0x0e 0x1c 0x0e                   x....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 71 PumpResume 2014-06-28T14:02:56 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-28T14:02:56)
    0000   0x78 0x82 0x0e 0x1c 0x0e                   x....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 72 PumpSuspend 2014-06-28T19:11:02 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-28T19:11:02)
    0000   0x42 0x8b 0x13 0x1c 0x0e                   B....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 73 CalBGForPH 2014-06-28T19:47:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2014-06-28T19:47:19)
    0000   0x53 0xaf 0x33 0x7c 0x0e                   S.3|.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 74 Ian3F 2014-06-28T19:47:19 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2014-06-28T19:47:19)
    0000   0x53 0xaf 0x13 0x7c 0x0e                   S..|.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 75 BasalProfileStart 2014-06-28T21:08:11 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-28T21:08:11)
    0000   0x4b 0x88 0x15 0x1c 0x0e                   K....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 76 PumpResume 2014-06-28T21:08:11 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-28T21:08:11)
    0000   0x4b 0x88 0x15 0x1c 0x0e                   K....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 77 CalBGForPH 2014-06-28T21:08:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 80}
```
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2014-06-28T21:08:15)
    0000   0x4f 0x88 0x35 0x1c 0x0e                   O.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 78 BolusWizard 2014-06-28T21:08:24 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 80,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 1.0,
 'carb_input': 12,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2014-06-28T21:08:24)
    0000   0x58 0x88 0x15 0x1c 0x0e                   X....
    body (15)
    hex
    0000   0x0c 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x28 0x00 0x00 0x00 0x00 0x28 0x64         (....(d
    decimal
             12   80    0  110   50   80    0    0
             40    0    0    0    0   40  100
    HOUR BITS: [1, 0, 0]
#### RECORD 79 Bolus 2014-06-28T21:08:24 head[8], body[0] op[0x01]
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
    datetime (2014-06-28T21:08:24)
    0000   0x58 0x88 0x55 0x1c 0x0e                   X.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 80 BolusWizard 2014-06-28T21:16:07 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 80,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 5.0,
 'carb_input': 55,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 1.0}
```
    op hex (2)
    0000   0x5b 0x50                                  [P
    decimal
             91   80
    datetime (2014-06-28T21:16:07)
    0000   0x47 0x90 0x15 0x7c 0x0e                   G..|.
    body (15)
    hex
    0000   0x37 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    7P.n2P..
    0008   0xc8 0x00 0x00 0x28 0x00 0xc8 0x64         ...(..d
    decimal
             55   80    0  110   50   80    0    0
            200    0    0   40    0  200  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 81 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 16, 'amount': 1.0, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x28 0x10 0x80                   \.(..
    decimal
             92    5   40   16  128
    datetime (unknown)

    body (0)

#### RECORD 82 Bolus 2014-06-28T21:16:07 head[8], body[0] op[0x01]
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
    datetime (2014-06-28T21:16:07)
    0000   0x47 0x90 0x55 0x7c 0x0e                   G.U|.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 83 BolusWizard 2014-06-28T21:40:34 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.2,
 'carb_input': 25,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 2.2,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-28T21:40:34)
    0000   0x62 0xa8 0x15 0x7c 0x0e                   b..|.
    body (15)
    hex
    0000   0x19 0x50 0x00 0x6e 0x32 0x50 0x00 0x00    .P.n2P..
    0008   0x58 0x00 0x00 0x00 0x00 0x58 0x64         X....Xd
    decimal
             25   80    0  110   50   80    0    0
             88    0    0    0    0   88  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 84 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 30, 'amount': 5.0, 'curve': 128},
 {'age': 40, 'amount': 1.0, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0xc8 0x1e 0x80 0x28 0x28 0x80    \....((.
    decimal
             92    8  200   30  128   40   40  128
    datetime (unknown)

    body (0)

`end brandon-ReadHistoryData-page-3.data: 85 records`
```
+ for x in 'brandon-ReadHistoryData-page-*.data'
+ echo brandon-ReadHistoryData-page-4.data
brandon-ReadHistoryData-page-4.data
+ python list_history.py --larger brandon-ReadHistoryData-page-4.data
```
## START brandon-ReadHistoryData-page-4.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe9 0x4b                                  .K
##### DEBUG DECIMAL
            233   75
#### RECORD 0 Sara6E 2014-06-19T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-19T00:00:00)
    0000   0x72 0x0e                                  r.
    body (49)
    hex
    0000   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 1 CalBGForPH 2014-06-19T15:59:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 239}
```
    op hex (2)
    0000   0x0a 0xef                                  ..
    decimal
             10  239
    datetime (2014-06-19T15:59:48)
    0000   0x70 0xbb 0x2f 0x73 0x0e                   p./s.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2014-06-19T15:59:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2014-06-19T15:59:48)
    0000   0x70 0xbb 0xef 0x73 0x0e                   p..s.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 MResultTotals 2014-06-20T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-20T00:00:00)
    0000   0x73 0x0e                                  s.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 4 Sara6E 2014-06-20T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-20T00:00:00)
    0000   0x73 0x0e                                  s.
    body (49)
    hex
    0000   0x05 0x00 0xef 0xef 0xef 0x01 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  239  239  239    1    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 5 LowBattery 2014-06-20T02:02:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2014-06-20T02:02:00)
    0000   0x40 0x82 0x02 0x14 0x0e                   @....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 NoDelivery 2014-06-20T08:01:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x0a 0x21 0x3c                        ..!<
    decimal
              6   10   33   60
    datetime (2014-06-20T08:01:00)
    0000   0x40 0x81 0x68 0x14 0x0e                   @.h..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 7 Battery 2014-06-20T08:25:48 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2014-06-20T08:25:48)
    0000   0x70 0x99 0x08 0x14 0x0e                   p....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 8 ClearAlarm 2012-01-01T00:00:00 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x0a                                  ..
    decimal
             12   10
    datetime (2012-01-01T00:00:00)
    0000   0x00 0x40 0x00 0x01 0x0c                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 9 NoDelivery 2014-06-20T08:25:48 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x03 0x03 0xa3                        ....
    decimal
              6    3    3  163
    datetime (2014-06-20T08:25:48)
    0000   0x70 0x99 0x68 0x14 0x0e                   p.h..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 10 ClearAlarm 2012-01-01T00:00:18 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x03                                  ..
    decimal
             12    3
    datetime (2012-01-01T00:00:18)
    0000   0x12 0x40 0x00 0x01 0x0c                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 11 ChangeTimeDisplay 2012-01-01T00:00:19 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2012-01-01T00:00:19)
    0000   0x13 0x40 0x00 0x01 0x0c                   .@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 12 ChangeTime 2012-01-01T00:00:58 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2012-01-01T00:00:58)
    0000   0x3a 0x40 0x00 0x01 0x0c                   :@...
    body (0)
    HOUR BITS: [0, 1, 0]
#### RECORD 13 NewTimeSet 2014-06-25T23:37:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2014-06-25T23:37:00)
    0000   0x40 0xa5 0x17 0x19 0x0e                   @....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 14 MResultTotals 2014-06-21T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-21T00:00:00)
    0000   0x74 0x0e                                  t.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 15 Sara6E 2014-06-21T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-21T00:00:00)
    0000   0x74 0x0e                                  t.
    body (49)
    hex
    0000   0x05 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 16 BasalProfileStart 2014-06-25T23:37:04 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 81000000, 'rate': 0.65}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-06-25T23:37:04)
    0000   0x44 0xa5 0x17 0x19 0x0e                   D....
    body (3)
    hex
    0000   0x2d 0x1a 0x00                             -..
    decimal
             45   26    0
    HOUR BITS: [1, 0, 1]
#### RECORD 17 PumpResume 2014-06-25T23:37:04 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-25T23:37:04)
    0000   0x44 0xa5 0x17 0x19 0x0e                   D....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 18 Rewind 2014-06-25T23:37:17 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2014-06-25T23:37:17)
    0000   0x51 0xa5 0x17 0x19 0x0e                   Q....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 19 Prime 2014-06-25T23:44:30 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 9.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x61                   ....a
    decimal
              3    0    0    0   97
    datetime (2014-06-25T23:44:30)
    0000   0x5e 0xac 0x37 0x19 0x0e                   ^.7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 20 BasalProfileStart 2014-06-25T23:45:29 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 81000000, 'rate': 0.65}
```
    op hex (2)
    0000   0x7b 0x04                                  {.
    decimal
            123    4
    datetime (2014-06-25T23:45:29)
    0000   0x5d 0xad 0x17 0x19 0x0e                   ]....
    body (3)
    hex
    0000   0x2d 0x1a 0x00                             -..
    decimal
             45   26    0
    HOUR BITS: [1, 0, 1]
#### RECORD 21 Prime 2014-06-25T23:45:19 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.3, 'fixed': 0.3, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2014-06-25T23:45:19)
    0000   0x53 0xad 0x17 0x19 0x0e                   S....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 CalBGForPH 2014-06-25T23:45:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 191}
```
    op hex (2)
    0000   0x0a 0xbf                                  ..
    decimal
             10  191
    datetime (2014-06-25T23:45:52)
    0000   0x74 0xad 0x37 0x19 0x0e                   t.7..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 23 BolusWizard 2014-06-25T23:45:57 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 191,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.6,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 2.6,
 'food_estimate': 0.0,
 'sensitivity': 35,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xbf                                  [.
    decimal
             91  191
    datetime (2014-06-25T23:45:57)
    0000   0x79 0xad 0x17 0x19 0x0e                   y....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x23 0x50 0x68 0x00    .P.n#Ph.
    0008   0x00 0x00 0x00 0x00 0x00 0x68 0x64         .....hd
    decimal
              0   80    0  110   35   80  104    0
              0    0    0    0    0  104  100
    HOUR BITS: [1, 0, 1]
#### RECORD 24 Bolus 2014-06-25T23:45:57 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x00 0x00    ..<.<...
    decimal
              1    0   60    0   60    0    0    0
    datetime (2014-06-25T23:45:57)
    0000   0x79 0xad 0x57 0x19 0x0e                   y.W..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 25 BasalProfileStart 2014-06-26T00:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-06-26T00:00:00)
    0000   0x40 0x80 0x00 0x1a 0x0e                   @....
    body (3)
    hex
    0000   0x00 0x19 0x00                             ...
    decimal
              0   25    0
    HOUR BITS: [1, 0, 0]
#### RECORD 26 MResultTotals 2014-06-26T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x42                   ....B
    decimal
              7    0    0    0   66
    datetime (2014-06-26T00:00:00)
    0000   0x79 0x0e                                  y.
    body (3)
    hex
    0000   0x01 0x25 0x17                             .%.
    decimal
              1   37   23

#### RECORD 27 Sara6E 2014-06-26T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-26T00:00:00)
    0000   0x79 0x0e                                  y.
    body (49)
    hex
    0000   0x15 0x00 0xbf 0x00 0x00 0x01 0x00 0x00    ........
    0008   0x00 0x42 0x00 0x06 0x09 0x00 0x3c 0x5b    .B....<[
    0010   0x00 0x00 0x00 0x00 0x00 0x3c 0x00 0x00    .....<..
    0018   0x00 0x00 0x00 0x01 0x00 0x00 0x50 0x00    ......P.
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xbf    ........
    0028   0xbf 0x00 0x00 0x00 0x80 0x00 0x00 0x00    ........
    0030   0xb8                                       .
    decimal
             21    0  191    0    0    1    0    0
              0   66    0    6    9    0   60   91
              0    0    0    0    0   60    0    0
              0    0    0    1    0    0   80    0
              0    0    0    0    0    0    0  191
            191    0    0    0  128    0    0    0
            184

#### RECORD 28 BasalProfileStart 2014-06-26T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-06-26T04:00:00)
    0000   0x40 0x80 0x04 0x1a 0x0e                   @....
    body (3)
    hex
    0000   0x08 0x19 0x00                             ...
    decimal
              8   25    0
    HOUR BITS: [1, 0, 0]
#### RECORD 29 BasalProfileStart 2014-06-26T06:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-06-26T06:00:00)
    0000   0x40 0x80 0x06 0x1a 0x0e                   @....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 0, 0]
#### RECORD 30 CalBGForPH 2014-06-26T07:25:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 58}
```
    op hex (2)
    0000   0x0a 0x3a                                  .:
    decimal
             10   58
    datetime (2014-06-26T07:25:33)
    0000   0x61 0x99 0x27 0x7a 0x0e                   a.'z.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 Ian3F 2014-06-26T07:25:33 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-06-26T07:25:33)
    0000   0x61 0x99 0x47 0x7a 0x0e                   a.Gz.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 PumpSuspend 2014-06-26T07:26:49 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-26T07:26:49)
    0000   0x71 0x9a 0x07 0x1a 0x0e                   q....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 33 BasalProfileStart 2014-06-26T11:21:26 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-26T11:21:26)
    0000   0x5a 0x95 0x0b 0x1a 0x0e                   Z....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 34 PumpResume 2014-06-26T11:21:26 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-26T11:21:26)
    0000   0x5a 0x95 0x0b 0x1a 0x0e                   Z....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 BolusWizard 2014-06-26T11:21:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 1.2,
 'carb_input': 15,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-26T11:21:33)
    0000   0x61 0x95 0x0b 0x7a 0x0e                   a..z.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x64         0....0d
    decimal
             15   80    0  120   50   80    0    0
             48    0    0    0    0   48  100
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 Battery 2014-06-26T11:21:53 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2014-06-26T11:21:53)
    0000   0x75 0x95 0x0b 0x1a 0x0e                   u....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 37 BasalProfileStart 2014-06-26T11:21:54 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-26T11:21:54)
    0000   0x76 0x95 0x0b 0x1a 0x0e                   v....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 38 Bolus 2014-06-26T11:21:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2,
 'duration': 0,
 'programmed': 1.2,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x00 0x00    ..0.0...
    decimal
              1    0   48    0   48    0    0    0
    datetime (2014-06-26T11:21:33)
    0000   0x61 0x95 0x4b 0x7a 0x0e                   a.Kz.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 CalBGForPH 2014-06-26T12:45:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 191}
```
    op hex (2)
    0000   0x0a 0xbf                                  ..
    decimal
             10  191
    datetime (2014-06-26T12:45:35)
    0000   0x63 0xad 0x2c 0x1a 0x0e                   c.,..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 40 BolusWizard 2014-06-26T12:45:38 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 191,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 1.8,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.3}
```
    op hex (2)
    0000   0x5b 0xbf                                  [.
    decimal
             91  191
    datetime (2014-06-26T12:45:38)
    0000   0x66 0xad 0x0c 0x7a 0x0e                   f..z.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x78 0x32 0x50 0x48 0x00    .P.x2PH.
    0008   0x00 0x00 0x00 0x0c 0x00 0x3c 0x64         .....<d
    decimal
              0   80    0  120   50   80   72    0
              0    0    0   12    0   60  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 85, 'amount': 1.2, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0x55 0x80                   \.0U.
    decimal
             92    5   48   85  128
    datetime (unknown)

    body (0)

#### RECORD 42 Bolus 2014-06-26T12:45:38 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.5,
 'duration': 0,
 'programmed': 1.5,
 'type': 'normal',
 'unabsorbed': 0.3}
```
    op hex (8)
    0000   0x01 0x00 0x3c 0x00 0x3c 0x00 0x0c 0x00    ..<.<...
    decimal
              1    0   60    0   60    0   12    0
    datetime (2014-06-26T12:45:38)
    0000   0x66 0xad 0x4c 0x7a 0x0e                   f.Lz.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 BolusWizard 2014-06-26T13:47:33 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 0,
 'bg_target_high': 120,
 'bg_target_low': 80,
 'bolus_estimate': 1.2,
 'carb_input': 15,
 'carb_ratio': 10.0,
 'correction_estimate': 0.0,
 'food_estimate': 1.2,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2014-06-26T13:47:33)
    0000   0x61 0xaf 0x0d 0x7a 0x0e                   a..z.
    body (15)
    hex
    0000   0x0f 0x50 0x00 0x78 0x32 0x50 0x00 0x00    .P.x2P..
    0008   0x30 0x00 0x00 0x00 0x00 0x30 0x64         0....0d
    decimal
             15   80    0  120   50   80    0    0
             48    0    0    0    0   48  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 67, 'amount': 1.5, 'curve': 128},
 {'age': 147, 'amount': 1.2, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x3c 0x43 0x80 0x30 0x93 0x80    \.<C.0..
    decimal
             92    8   60   67  128   48  147  128
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2014-06-26T13:47:33 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2,
 'duration': 0,
 'programmed': 1.2,
 'type': 'normal',
 'unabsorbed': 0.6}
```
    op hex (8)
    0000   0x01 0x00 0x30 0x00 0x30 0x00 0x18 0x00    ..0.0...
    decimal
              1    0   48    0   48    0   24    0
    datetime (2014-06-26T13:47:33)
    0000   0x61 0xaf 0x4d 0x7a 0x0e                   a.Mz.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 PumpSuspend 2014-06-26T16:22:48 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-26T16:22:48)
    0000   0x70 0x96 0x10 0x1a 0x0e                   p....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 47 CalBGForPH 2014-06-26T16:31:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2014-06-26T16:31:35)
    0000   0x63 0x9f 0x30 0x7a 0x0e                   c.0z.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 Ian3F 2014-06-26T16:31:35 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-26T16:31:35)
    0000   0x63 0x9f 0x50 0x7a 0x0e                   c.Pz.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 CalBGForPH 2014-06-26T16:32:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 148}
```
    op hex (2)
    0000   0x0a 0x94                                  ..
    decimal
             10  148
    datetime (2014-06-26T16:32:23)
    0000   0x57 0xa0 0x30 0x7a 0x0e                   W.0z.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 50 Ian3F 2014-06-26T16:32:23 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2014-06-26T16:32:23)
    0000   0x57 0xa0 0x90 0x7a 0x0e                   W..z.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 51 CalBGForPH 2014-06-26T19:19:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2014-06-26T19:19:31)
    0000   0x5f 0x93 0x33 0x7a 0x0e                   _.3z.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 Ian3F 2014-06-26T19:19:31 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-06-26T19:19:31)
    0000   0x5f 0x93 0x53 0x7a 0x0e                   _.Sz.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 BasalProfileStart 2014-06-26T20:30:18 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 37800000, 'rate': 0.47500000000000003}
```
    op hex (2)
    0000   0x7b 0x03                                  {.
    decimal
            123    3
    datetime (2014-06-26T20:30:18)
    0000   0x52 0x9e 0x14 0x1a 0x0e                   R....
    body (3)
    hex
    0000   0x15 0x13 0x00                             ...
    decimal
             21   19    0
    HOUR BITS: [1, 0, 0]
#### RECORD 54 PumpResume 2014-06-26T20:30:18 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-26T20:30:18)
    0000   0x52 0x9e 0x14 0x1a 0x0e                   R....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 55 CalBGForPH 2014-06-26T20:50:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2014-06-26T20:50:21)
    0000   0x55 0xb2 0x34 0x7a 0x0e                   U.4z.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 Ian3F 2014-06-26T20:50:21 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2014-06-26T20:50:21)
    0000   0x55 0xb2 0x14 0x7a 0x0e                   U..z.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 BolusWizard 2014-06-26T20:50:48 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 120,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 4.0,
 'carb_input': 40,
 'carb_ratio': 10.0,
 'correction_estimate': 0.4,
 'food_estimate': 3.6,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2014-06-26T20:50:48)
    0000   0x70 0xb2 0x14 0x1a 0x0e                   p....
    body (15)
    hex
    0000   0x28 0x50 0x00 0x6e 0x32 0x50 0x10 0x00    (P.n2P..
    0008   0x90 0x00 0x00 0x00 0x00 0xa0 0x64         ......d
    decimal
             40   80    0  110   50   80   16    0
            144    0    0    0    0  160  100
    HOUR BITS: [1, 0, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 174, 'amount': 1.2, 'curve': 144}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0xae 0x90                   \.0..
    decimal
             92    5   48  174  144
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2014-06-26T20:50:48 head[8], body[0] op[0x01]
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
    datetime (2014-06-26T20:50:48)
    0000   0x70 0xb2 0x54 0x1a 0x0e                   p.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 60 CalBGForPH 2014-06-26T21:55:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2014-06-26T21:55:52)
    0000   0x74 0xb7 0x35 0x1a 0x0e                   t.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 61 BolusWizard 2014-06-26T21:56:01 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 169,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 0.0,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 1.3,
 'food_estimate': 0.0,
 'sensitivity': 50,
 'unabsorbed_insulin_total': 1.4}
```
    op hex (2)
    0000   0x5b 0xa9                                  [.
    decimal
             91  169
    datetime (2014-06-26T21:56:01)
    0000   0x41 0xb8 0x15 0x7a 0x0e                   A..z.
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x32 0x50 0x34 0x00    .P.n2P4.
    0008   0x00 0x00 0x00 0x38 0x00 0x00 0x64         ...8..d
    decimal
              0   80    0  110   50   80   52    0
              0    0    0   56    0    0  100
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 66, 'amount': 3.5, 'curve': 128}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0x42 0x80                   \..B.
    decimal
             92    5  140   66  128
    datetime (unknown)

    body (0)

#### RECORD 63 Bolus 2014-06-26T21:56:01 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3,
 'duration': 0,
 'programmed': 1.3,
 'type': 'normal',
 'unabsorbed': 1.4}
```
    op hex (8)
    0000   0x01 0x00 0x34 0x00 0x34 0x00 0x38 0x00    ..4.4.8.
    decimal
              1    0   52    0   52    0   56    0
    datetime (2014-06-26T21:56:01)
    0000   0x41 0xb8 0x55 0x7a 0x0e                   A.Uz.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 CalBGForPH 2014-06-26T22:04:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 125}
```
    op hex (2)
    0000   0x0a 0x7d                                  .}
    decimal
             10  125
    datetime (2014-06-26T22:04:25)
    0000   0x59 0x84 0x36 0x7a 0x0e                   Y.6z.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 65 Ian3F 2014-06-26T22:04:25 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0f                                  ?.
    decimal
             63   15
    datetime (2014-06-26T22:04:25)
    0000   0x59 0x84 0xb6 0x7a 0x0e                   Y..z.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 66 PumpSuspend 2014-06-26T22:04:46 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-26T22:04:46)
    0000   0x6e 0x84 0x16 0x1a 0x0e                   n....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 67 CalBGForPH 2014-06-26T22:05:27 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 141}
```
    op hex (2)
    0000   0x0a 0x8d                                  ..
    decimal
             10  141
    datetime (2014-06-26T22:05:27)
    0000   0x5b 0x85 0x36 0x7a 0x0e                   [.6z.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 Ian3F 2014-06-26T22:05:27 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-06-26T22:05:27)
    0000   0x5b 0x85 0xb6 0x7a 0x0e                   [..z.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 69 CalBGForPH 2014-06-26T22:57:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 151}
```
    op hex (2)
    0000   0x0a 0x97                                  ..
    decimal
             10  151
    datetime (2014-06-26T22:57:43)
    0000   0x6b 0xb9 0x36 0x7a 0x0e                   k.6z.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 Ian3F 2014-06-26T22:57:43 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2014-06-26T22:57:43)
    0000   0x6b 0xb9 0xf6 0x7a 0x0e                   k..z.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 71 MResultTotals 2014-06-27T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x02 0x9d                   .....
    decimal
              7    0    0    2  157
    datetime (2014-06-27T00:00:00)
    0000   0x7a 0x0e                                  z.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 72 Sara6E 2014-06-27T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-27T00:00:00)
    0000   0x7a 0x0e                                  z.
    body (49)
    hex
    0000   0x05 0x00 0x88 0x3a 0x9a 0x0a 0x00 0x00    ...:....
    0008   0x02 0x9d 0x01 0x41 0x30 0x01 0x5c 0x34    ...A0.\4
    0010   0x00 0x46 0x00 0xec 0x00 0x70 0x00 0x00    .F...p..
    0018   0x00 0x00 0x03 0x02 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0xa9    ........
    0028   0xbf 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  136   58  154   10    0    0
              2  157    1   65   48    1   92   52
              0   70    0  236    0  112    0    0
              0    0    3    2    0    0    0    0
              0    0    0    0    0    0    0  169
            191    0    0    0    0    0    0    0
              0

#### RECORD 73 CalBGForPH 2014-06-27T00:15:29 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2014-06-27T00:15:29)
    0000   0x5d 0x8f 0x20 0x7b 0x0e                   ]. {.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 74 Ian3F 2014-06-27T00:15:29 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2014-06-27T00:15:29)
    0000   0x5d 0x8f 0xa0 0x7b 0x0e                   ]..{.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 75 BasalProfileStart 2014-06-27T00:15:39 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 0, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x00                                  {.
    decimal
            123    0
    datetime (2014-06-27T00:15:39)
    0000   0x67 0x8f 0x00 0x1b 0x0e                   g....
    body (3)
    hex
    0000   0x00 0x19 0x00                             ...
    decimal
              0   25    0
    HOUR BITS: [1, 0, 0]
#### RECORD 76 PumpResume 2014-06-27T00:15:39 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-27T00:15:39)
    0000   0x67 0x8f 0x00 0x1b 0x0e                   g....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 77 BolusWizard 2014-06-27T00:15:42 head[2], body[15] op[0x5b]
###### DECODED
```python
{'bg': 189,
 'bg_target_high': 110,
 'bg_target_low': 80,
 'bolus_estimate': 2.9,
 'carb_input': 0,
 'carb_ratio': 10.0,
 'correction_estimate': 2.9,
 'food_estimate': 0.0,
 'sensitivity': 30,
 'unabsorbed_insulin_total': 0.0}
```
    op hex (2)
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2014-06-27T00:15:42)
    0000   0x6a 0x8f 0x00 0x1b 0x0e                   j....
    body (15)
    hex
    0000   0x00 0x50 0x00 0x6e 0x1e 0x50 0x74 0x00    .P.n.Pt.
    0008   0x00 0x00 0x00 0x00 0x00 0x74 0x64         .....td
    decimal
              0   80    0  110   30   80  116    0
              0    0    0    0    0  116  100
    HOUR BITS: [1, 0, 0]
#### RECORD 78 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 145, 'amount': 1.3, 'curve': 128},
 {'age': 205, 'amount': 3.5, 'curve': 128}]
```
    op hex (8)
    0000   0x5c 0x08 0x34 0x91 0x80 0x8c 0xcd 0x80    \.4.....
    decimal
             92    8   52  145  128  140  205  128
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2014-06-27T00:15:43 head[8], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9,
 'duration': 0,
 'programmed': 2.9,
 'type': 'normal',
 'unabsorbed': 0.0}
```
    op hex (8)
    0000   0x01 0x00 0x74 0x00 0x74 0x00 0x00 0x00    ..t.t...
    decimal
              1    0  116    0  116    0    0    0
    datetime (2014-06-27T00:15:43)
    0000   0x6b 0x8f 0x40 0x1b 0x0e                   k.@..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 80 BasalProfileStart 2014-06-27T04:00:00 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 14400000, 'rate': 0.625}
```
    op hex (2)
    0000   0x7b 0x01                                  {.
    decimal
            123    1
    datetime (2014-06-27T04:00:00)
    0000   0x40 0x80 0x04 0x1b 0x0e                   @....
    body (3)
    hex
    0000   0x08 0x19 0x00                             ...
    decimal
              8   25    0
    HOUR BITS: [1, 0, 0]
`end brandon-ReadHistoryData-page-4.data: 81 records`
```
+ for x in 'brandon-ReadHistoryData-page-*.data'
+ echo brandon-ReadHistoryData-page-5.data
brandon-ReadHistoryData-page-5.data
+ python list_history.py --larger brandon-ReadHistoryData-page-5.data
```
## START brandon-ReadHistoryData-page-5.data
#### STOPPING DOUBLE NULLS @ 1019, found 3 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x35 0x44                                  5D
##### DEBUG DECIMAL
             53   68
#### RECORD 0 Sara6E 2014-06-10T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-10T00:00:00)
    0000   0x69 0x0e                                  i.
    body (49)
    hex
    0000   0x05 0x00 0x53 0x2c 0x9a 0x05 0x00 0x00    ..S,....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0   83   44  154    5    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 1 CalBGForPH 2014-06-10T06:58:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 54}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2014-06-10T06:58:12)
    0000   0x4c 0xba 0x26 0x6a 0x0e                   L.&j.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 2 Ian3F 2014-06-10T06:58:12 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2014-06-10T06:58:12)
    0000   0x4c 0xba 0xc6 0x6a 0x0e                   L..j.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 3 CalBGForPH 2014-06-10T13:29:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 139}
```
    op hex (2)
    0000   0x0a 0x8b                                  ..
    decimal
             10  139
    datetime (2014-06-10T13:29:04)
    0000   0x44 0x9d 0x2d 0x6a 0x0e                   D.-j.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 4 Ian3F 2014-06-10T13:29:04 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-06-10T13:29:04)
    0000   0x44 0x9d 0x6d 0x6a 0x0e                   D.mj.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 5 CalBGForPH 2014-06-10T15:36:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 157}
```
    op hex (2)
    0000   0x0a 0x9d                                  ..
    decimal
             10  157
    datetime (2014-06-10T15:36:52)
    0000   0x74 0xa4 0x2f 0x6a 0x0e                   t./j.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 6 Ian3F 2014-06-10T15:36:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-10T15:36:52)
    0000   0x74 0xa4 0xaf 0x6a 0x0e                   t..j.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 7 MResultTotals 2014-06-11T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-11T00:00:00)
    0000   0x6a 0x0e                                  j.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 8 Sara6E 2014-06-11T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-11T00:00:00)
    0000   0x6a 0x0e                                  j.
    body (49)
    hex
    0000   0x05 0x00 0x75 0x36 0x9d 0x03 0x00 0x00    ..u6....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  117   54  157    3    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 9 CalBGForPH 2014-06-11T07:24:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2014-06-11T07:24:06)
    0000   0x46 0x98 0x27 0x6b 0x0e                   F.'k.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 10 Ian3F 2014-06-11T07:24:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-06-11T07:24:06)
    0000   0x46 0x98 0x87 0x6b 0x0e                   F..k.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 11 CalBGForPH 2014-06-11T13:49:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2014-06-11T13:49:56)
    0000   0x78 0xb1 0x2d 0x6b 0x0e                   x.-k.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 12 Ian3F 2014-06-11T13:49:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-06-11T13:49:56)
    0000   0x78 0xb1 0x6d 0x6b 0x0e                   x.mk.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 CalBGForPH 2014-06-11T15:56:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2014-06-11T15:56:52)
    0000   0x74 0xb8 0x2f 0x6b 0x0e                   t./k.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 Ian3F 2014-06-11T15:56:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-11T15:56:52)
    0000   0x74 0xb8 0x2f 0x6b 0x0e                   t./k.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 15 CalBGForPH 2014-06-11T22:54:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 134}
```
    op hex (2)
    0000   0x0a 0x86                                  ..
    decimal
             10  134
    datetime (2014-06-11T22:54:00)
    0000   0x40 0xb6 0x36 0x6b 0x0e                   @.6k.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 16 Ian3F 2014-06-11T22:54:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-06-11T22:54:00)
    0000   0x40 0xb6 0xd6 0x6b 0x0e                   @..k.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 17 MResultTotals 2014-06-12T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-12T00:00:00)
    0000   0x6b 0x0e                                  k.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 18 Sara6E 2014-06-12T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-12T00:00:00)
    0000   0x6b 0x0e                                  k.
    body (49)
    hex
    0000   0x05 0x00 0x8e 0x6c 0xab 0x04 0x00 0x00    ...l....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  142  108  171    4    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 19 CalBGForPH 2014-06-12T07:07:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2014-06-12T07:07:02)
    0000   0x42 0x87 0x27 0x6c 0x0e                   B.'l.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 Ian3F 2014-06-12T07:07:02 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-06-12T07:07:02)
    0000   0x42 0x87 0xc7 0x6c 0x0e                   B..l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 21 CalBGForPH 2014-06-12T22:45:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 52}
```
    op hex (2)
    0000   0x0a 0x34                                  .4
    decimal
             10   52
    datetime (2014-06-12T22:45:14)
    0000   0x4e 0xad 0x36 0x6c 0x0e                   N.6l.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 Ian3F 2014-06-12T22:45:14 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2014-06-12T22:45:14)
    0000   0x4e 0xad 0x96 0x6c 0x0e                   N..l.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 23 MResultTotals 2014-06-13T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-13T00:00:00)
    0000   0x6c 0x0e                                  l.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 24 Sara6E 2014-06-13T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-13T00:00:00)
    0000   0x6c 0x0e                                  l.
    body (49)
    hex
    0000   0x05 0x00 0x61 0x34 0x8e 0x02 0x00 0x00    ..a4....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0   97   52  142    2    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 25 CalBGForPH 2014-06-13T07:15:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2014-06-13T07:15:48)
    0000   0x70 0x8f 0x27 0x6d 0x0e                   p.'m.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 Ian3F 2014-06-13T07:15:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-06-13T07:15:48)
    0000   0x70 0x8f 0xa7 0x6d 0x0e                   p..m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 CalBGForPH 2014-06-13T07:16:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 66}
```
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2014-06-13T07:16:34)
    0000   0x62 0x90 0x27 0x6d 0x0e                   b.'m.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 Ian3F 2014-06-13T07:16:34 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-06-13T07:16:34)
    0000   0x62 0x90 0x47 0x6d 0x0e                   b.Gm.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 CalBGForPH 2014-06-13T08:05:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 79}
```
    op hex (2)
    0000   0x0a 0x4f                                  .O
    decimal
             10   79
    datetime (2014-06-13T08:05:40)
    0000   0x68 0x85 0x28 0x6d 0x0e                   h.(m.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 Ian3F 2014-06-13T08:05:40 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2014-06-13T08:05:40)
    0000   0x68 0x85 0xe8 0x6d 0x0e                   h..m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 31 CalBGForPH 2014-06-13T09:12:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2014-06-13T09:12:40)
    0000   0x68 0x8c 0x29 0x6d 0x0e                   h.)m.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 32 Ian3F 2014-06-13T09:12:40 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-06-13T09:12:40)
    0000   0x68 0x8c 0xc9 0x6d 0x0e                   h..m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 33 CalBGForPH 2014-06-13T09:13:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2014-06-13T09:13:24)
    0000   0x58 0x8d 0x29 0x6d 0x0e                   X.)m.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 34 Ian3F 2014-06-13T09:13:24 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-06-13T09:13:24)
    0000   0x58 0x8d 0x49 0x6d 0x0e                   X.Im.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 35 CalBGForPH 2014-06-13T09:27:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 114}
```
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2014-06-13T09:27:58)
    0000   0x7a 0x9b 0x29 0x6d 0x0e                   z.)m.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 36 Ian3F 2014-06-13T09:27:58 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2014-06-13T09:27:58)
    0000   0x7a 0x9b 0x49 0x6d 0x0e                   z.Im.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 CalBGForPH 2014-06-13T09:28:32 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 119}
```
    op hex (2)
    0000   0x0a 0x77                                  .w
    decimal
             10  119
    datetime (2014-06-13T09:28:32)
    0000   0x60 0x9c 0x29 0x6d 0x0e                   `.)m.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 Ian3F 2014-06-13T09:28:32 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2014-06-13T09:28:32)
    0000   0x60 0x9c 0xe9 0x6d 0x0e                   `..m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 CalBGForPH 2014-06-13T10:53:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 158}
```
    op hex (2)
    0000   0x0a 0x9e                                  ..
    decimal
             10  158
    datetime (2014-06-13T10:53:46)
    0000   0x6e 0xb5 0x2a 0x6d 0x0e                   n.*m.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 40 Ian3F 2014-06-13T10:53:46 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-13T10:53:46)
    0000   0x6e 0xb5 0xca 0x6d 0x0e                   n..m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 CalBGForPH 2014-06-13T23:57:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2014-06-13T23:57:20)
    0000   0x54 0xb9 0x37 0x6d 0x0e                   T.7m.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 Ian3F 2014-06-13T23:57:20 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-06-13T23:57:20)
    0000   0x54 0xb9 0x37 0x6d 0x0e                   T.7m.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 MResultTotals 2014-06-14T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-14T00:00:00)
    0000   0x6d 0x0e                                  m.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 44 Sara6E 2014-06-14T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-14T00:00:00)
    0000   0x6d 0x0e                                  m.
    body (49)
    hex
    0000   0x05 0x00 0x62 0x3d 0x9e 0x09 0x00 0x00    ..b=....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0   98   61  158    9    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 45 CalBGForPH 2014-06-14T03:45:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 70}
```
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2014-06-14T03:45:02)
    0000   0x42 0xad 0x23 0x6e 0x0e                   B.#n.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 Ian3F 2014-06-14T03:45:02 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-06-14T03:45:02)
    0000   0x42 0xad 0xc3 0x6e 0x0e                   B..n.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 47 CalBGForPH 2014-06-14T07:54:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 132}
```
    op hex (2)
    0000   0x0a 0x84                                  ..
    decimal
             10  132
    datetime (2014-06-14T07:54:36)
    0000   0x64 0xb6 0x27 0x6e 0x0e                   d.'n.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 48 Ian3F 2014-06-14T07:54:36 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-06-14T07:54:36)
    0000   0x64 0xb6 0x87 0x6e 0x0e                   d..n.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 49 MResultTotals 2014-06-15T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-15T00:00:00)
    0000   0x6e 0x0e                                  n.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 50 Sara6E 2014-06-15T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-15T00:00:00)
    0000   0x6e 0x0e                                  n.
    body (49)
    hex
    0000   0x05 0x00 0x65 0x46 0x84 0x02 0x00 0x00    ..eF....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  101   70  132    2    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 51 CalBGForPH 2014-06-15T05:31:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2014-06-15T05:31:54)
    0000   0x76 0x9f 0x25 0x6f 0x0e                   v.%o.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 Ian3F 2014-06-15T05:31:54 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2014-06-15T05:31:54)
    0000   0x76 0x9f 0xe5 0x6f 0x0e                   v..o.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 53 CalBGForPH 2014-06-15T08:08:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2014-06-15T08:08:18)
    0000   0x52 0x88 0x28 0x6f 0x0e                   R.(o.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 54 Ian3F 2014-06-15T08:08:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-06-15T08:08:18)
    0000   0x52 0x88 0xa8 0x6f 0x0e                   R..o.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 55 MResultTotals 2014-06-16T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-16T00:00:00)
    0000   0x6f 0x0e                                  o.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 56 Sara6E 2014-06-16T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-16T00:00:00)
    0000   0x6f 0x0e                                  o.
    body (49)
    hex
    0000   0x05 0x00 0x6a 0x67 0x6d 0x02 0x00 0x00    ..jgm...
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  106  103  109    2    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 57 CalBGForPH 2014-06-16T08:42:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2014-06-16T08:42:06)
    0000   0x46 0xaa 0x28 0x70 0x0e                   F.(p.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 Ian3F 2014-06-16T08:42:06 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-06-16T08:42:06)
    0000   0x46 0xaa 0xe8 0x70 0x0e                   F..p.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 59 MResultTotals 2014-06-17T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-17T00:00:00)
    0000   0x70 0x0e                                  p.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 60 Sara6E 2014-06-17T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-17T00:00:00)
    0000   0x70 0x0e                                  p.
    body (49)
    hex
    0000   0x05 0x00 0x87 0x87 0x87 0x01 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  135  135  135    1    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 61 CalBGForPH 2014-06-17T01:04:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2014-06-17T01:04:20)
    0000   0x54 0x84 0x21 0x71 0x0e                   T.!q.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 62 Ian3F 2014-06-17T01:04:20 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x16                                  ?.
    decimal
             63   22
    datetime (2014-06-17T01:04:20)
    0000   0x54 0x84 0x01 0x71 0x0e                   T..q.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 63 CalBGForPH 2014-06-17T06:21:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 204}
```
    op hex (2)
    0000   0x0a 0xcc                                  ..
    decimal
             10  204
    datetime (2014-06-17T06:21:14)
    0000   0x4e 0x95 0x26 0x71 0x0e                   N.&q.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 64 Ian3F 2014-06-17T06:21:14 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2014-06-17T06:21:14)
    0000   0x4e 0x95 0x86 0x71 0x0e                   N..q.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 65 CalBGForPH 2014-06-17T20:34:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2014-06-17T20:34:44)
    0000   0x6c 0xa2 0x34 0x71 0x0e                   l.4q.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 66 Ian3F 2014-06-17T20:34:44 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-06-17T20:34:44)
    0000   0x6c 0xa2 0x14 0x71 0x0e                   l..q.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 67 CalBGForPH 2014-06-17T20:35:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 153}
```
    op hex (2)
    0000   0x0a 0x99                                  ..
    decimal
             10  153
    datetime (2014-06-17T20:35:14)
    0000   0x4e 0xa3 0x34 0x71 0x0e                   N.4q.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 68 Ian3F 2014-06-17T20:35:14 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-17T20:35:14)
    0000   0x4e 0xa3 0x34 0x71 0x0e                   N.4q.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 69 MResultTotals 2014-06-18T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-18T00:00:00)
    0000   0x71 0x0e                                  q.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 70 Sara6E 2014-06-18T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-18T00:00:00)
    0000   0x71 0x0e                                  q.
    body (49)
    hex
    0000   0x05 0x00 0xad 0x99 0xcc 0x04 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  173  153  204    4    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 71 MResultTotals 2014-06-19T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-19T00:00:00)
    0000   0x72 0x0e                                  r.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end brandon-ReadHistoryData-page-5.data: 72 records`
```
+ for x in 'brandon-ReadHistoryData-page-*.data'
+ echo brandon-ReadHistoryData-page-6.data
brandon-ReadHistoryData-page-6.data
+ python list_history.py --larger brandon-ReadHistoryData-page-6.data
```
## START brandon-ReadHistoryData-page-6.data
#### STOPPING DOUBLE NULLS @ 1021, found 1 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x35 0x66                                  5f
##### DEBUG DECIMAL
             53  102
#### RECORD 0 BasalProfileStart 2014-06-02T09:01:55 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-06-02T09:01:55)
    0000   0x77 0x81 0x09 0x02 0x0e                   w....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 0, 0]
#### RECORD 1 PumpResume 2014-06-02T09:01:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-02T09:01:55)
    0000   0x77 0x81 0x09 0x02 0x0e                   w....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 2 PumpSuspend 2014-06-02T09:27:24 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-02T09:27:24)
    0000   0x58 0x9b 0x09 0x02 0x0e                   X....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 3 BasalProfileStart 2014-06-02T09:43:10 head[2], body[3] op[0x7b]
###### DECODED
```python
{'offset': 21600000, 'rate': 0.775}
```
    op hex (2)
    0000   0x7b 0x02                                  {.
    decimal
            123    2
    datetime (2014-06-02T09:43:10)
    0000   0x4a 0xab 0x09 0x02 0x0e                   J....
    body (3)
    hex
    0000   0x0c 0x1f 0x00                             ...
    decimal
             12   31    0
    HOUR BITS: [1, 0, 1]
#### RECORD 4 PumpResume 2014-06-02T09:43:10 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x20                                  . 
    decimal
             31   32
    datetime (2014-06-02T09:43:10)
    0000   0x4a 0xab 0x09 0x02 0x0e                   J....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 5 PumpSuspend 2014-06-02T10:15:37 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x01                                  ..
    decimal
             30    1
    datetime (2014-06-02T10:15:37)
    0000   0x65 0x8f 0x0a 0x02 0x0e                   e....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 CalBGForPH 2014-06-02T20:11:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2014-06-02T20:11:16)
    0000   0x50 0x8b 0x34 0x62 0x0e                   P.4b.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 7 Ian3F 2014-06-02T20:11:16 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2014-06-02T20:11:16)
    0000   0x50 0x8b 0xd4 0x62 0x0e                   P..b.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 8 CalBGForPH 2014-06-02T23:55:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 156}
```
    op hex (2)
    0000   0x0a 0x9c                                  ..
    decimal
             10  156
    datetime (2014-06-02T23:55:08)
    0000   0x48 0xb7 0x37 0x62 0x0e                   H.7b.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 9 Ian3F 2014-06-02T23:55:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-02T23:55:08)
    0000   0x48 0xb7 0x97 0x62 0x0e                   H..b.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 10 MResultTotals 2014-06-03T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0xea                   .....
    decimal
              7    0    0    0  234
    datetime (2014-06-03T00:00:00)
    0000   0x62 0x0e                                  b.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 11 Sara6E 2014-06-03T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-03T00:00:00)
    0000   0x62 0x0e                                  b.
    body (49)
    hex
    0000   0x05 0x00 0x68 0x45 0x9c 0x03 0x00 0x00    ..hE....
    0008   0x00 0xea 0x00 0xea 0x64 0x00 0x00 0x00    ....d...
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  104   69  156    3    0    0
              0  234    0  234  100    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 12 CalBGForPH 2014-06-03T07:42:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2014-06-03T07:42:54)
    0000   0x76 0xaa 0x27 0x63 0x0e                   v.'c.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 13 Ian3F 2014-06-03T07:42:54 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-06-03T07:42:54)
    0000   0x76 0xaa 0x07 0x63 0x0e                   v..c.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 14 MResultTotals 2014-06-04T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-04T00:00:00)
    0000   0x63 0x0e                                  c.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 15 Sara6E 2014-06-04T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-04T00:00:00)
    0000   0x63 0x0e                                  c.
    body (49)
    hex
    0000   0x05 0x00 0x80 0x80 0x80 0x01 0x00 0x00    ........
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  128  128  128    1    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 16 CalBGForPH 2014-06-04T00:03:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2014-06-04T00:03:08)
    0000   0x48 0x83 0x20 0x64 0x0e                   H. d.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 17 Ian3F 2014-06-04T00:03:08 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-06-04T00:03:08)
    0000   0x48 0x83 0xe0 0x64 0x0e                   H..d.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 18 CalBGForPH 2014-06-04T07:26:50 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2014-06-04T07:26:50)
    0000   0x72 0x9a 0x27 0x64 0x0e                   r.'d.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 19 Ian3F 2014-06-04T07:26:50 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-06-04T07:26:50)
    0000   0x72 0x9a 0x67 0x64 0x0e                   r.gd.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 20 CalBGForPH 2014-06-04T09:35:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 73}
```
    op hex (2)
    0000   0x0a 0x49                                  .I
    decimal
             10   73
    datetime (2014-06-04T09:35:56)
    0000   0x78 0xa3 0x29 0x64 0x0e                   x.)d.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 21 Ian3F 2014-06-04T09:35:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x09                                  ?.
    decimal
             63    9
    datetime (2014-06-04T09:35:56)
    0000   0x78 0xa3 0x29 0x64 0x0e                   x.)d.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 22 MResultTotals 2014-06-05T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-05T00:00:00)
    0000   0x64 0x0e                                  d.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 23 Sara6E 2014-06-05T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-05T00:00:00)
    0000   0x64 0x0e                                  d.
    body (49)
    hex
    0000   0x05 0x00 0x71 0x49 0xab 0x03 0x00 0x00    ..qI....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  113   73  171    3    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 24 CalBGForPH 2014-06-05T00:02:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 205}
```
    op hex (2)
    0000   0x0a 0xcd                                  ..
    decimal
             10  205
    datetime (2014-06-05T00:02:44)
    0000   0x6c 0x82 0x20 0x65 0x0e                   l. e.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 25 Ian3F 2014-06-05T00:02:44 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x19                                  ?.
    decimal
             63   25
    datetime (2014-06-05T00:02:44)
    0000   0x6c 0x82 0xa0 0x65 0x0e                   l..e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 26 CalBGForPH 2014-06-05T00:03:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 195}
```
    op hex (2)
    0000   0x0a 0xc3                                  ..
    decimal
             10  195
    datetime (2014-06-05T00:03:14)
    0000   0x4e 0x83 0x20 0x65 0x0e                   N. e.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 27 Ian3F 2014-06-05T00:03:14 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x18                                  ?.
    decimal
             63   24
    datetime (2014-06-05T00:03:14)
    0000   0x4e 0x83 0x60 0x65 0x0e                   N.`e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 28 CalBGForPH 2014-06-05T19:13:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2014-06-05T19:13:16)
    0000   0x50 0x8d 0x33 0x65 0x0e                   P.3e.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 29 Ian3F 2014-06-05T19:13:16 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2014-06-05T19:13:16)
    0000   0x50 0x8d 0x13 0x65 0x0e                   P..e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 30 CalBGForPH 2014-06-05T23:53:54 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 168}
```
    op hex (2)
    0000   0x0a 0xa8                                  ..
    decimal
             10  168
    datetime (2014-06-05T23:53:54)
    0000   0x76 0xb5 0x37 0x65 0x0e                   v.7e.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 31 Ian3F 2014-06-05T23:53:54 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-06-05T23:53:54)
    0000   0x76 0xb5 0x17 0x65 0x0e                   v..e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 32 CalBGForPH 2014-06-05T23:59:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2014-06-05T23:59:10)
    0000   0x4a 0xbb 0x37 0x65 0x0e                   J.7e.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 33 Ian3F 2014-06-05T23:59:10 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x15                                  ?.
    decimal
             63   21
    datetime (2014-06-05T23:59:10)
    0000   0x4a 0xbb 0x37 0x65 0x0e                   J.7e.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 34 MResultTotals 2014-06-06T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-06T00:00:00)
    0000   0x65 0x0e                                  e.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 35 Sara6E 2014-06-06T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-06T00:00:00)
    0000   0x65 0x0e                                  e.
    body (49)
    hex
    0000   0x05 0x00 0xa7 0x60 0xcd 0x05 0x00 0x00    ...`....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  167   96  205    5    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 36 CalBGForPH 2014-06-06T01:28:16 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 135}
```
    op hex (2)
    0000   0x0a 0x87                                  ..
    decimal
             10  135
    datetime (2014-06-06T01:28:16)
    0000   0x50 0x9c 0x21 0x66 0x0e                   P.!f.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 37 Ian3F 2014-06-06T01:28:16 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x10                                  ?.
    decimal
             63   16
    datetime (2014-06-06T01:28:16)
    0000   0x50 0x9c 0xe1 0x66 0x0e                   P..f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 38 CalBGForPH 2014-06-06T01:28:48 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 142}
```
    op hex (2)
    0000   0x0a 0x8e                                  ..
    decimal
             10  142
    datetime (2014-06-06T01:28:48)
    0000   0x70 0x9c 0x21 0x66 0x0e                   p.!f.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 39 Ian3F 2014-06-06T01:28:48 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x11                                  ?.
    decimal
             63   17
    datetime (2014-06-06T01:28:48)
    0000   0x70 0x9c 0xc1 0x66 0x0e                   p..f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 40 CalBGForPH 2014-06-06T08:38:10 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 40}
```
    op hex (2)
    0000   0x0a 0x28                                  .(
    decimal
             10   40
    datetime (2014-06-06T08:38:10)
    0000   0x4a 0xa6 0x28 0x66 0x0e                   J.(f.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 41 Ian3F 2014-06-06T08:38:10 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x05                                  ?.
    decimal
             63    5
    datetime (2014-06-06T08:38:10)
    0000   0x4a 0xa6 0x08 0x66 0x0e                   J..f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 42 CalBGForPH 2014-06-06T09:37:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 146}
```
    op hex (2)
    0000   0x0a 0x92                                  ..
    decimal
             10  146
    datetime (2014-06-06T09:37:18)
    0000   0x52 0xa5 0x29 0x66 0x0e                   R.)f.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 43 Ian3F 2014-06-06T09:37:18 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x12                                  ?.
    decimal
             63   18
    datetime (2014-06-06T09:37:18)
    0000   0x52 0xa5 0x49 0x66 0x0e                   R.If.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 44 CalBGForPH 2014-06-06T11:43:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2014-06-06T11:43:46)
    0000   0x6e 0xab 0x2b 0x66 0x0e                   n.+f.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 45 Ian3F 2014-06-06T11:43:46 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x17                                  ?.
    decimal
             63   23
    datetime (2014-06-06T11:43:46)
    0000   0x6e 0xab 0x2b 0x66 0x0e                   n.+f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 46 CalBGForPH 2014-06-06T12:20:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 159}
```
    op hex (2)
    0000   0x0a 0x9f                                  ..
    decimal
             10  159
    datetime (2014-06-06T12:20:30)
    0000   0x5e 0x94 0x2c 0x66 0x0e                   ^.,f.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 47 Ian3F 2014-06-06T12:20:30 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-06T12:20:30)
    0000   0x5e 0x94 0xec 0x66 0x0e                   ^..f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 48 CalBGForPH 2014-06-06T12:21:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 160}
```
    op hex (2)
    0000   0x0a 0xa0                                  ..
    decimal
             10  160
    datetime (2014-06-06T12:21:12)
    0000   0x4c 0x95 0x2c 0x66 0x0e                   L.,f.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 49 Ian3F 2014-06-06T12:21:12 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x14                                  ?.
    decimal
             63   20
    datetime (2014-06-06T12:21:12)
    0000   0x4c 0x95 0x0c 0x66 0x0e                   L..f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 50 CalBGForPH 2014-06-06T16:26:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2014-06-06T16:26:00)
    0000   0x40 0x9a 0x30 0x66 0x0e                   @.0f.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 51 Ian3F 2014-06-06T16:26:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0e                                  ?.
    decimal
             63   14
    datetime (2014-06-06T16:26:00)
    0000   0x40 0x9a 0x90 0x66 0x0e                   @..f.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 52 MResultTotals 2014-06-07T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-07T00:00:00)
    0000   0x66 0x0e                                  f.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 53 Sara6E 2014-06-07T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-07T00:00:00)
    0000   0x66 0x0e                                  f.
    body (49)
    hex
    0000   0x05 0x00 0x87 0x28 0xb9 0x08 0x00 0x00    ...(....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  135   40  185    8    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 54 CalBGForPH 2014-06-07T00:35:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2014-06-07T00:35:36)
    0000   0x64 0xa3 0x20 0x67 0x0e                   d. g.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 55 Ian3F 2014-06-07T00:35:36 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0c                                  ?.
    decimal
             63   12
    datetime (2014-06-07T00:35:36)
    0000   0x64 0xa3 0xe0 0x67 0x0e                   d..g.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 56 CalBGForPH 2014-06-07T00:36:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2014-06-07T00:36:30)
    0000   0x5e 0xa4 0x20 0x67 0x0e                   ^. g.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 57 Ian3F 2014-06-07T00:36:30 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-06-07T00:36:30)
    0000   0x5e 0xa4 0x60 0x67 0x0e                   ^.`g.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 58 CalBGForPH 2014-06-07T07:29:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2014-06-07T07:29:56)
    0000   0x78 0x9d 0x27 0x67 0x0e                   x.'g.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 59 Ian3F 2014-06-07T07:29:56 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0d                                  ?.
    decimal
             63   13
    datetime (2014-06-07T07:29:56)
    0000   0x78 0x9d 0x67 0x67 0x0e                   x.gg.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 60 CalBGForPH 2014-06-07T11:36:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 235}
```
    op hex (2)
    0000   0x0a 0xeb                                  ..
    decimal
             10  235
    datetime (2014-06-07T11:36:26)
    0000   0x5a 0xa4 0x2b 0x67 0x0e                   Z.+g.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 61 Ian3F 2014-06-07T11:36:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x1d                                  ?.
    decimal
             63   29
    datetime (2014-06-07T11:36:26)
    0000   0x5a 0xa4 0x6b 0x67 0x0e                   Z.kg.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 62 CalBGForPH 2014-06-07T13:34:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 93}
```
    op hex (2)
    0000   0x0a 0x5d                                  .]
    decimal
             10   93
    datetime (2014-06-07T13:34:52)
    0000   0x74 0xa2 0x2d 0x67 0x0e                   t.-g.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 63 Ian3F 2014-06-07T13:34:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0b                                  ?.
    decimal
             63   11
    datetime (2014-06-07T13:34:52)
    0000   0x74 0xa2 0xad 0x67 0x0e                   t..g.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 64 MResultTotals 2014-06-08T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-08T00:00:00)
    0000   0x67 0x0e                                  g.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 65 Sara6E 2014-06-08T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-08T00:00:00)
    0000   0x67 0x0e                                  g.
    body (49)
    hex
    0000   0x05 0x00 0x81 0x5d 0xeb 0x05 0x00 0x00    ...]....
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0  129   93  235    5    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 66 CalBGForPH 2014-06-08T03:14:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 63}
```
    op hex (2)
    0000   0x0a 0x3f                                  .?
    decimal
             10   63
    datetime (2014-06-08T03:14:26)
    0000   0x5a 0x8e 0x23 0x68 0x0e                   Z.#h.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 67 Ian3F 2014-06-08T03:14:26 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x07                                  ?.
    decimal
             63    7
    datetime (2014-06-08T03:14:26)
    0000   0x5a 0x8e 0xe3 0x68 0x0e                   Z..h.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 68 CalBGForPH 2014-06-08T10:58:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 64}
```
    op hex (2)
    0000   0x0a 0x40                                  .@
    decimal
             10   64
    datetime (2014-06-08T10:58:38)
    0000   0x66 0xba 0x2a 0x68 0x0e                   f.*h.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 69 Ian3F 2014-06-08T10:58:38 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x08                                  ?.
    decimal
             63    8
    datetime (2014-06-08T10:58:38)
    0000   0x66 0xba 0x0a 0x68 0x0e                   f..h.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 70 MResultTotals 2014-06-09T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-09T00:00:00)
    0000   0x68 0x0e                                  h.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

#### RECORD 71 Sara6E 2014-06-09T00:00:00 head[1], body[49] op[0x6e]

    op hex (1)
    0000   0x6e                                       n
    decimal
            110
    datetime (2014-06-09T00:00:00)
    0000   0x68 0x0e                                  h.
    body (49)
    hex
    0000   0x05 0x00 0x40 0x3f 0x40 0x02 0x00 0x00    ..@?@...
    0008   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0028   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0030   0x00                                       .
    decimal
              5    0   64   63   64    2    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0

#### RECORD 72 CalBGForPH 2014-06-09T00:27:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 154}
```
    op hex (2)
    0000   0x0a 0x9a                                  ..
    decimal
             10  154
    datetime (2014-06-09T00:27:44)
    0000   0x6c 0x9b 0x20 0x69 0x0e                   l. i.
    body (0)
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 73 Ian3F 2014-06-09T00:27:44 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x13                                  ?.
    decimal
             63   19
    datetime (2014-06-09T00:27:44)
    0000   0x6c 0x9b 0x40 0x69 0x0e                   l.@i.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 0] DAY BITS: [0, 1, 1]
#### RECORD 74 CalBGForPH 2014-06-09T06:58:00 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 82}
```
    op hex (2)
    0000   0x0a 0x52                                  .R
    decimal
             10   82
    datetime (2014-06-09T06:58:00)
    0000   0x40 0xba 0x26 0x69 0x0e                   @.&i.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 75 Ian3F 2014-06-09T06:58:00 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2014-06-09T06:58:00)
    0000   0x40 0xba 0x46 0x69 0x0e                   @.Fi.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 76 CalBGForPH 2014-06-09T06:58:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 84}
```
    op hex (2)
    0000   0x0a 0x54                                  .T
    decimal
             10   84
    datetime (2014-06-09T06:58:52)
    0000   0x74 0xba 0x26 0x69 0x0e                   t.&i.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 77 Ian3F 2014-06-09T06:58:52 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x0a                                  ?.
    decimal
             63   10
    datetime (2014-06-09T06:58:52)
    0000   0x74 0xba 0x86 0x69 0x0e                   t..i.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 78 CalBGForPH 2014-06-09T23:42:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 44}
```
    op hex (2)
    0000   0x0a 0x2c                                  .,
    decimal
             10   44
    datetime (2014-06-09T23:42:58)
    0000   0x7a 0xaa 0x37 0x69 0x0e                   z.7i.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 79 Ian3F 2014-06-09T23:42:58 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x05                                  ?.
    decimal
             63    5
    datetime (2014-06-09T23:42:58)
    0000   0x7a 0xaa 0x97 0x69 0x0e                   z..i.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 80 CalBGForPH 2014-06-09T23:43:28 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 50}
```
    op hex (2)
    0000   0x0a 0x32                                  .2
    decimal
             10   50
    datetime (2014-06-09T23:43:28)
    0000   0x5c 0xab 0x37 0x69 0x0e                   \.7i.
    body (0)
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 81 Ian3F 2014-06-09T23:43:28 head[2], body[3] op[0x3f]

    op hex (2)
    0000   0x3f 0x06                                  ?.
    decimal
             63    6
    datetime (2014-06-09T23:43:28)
    0000   0x5c 0xab 0x57 0x69 0x0e                   \.Wi.
    body (3)
    hex
    0000   0xc2 0x89 0x65                             ..e
    decimal
            194  137  101
    HOUR BITS: [1, 0, 1] DAY BITS: [0, 1, 1]
#### RECORD 82 MResultTotals 2014-06-10T00:00:00 head[5], body[3] op[0x07]

    op hex (5)
    0000   0x07 0x00 0x00 0x00 0x00                   .....
    decimal
              7    0    0    0    0
    datetime (2014-06-10T00:00:00)
    0000   0x69 0x0e                                  i.
    body (3)
    hex
    0000   0x00 0x00 0x00                             ...
    decimal
              0    0    0

`end brandon-ReadHistoryData-page-6.data: 83 records`
