## START analysis/bewest-pump/fall-2013//ReadHistoryData-page-7.data
#### STOPPING DOUBLE NULLS @ 1020, found 2 nulls
reading more to debug 0x00
    0000   0x00 0x00                                  ..
              0    0
##### DEBUG HEX
    0000   0xe9 0xbe                                  ..
##### DEBUG DECIMAL
            233  190
#### RECORD 0 CalBGForPH 2013-07-02T16:32:34 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 234}
```
    op hex (2)
    0000   0x0a 0xea                                  ..
    decimal
             10  234
    datetime (2013-07-02T16:32:34)
    0000   0x62 0xe0 0x30 0x02 0x0d                   b.0..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 1 CalBGForPH 2013-07-02T17:11:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 194}
```
    op hex (2)
    0000   0x0a 0xc2                                  ..
    decimal
             10  194
    datetime (2013-07-02T17:11:08)
    0000   0x48 0xcb 0x31 0x02 0x0d                   H.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 2 CalBGForPH 2013-07-02T21:44:22 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 115}
```
    op hex (2)
    0000   0x0a 0x73                                  .s
    decimal
             10  115
    datetime (2013-07-02T21:44:22)
    0000   0x56 0xec 0x35 0x02 0x0d                   V.5..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 3 BolusWizard 2013-07-02T21:44:58 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 115,
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
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2013-07-02T21:44:58)
    0000   0x7a 0xec 0x15 0x02 0x0d                   z....
    body (13)
    hex
    0000   0x41 0x50 0x0d 0x2d 0x6a 0x00 0x32 0x00    AP.-j.2.
    0008   0x00 0x00 0x00 0x32 0x7d                   ...2}
    decimal
             65   80   13   45  106    0   50    0
              0    0    0   50  125
    HOUR BITS: [1, 1, 1]
#### RECORD 4 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 114, 'amount': 0.1, 'curve': 21}]
```
    op hex (5)
    0000   0x5c 0x05 0x04 0x72 0x15                   \..r.
    decimal
             92    5    4  114   21
    datetime (unknown)

    body (0)

#### RECORD 5 Bolus 2013-07-02T21:44:58 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.0, 'dual_component': '??', 'programmed': 5.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x32 0x32 0x00                        .22.
    decimal
              1   50   50    0
    datetime (2013-07-02T21:44:58)
    0000   0x7a 0xec 0x55 0x02 0x0d                   z.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 6 CalBGForPH 2013-07-02T22:40:42 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 108}
```
    op hex (2)
    0000   0x0a 0x6c                                  .l
    decimal
             10  108
    datetime (2013-07-02T22:40:42)
    0000   0x6a 0xe8 0x36 0x02 0x0d                   j.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 7 MResultTotals (2013, 0, 2, 0, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 2, 0, 5, 0))
    0000   0x00 0x05 0x40 0x62 0x8d                   ..@b.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 8 Model522ResultTotals 2013-07-03T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-03T00:00:00)
    0000   0x62 0x8d                                  b.
    body (41)
    hex
    0000   0x05 0x00 0xa3 0x6c 0xea 0x06 0x00 0x00    ...l....
    0008   0x05 0x40 0x03 0x74 0x42 0x01 0xcc 0x22    .@.tB.."
    0010   0x00 0x8d 0x01 0xcc 0x22 0x01 0xb0 0x5e    ...."..^
    0018   0x00 0x1c 0x06 0x00 0x00 0x00 0x02 0x01    ........
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  163  108  234    6    0    0
              5   64    3  116   66    1  204   34
              0  141    1  204   34    1  176   94
              0   28    6    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 9 LowReservoir 2013-07-03T11:21:49 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-03T11:21:49)
    0000   0x71 0xd5 0x0b 0x03 0x0d                   q....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 10 PumpSuspend 2013-07-03T14:27:03 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-03T14:27:03)
    0000   0x43 0xdb 0x0e 0x03 0x0d                   C....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 11 PumpResume 2013-07-03T14:42:48 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-03T14:42:48)
    0000   0x70 0xea 0x0e 0x03 0x0d                   p....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 12 CalBGForPH 2013-07-03T17:37:56 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 255}
```
    op hex (2)
    0000   0x0a 0xff                                  ..
    decimal
             10  255
    datetime (2013-07-03T17:37:56)
    0000   0x78 0xe5 0x31 0x03 0x0d                   x.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 13 BolusWizard 2013-07-03T17:38:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 28,
 '_byte[7]': 0,
 'bg': 255,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
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
    0000   0x5b 0xff                                  [.
    decimal
             91  255
    datetime (2013-07-03T17:38:03)
    0000   0x43 0xe6 0x11 0x03 0x0d                   C....
    body (13)
    hex
    0000   0x00 0x50 0x0d 0x2d 0x6a 0x1c 0x00 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x1c 0x7d                   ....}
    decimal
              0   80   13   45  106   28    0    0
              0    0    0   28  125
    HOUR BITS: [1, 1, 1]
