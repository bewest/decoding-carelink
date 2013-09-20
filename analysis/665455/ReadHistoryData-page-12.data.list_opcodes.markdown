## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-12.data
#### STOPPING DOUBLE NULLS @ 1014, found 8 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xda 0x44                                  .D
##### DEBUG DECIMAL
            218   68
#### RECORD 0 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 0.3, 'curve': 4},
 {'age': 82, 'amount': 0.1, 'curve': 4},
 {'age': 16, 'amount': 1.9, 'curve': 20},
 {'age': 106, 'amount': 3.4, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0c 0x48 0x04 0x04 0x52 0x04    \..H..R.
    0008   0x4c 0x10 0x14 0x88 0x6a 0x14              L...j.
    decimal
             92   14   12   72    4    4   82    4
             76   16   20  136  106   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-06-10T20:36:39 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-06-10T20:36:39)
    0000   0x67 0xa4 0x54 0x0a 0x0d                   g.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 2 BolusWizard 2013-06-10T20:40:53 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 41,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2013-06-10T20:40:53)
    0000   0x75 0xa8 0x14 0x0a 0x0d                   u....
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x00 0x1f 0x00    )P.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             41   80   13   45  106    0   31    0
              0    0    0   31  125
    HOUR BITS: [1, 0, 1]
#### RECORD 3 UnabsorbedInsulinBolus unknown head[17], body[0] op[0x5c]
###### DECODED
```python
[{'age': 6, 'amount': 0.9, 'curve': 4},
 {'age': 76, 'amount': 0.3, 'curve': 4},
 {'age': 86, 'amount': 0.1, 'curve': 4},
 {'age': 20, 'amount': 1.9, 'curve': 20},
 {'age': 110, 'amount': 3.4, 'curve': 20}]
```
    op hex (17)
    0000   0x5c 0x11 0x24 0x06 0x04 0x0c 0x4c 0x04    \.$...L.
    0008   0x04 0x56 0x04 0x4c 0x14 0x14 0x88 0x6e    .V.L...n
    0010   0x14                                       .
    decimal
             92   17   36    6    4   12   76    4
              4   86    4   76   20   20  136  110
             20
    datetime (unknown)

    body (0)

#### RECORD 4 Bolus 2013-06-10T20:40:54 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-06-10T20:40:54)
    0000   0x76 0xa8 0x54 0x0a 0x0d                   v.T..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 5 CalBGForPH 2013-06-10T22:30:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 136}
```
    op hex (2)
    0000   0x0a 0x88                                  ..
    decimal
             10  136
    datetime (2013-06-10T22:30:20)
    0000   0x54 0x9e 0x36 0x0a 0x0d                   T.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 6 MResultTotals (2013, 0, 10, 26, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 10, 26, 4, 0))
    0000   0x00 0x04 0xfa 0x6a 0x0d                   ...j.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 7 Model522ResultTotals 2013-06-11T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-11T00:00:00)
    0000   0x6a 0x0d                                  j.
    body (41)
    hex
    0000   0x05 0x10 0x9a 0x6f 0x07 0x07 0x00 0x00    ...o....
    0008   0x04 0xfa 0x03 0x76 0x46 0x01 0x84 0x1e    ...vF...
    0010   0x00 0x48 0x01 0x84 0x1e 0x00 0xd8 0x38    .H.....8
    0018   0x00 0xac 0x2c 0x00 0x00 0x00 0x05 0x03    ..,.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  154  111    7    7    0    0
              4  250    3  118   70    1  132   30
              0   72    1  132   30    0  216   56
              0  172   44    0    0    0    5    3
              2    0    0   12    0  232    0    0
              0

#### RECORD 8 CalBGForPH 2013-06-11T17:59:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 98}
```
    op hex (2)
    0000   0x0a 0x62                                  .b
    decimal
             10   98
    datetime (2013-06-11T17:59:42)
    0000   0x6a 0xbb 0x31 0x0b 0x0d                   j.1..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 BolusWizard 2013-06-11T17:59:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 98,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 46,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 3.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x62                                  [b
    decimal
             91   98
    datetime (2013-06-11T17:59:59)
    0000   0x7b 0xbb 0x11 0x0b 0x0d                   {....
    body (13)
    hex
    0000   0x2e 0x50 0x0d 0x2d 0x6a 0xfe 0x23 0xf0    .P.-j.#.
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
             46   80   13   45  106  254   35  240
              0    0    0   33  125
    HOUR BITS: [1, 0, 1]
#### RECORD 10 Bolus 2013-06-11T17:59:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-06-11T17:59:59)
    0000   0x7b 0xbb 0x51 0x0b 0x0d                   {.Q..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 11 CalBGForPH 2013-06-11T19:04:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-06-11T19:04:41)
    0000   0x69 0x84 0x33 0x0b 0x0d                   i.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 12 BolusWizard 2013-06-11T19:05:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
 'carb_input': 27,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-06-11T19:05:11)
    0000   0x4b 0x85 0x13 0x0b 0x0d                   K....
    body (13)
    hex
    0000   0x1b 0x50 0x0d 0x2d 0x6a 0x00 0x14 0x00    .P.-j...
    0008   0x00 0x1a 0x00 0x14 0x7d                   ....}
    decimal
             27   80   13   45  106    0   20    0
              0   26    0   20  125
    HOUR BITS: [1, 0, 0]
