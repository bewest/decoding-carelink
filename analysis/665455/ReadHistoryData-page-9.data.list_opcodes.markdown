## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-9.data
#### STOPPING DOUBLE NULLS @ 1011, found 11 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0x53 0x7e                                  S~
##### DEBUG DECIMAL
             83  126
#### RECORD 0 BolusWizard 2013-06-23T12:58:04 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.6,
 'carb_input': 48,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-06-23T12:58:04)
    0000   0x44 0xba 0x0c 0x17 0x0d                   D....
    body (13)
    hex
    0000   0x30 0x50 0x0d 0x2d 0x6a 0x00 0x24 0x00    0P.-j.$.
    0008   0x00 0x07 0x00 0x24 0x7d                   ...$}
    decimal
             48   80   13   45  106    0   36    0
              0    7    0   36  125
    HOUR BITS: [1, 0, 1]
#### RECORD 1 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 124, 'amount': 1.5, 'curve': 4},
 {'age': 48, 'amount': 2.45, 'curve': 20},
 {'age': 58, 'amount': 4.15, 'curve': 20}]
```
    op hex (11)
    0000   0x5c 0x0b 0x3c 0x7c 0x04 0x62 0x30 0x14    \.<|.b0.
    0008   0xa6 0x3a 0x14                             .:.
    decimal
             92   11   60  124    4   98   48   20
            166   58   20
    datetime (unknown)

    body (0)

#### RECORD 2 Bolus 2013-06-23T12:58:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.6, 'dual_component': '??', 'programmed': 3.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x24 0x24 0x00                        .$$.
    decimal
              1   36   36    0
    datetime (2013-06-23T12:58:05)
    0000   0x45 0xba 0x4c 0x17 0x0d                   E.L..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 3 CalBGForPH 2013-06-23T14:49:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 113}
```
    op hex (2)
    0000   0x0a 0x71                                  .q
    decimal
             10  113
    datetime (2013-06-23T14:49:18)
    0000   0x52 0xb1 0x2e 0x17 0x0d                   R....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 4 CalBGForPH 2013-06-23T15:30:07 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 118}
```
    op hex (2)
    0000   0x0a 0x76                                  .v
    decimal
             10  118
    datetime (2013-06-23T15:30:07)
    0000   0x47 0x9e 0x2f 0x17 0x0d                   G./..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 5 CalBGForPH 2013-06-23T19:51:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 105}
```
    op hex (2)
    0000   0x0a 0x69                                  .i
    decimal
             10  105
    datetime (2013-06-23T19:51:37)
    0000   0x65 0xb3 0x33 0x17 0x0d                   e.3..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 6 BolusWizard 2013-06-23T19:52:24 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 105,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 65,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 5.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x69                                  [i
    decimal
             91  105
    datetime (2013-06-23T19:52:24)
    0000   0x58 0xb4 0x13 0x17 0x0d                   X....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x00 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             65   80   13   45  106    0   50    0
              0    0    0   50  125
    HOUR BITS: [1, 0, 1]
#### RECORD 7 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 162, 'amount': 3.6, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x90 0xa2 0x14                   \....
    decimal
             92    5  144  162   20
    datetime (unknown)

    body (0)

#### RECORD 8 Bolus 2013-06-23T19:52:24 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-06-23T19:52:24)
    0000   0x58 0xb4 0x53 0x17 0x0d                   X.S..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 9 MResultTotals (2013, 0, 23, 4, 6, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 23, 4, 6, 0))
    0000   0x00 0x06 0x04 0x77 0x0d                   ...w.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 10 Model522ResultTotals 2013-06-24T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-24T00:00:00)
    0000   0x77 0x0d 0x05 0x10 0xab                   w....
    body (38)
    hex
    0000   0x69 0xa3 0x08 0x00 0x00 0x06 0x04 0x03    i.......
    0008   0x68 0x39 0x02 0x9c 0x2b 0x00 0x71 0x02    h9..+.q.
    0010   0x9c 0x2b 0x01 0x58 0x33 0x01 0x44 0x31    .+.X3.D1
    0018   0x00 0x00 0x00 0x04 0x02 0x02 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            105  163    8    0    0    6    4    3
            104   57    2  156   43    0  113    2
            156   43    1   88   51    1   68   49
              0    0    0    4    2    2    0    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 1, 0]