#### RECORD 14 Bolus 2013-07-03T17:38:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-07-03T17:38:03)
    0000   0x43 0xe6 0x51 0x03 0x0d                   C.Q..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 15 LowReservoir 2013-07-03T18:41:03 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-07-03T18:41:03)
    0000   0x43 0xe9 0x12 0x03 0x0d                   C....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 16 CalBGForPH 2013-07-03T22:49:08 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 106}
```
    op hex (2)
    0000   0x0a 0x6a                                  .j
    decimal
             10  106
    datetime (2013-07-03T22:49:08)
    0000   0x48 0xf1 0x36 0x03 0x0d                   H.6..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 17 BolusWizard 2013-07-03T22:49:20 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 106,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.7,
 'carb_input': 49,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 3.7,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x6a                                  [j
    decimal
             91  106
    datetime (2013-07-03T22:49:20)
    0000   0x54 0xf1 0x16 0x03 0x0d                   T....
    body (13)
    hex
    0000   0x31 0x50 0x0d 0x2d 0x6a 0x00 0x25 0x00    1P.-j.%.
    0008   0x00 0x00 0x00 0x25 0x7d                   ...%}
    decimal
             49   80   13   45  106    0   37    0
              0    0    0   37  125
    HOUR BITS: [1, 1, 1]
#### RECORD 18 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 59, 'amount': 2.9, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x74 0x3b 0x14                   \.t;.
    decimal
             92    5  116   59   20
    datetime (unknown)

    body (0)

#### RECORD 19 Bolus 2013-07-03T22:49:20 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.7, 'dual_component': '??', 'programmed': 3.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x25 0x25 0x00                        .%%.
    decimal
              1   37   37    0
    datetime (2013-07-03T22:49:20)
    0000   0x54 0xf1 0x56 0x03 0x0d                   T.V..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 20 MResultTotals (2013, 0, 3, 2, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 3, 2, 4, 0))
    0000   0x00 0x04 0x82 0x63 0x8d                   ...c.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 21 Model522ResultTotals 2013-07-04T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-04T00:00:00)
    0000   0x63 0x8d                                  c.
    body (41)
    hex
    0000   0x05 0x00 0xb5 0x6a 0xff 0x02 0x00 0x00    ...j....
    0008   0x04 0x82 0x03 0x7a 0x4d 0x01 0x08 0x17    ...zM...
    0010   0x00 0x31 0x01 0x08 0x17 0x00 0x94 0x38    .1.....8
    0018   0x00 0x74 0x2c 0x00 0x00 0x00 0x02 0x01    .t,.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  181  106  255    2    0    0
              4  130    3  122   77    1    8   23
              0   49    1    8   23    0  148   56
              0  116   44    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 22 PumpSuspend 2013-07-04T17:31:18 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-04T17:31:18)
    0000   0x52 0xdf 0x11 0x04 0x0d                   R....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 23 PumpResume 2013-07-04T17:52:14 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-04T17:52:14)
    0000   0x4e 0xf4 0x11 0x04 0x0d                   N....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 24 Rewind 2013-07-04T17:52:18 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-04T17:52:18)
    0000   0x52 0xf4 0x11 0x04 0x0d                   R....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 25 Prime 2013-07-04T17:53:36 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 3.4, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x22                   ...."
    decimal
              3    0    0    0   34
    datetime (2013-07-04T17:53:36)
    0000   0x64 0xf5 0x31 0x04 0x0d                   d.1..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 26 Prime 2013-07-04T17:54:03 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 0.5, 'fixed': 0.5, 'type': 'fixed'}
```
    op hex (5)
    0000   0x03 0x00 0x05 0x00 0x05                   .....
    decimal
              3    0    5    0    5
    datetime (2013-07-04T17:54:03)
    0000   0x43 0xf6 0x11 0x04 0x0d                   C....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 27 BolusWizard 2013-07-04T19:03:29 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 0,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.6,
 'carb_input': 35,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 2.6,
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
    datetime (2013-07-04T19:03:29)
    0000   0x5d 0xc3 0x13 0x04 0x0d                   ]....
    body (13)
    hex
    0000   0x23 0x50 0x0d 0x2d 0x6a 0x00 0x1a 0x00    #P.-j...
    0008   0x00 0x00 0x00 0x1a 0x7d                   ....}
    decimal
             35   80   13   45  106    0   26    0
              0    0    0   26  125
    HOUR BITS: [1, 1, 0]
