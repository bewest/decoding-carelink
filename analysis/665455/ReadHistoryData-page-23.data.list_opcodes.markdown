## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-23.data
#### STOPPING DOUBLE NULLS @ 1022, found 0 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x7b 0xf9                                  {.
##### DEBUG DECIMAL
            123  249
#### RECORD 0 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 34, 'amount': 4.8, 'curve': 20},
 {'age': 204, 'amount': 1.2, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0xc0 0x22 0x14 0x30 0xcc 0x14    \..".0..
    decimal
             92    8  192   34   20   48  204   20
    datetime (unknown)

    body (0)

#### RECORD 1 Bolus 2013-04-26T13:24:23 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-04-26T13:24:23)
    0000   0x57 0x18 0x4d 0x1a 0x0d                   W.M..
    body (0)

#### RECORD 2 CalBGForPH 2013-04-26T14:47:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 95}
```
    op hex (2)
    0000   0x0a 0x5f                                  ._
    decimal
             10   95
    datetime (2013-04-26T14:47:08)
    0000   0x48 0x2f 0x2e 0x1a 0x0d                   H/...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 3 BolusWizard 2013-04-26T14:47:59 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 253,
 '_byte[7]': 240,
 'bg': 95,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.4,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': -0.3,
 'food_estimate': 2.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5f                                  [_
    decimal
             91   95
    datetime (2013-04-26T14:47:59)
    0000   0x7b 0x2f 0x0e 0x1a 0x0d                   {/...
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0xfd 0x1b 0xf0    $P.-j...
    0008   0x00 0x04 0x00 0x18 0x7d                   ....}
    decimal
             36   80   13   45  106  253   27  240
              0    4    0   24  125
    HOUR BITS: [0, 0, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 83, 'amount': 0.5, 'curve': 4},
 {'age': 117, 'amount': 4.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x53 0x04 0xc0 0x75 0x14    \..S..u.
    decimal
             92    8   20   83    4  192  117   20
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-04-26T14:47:59 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.4, 'dual_component': '??', 'programmed': 2.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x18 0x18 0x00                        ....
    decimal
              1   24   24    0
    datetime (2013-04-26T14:47:59)
    0000   0x7b 0x2f 0x4e 0x1a 0x0d                   {/N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 6 PumpSuspend 2013-04-26T16:17:16 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-26T16:17:16)
    0000   0x50 0x11 0x10 0x1a 0x0d                   P....
    body (0)

#### RECORD 7 PumpResume 2013-04-26T17:45:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-26T17:45:58)
    0000   0x7a 0x2d 0x11 0x1a 0x0d                   z-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 8 CalBGForPH 2013-04-26T20:12:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 238}
```
    op hex (2)
    0000   0x0a 0xee                                  ..
    decimal
             10  238
    datetime (2013-04-26T20:12:07)
    0000   0x47 0x0c 0x34 0x1a 0x0d                   G.4..
    body (0)

#### RECORD 9 BolusWizard 2013-04-26T20:12:52 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 25,
 '_byte[7]': 0,
 'bg': 238,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.4,
 'carb_input': 38,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 2.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xee                                  [.
    decimal
             91  238
    datetime (2013-04-26T20:12:52)
    0000   0x74 0x0c 0x14 0x1a 0x0d                   t....
    body (13)
    hex
    0000   0x26 0x50 0x0d 0x2d 0x6a 0x19 0x1d 0x00    &P.-j...
    0008   0x00 0x00 0x00 0x36 0x7d                   ...6}
    decimal
             38   80   13   45  106   25   29    0
              0    0    0   54  125

#### RECORD 10 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 72, 'amount': 2.4, 'curve': 20},
 {'age': 152, 'amount': 0.5, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x60 0x48 0x14 0x14 0x98 0x14    \.`H....
    decimal
             92    8   96   72   20   20  152   20
    datetime (unknown)

    body (0)

#### RECORD 11 Bolus 2013-04-26T20:12:52 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.4, 'dual_component': '??', 'programmed': 5.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x36 0x36 0x00                        .66.
    decimal
              1   54   54    0
    datetime (2013-04-26T20:12:52)
    0000   0x74 0x0c 0x54 0x1a 0x0d                   t.T..
    body (0)

#### RECORD 12 CalBGForPH 2013-04-26T22:33:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2013-04-26T22:33:15)
    0000   0x4f 0x21 0x36 0x1a 0x0d                   O!6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 13 MResultTotals (2013, 0, 26, 8, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 26, 8, 5, 0))
    0000   0x00 0x05 0x88 0x5a 0x0d                   ...Z.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 14 Model522ResultTotals 2013-04-27T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-27T00:00:00)
    0000   0x5a 0x0d 0x05 0x00 0x87                   Z....
    body (38)
    hex
    0000   0x45 0xee 0x0a 0x00 0x00 0x05 0x88 0x03    E.......
    0008   0x4c 0x3c 0x02 0x3c 0x28 0x00 0x86 0x02    L<.<(...
    0010   0x3c 0x28 0x01 0x8c 0x45 0x00 0xb0 0x1f    <(..E...
    0018   0x00 0x00 0x00 0x05 0x01 0x02 0x02 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             69  238   10    0    0    5  136    3
             76   60    2   60   40    0  134    2
             60   40    1  140   69    0  176   31
              0    0    0    5    1    2    2    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 15 CalBGForPH 2013-04-27T00:28:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 69}
```
    op hex (2)
    0000   0x0a 0x45                                  .E
    decimal
             10   69
    datetime (2013-04-27T00:28:56)
    0000   0x78 0x1c 0x20 0x1b 0x0d                   x. ..
    body (0)

#### RECORD 16 CalBGForPH 2013-04-27T07:23:12 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 200}
```
    op hex (2)
    0000   0x0a 0xc8                                  ..
    decimal
             10  200
    datetime (2013-04-27T07:23:12)
    0000   0x4c 0x17 0x27 0x1b 0x0d                   L.'..
    body (0)

#### RECORD 17 BolusWizard 2013-04-27T07:23:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 16,
 '_byte[7]': 0,
 'bg': 200,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.6,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc8                                  [.
    decimal
             91  200
    datetime (2013-04-27T07:23:14)
    0000   0x4e 0x17 0x07 0x1b 0x0d                   N....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x10 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x10 0x7d                   ....}
    decimal
              0   80   13   45  106   16    0    0
              0    0    0   16  125

#### RECORD 18 Bolus 2013-04-27T07:23:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.6, 'dual_component': '??', 'programmed': 1.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x10 0x10 0x00                        ....
    decimal
              1   16   16    0
    datetime (2013-04-27T07:23:14)
    0000   0x4e 0x17 0x47 0x1b 0x0d                   N.G..
    body (0)

#### RECORD 19 PumpSuspend 2013-04-27T07:36:33 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-27T07:36:33)
    0000   0x61 0x24 0x07 0x1b 0x0d                   a$...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 20 PumpResume 2013-04-27T07:43:05 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-27T07:43:05)
    0000   0x45 0x2b 0x07 0x1b 0x0d                   E+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 21 CalBGForPH 2013-04-27T08:54:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-04-27T08:54:20)
    0000   0x54 0x36 0x28 0x1b 0x0d                   T6(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 22 CalBGForPH 2013-04-27T08:55:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-04-27T08:55:39)
    0000   0x67 0x37 0x28 0x1b 0x0d                   g7(..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 23 BolusWizard 2013-04-27T08:55:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.7,
 'carb_input': 36,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 2.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-04-27T08:55:57)
    0000   0x79 0x37 0x08 0x1b 0x0d                   y7...
    body (13)
    hex
    0000   0x24 0x50 0x0d 0x2d 0x6a 0x01 0x1b 0x00    $P.-j...
    0008   0x00 0x0a 0x00 0x1b 0x7d                   ....}
    decimal
             36   80   13   45  106    1   27    0
              0   10    0   27  125
    HOUR BITS: [0, 0, 1]
#### RECORD 24 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 91, 'amount': 0.45, 'curve': 4},
 {'age': 101, 'amount': 1.15, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x12 0x5b 0x04 0x2e 0x65 0x04    \..[..e.
    decimal
             92    8   18   91    4   46  101    4
    datetime (unknown)

    body (0)

#### RECORD 25 Bolus 2013-04-27T08:55:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.7, 'dual_component': '??', 'programmed': 2.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1b 0x1b 0x00                        ....
    decimal
              1   27   27    0
    datetime (2013-04-27T08:55:57)
    0000   0x79 0x37 0x48 0x1b 0x0d                   y7H..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 26 CalBGForPH 2013-04-27T09:16:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 134}
```
    op hex (2)
    0000   0x0a 0x86                                  ..
    decimal
             10  134
    datetime (2013-04-27T09:16:42)
    0000   0x6a 0x10 0x29 0x1b 0x0d                   j.)..
    body (0)

#### RECORD 27 BolusWizard 2013-04-27T09:18:15 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 2,
 '_byte[7]': 0,
 'bg': 134,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 44,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x86                                  [.
    decimal
             91  134
    datetime (2013-04-27T09:18:15)
    0000   0x4f 0x12 0x09 0x1b 0x0d                   O....
    body (13)
    hex
    0000   0x2c 0x50 0x0d 0x2d 0x6a 0x02 0x21 0x00    ,P.-j.!.
    0008   0x00 0x22 0x00 0x21 0x7d                   .".!}
    decimal
             44   80   13   45  106    2   33    0
              0   34    0   33  125

#### RECORD 28 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 24, 'amount': 2.7, 'curve': 4},
 {'age': 114, 'amount': 0.45, 'curve': 4},
 {'age': 124, 'amount': 1.15, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x6c 0x18 0x04 0x12 0x72 0x04    \.l...r.
    0008   0x2e 0x7c 0x04                             .|.
    decimal
             92   11  108   24    4   18  114    4
             46  124    4
    datetime (unknown)

    body (0)

#### RECORD 29 Bolus 2013-04-27T09:18:16 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-04-27T09:18:16)
    0000   0x50 0x12 0x49 0x1b 0x0d                   P.I..
    body (0)

#### RECORD 30 CalBGForPH 2013-04-27T09:55:17 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 110}
```
    op hex (2)
    0000   0x0a 0x6e                                  .n
    decimal
             10  110
    datetime (2013-04-27T09:55:17)
    0000   0x51 0x37 0x29 0x1b 0x0d                   Q7)..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 31 CalBGForPH 2013-04-27T10:00:47 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-04-27T10:00:47)
    0000   0x6f 0x00 0x2a 0x1b 0x0d                   o.*..
    body (0)

#### RECORD 32 CalBGForPH 2013-04-27T11:23:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-04-27T11:23:56)
    0000   0x78 0x17 0x2b 0x1b 0x0d                   x.+..
    body (0)

#### RECORD 33 TempBasal 2013-04-27T11:45:10 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.75}
```
    op hex (2)
    0000   0x33 0x1e                                  3.
    decimal
             51   30
    datetime (2013-04-27T11:45:10)
    0000   0x4a 0x2d 0x0b 0x1b 0x0d                   J-...
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [0, 0, 1]
#### RECORD 34 TempBasalDuration 2013-04-27T11:45:10 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 150}
```
    op hex (2)
    0000   0x16 0x05                                  ..
    decimal
             22    5
    datetime (2013-04-27T11:45:10)
    0000   0x4a 0x2d 0x0b 0x1b 0x0d                   J-...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 35 CalBGForPH 2013-04-27T11:52:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 54}
```
    op hex (2)
    0000   0x0a 0x36                                  .6
    decimal
             10   54
    datetime (2013-04-27T11:52:23)
    0000   0x57 0x34 0x2b 0x1b 0x0d                   W4+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 36 TempBasal 2013-04-27T12:13:23 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.6}
```
    op hex (2)
    0000   0x33 0x18                                  3.
    decimal
             51   24
    datetime (2013-04-27T12:13:23)
    0000   0x57 0x0d 0x0c 0x1b 0x0d                   W....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0

#### RECORD 37 TempBasalDuration 2013-04-27T12:13:23 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 120}
```
    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2013-04-27T12:13:23)
    0000   0x57 0x0d 0x0c 0x1b 0x0d                   W....
    body (0)

#### RECORD 38 TempBasal 2013-04-27T12:13:34 head[2], body[1] op[0x33]
###### DECODED
```python
{'rate': 0.45}
```
    op hex (2)
    0000   0x33 0x12                                  3.
    decimal
             51   18
    datetime (2013-04-27T12:13:34)
    0000   0x62 0x0d 0x0c 0x1b 0x0d                   b....
    body (1)
    hex
    0000   0x00                                       .
    decimal
              0

#### RECORD 39 TempBasalDuration 2013-04-27T12:13:34 head[2], body[0] op[0x16]
###### DECODED
```python
{'duration (min)': 120}
```
    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2013-04-27T12:13:34)
    0000   0x62 0x0d 0x0c 0x1b 0x0d                   b....
    body (0)