#### RECORD 11 PumpSuspend 2013-06-24T13:47:44 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-24T13:47:44)
    0000   0x6c 0xaf 0x0d 0x18 0x0d                   l....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 12 PumpResume 2013-06-24T14:09:33 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-24T14:09:33)
    0000   0x61 0x89 0x0e 0x18 0x0d                   a....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 13 CalBGForPH 2013-06-24T15:56:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 164}
```
    op hex (2)
    0000   0x0a 0xa4                                  ..
    decimal
             10  164
    datetime (2013-06-24T15:56:13)
    0000   0x4d 0xb8 0x2f 0x18 0x0d                   M./..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 14 BolusWizard 2013-06-24T15:56:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 8,
 '_byte[7]': 0,
 'bg': 164,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.0,
 'carb_input': 55,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 4.2,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xa4                                  [.
    decimal
             91  164
    datetime (2013-06-24T15:56:40)
    0000   0x68 0xb8 0x0f 0x18 0x0d                   h....
    body (13)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x08 0x2a 0x00    7P.-j.*.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             55   80   13   45  106    8   42    0
              0    0    0   50  125
    HOUR BITS: [1, 0, 1]
#### RECORD 15 Bolus 2013-06-24T15:56:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-06-24T15:56:40)
    0000   0x68 0xb8 0x4f 0x18 0x0d                   h.O..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 16 CalBGForPH 2013-06-24T18:15:26 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 268}
```
    op hex (2)
    0000   0x0a 0x0c                                  ..
    decimal
             10   12
    datetime (2013-06-24T18:15:26)
    0000   0x5a 0x8f 0x32 0x18 0x8d                   Z.2..
    body (0)
    HOUR BITS: [1, 0, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 17 BolusWizard 2013-06-24T18:15:34 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 31,
 '_byte[7]': 0,
 'bg': 268,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.4,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.5,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.7,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x0c                                  [.
    decimal
             91   12
    datetime (2013-06-24T18:15:34)
    0000   0x62 0x8f 0x12 0x18 0x0d                   b....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00    .Q.-j...
    0008   0x00 0x11 0x00 0x0e 0x7d                   ....}
    decimal
              0   81   13   45  106   31    0    0
              0   17    0   14  125
    HOUR BITS: [1, 0, 0]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 141, 'amount': 5.0, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xc8 0x8d 0x04                   \....
    decimal
             92    5  200  141    4
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-06-24T18:15:34 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-06-24T18:15:34)
    0000   0x62 0x8f 0x52 0x18 0x0d                   b.R..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 20 MResultTotals (2013, 0, 24, 12, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 24, 12, 4, 0))
    0000   0x00 0x04 0x6c 0x78 0x0d                   ..lx.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 21 Model522ResultTotals 2013-06-25T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-25T00:00:00)
    0000   0x78 0x0d 0x05 0x10 0xd8                   x....
    body (38)
    hex
    0000   0xa4 0x0c 0x02 0x00 0x00 0x04 0x6c 0x03    ......l.
    0008   0x74 0x4e 0x00 0xf8 0x16 0x00 0x37 0x00    tN....7.
    0010   0xf8 0x16 0x00 0xa8 0x44 0x00 0x50 0x20    ....D.P 
    0018   0x00 0x00 0x00 0x02 0x00 0x01 0x01 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            164   12    2    0    0    4  108    3
            116   78    0  248   22    0   55    0
            248   22    0  168   68    0   80   32
              0    0    0    2    0    1    1    0
             12    0  232    0    0    0
    YEAR BITS: [1, 1, 0, 1]
#### RECORD 22 LowReservoir 2013-06-25T01:15:00 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-06-25T01:15:00)
    0000   0x40 0x8f 0x01 0x19 0x0d                   @....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 23 PumpSuspend 2013-06-25T09:07:01 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-25T09:07:01)
    0000   0x41 0x87 0x09 0x19 0x0d                   A....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 24 PumpResume 2013-06-25T10:00:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-25T10:00:03)
    0000   0x43 0x80 0x0a 0x19 0x0d                   C....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 25 CalBGForPH 2013-06-25T10:37:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 77}