#### RECORD 28 Bolus 2013-07-04T19:03:29 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.6, 'dual_component': '??', 'programmed': 2.6, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1a 0x1a 0x00                        ....
    decimal
              1   26   26    0
    datetime (2013-07-04T19:03:29)
    0000   0x5d 0xc3 0x53 0x04 0x0d                   ].S..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 29 CalBGForPH 2013-07-04T21:04:04 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 308}
```
    op hex (2)
    0000   0x0a 0x34                                  .4
    decimal
             10   52
    datetime (2013-07-04T21:04:04)
    0000   0x44 0xc4 0x35 0x04 0x8d                   D.5..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 30 BolusWizard 2013-07-04T21:04:14 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 40,
 '_byte[7]': 0,
 'bg': 308,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 2.8,
 'carb_input': 0,
 'carb_ratio': 13,
 'correction_estimate': 0.8,
 'food_estimate': 0.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 1.2,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x34                                  [4
    decimal
             91   52
    datetime (2013-07-04T21:04:14)
    0000   0x4e 0xc4 0x15 0x04 0x0d                   N....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x28 0x00 0x00    .Q.-j(..
    0008   0x00 0x0c 0x00 0x1c 0x7d                   ....}
    decimal
              0   81   13   45  106   40    0    0
              0   12    0   28  125
    HOUR BITS: [1, 1, 0]
#### RECORD 31 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 120, 'amount': 1.8, 'curve': 4},
 {'age': 130, 'amount': 0.8, 'curve': 4}]
```
    op hex (8)
    0000   0x5c 0x08 0x48 0x78 0x04 0x20 0x82 0x04    \.Hx. ..
    decimal
             92    8   72  120    4   32  130    4
    datetime (unknown)

    body (0)

#### RECORD 32 Bolus 2013-07-04T21:04:15 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 2.9, 'dual_component': '??', 'programmed': 2.9, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1d 0x1d 0x00                        ....
    decimal
              1   29   29    0
    datetime (2013-07-04T21:04:15)
    0000   0x4f 0xc4 0x55 0x04 0x0d                   O.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 33 MResultTotals (2013, 0, 4, 16, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 4, 16, 4, 0))
    0000   0x00 0x04 0x50 0x64 0x8d                   ..Pd.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 34 Model522ResultTotals 2013-07-05T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-05T00:00:00)
    0000   0x64 0x8d                                  d.
    body (41)
    hex
    0000   0x05 0x15 0x34 0x34 0x34 0x01 0x00 0x00    ..444...
    0008   0x04 0x50 0x03 0x74 0x50 0x00 0xdc 0x14    .P.tP...
    0010   0x00 0x23 0x00 0xdc 0x14 0x00 0x68 0x2f    .#....h/
    0018   0x00 0x74 0x35 0x00 0x00 0x00 0x02 0x01    .t5.....
    0020   0x01 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21   52   52   52    1    0    0
              4   80    3  116   80    0  220   20
              0   35    0  220   20    0  104   47
              0  116   53    0    0    0    2    1
              1    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 35 PumpSuspend 2013-07-05T15:34:05 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-05T15:34:05)
    0000   0x45 0xe2 0x0f 0x05 0x0d                   E....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 36 PumpResume 2013-07-05T16:45:08 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-05T16:45:08)
    0000   0x48 0xed 0x10 0x05 0x0d                   H....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 37 CalBGForPH 2013-07-05T17:02:30 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 89}