#### RECORD 40 CalBGForPH 2013-04-27T12:17:23 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 92}
```
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2013-04-27T12:17:23)
    0000   0x57 0x11 0x2c 0x1b 0x0d                   W.,..
    body (0)

#### RECORD 41 CalBGForPH 2013-04-27T12:42:19 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-04-27T12:42:19)
    0000   0x53 0x2a 0x2c 0x1b 0x0d                   S*,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 42 CalBGForPH 2013-04-27T14:33:33 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 215}
```
    op hex (2)
    0000   0x0a 0xd7                                  ..
    decimal
             10  215
    datetime (2013-04-27T14:33:33)
    0000   0x61 0x21 0x2e 0x1b 0x0d                   a!...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 43 BolusWizard 2013-04-27T14:33:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 20,
 '_byte[7]': 0,
 'bg': 215,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
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
    0000   0x5b 0xd7                                  [.
    decimal
             91  215
    datetime (2013-04-27T14:33:38)
    0000   0x66 0x21 0x0e 0x1b 0x0d                   f!...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125
    HOUR BITS: [0, 0, 1]
#### RECORD 44 UnabsorbedInsulinBolus unknown head[14], body[0] op[0x5c]
###### DECODED
```python
[{'age': 63, 'amount': 3.3, 'curve': 20},
 {'age': 83, 'amount': 2.7, 'curve': 20},
 {'age': 173, 'amount': 0.45, 'curve': 20},
 {'age': 183, 'amount': 1.15, 'curve': 20}]
```
    op hex (14)
    0000   0x5c 0x0e 0x84 0x3f 0x14 0x6c 0x53 0x14    \..?.lS.
    0008   0x12 0xad 0x14 0x2e 0xb7 0x14              ......
    decimal
             92   14  132   63   20  108   83   20
             18  173   20   46  183   20
    datetime (unknown)

    body (0)

#### RECORD 45 Bolus 2013-04-27T14:33:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-04-27T14:33:38)
    0000   0x66 0x21 0x4e 0x1b 0x0d                   f!N..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 46 CalBGForPH 2013-04-27T15:05:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 123}