```
    op hex (2)
    0000   0x0a 0x4d                                  .M
    decimal
             10   77
    datetime (2013-06-25T10:37:37)
    0000   0x65 0xa5 0x2a 0x19 0x0d                   e.*..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 26 BolusWizard 2013-06-25T10:38:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 77,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 33,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 2.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4d                                  [M
    decimal
             91   77
    datetime (2013-06-25T10:38:05)
    0000   0x45 0xa6 0x0a 0x19 0x0d                   E....
    body (13)
    hex
    0000   0x21 0x50 0x0d 0x2d 0x6a 0xf9 0x19 0xf0    !P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
             33   80   13   45  106  249   25  240
              0    0    0   18  125
    HOUR BITS: [1, 0, 1]
#### RECORD 27 Bolus 2013-06-25T10:38:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.8, 'dual_component': '??', 'programmed': 1.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x12 0x12 0x00                        ....
    decimal
              1   18   18    0
    datetime (2013-06-25T10:38:05)
    0000   0x45 0xa6 0x4a 0x19 0x0d                   E.J..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 28 LowReservoir 2013-06-25T11:24:32 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-06-25T11:24:32)
    0000   0x60 0x98 0x0b 0x19 0x0d                   `....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 29 Rewind 2013-06-25T12:04:55 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-06-25T12:04:55)
    0000   0x77 0x84 0x0c 0x19 0x0d                   w....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 30 Prime 2013-06-25T12:05:32 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.8, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x26                   ....&
    decimal
              3    0    0    0   38
    datetime (2013-06-25T12:05:32)
    0000   0x60 0x85 0x2c 0x19 0x0d                   `.,..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 31 Prime 2013-06-25T12:05:52 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-06-25T12:05:52)
    0000   0x74 0x85 0x0c 0x19 0x0d                   t....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 32 CalBGForPH 2013-06-25T12:17:13 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 196}
```
    op hex (2)
    0000   0x0a 0xc4                                  ..
    decimal
             10  196
    datetime (2013-06-25T12:17:13)
    0000   0x4d 0x91 0x2c 0x19 0x0d                   M.,..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 33 BolusWizard 2013-06-25T12:17:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 15,
 '_byte[7]': 0,
 'bg': 196,
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
    0000   0x5b 0xc4                                  [.
    decimal
             91  196
    datetime (2013-06-25T12:17:18)
    0000   0x52 0x91 0x0c 0x19 0x0d                   R....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0f 0x00 0x00    .P.-j...
    0008   0x00 0x0b 0x00 0x04 0x7d                   ....}
    decimal
              0   80   13   45  106   15    0    0
              0   11    0    4  125
    HOUR BITS: [1, 0, 0]
#### RECORD 34 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 103, 'amount': 1.8, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x48 0x67 0x04                   \.Hg.
    decimal
             92    5   72  103    4
    datetime (unknown)

    body (0)

#### RECORD 35 Bolus 2013-06-25T12:17:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-06-25T12:17:18)
    0000   0x52 0x91 0x4c 0x19 0x0d                   R.L..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 36 CalBGForPH 2013-06-25T13:51:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 189}