```
    op hex (2)
    0000   0x0a 0x59                                  .Y
    decimal
             10   89
    datetime (2013-07-05T17:02:30)
    0000   0x5e 0xc2 0x31 0x05 0x0d                   ^.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 38 BolusWizard 2013-07-05T17:02:38 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 252,
 '_byte[7]': 240,
 'bg': 89,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 1.2,
 'carb_input': 22,
 'carb_ratio': 13,
 'correction_estimate': -0.4,
 'food_estimate': 1.6,
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
    datetime (2013-07-05T17:02:38)
    0000   0x66 0xc2 0x11 0x05 0x0d                   f....
    body (13)
    hex
    0000   0x16 0x50 0x0d 0x2d 0x6a 0xfc 0x10 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x0c 0x7d                   ....}
    decimal
             22   80   13   45  106  252   16  240
              0    0    0   12  125
    HOUR BITS: [1, 1, 0]
#### RECORD 39 Bolus 2013-07-05T17:02:38 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 1.2, 'dual_component': '??', 'programmed': 1.2, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x0c 0x0c 0x00                        ....
    decimal
              1   12   12    0
    datetime (2013-07-05T17:02:38)
    0000   0x66 0xc2 0x51 0x05 0x0d                   f.Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 40 CalBGForPH 2013-07-05T20:35:37 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 174}
```
    op hex (2)
    0000   0x0a 0xae                                  ..
    decimal
             10  174
    datetime (2013-07-05T20:35:37)
    0000   0x65 0xe3 0x34 0x05 0x0d                   e.4..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 41 BolusWizard 2013-07-05T20:36:05 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 10,
 '_byte[7]': 0,
 'bg': 174,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.3,
 'carb_input': 45,
 'carb_ratio': 13,
 'correction_estimate': 1.0,
 'food_estimate': 3.4,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.1,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0xae                                  [.
    decimal
             91  174
    datetime (2013-07-05T20:36:05)
    0000   0x45 0xe4 0x14 0x05 0x0d                   E....
    body (13)
    hex
    0000   0x2d 0x50 0x0d 0x2d 0x6a 0x0a 0x22 0x00    -P.-j.".
    0008   0x00 0x01 0x00 0x2b 0x7d                   ...+}
    decimal
             45   80   13   45  106   10   34    0
              0    1    0   43  125
    HOUR BITS: [1, 1, 1]