```
    op hex (2)
    0000   0x0a 0x7b                                  .{
    decimal
             10  123
    datetime (2013-04-27T15:05:22)
    0000   0x56 0x05 0x2f 0x1b 0x0d                   V./..
    body (0)

#### RECORD 47 CalBGForPH 2013-04-27T16:02:03 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 128}
```
    op hex (2)
    0000   0x0a 0x80                                  ..
    decimal
             10  128
    datetime (2013-04-27T16:02:03)
    0000   0x43 0x02 0x30 0x1b 0x0d                   C.0..
    body (0)

#### RECORD 48 PumpSuspend 2013-04-27T17:48:22 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-27T17:48:22)
    0000   0x56 0x30 0x11 0x1b 0x0d                   V0...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 49 PumpResume 2013-04-27T18:41:19 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-27T18:41:19)
    0000   0x53 0x29 0x12 0x1b 0x0d                   S)...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 50 CalBGForPH 2013-04-27T22:21:21 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 167}
```
    op hex (2)
    0000   0x0a 0xa7                                  ..
    decimal
             10  167
    datetime (2013-04-27T22:21:21)
    0000   0x55 0x15 0x36 0x1b 0x0d                   U.6..
    body (0)

#### RECORD 51 BolusWizard 2013-04-27T22:21:51 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 167,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 7,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa7                                  [.
    decimal
             91  167
    datetime (2013-04-27T22:21:51)
    0000   0x73 0x15 0x16 0x1b 0x0d                   s....
    body (13)
    hex
    0000   0x07 0x50 0x0d 0x2d 0x6a 0x09 0x05 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0e 0x7d                   ....}
    decimal
              7   80   13   45  106    9    5    0
              0    0    0   14  125

#### RECORD 52 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 211, 'amount': 1.45, 'curve': 20},
 {'age': 221, 'amount': 0.55, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x3a 0xd3 0x14 0x16 0xdd 0x14    \.:.....
    decimal
             92    8   58  211   20   22  221   20
    datetime (unknown)

    body (0)

#### RECORD 53 Bolus 2013-04-27T22:21:51 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.3, 'dual_component': '??', 'programmed': 1.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0d 0x0d 0x00                        ....
    decimal
              1   13   13    0
    datetime (2013-04-27T22:21:51)
    0000   0x73 0x15 0x56 0x1b 0x0d                   s.V..
    body (0)

#### RECORD 54 CalBGForPH 2013-04-27T22:37:53 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2013-04-27T22:37:53)
    0000   0x75 0x25 0x36 0x1b 0x0d                   u%6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 55 CalBGForPH 2013-04-27T22:40:52 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2013-04-27T22:40:52)
    0000   0x74 0x28 0x36 0x1b 0x0d                   t(6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 56 CalBGForPH 2013-04-27T22:42:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 185}
```
    op hex (2)
    0000   0x0a 0xb9                                  ..
    decimal
             10  185
    datetime (2013-04-27T22:42:18)
    0000   0x52 0x2a 0x36 0x1b 0x0d                   R*6..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 57 BolusWizard 2013-04-27T22:43:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 185,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 34,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 2.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xb9                                  [.
    decimal
             91  185
    datetime (2013-04-27T22:43:02)
    0000   0x42 0x2b 0x16 0x1b 0x0d                   B+...
    body (13)
    hex
    0000   0x22 0x50 0x0d 0x2d 0x6a 0x0d 0x1a 0x00    "P.-j...
    0008   0x00 0x0d 0x00 0x1a 0x7d                   ....}
    decimal
             34   80   13   45  106   13   26    0
              0   13    0   26  125
    HOUR BITS: [0, 0, 1]