#### RECORD 13 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 71, 'amount': 3.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x84 0x47 0x04                   \..G.
    decimal
             92    5  132   71    4
    datetime (unknown)

    body (0)

#### RECORD 14 Bolus 2013-06-11T19:05:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-06-11T19:05:11)
    0000   0x4b 0x85 0x53 0x0b 0x0d                   K.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 15 CalBGForPH 2013-06-11T20:32:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-06-11T20:32:02)
    0000   0x42 0xa0 0x34 0x0b 0x0d                   B.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 16 MResultTotals (2013, 0, 11, 24, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 11, 24, 4, 0))
    0000   0x00 0x04 0x58 0x6b 0x0d                   ..Xk.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 17 Model522ResultTotals 2013-06-12T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-12T00:00:00)
    0000   0x6b 0x0d                                  k.
    body (41)
    hex
    0000   0x05 0x00 0x68 0x62 0x6d 0x03 0x00 0x00    ..hbm...
    0008   0x04 0x58 0x03 0x84 0x51 0x00 0xd4 0x13    .X..Q...
    0010   0x00 0x49 0x00 0xd4 0x13 0x00 0xd4 0x64    .I.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x02 0x02    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  104   98  109    3    0    0
              4   88    3  132   81    0  212   19
              0   73    0  212   19    0  212  100
              0    0    0    0    0    0    2    2
              0    0    0   12    0  232    0    0
              0

#### RECORD 18 LowReservoir 2013-06-12T00:18:45 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-06-12T00:18:45)
    0000   0x6d 0x92 0x00 0x0c 0x0d                   m....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 19 LowReservoir 2013-06-12T11:30:01 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-06-12T11:30:01)
    0000   0x41 0x9e 0x0b 0x0c 0x0d                   A....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 PumpSuspend 2013-06-12T13:34:11 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-12T13:34:11)
    0000   0x4b 0xa2 0x0d 0x0c 0x0d                   K....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 21 PumpResume 2013-06-12T13:58:52 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-12T13:58:52)
    0000   0x74 0xba 0x0d 0x0c 0x0d                   t....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 22 CalBGForPH 2013-06-12T15:33:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 96}
```
    op hex (2)
    0000   0x0a 0x60                                  .`
    decimal
             10   96
    datetime (2013-06-12T15:33:11)
    0000   0x4b 0xa1 0x2f 0x0c 0x0d                   K./..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 23 BolusWizard 2013-06-12T15:33:23 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 254,
 '_byte[7]': 240,
 'bg': 96,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': -0.2,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x60                                  [`
    decimal
             91   96
    datetime (2013-06-12T15:33:23)
    0000   0x57 0xa1 0x0f 0x0c 0x0d                   W....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0xfe 0x21 0xf0    ,P.-j.!.
    0008   0x00 0x00 0x00 0x1f 0x7d                   ....}
    decimal
             44   80   13   45  106  254   33  240
              0    0    0   31  125
    HOUR BITS: [1, 0, 1]