#### RECORD 42 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 222, 'amount': 1.2, 'curve': 4}]
```
    op hex (5)
    0000   0x5c 0x05 0x30 0xde 0x04                   \.0..
    decimal
             92    5   48  222    4
    datetime (unknown)

    body (0)

#### RECORD 43 Bolus 2013-07-05T20:36:05 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.3, 'dual_component': '??', 'programmed': 4.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x2b 0x2b 0x00                        .++.
    decimal
              1   43   43    0
    datetime (2013-07-05T20:36:05)
    0000   0x45 0xe4 0x54 0x05 0x0d                   E.T..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 44 MResultTotals (2013, 0, 5, 18, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 5, 18, 4, 0))
    0000   0x00 0x04 0x32 0x65 0x8d                   ..2e.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 45 Model522ResultTotals 2013-07-06T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-06T00:00:00)
    0000   0x65 0x8d                                  e.
    body (41)
    hex
    0000   0x05 0x00 0x84 0x59 0xae 0x02 0x00 0x00    ...Y....
    0008   0x04 0x32 0x03 0x56 0x50 0x00 0xdc 0x14    .2.VP...
    0010   0x00 0x43 0x00 0xdc 0x14 0x00 0xb8 0x54    .C.....T
    0018   0x00 0x24 0x10 0x00 0x00 0x00 0x02 0x01    .$......
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  132   89  174    2    0    0
              4   50    3   86   80    0  220   20
              0   67    0  220   20    0  184   84
              0   36   16    0    0    0    2    1
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 46 PumpSuspend 2013-07-06T18:05:17 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-06T18:05:17)
    0000   0x51 0xc5 0x12 0x06 0x0d                   Q....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 47 PumpResume 2013-07-06T18:31:03 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-06T18:31:03)
    0000   0x43 0xdf 0x12 0x06 0x0d                   C....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 48 CalBGForPH 2013-07-06T21:20:18 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 120}
```
    op hex (2)
    0000   0x0a 0x78                                  .x
    decimal
             10  120
    datetime (2013-07-06T21:20:18)
    0000   0x52 0xd4 0x35 0x06 0x0d                   R.5..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 49 BolusWizard 2013-07-06T21:20:25 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 0,
 '_byte[7]': 0,
 'bg': 120,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 4.0,
 'carb_input': 53,
 'carb_ratio': 13,
 'correction_estimate': 0.0,
 'food_estimate': 4.0,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x78                                  [x
    decimal
             91  120
    datetime (2013-07-06T21:20:25)
    0000   0x59 0xd4 0x15 0x06 0x0d                   Y....
    body (13)
    hex
    0000   0x35 0x50 0x0d 0x2d 0x6a 0x00 0x28 0x00    5P.-j.(.
    0008   0x00 0x00 0x00 0x28 0x7d                   ...(}
    decimal
             53   80   13   45  106    0   40    0
              0    0    0   40  125
    HOUR BITS: [1, 1, 0]
#### RECORD 50 Bolus 2013-07-06T21:20:25 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 4.0, 'dual_component': '??', 'programmed': 4.0, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x28 0x28 0x00                        .((.
    decimal
              1   40   40    0
    datetime (2013-07-06T21:20:25)
    0000   0x59 0xd4 0x55 0x06 0x0d                   Y.U..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 51 MResultTotals (2013, 0, 6, 20, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 6, 20, 4, 0))
    0000   0x00 0x04 0x14 0x66 0x8d                   ...f.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 52 Model522ResultTotals 2013-07-07T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-07T00:00:00)
    0000   0x66 0x8d                                  f.
    body (41)
    hex
    0000   0x05 0x00 0x78 0x78 0x78 0x01 0x00 0x00    ..xxx...
    0008   0x04 0x14 0x03 0x74 0x55 0x00 0xa0 0x0f    ...tU...
    0010   0x00 0x35 0x00 0xa0 0x0f 0x00 0xa0 0x64    .5.....d
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x01 0x01    ........
    0020   0x00 0x00 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5    0  120  120  120    1    0    0
              4   20    3  116   85    0  160   15
              0   53    0  160   15    0  160  100
              0    0    0    0    0    0    1    1
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 53 LowBattery 2013-07-07T10:01:00 head[2], body[0] op[0x19]

    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2013-07-07T10:01:00)
    0000   0x40 0xc1 0x0a 0x07 0x0d                   @....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 54 NoDelivery 2013-07-07T20:01:00 head[4], body[0] op[0x06]

    op hex (4)
    0000   0x06 0x05 0x1d 0x9f                        ....
    decimal
              6    5   29  159
    datetime (2013-07-07T20:01:00)
    0000   0x40 0xc1 0x74 0x07 0x0d                   @.t..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 55 ClearAlarm 2013-07-07T21:31:19 head[2], body[0] op[0x0c]

    op hex (2)
    0000   0x0c 0x05                                  ..
    decimal
             12    5
    datetime (2013-07-07T21:31:19)
    0000   0x53 0xdf 0x15 0x07 0x0d                   S....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 56 Battery 2013-07-07T21:31:40 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x00                                  ..
    decimal
             26    0
    datetime (2013-07-07T21:31:40)
    0000   0x68 0xdf 0x15 0x07 0x0d                   h....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 57 Battery 2013-07-07T21:32:01 head[2], body[0] op[0x1a]

    op hex (2)
    0000   0x1a 0x01                                  ..
    decimal
             26    1
    datetime (2013-07-07T21:32:01)
    0000   0x41 0xe0 0x15 0x07 0x0d                   A....
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 58 CalBGForPH 2013-07-07T22:09:45 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 262}
```
    op hex (2)
    0000   0x0a 0x06                                  ..
    decimal
             10    6
    datetime (2013-07-07T22:09:45)
    0000   0x6d 0xc9 0x36 0x07 0x8d                   m.6..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 59 BolusWizard 2013-07-07T22:10:28 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 262,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 8.3,
 'carb_input': 70,
 'carb_ratio': 13,
 'correction_estimate': 1.4,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x06                                  [.
    decimal
             91    6
    datetime (2013-07-07T22:10:28)
    0000   0x5c 0xca 0x16 0x07 0x0d                   \....
    body (13)
    hex
    0000   0x46 0x51 0x0d 0x2d 0x6a 0x1e 0x35 0x00    FQ.-j.5.
    0008   0x00 0x00 0x00 0x53 0x7d                   ...S}
    decimal
             70   81   13   45  106   30   53    0
              0    0    0   83  125
    HOUR BITS: [1, 1, 0]
#### RECORD 60 Bolus 2013-07-07T22:10:28 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 8.3, 'dual_component': '??', 'programmed': 8.3, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x53 0x53 0x00                        .SS.
    decimal
              1   83   83    0
    datetime (2013-07-07T22:10:28)
    0000   0x5c 0xca 0x56 0x07 0x0d                   \.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 61 MResultTotals (2013, 0, 7, 22, 4, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 7, 22, 4, 0))
    0000   0x00 0x04 0x96 0x67 0x8d                   ...g.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 62 Model522ResultTotals 2013-07-08T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-08T00:00:00)
    0000   0x67 0x8d                                  g.
    body (41)
    hex
    0000   0x05 0x15 0x06 0x06 0x06 0x01 0x00 0x00    ........
    0008   0x04 0x96 0x03 0x4a 0x48 0x01 0x4c 0x1c    ...JH.L.
    0010   0x00 0x46 0x01 0x4c 0x1c 0x00 0xd4 0x40    .F.L...@
    0018   0x00 0x78 0x24 0x00 0x00 0x00 0x01 0x00    .x$.....
    0020   0x00 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   21    6    6    6    1    0    0
              4  150    3   74   72    1   76   28
              0   70    1   76   28    0  212   64
              0  120   36    0    0    0    1    0
              0    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 63 CalBGForPH 2013-07-08T17:16:40 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 74}
```
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2013-07-08T17:16:40)
    0000   0x68 0xd0 0x31 0x08 0x0d                   h.1..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 64 BolusWizard 2013-07-08T17:17:03 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 249,
 '_byte[7]': 240,
 'bg': 74,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 0.8,
 'carb_input': 20,
 'carb_ratio': 13,
 'correction_estimate': -0.7,
 'food_estimate': 1.5,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 0.0,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x4a                                  [J
    decimal
             91   74
    datetime (2013-07-08T17:17:03)
    0000   0x43 0xd1 0x11 0x08 0x0d                   C....
    body (13)
    hex
    0000   0x14 0x50 0x0d 0x2d 0x6a 0xf9 0x0f 0xf0    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d                   ....}
    decimal
             20   80   13   45  106  249   15  240
              0    0    0    8  125
    HOUR BITS: [1, 1, 0]