#### RECORD 58 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 1.3, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x34 0x1d 0x04                   \.4..
    decimal
             92    5   52   29    4
    datetime (unknown)

    body (0)

#### RECORD 59 Bolus 2013-04-27T22:43:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-04-27T22:43:02)
    0000   0x42 0x2b 0x56 0x1b 0x0d                   B+V..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 60 MResultTotals (2013, 0, 27, 0, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 27, 0, 5, 0))
    0000   0x00 0x05 0x40 0x5b 0x0d                   ..@[.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 61 Model522ResultTotals 2013-04-28T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-28T00:00:00)
    0000   0x5b 0x0d 0x05 0x00 0x87                   [....
    body (38)
    hex
    0000   0x36 0xd7 0x12 0x00 0x00 0x05 0x40 0x03    6.....@.
    0008   0x24 0x3c 0x02 0x1c 0x28 0x00 0x79 0x02    $<..(.y.
    0010   0x1c 0x28 0x01 0x6c 0x43 0x00 0xb0 0x21    .(.lC..!
    0018   0x00 0x00 0x00 0x06 0x03 0x02 0x01 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             54  215   18    0    0    5   64    3
             36   60    2   28   40    0  121    2
             28   40    1  108   67    0  176   33
              0    0    0    6    3    2    1    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 CalBGForPH 2013-04-28T02:24:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 169}
```
    op hex (2)
    0000   0x0a 0xa9                                  ..
    decimal
             10  169
    datetime (2013-04-28T02:24:38)
    0000   0x66 0x18 0x22 0x1c 0x0d                   f."..
    body (0)

#### RECORD 63 BolusWizard 2013-04-28T02:24:41 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 9,
 '_byte[7]': 0,
 'bg': 169,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.7,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.9,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa9                                  [.
    decimal
             91  169
    datetime (2013-04-28T02:24:41)
    0000   0x69 0x18 0x02 0x1c 0x0d                   i....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x09 0x00 0x00    .P.-j...
    0008   0x00 0x02 0x00 0x07 0x7d                   ....}
    decimal
              0   80   13   45  106    9    0    0
              0    2    0    7  125

#### RECORD 64 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 220, 'amount': 1.15, 'curve': 4},
 {'age': 230, 'amount': 1.45, 'curve': 4},
 {'age': 250, 'amount': 1.3, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x2e 0xdc 0x04 0x3a 0xe6 0x04    \....:..
    0008   0x34 0xfa 0x04                             4..
    decimal
             92   11   46  220    4   58  230    4
             52  250    4
    datetime (unknown)

    body (0)

#### RECORD 65 Bolus 2013-04-28T02:24:41 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.7, 'dual_component': '??', 'programmed': 0.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x07 0x07 0x00                        ....
    decimal
              1    7    7    0
    datetime (2013-04-28T02:24:41)
    0000   0x69 0x18 0x42 0x1c 0x0d                   i.B..
    body (0)

#### RECORD 66 PumpSuspend 2013-04-28T06:29:41 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-28T06:29:41)
    0000   0x69 0x1d 0x06 0x1c 0x0d                   i....
    body (0)

#### RECORD 67 PumpResume 2013-04-28T06:43:55 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-28T06:43:55)
    0000   0x77 0x2b 0x06 0x1c 0x0d                   w+...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 68 ChangeTimeDisplay 2013-04-28T06:52:29 head[2], body[0] op[0x64]

    op hex (2)
    0000   0x64 0x00                                  d.
    decimal
            100    0
    datetime (2013-04-28T06:52:29)
    0000   0x5d 0x34 0x06 0x1c 0x0d                   ]4...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 69 ChangeTime 2013-04-28T06:52:34 head[2], body[0] op[0x17]

    op hex (2)
    0000   0x17 0x00                                  ..
    decimal
             23    0
    datetime (2013-04-28T06:52:34)
    0000   0x62 0x34 0x06 0x1c 0x0d                   b4...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 70 NewTimeSet 2013-04-28T09:52:00 head[2], body[0] op[0x18]

    op hex (2)
    0000   0x18 0x00                                  ..
    decimal
             24    0
    datetime (2013-04-28T09:52:00)
    0000   0x40 0x34 0x09 0x1c 0x0d                   @4...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 71 CalBGForPH 2013-04-28T11:52:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 193}
```
    op hex (2)
    0000   0x0a 0xc1                                  ..
    decimal
             10  193
    datetime (2013-04-28T11:52:22)
    0000   0x56 0x34 0x2b 0x1c 0x0d                   V4+..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 72 BolusWizard 2013-04-28T11:52:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 193,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc1                                  [.
    decimal
             91  193
    datetime (2013-04-28T11:52:27)
    0000   0x5b 0x34 0x0b 0x1c 0x0d                   [4...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x0f 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0    0    0   15  125
    HOUR BITS: [0, 0, 1]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 132, 'amount': 0.7, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x1c 0x84 0x14                   \....
    decimal
             92    5   28  132   20
    datetime (unknown)

    body (0)

#### RECORD 74 Bolus 2013-04-28T11:52:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.7, 'dual_component': '??', 'programmed': 1.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x11 0x11 0x00                        ....
    decimal
              1   17   17    0
    datetime (2013-04-28T11:52:28)
    0000   0x5c 0x34 0x4b 0x1c 0x0d                   \4K..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 75 CalBGForPH 2013-04-28T12:52:02 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 186}
```
    op hex (2)
    0000   0x0a 0xba                                  ..
    decimal
             10  186
    datetime (2013-04-28T12:52:02)
    0000   0x42 0x34 0x2c 0x1c 0x0d                   B4,..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 76 BolusWizard 2013-04-28T12:52:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 13,
 '_byte[7]': 0,
 'bg': 186,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.1,
 'carb_input': 41,
 'carb_ratio': 13,
 'correction_estimate': 1.3,
 'food_estimate': 3.1,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.4,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xba                                  [.
    decimal
             91  186
    datetime (2013-04-28T12:52:27)
    0000   0x5b 0x34 0x0c 0x1c 0x0d                   [4...
    body (13)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x0d 0x1f 0x00    )P.-j...
    0008   0x00 0x0e 0x00 0x1f 0x7d                   ....}
    decimal
             41   80   13   45  106   13   31    0
              0   14    0   31  125
    HOUR BITS: [0, 0, 1]
#### RECORD 77 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 68, 'amount': 1.7, 'curve': 4},
 {'age': 192, 'amount': 0.7, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x44 0x44 0x04 0x1c 0xc0 0x14    \.DD....
    decimal
             92    8   68   68    4   28  192   20
    datetime (unknown)

    body (0)

#### RECORD 78 Bolus 2013-04-28T12:52:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-04-28T12:52:27)
    0000   0x5b 0x34 0x4c 0x1c 0x0d                   [4L..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 79 CalBGForPH 2013-04-28T14:32:41 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 176}
```
    op hex (2)
    0000   0x0a 0xb0                                  ..
    decimal
             10  176
    datetime (2013-04-28T14:32:41)
    0000   0x69 0x20 0x2e 0x1c 0x0d                   i ...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 80 CalBGForPH 2013-04-28T21:40:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-04-28T21:40:08)
    0000   0x48 0x28 0x35 0x1c 0x0d                   H(5..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 81 BolusWizard 2013-04-28T21:41:17 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.6,
 'carb_input': 61,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-04-28T21:41:17)
    0000   0x51 0x29 0x15 0x1c 0x0d                   Q)...
    body (13)
    hex
    0000   0x3d 0x50 0x0d 0x2d 0x6a 0x00 0x2e 0x00    =P.-j...
    0008   0x00 0x00 0x00 0x2e 0x7d                   ....}
    decimal
             61   80   13   45  106    0   46    0
              0    0    0   46  125
    HOUR BITS: [0, 0, 1]