#### RECORD 24 Bolus 2013-06-12T15:33:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-06-12T15:33:23)
    0000   0x57 0xa1 0x4f 0x0c 0x0d                   W.O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 25 CalBGForPH 2013-06-12T17:10:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2013-06-12T17:10:47)
    0000   0x6f 0x8a 0x31 0x0c 0x0d                   o.1..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 26 PumpSuspend 2013-06-12T21:16:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-12T21:16:20)
    0000   0x54 0x90 0x15 0x0c 0x0d                   T....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 27 PumpResume 2013-06-12T21:16:25 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-12T21:16:25)
    0000   0x59 0x90 0x15 0x0c 0x0d                   Y....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 28 Rewind 2013-06-12T21:16:31 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-06-12T21:16:31)
    0000   0x5f 0x90 0x15 0x0c 0x0d                   _....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 Prime 2013-06-12T21:18:37 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 2.5, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x19                   .....
    decimal
              3    0    0    0   25
    datetime (2013-06-12T21:18:37)
    0000   0x65 0x92 0x35 0x0c 0x0d                   e.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 Prime 2013-06-12T21:18:55 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-06-12T21:18:55)
    0000   0x77 0x92 0x15 0x0c 0x0d                   w....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 CalBGForPH 2013-06-12T21:21:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 288}
```
    op hex (2)
    0000   0x0a 0x20                                  . 
    decimal
             10   32
    datetime (2013-06-12T21:21:37)
    0000   0x65 0x95 0x35 0x0c 0x8d                   e.5..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 32 BolusWizard 2013-06-12T21:21:49 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 36,
 '_byte[7]': 0,
 'bg': 288,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x20                                  [ 
    decimal
             91   32
    datetime (2013-06-12T21:21:49)
    0000   0x71 0x95 0x15 0x0c 0x0d                   q....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x24 0x00 0x00    .Q.-j$..
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
              0   81   13   45  106   36    0    0
              0    0    0   36  125
    HOUR BITS: [1, 0, 0]
#### RECORD 33 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 2.15, 'curve': 20},
 {'age': 101, 'amount': 0.95, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x56 0x5b 0x14 0x26 0x65 0x14    \.V[.&e.
    decimal
             92    8   86   91   20   38  101   20
    datetime (unknown)

    body (0)

#### RECORD 34 Bolus 2013-06-12T21:21:49 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-06-12T21:21:49)
    0000   0x71 0x95 0x55 0x0c 0x0d                   q.U..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 35 CalBGForPH 2013-06-12T22:24:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 205}
```
    op hex (2)
    0000   0x0a 0xcd                                  ..
    decimal
             10  205
    datetime (2013-06-12T22:24:04)
    0000   0x44 0x98 0x36 0x0c 0x0d                   D.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 BolusWizard 2013-06-12T22:25:01 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 17,
 '_byte[7]': 0,
 'bg': 205,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.8,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xcd                                  [.
    decimal
             91  205
    datetime (2013-06-12T22:25:01)
    0000   0x41 0x99 0x16 0x0c 0x0d                   A....
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x11 0x2e 0x00    =P.-j...
    0008   0x00 0x1c 0x00 0x2e 0x7d                   ....}
    decimal
             61   80   13   45  106   17   46    0
              0   28    0   46  125
    HOUR BITS: [1, 0, 0]
#### RECORD 37 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 61, 'amount': 0.35, 'curve': 4},
 {'age': 71, 'amount': 3.25, 'curve': 4},
 {'age': 155, 'amount': 2.15, 'curve': 20},
 {'age': 165, 'amount': 0.95, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x0e 0x3d 0x04 0x82 0x47 0x04    \..=..G.
    0008   0x56 0x9b 0x14 0x26 0xa5 0x14              V..&..
    decimal
             92   14   14   61    4  130   71    4
             86  155   20   38  165   20
    datetime (unknown)

    body (0)

#### RECORD 38 Bolus 2013-06-12T22:25:01 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-06-12T22:25:01)
    0000   0x41 0x99 0x56 0x0c 0x0d                   A.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 39 MResultTotals (2013, 0, 12, 20, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 12, 20, 5, 0))
    0000   0x00 0x05 0x34 0x6c 0x0d                   ..4l.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 40 Model522ResultTotals 2013-06-13T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-13T00:00:00)
    0000   0x6c 0x0d                                  l.
    body (41)
    hex
    0000   0x05 0x10 0xc3 0x60 0x20 0x04 0x00 0x00    ...` ...
    0008   0x05 0x34 0x03 0x70 0x42 0x01 0xc4 0x22    .4.pB.."
    0010   0x00 0x69 0x01 0xc4 0x22 0x01 0x34 0x44    .i..".4D
    0018   0x00 0x90 0x20 0x00 0x00 0x00 0x03 0x02    .. .....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  195   96   32    4    0    0
              5   52    3  112   66    1  196   34
              0  105    1  196   34    1   52   68
              0  144   32    0    0    0    3    2
              1    0    0   12    0  232    0    0
              0

#### RECORD 41 CalBGForPH 2013-06-13T07:43:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 323}
```
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2013-06-13T07:43:38)
    0000   0x66 0xab 0x27 0x0d 0x8d                   f.'..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 42 BolusWizard 2013-06-13T07:43:42 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 44,
 '_byte[7]': 0,
 'bg': 323,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x43                                  [C
    decimal
             91   67
    datetime (2013-06-13T07:43:42)
    0000   0x6a 0xab 0x07 0x0d 0x0d                   j....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2c 0x00 0x00    .Q.-j,..
    0008   0x00 0x00 0x00 0x2c 0x7d                   ...,}
    decimal
              0   81   13   45  106   44    0    0
              0    0    0   44  125
    HOUR BITS: [1, 0, 1]