#### RECORD 65 LowReservoir 2013-07-08T17:17:19 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 20.0}
```
    op hex (2)
    0000   0x34 0xc8                                  4.
    decimal
             52  200
    datetime (2013-07-08T17:17:19)
    0000   0x53 0xd1 0x11 0x08 0x0d                   S....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 66 Bolus 2013-07-08T17:17:03 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 0.8, 'dual_component': '??', 'programmed': 0.8, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x08 0x08 0x00                        ....
    decimal
              1    8    8    0
    datetime (2013-07-08T17:17:03)
    0000   0x43 0xd1 0x51 0x08 0x0d                   C.Q..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 67 CalBGForPH 2013-07-08T21:47:15 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 264}
```
    op hex (2)
    0000   0x0a 0x08                                  ..
    decimal
             10    8
    datetime (2013-07-08T21:47:15)
    0000   0x4f 0xef 0x35 0x08 0x8d                   O.5..
    body (0)
    HOUR BITS: [1, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 68 BolusWizard 2013-07-08T21:47:19 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 30,
 '_byte[7]': 0,
 'bg': 264,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 3.0,
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
    0000   0x5b 0x08                                  [.
    decimal
             91    8
    datetime (2013-07-08T21:47:19)
    0000   0x53 0xef 0x15 0x08 0x0d                   S....
    body (13)
    hex
    0000   0x00 0x51 0x0d 0x2d 0x6a 0x1e 0x00 0x00    .Q.-j...
    0008   0x00 0x00 0x00 0x1e 0x7d                   ....}
    decimal
              0   81   13   45  106   30    0    0
              0    0    0   30  125
    HOUR BITS: [1, 1, 1]
#### RECORD 69 UnabsorbedInsulinBolus unknown head[5], body[0] op[0x5c]
###### DECODED
```python
[{'age': 17, 'amount': 0.8, 'curve': 20}]
```
    op hex (5)
    0000   0x5c 0x05 0x20 0x11 0x14                   \. ..
    decimal
             92    5   32   17   20
    datetime (unknown)

    body (0)

#### RECORD 70 Bolus 2013-07-08T21:47:19 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 3.1, 'dual_component': '??', 'programmed': 3.1, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x1f 0x1f 0x00                        ....
    decimal
              1   31   31    0
    datetime (2013-07-08T21:47:19)
    0000   0x53 0xef 0x55 0x08 0x0d                   S.U..
    body (0)
    HOUR BITS: [1, 1, 1]
#### RECORD 71 CalBGForPH 2013-07-08T22:19:24 head[2], body[0] op[0x0a]
###### DECODED
```python
{'amount': 276}
```
    op hex (2)
    0000   0x0a 0x14                                  ..
    decimal
             10   20
    datetime (2013-07-08T22:19:24)
    0000   0x58 0xd3 0x36 0x08 0x8d                   X.6..
    body (0)
    HOUR BITS: [1, 1, 0] YEAR BITS: [1, 0, 0, 0]
#### RECORD 72 BolusWizard 2013-07-08T22:19:45 head[2], body[13] op[0x5b]
###### DECODED
```python
{'_byte[5]': 33,
 '_byte[7]': 0,
 'bg': 276,
 'bg_target_high': 125,
 'bg_target_low': 106,
 'bolus_estimate': 5.7,
 'carb_input': 69,
 'carb_ratio': 13,
 'correction_estimate': 0.1,
 'food_estimate': 5.3,
 'sensitivity': 45,
 'unabsorbed_insulin_count': '??',
 'unabsorbed_insulin_total': 2.9,
 'unknown_byte[10]': 0,
 'unknown_byte[8]': 0}
```
    op hex (2)
    0000   0x5b 0x14                                  [.
    decimal
             91   20
    datetime (2013-07-08T22:19:45)
    0000   0x6d 0xd3 0x16 0x08 0x0d                   m....
    body (13)
    hex
    0000   0x45 0x51 0x0d 0x2d 0x6a 0x21 0x35 0x00    EQ.-j!5.
    0008   0x00 0x1d 0x00 0x39 0x7d                   ...9}
    decimal
             69   81   13   45  106   33   53    0
              0   29    0   57  125
    HOUR BITS: [1, 1, 0]
#### RECORD 73 UnabsorbedInsulinBolus unknown head[8], body[0] op[0x5c]
###### DECODED
```python
[{'age': 35, 'amount': 3.1, 'curve': 4},
 {'age': 49, 'amount': 0.8, 'curve': 20}]
```
    op hex (8)
    0000   0x5c 0x08 0x7c 0x23 0x04 0x20 0x31 0x14    \.|#. 1.
    decimal
             92    8  124   35    4   32   49   20
    datetime (unknown)

    body (0)

#### RECORD 74 LowReservoir 2013-07-08T22:20:53 head[2], body[0] op[0x34]
###### DECODED
```python
{'amount': 10.0}
```
    op hex (2)
    0000   0x34 0x64                                  4d
    decimal
             52  100
    datetime (2013-07-08T22:20:53)
    0000   0x75 0xd4 0x16 0x08 0x0d                   u....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 75 Bolus 2013-07-08T22:19:45 head[4], body[0] op[0x01]
###### DECODED
```python
{'amount': 5.7, 'dual_component': '??', 'programmed': 5.7, 'type': '??'}
```
    op hex (4)
    0000   0x01 0x39 0x39 0x00                        .99.
    decimal
              1   57   57    0
    datetime (2013-07-08T22:19:45)
    0000   0x6d 0xd3 0x56 0x08 0x0d                   m.V..
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 76 MResultTotals (2013, 0, 8, 4, 5, 0) head[2], body[0] op[0x07]

    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime ((2013, 0, 8, 4, 5, 0))
    0000   0x00 0x05 0x04 0x68 0x8d                   ...h.
    body (0)
    DAY BITS: [0, 1, 1] YEAR BITS: [1, 0, 0, 0]
#### RECORD 77 Model522ResultTotals 2013-07-09T00:00:00 head[1], body[41] op[0x6d]

    op hex (1)
    0000   0x6d                                       m
    decimal
            109
    datetime (2013-07-09T00:00:00)
    0000   0x68 0x8d                                  h.
    body (41)
    hex
    0000   0x05 0x10 0xcd 0x4a 0x14 0x03 0x00 0x00    ...J....
    0008   0x05 0x04 0x03 0x84 0x46 0x01 0x80 0x1e    ....F...
    0010   0x00 0x59 0x01 0x80 0x1e 0x00 0xf4 0x40    .Y.....@
    0018   0x00 0x8c 0x24 0x00 0x00 0x00 0x03 0x01    ..$.....
    0020   0x01 0x01 0x00 0x0c 0x00 0xe8 0x00 0x00    ........
    0028   0x00                                       .
    decimal
              5   16  205   74   20    3    0    0
              5    4    3  132   70    1  128   30
              0   89    1  128   30    0  244   64
              0  140   36    0    0    0    3    1
              1    1    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0]