#### RECORD 82 Bolus 2013-04-28T21:41:17 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.6, 'dual_component': '??', 'programmed': 4.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2e 0x2e 0x00                        ....
    decimal
              1   46   46    0
    datetime (2013-04-28T21:41:17)
    0000   0x51 0x29 0x55 0x1c 0x0d                   Q)U..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 83 CalBGForPH 2013-04-28T22:16:36 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 91}
```
    op hex (2)
    0000   0x0a 0x5b                                  .[
    decimal
             10   91
    datetime (2013-04-28T22:16:36)
    0000   0x64 0x10 0x36 0x1c 0x0d                   d.6..
    body (0)

#### RECORD 84 MResultTotals (2013, 0, 28, 26, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 28, 26, 4, 0))
    0000   0x00 0x04 0x9a 0x5c 0x0d                   ...\.
    body (0)
    DAY BITS: [0, 1, 0]
#### RECORD 85 Model522ResultTotals 2013-04-29T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-04-29T00:00:00)
    0000   0x5c 0x0d 0x05 0x00 0x9a                   \....
    body (38)
    hex
    0000   0x5b 0xc1 0x06 0x00 0x00 0x04 0x9a 0x03    [.......
    0008   0x06 0x42 0x01 0x94 0x22 0x00 0x66 0x01    .B..".f.
    0010   0x94 0x22 0x01 0x34 0x4c 0x00 0x60 0x18    .".4L.`.
    0018   0x00 0x00 0x00 0x04 0x02 0x02 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             91  193    6    0    0    4  154    3
              6   66    1  148   34    0  102    1
            148   34    1   52   76    0   96   24
              0    0    0    4    2    2    0    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 86 CalBGForPH 2013-04-29T01:32:44 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 103}