#### RECORD 43 Bolus 2013-06-13T07:43:42 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.4, 'dual_component': '??', 'programmed': 4.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2c 0x2c 0x00                        .,,.
    decimal
              1   44   44    0
    datetime (2013-06-13T07:43:42)
    0000   0x6a 0xab 0x47 0x0d 0x0d                   j.G..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 44 PumpSuspend 2013-06-13T13:32:19 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-13T13:32:19)
    0000   0x53 0xa0 0x0d 0x0d 0x0d                   S....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 45 PumpResume 2013-06-13T13:44:02 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-13T13:44:02)
    0000   0x42 0xac 0x0d 0x0d 0x0d                   B....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 46 CalBGForPH 2013-06-13T14:30:46 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 143}
```
    op hex (2)
    0000   0x0a 0x8f                                  ..
    decimal
             10  143
    datetime (2013-06-13T14:30:46)
    0000   0x6e 0x9e 0x2e 0x0d 0x0d                   n....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 47 BolusWizard 2013-06-13T14:31:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 4,
 '_byte[7]': 0,
 'bg': 143,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.5,
 'carb_input': 41,
 'carb_ratio': 13,
 'correction_estimate': 0.4,
 'food_estimate': 3.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x8f                                  [.
    decimal
             91  143
    datetime (2013-06-13T14:31:08)
    0000   0x48 0x9f 0x0e 0x0d 0x0d                   H....
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x04 0x1f 0x00    )P.-j...
    0008   0x00 0x00 0x00 0x23 0x7d                   ...#}
    decimal
             41   80   13   45  106    4   31    0
              0    0    0   35  125
    HOUR BITS: [1, 0, 0]
#### RECORD 48 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 151, 'amount': 3.95, 'curve': 20},
 {'age': 161, 'amount': 0.45, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x9e 0x97 0x14 0x12 0xa1 0x14    \.......
    decimal
             92    8  158  151   20   18  161   20
    datetime (unknown)

    body (0)

#### RECORD 49 Bolus 2013-06-13T14:31:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.5, 'dual_component': '??', 'programmed': 3.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x23 0x23 0x00                        .##.
    decimal
              1   35   35    0
    datetime (2013-06-13T14:31:08)
    0000   0x48 0x9f 0x4e 0x0d 0x0d                   H.N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 50 Battery 2013-06-13T16:37:43 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-06-13T16:37:43)
    0000   0x6b 0xa5 0x10 0x0d 0x0d                   k....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 51 Battery 2013-06-13T16:38:02 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-06-13T16:38:02)
    0000   0x42 0xa6 0x10 0x0d 0x0d                   B....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 52 CalBGForPH 2013-06-13T16:38:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-06-13T16:38:18)
    0000   0x52 0xa6 0x30 0x0d 0x0d                   R.0..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 53 CalBGForPH 2013-06-13T18:04:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 180}
```
    op hex (2)
    0000   0x0a 0xb4                                  ..
    decimal
             10  180
    datetime (2013-06-13T18:04:05)
    0000   0x45 0x84 0x32 0x0d 0x0d                   E.2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 54 BolusWizard 2013-06-13T18:04:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 12,
 '_byte[7]': 0,
 'bg': 180,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.9,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb4                                  [.
    decimal
             91  180
    datetime (2013-06-13T18:04:10)
    0000   0x4a 0x84 0x12 0x0d 0x0d                   J....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0c 0x00 0x00    .P.-j...
    0008   0x00 0x03 0x00 0x09 0x7d                   ....}
    decimal
              0   80   13   45  106   12    0    0
              0    3    0    9  125
    HOUR BITS: [1, 0, 0]