```
    op hex (2)
    0000   0x0a 0xbd                                  ..
    decimal
             10  189
    datetime (2013-06-25T13:51:31)
    0000   0x5f 0xb3 0x2d 0x19 0x0d                   _.-..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 37 BolusWizard 2013-06-25T13:51:40 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 14,
 '_byte[7]': 0,
 'bg': 189,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.6,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xbd                                  [.
    decimal
             91  189
    datetime (2013-06-25T13:51:40)
    0000   0x68 0xb3 0x0d 0x19 0x0d                   h....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0e 0x00 0x00    .P.-j...
    0008   0x00 0x06 0x00 0x08 0x7d                   ....}
    decimal
              0   80   13   45  106   14    0    0
              0    6    0    8  125
    HOUR BITS: [1, 0, 1]
#### RECORD 38 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 97, 'amount': 0.5, 'curve': 4},
 {'age': 197, 'amount': 1.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x61 0x04 0x48 0xc5 0x04    \..a.H..
    decimal
             92    8   20   97    4   72  197    4
    datetime (unknown)

    body (0)

#### RECORD 39 Bolus 2013-06-25T13:51:40 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.9, 'dual_component': '??', 'programmed': 0.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x09 0x09 0x00                        ....
    decimal
              1    9    9    0
    datetime (2013-06-25T13:51:40)
    0000   0x68 0xb3 0x4d 0x19 0x0d                   h.M..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 40 CalBGForPH 2013-06-25T21:38:31 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 130}
```
    op hex (2)
    0000   0x0a 0x82                                  ..
    decimal
             10  130
    datetime (2013-06-25T21:38:31)
    0000   0x5f 0xa6 0x35 0x19 0x0d                   _.5..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 41 BolusWizard 2013-06-25T21:38:35 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 1,
 '_byte[7]': 0,
 'bg': 130,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.1,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x82                                  [.
    decimal
             91  130
    datetime (2013-06-25T21:38:35)
    0000   0x63 0xa6 0x15 0x19 0x0d                   c....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x01 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x01 0x7d                   ....}
    decimal
              0   80   13   45  106    1    0    0
              0    0    0    1  125
    HOUR BITS: [1, 0, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 218, 'amount': 0.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x24 0xda 0x14                   \.$..
    decimal
             92    5   36  218   20
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-06-25T21:38:35 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.2, 'dual_component': '??', 'programmed': 0.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x02 0x02 0x00                        ....
    decimal
              1    2    2    0
    datetime (2013-06-25T21:38:35)
    0000   0x63 0xa6 0x55 0x19 0x0d                   c.U..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 44 CalBGForPH 2013-06-25T22:01:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 85}
```
    op hex (2)
    0000   0x0a 0x55                                  .U
    decimal
             10   85
    datetime (2013-06-25T22:01:56)
    0000   0x78 0x81 0x36 0x19 0x0d                   x.6..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 45 BolusWizard 2013-06-25T22:03:13 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 85,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.4,
 'carb_input': 51,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 3.9,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x55                                  [U
    decimal
             91   85
    datetime (2013-06-25T22:03:13)
    0000   0x4d 0x83 0x16 0x19 0x0d                   M....
    body (13)
    hex
    0000   0x33 0x50 0x0d 0x2d 0x6a 0xfb 0x27 0xf0    3P.-j.'.
    0008   0x00 0x02 0x00 0x22 0x7d                   ..."}
    decimal
             51   80   13   45  106  251   39  240
              0    2    0   34  125
    HOUR BITS: [1, 0, 0]
#### RECORD 46 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 29, 'amount': 0.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x08 0x1d 0x04                   \....
    decimal
             92    5    8   29    4
    datetime (unknown)

    body (0)

#### RECORD 47 Bolus 2013-06-25T22:03:14 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.4, 'dual_component': '??', 'programmed': 3.4, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x22 0x22 0x00                        ."".
    decimal
              1   34   34    0
    datetime (2013-06-25T22:03:14)
    0000   0x4e 0x83 0x56 0x19 0x0d                   N.V..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 48 CalBGForPH 2013-06-25T22:44:39 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 109}
```
    op hex (2)
    0000   0x0a 0x6d                                  .m
    decimal
             10  109
    datetime (2013-06-25T22:44:39)
    0000   0x67 0xac 0x36 0x19 0x0d                   g.6..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 49 BolusWizard 2013-06-25T22:44:57 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 109,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.6,
 'carb_input': 9,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 0.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 3.3,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6d                                  [m
    decimal
             91  109
    datetime (2013-06-25T22:44:57)
    0000   0x79 0xac 0x16 0x19 0x0d                   y....
    body (13)
    hex
    0000   0x09 0x50 0x0d 0x2d 0x6a 0x00 0x06 0x00    .P.-j...
    0008   0x00 0x21 0x00 0x06 0x7d                   .!..}
    decimal
              9   80   13   45  106    0    6    0
              0   33    0    6  125
    HOUR BITS: [1, 0, 1]