```
    op hex (2)
    0000   0x0a 0x67                                  .g
    decimal
             10  103
    datetime (2013-04-29T01:32:44)
    0000   0x6c 0x20 0x21 0x1d 0x0d                   l !..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 87 PumpSuspend 2013-04-29T09:54:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-04-29T09:54:18)
    0000   0x52 0x36 0x09 0x1d 0x0d                   R6...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 88 PumpResume 2013-04-29T13:47:40 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-04-29T13:47:40)
    0000   0x68 0x2f 0x0d 0x1d 0x0d                   h/...
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 89 CalBGForPH 2013-04-29T13:52:20 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 218}
```
    op hex (2)
    0000   0x0a 0xda                                  ..
    decimal
             10  218
    datetime (2013-04-29T13:52:20)
    0000   0x54 0x34 0x2d 0x1d 0x0d                   T4-..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 90 BolusWizard 2013-04-29T13:52:27 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 20,
 '_byte[7]': 0,
 'bg': 218,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.0,
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
    0000   0x5b 0xda                                  [.
    decimal
             91  218
    datetime (2013-04-29T13:52:27)
    0000   0x5b 0x34 0x0d 0x1d 0x0d                   [4...
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x14 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x14 0x7d                   ....}
    decimal
              0   80   13   45  106   20    0    0
              0    0    0   20  125
    HOUR BITS: [0, 0, 1]
#### RECORD 91 Bolus 2013-04-29T13:52:27 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.0, 'dual_component': '??', 'programmed': 2.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x14 0x14 0x00                        ....
    decimal
              1   20   20    0
    datetime (2013-04-29T13:52:27)
    0000   0x5b 0x34 0x4d 0x1d 0x0d                   [4M..
    body (0)
    HOUR BITS: [0, 0, 1]
#### RECORD 92 LowReservoir 2013-04-29T14:22:06 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-04-29T14:22:06)
    0000   0x46 0x16 0x0e 0x1d 0x0d                   F....
    body (0)

#### RECORD 93 CalBGForPH 2013-04-29T15:30:05 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-04-29T15:30:05)
    0000   0x45 0x1e 0x2f 0x1d 0x0d                   E./..
    body (0)

#### RECORD 94 BolusWizard 2013-04-29T15:30:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 194,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xc2                                  [.
    decimal
             91  194
    datetime (2013-04-29T15:30:19)
    0000   0x53 0x1e 0x0f 0x1d 0x0d                   S....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0   11    0    4  125

#### RECORD 95 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 106, 'amount': 2.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x50 0x6a 0x04                   \.Pj.
    decimal
             92    5   80  106    4
    datetime (unknown)

    body (0)

#### RECORD 96 Bolus 2013-04-29T15:30:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-04-29T15:30:19)
    0000   0x53 0x1e 0x4f 0x1d 0x0d                   S.O..
    body (0)

`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-23.data: 97 records`