#### RECORD 55 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 220, 'amount': 3.5, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x8c 0xdc 0x04                   \....
    decimal
             92    5  140  220    4
    datetime (unknown)

    body (0)

#### RECORD 56 Bolus 2013-06-13T18:04:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-06-13T18:04:10)
    0000   0x4a 0x84 0x52 0x0d 0x0d                   J.R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 57 CalBGForPH 2013-06-13T19:03:11 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-06-13T19:03:11)
    0000   0x4b 0x83 0x33 0x0d 0x0d                   K.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 58 BolusWizard 2013-06-13T19:03:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.9,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-06-13T19:03:41)
    0000   0x69 0x83 0x13 0x0d 0x0d                   i....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0x00 0x27 0x00    3P.-j.'.
    0008   0x00 0x09 0x00 0x27 0x7d                   ...'}
    decimal
             51   80   13   45  106    0   39    0
              0    9    0   39  125
    HOUR BITS: [1, 0, 0]
#### RECORD 59 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 1.0, 'curve': 4},
 {'age': 23, 'amount': 3.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x28 0x3b 0x04 0x8c 0x17 0x14    \.(;....
    decimal
             92    8   40   59    4  140   23   20
    datetime (unknown)

    body (0)

#### RECORD 60 Bolus 2013-06-13T19:03:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.9, 'dual_component': '??', 'programmed': 3.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x27 0x27 0x00                        .''.
    decimal
              1   39   39    0
    datetime (2013-06-13T19:03:41)
    0000   0x69 0x83 0x53 0x0d 0x0d                   i.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 61 CalBGForPH 2013-06-13T21:06:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 61}
```
    op hex (2)
    0000   0x0a 0x3d                                  .=
    decimal
             10   61
    datetime (2013-06-13T21:06:33)
    0000   0x61 0x86 0x35 0x0d 0x0d                   a.5..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 MResultTotals (2013, 0, 13, 24, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 13, 24, 5, 0))
    0000   0x00 0x05 0x78 0x6d 0x0d                   ..xm.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 63 Model522ResultTotals 2013-06-14T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-14T00:00:00)
    0000   0x6d 0x0d                                  m.
    body (41)
    hex
    0000   0x05 0x10 0x9c 0x3d 0x43 0x06 0x00 0x00    ...=C...
    0008   0x05 0x78 0x03 0x78 0x3f 0x02 0x00 0x25    .x.x?..%
    0010   0x00 0x5c 0x02 0x00 0x25 0x01 0x18 0x37    .\..%..7
    0018   0x00 0xe8 0x2d 0x00 0x00 0x00 0x04 0x01    ..-.....
    0020   0x02 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  156   61   67    6    0    0
              5  120    3  120   63    2    0   37
              0   92    2    0   37    1   24   55
              0  232   45    0    0    0    4    1
              2    1    0   12    0  232    0    0
              0

#### RECORD 64 CalBGForPH 2013-06-14T08:43:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 171}
```
    op hex (2)
    0000   0x0a 0xab                                  ..
    decimal
             10  171
    datetime (2013-06-14T08:43:56)
    0000   0x78 0xab 0x28 0x0e 0x0d                   x.(..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 65 BolusWizard 2013-06-14T08:43:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 171,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.0,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xab                                  [.
    decimal
             91  171
    datetime (2013-06-14T08:43:58)
    0000   0x7a 0xab 0x08 0x0e 0x0d                   z....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0a 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    0    0   10  125
    HOUR BITS: [1, 0, 1]
#### RECORD 66 Bolus 2013-06-14T08:43:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.0, 'dual_component': '??', 'programmed': 1.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0a 0x0a 0x00                        ....
    decimal
              1   10   10    0
    datetime (2013-06-14T08:43:58)
    0000   0x7a 0xab 0x48 0x0e 0x0d                   z.H..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 67 PumpSuspend 2013-06-14T13:30:16 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-14T13:30:16)
    0000   0x50 0x9e 0x0d 0x0e 0x0d                   P....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 68 PumpResume 2013-06-14T13:43:24 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-14T13:43:24)
    0000   0x58 0xab 0x0d 0x0e 0x0d                   X....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 69 CalBGForPH 2013-06-14T14:16:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-06-14T14:16:30)
    0000   0x5e 0x90 0x2e 0x0e 0x0d                   ^....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 70 BolusWizard 2013-06-14T14:16:44 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 52,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x59                                  [Y
    decimal
             91   89
    datetime (2013-06-14T14:16:44)
    0000   0x6c 0x90 0x0e 0x0e 0x0d                   l....
    body (13)
    hex
    0000   0x34 0x50 0x0d 0x2d 0x6a 0xfc 0x28 0xf0    4P.-j.(.
    0008   0x00 0x00 0x00 0x24 0x7d                   ...$}
    decimal
             52   80   13   45  106  252   40  240
              0    0    0   36  125
    HOUR BITS: [1, 0, 0]
#### RECORD 71 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 76, 'amount': 0.95, 'curve': 20},
 {'age': 86, 'amount': 0.05, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x26 0x4c 0x14 0x02 0x56 0x14    \.&L..V.
    decimal
             92    8   38   76   20    2   86   20
    datetime (unknown)

    body (0)

#### RECORD 72 Bolus 2013-06-14T14:16:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-06-14T14:16:45)
    0000   0x6d 0x90 0x4e 0x0e 0x0d                   m.N..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 73 CalBGForPH 2013-06-14T18:47:14 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 199}
```
    op hex (2)
    0000   0x0a 0xc7                                  ..
    decimal
             10  199
    datetime (2013-06-14T18:47:14)
    0000   0x4e 0xaf 0x32 0x0e 0x0d                   N.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 74 CalBGForPH 2013-06-14T18:47:25 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 334}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2013-06-14T18:47:25)
    0000   0x59 0xaf 0x32 0x0e 0x8d                   Y.2..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 75 CalBGForPH 2013-06-14T18:47:55 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 334}
```
    op hex (2)
    0000   0x0a 0x4e                                  .N
    decimal
             10   78
    datetime (2013-06-14T18:47:55)
    0000   0x77 0xaf 0x32 0x0e 0x8d                   w.2..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 76 BolusWizard 2013-06-14T18:48:11 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 46,
 '_byte[7]': 0,
 'bg': 334,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4e                                  [N
    decimal
             91   78
    datetime (2013-06-14T18:48:11)
    0000   0x4b 0xb0 0x12 0x0e 0x0d                   K....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x2e 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
              0   81   13   45  106   46    0    0
              0    0    0   46  125
    HOUR BITS: [1, 0, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 18, 'amount': 3.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0x12 0x14                   \....
    decimal
             92    5  144   18   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2013-06-14T18:48:11 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-06-14T18:48:11)
    0000   0x4b 0xb0 0x52 0x0e 0x0d                   K.R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 79 CalBGForPH 2013-06-14T20:27:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-06-14T20:27:40)
    0000   0x68 0x9b 0x34 0x0e 0x0d                   h.4..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 80 CalBGForPH 2013-06-14T20:41:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-06-14T20:41:08)
    0000   0x48 0xa9 0x34 0x0e 0x0d                   H.4..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 81 MResultTotals (2013, 0, 14, 12, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 14, 12, 4, 0))
    0000   0x00 0x04 0xec 0x6e 0x0d                   ...n.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 82 Model522ResultTotals 2013-06-15T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-15T00:00:00)
    0000   0x6e 0x0d                                  n.
    body (41)
    hex
    0000   0x05 0x10 0xc0 0x59 0x4e 0x07 0x00 0x00    ...YN...
    0008   0x04 0xec 0x03 0x7c 0x47 0x01 0x70 0x1d    ...|G.p.
    0010   0x00 0x34 0x01 0x70 0x1d 0x00 0x90 0x27    .4.p...'
    0018   0x00 0xe0 0x3d 0x00 0x00 0x00 0x03 0x01    ..=.....
    0020   0x02 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  192   89   78    7    0    0
              4  236    3  124   71    1  112   29
              0   52    1  112   29    0  144   39
              0  224   61    0    0    0    3    1
              2    0    0   12    0  232    0    0
              0

#### RECORD 83 PumpSuspend 2013-06-15T15:14:45 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-15T15:14:45)
    0000   0x6d 0x8e 0x0f 0x0f 0x0d                   m....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 84 PumpResume 2013-06-15T15:30:31 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-15T15:30:31)
    0000   0x5f 0x9e 0x0f 0x0f 0x0d                   _....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 85 CalBGForPH 2013-06-15T16:39:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 202}
```
    op hex (2)
    0000   0x0a 0xca                                  ..
    decimal
             10  202
    datetime (2013-06-15T16:39:36)
    0000   0x64 0xa7 0x30 0x0f 0x0d                   d.0..
    body (0)
    HOUR BITS: [1, 0, 1]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-12.data: 86 records`