#### RECORD 78 PumpSuspend 2013-07-09T15:00:43 head[2], body[0] op[0x1e]

    op hex (2)
    0000   0x1e 0x00                                  ..
    decimal
             30    0
    datetime (2013-07-09T15:00:43)
    0000   0x6b 0xc0 0x0f 0x09 0x0d                   k....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 79 PumpResume 2013-07-09T15:23:50 head[2], body[0] op[0x1f]

    op hex (2)
    0000   0x1f 0x00                                  ..
    decimal
             31    0
    datetime (2013-07-09T15:23:50)
    0000   0x72 0xd7 0x0f 0x09 0x0d                   r....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 80 Rewind 2013-07-09T16:00:12 head[2], body[0] op[0x21]

    op hex (2)
    0000   0x21 0x00                                  !.
    decimal
             33    0
    datetime (2013-07-09T16:00:12)
    0000   0x4c 0xc0 0x10 0x09 0x0d                   L....
    body (0)
    HOUR BITS: [1, 1, 0]
#### RECORD 81 Prime 2013-07-09T16:01:25 head[5], body[0] op[0x03]
###### DECODED
```python
{'amount': 1.7, 'fixed': 0.0, 'type': 'manual'}
```
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x11                   .....
    decimal
              3    0    0    0   17
    datetime (2013-07-09T16:01:25)
    0000   0x59 0xc1 0x30 0x09 0x0d                   Y.0..
    body (0)
    HOUR BITS: [1, 1, 0]
`end analysis/bewest-pump/fall-2013//ReadHistoryData-page-7.data: 82 records`