#### RECORD 50 UnabsorbedInsulinBolus unknown head[11], body[0] op[0x5c]
###### DECODED
```python
[{'age': 40, 'amount': 2.25, 'curve': 4},
 {'age': 50, 'amount': 1.15, 'curve': 4},
 {'age': 70, 'amount': 0.2, 'curve': 4}]
```
    op hex (11)
    0000   0x5c 0x0b 0x5a 0x28 0x04 0x2e 0x32 0x04    \.Z(..2.
    0008   0x08 0x46 0x04                             .F.
    decimal
             92   11   90   40    4   46   50    4
              8   70    4
    datetime (unknown)

    body (0)

#### RECORD 51 Bolus 2013-06-25T22:44:57 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.6, 'dual_component': '??', 'programmed': 0.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x06 0x06 0x00                        ....
    decimal
              1    6    6    0
    datetime (2013-06-25T22:44:57)
    0000   0x79 0xac 0x56 0x19 0x0d                   y.V..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 52 MResultTotals (2013, 0, 25, 4, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 25, 4, 4, 0))
    0000   0x00 0x04 0x84 0x79 0x0d                   ...y.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 53 Model522ResultTotals 2013-06-26T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-26T00:00:00)
    0000   0x79 0x0d 0x05 0x00 0x83                   y....
    body (38)
    hex
    0000   0x4d 0xc4 0x06 0x00 0x00 0x04 0x84 0x03    M.......
    0008   0x5c 0x4a 0x01 0x28 0x1a 0x00 0x5d 0x01    \J.(..].
    0010   0x28 0x1a 0x00 0xe8 0x4e 0x00 0x40 0x16    (...N.@.
    0018   0x00 0x00 0x00 0x06 0x03 0x03 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             77  196    6    0    0    4  132    3
             92   74    1   40   26    0   93    1
             40   26    0  232   78    0   64   22
              0    0    0    6    3    3    0    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 54 CalBGForPH 2013-06-26T10:20:58 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 209}
```
    op hex (2)
    0000   0x0a 0xd1                                  ..
    decimal
             10  209
    datetime (2013-06-26T10:20:58)
    0000   0x7a 0x94 0x2a 0x1a 0x0d                   z.*..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 55 BolusWizard 2013-06-26T10:21:02 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 18,
 '_byte[7]': 0,
 'bg': 209,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.2,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xd1                                  [.
    decimal
             91  209
    datetime (2013-06-26T10:21:02)
    0000   0x42 0x95 0x0a 0x1a 0x0d                   B....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x12 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x12 0x7d                   ....}
    decimal
              0   80   13   45  106   18    0    0
              0    0    0   18  125
    HOUR BITS: [1, 0, 0]
#### RECORD 56 Bolus 2013-06-26T10:21:02 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.9, 'dual_component': '??', 'programmed': 1.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x13 0x13 0x00                        ....
    decimal
              1   19   19    0
    datetime (2013-06-26T10:21:02)
    0000   0x42 0x95 0x4a 0x1a 0x0d                   B.J..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 57 PumpSuspend 2013-06-26T11:55:40 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-26T11:55:40)
    0000   0x68 0xb7 0x0b 0x1a 0x0d                   h....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 58 PumpResume 2013-06-26T12:24:13 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-26T12:24:13)
    0000   0x4d 0x98 0x0c 0x1a 0x0d                   M....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 59 CalBGForPH 2013-06-26T19:30:38 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 107}
```
    op hex (2)
    0000   0x0a 0x6b                                  .k
    decimal
             10  107
    datetime (2013-06-26T19:30:38)
    0000   0x66 0x9e 0x33 0x1a 0x0d                   f.3..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 60 BolusWizard 2013-06-26T19:31:10 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 107,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.3,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6b                                  [k
    decimal
             91  107
    datetime (2013-06-26T19:31:10)
    0000   0x4a 0x9f 0x13 0x1a 0x0d                   J....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0x00 0x21 0x00    +P.-j.!.
    0008   0x00 0x00 0x00 0x21 0x7d                   ...!}
    decimal
             43   80   13   45  106    0   33    0
              0    0    0   33  125
    HOUR BITS: [1, 0, 0]
#### RECORD 61 Bolus 2013-06-26T19:31:10 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.3, 'dual_component': '??', 'programmed': 3.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x21 0x21 0x00                        .!!.
    decimal
              1   33   33    0
    datetime (2013-06-26T19:31:10)
    0000   0x4a 0x9f 0x53 0x1a 0x0d                   J.S..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 62 MResultTotals (2013, 0, 26, 0, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 26, 0, 4, 0))
    0000   0x00 0x04 0x40 0x7a 0x0d                   ..@z.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 63 Model522ResultTotals 2013-06-27T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-27T00:00:00)
    0000   0x7a 0x0d 0x05 0x00 0x9e                   z....
    body (38)
    hex
    0000   0x6b 0xd1 0x02 0x00 0x00 0x04 0x40 0x03    k.....@.
    0008   0x70 0x51 0x00 0xd0 0x13 0x00 0x2b 0x00    pQ....+.
    0010   0xd0 0x13 0x00 0x84 0x3f 0x00 0x4c 0x25    ....?.L%
    0018   0x00 0x00 0x00 0x02 0x01 0x01 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
            107  209    2    0    0    4   64    3
            112   81    0  208   19    0   43    0
            208   19    0  132   63    0   76   37
              0    0    0    2    1    1    0    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 0, 1]
#### RECORD 64 PumpSuspend 2013-06-27T11:20:20 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-27T11:20:20)
    0000   0x54 0x94 0x0b 0x1b 0x0d                   T....
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 65 PumpResume 2013-06-27T11:35:58 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-27T11:35:58)
    0000   0x7a 0xa3 0x0b 0x1b 0x0d                   z....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 66 CalBGForPH 2013-06-27T13:07:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 86}
```
    op hex (2)
    0000   0x0a 0x56                                  .V
    decimal
             10   86
    datetime (2013-06-27T13:07:30)
    0000   0x5e 0x87 0x2d 0x1b 0x0d                   ^.-..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 67 BolusWizard 2013-06-27T13:08:21 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 251,
 '_byte[7]': 240,
 'bg': 86,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.1,
 'carb_input': 60,
 'carb_ratio': 13,
 'correction_estimate': -0.5,
 'food_estimate': 4.6,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x56                                  [V
    decimal
             91   86
    datetime (2013-06-27T13:08:21)
    0000   0x55 0x88 0x0d 0x1b 0x0d                   U....
    body (13)
    hex
    0000   0x3c 0x50 0x0d 0x2d 0x6a 0xfb 0x2e 0xf0    <P.-j...
    0008   0x00 0x00 0x00 0x29 0x7d                   ...)}
    decimal
             60   80   13   45  106  251   46  240
              0    0    0   41  125
    HOUR BITS: [1, 0, 0]
#### RECORD 68 Bolus 2013-06-27T13:08:21 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.1, 'dual_component': '??', 'programmed': 4.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x29 0x29 0x00                        .)).
    decimal
              1   41   41    0
    datetime (2013-06-27T13:08:21)
    0000   0x55 0x88 0x4d 0x1b 0x0d                   U.M..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 69 CalBGForPH 2013-06-27T15:03:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 210}
```
    op hex (2)
    0000   0x0a 0xd2                                  ..
    decimal
             10  210
    datetime (2013-06-27T15:03:04)
    0000   0x44 0x83 0x2f 0x1b 0x0d                   D./..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 70 CalBGForPH 2013-06-27T16:29:06 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2013-06-27T16:29:06)
    0000   0x46 0x9d 0x30 0x1b 0x0d                   F.0..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 71 BolusWizard 2013-06-27T16:29:08 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.5,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.5,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2013-06-27T16:29:08)
    0000   0x48 0x9d 0x10 0x1b 0x0d                   H....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x0a 0x00 0x00    .P.-j...
    0008   0x00 0x05 0x00 0x05 0x7d                   ....}
    decimal
              0   80   13   45  106   10    0    0
              0    5    0    5  125
    HOUR BITS: [1, 0, 0]
#### RECORD 72 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 205, 'amount': 4.1, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0xa4 0xcd 0x04                   \....
    decimal
             92    5  164  205    4
    datetime (unknown)

    body (0)

#### RECORD 73 Bolus 2013-06-27T16:29:08 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.5, 'dual_component': '??', 'programmed': 0.5, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x05 0x05 0x00                        ....
    decimal
              1    5    5    0
    datetime (2013-06-27T16:29:08)
    0000   0x48 0x9d 0x50 0x1b 0x0d                   H.P..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 74 CalBGForPH 2013-06-27T18:01:35 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 116}
```
    op hex (2)
    0000   0x0a 0x74                                  .t
    decimal
             10  116
    datetime (2013-06-27T18:01:35)
    0000   0x63 0x81 0x32 0x1b 0x0d                   c.2..
    body (0)
    HOUR BITS: [1, 0, 0]
#### RECORD 75 CalBGForPH 2013-06-27T18:33:57 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 94}
```
    op hex (2)
    0000   0x0a 0x5e                                  .^
    decimal
             10   94
    datetime (2013-06-27T18:33:57)
    0000   0x79 0xa1 0x32 0x1b 0x0d                   y.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 76 CalBGForPH 2013-06-27T18:34:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 90}
```
    op hex (2)
    0000   0x0a 0x5a                                  .Z
    decimal
             10   90
    datetime (2013-06-27T18:34:08)
    0000   0x48 0xa2 0x32 0x1b 0x0d                   H.2..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 77 BolusWizard 2013-06-27T18:34:18 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 90,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.9,
 'carb_input': 43,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 3.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x5a                                  [Z
    decimal
             91   90
    datetime (2013-06-27T18:34:18)
    0000   0x52 0xa2 0x12 0x1b 0x0d                   R....
    body (13)
    hex
    0000   0x2b 0x50 0x0d 0x2d 0x6a 0xfc 0x21 0xf0    +P.-j.!.
    0008   0x00 0x02 0x00 0x1d 0x7d                   ....}
    decimal
             43   80   13   45  106  252   33  240
              0    2    0   29  125
    HOUR BITS: [1, 0, 1]
#### RECORD 78 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 130, 'amount': 0.5, 'curve': 4},
 {'age': 74, 'amount': 4.1, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x14 0x82 0x04 0xa4 0x4a 0x14    \.....J.
    decimal
             92    8   20  130    4  164   74   20
    datetime (unknown)

    body (0)

#### RECORD 79 Bolus 2013-06-27T18:34:18 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-06-27T18:34:18)
    0000   0x52 0xa2 0x52 0x1b 0x0d                   R.R..
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 80 MResultTotals (2013, 0, 27, 4, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 27, 4, 4, 0))
    0000   0x00 0x04 0xa4 0x7b 0x0d                   ...{.
    body (0)
    DAY BITS: [0, 1, 1]
#### RECORD 81 Model522ResultTotals 2013-06-28T00:00:00 head[1], body[38] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-06-28T00:00:00)
    0000   0x7b 0x0d 0x05 0x00 0x80                   {....
    body (38)
    hex
    0000   0x56 0xd2 0x06 0x00 0x00 0x04 0xa4 0x03    V.......
    0008   0x78 0x4b 0x01 0x2c 0x19 0x00 0x67 0x01    xK.,..g.
    0010   0x2c 0x19 0x01 0x18 0x5d 0x00 0x14 0x07    ,...]...
    0018   0x00 0x00 0x00 0x03 0x02 0x01 0x00 0x00    ........
    0020   0x0c 0x00 0xe8 0x00 0x00 0x00              ......
    decimal
             86  210    6    0    0    4  164    3
            120   75    1   44   25    0  103    1
             44   25    1   24   93    0   20    7
              0    0    0    3    2    1    0    0
             12    0  232    0    0    0
    YEAR BITS: [1, 0, 0, 0]
#### RECORD 82 PumpSuspend 2013-06-28T11:37:59 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-06-28T11:37:59)
    0000   0x7b 0xa5 0x0b 0x1c 0x0d                   {....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 83 PumpResume 2013-06-28T11:58:37 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-06-28T11:58:37)
    0000   0x65 0xba 0x0b 0x1c 0x0d                   e....
    body (0)
    HOUR BITS: [1, 0, 1]
#### RECORD 84 CalBGForPH 2013-06-28T13:33:43 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 104}
```
    op hex (2)
    0000   0x0a 0x68                                  .h
    decimal
             10  104
    datetime (2013-06-28T13:33:43)
    0000   0x6b 0xa1 0x2d 0x1c 0x0d                   k.-..
    body (0)
    HOUR BITS: [1, 0, 1]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-9.data: 85 records`
